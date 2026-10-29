# ch01-how-models-read

Companion folder for **How Models Read a Prompt** (Prompt, Chapter 1).

Book steps live in the manuscript. This folder holds before/after prompts, saved outputs or honest notes, exercises, and a small file-presence test.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Vague / mixed prompts used in the chapter |
| `after/` | Delimited prompt that separates instructions from data |
| `outputs/` | Real model runs plus provenance notes (never fabricated quotes) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | Checks that required prompt files exist |

## Run tests

```bash
cd ch01-how-models-read
python -m unittest discover -s tests -v
```

## Re-run the worked example

1. Paste `before/vague-one-liner.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename.
2. Paste `after/delimited-prompt.md` the same way. Save that reply too.
3. Compare whether the refund imperative was obeyed or flagged.

Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
