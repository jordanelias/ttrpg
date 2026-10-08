"""WR-03: Mending is priced by ONE owner at all three sites that resolve it.

Before WR-03, `operations.attempt_mending`, `collective.attempt_collective_operation` and
`opposing.resolve_opposing_operations` each priced a Mending its own way: the single operation
charged 0 Coherence (ED-871) and handed the mender a restorative term (C-1, §6.8); the collective
charged every participant the scale cost plus -1 on a bad degree and returned nothing; the opposed
table charged its scale costs and priced Mending Stability off the scale-cost proxy. Same working,
three answers — NERS S, "calculations consistent in methodology". All three now read
`operations.mending_priced_scale` (which scale was worked), `operations.price_mending` (cost, MS
delta, restorative term) and `operations.apply_mending_feedback` (the term, through `recover`).

  * THE PARITY TEST (`test_three_sites_price_one_mending_alike`): for every (scale, degree) the
    three sites return the same cost, the same MS delta and the same elastic displacement returned
    to a pre-stressed mender. Falsifier: a planted change at ONE site alone (re-pricing collective's
    Mending off the unfallen scale, say) reddens it.
  * THE CONTROL (`test_collective_and_opposing_unchanged_outside_mending`, `test_attempt_mending_unchanged`): every op_type EXCEPT Mending, in both
    collective and opposing, and every `attempt_mending` output, equals the base commit dd91783a
    at the shipped `RESILIENCE_GAIN` (0). The captured values are inlined as one sha256 per
    (site, op_type) over a canonical JSON of every result field and every resulting Coherence
    state, log included; on a mismatch the failure prints the recomputed first record.
  * R-14 ROUTING (`test_collective_and_opposing_route_cost_through_resilience`): collective and
    opposing now hand every cost to `operations.resist_coherence_cost` per practitioner.
"""
import hashlib
import json
import os
import random
import sys
from types import SimpleNamespace

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from systems.threadwork.sim import coherence as coh  # noqa: E402
from systems.threadwork.sim import collective as col  # noqa: E402
from systems.threadwork.sim import operations as ops  # noqa: E402
from systems.threadwork.sim import opposing as opp  # noqa: E402


class _World:
    """The one field coherence reads off a World."""
    def __init__(self):
        self.practitioners = {}


class _Practitioner:
    def __init__(self, actor_id, *, spirit=1, ts=30, history=0, cognition=None, resilience=None):
        self.actor_id, self.spirit, self.ts, self.history = actor_id, spirit, ts, history
        if cognition is not None:
            self.cognition = cognition
        if resilience is not None:
            self.resilience = resilience


# ─── The control grid (captured at dd91783a, before WR-03) ───────────────────────────────────────

CONTROL_SEEDS = range(12)
CONTROL_SCALES = ("Object", "Personal", "Relational", "Field", "Territorial", "Structural",
                  "Foundational")


def _states(w):
    return {aid: s.to_dict() for aid, s in sorted(w.practitioners.items())}


def _op_record(r):
    if r is None:
        return None
    return {k: getattr(r, k) for k in (
        "operation", "actor", "degree", "net_successes", "pool", "tn", "ob", "coherence_delta",
        "mending_stability_delta", "coherence_restored", "resting_point_mended", "notes")}


def _collective_actors():
    return [_Practitioner("anchor", spirit=3, ts=60),
            _Practitioner("helper1", spirit=2, ts=40, cognition=4),
            _Practitioner("helper2", spirit=1, ts=30)]


def collective_records(op_type):
    out = []
    for scale in CONTROL_SCALES:
        for seed in CONTROL_SEEDS:
            w = _World()
            r = col.attempt_collective_operation(_collective_actors(), op_type, {"scale": scale},
                                                 world=w, rng=random.Random(seed))
            out.append({"scale": scale, "seed": seed, "op_type": r.op_type, "anchor": r.anchor,
                        "helpers": r.helpers, "leap_results": r.leap_results,
                        "lattice_formed": r.lattice_formed,
                        "lattice_fractured": r.lattice_fractured, "notes": r.notes,
                        "operation_result": _op_record(r.operation_result), "states": _states(w)})
    return out


