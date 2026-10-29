# ch02-anatomy

Companion folder for **The Anatomy of a Good Prompt** (Prompt, Chapter 2).

Book steps live in the manuscript. This folder holds before/after prompts, saved outputs, exercises, and a small file-presence test.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Chatty, unstructured request used in the chapter |
| `after/` | Same task filled into the seven-part skeleton |
| `outputs/` | Real model runs plus provenance notes (never fabricated quotes) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | Checks that required prompt files exist |

## Run tests

```bash
cd ch02-anatomy
python -m unittest discover -s tests -v
```

## Re-run the worked example

1. Paste `before/chatty-readme-ask.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename.
2. Paste `after/skeleton-readme-ask.md` the same way. Save that reply too.
3. Compare whether the after reply matches the required sections and constraints.

Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
