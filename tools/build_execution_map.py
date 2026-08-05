#!/usr/bin/env python3
"""Build the boot-to-termination execution map — the fork's file map.

WHAT THIS IS. A single artifact answering "how does the game run, from boot to game over,
with every module, its contract, its Keys, and where its data lives". Emitted as JSON (for
tooling) and Markdown (for reading).

WHAT MAKES IT DIFFERENT FROM WHAT ALREADY EXISTS, so this does not duplicate:
  * `tools/observability/build_graph.py` emits the PROPAGATION graph — who emits/consumes which
    Key. It has no notion of ORDER.
  * `references/wiring_manifest.yaml` carries build state and port rank per module. It has no
    notion of CALL SEQUENCE.
  * `references/key_graph.json` reconciles producers/consumers across two authored sources.
This map adds the missing axis: **temporal order**, from `run_campaign` through the season loop
to the terminal condition, with every other view joined onto it.

THE HONESTY RULE, which is the whole point. A boot-to-termination map of a game where most of the
27 modules do not execute would, drawn naively, be a picture of intent presented as behaviour. So every
node carries `executes`, derived from `wiring_manifest`'s build ladder, and the phases are
derived from the ACTUAL call sequence in `engine/mc_v18.py` + `systems/overview/sim/season.py`,
not from a design document. Nodes that do not run are IN the map and marked, because for a fork
the un-run ones are the work-list.

SOURCES (nothing is invented; every row traces to a file):
  engine/mc_v18.py                        — boot, the season loop, terminal conditions
  systems/overview/sim/season.py          — the canonical 3-step season composition
  engine/cross_scale/scene_dispatch.py    — the scene phase
  references/module_contracts.yaml        — Key IN -> resolver -> OUT, owned state, gates
  references/wiring_manifest.yaml         — build state / godot state / port rank / parity
  references/key_graph.json               — producers + consumers per Key type
  systems/_architecture/key_type_registry_v30.md — Key payload/scale/permanence

Usage:
    python3 tools/build_execution_map.py            # write both artifacts
    python3 tools/build_execution_map.py --check     # verify they are current (CI-able)
"""
from __future__ import annotations

import ast
import json
import os
import sys

try:
    import yaml
except ImportError:
    yaml = None

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT_JSON = os.path.join(REPO, 'references', 'execution_map.json')
OUT_MD = os.path.join(REPO, 'references', 'EXECUTION_MAP.md')

