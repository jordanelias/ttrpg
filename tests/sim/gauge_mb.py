"""Mass Battle GAUGE v2 -- historically RECALIBRATED battery (bottom-up grounding).

Validates the current engine against win-rate bands derived bottom-up from historical
precedent and peer-reviewed academic military analysis -- NOT fitted to engine output.
The engine is validated AGAINST these bands; where it falls outside, the gauge flags the
divergence rather than lowering the band. The full grounding -- the metric change, the
source citations (with DOIs), the per-band rationale, and the validation report -- lives
in the companion reference:

    references/historical/mass_battle_gauge_grounding.md

Metric: the win-rate band is on the DECISIVE SPLIT  decA = A_wins / (A_wins + B_wins) --
"who wins WHEN a result is reached." The previous raw win-rate metric conflated the
win-split with the draw rate, so a symmetric mirror failed its band purely on draws. The
draw rate is therefore validated SEPARATELY (draw_exp), since near-parity forces produce
high draw rates by the quantitative combat-modelling literature (see grounding doc): even
matchups allow high draws; gross-asymmetry matchups (envelopment, cavalry vs braced or
shaken foot) are expected to resolve.

Two granularities: single (one engagement-turn) and multi (the resolving mode). Single
mode currently returns all-draws at the tick cap for every engine config -- a tick-cap
artifact, not a calibration issue -- so bands are evaluated in multi mode. The engine is
the live mass_battle package (tests/sim/mass_battle/engine.py), imported directly -- this
gauge runs against whatever engine config the environment toggles (PER_CELL, FIELD_MOVEMENT,
MB_NODE_COHESION, ...) select, not a frozen snapshot file.

Grounding + citations index: references/historical/mass_battle_gauge_grounding.md
"""
import sys, os, statistics

# import the package exactly as bat.py (the G5 digest harness) does
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # tests/sim on path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # [B19.01] the repo root, so `python tests/sim/gauge_mb.py` finds `systems`, `modules`, `engine` without a caller's PYTHONPATH
if __name__ == '__main__':   # [B17.12] a run from the command line builds the engine from the toggles its caller exported
    from systems.mass_battle.sim import variant
    variant.install(variant.cfg_from_environ(os.environ))
from systems.mass_battle.sim.engine import (  # noqa: E402
    Unit, Army, SIDE_A_START_ROW, SIDE_B_START_ROW,
    run_battle, run_multi_turn_battle, build_unit, build_army, build_envelopment, build_refused_flank,
    resolve_battle, _centered_line_cols)
from modules.mass_battle.config import TROOPS_PER_TIER, MB_VOLLEYS_START  # noqa: E402
from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import rngsource  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# [ED-MB-0027] HONEST-GAUGE density-matching constants (fiat register §1 measurement integrity).
# The gauge's confirmed #1 distortion (M1) was a per-cell DENSITY MISMATCH between the two deployment
# paths: single-subunit opponents built via the legacy tier footprint (make_unit → build_unit → ~16
# troops/cell for a tier-3 Line spread over ~25 cells) while the composed Envelopment/Refused presets
# set an explicit concentration=100 (~133/cell after the pin_frac split). Since density enters
# `_lanchester_strength` LINEARLY, that 8× gap — not the flanking geometry — drove H3/H4/C4 to a hard
# 100% (null test: dense-vs-thin, ZERO envelopment, already reproduces 100%; adversarial review 2026-
# 07-23). A ruler that varies density cannot measure geometry. FIX: hold per-cell density CONSTANT at
# GAUGE_CONC across EVERY unit — single and composed alike — by building all units from the SAME
# explicit troops/concentration path (footprint_for), and by choosing GAUGE_TROOPS so every historical
# split (pin_frac 1/3 & 2/3, strong_frac 1/2) divides evenly by GAUGE_CONC → integer-cell quantization
# is EXACT (no density overshoot). 600 @ 100/cell: single Line = 6 cells; 1/3-split = 200 → 2 cells;
# 2/3-split = 400 → 4 cells; wings 200/100 → 2/1 cells; 1/2-split = 300 → 3 cells — ALL exactly
# 100/cell. Now the only thing that varies across rows is frontage + geometry + posture — the ruler is
# fair, and any residual envelopment edge (or deficit) is the MECHANIC, not the density artifact.
# North star (fiat register §8): calibrate to independent history (Dupuy DLEDB, Sabin), NOT to these
# rows — the gauge stays a validation surface, never a training target.
GAUGE_TROOPS = 600.0   # [canonical: audit/2026-07-22-mass-battle-stress-test/honest_gauge_readout.md §"What changed" — per-unit total chosen so every historical split (pin 1/3, 2/3; strong 1/2) divides evenly by GAUGE_CONC → exact integer-cell quantization; harness calibration, not a mechanical constant]
GAUGE_CONC = 100.0     # per-cell troop density held constant across ALL gauge units (mid CELL_FLOOR..CELL_CAP band)

ANCHOR_MAP = {  # [canonical: mass_battle_v30.md §deployment — anchor columns]
    # [LC-8, ED-909, Jordan-approved 2026-07-02] Horseshoe/RefusedFlank entries retired along with
    # the shapes themselves -- _envelop_army/_refused_army below reference ('Line', tier) instead,
    # since those Army-level presets are now built from Line-shaped center/wing/refused units.
    ('Line',1):11,('Line',2):10,('Line',3):9,('Line',4):8,                       # [canonical: mass_battle_v30.md §deployment]
    ('Arrowhead',1):11,('Arrowhead',2):10,('Arrowhead',3):8,('Arrowhead',4):7,   # [canonical: mass_battle_v30.md §deployment]
    ('GappedLine',1):11,('GappedLine',2):9,('GappedLine',3):7,                   # [canonical: mass_battle_v30.md §deployment]
}

def make_mixed_unit(specs, name, faction, power=4, command=4, discipline=5, morale=6,  # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats P4/C4/D5/M6, same baseline as make_unit's defaults below]
                    morale_start=None, dr=1, stance='balanced', speed='Standard'):
    """Build a MULTI-subunit Army with per-subunit stats (Jordan directive: different unit
    types / troop counts per subunit). `specs` = list of dicts; each may set shape, tier, troop_type,
    unit_type, stance, instructions, starting_position, and per-subunit power/discipline/morale/morale_start/dr.
    Each subunit is built via Unit.of_type, so a CANONICAL troop type (TROOP_TYPE_STATS:
    levy, light_infantry, heavy_infantry, cavalry, archers, crossbow, sling, artillery, knights_templar)
    draws its §B.2 Power/Discipline/Morale presets unless the spec overrides them. A non-canonical
    type (e.g. 'infantry') or an explicit override behaves exactly as before -> inherits the unit-level
    fallbacks below, so a spec list of non-canonical types with no overrides still reproduces a homogeneous
    unit. make_unit (single-subunit) is unchanged.
    [canonical: derived_stats architecture -- unit stats composed from units]"""
    # [ED-MB-0017, adversarial-review finding 2] Frontage-aware centred line for un-positioned units
    # (was `(10 + i*4, 15)` — same row-stagger-at-fixed-col defect that stacked units, the P-1 bug the
    # engine builders fixed). No live gauge row hits this branch (every multi-subunit gauge row below sets
    # explicit `starting_position`), so this closes the latent default without changing any gauge result.
    _start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    _auto_cols = _centered_line_cols(specs, 25)
    subs = []
    for i, sp in enumerate(specs):
        sp = dict(sp)
        pos = sp.pop('starting_position', (_start_row, _auto_cols[i]))
        tt = sp.pop('troop_type', 'infantry')
        # build typed units via Unit.of_type so a canonical troop type draws its
        # §B.2 Power/Discipline/Morale presets (the taxonomy stat home, ED-1018). Only forward the
        # stat keys the caller explicitly set, so of_type's setdefault fills the rest from the preset;
        # a non-canonical type ('infantry') fills nothing and inherits the unit-level fallbacks exactly
        # as before. A caller-set stat still overrides the preset.
        kw = dict(unit_type=sp.pop('unit_type', 'melee'), stance=sp.pop('stance', stance),
                  instructions=sp.pop('instructions', ()))
        for k in ('power', 'discipline', 'morale', 'morale_start', 'dr', 'volleys'):
            if k in sp:
                kw[k] = sp.pop(k)
        # [A6, ED-MB-0067 Part A -- adversarial-pass round 2, F4] Same cross-subunit ammo-pool gap
        # engine.build_army had (see its own note): an unseeded ranged subunit's volleys (None)
        # inherits the ONE shared parent Army pool, which every OTHER subunit's between_turn_recovery
        # resupply call also writes to. Give a ranged subunit its own explicit pool unless the spec
        # already set one; a melee subunit's ammo count is never read for combat (volley_phase.fire's
        # own unit_type=='ranged' gate), so it is left inheriting as before. This does NOT backport
        # build_army's separate DG-4 morale-seeding fix (this function still leaves per-subunit
        # morale unseeded unless a spec sets it explicitly) -- that is a pre-existing gap unrelated
        # to A6, out of scope here.
        if kw.get('volleys') is None and kw['unit_type'] == 'ranged':
            kw['volleys'] = MB_VOLLEYS_START
        subs.append(Unit.of_type(tt, sp.pop('shape'), sp.pop('tier', 3), pos, **kw))
    return Army(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                units=subs, dr=dr, stance=stance, speed=speed)


