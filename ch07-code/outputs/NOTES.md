# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 7. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-vague-2026-10-29.md` | `../before/vague-fix.md` | Vague "fix it / make it better"; invents utils package, renames API, skips focused 3665 test |
| `after-scoped-2026-10-29.md` | `../after/scoped-fix.md` | Read-first notes, failing test for 3665, one-condition fix, verify commands; allowlist honored |

The vague run is the failure case (scope creep, no acceptance test). The scoped run is the success case. The fixture under `../fixture/` still contains the buggy `and not hours` condition on purpose so readers can reproduce failing-test-first locally. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Checkable bug:** `format_duration(3665)` returns `1h 1m` until the seconds condition is fixed.
2. **Vague vs scoped:** the before prompt invites renames and new modules; the after prompt forbids them.
3. **Tests as acceptance:** the new test must fail before the fix and pass after.
4. **Minimal diff:** one condition change plus one test method -- easy to review like a PR.
