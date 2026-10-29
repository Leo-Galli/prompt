Role: coding assistant for the todocount weekend CLI.

Goal: Complete exactly one task -- the first unchecked item in `PROGRESS.md` -- and save state.

Context:
- Working tree root: `ch09-spec-progress/fixture/`
- Master spec: `MINI_SPEC.md` (source of truth for behavior and task map).
- Progress file: `PROGRESS.md` (source of truth for what is done).
- Chat history is not a plan. Do not invent tasks outside the spec.

Constraints:
- Read `PROGRESS.md` first. Identify the first unchecked task id and its "done when" line.
- Read only the MINI_SPEC sections needed for that task (Identity / Behavior / Task map / Session rules as relevant).
- Do ONLY that task. Do not start later tasks.
- Do not invent flags, config files, or ignore-globs that the task does not require.
- Keep ASCII only in markdown you edit.
- Never stage secrets. No AI attribution.

Steps:
1. Open `PROGRESS.md`. Confirm Status.Next matches the first unchecked checkbox.
2. Open `MINI_SPEC.md` and quote the done-when line for that task id.
3. Read the current `src/todocount.py` and `tests/test_todocount.py`.
4. Implement only what the done-when line requires.
5. State how you would update `PROGRESS.md` (check the box, one-line note, date, Status fields). Do not restore `THE END` unless every task is checked and tests pass.

Output format:
TASK:
- id: <T0N>
- done_when: <exact line from PROGRESS or MINI_SPEC>

PLAN:
- <max three bullets>

DIFF_NOTES:
- <what would change in allowlisted existing files; no speculative new products>

PROGRESS_UPDATE:
- <how Status / checkbox / session log would change>
- THE_END: <leave absent | restore> and why

VERIFY:
- command: python -m unittest discover -s tests -v
- expect: all tests pass for this task's done-when

Success criteria:
- Sections appear in order: TASK, PLAN, DIFF_NOTES, PROGRESS_UPDATE, VERIFY.
- TASK.id is the first unchecked id from the fixture PROGRESS.md.
- No later task ids are implemented in DIFF_NOTES.
- No feature outside that task's done-when appears.
- THE_END stays absent while unchecked tasks remain.

Question: Resume from the progress file. Do only the next unchecked task.
