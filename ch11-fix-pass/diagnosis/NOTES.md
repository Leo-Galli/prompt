# Diagnosis -- soft release note failure

Date: 2026-10-29
Failed output: `../outputs/before-soft-release-2026-10-29.md`
Prompt: `../before/soft-release-note.md`
Trusted facts: `../fixture/CHANGE_FACTS.md`

## Failure classes (primary)

1. **Hallucinated fact** -- invents version `2.4.0`, `--json`, `--ignore`, Windows/macOS installers, cloud sync, Discord, a speed claim, and a user quote. None of these appear in trusted facts.
2. **Wrong format** -- marketing landing page with `#` title and Upgrade now CTA instead of the required RELEASE_NOTE sections used in the fix-pass contract.
3. **Scope creep** -- soft "mention anything else that would help" invited extras beyond the `--ext` change.
4. **Missing constraint** (contributing) -- soft prompt never banned invention, never locked headings, never required ASCII-only voice.

## What was already usable

- Mentions `--ext` and file-suffix filtering (keep that intent).
- Mentions example suffixes including `.py` (allowed as illustration of `--ext`).

## Surgical fix (one pass)

Do not restart the whole project and do not change the model yet.
Keep the original goal (short release note for `--ext`).
Add only:
- quote the failed reply as untrusted data
- name the failure classes above
- lock headings to RELEASE_NOTE / SUMMARY / CHANGE / EXAMPLE / OUT_OF_SCOPE
- allow only facts from `CHANGE_FACTS.md`
- ban invented versions and marketing CTAs
- require UNKNOWN rather than guesses for missing facts

## Reset vs continue

Continue with a fix-pass in a fresh paste (quoted failure included).
Reset the thread only if a later reply still invents after two surgical passes, or if the task itself was wrong.
Do not swap models for this failure: the soft prompt is the defect.

## Fix-pass artifact

Filled from `../../templates/fix-pass.md` -> `../after/fix-pass-filled.md`.
