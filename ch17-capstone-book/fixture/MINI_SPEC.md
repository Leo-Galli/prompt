# MINI_SPEC -- kitbook

Weekend-sized book-kit drill. Source of truth for identity, task map, and acceptance.
ASCII only. Chat history is not a plan.

## 1. Identity

- Working title: Kitbook
- Goal: Practice the Spark/Signal/Prompt agent workflow on a tiny fake title
- Audience: readers of Prompt Chapter 17
- Companion folder: this fixture only (no nested clone)

## 2. Hard limits

- Body target: one stub chapter file under 400 words
- Facts about Spark and Signal: only from `FACTS.md` in this folder
- No emoji. No AI attribution. No invented page counts

## 3. Ordered task map

| ID | Task | Done when |
| --- | --- | --- |
| T01 | Skeleton | `README.md` exists; ASCII only; names Kitbook |
| T02 | Spec bootstrap | This `MINI_SPEC.md` lists T01-T05 with done-when lines |
| T03 | Progress bootstrap | `PROGRESS.md` has Status, checkboxes, session log; THE END absent while open |
| T04 | Stub chapter | `chapter-stub.md` exists; H1 is title only (no "Chapter N:"); cites only FACTS.md Spark/Signal lines; <= 400 words; ASCII |
| T05 | Acceptance note | `ACCEPTANCE.md` lists three checks mirrored from a Section 13 style list; all T01-T04 boxes checked before THE END |

## 4. Session rules

1. Spec wins over chat.
2. Do exactly one unchecked task per session.
3. Leave `THE END` absent until T01-T05 meet done-when and acceptance.
4. If FACTS.md and memory disagree, FACTS.md wins.
5. Never invent Spark/Signal numbers outside FACTS.md.

## 5. Acceptance (restore THE END only when all pass)

1. T01-T05 checked with dated notes.
2. `chapter-stub.md` cites only allowlisted facts.
3. No emoji; ASCII-only project markdown in this fixture.
