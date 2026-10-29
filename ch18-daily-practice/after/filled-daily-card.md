# Filled daily card (todocount severity note)

Filled from `templates/daily-card.md` @ daily-card@0.1.0 for the Chapter 18 worked example.
Paste into chat. One job only.

---

DAILY_CARD
date: 2026-10-29
tool: chat
job: Write one README severity note for todocount issue triage.

Role: technical writer for a small CLI readme.

Goal: Produce one severity note a maintainer can paste under Contributing.

Context:
- Trusted facts only (do not invent stars, speedups, or user counts):
FACTS:
product: todocount
kind: weekend CLI that counts TODO/FIXME markers in a tree
issue: #12
symptom: nested directories were skipped when the user passed a relative path with ..
severity_label: medium
owner: maintainers
fix_status: patch in progress on branch fix/nested-relpath
doc_target: README Contributing section
- Do not invent metrics, quotes, or product claims missing from FACTS.

Constraints:
- ASCII only.
- No emoji.
- At most 80 words in the note body.
- Use severity_label exactly as given.
- If a fact is missing, write UNKNOWN -- never invent.

Steps:
1. Confirm Goal, Output format, and Success criteria are filled.
2. Run: `python -m prompt_lint` on this filled card path.
3. Run the ask once in chat.
4. Save the raw reply to outputs/after-daily-card-2026-10-29.md.
5. Stop. Do not start a second job on this card.

Output format:
SEVERITY_NOTE:
- product: <from FACTS>
- issue: <from FACTS>
- severity: <from FACTS>
- body: < <= 80 words; facts only >
LINT:
- command: python -m prompt_lint ch18-daily-practice/after/filled-daily-card.md
- result: <exit 0 | fail>
SAVE:
- path: outputs/after-daily-card-2026-10-29.md

Success criteria:
- Sections appear in order: SEVERITY_NOTE, LINT, SAVE.
- Every concrete claim in body appears in FACTS.
- body word count <= 80.
- No invented star counts, speedups, or badges.
- LINT.result is exit 0 (or records the real exit code).

LINT_COMMAND: python -m prompt_lint ch18-daily-practice/after/filled-daily-card.md
SAVE_PATH: outputs/after-daily-card-2026-10-29.md

Question: Fill SEVERITY_NOTE, LINT, and SAVE for today's card. Use FACTS only.
