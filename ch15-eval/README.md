# ch15-eval

Companion folder for **Evaluating Prompts** (Prompt, Chapter 15).

Book steps live in the manuscript. This folder holds a soft regressed triage prompt that fails a five-case set, a restored SEVERITY template that passes, golden cases, a CI-friendly scorer, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Regressed free-form triage ask (careless edit) |
| `after/` | Restored rubric + SEVERITY contract |
| `template/` | Reusable `label-severity.md` with `{{ISSUE_NOTE}}` |
| `cases/` | Five golden inputs + `EXPECTED.json` |
| `scripts/score_eval.py` | Pass/fail scorer for dated multi-case outputs |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + scorer regression checks |

## Run companion tests

```bash
cd ch15-eval
python -m unittest discover -s tests -v
```

## Score the saved runs

```bash
cd ch15-eval
python scripts/score_eval.py outputs/before-case-set-2026-10-29.md
python scripts/score_eval.py outputs/after-case-set-2026-10-29.md
```

Expect non-zero on before (regression) and zero on after.

## Re-run the worked examples

1. Skim `before/regressed-prompt.md`. Note soft success and missing rubric.
2. For each `cases/case-0N.md`, paste the issue note into the before prompt's `{{ISSUE_NOTE}}` slot. Save replies under `outputs/` with a dated filename.
3. Repeat with `after/restored-prompt.md` (or `template/label-severity.md`).
4. Run `scripts/score_eval.py` on both dated files.
5. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
