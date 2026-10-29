# Mini outline -- Counting TODOs (weekend CLI guide)

Identity:
- Working title: Counting TODOs
- Subtitle: A Weekend CLI You Can Finish
- Audience: developers who want a tiny Python scanner
- Promise: ship a working `todocount` CLI in one weekend without inventing scope

Locked product facts (do not invent beyond these):
- Tool name: todocount
- Behavior so far: recursively counts `TODO` and `FIXME` markers in a directory tree
- Planned next behavior (this chapter only): document the `--ext` filter that limits scans by file suffix
- Example command: `todocount --ext .py ./src`
- Non-goals for this chapter: installers, GUI, cloud sync, `--json`, `--ignore`, version marketing

Chapter map (guide, not this Prompt book):

| Id | Title | Word budget | Job |
| --- | --- | ---: | --- |
| G01 | Why count markers | 700-900 | Motivate the weekend problem |
| G02 | Install and first run | 700-900 | Get a working default scan |
| G03 | Limit scans with --ext | 700-900 | Teach `--ext` only |
| G04 | Tests that catch drift | 700-900 | Show the failing-then-passing test |
| G05 | What not to add yet | 500-700 | Freeze scope |

This companion run drafts **G03 only**.
