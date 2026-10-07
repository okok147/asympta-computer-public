# Asympta Computer — 9.5/10 Quality Target

Public architecture, acceptance evidence, benchmark material, and GitHub-synced plugin package for Asympta Computer.

Runtime release under evaluation: **v0.10.0**.

## v0.10.0 portable GitHub memory

- Long-term memory is GitHub-authoritative.
- Private source-of-truth repo: `okok147/asympta-computer-memory`.
- Local memory is a disposable cache/offline/runtime layer.
- Portable memory covers standing instructions, playbooks, reflections, traps, continuation summaries and selected output/blackboard notes.
- Credentials, tokens, private keys, raw audit/job/process logs and transient executable state are excluded.
- Clean-machine restore and multi-machine append-only merge were verified.
- The private memory records themselves are **not** mirrored into this public repository.

## Evidence

- [Architecture](docs/ARCHITECTURE_9_5.md)
- [Acceptance matrix](docs/ACCEPTANCE_9_5.md)
- [v0.10 portable memory evidence](docs/verification/2026-10-07-v0.10-portable-memory.json)
- [v0.9 predictive execution + external blackboard](docs/verification/2026-10-07-v0.9-predictive-blackboard.json)
- [v0.8 latency benchmark](docs/verification/2026-10-07-v0.8-benchmark.json)
- [v0.8 background/timeout evidence](docs/verification/2026-10-07-v0.8-background-timeout.json)
- [Paperie Build 35 three-round evidence](docs/verification/2026-10-07-build35-v080-3-rounds.json)
- [2–3 minute demo script](docs/DEMO_9_5.md)

## Plugin package

This repository includes the public-safe portable plugin package:

- `.agents/plugins/marketplace.json`
- `plugins/asympta-computer/plugin.json`
- `plugins/asympta-computer/mcp.json`
- `plugins/asympta-computer/.codex-plugin/plugin.json`
- `plugins/asympta-computer/.mcp.json`
- `plugins/asympta-computer/skills/asympta-computer/SKILL.md`
- `plugins/asympta-computer/AUTO_UPDATE.md`
- `plugin-version.json`

A GitHub-synced marketplace can pull package updates on the platform-supported sync cadence. `asympta_dispatch` remains the forward-compatible capability path when a client caches older visible tool metadata.

ChatGPT custom-MCP visible action snapshots are still controlled by ChatGPT. Newly changed tool schemas may require workspace/admin Refresh/approval; the server cannot bypass this boundary.

The private runtime source and private portable-memory records are intentionally not published here.

## v0.9.1 portable plugin branding fix

- Adds root portable `plugin.json` and `mcp.json`.
- Uses a spec-compliant 68×68 square Asympta icon.
- Existing direct custom-MCP ChatGPT connections still require client-side refresh/reinstall to switch to the branded plugin surface.
