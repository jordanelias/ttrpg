"""B11.70 (`08_FI_03` §1 with `08_FI_07` §1): THE INQUIRY WORLD -- `harness/scenarios.py::inquiry_world`.

The world is a premise folded through the season loop's own steps (a forging, a move, a handover) with no claim planted in
the investigator's ledger: his case is a goal whose `deed_doers` referents are his suspects, empty until his OWN ledger names
someone. `test_every_inquiry_world_run_ends_by_a_predicate` is B11.76's (it needs the ending; below, with the module fixture it shares with `test_shortest_case.py`).

B11.71 (`08_FI_03` §2, FRES §8): WHAT A LOOK TEACHES -- the three `observes:` rows and the one band table `finding_terms` (the tests after the world's).
"""
from __future__ import annotations

import dataclasses
import functools
from collections import Counter

import pytest

from ..data import goals as goals_data
from ..data.matrix import Step, WriteClass
from ..data.verbs import VERB_TABLE
from ..decision.options import opening_set
from ..epistemic import Seen
from ..harness import probes as P
from ..harness import scenarios as S
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q, world_q
from ..queries.person_q import record
from ..seam import Resolution
from ..state.carriers import Act, Claim, Proposition, Question, Record, Tenure, View


def test_inquiry_world_builds_its_six_parts_and_seeds_one_case_goal():
    """The six persons and the bench exist; the sheet was forged, handed on and is held by the holder; the witness saw the
    handover and not the forging; the investigator holds one goal whose object is `deed_doers` and whose referents are
    empty at build. FALSIFIER: a builder that authors an outcome (a claim naming the forger in the investigator's ledger)
    fails the last two asserts; the control below is the same read once his ledger does name the forger."""
    w = S.inquiry_world(0)
    assert set(S.INQUIRY_CAST) <= set(w.persons) and len(S.INQUIRY_CAST) == 6
    assert world_q.judging_set(w, S.TOWN) == ["p_bench_a", "p_bench_b", "p_investigator"]
    forged = [e for e in w.log if e.kind == "record.forged"]
    given = [e for e in w.log if e.kind == "record.given"]
    assert len(forged) == len(given) == 1, "the sheet was forged and handed on once"
    (rid,) = [c.subject for c in forged[0].changes]
    assert world_q.hold_force(w, rid).subject == "p_holder"
    ledger = lambda pid: w.persons[pid].ledger
    assert any(c.predicate == "record.given" for c in ledger("p_witness")), "the witness was at the handover"
    assert not any(c.predicate == "record.forged" for c in ledger("p_witness")), "and not at the forging"
    assert any(c.predicate == "record.forged" for c in ledger("p_forger")), "the forger holds his own deed"
    inv = w.persons["p_investigator"]
    mine = [t.object for t in w.tenures if t.kind == "commit" and t.subject == inv.id and t.object in w.propositions
            and goals_data.goal(t.object) is not None]
    assert mine == [S.CASE_GOAL], "the investigator holds exactly one goal"
    goal = goals_data.goal(S.CASE_GOAL)
    assert goal.object["kind"] == "deed_doers" and set(goal.object["kinds"]) >= {"record.forged"}
    assert not [c for c in inv.ledger if c.predicate in goal.object["kinds"]], "the investigator's ledger holds a covert deed at build"
    assert not [c for c in inv.ledger if c.subject == rid], "and nothing of the sheet"
    prop = w.propositions[S.CASE_GOAL]
    assert world_q.goal_referents(w, inv, prop) == ()
    # CONTROL: the reader sees a name once his own ledger holds one, wrongly or rightly.
    inv.ledger.append(Claim("c_ctl", inv.id, "p_forger", "record.forged", True, w.tick, "told", 1, "own"))
    assert world_q.goal_referents(w, inv, prop) == ("p_forger",)
    assert S.inquiry_world(0).content_hash() == S.inquiry_world(0).content_hash()


