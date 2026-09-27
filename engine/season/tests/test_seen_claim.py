"""The covering test file for `R8.1`'s `seen` claim -- partial observation, one struct per
(witness, event), deposited beside the event-kind and observation claims.

WHY A SEPARATE FILE: `CLAUDE.md` §0.4 clause 2 -- the mid-session run is the file covering the
edit, and this is the whole of this edit's subject. The ruling is `R8` in
`references/design_rulings_2026-09-06.md`; it is cited here for INTENT, and every behaviour below
is asserted by executing the loop, not by quoting the ruling.

The falsifier `R8.1` names -- *"a witness holds `(rung, seen, {stratum, who, ...})`; `Q2` fires for
everyone in the rung"* -- is `test_r8_falsifier_a_seen_claim_raises_q2_for_everyone_in_the_rung`,
which carries its own mutation arm. Cases 3 and 4, R8.5's document holder and the `total` arm are
produced by the loop; cases 1 and 2 are carrier-only checks and say so in their names.

Run: python -m pytest engine/season/tests/test_seen_claim.py -q
"""

from __future__ import annotations

import dataclasses

from ..data.requires import REQUIRES_STEMS
from ..data.rosters import OBSERVATION_TERMS, PERSON_PREDICATES, STRATA, TERMS_SUPPLIED_BY
from ..decision.options import agreement
from ..epistemic import SEEN_PREDICATE, Seen, seen_subject
from ..harness import headless as HL
from ..harness import probes as P
from ..loop import witness as WITNESS_MODULE
from ..loop.driver import SeasonDriver
from ..queries.person_q import LedgerReader
from ..queries.world_q import questions_for
from ..state.carriers import Act, Claim, Tenure


# ---------------------------------------------------------------------------
# One act, one barrier, on `probes.tiny_world`: `p_other` speaks at the hearth `Hh`, where
# `p_low` and `p_mid` also stand; `p_high` is at `S` and `p_king` at `R`. `speak` writes nothing,
# so the `seen` claim's subject falls through to the RUNG -- the case R8.1 calls load-bearing.
# The speech is ABOUT `p_king`, so the event-kind claim is about `p_king` and can raise Q2 for
# nobody in the hearth: any Q2 they get about `Hh` came from the `seen` claim alone.
# ---------------------------------------------------------------------------

ACTOR, RUNG, ABOUT = "p_other", "Hh", "p_king"


def _speak_and_witness(extra_tenures=()):
    w = P.tiny_world()
    for t in extra_tenures:
        w.add_tenure(t)
    d = SeasonDriver(w)
    d.matter([])
    out = d.resolve([Act(id="r8_speak", actor=ACTOR, verb="speak", payload={"subject": ABOUT})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "speech.made"), None)
    assert e is not None, (
        f"the fold emitted {[x.kind for x in out]}, not `speech.made` -- nothing below is about "
        "the `seen` deposit until the act itself executes")
    assert not [c for c in e.changes if c.subject], (
        f"`speech.made` now writes {[c.subject for c in e.changes]}; then the `seen` subject is "
        "the changed thing, not the rung, and this fixture no longer exercises the rung route")
    # ⚠ FIXED post-port: the real `season()` loop logs every resolved Event (`w.log.append(e)`,
    # driver.py "S19.5 -- ONE LOG, NOT TWO") BEFORE calling `witness()`, so later `causes=[e.id]`
    # deposits resolve against a known id. This fixture skipped that step and every deposit
    # `witness()` made about `e` raised `Forbidden` (S19.4, an unresolvable cause) the moment it
    # tried to log a claim caused by an Event that was never itself logged.
    for ev in out:
        w.log.append(ev)
    d.witness(out)
    return w, d, e


def _seen_claims(p, subject=None):
    return [c for c in p.ledger if c.predicate == SEEN_PREDICATE
            and (subject is None or c.subject == subject)]


def _in_rung(w, rung):
    return sorted(t.subject for t in w.tenures
                  if t.kind == "contain" and t.object == rung and t.live and t.subject in w.persons)


