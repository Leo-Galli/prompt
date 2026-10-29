# Exercise 2 -- Score two prompt versions

Goal: Compare the regressed prompt and the restored prompt on the same five cases.

Done when:
- You run (or manually score) both dated outputs against `cases/EXPECTED.json`
- You record pass/fail per case for before and after
- You name at least one failure class for each before miss (wrong format, wrong label, missing evidence)
- You do not invent an accuracy percentage for a published benchmark

Commands:

```bash
cd ch15-eval
python scripts/score_eval.py outputs/before-case-set-2026-10-29.md
python scripts/score_eval.py outputs/after-case-set-2026-10-29.md
```

Expected shape: before fails; after passes. If your own re-run differs in wording but matches labels, keep a new dated file and score that file instead.
