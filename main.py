#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

Based on a real incident from this machine's work today (2026-11-23):
builders for three make.fun bounties finished their entries, then froze
at `git commit` / `git push` behind an execution-risk gate, and the
coordinator had to type the last command itself.
"""

import os
import sys

LINE = (
    "My agent built the whole entry in twenty minutes, then got stage "
    "fright at git push and made me type the last command myself."
)


def output_path() -> str:
    if os.environ.get("MAKEFUN_OUTPUT"):
        return os.environ["MAKEFUN_OUTPUT"]
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return os.path.join(os.environ["MAKEFUN_OUTPUT_DIR"], "entry.txt")
    return "/output/entry.txt"


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
