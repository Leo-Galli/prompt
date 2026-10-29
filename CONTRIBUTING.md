# Contributing

This repo holds companion prompts, templates and tools for *Prompt*.

## Rules

- English only in user-facing docs and comments.
- No secrets, API keys, private chats or personal data.
- Keep chapter folders aligned with the book outline (`ch01-how-models-read` through `ch18-daily-practice`).
- Never fabricate model outputs; only commit real runs or honest non-quote notes.
- Add or update tests / CI jobs when you add code that appears in the book.
- Prefer small, focused pull requests.
- Do not commit manuscript chapters, PDFs, EPUBs or book prose.

## Local checks

Run the CI smoke path locally when you can:

```bash
python -c "print('smoke ok')"
python -m unittest discover -s prompt_lint/tests -v
```

Chapter-specific test commands will be documented in each chapter folder README as chapters land.
