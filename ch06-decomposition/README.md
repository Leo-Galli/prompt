# ch06-decomposition

Companion folder for **Decomposition and Chaining** (Prompt, Chapter 6).

Book steps live in the manuscript. This folder holds one overloaded mega-prompt that fails, a three-step chain that succeeds with handoff artifacts, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Overloaded single ask used in the chapter |
| `after/` | Step 1 plan, step 2 contract, step 3 verify |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + artifact-shape checks |

## Run tests

```bash
cd ch06-decomposition
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Paste `before/mega-prompt.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect format conflicts, allowlist slips, or hours overruns -- that is the lesson.
2. Run `after/step1-plan.md`, then paste its artifact into a fresh step-2 run (or use the frozen block already in `step2-contract.md`).
3. Run step 3 with both artifacts. Compare VERDICT PASS against the mega failure.
4. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
