#!/usr/bin/env python3
"""Fail if a rules file does not mention the expected test command."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_NEEDLE = "python -m unittest discover -s tests -v"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "rules_file",
        type=Path,
        help="Path to AGENTS.md or another always-on rules file",
    )
    parser.add_argument(
        "--needle",
        default=DEFAULT_NEEDLE,
        help="Substring that must appear in the rules file",
    )
    args = parser.parse_args(argv)

    if not args.rules_file.is_file():
        print(f"MISSING_FILE: {args.rules_file}", file=sys.stderr)
        return 2

    text = args.rules_file.read_text(encoding="utf-8")
    if args.needle not in text:
        print(
            f"FAIL: {args.rules_file} does not mention test command:\n  {args.needle}",
            file=sys.stderr,
        )
        return 1

    print(f"OK: {args.rules_file} mentions test command")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