# ======================================================================================
# B11.71 (`08_FI_03` §2): WHAT A LOOK TEACHES. A hand-built world, the act folded at a band the test names (`Resolution(band, {})`, as
# `test_aperture._lost_or_won_tell` folds one) and then witnessed, so what lands in the actor's own ledger is what the barrier deposited.
# ======================================================================================
LIAR, LOOKER = "p_other", "p_low"
REC = "rec_b1171"


def _world():
    """`tiny_world` at the shipped fixtures: `Hh` holds 8 grain, `site_harbour` stands in `S` (40 grain), `p_low` is at `Hh` and holds a petition
    (`REC`, the Record `research` reads), `p_high` is at `S`."""
    w = P.tiny_world()
    w.records[REC] = Record(REC, "Hh", "petition", subject_matter={"terms": "prop_x", "to": ("p_mid", "p_other"), "from": LOOKER})
    w.add_tenure(Tenure("t_hold_rec", LOOKER, REC, "hold", since=0))
    return w, SeasonDriver(w)


def _look(w, d, act, band):
    """Fold `act` at `band`, log its Events and witness them; returns the Events."""
    w.step = Step.RESOLVE
    w.acts.append(act)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution(band, {}))
    w.log.extend(out)
    for e in out:
        d.act_of[e.id] = act
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


def _told_false(w, hearer, subject, predicate, value):
    """`hearer` holds, told by the liar, a false value of a cell (`record` pairs it against his own firsthand claim of the cell)."""
    w.persons[hearer].ledger.append(Claim(f"c_told_{subject}_{predicate}", hearer, subject, predicate, value, 0, "told_by", 50, "own",
                                          chain=(LIAR,)))


LOOKS = {   # verb -> (looker, payload, the cell the liar lied on, the false value)
    "surveil": (LOOKER, {"subject": "Hh"}, ("Hh", "stores:grain"), 12),
    "examine": ("p_high", {"site": "site_harbour"}, ("site_harbour", "condition"), 1),
}


@pytest.mark.parametrize("verb", sorted(LOOKS))
def test_a_look_re_grades_a_liar_and_the_empty_observes_control_does_not(verb, monkeypatch):
    """`08_FI_03` §2 (the gate): a hearer's `record` of a liar reads 1.0 before his `examine`/`surveil` and below 1.0 after -- the look deposits
    his own firsthand cell, `queries/person_q.py::record` pairs the liar's word against it. CONTROL: the same act with the row's `observes:`
    emptied leaves the record at 1.0 (the gating reads it still deposits are not the cell the liar lied on). FALSIFIER: a look that deposits
    nothing, or a record that never pairs a told claim with a held one, reads 1.0 after."""
    looker, payload, (subject, predicate), false = LOOKS[verb]
    assert VERB_TABLE[verb].observes, f"`{verb}` declares no `observes:`"

    def run(empty):
        w, d = _world()
        _told_false(w, looker, subject, predicate, false)
        assert record(w.persons[looker], LIAR, w.fixtures, w.tick) == 1.0, "before: nothing of his own to check the word against"
        with monkeypatch.context() as m:
            if empty:
                m.setitem(VERB_TABLE, verb, dataclasses.replace(VERB_TABLE[verb], observes=()))
            out = _look(w, d, Act(id=f"a_{verb}", actor=looker, verb=verb, payload=payload), "Success")
        assert [e.kind for e in out] == ["finding.made"], [e.kind for e in out]
        return w, record(w.persons[looker], LIAR, w.fixtures, w.tick)

    w, after = run(empty=False)
    own = [c for c in w.persons[looker].ledger if (c.subject, c.predicate) == (subject, predicate) and c.firsthand]
    assert own and own[0].value != false, "the look left his own reading of the cell"
    assert after < 1.0, after
    assert run(empty=True)[1] == 1.0


def _mine(w, pid):
    """`pid`'s claims that nobody told him: `{(subject, predicate): value}`."""
    return {(c.subject, c.predicate): c.value for c in w.persons[pid].ledger if c.source != "told_by"}


def _stems(mine):
    return {str(p).partition(":")[0] for _s, p in mine}


READS = {"condition", "stores", "held_by", "content"}      # `rosters.yaml: look_reads`
ACTS = {"surveil": (LOOKER, {"subject": "Hh"}), "examine": ("p_high", {"site": "site_harbour"}), "research": (LOOKER, {"subject": REC})}


