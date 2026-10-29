# Model output -- after (six-slide outline)

- Date: 2026-10-29
- Prompt: ../after/slide-outline.md
- Context: single-turn coding-agent session used while authoring the companion folder; agent given brand locks and the six-slide contract
- Note: Real reply to the slide-outline prompt. Exactly six slides, one job each, title + one sentence + visual note, no invented screenshot paths.

---

META:
- talk_id: TALK06
- slide_count: 6
- brand_ok: yes
- unknowns: none

SLIDES:
### S1 | Count TODOs Without Boiling the Ocean
- job: Open the talk
- one_sentence: A ten-minute look at todocount, a weekend CLI that counts TODO and FIXME markers without turning into a platform.
- visual_note: describe title, teal rule, and bracket mark on flat #121110; no photo

### S2 | The problem is noisy trees
- job: Name the pain
- one_sentence: Default walks across mixed folders report true totals that still send you hunting in the wrong files.
- visual_note: diagram of a small tree with src, scripts, and docs; no fake IDE screenshot

### S3 | One command, one job
- job: Show the tool
- one_sentence: Run `todocount --ext .py ./src` when you only want Python markers in the tree you will edit.
- visual_note: describe monospace command centered on dark field; ASSET_REQUIRED: terminal capture if you later want a real recording

### S4 | What stays out of scope
- job: Freeze scope
- one_sentence: No cloud sync, no dashboard, and no invented metrics -- the tool counts markers and stops.
- visual_note: describe a short reject list as plain text lines; no neon icons

### S5 | How you would demo it
- job: Walk the demo
- one_sentence: Clone a sample tree, run the default count, then rerun with --ext and compare the two numbers aloud.
- visual_note: diagram two-step flow (default -> filtered); ASSET_REQUIRED: real terminal clip only if recorded

### S6 | Takeaways and next step
- job: Close cleanly
- one_sentence: Keep the prompt or README honest: one job, one example command, and no fake UI in the slides.
- visual_note: describe three takeaway lines plus GitHub path placeholder as text; no QR invent if URL unknown -- write ASSET_REQUIRED: final URL