# ---------------------------------------------------------------------------
# The execution spine.
#
# HAND-TRANSCRIBED FROM CODE, and that is a deliberate choice with a cost. The call sequence
# could be derived by static analysis, but the result would be a call graph, not a *phase*
# structure -- run_season's three steps are a documented composition, not something an AST
# reveals as phases. So the spine is transcribed, each step carries the file:line it came from,
# and `test_execution_map.py` re-checks every anchor still exists. If a step's anchor stops
# matching, the map is stale and the test says so rather than the map silently lying.
# ---------------------------------------------------------------------------
SPINE = [
    # (phase_id, parent, title, source, anchor, modules, note)
    ("boot", None, "Boot — construct the world",
     "engine/mc_v18.py", "world = game_state.create_world(seed=seed)", [],
     "Deterministic from `seed`. Builds factions, territories, clocks. Godot: this is the "
     "save/load entry point — strategy Stage 1 specifies save = initial conditions + Key log."),
    ("boot.victory_reset", "boot", "Reset victory state",
     "engine/mc_v18.py", "victory.reset()", ["victory"], ""),
    ("boot.slate_clear", "boot", "Clear the scene slate",
     "engine/mc_v18.py", "scene_slate.clear()", [], "Module-level queue; NOT per-world state."),
    ("boot.flags", "boot", "Resolve per-campaign flags",
     "engine/mc_v18.py", "world.dispatch_combat_bridge = _dispatch_combat_bridge_on(effective_params)",
     [], "DISPATCH_COMBAT_BRIDGE decided ONCE and stashed on `world` (single owner)."),
    ("boot.substrate", "boot", "Attach the Key substrate",
     "engine/mc_v18.py", "world.echo_scheduler = echo_transport.make_scheduler(", [],
     "THE ORCHESTRATOR. TickScheduler + KeyLog. Its PRESENCE is the ECHO_TRANSPORT flag — "
     "absence means the byte-exact legacy path. `world.key_log` is the log."),
    ("boot.subscribe", "boot", "Subscribe articulation to the scheduler",
     "engine/mc_v18.py", "_articulation.subscribe_all(world.echo_scheduler)", ["articulation"],
     "The only production TickScheduler subscriber wiring."),

    ("loop", None, "Season loop — `for _ in range(max_s)`",
     "engine/mc_v18.py", "for _ in range(max_s):", [], "Breaks on `world.winner`."),
    ("loop.s1", "loop", "Step 1 — advance_season",
     "systems/overview/sim/season.py", "sr = advance_season(world)", ["engine_clock"],
     "Season counter, arc boundary, per-arc + per-season faction flag resets. The temporal "
     "spine `engine_clock` is `doc: null` — ED-1051, the sole remaining T0 blocker."),
    ("loop.s2", "loop", "Step 2 — action_callback",
     "systems/overview/sim/season.py", "action_callback(world)", [],
     "The injection point. mc_v18 passes `_faction_actions_callback`; **Godot passes its own to "
     "drive UI scene flow** (season.py's own docstring). This is the seam the port hangs on."),
    ("loop.s2.factions", "loop.s2", "Faction actions, per parliamentary faction holding territory",
     "engine/mc_v18.py", "faction_take_action(faction, world, world.rng)",
     ["faction_state", "faction_politics"],
     "GD-2 mandatory-actions precedence enforced inside. Errors print to stderr, never abort."),
    ("loop.s2.scenes", "loop.s2", "Scene phase — the personal-scale seam",
     "engine/cross_scale/scene_dispatch.py", "def run_scene_phase",
     ["social_contest", "personal_combat", "fieldwork_knots", "threadwork"],
     "MEASURED 2026-08-03: a whole campaign dispatches 29 slots and ALL 29 are `contest`. "
     "`queue_triggered_scenes` is the only production caller of `queue_scene`, and "
     "`evaluate_triggers` can only emit scene_type=contest. No trigger produces combat."),
    ("loop.s2.parliament", "loop.s2", "Parliamentary vote (flag-gated on the scheduler)",
     "engine/mc_v18.py", "parliamentary_bridge.run_parliamentary_scene(world, world.rng)",
     ["social_contest"], "Resolves on aggregate state; composes a winner Domain Echo."),
    ("loop.s2.boundary", "loop.s2", "ACTION->ACCOUNTING boundary — deferred applies land",
     "engine/mc_v18.py", "_sched.accounting_boundary()", [],
     "OF-7. Keys emitted during the scene phase were logged LIVE; their `apply` closures execute "
     "HERE. Then `next_tick()` resets the per-tick emission counter. This is the orchestration "
     "contract: emission is immediate, effect is deferred to a named boundary."),
    ("loop.s3", "loop", "Step 3 — run_accounting",
     "systems/overview/sim/season.py", "run_accounting(world)",
     ["territorial_piety", "npc_behavior", "faction_state"],
     "SIX steps, read from the function body (accounting.py:95-142) rather than its summary. An "
     "earlier version of this note said 'CI calc + MS decay + NPC' and attributed "
     "`settlement_layer`, which run_accounting never calls -- written from the docstring, not the "
     "code. In order: (1) apply_seasonal_ci every season [PP-412]; (2) apply_ms_baseline_decay, "
     "gated by the CALLER on season % SEASONS_PER_YEAR == 0 [PP-255] -- the callee does not check "
     "cadence; (3) check_insurgency_triggers [GD-3 a-b]; (4) check_insurgency_promotion over a "
     "SNAPSHOT of the insurgency ids, since promotion mutates the dict; (5) simulate_npc_actions "
     "[NPE stance drift]; (6) _probe_province_accord_drift, report-only and deliberately last."),
    ("loop.victory", "loop", "Victory check (GD-1)",
     "engine/mc_v18.py", "results = victory.check_all_factions(world)", ["victory"],
     "Sets `world.winner`, which breaks the loop on the NEXT iteration."),

    ("term", None, "Termination", "engine/mc_v18.py", "if not world.winner:", [], ""),
    ("term.fallback", "term", "Fallback winner by territory count",
     "engine/mc_v18.py", "scores[fn] = held * 10 + f.L + len(f.territories)", ["victory"],
     "Runs when the loop exhausts `max_s` with no victor."),
    ("term.result", "term", "Emit CampaignResult",
     "engine/mc_v18.py", "return CampaignResult(", [],
     "Carries `key_log_hash` + `keys_emitted` — the parity surface the Godot port compares "
     "against (strategy Stage 2: Key-log equality is the master parity check)."),
]


