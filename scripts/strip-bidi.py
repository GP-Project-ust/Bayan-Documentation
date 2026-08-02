#!/usr/bin/env python3
"""
strip-bidi.py — Clean invisible Unicode Bidirectional Control Characters
from text that has been copy-pasted from a PDF generated with the LaTeX
`bidi` + `polyglossia` packages (Arabic / Hebrew documents).

USAGE
=====
  1. From a file:
       python3 scripts/strip-bidi.py input.txt -o clean.txt
       python3 scripts/strip-bidi.py input.txt            # prints to stdout
       cat input.txt | python3 scripts/strip-bidi.py > clean.txt

  2. From clipboard (requires `xclip` or `pbpaste`):
       xclip -o | python3 scripts/strip-bidi.py | xclip -i

WHY THIS IS NEEDED
==================
The LaTeX `bidi` package inserts invisible Unicode control characters into
the PDF content stream so the PDF viewer knows how to visually reorder
mixed LTR/RTL text. Examples:

  U+202A  LEFT-TO-RIGHT EMBEDDING (LRE)
  U+202B  RIGHT-TO-LEFT EMBEDDING (RLE)
  U+202C  POP DIRECTIONAL FORMATTING (PDF)
  U+202D  LEFT-TO-RIGHT OVERRIDE (LRO)
  U+202E  RIGHT-TO-LEFT OVERRIDE (RLO)
  U+200E  LEFT-TO-RIGHT MARK (LRM)
  U+200F  RIGHT-TO-LEFT MARK (RLM)
  U+2066  LEFT-TO-RIGHT ISOLATE (LRI)
  U+2067  RIGHT-TO-LEFT ISOLATE (RLI)
  U+2068  FIRST STRONG ISOLATE (FSI)
  U+2069  POP DIRECTIONAL ISOLATE (PDI)

When you copy text from the PDF, these controls get pasted into your
editor. Modern editors (Word, Google Docs, LibreOffice) usually hide them
silently, but plain-text editors and terminals show them as small boxes,
stray dots, or garbled characters.

This script removes them all, leaving clean text.

It also normalizes Arabic Presentation Forms (U+FB50–U+FDFF,
U+FE70–U+FEFF) to their basic Arabic equivalents (U+0600–U+06FF)
via Unicode NFKC normalization, so that copied text uses the
standard Arabic codepoints that search engines and text editors
expect.
"""

import sys
import argparse
import unicodedata

# All Unicode Bidirectional Control Characters
BIDI_CONTROLS = {
    "\u202a",  # LRE
    "\u202b",  # RLE
    "\u202c",  # PDF
    "\u202d",  # LRO
    "\u202e",  # RLO
    "\u200e",  # LRM
    "\u200f",  # RLM
    "\u2066",  # LRI
    "\u2067",  # RLI
    "\u2068",  # FSI
    "\u2069",  # PDI
}


def strip_bidi(text: str, normalize_arabic: bool = True) -> str:
    """Remove bidi control characters and optionally normalize Arabic.

    Args:
        text: Input text to clean.
        normalize_arabic: If True (default), convert Arabic Presentation
            Forms to their basic Arabic equivalents via NFKC.
    """
    for ch in BIDI_CONTROLS:
        text = text.replace(ch, "")
    if normalize_arabic:
        text = unicodedata.normalize("NFKC", text)
    return text


def main():
    parser = argparse.ArgumentParser(
        description="Strip invisible Unicode bidi control characters from text."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Input file (default: - for stdin)",
    )
    parser.add_argument(
        "-o", "--output",
        default="-",
        help="Output file (default: - for stdout)",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Print the number of removed characters to stderr",
    )
    parser.add_argument(
        "--no-normalize",
        action="store_true",
        help="Skip Arabic Presentation Forms normalization (keep as-is)",
    )
    args = parser.parse_args()

    # Read input
    if args.input == "-":
        text = sys.stdin.read()
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()

    # Count before
    n_before = sum(text.count(c) for c in BIDI_CONTROLS)

    # Strip
    clean = strip_bidi(text, normalize_arabic=not args.no_normalize)

    # Write output
    if args.output == "-":
        sys.stdout.write(clean)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(clean)

    if args.count:
        sys.stderr.write(f"Removed {n_before} bidi control characters\n")


if __name__ == "__main__":
    main()
