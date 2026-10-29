# Model output -- after (one-task resume from PROGRESS)

- Date: 2026-10-29
- Prompt: ../after/one-task-resume.md
- Context: single-turn coding-agent session used while authoring the companion folder; fixture PROGRESS left with T03 unchecked on purpose
- Note: Real reply to the resume prompt. TASK.id is T03; later tasks not implemented; THE END stays absent.

---

TASK:
- id: T03
- done_when: `--ext .py` limits the scan; tests cover filtered vs unfiltered; tests pass.

PLAN:
- Read `MINI_SPEC.md` Behavior item 3 and Task map T03; confirm Status.Next is T03.
- Add optional `--ext EXT` to the argparse parser and thread it into `count_todos`.
- Extend tests for unfiltered count vs `--ext .py` on a mixed `.py`/`.md` tree; run unittest.

DIFF_NOTES:
- `src/todocount.py`: add `--ext` argument; filter `path.suffix == ext` when provided; keep default scan unchanged.
- `tests/test_todocount.py`: keep existing count tests; add filtered vs unfiltered cases for `--ext .py`.
- No README, CHANGELOG, ignore-glob, JSON mode, or config file (those are later tasks or non-goals).

PROGRESS_UPDATE:
- Check off T03 with a one-line note and date; set Last completed: T03; Next: T04.
- Session log: note T03 closed and T04 next.
- THE_END: leave absent -- T04 and T05 remain unchecked, so acceptance is not complete.

VERIFY:
- command: python -m unittest discover -s tests -v
- expect: all tests pass for this task's done-when
