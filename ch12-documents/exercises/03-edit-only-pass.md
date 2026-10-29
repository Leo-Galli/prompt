# Exercise 03 -- Plan an edit-only pass

Goal: Write an edit-only prompt that repairs a draft without rewriting the whole chapter.

Scenario: G03 drafted successfully, but a reviewer found two defects:
1. One sentence uses the banned phrase "it's important to note".
2. The forward pointer accidentally includes three paragraphs of G04 test code.

Done when:
- Your prompt sets `pass_type: edit`.
- It quotes the two defects as untrusted excerpts inside delimiters.
- It forbids changing sections that already meet the outline.
- Success criteria reject new features, new headings, and a full rewrite.
- ASCII only.

Write your edit-only prompt below:

---

(paste your prompt here)
