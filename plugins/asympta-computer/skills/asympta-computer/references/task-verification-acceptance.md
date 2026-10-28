# Task list, verification, acceptance and three metrics

## One visible list for every multi-task request

Keep one visible list for every request with multiple substantive tasks, including short requests. Reuse the canonical Work and keep the native plan aligned with it. Track meaningful outcomes rather than every click; keep a single trivial action direct. Retain completed work, failed attempts, blocked and skipped rows. Update the list after real progress, failure, changed requirements or newly discovered work.

For new multi-task Work, use `completion_contract:"verified"` and a caller-generated `idempotency_key`. Preserve the key across uncertain acknowledgements. Record each requested output, protected constraints, owner, dependencies, resource ownership, observable acceptance criteria and finite budgets before execution. Continue owned ready work until the scope is accepted or a concrete blocker remains.

Use the live tool schema. When the connected server lacks the strict contract, keep the visible list and evidence, identify the missing capability, and mark strict acceptance unverified. Do not invent fields, silently downgrade acceptance or claim a server upgrade occurred. Preserve active legacy Work and its history rather than changing its contract mid-execution.

## Link execution, verification and acceptance

Use existing step statuses from the schema. Keep these three phases in separate rows:

| Phase | Link | Required evidence |
| --- | --- | --- |
| Execution | Original task dependencies | The actual operation, artifact and source/input identity. |
| Verification | `verification_of` references direct execution dependencies. | Relevant tests or readback demonstrating the result works on that exact version. |
| Acceptance / 驗收 | `acceptance_of` references direct verification dependencies; `acceptance_criteria` states observable outcomes. | Evidence that all requested outputs, quality requirements and destinations are satisfied. |

For example, adapt these rows to the task and add the caller-generated idempotency key:

```json
{
  "title": "Deliver the implementation and usage guide",
  "completion_contract": "verified",
  "steps": [
    {"id":"implement","title":"Implement the requested behavior"},
    {"id":"guide","title":"Update the usage guide"},
    {"id":"verify","title":"Check behavior and guide against exact source","depends_on":["implement","guide"],"verification_of":["implement","guide"]},
    {"id":"accept","title":"Accept both requested outputs","depends_on":["verify"],"acceptance_of":["verify"],"acceptance_criteria":["All requested behavior passes the agreed real-use scenarios on the recorded source version","The guide describes the delivered behavior and is accessible at the requested destination"]}
  ]
}
```

Use `work_schedule_plan` when available at meaningful boundaries; its schedule grants no new authority. Parallelize independent work with disjoint resources. Serialize shared writes, device control and release. Do not claim background continuation without an actual executor.

## Keep evidence current and judge what it proves

After starting or resetting a step, capture its requirement revision **before** that attempt's actual execution or check. Retain that revision with the resulting evidence and submit it as `expected_requirement_revision` for the corresponding `passed` update. A fresh owner verification or acceptance review pins its revision before that actual inspection. Bind evidence to the source, build and inputs checked.

If the retained token is stale, perform current execution or verification as needed under existing authority. Never read a new revision merely to resubmit old evidence. Inspect uncertain mutation effects before deciding whether another execution is needed. Reopen or replan affected work when requirements, inputs or outcomes change, and verify dependent results again. Preserve prior attempts and original evidence.

A successful tool call, green receipt, screenshot, model self-report or nonempty evidence string alone does not prove acceptance. Runtime checks establish evidence presence, dependency consistency and freshness; the owner still judges whether that evidence proves the criteria. Record independent source review for material changes. A valid artifact in the wrong destination can pass technical verification and fail acceptance.

Read `work.acceptance` before claiming completion. Require `accepted:true` for strict Work. Legacy `completed` status describes execution history and remains unverified. Missing proof, stale dependencies or required skipped work prevent strict completion. Unknown, NOT RUN and skipped are not PASS. Record authorized scope changes explicitly; do not remove difficult criteria to obtain a pass.

Objective acceptance uses existing authority and adds no confirmation gate. Ask only for a material unresolved requirement, missing authority or a subjective choice that needs the user. Run the smallest sufficient acceptance set; repeat it only for a relevant change, actual failure, changed external state or mandatory gate. Retain original logs instead of rerunning to retrieve output. Preserve release, security, signing and physical-device gates.

## Report exactly three metrics

Preserve **Token saving = Quality** and all mandatory acceptance criteria. Among equally accepted outcomes prefer lower measured total usage, then end-to-end speed and reliability. Report the following metrics separately; do not invent a composite improvement score.

| Metric | Measure | Interpretation |
| --- | --- | --- |
| Speed | Request-to-accepted-outcome elapsed time, including planning, queueing, execution, verification, retries, repair and integration. | Keep failures and timeouts in comparable cohorts. Report tool latency separately; it is not whole-task speed. |
| Accuracy / Quality | First-pass acceptance rate across all attempted cases, plus final criterion coverage, defects and rework. | Fix the criteria and denominator before comparison. A repaired result can pass final acceptance while remaining a first-pass failure. Report sample size and evidence. |
| Usage Saving | All attributable metered tokens and costs across all attempts, divided by accepted outcomes. Include parent/child agents, retries, compaction, tools/providers and acceptance overhead. | Deduplicate cumulative and cached counters; report tokens and cost separately. Missing coverage is unknown. No accepted outcomes makes usage per accepted outcome undefined, never zero. |

Use existing timestamps, retained receipts and available usage checkpoints. Count all attempts and agents. Bytes, smaller receipts, cache hits and fewer calls are proxies, not measured token savings. Native ChatGPT usage may be unavailable; disclose coverage. Do not create needless agents, polling or another telemetry store to measure this workflow.

Keep **10× a target** until a matched baseline/candidate comparison at equivalent accepted scope proves the specific metric:

- **Speed:** baseline elapsed time divided by candidate elapsed time is at least 10.
- **Accuracy / Quality:** first-pass failure rate falls by at least tenfold; do not multiply a bounded success percentage. Zero observed failures does not establish a zero underlying failure rate or infinite improvement.
- **Usage Saving:** candidate measured tokens per accepted outcome are at most one tenth of baseline, meaning at least 90% fewer tokens. Cost reductions require separate cost evidence.

Report the fixed workload, exact versions, sample size, failures, timing distribution and uncertainty. Without comparable baselines or adequate telemetry, report unknowns and the remaining measurement work.

## Final report

State the delivered outcome and exact source/release, completed and remaining task counts, verification results, acceptance with evidence, the three metrics or explicit unknowns, and concrete blockers. Distinguish implemented, tested, saved, deployed and independently accepted.
