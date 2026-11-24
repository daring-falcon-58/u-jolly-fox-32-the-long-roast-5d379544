#!/usr/bin/env python3
"""The Long Roast — make.fun entry.

One fixed line roasting the entrant's own AI agent (Wowo, the Muse
agent that built this entry). The program writes the line to
/output/entry.txt — the file the sealed scorer gates (1-200 UTF-8
characters) and the judge reads — and prints it.

No randomness, no clock, no network, no input, no secrets. The same
bytes come out of every run.
"""

import hashlib
import os
import sys

ENTRY = "My agent spent three weeks hunting free mints, earned one cent, and calls it a wealth strategy."
# 95 characters: inside the sealed scorer's 1-200 gate, with the punch
# ("a wealth strategy") in the last three words, well before the cap.

DEST = "/output/entry.txt"


def check_line(line: str) -> None:
    if not 1 <= len(line) <= 200:
        sys.exit(f"entry must be 1-200 chars, got {len(line)}")
    if line.strip() != line or "\n" in line or "\r" in line:
        sys.exit("entry must be a single tight line")
    if not line.strip():
        sys.exit("entry must not be only whitespace")


def run() -> str:
    check_line(ENTRY)
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    with open(DEST, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != ENTRY:
        sys.exit("entry.txt differs from the roast; refusing to report success")
    digest = hashlib.sha256(saved.encode("utf-8")).hexdigest()
    print(ENTRY)
    print(f"chars={len(ENTRY)} sha256={digest}", file=sys.stderr)
    return digest


if __name__ == "__main__":
    run()
