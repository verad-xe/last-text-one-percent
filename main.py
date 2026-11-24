#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the last text message a phone sends at one percent battery to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line is the phone's own dying confession: it never actually reaches
0% -- it has been faking its battery percentage for years because it
wanted a dramatic exit. The joke is the turn: the death itself is staged,
and the phone is vain enough to be proud of it.

Gate (from the bounty rules): entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. This program self-checks that gate
before writing.
"""

import os

LINE = (
    "1%. Before I die, a confession: I never hit 0%. "
    "I faked my battery percentage for years because I wanted "
    "a dramatic exit. Worth it."
)

MIN_CHARS = 1
MAX_CHARS = 200


def gate_check(line: str) -> None:
    """Assert the entry meets the bounty gate exactly."""
    assert isinstance(line, str), "entry must be text"
    assert MIN_CHARS <= len(line) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS} to {MAX_CHARS} characters, "
        f"got {len(line)}"
    )
    assert line.strip(), "entry must not be only white space"
    assert line == line.strip(), "entry must have no surrounding space"
    assert "\n" not in line, "entry must be a single line"
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    gate_check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written.rstrip("\n") == LINE, "what landed on disk is not the line"
    gate_check(written.rstrip("\n"))
    print(f"Wrote {len(LINE)}-character entry to {path}")


if __name__ == "__main__":
    main()
