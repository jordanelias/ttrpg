#!/usr/bin/env python3
"""
tools/observability/build_graph.py — Valoria propagation-graph extractor.

Reads the canonical machine-readable design sources and emits ONE normalized
graph that makes the engine's data flow transparent: which systems emit/consume
which Keys, which scalars each system owns (and how it derives / gates on them),
and how effects ripple across scales.

Sources (canon-over-memory; nothing is invented — every node/edge traces to a file):
  - references/module_contracts.yaml          : the IN(Keys) -> resolver -> OUT(Keys)
                                                 wrapper contracts + owned scalar state
                                                 + gates + derivations + transitions
  - designs/architecture/key_type_registry_v30.md : authoritative Key metadata
                                                 (family, scale, permanence, routing)
  - canon/mechanics_index.yaml                : scale / GD-constraint / sim_module enrichment

Output:
  - tools/observability/graph_data.js  : `window.VALORIA_GRAPH = {...}` (loaded by index.html
                                          via <script src> so the viewer opens offline, no server)
  - tools/observability/graph.json     : same payload as plain JSON (for tooling / diffing)

Run:  python tools/observability/build_graph.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parents[2]
CONTRACTS = REPO / "references" / "module_contracts.yaml"
REGISTRY = REPO / "designs" / "architecture" / "key_type_registry_v30.md"
MECHANICS = REPO / "canon" / "mechanics_index.yaml"
OUT_DIR = Path(__file__).resolve().parent

# --- Vocabulary reconciliation -------------------------------------------------
# Canon carries a known registry-system <-> module-name drift (module-adjudicator
# discipline keeps both visible). We normalize to the module id for accurate ripple
# tracing, but record every substitution in meta.naming_alerts so nothing is hidden.
SYSTEM_ALIASES = {
    "articulation": "articulation_layer",
    "da_framework": "domain_actions",
    "faction_layer": "faction_state",
    "fieldwork": "fieldwork_knots",
    "conviction_track": "piety_track",
    "substrate (auto)": "engine",
    "engine": "engine",
}
# Sentinel emitter/consumer strings that are NOT specific systems.
BROADCAST_SENTINELS = {"all", "all subscribing systems"}
DROP_SENTINELS = {"legacy-aware consumers only"}
# F2-class key-name drift: an emit string whose family-prefixed name differs from the
# canonical registry subtype name. Reconciled for ripple continuity; alert recorded.
KEY_ALIASES = {
    "scene_outcome.battle_concluded": "scene.battle_concluded",
}
FULLSTREAM = "*"  # a `consumes: {type: "*"}` means "subscribes to the entire Key stream"


# ----------------------------------------------------------------------------
# Parse the Key Type Registry (markdown with per-type YAML blocks)
# ----------------------------------------------------------------------------
def parse_key_registry(path: Path) -> dict:
    """Return {type_id: {family, description, scale_signature, permanence, cls,
                         emitting_systems, consuming_systems}}."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    keys: dict[str, dict] = {}
    family = None
    fam_re = re.compile(r"Family:\s*([a-z_]+)", re.I)
    type_re = re.compile(r"^###\s+([a-z_]+\.[a-z_]+)\s*$")
    i = 0
    while i < len(lines):
        line = lines[i]
        m_fam = fam_re.search(line) if line.startswith("##") else None
        if m_fam:
            family = m_fam.group(1)
            i += 1
            continue
        m_type = type_re.match(line)
        if m_type:
            type_id = m_type.group(1)
            # find the next ```yaml fenced block
            j = i + 1
            block: list[str] = []
            in_block = False
            while j < len(lines):
                lj = lines[j]
                if not in_block and lj.strip().startswith("```"):
                    in_block = True
                    j += 1
                    continue
                if in_block and lj.strip().startswith("```"):
                    break
                if in_block:
                    block.append(lj)
                # stop if we hit the next type/family before any block
                if not in_block and (type_re.match(lj) or (lj.startswith("##") and fam_re.search(lj))):
                    j -= 1
                    break
                j += 1
            data = {}
            if block:
                try:
                    data = yaml.safe_load("\n".join(block)) or {}
                except yaml.YAMLError:
                    data = {}
            keys[type_id] = {
                "family": family or type_id.split(".")[0],
                "description": (data.get("description") or "").strip(),
                "scale_signature": data.get("default_scale_signature") or [],
                "permanence": data.get("default_permanence") or "",
                "time_horizon": data.get("default_time_horizon") or "",
                "cls": str(data.get("class") or "A"),
                "emitting_systems": data.get("emitting_systems") or [],
                "consuming_systems": data.get("consuming_systems") or [],
            }
            i = j
        i += 1
    return keys


