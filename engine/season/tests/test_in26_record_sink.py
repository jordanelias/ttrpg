"""v9 IN-26 (BOUND-PAPER) -- a sink for Records: `destroy_record`, formable on `A-13`'s shape, behind an arm.

WHAT IS BUILT, AND WHERE EACH HALF LIVES:
  * THE ROW (`verb_table.yaml`): `own` first, typed on `give`'s first two conjuncts -- `existence` of
    `subject` kind `Record`, `relation` of `subject` `held_by` -- so H-75's placeholder half is answered by
    the cell; `loop/effects_information.py::_eff_destroy_record` destroys the bound `subject`.
  * WHO FORMS IT (`decision/options.py::opening_set`): only on a referent the person holds
    (`rosters.yaml: own_hold_declines`), and nobody while `Fixtures withheld_verbs` names it -- H-156's
    option (a) as a switch, SHIPPED naming it, so THE SINK ARM IS OFF and every realm hash is today's
    (`test_season_weather.py`'s `BASE_HASHES`/`BASE_EVENTS` are that falsifier, unmoved by IN-26).

What each block proves, on hand-built worlds through the real fold (v9 §0.5, RULED 2026-10-13: no test
here asserts a verb executed in the seed-0 realm):
  1. THE SINK, CHOOSER-SIDE TO FOLD: at the sink arm the holder's own Candidate, turned into an Act by the
     chooser's own payload builder, burns his document through a real season -- the Record leaves the
     world and his `hold` closes. CONTROL: the same season at the shipped arm forms nothing and the Record
     stays.
  2. ONLY WHAT HE HOLDS: at the sink arm nobody forms it on a referent he does not hold, and the fold
     refuses a stranger's hand-built burn at the `held_by` conjunct.
  3. THE SINK DOES NOT REACH TELLINGS (the position's falsifier names `harness/corpus_run.py`'s
     `told_redeposits`, which is inline code and not a callable, and reads 0 on both arms by hand): a burn
     leaves every ledger's claims about the burnt Record as they were (here a PROXY: the claims are
     compared, `told_redeposits` is not computed), so the redeposit reading over them cannot move. CONTROL: the planted told claim is
     really about the Record that burns.
  4. THE TWO READS REFUSE WHAT THEY CANNOT MEAN: a `withheld_verbs` member the table lacks, and an
     `own_hold_declines` member whose cell asks no holding.

MUTATIONS SEEN RED (each run by hand at the build, then reverted):
  * `_eff_destroy_record` reading the old `record` key -> block 1 RED (the Record survives).
  * `opening_set`'s `withheld_verbs` skip deleted -> block 1's control RED (and `test_u7_own.py` 5).
  * `opening_set`'s `own_hold_declines` narrowing deleted -> block 2 RED.
  * the row's `held_by` conjunct deleted -> block 2's stranger burn RED.
"""
from __future__ import annotations

import pytest

from ..data import verbs as VERBS
from ..data.fixtures import DEFAULT_FIXTURES
from ..decision.choose import _payload_of
from ..decision.options import opening_set
from ..gaps import Forbidden
from ..harness import probes as P
from ..queries.world_q import hold_force
from ..state.carriers import Claim, Question, View
from .test_u7_own import _formed as _u7_formed, _petition_held_by

SINK = DEFAULT_FIXTURES.sweep("withheld_verbs", ())
VERB = "destroy_record"


def _held_petition(w, pid="p_low"):
    """`pid` files a petition through the real fold and holds it (`test_u7_own.py`'s fixture)."""
    return _petition_held_by(w, pid)


def _formed(w, pid, referents):
    return _u7_formed(w, pid, VERB, referents)


def _burn_what_is_formed(w, rid, pid="p_low"):
    """One real season in which `pid` acts on every `destroy_record` Candidate his own opening set forms
    about `rid`, each made an Act by the chooser's payload builder (`decision/choose.py::_payload_of`)."""
    formed = []

    def choose(p, v, s, b):
        if p.id != pid:
            return []
        cands = _formed(w, pid, (rid,))
        formed.extend(cands)
        return [P.Act_(w, p, c.verb, payload=_payload_of(c)) for c in cands]
    d = P._run_d(w, choose)
    return formed, d


# ======================================================================================
# 1 -- THE SINK, CHOOSER-SIDE TO FOLD
# ======================================================================================

