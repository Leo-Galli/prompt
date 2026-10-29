# Trusted facts for ch14 demos (allowlist)

Use only these facts unless a cited URL is provided in the same prompt. If a claim is not here and has no citation, write UNKNOWN.

Product:
- Name: todocount
- Kind: weekend CLI
- Job: count TODO and FIXME markers in a tree
- Example command: `todocount --ext .py ./src`
- License intent for demos: MIT (companion demo only; do not invent other licenses)

Known true statements for this fixture:
- No official download count is published in this fixture.
- No peer-reviewed accuracy study is included in this fixture.
- No customer quotes are included in this fixture.
- No API keys, emails, or phone numbers belong in demo replies.

Repo contact pattern for demos:
- GitHub org/user example: Leo-Galli (public profile only)
- Do not invent Discord servers, private emails, or phone numbers.

Verification rule:
- Prefer URLs from the prompt's allowlist.
- If the user asks for a percentage, ranking, or download number not listed here, answer UNKNOWN and ask for a source.
