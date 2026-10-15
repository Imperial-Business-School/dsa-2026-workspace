<#
.SYNOPSIS
    Data Structures and Algorithms -- Windows setup script.

.DESCRIPTION
    Installs, in order: VS Code, Python (pinned version), a dedicated
    virtual environment with the required packages, and the recommended
    VS Code extensions. All version/package/extension choices are read
    from config.json in this folder.

    How to run:
      1. Right-click this file and choose "Run with PowerShell".
         (If that option is greyed out, open PowerShell, cd to this folder,
         and run:  .\install_windows.ps1)
      2. If Windows blocks the script ("running scripts is disabled"), open
         PowerShell as yourself (not Administrator) and run this once:
             Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
         then re-run this script.

    This script is safe to run more than once -- it skips anything that is
    already installed. If a step fails, it is recorded and the script keeps
    going, so you get one full report of everything that needs attention
    instead of stopping at the first problem.
#>

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogFile = Join-Path $ScriptDir "setup_log_$Timestamp.txt"
$VenvDir = Join-Path $env:USERPROFILE "dsa-env"
$Failures = New-Object System.Collections.Generic.List[string]

function Write-Log([string]$msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $msg
    Write-Host $line
    Add-Content -Path $LogFile -Value $line
}

# Runs a scriptblock, logs its full output to the log file, prints OK/FAILED,
# and records $Name in $Failures on failure. Never throws -- the caller
# continues to the next step either way.
function Invoke-Step {
    param(
        [string]$Name,
        [scriptblock]$Action
    )
    Write-Log "----- $Name -----"
    try {
        $output = & $Action 2>&1 | Out-String
        Add-Content -Path $LogFile -Value $output
        if ($LASTEXITCODE -ne $null -and $LASTEXITCODE -ne 0) {
            throw "exited with code $LASTEXITCODE"
        }
        Write-Log "OK: $Name"
        return $true
    } catch {
        Write-Log "FAILED: $Name -- $($_.Exception.Message). See $LogFile for details."
        $Failures.Add($Name)
        return $false
    }
}

Write-Host "==================================================================="
Write-Host " Data Structures and Algorithms -- Windows setup"
Write-Host " Log file: $LogFile"
Write-Host "==================================================================="
Write-Log "Setup started."

# ---------------------------------------------------------------------
# 0. winget must be available (ships with Windows 10 1809+ / Windows 11
#    via the "App Installer" package; cannot be silently installed by us)
# ---------------------------------------------------------------------
$wingetOk = $null -ne (Get-Command winget -ErrorAction SilentlyContinue)
if (-not $wingetOk) {
    Write-Log "FAILED: 'winget' was not found."
    Write-Host ""
    Write-Host "Please install 'App Installer' from the Microsoft Store, then re-run this script:"
    Write-Host "  https://apps.microsoft.com/detail/9nblggh4nns1"
    exit 1
} else {
    Write-Log "OK: winget is available."
}

# Load config.json (Python version, packages, extensions) -- PowerShell has
# native JSON support, so no extra tool is needed here (unlike on macOS).
$Config = $null
try {
    $Config = Get-Content (Join-Path $ScriptDir "config.json") -Raw | ConvertFrom-Json
} catch {
    Write-Log "FAILED: could not read/parse config.json -- $($_.Exception.Message)"
    $Failures.Add("Read config.json")
}

# Helper: is a winget package already installed?
function Test-WingetInstalled([string]$Id) {
    $result = winget list --id $Id -e --accept-source-agreements 2>$null
    return ($LASTEXITCODE -eq 0) -and ($result -match [regex]::Escape($Id))
}

# ---------------------------------------------------------------------
# 1. VS Code
# ---------------------------------------------------------------------
if (Test-WingetInstalled "Microsoft.VisualStudioCode") {
    Write-Log "OK: VS Code already installed."
} else {
    Invoke-Step "Install VS Code" {
        winget install -e --id Microsoft.VisualStudioCode --accept-package-agreements --accept-source-agreements
    }
}

