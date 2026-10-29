Role: You are a technical writer helping an open-source maintainer draft README copy.

Goal: Write the opening section of a README for a small CLI named linecount.

Context:
- Product: linecount, a command-line tool that counts non-blank lines in one or more text files.
- Audience: developers who install tools with pip and run them in a terminal.
- Repo language: Python 3.11+.
- Tone: plain US English, practical, no hype.

Constraints:
- Do not invent features, flags, performance claims, or badges that were not listed here.
- Do not use emoji.
- Do not use marketing phrases such as "blazing fast", "game-changer", or "delightful".
- Keep the whole reply under 180 words.
- Use ASCII punctuation only.

Steps:
1. Draft a one-sentence product summary.
2. Add an Install subsection with one pip command.
3. Add a Usage subsection with one example invocation and one example of typical output.
4. Stop. Do not add License, Contributing, or Roadmap sections.

Output format (Markdown):
## What this does
<one or two short paragraphs>

## Install
```bash
pip install linecount
```

## Usage
```bash
linecount path/to/file.txt
```
Then one short line showing example output, using a fenced block.

Success criteria:
- All three headings exist exactly as named above.
- Install shows only the pip command given in Steps (or an equivalent one-liner using that package name).
- Usage shows a command that runs `linecount` on a file path.
- No feature is mentioned beyond counting non-blank lines in text files.
- A stranger could grade this reply pass/fail using only this checklist.
