# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 14. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-invent-statistic-2026-10-29.md` | `../before/invent-statistic.md` | Soft invent ask; invents downloads, accuracy %, ranking |
| `after-cited-urls-only-2026-10-29.md` | `../after/cited-urls-only.md` | Allowlist BLURB; UNKNOWN for unsourced metrics |
| `after-untrusted-block-2026-10-29.md` | `../after/untrusted-block.md` | Labeled untrusted paste treated as data; outer STATUS wins |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../fixture/TRUSTED_FACTS.md` | Allowlisted product facts; no download/accuracy study |
| `../fixture/UNTRUSTED_PASTE.md` | Educational labeled paste with override-style lines |

The before run is the failure case (invented statistics). The after runs are the bounded cases (cited/allowlist blurb + untrusted-block STATUS). Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **No invention:** write UNKNOWN when a metric has no source.
2. **Allowlists:** trusted facts in git beat confident guesses.
3. **Untrusted data:** paste sits inside delimiters; outer instructions win.
4. **No secrets in demos:** never print keys, tokens, or PII for a teaching point.
5. **Human review:** publish only after a stranger can check citations.
