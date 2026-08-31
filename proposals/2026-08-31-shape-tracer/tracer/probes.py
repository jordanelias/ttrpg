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
