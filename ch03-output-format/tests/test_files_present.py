"""Smoke checks for Chapter 3 companion prompt files."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh03FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "freeform-bug-summary.md",
            ROOT / "after" / "schema-bug-summary.md",
            ROOT / "after" / "failed-json-ask.md",
            ROOT / "after" / "fix-pass-json.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-freeform-2026-10-29.md",
            ROOT / "outputs" / "after-schema-2026-10-29.md",
            ROOT / "outputs" / "failed-json-2026-10-29.md",
            ROOT / "outputs" / "fix-pass-json-2026-10-29.md",
            ROOT / "exercises" / "01-five-field-schema.md",
            ROOT / "exercises" / "02-markdown-contract.md",
            ROOT / "exercises" / "03-unknown-fallback.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_before_prompt_is_freeform(self) -> None:
        text = (ROOT / "before" / "freeform-bug-summary.md").read_text(encoding="utf-8")
        self.assertIn("LINE-218", text)
        self.assertNotIn("Success criteria:", text)
        self.assertNotIn("Output format", text)

    def test_schema_prompt_names_json_contract(self) -> None:
        text = (ROOT / "after" / "schema-bug-summary.md").read_text(encoding="utf-8")
        for label in ("Output format", "Success criteria:", "ticket_id", "UNKNOWN"):
            self.assertIn(label, text)
        self.assertIn("raw JSON only", text)

    def test_after_schema_output_parses(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-schema-2026-10-29.md")
        data = json.loads(body)
        for key in ("ticket_id", "title", "symptom", "priority", "repro_hint"):
            self.assertIn(key, data)
        self.assertEqual(data["ticket_id"], "LINE-218")
        self.assertEqual(data["priority"], "high")

    def test_failed_json_output_does_not_parse_raw(self) -> None:
        body = _model_body(ROOT / "outputs" / "failed-json-2026-10-29.md")
        with self.assertRaises(json.JSONDecodeError):
            json.loads(body)
        self.assertIn("```", body)

    def test_fix_pass_output_parses(self) -> None:
        body = _model_body(ROOT / "outputs" / "fix-pass-json-2026-10-29.md")
        data = json.loads(body)
        self.assertEqual(data["ticket_id"], "LINE-218")
        self.assertNotIn("```", body)


if __name__ == "__main__":
    unittest.main()
