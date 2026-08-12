#!/usr/bin/env python3
"""Measure which module code executes in each phase of a seeded campaign.

WHY THIS EXISTS. `tools/build_execution_map.py` carries a per-phase module list marked
`authored-unverified`, because two attempts to DERIVE it statically both failed:

  * per-FILE transitive imports -> every phase sourced from mc_v18.py returned the same seven
    units. A file's import closure wearing a phase's name.
  * per-FUNCTION local imports -> `articulation_layer` for those phases and nothing for the rest,
    because this codebase splits cross-subsystem calls between module-level and function-local
    imports while phase boundaries do not align with function boundaries.

Neither is fixable by tuning: an import edge is not a call, and a call is what a phase is made of.
So this measures instead. `sys.setprofile` records every Python call during a seeded campaign; a
phase stack maintained by wrapping the eight phase-boundary functions says which phase each call
happened in; the file the callee is defined in maps back to a unit via module_contracts'
`sim_module`.

WHAT THIS IS AND IS NOT. It is a record of ONE seeded campaign. A module that only runs on a
different seed will read as absent, so absence here is "not observed at this seed", NOT "dead" --
the two are different claims and conflating them is the false-absence error this repo keeps hitting.
Presence, by contrast, is hard evidence: the code ran.

CALLS MEASURE COMPUTATIONAL DEPTH, NOT GAME SIGNIFICANCE -- and the difference is large enough to
invert a conclusion. The first run of this tool produced "mass_battle is 98.72% of the campaign",
which is true and was about to be read as a statement about design priority. Normalised by game
EVENT it says the opposite: 481,653 calls for 8 recorded battles (~60,000 calls each) against 84
calls for 12 resolved scenes (~7 calls each). A tick-level physics simulation will always dominate
a call profile against a dice-pool resolver; that is a fact about resolution granularity, not about
what matters. Read this output as "where the RUNTIME COST is" -- which is exactly what a Godot port
needs to know, since that is the path most likely to need optimisation -- and never as "where the
game is".

`setprofile` is used rather than `settrace` deliberately: it fires on call/return only, not per
line, which is roughly an order of magnitude cheaper on a full campaign.

Usage:
    python3 tools/trace_execution_phases.py [--seed N] [--seasons N] [--json PATH]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import collections

# ONE OWNER for the repo root: tools/ci_common.py (plan G7, ED-IN-0159 §8.3).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
if REPO not in sys.path:
    sys.path.insert(0, REPO)

# (module_path, attribute, phase_id) — the eight boundaries, each verified to resolve before use.
BOUNDARIES = [
    ("engine.autoload.game_state", "create_world", "boot"),
    ("engine.autoload.season_manager", "advance_season", "loop.s1"),
    ("systems.factions.sim.faction_action", "faction_take_action", "loop.s2.factions"),
    ("engine.cross_scale.scene_dispatch", "run_scene_phase", "loop.s2.scenes"),
    ("engine.cross_scale.parliamentary_bridge", "run_parliamentary_scene", "loop.s2.parliament"),
    ("systems.overview.sim.accounting", "run_accounting", "loop.s3"),
    ("engine.autoload.victory", "check_all_factions", "loop.victory"),
]


def _unit_index():
    """dotted module path -> manifest unit, from module_contracts' `sim_module`."""
    import yaml
    contracts = ci_common.load_yaml(os.path.join(REPO, 'references', 'module_contracts.yaml'))
    idx = {}
    for c in contracts.get('modules') or []:
        code = c.get('sim_module')
        if not isinstance(code, str) or code.strip().lower() in ('none', 'null', 'n/a', ''):
            continue
        abs_path = os.path.join(REPO, code)
        if code.endswith('.py'):
            idx[abs_path] = c['module']
        elif os.path.isdir(abs_path):
            # DIRECTORY POINTER. Three contracts name a package rather than a file
            # (personal_combat, social_contest, peninsular_strain -- 37 .py files). Indexing only
            # `.py` pointers left their execution attributed by path guess instead of by contract,
            # which is why social_contest showed up as an unmapped directory in the first trace.
            for dirpath, dirnames, filenames in os.walk(abs_path):
                dirnames[:] = [d for d in dirnames if d != '__pycache__']
                for fn in filenames:
                    if fn.endswith('.py'):
                        idx.setdefault(os.path.join(dirpath, fn), c['module'])
    return idx


