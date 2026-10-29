# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 6. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-mega-2026-10-29.md` | `../before/mega-prompt.md` | Overloaded single ask; fails allowlist, hours ceiling, and raw-JSON-only consumer rules |
| `after-step1-plan-2026-10-29.md` | `../after/step1-plan.md` | Plan artifact only; handoff into step 2 |
| `after-step2-contract-2026-10-29.md` | `../after/step2-contract.md` | Contract artifact from frozen plan; handoff into step 3 |
| `after-step3-verify-2026-10-29.md` | `../after/step3-verify.md` | Checklist grade; VERDICT PASS |

The mega run is the failure case. The three-step chain is the success case with intermediate artifacts saved. Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Checkable allowlist:** inventing `src/globutil.py` is an obvious mega-prompt failure.
2. **Handoff artifacts:** each chain step emits a named block the next step can paste.
3. **Stop conditions:** plan/contract steps forbid code; verify forbids redesign.
4. **No fake scores:** Yao et al. 2022 is cited in the chapter as a pattern only.
