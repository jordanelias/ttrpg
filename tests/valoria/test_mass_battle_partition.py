"""The pair rule's gate (`16_PESSIMIST_MB_partition_and_the_pair_rule` gate rows 1-5; MBA-04's GATE, B19.12): a force's result does
not depend on how many bodies its cells are grouped into, and no match-up is certain.

Rows 1-4 fight hand-built armies through `run_battle` (the field's own loop; friction off, the per-side log-normal would swamp a
partition effect); row 5 goes through `resolve_field`, shipped configuration. Every loop asserts it counted (`checked >= n`), n 100
unless said. Footprints are width x depth in cells (S-7: the pair rule's `files`/`ranks`). A side WINS a field when `run_battle`
names it the winner (the other side routed or conceded), or, when the eighteen ticks ran out with both standing, when it kept the
larger share of its men (`hp / hp_max`). [ASSUMPTION: a drawn field is won on the share kept -- basis: one bout rarely routs a side at
the seeded exposure, so `run_battle`'s winner alone reads nearly every field drawn and a band of shares of nothing observes nothing;
the share kept is `_grade`'s own reading of a field; reversible: `_winner`.]

THE SAMPLING BAND (row 1): two standard errors of the difference of two shares of n, at the one-body row's share (the gate's "about ten
points either way at n 100" is the reading at a share near 0.2 or 0.8; at 0.5 it is 14 points). [ASSUMPTION: two standard errors --
basis: the gate names a sampling band and its size at n 100, not a multiple; two is the convention every other band in these files uses.]
"""
import math

import pytest

from engine.dice_engine import draw
from modules.mass_battle import orchestration as orch
from modules.mass_battle import rngsource
from modules.mass_battle.battle_loop import run_battle
from modules.mass_battle.hierarchy.units import Army, Unit

N = 100
A_ROW, B_ROW = 30, 36        # the two deployment rows: A advances +row, B -row; six rows apart, so the bodies close in a few ticks
TROOP = 'spearmen'           # a pole arm: its support reaches a second rank, so depth is a live quantity in every row


@pytest.fixture(autouse=True)
def _no_friction(monkeypatch):
    monkeypatch.setattr(orch, 'MB_FRICTION', False)


def _body(row, col, adv, width, depth, troops, troop_type=TROOP):
    return Unit.of_type(troop_type, 'Line', 2, (row, col), troops=float(troops), width=width, depth=depth, advance_dir=adv)


def _army(fac, bodies):
    return Army(name=fac, faction=fac, power=4, command=4, discipline=5, discipline_start=5, morale=6, morale_start=6,
                units=list(bodies), dr=1)


def _winner(res, ua, ub):
    """'A', 'B' or 'draw' (the module docstring's reading of a field)."""
    if res['winner'] in ('A', 'B'):
        return res['winner']
    ka, kb = ua.hp / ua.hp_max, ub.hp / ub.hp_max
    return 'A' if ka > kb else ('B' if kb > ka else 'draw')


def _fight(build_a, build_b, seed, tag):
    """One field: `build_a()`/`build_b()` return each side's list of bodies; returns (winner, army A, army B)."""
    ua, ub = _army('A', build_a()), _army('B', build_b())
    with rngsource.using(draw.seeded(draw.H2(f'test_mass_battle_partition|{tag}', seed))):
        res = run_battle(ua, ub, max_ticks=18)
    return _winner(res, ua, ub), ua, ub


def _split(row, col, adv, width, depth, troops, parts):
    """The footprint `width x depth` at `(row, col)` as `parts` bodies side by side, each `width // parts` files wide: the same cells,
    the same men, grouped into more bodies."""
    w = width // parts
    assert w * parts == width
    return [_body(row, col + i * w, adv, w, depth, troops / parts) for i in range(parts)]


def _band(p, n=N):
    return 2.0 * math.sqrt(max(p * (1.0 - p), 0.25 / n) * 2.0 / n)


# (width, depth, men, parts, the block's width x depth): three files by two deep, one file each; three cells in one row, one cell each;
# six files by one row, two cells each. The block facing it holds the same men, deeper.
FOOTPRINTS = ((3, 2, 600, 3, (2, 3)), (3, 1, 300, 3, (1, 3)), (6, 1, 600, 3, (3, 2)))


@pytest.mark.parametrize('role', ['attacker', 'defender'])
def test_partition_same_cells_inside_sampling_band(role):
    """Row 1: one body against a block, and the same cells as three bodies, on three footprints, as attacker and as defender: every
    split row's share of wins within the sampling band of its one-body row. Falsifier: any split row outside its band ("row 1 on the
    block footprint ... rests on edit 4 alone")."""
    checked, rows = 0, []
    for width, depth, men, parts, (bw, bd) in FOOTPRINTS:
        col, bcol = 12, 12 + (width - bw) // 2
        wins = {}
        for k in (1, parts):
            won = 0
            for seed in range(N):
                ours = lambda k=k: _split(A_ROW if role == 'attacker' else B_ROW, col, 1 if role == 'attacker' else -1,
                                          width, depth, men, k)
                block = lambda: [_body(B_ROW if role == 'attacker' else A_ROW, bcol, -1 if role == 'attacker' else 1, bw, bd, men)]
                build_a, build_b = (ours, block) if role == 'attacker' else (block, ours)
                winner, _ua, _ub = _fight(build_a, build_b, seed, f'p1|{role}|{width}x{depth}|{k}')
                won += winner == ('A' if role == 'attacker' else 'B')
                checked += 1
            wins[k] = won / N
        rows.append((f'{width}x{depth}', wins[1], wins[parts], _band(wins[1])))
    assert checked >= len(FOOTPRINTS) * 2 * N
    bad = [r for r in rows if abs(r[2] - r[1]) > r[3]]
    assert not bad, f'{role}: split rows outside the sampling band of their one-body row (footprint, one body, split, band): {rows}'


