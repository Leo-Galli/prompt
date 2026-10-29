# ch13-media

Companion folder for **Prompts for Images, Video and Presentations** (Prompt, Chapter 13).

Book steps live in the manuscript. This folder holds a vague image ask that fails, a structured image brief, a six-slide outline prompt, brand locks, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Vague "make it pop" hero-image ask |
| `after/` | Structured image brief + six-slide outline prompts |
| `fixture/` | Brand locks (colors, mark, negatives, accessibility) |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |

## Run companion tests

```bash
cd ch13-media
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Skim `before/vague-image-ask.md`. Note soft success ("looks cool" / "ready to generate") and the invitation to invent a UI screenshot.
2. Paste it into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect neon tropes and fake chrome.
3. Open `fixture/BRAND_LOCKS.md`, then paste `after/structured-image-brief.md`.
4. Paste `after/slide-outline.md` for the six-slide outline.
5. Compare BRIEF fields and S1..S6 blocks to the before scene dump.
6. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
