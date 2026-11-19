"""WHAT THE WORLD KEEPS OF A FIGHT: THE SCENE'S SHAPE (B14.15; `16_PESSIMIST_PC_C` 1, gates 1, 3 (the control is the commit's),
4 and 5's `first_blood` half).

The module folds its own trace into a `SceneShape` (`modules/combat/fight.py::scene_shape`), the seam returns it beside
`beat`, and `_eff_kill` puts it on the act's success Events as `Observation`s: `blows_landed` per party, and once per
scene `fight_rounds`, `first_blood` (when a blow landed) and `lead_changes`. They ride `Event.observed` as `fell_to` does
(B14.03: `rosters.yaml: observation_terms` is `epistemic.Seen`'s field list, not a roster of observation predicates).

B14.16 adds gate 2 (`test_fell_to_hand_names_the_prevailing_party`) and the `fell_to_hand` half of gate 5: a felled ACTOR's
`person.died` Event names the standing party, and `person_q.deed_doer` reads it before the `seen.who` pairing.
"""
from __future__ import annotations

import copy
import dataclasses
from types import SimpleNamespace

import pytest

from engine.dice_engine import draw
from engine.season.boot.realm import build_realm
from engine.season.data.matrix import Step, WriteClass
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.loop import effects_combat
from engine.season.queries import person_q
from engine.season.queries.inputs import PersonalCombatInput, PlayHost, SceneShape
from engine.season.seam.wrappers import combat
from engine.season.state.carriers import Act
from modules.combat import fight as entry

pytestmark = pytest.mark.combat

_QS = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")
SHAPE_PREDICATES = ("blows_landed", "fight_rounds", "first_blood", "lead_changes")


def _wound(by, victim, cumulative, damage=1, felled=False):
    return dict(kind="wound", by=by, victim=victim, damage=damage, source="exchange", wounds=0,
                cumulative=cumulative, felled=felled)


