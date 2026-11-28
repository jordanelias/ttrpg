"""The contact draw (MBA-04 steps 1-2): `core/contact_draw.py::contact_casualties`, a pure function of one `ContactVector`, the measured
table and a handed-in standard normal `z`. The first four tests call it directly, on the real table, with a seeded stream standing in
for the keyed draw owner; the last two read it where the field calls it (`resolve_melee_pair`, B19.12): its key and its armour."""
import dataclasses
import random

import pytest

from modules.mass_battle.core import contact_draw as cd
from modules.mass_battle.core import contact_table
from modules.mass_battle.troop_types.registry import support_weight

DRAWS = 20_000


def _vec(**kw):
    base = dict(arm_a='spear', armour_d='light', skill_a=3.0, skill_d=3.0, rounds_d=2.0, support_a=1.0, exposure_d=2.0,
                levels_d=(), frontage=100.0, men_d=10_000.0, arm_d='spear', armour_a='light')
    base.update(kw)
    return cd.ContactVector(**base)


def _draw_mean(vec, n=DRAWS, seed=11):
    rng = random.Random(seed)
    return sum(cd.contact_casualties(vec, contact_table, rng.gauss(0.0, 1.0)) for _ in range(n)) / n


def test_contact_draw_mean_equals_mu_above_five():
    """The drawn mean is `mu` within 1% wherever `mu >= 5` (the normal form's own accuracy); control: a vector below 5 is NOT held to it."""
    checked = 0
    for kw in (dict(frontage=100.0), dict(frontage=400.0, rounds_d=4.0), dict(frontage=200.0, exposure_d=3.0, arm_a='arming', armour_d='none'),
               dict(frontage=250.0, levels_d=(2.0, 1.0), support_a=1.5), dict(frontage=1500.0, skill_a=5.0, skill_d=1.0, rounds_d=6.0)):
        vec = _vec(**kw)
        mu, var = cd.contact_mu_var(vec, contact_table)
        assert mu >= 5.0 and var > 0.0, (kw, mu, var)
        got = _draw_mean(vec)
        assert abs(got - mu) <= 0.01 * mu, (kw, got, mu)
        checked += 1
    assert checked == 5
    thin = _vec(frontage=3.0, exposure_d=1.0)
    assert cd.contact_mu_var(thin, contact_table)[0] < 5.0   # the control arm exists: below 5 the clip is allowed to bias


def test_clip_bias_is_reported_below_five():
    """Clipping at zero raises the mean where `mu` is small; the bias is printed by `mu` (run with -s), and it is never negative."""
    rows = []
    for f in (2.0, 5.0, 10.0, 20.0, 30.0, 40.0, 50.0):
        vec = _vec(frontage=f, exposure_d=1.0, rounds_d=1.0)
        mu, var = cd.contact_mu_var(vec, contact_table)
        if mu >= 5.0:
            continue
        rows.append((mu, _draw_mean(vec) - mu))
    assert len(rows) >= 4
    for mu, bias in rows:
        print(f'clip bias at mu={mu:.3f}: {bias:+.4f} men ({bias / mu:+.2%})')
        assert bias >= -0.02 * mu
    assert max(b for _, b in rows) > 0.0   # the bias the clip adds is observable, not assumed away


def test_the_vector_is_the_only_input(monkeypatch):
    """Planting `_friction` on the vector, or flipping the field's side terms in config, changes nothing; a real field does (control)."""
    vec = _vec()
    base = cd.contact_casualties(vec, contact_table, 0.7)
    state = random.getstate()
    planted = _vec()
    object.__setattr__(planted, '_friction', 9.0)
    assert cd.contact_casualties(planted, contact_table, 0.7) == base
    monkeypatch.setattr(cd, 'MB_FRICTION', True, raising=False)
    monkeypatch.setattr(cd, 'MB_FRICTION_SIGMA', 4.0, raising=False)
    assert cd.contact_casualties(vec, contact_table, 0.7) == base
    assert random.getstate() == state    # no RNG inside: the module drew nothing of its own
    assert cd.contact_casualties(_vec(frontage=vec.frontage * 2), contact_table, 0.7) != base
    with pytest.raises(dataclasses.FrozenInstanceError):
        vec.frontage = 1.0


def test_depth_enters_only_through_support_and_endurance():
    """Two bodies of equal frontage and different depth: the vector has no depth, so `mu` differs only through `support_a` (the one
    owner `support_weight`) and `rounds_d` (endurance); with those held equal `mu` is equal."""
    assert not {'depth', 'ranks', 'files', 'troops', 'size', 'men'} & {f.name for f in dataclasses.fields(cd.ContactVector)}
    shallow = _vec(support_a=sum(support_weight(d, 'spearmen') for d in range(1, 2)))
    deep = _vec(support_a=sum(support_weight(d, 'spearmen') for d in range(1, 7)))
    assert shallow.frontage == deep.frontage and shallow.support_a != deep.support_a
    mu_s, mu_d = cd.contact_mu_var(shallow, contact_table)[0], cd.contact_mu_var(deep, contact_table)[0]
    assert mu_s != mu_d                                                   # depth did reach mu, through support_a
    assert cd.contact_mu_var(dataclasses.replace(deep, support_a=shallow.support_a), contact_table)[0] == mu_s   # and only through it
    tired = cd.contact_mu_var(dataclasses.replace(shallow, rounds_d=5.0), contact_table)[0]
    assert tired != mu_s                                                  # endurance is the other road


# ---- where the field calls it (B19.12): the key, and the armour through `resolve_field` -------------------------------------------

