# Developer integrations — v0.12.0

## Execution invariant

Asympta Computer is CLI-first. Developer actions execute directly on the Mac: `xcodebuild` for Xcode, `asc` for App Store Connect/TestFlight, `git`/`gh` for GitHub, and `uvx mcp-for-blender==2.0.4` for Blender MCP. ChatGPT Work and Codex are not execution dependencies. The `work_*` tools are Asympta's own durable task state only.

## What is implemented

| Capability | Tools | Execution |
|---|---|---|
| Ultra ChatGPT-first control | `asympta_port`, `asympta_dispatch` | Default client sees only two schemas. `brief` selects bounded context/routes; `call` executes hidden capabilities and stores full results locally; `read` defaults to a 0/1 receipt and can expand only on demand. `ASYMPTA_TOOL_EXPOSURE=full` restores direct typed-tool advertisement. |
| Mission / Tasklist wrapper | `tasklist_wrap`, `tasklist_get`, `tasklist_update`, `tasklist_list`, `tasklist_stats` | External long-horizon wrapper over canonical `work_*`. Stores only focus/done/horizon/phase; derives percent/next/blockers. Hidden behind Ultra control plane. |
| Xcode inspection and compilation | `xcode_info`, `xcode_build` | Schemes, build/test/archive, explicit destination and artifact paths. Tests disable parallel simulator execution. |
| Xcode artifact export | `xcode_export` | `xcodebuild -exportArchive` plus actual artifact existence checks. |
| GitHub CLI | `github_cli`, `github_context`, existing `git_*` / `github_api_*` | Native `gh` / Git with existing login. `github_context` returns branch, HEAD, dirty state, repository metadata and current PR/check context in one call. |
| Capability discovery | `capability_discover` | Discovers current MCP tools, native CLIs and routing hints; optional external GitHub/Blender capability probes. |
| Background visual control | `background_window_info`, `screenshot_background_window`, `background_inspect_ui`, `background_click_ui_element`, `background_click`, `background_set_ui_value` | Target-window capture and Accessibility actions without intentionally activating the target or injecting the global mouse. Visual-coordinate click maps into the target AX tree. Unsupported non-AX surfaces do not silently fall back to foreground mouse control. |
| Offscreen drawing | `background_draw_vector` | Renders SVG strokes offscreen with optional RDP simplification and Catmull-Rom smoothing; does not use the mouse or require target-app focus. |
| Predictive execution + continuation | `simulation_status`, `trap_list`, `continuation_get`, `blackboard_note`, `predictive_stats` | Every non-control action gets a durable simulated action/result map before execution. Matching results stay on the fast path; deviations generate traps and a future replan. Continuation capsules externalize chat context so reconnects resume instead of replaying side effects. |
| Portable GitHub memory | `memory_status`, `memory_sync`, `memory_profile_get`, `memory_profile_update` | Private GitHub repo is the long-term memory source of truth; local state is a disposable cache. Append-only sanitized records sync playbooks/reflections/traps/continuations/operator preferences and selected blackboard summaries across machines. |
| Reflection + playbooks | `reflection_*`, `playbook_*`, `work_create reuse_policy` | Terminal work produces evidence-backed completion/quality/time/waste analysis. Similar successful tasks confirm invariants, isolate variants, retain the fastest successful route, and attach a lightweight reuse plan. `playbook_materialize` emits the last successful completion-call templates and remains blocked until current variants are overridden or explicitly revalidated. |
| Multi-agent teamwork | `team_create`, `team_get`, `team_list`, `team_heartbeat`, `team_allocate`, `team_report` | Capability-aware allocation of dependency-ready `work_*` steps with concurrency and heartbeat controls; evidence flows back into the canonical work plan. |
| Public Internet | `internet_fetch` | Bounded HTTP(S) GET/HEAD with DNS/private-network blocking, redirect revalidation, byte/time limits and safe retries. |
| App Store Connect CLI | `asc_cli`, `testflight_builds`, `testflight_groups`, `testflight_publish` | Native `asc`, existing profile/Keychain, separate stdout JSON and stderr diagnostics. |
| Official GitHub MCP | `github_mcp_tools`, `github_mcp_call` | MCP v2 client protocol connection over HTTP or configured native stdio. Not a REST-wrapper alias. |
| Blender MCP CLI | `blender_mcp_status`, `blender_mcp_tools`, `blender_mcp_call` | MCP v2 client plus direct `uvx` stdio launch of `mcp-for-blender==2.0.4`, targeting the local Blender addon socket. |
| Long operations | `job_get`, `job_logs`, `job_cancel`, `job_retry` | Detached worker, private durable records, heartbeat and bounded output. |
| Resumable iOS release | `release_prepare`, `release_run`, `release_get` | Clean source commit, archive/export checkpoints, IPA SHA-256 and uncertain-upload protection. |

