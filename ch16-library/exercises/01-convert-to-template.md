# Exercise 1 -- Convert a chat prompt into a template

## Done when

- You have a `.md` file under a personal or local `templates/` folder
- Every reusable slot is a `{{VARIABLE}}` (ASCII names)
- The file includes Goal, Output format, and Success criteria markers
- `python -m prompt_lint path/to/your-template.md` exits 0

## Steps

1. Paste a recent chat prompt you reused at least twice.
2. Replace one-off nouns (product name, version, paths) with `{{variables}}`.
3. Add missing Goal / Output format / Success criteria if absent.
4. Add a version tag line such as `Version tag: my-template@0.1.0`.
5. Run prompt-lint until it passes.

## Notes

Do not invent product facts inside the template defaults. Leave trusted lists as `{{CHANGES}}` or similar empty slots.
