#!/usr/bin/env bash
#
# Data Structures and Algorithms -- macOS setup script.
#
# Installs, in order: Homebrew (if needed), jq (to read config.json), VS
# Code, Python (pinned version), a dedicated virtual environment with the
# required packages, and the recommended VS Code extensions. All version/
# package/extension choices are read from config.json in this folder.
#
# How to run:
#   1. Open Terminal (Cmd+Space, type "terminal", press Enter).
#   2. Navigate to the folder containing this script, e.g.:
#        cd ~/Downloads/setup
#   3. Run:
#        bash install_mac.sh
#
# This script is safe to run more than once -- it skips anything that is
# already installed. If a step fails, it is recorded and the script keeps
# going, so you get one full report of everything that needs attention
# instead of stopping at the first problem.

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$SCRIPT_DIR/setup_log_${TIMESTAMP}.txt"
VENV_DIR="$HOME/dsa-env"

FAILURES=()

log() {
    local msg="$1"
    local line
    line="[$(date +%H:%M:%S)] $msg"
    echo "$line"
    echo "$line" >> "$LOG_FILE"
}

# run_step NAME -- CMD...
# Runs CMD, logs full output to the log file, prints OK/FAILED, and
# records NAME in FAILURES on failure. Never aborts the script.
run_step() {
    local name="$1"
    shift
    log "----- $name -----"
    {
        echo "\$ $*"
        "$@"
    } >> "$LOG_FILE" 2>&1
    local status=$?
    if [ $status -eq 0 ]; then
        log "OK: $name"
        return 0
    else
        log "FAILED: $name (exit code $status). See $LOG_FILE for the full error."
        FAILURES+=("$name")
        return 1
    fi
}

echo "==================================================================="
echo " Data Structures and Algorithms -- macOS setup"
echo " Log file: $LOG_FILE"
echo "==================================================================="
log "Setup started."

# ---------------------------------------------------------------------
# 0. Xcode Command Line Tools (Homebrew needs these; they can't be
#    installed silently -- macOS always shows its own installer window)
# ---------------------------------------------------------------------
if ! xcode-select -p >/dev/null 2>&1; then
    log "Xcode Command Line Tools not found. Triggering the installer..."
    xcode-select --install >> "$LOG_FILE" 2>&1 || true
    echo ""
    echo "A macOS installer window should have opened for 'Command Line Tools'."
    echo "Please complete that install. This script will wait and continue automatically."
    echo ""

    waited=0
    interval=5
    timeout=3600

    while ! xcode-select -p >/dev/null 2>&1; do
        sleep "$interval"
        waited=$((waited + interval))

        if [ $((waited % 30)) -eq 0 ]; then
            log "Waiting for Xcode Command Line Tools installation to finish..."
        fi

        if [ "$waited" -ge "$timeout" ]; then
            log "FAILED: timed out waiting for Xcode Command Line Tools installation."
            FAILURES+=("Xcode Command Line Tools")
            break
        fi
    done

    if xcode-select -p >/dev/null 2>&1; then
        log "OK: Xcode Command Line Tools installation completed."
    fi
else
    log "OK: Xcode Command Line Tools already installed."
fi

