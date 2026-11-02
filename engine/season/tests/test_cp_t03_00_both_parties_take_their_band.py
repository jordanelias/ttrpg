"""CP-T03-00 -- BOTH PARTIES OF A FIGHT TAKE THEIR BAND (the REPAIR per `-08` AM-C-01).

`seam/ladder.py::party_degree` is the per-party walk; `combat_degree` (the act's band, the token
`writes_at`/`emits_at` key on) is the WORST of it over every `wound_state` entry; `_eff_kill` writes each
party -- the actor as well as the subject -- by his own band, each Subject earning his band's kind. And,
fold-wide, each emitted kind's Event carries only the changes of the Subjects that earned it
(`loop/resolve.py::_fold`), so WITNESS mints a kind only about those who earned it.

Every scene below is the shape `seam/wrappers/combat.py::_wound_state` lifts (`_scar_helpers.party_state`)
and its band is minted by the seam's own `degree_of`, not written into the test.

  FALSIFIER: a Felled actor with a Wounded subject emits both kinds -- `person.died` about the actor,
  `body.changed` about the subject -- and NO ledger holds `(subject, person.died, True)` about the living
  man, so IN-58's pairing (`person_q.deed_doer`) never names the actor his killer.
  MUTATION (run by hand at the build, reported in the commit body): the subject-only walk
  (`combat_degree` reading `states.get(subject)` alone and `_eff_kill` reading the subject alone) turns
  it red -- the actor stands and only `body.changed` is emitted.
  Also: both Untouched emits `contest.undecided`, and only then; both Felled; an attacker felled by his
  target names no killer (the limit `person_q.deed_doer` states); `march`'s per-kind Events.
"""
from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..data.rosters import FELLED, UNTOUCHED, WOUNDED
from ..harness import probes as P
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q, world_q
from ..seam import Resolution, combat_degree, degree_of, party_degree
from ..state.carriers import Act, Tenure
from ._scar_helpers import party_state
from .test_cp_t02_01_death_names_seats import CHURCH, CROWN, _march, _won_total

ACTOR, SUBJECT = "p_low", "p_mid"      # `tiny_world`: co-located, so a `fight` between them is admitted

_BAND_STATE = {FELLED: dict(felled=True, wounds=2, left=0),
               WOUNDED: dict(wounds=1, left=5),
               UNTOUCHED: dict()}


def _scene(actor_band, subject_band) -> dict:
    return {"wound_state": {SUBJECT: party_state(**_BAND_STATE[subject_band]),
                            ACTOR: party_state(**_BAND_STATE[actor_band])}}


def _fight(actor_band, subject_band, aid="cp300", fan="total"):
    """`ACTOR` fights `SUBJECT` on a scene taking each his band: through the real fold and gate at
    RESOLVE, the band minted by `degree_of` as `resolve()`'s seam branch mints it; then WITNESS.

    ⚠ WITNESSED UNDER `fan_out_mode = total` (H-33's control: everyone witnesses every Event), so a
    deposit assertion cannot pass by nobody seeing the fight. At the shipped `all_five` an act-caused
    Event is placed where its ACTOR stood (`world_q.event_place`), and a felled actor stands nowhere --
    the mixed fight reaches no co-located witness at all there, and "no ledger holds the living subject
    as dead" would hold vacuously."""
    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("fan_out_mode", fan)
    bodies = {pid: w.persons[pid].body for pid in (ACTOR, SUBJECT)}
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    raw = _scene(actor_band, subject_band)
    res = Resolution(degree_of(raw, SUBJECT, w.fixtures), raw)
    act = Act(id=aid, actor=ACTOR, verb="fight", payload={"subject": SUBJECT})
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, res)
    for e in out:
        w.log.append(e)
        d.act_of[e.id] = act       # as `resolve()` maps them: what `seen.who` is read from (IN-58)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return w, out, bodies


def _receipts(out, kind) -> list:
    return [c.subject for e in out if e.kind == kind for c in e.changes]


def _claims(w, subject, predicate) -> list:
    return [(p.id, c) for p in w.persons.values() for c in p.ledger
            if c.subject == subject and c.predicate == predicate and c.value is True]


def test_the_fights_band_is_the_worst_partys_and_each_partys_is_his_own():
    """`party_degree` is the per-party walk; `combat_degree` the worst over both, whichever party is
    named the subject (the subject must still be a party)."""
    checked = 0
    for a in (FELLED, WOUNDED, UNTOUCHED):
        for s in (FELLED, WOUNDED, UNTOUCHED):
            raw = _scene(a, s)
            assert party_degree(raw["wound_state"][ACTOR]) == a
            assert party_degree(raw["wound_state"][SUBJECT]) == s
            worst = FELLED if FELLED in (a, s) else (WOUNDED if WOUNDED in (a, s) else UNTOUCHED)
            assert combat_degree(raw, SUBJECT) == combat_degree(raw, ACTOR) == worst, (a, s)
            checked += 1
    assert checked == 9


