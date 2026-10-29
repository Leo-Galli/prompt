# case-05

Expected label: HIGH

Issue note:
Cache write silently overwrites `./.todocount-cache` even when that path is a user-owned notes file redirected there. No warning. Previous notes are gone after one run.
