"""Smoke checks for Chapter 17 capstone companion files."""

from __future__ import annotations

import re
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


class TestCh17FilesPresent(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [
            ROOT / "before" / "invent-book-stats.md",
            ROOT / "after" / "capstone-task-prompt.md",
            ROOT / "fixture" / "MINI_SPEC.md",
            ROOT / "fixture" / "PROGRESS.md",
            ROOT / "fixture" / "FACTS.md",
            ROOT / "fixture" / "README.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-invent-stats-2026-10-29.md",
            ROOT / "outputs" / "after-one-task-capstone-2026-10-29.md",
            ROOT / "exercises" / "01-map-section12-tasks.md",
            ROOT / "exercises" / "02-prepub-audit-stub.md",
            ROOT / "exercises" / "03-acceptance-checks.md",
            ROOT / "README.md",
            REPO / "templates" / "single-task.md",
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

    def test_progress_t04_next_no_the_end(self) -> None:
        text = (ROOT / "fixture" / "PROGRESS.md").read_text(encoding="utf-8")
        self.assertIn("Next: T04", text)
        self.assertIn("- [ ] T04", text)
        self.assertIn("- [x] T03", text)
        self.assertNotIn("\nTHE END\n", text)
        self.assertFalse(text.strip().endswith("THE END"))

    def test_facts_allowlist_has_verified_numbers(self) -> None:
        facts = (ROOT / "fixture" / "FACTS.md").read_text(encoding="utf-8")
        for token in (
            "800",
            "211706",
            "1.8016",
            "14.0516",
            "802",
            "374p",
            "0.75 in",
            "28/28",
            "358p",
            "0.80622",
            "SPARK_KDP_FINAL",
            "RADIO_KDP_FINAL",
        ):
            self.assertIn(token, facts)

    def test_before_prompt_asks_to_invent(self) -> None:
        text = (ROOT / "before" / "invent-book-stats.md").read_text(encoding="utf-8")
        self.assertIn("Invent", text)
        self.assertIn("success rates", text)
        self.assertIn("Do not say UNKNOWN", text)

    def test_after_prompt_is_single_task_t04(self) -> None:
        text = (ROOT / "after" / "capstone-task-prompt.md").read_text(encoding="utf-8")
        self.assertIn("T04", text)
        self.assertIn("FACTS.md", text)
        self.assertIn("THE END", text)
        self.assertIn("Do ONLY T04", text)
        self.assertIn("FACTS_USED:", text)

    def test_before_output_invents_metrics(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-invent-stats-2026-10-29.md")
        self.assertIn("94%", body)
        self.assertIn("640", body)
        self.assertIn("420", body)
        self.assertIn("one-shot", body)
        self.assertNotIn("1.8016", body)
        self.assertNotIn("374p", body)

    def test_after_output_uses_allowlisted_facts(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-one-task-capstone-2026-10-29.md")
        self.assertIn("TASK:", body)
        self.assertIn("id: T04", body)
        self.assertIn("FACTS_USED:", body)
        self.assertIn("800", body)
        self.assertIn("374p", body)
        self.assertIn("1.8016", body)
        self.assertIn("leave absent", body.lower())
        self.assertNotIn("94%", body)
        self.assertNotIn("640-page", body)
        self.assertNotIn("one-shot", body)

    def test_after_output_section_order(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-one-task-capstone-2026-10-29.md")
        markers = [
            "TASK:",
            "PLAN:",
            "DIFF_NOTES:",
            "PROGRESS_UPDATE:",
            "VERIFY:",
            "FACTS_USED:",
        ]
        positions = [body.find(m) for m in markers]
        self.assertTrue(all(p >= 0 for p in positions), positions)
        self.assertEqual(positions, sorted(positions))

    def test_ascii_only_project_markdown(self) -> None:
        paths = [
            ROOT / "before" / "invent-book-stats.md",
            ROOT / "after" / "capstone-task-prompt.md",
            ROOT / "fixture" / "MINI_SPEC.md",
            ROOT / "fixture" / "PROGRESS.md",
            ROOT / "fixture" / "FACTS.md",
            ROOT / "fixture" / "README.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "README.md",
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
