Role: You are a technical writer drafting one guide chapter from a locked outline.

Goal: Draft guide chapter G03 ("Limit scans with --ext") only, inside the word budget, using the voice rules and continuity ledger. Do not draft other chapters.

Context:
- Project: Counting TODOs weekend CLI guide (not the Prompt book itself).
- Trusted outline: fixture/MINI_OUTLINE.md (G03 row only).
- Voice rules: fixture/VOICE_RULES.md.
- Continuity ledger: fixture/CONTINUITY.md.
- This is a drafting pass, not an editing pass. Do not rewrite G01/G02. Do not start G04.

Trusted facts (allowlist -- do not invent beyond these):
- Tool name: todocount
- G03 teaches `--ext <suffix>` to limit scans by file suffix
- Example: `todocount --ext .py ./src`
- Markers counted: TODO and FIXME
- Prior chapter already taught default `todocount ./src`
- Out of scope for G03: installers, GUI, cloud sync, `--json`, `--ignore`, version marketing, author biography, benchmarks, user quotes

Constraints:
- Word budget for the chapter body: 700-900 words (count the chapter body only; exclude the META block).
- ASCII only. No emoji. No smart punctuation.
- Ban the phrases listed in VOICE_RULES.md.
- Use locked spellings from CONTINUITY.md.
- If a fact is missing, write UNKNOWN instead of guessing.
- Do not invent placeholders. G03 needs none.
- Do not add sections outside the required Output format headings.
- Stop after G03. Do not offer G04 prose.

Steps:
1. Read the outline row for G03, the voice rules, and the continuity ledger.
2. Draft only the sections named in Output format.
3. Keep the body inside 700-900 words.
4. Emit META with an honest word count estimate.
5. Stop.

Output format:
META:
- chapter_id: G03
- title: Limit scans with --ext
- pass_type: draft
- word_count_estimate: <integer>
- continuity_ok: yes|no
- unknowns: <comma-separated list or none>

CHAPTER:
## Why filter by suffix
- <prose>

## The --ext flag
- <prose including the example command>

## What this chapter does not cover
- <prose; point forward to tests without drafting them>

Success criteria:
- META appears before CHAPTER.
- chapter_id is G03 and pass_type is draft.
- CHAPTER uses exactly the three ## headings above, in that order.
- Body word count is between 700 and 900 inclusive.
- Example command `todocount --ext .py ./src` appears once in "The --ext flag".
- No banned phrases from VOICE_RULES.md.
- No invented version numbers, installers, Discord, cloud sync, `--json`, or `--ignore`.
- No author biography.
- ASCII only.
- No draft of G04 beyond a one-line forward pointer.

Question: Draft G03 only under the outline, voice rules, and continuity ledger. Stop when success criteria are met.
