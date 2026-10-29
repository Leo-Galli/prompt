"""Smoke checks for Chapter 16 companion library files."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


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


class TestCh16FilesPresent(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [
            ROOT / "before" / "raw-chat-prompt.md",
            ROOT / "after" / "templated-changelog.md",
            ROOT / "fixture" / "lint-fail.md",
            ROOT / "fixture" / "lint-pass.md",
            ROOT / "fixture" / "FILLED_CHANGELOG.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "lint-fail-2026-10-29.md",
            ROOT / "outputs" / "lint-pass-2026-10-29.md",
            ROOT / "outputs" / "before-raw-changelog-2026-10-29.md",
            ROOT / "outputs" / "after-templated-changelog-2026-10-29.md",
            ROOT / "exercises" / "01-convert-to-template.md",
            ROOT / "exercises" / "02-run-prompt-lint.md",
            ROOT / "exercises" / "03-pr-style-note.md",
            ROOT / "README.md",
            REPO / "templates" / "master-spec.md",
            REPO / "templates" / "single-task.md",
            REPO / "templates" / "fix-pass.md",
            REPO / "prompt_lint" / "__main__.py",
            REPO / "prompt_lint" / "check.py",
        ]
        missing = []
        for path in required:
            if not path.is_file():
                try:
                    missing.append(str(path.relative_to(REPO)))
                except ValueError:
                    missing.append(str(path))
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_before_fails_lint_after_passes(self) -> None:
        before = ROOT / "before" / "raw-chat-prompt.md"
        after = ROOT / "after" / "templated-changelog.md"

        before_proc = _run_lint(before)
        self.assertEqual(before_proc.returncode, 1, before_proc.stdout + before_proc.stderr)
        self.assertIn("missing goal", before_proc.stderr)

        after_proc = _run_lint(after)
        self.assertEqual(after_proc.returncode, 0, after_proc.stdout + after_proc.stderr)
        self.assertIn("OK:", after_proc.stdout)

    def test_fixture_lint_fail_then_pass(self) -> None:
        fail_proc = _run_lint(ROOT / "fixture" / "lint-fail.md")
        self.assertEqual(fail_proc.returncode, 1)
        self.assertIn("missing output format", fail_proc.stderr)
        self.assertIn("missing success criteria", fail_proc.stderr)

        pass_proc = _run_lint(ROOT / "fixture" / "lint-pass.md")
        self.assertEqual(pass_proc.returncode, 0)
        self.assertIn("OK:", pass_proc.stdout)

    def test_after_template_has_variables_and_version(self) -> None:
        text = (ROOT / "after" / "templated-changelog.md").read_text(encoding="utf-8")
        for token in (
            "{{PRODUCT}}",
            "{{VERSION}}",
            "{{CHANGES}}",
            "{{MAX_WORDS}}",
            "Goal:",
            "Output format:",
            "Success criteria:",
            "changelog-blurb@1.0.0",
        ):
            self.assertIn(token, text)

    def test_before_output_invents_metrics(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-raw-changelog-2026-10-29.md")
        self.assertIn("10k GitHub stars", body)
        self.assertIn("3x faster", body)
        self.assertNotIn("CHANGELOG:", body)

    def test_after_output_matches_contract(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-templated-changelog-2026-10-29.md")
        self.assertIn("CHANGELOG:", body)
        self.assertIn("- product: todocount", body)
        self.assertIn("- version: 0.3.0", body)
        self.assertIn("- unknown: NONE", body)
        self.assertIn("recieve", body)
        self.assertNotIn("10k GitHub stars", body)
        self.assertNotIn("3x faster", body)

    def test_saved_lint_transcripts_match_exit_story(self) -> None:
        fail_text = (ROOT / "outputs" / "lint-fail-2026-10-29.md").read_text(encoding="utf-8")
        pass_text = (ROOT / "outputs" / "lint-pass-2026-10-29.md").read_text(encoding="utf-8")
        self.assertIn("exit_code: 1", fail_text)
        self.assertIn("missing output format", fail_text)
        self.assertIn("exit_code: 0", pass_text)
        self.assertIn("OK:", pass_text)

    def test_root_templates_pass_lint(self) -> None:
        proc = _run_lint(REPO / "templates")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertGreaterEqual(proc.stdout.count("OK:"), 3)

    def test_ascii_only_project_markdown(self) -> None:
        paths = [
            ROOT / "before" / "raw-chat-prompt.md",
            ROOT / "after" / "templated-changelog.md",
            ROOT / "fixture" / "lint-fail.md",
            ROOT / "fixture" / "lint-pass.md",
            ROOT / "fixture" / "FILLED_CHANGELOG.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "README.md",
            REPO / "templates" / "master-spec.md",
        ]
        for path in paths:
            raw = path.read_bytes()
            try:
                text = raw.decode("ascii")
            except UnicodeDecodeError as exc:
                self.fail(f"Non-ASCII in {path}: {exc}")
            self.assertTrue(text, f"Empty file: {path.name}")
            self.assertIsNone(re.search(r"[^\x00-\x7F]", text))


if __name__ == "__main__":
    unittest.main()
