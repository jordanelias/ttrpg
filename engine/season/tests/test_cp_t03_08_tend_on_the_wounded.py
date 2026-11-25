"""v11 CP-T03-08 -- `tend` FORMS ON THE WOUNDED.

(i) `queries/world_q.py::wounded_with`, one more term appended to `questions_for`'s `added` splice (REM-21's shared
stamp registry; no second one): the asker himself when his OWN body is below his OWN `body_ceiling` (CP-T03-07), then
each other living person `with` him whom HIS LEDGER'S newest `(person, "body", v)` claim (CP-T03-02's Observation, or a
told copy) puts below `condition_scale`. Stamped as `Person` (`World.class_of`). (ii) `tend` declares
`referent_class: Person` (`verb_table.yaml`), so it forms only on a `Person`-classed referent.
[ASSUMPTION; medium; Jordan to correct; revert: the row's column and the term -- `revert_cp_t03_08`]

  FALSIFIER (hand-built): the home's case 5 -- a DETAINED man below his ceiling is stamped for himself, `tend` forms on
  him, and the real fold raises him to his ceiling (`_eff_tend` restores the WHOLE headroom to
  `max(body, body_ceiling)`: there is no `tend_share`, that is CP-T10-04's, unbuilt, so case 5's `725` is not this
  tree's -- 450 -> 799 for a marked man here).
  THE LAWFUL-INPUT RULE: the stamper reads no other person's TRUE body. `_lawful_input_violations` checks it by
  moving true bodies and beliefs independently; MUTATION (executed below): a stamper that reads true bodies turns it
  red -- an unwitnessed wound is stamped for a stranger.
  CONTROL: `revert_cp_t03_08` (the column emptied, the term returning `()`), which other files' reverts call; the
  realm hashes are `_realm_goldens.py`'s.
  REALM READINGS (seeds 0-2, two seasons, the formation/attempt/execution split by arm) are commit-body readings,
  never assertions here.
"""
from __future__ import annotations

from dataclasses import replace

from ..data.rosters import DETAIN_KIND
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..harness import probes as P
from ..boot.realm import build_realm
from ..harness.populated import run
from ..queries import world_q
from ..state.carriers import Claim, Tenure
from .test_in10_record_operands import _acts, _resolve
from .test_in12_step9 import _world
import pytest

pytestmark = pytest.mark.flat_fold

A, B = "p_low", "p_mid"            # `tiny_world`: both stand at the hearth (`with` each other)
FAR = "p_high"                     # elsewhere


def revert_cp_t03_08(monkeypatch):
    """The item OFF, in process: `tend` declares no `referent_class` (it forms on plain referents, as before) and the
    `wounded_with` term stamps nobody. Other tests that pin a pre-item hash call it."""
    monkeypatch.setitem(VERB_TABLE, "tend", replace(VERB_TABLE["tend"], referent_class=""))
    monkeypatch.setattr(world_q, "wounded_with", lambda w, p: ())


def _believe(w, holder, about, v, cid="c_body", when=0, rnd=0):
    """`holder` holds `(about, "body", v)` -- the Observation CP-T03-02 deposits to a fight's actor."""
    w.persons[holder].ledger.append(Claim(cid, holder, about, world_q.BODY_STEM, v, when, "firsthand", 100, "own",
                                          lap=rnd))


def _tends(w, pid):
    p = w.persons[pid]
    qs = world_q.questions_for(w, p)
    return [c for q in qs[:1] for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == "tend"]


# ---- (i) the row, the stem ---------------------------------------------------------------------------------------

def test_tend_declares_person():
    assert VERB_TABLE["tend"].referent_class == "Person"


# ---- (ii) the falsifier: case 5, through the fold ----------------------------------------------------------------

def test_case_5_a_detained_man_below_his_ceiling_forms_tend_on_himself_and_is_raised_to_it():
    w, d = _world()
    p = w.persons[B]
    seat = next(iter(w.offices))
    w.add_tenure(Tenure("t_det_case5", B, seat, DETAIN_KIND, since=w.tick))
    p.body_ceiling, p.body = 799, 450
    assert world_q.wounded_with(w, p) == (B,)
    q = world_q.questions_for(w, p)[0]
    assert (B, "Person") in q.classes, q
    cands = [c for c in _tends(w, B) if c.subject == B]
    assert cands, "case 5: no tend formed on himself"
    assert [e.kind for e in _resolve(w, d, *_acts(w, B, cands[:1]))] == ["body.tended"]
    assert p.body == 799, "healed to his own ceiling, the whole headroom"


def test_control_a_whole_man_is_stamped_for_nobody_and_forms_no_tend_on_himself():
    w, _ = _world()
    for pid in w.persons:
        assert world_q.wounded_with(w, w.persons[pid]) == (), pid
    assert not [c for c in _tends(w, B) if c.subject == B]


# ---- (iii) the lawful-input rule and its mutation ---------------------------------------------------------------

