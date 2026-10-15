#!/usr/bin/env python3
"""
Reset one or more ok questions back to their original (locked) state, so you
can practice them again from scratch. This discards any progress you've made
unlocking or answering the question(s) -- it does not affect your code in
.py files like algo.py, only the tests/ question files.

Usage:
    python3 reset_ok.py            # reset every question in this session
    python3 reset_ok.py q1         # reset just q1
    python3 reset_ok.py q1 q2      # reset q1 and q2
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKUP = HERE / ".tests_backup"
TESTS = HERE / "tests"


def main():
    if not BACKUP.is_dir():
        sys.exit("No backup found (.tests_backup/ missing) -- cannot reset.")

    if len(sys.argv) > 1:
        names = [a if a.endswith(".py") else a + ".py" for a in sys.argv[1:]]
    else:
        names = [p.name for p in sorted(BACKUP.glob("*.py"))]

    reset = 0
    for name in names:
        src = BACKUP / name
        dest = TESTS / name
        if not src.exists():
            print(f"  !! no such question: {name}")
            continue
        shutil.copy2(src, dest)
        print(f"  -- reset {name}")
        reset += 1

    # Clear cached bytecode and local unlock history, or the reset won't
    # actually take effect the next time you run ok.
    for p in TESTS.glob("__pycache__"):
        shutil.rmtree(p, ignore_errors=True)
    for pattern in (".ok_history", ".ok_storage*"):
        for p in HERE.glob(pattern):
            p.unlink(missing_ok=True)

    print(f"Reset {reset} question(s).")


if __name__ == "__main__":
    main()
