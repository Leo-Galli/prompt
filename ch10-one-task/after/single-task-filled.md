Role: coding assistant for the todocount weekend CLI.

Goal: Complete exactly one task -- T03 -- and stop.

Context:
- Working tree / project root: `ch10-one-task/fixture/`
- Master spec (source of truth): `MINI_SPEC.md`
- Progress file (what is done): `PROGRESS.md`
- Chat history is not a plan. Do not invent tasks outside the spec.

Task:
- id: T03
- done_when: `--ext .py` limits the scan; tests cover filtered vs unfiltered; tests pass.
- Spec sections to load (only these): Identity; Behavior items 1-4; Task map row T03; Session rules

Constraints:
- Do ONLY T03. Do not start later tasks.
- Meet the done_when line before proposing anything else.
- Do not invent flags, files, or features the task does not require.
- Keep ASCII only in markdown you edit.
- Never stage secrets. No AI attribution.
- End marker rule: leave `THE END` absent while any later task remains open; restore it only when every acceptance check for the project passes.

Steps:
1. Confirm Status.Next (or the first unchecked box) matches T03.
2. Read only the listed spec sections.
3. Read the allowlisted paths: `src/todocount.py`, `tests/test_todocount.py`, `PROGRESS.md`, `MINI_SPEC.md`
4. Implement only what done_when requires.
5. Run verify: `python -m unittest discover -s tests -v`
6. State the PROGRESS update (checkbox, one-line note, date, Status fields). Do not rewrite old session-log lines.

Output format:
TASK:
- id: T03
- done_when: `--ext .py` limits the scan; tests cover filtered vs unfiltered; tests pass.

PLAN:
- <max three bullets>

DIFF_NOTES:
- <paths and changes inside the allowlist only>

PROGRESS_UPDATE:
- <Status / checkbox / session log>
- THE_END: <leave absent | restore> and why

VERIFY:
- command: `python -m unittest discover -s tests -v`
- result: <pass | fail | not run -- with reason>

Success criteria:
- Sections appear in order: TASK, PLAN, DIFF_NOTES, PROGRESS_UPDATE, VERIFY.
- TASK.id is exactly T03.
- No later task ids appear in DIFF_NOTES as work started.
- No feature outside done_when appears.
- THE_END rule above is respected.

Question: Do only T03. Stop when done_when is met.
