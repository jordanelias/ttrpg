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
# status: WIRED | PARTIAL | STUB. Mirrors the completeness audit (audit/lane-c/2026-06-01-massbattle-stub-wiring_mb_engine_completeness_audit.md).
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

# [ED-1090, Jordan-ruled 2026-07-02: "subunits can be as high as 11."] Videogame hard ceiling on
# simultaneously-commanded subunits — LIFTS the TTRPG hard cap of 3 (mass_battle_v30.md §A.5 Command
# Rating: "Sub-unit limit (max simultaneous commanded = Command; TTRPG hard cap: 3)", PP-504/ED-899 — a
# tabletop-bookkeeping limit a digital UI does not need). Command remains the span-of-control governor
# per §A.5; this is the absolute ceiling above it. Module-level (not local to build_army) so any other
# caller — notably the Army Configuration Mode UI (Stage E, workbench) — reads the single source
# instead of duplicating the literal. NOTE (flagged, not resolved): the ratified Command formula clamps
# to 1..7, so reaching 11 commanded subunits implies some future Command-exceeding mechanism (e.g.
# subordinate officers) — that reconciliation is queued for canon, not silently invented here.
SUBUNIT_CAP = 11  # [canonical: mass_battle_v30.md §A.5 Command Rating — videogame cap per ED-1090, superseding the TTRPG hard cap 3]

# ─── ARMY-LEVEL DEPLOYMENT GEOMETRY (ED-MB-0017) ──────────────────────────────
# [canonical: audit/2026-07-22-mass-battle-stress-test/pathing_deployment_diagnosis.md — multi-unit
#  deployment fix; historical geometry per the Cannae/Leuctra/triplex-acies research synthesis]
# The pre-fix `build_army` deployed subunit i at column `15 + i*4` — a rightward column-of-columns with a
# fixed 4-col step narrower than a battle-scale subunit's frontage, so subunits OVERLAPPED (P-1), the
# envelopment's "wings" both landed on ONE side of the centre (P-2, no double envelopment), and the
# refused wing sat level with the line, overlapping it (P-3). These helpers replace the fixed step with
# FRONTAGE-AWARE placement: a battle line centred on the anchor, symmetric wings for envelopment, and an
# echeloned-rear refused wing.
DEPLOY_GAP = 1        # [canonical: pathing_deployment_diagnosis.md §3 — lateral gap (cols) between adjacent subunits; a coherent line (hoplite ~0) not the wide manipular quincunx]
ENVELOP_WING_GAP = 3  # [canonical: pathing_deployment_diagnosis.md §3 / Cannae research §1 — wings sit WIDE of the centre's flanks (columns, refused slightly), clear of its frontage]
REFUSE_ECHELON = 6    # [canonical: pathing_deployment_diagnosis.md §2 / Leuctra research §2 — refused wing echeloned back so it cannot reach contact when the strong wing does (depth-ratio-grounded offset in rows)]


def _spec_span(sp):
    """(cmin, cmax) column span of a spec's footprint pattern, computed PRE-construction (so deployment
    can space subunits by their true frontage). Resolves shape from an explicit `shape` or a `role`."""
    shape = sp.get('shape')
    if shape is None and sp.get('role') is not None and sp['role'] in ROLE_SPEC:
        shape = ROLE_SPEC[sp['role']]['shape']
    shape = shape or 'Line'
    troops, conc = sp.get('troops'), sp.get('concentration')
    pat = footprint_for(shape, troops, conc, sp.get('troop_type')) if (troops is not None and conc is not None) \
        else CELL_PATTERN_FN[shape](sp.get('tier', 3))
    cs = [c for _r, c in pat]
    return (min(cs), max(cs)) if cs else (0, 0)