# ---------------------------------------------------------------------------------------------------------------------
# THE FOLD (instruction 3)
# ---------------------------------------------------------------------------------------------------------------------
def test_scene_shape_is_a_pure_fold_over_trace():
    """`scene_shape(trace, claimants, health_full)` is a function of its three arguments: a hand-built trace folds to
    hand-computed numbers; the trace is not written; a real scene's shape equals the fold of the trace the same scene
    returned; and the fold agrees with the engine's own tracker (the lowest Health a party reached is the Health he ends on,
    the wounds counted are the `wound` events). FALSIFIER: a count read off any other event kind (the `outcome` event below
    carries a `by`), a lead counted on a tie, or a fold that needs the Combatants."""
    a, b = "p_a", "p_b"
    full = {a: 40, b: 30}
    trace = [
        dict(kind="fight_start", A=a, B=b, weapon_A="arming", weapon_B="arming"),
        dict(kind="turn_start", turn=1, first=a),
        _wound(a, b, 5),            # b 25/30 = .83, a 1.0: a ahead (the first lead is not a change)
        dict(kind="outcome", by=a, hit=1),
        _wound(b, a, 12),           # a 28/40 = .70 < .83: b ahead (change 1)
        dict(kind="turn_start", turn=2, first=b),
        _wound(a, b, 25, felled=False),   # b 5/30 = .17 < .70: a ahead (change 2)
        dict(kind="yield", turn=2, by=b, accepted=True, refused=None),
        dict(kind="turn_start", turn=3, first=a),
    ]
    frozen = copy.deepcopy(trace)
    got = entry.scene_shape(trace, (a, b), full)
    assert isinstance(got, SceneShape) and dataclasses.is_dataclass(got)
    assert got == SceneShape(rounds=3, blows={a: 2, b: 1}, first_blood=a, lead_changes=2, nearest={a: 28, b: 5}), got
    assert trace == frozen, "the fold wrote its input"
    assert entry.scene_shape(tuple(trace), (a, b), full) == got
    # a scene with no blow: the rounds and nothing else (`first_blood` None, a zero for each party, the full Health)
    quiet = [dict(kind="turn_start", turn=1, first=a), dict(kind="turn_start", turn=2, first=b)]
    assert entry.scene_shape(quiet, (a, b), full) == SceneShape(
        rounds=2, blows={a: 0, b: 0}, first_blood=None, lead_changes=0, nearest=dict(full))
    # a tie is no lead and no change: a ahead (36 against 40), level (36 and 36), then b ahead (36 against 30): one change
    tie = [_wound(a, b, 4), _wound(b, a, 4), _wound(b, a, 10)]
    assert entry.scene_shape(tie, (a, b), {a: 40, b: 40}).lead_changes == 1
    assert entry.scene_shape(tie, (a, b), {a: 40, b: 40}).first_blood == a
    # the real scenes: the shape is the fold of the returned trace, and the tracker agrees with it
    checked = 0
    for seed in range(24):
        inp = PersonalCombatInput(claimants=(a, b), ends=(4, 3), wound_quantities=_QS)
        out = entry.fight(inp, draw.seeded(draw.H2("test_combat_scene_shape", seed)))
        full = {pid: pw.health_full for pid, pw in out.wounds.items()}
        assert out.shape == entry.scene_shape(out.trace, out.claimants, full), seed
        assert out.shape.rounds == out.rounds == sum(1 for e in out.trace if e["kind"] == "turn_start"), seed
        assert sum(out.shape.blows.values()) == sum(1 for e in out.trace if e["kind"] == "wound"), seed
        assert {pid: out.shape.nearest[pid] for pid in (a, b)} == {pid: out.wounds[pid].health_remaining for pid in (a, b)}, seed
        assert (out.shape.first_blood is None) == (sum(out.shape.blows.values()) == 0), seed
        checked += 1
    assert checked >= 24
    # the control the sweep can see: a fold over a stripped trace is not the same shape (the assertion observes what it excludes)
    assert any(entry.fight(PersonalCombatInput(claimants=(a, b), ends=(4, 3), wound_quantities=_QS),
                           draw.seeded(draw.H2("test_combat_scene_shape", s))).shape.lead_changes for s in range(24)), "no scene in 24 changed its lead"


# ---------------------------------------------------------------------------------------------------------------------
# THE SEAM AND THE EFFECT (instructions 4 and 5): a `fight` through RESOLVE, ENCOUNTER and WITNESS
# ---------------------------------------------------------------------------------------------------------------------
def _fought(aid, seed=1003, host=None, world=None, fan=None, witness=False, obs=None):
    """`p_low` fights `p_mid` on `tiny_world` at world seed `seed`: declared at RESOLVE, fought at ENCOUNTER (the driver's own
    two calls). Returns `(world, driver, declared, fought, outcome)`; the module's `CombatOutcome` is on `box`'s way out through a spy on
    the seam's entry lookup, so the test can fold the trace itself."""
    box = {}
    real = combat.entry_for

    def spy(prize, provider):
        found, refusal = real(prize, provider)
        if found is None:
            return found, refusal

        def fn(*args, **kw):
            box["out"] = found.fn(*args, **kw)
            return box["out"]
        return SimpleNamespace(fn=fn), refusal
    w = world or P.tiny_world()
    if world is None:
        w.world_seed = seed
        if fan is not None:
            w.fixtures = w.fixtures.sweep("fan_out_mode", fan)
        if obs is not None:      # `observation_deposit_mode`: shipped `actor`, so a bystander holds none of an Event's `observed`
            w.fixtures = w.fixtures.sweep("observation_deposit_mode", obs)
    d = SeasonDriver(w)
    md = w.fixtures.get("contest_max_depth")
    act = Act(id=aid, actor="p_low", verb="fight", payload={"subject": "p_mid"})
    combat.entry_for = spy
    try:
        declared = d.resolve(mint_token(w, WriteClass.ACTS), [act], md)
        fought = d.encounter(mint_token(w, WriteClass.ACTS), declared, md, host)
    finally:
        combat.entry_for = real
    if witness:
        w.log.extend(declared + fought)
        for e in declared + fought:
            d.act_of[e.id] = act
        w.step = Step.WITNESS
        d.witness(mint_token(w, WriteClass.INTERIOR), declared + fought)
    return w, d, declared, fought, box["out"]


