# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 11. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-soft-release-2026-10-29.md` | `../before/soft-release-note.md` | Soft release-note ask; invents version/flags/installers; marketing shape |
| `after-fix-pass-2026-10-29.md` | `../after/fix-pass-filled.md` | Filled from `templates/fix-pass.md`; quotes failure; surgical repair |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../../templates/fix-pass.md` | Shared fix-pass template with `{{variables}}` |
| `../diagnosis/NOTES.md` | Failure-class diagnosis and reset-vs-continue decision |
| `../fixture/CHANGE_FACTS.md` | Trusted fact allowlist for the `--ext` change |

The before run is the failure case (soft prompt). The after run is the repair case (quoted failure + surgical constraints). Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Diagnose before rewrite:** name the failure class; do not burn the thread on vibes.
2. **Quote the failure:** paste the bad reply as untrusted data inside delimiters.
3. **Surgical edit:** change the fewest constraints that fix the class.
4. **Reset vs continue:** continue when the goal is right and the prompt was soft; reset when the thread is poisoned or the task was wrong.
