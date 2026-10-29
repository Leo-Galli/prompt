# Model output -- before (free-form bug summary)

- Date: 2026-10-29
- Prompt: ../before/freeform-bug-summary.md
- Context: single-turn coding-agent session used while authoring the companion folder
- Note: This is a real reply to the free-form prompt. It is readable prose, not machine-parseable. Useful for humans; weak as an API contract.

---

## LINE-218 -- Windows paths with spaces break linecount

**What happens**
On Windows PowerShell, if someone runs linecount with an unquoted path that contains spaces (example: `C:\Users\Ada Lopez\notes.txt`), the CLI reports `File not found` and exits with code 1 even when that file is present. The same path works on macOS/Linux when it is quoted correctly.

**Why it might be happening**
Reporter suspects argv splitting -- the path may be getting broken into multiple arguments at the space, so the tool looks for a file that is only the first fragment.

**Impact / priority**
Feels high: Windows users can hit this on day one if their home or project paths include spaces (common with display names in `C:\Users\...`).

**Ask for the team**
Confirm whether we split/join argv ourselves versus relying on the shell, and add a regression case for spaced paths on Windows. Ticket: LINE-218.
