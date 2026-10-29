# Exercise 02 -- Write a prepub audit stub

Goal: Draft a tiny `PREPUB_AUDIT.md` stub with BLOCKER / SHOULD FIX / OPTIONAL tables.

Done when:
- File has a one-line verdict placeholder.
- Three tables exist with headers: BLOCKER, SHOULD FIX, OPTIONAL.
- Each table has column headers at least: File | Problem | Status.
- You add one example OPTIONAL row about checking page count against the hard band.
- ASCII only. No invented Spark/Signal metrics.

Steps:
1. Copy the table shape from a real audit you trust, or start empty.
2. Leave BLOCKER and SHOULD FIX body rows empty (header only) if you have no findings.
3. Add the OPTIONAL page-band reminder row.
4. Stop. Do not fake blockers.

Verify: searching the stub finds the strings `BLOCKER`, `SHOULD FIX`, and `OPTIONAL` exactly as section headings.
