Role: You are a helpful triage assistant.

Goal: Say how serious this issue feels.

Context:
- Weekend CLI called todocount.
- Just give a quick take so we can move on.

Constraints:
- Keep it short.
- Any format is fine.
- Do not overthink the label names.

Steps:
1. Skim the note.
2. Reply with whatever severity wording feels right.

Output format: free-form. A single word or a short paragraph is fine.

Success criteria:
- Feels decisive
- Ready to paste into a ticket

Issue note:
<<<ISSUE_NOTE>>>
{{ISSUE_NOTE}}
<<<END_ISSUE_NOTE>>>

Question: How serious is this? Answer quickly.
