#!/usr/bin/env python3
"""export_sim_params.py — extract the typed computational constants from the Python sim code
into one queryable surface (Repository State Armature, values layer, ED-IN-0079).

The values/formulae the game actually computes with live as typed module-scope constants in the
sim reference code (systems/*/sim, engine, sim/*) — the 1:1 Python reference the Godot port
validates against (CLAUDE.md §7). Only combat's were ever exported (combat_engine_v1.json). This
generalizes that: AST-read every module-scope numeric/collection constant (NO fabrication — it
reads the Python literal, never invents a value) with its source file and any inline provenance
comment, into engine/engine_params/sim_params.json.

Each record: {key, name, value, kind, module, file, note}. `value` is the literal-evaluated Python
constant; `note` is the trailing inline comment (often the [canonical: …]/ED-/PP- cite). The line
number is intentionally not stored (it churns on unrelated edits); provenance is file + note.

CLI:
  python3 tools/export_sim_params.py --build     # regenerate engine/engine_params/sim_params.json
  python3 tools/export_sim_params.py --check      # drift gate: committed == fresh extract (exit 1 on drift)
  python3 tools/export_sim_params.py --search TN  # find constants by name/module substring
"""
from __future__ import annotations
import argparse
import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "engine" / "engine_params" / "sim_params.json"

# The sim reference surfaces (the computational truth). Combat keeps its own dedicated export.
SCAN_DIRS = [
    "systems/factions/sim", "systems/social_contest/sim", "systems/mass_battle/sim",
    "systems/threadwork/sim", "systems/world/sim", "systems/settlements/sim",
    "systems/fieldwork/sim", "systems/combat/sim", "systems/characters/sim", "systems/overview/sim", "engine",
]


def _literal(node):
    """Return the Python value if node is a pure literal (num/str/bool/None or a collection of
    those), else None. ast.literal_eval is the anti-fabrication guard — non-literals are skipped."""
    try:
        return ast.literal_eval(node)
    except (ValueError, SyntaxError, TypeError):
        return None


def _is_numericish(v) -> bool:
    """Keep numeric constants and collections that CONTAIN numbers (the mechanical params);
    skip pure-string constants (labels, keys) which aren't values/formulae."""
    if isinstance(v, bool):
        return False
    if isinstance(v, (int, float)):
        return True
    if isinstance(v, (list, tuple, set)):
        return any(_is_numericish(x) for x in v)
    if isinstance(v, dict):
        return any(_is_numericish(x) for x in v.values())
    return False


