# Exercise 01 -- Map Section 12 tasks to session prompts

Goal: Turn Prompt `BOOK_SPEC.md` Section 12 rows into paste-ready one-task openers.

Done when:
- You list five task ids from Section 12 (example: T19-T23 or T21-T25).
- For each id you write a 6-12 line session prompt with: Role, Goal (one id), Spec sections to load, done_when quote, THE END rule, Output format headings.
- No prompt stacks two task ids.
- ASCII only.

Steps:
1. Open the book's Section 12 table (or this repo's chapter text that mirrors it).
2. Pick five consecutive unfinished-style ids.
3. Fill `templates/single-task.md` once per id (or write equivalent text).
4. Save your five prompts under a local notes folder (do not commit secrets).

Verify: each prompt contains exactly one `TASK_ID` / `T0N` and the words `THE END`.
