# v0.16.7 — Correct handling of shared negative aesthetic intent

A real v0.16.6 Asympta Computer MCP request interpreted the instruction "不要太可愛或塑膠感" incorrectly: it avoided cute styling but treated plastic gloss as **desired**. The updated aesthetic_brief now keeps a negation across coordinated expressions (or/and/或/和), while explicit contrasts and preserve/do-not-lose language stop unintended spillover. Ambiguous long-range scope is flagged instead of silently treating a negative property as positive.

This is a semantic reliability correction inside the **same plugin**, not a new AI model or a universal taste score. v0.16.6 creative planning, human pairwise evidence and the native Computer Use / Xcode / Blender paths remain unchanged. Complete private CI and real Mac MCP entrypoint regression are required before claiming this specific user-observed bug is fixed.

# v0.16.6 — Aesthetic Intent & Taste for creative work

The same **Asympta Computer** ChatGPT/Codex/Claude plugin adds two optional read-only tools for vague art direction in UI/UX, animation and 3D:

- **aesthetic_brief** preserves original words, explicit exclusions, protected designs and technical constraints. It proposes three reversible creative directions and visual, motion and functional validation criteria. If an observed sequence is actually supplied, it can describe empirical first-order transitions, **not** a listener's expectation or a beauty score.
- **aesthetic_review** summarizes declared screenshots/renders, claimed technical evidence, and pseudonymous human pairwise preferences. It does **not** inspect images or certify test results. A provisional preference is not publication approval; real artifact inspection and owner judgment remain required.

For relevant creative tasks the plugin skill asks ChatGPT to observe actual work, inspect equivalent variants and verify technical + aesthetic outcomes before release. The pure helper itself uses no extra model/network calls, leaving speed and cost of actual creative workflow to be measured. Research-inspired lenses of classical/expressive aesthetics and unity-in-variety are **not** universal taste formulas.

The existing Xcode/TestFlight, Blender, macOS Accessibility and native Computer Use paths remain unchanged. The private implementation carries focused tests, seeded local microbenchmarks and GitHub CI; measured visual-preference improvements or global artistic rankings are **not claimed**.

# v0.16.5 — Reliable background job completion

