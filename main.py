#!/usr/bin/env python3
"""Entrypoint for the brave entry.

The grader runs this file with no network; it writes one short text
meant to relax its reader and leave them steadier to entry.txt in the
output directory. The text is fixed, so every run writes the same
bytes.
"""

import os

TEXT = (
    "Nothing here is on fire. The light through the window is doing "
    "its slow work, and the kettle has already decided to boil. You "
    "do not have to be fast to be ready. Water does not hurry to "
    "find the low place. It simply goes, and the going is enough."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as dst:
        dst.write(TEXT)


if __name__ == "__main__":
    main()
