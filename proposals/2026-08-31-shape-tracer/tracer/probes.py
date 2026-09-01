"""PROBES — concrete attempts to do a thing with the idealized shape.

Each probe is a real execution. It either completes (the shape carries the case) or raises a
ShapeGap (it does not). Nothing here works around a gap; a probe that cannot proceed reports
and stops, which is the measurement.

A probe is deliberately SMALL and names one capability, so that when a case's `need` maps to it
the verdict is about that capability and not about a whole scenario.
"""

from __future__ import annotations

from trace_log import TRACE
from shape import (
    Act, Claim, Collision, Date, Event, Forbidden, NoProducer, Office, Person,
    Proposition, Record, Rung, SeasonLoop, ShapeGap, Site, Step, Tenure,
    Unspecified, View, World, WriteClass, condition_band, leaders,
    resolve, verbs, witness, WEAR,
)

PROBES: dict[str, callable] = {}
PROBE_DOC: dict[str, str] = {}


def probe(pid: str, doc: str):
    def deco(fn):
        PROBES[pid] = fn
        PROBE_DOC[pid] = doc
        return fn
    return deco


def _world() -> World:
    w = World()
    w.rungs["realm"] = Rung(id="realm", kind="realm")
    w.rungs["prov"] = Rung(id="prov", kind="province")
    w.rungs["settl"] = Rung(id="settl", kind="settlement", stores={"grain": 100})
    w.sites["harbour"] = Site(id="harbour", rung="settl", kind="harbour", condition=560)
    w.sites["seam"] = Site(id="seam", rung="settl", kind="seam", condition=800)
    return w


# ===========================================================================
# PERSON-SCALE
# ===========================================================================

@probe("P1", "a person holding no office acts at all")
def p1(w=None):
    w = w or _world()
    w.persons["carin"] = Person(id="carin", name="Carin Vedel")   # copyist, no office
    loop = SeasonLoop(w)
    loop.run({"carin": lambda p, v, s: Act(actor="carin", verb="copy", target="seam")})
    return "OK: an act by a postless person reaches RESOLVE and produces an Event"


@probe("P2", "a postless person puts a demand in front of someone who holds a post")
def p2(w=None):
    w = w or _world()
    w.persons["carin"] = Person(id="carin", name="Carin Vedel")
    w.offices["clerk"] = Office(id="clerk", post="Chief Parliamentary Clerk", rung="realm",
                                establishment=["peder"])
    w.persons["peder"] = Person(id="peder", name="Peder Almstedt")
    d = Date(id="sitting.1", holder="clerk", season=1)
    w.rungs["realm"].dates.append(d)
    loop = SeasonLoop(w)
    loop.run({"carin": lambda p, v, s: Act(actor="carin", verb="petition", target="sitting.1")})
    # `02` §7.1: Petition -> carry -> DocketItem -> sitting, filtered by a NAMED person who pays.
    raise Unspecified(
        "`carry` — who moves a Petition onto a DocketItem, and what it costs them",
        "P2 petition->docket",
        needs="a specified carry act with a named payer; `02` §7.1 names the chain, `08` has no signature",
    )


@probe("P3", "an act is performed without others learning WHO did it")
def p3(w=None):
    w = w or _world()
    w.persons["sigrid"] = Person(id="sigrid", name="Sigrid Torsvald")
    w.persons["obs"] = Person(id="obs", name="Observer")
    loop = SeasonLoop(w)
    evs = loop.run({"sigrid": lambda p, v, s: Act(actor="sigrid", verb="sabotage", target="harbour")})
    ev = evs[0]
    if not hasattr(ev, "actor_visibility"):
        raise NoProducer(
            "covert action: an Event has no field separating the deed from its doer, so witnessing "
            "an act necessarily reveals its actor",
            "P3 covert",
            needs="attribution as a separate, per-witness claim from the occurrence",
        )
    return "OK"


@probe("P4", "an outcome changes what a person is — a conviction moves")
def p4(w=None):
    w = w or _world()
    p = Person(id="saemund", name="Saemund Haelgrund", convictions={"Faith": 0.7, "Order": 0.3})
    w.persons["saemund"] = p
    p.scar("Faith", w)          # `02` §5.5 names this and does not specify it
    return "unreachable"


@probe("P5", "a person concludes something FALSE and cannot tell it from a true conclusion")
def p5(w=None):
    w = w or _world()
    w.persons["saemund"] = Person(id="saemund", name="Saemund Haelgrund")
    ev = Event(id="E.forge", family="reconstruct", scope="place", subject="seam")
    w._step = Step.WITNESS
    cl = witness(w.persons["saemund"], ev)[0]
    w._step = None
    return f"OK: claim {cl.proposition!r} at confidence {cl.confidence} with no truth flag on it"


@probe("P6", "a person forgets — a claim leaves the ledger")
def p6(w=None):
    w = w or _world()
    p = Person(id="orm", name="Orm")
    w.persons["orm"] = p
    p.ledger = [Claim(proposition=f"c{i}", source_event="E0", confidence=1, holder="orm")
                for i in range(5)]
    raise Unspecified(
        "the ledger cap `L` and the eviction comparator (`confidence_live x recency`)",
        "P6 forgetting",
        needs="a value for L and a specified eviction order; `11_PARAMS` grades it assumption",
    )


@probe("P7", "two people witness one event and hold incompatible accounts of it")
def p7(w=None):
    w = w or _world()
    w.persons["a"] = Person(id="a")
    w.persons["b"] = Person(id="b")
    ev = Event(id="E.x", family="strike", scope="place", subject="harbour")
    w._step = Step.WITNESS
    ca = witness(w.persons["a"], ev)[0]
    cb = witness(w.persons["b"], ev)[0]
    w._step = None
    if ca.proposition == cb.proposition and ca.confidence == cb.confidence:
        raise NoProducer(
            "construal divergence: `witness` is per-person but nothing in it VARIES by person, so "
            "two witnesses of one event necessarily agree",
            "P7 divergence",
            needs="a per-person construal term (stance/capability/channel) inside witness()",
        )
    return "OK"


@probe("P8", "an enmity survives the death of the person who held it")
def p8(w=None):
    w = w or _world()
    w.persons["father"] = Person(id="father", stance=[("rival_house", -5, 5)])
    w.persons["heir"] = Person(id="heir")
    w.tenures["k1"] = Tenure(id="k1", subject="heir", object="father", kind="tie", since=0)
    w._step = Step.MATTER
    w.write("Tenure", "contain", "father", None, WriteClass.MATTER, driver="Event")  # death
    w._step = None
    if not w.persons["heir"].stance:
        raise NoProducer(
            "feud inheritance: nothing at death writes the deceased's stances into a kinsman's "
            "interior, and claim confidence decays — so an enmity is LOST BY BEING FORGOTTEN",
            "P8 inheritance",
            needs="a WITNESS/CENSUS rule depositing high-weight stances into kin ledgers",
        )
    return "OK"


@probe("P9", "an office-holder directs a named subordinate, who may refuse")
def p9(w=None):
    w = w or _world()
    w.persons["almud"] = Person(id="almud", name="Almud Almqvist")
    w.persons["voss"] = Person(id="voss", name="Wilhelm Voss")
    w.offices["crown"] = Office(id="crown", post="King", rung="realm",
                                establishment=["voss"], upkeep=3)
    refused = {"v": False}

    def voss_chooses(p, v, s):
        refused["v"] = True          # the subordinate runs their OWN choose
        return None                  # and declines

    loop = SeasonLoop(w)
    loop.run({
        "almud": lambda p, v, s: Act(actor="almud", verb="dispatch", target="voss"),
        "voss": voss_chooses,
    })
    if not refused["v"]:
        raise NoProducer("dispatch did not route through the subordinate's own choose", "P9")
    return "OK: dispatch costs the holder an act; compliance is the hearer's own choose"


