# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 5. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-answer-only-2026-10-29.md` | `../before/answer-only.md` | Answer-only; correct `R+W`; no visible working |
| `after-visible-steps-2026-10-29.md` | `../after/visible-steps.md` | Numbered steps + same `FINAL_ANSWER: R+W`; clearer audit trail |

Both runs agree on the final set. The chapter compares clarity of the final answer path, not invented accuracy percentages. Re-run the prompts in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Checkable rules:** capacity, blockers, and tie-breakers are in the prompt -- no private product lore.
2. **Same final answer is likely:** the lesson is when visible steps help a reviewer, not a fake win-rate claim.
3. **Clear FINAL_ANSWER marker:** easy to grade in tests and in manual review.
