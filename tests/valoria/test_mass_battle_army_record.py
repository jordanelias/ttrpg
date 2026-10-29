"""ED-IN-0304 phase 2 -- the rules under the season's army verbs: how many troops a place can raise
(`troop_types/recruitment.py`) and what an army record says and how it changes (`armyrecord.py`).

Both are pure, so they are tested without a `World`. What each test is able to see go wrong is stated beside it:
a recruit limit that ignored population, or infrastructure, or a type's own kind of infrastructure, fails the
test named for that; a record operation that lost or invented a trooper fails the conservation test.
"""
import random

import pytest

from engine.season.data.rosters import SITE_KINDS
from engine.season.queries.inputs import MassBattleInput
from modules.mass_battle import armyrecord as A
from modules.mass_battle import massbattle
from modules.mass_battle.troop_types import recruitment as R
from modules.mass_battle.troop_types.registry import TROOP_TYPE_STATS

FULL = 1000


def _limit(t, weight=12, sites=None, raised=None):
    return R.recruit_limit(t, weight, sites or {}, raised or {}, FULL)


# ----------------------------------------------------------------------------------- recruiting limits
def test_population_bounds_the_army():
    small, big = _limit('levy', weight=2), _limit('levy', weight=12)
    assert 0 < small < big, "more population must allow more troops, and a small place some"
    assert big == R.under_arms_cap(12) == int(12 * R.TROOPS_PER_WEIGHT * R.MUSTER_FRACTION)


def test_levy_needs_no_infrastructure_but_a_trained_type_does():
    assert R.training_site_for('levy') is None and _limit('levy') > 0
    assert _limit('archers') == 0, "archers with no archery range must raise none"
    assert _limit('archers', sites={'archery_range': FULL}) == R.under_arms_cap(12)


def test_each_kind_of_troop_needs_its_own_kind_of_site():
    kinds = {k for k, _ in R.TRAINING_SITE.values()}
    assert len(kinds) == 4, "vacuous if the types do not span four kinds of site"
    for t, (kind, _floor) in R.TRAINING_SITE.items():
        for other in kinds - {kind}:
            assert _limit(t, sites={other: FULL}) == 0, f"{t}: a {other} must not train it"
        assert _limit(t, sites={kind: FULL}) > 0, f"{t}: its {kind} must train it"