# ----------------------------------------------------------------------------
# Parse the mechanics index (scale / constraints / sim module per mechanic)
# ----------------------------------------------------------------------------
def parse_mechanics(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return {}
    out = {}
    for name, e in (raw.get("mechanics") or {}).items():
        if not isinstance(e, dict):
            continue
        out[name] = {
            "scale": e.get("scale", ""),
            "faction": e.get("faction", "universal"),
            "sim_module": e.get("sim_module", ""),
            "test_status": e.get("test_status", ""),
            "gd_constraints": e.get("gd_constraints", []) or [],
            "canon_sources": e.get("canon_sources", []) or [],
        }
    return out


# ----------------------------------------------------------------------------
# Build the normalized graph
# ----------------------------------------------------------------------------
def gate_target(gate: dict) -> tuple[str, list]:
    """Return ('on'|'reads', value) for a gate, tolerating YAML bool coercion of 'on'."""
    for k in ("on", True):
        if k in gate and gate[k]:
            return "on", gate[k] if isinstance(gate[k], list) else [gate[k]]
    if gate.get("reads"):
        r = gate["reads"]
        return "reads", r if isinstance(r, list) else [r]
    return "", []


def scalar_id(system: str, name: str) -> str:
    return f"{system}::{name}"


def _clean_name(name: str) -> str:
    """Strip parentheticals and ' / Procedure X' qualifiers from a system reference."""
    n = re.sub(r"\([^)]*\)", "", name)
    n = re.split(r"\s*/\s*", n)[0]
    return n.strip()


def build():
    contracts_raw = yaml.safe_load(CONTRACTS.read_text(encoding="utf-8"))
    modules = contracts_raw.get("modules", [])
    accounting_sequence = contracts_raw.get("accounting_sequence", [])
    registry = parse_key_registry(REGISTRY)
    mechanics = parse_mechanics(MECHANICS)

    systems: dict[str, dict] = {}
    keys: dict[str, dict] = {}
    scalars: dict[str, dict] = {}
    edges: list[dict] = []
    scales: set[str] = set()
    naming_alerts: list[dict] = []
    _alert_seen: set[tuple] = set()

    def alert(kind: str, original: str, resolved: str, note: str = ""):
        sig = (kind, original, resolved)
        if sig not in _alert_seen:
            _alert_seen.add(sig)
            naming_alerts.append({"kind": kind, "original": original,
                                  "resolved": resolved, "note": note})

    # auto registry_system -> module-id map (from the contracts themselves)
    auto_alias = {}
    module_ids = {m.get("module") for m in modules if m.get("module")}
    for m in modules:
        rs = _clean_name(m.get("registry_system") or "")
        if rs and rs not in module_ids:
            auto_alias.setdefault(rs, m.get("module"))

    def resolve_system(name: str):
        """Return canonical system id, or None for broadcast/drop sentinels."""
        if not name:
            return None
        if name in BROADCAST_SENTINELS:
            return None  # caller marks the key broadcast
        if name in DROP_SENTINELS:
            return None
        clean = _clean_name(name)
        if clean in module_ids:
            return clean
        if name in SYSTEM_ALIASES:
            r = SYSTEM_ALIASES[name]
            alert("system", name, r)
            return r
        if clean in SYSTEM_ALIASES:
            r = SYSTEM_ALIASES[clean]
            alert("system", name, r)
            return r
        if clean in auto_alias:
            r = auto_alias[clean]
            if r != name:
                alert("system", name, r, "registry_system->module")
            return r
        # unknown -> registry-only stub (kept visible, flagged)
        if clean and clean != FULLSTREAM:
            return clean
        return None

    def resolve_key(kid: str):
        if kid in KEY_ALIASES:
            r = KEY_ALIASES[kid]
            alert("key", kid, r, "F2 family-prefix drift")
            return r
        return kid

    def ensure_key(kid: str):
        if kid not in keys:
            reg = registry.get(kid, {})
            keys[kid] = {
                "id": kid,
                "family": reg.get("family") or kid.split(".")[0],
                "description": reg.get("description", ""),
                "scale_signature": reg.get("scale_signature", []),
                "permanence": reg.get("permanence", ""),
                "cls": reg.get("cls", ""),
                "registered": kid in registry,
                "broadcast": False,
                "emitters": set(),
                "consumers": set(),
            }
            for s in reg.get("scale_signature", []):
                scales.add(s)
        return keys[kid]

    # Seed every registered key (so unwired-but-registered keys still show)
    for kid in registry:
        ensure_key(kid)

    for mod in modules:
        sid = mod.get("module")
        if not sid:
            continue
        mech = mechanics.get(mod.get("registry_system") or sid) or mechanics.get(sid) or {}
        mod_scales = mod.get("scales") or ([mech.get("scale")] if mech.get("scale") else [])
        for s in mod_scales:
            if s:
                scales.add(s)
        systems[sid] = {
            "id": sid,
            "full_stream": False,
            "registry_only": False,
            "registry_system": mod.get("registry_system") or sid,
            "doc": mod.get("doc"),
            "resolver": mod.get("resolver", ""),
            "scales": mod_scales,
            "status": mod.get("status", ""),
            "accounting_phase": mod.get("accounting_phase", []) or [],
            "transitions": [t.get("via") for t in (mod.get("transitions") or []) if isinstance(t, dict)],
            "loops": mod.get("loops", []) or [],
            "gap_notes": mod.get("gap_notes", []) or [],
            "sources": mod.get("sources", []) or [],
            "gd_constraints": mech.get("gd_constraints", []),
            "sim_module": mech.get("sim_module", ""),
            "test_status": mech.get("test_status", ""),
            "emits": [],
            "consumes": [],
            "state": [],
            "gates": mod.get("gates", []) or [],
            "derivations": mod.get("derivations", []) or [],
        }

        for em in mod.get("emits") or []:
            kid = resolve_key(em.get("type") or "")
            if not kid or kid == FULLSTREAM:
                continue
            ensure_key(kid)["emitters"].add(sid)
            systems[sid]["emits"].append({"type": kid, "terminal": bool(em.get("terminal"))})
            edges.append({"src": sid, "dst": kid, "kind": "emits",
                          "terminal": bool(em.get("terminal"))})

        for co in mod.get("consumes") or []:
            raw = co.get("type")
            if raw == FULLSTREAM:
                systems[sid]["full_stream"] = True
                continue
            kid = resolve_key(raw or "")
            if not kid:
                continue
            ensure_key(kid)["consumers"].add(sid)
            frm_raw = co.get("from") or []
            if isinstance(frm_raw, str):
                frm_raw = [frm_raw]
            frm = []
            for f in frm_raw:
                rf = resolve_system(f) if isinstance(f, str) else None
                if rf and rf not in frm:
                    frm.append(rf)
            systems[sid]["consumes"].append({"type": kid, "from": frm})
            edges.append({"src": kid, "dst": sid, "kind": "consumes"})

        for st in mod.get("state") or []:
            nm = st.get("name")
            if not nm:
                continue
            scid = scalar_id(sid, nm)
            scalars[scid] = {
                "id": scid, "name": nm, "owner": sid,
                "bucket": st.get("bucket", ""), "writable": bool(st.get("writable")),
                "derived_by": [], "gated_by": [], "read_by": [],
            }
            systems[sid]["state"].append({"name": nm, "bucket": st.get("bucket", ""),
                                          "writable": bool(st.get("writable")), "scalar_id": scid})
            edges.append({"src": sid, "dst": scid, "kind": "owns"})

        # derivations: output scalar computed from inputs
        for dv in mod.get("derivations") or []:
            out_name = dv.get("output")
            if not out_name:
                continue
            scid = scalar_id(sid, out_name)
            if scid in scalars:
                scalars[scid]["derived_by"].append(dv.get("formula", ""))
            edges.append({"src": sid, "dst": scid, "kind": "derives",
                          "formula": dv.get("formula", ""), "inputs": dv.get("inputs", "")})

        # gates: a system threshold firing on / reading a scalar
        for g in mod.get("gates") or []:
            kind, targets = gate_target(g)
            for tnm in targets:
                # gate target may be an in-module scalar name or a free-text quantity
                scid = scalar_id(sid, tnm) if kind == "on" else None
                rec = {"system": sid, "id": g.get("id"), "when": g.get("when"),
                       "then": g.get("then"), "source": g.get("source"), "kind": kind, "target": tnm}
                if scid and scid in scalars:
                    scalars[scid]["gated_by"].append(rec)
                    edges.append({"src": sid, "dst": scid, "kind": "gates", "gate": g.get("id")})
                else:
                    # cross-module / unowned read — record as a loose gate edge to a scalar if we can match by name later
                    edges.append({"src": sid, "dst": f"quantity::{tnm}", "kind": kind,
                                  "gate": g.get("id")})

    # cross-validate registry routing onto systems that may not be in contracts
    for kid, reg in registry.items():
        if kid not in keys:
            continue
        k = keys[kid]
        for s in reg.get("emitting_systems", []):
            if not isinstance(s, str):
                continue
            rs = resolve_system(s)
            if rs:
                k["emitters"].add(rs)
        for s in reg.get("consuming_systems", []):
            if not isinstance(s, str):
                continue
            if s.strip().startswith("all") or s in BROADCAST_SENTINELS:
                k["broadcast"] = True
                continue
            rs = resolve_system(s)
            if rs:
                k["consumers"].add(rs)

    # synthesize any referenced-but-undeclared system as a flagged stub (keep visible)
    referenced = set()
    for k in keys.values():
        referenced |= set(k["emitters"]) | set(k["consumers"])
    for scid in scalars:
        referenced.add(scalars[scid]["owner"])
    for sid in sorted(referenced):
        if sid not in systems:
            systems[sid] = {
                "id": sid, "full_stream": False, "registry_only": True,
                "registry_system": sid, "doc": None,
                "resolver": "kernel" if sid == "engine" else "",
                "scales": ["system_meta"] if sid == "engine" else [],
                "status": "synthetic" if sid == "engine" else "registry-only",
                "accounting_phase": [], "transitions": [], "loops": [],
                "gap_notes": ["substrate / kernel auto-emitter" if sid == "engine"
                              else "referenced in routing but has no module contract"],
                "sources": [], "gd_constraints": [], "sim_module": "", "test_status": "",
                "emits": [], "consumes": [], "state": [], "gates": [], "derivations": [],
            }
            if sid != "engine":
                alert("system", sid, sid, "registry-only (no contract)")

    # link gates to the Keys they fire (scan when/then text for canonical key ids)
    key_token = re.compile(r"\b([a-z_]+\.[a-z_]+)\b")
    for s in systems.values():
        for g in s.get("gates", []):
            txt = f"{g.get('when', '')} {g.get('then', '')}"
            hits = sorted({resolve_key(t) for t in key_token.findall(txt)
                           if resolve_key(t) in keys})
            if hits:
                g["emits_keys"] = hits

    # finalize sets -> sorted lists
    for k in keys.values():
        k["emitters"] = sorted(k["emitters"])
        k["consumers"] = sorted(k["consumers"])

    # closure stats
    n_emit_closed = sum(1 for k in keys.values() if k["emitters"])
    n_consume_closed = sum(1 for k in keys.values() if k["consumers"])
    orphan_emits = sorted(k["id"] for k in keys.values()
                          if k["emitters"] and not k["consumers"] and not k.get("broadcast"))
    unemitted = sorted(k["id"] for k in keys.values() if k["consumers"] and not k["emitters"])

    families = sorted({k["family"] for k in keys.values()})
    payload = {
        "meta": {
            "generated_from": [str(CONTRACTS.relative_to(REPO)).replace("\\", "/"),
                               str(REGISTRY.relative_to(REPO)).replace("\\", "/"),
                               str(MECHANICS.relative_to(REPO)).replace("\\", "/")],
            "contracts_schema_version": contracts_raw.get("schema_version"),
            "contracts_status": contracts_raw.get("status"),
            "accounting_sequence": accounting_sequence,
            "naming_alerts": naming_alerts,
            "full_stream_systems": sorted(s["id"] for s in systems.values() if s.get("full_stream")),
            "broadcast_keys": sorted(k["id"] for k in keys.values() if k.get("broadcast")),
            "stats": {
                "systems": len(systems),
                "keys": len(keys),
                "key_families": len(families),
                "scalars": len(scalars),
                "scales": len(scales),
                "edges": len(edges),
                "keys_with_emitter": n_emit_closed,
                "keys_with_consumer": n_consume_closed,
                "orphan_emits": orphan_emits,
                "unemitted_consumes": unemitted,
                "naming_alerts": len(naming_alerts),
            },
        },
        "systems": sorted(systems.values(), key=lambda s: s["id"]),
        "keys": sorted(keys.values(), key=lambda k: k["id"]),
        "families": families,
        "scalars": sorted(scalars.values(), key=lambda s: s["id"]),
        "scales": sorted(scales),
        "edges": edges,
    }
    return payload


def main():
    payload = build()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "graph.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    data_js = "window.VALORIA_GRAPH = " + json.dumps(payload, separators=(",", ":")) + ";"
    js = "// AUTO-GENERATED by tools/observability/build_graph.py — do not hand-edit.\n" + data_js + "\n"
    (OUT_DIR / "graph_data.js").write_text(js, encoding="utf-8")

    # build lexicon + decision register + archive cross-ref (each reads the prior outputs)
    for mod in ("build_lexicon", "build_decisions", "build_archive_xref"):
        try:
            __import__(mod).main()
        except Exception as e:  # additive — never block the graph build
            print(f"  ({mod} skipped: {e})")

    def _read(name):
        p = OUT_DIR / name
        return p.read_text(encoding="utf-8") if p.exists() else ""
    lex_js, dec_js = _read("lexicon_data.js"), _read("decisions_data.js")

    # self-contained single-file bundle (data inlined) for zero-friction double-click
    index = OUT_DIR / "index.html"
    if index.exists():
        html = index.read_text(encoding="utf-8")
        html = html.replace('<script src="graph_data.js"></script>',
                            "<script>/*inlined*/" + data_js + "</script>")
        html = html.replace('<script src="lexicon_data.js"></script>',
                            "<script>/*inlined*/" + lex_js + "</script>")
        html = html.replace('<script src="decisions_data.js"></script>',
                            "<script>/*inlined*/" + dec_js + "</script>")
        (OUT_DIR / "console.html").write_text(html, encoding="utf-8")

    s = payload["meta"]["stats"]
    print("Valoria propagation graph built:")
    print(f"  systems={s['systems']}  keys={s['keys']} ({s['key_families']} families)"
          f"  scalars={s['scalars']}  scales={s['scales']}  edges={s['edges']}")
    print(f"  key emit-closure={s['keys_with_emitter']}/{s['keys']}"
          f"  consume-closure={s['keys_with_consumer']}/{s['keys']}")
    print(f"  orphan emits (no consumer): {len(s['orphan_emits'])}")
    print(f"  unemitted consumes (read but never emitted): {len(s['unemitted_consumes'])}")
    print(f"  -> {OUT_DIR / 'graph_data.js'}")
    print(f"  -> {OUT_DIR / 'graph.json'}")
    if (OUT_DIR / 'console.html').exists():
        print(f"  -> {OUT_DIR / 'console.html'}  (self-contained — double-click to open)")


if __name__ == "__main__":
    main()