def trace(seed: int, seasons: int):
    import importlib
    idx = _unit_index()

    phase_stack: list[str] = []
    # phase -> {unit -> call count}. Counts, not a set: "ran once at boot" and "ran 4,000 times
    # every season" are different facts and a set erases the difference.
    hits: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    # phase -> {file -> count} for files that map to NO unit, so unattributed work is visible
    # rather than silently dropped.
    unmapped: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    # phase -> {subsystem-dir -> count}: attribution by PATH, not by contract. Coarser and
    # clearly labelled, but it covers the 17 contracts that declare no code file.
    by_subsystem: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)

    def profiler(frame, event, arg):
        if event != 'call' or not phase_stack:
            return
        path = frame.f_code.co_filename
        if not path.startswith(REPO):
            return
        unit = idx.get(path)
        if unit:
            hits[phase_stack[-1]][unit] += 1
        elif path.startswith((os.path.join(REPO, 'engine'), os.path.join(REPO, 'systems'))):
            rel = os.path.relpath(path, REPO)
            unmapped[phase_stack[-1]][rel] += 1
            # SECOND-BEST ATTRIBUTION, marked as such. Only 10 of 27 contracts declare a
            # `sim_module`, so most executing code has no contract file pointer -- mass_battle's
            # is literally null, which is why the campaign's hottest path (massbattle.py) lands
            # here. `systems/<subsystem>/...` is the ED-IN-0071 P4 rule "one subsystem = one
            # folder", so the directory IS a fact about ownership, just a coarser one than a
            # contract. Kept separate from `hits` so nobody reads a path guess as a contract join.
            parts = rel.split(os.sep)
            if parts[0] == 'systems' and len(parts) > 1:
                by_subsystem[phase_stack[-1]][parts[1]] += 1
            elif parts[0] == 'engine' and len(parts) > 1:
                by_subsystem[phase_stack[-1]][f"engine/{parts[1]}"] += 1

    def wrap(mod_path, attr, phase):
        mod = importlib.import_module(mod_path)
        original = getattr(mod, attr)

        def wrapped(*a, **k):
            phase_stack.append(phase)
            try:
                return original(*a, **k)
            finally:
                phase_stack.pop()
        setattr(mod, attr, wrapped)
        return mod, attr, original

    restore = [wrap(*b) for b in BOUNDARIES]
    try:
        from engine import mc_v18
        sys.setprofile(profiler)
        try:
            mc_v18.run_campaign(seed=seed,
                                params={'ECHO_TRANSPORT': True, 'CAMPAIGN_SEASONS': seasons})
        finally:
            sys.setprofile(None)
    finally:
        for mod, attr, original in restore:
            setattr(mod, attr, original)

    return hits, unmapped, by_subsystem


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=20260803)
    ap.add_argument('--seasons', type=int, default=12)
    ap.add_argument('--json', default=os.path.join(REPO, 'references', 'execution_trace.json'))
    args = ap.parse_args(argv)

    hits, unmapped, by_subsystem = trace(args.seed, args.seasons)
    out = {
        "_generated": ("GENERATED by tools/trace_execution_phases.py. Which module code ACTUALLY "
                       "executes in each phase of ONE seeded campaign. Absence means 'not observed "
                       "at this seed', not 'dead'. Presence is hard evidence."),
        "seed": args.seed,
        "seasons": args.seasons,
        "phases": {p: dict(c.most_common()) for p, c in sorted(hits.items())},
        "by_contract": {p: dict(c.most_common()) for p, c in sorted(hits.items())},
        "by_subsystem_path": {p: dict(c.most_common()) for p, c in sorted(by_subsystem.items())},
        "unmapped_files": {p: dict(c.most_common(8)) for p, c in sorted(unmapped.items())},
    }
    with open(args.json, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1) + "\n")

    print(f"seed={args.seed} seasons={args.seasons}")
    for phase in sorted(hits):
        units = hits[phase]
        print(f"\n  {phase}")
        for unit, n in units.most_common():
            print(f"      {unit:24s} {n:>8,} calls")
        for sub, n in by_subsystem[phase].most_common():
            print(f"      ~{sub:23s} {n:>8,} calls   (by path, no contract pointer)")
    print(f"\n-> {os.path.relpath(args.json, REPO)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
