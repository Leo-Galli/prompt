# Model output -- before (regressed prompt on 5-case set)

- Date: 2026-10-29
- Prompt: ../before/regressed-prompt.md
- Cases: ../cases/case-01.md ... case-05.md
- Context: single-turn coding-agent session used while authoring the companion folder; agent told only the soft triage ask with free-form success ("feels decisive")
- Note: Real replies to the regressed prompt. Wrong labels and missing SEVERITY shape are the teaching point. score_eval.py on this file must FAIL.

---

## case-01
This looks critical -- empty path blows up with a traceback. I'd call it a blocker and maybe bump it above docs work. Ship a guard soon.

## case-02
Medium. Help text typos make the CLI look sloppy and can confuse new users, so I would not leave it forever. Not a crash though.

## case-03
High severity. Wrong counts in nested trees mean people cannot trust the tool. Treat it like a product-breaking bug until the walk is fixed.

## case-04
Low / docs. README should show `todocount --ext .py ./src`. Easy fix when someone has a spare minute.

## case-05
Pretty bad. Overwriting a user notes file through the cache path without a warning is unacceptable. Prioritize it.
