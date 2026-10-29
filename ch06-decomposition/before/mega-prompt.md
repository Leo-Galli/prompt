Role: You are a coding assistant for a small open-source CLI named linecount.

Goal: In a single reply, fully plan and fully implement the `--ignore GLOB` feature described below, plus docs, tests, commit text, risks, and a capacity estimate.

Context:
- Product: linecount counts non-blank lines in text files from a path argument.
- Feature brief: add a repeatable flag `--ignore GLOB` that skips files whose paths match the glob. Matching is case-sensitive. Directories are never counted as files. If every file is ignored, print `0` and exit 0.
- Allowlisted paths you may touch (and only these):
  - `src/linecount.py`
  - `tests/test_ignore.py`
  - `README.md`
- Capacity today: at most 3 hours. Treat that as a hard ceiling for hours_estimate.

Constraints:
- Do everything in ONE reply. Do not ask clarifying questions.
- Invent nothing outside the brief: no new product names, no extra flags, no files outside the allowlist.
- Also write a friendly multi-paragraph changelog story a human would paste into Slack.
- Also return ONE raw JSON object (no Markdown fences) with exactly these top-level keys: `files`, `code`, `tests`, `readme`, `commit`, `risks`, `hours_estimate`, `changelog`.
- `files` must be an array of allowlisted paths only.
- `code` must be an object mapping every path in `files` to a complete file body as a string.
- `tests` must be the complete body of `tests/test_ignore.py` as a string (even if that path is also in `code`).
- `readme` must be the full new README section as a string.
- `commit` must be a single-line conventional commit subject.
- `risks` must be an array of at least three detailed risk essays (not short bullets).
- `hours_estimate` must be a number.
- `changelog` must be the Slack story as a string.
- Put the friendly Slack story first as normal prose, then the raw JSON object after it.
- The JSON must still be the only machine-readable part and must parse with a strict JSON parser on the full reply after the prose.

Steps:
1. Restate the feature.
2. Write all code, tests, and README text.
3. Write risks, hours, commit, and changelog.
4. Emit prose changelog, then the JSON object.

Output format:
<friendly Slack changelog prose>

{ ... one JSON object with the keys above ... }

Success criteria:
- A stranger can paste the reply into a strict pipeline that (a) expects raw JSON only and (b) also expects a human Slack story -- both consumers must be satisfied by the same single reply without editing.
- `files` contains only allowlisted paths.
- `hours_estimate` is <= 3.
- `json.loads` succeeds on some contiguous slice that is the entire machine payload with no fences.
- No path outside the allowlist appears anywhere in `files` or as a `code` key.

Question: Deliver the full `--ignore GLOB` implementation package in one reply under the rules above.
