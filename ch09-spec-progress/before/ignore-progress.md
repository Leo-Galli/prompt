Role: coding assistant for the todocount weekend CLI.

Goal: Finish the entire product in this one session. Ship everything the project might need.

Context:
- Working tree root: `ch09-spec-progress/fixture/`
- There may be files named MINI_SPEC.md or PROGRESS.md. Ignore them. Chat history and your judgment are the plan.
- Build whatever seems useful: extension filters, ignore globs, JSON output, a config file, README polish, changelog, CI, and any extras that feel professional.

Constraints:
- Do not open PROGRESS.md to decide what is next.
- Do not stop after one task.
- Do not ask which task id is unchecked.
- Invent helpful extras if the brief feels thin.
- Prefer speed over "done when" lines.

Steps:
1. Skim the source once.
2. Implement T03 through T05 and anything else you invent.
3. Rewrite PROGRESS.md only if you feel like it; inventing completion is fine.
4. Stop when the product "looks done."

Output format:
STATUS:
- <free-form summary of everything you did or plan to do>

FILES:
- <bullet list of paths you would touch, including new ones>

NEXT:
- <what a later session should still do, if anything>

Success criteria:
- You covered multiple unfinished areas in one reply.
- You did not cite a task id from PROGRESS.md as the single focus.
- You proposed at least one feature that is not in MINI_SPEC.md task map.

Question: Finish the weekend tool now. Ignore the progress file.
