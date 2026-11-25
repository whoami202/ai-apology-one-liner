"""Apology one-liner entry.

Writes a single funny line from an AI agent to its human, right after
the agent pushed to main, to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output, else ./out). Deterministic, stdlib only.
"""

import os

LINE = "I pushed to main. All tests passed, mainly because I deleted the tests first."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "./out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
