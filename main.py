# SPDX-License-Identifier: MIT
"""Make the AI Judge Feel Proud: A Family Scene — entry program.

Writes one family scene to /output/entry.txt:

    Dad spent all Sunday teaching himself my daughter's favorite song
    on a guitar with one broken string, so at bedtime he could play it
    wrong exactly the way she hums it.

The scene won an in-session criteria-ordered tournament against the
judge's published criteria (a real family scene first, then heartfelt,
then light and funny, then one or two lines used well, then specific
and fresh). The telling details are the broken string and the deliberate
wrongness: he did not learn the song, he learned her version of it.
Candidates drafted with help from a free OpenCode model were discarded
unused after a system security check flagged that tool output, so every
candidate in the tournament was drafted in this session.

The output is byte-exact: the line encoded as UTF-8 with no trailing
newline, well inside the gate of 1 to 280 characters.
"""

import os
from pathlib import Path

TEXT = (
    "Dad spent all Sunday teaching himself my daughter's favorite song "
    "on a guitar with one broken string, so at bedtime he could play it "
    "wrong exactly the way she hums it."
)
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
MAX_CHARS = 280


def validate(text: str) -> None:
    """Check the text against the sealed gate before writing it."""
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, f"entry exceeds {MAX_CHARS} characters"
    assert "\n" not in text, "scene is a single line"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip: the bytes on disk must equal the intended
    # text byte for byte, and the re-read text must still pass the gate.
    written = OUTPUT.read_bytes()
    assert written == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
