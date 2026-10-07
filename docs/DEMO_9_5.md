# Asympta Computer v0.7.0 — 9.5/10 Target — 2–3 minute demo script

## 0:00–0:20 — One endpoint, two clients

Show the same Asympta Computer MCP URL in ChatGPT and Claude Code configuration. Run the stable dispatch manifest and show the server version/schema hash.

Narration: “The model is replaceable. The computer runtime and durable work state are not.”

## 0:20–0:45 — Disconnect-safe long task

Start a durable command or build. Show its job ID and worker PID. Close/restart the MCP daemon, reconnect, then read the same job and show that the detached worker continues.

Show the >1-hour canary evidence when available.

## 0:45–1:10 — Parallel DAG + crash recovery

Create a flow with two independent nodes and one join node. Show the two nodes starting together. Kill the flow worker during an idempotent node, resume and show completion. Repeat with a non-idempotent node and show that it becomes `uncertain` instead of being replayed.

## 1:10–1:30 — iPad steering

Open the LAN steering URL on iPad Safari, enter the one-time pairing code, then send pause/resume or a steer note. Show the signal appearing in the Mac flow/event history.

## 1:30–1:50 — Security + audit

Run `repo_read` capability against the repository, then demonstrate that reading personal Home or writing a file is denied. Run `event_verify` and show a valid hash chain.

## 1:50–2:20 — Real Apple release

Show the Asympta Paperie flow:

GitHub source → Xcode archive → IPA export → App Store Connect upload → TestFlight VALID / IN_BETA_TESTING.

Show timings from the three build rounds and the selected optimized configuration.

## 2:20–2:40 — Reflection

Open the generated reflection/playbook. Highlight invariant workflow, current variants, measured avoidable work and the next-run fast path.

## 2:40–3:00 — Public evidence

Open the public architecture repository and benchmark JSON. End on the acceptance matrix rather than a marketing claim.
