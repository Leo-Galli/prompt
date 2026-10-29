# Filled changelog template (for the after model run)

This file is the after template with variables filled for one reproducible run.
It is not a library template by itself -- prefer `../after/templated-changelog.md`.

---

Role: Careful release writer for a weekend CLI.

Goal: Write one changelog blurb for todocount version 0.3.0 using only the trusted change list.

Context:
- Product: todocount
- Version: 0.3.0
- Audience: maintainers pasting into GitHub Releases
- Trusted change list (only these facts are allowed):
<<<CHANGES
- Fix: nested directories were under-counted when a folder name started with a dot
- Fix: `--help` typo "recieve" -> "receive"
- Docs: README example now shows `todocount ./src`
>>>

Constraints:
- ASCII only. No emoji. No smart punctuation.
- Use only facts inside CHANGES. If a detail is missing, write UNKNOWN instead of guessing.
- Do not invent metrics, star counts, benchmarks, or user quotes.
- Max 60 words in the BODY paragraph.
- Stop after the CHANGELOG block.

Steps:
1. Read CHANGES.
2. Draft one BODY paragraph that covers every trusted change without padding.
3. Fill Output format exactly.
4. Stop.

Output format:
CHANGELOG:
- product: todocount
- version: 0.3.0
- body: <one paragraph, max 60 words>
- unknown: <NONE or comma-separated missing details>

Success criteria:
- Output starts with CHANGELOG:
- product and version match the filled variables exactly
- body uses only trusted changes (or UNKNOWN)
- body word count is at or under 60
- unknown is NONE when nothing is missing
- No invented metrics or extra sections
- ASCII only

Question: Write the changelog blurb for todocount 0.3.0. Stop when success criteria are met.
