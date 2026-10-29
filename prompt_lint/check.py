"""Required-field checks for prompt text (skeleton)."""

from __future__ import annotations

from dataclasses import dataclass


REQUIRED_MARKERS = (
    ("goal", ("## Goal", "Goal:", "**Goal**")),
    ("output format", ("## Output format", "Output format:", "**Output format**")),
    ("success criteria", ("## Success criteria", "Success criteria:", "**Success criteria**")),
)


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    issues: tuple[str, ...]


def check_text(text: str) -> CheckResult:
    """Return ok when goal, output format and success criteria markers are present."""
    lowered = text.lower()
    issues: list[str] = []

    for label, markers in REQUIRED_MARKERS:
        found = any(marker.lower() in lowered for marker in markers)
        if not found:
            issues.append(f"missing {label}")

    return CheckResult(ok=len(issues) == 0, issues=tuple(issues))
