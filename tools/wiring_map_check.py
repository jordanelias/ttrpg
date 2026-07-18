#!/usr/bin/env python3
"""
tools/wiring_map_check.py — validate + query the wiring manifest (ED-IN-0074).

The wiring map (designs/audit/2026-07-17-mc-wiring-coverage-audit/wiring_map.html) is a
human view of references/wiring_manifest.yaml. This tool is the machine side: it turns
the map from a static briefing into a work-driver.

  python3 tools/wiring_map_check.py --check       # GATE: every tag resolves; full coverage; valid vocab
  python3 tools/wiring_map_check.py --work-list    # the Godot port work-list, ranked
  python3 tools/wiring_map_check.py --summary      # build-state / godot-status counts
  python3 tools/wiring_map_check.py --json         # machine-readable dump (check + work-list)

--check exits non-zero on any failure, so it can be wired report-only or blocking into CI
(alongside the other tag/name-integrity gates in .github/workflows/valoria-ci.yml).

Durability: because every node is anchored on a registry TAG (module/adapter name), a tag
that stops resolving — e.g. a module renamed or a cross_scale adapter moved — is a CAUGHT
ERROR here, not silent drift in the HTML.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "references", "wiring_manifest.yaml")


def _load_yaml(path):
    try:
        import yaml
    except ImportError:
        sys.exit("wiring_map_check: PyYAML required (pip install pyyaml)")
    with open(path) as f:
        return yaml.safe_load(f)


def load_registries(man):
    """Return the live authoritative tag sets, read from the paths the manifest declares."""
    reg = man["registries"]
    modpath = os.path.join(ROOT, reg["module"])
    modules = set(re.findall(r"^  - module:\s*(\S+)", open(modpath).read(), re.M))
    adir = os.path.join(ROOT, reg["adapter"])
    adapters = {f[:-3] for f in os.listdir(adir) if f.endswith(".py") and not f.startswith("__")}
    kpath = os.path.join(ROOT, reg["key"])
    keys = set(re.findall(r"\b(?:da|env|scene|state|meta|mechanical)\.[a-z_]+", open(kpath).read()))
    return {"module": modules, "adapter": adapters, "key": keys}


def validate(man, reg):
    """Return a list of failures (empty == green)."""
    fails = []
    builds, godots = set(man["build_states"]), set(man["godot_states"])
    man_mods = set(man["modules"]); man_ads = set(man["adapters"])

    # 1) every tag resolves in its live registry
    for name in man_mods:
        if name not in reg["module"]:
            fails.append(f"module tag does not resolve in module_contracts: {name}")
    for name in man_ads:
        if name not in reg["adapter"]:
            fails.append(f"adapter tag does not resolve in engine/cross_scale/: {name}")

    # 2) full coverage (map must represent the whole contract spine + adapter seam)
    missing_m = reg["module"] - man_mods
    if missing_m:
        fails.append(f"module coverage {len(man_mods)}/{len(reg['module'])} — MISSING: {sorted(missing_m)}")
    missing_a = reg["adapter"] - man_ads
    if missing_a:
        fails.append(f"adapter coverage {len(man_ads)}/{len(reg['adapter'])} — MISSING: {sorted(missing_a)}")

    # 3) valid vocabulary on every entry
    for kind, entries in (("module", man["modules"]), ("adapter", man["adapters"])):
        for name, e in entries.items():
            if e.get("build") not in builds:
                fails.append(f"{kind}:{name} bad build_state {e.get('build')!r}")
            if e.get("godot") not in godots:
                fails.append(f"{kind}:{name} bad godot_state {e.get('godot')!r}")
    return fails


def all_entries(man):
    for kind, entries in (("module", man["modules"]), ("adapter", man["adapters"])):
        for name, e in entries.items():
            yield kind, name, e


def work_list(man):
    """Ranked Godot port work-list: what has a Python oracle but no GDScript yet."""
    portable = sorted(
        [(name, kind, e) for kind, name, e in all_entries(man) if e["godot"] == "python-oracle"],
        key=lambda t: (t[2].get("port_rank", 5), t[0]),
    )
    blocked = sorted(
        [(name, kind, e) for kind, name, e in all_entries(man) if e["godot"] == "no-oracle"],
        key=lambda t: t[0],
    )
    ported = [(name, e) for kind, name, e in all_entries(man) if e["godot"] in ("gd-ported", "typed-exported")]
    retire = [name for kind, name, e in all_entries(man) if e["godot"] == "retire"]
    return portable, blocked, ported, retire


def map_json(man):
    """The embeddable block the HTML map's `const PORT` is generated from.

    Keeping the human map's godot axis sourced from this — not hand-annotated — is what
    stops it drifting from the gate. Regenerate the HTML block with:
        python3 tools/wiring_map_check.py --emit-map-json
    """
    from collections import Counter
    def rec(e):
        return {k: e.get(k) for k in ("tier", "scale", "resolver", "build", "godot", "port_rank", "parity", "note")}
    return {
        "as_of": man.get("as_of"),
        "golden_path": man.get("golden_path"),
        "modules": {n: rec(e) for _, n, e in all_entries(man) if e["tier"] == "module"},
        "adapters": {n: rec(e) for _, n, e in all_entries(man) if e["tier"] == "adapter"},
        "foundation_gaps": man.get("foundation_gaps", {}),
        "build_counts": dict(Counter(e["build"] for _, _, e in all_entries(man))),
        "godot_counts": dict(Counter(e["godot"] for _, _, e in all_entries(man))),
    }


def cmd_worklist(man):
    portable, blocked, ported, retire = work_list(man)
    print("═══ GODOT PORT WORK-LIST ═══  (source: references/wiring_manifest.yaml)\n")
    print(f"✓ ALREADY PORTED ({len(ported)}): " + ", ".join(n for n, _ in ported) + "  — the golden path template\n")
    print(f"▶ NEXT — has a Python oracle, no GDScript yet ({len(portable)}), ranked:")
    for name, kind, e in portable:
        print(f"   [{e.get('port_rank')}] {kind:7} {name:20} {e['build']:9} parity:{e.get('parity','?'):12} {e.get('note','')}")
    print(f"\n⛔ BLOCKED — no oracle; author canon first ({len(blocked)}):")
    for name, kind, e in blocked:
        print(f"       {kind:7} {name:20} {e['build']:9} {e.get('note','')}")
    if retire:
        print(f"\n🗑  RETIRE (do not port): {', '.join(retire)}")
    fg = man.get("foundation_gaps", {})
    if fg:
        print("\n⚠ FOUNDATION GAPS (block whole tiers, not single units):")
        for k, v in fg.items():
            print(f"       {k}: {v.get('note','')}")


def cmd_summary(man, reg):
    from collections import Counter
    b = Counter(e["build"] for _, _, e in all_entries(man))
    g = Counter(e["godot"] for _, _, e in all_entries(man))
    print(f"coverage: {len(man['modules'])}/{len(reg['module'])} modules · {len(man['adapters'])}/{len(reg['adapter'])} adapters")
    print("build-state: " + " · ".join(f"{k}:{v}" for k, v in b.most_common()))
    print("godot-status: " + " · ".join(f"{k}:{v}" for k, v in g.most_common()))
    portable = [n for _, n, e in all_entries(man) if e["godot"] == "python-oracle"]
    print(f"port surface: {len(portable)} units have a Python oracle awaiting GDScript "
          f"(vs 1 ported); the rest need canon authored first.")


def main():
    ap = argparse.ArgumentParser(description="Validate + query the Valoria wiring manifest.")
    ap.add_argument("--check", action="store_true", help="validate tags/coverage/vocab; exit 1 on failure (CI gate)")
    ap.add_argument("--work-list", dest="worklist", action="store_true", help="ranked Godot port work-list")
    ap.add_argument("--summary", action="store_true", help="build-state / godot-status counts")
    ap.add_argument("--json", action="store_true", help="machine-readable dump")
    ap.add_argument("--emit-map-json", dest="emitmap", action="store_true",
                    help="print the embeddable PORT block the HTML map is generated from")
    args = ap.parse_args()
    if not any((args.check, args.worklist, args.summary, args.json, args.emitmap)):
        args.check = True  # default action is the gate

    man = _load_yaml(MANIFEST)
    reg = load_registries(man)
    fails = validate(man, reg)

    if args.emitmap:
        print(json.dumps(map_json(man), indent=1, ensure_ascii=False))
        return 0 if not fails else 1

    if args.json:
        portable, blocked, ported, retire = work_list(man)
        print(json.dumps({
            "ok": not fails, "failures": fails,
            "coverage": {"modules": [len(man["modules"]), len(reg["module"])],
                         "adapters": [len(man["adapters"]), len(reg["adapter"])]},
            "work_list": {"next": [n for n, _, _ in portable],
                          "blocked": [n for n, _, _ in blocked],
                          "ported": [n for n, _ in ported], "retire": retire},
        }, indent=2))
        return 0 if not fails else 1

    if args.summary:
        cmd_summary(man, reg)
    if args.worklist:
        cmd_worklist(man)
    if args.check or not (args.summary or args.worklist):
        if fails:
            print("✗ wiring manifest FAILED validation:")
            for f in fails:
                print("   -", f)
            return 1
        print(f"✓ wiring manifest valid — {len(man['modules'])}/{len(reg['module'])} modules · "
              f"{len(man['adapters'])}/{len(reg['adapter'])} adapters · all tags resolve in their live registries.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
