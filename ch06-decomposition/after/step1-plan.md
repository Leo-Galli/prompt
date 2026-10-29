Role: You are a planning helper for a small open-source CLI named linecount.

Goal: Produce only a plan artifact for the `--ignore GLOB` feature. Do not write code.

Context:
- Product: linecount counts non-blank lines in text files from a path argument.
- Feature brief: add a repeatable flag `--ignore GLOB` that skips files whose paths match the glob. Matching is case-sensitive. Directories are never counted as files. If every file is ignored, print `0` and exit 0.
- Allowlisted paths you may name (and only these):
  - `src/linecount.py`
  - `tests/test_ignore.py`
  - `README.md`
- Capacity today: at most 3 hours for the whole feature across later steps.

Constraints:
- Emit the ARTIFACT_PLAN block only.
- Do not write source code, tests, README prose, commit messages, or Slack stories.
- Do not invent files outside the allowlist.
- Do not invent extra flags.
- `hours_estimate` must be an integer from 1 to 3 inclusive.
- `risks` must contain exactly two short bullets (one line each).
- Stop after the artifact. No closing advice.

Steps:
1. Choose which allowlisted files must change.
2. List what stays out of scope for this feature.
3. Name exactly two risks.
4. Estimate hours under the ceiling.
5. Emit ARTIFACT_PLAN in the output format.

Output format:
ARTIFACT_PLAN:
files:
- <path>
- <path>
out_of_scope:
- <item>
- <item>
risks:
- <one line>
- <one line>
hours_estimate: <1-3>

Success criteria:
- The reply starts with `ARTIFACT_PLAN:`.
- Every `files` entry is on the allowlist.
- Exactly two `risks` lines.
- `hours_estimate` is 1, 2, or 3.
- No code fences and no source code appear.
- No text after the `hours_estimate` line.

Question: Emit the plan artifact for `--ignore GLOB` under these rules.