def test_r8_falsifier_a_seen_claim_raises_q2_for_everyone_in_the_rung():
    """⭐ `R8.1`'s FALSIFIER. A `seen` claim subjected to the rung raises `questions_for`'s Q2 for
    every person standing in it, and for nobody outside it -- through `c.subject in mine` and the
    `contain` Tenure, machinery that existed before this claim did.

    ⚠ EACH PERSON'S Q2 COMES FROM THEIR OWN LEDGER. Q2 never reads another person's claims; *"for
    everyone in the rung"* holds because every one of them WITNESSED (co-location) and so holds
    their own `seen` claim. The test asserts both halves: the deposit, and the question.

    ⚠ MUTATION ARM, RUN IN THE TEST RATHER THAN RECORDED: re-subject the claim to the ACTOR (the
    event-kind claim's old `H-79` shape, and what a naive deposit would do) and the listeners' Q2
    about the rung must vanish. If it does not, the assertion above could not observe the failure
    it excludes (§0.1 pt 2)."""
    w, d, e = _speak_and_witness()
    present = _in_rung(w, RUNG)
    listeners = [pid for pid in present if pid != ACTOR]
    assert len(listeners) >= 2, f"the fixture seats {present} in {RUNG}; the claim is vacuous"

    for pid in present:
        seen = _seen_claims(w.persons[pid], RUNG)
        assert len(seen) == 1, (
            f"{pid} stands in {RUNG} and holds {len(seen)} `seen` claims about it; R8.1 is one per "
            f"(witness, event)")
        qs = [q for q in questions_for(w, w.persons[pid], since=(w.tick, 0))
              if q.source == "claim_landed" and q.about == seen[0].id]
        assert qs and qs[0].referents == (RUNG,), (
            f"{pid} holds `({RUNG}, {SEEN_PREDICATE}, ...)` and no Q2 fired for it. Then a `seen` "
            "claim about a rung is inert on arrival, which is R8.4's last row")

    for pid in sorted(set(w.persons) - set(present)):
        assert not _seen_claims(w.persons[pid]), (
            f"{pid} stands outside {RUNG} and holds a `seen` claim about the speech -- the deposit "
            "is reaching past the channels that admit a witness")
        assert not [q for q in questions_for(w, w.persons[pid], since=(w.tick, 0))
                    if q.referents == (RUNG,)], f"{pid} got a Q2 about {RUNG} without being there"

    # the event-kind claim alone cannot have done this: it is about `ABOUT`, which no listener holds
    kind_claims = [c for c in w.persons[listeners[0]].ledger if c.predicate == e.kind]
    assert kind_claims and all(c.subject == ABOUT for c in kind_claims), (
        f"the event-kind claims are {[(c.subject, c.predicate) for c in kind_claims]}; if one is "
        f"about {RUNG} the Q2 above is not evidence for the `seen` route")

    # MUTATION ARM -- subject the `seen` claim to the actor instead of the rung.
    original = WITNESS_MODULE.seen_subject
    WITNESS_MODULE.seen_subject = lambda w_, e_, pid_, mode_: e_.subject
    try:
        w2, _d2, _e2 = _speak_and_witness()
    finally:
        WITNESS_MODULE.seen_subject = original
    for pid in listeners:
        assert _seen_claims(w2.persons[pid]), "the mutated arm deposited nothing; it tests nothing"
        assert not [q for q in questions_for(w2, w2.persons[pid], since=(w2.tick, 0))
                    if q.referents == (RUNG,)], (
            f"with the claim about the ACTOR, {pid} still got Q2 about {RUNG} -- then the rung "
            "subject is not what raised it and the falsifier above observes nothing")


