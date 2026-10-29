# Model output -- failed JSON ask (fence-wrapped)

- Date: 2026-10-29
- Prompt: ../after/failed-json-ask.md
- Context: single-turn coding-agent session used while authoring the companion folder
- Note: This is a real reply to a soft "return JSON" ask. A strict `json.loads` on the full reply fails because of Markdown fences. That failure is the teaching point; the object inside is otherwise sensible.

---

```json
{
  "ticket_id": "LINE-218",
  "title": "Windows path with spaces fails",
  "symptom": "Unquoted path with spaces -> File not found, exit 1",
  "priority": "high",
  "repro_hint": "PowerShell: linecount C:\\Users\\Ada Lopez\\notes.txt"
}
```
