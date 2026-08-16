#!/usr/bin/env python3
"""
strip-bidi.py — Clean text copied from Bayan thesis PDF.

Cleans:
1. Invisible Unicode Bidirectional Control Characters
   (U+202A/B/C/D/E, U+200E/F, U+2066/7/8/9)
2. Arabic Presentation Forms (U+FB50–U+FDFF, U+FE70–U+FEFF)
   → normalized to basic Arabic (U+0600–U+06FF) via NFKC.

USAGE
=====
  python3 scripts/strip-bidi.py input.txt -o clean.txt
  cat input.txt | python3 scripts/strip-bidi.py > clean.txt
  pdftotext main.pdf - | python3 scripts/strip-bidi.py > clean.txt
"""

import sys
import argparse
import unicodedata

BIDI_CONTROLS = {
    "\u202a", "\u202b", "\u202c", "\u202d", "\u202e",
    "\u200e", "\u200f",
    "\u2066", "\u2067", "\u2068", "\u2069",
}


def strip_bidi(text: str) -> str:
    """Remove bidi control characters and normalize Arabic."""
    for ch in BIDI_CONTROLS:
        text = text.replace(ch, "")
    # NFKC normalization converts Presentation Forms to basic Arabic
    text = unicodedata.normalize("NFKC", text)
    return text


def main():
    parser = argparse.ArgumentParser(
        description="Strip bidi controls + normalize Arabic from PDF text."
    )
    parser.add_argument("input", nargs="?", default="-",
                        help="Input file (default: stdin)")
    parser.add_argument("-o", "--output", default="-",
                        help="Output file (default: stdout)")
    parser.add_argument("--count", action="store_true",
                        help="Print stats to stderr")
    args = parser.parse_args()

    if args.input == "-":
        text = sys.stdin.read()
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()

    n_bidi = sum(text.count(c) for c in BIDI_CONTROLS)
    n_pres = sum(1 for c in text if 0xFB50 <= ord(c) <= 0xFEFF)

    clean = strip_bidi(text)

    if args.output == "-":
        sys.stdout.write(clean)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(clean)

    if args.count:
        sys.stderr.write(f"Removed {n_bidi} bidi controls\n")
        sys.stderr.write(f"Normalized {n_pres} presentation forms\n")


if __name__ == "__main__":
    main()