def _two_contacts():
    """Two armies of two units each, in two separate contacts (A0 against B0 at column 6, A1 against B1 at column 20): a hand-built
    tick, the pairs from `find_contacts`."""
    from modules.mass_battle.core import contact
    from modules.mass_battle.hierarchy.units import Army, Unit

    def army(fac, row, adv):
        subs = [Unit.of_type('spearmen', 'Line', 2, (row, c), troops=200, width=2, depth=1, advance_dir=adv) for c in (6, 20)]
        return Army(name=fac, faction=fac, power=4, command=4, discipline=5, discipline_start=5, morale=6, morale_start=6,
                    units=subs, dr=1)
    ua, ub = army('A', 23, 1), army('B', 25, -1)
    pairs = contact.find_contacts(ua, ub)
    assert len(pairs) == 2 and {id(p['atom_b']) for p in pairs} == {id(s) for s in ub.units}, 'the fixture lost a contact'
    return ua, ub, pairs


def _one_tick(seed, t=3):
    """One `resolve_engagements` over the two contacts: the per-cell casualties each B unit took, and the field stream's ordinal before
    and after (the contact draw takes nothing from it)."""
    from engine.dice_engine import draw
    from modules.mass_battle import orchestration as orch
    from modules.mass_battle import rngsource
    ua, ub, pairs = _two_contacts()
    rng = draw.seeded(draw.H2('test_mass_battle_contact_draw', seed))
    with rngsource.using(rng):
        n0 = rng.n
        res = orch.resolve_engagements(ua, ub, pairs, t=t)
        n1 = rng.n
    got = {}
    for i, sub in enumerate(ub.units):
        slot = res['cell_dmg_b'].get(id(sub))
        got[i] = sum(slot[1].values()) if slot else 0.0
    return got, (n0, n1)


def test_one_key_per_purpose(monkeypatch):
    """A-30: each contact's draw is keyed on its own (field, bout, tick, pair, side, "contact"), so re-keying one contact changes that
    contact and no other, and the draw takes nothing from the field's stream. Falsifier (MBA-04 (d)): "re-keying one contact changes
    another". Control: the re-key is seen on the contact it was applied to."""
    checked = 0
    for seed in range(20):
        base, (n0, n1) = _one_tick(seed)
        assert n1 == n0, 'the contact draw consumed the field stream: a change elsewhere in the field would re-key it'
        orig = cd.contact_z

        def rekeyed(bout, t, slot_a, slot_b, side, _orig=orig):
            return _orig(bout, t, slot_a, slot_b, side + ('-rekeyed' if slot_a == 0 else ''))
        monkeypatch.setattr(cd, 'contact_z', rekeyed)
        moved, _ = _one_tick(seed)
        monkeypatch.setattr(cd, 'contact_z', orig)
        assert moved[1] == base[1], (seed, base, moved)       # the other contact's casualties did not move
        if moved[0] != base[0]:
            checked += 1                                      # the re-key reached the contact it was applied to
    assert checked >= 15, f'the re-key moved the re-keyed contact on only {checked} of 20 seeds: the control does not observe it'


def _armour_field(armour, seed, monkeypatch):
    """A mirror field through `resolve_field` (two headcount sides, open ground, friction off) in which the DEFENDER's men wear `armour`
    and the attacker's wear `light`; everything else equal. Returns the defender's men lost as a share of its start."""
    from engine.dice_engine import draw
    from modules.mass_battle import orchestration as orch
    from modules.mass_battle.massbattle import resolve_field
    monkeypatch.setattr(orch, 'MB_FRICTION', False)
    orig = cd.fighter

    def kit(atom, _orig=orig):
        arm, _armour, skill = _orig(atom)
        return arm, (armour if atom._unit.faction == 'B' else 'light'), skill     # 'B' is the defender (`_weighted_unit`)
    monkeypatch.setattr(cd, 'fighter', kit)
    try:
        out = resolve_field(_MIRROR, draw.seeded(draw.H2('test_heavier_armour_loses_fewer_men', seed)))
    finally:
        monkeypatch.setattr(cd, 'fighter', orig)
    return 1.0 - out.defender.share / 100.0


def _mirror_input():
    import yaml
    from engine.season.data import files
    from engine.season.queries.inputs import MassBattleInput
    with open(files.GEOGRAPHY_YAML, encoding='utf-8') as f:
        geo = yaml.safe_load(f)
    return MassBattleInput(weights=((3.0,), (3.0,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None, origin=None,
                           loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo, condition_scale=100, members=(('a',), ('b',)))


_MIRROR = _mirror_input()


def test_heavier_armour_loses_fewer_men(monkeypatch):
    """Armour enters through the measured felling chance and nowhere else (MBA §1.6: never subtracted), so through `resolve_field` the
    defender's mean losses fall strictly as its armour tier rises, none > light > medium > heavy, on the same seeds. Falsifier (MBA-04
    (e)): armour not monotone. n 200 fields per tier; the loop asserts it fought them, and that the fields were fought (losses above 0)."""
    n, checked, means = 200, 0, []
    for armour in ('none', 'light', 'medium', 'heavy'):
        lost = []
        for seed in range(n):
            lost.append(_armour_field(armour, seed, monkeypatch))
            checked += 1
        means.append(sum(lost) / n)
    assert checked >= 4 * n
    assert means[0] > 0.0, f'the defender lost nobody without armour: no field was fought ({means})'
    assert means[0] > means[1] > means[2] > means[3], f'armour not monotone through resolve_field: {means}'
