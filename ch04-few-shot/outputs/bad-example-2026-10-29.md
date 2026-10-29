# Model output -- after (deliberately bad examples)

- Date: 2026-10-29
- Prompt: ../after/bad-example-classify.md
- Context: single-turn coding-agent session used while authoring the companion folder
- Note: Real reply when the prompt's examples mislabel questions/requests as bugs and use a chatty multi-sentence style. The model followed the skewed examples: wrong label class and wrong shape versus the clean one-line contract in the good 2-shot prompt.

---

Answer: Folder support is unclear from the message, and that kind of gap usually shows up as broken expectations in the wild, so treat it as a bug until someone confirms single-path-only behavior. Suggested reply to user: we should clarify docs and maybe patch recursive folder handling. label=bug severity=medium
