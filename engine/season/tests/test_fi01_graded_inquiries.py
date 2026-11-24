"""v9 FI-01 (`ED-FI-0009`; J-22 answered option (A)) -- a degree producer for the inquiries, and the
deposit half built as the SKIP arm (RS-21 item 1, H-111 ANSWERED [medium; Jordan to correct]).

Built: the `graded_inquiries` routing roster (`research`, `examine`, `surveil`'s place case; `interview` is
a prompt, K-36, and `reconstruct`/`thread_read` wait, K-37/H-85), its loader and construction checks, the
roll through `seam/contest.py::grade` and the `social_contest` entry, and the SKIP arm
(`undeposited_kinds`: `finding.none` fans to nobody at WITNESS). The design is in `rosters.yaml`.

THE FALSIFIERS (the position's, `workplans/valoria_master_workplan_v9_part6.md` FI-01):
  * a `Failure` inquiry, seeded at the shipped fixtures, deposits no claim -- no `claim.deposited` caused
    by its `finding.none`, no ledger moves -- and a refused one likewise; the control is that a
    `news.untold` still deposits, and a graded `finding.made` deposits (the arm is keyed on the KIND);
  * the route is not readable as a prize (`test_the_route_is_not_readable_as_a_prize`);
  * the degree follows the one owner: the module entry replaced, the inquiry's band moves with it; and
    the host producer scan returns a planted inquiry resolver
    (`test_season_shape.py::test_a_verb_is_graded_by_a_contest_or_by_its_task_draw_and_by_nothing_else`, where the
    scan's own helper is run over the plant).
"""

from __future__ import annotations

import copy
import dataclasses
import unittest.mock as mock

import pytest
import yaml

from ..data import rosters as _rosters
from ..data import verbs as VERBS
from ..data.matrix import Step, WriteClass
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import GRADED_TASKS, UNDEPOSITED_KINDS, graded_route, roster_map
from ..data.verbs import VERB_TABLE
from ..data.requires import binding_from_act, evaluate
from ..gaps import Unspecified
from ..harness import populated as POP
from ..boot.realm import build_realm
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..manifest import MODULE_ENTRIES, check_graded_tasks, resolve as manifest_resolve
from ..queries.inputs import Margin
from ..queries.person_q import said_of
from ..queries.world_q import WorldReader
from ..state.carriers import Act, Claim, Record, Site

# The six acts canon names (`verb_table.yaml`'s block comment), and the position's partition of them:
# one prompt, two waiting, and the rest graded -- derived, so the graded set is not a second copy of
# `graded_inquiries` (`test_season_shape.py::test_jordan_no_definition_is_hardcoded_in_a_body` (retired)).
INQUIRIES = ("examine", "interview", "research", "surveil", "thread_read", "reconstruct")
WAITING = {"thread_read": "K-37 (no value space; its H-85 carrier landed at v9 PC-06 K-3)"}
# B07 (UNDECIDED (2)): `reconstruct` is `form: inquiry` and band-keyed, routed only with `task_draw_arm` on, so with the arm off (the
# three CARRIED inquiries' world) it is neither graded nor waiting-and-flat: its K-37 limit is superseded by that ruling.
ARMED = {"reconstruct": "form: inquiry since B07 (UNDECIDED (2)), routed only with the arm on"}
PROMPT = "interview"
GRADED = {v for v in INQUIRIES if v != PROMPT and v not in WAITING and v not in ARMED}
REC, ACTOR = "rec_fi01", "p_low"


def _world():
    """`tiny_world` at the shipped fixtures, one documentary Record in `Hh` for `research` to consult."""
    w = P.tiny_world()
    w.records[REC] = Record(REC, "Hh", "text")
    return w, SeasonDriver(w)


