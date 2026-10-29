# Single-task session template

Fill every `{{variable}}`. Paste into a fresh chat or agent session.
Do not stack multiple task ids. ASCII only in files you edit.

---

Role: {{ROLE}}

Goal: Complete exactly one task -- {{TASK_ID}} -- and stop.

Context:
- Working tree / project root: {{PROJECT_ROOT}}
- Master spec (source of truth): {{SPEC_PATH}}
- Progress file (what is done): {{PROGRESS_PATH}}
- Chat history is not a plan. Do not invent tasks outside the spec.

Task:
- id: {{TASK_ID}}
- done_when: {{DONE_WHEN}}
- Spec sections to load (only these): {{SPEC_SECTIONS}}

Constraints:
- Do ONLY {{TASK_ID}}. Do not start later tasks.
- Meet the done_when line before proposing anything else.
- Do not invent flags, files, or features the task does not require.
- Keep ASCII only in markdown you edit.
- Never stage secrets. No AI attribution.
- End marker rule: leave `THE END` absent while any later task remains open; restore it only when every acceptance check for the project passes.

Steps:
1. Confirm Status.Next (or the first unchecked box) matches {{TASK_ID}}.
2. Read only the listed spec sections.
3. Read the allowlisted paths: {{ALLOWLIST}}
4. Implement only what done_when requires.
5. Run verify: {{VERIFY_COMMAND}}
6. State the PROGRESS update (checkbox, one-line note, date, Status fields). Do not rewrite old session-log lines.

Output format:
TASK:
- id: {{TASK_ID}}
- done_when: {{DONE_WHEN}}

PLAN:
- <max three bullets>

DIFF_NOTES:
- <paths and changes inside the allowlist only>

PROGRESS_UPDATE:
- <Status / checkbox / session log>
- THE_END: <leave absent | restore> and why

VERIFY:
- command: {{VERIFY_COMMAND}}
- result: <pass | fail | not run -- with reason>

Success criteria:
- Sections appear in order: TASK, PLAN, DIFF_NOTES, PROGRESS_UPDATE, VERIFY.
- TASK.id is exactly {{TASK_ID}}.
- No later task ids appear in DIFF_NOTES as work started.
- No feature outside done_when appears.
- THE_END rule above is respected.

Question: Do only {{TASK_ID}}. Stop when done_when is met.
