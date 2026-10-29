"""Tests for todocount. Extension filter tests arrive with T03."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.todocount import count_todos, main


class TestTodoCount(unittest.TestCase):
    def test_counts_todo_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.py").write_text("# TODO one\n", encoding="utf-8")
            (root / "b.md").write_text("TODO two\nTODO three\n", encoding="utf-8")
            self.assertEqual(count_todos(root), 3)

    def test_main_prints_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "x.txt").write_text("TODO\n", encoding="utf-8")
            self.assertEqual(main([str(root)]), 0)


if __name__ == "__main__":
    unittest.main()
