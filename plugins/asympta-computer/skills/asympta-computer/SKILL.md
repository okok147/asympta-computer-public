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
8. On client disconnect or MCP daemon restart, recover existing task/job/flow IDs instead of restarting consequential work.
9. Inspect reflection/event evidence after completion and use it to improve the next run.