def _resolve(w, d, *acts):
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _witness(w, d, events):
    """WITNESS over `events`; returns `(ledgers before, ledgers after)` as id tuples per person."""
    before = {pid: tuple(c.id for c in p.ledger) for pid, p in w.persons.items()}
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), events)
    after = {pid: tuple(c.id for c in p.ledger) for pid, p in w.persons.items()}
    return before, after


def _deposits_caused_by(w, eid) -> list:
    return [e for e in w.log if e.kind == "claim.deposited" and eid in e.causes]


def test_the_rosters_name_three_graded_and_the_skip_names_finding_none():
    """The routing roster grades exactly the three the position builds and names none that waits; the
    skip arm is keyed on the one kind. A row that waits keeps a flat `emits:`, so it cannot be graded."""
    # B07.01: the roster is `graded_tasks`; the routes LIVE at the shipped fixtures are the three (the armed rows,
    # `reconstruct` and `thread_read` among them, are taken only with `task_draw_arm` on, `graded_route`).
    # B07.05 ships the arm on, so every armed route is live at the shipped fixtures; the three CARRIED inquiries are the routes live with it off.
    live = {v for v in GRADED_TASKS if graded_route(v, DEFAULT_FIXTURES.sweep("task_draw_arm", "off")) is not None}
    assert live == set(GRADED), sorted(live)
    assert UNDEPOSITED_KINDS == frozenset({"finding.none", "inquiry.refused"}), UNDEPOSITED_KINDS   # B11.12: the refusal is its own kind
    for verb in GRADED:
        row = VERB_TABLE[verb]
        assert set(row.emits_by_degree) == {"Overwhelming", "Success", "Partial", "Failure"}, verb
        assert row.emits_at("Failure") == ("finding.none",) and "inquiry.refused" in row.emits_on_refusal
    off = DEFAULT_FIXTURES.sweep("task_draw_arm", "off")
    for verb in (PROMPT, *WAITING):
        assert graded_route(verb, off) is None and not VERB_TABLE[verb].emits_by_degree, (
            f"{verb!r} is graded, and it is a prompt or waits ({WAITING.get(verb, 'K-36')})")
    for verb in ARMED:       # armed: not routed with the arm off, graded (band-keyed) by the row once armed
        assert graded_route(verb, off) is None and graded_route(verb, DEFAULT_FIXTURES) is not None, verb


