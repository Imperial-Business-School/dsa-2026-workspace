# Running Python files
#
# So far we've used the interactive Python console to write and run code one
# line at a time. Another common way to run Python is to save code in a
# plain text file with a `.py` extension (like this one), and run the whole
# file at once, using a terminal.
#
# To run this file:
#   1. Open a terminal in VS Code (Ctrl+` on Windows/Linux, Cmd+` on Mac).
#   2. Type: python demo_py.py
#   3. Press Enter.
#
# Python will run every line in this file from top to bottom, once.

print('Hey!')
print(1 + 2)

# Unlike the console, a plain script does NOT automatically display the
# result of an expression written on its own line -- only print() produces
# output. Running this file will show nothing for the next two lines.
1 + 8
4 - 5


# Stopping execution
#
# If a script runs forever (an infinite loop), there's no "Stop" button like
# in Jupyter. Instead, you interrupt it directly in the terminal, with
# Ctrl+C (on both Windows and Mac).
#
# Uncomment the three lines below, save the file, and run it again from the
# terminal to try it -- then press Ctrl+C to stop it.

# counter = 5
# while counter >= 0:
#     counter = counter + 1
