"""systems.mass_battle.sim.engine — public API wrapper for the mass-battle engine.
Imports all modules and re-exports the full namespace, so `from systems.mass_battle.sim.engine import *`
(and the sim_mb_sigma.py shim) yields the same names the monolith exposed.
Also defines MECHANICS: a registry of canonical mechanic -> implementing symbol + toggle +
canonical source + status, with a self-test asserting every registered mechanic resolves."""
from modules.mass_battle.config import *
from modules.mass_battle.core.exchange import *  # [Stage-1] resolver layer: pool-assembly primitives
from modules.mass_battle.core.state import *     # [Stage-1] resolver layer: morale/discipline/rout transitions
from modules.mass_battle.core.attrition import * # [Stage-1] resolver layer: Lanchester attrition law
from modules.mass_battle.core.contact import *   # [Stage-1] targeting + contact detection
from modules.mass_battle.troop_types.registry import *  # [Stage-1] troop-type stats + gated roles
from modules.mass_battle.hierarchy.units import *  # [Stage-1] Unit/Army data model
from modules.mass_battle.geometry import *
from modules.mass_battle.percell import *
from modules.mass_battle.resolution import *
from modules.mass_battle.orchestration import *
from systems.mass_battle.sim.multi import *  # the multi-battle loops: workbench code, not the module's (B17.05)

import modules.mass_battle.config as _cfg
import modules.mass_battle.core.exchange as _ce
import modules.mass_battle.core.state as _cs
import modules.mass_battle.core.attrition as _ca
import modules.mass_battle.core.contact as _cc
import modules.mass_battle.troop_types.registry as _tt
import modules.mass_battle.hierarchy.units as _hu
import modules.mass_battle.geometry as _geo
import modules.mass_battle.percell as _pc
import modules.mass_battle.resolution as _res
import modules.mass_battle.orchestration as _orch
import systems.mass_battle.sim.multi as _multi

# Re-export contract used by gauge_mb.py (and any external caller):
#   Unit, Army, run_battle, run_multi_turn_battle, run_multi_unit_battle,
#   SIDE_A_START_ROW, SIDE_B_START_ROW, plus the full mechanic surface via import *.

def _resolve(sym):
    for m in (_ce,_cs,_ca,_cc,_tt,_hu,_orch,_multi,_res,_pc,_geo,_cfg):
        if hasattr(m, sym): return getattr(m, sym)
    return None

