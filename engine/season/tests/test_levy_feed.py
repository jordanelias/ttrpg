"""v9 IN-52 -- THE LEVY-TO-FIELD FEED, built SHIPPED OFF (`field_provisioning`, `H-241`).

A levied treasury PROVISIONS a field; it does not create troops (the design's §5, LF-1..LF-3, delegated-ruled
[ASSUMPTION; medium; Jordan to correct]). `settlements.provision` (`modules/settlements/provision.py`,
`entry: query`, reached here by role string as the adapter reaches it) bounds each side's troops by its
treasury at the larder's ration; the field adapter (`seam/wrappers/mass_battle.py::resolve`) hands them to
`mass_battle.resolve_field` as `troops_a`/`troops_b`; `_eff_march` debits what the field ate.

What each block proves, and the control that stops it passing vacuously:
  1. THE MODULE'S RULE: the control arm is `troops = weight`, `consumed = ()`; the arm on takes the MIN over
     ration kinds of whole rations (`//`), so a `max` or a `/` reddens here (the sides are chosen so both
     mutations give a different number).
  2. THE ADAPTER, ON A HAND-BUILT WORLD: `build_realm(0)` with stores PLANTED on the treasuries, because
     `requisition` executes 0 times in computed play (`H-163` limit 3(a)) and the realm's treasuries are
     empty. A short attacker treasury fields fewer troops than its mustered weight; an empty defender
     treasury fields 0, which the module's crash floor lifts (A16: a floor, not a refusal). The same call
     with the arm OFF fields Σ weight on both sides and consumes nothing -- the control.
  3. THE DEBIT, THROUGH THE REAL FOLD (RESOLVE -> ENCOUNTER): the attacker's treasury falls by exactly
     `consumed`; with the arm OFF it does not move.
  4. A PLANTED SECOND LEVY: two real `requisition` folds into the same treasury (each hand-built: its
     larder's grain is planted), a field between them -- the second field fields more troops than the first.
"""
import random
from types import SimpleNamespace

import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.manifest.registrar import MODULE_ENTRIES
from engine.season.queries import world_q
from engine.season.queries.inputs import ProvisionInput
from engine.season.state.carriers import Act
from engine.substrate import composition

# `build_realm(0)`'s fixture facts this file stands on (each re-asserted where it is used): the Crown's two
# at `set_s_014` march through `off_npc_033` (rung `terr_T1`, the treasury `requisition` fills) on
# `set_s_036`, where six of the Church of Solmund stand and the nearest held rung is `terr_T9`.
ACTOR, SEAT, ORIGIN, TARGET, DEFENDER = "p_npc_033", "off_npc_033", "set_s_014", "set_s_036", \
    "fac_church_of_solmund"
TREASURY_A, TREASURY_B = "terr_T1", "terr_T9"
LARDER = "set_s_001"                     # under `terr_T1`, inside the seat's purview


@pytest.fixture(autouse=True, scope="module")
def _module_entries_registered():
    """The adapter calls `mass_battle.resolve_field` through `MODULE_ENTRIES`, which the registrar fills at
    driver construction (`test_mass_battle_provider.py`'s fixture)."""
    SeasonDriver(build_realm(0))


def _provision(inp):
    return composition.require(world_q.PROVISION)(inp)


# ======================================================================================
# 1 -- THE MODULE'S RULE
# ======================================================================================

def test_the_control_arm_fields_the_whole_weight_and_consumes_nothing():
    """`on` false: `troops = weight` and `consumed = ()` whatever the treasury holds -- empty, short or
    full. The arm the feed ships at."""
    ration = (("grain", 2), ("salt", 1))
    for stores in ((), (("grain", 1),), (("grain", 100), ("salt", 100))):
        got = _provision(ProvisionInput(7, stores, ration, False))
        assert (got.troops, got.consumed) == (7, ()), (stores, got)


def test_the_bound_is_the_scarcest_kind_in_whole_rations():
    """`troops = min(weight, min over kinds of stores // ration)`. Grain 11 at 2 is 5 whole rations and salt
    3 at 1 is 3, so 3 troops, where `max` over kinds would read 5. The grain-bound side reads 3 (7 // 2),
    where `/` would read 3.5. Consumed is `ration x troops` per kind."""
    ration = (("grain", 2), ("salt", 1))
    salt_bound = _provision(ProvisionInput(8, (("grain", 11), ("salt", 3)), ration, True))
    assert (salt_bound.troops, salt_bound.consumed) == (3, (("grain", 6), ("salt", 3))), salt_bound
    grain_bound = _provision(ProvisionInput(8, (("salt", 9), ("grain", 7)), ration, True))
    assert grain_bound.troops == 3 and isinstance(grain_bound.troops, int), grain_bound
    assert grain_bound.consumed == (("grain", 6), ("salt", 3)), grain_bound
    rich = _provision(ProvisionInput(4, (("grain", 100), ("salt", 100)), ration, True))
    assert (rich.troops, rich.consumed) == (4, (("grain", 8), ("salt", 4))), (
        "a treasury richer than the side fields the side, never more people than it has")


