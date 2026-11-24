"""Say What Actually Broke — one brutally honest error message.

Writes a single-line error message to /output/entry.txt.
The line names the real failure (out of memory, too many tabs) and
tells the user exactly what to do next, in one memorable sentence.
"""

import os

LINE = "The app ran out of memory opening your 847 tabs. Close a few — even the browser is begging you to stop."

MAX_CHARS = 200


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
