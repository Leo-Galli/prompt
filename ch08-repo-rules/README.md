# ch08-repo-rules

Companion folder for **Repository Rules That Stick** (Prompt, Chapter 8).

Book steps live in the manuscript. This folder holds a bloated always-on rules file, a short rules file with pointers, a task that pastes rules into chat, a lean task that relies on AGENTS.md, a small linecount fixture, saved outputs, exercises, and tests.

## Layout

| Path | Purpose |
| --- | --- |
| `before/` | Bloated AGENTS-style rules + task that repeats the novel |
| `after/` | Short rules with pointers + lean task that relies on them |
| `fixture/` | Sample CLI + short `AGENTS.md` + canonical docs pointers |
| `outputs/` | Real model runs plus provenance notes (never fabricated) |
| `exercises/` | Starter files for the three chapter exercises |
| `scripts/` | CI-friendly check that rules mention the test command |
| `tests/` | File presence + shape checks |

## Run companion tests

```bash
cd ch08-repo-rules
python -m unittest discover -s tests -v
```

## Check that rules mention tests

```bash
python scripts/check_rules_mention_tests.py fixture/AGENTS.md
```

## Fixture tests (CLI without --quiet yet)

```bash
cd ch08-repo-rules/fixture
python -m unittest discover -s tests -v
```

## Re-run the worked examples

1. Skim `before/bloated-rules.md`. Note how late the critical path notes appear.
2. Paste `before/task-repeats-rules.md` into your chat or agent product. Save the reply under `outputs/` with a dated filename. Expect restated policy noise and scope creep.
3. Paste `after/task-relies-on-rules.md` with `fixture/AGENTS.md` available. Compare RULES_USED and allowlist discipline to the before run.
4. Keep dated files. Do not invent replies. If you cannot run a model, keep the notes in `outputs/NOTES.md` and skip quoting an output in your own write-up.
