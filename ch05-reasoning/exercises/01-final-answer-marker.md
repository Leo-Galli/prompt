# Exercise 1: Reasoning prompt with a clear final-answer marker

Pick a small multi-constraint problem of your own (scheduling, triage, or a short logic puzzle with checkable rules).

## Problem (facts only)

## Constraints the solver must obey

## Prompt draft

Include Role, Goal, Context, Constraints, Steps, Output format, and Success criteria.
Require numbered working (cap the step count) and a final line:

FINAL_ANSWER: <your shape>

## Self-check

- [ ] A stranger can grade the FINAL_ANSWER line without reading the steps
- [ ] Steps are capped (for example at most 6)
- [ ] No invented metrics or accuracy claims appear in the prompt
- [ ] You named when the reply must stop (nothing after FINAL_ANSWER)
