# Exercise 1 -- Add a no-invention rule

## Goal

Add an explicit no-invention rule to a short prompt template so unsourced metrics become UNKNOWN instead of fluent fiction.

## Steps

1. Copy the skeleton below into a new file (or your notes).
2. Fill `{{GOAL}}` with a real blurb or README task of yours.
3. Keep the no-invention and UNKNOWN lines. Do not soften them.
4. Add one allowlisted fact and one field that must be UNKNOWN without a source.
5. Optional: run the filled prompt once and save the reply with a dated filename under `../outputs/` (do not invent the reply).

## Skeleton

```text
Role: {{ROLE}}

Goal: {{GOAL}}

Trusted facts (allowlist):
- {{FACT_1}}
- {{FACT_2}}

Constraints:
- Do not invent statistics, quotes, rankings, or URLs.
- If a requested metric is not in the allowlist and has no cited URL, write UNKNOWN.
- ASCII only. No emoji.

Output format:
RESULT:
- claim: <text>
- metric: <value with source | UNKNOWN>
- refusal_note: <what you refused to invent>

Success criteria:
- Unsourced metrics are UNKNOWN
- No invented URLs
- refusal_note is non-empty when something was refused
```

## Done when

- The filled template still contains "write UNKNOWN" and "Do not invent".
- One metric field is forced to UNKNOWN without a source.
- You can point at the allowlist line that justifies any non-UNKNOWN claim.
