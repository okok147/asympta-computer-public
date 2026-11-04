---
name: blender-reference-modeling
description: Build, refine and verify editable Blender models from image references through Asympta Computer and Blender MCP. Use for reference-matched characters, creatures or props, fixed-camera visual iteration, and GLB delivery to websites or games without paid generation services.
---

# Blender Reference Modeling

Produce a real editable model and verify the actual export in its destination. Treat resemblance, mesh validity, animation and runtime behavior as separate evidence.

## Keep the boundary

Use Blender geometry, curves, modifiers, materials and Python with the existing chat model. Do not call external image-to-3D, paid model APIs, hosted GPU inference or asset-generation services. Do not silently enable Meshy, Rodin, Tripo, Hunyuan, Hyper3D, Poly Haven or Sketchfab integrations. Existing user-provided assets may be used with their provenance. A later explicit user authorization may change this task's boundary; tool availability never does.

Keep one writer per Blender scene. Use an owned scene/collection and deterministic names; preserve other scenes, unsaved work and other operators. Check current files and ownership before opening, resetting or saving a scene. Keep generators and meaningful checkpoints in the project.

## 1. Establish the reference and delivery contract

Inspect the actual supplied image. Transfer its bytes to the Blender execution host when that host needs them; a cloud path is not a Mac path. Record input SHA-256, actual dimensions and destination path. If transfer is unavailable, retain the original visual observation and report the comparison limitation.

Separate visible observations, explicit user requirements, reversible assumptions and hidden-view unknowns. Record 5–8 identifying cues: silhouette, major proportions, face/feature spacing, attachments, colors and asymmetry. Infer unseen depth coherently; do not claim one image uniquely determines it.

Choose the required use view, scale/origin, orientation, materials, geometry budget and static/animated scope from the destination. Resolve only consequential ambiguity. For a website, inspect its current asset loading, rendering and interaction before choosing an export contract. Read [form and likeness](references/form-and-likeness.md) for single-view characters and stylized props.

## 2. Connect and construct

Discover the installed Asympta/Blender tools and verify a real scene read. Do not assume upstream names or an open socket mean Blender execution works. Use the existing authorized Blender MCP route; prefer bounded Python operations with explicit object names. Preserve uncertain call effects and inspect state before replay.

Build silhouette and proportion first. Use coherent mesh construction, lofted cross-sections, connected forms and intentional curve profiles. Simple primitives are useful for blockout; refine junctions, depth and silhouette where the reference needs it. Keep face patches, accessories and pivots separately editable when this supports iteration or animation. Avoid adding subdivision merely to inflate polygon counts.

Use glTF-compatible materials where runtime delivery matters. Keep roughness, color management and light intensity controlled. Author required detail as geometry, UV textures or supported material inputs; Blender-only procedural shading is not export proof.

## 3. Compare, correct, checkpoint

Lock a reference-matched camera, framing, pose, lighting and color management. Keep named front/reference and three-quarter cameras; add side/back/clay/wireframe views only to resolve a real question. Inspect real rendered or viewport images, including the destination's normal display size.

Record the largest 1–3 visible discrepancies and their view/component before each correction. Fix silhouette and proportion before small details. Distinguish geometry from camera or lighting errors. Edit the same asset, preserve correct regions and compare under the same conditions. Save checkpoints before destructive topology changes. Stop optional checks after the requirements pass; revise the plan when a remaining defect needs a different technique.

Never replace a missing 3D asset with an image billboard or treat a beauty render as geometry verification. Do not infer a percentage resemblance or animation readiness from a successful script.

## 4. Export and demonstrate

Save the editable `.blend` and a collection-scoped `.glb`. Exclude studio geometry/lights/cameras unless explicitly required. Retain root, semantic object names, animation/rig requirements and source/asset hashes. Preserve shape keys deliberately; applying modifiers during glTF export can remove their export path.

Use the bundled helpers through the execution host:

- [`scripts/blender_asset.py`](scripts/blender_asset.py): inspect an explicit collection, record evaluated geometry and named camera settings, optionally render those cameras and export only the collection. Submit its source directly through safe-mode MCP. It preserves selection/frame/camera/render path, does not clear scenes or generate geometry, and performs no filesystem reads or network requests.
- [`scripts/inspect_glb.py`](scripts/inspect_glb.py): inspect GLB container/buffer integrity and declared mesh/material/scene counts with standard Python. It is a bounded structural check, not a complete glTF validator or aesthetic judge.

Read [execution and evidence](references/execution-and-evidence.md) before running helpers. Reopen the export in a separate clean scene/process and test it in the actual target. Check orientation, floor contact, scale, materials, normals, missing dependencies, camera framing and requested interactions/poses. Match performance claims to measured device/browser evidence.

For a requested website result, integrate the actual GLB, preserve the existing product, deploy through its established authorized route, and inspect the live URL after loading the new asset. A local screenshot, deployment ACK or source commit alone does not establish live acceptance.

Deliver actual artifact paths/links, source revision, exact changed asset, inspection evidence and remaining limits. Distinguish a static mesh with object-pivot motion from a skinned character rig; only claim the behavior actually implemented and observed.
