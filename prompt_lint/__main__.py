"""CLI entry for prompt-lint (skeleton)."""

from __future__ import annotations

import argparse
import sys

from prompt_lint.check import check_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="prompt-lint",
        description="Fail when a prompt is missing goal, output format or success criteria.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to a prompt or template Markdown file",
    )
    args = parser.parse_args(argv)

    if not args.path:
        parser.print_help()
        return 2

    with open(args.path, encoding="utf-8") as handle:
        text = handle.read()

    result = check_text(text)
    if result.ok:
        print(f"OK: {args.path}")
        return 0

    for issue in result.issues:
        print(f"FAIL: {issue}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
