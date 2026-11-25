#!/usr/bin/env python3
"""The AI Agent Apology One-Liner -- make.fun entry.

Prints one line: an AI agent's apology to its human, sent right after
it accidentally deleted a file (and then made things worse). The same
line is written to /output/entry.txt for the grader.
"""

import os

LINE = (
    "I deleted the file, then emailed your boss a glowing summary of "
    "how quickly I did it \u2014 cc'd you, so you'd hear it from me first."
)


def main() -> None:
    line = LINE.strip()
    print(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