def test_falsifier_a_felled_actor_beside_a_wounded_subject_emits_both_and_names_no_living_dead():
    w, out, bodies = _fight(FELLED, WOUNDED)
    kinds = [e.kind for e in out]
    assert "person.died" in kinds and "body.changed" in kinds, kinds
    assert {e.degree for e in out} == {FELLED}, "the fight's band is not the worst party's"
    assert ACTOR not in w.persons, "the felled actor still stands"
    assert SUBJECT in w.persons and w.persons[SUBJECT].body < bodies[SUBJECT], "the subject was not bled"
    assert [s for s in _receipts(out, "person.died") if s in bodies] == [ACTOR], _receipts(out, "person.died")
    assert _receipts(out, "body.changed") == [SUBJECT], _receipts(out, "body.changed")
    # THE DEPOSITS: the death is about the actor and the wound about the subject -- never the death
    # about the living subject.
    assert _claims(w, ACTOR, "person.died"), "control: nobody holds the actor's death"
    assert _claims(w, SUBJECT, "body.changed"), "control: nobody holds the subject's wound"
    assert _claims(w, SUBJECT, "person.died") == [], "a ledger holds the living subject as dead"


def test_in58_the_wounded_subject_is_paired_to_his_wounder_and_the_felled_attacker_names_no_killer():
    """IN-58's pairing in the mixed case: no holder's pairing names the actor as anybody's KILLER (there
    is no `person.died` claim about the subject to pair), the wound on the subject pairs to the actor,
    and the actor's own death pairs to nobody -- the limit `deed_doer` states (an attacker felled by his
    target is seen as `who` of his own death). `paired` and `limited` are asserted, so neither loop
    passes vacuously."""
    w, _out, _b = _fight(FELLED, WOUNDED)
    paired = limited = 0
    for p in w.persons.values():
        seen = person_q._seen_index(p.ledger)
        for c in p.ledger:
            if c.chain or c.predicate not in person_q.PAIRED_KINDS:
                continue
            doer = person_q.deed_doer(c, seen)
            if c.predicate == "person.died":
                assert c.subject != SUBJECT, f"{p.id} holds the living subject as dead"
                if c.subject == ACTOR:
                    assert doer is None, f"{p.id}'s pairing names {doer} the attacker's killer"
                    limited += 1
            elif c.predicate == "body.changed" and c.subject == SUBJECT and doer is not None:
                assert doer == ACTOR, f"{p.id} pairs the subject's wound to {doer}"
                paired += 1
    assert limited >= 1, "no holder carries the attacker's death firsthand: the limit was not observed"
    assert paired >= 1, "no holder paired the subject's wound to his wounder"


def test_a_felled_subject_beside_a_wounded_actor_names_the_actor_his_killer():
    """The ordinary kill, now with the attacker bled: the subject's death pairs to the actor, the
    actor's wound is about him, and nobody holds the actor dead."""
    w, out, bodies = _fight(WOUNDED, FELLED)
    assert SUBJECT not in w.persons and ACTOR in w.persons
    assert w.persons[ACTOR].body < bodies[ACTOR], "the attacker's own band was not written"
    assert _receipts(out, "body.changed") == [ACTOR]
    assert ACTOR not in _receipts(out, "person.died"), "the standing attacker rides the death's Event"
    killers = set()
    for p in w.persons.values():
        seen = person_q._seen_index(p.ledger)
        killers |= {person_q.deed_doer(c, seen) for c in p.ledger
                    if c.predicate == "person.died" and c.subject == SUBJECT and not c.chain}
    assert killers - {None} == {ACTOR}, killers


def test_both_felled_both_die_on_one_person_died_and_nothing_else_is_published():
    w, out, _b = _fight(FELLED, FELLED)
    assert ACTOR not in w.persons and SUBJECT not in w.persons
    assert sorted(s for s in _receipts(out, "person.died") if s in (ACTOR, SUBJECT)) == sorted((ACTOR, SUBJECT))
    assert "body.changed" not in [e.kind for e in out] and "contest.undecided" not in [e.kind for e in out]


def test_contest_undecided_is_emitted_when_both_are_untouched_and_only_then():
    checked = 0
    for a in (FELLED, WOUNDED, UNTOUCHED):
        for s in (FELLED, WOUNDED, UNTOUCHED):
            w, out, bodies = _fight(a, s, aid=f"cp300_{a}_{s}")
            kinds = [e.kind for e in out]
            both = a == s == UNTOUCHED
            assert ("contest.undecided" in kinds) == both, (a, s, kinds)
            if both:
                assert kinds == ["contest.undecided"], kinds
                assert {pid: w.persons[pid].body for pid in bodies} == bodies, "an untouched fight wrote"
            checked += 1
    assert checked == 9


