---
name: plan-first-orchestration
description: Track every request with multiple substantive tasks in one visible Work list, then execute, verify and accept each requested outcome with current evidence and bounded resources. Use for multi-task delivery, delegated work and resuming an existing plan.
---

# Plan-first orchestration

Use the connected tool schema and the [task verification and acceptance contract](../asympta-computer/references/task-verification-acceptance.md). Preserve the exact deliverable and existing authority. Keep a single trivial action direct; keep a short multi-task plan short.

1. **Make the scope visible.** List every requested outcome, protected constraint, observable acceptance criterion, owner, dependency and finite budget. Reuse the canonical `work_id`; keep the native plan aligned with that Work rather than creating a competing backlog.
2. **Separate the completion stages.** Create new multi-task Work with `completion_contract:"verified"` and a stable idempotency key. Link verification rows directly to execution through `verification_of` and matching dependencies. Link separate acceptance rows to verification through `acceptance_of`, matching dependencies and explicit `acceptance_criteria`.
3. **Execute ready work.** After starting/resetting each step, capture its revision before that attempt's execution, verification or acceptance review; retain it with the resulting evidence. Use `work_schedule_plan` when available at meaningful boundaries. Parallelize independent work with disjoint resources; serialize shared writes, devices and releases. Delegate only with existing authorization and explicit scope. Continue owned ready work until accepted or concretely blocked.
4. **Keep history and revisions.** Update the visible list after real progress, failure or a requirement change. Retain failed attempts, blocked and skipped rows, evidence and uncertain effects. Read authoritative state before retrying a mutation. Replan explicitly and reverify affected results after source, input or attempt changes.
5. **Verify, then accept.** Inspect the artifact and current source/input evidence. Submit the revision retained for that actual attempt or review. A stale token requires current execution or verification; never refresh a token merely to resubmit old evidence. Check every original requirement, quality bar and destination separately from technical success. Require `work.acceptance.accepted:true`; keep legacy completion and unsupported contracts explicitly unverified. Objective acceptance adds no permission prompt.
6. **Deliver the evidence.** Report the exact artifact/release, completed and remaining scope, verification, acceptance and blockers. Report Speed, Accuracy / Quality and Usage Saving across all attempts. Preserve **Token saving = Quality**; prefer lower measured usage among equally accepted outcomes, then end-to-end speed and reliability. Treat 10× as a target until measured comparably.

Do not add status-only polling, repeat passing checks without a relevant change, or claim background continuation without an actual executor. Follow the reference for live-schema fallback, evidence freshness and measurement definitions.
