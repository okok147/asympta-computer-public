# Native Codex context alignment — 2026-10-17

## Authority and responsibilities

The latest main-chat-only restriction remains active. This reference NEVER enables agents, forks/resumes a provider thread, changes global model/effort/context limits, or overrides host/managed policy. Codex 0.163.0 is the verified upstream release, not proof that every local active session runs it. Asympta's isolated model adapter still requires its separately verified protocol profile; a newer version string alone is not permission to launch.

When model workers are explicitly restored, let native Codex own its native subagent lifecycle. Do not wrap each native agent in another model orchestrator. Asympta owns deterministic I/O, canonical Work/Flow evidence, bounded source handoffs and resource-safe verification. No duplicate worker pools or per-session limit multiplication. Until restored, use the same context discipline with deterministic tools/Jobs/Flows only.

## Context is not capability

Upstream 0.163.0 preserves subagent capabilities independently of `fork_turns: none/all`. Fresh history is not reduced permission. Task scope, resource claims, sandbox and managed policy still apply. Native subagents inherit model/reasoning unless configured otherwise; check actual schemas, not remembered flags.

Use a fresh task capsule for self-contained authorized exploration/review. Fork full history only for a continuation that genuinely needs it. `preserve_fork_prefix` is opt-in for full forks, not a token-reduction guarantee. `subagent_default_context_limits` concerns native subagents' model defaults, not arbitrary limits for Asympta-owned root threads. Do not blindly write these flags into every worker config. Preserve required sources, images, instructions and uncertainty.

## Bounded evidence protocol

1. Keep the stable policy/tool prefix and task identity. Carry goal, scope, permissions, source SHA, dependencies, acceptance and missing evidence, not whole sibling conversations.
2. Use bit/compact first. For bounded compact/full reads set `budget_chars: 1200` (UTF-8 bytes of the structured view). Explicit budgets now apply to both modes. Omitted budget preserves legacy full output.
3. On `payload_omitted`, retain ref and `receipt_digest`. Omission is not empty data or PASS. Never rerun a mutation to recover text. Call `receipt_read` with `source: payload_json`, `pointer: /structuredContent/sessions/0`, `expected_digest: <returned digest>` and finite `budget_bytes`. RFC 6901 pointers select exact retained JSON; empty selects raw payload, `/content` preserves non-text and non-mirror blocks. Missing, null and false are distinct.
4. Follow `next_start_line` on the SAME source/digest. `single_line_exceeds_budget` requires a narrower selection or a larger bounded budget, not identical retries. JSON completeness describes selected retained JSON, never uncaptured original evidence.
5. Independent read-only tools may run in parallel through supported native tools or the audited deterministic read batch. Mixed mutation-capable control ports do not become read-only because the caller labels them so. Shared writes, devices and releases remain serialized.
6. Join all required results; independently accept source-pinned evidence. A model summary, green receipt and unrelated passing test do not prove task acceptance. Reconcile interrupted/unknown effects before replay.

## Metrics

Measure verified end-to-end wall time including joins, checks and rework; acceptance outcomes; and actual parent/child/compaction/retry counters with coverage. Missing counters remain unknown. Raw/cached input are separate. Wire bytes, JSON speed and cache discounts are not model-token or billing savings. A 10x result must name workload and scope. Verify the compatible batch once; recheck changed scope, failures or required gates.

## Primary sources

- https://github.com/openai/codex/releases/tag/rust-v0.163.0 — read-only parallel tools, steering, daemon warnings; released 2026-10-15.
- https://developers.openai.com/codex/subagents/ — context isolation, write conflicts, model/reasoning inheritance.
- https://github.com/openai/codex/pull/52241 — capabilities independent of forked history.
- https://github.com/openai/codex/pull/52535 — opt-in full-fork prefix preservation.
- https://github.com/openai/codex/pull/52659 — opt-in context defaults, listed in 0.163 release; not a claim of local activation.
