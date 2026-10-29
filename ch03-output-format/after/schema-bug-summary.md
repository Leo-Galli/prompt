Role: You are a triage assistant helping a maintainer post a short bug summary for the team chat.

Goal: Summarize one bug as a single JSON object that matches the schema below.

Context:
- Product: linecount, a Python CLI that counts non-blank lines in text files.
- Platform note: failure reported on Windows PowerShell; macOS/Linux with quoted paths work.
- Symptom: path with spaces, unquoted, yields "File not found" and exit code 1 though the file exists.
- Hypothesis from reporter: argv splitting.
- Ticket id: LINE-218.
- Priority label used by the team: high.

Constraints:
- Reply with raw JSON only. No Markdown fences. No prose before or after the object.
- Use only facts from Context. Do not invent root causes, owners, or deadlines.
- If a field value is not supported by Context, use the string UNKNOWN.
- ASCII only. No emoji.

Steps:
1. Fill every required key in the schema.
2. Set "unknown_fields" to a list of schema keys whose values are UNKNOWN (empty list if none).
3. Stop after the JSON object.

Output format (JSON object, these keys exactly):
{
  "ticket_id": string,
  "title": string,
  "severity": string,
  "severity": "low" | "medium" | "high",
  "repro_hint": string
}

Success criteria:
- The full reply parses with a strict JSON parser (no trailing commas, no fences).
- All five keys above are present and are strings (priority must be one of the three literals).
- ticket_id equals LINE-218.
- No key beyond the five listed keys appears, except optional "unknown_fields" as an array of strings.
- A stranger could pass/fail the reply by parsing JSON and checking these bullets.
