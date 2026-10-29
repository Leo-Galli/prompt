# Daily practice card

Version tag: daily-card@0.1.0

Fill every field. Run lint. Run once. Save the reply. One job only.

---

DAILY_CARD
date: {{DATE}}
tool: {{TOOL}}
job: {{JOB_ONE_SENTENCE}}

Role: {{ROLE}}

Goal: {{GOAL}}

Context:
- Trusted facts / files only (paste below or point at paths):
{{FACTS_OR_PATHS}}
- Do not invent metrics, quotes, or product claims missing from trusted context.

Constraints:
{{CONSTRAINTS}}

Steps:
1. Confirm Goal, Output format, and Success criteria are filled.
2. Run: `python -m prompt_lint` on this filled card (or the path you keep it in).
3. Run the ask once with the chosen tool (chat or agent).
4. Save the raw reply to {{SAVE_PATH}}.
5. Stop. Do not start a second job on this card.

Output format:
{{OUTPUT_FORMAT}}

Success criteria:
{{SUCCESS_CRITERIA}}

LINT_COMMAND: python -m prompt_lint {{CARD_PATH}}
SAVE_PATH: {{SAVE_PATH}}

Question: {{QUESTION}}
