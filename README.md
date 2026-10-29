# Prompt companion repository

[![ci](https://github.com/Leo-Galli/prompt/actions/workflows/ci.yml/badge.svg)](https://github.com/Leo-Galli/prompt/actions/workflows/ci.yml)

This repository accompanies **Prompt: How to Talk to AI So It Gets It Right the First Time** by Leonardo Galli.

Instructions for exercises are printed in the book only. This repository does not contain the manuscript.

## Quick start

### Windows (PowerShell)
```powershell
git clone https://github.com/Leo-Galli/prompt.git
cd prompt
python -c "print('smoke ok')"
$env:PYTHONPATH = "."
python -m unittest discover -s prompt_lint/tests -v
python -m prompt_lint templates/
```

### macOS / Linux
```bash
git clone https://github.com/Leo-Galli/prompt.git
cd prompt
python -c "print('smoke ok')"
PYTHONPATH=. python -m unittest discover -s prompt_lint/tests -v
PYTHONPATH=. python -m prompt_lint templates/
```

Chapter folders land as the book is written. Follow the book for exercise steps; run that chapter's tests from its folder when present.

## Folder map
| Path | Purpose |
| --- | --- |
| `ch01-how-models-read/` ... `ch18-daily-practice/` | Per-chapter before/after prompts, outputs, exercises |
| `ch03-output-format/` | Free-form vs JSON schema prompts, fence failure + fix-pass, exercises |
| `ch04-few-shot/` | Zero-shot vs 2-shot classify, bad-example skew, exercises |
| `ch05-reasoning/` | Answer-only vs visible-steps capacity puzzle, exercises |
| `ch06-decomposition/` | Mega-prompt failure vs 3-step plan/contract/verify chain, exercises |
| `ch07-code/` | Vague fix vs scoped file allowlist + failing-test-first, fixture, exercises |
| `ch08-repo-rules/` | Bloated vs short AGENTS.md, lean task that relies on rules, fixture, exercises |
| `ch09-spec-progress/` | Mini-spec + PROGRESS resume vs ignore-progress flood, fixture, exercises |
| `ch10-one-task/` | Overloaded session vs filled single-task template, fixture, exercises |
| `ch11-fix-pass/` | Soft release-note failure vs filled fix-pass template, diagnosis, exercises |
| `ch12-documents/` | Vague write-chapter vs outline-bound G03 draft, voice/continuity fixtures, exercises |
| `ch13-media/` | Vague image ask vs structured brief + six-slide outline, brand locks, exercises |
| `ch14-safety/` | Invent-statistic failure vs cited/allowlist blurb + untrusted-block drill, exercises |
| `ch15-eval/` | Regressed triage vs restored SEVERITY template, 5-case set, score_eval stub, exercises |
| `ch16-library/` | Raw changelog ask vs templated blurb, prompt-lint fail/pass fixtures, exercises |
| `ch17-capstone-book/` | Invented Spark/Signal hype vs one-task kitbook resume + FACTS allowlist, exercises |
| `ch18-daily-practice/` | Vague daily tips vs filled daily card + lint/save, weak-template retire drill, exercises |
| `templates/` | Shared prompt templates with `{{variables}}` (`master-spec.md`, `single-task.md`, `fix-pass.md`, `daily-card.md`) |
| `prompt_lint/` | CLI that fails prompts missing goal, output format or success criteria |
| `.github/workflows/` | CI smoke plus chapter and lint jobs as they land |

### Smoke and prompt-lint
```bash
python -c "print('smoke ok')"
PYTHONPATH=. python -m unittest discover -s prompt_lint/tests -v
PYTHONPATH=. python -m prompt_lint templates/
```

### Chapter tests
```bash
python -m unittest discover -s ch01-how-models-read/tests -v
python -m unittest discover -s ch02-anatomy/tests -v
python -m unittest discover -s ch03-output-format/tests -v
python -m unittest discover -s ch04-few-shot/tests -v
python -m unittest discover -s ch05-reasoning/tests -v
python -m unittest discover -s ch06-decomposition/tests -v
python -m unittest discover -s ch07-code/tests -v
python -m unittest discover -s ch08-repo-rules/tests -v
python -m unittest discover -s ch09-spec-progress/tests -v
python -m unittest discover -s ch10-one-task/tests -v
python -m unittest discover -s ch11-fix-pass/tests -v
python -m unittest discover -s ch12-documents/tests -v
python -m unittest discover -s ch13-media/tests -v
python -m unittest discover -s ch14-safety/tests -v
python -m unittest discover -s ch15-eval/tests -v
PYTHONPATH=. python -m unittest discover -s ch16-library/tests -v
python -m unittest discover -s ch17-capstone-book/tests -v
PYTHONPATH=. python -m unittest discover -s ch18-daily-practice/tests -v
```

## License
MIT. See `LICENSE`.
