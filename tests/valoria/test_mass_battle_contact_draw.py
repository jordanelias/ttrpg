"""The contact draw (MBA-04 step 1): `core/contact_draw.py::contact_casualties`, a pure function of one `ContactVector`, the measured
table and a handed-in standard normal `z`. Nothing in the field calls it yet (B19.12), so these tests call it directly, on the real
table, with a seeded stream standing in for the keyed draw owner."""
import dataclasses
import random

import pytest

from modules.mass_battle.core import contact_draw as cd
from modules.mass_battle.core import contact_table
from modules.mass_battle.troop_types.registry import support_weight

DRAWS = 20_000


def _vec(**kw):
    base = dict(arm_a='spear', armour_d='light', skill_a=3.0, skill_d=3.0, rounds_d=2.0, support_a=1.0, exposure_d=2.0,
                levels_d=(), levels_a=(), frontage=100.0, men_d=10_000.0, arm_d='spear', armour_a='light')
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
