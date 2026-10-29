# ch16-library

Companion folder for **A Prompt Library** (Prompt, Chapter 16).

Book steps live in the manuscript. This folder holds a raw chat changelog ask that invents metrics, a templated changelog with `{{variables}}`, lint fixtures that fail then pass under `prompt-lint`, saved outputs, exercises, and tests.

Shared library templates also live at repo root under `templates/` (`master-spec.md`, `single-task.md`, `fix-pass.md`).

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Raw chatty changelog ask (fails lint; invites invention) |
| `after/` | Templated changelog with variables + version tag |
| `fixture/` | Minimal lint-fail / lint-pass files + one filled changelog instance |
| `outputs/` | Real lint transcripts + model runs (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + lint regression checks |

## Run companion tests

```bash
cd ch16-library
PYTHONPATH=.. python -m unittest discover -s tests -v
```

## Run prompt-lint on the fixtures

From the companion repo root:

```bash
PYTHONPATH=. python -m prompt_lint ch16-library/fixture/lint-fail.md
PYTHONPATH=. python -m prompt_lint ch16-library/fixture/lint-pass.md
PYTHONPATH=. python -m prompt_lint ch16-library/after/templated-changelog.md
PYTHONPATH=. python -m prompt_lint templates/
```

Expect non-zero on lint-fail and before raw prompt; zero on lint-pass, after template, and `templates/`.

## Re-run the worked examples

1. Skim `before/raw-chat-prompt.md`. Note missing Goal / Output format / Success criteria.
2. Paste it into a chat with only the product name as context. Save the reply under `outputs/` with a dated filename.
3. Fill `after/templated-changelog.md` (or use `fixture/FILLED_CHANGELOG.md`). Save the reply.
4. Run prompt-lint on `fixture/lint-fail.md` then `fixture/lint-pass.md`. Keep dated transcripts.
5. Do not invent replies or exit codes. If you cannot run a model, keep notes in `outputs/NOTES.md` and skip quoting a model reply in your own write-up.
