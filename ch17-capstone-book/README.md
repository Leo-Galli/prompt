# ch17-capstone-book

Companion folder for Prompt Chapter 17 -- Capstone: Build a Book with an AI Agent.

## Layout

| Path | Purpose |
| --- | --- |
| `before/invent-book-stats.md` | Hype prompt that asks for invented Spark/Signal metrics |
| `after/capstone-task-prompt.md` | One-task resume (T04) with FACTS allowlist + THE END rule |
| `fixture/` | kitbook MINI_SPEC, PROGRESS (T04 next), FACTS.md, README |
| `outputs/` | Dated real model replies + provenance notes |
| `exercises/` | Map Section 12 tasks; prepub stub; Section 13 checks |
| `tests/` | File and honesty smoke tests (no live model calls) |

## Quick test

```bash
python -m unittest discover -s ch17-capstone-book/tests -v
```

Exercise steps are printed in the book. This folder does not contain the manuscript.
