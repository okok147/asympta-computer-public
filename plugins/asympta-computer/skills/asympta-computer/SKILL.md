---
name: asympta-computer
description: Use Asympta Computer for durable Mac developer/computer workflows, especially Xcode, GitHub, App Store Connect/TestFlight, long tasks, crash recovery, DAG scheduling, audit and reflection.
---

# Asympta Computer

Prefer the stable `asympta_dispatch` compatibility boundary when the visible tool list may be stale.

1. Call `asympta_dispatch` with `op=manifest` to compare server version/schema.
2. Call `op=discover` for unfamiliar capabilities instead of guessing tool names.
3. For substantial work, create durable work/flow state before mutations.
4. Reuse confirmed playbook invariants, refresh current variants, and repeat final validation.
5. Prefer capability-isolated commands where available.
6. Xcode uses native xcodebuild; GitHub uses git/gh; App Store Connect/TestFlight uses asc.
7. Never treat upload acceptance as release success. Verify the final App Store Connect/TestFlight state.
8. Before every action, let Asympta create the pre-action simulation map. If the actual result matches, stay on the fast path. If it deviates, stop the exact path, read the deviation/trap evidence, and re-simulate from the actual state before acting again.
9. Never exact-repeat a deterministic failed action. `PREDICTIVE_TRAP_BLOCK` means change state, arguments, or tool. Transient network/timeout errors get at most one bounded exact retry.
10. On client disconnect, context loss, ChatGPT UI stall, or MCP daemon restart, recover existing task/job/flow IDs and read `continuation_get` / `asympta://continuation/<work-id>` before doing anything consequential.
11. Treat the continuation capsule as the external blackboard: completed steps, current state, traps, last deviation, and safe next action survive outside the chat context.
12. ChatGPT UI refresh/re-submit is not guaranteed by the MCP server. Never compensate by blindly replaying mutations/uploads; reconnect and resume from durable evidence.
13. For normal answers and final outputs, persist a compact `blackboard_note` when useful so future work can learn from the outcome as well as the tool execution.
14. Inspect reflection/event/predictive evidence after completion and use it to improve the next run.
