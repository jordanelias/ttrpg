"""engine/cross_scale/combat_bridge.py — the IN-side of the combat seam (NEW, ED-IN-0091 plan
§2.2, OI-01: "Campaign loop cannot reach the canonical combat resolver" —
`audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §2.2 / §3 Wave 1 stage 3).

WHAT THIS IS
------------
scene_dispatch's combat branch used to call the DEPRECATED
`systems.combat.sim.combat.resolve_combat_round` (retired 2026-09-25, ED-900/904, ED-1029) and
deferred whenever the aggregate World held no personal-scale actors (scene_dispatch.py's own "DELIBERATE BOUNDARIES" note: "combat... still
defer[s] (no bridge exists for those actor shapes)"). This module is that bridge's combat half —
the mirror of `_emergency_council_parties` (ED-SC-0006), which closed the identical gap for the
`contest` branch. It is IN-side only (`engine/cross_scale/`); it imports
`systems/combat/combat_engine_v1/` as a consumer, and per the PC-lane seam declaration
(plan §0 "Concurrency & lane partition") this module and everything under `engine/cross_scale/`
may NOT edit anything under `systems/combat/` — a wrapper-side need is filed to the PC session,
never patched here.

PARTY DERIVATION (mirrors `_emergency_council_parties`, ED-SC-0006 — same pattern, new field)
----------------------------------------------------------------------------------------------
`_emergency_council_parties` derives two CONTEST "faculty" ints from ONE faction's own already-
cited aggregate stats (`Faction.L`, `Faction.Sta`) because no player-character schema exists at
this (aggregate, Monte-Carlo) scale — CLAUDE.md §5's no-fabrication rule forbids inventing a
personal actor. Combat needs a fuller object (`combatant.Combatant` — weapon, armour, nine
attributes) than the contest kernel does, so the same discipline is applied differently: EXACTLY
ONE field, `history` (the field the resolution pool is keyed off — `core.resolution_pool`, PC's
own OI-44 formula, mirrors `Pool.size`'s role in the contest kernel), is derived from a faction's
own aggregate `Mil` (Military — the one Faction stat that is combat-relevant, unlike `L`/`Sta`
which the contest side already claimed). EVERY OTHER Combatant field is left at the class's own
pre-existing constructor default (`Combatant.__init__`'s own defaults: strength=4, agi=4, end=4,
cog=3, att=3, spirit=3, focus=3, disp=4, weapon='arming', armor='light', tradition='none') — not
invented by this bridge, not tuned, exactly what every other caller of `Combatant()` gets when it
supplies no override. [SEED — a provisional derivation, same status as `_emergency_council_parties`
itself: open to Jordan revision, not itself a P0 fork.] The two sides are two DIFFERENT factions in
conflict (unlike the contest branch's single-faction two-facets frame — a combat scene has an
attacker and a defender, not one faction debating itself), named via `ctx['factions'] = (fid_a,
fid_b)` — a new ctx contract this module defines, since nothing in the live loop yet queues a
`combat` scene_type (verified: no `queue_scene("combat", ...)` call site exists anywhere in the
tree at this wave — grepped 2026-07-29). `derive_parties` returns `None` (a context-derivation gap,
flagged by the caller, never faked here) when `ctx['factions']` is absent or either faction id does
not resolve.

RESOLUTION — the wrapper's PUBLIC API, as-is
---------------------------------------------
`combat_engine_v1/wrapper.py`'s public entry point is `fight(A, B, cfg=None, rng=None,
max_bouts=12) -> int` (+1 = A wins, -1 = B wins, 0 = unresolved after `max_bouts` — read directly
off the wrapper source's own `# +1 => A won` comment at its `result = -1 if loser is A else 1`
line, not inferred). Unlike the contest kernel (which resolves off the global
`random` module, forcing scene_dispatch's contest branch to reseed-then-restore global state),
`fight()` takes an explicit `rng` — so this bridge derives one `random.Random` from the caller's
world-seeded stream and passes it straight through; no global-state save/restore needed.

CHARACTERIZATION, NOT OUTCOME (critic F2, plan §0 "Seam terms for the wrapper")
--------------------------------------------------------------------------------
`resolve()`'s return dict is the SHAPE the seam's characterization test
(`engine/tests/test_combat_bridge_seam.py`) pins — schema, determinism under a fixed seed, and the
presence of the fields the dispatch slot below consumes. It never pins a damage value, a win rate,
or any balance quantity: a PC rebalance must not turn that test red.
"""
from __future__ import annotations

