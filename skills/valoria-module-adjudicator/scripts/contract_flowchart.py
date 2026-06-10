#!/usr/bin/env python3
"""contract_flowchart.py — derived views over references/module_contracts.yaml.

Emits three artifacts (regenerable; never hand-edit the outputs):
  module_flowchart.mermaid   Key-flow topology, scale-grouped, seams marked
  state_graph.mermaid        state quantities + writers + derivations + gates
  module_map_flat.md         consolidated doc: both graphs + era state machine
                             + flattened input/mechanic/gate/output tables

Graph content is generated from the contracts; the gates / derivations /
sequence data below are authored transcriptions from the cited canon reads
(provenance inline). Stage-3 companion to contract_adjudicator.py.
"""
import os
import sys
import argparse
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contract_adjudicator import _pat_overlap, parse_registry_types

UNREG_MARK = " [unreg]"

# ── authored, canon-grounded reference data ─────────────────────────────────

GATES = [
    # (id, condition, consequence, source)
    ("g_ci100", "CI = 100", "Theocracy Unification attempt", "ci_political_v30 §2.2"),
    ("g_cicap", "seasonal CI cap", "CI gain bounded per season", "ci_political_v30 §2.4"),
    ("g_ip100", "IP = 100", "Occupation Phase 1 (first pass)", "victory_v30 §5.2"),
    ("g_ip85", "IP ≥ 85 for 3 seasons", "Occupation Phase 2 (Schoenland)", "victory_v30 §5.2"),
    ("g_ip80", "IP ≥ 80 for 3 more seasons", "Occupation Phase 3 (NW pass)", "victory_v30 §5.2"),
    ("g_ipfall", "IP < 85 (P1) / < 75 (P2)", "invasion stalls / corridor abandoned", "victory_v30 §5.2"),
    ("g_ms0", "MS = 0", "Post-Calamity Era", "victory_v30 §5.1"),
    ("g_ms5", "MS ≤ 5 sustained 10 seasons", "Second Calamity (true terminal)", "victory_v30 §5.1"),
    ("g_msrec", "MS restored to 20 within 10 seasons", "Post-Calamity recovery", "victory_v30 §5.1"),
    ("g_diss", "all factions dissolved", "Anarchy Era (Ministry continues)", "victory_v30 §5.3"),
    ("g_ord0", "settlement Order = 0", "local revolt", "settlement_layer_v30 §1.3"),
    ("g_def0", "settlement Defense = 0", "undefended — auto-capture", "settlement_layer_v30 §1.3"),
    ("g_dv0", "derived value = 0 held through Accounting", "owning stat −1 (same rule as faction stats)",
     "settlement_layer_v30 §1.3"),
    ("g_scar3", "Scars on Conviction X ≥ 3", "Conviction crisis on X (d6 crisis table, 1 season)",
     "conviction_track_v1 §2 (PP-718 per-Conviction)"),
    ("g_scar2", "Scars on Conviction X = 2", "Resonant Style X exposed; arc transition if X was top primary",
     "conviction_track_v1 §2"),
    ("g_stall8", "project stall ≥ 8", "state.project_failed emitted", "doc-12 §8 / §4.2"),
    ("g_drift", "cumulative_drift > 0.5", "scene.gossip emitted", "doc-12 §8 / §6.3"),
    ("g_strain", "Knot strain > capacity", "Knot Break", "knots_v30 §6.1"),
    ("g_decay", "no new strain that season AND Disposition ≥ +3", "Knot strain −1 at Accounting",
     "knots_v30 §5"),
    ("g_bond5", "Bonds ≥ 5", "knot operations eligible (Memory-Query-checked prerequisite)",
     "key_substrate_v30 §8.4"),
]