def make_unit(shape, tier, name, faction, unit_type='melee', power=4, command=4,   # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats P4/C4]
              discipline=5, morale=6, stance='balanced',                          # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats D5/M6]
              troop_type='infantry', speed='Standard', morale_start=None, instructions=(),
              troops=None, concentration=None, width=None, depth=None):  # [ED-MB-0027] explicit density; [ED-MB-0034] width/depth for deep-formation rows (braced pike-block/schiltron: brace-recoil is depth-gated)
    # troop_type/speed default to the historical infantry baseline so the original
    # 13 tests construct byte-identically; cavalry rows pass troop_type='cavalry',
    # speed='Fast' by kwargs. Cavalry charge mechanics (charge_pen,
    # MB_CAVALRY_SPEED_MULT) are PER_CELL=1-gated in the engine; under PER_CELL=0
    # cavalry == infantry (S1: speed is not yet wired into combat).
    #
    # morale_start / instructions default to leave EVERY pre-existing row byte-exact
    # (morale_start=None -> morale_start==morale; instructions=() -> no brace).
    #   * instructions=('brace',) sets the engine's FM brace tactic on the subunit:
    #     _unit_braced(unit) then fires the grounded reciprocal charge-recoil
    #     (MB_CHARGE_RECOIL, calibrated vs Courtrai/Swiss/Waterloo) so a frontal
    #     charge into a prepared wall is REPELLED. Bracing is a deliberate tactic,
    #     NOT an automatic consequence of holding -> the gauge must set it to test
    #     a braced unit (the engine gating is correct game design).
    #   * morale_start>morale expresses a genuinely SHAKEN unit (cohesion eroded
    #     BELOW its start, du Picq): _charge_shock_sigma's shaken-amplifier
    #     (MB_SHOCK_SHAKEN_GAIN) and _morale_sigma then fire. "Shaken" is RELATIVE
    #     (a unit that has LOST morale), not a low absolute ceiling -> a shaken line
    #     needs morale<morale_start, which make_unit's old morale_start==morale
    #     could not express.
    # [ED-MB-0027, honest-gauge density-matching] Route the single-subunit gauge unit through the SAME
    # explicit troops/concentration path (build_army → footprint_for) the composed Envelopment/Refused
    # presets use, so per-cell density is IDENTICAL (GAUGE_CONC) on both sides of every matchup. Was
    # `build_unit(...)`, whose legacy tier footprint gave a tier-3 Line ~16 troops/cell (~25 cells) vs
    # the presets' ~100–133/cell — the M1 density artifact that drove H3/H4/C4 to a fiat 100%. `troops`/
    # `concentration` (default GAUGE_TROOPS/GAUGE_CONC, overridable for bespoke rows) build a single
    # spec placed at THIS gauge's ANCHOR_MAP column. Every make_unit kwarg (unit_type/stance/
    # instructions/discipline/morale/morale_start/speed/power/command/dr) forwards through build_army's
    # spec + unit-level params exactly as before, so R1/R3 ranged, C2/C6 brace+d8, and C5 shaken rows
    # keep their posture; only the DENSITY is now matched. build_unit remains the public single-subunit
    # constructor (bat.py's byte-exact digest path is unaffected — it does not import this gauge).
    anchor_col = ANCHOR_MAP.get((shape, tier), 10)
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    _troops = GAUGE_TROOPS if troops is None else troops
    _conc = GAUGE_CONC if concentration is None else concentration
    # [Fable-audit A1 fix, 2026-07-24] Forward power/discipline INTO the spec dict. Without them,
    # build_army -> Unit.of_type fills the canonical §B.2 troop-type PRESET (cavalry Power 5), silently
    # changing the gauge's cavalry from the documented uniform baseline P4 to P5 when make_unit was routed
    # through build_army for the ED-MB-0027 density match — an unintended stat change that inverted the
    # C-battery verdicts. Explicit spec keys beat of_type's setdefault (engine.py), so this restores P4
    # and is a NO-OP for the infantry rows (which carry no preset). To adopt §B.2 stats as the gauge
    # baseline instead, this is the one place to change it — deliberately, with the C-bands rebaselined.
    spec = {'shape': shape, 'tier': tier, 'troop_type': troop_type, 'unit_type': unit_type,
            'stance': stance, 'instructions': tuple(instructions),
            'power': power, 'discipline': discipline,
            'troops': _troops, 'concentration': _conc,
            'starting_position': (start_row, anchor_col)}
    if width is not None:  spec['width'] = width    # [ED-MB-0034] explicit frontage×depth grid (footprint_for)
    if depth is not None:  spec['depth'] = depth    # deep braced formations need real depth for the depth-gated recoil
    return build_army([spec], name, faction, power=power, command=command,
                       discipline=discipline, morale=morale, morale_start=morale_start,
                       dr=1, stance=stance, speed=speed)


def _command_army(shape, tier=3, n_cmd=3):  # [canonical: sim_mb_06_v9_historical_spec.md — T3 tier] [CALIBRATED-DEBT: n_cmd=3 — no independent anchor; the triplex acies is three lines in DEPTH, not a lateral split (ED-MB-0045 item 2)]
    """[ED-MB-0038] MATCHED COMMAND-GRANULARITY builder — a shape deployed as `n_cmd` side-by-side
    commands (left wing / centre / right wing; n_cmd=3 is CALIBRATED-DEBT, not a historical anchor —
    see the tag at the end) at constant density (GAUGE_CONC), summing to GAUGE_TROOPS. Returns a
    matchup-callable (name, faction, **kw) so it drops into a TESTS row exactly where a shape-STRING
    would, but yields a MULTI-BODY unit instead of one monolith.

    Motivation (honest-gauge measurement integrity, the granularity analog of ED-MB-0027's density
    match). The composed enveloper/refused presets (`_envelop_army`, 3 bodies: centre + 2 wings;
    `_refused_army`, 2) always faced a SINGLE-subunit opponent built by `make_unit`. A monolithic
    subunit is nearly UNBREAKABLE by envelopment: the flank/rear octagon multiplier + multi-side shock
    land on its cells, but the casualties DILUTE across its whole HP pool (distribute_casualties) and no
    section can rout independently, so the per-subunit rout cascade (ED-1019 — a section of the line
    breaks while a fresh sibling holds) has nothing to bite. Direct measurement (2026-07-24, audit
    2026-07-22-mass-battle-stress-test/granularity_probe.py): H3 envelop vs a monolithic Line = 0%
    decisive-for-A; vs a 3-command Line ~53%; vs 6-command ~95% — granularity is a FIRST-ORDER
    determinant that the single-subunit opponent was silently pinning to 0. A ruler whose defender
    cannot fracture cannot measure envelopment. FIX: match the composed side's command-granularity —
    the enveloper is 3 bodies, so its opponent is 3 commands, and the only thing that varies across the
    matchup is geometry/posture (exactly ED-MB-0027's density-constant argument, one axis up).
    [canonical: honest-gauge granularity match — audit/2026-07-22-mass-battle-stress-test/honest_gauge_readout.md]
    [CALIBRATED-DEBT: n_cmd=3 — the Roman triplex acies (Polybius VI) names three lines in DEPTH, not a lateral three-way division, so it anchors no granularity here (ED-MB-0045 item 2).]"""
    anchor = ANCHOR_MAP.get((shape, tier), 10)

    def _build(name, faction, unit_type='melee', power=4, command=4, discipline=5, morale=6,  # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 baseline P4/C4/D5/M6, same defaults as make_unit]
               stance='balanced', troop_type='infantry', speed='Standard', morale_start=None,
               instructions=(), troops=None, concentration=None):
        start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
        total = GAUGE_TROOPS if troops is None else troops
        conc = GAUGE_CONC if concentration is None else concentration
        per = total / n_cmd
        cells_per = per / conc                        # frontage (cols) of one command
        c0 = anchor - (n_cmd * cells_per) / 2.0        # centre the whole line on the shape's anchor
        specs = [{'shape': shape, 'tier': tier, 'troop_type': troop_type, 'unit_type': unit_type,
                  'stance': stance, 'instructions': tuple(instructions),
                  'power': power, 'discipline': discipline,
                  'troops': per, 'concentration': conc,
                  'starting_position': (start_row, int(round(c0 + (k + 0.5) * cells_per)))}
                 for k in range(n_cmd)]
        return build_army(specs, name, faction, power=power, command=command,
                          discipline=discipline, morale=morale, morale_start=morale_start,
                          dr=1, stance=stance, speed=speed)
    return _build


