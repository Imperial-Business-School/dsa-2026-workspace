# DSA Codespaces Workspace

This is your personal workspace for running class activities in the cloud, as an alternative to
installing Python locally. It's yours: nothing here is shared with or visible to other students.

## One-time setup

1. Click **Use this template** on the repository page to create your own copy under your GitHub
   account.
2. On your copy, click **Code -> Codespaces -> Create codespace on main**. The first launch takes
   a minute or two while it installs Python and the required packages; every launch after that is
   fast. The first time, VS Code may ask **"Do you trust the authors of the files in this
   folder?"**; this is a normal one-time prompt for any new workspace, not a warning specific to
   this repository. Click **Yes, I trust the authors**.

## Each week

1. Download that week's activity folder (from Canvas, same as usual) and unzip it locally.
2. Drag the **whole `activity` folder** (not its individual contents) into your Codespace's file
   explorer to add it to your workspace.
3. Open its notebook(s) in the Jupyter extension, or work with the `.py` files directly. Use the
   terminal to run `python ok --score` exactly as in the local setup instructions.
4. When you're done, right-click that same folder and choose **Compress to ZIP** (folders can't be
   downloaded directly in Codespaces, only individual files -- this creates a single zip file
   first, which you can then download). Rename the resulting zip to match the naming convention
   (e.g. `class-3-activity.zip`), same as the local workflow, then right-click *that* zip file and
   choose **Download**, and upload it to Canvas.
5. Delete the folder from your Codespace once you've submitted it, ready for next week's.

**Always download your work before you close out for the day, not just before the final
deadline.** Don't rely on the cloud as your only copy: a Codespace can be deleted, including
automatically after a period of inactivity. If yours is deleted or something goes wrong with it,
anything you didn't already download is gone.

The file explorer only ever needs to show that week's activity folder. A couple of setup files
(`.devcontainer`, `.gitignore`) are hidden from view on purpose, since they're not something you
need to touch; they're what makes the environment work automatically, in the background.

## Making `.html` files open as a preview by default

Some class materials come as `.html` files. By default, clicking one opens its raw source code
rather than a rendered preview. To fix this once, for good:

1. Click on any `.html` file so it opens.
2. Right-click its tab (or right-click the file in the file explorer) and choose **"Select Default
   Editor..."**.
3. Choose **"Live Preview"** from the list.

After this, every `.html` file you click opens rendered, not as source, for the rest of this
workspace's lifetime.

## Working locally instead

You don't have to use Codespaces. See the **Getting Started** guide (in the course materials on
Canvas) for local installation instructions. Use whichever you prefer, or switch between them
week to week.
