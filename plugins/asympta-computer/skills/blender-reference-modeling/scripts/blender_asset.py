"""Blender/MCP-safe collection inspection and optional export; submit source directly.
Do host-side output preflight first. No filesystem reads, network, exec or scene reset.
"""
import bpy
import json
import re
from mathutils import Vector


def _object_name(obj):
    return obj.name


def _matrix(value):
    return [[round(float(n), 8) for n in row] for row in value]


def _output_path(value, suffix=None):
    if value is None:
        return None
    if not isinstance(value, str) or not value.startswith("/"):
        raise ValueError("Use an explicit absolute output path.")
    if suffix and not value.lower().endswith(suffix):
        raise ValueError("Expected " + suffix + " output path.")
    return value


def capture_asset(collection_name, camera_names=(), glb_path=None, blend_path=None,
                  render_dir=None, outputs_preflighted=False, export_animations=False):
    """Inspect without mutation by default. Preflight owned output paths on the host."""
    if bpy.context.mode != "OBJECT":
        raise ValueError("Switch the owned scene to OBJECT mode before capture.")
    collection = bpy.data.collections.get(collection_name)
    if collection is None:
        raise ValueError("Missing collection: " + collection_name)
    objects = sorted(collection.all_objects, key=_object_name)
    if not objects:
        raise ValueError("The named collection is empty.")
    scene = bpy.context.scene
    outside_scene = [o.name for o in objects if o.name not in scene.objects]
    if outside_scene:
        raise ValueError("Collection is not fully in the active scene: " + repr(outside_scene))
    cameras = []
    for name in dict.fromkeys(camera_names):
        obj = bpy.data.objects.get(name)
        if obj is None or obj.type != "CAMERA" or obj.name not in scene.objects:
            raise ValueError("Missing camera in the active scene: " + name)
        cameras.append(obj)
    if render_dir and not cameras:
        raise ValueError("Rendering requires explicit existing camera names.")
    glb_path = _output_path(glb_path, ".glb")
    blend_path = _output_path(blend_path, ".blend")
    render_dir = _output_path(render_dir)
    render_paths = [(render_dir.rstrip("/") + "/" +
                     re.sub(r"[^A-Za-z0-9_.-]+", "_", camera.name) + ".png")
                    for camera in cameras] if render_dir else []
    outputs = [p for p in (glb_path, blend_path) if p] + render_paths
    if len(outputs) != len(set(outputs)):
        raise ValueError("Output paths collide.")
    if outputs and not outputs_preflighted:
        raise ValueError("Check output ownership, existing files and parent directories on the host first.")

    object_set = set(objects)
    dependencies, instances = [], []
    for obj in objects:
        if obj.parent and obj.parent not in object_set:
            dependencies.append({"object": obj.name, "kind": "parent", "target": obj.parent.name})
        if obj.instance_type == "COLLECTION":
            instances.append(obj.name)
        for mod in obj.modifiers:
            if mod.type == "ARMATURE" and mod.object and mod.object not in object_set:
                dependencies.append({"object": obj.name, "kind": "armature", "target": mod.object.name})
        for con in obj.constraints:
            target = getattr(con, "target", None)
            if target and target not in object_set:
                dependencies.append({"object": obj.name, "kind": "constraint", "target": target.name})
    if glb_path and (dependencies or instances):
        raise ValueError("Resolve external dependencies/realize collection instances before export: "
                         + json.dumps({"dependencies": dependencies, "instances": instances}))

    graph = bpy.context.evaluated_depsgraph_get()
    rows, corners = [], []
    for obj in objects:
        row = {"name": obj.name, "type": obj.type,
               "parent": obj.parent.name if obj.parent else None,
               "world_matrix": _matrix(obj.matrix_world),
               "hidden_render": bool(obj.hide_render),
               "materials": [slot.material.name if slot.material else None
                             for slot in obj.material_slots],
               "modifiers": [mod.type for mod in obj.modifiers]}
        if obj.type in {"MESH", "CURVE", "SURFACE", "FONT", "META"}:
            evaluated = obj.evaluated_get(graph)
            mesh = evaluated.to_mesh()
            try:
                if mesh is not None:
                    mesh.calc_loop_triangles()
                    row.update(vertices=len(mesh.vertices), polygons=len(mesh.polygons),
                               evaluated_triangles=len(mesh.loop_triangles))
                    corners.extend(evaluated.matrix_world @ Vector(c) for c in evaluated.bound_box)
            finally:
                evaluated.to_mesh_clear()
        rows.append(row)
    report = {
        "schema": "asympta.blender-asset.v1",
        "blender_version": bpy.app.version_string,
        "source_file": bpy.data.filepath or None,
        "scene": scene.name, "collection": collection.name,
        "frame": scene.frame_current,
        "unit_scale": scene.unit_settings.scale_length,
        "objects": rows, "object_count": len(rows),
        "evaluated_triangles": sum(r.get("evaluated_triangles", 0) for r in rows),
        "external_dependencies": dependencies, "collection_instances": instances,
        "cameras": [{
            "name": c.name, "world_matrix": _matrix(c.matrix_world),
            "type": c.data.type, "lens_mm": c.data.lens,
            "ortho_scale": c.data.ortho_scale, "shift_x": c.data.shift_x,
            "shift_y": c.data.shift_y, "clip_start": c.data.clip_start,
            "clip_end": c.data.clip_end} for c in cameras],
        "render": {
            "engine": scene.render.engine,
            "resolution": [scene.render.resolution_x, scene.render.resolution_y],
            "percentage": scene.render.resolution_percentage,
            "view_transform": scene.view_settings.view_transform,
            "look": scene.view_settings.look,
            "exposure": scene.view_settings.exposure,
            "gamma": scene.view_settings.gamma},
        "artifact_paths": {},
        "limits": ["Host must verify produced files, sizes and hashes.",
                   "Evaluated mesh counts can differ from exported counts.",
                   "This report does not establish likeness, topology quality, deformation or runtime acceptance.",
                   "A blend copy includes the entire open Blender file."]}
    if corners:
        report["world_bounds"] = {
            "min": [min(float(c[i]) for c in corners) for i in range(3)],
            "max": [max(float(c[i]) for c in corners) for i in range(3)]}
    json.dumps(report, allow_nan=False)
    if not outputs:
        return report

    old_selection = list(bpy.context.selected_objects)
    old_active = bpy.context.view_layer.objects.active
    old_camera, old_frame = scene.camera, scene.frame_current
    old_path = scene.render.filepath
    old_format = scene.render.image_settings.file_format
    old_extension = scene.render.use_file_extension
    try:
        if glb_path:
            unavailable = [o.name for o in objects if o.name not in bpy.context.view_layer.objects]
            if unavailable:
                raise ValueError("Export objects are excluded from active view layer: " + repr(unavailable))
            options = {"filepath": glb_path, "export_format": "GLB",
                       "use_selection": True, "use_active_scene": True,
                       "collection": collection_name, "export_apply": False,
                       "export_yup": True, "export_cameras": False,
                       "export_lights": False, "export_animations": bool(export_animations)}
            supported = set(bpy.ops.export_scene.gltf.get_rna_type().properties.keys())
            missing = set(options) - supported
            if missing:
                raise RuntimeError("Installed glTF exporter lacks required options: " + repr(sorted(missing)))
            for obj in bpy.context.selected_objects:
                obj.select_set(False)
            for obj in objects:
                obj.select_set(True)
            result = bpy.ops.export_scene.gltf(**options)
            if "FINISHED" not in result:
                raise RuntimeError("glTF exporter did not report FINISHED.")
            report["export_options_requested"] = options
            report["artifact_paths"]["glb"] = glb_path
        if render_dir:
            scene.render.image_settings.file_format = "PNG"
            scene.render.use_file_extension = True
            report["artifact_paths"]["renders"] = []
            for camera, path in zip(cameras, render_paths):
                scene.camera = camera
                scene.render.filepath = path
                result = bpy.ops.render.render(write_still=True)
                if "FINISHED" not in result:
                    raise RuntimeError("Render did not report FINISHED: " + path)
                report["artifact_paths"]["renders"].append({"camera": camera.name, "path": path})
    finally:
        if render_dir:
            scene.camera = old_camera
            scene.render.filepath = old_path
            scene.render.image_settings.file_format = old_format
            scene.render.use_file_extension = old_extension
        if scene.frame_current != old_frame:
            scene.frame_set(old_frame)
        if glb_path:
            for obj in bpy.context.selected_objects:
                obj.select_set(False)
            for obj in old_selection:
                if obj.name in bpy.context.view_layer.objects:
                    obj.select_set(True)
            bpy.context.view_layer.objects.active = old_active
    if blend_path:
        result = bpy.ops.wm.save_as_mainfile(filepath=blend_path, copy=True, check_existing=False)
        if "FINISHED" not in result:
            raise RuntimeError("Blend copy operator did not report FINISHED.")
        report["artifact_paths"]["blend"] = blend_path
    return report