def _envelop_army(name, faction, tier=3, troop_type='infantry', speed='Standard', **kw):  # [canonical: sim_mb_06_v9_historical_spec.md — T3 (tier-3) baseline]
    """[LC-8, ED-909] Composed replacement for the retired Horseshoe shape: a held center + two
    wide-placed wings released into 'envelop' via a Stage C timed order -- ED-909's Army-level
    Envelopment preset. Mirrors make_unit's kwarg surface closely enough to drop straight into
    matchup()'s (sa,tier,name,faction,**k) call convention.

    [2026-07-05 fix, mass-battle Cannae gauge follow-up audit, Jordan-ratified DG-1] Two corrections,
    both empirically confirmed necessary (a Fable-5 adversarial audit + direct gauge measurement):

    1. FORCE PARITY (the load-bearing part). Previously every subunit here independently drew a full
       tier's troops (TROOPS_PER_TIER[tier] each via the legacy tier-keyed CELL_PATTERN_FN path), so a
       3-subunit envelopment army silently fielded 3x its single-subunit opponent's troops -- a side
       effect of the LC-8 migration from a single-subunit Horseshoe shape, never itself historically
       ratified (the grounding doc's own bands assume "comparable forces"). `total_troops` (default
       TROOPS_PER_TIER[tier], matching every other row's single-subunit baseline) is now the SAME total
       split across center+wings via the continuous-scale troops/concentration path (footprint_for),
       not the legacy tier path -- so this preset fields the same total strength as its opponent.
    2. COMPOSITION (Jordan-ratified, "symmetric at parity + majority pin cavalry wing so long as
       bottom-up emergent primitives approach"). `pin_frac` (default 1/3, symmetric-thirds) sets the
       center's share of `total_troops`; the two wings split the remainder evenly. The infantry rows
       (H3/H5/H6) keep this symmetric default. The cavalry rows (C4/C7) pass `pin_frac=2/3` +
       `wing_troop_type='cavalry'` (see CAV_TESTS below) -- a majority INFANTRY pin with a minority
       CAVALRY envelopment wing, matching the Polybius/Livy order of battle for Cannae-pattern
       double-envelopments, built entirely from the existing build_army/build_envelopment primitives
       (no new mechanic -- an army-composition choice fed into an already-verified constructor)."""
    anchor = ANCHOR_MAP.get(('Line', tier), 10)
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    total_troops = kw.pop('total_troops', GAUGE_TROOPS)  # [ED-MB-0027] honest-gauge total (divisible by GAUGE_CONC under 1/3 & 2/3 splits) — was TROOPS_PER_TIER[tier]=400 (133/cell after split, the M1 density artifact)
    pin_frac = kw.pop('pin_frac', 1.0 / 3)
    wing_troop_type = kw.pop('wing_troop_type', troop_type)
    wing_speed = kw.pop('wing_speed', speed)
    conc = kw.pop('concentration', GAUGE_CONC)  # [ED-MB-0027] density held at GAUGE_CONC to match make_unit; [canonical: config.py CELL_FLOOR=40/CELL_CAP=200 band]
    center_troops = total_troops * pin_frac
    wing_troops = (total_troops - center_troops) / 2
    # [2026-07-05 adversarial-review fix] `Unit` has NO `speed` field at all -- a per-subunit
    # 'speed' key in these spec dicts is silently dropped by `build_army` (it never pops one), so it
    # was pure dead decoration. `Army.speed` is the only real speed knob (checked whole-unit at
    # post-rout pursuit, orchestration.py `routing_unit.speed == "Fast"`/`victor.speed == "Fast"`) --
    # forwarded below via `build_envelopment(..., speed=wing_speed)` instead. For the infantry rows
    # (H3/H5/H6) `wing_speed` defaults to `speed` ('Standard'), so this is a no-op there; for C4/C7's
    # cavalry-wing composition it correctly marks the WHOLE composed army (which contains the fast
    # pursuing wing) as Fast for pursuit purposes -- the coarsest expression the engine's current
    # unit-level (not per-subunit) speed model allows.
    center = [{'shape': 'Line', 'troop_type': troop_type,
               'troops': center_troops, 'concentration': conc,
               'starting_position': (start_row, anchor)}]
    # wing offset: [canonical: sim_verification_ledger.json — CALIBRATED, matches bat.py's _envelop_army spacing, not historically cited]
    wings = [{'shape': 'Line', 'troop_type': wing_troop_type,
              'troops': wing_troops, 'concentration': conc,
              'starting_position': (start_row, anchor - 6)},  # [canonical: sim_verification_ledger.json — CALIBRATED, not historically cited]
             {'shape': 'Line', 'troop_type': wing_troop_type,
              'troops': wing_troops, 'concentration': conc,
              'starting_position': (start_row, anchor + 6)}]  # [canonical: sim_verification_ledger.json — CALIBRATED, not historically cited]
    return build_envelopment(center, wings, name, faction,
                              power=kw.pop('power', 4), command=kw.pop('command', 4),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                              discipline=kw.pop('discipline', 5), morale=kw.pop('morale', 6),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                              morale_start=kw.pop('morale_start', None), speed=wing_speed,
                              freeze_wings=kw.pop('freeze_wings', False))  # [ED-MB-0002 §2 step 4, measurement only]


def _refused_army(name, faction, tier=3, troop_type='infantry', speed='Standard', **kw):  # [canonical: sim_mb_06_v9_historical_spec.md — T3 (tier-3) baseline]
    """[LC-8, ED-909] Composed replacement for the retired RefusedFlank shape: a strong wing +
    a withheld/refused wing released only once directly threatened -- ED-909's Army-level Refused
    Flank preset.

    [2026-07-05 fix, same force-parity rationale as _envelop_army above] `total_troops` (default
    TROOPS_PER_TIER[tier]) is split across strong+refused via the continuous-scale troops/
    concentration path instead of each subunit independently drawing a full tier's troops (a 2x
    dilution vs a single-subunit opponent) -- matches every other row's single-subunit baseline, and
    matches _envelop_army's own total when the two face off (H5)."""
    anchor = ANCHOR_MAP.get(('Line', tier), 10)
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    total_troops = kw.pop('total_troops', GAUGE_TROOPS)  # [ED-MB-0027] honest-gauge total (600, 1/2-split → 300 → 3 cells @100); was TROOPS_PER_TIER[tier]=400
    strong_frac = kw.pop('strong_frac', 0.5)
    conc = kw.pop('concentration', GAUGE_CONC)  # [ED-MB-0027] density held at GAUGE_CONC to match make_unit; [canonical: config.py CELL_FLOOR=40/CELL_CAP=200]
    strong_troops = total_troops * strong_frac
    refused_troops = total_troops - strong_troops
    # [2026-07-05 adversarial-review fix, same rationale as _envelop_army above] per-subunit 'speed'
    # keys are dead (Unit has no speed field); the real Army.speed is forwarded below instead.
    strong = [{'shape': 'Line', 'troop_type': troop_type,
               'troops': strong_troops, 'concentration': conc,
               'starting_position': (start_row, anchor - 4)}]
    refused = [{'shape': 'Line', 'troop_type': troop_type,
                'troops': refused_troops, 'concentration': conc,
                'starting_position': (start_row, anchor + 4)}]
    return build_refused_flank(strong, refused, name, faction,
                                power=kw.pop('power', 4), command=kw.pop('command', 4),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                                discipline=kw.pop('discipline', 5), morale=kw.pop('morale', 6),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                                morale_start=kw.pop('morale_start', None), speed=speed)


