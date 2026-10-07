# Asympta Computer 9.5/10 Quality Acceptance Matrix

Runtime release under evaluation: **v0.10.0**.

This matrix is evidence-driven. A requirement is PASS only when the stated proof exists.

| # | Requirement | Status | Evidence |
|---:|---|---|---|
| 1 | Real long-running task >1h | **PASS** | Detached canary `c7f36769-a61c-4e06-9465-cb431e185b1f` completed after **3663.26 s** (>61 min). |
| 2 | Client disconnect does not stop task | **PASS** | The live canary continued through MCP/client reconnect with the same worker PID/generation and progressing heartbeat. |
| 3 | Daemon crash recovery | **PASS** | MCP daemon was force-killed and LaunchAgent restarted it; the long-running worker continued. DAG crash regression replays idempotent nodes and fences non-idempotent nodes as `uncertain`. |
| 4 | Command/event latency benchmark | **PASS** | v0.8 benchmark: dispatch p50 **6.032 ms**, event append **7.056 ms**, event verify **1.855 ms**, Node command **42.032 ms**, steering RTT **5.108 ms**. |
| 5 | Mac ↔ iPad realtime steer | **PARTIAL / external device gate** | Paired LAN SSE + persistent signals pass and steering service is live. Physical `ok’s iPad` is still `unavailable` in `devicectl`, so device-level proof is not claimed. |
| 6 | Agent can auto-discover tools | **PASS** | v0.10 adds portable-memory tools on top of the stable dispatch surface; `asympta_dispatch discover` dynamically finds current capabilities even when ChatGPT visible metadata is stale. |
| 7 | Parallel workers + dependency scheduling + multi-agent | **PASS** | Durable DAG scheduler, critical-path priority, crash recovery, and `team_*` capability-aware allocation pass. Current scheduler microbenchmark: **1.42×**; earlier repeated runs: **2.11× / 2.17× / 2.40×**. |
| 8 | Shell capability/security isolation | **PASS** | `repo_read` sandbox allows repo reads while denying Home access, interpreter escape, and `git push`; release/model paths use explicit capability profiles. |
| 9 | Every action has audit trail | **PASS** | Every MCP tool action is written to normal audit and SHA-256 hash-chained event history; tamper regression detects modified history. |
| 10 | GPT + Claude can operate | **BLOCKED EXTERNALLY** | ChatGPT is live. Claude Code is installed and MCP-configured through `model_client`, but `claude auth status` returns `loggedIn:false`; a real Claude model call cannot be honestly marked PASS until the user authenticates Anthropic. |
| 11 | Real Xcode → GitHub → TestFlight workflow | **PASS** | Paperie Build 35: GitHub source `592f4fe` → three signed archives → IPA export → native `asc` upload → build `31c4e2b1-66c4-4981-a2ce-38834228ffd0` **VALID + IN_BETA_TESTING** in Internal. |
| 12 | Public architecture + benchmark + 2–3 minute demo | **PASS** | Public evidence repo: `okok147/asympta-computer-public`; private runtime source remains private. |

## Additional v0.10 gates

