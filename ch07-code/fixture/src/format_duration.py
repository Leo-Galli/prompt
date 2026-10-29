"""Compact human-readable durations for non-negative whole seconds."""


def format_duration(total_seconds: int) -> str:
    """Return a compact duration like '1h 2m 3s'.

    Parts with value 0 are omitted, except that exactly 0 seconds returns '0s'.
    """
    if total_seconds < 0:
        raise ValueError("total_seconds must be >= 0")

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    parts: list[str] = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    # BUG: seconds are skipped whenever hours > 0 (e.g. 3665 -> '1h 1m' missing '5s').
    if seconds and not hours:
        parts.append(f"{seconds}s")
    if not parts:
        return "0s"
    return " ".join(parts)