def _shape_obs(events):
    return {e.kind: [o for o in e.observed if o.predicate in SHAPE_PREDICATES] for e in events}


def test_a_seed_1003_fight_carries_its_shape():
    """THE S1 PROBE RESTATED (U3 §6.2): one `fight` at world seed 1003, `p_low` on `p_mid`, through RESOLVE, ENCOUNTER and
    WITNESS. The scratch probe (`pS_season.py`, at 826b747) read 8 rounds, 5 wounds; its act id is not in the repository and
    the scene is keyed on the act id (the seam's seed is `H(world_seed, tick, actor, "contest:<prize>:<act id>")`), so the act
    id here, `x24`, is the first of a scan (`s1`, then `x0`..`x29`) whose scene runs 8 rounds as the probe's did. The
    numbers below are READ AT THIS TREE from the trace of that scene, folded by hand in the comments.

    The success Events (`person.died`, `body.changed`, `capability.raised`) each carry the scene's Observations once;
    `fight.declared` is RESOLVE's, written before any scene is fought, and carries none."""
    w, d, declared, fought, out = _fought("x24")
    assert [e.kind for e in declared] == ["fight.declared"]
    assert [e.kind for e in fought] == ["person.died", "body.changed", "capability.raised"], [e.kind for e in fought]
    # the trace, folded by hand: 8 turn_starts; wounds p_low->p_mid 3 (cum 3), p_mid->p_low 25, p_low->p_mid 24 (cum 27),
    # p_low->p_mid 27 (cum 54, felled); Health 40 each: p_low ahead, then p_mid ahead, then p_low ahead again (2 changes)
    assert sum(1 for e in out.trace if e["kind"] == "turn_start") == 8
    assert [(e["by"], e["cumulative"]) for e in out.trace if e["kind"] == "wound"] == [
        ("p_low", 3), ("p_mid", 25), ("p_low", 27), ("p_low", 54)]
    want = {("p_low", "blows_landed"): 3, ("p_mid", "blows_landed"): 1, ("p_low", "fight_rounds"): 8,
            ("p_low", "first_blood"): True, ("p_low", "lead_changes"): 2}
    assert _shape_obs(declared) == {"fight.declared": []}
    checked = 0
    for e in fought:
        got = {(o.subject, o.predicate): o.value for o in _shape_obs([e])[e.kind]}
        assert got == want, (e.kind, got)
        assert len([o for o in e.observed if o.predicate in SHAPE_PREDICATES]) == len(want), (e.kind, "carried twice", e.observed)
        checked += 1
    assert checked == 3
    assert sum(v for (pid, p), v in want.items() if p == "blows_landed") == 4
    # the seam's returned shape is the same numbers, as a dict (the way `beat` and `surrender` ride the result)
    assert out.shape == SceneShape(rounds=8, blows={"p_low": 3, "p_mid": 1}, first_blood="p_low", lead_changes=2,
                                   nearest={"p_low": 15, "p_mid": 0})
    # CONTROL, a scene that took no blow of one party and no lead change: the shorter scene `s1` (1 round, 2 blows by p_low)
    _w, _d, _dec, fought_s1, out_s1 = _fought("s1")
    assert out_s1.shape.rounds == 1 and out_s1.shape.blows == {"p_low": 2, "p_mid": 0} and out_s1.shape.lead_changes == 0
    for e in fought_s1:
        got = {(o.subject, o.predicate): o.value for o in _shape_obs([e])[e.kind]}
        assert got == {("p_low", "blows_landed"): 2, ("p_mid", "blows_landed"): 0, ("p_low", "fight_rounds"): 1,
                       ("p_low", "first_blood"): True, ("p_low", "lead_changes"): 0}, (e.kind, got)


