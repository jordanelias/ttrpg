#!/usr/bin/env python3
"""
jsx_to_canonical.py — Phase 2 coordinate migration helper.

Reads designs/world/adjacency_map.jsx, extracts 17 territory (x, y) coordinates
from the abstract 700×600 jsx canvas, and projects them onto the canonical
1920×2880 coordinate system established by Phase 2 workplan §1.1.

Outputs a YAML stub for hand-authoring during the Phase 2 authoring session.
The stub contains:
  - jsx_anchor: original jsx coordinates (for reference)
  - scaled_anchor: pure linear scaling result
  - canonical_anchor: TBD placeholder for hand-authoring
  - correction_note: per-territory hint for the geographic correction needed

The script is deterministic and side-effect-free. It does NOT make territory
placement decisions — those are hand-authored in the next session per workplan
§1.3 (Lake Eidursjø + T4 Grauwald) and known geographic facts.

Authority: PP-707 / ED-779 / Phase 2 workplan
Date: 2026-05-01
Usage: python3 tools/geography/jsx_to_canonical.py [--out OUTPUT.yaml]
       (default output: tools/geography/canonical_anchors_stub.yaml)
"""

import re
import sys
import argparse
from pathlib import Path

# Canvas dimensions (per Phase 2 workplan §1.1).
JSX_W, JSX_H = 700, 600
CANONICAL_W, CANONICAL_H = 1920, 2880
SCALE_X = CANONICAL_W / JSX_W   # ~2.7428
SCALE_Y = CANONICAL_H / JSX_H   # 4.8

# Per-territory geographic correction notes.
# These are hints for the Phase 2 authoring session — NOT prescriptions.
# The author applies geographic knowledge (region from geography_v30.md, faction
# clustering, terrain features) to place each anchor at a sensible canonical
# location, using scaled_anchor as starting reference.
CORRECTION_NOTES = {
    'T1': "Eastern Lowlands. River-sea nexus. Place south of northern mountains, on east coast adjacent to major river outflow. Crown capital, Italian-coded.",
    'T2': "Crown heartland, agricultural. Place between T1 (east) and northern mountains (north). Adjacent T1, T3, T9, T14.",
    'T3': "NE pass border fortress. Place at the junction of NE Lowenskyst Pass and the Crown territory boundary, near the northern range.",
    'T4': "Highland timber, NE shore of Lake Eidursjø per workplan §1.3. Approximate canonical position: ~(1090, 1430). Above lake's north tip.",
    'T5': "Crown breadbasket, fertile floodplain. Place east-central, between T1 and T6, in Eastern Lowlands.",
    'T6': "Southern Crown farmland, Calamity-adjacent. Place south, between T5 (north) and T15 Askeheim (south). Adjacent T5, T13, T15.",
    'T7': "Hafenmark timber valley. Place in NW Highlands region, west-central, north of Lake Eidursjø. Adjacent T4, T8.",
    'T8': "Hafenmark capital. Place in NW Highlands, central-west. Major settlement; mining and smithing infrastructure (T17 mines + T8 metalworking). Adjacent T7, T9, T10, T17.",
    'T9': "Cathedral city. Place on mountain ridge between NE and NW passes (per geography_v30 — Altonian containment decision). Center-north. Adjacent T2, T3, T8, T14, T17.",
    'T10': "NW pass border castle. Place at junction of NW Spartfell Pass and Hafenmark territory. Northwestern.",
    'T11': "Central fjords, Varfell. Place west of Lake Eidursjø, north (Norwegian-coded). Adjacent T10, T12.",
    'T12': "Varfell Seat, central western fjord coast. Place west of Lake Eidursjø. Approximate canonical position: ~(540, 1850) per workplan §1.3.",
    'T13': "Southern fjords, Calamity-adjacent. Place south, west of T15. Adjacent T6, T12, T15.",
    'T14': "Crown military hinge. Place east of Lake Eidursjø, central. Approximate canonical position: ~(1290, 1320). 5-way connection hub.",
    'T15': "Askeheim. Calamity epicenter. Place south, west-central. Approximate canonical position: ~(890, 2680). Surrounded by Calamity radiation rings + Forgetting Zone polygon.",
    'T16': "Schoenland island. Place EAST of peninsula, off-shore from T1 Valorsplatz. Per geography_v30, sea connection to T1. NOT north (jsx places it north schematically; canon places it east-coast offshore).",
    'T17': "Northern mines (Hafenmark). Place high-north, in NW Highlands above T8. Adjacent T3, T8, T9.",
}


