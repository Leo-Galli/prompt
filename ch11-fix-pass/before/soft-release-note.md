Role: You are a helpful release-notes writer.

Goal: Write a short release note for a recent CLI change.

Context:
- Tool: todocount (counts TODO/FIXME markers in a tree).
- Change: we added an `--ext` flag so users can limit the scan by file suffix (example: `--ext .py`).
- Audience: developers who already use the tool.

Constraints:
- Keep it short and friendly.
- Make it sound polished and complete.

Steps:
1. Explain the change.
2. Mention anything else that would help users adopt it.
3. Stop when it feels done.

Output format: a nice release note (use whatever structure seems best).

Success criteria:
- A teammate could paste it somewhere.
- It feels ready to ship.

Question: Write the release note.
