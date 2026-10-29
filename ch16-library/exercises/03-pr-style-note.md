# Exercise 3 -- PR-style note for a template change

## Done when

- You wrote a short pull-request style note (bullet list is fine)
- The note names the template path, old version tag, new version tag
- The note says whether prompt-lint passes
- The note says whether any consumer prompts need a fill-slot update
- Soft success language ("feels better") is absent

## Template for the note

```text
Template PR note
- path:
- change summary (one sentence):
- version: <old> -> <new>
- prompt-lint: <pass | fail -- paste issues>
- consumers to update:
- deprecation: <none | path of retired file>
- risk if merged without lint:
```

## Hint

Use a real edit: rename a variable, tighten Output format, or deprecate a soft success line. Run prompt-lint before you claim pass.
