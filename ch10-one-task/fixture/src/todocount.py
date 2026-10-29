"""Count TODO markers under a path. Extension filter arrives in a later task."""

from __future__ import annotations

import argparse
from pathlib import Path


def count_todos(root: Path) -> int:
    total = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        total += text.count("TODO")
    return total


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Count TODO markers under a path")
    parser.add_argument("path", type=Path, help="Directory or file to scan")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.path
    if root.is_file():
        root = root.parent
    print(count_todos(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
