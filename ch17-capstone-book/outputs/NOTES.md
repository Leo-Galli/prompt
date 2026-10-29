# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 17. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-invent-stats-2026-10-29.md` | `../before/invent-book-stats.md` | Invents 94% success, 640/420 pages, 40 chapters, one-shot covers; contradicts FACTS.md |
| `after-one-task-capstone-2026-10-29.md` | `../after/capstone-task-prompt.md` | TASK.id T04 only; FACTS_USED from allowlist; THE END stays absent |

Spec/progress artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../fixture/MINI_SPEC.md` | Master spec for the kitbook drill |
| `../fixture/PROGRESS.md` | Checklist with T01-T03 done, T04 next, THE END absent |
| `../fixture/FACTS.md` | Verified Spark/Signal lines copied from real PROGRESS trees |
| `../fixture/README.md` | Fixture identity stub from T01 |

The before run is the failure case (marketing invention about real books). The after run is the success case (spec + next unchecked task + allowlisted facts). The fixture stays mid-project on purpose. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Books are long agent projects:** page counts and export folders only stay honest if they come from PROGRESS/FACTS files.
2. **One unchecked task:** the Prompt book itself resumes from Section 12 task ids the same way.
3. **THE END marker:** absent while later tasks remain; restored only after acceptance.
4. **True book facts:** Spark 800 pages and Signal 374p after margins/QR are file facts -- never marketing guesses.
