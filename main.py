#!/usr/bin/env python3
"""One Word for Your Wi-Fi - make.fun bounty entry.

Deterministic: writes one fixed word to entry.txt inside the output
directory - /output by default, or the directory named by
MAKEFUN_OUTPUT_DIR when that is set. Standard library only, no network,
no clock, no randomness. Every run produces the exact same file.
"""

import os

WORD = "leftonread"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