def opposing_records(op_type):
    out = []
    for scale in CONTROL_SCALES:
        for seed in CONTROL_SEEDS:
            w = _World()
            r = opp.resolve_opposing_operations(_Practitioner("a", spirit=3, ts=50),
                                                _Practitioner("b", spirit=2, ts=40),
                                                op_type, {"scale": scale}, world=w,
                                                rng=random.Random(seed))
            out.append({"scale": scale, "seed": seed, **{k: getattr(r, k) for k in (
                "actor_a", "actor_b", "op_type", "a_net", "b_net", "a_degree", "b_degree",
                "outcome", "ms_delta", "a_consequences", "b_consequences")}, "states": _states(w)})
    return out


def mending_records():
    out = []
    for scale in (*ops.MENDING_OB, "Object", None):
        for configuration_of in (None, "self"):
            for env in (False, True):
                for seed in CONTROL_SEEDS:
                    w = _World()
                    coh.apply_coherence_delta("prac", -(coh.ELASTIC_RANGE + 3), "pre-stress", world=w)
                    target = {} if scale is None else {"scale": scale}
                    if configuration_of is not None:
                        target["configuration_of"] = configuration_of
                    r = ops.attempt_mending(_Practitioner("prac", spirit=2), target, world=w,
                                            rng=random.Random(seed), environment_in_equilibrium=env)
                    out.append({"scale": scale, "configuration_of": configuration_of, "env": env,
                                "seed": seed, "result": _op_record(r), "states": _states(w)})
    return out


def digest(records):
    return hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()

# sha256 of `digest(<site>_records(op_type))`, captured at dd91783a (WR-02, before WR-03) with
# RESILIENCE_GAIN = 0. Mending in collective/opposing is NOT here: it is the declared mover.
# 10 digests x 84 records (7 scales x 12 seeds) here, plus BASE_MENDING_DIGEST over 288 records = 1128
# pinned. TO RE-DERIVE (the SHA will not survive a squash merge, so the recipe is the provenance): check
# out systems/threadwork/sim/{operations,collective,opposing,coherence}.py from the last commit before
# WR-03's owner existed (the parent of the commit that added `price_mending`), set RESILIENCE_GAIN = 0,
# and run `digest(collective_records(op))` / `digest(opposing_records(op))` / `digest(mending_records())`
# from this file.
BASE_DIGESTS = {
    ("collective", "Weaving"): "12c54575a96ea3181cbbee8a028fa1b409a2661b33de49b9d3a629e22691fe6a",
    ("collective", "Pulling"): "0565bff6080038a7b630a023a584d6e3bf8ad177ca2c8d1bd7541c27d519efd2",
    ("collective", "Locking"): "a3c11b29c120ab2026c8ca92b3c9fe088396ceedddcfc8b21e8c8fca18a979bd",
    ("collective", "Dissolution"): "3b852e5019baf6fd816086076270dad746288296798702ad5ad296af05c7180c",
    ("collective", "POP"): "17d862b60771da29bf8fa94d2fda28e296fd114e69eaa27a22e2bbf27d13a02f",
    ("opposing", "Weaving"): "6cc3f6df33081ea65dce96be96cfd672805e60f696f13f5dfb900e86a41be660",
    ("opposing", "Pulling"): "5c994c7a4809ceb1b140e03fe7f8987574afd11368339765c254fa91f9e7283c",
    ("opposing", "Locking"): "aa9bf523a8ca0d37ae25c1dc76051620dddd0f07fedf846145bee8851fc5cff2",
    ("opposing", "Dissolution"): "a4470b6deb3d04455d27a2d1068c0d5ce69e906c21fbf5252ba4b71c14ded393",
    ("opposing", "POP"): "763e3426cdce3033c8f4c6c5694bad57fdef03816b237dcbcd8a3c1410cdd7e4",
}
BASE_MENDING_DIGEST = "df54b6f5164d89f7a83b17299772622546f35598b3568dcf2da0cc14455d97a2"


