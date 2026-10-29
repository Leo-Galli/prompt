"""Tests for the Chapter 8 linecount fixture."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from linecount import count_lines, main  # noqa: E402


class TestLinecount(unittest.TestCase):
    def test_count_lines_basic(self) -> None:
        path = ROOT / "tests" / "_sample.txt"
        path.write_text("a\nb\nc\n", encoding="utf-8")
        self.addCleanup(path.unlink)
        self.assertEqual(count_lines(path), 3)

    def test_default_prints_summary(self) -> None:
        path = ROOT / "tests" / "_sample2.txt"
        path.write_text("x\n", encoding="utf-8")
        self.addCleanup(path.unlink)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main([str(path)])
        self.assertEqual(code, 0)
        out = buf.getvalue()
        self.assertIn("1\n", out)
        self.assertIn("1 files scanned", out)


if __name__ == "__main__":
    unittest.main()
