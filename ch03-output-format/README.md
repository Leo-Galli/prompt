# ch03-output-format

Companion folder for **Specifying the Output** (Prompt, Chapter 3).

Book steps live in the manuscript. This folder holds before/after prompts, saved outputs, exercises, and tests that check file presence plus JSON parse behavior.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Free-form bug summary ask used in the chapter |
| `after/` | Schema-constrained ask, soft JSON ask, and fix-pass prompt |
| `outputs/` | Real model runs plus provenance notes (never fabricated quotes) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + strict JSON parse checks |

## Run tests

```bash
cd ch03-output-format
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Paste `before/freeform-bug-summary.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename.
2. Paste `after/schema-bug-summary.md` the same way. Confirm the reply is raw JSON that parses.
3. Paste `after/failed-json-ask.md` to reproduce a soft JSON ask. If the reply includes fences, keep it as a failure sample.
4. Paste `after/fix-pass-json.md` (or adapt it to quote your failure). Save the repaired raw JSON.

Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
