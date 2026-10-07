# Auto-update behavior

This plugin package is intended to be imported through ChatGPT's GitHub-synced plugin marketplace or a compatible Codex marketplace.

- The GitHub marketplace source can sync plugin package changes automatically on the platform's supported cadence.
- The MCP runtime exposes a stable `asympta_dispatch` tool so server-side capability additions can be discovered without changing that compatibility schema.
- ChatGPT MCP app/action snapshots are still controlled by ChatGPT. OpenAI currently requires admin review/Refresh before newly changed MCP actions become enabled. The server cannot bypass this approval boundary.
- Existing stable dispatch calls continue to validate the live action schema on the server.
