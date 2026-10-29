"""Required-field checks for prompt and template Markdown."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


REQUIRED_MARKERS = (
    ("goal", ("## Goal", "Goal:", "**Goal**")),
    ("output format", ("## Output format", "Output format:", "**Output format**")),
    ("success criteria", ("## Success criteria", "Success criteria:", "**Success criteria**")),
)


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    issues: tuple[str, ...]
    path: str | None = None


def check_text(text: str, path: str | None = None) -> CheckResult:
    """Return ok when goal, output format and success criteria markers are present."""
    lowered = text.lower()
    issues: list[str] = []

    for label, markers in REQUIRED_MARKERS:
        found = any(marker.lower() in lowered for marker in markers)
        if not found:
            issues.append(f"missing {label}")

    return CheckResult(ok=len(issues) == 0, issues=tuple(issues), path=path)


def check_path(path: Path) -> CheckResult:
    """Read one UTF-8 file and run check_text."""
    text = path.read_text(encoding="utf-8")
    return check_text(text, path=str(path))


def iter_markdown_paths(root: Path) -> list[Path]:
    """Collect .md files under root (file or directory). Skip hidden dirs."""
    if root.is_file():
        if root.suffix.lower() != ".md":
            raise ValueError(f"not a Markdown file: {root}")
        return [root]

    if not root.is_dir():
        raise FileNotFoundError(str(root))

    found: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.parts):
            continue
        found.append(path)
    return found