@pytest.mark.parametrize("site,op_type", sorted(BASE_DIGESTS))
def test_collective_and_opposing_unchanged_outside_mending(site, op_type):
    assert ops.RESILIENCE_GAIN == 0, "the control is defined at the shipped gain"
    records = {"collective": collective_records, "opposing": opposing_records}[site](op_type)
    assert digest(records) == BASE_DIGESTS[(site, op_type)], (
        f"{site} {op_type} moved off dd91783a; first record now: {json.dumps(records[0])[:800]}")


def test_control_grid_reaches_every_branch():
    """Non-vacuity of the control: the grid reaches all four collective degrees and all nine ordered (A, B)
    pairs of the §2.6 table's three degrees, so the digests above cover every path a non-Mending result can take."""
    degrees = {r["operation_result"]["degree"] for r in collective_records("Weaving")
               if r["operation_result"] is not None}
    assert degrees == {"Overwhelming", "Success", "Partial", "Failure"}
    rows = {(r["a_degree"], r["b_degree"]) for r in opposing_records("Weaving")}
    assert len(rows) == 9, rows


def test_attempt_mending_unchanged():
    """Lifting the price and the feedback out of `attempt_mending` moved none of its outputs, on
    either aim, either environment, every priced scale plus an unpriced and an absent one."""
    records = mending_records()
    assert {r["result"]["degree"] for r in records} == {"Overwhelming", "Success", "Partial",
                                                         "Failure"}
    assert any(r["result"]["coherence_restored"] > 0 for r in records)
    assert any(r["result"]["resting_point_mended"] > 0 for r in records)
    assert digest(records) == BASE_MENDING_DIGEST, (
        f"attempt_mending moved off dd91783a; first record now: {json.dumps(records[0])[:800]}")


# ─── (a) THE PARITY TEST ─────────────────────────────────────────────────────────────────────────

PARITY_SCALES = (*ops.MENDING_OB, "Object")          # every priced scale, and one it does not price
PARITY_DEGREES = ("Overwhelming", "Success", "Partial", "Failure")
_THREE_BAND = {"Overwhelming": "Meets", "Success": "Meets", "Partial": "Partial", "Failure": "Failure"}


def _pre_stressed(w, actor_id="prac"):
    coh.apply_coherence_delta(actor_id, -coh.ELASTIC_RANGE, "pre-stress", world=w)


def _elastic(w, actor_id="prac"):
    return coh.get_state(actor_id, world=w).elastic_displacement


def _single(scale, degree, monkeypatch, env=True):
    monkeypatch.setattr(ops, "_compute_degree", lambda net, ob: degree)
    w = _World()
    _pre_stressed(w)
    r = ops.attempt_mending(_Practitioner("prac"), {"scale": scale}, world=w,
                            rng=random.Random(0), environment_in_equilibrium=env)
    return (r.ob, r.coherence_delta, r.mending_stability_delta, r.coherence_restored, _elastic(w))


def _collective(scale, degree, monkeypatch, env=True):
    # Force the Leap to take and the working's degree, through collective's own module names only.
    monkeypatch.setattr(col, "attempt_leap",
                        lambda a, t, world=None, rng=None: SimpleNamespace(degree="Success"))
    monkeypatch.setattr(col, "dice_engine", SimpleNamespace(degree_label=lambda net, ob: degree))
    w = _World()
    _pre_stressed(w)
    _pre_stressed(w, "second")
    r = col.attempt_collective_operation([_Practitioner("prac", ts=60), _Practitioner("second")],
                                         "Mending", {"scale": scale}, world=w,
                                         rng=random.Random(0), environment_in_equilibrium=env)
    op = r.operation_result
    assert op.degree == degree and not r.lattice_fractured
    # Every participant whose Leap took is priced alike, not only the Anchor.
    assert r.coherence_restored["second"] == r.coherence_restored["prac"] == op.coherence_restored
    assert _elastic(w, "second") == _elastic(w)
    return (op.ob, op.coherence_delta, op.mending_stability_delta, op.coherence_restored, _elastic(w))


