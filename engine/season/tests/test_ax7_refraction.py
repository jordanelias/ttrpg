"""v9 IN-15 -- `AX-7`'s DIVERGENCE FORMULA, REFRACTION, and its wiring into WITNESS's deposits.

`AX-7` (`architecture/meta/01_AXIOMS.md`, `ED-IN-0244`): what everyone else holds of an act may be
wrong, *"by channel, competence and prior belief"*; `H-36`: the divergence is receiver-side and the
emission is never distorted. REFRACTION (`decision/options.py::refracted_confidence`) is

    confidence' = floor(confidence * (1 - g*remove(channel)) * (1 - g*dissent) * competence + 1/2)

with `g` = `refraction_gain` (`H-199`, shipped at its control 0), `remove` the channel's source's place
in the ordinal of remove, `dissent` the receiver's firsthand prior disagreeing -- or, for the
event-kind and `seen` deposits of an act's own emission, the receiver's ledger making the act's
`requires` known-false for its ACTOR (`H-201`, the `test_h201_*` tests) -- `competence` 1 (`H-200`,
absent). `loop/witness.py::_refract` applies it to every deposit a person receives of an
act not their own.

THE PLAN'S FALSIFIER: one claim told through two channels deposits a different value or confidence;
at the formula's control the deposit equals today's. The realm-hash half is a scratch reading
recorded in the commit (`build_realm(0)` ×1 / ×3 at 0 equal the base); these tests are the tiny-world
half, each run at the control AND above it so a test that cannot see refraction cannot pass.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.rosters import CHANNEL_CLAIM_SOURCE, WITNESS_CHANNELS
from ..decision.options import channel_remove, dissents, refracted_confidence
from ..epistemic import SEEN_PREDICATE, observers_for
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries.person_q import said_of
from ..state.carriers import Act, Claim, Event, Tenure
from ..state.ids import H
from .test_told_by_channel import _transfer_into_hh

TELLER, NEAR, KNOTTED, HELD_CONF = "p_low", "p_mid", "p_king", 37


def _tell_hh(gain: float, plant=()):
    """`TELLER` (standing in `Hh`) tells what they hold firsthand of `Hh`'s grain, `(Hh, stores:grain,
    8)` at confidence 37 -- a value the default (100) cannot impersonate. `NEAR` stands in `Hh` and
    hears it by presence; `KNOTTED` stands in `R` and is knotted to the teller, so `witness_key`
    admits them. `plant` is `(pid, Claim)` pairs placed in ledgers first. Returns the world after
    WITNESS, and the telling Event."""
    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("refraction_gain", gain)
    w.add_tenure(Tenure("t_knot_in15", TELLER, KNOTTED, "knot", since=0))
    w.persons[TELLER].ledger.append(
        Claim("c_held", TELLER, "Hh", "stores:grain", 8, 0, "firsthand", HELD_CONF, "own"))
    for pid, c in plant:
        w.persons[pid].ledger.append(c)
    act = Act(id="a_tell_in15", actor=TELLER, verb="tell",
              payload={"subject": "Hh", "said": said_of(w.persons[TELLER].ledger, "Hh", w.fixtures)})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, TELLER, f"ev:news.told:{act.id}"), "news.told",
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    chans = dict(observers_for(w, ev, "all_five", list(w.persons)))
    assert chans.get(NEAR) == "co_located" and chans.get(KNOTTED) == "witness_key", (
        f"the fixture moved: {chans} -- the two hearers no longer hear through two channels")
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    return w, ev


def _told(w, pid):
    return [c for c in w.persons[pid].ledger if c.source == "told_by" and c.chain
            and (c.subject, c.predicate) == ("Hh", "stores:grain")]


def test_in15_the_shipped_gain_is_the_control():
    assert DEFAULT_FIXTURES.get("refraction_gain") == 0, "the shipped gain moved: restate H-199"


def test_in15_channel_remove_is_the_ordinal_of_remove_read_off_the_roster():
    """`remove` is the channel's SOURCE's place among the distinct `claim_source:` values in the
    precedence order: presence 0, a knot 1/3, a document and the public record 2/3 (one source, one
    remove), `post_remit`'s `inferred` 1. Checked against the roster, so a reordered roster is
    followed rather than contradicted."""
    got = [channel_remove(ch) for ch in WITNESS_CHANNELS]
    assert got[0] == 0.0 and got[-1] == 1.0 and got == sorted(got), got
    for a in WITNESS_CHANNELS:
        for b in WITNESS_CHANNELS:
            same = CHANNEL_CLAIM_SOURCE[a] == CHANNEL_CLAIM_SOURCE[b]
            assert (channel_remove(a) == channel_remove(b)) == same, (a, b)
    # The shipped roster, read as values (no roster literal here: `rosters.yaml` owns the list).
    assert channel_remove("co_located") == 0.0 and channel_remove("witness_key") == 1 / 3
    assert channel_remove("document_key") == channel_remove("chronicle") == 2 / 3
    assert channel_remove("post_remit") == 1.0


def test_in15_one_telling_through_two_channels_deposits_two_confidences():
    """THE PLAN'S FALSIFIER. One `Said`, two hearers, two channels: above the control the hearer who
    heard it through a knot holds it less firmly than the one in the room; at the control both hold
    the teller's own 37. The VALUE is the same for both (refraction moves confidence only), and so is
    everything but confidence. The event-kind claim -- THAT the telling happened, `AX-7`'s named
    deposit -- diverges the same way.

    MUTATION (run 2026-10-09): the told branch's `if refracting: tc = _refract(...)` deleted -- RED
    on the knotted hearer's told confidence (37, expected 31). Restored, GREEN."""
    checked = 0
    for gain, near_conf, knot_conf, knot_kind_conf in ((0.0, 37, 37, 100), (0.5, 37, 31, 83)):
        w, ev = _tell_hh(gain)
        near, knot = _told(w, NEAR), _told(w, KNOTTED)
        assert len(near) == 1 and len(knot) == 1, (gain, near, knot)
        assert near[0].value == knot[0].value == 8, "refraction moved a VALUE; it may move confidence only"
        assert (near[0].confidence, knot[0].confidence) == (near_conf, knot_conf), (
            f"at refraction_gain {gain} the room hears {near[0].confidence} and the knot "
            f"{knot[0].confidence}; expected {near_conf} / {knot_conf}")
        assert (near[0].chain, near[0].source) == (knot[0].chain, knot[0].source) == ((TELLER,), "told_by")
        kinds = {pid: [c.confidence for c in w.persons[pid].ledger if c.predicate == ev.kind]
                 for pid in (NEAR, KNOTTED)}
        assert kinds == {NEAR: [100], KNOTTED: [knot_kind_conf]}, (gain, kinds)
        checked += 1
    assert checked == 2


def test_in15_a_dissenting_firsthand_prior_lowers_the_told_copy():
    """THE PRIOR-BELIEF TERM, through WITNESS. Two hearers in the room (remove 0, so the channel term
    is silent): `NEAR` saw `Hh` hold 5, `p_other` holds nothing about it. Above the control the told
    8 lands at half confidence for the one it contradicts and whole for the other; at the control,
    37 for both.

    MUTATION (run 2026-10-09): `dissents` made to return `False` -- RED on NEAR's 19. Restored, GREEN."""
    prior = (NEAR, Claim("c_saw5", NEAR, "Hh", "stores:grain", 5, 0, "firsthand", 100, "own"))
    checked = 0
    for gain, near_conf in ((0.0, 37), (0.5, 19)):
        w, _ev = _tell_hh(gain, plant=(prior,))
        near, other = _told(w, NEAR), _told(w, "p_other")
        assert len(near) == 1 and len(other) == 1, (gain, near, other)
        assert (near[0].confidence, other[0].confidence) == (near_conf, HELD_CONF), (
            gain, near[0].confidence, other[0].confidence)
        checked += 1
    assert checked == 2


def test_in15_dissents_pairs_on_the_keys_the_tree_already_pairs_on():
    """`dissents`, unit by unit. A claim about the receiver on a `person_predicates` member is
    `agreement`'s pairing (`AX-7`'s *"(2) is revisable by (3)"* from the receiving end); a cell is
    `record`'s; a `seen` struct and an event-kind claim are never scored; hearsay is no prior."""
    p = P.tiny_world().persons[NEAR]

    def c(subject, predicate, value, source="firsthand", chain=()):
        return Claim(f"c_{subject}_{predicate}_{value}", p.id, subject, predicate, value, 0,
                     source, 100, "own", chain=chain)

    p.ledger.extend([c(p.id, "residence", "Hh"), c("Hh", "stores:grain", 5),
                     c("Hh", SEEN_PREDICATE, "a"), c("S", "stores:grain", 9, "told_by", ("p_low",))])
    told = dict(source="told_by", chain=("p_low",))
    cases = [
        (c(p.id, "residence", "S", **told), True),       # contradicts what p holds of themself
        (c(p.id, "residence", "Hh", **told), False),     # agrees
        (c("Hh", "stores:grain", 8, **told), True),      # contradicts a firsthand cell
        (c("Hh", "stores:grain", 5, **told), False),
        (c("Hh", SEEN_PREDICATE, "b", **told), False),   # not a cell: never scored
        (c("Hh", "transfer.made", True, **told), False),  # an event-kind claim: never scored
        (c("S", "stores:grain", 1, **told), False),      # the only prior is hearsay: no prior
        (c("R", "stores:grain", 1, **told), False),      # no prior at all
    ]
    assert [dissents(p, x) for x, _ in cases] == [want for _, want in cases]
    assert sum(1 for _, want in cases if want) >= 1


def test_in15_the_actor_is_never_refracted():
    """`AX-7`'s layer (2) -- the performer's own understanding -- is not this formula's. The actor of a
    transfer holds a firsthand prior (`S` held 999) that its own observation of `S` contradicts:
    above the control the actor's deposits are still whole, while `p_king`, who learns of the act
    only through the rung they hold (`document_key`, remove 2/3), holds every claim at 67.

    MUTATION (run 2026-10-09): `and actor_of(w, e) != pid` deleted from `refracting` -- RED on the
    actor's observation claim (50). Restored, GREEN."""
    checked = 0
    for gain, king_conf in ((0.0, 100), (0.5, 67)):
        w, d, out, e = _transfer_into_hh("p_king")
        w.fixtures = w.fixtures.sweep("refraction_gain", gain)
        actor = "p_other"
        w.persons[actor].ledger.append(
            Claim("c_prior999", actor, "S", "stores:grain", 999, 0, "firsthand", 100, "own"))
        d.witness(mint_token(w, WriteClass.INTERIOR), out)
        mine = [c for c in w.persons[actor].ledger if c.id != "c_prior999"]
        assert any(c.predicate == "stores:grain" for c in mine), "the actor observed nothing: vacuous"
        assert {c.confidence for c in mine} == {100}, (gain, [(c.predicate, c.confidence) for c in mine])
        king = w.persons["p_king"].ledger
        assert king and {c.confidence for c in king} == {king_conf}, (
            gain, [(c.predicate, c.confidence) for c in king])
        checked += 1
    assert checked == 2


def _kinds_and_seen(w, pid, e):
    """`pid`'s event-kind and `seen` claims of `e`, as `{predicate: [confidence, ...]}` -- the two
    deposits `H-201`'s act-level prior reaches. Ledgers start empty in `tiny_world`, so a planted
    prior (another predicate) is never among them."""
    out: dict = {}
    for c in w.persons[pid].ledger:
        if c.predicate in (e.kind, SEEN_PREDICATE):
            out.setdefault(c.predicate, []).append(c.confidence)
    return out


def test_h201_a_witness_who_held_the_actors_granary_empty_doubts_the_transfer_out_of_it():
    """`H-201`, THE PLAN'S CASE, THROUGH THE REAL FOLD AND WITNESS. `p_other` transfers 3 grain out of
    `S`, which it holds; `p_king` learns of it through `Hh`, the rung it holds (`document_key`,
    remove 2/3). In one world `p_king` already held, firsthand, `S` at 0 grain -- `transfer`'s
    `requires` (`stores(from, kind) >= amount`) is KNOWN-FALSE on its own ledger -- and in the other
    it held nothing. Above the control the doubting witness holds THAT the transfer happened, and
    what it saw of it, at a lower confidence than the otherwise identical one; at the control both
    are whole.

    MUTATIONS (run 2026-10-09), each RED here and restored GREEN: `dissents`' act-level term
    deleted (the doubter at 67, expected 33); its sign inverted, `not belief_contradicts(...)` (the
    plain witness lowered to 33 and the doubter whole); the dissent factor made `1 + g*dissent`
    (the doubter at 100); either deposit site's `prior_act` dropped in `loop/witness.py` (that
    claim alone at 67)."""
    prior = Claim("c_s_empty", "p_king", "S", "stores:grain", 0, 0, "firsthand", 100, "own")
    checked = 0
    for gain, plain, doubting in ((0.0, 100, 100), (0.5, 67, 33)):
        got = {}
        for planted in (False, True):
            w, d, out, e = _transfer_into_hh("p_king")
            w.fixtures = w.fixtures.sweep("refraction_gain", gain)
            if planted:
                w.persons["p_king"].ledger.append(prior)
            d.witness(mint_token(w, WriteClass.INTERIOR), out)
            got[planted] = _kinds_and_seen(w, "p_king", e)
        want = {False: plain, True: doubting}
        for planted in (False, True):
            assert set(got[planted]) == {e.kind, SEEN_PREDICATE}, (
                f"p_king holds {got[planted]} -- the event-kind or the `seen` claim is missing, and "
                "the comparison below would be vacuous")
            assert {x for v in got[planted].values() for x in v} == {want[planted]}, (gain, got)
        checked += 1
    assert checked == 2


def _act_seen_by_two(gain: float, kind: str, plant=(), verb: str = "build", subject: str = "W"):
    """`TELLER` performs `verb` on `subject` -- by default builds `W`: `build`'s `requires` is *the
    subject is a works AND THE ACTOR HOLDS IT* (`held_by:<actor>`), a cell the ACTOR binds, so this
    is where binding the wrong person shows. `NEAR` and `p_other` stand in the room (`co_located`,
    remove 0: the channel term is silent and only dissent can move a confidence). The Event is
    hand-built as `_tell_hh`'s is, of `kind`."""
    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("refraction_gain", gain)
    for pid, c in plant:
        w.persons[pid].ledger.append(c)
    act = Act(id=f"a_{verb}_h201", actor=TELLER, verb=verb, payload={"subject": subject})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, TELLER, f"ev:{kind}:{act.id}"), kind,
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    chans = dict(observers_for(w, ev, "all_five", list(w.persons)))
    assert chans.get(NEAR) == chans.get("p_other") == "co_located", (
        f"the fixture moved: {chans} -- the two witnesses are no longer in the room")
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    return w, ev


def test_h201_the_prior_binds_the_acts_actor_never_the_witness():
    """THE MISBINDING `belief_contradicts`' old default would have made -- *could I have done this*
    in place of *could the actor have*. `NEAR` holds, firsthand, that `TELLER` does not hold `W`;
    `p_other` holds that `p_other` ITSELF does not hold `W`, and nothing about `TELLER`. Above the
    control only `NEAR` is lowered: `p_other`'s belief about its own hands says nothing about the
    builder's. At the control both are whole.

    MUTATION (run 2026-10-09): `actor=act.actor` dropped from `dissents`' call -- RED: each witness
    is bound as the builder, so `NEAR` is no longer lowered (100, expected 50) and `p_other` would
    be. Restored, GREEN."""
    plant = ((NEAR, Claim("c_not_his", NEAR, "W", f"held_by:{TELLER}", False, 0, "firsthand", 100, "own")),
             ("p_other", Claim("c_not_mine", "p_other", "W", "held_by:p_other", False, 0,
                               "firsthand", 100, "own")))
    checked = 0
    for gain, near_conf in ((0.0, 100), (0.5, 50)):
        w, ev = _act_seen_by_two(gain, "site.built", plant)
        near, other = _kinds_and_seen(w, NEAR, ev), _kinds_and_seen(w, "p_other", ev)
        for got in (near, other):
            assert set(got) == {ev.kind, SEEN_PREDICATE}, (gain, got)
        assert {x for v in near.values() for x in v} == {near_conf}, (gain, near)
        assert {x for v in other.values() for x in v} == {100}, (
            f"at refraction_gain {gain} p_other was lowered to {other} by a belief about ITS OWN "
            "hands -- the witness was bound as the actor")
        checked += 1
    assert checked == 2


def test_h201_a_refusal_is_not_doubted_by_a_belief_that_it_could_not_happen():
    """The act-level prior bears on a deposit reporting the act HAPPENING -- a kind on the row's
    `emits:` and not on its `emits_on_refusal:` (`loop/driver.py`'s test for a refusal). A witness
    who believed the act could not happen and sees it refused holds the refusal whole; the same
    witness seeing it succeed is lowered (the control that the world can lower at all). Two arms,
    one per clause of `loop/witness.py::_happened`: `build.refused` is on no `emits:`; `tell`'s
    `news.untold` is on BOTH columns, so only the refusal clause excludes it. ⚠ The `tell` prior is
    PLANTED: `(Hh, claim.held, False)` is a `LEDGER_DERIVED_STEMS` read WITNESS never deposits, so in
    a run no ledger makes `tell`'s `requires` known-false and that clause is a guard for the row's
    shape, observed here and nowhere else.

    MUTATION (run 2026-10-09): the refusal clause dropped from `_happened` -- RED (`news.untold`
    lowered to 50). Restored, GREEN."""
    arms = (
        ("build", "W", "site.built", "build.refused",
         Claim("c_not_his", NEAR, "W", f"held_by:{TELLER}", False, 0, "firsthand", 100, "own")),
        ("tell", "Hh", "news.told", "news.untold",
         Claim("c_nobody_holds", NEAR, "Hh", "claim.held", False, 0, "firsthand", 100, "own")),
    )
    checked = 0
    for verb, subject, happened, refused, prior in arms:
        w_ok, ev_ok = _act_seen_by_two(0.5, happened, ((NEAR, prior),), verb, subject)
        w_no, ev_no = _act_seen_by_two(0.5, refused, ((NEAR, prior),), verb, subject)
        ok, no = _kinds_and_seen(w_ok, NEAR, ev_ok), _kinds_and_seen(w_no, NEAR, ev_no)
        assert set(ok) == {happened, SEEN_PREDICATE} and set(no) == {refused, SEEN_PREDICATE}, (ok, no)
        assert {x for v in ok.values() for x in v} == {50}, (verb, ok)
        assert {x for v in no.values() for x in v} == {100}, (verb, no)
        checked += 1
    assert checked == 2


def test_in15_a_gain_outside_the_unit_interval_refuses():
    c = Claim("c_x", NEAR, "Hh", "stores:grain", 8, 0, "told_by", 37, "own")
    p = P.tiny_world().persons[NEAR]
    assert refracted_confidence(p, c, "co_located", 0.0) == 37
    for bad in (-0.1, 1.5):
        with pytest.raises(ValueError):
            refracted_confidence(p, c, "co_located", bad)
