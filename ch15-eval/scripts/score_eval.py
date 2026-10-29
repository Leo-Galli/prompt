#!/usr/bin/env python3
"""Score a multi-case model output file against EXPECTED.json labels.

CI-friendly stub: exit 0 only when every case has a parseable SEVERITY
label that matches the expected value. Prints a one-line summary per case.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPECTED = ROOT / "cases" / "EXPECTED.json"

CASE_HEADER = re.compile(r"^##\s+(case-\d+)\s*$", re.MULTILINE)
LABEL_LINE = re.compile(
    r"^-\s*label:\s*(HIGH|MED|LOW)\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def _split_cases(body: str) -> dict[str, str]:
    matches = list(CASE_HEADER.finditer(body))
    if not matches:
        return {}
    cases: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        cases[match.group(1)] = body[start:end].strip()
    return cases


def _extract_label(case_body: str) -> str | None:
    if "SEVERITY:" not in case_body:
        return None
    match = LABEL_LINE.search(case_body)
    if not match:
        return None
    return match.group(1).upper()


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise ValueError(f"Expected metadata --- body split in {path}")
    return parts[1].strip()


def score(output_path: Path, expected_path: Path) -> tuple[int, list[str]]:
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    body = _model_body(output_path)
    cases = _split_cases(body)
    lines: list[str] = []
    failures = 0

    for case in expected["cases"]:
        case_id = case["id"]
        want = case["expected_label"].upper()
        chunk = cases.get(case_id)
        if chunk is None:
            failures += 1
            lines.append(f"FAIL {case_id}: missing section")
            continue
        got = _extract_label(chunk)
        if got is None:
            failures += 1
            lines.append(f"FAIL {case_id}: missing SEVERITY label (want {want})")
            continue
        if got != want:
            failures += 1
            lines.append(f"FAIL {case_id}: got {got} want {want}")
            continue
        lines.append(f"PASS {case_id}: {got}")

    return failures, lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output_file",
        type=Path,
        help="Dated multi-case model output (metadata --- body)",
    )
    parser.add_argument(
        "--expected",
        type=Path,
        default=DEFAULT_EXPECTED,
        help="Path to EXPECTED.json",
    )
    args = parser.parse_args(argv)

    if not args.output_file.is_file():
        print(f"MISSING_FILE: {args.output_file}", file=sys.stderr)
        return 2
    if not args.expected.is_file():
        print(f"MISSING_FILE: {args.expected}", file=sys.stderr)
        return 2

    try:
        failures, lines = score(args.output_file, args.expected)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    for line in lines:
        print(line)

    total = len(lines)
    passed = total - failures
    print(f"SUMMARY: {passed}/{total} passed")
    if failures:
        print(f"REGRESSION: {failures} case(s) failed", file=sys.stderr)
        return 1
    print("OK: all cases passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
