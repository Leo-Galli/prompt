# Output provenance

All quoted files in this folder are real model replies produced in a coding-agent session on 2026-10-29 while drafting Prompt Chapter 3. They are not hand-written fake transcripts.

| File | Prompt source | Notes |
| --- | --- | --- |
| `before-freeform-2026-10-29.md` | `../before/freeform-bug-summary.md` | Readable prose; no stable machine shape |
| `after-schema-2026-10-29.md` | `../after/schema-bug-summary.md` | Raw JSON matching the five-key contract |
| `failed-json-2026-10-29.md` | `../after/failed-json-ask.md` | Soft JSON ask; reply wrapped in Markdown fences; strict parse fails |
| `fix-pass-json-2026-10-29.md` | `../after/fix-pass-json.md` | Fix-pass quoting the failure; raw JSON parses cleanly |

Re-run the prompts in your own product; results will differ. Do not replace these files with invented text. Add new dated files instead.

## Quick validation (optional)

From this chapter folder, with Python 3:

```bash
python -c "import json,pathlib; p=pathlib.Path('outputs/after-schema-2026-10-29.md').read_text(encoding='utf-8'); body=p.split('---',1)[1].strip(); json.loads(body); print('after-schema: ok')"
python -c "import json,pathlib; p=pathlib.Path('outputs/failed-json-2026-10-29.md').read_text(encoding='utf-8'); body=p.split('---',1)[1].strip();
try:
 json.loads(body); print('failed-json: unexpected pass')
except json.JSONDecodeError as e:
 print('failed-json: expected fail:', type(e).__name__)"
python -c "import json,pathlib; p=pathlib.Path('outputs/fix-pass-json-2026-10-29.md').read_text(encoding='utf-8'); body=p.split('---',1)[1].strip(); json.loads(body); print('fix-pass: ok')"
```
