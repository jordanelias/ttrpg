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
    def told_by_count() -> tuple:
        w = populated.build_realm(0)
        out = populated.run(1, 0, w=w)
        told_by = [c for p in w.persons.values() for c in p.ledger if c.source == "told_by"]
        channel = sum(1 for c in told_by if c.chain)
        return len(told_by) - channel, channel, sum(out["claim_sources"].values())

    live, live_channel, total = told_by_count()
    assert live > 0, f"every one of {total} deposits is still firsthand -- no hearsay was minted"
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
# T3a (`workplans/2026-10-01-telling-workplan.md`, ED-IN-0282; `H-157`, `H-176`..`H-180`): HEARSAY
# WEIGHED WHEN READ. Until `T3b` a told claim was one hop and its origin its teller; since `T3b`
# hops are `len(Claim.chain)` and the origin is `chain[0]`. A claim with no chain weighs 1.0 and
# its origin is its holder.
# ---------------------------------------------------------------------------------------------

def _t3_fx(told_weight, regard_gain, rank_gain=None):
    from ..data.fixtures import DEFAULT_FIXTURES
    fx = DEFAULT_FIXTURES.sweep("told_weight", told_weight).sweep("regard_gain", regard_gain)
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
    0.5, and while `rank` reads 0 (`H-180`), a one-hop claim weighs at most 0.5 x 1.5 = 0.75
    against a firsthand claim's 1.0, so NO regard
    can make hearsay beat what the hearer saw (`H-178`'s default says so); regard then decides
    only between told claims. Against a firsthand claim the regard term is observable only where
    `told_weight * relation` can reach 1.0. The firsthand and told claims are planted (identically
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

    def spy(pp, row, subject, operands, via=None, weigh=None):
        seen.append(weigh)
        return real(pp, row, subject, operands, via, weigh=weigh)

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
    assert {wt(probe) for wt in seen} == {0.5}, (
        "the weigh opening_set passed does not grade a told claim at the shipped told_weight")


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
    observation `H-178` claims and `test_t3_unplanted_members_...` cannot make, because that one
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
    checked = len(told("p_mid")) + len(told("p_other"))
    assert checked >= 1, "no other hearer was told either: the telling never reached WITNESS"


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

    MUTATION (run 2026-10-01, `T5`): the empty-chain clause removed (`c.chain[0] == _origin`
    alone) -- both holders are told and this goes RED on the first assertion. Restored, GREEN."""
    for source in ("firsthand", "inferred"):
        w, tell, told = _t5_world()
        held = Claim("c_held", "p_high", _T5_SUBJECT, _T5_PRED, 8, 0, source, 100, "own")
        assert held.chain == ()
        w.persons["p_high"].ledger.append(held)
        tell("p_mid", (), 8)
        assert told("p_high") == [], f"a {source} holder was told what they already hold"
        tell("p_low", ("p_mid",), 8)
        assert told("p_high") == [], f"a {source} holder was told the same triple by another origin"
        assert len(told("p_other")) == 1, "the positive control: a hearer who holds nothing is told"

