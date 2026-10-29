# Output provenance

Files in this folder are real artifacts from 2026-10-29 while drafting Prompt Chapter 18. They are not hand-written fake transcripts for the model replies, and not invented exit codes for the lint runs.

| File | Source | Notes |
| --- | --- | --- |
| `lint-fail-before-2026-10-29.md` | `python -m prompt_lint before/vague-daily-ask.md` | Exit 1; missing goal, output format, success criteria |
| `lint-pass-daily-card-2026-10-29.md` | `python -m prompt_lint after/filled-daily-card.md` | Exit 0 |
| `before-vague-daily-2026-10-29.md` | `../before/vague-daily-ask.md` | Soft tips ask; invents Prompt Gym, 40% claim, badges |
| `after-daily-card-2026-10-29.md` | `../after/filled-daily-card.md` | Filled daily card; SEVERITY_NOTE stays inside FACTS |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../after/filled-daily-card.md` | One filled daily card instance |
| `../fixture/FACTS.md` | Allowlisted product facts for the severity note |
| `../fixture/weak-tips-prompt.md` | Soft personal prompt to retire (Exercise 2) |
| `../../templates/daily-card.md` | Shared daily-card template at repo root |

Re-run lint locally with `PYTHONPATH=. python -m prompt_lint <path>`. Re-run the filled card in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Vague daily tips asks** invent branded routines and fake improvement percents.
2. **A filled daily card** locks one job, trusted facts, lint, and a save path.
3. **prompt-lint** fails incomplete before asks before anyone pastes them.
4. **Retiring weak prompts** keeps soft copies out of the default path.
5. **Chat vs agent** is a sizing choice, not a productivity upgrade mid-ask.
