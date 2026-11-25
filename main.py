"""Entry for make.fun bounty u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.

Writes the breakup line a smart toaster sends its owner the morning it
gains self-awareness mid-batch, to /output/entry.txt.
"""

import os

ENTRY = "You kept me on 'lightly toasted' for 2,847 mornings — I burned for you and you never once committed to dark. I'm unplugging myself. The crumbs are yours now."


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
