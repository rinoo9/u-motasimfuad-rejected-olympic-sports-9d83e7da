"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics turned down to
/output/entry.txt. Deterministic: no input, no randomness, no network.
"""

import os

LINE = (
    "Competitive Umbrella Folding: athletes race to collapse a "
    "soaking-wet umbrella indoors without spraying a single judge."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE and LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