def test_played_and_automated_scenes_carry_equal_observations():
    """GATE 4: a played `fight` and an automated one from equal choices carry equal Observations -- the module computes them
    from the same trace. Two hand-built fights on `build_realm(0)` (`test_rem31_grid_suspension.FIGHTS`' pairs), each fought at
    ENCOUNTER with no host and with a host playing everyone and engaging every turn; the fought Events are compared whole
    (`kind`, `observed`), and the PLAYABLE arm must have SUSPENDED (its decider was called) or the equality is by construction."""
    pairs = (("p_npc_035", "p_npc_072"), ("p_npc_005", "p_npc_083"))

    def arm(played):
        w = build_realm(0)
        d = SeasonDriver(w)
        calls = []

        def decide(view):
            calls.append(view.turn)
            return "engage"
        host = PlayHost(frozenset(w.persons), decide) if played else None
        acts = [Act(id=f"b1415_{i}", actor=x, verb="fight", payload={"subject": y}) for i, (x, y) in enumerate(pairs)]
        md = w.fixtures.get("contest_max_depth")
        declared = d.resolve(mint_token(w, WriteClass.ACTS), acts, md)
        fought = d.encounter(mint_token(w, WriteClass.ACTS), declared, md, host)
        return [(e.kind, e.observed) for e in fought], calls
    auto, _ = arm(False)
    played, calls = arm(True)
    assert calls, "the PLAYABLE arm never entered the suspension"
    assert played == auto
    checked = 0
    for kind, observed in auto:
        shape = [o for o in observed if o.predicate in SHAPE_PREDICATES]
        if kind in ("person.died", "body.changed"):
            assert {o.predicate for o in shape} >= {"fight_rounds", "blows_landed", "lead_changes"}, (kind, shape)
            checked += 1
    assert checked >= 2


def test_bystanders_hold_no_scene_shape_under_the_shipped_deposit_mode():
    """GATE 5, `first_blood` here and `fell_to_hand` in `test_the_hand_rides_the_death_and_reaches_only_who_it_was_deposited_to`.
    WHAT THE TREE DOES, asserted: WITNESS deposits an
    Event's `observed` under `observation_deposit_mode` (shipped `actor`: the act's actor alone), and it does not look at the
    admitting channel for a predicate that is not a `Seen` field; so under the shipped mode the one ledger that holds
    `(first_blood-holder, "first_blood", True)` is the actor's, and witnesses of the death admitted by the other channels hold
    none. The entry's constraint that `first_blood` reach only channels whose `observation_terms.supplied_by` includes `who`
    is NOT enforced by any mechanism in this tree and is not asserted: see the receipt. Read on the real WITNESS."""
    w, d, declared, fought, out = _fought("x24", fan="total", witness=True)
    holders = {p.id for p in w.persons.values()
               if any(c.predicate == "first_blood" and c.subject == "p_low" and c.value is True for c in p.ledger)}
    assert holders == {"p_low"}, holders
    witnesses = {p.id for p in w.persons.values() if any(c.predicate == "person.died" for c in p.ledger)}
    bystanders = witnesses - {"p_low", "p_mid"}
    assert bystanders, "no bystander witnessed the death: the exclusion above is vacuous"
    for pid in bystanders:
        assert not [c for c in w.persons[pid].ledger if c.predicate in ("first_blood", "blows_landed", "fight_rounds", "lead_changes")], pid
    # and the actor holds the whole shape: the counts and the name
    mine = {(c.subject, c.predicate): c.value for c in w.persons["p_low"].ledger if c.predicate in SHAPE_PREDICATES}
    assert mine == {("p_low", "blows_landed"): 3, ("p_mid", "blows_landed"): 1, ("p_low", "fight_rounds"): 8,
                    ("p_low", "first_blood"): True, ("p_low", "lead_changes"): 2}, mine


