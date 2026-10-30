"""modules.mass_battle.armies -- the faction -> ARMY adapter: constructs a MULTI-subunit `Unit` from a list of
per-subunit spec dicts (`build_army`), with the frontage-aware deployment geometry it needs.

Moved here, byte for byte, from `systems/mass_battle/sim/engine.py` (which re-imports every name below, so
`from systems.mass_battle.sim.engine import build_army` and the star re-export are unchanged). WHY IT MOVED:
`modules/mass_battle/` is the reachable closure and the canon tree (`references/module_contracts.yaml`, the
`mass_battle` row's note); a season-facing order-of-battle builder (`orderofbattle.py`) needs this constructor,
and a module may not import from `systems/` (the harness and workbench tree). Moving it leaves ONE owner.
The moved text was edited in ONE place: `build_army`'s spec tuple gained `'target_condition'` (a spec's targeting
preference was silently dropped before; no caller passed one). A diff against the old engine.py lines is otherwise
empty but for this docstring and the imports."""
from modules.mass_battle.config import *
from modules.mass_battle.core.exchange import *
from modules.mass_battle.core.state import *
from modules.mass_battle.core.attrition import *
from modules.mass_battle.core.contact import *
from modules.mass_battle.troop_types.registry import *
from modules.mass_battle.hierarchy.units import *
from modules.mass_battle.geometry import *
from modules.mass_battle.percell import *
from modules.mass_battle.resolution import *
from modules.mass_battle.orchestration import *

__all__ = ['SUBUNIT_CAP', 'DEPLOY_GAP', 'ENVELOP_WING_GAP', 'REFUSE_ECHELON', '_spec_span',
           '_centered_line_cols', 'build_army']

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
SUBUNIT_CAP = 11  # [canonical: mass_battle_v30.md §A.5 Command — videogame cap per ED-1090, superseding the TTRPG hard cap 3]

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
    w, d = sp.get('width'), sp.get('depth')                         # [ED-MB-0026] explicit frontage×depth
    _continuous = troops is not None and (conc is not None or (w is not None and d is not None))
    pat = footprint_for(shape, troops, conc, sp.get('troop_type'), width=w, depth=d) if _continuous \
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