def _centered_line_cols(specs, anchor_col, gap=DEPLOY_GAP):
    """Deployment columns (the `starting_position` col for each spec) laying `specs` out as a battle line
    CENTRED on `anchor_col`, spaced by each subunit's own frontage + `gap` — so no two subunits overlap
    at any subunit count (P-1). Returns [col_i]; col_i places spec i's pattern so the block is centred.

    [ED-MB-0017, adversarial-review finding 1] The block is FIT to the battlefield so it can never place
    a cell off-board (which Subunit.__post_init__ rejects with a hard ValueError). A block that fits is
    left exactly centred (a no-op for every normal army — the presets and the ≤11-subunit test cases);
    an over-wide block (an army wider than the 50-cell field even at gap 0) is first re-tried at gap 0,
    then, if still too wide, LINEARLY COMPRESSED to fit — subunits then abut/overlap (no worse than the
    pre-fix `15 + i*4` layout, which also overlapped) rather than CRASHING. Degrade, don't crash."""
    spans = [_spec_span(s) for s in specs]

    def _place(g):
        widths = [cmax - cmin + 1 for cmin, cmax in spans]
        total = sum(widths) + g * (len(specs) - 1)
        x = anchor_col - total / 2.0
        cols = []
        for (cmin, _cmax), w in zip(spans, widths):
            cols.append(int(round(x - cmin)))
            x += w + g
        return cols

    lo_bound, hi_bound = 1, BATTLEFIELD_SIZE - 2          # keep a 1-cell margin inside [0, 49]
    cols = _place(gap)
    lo = min(c + s[0] for c, s in zip(cols, spans))
    hi = max(c + s[1] for c, s in zip(cols, spans))
    if lo < lo_bound or hi > hi_bound:                   # overflows the field
        cols = _place(0)                                 # first: close the gaps
        lo = min(c + s[0] for c, s in zip(cols, spans))
        hi = max(c + s[1] for c, s in zip(cols, spans))
        if hi > lo and (hi - lo) > (hi_bound - lo_bound):  # genuinely wider than the field -> compress
            scale = (hi_bound - lo_bound) / float(hi - lo)
            cols = [int(round(lo_bound + (c - lo) * scale)) for c in cols]
        else:                                            # fits after gap-0 -> just translate on-board
            shift = (lo_bound - lo) if lo < lo_bound else (hi_bound - hi)
            cols = [c + shift for c in cols]
    # Final per-subunit clamp: every subunit's own cells must land on-board even when the army is wider
    # than the field can hold at all (11 large blocks) -- clamp its start so [col+cmin, col+cmax] ⊆
    # [0, FIELD-1]. For a fitting army this is a no-op; for an impossible one subunits pile up/overlap at
    # the edge (no worse than the pre-fix overlap) instead of raising an off-board ValueError.
    cols = [max(-s[0], min(BATTLEFIELD_SIZE - 1 - s[1], c)) for c, s in zip(cols, spans)]
    return cols


def build_unit(shape, tier, name, faction, anchor_col, *, troop_type='infantry', unit_type=None,
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
    role->shape defaulting ambiguity to resolve).

    [movement audit gate 2, ED-MB-0001, Jordan-ruled 2026-07-02: "Ranged is troop type as per the
    weapon assigned to troop."] `unit_type` now defaults to None and, when not explicitly given by
    the caller, derives from troop_type's assigned weapon via troop_types.registry.unit_type_for
    (TROOP_LOADOUT/loadout_for) instead of the prior hardcoded 'melee'. An unmapped troop_type
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
    su = Subunit(shape=shape, troop_type=troop_type, tier=tier,
                 starting_position=(start_row, anchor_col), advance_dir=advance_dir,
                 unit_type=unit_type, instructions=tuple(instructions), role=role)
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=[su], dr=dr, stance=stance, speed=speed)


