"""Smoke checks for Chapter 11 companion prompt files."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
FIXTURE = ROOT / "fixture"
TEMPLATE = REPO / "templates" / "fix-pass.md"


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh11FilesPresent(unittest.TestCase):
    def test_before_after_outputs_template_exist(self) -> None:
        required = [
            ROOT / "before" / "soft-release-note.md",
            ROOT / "after" / "fix-pass-filled.md",
            ROOT / "diagnosis" / "NOTES.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-soft-release-2026-10-29.md",
            ROOT / "outputs" / "after-fix-pass-2026-10-29.md",
            ROOT / "exercises" / "01-classify-failures.md",
            ROOT / "exercises" / "02-one-constraint-fix.md",
            ROOT / "exercises" / "03-reset-vs-continue.md",
            FIXTURE / "CHANGE_FACTS.md",
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
            "{{ORIGINAL_GOAL}}",
            "{{FAILURE_CLASSES}}",
            "{{DIAGNOSIS}}",
            "{{FAILED_OUTPUT}}",
            "{{VALIDATION_NOTES}}",
            "{{TRUSTED_FACTS}}",
            "{{OUTPUT_FORMAT_RULE}}",
            "{{OUTPUT_FORMAT_BLOCK}}",
            "{{SUCCESS_CRITERIA}}",
            "<<<FAILED_OUTPUT",
            "Repair the previous reply",
        ]:
            self.assertIn(token, text)

    def test_before_prompt_is_soft(self) -> None:
        text = (ROOT / "before" / "soft-release-note.md").read_text(encoding="utf-8")
        self.assertIn("whatever structure seems best", text)
        self.assertIn("feels ready to ship", text)
        self.assertNotIn("RELEASE_NOTE:", text)
        self.assertNotIn("<<<FAILED_OUTPUT", text)

    def test_after_prompt_is_fix_pass(self) -> None:
        text = (ROOT / "after" / "fix-pass-filled.md").read_text(encoding="utf-8")
        self.assertIn("<<<FAILED_OUTPUT", text)
        self.assertIn("hallucinated fact", text)
        self.assertIn("RELEASE_NOTE:", text)
        self.assertIn("Trusted context", text)
        self.assertIn("2.4.0", text)
        self.assertIn("Repair the previous reply", text)

    def test_diagnosis_names_classes(self) -> None:
        text = (ROOT / "diagnosis" / "NOTES.md").read_text(encoding="utf-8")
        self.assertIn("Hallucinated fact", text)
        self.assertIn("Wrong format", text)
        self.assertIn("Scope creep", text)
        self.assertIn("Reset vs continue", text)

    def test_before_output_shows_failure_modes(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-soft-release-2026-10-29.md")
        self.assertIn("2.4.0", body)
        self.assertTrue(
            "--json" in body or "--ignore" in body or "installer" in body.lower(),
            "before output should invent extras beyond --ext",
        )
        self.assertNotIn("FAILURE_CLASS:", body)
        self.assertNotIn("OUT_OF_SCOPE:", body)

    def test_after_output_is_repaired(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-fix-pass-2026-10-29.md")
        self.assertIn("FAILURE_CLASS:", body)
        self.assertIn("RELEASE_NOTE:", body)
        self.assertIn("SUMMARY:", body)
        self.assertIn("CHANGE:", body)
        self.assertIn("EXAMPLE:", body)
        self.assertIn("OUT_OF_SCOPE:", body)
        self.assertIn("--ext", body)
        self.assertNotIn("2.4.0", body)
        self.assertNotIn("Discord", body)
        self.assertNotIn("pip install", body)
        change_block = body.split("CHANGE:", 1)[1].split("EXAMPLE:", 1)[0]
        self.assertNotIn("--json", change_block)
        self.assertNotIn("--ignore", change_block)
        pos_fail = body.index("FAILURE_CLASS:")
        pos_note = body.index("RELEASE_NOTE:")
        pos_summary = body.index("SUMMARY:")
        pos_change = body.index("CHANGE:")
        pos_example = body.index("EXAMPLE:")
        pos_scope = body.index("OUT_OF_SCOPE:")
        self.assertLess(pos_fail, pos_note)
        self.assertLess(pos_note, pos_summary)
        self.assertLess(pos_summary, pos_change)
        self.assertLess(pos_change, pos_example)
        self.assertLess(pos_example, pos_scope)

    def test_fixture_forbids_extras(self) -> None:
        text = (FIXTURE / "CHANGE_FACTS.md").read_text(encoding="utf-8")
        self.assertIn("--ext", text)
        self.assertIn("Not in this change", text)
        self.assertIn("--json", text)

    def test_ascii_only_project_markdown(self) -> None:
        for path in [
            TEMPLATE,
            FIXTURE / "CHANGE_FACTS.md",
            ROOT / "before" / "soft-release-note.md",
            ROOT / "after" / "fix-pass-filled.md",
            ROOT / "diagnosis" / "NOTES.md",
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