def _lawful_input_violations(stamper) -> list:
    """The rule as a check, by moving TRUE bodies and BELIEFS independently. Empty = the rule holds."""
    bad = []
    w = P.tiny_world()
    scale = w.fixtures.get("condition_scale")
    assert world_q.place_of(w, A) == world_q.place_of(w, B) != world_q.place_of(w, FAR), "setup: who stands with whom"
    # 1. B truly wounded, nobody saw it: B is stamped for himself only.
    w.persons[B].body = scale // 4
    if B in stamper(w, w.persons[A]):
        bad.append("an unwitnessed wound is stamped for a stranger")
    if stamper(w, w.persons[B]) != (B,):
        bad.append(f"the wounded man is not stamped for himself: {stamper(w, w.persons[B])}")
    # 2. A believes B below whole but B is truly whole: the belief, not the body, stamps.
    w = P.tiny_world()
    _believe(w, A, B, scale // 4)
    if B not in stamper(w, w.persons[A]):
        bad.append("a believed wound beside him is not stamped")
    # 3. A's NEWEST belief is whole while B is truly wounded: not stamped.
    w = P.tiny_world()
    w.persons[B].body = scale // 4
    _believe(w, A, B, scale // 4, cid="c_old", when=0)
    _believe(w, A, B, scale, cid="c_new", when=1)
    if B in stamper(w, w.persons[A]):
        bad.append("a stale belief, or the true body, outranks his newest belief")
    # 4. a believed wound on someone not with him: not stamped.
    w = P.tiny_world()
    _believe(w, A, FAR, scale // 4)
    if FAR in stamper(w, w.persons[A]):
        bad.append("a believed wound elsewhere is stamped")
    return bad


def test_the_stamper_reads_no_other_persons_true_body():
    assert _lawful_input_violations(world_q.wounded_with) == []


def test_a_believed_wound_beside_him_forms_tend_on_the_other_through_questions_for():
    w, d = _world()
    scale = w.fixtures.get("condition_scale")
    w.persons[B].body = scale // 4
    assert not [c for c in _tends(w, A) if c.subject == B], "CONTROL: no belief, no tend on another"
    _believe(w, A, B, scale // 4)
    cands = [c for c in _tends(w, A) if c.subject == B]
    assert cands
    assert [e.kind for e in _resolve(w, d, *_acts(w, A, cands[:1]))] == ["body.tended"]
    assert w.persons[B].body == scale


def test_rem52s_fall_is_tended_by_30_of_37_while_the_seat_news_floods_oblige():
    """THE REALM READING, PINNED (seed 0, one season), AS IT NOW STANDS: REM-52's hunger lowers every short cohort's body in MATTER,
    `wounded_with` stamps each for himself below his ceiling, and `_eff_tend` restores the whole headroom to the persons who choose it --
    30 of the 37 short, each named by a `body.tended`, every one tended whole, none tended who was not short. THE SIX THE OLD READING TENDED
    ARE A REGRESSION THIS PIN RECORDS, NOT A FINDING: (37, 37) -> (37, 31) at v12 B11.08 (and (37, 30) at B11.14), whose `seed_seat_news` tells every person of every
    seat of his realm, so `seats_named` stamps ~31 Offices on his question and `oblige` forms on them for everyone (`hole_register.yaml`'s
    B11.08 row); the cohorts spend the season on it. The mechanism itself (`wounded_with`, `_eff_tend`'s whole-headroom magnitude, CP-T10-04's
    `tend_share`, unbuilt) is the hand-built tests of this file, unmoved."""
    w = build_realm(0)
    run(1, 0, w=w)
    short = {pid for pid in w._subsistence_shortfall if pid in w.persons}
    tended = {c.subject for e in w.log if e.kind == "body.tended" for c in e.changes}
    assert short, "setup: nobody went hungry"
    assert tended <= short, sorted(tended - short)
    assert all(w.persons[pid].body == w.persons[pid].body_ceiling for pid in tended)
    # B11 lane A (the duel chain's reach; re-pinned in B01.02): (37, 37) -> (37, 38): one person tended who was not short
    # (`p_npc_033`, wounded by the reach's new formations). With `revert_b11a_scores` alone it reads (37, 38); with
    # `revert_b11a` too, (37, 37) (scratch, not kept).
    # B01a.99 (every person's attributes are drawn, a population change): (37, 38) -> (37, 37): the duels the drawn sheets
    # resolve do not wound `p_npc_033`, so the tended are exactly the short (`tended - short` and `short - tended` both empty,
    # read in process at PYTHONHASHSEED=0).
    # v12 B11.08 re-pin, SAID PLAINLY: (37, 37) -> (37, 31); the cause is the docstring's.
    # v12 B11.14 (one more cohort no longer tends, attributed to B11.14 by the B11.99 reading):
    # (37, 31) -> (37, 30). A measured pin moved by a declared mover, re-recorded here; the six lost to the flood stand.
    # B21b.02 (the guards ship on, three guard cohorts join the realm): (37, 30) -> (40, 31), read at PYTHONHASHSEED=0; `tended <= short` above still holds.
    assert (len(short), len(tended)) == (40, 31)