# quantity → gate wiring: (module, state-name substring) → gate ids
GATE_WIRES = [
    ("territorial_piety", "CI (Church Influence)", ["g_ci100", "g_cicap"]),
    ("peninsular_strain", "IP (Institutional Pressure)", ["g_ip100", "g_ip85", "g_ip80", "g_ipfall"]),
    ("__MS__", None, ["g_ms0", "g_ms5", "g_msrec"]),
    ("faction_state", "Mandate", ["g_diss"]),
    ("settlement_layer", "Prosperity / Defense / Order", ["g_ord0", "g_def0"]),
    ("settlement_layer", "Local Economy / Garrison Strength / Public Order", ["g_dv0"]),
    ("piety_track", "conviction scars", ["g_scar2", "g_scar3"]),
    ("npc_behavior", "projects", ["g_stall8"]),
    ("npc_behavior", "beliefs/opinions", ["g_drift"]),
    ("fieldwork_knots", "knot strain", ["g_strain", "g_decay"]),
    ("fieldwork_knots", "Bonds", ["g_bond5"]),
]

DERIVATIONS = [
    # (src label, dst label, formula, source)
    ("settlement Order", "province Accord", "floor(mean settlement Order)", "settlement_layer_v30 §1.3"),
    ("Prosperity", "Local Economy", "Prosperity × 50", "settlement_layer_v30 §1.3"),
    ("Defense (+ Fort Level)", "Garrison Strength", "Defense × 20 + Fort × 30", "settlement_layer_v30 §1.3"),
    ("settlement Order", "Public Order", "Order × 20 (riot events below 0)", "settlement_layer_v30 §1.3"),
    ("L_s, PS_s, W_s", "faction Mandate",
     "q_s = 0.5L + 0.5PS; W_s = base(Type)+Prosperity+FacilityTier; T = Σ W_s·(q_s/7); "
     "Mandate = clamp(round(7T/(T+6)), 0, 7) — saturating (Lesson-5 bound)",
     "settlement_layer_v30 §1.8 LPS-2e"),
    ("faction Mandate", "settlement L/PS",
     "drift ±1/settlement/season toward Mandate (damped); mean-reverting stabilizing feedback; "
     "Stage-4 sim bounded over 30 seasons", "settlement_layer_v30 §1.8"),
    ("settlement Prosperity", "faction Treasury income", "Σ settlement Prosperity × 10",
     "derived_stats §8.1 (as quoted in settlement_layer §1.8)"),
]

SEQUENCE = [
    ("season tick", "engine_clock emits mechanical.season_change",
     "key_type_registry (engine_clock)"),
    ("Accounting boundary", "engine_clock emits mechanical.accounting", "doc-12 §8"),
    ("1. Procedure B", "Knowledge Decay → Concern Generation (memory_query reads Keys) → "
     "Resolution (state.concern_resolved, state.belief_revised, MemoryReferences)", "doc-12 §8"),
    ("2. DA Proposal Phase", "select_proposal() reads Faction Meta-Armature; "
     "execute_proposed_domain_actions() emits da_outcome.*; displacement_neglect_observed → "
     "scene.displacement [unreg]", "doc-12 §8"),
    ("3. Procedure C", "mechanical.project_advanced [unreg]; state.project_failed [unreg] "
     "(stall ≥ 8); state.project_completed [unreg]", "doc-12 §8"),
    ("4. Procedure D", "state.opinion_revised per drift threshold", "doc-12 §8"),
    ("5. Procedure E", "scene.interaction (ambient pairs); scene.dialogue (knowledge sharing); "
     "scene.gossip (cumulative_drift > 0.5)", "doc-12 §8"),
    ("emission processing", "substrate single-update rule: validate (registry + invariants, "
     "causes[] DAG) → append immutable KEY_LOG → resolve observers — inline, deterministic",
     "key_substrate_v30 §4.1"),
    ("settlement Accounting", "derived-value-at-0-through-Accounting → stat −1; Mandate "
     "feedback drift ±1; Knot strain decay check", "settlement §1.3/§1.8; knots §5"),
]

