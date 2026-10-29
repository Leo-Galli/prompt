# ch18-daily-practice

Companion folder for **From First Prompt to Daily Practice** (Prompt, Chapter 18).

Book steps live in the manuscript. This folder holds a vague daily-tips ask that invents a branded gym and a fake improvement percent, a filled daily card with lint and save lines, FACTS for a severity note, a weak prompt fixture to retire, saved outputs, exercises, and tests.

Shared daily card template: `templates/daily-card.md`.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Vague tips ask (fails lint; invites invention) |
| `after/` | Filled daily card for one severity-note job |
| `fixture/` | FACTS allowlist + weak tips prompt to retire |
| `outputs/` | Real lint transcripts + model runs (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + lint / output regression checks |

## Run companion tests

```bash
cd ch18-daily-practice
PYTHONPATH=.. python -m unittest discover -s tests -v
```

## Run prompt-lint on the demos

From the companion repo root:

```bash
PYTHONPATH=. python -m prompt_lint ch18-daily-practice/before/vague-daily-ask.md
PYTHONPATH=. python -m prompt_lint ch18-daily-practice/after/filled-daily-card.md
PYTHONPATH=. python -m prompt_lint ch18-daily-practice/fixture/weak-tips-prompt.md
PYTHONPATH=. python -m prompt_lint templates/daily-card.md
```

Expect non-zero on before and weak-tips; zero on filled card and `templates/daily-card.md`.

## Re-run the worked examples

1. Skim `before/vague-daily-ask.md`. Note missing Goal / Output format / Success criteria.
2. Paste it into a chat with no trusted facts. Save the reply under `outputs/` with a dated filename.
3. Fill `templates/daily-card.md` (or use `after/filled-daily-card.md`). Save the reply.
4. Run prompt-lint on before then after. Keep dated transcripts.
5. Do not invent replies or exit codes. If you cannot run a model, keep notes in `outputs/NOTES.md` and skip quoting a model reply in your own write-up.