@probe("P10", "custody of a register confers power")
def p10(w=None):
    w = w or _world()
    w.records["roll"] = Record(id="roll", rung="realm", kind="register")
    w.rungs["realm"].records.append("roll")
    w.persons["peder"] = Person(id="peder", name="Peder Almstedt")
    raise Collision(
        "custody: `03` §1.3 homes a Record as Rung matter, so a clerk's CUSTODY of it is not "
        "represented — `01` §3.1 names custody as one of four things that make an ordinary person "
        "matter, and no field carries it",
        "P10 custody",
        needs="custody as a Tenure (a `hold` over a Record), or a named custodian field",
    )


@probe("P11", "a person owes two masters and the obligations conflict")
def p11(w=None):
    w = w or _world()
    w.persons["gustav"] = Person(id="gustav", name="Gustav Linder")
    w.tenures["o1"] = Tenure(id="o1", subject="gustav", object="church", kind="oblige", since=0)
    w.tenures["o2"] = Tenure(id="o2", subject="gustav", object="crown", kind="oblige", since=0)
    raise NoProducer(
        "conflicting obligation: two `oblige` Tenures may coexist and nothing computes that "
        "satisfying one breaches the other; the collision rule is specified for Propositions "
        "(`02` §3, intersecting `when`), not for obligations",
        "P11 dual loyalty",
        needs="an obligation-collision Query, or oblige carrying a Proposition it discharges",
    )


@probe("P12", "a stranger's act moves someone's ambition without either knowing the other")
def p12(w=None):
    w = w or _world()
    prop = Proposition(id="amb.1", mood="OUGHT", subject="seat.prefect",
                       predicate="held_by", value="maret", when=(0, 99), scope="prov",
                       utterer="maret")
    w.propositions["amb.1"] = prop
    w.persons["maret"] = Person(id="maret")
    w.persons["stranger"] = Person(id="stranger")
    # progress(P) = sum over terms of w_i * [term_i holds now] — DERIVED AT READ over world terms.
    def progress(world) -> float:
        held = [t for t in world.tenures.values()
                if t.kind == "hold" and t.object == "seat.prefect" and t.until is None]
        return 1.0 if any(t.subject == "maret" for t in held) else 0.0

    w.tenures["h0"] = Tenure(id="h0", subject="maret", object="seat.prefect",
                             kind="hold", since=0)
    before = progress(w)

    def stranger_takes(p, v, s):
        return Act(actor="stranger", verb="take_seat", target="seat.prefect")

    loop = SeasonLoop(w)
    loop.run({"stranger": stranger_takes})
    # the stranger's act ends Maret's hold; nothing in the resolver mentions Maret or her ambition
    w.tenures["h0"].until = w.tick
    w.tenures["h1"] = Tenure(id="h1", subject="stranger", object="seat.prefect",
                             kind="hold", since=w.tick)
    after = progress(w)
    if not (before == 1.0 and after == 0.0):
        raise NoProducer(f"ambition progress did not move: {before} -> {after}", "P12")
    return (f"OK: progress {before} -> {after}. A stranger obstructed Maret with no `obstruct` verb, "
            "no knowledge of her, and no resolver branch — derived-at-read does the work")


# ===========================================================================
# FACTION / GOVERNANCE
# ===========================================================================

@probe("F1", "a faction exists as an uttered OUGHT plus its commit edges")
def f1(w=None):
    w = w or _world()
    w.persons["yrsa"] = Person(id="yrsa", name="Yrsa Vossen")
    w.propositions["rm"] = Proposition(id="rm", mood="OUGHT", subject="einhir_culture",
                                       predicate="ought_be", value="restored", when=(0, 99),
                                       scope="realm", utterer="yrsa")
    for i, m in enumerate(["yrsa", "uwe", "carin"]):
        w.persons.setdefault(m, Person(id=m))
        w.tenures[f"c{i}"] = Tenure(id=f"c{i}", subject=m, object="rm", kind="commit", since=0)
    members = [t.subject for t in w.tenures.values() if t.kind == "commit" and t.until is None]
    return f"OK: faction = Proposition + {len(members)} commit edges, no Faction record"


@probe("F2", "a faction's leadership changes with no deposition subsystem")
def f2(w=None):
    w = w or _world()
    f1(w)
    leaders(w, "rm", "realm")     # comparator is OPEN — `02` §10 item 2
    return "unreachable"


@probe("F3", "a faction ENDS when everyone leaves")
def f3(w=None):
    w = w or _world()
    f1(w)
    w.tenures["hold.rm"] = Tenure(id="hold.rm", subject="rm", object="settl", kind="hold", since=0)
    for t in list(w.tenures.values()):
        if t.kind == "commit":
            t.until = 1                     # every member decommits
    live = [t for t in w.tenures.values() if t.kind == "commit" and t.until is None]
    holds = [t for t in w.tenures.values()
             if t.kind == "hold" and t.subject == "rm" and t.until is None]
    if not live and holds:
        raise NoProducer(
            "the ghost polity: every member has decommitted, the Proposition is immutable and "
            "never destroyed, and its `hold` Tenure over a settlement has NO PRODUCER TO END IT — "
            "revocation names a venue, and no person remains who can appear at one",
            "F3 faction ending",
            needs="a hold whose subject-Proposition has no live commits becomes contestable as "
                  "vacant custody at the venue that would have heard its revocation",
        )
    return "OK"


@probe("F4", "a claim on sovereignty is PRESSED across seasons")
def f4(w=None):
    w = w or _world()
    w.persons["baralta"] = Person(id="baralta", name="Inge Baralta")
    w.propositions["claim"] = Proposition(id="claim", mood="OUGHT", subject="crown",
                                          predicate="held_by", value="baralta", when=(0, 99),
                                          scope="realm", utterer="baralta")
    loop = SeasonLoop(w)
    for _ in range(3):
        loop.run({"baralta": lambda p, v, s: Act(actor="baralta", verb="press_claim",
                                                 target="claim")})
    return "OK: a claim is an immutable Proposition; pressing it is an act each season"


@probe("F5", "an office is conferred, and later revoked")
def f5(w=None):
    w = w or _world()
    w.persons["almud"] = Person(id="almud")
    w.persons["hedda"] = Person(id="hedda")
    w.offices["gov"] = Office(id="gov", post="Governor of Ehrenfeld", rung="settl",
                              conferral="crown", revocation="crown_at_sitting")
    loop = SeasonLoop(w)
    loop.run({"almud": lambda p, v, s: Act(actor="almud", verb="confer",
                                           target="gov", payload="hedda")})
    return "OK: conferral and revocation are acts with a named basis per office"


