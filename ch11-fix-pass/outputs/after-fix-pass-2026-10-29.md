# Model output -- after (fix-pass repair)

- Date: 2026-10-29
- Prompt: ../after/fix-pass-filled.md
- Context: single-turn coding-agent session used while authoring the companion folder; agent given the filled fix-pass with the quoted failure
- Note: Real reply to the fix-pass. Keeps `--ext` only, uses the locked headings, and drops invented version/flags/installers.

---

FAILURE_CLASS:
- hallucinated fact + wrong format + scope creep (soft polish invite)

RELEASE_NOTE:
SUMMARY:
- todocount can limit scans by file suffix with the new `--ext` flag.

CHANGE:
- `--ext <suffix>` limits which files are scanned by suffix (change id T03).

EXAMPLE:
- todocount --ext .py ./src

OUT_OF_SCOPE:
- This note does not claim `--ignore`, `--json`, installers, GUI, cloud sync, or a version bump.
