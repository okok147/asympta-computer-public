# Execution and evidence

## Host boundary and ownership

Discover the live Asympta tool schema once when the route is unknown. Check Blender version, MCP status and a real scene read. Use one scene writer and the established authorized connection. Do not start a second writer, restart services, disable safe mode or enable paid generators to bypass a failure.

Transfer files through a supported file API or an explicit authorized artifact path. Verify SHA-256 and size after transfer. Never assume a ChatGPT scratch path exists on the Mac. Keep API keys, signed URLs and unrelated scene contents out of evidence. If a write times out, inspect the object/file before retrying.

Use an isolated owned collection and descriptive stable names. Keep studio elements outside the export collection. Use real screenshots returned by Blender or the destination; never substitute a generated depiction for evidence.

## Blender helper through safe-mode MCP

Read `scripts/blender_asset.py` on the host and submit its source as the execute-code tool's code argument, followed by an explicit call. Do not use `exec(open(...))`, `eval`, dynamic module loading or an external file loader inside Blender MCP. Use named functions rather than lambdas; the observed guard rejects lambda callbacks even in sorting. Keep the tool's safe mode enabled.

The observed MCP 2.0.4 safe mode allows `bpy`, `bmesh`, `mathutils` and pure Python standard-library imports. It rejects `eval/exec/open`, `os/subprocess/network`, handlers/timers/drivers, class/property registration and `bpy.data.libraries.*`. Blender operators for saving, rendering and import/export remain allowed. Verify the installed behavior instead of assuming later versions have identical guards.

Append an inspect-only call first:

```python
print(json.dumps(capture_asset(
    collection_name="Momo_Character",
    camera_names=["Momo_CameraFront", "Momo_CameraThreeQuarter"],
), allow_nan=False))
```

Inspect the inner Blender result, not only the outer MCP success flag or receipt. An outer successful tool envelope can contain an explicit safe-mode rejection; that is a failed execution, and the intended scene mutation has not been demonstrated.

The helper requires an existing collection and OBJECT mode. It never creates geometry or clears a scene. Copy its returned JSON to an evidence file through the host file API. Inspect-only mode performs no file writes.

Before requesting any export, use host tools to check exact output ownership, existing-file status and parent directories. Create only the needed directories. Choose new filenames unless replacing a known owned output is intentional. Then call:

```python
print(json.dumps(capture_asset(
    collection_name="Momo_Character",
    camera_names=["Momo_CameraFront", "Momo_CameraThreeQuarter"],
    glb_path="/absolute/project/assets/momo.glb",
    blend_path="/absolute/project/source/momo.blend",
    render_dir="/absolute/project/evidence/fixed-views",
    outputs_preflighted=True,
    export_animations=False,
), allow_nan=False))
```

Omit any unneeded output parameter. `outputs_preflighted` records that the operator performed the host checks; it is not permission or proof. Verify the resulting files through the host afterward. The helper intentionally performs no filesystem reads or hashing inside MCP.

The `.blend` operator saves a copy of the entire open file, including other scenes and studio objects. Preserve unsaved work and isolate the source before sharing it; do not use forbidden `libraries.write` to evade safe mode. A copy-save receipt does not establish that only one collection is present.

The GLB exporter requires `use_selection=True`, `use_active_scene=True` and the exact `collection` name. Actual Blender 5.2.2 testing found that selection alone could include a default Cube from another scene. Inspect exported node/mesh names and reject unrelated objects; do not infer scope from `FINISHED`.

Collection instances and external parent/armature/constraint targets block export until deliberately resolved. Preserve shape keys with `export_apply=False`; apply necessary modifiers on an owned export copy only after checking shape-key/rig effects. Animation export is opt-in. Record and test actual clips; rigid web pivots are not a skinning rig.

For inverted-hull cartoon outlines, verify shadows separately from visible backface culling. An outline shell can cast unwanted dark shadows onto the colored character. Use the installed Blender material's supported shadow-culling controls and compare a real render; verify the exported/runtime outline behavior independently.

The report records evaluated triangles at the current frame, camera matrices, render settings and requested exporter options. Evaluated counts can differ from exported counts. Rendering uses existing resolution, lighting, engine and camera configuration and restores properties changed by the helper.

## GLB helper on the host

Run the exported bytes through ordinary host Python:

```text
python3 inspect_glb.py /absolute/project/assets/momo.glb \
  --max-triangles 60000 --report /absolute/project/evidence/glb-report.json
```

Choose the budget for the actual task; 60,000 is an example. The helper returns nonzero on structural errors or an exceeded declared scene-triangle budget. It reports file SHA-256/bytes, unique mesh triangles and instantiated active-scene triangles. URI resources are listed but never fetched. Unknown compressed/extension semantics are warnings.

Use returned node names to check collection scope. For a consistently prefixed asset, every mesh/node must belong to that prefix; studio floor, default Cube, cameras and lights must be absent unless explicitly required. Check actual camera/light counts and extensions when relevant.

Bounds, normals, intersections, texture appearance and motion still need appropriate inspection. This helper is a structural subset, not the official [Khronos glTF Validator](https://github.com/KhronosGroup/glTF-Validator). Use the latter if broader format validation is required.

## Destination acceptance

Reimport the GLB in a separate owned scene/process; preserve the original. Confirm mesh presence, useful 3D depth, scale, orientation, materials and root/pivots. Use the real site/engine with its actual camera and lighting. Test drag/orbit, idle/animation and loading/fallback states when applicable. Use the exact deployed asset URL/hash to link evidence to the live result.

Retain a short manifest: input hash/dimensions; generator path/hash; Blender/MCP versions; source revision; collection/cameras/frame; exported asset hash/bytes; GLB report; observed runtime URL/version; screenshots and unresolved issues. Label tests not run. Record authoring as procedural Blender modeling unless another source was actually used.

## Technical references

- [Blender MCP upstream](https://github.com/ahujasid/blender-mcp): installed capabilities/guards vary; external generators are optional, not required.
- [Blender glTF documentation](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html): material compatibility and shape-key/modifier constraints.
- [Khronos glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html): container, primitive and scene semantics.
