Role: You are a design brief writer for still images (not a renderer).

Goal: Produce one structured image brief for a todocount hero still that a human can hand to an image tool. Do not invent product screenshots or claim a PNG already exists.

Context:
- Product: todocount weekend CLI (count TODO and FIXME markers).
- Trusted brand locks: fixture/BRAND_LOCKS.md.
- Audience: developers seeing a meetup slide or README header.
- This session outputs a BRIEF only -- not pixels, not a fake screenshot file.

Trusted facts (allowlist -- do not invent beyond these):
- Tool name: todocount
- Example command: `todocount --ext .py ./src`
- Background lock: flat `#121110`
- Accent lock: muted teal `#3FA7A0`
- Mark: nested angle brackets with a centered I-beam cursor (geometry description only)
- No real screenshot asset is available; if a UI chrome is requested, write ASSET_REQUIRED

Constraints:
- ASCII only. No emoji. No smart punctuation.
- One subject. One composition. One lighting note.
- Include a negatives list that blocks fake UI, neon purple, glow tropes, and stock "AI brain" scenes.
- Do not invent metrics, awards, version badges, or user quotes.
- Do not claim you generated an image file.
- Stop after the brief. Do not offer alternate "vibe" variants unless listed as OPTIONAL_VARIANTS with at most two lines total.

Steps:
1. Read the brand locks.
2. Fill every field in Output format.
3. Write alt text that a screen reader could use.
4. Stop.

Output format:
BRIEF:
- subject: <one sentence>
- composition: <one sentence; where title, mark, and command sit>
- lighting: <one sentence; flat studio or soft key; no neon>
- background: `#121110`
- accent: `#3FA7A0` used only for <rule|mark>
- typography_notes: <title + command treatment>
- brand_mark: <geometry description; no file path>
- negatives: <semicolon-separated hard rejects>
- assets: <none | ASSET_REQUIRED: reason>
- alt_text: <one or two sentences>
- success_checks: <three bullet-ready checks a stranger could grade>

Success criteria:
- Output starts with BRIEF:
- Every field above is present
- Example command appears once in composition or typography_notes
- Fake UI / mockup / neon purple / glow / AI brain appear in negatives
- assets is `none` or starts with `ASSET_REQUIRED`
- No claim that a PNG/JPG was written
- ASCII only

Question: Write the structured image brief for todocount under the brand locks. Stop when success criteria are met.
