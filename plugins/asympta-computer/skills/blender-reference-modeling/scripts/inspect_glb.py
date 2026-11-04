#!/usr/bin/env python3
"""Bounded standard-library GLB inspection; not a full glTF or visual validator."""
import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path

COMPONENTS = {5120: (1, "b"), 5121: (1, "B"), 5122: (2, "h"),
              5123: (2, "H"), 5125: (4, "I"), 5126: (4, "f")}
WIDTHS = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4,
          "MAT2": 4, "MAT3": 9, "MAT4": 16}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, name, minimum=0):
    require(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
            name + " must be an integer >= " + str(minimum))
    return value


def ref(items, index, label):
    integer(index, label)
    require(index < len(items), label + " index out of range")
    return items[index]


def parse_glb(path):
    raw = path.read_bytes()
    require(len(raw) >= 20, "Truncated GLB header/chunk")
    magic, version, size = struct.unpack_from("<4sII", raw)
    require(magic == b"glTF" and version == 2, "Expected GLB version 2")
    require(size == len(raw), "GLB declared length does not match bytes")
    chunks = []
    pos = 12
    while pos < len(raw):
        require(pos + 8 <= len(raw), "Truncated chunk header")
        length, kind = struct.unpack_from("<II", raw, pos)
        pos += 8
        require(length % 4 == 0, "Chunk length is not aligned to four bytes")
        require(pos + length <= len(raw), "Chunk exceeds container")
        chunks.append((kind, raw[pos:pos + length]))
        pos += length
    require(chunks and chunks[0][0] == 0x4E4F534A, "First GLB chunk must be JSON")
    require(sum(k == 0x4E4F534A for k, _ in chunks) == 1, "Duplicate JSON chunk")
    require(sum(k == 0x004E4942 for k, _ in chunks) <= 1, "Duplicate BIN chunk")
    document = json.loads(chunks[0][1].decode("utf-8"))
    require(isinstance(document, dict), "glTF JSON root must be an object")
    require(document.get("asset", {}).get("version") == "2.0", "Expected glTF asset version 2.0")
    binary = next((data for kind, data in chunks if kind == 0x004E4942), b"")
    return raw, document, binary, [hex(k) for k, _ in chunks if k not in (0x4E4F534A, 0x004E4942)]


