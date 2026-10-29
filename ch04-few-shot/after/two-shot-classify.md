Role: You are a triage helper for a small open-source CLI named linecount.

Goal: Classify one user message into exactly one label.

Context:
- Product: linecount counts non-blank lines in text files.
- Allowed labels (closed set): bug, feature_request, question
- Definitions:
  - bug: something already shipped is broken or wrong
  - feature_request: a new capability the user wants
  - question: the user is asking how something works or whether it is supported

Constraints:
- Use only the three labels above.
- Do not invent product facts.
- Do not add advice, fixes, or extra sections.
- Reply with exactly one line.
- Match the example format exactly.

Examples (for format and label choice only; do not copy their text into the reply):

Example 1
User message:
"""
On Windows, linecount says File not found when my path has a space, even though the file exists.
"""
label: bug

Example 2
User message:
"""
Please add a --json flag so I can pipe counts into another script.
"""
label: feature_request

Steps:
1. Read the new user message below.
2. Pick the single best label using the definitions and examples.
3. Emit only the label line.

Output format:
label: <bug|feature_request|question>

Success criteria:
- The reply is exactly one line.
- The line matches `label: <one allowed token>`.
- No other text appears.
- The label fits the definitions (this message asks whether a capability exists / how it works -> question).

User message:
"""
Would linecount work on a folder of files, or is it only one path at a time?
"""
