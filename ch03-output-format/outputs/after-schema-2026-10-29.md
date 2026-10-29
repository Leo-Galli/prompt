# Model output -- after (schema-constrained JSON)

- Date: 2026-10-29
- Prompt: ../after/schema-bug-summary.md
- Context: single-turn coding-agent session used while authoring the companion folder
- Note: This is a real reply to the schema prompt. The body below the metadata rule is the model reply only (raw JSON, no fences).

---

{"ticket_id":"LINE-218","title":"Unquoted Windows path with spaces returns File not found","symptom":"On Windows PowerShell, path with spaces without quotes yields File not found and exit code 1 though the file exists; macOS/Linux with quoting works","priority":"high","repro_hint":"On Windows PowerShell run linecount with an unquoted path containing spaces, e.g. C:\\Users\\Ada Lopez\\notes.txt","unknown_fields":[]}