def build_army(specs, name, faction, *, power=4, command=4, discipline=5, morale=6,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit]
               morale_start=None, dr=1, stance='balanced', speed='Standard', anchor_col=25):
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

    [ED-1095, Jordan-ruled 2026-07-02] A spec with troop_type='mounted_archers' and NO explicit role
    AND no explicit shape/instructions implicitly defaults role to 'Kite' (kiting/stand-off posture
    instead of closing to melee) -- verified no existing call site anywhere in this package uses
    'mounted_archers', so this is a pure gap-fill, not a behavior change to any live spec. An explicit
    shape, explicit instructions, or explicit role in the spec always wins over this implicit default
    (same precedence as the role->shape/instructions defaulting above). build_unit intentionally does
    NOT get this same treatment -- its shape parameter is a required positional with no default, so
    there is no "unspecified shape" case there to fill (see its own docstring).
    [canonical: gauge_mb.make_mixed_unit — the spec-dict-list shape this mirrors; config.py
    TROOP_TYPE_ROLES/ROLE_SPEC — the role->shape/instructions menu this wires]"""
    # [ED-1090] SUBUNIT_CAP is module-level (see its definition above build_unit) so other callers
    # (Army Configuration Mode's UI) read the single source rather than duplicating the literal.
    if len(specs) > SUBUNIT_CAP:
        raise ValueError(f"build_army: {len(specs)} subunits exceeds the videogame cap of "
                          f"{SUBUNIT_CAP} (ED-1090; mass_battle_v30.md §A.5)")
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    # [ED-MB-0017] Frontage-aware, anchor-centred battle line: space subunits by their own frontage so
    # they never overlap (fixes P-1, the `15 + i*4` fixed-step overlap). A spec's explicit
    # `starting_position` always wins (envelopment/refused-flank presets and callers doing bespoke
    # placement); only specs that omit it get an auto column here.
    _auto_cols = _centered_line_cols(specs, anchor_col)
    subs = []
    for i, sp in enumerate(specs):
        sp = dict(sp)
        pos = sp.pop('starting_position', (start_row, _auto_cols[i]))
        tt = sp.pop('troop_type', 'infantry')
        role = sp.pop('role', None)
        # [ED-1095, Jordan-ruled 2026-07-02: "mounted archers shouldn't be closing in on the enemy--
        # they should be flying by and taking advantage of their range advantage with their bows."]
        # A mounted_archers spec with NO explicit role AND no explicit shape/instructions defaults to
        # the Kite role (kiting/stand-off posture) instead of silently closing to melee like any other
        # troop type. Checked BEFORE 'shape'/'instructions' are popped below so an explicit caller
        # choice of either is detected and always wins (matches every other precedence rule in this
        # function: explicit beats default). Mirrors the existing role->shape/instructions defaulting
        # immediately below, just with an implicit role instead of a caller-supplied one.
        if role is None and tt == 'mounted_archers' and 'shape' not in sp and 'instructions' not in sp:
            role = 'Kite'
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
        # [movement audit gate 2, ED-MB-0001] unit_type derives from tt's assigned weapon
        # (unit_type_for/TROOP_LOADOUT) rather than a hardcoded 'melee' -- an explicit spec value
        # still always wins. See build_unit's docstring for the byte-exact-preservation argument
        # (unmapped troop types, including the 'infantry' default, still resolve to 'melee').
        #
        # [2026-07-02 adversarial-review finding, ED-MB-0001] `sp.pop('unit_type', unit_type_for(tt))`
        # only falls back to derivation when the 'unit_type' KEY is absent from the spec dict -- an
        # explicit `{'unit_type': None, ...}` (the same None sentinel build_unit's own signature
        # uses to mean "derive it") would pop back None verbatim instead of deriving, inconsistent
        # with build_unit's `if unit_type is None: unit_type = unit_type_for(troop_type)` for the
        # identical sentinel. Matched to build_unit's own semantics here so both constructors treat
        # None the same way; no current spec anywhere sets unit_type=None explicitly, so this is a
        # latent-inconsistency fix, not a behavior change for any existing call site.
        spec_unit_type = sp.pop('unit_type', None)
        kw = dict(unit_type=spec_unit_type if spec_unit_type is not None else unit_type_for(tt),
                  stance=sp.pop('stance', stance),
                  instructions=tuple(instructions), advance_dir=advance_dir, role=role)
        for k in ('power', 'discipline', 'morale', 'morale_start', 'dr', 'stamina', 'stamina_max',
                  'troops', 'concentration', 'orders'):
            if k in sp:
                kw[k] = sp.pop(k)
        # [DG-4, ED-MB-0002, 2026-07-04 ruling: "Morale is blend of per-subunit as well as whole
        # unit."] Default every subunit to its OWN real starting morale (unless the spec already
        # overrode it above) instead of leaving it at the Subunit dataclass default of None. A None
        # morale falls through to the shared parent Unit.morale (eff_morale/erode_morale,
        # hierarchy/units.py:384-386,424-431) -- harmless for a single subunit, but for a composed
        # army it meant every subunit's own §A.4 casualty-fraction trigger independently wrote to
        # the SAME shared pool, double-eroding it (RC-1(b)). Giving each subunit its own copy closes
        # that double-count by construction -- no new state. The "whole unit" half of the blend is
        # NOT deleted: it emerges from Unit.agg_morale()/derive_rout() (~L1460-1481, a troop-weighted
        # aggregate of subunits' own eff_morale already used for whole-unit rout) and
        # cascade_morale_hit() (~L1482-1491, already-existing army-wide contagion), both of which
        # only activate meaningfully once subunits carry real values instead of None.
        # [2026-07-04 adversarial-review fix] `setdefault` only fires when the key is ABSENT -- a
        # spec that explicitly sets `'morale': None` (as opposed to omitting the key) would pop that
        # None into kw above and silently defeat this fix, leaving that one subunit back on the
        # shared-pool double-erosion path DG-4 exists to close. Explicit None-check instead, matching
        # this file's own `if unit_type is None: derive` precedent immediately above.
        if kw.get('morale') is None:
            kw['morale'] = morale
        if kw.get('morale_start') is None:
            kw['morale_start'] = kw['morale'] if morale_start is None else morale_start
        subs.append(Subunit.of_type(tt, shape, tier, pos, **kw))
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=subs, dr=dr, stance=stance, speed=speed)


def build_envelopment(center_specs, wing_specs, name, faction, *,
                       release_tick=4,  # [canonical: sim_verification_ledger.json — CALIBRATED, mirrors Stage C.4's acceptance-test hold duration, not independently historically cited]
                       power=4, command=4, discipline=5, morale=6, morale_start=None, dr=1,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit/build_army]
                       speed='Standard', freeze_wings=False):
    """[Stage D, ED-909] Unit-level 'Envelopment' allocation-grid preset (the Cannae 216 BC pattern):
    ED-909 retires Horseshoe/RefusedFlank as SUBUNIT-level shapes and re-realizes them as emergent,
    multi-body UNIT-level postures composed from Line/Arrowhead/GappedLine subunits — "why is
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
    'Horseshoe'/'RefusedFlank' are now fully retired as Subunit.shape values (removed from
    geometry.CELL_PATTERN_FN/config.MIN_DISCIPLINE) — this preset, not a literal shape choice, is the
    only way to build an envelopment. bat.py's grid-mode byte-exact golden digests were re-baselined
    for this change (a deliberate, verified behavior change, not a regression): three battery rows now
    build multi-subunit armies via this function/build_refused_flank instead of a single Horseshoe-
    shaped subunit.
    [canonical: designs/provincial/mass_battle_v30.md — Cannae 216 BC precedent; ED-909]

    [ED-MB-0002 §2 step 4, measurement only] `freeze_wings=True` (default False, zero effect on any
    existing call site/digest) skips attaching the release order entirely, leaving wing subunits
    permanently at `stance='hold'` for the whole battle instead of releasing into 'envelop' at
    `release_tick`. `stance == 'hold'` is an immediate early-return at the top of BOTH `_node_advance`
    and the legacy `advance_cells` (confirmed by direct read, hierarchy/units.py) -- fully sufficient
    to freeze position, no separate position-pinning mechanism needed. Used by the frozen-vs-wheeling
    gauge ablation to settle DG-5 (is a genuine maneuver-timing race live, or was RC-1's accounting
    layer sufficient on its own) -- an instrumentation-only toggle, not a design change."""
    # [ED-MB-0017] SYMMETRIC deployment (fixes P-2). The centre is bowed FORWARD on the field-centre
    # anchor (the convex crescent apex); the wings are split to OPPOSITE flanks — left wings well left of
    # the centre, right wings well right — so `_envelop_goal` sends each around the OPPOSITE flank
    # (`ac < enemy-centre` -> wrap left; `ac > enemy-centre` -> wrap right), i.e. the two wings wheel in
    # MIRROR (opposite rotational sense), the load-bearing invariant of a double envelopment
    # (Cannae research §1/§5). Pre-fix, `build_army`'s `15 + i*4` put both wings to the RIGHT of centre,
    # so both wrapped the same flank — no ring ever formed.
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    APEX = 2  # [canonical: Cannae research §1 — centre apex ~2-4 rank-units forward of the flank line]
    center = [dict(sp) for sp in center_specs]
    n_center = len(center)
    c_spans = [_spec_span(sp) for sp in center]
    # [ED-MB-0025 wing-placement fix] The wings must flank the centre's ACTUAL column. Previously the
    # wing boundaries (c_left/c_right) were derived from `_centered_line_cols(center, 25)` — a phantom
    # field-centre-anchored placement — even when the caller PRE-SET the centre's starting_position (as
    # the gauge's `_envelop_army` does, at the enemy's column). The wings then wrapped a centre that
    # wasn't there (landed cols 21/27 while the centre sat at col 9), so no ring ever formed around the
    # real body. Now: honour a pre-set centre column and place wings relative to THAT; only fall back to
    # the field-centre placement for centres with no explicit position (production/bat.py path unchanged).
    default_cols = _centered_line_cols(center, 25)  # field-centre anchor (BATTLEFIELD_SIZE 50)
    c_cols = []
    for sp, dcol in zip(center, default_cols):
        if 'starting_position' in sp:
            c_cols.append(sp['starting_position'][1])            # honour caller's real centre placement
        else:
            sp['starting_position'] = (start_row + APEX * advance_dir, dcol)  # apex forward (field-centre)
            c_cols.append(dcol)
    c_left = min(col + s[0] for col, s in zip(c_cols, c_spans))
    c_right = max(col + s[1] for col, s in zip(c_cols, c_spans))
    left_x = c_left - ENVELOP_WING_GAP    # right boundary of the left wing group (grows leftward)
    right_x = c_right + ENVELOP_WING_GAP  # left boundary of the right wing group (grows rightward)
    wings = []
    for i, sp0 in enumerate(wing_specs):
        sp = dict(sp0)
        sp.setdefault('stance', 'hold')
        cmin, cmax = _spec_span(sp)
        # [ED-MB-0025] Honour an EXPLICIT wing position if the caller gave one (explicit-placement
        # directive); only auto-compute the flank-split placement when none is supplied. Previously this
        # was an unconditional assignment that silently discarded a caller's `starting_position`.
        if 'starting_position' not in sp:
            if i % 2 == 0:  # left wing: place its RIGHT edge at left_x, then extend further left
                col = int(round(left_x - cmax))
                left_x = (col + cmin) - ENVELOP_WING_GAP
            else:           # right wing: place its LEFT edge at right_x, then extend further right
                col = int(round(right_x - cmin))
                right_x = (col + cmax) + ENVELOP_WING_GAP
            sp['starting_position'] = (start_row, col)  # wings at the flank base line, behind the apex
        wings.append(sp)
    specs = center + wings
    unit = build_army(specs, name, faction, power=power, command=command, discipline=discipline,
                       morale=morale, morale_start=morale_start, dr=dr, speed=speed)
    if not freeze_wings:
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
    mechanic. Same LC-8 retirement note as build_envelopment (see its docstring) applies here."""
    # [ED-MB-0017] OBLIQUE deployment (fixes P-3). Lay strong + refused across one centred frontage
    # (so no lateral overlap), then push the REFUSED subunits ECHELONED BACK by REFUSE_ECHELON rows —
    # out of contact range while the strong wing engages (Leuctra/Leuthen research §2/§4). Strong subunits
    # take the left of the line and lead at the front; refused take the right and trail rearward: the
    # diagonal "staircase" of an oblique order. Pre-fix, `build_refused_flank` never moved the refused
    # wing at all — it sat level with the strong wing AND overlapped it (P-3, "makes no sense").
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    strong = [dict(sp) for sp in strong_specs]
    refused = [dict(sp) for sp in refused_specs]
    n_strong = len(strong)
    all_specs = strong + refused
    cols = _centered_line_cols(all_specs, 25)  # field-centre anchor
    for i, sp in enumerate(all_specs):
        if i < n_strong:
            sp.setdefault('starting_position', (start_row, cols[i]))                       # strong: front line
        else:
            sp.setdefault('stance', 'hold')
            sp.setdefault('starting_position',
                          (start_row - REFUSE_ECHELON * advance_dir, cols[i]))             # refused: echeloned BACK
    specs = all_specs
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


_WRAPPER_API = {"build_unit", "build_army", "build_envelopment", "build_refused_flank", "resolve_battle", "SUBUNIT_CAP"}

_mods = (_cfg,_ce,_cs,_ca,_cc,_tt,_hu,_geo,_pc,_res,_orch)
__all__ = sorted({n for _m in _mods for n in getattr(_m,'__all__',[])} | {"MECHANICS","mechanics_selftest"} | _WRAPPER_API)
