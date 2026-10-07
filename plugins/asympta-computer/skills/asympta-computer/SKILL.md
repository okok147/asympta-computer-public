---
name: asympta-computer
description: Use Asympta Computer for durable Mac developer/computer workflows, especially Xcode, GitHub, App Store Connect/TestFlight, long tasks, crash recovery, DAG scheduling, audit and reflection.
---

# Asympta Computer

Default to Ultra mode: ChatGPT reasons; Asympta executes.

1. Use `asympta_port brief` only when local memory/work/routing is needed.
2. For any multi-step or long-horizon mission, create one canonical `work_*` plan, then use `tasklist_wrap` to persist only 1–3 mission focus points, completion criteria, horizon and phase outside chat.
3. Resume with `asympta_port brief` + the mission `work_id`; the derived Tasklist replaces normal work/continuation duplication and surfaces only progress, focus, next actions and blockers. In ChatGPT/Work the same call can render an inline checkbox mission card; full UI rows stay in widget-only metadata rather than model context. Read full `work_get` only when necessary.
4. Update `tasklist_update` only when mission priorities/phase/horizon change. Never duplicate step status there; `work_*` remains canonical.
5. Use `asympta_port call` for execution. Default result is only `{s:0|1,ref}`.
6. Use `asympta_port read detail=compact|full` only when ChatGPT truly needs more evidence.
7. `s=0` is not permission to repeat a mutation. Read the receipt first; durable jobs, traps and exceptional continuation state survive outside chat.
8. Use `asympta_dispatch` only for explicit hidden-tool discovery/compatibility.
9. Hidden capabilities still use native git/gh, xcodebuild, asc and Blender MCP, existing credentials, predictive simulation, durable jobs, audit, reflection and GitHub-backed memory.
10. Verify the original failure/release path before declaring completion. Never expose credentials or replay uncertain uploads.
