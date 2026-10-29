# ch04-few-shot

Companion folder for **Examples and Few-Shot Prompting** (Prompt, Chapter 4).

Book steps live in the manuscript. This folder holds zero-shot vs 2-shot prompts, a deliberately bad example set, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Zero-shot classification ask used in the chapter |
| `after/` | 2-shot ask with good examples; bad-example ask that skews label and shape |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + output-shape checks |

## Run tests

```bash
cd ch04-few-shot
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Paste `before/zero-shot-classify.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename.
2. Paste `after/two-shot-classify.md` the same way. Compare label and format to the zero-shot run.
3. Paste `after/bad-example-classify.md` to see how poor examples skew the reply. Keep that failure as documentation.

Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