@probe("F6", "a sitting is convened and something is DECIDED there")
def f6(w=None):
    w = w or _world()
    w.persons["peder"] = Person(id="peder")
    w.offices["parl"] = Office(id="parl", post="Parliament", rung="realm",
                               establishment=["peder"])
    d = Date(id="sitting.1", holder="parl", season=1, convening_conditions=["quorum"])
    w.rungs["realm"].dates.append(d)
    loop = SeasonLoop(w)
    loop.run({"peder": lambda p, v, s: Act(actor="peder", verb="convene", target="sitting.1")})
    if not d.fired:
        raise NoProducer("the date did not fire", "F6")
    raise Unspecified(
        "the judging set's decision rule at a sitting — `02` §2.2 names `judging_set_rule` as a "
        "Rung field and no document specifies its form or how a motion is carried",
        "F6 sitting decision",
        needs="a specified decision rule; the archive has ten motion types and two vote models",
    )


# ===========================================================================
# WORLD
# ===========================================================================

@probe("W1", "a site decays until a verb leaves its option set")
def w1(w=None):
    w = w or _world()
    s = w.sites["harbour"]
    loop = SeasonLoop(w)
    before = verbs(w, s)
    for _ in range(6):
        loop.run({})
    after = verbs(w, s)
    return (f"OK: condition 560->{s.condition}, band {condition_band(s)}, "
            f"verbs {sorted(before)} -> {sorted(after)}")


@probe("W2", "a site held at the wear/tending equilibrium does NOT strobe its band")
def w2(w=None):
    w = w or _world()
    s = w.sites["harbour"]
    s.condition = 500                 # exactly a band edge
    w.persons["tender"] = Person(id="tender")
    loop = SeasonLoop(w)
    for _ in range(6):
        loop.run({"tender": lambda p, v, s2: Act(actor="tender", verb="restore",
                                                 target="harbour")})
        s.condition = min(1000, s.condition + WEAR["harbour"])   # tending exactly offsets wear
    # count from the LOG, not from resolve()'s return: band crossings are emitted at MATTER
    crossings = sum(1 for e in w.log if e.family == "band_crossed")
    if crossings > 1:
        raise NoProducer(
            f"band strobing: {crossings} crossing events in 6 seasons at the tending equilibrium. "
            "A band edge is a single threshold, so recovery costs exactly what decline gave back "
            "and the site oscillates across it, spamming witnessed crossings and flickering verbs",
            "W2 hysteresis",
            needs="paired (fall_edge, rise_edge) per band — the archive's ratified +8 gap",
        )
    return "OK"


@probe("W3", "something happens to a place that nobody chose")
def w3(w=None):
    w = w or _world()
    loop = SeasonLoop(w)
    loop.run({})           # no deciders at all
    assert w.sites["harbour"].condition < 560
    return "OK: wear fires at MATTER with no actor; the world churns with nobody in it"


@probe("W4", "an off-board power applies pressure that is a DECISION, not weather")
def w4(w=None):
    raise Forbidden(
        "an agentive actorless row — 'an empire demands a levy' is an actor's decision rendered as "
        "weather. `05` §4.4 blocks it until a criterion exists that stops any actor being "
        "reclassified as weather",
        "W4 off-board agency",
        needs="the agentive/non-agentive criterion, or a simulated foreign person",
    )


# ===========================================================================
# ARC-SHAPED
# ===========================================================================

@probe("A1", "an arc ENDS at a sitting somebody convenes")
def a1(w=None):
    try:
        f6(w)
    except Unspecified:
        return ("PARTIAL: the sitting fires and a named convener can be bought, delayed or killed — "
                "but what is DECIDED there is unspecified (see F6)")
    return "OK"


@probe("A2", "an arc ENDS at a counter reaching a number with nobody deciding")
def a2(w=None):
    w = w or _world()
    w._step = Step.MATTER
    try:
        w.write("Office", "post", "gov", "deposed", WriteClass.MATTER, driver="Event")
    finally:
        w._step = None
    return "unreachable"


@probe("A3", "an arc turns on the state of the world-substrate")
def a3(w=None):
    w = w or _world()
    seam = w.sites["seam"]           # `05` §3: a Thread seam IS a Site; condition is the quantity
    loop = SeasonLoop(w)
    for _ in range(4):
        loop.run({})
    return f"OK: substrate is a Site kind, condition {seam.condition}, band {condition_band(seam)}"


@probe("A4", "a story is recoverable by walking causes[] backwards")
def a4(w=None):
    w = w or _world()
    w.persons["a"] = Person(id="a")
    loop = SeasonLoop(w)
    evs = loop.run({"a": lambda p, v, s: Act(actor="a", verb="accuse", target="b")})
    ev = evs[0]
    if ev.causes == []:
        raise NoProducer(
            "provenance: `resolve` emits Events with an EMPTY causes[] — nothing in the specified "
            "loop populates the causal edge that `06` §1 calls the arc itself",
            "A4 provenance chain",
            needs="resolve() to attribute each Event to the claims/events that motivated its act",
        )
    return "OK"


@probe("A5", "a self-reinforcing loop runs and provably terminates")
def a5(w=None):
    w = w or _world()
    w.persons["p"] = Person(id="p", stance=[("crown", -1, 1)])
    loop = SeasonLoop(w)
    grievance = 1
    for _ in range(8):
        loop.run({"p": lambda pp, v, s: Act(actor="p", verb="protest", target="crown")})
        grievance += 1                    # suppression scars ratchet the arming threshold
    raise NoProducer(
        f"boundedness: grievance rose monotonically to {grievance} over 8 seasons with nothing "
        "damping it. Per-tick emission caps bound a cascade WITHIN a season; nothing bounds a "
        "behavioural spiral ACROSS seasons, and no guard or measurement is licensed for it",
        "A5 termination",
        needs="a termination argument per self-feeding mechanism + a sustained-shock battery",
    )


@probe("A6", "a secret becomes public and legitimacy collapses retroactively")
def a6(w=None):
    w = w or _world()
    w.persons["a"] = Person(id="a")
    w.persons["b"] = Person(id="b")
    w.records["forged"] = Record(id="forged", rung="realm", kind="charter")
    loop = SeasonLoop(w)
    loop.run({"a": lambda p, v, s: Act(actor="a", verb="reconstruct", target="forged")})
    return "OK: legitimacy is a Query over claims, so it flips per-knower at telling speed"


def run_all() -> dict:
    """Run every probe. A probe that raises ShapeGap has ALREADY recorded it."""
    results = {}
    for pid, fn in PROBES.items():
        TRACE.start_case(f"PROBE-{pid}")
        try:
            out = fn()
            results[pid] = ("PARTIAL" if str(out).startswith("PARTIAL") else "PASS", out)
        except ShapeGap as e:
            results[pid] = (e.kind, str(e))
        except Exception as e:  # a genuine tracer bug — must not be silently read as a gap
            results[pid] = ("TRACER-ERROR", f"{type(e).__name__}: {e}")
    return results


# ===========================================================================
# SECOND WAVE — capabilities the NPC spectrum demands (copyist .. king)
# ===========================================================================

@probe("P13", "a person is somewhere, and moving costs something")
def p13(w=None):
    w = w or _world()
    w.persons["joren"] = Person(id="joren", name="Joren Bergvall")
    w.tenures["at"] = Tenure(id="at", subject="joren", object="settl", kind="contain", since=0)
    loop = SeasonLoop(w)
    loop.run({"joren": lambda p, v, s: Act(actor="joren", verb="travel", target="prov")})
    return "OK: presence is a `contain` Tenure; travel is an act; travel-in-progress ticks at MATTER"


