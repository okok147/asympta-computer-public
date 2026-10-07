# Asympta Computer v0.15: verified-frontier orchestration

## Meaning and scope

This implementation interprets the requested “極限曲面” as the boundary of feasible engineering trade-offs: quality, verified completion, latency, response size and declared memory. It is not a claim to implement a differential-geometric minimal-surface theorem. A concrete surface theorem or proof artifact would require a separate mapping and validation.

The transferable Navier–Stokes lesson is the research procedure: explore genuinely different variants, retain measured useful results, concentrate effort after a signal, synthesize intermediate results, and independently verify before promotion. The OpenAI September 8, 2026 account describes variant groups, resource reallocation following Euler progress, cross-group consolidation and subsequent Lean formalization. This project does not run that model, replicate that scale, solve a fluid PDE, or obtain a mathematical guarantee from the NS result.

Primary references, checked 2026-10-07:
- https://openai.com/index/navier-stokes-solution/ — reported research process and result.
- https://github.com/openai/math — proof artifacts, mixed verification states and versioned corrections. Not every manuscript is formalized or independently certified.
- https://developer.apple.com/documentation/foundation/filemanager/trashitem(at:resultingitemurl:) — native reversible Trash operation.

## A finite evidence-constrained frontier

For each candidate x, measurements are latency T(x), response/model-token estimate K(x), declared memory M(x), success count s and trial count n, workload context and an evidence reference. Token observations must come from an actual meter or be explicitly labeled estimates by the caller. Response bytes are not model tokens.

The feasible set is:

    F = {x: context matches; verification reported; evidence present;
            n >= n_min; L_Wilson(s,n) >= q_min;
            T(x) <= T_max; K(x) <= K_max; M(x) <= M_max}

The policy removes dominated candidates from F. Candidate a dominates b only when it is no worse on every coordinate and strictly better on at least one. Quality is maximized; time, tokens and memory are minimized. Selection among nondominated candidates uses an explicit objective, not an opaque weighted total that can trade away correctness.

`optimization_frontier` is a read-only hidden action. It returns the finite frontier, rejected candidates and reasons, and either a recommendation for independent revalidation or no recommendation. It rejects invalid numerical data, duplicate IDs, mismatched contexts, insufficient samples and over-budget candidates.

The Wilson lower bound assumes independent, comparable Bernoulli trials. Correlated tests, selected workloads and unreliable caller inputs invalidate a production-reliability interpretation. An `evidence_ref` is provenance supplied by the caller, not a checked proof certificate. This policy does not fetch or validate that reference. The result is a finite empirical frontier, not proof of global optimality.

## Agent and verification contract

The host remains the reasoning/planning layer. Asympta executes authorized tools and records evidence. No nested model call or paid-agent fan-out is introduced.

    Objective + constraints
          -> small bounded candidate set
          -> isolated execution branches
          -> evidence extraction / frontier assessment
          -> independent verifier
          -> centralized integration and delivery gate

The durable work graph remains canonical; there is no second competing task-state system. Agent `required_capabilities` are hard allocation constraints. A step with `verification_of` must depend directly on the generated step and be allocated to a different agent identity with verification capability. Passing an explicit verification step requires an evidence string. Unsupported earlier steps no longer prevent later compatible steps from being allocated.

These are logical role checks, not authentication or formal proof. A caller can lie about an identity or an evidence string. Production promotion must still inspect the actual artifact and original failure path. No Lean proof of Asympta is claimed. The separate scheduling checker and regression/property tests are the engineering verification used here.

## Event-driven, resource-aware DAG execution

The old batch barrier waited for the slowest sibling before admitting any next work. The new executor fills a newly free slot immediately. Dependency order and critical-path priority remain; a separate `verifySchedule` gate checks the proposed admission before execution.

Safety and resource gates check node identity, duplicates, completed dependencies, parallel capacity, resource overlap and declared memory. Resource inference canonicalizes symlinks and detects parent/child path overlap. Reads can overlap; conflicting writes cannot. Generic commands are conservatively exclusive in their working directory unless explicitly declared `parallel_safe`. This flag changes scheduling only: it never grants permission, weakens command validation, or authorizes retries. Named resource locks remain additive. Apple build/release work shares a dedicated resource key.

