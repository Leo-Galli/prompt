"""Unit tests for prompt-lint."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prompt_lint.check import check_path, check_text, iter_markdown_paths

REPO = Path(__file__).resolve().parents[2]


COMPLETE = """
## Goal
Rewrite the summary in plain US English.

## Output format
One paragraph, max 80 words.

## Success criteria
A stranger can grade yes/no without asking follow-ups.
"""

INCOMPLETE = """
## Goal
Do something vague.
"""

COLON_STYLE = """
Goal: Label one issue.

Output format:
SEVERITY:
- label: HIGH|MED|LOW

Success criteria:
- label is one of HIGH, MED, LOW
"""


def _run_lint(*paths: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO)
    return subprocess.run(
        [sys.executable, "-m", "prompt_lint", *[str(p) for p in paths]],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )


class TestCheckText(unittest.TestCase):
    def test_complete_prompt_passes(self) -> None:
        result = check_text(COMPLETE)
        self.assertTrue(result.ok)
        self.assertEqual(result.issues, ())

    def test_incomplete_prompt_fails(self) -> None:
        result = check_text(INCOMPLETE)
        self.assertFalse(result.ok)
        self.assertIn("missing output format", result.issues)
        self.assertIn("missing success criteria", result.issues)

    def test_colon_style_markers_pass(self) -> None:
        result = check_text(COLON_STYLE)
        self.assertTrue(result.ok)


class TestCheckPathAndCli(unittest.TestCase):
    def test_check_path_and_iter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = root / "good.md"
            bad = root / "bad.md"
            good.write_text(COMPLETE, encoding="utf-8")
            bad.write_text(INCOMPLETE, encoding="utf-8")
            (root / ".hidden").mkdir()
            (root / ".hidden" / "skip.md").write_text(COMPLETE, encoding="utf-8")

            paths = iter_markdown_paths(root)
            self.assertEqual([p.name for p in paths], ["bad.md", "good.md"])

            good_result = check_path(good)
            bad_result = check_path(bad)
            self.assertTrue(good_result.ok)
            self.assertFalse(bad_result.ok)

    def test_cli_fail_then_pass_on_ch16_fixtures(self) -> None:
        fail_path = REPO / "ch16-library" / "fixture" / "lint-fail.md"
        pass_path = REPO / "ch16-library" / "fixture" / "lint-pass.md"
        if not fail_path.is_file() or not pass_path.is_file():
            self.skipTest("ch16 fixtures not present yet")

        fail_proc = _run_lint(fail_path)
        self.assertEqual(fail_proc.returncode, 1, fail_proc.stdout + fail_proc.stderr)
        self.assertIn("missing", fail_proc.stderr)

        pass_proc = _run_lint(pass_path)
        self.assertEqual(pass_proc.returncode, 0, pass_proc.stdout + pass_proc.stderr)
        self.assertIn("OK:", pass_proc.stdout)

    def test_root_templates_pass_lint(self) -> None:
        templates = REPO / "templates"
        if not templates.is_dir():
            self.skipTest("templates/ missing")
        for path in sorted(templates.glob("*.md")):
            result = check_path(path)
            self.assertTrue(result.ok, f"{path.name}: {result.issues}")


if __name__ == "__main__":
    unittest.main()
