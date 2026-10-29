"""Smoke checks for Chapter 4 companion prompt files."""

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


class TestCh04FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "zero-shot-classify.md",
            ROOT / "after" / "two-shot-classify.md",
            ROOT / "after" / "bad-example-classify.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-zero-shot-2026-10-29.md",
            ROOT / "outputs" / "after-two-shot-2026-10-29.md",
            ROOT / "outputs" / "bad-example-2026-10-29.md",
            ROOT / "exercises" / "01-three-example-set.md",
            ROOT / "exercises" / "02-remove-weakest.md",
            ROOT / "exercises" / "03-document-trait.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_zero_shot_has_no_examples_block(self) -> None:
        text = (ROOT / "before" / "zero-shot-classify.md").read_text(encoding="utf-8")
        self.assertIn("Success criteria:", text)
        self.assertIn("User message:", text)
        self.assertNotIn("Example 1", text)
        self.assertNotIn("Examples (", text)

    def test_two_shot_has_two_examples_and_closed_labels(self) -> None:
        text = (ROOT / "after" / "two-shot-classify.md").read_text(encoding="utf-8")
        self.assertIn("Example 1", text)
        self.assertIn("Example 2", text)
        self.assertIn("label: bug", text)
        self.assertIn("label: feature_request", text)
        for label in ("bug", "feature_request", "question"):
            self.assertIn(label, text)

    def test_bad_example_prompt_mislabels_on_purpose(self) -> None:
        text = (ROOT / "after" / "bad-example-classify.md").read_text(encoding="utf-8")
        self.assertIn("label=bug", text)
        self.assertIn("hotfix lane", text)
        self.assertIn("Can linecount skip blank lines", text)

    def test_zero_and_two_shot_outputs_are_one_line_question(self) -> None:
        for name in (
            "before-zero-shot-2026-10-29.md",
            "after-two-shot-2026-10-29.md",
        ):
            body = _model_body(ROOT / "outputs" / name)
            self.assertEqual(body, "label: question", msg=name)

    def test_bad_example_output_skews_label_and_shape(self) -> None:
        body = _model_body(ROOT / "outputs" / "bad-example-2026-10-29.md")
        self.assertNotEqual(body, "label: question")
        self.assertFalse(body.startswith("label: "))
        self.assertIn("label=bug", body)
        self.assertIn("Answer:", body)
        self.assertGreater(len(body), 80)


if __name__ == "__main__":
    unittest.main()