def _jsonsafe(v):
    """Coerce a literal to a JSON-serializable form WITHOUT changing its numbers: tuples→lists,
    sets→sorted lists, and dict keys that aren't str/num→str(key) (sim code sometimes keys dicts
    by tuples, e.g. transition matrices). Faithful to the values; only the container shape is normalized."""
    if isinstance(v, dict):
        return {(k if isinstance(k, (str, int, float, bool)) else str(k)): _jsonsafe(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_jsonsafe(x) for x in v]
    if isinstance(v, set):
        return sorted((_jsonsafe(x) for x in v), key=lambda z: str(z))
    return v


def _kind(v) -> str:
    if isinstance(v, (int, float)):
        return "scalar"
    if isinstance(v, dict):
        return "table"
    if isinstance(v, (list, tuple, set)):
        return "vector"
    return "other"


def _comment(src_lines: list[str], lineno: int) -> str:
    """The trailing inline `# …` comment on the assignment's line (provenance/cite), if any."""
    if 0 < lineno <= len(src_lines):
        line = src_lines[lineno - 1]
        h = line.find("#")
        if h != -1:
            return line[h + 1:].strip()
    return ""


def _subsystem(p: Path) -> str:
    """The subsystem a sim file belongs to — links values back to the pointers/module map.
    systems/<sub>/sim/... -> <sub>; engine/<x>/... -> engine.<x>; sim/<x>/... -> personal.<x>."""
    parts = p.relative_to(ROOT).parts
    if parts[0] == "systems" and len(parts) > 1:
        return parts[1]
    if parts[0] == "engine":
        return "engine." + parts[1].replace(".py", "") if len(parts) > 2 else "engine"
    if parts[0] == "sim" and len(parts) > 1:
        return "sim." + parts[1]
    return parts[-2] if len(parts) > 1 else "root"


def _iter_py_files():
    seen = set()
    for d in SCAN_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            # Skip test files: their fixture constants (GOLDEN_WINNERS, etc.) are not
            # engine params. (Before the sim/ hollow-out these lived under sim/tests/,
            # which was never in SCAN_DIRS; now under engine/tests/ they must stay excluded.)
            if "tests" in p.parts or p.name.startswith("test_") or "__pycache__" in p.parts or p in seen:
                continue
            seen.add(p)
            yield p


def build() -> dict:
    records = []
    for p in _iter_py_files():
        rel = str(p.relative_to(ROOT))
        module = _subsystem(p)
        try:
            src = p.read_text(encoding="utf-8")
            tree = ast.parse(src)
        except (SyntaxError, UnicodeDecodeError):
            continue
        src_lines = src.splitlines()
        for node in tree.body:  # MODULE-SCOPE assignments only (top-level params)
            if not isinstance(node, ast.Assign) or len(node.targets) != 1:
                continue
            tgt = node.targets[0]
            if not isinstance(tgt, ast.Name):
                continue
            val = _literal(node.value)
            if val is None or not _is_numericish(val):
                continue
            records.append({
                "key": f"{module}.{tgt.id}",
                "name": tgt.id,
                "value": _jsonsafe(val),
                "kind": _kind(val),
                "module": module,
                "file": rel,   # line number deliberately NOT stored — it churns on unrelated edits;
                "note": _comment(src_lines, node.lineno),  # provenance travels in file + note (cite)
            })
    records.sort(key=lambda r: (r["file"], r["name"]))
    from collections import Counter
    by_module = Counter(r["module"] for r in records)
    return {
        "_generated": "GENERATED by tools/export_sim_params.py — the typed computational constants "
                      "read (AST literal) from the sim reference code. No value is invented. "
                      "Regenerate with --build; drift-gated by --check.",
        "schema_version": 1,
        "count": len(records),
        "by_module": dict(by_module),
        "params": records,
    }


def _serialize(state: dict) -> str:
    return json.dumps(state, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def write() -> Path:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(_serialize(build()), encoding="utf-8")
    return OUT


def check() -> tuple[bool, list[str]]:
    if not OUT.exists():
        return False, ["sim_params.json missing — run `export_sim_params.py --build`"]
    fresh = _serialize(build())
    if OUT.read_text(encoding="utf-8") != fresh:
        return False, ["DRIFT: committed sim_params.json != fresh extract — run --build and commit"]
    return True, []


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--search", metavar="TERM")
    args = ap.parse_args(argv)
    if args.build:
        p = write()
        s = json.loads(p.read_text())
        print(f"wrote {p.relative_to(ROOT)} — {s['count']} constants across {len(s['by_module'])} modules")
        return 0
    if args.check:
        ok, msgs = check()
        for m in msgs:
            print("  - " + m, file=sys.stderr)
        print("[SIM-PARAMS] current" if ok else "[SIM-PARAMS] FAILED", file=sys.stdout if ok else sys.stderr)
        return 0 if ok else 1
    if args.search:
        q = args.search.lower()
        data = json.loads(OUT.read_text()) if OUT.exists() else {"params": []}
        hits = [r for r in data["params"] if q in r["name"].lower() or q in r["module"].lower()]
        for r in hits[:60]:
            print(f"  {r['key']:38} = {json.dumps(r['value'])[:50]:52} {r['file']}"
                  + (f"  # {r['note'][:50]}" if r["note"] else ""))
        print(f"\n{len(hits)} match(es)")
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
