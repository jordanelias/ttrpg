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
from ..queries.person_q import said_of
from ..state.carriers import Act, Claim, Event, Said, Tenure
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
    # T1: WHAT A TELLING PASSES ON RIDES THE ACT (set at CHOOSE by `opening_set`; a hand-built act
    # sets it through the same owner, `said_of`).
    act = Act(id="a_tell_15d", actor=teller, verb="tell",
              payload={"subject": "Hh", "said": said_of(w.persons[teller].ledger, "Hh", w.fixtures)})
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
    assert told[0].chain == (teller,) and told[0].hops == 1, (
        f"the told claim's chain is {told[0].chain!r}: a first telling of a claim the teller holds "
        f"firsthand is a chain of exactly the teller (`T3b`)")
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
    at all, so the hearsay is the map's and not the told channel's.

    ⚠ TELLING WORKPLAN `T4`: THE TOLD CHANNEL MINTS IN THIS WORLD NOW, AND ITS DEPOSITS ARE NOT THE
    MAP'S. This read *"which mints none in this world at seed 0, measured"* until a telling named a
    hearer; at `T4` three told claims land in the realm's first season, and a told claim is
    `told_by` whatever the map says (the told branch sets its source itself). So each arm counts the
    map's `told_by` (no `chain`) apart from the told channel's (a `chain`), the control asserts the
    map's is zero, and the told channel's is asserted UNMOVED by neutralising the map."""
    # ⚠ RE-PINNED SEED 0 -> 5 AT `13d-iii` (2026-10-01): at seed 0 the first season stopped depositing
    # any chained told claim (3 before), and the precondition below needs one.
    # WHAT TWO TEN-SEED TABLES SHOW (Batch C close, fix lane 4, 2026-10-02). THE QUANTITY IS THIS
    # TEST'S OWN -- chained `told_by` claims (`live_channel`) after `populated.build_realm(s)` and
    # `populated.run(1, s)` -- measured on tree `5519cf52` (position 17, before `13d-iii`, and that
    # commit's own PARENT) and on the tree after it, one run per seed, the same script on both. The
    # tree after is `13d-iii` itself (`294a152d`), and the later commits to HEAD agree with it at every
    # seed on all three columns (chained, unchained, total), so the comparison is one commit's:
    #   seed                0   1   2   3   4   5   6   7    8   9
    #   chained, before     3   0   3   0   1   6   4   0    7   0
    #   chained, after      0   0   0   0   1   6   3   0   12   0
    # `13d-iii` LOWERED the chained count in 3 of the 10 seeds (0, 2 and 6 -- to 0 at seeds 0 and 2),
    # left it unchanged in 6 (seeds 1, 3, 7 and 9 at 0; 4 at 1; 5 at 6) and RAISED it in 1 (seed 8,
    # 7 -> 12); the ten sum to 24 before and 22 after. SEED 5 IS A SEED WHERE THE CHANNEL IS STILL
    # LIVE, AND ITS COUNT IS THE SAME ON BOTH TREES. THE MECHANISM BY WHICH `13d-iii` LOWERED THE
    # COUNT IN THE THREE SEEDS IS NOT ISOLATED. `told_by` claims WITHOUT a chain rose in all 10
    # seeds (1,113 -> 2,807 at seed 0; 79 -> 750 at seed 9), as did every seed's total claims.
    # SEED 0 ONLY, from the control run before these tables (one season, `5519cf52` against
    # `8b03e518`): executed `tell` acts 4 -> 6, so FEWER TELLINGS IS NOT THE CAUSE; the unchained
    # rise there includes `dispensation.issued` 0 -> 598 and `order.given` 75 -> 586 (binding-decision
    # Events, the kind `rosters.yaml: witness_channels` gives the public record `chronicle`; the
    # channel of each claim was not read; offices 24 -> 30 on the same change). The cause first
    # stated here -- *giving every seat a rung widened what `chronicle`/`post_remit` hand a hearer*
    # -- is PARTLY WRONG: `post_remit` mints `inferred`, not `told_by` (`rosters.yaml:
    # witness_channels`, since `17a`), `inferred` is 0 in the first season on BOTH trees, and
    # `chronicle` reads no seat; what grew is the number of binding-decision Events, because more
    # seats execute. THAT `loop/witness.py`'s dedup guard ("ALREADY SAW") is what eats the chained
    # deposits IS NOT ISOLATED EITHER.
    # SEED 5 IS A CHOICE, NOT THE LOWEST SEED STRONG ENOUGH: seed 4's one deposit already passes the
    # `live_channel > 0` guard below; 5 is the lowest seed with more than one, so the control's `==`
    # compares a count that is neither 0 nor 1. The assertions below are unmoved.
    # ⚠ RE-PINNED SEED 5 -> 4 AT IN-08's CELLS COMMIT (B-G), BY THE SAME RULE: at seed 5 the first
    # season stopped depositing any chained told claim (6 before). The chooser is re-scored on the
    # 15x7 basis, the cast's pursuits migrated and `challenge`/`accept` form, so the realm's act mix
    # moved. The same quantity, the same script, on the tree after:
    #   seed                0   1   2   3   4   5   6   7    8   9
    #   chained, after      0   0   0   0   4   0   0   0    7   0
    # Seed 4 is the lowest seed with more than one; the mechanism by which the count moved per seed
    # is NOT isolated, as before. The assertions below are unmoved.
    # ⚠ RE-PINNED SEED 4 -> 18 AT `H-160` LIMIT 1 (IN-22's paying half), BY THE SAME RULE. THIS TIME
    # THE MECHANISM IS ISOLATED: seed 4's four chained claims were all one telling of
    # `(b_s_036_cathedral, stores:grain, 0)` by `p_npc_037`, a read he held from his OWN REFUSED
    # `transfer` out of that hearth. `transfer`'s first alternative is now `remit:issue`, so a seated
    # holder gives through his seat out of its rung -- his refused transfer reads `terr_T1` instead,
    # and the hearth-stores telling is gone. Seed 4's acts are otherwise the same list (604 resolved,
    # 7 rows differ, every one a seated holder's `transfer`, still refused). The same quantity, the
    # same script, on the tree after:
    #   seed                0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17  18
    #   chained, after      0  0  0  0  0  0  0  0  0  0   0  0  0  0  0  0  0  0   9
    # Seed 18 is the lowest seed with more than one, and reads 9 on the tree before too. Unchained
    # `told_by` is unchanged at seeds 0-9. The assertions below are unmoved.
    SEED = 18

    def told_by_count() -> tuple:
        w = populated.build_realm(SEED)
        out = populated.run(1, SEED, w=w)
        told_by = [c for p in w.persons.values() for c in p.ledger if c.source == "told_by"]
        channel = sum(1 for c in told_by if c.chain)
        return len(told_by) - channel, channel, sum(out["claim_sources"].values())

    live, live_channel, total = told_by_count()
    assert live > 0, f"every one of {total} deposits is still firsthand -- no hearsay was minted"
    # `control_channel == live_channel` below passes at 0 == 0 and would then observe nothing (§0.1 pt 2)
    assert live_channel > 0, "the told channel minted nothing in the realm: the control below is vacuous"
    monkeypatch.setattr(WITNESS_MODULE, "CHANNEL_CLAIM_SOURCE",
                        {c: "firsthand" for c in CHANNEL_CLAIM_SOURCE})
    control, control_channel, control_total = told_by_count()
    assert control == 0 and control_total == total, (
        f"with the map neutralised the season still holds {control} map-sourced told_by claims (of "
        f"{control_total}, against {total}) -- the hearsay above is not the channel map's")
    assert control_channel == live_channel, (
        f"neutralising the map moved the told channel's deposits {live_channel} -> "
        f"{control_channel}: the told branch's source is not the map's to set")


def test_t1_what_hearers_receive_is_decided_at_choose_not_at_witness():
    """T1 (`workplans/2026-10-01-telling-workplan.md`). WHAT A TELLING PASSES ON IS FIXED WHEN IT IS
    CHOSEN. `opening_set` copies the teller's claim onto `Act.payload["said"]` through `said_of`;
    WITNESS reads that and never the teller's live ledger, so a claim landing in the teller's
    ledger BETWEEN the two cannot reach a hearer.

    THE FALSIFIER, IN ORDER: (1) the teller holds `(Hh, stores:grain, 8)` at confidence 37 and forms
    a `tell` through the real chooser; (2) a NEWER claim about `Hh` (value 99, confidence 100) is
    appended to the teller's ledger; (3) WITNESS runs. The hearer must hold the CHOSEN triple, and
    not the newer one. Against the pre-T1 `_told_content` -- which read the teller's live ledger at
    the barrier -- the hearer is handed the newer claim and this fails (observed once, by running
    this body with the old pick patched in; recorded in the T1 commit).

    ⚠ IT CHECKS THAT IT CHECKED (§0.1 pt 2). The assertion that the newer claim IS the teller's
    live pick (`LedgerReader`'s own comparator) is what makes the final inequality observable: a
    newer claim the live read would not have preferred could not distinguish the two behaviours."""
    from ..data.matrix import Step
    from ..decision import assemble
    from ..queries.person_q import LedgerReader
    from ..state.carriers import Question, Sensation

    w = P.tiny_world()
    teller, hearer, subject = "p_low", "p_mid", "Hh"
    tp = w.persons[teller]
    tp.ledger.append(Claim("c_held", teller, subject, "stores:grain", 8, 0, "firsthand", 37, "own"))
    # `T4`: a telling is told TO somebody the teller knows (`known_persons`), so the teller learns
    # the hearer exists -- the `existence` reading's shape -- or no `tell` is formed at all.
    tp.ledger.append(Claim("c_knows", teller, hearer, "exists:Person", 1, 0, "firsthand", 100, "own"))

    # (1) CHOOSE -- through the real chooser, so `opening_set` is what sets `said`.
    w.step = Step.DELIBERATE
    q = Question("q:t1", "need", (subject,), "prop")
    scenes = P.chooser(w, only=teller, verbs=frozenset({"tell"}))(
        tp, assemble(tp, q, w.fixtures.get("view_k")), Sensation(0), lambda: 5)
    tells = [a for s in scenes for a in s.acts if a.verb == "tell"]
    assert tells, "the chooser formed no `tell` for a teller holding a claim -- the fixture changed"
    act = tells[0]
    said = act.payload.get("said")
    assert said is not None and (said.subject, said.predicate, said.value, said.confidence) == (
        subject, "stores:grain", 8, 37), f"`said` on the Act is {said!r}, not the held claim"

    # (2) a NEWER claim about the subject lands in the teller's ledger AFTER CHOOSE.
    newer = Claim("c_newer", teller, subject, "stores:grain", 99, w.tick + 1, "firsthand", 100, "own")
    tp.ledger.append(newer)
    assert LedgerReader(tp.ledger).latest_about(subject) is newer, (
        "the newer claim is not the teller's live pick, so reading the live ledger would not have "
        "handed it to the hearer and this test could not tell the two behaviours apart")

    # (3) WITNESS.
    w.step = Step.WITNESS
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, teller, f"ev:news.told:{act.id}"), "news.told",
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])

    told = [c for c in w.persons[hearer].ledger
            if c.source == "told_by" and c.subject == subject]
    checked = len(told)
    assert checked >= 1, "the hearer was told nothing -- the arm under test never ran"
    for c in told:
        assert (c.predicate, c.value, c.confidence) == (said.predicate, said.value, said.confidence), (
            f"the hearer holds {(c.predicate, c.value, c.confidence)!r}, not what the telling "
            f"carried {(said.predicate, said.value, said.confidence)!r}")
        assert c.value != newer.value, (
            "the hearer received the claim that landed in the teller's ledger AFTER the telling was "
            "chosen -- WITNESS is reading the teller's live ledger again")


def test_t1_said_is_not_a_binding_operand():
    """`said` rides the payload and is dropped by `binding_of` like `harm` and `stages`: the grammar's
    vocabulary is closed on `requires_operands`, and a non-scalar must not reach either reader."""
    from ..data.requires import REQUIRES_OPERANDS, binding_of
    from ..state.carriers import Said
    assert "said" not in REQUIRES_OPERANDS
    out = binding_of("p", {"subject": "Hh", "said": Said("Hh", "stores:grain", 8, 37)})
    assert "said" not in out and out["subject"] == "Hh" and out["actor"] == "p", out


# ---------------------------------------------------------------------------------------------
# T3a (`workplans/2026-10-01-telling-workplan.md`, ED-IN-0282; `H-157`, `H-177`..`H-181`): HEARSAY
# WEIGHED WHEN READ. Until `T3b` a told claim was one hop and its origin its teller; since `T3b`
# hops are `len(Claim.chain)` and the origin is `chain[0]`. A claim with no chain weighs 1.0 and
# its origin is its holder.
# ---------------------------------------------------------------------------------------------

def _t3_fx(told_weight, regard_gain, rank_gain=None):
    """The T3 tests isolate `told_weight`, `regard_gain` and `rank_gain`, so `record_gain` is held at
    its CONTROL 0 here: several plant a told claim against a firsthand claim on one cell, which is
    a `record` pair (`T6`) and would lower that teller's weight at the shipped 0.5. `record` has its
    own falsifiers, `test_t6_*`."""
    from ..data.fixtures import DEFAULT_FIXTURES
    fx = (DEFAULT_FIXTURES.sweep("told_weight", told_weight).sweep("regard_gain", regard_gain)
          .sweep("record_gain", 0.0))
    return fx if rank_gain is None else fx.sweep("rank_gain", rank_gain)


def _t3_transfer_ops(rung):
    """`transfer`'s typed cell is `stores(from, kind) >= amount`: a claim `(rung, stores:grain, 5)`
    leaves it holding, `(rung, stores:grain, 0)` contradicts it."""
    return {"from": rung, "to": rung, "kind": "grain", "amount": 1}


def test_t3_a_firsthand_claim_holds_against_a_newer_told_claim_of_equal_confidence():
    """THE HEARSAY DISCOUNT, BOTH ARMS. The hearer saw `Hh` stocked (when 1, confidence 100); a
    teller `x` then told them it is empty (when 2, confidence 100). Under `(when, confidence)` --
    the pre-`T3a` comparator, and the CONTROL `told_weight` 1.0 -- the newer told value wins and
    `transfer` is KNOWN-FALSE; at the SHIPPED `told_weight` 0.5 the firsthand value's support is
    1.0 against the told one's 0.5, so what the hearer saw holds and nothing is contradicted.
    `record_gain` is held at its control 0 (`_t3_fx`): the told claim contradicts the firsthand
    one on the same cell, which is a `record` pair, and at the shipped 0.5 `x`'s weight would read
    0.25 here (`test_t6_*` observe that).

    MUTATION (run 2026-10-01, `T3a`): `LedgerReader._best` forced onto its `weigh is None` branch
    -- the shipped arm reads the told value and this goes RED on its first assertion. Restored,
    GREEN."""
    from ..data.verbs import VERB_TABLE
    from ..decision.options import teller_weight
    from ..epistemic import belief_contradicts
    from ..queries.person_q import LedgerReader

    w = P.tiny_world()
    p = w.persons["p_low"]
    assert not p.stance or all(r[0] != "x" for r in p.stance), "the hearer regards `x` already"
    seen = Claim("c_seen", p.id, "Hh", "stores:grain", 5, 1, "firsthand", 100, "own")
    told = Claim("c_told", p.id, "Hh", "stores:grain", 0, 2, "told_by", 100, "own", chain=("x",))
    p.ledger[:] = [seen, told]
    row, ops = VERB_TABLE["transfer"], _t3_transfer_ops("Hh")

    checked = 0
    shipped = teller_weight(p, _t3_fx(0.5, 0.5, 0.5))
    assert shipped(told) == 0.5 and shipped(seen) == 1.0, (shipped(told), shipped(seen))
    assert LedgerReader(p.ledger, shipped).read("Hh", "stores:grain") == 5, (
        "at the shipped told_weight a newer one-hop claim outranked what the hearer saw")
    assert not belief_contradicts(p, row, "Hh", ops, None, weigh=shipped)
    checked += 1

    control = teller_weight(p, _t3_fx(1.0, 0.0, 0.0))
    assert control(told) == 1.0
    assert LedgerReader(p.ledger, control).read("Hh", "stores:grain") == 0, (
        "at the control told_weight the newer claim must win, as before T3a")
    assert LedgerReader(p.ledger).read("Hh", "stores:grain") == 0
    assert belief_contradicts(p, row, "Hh", ops, None, weigh=control)
    checked += 1
    assert checked >= 1


def test_t3_unplanted_members_with_opposite_loyalty_reach_different_verdicts():
    """REGARD, READ FROM LOYALTY NOBODY PLANTED. In `build_realm(0)` two members of one faction
    whose stance rows toward its leader carry OPPOSITE signs (`populated`'s loyalty, through
    `cast.stance_from_loyalty`) each hold the same firsthand claim; the leader then tells both the
    contradicting value, newer. At `regard_gain` 0.5 the one who likes the leader credits him in
    full and believes him (`transfer` known-false); the one who dislikes him credits him below 1.0
    and keeps what they saw. At the control `regard_gain` 0 they agree.

    ⚠ `told_weight` IS HELD AT 1.0 HERE (its control value; this is not a control arm, since
    `regard_gain` is the variable), AND THAT IS FORCED, NOT CHOSEN. At the shipped
    0.5, a one-hop claim weighs at most 0.5 x 1.5 = 0.75 against a firsthand claim's 1.0 -- but
    ONLY WHILE `rank` reads 0 (`H-181`) AND `record` is neutral (`H-183`: no pair, or
    `record_gain` 0; a teller with a good record can reach 1.0). Here the told claim contradicts
    the firsthand one, a pair that would LOWER the leader's record at the shipped `record_gain`,
    so `record_gain` is held at its control 0 as well (`_t3_fx`) and no regard can make
    hearsay beat what the hearer saw (`H-179`'s default says so); regard then decides
    only between told claims. Against a firsthand claim the regard term is observable only where
    `told_weight * relation * record` can reach 1.0. The firsthand and told claims are planted (identically
    in both); the loyalty -- the variable under test -- is not.

    MUTATION (run 2026-10-01, `T3a`): `LedgerReader._best` forced onto its `weigh is None` branch
    -- both members believe the leader at 0.5 and this goes RED on the `differ` assertion.
    Restored, GREEN."""
    from collections import defaultdict
    from ..data.verbs import VERB_TABLE
    from ..decision.options import teller_weight
    from ..epistemic import belief_contradicts
    from ..queries.person_q import stance_toward

    w = populated.build_realm(0)
    toward = defaultdict(dict)
    for pid, p in w.persons.items():
        for r in p.stance:
            if len(r) >= 3 and r[0] in w.persons and r[0] != pid:
                toward[r[0]][pid] = stance_toward(p, r[0])
    pairs = []
    for leader, members in sorted(toward.items()):
        pos = sorted(m for m, s in members.items() if s > 0)
        neg = sorted(m for m, s in members.items() if s < 0)
        if pos and neg:
            pairs.append((leader, pos[0], neg[0]))
    assert pairs, ("no faction in build_realm(0) has members of opposite loyalty toward its "
                   "leader -- the unplanted premise is gone")
    row = VERB_TABLE["transfer"]
    checked = 0
    for leader, fond, hostile in pairs:
        rung = "r_t3"
        ops = _t3_transfer_ops(rung)
        verdict = {}
        for pid in (fond, hostile):
            p = w.persons[pid]
            p.ledger.append(Claim(f"c_t3_seen_{pid}", pid, rung, "stores:grain", 5, 1,
                                  "firsthand", 100, "own"))
            p.ledger.append(Claim(f"c_t3_told_{pid}", pid, rung, "stores:grain", 0, 2,
                                  "told_by", 100, "own", chain=(leader,)))
            verdict[pid] = tuple(
                belief_contradicts(p, row, rung, ops, None, weigh=teller_weight(p, fx))
                for fx in (_t3_fx(1.0, 0.5), _t3_fx(1.0, 0.0)))
        assert verdict[fond][0] != verdict[hostile][0], (
            f"{fond} (stance {toward[leader][fond]:+}) and {hostile} "
            f"(stance {toward[leader][hostile]:+}) reached the same verdict on {leader}'s word at "
            f"regard_gain 0.5: {verdict}")
        assert verdict[fond][0] is True and verdict[hostile][0] is False, verdict
        assert verdict[fond][1] == verdict[hostile][1] is True, (
            f"at the control regard_gain 0 the two must agree, and believe the newer claim: {verdict}")
        checked += 1
    assert checked >= 1


def test_t3_weigh_none_and_weigh_one_order_a_ledger_as_today():
    """THE COLLAPSE, OVER RANDOMISED LEDGERS. `weigh=None` and a `weigh` returning 1.0 for every
    claim must pick EXACTLY the claim the pre-`T3a` comparator picked -- `(when, confidence)`,
    strict `>`, first found wins a tie -- for `read` and `latest_about`. `when` and `confidence`
    are drawn from small ranges so ties are common: a tie is where a broken first-found rule shows.

    MUTATION (run 2026-10-01, `T3a`): the weighted branch's `key > best_key` written `>=` -- the
    last tied claim wins and this goes RED. Restored, GREEN."""
    import random
    from ..queries.person_q import LedgerReader

    def today(claims, match):
        best = None
        for c in claims:
            if match(c) and (best is None or (c.when, c.confidence) > (best.when, best.confidence)):
                best = c
        return best

    rng = random.Random(20261001)
    checked = ties = 0
    for trial in range(400):
        claims = []
        for i in range(rng.randint(1, 9)):
            told = rng.random() < 0.5
            claims.append(Claim(f"c{trial}_{i}", "h", rng.choice("AB"), rng.choice(("p", "q")),
                                rng.choice((0, 1, 2)), rng.randint(0, 2),
                                "told_by" if told else "firsthand", rng.choice((50, 100)), "own",
                                chain=(rng.choice(("x", "y")),) if told else ()))
        for subject in "AB":
            for predicate in ("p", "q"):
                m = lambda c, s=subject, pr=predicate: c.subject == s and c.predicate == pr
                want = today(claims, m)
                matches = [c for c in claims if m(c)]
                if want is not None and sum((c.when, c.confidence) == (want.when, want.confidence)
                                            for c in matches) > 1:
                    ties += 1
                for weigh in (None, lambda c: 1.0):
                    r = LedgerReader(claims, weigh)
                    assert r._best(m) is want, (trial, subject, predicate, weigh)
                    got = r.read(subject, predicate)
                    assert (got is want.value) if want is not None else got is not None
                    checked += 1
            want = today(claims, lambda c, s=subject: c.subject == s)
            for weigh in (None, lambda c: 1.0):
                assert LedgerReader(claims, weigh).latest_about(subject) is want
                checked += 1
    assert checked >= 1000 and ties >= 50, (checked, ties)


def test_t3_opening_set_hands_clause_4_the_teller_weight(monkeypatch):
    """THE WIRING: `opening_set` passes `teller_weight(p, fx)` to `belief_contradicts` whenever the
    person's ledger holds a told claim, so clause 4 is the weighed reader in play and not only in
    a test; a ledger with no told claim takes the plain reader (`weigh=None`), which orders it
    identically (`test_t3_weigh_none_and_weigh_one_order_a_ledger_as_today`). Spied through the
    module attribute every rebind already uses (`decision.options.belief_contradicts`)."""
    from ..decision import options as O
    from ..state.carriers import Question, View

    w = P.tiny_world()
    p = w.persons["p_low"]
    q = Question("q_wire", "claim_landed", ("Hh",), "")
    v = View(p.id, [], w.fixtures.get("view_k"), q)
    seen = []
    real = O.belief_contradicts

    def spy(pp, row, subject, operands, via=None, weigh=None, actor=None):
        seen.append(weigh)
        return real(pp, row, subject, operands, via, weigh=weigh, actor=actor)

    monkeypatch.setattr(O, "belief_contradicts", spy)

    p.ledger[:] = [Claim("c_seen", p.id, "Hh", "stores:grain", 5, 1, "firsthand", 100, "own")]
    O.opening_set(p, v, q, w.fixtures)
    assert seen, "opening_set never reached clause 4 -- the spy observed nothing"
    assert all(wt is None for wt in seen), "a ledger with no told claim was given a weigh"

    seen.clear()
    p.ledger[:] = [Claim("c_seen", p.id, "Hh", "stores:grain", 5, 1, "firsthand", 100, "own"),
                   Claim("c_told", p.id, "Hh", "stores:grain", 0, 2, "told_by", 100, "own",
                         chain=("x",))]
    O.opening_set(p, v, q, w.fixtures)
    assert seen, "opening_set never reached clause 4 -- the spy observed nothing"
    probe = Claim("c_probe", "h", "S", "stores:grain", 0, 0, "told_by", 100, "own", chain=("x",))
    assert all(callable(wt) for wt in seen), "a clause-4 call ran with weigh=None"
    # 0.25 = shipped `told_weight` 0.5 x `record` 0.5: `c_told` (by `x`) contradicts `c_seen` on one
    # cell, a pair (`T6`), and the closure `opening_set` hands over is the whole shipped one.
    assert {wt(probe) for wt in seen} == {0.25}, (
        "the weigh opening_set passed does not grade a told claim at the shipped told_weight and record")


# ---------------------------------------------------------------------------------------------
# T3b (`workplans/2026-10-01-telling-workplan.md`, ED-IN-0282): `Claim.chain` REPLACES `Claim.teller`.
# Hops, origin and the weighed reader all read the chain; `teller` is `chain[-1]`, derived.
# ---------------------------------------------------------------------------------------------

def test_t3b_a_two_hop_claim_weighs_less_than_a_one_hop_claim():
    """HOPS ARE READ FROM THE CHAIN, BOTH ARMS. The hearer holds two told claims about one cell with
    DIFFERENT values and EQUAL `when` and `confidence`: a one-hop claim (told by `x`, chain length 1)
    and a two-hop one (told by `z`, then retold by `y`: chain length 2). At the SHIPPED `told_weight` 0.5
    the one-hop value weighs 0.5 and the two-hop 0.25, so the one-hop value wins WHICHEVER IS FIRST
    in the ledger; at the CONTROL `told_weight` 1.0 both weigh 1.0, they tie, and today's rule --
    the first found wins a tie -- decides, so the ledger's order picks. The two-hop claim is listed
    first in one order precisely so that a reader that counts every told claim as ONE hop would
    tie at the shipped value too and hand it the win.

    MUTATION (run 2026-10-01, `T3b`): `teller_weight`'s exponent forced to `1` (hops read as 1
    always) -- both claims weigh 0.5, so this goes RED on the weight assertion; with that line
    removed the shipped arm ties and the first-listed two-hop value (5) wins the `read`, RED
    again. Restored, GREEN."""
    from ..decision.options import teller_weight
    from ..queries.person_q import LedgerReader

    w = P.tiny_world()
    p = w.persons["p_low"]
    assert all(r[0] not in ("x", "y", "z") for r in p.stance), "the hearer regards a teller already"
    one = Claim("c_one", p.id, "Hh", "stores:grain", 0, 2, "told_by", 100, "own", chain=("x",))
    two = Claim("c_two", p.id, "Hh", "stores:grain", 5, 2, "told_by", 100, "own", chain=("z", "y"))
    assert (one.hops, two.hops, one.teller, two.teller) == (1, 2, "x", "y")

    checked = 0
    shipped = teller_weight(p, _t3_fx(0.5, 0.5, 0.5))
    assert (shipped(one), shipped(two)) == (0.5, 0.25), (shipped(one), shipped(two))
    control = teller_weight(p, _t3_fx(1.0, 0.0, 0.0))
    assert (control(one), control(two)) == (1.0, 1.0)
    for order in ((two, one), (one, two)):
        p.ledger[:] = list(order)
        assert LedgerReader(p.ledger, shipped).read("Hh", "stores:grain") == one.value, (
            f"at the shipped told_weight the two-hop value won with the ledger as "
            f"{[c.id for c in order]} -- hops are not read off the chain")
        assert LedgerReader(p.ledger, shipped).latest_about("Hh") is one
        checked += 1
        first = order[0]
        assert LedgerReader(p.ledger, control).read("Hh", "stores:grain") == first.value, (
            "at the control told_weight the two claims tie and the first found must win, as before")
        assert LedgerReader(p.ledger, control).latest_about("Hh") is first
        assert LedgerReader(p.ledger).latest_about("Hh") is first
        checked += 1
    assert checked >= 1


def test_t3b_a_witnessed_retelling_extends_the_chain_by_the_teller():
    """THE DEPOSIT, ON A REAL RETELLING. `p_low` holds a claim firsthand and tells it at `Hh`; `p_mid`
    hears it (chain `(p_low,)`), walks to `S`, and tells it on; `p_high` hears THAT. Each deposit's
    chain is the teller's chain plus the teller -- `(p_low,)` then `(p_low, p_mid)` -- and `teller`
    is the last of it, `p_mid`, not the origin. Both tellings go through the real WITNESS barrier
    and `said_of`, the one owner of what a teller says.

    ⚠ `confidence_default` is swept to 50 so that `p_mid`'s told claim (the teller's own 100) is
    strictly the best claim he holds about `Hh`: the ambient `news.told` claim every hearer also
    deposits is at the default, and at 100 it would tie the told claim and `said_of` would carry
    THAT -- a retelling of THAT a telling happened, not of what was told."""
    from ..harness.soak import _claim_row

    fx = _t3_fx(0.5, 0.5, 0.5).sweep("confidence_default", 50)
    w = P.tiny_world(fx)
    assert w.fixtures.get("confidence_default") != 100

    def move(pid, rung):
        edge = next(t for t in w.tenures if t.subject == pid and t.kind == "contain" and t.live)
        edge.object = rung

    def tell(teller, label):
        said = said_of(w.persons[teller].ledger, "Hh", w.fixtures)
        assert said is not None, f"{teller} has nothing to say about Hh"
        act = Act(id=f"a_tell_{label}", actor=teller, verb="tell",
                  payload={"subject": "Hh", "said": said})
        w.acts.append(act)
        ev = Event(H(w.world_seed, w.tick, teller, f"ev:news.told:{act.id}"), "news.told",
                   [], [act.id], w.tick, "Success", ())
        w.log.append(ev)
        d.act_of[ev.id] = act
        d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
        return said

    def told(pid):
        return [c for c in w.persons[pid].ledger
                if c.source == "told_by" and c.subject == "Hh" and c.predicate == "stores:grain"]

    d = SeasonDriver(w)
    move("p_other", "S")        # `Hh` now holds `p_low` and `p_mid` only; `S` holds `p_high`, `p_other`
    w.persons["p_low"].ledger.append(
        Claim("c_held", "p_low", "Hh", "stores:grain", 8, 0, "firsthand", 100, "own"))
    first = tell("p_low", "hop1")
    assert first.chain == (), "a claim the teller holds firsthand carries an empty chain"
    mid = told("p_mid")
    assert len(mid) == 1 and mid[0].chain == ("p_low",), [c.chain for c in mid]

    w.tick += 1                  # a later barrier: the presence index is built once per barrier
    move("p_mid", "S")
    second = tell("p_mid", "hop2")
    assert second.chain == ("p_low",), (
        f"`said_of` handed the second telling the chain {second.chain!r}, not the one claim it picked")

    high = told("p_high")
    checked = len(high)
    assert checked == 1, f"p_high holds {len(high)} told claims -- the second hop never deposited"
    c = high[0]
    assert (c.chain, c.teller, c.hops) == (("p_low", "p_mid"), "p_mid", 2), (c.chain, c.teller, c.hops)
    assert c.chain[0] == "p_low", "the origin is the first element of the chain"
    row = _claim_row(c)
    assert (row["chain"], row["teller"]) == (["p_low", "p_mid"], "p_mid"), row


# ---------------------------------------------------------------------------------------------
# BATCH 1 CLOSE (antagonist rulings L2, F3): the support arithmetic and the regard term, observed
# at weights BELOW 1. Before these, every weighed test put one origin in each value group, and the
# only regard test held `told_weight` at 1.0, so origin choice, the per-origin `max`, the product
# over origins, and regard at the shipped weight were observed by nothing.

def _t3_cell_claims(p, rows):
    """`rows`: (id, value, chain) -> told claims on one cell, equal `when` and `confidence`."""
    return [Claim(cid, p.id, "Hh", "stores:grain", value, 2, "told_by", 100, "own", chain=chain)
            for cid, value, chain in rows]


def test_t3_support_two_origins_beat_one_and_one_origin_counts_once():
    """TWO INDEPENDENT ORIGINS OUTWEIGH ONE; ONE ORIGIN TWICE IS STILL ONE. At `told_weight` 0.5
    (gains 0, `rank` reads 0): value 5 told by `x` and by `y` (two origins, each weighs 0.5) has
    support 1 - 0.5 x 0.5 = 0.75 against value 0 told by `z` alone at 0.5, and value 5 told by `o`
    and retold through `o` -> `y` (ONE origin, weights 0.5 and 0.25) has support 0.5 -- the
    per-origin MAX, not the product over claims -- and ties value 0, which the first-listed wins.

    MUTATIONS this must notice (each reasoned against `_support`): origin = holder always (the two
    origins collapse, support 0.5, the first-listed value 0 wins), the product replaced by `max`
    (0.5, same), a product over claims instead of origins (0.625, value 5 wins the same-origin
    case), `max` replaced by overwrite or `min` (0.25 against the asserted 0.5), origin = the
    last teller instead of the first (the same-origin case reads two origins and 0.625)."""
    from ..decision.options import teller_weight
    from ..queries.person_q import LedgerReader

    p = P.tiny_world().persons["p_low"]
    weigh = teller_weight(p, _t3_fx(0.5, 0.0, 0.0))
    checked = 0

    two = _t3_cell_claims(p, [("c_z", 0, ("z",)), ("c_x", 5, ("x",)), ("c_y", 5, ("y",))])
    r = LedgerReader(two, weigh)
    assert r._support(two) == [0.5, 0.75, 0.75], r._support(two)
    assert r.read("Hh", "stores:grain") == 5, "two independent origins did not outweigh one"
    checked += 1

    same = _t3_cell_claims(p, [("c_z", 0, ("z",)), ("c_o1", 5, ("o",)), ("c_o2", 5, ("o", "y"))])
    r = LedgerReader(same, weigh)
    assert r._support(same) == [0.5, 0.5, 0.5], r._support(same)
    assert r.read("Hh", "stores:grain") == 0, (
        "one origin told twice out-supported a single other origin: it was counted per claim")
    checked += 1
    assert checked == 2


def test_t3_regard_decides_between_two_told_claims_at_the_shipped_weights():
    """REGARD, OBSERVED AT THE SHIPPED `told_weight` 0.5. The hearer's stance rows toward `f` and `h`
    are `(f, +5, 5)` and `(h, -5, 5)`, i.e. regard +25 / -25 = +-STANCE_MAX. `f` and `h` each tell
    a DIFFERENT value, equal `when` and `confidence`: at the shipped gains (0.5) `f` weighs
    0.5 x 1.5 = 0.75 and `h` 0.5 x 0.5 = 0.25, so `f`'s value wins WHICHEVER IS LISTED FIRST; at
    the CONTROL (told_weight 1.0, both gains 0) they tie and the first-listed decides. This is the
    observation `H-179` claims and `test_t3_unplanted_members_...` cannot make, because that one
    holds `told_weight` at 1.0 to reach a firsthand claim."""
    from ..decision.options import STANCE_MAX, teller_weight
    from ..queries.person_q import LedgerReader, regard

    p = P.tiny_world().persons["p_low"]
    p.stance = [("f", 5, 5), ("h", -5, 5)]
    assert regard(p, "f") == STANCE_MAX and regard(p, "h") == -STANCE_MAX
    checked = 0
    for order in (("f", "h"), ("h", "f")):
        val = {"f": 5, "h": 0}
        claims = _t3_cell_claims(p, [(f"c_{t}", val[t], (t,)) for t in order])
        shipped = teller_weight(p, _t3_fx(0.5, 0.5, 0.5))
        assert {c.chain[0]: shipped(c) for c in claims} == {"f": 0.75, "h": 0.25}
        assert LedgerReader(claims, shipped).read("Hh", "stores:grain") == 5, (
            f"regard did not decide between two told claims at the shipped weights ({order})")
        checked += 1
    first_5 = _t3_cell_claims(p, [("c_f", 5, ("f",)), ("c_h", 0, ("h",))])
    first_0 = list(reversed(first_5))
    control = teller_weight(p, _t3_fx(1.0, 0.0, 0.0))
    assert LedgerReader(first_5, control).read("Hh", "stores:grain") == 5
    assert LedgerReader(first_0, control).read("Hh", "stores:grain") == 0, (
        "at the control the two told claims did not tie: regard is leaking into the control arm")
    checked += 1
    assert checked == 3


# ---------------------------------------------------------------------------------------------
# T4 (`workplans/2026-10-01-telling-workplan.md`, ED-IN-0282): A TELLING NAMES ITS HEARER. `to` is
# a person the teller knows; the fold refuses a hearer who is not with the teller (`hearer`, the
# `with` stem); a present one hears by presence, and so does everybody else standing there -- no
# `addressed` channel (T-e).
# ---------------------------------------------------------------------------------------------

def test_t4_a_telling_to_an_absent_hearer_is_refused_and_a_present_one_hears():
    """`p_low` (in `Hh`) holds a claim on `Hh` and tells it twice.

    ABSENT -- to `p_king`, who stands in `R`: the fold refuses BEFORE any contest, on the `hearer`
    conjunct, with `news.untold`; the Event carries no degree (a refusal, not a lost contest, so a
    Failure roll cannot impersonate it), and nobody is told anything.
    PRESENT -- to `p_mid`, who stands in `Hh`: admitted, and folded at `Success` (the band the seam
    would hand back on a win -- the roll is not this test's subject); at WITNESS the addressee AND
    `p_other`, a bystander nobody addressed, both hold the told claim, chain `(p_low,)`.

    MUTATIONS, run once at T4 (recorded in the commit): drop the `hearer` conjunct from the row
    and the absent arm is admitted (the `failed` assertion goes red); make `co_located` admit
    nobody and neither hearer is told (the present arm goes red)."""
    from ..data.matrix import Step
    from ..data.requires import binding_from_act, evaluate
    from ..data.verbs import VERB_TABLE
    from ..queries.world_q import WorldReader
    from ..seam import Resolution

    w = P.tiny_world()
    teller, subject = "p_low", "Hh"
    w.persons[teller].ledger.append(
        Claim("c_held", teller, subject, "stores:grain", 8, 0, "firsthand", 37, "own"))
    row = VERB_TABLE["tell"]
    said = said_of(w.persons[teller].ledger, subject, w.fixtures)
    d = SeasonDriver(w)
    w.step = Step.RESOLVE

    def act(label, to):
        return Act(id=f"a_t4_{label}", actor=teller, verb="tell",
                   payload={"subject": subject, "to": to, "said": said})

    # ABSENT.
    gone = act("absent", "p_king")
    verdict = evaluate(row.requires_typed, WorldReader(w, teller), binding_from_act(gone))
    assert verdict.value is False and verdict.failed == "hearer", (
        f"a telling to someone in another rung read {verdict.value!r} on {verdict.failed!r}, "
        "not False on `hearer`")
    ok, kinds, _ = d._admits(w, gone, row)
    assert not ok and list(kinds) == ["news.untold"], (ok, kinds)
    out = d.resolve(mint_token(w, WriteClass.ACTS), [gone],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["news.untold"] and all(e.degree is None for e in out), (
        f"the absent telling emitted {[(e.kind, e.degree) for e in out]} -- it reached the contest")

    # PRESENT.
    here = act("present", "p_mid")
    ok, _, verdict = d._admits(w, here, row)
    assert ok and verdict.value is True, f"a telling to someone in the teller's rung was refused: {verdict}"
    w.acts.append(here)
    told_ev = d._fold(w, mint_token(w, WriteClass.ACTS), here, Resolution("Success", {}))
    assert [e.kind for e in told_ev] == ["news.told"], [e.kind for e in told_ev]
    w.log.extend(told_ev)
    for e in told_ev:       # what `resolve()` records for every Event it emits
        d.act_of[e.id] = here
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), told_ev)
    checked = 0
    for pid in ("p_mid", "p_other"):
        got = [c for c in w.persons[pid].ledger
               if (c.subject, c.predicate, c.value) == (subject, "stores:grain", 8) and c.chain]
        assert len(got) == 1 and got[0].chain == (teller,), (
            f"{pid} holds {[(c.value, c.chain) for c in got]} -- a present "
            f"{'addressee' if pid == 'p_mid' else 'bystander'} was not told")
        checked += 1
    assert checked == 2
    assert not any(c.chain for c in w.persons["p_king"].ledger), "the absent hearer was told anyway"


def test_t4_a_with_read_is_observed_and_never_deposited_into_the_tellers_ledger():
    """BATCH-2 CLOSE `F1` (`ED-IN-0282`). The `hearer` conjunct's read of `with` rides the Event as
    `Observation(to, "with:<teller>", True|False)`; WITNESS must NOT append it to the teller's ledger
    (`loop/witness.py` skips `WORLD_ONLY_STEMS` beside `LEDGER_DERIVED_STEMS`). The person side never
    reads `with` back, but undeclared readers do: `claim.held` (any claim on the subject), Q2
    `claim_landed` (a question on the HEARER, from which `opening_set` forms a `tell`), and `said_of`
    (the newest non-`seen` claim on the subject, any predicate).

    Four cases -- a refused telling to an ABSENT hearer and a successful one to a PRESENT hearer, each
    under the shipped `claim_subject_rule` and under `actor` -- and in each: no `with:` claim in the
    teller's ledger, `Event.observed` STILL carries the observation (the hash-bearing Event is
    unchanged: only the ledger append is skipped), the absent refusal is still `degree is None` (the
    T4 refusal is the WorldReader's), and Q2 raises no `claim_landed` question from a `with:` claim.
    `checked` pins that all four cases ran.

    MUTATION (run 2026-10-01): the `WORLD_ONLY_STEMS` skip deleted from `loop/witness.py` -- a `with:`
    claim lands in the teller's ledger in all four cases and the first assertion of each goes RED
    (the Q2 assertion, which reads the ledger id back, goes red with it). Restored, GREEN."""
    from ..data.matrix import Step
    from ..data.requires import WORLD_ONLY_STEMS
    from ..data.verbs import VERB_TABLE
    from ..queries.world_q import questions_for
    from ..seam import Resolution

    row = VERB_TABLE["tell"]
    teller, subject = "p_low", "Hh"
    checked = 0
    for rule in (P.DEFAULT_FIXTURES.get("claim_subject_rule"), "actor"):
        for to, present in (("p_king", False), ("p_mid", True)):
            w = P.tiny_world(P.DEFAULT_FIXTURES.sweep("claim_subject_rule", rule))
            w.persons[teller].ledger.append(
                Claim("c_held", teller, subject, "stores:grain", 8, 0, "firsthand", 37, "own"))
            said = said_of(w.persons[teller].ledger, subject, w.fixtures)
            d = SeasonDriver(w)
            w.step = Step.RESOLVE
            a = Act(id=f"a_f1_{to}", actor=teller, verb="tell",
                    payload={"subject": subject, "to": to, "said": said})
            where = f"rule={rule!r} to={to!r}"
            if present:
                w.acts.append(a)
                out = d._fold(w, mint_token(w, WriteClass.ACTS), a, Resolution("Success", {}))
                assert [e.kind for e in out] == ["news.told"], (where, [e.kind for e in out])
                for e in out:
                    d.act_of[e.id] = a
            else:
                out = d.resolve(mint_token(w, WriteClass.ACTS), [a],
                                contest_max_depth=w.fixtures.get("contest_max_depth"))
                assert [e.kind for e in out] == ["news.untold"], (where, [e.kind for e in out])
                assert all(e.degree is None for e in out), (
                    where, "the T4 refusal reached the contest: it is the WorldReader's, not the ledger's")
            w.log.extend(out)
            # The observation IS on the Event, with the read's own value -- the hash is unchanged.
            obs = [o for e in out for o in e.observed
                   if str(o.predicate).partition(":")[0] in WORLD_ONLY_STEMS]
            assert [(o.subject, o.predicate, o.value) for o in obs] == [(to, f"with:{teller}", present)], (
                where, "Event.observed no longer carries the `with` read", obs)
            w.step = Step.WITNESS
            d.witness(mint_token(w, WriteClass.INTERIOR), out)
            held = [c for c in w.persons[teller].ledger
                    if str(c.predicate).partition(":")[0] in WORLD_ONLY_STEMS]
            assert not held, (where, "a `with` read was deposited into the teller's ledger",
                              [(c.subject, c.predicate, c.value) for c in held])
            # Q2: nothing the telling left in the teller's ledger raises a question from a `with` claim.
            qs = [q for q in questions_for(w, w.persons[teller], since=(-1, 0))
                  if q.source == "claim_landed"]
            by_id = {c.id: c for c in w.persons[teller].ledger}
            assert not [q for q in qs if str(by_id[q.about].predicate).startswith("with:")], (
                where, "Q2 raised `claim_landed` from a `with` claim")
            # Measured with the skip removed: ONE `claim_landed` question about the hearer, in each
            # of the four cases; nothing else in this world is about them, so the count is 0 here.
            assert not [q for q in qs if q.referents == (to,)], (
                where, "Q2 raised a question about the hearer from a prior telling's `with` read")
            checked += 1
    assert checked == 4


def test_t4_a_planted_false_with_claim_in_the_tellers_ledger_does_not_decline_the_telling():
    """THE PERSON SIDE NEVER ANSWERS `with` (`data/requires.py: WORLD_ONLY_STEMS`;
    `LedgerReader.read`'s early UNKNOWN). WITNESS no longer deposits the fold's `with` read (batch-2
    close `F1`), so this is the reader's OWN guard, kept as defence in depth: a `with:` claim that
    reached a ledger some other way -- planted here as `(p_mid, "with:p_low", False)` -- must still
    not decide presence. If the person-side reader
    answered it, clause 4 (`belief_contradicts`) would read the `hearer` conjunct False from that
    stale claim and the telling would never be formed for a hearer who has since arrived -- a ledger
    deciding presence, which is the world's to decide.

    Planted, then observed three ways: the reader says UNKNOWN, `belief_contradicts` is False, and
    the real chooser still forms a `tell` to `p_mid`. A control run without the planted claim forms
    the same `tell`, so the assertion that one IS formed is not vacuous.

    MUTATION (run 2026-10-01): the `WORLD_ONLY_STEMS` branch deleted from `LedgerReader.read` --
    the reader answers False, `belief_contradicts` is True and this goes RED on the first
    assertion. Restored, GREEN."""
    from ..data.matrix import Step
    from ..data.requires import UNKNOWN
    from ..data.verbs import VERB_TABLE
    from ..decision import assemble
    from ..epistemic import belief_contradicts
    from ..queries.person_q import LedgerReader
    from ..state.carriers import Question, Sensation

    def tells_to_hearer(plant: bool) -> list:
        w = P.tiny_world()
        teller, hearer, subject = "p_low", "p_mid", "Hh"
        tp = w.persons[teller]
        tp.ledger.append(Claim("c_held", teller, subject, "stores:grain", 8, 0, "firsthand", 37, "own"))
        tp.ledger.append(Claim("c_knows", teller, hearer, "exists:Person", 1, 0, "firsthand", 100, "own"))
        if plant:
            tp.ledger.append(Claim("c_with", teller, hearer, f"with:{teller}", False, 0, "firsthand",
                                   100, "own"))
            assert LedgerReader(tp.ledger).read(hearer, f"with:{teller}") is UNKNOWN, (
                "the person-side reader answered a `with` claim from the ledger")
            assert not belief_contradicts(
                tp, VERB_TABLE["tell"], subject, {"subject": subject, "to": hearer}), (
                "clause 4 read the `hearer` conjunct False from a planted `with` claim")
        w.step = Step.DELIBERATE
        q = Question("q:t4with", "need", (subject,), "prop")
        scenes = P.chooser(w, only=teller, verbs=frozenset({"tell"}))(
            tp, assemble(tp, q, w.fixtures.get("view_k")), Sensation(0), lambda: 5)
        return [a.payload.get("to") for s in scenes for a in s.acts if a.verb == "tell"]

    assert tells_to_hearer(False) == ["p_mid"], "the control forms no `tell` to the hearer: fixture moved"
    assert tells_to_hearer(True) == ["p_mid"], (
        "a planted `with:<actor>` False claim declined the telling: the person side answered it")


def test_t4_the_known_person_claim_roster_refuses_a_planted_collision():
    """`_check_known_person_claim` is the load-time cross-check of `rosters.yaml:
    known_person_operands.claim` against `REQUIRES_STEMS` and `observation_terms`; it never fires on
    the shipped data, so nothing observed that it could (the shape `test_demand_delivery.py`'s
    `_check_shortfall_stem` and `test_content_operands.py`'s `_check_writ_sourced_subset` calls
    follow). Each planted collision must raise `Unspecified`, and the shipped claim must pass.

    MUTATION (run 2026-10-01): the `stem not in requires_stems` clause deleted -- the stem
    collision stops raising and this goes RED. Restored, GREEN."""
    from ..data.requires import (
        KNOWN_PERSON_CLAIM, OBSERVATION_TERMS, REQUIRES_STEMS, _check_known_person_claim)
    from ..gaps import Unspecified
    import pytest

    term = KNOWN_PERSON_CLAIM["seen_term"]
    stem = KNOWN_PERSON_CLAIM["predicate"].partition(":")[0]
    checked = 0
    for bad in ({"predicate": f"nostem:Person", "seen_term": term},        # a stem no reader answers
                {"predicate": stem, "seen_term": term},                    # no `:<kind>`
                {"predicate": f"{stem}:", "seen_term": term},              # an empty kind
                {"predicate": KNOWN_PERSON_CLAIM["predicate"], "seen_term": "nonterm"},
                {}):
        with pytest.raises(Unspecified):
            _check_known_person_claim(bad, REQUIRES_STEMS, OBSERVATION_TERMS)
        checked += 1
    assert checked == 5
    _check_known_person_claim(KNOWN_PERSON_CLAIM, REQUIRES_STEMS, OBSERVATION_TERMS)   # shipped passes


# ---------------------------------------------------------------------------------------------
# T4b (ED-IN-0282): AN OPPORTUNITY INCLUDES ITS COUNTERPARTY. The once-per-season filter keyed
# `(verb, subject)`, so once topic C was told to B it was dropped for D too, though a person tells
# several hearers. The key is the general rule for a row naming a counterparty; `tell` is the row where
# it changes anything of the rows measured here (`petition`/`issue` have `to` == `subject`; `give` was typed at
# position 14 and fans its counterparty over the persons the giver knows, so the key applies to it too).
# `data/verbs.py::opportunity_key` is the
# ONE key; `loop/driver.py` writes it after the fold and `_drop_what_was_already_done` reads it.
# ---------------------------------------------------------------------------------------------

def _t4b_scene_of(act):
    from ..state.carriers import Scene
    return Scene(id=f"sc_{act.id}", actor=act.actor, acts=[act])


def _t4b_kept(taken, acts):
    """The acts `_drop_what_was_already_done` keeps, one scene per act, in order."""
    from ..loop.deliberate import _drop_what_was_already_done
    scenes = _drop_what_was_already_done([_t4b_scene_of(a) for a in acts], taken)
    return [a.id for sc in scenes for a in sc.acts]


def test_t4b_a_second_hearer_is_a_distinct_opportunity():
    """THE DRIVER ROUND, END TO END. `p_low` holds a claim on `Hh` and, with `p_mid` and `p_other`
    both standing with them, tells it to `p_mid` in round 0 (realised: the writer in
    `SeasonDriver.season` records the key). In a later round the chooser offers a repeat to
    `p_mid` and a telling to `p_other`: the filter DROPS the repeat and KEEPS the second hearer.

    MUTATION (run 2026-10-01, `T4b`): `opportunity_key` reverted to `(verb, subject)` -- the telling
    to `p_other` is dropped with the repeat and the `kept` assertion goes RED. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("scene_budget", 5))   # five rounds, so a later one exists
    teller, subject = "p_low", "Hh"
    w.persons[teller].ledger.append(
        Claim("c_held", teller, subject, "stores:grain", 8, 0, "firsthand", 37, "own"))
    said = said_of(w.persons[teller].ledger, subject, w.fixtures)
    d = SeasonDriver(w)
    n, state = [0], {"pair": None}

    def tell(to):
        n[0] += 1
        return Act(id=f"a_t4b_{n[0]}", actor=teller, verb="tell",
                   payload={"subject": subject, "to": to, "said": said})

    def tells():
        return [a.payload["to"] for a in w.acts if a.verb == "tell" and a.actor == teller]

    def choose(p, verbs, sn, ask_budget):
        if p.id != teller:
            return []
        if not d._realised.get(teller):
            return [tell("p_mid")]          # until one is REALISED (a refused attempt is retried)
        if state["pair"] is None:           # the telling to `p_mid` is behind us: offer it AGAIN,
            state["pair"] = len(tells())    # and a telling to `p_other`
            return [tell("p_mid"), tell("p_other")]
        return []

    d.season(choose, None, P.SUBSIST, contest_max_depth=w.fixtures.get("contest_max_depth"))
    realised = d._realised.get(teller) or set()
    from ..data.verbs import opportunity_key
    assert opportunity_key("tell", subject, {"subject": subject, "to": "p_mid"}) in realised, (
        f"no telling to `p_mid` was realised ({realised}); the test has nothing to filter by")
    assert state["pair"] is not None, "the pair was never offered: no later round reached the filter"
    after = tells()[state["pair"]:]
    assert after == ["p_other"], (
        f"after the telling to `p_mid` was realised the filter let through {after}: expected the "
        "repeat to `p_mid` dropped and the telling to `p_other` (a distinct opportunity) released")


def test_t4b_the_reader_keeps_a_distinct_counterparty_and_drops_the_same_one():
    """`tell` and `petition` both name `counterparty: to`. With a telling/petition on `Hh` to `p_mid`
    REALISED, a second to `p_other` is a distinct opportunity and survives; a repeat to `p_mid` is the
    same one and is dropped. `checked` guards the loop against asserting nothing.

    MUTATION (run 2026-10-01, `T4b`): `opportunity_key` reverted to the 2-tuple -- both rows' second
    counterparty is dropped and this goes RED. Restored, GREEN."""
    from ..data.verbs import VERB_TABLE, opportunity_key
    checked = 0
    for verb in ("tell", "petition"):
        assert VERB_TABLE[verb].counterparty == "to", verb
        def act(label, to, verb=verb):
            return Act(id=f"a_{verb}_{label}", actor="p_low", verb=verb,
                       payload={"subject": "Hh", "to": to})
        done = act("done", "p_mid")
        taken = {opportunity_key(done.verb, "Hh", done.payload)}
        got = _t4b_kept(taken, [act("again", "p_mid"), act("other", "p_other")])
        assert got == [f"a_{verb}_other"], f"{verb}: kept {got}"
        checked += 1
    assert checked == 2


def test_t4b_a_row_with_no_counterparty_keys_exactly_as_before():
    """`fight`, `move` and `transfer` name no counterparty column, so their key is `(verb, subject)`
    whatever else the payload carries (a `to` here is a decoy, not a counterparty); two acts on one
    subject are ONE opportunity. An act with no subject has none: `None`, never recorded, never
    dropped. `give` is untyped, so no Candidate carries its `to`; absent from the payload it is the
    2-tuple too.

    MUTATION (run 2026-10-01, `T4b`): the key made to read `to` for every row -- the decoy arms split
    and the first assertion goes RED."""
    from ..data.verbs import VERB_TABLE, opportunity_key
    checked = 0
    for verb in ("fight", "move", "transfer"):
        assert not VERB_TABLE[verb].counterparty, verb
        a = Act(id=f"a_{verb}_1", actor="p_low", verb=verb, payload={"subject": "Hh", "to": "p_mid"})
        b = Act(id=f"a_{verb}_2", actor="p_low", verb=verb, payload={"subject": "Hh", "to": "p_other"})
        key = opportunity_key(verb, "Hh", a.payload)
        assert key == (verb, "Hh") == opportunity_key(verb, "Hh", b.payload), key
        assert _t4b_kept({key}, [a, b]) == [], f"{verb}: the same opportunity survived"
        checked += 1
    assert checked == 3
    assert opportunity_key("tell", "", {"to": "p_mid"}) is None
    assert opportunity_key("give", "rec", {"subject": "rec"}) == ("give", "rec")
    # a counterparty that IS the subject adds nothing (`determine`, `oblige`): keyed as before
    assert VERB_TABLE["oblige"].counterparty == "subject"
    assert opportunity_key("oblige", "p_mid", {"subject": "p_mid"}) == ("oblige", "p_mid")


# ---------------------------------------------------------------------------------------------
# T5 (`workplans/2026-10-01-telling-workplan.md`, ED-IN-0282): THE TOLD DEDUP IS BY ORIGIN. A told
# deposit is skipped only if the hearer holds the triple with an EMPTY chain (firsthand, seen,
# inferred) or with the SAME `chain[0]`. A held copy from a DIFFERENT origin does not skip: that
# second claim is what `LedgerReader._support`'s noisy-OR counts.
# ---------------------------------------------------------------------------------------------

_T5_SUBJECT, _T5_PRED = "Hh", "stores:grain"


def _t5_world(fx=None):
    """`tiny_world` plus a `tell` helper that drives one telling through the REAL WITNESS barrier
    with a hand-built `Said` (so the guard is observed alone, not `said_of`'s pick). Returns
    `(w, tell, told)`: `told(pid)` is the hearer's told claims on the cell; `tell(teller, chain,
    value)` advances the tick (the presence index is built once per barrier) and tells whoever
    stands with the teller."""
    w = P.tiny_world() if fx is None else P.tiny_world(fx)
    d = SeasonDriver(w)
    n = [0]

    def move(pid, rung):
        edge = next(t for t in w.tenures if t.subject == pid and t.kind == "contain" and t.live)
        edge.object = rung

    def tell(teller, chain, value, conf=100):
        n[0] += 1
        w.tick += 1
        said = Said(_T5_SUBJECT, _T5_PRED, value, conf, tuple(chain))
        act = Act(id=f"a_t5_{n[0]}", actor=teller, verb="tell",
                  payload={"subject": _T5_SUBJECT, "said": said})
        w.acts.append(act)
        ev = Event(H(w.world_seed, w.tick, teller, f"ev:news.told:{act.id}"), "news.told",
                   [], [act.id], w.tick, "Success", ())
        w.log.append(ev)
        d.act_of[ev.id] = act
        d.witness(mint_token(w, WriteClass.INTERIOR), [ev])

    def told(pid):
        return [c for c in w.persons[pid].ledger
                if c.source == "told_by" and c.subject == _T5_SUBJECT and c.predicate == _T5_PRED]

    for pid in ("p_mid", "p_other", "p_low"):
        move(pid, "S")          # everybody but the King stands with `p_high`
    return w, tell, told


def test_t5_one_origin_through_two_tellers_deposits_once():
    """ONE ORIGIN HEARD BY TWO ROUTES IS ONE WITNESS. `p_low` is the origin; `p_mid` and then
    `p_other` each retell `p_low`'s claim to `p_high` (chains `(p_low, p_mid)` and `(p_low,
    p_other)`, one origin). The second is skipped: `p_high` holds exactly the first. The positive
    control is the FIRST telling, which does deposit, and `test_t5_two_origins_...` below, where a
    telling from a different origin does too.

    MUTATION (run 2026-10-01, `T5`): the guard's origin clause removed so any held TOLD copy of the
    triple fails to skip (`(not c.chain)` alone) -- `p_high` then holds two and this goes RED on the
    count. Restored, GREEN."""
    w, tell, told = _t5_world()
    assert told("p_high") == []
    tell("p_mid", ("p_low",), 8)
    first = told("p_high")
    assert len(first) == 1 and first[0].chain == ("p_low", "p_mid"), [c.chain for c in first]
    tell("p_other", ("p_low",), 8)
    got = told("p_high")
    assert [c.chain for c in got] == [("p_low", "p_mid")], (
        f"`p_high` holds {[c.chain for c in got]} -- one origin was deposited twice")
    # The second telling's other hearer, `p_mid`, holds nothing of it from the first (they were its
    # teller), so it is the ONE copy that shows the second telling reached WITNESS and deposited for
    # somebody; the first telling alone cannot satisfy it.
    heard = told("p_mid")
    assert [c.chain for c in heard] == [("p_low", "p_other")], (
        f"`p_mid` holds {[c.chain for c in heard]}: the second telling never reached WITNESS, so "
        "`p_high` holding one copy proves nothing about it")


def test_t5_two_origins_deposit_twice_and_outrank_one():
    """TWO INDEPENDENT ORIGINS ARE TWO CLAIMS, AND THEY OUTRANK ONE. `p_mid` and `p_other` each tell
    `p_high` the SAME triple (value 5) firsthand -- chains `(p_mid,)` and `(p_other,)`, origins A and
    B -- and then `p_low`, the latest teller by a tick, tells a DIFFERENT value (0), one origin. The
    old guard skipped B (the triple was held, told); now both land. Read at the SHIPPED `told_weight`
    0.5 (no stance toward any of them, `rank` 0) each one-hop claim weighs 0.5, so value 5 has support
    1 - 0.5 x 0.5 = 0.75 against 0.5 for value 0, and 5 wins although 0 is newer; with ONE copy of 5
    the two tie on support and the newer 0 would win.

    MUTATION (run 2026-10-01, `T5`): the old guard restored (skip on any held copy of the triple) --
    B is dropped, value 5 reads support 0.5 and this goes RED on the count of claims and on the read.
    Restored, GREEN."""
    from ..decision.options import teller_weight
    from ..queries.person_q import LedgerReader

    w, tell, told = _t5_world()
    p = w.persons["p_high"]
    assert all(r[0] not in ("p_mid", "p_other", "p_low") for r in p.stance)
    tell("p_mid", (), 5)
    tell("p_other", (), 5)
    tell("p_low", (), 0)
    five = [c for c in told("p_high") if c.value == 5]
    assert sorted(c.chain for c in five) == [("p_mid",), ("p_other",)], [c.chain for c in five]
    weigh = teller_weight(p, _t3_fx(0.5, 0.5, 0.5))
    reader = LedgerReader(p.ledger, weigh)
    cell = [c for c in p.ledger if c.subject == _T5_SUBJECT and c.predicate == _T5_PRED
            and c.source == "told_by"]
    support = dict(zip((c.chain[0] for c in cell), reader._support(cell)))
    assert support == {"p_mid": 0.75, "p_other": 0.75, "p_low": 0.5}, support
    assert reader.read(_T5_SUBJECT, _T5_PRED) == 5, (
        "two independent origins did not outrank one newer single-origin claim")
    # the control: the same ledger with ONE copy of 5 gives the newer value
    one = [c for c in cell if c.chain != ("p_other",)]
    assert LedgerReader(one, weigh).read(_T5_SUBJECT, _T5_PRED) == 0


def test_t5_a_firsthand_holder_still_skips():
    """THE 175-OF-180 FIX STANDS. A hearer holding the triple with an EMPTY chain -- firsthand, and
    `inferred` -- receives no told copy, even from an origin they have never heard; `p_other`, who
    holds nothing, hears the same telling and gets one (the positive control: the telling did reach
    WITNESS). The corpus-wide `told_redeposits == 0` assertion
    (`test_season_shape.py`, beside `by_sig`) is the same property at scale.

    MUTATIONS (run 2026-10-01, `T5`, both on `witness.py`'s guard): the empty-chain clause removed as
    `c.chain[0] == _origin` ALONE does not fail an assertion -- the held claim's chain is empty, so
    the guard raises `IndexError` and the test ERRORS. The clause removed with the index guarded
    (`c.chain and c.chain[0] == _origin`) -- the firsthand holder is told and this goes RED on the
    first assertion. Restored, GREEN."""
    for source in ("firsthand", "inferred"):
        w, tell, told = _t5_world()
        held = Claim("c_held", "p_high", _T5_SUBJECT, _T5_PRED, 8, 0, source, 100, "own")
        assert held.chain == ()
        w.persons["p_high"].ledger.append(held)
        tell("p_mid", (), 8)
        assert told("p_high") == [], f"a {source} holder was told what they already hold"
        assert len(told("p_other")) == 1, "the positive control: a hearer who holds nothing is told"
        # a genuinely DIFFERENT origin from the first telling's `p_mid`: `p_low` passes on what
        # `p_king` said, so the incoming chain is `(p_king, p_low)`
        tell("p_low", ("p_king",), 8)
        assert told("p_high") == [], f"a {source} holder was told the same triple by another origin"
        assert [c.chain for c in told("p_other")] == [("p_mid",), ("p_king", "p_low")], (
            "the positive control: the second telling reached WITNESS and a hearer who holds only "
            "another origin's copy is told it")


# ---------------------------------------------------------------------------------------------
# T6 (`workplans/2026-10-01-telling-workplan.md`, ED-IN-0282; `H-183`): A TELLER'S RECORD.
# `record(p, x, fx)` pairs `p`'s claims told by `x` with `p`'s OWN firsthand claim on the same
# `(subject, predicate)` cell; `weigh` multiplies it in once per teller.
# ---------------------------------------------------------------------------------------------

def _t6_claims(p, firsthand, told):
    """`firsthand`: `(subject, value)` rows; `told`: `(id, subject, value, teller)` rows -- all on
    predicate `stores:grain`, planted into `p`'s ledger."""
    p.ledger[:] = (
        [Claim(f"c_own_{s}", p.id, s, "stores:grain", v, 1, "firsthand", 100, "own")
         for s, v in firsthand]
        + [Claim(cid, p.id, s, "stores:grain", v, 2, "told_by", 100, "own", chain=(t,))
           for cid, s, v, t in told])


def _t6_pre_record_weight(fx, hops, relation):
    """What `teller_weight` computed before `T6`, written out here independently of `record`."""
    return min(1.0, fx.get("told_weight") ** hops * relation)


def test_t6_an_unknown_teller_weighs_exactly_told_weight():
    """NO PAIR IS NEUTRAL, EXACTLY. `x` has told `p` two things -- one on a cell `p` holds nothing
    firsthand about, one on a cell `p` holds a firsthand claim about under a DIFFERENT predicate --
    so `x` has no pair; `y` has one. At the shipped gains `record(p, x)` is exactly 1.0 and `x`'s
    claim weighs `told_weight ** 1 * relation` bit-for-bit (0.5 x 1.5 = 0.75, `p` regards `x` at
    +STANCE_MAX); `y`, who has a pair, does not -- so the neutrality is observed against a teller
    for whom `record` moves, not against a `record` that is constant.

    MUTATION (run 2026-10-01, `T6`): zero pairs returned as `1.0 - record_gain` (`standing_of`'s
    polarity -- the maximum gap) -- `x` weighs 0.375 and this goes RED on the `record == 1.0`
    assertion. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES as fx
    from ..decision.options import STANCE_MAX, record, teller_weight

    p = P.tiny_world().persons["p_low"]
    p.stance = [("x", 5, 5)]
    _t6_claims(p, [("Hh", 5)], [("c_x1", "S", 3, "x"), ("c_x2", "R", 4, "x"), ("c_y", "Hh", 0, "y")])
    p.ledger.append(Claim("c_x_other", p.id, "Hh", "stores:wood", 9, 2, "told_by", 100, "own",
                          chain=("x",)))
    assert fx.get("record_gain") == 0.5, "the shipped record_gain moved: restate this test's numbers"
    weigh = teller_weight(p, fx)
    checked = 0
    assert record(p, "x", fx) == 1.0 and record(p, "x", fx) is not None
    expected = _t6_pre_record_weight(fx, 1, 1.0 + fx.get("regard_gain") * (STANCE_MAX / STANCE_MAX))
    assert expected == 0.75
    for c in p.ledger:
        if c.chain == ("x",):
            assert weigh(c) == expected, (c.id, weigh(c), expected)
            checked += 1
    assert checked == 3, checked
    assert record(p, "y", fx) == 0.5, record(p, "y", fx)
    assert weigh(next(c for c in p.ledger if c.id == "c_y")) < expected


def test_t6_a_teller_contradicted_twice_weighs_less_than_one_confirmed_twice():
    """THE RECORD MOVES THE WEIGHT, IN THE RIGHT DIRECTION. `p` holds two firsthand cells (`Hh`, `S`).
    `good` told `p` the same two values, `bad` told `p` two different ones, `mixed` one of each; each
    also told `p` the same value on a third cell (`R`) with no firsthand mate, so the claim weighed
    differs only by its teller. At the shipped gains `good` weighs 0.5 x 1.5 = 0.75, `bad`
    0.5 x 0.5 = 0.25 and `mixed` (balance 0) exactly 0.5. Each teller really holds the pairs the
    arithmetic needs (`_pair`'s counts are asserted), so a `record` that read nothing would fail.

    MUTATION (run 2026-10-01, `T6`): `agree` and `dis` swapped in `record`'s balance -- `good`
    weighs 0.25 and `bad` 0.75, and this goes RED on the first weight assertion. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES as fx
    from ..decision.options import _pair, record, teller_weight

    p = P.tiny_world().persons["p_low"]
    own_rows = [("Hh", 5), ("S", 6)]
    told_rows = [("c_g1", "Hh", 5, "good"), ("c_g2", "S", 6, "good"), ("c_g3", "R", 7, "good"),
                 ("c_b1", "Hh", 0, "bad"), ("c_b2", "S", 0, "bad"), ("c_b3", "R", 7, "bad"),
                 ("c_m1", "Hh", 5, "mixed"), ("c_m2", "S", 0, "mixed"), ("c_m3", "R", 7, "mixed")]
    _t6_claims(p, own_rows, told_rows)
    key = lambda c: (c.subject, c.predicate)
    own = [c for c in p.ledger if not c.chain]
    counts = {t: _pair([c for c in p.ledger if c.teller == t], own, key)
              for t in ("good", "bad", "mixed")}
    assert counts == {"good": (2, 0), "bad": (0, 2), "mixed": (1, 1)}, counts
    weigh = teller_weight(p, fx)
    w = {t: weigh(next(c for c in p.ledger if c.id == f"c_{t[0]}3")) for t in counts}
    assert w["good"] > w["bad"], w
    assert w == {"good": 0.75, "bad": 0.25, "mixed": 0.5}, w
    assert record(p, "good", fx) == 1.5 and record(p, "bad", fx) == 0.5
    # and the gain scales it: at 1.0 a teller always contradicted weighs nothing
    full = teller_weight(p, fx.sweep("record_gain", 1.0))
    assert full(next(c for c in p.ledger if c.id == "c_b3")) == 0.0


def test_t6_record_gain_zero_is_the_control():
    """AT `record_gain` 0 EVERY WEIGHT IS ITS PRE-`T6` VALUE, ON A LEDGER THAT HAS PAIRS. The ledger is
    the previous test's (`good` agrees twice, `bad` contradicts twice, `mixed` once each) plus a
    two-hop claim; the pairs are asserted to exist, so the control is not vacuous (a ledger with no
    pair reads the same at any gain). At the shipped 0.5 the same claims differ from the control,
    so the arms are told apart from both sides.

    MUTATION (run 2026-10-01, `T6`): the balance applied without its gain
    (`1 + (agree - dis)/(agree + dis)`) -- `good` weighs 1.0 at the control instead of 0.5 and this
    goes RED. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision.options import _pair, teller_weight

    p = P.tiny_world().persons["p_low"]
    _t6_claims(p, [("Hh", 5), ("S", 6)],
               [("c_g", "Hh", 5, "good"), ("c_b", "Hh", 0, "bad"), ("c_g2", "S", 6, "good"),
                ("c_b2", "S", 0, "bad"), ("c_g3", "R", 7, "good"), ("c_b3", "R", 7, "bad")])
    p.ledger.append(Claim("c_two", p.id, "R", "stores:grain", 7, 2, "told_by", 100, "own",
                          chain=("o", "good")))
    key = lambda c: (c.subject, c.predicate)
    own = [c for c in p.ledger if not c.chain]
    pairs = sum(sum(_pair([c for c in p.ledger if c.teller == t], own, key)) for t in ("good", "bad"))
    assert pairs == 4, f"the control ledger has {pairs} pairs, not 4: it would be vacuous"
    shipped_fx = DEFAULT_FIXTURES
    control_fx = shipped_fx.sweep("record_gain", 0.0)
    shipped, control = teller_weight(p, shipped_fx), teller_weight(p, control_fx)
    differ = checked = 0
    for c in p.ledger:
        if not c.chain:
            assert control(c) == shipped(c) == 1.0
            continue
        # relation is 1.0 (no stance rows), so the pre-T6 weight is `told_weight ** hops`
        assert control(c) == _t6_pre_record_weight(control_fx, c.hops, 1.0), (c.id, control(c))
        checked += 1
        differ += shipped(c) != control(c)
    assert checked == 7 and differ >= 4, (checked, differ)


def test_t6_record_reads_the_hearers_own_ledger_only():
    """ANOTHER PERSON'S LEDGER CHANGES NOTHING. `p_mid` holds the firsthand claim and `x`'s
    contradicting told claim on a cell; `p_low` holds only a told claim from `x` on it. `p_low`'s
    record for `x` is neutral (1.0) while the pair sits in `p_mid`'s ledger, `p_mid`'s own is 0.5, and
    once the same firsthand claim is in `p_low`'s ledger `p_low`'s moves to 0.5 -- so the neutrality
    was the ledger, not a `record` that never pairs. A told claim by a different teller `y` on that
    cell does not move `x`'s record either.

    MUTATION (run 2026-10-01, `T6`): `told` filtered on nothing (every teller's claims pair) --
    `y`'s agreeing claim lifts `x`'s record from 0.5 to 1.0 and this goes RED on the last assertion.
    Restored, GREEN. (`record` takes `p` and `fx` only, so a read of another person's ledger is
    not expressible in its signature; that half is observed, not mutated.)"""
    from ..data.fixtures import DEFAULT_FIXTURES as fx
    from ..decision.options import record

    w = P.tiny_world()
    low, mid = w.persons["p_low"], w.persons["p_mid"]
    own_claim = lambda pid: Claim(f"c_own_{pid}", pid, "Hh", "stores:grain", 5, 1, "firsthand", 100, "own")
    told_x = lambda pid: Claim(f"c_x_{pid}", pid, "Hh", "stores:grain", 0, 2, "told_by", 100, "own",
                               chain=("x",))
    low.ledger[:] = [told_x(low.id)]
    mid.ledger[:] = [own_claim(mid.id), told_x(mid.id)]
    assert record(mid, "x", fx) == 0.5, "the pair in p_mid's own ledger does not register"
    assert record(low, "x", fx) == 1.0, "a claim in another person's ledger moved p_low's record"
    low.ledger.append(own_claim(low.id))
    assert record(low, "x", fx) == 0.5, "a pair in p_low's own ledger does not register"
    low.ledger.append(Claim("c_y_low", low.id, "Hh", "stores:grain", 5, 2, "told_by", 100, "own",
                            chain=("y",)))
    assert record(low, "x", fx) == 0.5, "another teller's agreeing claim moved x's record"


def test_t6_the_mate_is_the_belief_ledger_reader_reads_not_the_last_listed_claim():
    """A LEDGER IN EVICTION ORDER IS NOT IN BELIEF ORDER. `p` holds two firsthand claims on one
    cell: an OLDER, higher-confidence one (value 5, `when` 1, confidence 100) and a NEWER, lower-
    confidence one (value 6, `when` 5, confidence 20). `ledgers.eviction_key` ranks them 200 and 120,
    so in eviction order the newer is listed FIRST and the older LAST -- while `LedgerReader` reads
    the NEWER as the belief (most recent). `x` told `p` value 6. Against the belief (6) that
    AGREES, and `record` is `1 + record_gain`; against the last-listed claim (5) it disagrees and
    would read `1 - record_gain`. Both orders are asserted to hold, so the ledger really is in the
    order that separates the two pickers.

    MUTATION (run 2026-10-01, `T6`): `_pair` reverted to `{key(c): c for c in own}` (the last listed
    wins) -- `record` reads 0.5 and this goes RED on the final assertion. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES as fx
    from ..decision.options import record
    from ..queries.person_q import LedgerReader
    from ..state.ledgers import eviction_key

    p = P.tiny_world().persons["p_low"]
    older = Claim("c_old", p.id, "Hh", "stores:grain", 5, 1, "firsthand", 100, "own")
    newer = Claim("c_new", p.id, "Hh", "stores:grain", 6, 5, "firsthand", 20, "own")
    told = Claim("c_told", p.id, "Hh", "stores:grain", 6, 6, "told_by", 100, "own", chain=("x",))
    p.ledger[:] = [newer, older, told]
    assert sorted(p.ledger[:2], key=lambda c: eviction_key(c.confidence, c.when)) == [newer, older], (
        "the fixture is not in eviction order: it cannot tell the two pickers apart")
    assert LedgerReader(p.ledger).read("Hh", "stores:grain") == 6, "the belief is not the newer claim"
    assert [c for c in p.ledger if not c.chain][-1] is older, "the last-listed firsthand claim moved"
    assert record(p, "x", fx) == 1.5, (
        f"`record` read {record(p, 'x', fx)}: the told claim was paired against a claim other than "
        "the one `LedgerReader` calls the belief")


def test_t6_a_seen_pair_and_an_event_kind_pair_are_not_scored():
    """ONLY CELLS PAIR. A `seen` claim carries a different `Seen` value per sighting, so a teller
    passing a sighting on would score as CONTRADICTING the very sighting; an event-kind claim
    (`news.told`) is always `True`, so a pair of them would AGREE for free. Neither is a cell, so
    both read exactly 1.0 (no pair). The controls run on the same ledger shape with a cell
    predicate: a disagreeing pair reads 0.5 and an agreeing pair 1.5, so a `record` that read
    nothing, or one that paired everything, is told apart from this one.

    MUTATION (run 2026-10-01, `T6`): the `_is_cell` filter removed from `record` -- the `seen` pair
    reads 0.5 and the event-kind pair 1.5, and this goes RED on the first assertion. Restored,
    GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES as fx
    from ..decision.options import record
    from ..epistemic import Seen

    def rec(predicate, own_value, told_value, source="firsthand"):
        p = P.tiny_world().persons["p_low"]
        p.ledger[:] = [
            Claim("c_own", p.id, "Hh", predicate, own_value, 1, source, 100, "own"),
            Claim("c_told", p.id, "Hh", predicate, told_value, 2, "told_by", 100, "own", chain=("x",))]
        return record(p, "x", fx)

    a = Seen(stratum="social", marks=("tall",), who="p_x")
    b = Seen(stratum="social", marks=("short",), who="p_x")
    assert a != b
    assert rec(SEEN_PREDICATE, a, b) == 1.0, "a `seen` pair was scored"
    assert rec("news.told", True, True) == 1.0, "an event-kind pair was scored"
    assert rec("stores:grain", 5, 0) == 0.5, "the control: a disagreeing cell pair does not register"
    assert rec("stores:grain", 5, 5) == 1.5, "the control: an agreeing cell pair does not register"


# ---------------------------------------------------------------------------------------------
# T7 (v9 IN-16, G9 declared intent, `ED-IN-0282`; `H-190`, `H-191`): A TELLER MAY TELL A HEARER AN
# ACT THEY HAVE CHOSEN AND NOT YET DONE. `decision/choose.py::declare_intents` swaps a telling's
# `said` for `queries/person_q.py::intent_said(...)` with chance `intent_disclosure` (control 0,
# shipped 0); the told deposit lands `(teller, intent:<verb>, ((name, id), ...))` in each hearer's
# ledger; `queries/world_q.py::named` reads the ids back for `questions_for`'s clause 3.
# ---------------------------------------------------------------------------------------------

class _T7Always:
    """A draw stream whose every draw discloses (`random() < rate` for any rate > 0)."""

    def random(self):
        return 0.0


def _t7_scenes(w, teller, topic, later, same_scene=()):
    """`teller`'s own triage as `pack_scenes` returns it: scene 0 a telling about `topic` to
    `p_high`, carrying what the teller holds about it (`said_of`, as `opening_set` sets it), plus
    `same_scene` acts beside it; then one scene per `(verb, payload)` in `later` -- acts the teller
    has chosen and that have not run."""
    from ..state.carriers import Scene
    p = w.persons[teller]
    said = said_of(p.ledger, topic, w.fixtures)
    assert said is not None, f"{teller} holds nothing about {topic}: the telling would not form"
    tell = Act(f"a_t7_tell_{topic}", teller, "tell",
               payload={"subject": topic, "to": "p_high", "said": said})
    first = [tell] + [Act(f"a_t7_same_{n}", teller, v, payload=pay)
                      for n, (v, pay) in enumerate(same_scene)]
    scenes = [Scene("sc_t7_0", teller, first)]
    for n, (verb, pay) in enumerate(later, 1):
        scenes.append(Scene(f"sc_t7_{n}", teller, [Act(f"a_t7_{n}", teller, verb, payload=pay)]))
    return p, tell, scenes


def _t7_hear(w, act):
    """One telling through the REAL WITNESS barrier (`_t5_world`'s drive, with the act built by the
    caller): whoever stands with the teller hears it."""
    d = SeasonDriver(w)
    w.tick += 1
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, act.actor, f"ev:news.told:{act.id}"), "news.told",
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d.act_of[ev.id] = act
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])


def _t7_own(w, pid, subject, value=7):
    w.persons[pid].ledger.append(
        Claim(f"c_t7_{pid}_{subject}", pid, subject, "stores:grain", value, 0, "firsthand", 100, "own"))


def test_t7_a_hearer_holds_the_tellers_chosen_not_done_act():
    """THE PLAN'S FALSIFIER, ABOVE 0. `p_mid` holds a claim about `Hh` and has chosen, this season, a
    telling about `Hh` (scene 0) and a `transfer` out of `Hh` (scene 1, not yet run). At
    `intent_disclosure` 1.0 the telling's `said` becomes the intent, and every hearer -- the people
    standing with `p_mid` -- holds `(p_mid, intent:transfer, (("subject", "Hh"), ("to", "S")))` as a
    `told_by` claim whose chain is the teller; the `transfer` is in no act store and no log when they
    hear it. THE CONTROL is the same triage at 0: the telling passes on the held `stores:grain`
    claim, as before `T7`, and nobody holds an intent.

    MUTATION (run 2026-10-09, `T7`): `declare_intents`' swap line deleted (`a.payload = ...`) -- the
    1.0 arm deposits the `stores:grain` claim and this goes RED on the `said` assertion. Restored,
    GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision.choose import declare_intents
    from ..queries.person_q import INTENT_STEM
    from ..state.ids import draw_factory

    teller = "p_mid"
    held = {}
    for rate in (0.0, 1.0):
        w, _tell, _told = _t5_world()
        _t7_own(w, teller, "Hh")
        p, tell, scenes = _t7_scenes(w, teller, "Hh", [("transfer", {"subject": "Hh", "to": "S"})])
        before = tell.payload["said"]
        assert before.predicate == "stores:grain" and before.subject == "Hh"
        fx = DEFAULT_FIXTURES.sweep("intent_disclosure", rate)
        assert declare_intents(p, scenes, fx, draw_factory(w.world_seed, lambda: w.tick)) is scenes
        said = tell.payload["said"]
        assert not any(a.actor == teller and a.verb == "transfer" for a in w.acts)
        assert not any(e.kind.startswith("transfer") for e in w.log)
        _t7_hear(w, tell)
        held[rate] = {pid: [(c.subject, c.predicate, c.value, c.source, c.chain) for c in q.ledger
                            if str(c.predicate).startswith(f"{INTENT_STEM}:")]
                      for pid, q in w.persons.items()}
        if rate == 0.0:
            assert said is before, "the control touched the telling's `said`"
            assert not any(held[rate].values()), f"an intent was held at the control: {held[rate]}"
            told = [pid for pid, q in w.persons.items()
                    if any(c.predicate == "stores:grain" and c.chain == (teller,) for c in q.ledger)]
            assert told, "the control's telling reached nobody, so its silence proves nothing"
            continue
        want = (teller, f"{INTENT_STEM}:transfer", (("subject", "Hh"), ("to", "S")), "told_by",
                (teller,))
        assert said == Said(teller, want[1], want[2], DEFAULT_FIXTURES.get("confidence_default"), ())
        checked = 0
        for pid, rows in held[rate].items():
            if pid == teller:
                assert rows == [], "the teller deposited their own intent"
                continue
            if rows:
                assert rows == [want], (pid, rows)
                checked += 1
        assert checked >= 1, "no hearer holds the declared intent"


def test_t7_the_intent_is_the_first_later_act_that_names_the_topic():
    """WHICH CHOSEN ACT IS DECLARED. A telling about `Hh` sits in scene 0 beside a `move` naming `Hh`
    (the SAME scene: it runs with the telling, so it is not "not yet done"); scene 1 is a `move` to
    `S` (does not name `Hh`); scene 2 a `transfer` out of `Hh`. The intent is the `transfer`. A
    SELF-telling (topic = the teller, Decision 3) declares the first later act whatever it names:
    the `move` to `S`. A telling in the last scene has no later act and is untouched.

    MUTATION (run 2026-10-09, `T7`, with the first test's): the swap line deleted -- RED on the
    first `predicate` assertion. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision.choose import declare_intents

    fx = DEFAULT_FIXTURES.sweep("intent_disclosure", 1.0)
    always = lambda _pid, _purpose: _T7Always()
    later = [("move", {"subject": "S"}), ("transfer", {"subject": "Hh", "to": "S"})]
    w = P.tiny_world()
    _t7_own(w, "p_mid", "Hh")
    _t7_own(w, "p_mid", "p_mid")
    p, tell, scenes = _t7_scenes(w, "p_mid", "Hh", later, same_scene=[("move", {"subject": "Hh"})])
    declare_intents(p, scenes, fx, always)
    assert tell.payload["said"].predicate == "intent:transfer", tell.payload["said"]
    p, tell, scenes = _t7_scenes(w, "p_mid", "p_mid", later)
    declare_intents(p, scenes, fx, always)
    assert tell.payload["said"].predicate == "intent:move", tell.payload["said"]
    assert tell.payload["said"].value == (("subject", "S"),)
    p, tell, scenes = _t7_scenes(w, "p_mid", "Hh", [])
    before = tell.payload["said"]
    declare_intents(p, scenes, fx, always)
    assert tell.payload["said"] is before, "a telling with no later act declared something"


def test_t7_an_intent_names_its_target_into_the_hearers_question():
    """THE `world_q` BRANCH. `p_low` holds, as a fresh `told_by` claim, that `x_far` -- an id with no
    place and outside `p_low`'s reach -- intends to `fight` `p_low`. `named` returns `("p_low",)`, so
    `questions_for`'s clause 3 raises a `claim_landed` question about `x_far`. THE CONTROL is the
    same claim, same value, under a cell predicate: `named` returns `()` and no question forms, so
    the question is the intent branch's and not clause 1 or 2's.

    MUTATION (run 2026-10-09, `T7`): `named`'s intent branch disabled (`if False:`) -- `named`
    returns `()` for the intent claim and this goes RED. Restored, GREEN."""
    from ..queries.world_q import named, questions_for

    for predicate, want in (("intent:fight", ("p_low",)), ("stores:grain", ())):
        w = P.tiny_world()
        low = w.persons["p_low"]
        c = Claim("c_t7_intent", "p_low", "x_far", predicate, (("subject", "p_low"),), w.tick,
                  "told_by", 100, "own", 0, chain=("x_far",))
        low.ledger.append(c)
        assert named(c) == want, (predicate, named(c))
        qs = [q for q in questions_for(w, low) if q.about == c.id]
        if want:
            assert [(q.source, q.referents) for q in qs] == [("claim_landed", ("x_far",))], qs
        else:
            assert qs == [], f"the control claim raised a question by another clause: {qs}"


def test_t7_the_claim_kind_and_the_rate_refuse_what_they_cannot_mean():
    """`intent_disclosure` is a chance: outside [0, 1] (or NaN) it raises, and a non-zero rate with a
    telling to declare and no draw raises rather than declaring every intent or none; at 0 nothing
    is read, so no draw is needed. The claim kind's stem is refused at import if another reader
    already answers it -- a `requires` stem, the `seen` predicate, the `content:` predicate, an
    emitted event kind -- or if it carries a colon, and a carried name that is no operand refuses."""
    import pytest
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..data.requires import REQUIRES_OPERANDS, REQUIRES_STEMS
    from ..data.rosters import RECORD_CONTENT
    from ..decision.choose import declare_intents
    from ..gaps import Unspecified
    from ..queries.person_q import INTENT_NAMES, INTENT_STEM, _check_intent_claim

    w = P.tiny_world()
    _t7_own(w, "p_mid", "Hh")
    p, _tell, scenes = _t7_scenes(w, "p_mid", "Hh", [("transfer", {"subject": "Hh"})])
    for bad in (-0.1, 1.5, float("nan")):
        with pytest.raises(ValueError):
            declare_intents(p, scenes, DEFAULT_FIXTURES.sweep("intent_disclosure", bad), None)
    with pytest.raises(Unspecified):
        declare_intents(p, scenes, DEFAULT_FIXTURES.sweep("intent_disclosure", 0.5), None)
    assert declare_intents(p, scenes, DEFAULT_FIXTURES.sweep("intent_disclosure", 0.0), None) is scenes
    taken = {SEEN_PREDICATE, RECORD_CONTENT.get("predicate"), "news.told"}
    _check_intent_claim(INTENT_STEM, INTENT_NAMES, REQUIRES_STEMS, REQUIRES_OPERANDS, taken)
    for stem in ("stores", SEEN_PREDICATE, RECORD_CONTENT.get("predicate"), "news.told", "intent:x", ""):
        with pytest.raises(ValueError):
            _check_intent_claim(stem, INTENT_NAMES, REQUIRES_STEMS, REQUIRES_OPERANDS, taken)
    with pytest.raises(ValueError):
        _check_intent_claim(INTENT_STEM, ("subject", "bogus"), REQUIRES_STEMS, REQUIRES_OPERANDS, taken)


def test_t7_intent_disclosure_zero_is_the_control_on_the_realm(monkeypatch):
    """THE PLAN'S FALSIFIER, AT 0. `build_realm(0)`, one season, run twice: once through the shipped
    chooser at `intent_disclosure` 0, once with `declare_intents` excised (the pre-`T7` chooser,
    which returned `pack_scenes`' scenes as they were). Equal in BOTH observables: the
    `content_hash()`, and what every act in the store CARRIED -- `(act id, said)` -- because a
    payload is not hashed (`T1`), and in the realm's first season every telling that carries an
    intent is refused (`news.untold`), so a leak at 0 moves the said and not the hash (scratch
    `t7_arms.py`: the one-season hash is d0015936 at 0, 0.5 and 1.0; at three seasons 0.5 moves it).
    [GROUNDED: measured 2026-10-09 on the pre-rebase base a59d52f9 (off HEAD's first-parent line,
    reachable only through the merge 48991c37), BEFORE T7's first edit:
    `build_realm(0)` 5b8618f2..., one season d0015936..., three seasons 43b1fac8...; after T7, at
    `intent_disclosure` 0, d0015936 and 43b1fac8 again -- scratch, not re-read here.]
    The control is NOT VACUOUS: the shipped arm's `declare_intents` is spied, and on a COPY of each
    triage the same rule at 1.0 (a draw that always discloses) counts the tellings that had a
    chosen-not-done act to declare (`checked >= 1`); at least one telling in the store carries a
    `said` (so the said comparison compares something).

    MUTATION (run 2026-10-09, `T7`): the `rate == 0` early return deleted and the draw test made
    `<=` (every opportunity declares at 0) -- the hashes still match and this goes RED on the
    `said` comparison. Restored, GREEN."""
    import copy
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision import choose as CH

    assert DEFAULT_FIXTURES.get("intent_disclosure") == 0, "the shipped rate moved: restate this test"
    real = CH.declare_intents
    seen = {"calls": 0, "opportunities": 0}

    def spy(p, scenes, fx, draw=None):
        assert fx.get("intent_disclosure") == 0
        seen["calls"] += 1
        copies = copy.deepcopy(scenes)
        before = [a.payload.get("said") for sc in copies for a in sc.acts if isinstance(a.payload, dict)]
        real(p, copies, fx.sweep("intent_disclosure", 1.0), lambda _p, _u: _T7Always())
        after = [a.payload.get("said") for sc in copies for a in sc.acts if isinstance(a.payload, dict)]
        seen["opportunities"] += sum(1 for b, a in zip(before, after) if a is not b)
        return real(p, scenes, fx, draw)

    hashes, carried = {}, {}
    for arm, fn in (("shipped", spy), ("excised", lambda p, scenes, fx, draw=None: scenes)):
        monkeypatch.setattr(CH, "declare_intents", fn)
        w = populated.build_realm(0)
        populated.run(1, 0, w=w)
        hashes[arm] = w.content_hash()
        carried[arm] = [(a.id, a.payload.get("said")) for a in w.acts
                        if isinstance(a.payload, dict) and a.payload.get("said") is not None]
    print(f"\n  T7 -- realm one season at intent_disclosure 0: {seen['calls']} triages, "
          f"{seen['opportunities']} tellings with a declarable intent, {len(carried['shipped'])} "
          f"acts carrying a said; hash {hashes['shipped']}")
    assert seen["calls"] >= 1 and seen["opportunities"] >= 1, seen
    assert len(carried["shipped"]) >= 1, "no act in the store carried a said: nothing was compared"
    assert carried["shipped"] == carried["excised"], "a telling's said differs from the pre-T7 chooser's"
    assert hashes["shipped"] == hashes["excised"], hashes


# ---------------------------------------------------------------------------------------------------
# v9 IN-18 `G1` -- JUDGED REGARD (`queries/person_q.py::regard`, `deeds_judged`; H-192, H-193).
# ---------------------------------------------------------------------------------------------------

def _g1_split():
    """A DEED KIND AND TWO PURSUITS THAT JUDGE IT OPPOSITELY, read off the shipped tables -- nothing
    planted: the first DEED kind (sorted; an `EMITTED_KINDS` member no row emits on refusal, as
    `person_q.is_deed` reads it) on which some pursuit's projection, dotted with `align_kind`, is
    positive and another's negative. Returns `(kind, pursuit_for, pursuit_against)`."""
    from ..data import verbs as V
    from ..data.pursuits import to_axes
    from ..data.rosters import PURSUIT_AXES, PURSUITS

    def dot(e, k):
        ax = to_axes({e: 1.0})
        return sum(ax[a] * V.align_kind(k, a) for a in PURSUIT_AXES)

    for k in sorted(V.DEED_KINDS):
        d = {e: dot(e, k) for e in sorted(PURSUITS)}
        pos = [e for e in d if d[e] > 0]
        neg = [e for e in d if d[e] < 0]
        if pos and neg:
            return k, pos[0], neg[0]
    raise AssertionError("no emitted kind splits two pursuits by sign: G1's falsifier has no deed")


def _g1_fx(judged, told):
    from ..data.fixtures import DEFAULT_FIXTURES
    return DEFAULT_FIXTURES.sweep("judged_gain", judged).sweep("told_valence_gain", told)


def _g1_hearers(kind, pro, con, chain=()):
    """`p_low` holds `pro` and `p_mid` holds `con`, each at weight 1, NO stance row; both hold the
    same deed claim `(p_other, kind, True)` -- firsthand with an empty `chain`, else told by it."""
    w = P.tiny_world()
    for pid, e in (("p_low", pro), ("p_mid", con)):
        p = w.persons[pid]
        p.pursuits = {e: 1.0}
        assert not p.stance, f"{pid} carries a stance row: the stored half would not be 0"
        p.ledger.append(Claim(f"c_g1_{pid}", pid, "p_other", kind, True, 0, "firsthand", 100, "own",
                              chain=chain))
    return w, w.persons["p_low"], w.persons["p_mid"]


def test_g1_opposite_pursuits_judge_one_deed_with_opposite_regard():
    """THE PLAN'S FALSIFIER (§5 row G1): *"no planted rows; two hearers, opposite `pursuits` on a
    deed's axis, same deed claim about X: `regard` signs differ; both 0 at control."* No stance row,
    no alignment cell planted: the kind and the two pursuits are read off the shipped tables. Both
    halves: the deed held firsthand moves the JUDGED half, the same deed told moves the TOLD half,
    and each gain alone moves only its own half.

    MUTATION (run 2026-10-09, IN-18): `deeds_judged` returning `(0.0, 0.0)` reddens the sign
    assertions; `regard` ignoring `fx` (returning the stored half) reddens them too. Restored, GREEN."""
    from ..queries.person_q import regard, stance_toward
    kind, pro, con = _g1_split()
    checked = 0
    for chain, live in (((), _g1_fx(0.5, 0.0)), (("p_king",), _g1_fx(0.0, 0.5))):
        w, a, b = _g1_hearers(kind, pro, con, chain)
        ra, rb = regard(a, "p_other", live), regard(b, "p_other", live)
        assert ra > 0 > rb, (kind, pro, con, chain, ra, rb)
        # CONTROL: both gains 0 -- and no `fx` at all -- is the stored half, which is 0 here.
        for fx in (_g1_fx(0.0, 0.0), None):
            assert regard(a, "p_other", fx) == regard(b, "p_other", fx) == 0.0
        assert stance_toward(a, "p_other") == stance_toward(b, "p_other") == 0.0
        # Each gain reads only its own half: the firsthand deed is invisible to the told gain, and
        # the told one to the judged gain.
        other = _g1_fx(0.0, 0.5) if not chain else _g1_fx(0.5, 0.0)
        assert regard(a, "p_other", other) == regard(b, "p_other", other) == 0.0
        checked += 1
    assert checked == 2


def test_g1_regard_at_control_reads_no_ledger_and_a_victims_kind_judges_nothing():
    """At both gains 0 `regard` is `stance_toward` and never scans the ledger (so the control cannot
    differ from the pre-G1 reader by construction); and a kind several rows emit -- the ones whose
    claim subject may be the PATIENT, `person.died` among them -- has no `KIND_VERB` and judges 0."""
    from ..data import verbs as V
    from ..queries import person_q as PQ
    kind, pro, con = _g1_split()
    w, a, _b = _g1_hearers(kind, pro, con)

    class _Boom(list):
        def __iter__(self):
            raise AssertionError("the control read the ledger")

    a.ledger = _Boom(a.ledger)
    assert PQ.regard(a, "p_other", _g1_fx(0.0, 0.0)) == 0.0
    a.ledger = list(a.ledger.copy())
    assert "person.died" in V.EMITTED_KINDS and "person.died" not in V.KIND_VERB
    a.ledger.append(Claim("c_g1_died", a.id, "p_other", "person.died", True, 0, "firsthand", 100, "own"))
    j_with, _ = PQ.deeds_judged(a, "p_other")
    a.ledger.pop()
    j_without, _ = PQ.deeds_judged(a, "p_other")
    assert j_with == j_without > 0, (j_with, j_without)


def test_g1_a_told_by_deed_with_an_empty_chain_is_told_not_judged():
    """`judged` IS FIRSTHAND ONLY (`H-193`): a deed claim sourced `told_by` with an empty `chain` is
    hearsay, and lands in `told`. CONTROL: the same claim sourced `firsthand` lands in `judged`."""
    from dataclasses import replace
    from ..queries import person_q as PQ
    kind, pro, con = _g1_split()
    w, a, _b = _g1_hearers(kind, pro, con)
    (c,) = [c for c in a.ledger if c.subject == "p_other" and c.predicate == kind]
    j_first, t_first = PQ.deeds_judged(a, "p_other")
    assert j_first != 0.0 and t_first == 0.0, (j_first, t_first)
    a.ledger = [x for x in a.ledger if x is not c] + [replace(c, source="told_by", chain=())]
    assert PQ.deeds_judged(a, "p_other") == (0.0, j_first)


def test_g1_a_refusal_is_no_deed():
    """A REFUSAL REPORTS AN ACT THAT DID NOT HAPPEN (`data/verbs.py::REFUSAL_KINDS`): a firsthand
    `kill.refused` about V judges nothing. `kill.refused` has a `KIND_VERB` (one row emits it), so
    without the exclusion it would be scored as that verb's deed. `news.untold`, which `tell` emits
    on success AND refusal, is no deed either."""
    from ..data import verbs as V
    from ..data.pursuits import to_axes
    from ..data.rosters import PURSUIT_AXES, PURSUITS
    from ..queries import person_q as PQ
    kind = "kill.refused"
    assert kind in V.REFUSAL_KINDS and V.KIND_VERB.get(kind), "the falsifier needs a scored kind"
    w = P.tiny_world()
    a = w.persons["p_low"]
    # CONTROL that the claim WOULD score: a pursuit under which the refusal's verb leans non-zero.
    e = next(e for e in sorted(PURSUITS)
             if sum(to_axes({e: 1.0})[x] * V.align_kind(kind, x) for x in PURSUIT_AXES))
    a.pursuits = {e: 1.0}
    a.ledger = [x for x in a.ledger if x.subject != "p_other"] + [
        Claim("c_g1_ref", a.id, "p_other", kind, True, 0, "firsthand", 100, "own")]
    assert PQ.deeds_judged(a, "p_other") == (0.0, 0.0)
    assert not PQ.is_deed(Claim("c_untold", a.id, "p_other", "news.untold", True, 0, "firsthand",
                                100, "own"))


def _r07_pairs(w, fx):
    """R-07's reading over one world: for every person `C` and every pair of persons holding a claim
    about `C` (neither of them `C`), whether their `regard` of `C` differs BEYOND their stored
    stance -- `regard - stance_toward` unequal, so the difference is a claim's or a teller's and not
    stance alone. Returns `(pairs read, pairs differing beyond stance)`."""
    from ..queries.person_q import regard, stance_toward
    holders: dict = {}
    for p in w.persons.values():
        for c in p.ledger:
            if c.subject in w.persons and c.subject != p.id:
                holders.setdefault(c.subject, set()).add(p.id)
    read = differ = 0
    for subject, ids in sorted(holders.items()):
        beyond = sorted((regard(w.persons[i], subject, fx) - stance_toward(w.persons[i], subject), i)
                        for i in ids)
        for n, (a, _ia) in enumerate(beyond):
            for b, _ib in beyond[n + 1:]:
                read += 1
                differ += a != b
    return read, differ


def test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone():
    """R-07'S REALM READER (v9 IN-18 EXIT, `_part2` R-07): a two-season `build_realm(0)` run at G1's
    LIVE arm -- the SHIPPED fixtures, `judged_gain` and `told_valence_gain` 0.5 (the sweep midpoint,
    shipped live per Jordan's 2026-10-09 ruling) -- reads `regard(p, C)` for every pair of persons
    holding a claim about one `C`, and at least one pair's regard differs because of a claim (or a
    teller) and not from stored stance alone; the same run at G1's CONTROL arm -- both gains set to
    0 explicitly, every other fixture shipped -- shows no such pair, while reading at least as many.

    MUTATION (run 2026-10-09, IN-18): `regard` returning the stored half whatever `fx` reddens the
    live arm's `differ >= 1`. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    assert DEFAULT_FIXTURES.get("judged_gain") == 0.5 and DEFAULT_FIXTURES.get("told_valence_gain") == 0.5, (
        "G1's shipped gains moved: restate this test's live arm")
    out = {}
    for arm, fx in (("control", _g1_fx(0.0, 0.0)),
                    ("live", DEFAULT_FIXTURES)):
        w = populated.build_realm(0)
        w.fixtures = fx
        populated.run(2, 0, w=w)
        out[arm] = _r07_pairs(w, fx)
    print(f"\n  R-07 -- realm two seasons, (pairs read, differing beyond stance): {out}")
    assert out["control"][0] >= 1 and out["live"][0] >= 1, out
    assert out["control"][1] == 0, out
    assert out["live"][1] >= 1, out


# ---------------------------------------------------------------------------------------------------
# v9 IN-18 `G2` -- POLARITY IN §F2 TERM 2 (`decision/choose.py::stance_term`; H-194, H-195).
# ---------------------------------------------------------------------------------------------------

def _g2_ranked(arm, cands, stance, monkeypatch):
    """`make_chooser`'s real ranking of `cands` for a person with NO pursuits (term 1 is 0 for every
    candidate) and the stance rows `stance`, at `stance_polarity == arm`, temperature 0."""
    from types import SimpleNamespace
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision import choose as CH
    from ..state.carriers import Person
    p = Person(id="p_g2", name="p_g2")
    p.stance = list(stance)
    seen = {}
    monkeypatch.setattr(CH, "opening_set", lambda person, view, q, fx: list(cands))

    def spy(person, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = [(c.verb, c.subject) for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    fx = DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("stance_polarity", arm)
    CH.make_chooser(fx, lambda *a: "act")(p, SimpleNamespace(question=object()),
                                         SimpleNamespace(subsistence=0), lambda: 1)
    assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
    return seen["ranked"]


def test_g2_a_grudge_raises_fight_on_its_object_under_declared_not_legacy(monkeypatch):
    """THE PLAN'S FALSIFIER (§5 row G2), its observable half: *"`fight` against the disliked
    rises"* under `declared` against `legacy` (`checked >= 1`). A person holding `march`'s grudge
    shape -- `(X, -1.0, weight)`, `loop/effects_combat.py::_eff_march`'s row -- toward `p_x` and
    nothing toward `p_y`: under `legacy` `fight` on `p_x` ranks BELOW `fight` on `p_y` (the old term
    adds the negative stance), under `declared` ABOVE it. Rows not contested against their subject
    keep the sign on both arms (`tell` is contested against its `to`, not its topic).

    The falsifier's `march` half -- members of a faction choose `march` on F-held rungs more -- is
    NOT observable while the `holder` operand reads 0 (`H-195`: no ledger holds a `held_by` claim,
    M0g 0 % on `build_realm(0)`), so a rung subject's term is 0 on both arms, asserted below.

    MUTATION (run 2026-10-09, IN-18): `stance_term`'s negation removed (declared returns `r`)
    reddens the `declared` ordering. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..data.verbs import VERB_TABLE
    from ..decision.choose import stance_term
    from ..decision.options import subject_is_opponent
    from ..state.carriers import Candidate, Person
    assert DEFAULT_FIXTURES.get("stance_polarity") == "legacy", "the shipped arm moved: restate"
    assert subject_is_opponent(VERB_TABLE["fight"]) and not subject_is_opponent(VERB_TABLE["tell"])
    grudge = [("p_x", -1.0, 3.0)]
    cands = [Candidate("fight", "p_x"), Candidate("fight", "p_y")]
    checked = 0
    legacy = _g2_ranked("legacy", cands, grudge, monkeypatch)
    declared = _g2_ranked("declared", cands, grudge, monkeypatch)
    assert legacy == [("fight", "p_y"), ("fight", "p_x")], legacy
    assert declared == [("fight", "p_x"), ("fight", "p_y")], declared
    checked += 1
    p = Person(id="p_g2", name="p_g2")
    p.stance = list(grudge)
    # The term's SIGN at the CONTROL gains, set explicitly: `stance_gain` (H-202) and G1's two gains
    # (H-192/H-193) ship live (Jordan, 2026-10-09), and this test reads polarity, not magnitude --
    # `test_in25_stance_gain.py` owns the gain's scaling.
    ctl = (DEFAULT_FIXTURES.sweep("stance_gain", 0.0).sweep("judged_gain", 0.0)
           .sweep("told_valence_gain", 0.0))
    for arm in ("legacy", "declared"):
        fx = ctl.sweep("stance_polarity", arm)
        # a row NOT contested against its subject keeps the sign: telling about the disliked
        assert stance_term(p, Candidate("tell", "p_x"), fx) == -3.0
        # a Rung subject reads 0 on both arms: its holder is the absent operand (H-195)
        assert stance_term(p, Candidate("march", "R"), fx) == 0.0
    assert stance_term(p, Candidate("fight", "p_x"), ctl.sweep("stance_polarity", "declared")) == 3.0
    # the `regard` midpoint: G1's regard, no sign -- at G1's control gains it is the legacy term
    assert stance_term(p, Candidate("fight", "p_x"), ctl.sweep("stance_polarity", "regard")) == -3.0
    assert checked >= 1


def test_g2_an_unknown_polarity_arm_refuses():
    import pytest
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision.choose import stance_term
    from ..state.carriers import Candidate, Person
    with pytest.raises(Exception, match="stance polarity"):
        stance_term(Person(id="p", name="p"), Candidate("fight", "p_x"),
                    DEFAULT_FIXTURES.sweep("stance_polarity", "inverted"))


# ---------------------------------------------------------------------------------------------------
# v9 IN-18 `G3` -- SLANT (`queries/person_q.py::said_of`; H-196).
# ---------------------------------------------------------------------------------------------------

def test_g3_the_strongly_valenced_older_claim_is_told_under_valence_the_newer_at_control():
    """THE PLAN'S FALSIFIER (§5 row G3): *"the strongly valenced older claim is told under
    `valence`, the newer neutral one at control."* The teller holds, about `p_other`, an OLDER deed
    claim their own pursuits judge strongly (`_g1_split`'s kind, read off the shipped tables) and a
    NEWER claim no pursuit judges (`exists:Person`). At `newest` -- and with no teller, and at no
    `fx` -- the newer is said; at `valence` the older deed. A teller whose pursuits judge nothing
    says the newer at `valence` too (no valenced claim: the unslanted pick exactly).

    MUTATION (run 2026-10-09, IN-18): the narrowing deleted (`valence` keeps the whole pool)
    reddens the `valence` assertion. Restored, GREEN."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..queries.person_q import said_of
    assert DEFAULT_FIXTURES.get("said_slant") == "newest", "the shipped arm moved: restate"
    kind, pro, _con = _g1_split()
    w = P.tiny_world()
    p = w.persons["p_low"]
    p.pursuits = {pro: 1.0}
    old = Claim("c_g3_old", p.id, "p_other", kind, True, 0, "firsthand", 100, "own")
    new = Claim("c_g3_new", p.id, "p_other", "exists:Person", 1, 3, "firsthand", 100, "own")
    p.ledger.extend([old, new])
    slant = DEFAULT_FIXTURES.sweep("said_slant", "valence")
    for fx, teller in ((DEFAULT_FIXTURES, p), (slant, None), (None, p)):
        assert said_of(p.ledger, "p_other", fx, teller=teller).predicate == "exists:Person"
    assert said_of(p.ledger, "p_other", slant, teller=p).predicate == kind
    p.pursuits = {}
    assert said_of(p.ledger, "p_other", slant, teller=p).predicate == "exists:Person"


def test_g3_an_unknown_slant_refuses():
    import pytest
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..queries.person_q import said_of
    w = P.tiny_world()
    p = w.persons["p_low"]
    p.ledger.append(Claim("c_g3", p.id, "Hh", "exists:Rung", 1, 0, "firsthand", 100, "own"))
    with pytest.raises(ValueError, match="said_slant"):
        said_of(p.ledger, "Hh", DEFAULT_FIXTURES.sweep("said_slant", "loudest"), teller=p)


def test_claim_firsthand_needs_an_empty_chain_and_the_firsthand_source():
    def c(chain, source):
        return Claim("c", "p", "Hh", "stores:grain", 8, 0, source, 100, "own", chain=chain)
    assert [c((), "firsthand").firsthand, c((), "told_by").firsthand,
            c(("x",), "firsthand").firsthand] == [True, False, False]


# ---------------------------------------------------------------------------------------------------
# v9 IN-18 `G6` -- CONFIDENCES (`loop/witness.py::_circle_of`, `loop/resolve.py::_confidence_broken`;
# H-197). §5 row G6's falsifier: *"a private telling deposits `visibility == (A, B)`; retelling outside
# it emits `confidence.broken`"*. Driven through the REAL fold (`_fold` at a told band, as `resolve()`'s
# seam branch calls it) and the REAL WITNESS barrier, `test_t4_a_telling_to_an_absent_hearer_...`'s drive.
# `tiny_world`: `p_low`, `p_mid`, `p_other` stand in `Hh`, so each hears every telling made there.
# ---------------------------------------------------------------------------------------------------

_G6_SUBJECT, _G6_PRED, _G6_VALUE = "Hh", "stores:grain", 8


def _g6_world(rate):
    """`tiny_world` at `telling_privacy` `rate` (`None`: the shipped fixtures, untouched), `p_low`
    holding `(Hh, stores:grain, 8)` firsthand. Returns `(w, tell, told)`: `tell(teller, to)` folds a
    `tell` about `Hh` carrying `said_of(teller's own ledger)` at `Success` and runs WITNESS on what it
    emitted, returning the kinds; `told(pid)` is `pid`'s told copies of the cell."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..data.matrix import Step
    from ..seam import Resolution
    fx = DEFAULT_FIXTURES if rate is None else DEFAULT_FIXTURES.sweep("telling_privacy", rate)
    w = P.tiny_world(fx)
    w.persons["p_low"].ledger.append(Claim("c_g6_held", "p_low", _G6_SUBJECT, _G6_PRED, _G6_VALUE,
                                           0, "firsthand", 37, "own"))
    d = SeasonDriver(w)
    n = [0]

    def tell(teller, to):
        n[0] += 1
        w.tick += 1
        # What `said_of` copies out of a claim, from the teller's copy of THE CELL: a hearer also
        # holds `(Hh, news.told, True)` firsthand from having heard, and `said_of`'s newest-first pick
        # would pass that on instead (G3's `newest`), which is not the retelling under test.
        mine = [c for c in w.persons[teller].ledger
                if (c.subject, c.predicate, c.value) == (_G6_SUBJECT, _G6_PRED, _G6_VALUE)]
        assert len(mine) == 1, f"{teller} holds {len(mine)} copies of the cell"
        c = mine[0]
        said = Said(c.subject, c.predicate, c.value, c.confidence, c.chain)
        if n[0] == 1:              # the first telling: the pick `opening_set` makes, observed equal
            assert said_of(w.persons[teller].ledger, _G6_SUBJECT, w.fixtures) == said
        act = Act(id=f"a_g6_{n[0]}", actor=teller, verb="tell",
                  payload={"subject": _G6_SUBJECT, "to": to, "said": said})
        w.step = Step.RESOLVE
        ok, kinds, _ = d._admits(w, act, _tell_row())
        assert ok, f"the telling {teller} -> {to} was refused ({kinds}); the fold never ran"
        w.acts.append(act)
        out = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution("Success", {}))
        w.log.extend(out)
        for e in out:
            d.act_of[e.id] = act
        w.step = Step.WITNESS
        d.witness(mint_token(w, WriteClass.INTERIOR), out)
        return [e.kind for e in out]

    def told(pid):
        return [c for c in w.persons[pid].ledger if c.source == "told_by"
                and (c.subject, c.predicate, c.value) == (_G6_SUBJECT, _G6_PRED, _G6_VALUE)]

    return w, tell, told


def _tell_row():
    from ..data.verbs import VERB_TABLE
    return VERB_TABLE["tell"]


def test_g6_a_private_telling_deposits_the_circle_teller_and_addressee():
    """FALSIFIER (1). At `telling_privacy` 1.0 `p_low` tells `p_mid`: `p_mid` holds the told claim
    `visibility == ("p_low", "p_mid")` -- the circle is the teller and the ADDRESSEE. `p_other`, a
    bystander nobody addressed, still hears (§10 decision 1: recipiency stays WITNESS's) and holds the
    same circle, outside it. The original telling breaks nothing: `p_low`'s own copy is `own`.

    MUTATION (run once at G6, 2026-10-10): `_circle_of` returning `None` (the pre-G6 line) reddens the
    visibility assertion; restored, GREEN."""
    w, tell, told = _g6_world(1.0)
    assert tell("p_low", "p_mid") == ["news.told"]
    checked = 0
    for pid in ("p_mid", "p_other"):
        got = told(pid)
        assert len(got) == 1 and got[0].chain == ("p_low",), [(c.chain, c.visibility) for c in got]
        assert got[0].visibility == ("p_low", "p_mid"), (
            f"{pid} holds the private telling as {got[0].visibility!r}, not the circle (p_low, p_mid)")
        checked += 1
    assert checked == 2
    assert [c.visibility for c in w.persons["p_low"].ledger if c.id == "c_g6_held"] == ["own"]


def test_g6_a_retelling_outside_the_circle_emits_confidence_broken():
    """FALSIFIER (2). `p_mid`, holding `p_low`'s confidence `(p_low, p_mid)`, tells it to `p_other`
    -- outside the circle: the fold emits `news.told` AND `confidence.broken`, and the betrayal is an
    Event WITNESS carries to the people present (an event-kind claim on the broken kind).

    MUTATION (run once at G6, 2026-10-10): `_confidence_broken` returning False reddens the kinds
    assertion; dropping the `hearer not in c.visibility` clause reddens
    `test_g6_a_retelling_inside_the_circle_breaks_nothing`; restored, GREEN."""
    w, tell, told = _g6_world(1.0)
    tell("p_low", "p_mid")
    assert told("p_mid")[0].visibility == ("p_low", "p_mid")
    kinds = tell("p_mid", "p_other")
    assert kinds == ["news.told", "confidence.broken"], kinds
    heard = [c for pid in ("p_low", "p_other") for c in w.persons[pid].ledger
             if c.predicate == "confidence.broken"]
    assert heard, "the broken confidence reached nobody's ledger at WITNESS"


def test_g6_a_retelling_inside_the_circle_breaks_nothing():
    """FALSIFIER (3). `p_mid` tells the confided claim back to `p_low`, the confider -- INSIDE the
    circle: `news.told` alone. And `p_low`, the confider, telling their own claim to `p_other` breaks
    nothing either: their copy is `own` (a confidence binds the hearer, never the teller)."""
    w, tell, told = _g6_world(1.0)
    tell("p_low", "p_mid")
    assert tell("p_mid", "p_low") == ["news.told"]
    assert tell("p_low", "p_other") == ["news.told"]


def test_g6_the_shipped_control_deposits_own_and_breaks_nothing(monkeypatch):
    """FALSIFIER (4). The SHIPPED `telling_privacy` is 0 (the control). At it the deposit is `own`
    and EQUAL to the 1.0 arm's deposit in every other field (so G6 moves `visibility` alone), no draw
    is taken (`draw_factory` replaced by a raiser), and a retelling outside what would have been the
    circle emits `news.told` alone. Hash equality of `build_realm(0)` against the pre-G6 tree holds by
    construction at 0 (no draw, no circle, nothing filtered differently); this observes the deposit."""
    from dataclasses import replace
    from ..data.fixtures import DEFAULT_FIXTURES
    assert DEFAULT_FIXTURES.get("telling_privacy") == 0, "the shipped chance moved: restate this test"
    live_w, live_tell, live_told = _g6_world(1.0)
    live_tell("p_low", "p_mid")

    def _no_draw(*_a, **_k):
        raise AssertionError("a draw was taken at telling_privacy 0")
    monkeypatch.setattr(WITNESS_MODULE, "draw_factory", _no_draw)
    w, tell, told = _g6_world(None)
    assert tell("p_low", "p_mid") == ["news.told"]
    got, live = told("p_mid"), live_told("p_mid")
    assert len(got) == 1 and got[0].visibility == "own", [c.visibility for c in got]
    assert got[0] == replace(live[0], visibility="own"), (got[0], live[0])
    assert all(c.visibility == "own" for pid in w.persons for c in w.persons[pid].ledger)
    assert tell("p_mid", "p_other") == ["news.told"]


def test_g6_the_privacy_chance_refuses_what_is_not_a_chance():
    import pytest
    for bad in (-0.1, 1.5, float("nan")):
        w, tell, _ = _g6_world(bad)
        with pytest.raises(ValueError, match="telling_privacy"):
            tell("p_low", "p_mid")
