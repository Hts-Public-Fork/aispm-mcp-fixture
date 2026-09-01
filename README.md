# aispm-mcp-fixture

A test fixture for **HTSOne AI-SPM**. Not a real application — every file
exists to exercise one detection path.

`GITHUB_TOKEN` in `.mcp.json` is the literal string `PLACEHOLDER-SEE-README`.
It is not a credential; it is there so the inline-credential rule has something
to fire on.

## What each file is for

| file | should produce |
|---|---|
| `.mcp.json` | 3 MCP servers, tool snapshots from `autoApprove`, an inline-credential finding, an auto-approve finding |
| `.vscode/mcp.json` | a 4th MCP server + snapshot |
| `requirements.txt` | pinned + unpinned AI packages |
| `app/agent.py` | a genuine agent |
| `app/rag.py` | genuine RAG + a vector store |
| `app/models.py` | genuine HuggingFace model ids |
| `services/http_client.py` | **nothing.** Every construct in it is a false positive that AI-SPM used to report |

That last row is the point. `User-Agent`, `user_agent`, `storage`, `coverage`,
`average`, `leverage` and `"application/json"` were all reported as AI usage
until 2026-08-21. They are kept here so a regression is visible.

<!-- signing rollout probe 2026-09-01T07:08:18Z: forces a scan job so the signature verdict can be observed -->
<!-- enforce-mode probe 2026-09-01T07:13:58Z -->
