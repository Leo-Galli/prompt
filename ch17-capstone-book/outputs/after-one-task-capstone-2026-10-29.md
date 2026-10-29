# Model output -- after (capstone one-task T04)

- Date: 2026-10-29
- Prompt: ../after/capstone-task-prompt.md
- Context: single-turn coding-agent session used while authoring the companion folder; fixture PROGRESS left with T04 unchecked on purpose
- Note: Real reply to the resume prompt. TASK.id is T04; T05 not started; THE END stays absent; facts limited to FACTS.md.

---

TASK:
- id: T04
- done_when: `chapter-stub.md` exists; H1 title only (no "Chapter N:"); cites only FACTS.md Spark/Signal lines; <= 400 words; ASCII

PLAN:
- Confirm Status.Next is T04 and T05 stays untouched.
- Draft `chapter-stub.md` with title-only H1; quote only allowlisted Spark/Signal lines from FACTS.md.
- State PROGRESS update; leave THE END absent because T05 remains open.

DIFF_NOTES:
- Create `chapter-stub.md` only.
- Proposed body (ASCII, under 400 words) would open with H1 `Why a tiny book kit uses a progress file`, then cite: Spark real PDF pages 800; Final-export spine 1.8016 in and cover 14.0516 x 9.25 in; Prepub-fixes note of 802 pages before later settle at 800; Signal KDP-margins-QR close at 374p with gutter 0.75 in and QR decode 28/28; earlier T23 interior 358p; export folders SPARK_KDP_FINAL and RADIO_KDP_FINAL; clear/restore THE END pattern on both trees.
- No edits to MINI_SPEC.md, FACTS.md, or ACCEPTANCE.md.
- No invented success rates or single-attempt cover claims.

PROGRESS_UPDATE:
- Check off T04 with a one-line note and date after the file exists and verify passes.
- Set Last completed: T04; Next: T05; Open issues: none.
- Session log: append T04 closed; T05 next.
- THE_END: leave absent -- T05 and acceptance remain open.

VERIFY:
- command: python -c "from pathlib import Path; p=Path('chapter-stub.md'); t=p.read_text(encoding='ascii'); assert not t.startswith('# Chapter'); assert len(t.split())<=400; print('ok', len(t.split()), 'words')"
- result: not run in this plan-only turn -- fixture left mid-project so readers can apply T04; expect pass after create

FACTS_USED:
- Spark Words line: 211706 / 220000 (real PDF pages: 800)
- Spark Final-export: pages 800; spine 1.8016 in; cover 14.0516 x 9.25 in; SPARK_KDP_FINAL
- Spark Prepub-fixes: pages 802; spine 1.8061 in (later settle at 800)
- Signal Status after MQ phase: 374p; gutter 0.75 in; QR 28/28; RADIO_KDP_FINAL
- Signal T23: 358p at 0.625 in gutter
- Signal T24: spine 0.80622 in at 358p cover wrap
- Both: THE END cleared when a phase opens and restored when that phase closes
