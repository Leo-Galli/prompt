# Exercise 3 -- CI-friendly check script stub

Goal: Wire a tiny scorer into a local or CI command so a prompt edit fails loudly.

Done when:
- `python scripts/score_eval.py outputs/after-case-set-2026-10-29.md` exits 0
- The same command on the before output exits non-zero
- You write three bullet lines describing where you would call the script (pre-commit, GitHub Action step, or Makefile target)
- You do not claim the stub measures model quality in general -- only label match on this set

Stretch: point the script at a new dated output from your own re-run and keep EXPECTED.json unchanged unless the rubric itself changed on purpose.
