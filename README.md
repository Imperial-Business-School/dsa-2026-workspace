# DSA Codespaces Workspace

This repository is the shared starting point for running class activities in the cloud, as an
alternative to installing Python locally. The repository itself is visible to everyone on the
course, but the **Codespace** you launch from it (where you actually do your work) is private to
you: nobody else can see or access it.

**Note:** this repository's page is publicly viewable, but you'll need to be signed in to GitHub
to create a Codespace from it. See the **Getting Started** guide (in the course materials on
Canvas) for how to register through Imperial's GitHub organisation first.

A few terms used below: your **workspace** is this open project folder in VS Code. The **file
explorer** is the panel of files and folders down the left side of the window. An **extension** is
a small add-on that gives VS Code an extra feature -- Compress to ZIP (used below) and Live
Preview are both extensions. The **terminal** is a text-based command window, opened with
`` Ctrl+` `` (backtick) or `` Cmd+` ``.

## One-time setup

1. On this repository's page, click **Code**, select the **Codespaces** tab, then click the **+**
   icon to create a codespace on `main`. The first
   launch can take up to 5 minutes while it installs Python and the required packages; every
   launch after that is fast. The first time, VS Code may ask **"Do you trust the authors of the
   files in this folder?"**; this is a normal one-time prompt for any new workspace, not a warning
   specific to this repository. Click **Yes, I trust the authors**.
2. If **Compress to ZIP** (used in step 3 below) doesn't appear when you right-click a file the
   very first time you open your Codespace, reload the window using the **Command Palette** (a
   search box for running commands by name -- open it with `Ctrl+Shift+P` on Windows/Linux or
   `Cmd+Shift+P` on Mac, type **"Developer: Reload Window"**, and press Enter) and it'll show up.
   This is normal VS Code behaviour after a fresh install, not a problem with the extension
   itself: an extension's right-click menu entries sometimes don't register until the next reload.

## Each week

1. Download that week's materials from Dropbox (same as usual) and unzip it. Depending on whether
   you downloaded a single class or several together, you may need to look inside a folder or two
   to find it, but find that week's **`activity` folder**.
2. Select everything **inside** that `activity` folder (not the folder itself), and drag those
   files and folders into your Codespace's file explorer, so they land directly in your workspace
   rather than nested inside an extra folder.
3. Open its notebook(s) in the Jupyter extension, or work with the `.py` files directly. Use the
   terminal to run `python ok --score` exactly as in the local setup instructions.
4. When you're done, click into the file explorer and press **Ctrl+A** (Windows/Linux) or
   **Cmd+A** (Mac) to select everything, then right-click and choose **Compress to ZIP**. Rename
   the resulting zip to match the naming convention (e.g. `class-3-activity.zip`), same as the
   local workflow, then right-click that zip file and choose **Download**, and upload it to
   Canvas.
5. **Confirm you actually have the downloaded zip saved locally** (check your Downloads folder)
   before doing anything else. Once you've verified that, delete those files (and the zip) from
   your Codespace, ready for next week's.

**Always download your work before you close out for the day, not just before the final
deadline.** Don't rely on the cloud as your only copy: a Codespace can be deleted, including
automatically after a period of inactivity. If yours is deleted or something goes wrong with it,
anything you didn't already download is gone.

The file explorer only ever needs to show that week's activity folder. A couple of setup files
(`.devcontainer`, `.gitignore`) are hidden from view on purpose, since they're not something you
need to touch; they're what makes the environment work automatically, in the background.

## Working locally instead

You don't have to use Codespaces. See the **Getting Started** guide (in the course materials on
Canvas) for local installation instructions. Use whichever you prefer, or switch between them
week to week.