@pytest.mark.parametrize("verb", sorted(ACTS))
def test_a_failed_look_deposits_the_gating_reads_only(verb):
    """FRES §8 (and `08_FI_07` §2 (b)'s `test_a_failed_look_deposits_gating_reads_only`, one test for one claim): at `Failure` the actor holds the
    reads the row's own cell made (`exists`, `present_at`: above 0) and none of the look -- no `condition`, `stores`, `held_by`, and no
    `content:` claim. CONTROL: the same act at `Success` deposits the look, so the assertion that none landed could have failed."""
    actor, payload = ACTS[verb]

    def deposited(band):
        w, d = _world()
        out = _look(w, d, Act(id=f"a_{verb}", actor=actor, verb=verb, payload=payload), band)
        return _stems(_mine(w, actor)), out

    failed, out = deposited("Failure")
    assert [e.kind for e in out] == ["finding.none"], [e.kind for e in out]
    assert {"exists", "present_at"} <= failed, failed
    assert not failed & READS, failed
    assert deposited("Success")[0] & READS, "control: a success deposits what the row observes"


def test_a_look_deposits_what_finding_terms_lists_at_each_band():
    """FRES §8 rule 2: Overwhelming and Success deposit every listed read; Partial every one but `held_by`, a number through the lossy-copy rule
    (`loop/witness.py::_told_value`: the figure comes back moved, never across zero). `research` stands for `content` and `held_by`, `surveil` for
    `stores`."""
    for band in ("Overwhelming", "Success", "Partial"):
        w, d = _world()
        _look(w, d, Act(id="a_r", actor=LOOKER, verb="research", payload={"subject": REC}), band)
        _look(w, d, Act(id="a_s", actor=LOOKER, verb="surveil", payload={"subject": "Hh"}), band)
        mine = _mine(w, LOOKER)
        assert (REC, "content:petition") in mine, (band, sorted(mine))
        assert ((REC, f"held_by:{LOOKER}") in mine) == (band != "Partial"), (band, sorted(mine))
        grain = mine[("Hh", "stores:grain")]
        assert (grain == 8) == (band != "Partial") and grain > 0, (band, grain)


# ======================================================================================
# B11.73 (`08_FI_03` §3 act 1; FRES §7 (1)-(2)): `reconstruct` REASONS AND DEPOSITS ITS CONCLUSION TO ITS MAKER. The conclusion is read off his OWN ledger
# at CHOOSE (`person_q.conclusion_cites`, over `_concluded`) and rides the act as `concluded`; WITNESS deposits it to the maker by band.
# ======================================================================================
CONCLUDER, VICTIM, KILLER, OTHER = "p_low", "p_mid", "p_other", "p_high"
DEED = "person.died"        # a paired covert kind: the claim's subject is the one it was done to, the doer is read off a sighting
BANDS = ("Overwhelming", "Success", "Partial", "Failure")


def _concluder(sighted=KILLER):
    """`tiny_world` where `p_low` holds a death of `p_mid` and, unless `sighted` is `None`, a sighting of the same deed naming `sighted` as the hand."""
    w, d = _world()
    p = w.persons[CONCLUDER]
    p.ledger.append(Claim("c_death", p.id, VICTIM, DEED, True, 0, "firsthand", 100, "own"))
    if sighted is not None:
        stratum = next(iter(person_q._KIND_STRATA[DEED]))
        p.ledger.append(Claim("c_seen", p.id, VICTIM, "seen", Seen(stratum=stratum, who=sighted), 0, "firsthand", 100, "own"))
    return w, d


def _reconstruct(w):
    """The Candidate his ledger forms on `p_mid` and the act it becomes: `(candidate, act)`."""
    p = w.persons[CONCLUDER]
    q = Question("q_b1173", "claim_landed", (VICTIM,), "")
    (c,) = [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures) if c.verb == "reconstruct" and c.subject == VICTIM]
    return c, Act(id="a_rc", actor=p.id, verb="reconstruct", payload={"subject": VICTIM, **c.operands})


