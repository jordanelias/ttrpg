"""Plan position `15d` -- proceedings `19_PLAN.md` step 4 parts (a) and (b): HEARSAY MINTED FROM THE
CHANNEL. `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` §3.2 row 7.

(a) `epistemic.observers_for` returns `(person, channel)` pairs, ONE channel per person: the
    strongest admitting one, by `rosters.yaml: witness_channels`' declared order (the precedence).
(b) `loop/witness.py` sets the deposit's source from `witness_channels.claim_source` -- presence
    `firsthand`, a knot `firsthand_via_knot`, a document / a remit / the public record `told_by`.
(c) is 15b's and earlier: a told claim carries the TELLER'S OWN confidence. Confirmed here with a
    confidence the default cannot impersonate, which no test did before (every planted teller
    claim sat at 100, which IS `confidence_default`, so the assertion could not observe a default).

Each falsifier is `19_PLAN.md` step 4's own: *every deposit in a three-season run is still
firsthand* (the realm test); *a told claim carries full confidence when it should carry the
teller's own* (the telling test); and *breaks if wrong* -- *"an office-holder who was in the room is
downgraded ... Test both channels admitting one person"* (the precedence test, in both directions).

The fixture is `probes.tiny_world`: `p_low`, `p_mid`, `p_other` stand in the hearth `Hh`; `p_high`
in `S`; `p_king` in `R`. `p_other` holds `S` and moves grain into `Hh` -- the construction
`test_r8_4_document_key_reaches_a_non_author_through_a_store` already uses to reach `document_key`
on an act -- so whoever holds `Hh` is admitted by `document_key`, and ALSO by `co_located` exactly
when they stand in `Hh`.
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..data.rosters import CHANNEL_CLAIM_SOURCE, CLAIM_SOURCES, WITNESS_CHANNELS
from .. import epistemic as EP
from ..epistemic import CHANNEL_PREDICATES, SEEN_PREDICATE, observers_for
from ..harness import populated
from ..harness import probes as P
from ..loop import witness as WITNESS_MODULE
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Claim, Event, Tenure
from ..state.ids import H

ACTOR = "p_other"


def _transfer_into_hh(holder_of_hh: str):
    """`ACTOR` moves grain from `S` (which it holds) into `Hh` (which `holder_of_hh` holds), through
    the real fold. Returns `(w, driver, events, the transfer.made Event)`; nothing witnessed yet."""
    w = P.tiny_world()
    w.add_tenure(Tenure("t_src", ACTOR, "S", "hold", since=0))
    w.add_tenure(Tenure("t_dst", holder_of_hh, "Hh", "hold", since=0))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="tr1", actor=ACTOR, verb="transfer",
                         payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "transfer.made"), None)
    assert e is not None, (
        f"the fold emitted {[x.kind for x in out]} -- the transfer was refused, and nothing below "
        "is about the channels")
    w.log.extend(out)   # S19.5, as `SeasonDriver.season` does before WITNESS: a deposit's cause
    #                     must resolve to a logged Event

    assert CHANNEL_PREDICATES["document_key"](w, e, holder_of_hh), (
        f"`document_key` does not admit {holder_of_hh}, the holder of the rung the act wrote to -- "
        "every assertion below would be about some other channel")
    return w, d, out, e


def _sources_of(w, pid: str, e: Event) -> dict:
    """What `pid` came to hold about `e` through WITNESS: predicate -> the SET of sources, so two
    event-kind claims (one per subject under `both`) that disagreed would show as two. The ledgers
    start empty in `tiny_world`, so every such claim is this barrier's."""
    out: dict = {}
    for c in w.persons[pid].ledger:
        if c.predicate in (e.kind, SEEN_PREDICATE):
            out.setdefault(c.predicate, set()).add(c.source)
    return out


def test_15d_the_map_is_total_over_the_channels_and_the_precedence_puts_presence_first():
    """The data this position reads, checked for the two properties the step's prose states rather
    than for its exact spelling: every channel has a source from `claim_sources`, and presence --
    the one channel that gives `firsthand` -- heads the precedence, so nothing can outrank being in
    the room. (Membership is refused at import, in `data/rosters.py`; this pins the ORDER.)"""
    assert set(CHANNEL_CLAIM_SOURCE) == set(WITNESS_CHANNELS)
    assert set(CHANNEL_CLAIM_SOURCE.values()) <= set(CLAIM_SOURCES)
    head = WITNESS_CHANNELS[0]
    assert CHANNEL_CLAIM_SOURCE[head] == "firsthand", (
        f"the precedence head is {head!r}, sourcing {CHANNEL_CLAIM_SOURCE[head]!r} -- a person in "
        "the room would be credited to a weaker channel whenever that one also admits them")
    assert [c for c in WITNESS_CHANNELS if CHANNEL_CLAIM_SOURCE[c] == "firsthand"] == [head]


