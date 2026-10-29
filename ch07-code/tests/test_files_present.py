"""Smoke checks for Chapter 7 companion prompt files."""

from __future__ import annotations

import importlib.util
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


def _load_format_duration():
    path = FIXTURE / "src" / "format_duration.py"
    spec = importlib.util.spec_from_file_location("format_duration_under_test", path)
    if spec is None or spec.loader is None:
        raise AssertionError("Could not load fixture format_duration")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.format_duration


class TestCh07FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "vague-fix.md",
            ROOT / "after" / "scoped-fix.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-vague-2026-10-29.md",
            ROOT / "outputs" / "after-scoped-2026-10-29.md",
            ROOT / "exercises" / "01-file-scoped-fix.md",
            ROOT / "exercises" / "02-failing-test-first.md",
            ROOT / "exercises" / "03-review-checks.md",
            FIXTURE / "src" / "format_duration.py",
            FIXTURE / "tests" / "test_format_duration.py",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_vague_prompt_is_underspecified(self) -> None:
        text = (ROOT / "before" / "vague-fix.md").read_text(encoding="utf-8")
        self.assertIn("bug", text.lower())
        self.assertIn("better", text.lower())
        self.assertNotIn("Success criteria:", text)
        self.assertNotIn("Allowlisted", text)

    def test_scoped_prompt_requires_read_test_and_allowlist(self) -> None:
        text = (ROOT / "after" / "scoped-fix.md").read_text(encoding="utf-8")
        self.assertIn("Read both allowlisted files", text)
        self.assertIn("src/format_duration.py", text)
        self.assertIn("tests/test_format_duration.py", text)
        self.assertIn("test_hours_minutes_and_seconds", text)
        self.assertIn("3665", text)
        self.assertIn("Success criteria:", text)
        self.assertIn("FAILING_TEST:", text)

    def test_fixture_still_has_seconds_bug(self) -> None:
        format_duration = _load_format_duration()
        self.assertEqual(format_duration(3665), "1h 1m")
        src = (FIXTURE / "src" / "format_duration.py").read_text(encoding="utf-8")
        self.assertIn("if seconds and not hours:", src)

    def test_vague_output_shows_scope_creep(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-vague-2026-10-29.md")
        self.assertTrue(
            "utils/timefmt" in body or "humanize_duration" in body or "legacy.py" in body,
            "vague output should invent files or rename the API",
        )
        self.assertNotIn("test_hours_minutes_and_seconds", body)

    def test_scoped_output_is_minimal_and_ordered(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-scoped-2026-10-29.md")
        self.assertIn("READ_NOTES:", body)
        self.assertIn("FAILING_TEST:", body)
        self.assertIn("FIX:", body)
        self.assertIn("VERIFY:", body)
        self.assertIn("3665", body)
        self.assertIn("1h 1m 5s", body)
        self.assertIn("if seconds:", body)
        self.assertNotIn("humanize_duration", body)
        self.assertNotIn("utils/timefmt", body)
        pos_read = body.index("READ_NOTES:")
        pos_fail = body.index("FAILING_TEST:")
        pos_fix = body.index("FIX:")
        pos_verify = body.index("VERIFY:")
        self.assertLess(pos_read, pos_fail)
        self.assertLess(pos_fail, pos_fix)
        self.assertLess(pos_fix, pos_verify)


if __name__ == "__main__":
    unittest.main()