def build_army(specs, name, faction, *, power=4, command=4, discipline=5, morale=6,  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults, same as build_unit]
               morale_start=None, dr=1, stance='balanced', speed='Standard', anchor_col=25,
               officers=()):
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
    TROOP_TYPE_ROLES/ROLE_SPEC — the role->shape/instructions menu this wires]

    officers: [A3, ED-MB-0067 Part A / ED-MB-0073] Default () — ZERO behavior change for every
    existing caller (every existing spec omits 'officer', so `direct == len(specs)` below and the
    SUBUNIT_CAP check is exactly what it always was). When given, a list of Officer specs (dicts,
    e.g. {'name': 'Aulus', 'command': 5}, or {'name':..., 'charisma':..., 'cognition':...} to derive
    Command the ED-899 way) or Officer instances. A subunit spec may then carry an 'officer': NAME
    key naming which officer commands it (omitted = a direct report to the general, same as today).
    This is ED-1090's own queued reconciliation: Command clamps 1..7, so fielding more than Command
    (up to the hard ceiling SUBUNIT_CAP=11) "implies a future Command-exceeding mechanism (e.g.
    subordinate officers/lieutenancy)" — verbatim, `registers/editorial_ledger.jsonl`'s ED-1090 row.
    A3's OWN text is precise about what changes and what does not: "the general's cap... counts the
    officers he commands rather than every sub-unit" — SUBUNIT_CAP itself is NOT dropped, only what
    it counts changes, from raw subunits to (officers actually used + un-officered direct subunits).
    C5 (Part C, ruled 2026-09-25) separately ladders each officer's OWN span, and the general's
    direct-reports count, against Command — "one ladder... at every echelon, including the new
    officer post."

    [FIX, adversarial-review round 1] The first version of this validation branched on `if not
    officer_objs` and skipped SUBUNIT_CAP entirely once ANY officer was supplied — even one no spec
    actually referenced. Combined with `command` never being clamped anywhere in this file (unlike
    `Officer`'s own clamp), that let a single unused dummy officer plus an unrealistically large
    `command` value bypass BOTH ceilings at once: an idle officer contributes to neither `counts` nor
    the general's Command check, so an arbitrary number of un-officered subunits passed. Fixed by
    computing `general_direct` (officers actually referenced + un-officered subunits) UNIFORMLY,
    always checking it against SUBUNIT_CAP (which is what lets it count officers instead of raw
    subunits, exactly as A3's text says, in BOTH the empty- and non-empty-officers case), and
    checking it against the general's own (now clamped) Command ONLY when officers are actually used
    — enforcing the Command ladder unconditionally would raise on existing single-tier armies built
    with more direct subunits than their Command (several already exist in this package's own
    tests/gauges), which is an existing-behavior change this item does not make."""
    # [ED-1090] SUBUNIT_CAP is module-level (see its definition above build_unit) so other callers
    # (Army Configuration Mode's UI) read the single source rather than duplicating the literal.
    # isinstance(o, Officer) would be the direct check, but several tests in this package reload
    # hierarchy.units (importlib.reload) to pick up an env-var-gated flag -- which rebinds Officer to
    # a NEW class object, so an instance built from the pre-reload class fails isinstance against the
    # post-reload one in the same worker process (found by adversarial review running the full suite,
    # not by this file's own tests, which stay single-module and never see the mismatch). Checking for
    # `dict` instead is reload-safe: dict's identity never changes, and everything this parameter
    # accepts is either a mapping (build one) or already Officer-shaped (pass through).
    officer_objs = tuple(Officer(**o) if isinstance(o, dict) else o for o in officers)
    # [A3, ED-MB-0067 Part A / ED-MB-0073] Eager, fail-loud validation, matching this file's own
    # existing SUBUNIT_CAP-raise convention rather than silently truncating or ignoring an
    # over-assigned officer. Runs UNCONDITIONALLY (not only when officers is non-empty, F6's fix): a
    # spec referencing an officer that does not exist is a caller mistake regardless of whether any
    # OTHER officer was supplied.
    by_name = {}
    for o in officer_objs:
        if o.name in by_name:
            raise ValueError(f"build_army: duplicate officer name {o.name!r}")
        by_name[o.name] = o
    counts = {}
    direct = 0
    for sp in specs:
        oname = sp.get('officer')
        if oname is None:
            direct += 1
            continue
        if oname not in by_name:
            raise ValueError(f"build_army: subunit officer {oname!r} is not in officers "
                              f"(known: {sorted(by_name)})")
        counts[oname] = counts.get(oname, 0) + 1
    for oname, n in counts.items():
        cap = by_name[oname].command
        if n > cap:
            raise ValueError(f"build_army: officer {oname!r} commands {n} subunits, exceeding "
                              f"their own Command {cap} (C5, ED-MB-0067 Part C: max commanded "
                              f"= Command at every echelon)")
    # general_direct == len(specs) whenever no spec sets 'officer' (every existing caller) --
    # byte-exact continuation of ED-1090's own flat check in that case.
    general_direct = len(counts) + direct
    if general_direct > SUBUNIT_CAP:
        raise ValueError(f"build_army: {general_direct} direct reports "
                          f"({len(counts)} officers + {direct} un-officered subunits) exceeds the "
                          f"videogame cap of {SUBUNIT_CAP} (ED-1090; mass_battle_v30.md §A.5)")
    if officer_objs:
        clamped_command = clamp_command(command)
        if general_direct > clamped_command:
            raise ValueError(f"build_army: general commands {general_direct} direct reports "
                              f"({len(counts)} officers + {direct} un-officered subunits), exceeding "
                              f"their own Command {clamped_command} (C5, ED-MB-0067 Part C: max "
                              f"commanded = Command at every echelon)")
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
                  _stance_explicit='stance' in sp,   # [MB-04] evaluated before the pop on the next line
                  stance=sp.pop('stance', stance),
                  instructions=tuple(instructions), advance_dir=advance_dir, role=role)
        for k in ('power', 'discipline', 'morale', 'morale_start', 'dr', 'stamina', 'stamina_max',
                  'volleys',  # [A6, ED-MB-0067 Part A -- F4] was missing from this tuple entirely,
                  # so an explicit per-spec override silently vanished (sp.pop never ran, kw never
                  # got the key) -- see this loop's own note below for the seed-when-absent half.
                  'troops', 'concentration', 'orders',
                  'target_condition',  # [ED-IN-0304] was missing from this tuple, so a spec's targeting preference silently vanished (the 'volleys' omission above, again); a Subunit field since class-B targeting
                  'width', 'depth', 'distribution',  # [ED-MB-0025/0026] explicit grid + density gradient
                  'officer'):  # [A3, ED-MB-0067 Part A / ED-MB-0073] already validated above this loop;
                  # forwarded the same generic way as every other per-subunit override in this tuple.
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
        # [A6, ED-MB-0067 Part A -- adversarial-pass round 2, F4] `volleys` was missing from the
        # per-subunit forwarding tuple above entirely -- not merely unseeded like morale used to be,
        # NEVER forwarded at all, so every ranged subunit built here fell through to
        # Subunit.volleys=None -> eff_volleys inherits the ONE shared parent Unit pool. With 2+
        # subunits on that Unit (this constructor's whole point), between_turn_recovery's per-
        # subunit resupply_volleys call still runs for every OTHER subunit too (melee siblings
        # included -- it is not gated on unit_type), so a shared pool is resupplied once per
        # sibling per turn instead of once, and a ranged subunit's own drain is likewise not
        # isolated from what its siblings do to that same pool -- the exact column-block-style
        # sharing bug this file's own ledger-move note already fixed once, relocated one level up
        # from "per-column" to "per-Unit". Same fix shape as the morale defaulting immediately
        # above (DG-4), scoped to unit_type=='ranged' -- the exact gate volley_phase.fire() itself
        # checks before ever reading eff_volleys -- rather than every subunit: a melee subunit's
        # ammo count is never read for combat, so seeding it would be harmless but meaningless
        # bookkeeping; what matters is that the SHOOTER's own pool is isolated.
        if kw.get('volleys') is None and kw['unit_type'] == 'ranged':
            kw['volleys'] = MB_VOLLEYS_START
        subs.append(Subunit.of_type(tt, shape, tier, pos, **kw))
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=subs, dr=dr, stance=stance, speed=speed, officers=officer_objs)