def _exists(rel):
    """None -> None (nothing declared); otherwise whether the declared path is on disk."""
    if not rel:
        return None
    return os.path.exists(os.path.join(REPO, rel))


def _code_path(name, contract, manifest_row):
    """Declared code path for a unit. Adapters have no `sim_module` in module_contracts -- the
    manifest declares `adapter: engine/cross_scale/` as their registry, so resolve there."""
    declared = contract.get('sim_module')
    # module_contracts writes an ABSENT code path as the literal string "none" (not YAML null),
    # so a naive truthiness check treats it as a declared path that fails to resolve -- which
    # reads as 13 dead pointers when the truth is 13 modules that have no code yet. Normalised
    # here so "declared but missing" means what it says; that distinction is the difference
    # between a rot report and a work-list.
    if isinstance(declared, str) and declared.strip().lower() in ('none', 'null', 'n/a', ''):
        declared = None
    # A pointer may be a DIRECTORY, not a file -- peninsular_strain -> systems/overview/sim/,
    # personal_combat -> systems/combat/combat_engine_v1/, social_contest ->
    # systems/social_contest/sim/contest/, 37 .py files between them. THIS function has always
    # accepted both; the `.endswith('.py')` restriction was in the TRACER's unit index and in a
    # throwaway diagnostic, where it reported all three as "no pointer" and nearly became a
    # 17-item work-list that did not exist. Both granularities are legitimate: a subsystem whose
    # implementation is a package cannot name one file.
    if declared:
        return declared
    if manifest_row.get('tier') == 'adapter':
        candidate = os.path.join('engine', 'cross_scale', f'{name}.py')
        if os.path.exists(os.path.join(REPO, candidate)):
            return candidate
    return None


def _load_yaml(rel):
    path = os.path.join(REPO, rel)
    if yaml is None or not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as fh:
        return yaml.safe_load(fh) or {}


def _load_json(rel):
    path = os.path.join(REPO, rel)
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def _anchor_present(source, anchor):
    """Does the transcribed anchor still exist in its source file?"""
    path = os.path.join(REPO, source)
    if not os.path.exists(path):
        return False
    return anchor in open(path, encoding='utf-8').read()


# Build states that mean "this actually runs in a campaign today".
EXECUTING = {'live', 'gated'}