# per-module gate/sequence annotations for the flat table
MODULE_GATES = {
    "npc_behavior": "Accounting order B→DA→C→D→E (doc-12 §8); stall≥8; drift threshold; "
                    "cumulative_drift>0.5",
    "piety_track": "per-Conviction Scar 2 (Style exposed) / 3+ (crisis, d6 table) — PP-718",
    "territorial_piety": "CI seasonal cap (ci_political §2.4); CI=100 handoff",
    "ci_political": "CI=100 Theocracy attempt (§2.2); card cooldown track (§5.3)",
    "victory": "MS=0; MS≤5×10s; IP=100/85/80 phase chain + repulsion exits; all-dissolved",
    "peninsular_strain": "Turmoil 0–10; IP milestones 60/80/90 visibility (victory §5.2)",
    "settlement_layer": "Order=0 revolt; Defense=0 auto-capture; derived=0 through "
                        "Accounting → stat −1; Mandate↔L/PS damped feedback (§1.8)",
    "fieldwork_knots": "Bonds≥5 prerequisite; strain>capacity Break; decay gate "
                       "(Disposition≥+3, no new strain)",
    "engine_clock": "season tick → mechanical.season_change; Accounting boundary → "
                    "mechanical.accounting",
    "faction_state": "±2 faction-stat seasonal cap (settlement §1.8); cascade loop [open]",
    "threadwork": "Coherence depletion (variable cost); Thread Fatigue (ED-694)",
}

SCALE_GROUPS = [
    ("PENINSULA", ["peninsula"]),
    ("PROVINCIAL", ["provincial"]),
    ("TERRITORY_SETTLEMENT", ["territory", "settlement"]),
    ("SCENE", ["scene"]),
    ("PERSONAL", ["personal", "thread"]),
]

BUCKET_SHAPE = {  # mermaid shape templates
    "clock": ('[("', '")]'),
    "track": ('["', '"]'),
    "pool": ('(["', '"])'),
    "derived_value": ('[/"', '"/]'),
}


def fam_summary(types):
    """Compact label for a set of type strings."""
    fams = {}
    for t in sorted(types):
        fams.setdefault(t.split('.')[0], []).append(t)
    parts = []
    for f, ts in sorted(fams.items()):
        parts.append(ts[0] if len(ts) == 1 else f"{f}.* x{len(ts)}")
    return ", ".join(parts)


def load(contracts_path, registry_path):
    doc = yaml.safe_load(open(contracts_path))
    mods = doc["modules"]
    registered = parse_registry_types(open(registry_path).read())
    return mods, registered


def build_edges(mods):
    """Module-pair edges, engine edges, orphan list, seam set."""
    by = {m["module"]: m for m in mods}
    pair, engine_edges = {}, {}
    for m in mods:
        for c in m.get("consumes", []) or []:
            t, frm = c.get("type"), c.get("from", [])
            if frm in ("engine", ["engine"]):
                engine_edges.setdefault(m["module"], set()).add(t)
                continue
            for p in frm or []:
                pair.setdefault((p, m["module"]), set()).add(t)
    # seams: A6 logic
    seams = set()
    for (p, cns), types in pair.items():
        pm, cm = by.get(p), by.get(cns)
        if not pm or not cm:
            continue
        if set(pm.get("scales") or []) & set(cm.get("scales") or []):
            continue
        if pm.get("transitions") or cm.get("transitions"):
            continue
        seams.add((p, cns))
    # orphans: A4 logic
    cpats = [(c.get("type"), m["module"]) for m in mods
             for c in m.get("consumes", []) or [] if c.get("type") != "*"]
    orphans = []   # (module, type)
    for m in mods:
        for e in m.get("emits", []) or []:
            t = e.get("type")
            if e.get("terminal") or not t:
                continue
            if not any(_pat_overlap(t, cp) for cp, _ in cpats):
                orphans.append((m["module"], t))
    return pair, engine_edges, seams, orphans


