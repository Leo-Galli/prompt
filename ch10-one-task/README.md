# ch10-one-task

Companion folder for **One Task Per Session** (Prompt, Chapter 10).

Book steps live in the manuscript. This folder holds an overloaded multi-task session prompt, a filled single-task prompt (from `templates/single-task.md`), a mid-project todocount fixture, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Overloaded "clear the backlog" session prompt |
| `after/` | Single-task prompt filled from the shared template |
| `fixture/` | Mini-spec + PROGRESS (T03 next) + partial CLI |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |
| `../templates/single-task.md` | Shared one-task-per-session template with `{{variables}}` |

## Run companion tests

```bash
cd ch10-one-task
python -m unittest discover -s tests -v
```

## Fixture tests (CLI without --ext yet)

```bash
cd ch10-one-task/fixture
PYTHONPATH=. python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Skim `before/overloaded-session.md`. Note how it asks for T03-T05 plus bonuses.
2. Paste it into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect a BATCH of several areas.
3. Open `../templates/single-task.md`, then compare to `after/single-task-filled.md`.
4. Paste the after prompt with the fixture available. Compare TASK.id discipline to the before run.
5. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