def test_shape_one_rank_loses_more_than_wins():
    """Row 2: a one-row line (six files by one) against a block of equal men (three by two) loses more often than it wins, and wins
    some. Falsifier: the line wins at least as often as it loses, or never wins."""
    checked = won = lost = 0
    for seed in range(N):
        winner, _ua, _ub = _fight(lambda: [_body(A_ROW, 12, 1, 6, 1, 600)], lambda: [_body(B_ROW, 13, -1, 3, 2, 600)], seed, 'p2')
        won += winner == 'A'
        lost += winner == 'B'
        checked += 1
    assert checked >= N
    assert lost > won and won > 0, f'line against block: line won {won}, lost {lost} of {N}'


def test_size_two_to_one_smaller_wins_some():
    """Row 3: one body each, 2:1 in men on the same footprint shape: the smaller side wins some fields and fewer than half."""
    checked = small = 0
    for seed in range(N):
        winner, _ua, _ub = _fight(lambda: [_body(A_ROW, 12, 1, 4, 3, 1200)], lambda: [_body(B_ROW, 12, -1, 4, 3, 600)], seed, 'p3')
        small += winner == 'B'
        checked += 1
    assert checked >= N
    assert 0 < small < N / 2, f'2:1: the smaller side won {small} of {N}'


def test_flank_detachment_helps():
    """Row 4: 600 in front and 300 on the flank rout a three-deep line of 600 more often than 600 alone do. The detachment deploys
    two rows ahead of the frontal body and off the line's end (column 15 against a line on 12-13), so it closes on the line's flank
    while the front holds it."""
    def line():
        return [_body(B_ROW, 12, -1, 2, 3, 600)]

    checked, routs = 0, {}
    for arm, build in (('alone', lambda: [_body(A_ROW, 12, 1, 2, 3, 600)]),
                       ('flank', lambda: [_body(A_ROW, 12, 1, 2, 3, 600), _body(A_ROW + 2, 15, 1, 1, 3, 300)])):
        r = 0
        for seed in range(N):
            _w, _ua, ub = _fight(build, line, seed, f'p4|{arm}')
            r += bool(ub.routed)
            checked += 1
        routs[arm] = r
    assert checked >= 2 * N
    assert routs['flank'] > routs['alone'], f'the flank detachment did not help: routs {routs} of {N}'


def _field(oob_a, oob_b, territory, fort_level, seed):
    import yaml
    from engine.season.data import files
    from engine.season.queries.inputs import MassBattleInput
    from modules.mass_battle.massbattle import resolve_field
    global _GEO
    if _GEO is None:
        with open(files.GEOGRAPHY_YAML, encoding='utf-8') as f:
            _GEO = yaml.safe_load(f)
    inp = MassBattleInput(weights=((10,), (10,)), territory=territory, fort_level=fort_level, stances=(0.0, 0.0), walls_dr=None,
                          origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography=_GEO, condition_scale=100,
                          orders_of_battle=(oob_a, oob_b))
    return resolve_field(inp, draw.seeded(draw.H2('test_mass_battle_partition|p5', seed)))


_GEO = None


def test_no_certain_matchup_through_resolve_field():
    """Row 5, through `resolve_field`, shipped configuration (friction as shipped): 3,000 spearmen against 300 levy behind walls: the
    defender loses somebody in most fields and the attacker's wins are neither 0 nor n; levy against levy on open ground: somebody is
    hurt in most fields."""
    from engine.season.data.rosters import WON
    from engine.season.seam.ladder import field_degree
    from modules.mass_battle.orderofbattle import OrderOfBattle, UnitRow
    from modules.mass_battle import terrain

    def oob(troop_type, n):
        return OrderOfBattle((UnitRow('body', troop_type, n),), 'line')

    walled = next(t for t in _walled_territories())
    checked = hurt_def = wins = 0
    for seed in range(N):
        out = _field(oob('spearmen', 3000), oob('levy', 300), walled, 1.0, seed)
        assert not isinstance(out, dict), f'the field was refused: {out}'
        hurt_def += out.defender.share < 100
        wins += field_degree(out) == WON
        checked += 1
    assert checked >= N
    assert terrain.terrain_row_for_territory(walled, 1.0, geography=_GEO) == terrain.WALLS
    assert hurt_def > N / 2, f'behind walls the levy lost nobody in {N - hurt_def} of {N} fields'
    assert 0 < wins < N, f'3,000 spearmen against 300 levy behind walls: the attacker won {wins} of {N}'
    checked = hurt = 0
    for seed in range(N):
        out = _field(oob('levy', 300), oob('levy', 300), None, 0.0, seed)
        hurt += out.attacker.share < 100 or out.defender.share < 100
        checked += 1
    assert checked >= N
    assert hurt > N / 2, f'levy against levy on open ground: nobody hurt in {N - hurt} of {N} fields'


def _walled_territories():
    """Known territories of the geography file: a fielded fortification makes any of them a WALLS field (`terrain_row_for_territory`)."""
    import yaml
    from engine.season.data import files
    global _GEO
    if _GEO is None:
        with open(files.GEOGRAPHY_YAML, encoding='utf-8') as f:
            _GEO = yaml.safe_load(f)
    return sorted(_GEO['provinces'])