def test_an_unprovisioned_side_fields_nobody_and_eats_nothing():
    """An empty treasury, a kind it does not hold, or a store driven negative: `troops = 0` and nothing is
    consumed (a zero debit would add a `kind: 0` key to `Rung.stores` for nothing). The crash floor is
    massbattle's, not this module's (A16)."""
    ration = (("grain", 2), ("salt", 1))
    for stores in ((), (("grain", 10),), (("grain", -4), ("salt", 5))):
        got = _provision(ProvisionInput(5, stores, ration, True))
        assert (got.troops, got.consumed) == (0, ()), (stores, got)
    # A ration with no positive kind bounds nothing.
    assert _provision(ProvisionInput(5, (), (("grain", 0),), True)).troops == 5


# ======================================================================================
# 2 -- THE ADAPTER, ON A HAND-BUILT WORLD
# ======================================================================================

def _world(on: bool, treasury_a=None, treasury_b=None):
    """`build_realm(0)` at the arm, with the two treasuries' stores PLANTED (hand-built: `requisition`
    executes 0 times in computed play, `H-163` limit 3(a), and the realm seeds no treasury)."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_provisioning", on)
    assert w.offices[SEAT].rung == TREASURY_A, "the march seat's treasury moved; re-pick the fixture"
    assert world_q.governing_hold(w, TARGET).object == TREASURY_B, "the target's held rung moved"
    if treasury_a is not None:
        w.rungs[TREASURY_A].stores = dict(treasury_a)
    if treasury_b is not None:
        w.rungs[TREASURY_B].stores = dict(treasury_b)
    return w


def _recording(monkeypatch):
    """The real `mass_battle.resolve_field` entry, wrapped to record the troops the adapter handed it."""
    from engine.season.seam.wrappers import mass_battle as MB
    real = MODULE_ENTRIES["mass_battle.resolve_field"]
    seen: list = []

    def fn(inp, rng, **kw):
        seen.append((tuple(sum(s) for s in inp.weights), kw))
        return real.fn(inp, rng, **kw)
    monkeypatch.setattr(MB, "entry_for", lambda prize, module: (SimpleNamespace(fn=fn), None))
    return seen


def _march_act(act_id="m1"):
    return Act(id=act_id, actor=ACTOR, verb="march", payload={"subject": TARGET}, via=SEAT)


def _provider_field(w, act):
    """The adapter called directly, the act planted in `w.acts` as the fold plants it before folding."""
    from engine.season.seam.wrappers.mass_battle import resolve
    w.acts.append(act)
    attackers = world_q.mustered(w, ORIGIN, "fac_crown")
    assert len(attackers) == 2, attackers
    return resolve(w, attackers, [act.id], "a field", subject=DEFENDER, rung=TARGET,
                   rng=random.Random(11))


def test_on_a_short_attacker_treasury_fields_fewer_than_its_weight_and_an_empty_defender_the_floor(
        monkeypatch):
    """THE ENTRY'S EXIT: one ration (grain 2, salt 1) for a side of weight 2 fields 1; the defender's empty
    treasury fields 0, which `resolve_field`'s `_MIN_TROOPS` lifts -- a floor, not a refusal (A16): the
    field still RESOLVES."""
    seen = _recording(monkeypatch)
    w = _world(True, treasury_a={"grain": 2, "salt": 1})
    r = _provider_field(w, _march_act())
    assert r["status"] == "RESOLVED" and r["unopposed"] is False, r
    (weights, kw), = seen
    assert weights == (2, 6), weights
    assert kw == {"troops_a": 1, "troops_b": 0}, kw
    assert kw["troops_a"] < weights[0], "a short treasury fielded the whole mustered weight"
    assert r["provision"] == ((TREASURY_A, (("grain", 2), ("salt", 1))), (TREASURY_B, ())), r["provision"]


def test_off_the_same_field_is_the_whole_weight_and_consumes_nothing(monkeypatch):
    """THE CONTROL: the same treasuries, the arm OFF -- Σ weight on both sides, nothing consumed."""
    seen = _recording(monkeypatch)
    w = _world(False, treasury_a={"grain": 2, "salt": 1})
    r = _provider_field(w, _march_act())
    (weights, kw), = seen
    assert kw == {"troops_a": weights[0], "troops_b": weights[1]} and weights == (2, 6), (weights, kw)
    assert r["provision"] == ((TREASURY_A, ()), (TREASURY_B, ())), r["provision"]


def test_off_the_field_is_the_none_keyword_field():
    """THE OLD-BEHAVIOUR CONTROL ON THE ENTRY ITSELF: with the arm off the adapter's troops equal Σ weight,
    so `resolve_field` with them returns exactly what it returns with `troops_a=troops_b=None` (today)."""
    from engine.season.seam.wrappers.mass_battle import field_input
    w = _world(False)
    attackers = world_q.mustered(w, ORIGIN, "fac_crown")
    defenders = world_q.mustered(w, TARGET, DEFENDER)
    inp = field_input(w, attackers, defenders, TARGET)
    fn = MODULE_ENTRIES["mass_battle.resolve_field"].fn
    weights = tuple(sum(s) for s in inp.weights)
    assert (fn(inp, random.Random(3)) == fn(inp, random.Random(3), troops_a=None, troops_b=None)
            == fn(inp, random.Random(3), troops_a=weights[0], troops_b=weights[1]))


# ======================================================================================
# 3 -- THE DEBIT, THROUGH THE REAL FOLD
# ======================================================================================

def _fold(w, *acts):
    """RESOLVE then ENCOUNTER over `acts` -- a march declares at RESOLVE and fights at ENCOUNTER
    (`test_march.py::_fold_one`); the events are logged as `SeasonDriver.season` logs them."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), 2)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, 2)
    w.log.extend(events)
    return events