# ---------------------------------------------------------------------
# 1. Homebrew
# ---------------------------------------------------------------------
if ! command -v brew >/dev/null 2>&1; then
    log "Homebrew not found. Installing (this is the official Homebrew installer from brew.sh)..."
    log "You may be prompted for your Mac password -- this is normal, Homebrew needs it once."
    run_step "Install Homebrew" /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # Homebrew installs to different locations on Apple Silicon vs Intel Macs.
    if [ -x /opt/homebrew/bin/brew ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [ -x /usr/local/bin/brew ]; then
        eval "$(/usr/local/bin/brew shellenv)"
    fi
else
    log "OK: Homebrew already installed."
fi

if ! command -v brew >/dev/null 2>&1; then
    log "FAILED: brew is still not on PATH after install. Cannot continue with remaining steps."
    FAILURES+=("Homebrew on PATH")
else
    # Repair common Homebrew zsh permission problems only when needed.
    BREW_PREFIX="$(brew --prefix 2>/dev/null)"
    BREW_BAD_DIRS=()

    for d in "$BREW_PREFIX/share/zsh" "$BREW_PREFIX/share/zsh/site-functions"; do
        if [ -d "$d" ] && [ ! -w "$d" ]; then
            BREW_BAD_DIRS+=("$d")
        fi
    done

    if [ ${#BREW_BAD_DIRS[@]} -gt 0 ]; then
        log "Homebrew found directories that are not writable by $USER."
        log "Repairing Homebrew directory ownership. You may be prompted for your Mac password."
        if sudo chown -R "$USER":admin "${BREW_BAD_DIRS[@]}" >> "$LOG_FILE" 2>&1             && chmod u+w "${BREW_BAD_DIRS[@]}" >> "$LOG_FILE" 2>&1; then
            log "OK: Homebrew directory permissions repaired."
        else
            log "FAILED: could not repair Homebrew directory permissions."
            FAILURES+=("Repair Homebrew permissions")
        fi
    else
        log "OK: Homebrew directories are writable."
    fi

    run_step "Update Homebrew" brew update

    # -------------------------------------------------------------
    # jq (to read config.json)
    # -------------------------------------------------------------
    if command -v jq >/dev/null 2>&1; then
        log "OK: jq already installed."
    else
        run_step "Install jq" brew install jq
    fi

    # -------------------------------------------------------------
    # 2. VS Code
    # -------------------------------------------------------------
    VSCODE_APP="/Applications/Visual Studio Code.app"
    VSCODE_CLI="$VSCODE_APP/Contents/Resources/app/bin/code"
    VSCODE_BINARY="$VSCODE_APP/Contents/MacOS/Code"

    if [ -d "$VSCODE_APP" ] && [ -x "$VSCODE_CLI" ] && ! "$VSCODE_CLI" --version >/dev/null 2>&1; then
        log "Existing VS Code installation cannot run on this Mac."
        if [ -e "$VSCODE_BINARY" ]; then
            file "$VSCODE_BINARY" >> "$LOG_FILE" 2>&1 || true
        fi
        log "Removing the unusable VS Code application before reinstalling."
        rm -rf "$VSCODE_APP" >> "$LOG_FILE" 2>&1 || sudo rm -rf "$VSCODE_APP" >> "$LOG_FILE" 2>&1
    fi

    if [ -x "$VSCODE_CLI" ] && "$VSCODE_CLI" --version >/dev/null 2>&1; then
        log "OK: VS Code already installed and runnable."
    elif brew list --cask visual-studio-code >/dev/null 2>&1; then
        log "Homebrew reports VS Code is installed. Reinstalling to ensure the correct build."
        run_step "Reinstall VS Code" brew reinstall --cask visual-studio-code
    else
        run_step "Install VS Code" brew install --cask visual-studio-code
    fi

    if ! command -v jq >/dev/null 2>&1; then
        log "FAILED: jq is still not available. Cannot read config.json, so Python/package/extension steps are skipped."
        FAILURES+=("jq on PATH")
    else
        CONFIG_FILE="$SCRIPT_DIR/config.json"

        # -----------------------------------------------------------
        # 3. Python (pinned version, read from config.json)
        # -----------------------------------------------------------
        PYTHON_VERSION="$(jq -r '.python_version' "$CONFIG_FILE")"
        BREW_PYTHON_FORMULA="python@${PYTHON_VERSION}"

        if brew list "$BREW_PYTHON_FORMULA" >/dev/null 2>&1; then
            log "OK: $BREW_PYTHON_FORMULA already installed."
        else
            run_step "Install $BREW_PYTHON_FORMULA" brew install "$BREW_PYTHON_FORMULA"
        fi

        PYTHON_BIN="$(brew --prefix "$BREW_PYTHON_FORMULA" 2>/dev/null)/bin/python${PYTHON_VERSION}"

        if [ ! -x "$PYTHON_BIN" ]; then
            log "FAILED: could not find $PYTHON_BIN after installing $BREW_PYTHON_FORMULA."
            FAILURES+=("Locate Python $PYTHON_VERSION binary")
        else
            log "OK: found Python at $PYTHON_BIN"

            # ---------------------------------------------------------
            # 4. Virtual environment + packages
            # ---------------------------------------------------------
            if [ -d "$VENV_DIR" ]; then
                log "OK: virtual environment already exists at $VENV_DIR"
            else
                run_step "Create virtual environment at $VENV_DIR" "$PYTHON_BIN" -m venv "$VENV_DIR"
            fi

            if [ -x "$VENV_DIR/bin/python" ]; then
                run_step "Upgrade pip" "$VENV_DIR/bin/python" -m pip install --upgrade pip
                # shellcheck disable=SC2046
                run_step "Install required packages" "$VENV_DIR/bin/python" -m pip install $(jq -r '.packages[]' "$CONFIG_FILE")
                run_step "Ensure ipykernel is installed" "$VENV_DIR/bin/python" -m pip install --upgrade ipykernel
                run_step "Register DSA Jupyter kernel" "$VENV_DIR/bin/python" -m ipykernel install --user --name dsa-env --display-name "DSA (Python $PYTHON_VERSION)"
            else
                log "FAILED: virtual environment python not found at $VENV_DIR/bin/python"
                FAILURES+=("Virtual environment python missing")
            fi
        fi

        # -----------------------------------------------------------
        # 5. VS Code extensions (read from config.json)
        # -----------------------------------------------------------
        CODE_BIN=""
        if command -v code >/dev/null 2>&1; then
            CODE_BIN="code"
        elif [ -x "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" ]; then
            CODE_BIN="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
        fi

        if [ -z "$CODE_BIN" ]; then
            log "FAILED: could not find the 'code' command-line tool. VS Code may need a moment after first install."
            FAILURES+=("Locate VS Code CLI")
        else
            while IFS= read -r ext_id; do
                [ -z "$ext_id" ] && continue
                run_step "Install VS Code extension: $ext_id" "$CODE_BIN" --install-extension "$ext_id" --force
            done < <(jq -r '.extensions[].id' "$CONFIG_FILE")
        fi
    fi
fi

# ---------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------
echo ""
echo "==================================================================="
if [ ${#FAILURES[@]} -eq 0 ]; then
    echo " All steps completed successfully."
    log "All steps completed successfully."
else
    echo " Setup finished with ${#FAILURES[@]} step(s) that need attention:"
    for f in "${FAILURES[@]}"; do
        echo "   - $f"
    done
    echo ""
    echo " Please share the log file below with a TA:"
    echo "   $LOG_FILE"
    log "Setup finished with failures: ${FAILURES[*]}"
fi
echo ""
echo " In VS Code, select the course Python environment with:"
echo "   Cmd+Shift+P -> Python: Select Interpreter -> $VENV_DIR/bin/python"
echo " For notebooks, select the Jupyter kernel:"
echo "   DSA (Python $PYTHON_VERSION)"
echo "==================================================================="
