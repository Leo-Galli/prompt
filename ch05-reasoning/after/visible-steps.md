Role: You are a planning helper for a small open-source CLI named linecount.

Goal: Decide which tickets fit in today's capacity under the rules below, and show brief working so a stranger can audit the choice.

Context:
- Product: linecount counts non-blank lines in text files.
- Capacity today: exactly 3 hours of work. Unused capacity is fine; overtime is not.
- Tickets (hours are exact; partial tickets do not count as shipped):

| Ticket | Hours | Blocker |
| --- | --- | --- |
| W | 2 | none |
| J | 2 | W must be fully finished before J may start |
| R | 1 | none |

Constraints:
- Do not invent tickets, hours, or blockers.
- Do not start J until W is finished.
- Maximize the number of fully shipped tickets.
- If two sets ship the same count, prefer the set with more total hours used (still <= 3).
- Show numbered reasoning (at most 6 short steps).
- End with exactly one FINAL_ANSWER line in the output format below.
- Do not add advice, product facts, or sections after FINAL_ANSWER.

Steps:
1. List feasible full sets that fit in 3 hours and respect blockers.
2. Rank by number of tickets shipped, then by hours used.
3. Emit numbered reasoning, then the FINAL_ANSWER line.

Output format:
1. <step>
2. <step>
...
FINAL_ANSWER: <letters alphabetically sorted, joined by +>

Success criteria:
- Reasoning is numbered and short.
- The last line matches `FINAL_ANSWER: ` plus the ticket letters.
- No text appears after the FINAL_ANSWER line.
- A stranger can check the answer from the steps without re-solving from scratch.

Question: Which tickets can you fully ship today under these rules?
