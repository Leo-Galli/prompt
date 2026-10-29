"""Minimal linecount CLI used by the Chapter 8 companion fixture."""

from __future__ import annotations

import argparse
from pathlib import Path


def count_lines(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if text == "":
        return 0
    return len(text.splitlines())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Count lines in text files.")
    parser.add_argument("paths", nargs="+", type=Path, help="Files to scan")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    total = 0
    file_count = 0
    for path in args.paths:
        total += count_lines(path)
        file_count += 1
    print(total)
    print(f"{file_count} files scanned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
