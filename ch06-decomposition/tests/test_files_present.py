"""Smoke checks for Chapter 6 companion prompt files."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ALLOWLIST = {
    "src/linecount.py",
    "tests/test_ignore.py",
    "README.md",
}


def _model_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 1)
    if len(parts) != 2:
        raise AssertionError(f"Expected metadata --- body split in {path.name}")
    return parts[1].strip()


class TestCh06FilesPresent(unittest.TestCase):
    def test_before_after_and_outputs_exist(self) -> None:
        required = [
            ROOT / "before" / "mega-prompt.md",
            ROOT / "after" / "step1-plan.md",
            ROOT / "after" / "step2-contract.md",
            ROOT / "after" / "step3-verify.md",
            ROOT / "outputs" / "NOTES.md",
            ROOT / "outputs" / "before-mega-2026-10-29.md",
            ROOT / "outputs" / "after-step1-plan-2026-10-29.md",
            ROOT / "outputs" / "after-step2-contract-2026-10-29.md",
            ROOT / "outputs" / "after-step3-verify-2026-10-29.md",
            ROOT / "exercises" / "01-split-feature.md",
            ROOT / "exercises" / "02-define-artifacts.md",
            ROOT / "exercises" / "03-stop-condition.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing companion files: {missing}")

    def test_mega_prompt_is_overloaded(self) -> None:
        text = (ROOT / "before" / "mega-prompt.md").read_text(encoding="utf-8")
        self.assertIn("ONE reply", text)
        self.assertIn("Slack", text)
        self.assertIn("raw JSON", text)
        self.assertIn("Success criteria:", text)
        self.assertIn("src/linecount.py", text)

    def test_chain_prompts_name_artifacts(self) -> None:
        step1 = (ROOT / "after" / "step1-plan.md").read_text(encoding="utf-8")
        step2 = (ROOT / "after" / "step2-contract.md").read_text(encoding="utf-8")
        step3 = (ROOT / "after" / "step3-verify.md").read_text(encoding="utf-8")
        self.assertIn("ARTIFACT_PLAN", step1)
        self.assertIn("Do not write source code", step1)
        self.assertIn("ARTIFACT_CONTRACT", step2)
        self.assertIn("PLAN_ARTIFACT_BEGIN", step2)
        self.assertIn("VERDICT:", step3)
        self.assertIn("CONTRACT_ARTIFACT_BEGIN", step3)

    def test_mega_output_fails_allowlist_or_hours(self) -> None:
        body = _model_body(ROOT / "outputs" / "before-mega-2026-10-29.md")
        self.assertIn("```", body)
        self.assertTrue(
            "src/globutil.py" in body or "hours_estimate\": 5" in body or '"hours_estimate": 5' in body,
            "mega output should show an allowlist or hours failure",
        )

    def test_step1_output_is_plan_only(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-step1-plan-2026-10-29.md")
        self.assertTrue(body.startswith("ARTIFACT_PLAN:"))
        self.assertIn("hours_estimate:", body)
        self.assertNotIn("```", body)
        self.assertNotIn("def ", body)
        files = re.findall(r"(?m)^- (src/\S+|tests/\S+|README\.md)$", body)
        self.assertTrue(files, "expected file bullets under ARTIFACT_PLAN")
        for path in files:
            self.assertIn(path, ALLOWLIST)

    def test_step2_output_is_contract(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-step2-contract-2026-10-29.md")
        self.assertTrue(body.startswith("ARTIFACT_CONTRACT:"))
        self.assertIn("flag: --ignore", body)
        self.assertIn("test_ignore_", body)
        self.assertNotIn("```", body)

    def test_step3_output_verdict_pass(self) -> None:
        body = _model_body(ROOT / "outputs" / "after-step3-verify-2026-10-29.md")
        lines = [line for line in body.splitlines() if line.strip()]
        self.assertEqual(lines[0], "CHECKS:")
        self.assertEqual(lines[-1], "VERDICT: PASS")
        self.assertEqual(sum(1 for line in lines if line[:1].isdigit()), 4)
        for line in lines:
            if line[:1].isdigit():
                self.assertIn("PASS", line)


if __name__ == "__main__":
    unittest.main()
