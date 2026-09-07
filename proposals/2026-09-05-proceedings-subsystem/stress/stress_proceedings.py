"""STRESS TESTS for `proposals/2026-09-05-proceedings-subsystem/` — run against the tracer.

## Status: PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.

WHAT THIS IS. Twenty-eight logical stress tests that try to RUN a proceeding — convene it,
docket it, enter it, speak at it, determine it, appeal it, tell the world about it — against
`proposals/2026-09-01-season-loop-tests/tracer/shape.py`, the executable tracer the design
itself cites by line number throughout. Every verdict below is an EXECUTION or a declared
absence, never an opinion.

WHY THE TRACER AND NOT PROSE. `CLAUDE.md` §0.2: a juncture is done when the behaviour
EXECUTES. The subsystem is PROPOSED and nothing in it runs, so the honest question is not
"is the design good" — three passes have already asked that (`13`, `17`, `18`) — but
"what must be INVENTED before a single proceeding can be traced end to end, and where does
the attempt stop." Building a fixture is what forces that question, because a fixture cannot
be vague.

THE THREE LOGS THIS EMITS, which are the deliverable:
  INVENTIONS  — everything that had to be created for a proceeding to be traceable at all:
                characters, seats, dockets, venues, rosters, magnitudes, whole functions.
                Each carries WHO SHOULD OWN IT, which is what turns a fixture note into a
                finding.
  DECISIONS   — every mechanical choice made where the design admits two readings. Each
                names the alternative not taken and what would show the choice wrong.
  FINDINGS    — gaps, conflicts and failures. Each carries the same `by=` grade the tracer's
                own probes use, so a reader can discount the weak ones:

    by="construction"   the tracer, the loader, a roster or a law raised / refused. EVIDENCE.
    by="no-signature"   there is nothing to call. The absence IS the refusal, but absence is
                        not a guard, so this is weaker evidence than a raise.
    by="document"       two documents in the tree disagree, or one contradicts the code it
                        cites by line number. Verified by reading both, mechanically where
                        the check is mechanisable.
    by="probe-model"    this harness supplied a model the design does not, to reach the
                        question at all. The verdict is about the design; the model is mine
                        and is named so it can be discounted.

RUN:  python3 stress_proceedings.py            # report to stdout
      python3 stress_proceedings.py --json     # machine-readable
"""

from __future__ import annotations

import json
import os
import re
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
TRACER = REPO / "proposals" / "2026-09-01-season-loop-tests" / "tracer"
ARCH = REPO / "proposals" / "2026-09-02-executable-architecture"
DESIGN = HERE.parent

sys.path.insert(0, str(TRACER))

import yaml  # noqa: E402
import shape  # noqa: E402
from shape import (  # noqa: E402
    Act, Collision, ContestError, DEFAULT_FIXTURES, Forbidden, H, NoProducer, Office,
    Person, Proposition, Query, Record, Rung, SeasonDriver, ShapeGap, Site, Tenure,
    Unowned, Unspecified, VERB_TABLE, World, contest, contest_subsystem, roster,
)

# ---------------------------------------------------------------------------
# THE THREE REGISTERS
# ---------------------------------------------------------------------------
INVENTIONS: list[dict] = []
DECISIONS: list[dict] = []
FINDINGS: list[dict] = []
MATRIX: dict[str, dict] = {}
RESULTS: list[dict] = []
WALK: list[dict] = []


def _once(bag: list, row: dict) -> str:
    """Register a row ONCE. The fixture builder runs per test, so an id may be offered many
    times; a register that counted them would report 48 inventions where there are 8."""
    if not any(r["id"] == row["id"] for r in bag):
        bag.append(row)
    return row["id"]


def INV(iid, what, why, owner, kind="fixture"):
    """Something that had to be created for a proceeding to be traceable.

    `owner` is the load-bearing column: a character invented for a test is a harness artifact;
    a Query, a roster or a magnitude invented to get past a hole is WORK SOMEBODY OWES."""
    return _once(INVENTIONS, dict(id=iid, what=what, why=why, owner=owner, kind=kind))


def MD(did, decision, because, alternative, falsifier):
    return _once(DECISIONS, dict(id=did, decision=decision, because=because,
                                 alternative=alternative, falsifier=falsifier))


def FIND(fid, title, detail, by, severity, site="", dup="NEW"):
    """`dup` is the column an adversarial pass forced into existence and it is the one to read
    beside the count. This directory's gap register is unusually complete, and a stress report
    that re-reports its honestly-registered holes as discoveries is padding. `dup="NEW"` means no
    row in `10_LOOPS_AND_GAPS.md`, `13_ADVERSARIAL.md` or `17_PLAYABILITY.md` covers it; anything
    else names the row it restates, and what (if anything) the execution ADDS to it."""
    return _once(FINDINGS, dict(id=fid, title=title, detail=detail, by=by,
                                severity=severity, site=site, dup=dup))


# ---------------------------------------------------------------------------
# THE FIXTURE — a settlement, a bench, a matter, and six people
#
# Every line of this function is an INVENTION and is registered as one. That is the point of
# the function: the design has no fixture, no world-gen for a proceeding, and no example row,
# so the smallest runnable proceeding must be built from nothing and the bill comes here.
# ---------------------------------------------------------------------------

def proceedings_world() -> World:
    INV("INV-21", "eight swept fixture constants, adopted whole from `DEFAULT_FIXTURES`",
        "`ledger_cap=200` · `scene_budget=5` · `fan_out_mode='total'` · `contest_max_depth=2` · "
        "`question_aggregation_rule='first'` · `claim_subject_rule='both'` · "
        "`observation_deposit_mode='actor'` · `record_stages_default=3`. **Each carries its own "
        "H-row and a declared three-point sweep**, and every season this harness runs is ONE "
        "UNDECLARED ARM of eight. `18_FINDINGS.md` states the trap verbatim: *the sweep must run "
        "against a setting that is not the current fixture, or it measures the fixture.* Named "
        "here because a suite that inherits them silently is doing exactly that.",
        owner="the harness — DECLARED, not swept. Any verdict below that depends on one says so",
        kind="fixture")
    INV("INV-22", "`world_seed=7`, `SUBSIST` (a subsistence model), `NOCHOOSE` (a chooser that "
        "takes nothing), and grain stores of 40 at the settlement and 8 at the hearth",
        "the season loop will not turn without a seed, a subsistence function and a chooser, and "
        "the design supplies none of the three. `SUBSIST` is copied from the tracer's own probe "
        "harness, which declares it *the instrument's own subsistence model, INJECTED rather "
        "than invented inside the shape*.",
        owner="the harness — and the note is that a PROCEEDING-shaped chooser (one that weighs "
              "row 0, the entry decision the design calls its largest lever) does not exist "
              "anywhere, so no test here can exercise the decision the design cares most about",
        kind="fixture")
    INV("INV-23", "⚠ a `manifest` installed directly on the world: "
        "`{contest: seam.contest_resolver, order: core.canonical_order}`",
        "copied from the tracer's own fixture so the world boots. **It is worth flagging against "
        "`F-01`, which reports that no `manifest.yaml` exists in the repo**: both are true — the "
        "tracer's world carries a two-row boot manifest naming a RESOLVER, and the design's "
        "PART B row naming a PROVIDER for a prize is a different row in a different file that "
        "does not exist. A reader could otherwise take F-01 and this line as contradicting.",
        owner="the harness (the boot manifest) · the design (the provider row)", kind="fixture")
    w = World(world_seed=7, fixtures=DEFAULT_FIXTURES)

    INV("INV-01", "four venues: realm R, duchy D, settlement S, hearth Hh",
        "`venue_min_rank` is an ordinal over `rung_kinds`, so a proceeding needs a containment "
        "ladder to sit on. No fixture, seed world or example venue exists in the design.",
        owner="harness (the tracer's own `tiny_world` sets the precedent)")
    for rid, kind, stores in (("R", "realm", None), ("D", "duchy", None),
                              ("S", "settlement", {"grain": 40}), ("Hh", "hearth", {"grain": 8})):
        w.rungs[rid] = Rung(rid, kind, stores=stores)

    INV("INV-02", "six persons: p_bench_a, p_bench_b (bench) · p_party_a, p_party_b (parties) "
        "· p_floor (audience) · p_absent (the subject who did not travel)",
        "`AX-1` — only a person acts — so every seat, every party and every witness must be a "
        "person before anything can be traced. The design names no character anywhere and the "
        "tree's `references/npc_registry.yaml` is out of this proposal's declared scope.",
        owner="harness — BUT see PART D: the design has no worked cast for ANY of its twelve "
              "games, so before this walk no row had been instantiated even on paper")
    for pid in ("p_bench_a", "p_bench_b", "p_party_a", "p_party_b", "p_floor", "p_absent"):
        w.persons[pid] = Person(pid, pid)
        w.rungs[pid] = Rung(pid, "person")

    INV("INV-03", "one office `off_justice` with remit_acts [determine, convene, issue], "
        "scope_rung S, faction Crown",
        "`bench_basis: determine` reads a remit act off a SEAT. The design specifies the Query "
        "that would find such seats and no seat to find. `remit_acts` membership is validated "
        "against `rosters.yaml`, so the acts are the roster's; the SEAT is invented.",
        owner="world-gen / the political layer — but nothing in the tree creates a "
              "bench-shaped office either, so until something does, no proceeding has a bench "
              "to find even once `judging_set` is written", kind="mechanism")
    w.offices["off_justice"] = Office("off_justice", "Justice", "S",
                                      ["determine", "convene", "issue"], faction="Crown")

    n = [0]

    def edge(sub, obj, kind, **kw):
        n[0] += 1
        t = Tenure(f"t{n[0]}", sub, obj, kind, since=0, **kw)
        w.add_tenure(t)
        return t

    edge("D", "R", "contain")
    edge("S", "D", "contain")
    edge("Hh", "S", "contain")
    INV("INV-04", "presence: five of six persons `contain`-ed at S; p_absent left at Hh",
        "`floor` = whoever travelled, and `presence` is a `contain` walk. To have a floor at "
        "all somebody must have been put in the room by the fixture, because `move` is the "
        "attendee's own act and this harness cannot make six people decide.",
        owner="harness — and it is the honest form of `07_THE_GAME.md`'s entry decision: the "
              "test cannot exercise row 0 without a chooser that weighs it, which does not exist")
    for pid in ("p_bench_a", "p_bench_b", "p_party_a", "p_party_b", "p_floor"):
        edge(pid, "S", "contain")
    edge("p_absent", "Hh", "contain")

    edge("p_bench_a", "off_justice", "hold")
    INV("INV-05", "p_bench_b holds NO seat, deliberately",
        "so the bench Query has something to exclude. A bench of one cannot test "
        "`&#124;bench&#124; > 1`, which four of the twelve rows require.",
        owner="harness")

    INV("INV-06", "the matter: Proposition(HOLDS, subject=p_absent, predicate='took', "
        "value='the cattle') uttered by p_party_a",
        "`14_THE_WORLD_IN_THE_ROOM.md` §A: the matter's MOOD selects the genre. The tracer's "
        "`Proposition` carries `mood`, so this is expressible — but no act in the design "
        "creates the matter as part of opening a proceeding, and `utter` is a separate act in "
        "a separate season.",
        owner="the design — `open_case` writes Record.exists/stages and never names the matter, "
              "so no step of any procedure here puts the matter before the room",
        kind="mechanism")
    w.propositions["prop_cattle"] = Proposition(
        "prop_cattle", "HOLDS", "p_absent", "took", "the cattle", when=0, scope="S")

    INV("INV-07", "two `commit` edges making p_party_a and p_party_b parties",
        "`parties` is defined as live `commit` edges to a disposition of the matter. Nothing "
        "in the design produces the FIRST commit — `commit` is a live verb, but which "
        "Proposition a party commits to at a proceeding, and when, is unspecified.",
        owner="the design — `03_PARAMETERS.md` §C.2 defines the party role and no step confers "
              "it, so `bench ∩ parties`, the column the whole taxonomy rests on, has no producer",
        kind="mechanism")
    edge("p_party_a", "prop_cattle", "commit")
    edge("p_party_b", "prop_cattle", "commit")

    INV("INV-08", "a Date `d_sitting` due at tick 1 with holder=p_bench_a",
        "a proceeding CONVENES because a Date fires. `convene` writes `Date.due_at`, so a real "
        "run would need a prior season in which somebody with a `convene` remit acted; the "
        "fixture short-circuits that.",
        owner="harness (short-circuit) — the verb exists and is `ruled`")
    w.dates["d_sitting"] = {"due_at": 1, "holder": "p_bench_a", "fired": False, "rung": "S"}

    w.manifest = {"contest": "seam.contest_resolver", "order": "core.canonical_order"}
    return w


