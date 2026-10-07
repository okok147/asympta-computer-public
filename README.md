# Asympta Computer — 9.5/10 Quality Target

Public architecture, acceptance evidence, benchmark material, and GitHub-synced plugin package for Asympta Computer.

Runtime release under evaluation: **v0.12.0**.

## v0.12.0 Mission / Tasklist wrapper + inline ChatGPT/Work card

- `work_*` remains the only canonical task graph; Tasklist stores only mission focus, completion criteria, horizon and phase.
- Progress, next actions and blockers are derived live, so the wrapper cannot drift from actual execution state.
- With a mission `work_id`, Ultra brief suppresses duplicate normal work/continuation context; historical traps on already-completed steps stay in durable evidence but do not bloat normal resume context.
- The `asympta_port` tool links to an MCP Apps inline task card. Full checkbox rows are sent through tool-result `_meta`, which ChatGPT keeps hidden from the model.
- 16-step fixture: full work + continuation ≈ **2,034 estimated tokens**; normal Mission brief ≈ **187**, **10.89× smaller / 90.82% reduction**.
- Live runtime: **129 catalog / 2 exposed tools**. Final regression: **103/103**; focused Mission+Ultra: **15/15**; audit: 0 vulnerabilities.
- Public verification: [v0.12 Mission/Tasklist evidence](docs/verification/2026-10-07-v0.12-mission-tasklist.json).

## v0.11.0 ChatGPT-first Ultra compression

- Default MCP surface is only `asympta_port` + `asympta_dispatch`; the full **124-capability** catalog remains server-side.
- Advertised schema dropped from about **93,470 bytes / 23.4k estimated tokens** to **2,276 bytes / 569 estimated tokens**: **41.58× smaller / 97.59% reduction**.
- Normal execution returns a tiny receipt; Work-style polling by `work_id` can be exactly `{"s":0}` or `{"s":1}` (**7 bytes**).
- Full results remain in local receipts and expand only when explicitly requested; compact briefs are intent-filtered, cached, and delta-aware.
- Full compatibility remains available with `ASYMPTA_TOOL_EXPOSURE=full`.
- Current verification: **95/95 full regression**, **8/8 Ultra regression**, live compact manifest **2 exposed / 124 catalog tools**.
- These numbers measure MCP-visible schema/context/result compression; they do not claim control over OpenAI internal ChatGPT Work/Codex token accounting.

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
- [v0.12 Mission/Tasklist + inline UI evidence](docs/verification/2026-10-07-v0.12-mission-tasklist.json)
- [v0.11 Ultra compression evidence](docs/verification/2026-10-07-v0.11-ultra-compression.json)
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
- `plugins/asympta-computer/ui/mission-tasklist.html`
- `plugins/asympta-computer/AUTO_UPDATE.md`
- `plugin-version.json`

A GitHub-synced marketplace can pull package updates on the platform-supported sync cadence. `asympta_dispatch` remains the forward-compatible capability path when a client caches older visible tool metadata.

ChatGPT custom-MCP visible action snapshots are still controlled by ChatGPT. Newly changed tool schemas may require workspace/admin Refresh/approval; the server cannot bypass this boundary.

The private runtime source and private portable-memory records are intentionally not published here.

## v0.9.1 portable plugin branding fix

- Adds root portable `plugin.json` and `mcp.json`.
- Uses a spec-compliant 68×68 square Asympta icon.
- Existing direct custom-MCP ChatGPT connections still require client-side refresh/reinstall to switch to the branded plugin surface.