Short/read-oriented integration calls execute inline in `mode: "auto"`; known long operations such as Xcode export, App Store/TestFlight work, remote MCP calls and release stages auto-promote to durable jobs. `run_command` in `auto` also promotes when its explicit timeout crosses the durable threshold (30 seconds by default). The same policy applies through stable `asympta_dispatch call`, so plugin metadata compatibility does not reintroduce request-timeout risk. Before the real action starts, the predictive boundary persists an expected action/result map. If the result deviates, deterministic exact repeats are blocked and a new path must be simulated from actual state. `mode: "background"` explicitly requests durable execution; `mode: "wait"` forces inline execution where appropriate. Poll `job_get` using its interval and read `job_logs` for progress. A quiet poll does not mean a command should be restarted. Explicit mutation retries are not silently performed. If a chat/client loses context, recover durable IDs and read `continuation_get`; do not replay a consequential action merely because the UI stalled.

## Native credentials and limits

The installed service runs as the logged-in Mac user and declares the native CLI PATH and HOME. Git/gh/asc reuse existing login state. Blender MCP uses a local socket and does not require a Codex or ChatGPT login. The public tool schemas do not accept passwords or raw credential material. If native authentication expires or Apple requires an approval, the tool reports the failure; it does not bypass authentication or keep sessions alive artificially.

The GitHub MCP bridge internally obtains the existing `gh` credential, keeps it in memory, and delegates it only to the fixed official GitHub MCP HTTPS origin or the locally configured official native binary. It is not returned in MCP results, written to job arguments, or sent in process argv. Native stdio inherits only a small environment plus the GitHub credential, not unrelated Apple credentials. Provider policies still determine whether a particular account may use that server.

Set `ASYMPTA_GITHUB_MCP_TRANSPORT=http` for the default official remote endpoint. For native stdio, install `github-mcp-server`, set transport to `stdio`, and optionally set `ASYMPTA_GITHUB_MCP_BINARY` to its absolute path. The server does not download or run arbitrary remote executables supplied as tool arguments.

Raw `run_command` remains enabled as requested. This is a trusted personal-Mac command environment, **not an OS sandbox**. A Python/Node/CLI process can access resources allowed by the operating-system account. Filesystem-root checks apply to focused path arguments and working directories; they do not sandbox an arbitrary child program. Secret masking covers common formats but is not a comprehensive data-loss-prevention system.

## Tool examples

Arguments below are JSON objects passed to the named MCP tool, not shell strings. Replace the example paths and identifiers with the actual project.

`github_cli`:

```json
{"args":["repo","view","okok147/asympta-computer-mcp","--json","nameWithOwner,defaultBranchRef"],"cwd":"~/Developer/asympta-computer-mcp"}
```

`github_mcp_tools` first discovers current names and schemas:

```json
{"query":"get_file_contents","limit":5}
```

`github_mcp_call` then uses the discovered tool:

```json
{"name":"get_file_contents","arguments":{"owner":"okok147","repo":"asympta-computer-mcp","path":"CHECKLIST.md"}}
```

`asc_cli` is a read-only provider operation in this example:

```json
{"args":["apps","list","--limit","10","--output","json"],"cwd":"~/Developer/asympta-computer-mcp"}
```

`xcode_build`:

```json
{"container":"~/Developer/App/App.xcodeproj","scheme":"App","action":"archive","configuration":"Release","destination":"generic/platform=iOS","archive_path":"~/Developer/AppArtifacts/build-001.xcarchive","derived_data_path":"~/Developer/AppDerivedData","jobs":1}
```

`xcode_export`:

```json
{"archive_path":"~/Developer/AppArtifacts/build-001.xcarchive","export_options":"~/Developer/App/ExportOptions.plist","export_path":"~/Developer/AppArtifacts/build-001-export"}
```

Provisioning changes are not enabled by default. Set `allow_provisioning_updates: true` only when the project task authorizes them and the Mac has suitable signing access.

`blender_mcp_tools` discovers the live Blender MCP schema directly:

```json
{"query":"scene","limit":20}
```