def _concluded(w):
    """`{(subject, predicate): value}` of the `concluded:` claims the maker holds."""
    return {(c.subject, c.predicate): c.value for c in w.persons[CONCLUDER].ledger if str(c.predicate).startswith("concluded:")}


def test_reconstruct_writes_nothing():
    """FRES §7 (1): the row is an inquiry and writes nothing, at every band -- no typed write, no `changes[]`. A conclusion is a claim minted at WITNESS.
    CONTROL: the same act at `Success` leaves a `concluded:` claim, so the empty write is not an empty act."""
    row = VERB_TABLE["reconstruct"]
    assert not row.writes and not row.writes_by_degree
    for band in BANDS:
        w, d = _concluder()
        out = _look(w, d, _reconstruct(w)[1], band)
        assert len(out) == 1 and not out[0].changes, (band, out[0].changes)
    w, d = _concluder()
    _look(w, d, _reconstruct(w)[1], "Success")
    assert _concluded(w), "control: a winning reconstruct deposits"


def test_a_winning_reconstruct_deposits_a_concluded_claim_by_band():
    """FRES §7 (2) and R-19-04's table: at WITNESS the maker holds `(the one the deed was done to, concluded:<deed kind>, doer)`, source `inferred`, the
    doer the one his OWN ledger names. `Partial` withholds the hand (the claim is the deed alone: value `True`), `Success` and `Overwhelming` name it,
    `Failure` emits `finding.none` and leaves no `concluded:` claim. FALSIFIER: a conclusion whose doer his ledger did not name -- the same
    world with no sighting (his ledger names nobody) deposits none at a winning band, and with a sighting of ANOTHER hand he concludes that hand."""
    cell = (VICTIM, f"concluded:{DEED}")
    for band, want in (("Overwhelming", KILLER), ("Success", KILLER), ("Partial", True), ("Failure", None)):
        w, d = _concluder()
        c, act = _reconstruct(w)
        assert c.operands["concluded"] == (VICTIM, DEED, KILLER), c.operands
        out = _look(w, d, act, band)
        assert [e.kind for e in out] == (["finding.none"] if band == "Failure" else ["conclusion.reached"]), (band, [e.kind for e in out])
        assert _concluded(w) == ({} if want is None else {cell: want}), (band, _concluded(w))
        if want is not None:
            (claim,) = [x for x in w.persons[CONCLUDER].ledger if (x.subject, x.predicate) == cell]
            assert claim.source == "inferred" and not claim.firsthand, claim
    for sighted, want in ((None, {}), (OTHER, {cell: OTHER})):
        w, d = _concluder(sighted)
        _, act = _reconstruct(w)
        _look(w, d, act, "Success")
        assert _concluded(w) == want, (sighted, _concluded(w))


# ======================================================================================
# B11.76 (`08_FI_03` §1, §3, §5): THE INQUIRY ROW'S RUNS. Twenty runs of `inquiry` at two seasons (A-114, D-17: at two seasons `cold` cannot fire),
# the shipped ranking in the investigator's seat, read once and shared with `test_shortest_case.py` (the same claim at the same seeds).
# ======================================================================================
SEEDS = range(20)
SEASONS = 2


@functools.lru_cache(maxsize=None)
def inquiry_runs() -> tuple:
    """The twenty `inquiry` runs, seeds 0 to 19 at two seasons, the seat taking the ranking whole -- the module fixture the two files' tests read. Cached,
    so one process plays them once (single-threaded: `-n` gives each worker its own set)."""
    return tuple(S.run("inquiry", seed, SEASONS) for seed in SEEDS)