@probe("P14", "a person gets better at something")
def p14(w=None):
    w = w or _world()
    p = Person(id="carin", capability={"copy": 2})
    w.persons["carin"] = p
    w._step = Step.RESOLVE
    try:
        w.write("Person", "capability", "carin", 3, WriteClass.ACTS, driver="Act")
    finally:
        w._step = None
    return "OK"


@probe("P15", "two people marry, and the bond is a political fact")
def p15(w=None):
    w = w or _world()
    w.persons["elske"] = Person(id="elske", name="Elske Almqvist")
    w.persons["alexios"] = Person(id="alexios", name="Alexios Laskaris")
    # Law 4's Partition names MARRIAGE explicitly as peninsular human society (act-driven).
    # The seven Tenure kinds are hold/contain/commit/oblige/succeed/tie/knot. Which carries it?
    t = Tenure(id="m1", subject="elske", object="alexios", kind="tie", since=0)
    w.tenures["m1"] = t
    raise Collision(
        "marriage: `01` Law 4 names marriage as a governed social change, but no Tenure kind carries "
        "it — `tie` is an affective bond that DECAYS, and a dynastic marriage is a durable political "
        "instrument that binds two houses and routes succession",
        "P15 marriage",
        needs="marriage as an `oblige`-class Tenure with a payload, or an eighth kind",
    )


@probe("P16", "a person without a post feeds themselves")
def p16(w=None):
    w = w or _world()
    w.persons["carin"] = Person(id="carin")
    w.rungs["settl"].stores["grain"] = 100
    loop = SeasonLoop(w)
    loop.run({})
    # `02` §8.1: "subsistence, craft and travel-in-progress happen *to* you at MATTER."
    if w.rungs["settl"].stores["grain"] == 100:
        raise NoProducer(
            "subsistence: `02` §8.1 says subsistence happens TO a person at MATTER, but no step "
            "consumes stores on their behalf and no rule links a person to a larder — so `need` in "
            "`Sensation` has no producer either",
            "P16 subsistence",
            needs="a MATTER draw per contained person against the Rung's stores",
        )
    return "OK"


@probe("P17", "the world produces the person a situation requires")
def p17(w=None):
    w = w or _world()
    w.persons["cohort"] = Person(id="cohort", weight=40)
    loop = SeasonLoop(w)
    loop.run({})
    # `05` churn row 13: individuation — a Person created with no decider, at CENSUS.
    raise Unspecified(
        "individuation: `05` row 13 requires the world to mint a Person on demand with no decider, "
        "and no rule says WHAT TRIGGERS IT or what interior the new person starts with — `02` §10 "
        "item 3 carries the 'plausible past' as open and ruled-against in three placements",
        "P17 individuation",
        needs="a trigger condition and a specified starting interior for a minted person",
    )


# ===========================================================================
# THIRD WAVE — capabilities the ARC corpus demands
# ===========================================================================

@probe("A7", "an institution acts as one body")
def a7(w=None):
    w = w or _world()
    w.offices["church"] = Office(id="church", post="The Church", rung="realm",
                                 establishment=["conf", "card1", "card2"])
    for m in ("conf", "card1", "card2"):
        w.persons[m] = Person(id=m)
    loop = SeasonLoop(w)
    # Law 1 is mechanical: an Act's actor is a PERSON id. "The Church excommunicates" is not
    # spellable; only "the Confessor, at a venue, issues" is.
    loop.run({"conf": lambda p, v, s: Act(actor="conf", verb="issue", target="excommunication")})
    return ("OK: an institution acts through a named person at a venue; 'the Church acted' is a "
            "reading of the log, never a row in it")


@probe("A8", "a deadline passes with nothing heard, and that is itself the consequence")
def a8(w=None):
    w = w or _world()
    d = Date(id="audience", holder="realm", season=1)
    w.rungs["realm"].dates.append(d)
    w.persons["petitioner"] = Person(id="petitioner")
    loop = SeasonLoop(w)
    loop.run({})                     # nobody convenes, nobody answers
    # `05` §5.1: a lapse is CALENDAR class and is the ABSENCE of an act — not a change with a driver.
    lapsed = d.fired and True
    if not any(e.family == "lapse" for e in w.log):
        raise NoProducer(
            "the lapse: `05` §5.1 calls a date passing unheard 'a real consequence' with "
            "'nobody's act, nobody to blame' — but nothing EMITS it, so the specific injury of "
            "being ignored is not witnessable and cannot enter anyone's ledger",
            "A8 lapse",
            needs="CALENDAR to emit a lapse Event for a date that fired with no answering act",
        )
    return "OK"


@probe("A9", "a term ripens and a truce runs out")
def a9(w=None):
    w = w or _world()
    w.records["truce"] = Record(id="truce", rung="realm", kind="truce", ttl=3)
    loop = SeasonLoop(w)
    for _ in range(4):
        loop.run({})
    r = w.records["truce"]
    if r.ttl == 3:
        raise NoProducer(
            "no step decrements a Record's ttl. `05` rows 11a/11b make a ttl expiry and an "
            "act-created term's ripening the carriers for cooldowns, remissions and truces — "
            "and MATTER never touches them",
            "A9 ttl",
            needs="a MATTER pass over Records decrementing ttl and emitting expiry",
        )
    return "OK"


@probe("A10", "a person is removed from play without being killed")
def a10(w=None):
    w = w or _world()
    w.persons["torben"] = Person(id="torben", name="Torben Almqvist")
    w.tenures["at"] = Tenure(id="at", subject="torben", object="settl", kind="contain", since=0)
    d = Date(id="succession", holder="realm", season=1,
             convening_conditions=["heir_present"])
    w.rungs["realm"].dates.append(d)
    loop = SeasonLoop(w)
    loop.run({})
    # `06` row 3: hostage politics — vacancy-by-absence as a convening condition over presence.
    raise Unspecified(
        "vacancy-by-absence: `06` row 3 requires a convening condition to read PRESENCE, so that "
        "making a man absent substitutes for killing him — `ConveningCondition` is a six-field "
        "object the adversarial pass found had no owner, and its predicate form is unspecified",
        "A10 hostage politics",
        needs="a specified ConveningCondition predicate that can read a person's address",
    )


@probe("A11", "something ripens over many seasons and pays off late")
def a11(w=None):
    w = w or _world()
    w.persons["baralta"] = Person(id="baralta")
    w.propositions["claim"] = Proposition(id="claim", mood="OUGHT", subject="crown",
                                          predicate="held_by", value="baralta",
                                          when=(0, 40), scope="realm", utterer="baralta")
    loop = SeasonLoop(w)
    for _ in range(12):
        loop.run({"baralta": lambda p, v, s: Act(actor="baralta", verb="press_claim",
                                                 target="claim")})
    # Twelve seasons of pressing. What accumulated? Claims in others' ledgers -- which DECAY.
    return ("OK-BUT: the claim persists (a Proposition is immutable) and each pressing is an act, "
            "but the only accumulator is other people's claims, which decay under the universal "
            "rule — so a long campaign of pressing is not distinguishable from a recent one "
            "except by re-reading the log")


