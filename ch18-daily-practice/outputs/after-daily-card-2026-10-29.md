prompt: ../after/filled-daily-card.md
date: 2026-10-29
session: coding-agent draft for Prompt Chapter 18
product_context_hint: todocount weekend CLI; FACTS block from filled card / fixture/FACTS.md
---
SEVERITY_NOTE:
- product: todocount
- issue: #12
- severity: medium
- body: Nested directories can be skipped when the user passed a relative path with .. Maintainers own triage. A patch is in progress on branch fix/nested-relpath. Until it lands, prefer paths without parent segments when counting TODO/FIXME markers. Document under README Contributing.

LINT:
- command: python -m prompt_lint ch18-daily-practice/after/filled-daily-card.md
- result: exit 0

SAVE:
- path: outputs/after-daily-card-2026-10-29.md
