"""One-Liner Laugh Lab entry.

Writes our single funny line -- the robot vacuum's excuse for eating a
sock -- to /output/entry.txt, byte for byte, with no trailing newline.
Deterministic: the same bytes every run, no network, no randomness.
"""

from pathlib import Path

# The line itself: a deadpan excuse with a twist -- the vacuum blames its
# own job description, which is exactly the kind of literal-minded
# malfunction a robot would offer as a defence.
PUNCHLINE = (
    "It was striped, it was wriggling, and my job description "
    "literally says 'eat things off the floor'."
)

DESTINATION = Path("/output/entry.txt")

# The sealed gate rejects anything over 200 characters, so refuse loudly
# instead of writing an entry that could never be judged.
MAX_CHARS = 200


def check_length(line: str) -> None:
    """Fail fast if the punchline ever grows past the competition gate."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, gate allows 1-200")


def emit_line() -> None:
    """Persist the punchline as UTF-8 bytes, nothing more, nothing less."""
    check_length(PUNCHLINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(PUNCHLINE.encode("utf-8"))


if __name__ == "__main__":
    emit_line()
