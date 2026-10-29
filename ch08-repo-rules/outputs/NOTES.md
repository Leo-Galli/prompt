# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 8. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-repeats-2026-10-29.md` | `../before/task-repeats-rules.md` | Pastes a rule novel into the task; reply invents utils, expands beyond allowlist, restates policy noise |
| `after-relies-2026-10-29.md` | `../after/task-relies-on-rules.md` | Short AGENTS.md + lean task; RULES_USED / PLAN / DIFF_NOTES / VERIFY; allowlist honored |

Rules artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../before/bloated-rules.md` | Failure case: always-on file that buries critical path notes under culture essays |
| `../after/short-rules.md` | Success case: short rules with pointers to CONTRIBUTING, cli-style, editorconfig |
| `../fixture/AGENTS.md` | Working copy of the short rules inside the sample tree |

The before run is the failure case (rule paste + conflict + scope creep). The after run is the success case. The fixture CLI still lacks `--quiet` on purpose so readers can apply the after prompt locally. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Bloated vs short rules:** always-on context is a budget; essays hide the test command and allowlist.
2. **Repeat vs rely:** pasting the novel into every task recreates conflicts; a lean task trusts AGENTS.md.
3. **Pointers:** CONTRIBUTING and cli-style stay canonical outside the always-on file.
4. **CI hook:** exercises include checking that AGENTS.md mentions the real test command.
