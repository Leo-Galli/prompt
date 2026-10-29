# ch12-documents

Companion folder for **Prompts for Documents and Books** (Prompt, Chapter 12).

Book steps live in the manuscript. This folder holds a vague "write a chapter" prompt that fails, an outline-bound drafting prompt with voice and continuity locks, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Vague "write chapter 3" prompt |
| `after/` | Outline-bound G03 draft prompt (budget + voice + continuity) |
| `fixture/` | Mini outline, voice rules, continuity ledger |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |

## Run companion tests

```bash
cd ch12-documents
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Skim `before/vague-write-chapter.md`. Note the soft success line ("feels ready to publish").
2. Paste it into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect hype, invention, and missing budgets.
3. Open `fixture/MINI_OUTLINE.md`, `VOICE_RULES.md`, and `CONTINUITY.md`, then paste `after/outline-bound-chapter.md`.
4. Compare META + three locked headings to the before essay.
5. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