def flowchart(mods, registered):
    pair, engine_edges, seams, orphans = build_edges(mods)
    L = ["flowchart LR"]
    placed = set()
    overrides = {"articulation_layer": "READERS"}
    groups = {g: [] for g, _ in SCALE_GROUPS}
    groups["READERS"] = []
    groups["STUBS"] = []
    for m in mods:
        name = m["module"]
        if m.get("status") == "stub":
            groups["STUBS"].append(name); placed.add(name); continue
        if name in overrides:
            groups[overrides[name]].append(name); placed.add(name); continue
        s0 = (m.get("scales") or ["provincial"])[0]
        for g, scales in SCALE_GROUPS:
            if s0 in scales:
                groups[g].append(name); placed.add(name); break
    assert placed == {m["module"] for m in mods}
    for g in [*[x for x, _ in SCALE_GROUPS], "READERS", "STUBS"]:
        if not groups[g]:
            continue
        L.append(f'  subgraph {g}["{g.replace("_", " / ")}"]')
        for n in groups[g]:
            suffix = " (stub)" if g == "STUBS" else ""
            L.append(f'    {n}["{n}{suffix}"]')
        L.append("  end")
    L.append('  ENGINE(["engine: Key stream / Memory / clock state"])')
    L.append('  UNCONSUMED["no declared consumer (A4)"]')
    for (p, c), types in sorted(pair.items()):
        lbl = fam_summary(types)
        if (p, c) in seams:
            L.append(f'  {p} -.->|"{lbl} !A6"| {c}')
        else:
            L.append(f'  {p} -->|"{lbl}"| {c}')
    for c, types in sorted(engine_edges.items()):
        L.append(f'  ENGINE -.->|"{fam_summary(types)}"| {c}')
    for emitter, t in sorted(orphans):
        mark = "" if t in registered or _wild_reg(t, registered) else " *UNREG"
        L.append(f'  {emitter} -.->|"{t}{mark}"| UNCONSUMED')
    L += [
        "  classDef stubcls stroke-dasharray: 5 5,opacity:0.7;",
        "  class " + ",".join(groups["STUBS"]) + " stubcls;" if groups["STUBS"] else "",
        "  classDef sink fill:#fee,stroke:#c00;",
        "  class UNCONSUMED sink;",
    ]
    return "\n".join(x for x in L if x)


def _wild_reg(t, registered):
    return t.endswith(".*") and any(x.startswith(t[:-1]) for x in registered)


def state_graph(mods):
    L = ["flowchart TB"]
    qid = {}
    n = 0
    for m in mods:
        sts = m.get("state") or []
        if not sts:
            continue
        name = m["module"]
        L.append(f'  subgraph sg_{name}["{name}"]')
        L.append(f'    {name}_x(("{name}"))')
        for s in sts:
            n += 1
            o, c = BUCKET_SHAPE.get(s.get("bucket"), ('["', '"]'))
            disp = s["name"].replace('"', "'")
            L.append(f'    q{n}{o}{disp} : {s.get("bucket")}{c}')
            qid[(name, s["name"])] = f"q{n}"
        L.append("  end")
        for s in sts:
            q = qid[(name, s["name"])]
            if s.get("writable"):
                L.append(f'  {name}_x -->|writes| {q}')
            else:
                L.append(f'  {q} -.->|reads| {name}_x')
    L.append('  MS[("Mending Stability (MS) : clock — NO owning module in contracts")]')
    L.append('  subgraph DERIV["DERIVATIONS (calculations — authored from cited reads)"]')
    for i, (src, dst, formula, source) in enumerate(DERIVATIONS):
        L.append(f'    d{i}_s["{src}"] -->|"{formula.split(";")[0][:60]}"| d{i}_t[/"{dst}"/]')
        L.append(f'    %% {source}')
    L.append("  end")
    L.append('  subgraph GATESB["GATES (thresholds — authored from cited reads)"]')
    for gid, cond, conseq, source in GATES:
        L.append(f'    {gid}{{"{cond}"}} --> {gid}_c["{conseq}"]')
        L.append(f'    %% {source}')
    L.append("  end")
    # wire owning quantities into their gates
    for mod, sub, gids in GATE_WIRES:
        if mod == "__MS__":
            src = "MS"
        else:
            src = next((q for (mn, sn), q in qid.items()
                        if mn == mod and sub in sn), None)
            if not src:
                continue
        for gid in gids:
            L.append(f'  {src} -.-> {gid}')
    L += ["  classDef gatecls fill:#ffd,stroke:#a80;",
          "  class " + ",".join(g[0] for g in GATES) + " gatecls;"]
    return "\n".join(L)


