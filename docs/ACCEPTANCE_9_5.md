# Asympta Computer 9.5/10 Quality Acceptance Matrix

Runtime release under evaluation: **v0.7.0**.

This file is evidence-driven. A requirement stays **PENDING** until the stated proof exists.

| # | Requirement | Status | Evidence gate |
|---:|---|---|---|
| 1 | Real long-running task >1h | RUNNING | Detached 61-minute canary `c7f36769-a61c-4e06-9465-cb431e185b1f` is running independently; PASS requires measured elapsed >3600s |
| 2 | Client disconnect does not stop task | PASS | Live canary survived forced MCP daemon SIGKILL/reconnect with the same worker PID and generation while heartbeat continued |
| 3 | Daemon crash recovery | PASS | Live MCP daemon SIGKILL recovered through LaunchAgent; DAG crash regression replays idempotent nodes and fences non-idempotent uncertainty; PID-aware lease locks reclaim dead owners immediately |
| 4 | Command/event latency benchmark | PASS | `docs/verification/2026-10-07-9.5-benchmark.json` |
| 5 | Mac ↔ iPad realtime steer | PARTIAL | LAN paired SSE/signal server is live on port 43111 and protocol regression passes; physical `ok’s iPad` is currently reported `unavailable`, so device-level PASS is not claimed |
| 6 | Agent auto tool discovery | PASS | Installed v0.7.0 exposes 107 tools locally; stable `asympta_dispatch discover` dynamically found current `flow_*` actions despite stale ChatGPT connector metadata |
| 7 | Parallel workers + dependencies | PASS | Critical-path DAG scheduler regression passes; benchmark shows 4-worker flow speedup over sequential execution |
| 8 | Shell capability/security isolation | PASS | Live `repo_read` macOS sandbox allows repo read while denying Home access, interpreter escape and `git push`; Apple release paths use bounded logical capability profiles |
| 9 | Every action audit trail | PASS | Installed hash-chained event history verified clean; tamper regression detects modified history; significant tool/job/flow/steering actions emit events |
| 10 | GPT + Claude model operation | BLOCKED EXTERNALLY | ChatGPT operates the runtime. Claude Code 2.1.292 is installed and points to the same MCP, but `claude auth status` reports `loggedIn:false`; Anthropic login is required before a real Claude model call can pass |
| 11 | Real Xcode → GitHub → TestFlight | PASS | Paperie Build 34 source `12c087e` → three valid Xcode archives → IPA export → native `asc` upload → build `53a2aa08-aff9-4bd2-a663-a36fffa4cef3` `VALID` + `IN_BETA_TESTING` in Internal |
| 12 | Public architecture + benchmark + 2–3 min demo | PASS | Public docs-only repo: `okok147/asympta-computer-public`; private runtime source remains private |

## Additional 9.5 gates

- Full regression suite must pass.
- `npm audit` must report zero known vulnerabilities at release time.
- `git diff --check` must pass.
- Installed service must report 0.7.0.
- Stable dispatch must work even when visible ChatGPT plugin metadata is stale.
- Custom ChatGPT plugin metadata refresh must be attempted after deployment. OpenAI currently requires explicit **Refresh** for changed custom MCP metadata; this platform limitation must not be described as server-controlled auto-refresh.
- Three measured Paperie build rounds must complete before the final performance recommendation.
