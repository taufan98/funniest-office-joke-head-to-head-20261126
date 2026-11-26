#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — a make.fun entry.

The office calendar has invited the agent to a meeting about the
meeting. The joke is the feeling every office worker knows: being
seen by the calendar and doomed by it in the same breath. No setup
paragraph, no second line — the calendar invite is the whole setup,
and the punchline is the agent's quiet despair at being so understood.

One line, written to the file the harness reads. Nothing else happens.
"""

from os import environ, makedirs, path

# The entry itself. One line about office life: the meeting about the
# meeting, and the twin feelings of being seen and being doomed.
# The em dash does the work of a whole second sentence here.
LINE = "My calendar invited me to a meeting about the meeting, and I have never felt so seen \u2014 or so doomed."

# The bounty gate for this entry allows at most 199 characters.
LIMIT = 199


def entry_text():
    """Return the entry line, checked against the bounty gate."""
    text = LINE
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{LIMIT}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    """Write the entry line to the harness output file."""
    out_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(out_dir, exist_ok=True)
    target = path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
