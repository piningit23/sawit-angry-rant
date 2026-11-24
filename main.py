#!/usr/bin/env python3
"""Angry Judge - The Short Rant.

Writes one fixed, deterministic rant about an everyday annoyance to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Standard library
only; no network, clock, randomness or file reads. The rant is 1-400
characters, so it passes the gate.
"""

import os

RANT = (
    "The office printer behaved itself for six months. Today, five "
    "minutes before my deadline, it jammed, blinked twice, and printed a "
    "test page in a language I do not speak. I am now on my knees, "
    "negotiating with a machine that has exactly one job and apparently "
    "a union rep."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = RANT
    if not (1 <= len(text) <= 400) or not text.strip():
        raise SystemExit("rant fails the 1-400 character gate")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