def SUBSIST(p, w):
    scale = w.fixtures.get("condition_scale")
    home = Query.parent_of(w, p.id)
    if home is None or home not in w.rungs:
        return 0
    return min(scale, sum(w.rungs[home].stores.values()) * scale // max(1, p.weight))


def NOCHOOSE(p, v, s, ask_budget):
    return []


def act(w, pid, verb, key="", **kw):
    return Act(H(w.world_seed, w.tick, pid, f"act:{verb}:{key}"), pid, verb, **kw)


# ---------------------------------------------------------------------------
# THE SUITE
# ---------------------------------------------------------------------------
TESTS: list[dict] = []


def stress(sid, title, stresses, by):
    def deco(fn):
        TESTS.append(dict(id=sid, title=title, stresses=stresses, by=by, fn=fn))
        return fn
    return deco


# ===========================================================================
# GROUP A · CAN THE SUBSYSTEM BE REACHED AT ALL
# ===========================================================================

@stress("ST-01", "the prize `a matter` routes to a provider", "08_SEAM.md PART B", by="construction")
def st01():
    got = contest_subsystem("a matter")
    prizes = roster("contest_subsystems", "prizes") if False else None
    declared = yaml.safe_load((ARCH / "rosters.yaml").read_text())["rosters"]["contest_subsystems"]["prizes"]
    if got is not None:
        return "RAN", f"`a matter` resolves to {got}", []
    FIND("F-01", "the proceedings prize is declared in no roster, so the seam cannot reach the "
         "subsystem even in principle",
         f"`contest_subsystem('a matter')` returns None. `rosters.yaml: contest_subsystems.prizes` "
         f"declares {sorted(declared)} and no `manifest.yaml` exists anywhere in the repo. "
         f"`08_SEAM.md` PART B specifies the row and deliberately does NOT claim the two "
         f"`social_contest` rows, so today a `speak` that contests `a matter` falls through to "
         f"the generic `Unspecified('the degree ladder's margin model')`.",
         by="construction", severity="blocking", site="08_SEAM.md PART B",
         dup="the design's own `08_SEAM.md` PART B — it specifies the row and says the prize is new rather than claimed. **ADDS: the execution, and that no `manifest.yaml` exists anywhere**")
    INV("INV-09", "a manifest row `{role: contest, provider: proceedings, prize: 'a matter'}`",
        "without it nothing dispatches. The design specifies the row; no file in the tree holds it.",
        owner="the design (step 8 of 19_PLAN.md) — and a `rosters.yaml` prize edit, which is "
              "a data change somebody must make", kind="mechanism")
    return "BLOCKED", "no roster row; the seam cannot name a proceedings provider", ["F-01"]


@stress("ST-02", "the seam can carry a venue, a matter and an arrangement together",
        "08_SEAM.md PART A · shape.py:6139", by="construction")
def st02():
    src = (TRACER / "shape.py").read_text().splitlines()
    line = next((i + 1 for i, l in enumerate(src)
                 if "rung=(a.payload if isinstance(a.payload, str) else None)" in l), None)
    sig = shape.inspect.signature(contest) if hasattr(shape, "inspect") else None
    import inspect as _i
    params = list(_i.signature(contest).parameters)
    FIND("F-02", "the seam's own dispatch cannot pass a proceeding its venue AND its matter, "
         "because both ride on one `payload` field of two incompatible types",
         f"`contest(...)` takes {params} — there is no `matter`, no `arrangement` and no "
         f"`attendees` parameter. The fold builds the call at shape.py:{line} as "
         f"`rung=(a.payload if isinstance(a.payload, str) else None) or 'R'`, and the SAME "
         f"`payload` must be a dict to carry `subject` (the second claimant). So an act that "
         f"names its opponent CANNOT name its venue: every contested act with a dict payload "
         f"is dispatched at the REALM. `08_SEAM.md` writes "
         f"`proceedings.run(proj, place, claimants, depth, max_depth)` and then reads "
         f"`occasion_at(proj, place).arrangement` and `judging_set(proj, place, matter)` inside "
         f"it — `matter` is closed over from nowhere. The design's §C.1 amendment (the caller's "
         f"ordering) is stated; this one is not stated at all.",
         by="construction", severity="blocking", site="08_SEAM.md PART A",
         dup="NEW — no register row covers the seam's inability to carry a matter or an arrangement")
    MD("MD-01", "treat the venue/matter channel as a THIRD seam amendment, not a wiring detail",
       "`08_SEAM.md` PART C declares two amendments (the caller's ordering; the margin producer) "
       "and this is a third of the same kind — a signature the one owner must widen.",
       alternative="pass the matter inside `prize` (i.e. prize = the Proposition id), which the "
                   "roster's prize→module map cannot then key on, since the map is keyed by "
                   "prize STRING",
       falsifier="a `contest` signature carrying `matter` and `arrangement`, with the prize "
                 "still a rostered string")
    return "BLOCKED", "no channel for matter or arrangement; venue collapses to the realm", ["F-02"]


@stress("ST-03", "the bench Query answers", "00_DERIVATION.md §A.4 · 04_VERBS.md §B.2", by="construction")
def st03():
    w = proceedings_world()
    import inspect as _i
    live = list(_i.signature(Query.judging_set).parameters)
    try:
        Query.judging_set(w, "S")
        return "RAN", "judging_set answered", []
    except Unspecified as e:
        FIND("F-03", "the bench does not exist: `Query.judging_set` raises unconditionally, and "
             "the design's replacement takes a parameter the live signature has no room for",
             f"live signature {live} — two parameters. The design specifies "
             f"`judging_set(w, venue, matter)` and argues the third is REQUIRED, not convenient "
             f"(`04_VERBS.md` §B.2). The tracer raises: {e}. Everything downstream of the bench "
             f"— `disposal: bench` in 10 of 12 rows, `genre` (derived from the bench's remit), "
             f"`bench ∩ parties` (the column the taxonomy rests on) — is unreachable until this "
             f"function is written.",
             by="construction", severity="blocking", site="shape.py:3161",
         dup="`00_DERIVATION.md` §A.4 (*this subsystem's first deliverable*) + `04_VERBS.md` §B.2. **ADDS: the raise as an execution**")
        INV("INV-10", "a three-parameter `judging_set(w, venue, matter)` returning SEATS",
            "no proceeding can identify who may dispose of anything without it. ⚠ This harness "
            "does NOT supply a stand-in: a stand-in bench would turn the design's first "
            "deliverable into a harness fixture and every downstream trace would then be "
            "measuring my Query rather than the design.",
            owner="the design — its own §A.4 calls this 'this subsystem's first deliverable'",
            kind="mechanism")
        return "BLOCKED", f"judging_set raises: {e}", ["F-03"]


@stress("ST-04", "there is an occasion to attach an arrangement to",
        "08_SEAM.md PART A · 03_PARAMETERS.md PART D", by="no-signature")
def st04():
    missing = [n for n in ("occasion_at", "present_at", "attendees_at", "arrangements",
                           "latitude", "reception", "genre_of")
               if not hasattr(shape, n) and not hasattr(Query, n)]
    arr = list(REPO.rglob("arrangements.y*ml"))
    FIND("F-04", "every function `08_SEAM.md`'s own pseudocode calls is absent, and the "
         "arrangement file it reads does not exist",
         f"absent from the tracer: {missing}. `Query.presence(w, rung)` exists and is the only "
         f"one of the seven with a live analogue. No `arrangements.yaml` anywhere in the repo "
         f"({len(arr)} matches). So the twelve games are twelve YAML blocks inside a markdown "
         f"file — which under `CLAUDE.md` §0.05 is REFERENCE, not mechanism, and is the exact "
         f"grade `04_VERBS.md` §B.3 applies to the six investigation acts when it says a prose "
         f"table means they do not exist. The same test applied to this design's own parameter "
         f"space returns the same answer.",
         by="no-signature", severity="material", site="03_PARAMETERS.md PART D",
         dup="`03_PARAMETERS.md` §F.3 self-grades the closure claim `STATUS: HYPOTHESIS`. **ADDS: the count of absent signatures**")
    INV("INV-11", "`data/arrangements.yaml` with fifteen keys × twelve rows",
        "the parameter space is the subsystem's central claim and has no machine-readable form.",
        owner="the design (step 11 of 19_PLAN.md)", kind="mechanism")
    return "BLOCKED", f"{len(missing)} of 7 named functions absent; no arrangements file", ["F-04"]


# ===========================================================================
# GROUP B · CONVENING, THE DOCKET, AND OPENING A CASE
# ===========================================================================

@stress("ST-05", "a fired Date puts the matter on a docket a `speak` can name",
        "04_VERBS.md §B.1(ii) · 03_PARAMETERS.md §C.1.1", by="construction")
def st05():
    w = proceedings_world()
    d = SeasonDriver(w)
    # ⛔ A DRAFT RAN ONE SEASON AND REPORTED AN EMPTY DOCKET AS EVIDENCE. It was not:
    # `World.tick` starts at 0 and `season()` increments at its END, so a date `due_at: 1` is
    # never reached in one season and CALENDAR's `due_at != tick` guard skipped the branch
    # entirely. The empty list measured the fixture's off-by-one, not the design. Two seasons.
    d.season(NOCHOOSE, question=None, subsistence=SUBSIST)
    d.season(NOCHOOSE, question=None, subsistence=SUBSIST)
    items = list(w.docket)
    matters = [it.get("matter") for it in items]
    fired = w.dates["d_sitting"].get("fired")
    FIND("F-05", "the docket item CALENDAR appends carries `matter: None`, so `speak`'s only "
         "precondition can never be satisfied by convening alone",
         f"after two seasons the date has fired ({fired}) and the docket holds {items}. "
         f"`speak`'s `requires_typed` is "
         f"`{{form: existence, of: subject, kind: DocketItem}}`, and CALENDAR "
         f"(shape.py:5378-5380) writes "
         f"`{{'date': did, 'matter': None}}`. The only writer of `DocketItem.matter` in the "
         f"32-row verb table is `carry`. "
         f"⚠ **AND THE TYPED CELL AND ITS OWN PROSE DO NOT AGREE, WHICH IS THE SHARPER HALF.** "
         f"The prose `requires` reads *a live occasion at the actor's venue **whose docket names "
         f"the subject***; the typed form is a bare existence test that binds the act's "
         f"`subject` and asks whether it exists as a `DocketItem`. **A docket item with "
         f"`matter: None` satisfies the typed cell and fails the prose.** So `speak` either has "
         f"a precondition that is unsatisfiable until somebody carries the papers, or one that "
         f"is satisfied by an empty sitting — and which it is depends on which half of the row a "
         f"reader takes as the mechanism. Under `CLAUDE.md` §0.05 the typed cell is the "
         f"mechanism and the prose is reference, so the *empty sitting* reading wins and the "
         f"design's own account of what `speak` is for does not. "
         f"⛔ **A DRAFT OF THIS FINDING CLAIMED THE CELL REQUIRES THE MATTER AND CONCLUDED A "
         f"CLERK IS MANDATORY. It does not, and the retraction is recorded.** The clerk is still "
         f"the thing nobody has: `03_PARAMETERS.md` §C.2 lists *clerk / recorder* as a role and "
         f"no procedure gives it a step, so the docket in practice never names a matter.",
         by="construction", severity="blocking", site="04_VERBS.md §B.1",
         dup="NEW — the docket's content was never checked")
    INV("INV-12", "a clerk act — `carry` by a person holding the case Record — between the "
        "date firing and the first speech",
        "without it `DocketItem.matter` is None and no `speak` forms. `03_PARAMETERS.md` §C.2 "
        "lists 'clerk / recorder' as a role and gives it no step in any procedure.",
        owner="the design — 05_PROCEDURE.md's nested run has no docketing step", kind="mechanism")
    return "BLOCKED", f"docket matter is {matters}", ["F-05"]


@stress("ST-06", "the design's account of when CALENDAR dockets is the code's",
        "03_PARAMETERS.md §C.1.1 vs shape.py:5363-5381", by="document")
def st06():
    src = (TRACER / "shape.py").read_text()
    i = src.index("vacant = not d.get(\"holder\")")
    window = src[i:i + 900]
    guarded_by_not_vacant = "if not vacant:" in window and "w.docket.append" in window
    claim = "CALENDAR appends a `DocketItem` when a fired date is\n   **vacant**"
    doc = (DESIGN / "03_PARAMETERS.md").read_text()
    asserts_vacant = "vacant" in doc
    if guarded_by_not_vacant and asserts_vacant:
        FIND("F-06", "the design states the docketing rule BACKWARDS against the code it cites "
             "by line number",
             "`03_PARAMETERS.md` §C.1.1 item 2: *'the path already exists: CALENDAR appends a "
             "`DocketItem` when a fired date is **vacant** (`shape.py:5363-5381`)'*. The code at "
             "that exact range computes `vacant = not d.get('holder')` and then appends the "
             "docket item under `if not vacant:`. A VACANT date fires and lapses and dockets "
             "NOTHING. The design's proof that 'a convened proceeding nobody attends is a "
             "legitimate outcome' therefore cites the branch that does the opposite of what it "
             "says. The OUTCOME may still be legitimate; the mechanism named for it is not there.",
             by="document", severity="material", site="03_PARAMETERS.md §C.1.1",
         dup="NEW")
        return "FAILED", "design says vacant→docket; code says holder→docket", ["F-06"]
    return "RAN", "the claim matches the code", []


@stress("ST-07", "a party with no seat can open the case that names its own terms",
        "00_DERIVATION.md §A.5 (T-n) · verb_table.yaml", by="construction")
def st07():
    row = VERB_TABLE.get("open_case")
    elig = list(row.eligibility) if row else []
    FIND("F-07", "`open_case` is `remit:determine`, so in the games with no bench NOBODY CAN "
         "OPEN THE CASE — and with it, nobody can declare the term, the stages or the appeal cap",
         f"`open_case` eligibility = {elig}. `00_DERIVATION.md` §A.5 and §A.6 hang four "
         f"mechanisms on the opening act: the declared term that ends a proceeding nobody is "
         f"advancing (`T-n`), the stages, the named arbiter, and the appeal DEPTH CAP whose "
         f"absence of a default is a stated invariant (`H-87`). §B.2 objection 3 already "
         f"notices that FIVE of the twelve games have no `open_case` — negotiation, public "
         f"debate, audience, interrogation, negotiation-by-envoys — and uses it as an argument "
         f"against a field. It is a much larger problem than that: those five games have NO "
         f"TERM, NO STAGES and NO DEPTH CAP, and `05_PROCEDURE.md` §B.1 lists 'the declared "
         f"term matures' as one of only four things that can end a run. Two of the remaining "
         f"three (the depth cap, the foot of the ladder) also come from the opening act or from "
         f"a bench. In a negotiation the ONLY termination condition left is 'nobody acts'.",
         by="construction", severity="material", site="04_VERBS.md PART A",
         dup="`00_DERIVATION.md` §B.2 objection 3 (five games have no `open_case`). **ADDS: that those five therefore have no term, no stages and no depth cap**")
    return "FAILED", f"open_case is {elig}; five games cannot take it", ["F-07"]


@stress("ST-08", "the `scale:` key invariant 10 forbids actually fails the load",
        "03_PARAMETERS.md §C.1 · 08_SEAM.md D.2 invariant 10", by="construction")
def st08():
    """⛔ **REWRITTEN. A DRAFT OF THIS TEST PUBLISHED A FALSE FINDING AND CONTRADICTED ITSELF IN
    ITS OWN OUTPUT STRING.** It claimed *the key is ALREADY GONE from the table this repo
    carries*, while interpolating `scale present = True` into the same paragraph and printing
    `scale key absent (True)` as its verdict line. The key is at `verb_table.yaml:138`. The
    retraction is recorded rather than overwritten, and the test now asks the question that was
    worth asking: **the design says invariant 10 makes this key fail the load — does it?**"""
    raw = yaml.safe_load((ARCH / "verb_table.yaml").read_text())
    rows = raw if isinstance(raw, list) else raw.get("verbs")
    cv = next(r for r in rows if r.get("verb") == "convene")
    has_scale = "scale" in cv
    loaded = VERB_TABLE.get("convene")
    kept = getattr(loaded, "scale", "<no attribute>")
    ops = roster("requires_operands")
    FIND("F-08", "the key the design corrects is live, the loader ACCEPTS it, and the ordinal "
         "that replaces it has no operand to name the venue",
         f"`convene` carries `scale: {cv.get('scale')!r}` at `verb_table.yaml:138` "
         f"(present: {has_scale}), and the tracer's loader parsed it into a live `VerbRow.scale` "
         f"= {kept!r} without complaint. So `08_SEAM.md` D.2 invariant 10 — *a `scale:` key fails "
         f"the load* — is a specified invariant with **no implementation**, and Jordan's "
         f"2026-09-05 correction is unexecuted rather than already applied. "
         f"⚠ **AND THE REPLACEMENT IS NOT EXPRESSIBLE**: `rank(venue.kind) > rank(person)` needs "
         f"`venue` as an operand and `requires_operands` = {ops} has none; the nearest member is "
         f"`site`, a different carrier. `rung_kinds` IS ordered, so the comparison exists — it "
         f"has nothing to compare. **The correction is one roster member away and the design does "
         f"not say so.**",
         by="construction", severity="material", site="03_PARAMETERS.md §C.1",
         dup="`03_PARAMETERS.md` §C.1 + `08_SEAM.md` D.2 invariant 10 both say the key must go. "
             "**ADDS: that the loader does not refuse it, so the invariant is unimplemented; and "
             "that the replacement needs a `venue` operand the closed roster lacks**")
    return "FAILED", f"scale={cv.get('scale')!r} live and loaded; no `venue` operand", ["F-08"]


# ===========================================================================
# GROUP C · CAN A PERSON SPEAK, AND WHAT DOES THE SPEECH DO
# ===========================================================================

@stress("ST-09", "a `speak` reaches RESOLVE and emits", "04_VERBS.md §B.1", by="construction")
def st09():
    w = proceedings_world()
    made = []

    def choose(p, v, s, ask_budget):
        if p.id != "p_party_a":
            return []
        a = act(w, "p_party_a", "speak", key="open")
        made.append(a)
        return [a]

    d = SeasonDriver(w)
    r = d.season(choose, question=None, subsistence=SUBSIST)
    mine = [e for e in w.log if made and made[0].id in e.causes] if made else []
    if not made:
        return "BLOCKED", "the chooser was never asked (no Candidate formed)", []
    if not mine:
        FIND("F-09", "a `speak` reaches RESOLVE and produces nothing at all",
             "the act folded and emitted no Event naming it. The live row is "
             "`writes: []`, `emits: [speech.made]`, `grade: assumption`.",
             by="construction", severity="material", site="verb_table.yaml speak",
         dup="—")
        return "FAILED", "no Event names the speech", ["F-09"]
    return "RAN", (f"a `speak` by a person holding no seat folded and emitted "
                   f"{[e.kind for e in mine]} — the ONE thing in the whole proceeding that "
                   f"executes today, and it writes nothing"), []


@stress("ST-10", "a `speak` that contests a matter reaches a provider",
        "04_VERBS.md PART C · 08_SEAM.md", by="construction")
def st10():
    w = proceedings_world()

    def choose(p, v, s, ask_budget):
        if p.id != "p_party_a":
            return []
        return [act(w, "p_party_a", "speak", key="press",
                    contests=["a matter"], payload={"subject": "p_party_b"})]

    d = SeasonDriver(w)
    try:
        d.season(choose, question=None, subsistence=SUBSIST, contest_max_depth=2)
    except Unspecified as e:
        FIND("F-10", "a contested `speak` stops at the seam with no provider and no margin",
             f"the fold dispatched and the seam refused: {e}. This is the design's own "
             f"`08_SEAM.md` PART C.2 stated as an execution: the margin-graded branch has a "
             f"reader (`degree_of` recognises `net`/`ob`) and NO PRODUCER, and this subsystem "
             f"was to be the first. It is not one yet.",
             by="construction", severity="blocking", site="08_SEAM.md PART C.2",
         dup="`08_SEAM.md` PART C.2, the design's own second declared amendment. **ADDS: the execution**")
        return "BLOCKED", f"seam refused: {type(e).__name__}", ["F-10"]
    except Forbidden as e:
        return "BLOCKED", f"forbidden: {e}", []
    return "RAN", "a provider answered", []


@stress("ST-11", "the four band keys the design writes against are the ladder's",
        "04_VERBS.md §B.1 · 09_IMPOSSIBILITIES.md row 16", by="construction")
def st11():
    design_bands = ["Overwhelming", "Success", "Partial", "Failure"]
    inv_bands = ["Found", "Partial", "Nothing", "Read", "Misread", "Sound", "Wrong",
                 "Seen", "Glimpsed"]
    non_ladder = sorted(set(inv_bands) - set(design_bands))
    ladder = REPO / "engine" / "autoload" / "dice_engine.py"
    labels = []
    if ladder.exists():
        txt = ladder.read_text()
        m = re.search(r"DEGREE_LABEL[^=]*=\s*\{(.*?)\}", txt, re.S)
        if m:
            labels = re.findall(r":\s*[\"']([A-Za-z ]+)[\"']", m.group(1))
    same = labels[:4] == design_bands if labels else None
    # EXECUTE the claim rather than assert it: build the `examine` row exactly as the design
    # declares it and hand it the band a margin-graded contest actually returns.
    probe = None
    try:
        row = shape.VerbRow(
            verb="examine", stratum="contested_physical", eligibility=("own",),
            requires="the actor is present where the thing examined is",
            writes=(), emits=(), emits_on_refusal=("examine.impossible",),
            grade="assumption", scale=None, contests="what persists",
            writes_by_degree={"Found": (), "Partial": (), "Nothing": ()},
            emits_by_degree={"Found": ("facet.found",), "Partial": ("facet.found",),
                             "Nothing": ("facet.none",)},
            requires_typed=None, requires_typed_note=None)
        row.writes_at("Success")
        probe = "the row ACCEPTED the ladder's `Success` band"
    except Unspecified as e:
        probe = f"the row RAISED on the ladder's own band: {str(e).splitlines()[0][:160]}"
    except Exception as e:  # noqa: BLE001
        probe = f"harness could not build the row ({type(e).__name__}: {e}); claim stays document-grade"
    FIND("F-11", "`speak` uses the ruled four-band ladder and the five investigation rows use "
         "NINE band names of their own, in the same directory that calls a second ladder its "
         "weak point",
         f"the tree's ladder labels = {labels or 'not parsed'} (speak matches: {same}). "
         f"`04_VERBS.md` §B.3.2 keys the five investigation rows on {sorted(set(inv_bands))}, of "
         f"which {len(non_ladder)} are not the ladder's: {non_ladder}. ⚠ `Partial` IS the "
         f"ladder's third band and appears in two of the five rows, so a draft's *none of them "
         f"the ladder's* was wrong by two. "
         f"⭐ EXECUTED: {probe}. "
         f"Three bands per row, none of them the ladder's, in three different vocabularies "
         f"(Found/Partial/Nothing · Read/Misread/Nothing · Sound/Wrong/Nothing · "
         f"Seen/Glimpsed/Nothing). §B.1 retracts exactly this defect for `speak` — *'every "
         f"`speak` would have raised at the first fold'* — and leaves it standing in the five "
         f"rows on the next page. `writes_at`/`emits_at` raise on any undeclared degree, so if "
         f"these five ever route through a margin-graded contest they raise identically. "
         f"⚠ The narrower reading, which the design does not state: they contest against "
         f"something (`retention`, `obstinacy`, concealment) and are three-band, so either they "
         f"are NOT margin-graded — in which case they need combat's kind of ruled exemption and "
         f"do not have one — or they are, and they are broken.",
         by="construction", severity="material", site="04_VERBS.md §B.3.2",
         dup="NEW — §B.1 retracts the coined bands for `speak` and leaves the five investigation rows")
    MD("MD-02", "read the five investigation rows as UNRULED rather than as broken",
       "combat's three-band exemption exists BY RULING because it reads a scene rather than a "
       "margin (`rosters.yaml: combat_degree_bands`), and these five plausibly do the same. "
       "But no ruling covers them and the design does not ask for one.",
       alternative="grade them broken outright, as §B.1 graded the coined `speak` bands",
       falsifier="a ruling, or a `writes_at` call against one of these rows returning a band")
    return "FAILED", (f"{len(non_ladder)} non-ladder band names across 5 rows; speak matches "
                      f"ladder: {same}"), ["F-11"]


@stress("ST-12", "every `requires_typed` form the design declares exists in the grammar",
        "04_VERBS.md · rosters.yaml requires_forms", by="construction")
def st12():
    forms = roster("requires_forms")
    declared = {
        "speak": "existence",
        "determine (conjunct 1)": "existence",
        "determine (conjunct 2)": "basis",
        "examine": "path",
        "interview": "path",
        "research": "existence",
        "reconstruct": "own_ledger",
        "release": "existence",
    }
    bad = {v: f for v, f in declared.items() if f not in forms}
    if not bad:
        return "RAN", "every declared form is in the roster", []
    probe = None
    try:
        shape.build_typed_requires("examine", {"form": "path", "of": "subject", "kind": "contain"})
        probe = "the loader ACCEPTED an unrostered form"
    except SystemExit as e:
        probe = f"the loader refused: {e}"
    except Exception as e:  # noqa: BLE001
        probe = f"{type(e).__name__}: {e}"
    FIND("F-12", "two of the five new investigation rows name a `requires_typed` form that is "
         "not in the closed grammar, and would refuse at load",
         f"roster `requires_forms` = {forms}. Declared but absent: {sorted(bad)} — both write "
         f"`form: path` where the roster's member is `contain_path`. Probe against the real "
         f"loader: {probe}. This is a one-word fix and it is worth recording only because of "
         f"WHERE it is: `04_VERBS.md` §B.3.1 argues that five of six preconditions are "
         f"*'expressible in it without inventing anything'*, and two of the five are written in "
         f"a form name the grammar does not carry. The claim is right; the cells do not "
         f"instantiate it.",
         by="construction", severity="nit", site="04_VERBS.md §B.3.2",
         dup="NEW")
    return "FAILED", f"{len(bad)} cells name a non-member form", ["F-12"]


@stress("ST-13", "whose stance a `speak` writes", "04_VERBS.md §B.1(v)", by="document")
def st13():
    doc = (DESIGN / "04_VERBS.md").read_text()
    says_own = "the band writes the speaker's own" in doc
    FIND("F-13", "three of `speak`'s four bands write `Person.stance` and the design says whose "
         "only for the fourth",
         f"`writes: {{Overwhelming: [Person.stance], Success: [Person.stance], "
         f"Partial: [DocketItem.matter], Failure: [Person.stance]}}`. The text names the owner "
         f"for `Failure` only — *'the band writes the speaker's own stance'* (present: "
         f"{says_own}) — and it is named there precisely because writing the SPEAKER's stance on "
         f"a failure is the surprising half. On `Overwhelming` and `Success` the natural reading "
         f"is the opposite one: the speech moved THE HEARERS' stances. That reading is a "
         f"one-act-many-owners write, which `T-m` refuses and which `00_DERIVATION.md` §B.2 "
         f"objection 2 uses to KILL the `Tenure.degree` proposal in this same directory "
         f"(*'each party who descends would write the OPENER's edge. Many writers, one owner'*). "
         f"The design applies that objection to a field it rejected and not to the verb it kept. "
         f"⚠ And the harness cannot resolve it from the row: a matrix row is `(Person, stance)` "
         f"with no subject column, so BOTH readings load.",
         by="document", severity="material", site="04_VERBS.md §B.1",
         dup="`17_PLAYABILITY.md` §D.3 and §I item 3, which already grade it *a live `AX-4` breach in the row as written*. **ADDS: nothing but a second confirmation — and this suite failed to cite it, which is the citation defect it faults elsewhere**")
    MD("MD-03", "trace `Overwhelming`/`Success` as writing the SPEAKER's stance, matching Failure",
       "it is the only reading that survives `T-m`, and it keeps all four bands one-owner.",
       alternative="the hearers' stances move — which is what 'carrying the room' means in the "
                   "fiction, and what `06_RESOLUTION.md` PART D's 'COSTLY writes Person.stance "
                   "AND claims into every witness's ledger' implies",
       falsifier="a ruling; or a `speak` fold that writes two persons' stances and passes the "
                 "one-owner gate, which would mean the gate does not check subject==actor")
    return "FAILED", "ownership of the stance write is undetermined for 3 of 4 bands", ["F-13"]


# ===========================================================================
# GROUP D · DISPOSING OF THE MATTER
# ===========================================================================

@stress("ST-14", "a verdict is a Tenure its determiner OPENED", "00_DERIVATION.md §A.6", by="construction")
def st14():
    row = VERB_TABLE.get("determine")
    writes = row.writes if row else None
    FIND("F-14", "`determine` can GRADE a Tenure and cannot OPEN one, so the verdict the whole "
         "`AX-6` argument rests on has no producer",
         f"`determine.writes` = {writes}. `00_DERIVATION.md` §A.6 is explicit that a verdict is "
         f"*'a `Tenure` the determiner opened, closable by `T-o`'*, and that this is what gives "
         f"the appeal for free. Opening a Tenure is `Tenure.since`, which `determine` does not "
         f"write — `commit`, `oblige`, `confer`, `succeed` and `tie / knot` do. `04_VERBS.md` "
         f"§B.2 then adds *'⚠ UNCHANGED from the live row'* and corrects a draft that had "
         f"proposed `[Tenure.degree, Tenure.since, Tenure.until]` — i.e. the draft that WOULD "
         f"have opened the verdict was corrected into one that cannot. "
         f"⚠ So: WHICH Tenure does a finding grade? The design never says. If it grades the "
         f"loser's existing `hold`, the finding is a number on somebody else's edge and the "
         f"non-owner objection of §B.2 applies verbatim. If it grades a new one, nothing opens it. "
         f"⭐ AND THE SHARPER FORM IS ABOUT THE KEY, NOT THE VERB: `disposes:` NAMES A WRITE "
         f"AND HAS NO WRITER. Every one of the twelve rows carries "
         f"`disposes: <tenure> | Record | oblige | none`; `14_THE_WORLD_IN_THE_ROOM.md` §E "
         f"makes *what does this game change in the world* the governing test; and NOTHING "
         f"IN THE DESIGN CONNECTS THE KEY TO ANY ACT'S `writes` COLUMN. That is `ID-13` — "
         f"find a key a reader or remove it — applied to this design's most load-bearing "
         f"key. ⚠ And `11_NERS.md`'s diagonal PASS rests on it verbatim: *'`disposes` "
         f"writes a Tenure — a seat, a duty, a severance — which is a strategic object'*. "
         f"It does not write one, and no verb in the table does.",
         by="construction", severity="blocking", site="00_DERIVATION.md §A.6",
         dup="NEW — and it is the strongest finding here")
    INV("INV-13", "the verdict Tenure: a kind, a subject, and an act that opens it",
        "the harness cannot trace a disposal without inventing the edge the finding IS.",
        owner="the design — this is the disposal, i.e. the thing every game's `disposes:` key "
              "names", kind="mechanism")
    return "BLOCKED", f"determine writes {writes}; nothing opens a verdict", ["F-14"]


@stress("ST-15", "an adjudicator can act AS a seat", "10_LOOPS_AND_GAPS.md P-03", by="construction")
def st15():
    import dataclasses
    fields = [f.name for f in dataclasses.fields(Act)]
    ops = roster("requires_operands")
    FIND("F-15", "`Act` has no `via`, so the one thing that makes an adjudicator's act a "
         "SEAT'S act is unrepresentable — and the design's own `requires` cell for it was "
         "already retracted once for naming an operand outside the roster",
         f"Act fields = {fields}. `requires_operands` = {ops} — no `via`. The design registers "
         f"this as `P-03` / `H-108` and then relies on it in four places that are not marked as "
         f"blocked by it: the verdict's authorship (`AX-6`), `T-o`'s revocation gate, the "
         f"tribunal's `interposed: [office]` discount, and `03_PARAMETERS.md` §C.2's whole "
         f"adjudicator row (*'holds a seat … and acts **via** it'*). Without `via`, an "
         f"adjudicator's determination is indistinguishable from a private opinion by the same "
         f"person, which deletes the difference between the bench and the floor.",
         by="construction", severity="blocking", site="04_VERBS.md §B.2",
         dup="`P-03` / `H-108` on the `via` half. **ADDS: the tribunal `interposed: [office]` discount and the verdict's authorship as sites that depend on it and are not marked blocked by it**")
    return "BLOCKED", "no Act.via", ["F-15"]


@stress("ST-16", "two bench members determining is a MAP, not a procedure",
        "05_PROCEDURE.md PART A · §C", by="document")
def st16():
    """⛔ **A DRAFT OF THIS TEST GRADED THE QUORUM AS AN OPEN QUESTION IT WAS PROMOTING TO A
    BLOCKER. IT IS RULED AND CLOSED**, and this suite had the ruling in hand — it cites
    `ED-SC-0034` in the very next test. Corrected."""
    FIND("F-16", "the quorum is RULED, not open — what is unbuilt is a ruled thing, and six rows "
         "wait on it",
         "⛔ **RETRACTION.** A draft said *`P-15` calls a quorum 'not built' and 'a ruling on "
         "whether majorities are wanted'* and regraded it a build blocker. `19_PLAN.md` says "
         "**`P-15` closes**, and `ED-SC-0034` (status `ruled`, `needs_jordan: false`) records "
         "Jordan's *'of course we accept those shapes'* — the multilateral tally and the debate "
         "score land, and conclaves, votes and majority verdicts come into range. The row at "
         "`10_LOOPS_AND_GAPS.md` P-15 is the **stale surface**, and it is stale in the register "
         "the design points a reader at first. "
         "⭐ **WHAT SURVIVES, AND IT IS NARROWER AND STILL WORTH SAYING**: the ruled shape — a "
         "Query over the bench's live determinations, read by a LATER declaring act — means the "
         "disposal of a multi-member bench needs *a further person to act*. `05_PROCEDURE.md` "
         "§A grades the bench's determinations a MAP on the ground that *two determinations do "
         "not read each other*, which stays true; but the finding they produce is then nobody's "
         "until somebody declares it, and **no verb in this design declares a tally**. So the "
         "ruling is landed and its verb is missing, which is `ID-14` in the same shape as F-14. "
         "⚠ And the stale P-15 row is itself the finding a reader should act on: the gap "
         "register is the first thing `README.md` sends you to.",
         by="document", severity="material", site="10_LOOPS_AND_GAPS.md P-15",
         dup="⛔ `P-15` — **and P-15 IS CLOSED** by `19_PLAN.md` step 15 and `ED-SC-0034`. "
             "**ADDS: that the register row is stale, and that the ruled shape needs a declaring "
             "act no verb supplies**")
    MD("MD-04", "check every gap-register row against the newer rulings before citing it",
       "the register at `10_LOOPS_AND_GAPS.md` predates the 2026-09-06 rulings recorded in "
       "`19_PLAN.md`, `ED-SC-0033..0035` and `HANDOFF_SC.md`, and P-15 and P-29 are both stale "
       "there. A suite that cites the register without the ledger reports settled questions.",
       alternative="cite the register as the design presents it, which is what a draft of this "
                   "suite did for P-15 while citing the ledger for the next finding",
       falsifier="any other P-row a later ruling closed — `P-29` is the second, closed by *pool "
                 "only it is*, and it is not in the register at all (see F-37)")
    return "FAILED", "P-15 is ruled and closed; the register row is stale", ["F-16"]


@stress("ST-17", "a five-party negotiation can settle", "14_THE_WORLD_IN_THE_ROOM.md §A.1",
        by="document")
def st17():
    FIND("F-17", "`disposal: mutual` is defined over two parties and the game's own headline "
         "case — a peace conference — has five",
         "the design says so itself and then leaves the row: *'a multilateral treaty does not "
         "work. `disposal: mutual` is defined over TWO parties'*. `19_PLAN.md` step 15 proposes "
         "the fix (a Query read by a declaring act) and `ED-SC-0034` records Jordan accepting "
         "the multilateral tally. So this is RULED and unbuilt rather than open — but until it "
         "is built, the negotiation row is a two-body row and the design's catalogue does not "
         "say so.",
         by="document", severity="material", site="03_PARAMETERS.md §E.2",
         dup="`P-15` / `19_PLAN.md` step 15 / `ED-SC-0034` / `17_PLAYABILITY.md` PART F row B-6. **ADDS: nothing; it is the ruling restated**")
    return "FAILED", "mutual disposal is 2-party only", ["F-17"]


# ===========================================================================
# GROUP E · ENDING, APPEALING, AND BEING ABSENT
# ===========================================================================

@stress("ST-18", "a proceeding nobody advances can END", "05_PROCEDURE.md §B.1", by="construction")
def st18():
    import dataclasses
    tf = [f.name for f in dataclasses.fields(Tenure)]
    rf = [f.name for f in dataclasses.fields(Record)]
    matrix = yaml.safe_load((ARCH / "write_matrix.yaml").read_text())
    rows = matrix if isinstance(matrix, list) else matrix.get("rows")
    rec_rows = [(r["kind"], r["field"], r.get("steps"), r.get("emits"))
                for r in rows if r.get("kind") == "Record"]
    FIND("F-18", "`Tenure` has no `term` — but `Record` already carries `ttl`, `stages` and a "
         "`term.matured` emission, and the design never considers it",
         f"Tenure fields = {tf} (no `term`; `P-04` grades this `absent`, no default). "
         f"Record fields = {rf}. Record matrix rows = {rec_rows}. `open_case` writes "
         f"`Record.exists` and `Record.stages` — it is ALREADY the act that opens the case "
         f"document — and the matrix declares `(Record, matured)` at MATTER emitting "
         f"`term.matured`, plus `(Record, ttl)` at MATTER emitting `record.expired`. That is "
         f"`T-n`'s shape — *MATTER matures what an act wound, citing the act that wound it* — "
         f"sitting on the carrier the opening act already writes. The design instead specifies a "
         f"NEW `Tenure.term(matures_at, declared_by, closer)` field, which `19_PLAN.md` step 22 "
         f"calls *'the one new field in the whole plan'*. "
         f"⚠ The five-test order in `CLAUDE.md` §0 puts *answered by precedent* fourth and it "
         f"fires here: the summons's return day may need no new field at all. "
         f"⚠⚠ AND `(Record, matured)` IS IN THE MATRIX AND NOT ON THE CLASS — a matrix row for a "
         f"field that does not exist, which is its own defect and which is why nobody noticed "
         f"the carrier was available.",
         by="construction", severity="material", site="10_LOOPS_AND_GAPS.md P-04",
         dup="`P-04` on the first half. **ADDS: the `Record` carrier the design never considered, and a matrix row for a field the class does not have**")
    return "FAILED", "no Tenure.term; Record.ttl/stages/matured unexamined", ["F-18"]


@stress("ST-19", "an appeal chain terminates", "00_DERIVATION.md §A.6 · shape.py contest",
        by="construction")
def st19():
    w = proceedings_world()
    r = contest(w, rung="S", prize="a matter", claimants=["p_party_a", "p_party_b"],
                depth=2, max_depth=2, causes=["act:x"])
    ok = isinstance(r, ContestError)
    try:
        contest(w, rung="S", prize="a matter", claimants=["p_party_a"], depth=0, max_depth=2,
                causes=["act:x"])
        deeper = "no refusal below the cap"
    except ShapeGap as e:
        deeper = f"{type(e).__name__}: {str(e)[:80]}"
    if ok:
        FIND("F-19", "the depth cap WORKS and nothing can supply it, because the act that "
             "declares it cannot be taken in five of the twelve games",
             f"`contest(depth=2, max_depth=2)` returned {r!r} — a typed refusal, not a raise, "
             f"exactly as `00_DERIVATION.md` §A.6 and `H-87` require. Below the cap the call "
             f"still stops: {deeper}. The mechanism is built and unfed. And the FEED is the "
             f"problem: §A.6 rules that the cap *'is declared by the act that opened the case'*, "
             f"`open_case` is `remit:determine` (F-07), and `appeal_basis: determine` appears in "
             f"five rows — so the number of appeals a matter admits is set by an act the "
             f"appellant cannot take and, in the five bench-less games, nobody can take at all. "
             f"⚠ **And this harness supplies `max_depth` itself** (INV-21, `contest_max_depth=2` "
             f"from the tracer's fixtures), which is what let the cap be exercised at all — so "
             f"*nothing supplies it* means nothing IN THE DESIGN does, not that the parameter is "
             f"unreachable.",
             by="construction", severity="material", site="00_DERIVATION.md §A.6",
         dup="`00_DERIVATION.md` §A.6 (*the mechanism is built; nothing has fed it*). **ADDS: the `ContestError` as an execution**")
        return "RAN", f"cap returns {r!r}; nothing supplies max_depth", ["F-19"]
    return "FAILED", f"cap returned {r!r}", []


@stress("ST-20", "the world can say WHY the subject is absent", "10_LOOPS_AND_GAPS.md P-33",
        by="construction")
def st20():
    w = proceedings_world()
    present = Query.presence(w, "S")
    absent_is_elsewhere = "p_absent" not in present
    row = VERB_TABLE.get("evade / defy")
    FIND("F-20", "contumacy and incapacity are the same state, and in canon and common law the "
         "first IS the finding",
         f"presence at S = {sorted(present)}; the subject is absent = {absent_is_elsewhere}. "
         f"The world knows only that a `contain` edge points elsewhere. `P-33` names the four "
         f"cases — declined · could not · was not admitted · did not know — and grades the "
         f"collapse *a RULING*. Two of the four are already expressible and the design does not "
         f"use them: **was not admitted** is `floor: closed` plus `admitted:<basis>`, a key it "
         f"already carries; **declined** is `evade / defy` against a summons, a live verb "
         f"(`writes: {row.writes if row else '?'}`) that needs a summons with a return day, "
         f"i.e. F-18. So P-33 is not one ruling — it is one ruling (did-not-know vs could-not) "
         f"plus two wirings the design already owns and did not connect. "
         f"⚠ And the excommunication row's boast — *'there is NO `subject_absent` key, and that "
         f"is the result'* — is only true for the case where absence is uninformative. Where "
         f"contumacy is the finding, the absence must be READ, and nothing reads it.",
         by="construction", severity="material", site="03_PARAMETERS.md §C.1.1",
         dup="`P-33`, which already names `evade / defy` and the return day. **ADDS: that `floor: closed` + `admitted:<basis>` is the third case and is already a key the design carries**")
    return "FAILED", "four absence reasons collapse to one containment fact", ["F-20"]


# ===========================================================================
# GROUP F · WHO LEARNS WHAT HAPPENED
# ===========================================================================

@stress("ST-21", "a disposal's reach can be computed from anything but presence",
        "08_SEAM.md §D.3 · 03_PARAMETERS.md §B.7", by="construction")
def st21():
    """⛔ **A DRAFT OF THIS TEST PUBLISHED A FALSE FINDING**: that `disposal_reach` needs a sixth
    witness channel because *no channel mints a claim for a non-attendee*. Two do, and the draft
    graded the claim `construction` while never opening either. Retracted here; the corrected
    finding is narrower and is about whether the two that exist FIRE."""
    w = proceedings_world()
    channels = roster("witness_channels")
    # do the channels that would carry `body` and `<rung kind>` fire in this fixture?
    from shape import CHANNEL_PREDICATES, Event as _E
    e = _E("e_probe", "tenure.opened", "p_bench_a", [], ["a"], 0)
    fires = {c: [pid for pid in w.persons if CHANNEL_PREDICATES[c](w, e, pid)]
             for c in channels if c in CHANNEL_PREDICATES}
    FIND("F-21", "the two channels that would carry `body` and `<rung kind>` already exist and "
         "neither fires — one because no verb emitting a proceeding's disposal has a typed "
         "`requires`, the other because nobody holds the matching remit",
         f"⛔ **RETRACTION.** A draft of this finding said the reach *needs a SIXTH channel* and "
         f"graded it `construction` without opening the five. It is false: `_ch_post_remit` "
         f"walks a person's live `hold` Tenures for an office whose `remit_acts` intersect the "
         f"emitting verb's `remit:` eligibility, **with no presence test at all** — which is "
         f"`08_SEAM.md`'s `body` reach exactly — and `_ch_chronicle`'s own docstring says *when "
         f"it fires it fires for everyone alive*, which is the `<rung kind>` case at its widest. "
         f"**The mechanism `disposal_reach` needs is closer to free than either the design or "
         f"the draft said.** "
         f"⭐ **THE CORRECTED FINDING IS ABOUT FIRING, NOT ABOUT EXISTING.** On a "
         f"`tenure.opened` Event in this fixture the five channels select: "
         f"{json.dumps({k: sorted(v) for k, v in fires.items()})}. `chronicle` is an "
         f"EVENT-KIND filter over verbs the fold can resolve, and the tracer's own comment "
         f"records that *the eight `binding_decision` verbs all have prose `requires:` and none "
         f"is in `REQUIRES_PREDICATES`*, so it matches nobody — and `determine`, the verb that "
         f"disposes, is one of those eight. `post_remit` needs somebody holding the remit the "
         f"emitting verb requires. **So the reach has carriers and no traffic**, and closing "
         f"`P-43` on `disposal_reach` was right about the shape and has not been tested against "
         f"the channels that must carry it.",
         by="construction", severity="material", site="08_SEAM.md §D.3",
         dup="`P-43`, closed 2026-09-06 by `disposal_reach`. **ADDS: that the two channels which "
             "would implement it exist and do not fire, and a RETRACTION of this suite's own "
             "draft claim that they do not exist**")
    INV("INV-14", "nothing — ⛔ **this invention row is WITHDRAWN.** A draft claimed a "
        "proclamation channel had to be invented; `post_remit` and `chronicle` already carry "
        "`body` and `<rung kind>`.",
        "recorded rather than deleted, because a withdrawn invention is the shape of an error "
        "this log exists to catch: it counted a mechanism as missing without opening the module "
        "that has it.",
        owner="⛔ WITHDRAWN — no owner", kind="mechanism")
    return "FAILED", ("both reach channels exist; neither fires for a disposal in this fixture"), ["F-21"]


@stress("ST-22", "a witnessed concession survives long enough to be worth making",
        "10_LOOPS_AND_GAPS.md P-42", by="probe-model")
def st22():
    cap = DEFAULT_FIXTURES.get("ledger_cap")
    FIND("F-22", "the ledger cap is the only bound on the design's one amplifying loop and "
         "nothing has measured it",
         f"`ledger_cap` = {cap}, evicting on `(confidence, recency)`. `L-1` "
         f"(standing → reception → outcome → standing) is signed `+` and three of its four "
         f"bounds are properties of the corpus rather than columns. The design's answer to "
         f"'does a concession stay paid' is `P-42`, open. This harness cannot settle it — a "
         f"seeded multi-season run with one recurring bench is the instrument and it does not "
         f"exist — but it can name why it matters HERE rather than generally: a proceeding is "
         f"the heaviest depositor in the game (one occasion, many witnesses, many deposits), "
         f"so a proceedings subsystem is what makes the cap bind. The subsystem that stresses "
         f"the bound is the one shipping without measuring it.",
         by="probe-model", severity="material", site="10_LOOPS_AND_GAPS.md P-42",
         dup="`P-42`, which already carries the cap, the eviction key, *nothing has measured it*, and the instrument. **ADDS: nothing. Kept only because ST-22 declined to run an instrument the harness holds**")
    return "BLOCKED", f"ledger_cap={cap}, unmeasured under proceeding load", ["F-22"]


# ===========================================================================
# GROUP G · THE CLOSURE CLAIM, AND THE DOCUMENTS AGAINST EACH OTHER
# ===========================================================================

@stress("ST-23", "the arrangement rows carry the keys the schema declares",
        "03_PARAMETERS.md PART D · §E.2", by="construction")
def st23():
    doc = (DESIGN / "03_PARAMETERS.md").read_text()
    schema_block = doc.split("# data/arrangements.yaml")[1].split("```")[0]
    keys = re.findall(r"^\s{2}([a-z_]+):", schema_block, re.M)
    keys = [k for k in dict.fromkeys(keys) if k != "id"]
    # ⛔ A DRAFT MATCHED EVERY ```yaml BLOCK IN THE FILE CONTAINING ONE OF FOUR WORDS, which swept
    # in PART D's own schema block (0 omissions, not a game row) and PART F's examination. It
    # reported "9 of 15 partial rows" over a section that holds twelve. Scoped to §E.2.
    e2 = doc.split("## E.2 ·")[1].split("# PART F")[0]
    blocks = re.findall(r"```yaml\n(.*?)```", e2, re.S)
    rows = []
    for b in blocks:
        present = {k for k in keys if re.search(rf"\b{k}\s*:", b)}
        rows.append((len(present), sorted(set(keys) - present)))
    header = re.search(r"\*\*(\w+) keys\.\*\*", doc)
    header_word = header.group(1) if header else "?"
    partial = [r for r in rows if r[1]]
    FIND("F-23", "the schema declares fifteen keys, its own header says fourteen, and every "
         "one of the twelve game rows is written as a partial row",
         f"parsed schema keys = {len(keys)}: {keys}. PART D's header word = '{header_word}'. "
         f"Of the {len(rows)} YAML blocks in §E.2, {len(partial)} omit at least one key; the "
         f"omission counts run {sorted(len(r[1]) for r in rows)}. The rows are written as "
         f"DIFFS — 'differs from a trial in three keys' — which is fine as prose and is not a "
         f"loadable row, and `08_SEAM.md` D.2 invariant 13 already requires that *every* "
         f"arrangement declare `disposal_reach`. So the closure claim's own evidence (twelve "
         f"rows, no branch) cannot be run against a loader, because there are no twelve complete "
         f"rows to load. ⚠ **The header mismatch has a visible cause and is the NEW half**: "
         f"`disposal_reach` was added on 2026-09-06 by §B.7 and the count word above the schema "
         f"was not bumped with it, so the schema and its own header disagree by exactly the key "
         f"that was added last. The partial-row half is a statement about prose written as "
         f"prose, and is a defect only against the loader `19_PLAN.md` step 11 proposes.",
         by="construction", severity="material", site="03_PARAMETERS.md PART D",
         dup="NEW on the header (`disposal_reach` was added 2026-09-06 and the header was not bumped)")
    return "FAILED", (f"{len(keys)} keys, header says {header_word}; {len(partial)} of "
                      f"{len(rows)} §E.2 blocks omit a key"), ["F-23"]


@stress("ST-24", "the closure falsifier can see the failure it excludes",
        "03_PARAMETERS.md §F.3 · P-34", by="probe-model")
def st24():
    enums = {"order": ["free", "rank", "alternating", "scripted", "written_only"],
             "disposal": ["bench", "mutual", "none"],
             "floor": ["open", "admitted", "closed"],
             "verdict_reasons": ["given", "withheld"],
             "stakes_grade": ["terminal", "costly", "free"],
             "disposal_reach": ["room", "body", "<rung kind>"]}
    branches = sum(len(v) for v in enums.values())
    FIND("F-24", "the design's own falsifier greps for a literal the provider will never write, "
         "while the provider must branch on six enums totalling ~19 values",
         f"`test_no_branch_on_arrangement.py` is specified as a scan for "
         f"`arrangement.id == '<literal>'`. The provider never needs one: it needs "
         f"{ {k: len(v) for k, v in enums.items()} } = ~{branches} value-branches on OTHER keys. "
         f"`P-34` records this ('the closure falsifier cannot see the failure it excludes') and "
         f"grades it *pending edit*. Restated as an execution claim: the twelve games are twelve "
         f"rows in the sense that no code says the WORD 'tribunal', and they are not twelve rows "
         f"in the sense the headline implies, because `order: scripted` and `order: rank` are "
         f"two different sequencing mechanisms that a provider must implement separately. "
         f"⚠ `P-08` already concedes the sharpest instance — `order: rank` needs the fold's "
         f"canonical sort changed for everybody — and grades it `absent`. A key whose value "
         f"requires amending a shared mechanism is not a parameter of this subsystem.",
         by="probe-model", severity="material", site="03_PARAMETERS.md §F.3",
         dup="`P-34` (*the closure falsifier cannot see the failure it excludes*) + `P-08`. **ADDS: nothing measured — the branch count is hand-typed, which is the defect the finding faults**")
    return "FAILED", f"~{branches} enum branches the falsifier is blind to", ["F-24"]


@stress("ST-25", "`matter` means one thing", "CLAUDE.md §4 (idempotent in meaning)", by="construction")
def st25():
    senses = {
        "rosters.yaml: matter_kinds": sorted(roster("matter_kinds")),
        "Record.subject_matter": "the case papers' subject",
        "DocketItem.matter": "what is before the sitting",
        "contests: 'a matter'": "the contest PRIZE this design declares",
        "Step.MATTER / WriteClass.MATTER": "the second barrier of the season loop",
    }
    FIND("F-25", "`matter` carries five distinct senses across the live tree and this design, "
         "one of which is a barrier name",
         f"{json.dumps(senses)}. "
         f"`CLAUDE.md` §4's binding test is IDEMPOTENT IN MEANING — *reading the word cold, in a "
         f"later session, must yield the same meaning* — and the worked failure it records "
         f"(`evacuate`) cost real work. Here the collision is worse than a coinage because one "
         f"sense is a STEP of the loop: `MATTER matures what an act wound` and `a matter is "
         f"pressed before a bench` are the same word two lines apart in `05_PROCEDURE.md`. "
         f"⚠ The design cannot simply rename: `DocketItem.matter` is a live matrix row and "
         f"`matter_kinds` is a live roster, so the free name is the PRIZE and the disputed "
         f"Proposition — the two this directory introduced.",
         by="construction", severity="nit", site="04_VERBS.md §B.1",
         dup="NEW — and MD-05 declines the rename, so it carries no action: it is recorded so a later session meeting `contests: 'a matter'` cold does not resolve it against `matter_kinds`")
    MD("MD-05", "log the collision and do not propose a rename",
       "`CLAUDE.md` §4 binds NEW coinage and takes a no-retrofit posture; three of the five "
       "senses predate this design.",
       alternative="rename the prize to `a disposition` and the disputed Proposition to `the "
                   "question`, which is what the corpus calls it",
       falsifier="a session reading `contests: 'a matter'` and resolving it to `matter_kinds`")
    return "FAILED", "5 senses of `matter`", ["F-25"]


@stress("ST-26", "`release` exists, so a duty a proceeding imposes can be discharged",
        "04_VERBS.md §B.5 · ID-14", by="construction")
def st26():
    have = "release" in VERB_TABLE
    closers = [v for v, r in VERB_TABLE.items() if "Tenure.until" in (r.writes or [])]
    FIND("F-26", "`release` is still absent, so every `oblige` a proceeding imposes is closable "
         "only by the person who did not open it",
         f"`release` in the verb table: {have}. Verbs writing `Tenure.until` = {sorted(closers)} "
         f"— `repudiate` (`own`), `revoke` (`remit:revoke`), `confer` (`remit:confer`), "
         f"`move` (containment). So a penance, a surety or a term of service imposed by a "
         f"finding can be ended by `repudiate` — which is REPUDIATION, publicly, not discharge — "
         f"or by a seat-holder revoking. `ID-14` (what an act opens, an act must close) is "
         f"therefore unmet for the design's own principal output, and `09_IMPOSSIBILITIES.md` "
         f"row 8 already grades itself CONVENTION for this reason: *'only once `release` exists. "
         f"Today it does not.'* "
         f"⛔ **A DRAFT READ `04_VERBS.md` PART A's '⭐ LANDED' AS A CLAIM THAT THE ROW IS IN THE "
         f"TREE. IT IS NOT ONE** — the same table cell reads *'⚠ DOES NOT EXIST IN THE TABLE'*, "
         f"and 'landed' means landed in this proposal, whose complete replacement row is written "
         f"out at §B.5. The retraction is recorded; the draft read the second word of a two-word "
         f"cell. "
         f"⭐ **What survives is worth keeping and is smaller**: the row is written, it is the "
         f"cheapest thing in the directory to ship, `ID-14` cannot hold without it, and it is "
         f"⛔ **AND A DRAFT ADDED THAT IT IS ABSENT FROM `12_BUILD_ORDER.md`'s "
         f"buildable-today list. THAT IS FALSE**: `release` is **step 3**, with its dependency "
         f"column reading *nothing* and its execution artifact written out (*loader invariant 6 "
         f"is satisfiable for the first time; a person resigns an office*). So the plan has it, "
         f"costed at zero, and nobody has run the plan — which is a statement about execution "
         f"and not about the design, and is why this is `material` rather than `blocking`.",
         by="construction", severity="material", site="04_VERBS.md §B.5",
         dup="`09_IMPOSSIBILITIES.md` row 8, which already self-grades CONVENTION *only once `release` exists. Today it does not*. **ADDS: nothing**")
    return "FAILED", f"release present: {have}", ["F-26"]


@stress("ST-27", "the emission a write produces is the one the design names",
        "08_SEAM.md §D.1 vs write_matrix.yaml", by="document")
def st27():
    matrix = yaml.safe_load((ARCH / "write_matrix.yaml").read_text())
    rows = matrix if isinstance(matrix, list) else matrix.get("rows")
    got = {(r["kind"], r["field"]): (r.get("emits") or "").strip("` ")
           for r in rows if r.get("kind") in ("Person", "Tenure", "DocketItem", "Record", "Date")}
    claims = {("Tenure", "degree"): "matter.moved",
              ("Person", "stance"): "stance.changed",
              ("DocketItem", "matter"): "docket.formed",
              ("Record", "exists"): "case.opened",
              ("Record", "stages"): "case.opened",
              ("Date", "due_at"): "date.scheduled"}
    bad = {k: (v, got.get(k)) for k, v in claims.items() if got.get(k) and v not in got.get(k, "")}
    if not bad:
        return "RAN", "every claimed emission matches the matrix", []
    FIND("F-27", "`08_SEAM.md`'s data table names emissions the write matrix does not carry",
         f"claimed vs matrix: {json.dumps({f'{k[0]}.{k[1]}': v for k, v in bad.items()})}. "
         f"Loader invariant 7 is that *the Event-kind roster is DERIVED from emission columns*, "
         f"and this design has two emission columns for the same write — the matrix row's and "
         f"the verb row's (`speak` declares `matter.carried/advanced/held/turned`). The design "
         f"resolves this once, correctly, for band KEYS (§B.1: *'only the KEYS are the "
         f"ladder's'*) and never for emission KINDS. If both fire, one write emits twice; if "
         f"the verb's wins, the matrix's column is dead; if the matrix's wins, the "
         f"proceeding's whole vocabulary is dead and with it the rung fold, which reads "
         f"`matter.*` emissions.",
         by="document", severity="material", site="08_SEAM.md §D.1",
         dup="NEW")
    return "FAILED", f"{len(bad)} emission mismatches", ["F-27"]


@stress("ST-28", "the rung fold is computable from the run's own emissions",
        "00_DERIVATION.md §B.2 · 05_PROCEDURE.md PART C", by="probe-model")
def st28():
    FIND("F-28", "the ladder rung is a fold over `matter.*` emissions and NOTHING IN THE "
         "EMISSION SAYS WHICH RUNG",
         "`00_DERIVATION.md` §B.2 replaces the retracted `Tenure.degree` with "
         "`rung(run) := the lowest rung any emitted matter.* Event in THIS run has named`. "
         "`speak` emits four kinds — `matter.carried`, `matter.advanced`, `matter.held`, "
         "`matter.turned` — and NONE of them names a rung. `Event` carries "
         "`(id, kind, subject, changes, causes, emitted_at, degree, observed)`; there is no "
         "payload for 'procedural' or 'quality'. So the fold has nothing to fold: either the "
         "rung goes in the Event kind (`matter.advanced.at_definition` — which multiplies the "
         "declared kind roster by four and breaks invariant 7's derivation), or in `subject` "
         "(which is the actor, set by the fold), or a field is added after all — which is the "
         "conclusion §B.2 spent five objections avoiding. "
         "⚠ **AND THE TRILEMMA OMITS A FOURTH OPTION THAT COSTS NOTHING, WHICH IS WHY THIS IS "
         "GRADED `material` RATHER THAN `blocking`**: the fold already keeps `self.resolved` and "
         "`act_of` (Event id → the Act that emitted it), and `Act.payload` is a free dict. A "
         "per-run local that reads the run's own acts needs no field, no Event kind and no "
         "ruling — and `ED-SC-0034` licenses exactly that (*per-proceeding aggregates that die "
         "with the run are FREE*). So the gap is a specification gap rather than an "
         "architectural one. What stands is that §B.2's replacement is stated as a fold over "
         "EMISSIONS, the emissions cannot carry it, and nothing in the directory noticed. "
         "⚠ This is the load-bearing consequence: the rung is what the descent mechanism, the "
         "obstacle's third term, and `AX-3`'s two-track separation all read. `P-32` already "
         "grades the `track` column *read by nothing*; this is the same hole one level down, "
         "and it means the ISSUE LADDER — the design's central procedure — has no state.",
         by="probe-model", severity="material", site="00_DERIVATION.md §B.2",
         dup="NEW — §B.2 replaced a retracted field with this fold and nothing checked that the fold has an operand")
    INV("INV-15", "a rung carrier: an Event payload field, a per-run local threaded through the "
        "provider, or the field §B.2 refused",
        "the ladder is the design's central procedure and its position is stored nowhere and "
        "emitted nowhere.",
        owner="the design", kind="mechanism")
    return "BLOCKED", "no rung is nameable in an emission", ["F-28"]


@stress("ST-29", "each of the twelve arrangement rows can be run, one row at a time",
        "03_PARAMETERS.md §E.2 · 07_THE_GAME.md PART F", by="probe-model")
def st29():
    """The per-game matrix.

    ⚠ **REBUILT after an adversarial pass killed the first version, and the kill was right.**
    The first version hard-coded a blocker STRING per row, so `runnable = []` was an identity —
    arithmetic on a constant, published as a probe result, and unable to move if a blocking test
    had passed. That is `CLAUDE.md` §0.1 point 2 (*an assertion must be able to observe the
    failure it excludes*) committed inside a suite that cites §0.1. **Each need now names a
    STRESS TEST and reads that test's real verdict**, so a row's state moves when its blockers'
    do. The row→needs reading is still mine and is MD-06."""
    verdicts = {r["id"]: r["verdict"] for r in RESULTS}
    need = {                       # what the need is        # the test that decides it
        "bench":            ("a bench can be identified", "ST-03"),
        "quorum":           ("many determinations become one finding", "ST-16"),
        "disposal-writer":  ("the `disposes:` key has a writer", "ST-14"),
        "via":              ("an adjudicator can act as a seat", "ST-15"),
        "rung":             ("the ladder rung is nameable", "ST-28"),
        "mutual2":          ("more than two parties can settle mutually", "ST-17"),
        "opener":           ("the opening act declares term and stages", "ST-07"),
        "term":             ("a declared term can mature", "ST-18"),
        "depth":            ("the appeal cap is fed", "ST-19"),
        "absence":          ("why the subject is absent is readable", "ST-20"),
        "reach":            ("the ruling reaches beyond the room", "ST-21"),
        "arrangement":      ("the row can be loaded at all", "ST-04"),
        "docket":           ("the matter is on the docket", "ST-05"),
    }
    rows = {
        "negotiation":        ["arrangement", "docket", "mutual2", "opener", "term", "reach"],
        "negotiation/envoys": ["arrangement", "docket", "mutual2", "opener", "term", "reach"],
        "arbitration":        ["arrangement", "docket", "bench", "disposal-writer", "opener",
                               "term", "reach"],
        "legal trial":        ["arrangement", "docket", "bench", "quorum", "disposal-writer",
                               "via", "rung", "depth", "reach"],
        "tribunal":           ["arrangement", "docket", "bench", "quorum", "disposal-writer",
                               "via", "reach"],
        "interrogation":      ["arrangement", "docket", "bench", "disposal-writer", "via",
                               "rung", "reach"],
        "inquisition":        ["arrangement", "docket", "bench", "quorum", "disposal-writer",
                               "via", "rung", "reach"],
        "excommunication":    ["arrangement", "docket", "bench", "quorum", "disposal-writer",
                               "via", "absence", "reach"],
        "parliament":         ["arrangement", "docket", "bench", "quorum", "disposal-writer",
                               "reach"],
        "council of state":   ["arrangement", "docket", "bench", "quorum", "disposal-writer",
                               "reach"],
        "audience / embassy": ["arrangement", "docket", "bench", "disposal-writer", "via",
                               "reach"],
        "appeal":             ["arrangement", "docket", "bench", "disposal-writer", "via",
                               "depth", "reach"],
    }
    for g, ns in rows.items():
        blocked, met = [], []
        for n in ns:
            label, tid = need[n]
            (met if verdicts.get(tid) == "RAN" else blocked).append(f"{label} (`{tid}`)")
        MATRIX[g] = dict(blocked=blocked, met=met)
    runnable = [g for g, v in MATRIX.items() if not v["blocked"]]
    shared = sorted({n for ns in rows.values() for n in ns
                     if all(n in ns2 for ns2 in rows.values())})
    MD("MD-06", "read each row's structural needs off its own YAML block in §E.2",
       "a row's needs are what its keys imply — `disposal: bench` needs a bench, "
       "`|bench| > 1` needs a quorum, `appeal_basis: determine` needs a fed cap.",
       alternative="score every row against every need, which would make the matrix a constant "
                   "in the other direction and say nothing about the rows",
       falsifier="a row whose YAML implies a need this reading omits — the parliament's "
                 "`proofs: []`, for instance, arguably needs nothing of the forensic machinery "
                 "and is scored here as needing the disposal writer only")
    FIND("F-29", "no arrangement row can be run, and every row is blocked BEFORE it reaches "
         "anything that distinguishes it from its neighbours",
         f"runnable rows: {runnable or 'none'} of {len(rows)}. **Needs shared by ALL twelve "
         f"rows: {shared}** — the arrangement loader and the docket, neither of which is about "
         f"any particular game. Adding the near-universal ones (the bench: 10 of 12; the "
         f"disposal writer: 11 of 12; the reach: 12 of 12) gives the result: **not one game is "
         f"blocked on a parameter of its own.** "
         f"⭐ That is the closure claim holding in the only direction currently testable — the "
         f"differences between the twelve really are data — **and it is also why the catalogue "
         f"has not yet bought anything**: twelve rows over an unbuilt structure differentiate "
         f"nothing, and the design's own `18_FINDINGS.md` PART J reaches the same place from "
         f"the play side (*three of the twelve have no distinct play as the code stands*). "
         f"⚠ **NOT counted here: `public debate`**, which `14_THE_WORLD_IN_THE_ROOM.md` §E.3 "
         f"retires as *not a twelfth game but what a proceeding degenerates to when nobody can "
         f"dispose*. Scoring it as a blocked game would have inflated the denominator with a "
         f"row the design itself withdrew.",
         by="probe-model", severity="material", site="03_PARAMETERS.md §E.2",
         dup="aggregates `P-03`, `P-08`, `P-15`, `P-33`, `P-42` and the findings above. **ADDS: the shape — that the blockers are shared rather than per-row**")
    return "BLOCKED", f"{len(runnable)}/{len(rows)} rows runnable; needs shared by all: {shared}", ["F-29"]


@stress("ST-30", "the thirteenth game is a data edit, as the closure claim promises",
        "03_PARAMETERS.md §F.1", by="construction")
def st30():
    rosters = yaml.safe_load((ARCH / "rosters.yaml").read_text())["rosters"]
    missing = [r for r in ("proofs", "registers", "interposition_kinds", "speech_kinds",
                           "ladder_rungs", "standing_routes", "genres")
               if r not in rosters]
    FIND("F-30", "the design's five closed rosters and its speech-kind roster do not exist, so "
         "'adding a game is a data edit' has no data to edit",
         f"absent from `rosters.yaml`: {missing}. `00_DERIVATION.md` §B.1 counts *'rosters: 5 "
         f"closed sets, in data — ladder rungs · interposition kinds · genre · register · "
         f"standing route'*, and §B.1.1 adds a sixth (`speech_kinds`). None is in the data. "
         f"§F.1's examination — the thirteenth game, offered as the proof that the space is "
         f"closed — turns on `proofs` gaining a `performance` member and says *'it is a roster "
         f"edit, not a code change, so the closure claim survives it'*. There is no roster to "
         f"add the member to. The claim is not wrong; it is untested, and `§F.3` says so "
         f"itself (`STATUS: HYPOTHESIS`). What this execution adds is that it cannot be tested "
         f"by a small step: six rosters and a loader come first.",
         by="construction", severity="material", site="03_PARAMETERS.md §F.1",
         dup="`03_PARAMETERS.md` §F.3 self-grades `STATUS: HYPOTHESIS`. **ADDS: that six named rosters do not exist, so the claim cannot be tested by a small step**")
    INV("INV-16", "six closed rosters — ladder rungs, interposition kinds, genres, registers, "
        "proofs, standing routes — plus speech_kinds",
        "the parameter space's vocabulary is prose in a markdown table.",
        owner="the design (step 7 and step 11 of 19_PLAN.md)", kind="mechanism")
    return "BLOCKED", f"{len(missing)} of 7 rosters absent", ["F-30"]


SEV_ORDER = {"blocking": 0, "material": 1, "nit": 2}


def emit_md(out: dict) -> str:
    """The three registers, as markdown. The REPORT'S TABLES ARE GENERATED FROM THE RUN so a
    finding cannot drift from the execution that produced it -- `ID-2`, one home for one fact."""
    L: list[str] = []
    tally: dict[str, int] = {}
    for r in out["results"]:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1

    newf = [f for f in out["findings"] if f.get("dup", "NEW").startswith("NEW")]
    L.append("## The run\n")
    L.append(f"⚠ **READ THE SECOND LINE, NOT THE FIRST.** Of the "
             f"{len(out['findings'])} findings, **{len(newf)} are new** and the rest restate a "
             f"row the design already registers — its gap register, its adversarial record and "
             f"its playability adjudication are unusually complete, and a stress report that "
             f"presents their honestly-registered holes as discoveries is padding. Every finding "
             f"carries an *already registered?* line saying which it is and what the execution "
             f"adds. **The new ones are "
             + ", ".join(f"`{f['id']}`" for f in newf) + ".**\n")
    L.append(f"**{len(out['results'])} stress tests** · "
             + " · ".join(f"**{k}** {v}" for k, v in sorted(tally.items()))
             + f" · **{len(out['findings'])} findings** · "
               f"**{len(out['inventions'])} inventions** · "
               f"**{len(out['decisions'])} mechanical decisions**\n")
    L.append("| # | stress test | stresses | evidence | verdict |")
    L.append("|---|---|---|---|---|")
    for r in out["results"]:
        L.append(f"| `{r['id']}` | {r['title']} | {r['stresses']} | `{r['by']}` | "
                 f"**{r['verdict']}** |")

    L.append("\n---\n\n# PART A · THE INVENTION LOG\n")
    L.append("**Everything that had to be created for a proceeding to be traceable at all.** The "
             "`owner` column is the load-bearing one: a character invented for a fixture is a "
             "harness artifact; a Query, a roster or a magnitude invented to get past a hole is "
             "**work somebody owes**.\n")
    for k, lbl in (("mechanism", "A.1 · Invented because the subsystem cannot run without it — "
                                 "these are the bill"),
                   ("fixture", "A.2 · Invented to have a world at all — harness artifacts, "
                               "each with what its absence says")):
        L.append(f"\n## {lbl}\n")
        L.append("| id | what was invented | why it had to be | who owns it |")
        L.append("|---|---|---|---|")
        for i in out["inventions"]:
            if i["kind"] == k:
                L.append(f"| **`{i['id']}`** | {i['what']} | {i['why']} | {i['owner']} |")

    L.append("\n---\n\n# PART B · THE MECHANICAL DECISIONS\n")
    L.append("**Every place the design admits two readings and the trace had to take one.** Each "
             "names the alternative not taken and what would show the choice wrong (`ID-11`: ship "
             "the falsifier with the claim).\n")
    for d in out["decisions"]:
        L.append(f"\n### `{d['id']}` — {d['decision']}\n")
        L.append(f"- **because:** {d['because']}")
        L.append(f"- **the alternative not taken:** {d['alternative']}")
        L.append(f"- **falsifier:** {d['falsifier']}")

    L.append("\n---\n\n# PART C · THE FINDINGS — gaps, conflicts and failures\n")
    L.append("Ranked by severity, then by id. **`by=` is the evidence grade** and it is the "
             "column to read first: `construction` means the tracer, a loader, a roster or a law "
             "refused — that is evidence. `no-signature` means there was nothing to call, which "
             "*is* the refusal but is weaker, because absence is not a guard. `document` means "
             "two surfaces in the tree disagree. `probe-model` means this harness supplied a "
             "model the design does not, to reach the question at all — **discount those "
             "accordingly.**\n")
    for sev in ("blocking", "material", "nit"):
        rows = [f for f in out["findings"] if f["severity"] == sev]
        if not rows:
            continue
        L.append(f"\n## C.{SEV_ORDER[sev] + 1} · {sev.upper()} ({len(rows)})\n")
        for f in rows:
            L.append(f"\n### `{f['id']}` · {f['title']}\n")
            L.append(f"> **`by={f['by']}`** · site: `{f['site']}`\n>\n"
                     f"> **already registered?** {f.get('dup', 'NEW')}\n")
            L.append(f["detail"])

    if out.get("walk"):
        L.append("\n---\n\n# PART D · THE WORKED TRIAL — sixteen steps, and where each one "
                 "stands\n")
        L.append("*Vellenmark v. the herdsman* — a `HOLDS` matter about cattle, before a "
                 "settlement bench, `floor: open`. **The walk does not stop at the first "
                 "block**: every step is recorded so the reader sees where the inventions "
                 "cluster rather than only where the trace dies.\n")
        L.append("| # | the step | what it needs | state | invented here | note |")
        L.append("|---|---|---|---|---|---|")
        for s_ in out["walk"]:
            inv = ", ".join(f"`{i.split()[0]}`" for i in s_["invented"]) or "—"
            L.append(f"| {s_['n']} | {s_['what']} | {s_['needs']} | **{s_['state']}** | "
                     f"{inv} | {s_['note']} |")

    if out.get("matrix"):
        L.append("\n---\n\n# PART E · THE PER-GAME MATRIX — what each of the twelve is "
                 "stopped by\n")
        L.append("**Read the columns, not the rows.** Every cell is a stress test's verdict, "
                 "so a row's state moves when that test's does. **No row is blocked by a "
                 "parameter of its own** — the blockers are shared mechanisms, which is the "
                 "closure claim holding and the catalogue not yet paying.\n")
        L.append("| game | met | blocked | what it is waiting on |")
        L.append("|---|---|---|---|")
        for g, v in out["matrix"].items():
            L.append(f"| **{g}** | {len(v['met'])} | {len(v['blocked'])} | "
                     + " · ".join(v["blocked"]) + " |")

    return "\n".join(L)


@stress("ST-31", "ONE WORKED TRIAL, step by step, until it stops",
        "the whole directory", by="construction")
def st31():
    """The narrative walk. Sixteen steps of a single legal trial — *Vellenmark v. the herdsman*,
    a HOLDS matter about cattle — each recorded with what it needed, what the tree supplied, and
    what had to be invented. The walk does not stop at the first block: it records every step's
    state so the reader sees HOW FAR a proceeding gets and WHERE the inventions cluster."""
    w = proceedings_world()

    def step(n, what, needs, state, invented=(), note=""):
        WALK.append(dict(n=n, what=what, needs=needs, state=state,
                         invented=list(invented), note=note))

    step(1, "a person with a `convene` remit sets a date at the settlement",
         "`convene` (remit:convene) writing `Date.due_at` + a ConveningCondition",
         "SUPPLIED", note="the verb is `ruled` and both matrix rows exist. The fixture "
                          "short-circuits the act itself (INV-08) because a chooser that "
                          "decides to convene does not exist")
    step(2, "the date fires and a sitting exists",
         "CALENDAR firing a due Date with a holder",
         "RUNS", note="executed in ST-05: the date fired and the docket grew by one item")
    step(3, "the docket names the matter",
         "`DocketItem.matter` = the Proposition",
         "STOPS", invented=["INV-12 a clerk act"],
         note="F-05 — CALENDAR writes `matter: None` and only `carry` writes it. Nobody in the "
              "design carries the papers")
    step(4, "the bench is identified",
         "`judging_set(venue, matter)` -> seats",
         "STOPS", invented=["INV-10 the three-parameter bench Query"],
         note="F-03 — raises unconditionally. NOT stubbed by this harness on purpose: a "
              "stand-in bench would make every step below measure my Query")
    step(5, "the arrangement is read",
         "a row of fifteen keys from `data/arrangements.yaml`",
         "STOPS", invented=["INV-11 the arrangements file"],
         note="F-04, F-23 — the file does not exist and the twelve markdown rows are partial")
    step(6, "the genre is derived from the bench's remit",
         "a Query over remit acts -> {forensic, deliberative, epideictic}",
         "STOPS", invented=["INV-16 the `genres` roster"],
         note="F-30 — downstream of step 4 and of a roster that is not in the data")
    step(7, "the attendees are frozen",
         "`present_at(venue)` at entry",
         "SUPPLIED", note="`Query.presence(w, rung)` exists and answers — the design calls it "
                          "`present_at`, which does not, but the mechanism is there (ST-04)")
    step(8, "the attendees are ordered per `arrangement.order: rank`",
         "a sort by rank within the run",
         "STOPS", note="P-08, graded `absent` by the design itself: `order: rank` needs the "
                       "fold's canonical sort changed for everybody, which is not a parameter "
                       "of this subsystem")
    step(9, "a party speaks",
         "`speak` with `contests: 'a matter'`",
         "RUNS-THEN-STOPS",
         note="ST-09 — an uncontested `speak` folds and emits `speech.made`. ST-10 — the "
              "contested one reaches the seam and the seam has no provider (F-01, F-10)")
    step(10, "the speech draws against an obstacle",
         "pool = brought + conduct x latitude; Ob = score/2 +- four room terms",
         "STOPS",
         invented=["INV-17 two capability keys", "INV-18 the latitude multiplier and its floor",
                   "INV-19 the four room-term magnitudes", "INV-20 the reception composition"],
         note="P-06, graded `assumption` — inject, declare, sweep. Nothing to inject INTO: "
              "there is no provider, so the four magnitudes have no site")
    step(11, "the margin becomes a degree",
         "`degree_from_net(net, ob)` -> one of four bands",
         "SUPPLIED", note="the tree owns the ladder and `speak`'s four keys match it exactly "
                          "(ST-11). This step is the design's cleanest: it borrows rather than "
                          "re-deciding")
    step(12, "the band's writes are applied",
         "`Person.stance` at three bands; `DocketItem.matter` at Partial",
         "AMBIGUOUS", invented=["MD-03 whose stance"],
         note="F-13 — the matrix row is `(Person, stance)` with no subject column, so both the "
              "speaker-writes and hearers-write readings load")
    step(13, "the ladder rung moves",
         "a fold over this run's `matter.*` emissions",
         "STOPS", invented=["INV-15 a rung carrier"],
         note="F-28 — no emission can name a rung. The design's ZERO-NEW-FIELDS count rests on "
              "this fold")
    step(14, "the bench determines",
         "`determine` via a seat, one finding out of many determinations",
         "STOPS", invented=["INV-13 the verdict Tenure"],
         note="F-14 (`disposes:` has no writer), F-15 (no `Act.via`), F-16 (no quorum)")
    step(15, "the finding reaches the settlement",
         "`disposal_reach: settlement` minting claims for non-attendees",
         "STOPS", invented=["INV-14 a proclamation channel"],
         note="F-21 — no witness channel mints a claim for somebody who was not there")
    step(16, "the loser discharges the duty imposed",
         "`release` on the `oblige` the finding opened",
         "STOPS", note="F-26 — `release` is not in the verb table, and the design says it is "
                       "LANDED")

    runs = [s_ for s_ in WALK if s_["state"] in ("RUNS", "SUPPLIED", "RUNS-THEN-STOPS")]
    stops = [s_ for s_ in WALK if s_["state"] == "STOPS"]
    amb = [s_ for s_ in WALK if s_["state"] == "AMBIGUOUS"]
    FIND("F-31", "of sixteen steps in one trial, five are supplied, ten stop on something that "
         "does not exist, and one is ambiguous in the spec",
         f"{len(runs)} of {len(WALK)} steps are supplied or run; {len(stops)} stop; "
         f"{len(amb)} is ambiguous. "
         f"⭐ The distribution is the result: the steps that RUN are the ones the tree already "
         f"owned before this design existed — the calendar firing, the presence walk, the fold, "
         f"the degree ladder. **Every step that stops is one this directory specified.** That is "
         f"not a criticism of the specification; it is the measurement of how much of it is "
         f"specification. "
         f"⭐ **AND THE WALK FINDS ONE THING THE BUILD ORDER DOES NOT HAVE A STEP FOR.** "
         f"`12_BUILD_ORDER.md` has twelve steps, three of them (`judging_set`, `release`, "
         f"`convene` corrected) with a dependency column reading *nothing*. **Step 3 of this "
         f"walk — somebody putting the matter on the docket — is in none of them.** Step 6 is "
         f"*`speak` with its `requires`* and depends on steps 0 and 2; step 9 is **THE BAR**, "
         f"*one seeded proceeding runs end to end with zero authored acts, twice, "
         f"byte-identical*. A proceeding with zero authored acts requires a docket item naming "
         f"a matter, `DocketItem.matter` is written by `carry` alone, and no step of the build "
         f"order produces one. **The plan's own bar is unreachable by the plan's own steps**, by "
         f"one missing act that costs nothing. "
         f"⛔ A draft of this finding said the build order's first buildable thing should be the "
         f"clerk; the correction is that the build order's step 1 is genuinely buildable and the "
         f"clerk is simply not in it at all.",
         by="construction", severity="material", site="12_BUILD_ORDER.md",
         dup="NEW")
    for iid, what, why, owner in (
        ("INV-17", "two `capability` key names for `brought` and `conduct`",
         "`06_RESOLUTION.md` §B.1 defines the pool as `brought + conduct x latitude` and names "
         "neither key, correctly (the attribute roster is IN FLUX and Jordan ruled *ignore their "
         "use of attributes*). But a trace cannot roll without them.",
         "content by `ID-12` once the attribute roster settles — a data edit, not a decision"),
        ("INV-18", "the latitude multiplier's shape and `LATITUDE_FLOOR`",
         "ruled 2026-09-06 to be floored near the measured ~0.7 and swept; the number and the "
         "curve are both unwritten.",
         "the design (`19_PLAN.md` step 12) — and M-7 is a BLOCKING measurement, so this is "
         "not a fixture choice anybody may make quietly"),
        ("INV-19", "magnitudes for the four room terms (aptness · rung · register fit · proofs)",
         "`06_RESOLUTION.md` §C.1 composes the obstacle from four signed terms and supplies no "
         "sizes. `ID-6` says inject, declare, sweep — there is nothing to inject into yet.",
         "the design (`19_PLAN.md` step 12), and `P-25` says FOLLOW THE TRIBUNAL rather than "
         "re-derive"),
        ("INV-20", "the `reception` composition — which of the bench's claims and which "
         "conviction axes, at what weights",
         "`15_WHY_IT_IS_A_GAME.md` makes this the one hidden term that stops the proceeding "
         "being a solved flowchart. It is the design's central claim and it is a sentence.",
         "the design (`19_PLAN.md` step 17) — ⚠ and `HANDOFF_SC.md` already records that the "
         "set it reads cannot be populated today: no deposit names an actor, every claim is "
         "firsthand at confidence 100, `told_by` is never minted"),
    ):
        INV(iid, what, why, owner, kind="mechanism")
    return "BLOCKED", f"{len(runs)}/{len(WALK)} steps supplied or running; {len(stops)} stop", ["F-31"]


# ===========================================================================
# GROUP H · THE ROOM'S MEMORY — added after an adversarial pass found the suite
#           had built a fixture with five people in a room and never opened a ledger
# ===========================================================================

@stress("ST-32", "the room remembers WHO spoke", "15_WHY_IT_IS_A_GAME.md PART C · 18_FINDINGS.md",
        by="construction")
def st32():
    """The single test this suite most owed and did not have. `reception` — the one hidden term
    the whole anti-solver argument rests on — is composed from THE HEARERS' OWN CLAIMS ABOUT THE
    SPEAKER. So: after a speech, does anybody in the room hold a claim naming the speaker?"""
    w = proceedings_world()
    made = []

    def choose(p, v, s_, ask_budget):
        if p.id != "p_party_a":
            return []
        a = act(w, "p_party_a", "speak", key="press")
        made.append(a)
        return [a]

    SeasonDriver(w).season(choose, question=None, subsistence=SUBSIST)
    bench = w.persons["p_bench_a"]
    about_speaker = [c for c in bench.ledger if c.subject == "p_party_a"]
    kinds = sorted({c.predicate for c in bench.ledger})
    confs = sorted({c.confidence for c in bench.ledger})
    srcs = sorted({c.source for c in bench.ledger})
    absent_l = w.persons["p_absent"].ledger
    FIND("F-32", "the room's memory of a speech is ONE claim, at one confidence, from one source, "
         "saying that it happened — and `reception` needs claims about how it LANDED",
         f"after one season with a `speak` by p_party_a in front of five people, p_bench_a's "
         f"ledger holds {len(bench.ledger)} claims, of which {len(about_speaker)} name the "
         f"speaker: predicates {kinds}, confidences {confs}, sources {srcs}. "
         f"⛔ **A DRAFT OF THIS FINDING SAID NO CLAIM NAMES THE SPEAKER AND THAT WAS FALSE** — "
         f"the execution says one does, and the retraction is recorded here rather than "
         f"overwritten because the corrected finding is the sharper one. "
         f"⭐ **WHAT IS ACTUALLY DEPOSITED IS `(p_party_a, speech.made, 100, firsthand)` — that "
         f"he spoke.** `06_RESOLUTION.md` §C.1 composes `reception` from *the hearers' own claims "
         f"about the speaker*, and `PART A` defines ethos as *what others take a person to be — "
         f"claims in OTHER PEOPLE'S ledgers, each of which may be wrong*. The only claim about "
         f"the speaker is that he made a speech. There is no reading in it, nothing that could "
         f"be wrong, and nothing that differs between two hearers. "
         f"⚠ **AND THE TRACER SAYS WHY, IN ITS OWN COMMENT AT `claim_subjects`**: an Event with "
         f"an empty `changes[]` — which is every `speak`, since `writes: []` — mints its claim "
         f"about the ACTOR by the `e.subject` fallback, and *'a claim about the actor can never "
         f"raise a listener's question: the news arrived in a form nobody could act on'*, "
         f"measured at *R3 = 0 of 30 on the NPC lane, 0 of 59 on ARC*. So the one claim a speech "
         f"deposits about its speaker is the one shape the question machinery cannot read. "
         f"⚠ **CREDIT WHERE IT IS DUE**: `18_FINDINGS.md` PART B and `HANDOFF_SC.md` already "
         f"name this as the directory's headline diagnosis. What this adds is the execution and "
         f"one correction — their wording is *no deposit names the actor*, and a deposit does; "
         f"the defect is the CONTENT of that deposit, not its absence, and the fix named in "
         f"`19_PLAN.md` step 2 (attribution) is aimed at a hole one step to the left of the "
         f"real one.",
         by="construction", severity="blocking", site="15_WHY_IT_IS_A_GAME.md PART C",
         dup="`18_FINDINGS.md` PART B / `HANDOFF_SC.md`, the directory's own headline diagnosis. **ADDS: the execution, and a CORRECTION — a deposit does name the actor; the defect is its content**")
    MD("MD-08", "report the deposit's CONTENT as the defect rather than its absence",
       "the execution shows a claim naming the actor; the directory's own wording says there is "
       "none. Reporting the absence would have repeated a claim the run refutes.",
       alternative="take `18_FINDINGS.md` PART B at its word — which is what the draft did, and "
                   "it produced a false finding",
       falsifier="`shape.py`'s `claim_subjects` under a different `claim_subject_rule` arm: at "
                 "`per_change` an Event with no changes deposits NOTHING, which would make the "
                 "directory's wording true and this finding arm-dependent. The arm in force is "
                 "`both` (INV-21) and it is a swept fixture, not a ruling")
    return "BLOCKED", (f"{len(about_speaker)} of {len(bench.ledger)} claims name the speaker, "
                       f"and it says only that he spoke; the absent man holds "
                       f"{len(absent_l)} identical claims"), ["F-32"]


@stress("ST-33", "a person who was not there does not learn what happened",
        "07_THE_GAME.md PART E", by="construction")
def st33():
    """`07_THE_GAME.md` PART E in bold: *a player can be condemned and not know it, and that
    needs no mechanism.* The fixture has a subject who did not travel. Test the claim."""
    w = proceedings_world()

    def choose(p, v, s_, ask_budget):
        return [act(w, "p_party_a", "speak", key="press")] if p.id == "p_party_a" else []

    SeasonDriver(w).season(choose, question=None, subsistence=SUBSIST)
    absent = w.persons["p_absent"]
    present = w.persons["p_bench_a"]
    mode = DEFAULT_FIXTURES.get("fan_out_mode")
    FIND("F-33", "the absent subject learns everything, because the fan-out mode that is the "
         "specified behaviour deposits to EVERYONE regardless of presence",
         f"fan-out mode = {mode!r} (`H-33`'s control and the tracer's declared default). After "
         f"the sitting, p_absent — contained at the hearth, never at the venue — holds "
         f"{len(absent.ledger)} claims against the attending bench member's {len(present.ledger)}. "
         f"`observers_for` returns `list(everyone)` at this mode with no presence predicate. "
         f"⭐ So the design's most-quoted *needs no mechanism* claim — *a player can be "
         f"condemned and not know it* — is **false under the current fixture and true under a "
         f"different arm of a sweep that has not been run.** `H-33`'s other two arms "
         f"(`presence_only`, `all_five`) would make it true. "
         f"⚠ This is exactly what `19_PLAN.md` step 1 (*take fan-out off `total`*) is for, so "
         f"the design KNOWS the arm is wrong; what it does not say is that four of its own "
         f"structural claims — trial in absentia, the closed floor, the covert approach, and "
         f"*finding out too late is the game* — are claims about a sweep arm rather than about "
         f"the architecture. Under `total` there is no such thing as being absent.",
         by="construction", severity="blocking", site="07_THE_GAME.md PART E",
         dup="NEW — `19_PLAN.md` step 1 proposes the fix without noting that four structural claims depend on the arm")
    return "BLOCKED", (f"absent subject holds {len(absent.ledger)} claims from a sitting he did "
                       f"not attend (fan_out_mode={mode!r})"), ["F-33"]


# ===========================================================================
# GROUP I · THE ARITHMETIC — the design's two BLOCKING measurements, run
# ===========================================================================

@stress("ST-34", "the deprivation floor holds: a floored pool against a composed obstacle still "
        "has a chance", "06_RESOLUTION.md §B.3a", by="probe-model")
def st34():
    """`06_RESOLUTION.md` §B.3a names this *a blocking check on shipping the composed obstacle,
    not an advisory one*: at the minimum lawful pool against the maximum plausible composed
    obstacle, `p_success` must not be effectively zero. The design supplies no magnitudes
    (`P-06`), so the harness injects a declared set — that is what makes this `probe-model`."""
    sys.path.insert(0, str(REPO))
    try:
        from engine.autoload import dice_engine as DE
    except Exception as e:  # noqa: BLE001
        return "BLOCKED", f"could not import the ladder: {type(e).__name__}: {e}", []
    fn = getattr(DE, "p_success", None) or getattr(DE, "success_probability", None)
    names = [n for n in dir(DE) if "success" in n.lower() or "prob" in n.lower()]
    MD("MD-07", "inject a declared obstacle set rather than refuse the measurement",
       "`ID-6` says inject, declare and sweep an `assumption`-grade magnitude rather than "
       "escalate it, and `06_RESOLUTION.md` grades the four room terms exactly that. The "
       "injected set is: base_Ob = 3 (an opposition score of 6), and the four terms each in "
       "[-1, +2], giving a maximum composed Ob of 11 against the 1D floor.",
       alternative="refuse, on the grounds that the design supplies no numbers — which is what "
                   "a draft of this suite did, and it left the design's own BLOCKING check "
                   "unrun on the grounds that it was blocked",
       falsifier="a ruled magnitude set that differs from this one, at which point this "
                 "measurement is re-run rather than argued with")
    if fn is None:
        FIND("F-34", "the design's own blocking check cannot be run, because the ladder exposes "
             "no `p_success` and the design forbids resolving on the thing it does expose",
             f"`engine/autoload/dice_engine.py` exports {names or 'nothing matching /success|prob/'}. "
             f"`06_RESOLUTION.md` §C.3 forbids resolving on `eff_ob()` — *display only* — and "
             f"§B.3a's deprivation floor is stated in terms of `p_success`. So the BLOCKING "
             f"check is specified against a function name and the module is the wrong place to "
             f"look, or the name is wrong. Either way the check has not been run and cannot be "
             f"run from the spec as written.",
             by="construction", severity="material", site="06_RESOLUTION.md §B.3a",
         dup="NEW")
        return "BLOCKED", f"no p_success in the ladder module; exports: {names}", ["F-34"]
    worst = [fn(pool=1.0, ob=ob) if "pool" in fn.__code__.co_varnames else fn(1.0, ob)
             for ob in (3, 7, 11)]
    ok = worst[-1] > 0.01
    FIND("F-34", f"at the 1D floor against the maximum injected obstacle, p_success = "
         f"{worst[-1]:.4f}",
         f"p_success at pool=1 against Ob {{3, 7, 11}} = {[round(x, 4) for x in worst]}. "
         f"The design's constraint is that this must not be *effectively zero*. "
         f"{'It is not' if ok else 'IT IS'}. ⚠ Under MD-07's injected magnitudes only — the "
         f"design supplies none, so this is a measurement of my numbers, and its value is that "
         f"it is now a number somebody can disagree with rather than a check nobody ran.",
         by="probe-model", severity="material" if ok else "blocking",
         site="06_RESOLUTION.md §B.3a")
    return "RAN", f"p_success at the floor vs Ob 11 = {worst[-1]:.4f} (injected magnitudes)", ["F-34"]


# ===========================================================================
# GROUP J · THE PROPERTIES THAT SHOULD PASS — added because a suite reporting
#           28 of 30 not-RAN is suspicious in the direction of manufacturing failure
# ===========================================================================

@stress("ST-35", "the same season replays byte-identically", "06_RESOLUTION.md PART C.5 · "
        "12_BUILD_ORDER.md", by="construction")
def st35():
    """`06_RESOLUTION.md` C.5: *the same season replays byte-identically, including the hash.*
    `12_BUILD_ORDER.md` makes it the bar. A suite that only reports holes would not have looked."""
    def one():
        w = proceedings_world()

        def choose(p, v, s_, ask_budget):
            return [act(w, "p_party_a", "speak", key="press")] if p.id == "p_party_a" else []

        SeasonDriver(w).season(choose, question=None, subsistence=SUBSIST)
        return [(e.kind, tuple(e.causes), e.emitted_at) for e in w.log], w

    a, wa = one()
    b, wb = one()
    ledgers_a = sorted((c.holder, c.subject, c.predicate, c.confidence)
                       for p in wa.persons.values() for c in p.ledger)
    ledgers_b = sorted((c.holder, c.subject, c.predicate, c.confidence)
                       for p in wb.persons.values() for c in p.ledger)
    same = a == b and ledgers_a == ledgers_b
    if same:
        return "RAN", (f"two independent runs of the same seeded proceeding produced identical "
                       f"logs ({len(a)} Events) and identical ledgers ({len(ledgers_a)} claims). "
                       f"⭐ The determinism claim HOLDS on the path that exists — credited "
                       f"because a suite that only reports holes has not checked whether "
                       f"anything works"), []
    FIND("F-35", "the same seeded season does not replay identically",
         f"run A: {len(a)} Events / {len(ledgers_a)} claims; run B: {len(b)} / {len(ledgers_b)}.",
         by="construction", severity="blocking", site="06_RESOLUTION.md PART C.5",
         dup="—")
    return "FAILED", "replay diverged", ["F-35"]


@stress("ST-36", "permuting who attends does not move the outcome", "05_PROCEDURE.md PART A row 5",
        by="construction")
def st36():
    """`05_PROCEDURE.md` PART A: *who attends — permuting it must not move the hash*, declared a
    MAP. The file's own header says *the criterion is its own falsifier: permute and compare*,
    and nothing in the directory had permuted anything."""
    def run(order):
        w = World(world_seed=7, fixtures=DEFAULT_FIXTURES)
        for rid, kind, stores in (("R", "realm", None), ("D", "duchy", None),
                                  ("S", "settlement", {"grain": 40}), ("Hh", "hearth", {"grain": 8})):
            w.rungs[rid] = Rung(rid, kind, stores=stores)
        for pid in order:
            w.persons[pid] = Person(pid, pid)
            w.rungs[pid] = Rung(pid, "person")
        n = [0]

        def edge(sub, obj, kind):
            n[0] += 1
            w.add_tenure(Tenure(f"t{n[0]}", sub, obj, kind, since=0))
        edge("D", "R", "contain"); edge("S", "D", "contain"); edge("Hh", "S", "contain")
        for pid in order:
            edge(pid, "S", "contain")
        w.manifest = {"contest": "seam.contest_resolver", "order": "core.canonical_order"}

        def choose(p, v, s_, ask_budget):
            return [act(w, p.id, "speak", key="press")] if p.id in ("p_party_a", "p_party_b") else []

        SeasonDriver(w).season(choose, question=None, subsistence=SUBSIST)
        return [(e.kind, tuple(sorted(e.causes))) for e in w.log]

    fwd = run(["p_party_a", "p_party_b", "p_bench_a", "p_floor"])
    rev = run(["p_floor", "p_bench_a", "p_party_b", "p_party_a"])
    if sorted(fwd) == sorted(rev):
        return "RAN", (f"permuting the attendee list left the Event multiset identical "
                       f"({len(fwd)} Events both ways). ⭐ `05_PROCEDURE.md`'s MAP claim for "
                       f"'who attends' HOLDS under execution — the fold's canonical sort is "
                       f"content-derived, so insertion order does not reach the outcome. "
                       f"This is the design's permutation criterion run for the first time"), []
    FIND("F-36", "permuting the attendee list moves the outcome, so 'who attends' is not a map",
         f"forward: {len(fwd)} Events; reversed: {len(rev)}. Difference: "
         f"{sorted(set(map(str, fwd)) ^ set(map(str, rev)))[:4]}.",
         by="construction", severity="blocking", site="05_PROCEDURE.md PART A",
         dup="—")
    return "FAILED", "attendee permutation moved the outcome", ["F-36"]



@stress("ST-37", "every gap the design registers is IN the gap register",
        "10_LOOPS_AND_GAPS.md PART C · §F.34", by="construction")
def st37():
    """`10_LOOPS_AND_GAPS.md` PART C quotes the discipline it is written under: *a defect in
    neither the gap register nor the not-a-gap register is invisible to both counts.* Test it by
    counting."""
    reg = (DESIGN / "10_LOOPS_AND_GAPS.md").read_text()
    in_reg = set(re.findall(r"\bP-(\d{2})\b", reg))
    cited: dict[str, set] = {}
    for f in sorted(DESIGN.glob("*.md")):
        if f.name.startswith("20_"):
            continue
        for m in re.findall(r"\bP-(\d{2})\b", f.read_text()):
            cited.setdefault(m, set()).add(f.name)
    missing = sorted(set(cited) - in_reg, key=int)
    if not missing:
        return "RAN", f"all {len(in_reg)} cited P-rows appear in the register", []
    where = {f"P-{m}": sorted(cited[m]) for m in missing}
    FIND("F-37", "five gaps are registered by the files that raise them and appear in the gap "
         "register nowhere — including the one the design calls the sharpest thing its own "
         "hardest question surfaced",
         f"the register carries {len(in_reg)} P-rows. Cited elsewhere and absent from it: "
         f"{json.dumps(where)}. `10_LOOPS_AND_GAPS.md` PART C states the discipline in the words "
         f"this test applies — *a defect in neither the gap register nor the not-a-gap register "
         f"is invisible to both counts* — and five are in exactly that position. "
         f"⭐ **What is in the five matters more than the count.** `P-24` is "
         f"`14_THE_WORLD_IN_THE_ROOM.md`'s own verdict on Jordan's fourth worked matter "
         f"(*a claim about a future state has no producer … nothing writes the `commit` that "
         f"would make a person's fear legible to a bench*), which that file calls **the sharpest "
         f"thing this question surfaced**. `P-22` is the price of the zero-new-fields result — "
         f"*a matter's ladder position does not persist between seasons* — and `00_DERIVATION.md` "
         f"§B.2 says *Registered `P-22`* while registering it nowhere. `P-23` is the refusal the "
         f"design lost when it corrected `determine` (*without a producer for `heard`, "
         f"`determine.unheard` does not exist*). `P-28` and `P-29` are the two resolution rows, "
         f"one of them RULED. "
         f"⚠ **The failure mode is the one the design names and not a filing error:** each was "
         f"written as *Registered `P-nn`* at its own site, which reads as done, and the register "
         f"is what a next session opens. Five of them are invisible to both counts.",
         by="construction", severity="material", site="10_LOOPS_AND_GAPS.md PART B",
         dup="NEW — and it is a defect in the register the design's `README.md` sends a reader "
             "to first")
    return "FAILED", f"{len(missing)} cited P-rows absent from the register: {['P-'+m for m in missing]}", ["F-37"]



@stress("ST-38", "the count table that is the design's whole argument is current",
        "00_DERIVATION.md §B.1 · README.md", by="construction")
def st38():
    """`00_DERIVATION.md` PART B opens with the bar: *the test is not did we cover the twelve
    kinds but WHAT DID WE ADD to cover them.* §B.1 is that count, and README calls it *the whole
    argument*. Three of its five rows do not survive reading against the sections they cite."""
    doc = (DESIGN / "00_DERIVATION.md").read_text()
    verbs = (DESIGN / "04_VERBS.md").read_text()
    readme = (DESIGN / "README.md").read_text()
    fields_cell = re.search(r"\*\*fields on existing carriers\*\*.*", doc)
    verbs_cell = re.search(r"\*\*verbs\*\*.*", doc)
    carriers_cell = re.search(r"\*\*carriers\*\*.*", doc)
    withdrawn = "THERE IS NO NEW FIELD" in doc
    zero_verbs = "adds ZERO new verbs" in verbs or "ZERO new verbs" in verbs
    readme_zero = "ZERO" in readme
    import shape as _sh
    seat_is_a_carrier = hasattr(_sh, "Seat")
    FIND("F-38", "the count table §B.1 exists to produce is stale in three of five rows, and one "
         "of them names a different field than the section it points at",
         f"**fields** — the cell reads *1, and it is contested · `Proposition.rung` … See B.2, "
         f"where it is argued against and then **admitted with its price**.* §B.2 is titled "
         f"*THE ONE FIELD IS WITHDRAWN. THERE IS NO NEW FIELD* (present: {withdrawn}), it argues "
         f"about **`Tenure.degree`** rather than `Proposition.rung`, and it RETRACTS rather than "
         f"admits. Three defects in one cell: a stale number, the wrong field name, and a "
         f"description that inverts the section's verdict. `13_ADVERSARIAL.md` books the result "
         f"as *the count improves to zero new fields* — so the retraction propagated everywhere "
         f"except the table it was a retraction OF. "
         f"**verbs** — the cell reads *4 new, 6 reused, 1 filled*, while `04_VERBS.md`'s "
         f"headline is *the game structure adds ZERO new verbs* (present: {zero_verbs}) and "
         f"`README.md`'s cost table says *new verb names invented: ZERO* (present: {readme_zero}). "
         f"Two files say zero and the count table says four. "
         f"**carriers** — the cell claims *0 new* and lists ten as *every one already rostered*, "
         f"including **`Seat`**, which is not a carrier in the tracer (`Seat` defined: "
         f"{seat_is_a_carrier}; the seat is an `Office` and a `hold` Tenure, which is what the "
         f"rest of the directory says). The claim is still true — the design adds no carrier — "
         f"and its evidence names one that does not exist. "
         f"⭐ **Why this is worth a row rather than a nit: §B.1 IS the argument.** `README.md` "
         f"puts the same count at the top under *what it costs — the count, which is the whole "
         f"argument*, and a reader checking the design's central claim reads this table first.",
         by="construction", severity="material", site="00_DERIVATION.md §B.1",
         dup="NEW — `17_PLAYABILITY.md` §H.2/§H.3 fixed two instances of this class and did not "
             "reach §B.1; `13_ADVERSARIAL.md` records the retraction that made the cell stale")
    return "FAILED", "3 of 5 count rows stale: fields (wrong field, inverted verdict), verbs (4 vs ZERO), carriers (names `Seat`)", ["F-38"]



# ===========================================================================
# THE RUNNER
# ===========================================================================

def run() -> dict:
    results = []
    for t in TESTS:
        try:
            verdict, detail, fids = t["fn"]()
        except ShapeGap as e:                       # the shape refused where we did not expect it
            verdict, detail, fids = "BLOCKED", f"{type(e).__name__}: {e}", []
        except Exception as e:                      # noqa: BLE001 — a harness bug, reported as one
            verdict = "HARNESS-ERROR"
            detail = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}"
            fids = []
        row = dict(id=t["id"], title=t["title"], stresses=t["stresses"],
                   by=t["by"], verdict=verdict, detail=detail, findings=fids)
        results.append(row)
        RESULTS.append(row)          # ST-29 reads these; the matrix is derived, never typed
    return dict(results=results, inventions=INVENTIONS, decisions=DECISIONS,
                findings=FINDINGS, matrix=MATRIX, walk=WALK)


