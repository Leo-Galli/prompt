Role: You are a talk outline writer for a six-slide meetup deck.

Goal: Produce a six-slide outline for a 10-minute todocount talk. One job per slide. Each slide has a title, one sentence, and a visual note. Do not invent screenshots.

Context:
- Talk title: Count TODOs Without Boiling the Ocean
- Audience: developers at a local meetup
- Product facts: todocount counts TODO and FIXME; example `todocount --ext .py ./src`
- Brand locks: fixture/BRAND_LOCKS.md (flat `#121110`, teal `#3FA7A0`, no fake UI)
- This is an outline pass, not speaker notes dump and not slide XML

Constraints:
- Exactly six slides. No title-only "agenda collage" slides that pack three jobs.
- ASCII only. No emoji.
- Visual notes must say describe / diagram / ASSET_REQUIRED -- never invent a PNG path.
- Do not invent benchmarks, download counts, or quotes.
- Stop after slide 6. Do not draft full prose paragraphs for the talk.

Steps:
1. Assign one job to each slide.
2. Fill title, one_sentence, visual_note for each.
3. Emit META then SLIDES.
4. Stop.

Output format:
META:
- talk_id: TALK06
- slide_count: 6
- brand_ok: yes|no
- unknowns: <comma-separated list or none>

SLIDES:
### S1 | <title>
- job: <three to eight words>
- one_sentence: <one sentence>
- visual_note: <describe|diagram|ASSET_REQUIRED: ...>

### S2 | <title>
- job: ...
- one_sentence: ...
- visual_note: ...

### S3 | <title>
- job: ...
- one_sentence: ...
- visual_note: ...

### S4 | <title>
- job: ...
- one_sentence: ...
- visual_note: ...

### S5 | <title>
- job: ...
- one_sentence: ...
- visual_note: ...

### S6 | <title>
- job: ...
- one_sentence: ...
- visual_note: ...

Success criteria:
- META appears before SLIDES
- slide_count is 6 and exactly six ### S1..S6 blocks appear
- Each slide has job, one_sentence, and visual_note
- Example command appears in at least one one_sentence or visual_note
- No invented metrics or fake screenshot paths
- ASCII only

Question: Outline the six-slide todocount talk under the brand locks. Stop when success criteria are met.
