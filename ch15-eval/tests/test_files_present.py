"""Smoke checks for Chapter 15 companion eval files."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
CASES = ROOT / "cases"
SCRIPTS = ROOT / "scripts"


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh15FilesPresent(unittest.TestCase):
    def test_before_after_cases_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "regressed-prompt.md",
            ROOT / "after" / "restored-prompt.md",
            ROOT / "template" / "label-severity.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-case-set-2026-10-29.md",
            ROOT / "outputs" / "after-case-set-2026-10-29.md",
            ROOT / "exercises" / "01-build-five-case-set.md",
            ROOT / "exercises" / "02-score-two-versions.md",
            ROOT / "exercises" / "03-ci-check-stub.md",
            SCRIPTS / "score_eval.py",
            CASES / "EXPECTED.json",
            CASES / "case-01.md",
            CASES / "case-02.md",
            CASES / "case-03.md",
            CASES / "case-04.md",
            CASES / "case-05.md",
        ]
        missing = []
        for path in required:
            if not path.is_file():
                try:
                    missing.append(str(path.relative_to(REPO)))
                except ValueError:
                    missing.append(str(path))
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_expected_json_has_five_cases(self) -> None:
        data = json.loads((CASES / "EXPECTED.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["cases"]), 5)
        labels = {case["expected_label"] for case in data["cases"]}
        self.assertEqual(labels, {"HIGH", "MED", "LOW"})
        for case in data["cases"]:
            self.assertTrue((ROOT / case["input_file"]).is_file())

    def test_before_prompt_is_soft(self) -> None:
        text = (ROOT / "before" / "regressed-prompt.md").read_text(encoding="utf-8")
        self.assertIn("Any format is fine", text)
        self.assertIn("Feels decisive", text)
        self.assertNotIn("SEVERITY:", text)
        self.assertNotIn("HIGH: crash", text)

    def test_after_and_template_share_contract(self) -> None:
        after = (ROOT / "after" / "restored-prompt.md").read_text(encoding="utf-8")
        template = (ROOT / "template" / "label-severity.md").read_text(encoding="utf-8")
        for text in (after, template):
            self.assertIn("SEVERITY:", text)
            self.assertIn("HIGH: crash", text)
            self.assertIn("evidence:", text)
            self.assertIn("{{ISSUE_NOTE}}", text)

    def test_before_output_lacks_severity_shape(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-case-set-2026-10-29.md")
        self.assertIn("## case-01", body)
        self.assertIn("## case-05", body)
        self.assertNotIn("SEVERITY:", body)
        self.assertNotIn("- label: HIGH", body)

    def test_after_output_matches_expected_labels(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-case-set-2026-10-29.md")
        expected = json.loads((CASES / "EXPECTED.json").read_text(encoding="utf-8"))
        for case in expected["cases"]:
            self.assertIn(f"## {case['id']}", body)
        self.assertEqual(body.count("SEVERITY:"), 5)
        self.assertIn("- label: HIGH", body)
        self.assertIn("- label: MED", body)
        self.assertIn("- label: LOW", body)
        # Spot-check the two easy traps from the before run.
        case02 = body.split("## case-02", 1)[1].split("## case-03", 1)[0]
        case03 = body.split("## case-03", 1)[1].split("## case-04", 1)[0]
        self.assertIn("- label: LOW", case02)
        self.assertIn("- label: MED", case03)

    def test_score_eval_fails_before_passes_after(self) -> None:
        script = SCRIPTS / "score_eval.py"
        before = ROOT / "outputs" / "before-case-set-2026-10-29.md"
        after = ROOT / "outputs" / "after-case-set-2026-10-29.md"

        before_proc = subprocess.run(
            [sys.executable, str(script), str(before)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(before_proc.returncode, 1, before_proc.stdout + before_proc.stderr)
        self.assertIn("REGRESSION", before_proc.stderr)

        after_proc = subprocess.run(
            [sys.executable, str(script), str(after)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(after_proc.returncode, 0, after_proc.stdout + after_proc.stderr)
        self.assertIn("OK: all cases passed", after_proc.stdout)
        self.assertIn("SUMMARY: 5/5 passed", after_proc.stdout)

    def test_ascii_only_project_markdown(self) -> None:
        paths = [
            ROOT / "before" / "regressed-prompt.md",
            ROOT / "after" / "restored-prompt.md",
            ROOT / "template" / "label-severity.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "README.md",
            CASES / "case-01.md",
            CASES / "case-02.md",
            CASES / "case-03.md",
            CASES / "case-04.md",
            CASES / "case-05.md",
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