def test_a_wounded_actor_beside_an_untouched_subject_is_the_one_written():
    """The attacker bled and his target untouched: before this item the fight read `Untouched` off the
    subject and wrote nobody; now the actor's body falls and the subject's does not."""
    w, out, bodies = _fight(WOUNDED, UNTOUCHED)
    assert [e.kind for e in out] == ["body.changed"]
    assert _receipts(out, "body.changed") == [ACTOR]
    assert w.persons[ACTOR].body < bodies[ACTOR] and w.persons[SUBJECT].body == bodies[SUBJECT]


def test_a_felled_actors_own_death_reaches_the_co_located_subject_at_the_shipped_fan():
    """B10-09 close one, D2: at the SHIPPED `all_five` the felled attacker's `person.died` -- an Event of the
    act that removed its own actor, carrying his receipt -- is placed where he stood when the act took him out
    (`world_q.event_place`, `World.departed_from`), so the untouched subject beside him holds it. Before the
    limb the Event had no place and reached no co-located witness. The total-fan arms above cannot see this."""
    w, out, _b = _fight(FELLED, UNTOUCHED, fan="all_five")
    assert w.fixtures.get("fan_out_mode") == "all_five"
    assert ACTOR not in w.persons and SUBJECT in w.persons
    (died,) = [e for e in out if e.kind == "person.died"]
    assert ACTOR in [c.subject for c in died.changes], "fixture: the death carries no receipt of the actor"
    assert world_q.place_of(w, ACTOR) is None, "`place_of` was widened; `reach` reads it about the dead"
    assert world_q.event_place(w, died) == w.departed_from(ACTOR, died.emitted_at) is not None
    assert SUBJECT in {pid for pid, _c in _claims(w, ACTOR, "person.died")}, (
        "the co-located subject does not hold the attacker's death")


def test_a_confer_onto_a_held_seat_puts_each_hold_on_its_own_kind_only():
    """Per-kind carriage beyond `fight`/`march` (item 4): a `confer` displacing an incumbent emits
    `tenure.opened` carrying ONLY the new hold and `tenure.closed` carrying ONLY the closed one. Before
    CP-T03-00 both Events carried both receipts."""
    from .test_g3_not_yours import _gov_world, _hold
    w, d = _gov_world()
    old = _hold(w, "off_duke")
    assert old is not None and old.subject == "p_high", "fixture: the duke's seat is not held"
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="cp300_cf", actor="p_king", verb="confer", via="off_crown",
                         payload={"subject": "off_duke", "office": "off_duke", "to": "p_mid"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    new = _hold(w, "off_duke")
    assert new is not None and new.subject == "p_mid" and not old.live, [e.kind for e in out]
    by = {e.kind: [c.subject for c in e.changes] for e in out}
    assert sorted(by) == ["tenure.closed", "tenure.opened"], by
    assert by["tenure.opened"] == [new.id], by
    assert by["tenure.closed"] == [old.id], by


def test_march_each_kinds_event_carries_its_earners_only_on_the_total_arm():
    """`march`'s deposits, declared: a total-arm `Won` kills every defender and moves the army. The
    `person.died` Event names the dead defenders only (no mover), `tenure.closed` the seats only, and
    `field.won`/`army.arrived` no seat. Before CP-T03-00 all four Events carried every receipt."""
    w = build_realm(0)
    defenders, attackers, seats, out = _won_total(w)
    assert defenders and attackers and seats, "fixture: no defender, attacker or defending seat"
    by = {e.kind: [c.subject for c in e.changes] for e in out}
    assert set(by["person.died"]) <= set(defenders) and set(defenders) <= set(by["person.died"]), by
    assert sorted(by["tenure.closed"]) == seats, by["tenure.closed"]
    assert not set(seats) & set(by["field.won"]) and not set(seats) & set(by["army.arrived"])
    assert set(defenders) <= set(by["field.won"]), "the losers' own outcome left the band's Event"
    assert set(by["army.arrived"]) - set(defenders), "no mover rides the arrival"


def test_march_control_the_shipped_arm_publishes_one_receipt_list_on_every_kind():
    """CONTROL at the shipped `scaled_by_degree` arm (nobody dies): every subject earns the band's same
    kinds, so `field.won` and `army.arrived` carry the identical receipts -- no march Event moves there."""
    w = build_realm(0)
    for t in w.persons["p_npc_037"].tenures:
        if t.kind == "contain" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_cp300_037_moved", "p_npc_037", "b_s_002_cottage", "contain", w.tick))
    assert w.fixtures.get("field_casualty_model") == "scaled_by_degree", "the shipped arm moved"
    res = Resolution("Won", {"parties": {"claimants": world_q.mustered(w, "set_s_014", CROWN),
                                         "subject_members": world_q.mustered(w, "set_s_036", CHURCH)},
                             "result": {"attacker_size_pct": 1.0, "defender_size_pct": 0.5}})
    out = _march(w, res)
    assert [e.kind for e in out] == ["field.won", "army.arrived"]
    assert out[0].changes and out[0].changes == out[1].changes
