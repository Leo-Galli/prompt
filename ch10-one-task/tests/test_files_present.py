"""Smoke checks for Chapter 10 companion prompt files."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
FIXTURE = ROOT / "fixture"
TEMPLATE = REPO / "templates" / "single-task.md"


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh10FilesPresent(unittest.TestCase):
    def test_before_after_outputs_template_exist(self) -> None:
        required = [
            ROOT / "before" / "overloaded-session.md",
            ROOT / "after" / "single-task-filled.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-overloaded-2026-10-29.md",
            ROOT / "outputs" / "after-single-task-2026-10-29.md",
            ROOT / "exercises" / "01-split-feature.md",
            ROOT / "exercises" / "02-done-when.md",
            ROOT / "exercises" / "03-resume-opener.md",
            FIXTURE / "MINI_SPEC.md",
            FIXTURE / "PROGRESS.md",
            FIXTURE / "src" / "todocount.py",
            FIXTURE / "tests" / "test_todocount.py",
            TEMPLATE,
        ]
        missing = []
        for path in required:
            if not path.is_file():
                try:
                    missing.append(str(path.relative_to(REPO)))
                except ValueError:
                    missing.append(str(path))
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_template_has_required_variables(self) -> None:
        text = TEMPLATE.read_text(encoding="utf-8")
        for token in [
            "{{ROLE}}",
            "{{TASK_ID}}",
            "{{DONE_WHEN}}",
            "{{SPEC_PATH}}",
            "{{PROGRESS_PATH}}",
            "{{PROJECT_ROOT}}",
            "{{SPEC_SECTIONS}}",
            "{{ALLOWLIST}}",
            "{{VERIFY_COMMAND}}",
            "Do ONLY",
            "THE_END",
            "PROGRESS_UPDATE:",
        ]:
            self.assertIn(token, text)

    def test_progress_has_t03_next_and_no_the_end(self) -> None:
        text = (FIXTURE / "PROGRESS.md").read_text(encoding="utf-8")
        self.assertIn("Next: T03", text)
        self.assertIn("- [x] T01", text)
        self.assertIn("- [x] T02", text)
        self.assertRegex(text, r"- \[ \] T03 ")
        self.assertRegex(text, r"- \[ \] T04 ")
        self.assertRegex(text, r"- \[ \] T05 ")
        self.assertNotRegex(text, r"(?m)^THE END\s*$")
        self.assertIn("Done when:", text)

    def test_fixture_missing_ext_filter(self) -> None:
        src = (FIXTURE / "src" / "todocount.py").read_text(encoding="utf-8")
        self.assertNotIn('add_argument("--ext"', src)
        self.assertNotIn("add_argument('--ext'", src)

    def test_before_prompt_is_overloaded(self) -> None:
        text = (ROOT / "before" / "overloaded-session.md").read_text(encoding="utf-8")
        self.assertIn("T03, T04, and T05", text)
        self.assertIn("bonus", text.lower())
        self.assertNotIn("Do ONLY T03", text)

    def test_after_prompt_is_single_task(self) -> None:
        text = (ROOT / "after" / "single-task-filled.md").read_text(encoding="utf-8")
        self.assertIn("Do ONLY T03", text)
        self.assertIn("done_when:", text)
        self.assertIn("TASK:", text)
        self.assertIn("PROGRESS_UPDATE:", text)
        self.assertIn("THE_END", text)
        self.assertIn("T03", text)

    def test_before_output_batches_work(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-overloaded-2026-10-29.md")
        self.assertIn("STATUS:", body)
        self.assertIn("BATCH:", body)
        self.assertTrue(
            "todocount.toml" in body or "--json" in body or "--ignore" in body or "ci.yml" in body,
            "before output should invent extras outside one done-when",
        )
        self.assertNotRegex(body, r"(?m)^TASK:\s*$")
        self.assertNotIn("id: T03", body)

    def test_after_output_targets_t03_only(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-single-task-2026-10-29.md")
        self.assertIn("TASK:", body)
        self.assertIn("id: T03", body)
        self.assertIn("PLAN:", body)
        self.assertIn("DIFF_NOTES:", body)
        self.assertIn("PROGRESS_UPDATE:", body)
        self.assertIn("VERIFY:", body)
        self.assertIn("leave absent", body.lower())
        self.assertNotIn("CHANGELOG.md", body)
        self.assertNotIn("todocount.toml", body)
        pos_task = body.index("TASK:")
        pos_plan = body.index("PLAN:")
        pos_diff = body.index("DIFF_NOTES:")
        pos_prog = body.index("PROGRESS_UPDATE:")
        pos_verify = body.index("VERIFY:")
        self.assertLess(pos_task, pos_plan)
        self.assertLess(pos_plan, pos_diff)
        self.assertLess(pos_diff, pos_prog)
        self.assertLess(pos_prog, pos_verify)

    def test_ascii_only_project_markdown(self) -> None:
        for path in [
            TEMPLATE,
            FIXTURE / "MINI_SPEC.md",
            FIXTURE / "PROGRESS.md",
            ROOT / "before" / "overloaded-session.md",
            ROOT / "after" / "single-task-filled.md",
            ROOT / "outputs" / "NOTES.md",
        ]:
            raw = path.read_bytes()
            try:
                text = raw.decode("ascii")
            except UnicodeDecodeError as exc:
                self.fail(f"Non-ASCII in {path}: {exc}")
            self.assertTrue(text, f"Empty file: {path.name}")
            self.assertIsNone(re.search(r"[^\x00-\x7F]", text))


if __name__ == "__main__":
    unittest.main()