def test_every_inquiry_world_run_ends_by_a_predicate():
    """`08_FI_03` §1 (gate): each of twenty runs ends by one of the row's predicates or reaches the two-season cap, never by anything else, and the ending the
    runner names is the one `inquiry_ending` reads off the finished world. FALSIFIER (`08_FI_07`): all twenty end the same way, so the scenario offers no real
    choice -- at least two ending kinds occur. At two seasons `cold` cannot fire (it needs four), so a run that ended `cold` here read the clock wrong."""
    runs = inquiry_runs()
    assert len(runs) == len(SEEDS)
    for r in runs:
        assert r["ending"] != "cold", "cold needs four seasons"
        if r["ending"] is None:
            assert r["seasons"] == SEASONS, "a run with no ending stopped before the cap"
        else:
            assert r["ending"] in S.INQUIRY_KINDS and r["kind"] == S.INQUIRY_KINDS[r["ending"]], r["ending"]
        assert S.inquiry_ending(r["world"], r["seat"]) == r["ending"], "the ending is a read of the finished world"
    endings = Counter(r["ending"] for r in runs if r["ending"] is not None)
    assert len(endings) >= 2, f"FALSIFIER (`08_FI_07` falsifier 3): endings among twenty runs {dict(endings)}; the rest reached the cap"


def test_some_conclusion_names_a_non_actor():
    """`08_FI_03` §3 and `19_LACUNA_conclusion...`: over the twenty runs at least one ends with a conclusion naming someone who is not the Event's actor, and at
    least one with the actor named (`scenarios.named_and_actor`: a `concluded:` claim's hand against the actors of the Events it concludes about, else the
    person a bench disposed against the premise's forger). FALSIFIER: every conclusion names the true actor, so nothing can mislead and the wrong conclusion is
    still unrepresented -- and with no run naming anyone, neither can be shown."""
    named = [got for r in inquiry_runs() if (got := S.named_and_actor(r["world"], r["seat"])) is not None]
    assert named, "no run named anyone: neither a conclusion nor an accusation formed in twenty runs"
    assert any(not is_actor for _n, _a, is_actor in named), "every conclusion names the true actor"
    assert any(is_actor for _n, _a, is_actor in named), "no conclusion names the actor"


# ======================================================================================
# B11.78 (`08_FI_03` §3 "Acting on it", §4; `proposals/v12_B11_a_conclusion_acted_on.md` §1): A HELD CONCLUSION FORMS AN ACCUSATION; A CAUGHT LIAR IS A QUESTION.
# Hand-built worlds (no computed `utter` makes a `HOLDS` Proposition until B25 types it), the person-side formation read through `questions_for` and `opening_set`.
# ======================================================================================
def _holds_conclusion(w, mood="HOLDS", held=True, doer=KILLER):
    """`p_low` holds a `concluded:` claim naming `doer` and, per the arguments, the Proposition he uttered of it `(VICTIM, concluded:<deed>, doer)` of `mood`, on a live `hold`."""
    p = w.persons[CONCLUDER]
    p.ledger.append(Claim("c_concluded", p.id, VICTIM, f"concluded:{DEED}", doer, 0, "inferred", 100, "own"))
    w.propositions["prop_b1178"] = Proposition("prop_b1178", mood, VICTIM, f"concluded:{DEED}", doer, 0)
    if held:
        w.add_tenure(Tenure("t_hold_prop", p.id, "prop_b1178", "hold", since=0))
    return p