def test_the_chronicle_line_of_a_fight_names_its_shape():
    """Instruction 6, a render change only: where an act's Events carry `fight_rounds` the line appends
    `(n rounds, first blood X, k lead changes)`, X the person's name as the line names its actor; a scene in which no blow
    landed says no first blood was drawn; an act whose Events carry no `fight_rounds` gains nothing."""
    from engine.season.harness import chronicle as CH
    w, d, declared, fought, out = _fought("x24")
    act = d.act_of["x24"] if "x24" in d.act_of else next(iter(d.act_of.values()))
    log = declared + fought
    name = w.persons["p_low"].name
    assert CH._shapes(log, d.act_of, w.persons) == {act.id: f"(8 rounds, first blood {name}, 2 lead changes)"}
    rows = {act.id: {"depth": 1, "cross": [], "season": 0, "actor": "p_low"}}
    ls = CH.lines(log, d.act_of, rows, w.persons)
    assert ls[0]["shape"] == f"(8 rounds, first blood {name}, 2 lead changes)"
    assert f"(8 rounds, first blood {name}, 2 lead changes) | opens the chain" in CH.render(log, d.act_of, rows, w.persons)
    # no blow: the Events a scene with `first_blood` withheld carries read `no first blood`; and an act with no `fight_rounds` gains nothing
    bare = [e for e in declared]
    assert CH._shapes(bare, d.act_of, w.persons) == {}
    assert CH.lines(bare, d.act_of, rows, w.persons)[0]["shape"] == ""
    quiet = [dataclasses.replace(e, observed=tuple(o for o in e.observed if o.predicate != "first_blood")) for e in fought]
    assert CH._shapes(quiet, d.act_of, w.persons) == {act.id: "(8 rounds, no first blood, 2 lead changes)"}


# ---------------------------------------------------------------------------------------------------------------------
# THE HAND (B14.16; `16_PESSIMIST_PC_C` 2, gates 2 and 5's `fell_to_hand` half)
# ---------------------------------------------------------------------------------------------------------------------
def _scenes_where_the_actor_falls(want, obs="total", limit=None):
    """`want` scenes (`_fought`, act ids `h0`, `h1`, ...) in which the ACTOR `p_low` is felled and the subject `p_mid` stands,
    each as `(world, fought)`; and how many fights it took. `witness=True`: WITNESS deposits on the real driver; `fan_out_mode`
    `total` so the bystanders witness the death; `obs` is `observation_deposit_mode` (`total`: a bystander holds the Event's
    `observed`; `None`: the shipped `actor`, the act's actor alone)."""
    found, i = [], 0
    while len(found) < want and i < (limit or 8 * want):
        w, _d, _declared, fought, _out = _fought(f"h{i}", fan="total", witness=True, obs=obs)
        i += 1
        if "p_low" not in w.persons and "p_mid" in w.persons:
            found.append((w, fought))
    return found, i


def _killers(w, victim="p_low"):
    """`{bystander: deed_doer of his firsthand `person.died` claim on `victim`}`, the holder's own pairing read as
    `suffered_deeds` and `attributed_deeds` ask it."""
    out = {}
    for p in w.persons.values():
        if p.id in ("p_low", "p_mid"):
            continue
        seen = person_q._seen_index(p.ledger)
        for c in p.ledger:
            if c.predicate == "person.died" and c.subject == victim and not c.chain:
                out[p.id] = person_q.deed_doer(c, seen)
    return out


