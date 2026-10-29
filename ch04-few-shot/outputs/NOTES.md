# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 4. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-zero-shot-2026-10-29.md` | `../before/zero-shot-classify.md` | Zero-shot; correct `question` label; one-line format |
| `after-two-shot-2026-10-29.md` | `../after/two-shot-classify.md` | 2-shot with diverse good examples; same correct label and format |
| `bad-example-2026-10-29.md` | `../after/bad-example-classify.md` | Bad examples teach "everything is a bug" + chatty answers; reply skews label and shape |

Re-run the prompts in your own product; results will differ. Do not replace these files with invented text. Add new dated files instead.

## What the bad examples taught (on purpose)

1. **Label leakage / wrong distribution:** both examples mark non-bugs as `bug`, so the model over-uses `bug`.
2. **Format drift:** examples use multi-sentence "Answer:" prose instead of `label: <token>`, so the reply abandons the one-line contract.
3. **Stale triage policy:** "hotfix lane" language is not in the product definitions; the model copies it anyway.
