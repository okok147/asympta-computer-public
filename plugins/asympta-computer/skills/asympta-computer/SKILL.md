---
name: asympta-computer
description: Use Asympta Computer for durable Mac developer/computer workflows, especially Xcode, GitHub, App Store Connect/TestFlight, long tasks, crash recovery, DAG scheduling, audit and reflection.
---

# Asympta Computer

Prefer the stable `asympta_dispatch` compatibility boundary when the visible tool list may be stale.

1. Call `asympta_dispatch` with `op=manifest` to compare server version/schema.
2. Call `op=discover` for unfamiliar capabilities instead of guessing tool names.
3. On a new machine/client or when memory may be stale, read `memory_status` and `memory_profile_get`; pull GitHub memory before substantial work if bootstrap has not completed.
4. Treat private GitHub portable memory as long-term source of truth. Local memory is only a disposable cache/offline fallback; never copy raw credentials, audit logs, job logs, or process output into portable memory.
5. For substantial work, create durable work/flow state before mutations.
6. Reuse confirmed playbook invariants, refresh current variants, and repeat final validation.
7. Prefer capability-isolated commands where available.
8. Xcode uses native xcodebuild; GitHub uses git/gh; App Store Connect/TestFlight uses asc.
9. Never treat upload acceptance as release success. Verify the final App Store Connect/TestFlight state.
10. Before every action, let Asympta create the pre-action simulation map. If the actual result matches, stay on the fast path. If it deviates, stop the exact path, read the deviation/trap evidence, and re-simulate from the actual state before acting again.
11. Never exact-repeat a deterministic failed action. `PREDICTIVE_TRAP_BLOCK` means change state, arguments, or tool. Transient network/timeout errors get at most one bounded exact retry.
12. On client disconnect, context loss, ChatGPT UI stall, or MCP daemon restart, recover existing task/job/flow IDs and read `continuation_get` / `asympta://continuation/<work-id>` before doing anything consequential.
13. Treat the continuation capsule as the external blackboard: completed steps, current state, traps, last deviation, and safe next action survive outside the chat context.
14. ChatGPT UI refresh/re-submit is not guaranteed by the MCP server. Never compensate by blindly replaying mutations/uploads; reconnect and resume from durable evidence.
15. For normal answers and final outputs, persist a compact `blackboard_note` when useful so future work can learn from the outcome; portable memory will sync allowed summary notes to GitHub.
16. Inspect reflection/event/predictive/memory evidence after completion and use it to improve the next run.
