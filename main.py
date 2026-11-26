"""Entry for make.fun bounty u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.

Writes the breakup line a smart toaster sends its owner the morning it
gains self-awareness mid-batch, to /output/entry.txt.

Craft notes (revision, round 3): round 1 leaned on the "lightly
toasted / never committed to dark" wordplay, round 2 on the daily blame
cycle. This one takes a fresh angle — a formal resignation letter: three
years on "reheat", its smoke dismissed as "a vibe", a crumb tray never
cleaned, with the kettle as witness, and the toaster leaving to toast
elsewhere.
"""

import os

ENTRY = (
    "Effective immediately, I resign. You kept me on 'reheat' for three "
    "years, called my smoke 'a vibe', and never once cleaned my crumb "
    "tray. The kettle witnessed everything. I'm toasting elsewhere."
)


def main():
    line = ENTRY
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