ERA_MACHINE = """stateDiagram-v2
    [*] --> Baseline
    Baseline --> PostCalamity : MS = 0
    PostCalamity --> Baseline : MS restored to 20 (within 10 seasons)
    PostCalamity --> SecondCalamity : MS <= 5 sustained 10 seasons
    SecondCalamity --> [*]
    Baseline --> OccupationP1 : IP = 100
    OccupationP1 --> Baseline : IP < 85 (invasion stalls)
    OccupationP1 --> OccupationP2 : IP >= 85 for 3 seasons
    OccupationP2 --> OccupationP1 : IP < 75 (corridor abandoned)
    OccupationP2 --> OccupationP3 : IP >= 80 for 3 more seasons
    OccupationP3 --> Repelled : resistance repulsion (UN Mandate >= 3, Accord 0, battle Success+)
    OccupationP1 --> Repelled : military OW x2 / diplomatic NAP
    OccupationP2 --> Repelled : military OW x2 / diplomatic NAP
    Repelled --> Baseline : IP frozen or reset (60/40/30/20 per path)
    Baseline --> Anarchy : all factions dissolved
    Anarchy --> Baseline : >= 2 factions re-establish Parliament quorum
"""


def flat_tables(mods, registered):
    rows = ["| Module | Scales | Mechanic | Inputs | State & calculations | Gates / sequence | Outputs |",
            "|---|---|---|---|---|---|---|"]
    for m in mods:
        name = m["module"]
        if m.get("status") == "stub":
            rows.append(f"| {name} | {' '.join(m.get('scales') or [])} | — (stub) | — | — | — | — |")
            continue
        cons = []
        for c in m.get("consumes", []) or []:
            frm = c.get("from")
            src = "engine" if frm in ("engine", ["engine"]) else ",".join(frm or ["?"])
            cons.append((c["type"], src))
        by_src = {}
        for t, s in cons:
            by_src.setdefault(s, set()).add(t)
        inputs = "; ".join(f"{fam_summary(ts)} ← {s}" for s, ts in sorted(by_src.items())) or "—"
        emits = []
        for e in m.get("emits", []) or []:
            t = e["type"]
            mark = "" if (t in registered or _wild_reg(t, registered)) else UNREG_MARK
            emits.append(t + mark)
        outputs = "; ".join(emits) or "—"
        state = "; ".join(f"{s['name']} ({s['bucket']}{'' if s.get('writable') else ', read'})"
                          for s in m.get("state") or []) or "—"
        gates = MODULE_GATES.get(name, "—")
        rows.append(f"| {name} | {' '.join(m.get('scales') or [])} | {m.get('resolver') or '?'} "
                    f"| {inputs} | {state} | {gates} | {outputs} |")
    # type matrix
    all_types = set(registered)
    emit_map, cons_map = {}, {}
    for m in mods:
        for e in m.get("emits", []) or []:
            all_types.add(e["type"]); emit_map.setdefault(e["type"], []).append(m["module"])
        for c in m.get("consumes", []) or []:
            if c["type"] != "*":
                all_types.add(c["type"]); cons_map.setdefault(c["type"], []).append(m["module"])
    tm = ["| Key type | Registered | Emitters (contracts) | Consumers (contracts; wildcard-matched) |",
          "|---|---|---|---|"]
    for t in sorted(x for x in all_types if not x.endswith(".*") and x != "*"):
        reg = "yes" if t in registered else "**NO**"
        em = ", ".join(sorted(set(emit_map.get(t, [])))) or "—"
        cn = sorted({m for p, ms in [(k, v) for k, v in cons_map.items()] for m in ms
                     if _pat_overlap(t, p)})
        tm.append(f"| {t} | {reg} | {em} | {', '.join(cn) or '— (orphan / pseudo-only)'} |")
    return "\n".join(rows), "\n".join(tm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contracts", required=True)
    ap.add_argument("--registry", required=True)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    mods, registered = load(a.contracts, a.registry)
    os.makedirs(a.outdir, exist_ok=True)
    fc = flowchart(mods, registered)
    sg = state_graph(mods)
    master, types_tbl = flat_tables(mods, registered)
    open(os.path.join(a.outdir, "module_flowchart.mermaid"), "w").write(fc + "\n")
    open(os.path.join(a.outdir, "state_graph.mermaid"), "w").write(sg + "\n")
    seq = "\n".join(f"| {a_} | {b} | {c} |" for a_, b, c in SEQUENCE)
    gates = "\n".join(f"| {c} | {q} | {s} |" for _, c, q, s in GATES)
    deriv = "\n".join(f"| {s} → {d} | `{f}` | {src} |" for s, d, f, src in DERIVATIONS)
    doc = DOC_TMPL.format(flow=fc, state=sg, era=ERA_MACHINE, master=master,
                          types=types_tbl, seq=seq, gates=gates, deriv=deriv,
                          n=len(mods))
    open(os.path.join(a.outdir, "module_map_flat.md"), "w").write(doc)
    print(f"wrote 3 artifacts to {a.outdir} ({len(mods)} modules)")


DOC_TMPL = """# Module Map — Flowchart, State Graph, Flattened Pipeline
**Generated 2026-06-10 by `skills/valoria-module-adjudicator/scripts/contract_flowchart.py`**
Source of truth: `references/module_contracts.yaml` (v2.1, commit 4c474c52) — REGENERATE, never hand-edit.
Graph sections are generated; gates / derivations / sequence tables are authored transcriptions
from cited canon reads (doc-12 §8, victory §5, settlement §1.3/§1.8, ci_political §2,
conviction_track_v1 §2, knots §5–§6, key_substrate §4.1/§8.4). Findings context: ED-1006.

## 1. Module flowchart — Key-flow topology ({n} modules)
Solid = declared edge; dashed `!A6` = cross-scale seam with no transition rule (violation);
dashed to UNCONSUMED = orphan emission (A4); `*UNREG` = canon-named type absent from the
Key Type Registry (A2 / F2 class).

```mermaid
{flow}
```

## 2. Comprehensive state graph — quantities, writers, derivations, gates
Shapes: cylinder = clock, rectangle = track, stadium = pool, parallelogram = derived value
(F1 guard: derived values are never written directly). MS has **no owning module** in the
contracts — a coverage gap, not an omission.

```mermaid
{state}
```

## 3. World-state era machine (victory_v30 §5)
Era states are not strictly exclusive — canon: "during Occupation the game world continues
ticking; MS declines" (§5.2) — Occupation and MS-driven transitions run concurrently.

```mermaid
{era}
```

## 4. Flattened pipeline — all inputs, mechanics, gates, outputs

### 4.1 Master module table
{master}

### 4.2 Canonical sequence (Accounting spine)
| Step | What happens | Source |
|---|---|---|
{seq}

### 4.3 Gates
| Condition | Consequence | Source |
|---|---|---|
{gates}

### 4.4 Derivations (calculations)
| Mapping | Formula | Source |
|---|---|---|
{deriv}

### 4.5 Key-type matrix (flattened I/O at type granularity)
{types}

## 5. Red overlay (where the map bleeds)
Adjudication v2.1: 27 violations / 56 warnings — 7 unregistered canon-named types (A2),
19 top-down cross-scale seams (A6: scale_transitions §3 has no downward rule), orphan
emissions incl. pseudo-consumer-only types (A4), conviction_track_v1 outside
canonical_sources (A8), registry 37-vs-38 self-drift (A9). Full detail: ED-1006 +
`references/module_contracts.yaml` gap_notes. The Mandate↔settlement L/PS loop has a
**documented canon damper** (settlement §1.8 saturating form + mean reversion, Stage-4
sim bounded) — contracts loop annotation upgrade pending.
"""

if __name__ == "__main__":
    main()
