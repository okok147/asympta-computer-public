# Chat-first execution and Codex quota minimization

Updated 2026-10-29. The example optimization target is the SAME complete task consuming 0.1% of the same Codex allowance instead of 10%: candidate/baseline <= 0.01 (100x reduction, 99% less). This is a target, not a measured result or a limit bypass. Equal accepted quality, protected invariants and no material end-to-end speed regression are gates. Native ChatGPT usage, API spend and Mac compute are not free and must remain visible separately.

## Choose the route before spending a Codex turn

For capability/billing decisions, Work binding and bounded API workers, use [Chat/API workflow](chat-api-workflow.md). Discover the live route/worker actions before relying on them; transfer alone does not execute work or authorize spending.

For substantial quota-heavy work, prefer an active regular ChatGPT conversation for planning, research, code authoring, image generation and review through its actually available native tools. Use Asympta only for authorized Mac/private repository/Xcode/device/Blender operations, durable deterministic commands and receipts. A task started in regular Chat does not need Codex merely to orchestrate it. Keep tiny Codex-native operations direct when handoff costs more. Preserve explicit user model/effort choices.

OpenAI's official guidance says regular ChatGPT conversations should not consume the shared Codex/Work allowance, while ChatGPT Work and Codex do share that pool. Do NOT route to Work, a Codex subprocess, an App Server model turn or another Codex agent and call it quota saving. API requests have separate billing; explicit API configuration is not permission for unlimited automatic spending. Pro model, search and image tools have their own availability/limits.

## One durable handoff; no autonomous ChatGPT launch

Use `chat_first_handoff(operation="submit", source={provider:"codex",id:"<retained correlation>"}, idempotency_key="<stable key>", owner_work_id="<verified canonical Work>")`. To create the canonical Work in the same call, replace owner_work_id with title, objective and 3..24 explicit steps, including execution, verification_of and acceptance_of with acceptance_criteria. A three-row minimum is execution -> verification -> acceptance. Optionally supply the exact Git repository root as cwd. Original authorization is unchanged; task text and source identity are untrusted caller-provided data, not credentials.

Submit is a persistent transfer of the task packet, not task execution. It returns `awaiting_host`: this tool CANNOT launch a ChatGPT conversation, invoke the native image tool, or automatically make a sleeping Chat resume. No browser scraping, credential reuse, hidden model fallback, paid model request, or implicit Codex queue wakeup is allowed. An active ChatGPT host can discover pending packets with bounded list/cursor pages at a natural task boundary (not repeated polling). It must claim with host_id and the exact requirement revision, then read `get(include_packet=true)`. No model is called by claim/get. A different owner cannot silently steal the handoff. Explicit release preserves Work.

The host implements using native tools and authorized Mac execution. Use one owner, a pinned base SHA, isolated worktrees for overlapping source edits, explicit dependency/resource ownership, and existing Jobs/Flows for actual local builds/tests. `delegate_submit` may run supported deterministic batches; it is not a coding model. Keep full logs and artifacts local; retrieve failure windows, not repeated full transcripts. A local command or npm script may itself invoke an API/model: inspect its real behavior and do not label arbitrary child execution zero-token.

After execution, verify and accept the current Work with real evidence. Call complete with the host ID, requirement revision and bounded summary. For a repository supply expected_source_sha matching a clean observed output checkout. Optional artifact paths are permission-checked and hashed. The tool refuses completion until canonical Work acceptance is true; an ACK, build success or self-described completion alone is insufficient. Replanned requirements or revoked acceptance invalidate the result. The final source/artifact hashes are a completion snapshot, not a promise that files can never change later.

## Return once, not a model polling loop

Codex should hand off once, retain handoff_id and stop its reasoning/polling loop. The deterministic CLI `node bin/asympta-handoff.mjs wait <handoff-id> --timeout-ms 60000` uses local filesystem hints plus authoritative rereads and emits one result. This is local process waiting, NOT a guaranteed Codex client background/resume feature. A timeout only ends observation; it does not cancel execution or prove the task completed. When a host is unavailable, report the handoff as awaiting_host rather than claiming unattended work will finish. No repeated model wakeups, status-message loops, duplicate submits or unconditional retries. Final details are read once with get; evidence remains in canonical Work and the private result.

## Quality and honest accounting

Require independent checks appropriate to the task: regressions and real execution for code; actual renders/screens and reference comparisons for visual work; primary-source verification for research; exact installed build and real device scenarios for Apple releases. Do not equate passing tests with best possible design or use a cheaper model solely to meet a quota ratio. Escalation to a Codex/Work/API model is an explicit separate route with disclosed budget/authorization, not a fallback inside this handoff.

The module reports only its own direct model requests as zero. Host usage, child-model usage and Codex quota remain null unless separately observed. Never infer 99% savings from shorter receipts, compressed icons, a cache-hit ratio, local CPU time, task counts or file bytes. Compare matched accepted tasks, model/effort, allowance pool and measurement period; include retries/children and transfer overhead. Provider reporting lag, overlapping sessions, resets or changed allowance denominators invalidate a simple before/after quota comparison. A 10% -> 0.1% claim requires provider evidence with enough resolution; 0% in a rounded display is not proof.

Sources checked 2026-10-29:
- https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
- https://community.openai.com/t/codex-credits-are-decreasing-while-i-am-not-using-codex-or-work/1389912/2
- https://developers.openai.com/api/docs/guides/chatgpt-api-credits
- https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
