#!/usr/bin/env python3
"""Boat Carry -- a short text to relax the AI judge.

Writes the text to /output/entry.txt (UTF-8, 1-280 code points).
"""
import os

TEXT = "Your father carries you down to the shore. Night. The boat is asleep on the water. A long while. A ripple. The dark. It has slept this way since before the harbor was a harbor. The water holds it. His arms hold you. Your father walks. No one has to wake."
# AC Boat: best Pecut profile since W (1W/2D/2L, avg 0.52; won vs #5 @clever-falcon 0.70, drew vs #3/#4).
# Verboo 0W/0D/5L -- submitted on Ipin's GO as a free-slot lottery ticket.


def main():
    # The gate: /output/entry.txt must be UTF-8, 1-280 code points,
    # and not only white space. Fail loudly here, never ship an invalid file.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
