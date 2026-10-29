# Exercise 2 -- Run prompt-lint

## Done when

- You captured a failing run on `fixture/lint-fail.md` (exit 1)
- You captured a passing run on `fixture/lint-pass.md` (exit 0)
- You can name which markers the fail file was missing

## Commands

From the companion repo root:

```bash
PYTHONPATH=. python -m prompt_lint ch16-library/fixture/lint-fail.md
PYTHONPATH=. python -m prompt_lint ch16-library/fixture/lint-pass.md
PYTHONPATH=. python -m prompt_lint templates/
```

On Windows PowerShell:

```powershell
$env:PYTHONPATH = "."
python -m prompt_lint ch16-library/fixture/lint-fail.md
python -m prompt_lint ch16-library/fixture/lint-pass.md
python -m prompt_lint templates/
```

## Record

| Target | Exit code | Issues |
| --- | --- | --- |
| lint-fail.md |  |  |
| lint-pass.md |  |  |
| templates/ |  |  |
