# [canonical: mass_battle_v30.md §A.3 TroopCount/block_size, §A.4 morale triggers,
#  §A.7 battle turn structure, §A.12 rout/pursuit; params/mass_combat.md;
#  derived_stats architecture — TroopCount as granular health pool]
#
#   v12 note #4 — VOLLEY HP SCALING (superseded): v12 made one volley Size loss ceil(h_per_size/2) hp, an
#   admitted band-fit that moved R1 from 69% to 35%, into 30-50% band. ED-MB-0041 replaced that per-target
#   formula with the flat `config.VOLLEY_LETHALITY_SCALE` (3, its value at the gauge baseline); the Tier-3
#   debt carries over. Cited by `config.py` VOLLEY_LETHALITY_SCALE and `battle_loop.py`'s volley note.
#
#   G-3 CONTINUOUS EFFECTIVE SIZE — HP represents TroopCount at Company scale.
#   effective_size = hp / h_per_size (FLOAT, not floored to integer).
#   Pool formula uses continuous effective_size: a unit at 280/400 troops
#   fights at effective_size 2.8, not Size 2. Pool degrades continuously
#   as casualties mount, producing proportional combat degradation instead
#   of step-function drops at Size boundaries.
#   [canonical: mass_battle_v30.md §A.3/§A.4 — "TroopCount = Size × block_size",
#    "Size = floor(TroopCount / block_size)"; derived_stats architecture
#    from 2026-04-19 session — continuous TroopCount as granular health pool]
#
#   G-3 LETHALITY RECALIBRATION — damage scaled so 3-phase battles (18 ticks)
#   produce ~30% casualties on the losing side. Historical battles ended by
#   rout at 10-30% casualties; 30% chosen as gameplay-appropriate threshold
#   (enough fighting to feel consequential, army survives to fight again).
#   HP = TroopCount; damage = soldier casualties (no scaling).
#   Morale triggers fire on loss_pct (HP percentage) at 30%/50%.
#   [canonical: Jordan direction — "3-phase battles should be damaging, not
#    eliminating"; "30% rout threshold, not 10-15%"]
#
#   Cross-side cell contention (resolve_cross_side_contention). After both
#   sides advance, cells from opposing sides may end the phase at the same
#   absolute position (over-run).
#
#   Rule (per Jordan design 2026-05-12, full spec):
#     "if they were to occupy the same cell, then the troop with higher speed
#      gets priority for taking up that adjacent cell while the other remains
#      in place. if they have the same speed, then the troop with the greater
#      size gets that space. if they are the same size, then it's randomized."
#
#   Implementation (conservative subset):
#     - STRICT speed differential only: faster cell wins, loser cells that
#       moved this turn revert to pre-move snapshot.
#     - Tied speed → NO movement resolution (combat decides via engagement).
#     - Size and random tiebreakers DEFERRED until cavalry units exist: applying them per contested
#       position per turn produces battery noise in symmetric matchups without modelling anything
#       historical (equal infantry formations don't resolve by random; they resolve by combat).
#
#   Charge-through (cavalry past static infantry) and end-of-phase
#   displacement (opponent shifts back when overlapping with cavalry) are
#   noted in code but NOT WIRED — no cavalry in current battery.
#   Framework supports: _moved_this_turn tracking, _prev_offsets snapshot,
#   pre-existing cell_last_speed. Wiring requires power × facing inputs.

import math
from modules.mass_battle.troop_types import table as _troop_table   # `between_turn_recovery`'s `fatigue.lull_recover`
from engine.dice_engine import fmath
from engine.dice_engine.dice_engine import degree_label  # the one degree ladder (A-5); the field grades nothing of its own
from modules.mass_battle import rngsource  # single owner of engine randomness (see rngsource.py)

# [canonical: designs/provincial/mass_battle_v30.md §map — 25×25 grid, 5-cell buffer per side]
from modules.mass_battle.config import *  # P-A: constants extracted to mass_battle/config.py
from modules.mass_battle.core.exchange import *  # [Stage-1] pool primitives extracted to core.exchange
from modules.mass_battle.core.state import *  # [Stage-1] morale/discipline/rout transitions extracted to core.state
from modules.mass_battle.core.attrition import *  # [Stage-1] Lanchester attrition law extracted to core.attrition
from modules.mass_battle.core.contact import *  # [Stage-1] targeting/contact extracted to core.contact
from modules.mass_battle.core.contact_draw import resolve_melee_pair, pursuit_damage, REARGUARD_PENALTY, _momentum_speed  # B19.10 (ED-1043): the melee pair's resolution and the pursuit
from modules.mass_battle.core.volley import volley_phase, _roll_volley_pool, _atom_distance  # B19.10 (ED-1043): Phase 2 volley
from modules.mass_battle.troop_types.registry import *  # [Stage-1] troop-type stats/roles extracted
from modules.mass_battle.hierarchy.units import *  # [Stage-1] Unit/Army data model extracted
from modules.mass_battle.resolution import *  # [Stage-1] sigma head (roll/degree/morale-sigma/trace) — restored: import rode into hierarchy with the class block
# [canonical: designs/provincial/mass_battle_v30.md §units — 15×15 cell unit grid fits T4 pattern]
# [canonical: designs/provincial/mass_battle_v30.md §deployment]



# [canonical: mass_battle_v30.md §Scale — T1=100(1 size), T2=200(2), T3=400(4), T4=800(8), base 100]

# F-i: Cell support stacking [canonical: Jordan handoff §(1)]
# [canonical: Jordan handoff §(1) — depth-1: full, depth-2: 0.7, depth-3: 0.5, floor 0.3]

# F-ii: Puncture mechanism [canonical: Jordan handoff §(2)]

# F-iii: Cascading resolution [canonical: Jordan handoff §(3)]

# ─── PHASE / TICK STRUCTURE ────────────────────────────────────────────
# A "tick" is one resolution cycle (volley + advance + engagement). A "phase"
# is a block of TICKS_PER_PHASE ticks corresponding to one cavalry charge-and-
# return cycle (approach + gallop + impact + contact + disengage/reform).
# A pre-modern battle is then ~3-6 phases, matching the 30-90 minutes of
# active fighting found in hoplite, medieval, and early-modern accounts.
# [canonical: Jordan design — phase = gallop and charge cycle, ~5-6 ticks per
#  Operational Studies Group's "three-hex charge would take about 5 minutes",
#  with reform-to-position adding 1-2 ticks; hoplite phalanx fighting bounded
#  ~10-15 minutes by exhaustion before rotation/withdrawal]

# ─── TROOP COUNT / BLOCK SIZE (bottom-up lethality) ─────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.3 — "1 Size = block_size soldiers"]
# [canonical: derived_stats architecture (2026-04-19) — "TroopCount = Size × block_size"]
# HP = TroopCount = Size × BLOCK_SIZE. Damage from combat = soldier casualties.
# No LETHALITY_SCALE — casualty rates emerge from pool/TN/DR mechanics directly.
# At Company scale: Size 4 unit = 400 soldiers = 400 HP. Pool=8, ~3 successes/tick
# = ~3 soldiers killed/tick = 0.75%/tick = ~13% per 3-phase turn. Emergent.

# ─── MORALE EROSION (fully emergent) ───────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.4 morale triggers]
# Morale eroded by damage_taken / (discipline × command) each tick.
# NO thresholds. Rout point emerges from unit stats:
#   morale 6, damage ~3/tick, disc=5, cmd=4: erosion 3/20 = 0.15/tick
#   morale 6 → 0 in 40 ticks × 0.75%/tick = ~30% casualties to rout.
#   cmd=6: 45% to rout. cmd=2: 15%. Generalship dominance (T1) is structural.
# Morale is now float (accumulates fractional erosion). Rout at morale ≤ 0.
# No morale floor — general's contribution is in the denominator.
# [canonical: designs/provincial/mass_battle_v30.md §A.4 — "Generalship dominates"]

# G-2 rout-at-threshold constants (phase-boundary morale check for exhausted units)
# [canonical: mass_battle_v30.md §A.4 — morale floor = 1 while general present;
#  G-2 overrides this for exhausted+damaged units at phase boundary]
# [canonical: mass_battle_v30.md §A.4 — cap −3 per Cascade Phase for non-general morale loss]

# ─── DISCIPLINE DEGRADATION WITH CONTINUOUS EFFECTIVE_SIZE (D-6) ─────────
# [canonical: params/mass_combat.md §Discipline Degradation —
#  "Discipline degrades when Size lost > Discipline AND asymmetric"]
# Reinterpreted for continuous: check cumulative HP loss as fraction of
# h_per_size at each phase boundary. Fires when cumulative_loss in eff_size
# terms exceeds 1.0 AND loss is asymmetric. Each time it fires, threshold
# resets (so it can fire again after another 1.0 eff_size loss).
# [ASSUMPTION: threshold 1.0 eff_size maps to "Size lost > 1" in original]

