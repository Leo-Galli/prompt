# ch11-fix-pass

Companion folder for **Fixing Bad Results** (Prompt, Chapter 11).

Book steps live in the manuscript. This folder holds a soft release-note prompt that fails, diagnosis notes, a filled fix-pass prompt (from `templates/fix-pass.md`), trusted change facts, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Soft "polish it" release-note prompt |
| `after/` | Fix-pass prompt filled from the shared template |
| `diagnosis/` | Failure-class notes and reset-vs-continue decision |
| `fixture/` | Trusted fact allowlist for the `--ext` change |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `tests/` | File presence + shape checks |
| `../templates/fix-pass.md` | Shared targeted-repair template with `{{variables}}` |

## Run companion tests

```bash
cd ch11-fix-pass
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Skim `before/soft-release-note.md`. Note the soft success line ("feels ready to ship").
2. Paste it into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect invention and marketing shape.
3. Read `diagnosis/NOTES.md`, then open `../templates/fix-pass.md` and compare to `after/fix-pass-filled.md`.
4. Paste the after prompt. Compare FAILURE_CLASS + RELEASE_NOTE discipline to the before run.
5. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
