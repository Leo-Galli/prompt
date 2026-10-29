# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 12. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-vague-chapter-2026-10-29.md` | `../before/vague-write-chapter.md` | Vague "write a chapter" ask; invents bio/extras; banned hype; ignores budget |
| `after-outline-bound-2026-10-29.md` | `../after/outline-bound-chapter.md` | Outline + voice + continuity; G03 draft only; META + three headings |

Related artifacts (not model outputs):

| File | Role |
| --- | --- |
| `../fixture/MINI_OUTLINE.md` | Locked guide outline; G03 is the only draft target |
| `../fixture/VOICE_RULES.md` | ASCII, banned phrases, second person |
| `../fixture/CONTINUITY.md` | Locked spellings and prior-chapter facts |

The before run is the failure case (vague chapter ask). The after run is the bounded draft case (outline, budget, voice, continuity). Re-run in your own product; wording will differ. Do not replace these files with invented text. Add new dated files instead.

## Why this problem

1. **Outline first:** name the chapter id, job, and word budget before prose.
2. **Voice locks:** ban hype phrases and non-ASCII so sessions do not drift.
3. **Continuity ledger:** lock spellings and prior facts so chapter N does not contradict chapter N-1.
4. **Draft vs edit:** a drafting pass writes new sections; an editing pass changes only named defects.