def test_r8_seen_carries_no_verb_token_and_sits_beside_the_other_deposits():
    """Case 3 as the loop produces it: *doing something I can't name* -- `who` and `stratum` set,
    and no verb token anywhere in the value. The event-kind claim still carries `e.kind` beside it:
    `seen` is ADDED, it replaces nothing."""
    w, _d, e = _speak_and_witness()
    p = w.persons["p_low"]
    (c,) = _seen_claims(p, RUNG)
    v = c.value
    assert isinstance(v, Seen)
    assert v.who == ACTOR and v.stratum in STRATA and v.why is None, v
    tokens = {str(getattr(v, f.name)) for f in dataclasses.fields(v)}
    assert e.kind not in tokens and "speak" not in tokens, (
        f"the `seen` value {v} carries the verb; case 3 is a witness who CANNOT name what was done")
    assert [x for x in p.ledger if x.predicate == e.kind], (
        "the event-kind deposit is gone -- R8.1 adds `seen` BESIDE the existing deposits")
    assert c.source == "firsthand" and c.holder == "p_low", c


def test_r8_case_1_carrier_only_no_description_of_whoever_did_it():
    """⚠ STRUCTURAL CHECK ON THE CARRIER, NOT BEHAVIOURAL COVERAGE. This passes with the deposit
    deleted; the behavioural falsifier is `test_r8_falsifier_...` above.

    Case 1: *"I don't know the description of the person who did x"* -> `who=None, marks=()`.
    `marks=()` is SHOWN-AND-NOTHING-DESCRIBABLE, which is not the same state as `marks=None` (the
    channel shows no body). NO CHANNEL PRODUCES CASE 1: it needs a body shown without identity,
    i.e. a recognition producer, which `R8.2` defers. What this pins is that the struct can HOLD
    the state, round-trips through a ledger, and does not collapse it into a neighbour."""
    v = Seen(stratum="social", marks=(), who=None)
    assert v.who is None and v.marks == () and v.marks is not None
    assert v != Seen(stratum="social", marks=None, who=None), "() and None collapsed into one state"
    c = Claim("c1", "p", RUNG, SEEN_PREDICATE, v, 0, "firsthand", 100, "own")
    assert LedgerReader([c]).read(RUNG, SEEN_PREDICATE) == v
    assert hash(v) == hash(Seen(stratum="social", marks=(), who=None)), "the struct is not hashable"


def test_r8_case_2_carrier_only_and_unreached_by_the_loop():
    """⚠ THE FIRST HALF IS A STRUCTURAL CHECK ON THE CARRIER; THE SECOND HALF IS BEHAVIOURAL, AND
    WHAT IT ASSERTS IS ABSENCE. Case 2: *"someone looking like y did x"* -> `marks=(...,)`,
    `who=None`. The struct holds it. The loop does not produce it -- every channel that shows
    `marks` shows `who` with it, and `Person.marks` -- which `R8.4` recorded as having no writer
    while the field still existed -- was itself DELETED 2026-09-24 (`ED-IN-0261` item 1), so
    `_term_marks` now reads nothing at all rather than an unwritten field -- and the scan over a
    real run says so. The day a recognition producer lands, the scan goes red and this test must
    be rewritten into the positive case."""
    v = Seen(stratum="movement", marks=("scarred", "tall"), who=None)
    assert v.who is None and v.marks == ("scarred", "tall")
    assert v != Seen(stratum="movement", marks=("scarred", "tall"), who="p_x")
    shows_marks = [c for c, terms in TERMS_SUPPLIED_BY.items() if "marks" in terms]
    assert shows_marks and all("who" in TERMS_SUPPLIED_BY[c] for c in shows_marks), (
        "a channel now shows marks without identity; case 2 is reachable and this test is stale")
    r = HL.run(2, 0)
    seen = [c.value for p in r["world"].persons.values() for c in p.ledger
            if c.predicate == SEEN_PREDICATE]
    assert seen, "a two-season headless run deposited no `seen` claim; the scan below is vacuous"
    assert not [v for v in seen if v.who is None and v.marks], (
        "the loop produced case 2 -- a recognition producer exists now; see the docstring")