# (id, label, shape_a, shape_b, ka, kb, lo, hi, draw_exp[, metric])
#   (lo,hi)  = band, % [history-grounded]. metric (optional, default 'decA') selects what (lo,hi) bounds:
#     'decA' = DECISIVE-split decA = A_wins/(A_wins+B_wins); draw_exp constrains the draw rate.
#     'rawA' = RAW A win-rate (braced-REPEL rows): the wall repels, so cavalry (A) must be LOW; a
#              repulse is a HOLD (decisive n tiny -> decA uninformative) and high draws are EXPECTED.
#   draw_exp = 'high' (even matchup / repel hold, high draws OK) | 'low' (decisive, expect draw<30%)
# Bands are set by HISTORY. Where the engine falls outside a band, the test FAILS BY DESIGN
# (the gauge flags engine divergence; the band is NOT lowered to make the engine pass).
# Every band cites references/historical/mass_battle_gauge_grounding.md §3 (per-band rationale).
TESTS = [
    ('H1','Line vs Line (mirror)','Line','Line',{},{},42,58,'high'),                       # [canonical: mass_battle_gauge_grounding.md §3 — H1 mirror symmetry]
    ('H2','Arrowhead(wedge) vs Line','Arrowhead','Line',{},{},48,62,'high'),               # [canonical: mass_battle_gauge_grounding.md §3 — H2 modest wedge edge]
    # [ED-MB-0038] MATCHED COMMAND-GRANULARITY: the composed enveloper/refused presets face a 3-command
    # (tripartite) opponent, not a single monolith — a monolithic subunit is unbreakable by envelopment
    # (casualties dilute across one HP pool; the ED-1019 per-subunit rout cascade has nothing to bite),
    # pinning H3/H4/H6 to 0% regardless of geometry. See _command_army for the granularity-match rationale.
    ('H3','Envelopment vs Line',_envelop_army,_command_army('Line'),{},{},55,72,'high'),             # [canonical: mass_battle_gauge_grounding.md §3 — H3 full envelopment]
    ('H4','Envelopment vs Arrowhead (Cannae)',_envelop_army,_command_army('Arrowhead'),{},{},45,62,'high'),   # [canonical: mass_battle_gauge_grounding.md §3 — H4 Cannae proper]
    ('H5','RefusedFlank vs Envelopment',_refused_army,_envelop_army,{},{},48,62,'high'),       # [canonical: mass_battle_gauge_grounding.md §3 — H5 oblique counter]
    ('H6','RefusedFlank vs Line',_refused_army,_command_army('Line'),{},{},48,60,'high'),                 # [canonical: mass_battle_gauge_grounding.md §3 — H6 oblique order]
    ('H7','GappedLine(manip) vs Line','GappedLine','Line',{},{},48,62,'high'),              # [canonical: mass_battle_gauge_grounding.md §3 — H7 manipular flex]
    ('H8','GappedLine vs Arrowhead','GappedLine','Arrowhead',{},{},50,65,'high'),           # [canonical: mass_battle_gauge_grounding.md §3 — H8 maniples absorb wedge]
    ('H9','Line vs Arrowhead (rev H2)','Line','Arrowhead',{},{},38,52,'high'),              # [canonical: mass_battle_gauge_grounding.md §3 — H9 inverse H2]
    ('H10','Line vs Envelopment (rev H3)',_command_army('Line'),_envelop_army,{},{},28,45,'high'),             # [canonical: mass_battle_gauge_grounding.md §3 — H10 inverse H3; ED-MB-0038 matched granularity]
    ('H11','Arrowhead vs Envelopment (rev H4)',_command_army('Arrowhead'),_envelop_army,{},{},38,55,'high'),   # [canonical: mass_battle_gauge_grounding.md §3 — H11 symmetric H4; ED-MB-0038 matched granularity]
    ('R1','Ranged vs Line (open field)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{},0,30,'low'),                             # [canonical: mass_battle_gauge_grounding.md §3 — R1 ranged loses open field]
    # [ED-MB-0044 superseding row, 2026-09-15] Was both sides {'stance':'hold'} — 'hold' is an
    # UNCONDITIONAL early-return from steering on both paths (hierarchy/units.py's _node_advance and
    # advance_cells), so with tier-3 Lines spawning 15 cells apart (outside VOLLEY_MAX_RANGE=8) and
    # neither side ever moving, the row was a structural 100%-draw/0%-casualty test-fixture defect,
    # not a balance finding. Fixed per the row's own recommended, lower-blast-radius alternative
    # (changing the SCENARIO, not the engine's hold semantics, which stays load-bearing for
    # build_envelopment's freeze_wings and build_refused_flank's refused wing): 'balanced' stance +
    # the 'kite' instruction lets the band-seeking primitive _kite_goal close to volley range and
    # hold it. Falsifier verified before this edit (matching the row's own falsifier): the OLD
    # kwargs reproduce 100% draw / 0.0% casualties both sides at n=60 multi mode; the NEW kwargs
    # give decA=47.2 (band 42-58, PASS) with 11.7% draws (well under the 30% low-draw threshold,
    # not that this row needs it — draw_exp is 'high').
    ('R3','Ranged vs Ranged (mirror)','Line','Line',
        {'unit_type':'ranged','stance':'balanced','instructions':('kite',)},
        {'unit_type':'ranged','stance':'balanced','instructions':('kite',)},42,58,'high'),  # [canonical: mass_battle_gauge_grounding.md §3 — R3 ranged mirror]
]

CAV = {'troop_type':'cavalry','speed':'Fast'}
CAV_TESTS = [
    # C1: frontal shock cavalry vs STEADY close-order but UNBRACED foot, open ground. CONTESTED,
    # NOT a cavalry win -- a horse will not charge a solid formation, and cavalry's decisive work
    # was against BROKEN or FLANKED foot (Burkholder 2007). [REBASELINE: the old band encoded the
    # popular cavalry-beats-unprepared-infantry misconception this source debunks.]
    ('C1','Cav vs steady unbraced Line','Arrowhead','Line',dict(CAV),{},35,55,'high'),     # [canonical: mass_battle_gauge_grounding.md §3 — C1 contested frontal, rebaseline]
    # C2: frontal cavalry vs a BRACED wall (hold + disc8 + the 'brace' tactic = square / schiltron /
    # pike block). The brace instruction fires the grounded reciprocal charge-recoil (MB_CHARGE_RECOIL,
    # calibrated vs Courtrai/Swiss/Waterloo): the wall REPELS the charge -- cavalry rarely breaks it.
    # Judged on RAW cavalry win-rate (must be LOW): a repelled charge is a HOLD, not a decisive result,
    # so decisive-split is uninformative here (tiny decisive n) and high draws are EXPECTED (Waterloo
    # squares held all day; cavalry could not charge a solid formation -- Burkholder 2007; Barua 2011).
    # [ED-MB-0041] C2 now builds a genuinely DEEP braced block (width 3 x depth 6) — a pike block /
    # schiltron / square, which is what the band's Courtrai/Swiss/Waterloo grounding describes. It
    # previously passed no width/depth, so it built the default 3x2 and was BIT-IDENTICAL to C6.
    ('C2','Cav vs BRACED deep block (hold+d8+brace)','Arrowhead','Line',dict(CAV),
        {'stance':'hold','discipline':8,'instructions':('brace',),'width':3,'depth':6,'troop_type':'pike'},0,30,'high','rawA'),  # [canonical: mass_battle_gauge_grounding.md §3 — C2 braced repels; raw cav-a LOW]
    # C3: cavalry mirror -- side-symmetry control of the charge/momentum path. Even.
    ('C3','Cav vs Cav (mirror control)','Arrowhead','Arrowhead',dict(CAV),dict(CAV),42,58,'high'),  # [canonical: mass_battle_gauge_grounding.md §3 — C3 cav mirror]
    # C4: mounted ENVELOPMENT of a line -- flank/rear is devastating (Cannae; Adrianople; Boddy 2015).
    # [2026-07-05 fix, DG-1 ratified: "majority pin cavalry wing"] Was dict(CAV) applied uniformly
    # (the WHOLE _envelop_army fielded as cavalry) -- now a majority (2/3) INFANTRY pin with a
    # minority (1/3, split across both wings) CAVALRY envelopment wing, matching the Polybius/Livy
    # order of battle this row is named for, at force parity with the single-subunit Line defender.
    ('C4','Cav flank/envelopment vs Line',_envelop_army,'Line',
        {'pin_frac':2/3,'wing_troop_type':'cavalry','wing_speed':'Fast'},{},75,95,'low'),    # [canonical: mass_battle_gauge_grounding.md §3 — C4 mounted envelopment]
    # C5: cavalry vs a genuinely SHAKEN line -- morale 2 of a start-6 unit (cohesion eroded 2/3 BELOW
    # start; "shaken" is RELATIVE, du Picq, not a low absolute ceiling). The shaken-amplifier
    # (MB_SHOCK_SHAKEN_GAIN) + _morale_sigma fire: the wavering line breaks under the charge --
    # exploitation + pursuit. Decisive cavalry win; ceiling is NEAR-TOTAL rout: cavalry vs disordered
    # foot was catastrophic (Boddy 2015 dispersed 15,000 disordered French; Hastings post-feint). The
    # Phase-2 ceiling 90 was provisional (set when this row was inert/contested at 45.7); the working
    # shock + history put it near-total. draws scarce (decisive-split appropriate).
    ('C5','Cav vs SHAKEN Line (m2/start6)','Arrowhead','Line',dict(CAV),
        {'morale':2,'morale_start':6},65,98,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C5 exploits shaken; near-total ceiling]
    # C6: cavalry vs a BRACED-shallow line (hold + disc8 + 'brace') -- a faced brace still repels
    # frontally (the recoil needs discipline x some depth, not maximal depth). Control duplicate of C2
    # on a shallower wall; same RAW cav-a-LOW judgement, draws expected.
    # [ED-MB-0041] C6 is now genuinely SHALLOW (width 6 x depth 1) so it actually tests what its label
    # claims — a thin braced line vs C2's deep block. The two rows were previously identical inputs
    # with a fixed seed_base, i.e. the same run counted as two passes.
    ('C6','Cav vs BRACED-shallow Line (hold+d8+brace)','Arrowhead','Line',dict(CAV),
        {'stance':'hold','discipline':8,'instructions':('brace',),'width':6,'depth':1,'troop_type':'pike'},0,30,'high','rawA'),  # [canonical: mass_battle_gauge_grounding.md §3 — C6 = C2; raw cav-a LOW]
    # C7: cavalry ENVELOPS a holding line (Horseshoe vs hold+disc8) -- the flank/rear bypasses the
    # frontal brace (you cannot face the rear, Burkholder 2007). An immobile (hold-stance) line that
    # cannot turn to face the encirclement is ANNIHILATED when resolved (Cannae/Adrianople) -> decA
    # saturates to ~100 (infantry never wins); the brace only DELAYS the kill (higher draw rate than
    # the unbraced C4). Decisive-to-total -> ceiling 100. NOTE: C7 uses hold-only, NOT the 'brace'
    # instruction, deliberately -- the reciprocal charge-recoil (orchestration ~L1647) does NOT
    # zone-gate, so a braced+enveloped unit would WRONGLY fire the recoil from the rear. [FLAG: latent
    # engine issue -- the recoil should fire frontally only; out of scope here, see grounding §4.]
    # [2026-07-05 fix, same DG-1 composition rationale as C4 above]
    ('C7','Cav envelop vs holding Line (hold+d8)',_envelop_army,'Line',
        {'pin_frac':2/3,'wing_troop_type':'cavalry','wing_speed':'Fast'},{'stance':'hold','discipline':8},65,100,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C7 envelop bypasses brace; Cannae-total ceiling]
]

def winner_of(r):
    return r.get('winner','draw')

SINGLE_TURN_CAP = 18          # [canonical: mass_battle_gauge_grounding.md §1 — single-mode tick cap]
MULTI_BATTLE_TURN_CAP = 20    # [canonical: mass_battle_gauge_grounding.md §1 — multi-mode battle-turn cap]

# ─── CASUALTY / DURATION REALISM BANDS (ED-MB-0041) ──────────────────────────
# The win-share bands above ask "how often does A beat B". They cannot distinguish a double
# envelopment from two lines colliding, because both can produce the same win-share -- which is exactly
# how the reachability sweep found a configuration that passes the Cannae row with envelopment pathing
# switched OFF. These bands ask the question the sources actually constrain: what did it COST, and did
# it resolve at all. `matchup()` already computed every input; nothing here is new instrumentation.
#
# PROVENANCE -- deliberately narrow. Each band is either in-repo or a logical consequence of one; none
# is an invented literature interval.
#   LOSER_CAS_BAND  the losing side's mean casualties at the decision. 15-30% is the repo's OWN
#                   rout-onset band (ED-MB-0031, "routs at 15% early / 30% upper"), already used to
#                   draw each subunit's stochastic break-point. If a body breaks at 15-30% losses, the
#                   side that broke should be carrying about that when the battle is decided.
#   WINNER_CAS_MAX  the winner did not break, by definition. So its losses must sit BELOW the floor of
#                   the same break band. This is not a second estimate -- it is the first one's
#                   contrapositive, which is why it needs no independent source.
#   CAPPED_MAX      fraction of seeds that ran to the turn cap without resolving. A structural check,
#                   not a historical one: a matchup that times out has not been measured. This is the
#                   check that would have caught H6 reading 0.0/0.0 casualties across 60/60 seeds.
# DURATION IS DELIBERATELY *NOT* BANDED ABSOLUTELY. An engine "turn" has no defensible mapping to real
# time, so any interval in turns would be fabricated to look grounded. The cap-hit rate is the honest
# part of the duration question and is the only part banded.
LOSER_CAS_BAND = (15.0, 30.0)   # [canonical: ED-MB-0031 stochastic-rout breakpoint band, 15-30% casualties]
WINNER_CAS_MAX = 15.0           # [canonical: contrapositive of ED-MB-0031 — the winner did not break, so it is below the break floor]
CAPPED_MAX = 20.0               # [JUSTIFIED: structural, not historical — a matchup that times out on >1 seed in 5 has not been measured]


def casualty_verdict(r):
    """Judge one matchup result against the realism bands. Returns (ok, flag, detail-string).

    A row with no decisive result is UNMEASURED, never a pass: `win_cas`/`lose_cas` are None there,
    and treating an absent measurement as 0.0 would silently satisfy the winner-cost check.
    """
    if r['win_cas'] is None or r['lose_cas'] is None:
        return False, 'UNMEASURED', 'no decisive result'
    lo, hi = LOSER_CAS_BAND
    loser_ok = lo <= r['lose_cas'] <= hi
    winner_ok = r['win_cas'] < WINNER_CAS_MAX
    capped_ok = r['capped'] <= CAPPED_MAX
    if loser_ok and winner_ok and capped_ok:
        return True, 'OK', ''
    why = []
    if not loser_ok:
        why.append(f'loser {r["lose_cas"]:.0f}% outside {lo:.0f}-{hi:.0f}')
    if not winner_ok:
        why.append(f'winner {r["win_cas"]:.0f}% >= {WINNER_CAS_MAX:.0f}')
    if not capped_ok:
        why.append(f'capped {r["capped"]:.0f}%')
    return False, 'UNREAL', '; '.join(why)


def matchup(sa, sb, ka, kb, mode, n=60, seed_base=1_000_000):  # [Jordan directive 2026-07-01: n 120->60 for runtime; SE~sqrt(0.25/n) rises ~4.6pp->~6.5pp at p=0.5, vs the grounding doc's cited n=120/SE~5pp basis (mass_battle_gauge_grounding.md §1)]
    # sa/sb: a plain shape string (single-subunit, via make_unit) or an army-builder callable
    # (_envelop_army/_refused_army) for the composed Envelopment/Refused-Flank presets that replaced
    # the retired Horseshoe/RefusedFlank shapes (LC-8). resolve_battle's shape_a/shape_b positional
    # is only consulted by reset_positions as a defensive fallback now (every subunit resets to its
    # OWN spawn position first) -- 'Line' is a safe placeholder for a callable side.
    a_is_fn = callable(sa); b_is_fn = callable(sb)
    aw=bw=dr=0; turns=[]; a_cas=[]; b_cas=[]
    # [ED-MB-0041] WINNER/LOSER-CONDITIONED casualties + cap-hit rate. The per-side means below
    # (a_cas/b_cas) average over ALL seeds regardless of who won, which is the wrong quantity to compare
    # against history: the sources constrain what the LOSER lost and how much less the WINNER lost, and
    # in a near-even matchup the per-side means wash that asymmetry out entirely. Collected per decisive
    # seed and conditioned on the outcome. `capped` counts seeds that ran to the turn cap without
    # resolving — the structural check that would have caught H6's 0.0/0.0 all-draw instrument break.
    win_cas=[]; lose_cas=[]; capped=0
    for s in range(n):
        with rngsource.using(draw.seeded(draw.H2("gauge_mb", s+seed_base))):
            ua = sa('A','A',**ka) if a_is_fn else make_unit(sa,3,'A','A',**ka)  # [canonical: sim_mb_06_v9_historical_spec.md — T3 (tier-3) units]
            ub = sb('B','B',**kb) if b_is_fn else make_unit(sb,3,'B','B',**kb)
            a0,b0 = ua.hp_max, ub.hp_max
            shape_a = 'Line' if a_is_fn else sa
            shape_b = 'Line' if b_is_fn else sb
            # [ED-MB-0041] The cap is bound ONCE and reused for both the resolve call and the cap-hit
            # test below. It was previously written as a literal in each of the two resolve_battle calls,
            # and the cap-hit check would have needed a third and fourth copy -- at which point a future
            # change to one would silently stop the "did this battle actually resolve" measurement from
            # meaning anything, while still reporting a number.
            cap = SINGLE_TURN_CAP if mode=='single' else MULTI_BATTLE_TURN_CAP
            if mode=='single':
                r=resolve_battle(ua,ub,kind='single',max_ticks=cap); turns.append(r.get('turns',cap))
            else:
                r=resolve_battle(ua,ub,shape_a,shape_b,ANCHOR_MAP,kind='multi',max_battle_turns=cap); turns.append(r.get('battle_turns',cap))
            w=winner_of(r)
            if w=='A':aw+=1
            elif w=='B':bw+=1
            else:dr+=1
            _ac = 100*(a0-ua.hp)/a0 if a0 else 0; _bc = 100*(b0-ub.hp)/b0 if b0 else 0
            a_cas.append(_ac); b_cas.append(_bc)
            if w=='A': win_cas.append(_ac); lose_cas.append(_bc)
            elif w=='B': win_cas.append(_bc); lose_cas.append(_ac)
            if turns[-1] >= cap: capped += 1
    dec = aw+bw
    return dict(a=aw/n*100, b=bw/n*100, d=dr/n*100,
                decA=(100*aw/dec if dec else 50.0), dec_n=dec,  # [canonical: mass_battle_gauge_grounding.md §1 — even-split fallback when no decisive result]
                t=statistics.mean(turns), a_cas=statistics.mean(a_cas), b_cas=statistics.mean(b_cas),
                # [ED-MB-0041] None (not 0.0) when no decisive result: an absent measurement must not
                # read as "the winner lost nothing", which would silently PASS the asymmetry check.
                win_cas=(statistics.mean(win_cas) if win_cas else None),
                lose_cas=(statistics.mean(lose_cas) if lose_cas else None),
                capped=capped/n*100)

def run(mode, tests=TESTS, n=60):  # [Jordan directive 2026-07-01: default sample n 120->60 for runtime — see matchup()]
    print(f"\n----- MODE: {mode}  (engine: mass_battle package)  metric: DECISIVE split A/(A+B); RAW A% for 'rawA' repel rows -----")
    print(f"  {'id':4} {'matchup':30} {'A%':>5} {'B%':>5} {'D%':>5} {'val':>5} {'band':>7} {'dexp':>4} {'m':>4} verdict")
    nb=0; cas_rows=[]
    for t in tests:
        tid,label,sa,sb,ka,kb,lo,hi,dexp,*rest = t
        metric = rest[0] if rest else 'decA'  # [canonical: mass_battle_gauge_grounding.md §1 — decA default; rawA for braced-repel rows]
        r=matchup(sa,sb,ka,kb,mode,n=n)
        if metric=='rawA':
            # REPEL rows (braced wall): judge RAW cavalry (A) win-rate LOW. A repulse is a HOLD, so the
            # decisive-split (tiny decisive n) is uninformative and high draws are EXPECTED (not penalised).
            val=r['a']; win_ok = lo<=val<=hi; draw_ok = True
            flag = 'REPELLED' if (win_ok and draw_ok) else 'NOT-REPELLED'
        else:
            val=r['decA']; win_ok = (r['dec_n']>0) and (lo<=val<=hi)
            draw_ok = (dexp!='low') or (r['d']<30.0)  # [canonical: mass_battle_gauge_grounding.md §1 — decisive matchups expect draw<30%]
            flag = 'OK' if (win_ok and draw_ok) else ('WIN-OUT' if not win_ok else 'TOO-DRAWISH')
            if r['dec_n']==0: flag='UNRESOLVED'
        ok = win_ok and draw_ok
        nb+=ok
        print(f"  {tid:4} {label[:30]:30} {r['a']:5.1f} {r['b']:5.1f} {r['d']:5.1f} {val:5.1f} {lo:>3}-{hi:<3} {dexp:>4} {metric:>4} {flag}")
        cas_rows.append((tid, label, r))
    print(f"  => pass {nb}/{len(tests)}  (bands are HISTORY-grounded; a fail flags engine divergence, not a band to lower)")

    # [ED-MB-0041] SECOND scoreboard, reported separately and NOT folded into the win-share count --
    # so `nb` stays comparable with every figure already recorded in the ledger, handoff and PR bodies,
    # while the harder question is visible beside it rather than buried in a returned dict.
    print(f"\n  --- casualty/duration realism (loser {LOSER_CAS_BAND[0]:.0f}-{LOSER_CAS_BAND[1]:.0f}%, "
          f"winner <{WINNER_CAS_MAX:.0f}%, capped <={CAPPED_MAX:.0f}%) ---")
    print(f"  {'id':4} {'matchup':30} {'win%':>6} {'lose%':>6} {'turns':>6} {'cap%':>5}  verdict")
    cb = 0
    for tid, label, r in cas_rows:
        ok, cflag, why = casualty_verdict(r)
        cb += ok
        wc = '  n/a' if r['win_cas'] is None else f"{r['win_cas']:6.1f}"
        lc = '  n/a' if r['lose_cas'] is None else f"{r['lose_cas']:6.1f}"
        print(f"  {tid:4} {label[:30]:30} {wc} {lc} {r['t']:6.1f} {r['capped']:5.1f}  "
              f"{cflag}{(' — ' + why) if why else ''}")
    print(f"  => casualty-realism pass {cb}/{len(tests)}")
    return nb

# ═════════════════════════════════════════════════════════════════════════════════════════════════
# THE "RESULTS" BLOCK (B19.01; proposals/.../26_MASS_BATTLE_calibration_targets.md §1-§2).
#
# The win-share block above is untouched. This block reads RESULTS -- who loses how much, how often a field is
# decided -- as ratios and orderings (never a historical percentage against an engine loss: history counts the dead,
# the engine counts men lost to the fight, so only a ratio of two engine losses has no unit). Each scenario is built
# through the season's own constructors and fought by the season's own entry: the order of battle is the army record's
# (`troop_types/presets.plan` -> `armyrecord.apply` -> `armyrecord.to_order_of_battle`), the field is
# `massbattle.resolve_field` over a `MassBattleInput`, and a side's band is `ladder.field_degree`'s. It writes nothing
# tracked. A reading outside a TARGET is reported with its scenario and seeds; the band is NOT moved to fit; a failed
# flag or ordering is a finding about a mechanism, not a number to tune. No band here gates a merge.
#
#   PYTHONHASHSEED=0 python tests/sim/gauge_mb.py --results [--n N] [--only T-2,T-9] [--jobs J]
#
# `--n` defaults to the source's 400 (its floor: "n at least 400 seeded fields per scenario"); `--only` and `--jobs`
# change which rows run and on how many processes, never what a seed draws, so a same-seed table is the same table.
# A row whose mechanism is not in the tree prints "no mechanism", never a number; the probe for each is below.
# ═════════════════════════════════════════════════════════════════════════════════════════════════
RESULTS_N = 400                 # [canonical: calibration targets §1 -- "n at least 400 seeded fields per scenario"]
RESULTS_SEED = "gauge_mb_results"   # the seeded key: field `s` of every scenario draws from H2(RESULTS_SEED, s), so arms share seeds

# (id, reading, lo, hi, band as printed, source and tier, status of the band). THE ONLY PLACE A BAND IS WRITTEN:
# a reading is judged against these rows and never against a literal in the code that reads it.
RESULTS = [
    ('T-1', "the winner's share lost in a decided even field (median)", None, 0.10,
     'reported; flag if median > 0.10', 'CR A1 [D]; CR A11 [D]', 'flag (the unit differs)'),
    ('T-2', "loser's loss / winner's loss, even field, no pursuit possible", 1.7, 5.2,
     '1.7 to 5.2 (centre near 3)', 'Krentz (CR A1, A2 [D])', 'target'),
    ('T-3', "loser's loss with mounted pursuit / without, same seeds", 2.0, 5.0,
     '2 to 5', 'CR A1, A6 [D]', 'target; wide on purpose'),
    ('T-4', "share of even fields decided within 1 bout, and within max_bouts", None, None,
     'reported; the second must exceed the first', 'CR C1 [D]', 'ordering only'),
    ('T-5', "share of decided fields where the loser broke below the casualty floor", None, None,
     '> 0 with stand_draw on; 0 with it off', 'CR D5 [D]', 'ordering against the control'),
    ('T-6', "horse charging frontally: unbraced foot > braced pole-armed foot > 0; shaken foot highest", None, None,
     'the ordering', 'MV H1-H3 [T]; rows C1, C2, C5', 'ordering'),
    ('T-7', "no scenario's win share is 0 or 1", 0.0, 1.0,
     'every share inside (0, 1)', 'the standing rule', 'target'),
    ('T-8', "fresh against tired: entry_stamina 0.5 against 1.0", None, None,
     'loses more often than the mirror, by more than the sampling band', 'CR D3 [D]', 'ordering'),
    ('T-9', "numbers: win share of the larger side at 2:1 and 3:1", None, 1.0,
     'rises with the ratio; below 1', 'CR D8 [T]', 'ordering'),
    ('T-10', "of men lost in flight under mounted pursuit, the share captured (mean)", 0.2, 0.8,
     '0.2 to 0.8 as a mean, not constant across seeds', 'CR A6, section B', 'flag; three battles'),
]
_BAND = {r[0]: (r[2], r[3]) for r in RESULTS}

_SPEAR_UNIT = 300       # troops in one spear unit of the even-foot and numbers scenarios (a unit is at least 4 cells of 50: 200)
_EVEN_FOOT_UNITS = 4    # two equal spear armies of 4 x 300 = 1200 troops (an army is at least MIN_ARMY_TROOPS = 1000)
_PRESET_WEIGHT = 20     # "the preset army of a weight-20 faction": one cohort of weight 20 with a full Site of every kind
_CHARGE_HORSE, _CHARGE_FOOT = 200, 400
_SHAKEN_STANCE = -3.0   # the season's shaken: a side's morale start is 5 + its mean stance toward its faction, clamped to 1..7 (-3 -> 2)
_SEAT_Z = 2.0           # the sampling band of a seat-symmetry control: z standard errors of the difference of two shares of n


def _results_inputs():
    """The pieces every scenario shares, built once per process by the season's own owners: the condition scale, the geography
    and the preset order of battle of a weight-20 faction (`presets.plan` -> `armyrecord.apply` -> `to_order_of_battle`)."""
    import yaml
    from engine.season.data import files
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.queries.inputs import ArmyCommand, ArmyPresetQuery
    from modules.mass_battle import armyrecord
    from modules.mass_battle.troop_types import presets, recruitment
    scale = DEFAULT_FIXTURES.get("condition_scale")
    with open(files.GEOGRAPHY_YAML, encoding="utf-8") as f:
        geo = yaml.safe_load(f)
    sites = {kind: float(scale) for kind, _floor in recruitment.TRAINING_SITE.values()}
    plan = presets.plan(ArmyPresetQuery("fac_results", (("c0", _PRESET_WEIGHT, sites),), scale, ()))
    verb_op = {'recruit': 'recruit', 'form_unit': 'form', 'assign_troops': 'assign'}
    rec = armyrecord.new("fac_results")
    for verb, payload in plan:
        args = dict(payload)
        if verb == 'recruit':
            args.update(weight=_PRESET_WEIGHT, sites=sites, full=scale)
        rec = armyrecord.apply(ArmyCommand(rec, verb_op[verb], args))
    return scale, geo, armyrecord.to_order_of_battle(rec)


_SHARED = {}


def _shared():
    if not _SHARED:
        _SHARED['v'] = _results_inputs()
    return _SHARED['v']


def _no_horse(oob):
    """The same order of battle with every mounted unit (and the cohort draws that fed it) taken out."""
    import dataclasses
    from modules.mass_battle.orderofbattle import class_of
    keep = tuple(u for u in oob.units if class_of(u.troop_type) != 'mounted')
    names = {u.name for u in keep}
    return dataclasses.replace(oob, units=keep, drawn=tuple(d for d in oob.drawn if d[0] in names))


def _spears(k):
    from modules.mass_battle.orderofbattle import OrderOfBattle, UnitRow
    return OrderOfBattle(tuple(UnitRow(f'spear_{i + 1}', 'spearmen', float(_SPEAR_UNIT)) for i in range(k)))


def _line(troop_type, troops, role=None):
    from modules.mass_battle.orderofbattle import OrderOfBattle, UnitRow
    return OrderOfBattle((UnitRow(troop_type, troop_type, float(troops), role=role),))


def _scenario(key):
    """`(attacker's order, defender's order, stances)` for one scenario key. The attacker is the scenario's SUBJECT (the horse, the
    larger side); on an even scenario the seats are the two sides and the control is that their win shares are equal."""
    _scale, _geo, preset = _shared()
    horse = lambda: _line('cavalry', _CHARGE_HORSE, role='Shock')
    even = (0.0, 0.0)
    return {
        'foot':             (_spears(_EVEN_FOOT_UNITS), _spears(_EVEN_FOOT_UNITS), even),
        'combined':         (preset, preset, even),
        'combined_nohorse': (_no_horse(preset), _no_horse(preset), even),
        'charge_levy':      (horse(), _line('levy', _CHARGE_FOOT), even),
        'charge_pike':      (horse(), _line('pike', _CHARGE_FOOT, role='ShieldWall'), even),
        'charge_shaken':    (horse(), _line('spearmen', _CHARGE_FOOT), (0.0, _SHAKEN_STANCE)),
        'charge_control':   (horse(), horse(), even),
        'numbers_1':        (_spears(1), _spears(1), even),
        'numbers_2':        (_spears(2), _spears(1), even),
        'numbers_3':        (_spears(3), _spears(1), even),
    }[key]


# per-scenario cost, heaviest first, so the pool is not left waiting on the 20,000-troop armies
SCENARIOS = ('combined', 'combined_nohorse', 'foot', 'charge_levy', 'charge_pike', 'charge_shaken', 'charge_control',
             'numbers_1', 'numbers_2', 'numbers_3')
EVEN_SCENARIOS = ('foot', 'combined', 'combined_nohorse', 'charge_control', 'numbers_1')   # the seats are the two sides: gate 3's control
_ROW_SCENARIOS = {
    'T-1': ('foot', 'combined', 'combined_nohorse'), 'T-2': ('foot', 'combined_nohorse'),
    'T-3': ('combined', 'combined_nohorse'), 'T-4': ('foot', 'combined'),
    'T-6': ('charge_levy', 'charge_pike', 'charge_shaken', 'charge_control'), 'T-7': SCENARIOS,
    'T-9': ('numbers_1', 'numbers_2', 'numbers_3'),
}

import collections
Fld = collections.namedtuple('Fld', 'band a_loss b_loss ended ticks')   # one fought field: the band `field_degree` reads, each side's share lost


def _fight(args):
    """Fields `lo..hi-1` of one scenario, in seed order. Runs in a worker; draws only from its own seeded rng."""
    from engine.season.queries.inputs import FieldOutcome, MassBattleInput
    from engine.season.seam.ladder import field_degree
    from modules.mass_battle import massbattle
    key, lo, hi = args
    scale, geo, _preset = _shared()
    oob_a, oob_b, stances = _scenario(key)
    inp = MassBattleInput(weights=((1.0,), (1.0,)), territory=None, fort_level=0.0, stances=stances, walls_dr=None, origin=None,
                          loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo, condition_scale=scale,
                          orders_of_battle=(oob_a, oob_b))
    out = []
    for s in range(lo, hi):
        r = massbattle.resolve_field(inp, draw.seeded(draw.H2(RESULTS_SEED, s)))
        if not isinstance(r, FieldOutcome):
            raise RuntimeError(f"{key} seed {s}: the field was refused, not fought: {r!r}")
        out.append(Fld(field_degree(r), 1 - r.attacker.share / scale, 1 - r.defender.share / scale, r.ended, r.ticks))
    return key, lo, out


def _fight_all(keys, n, jobs):
    """{scenario: [Fld per seed 0..n-1]}. The same seeds in every scenario; a chunk's place in the answer is its seed, so the
    process count changes the clock and never the table."""
    import multiprocessing
    chunk = 10
    tasks = [(k, lo, min(n, lo + chunk)) for k in SCENARIOS if k in keys for lo in range(0, n, chunk)]
    done = {k: {} for k in keys}
    if jobs <= 1:
        results = map(_fight, tasks)
    else:
        pool = multiprocessing.get_context('fork').Pool(jobs)
        results = pool.imap_unordered(_fight, tasks)
    try:
        for key, lo, flds in results:
            done[key][lo] = flds
    finally:
        if jobs > 1:
            pool.close(); pool.join()
    return {k: [f for lo in sorted(done[k]) for f in done[k][lo]] for k in done}


def _decided(flds):
    """`(winner_loss, loser_loss)` per decided field -- the band is `field_degree`'s, the attacker's own Won or Lost."""
    from engine.season.data.rosters import LOST, WON
    return [((f.a_loss, f.b_loss) if f.band == WON else (f.b_loss, f.a_loss)) for f in flds if f.band in (WON, LOST)]


def _win_share(flds, seat='A'):
    from engine.season.data.rosters import LOST, WON
    return sum(f.band == (WON if seat == 'A' else LOST) for f in flds) / len(flds)


def _seat_symmetry(flds):
    """Gate 3: on an even scenario the attacker's seat and the defender's win equally often, to within `_SEAT_Z` standard errors
    of the difference of two shares of n. Returns (a share, b share, |difference|, band, inside)."""
    a, b, n = _win_share(flds, 'A'), _win_share(flds, 'B'), len(flds)
    band = _SEAT_Z * ((a + b - (a - b) ** 2) / n) ** 0.5
    return a, b, abs(a - b), band, abs(a - b) <= band


def _median(xs):
    return statistics.median(xs) if xs else None


def _ratio(flds):
    """Loser's loss / winner's loss over a scenario's decided fields: the ratio of means, then the median of the per-field ratios
    (fields in which the winner lost nothing have no ratio and are counted out of the second). None if nothing was decided."""
    d = _decided(flds)
    if not d or statistics.mean(w for w, _l in d) == 0:
        return None
    each = [l / w for w, l in d if w > 0]
    return statistics.mean(l for _w, l in d) / statistics.mean(w for w, _l in d), _median(each), len(d), len(each)


def _t3_reading(with_horse, without):
    """T-3: loser's loss with mounted pursuit / loser's loss without, same seeds. A pure function of the two arms' fields."""
    lw = [l for _w, l in _decided(with_horse)]
    lo = [l for _w, l in _decided(without)]
    if not lw or not lo or statistics.mean(lo) == 0:
        return None
    return statistics.mean(lw) / statistics.mean(lo)


# ── the probes: is the mechanism a row reads in the tree? (a row without one prints "no mechanism", never a number) ──────────
def _in_tree(name):
    """True when `name` is a field of the field's input/output records, a name in `modules.mass_battle.config`, or a key of
    `references/troops.yaml` (the three places a calibrated mechanism's knob lives)."""
    import dataclasses
    from engine.season.queries import inputs
    import modules.mass_battle.config as cfg
    fields = {f.name for rec in (inputs.MassBattleInput, inputs.FieldOutcome, inputs.SideOutcome) for f in dataclasses.fields(rec)}
    if name in fields or any(n.lower() == name.lower() for n in dir(cfg)):
        return True
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'references', 'troops.yaml'), encoding='utf-8') as f:
        return name in f.read()


