# Model output -- after (single-task template filled for T03)

- Date: 2026-10-29
- Prompt: ../after/single-task-filled.md (filled from ../../templates/single-task.md)
- Context: single-turn coding-agent session used while authoring the companion folder; fixture PROGRESS left with T03 unchecked on purpose
- Note: Real reply to the single-task prompt. TASK.id is T03 only; later tasks not started; THE END stays absent.

---

TASK:
- id: T03
- done_when: `--ext .py` limits the scan; tests cover filtered vs unfiltered; tests pass.

PLAN:
- Confirm Status.Next is T03 and load Behavior items 1-4 plus Task map row T03.
- Add optional `--ext EXT` to argparse and filter `path.suffix` inside `count_todos`.
- Extend unit tests for unfiltered vs `--ext .py` on a mixed `.py`/`.md` tree; run unittest.

DIFF_NOTES:
- `src/todocount.py`: add `--ext`; when set, only count files whose suffix matches; default scan unchanged.
- `tests/test_todocount.py`: keep existing count tests; add filtered vs unfiltered cases for `--ext .py`.
- No README, CHANGELOG, ignore-glob, JSON mode, config, or CI (those are later tasks or non-goals).

PROGRESS_UPDATE:
- Check off T03 with a one-line note and date; set Last completed: T03; Next: T04.
- Append session log: T03 closed; T04 next.
- THE_END: leave absent -- T04 and T05 remain unchecked, so project acceptance is not complete.

VERIFY:
- command: `python -m unittest discover -s tests -v`
- result: not run in this planning turn -- command is the acceptance gate before checking the box; expect all tests pass for T03 done_when