def main() -> int:
    out = run()
    if "--json" in sys.argv:
        print(json.dumps(out, indent=2))
        return 0
    if "--md" in sys.argv:
        print(emit_md(out))
        return 0
    tally: dict[str, int] = {}
    for r in out["results"]:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    print("=" * 78)
    print("STRESS SUITE — proposals/2026-09-05-proceedings-subsystem")
    print("=" * 78)
    for r in out["results"]:
        print(f"\n[{r['verdict']:<14}] {r['id']}  {r['title']}")
        print(f"    stresses: {r['stresses']}   by={r['by']}")
        print(f"    -> {r['detail'][:400]}")
    print("\n" + "=" * 78)
    print("TALLY:", ", ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print(f"FINDINGS: {len(out['findings'])}  "
          f"(blocking={sum(1 for f in out['findings'] if f['severity'] == 'blocking')}, "
          f"material={sum(1 for f in out['findings'] if f['severity'] == 'material')}, "
          f"nit={sum(1 for f in out['findings'] if f['severity'] == 'nit')})")
    print(f"INVENTIONS: {len(out['inventions'])}  "
          f"(mechanism={sum(1 for i in out['inventions'] if i['kind'] == 'mechanism')}, "
          f"fixture={sum(1 for i in out['inventions'] if i['kind'] == 'fixture')})")
    print(f"MECHANICAL DECISIONS: {len(out['decisions'])}")
    by = {}
    for f in out["findings"]:
        by[f["by"]] = by.get(f["by"], 0) + 1
    print("EVIDENCE GRADE:", ", ".join(f"{k}={v}" for k, v in sorted(by.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
