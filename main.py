#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word to /output/entry.txt: the funniest and most accurate
description of the entrant's Wi-Fi.

The word is "Liar". Home Wi-Fi's most universal lived truth is not that it
is slow — it is that it lies: full bars, "Connected", and nothing loads.
The network says one thing and does another, to your face, every day.
As a network name it is funny the instant you read it, needs no setup,
and no other entrant's first word will be it.
"""

import os

WORD = "Liar"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> str:
    """Enforce the competition gate: 1-20 UTF-8 chars, one word, not blank."""
    if not word or word != word.strip():
        raise ValueError("word must not be blank or padded with whitespace")
    if len(word) > 20:
        raise ValueError("word must be at most 20 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    print(f"Wrote one-word entry to {OUTPUT_PATH}: {word!r}")


if __name__ == "__main__":
    main()