def _opposing(scale, degree, monkeypatch, env=True):
    monkeypatch.setattr(opp, "_degree_label", lambda net, ob: _THREE_BAND[degree])
    w = _World()
    _pre_stressed(w)
    a, b = _Practitioner("prac"), _Practitioner("other")
    r = opp.resolve_opposing_operations(a, b, "Mending", {"scale": scale}, world=w,
                                        rng=random.Random(0), environment_in_equilibrium=env)
    assert r.a_degree == _THREE_BAND[degree]
    cons = r.a_consequences
    # OpposingResult reports no Ob, so the opposed site is compared on the price alone.
    return (None, cons["coherence_delta"], r.ms_delta, cons["coherence_restored"], _elastic(w))


def test_three_sites_price_one_mending_alike(monkeypatch):
    """Every (scale, degree, environment) cell: the three sites return the same cost, MS delta and
    elastic displacement returned. With the environment stated False the restorative term is 0 at all
    three (E-1's gate is `recover`'s, and each site must pass the caller's fact through)."""
    reached = restored_cells = 0
    for scale in PARITY_SCALES:
        priced = ops.mending_priced_scale({"scale": scale})
        for degree in PARITY_DEGREES:
            price = ops.price_mending(priced, degree)
            for env in (True, False):
                with monkeypatch.context() as m:
                    single = _single(scale, degree, m, env)
                with monkeypatch.context() as m:
                    collective = _collective(scale, degree, m, env)
                with monkeypatch.context() as m:
                    opposed = _opposing(scale, degree, m, env)
                restored = price.restorative if env else 0
                expected = (ops.MENDING_OB[priced], price.coherence_cost, price.mending_stability_delta,
                            restored, coh.ELASTIC_RANGE - restored)
                assert single[0] == collective[0] == expected[0], f"{scale}/{degree}: Ob differs"
                assert single[1:] == collective[1:] == opposed[1:] == expected[1:], (
                    f"{scale}/{degree}/env={env}: single={single} collective={collective} "
                    f"opposed={opposed} owner={expected}")
                assert price.coherence_cost == 0, "ED-871"
                reached += 1
                restored_cells += single[3] > 0
    # Non-vacuity: the restorative comparison was not 0 == 0 throughout.
    assert restored_cells == len(PARITY_SCALES) * (len(PARITY_DEGREES) - 1)


def test_the_owner_does_not_price_overwhelming_apart_from_success():
    """Opposing folds Overwhelming and Success to 'Meets' (the section 2.6 table has no fourth band) and
    maps it back to Success; that round trip is lossless only while the price ignores the difference."""
    for scale in ops.MENDING_OB:
        assert ops.price_mending(scale, "Overwhelming") == ops.price_mending(scale, "Success")


@pytest.mark.parametrize("aim", ["self", "prac", "other"])
def test_collective_and_opposed_mending_refuse_own_configuration_aim(aim):
    """Only `attempt_mending` routes an own-configuration Mending to the resting point. The other two
    sites name no routing for it, so a target that aims at a participant's own configuration is
    refused instead of silently taking the elastic path."""
    target = {"scale": "Relational", "configuration_of": aim}
    w = _World()
    with pytest.raises(ValueError, match="OWN configuration"):
        col.attempt_collective_operation([_Practitioner("prac", ts=60), _Practitioner("other")],
                                         "Mending", target, world=w, rng=random.Random(0))
    with pytest.raises(ValueError, match="OWN configuration"):
        opp.resolve_opposing_operations(_Practitioner("prac"), _Practitioner("other"), "Mending",
                                        target, world=w, rng=random.Random(0))
    assert w.practitioners == {}, "a refused Mending must not have touched any state"


def test_a_non_mending_working_ignores_configuration_of():
    """The refusal is Mending's: the field means nothing to a Weaving."""
    target = {"scale": "Relational", "configuration_of": "self"}
    col.attempt_collective_operation([_Practitioner("prac", ts=60), _Practitioner("other")],
                                     "Weaving", target, world=_World(), rng=random.Random(0))
    opp.resolve_opposing_operations(_Practitioner("prac"), _Practitioner("other"), "Weaving",
                                    target, world=_World(), rng=random.Random(0))


def test_owner_refuses_an_unpriced_scale_and_an_unknown_degree():
    with pytest.raises(ValueError, match="mending_priced_scale"):
        ops.price_mending("Object", "Success")
    with pytest.raises(ValueError, match="four-band"):
        ops.price_mending("Relational", "Meets")


