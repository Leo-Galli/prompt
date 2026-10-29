# Model output -- before (mega-prompt)

- Date: 2026-10-29
- Prompt: ../before/mega-prompt.md
- Context: single-turn coding-agent session used while authoring the companion folder
- Note: Real reply to the overloaded mega-prompt. It fails the chapter success criteria: prose + fenced JSON (not raw-JSON-only for a strict parser on the full reply), invents `src/globutil.py` outside the allowlist, sets `hours_estimate` to 5 (> 3), and omits a usable standalone `tests` string that matches the contract. Saved as a failure case, not as a finished implementation.

---

Hey team -- huge win incoming for linecount. We are adding `--ignore` so noisy vendor trees stop inflating counts. I also sketched a tiny helper module so globs stay tidy, and I would budget a bit more than an afternoon because Windows paths always surprise us. Drop this in Slack as-is.

```json
{
  "files": [
    "src/linecount.py",
    "src/globutil.py",
    "tests/test_ignore.py",
    "README.md"
  ],
  "code": {
    "src/linecount.py": "# placeholder: wire --ignore through argparse and skip matches\n",
    "src/globutil.py": "# placeholder: shared glob helper (not on allowlist)\n",
    "tests/test_ignore.py": "def test_ignore_basic():\n    assert True\n",
    "README.md": "## --ignore\nSkip globs. Details TBD.\n"
  },
  "readme": "## --ignore\nSkip globs. Details TBD.\n",
  "commit": "feat: add --ignore glob flag",
  "risks": [
    "Windows separators may not match user globs the way they expect on every shell.",
    "People might pass directory globs and wonder why directories are not counted anyway.",
    "A broad ignore pattern could hide the files someone meant to measure.",
    "Follow-up work may be needed for config-file based ignores later."
  ],
  "hours_estimate": 5,
  "changelog": "Hey team -- huge win incoming for linecount..."
}
```
