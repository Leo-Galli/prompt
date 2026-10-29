"""Smoke checks for Chapter 5 companion prompt files."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh05FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "answer-only.md",
            ROOT / "after" / "visible-steps.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-answer-only-2026-10-29.md",
            ROOT / "outputs" / "after-visible-steps-2026-10-29.md",
            ROOT / "exercises" / "01-final-answer-marker.md",
            ROOT / "exercises" / "02-cot-to-checklist.md",
            ROOT / "exercises" / "03-when-not-cot.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_answer_only_forbids_visible_working(self) -> None:
        text = (ROOT / "before" / "answer-only.md").read_text(encoding="utf-8")
        self.assertIn("Do not show working", text)
        self.assertIn("FINAL_ANSWER:", text)
        self.assertIn("Success criteria:", text)
        self.assertNotIn("numbered reasoning", text.lower())

    def test_visible_steps_requires_marker_and_cap(self) -> None:
        text = (ROOT / "after" / "visible-steps.md").read_text(encoding="utf-8")
        self.assertIn("numbered reasoning", text.lower())
        self.assertIn("at most 6", text)
        self.assertIn("FINAL_ANSWER:", text)
        self.assertIn("Success criteria:", text)

    def test_answer_only_output_is_one_line(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-answer-only-2026-10-29.md")
        self.assertEqual(body, "FINAL_ANSWER: R+W")

    def test_visible_steps_output_ends_with_same_answer(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-visible-steps-2026-10-29.md")
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertGreaterEqual(len(lines), 2)
        self.assertTrue(lines[0].startswith("1."))
        self.assertEqual(lines[-1], "FINAL_ANSWER: R+W")
        self.assertNotIn("FINAL_ANSWER:", "\n".join(lines[:-1]))


if __name__ == "__main__":
    unittest.main()
