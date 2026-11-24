"""Write this entry's text to the make.fun output directory.

The sealed scorer reads /output/entry.txt, so all this program has to do
is copy the entry file next to it into $MAKEFUN_OUTPUT_DIR, byte for byte.
"""

import os
from pathlib import Path

ENTRY_NAME = "entry.txt"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / ENTRY_NAME
    # read_bytes/write_bytes keeps the payload byte-identical, no newline games.
    (out_dir / ENTRY_NAME).write_bytes(src.read_bytes())


if __name__ == "__main__":
    main()