Then call the discovered tool without Codex:

```json
{"name":"get_scene_info","arguments":{"user_prompt":"Read the current scene only; do not modify it."}}
```

The local addon must be running. Default connection is `127.0.0.1:9876`; configure `ASYMPTA_BLENDER_HOST`, `ASYMPTA_BLENDER_PORT`, and `ASYMPTA_BLENDER_MCP_SAFE_MODE` if needed.

## Resumable iOS release

Create a plan with `release_prepare`: repo, project/workspace, scheme, fresh archive/export paths, export-options plist, app ID and group. It requires a clean Git tree and records the source commit plus export-options hash.

`release_run` with `publish: false` (the default) runs archive/export and stops. It verifies archive metadata at its checkpoint and the entire IPA hash before publication. It does not hash every archive resource, so external modification of an archive should trigger a new release plan.

Only `publish: true` invokes `asc publish testflight`. JSON booleans are enforced: a string such as `"false"` is rejected before a job is queued. The tool never implicitly submits an app for App Store review, changes pricing, or notifies testers.

Before upload/distribution starts, the persisted state crosses an **uncertain outcome** boundary. A timeout may mean Apple accepted the upload but the response was lost. A subsequent retry therefore does not re-upload blindly. Inspect App Store Connect; then resume with an `existing_build_id` to distribute the confirmed build. If no accepted build can be identified, reconcile that state before preparing a new release.

The current named pipeline is for iOS IPA files. Generic `xcode_export` can also return a macOS app or package, but macOS TestFlight is not claimed as a fully implemented named release pipeline.

## Verification

Run the isolated suite:

```sh
npm ci
npm run check
npm test
```

The tests use provider fixtures where writes would otherwise affect accounts. They cover argument preservation, auth-output restrictions, malformed inputs, output bounds, token-split masking, SDK stdio transport, artifact validation, work/job failure propagation, release checkpoints, tampering, concurrent runners, uncertain uploads, and HTTP Origin/SDK compatibility. Fixture tests are not evidence of a real App Store upload.

A live opt-in probe is supplied as `bin/verify-live.mjs`. It only performs GitHub/ASC reads and local Xcode compilation. It never publishes or creates provider resources. Set up an independent macOS smoke fixture without another simulator:

```sh
mkdir -p /private/tmp/AsymptaComputerLiveSmoke
cp -R test/fixtures/xcode-smoke/. /private/tmp/AsymptaComputerLiveSmoke/
(cd /private/tmp/AsymptaComputerLiveSmoke && xcodegen generate)
./bin/install-launch-agent.sh
node bin/verify-live.mjs /private/tmp/AsymptaComputerLiveSmoke
```

See `verification/2026-10-07-live.json` for the live results and `verification/2026-10-07-live-before-json-fix.json` for the reproduced stderr/JSON failure. The latter is deliberately retained as regression evidence, not the current result. The smoke app uses local ad-hoc macOS signing, not Apple distribution signing.

## Connection and operational boundaries

The local endpoint is `http://127.0.0.1:43110/mcp`. Local CLI integration does **not** establish a native ChatGPT custom-MCP connection. The current verification path is ChatGPT → authorized terminal bridge → local MCP → native CLI / GitHub MCP. Secure MCP Tunnel and direct ChatGPT connector registration remain separate account-level setup and verification gates.

The listener checks Host and Origin, binds to loopback by default, and requires a bearer token for non-loopback configuration. Loopback is not authentication against other local users/processes; add a local token in multi-user environments. Do not expose the server publicly without authenticated transport. Existing ChatGPT confirmation policy remains in effect for consequential actions.

Job capture retains a bounded tail per stdout/stderr stream and up to 16 MiB of progress logs per job. Records use private file permissions. Job cancellation signals the worker process group; it is not a guarantee against deliberately uncooperative child processes. Process sessions in auto mode are not restart-durable; use durable jobs for restart survival. A sleeping/offline Mac cannot execute new commands.

## Primary references

- GitHub MCP server: https://github.com/github/github-mcp-server
- Official MCP TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk
- MCP HTTP transport: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
- GitHub CLI authentication: https://cli.github.com/manual/gh_auth_status
- App Store Connect CLI: https://github.com/rorkai/App-Store-Connect-CLI
- Apple Xcode CLI technical note: https://developer.apple.com/library/archive/technotes/tn2339/_index.html

The installed CLI help was also checked directly for version-specific flags.
