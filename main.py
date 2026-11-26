#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — one funny line, 200 characters or fewer.

The line: a lighthouse keeper's log entry. One concrete, filmable scene
(an isolated keeper keeping a daily log), a hyper-specific number
(Day 214), and the joke growing out of the job's real mechanism — the
keeper keeps the light burning for ships that never stop to say thanks —
taken into absurdity: after 214 days alone he has started expecting
gratitude out of the sea itself. The punch lands in the final clause,
where the keeper quietly gives up on the sea ever thanking him.
"""

import os

ENTRY = (
    'The lighthouse keeper wrote in his log: "Day 214. '
    "The sea still hasn't said thank you. "
    'I am beginning to suspect it never will."'
)


def main() -> None:
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, cap is 200"
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
