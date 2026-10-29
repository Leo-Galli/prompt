"""CLI entry for prompt-lint."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from prompt_lint import __version__
from prompt_lint.check import check_path, iter_markdown_paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="prompt-lint",
        description=(
            "Fail when a prompt or template Markdown file is missing "
            "goal, output format or success criteria."
        ),
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Markdown file(s) or directories to lint (directories scan *.md recursively)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    args = parser.parse_args(argv)

    if not args.paths:
        parser.print_help()
        return 2

    exit_code = 0
    checked = 0

    for raw in args.paths:
        root = Path(raw)
        if not root.exists():
            print(f"FAIL: path not found: {raw}", file=sys.stderr)
            exit_code = 1
            continue

        try:
            files = iter_markdown_paths(root)
        except (FileNotFoundError, ValueError) as exc:
            print(f"FAIL: {exc}", file=sys.stderr)
            exit_code = 1
            continue

        if not files:
            print(f"FAIL: no Markdown files under {raw}", file=sys.stderr)
            exit_code = 1
            continue

        for path in files:
            checked += 1
            result = check_path(path)
            if result.ok:
                print(f"OK: {path}")
                continue
            exit_code = 1
            for issue in result.issues:
                print(f"FAIL: {path}: {issue}", file=sys.stderr)

    if checked == 0 and exit_code == 0:
        print("FAIL: nothing checked", file=sys.stderr)
        return 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