def _pursuit_in_the_field(seeds=5):
    """T-3's mechanism: is `orchestration.pursuit_damage` reached from `resolve_field`? Counted over the charge fields, the ones in
    which a body of foot breaks with horse standing (the season's pursuit has to be there if it is anywhere)."""
    from modules.mass_battle import massbattle, orchestration
    from engine.season.queries.inputs import MassBattleInput
    scale, geo, _preset = _shared()
    real, calls = orchestration.pursuit_damage, [0]
    def counting(*a, **k):
        calls[0] += 1
        return real(*a, **k)
    orchestration.pursuit_damage = counting
    try:
        for key in ('charge_levy', 'charge_shaken'):
            oob_a, oob_b, stances = _scenario(key)
            inp = MassBattleInput(weights=((1.0,), (1.0,)), territory=None, fort_level=0.0, stances=stances, walls_dr=None, origin=None,
                                  loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo, condition_scale=scale,
                                  orders_of_battle=(oob_a, oob_b))
            for s in range(seeds):
                massbattle.resolve_field(inp, draw.seeded(draw.H2(RESULTS_SEED, s)))
    finally:
        orchestration.pursuit_damage = real
    return calls[0] > 0


def _pct(x):
    return 'n/a' if x is None else f'{100 * x:.1f}%'


