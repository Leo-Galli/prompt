# Output provenance

Files in this folder are real artifacts from 2026-10-29 while drafting Prompt Chapter 16. They are not hand-written fake transcripts for the model replies, and not invented exit codes for the lint runs.

| File | Source | Notes |
| --- | --- | --- |
| `lint-fail-2026-10-29.md` | `python -m prompt_lint fixture/lint-fail.md` | Exit 1; missing output format and success criteria |
| `lint-pass-2026-10-29.md` | `python -m prompt_lint fixture/lint-pass.md` | Exit 0 |
| `before-raw-changelog-2026-10-29.md` | `../before/raw-chat-prompt.md` | Soft chat ask; invents stars, speedup, dashboard, AI hints |
| `after-templated-changelog-2026-10-29.md` | `../fixture/FILLED_CHANGELOG.md` | Filled template; CHANGELOG block stays inside trusted changes |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../after/templated-changelog.md` | Library template with `{{variables}}` |
| `../fixture/lint-fail.md` / `lint-pass.md` | Minimal fixtures for the CLI fail-then-pass demo |
| `../fixture/FILLED_CHANGELOG.md` | One filled instance used for the after model run |
| `../../templates/master-spec.md` | Shared master-spec template at repo root |
| `../../prompt_lint/` | CLI that gates goal / output format / success criteria |

Re-run lint locally with `PYTHONPATH=. python -m prompt_lint <path>`. Re-run the filled changelog prompt in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Raw chat prompts** invent metrics when no trusted change list exists.
2. **Templates with variables** lock the contract and the fill slots.
3. **prompt-lint** fails incomplete templates before anyone pastes them.
4. **Version tags** on templates make PR review and deprecation possible.
5. **Library layout** keeps shared skeletons under `templates/` and chapter demos under `ch16-library/`.