@pytest.mark.parametrize("on", [True, False])
def test_the_field_eats_its_ration_from_the_treasury_only_when_on(on, monkeypatch):
    """LF-3: the attacker's treasury (grain 4, salt 1: one whole ration's worth of salt) falls by exactly what
    its one fielded troop ate; the defender's empty treasury does not move. OFF, neither moves."""
    seen = _recording(monkeypatch)
    w = _world(on, treasury_a={"grain": 4, "salt": 1})
    before_b = dict(w.rungs[TREASURY_B].stores or {})
    events = _fold(w, _march_act())
    kinds = {e.kind for e in events}
    assert kinds & {"field.lost", "field.won"}, sorted(kinds)
    assert len(seen) == 1, seen
    if on:
        assert seen[0][1] == {"troops_a": 1, "troops_b": 0}, seen
        assert w.rungs[TREASURY_A].stores == {"grain": 2, "salt": 0}, w.rungs[TREASURY_A].stores
    else:
        assert seen[0][1] == {"troops_a": 2, "troops_b": 6}, seen
        assert w.rungs[TREASURY_A].stores == {"grain": 4, "salt": 1}, w.rungs[TREASURY_A].stores
    assert dict(w.rungs[TREASURY_B].stores or {}) == before_b


# ======================================================================================
# 4 -- A PLANTED SECOND LEVY RAISES THE NEXT FIELD
# ======================================================================================

def _requisition(act_id, amount):
    return Act(id=act_id, actor=ACTOR, verb="requisition", via=SEAT,
               payload={"subject": LARDER, "kind": "grain", "amount": amount})


def test_a_second_levy_into_the_same_treasury_raises_the_next_fields_troops(monkeypatch):
    """Two REAL `requisition` folds into `terr_T1` -- hand-built, because none executes in computed play
    (`H-163` limit 3(a)): the larder's grain and the treasury's salt are planted. Levy 1 (grain 2) provisions
    one troop and the field eats it; levy 2 (grain 4) provisions two, and the next field fields two."""
    seen = _recording(monkeypatch)
    w = _world(True, treasury_a={"salt": 10})
    w.rungs[LARDER].stores = {"grain": 20}
    assert [e.kind for e in _fold(w, _requisition("rq1", 2))] == ["requisition.taken"]
    assert w.rungs[TREASURY_A].stores == {"salt": 10, "grain": 2}
    _fold(w, _march_act("m1"))
    assert w.rungs[TREASURY_A].stores == {"salt": 9, "grain": 0}, w.rungs[TREASURY_A].stores
    assert [e.kind for e in _fold(w, _requisition("rq2", 4))] == ["requisition.taken"]
    _fold(w, _march_act("m2"))
    first, second = (kw["troops_a"] for _w, kw in seen)
    assert (first, second) == (1, 2), seen
    assert w.rungs[TREASURY_A].stores == {"salt": 7, "grain": 0}, w.rungs[TREASURY_A].stores
