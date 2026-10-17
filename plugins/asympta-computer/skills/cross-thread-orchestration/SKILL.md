---
name: cross-thread-orchestration
description: Read authorized Asympta SubThread outcomes through a compact internal inbox; main checks when useful and expands only needed results, preserving worker authorization and independent acceptance.
---

# SubThread internal delivery

Use one main conversation as the decision and acceptance owner. Observe only authorized Asympta missions using actual returned mission IDs. Preserve any existing user or host suspension of model workers; inbox access does not restore execution or grant permission to launch, resume, or retry a worker.

Let the owned runtime retain worker completion and full results automatically. Workers need no separate success message or extra model turn, and may close before main reads the result. At a natural checkpoint, main reads `subthread_inbox`, reuses its revision, and expands only needed `subthread_result` sections. Do not add a status-only model loop or replay a worker transcript into main.

Record consumed deliveries with `subthread_ack` to suppress duplicate notifications. This is a read receipt, never task acceptance. Review the exact result and source independently, use the existing engineering verifier where required, and accept through the existing mission contract. Pending-review and failure counts remain visible after acknowledgement.

Use Linear only when requirements, external coordination, or an explicit reporting need calls for it. Keep ordinary internal status and result delivery inside Asympta.

Load the [inbox reference](references/subthread-inbox.md) for exact action shapes, budgets, pagination, recovery, evidence boundaries, and measurement limits. Do not claim arbitrary ChatGPT window control, automatic wake-up of a completed conversation, or unmeasured token savings.
