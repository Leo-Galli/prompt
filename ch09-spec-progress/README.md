# ch09-spec-progress

Companion folder for **Long Agent Projects: Spec and Progress** (Prompt, Chapter 9).

Book steps live in the manuscript. This folder holds a mini master spec, a mid-project progress file, a bad session prompt that ignores progress, a one-task resume prompt, a partial todocount fixture, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Session prompt that ignores PROGRESS and floods scope |
| `after/` | Resume prompt that loads spec + first unchecked task |
| `fixture/` | Mini-spec, PROGRESS (T03 next), partial CLI without `--ext` |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |

## Run companion tests

```bash
cd ch09-spec-progress
python -m unittest discover -s tests -v
```

## Fixture tests (CLI without --ext yet)

```bash
cd ch09-spec-progress/fixture
PYTHONPATH=. python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Read `fixture/PROGRESS.md`. Note T03 is next and `THE END` is absent.
2. Paste `before/ignore-progress.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect invented extras and no single task id.
3. Paste `after/one-task-resume.md` with the fixture available. Compare TASK.id and THE_END handling to the before run.
4. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
