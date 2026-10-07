# Asympta Computer v0.11.0 — 9.5/10 Target — 2–3 minute demo script

## 0:00–0:18 — One runtime, replaceable client

Show ChatGPT connected to Asympta Computer and run the stable dispatch manifest/discovery. Show v0.11.0, the schema hash, and live tool discovery.

Narration: “The model/client is replaceable. Durable computer state is not.”

## 0:18–0:42 — >1h work + disconnect/crash survival

Show the completed 61-minute canary evidence: **3663.26 seconds**. Show the same worker/generation surviving a forced MCP daemon SIGKILL and reconnect.

Then start a 30-second-class command through `asympta_dispatch`. Show that it immediately returns a durable job handle instead of occupying one MCP request.

## 0:42–1:02 — Parallel DAG + uncertainty fencing

Create a flow with two independent nodes and one join. Show siblings run concurrently and the join waits.

Kill the worker during an idempotent node and resume it. Contrast with a non-idempotent node becoming `uncertain` instead of being replayed blindly.

## 1:02–1:30 — Background visual control without stealing attention

Keep Safari visibly frontmost.

1. Capture the background native harness window.
2. Inspect its AX tree.
3. Press `Increment` semantically: target state 0→1.
4. Click the same button from window-relative visual coordinates: target state 1→2.
5. Show `focus_preserved=true` and `mouse_injected=false`.

Then render an offscreen vector curve. Show 2,000 input points simplified to 123 points in about 8 ms with `mouse_used=false`.

State the boundary explicitly: arbitrary non-AX games/canvases are **not** silently controlled by stealing focus or the global mouse.

## 1:30–1:48 — Security + audit

Run `repo_read` against the repository, then demonstrate denied Home access, denied interpreter escape, and denied `git push`.

Run `event_verify` and show a valid SHA-256 chain.

## 1:48–2:13 — Real Apple release + measured response surface

Show Paperie Build 35:

GitHub `592f4fe` → three signed Xcode archives → IPA export → native `asc` → TestFlight.

Archive timings:

- cold / 4 workers: **45.323 s**
- cold / 8 workers: **29.593 s**
- warm / 8 workers: **26.263 s**

Show Build 35 `VALID` + `IN_BETA_TESTING`.

## 2:13–2:38 — Predictive execution, trap recovery, and reflection

Show one successful action's pre-action simulation map, then its prediction match and fast continuation. Next, deliberately run a deterministic failing action and show:

- deviation classification;
- generated future re-simulation sequence;
- exact-repeat `PREDICTIVE_TRAP_BLOCK`;
- `continuation_get` carrying the trap and safe next action outside chat context;
- a changed action succeeding and clearing the active trap.

Then open the task reflection/playbook. Highlight the stable invariant (8 workers + warm DerivedData), current variants, and the rule that final validation is always repeated.

## 2:38–2:52 — iPad steer + model neutrality

Show the paired LAN steering protocol and SSE/signal path. If the physical iPad is unavailable, show the protocol evidence and say the hardware gate is still open.

Show Claude MCP configuration. Do not claim Claude model execution unless `claude auth status` is logged in.

## 2:52–3:00 — Public evidence

Open `okok147/asympta-computer-public`: architecture, acceptance matrix, benchmark JSON, and this demo script.

End on the evidence matrix rather than a marketing claim.