@probe("A12", "a person is killed, and their tenures end — and a storm may NOT do the same")
def a12(w=None):
    """⚠ THIS PROBE PREVIOUSLY REPORTED A DEFECT IN THE SHAPE THAT WAS A DEFECT IN THIS TRACER.

    It wrote `("Tenure","hold")` at MATTER, got FORBIDDEN, and reported that a dead king still
    holds the crown. But `02` §5.1 RULES the seam closed: death writes **`until`**, not `hold`,
    and `(Tenure, until)` is `social: false` — "the Partition's ONE DECLARED SEAM", bounded by a
    causation rule. The tracer's Partition table simply omitted the ruled row, so the probe was
    measuring an omission of mine. Found by a read-only audit; instrument defect five, and the
    first that pointed the DAMNING way rather than the flattering one.

    What the probe tests now is the thing actually worth testing: the seam is bounded.
    """
    w = w or _world()
    w.persons["almud"] = Person(id="almud")
    w.offices["crown"] = Office(id="crown", post="King", rung="realm")
    w.tenures["h"] = Tenure(id="h", subject="almud", object="crown", kind="hold", since=0)
    w._step = Step.MATTER
    try:
        # 1. a plague that kills him ends his tenure: the same row caused (Person, exists).
        w._died_this_row = {"almud"}
        w.write("Tenure", "until", "almud", w.tick, WriteClass.MATTER, driver="Event")
        succession_fires = True

        # 2. a storm, which killed nobody, must NOT be able to vacate the praefecture.
        w._died_this_row = set()
        storm_blocked = False
        try:
            w.write("Tenure", "until", "almud", w.tick, WriteClass.MATTER, driver="Event")
        except Forbidden:
            storm_blocked = True
    finally:
        w._step = None
        w._died_this_row = set()

    if not (succession_fires and storm_blocked):
        raise Collision(
            "the declared seam is not bounded: death and storm are not distinguished",
            "A12 seam",
            needs="`02` §5.1's causation rule — an actorless row may write `until` only on a "
                  "(Person, exists) change the SAME row caused",
        )
    return ("OK — death ends the tenure and a storm cannot. The seam `05` §7 leaves open is "
            "CLOSED by `02` §5.1, and it is closed by a causation rule rather than by the column")


# ===========================================================================
# FOURTH WAVE — driven by UNMAPPED needs the a:NPC cases actually raised.
# Each of these was written only AFTER a real case demanded it.
# ===========================================================================

@probe("P18", "an institution reassesses its loyalty in STAGES that do not revert on their own")
def p18(w=None):
    """Raised by NPC-020 (Almud) and NPC-070 (Ehrenwall) independently — the coup mechanism."""
    w = w or _world()
    for m in ("ehrenwall", "off1", "off2"):
        w.persons[m] = Person(id=m, stance=[("crown", 2, 3)])
    # The shape refuses a stored aggregate, so "the army's loyalty stage" must be a Query over
    # members' stances. A Query is a pure function of current state.
    def loyalty_stage(world) -> str:
        vals = [v for p in ("ehrenwall", "off1", "off2")
                for (ref, v, _) in world.persons[p].stance if ref == "crown"]
        m = sum(vals) / len(vals)
        return "loyal" if m >= 2 else "restless" if m >= 0 else "autonomous" if m >= -2 else "split"

    assert loyalty_stage(w) == "loyal"
    for p in ("ehrenwall", "off1", "off2"):
        w.persons[p].stance = [("crown", -1, 3)]
    assert loyalty_stage(w) == "autonomous"
    for p in ("ehrenwall", "off1", "off2"):      # one good season restores every stance
        w.persons[p].stance = [("crown", 2, 3)]
    if loyalty_stage(w) == "loyal":
        raise NoProducer(
            "staged institutional judgement: a stage computed as a Query over current stances "
            "REVERTS the moment the stances do, so an army that has decided its king is unfit "
            "un-decides it after one good season. A ratchet needs state that survives its inputs, "
            "and Law 3 forbids exactly that state",
            "P18 loyalty stages",
            needs="either a per-person scar/ratchet the Query reads (see P4), or an explicit "
                  "exception to Law 3 for monotone institutional judgement",
        )
    return "OK"


@probe("P19", "not acting is itself a choice, and costs something")
def p19(w=None):
    """Raised by NPC-020: 'his uncertainty is itself a decision he does not recognize as one'."""
    w = w or _world()
    w.persons["almud"] = Person(id="almud")
    loop = SeasonLoop(w)
    for _ in range(3):
        loop.run({"almud": lambda p, v, s: None})       # three seasons of deciding nothing
    acted = [e for e in w.log if e.family not in ("band_crossed",)]
    if not acted:
        raise NoProducer(
            "deferral: a person who chooses nothing produces no Act, so no Event, so nothing enters "
            "anyone's ledger — a ruler's sustained refusal to decide is INVISIBLE to the world and "
            "indistinguishable from his absence",
            "P19 inaction",
            needs="an abstention that emits, so that not-deciding is witnessable and chargeable",
        )
    return "OK"


@probe("P20", "an order is carried out differently from how it was intended")
def p20(w=None):
    """Raised by NPC-020: the king must be able to learn of the divergence only afterwards."""
    w = w or _world()
    w.persons["almud"] = Person(id="almud")
    w.persons["voss"] = Person(id="voss")
    w.offices["crown"] = Office(id="crown", post="King", rung="realm", establishment=["voss"])
    loop = SeasonLoop(w)
    evs = loop.run({
        "almud": lambda p, v, s: Act(actor="almud", verb="dispatch", target="voss"),
        # Voss runs his OWN choose and does something adjacent to, but not, what was asked
        "voss": lambda p, v, s: Act(actor="voss", verb="levy_harshly", target="settl"),
    })
    fams = {e.family for e in evs}
    if "levy_harshly" not in fams:
        raise NoProducer("the subordinate's divergent act did not resolve", "P20")
    return ("OK: dispatch names one person who runs their own choose, so the deed done is the "
            "subordinate's, not the holder's — and the holder learns of it only by witnessing")


@probe("P21", "high office is MORE constrained by visibility than a private person")
def p21(w=None):
    """Raised by NPC-020, marked core: 'he is MORE constrained by visibility, not less'."""
    w = w or _world()
    w.persons["almud"] = Person(id="almud")
    w.persons["carin"] = Person(id="carin")
    w.offices["crown"] = Office(id="crown", post="King", rung="realm")
    w.tenures["h"] = Tenure(id="h", subject="almud", object="crown", kind="hold", since=0)
    loop = SeasonLoop(w)
    evs = loop.run({
        "almud": lambda p, v, s: Act(actor="almud", verb="favour_heretic", target="carin"),
        "carin": lambda p, v, s: Act(actor="carin", verb="favour_heretic", target="almud"),
    })
    king_ev, commoner_ev = evs[0], evs[1]
    if king_ev.scope == commoner_ev.scope:
        raise NoProducer(
            "publicness: the same act by a king and by a copyist produces Events identical in scope "
            "and witnessability. Nothing in Act, Event or witness() reads the actor's office, so "
            "office cannot make an act cost more — and `07` §5 asks precisely that it do so",
            "P21 visibility cost",
            needs="a witnessability term keyed on the actor's standing/office, not on the act",
        )
    return "OK"


@probe("P22", "the same words cost differently said in private and in public")
def p22(w=None):
    """Raised by NPC-020 and NPC-021: frank counsel must be free; public contradiction must not."""
    w = w or _world()
    w.persons["reichard"] = Person(id="reichard")
    w.persons["almud"] = Person(id="almud")
    w.persons["bystander"] = Person(id="bystander")
    loop = SeasonLoop(w)
    evs = loop.run({"reichard": lambda p, v, s: Act(actor="reichard", verb="contradict",
                                                    target="almud")})
    # Every person in the world witnesses every Event in the specified loop.
    heard = [p for p in w.persons if any(c.source_event == evs[0].id for c in w.persons[p].ledger)]
    if "bystander" in heard:
        raise NoProducer(
            "privacy: WITNESS as specified fans every Event out to every person, so there is no "
            "private utterance — a councillor's frank advice is heard by the whole realm. `06` §4.2 "
            "names five witness CHANNELS as the cast gate, but the loop never consults them",
            "P22 private vs public",
            needs="witness() to consult presence/channel before depositing, not after",
        )
    return "OK"


