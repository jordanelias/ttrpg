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
PC_NODE_COHESION, ...) select, not a frozen snapshot file.

Grounding + citations index: references/historical/mass_battle_gauge_grounding.md
"""
import sys, os, random, statistics

# import the package exactly as bat.py (the G5 digest harness) does
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # tests/sim on path
from mass_battle.engine import (  # noqa: E402
    Subunit, Unit, SIDE_A_START_ROW, SIDE_B_START_ROW,
    run_battle, run_multi_turn_battle, build_unit, build_army, build_envelopment, build_refused_flank,
    resolve_battle, _centered_line_cols)
from mass_battle.config import TROOPS_PER_TIER  # noqa: E402

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
    # since those Unit-level presets are now built from Line-shaped center/wing/refused subunits.
    ('Line',1):11,('Line',2):10,('Line',3):9,('Line',4):8,                       # [canonical: mass_battle_v30.md §deployment]
    ('Arrowhead',1):11,('Arrowhead',2):10,('Arrowhead',3):8,('Arrowhead',4):7,   # [canonical: mass_battle_v30.md §deployment]
    ('GappedLine',1):11,('GappedLine',2):9,('GappedLine',3):7,                   # [canonical: mass_battle_v30.md §deployment]
}

def make_mixed_unit(specs, name, faction, power=4, command=4, discipline=5, morale=6,  # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats P4/C4/D5/M6, same baseline as make_unit's defaults below]
                    morale_start=None, dr=1, stance='balanced', speed='Standard'):
    """Build a MULTI-subunit Unit with per-subunit stats (Jordan directive: different unit
    types / troop counts per subunit). `specs` = list of dicts; each may set shape, tier, troop_type,
    unit_type, stance, instructions, starting_position, and per-subunit power/discipline/morale/morale_start/dr/stamina/stamina_max.
    Each subunit is built via Subunit.of_type, so a CANONICAL troop type (TROOP_TYPE_STATS:
    levy, light_infantry, heavy_infantry, cavalry, archers, crossbow, sling, artillery, knights_templar)
    draws its §B.2 Power/Discipline/Morale presets unless the spec overrides them. A non-canonical
    type (e.g. 'infantry') or an explicit override behaves exactly as before -> inherits the unit-level
    fallbacks below, so a spec list of non-canonical types with no overrides still reproduces a homogeneous
    unit. make_unit (single-subunit) is unchanged.
    [canonical: derived_stats architecture -- unit stats composed from subunits]"""
    # [ED-MB-0017, adversarial-review finding 2] Frontage-aware centred line for un-positioned subunits
    # (was `(10 + i*4, 15)` — same row-stagger-at-fixed-col defect that stacked subunits, the P-1 bug the
    # engine builders fixed). No live gauge row hits this branch (every multi-subunit gauge row below sets
    # explicit `starting_position`), so this closes the latent default without changing any gauge result.
    _start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    _auto_cols = _centered_line_cols(specs, 25)
    subs = []
    for i, sp in enumerate(specs):
        sp = dict(sp)
        pos = sp.pop('starting_position', (_start_row, _auto_cols[i]))
        tt = sp.pop('troop_type', 'infantry')
        # build typed subunits via Subunit.of_type so a canonical troop type draws its
        # §B.2 Power/Discipline/Morale presets (the taxonomy stat home, ED-1018). Only forward the
        # stat keys the caller explicitly set, so of_type's setdefault fills the rest from the preset;
        # a non-canonical type ('infantry') fills nothing and inherits the unit-level fallbacks exactly
        # as before. A caller-set stat still overrides the preset.
        kw = dict(unit_type=sp.pop('unit_type', 'melee'), stance=sp.pop('stance', stance),
                  instructions=sp.pop('instructions', ()))
        for k in ('power', 'discipline', 'morale', 'morale_start', 'dr', 'stamina', 'stamina_max'):
            if k in sp:
                kw[k] = sp.pop(k)
        subs.append(Subunit.of_type(tt, sp.pop('shape'), sp.pop('tier', 3), pos, **kw))
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=subs, dr=dr, stance=stance, speed=speed)


def make_unit(shape, tier, name, faction, unit_type='melee', power=4, command=4,   # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats P4/C4]
              discipline=5, morale=6, stance='balanced',                          # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats D5/M6]
              troop_type='infantry', speed='Standard', morale_start=None, instructions=(),
              troops=None, concentration=None):  # [ED-MB-0027] explicit density (default GAUGE_TROOPS/GAUGE_CONC) — honest-gauge matching
    # troop_type/speed default to the historical infantry baseline so the original
    # 13 tests construct byte-identically; cavalry rows pass troop_type='cavalry',
    # speed='Fast' by kwargs. Cavalry charge mechanics (charge_pen,
    # PC_CAVALRY_SPEED_MULT) are PER_CELL=1-gated in the engine; under PER_CELL=0
    # cavalry == infantry (S1: speed is not yet wired into combat).
    #
    # morale_start / instructions default to leave EVERY pre-existing row byte-exact
    # (morale_start=None -> morale_start==morale; instructions=() -> no brace).
    #   * instructions=('brace',) sets the engine's FM brace tactic on the subunit:
    #     _unit_braced(unit) then fires the grounded reciprocal charge-recoil
    #     (PC_CHARGE_RECOIL, calibrated vs Courtrai/Swiss/Waterloo) so a frontal
    #     charge into a prepared wall is REPELLED. Bracing is a deliberate tactic,
    #     NOT an automatic consequence of holding -> the gauge must set it to test
    #     a braced unit (the engine gating is correct game design).
    #   * morale_start>morale expresses a genuinely SHAKEN unit (cohesion eroded
    #     BELOW its start, du Picq): _charge_shock_sigma's shaken-amplifier
    #     (PC_SHOCK_SHAKEN_GAIN) and _morale_sigma then fire. "Shaken" is RELATIVE
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
    # build_army -> Subunit.of_type fills the canonical §B.2 troop-type PRESET (cavalry Power 5), silently
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
    return build_army([spec], name, faction, power=power, command=command,
                       discipline=discipline, morale=morale, morale_start=morale_start,
                       dr=1, stance=stance, speed=speed)


def _envelop_army(name, faction, tier=3, troop_type='infantry', speed='Standard', **kw):  # [canonical: sim_mb_06_v9_historical_spec.md — T3 (tier-3) baseline]
    """[LC-8, ED-909] Composed replacement for the retired Horseshoe shape: a held center + two
    wide-placed wings released into 'envelop' via a Stage C timed order -- ED-909's Unit-level
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
    # [2026-07-05 adversarial-review fix] `Subunit` has NO `speed` field at all -- a per-subunit
    # 'speed' key in these spec dicts is silently dropped by `build_army` (it never pops one), so it
    # was pure dead decoration. `Unit.speed` is the only real speed knob (checked whole-unit at
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
    a withheld/refused wing released only once directly threatened -- ED-909's Unit-level Refused
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
    # keys are dead (Subunit has no speed field); the real Unit.speed is forwarded below instead.
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
    ('H3','Envelopment vs Line',_envelop_army,'Line',{},{},55,72,'high'),             # [canonical: mass_battle_gauge_grounding.md §3 — H3 full envelopment]
    ('H4','Envelopment vs Arrowhead (Cannae)',_envelop_army,'Arrowhead',{},{},45,62,'high'),   # [canonical: mass_battle_gauge_grounding.md §3 — H4 Cannae proper]
    ('H5','RefusedFlank vs Envelopment',_refused_army,_envelop_army,{},{},48,62,'high'),       # [canonical: mass_battle_gauge_grounding.md §3 — H5 oblique counter]
    ('H6','RefusedFlank vs Line',_refused_army,'Line',{},{},48,60,'high'),                 # [canonical: mass_battle_gauge_grounding.md §3 — H6 oblique order]
    ('H7','GappedLine(manip) vs Line','GappedLine','Line',{},{},48,62,'high'),              # [canonical: mass_battle_gauge_grounding.md §3 — H7 manipular flex]
    ('H8','GappedLine vs Arrowhead','GappedLine','Arrowhead',{},{},50,65,'high'),           # [canonical: mass_battle_gauge_grounding.md §3 — H8 maniples absorb wedge]
    ('H9','Line vs Arrowhead (rev H2)','Line','Arrowhead',{},{},38,52,'high'),              # [canonical: mass_battle_gauge_grounding.md §3 — H9 inverse H2]
    ('H10','Line vs Envelopment (rev H3)','Line',_envelop_army,{},{},28,45,'high'),             # [canonical: mass_battle_gauge_grounding.md §3 — H10 inverse H3]
    ('H11','Arrowhead vs Envelopment (rev H4)','Arrowhead',_envelop_army,{},{},38,55,'high'),   # [canonical: mass_battle_gauge_grounding.md §3 — H11 symmetric H4]
    ('R1','Ranged vs Line (open field)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{},0,30,'low'),                             # [canonical: mass_battle_gauge_grounding.md §3 — R1 ranged loses open field]
    ('R3','Ranged vs Ranged (mirror)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{'unit_type':'ranged','stance':'hold'},42,58,'high'),  # [canonical: mass_battle_gauge_grounding.md §3 — R3 ranged mirror]
]

CAV = {'troop_type':'cavalry','speed':'Fast'}
CAV_TESTS = [
    # C1: frontal shock cavalry vs STEADY close-order but UNBRACED foot, open ground. CONTESTED,
    # NOT a cavalry win -- a horse will not charge a solid formation, and cavalry's decisive work
    # was against BROKEN or FLANKED foot (Burkholder 2007). [REBASELINE: the old band encoded the
    # popular cavalry-beats-unprepared-infantry misconception this source debunks.]
    ('C1','Cav vs steady unbraced Line','Arrowhead','Line',dict(CAV),{},35,55,'high'),     # [canonical: mass_battle_gauge_grounding.md §3 — C1 contested frontal, rebaseline]
    # C2: frontal cavalry vs a BRACED wall (hold + disc8 + the 'brace' tactic = square / schiltron /
    # pike block). The brace instruction fires the grounded reciprocal charge-recoil (PC_CHARGE_RECOIL,
    # calibrated vs Courtrai/Swiss/Waterloo): the wall REPELS the charge -- cavalry rarely breaks it.
    # Judged on RAW cavalry win-rate (must be LOW): a repelled charge is a HOLD, not a decisive result,
    # so decisive-split is uninformative here (tiny decisive n) and high draws are EXPECTED (Waterloo
    # squares held all day; cavalry could not charge a solid formation -- Burkholder 2007; Barua 2011).
    ('C2','Cav vs BRACED Line (hold+d8+brace)','Arrowhead','Line',dict(CAV),
        {'stance':'hold','discipline':8,'instructions':('brace',)},0,30,'high','rawA'),  # [canonical: mass_battle_gauge_grounding.md §3 — C2 braced repels; raw cav-a LOW]
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
    # (PC_SHOCK_SHAKEN_GAIN) + _morale_sigma fire: the wavering line breaks under the charge --
    # exploitation + pursuit. Decisive cavalry win; ceiling is NEAR-TOTAL rout: cavalry vs disordered
    # foot was catastrophic (Boddy 2015 dispersed 15,000 disordered French; Hastings post-feint). The
    # Phase-2 ceiling 90 was provisional (set when this row was inert/contested at 45.7); the working
    # shock + history put it near-total. draws scarce (decisive-split appropriate).
    ('C5','Cav vs SHAKEN Line (m2/start6)','Arrowhead','Line',dict(CAV),
        {'morale':2,'morale_start':6},65,98,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C5 exploits shaken; near-total ceiling]
    # C6: cavalry vs a BRACED-shallow line (hold + disc8 + 'brace') -- a faced brace still repels
    # frontally (the recoil needs discipline x some depth, not maximal depth). Control duplicate of C2
    # on a shallower wall; same RAW cav-a-LOW judgement, draws expected.
    ('C6','Cav vs BRACED-shallow Line (hold+d8+brace)','Arrowhead','Line',dict(CAV),
        {'stance':'hold','discipline':8,'instructions':('brace',)},0,30,'high','rawA'),  # [canonical: mass_battle_gauge_grounding.md §3 — C6 = C2; raw cav-a LOW]
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

def matchup(sa, sb, ka, kb, mode, n=60, seed_base=1_000_000):  # [Jordan directive 2026-07-01: n 120->60 for runtime; SE~sqrt(0.25/n) rises ~4.6pp->~6.5pp at p=0.5, vs the grounding doc's cited n=120/SE~5pp basis (mass_battle_gauge_grounding.md §1)]
    # sa/sb: a plain shape string (single-subunit, via make_unit) or an army-builder callable
    # (_envelop_army/_refused_army) for the composed Envelopment/Refused-Flank presets that replaced
    # the retired Horseshoe/RefusedFlank shapes (LC-8). resolve_battle's shape_a/shape_b positional
    # is only consulted by reset_positions as a defensive fallback now (every subunit resets to its
    # OWN spawn position first) -- 'Line' is a safe placeholder for a callable side.
    a_is_fn = callable(sa); b_is_fn = callable(sb)
    aw=bw=dr=0; turns=[]; a_cas=[]; b_cas=[]
    for s in range(n):
        random.seed(s+seed_base)
        ua = sa('A','A',**ka) if a_is_fn else make_unit(sa,3,'A','A',**ka)  # [canonical: sim_mb_06_v9_historical_spec.md — T3 (tier-3) units]
        ub = sb('B','B',**kb) if b_is_fn else make_unit(sb,3,'B','B',**kb)
        a0,b0 = ua.hp_max, ub.hp_max
        shape_a = 'Line' if a_is_fn else sa
        shape_b = 'Line' if b_is_fn else sb
        if mode=='single':
            r=resolve_battle(ua,ub,kind='single',max_turns=18); turns.append(r.get('turns',18))  # [canonical: mass_battle_gauge_grounding.md §1 — single-mode tick cap]
        else:
            r=resolve_battle(ua,ub,shape_a,shape_b,ANCHOR_MAP,kind='multi',max_battle_turns=20); turns.append(r.get('battle_turns',20))  # [canonical: mass_battle_gauge_grounding.md §1 — multi-mode battle-turn cap]
        w=winner_of(r)
        if w=='A':aw+=1
        elif w=='B':bw+=1
        else:dr+=1
        a_cas.append(100*(a0-ua.hp)/a0 if a0 else 0); b_cas.append(100*(b0-ub.hp)/b0 if b0 else 0)
    dec = aw+bw
    return dict(a=aw/n*100, b=bw/n*100, d=dr/n*100,
                decA=(100*aw/dec if dec else 50.0), dec_n=dec,  # [canonical: mass_battle_gauge_grounding.md §1 — even-split fallback when no decisive result]
                t=statistics.mean(turns), a_cas=statistics.mean(a_cas), b_cas=statistics.mean(b_cas))

def run(mode, tests=TESTS, n=60):  # [Jordan directive 2026-07-01: default sample n 120->60 for runtime — see matchup()]
    print(f"\n----- MODE: {mode}  (engine: mass_battle package)  metric: DECISIVE split A/(A+B); RAW A% for 'rawA' repel rows -----")
    print(f"  {'id':4} {'matchup':30} {'A%':>5} {'B%':>5} {'D%':>5} {'val':>5} {'band':>7} {'dexp':>4} {'m':>4} verdict")
    nb=0
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
    print(f"  => pass {nb}/{len(tests)}  (bands are HISTORY-grounded; a fail flags engine divergence, not a band to lower)")
    return nb

if __name__=='__main__':
    # Cavalry rows are PER_CELL=1-only (engine gates charge_pen + speed mult on PER_CELL). Read the
    # RESOLVED config value (mass_battle.config.PER_CELL), not a second, independently-defaulted
    # os.environ.get -- the latter drifted out of sync with config.PER_CELL's own default the moment
    # gate 4 (ED-MB-0001) flipped PER_CELL's default '0'->'1': a bare invocation now runs the engine
    # with PER_CELL=True, but a locally re-derived '0' fallback here would still silently exclude
    # CAV_TESTS, exactly the mode-key mismatch bat.py's compute() was fixed for at the same time.
    import mass_battle.config as _mb_cfg
    _pc = _mb_cfg.PER_CELL
    _tests = TESTS + (CAV_TESTS if _pc else [])
    s=run('single', _tests); m=run('multi', _tests)
    n=len(_tests)
    print(f"\n==== mass_battle package: single={s}/{n}  multi={m}/{n} (multi is the resolving mode) ====")
