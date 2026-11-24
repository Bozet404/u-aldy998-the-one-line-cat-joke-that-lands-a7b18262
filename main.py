#!/usr/bin/env python3
"""One-line cat joke entry.

Writes a single joke line about cats to /output/entry.txt.
The joke is one line, under 200 characters, and nothing else.
"""

from pathlib import Path

JOKE = "My cat sprints down the hallway at 3 a.m. like the rent is due, then falls asleep on my face like she earned every minute of it."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
