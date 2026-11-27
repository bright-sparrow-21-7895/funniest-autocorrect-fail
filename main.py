"""Funniest Autocorrect Fail.

Writes one short original autocorrect fail to /output/entry.txt:
a routine sign-off to a colleague that autocorrect turns into
a confession to the boss, capped by the sender's bleak punchline.
The wrong word is specific and surprising, and the joke lands
on first read without any explanation.
"""

import os

# The entry: a routine sign-off autocorrected into a confession to the boss.
ENTRY = "Texted my boss 'I love you' instead of 'I'll see you tomorrow' — autocorrect really wants me fired."

# The gate requires 1 to 199 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 199


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
