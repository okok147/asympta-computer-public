# Form and likeness

## Translate a single image into a model

Treat the reference as a projection with style decisions, not a depth scan. Record the camera assumption before changing geometry to match perspective. Prefer an orthographic or long-lens matched view for flat character drawings; retain diagnostic perspective views to expose shallow or broken construction.

Measure ratios against a stable unit such as head width or total visible height. Use only enough landmarks to guide decisions: head/body ratio, eye spacing, muzzle or face-patch width, ear span, limb length, feet spacing and accessory extent. Record normalized coordinates or proportions when helpful. Absolute dimensions remain an authored choice without calibration.

Identify the strongest recognition cues. For the supplied Momo monkey example these are the large rounded head/ears, peach heart-like face patch, tiny dark features, pear-shaped seated body, pale belly, curled tail and yellow banana-peel hat. Hidden back and side forms are design assumptions. Do not copy these cues into unrelated tasks.

## Construct expressive depth

- Build a continuous main body/head form with deliberately controlled cross-sections. Use symmetry only where it preserves the source's character.
- Shape face patches to the underlying curvature; avoid disconnected flat disks, clipping eyebrows and protruding eyes unless the style calls for them.
- Use tapered, smooth centerline curves for tails, stems, handles and ropes. Inspect endpoints, joins and thickness from multiple angles.
- Give accessories thickness and plausible attachment. For a banana peel hat, vary each peel's arc and taper while preserving the visible silhouette.
- Treat arm, leg and ear junctions as design decisions. Separate pieces can work for toy-like characters; inspect intersections at the final camera distance and required poses.
- Prefer broad readable forms over dense generic detail. Smooth shading hides facet normals, not an incorrect silhouette.

For organic deformation, require suitable topology and weights at joints. Voxel remesh can improve a static union but does not establish animation topology. For simple web idle motion, named rigid pivots can be sufficient; state this scope and test their actual transforms.

## Judge from evidence

Freeze the comparison view and list the visible mismatch before changing a parameter. Record `view → component → observed difference → correction`. Use clay for shape, flat colors for palette, wireframe for topology, and runtime lighting for the delivered look. Do not make every view a mandatory ritual.

Evaluate silhouette/proportion, identifying features, construction/depth, material readability and destination behavior separately. Avoid a single self-assigned score. Ask for user artistic feedback when it would resolve a subjective choice; complete reversible improvements first.

## Sources and limits

- [Blender mesh tools](https://docs.blender.org/manual/en/latest/modeling/meshes/index.html) and [curve tools](https://docs.blender.org/manual/en/latest/modeling/curves/index.html) describe construction operations.
- [Blender dependency graph example](https://docs.blender.org/api/current/bpy.types.Depsgraph.html) explains evaluated object/mesh inspection.
- [Blender glTF exporter documentation](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html) explains supported material/export behavior.

These technical sources do not validate an asset's likeness. Ground visual claims in the actual input, fixed-view comparisons and target-runtime inspection.