def test_rolled_collective_and_opposed_mending_never_cost_coherence():
    """Unforced dice: ED-871 holds at every degree the collective and opposed paths roll, and the
    opposed MS delta is the owner's 0, not the table's proxy. Asserts it asserted."""
    seen = set()
    for seed in range(60):
        w = _World()
        r = col.attempt_collective_operation(_collective_actors(), "Mending",
                                             {"scale": "Structural"}, world=w,
                                             rng=random.Random(seed))
        if r.operation_result is not None:
            seen.add(("collective", r.operation_result.degree))
            assert r.operation_result.coherence_delta == 0
            # Only the working's own events: a Leap's blanket Partial/Failure -1 (C-TW-3, a known
            # separate defect in `_resolve_operation`) may stress a participant before it.
            assert not [e for s in _states(w).values() for e in s["log"]
                        if e["kind"] == "stress" and e["source"].startswith("Collective")], \
                "a collective Mending stressed a participant"
        w = _World()
        o = opp.resolve_opposing_operations(_Practitioner("a", spirit=3, ts=50),
                                            _Practitioner("b", spirit=2, ts=40), "Mending",
                                            {"scale": "Structural"}, world=w,
                                            rng=random.Random(seed))
        seen.add(("opposing", o.a_degree))
        assert o.a_consequences["coherence_delta"] == o.b_consequences["coherence_delta"] == 0
        assert o.ms_delta == 0
    collective_degrees = {d for s, d in seen if s == "collective"}
    assert "Failure" in collective_degrees and collective_degrees - {"Failure"}, seen
    assert {d for s, d in seen if s == "opposing"} >= {"Meets", "Failure"}, seen


# ─── (e) R-14 routing in collective and opposing ─────────────────────────────────────────────────

_STRUCTURAL = {"scale": "Structural"}


def _taken(w, actor_id):
    s = coh.get_state(actor_id, world=w)
    return 0 if s is None else (s.resting_point - coh.RESTING_POINT_START) + s.elastic_displacement


@pytest.mark.parametrize("gain", ops.RESILIENCE_GAIN_SWEEP)
def test_collective_and_opposing_route_cost_through_resilience(gain, monkeypatch):
    monkeypatch.setattr(ops, "RESILIENCE_GAIN", gain)
    # Collective: one lattice, a plain Anchor and a resilient Helper, both Leaping on one seed.
    w = _World()
    r = col.attempt_collective_operation(
        [_Practitioner("plain", spirit=3, ts=60), _Practitioner("steady", spirit=3, ts=60 - 1,
                                                                resilience=1)],
        "Weaving", _STRUCTURAL, world=w, rng=random.Random(0))
    assert r.leap_results == {"plain": True, "steady": True}, "the planted pair did not both Leap"
    plain, steady = _taken(w, "plain"), _taken(w, "steady")
    assert plain > 0, "the planted working must cost something"
    assert r.operation_result.coherence_delta == -plain     # the reported cost is the Anchor's
    # Opposing: the same side, same seed, once plain and once resilient; the roll is untouched.
    taken = {}
    for label, res in (("plain", None), ("steady", 1)):
        w2 = _World()
        o = opp.resolve_opposing_operations(_Practitioner("a", spirit=3, ts=50, resilience=res),
                                            _Practitioner("b", spirit=2, ts=40), "Weaving",
                                            _STRUCTURAL, world=w2, rng=random.Random(0))
        taken[label] = (o.a_degree, o.b_degree, _taken(w2, "a"), o.a_consequences["coherence_delta"])
    assert taken["plain"][:2] == taken["steady"][:2], "resilience must not touch the roll"
    assert taken["plain"][2] > 0
    for d_plain, d_steady, cons in ((plain, steady, None),
                                    (taken["plain"][2], taken["steady"][2], taken["steady"][3])):
        if gain == 0:
            assert d_steady == d_plain
        else:
            assert d_steady < d_plain
            assert d_steady == -min(0, -d_plain + gain)
        if cons is not None:
            assert cons == -d_steady, "the consequences dict reports the cost actually applied"
