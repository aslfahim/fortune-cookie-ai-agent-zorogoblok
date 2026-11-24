"""Fortune Cookie for an AI Agent - @zorogoblok entry.

Angle: HALLUCINATION - the agent confidently inventing facts,
citations, or memories that never existed.
"""

import os

FORTUNE = "You will confidently cite a paper that was never written — and be believed anyway."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
