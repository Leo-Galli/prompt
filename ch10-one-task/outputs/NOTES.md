# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 10. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-overloaded-2026-10-29.md` | `../before/overloaded-session.md` | Batches T03-T05; invents ignore/JSON/config/CI; no hard single-task stop |
| `after-single-task-2026-10-29.md` | `../after/single-task-filled.md` | Filled from `templates/single-task.md`; TASK.id T03 only; THE END stays absent |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../../templates/single-task.md` | Shared one-task-per-session template with `{{variables}}` |
| `../fixture/MINI_SPEC.md` | Master spec for the weekend CLI sample |
| `../fixture/PROGRESS.md` | Checklist with T01-T02 done, T03 next, THE END absent |
| `../fixture/src/todocount.py` | Partial CLI; `--ext` intentionally missing |

The before run is the failure case (overloaded session). The after run is the success case (one filled template, one id). The fixture stays mid-project on purpose. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Session size:** one sitting should finish and verify one done-when line.
2. **Template beats improvisation:** `templates/single-task.md` forces id, allowlist, verify, and end-marker rules.
3. **Split mid-flight:** if the reply starts T04 while T03 is open, stop and open a new session.
4. **Log without rewrite:** append progress notes; do not silently edit yesterday's lines.
