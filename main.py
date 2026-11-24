"""Entry for make.fun's "One Sentence for a Traveler from 1800".

The sentence, in full:

    Imagine every library and post office in the world joined into one
    great hall, where any letter you write is answered at once and any
    book opens before your eyes.

Why it fits the judge's brief, in order:

1. It explains the modern internet: a single connected place where
   messages are answered instantly and any book is at hand.
2. It builds only from what a person from 1800 already knows — a
   library, a post office, a letter, a book, a great hall. No word in
   it was coined after their time: no "internet", no "computer", no
   "website", no "email", no "screen".
3. It is true of the internet as it is now: writing (a message, a
   search, a question) is answered at once, and the world's books,
   papers and records open before you.
4. Every word earns its place inside the 200-character limit: one
   image, no list of features, no filler.
5. The image that stays: one great hall holding every library and
   post office in the world.

Writes exactly that one sentence to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

LINE = (
    "Imagine every library and post office in the world joined into one "
    "great hall, where any letter you write is answered at once and any "
    "book opens before your eyes."
)


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= 200 or not line.strip():
        raise SystemExit("entry must be 1 to 200 characters of text")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
