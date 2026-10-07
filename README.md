# Asympta Computer — 9.5/10 Quality Target

Public architecture, benchmark, acceptance matrix, demo material, and GitHub-synced plugin package for Asympta Computer.

Runtime release under evaluation: **v0.9.1**.

## Evidence

- [Architecture](docs/ARCHITECTURE_9_5.md)
- [Acceptance matrix](docs/ACCEPTANCE_9_5.md)
- [v0.9 predictive execution + external blackboard](docs/verification/2026-10-07-v0.9-predictive-blackboard.json)
- [v0.8 latency benchmark](docs/verification/2026-10-07-v0.8-benchmark.json)
- [v0.8 background/timeout evidence](docs/verification/2026-10-07-v0.8-background-timeout.json)
- [Paperie Build 35 three-round evidence](docs/verification/2026-10-07-build35-v080-3-rounds.json)
- [2–3 minute demo script](docs/DEMO_9_5.md)

## v0.9.0 predictive execution

- Every non-control action gets a durable simulated action/result map before execution.
- Prediction matches stay on the fast path; deviations generate traps and a future replan.
- Deterministic exact-repeat failures are blocked rather than looped.
- Continuation capsules externalize chat context so client/UI interruption does not imply replaying side effects.
- `blackboard_note` allows compact answer/output checkpoints for longer-term behavior learning.
- Stable `asympta_dispatch`, direct typed tools, durable jobs, and flow workers share the same predictive boundary.

**Platform boundary:** the MCP server cannot guarantee detection or forced refresh/re-submit of a ChatGPT UI stall. UI refresh remains a client responsibility. The server instead guarantees durable resume state and forbids blind replay of consequential actions after reconnect.

## Plugin package

This repository includes a public-safe GitHub marketplace package for Asympta Computer:

- `.agents/plugins/marketplace.json`
- `plugins/asympta-computer/.codex-plugin/plugin.json`
- `plugins/asympta-computer/.mcp.json`
- `plugins/asympta-computer/skills/asympta-computer/SKILL.md`
- `plugins/asympta-computer/AUTO_UPDATE.md`
- `plugin-version.json`

A GitHub-synced marketplace can pull package updates on the platform-supported sync cadence. The runtime also keeps `asympta_dispatch` backward-compatible so newly added server capabilities can be dynamically discovered.

ChatGPT custom-MCP visible action snapshots are still controlled by ChatGPT. Newly changed tool schemas may require workspace/admin Refresh/approval; the server cannot bypass this security boundary.

The private runtime/source repository is intentionally not published here.

## v0.8.1 presentation patch

- Asympta Computer ships the user-provided puzzle icon as composerIcon, logo, and MCP server/tool icon metadata for chat thinking/process surfaces.

## v0.9.1 portable plugin branding fix

- Adds root portable `plugin.json` and `mcp.json`.
- Uses a spec-compliant 68×68 square Asympta icon for composer/listing branding.
- Existing direct custom-MCP ChatGPT connections still require client-side refresh/reinstall to switch to the branded plugin surface.
