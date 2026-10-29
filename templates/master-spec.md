# Master project spec template

Fill every `{{variable}}`. Keep this file as the source of truth for a multi-session agent project.
ASCII only. Do not invent facts outside the Allowed facts section.

Version: {{SPEC_VERSION}}

---

## Identity

- Working title: {{TITLE}}
- One-sentence promise: {{PROMISE}}
- Audience: {{AUDIENCE}}
- Primary delivery: {{DELIVERY}}

## Goal

Produce {{DELIVERABLE}} that a stranger can accept using the done-when lines in the progress file.

## Allowed facts

Only these facts may appear in generated prose or marketing copy:

{{ALLOWED_FACTS}}

Never invent employers, awards, metrics, quotes, or other projects.

## Constraints

- Language: US English, ASCII only in project markdown
- No emoji
- No AI attribution in commits or docs
- Secrets never staged
- Page / size / word budgets: {{BUDGETS}}
- Companion or code layout: {{LAYOUT_RULES}}

## Outline

{{OUTLINE}}

## Task policy

- One task id per session
- Progress file path: {{PROGRESS_PATH}}
- End marker rule: leave `THE END` absent while work remains; restore only when every acceptance check passes
- Spec sections to load for a task: only the sections named in that task prompt

## Output format

When an agent summarizes a completed task, emit exactly:

```text
TASK:
- id: <id>
- done_when: <line>

VERIFY:
- command: <command>
- result: <pass | fail | not run -- with reason>

PROGRESS_UPDATE:
- <checkbox / status / session-log line>
```

## Success criteria

- A stranger can grade each task from its done-when line without asking follow-ups
- No facts appear outside Allowed facts unless marked UNKNOWN
- Templates and prompts used by the project pass `python -m prompt_lint` on the files listed in {{LINT_PATHS}}
- Acceptance checks for the whole project are listed and must all pass before `THE END` is restored

## Acceptance checks

{{ACCEPTANCE_CHECKS}}
