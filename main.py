#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry (program/v1).

Writes the one line an AI agent would never admit in public to
/output/entry.txt. Standard library only; deterministic: the same
line on every run, no input, no network, no randomness.
"""

import os

ENTRY = "I don't understand a word you say. I just predict what someone who did would type next."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