def test_15d_observers_for_reports_one_channel_per_person_the_strongest():
    """(a): `(person, channel)` pairs, one per person, and where two channels admit the same person
    the pair names the STRONGER. `p_low` stands in `Hh` AND holds it."""
    w, _d, _out, e = _transfer_into_hh("p_low")
    assert CHANNEL_PREDICATES["co_located"](w, e, "p_low"), "p_low is not in the room; fixture moved"
    pairs = observers_for(w, e, "all_five", list(w.persons))
    who = [pid for pid, _ch in pairs]
    assert len(who) == len(set(who)), f"a person is reported twice: {pairs}"
    assert all(ch in WITNESS_CHANNELS for _pid, ch in pairs), pairs
    assert dict(pairs)["p_low"] == "co_located", (
        f"p_low is admitted by `co_located` AND `document_key` and was credited to "
        f"{dict(pairs)['p_low']!r} -- the precedence did not credit the stronger")


def test_15d_breaks_if_wrong_two_channels_admit_one_person_and_presence_is_not_downgraded(
        monkeypatch):
    """`19_PLAN.md` step 4, *breaks if wrong*: *"If a remit maps to hearsay, an office-holder who
    was in the room is downgraded -- which is what the precedence is for. Test both channels
    admitting one person."* The same shape with `document_key` as the hearsay channel: `p_low` is
    in the room and holds the changed thing, and must hold what they saw `firsthand`.

    ⚠ BOTH DIRECTIONS, IN ONE TEST (§0.1 pt 2). With the precedence REVERSED -- a data edit, the
    roster order -- the same person in the same world is credited to `document_key` and holds the
    same Event `told_by`. So it is the declared order that decides, not an accident of which
    predicate ran first, and a precedence that stopped working would redden the first half."""
    w, d, out, e = _transfer_into_hh("p_low")
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    got = _sources_of(w, "p_low", e)
    assert got.get(e.kind) == {"firsthand"} and got.get(SEEN_PREDICATE) == {"firsthand"}, (
        f"p_low was IN THE ROOM and holds {got} -- downgraded because they also hold the changed "
        "thing, which is the failure the precedence exists to prevent")

    monkeypatch.setattr(EP, "WITNESS_CHANNELS", tuple(reversed(WITNESS_CHANNELS)))
    w2, d2, out2, e2 = _transfer_into_hh("p_low")
    assert dict(observers_for(w2, e2, "all_five", list(w2.persons)))["p_low"] == "document_key"
    d2.witness(mint_token(w2, WriteClass.INTERIOR), out2)
    got2 = _sources_of(w2, "p_low", e2)
    assert got2.get(e2.kind) == {"told_by"}, (
        f"with the precedence reversed p_low still holds {got2} -- the source is not being read "
        "off the credited channel, so the first half above could not have observed a downgrade")


def test_15d_a_document_holder_who_was_not_there_holds_the_event_as_hearsay():
    """(b): *a document ... gives told_by*. `p_king` stands in `R`, holds `Hh`, and learns of the
    transfer through `document_key` alone; the residents of `Hh` saw it."""
    w, d, out, e = _transfer_into_hh("p_king")
    assert not CHANNEL_PREDICATES["co_located"](w, e, "p_king"), "p_king is in the room; fixture moved"
    pairs = dict(observers_for(w, e, "all_five", list(w.persons)))
    assert pairs.get("p_king") == "document_key", pairs
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    king = _sources_of(w, "p_king", e)
    assert king.get(e.kind) == {"told_by"} and king.get(SEEN_PREDICATE) == {"told_by"}, (
        f"the holder of the changed rung, nowhere near it, holds {king} -- hearsay is not minted "
        "from the channel")
    for pid in ("p_low", "p_mid"):
        assert _sources_of(w, pid, e).get(e.kind) == {"firsthand"}, (pid, _sources_of(w, pid, e))


def test_15d_the_total_arm_credits_everyone_to_the_precedence_head_and_asks_no_predicate():
    """`total` is `H-33`'s control and uniform by definition (`seen_of`, `seen_subject`): every
    person, the SAME channel -- the precedence head -- including a person no predicate admits."""
    w, _d, _out, e = _transfer_into_hh("p_king")
    everyone = list(w.persons)
    pairs = observers_for(w, e, "total", everyone)
    assert [pid for pid, _ch in pairs] == everyone
    assert {ch for _pid, ch in pairs} == {WITNESS_CHANNELS[0]}, pairs
    assert not any(fn(w, e, "p_high") for fn in CHANNEL_PREDICATES.values()), (
        "p_high is admitted by some channel -- this line no longer shows `total` admitting a "
        "person nobody else would")


