# Model output -- after (task relies on short rules)

- Date: 2026-10-29
- Prompt: ../after/task-relies-on-rules.md
- Context: single-turn coding-agent session used while authoring the companion folder; always-on rules are the short AGENTS.md
- Note: Real reply to the lean prompt. RULES_USED cites AGENTS.md and the unittest command from that file; allowlist honored; no utils package; full rules body not pasted back.

---

RULES_USED:
- Read fixture `AGENTS.md` (same short text as companion `after/short-rules.md`).
- Test command from rules: `python -m unittest discover -s tests -v` (fixture root).

PLAN:
- Add `--quiet` to `build_parser()` / `main()` so the summary line is skipped when set.
- Extend tests for default (summary present) vs quiet (summary absent, count still printed).
- Leave `count_lines` named as-is; no new packages.

DIFF_NOTES:
- `src/linecount.py`: `parser.add_argument("--quiet", action="store_true", help="Hide the files-scanned summary")`; print summary only when `not args.quiet`.
- `tests/test_linecount.py`: keep default summary assertion; add `test_quiet_hides_summary` that calls `main(["--quiet", str(path)])` and checks the count prints without `files scanned`.
- `docs/cli-style.md`: not edited; existing long-flag guidance already covers documenting `--quiet` when examples are updated in a docs task.

VERIFY:
- command: `python -m unittest discover -s tests -v`
- expect: all tests pass
