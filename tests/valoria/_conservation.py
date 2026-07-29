"""[ED-MB-0045 A4/S6] Single owner of the I1 troop-conservation check: Sum(cell_troops) == hp.

WHY THIS MODULE EXISTS — a pattern defect, not four coincidences (CLAUDE.md §0.1 #5).

Four acceptance suites each open-coded the same loop, and each of the four opened it with the same
UNCOUNTED skip::

    for unit in (a, b):
        if unit.routed or unit.broken:
            continue
        assert math.isclose(_unit_troops(unit), unit.hp, ...)

(`test_frontage_conservation.py` — which calls it "the hardest check" — plus
`test_reach_weapon_class.py`, `test_friction_cev.py`, `test_obb_contact_toi.py`.) A conditional assertion
with no counter cannot distinguish "the invariant held" from "the loop never reached an assertion",
which is exactly the failure §0.1 #2 names. So: one owner, every site routed through it, and the
owner RETURNS the count so each call site can assert it actually checked something.

**What the skip's incidence actually is, measured rather than assumed (§1 G1/G12 — existence in
source is not evidence of rate).** The finding that routed this work predicted the skip would fire
"almost always" under the shipped `PC_STOCHASTIC_ROUT=1`. Measured 2026-07-29 at shipped defaults, it
does not: the Line-vs-Line matchup used by three of the four files routs **0 of 120 units** across a
60-seed sweep, and the pike-vs-cavalry matchup **8 of 120**. So the four suites were NOT running
vacuous — they were one engine-tuning change away from it, with nothing that would have said so. The
defect being fixed is the missing counter, not a currently-silent test; the severity claim is
corrected here rather than repeated.

WHY THE ROUTED/BROKEN SKIP IS GONE, and the evidence for it (§0.1 #4 — a claim needs a measurement,
not an intuition):

  * Every hp write in the live tree mirrors its loss onto the cells through `distribute_casualties`.
    The four sites are `orchestration.py:1966-1967` (the melee/volley exchange, followed by the
    PER_CELL mirror immediately below), `:2504` (pursuit) and `:2566` (freed-attacker flanking) —
    the latter two being hp-ONLY writes until ED-MB-0041 fixed exactly this divergence, each now
    carrying an explicit `distribute_casualties(...)` beside it. Rout itself is a morale/flag
    transition (`core/state.py:149,189`, `hierarchy/units.py:2287-2331`): it moves no troops.
  * Structural, not only empirical (critic-sharpened): every one of the four sites drives
    `run_battle`, whose loop BREAKS the moment either unit routs (`orchestration.py:1695`) — a
    routed unit receives zero further hp writes here by construction. `core/contact.py` has no
    routed/broken filter, so a routed subunit's cells keep absorbing their mirrored share; and the
    two post-rout hp paths (`:2504`, `:2566`) live only in `run_multi_turn_battle`, which none of
    the four tests calls.
  * Measured 2026-07-29 at shipped defaults (`PC_STOCHASTIC_ROUT=1`, `PC_CELL_MORALE=0`), node
    movement path (AGENT-MEASURED per G12, ad-hoc battery, orchestrator-unreplicated; the
    structural argument above carries the decision independently): a 3:1 lopsided 200-battle
    battery produced 200 routed/broken units, 200 conserving; a 4-ratio × 60-seed
    annihilation-pressure battery 360/360, worst |Sum(cell_troops) − hp| = 4.5e-13.

  ⚠ ONE DIVERGENCE CLASS IS REAL AND UNTESTED HERE, recorded rather than papered over: the
  engaged-front spill shortfall. `_apply_with_spill` returns the amount actually applied (≤ dmg —
  "the shortfall is real", `percell.py:108-129`) and `distribute_casualties` DISCARDS that return
  (`percell.py:179`) while spilling only across the engaged front (`:162-172`) — so
  Sum(cells) > hp whenever dmg exceeds the engaged front's live troops (a strict superset of the
  hp == 0 clamp case; see `tests/valoria/test_hp_cell_ledger.py`, which documents the shortfall as
  reported). No unit in the 560 above got near it — rout ends battles long before annihilation. If
  it ever becomes reachable in these batteries, this helper going red IS the correct outcome: the
  two ledgers really would have diverged.

PRECONDITION: the hp→cell mirror is `if PER_CELL:`-gated (`orchestration.py:1968`). At PER_CELL=0
hp falls and cells never move, so this invariant is FALSE of correct grid-oracle behaviour — the
owner asserts the live config before checking anything (the only identified path where these tests
could go red on a correct engine).
"""
import math
import sys

# The tolerance the four call sites all used, kept identical so this is a pure de-duplication and
# moves no assertion. Float slop only: the measured worst case above is 4.5e-13.
REL_TOL = 1e-6
ABS_TOL = 1e-3


def unit_troops(unit):
    """Sum of live per-cell troop counts across a unit's subunits (the cell-side ledger).

    Composes on Subunit.troop_total() — the engine's own single owner of "a subunit's live
    troops" (hierarchy/units.py) — rather than re-summing cell_troops here. Sibling invariant
    home: tests/valoria/test_hp_cell_ledger.py (per-exchange drift; this module checks end-state).
    """
    return sum(su.troop_total() for su in unit.subunits)


def assert_troop_conservation(*units, context=''):
    """I1: assert Sum(cell_troops) == hp for EVERY unit given (routed and broken included).

    Returns the number of units checked. NOTE: `checked` increments unconditionally per unit
    passed, so a call-site `assert checked >= 2` is a FORWARD GUARD against a skip being re-added
    inside this owner — it cannot fail today, and that is its declared purpose, not a live check.
    Raises AssertionError naming the offending unit on the first divergence.
    """
    cfg = sys.modules.get('mass_battle.config')
    assert cfg is not None and getattr(cfg, 'PER_CELL', False), (
        "conservation requires PER_CELL=1 — the hp->cell mirror is PER_CELL-gated "
        "(orchestration.py:1968); at PER_CELL=0 this invariant is false of correct behaviour")
    checked = 0
    where = f"{context}: " if context else ''
    for unit in units:
        troops = unit_troops(unit)
        assert math.isclose(troops, unit.hp, rel_tol=REL_TOL, abs_tol=ABS_TOL), (
            f"{where}{getattr(unit, 'name', unit)}"
            f"{' [routed]' if getattr(unit, 'routed', False) else ''}"
            f"{' [broken]' if getattr(unit, 'broken', False) else ''}"
            f": Sum(cell_troops)={troops} != hp={unit.hp}")
        checked += 1
    return checked