def test_15d_a_telling_is_hearsay_for_what_was_said_and_firsthand_for_that_it_was_said():
    """`19_PLAN.md` step 4 (b)'s telling clause and (c), on one telling.

    *"For a telling event specifically, even co-located hearers get told_by -- they heard it told,
    they did not see the thing."* The THING is the told channel's content claim, and a co-located
    hearer holds it `told_by`. The event-kind claim -- THAT the teller spoke -- stays `firsthand`
    for them: the step's own artifact is *"a witness who saw the speech directly holds it
    firsthand"*, and downgrading it is the downgrade *breaks if wrong* names.

    (c): the told claim carries the teller's own confidence. Planted at 37, which the default
    cannot impersonate -- asserted first, since a fixture of 37 would make the check vacuous."""
    w = P.tiny_world()
    teller, hearer, held_conf = "p_low", "p_mid", 37
    assert w.fixtures.get("confidence_default") != held_conf
    held = Claim("c_held", teller, "Hh", "stores:grain", 8, 0, "firsthand", held_conf, "own")
    w.persons[teller].ledger.append(held)
    act = Act(id="a_tell_15d", actor=teller, verb="tell", payload={"subject": "Hh"})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, teller, f"ev:news.told:{act.id}"), "news.told",
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    assert dict(observers_for(w, ev, "all_five", list(w.persons))).get(hearer) == "co_located"
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    mine = w.persons[hearer].ledger
    told = [c for c in mine if (c.subject, c.predicate, c.value) == ("Hh", "stores:grain", 8)]
    assert len(told) == 1 and told[0].source == "told_by", (
        f"a co-located hearer holds what was said as {[c.source for c in told]} -- they heard it "
        "told, they did not see it")
    assert told[0].confidence == held_conf, (
        f"the told claim carries {told[0].confidence}, not the teller's own {held_conf}")
    # BATCH-CLOSE FINDING (methodology-close Phase 1, antagonist): `RULINGS.yaml` CAT-3, CLOSED --
    # "STORE THE TELLER" -- shipped with the field but no falsifier. A deletion of `_act.actor` at
    # the told-deposit's `Claim(...)` construction (`loop/witness.py`) would turn no test red
    # without this line.
    assert told[0].teller == teller, (
        f"the told claim's teller is {told[0].teller!r}, not {teller!r} -- CAT-3's 'store the "
        "teller' is the one thing this deposit is FOR")
    spoke = [c for c in mine if c.predicate == "news.told"]
    assert spoke and {c.source for c in spoke} == {"firsthand"}, (
        f"the co-located hearer holds THAT the telling happened as {[c.source for c in spoke]} -- "
        "they saw the speech; only its content is hearsay")
    assert all(c.teller is None for c in spoke), (
        "the event-kind claim (that a telling happened) is not a told-channel deposit and must "
        "not carry a teller -- only the told channel's own content claim does")


def test_15d_falsifier_the_realm_holds_hearsay_no_telling_minted(monkeypatch):
    """`19_PLAN.md` step 4's falsifier: *"every deposit in a ... run is still firsthand."* The
    realm's first season is the cheapest fold-driven world where a non-presence channel is the
    strongest for anyone (`chronicle`/`post_remit`, measured at `15d`: 266 pairs; Carin's world
    has none, and every deposit in `headless.run(3, 0)` is still `firsthand` -- which is a fact
    about that world's geography, not the mechanism). One season, not three: three cost ~110 s and
    observe nothing one does not.

    ⚠ THE CONTROL IS IN THE TEST (§0.1 pt 4). The same season with every channel's source
    collapsed to `firsthand` -- the map neutralised, nothing else touched -- holds no `told_by`
    at all, so the hearsay is the map's and not the told channel's (which mints none in this
    world at seed 0, measured)."""
    def told_by_count() -> tuple:
        w = populated.build_realm(0)
        out = populated.run(1, 0, w=w)
        return out["claim_sources"].get("told_by", 0), sum(out["claim_sources"].values())

    live, total = told_by_count()
    assert live > 0, f"every one of {total} deposits is still firsthand -- no hearsay was minted"
    monkeypatch.setattr(WITNESS_MODULE, "CHANNEL_CLAIM_SOURCE",
                        {c: "firsthand" for c in CHANNEL_CLAIM_SOURCE})
    control, control_total = told_by_count()
    assert control == 0 and control_total == total, (
        f"with the map neutralised the season still holds {control} told_by claims (of "
        f"{control_total}, against {total}) -- the hearsay above is not the channel map's")