def test_a_failed_inquiry_deposits_no_claim_and_news_untold_still_does():
    """THE SKIP ARM, ON A SEEDED CASE (B11.12: the name is the test's first form; a FAILED inquiry now deposits to its actor alone and a
    REFUSED one to nobody). `research` at the shipped fixtures (`pool_default` 2 against the
    module's stand-in `opposed_ob(pool_default, opposition_rate)`): the act ids are swept until one draws `Failure` and one draws a finding
    band; each is resolved through the real driver and witnessed. The `Failure` act emits `finding.none`
    with the degree on it and NOTHING lands in any ledger -- no `claim.deposited` names it; the finding
    act's `finding.made` does deposit (the arm reads the kind, not the act). A REFUSED research (no such
    Record) likewise deposits nothing. THE CONTROL: a refused `tell` (`tell.refused`, a keyed kind `tell`
    declares; `news.untold` before CP-T05-03) deposits as before.

    MUTATION (run 2026-10-17, reverted): `undeposited_kinds` emptied in `loop/witness.py`'s filter (the
    `events = [...]` line made a no-op) -- the failed research deposits, and the first ledger assertion
    goes RED."""
    found: dict = {}
    for n in range(60):
        w, d = _world()
        a = Act(id=f"a_fi01_research_{n}", actor=ACTOR, verb="research", payload={"subject": REC})
        out = _resolve(w, d, a)
        assert len(out) == 1, [(e.kind, e.degree) for e in out]
        band = "Failure" if out[0].degree == "Failure" else "finding"
        found.setdefault(band, (w, d, out))
        if len(found) == 2:
            break
    assert set(found) == {"Failure", "finding"}, f"60 act ids drew only {sorted(found)}"

    w, d, out = found["Failure"]
    (ev,) = out
    assert (ev.kind, ev.degree) == ("finding.none", "Failure"), (ev.kind, ev.degree)
    before, after = _witness(w, d, out)
    # B11.12 (A-81): the failed inquiry leaves its ACTOR's claim and no bystander's (`test_fi_small_edits.py` owns the control arm).
    assert {p for p in before if before[p] != after[p]} == {ACTOR}, "a Failure inquiry deposited to somebody besides its actor"
    assert _deposits_caused_by(w, ev.id), "the actor's own claim did not deposit"

    w, d, out = found["finding"]
    (ev,) = out
    assert ev.kind == "finding.made" and ev.degree in ("Partial", "Success", "Overwhelming"), (
        ev.kind, ev.degree)
    _witness(w, d, out)
    assert _deposits_caused_by(w, ev.id), "a graded `finding.made` deposited nothing"
    assert any(c.predicate == "finding.made" for p in w.persons.values() for c in p.ledger)

    # A REFUSED inquiry: the Record does not exist, so the precondition refuses before any roll.
    w, d = _world()
    gone = Act(id="a_fi01_research_gone", actor=ACTOR, verb="research", payload={"subject": "rec_none"})
    out = _resolve(w, d, gone)
    assert [(e.kind, e.degree) for e in out] == [("inquiry.refused", None)], [(e.kind, e.degree) for e in out]
    before, after = _witness(w, d, out)
    assert before == after and not _deposits_caused_by(w, out[0].id), "a refused inquiry deposited"

    # THE CONTROL: a telling to an absent hearer is refused `tell.refused` (T4) and still deposits.
    w = P.tiny_world()
    d = SeasonDriver(w)
    w.persons[ACTOR].ledger.append(
        Claim("c_held", ACTOR, "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    told = Act(id="a_fi01_tell_absent", actor=ACTOR, verb="tell",
               payload={"subject": "Hh", "to": "p_king",
                        "said": said_of(w.persons[ACTOR].ledger, "Hh", w.fixtures)})
    out = _resolve(w, d, told)
    assert [e.kind for e in out] == ["tell.refused"], [e.kind for e in out]
    _witness(w, d, out)
    assert _deposits_caused_by(w, out[0].id), "`tell.refused` stopped depositing -- the skip widened"
    assert any(c.predicate == "tell.refused" for p in w.persons.values() for c in p.ledger)


def test_the_route_is_not_readable_as_a_prize():
    """NOT A PRIZE (`rosters.yaml`: a prize here is scripting drift). No graded verb declares `contests:`,
    no route key or field is a `contest_subsystems` prize, the contest manifest answers `None` for every
    route key, and a route carries `{provider, module_entry, form}` and at most `armed_by` (B07.01) -- no `module:` a prize reader keys
    on. Then the refusals, each planted and each naming what it refuses: a routed row that also contests
    (loader), a routed row with a flat `emits:` (loader), a route with a `module:` (loader), and a route
    to a roll no prize row binds (driver construction)."""
    prizes = roster_map("contest_subsystems", "prizes")
    checked = 0
    for verb, route in GRADED_TASKS.items():
        assert VERB_TABLE[verb].contests == "", verb
        assert verb not in prizes and manifest_resolve("contest", verb) is None, verb
        assert {"provider", "module_entry", "form"} <= set(route) <= {"provider", "module_entry", "form", "armed_by"}, route
        assert not set(route.values()) & set(prizes), route
        checked += 1
    assert checked == len(GRADED_TASKS) >= 3
    assert check_graded_tasks(VERB_TABLE) == sorted(GRADED_TASKS)

    src = yaml.safe_load(VERBS.VERB_TABLE_YAML.read_text())

    def loads(mutate, routes=None, kinds=None):
        doc = copy.deepcopy(src)
        mutate(doc)
        with mock.patch.object(VERBS, "VERB_TABLE_YAML") as fake, \
                mock.patch.object(VERBS, "GRADED_TASKS", routes or GRADED_TASKS), \
                mock.patch.object(VERBS, "UNDEPOSITED_KINDS", kinds or UNDEPOSITED_KINDS):
            fake.exists.return_value = True
            fake.read_text.return_value = yaml.safe_dump(doc)
            with pytest.raises(SystemExit) as e:
                VERBS._load_verb_table()
        return str(e.value)

    def row(doc, verb):
        return next(r for r in doc["verbs"] if r["verb"] == verb)

    msg = loads(lambda doc: row(doc, "research").update(contests="a standing"))
    assert "NOT a prize" in msg and "research" in msg, msg
    msg = loads(lambda doc: row(doc, "surveil").update(emits=["finding.made"]))
    assert "FLAT `emits:`" in msg and "surveil" in msg, msg
    with_module = dict(GRADED_TASKS, examine=dict(GRADED_TASKS["examine"], module="social_contest"))
    msg = loads(lambda doc: None, routes=with_module)
    assert "examine" in msg and "fields" in msg, msg
    # A MISSPELLED skip kind would skip nothing and report the deposit half built: the loader names it.
    msg = loads(lambda doc: None, kinds=frozenset({"finding.nnoe"}))
    assert "finding.nnoe" in msg, msg

    stray = dict(GRADED_TASKS, research={"provider": "social_contest", "module_entry": "combat.fight", "form": "inquiry"})
    with mock.patch.object(_rosters, "GRADED_TASKS", stray):
        with pytest.raises(Unspecified) as e:
            check_graded_tasks(VERB_TABLE)
        # ...and the same refusal at DRIVER CONSTRUCTION, where the check is wired (`loop/driver.py`):
        # delete that call and this goes red, which the direct call above cannot show.
        with pytest.raises(Unspecified) as e2:
            SeasonDriver(P.tiny_world())
    assert "research" in str(e.value) and "combat.fight" in str(e.value), str(e.value)
    assert "research" in str(e2.value), str(e2.value)
    # A PAIR A PRIZE ROW BINDS, on a provider that cannot take a route: bound, so refusal 2 passes, and
    # refused for the signature instead of raising `TypeError` at the first act.
    bound_elsewhere = dict(GRADED_TASKS, research={"provider": "personal_combat", "module_entry": "combat.fight", "form": "inquiry"})
    with mock.patch.object(_rosters, "GRADED_TASKS", bound_elsewhere):
        with pytest.raises(Unspecified) as e3:
            check_graded_tasks(VERB_TABLE)
    assert "research" in str(e3.value) and "module_entry" in str(e3.value), str(e3.value)


def test_examine_at_a_present_site_is_graded():
    """`examine` binds a `Site` (not a Record), and no corpus act is admitted there, so the sweep over
    `research` above says nothing about it. A Site in the actor's own rung admits it; the act ids are
    swept until one draws each of `Failure` and a finding band, so the graded `examine` is SEEN to roll
    (an `Event.degree` set, the kinds the row's degree-keyed `emits:` names) and not only declared."""
    seen: dict = {}
    for n in range(60):
        w = P.tiny_world()
        w.sites["site_fi01"] = Site("site_fi01", "Hh", "ruin", condition=500)
        d = SeasonDriver(w)
        a = Act(id=f"a_fi01_examine_{n}", actor=ACTOR, verb="examine", payload={"site": "site_fi01"})
        (ev,) = _resolve(w, d, a)
        assert ev.degree is not None, (ev.kind, ev.degree)
        seen.setdefault(ev.degree, ev.kind)
    assert "Failure" in seen and set(seen) - {"Failure"}, f"60 act ids drew only {sorted(seen)}"
    assert seen["Failure"] == "finding.none" and all(
        k == "finding.made" for deg, k in seen.items() if deg != "Failure"), seen


def test_the_inquiry_degree_is_the_one_owners(monkeypatch):
    """ONE ROLL OWNER (S27.2, A-21). The route reaches the `social_contest` module entry through the
    registrar's table, and the band is the one ladder's reading of the `Margin` it returns: replace the
    entry with one returning a fixed margin and the inquiry's degree follows it, band for band. The
    inquiry's subject is a Record, so the module is handed no opposition (the obstacle's non-person
    default). The host scan that no second resolver exists is the shape pin named in this module's
    docstring, where a planted inquiry resolver is seen to fail it."""
    w, d = _world()                         # a driver is constructed first: the registrar fills the table
    real = MODULE_ENTRIES["social_contest.roll"]
    seen: list = []
    for net, ob, band in ((5, 2, "Overwhelming"), (3, 2, "Success"), (2, 2, "Partial"), (0, 2, "Failure")):
        def fn(inp, rng, net=net, ob=ob):
            seen.append(inp)
            return Margin(net=net, ob=ob)
        monkeypatch.setitem(MODULE_ENTRIES, "social_contest.roll", dataclasses.replace(real, fn=fn))
        a = Act(id=f"a_fi01_owner_{band}", actor=ACTOR, verb="research", payload={"subject": REC})
        (ev,) = _resolve(w, d, a)
        assert ev.degree == band, (net, ob, ev.degree)
    assert len(seen) == 4
    assert all(i.opposition is None for i in seen), [i.opposition for i in seen]
    # B05.99 re-pin (B05.25, B05.23): the actor's pool is the one pool reader's, `pool_of(governing score + rank, .., 6, 5)` -- the
    # untrained man's 2 + 6 here; was `pool_default` alone
    from ..seam.wrappers import pool
    assert all(i.pool == pool.faculty(w, w.persons[ACTOR], "research") == w.fixtures.get("pool_default") + w.fixtures.get("pool_add")
               for i in seen), [i.pool for i in seen]


def test_an_inquiry_admits_before_it_rolls():
    """`resolve()` checks eligibility and `requires` once, before the roll, as for a contest: a research
    on a Record that does not exist reads False on `subject` and never reaches the module entry."""
    w, d = _world()
    a = Act(id="a_fi01_admits", actor=ACTOR, verb="research", payload={"subject": "rec_none"})
    verdict = evaluate(VERB_TABLE["research"].requires_typed, WorldReader(w, ACTOR), binding_from_act(a))
    assert verdict.value is False, verdict
    called: list = []
    real = MODULE_ENTRIES["social_contest.roll"]
    with mock.patch.dict(MODULE_ENTRIES, {"social_contest.roll": dataclasses.replace(
            real, fn=lambda inp, rng: called.append(inp) or Margin(net=0, ob=2))}):
        out = _resolve(w, d, a)
    assert not called and [e.kind for e in out] == ["inquiry.refused"], (called, [e.kind for e in out])


def test_the_realm_grades_inquiries_in_one_season():
    """THE EXIT'S EXECUTION ARTIFACT, in the realm and not in a unit world. `corpus_run`'s `DEGREES RESOLVED`
    is one histogram over every verb and was non-empty before this position, so it cannot show an
    inquiry graded; here the realm's own first season (`build_realm(0)`, seed 0) is run and the log is
    read: a `finding.*` Event carries a degree. A `finding.made` with no degree is a flat-`emits:` inquiry
    (`interview`, `reconstruct`, `thread_read`) and is not counted."""
    w = build_realm(0)
    POP.run(seasons=1, seed=0, w=w)
    graded = [(e.kind, e.degree) for e in w.log if e.kind.startswith("finding.") and e.degree is not None]
    assert graded, "no inquiry in the realm's first season drew a degree"
    assert {k for k, _ in graded} <= {"finding.made", "finding.none"}
    assert all((k == "finding.none") == (deg == "Failure") for k, deg in graded), graded
