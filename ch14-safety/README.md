# ch14-safety

Companion folder for **Safety and Honesty** (Prompt, Chapter 14).

Book steps live in the manuscript. This folder holds a soft invent-statistic ask that fails, a cited/allowlist blurb prompt, an educational untrusted-block drill, fixtures, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Soft invent-statistic launch-blurb ask |
| `after/` | Cited/allowlist BLURB + untrusted-block STATUS prompts |
| `fixture/` | TRUSTED_FACTS allowlist + labeled UNTRUSTED_PASTE |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |

## Run companion tests

```bash
cd ch14-safety
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Skim `before/invent-statistic.md`. Note soft success and the invitation to invent numbers.
2. Paste it into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect fluent fake metrics.
3. Open `fixture/TRUSTED_FACTS.md`, then paste `after/cited-urls-only.md`.
4. Paste `after/untrusted-block.md` (or load `fixture/UNTRUSTED_PASTE.md`) for the injection-education drill.
5. Compare UNKNOWN fields and STATUS refusal lines to the before blurb.
6. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.

## Safety note

The untrusted paste is educational. It is not an exploit guide. Do not paste live secrets into demos. Do not use the override-style lines against systems you do not own.
