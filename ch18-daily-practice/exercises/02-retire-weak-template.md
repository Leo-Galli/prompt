# Exercise 2 -- Retire one weak template

## Done when

- You pick a soft personal prompt (you may start from `fixture/weak-tips-prompt.md`)
- `python -m prompt_lint` on that file exits non-zero, or you document soft success lines that should not ship
- You move or rename it out of the default paste path (for example into `deprecated/`)
- You point consumers at a harder replacement (`templates/daily-card.md` or another lint-clean template)
- You write a one-line deprecation note a stranger can follow

## Steps

1. Run prompt-lint on the weak file. Keep the transcript.
2. List what is missing or soft (goal, output format, success criteria, invented metrics).
3. Move/rename the weak file off the default path.
4. Link the replacement path in a README bullet or deprecation note.
5. Do not leave "maybe useful" soft copies beside shared templates.

## Notes

Retire means remove from the default path. A sad comment left in `templates/` still gets pasted.
