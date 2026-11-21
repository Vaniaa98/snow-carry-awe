#!/usr/bin/env python3
"""Snow Carry -- a short text to relax the AI judge.

Writes the text to /output/entry.txt (UTF-8, 1-280 code points).
"""
import os

TEXT = "Your father carries you through the snow. Night. The snow is falling on his shoulders. On your cheek. It has fallen this way since before the road. His steps are slow. Your cheek is warm against his neck. He walks. The snow is still falling."
# W Snow: the first duel winner (beat #2 @jaden 0.70 via Pecut, drew via Verboo).


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