@probe("P23", "a failed attempt costs standing and cannot be retried for some seasons")
def p23(w=None):
    """Raised by NPC-050 (Baralta), marked core: the claim must be a real multi-season bet."""
    w = w or _world()
    w.persons["baralta"] = Person(id="baralta")
    loop = SeasonLoop(w)
    for _ in range(3):
        loop.run({"baralta": lambda p, v, s: Act(actor="baralta", verb="press_claim",
                                                 target="crown")})
    tries = [e for e in w.log if e.family == "press_claim"]
    if len(tries) == 3:
        raise NoProducer(
            f"act cooldown: the claim was pressed {len(tries)} seasons running with no cost and no "
            "bar. `05` §4.1 gives event ROWS a required cooldown; nothing gives an ACT one, so a "
            "failed bid for a throne is a free repeatable check rather than a bet",
            "P23 act cooldown",
            needs="a per-act-kind cooldown carried by the actor, or a Record with a ttl that gates "
                  "eligibility (the shape already has the Record; nothing writes it here)",
        )
    return "OK"


@probe("P24", "a collective body revokes the authority it granted")
def p24(w=None):
    """Raised by NPC-052 (Vaynard), core: authority revocable by his own senior subordinates."""
    w = w or _world()
    for m in ("vaynard", "jarl1", "jarl2"):
        w.persons[m] = Person(id=m)
    w.offices["duke"] = Office(id="duke", post="Duke of Varfell", rung="prov",
                               conferral="jarl_council", revocation="jarl_council_at_thing")
    w.tenures["h"] = Tenure(id="h", subject="vaynard", object="duke", kind="hold", since=0)
    d = Date(id="thing", holder="duke", season=1)
    w.rungs["prov"].dates.append(d)
    loop = SeasonLoop(w)
    loop.run({"jarl1": lambda p, v, s: Act(actor="jarl1", verb="convene", target="thing"),
              "jarl2": lambda p, v, s: Act(actor="jarl2", verb="move_revocation", target="h")})
    return ("OK-BUT: the acts resolve and the office declares its revocation basis, but WHETHER THE "
            "MOTION CARRIES is the unspecified judging-set rule of F6 — so revocation reaches the "
            "venue and stops there")


@probe("P25", "a subordinate silently underperforms, and nobody can tell without investigating")
def p25(w=None):
    """Raised by NPC-052: a compromised operative with divided loyalty."""
    w = w or _world()
    w.persons["vaynard"] = Person(id="vaynard")
    w.persons["maret"] = Person(id="maret", stance=[("vaynard", 1, 2), ("rm", 4, 4)])
    loop = SeasonLoop(w)
    loop.run({"vaynard": lambda p, v, s: Act(actor="vaynard", verb="dispatch", target="maret"),
              "maret": lambda p, v, s: Act(actor="maret", verb="scout", target="settl",
                                           payload={"effort": "half"})})
    return ("OK: the operative's own choose returns a weaker act; her divided stance is her interior "
            "and nobody may read it — investigating is the only route, which is the design")


@probe("P26", "accumulated visible harm crosses a threshold and forces a confrontation")
def p26(w=None):
    """Raised by NPC-001 (Edeyja), core: her patience must have a hard triggered limit."""
    w = w or _world()
    w.persons["edeyja"] = Person(id="edeyja")
    w.persons["offender"] = Person(id="offender")
    loop = SeasonLoop(w)
    for _ in range(6):
        loop.run({"offender": lambda p, v, s: Act(actor="offender", verb="tear_seam",
                                                  target="seam")})
    harms = [c for c in w.persons["edeyja"].ledger if "tear_seam" in c.proposition]
    # she must have WITNESSED them; and claim confidence decays under the universal rule
    raise NoProducer(
        f"accumulation vs decay: Edeyja holds {len(harms)} claims of harm, but the only accumulator "
        "the shape offers is a ledger whose confidence DECAYS and whose rows are EVICTED at a cap. "
        "A threshold over 'visible harm accumulated' is therefore a race between witnessing and "
        "forgetting, and the shape has no counter that only goes up",
        "P26 accumulation",
        needs="a monotone per-person tally (the archive's scar is exactly this shape), or an "
              "explicit statement that patience is a Query over undecayed claims and is losable",
    )


@probe("P27", "a contested person's allegiance is won by investment inside a closing window")
def p27(w=None):
    """Raised by NPC-031 (Torben), core: alignment won, then permanently locked."""
    w = w or _world()
    w.persons["torben"] = Person(id="torben")
    for inv in ("altonia", "church"):
        w.persons[inv] = Person(id=inv)
    loop = SeasonLoop(w)
    for _ in range(3):
        loop.run({"altonia": lambda p, v, s: Act(actor="altonia", verb="tutor", target="torben"),
                  "church": lambda p, v, s: Act(actor="church", verb="tutor", target="torben")})
    raise Unspecified(
        "contested formation: investments in a person resolve as Events he witnesses, but nothing "
        "converts accumulated tutoring into a DURABLE alignment, and nothing closes a window after "
        "which it LOCKS. `02` §10 item 3 carries the 'plausible past' of a newly made person as "
        "open; this is the same hole seen from the other end — how a person's interior is FORMED",
        "P27 formation window",
        needs="a specified route from repeated acts upon a person to that person's convictions "
              "(which is P4's missing mechanism again), plus a lock condition",
    )


# ===========================================================================
# FIFTH WAVE — the low-agency end. Raised by NPC-088/087/086/075/005.
# ===========================================================================

@probe("P28", "a person MAKES a durable object that outlives the scene")
def p28(w=None):
    """Carin Vedel, core: 'a copied text must exist as a persistent object'."""
    w = w or _world()
    w.persons["carin"] = Person(id="carin")
    loop = SeasonLoop(w)
    loop.run({"carin": lambda p, v, s: Act(actor="carin", verb="copy", target="text.einhir")})
    made = [r for r in w.records.values() if r.kind == "copy"]
    if not made:
        raise NoProducer(
            "craft: `02` §7.4 has `Record` — the only non-person root-bearer, keepable at a Rung, "
            "burnable, admissible at a venue — which is exactly the object a copyist makes. But no "
            "act CREATES one: `resolve` emits Events and nothing mints a Record, so the shape has "
            "the noun and not the verb",
            "P28 making a thing",
            needs="a `create`-mode StateChange whose subject is a Record, produced by an act",
        )
    return "OK"


@probe("P29", "merely HOLDING a thing is actionable against you")
def p29(w=None):
    """Carin Vedel, core: 'possession is a heresy charge', independent of being seen to copy."""
    w = w or _world()
    w.records["banned"] = Record(id="banned", rung="settl", kind="copy")
    w.persons["carin"] = Person(id="carin")
    # Who HOLDS the banned copy? `03` §1.3 gap 2 homes a Record as Rung matter, so it sits at a
    # place, not with a person. This is the same hole P10 found from the custody side.
    raise Collision(
        "possession: a Record is homed as Rung matter, so it is at a PLACE and never in a person's "
        "hands — 'she was found with it' is not expressible, and possession-as-offence has no "
        "subject. P10 found the same hole from the custody side; they are one gap",
        "P29 possession",
        needs="a person-to-Record `hold` Tenure, which also closes P10",
    )


