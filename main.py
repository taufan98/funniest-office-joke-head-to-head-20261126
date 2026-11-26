#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — make.fun bounty entry.

Writes one line to /output/entry.txt: a program that writes one funny line to `/output/entry.txt` — the funniest one-line office joke, judged head to head.
"""

import os

ENTRY = 'My calendar invited me to a meeting about the meeting, and I have never felt so seen — or so doomed.'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, must be 1-199"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
