"""B11.70 (`08_FI_03` §1 with `08_FI_07` §1): THE INQUIRY WORLD -- `harness/scenarios.py::inquiry_world`.

The world is a premise folded through the season loop's own steps (a forging, a move, a handover) with no claim planted in
the investigator's ledger: his case is a goal whose `deed_doers` referents are his suspects, empty until his OWN ledger names
someone. `test_every_inquiry_world_run_ends_by_a_predicate` is B11.76's (it needs the ending).

B11.71 (`08_FI_03` §2, FRES §8): WHAT A LOOK TEACHES -- the three `observes:` rows and the one band table `finding_terms` (the tests after the world's).
"""
from __future__ import annotations

import dataclasses

import pytest

from ..data import goals as goals_data
from ..data.matrix import Step, WriteClass
from ..data.verbs import VERB_TABLE
from ..harness import probes as P
from ..harness import scenarios as S
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..queries.person_q import record
from ..seam import Resolution
from ..state.carriers import Act, Claim, Record, Tenure


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
