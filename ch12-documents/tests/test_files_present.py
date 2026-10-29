"""Smoke checks for Chapter 12 companion prompt files."""

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


class TestCh12FilesPresent(unittest.TestCase):
    def test_before_after_outputs_fixture_exist(self) -> None:
        required = [
            ROOT / "before" / "vague-write-chapter.md",
            ROOT / "after" / "outline-bound-chapter.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-vague-chapter-2026-10-29.md",
            ROOT / "outputs" / "after-outline-bound-2026-10-29.md",
            ROOT / "exercises" / "01-chapter-prompt-from-outline.md",
            ROOT / "exercises" / "02-continuity-check.md",
            ROOT / "exercises" / "03-edit-only-pass.md",
            FIXTURE / "MINI_OUTLINE.md",
            FIXTURE / "VOICE_RULES.md",
            FIXTURE / "CONTINUITY.md",
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
        text = (ROOT / "before" / "vague-write-chapter.md").read_text(encoding="utf-8")
        self.assertIn("whatever structure seems best", text)
        self.assertIn("feels ready to publish", text)
        self.assertNotIn("word budget", text.lower())
        self.assertNotIn("G03", text)
        self.assertNotIn("VOICE_RULES", text)

    def test_after_prompt_is_outline_bound(self) -> None:
        text = (ROOT / "after" / "outline-bound-chapter.md").read_text(encoding="utf-8")
        self.assertIn("G03", text)
        self.assertIn("700-900", text)
        self.assertIn("VOICE_RULES.md", text)
        self.assertIn("CONTINUITY.md", text)
        self.assertIn("pass_type: draft", text)
        self.assertIn("Why filter by suffix", text)
        self.assertIn("The --ext flag", text)
        self.assertIn("What this chapter does not cover", text)
        self.assertIn("Draft G03 only", text)

    def test_fixture_locks_g03(self) -> None:
        outline = (FIXTURE / "MINI_OUTLINE.md").read_text(encoding="utf-8")
        voice = (FIXTURE / "VOICE_RULES.md").read_text(encoding="utf-8")
        continuity = (FIXTURE / "CONTINUITY.md").read_text(encoding="utf-8")
        self.assertIn("G03", outline)
        self.assertIn("Limit scans with --ext", outline)
        self.assertIn("delve", voice)
        self.assertIn("ASCII only", voice)
        self.assertIn("todocount", continuity)
        self.assertIn("--ext", continuity)

    def test_before_output_shows_failure_modes(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-vague-chapter-2026-10-29.md")
        self.assertTrue(
            "delve" in body.lower()
            or "unleash" in body.lower()
            or "game-changer" in body.lower(),
            "before output should use banned hype phrases",
        )
        self.assertTrue(
            "2.4.0" in body or "--json" in body or "installer" in body.lower(),
            "before output should invent extras beyond --ext",
        )
        self.assertNotIn("chapter_id: G03", body)
        self.assertNotIn("pass_type: draft", body)

    def test_after_output_is_outline_bound(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-outline-bound-2026-10-29.md")
        self.assertIn("META:", body)
        self.assertIn("CHAPTER:", body)
        self.assertIn("chapter_id: G03", body)
        self.assertIn("pass_type: draft", body)
        self.assertIn("## Why filter by suffix", body)
        self.assertIn("## The --ext flag", body)
        self.assertIn("## What this chapter does not cover", body)
        self.assertIn("todocount --ext .py ./src", body)
        self.assertNotIn("2.4.0", body)
        self.assertNotIn("Discord", body)
        lowered = body.lower()
        for banned in ["delve", "unleash", "game-changer", "thrilled to announce"]:
            self.assertNotIn(banned, lowered)
        pos_meta = body.index("META:")
        pos_chapter = body.index("CHAPTER:")
        pos_why = body.index("## Why filter by suffix")
        pos_ext = body.index("## The --ext flag")
        pos_not = body.index("## What this chapter does not cover")
        self.assertLess(pos_meta, pos_chapter)
        self.assertLess(pos_why, pos_ext)
        self.assertLess(pos_ext, pos_not)
        chapter_body = body.split("CHAPTER:", 1)[1]
        words = re.findall(r"\b[\w']+\b", chapter_body)
        self.assertGreaterEqual(len(words), 700)
        self.assertLessEqual(len(words), 900)

    def test_ascii_only_project_markdown(self) -> None:
        for path in [
            FIXTURE / "MINI_OUTLINE.md",
            FIXTURE / "VOICE_RULES.md",
            FIXTURE / "CONTINUITY.md",
            ROOT / "before" / "vague-write-chapter.md",
            ROOT / "after" / "outline-bound-chapter.md",
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