# ─── PHASE-BOUNDARY HOOKS ───────────────────────────────────────────────────
# Called once per phase boundary. Order is canonical:
# discipline → morale → rout → rally → reform. (Stamina is the column ledger, `percell.update_stamina`, each tick.)
# v15 populates morale_check_phase, rout_resolution.
# rally_check and reform_check remain empty (future cycles).


def rally_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — rally lands in a future cycle (G-7)."""
    pass

# G-8 reform flag: `REFORM_CHECK_ENABLED` (EngineConfig; default ON).

def reform_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    # [canonical: mass_battle_v30.md §A.5; PP-241 — Reform Phase Discipline restoration:]
    #   an unengaged unit gains +1 Discipline; requires the general's Command to be at least
    #   one above the unit's current Discipline, and Command of at least two; a Command of one
    #   cannot restore (the Command-asymmetry rule).
    # [canonical: mass_battle_v30.md §A.7 Phase Reform — non-engaged units restore Discipline.]
    """G-8 Reform: an unengaged unit restores one step of Discipline toward its start,
    gated by the general's Command. Flag-gated (REFORM_CHECK_ENABLED, which defaults
    to True, so the check runs unless a variant EngineConfig turns it off). Canon Reform also recovers Morale and merges sub-units —
    not implemented here (separate, morale/lifecycle-touching).
    [ASSUMPTION: cadence — fires per phase-boundary, bounded by discipline_start so a unit
     only recovers what it lost. Canon Reform is once-per-turn (the Reform Phase); the sim's
     phase-boundary count varies with the turn cap, so per-boundary+cap is the conservative
     mapping pending a once-per-turn ruling.]
    """
    if not REFORM_CHECK_ENABLED:
        return
    if find_contacts(unit_a, unit_b):
        return  # any contact pair -> both units engaged (1v1) -> no reform this boundary
    for u in (unit_a, unit_b):
        if u.routed or u.disordered:
            continue
        # Command-asymmetry (PP-241 on the citation line above): one cannot restore;
        # restoration needs Command at least one above the (per-subunit) current Discipline.
        if u.command < 2:
            continue
        for atom in u.units:
            if atom.routed or atom.disordered:
                continue
            if u.command < atom.eff_discipline + 1:
                continue
            if atom.eff_discipline < atom.eff_discipline_start:
                atom.restore_discipline()   # +1 toward start, routes own-else-Army (byte-exact single-subunit)
        u.check_drift()


def phase_boundary(unit_a, unit_b, phase_idx):
    """Run the phase-boundary hook sequence in canonical order.
    Called every TICKS_PER_PHASE ticks within run_battle."""
    discipline_check_phase(unit_a, unit_b, phase_idx)
    morale_check_phase(unit_a, unit_b, phase_idx)
    rout_resolution(unit_a, unit_b, phase_idx)
    rally_check(unit_a, unit_b, phase_idx)
    reform_check(unit_a, unit_b, phase_idx)

# v9 Volley (Phase 2 ranged fire) [canonical: mass_battle_v30.md §A.7 Phase 2; PP-503]
# TN for Volley success rolls. Standard d10: TN 6 success rate ≈ 0.5/die.
# [canonical: mass_battle_v30.md §A.7 PP-503 — "TN 6 [PROVISIONAL]"]
# [canonical: mass_battle_v30.md §A.7 PP-503 — "Roll [Power stat] dice"]
# Volley pool = Power dice; not the engagement pool formula.
# Ranged DR table [canonical: params/mass_combat.md §Ranged DR Table — Volley Phase, PP-188]
# Keys: (armour_class) → DR vs Piercing. Sim default: Light armour (DR 1).
# Ranged_DR_None=0, Light=1, Medium=2, Heavy=3 (Piercing column).
# Default DR vs Piercing (ranged) applied to ALL volley targets. Medium-armoured
# infantry (typical Veteran/Professional tier) = DR 2 vs Piercing. Configurable via
# Atom.armour_class in future iterations.
# [canonical: params/mass_combat.md §Ranged DR Table — Medium vs Piercing = 2]
# [canonical: params/mass_combat.md §Ranged DR Table — default DR vs piercing 2]
# Minimum cell-distance for Volley targeting. Distance ≤ 1 = adjacent/melee contact;
# ranged units historically stop firing once enemy closes to hand-to-hand range.
# [canonical: mass_battle_v30.md §A.7 Phase 2 vs Phase 5 — Volley is pre-Engagement;
#  once contact made, units fight in melee not volley]
# Initial deployment is row 5 vs row 15 = 10 cells apart. Range 8 means ranged
# units must close 1-2 cells (or wait for enemy to approach) before volley begins.
# Historical longbow at Crécy/Agincourt: effective fire began ~100 paces (~5 cells)
# but harassment fire extended further. Range 8 captures both regimes.
# [canonical: references/historical/precedents_warfare.md — effective volleys at
#  100-200 paces; killing zone was the final approach to contact]

# [canonical: mass_battle_v30.md §ED-816 shape mods; -99 = structural sentinel (−∞ pool)]
# [canonical: v11 — gap=-99 removed for GappedLine. Gap effect is geometric:
#  no cells at the gap column means no engagement there. Per-cell angles handle
#  the flanking naturally. Structural sentinel only retained where cell is absent.]

# ─── CELL PATTERNS ───────────────────────────────────────────────────────────
# [canonical: mass_battle_v30.md §Shapes — per-tier cell grid dimensions, Jordan design]

from modules.mass_battle.geometry import *  # P-A stage 2: geometry extracted

# ─── ATOM ────────────────────────────────────────────────────────────────────

def _cascade_depth_key(pair):
    """Sub-phase ordering: foremost attacker resolves first.
    [canonical: Jordan handoff §(3) — tip arrives first]"""
    atom_a = pair["atom_a"]
    a_cells = pair["a_cells"]
    if not a_cells: return 999  # [canonical: sentinel: 999 = no-cells max distance]
    if atom_a.advance_dir == -1:
        return min(r for r, c in a_cells)
    return -max(r for r, c in a_cells)

# === SIGMA-LEVERAGE HEAD constants + helpers (prototype, sim-tunable) ===
# === GRADED MORALE / DAMPED ROUT (Jordan directive 2026-05-31: damp rout, more attrition; morale = inspiration not fact) ===

# Perception model (Jordan 2026-05-31; grounded in visual physiology + military scholarship):
#   human horizontal visual field ~190-210deg -> REAR BLIND ARC ~150deg, visible +/-105deg.
#   Pinning models the attentional lock of an engaged cell separately (fixing-force doctrine).
# Pocket / gap-trap (Polybius: maniple gaps "lured hoplites in... surrounded"; also the concave Cannae pocket):
# an enemy cell that penetrates LEVEL between two of our cells (attackers on both lateral sides, same rank) is
# surrounded -> not refusable. Mirror-safe: parallel lines put attackers AHEAD (a different rank), never beside
# on both flanks; only a penetration into a gap/concavity produces it.
# Oblique-offense ROLL-UP (Leuthen/Leuctra: a concentrated DEEP wing crushes a thinner enemy wing at the point of
# contact). At an in-contact pair, depth is measured PARALLEL to the contact vector for BOTH sides (Jordan's
# vectorized depth). If the attacker's local push-depth exceeds our supporting depth by more than a margin, that
# local superiority rolls the cell up. Fires ONLY where neither wrap nor pocket fired (no double-count) and only
# in contact (a recessed/refused cell that no one is yet in contact with is not rolled up -- this protects a
# deliberately thin Cannae centre). Mirror-safe: equal formations have equal depth, so excess <= 0 everywhere.
# A roll-up is a FLANK phenomenon: you concentrate a wing and roll the enemy line up FROM ITS END (Leuthen,
# Leuctra). The interior of a line is not directly rolled up -- its collapse is a downstream morale consequence.
# So the roll-up penalty bites only on cells at the defender's lateral extreme; a recessed/penetrated centre
# (e.g. a Cannae concave) is handled by the pocket, not the roll-up.
# A roll-up breaks a still-FORMED but out-massed wing (a deep wing rolling a thinner one by design); it must not
# mop up a cell already attrited to a single rank -- that cell is already losing on troop count, and penalising it
# again double-counts attrition. So the defender cell must retain real depth (>= floor) to be rollable.

from modules.mass_battle.percell import *  # P-A stage 3: percell extracted


def _cell_shares(pairs):
    """[the pair rule's edit 4, B19.12] One pass over a tick's pairs counting, per side, the pairs each contact cell is in; the count
    rides on the pair as `a_share` / `b_share` (`{abs cell: m}`), and `core.attrition.engaged_files` counts the cell at `1 / m` in each.
    So a cell adjacent to two enemy bodies lends half its men to each contact, and the same cells grouped into more bodies put the
    same men in the front (`16_PESSIMIST_MB_partition_and_the_pair_rule`: a force's result does not depend on how many bodies its
    cells are grouped into). It replaces the retired `_convergence_scale` and `pair_pool_contribution`'s share, and their "known
    accepted residual" (a cell in two pairs counted in full in both). Computed on the FULL tick by `resolve_engagements_cascading`, for
    the reason the face set is: a cascade sub-phase is not the tick."""
    count_a, count_b = {}, {}
    for p in pairs:
        for c in set(p["a_cells"]):
            k = (id(p["atom_a"]), c); count_a[k] = count_a.get(k, 0) + 1
        for c in set(p["b_cells"]):
            k = (id(p["atom_b"]), c); count_b[k] = count_b.get(k, 0) + 1
    for p in pairs:
        p["a_share"] = {c: count_a[(id(p["atom_a"]), c)] for c in set(p["a_cells"])}
        p["b_share"] = {c: count_b[(id(p["atom_b"]), c)] for c in set(p["b_cells"])}


def _compute_atom_sides(pairs):
    """The set of DISTINCT octagon FACES (F/B/L/R) each defender subunit is struck on this TICK, ONE face per
    contacting enemy body (its contact-cell centroid -> nearest defender face). Computed ONCE on the FULL
    tick's pairs (like the cell shares) and threaded into every cascade sub-phase's resolve_engagements, so the
    graded MULTI-SIDE SHOCK (2 sides x1.5, 3 x2.0) sees every face an enveloped body is struck on."""
    def _mean_facing(_atom):
        _fv = getattr(_atom, 'cell_facing_vec', None)
        if _fv:
            _rs = sum(v[0] for v in _fv.values()); _cs = sum(v[1] for v in _fv.values())
            if _rs or _cs:
                return (_rs, _cs)
        return (_atom.advance_dir, 0)
    def _nearest_face(_dcells, _dfac, _acen):
        _n = len(_dcells)
        _cr = sum(r for r, c in _dcells) / _n; _cc = sum(c for r, c in _dcells) / _n
        _fm = (_dfac[0] ** 2 + _dfac[1] ** 2) ** 0.5 or 1.0
        _fu = (_dfac[0] / _fm, _dfac[1] / _fm)
        _pu = (-_fu[1], _fu[0])
        _al = [(r - _cr) * _fu[0] + (c - _cc) * _fu[1] for r, c in _dcells]
        _pp = [(r - _cr) * _pu[0] + (c - _cc) * _pu[1] for r, c in _dcells]
        _faces = {
            'F': (_cr + max(_al) * _fu[0], _cc + max(_al) * _fu[1]),
            'B': (_cr + min(_al) * _fu[0], _cc + min(_al) * _fu[1]),
            'L': (_cr + max(_pp) * _pu[0], _cc + max(_pp) * _pu[1]),
            'R': (_cr + min(_pp) * _pu[0], _cc + min(_pp) * _pu[1]),
        }
        return min(_faces, key=lambda k: (_faces[k][0] - _acen[0]) ** 2 + (_faces[k][1] - _acen[1]) ** 2)
    sides = {}
    for _p in pairs:
        for _datom, _atk_cells in ((_p["atom_b"], _p["a_cells"]), (_p["atom_a"], _p["b_cells"])):
            _dcells = list(_datom.cells())
            _ac = list(set(_atk_cells))
            if not _dcells or not _ac:
                continue
            _acen = (sum(r for r, c in _ac) / len(_ac), sum(c for r, c in _ac) / len(_ac))
            _face = _nearest_face(_dcells, _mean_facing(_datom), _acen)
            sides.setdefault(id(_datom), set()).add(_face)
    return sides


def _merge_cell_damage(dst, src):
    """[ED-MB-0040] Merge one cascade sub-phase's per-cell damage into the tick's accumulator."""
    for k, (atom, cells) in src.items():
        slot = dst.get(k)
        if slot is None:
            dst[k] = (atom, dict(cells))
        else:
            acc = slot[1]
            for cell, d in cells.items():
                acc[cell] = acc.get(cell, 0.0) + d


def _expire_charger_latches(unit_a, unit_b, pairs):
    """[ED-MB-0041 Tier-2] Drop each atom's latched charger-role for opponents it is no longer touching.

    The latch (`atom._pressing`, set in resolve_engagements) holds "I charged this body" across the ticks
    after impact, because momentum is an impulse and the braced-wall repel must not expire with it. It has
    to be released when the bodies part, or a cavalry subunit that charged a pike wall, broke off, and
    later engaged a DIFFERENT wall would arrive already flagged as its charger.

    Computed from the FULL tick's pair list by resolve_engagements_cascading, for the same reason
    `_compute_front_fixers` is: a cascade sub-phase group is not the tick, and clearing from a partial
    view would expire latches for pairs that are still very much in contact.
    """
    live = {}
    for p in pairs:
        a, b = p["atom_a"], p["atom_b"]
        live.setdefault(id(a), set()).add(id(b))
        live.setdefault(id(b), set()).add(id(a))
    for u in (unit_a, unit_b):
        for atom in u.units:
            pressing = getattr(atom, '_pressing', None)
            if pressing:
                pressing &= live.get(id(atom), set())


def _compute_front_fixers(pairs):
    """[ED-MB-0041 Tier-2] THE single owner of the atomized fixing-force relation, computed on a
    pair list: {id(defender): {id(enemy) that is contacting its FRONT arc}}.

    A subunit engaged on its FRONT by an enemy body cannot wheel as a body to face a SEPARATE
    detachment on its flank/rear -- so that detachment's hit lands with the zone penalty (the
    envelopment of a fixed unit). "Fixed" is emergent from frontal contact and requires a DIFFERENT
    enemy subunit than the flanker, so it is impossible in any single-subunit clash. Centroid-based,
    per contacting pair.

    SCOPING: computed ONCE on the full tick by resolve_engagements_cascading and threaded in (a cascade
    sub-phase group is not the tick: a defender pinned frontally by a body in group 0 and flanked by a
    detachment in group 1 must see the fixer in group 1), the same treatment eng_counts/atom_sides get."""
    def _su_centroid(_su):
        _cs = _su.cells()
        return (sum(r for r, c in _cs) / len(_cs), sum(c for r, c in _cs) / len(_cs)) if _cs else None
    ff = {}
    for _p in pairs:
        for _d, _e in ((_p["atom_a"], _p["atom_b"]), (_p["atom_b"], _p["atom_a"])):
            _dc = _su_centroid(_d); _ec = _su_centroid(_e)
            if _dc is None or _ec is None:
                continue
            _fz0, _ = octagon_angle(_ec, _dc, (_d.advance_dir, 0))
            if _fz0 == "GREEN":
                ff.setdefault(id(_d), set()).add(id(_e))
    return ff


def resolve_engagements(unit_a, unit_b, pairs, t=None,
                        eng_counts=None, atom_sides=None, front_fixers=None):
    """Resolve all contact pairs.
    F-i: support from ranks behind reaches the draw as `support_a` (`exchange._pair_troops`).
    F-ii: puncture bonus from momentum differential.
    F-iii: per-cell facing comes from the subunit's LIVE `cell_facing_vec` (via get_cell_facing),
    read inside _octagon_cell_mods.
    t: current battle tick (None -> old instantaneous-brace behaviour; see resolution._brace_setup_ok),
    threaded to _charge_shock_sigma and the reciprocal-recoil _subunit_braced calls. [ED-1095]
    eng_counts/atom_sides: [B6] precomputed on the FULL tick by resolve_engagements_cascading and threaded
    in so the multi-side shock + encirclement penalty see the whole tick's engagement, not a cascade group;
    None -> computed locally from `pairs` (direct callers / non-cascading path -> identical, same pairs).
    B19.12 (MBA-04 step 2): each pair is resolved by the contact draw (`core/contact_draw.py::resolve_melee_pair`); there is no pool.
    A pair without `a_share`/`b_share` (a direct caller's) gets them from `_cell_shares` over `pairs`, as the cascade gives the full
    tick's."""
    if any("a_share" not in p for p in pairs):
        _cell_shares(pairs)
    dmg_a, dmg_b = 0, 0
    cell_dmg_a, cell_dmg_b = {}, {}   # [ED-MB-0040] {id(atom): (atom, {abs_cell: dmg})}, MB_CELL_DAMAGE only
    # [ED-MB-0075 option (2)] Army-level envelopment-shock flags, OR-accumulated over every pair this call
    # resolves (mirrors dmg_a/dmg_b's own per-pair accumulation, at the same Army granularity
    # cascade_morale_hit consumes). Set below in place of the old pre-combat delta-sigma penalty; consumed
    # by run_battle's per-tick loop (discipline-gated erosion) after damage commits, not here.
    shocked_a = shocked_b = False
    if eng_counts is None:
        eng_counts = count_engagements_per_atom(pairs)
    # MULTI-SIDE = the set of DISTINCT octagon SIDES a subunit is struck from, aggregated over its contact
    # pairs' real attacker-cell BEARINGS (front / left / right / rear, relative to the subunit's own facing),
    # not the arc-blind pair COUNT (`eng_counts`). Only computed under the octagon-damage flag (it drives
    # the graded multi-side shock in the damage block).
    # [B6] MULTI-SIDE = distinct FACES a subunit is struck on (see _compute_atom_sides). Threaded in from
    # the FULL tick by resolve_engagements_cascading; else computed here from `pairs` (identical when pairs
    # IS the full tick). Only under the octagon-damage flag (it gates the graded multi-side shock below).
    if atom_sides is not None:
        _atom_sides = atom_sides
    elif MB_OCTAGON_DMG:
        _atom_sides = _compute_atom_sides(pairs)
    else:
        _atom_sides = {}
    # A (atomized fixing-force, subunit-scale) -- see _compute_front_fixers for the mechanism and for
    # why it must be scoped to the FULL tick rather than a cascade sub-phase group. Threaded in by
    # resolve_engagements_cascading; a direct caller (tests / non-cascading path, where `pairs` already
    # IS the full tick) gets it computed here instead -- identical math either way.
    _front_fixers = _compute_front_fixers(pairs) if front_fixers is None else front_fixers
    for p in pairs:
        atom_a, atom_b = p["atom_a"], p["atom_b"]
        # Per-cell octagon angle — per-cell raw vectors, not centroid-to-centroid
        # [canonical: Jordan design — octagon, GREEN<45°, YELLOW 45-90°, RED≥90°]
        # For each contact cell-pair, compute angle using defender's per-cell facing vector.
        # Average the modifier across all contact cell-pairs per side.
        def _per_cell_angle_mod(defender_subunit, defender_cells, attacker_cells, attacker_subunit=None, fixed_by_other=False):
            if not defender_cells or not attacker_cells: return 0
            # Use attacker CENTROID rather than nearest-cell to avoid non-determinism
            # when a defender cell is equidistant between attacker cells (e.g. Arrowhead tip
            # embedded between two Line rows). [canonical: Jordan design]
            atk_cr = sum(r for r,c in attacker_cells) / len(attacker_cells)
            atk_cc = sum(c for r,c in attacker_cells) / len(attacker_cells)
            atk_centroid = (atk_cr, atk_cc)
            mods = []
            op = _oriented(defender_subunit)   # kept: frontage SPAN (_dc below) reads the static oriented pattern
            # abs->orig from the single live identity map (see _octagon_cell_mods): live _node_pos on the
            # field path; starting_position+cell_offsets on the grid path.
            abs_to_orig = _oriented_abs_map(defender_subunit)
            seen = set()
            _pc_refuse = PER_CELL and MB_REFUSE
            atk_sorted = sorted(set(attacker_cells)) if _pc_refuse else None
            if _pc_refuse:
                _dcols = [c for (_r, c) in defender_cells]
                _dmin, _dmax = min(_dcols), max(_dcols)
                # F1 structural: envelopers = attacker cells wrapped BEYOND the defender's frontage span
                # (past either flank). Mirror-stable BY CONSTRUCTION — equal-width formations produce NO
                # wrappers, so a frontal/mirror clash incurs no envelopment penalty regardless of integer-
                # movement stagger. Also fixes the enveloper self-flank (F2): the wider side's narrower
                # enemy cannot wrap it, so an enveloper is never penalised for its own inward-rotated facing.
                # F3 (mirror fix): only a NOMINALLY WIDER attacker can wrap. Width = column SPAN (extent)
                # of the static oriented pattern, symmetric under A<->B — a true mirror has equal span ->
                # NO wrappers regardless of dynamic drift (mirror == refuse-off). SPAN not distinct-count, so
                # a gapped formation (GappedLine) is correctly "wide" by its reach.
                _dc = [t[3] for t in op]; _def_front = max(_dc) - min(_dc) + 1
                if attacker_subunit is not None:
                    _op_atk = _oriented(attacker_subunit)
                    _ac = [t[3] for t in _op_atk]; _atk_front = max(_ac) - min(_ac) + 1
                else:
                    _atk_front = _def_front + 1
                if _atk_front > _def_front:
                    _wrappers = [a for a in atk_sorted if a[1] < _dmin or a[1] > _dmax]
                else:
                    _wrappers = []
                # full defender footprint, for vectorized depth resistance: reserves resist the wrap
                # measured along the WRAPPER'S approach vector, not the Y-column (Clausewitz reserves;
                # Jordan's geometric correction). Captured once per call.
                _def_cells = list(defender_subunit.cells())
                _atk_full = list(attacker_subunit.cells())   # full attacker footprint, for roll-up push-depth
            for d_pos in defender_cells:
                if d_pos in seen: continue
                seen.add(d_pos)
                orig = abs_to_orig.get(d_pos)
                facing = (defender_subunit.get_cell_facing(*orig)
                          if orig else (defender_subunit.advance_dir, 0))
                if _pc_refuse:
                    # Envelopment + refusal (fixing-force doctrine). A cell PINNED in front (attacker
                    # engaged adjacent in the front arc) cannot reorient; a flanker outside the cell's
                    # FOV cannot be seen. The cell REFUSES (turns to face -> no penalty) only if NOT
                    # pinned AND it can see the threat; otherwise the rear penalty lands. The threat is a
                    # STRUCTURAL wrapper (attacker beyond the defender frontage) in this cell's REAR.
                    pinned = False
                    for a in atk_sorted:
                        _z, _a = octagon_angle(a, d_pos, facing)
                        # (c) FOV blind arc GATES reaction: a threat in the rear blind arc cannot be perceived,
                        # so it cannot pin. Reuses FOV_HALF_DEG; no-op unless the facing model is enabled.
                        if MB_FACING_MODEL and MB_FACING_FOV_GATE and _a > FOV_HALF_DEG:
                            continue
                        if (((a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2) ** 0.5 <= MB_PIN_REACH
                                and _a < 45.0):  # [canonical: Jordan design — octagon zones; NOT in mass_battle_v30.md, which contains no octagon model (ED-MB-0041 verified: 0 occurrences)]
                            pinned = True; break
                    worst_mod = 0; worst_ang = 0.0; worst_pos = None
                    for a in _wrappers:
                        zone, ang = octagon_angle(a, d_pos, facing)
                        if zone == "RED" and MB_ENVELOP_MOD < worst_mod:
                            worst_mod = MB_ENVELOP_MOD; worst_ang = ang; worst_pos = a
                    if worst_mod < 0 and (not pinned) and worst_ang <= FOV_HALF_DEG:
                        worst_mod = 0   # refused: free to turn AND can see the threat
                    # A (atomized detached-flank / envelopment of a fixed unit): if no wider-line wrap
                    # fired, a cell whose SUBUNIT is fixed frontally by a separate body (fixed_by_other)
                    # with the attacker bearing on its flank/rear arc takes the zone penalty -- independent
                    # of attacker frontage-width. The detachment strikes the flank/rear of a fixed unit.
                    # [canonical: Cannae 216 BC; du Picq -- the unseen attack on a pinned line.]
                    if worst_mod == 0 and fixed_by_other and MB_FIXING_FLANK:
                        _fz, _fa = octagon_angle(atk_centroid, d_pos, facing)
                        if _fz in ("YELLOW", "RED") and ANGLE_DEF_MOD[_fz] < 0:
                            worst_mod = ANGLE_DEF_MOD[_fz]; worst_ang = _fa
                            worst_pos = min(attacker_cells,
                                            key=lambda a: (a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2)
                    if worst_mod < 0:
                        # depth resists the wrap, measured PARALLEL to the wrapper's approach (Jordan):
                        # a flank wrap is blunted by ROW depth, a rear wrap by FILE depth -- not the
                        # Y-column. A cell hit along X no longer draws spurious support from y-1.
                        _cd = _support_along_vector(d_pos, worst_pos, _def_cells)
                        worst_mod *= 1.0 / (1.0 + MB_ENVELOP_DEPTH_RESIST * max(0.0, _cd - 1.0))
                    # pocket / gap-trap: only where the WRAP did not already fire (worst_mod==0). The gap-
                    # flanking maniples sit WITHIN the defender's span (not wrappers), so a cell trapped level
                    # between them gets the pocket; a Horseshoe's concave wings are BEYOND the span (wrappers),
                    # so those cells take the depth-scaled wrap instead — no double-count. Enemy level on BOTH
                    # lateral sides; not refusable. Mirror-safe (parallel lines never put enemies beside on both).
                    if worst_mod == 0:
                        _hl = _hr = False
                        for a in atk_sorted:
                            if abs(a[0] - d_pos[0]) <= 0.5:
                                _dcol = a[1] - d_pos[1]
                                if -MB_POCKET_REACH <= _dcol < 0: _hl = True
                                elif 0 < _dcol <= MB_POCKET_REACH: _hr = True
                        if _hl and _hr:
                            worst_mod = MB_POCKET_MOD
                    # oblique-offense roll-up: fires only where neither wrap nor pocket fired, and the
                    # cell is actually in contact. Depth is measured PARALLEL to the contact vector for
                    # both sides (Jordan); if the nearest attacker's local push-depth out-masses our
                    # supporting depth past the margin, the local concentration rolls the cell up
                    # (Leuthen deep wing vs thin wing). A recessed/refused cell with no attacker in
                    # contact is NOT rolled up -- protects a deliberately thin Cannae centre.
                    if worst_mod == 0:
                        _cols = [c for (_r, c) in _def_cells]
                        _cmn = min(_cols); _cmx = max(_cols)
                        _is_wing = ((d_pos[1] - _cmn) <= MB_ROLLUP_FLANK_REACH
                                    or (_cmx - d_pos[1]) <= MB_ROLLUP_FLANK_REACH)
                        _na = None; _nd = 1e9
                        if _is_wing:
                            for a in atk_sorted:
                                _dd = ((a[0] - d_pos[0]) ** 2 + (a[1] - d_pos[1]) ** 2) ** 0.5
                                if _dd < _nd:
                                    _nd = _dd; _na = a
                        if _na is not None and _nd <= MB_ROLLUP_REACH:
                            _ds = _support_along_vector(d_pos, _na, _def_cells)
                            _ap = _support_along_vector(_na, d_pos, _atk_full)
                            _excess = _ap - _ds
                            if _excess > MB_ROLLUP_MARGIN and _ds >= MB_ROLLUP_MIN_DEPTH:
                                worst_mod = max(MB_ROLLUP_CAP,
                                                -MB_ROLLUP_PER_RANK * (_excess - MB_ROLLUP_MARGIN))
                    mods.append(worst_mod)
                else:
                    zone, _ = octagon_angle(atk_centroid, d_pos, facing)
                    mods.append(ANGLE_DEF_MOD[zone])
            return sum(mods) / len(mods) if mods else 0

        # [ED-MB-0018, Jordan 2026-07-22] The OCTAGON = a DAMAGE-RECEIVED MULTIPLIER, not a dice penalty.
        # This computes the pure per-cell FACING ARC that feeds that multiplier -- SEPARATE from
        # `_per_cell_angle_mod` above (which bundles the wrapper/pocket/roll-up tactical POOL penalties of
        # the legacy paradigm Jordan is replacing). Three Jordan requirements are modelled here:
        #   (1) arc = damage multiplier: front GREEN 0, flank YELLOW -1, rear RED -2 -> mult 1.0/1.5/2.0.
        #   (2) reaction is NOT instantaneous: a cell hit outside its front arc keeps its EXPOSED facing
        #       (penalty stands) until it has had FACING_REACTION_TICKS to wheel -- and only if it can SEE
        #       the threat (within FOV) and is not pinned frontally. A REAR strike (in the blind arc) is
        #       never seen -> the cell never turns -> the 2x lands for the whole engagement (the surprise
        #       rear attack). The per-cell reaction clock persists on the subunit across ticks.
        #   (3) multi-side compounding is applied by the CALLER (eng_counts>=2 -> *(1+MULTI_SIDE_SHOCK)):
        #       orderly rank-relief collapses when hit from >=2 sides -- worse than a mere halving.
        # Uses the LOCAL attacker centroid (attacker cells within OCTAGON_LOCAL_REACH of each defender
        # cell; global fallback) so a wing cell of a WIDE line in a head-on clash stays GREEN instead of
        # reading the whole enemy line's centre as an oblique (flank) bearing -- verified front->1.00x,
        # rear->2.00x exactly. [canonical: Jordan design -- octagon damage multiplier; du Picq flank/rear
        # lethality + reaction time under surprise]
        def _octagon_cell_mods(defender_subunit, defender_cells, attacker_cells):
            """[ED-MB-0040] THE single owner of the per-cell octagon arc (Jordan: "each cell has its own
            octagon facing"). Returns {abs_cell: arc_mod} — 0 (GREEN/front) .. -2 (RED/rear) per ANGLE_DEF_MOD,
            each cell judged against ITS OWN facing, its own local attacker centroid, its own pin/FOV state and
            its own reaction clock. The subunit scalar (`a_arc`/`b_arc` at the call site) is the troop-blind
            MEAN of this map; MB_CELL_DAMAGE reads the map itself so casualties land on the cells that are actually
            exposed instead of being averaged into one subunit scalar and smeared back uniformly."""
            if not defender_cells or not attacker_cells:
                return {}
            atk = list(set(attacker_cells))
            # abs->orig from the single live identity map. On the field/node path movement lives in
            # _node_pos (cell_offsets is not updated there), so the spawn lattice would not overlap the
            # unit's live cells and every cell would fall back to nominal (advance_dir,0) facing.
            # _oriented_abs_map keys off _node_pos on the field path and off the starting_position+
            # cell_offsets build on the grid path.
            abs_to_orig = _oriented_abs_map(defender_subunit)
            _rs = getattr(defender_subunit, '_react_since', None)
            if _rs is None:
                _rs = {}; defender_subunit._react_since = _rs
            mods = {}
            seen = set()
            for d_pos in defender_cells:
                if d_pos in seen:
                    continue
                seen.add(d_pos)
                orig = abs_to_orig.get(d_pos)
                facing = (defender_subunit.get_cell_facing(*orig)
                          if orig else (defender_subunit.advance_dir, 0))
                near = [a for a in atk
                        if (a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2 <= OCTAGON_LOCAL_REACH ** 2]
                if not near:
                    near = atk
                lc = (sum(r for r, c in near) / len(near), sum(c for r, c in near) / len(near))
                zone, ang = octagon_angle(lc, d_pos, facing)
                m = ANGLE_DEF_MOD[zone]
                _rk = orig if orig else d_pos
                _clear = True   # clear this cell's reaction clock unless it is actively counting toward a wheel
                if m < 0:
                    # frontally pinned? an attacker in the front arc within reach holds the cell so it
                    # cannot wheel to face the flank/rear threat (the fixing-force half of envelopment).
                    pinned = False
                    for a in atk:
                        _z2, _a2 = octagon_angle(a, d_pos, facing)
                        # [canonical: Jordan design — octagon zones; NOT in mass_battle_v30.md, which contains no octagon model (ED-MB-0041 verified: 0 occurrences)]
                        if (_a2 < 45.0
                                and (a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2 <= MB_PIN_REACH ** 2):
                            pinned = True; break
                    can_react = (ang <= FOV_HALF_DEG) and (not pinned)   # must SEE it AND be free to turn
                    if can_react:
                        if FACING_REACTION_TICKS <= 0:
                            m = 0                       # reaction delay disabled -> instant face
                        elif t is None:
                            pass                        # [ED-MB-0018 fix, arc-critic A4] no tick context -> cannot
                            #                             time the wheel -> penalty STANDS (was: instant-face footgun
                            #                             that silently zeroed every flank/side penalty on a t=None call)
                        else:
                            # [ED-MB-0018 fix, reaction-critic R1/R2] Frame-INDEPENDENT consecutive-tick counter,
                            # idempotent within a tick. Stored as (last_tick, count): survives run_battle's per-turn
                            # `t` restart (a continuous multi-turn flank keeps accumulating -- no absolute-tick
                            # arithmetic, which previously left a cell "stuck" penalized when t reset below its
                            # stamp), and a cell struck in >=2 pairs in ONE tick advances the counter ONCE (same
                            # `t` -> no double-count, which previously made a 2-sided cell's wheel order-dependent).
                            # The clock is RESET at engagement boundaries (reset_positions / reset_morale_between_
                            # battles) so it never leaks a stale stamp into a later, asymmetric re-engagement.
                            _prev = _rs.get(_rk)
                            if _prev is None or _prev[0] != t:
                                _cnt = (0 if _prev is None else _prev[1]) + 1
                                _rs[_rk] = (t, _cnt)
                            else:
                                _cnt = _prev[1]
                            _clear = False              # actively counting toward the wheel -> keep the clock
                            if _cnt >= FACING_REACTION_TICKS:
                                m = 0                   # reaction window elapsed -> wheeled to face -> penalty drops
                    # else (rear/blind or pinned): never wheels -> full penalty persists; clock cleared below
                if _clear:
                    _rs.pop(_rk, None)   # faced/green, rear/blind/pinned, or no-tick -> not counting -> reset clock
                mods[d_pos] = m
            return mods

        a_fixed_other = bool(_front_fixers.get(id(atom_a), set()) - {id(atom_b)})
        b_fixed_other = bool(_front_fixers.get(id(atom_b), set()) - {id(atom_a)})
        a_angle_mod = _per_cell_angle_mod(atom_a, list(set(p["a_cells"])),
                                           list(set(p["b_cells"])), atom_b, a_fixed_other)
        b_angle_mod = _per_cell_angle_mod(atom_b, list(set(p["b_cells"])),
                                           list(set(p["a_cells"])), atom_a, b_fixed_other)
        _pair_a, _pair_b, _sh_a, _sh_b = resolve_melee_pair(
            p, atom_a, atom_b, unit_a, unit_b, a_angle_mod, b_angle_mod, a_fixed_other, b_fixed_other, eng_counts, _atom_sides,
            _octagon_cell_mods, cell_dmg_a, cell_dmg_b, t)
        dmg_a += _pair_a
        dmg_b += _pair_b
        if _sh_a: shocked_a = True
        if _sh_b: shocked_b = True
    return {"dmg_a": dmg_a, "dmg_b": dmg_b, "engagements": len(pairs),
            "cell_dmg_a": cell_dmg_a, "cell_dmg_b": cell_dmg_b,
            "shocked_a": shocked_a, "shocked_b": shocked_b}

def resolve_engagements_cascading(unit_a, unit_b, pairs, t=None):
    """F-iii: cascading sub-phase resolution with facing rotation.
    [canonical: Jordan handoff §(3)]

    Contacts sorted by attacker depth (tip first). Each sub-phase resolves
    one depth group, then rotates engaged cells' facings toward their attacker.
    Later sub-phases see FLANK/REAR angles on already-rotated cells.
    Effect requires tight formation (TIP_SUPPORT_GAP=1 or 2) so multiple
    Arrowhead rows are simultaneously adjacent to Line cells.
    t: current battle tick, threaded to resolve_engagements for the brace-setup-delay gate. [ED-1095]"""
    # [the pair rule's edit 4, B19.12] Count, per side, the pairs each contact cell is in ONCE on the FULL tick's pairs, before any
    # cascading sub-phase split below: a cell in a pair of an early sub-phase and a pair of a later one is in two pairs this tick.
    _cell_shares(pairs)
    # Compute the multi-side face set AND the per-atom engagement count ONCE on the FULL tick's pairs (exactly
    # as the cell shares are), then thread them into every sub-phase's resolve_engagements: a depth-group split
    # would feed each sub-call only its group's pairs, so an encircled body would show 1 face / 1 engagement
    # per call and the multi-side shock + encirclement penalty would never fire.
    full_sides = _compute_atom_sides(pairs) if MB_OCTAGON_DMG else {}
    full_eng = count_engagements_per_atom(pairs)
    full_fixers = _compute_front_fixers(pairs)   # [ED-MB-0041 Tier-2] full-tick scope, not per-group
    _expire_charger_latches(unit_a, unit_b, pairs)   # [ED-MB-0041 Tier-2] see the latch note in resolve_engagements
    if not CASCADING_ENABLED:
        return resolve_engagements(unit_a, unit_b, pairs, t=t,
                                   eng_counts=full_eng, atom_sides=full_sides,
                                   front_fixers=full_fixers)

    total_dmg_a = total_dmg_b = 0
    total_cell_a, total_cell_b = {}, {}   # [ED-MB-0040] per-cell damage merged across sub-phases
    # [ED-MB-0075 option (2)] OR-accumulated across every sub-phase — a unit flagged shocked in ANY
    # sub-phase this tick stays shocked for the tick, mirroring total_dmg_a/total_dmg_b's own summing.
    shocked_a_any = shocked_b_any = False
    resolved_keys = set()

    # Sort by attacker depth; group into sub-phases by proximity (1-row buckets)
    sorted_pairs = sorted(pairs, key=_cascade_depth_key)
    if not sorted_pairs:
        return {"dmg_a": 0, "dmg_b": 0, "engagements": 0, "cell_dmg_a": {}, "cell_dmg_b": {},
                "truncated_groups": 0, "truncated_pairs": 0, "truncated_troops": 0.0,
                "n_groups": 0, "shocked_a": False, "shocked_b": False}

    groups = []
    cur_group = [sorted_pairs[0]]
    cur_depth = _cascade_depth_key(sorted_pairs[0])
    for p in sorted_pairs[1:]:
        d = _cascade_depth_key(p)
        if abs(d - cur_depth) <= 1:
            cur_group.append(p)
        else:
            groups.append(cur_group)
            cur_group = [p]
            cur_depth = d
    groups.append(cur_group)

    total_engagements = 0
    # [ED-MB-0048 / plan-v2 A3] Engagement groups past MAX_SUB_PHASES deal zero damage that tick; the
    # truncation is recorded in the result dict (`truncated_*`) so it is visible without a bespoke probe.
    # Truncation drops the DEEPEST-sorted groups (`sorted_pairs` is ordered by `_cascade_depth_key`, tip
    # first), so its bias is systematic against deep formations; engaged-troop WEIGHT (from
    # `_pair_engaged_troops`, the single owner of "troops actually in contact plus depth-weighted support")
    # expresses that where a count of ticks-that-truncated cannot. No RNG draws, no writes to engine state.
    # `n_groups` is the control: carried against the bound MAX_SUB_PHASES it turns "0 truncations" into a
    # headroom reading. MAX_SUB_PHASES itself is CALIBRATED-DEBT (config.py:106).
    truncated_groups = 0
    truncated_pairs = 0
    truncated_troops = 0.0
    n_groups = len(groups)
    for sub_idx, group in enumerate(groups):
        if sub_idx >= MAX_SUB_PHASES:
            for _dropped in groups[sub_idx:]:
                truncated_groups += 1
                for _p in _dropped:
                    # Same already-resolved filter the live path applies, so a pair that a
                    # previous sub-phase already resolved is not double-counted as "dropped".
                    if (id(_p["atom_a"]), id(_p["atom_b"])) in resolved_keys:
                        continue
                    truncated_pairs += 1
                    truncated_troops += (_pair_engaged_troops(_p["atom_a"], _p["a_cells"])
                                         + _pair_engaged_troops(_p["atom_b"], _p["b_cells"]))
            break
        active = [p for p in group
                  if (id(p["atom_a"]), id(p["atom_b"])) not in resolved_keys]
        if not active:
            continue
        result = resolve_engagements(unit_a, unit_b, active, t=t,
                                     eng_counts=full_eng, atom_sides=full_sides,
                                     front_fixers=full_fixers)
        total_dmg_a += result["dmg_a"]
        total_dmg_b += result["dmg_b"]
        total_engagements += result["engagements"]
        shocked_a_any = shocked_a_any or result.get("shocked_a", False)
        shocked_b_any = shocked_b_any or result.get("shocked_b", False)
        if MB_CELL_DAMAGE:   # [ED-MB-0040] accumulate this sub-phase's cellular placement
            _merge_cell_damage(total_cell_a, result.get("cell_dmg_a", {}))
            _merge_cell_damage(total_cell_b, result.get("cell_dmg_b", {}))
        for p in active:
            resolved_keys.add((id(p["atom_a"]), id(p["atom_b"])))
            # Engaged cells turn toward their opponents via the live `cell_facing_vec` slew in _node_advance
            # (MB_FACING_ATTENTION), which is what the octagon reads.

    return {"dmg_a": total_dmg_a, "dmg_b": total_dmg_b, "engagements": total_engagements,
            "cell_dmg_a": total_cell_a, "cell_dmg_b": total_cell_b,
            "truncated_groups": truncated_groups, "truncated_pairs": truncated_pairs,
            "truncated_troops": truncated_troops, "n_groups": n_groups,
            "shocked_a": shocked_a_any, "shocked_b": shocked_b_any}

# ─── VOLLEY (Phase 2 — ranged fire at distance): `core/volley.py`, imported above (B19.10) ──

# ─── WORKBENCH TRACE SNAPSHOTS (read-only; gated by tracing_on(), zero cost when tracing is off) ──
# [tick-by-tick visualizer, Jordan directive 2026-07-01] Extends the existing observe-only trace seam
# (resolution.tracing()/trace_event, a scoped buffer) with a spatial 'positions' event per tick. Uses
# atom.cells() (NOT iter_cells(), which reads legacy cell_offsets unconditionally and is NOT
# field-aware) zipped against _oriented(atom)'s stable (orig_r,orig_c) ids — both iterate in the
# SAME order (cells()/_node_cells() are themselves built by iterating _oriented(self)), so this is a
# correct pairing on BOTH the integer-grid and coordinate-field paths. Callers gate on tracing_on()
# so this construction (and its cost) is skipped entirely for every normal battle run.
def _cell_snapshot(atom):
    ids = [(o_r, o_c) for o_r, o_c, _, _ in _oriented(atom)]
    cells = []
    for cid, pos in zip(ids, atom.cells()):
        fr, fc = atom.get_cell_facing(*cid)
        cells.append({'id': list(cid), 'pos': [pos[0], pos[1]],
                       'troops': round(atom.cell_troops.get(cid, 0.0), 1),
                       'facing': [fr, fc], 'halted': cid in atom.halted_cells})
    return cells

def _subunit_snapshot(atom):
    return {'shape': atom.shape, 'troop_type': atom.troop_type, 'unit_type': atom.unit_type,
            'role': atom.role, 'instructions': list(atom.instructions),
            'routed': atom.routed, 'broken': atom.disordered, 'stance': atom.stance,
            'cells': _cell_snapshot(atom)}

def _unit_snapshot(unit):
    return {'name': unit.name, 'faction': unit.faction,
            'hp': round(unit.hp, 1), 'hp_max': unit.hp_max,
            'morale': unit.morale, 'discipline': unit.discipline, 'stance': unit.stance,
            'routed': unit.routed, 'broken': unit.disordered,
            'subunits': [_subunit_snapshot(a) for a in unit.units]}


# ─── BATTLE ──────────────────────────────────────────────────────────────────

def _draw_friction(unit):
    """[ED-MB-0016, DG-6 resolution] Draw `unit`'s per-battle combat-effectiveness friction factor ONCE.
    Idempotent within a battle: a fresh unit has no `_friction`; once set it is never redrawn (so a
    multi-turn battle's repeated run_battle entries keep the single per-battle draw). M ~ LogNormal(0,
    MB_FRICTION_SIGMA^2) via exp(normal) on the keyed `Draw`. MB_FRICTION off -> 1.0
    (default-inert, byte-exact). See config.py MB_FRICTION for the full grounding."""
    if getattr(unit, '_friction', None) is not None:
        return
    if MB_FRICTION and MB_FRICTION_SIGMA > 0.0:
        unit._friction = fmath.exp(rngsource.get().normal(0.0, MB_FRICTION_SIGMA))
    else:
        unit._friction = 1.0


# ─── [ED-MB-0052 / plan-v2 §5 C1] PER-PHASE CASUALTY ATTRIBUTION ─────────────
# Every hp loss is tagged with WHERE it came from and WHEN. This is load-bearing, not decoration:
# it is the only way to measure §0's inverted causal shape — the engine kills the loser and THEN
# breaks him, where history breaks him and then kills him — and the only way to check that a change
# advertised as a no-op (A2's sigma snap, B1c's re-key) really is one, per source rather than in aggregate.
#
# BINDING RULES for anything on this seam, and each one is checked rather than promised:
#   * ZERO RNG draws and NO float writes to engine state. This function reads two numbers the caller
#     already has and appends a dict. It cannot perturb what it observes.
#   * `trace_event` is a no-op when tracing is off, so with tracing off the engine is byte-identical.
#   * INSTRUMENTING MUST NEVER RESTRUCTURE THE INSTRUMENTED. The damage sites keep their existing
#     arithmetic and ordering exactly; attribution is observed AROUND each assignment (before/after),
#     never by routing the assignment through a new owner, which would change float ordering.
#
# `delta` is the ACTUAL hp movement including the `max(0, …)` clamp, not the nominal damage — the
# two differ on the killing blow, and conservation must be stated in the quantity that actually
# moved or it fails on every battle that ends in annihilation.
def attribute_hp_loss(unit, before, after, source, t=None, phase=None):
    """Record one attributed hp loss. Pure observation; no-op when tracing is off."""
    if not tracing_on():
        return
    delta = before - after
    if delta == 0:
        return
    trace_event('casualty', unit=getattr(unit, 'name', '?'),
                faction=getattr(unit, 'faction', '?'),
                source=source, t=t, phase=phase,
                before=before, after=after, delta=delta)


def _is_moving_atom(atom):
    """An atom is included in this tick's advance_cells pass if it has a target, is actively screening as an
    unengaged escort, OR is marching an unfinished route.

    The route case is gated on the node path being active (`hasattr(atom, '_node_anchor')`): on the
    legacy-lattice arm (MB_NODE_COHESION=0) advance_cells' per-cell loop has no route steering and would
    march a route-only atom full-speed along advance_dir forever. On the node path, _resolve_route_goal
    (via _resolve_maneuver_goal <- _node_advance) consumes the route as a real steering goal.

    A single named predicate so the gate lives once and a unit test can call it directly."""
    return bool(atom.target_atom or (atom.escort_of is not None and not atom._escort_engaged)
                or (atom._route_idx < len(atom.route) and hasattr(atom, '_node_anchor')))


from modules.mass_battle.battle_loop import run_battle  # the name is re-exported here

# ─── BETWEEN-TURN CONSTANTS (D-1, D-9) ──────────────────────────────────────
# The multi-turn loops that read these live in systems/mass_battle/sim/multi.py (workbench code), which reads
# them from this namespace at call time; nothing in the season path reads them.
# [canonical: Jordan direction — "we have a bunch of turns throughout the mass
#  battle system. 5 turns in a row attacking. limit of 3 phases per engagement"]

# Between-turn recovery rules (D-9):
# [ASSUMPTION: between-turn recovery constants are tuning parameters —
#  basis: no canonical source specifies inter-turn recovery rates]
# [canonical: params/mass_combat.md §PP-712 — "Discipline persists between battles"]
# (the stamina a lull returns is `fatigue.lull_recover` in `references/troops.yaml`, read by `between_turn_recovery` below)
BETWEEN_TURN_MORALE_RECOVERY = 0    # morale does NOT recover between turns
# HP does NOT recover between turns (casualties are permanent within a battle)
# Discipline persists (canonical PP-712)
# [canonical: designs/provincial/mass_battle_v30.md §A.4 — "Morale reset between battles"]


def between_turn_recovery(unit):
    """Apply between-turn state changes: THE LULL'S RECOVERY (B19.22), the one owner. `massbattle._run_and_grade` calls it on each army
    between two bouts of a field; `systems/mass_battle/sim/multi.py` (the workbench's multi-turn loop) re-exports it, so the oracle
    and the game run one rule (it lived there until B19.22, which `modules/` cannot import). Rested columns regain
    `fatigue.lull_recover` of stamina (`references/troops.yaml`); volleys are resupplied; morale recovers by
    `BETWEEN_TURN_MORALE_RECOVERY` (0 shipped); a yielding body that has rallied returns to the line. A routed or disordered body
    recovers nothing. Troops are never restored (casualties are permanent within a battle).
    [canonical: params/mass_combat.md §PP-712 — discipline persists]"""
    if unit.routed or unit.disordered:
        return
    for b in (unit.col_grid or ()):   # the one stamina ledger (`_ColBlock.stamina`); None on the PER_CELL-off arm
        b.stamina = min(float(STAMINA_MAX), b.stamina + _troop_table.fatigue()['lull_recover'])
    for atom in unit.units:
        # [A6, ED-MB-0067 Part A] Resupply at the between-turn lull. Per-subunit (Unit.resupply_volleys,
        # capped at MB_VOLLEYS_START): not singled out by troop type (a melee atom's volleys count is simply never read -- see fire()'s own
        # unit_type=='ranged' gate).
        if MB_AMMO_ENABLED:
            atom.resupply_volleys(MB_VOLLEYS_RESUPPLY)
    # [ED-MB-0042 sweep] Deliberately a BARE write, not unit.set_morale. Recovery is a bounded INCREMENT,
    # not an absolute statement about the body — and once cells own the state this pool is STALE (erosion
    # goes to the cells and never updates it), so broadcasting it downward would RE-INFLATE damaged cells
    # to the pool's old value. The pool is kept current here for the unseeded path, which still reads it.
    unit.morale = min(unit.morale_start, unit.morale + BETWEEN_TURN_MORALE_RECOVERY)
    for atom in unit.units:        # per-subunit Morale recovery (own-Morale units; inert at RECOVERY=0)
        # [ED-MB-0058, resolving ED-MB-0046] ONE owner, both ownership kinds: `pull_morale`, the RELATIVE
        # owner. Recovery is a bounded INCREMENT, so it must not go through `set_morale` (the ABSOLUTE writer,
        # which sets EVERY cell to one value and would flatten per-cell morale divergence to the mean at every
        # turn boundary). `pull_morale` caps against `eff_morale_start`, derives ONE shift from the aggregate
        # and applies that same shift to every cell, so the body recovers by the right amount and the divergence
        # between its cells survives. Unseeded it reduces to `min(eff_morale_start, eff_morale + R)` written to
        # the scalar.
        #
        # The `or atom.cell_morale` keeps an inheriting-but-cellular body in scope; a body that is NEITHER stays
        # out of it — the unit-pool line above is that body's recovery, and calling `pull_morale` for it would
        # write the unit pool once per subunit and compound the increment.
        if atom.morale is not None or atom.cell_morale:
            atom.pull_morale(BETWEEN_TURN_MORALE_RECOVERY)
    # [ED-MB-0024, DG-2 §2.4 RALLY exit] The between-turn boundary IS the lull (units have disengaged for
    # the turn break -> no active engaged pair). A yielding subunit whose morale has recovered above
    # YIELD_RALLY_MORALE_FRAC of its start reverts to normal combat/stance ("gave ground, pressure
    # relieved, reformed"). Gated OFF -> inert. `pocketed` is cleared alongside (fresh next engagement).
    if MB_YIELD_RALLY:
        for atom in unit.units:
            if atom.yielding and not atom.routed and not atom.disordered:
                if atom.eff_morale >= YIELD_RALLY_MORALE_FRAC * atom.eff_morale_start:
                    atom.yielding = False
                    atom.pocketed = False


# ─── PURSUIT (G-11) ─────────────────────────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.12-514]
# "Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
#  Offence successes (no Defence) each turn. Recall: Command Ob 2."
# "Routing: Slow/Standard cannot fight back. Fast may rearguard at −2D Off."
# (`pursuit_damage` and `REARGUARD_PENALTY` live in `core/contact_draw.py`, imported above, B19.10)
RECALL_OB = 2  # [canonical: §A.12 — "Recall: Command Ob 2"]




def recall_check(pursuer):
    """General attempts to recall pursuing unit. Command Ob 2.
    Returns True if recalled (pursuit stops).
    [canonical: designs/provincial/mass_battle_v30.md §A.12]"""
    net = roll_pool(pursuer.command)
    trace_event('draw', tick=None, side=getattr(pursuer, 'faction', '?'), unit=getattr(pursuer, 'name', '?'), kind='recall', band=degree_label(net, RECALL_OB))
    return net >= RECALL_OB


def feigned_retreat_recognized(pursuer):
    """Pursuing-side general rolls Command d10s vs Ob 2 to RECOGNISE a Feigned Retreat as a feint.
    Returns True if recognised — the feint has no effect and pursuit proceeds normally.
    [canonical: mass_battle_v30.md §A.12 Clarification — "d10s equal to the opposing general's
     Command against Ob 2 to recognise the Feigned Retreat as a feint"]"""
    net = roll_pool(pursuer.command)
    trace_event('draw', tick=None, side=getattr(pursuer, 'faction', '?'), unit=getattr(pursuer, 'name', '?'), kind='feint', band=degree_label(net, FEIGNED_RECOGNIZE_OB))
    return net >= FEIGNED_RECOGNIZE_OB


def feigned_retreat_check(pursuer):
    """A pursuer deceived by a Feigned Retreat makes a Discipline check Ob 1 to HOLD (not overextend).
    Returns True if it holds; False if it OVEREXTENDS (chases into the trap).
    [canonical: PP-256 / mass_combat.md §PP-256 — pursuing-side Discipline check Ob 1; hold
     P~87% at Discipline 4, ~40% at Discipline 1]"""
    net = roll_pool(pursuer.discipline)
    trace_event('draw', tick=None, side=getattr(pursuer, 'faction', '?'), unit=getattr(pursuer, 'name', '?'), kind='feint', band=degree_label(net, FEIGNED_RETREAT_OB))
    return net >= FEIGNED_RETREAT_OB


def resolve_feigned_retreat(pursuer, feigning_unit):
    """Resolve a Feigned Retreat when `pursuer` begins chasing a `feigning_unit`. Inert unless
    MB_FEIGNED_RETREAT is ON. Two-stage per §A.12: recognise (Command Ob 2) then, if deceived,
    Discipline Ob 1. On a failed Discipline check the pursuer is marked OVEREXTENDED (its next
    engagement pool is cut by OVEREXTEND_PENALTY — see multi.base_combat_pool). Returns a dict
    describing the outcome, or None if the feint did not apply.
    [canonical: PP-256, mass_battle_v30.md §A.12 / §B.4 tactic card — Overextended]"""
    # [MB-04] A 'lure' instruction (the Feint role) declares the same feint the 'feign_retreat' order
    # pseudo-field does; read live here (hierarchy.units.unit_lures), never copied onto `.feigned`.
    if not MB_FEIGNED_RETREAT or not (getattr(feigning_unit, 'feigned', False) or unit_lures(feigning_unit)):
        return None
    if feigned_retreat_recognized(pursuer):
        return {'recognized': True, 'overextended': False}
    # Deceived — Discipline check to avoid overextending.
    held = feigned_retreat_check(pursuer)
    if not held:
        pursuer.overextended = True
    return {'recognized': False, 'overextended': not held}


# ─── MULTI-UNIT BATTLE ORCHESTRATOR (D-3, D-5) ──────────────────────────
# (B17.05: the multi-engagement loops moved to `systems/mass_battle/sim/multi.py`; what stays here is what the season reaches.)
# Models battles with multiple units per side. Each engagement pair runs through
# run_battle (1v1). After all pairs resolve: morale cascade, rout contagion,
# freed-attacker flanking. Between turns: recovery.
# [canonical: designs/provincial/mass_battle_v30.md §A.12 — Morale Cascade,
#  Rout contagion brake, pursuit rules]

# Morale cascade discipline check — Ob 1, fires at Phase 6 Step 3
# [canonical: §A.12 — "all friendly units in the same engagement make a
#  Discipline check (Ob 1). Failure: Morale −1"]
MORALE_CASCADE_OB = 1  # [canonical: designs/provincial/mass_battle_v30.md §A.12]
ROUT_CONTAGION_MORALE_HIT = 1  # [canonical: designs/provincial/mass_battle_v30.md L167]
FREED_ATTACKER_FLANK_PENALTY = 1  # [canonical: §A.4 octagon YELLOW = -1D]


def discipline_check_cascade(unit):
    """Discipline check Ob 1 for morale cascade.
    Returns True if unit PASSES (resists cascade).
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — Ob 1 check]"""
    # [canonical: params/mass_combat.md — roll_pool uses TN 7 default]
    net = roll_pool(unit.discipline)
    return net >= MORALE_CASCADE_OB


__all__ = ['morale_check_phase', 'rout_resolution', 'discipline_check_phase', 'rally_check', 'reform_check', 'phase_boundary', 'Unit', 'Army', 'derive_command', 'assign_targets', 'resolve_cross_side_contention', 'find_contacts', 'count_engagements_per_atom', '_momentum_speed', '_cascade_depth_key', 'MB_ROLLUP_PER_RANK', 'MB_ROLLUP_MARGIN', 'MB_ROLLUP_REACH', 'MB_ROLLUP_CAP', 'MB_ROLLUP_FLANK_REACH', 'MB_ROLLUP_MIN_DEPTH', 'engaged_files', 'resolve_engagements', 'resolve_engagements_cascading', '_atom_distance', '_roll_volley_pool', 'volley_phase', 'run_battle', 'BETWEEN_TURN_MORALE_RECOVERY', 'REARGUARD_PENALTY', 'RECALL_OB', 'pursuit_damage', 'recall_check', 'MORALE_CASCADE_OB', 'ROUT_CONTAGION_MORALE_HIT', 'FREED_ATTACKER_FLANK_PENALTY', 'discipline_check_cascade', 'roles_for', 'role_allowed', 'stats_for', 'TROOP_TYPE_STATS']
