#!/usr/bin/env python3
"""
Coordinate transformation script — geography canon Phase 2 prep
Authority: PP-707 / ED-779

Reads designs/world/adjacency_map.jsx (700×600 abstract canvas) and projects
the 17 territory coordinates to canonical (2400×2880) coordinate system.

Usage:
    python3 01_coord_transform.py
    
Output:
    Stdout: coordinate transform table + Lake Eidursjø position
    File: territory_anchors_canonical.json (machine-readable for execution session)

This script is mechanical and deterministic. Run it once at start of execution
session; results feed directly into territories: section of valoria_geography_v30.yaml.

Settlement-level (x, y) coordinates are NOT produced by this script — only the
17 territory anchors. Settlement placement within territories is manual authoring
work (use territory anchor + offsets per settlement_layer §2.1 narrative).
"""
import re
import json
import os
import sys

# Constants
JSX_W, JSX_H = 700, 600
TARGET_W, TARGET_H = 2400, 2880

# Lake Eidursjø canonical position (decision §1.2 of workplan)
LAKE_EIDURSJO = {
    'shape': 'ellipse',
    'center': [1135, 2263],
    'rx': 200,
    'ry': 150,
    'description': 'East-west barrier in central-south interior',
}

JSX_PATH_DEFAULT = 'designs/world/adjacency_map.jsx'


def project(x, y):
    """Linear scale jsx (x,y) to canonical."""
    return round(x * TARGET_W / JSX_W), round(y * TARGET_H / JSX_H)


def parse_jsx_coords(jsx_text):
    """Extract T# coordinates from adjacency_map.jsx source."""
    pattern = r"T(\d+):\s*\{[^}]*name:\s*'([^']+)'[^}]*control:\s*'([^']+)'[^}]*x:\s*(\d+),\s*y:\s*(\d+)"
    coords = {}
    for m in re.finditer(pattern, jsx_text):
        tnum, name, control, x, y = m.groups()
        coords[f'T{tnum}'] = {
            'name': name,
            'control': control,
            'jsx_x': int(x),
            'jsx_y': int(y),
        }
    return coords


def project_all(coords):
    """Apply projection to all entries; return enriched dict."""
    out = {}
    for tid, d in coords.items():
        cx, cy = project(d['jsx_x'], d['jsx_y'])
        out[tid] = {**d, 'canonical_x': cx, 'canonical_y': cy}
    return out


def inside_ellipse(pt, ellipse):
    """True if point is inside (or on) ellipse defined by center/rx/ry."""
    cx, cy = ellipse['center']
    dx = (pt[0] - cx) / ellipse['rx']
    dy = (pt[1] - cy) / ellipse['ry']
    return dx * dx + dy * dy <= 1


def validate(projected):
    """Smoke checks: no settlement inside lake, all coords in canvas bounds."""
    errors = []
    for tid, d in projected.items():
        x, y = d['canonical_x'], d['canonical_y']
        if not (0 <= x <= TARGET_W):
            errors.append(f'{tid} canonical_x {x} outside canvas [0, {TARGET_W}]')
        if not (0 <= y <= TARGET_H):
            errors.append(f'{tid} canonical_y {y} outside canvas [0, {TARGET_H}]')
        if inside_ellipse((x, y), LAKE_EIDURSJO):
            errors.append(f'{tid} {d["name"]} canonical ({x}, {y}) is inside Lake Eidursjø')
    return errors


def main():
    # Locate jsx
    jsx_path = JSX_PATH_DEFAULT
    if len(sys.argv) > 1:
        jsx_path = sys.argv[1]
    if not os.path.exists(jsx_path):
        # Try common fallbacks
        for fallback in ['adjacency_map.jsx', '/home/claude/_PHASE1_adjacency_map.jsx']:
            if os.path.exists(fallback):
                jsx_path = fallback
                break
        else:
            print(f'ERROR: cannot find {JSX_PATH_DEFAULT} or fallbacks', file=sys.stderr)
            sys.exit(1)

    jsx_text = open(jsx_path).read()
    coords = parse_jsx_coords(jsx_text)
    if not coords:
        print('ERROR: no coordinates parsed from jsx', file=sys.stderr)
        sys.exit(1)

    projected = project_all(coords)

    # Print transform table
    print('=' * 72)
    print('COORDINATE TRANSFORMATION — Phase 2 prep')
    print('=' * 72)
    print(f'Source: {jsx_path} ({JSX_W}×{JSX_H})')
    print(f'Target: canonical ({TARGET_W}×{TARGET_H})')
    print(f'Method: linear scale (x×{TARGET_W}/{JSX_W}, y×{TARGET_H}/{JSX_H})')
    print()
    print(f'{"T#":4} {"Name":<14} {"Faction":<12} {"jsx":>11}  →  {"canonical":>13}')
    print('-' * 72)
    for tid in sorted(projected, key=lambda t: int(t[1:])):
        d = projected[tid]
        print(f'{tid:4} {d["name"]:<14} {d["control"]:<12} '
              f'({d["jsx_x"]:>3},{d["jsx_y"]:>3})  →  '
              f'({d["canonical_x"]:>5},{d["canonical_y"]:>4})')

    print()
    print(f'Lake Eidursjø: center={LAKE_EIDURSJO["center"]}, rx={LAKE_EIDURSJO["rx"]}, ry={LAKE_EIDURSJO["ry"]}')

    # Validate
    errors = validate(projected)
    print()
    if errors:
        print(f'VALIDATION ERRORS ({len(errors)}):')
        for e in errors:
            print(f'  ✗ {e}')
    else:
        print('VALIDATION: ✓ all settlements inside canvas, none inside lake')

    # Write JSON output for execution session
    out_path = 'territory_anchors_canonical.json'
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'canonical_canvas': [TARGET_W, TARGET_H],
                'source': jsx_path,
                'source_canvas': [JSX_W, JSX_H],
                'method': 'linear scale',
            },
            'lake_eidursjo': LAKE_EIDURSJO,
            'territory_anchors': {tid: {
                'name': d['name'],
                'control': d['control'],
                'canonical': [d['canonical_x'], d['canonical_y']],
                'source_jsx': [d['jsx_x'], d['jsx_y']],
            } for tid, d in projected.items()},
        }, f, indent=2)
    print(f'\nMachine-readable output: {out_path}')

    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main())