# MECHANICS registry — name -> {fn, toggle (env var or None), source, status}
# status: WIRED | PARTIAL | STUB. Mirrors the completeness audit (audit/lane-c/2026-06-01-massbattle-stub-wiring_mb_engine_completeness_audit.md).
MECHANICS = {
    # geometry / deployment
    "cell_layout":        {"fn":"oriented_pattern",      "toggle":None,        "source":"mass_battle_v30 §A.3b", "status":"WIRED"},
    "octagon_facing":     {"fn":"octagon_angle",         "toggle":None,        "source":"Jordan design (per-cell octagon)", "status":"WIRED"},
    "support_vector":     {"fn":"_support_along_vector", "toggle":None,        "source":"engine S4 seam", "status":"WIRED"},
    "cell_speed":         {"fn":"cell_speed",            "toggle":None,        "source":"precedents_warfare (Leuctra)", "status":"WIRED"},
    # resolution core
    "pool_roll":          {"fn":"roll_pool",             "toggle":None,        "source":"params/core.md", "status":"WIRED"},
    # (degree ladder, sigma soft cap and net boost: the dice engine's, `dice_engine.degree_label` and `sigma_leverage.soft_cap` /
    #  `net_boost`, called from `orchestration` -- not this module's symbols since B05.03, so no row here)
    "morale_sigma":       {"fn":"_morale_sigma",         "toggle":"MORALE_FIX","source":"mass_battle_v30 §A.4 (du Picq)", "status":"WIRED"},
    "casualties":         {"fn":"distribute_casualties", "toggle":None,        "source":"mass_battle_v30 §A.4", "status":"WIRED"},
    # per-cell layer
    "column_grid":        {"fn":"build_column_grid",     "toggle":"PER_CELL",  "source":"derived_stats / Incr1-4", "status":"WIRED"},
    "fatigue":            {"fn":"column_stamina_share",  "toggle":"PER_CELL",  "source":"engine fatigue model; the contact draw's rounds_d (B19.12)", "status":"WIRED"},
    "defender_depth":     {"fn":"_defender_depth",       "toggle":"PER_CELL",  "source":"Jordan handoff depth-damping", "status":"WIRED"},
    "charge_shock":       {"fn":"_charge_shock_sigma",   "toggle":"PER_CELL",  "source":"mass_battle_v30 §A.8 + du Picq (Phase 3, ratified)", "status":"WIRED"},
    "envelopment_wrap":   {"fn":"_momentum_speed",       "toggle":"MB_REFUSE", "source":"Cannae/Adrianople (M3 wheel/wrap)", "status":"WIRED"},
    # orchestration / turn structure
    "assign_targets":     {"fn":"assign_targets",        "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "find_contacts":      {"fn":"find_contacts",         "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "engage":             {"fn":"resolve_engagements",   "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "cascade_order":      {"fn":"resolve_engagements_cascading","toggle":"CASCADING_ENABLED","source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "volley":             {"fn":"volley_phase",          "toggle":"VOLLEY_ENABLED","source":"mass_battle_v30 §A.7 Phase 2", "status":"WIRED"},
    "battle_turn":        {"fn":"run_battle",            "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "multi_turn":         {"fn":"run_multi_turn_battle", "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "rout":               {"fn":"rout_resolution",       "toggle":None,        "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "pursuit":            {"fn":"pursuit_damage",        "toggle":None,        "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "recall":             {"fn":"recall_check",          "toggle":None,        "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "morale_cascade":     {"fn":"discipline_check_cascade","toggle":None,      "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "between_turn_recovery":{"fn":"between_turn_recovery","toggle":None,       "source":"mass_battle_v30 §A.13", "status":"WIRED"},
    # attrition substrate (P-L) + command-only resolution (canon-structure, ED-899)
    "lanchester_attrition":{"fn":"engaged_files",       "toggle":None,"source":"the contact draw's frontage in men, each contact cell at 1/m of its pairs (B19.12, MBA-04 step 3)", "status":"WIRED"},
    "command_derivation": {"fn":"derive_command",       "toggle":"COMMAND_SIGMA_ENABLED","source":"ED-899 — Command = f(Charisma primary, Cognition secondary)", "status":"WIRED"},
}

def mechanics_selftest():
    """Assert every registered mechanic resolves to a real symbol. Returns (ok, missing)."""
    missing = [name for name,spec in MECHANICS.items() if _resolve(spec["fn"]) is None]
    return (len(missing)==0, missing)


# ─── ARMY CONSTRUCTION moved to modules/mass_battle/armies.py (the module closure): re-imported, not copied. ───
from modules.mass_battle.armies import (UNIT_CAP, DEPLOY_GAP, ENVELOP_WING_GAP, REFUSE_ECHELON,
                                        _spec_span, _centered_line_cols, build_army)
from modules.mass_battle.orderofbattle import place_posts   # [B19.18] the one reader of a formation row (the season's `_place` calls it too)


def build_unit(shape, tier, name, faction, anchor_col, *, troop_type='infantry', unit_type=None,
               power=4, command=4, discipline=5, morale=6, morale_start=None, stance='balanced',  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
               speed='Standard', instructions=(), dr=1, role=None):
    """Faction→unit ADAPTER: construct a single-subunit Army. The canonical public constructor — the
    wrapper's adapter duty. Deployment follows the engine convention (faction A faces −row from
    SIDE_A_START_ROW; B faces +row from SIDE_B_START_ROW); `anchor_col` is the deployment column. Draws
    the data model from hierarchy.units and stats as given; resolution stays in core/. No outcome logic.

    [Stage D, ED-907 L3] `role` (default None, byte-exact for every existing call) is validated via
    troop_types.registry.role_allowed(troop_type, role) — raises ValueError on a disallowed combo —
    and stored on the Unit; unlike build_army, shape/instructions here stay caller-controlled (both
    are already required/explicit in this single-subunit constructor's own signature, so there is no
    role->shape defaulting ambiguity to resolve).

    [movement audit gate 2, ED-MB-0001, Jordan-ruled 2026-07-02: "Ranged is troop type as per the
    weapon assigned to troop."] `unit_type` now defaults to None and, when not explicitly given by
    the caller, derives from troop_type's assigned weapon via troop_types.registry.unit_type_for
    (the troop file's `primary` arm/loadout_for) instead of the prior hardcoded 'melee'. An unmapped troop_type
    (e.g. the 'infantry' default) resolves to 'melee' either way, so every existing call site that
    relies on the default is byte-exact; only troop_type='archers'/'crossbow'/'sling'/'artillery'/
    'mounted_archers' (or a future loadout-mapped type) with no explicit unit_type now change."""
    if role is not None and not role_allowed(troop_type, role):
        raise ValueError(f"role {role!r} not allowed for troop_type {troop_type!r} "
                          f"(allowed: {roles_for(troop_type)})")
    if unit_type is None:
        unit_type = unit_type_for(troop_type)
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    su = Unit(shape=shape, troop_type=troop_type, tier=tier,
                 starting_position=(start_row, anchor_col), advance_dir=advance_dir,
                 unit_type=unit_type, instructions=tuple(instructions), role=role)
    return Army(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                units=[su], dr=dr, stance=stance, speed=speed)


def build_envelopment(center_specs, wing_specs, name, faction, *,
                       release_tick=4,  # [CALIBRATED-DEBT: mirrors Stage C.4's acceptance-test hold duration — magnitude fitted to engine behaviour, no external source; was tagged `canonical: sim_verification_ledger.json`, the bare-integer self-whitelist deleted in ED-MB-0041 Tier-0.1]
                       power=4, command=4, discipline=5, morale=6, morale_start=None, dr=1,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit/build_army]
                       speed='Standard', freeze_wings=False):
    """[Stage D, ED-909] Army-level 'Envelopment' allocation-grid preset (the Cannae 216 BC pattern):
    ED-909 retires Horseshoe/RefusedFlank as SUBUNIT-level shapes and re-realizes them as emergent,
    multi-body UNIT-level postures composed from Line/Arrowhead/GappedLine units — "why is
    Horseshoe a subformation instead of an emergent strategy," Jordan's own live-fire question. This
    is that composition, built entirely from EXISTING, already-verified primitives: build_army
    (placement) + Stage C's timed Order queue + the pre-existing, UNMODIFIED 'envelop' instruction
    (units.py's phase-1/phase-2 wrap logic) — confirmed in Stage C.4's acceptance test to need no new
    flanking mechanic at all.

    center_specs/wing_specs: build_army-style per-subunit spec lists. Centers are placed and tasked
    exactly as given (typically a hold/anvil role at the front). Wings additionally get stance='hold'
    (a spec's own explicit stance still wins) and, UNLESS the spec already queues its own `orders`, a
    `tick:{release_tick}` order that releases them into stance='balanced' + instructions including
    'envelop' — holding the "bow" while the center absorbs contact, then wheeling wide to close behind
    the enemy line, matching the historical sequencing this preset is named for.

    [LC-8, Jordan-approved 2026-07-02: "correct, retire them. those are emergent outcomes."]
    'Horseshoe'/'RefusedFlank' are now fully retired as Unit.shape values (removed from
    geometry.CELL_PATTERN_FN/config.MIN_DISCIPLINE) — this preset, not a literal shape choice, is the
    only way to build an envelopment. bat.py's grid-mode byte-exact golden digests were re-baselined
    for this change (a deliberate, verified behavior change, not a regression): three battery rows now
    build multi-subunit armies via this function/build_refused_flank instead of a single Horseshoe-
    shaped subunit.
    [canonical: designs/provincial/mass_battle_v30.md — Cannae 216 BC precedent; ED-909]

    [ED-MB-0002 §2 step 4, measurement only] `freeze_wings=True` (default False, zero effect on any
    existing call site/digest) skips attaching the release order entirely, leaving wing units
    permanently at `stance='hold'` for the whole battle instead of releasing into 'envelop' at
    `release_tick`. `stance == 'hold'` is an immediate early-return at the top of BOTH `_node_advance`
    and the legacy `advance_cells` (confirmed by direct read, hierarchy/units.py) -- fully sufficient
    to freeze position, no separate position-pinning mechanism needed. Used by the frozen-vs-wheeling
    gauge ablation to settle DG-5 (is a genuine maneuver-timing race live, or was RC-1's accounting
    layer sufficient on its own) -- an instrumentation-only toggle, not a design change."""
    # [ED-MB-0017] SYMMETRIC deployment (fixes P-2). The centre is bowed FORWARD on the field-centre anchor (the convex crescent apex); the
    # wings are split to OPPOSITE flanks -- left wings well left of the centre, right wings well right -- so `_envelop_goal` sends each
    # around the OPPOSITE flank (`ac < enemy-centre` -> wrap left; `ac > enemy-centre` -> wrap right), i.e. the two wings wheel in MIRROR,
    # the load-bearing invariant of a double envelopment (Cannae research §1/§5). [B19.18] The placement is the `envelopment` row of
    # `references/troops.yaml: formations` read by `orderofbattle.place_posts` (the season's `_place` calls the same function): the centre at
    # the `centre` post (the apex, `forward` rows ahead of the flank line), the wings alternately at `left` and `right` (wide of the centre's
    # ACTUAL span, so a caller-placed centre is flanked where it stands [ED-MB-0025]); an EXPLICIT `starting_position` is honoured as given.
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    center = [dict(sp) for sp in center_specs]
    n_center = len(center)
    wings = [dict(sp0) for sp0 in wing_specs]
    for sp in wings:
        sp.setdefault('stance', 'hold')
    specs = center + wings
    posts = ['centre'] * n_center + ['left' if i % 2 == 0 else 'right' for i in range(len(wings))]
    for i, pos in place_posts(specs, posts, 'envelopment', faction, start_row).items():
        specs[i]['starting_position'] = pos
    unit = build_army(specs, name, faction, power=power, command=command, discipline=discipline,
                       morale=morale, morale_start=morale_start, dr=dr, speed=speed)
    if not freeze_wings:
        for atom in unit.units[n_center:]:
            if not atom.orders:
                released = tuple(dict.fromkeys(atom.instructions + ('envelop',)))  # de-dup, order-preserving
                atom.orders = (Order(f'tick:{release_tick}', {'stance': 'balanced', 'instructions': released}),)
    return unit


def build_refused_flank(strong_specs, refused_specs, name, faction, *,
                         refuse_range=10,  # [ED-MB-0041 FIX] was 3 and NEVER FIRED. check_orders measures the
                         # subunit CENTROID to the nearest enemy cell; a refused wing's measured minimum
                         # approach in the live deployment is ~9.5, so 'enemy_range:3' was geometrically
                         # unsatisfiable and the refused wing held for the entire battle in EVERY caller
                         # (none overrides the default). 10 is the smallest value that actually triggers.
                         # [JUSTIFIED: magnitude set by direct measurement of the trigger geometry; the
                         # old tag cited a sim_verification_ledger.json row that does not exist.]
                         power=4, command=4, discipline=5, morale=6, morale_start=None, dr=1,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit/build_army]
                         speed='Standard'):
    """[Stage D, ED-909] Army-level 'Refused Flank' allocation-grid preset (Leuctra 371 BC /
    Leuthen 1757): the other emergent army posture ED-909 names alongside Envelopment. strong_specs
    (the attacking wing/center) are placed and tasked as given; refused_specs (the withheld wing) get
    stance='hold' and, UNLESS the spec already queues its own `orders`, an 'enemy_range:{refuse_range}'
    order releasing into stance='balanced' — the refused wing does not advance or chase, but will fight
    once an enemy actually closes to that range, matching the historical "declines general engagement,
    holds if directly pressed" doctrine. Reuses Stage C's existing enemy_range order trigger; no new
    mechanic. Same LC-8 retirement note as build_envelopment (see its docstring) applies here."""
    # [ED-MB-0017] OBLIQUE deployment (fixes P-3): strong + refused across one centred frontage (no lateral overlap), the REFUSED units
    # abutting the strong wing on its right and ECHELONED BACK out of contact range while the strong wing engages (Leuctra/Leuthen research
    # §2/§4). [B19.18] The placement is the `refused_flank` row of `references/troops.yaml: formations` read by `orderofbattle.place_posts`:
    # the strong units at `centre`, the refused at `right` (`forward` -6, `gap` 0), against the strong wing's ACTUAL span [ED-MB-0025]; an
    # EXPLICIT `starting_position` is honoured as given.
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    strong = [dict(sp) for sp in strong_specs]
    refused = [dict(sp) for sp in refused_specs]
    n_strong = len(strong)
    for sp in refused:
        sp.setdefault('stance', 'hold')
    specs = strong + refused
    for i, pos in place_posts(specs, ['centre'] * n_strong + ['right'] * len(refused), 'refused_flank', faction, start_row).items():
        specs[i]['starting_position'] = pos
    unit = build_army(specs, name, faction, power=power, command=command, discipline=discipline,
                       morale=morale, morale_start=morale_start, dr=dr, speed=speed)
    for atom in unit.units[n_strong:]:
        if not atom.orders:
            atom.orders = (Order(f'enemy_range:{refuse_range}', {'stance': 'balanced'}),)
    return unit


def resolve_battle(*args, kind='multi', **kwargs):
    """Battle-type ROUTER — the wrapper's routing duty. Transparently dispatches to the loop in
    orchestration or multi.py; it computes no outcome itself. Kinds:
      'single'     → run_battle(unit_a, unit_b, max_ticks=18)
      'multi'      → run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, max_battle_turns=8)
      'multi_unit' → run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, anchor_map, max_battle_turns=8)
    Args/kwargs pass straight through, so routing is byte-exact with calling the run_* function directly."""
    if kind == 'single':
        return run_battle(*args, **kwargs)
    if kind == 'multi':
        return run_multi_turn_battle(*args, **kwargs)
    if kind == 'multi_unit':
        return run_multi_unit_battle(*args, **kwargs)
    raise ValueError(f"resolve_battle: unknown kind {kind!r} (expected 'single' | 'multi' | 'multi_unit')")


_WRAPPER_API = {"build_unit", "build_army", "build_envelopment", "build_refused_flank", "resolve_battle", "UNIT_CAP"}

_mods = (_cfg,_ce,_cs,_ca,_cc,_tt,_hu,_geo,_pc,_res,_orch,_multi)
__all__ = sorted({n for _m in _mods for n in getattr(_m,'__all__',[])} | {"MECHANICS","mechanics_selftest"} | _WRAPPER_API)
