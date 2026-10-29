"""Smoke checks for Chapter 8 companion prompt files."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixture"


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh08FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "bloated-rules.md",
            ROOT / "before" / "task-repeats-rules.md",
            ROOT / "after" / "short-rules.md",
            ROOT / "after" / "task-relies-on-rules.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-repeats-2026-10-29.md",
            ROOT / "outputs" / "after-relies-2026-10-29.md",
            ROOT / "exercises" / "01-twenty-line-rules.md",
            ROOT / "exercises" / "02-move-constraints.md",
            ROOT / "exercises" / "03-ci-rules-mention-tests.md",
            ROOT / "scripts" / "check_rules_mention_tests.py",
            FIXTURE / "AGENTS.md",
            FIXTURE / "CONTRIBUTING.md",
            FIXTURE / "docs" / "cli-style.md",
            FIXTURE / ".editorconfig",
            FIXTURE / "src" / "linecount.py",
            FIXTURE / "tests" / "test_linecount.py",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_bloated_rules_are_long_and_bury_critical_notes(self) -> None:
        text = (ROOT / "before" / "bloated-rules.md").read_text(encoding="utf-8")
        self.assertGreater(len(text.splitlines()), 80)
        self.assertIn("Critical path notes buried here on purpose", text)
        self.assertIn("world-class", text.lower())
        self.assertIn("Appendix A", text)

    def test_short_rules_point_and_stay_short(self) -> None:
        text = (ROOT / "after" / "short-rules.md").read_text(encoding="utf-8")
        self.assertLessEqual(len([ln for ln in text.splitlines() if ln.strip()]), 40)
        self.assertIn("CONTRIBUTING.md", text)
        self.assertIn("docs/cli-style.md", text)
        self.assertIn(".editorconfig", text)
        self.assertIn("python -m unittest discover -s tests -v", text)
        self.assertNotIn("Appendix A", text)
        self.assertNotIn("world-class", text.lower())

    def test_task_repeats_rules_is_bloated(self) -> None:
        text = (ROOT / "before" / "task-repeats-rules.md").read_text(encoding="utf-8")
        self.assertIn("pasting the rules", text.lower())
        self.assertIn("Prefer TypeScript", text)
        self.assertIn("Update changelog", text)
        self.assertNotIn("RULES_USED:", text)

    def test_task_relies_on_rules_is_lean(self) -> None:
        text = (ROOT / "after" / "task-relies-on-rules.md").read_text(encoding="utf-8")
        self.assertIn("AGENTS.md", text)
        self.assertIn("Do not restate those rules", text)
        self.assertIn("RULES_USED:", text)
        self.assertIn("Success criteria:", text)
        self.assertNotIn("Prefer TypeScript for new files", text)
        self.assertNotIn("Update changelog", text)

    def test_fixture_agents_matches_short_rules_command(self) -> None:
        agents = (FIXTURE / "AGENTS.md").read_text(encoding="utf-8")
        short = (ROOT / "after" / "short-rules.md").read_text(encoding="utf-8")
        needle = "python -m unittest discover -s tests -v"
        self.assertIn(needle, agents)
        self.assertIn(needle, short)
        src = (FIXTURE / "src" / "linecount.py").read_text(encoding="utf-8")
        self.assertNotIn("--quiet", src)

    def test_check_script_passes_on_short_rules(self) -> None:
        script = ROOT / "scripts" / "check_rules_mention_tests.py"
        proc = subprocess.run(
            [sys.executable, str(script), str(FIXTURE / "AGENTS.md")],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_before_output_shows_scope_creep(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-repeats-2026-10-29.md")
        self.assertTrue(
            "utils/cli_out" in body or "linecount.ts" in body or "CHANGELOG" in body,
            "before output should invent helpers, extra langs, or docs outside allowlist",
        )
        self.assertNotIn("RULES_USED:", body)

    def test_after_output_relies_on_rules(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-relies-2026-10-29.md")
        self.assertIn("RULES_USED:", body)
        self.assertIn("PLAN:", body)
        self.assertIn("DIFF_NOTES:", body)
        self.assertIn("VERIFY:", body)
        self.assertIn("AGENTS.md", body)
        self.assertIn("python -m unittest discover -s tests -v", body)
        self.assertNotIn("utils/cli_out", body)
        self.assertNotIn("linecount.ts", body)
        pos_rules = body.index("RULES_USED:")
        pos_plan = body.index("PLAN:")
        pos_diff = body.index("DIFF_NOTES:")
        pos_verify = body.index("VERIFY:")
        self.assertLess(pos_rules, pos_plan)
        self.assertLess(pos_plan, pos_diff)
        self.assertLess(pos_diff, pos_verify)


if __name__ == "__main__":
    unittest.main()