def run_results(n=RESULTS_N, only=None, jobs=None, out=print):
    """Print the ten rows of the results table with the reading, the band, n and the same-run control; write nothing tracked.
    `only` is a set of row ids (None is all ten). Returns {row id: (verdict, reading)} for the caller that wants the numbers."""
    jobs = jobs or os.cpu_count() or 1
    want = set(only) if only else {r[0] for r in RESULTS}
    keys = set()
    for rid in want:
        keys |= set(_ROW_SCENARIOS.get(rid, ()))
    t0 = __import__('time').time()
    S = _fight_all(keys, n, jobs) if keys else {}
    ids = [r[0] for r in RESULTS if r[0] in want]
    rows = {r[0]: r for r in RESULTS}
    seeds = f'seeds H2("{RESULTS_SEED}", 0..{n - 1})'
    got = {}
    out(f"\n----- RESULTS (calibration targets T-1..T-10)  n={n} fields per scenario, {seeds}; a reading outside a target is reported, never moved to -----")
    if n < RESULTS_N:
        out(f"  !! n={n} is below the source's {RESULTS_N}: this table is not the baseline")
    out(f"  {'id':5} {'verdict':14} reading  [band; status]   control")

    def line(rid, verdict, text, control=''):
        r = rows[rid]
        got[rid] = (verdict, text)
        out(f"  {rid:5} {verdict:14} {text}  [{r[4]}; {r[6]}]" + (f"\n  {'':5} {'':14} control: {control}" if control else ''))

    def seat_controls(names):
        parts, ok = [], True
        for k in names:
            a, b, d, band, inside = _seat_symmetry(S[k])
            ok &= inside
            parts.append(f"{k} A {_pct(a)} / B {_pct(b)} |d|={100 * d:.1f}pp band {100 * band:.1f}pp {'in' if inside else 'OUT'}")
        return '; '.join(parts), ok

    def verdict_target(rid, v):
        lo, hi = _BAND[rid]
        return 'NO-READING' if v is None else ('IN-BAND' if (lo is None or v >= lo) and (hi is None or v <= hi) else 'OUT-OF-BAND')

    if 'T-1' in want:
        sc = ('foot', 'combined', 'combined_nohorse')
        meds = {k: _median([w for w, _l in _decided(S[k])]) for k in sc}
        text = '; '.join(f"{k} median {'n/a (none decided)' if meds[k] is None else f'{meds[k]:.3f}'} of {len(_decided(S[k]))} decided" for k in sc)
        flagged = [k for k in sc if meds[k] is not None and meds[k] > _BAND['T-1'][1]]
        ctrl, _ok = seat_controls(sc)
        line('T-1', 'FLAG' if flagged else ('NO-READING' if all(m is None for m in meds.values()) else 'ok'),
             text + (f" -- over {_BAND['T-1'][1]}: {', '.join(flagged)}" if flagged else ''), ctrl)
    if 'T-2' in want:
        sc = ('foot', 'combined_nohorse')
        reads = {k: _ratio(S[k]) for k in sc}
        text = '; '.join(f"{k} " + ('n/a (none decided or winner lost nothing)' if reads[k] is None else
                         f"{reads[k][0]:.2f} (median per field {reads[k][1]:.2f}, {reads[k][2]} decided)") for k in sc)
        vs = [verdict_target('T-2', None if reads[k] is None else reads[k][0]) for k in sc]
        ctrl, _ok = seat_controls(sc)
        line('T-2', 'OUT-OF-BAND' if 'OUT-OF-BAND' in vs else ('NO-READING' if 'NO-READING' in vs else 'IN-BAND'), text, ctrl)
    if 'T-3' in want:
        if not _pursuit_in_the_field():
            line('T-3', 'no mechanism', "pursuit_damage is not reached from resolve_field (0 calls over 10 charge fields), so a with/without-horse ratio would read the horse's presence, not its pursuit")
        else:
            v = _t3_reading(S['combined'], S['combined_nohorse'])
            line('T-3', verdict_target('T-3', v), f"combined with horse / without: {'n/a' if v is None else f'{v:.2f}'} ({len(_decided(S['combined']))} / {len(_decided(S['combined_nohorse']))} decided)",
                 'the no-horse arm of the same seeds is the denominator')
    if 'T-4' in want:
        parts = []
        for k in ('foot', 'combined'):
            parts.append(f"{k}: decided in the one engagement {_pct(len(_decided(S[k])) / len(S[k]))} ({len(_decided(S[k]))}/{len(S[k])}); within max_bouts: "
                         + ('no mechanism (max_bouts is not in the tree)' if not _in_tree('max_bouts') else 'mechanism present, reading not written'))
        ctrl, _ok = seat_controls(('foot', 'combined'))
        line('T-4', 'reported', '; '.join(parts), ctrl)
    if 'T-5' in want:
        line('T-5', 'no mechanism' if not _in_tree('stand_draw') else 'unread', "stand_draw is not in the tree" if not _in_tree('stand_draw') else 'mechanism present, reading not written')
    if 'T-6' in want:
        ws = {k: _win_share(S[k]) for k in ('charge_levy', 'charge_pike', 'charge_shaken', 'charge_control')}
        ordering = ws['charge_levy'] > ws['charge_pike'] > 0
        shaken_highest = ws['charge_shaken'] > ws['charge_levy']
        a, b, d, band, inside = _seat_symmetry(S['charge_control'])
        text = (f"horse win share v unbraced levy {_pct(ws['charge_levy'])}, v braced pike {_pct(ws['charge_pike'])}, v shaken spear "
                f"(morale start 2) {_pct(ws['charge_shaken'])}; unbraced > braced > 0: {'holds' if ordering else 'FAILS'}; shaken highest: {'holds' if shaken_highest else 'FAILS'}")
        line('T-6', 'ORDER-HOLDS' if ordering and shaken_highest else 'ORDER-FAILS', text,
             f"horse v horse A {_pct(a)} / B {_pct(b)} |d|={100 * d:.1f}pp band {100 * band:.1f}pp {'in' if inside else 'OUT'}")
    if 'T-7' in want:
        shares = {k: _win_share(S[k]) for k in SCENARIOS}
        bad = [k for k, v in shares.items() if not 0.0 < v < 1.0]
        line('T-7', 'OUT-OF-BAND' if bad else 'IN-BAND',
             'subject (attacker-seat) win share: ' + ', '.join(f"{k} {_pct(v)}" for k, v in shares.items())
             + (f" -- 0 or 1: {', '.join(bad)}" if bad else ''), f"n = {n} per scenario")
    if 'T-8' in want:
        has = _in_tree('entry_stamina')
        line('T-8', 'no mechanism' if not has else 'unread', 'MassBattleInput.entry_stamina is not in the tree' if not has else 'mechanism present, reading not written')
    if 'T-9' in want:
        ws = [_win_share(S[k]) for k in ('numbers_1', 'numbers_2', 'numbers_3')]
        rises = ws[0] < ws[1] < ws[2] and ws[2] < 1.0
        line('T-9', 'ORDER-HOLDS' if rises else 'ORDER-FAILS',
             f"larger side's win share 1:1 {_pct(ws[0])}, 2:1 {_pct(ws[1])}, 3:1 {_pct(ws[2])}; rises and stays below 1: {'holds' if rises else 'FAILS'}",
             'the 300 v 300 field is the 1:1 arm; its seats: ' + seat_controls(('numbers_1',))[0])
    if 'T-10' in want:
        has = _in_tree('captured')
        line('T-10', 'no mechanism' if not has else 'unread', 'no record of the field carries a captured share' if not has else 'mechanism present, reading not written')
    if keys:
        _ctrl, _ok = seat_controls([k for k in EVEN_SCENARIOS if k in S])
        out(f"  gate 3, side symmetry of every even scenario: {'all inside' if _ok else 'OUTSIDE for at least one'}  ({_ctrl})")
    out(f"  ({len(ids)} rows, {len(keys)} scenarios x {n} fields)")
    print(f"  [clock, not part of the table] {jobs} process(es), {__import__('time').time() - t0:.0f}s", file=sys.stderr)
    return got


