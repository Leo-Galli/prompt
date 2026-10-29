"""Smoke checks for Chapter 9 companion prompt files."""

from __future__ import annotations

import re
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


class TestCh09FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "ignore-progress.md",
            ROOT / "after" / "one-task-resume.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-ignore-2026-10-29.md",
            ROOT / "outputs" / "after-one-task-2026-10-29.md",
            ROOT / "exercises" / "01-mini-spec.md",
            ROOT / "exercises" / "02-five-tasks.md",
            ROOT / "exercises" / "03-resume-prompt.md",
            FIXTURE / "MINI_SPEC.md",
            FIXTURE / "PROGRESS.md",
            FIXTURE / "src" / "todocount.py",
            FIXTURE / "tests" / "test_todocount.py",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

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

    def test_mini_spec_has_task_map_and_session_rules(self) -> None:
        text = (FIXTURE / "MINI_SPEC.md").read_text(encoding="utf-8")
        self.assertIn("Task map", text)
        self.assertIn("Session rules", text)
        self.assertIn("Chat history is not a plan", text)
        self.assertIn("T03", text)
        self.assertIn("--ext", text)

    def test_fixture_missing_ext_filter(self) -> None:
        src = (FIXTURE / "src" / "todocount.py").read_text(encoding="utf-8")
        self.assertNotIn('add_argument("--ext"', src)
        self.assertNotIn("add_argument('--ext'", src)
        self.assertIn("TODO", src)

    def test_before_prompt_ignores_progress(self) -> None:
        text = (ROOT / "before" / "ignore-progress.md").read_text(encoding="utf-8")
        self.assertIn("Ignore them", text)
        self.assertIn("Do not open PROGRESS.md", text)
        self.assertNotIn("first unchecked", text.lower())

    def test_after_prompt_loads_next_unchecked(self) -> None:
        text = (ROOT / "after" / "one-task-resume.md").read_text(encoding="utf-8")
        self.assertIn("PROGRESS.md", text)
        self.assertIn("first unchecked", text)
        self.assertIn("MINI_SPEC.md", text)
        self.assertIn("Do ONLY that task", text)
        self.assertIn("TASK:", text)
        self.assertIn("PROGRESS_UPDATE:", text)
        self.assertIn("THE_END", text)

    def test_before_output_skips_task_focus(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-ignore-2026-10-29.md")
        self.assertIn("STATUS:", body)
        self.assertTrue(
            "todocount.toml" in body or "--json" in body or "--ignore" in body,
            "before output should invent extras outside the task map",
        )
        self.assertNotRegex(body, r"(?m)^TASK:\s*$")
        self.assertNotIn("id: T03", body)

    def test_after_output_targets_t03_only(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-one-task-2026-10-29.md")
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
            FIXTURE / "MINI_SPEC.md",
            FIXTURE / "PROGRESS.md",
            ROOT / "before" / "ignore-progress.md",
            ROOT / "after" / "one-task-resume.md",
            ROOT / "outputs" / "NOTES.md",
        ]:
            raw = path.read_bytes()
            try:
                text = raw.decode("ascii")
            except UnicodeDecodeError as exc:
                self.fail(f"Non-ASCII in {path.relative_to(ROOT)}: {exc}")
            self.assertTrue(text, f"Empty file: {path.name}")
            self.assertIsNone(re.search(r"[^\x00-\x7F]", text))


if __name__ == "__main__":
    unittest.main()
