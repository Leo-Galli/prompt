"""Unit tests for prompt-lint skeleton."""

from __future__ import annotations

import unittest

from prompt_lint.check import check_text


COMPLETE = """
## Goal
Rewrite the summary in plain US English.

## Output format
One paragraph, max 80 words.

## Success criteria
A stranger can grade yes/no without asking follow-ups.
"""

INCOMPLETE = """
## Goal
Do something vague.
"""


class TestCheckText(unittest.TestCase):
    def test_complete_prompt_passes(self) -> None:
        result = check_text(COMPLETE)
        self.assertTrue(result.ok)
        self.assertEqual(result.issues, ())

    def test_incomplete_prompt_fails(self) -> None:
        result = check_text(INCOMPLETE)
        self.assertFalse(result.ok)
        self.assertIn("missing output format", result.issues)
        self.assertIn("missing success criteria", result.issues)


if __name__ == "__main__":
    unittest.main()