def inspect_glb(filename, max_triangles=None, node_prefix=None, forbid_nodes=(), no_cameras_lights=False):
    path = Path(filename)
    raw, doc, binary, unknown_chunks = parse_glb(path)
    warnings = []
    if unknown_chunks:
        warnings.append("Unknown GLB chunk types: " + repr(unknown_chunks))
    lists = {}
    for key in ("buffers", "bufferViews", "accessors", "meshes", "nodes",
                "scenes", "materials", "images", "textures", "skins", "animations", "cameras"):
        items = doc.get(key, [])
        require(isinstance(items, list) and all(isinstance(item, dict) for item in items),
                key + " must be an array of objects")
        lists[key] = items
    buffers, views, accessors = (lists[k] for k in ("buffers", "bufferViews", "accessors"))
    external = []
    embedded_buffer_index = None
    for index, buffer in enumerate(buffers):
        length = integer(buffer.get("byteLength"), "buffer byteLength")
        uri = buffer.get("uri")
        if uri is None:
            require(index == 0, "Only GLB buffer 0 may omit its URI")
            require(length <= len(binary) <= length + 3, "BIN length does not fit buffer 0")
            embedded_buffer_index = index
        else:
            require(isinstance(uri, str), "buffer URI must be text")
            external.append({"kind": "buffer", "index": index,
                             "uri": "[data URI]" if uri.startswith("data:") else uri})
    require(not binary or embedded_buffer_index is not None, "Unreferenced BIN chunk")
    for index, view in enumerate(views):
        buffer = ref(buffers, view.get("buffer"), "bufferView buffer")
        offset = integer(view.get("byteOffset", 0), "bufferView byteOffset")
        length = integer(view.get("byteLength"), "bufferView byteLength")
        require(offset + length <= buffer["byteLength"], "bufferView exceeds buffer")
        if "byteStride" in view:
            stride = integer(view["byteStride"], "bufferView byteStride", 4)
            require(stride <= 252 and stride % 4 == 0, "Invalid bufferView byteStride")

    def element_size(accessor):
        size = COMPONENTS[accessor["componentType"]][0]
        kind = accessor["type"]
        if kind.startswith("MAT"):
            side = int(kind[-1])
            column_bytes = ((side * size + 3) // 4) * 4
            return side * column_bytes
        return WIDTHS[kind] * size

    for index, accessor in enumerate(accessors):
        integer(accessor.get("count"), "accessor count", 1)
        require(accessor.get("componentType") in COMPONENTS, "Unsupported accessor componentType")
        require(accessor.get("type") in WIDTHS, "Unsupported accessor type")
        offset = integer(accessor.get("byteOffset", 0), "accessor byteOffset")
        if "bufferView" in accessor:
            view = ref(views, accessor["bufferView"], "accessor bufferView")
            size = element_size(accessor)
            stride = view.get("byteStride", size)
            require(stride >= size, "Accessor element exceeds byte stride")
            require(offset + (accessor["count"] - 1) * stride + size <= view["byteLength"],
                    "Accessor exceeds bufferView")
            require((view.get("byteOffset", 0) + offset) % COMPONENTS[accessor["componentType"]][0] == 0,
                    "Accessor offset is not component aligned")
        elif offset:
            raise ValueError("Accessor without bufferView has byteOffset")
        if "sparse" in accessor:
            sparse = accessor["sparse"]
            count = integer(sparse.get("count"), "sparse count", 1)
            require(count <= accessor["count"], "Sparse count exceeds accessor count")
            for kind in ("indices", "values"):
                entry = sparse.get(kind, {})
                view = ref(views, entry.get("bufferView"), "sparse " + kind + " bufferView")
                offset = integer(entry.get("byteOffset", 0), "sparse byteOffset")
                size = element_size(accessor)
                if kind == "indices":
                    require(entry.get("componentType") in (5121, 5123, 5125), "Invalid sparse index component")
                    size = COMPONENTS[entry["componentType"]][0]
                require(offset + count * size <= view["byteLength"], "Sparse data exceeds bufferView")
            warnings.append("Sparse accessor " + str(index) + ": data range checked; replacement values not decoded.")

    mesh_rows = []
    for index, mesh in enumerate(lists["meshes"]):
        primitives = mesh.get("primitives", [])
        require(isinstance(primitives, list) and primitives, "Mesh has no primitives")
        triangles, vertices = 0, 0
        for primitive in primitives:
            require(isinstance(primitive, dict), "Primitive must be an object")
            attrs = primitive.get("attributes", {})
            require(isinstance(attrs, dict) and "POSITION" in attrs, "Primitive lacks POSITION")
            position = ref(accessors, attrs["POSITION"], "POSITION")
            require(position["type"] == "VEC3", "POSITION must be VEC3")
            for semantic, value in attrs.items():
                attr = ref(accessors, value, "attribute " + semantic)
                require(attr["count"] == position["count"], "Primitive attribute counts differ")
            vertices += position["count"]
            if "material" in primitive:
                ref(lists["materials"], primitive["material"], "primitive material")
            count = position["count"]
            if "indices" in primitive:
                accessor = ref(accessors, primitive["indices"], "indices")
                require(accessor["type"] == "SCALAR" and accessor["componentType"] in (5121, 5123, 5125),
                        "Invalid index accessor")
                count = accessor["count"]
                view = views[accessor["bufferView"]] if "bufferView" in accessor else None
                if view and view["buffer"] == embedded_buffer_index and "sparse" not in accessor:
                    size, fmt = COMPONENTS[accessor["componentType"]]
                    stride = view.get("byteStride", size)
                    start = view.get("byteOffset", 0) + accessor.get("byteOffset", 0)
                    maximum = max(struct.unpack_from("<" + fmt, binary, start + n * stride)[0]
                                  for n in range(count))
                    require(maximum < position["count"], "Index references a missing vertex")
            mode = primitive.get("mode", 4)
            require(isinstance(mode, int) and 0 <= mode <= 6, "Invalid primitive mode")
            if mode == 4:
                require(count % 3 == 0, "TRIANGLES count is not divisible by three")
                triangles += count // 3
            elif mode in (5, 6):
                triangles += max(0, count - 2)
            else:
                warnings.append("Non-triangle primitive in mesh " + str(index))
            for target in primitive.get("targets", []):
                for semantic, value in target.items():
                    require(ref(accessors, value, "morph " + semantic)["count"] == position["count"],
                            "Morph target count differs from POSITION")
        mesh_rows.append({"index": index, "name": mesh.get("name"),
                          "primitives": len(primitives), "triangles": triangles,
                          "primitive_vertices": vertices})
    nodes = lists["nodes"]
    for node in nodes:
        if "mesh" in node:
            ref(mesh_rows, node["mesh"], "node mesh")
        if "skin" in node:
            ref(lists["skins"], node["skin"], "node skin")
        if "camera" in node:
            ref(lists["cameras"], node["camera"], "node camera")
        for child in node.get("children", []):
            ref(nodes, child, "child node")
    for image in lists["images"]:
        if "bufferView" in image:
            ref(views, image["bufferView"], "image bufferView")
        if "uri" in image:
            require(isinstance(image["uri"], str), "image URI must be text")
            external.append({"kind": "image", "uri": "[data URI]" if image["uri"].startswith("data:") else image["uri"]})
    scene_index = doc.get("scene", 0 if lists["scenes"] else None)
    scene_triangles = None
    scene_nodes = []
    if scene_index is not None:
        active = ref(lists["scenes"], scene_index, "active scene")
        pending = list(active.get("nodes", []))
        seen = set()
        scene_triangles = 0
        while pending:
            index = pending.pop()
            node = ref(nodes, index, "scene node")
            require(index not in seen, "Active scene contains a cycle or multiply parented node")
            seen.add(index)
            scene_nodes.append(index)
            multiplier = 1
            instanced = node.get("extensions", {}).get("EXT_mesh_gpu_instancing", {}).get("attributes", {})
            if instanced:
                counts = {ref(accessors, value, "instance attribute")["count"] for value in instanced.values()}
                require(len(counts) == 1, "Instance attribute counts differ")
                multiplier = counts.pop()
            if "mesh" in node:
                scene_triangles += mesh_rows[node["mesh"]]["triangles"] * multiplier
            pending.extend(node.get("children", []))
    else:
        warnings.append("No scene is declared; only unique mesh counts are available.")
    light_count = len(doc.get("extensions", {}).get("KHR_lights_punctual", {}).get("lights", []))
    if node_prefix:
        for entity in nodes + lists["meshes"]:
            require(isinstance(entity.get("name"), str) and entity["name"].startswith(node_prefix),
                    "Object outside required name prefix: " + repr(entity.get("name")))
    forbidden = set(forbid_nodes)
    require(not any(node.get("name") in forbidden for node in nodes), "Forbidden node present")
    if no_cameras_lights:
        require(not lists["cameras"] and not light_count
                and not any("KHR_lights_punctual" in node.get("extensions", {}) for node in nodes),
                "Camera/light data is present in character-only export")
    required_extensions = doc.get("extensionsRequired", [])
    used_extensions = doc.get("extensionsUsed", [])
    require(isinstance(required_extensions, list) and isinstance(used_extensions, list), "Invalid extensions lists")
    if used_extensions:
        warnings.append("Extension semantics are not fully validated: " + ", ".join(used_extensions))
    if external:
        warnings.append("URI resources are listed but not fetched or verified.")
    if max_triangles is not None:
        integer(max_triangles, "max_triangles")
        require(scene_triangles is not None, "Cannot check scene triangle budget without a scene")
        require(scene_triangles <= max_triangles,
                "Active scene triangle budget exceeded: " + str(scene_triangles) + " > " + str(max_triangles))
    return {
        "schema": "asympta.glb-inspection.v1", "ok": True,
        "path": str(path.resolve()), "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "generator": doc["asset"].get("generator"),
        "counts": {key: len(value) for key, value in lists.items()},
        "unique_mesh_triangles": sum(row["triangles"] for row in mesh_rows),
        "active_scene": scene_index, "active_scene_nodes": len(scene_nodes),
        "active_scene_triangles": scene_triangles,
        "meshes": mesh_rows,
        "node_names": [node.get("name") for node in nodes],
        "material_names": [material.get("name") for material in lists["materials"]],
        "animation_names": [animation.get("name") for animation in lists["animations"]],
        "light_count": light_count, "used_extensions": used_extensions,
        "required_extensions": required_extensions,
        "external_resources": external, "warnings": warnings,
        "limits": ["Structural subset only; not the complete Khronos validator.",
                   "Does not assess silhouette, depth, normals, topology, shading, rig motion or runtime performance."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--max-triangles", type=int)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--node-prefix")
    parser.add_argument("--forbid-node", action="append", default=[])
    parser.add_argument("--no-cameras-lights", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = inspect_glb(args.file, args.max_triangles, args.node_prefix,
                             args.forbid_node, args.no_cameras_lights)
    except (OSError, ValueError, TypeError, KeyError, struct.error) as error:
        report = {"schema": "asympta.glb-inspection.v1", "ok": False,
                  "path": str(args.file), "error": str(error)}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
