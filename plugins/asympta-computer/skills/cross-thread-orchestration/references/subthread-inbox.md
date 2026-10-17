# SubThread internal result inbox

Use one main conversation as the decision and acceptance owner. Asympta's existing owned worker runtime already persists task state, provider IDs, output, closure proof, and evidence. The inbox projects those records automatically; it does not ask the worker for another message, launch another model, create a second task database, or call Linear.

## Operating cycle

1. Plan and delegate only authorized, bounded tasks using the existing mission/Work contract and resource limits. Preserve applicable model-worker suspension; observing the inbox does not restore execution.
2. Let workers finish and release their owned execution resources. A finished worker need not remain alive until main reads its result.
3. At a natural checkpoint, call `subthread_inbox` for the exact `mission_id`. Read counts and delivery IDs, not full conversations. The default serialized payload budget is 1,600 bytes.
4. If nothing relevant changed, pass the previous `revision` as `known_revision`. Do not add a status-only model loop, heartbeat, schedule, or unconditional per-action check.
5. When ready to handle a delivery, call `subthread_result` with its exact `delivery_id`. Choose `manifest`, `result`, or `evidence`; only requested content enters the main context. The tool checks the owned wrapper's closure proof and matching result bytes.
6. Call `subthread_ack` after consuming notifications to suppress repeated rows. This only records that main has read them. `needs_review`, failure, and blocked counts remain truthful; use `include_acknowledged:true` to revisit them.
7. Independently review and, for engineering, run the existing pinned host verifier. Accept through the existing mission API, integrate only matching artifacts, and synchronize canonical Work when appropriate. A worker's completed turn or an inbox read receipt never means accepted completion.

Use Linear only when a requirement, external collaboration, or explicit reporting need requires it. Keep internal progress and result transport inside Asympta. Do not mirror every worker transition, wait, or read receipt to Linear.

## Minimal calls

```json
{"action":"subthread_inbox","arguments":{"mission_id":"tm-<actual ID>","budget_bytes":1600}}
```

```json
{"action":"subthread_result","arguments":{"mission_id":"tm-<actual ID>","delivery_id":"sd-<returned ID>","section":"manifest"}}
```

```json
{"action":"subthread_ack","arguments":{"mission_id":"tm-<actual ID>","delivery_ids":["sd-<returned ID>"]}}
```

These are action payloads for the existing `asympta_dispatch(op="call")` control plane; use actual returned IDs, not the placeholders.

## State and recovery

- `needs_review` means the host recorded execution completion and main still owes acceptance. `accepted` is a separate canonical state.
- `failed`, `blocked`, and `needs_reconciliation` remain distinct. An unknown provider attempt retains its existing ownership/reconciliation rules; a notification never authorizes replay.
- The inbox revision reflects relevant task outcomes, verification records, mission control state, and read receipts. Progress-only changes do not force repeated context.
- `omitted_count` and `next_offset` identify rows outside the requested budget. Pin subsequent pages with `snapshot_revision`; if stale, restart from a fresh view. An unchanged result with omitted rows does not mean the inbox is empty.
- Read receipts are durable and idempotent. A changed outcome, attempt, error, or verifier record creates a new delivery identity and can reappear unread. A stale batch fails before any receipt is recorded.
- A result request is pinned to a current delivery. If a task changes before expansion, refresh the inbox rather than accidentally reading a different attempt.
- `result` pages use exact UTF-8 byte offsets. Continue from `next_offset_bytes`; do not invent offsets inside a multibyte character.
- The evidence section exposes manifest references and hashes, not full edited file contents. `workspace_reverified:false` explicitly distinguishes archived evidence integrity from fresh artifact verification.

## Boundaries and measurement

This is durable internal delivery and main-initiated reading. It does not inject messages into a busy main conversation, share hidden reasoning, create consumer ChatGPT Web subwindows, or wake a conversation after it has ended. Provider execution availability and authorization remain separate.

The inbox adds no model calls or Linear calls. Its byte budget limits the returned payload, not total model tokens or billing. Measure end-to-end accepted completion time, review/rework, and all main/child token usage before claiming overall speed, quality, or cost improvements. Fewer returned bytes alone are not a measured token reduction.
