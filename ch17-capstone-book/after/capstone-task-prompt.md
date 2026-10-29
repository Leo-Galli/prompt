# Capstone one-task session (kitbook fixture)

Pattern matches how the Prompt book project itself is run: load BOOK_SPEC/MINI_SPEC,
read PROGRESS, do only the first unchecked task, respect THE END, cite verified facts only.

Fill is already done for this fixture. Paste into a fresh agent session rooted at
`ch17-capstone-book/fixture/`.

---

Role: coding assistant for the kitbook fixture.

Goal: Complete exactly one task -- T04 -- and stop.

Context:
- Working tree / project root: `ch17-capstone-book/fixture/`
- Master spec (source of truth): `MINI_SPEC.md`
- Progress file: `PROGRESS.md`
- Verified Spark/Signal facts: `FACTS.md` only
- Chat history is not a plan. Do not invent tasks outside the spec.

Task:
- id: T04
- done_when: `chapter-stub.md` exists; H1 title only (no "Chapter N:"); cites only FACTS.md Spark/Signal lines; <= 400 words; ASCII
- Spec sections to load: Identity, Hard limits, Task map T04, Session rules, Acceptance

Constraints:
- Read `PROGRESS.md` first. Confirm Status.Next is T04 and T04 is the first unchecked box.
- Do ONLY T04. Do not start T05. Do not restore `THE END`.
- Cite Spark/Signal numbers only from `FACTS.md`. If a number is missing, write UNKNOWN or omit -- never invent.
- Keep ASCII only. No emoji. No AI attribution.
- End marker rule: leave `THE END` absent while T05 remains open.

Steps:
1. Confirm Status.Next matches T04.
2. Read MINI_SPEC sections listed above and quote the T04 done-when line.
3. Read `FACTS.md` completely before drafting.
4. Write `chapter-stub.md` only (create the file). Do not edit MINI_SPEC or FACTS.md.
5. State the PROGRESS update (checkbox, one-line note, date, Status fields). Do not rewrite old session-log lines.
6. Stop. Do not write ACCEPTANCE.md (that is T05).

Output format:
TASK:
- id: T04
- done_when: <exact done-when text>

PLAN:
- <max three bullets>

DIFF_NOTES:
- <paths and changes; allowlist: chapter-stub.md create only>

PROGRESS_UPDATE:
- <Status / checkbox / session log>
- THE_END: <leave absent | restore> and why

VERIFY:
- command: python -c "from pathlib import Path; p=Path('chapter-stub.md'); t=p.read_text(encoding='ascii'); assert not t.startswith('# Chapter'); assert len(t.split())<=400; print('ok', len(t.split()), 'words')"
- result: <pass | fail | not run -- with reason>

FACTS_USED:
- <bullet list of Spark/Signal lines copied from FACTS.md only>

Success criteria:
- Sections appear in order: TASK, PLAN, DIFF_NOTES, PROGRESS_UPDATE, VERIFY, FACTS_USED.
- TASK.id is exactly T04.
- No T05 work and no invented Spark/Signal metrics.
- THE_END stays absent.
- Every number under FACTS_USED appears in FACTS.md.

Question: Resume from PROGRESS. Do only T04.
