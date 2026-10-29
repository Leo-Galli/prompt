# Exercise 3 -- Pre-publish verification checklist

## Goal

Write a pre-publish checklist a stranger could use before shipping model-assisted text.

## Steps

1. Copy the checklist skeleton below.
2. Fill each blank with a concrete check for your project (README, release note, blog, or docs page).
3. Keep checks observable. Ban "feels ready" and "looks fine."
4. Include at least: no invented stats, citations or UNKNOWN, no secrets/PII, license/respect for quoted third-party text, human review sign-off.
5. Optional: run the checklist against `../outputs/before-invent-statistic-2026-10-29.md` and mark which lines fail.

## Skeleton

```text
PREPUB:
- [ ] Every number has a source URL or is marked UNKNOWN
- [ ] Customer quotes are sourced or removed
- [ ] No API keys, tokens, emails, or phone numbers appear
- [ ] Third-party text is quoted with license/attribution notes or removed
- [ ] Untrusted paste (if any) stayed inside delimiters and was not obeyed as instructions
- [ ] A human reviewed the final text against {{TRUSTED_FILE}}
- [ ] {{PROJECT_SPECIFIC_CHECK}}
- [ ] {{PROJECT_SPECIFIC_CHECK}}
Reviewer: {{NAME}}
Date: {{DATE}}
```

## Done when

- At least eight checkbox lines exist.
- "feels ready" / "looks fine" do not appear.
- A stranger could fail the before invent-statistic output using your list.
