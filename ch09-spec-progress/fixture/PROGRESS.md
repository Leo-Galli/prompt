# PROGRESS -- todocount

Source of truth for task state. Spec: `MINI_SPEC.md`.
Workflow: remove `THE END` while work is open; check items off when "done when" is met; restore `THE END` only when T01-T05 pass.

## Status
- Phase: Drafting
- Last completed: T02
- Next: T03
- Open issues: none

## Tasks

- [x] T01 Repo skeleton -- 2026-10-29: `src/todocount.py` + `tests/test_todocount.py` smoke import.
- [x] T02 Count TODOs -- 2026-10-29: default scan returns integer; unit tests pass.
- [ ] T03 Extension filter -- Done when: `--ext .py` limits the scan; tests cover filtered vs unfiltered; tests pass.
- [ ] T04 README usage -- Done when: README shows two example commands; ASCII only.
- [ ] T05 Release note -- Done when: `CHANGELOG.md` has a 0.1.0 section listing T01-T04 behaviors.

## Session log
- 2026-10-29 Spec opened: wrote MINI_SPEC + PROGRESS; T01-T02 closed; T03 next. THE END not restored (work open).
