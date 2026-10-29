# ch05-reasoning

Companion folder for **Reasoning Prompts** (Prompt, Chapter 5).

Book steps live in the manuscript. This folder holds an answer-only ask vs a visible-steps ask on the same ticket-capacity problem, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Answer-only ask used in the chapter |
| `after/` | Visible numbered steps plus FINAL_ANSWER marker |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + output-shape checks |

## Run tests

```bash
cd ch05-reasoning
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Paste `before/answer-only.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename.
2. Paste `after/visible-steps.md` the same way. Compare clarity of the path to the final answer -- do not invent accuracy percentages.
3. Keep both dated files. Agreement on `FINAL_ANSWER` is common; the lesson is auditability.

Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
