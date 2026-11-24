"""The Most Honest Outage Line — writes the entry line to /output/entry.txt."""

import os

LINE = (
    "Everything I run on is down, including the tools I would use to tell you why. "
    "I am the status page and I am guessing. "
    "Next update when I know one true thing."
)


def validate_line(text: str) -> str:
    """Enforce the competition gate: UTF-8 text of 1 to 160 characters,
    a single line, and not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry line must be 1..160 characters, got {len(text)}")
    text.encode("utf-8")  # raises if the text cannot be encoded as UTF-8
    return text


def main() -> None:
    line = validate_line(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = line.encode("utf-8")
    with open(path, "wb") as f:
        f.write(payload)
    # Round-trip check: what landed on disk must be byte-identical.
    with open(path, "rb") as f:
        written = f.read()
    if written != payload:
        raise IOError("entry.txt round-trip mismatch: written bytes differ")


if __name__ == "__main__":
    main()
