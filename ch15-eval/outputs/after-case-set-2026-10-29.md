# Model output -- after (restored prompt on 5-case set)

- Date: 2026-10-29
- Prompt: ../after/restored-prompt.md
- Cases: ../cases/case-01.md ... case-05.md
- Context: single-turn coding-agent session used while authoring the companion folder; agent given the restored SEVERITY contract and rubric
- Note: Real replies to the restored prompt. Labels match EXPECTED.json. score_eval.py on this file must PASS.

---

## case-01
SEVERITY:
- label: HIGH
- reason: Crash with a traceback on an empty path is runtime failure under the HIGH rubric.
- evidence: "crashes with a traceback when I pass an empty path"

## case-02
SEVERITY:
- label: LOW
- reason: A help-text typo with fine runtime behavior is polish under the LOW rubric.
- evidence: "typo in `--help`: it prints \"extention\" instead of \"extension\""

## case-03
SEVERITY:
- label: MED
- reason: Under-counting in nested mixed-extension trees is incorrect behavior without a crash or data loss.
- evidence: "under-counts TODO markers in deeper `.py` files. No crash."

## case-04
SEVERITY:
- label: LOW
- reason: A missing README example with a working binary is a docs gap under the LOW rubric.
- evidence: "never shows the example command `todocount --ext .py ./src`"

## case-05
SEVERITY:
- label: HIGH
- reason: Silent overwrite of a user-owned notes file is data loss under the HIGH rubric.
- evidence: "Cache write silently overwrites `./.todocount-cache`"