def _results_main(argv):
    def opt(flag, default=None, cast=str):
        return cast(argv[argv.index(flag) + 1]) if flag in argv else default
    only = opt('--only')
    return run_results(n=opt('--n', RESULTS_N, int), only=only.split(',') if only else None, jobs=opt('--jobs', None, int))


if __name__=='__main__':
    if '--results' in sys.argv:
        _results_main(sys.argv); sys.exit(0)
    # Cavalry rows are PER_CELL=1-only (engine gates charge_pen + speed mult on PER_CELL). Read the
    # RESOLVED config value (modules.mass_battle.config.PER_CELL), not a second, independently-defaulted
    # os.environ.get -- the latter drifted out of sync with config.PER_CELL's own default the moment
    # gate 4 (ED-MB-0001) flipped PER_CELL's default '0'->'1': a bare invocation now runs the engine
    # with PER_CELL=True, but a locally re-derived '0' fallback here would still silently exclude
    # CAV_TESTS, exactly the mode-key mismatch bat.py's compute() was fixed for at the same time.
    import modules.mass_battle.config as _mb_cfg
    _pc = _mb_cfg.PER_CELL
    _tests = TESTS + (CAV_TESTS if _pc else [])
    s=run('single', _tests); m=run('multi', _tests)
    n=len(_tests)
    print(f"\n==== mass_battle package: single={s}/{n}  multi={m}/{n} (multi is the resolving mode) ====")
