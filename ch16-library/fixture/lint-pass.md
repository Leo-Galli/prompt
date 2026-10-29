# Complete template (lint must pass)

Fill every `{{variable}}` before paste.

Version tag: note-blurb@1.0.0

---

Role: Careful note writer.

Goal: Draft one short note about {{TOPIC}} for {{AUDIENCE}}.

Context:
- Topic: {{TOPIC}}
- Audience: {{AUDIENCE}}
- Trusted facts only:
<<<FACTS
{{FACTS}}
>>>

Constraints:
- ASCII only
- Do not invent facts outside FACTS
- Max {{MAX_WORDS}} words

Steps:
1. Read FACTS.
2. Write the note.
3. Stop after Output format.

Output format:
NOTE:
- topic: {{TOPIC}}
- body: <one paragraph, max {{MAX_WORDS}} words>

Success criteria:
- Output starts with NOTE:
- body uses only trusted facts
- body word count is at or under {{MAX_WORDS}}
- ASCII only

Question: Write the note for {{TOPIC}}. Stop when success criteria are met.