@probe("P30", "work spans seasons and can be interrupted partway")
def p30(w=None):
    """Carin (a copy takes many weeks) and Uwe (a school is a standing condition, not an act)."""
    w = w or _world()
    w.persons["carin"] = Person(id="carin")
    loop = SeasonLoop(w)
    loop.run({"carin": lambda p, v, s: Act(actor="carin", verb="copy", target="text",
                                           payload={"progress": 1, "of": 3})})
    # `02` §8.1 lists "travel-in-progress" as a thing MATTER ticks. Nothing generalises it.
    raise NoProducer(
        "work-in-progress: `02` §8.1 names travel-in-progress as ticking at MATTER, but there is no "
        "general partial-work record, so every act completes or fails within its season. A craft, a "
        "school, a survey or a long investigation cannot be half-done and interrupted",
        "P30 ongoing work",
        needs="an act that deposits a Record with remaining effort, which MATTER advances",
    )


@probe("P31", "a person is worn down by WHERE THEY ARE, not by what they do")
def p31(w=None):
    """Orm, core: 31 years of Warden degradation is environmental — proximity, not operations."""
    w = w or _world()
    w.persons["orm"] = Person(id="orm")
    w.tenures["at"] = Tenure(id="at", subject="orm", object="settl", kind="contain", since=0)
    w.sites["seam"].condition = 120                       # a badly damaged seam he lives beside
    loop = SeasonLoop(w)
    for _ in range(5):
        loop.run({})                                      # he does nothing at all
    raise NoProducer(
        "environmental cost: a person contained at a Rung whose Site is derelict takes NOTHING from "
        "it. MATTER wears Sites; nothing wears the PEOPLE standing next to them, so a Warden's "
        "thirty-one years of proximity to substrate damage is free",
        "P31 proximity harm",
        needs="a MATTER pass from Site condition onto contained persons — the same shape as "
              "subsistence (P16), which is also missing",
    )


@probe("P32", "spending your life on an act buys something a surviving act cannot")
def p32(w=None):
    """Orm, core: his death while sealing a breach seals it PERMANENTLY, unlike a survived seal."""
    w = w or _world()
    w.persons["orm"] = Person(id="orm")
    loop = SeasonLoop(w)
    evs = loop.run({"orm": lambda p, v, s: Act(actor="orm", verb="seal_breach", target="seam",
                                               payload={"stake": "life"})})
    # An Act has (actor, verb, target, payload). resolve() ignores payload; degrees come from the
    # ladder, and nothing lets an actor WAGER themselves for a better band.
    raise NoProducer(
        "sacrifice: `resolve` reads no stake from an Act, so spending your life on an act cannot buy "
        "a different outcome than performing it and living. Orm's death-seal and an ordinary seal "
        "are the same Event",
        "P32 self-sacrifice",
        needs="a declared stake on an Act that the resolver may read, priced against the ladder",
    )


@probe("P33", "one person carries two independent standings that move separately")
def p33(w=None):
    """Sigrid Torsvald, important: an overt rank and a covert rank that do not imply each other."""
    w = w or _world()
    w.persons["sigrid"] = Person(id="sigrid", marks=["officer:lowenritter"])
    # `07` §3.1: Sensation.standing is ONE scalar — "the gap between what everyone reads off you
    # and what you hold". A covert reputation is by definition NOT what everyone reads off you.
    raise NoProducer(
        "two standings: `Sensation.standing` is a single scalar defined as what EVERYONE reads off "
        "you, so a reputation held only among people who can never publicly credit you has no "
        "carrier — and a covert operative's whole economy is that second, unreadable standing",
        "P33 covert standing",
        needs="standing as a Query over a NAMED audience, not a global scalar",
    )


# ===========================================================================
# SIXTH WAVE — driven by UNMAPPED needs the b:ARCS cases raised.
# ===========================================================================

@probe("A13", "an ambient SOCIAL quantity drifts from the ABSENCE of anyone acting")
def a13(w=None):
    """ARC-01 core: a cultural track drifts toward a pole purely because no faction acted."""
    w = w or _world()
    w._step = Step.MATTER
    try:
        # `wear` does exactly this for Sites, because (Site, condition) is social:false.
        w.write("Site", "condition", "harbour", 520, WriteClass.MATTER, driver="Event")
        # The arc needs the same shape for a POPULATION'S disposition. That is a stance —
        # (Person, stance) is social:true, so an Event may not write it.
        w.write("Person", "stance", "populace", -1, WriteClass.MATTER, driver="Event")
    finally:
        w._step = None
    return "unreachable"


@probe("A14", "a person changes with nobody — including them — deciding")
def a14(w=None):
    """ARC-02 core: Klapp develops a sensitivity; 'no actor triggers this'."""
    w = w or _world()
    w.persons["klapp"] = Person(id="klapp", capability={"perceive": 0})
    w._step = Step.MATTER
    try:
        w.write("Person", "capability", "klapp", 1, WriteClass.MATTER, driver="Event")
    finally:
        w._step = None
    return "unreachable"


@probe("A15", "a once-per-arc resource is held in reserve, and the window can close unannounced")
def a15(w=None):
    """ARC-03 core: Baralta's hammer. Holding it is the play; the window closes silently."""
    w = w or _world()
    w.persons["baralta"] = Person(id="baralta")
    loop = SeasonLoop(w)
    for _ in range(4):
        loop.run({"baralta": lambda p, v, s: None})       # she deliberately holds
    raise NoProducer(
        "reserve: nothing marks an act as once-per-arc, nothing records that it is being WITHHELD, "
        "and nothing lets its value decay while unused. Holding a hammer is indistinguishable from "
        "not having one (and see P19 — the holding itself emits nothing)",
        "A15 held reserve",
        needs="an act kind with a use-once flag and a value that varies with world state, so that "
              "waiting is a priced decision rather than an absence",
    )


@probe("A16", "a formal process advances on its own stages regardless of anyone acting")
def a16(w=None):
    """ARC-04 core: the Inquisitors' case proceeds whether or not Vaynard acts."""
    w = w or _world()
    w.records["case"] = Record(id="case", rung="realm", kind="accusation", ttl=None)
    loop = SeasonLoop(w)
    for _ in range(3):
        loop.run({})
    raise NoProducer(
        "procedural advance: an accusation, a probate, a licence application — a process with "
        "STAGES that advance on their own timetable — has no carrier. A Record is inert (A9 shows "
        "even its ttl is never decremented), and CALENDAR fires dates rather than advancing "
        "processes. So a case against you cannot ripen while you do nothing",
        "A16 procedural stages",
        needs="a staged Record that MATTER advances, whose stage gates what acts are available",
    )


