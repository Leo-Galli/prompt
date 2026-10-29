# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 15. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-case-set-2026-10-29.md` | `../before/regressed-prompt.md` | Soft free-form triage on all five cases; wrong labels + missing SEVERITY shape |
| `after-case-set-2026-10-29.md` | `../after/restored-prompt.md` | Restored rubric + SEVERITY contract; labels match EXPECTED.json |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../template/label-severity.md` | Golden template with `{{ISSUE_NOTE}}` |
| `../cases/EXPECTED.json` | Five expected labels for the mini test set |
| `../cases/case-01.md` ... `case-05.md` | Golden inputs |
| `../scripts/score_eval.py` | CI-friendly pass/fail scorer |

The before run is the regression case (careless edit removed rubric and shape). The after run is the restored case. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Golden cases:** five fixed inputs with expected labels beat vibes.
2. **Rubrics:** HIGH/MED/LOW meanings must be written down or scores drift.
3. **Regression:** a "simplify the prompt" edit can fail the same set overnight.
4. **Smoke vs deep:** shape checks catch missing SEVERITY; deep review still reads reasons.
5. **No fake benchmarks:** pass/fail on your cases is not a published accuracy study.
