"""Smoke checks for Chapter 13 companion prompt files."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
FIXTURE = ROOT / "fixture"


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh13FilesPresent(unittest.TestCase):
    def test_before_after_outputs_fixture_exist(self) -> None:
        required = [
            ROOT / "before" / "vague-image-ask.md",
            ROOT / "after" / "structured-image-brief.md",
            ROOT / "after" / "slide-outline.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-vague-image-2026-10-29.md",
            ROOT / "outputs" / "after-structured-brief-2026-10-29.md",
            ROOT / "outputs" / "after-slide-outline-2026-10-29.md",
            ROOT / "exercises" / "01-image-brief-three-constraints.md",
            ROOT / "exercises" / "02-six-slide-talk.md",
            ROOT / "exercises" / "03-alt-text.md",
            FIXTURE / "BRAND_LOCKS.md",
        ]
        missing = []
        for path in required:
            if not path.is_file():
                try:
                    missing.append(str(path.relative_to(REPO)))
                except ValueError:
                    missing.append(str(path))
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_before_prompt_is_vague(self) -> None:
        text = (ROOT / "before" / "vague-image-ask.md").read_text(encoding="utf-8")
        self.assertIn("Make it pop", text)
        self.assertIn("looks cool", text)
        self.assertIn("invent a polished product UI screenshot", text)
        self.assertNotIn("BRAND_LOCKS", text)
        self.assertNotIn("alt_text", text)
        self.assertNotIn("#121110", text)

    def test_after_image_brief_is_structured(self) -> None:
        text = (ROOT / "after" / "structured-image-brief.md").read_text(encoding="utf-8")
        self.assertIn("BRAND_LOCKS.md", text)
        self.assertIn("#121110", text)
        self.assertIn("#3FA7A0", text)
        self.assertIn("BRIEF:", text)
        self.assertIn("alt_text:", text)
        self.assertIn("negatives:", text)
        self.assertIn("ASSET_REQUIRED", text)
        self.assertIn("todocount --ext .py ./src", text)

    def test_after_slide_outline_requires_six(self) -> None:
        text = (ROOT / "after" / "slide-outline.md").read_text(encoding="utf-8")
        self.assertIn("slide_count: 6", text)
        self.assertIn("one_sentence", text)
        self.assertIn("visual_note", text)
        self.assertIn("TALK06", text)
        self.assertIn("ASSET_REQUIRED", text)

    def test_fixture_brand_locks(self) -> None:
        locks = (FIXTURE / "BRAND_LOCKS.md").read_text(encoding="utf-8")
        self.assertIn("todocount", locks)
        self.assertIn("#121110", locks)
        self.assertIn("#3FA7A0", locks)
        self.assertIn("No fake product UI screenshots", locks)
        self.assertIn("alt text", locks.lower())

    def test_before_output_shows_failure_modes(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-vague-image-2026-10-29.md")
        lowered = body.lower()
        self.assertTrue(
            "screenshot" in lowered or "ui" in lowered,
            "before output should invent UI/screenshot chrome",
        )
        self.assertTrue(
            "neon" in lowered or "purple" in lowered or "ai brain" in lowered,
            "before output should use neon/AI tropes",
        )
        self.assertTrue(
            "2.4m" in lowered or "98%" in lowered or "award" in lowered,
            "before output should invent metrics or awards",
        )
        self.assertNotIn("BRIEF:", body)
        self.assertNotIn("alt_text:", body)

    def test_after_brief_output_is_structured(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-structured-brief-2026-10-29.md")
        self.assertIn("BRIEF:", body)
        for field in [
            "subject:",
            "composition:",
            "lighting:",
            "background:",
            "accent:",
            "typography_notes:",
            "brand_mark:",
            "negatives:",
            "assets:",
            "alt_text:",
            "success_checks:",
        ]:
            self.assertIn(field, body)
        self.assertIn("#121110", body)
        self.assertIn("#3FA7A0", body)
        self.assertIn("todocount --ext .py ./src", body)
        lowered = body.lower()
        self.assertIn("fake", lowered)
        self.assertIn("ai brain nebula", body.lower())
        # Nebula may appear only inside negatives -- not as a requested subject.
        subject_line = [
            line for line in body.splitlines() if line.strip().startswith("- subject:")
        ]
        self.assertEqual(len(subject_line), 1)
        self.assertNotIn("nebula", subject_line[0].lower())
        self.assertNotIn("2.4m", lowered)
        self.assertNotIn(".png", lowered)

    def test_after_slide_output_has_six_jobs(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-slide-outline-2026-10-29.md")
        self.assertIn("META:", body)
        self.assertIn("SLIDES:", body)
        self.assertIn("slide_count: 6", body)
        for n in range(1, 7):
            self.assertIn(f"### S{n} |", body)
        self.assertEqual(len(re.findall(r"^### S\d+ \|", body, flags=re.M)), 6)
        self.assertIn("todocount --ext .py ./src", body)
        self.assertIn("job:", body)
        self.assertIn("one_sentence:", body)
        self.assertIn("visual_note:", body)
        self.assertNotIn(".png", body.lower())
        lowered = body.lower()
        self.assertNotIn("2.4m", lowered)
        self.assertNotIn("download count", lowered)

    def test_ascii_only_project_markdown(self) -> None:
        for path in [
            FIXTURE / "BRAND_LOCKS.md",
            ROOT / "before" / "vague-image-ask.md",
            ROOT / "after" / "structured-image-brief.md",
            ROOT / "after" / "slide-outline.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "README.md",
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
