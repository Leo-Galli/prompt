Role: You are a planning helper for a small open-source CLI named linecount.

Goal: Decide which tickets fit in today's capacity under the rules below.

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
- Reply with exactly one line in the output format below.
- Do not show working, steps, or explanations.

Steps:
1. Read the table and rules.
2. Choose the winning ticket set.
3. Stop.

Output format:
FINAL_ANSWER: <letters alphabetically sorted, joined by +>

Success criteria:
- The reply is exactly one line.
- The line matches `FINAL_ANSWER: ` plus the ticket letters.
- No other text appears.

Question: Which tickets can you fully ship today under these rules?