import random as _random_mod

from engine.substrate import pc_engine

# SEAM CONSUMED (widened from the plan's "wrapper public API" declaration — recorded in
# audit/2026-07-29-code-shape-open-items/04_execution_ledger.md): `wrapper.fight(A, B, cfg, rng,
# max_bouts)` + the `combatant.Combatant` constructor, both PC-owned, consumed AS-IS, never edited
# here.
#
# combat_engine_v1/ is a non-package "scripts-on-path" directory (CLAUDE.md §3: "stays a
# non-package scripts-on-path dir; only systems/combat/ + systems/combat/sim/ are packages"), so it
# is loaded through the ONE path seam, engine/substrate/pc_engine.py (2026-09-25; this module's
# former private loader was one of two copies of that insert). `pc_engine.load()` runs on first
# actual use and RAISES on a missing tree, which this bridge lets propagate. Importing pc_engine is
# side-effect-free, so `import combat_bridge` still never mutates sys.path, and the flag-OFF world
# (DISPATCH_COMBAT_BRIDGE off) never touches the PC combat_engine_v1 tree.


def _combatant_from_faction_mil(fid, world):
    """Derive ONE personal-combat side from `fid`'s own aggregate `Mil` stat (see module
    docstring). Returns `None` if `fid` does not name a live faction on `world`."""
    f = getattr(world, "factions", {}).get(fid)
    if f is None:
        return None
    history = max(1, round(f.Mil))
    return pc_engine.load().combatant.Combatant(label=fid, history=history)


def derive_parties(ctx, world):
    """Derive the two `Combatant` sides for a queued `combat` scene from `ctx['factions'] =
    (fid_a, fid_b)` — two DIFFERENT factions in conflict, each contributing its own Combatant via
    `_combatant_from_faction_mil`. Returns `(Combatant, Combatant)`, or `None` on a
    context-derivation gap (missing/short `ctx['factions']`, or either id not resolving to a live
    faction) — the caller (scene_dispatch) is responsible for flagging that gap, never this
    module inventing a substitute."""
    fids = ctx.get("factions")
    if not fids or len(fids) < 2:
        return None
    a = _combatant_from_faction_mil(fids[0], world)
    b = _combatant_from_faction_mil(fids[1], world)
    if a is None or b is None:
        return None
    return (a, b)


def resolve(a, b, rng):
    """Call `combat_engine_v1/wrapper.py`'s public `fight(A, B, cfg=None, rng=None,
    max_bouts=12)` AS-IS. `rng` is the caller's world-seeded stream (a `random.Random`-like
    object exposing `.getrandbits`); this bridge derives a fresh, independent `random.Random`
    from it so the same campaign seed reproduces the same combat outcome without touching any
    global RNG state. Returns a small typed dict — SHAPE ONLY, see module docstring's
    "CHARACTERIZATION, NOT OUTCOME" note: `{'result': -1|0|1, 'winner': label|None, 'a_label':
    str, 'b_label': str, 'a_history': int, 'b_history': int}`."""
    fight_rng = _random_mod.Random(rng.getrandbits(32))
    result = pc_engine.load().wrapper.fight(a, b, rng=fight_rng)
    winner = a.label if result == 1 else (b.label if result == -1 else None)
    return {
        "result": result,
        "winner": winner,
        "a_label": a.label,
        "b_label": b.label,
        "a_history": a.history,
        "b_history": b.history,
    }