def _petitions_to(w, doer):
    """The `petition` Candidates `p_low` forms on the first question `questions_for` gives him, those that name `doer`."""
    p = w.persons[CONCLUDER]
    (q, *_rest) = world_q.questions_for(w, p)
    return [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k")), q, w.fixtures) if c.verb == "petition" and c.operands.get("to") == doer]


@pytest.mark.parametrize("variant", ["no_proposition", "mood_ought", "not_held"])
def test_a_held_conclusion_forms_an_accusation(variant):
    """B11.78 (design §1): a person who holds a `concluded:` claim AND the `HOLDS` Proposition he made of it forms a `petition` naming the doer, and folding it through the
    real driver mints a petition Record whose `terms` is the doer. CONTROL (each variant, one at a time): the same claim without the Proposition, with it in mood `OUGHT`, or
    with it uttered and no longer held forms none -- the conclusion is acted on once it is a committed assertion, not on the inference alone."""
    w, d = _concluder()
    _holds_conclusion(w)
    assert world_q.conclusions_held(w, w.persons[CONCLUDER]) == (KILLER,)
    (c,) = _petitions_to(w, KILLER)
    out = _look(w, d, Act(id="a_acc", actor=CONCLUDER, verb="petition", payload={"subject": c.subject, **c.operands}), "Success")
    assert [e.kind for e in out] == ["petition.filed"], [e.kind for e in out]
    minted = [r for r in w.records.values() if r.kind == "petition" and r.id != REC]
    assert [r.subject_matter["terms"] for r in minted] == [KILLER], minted
    ctl, _ = _concluder()
    if variant == "no_proposition":
        ctl.persons[CONCLUDER].ledger.append(Claim("c_concluded", CONCLUDER, VICTIM, f"concluded:{DEED}", KILLER, 0, "inferred", 100, "own"))
    else:
        _holds_conclusion(ctl, **{"mood_ought": dict(mood="OUGHT"), "not_held": dict(held=False)}[variant])
    assert world_q.conclusions_held(ctl, ctl.persons[CONCLUDER]) == ()
    assert _petitions_to(ctl, KILLER) == []


def _caught(w, told=True, own_value=8, own_when=0, told_by=None):
    """`LOOKER` was told by `LIAR` that `Hh` holds 12 grain (a false cell) and, unless `own_value` is `None`, holds his own firsthand reading of it at `own_when`; returns the
    contradicting claim."""
    p = w.persons[LOOKER]
    if told:
        _told_false(w, LOOKER, "Hh", "stores:grain", 12)
    mine = Claim("c_own_grain", p.id, "Hh", "stores:grain", own_value, own_when, "firsthand", 100, "own")
    if own_value is not None:
        p.ledger.append(mine)
    return mine


def _liar_questions(w, since=None):
    """The questions `questions_for` gives `LOOKER` whose referent is the liar."""
    return [q for q in world_q.questions_for(w, w.persons[LOOKER], since) if LIAR in q.referents]


def test_a_contradicted_teller_becomes_a_question():
    """B11.78 (`08_FI_03` §4, "Gates" §4): when `record(p, teller)` is below neutral and the firsthand claim that contradicts the teller landed since `p` last deliberated, one
    `claim_landed` question exists whose referent is the teller and whose `about` is that claim -- no new source, deposit or Event kind. CONTROLS, one at a time, each leaving
    no such question: no contradiction (his own reading AGREES with the telling), no telling (the firsthand claim contradicts nobody), a contradiction that landed before he last
    deliberated (`since`), and the teller's record at neutral (`record_gain` 0, where a contradicted teller reads 1.0). The question is the ordinary one: the unclassed rows (`speak`, `interview`) form on the liar; the classed ones (`petition`, `challenge`) reach him only as a Person-classed referent of the question he answers first (`own_referents_of_class`)."""
    w, _ = _world()
    mine = _caught(w)
    assert record(w.persons[LOOKER], LIAR, w.fixtures, w.tick) < 1.0
    (q,) = _liar_questions(w)
    assert (q.source, q.referents, q.about) == ("claim_landed", (LIAR,), mine.id), q
    formed = {c.verb for c in opening_set(w.persons[LOOKER], View(LOOKER, [], w.fixtures.get("view_k")), q, w.fixtures) if c.subject == LIAR}
    assert {"speak", "interview"} <= formed, f"the unclassed rows form on the liar: {sorted(formed)}"
    for name, build in {"agreeing": lambda x: _caught(x, own_value=12), "untold": lambda x: _caught(x, told=False),
                        "no_own_claim": lambda x: _caught(x, own_value=None)}.items():
        ctl, _ = _world()
        build(ctl)
        assert _liar_questions(ctl) == [], name
    stale, _ = _world()
    _caught(stale)
    assert _liar_questions(stale, since=(stale.tick + 1, 0)) == [], "landed before he last deliberated"
    flat, _ = _world()
    flat.fixtures = flat.fixtures.sweep("record_gain", 0)
    _caught(flat)
    assert record(flat.persons[LOOKER], LIAR, flat.fixtures, flat.tick) == 1.0
    assert _liar_questions(flat) == [], "his record is neutral: no question"
