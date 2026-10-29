# ch07-code

Companion folder for **Prompting for Code** (Prompt, Chapter 7).

Book steps live in the manuscript. This folder holds a vague "fix the bug" ask that creeps scope, a scoped fix prompt with read-first and failing-test-first rules, a small buggy fixture, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Vague fix ask used in the chapter |
| `after/` | Scoped fix with allowlist, read-first, tests as acceptance |
| `fixture/` | Buggy `format_duration` plus incomplete tests (bug kept on purpose) |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |

## Run companion tests

```bash
cd ch07-code
python -m unittest discover -s tests -v
```

## Reproduce the fixture bug

```bash
cd ch07-code/fixture
# PowerShell: $env:PYTHONPATH="src"
# bash: export PYTHONPATH=src
python -c "from format_duration import format_duration; print(format_duration(3665))"
python -m unittest discover -s tests -v
```

Expect `1h 1m` for input `3665`, and a green suite that never asserts hours+minutes+seconds together.

## Re-run the worked examples

1. Paste `before/vague-fix.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect renames, new modules, or missing acceptance tests -- that is the lesson.
2. Paste `after/scoped-fix.md` (point the agent at `fixture/`). Compare read notes, failing test, and one-condition fix against the vague run.
3. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