def extract_jsx_coords(jsx_path: Path) -> dict:
    """Parse jsx file for territory (x, y) coords."""
    text = jsx_path.read_text()
    # Match: T1: { name: 'Valorsplatz', control: 'Crown', x: 560, y: 245 }
    pattern = (
        r"T(\d+):\s*\{[^}]*"
        r"name:\s*'([^']+)'[^}]*"
        r"control:\s*'([^']+)'[^}]*"
        r"x:\s*(\d+),\s*y:\s*(\d+)"
    )
    out = {}
    for m in re.finditer(pattern, text):
        tnum, name, control, x, y = m.groups()
        tid = f'T{tnum}'
        out[tid] = {
            'name': name,
            'control': control,
            'x': int(x),
            'y': int(y),
        }
    return out


def extract_jsx_edges(jsx_path: Path) -> list:
    """Parse jsx file for territory adjacency edges."""
    text = jsx_path.read_text()
    edge_re = r"\['(T\d+)',\s*'(T\d+)'\]"
    edges = set()
    for m in re.finditer(edge_re, text):
        a, b = sorted([m.group(1), m.group(2)], key=lambda s: int(s[1:]))
        edges.add((a, b))
    return sorted(edges, key=lambda p: (int(p[0][1:]), int(p[1][1:])))


def scale_to_canonical(x: int, y: int) -> tuple:
    """Pure linear scale from 700×600 → 1920×2880."""
    return (round(x * SCALE_X), round(y * SCALE_Y))


def emit_yaml_stub(coords: dict, edges: list, out_path: Path) -> None:
    """Write the YAML stub for Phase 2 hand-authoring."""
    lines = []
    lines.append("# Canonical Territory Anchors — Phase 2 Stub")
    lines.append("# Generated by tools/geography/jsx_to_canonical.py")
    lines.append("# Authority: PP-707 / ED-779 / Phase 2 workplan §1.1, §1.2, §1.3")
    lines.append(f"# Source: designs/world/adjacency_map.jsx ({JSX_W}×{JSX_H} canvas)")
    lines.append(f"# Target: canonical {CANONICAL_W}×{CANONICAL_H} system")
    lines.append(f"# Scale factors: x×{SCALE_X:.4f}, y×{SCALE_Y:.4f}")
    lines.append("#")
    lines.append("# Phase 2 authoring session: fill canonical_anchor for each territory")
    lines.append("# using scaled_anchor as starting reference plus correction_note as guidance.")
    lines.append("# Then author province polygons (4-8 vertices each) per §1.7 schema.")
    lines.append("")
    lines.append("territories:")

    # Order by T#
    for tid in sorted(coords.keys(), key=lambda t: int(t[1:])):
        d = coords[tid]
        sx, sy = scale_to_canonical(d['x'], d['y'])
        note = CORRECTION_NOTES.get(tid, "(no correction note)")
        lines.append(f"  {tid}:")
        lines.append(f"    name: {d['name']}")
        lines.append(f"    faction: {d['control']}")
        lines.append(f"    jsx_anchor: [{d['x']}, {d['y']}]   # original abstract jsx coords")
        lines.append(f"    scaled_anchor: [{sx}, {sy}]   # pure linear scale to 1920×2880")
        lines.append(f"    canonical_anchor: [TBD, TBD]   # FILL: scaled + geographic correction")
        lines.append(f"    correction_note: \"{note}\"")
        lines.append(f"    polygon: TBD   # FILL: province polygon (4-8 vertices)")
        lines.append("")

    lines.append("# Edges from adjacency_map.jsx (canonical adjacency, 26 edges):")
    lines.append("adjacency_edges:")
    for a, b in edges:
        lines.append(f"  - [{a}, {b}]")

    out_path.write_text('\n'.join(lines) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument(
        '--jsx',
        default='designs/world/adjacency_map.jsx',
        help='Path to adjacency_map.jsx (default: designs/world/adjacency_map.jsx)',
    )
    parser.add_argument(
        '--out',
        default='tools/geography/canonical_anchors_stub.yaml',
        help='Output YAML stub path (default: tools/geography/canonical_anchors_stub.yaml)',
    )
    args = parser.parse_args()

    jsx_path = Path(args.jsx)
    out_path = Path(args.out)

    if not jsx_path.exists():
        print(f"ERROR: {jsx_path} not found", file=sys.stderr)
        return 1

    coords = extract_jsx_coords(jsx_path)
    edges = extract_jsx_edges(jsx_path)

    if len(coords) != 17:
        print(
            f"WARNING: expected 17 territories, found {len(coords)}",
            file=sys.stderr,
        )
    if len(edges) != 26:
        print(
            f"WARNING: expected 26 edges, found {len(edges)}",
            file=sys.stderr,
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    emit_yaml_stub(coords, edges, out_path)
    print(f"Wrote {out_path} ({len(coords)} territories, {len(edges)} edges)")

    # Sanity report
    print()
    print(f"Canvas: {JSX_W}×{JSX_H} → {CANONICAL_W}×{CANONICAL_H}")
    print(f"Scale: x×{SCALE_X:.4f}, y×{SCALE_Y:.4f}")
    print(f"Territories: {len(coords)}")
    print(f"Edges: {len(edges)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
