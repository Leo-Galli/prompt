# Changelog blurb template

Fill every `{{variable}}` before paste. ASCII only. Do not invent product facts.

Version tag for this template file: changelog-blurb@1.0.0

---

Role: Careful release writer for a weekend CLI.

Goal: Write one changelog blurb for {{PRODUCT}} version {{VERSION}} using only the trusted change list.

Context:
- Product: {{PRODUCT}}
- Version: {{VERSION}}
- Audience: maintainers pasting into GitHub Releases
- Trusted change list (only these facts are allowed):
<<<CHANGES
{{CHANGES}}
>>>

Constraints:
- ASCII only. No emoji. No smart punctuation.
- Use only facts inside CHANGES. If a detail is missing, write UNKNOWN instead of guessing.
- Do not invent metrics, star counts, benchmarks, or user quotes.
- Max {{MAX_WORDS}} words in the BODY paragraph.
- Stop after the CHANGELOG block.

Steps:
1. Read CHANGES.
2. Draft one BODY paragraph that covers every trusted change without padding.
3. Fill Output format exactly.
4. Stop.

Output format:
CHANGELOG:
- product: {{PRODUCT}}
- version: {{VERSION}}
- body: <one paragraph, max {{MAX_WORDS}} words>
- unknown: <NONE or comma-separated missing details>

Success criteria:
- Output starts with CHANGELOG:
- product and version match the filled variables exactly
- body uses only trusted changes (or UNKNOWN)
- body word count is at or under {{MAX_WORDS}}
- unknown is NONE when nothing is missing
- No invented metrics or extra sections
- ASCII only

Question: Write the changelog blurb for {{PRODUCT}} {{VERSION}}. Stop when success criteria are met.
