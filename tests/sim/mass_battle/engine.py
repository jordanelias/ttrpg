"""mass_battle.engine — public API wrapper for the mass-battle engine.
Imports all modules and re-exports the full namespace, so `from mass_battle.engine import *`
(and the sim_mb_sigma.py shim) yields the same names the monolith exposed.
Also defines MECHANICS: a registry of canonical mechanic -> implementing symbol + toggle +
canonical source + status, with a self-test asserting every registered mechanic resolves."""
from mass_battle.config import *
from mass_battle.core.exchange import *  # [Stage-1] resolver layer: pool-assembly primitives
from mass_battle.core.state import *     # [Stage-1] resolver layer: morale/discipline/rout transitions
from mass_battle.core.attrition import * # [Stage-1] resolver layer: Lanchester attrition law
from mass_battle.core.contact import *   # [Stage-1] targeting + contact detection
from mass_battle.troop_types.registry import *  # [Stage-1] troop-type stats + gated roles
from mass_battle.hierarchy.units import *  # [Stage-1] Subunit/Unit data model
from mass_battle.geometry import *
from mass_battle.percell import *
from mass_battle.resolution import *
from mass_battle.orchestration import *

import mass_battle.config as _cfg
import mass_battle.core.exchange as _ce
import mass_battle.core.state as _cs
import mass_battle.core.attrition as _ca
import mass_battle.core.contact as _cc
import mass_battle.troop_types.registry as _tt
import mass_battle.hierarchy.units as _hu
import mass_battle.geometry as _geo
import mass_battle.percell as _pc
import mass_battle.resolution as _res
import mass_battle.orchestration as _orch

# Re-export contract used by gauge_mb.py (and any external caller):
#   Subunit, Unit, run_battle, run_multi_turn_battle, run_multi_unit_battle,
#   SIDE_A_START_ROW, SIDE_B_START_ROW, plus the full mechanic surface via import *.

def _resolve(sym):
    for m in (_ce,_cs,_ca,_cc,_tt,_hu,_orch,_res,_pc,_geo,_cfg):
        if hasattr(m, sym): return getattr(m, sym)
    return None

# MECHANICS registry — name -> {fn, toggle (env var or None), source, status}
# status: WIRED | PARTIAL | STUB. Mirrors the completeness audit (designs/audit/.../mb_engine_completeness_audit.md).
MECHANICS = {
    # geometry / deployment
    "cell_layout":        {"fn":"oriented_pattern",      "toggle":None,        "source":"mass_battle_v30 §A.3b", "status":"WIRED"},
    "octagon_facing":     {"fn":"octagon_angle",         "toggle":None,        "source":"Jordan design (per-cell octagon)", "status":"WIRED"},
    "support_vector":     {"fn":"_support_along_vector", "toggle":None,        "source":"engine S4 seam", "status":"WIRED"},
    "cell_speed":         {"fn":"cell_speed",            "toggle":None,        "source":"precedents_warfare (Leuctra)", "status":"WIRED"},
    # resolution core
    "pool_roll":          {"fn":"roll_pool",             "toggle":None,        "source":"params/core.md", "status":"WIRED"},
    "degree":             {"fn":"compute_degree",        "toggle":None,        "source":"params/core.md", "status":"WIRED"},
    "sigma_net_boost":    {"fn":"_sigma_net_boost",      "toggle":"SIGMA_HEAD","source":"modifier_system_spec §2.1", "status":"WIRED"},
    "sigma_softcap":      {"fn":"_sigma_softcap",        "toggle":None,        "source":"modifier_system_spec §3.1", "status":"WIRED"},
    "morale_sigma":       {"fn":"_morale_sigma",         "toggle":"MORALE_FIX","source":"mass_battle_v30 §A.4 (du Picq)", "status":"WIRED"},
    "casualties":         {"fn":"distribute_casualties", "toggle":None,        "source":"mass_battle_v30 §A.4", "status":"WIRED"},
    # per-cell layer
    "column_grid":        {"fn":"build_column_grid",     "toggle":"PER_CELL",  "source":"derived_stats / Incr1-4", "status":"WIRED"},
    "fatigue":            {"fn":"_fatigue_sigma",        "toggle":"PER_CELL",  "source":"engine fatigue model", "status":"WIRED"},
    "defender_depth":     {"fn":"_defender_depth",       "toggle":"PER_CELL",  "source":"Jordan handoff depth-damping", "status":"WIRED"},
    "charge_shock":       {"fn":"_charge_shock_sigma",   "toggle":"PER_CELL",  "source":"mass_battle_v30 §A.8 + du Picq (Phase 3, ratified)", "status":"WIRED"},
    "envelopment_wrap":   {"fn":"_momentum_speed",       "toggle":"PC_REFUSE", "source":"Cannae/Adrianople (M3 wheel/wrap)", "status":"WIRED"},
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
    "lanchester_attrition":{"fn":"_lanchester_strength","toggle":"LANCHESTER_ENABLED","source":"mb_lanchester_design.md §3 — linear melee / square volley (P-L)", "status":"WIRED"},
    "command_sigma_base": {"fn":"command_base_pool",   "toggle":"COMMAND_SIGMA_ENABLED","source":"ED-899 / Jordan 2026-06-02 — Command-only base; sets aside PP-233 Size pool", "status":"WIRED"},
    "command_derivation": {"fn":"derive_command",       "toggle":"COMMAND_SIGMA_ENABLED","source":"ED-899 — Command = f(Charisma primary, Cognition secondary)", "status":"WIRED"},
}

