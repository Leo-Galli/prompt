# Model output -- after step 2 (contract artifact)

- Date: 2026-10-29
- Prompt: ../after/step2-contract.md
- Context: single-turn coding-agent session used while authoring the companion folder
- Note: Real reply. Uses the frozen step-1 plan embedded in the prompt. Contract-only; no implementation bodies. Feeds step 3.

---

ARTIFACT_CONTRACT:
flag: --ignore
argv_shape: linecount --ignore GLOB PATH
behavior_bullets:
- Skip files whose paths match any --ignore GLOB (case-sensitive)
- Never count directories as files
- If every file is ignored, print 0 and exit 0
test_names:
- test_ignore_skips_matching_file
- test_ignore_all_matched_prints_zero
