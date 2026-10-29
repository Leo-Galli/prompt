# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 9. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-ignore-2026-10-29.md` | `../before/ignore-progress.md` | Ignores PROGRESS; invents ignore/JSON/config/CI; no single task id focus |
| `after-one-task-2026-10-29.md` | `../after/one-task-resume.md` | Reads PROGRESS; TASK.id T03 only; THE END stays absent |

Spec/progress artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../fixture/MINI_SPEC.md` | Master spec for the weekend CLI sample |
| `../fixture/PROGRESS.md` | Checklist with T01-T02 done, T03 next, THE END absent |
| `../fixture/src/todocount.py` | Partial CLI; `--ext` intentionally missing so readers can apply T03 |

The before run is the failure case (chat-as-plan, scope flood). The after run is the success case (spec + next unchecked task). The fixture stays mid-project on purpose. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Chat is not a plan:** long threads lose task order; files do not.
2. **One unchecked task:** resumable sessions need a single "done when" target.
3. **THE END marker:** absent while work is open; restored only when the checklist acceptance passes.
4. **True book facts:** Spark and Signal PROGRESS files show the same clear/restore pattern; Chapter 9 cites only numbers and phases recorded there.