def mechanics_selftest():
    """Assert every registered mechanic resolves to a real symbol. Returns (ok, missing)."""
    missing = [name for name,spec in MECHANICS.items() if _resolve(spec["fn"]) is None]
    return (len(missing)==0, missing)


# ─── WRAPPER DUTIES (Stage-1 finish): the wrapper adapts + routes; it RESOLVES NOTHING. ─────────────
# build_* are the faction→unit ADAPTER; resolve_battle is the battle-type ROUTER. Both delegate to the
# lower layers (hierarchy.units for the data model, orchestration for the loop) — no resolution logic
# lives here. This is the P1 seam: engine.py = adapter + router + I/O, never an outcome computation.

def build_unit(shape, tier, name, faction, anchor_col, *, troop_type='infantry', unit_type='melee',
               power=4, command=4, discipline=5, morale=6, morale_start=None, stance='balanced',  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
               speed='Standard', instructions=(), dr=1, role=None):
    """Faction→unit ADAPTER: construct a single-subunit Unit. The canonical public constructor — the
    wrapper's adapter duty. Deployment follows the engine convention (faction A faces −row from
    SIDE_A_START_ROW; B faces +row from SIDE_B_START_ROW); `anchor_col` is the deployment column. Draws
    the data model from hierarchy.units and stats as given; resolution stays in core/. No outcome logic.

    [Stage D, ED-907 L3] `role` (default None, byte-exact for every existing call) is validated via
    troop_types.registry.role_allowed(troop_type, role) — raises ValueError on a disallowed combo —
    and stored on the Subunit; unlike build_army, shape/instructions here stay caller-controlled (both
    are already required/explicit in this single-subunit constructor's own signature, so there is no
    role->shape defaulting ambiguity to resolve)."""
    if role is not None and not role_allowed(troop_type, role):
        raise ValueError(f"role {role!r} not allowed for troop_type {troop_type!r} "
                          f"(allowed: {roles_for(troop_type)})")
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    su = Subunit(shape=shape, troop_type=troop_type, tier=tier,
                 starting_position=(start_row, anchor_col), advance_dir=advance_dir,
                 unit_type=unit_type, instructions=tuple(instructions), role=role)
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=[su], dr=dr, stance=stance, speed=speed)


