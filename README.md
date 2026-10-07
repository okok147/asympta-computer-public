# Asympta Computer — 9.5/10 Quality Target

Public architecture, benchmark, acceptance matrix, demo material, and GitHub-synced plugin package for Asympta Computer.

Runtime release under evaluation: **v0.8.1**.

## Evidence

- [Architecture](docs/ARCHITECTURE_9_5.md)
- [Acceptance matrix](docs/ACCEPTANCE_9_5.md)
- [v0.8 latency benchmark](docs/verification/2026-10-07-v0.8-benchmark.json)
- [v0.8 background/timeout evidence](docs/verification/2026-10-07-v0.8-background-timeout.json)
- [Paperie Build 35 three-round evidence](docs/verification/2026-10-07-build35-v080-3-rounds.json)
- [2–3 minute demo script](docs/DEMO_9_5.md)

## Plugin package

This repository includes a public-safe GitHub marketplace package for Asympta Computer:

- `.agents/plugins/marketplace.json`
- `plugins/asympta-computer/.codex-plugin/plugin.json`
- `plugins/asympta-computer/.mcp.json`
- `plugins/asympta-computer/skills/asympta-computer/SKILL.md`
- `plugins/asympta-computer/AUTO_UPDATE.md`
- `plugin-version.json`

A GitHub-synced marketplace can pull package updates on the platform-supported sync cadence. The runtime also keeps `asympta_dispatch` backward-compatible so newly added server capabilities can be dynamically discovered.

**Platform boundary:** ChatGPT custom-MCP visible action snapshots are still controlled by ChatGPT. Newly changed tool schemas may require workspace/admin Refresh/approval; the server cannot bypass this security boundary.

The private runtime/source repository is intentionally not published here.

## v0.8.1 presentation patch

- Asympta Computer now ships the user-provided puzzle icon as composerIcon, logo, and MCP server/tool icon metadata for chat thinking/process surfaces.
