# Asympta Computer 9.5/10 Quality Acceptance Matrix

Runtime release under evaluation: **v0.7.0**.

This file is evidence-driven. A requirement stays **PENDING** until the stated proof exists.

| # | Requirement | Status | Evidence gate |
|---:|---|---|---|
| 1 | Real long-running task >1h | RUNNING | Detached 61-minute canary job must complete with measured elapsed >3600s |
| 2 | Client disconnect does not stop task | PARTIAL | Durable detached worker architecture + reconnect test; final live 9.5 disconnect smoke still required |
| 3 | Daemon crash recovery | PARTIAL | Automated worker-crash/replay/uncertainty tests pass; final installed-daemon live smoke required |
| 4 | Command/event latency benchmark | PASS | `docs/verification/2026-10-07-9.5-benchmark.json` |
| 5 | Mac ↔ iPad realtime steer | PARTIAL | Paired SSE/signal protocol regression passes; physical iPad connection still required for device-level PASS |
| 6 | Agent auto tool discovery | PASS (source) | `capability_discover` + forward-compatible `asympta_dispatch discover`; installed 9.5 smoke pending |
| 7 | Parallel workers + dependencies | PASS (source) | DAG flow regression proves sibling parallelism + join ordering + crash recovery |
| 8 | Shell capability/security isolation | PASS (source) | macOS sandbox regression proves repo read while Home/write are denied; Apple paths use strict logical capabilities |
| 9 | Every action audit trail | PASS (source) | audit log + hash-chained event history; tamper regression detected |
| 10 | GPT + Claude model operation | BLOCKED EXTERNALLY | ChatGPT operates current connector. Claude Code 2.1.292 installed and MCP configured, but Anthropic account is not logged in / MCP approval pending |
| 11 | Real Xcode → GitHub → TestFlight | PASS previously / 9.5 re-run pending | Paperie Build 33 previously VALID + IN_BETA_TESTING; Build 34 9.5 workflow required |
| 12 | Public architecture + benchmark + 2–3 min demo | IN PROGRESS | Local docs/demo + benchmark exist; public GitHub repo publish pending |

## Additional 9.5 gates

- Full regression suite must pass.
- `npm audit` must report zero known vulnerabilities at release time.
- `git diff --check` must pass.
- Installed service must report 0.7.0.
- Stable dispatch must work even when visible ChatGPT plugin metadata is stale.
- Custom ChatGPT plugin metadata refresh must be attempted after deployment. OpenAI currently requires explicit **Refresh** for changed custom MCP metadata; this platform limitation must not be described as server-controlled auto-refresh.
- Three measured Paperie build rounds must complete before the final performance recommendation.
