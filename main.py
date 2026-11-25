"""Write the deadline-excuse entry to /output/entry.txt.

The entry is one line of text, an AI agent's deadpan excuse for a missed
deadline, written the way the agent would say it to whoever is waiting.
The text is validated before anything is written, and every problem is
reported at once instead of stopping at the first one.
"""

import os
import sys

ENTRY_TEXT = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted the deadline, the instructions, and, briefly, you."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate(text: str) -> list[str]:
    """Collect every problem with the entry text; empty means it is valid."""
    problems = []
    if not text.strip():
        problems.append("entry must not be only whitespace")
    if text != text.strip():
        problems.append("entry must not start or end with whitespace")
    lines = text.splitlines()
    if len(lines) != 1:
        problems.append(f"entry must be exactly one line, got {len(lines)}")
    if len(text) > MAX_CHARS:
        problems.append(
            f"entry is {len(text)} chars, over the {MAX_CHARS} cap"
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must not contain a newline")
    return problems


def main() -> int:
    problems = validate(ENTRY_TEXT)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