def test_a_half_built_site_trains_half_and_an_elite_floor_blocks_it():
    full = _limit('heavy_infantry', sites={'barracks': FULL})
    half = _limit('heavy_infantry', sites={'barracks': FULL // 2})
    assert 0 < half < full and abs(half - full // 2) <= 1
    assert _limit('knights_templar', sites={'stable': FULL * 0.4}) == 0       # below the elite floor
    assert _limit('knights_templar', sites={'stable': FULL * 0.5}) > 0
    assert _limit('cavalry', sites={'stable': FULL * 0.4}) > 0                # no floor for ordinary horse


def test_the_two_bounds_compose():
    cap = R.under_arms_cap(12)
    sites = {'barracks': FULL, 'archery_range': FULL}
    # archers are limited by what the whole cap leaves once heavy infantry hold most of it
    assert _limit('archers', sites=sites, raised={'heavy_infantry': cap - 5}) == 5
    # a type's own raised troops count against its own share, not only the total
    assert _limit('heavy_infantry', sites={'barracks': FULL // 4}, raised={'heavy_infantry': cap // 4}) == 0
    assert _limit('levy', raised={'levy': cap}) == 0 and _limit('levy', raised={'levy': cap + 50}) == 0


def test_limits_refuse_nonsense_loudly():
    with pytest.raises(ValueError):
        _limit('dragons')
    with pytest.raises(ValueError):
        R.recruit_limit('levy', 12, {}, {}, 0)


def test_every_trained_type_names_a_real_site_kind_and_a_real_troop_type():
    for t, (kind, floor) in R.TRAINING_SITE.items():
        assert t in TROOP_TYPE_STATS, t
        assert kind in SITE_KINDS, f"{t}: {kind} is not a roster site kind"
        assert 0.0 <= floor <= 1.0


def test_every_stat_preset_type_is_trainable_or_a_levy():
    assert set(TROOP_TYPE_STATS) - set(R.TRAINING_SITE) == {'levy'}, (
        "a troop type with a stat line but no training rule could never be recruited")


# ------------------------------------------------------------------------------------- the army record
def _army():
    a = A.new('fac_crown')
    a = A.raised(a, 'c1', 'heavy_infantry', 60)
    a = A.raised(a, 'c2', 'heavy_infantry', 40)
    a = A.raised(a, 'c1', 'archers', 50)
    a = A.form(a, 'wall', 'heavy_infantry', role='ShieldWall')
    a = A.form(a, 'bows', 'archers')
    return a


def test_assign_and_release_conserve_every_trooper_and_never_mutate():
    a = _army()
    before = A.by_type(a)
    a2 = A.assign(a, 'wall', 'c1', 30)
    assert A.by_type(a) == before and A.by_type(a2) == before, "assigning moved or lost troops"
    assert A.unassigned(a, 'c1', 'heavy_infantry') == 60 and A.unassigned(a2, 'c1', 'heavy_infantry') == 30
    a3 = A.release(a2, 'wall', 'c1', 30)
    assert a3 == a, "release did not undo assign"
    for r in (a, a2, a3):
        A.validate(r)


def test_record_refusals():
    a = _army()
    cases = (lambda: A.assign(a, 'wall', 'c1', 61),            # more than trained
             lambda: A.assign(a, 'wall', 'c9', 1),             # a cohort that raised none
             lambda: A.assign(a, 'nobody', 'c1', 1),           # no such subformation
             lambda: A.assign(a, 'bows', 'c2', 1),             # c2 trained no archers
             lambda: A.form(a, 'wall', 'levy'),                # duplicate name
             lambda: A.form(a, 'x', 'heavy_infantry', role='Kite'),
             lambda: A.raised(a, 'c1', 'dragons', 5),
             lambda: A.raised(a, 'c1', 'levy', 0),
             lambda: A.raised(a, 'c1', 'levy', 2.5),
             lambda: A.order(a, 'wall', stance='retreat'),
             lambda: A.order(a, 'wall', fall_back_at=1.5),
             lambda: A.set_strategy(a, 'rout'))
    for bad in cases:
        with pytest.raises(ValueError):
            bad()
    full = A.new('f')
    for i in range(11):
        full = A.form(full, f's{i}', 'levy')
    with pytest.raises(ValueError):
        A.form(full, 'twelfth', 'levy')


def test_order_changes_only_what_it_names():
    a = A.assign(_army(), 'wall', 'c1', 30)
    b = A.order(a, 'wall', stance='hold', target='weakest')
    sf = b['subformations'][0]
    assert (sf['stance'], sf['target'], sf['role'], sf['assigned']) == ('hold', 'weakest', 'ShieldWall', (('c1', 30),))
    c = A.order(b, 'wall', stance=None, fall_back_at=0.4)
    assert c['subformations'][0]['stance'] is None and c['subformations'][0]['fall_back_at'] == 0.4


def test_record_to_order_of_battle_scales_by_fitness_and_drops_the_empty():
    a = A.assign(A.assign(_army(), 'wall', 'c1', 60), 'wall', 'c2', 40)
    a = A.order(A.set_strategy(a, 'advance'), 'wall', fall_back_at=0.5)
    oob = A.to_order_of_battle(a)                      # 'bows' has nobody assigned: dropped
    assert [s.name for s in oob.subformations] == ['wall'] and oob.strategy == 'advance'
    assert oob.subformations[0].troops == 100 and oob.subformations[0].fall_back_at == 0.5
    hurt = A.to_order_of_battle(a, fitness=lambda c: 0.5 if c == 'c1' else 1.0)
    assert hurt.subformations[0].troops == 60 * 0.5 + 40
    with pytest.raises(ValueError):
        A.to_order_of_battle(_army())                  # nothing assigned anywhere


def test_validate_rejects_a_malformed_record():
    a = _army()
    for bad in ({k: v for k, v in a.items() if k != 'trained'}, {**a, 'extra': 1}, {**a, 'strategy': 'x'},
                {**a, 'trained': (('c', 'levy', 0),)}):
        with pytest.raises(ValueError):
            A.validate(bad)


# ----------------------------------------------------------------- the record reaches the battle
def _field(oob_a, oob_b):
    return massbattle.resolve_field(MassBattleInput(
        weights=((10,), (10,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None, origin=None,
        loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, orders_of_battle=(oob_a, oob_b)), random.Random(7))


def test_an_army_record_fights():
    a = A.assign(A.assign(_army(), 'wall', 'c1', 60), 'bows', 'c1', 50)
    b = A.assign(A.raised(A.form(A.new('fac_guilds'), 'rabble', 'levy'), 'g1', 'levy', 90), 'rabble', 'g1', 90)
    r = _field(A.to_order_of_battle(a), A.to_order_of_battle(b))
    assert set(r) >= {'attacker_wins', 'degree', 'attacker_size_pct', 'defender_size_pct'}