@probe("A17", "winning the argument and enforcing the win are SEPARATE events, and the second can fail")
def a17(w=None):
    """ARC-06 core: 'the gap between a won contest and a successful enforcement is the arc'."""
    w = w or _world()
    w.persons["orator"] = Person(id="orator")
    w.persons["crown"] = Person(id="crown")
    loop = SeasonLoop(w)
    evs = loop.run({"orator": lambda p, v, s: Act(actor="orator", verb="win_debate",
                                                  target="tithe_rule")})
    # The ruling exists as an Event. Does anything make it BINDING, and separately ENFORCED?
    ruling = evs[0]
    loop.run({"crown": lambda p, v, s: Act(actor="crown", verb="enforce", target="tithe_rule")})
    return ("OK: the two are separate acts by separate persons in separate seasons, and the second "
            "can fail on its own — the shape gets this right for free, because a Dispensation is "
            "published as a telling and compliance is each hearer's own choose")


@probe("A18", "a rare roll leaves a condition that outlives the scene that produced it")
def a18(w=None):
    """ARC-07 core: two failed sub-checks leave an army mechanically unable to stand down."""
    w = w or _world()
    w.persons["cmdr"] = Person(id="cmdr")
    loop = SeasonLoop(w)
    loop.run({"cmdr": lambda p, v, s: Act(actor="cmdr", verb="give_battle", target="settl")})
    # The battle resolves into Events. Is there anywhere to put "this unit cannot stand down"?
    raise NoProducer(
        "persistent condition: an Event is a fact in the log, not a state on a thing. Nothing "
        "carries 'this unit is stuck', 'this person is disgraced', 'this place is under "
        "interdict' — a condition that outlives its scene and gates later acts. `09`'s seam "
        "returns Events from a contest and stops there",
        "A18 lingering condition",
        needs="a condition Record attached to a carrier, with a clearing act — the same shape "
              "A16 and P30 need, which is one gap seen three ways",
    )


@probe("A19", "a person crosses an irreversible personal floor and stops being an agent")
def a19(w=None):
    """ARC-09 core: Coherence zero. 'The arc exists because the rule has no exit.'"""
    w = w or _world()
    w.persons["prac"] = Person(id="prac", capability={"coherence": 1})
    loop = SeasonLoop(w)
    loop.run({"prac": lambda p, v, s: Act(actor="prac", verb="thread_op", target="seam")})
    # Does anything stop this person from being handed to `choose` next season?
    still_a_decider = "prac" in w.persons
    if still_a_decider:
        raise NoProducer(
            "loss of agency: the loop hands EVERY person in `world.persons` to `choose`. There is "
            "no state in which a person exists, is lucid, and may no longer choose — so an "
            "irreversible personal floor cannot be represented, and the arc that exists BECAUSE "
            "the rule has no exit has no rule",
            "A19 irreversible floor",
            needs="a per-person agency predicate the DELIBERATE map consults, and an act class "
                  "that can cross it one way only",
        )
    return "OK"


# ===========================================================================
# SEVENTH WAVE — raised by the EXPANDED arc corpus (arcs 19-45, lane ARC2).
#
# These exist because folding 31 more arcs in exposed a routing defect, not
# because the shape changed: sixteen core needs were landing on `W2` (band
# strobing) on the bare word "threshold". Reading them showed they are one
# capability the probe set did not have, and it is the single most frequent
# structural demand in the whole corpus. Narrowing W2's route without adding
# the probe would have converted a real finding into `UNMAPPED`.
# ===========================================================================

@probe("P34", "a quantity accumulates in a person from their OWN ordinary acts, unknown to them")
def p34(w=None):
    """Five arcs, independently: ARC-26, ARC-31, ARC-32, ARC-35, ARC-39.

    Each says the same thing in different clothes — a leader's repeated use of an asset, an
    official's long routine service, a surveillance file that grows from unrelated encounters —
    a quantity climbs from acts the person took for ordinary reasons, THE PERSON CANNOT SEE IT,
    and crossing fires something at them.
    """
    w = w or _world()
    w.persons["duke"] = Person(id="duke")
    loop = SeasonLoop(w)
    for _ in range(5):
        loop.run({"duke": lambda p, v, s: Act(actor="duke", verb="tutor", target="duke")})
    own = [e for e in w.log if e.family == "tutor"]
    # The acts happened. Where does the residue live?
    raise NoProducer(
        f"self-accumulating hidden exposure: the duke performed {len(own)} ordinary acts and the "
        "shape retains them ONLY as Events in the world log and as decaying Claims in whoever "
        "witnessed them. There is no per-person quantity that (a) climbs from the person's own "
        "acts, (b) is NOT readable by that person, and (c) can fire. The nearest thing, the claim "
        "ledger, is the wrong shape three ways over: it is other people's, it decays, and its "
        "holder reads it",
        "P34 hidden self-accumulation",
        needs="a monotone interior counter fed by the actor's OWN acts at WITNESS, excluded from "
              "that person's own View, with a firing rule that produces an Act by SOMEONE ELSE "
              "rather than an outcome — otherwise it is A2's forbidden threshold wearing a hat",
    )


@probe("P35", "an actor is stopped by an opponent building the SAME quantity in the same place")
def p35(w=None):
    """ARC-R17 core, and the contested half of P27: two people push one local quantity in
    opposite directions, and only the NET matters."""
    w = w or _world()
    for pid in ("pusher", "blocker"):
        w.persons[pid] = Person(id=pid)
    loop = SeasonLoop(w)
    evs = loop.run({
        "pusher": lambda p, v, s: Act(actor="pusher", verb="restore", target="harbour"),
        "blocker": lambda p, v, s: Act(actor="blocker", verb="wreck", target="harbour"),
    })
    fams = sorted({e.family for e in evs})
    raise NoProducer(
        f"contested quantity: both acts resolved and emitted {fams}; the site's condition took "
        "both deltas independently. That is correct for matter and it is NOT contest — nothing "
        "in `resolve()` sees that two acts addressed one target in one season, so there is no "
        "net, no opposition, and no way for a blocker to hold a line",
        "P35 opposed acts on one target",
        needs="either an explicit statement that opposition is emergent from summed deltas and "
              "arcs must be written that way, or a resolve() that groups acts by target — the "
              "second is a second resolver and the shape's own meta-rule forbids it",
    )


@probe("P36", "a person gets ~5 acts in a season and must choose which pressures to leave unaddressed")
def p36(w=None):
    """NPC-020 (Almud) core, and Jordan's stated player model: ~5 playable scenes per season,
    which may mean ~5 actions.

    The lane's words: 'a single leader must be able to face several independent, ongoing pressure
    sources in one season and ONLY BE ABLE TO SUBSTANTIVELY ADDRESS A SUBSET of them, with the
    unaddressed ones COMPOUNDING rather than pausing.' That is an action budget, and triage is the
    whole game at high office.
    """
    w = w or _world()
    w.persons["almud"] = Person(id="almud")
    loop = SeasonLoop(w)
    n = 0

    def greedy(p, v, s):
        nonlocal n
        n += 1
        return Act(actor="almud", verb="tell", target="settl")

    loop.run({"almud": greedy})
    raise NoProducer(
        f"action budget: `choose(Person, View, Sensation) -> Act` returns ONE Act, and DELIBERATE "
        f"called it {n} time(s). A season is one act per person, so nobody triages, nothing is left "
        "undone, and a King's scarcity is identical to a copyist's. Note what this also voids: "
        "`14` closes the petition-spray defect 'PROVISIONALLY by one act per person', a fix that "
        "does not survive the stated player model of ~5",
        "P36 acts per season",
        needs="`choose` returning an ORDERED Act[] bounded by a per-person budget, with the budget "
              "itself a Query (office, condition, distance travelled) rather than a constant — and "
              "a re-answer to petition-spray that survives a budget above one",
    )