The existing Asympta Computer plugin now prevents compact-MCP durable jobs from reporting success while a nested command is still running. The job worker uses the internal tool catalog (without expanding ChatGPT's public tool list), waits for the child process exit, and records terminal exit code/output. A real child-process regression test is included in the private runtime. macOS local full regression passed 292/292; public metadata, CI and installed-runtime verification are separate delivery gates.

The v0.16.4 native `computer_laser` remains available and still enforces bounded AX scans and focus/mouse checks. Initial read-only Mac Finder A/B encountered incomplete-scan/attention-preservation failures under concurrent activity, so a reliable end-to-end performance multiplier is not yet established; retain the existing fallback for uncertain UI states.

# v0.16.4 — One-process macOS Computer Use laser (XCTest-inspired)

The same **Asympta Computer** ChatGPT/Codex/Claude plugin now advertises `computer_laser`, a bounded single native Swift Accessibility control loop for semantic observation, AXPress, AXValue and explicit assertion steps (up to 10 per call). Compared to separately launching a helper for every UI step, this architecture is designed to cut native process launches and MCP tool roundtrips. It returns compact outcomes instead of entire AX trees.

Accuracy first: exact semantic identifier/text+role, unique-match requirement, bounded complete scans, conditional waiting *only* on read-only assertions, no blind click/write replay, macOS Accessibility permission retained, and no global mouse injection. An AX action acknowledgment is **not** a verified UI outcome; use a following assertion.

**Hardware Mac speedup is not yet verified.** Initial Apple API research and source-level comparison are in the [private design record](https://github.com/okok147/asympta-computer-mcp/blob/feat/computer-native-laser-v0164/docs/verification/2026-10-10-v0164-computer-laser.md). GitHub macOS Swift compilation and a real Finder/disposable-app A/B are mandatory before reporting performance improvement. No separate app or plugin, no user data modification.

# Asympta Computer v0.16.3 — Speed, accuracy and usage saving

The **same** Asympta Computer ChatGPT/Codex/Claude plugin now supports faster bounded CLI output buffering, truthful UTF-8/total output bytes and explicit truncation, and opt-in lightweight capability discovery.

- \`asympta_dispatch(op="discover", detail="compact")\` saves **74.04%** of structured discovery JSON bytes versus legacy \`detail="full"\` for 100 tool results. \`detail="names"\` saves **96.43%**.
- \`run_command(max_output_bytes=4096)\` returns the tail and actual emitted byte count, saving **96.32%** of result JSON bytes on the representative 120KB CLI case. Omitting this optional limit preserves legacy output capacity.
- A fixed-capacity lazy ring reduces large command-output allocations and keeps exit/Unicode/streaming evidence. Isolated 16.8MB process output benchmark: seven-run P50 **199.34 → 63.55ms**, cumulative CPU **1,216 → 154ms**, final process RSS **381 → 80MB**; these are local synthetic workload results, not ChatGPT end-to-end performance.
- Original default discovery and CLI result semantics remain unchanged. No additional app, security permission bypass or physical iPad gesture changes.

Source verification, raw data and error boundaries are in the private execution repository: \`docs/verification/2026-10-10-v0163-speed-accuracy-usage.md\`. Historical public release notes are preserved below.

# v0.16.2 — Apple-native wireless iPad connectivity

The **same Asympta Computer plugin** now supports read-only `ipad_wireless_status` and optional `wireless_only:true` on `ipad_status`, `ipad_test` and `ipad_laser`. This uses Xcode 27 Device Hub/CoreDevice to work with a physically paired iPad over a confirmed Wi-Fi/network transport, with no second app or custom proxy. A plugged-in USB transport or an unknown connection is never reported as cable-free success.

Xcode 27 can pair iPadOS 27+ over Wi-Fi from **Device Hub → Add Device (+) → Pair Nearby Device…**; PIN, Trust and Developer Mode prompts still require the owner's action. The runtime refuses to switch Mac network settings or fake connection status. Current real iPad Air M4 is known/paired but was unavailable while Mac Wi-Fi was not associated; a successful **unplugged** XCUITest remains unverified.

Official reference: https://developer.apple.com/documentation/xcode/pairing-your-devices-with-your-mac . Existing v0.16.1 optimization and all previous release notes follow.

# v0.16.1 — Three measured Asympta Computer improvements

Same plugin identity; no second app. The private MCP runtime is upgraded with (1) offline feedback fast path, (2) bounded backward-streaming of persisted iPad steering history with serialized writes, and (3) version-fenced memoization and a proven monotonic recent-byte index. A 70,000-record, 18.8 MB synthetic feedback fixture yielded a 0.048ms in-process **hot-cache** Laser median versus 173.703ms at the v0.16.0 baseline; the **live append-followed-by-read** median was 0.123ms (read only). The initial uncached read remains ~65ms; no real iPad gesture or ChatGPT network latency benefit has been measured. Correctness gates include 90 deterministic differential queries and the full plugin regression suite.

No Apple permissions are bypassed, historical data is not deleted, and genuine Apple Pencil pressure/latency remain hardware-only. Full research/methodology in the private repository verification document.

# v0.16.0 — one Asympta Computer plugin with native physical-iPad laser bridge

The same plugin now exposes bounded real-iPad observe → action → screenshot/XCTest/steering feedback via its existing MCP. Incremental Xcode build caching, grouped UI test filters, physical-device lease and failure-classified xcresult improve the **design** for speed and accuracy. Actual latency and success-rate improvements require hardware measurements. No second app, Simulator fallback, macOS/iPad approval bypass or simulated real Apple Pencil pressure is provided.

The ChatGPT/Codex/Claude portable package points to the existing private runtime at v0.16.0. GitHub metadata and installed service are verified separately. No Paperie app feature tests were run as part of this plugin-only upgrade.

# Asympta Computer — 9.5/10 Quality Target

Public architecture, acceptance evidence, benchmark material, and GitHub-synced plugin package for Asympta Computer.

Historical deployed runtime for that evidence snapshot: **v0.15.4** (2026-10-08). Live MCP reports 127 internal capabilities and 2 exposed tools; a new hidden read-only `work_query` tool is available through stable dispatch. The public package tracks this runtime; ChatGPT's client-side display cache may still require manual Refresh.

## v0.15.4 Intent-first work queries (verified)

- **Declarative request:** `work_query` selects work by safe filters (ID/status/title/recency/readiness) and exposes only requested allowlisted fields. A direct ID uses a single canonical record; a broader request uses bounded canonical JSON scanning. There is no extra mutable index, SQL expression, or shadow work state.
- **Measured output economy:** Existing five-work report: 49,544 → 1,745 JSON bytes (-96.5%). Synthetic 500-work sample, returning 200: 533,001 → 20,123 JSON bytes (-96.2%). Those are query-payload bytes, not total MCP transport bytes or proven token savings. Latency was inconsistent under other Mac workloads; no speedup is claimed.
- **Evidence:** v0.15.4 candidate passed 157/157 local tests; GitHub macOS and Ubuntu workflows [passed](https://github.com/okok147/asympta-computer-mcp/actions/runs/37720150858). Installed service restarted and live ChatGPT MCP dispatch verified new `work_query`, `work_list`, version 0.15.4, 127 internal/2 exposed tools. The original Codd 1971 and Kaplan et al. §4 were methodological inspirations, not drop-in formula improvements.
- **Usage:** `asympta_dispatch(op="discover", query="work_query")`, then `asympta_dispatch(op="call", action="work_query", arguments={where:{status:"active"},fields:["id","title","status"],max_bytes:4096})`.
- [Sanitized verification](docs/verification/2026-10-08-v0.15.4-public.json). Client-side ChatGPT connector Refresh may still be required to refresh labels/icons.

## v0.15.3 Read-independent work queries and bounded scanning (verified)

- **Canonical timestamp correctness:** `work_*` and `playbook_*` reads no longer refresh persisted `updated_at`; actual updates still advance it. A live duplicate `work_get` probe returned identical timestamps.
- **Query performance:** bounded 8/16-worker JSON scanning replaces serial per-file reads without introducing a duplicate database or changing existing MCP authorization, tool schema, or ordering behavior. The 500-work synthetic loaded-host comparison measured 10,264.754 ms → 1,691.990 ms (6.07×), but these times were inflated by other workloads and **are not an overall MCP latency claim**.
- **Full independent verification:** GitHub Actions [run 37697048190](https://github.com/okok147/asympta-computer-mcp/actions/runs/37697048190): macOS **149/149 PASS**, Linux **146/149 PASS** (3 platform-specific skipped), zero failures. Installed Mac focused tests: 7/7 query and 3/3 portable memory passing.
- **Method transfer only:** [Codd 1970](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks) informs data independence, while [Kaplan et al. 2020](https://arxiv.org/pdf/2001.08361#page=7) informs explicit compute-budget measurements. Their mathematical formulas are not claimed to accelerate MCP directly.
- [Public verification summary](docs/verification/2026-10-08-v0.15.3-public.json).

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
