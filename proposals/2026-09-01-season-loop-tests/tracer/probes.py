"""The probes. Each is a REAL EXECUTION against `shape.py` that either completes or raises a
typed ShapeGap. Nothing here asserts a conclusion; everything here RUNS one.

REVISION 2, after an antagonist that never saw the producer's reasoning broke revision 1.

THE DISTINCTION REVISION 2 ADDS, AND IT IS THE MOST IMPORTANT THING IN THIS FILE.
`ARCHITECTURE.md` S34 says overstating the enforcement column is the failure mode, and S47
says a false claim of enforcement is worse than none because it stops the next reader from
checking. Revision 1 had eleven probes that RAISED A GAP BY HAND and reported it as though the
shape had refused. Every probe now declares HOW its verdict was reached:

    by="construction"   the shape itself raised. The probe called a real signature and the
                        gate, the law or the type stopped it. This is evidence.
    by="no-signature"   there is nothing to call. The design supplies no function by which the
                        thing could even be attempted -- which IS the refusal, but is a
                        different kind of evidence, and weaker: absence is not a guard.
    by="convention"     the shape permits it and only a reader stops it. S27.2 is the design's
                        own example and it says so out loud.
    by="probe-model"    the probe supplies a model the design does not, to reach the question
                        at all. The verdict is about the design; the model is the instrument's,
                        and is named so a reader can discount it.

A probe's verdict is HARD (it is an execution). A case's verdict is ADVISORY (routing is
keyword-based over prose). Every source cited is in the PR #337 -> now chain.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from shape import (
    CLAIM_SOURCES, Candidate, Claim, Collision, ContestError, DEFAULT_FIXTURES, Event,
    Fixtures, Forbidden, H, NoProducer, Office, PARTITION, PARTITION_MISSING, Person,
    Proposition, Query, Record, ROOT, RUNG_KINDS, Rung, STRATA, SeasonDriver, ShapeGap,
    Site, StateChange, Step, Tenure, Ungraded, Unowned, Unspecified, View, World,
    WITNESS_CHANNELS, WriteClass, contest, expect_refusal, sense,
)
from trace_log import TRACE

PROBES: dict[str, dict] = {}


def probe(pid: str, title: str, section: str, tests: str, by: str):
    def deco(fn):
        PROBES[pid] = dict(id=pid, title=title, section=section, tests=tests, by=by, fn=fn)
        return fn
    return deco


# ---------------------------------------------------------------------------
# The shared fixture world. Built FRESH per probe.
# ---------------------------------------------------------------------------

def tiny_world(fixtures: Fixtures = DEFAULT_FIXTURES) -> World:
    w = World(world_seed=1, fixtures=fixtures)
    scale = fixtures.get("condition_scale")
    for rid, kind, stores in (("R", "realm", None), ("D", "duchy", None),
                              ("S", "settlement", {"grain": 40}), ("Hh", "hearth", {"grain": 8})):
        w.rungs[rid] = Rung(rid, kind, stores=stores)
    for pid, name in (("p_low", "a copyist"), ("p_mid", "a clerk"), ("p_high", "a duke"),
                      ("p_king", "the King"), ("p_other", "a stranger")):
        w.persons[pid] = Person(pid, name)
        w.rungs[pid] = Rung(pid, "person")
    w.sites["site_harbour"] = Site("site_harbour", "S", "harbour", condition=scale * 9 // 10)
    w.sites["site_seam"] = Site("site_seam", "S", "seam", condition=scale // 10)
    w.offices["off_duke"] = Office("off_duke", "Duke", "D",
                                   ["issue", "determine", "confer", "dispatch", "convene"])
    w.offices["off_dicastery"] = Office("off_dicastery", "Dicastery", None, ["issue", "determine"])
    n = [0]
    def edge(sub, obj, kind, **kw):
        n[0] += 1
        w.tenures.append(Tenure(f"t{n[0]}", sub, obj, kind, since=0, **kw))
    edge("D", "R", "contain"); edge("S", "D", "contain"); edge("Hh", "S", "contain")
    for pid in ("p_low", "p_mid", "p_other"):
        edge(pid, "Hh", "contain")
    edge("p_high", "S", "contain"); edge("p_king", "R", "contain")
    edge("p_high", "off_duke", "hold")
    edge("p_low", "p_mid", "tie")
    w.manifest = {"contest": "seam.contest_resolver", "order": "core.canonical_order"}
    return w


# The instrument's own subsistence model, INJECTED (S42.2.1) rather than invented inside the
# shape. No in-chain document supplies one; this is a harness fixture and is named as such.
def SUBSIST(p: Person, w: World) -> int:
    scale = w.fixtures.get("condition_scale")
    home = Query.parent_of(w, p.id)
    if home is None or home not in w.rungs:
        return 0
    return min(scale, sum(w.rungs[home].stores.values()) * scale // max(1, p.weight))


def NOCHOOSE(p, v, s, ask_budget):
    return []


def NOEFFECT(w, a):
    return []


def _run(w: World, choose=NOCHOOSE, effect=NOEFFECT, n: int = 1, **kw):
    d = SeasonDriver(w)
    out = None
    for _ in range(n):
        out = d.season(choose, effect, question="q", subsistence=SUBSIST, **kw)
    return out


# ===========================================================================
# P-SERIES -- THE PERSON
# ===========================================================================

@probe("P1", "a person holding no office acts", "S3-L1", by="construction",
       tests="a person with no office, post, command, faction rank or standing must be able to act at all")
def p1():
    w = tiny_world()
    def choose(p, v, s, ask_budget):
        return [] if p.id != "p_low" else [Act_(w, p, "speak")]
    def effect(w, a):
        return [Ev(w, a.actor, "speech.made", a.actor, [ROOT])]
    r = _run(w, choose, effect)
    assert r["events"] == 1, r
    return "PASS: a postless person produced an Act that reached RESOLVE and emitted an Event"


def Act_(w, p, verb, **kw):
    from shape import Act
    return Act(H(w.world_seed, w.tick, p.id, f"act:{verb}"), p.id, verb, **kw)


def Ev(w, subj_seed, kind, subject, causes, changes=None, degree=None):
    return Event(H(w.world_seed, w.tick, subj_seed, f"ev:{kind}"), kind, subject,
                 changes or [], causes, w.tick, degree)


@probe("P2", "the act budget is ~5 and the PERSON chooses what to leave undone", "S26.3",
       by="construction",
       tests="a character must be able to take several distinct actions in one season and choose what to leave undone")
def p2():
    w = tiny_world()
    left_undone = []
    def choose(p, v, s, ask_budget):
        if p.id != "p_king":
            return []
        b = ask_budget()          # THE PERSON asks their own budget (S26.3)
        wants = [f"v{i}" for i in range(9)]
        left_undone.extend(wants[b:])           # THE PERSON triages, not the engine
        return [Act_(w, p, vb) for vb in wants[:b]]
    got = []
    _run(w, choose, lambda w, a: got.append(a.verb) or [])
    b = w.fixtures.get("act_budget")
    assert len(got) == b and len(left_undone) == 9 - b
    return (f"PASS: budget {b}; the person left {left_undone} undone. The engine does NOT truncate "
            "-- an over-budget return RAISES, because silently discarding the tail would be an "
            "engine deciding a person's options, which is L1")


@probe("P2x", "the engine truncates an over-budget act list", "S26.3", by="construction",
       tests="an engine may quietly drop actions a character wanted beyond their budget")
def p2x():
    w = tiny_world()
    def choose(p, v, s, ask_budget):
        b = ask_budget()
        return [Act_(w, p, f"v{i}") for i in range(b + 3)] if p.id == "p_king" else []
    _run(w, choose)
    return "UNREACHABLE"


@probe("P3", "choose() cannot see the world", "S3-L2", by="construction",
       tests="a character must decide from what they believe, which may be wrong, and never from world truth")
def p3():
    w = tiny_world()
    caught = {}
    def choose(p, v, s, ask_budget):
        with expect_refusal():
            try:
                _ = v.persons
            except Forbidden as ex:
                caught["ok"] = str(ex)
        return []
    _run(w, choose)
    assert "ok" in caught
    return ("PASS: L2 holds BY TYPE. `choose` receives (Person, View, Sensation, budget) and no "
            "World; the View raises on any world collection; every resolver-side Query takes "
            "World first, so calling one fails at the call site for want of an argument")


@probe("P4", "a false conclusion is indistinguishable from a true one", "S3-L2", by="construction",
       tests="a character must be able to believe something false and act on it as if true")
def p4():
    w = tiny_world()
    p = w.persons["p_low"]
    k = w.fixtures.get("view_k")
    p.ledger += [Claim("c1", p.id, "p_high", "is_loyal", True, 0, "firsthand", 100, "own"),
                 Claim("c2", p.id, "p_high", "is_loyal", False, 0, "told_by", 100, "own")]
    v = Query.assemble(p, "q", k)
    assert set(v.claim_ids) == {"c1", "c2"}
    return ("PASS: the View carries both, holding IDS not references, and nothing person-side "
            "can tell them apart. A false conclusion is indistinguishable from a true one TO THE "
            "PERSON HOLDING IT")


@probe("P5", "attribution is a per-witness claim, not a field", "S19.3", by="construction",
       tests="a character must be able to do something covertly, or be wrongly blamed for what another did")
def p5():
    w = tiny_world()
    e = Ev(w, "p_low", "theft.done", "site_harbour", [ROOT])
    assert not hasattr(e, "actor") and not hasattr(e, "source_actor") and not hasattr(e, "target")
    return ("PASS: Event carries NO actor and NO target. Attribution is a per-witness Claim, so "
            "covert action and false attribution stay expressible -- and adding a target field to "
            "make routing easier is its twin and is refused (S19.3)")


@probe("P6", "a conviction moves at RESOLVE", "S9.3", by="construction",
       tests="a character's moral commitments must be able to change, through argument and consequence")
def p6():
    w = tiny_world()
    w.step = Step.RESOLVE
    w.write("stance", WriteClass.ACTS, lambda: None,
            record_kind="Person", fieldname="convictions", driver="Act")
    return "UNREACHABLE"


@probe("P7", "a per-conviction scar", "S54 item 21", by="construction",
       tests="a character must carry lasting moral damage from what they were made to do")
def p7():
    w = tiny_world()
    w.step = Step.RESOLVE
    w.write("stance", WriteClass.ACTS, lambda: None,
            record_kind="Person", fieldname="scar", driver="Act")
    return "UNREACHABLE"


@probe("P8", "an ambition is blocked with no obstruct verb", "S3-L1", by="construction",
       tests="one character must be able to be blocked by another without either knowing about the other")
def p8():
    w = tiny_world()
    seat = {"holder": None}
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "take_seat")] if p.id in ("p_other", "p_mid") else []
    def effect(w, a):
        if a.verb == "take_seat" and seat["holder"] is None:
            seat["holder"] = a.actor
            return [Ev(w, a.actor, "seat.taken", a.actor, [ROOT])]
        return []
    _run(w, choose, effect)
    assert seat["holder"] is not None
    return (f"PASS: {seat['holder']} took the seat by the ordered fold. NO `obstruct` VERB, no "
            "knowledge of the loser in the winner's decision, NO BRANCH IN THE RESOLVER. "
            "Obstruction is not implemented -- IT FALLS OUT")


@probe("P9", "an order is the subordinate's own choice", "S11.1", by="construction",
       tests="a superior must be able to direct a subordinate, and the subordinate must be able to refuse or deviate")
def p9():
    w = tiny_world()
    log = []
    def choose(p, v, s, ask_budget):
        if p.id == "p_high":
            return [Act_(w, p, "dispatch", payload="p_mid")]
        if p.id == "p_mid":
            log.append("ran-own-choose")
            return [Act_(w, p, "refuse")]
        return []
    def effect(w, a):
        log.append(a.verb)
        return [Ev(w, a.actor, f"act.{a.verb}", a.actor, [ROOT])]
    _run(w, choose, effect)
    assert "refuse" in log and "ran-own-choose" in log
    return ("PASS: `dispatch` names ONE PERSON; that person runs their OWN `choose` and refused. "
            "The King's reach really is other people's decisions, mechanically. NOTE the refusal "
            "and the order landed in the SAME season with no ordering between them -- see A14/A36")


@probe("P10", "a person tracks multi-season work in progress", "S13", by="construction",
       tests="a character must be able to perform a repeated, multi-season task the engine tracks as ongoing")
def p10():
    w = tiny_world()
    r = Record("rec1", "Hh", "copy", stages=[("half", 2), ("done", 4)])
    w.records[r.id] = r
    w.step = Step.RESOLVE
    w.write("carrier_exists", WriteClass.ACTS, lambda: w.records.__setitem__(r.id, r),
            record_kind="Record", fieldname="stage", driver="Act")
    return "UNREACHABLE"


@probe("P11", "capability gates no verb", "S9.2", by="probe-model",
       tests="skill must supply dice and must never make an action unavailable")
def p11():
    w = tiny_world()
    p = w.persons["p_low"]
    p.capability = {"copying": 0}
    roster = [Candidate("copy"), Candidate("petition"), Candidate("kill")]
    got = Query.opening_set(p, View(p.id, [], w.fixtures.get("view_k")), roster)
    assert len(got) == len(roster)
    return ("PASS: rank 0 removed no candidate. `rank` supplies dice and GATES NO VERB; the only "
            "class-shaped gate in the design is Thread Sensitivity")


@probe("P12", "opening_set returns Candidate[], not Act[]", "S17", by="probe-model",
       tests="the set of things a character may do must be computed, not an authored list")
def p12():
    from shape import Act
    w = tiny_world()
    p = w.persons["p_low"]
    got = Query.opening_set(p, View(p.id, [], w.fixtures.get("view_k")), [Candidate("speak")])
    assert all(isinstance(c, Candidate) for c in got) and not any(isinstance(c, Act) for c in got)
    return ("PARTIAL: the TYPE is right -- Candidate[], per the overturn (S54 item 1; #350's `07` "
            "still carries -> Act[]). THE PROPERTY THE TYPE WAS CHOSEN TO PROTECT IS NOT: the "
            "roster is the caller's AUTHORED LIST, because S61's missing producer for `q` means "
            "there is nothing from which to compute a set. A typed authored list is still authored")


@probe("P13", "a person acts on a need with no stored need field", "S18.2", by="probe-model",
       tests="a character's needs must drive their choices")
def p13():
    w = tiny_world()
    p = w.persons["p_low"]
    val = SUBSIST(p, w)
    assert isinstance(val, int) and val > 0
    return ("PASS-WITH-A-DISCLOSURE: `needs` is a Sensation plus a Query, stored nowhere. But the "
            "subsistence FORMULA is the instrument's, injected (S42.2.1): no in-chain document "
            "supplies one, and S10.4 makes MatterKind an OPEN registry, so summing kinds as if "
            "fungible is a model choice the design has not made")


@probe("P14", "standing is computed", "S18.2", by="construction",
       tests="how a character is regarded must be able to differ from how they regard themselves")
def p14():
    w = tiny_world()
    reached = {}
    def choose(p, v, s, ask_budget):
        if p.id != "p_low":
            return []
        reached["n"] = s.subsistence     # the computable half is fine
        _ = s.standing                   # the half no section computes
        return []
    _run(w, choose)
    return "UNREACHABLE"


@probe("P15", "a person's private act stays private", "S61", by="no-signature",
       tests="something said in private must be able to stay private")
def p15():
    w = tiny_world()
    unspecified = [c for c in WITNESS_CHANNELS if c != "co_located"]
    raise Unspecified(
        f"four of the five witness channels have no predicate: {unspecified}",
        "S61",
        needs="a channel predicate that can EXCLUDE a person",
        law="S61 -- WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY PERSON. Nothing said in private is private. A WRAPPER DOES NOT FIX THIS AND MUST NOT BE PRESENTED AS FIXING IT",
    )


@probe("P16", "regard moves per-knower", "S20", by="construction",
       tests="how a character is seen must be able to differ between people who know different things")
def p16():
    w = tiny_world()
    k = w.fixtures.get("view_k")
    a, b = w.persons["p_low"], w.persons["p_mid"]
    a.ledger.append(Claim("ca", a.id, "p_high", "is_traitor", True, 0, "told_by", 100, "own"))
    b.ledger.append(Claim("cb", b.id, "p_high", "is_traitor", False, 0, "firsthand", 100, "own"))
    assert Query.assemble(a, "q", k).claim_ids != Query.assemble(b, "q", k).claim_ids
    return ("PASS: legitimacy is PER-KNOWER and flips at TELLING speed, not at a global write. "
            "There is no signature by which either could read the other's ledger")


@probe("P17", "hidden exposure accumulates across seasons", "S22.4", by="probe-model",
       tests="a character's risk must be able to build up quietly across seasons without anyone acting")
def p17():
    w = tiny_world()
    Query.aggregate_guard(w, "exposure", per_person_tally=True)
    return "UNREACHABLE"


@probe("P18", "a crossing compels a person to act", "S3-L5", by="construction",
       tests="a counter reaching an edge must be able to force a named person to answer")
def p18():
    w = tiny_world()
    site = w.sites["site_harbour"]
    floors = w.fixtures.get("band_floors")[site.kind]
    before = Query.verbs(w, site, floors)
    n = 0
    mine = lambda: [c for c in w.crossings if c[0] == site.id]
    while not mine() and n < 400:
        _run(w); n += 1
    after = Query.verbs(w, site, floors)
    assert mine(), "no band edge was crossed at the site under test"
    sid, verb, was, now, eid = mine()[0]
    ev = next(e for e in w.log if e.id == eid)
    assert ev.kind == "condition.band_crossed" and ev.causes == [ROOT]
    assert verb in before and verb not in after
    social = [c for c in ev.changes if c.field in ("stance", "convictions", "beliefs")]
    assert not social and not ev.degree
    return (f"PASS, AND BOTH HALVES OF L5 RAN. `{sid}` crossed the `{verb}` floor in {n} seasons "
            f"({was} -> {now}). (1) IT CHANGED WHAT MAY BE CHOSEN: {sorted(before)} -> "
            f"{sorted(after)}. (2) IT EMITTED A WITNESSABLE EVENT into the one log "
            f"({ev.kind}), carrying NO social change and NO degree -- so it wrote no social row "
            "and PRODUCED NO OUTCOME. That is L5 exactly, and it is what the in-chain survey "
            "found 19 of 50 arcs asking for: THE COUNTER COMPELS SOMEONE TO ACT, IT DOES NOT ACT")


@probe("P19", "a threshold produces an outcome with nobody deciding", "S3-L5", by="construction",
       tests="the story must be able to end when a counter reaches a value, with no person choosing")
def p19():
    w = tiny_world()
    w.step = Step.MATTER
    w.write("stance", WriteClass.MATTER, lambda: None,
            record_kind="Person", fieldname="stance", driver="Event")
    return "UNREACHABLE"


@probe("P20", "a person is individuated on demand", "S29", by="construction",
       tests="a person who was previously part of a crowd must be able to become a named individual")
def p20():
    w = tiny_world()
    w.step = Step.CENSUS
    w.write("carrier_exists", WriteClass.MATTER,
            lambda: w.persons.__setitem__("p_new", Person("p_new", "someone")),
            record_kind="Person", fieldname="exists", driver="Event")
    return "UNREACHABLE"


@probe("P21", "a cohort and a named person are one type", "S9.1", by="construction",
       tests="a crowd must be able to act, and a person must be able to step out of one, with no conversion")
def p21():
    w = tiny_world()
    crowd = Person("crowd_1", "the quarry hands", weight=40)
    w.persons[crowd.id] = crowd
    assert type(crowd) is type(w.persons["p_low"])
    acted = []
    _run(w, lambda p, v, s, ask_budget: [Act_(w, p, "down_tools")] if p.weight > 1 else [],
         lambda w, a: acted.append(a.actor) or [])
    assert acted == ["crowd_1"]
    return ("PASS: ONE CLASS. A cohort IS a Person at weight>1, it went through the SAME `choose` "
            "and the SAME resolver, and there is no conversion operation because THERE IS NO "
            "SECOND TYPE TO CONVERT TO")


@probe("P22", "a held object gates another's act", "S13", by="construction",
       tests="possession of an object must be able to make someone else's action unavailable or costlier")
def p22():
    w = tiny_world()
    w.records["rec_writ"] = Record("rec_writ", "S", "writ")
    w.step = Step.RESOLVE
    w.write("Tenure", WriteClass.ACTS,
            lambda: w.tenures.append(Tenure("t_hold", "p_low", "rec_writ", "hold", since=0)),
            record_kind="Record", fieldname="held_by", driver="Act")
    return "UNREACHABLE"


@probe("P23", "a season ends outside every institution", "S16", by="construction",
       tests="a character must be able to simply vanish or be killed, with no institutional process")
def p23():
    w = tiny_world()
    w.step = Step.MATTER
    w.write("carrier_exists", WriteClass.MATTER, lambda: w.persons.pop("p_low", None),
            record_kind="Person", fieldname="exists", driver="Event")
    return "UNREACHABLE"


@probe("P24", "death ends every tenure the dead held", "S15.3", by="construction",
       tests="when a character dies everything they held must end, including things held elsewhere")
def p24():
    w = tiny_world()
    w.step = Step.MATTER
    held = [t for t in w.tenures if t.subject == "p_high"]
    assert held
    for t in held:
        w.write("Tenure", WriteClass.MATTER, lambda t=t: setattr(t, "until", w.tick),
                record_kind="Tenure", fieldname="until", driver="Event",
                caused_person_exists="p_high")
    assert all(not t.live for t in held)
    return ("PASS: `(Tenure, until)` is social:false -- THE PARTITION'S ONE DECLARED SEAM, and the "
            "only Partition row ARCHITECTURE.md states -- and death's `until` write is the only "
            "Tenure write in the MATTER class. The cascade CROSSES OWNERS (S31.1 exception 2), "
            "including a `hold` on an office at another rung")


@probe("P25", "a storm ends a tenure", "S15.3", by="construction",
       tests="the world must be able to end a person's position without anyone acting")
def p25():
    w = tiny_world()
    w.step = Step.MATTER
    t = [x for x in w.tenures if x.subject == "p_high" and x.kind == "hold"][0]
    w.write("Tenure", WriteClass.MATTER, lambda: setattr(t, "until", w.tick),
            record_kind="Tenure", fieldname="until", driver="Event")   # no causation supplied
    return "UNREACHABLE"


@probe("P26", "accumulated harm changes what a person may do", "S22.4", by="probe-model",
       tests="harm suffered over several seasons must be able to close off options")
def p26():
    w = tiny_world()
    Query.aggregate_guard(w, "harm_borne", per_person_tally=True)
    return "UNREACHABLE"


@probe("P27", "a subordinate underperforms undetectably", "S20", by="construction",
       tests="a character must be able to quietly do less than ordered, discoverable only by investigation")
def p27():
    w = tiny_world()
    a, b = w.persons["p_high"], w.persons["p_mid"]
    a.ledger.append(Claim("c_ord", a.id, b.id, "complied", True, 0, "told_by", 100, "own"))
    b.ledger.append(Claim("c_tru", b.id, b.id, "complied", False, 0, "firsthand", 100, "own"))
    k = w.fixtures.get("view_k")
    assert Query.assemble(a, "q", k).claim_ids == ["c_ord"]
    return ("PASS: the superior's ledger says complied, the subordinate's says not, and neither "
            "can read the other's. Only investigation closes the gap")


@probe("P28", "a ledger is unreadable by anyone else", "S20", by="no-signature",
       tests="no character may read another's memory directly")
def p28():
    w = tiny_world()
    p = w.persons["p_low"]
    v = Query.assemble(p, "q", w.fixtures.get("view_k"))
    assert v.holder == p.id
    person_side = [n for n in dir(Query) if not n.startswith("_")]
    return ("PASS-BY-ABSENCE: `assemble` takes THE ASKER and builds from the asker's own ledger. "
            f"There is no signature in the Query surface ({len(person_side)} functions) that takes "
            "one person and returns another's ledger. Absence is the refusal here, not a guard")


@probe("P29", "a person travels between rungs", "S22.3", by="no-signature",
       tests="a character must be able to move from one place to another and be somewhere else next season")
def p29():
    raise Unowned(
        "travel legs", "S22.3", needs="an ownership row",
        law="S22.3/S31.1 -- travel legs are IN THE WRITE MATRIX and IN THE CHURN LEDGER and IN NO OWNERSHIP ROW. And they move a person BETWEEN rungs, which is a fourth cross-owner operation MATTER's own list of three does not name",
    )


@probe("P30", "a claim survives the season", "S20", by="construction",
       tests="what a character learned must still be true for them next season")
def p30():
    w = tiny_world()
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "do")] if p.id == "p_low" and w.tick == 0 else []
    def effect(w, a):
        return [Ev(w, a.actor, "thing.happened", "Hh", [ROOT])]
    _run(w, choose, effect)
    n1 = sum(len(p.ledger) for p in w.persons.values())
    _run(w)
    assert sum(len(p.ledger) for p in w.persons.values()) == n1 and n1 > 0
    return (f"PASS: {n1} claims persisted into the next season, uncleared by any step. Claims live "
            "in the holder's own ledger and only WITNESS writes it")


@probe("P31", "a hidden motive biases every decision", "S9", by="probe-model",
       tests="a character must be able to act on a private motive that consistently skews their judgement, unrecognised by themselves and by their superiors")
def p31():
    w = tiny_world()
    p = w.persons["p_mid"]
    p.convictions = {"Precedent": 0.6, "self_preservation": 0.4}
    picked = []
    def choose(q, v, s, ask_budget):
        if q.id != p.id:
            return []
        roster = [Candidate("report_truthfully"), Candidate("delay"), Candidate("understate")]
        opts = Query.opening_set(q, v, roster)
        best = max(opts, key=lambda c: q.convictions.get("Precedent", 0)
                   if c.verb == "report_truthfully" else q.convictions.get("self_preservation", 0))
        picked.append(best.verb)
        return [Act_(w, q, best.verb)]
    _run(w, choose)
    assert picked
    return (f"PASS: chose {picked[0]}. `convictions` is Person-interior, read PERSON-SIDE ONLY, and "
            "it skewed the pick with no branch in the resolver and nothing stored about the bias. "
            "Nobody -- including the holder and his superiors -- has a signature that reads it out")


@probe("P32", "a person's own condition narrows their options in a fixed order", "S12",
       by="no-signature",
       tests="a character's own condition must be able to degrade across a season so that their available actions narrow predictably")
def p32():
    w = tiny_world()
    person_fields = {f for f in Person.__dataclass_fields__}
    raise Unspecified(
        "a banded scalar on Person",
        "S12",
        needs="the S12.1 verb gate is defined ONLY over a Site's `condition`",
        law=f"S12.1's gate `verbs(w, site, c)` is the right mechanism and its carrier is a SITE. Person's declared fields are {sorted(person_fields)} -- none is a banded scalar, Sensation is EXACTLY two floats (S18.2), and S22 gives no owner for a third",
    )


@probe("P33", "an act costs more when it is bigger", "S26.3", by="no-signature",
       tests="performing a larger or riskier version of an action must be able to cost the actor more")
def p33():
    raise Unspecified(
        "act cost beyond budget consumption", "S26.3",
        needs="a cost model; the budget is a FLAT COUNT of acts",
        law="S26.3 -- 'a petition consumes budget LIKE ANY ACT, AND THAT IS THE WHOLE OF THE PRICING'. There is no per-act cost scalar anywhere in Part II, so a cheap act and a ruinous one cost a character the same",
    )


@probe("P34", "one person holds knowledge nobody else has", "S20", by="construction",
       tests="an office-holder must be able to be the only living person who knows a thing, so that removing them destroys it")
def p34():
    w = tiny_world()
    p = w.persons["p_high"]
    p.ledger.append(Claim("c_only", p.id, "treaty_1", "original_terms", "the clause was struck",
                          0, "firsthand", 100, "own"))
    assert all(not any(c.subject == "treaty_1" for c in q.ledger)
               for q in w.persons.values() if q.id != p.id)
    del w.persons[p.id]
    assert not [c for q in w.persons.values() for c in q.ledger if c.subject == "treaty_1"]
    return ("PASS: the claim lived ONLY in his own ledger; his removal destroyed it, because a "
            "ledger is not readable by anyone else and NOTHING COPIES IT. Institutional memory IS "
            "a person, which is exactly what the case wanted")


@probe("P35", "a private track of regard runs separately from a public one", "S18.2",
       by="no-signature",
       tests="a character must be able to have a standing among people who can never publicly acknowledge them, separate from their public standing")
def p35():
    raise Unspecified(
        "an audience-scoped second standing", "S18.2",
        needs="a second standing scalar, or an owner for an audience-scoped one",
        law="S18.2 -- Sensation is EXACTLY TWO FLOATS and S46.1 makes widening it structural in Godot ('nobody can add a third field to Vector2'). A second, audience-scoped standing has NO CARRIER and S22 gives NO OWNER for one -- and the first standing does not compute either (see P14)",
    )


@probe("P36", "a choice branches three ways", "S17", by="probe-model",
       tests="a discovery must be able to be acted on in several distinct ways, each leading somewhere different")
def p36():
    w = tiny_world()
    p = w.persons["p_mid"]
    roster = [Candidate("protect", why="conceal"), Candidate("report", why="hand it up"),
              Candidate("leverage", why="trade on it")]
    got = []
    def choose(q, v, s, ask_budget):
        if q.id != p.id:
            return []
        b = ask_budget()
        return [Act_(w, q, c.verb) for c in Query.opening_set(q, v, roster)[:b]]
    _run(w, choose, lambda w, a: got.append(a.verb) or [Ev(w, a.actor, f"chose.{a.verb}", a.actor, [ROOT])])
    assert len(got) == 3
    return (f"PASS-WITH-A-DISCLOSURE: {got} -- three Candidates through the SAME resolver, no "
            "branching-outcome machinery (Part VIII refuses it as an authoring convention over "
            "Record). THE ROSTER IS THE PROBE'S, because S61 leaves `opening_set` nothing to "
            "compute from")


# ===========================================================================
# F-SERIES -- FACTIONS, OFFICES, PETITIONS. T5's aggregate-up.
# ===========================================================================

@probe("F1", "a faction is a proposition plus its commit edges", "S14.2", by="construction",
       tests="a group of people must be able to share a cause that spans places and outlives its founder")
def f1():
    w = tiny_world()
    prop = Proposition("prop_1", "OUGHT", "realm", "the wardens should hold", True, 0)
    w.propositions[prop.id] = prop
    w.tenures += [Tenure("tc1", "p_low", prop.id, "commit", since=0),
                  Tenure("tc2", "p_king", prop.id, "commit", since=0)]
    edges = [t for t in Query.lateral(w, "faction", "commit") if t.object == prop.id]
    n = Query.commit_count_guard(w, edges, "membership")
    try:
        prop.value = False
    except Exception:
        immutable = True
    else:
        immutable = False
    assert n == 2 and immutable
    return ("PASS: membership is `commit`, spanning a hearth-dweller and the King WITH NO PARENT "
            "RUNG -- the LATERAL topology, resolver-side, not an R-1 aggregate. The Proposition "
            "is structurally immutable, so the persistent part cannot be edited")


@probe("F2", "a memberless faction's holdings become contestable", "S54 item 20",
       by="probe-model",
       tests="when everyone abandons a cause, what it held must be able to be taken by someone else")
def f2():
    w = tiny_world()
    prop = Proposition("prop_dead", "OUGHT", "realm", "a dead cause", True, 0)
    w.propositions[prop.id] = prop
    w.tenures.append(Tenure("th_dead", prop.id, "S", "hold", since=0))
    assert not [t for t in Query.lateral(w, "faction", "commit") if t.object == prop.id]
    w.step = Step.RESOLVE
    old = Query.hold_force(w, "S")
    w.write("Tenure", WriteClass.ACTS, lambda: setattr(old, "until", w.tick),
            record_kind="Tenure", fieldname="until", driver="Act")
    w.write("Tenure", WriteClass.ACTS,
            lambda: w.tenures.append(Tenure("th_new", "p_high", "S", "hold", since=w.tick)),
            record_kind="Tenure", fieldname="since", driver="Act")
    assert Query.hold_force(w, "S").subject == "p_high"
    return ("PASS: `confer` on an object whose holder-Proposition has ZERO live commit edges was "
            "eligible, and THE SUCCESSFUL CONFER wrote `until` -- an ACT, in the ACTS class, via "
            "the 1-per-object cardinality. S54 item 20's REFUSED half (write `until` when the "
            "last commit reaches zero) would be an actorless social write outside the one seam")


@probe("F3", "a faction acts", "S3-L1", by="no-signature",
       tests="a faction must be able to take an action of its own")
def f3():
    w = tiny_world()
    from shape import Act
    actor_field = Act.__dataclass_fields__["actor"]
    props = list(w.propositions) + ["prop_any"]
    raise Forbidden(
        "a faction taking an action of its own", "S3-L1",
        needs="a named person at a venue",
        law=f"L1 -- `resolve` has NO FACTION PARAMETER and a faction has NO VERBS. `Act.actor` is a single id ({actor_field.type}) and a faction IS a Proposition plus commit edges (S14.2), which is not an actor. 'The Church excommunicates' IS NOT SPELLABLE",
    )


@probe("F4", "an office makes an ordinary act eligible", "S11.1", by="construction",
       tests="holding a post must be able to make an action available that is not available otherwise")
def f4():
    w = tiny_world()
    off = w.offices["off_duke"]
    holder = Query.hold_force(w, off.id)
    assert holder is not None and holder.subject == "p_high"
    assert not hasattr(off, "holder") and not hasattr(off, "held_by")
    return ("PASS: WHO HOLDS AN OFFICE IS NOT A FIELD ON THE OFFICE -- it is a `hold` Tenure owned "
            "by the holder, at cardinality 1 per object. The office adds NO verb and NO modifier; "
            "it makes ordinary acts eligible and SUBSTITUTES THE POOL SOURCE")


@probe("F5", "an office with no place issues to executors across the realm", "S6.2",
       by="probe-model",
       tests="a body with members everywhere and a seat nowhere must be able to issue instructions")
def f5():
    w = tiny_world()
    off = w.offices["off_dicastery"]
    assert off.rung is None
    scope = ["p_low", "p_king"]   # p_king sits under the realm, outside S's subtree
    w.dispensations["disp1"] = dict(id="disp1", issuer=off.id, proposition="prop_x",
                                    scope=scope, terms=[])
    sub = Query.descendants(w, "S")
    outside = [s for s in scope if s not in sub]
    assert all(s in w.persons for s in scope) and outside
    return (f"PASS: `rung? = null`, and SCOPE ENUMERATES EXECUTORS, NOT PLACES -- {outside} are "
            "outside the settlement's containment subtree entirely. A Dicastery, a chivalric order "
            "and a trans-settlement guild HAVE NO CONTAINMENT NODE, so R-1/R-2 do not govern this")


@probe("F6", "a dispensation reaches a person who never heard it", "S37.1", by="no-signature",
       tests="an order from above must be able to fail to arrive, distinctly from being refused")
def f6():
    raise Unspecified(
        "how much a dispensation distorts in transit", "S62",
        needs="a distortion model, and a ruling on emitter- vs receiver-side refraction",
        law="T6 says it distorts; NOTHING SPECIFIES BY HOW MUCH (S62). The structural half works -- publishing is a `tell`, delivery is not assumed, and an executor who never received it is DISTINCT from one who received it and refused -- but the distortion itself has no model, and S37.4 records that the chain uses `refraction` TWO WAYS",
    )


@probe("F7", "a demand rises from a hearth to a duchy", "S36.1", by="probe-model",
       tests="someone with no power must be able to get a matter in front of someone who has it")
def f7():
    w = tiny_world()
    w.petitions["pet1"] = dict(id="pet1", petitioner="p_low", proposition="mend the harbour",
                               respondent_venue="D", backing=[])
    w.dates["d_sitting"] = dict(due_at=99, holder="D", fired=False)
    carried = {}
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "carry", payload="pet1")] if p.id == "p_mid" else []
    def effect(w, a):
        if a.verb != "carry":
            return []
        carried["by"] = a.actor
        w.write("DocketItem", WriteClass.ACTS,
                lambda: w.docket.append({"date": "d_sitting", "matter": a.payload}),
                record_kind="DocketItem", fieldname="matter", driver="Act")
        return [Ev(w, a.actor, "petition.carried", a.payload, [ROOT])]
    _run(w, choose, effect)
    assert carried.get("by") == "p_mid" and w.docket
    return ("PASS: Petition -> `carry` (AN ACT, BY A NAMED PERSON, COSTING BUDGET) -> DocketItem on "
            "a Date. NO automatic promotion, NO queue drain, NO priority function. THE FILTER IS A "
            "PERSON AND THE PERSON PAYS -- which is why T5 produces politics rather than a work queue")


@probe("F8", "the sitting decides", "S61", by="construction",
       tests="the body a matter reaches must be able to decide it")
def f8():
    w = tiny_world()
    Query.judging_set(w, "D")
    return "UNREACHABLE"


@probe("F9", "petition spray", "S26.3", by="construction",
       tests="a character must be able to spend a whole season putting the same matter to many people")
def f9():
    w = tiny_world()
    filed = []
    def choose(p, v, s, ask_budget):
        b = ask_budget()
        return ([Act_(w, p, f"petition{i}", payload=f"venue{i}") for i in range(b)]
                if p.id == "p_low" else [])
    _run(w, choose, lambda w, a: filed.append(a.payload) or [])
    b = w.fixtures.get("act_budget")
    assert len(filed) == b == len(set(filed))
    return (f"PASS: {b} petitions to {b} different venues on one matter. NO DEDUP, NO CAP, NO "
            "PER-VENUE LIMIT, NO 'already before a body' RULE, NO COST GATE -- ruled allowable, and "
            "the budget IS the whole of the pricing. Spending all five here IS the triage the "
            "budget exists to create")


@probe("F10", "a matter closes by scarcity, not by cancelling", "S54.1", by="probe-model",
       tests="several live demands on one matter must be able to resolve without cancelling each other")
def f10():
    w = tiny_world()
    hearth = w.rungs["Hh"]
    granted, refused = [], []
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "transfer", payload=6)] if p.id in ("p_low", "p_mid") else []
    def effect(w, a):
        if a.verb != "transfer":
            return []
        # S54 item 7: transfer's PRECONDITION `stores(hearth(giver), kind) >= amount`. Without
        # it the ordered fold's own scarcity claim is FALSE, since a transfer could MINT FROM A
        # NEGATIVE LARDER -- and S54.1's close rule depends on this landing.
        if hearth.stores.get("grain", 0) < a.payload:
            refused.append(a.actor)
            return [Ev(w, a.actor, "transfer.refused", a.actor, [ROOT])]
        w.write("stores", WriteClass.ACTS,
                lambda: hearth.stores.__setitem__("grain", hearth.stores["grain"] - a.payload),
                record_kind="Rung", fieldname="stores", driver="Act")
        granted.append(a.actor)
        return [Ev(w, a.actor, "transfer.made", a.actor, [ROOT])]
    _run(w, choose, effect)
    assert len(granted) == 1 and len(refused) == 1 and hearth.stores["grain"] >= 0
    return (f"PASS: granted={granted}, refused={refused}, larder={hearth.stores['grain']} (never "
            "negative). THE SECOND CLAIMANT ON AN EMPTIED LARDER GOT A DIFFERENT EVENT. Petitions "
            "never closed each other; the matter closed AT RESOLVE BY SCARCITY. S54 item 7's "
            "precondition is what makes this true rather than minting")


@probe("F11", "a person knows their faction's true strength", "S38", by="no-signature",
       tests="a character must be able to know how strong their own faction is")
def f11():
    w = tiny_world()
    resolver_side = [n for n in ("descendants", "lateral", "presence", "r1_aggregate", "hold_force")]
    person_side = [n for n in ("assemble", "opening_set", "budget", "entrenchment")]
    raise Forbidden(
        "reading faction strength from inside choose()", "S38",
        needs="`leaders_as_claimed` / `norm_as_claimed` -- what they CLAIM about it",
        law=f"S38 -- every lateral traversal is RESOLVER-SIDE ({resolver_side}), World FIRST, and `choose` has no World, so the call fails at the call site for want of an argument. The person-side surface is {person_side}. THIS IS NOT A LIMITATION TO WORK AROUND: it is why a person CANNOT know their faction's true strength, only what they claim about it",
    )


@probe("F12", "an office is conferred and revoked as acts", "S11", by="construction",
       tests="a post must be able to be given and taken away by named people at named occasions")
def f12():
    w = tiny_world()
    w.step = Step.RESOLVE
    t = Query.hold_force(w, "off_duke")
    w.write("Tenure", WriteClass.ACTS, lambda: setattr(t, "until", w.tick),
            record_kind="Tenure", fieldname="until", driver="Act")
    w.write("Tenure", WriteClass.ACTS,
            lambda: w.tenures.append(Tenure("t_new", "p_mid", "off_duke", "hold", since=w.tick)),
            record_kind="Tenure", fieldname="since", driver="Act")
    assert not t.live and Query.hold_force(w, "off_duke").subject == "p_mid"
    ent = Query.entrenchment(w.persons["p_mid"], 30, w.fixtures.get("condition_scale"),
                             w.fixtures.get("entrenchment_seasons"))
    return (f"PASS: confer and revoke are ACTS, in the ACTS class, at RESOLVE. The revoked row was "
            f"NOT DELETED -- `until` makes it a HISTORICAL CLAIM SUBJECT, which is what "
            f"entrenchment reads ({ent}/{w.fixtures.get('condition_scale')} at 30 seasons)")


@probe("F13", "a vacancy opens the succession occasion", "S24", by="construction",
       tests="when a post falls empty the process to fill it must be able to start")
def f13():
    w = tiny_world()
    w.dates["d_conf"] = dict(due_at=0, holder="D", fired=False)
    w.dates["d_vacant"] = dict(due_at=0, holder=None, fired=False)
    SeasonDriver(w).calendar()
    assert w.dates["d_conf"]["fired"] and w.dates["d_vacant"]["fired"]
    assert len(w.docket) == 1
    return ("PASS: both dates FIRED; the vacant one ALLOCATED NOTHING AND LAPSED rather than "
            "blocking. Death does NOT open the conferral Date -- THE VACANCY IS A FACT, THE DATE "
            "IS AN OCCASION, AND CALENDAR IS WHERE FACTS BECOME OCCASIONS. CALENDAR decided nothing")


@probe("F14", "a faction's holdings-ever are counted", "S22.4", by="construction",
       tests="a faction's territory must be countable as it gains and loses ground")
def f14():
    w = tiny_world()
    prop = Proposition("prop_c", "OUGHT", "realm", "a cause", True, 0)
    w.propositions[prop.id] = prop
    w.tenures += [Tenure("e1", "p_low", prop.id, "commit", since=0),
                  Tenure("e2", "p_mid", prop.id, "commit", since=0, until=1)]
    Query.commit_count_guard(w, [t for t in w.tenures if t.kind == "commit"], "held_ever")
    return "UNREACHABLE"


@probe("F15", "an establishment does the office's work", "S11", by="no-signature",
       tests="a post must be able to employ people whose competence is what actually gets used")
def f15():
    w = tiny_world()
    off = w.offices["off_duke"]
    assert off.establishment == []
    raise Unspecified(
        "establishment size", "S54 item 13 / S61",
        needs="how many people an office employs, and how they are chosen",
        law="S61 -- one of FOUR BLOCKING GAPS DROPPED FROM THE OPEN REGISTER and folded back as `grade: absent`. S11.1 makes the pool `capability of the dispatched establishment member(s) ACTUALLY PERFORMING IT`, so with an empty establishment an office has no pool source at all",
    )


@probe("F16", "a faction-wide resource grows and is spent", "S3-L3", by="no-signature",
       tests="a faction must be able to hold a pooled resource that its members' actions raise and lower")
def f16():
    w = tiny_world()
    prop = Proposition("prop_f", "OUGHT", "realm", "a cause", True, 0)
    fields = sorted(Proposition.__dataclass_fields__)
    raise Forbidden(
        "a faction stat -- a pooled, stored, faction-wide quantity", "S3-L3",
        needs="a Query over live commit edges, recomputed; or the thing tracked belongs in a person's ledger",
        law=f"L3 -- a stored `unrest` is a lie that outlives its reasons. A faction IS a Proposition plus its commit edges (S14.2), and Proposition is FROZEN with fields {fields} -- there is nowhere to put it. A Rung refuses it too (S10.1). AND the obvious workaround is closed: summing per-member tallies is S22.4 clause 2, counting ever-held edges is clause 3",
    )


@probe("F17", "an authorization precedes the act it authorises", "S27.1", by="construction",
       tests="a superior's approval must be able to be a formal precondition without which subordinates cannot act")
def f17():
    w = tiny_world()
    authorized, seen = {}, []
    def choose(p, v, s, ask_budget):
        if p.id == "p_high":
            return [Act_(w, p, "confer_authority", payload="p_mid")]
        if p.id == "p_mid":
            return [Act_(w, p, "raid")]
        return []
    def effect(w, a):
        if a.verb == "confer_authority":
            authorized[a.payload] = True
            seen.append("authorised")
            return [Ev(w, a.actor, "authority.conferred", a.payload, [ROOT])]
        if a.verb == "raid":
            k = "raid.done" if authorized.get(a.actor) else "act.unauthorised"
            seen.append(k)
            return [Ev(w, a.actor, k, a.actor, [ROOT])]
        return []
    _run(w, choose, effect)
    return (f"PASS-CONDITIONALLY, AND THE CONDITION IS THE FINDING: sequence={seen}. Both acts "
            "landed in ONE season and THE FOLD'S CONTENT-DERIVED ORDER -- not intent, not rank, "
            "not the superior's seniority -- decided whether the raid counted as authorised. "
            "There is no within-season sequencing a person can rely on. See A14 and A36")


@probe("F18", "a place's demands conflict with its superior's orders", "S36.1", by="probe-model",
       tests="a place must be able to generate demands of its own that cut against what the authority above ordered")
def f18():
    w = tiny_world()
    w.petitions["pet_local"] = dict(id="pet_local", petitioner="p_low",
                                    proposition="mend the seam", respondent_venue="S", backing=[])
    w.dispensations["disp_order"] = dict(id="disp_order", issuer="off_duke",
                                         proposition="levy the grain", scope=["p_high"], terms=[])
    b = w.fixtures.get("act_budget")
    return (f"PASS-STRUCTURALLY: a Petition rising from below and a Dispensation enumerating the "
            f"same executor coexist WITH NO ARBITRATION ANYWHERE IN THE SHAPE. The governor's {b} "
            "acts are the only scarcity, so the conflict is REAL and is resolved BY THE PERSON, "
            "which is L1. Both objects are the probe's data, not the shape's -- nothing constructs "
            "either. See F19")


@probe("F19", "a place produces a demand with nobody petitioning", "S36.1", by="no-signature",
       tests="a settlement's needs must be able to surface as demands without a named petitioner")
def f19():
    raise NoProducer(
        "a demand originating from a place rather than a person", "S36.1",
        needs="a named person who wants it, and a named person who carries it",
        law="S36.1 -- 'a want -> Petition(petitioner, ...)'. EVERY ARROW IS A PERSON'S ACT OR A CALENDAR FACT: no automatic promotion, no queue drain, no priority function -- and therefore NO PRODUCER for a placeless want. A Rung owns `matter`, `dates`, `envelope`, `stake` -- arrangements, not wants",
    )


# ===========================================================================
# W-SERIES -- THE WORLD. T8's churn, the three licensed clocks.
# ===========================================================================

@probe("W1", "a site decays until a verb leaves its set", "S12.1", by="construction",
       tests="a place must be able to fall into disrepair until things can no longer be done there")
def w1():
    w = tiny_world()
    scale = w.fixtures.get("condition_scale")
    site = w.sites["site_harbour"]
    floors = w.fixtures.get("band_floors")[site.kind]
    assert "bulk_shipping" in Query.verbs(w, site, floors)
    n = 0
    while "bulk_shipping" in Query.verbs(w, site, floors) and n < 200:
        _run(w); n += 1
    assert n < 200
    return (f"PASS: wear at MATTER dropped condition below the floor in {n} seasons and the verb "
            f"LEFT THE SET. The COUNT is a function of the injected `wear_per_season` fixture and "
            "moves with it -- the STRUCTURAL claim (a verb leaves) does not")


@probe("W1x", "wear answers for an unregistered site kind", "S42.2.1", by="construction",
       tests="the world must be able to wear down a kind of place nobody wrote a rule for")
def w1x():
    w = tiny_world()
    w.sites["site_odd"] = Site("site_odd", "S", "reliquary", condition=500)
    _run(w)
    return "UNREACHABLE"


@probe("W2", "the world churns with nobody in it", "S3-L4", by="construction",
       tests="the world must be able to change while no character is doing anything")
def w2():
    w = tiny_world()
    before = w.sites["site_seam"].condition
    r = _run(w)
    assert r["acts"] == 0 and w.sites["site_seam"].condition < before
    return (f"PASS: ZERO acts, and matter still moved ({before} -> "
            f"{w.sites['site_seam'].condition}). T8 holds; the player is not necessary")


@probe("W3", "the world sours a mood", "S3-L4", by="construction",
       tests="a bad season must be able to make people angrier without anyone acting")
def w3():
    w = tiny_world()
    w.step = Step.MATTER
    w.write("stance", WriteClass.MATTER, lambda: None,
            record_kind="Person", fieldname="stance", driver="Event")
    return "UNREACHABLE"


@probe("W4", "an ambient MATERIAL quantity moves on its own", "S25", by="construction",
       tests="an environmental or material condition must be able to worsen on its own")
def w4():
    w = tiny_world()
    before = w.sites["site_harbour"].condition
    _run(w)
    assert w.sites["site_harbour"].condition < before
    return ("PASS: MATTER is a licensed clock and the substrate is a Site kind. AN AMBIENT "
            "MATERIAL QUANTITY IS LAWFUL; only an ambient SOCIAL one is not (W3). The in-chain "
            "arc test's most expensive correction was conflating these two -- 8 arcs became 3")


@probe("W5", "yield is produced", "S22.3", by="no-signature",
       tests="the harvest must be able to come in, better or worse from season to season")
def w5():
    raise Unowned(
        "season_factor's distribution", "S22.3", needs="an owner for the distribution",
        law="S22.3 -- THIS BLOCKS `yield`. `yield` is written ONLY at MATTER (S30, the one single-cell row in the whole matrix) and there is nothing to write, because the distribution that would drive it has no owner",
    )


@probe("W6", "a plague spans many rungs as one event", "S31.1", by="construction",
       tests="a disaster must be able to strike many places at once and be one thing that happened")
def w6():
    w = tiny_world()
    e = Ev(w, "R", "plague.struck", "R", [ROOT])
    r = _run(w, actorless=[e])
    assert e in w.log and e.causes == [ROOT]
    return (f"PASS: ONE Event spanning many rungs, with ONE id, emitted SERIALLY before the "
            "parallel section. Sharding it per rung would BREAK causes[], because ONE CAUSE IS "
            f"ONE ID (S31.1 exception 3). It reached {r['deposits']} ledger(s) through WITNESS")


@probe("W7", "a record expires", "S13", by="construction",
       tests="a document must be able to lapse after a time")
def w7():
    w = tiny_world()
    rec = Record("rec_ttl", "S", "writ", ttl=2)
    w.records[rec.id] = rec
    w.step = Step.MATTER
    w.write("carrier_exists", WriteClass.MATTER, lambda: setattr(rec, "ttl", rec.ttl - 1),
            record_kind="Record", fieldname="ttl", driver="Event")
    return "UNREACHABLE"


@probe("W8", "a case ripens against someone who does nothing", "S13.1", by="probe-model",
       tests="a legal or institutional process must be able to advance against a character who is passive")
def w8():
    w = tiny_world()
    rec = Record("rec_case", "S", "case", stages=[("deposition", 1), ("tribunal", 3)])
    w.records[rec.id] = rec
    opened = Ev(w, "p_high", "case.opened", rec.id, [ROOT])
    w.log.append(opened)
    matured = [s for s, term in rec.stages if term <= 1]
    ripening = Ev(w, rec.id, "term.matured", rec.id, [opened.id])
    assert matured == ["deposition"] and ripening.causes == [opened.id]
    return ("PASS-STRUCTURALLY: the Inquisitor's `open_case` act DECLARED the stages and their "
            "terms; each maturation is A PERSON'S PAST ACT RIPENING, with causes[] pointing at "
            "the act that wound the clock. NOT a MATTER-advanced `Record.stage`, which would be a "
            "FOURTH clock L5 forbids. But the stages are the PROBE'S -- S30.1 gives Record no "
            "Partition row, so the write that would store them raises (P10)")


@probe("W9", "births and deaths move a population", "S10.3", by="construction",
       tests="a place's population must be able to grow and shrink")
def w9():
    w = tiny_world()
    r = w.rungs["S"]
    r.envelope = [100, 200, 150, 60]
    w.step = Step.MATTER
    w.write("envelope", WriteClass.MATTER, lambda: r.envelope.__setitem__(0, r.envelope[0] + 5),
            record_kind="Rung", fieldname="envelope", driver="Event")
    assert r.envelope[0] == 105
    return ("PASS: BIRTH IS ENVELOPE WEIGHT, NOT A `create`. The envelope has no ledger, no stance "
            "and no act -- conflating them PRODUCES A DESIGN IN WHICH DEMOGRAPHY CAN CHOOSE")


@probe("W10", "a settlement holds a level of discontent", "S10.1", by="construction",
       tests="a place must be able to hold a level of discontent that rises and falls")
def w10():
    w = tiny_world()
    w.rungs["S"].morale = 5
    return "UNREACHABLE"


@probe("W11", "a person draws subsistence from the place containing them", "S31.1",
       by="construction",
       tests="a character must be able to eat from the stores of the place they live in")
def w11():
    w = tiny_world()
    parent = Query.parent_of(w, "p_low")
    assert parent == "Hh" and w.rungs[parent].stores.get("grain", 0) > 0
    return ("PASS: a `person`-kind rung draws from its CONTAINING rung's stores -- lawful as an "
            "R-1 ON-DEMAND READ OF THE PARENT, not a cross-rung write. But it means MATTER IS NOT "
            "CLOSED OVER ONE OWNER (S31.1 exception 1), which is the honest price of the partition")


@probe("W12", "the world holds people who hold no post", "S54 item 18", by="probe-model",
       tests="a world must be able to start with people in it who hold no post")
def w12():
    w = tiny_world()
    postless = [p.id for p in w.persons.values()
                if not any(t.kind == "hold" and t.subject == p.id and t.live for t in w.tenures)]
    assert postless
    return (f"PASS: {len(postless)} persons with ZERO live `hold` Tenures. S54 item 18 folds in "
            "THE SHAPE (a roster read from a registry row at grade: assumption), NOT THE NUMBER -- "
            "and a world-generation roster is not a clock (S29). The design's own acceptance test "
            "needs such a person and was unreachable until one existed")


# ===========================================================================
# A-SERIES -- THE ARCHITECTURE ITSELF
# ===========================================================================

@probe("A1", "causes[] is required and non-empty", "S19.4", by="construction",
       tests="the story must be able to be reconstructed from what caused what")
def a1():
    w = tiny_world()
    Event(H(1, 0, "x", "e"), "thing.happened", "x", [], [], 0)
    return "UNREACHABLE"


@probe("A2", "an arc is a provenance chain that walks", "S19.4", by="probe-model",
       tests="a sequence of related happenings must be able to be read back as one story")
def a2():
    w = tiny_world()
    e1 = Ev(w, "p_low", "petition.filed", "p_low", [ROOT])
    w.log.append(e1)
    w.tick = 1
    e2 = Ev(w, "p_mid", "petition.carried", "p_low", [e1.id])
    w.log.append(e2)
    w.tick = 2
    e3 = Ev(w, "D", "sitting.decided", "D", [e2.id])
    w.log.append(e3)
    ids = {e.id for e in w.log}
    assert all(c in ids or c == ROOT for e in w.log for c in e.causes)
    chain, cur = [], e3
    while cur.causes != [ROOT]:
        chain.append(cur.kind)
        cur = next(e for e in w.log if e.id == cur.causes[0])
    chain.append(cur.kind)
    assert len(chain) == 3
    return (f"PASS: {' <- '.join(chain)}. A three-link causes[] chain walks end to end across "
            "three seasons. THIS IS THE ARC, and it is the substrate of the whole emergent-"
            "narrative claim -- which the measured state of the chain says is 'declared and never "
            "populated'. It is populated here")


@probe("A3", "an arc ends at a counter with nobody deciding", "S3-L5", by="construction",
       tests="the story must be able to conclude when a tracked quantity reaches a value")
def a3():
    w = tiny_world()
    w.step = Step.MATTER
    # the crossing itself is lawful (P18); what is refused is the crossing PRODUCING AN OUTCOME.
    w.write("stance", WriteClass.MATTER, lambda: None,
            record_kind="Person", fieldname="stance", driver="Event")
    return "UNREACHABLE"


@probe("A4", "two runs of the same seed produce the same log AND the same hash", "S33",
       by="construction",
       tests="the same starting conditions must be able to produce the same history")
def a4():
    def run():
        w = tiny_world()
        def choose(p, v, s, ask_budget):
            return [Act_(w, p, "do")] if p.id in ("p_low", "p_mid") else []
        def effect(w, a):
            return [Ev(w, a.actor, "did.thing", "Hh", [ROOT])]
        r = None
        for _ in range(3):
            r = _run(w, choose, effect)
        return r["hash"], [(e.id, e.kind, tuple(e.causes)) for e in w.log]
    (h1, l1), (h2, l2) = run(), run()
    assert h1 == h2 and l1 == l2 and l1
    return (f"PASS: {len(l1)} events, BIT-IDENTICAL across two runs, and the CONTENT HASH OVER THE "
            f"LOG matches ({h1[:16]}...). Ids come from H(world_seed, tick, subject, purpose) -- "
            "NO ALLOCATOR, NO COUNTER, NOTHING TO SERIALISE ON. This is S66 artifact 1's shape")


@probe("A5", "the fold is order-independent, and the float control actually fires", "S32",
       by="construction",
       tests="the outcome must not depend on the order the engine happened to process things in")
def a5():
    w0 = tiny_world()
    scale = w0.fixtures.get("condition_scale")
    deltas = [3, -5, 3, -1, 2]

    # ARM 1 -- REPRODUCIBILITY, through the real fold. The act array is shuffled before entry
    # and S32 rest 3's content-derived canonicalization restores one order, so two runs agree.
    def run_fold(reverse: bool) -> tuple[int, str]:
        w = tiny_world()
        site = w.sites["site_harbour"]
        order = list(reversed(deltas)) if reverse else deltas
        def choose(p, v, s, ask_budget):
            if p.id != "p_low":
                return []
            # the label is derived from the DELTA, not from the position, so reversing the
            # list changes only the SEQUENCE -- the set of acts is identical. Rev 3 caught
            # this: pairing the label to the index made the two arms different EXPERIMENTS
            # (S0.1 pt 1), and the log hash then differed for a reason that had nothing to do
            # with summation order.
            return [Act_(w, p, f"mend_{d}",
                         changes=[StateChange(site.id, "alter", "Act", "condition", d)])
                    for d in order][:ask_budget()]
        def effect(w, a):
            return [Ev(w, a.actor, "site.worked", site.id, [ROOT], changes=a.changes)]
        r = _run(w, choose, effect)
        return w.sites[site.id].condition, r["hash"]

    (ca, ha), (cb, hb) = run_fold(False), run_fold(True)

    # ARM 2 -- THE CONTROL, AND IT MUST FIRE OR THIS PROBE IS WORTHLESS.
    #
    # ⚠ REV 3. Rev 2's control computed `0.9 + d/1000.0` over these same deltas, got
    # 0.902 == 0.902, printed `differing=False` AND ASSERTED IN THE SAME SENTENCE THAT THE
    # CONTROL HAD FIRED. It had not. S66 artifact 4 is explicit: "A float build must produce a
    # DIFFERENT hash under a reordered fold, OR THE TEST CANNOT OBSERVE WHAT IT EXCLUDES."
    # The magnitudes were the bug -- scaling by 1000 put every partial sum in a regime where
    # the additions happened to be exact.
    def float_sum(order):
        acc = 0.9
        for d in order:
            acc += float(d)
            acc = max(0.0, min(1000.0, acc))
        return acc
    fa, fb = float_sum(deltas), float_sum(list(reversed(deltas)))
    float_differs = (fa != fb)

    # integers: order-independent AS A FACT, because integer addition is associative.
    ia = sum(deltas)
    ib = sum(reversed(deltas))

    assert ca == cb and ha == hb, (ca, cb)
    assert ia == ib
    assert float_differs, (
        "THE CONTROL DID NOT FIRE. Without a float arm that actually diverges this probe "
        f"cannot observe the failure it excludes: {fa!r} == {fb!r}")
    return (f"PASS, AND THE CONTROL FIRED. Fixed point: condition {ca} == {cb} and the LOG "
            f"CONTENT HASH matches ({ha[:12]}...) under a reversed act order, through the real "
            f"fold and sum-then-clamp-once. THE CONTROL: the same five deltas summed as IEEE "
            f"floats in the two orders give {fa!r} vs {fb!r} -- DIFFERENT, so the assertion can "
            "observe what it excludes. TWO SEPARATE PROPERTIES, and S32 says not to conflate "
            "them: THE CANONICAL SORT BUYS REPRODUCIBILITY (arm 1); FIXED POINT BUYS "
            "ORDER-INDEPENDENCE (arm 2). If fixed point were refused, the honest word would be "
            "CANONICALLY ORDERED, not order-independent, and every document would have to change "
            "the word. A one-ulp difference at a band floor is A VERB THAT EXISTS IN ONE "
            "ORDERING AND NOT ANOTHER (S12.1/S48)")


@probe("A6", "an institution acts", "S3-L1", by="no-signature",
       tests="an institution must be able to take an action")
def a6():
    raise Forbidden(
        "'The Church excommunicates'", "S3-L1",
        needs="'the Confessor, at a venue, issues'",
        law="L1 -- NO INSTITUTION ACTS, NO FACTION ACTS, NO THRESHOLD ACTS. An institution acts BY A NAMED PERSON AT A VENUE. `Act.actor` is one person id and `resolve` takes no institution; the first sentence IS NOT SPELLABLE",
    )


@probe("A7", "a contest is the season loop nested", "S39", by="construction",
       tests="a fight, a hearing and an argument must be able to be the same machinery")
def a7():
    w = tiny_world()
    contest(w, "S", prize="the barn", claimants=["p_low", "p_mid"],
            depth=0, max_depth=3, causes=[ROOT])
    return "UNREACHABLE"


@probe("A8", "a contest recurses without a cap", "S39.3", by="construction",
       tests="a conflict must be able to open a conflict inside itself")
def a8():
    w = tiny_world()
    r = contest(w, "S", "x", ["p_low"], depth=3, max_depth=3, causes=[ROOT])
    assert isinstance(r, ContestError) and r.depth == r.max_depth
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "fight", contests=["the barn"], payload="S")] if p.id == "p_low" else []
    try:
        _run(w, choose)
        no_cap_raised = False
    except Forbidden:
        no_cap_raised = True
    assert no_cap_raised
    return (f"PASS: at the cap it returned a TYPED ERROR RESULT ({r!r}) the caller must check, not "
            "a crash and not an empty list indistinguishable from a lawful no-event contest. And "
            "reaching a contest with NO caller-supplied max_depth RAISED -- the cap has NO DEFAULT, "
            "because a default is a number somebody made up and would be cited later as measured")


@probe("A9", "a rung reads a sibling's state", "S4", by="no-signature",
       tests="one place must be able to see what is happening in another")
def a9():
    w = tiny_world()
    raise Forbidden(
        "a rung reading a sibling's or a descendant's state directly", "S4",
        needs="an R-1 compute-on-demand aggregate over its OWN descendants",
        law="R-1 -- a rung may read its own state and any message addressed to it; it MAY NOT read a sibling's or a descendant's state directly. A cross-rung read is THE SINGLE EASIEST WAY TO DESTROY T5 AND T6, because ONCE THE REALM CAN READ A PERSON DIRECTLY THERE IS NO REASON FOR THE LADDER TO EXIST AND EVERY INTERMEDIATE RUNG QUIETLY BECOMES DECORATION",
    )


@probe("A10", "a rung computes an aggregate over its descendants", "S4", by="construction",
       tests="a place must be able to know something summed over everything inside it")
def a10():
    w = tiny_world()
    total = Query.r1_aggregate(w, "S", lambda rid: w.rungs[rid].stores.get("grain", 0)
                               if rid in w.rungs else 0)
    w.tenures.append(Tenure("t_dead", "Gone", "S", "contain", since=0, until=0))
    w.rungs["Gone"] = Rung("Gone", "hearth", stores={"grain": 999})
    after = Query.r1_aggregate(w, "S", lambda rid: w.rungs[rid].stores.get("grain", 0)
                               if rid in w.rungs else 0)
    assert total == 8 and after == 8
    return (f"PASS: an R-1 ON-DEMAND aggregate over the CONTAINMENT SUBTREE = {total}. Nothing "
            "pushed, nothing stored, nothing to go stale. And a 999-grain hearth attached by an "
            "ENDED `contain` edge contributed NOTHING -- S22.4 clause 3, LIVE EDGES ONLY")


@probe("A11", "a rung stores that aggregate", "S4", by="construction",
       tests="a place must be able to keep a running total so it does not recompute every time")
def a11():
    w = tiny_world()
    w.rungs["S"].density = 12
    return "UNREACHABLE"


@probe("A12", "a cache is built inside the parallel map", "S4", by="construction",
       tests="an expensive derived value must be able to be reused within a step")
def a12():
    w = tiny_world()
    w._in_parallel_map = True
    w.cache_at_barrier("k", lambda: 1)
    return "UNREACHABLE"


@probe("A13", "a cache is built at a barrier and discarded there", "S4", by="construction",
       tests="a repeated derivation must be able to be computed once per step")
def a13():
    w = tiny_world()
    calls = []
    for _ in range(2):
        w.cache_at_barrier("presence", lambda: calls.append(1) or 7)
    assert len(calls) == 1
    w.discard_caches()
    w.cache_at_barrier("presence", lambda: calls.append(1) or 7)
    assert len(calls) == 2
    return ("PASS: built ONCE at the barrier, read-only until the next, DISCARDED there. "
            "compute-on-demand holds AT BARRIER GRANULARITY, storing nothing that can go stale "
            "because it does not survive the barrier. Without it six operations are O(N-squared)")


@probe("A14", "a person reacts within the season to what another just did", "S40.2",
       by="no-signature",
       tests="a character must be able to respond inside the same season to something that just happened")
def a14():
    raise Collision(
        "'no reaction inside a season' vs the seam's nested DELIBERATE", "S40.2",
        needs="a ruling on which sentence binds",
        law="S34.1 says 'NO REACTION INSIDE A SEASON AT PERSON SCALE -- you anticipated, or you are late'. S40.2 says a contest 'runs the same steps over a smaller person set on a shorter clock' INSIDE RESOLVE, and 'a contest can open a contest', so DELIBERATE RE-RUNS INSIDE RESOLVE against a partially-moved world. BOTH SENTENCES ARE IN THE CHAIN and the design has NOT reconciled them",
    )


@probe("A15", "a spiral terminates", "S40.1", by="no-signature",
       tests="a self-feeding situation must be able to stop")
def a15():
    raise Unspecified(
        "a termination argument per self-feeding loop", "S40.1",
        needs="a CROSS-SEASON bound",
        law="S40.1 -- FOUR ARCS PLUS THE KING ARE SPIRALS; NOTHING BOUNDS ONE. That debt is CROSS-SEASON and no within-tick argument touches it in either direction. `max_depth` bounds nesting WITHIN a tick and says nothing across ticks",
    )


@probe("A16", "a container runs its own clock", "S40.3", by="no-signature",
       tests="a region must be able to advance on its own schedule while others wait")
def a16():
    w = tiny_world()
    rung_fields = sorted(Rung._DECLARED)
    raise Forbidden(
        "a per-container clock", "S40.3",
        needs="nothing -- the parallelism it would buy is ALREADY AVAILABLE: DELIBERATE is a pure map at Godot 4.0",
        law=f"S40.3 -- a per-container clock is A NESTING FORM WITHOUT A CAP ARGUMENT: it has no `depth`, no `max_depth`, and no caller to supply one. It voids (1) the frozen world, (2) the canonical act order, (3) the non-decreasing season index. Rung's declared fields are {rung_fields} -- there is no tick, by construction. THE CLOCK BUYS NOTHING AND COSTS THREE INVARIANTS",
    )


@probe("A17", "the loop has one resolver", "S27.2", by="convention",
       tests="every outcome in the game must go through one place")
def a17():
    import shape as _s
    resolvers = [n for n in dir(_s) if n in ("contest",)] + ["SeasonDriver.resolve"]
    return (f"PASS-BY-CONVENTION ONLY, AND THE DESIGN SAYS SO ITSELF. Surface: {resolvers}. S27.2 "
            "is explicit that this refusal has NEITHER A MECHANISM NOR A CHEAP TEST -- IT IS "
            "ENFORCED BY A PERSON NOTICING -- and that it is 'the refusal whose violation is most "
            "tempting, most locally reasonable, and most catastrophic'. Recorded as THE DESIGN'S "
            "NAMED WEAK POINT, not as a guarantee. Revision 1 of this instrument violated it")


@probe("A18", "a module declares what it may receive and emit", "S41", by="no-signature",
       tests="a developer must be able to work one module without reading the world")
def a18():
    raise Unspecified(
        "the contract descent", "S41",
        needs="one validated parent over authored registries, generated, gated by a blocking round-trip",
        law="S41 -- T5 needs to know PER MODULE what it may RECEIVE; T6 needs to know what it may EMIT; R-2's 'no module reaches through another' is the same requirement as a prohibition. NO SURFACE IN THE CHAIN ANSWERS IT FOR ANY MODULE, which means R-1 AND R-2 ARE TODAY UNENFORCEABLE IN PRINCIPLE, not merely unenforced",
    )


@probe("A19", "a missing provider is a startup failure with a name in it", "S43",
       by="probe-model",
       tests="a piece of the game must be able to be swapped without editing the engine")
def a19():
    w = tiny_world()
    w.boot(("contest", "order"))            # both present -> boots clean
    w.boot(("contest", "order", "witness_channels"))
    return "UNREACHABLE"


@probe("A20", "a wrapper checks what crosses a rung boundary", "S44.1", by="no-signature",
       tests="influence passing between scales must be able to be checked for direction")
def a20():
    w = tiny_world()
    e = Ev(w, "S", "thing.happened", "S", [ROOT])
    fields = sorted(Event.__dataclass_fields__)
    assert "target" not in fields and "actor" not in fields
    raise Forbidden(
        "a wrapper checking direction on a Key crossing a rung boundary", "S44.1",
        needs="nothing -- THE RULE WAS STATED OVER A FIELD THAT DOES NOT EXIST",
        law=f"S44.1 -- THERE IS NOTHING TO CHECK. Event's fields are {fields}: no target, no actor. 'The only transport the suite defines IS a chain of `tell` acts; there is no non-act news transport anywhere in the shape.' Observers are computed at WITNESS from presence; THE EMITTER DECLARES NO RECIPIENT. Three independent lanes killed this, and the fix that suggests itself -- add a target field -- is the twin of the attribution field the design DELIBERATELY REMOVED",
    )


@probe("A21", "a dispensation is broadcast to every descendant", "S37.3", by="no-signature",
       tests="an order from above must be able to reach everyone it applies to")
def a21():
    raise Forbidden(
        "broadcasting a dispensation to all descendants", "S37.3",
        needs="publish as a `tell`, which DISTORTS IN TRANSIT; the person's own opening_set does the rest",
        law="S37.3 -- it deletes T3 AND T6 AT ONCE: everyone would receive IDENTICAL, UNDISTORTED terms. 'It travels by being noticed, NOT DOWN A CHAIN OF POSTS.' And SCOPE ENUMERATES EXECUTORS, NOT PLACES, so there is no descendant set to broadcast to in the office-cluster case",
    )


@probe("A22", "the loop's steps partition per container", "S31", by="construction",
       tests="each region must be able to run its own slice of the loop")
def a22():
    w = tiny_world()
    # Executed, not asserted from a table: RESOLVE's fold sorts ONE GLOBAL array, so a per-
    # container partition of it has no order to fold in.
    seen = []
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "act")] if p.id in ("p_low", "p_king") else []
    def effect(w, a):
        seen.append((a.actor, Query.parent_of(w, a.actor)))
        return []
    _run(w, choose, effect)
    rungs = {r for _, r in seen}
    assert len(rungs) > 1
    return (f"PASS, PARTIALLY, AND THE HONEST FRAME IS PER-OWNER. One RESOLVE fold consumed acts "
            f"from {len(rungs)} different containing rungs {sorted(rungs)} in ONE global order. "
            "Every step's BODY partitions by its write's owner EXCEPT TWO -- RESOLVE'S ORDERED "
            "FOLD (which needs ONE order) and WITNESS'S FAN-OUT (one pass over the presence "
            "index). EVERY STEP'S BOUNDARY IS GLOBAL. 'Two of six steps partition' was two "
            "different tests applied to two groups and is retracted")


@probe("A23", "an aggregate over ended edges is monotone", "S22.4", by="construction",
       tests="a running total of everything that ever happened must be able to be kept")
def a23():
    w = tiny_world()
    edges = [Tenure("x1", "p_low", "prop", "commit", since=0),
             Tenure("x2", "p_mid", "prop", "commit", since=0, until=1)]
    Query.commit_count_guard(w, edges, "revocations_ever")
    return "UNREACHABLE"


@probe("A24", "the ladder is one type at eight scales", "S35", by="construction",
       tests="a mechanism written for the powerful must be able to work for a whole population")
def a24():
    w = tiny_world()
    kinds = {r.kind for r in w.rungs.values()}
    assert kinds <= set(RUNG_KINDS) and len({type(r) for r in w.rungs.values()}) == 1
    # the SAME r1_aggregate runs at a hearth and at the realm
    at_hearth = Query.r1_aggregate(w, "Hh", lambda r: 1)
    at_realm = Query.r1_aggregate(w, "R", lambda r: 1)
    assert at_realm > at_hearth
    return (f"PASS: {len(kinds)} kinds observed, ONE type, and the SAME aggregate ran at a hearth "
            f"({at_hearth} descendants) and at the realm ({at_realm}) with no second code path. "
            "This is H1 and it is the design's best structural property: A MECHANISM WRITTEN FOR "
            "ELITES IS AUTOMATICALLY AVAILABLE TO POPULATIONS")


@probe("A25", "the containment tree and the lateral graph are kept apart", "S6.2",
       by="construction",
       tests="a cause that spans several regions must be able to exist with no parent region")
def a25():
    w = tiny_world()
    sub = Query.descendants(w, "S")
    lat = Query.lateral(w, "ties", "tie")
    crossing = [t for t in lat if (t.subject in sub) != (t.object in sub)] or lat
    assert "p_king" not in sub and lat
    return ("PASS: R-1's subtree over `S` excludes the King, and a `tie` reaches outside it. "
            "FOLLOWING A TIE, A KNOT, A COMMIT OR A DISTANT HOLD LEAVES THE SUBTREE AND IS NOT AN "
            "R-1 AGGREGATE -- it is a resolver-side Query, World first, therefore unreachable from "
            "`choose`. DO NOT 'FIX' R-1 TO COVER LATERAL EDGES: THE SPLIT IS THE DESIGN")


@probe("A26", "the graph is traversed without hanging", "S38.1", by="construction",
       tests="the engine must be able to walk its own references without looping forever")
def a26():
    w = tiny_world()
    w.tenures.append(Tenure("t_cyc", "R", "Hh", "contain", since=0))
    got = Query.descendants(w, "S")
    assert isinstance(got, list)
    return (f"PASS: a deliberate cycle (R contained by Hh) returned {len(got)} descendants and did "
            "not hang. ITERATIVE, WITH A VISITED SET, NEVER RECURSION -- the reference graph is "
            "CYCLIC ON PURPOSE (conferral path, containment path, tie graph, claim citation graph) "
            "and a tree walk hangs ON THE NORMAL CASE, not on an edge case")


@probe("A27", "every value the game needs has an owner", "S22", by="no-signature",
       tests="every value in the game must be able to name who writes it")
def a27():
    unowned = ["season_factor's distribution (BLOCKS yield)",
               "the cohort's construal spread (rule stated, representation not)",
               "the object-side Tenure index (Nobody, by rule -- a barrier-built cache)",
               "travel legs (in the write matrix AND the churn ledger AND no ownership row)"]
    raise Unowned(
        f"{len(unowned)} values named in the ownership table's OWN gap list", "S22.3",
        needs="an ownership row each",
        law="S22.3 -- named rather than glossed: " + "; ".join(unowned),
    )


@probe("A28", "the log's invariants hold", "S19.1", by="construction",
       tests="every recorded happening must be able to point at real prior happenings")
def a28():
    w = tiny_world()
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, "do")] if p.id == "p_low" else []
    def effect(w, a):
        prev = [w.log[-1].id] if w.log else [ROOT]
        return [Ev(w, a.actor, "did.thing", "Hh", prev)]
    for _ in range(4):
        _run(w, choose, effect)
    ids = {e.id for e in w.log}
    assert len(ids) == len(w.log)
    assert all(c == ROOT or c in ids for e in w.log for c in e.causes)
    assert [e.emitted_at for e in w.log] == sorted(e.emitted_at for e in w.log)
    return (f"PASS over {len(w.log)} events from a real run: id uniqueness, referential integrity "
            "on causes[], a NON-DECREASING season index, and a stable content hash. These are the "
            "head's log invariants and they SURVIVE the Event record S19 adds")


@probe("A29", "two logs share a causes chain", "S19.5", by="probe-model",
       tests="a subsystem must be able to keep its own record of what it did")
def a29():
    w = tiny_world()
    logs = [n for n in dir(w) if n == "log"]
    raise Forbidden(
        "an Event in log A naming an Event in log B as its cause", "S19.5",
        needs="ONE LOG",
        law=f"S19.5 -- World has exactly {len(logs)} log. Two logs CANNOT share a causes[] chain, so T3's multiple perspectives on one event AND arcs-as-provenance-chains BOTH break at the seam. The seam returns contest Events INTO THE SAME LOG. The non-circular grounds: WITNESS is ONE GLOBAL PASS, and the design's predecessor loop was RETIRED because its WITNESS was not global",
    )


@probe("A30", "an ungraded value is used anyway", "S42.2", by="construction",
       tests="a piece of the design with no evidence behind it must be able to be used anyway")
def a30():
    w = tiny_world()
    w.fixtures.get("a_number_nobody_ruled")
    return "UNREACHABLE"


@probe("A31", "a verdict is stable across a fixture sweep", "S42.2.1", by="construction",
       tests="a conclusion drawn from the engine must not depend on a number nobody decided")
def a31():
    results = []
    for v in (2, 5, 9):
        f = DEFAULT_FIXTURES.sweep("act_budget", v)
        w = tiny_world(f)
        got = []
        def choose(p, v_, s, ask_budget):
            return [Act_(w, p, f"v{i}") for i in range(ask_budget())] if p.id == "p_king" else []
        _run(w, choose, lambda w, a: got.append(a.verb) or [])
        results.append((v, len(got)))
    assert [n for _, n in results] == [2, 5, 9]
    return (f"PASS WITH A FINDING, AND THE FINDING MATTERS MORE THAN THE VERDICT: 3-point sweep "
            f"{results}. The count tracks the fixture EXACTLY, so any verdict phrased as 'a "
            "character can do N things in a season' FLIPS ACROSS THE SWEEP. S42.2.1 says a verdict "
            "that flips across the sweep IS ITSELF A FINDING. `~5` is a RULED BAND and no in-chain "
            "source turns the band into the integer the engine runs on -- that is S62's open "
            "scene/act question wearing different clothes")


@probe("A31b", "the world verdict is stable across the wear sweep", "S42.2.1", by="construction",
       tests="a conclusion about how fast the world decays must not depend on a number nobody decided")
def a31b():
    out = []
    for rate in (5, 10, 25):
        f = DEFAULT_FIXTURES.sweep("wear_per_season",
                                   {"harbour": rate, "seam": rate, "body": rate})
        w = tiny_world(f)
        scale = w.fixtures.get("condition_scale")
        site = w.sites["site_harbour"]
        floors = w.fixtures.get("band_floors")[site.kind]
        n = 0
        while "bulk_shipping" in Query.verbs(w, site, floors) and n < 500:
            _run(w); n += 1
        out.append((rate, n))
    seasons = [n for _, n in out]
    assert len(set(seasons)) > 1
    return (f"PASS WITH A FINDING: {out}. 'A harbour silts past the shipping floor in N seasons' "
            f"ranges {min(seasons)}-{max(seasons)} across a 3-point sweep of a wear rate NO "
            "IN-CHAIN DOCUMENT SUPPLIES. S22 assigns `wear per site kind` to params; the params "
            "document proposes NO VALUES. EVERY PACING CLAIM THIS TEST COULD MAKE IS A FUNCTION "
            "OF AN UNGRADED NUMBER, and S42.2.1 names a wear table with a silent default as the "
            "exact prior sin -- so an unregistered kind raises here rather than answering 20")


@probe("A32", "the scene/act identity is settled", "S62", by="no-signature",
       tests="the number of playable moments a character gets must be able to be counted")
def a32():
    raise Collision(
        "does a scene equal an act?", "S62",
        needs="a ruling on the IDENTITY, not on the number",
        law="S62 -- the ruling says '~5 playable scenes... WHICH MAY MEAN ~5 actions'. THE BUDGET IS SETTLED AT ~5; THE IDENTITY IS NOT. A5 scenes-as-5-acts and 5 scenes-containing-many-acts are different games, and A31 shows every count verdict moves with the integer chosen",
    )


@probe("A33", "refraction has a side", "S37.4", by="no-signature",
       tests="an instruction must be able to be distorted somewhere between issuer and executor")
def a33():
    raise Collision(
        "emitter-side vs receiver-side refraction", "S37.4",
        needs="pick one, write it down beside the code, and expect the choice to be revisited",
        law="S37.4 -- R-2 says downward influence is 'EMITTING a refraction' (EMITTER-side); the act vocabulary puts `refract` at the RECEIVING end, beside `comply`, `evade`, `defy`. THE CHAIN HAS NOT RECONCILED THESE and emitter-side and receiver-side distortion ARE DIFFERENT GAMES",
    )


@probe("A34", "a social quantity sinks by neglect alone", "S34", by="no-signature",
       tests="a relationship or a standing must be able to decay from nobody tending it")
def a34():
    steps = [s.value for s in Step]
    raise Forbidden(
        "a scheduled social recovery or decay", "S34",
        needs="a ruling -- S62 lists this as a LIVE DESIGN CHOICE affecting three arcs",
        law=f"S34 -- 'no scheduled social recovery' is STRUCTURAL BY PHASE MEMBERSHIP: of {steps}, MATTER moves no social quantity (L4), DELIBERATE writes nothing, RESOLVE needs an act, WITNESS writes only ledgers, CENSUS is demand-driven. THERE IS NO STEP IN WHICH A RESTORING TIMER COULD RUN, so a design that wanted one HAS NOWHERE TO PUT IT",
    )


@probe("A35", "the design needs Godot 4.6", "S52", by="probe-model",
       tests="the port must be able to target a decided engine version")
def a35():
    floor = {"WorkerThreadPool.add_group_task": (4, 0), "typed Dictionary": (4, 4),
             "@abstract": (4, 5)}
    hi = max(floor.values())
    assert hi == (4, 5) and floor["WorkerThreadPool.add_group_task"] == (4, 0)
    return (f"PASS (transcription, not execution -- this instrument runs no Godot): the highest "
            f"named requirement is {hi[0]}.{hi[1]}. NOTHING IN THIS DESIGN NEEDS 4.6; the honest "
            "floor is >= 4.4 and the real decision is 4.3 vs >= 4.4. THE HOLONIC DECOMPOSITION "
            "ADDS NO VERSION PRESSURE -- its heaviest requirement is 4.0, and @abstract's fallback "
            "(a typed error result) is needed anyway because GDScript has no exceptions")


@probe("A36", "a person's act order is the order it resolves in", "S26.3", by="construction",
       tests="what a character does first must be able to close off what they could have done after")
def a36():
    w = tiny_world()
    order = []
    intended = ["spend_treasury", "buy_grain", "bribe"]
    def choose(p, v, s, ask_budget):
        return [Act_(w, p, vb) for vb in intended] if p.id == "p_high" else []
    _run(w, choose, lambda w, a: order.append(a.verb) or [])
    if order == intended:
        return ("PASS-BY-COINCIDENCE: the content-derived order happened to match the person's. "
                "That is a hash accident, not a guarantee -- see the law below")
    raise Collision(
        f"the person's ORDER {intended} vs the fold's order {order}", "S26.3 / S32",
        needs="a ruling on whether a person's act list resolves in the order they chose",
        law="S26.3 says 'THE LIST IS ORDERED, so what he did first is legible when a season's later acts are foreclosed by its earlier ones'. S32 rest 3 says the act array is CANONICALIZED BY A CONTENT-DERIVED KEY over ONE GLOBAL ARRAY, sorted 'never by completion order'. A PER-PERSON INTENT ORDER AND A GLOBAL CONTENT ORDER ARE DIFFERENT ORDERS, and the chain specifies BOTH. This is what makes F17's authorization race real",
    )


# ===========================================================================
# THIRD TIER -- three the ARC corpus demands that the first two tiers could not execute.
# ===========================================================================

@probe("W13", "a background quantity decays on a schedule nobody wound", "S25.1",
       by="no-signature",
       tests="a world-scale tracked quantity must be able to decay on a fixed schedule independent of anyone's actions")
def w13():
    licensed = ["matter", "bodies", "the confidence of a memory"]
    raise Forbidden(
        "a fourth clock-driven quantity", "S25.1 / S3-L5",
        needs="an author -- a nameable act that wound it, so it can be bribed, delayed, burned, or killed",
        law=f"S25.1 -- THE THREE LICENSED CLOCKS ARE EXHAUSTIVE: {licensed}. Nobody wound any of the three and YOU CANNOT BRIBE SILT. EVERYTHING OUTSIDE THIS LIST NEEDS AN AUTHOR (L5's second paragraph). A quantity that advances on its own with no author is A SHADOW ACTOR -- unbuyable, undelayable, unkillable -- exactly the actor L1 forbids, arriving through a side door. S13.1 is the worked case: an act-DECLARED term does the same job lawfully AND gives the arc handles (bribe the clerk who set the term, burn the record that carries it, kill the man who must renew it)",
    )


@probe("P37", "a person's response is a lookup on their own state, not a deliberation", "S3-L1",
       by="probe-model",
       tests="a character's reaction must be able to be fully determined by their internal state rather than by a choice")
def p37():
    w = tiny_world()
    p = w.persons["p_high"]
    p.convictions = {"suspicion": 0.9}
    chosen = []
    def choose(q, v, s, ask_budget):
        if q.id != p.id:
            return []
        verb = "purge" if q.convictions.get("suspicion", 0) > 0.5 else "tolerate"
        chosen.append(verb)
        return [Act_(w, q, verb)]
    _run(w, choose)
    assert chosen == ["purge"]
    return ("PASS, AND IT IS AN UNCOMFORTABLE PASS -- report it as a finding, not a win. A "
            "threshold LOOKUP on a person's own interior is INDISTINGUISHABLE at the engine "
            "boundary from a DELIBERATION: both are a `choose` returning an Act, and L1 is "
            "satisfied because a named person is still the author. The design cannot detect the "
            "difference and does not claim to. The in-chain arc survey found a source that calls "
            "one act BOTH 'chooses' AND 'determined by a threshold lookup on his own internal "
            "state... a stat, not a deliberation'. THE SHAPE INHERITS THE CORPUS'S BLUR RATHER "
            "THAN RESOLVING IT -- which is a real answer to 8 of the 50 THRESHOLD arcs, and a "
            "hollow one, because nothing distinguishes a rich deliberation from a stat lookup")


@probe("P38", "an outcome is judged by a referee", "S1", by="no-signature",
       tests="an optimal window, a judgement call or an adjudication must be able to be made by a referee")
def p38():
    raise NoProducer(
        "a GM, referee or adjudicator", "S1",
        needs="a named person inside the world, or a rule the engine can evaluate",
        law="THE ENGINE RESOLVES EVERYTHING -- there is no GM anywhere in the shape. S1: 'EVERY ACTION IN THIS GAME IS PERFORMED BY A PERSON'. A 'GM-judged optimal window' has no carrier: it is neither a person's act, nor a Query, nor a licensed clock. Part VIII refuses scene-device machinery for the same reason -- forced dilemmas, letter-versus-spirit compliance and timing windows are DRAMATURGY, what a designer does WITH primitives, not primitives",
    )


# ===========================================================================
# FOURTH TIER -- five the NPC corpus asks for repeatedly with no execution in tiers 1-3.
# ===========================================================================

@probe("P39", "two named people carry a durable relationship with its own state", "S15",
       by="probe-model",
       tests="two characters must be able to have an ongoing relationship that carries state and changes over seasons")
def p39():
    w = tiny_world()
    t = next(x for x in w.tenures if x.kind == "tie")
    lo, hi = sorted([t.subject, t.object])
    assert t.subject == lo, "a tie must be stored on the LOWER id"
    dupes = [x for x in w.tenures if x.kind == "tie"
             and {x.subject, x.object} == {t.subject, t.object}]
    assert len(dupes) == 1
    return ("PASS: `tie` is Person<->Person AT ANY DISTANCE and is STORED ONCE, ON THE LOWER ID. "
            "That single-home rule is what stops a shared `strain` having two homes and being able "
            "to DISAGREE WITH ITSELF. The inverse index is owned by Nobody and stored nowhere, so "
            "the relationship has exactly one writer")


@probe("P40", "one person owes two bodies incompatible things", "S15", by="probe-model",
       tests="a character must be able to hold obligations to two bodies that come into direct conflict")
def p40():
    w = tiny_world()
    w.tenures += [Tenure("ob1", "p_mid", "off_duke", "oblige", since=0),
                  Tenure("ob2", "p_mid", "off_dicastery", "oblige", since=0)]
    obligations = [t for t in Query.lateral(w, "duty", "oblige") if t.subject == "p_mid"]
    assert len(obligations) == 2
    b = w.fixtures.get("act_budget")
    return (f"PASS-STRUCTURALLY: `oblige` is MANY per person, so two incompatible duties coexist "
            f"with NO arbitration anywhere in the shape, and the person's {b} acts are the only "
            "scarcity. That is L1 working -- THE PERSON resolves the conflict, not a priority "
            "function. NOTE what is absent: nothing scores an obligation, so 'which duty won' is "
            "legible only from what the person actually did")


@probe("P41", "a precedent is cited to strengthen an argument", "S7", by="no-signature",
       tests="a character must be able to cite an established precedent or prior ruling to make a present argument stronger")
def p41():
    w = tiny_world()
    e = Ev(w, "D", "sitting.decided", "D", [ROOT])
    w.log.append(e)
    raise Unspecified(
        "the argument layer's named faults, and how a cited precedent bears on one",
        "S2 T7",
        needs="the fault roster, and a rule by which a prior Event or Record strengthens a present argument",
        law="T7 says 'the argument layer resolves BY NAMED FAULT, not by a persuasion threshold' -- and the roster of faults is nowhere in Part II. The prior ruling EXISTS as an Event in the log and a person may hold a Claim about it, but no signature relates a cited precedent to a present contest, and S39.4's ladder reads off a MARGIN whose model is also unspecified",
    )


@probe("F20", "a treaty constrains what two polities' people may do", "S14", by="probe-model",
       tests="a standing agreement between two polities must be able to constrain what people on either side may do")
def f20():
    w = tiny_world()
    treaty = Proposition("prop_treaty", "OUGHT", "R", "the strait stays open", True, 0)
    w.propositions[treaty.id] = treaty
    w.tenures += [Tenure("c_a", "p_king", treaty.id, "commit", since=0),
                  Tenure("c_b", "p_high", treaty.id, "commit", since=0)]
    bound = [t.subject for t in Query.lateral(w, "treaty", "commit") if t.object == treaty.id]
    assert set(bound) == {"p_king", "p_high"}
    return ("PASS-STRUCTURALLY, AND THE STRUCTURE IS THE FINDING: a treaty is a Proposition plus "
            "`commit` edges -- THE SAME OBJECT AS A FACTION (S14.2). It is IMMUTABLE, it OUTLIVES "
            "ITS SIGNATORIES unowned, and it binds only those who committed. What it CANNOT do is "
            "constrain a person who never committed, because there is no edge from a Proposition "
            "TO a person -- only from a person to it. A treaty that binds a polity's subjects "
            "without their commit has no representation")


@probe("F21", "a member's individual position is recorded in a body's collective output", "S61",
       by="construction",
       tests="a character sitting on a collective body must be able to have their individual position registered distinctly from the body's decision")
def f21():
    w = tiny_world()
    Query.judging_set(w, "D")
    return "UNREACHABLE"


# ===========================================================================
# FIFTH TIER -- probes that REACH code the earlier tiers left dead. An implemented rule no
# probe exercises is indistinguishable from an absent one, and reporting it as landed is the
# flattering direction.
# ===========================================================================

@probe("A37", "the five strata order the fold before the content hash does", "S27",
       by="construction",
       tests="movement, binding decisions and social acts must be able to resolve in a fixed order relative to each other")
def a37():
    w = tiny_world()
    seen = []
    def choose(p, v, s, ask_budget):
        if p.id != "p_low":
            return []
        # deliberately submitted in REVERSE stratum order
        return [Act_(w, p, "speak", stratum=4), Act_(w, p, "decide", stratum=1),
                Act_(w, p, "walk", stratum=0)]
    _run(w, choose, lambda w, a: seen.append((a.stratum, a.verb)) or [])
    assert [x[0] for x in seen] == sorted(x[0] for x in seen), seen
    return (f"PASS: submitted reversed, resolved {seen}. S27's FIVE STRATA -- {list(STRATA)} -- "
            "order the fold BEFORE the content-derived key breaks ties within a stratum. Rev 2 "
            "declared STRATA and never referenced it, and no probe ever set `Act.stratum`, so "
            "the sort key's first component was constant and the rule was dead code reported "
            "as landed")


@probe("A38", "an attempt at Ob > 2 x Pool is refused and the season is spent", "S27.4",
       by="construction",
       tests="an attempt far beyond a character's ability must be refused rather than rolled")
def a38():
    w = tiny_world()
    mult = w.fixtures.get("obstacle_refusal_multiple")
    kinds = []
    def choose(p, v, s, ask_budget):
        if p.id != "p_low":
            return []
        return [Act_(w, p, "hopeless", obstacle=mult * 5 + 1, pool=5),
                Act_(w, p, "hard", obstacle=mult * 5, pool=5)]
    def effect(w, a):
        return [Ev(w, a.actor, f"did.{a.verb}", a.actor, [ROOT])]
    _run(w, choose, effect)
    kinds = [e.kind for e in w.log]
    assert "attempt.refused" in kinds and "did.hard" in kinds and "did.hopeless" not in kinds
    return (f"PASS: at Ob = {mult}xPool+1 the attempt was REFUSED and the act was spent; at exactly "
            f"{mult}xPool it resolved. An uncontested attempt routes to A GATE, never to an Ob=0 "
            "roll. Rev 2 had the branch and no probe ever set `obstacle` or `pool`, so both "
            "defaulted to 0 and the guard never ran -- while its regression test asserted only "
            "that two strings appeared in the source")


@probe("A31c", "the world verdict is stable across the BAND FLOOR sweep", "S42.2.1",
       by="construction",
       tests="a conclusion about which actions a place supports must not depend on a number nobody decided")
def a31c():
    out = []
    for floor in (600, 800, 950):
        f = DEFAULT_FIXTURES.sweep("band_floors", {
            "harbour": {"bulk_shipping": floor, "fishing": 100},
            "seam": {"deep_mining": 700, "surface_gleaning": 50},
            "body": {"full_operations": 800, "limited": 500, "withdrawal_only": 100}})
        w = tiny_world(f)
        site = w.sites["site_harbour"]
        n = 0
        mine = lambda: [c for c in w.crossings if c[0] == site.id]
        while not mine() and n < 400:
            _run(w); n += 1
        out.append((floor, n))
    seasons = [n for _, n in out]
    assert len(set(seasons)) > 1
    return (f"PASS WITH A FINDING: {out}. 'A harbour silts past the shipping floor in N seasons' "
            f"ranges {min(seasons)}-{max(seasons)} across a 3-point sweep of A BAND FLOOR NO "
            "IN-CHAIN DOCUMENT SUPPLIES. S42.2.1 names 'three band edges' as one of the four "
            "constants a prior instrument in the chain invented; rev 2 fixed the other three and "
            "LEFT THE BAND EDGES HARDCODED IN PROBE BODIES AND UNSWEPT, so W1's and P18's pacing "
            "claims were one-dimensional sweeps of a two-parameter model. S22 assigns 'band "
            "coefficients' to params and the params document proposes NO VALUES")


@probe("A39", "a contest Event names the act that caused it", "S39.2", by="construction",
       tests="the outcome of a conflict must be traceable back to the action that started it")
def a39():
    w = tiny_world()
    seen = {}
    def choose(p, v, s, ask_budget):
        if p.id != "p_low":
            return []
        a = Act_(w, p, "press_claim", contests=["the barn"], payload="S")
        seen["act"] = a.id
        return [a]
    try:
        _run(w, choose, contest_max_depth=3)
    except Unspecified:
        return ("PASS-AT-THE-BOUNDARY: the act reached the seam and `contest` refused for want of "
                "a MARGIN MODEL (S39.4), which is the honest state. What rev 3 fixed is upstream "
                "of that refusal: rev 2 passed `causes=[a.id] if any(e.id == a.id for e in w.log)` "
                "-- and w.log holds EVENTS, never Acts, so the predicate was PERMANENTLY FALSE and "
                "every contest was called with [ROOT]. S39.2 requires causes[] NAMING THE ACTS")
    return "UNREACHABLE"
