# Exercise 3: CI check that rules mention the test command

Book steps live in the manuscript. Use this file as your working sheet.

## Your task

Add a cheap guard so always-on rules cannot "lose" the test command.

1. Choose the rules file path (`AGENTS.md`, `.cursor/rules/*.mdc`, or tool equivalent).
2. Choose the exact substring that must appear (for the fixture: `python -m unittest discover -s tests -v`).
3. Write a CI step or script that fails if the substring is missing.
4. Optionally run the sample check script under `../scripts/check_rules_mention_tests.py` against `../fixture/AGENTS.md` and against `../before/bloated-rules.md` (bloated still mentions the command -- note that presence alone does not fix bury-and-miss; the chapter still wants the string findable and the file short).

## Draft CI step

```yaml
# paste a GitHub Actions step or a shell one-liner here
```

## Notes

- What other always-on strings would you guard next (license, "no secrets", ASCII)?