def build():
    manifest = _load_yaml('references/wiring_manifest.yaml')
    contracts = _load_yaml('references/module_contracts.yaml')
    keygraph = _load_json('references/key_graph.json')
    trace = _load_json('references/execution_trace.json')

    mods = manifest.get('modules') or {}
    adapters = manifest.get('adapters') or {}
    cmods = contracts.get('modules') or contracts

    # ---- per-module join: manifest state + contract keys + FILE PATHS ----
    # module_contracts.yaml's `modules` is a LIST of dicts keyed by a `module` field, and
    # `consumes`/`emits` are lists of {type, from|to} -- not the bare-string shapes a first pass
    # assumed. Indexed here rather than guessed.
    by_name = {}
    raw = contracts.get('modules')
    if isinstance(raw, list):
        for c in raw:
            if isinstance(c, dict) and c.get('module'):
                by_name[c['module']] = c
    elif isinstance(raw, dict):
        by_name = raw

    def _types(seq):
        out = []
        for item in seq or []:
            if isinstance(item, str):
                out.append(item)
            elif isinstance(item, dict):
                v = item.get('type') or item.get('name') or item.get('key')
                if v:
                    out.append(v)
        return out

    module_rows = {}
    for name, m in list(mods.items()) + list(adapters.items()):
        c = by_name.get(name) or {}
        module_rows[name] = {
            "module": name,
            "tier": m.get('tier'),
            "scale": m.get('scale'),
            "resolver": m.get('resolver') or c.get('resolver'),
            "build": m.get('build'),
            "executes": m.get('build') in EXECUTING,
            "godot": m.get('godot'),
            "port_rank": m.get('port_rank'),
            "parity": m.get('parity'),
            # THE FILE MAP: where this unit's code and canon actually live, AND whether those
            # paths resolve. A file map whose paths do not exist is worse than none -- it reads
            # as coverage. Adapters carry no `sim_module` (they are not modules); their code is
            # engine/cross_scale/<name>.py by the manifest's own registry declaration, so it is
            # derived rather than left blank.
            "code": _code_path(name, c, m),
            "code_exists": _exists(_code_path(name, c, m)),
            "doc": c.get('doc'),
            "doc_exists": _exists(c.get('doc')),
            "keys_in": _types(c.get('consumes')),
            "keys_out": _types(c.get('emits')),
            # CENTRALIZATION: the scalars this module OWNS. A scalar with two owners is the
            # centralization defect the fork exists to remove, so ownership travels with the node.
            "owned_state": _types(c.get('state')),
            "accounting_phase": c.get('accounting_phase'),
            "gap_notes": bool(c.get('gap_notes')),
            "contract_status": c.get('status'),
            "note": m.get('note') or '',
        }

    # ---- key rows from the merged graph ----
    ktypes = keygraph.get('keys') or {}
    key_rows = {}
    for kname, k in (ktypes.items() if isinstance(ktypes, dict) else []):
        if not isinstance(k, dict):
            continue
        rec = k.get('reconciliation') or {}
        payload = k.get('payload') or {}
        key_rows[kname] = {
            "type": kname,
            "producers": k.get('producers') or [],
            "consumers": k.get('consumers') or [],
            "permanence": k.get('permanence'),
            "payload_required": payload.get('required') or [],
            "producer_status": rec.get('producer_status'),
            "consumer_status": rec.get('consumer_status'),
            # A type with no producer cannot fire; with no consumer nothing reacts. Both are
            # fork work-list entries, so they are counted rather than filtered out.
            "no_producer": not (k.get('producers') or []),
            "no_consumer": not (k.get('consumers') or []),
        }

    # ---- the spine, with anchor verification ----
    phases = []
    for pid, parent, title, source, anchor, modules, note in SPINE:
        phases.append({
            "id": pid, "parent": parent, "title": title,
            "source": source, "anchor": anchor,
            "anchor_present": _anchor_present(source, anchor),
            # AUTHORED, NOT DERIVED -- and labelled that way because two attempts to derive it
            # both failed and shipping either would have looked authoritative:
            #   * per-FILE transitive imports: every mc_v18-sourced phase (boot, the loop,
            #     termination) returned the same seven units. A file's closure wearing a phase's
            #     name.
            #   * per-FUNCTION local imports: returned `articulation_layer` for those same
            #     phases and NOTHING for the rest, because this codebase splits cross-subsystem
            #     calls between module-level and function-local imports while phase boundaries do
            #     not align with function boundaries.
            # Static attribution is not reliably derivable here. The correct instrument is a
            # DYNAMIC one -- trace a seeded campaign and record which module code executes
            # between phase markers -- and until that exists these stay marked unverified rather
            # than dressed up. The verified parts of this map are the source anchors (checked),
            # `executes` (derived from the manifest and re-derived in test), the code/doc paths
            # (existence-checked) and the key + owned-state joins (read from the registries).
            "modules": modules,
            "modules_attribution": "authored-unverified",
            # MEASURED, from tools/trace_execution_phases.py: which code actually ran in this
            # phase of one seeded campaign, and how many calls. `by_contract` is exact (a
            # module_contracts sim_module join, no collisions); `by_subsystem` is by directory
            # and coarser, and covers the 17 contracts that declare no code file at all.
            # ABSENCE HERE MEANS "not observed at this seed", NOT "dead". Presence is evidence.
            "measured_by_contract": (trace.get('by_contract') or {}).get(pid, {}),
            "measured_by_subsystem": (trace.get('by_subsystem_path') or {}).get(pid, {}),
            "measured_calls": (sum((trace.get('by_contract') or {}).get(pid, {}).values())
                               + sum((trace.get('by_subsystem_path') or {}).get(pid, {}).values())),
            "modules_executing": [m for m in modules if module_rows.get(m, {}).get('executes')],
            "note": note,
        })

    executing = sorted(n for n, r in module_rows.items() if r['executes'])
    return {
        "_generated": ("GENERATED by tools/build_execution_map.py. Boot-to-termination execution "
                       "order joined against module contracts, the wiring manifest and the key "
                       "graph. NEVER hand-edit — regenerate and commit. Every phase carries the "
                       "file:anchor it was transcribed from; tests/valoria/test_execution_map.py "
                       "fails if an anchor stops matching its source."),
        "schema_version": 1,
        "sources": [
            "engine/mc_v18.py", "systems/overview/sim/season.py",
            "engine/cross_scale/scene_dispatch.py", "references/module_contracts.yaml",
            "references/wiring_manifest.yaml", "references/key_graph.json",
        ],
        "reality_check": {
            "modules_total": len(mods),
            "adapters_total": len(adapters),
            "units_executing": len(executing),
            "executing": executing,
            "key_types": len(key_rows),
            "code_paths_declared": sum(1 for r in module_rows.values() if r['code']),
            "code_paths_missing": sorted(n for n, r in module_rows.items()
                                         if r['code'] and r['code_exists'] is False),
            "doc_paths_missing": sorted(n for n, r in module_rows.items()
                                        if r['doc'] and r['doc_exists'] is False),
            "no_code_declared": sorted(n for n, r in module_rows.items() if not r['code']),
            "trace_seed": trace.get('seed'),
            "trace_seasons": trace.get('seasons'),
            "measured_calls_caveat": (
                "Call counts measure COMPUTATIONAL DEPTH, not game significance. mass_battle is "
                "98.72% of calls but that is ~60,000 calls for each of 8 recorded battles, against "
                "~7 calls for each of 12 resolved scenes. A tick-level physics sim always dominates "
                "a call profile against a dice-pool resolver. Use this to find the port's "
                "performance-critical path, never to rank design priority."),
            "note": ("`executes` is build state in {live, gated}. A boot-to-termination map of a "
                     "game where most modules do not run would otherwise read as a picture of "
                     "intent. The un-run nodes are kept — for a fork they ARE the work-list."),
        },
        "phases": phases,
        "modules": module_rows,
        "keys": key_rows,
    }