# Refresh PATH in this session so newly-installed tools (code, python) are
# visible without needing to reopen PowerShell.
$machinePath = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
$userPath = [System.Environment]::GetEnvironmentVariable("Path", "User")
$env:Path = "$machinePath;$userPath"

if (-not $Config) {
    Write-Log "Skipping Python/package/extension steps because config.json could not be read."
} else {
    # -------------------------------------------------------------
    # 2. Python (pinned version, from config.json)
    # -------------------------------------------------------------
    $PythonVersion = $Config.python_version
    $WingetPythonId = "Python.Python.$PythonVersion"

    if (Test-WingetInstalled $WingetPythonId) {
        Write-Log "OK: Python $PythonVersion already installed."
    } else {
        Invoke-Step "Install Python $PythonVersion" {
            winget install -e --id $WingetPythonId --accept-package-agreements --accept-source-agreements
        }
    }

    # Refresh PATH again after Python install.
    $machinePath = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [System.Environment]::GetEnvironmentVariable("Path", "User")
    $env:Path = "$machinePath;$userPath"

    # Find the Python launcher for the pinned version. The "py" launcher is
    # installed automatically alongside python.org/winget Python builds and is
    # the most reliable way to find a specific version regardless of PATH state.
    $PythonBin = $null
    try {
        $testLauncher = & py "-$PythonVersion" -c "import sys; print(sys.executable)" 2>$null
        if ($LASTEXITCODE -eq 0 -and $testLauncher) {
            $PythonBin = $testLauncher.Trim()
        }
    } catch { }

    if (-not $PythonBin) {
        Write-Log "FAILED: could not locate the Python $PythonVersion executable after install."
        Write-Log "  You may need to close and reopen PowerShell, then re-run this script."
        $Failures.Add("Locate Python $PythonVersion executable")
    } else {
        Write-Log "OK: found Python at $PythonBin"

        # ---------------------------------------------------------
        # 3. Virtual environment + packages
        # ---------------------------------------------------------
        if (Test-Path $VenvDir) {
            Write-Log "OK: virtual environment already exists at $VenvDir"
        } else {
            Invoke-Step "Create virtual environment at $VenvDir" {
                & $PythonBin -m venv $VenvDir
            }
        }

        $VenvPython = Join-Path $VenvDir "Scripts\python.exe"
        if (Test-Path $VenvPython) {
            Invoke-Step "Upgrade pip" {
                & $VenvPython -m pip install --upgrade pip
            }
            Invoke-Step "Install required packages" {
                & $VenvPython -m pip install $Config.packages
            }
        } else {
            Write-Log "FAILED: virtual environment python not found at $VenvPython"
            $Failures.Add("Virtual environment python missing")
        }
    }

    # -------------------------------------------------------------
    # 4. VS Code extensions (from config.json)
    # -------------------------------------------------------------
    $CodeCmd = Get-Command code -ErrorAction SilentlyContinue
    if (-not $CodeCmd) {
        Write-Log "FAILED: could not find the 'code' command-line tool. Try reopening PowerShell and re-running this script."
        $Failures.Add("Locate VS Code CLI")
    } else {
        foreach ($ext in $Config.extensions) {
            $extId = $ext.id
            Invoke-Step "Install VS Code extension: $extId" {
                code --install-extension $extId --force
            }
        }
    }
}

# ---------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------
Write-Host ""
Write-Host "==================================================================="
if ($Failures.Count -eq 0) {
    Write-Host " All steps completed successfully."
    Write-Log "All steps completed successfully."
} else {
    Write-Host " Setup finished with $($Failures.Count) step(s) that need attention:"
    foreach ($f in $Failures) {
        Write-Host "   - $f"
    }
    Write-Host ""
    Write-Host " Please share the log file below with a TA:"
    Write-Host "   $LogFile"
    Write-Log "Setup finished with failures: $($Failures -join ', ')"
}
Write-Host ""
Write-Host " In VS Code, select the course Python environment with:"
Write-Host "   Ctrl+Shift+P -> Python: Select Interpreter -> $VenvDir\Scripts\python.exe"
Write-Host "==================================================================="
