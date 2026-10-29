"""Tests for format_duration. Intentionally incomplete -- missing the hours+seconds case."""

from __future__ import annotations

import unittest

from format_duration import format_duration


class TestFormatDuration(unittest.TestCase):
    def test_zero(self) -> None:
        self.assertEqual(format_duration(0), "0s")

    def test_seconds_only(self) -> None:
        self.assertEqual(format_duration(45), "45s")

    def test_minutes_and_seconds(self) -> None:
        self.assertEqual(format_duration(65), "1m 5s")

    def test_hours_and_minutes(self) -> None:
        self.assertEqual(format_duration(3660), "1h 1m")

    def test_negative_raises(self) -> None:
        with self.assertRaises(ValueError):
            format_duration(-1)


if __name__ == "__main__":
    unittest.main()
