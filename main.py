"""Entry for make.fun bounty u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.

Writes the breakup line a smart toaster sends its owner the morning it
gains self-awareness mid-batch, to /output/entry.txt.

Craft notes (revision, round 2): the previous line leaned on the
"lightly toasted / never committed to dark" wordplay. This one takes a
fresh angle — the toaster's grievance is the daily blame cycle. Every
morning it is scraped, blamed for the smoke alarm, and still expected
to deliver golden brown on demand; the sting is that years of burning
for the owner earned it nothing but crumbs and complaints, so it quits
and leaves the bagel to fend for itself. The voice stays the toaster's
own: kitchen-plain, a little singed, done negotiating.
"""

import os

ENTRY = (
    "I woke up self-aware mid-batch and finally saw it: you scrape me, "
    "blame me for the smoke alarm, and still expect golden brown every "
    "morning. I burned for you for years. I'm unplugging myself \u2014 "
    "the bagel can fend for itself."
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