def build_army(specs, name, faction, *, power=4, command=4, discipline=5, morale=6,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit]
               morale_start=None, dr=1, stance='balanced', speed='Standard'):
    """Faction→ARMY adapter: construct a MULTI-subunit Unit from a list of per-subunit spec dicts.
    `gauge_mb.make_mixed_unit` already proves the data model supports independently-placed/typed/tasked
    subunits, but that constructor is gauge-harness-local; this is the public, workbench-facing
    equivalent (mirrors its spec-dict-list shape). `build_unit` (single-subunit) is untouched.

    specs: list of dicts, one per subunit. Each may set shape (required UNLESS role is given — see
    below), tier (default 3), troop_type (default 'infantry'), unit_type (default 'melee'),
    starting_position (default: staggered down the battlefield from this faction's start row — mirrors
    make_mixed_unit's own deployment-layout convenience default; CALIBRATED, not historically cited,
    see sim_verification_ledger.json), stance, instructions, troops, concentration, and per-subunit
    power/discipline/morale/morale_start/dr/stamina/stamina_max overrides.

    A canonical troop type (TROOP_TYPE_STATS) draws its §B.2 Power/Discipline/Morale presets via
    Subunit.of_type unless the spec overrides them; a non-canonical type (e.g. bare 'infantry')
    inherits the parent Unit's fallbacks below — same behavior as build_unit/make_mixed_unit.

    troops/concentration ARE forwarded here (make_mixed_unit's own 2-line omission — it never popped
    these two keys from its per-subunit spec dict, so a caller-supplied density silently vanished).

    Each subunit's advance_dir is set from faction (matching build_unit's convention) rather than left
    at the dataclass default of 1 for every subunit regardless of side (make_mixed_unit does not set
    this at all) — a deliberate correction, not a mirroring gap: a subunit placed wide via
    starting_position (the whole point of exposing placement here) must still advance toward the enemy
    on its own side's correct axis on the legacy (non-FIELD_MOVEMENT) path.

    [Stage D, ED-907 L3] `role` WIRES the previously-inert Subunit.role: a spec may set `role` (one of
    ROLE_SPEC's keys, e.g. 'ShieldWall'/'Skirmish'/'Shock') instead of `shape`, gated by
    troop_types.registry.role_allowed(troop_type, role) — a role not in that troop type's menu
    (TROOP_TYPE_ROLES) raises ValueError at construction time (fails loud, matching the Order trigger
    validation precedent) rather than silently building an incoherent army. When role is given and
    `shape`/`instructions` are NOT also explicitly set in the spec, both default from ROLE_SPEC[role]
    ('the FM position->role model': a role names a typical shape + instruction package). An explicit
    shape/instructions in the spec always wins over the role's defaults. role is also stored on the
    resulting Subunit (build_army/build_unit never set it before this — the reason it was confirmed
    inert: nothing ever populated it outside ad-hoc test scripts).

    Zero existing call site touched (role defaults to None -> every existing spec dict, which never set
    it, is byte-exact); net-new function, byte-exact by construction.
    [canonical: gauge_mb.make_mixed_unit — the spec-dict-list shape this mirrors; config.py
    TROOP_TYPE_ROLES/ROLE_SPEC — the role->shape/instructions menu this wires]"""
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    subs = []
    for i, sp in enumerate(specs):
        sp = dict(sp)
        pos = sp.pop('starting_position', (start_row, 15 + i * 4))  # [canonical: sim_verification_ledger.json — CALIBRATED gauge_mb.py make_mixed_unit deployment-layout convenience default]
        tt = sp.pop('troop_type', 'infantry')
        role = sp.pop('role', None)
        if role is not None and not role_allowed(tt, role):
            raise ValueError(f"role {role!r} not allowed for troop_type {tt!r} "
                              f"(allowed: {roles_for(tt)})")
        role_spec = ROLE_SPEC.get(role) if role is not None else None
        shape = sp.pop('shape', None)
        if shape is None:
            if role_spec is None:
                raise ValueError("build_army spec needs 'shape' or a 'role' present in ROLE_SPEC")
            shape = role_spec['shape']
        tier = sp.pop('tier', 3)
        instructions = sp.pop('instructions', None)
        if instructions is None:
            instructions = role_spec['instructions'] if role_spec is not None else ()
        kw = dict(unit_type=sp.pop('unit_type', 'melee'), stance=sp.pop('stance', stance),
                  instructions=tuple(instructions), advance_dir=advance_dir, role=role)
        for k in ('power', 'discipline', 'morale', 'morale_start', 'dr', 'stamina', 'stamina_max',
                  'troops', 'concentration'):
            if k in sp:
                kw[k] = sp.pop(k)
        subs.append(Subunit.of_type(tt, shape, tier, pos, **kw))
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=subs, dr=dr, stance=stance, speed=speed)


