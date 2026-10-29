Role: coding assistant for the sample linecount fixture.

Goal: Add a `--quiet` flag that suppresses the "N files scanned" summary line on stdout, while still printing the numeric line count.

Context:
- Working tree root: `ch08-repo-rules/fixture/` (paths below are relative to that root).
- Always-on rules: read `AGENTS.md` at the fixture root (same text as `../after/short-rules.md` in the companion folder). Follow it. Do not restate those rules in your reply.
- Canonical CLI flag examples live in `docs/cli-style.md` (pointer from AGENTS.md).
- Allowlisted paths you may edit (and only these):
  - `src/linecount.py`
  - `tests/test_linecount.py`
  - `docs/cli-style.md` (only if you must add a `--quiet` example line)

Constraints:
- Rely on AGENTS.md for style, test command, ASCII, commit voice, and "no new packages."
- Do not paste a second copy of AGENTS.md into the plan.
- Do not create `src/utils/` or rename `count_lines`.

Steps:
1. Read `AGENTS.md`, `src/linecount.py`, and `tests/test_linecount.py`.
2. Implement `--quiet` with a minimal diff.
3. Add or extend tests for quiet vs default.
4. Stop.

Output format:
RULES_USED:
- <one bullet: which always-on file you read>
- <one bullet: test command taken from rules (do not invent a different one)>

PLAN:
- <max three bullets>

DIFF_NOTES:
- <what changed in allowlisted paths>

VERIFY:
- command: <exact test command from AGENTS.md>
- expect: all tests pass

Success criteria:
- Sections appear in order: RULES_USED, PLAN, DIFF_NOTES, VERIFY.
- RULES_USED cites AGENTS.md and the unittest discover command from that file.
- Only allowlisted paths are edit targets.
- No utils package, no API rename.
- Reply does not paste the full AGENTS.md body.

Question: Add `--quiet` using the short repo rules instead of a pasted rule novel.