A PID-aware lease registry coordinates conflicts across flow workers sharing the same state directory. A lease is not reclaimed merely because it is old. It remains while its owner or detached process group is alive. Ordinary external CLI/UI actions not using the flow scheduler do not participate in this registry; it is not an OS-wide lock or sandbox. Declared memory admission is not measured resident-memory enforcement.

Concurrent start/resume requests share the flow lease and retain one live worker. After interruption, idempotent work can be recovered; uncertain side effects stay fenced. Failure propagates through all descendant levels rather than leaving an unreachable pending node polling forever. Only bounded idempotent transient retries are eligible; deterministic failures are not blindly replayed.

## Completion is an observation, not an optimistic receipt

A background handle is not completion. The worker waits for terminal process/job evidence. A late nonzero exit fails the node and prevents dependent work from running. Polling grows from 80 ms to a bounded 750 ms when output is unchanged, and resets when observable output changes.

Three meanings remain separate:
- `process_write` success means stdin was accepted, not that the receiving program executed it correctly.
- `process_stop` success means the requested process is observed stopped. Its raw signal and exit code remain available.
- `run_command` success requires actual successful terminal execution.

Stdin can execute code through an interpreter. Its metadata therefore remains destructive/open-world. Labeling it harmless would misrepresent its effects and does not solve a host-side safety rejection. The host's authorization layer remains in control; an upstream rejection is not bypassed by renaming the operation.

## Observable work with bounded context

Receipts retain action, optional work step, process/session and bounded latest output line. Compact source reads now include actual source line range and a bounded content window in the same response. Truncation remains explicit. Pending receipts include a recommended polling interval. Full evidence is still separately inspectable.

Unchanged-process deduplication compares a complete sanitized payload digest. It does not assume that equal first/last log lines imply an equal middle. Atomic receipt temporary names use random IDs to avoid same-millisecond concurrent collisions. Secret masking remains best-effort rather than a complete data-loss-prevention system.

Two exposed tools remain the default. New `command_policy` and `optimization_frontier` capabilities stay behind the compact port. Tasklist UI remains disabled. Returning progress fields does not guarantee that the ChatGPT client will render them as its native activity title or continuously stream them without a tool call.

## Native Trash and rejected approaches

The prior check-then-rename collision policy could race. A JXA bridge was experimentally rejected after it moved a test file and then crashed; disappearance of a source was not accepted as success. The selected helper uses typed Swift/Foundation and reports the resulting Trash destination. Actual moves are serialized across processes sharing the state directory to preserve simultaneous same-name files. There is no permanent-delete fallback and no automatic replay after ambiguous failure.

The helper is compiled once into the private state directory and keyed by its source hash, architecture and OS release. Cold compilation is a separate setup cost; subsequent moves reuse the executable. A failed or ambiguous move explicitly requires inspecting both source and Trash before retrying.

## Validation and measurement protocol

`test/frontier-orchestration.test.mjs` includes 1,000 deterministic randomized DAG-state cases plus real child-process tests for early refill, transitive failure, delayed exit failure, concurrent start, cross-flow conflicts, oversized declared memory, middle-log changes, source traces, independent verifier allocation and concurrent same-name Trash.

The full existing suite remains enabled, including release safety, credential masking, recovery, event integrity and other integrations. `bin/test.mjs` reduces concurrent suites when normalized host load is high; it never skips tests or lowers assertions. The HTTP test fixture uses an isolated per-run port, captures bounded diagnostics and distinguishes startup failure from test assertion failure.

`bin/benchmark-frontier.mjs` runs matched baseline/candidate ABBA blocks sequentially. It records complete source hashes, sample distributions, verified outputs, operation counts and response bytes. It does not run concurrently with the regression suite. The uneven-DAG benchmark uses real detached workers; read and command benchmarks measure the in-process verified port path. None includes model thinking time, ChatGPT transport latency or platform-billed tokens.

Measured results and final validation status belong in the dated files under `docs/verification/`. A failed intermediate experiment is not a final pass. Promotion requires the complete final suite and an independent original-path check against the exact source snapshot.
