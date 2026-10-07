---
name: asympta-computer
description: Use Asympta Computer for durable Mac execution, Xcode, GitHub, App Store Connect/TestFlight, crash recovery, audit and long tasks.
---

# Asympta Computer

ChatGPT reasons; Asympta executes. Tasklist UI and context injection are disabled by default.

1. Request asympta_port brief only when local memory, durable work state or routing is needed.
2. Keep one canonical work_* plan for a multi-step task. Do not create Tasklist wrappers.
3. Execute through asympta_port call. Use detail=bit for mutations/status, and detail=compact for bounded stdout in the same response. Expand to full only for complete evidence.
4. Treat s=1 as actual success. A running session is pending; a nonzero exit is an error. Read pending receipts rather than rerunning commands.
5. Use the diagnostic in an invalid-arguments receipt. Inspect its full stored schema only if needed. Never blindly repeat a deterministic failure.
6. Use run_command with a bare executable name, argument array and allowed cwd. A timeout is an allowance; mode=background explicitly creates a durable job. Auto commands start inline and become pending sessions when they exceed the inline budget.
7. Use asympta_dispatch for capability discovery/compatibility.
8. Reuse native git/gh, xcodebuild, asc and Blender MCP with existing credentials.
9. Verify the original failure or release path before declaring completion. Inspect external state before retrying an uncertain upload or publication.