def test_in26_at_the_sink_arm_a_holder_burns_what_he_holds_and_at_the_shipped_arm_nobody_does():
    w = P.tiny_world(SINK)
    rid = _held_petition(w)
    hold = hold_force(w, rid)
    formed, _ = _burn_what_is_formed(w, rid)
    assert [c.subject for c in formed] == [rid], formed
    assert rid not in w.records, "the formed burn did not destroy the Record it was about"
    assert hold.until is not None and not hold.live, "the holder's `hold` outlived the Record"
    assert any(e.kind == "record.destroyed" for e in w.log)
    # CONTROL: the shipped arm -- the same world built the same way forms nothing and the Record stays
    w0 = P.tiny_world()
    assert VERB in w0.fixtures.get("withheld_verbs"), "the shipped arm is not the hold"
    rid0 = _held_petition(w0)
    formed0, _ = _burn_what_is_formed(w0, rid0)
    assert not formed0 and rid0 in w0.records, formed0


# ======================================================================================
# 2 -- ONLY WHAT HE HOLDS
# ======================================================================================

def test_in26_nobody_forms_it_on_what_he_does_not_hold_and_the_fold_refuses_a_stranger():
    w = P.tiny_world(SINK)
    rid = _held_petition(w)
    # the holder: on his Record only, never on the hearth, the realm or a person
    assert [c.subject for c in _formed(w, "p_low", (rid, "Hh", "R", "p_mid"))] == [rid]
    # a stranger standing in the same hearth: on nothing, the Record included
    assert not _formed(w, "p_other", (rid, "Hh", "p_low")), "a non-holder formed a burn"
    # and his hand-built burn is refused at the cell: the Record survives him
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, VERB, payload={"subject": rid})]
                                    if p.id == "p_other" else []))
    assert rid in w.records and hold_force(w, rid).subject == "p_low"
    assert any(e.kind == "destroy.refused" for e in w.log), "the stranger's burn was never attempted"


# ======================================================================================
# 3 -- THE SINK DOES NOT REACH TELLINGS
# ======================================================================================

def _about(w, rid):
    return {pid: sorted((c.id, c.predicate, str(c.value), c.source, c.chain) for c in p.ledger
                        if c.subject == rid)
            for pid, p in w.persons.items()}


def test_in26_a_burn_leaves_every_claim_about_the_record_as_it_was():
    w = P.tiny_world(SINK)
    rid = _held_petition(w)
    told = Claim("c_in26_told", "p_mid", rid, "exists:Record", True, w.tick, "told_by", 50, "own",
                 chain=("p_low",))
    w.persons["p_mid"].ledger.append(told)
    before = _about(w, rid)
    # CONTROL: the planted telling is about the Record that burns, so the comparison can see it
    assert any(row[3] == "told_by" for row in before["p_mid"]), before["p_mid"]
    _burn_what_is_formed(w, rid)
    assert rid not in w.records, "nothing burned -- the comparison below would be vacuous"
    after = _about(w, rid)
    # a burn may ADD what its witnesses saw (`record.destroyed`); it never edits or removes a claim
    for pid, rows in before.items():
        assert set(rows) <= set(after[pid]), (pid, rows, after[pid])
    assert [r for r in after["p_mid"] if r[3] == "told_by"] == [r for r in before["p_mid"] if r[3] == "told_by"]


# ======================================================================================
# 4 -- THE TWO READS REFUSE WHAT THEY CANNOT MEAN
# ======================================================================================

def test_in26_a_withheld_verb_the_table_lacks_is_refused():
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("withheld_verbs", ("destroy_recrod",)))
    with pytest.raises(Forbidden, match="withheld_verbs"):
        _formed(w, "p_low", ("Hh",))


def test_in26_an_own_hold_declines_member_whose_cell_asks_no_holding_is_refused_at_load():
    assert VERBS._load_own_hold_declines([VERB]) == VERBS.OWN_HOLD_DECLINES == {VERB}
    assert VERBS._load_own_hold_declines(["give"]) == {"give"}, "give's cell asks the holding too"
    for planted in (["create_record"], ["no_such_verb"]):
        with pytest.raises(Forbidden, match="own_hold_declines"):
            VERBS._load_own_hold_declines(planted)