def test_r8_case_4_skulking_for_no_discernible_reason_produced_by_the_loop():
    """Case 4: *"they saw someone skulking around for no reason they could discern"* -> `stratum`
    alone, `why=None` -- PRODUCED BY THE LOOP, for a witness admitted only by `chronicle`.

    `release` is a `binding_decision` verb, so its Event is a matter of record and `chronicle`
    admits everyone. `p_king` stands at `R`, away from the hearth where `p_low` releases her tie to
    `p_mid`, holds nothing the act touched, and has no knot with her: he learns that a binding
    decision was taken and not by whom. `p_mid`, co-located, is the control -- same act, shown
    `who`, so the withholding is the channel's and not the deposit's."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter([])
    out = d.resolve([Act(id="r8_rel", actor="p_low", verb="release", payload={"subject": "p_mid"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "tenure.closed"), None)
    assert e is not None, f"the release did not execute: {[x.kind for x in out]}"
    for ev in out:
        w.log.append(ev)
    d.witness(out)
    (far,) = _seen_claims(w.persons["p_king"])
    assert far.value == Seen(stratum=far.value.stratum) and far.value.stratum in STRATA, (
        f"a chronicle-only witness was shown {far.value}; case 4 is `stratum` alone")
    assert far.value.why is None
    (near,) = _seen_claims(w.persons["p_mid"])
    assert near.value.who == "p_low" and near.value.stratum == far.value.stratum, (
        f"the co-located control was shown {near.value}; without `who` here the chronicle case "
        "above cannot be told apart from a deposit that withholds identity from everyone")


def test_r8_4_a_hold_tenures_own_id_is_expanded_not_deposited_raw():
    """`R8.4`'s office-conferral/revocation case, and the gap adversarial review found in the first
    `seen` writing: `release`/`revoke`/`confer` report a `hold` Tenure's OWN opaque id in
    `changes[]` (correct as a Receipt -- `H-71`'s others-half, `effects.py::_eff_release`), and
    `seen_subject` deposited that raw id unchanged. No live Tenure has a Tenure's own id as its
    `object`, so `mine` never contains it and Q2 could never fire for anyone -- the deposit was
    inert on arrival, exactly the failure mode `R8.5`'s Q2 assertion exists to catch for the
    document-holder case, uncaught here because nothing asserted it.

    `claim_subjects` already expands a `hold` Tenure id to `(holder, held)` for the same reason
    (`H-71`); `seen_subject` now shares that expansion via `_hold_tenure_ends` rather than carrying
    a second, divergent answer to *what is this deposit about*."""
    w = P.tiny_world()
    w.add_tenure(Tenure("t_src", ACTOR, "S", "hold", since=0))
    d = SeasonDriver(w)
    d.matter([])
    out = d.resolve([Act(id="r8_4_rel", actor=ACTOR, verb="release", payload={"subject": "S"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "tenure.closed"), None)
    assert e is not None, f"the release did not execute: {[x.kind for x in out]}"
    assert [c.subject for c in e.changes] == ["t_src"], (
        f"`tenure.closed` changes are {[c.subject for c in e.changes]}, not the Tenure's own id -- "
        "this test no longer exercises the raw-id case it was built for")
    mode = w.fixtures.get("fan_out_mode")
    subj = seen_subject(w, e, ACTOR, mode)
    assert subj != "t_src", (
        "`seen_subject` deposited the Tenure's own opaque id unchanged -- no live Tenure has a "
        "Tenure id as its `object`, so no witness's `mine` set can ever contain it and this claim "
        "is inert on arrival for everyone, the R8.4 gap adversarial review found")
    assert subj in (ACTOR, "S"), (
        f"the expanded subject is {subj!r}, not the released Tenure's holder or its object -- "
        "`_hold_tenure_ends` should resolve `t_src` to `(ACTOR, 'S')`")
    for ev in out:
        w.log.append(ev)
    d.witness(out)
    assert [q for q in questions_for(w, w.persons[ACTOR], since=(w.tick, 0))
            if q.source == "claim_landed"], (
        f"the released Tenure's own actor got no Q2 from the `seen` claim about {subj!r} -- "
        "the expansion resolved to something still unreachable")


def test_r8_5_a_document_holder_saw_only_that_the_document_changed():
    """`R8.5`, ratified: *"a co-located witness saw who acted; a document holder saw only that the
    document changed."* So a `document_key`-only witness holds an ALL-`None` struct, and it IS
    deposited -- its subject is what tells them something happened to what they hold.

    ⚠ AND THE SUBJECT IS THE CHANGED THING THE WITNESS HOLDS. A transfer writes `[S, Hh]`; `p_king`
    holds `Hh` and stands at `R`. The first writing subjected every witness to `changes[0]` (`S`),
    which is not in his Tenure objects, so his claim could raise no question -- the critic's 5d.
    The Q2 assertion is what observes that failure; the source-holder gets `S`."""
    w = P.tiny_world()
    w.add_tenure(Tenure("t_src", ACTOR, "S", "hold", since=0))
    w.add_tenure(Tenure("t_dst", "p_king", "Hh", "hold", since=0))
    d = SeasonDriver(w)
    d.matter([])
    out = d.resolve([Act(id="r8_tr", actor=ACTOR, verb="transfer",
                         payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "transfer.made"), None)
    assert e is not None, f"the transfer did not execute: {[x.kind for x in out]}"
    assert [c.subject for c in e.changes][:2] == ["S", "Hh"], (
        f"`transfer.made` changes {[c.subject for c in e.changes]}; the per-witness choice below "
        "is only observable when the destination is not first")
    for ev in out:
        w.log.append(ev)
    d.witness(out)

    mode = w.fixtures.get("fan_out_mode")
    (far,) = _seen_claims(w.persons["p_king"])
    assert far.value == Seen(), f"a document-only witness was shown {far.value}; R8.5 shows nothing"
    assert far.subject == "Hh" == seen_subject(w, e, "p_king", mode), (
        f"the destination's holder got a claim about {far.subject!r}, not the thing he holds")
    assert [q for q in questions_for(w, w.persons["p_king"], since=(w.tick, 0))
            if q.source == "claim_landed" and q.about == far.id], (
        "the document holder's `seen` claim raised no Q2 -- it is inert on arrival")
    assert seen_subject(w, e, ACTOR, mode) == "S", "the source's holder is not subjected to the source"

    (near,) = _seen_claims(w.persons["p_low"])
    assert near.value.who == ACTOR, (
        f"the co-located control was shown {near.value}; without `who` here the document case "
        "above cannot be told apart from a deposit that withholds identity from everyone")


def test_r8_the_total_arm_subjects_a_multi_change_event_uniformly():
    """`seen_subject`'s `total` branch, and the REAL falsifier for it -- found by adversarial
    review, not by running the wrong one first. `epistemic.py::seen_subject`'s docstring once cited
    `test_r7_two_persons_hold_different_things_and_at_total_they_cannot` as this branch's control;
    that test filters `_r7_witness_claims` down to claims whose predicate is a logged Event kind,
    `seen`'s predicate never is one, so a `seen` claim never reaches that comparison at all --
    deleting the whole `if mode == "total": return changed[0]` branch passes it unchanged.

    This is the case that branch exists for: the SAME `transfer` `test_r8_5...` uses, where the
    per-witness rule gives the destination's holder (`p_king`) a claim about `Hh` (what he holds)
    and the source's holder (`ACTOR`) a claim about `S` -- two DIFFERENT subjects for the one
    Event, which `total` must never produce, being `H-33`'s uniform-fan-out control."""
    w = P.tiny_world()
    w.add_tenure(Tenure("t_src", ACTOR, "S", "hold", since=0))
    w.add_tenure(Tenure("t_dst", "p_king", "Hh", "hold", since=0))
    d = SeasonDriver(w)
    d.matter([])
    out = d.resolve([Act(id="r8_tot_tr", actor=ACTOR, verb="transfer",
                         payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "transfer.made"), None)
    assert e is not None, f"the transfer did not execute: {[x.kind for x in out]}"
    assert [c.subject for c in e.changes][:2] == ["S", "Hh"], (
        "the destination is not first in `changes[]`; the uniformity this test checks is only "
        "observable when the per-witness rule would otherwise disagree with it")
    subjects = {pid: seen_subject(w, e, pid, "total") for pid in (ACTOR, "p_king")}
    assert len(set(subjects.values())) == 1, (
        f"`total` subjected two witnesses of one multi-change Event differently: {subjects}. "
        "`total` fans identically; a per-witness subject under it is the exact defect the "
        "per-witness rule was written to fix, recurring under the one arm meant to be immune to it")
    assert subjects[ACTOR] == "S", (
        f"the uniform `total` subject is {subjects[ACTOR]!r}, not the first changed thing `S` -- "
        "`seen_subject`'s `total` branch should return `changed[0]` regardless of witness")


def test_r8_the_total_arm_shows_every_term_to_every_witness():
    """`total` is `H-33`'s control -- every event to every person, maximal information. Under it
    `p_king`, whom NO channel admits to a speech at the hearth, still witnesses it and is shown
    `who`, `marks` and `stratum`. Under the shipped `all_five` arm the same person gets nothing,
    which is the control for this assertion."""
    from ..data.fixtures import DEFAULT_FIXTURES
    for mode, expect in (("total", True), ("all_five", False)):
        w = P.tiny_world(DEFAULT_FIXTURES.sweep("fan_out_mode", mode))
        d = SeasonDriver(w)
        d.matter([])
        out = d.resolve([Act(id="r8_tot", actor=ACTOR, verb="speak", payload={"subject": ABOUT})],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        for ev in out:
            w.log.append(ev)
        d.witness(out)
        got = [c.value for c in _seen_claims(w.persons["p_king"])]
        if not expect:
            assert not got, f"under {mode} p_king, admitted by no channel, holds {got}"
            continue
        assert len(got) == 1, got
        v = got[0]
        assert v.who == ACTOR and v.marks == () and v.stratum in STRATA and v.why is None, (
            f"under `total` the control arm showed {v}; every term a reader can fill must be shown")


def test_r8_3_seen_is_not_a_requirement_stem_and_agreement_does_not_pair_it():
    """`R8.3`, as the tree stands -- and both of its premises have MOVED, which this pins.

    (1) The ruling says a `seen` predicate *"is refused at load until it is declared"* by
    `_require_known_stem`. In this tree that function checks `verb_table.yaml`'s typed cells, never
    a deposit, so nothing refuses a ledger claim; `seen` is declared in `rosters.yaml:
    observation_terms` instead, and adding it to `REQUIRES_STEMS` would be wrong -- that set is
    what a verb's precondition may ASK, and it is read both ways against the readers' dispatch.

    (2) `agreement()` compares whole values, so two witnesses agreeing on `who` and differing on
    `marks` WOULD disagree -- the ruled price of the struct. Today it is not paid: `agreement`
    pairs only `person_predicates` and `seen` is not one, so a `seen` pair is not compared at all.
    The value-level half of the price is asserted directly."""
    assert SEEN_PREDICATE not in REQUIRES_STEMS
    assert SEEN_PREDICATE not in PERSON_PREDICATES
    assert tuple(f.name for f in dataclasses.fields(Seen)) == tuple(OBSERVATION_TERMS)
    a = Seen(stratum="social", marks=("tall",), who="p_x")
    b = Seen(stratum="social", marks=("short",), who="p_x")
    assert a != b, "whole-value equality no longer holds; R8.3's stated cost has changed shape"
    told = [Claim("t", "p", "p", SEEN_PREDICATE, a, 0, "told_by", 100, "own")]
    own = [Claim("o", "p", "p", SEEN_PREDICATE, b, 0, "firsthand", 100, "own")]
    assert agreement(told, own) == (0, 0, 0), (
        "`agreement` now pairs `seen` claims -- then R8.3's cost is PAID: two witnesses who agree "
        "on `who` and differ on `marks` score as disagreeing. Decide that deliberately")
