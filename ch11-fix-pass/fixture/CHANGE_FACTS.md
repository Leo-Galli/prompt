# Trusted change facts (only these)

Use this file as the allowlisted fact set for the Chapter 11 worked example.
Do not invent versions, dates, platforms, or extra flags.

- Tool name: todocount
- Change id: T03
- Behavior added: `--ext <suffix>` limits which files are scanned by suffix
- Example: `todocount --ext .py ./src`
- Related tests: filtered vs unfiltered scan cases must pass
- Not in this change: `--ignore`, `--json`, installers, GUI, cloud sync, version bump text
- Voice: US English, ASCII only