def render_md(d):
    total_calls = sum(p.get('measured_calls', 0) for p in d['phases']) or 1
    L = []
    A = L.append
    A("# Valoria — Execution Map (boot → termination)\n")
    A("> **GENERATED** by `tools/build_execution_map.py`. Do not hand-edit.\n")
    rc = d['reality_check']
    A(f"**{rc['units_executing']} of {rc['modules_total'] + rc['adapters_total']} units execute today** "
      f"({rc['modules_total']} modules + {rc['adapters_total']} adapters). "
      f"{rc['key_types']} Key types registered.\n")
    A("Every node below is annotated `RUNS` or `does not run`. Nodes that do not run are kept: "
      "for the fork they are the work-list, not noise.\n")

    A("\n## 1. Execution spine\n")
    for p in d['phases']:
        depth = p['id'].count('.')
        pad = "  " * depth
        mods = p['modules']
        run = p['modules_executing']
        tag = ""
        if mods:
            tag = f"  — modules: {', '.join(f'`{m}`' + ('' if m in run else ' *(does not run)*') for m in mods)}"
        warn = "" if p['anchor_present'] else "  ⚠ **ANCHOR MISSING — map is stale**"
        A(f"{pad}- **`{p['id']}`** {p['title']}{tag}{warn}")
        A(f"{pad}  <sub>`{p['source']}` → `{p['anchor']}`</sub>")
        if p.get('measured_calls'):
            top = list(p['measured_by_contract'].items()) + list(p['measured_by_subsystem'].items())
            top.sort(key=lambda kv: -kv[1])
            share = 100.0 * p['measured_calls'] / max(1, total_calls)
            A(f"{pad}  <sub>**MEASURED {p['measured_calls']:,} calls ({share:.2f}% of campaign)** — "
              + ", ".join(f"`{k}` {v:,}" for k, v in top[:5]) + "</sub>")
        if p['note']:
            A(f"{pad}  <sub>{p['note']}</sub>")

    A("\n## 2. Modules — contract, keys, state, port\n")
    A("| module | scale | resolver | build | runs | godot | rank | keys in | keys out |")
    A("|---|---|---|---|---|---|---|---|---|")
    for name in sorted(d['modules'], key=lambda n: (d['modules'][n]['port_rank'] is None,
                                                    d['modules'][n]['port_rank'] or 0, n)):
        m = d['modules'][name]
        A(f"| `{name}` | {m['scale'] or ''} | {m['resolver'] or ''} | {m['build'] or ''} | "
          f"{'✅' if m['executes'] else '—'} | {m['godot'] or ''} | {m['port_rank'] if m['port_rank'] is not None else ''} | "
          f"{len(m['keys_in'])} | {len(m['keys_out'])} |")

    A("\n## 3. Keys — producers, consumers, and the dead ends\n")
    if d['keys']:
        live = [k for k, r in d['keys'].items() if not r['no_producer'] and not r['no_consumer']]
        A(f"**{len(live)} of {len(d['keys'])} key types have both a producer and a consumer.** "
          f"A type with no producer cannot fire; one with no consumer means nothing reacts. Both "
          f"are kept below and marked — for the fork they are the work-list.\n")
        A("| key type | producers | consumers | required payload | gap |")
        A("|---|---|---|---|---|")
        for k in sorted(d['keys']):
            r = d['keys'][k]
            gap = []
            if r['no_producer']:
                gap.append("**no producer**")
            if r['no_consumer']:
                gap.append("**no consumer**")
            A(f"| `{k}` | {', '.join(r['producers']) or '—'} | {', '.join(r['consumers']) or '—'} | "
              f"{', '.join(r['payload_required']) or '—'} | {' · '.join(gap) or 'ok'} |")
    else:
        A("_No key rows resolved from `references/key_graph.json` — check its schema._")

    A("\n## 4. Centralization — owned state per module\n")
    A("The scalars each module's contract declares it OWNS. A scalar appearing under two owners "
      "is the centralization defect the fork exists to remove, so ownership travels with the node "
      "rather than living in a separate register.\n")
    owners = {}
    for name, m in d['modules'].items():
        for st in m['owned_state']:
            owners.setdefault(st, []).append(name)
    contested = {s_: o for s_, o in owners.items() if len(o) > 1}
    A(f"**{len(owners)} owned scalars across {len(d['modules'])} units; "
      f"{len(contested)} claimed by more than one owner.**\n")
    if contested:
        A("| scalar | claimed by |")
        A("|---|---|")
        for s_ in sorted(contested):
            A(f"| `{s_}` | {', '.join(sorted(contested[s_]))} |")
    else:
        A("_No scalar is claimed by two modules._\n")

    return "\n".join(L) + "\n"


