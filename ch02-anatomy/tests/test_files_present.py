"""Smoke checks for Chapter 2 companion prompt files."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestCh02FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "chatty-readme-ask.md",
            ROOT / "after" / "skeleton-readme-ask.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-chatty-2026-10-29.md",
            ROOT / "outputs" / "after-skeleton-2026-10-29.md",
            ROOT / "exercises" / "01-fill-skeleton.md",
            ROOT / "exercises" / "02-strip-bloated.md",
            ROOT / "exercises" / "03-success-criteria.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_before_prompt_is_chatty(self) -> None:
        text = (ROOT / "before" / "chatty-readme-ask.md").read_text(encoding="utf-8")
        self.assertIn("linecount", text)
        self.assertIn("Thanks", text)
        self.assertNotIn("Success criteria:", text)

    def test_after_prompt_has_seven_parts(self) -> None:
        text = (ROOT / "after" / "skeleton-readme-ask.md").read_text(encoding="utf-8")
        for label in (
            "Role:",
            "Goal:",
            "Context:",
            "Constraints:",
            "Steps:",
            "Output format",
            "Success criteria:",
        ):
            self.assertIn(label, text)


if __name__ == "__main__":
    unittest.main()