def test_fell_to_hand_names_the_prevailing_party(monkeypatch):
    """GATE 2 (the S7 probe restated, U3 §6.2): over 100 fights in which the ACTOR is felled, `deed_doer` on a bystander's
    `person.died` claim returns the standing party, `p_mid`. Before the change it returns `None` (the `seen.who` pairing
    refuses a subject seen acting in the lap) or the dead man. The `seen.who` pairing stands for every other case: where the
    SUBJECT is felled, the bystander's pairing still names the actor. CONTROL (observes the failure it excludes): with
    `hand_observed` withheld alone, the same scenes name `None` or `p_low`, never `p_mid`."""
    scenes, fought_n = _scenes_where_the_actor_falls(100)
    checked = 0
    for w, fought in scenes:
        killers = _killers(w)
        assert killers, "no bystander held the death: the scene proves nothing"
        assert set(killers.values()) == {"p_mid"}, killers
        died = [e for e in fought if e.kind == "person.died"]
        assert [(o.subject, o.value) for e in died for o in e.observed if o.predicate == "fell_to_hand"] == [("p_low", "p_mid")]
        checked += 1
    assert checked >= 100, (checked, fought_n)
    # the pairing stands for every other case: the subject felled, the bystander still names the actor
    others = 0
    for i in range(60):
        w, _d, _declared, fought, _out = _fought(f"h{i}", fan="total", witness=True, obs="total")
        if "p_mid" not in w.persons and "p_low" in w.persons:
            assert not [o for e in fought for o in e.observed if o.predicate == "fell_to_hand"], i
            got = _killers(w, "p_mid")
            assert got and set(got.values()) == {"p_low"}, (i, got)
            others += 1
    assert others >= 10, others
    # the control: the Observation withheld alone, the same scenes name nobody or the dead man
    monkeypatch.setattr(effects_combat, "hand_observed", lambda *a, **k: ())
    withheld = set()
    for i in range(fought_n):
        w, _d, _declared, _fought_, _out = _fought(f"h{i}", fan="total", witness=True, obs="total")
        if "p_low" not in w.persons and "p_mid" in w.persons:
            withheld |= set(_killers(w).values())
    assert withheld and withheld <= {None, "p_low"}, withheld


def test_the_hand_rides_the_death_and_reaches_only_who_it_was_deposited_to():
    """GATE 5, THE `fell_to_hand` HALF. WHAT THE TREE DOES, asserted, and what it cannot assert, stated.
    (1) The Observation `(p_low, fell_to_hand, p_mid)` rides the felled actor's `person.died` Event once and no other Event of
    the scene (not `body.changed`, the standing party's). (2) Under the shipped `observation_deposit_mode` (`actor`) it is
    deposited to the act's actor alone, and a felled actor is no longer a person: NO ledger holds it, and a bystander's
    `deed_doer` names nobody -- the hand is on the log and in no ledger until a mode deposits to witnesses. (3) Under `total`
    every co-located witness holds it from the admitting channel that supplies `who` (`firsthand`, presence), and a bystander
    names `p_mid`.
    NOT ASSERTED, and not built: that a `document_key`, `post_remit` or `chronicle` witness holds none. `loop/witness.py`
    deposits `Event.observed` per witness under the mode and never reads `observation_terms.supplied_by` for a predicate that
    is not a `Seen` field, and `tiny_world` has no such witness of a fight; (3)'s source check shows what the one channel
    present does, not that the others are excluded."""
    shipped_scenes, _n = _scenes_where_the_actor_falls(1, obs=None)
    assert shipped_scenes, "no scene in 8 felled the actor under the shipped mode"
    shipped, fought_s = shipped_scenes[0]
    died = [e for e in fought_s if e.kind == "person.died"]
    assert len(died) == 1
    assert [e.kind for e in fought_s if any(o.predicate == "fell_to_hand" for o in e.observed)] == ["person.died"]
    assert [(o.subject, o.value) for o in died[0].observed if o.predicate == "fell_to_hand"] == [("p_low", "p_mid")]
    assert not [c for p in shipped.persons.values() for c in p.ledger if c.predicate == "fell_to_hand"]
    assert set(_killers(shipped).values()) <= {None}, "a bystander named a hand under the shipped mode"
    total, _fought_t = _scenes_where_the_actor_falls(1)[0][0]
    held = {p.id: [c for c in p.ledger if c.predicate == "fell_to_hand"] for p in total.persons.values()}
    held = {pid: cs for pid, cs in held.items() if cs}
    assert set(held) - {"p_mid"}, "no bystander held the hand under `total`"
    for pid, cs in held.items():
        assert [(c.subject, c.value, c.source) for c in cs] == [("p_low", "p_mid", "firsthand")], (pid, cs)
