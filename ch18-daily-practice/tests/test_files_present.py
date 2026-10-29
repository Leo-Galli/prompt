"""Smoke checks for Chapter 18 daily-practice companion files."""

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


def _lint(path: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO)
    return subprocess.run(
        [sys.executable, "-m", "prompt_lint", str(path)],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        env=env,
    )


class TestCh18FilesPresent(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [
            ROOT / "before" / "vague-daily-ask.md",
            ROOT / "after" / "filled-daily-card.md",
            ROOT / "fixture" / "FACTS.md",
            ROOT / "fixture" / "weak-tips-prompt.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-vague-daily-2026-10-29.md",
            ROOT / "outputs" / "after-daily-card-2026-10-29.md",
            ROOT / "outputs" / "lint-fail-before-2026-10-29.md",
            ROOT / "outputs" / "lint-pass-daily-card-2026-10-29.md",
            ROOT / "exercises" / "01-fill-daily-card-week.md",
            ROOT / "exercises" / "02-retire-weak-template.md",
            ROOT / "exercises" / "03-one-hour-path.md",
            ROOT / "README.md",
            REPO / "templates" / "daily-card.md",
            REPO / "templates" / "single-task.md",
            REPO / "templates" / "fix-pass.md",
            REPO / "templates" / "master-spec.md",
        ]
        missing = []
        for path in required:
            if not path.is_file():
                try:
                    missing.append(str(path.relative_to(REPO)))
                except ValueError:
                    missing.append(str(path))
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_before_fails_lint(self) -> None:
        result = _lint(ROOT / "before" / "vague-daily-ask.md")
        self.assertNotEqual(result.returncode, 0)
        combined = (result.stdout + result.stderr).lower()
        self.assertIn("missing goal", combined)
        self.assertIn("missing output format", combined)
        self.assertIn("missing success criteria", combined)

    def test_after_and_template_pass_lint(self) -> None:
        for path in (
            ROOT / "after" / "filled-daily-card.md",
            REPO / "templates" / "daily-card.md",
        ):
            result = _lint(path)
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_weak_tips_fails_lint(self) -> None:
        result = _lint(ROOT / "fixture" / "weak-tips-prompt.md")
        self.assertNotEqual(result.returncode, 0)

    def test_before_output_invents_gym_metrics(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-vague-daily-2026-10-29.md")
        self.assertIn("Prompt Gym", body)
        self.assertIn("40%", body)
        self.assertIn("Badge", body)
        self.assertNotIn("SEVERITY_NOTE:", body)
        self.assertNotIn("fix/nested-relpath", body)

    def test_after_output_stays_in_facts(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-daily-card-2026-10-29.md")
        facts = (ROOT / "fixture" / "FACTS.md").read_text(encoding="utf-8")
        self.assertIn("SEVERITY_NOTE:", body)
        self.assertIn("todocount", body)
        self.assertIn("#12", body)
        self.assertIn("medium", body)
        self.assertIn("fix/nested-relpath", body)
        self.assertIn("LINT:", body)
        self.assertIn("exit 0", body)
        self.assertIn("SAVE:", body)
        self.assertNotIn("40%", body)
        self.assertNotIn("Prompt Gym", body)
        self.assertNotIn("Badge", body)
        for token in ("todocount", "#12", "medium", "fix/nested-relpath"):
            self.assertIn(token, facts)

    def test_after_output_section_order(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-daily-card-2026-10-29.md")
        markers = ["SEVERITY_NOTE:", "LINT:", "SAVE:"]
        positions = [body.find(m) for m in markers]
        self.assertTrue(all(p >= 0 for p in positions), positions)
        self.assertEqual(positions, sorted(positions))

    def test_after_body_word_budget(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-daily-card-2026-10-29.md")
        match = re.search(r"- body:\s*(.+?)(?:\nLINT:|\n- )", body, re.S)
        self.assertIsNotNone(match)
        note = match.group(1).strip()
        self.assertLessEqual(len(note.split()), 80, note)

    def test_filled_card_mentions_daily_habit_bits(self) -> None:
        text = (ROOT / "after" / "filled-daily-card.md").read_text(encoding="utf-8")
        self.assertIn("DAILY_CARD", text)
        self.assertIn("Goal:", text)
        self.assertIn("Output format:", text)
        self.assertIn("Success criteria:", text)
        self.assertIn("prompt_lint", text)
        self.assertIn("SAVE", text)

    def test_ascii_only_project_markdown(self) -> None:
        paths = [
            ROOT / "before" / "vague-daily-ask.md",
            ROOT / "after" / "filled-daily-card.md",
            ROOT / "fixture" / "FACTS.md",
            ROOT / "fixture" / "weak-tips-prompt.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "README.md",
            REPO / "templates" / "daily-card.md",
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
