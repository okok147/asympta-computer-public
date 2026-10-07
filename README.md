# Asympta Computer — 9.5/10 Quality Target

Public architecture, acceptance evidence, benchmark material, and GitHub-synced plugin package for Asympta Computer.

Current deployed runtime: **v0.15.2** (2026-10-08). The live MCP reports 126 internal capabilities and 2 exposed tools; plugin package metadata tracks this runtime. ChatGPT-side display metadata may still require a platform refresh.

## v0.15.2 Linear DAG failure propagation (verified)

- Replaced repeated failed-dependency scans with reverse-adjacency BFS over pending nodes, with a no-failure fast path. **O(V+E)** failure traversal (500-node maximum flow graph); existing MCP interface, resource checks and authorization behavior unchanged.
- Full automated suite: **142/142 passed, 0 failed**. The new logic passed **2,000 seeded randomized DAG differential comparisons** against the previous fixed-point algorithm.
- On a 500-node *reverse-chain failure microbenchmark*, closure median changed from **4.0925 ms to 0.05496 ms (~74.47×)** on the release candidate; the deployed runtime repeat was **4.19675 ms to 0.05992 ms (~70.04×)**. This is **not an overall MCP speedup**. Broad-fanout work improved only ~1.02×.
- the [2026 exact DFT research](https://github.com/openai/math) provides only methodological inspiration for exploiting structure. No faster floating-point FFT was implemented or claimed.
- [Public verification summary](docs/verification/2026-10-08-v0.15.2-public.json).
- The previously observed Safari cold/concurrent AX timeout remains a separate open reliability issue.

## v0.15.1 Bounded reliability and verified mathematical transfer

- **139/139 automated regressions passed**, plus Node syntax, Swift typecheck, and Git diff validation.
- The live MCP server reported **126 available capabilities / 2 exposed tools** under stable dispatch, version `0.15.1`.
- Multiscale source search found a root-level test needle under `/private/tmp`, reporting explicit `byte_budget` truncation instead of hanging. The scanner reported 85 ms internal execution for that one bounded test; this is not end-to-end ChatGPT latency.
- Safari Accessibility inspection at 120 elements / depth 6 completed in a warm read; one earlier concurrent cold-start attempt timed out at 5 seconds and remains a reliability follow-up, not a clean cold-start pass.
- Xcode/Swift status probes returned verified installed results with timeout-only retry and success caching. The plugin icon is now an independently hash-checked **512×512 RGBA PNG**.
- From the October 2026 [OpenAI mathematics release](https://github.com/openai/math), we adapted *localization, bounded search, and independent certificates* as engineering methods. These are analogies independently tested on the product; no mathematical theorem is claimed to directly accelerate the MCP.
- A trial scheduler that improved proxy criticality scores was **rejected** after making simulated end-to-end DAG runtime 0.316% worse.
- [v0.15.1 public verification notes](docs/verification/2026-10-08-v0.15.1-public.json).

## v0.15.0 Verified-frontier orchestration

- Default surface remains **2 exposed tools**; the live internal catalog is **126 capabilities**.
- Evidence-constrained finite Pareto frontier: quality/verification gates cannot be traded away for latency, response size, or declared memory.
- Event-driven flow scheduling refills free slots immediately while independently checking dependencies, capacity, resource conflicts, and declared memory budgets.
- Generator/verifier separation adds capability gates and explicit independent verification evidence.
- Compact receipts expose bounded action / step / process / latest-line progress; bounded `process_read(wait_ms)` reduces fragile polling.
- Native serialized Foundation Trash handling passes `/private/tmp` and concurrent same-name preservation tests.
- Final full regression: **136/136 PASS, 0 fail**; live original-path verification also passed.
- Verified read path reduced 12 reads from **24 → 12 calls** and **12,600 → 5,580 response bytes**. Response bytes are not model/platform tokens.
- No latency speedup claim is made because release-time shared-host contention invalidated a fair timing comparison.
- Public design note: [Verified-frontier orchestration](docs/VERIFIED_FRONTIER.md).
- Public evidence: [v0.15 release summary](docs/verification/2026-10-07-v0.15.0-public.json).

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
