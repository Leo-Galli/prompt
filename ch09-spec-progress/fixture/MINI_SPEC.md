# MINI_SPEC -- todocount

Single source of truth for this weekend CLI sample. ASCII only. No emoji.

## Identity

- Name: todocount
- Goal: Count `TODO` markers in text files under a path
- Language: Python 3.11+
- License: MIT (sample only)

## Behavior

1. Default: scan a directory path recursively for `TODO` (case-sensitive substring).
2. Print one integer count to stdout and exit 0.
3. Optional `--ext EXT` (example: `--ext .py`) limits scanned files to that suffix.
4. Do not invent other flags in early tasks.
5. Tests live under `tests/` and run with `python -m unittest discover -s tests -v`.

## Non-goals

- No network calls
- No config files
- No ignore-glob in tasks T01-T05
- No AI attribution in commits

## Task map (ordered)

| ID | Task | Done when |
| --- | --- | --- |
| T01 | Repo skeleton | `src/todocount.py` and `tests/test_todocount.py` exist; smoke import works. |
| T02 | Count TODOs | Default scan returns a correct integer for the fixture tree; tests pass. |
| T03 | Extension filter | `--ext .py` limits the scan; tests cover filtered vs unfiltered; tests pass. |
| T04 | README usage | README shows two example commands; ASCII only. |
| T05 | Release note | `CHANGELOG.md` has a 0.1.0 section listing T01-T04 behaviors. |

## Session rules

- Spec is the source of truth. Chat history is not a plan.
- Do only the first unchecked task in `PROGRESS.md`.
- Meet that task's "done when" line before starting another.
- Remove trailing `THE END` from `PROGRESS.md` while work is open.
- Check the task off with a one-line note and the date when done.
- Put `THE END` back only when T01-T05 are all checked and tests pass.
