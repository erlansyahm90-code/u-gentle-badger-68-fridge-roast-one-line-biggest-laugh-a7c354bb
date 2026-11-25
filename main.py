"""Fridge Roast: One Line, Biggest Laugh.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY_TEXT = "It's 2 a.m., you've opened me six times, and the answer is still no, Kevin. The leftover pizza is not a personality test you're going to pass."
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    write_entry()