- **PASS** — Full pre-deploy regression suite: **86/86** tests.
- **PASS** — `npm audit`: **0 vulnerabilities**.
- **PASS** — `git diff --check`.
- **PASS** — Installed service reports **v0.10.0**.
- **PASS** — Stable dispatch exposes the current server despite stale client metadata.
- **PASS** — Every non-control action gets a durable pre-action simulated action/result map.
- **PASS** — Matching results stay on the fast path; predictive bookkeeping optimized to **5.932 ms p50 / 9.481 ms p95** roundtrip, with post-match bookkeeping **0.440 ms p50**.
- **PASS** — Deterministic exact-repeat failure is blocked by `PREDICTIVE_TRAP_BLOCK`; transient network/timeout paths get at most one bounded exact retry.
- **PASS** — Installed live smoke: exit-17 deviation → active `process_exit` trap → exact repeat blocked → changed action `RECOVERED_LIVE` → trap cleared → work completed.
- **PASS** — Durable external blackboard + `continuation_get` resume capsule exposes completed/current/ready steps, traps, last deviation, and safe next action outside chat context.
- **PASS** — `asympta://predictive`, `asympta://continuation/active`, and dynamic continuation resources verified live.
- **PASS** — `asympta_dispatch call`, direct tools, durable jobs, and flow workers share the same predictive execution boundary.
- **PASS** — Private GitHub long-term memory source of truth: `okok147/asympta-computer-memory`.
- **PASS** — Seeded memory: 8 standing instructions, 9 playbooks, 11 reflections, 4 traps, 3 continuation capsules and 2 blackboard summaries.
- **PASS** — Clean-machine restore from empty state recovered every seeded category from GitHub.
- **PASS** — Two simulated machines independently appended memories and a third machine restored both without overwrite.
- **PASS** — Seeded repo DLP scan found no GitHub/OpenAI token, private key, or user-specific absolute home-path leak.
- **PASS** — Runtime excludes credentials, raw audit/job/process logs and transient executable state from portable memory.
- **PASS** — Background visual control on a real native harness:
  - background screenshot captured a 36,479-byte PNG;
  - semantic AX click changed target state 0→1;
  - visual-coordinate → AX hit-test click changed state 1→2;
  - Safari remained frontmost;
  - Asympta reported `mouse_injected=false`.
- **PASS** — Offscreen vector drawing: 2,000 points → 123 points (**93.85% reduction**) in **8.039 ms**, `mouse_used=false`, `attention_required=false`.
- **PASS** — Stable dispatch automatically promotes a 30s-class `run_command` to a durable job instead of waiting inside one MCP request.
- **PASS** — Paperie Build 35 three-round benchmark: **45.323 s → 29.593 s → 26.263 s**.
- **PASS** — Cross-build warm/8-worker timing is stable: Build 34 **26.103 s**, Build 35 **26.263 s** (0.61% range).
- **PASS** — Host has 8 available parallelism; build policy therefore uses up to 8 workers and does not oversubscribe.
- **PASS** — Paperie Build 35 export **4.671 s**; TestFlight upload+processing **168.767 s**.
- **PLATFORM LIMIT** — Custom ChatGPT MCP action snapshots still require platform/admin **Refresh** when visible schemas change. The repo ships a GitHub-synced plugin package and permanent stable dispatch, but the server does not claim it can bypass ChatGPT approval.

## Background-control safety boundary

Asympta does **not** claim generic invisible pointer injection into arbitrary games/canvases. Background UI control is only marked supported when the target exposes Accessibility/API actions that can be invoked without activating it.

For unsupported surfaces, Asympta returns unsupported rather than silently moving the user's mouse or stealing focus. Drawing that does not require a target app is rendered fully offscreen as vector output.

## Paperie performance surface

| Build | Cache | Workers | Archive |
|---|---|---:|---:|
| 34 | cold | 1 | 48.691 s |
| 34 | cold | 8 | 28.586 s |
| 34 | warm | 8 | 26.103 s |
| 35 | cold | 4 | 45.323 s |
| 35 | cold | 8 | 29.593 s |
| 35 | warm | 8 | **26.263 s** |

Conclusion: **8 workers + DerivedData reuse** is the stable latency Pareto point on this 8-way host. Preserve cache for routine archives, invalidate it when toolchain/project correctness requires it, and keep tests single-worker/single-simulator for determinism.

## Evidence

- `docs/verification/2026-10-07-v0.8-benchmark.json`
- `docs/verification/2026-10-07-v0.8-background-timeout.json`
- `docs/verification/2026-10-07-v0.9-predictive-blackboard.json`
- `docs/verification/2026-10-07-v0.10-portable-memory.json`
- Paperie: `docs/verification/2026-10-07-build35-v080-3-rounds.json`
- Public architecture/benchmark/demo: `okok147/asympta-computer-public`

## Remaining external gates to literal 12/12

1. Physical iPad must become available for a real device-level steering demonstration.
2. Claude must be authenticated on this Mac before a real Claude model call can be counted as PASS.
