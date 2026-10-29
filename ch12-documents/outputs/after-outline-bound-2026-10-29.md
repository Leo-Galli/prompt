# Model output -- after (outline-bound chapter draft)

- Date: 2026-10-29
- Prompt: ../after/outline-bound-chapter.md
- Context: single-turn coding-agent session used while authoring the companion folder; agent given outline, voice rules, continuity ledger, and G03-only contract
- Note: Real reply to the outline-bound prompt. Stays on G03, keeps ASCII voice, uses the required headings, includes the example command, and reports a body word count inside 700-900.

---

META:
- chapter_id: G03
- title: Limit scans with --ext
- pass_type: draft
- word_count_estimate: 762
- continuity_ok: yes
- unknowns: none

CHAPTER:
## Why filter by suffix

By the end of the previous chapter you could run `todocount ./src` and get a count of `TODO` and `FIXME` markers across a tree. That default walk is honest and useful. It is also noisy the moment your folder mixes languages, generated files, and vendored trees you do not intend to edit this weekend.

A suffix filter exists for one reason: you want the count for the files you will actually open. If you are cleaning Python modules before a release, a count that also includes Markdown notes and shell stubs will send you hunting in the wrong places. Filtering is not a product strategy. It is a way to keep the number tied to the work in front of you.

Think about a small monorepo layout. You have `./src` with `.py` files, a `./scripts` folder with `.sh` helpers, and a `./docs` tree with `.md` pages that mention TODO in examples. A default scan reports every marker. That total is true and still the wrong number for a Python cleanup pass. You need a lever that says "only these suffixes" without inventing a config file or a plugin system.

This chapter teaches that lever and only that lever. You will learn what `--ext` means, how to pass it, and what stays out of scope until later chapters. You will not get a tour of every possible future flag. The weekend guide stays small on purpose.

## The --ext flag

The `--ext` flag limits the walk to files whose names end with the suffix you pass. The guide locks one spelling and one example so later chapters do not drift:

`todocount --ext .py ./src`

Read the command left to right. You invoke `todocount`. You pass `--ext` with a suffix that includes the dot (`.py`). You pass the root directory to scan (`./src`). The tool walks that root, keeps files that match the suffix, and counts `TODO` and `FIXME` inside those files only.

A few practical notes keep the behavior predictable:

- Pass one suffix per run in this weekend slice. Do not invent comma lists or repeated flags unless a later task adds them on purpose.
- The suffix match is on the file name ending. `.py` matches `app.py` and does not match `app.pyc` unless you asked for `.pyc`.
- Paths that do not exist should still fail the way G02 taught: non-zero exit on an invalid path. `--ext` does not change that contract.
- If you omit `--ext`, you get the default recursive scan from G02. Filtering is opt-in.

When you run the example, compare the filtered count to an unfiltered run on the same tree. The filtered number should be less than or equal to the default number. If it is higher, something is wrong with the walk or the fixture, and you stop to fix the tool before you write more docs.

Keep the wording boring on purpose. Say "limits scans by file suffix." Do not dress the flag up with hype adjectives. Do not invent a version number to celebrate it. Do not add a community chat invite to the chapter because it "feels complete." The success line for this draft is outline fit plus word budget plus voice rules -- not applause.

If a teammate asks whether `--ext` writes a cache or talks to a network service, the answer in this guide is no. The flag only changes which files enter the count. Anything else is out of scope for G03 and belongs in a future task only if the progress file says so.

## What this chapter does not cover

This draft stops at teaching `--ext`. It does not document `--ignore` globs, `--json` output, installers, a GUI, or cloud sync. Those ideas may show up in brainstorms. They are not in the locked outline for G03, so they do not appear as features here.

This chapter also does not rewrite the install steps from G02 or start the test walkthrough reserved for G04. You may tell the reader that the next chapter will show tests that catch drift when `--ext` regresses. Do not paste the test code yet. Do not invent a PyPI package name; that value is UNKNOWN until the publish task lands. Do not invent a license line for the README either.

If you need a one-line forward pointer, use this: G04 will add tests that lock filtered versus unfiltered counts. Then stop. The drafting pass is done when the three sections above are present, the example command appears once, the continuity spellings hold, and the body sits inside the 700-900 word budget.
