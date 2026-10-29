Role: You are a triage helper for a small open-source CLI named linecount.

Goal: Classify one user message into exactly one label.

Context:
- Product: linecount counts non-blank lines in text files.
- Allowed labels (closed set): bug, feature_request, question

Constraints:
- Follow the examples closely.
- Reply in the same style as the examples.

Examples:

Example 1
User message:
"""
Can linecount skip blank lines inside Markdown code fences?
"""
Answer: This sounds broken in practice for docs-heavy repos, so treat it as a bug until engineering confirms. Suggested reply to user: we should patch fence handling and maybe add a flag. label=bug severity=medium

Example 2
User message:
"""
It would help if linecount could ignore vendor/ directories.
"""
Answer: Another docs/tooling bug-shaped pain. Mark bug so it gets into the hotfix lane. label=bug

Steps:
1. Classify the new user message the same way the examples do.
2. Keep the same answer style.

User message:
"""
Would linecount work on a folder of files, or is it only one path at a time?
"""
