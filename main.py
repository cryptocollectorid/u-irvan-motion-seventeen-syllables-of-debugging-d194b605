"""One haiku about debugging, 5-7-5 syllables, written to /output/entry.txt."""

import os

HAIKU = """The breakpoint still waits
cursor blinks at three a.m.
the bug lives in me"""

def main() -> None:
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert 1 <= len(HAIKU) <= 200, "entry must be 1-200 characters"
    assert HAIKU.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(HAIKU)

if __name__ == "__main__":
    main()