def main(argv):
    d = build()
    js = json.dumps(d, indent=1) + "\n"
    md = render_md(d)
    if '--check' in argv:
        ok = True
        for path, text in ((OUT_JSON, js), (OUT_MD, md)):
            if not os.path.exists(path) or open(path, encoding='utf-8').read() != text:
                print(f"[EXEC-MAP] stale or missing: {os.path.relpath(path, REPO)}", file=sys.stderr)
                ok = False
        stale = [p['id'] for p in d['phases'] if not p['anchor_present']]
        if stale:
            print(f"[EXEC-MAP] anchors no longer in source: {stale}", file=sys.stderr)
            ok = False
        print("[EXEC-MAP] current" if ok else "[EXEC-MAP] FAILED")
        return 0 if ok else 1
    with open(OUT_JSON, 'w', encoding='utf-8') as fh:
        fh.write(js)
    with open(OUT_MD, 'w', encoding='utf-8') as fh:
        fh.write(md)
    rc = d['reality_check']
    print(f"[EXEC-MAP] {len(d['phases'])} phases · {len(d['modules'])} units "
          f"({rc['units_executing']} executing) · {len(d['keys'])} key types")
    missing = [p['id'] for p in d['phases'] if not p['anchor_present']]
    if missing:
        print(f"[EXEC-MAP] WARNING anchors not found in source: {missing}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
