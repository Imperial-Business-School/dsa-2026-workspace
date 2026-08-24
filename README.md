# DSA Codespaces Workspace

This is your personal workspace for running class activities in the cloud, as an alternative to
installing Python locally. It's yours: nothing here is shared with or visible to other students.

## One-time setup

1. Click **Use this template** on the repository page to create your own copy under your GitHub
   account.
2. On your copy, click **Code -> Codespaces -> Create codespace on main**. The first launch takes
   a minute or two while it installs Python and the required packages; every launch after that is
   fast.

## Each week

1. Download that week's activity folder (from Canvas, same as usual) and unzip it locally.
2. In your Codespace, drag the unzipped folder into the file explorer on the left to add it to
   your workspace.
3. Open its notebook(s) in the Jupyter extension, or work with the `.py` files directly. Use the
   terminal to run `python ok --score` exactly as in the local setup instructions.
4. When you're done, select the folder in the file explorer, right-click, and choose **Download**.
   This downloads it as a zip you can upload to Canvas, same as the local workflow.
5. Delete that week's folder from your Codespace once you've submitted it, ready for next week's.

The file explorer only ever needs to show that week's activity folder. A couple of setup files
(`.devcontainer`, `.gitignore`) are hidden from view on purpose, since they're not something you
need to touch; they're what makes the environment work automatically, in the background.

## Working locally instead

You don't have to use Codespaces. See the **Getting Started** guide (in the course materials on
Canvas) for local installation instructions. Use whichever you prefer, or switch between them
week to week.