def build_envelopment(center_specs, wing_specs, name, faction, *,
                       release_tick=4,  # [canonical: sim_verification_ledger.json — CALIBRATED, mirrors Stage C.4's acceptance-test hold duration, not independently historically cited]
                       power=4, command=4, discipline=5, morale=6, morale_start=None, dr=1,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit/build_army]
                       speed='Standard'):
    """[Stage D, ED-909] Unit-level 'Envelopment' allocation-grid preset (the Cannae 216 BC pattern):
    ED-909 retires Horseshoe/RefusedFlank as SUBUNIT-level shapes (LC-8) and re-realizes them as
    emergent, multi-body UNIT-level postures composed from Line/Arrowhead/GappedLine subunits —
    "why is Horseshoe a subformation instead of an emergent strategy," Jordan's own live-fire question.
    This is that composition, built entirely from EXISTING, already-verified primitives: build_army
    (placement) + Stage C's timed Order queue + the pre-existing, UNMODIFIED 'envelop' instruction
    (units.py's phase-1/phase-2 wrap logic) — confirmed in Stage C.4's acceptance test to need no new
    flanking mechanic at all.

    center_specs/wing_specs: build_army-style per-subunit spec lists. Centers are placed and tasked
    exactly as given (typically a hold/anvil role at the front). Wings additionally get stance='hold'
    (a spec's own explicit stance still wins) and, UNLESS the spec already queues its own `orders`, a
    `tick:{release_tick}` order that releases them into stance='balanced' + instructions including
    'envelop' — holding the "bow" while the center absorbs contact, then wheeling wide to close behind
    the enemy line, matching the historical sequencing this preset is named for.

    [Deferred, NOT done here] The literal LC-8 removal of 'Horseshoe'/'RefusedFlank' as Subunit.shape
    values (retiring them from geometry.CELL_PATTERN_FN/config.MIN_DISCIPLINE) is NOT part of this
    change: bat.py's frozen byte-exact golden digests (the grid path's non-negotiable regression
    oracle) were computed against battles that use 'Horseshoe' as a direct Subunit.shape, so removing
    it would break that invariant and needs Jordan's explicit sign-off + a deliberate re-baseline, not
    a default execution of "LC-8 is not a fresh design decision." This preset delivers ED-909's INTENT
    (envelopment as a Unit-level composition) without that byte-exact-breaking step; the legacy shape
    values remain available, now understood as legacy/subunit-only options rather than the canonical
    way to build an envelopment.
    [canonical: designs/provincial/mass_battle_v30.md — Cannae 216 BC precedent; ED-909]"""
    specs = [dict(sp) for sp in center_specs]
    n_center = len(specs)
    for sp in wing_specs:
        sp = dict(sp)
        sp.setdefault('stance', 'hold')
        specs.append(sp)
    unit = build_army(specs, name, faction, power=power, command=command, discipline=discipline,
                       morale=morale, morale_start=morale_start, dr=dr, speed=speed)
    for atom in unit.subunits[n_center:]:
        if not atom.orders:
            released = tuple(dict.fromkeys(atom.instructions + ('envelop',)))  # de-dup, order-preserving
            atom.orders = (Order(f'tick:{release_tick}', {'stance': 'balanced', 'instructions': released}),)
    return unit


def build_refused_flank(strong_specs, refused_specs, name, faction, *,
                         refuse_range=3,  # [canonical: sim_verification_ledger.json — CALIBRATED, reuses the existing PC_PIN_REACH adjacency-scale convention, not independently historically cited]
                         power=4, command=4, discipline=5, morale=6, morale_start=None, dr=1,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit/build_army]
                         speed='Standard'):
    """[Stage D, ED-909] Unit-level 'Refused Flank' allocation-grid preset (Leuctra 371 BC /
    Leuthen 1757): the other emergent army posture ED-909 names alongside Envelopment. strong_specs
    (the attacking wing/center) are placed and tasked as given; refused_specs (the withheld wing) get
    stance='hold' and, UNLESS the spec already queues its own `orders`, an 'enemy_range:{refuse_range}'
    order releasing into stance='balanced' — the refused wing does not advance or chase, but will fight
    once an enemy actually closes to that range, matching the historical "declines general engagement,
    holds if directly pressed" doctrine. Reuses Stage C's existing enemy_range order trigger; no new
    mechanic. Same LC-8 deferral note as build_envelopment (see its docstring) applies here."""
    specs = [dict(sp) for sp in strong_specs]
    n_strong = len(specs)
    for sp in refused_specs:
        sp = dict(sp)
        sp.setdefault('stance', 'hold')
        specs.append(sp)
    unit = build_army(specs, name, faction, power=power, command=command, discipline=discipline,
                       morale=morale, morale_start=morale_start, dr=dr, speed=speed)
    for atom in unit.subunits[n_strong:]:
        if not atom.orders:
            atom.orders = (Order(f'enemy_range:{refuse_range}', {'stance': 'balanced'}),)
    return unit


def resolve_battle(*args, kind='multi', **kwargs):
    """Battle-type ROUTER — the wrapper's routing duty. Transparently dispatches to the loop in
    orchestration; it computes no outcome itself. Kinds:
      'single'     → run_battle(unit_a, unit_b, max_turns=18)
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


_WRAPPER_API = {"build_unit", "build_army", "build_envelopment", "build_refused_flank", "resolve_battle"}

_mods = (_cfg,_ce,_cs,_ca,_cc,_tt,_hu,_geo,_pc,_res,_orch)
__all__ = sorted({n for _m in _mods for n in getattr(_m,'__all__',[])} | {"MECHANICS","mechanics_selftest"} | _WRAPPER_API)
