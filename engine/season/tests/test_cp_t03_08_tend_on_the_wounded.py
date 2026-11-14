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
  CONTROL: `revert_cp_t03_08` (the column emptied, the term returning `()`) reproduces the eb34324f hashes.
  REALM READINGS (seeds 0-2, two seasons, the formation/attempt/execution split by arm) are commit-body readings,
  never assertions here.
"""
from __future__ import annotations

from dataclasses import replace

import pytest

from ..data.rosters import DETAIN_KIND
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..harness import probes as P
from ..harness.populated import build_realm, run
from ..queries import world_q
from ..state.carriers import Claim, Tenure
from .test_cp_t03_07_body_ceiling import POST_ITEM as PRE_ITEM
from .test_in10_record_operands import _acts, _resolve
from .test_in12_step9 import _world

A, B = "p_low", "p_mid"            # `tiny_world`: both stand at the hearth (`with` each other)
FAR = "p_high"                     # elsewhere

#: 1-season hashes after this item; PRE_ITEM is eb34324f's (CP-T03-07's POST_ITEM). `build_realm(0)` is unmoved
#: (600d8b27147478e158553552cc1409a5): the item writes no field and no world-gen.
#: Seeds 1 and 2 are the post-B10-11b reading (`reading @4b334f2a`), re-recorded by the batch pin commit (was d9f3be70... /
#: 285fb92a...): PC-20 (1) (the head-weighted strike impact, `K_STR_HEAD`) moves a one-season run that reaches `strike_impact`.
#: B10-13 batch pin commit (the batch's declared movers, CR-27 `lie` among them, move a one-season realm of every seed):
#: was d4c83c8c... / 7cacc763... / 447ed0d8....
#: B10-12 pin commit (CR-24 `field_winner_casualties: engine` and MB-07r's support cap move a one-season realm that fights;
#: control: both reverted reads the old pin): seed 2 was 77a09697....
POST_ITEM = {0: "256606154c30542f9456b2fe15c76f09", 1: "aa58ef0b71c947ce5ff9f0a75ffd8ca6", 2: "a21ab6e12e356ccc4261bec1c93ca3b4"}
BUILD = "600d8b27147478e158553552cc1409a5"


def revert_cp_t03_08(monkeypatch):
    """The item OFF, in process: `tend` declares no `referent_class` (it forms on plain referents, as before) and the
    `wounded_with` term stamps nobody. Other tests that pin a pre-item hash call it."""
    monkeypatch.setitem(VERB_TABLE, "tend", replace(VERB_TABLE["tend"], referent_class=""))
    monkeypatch.setattr(world_q, "wounded_with", lambda w, p: ())


def _believe(w, holder, about, v, cid="c_body", when=0, rnd=0):
    """`holder` holds `(about, "body", v)` -- the Observation CP-T03-02 deposits to a fight's actor."""
    w.persons[holder].ledger.append(Claim(cid, holder, about, world_q.BODY_STEM, v, when, "firsthand", 100, "own",
                                          round=rnd))


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


def test_mutation_a_stamper_reading_true_bodies_is_red():
    def true_bodies(w, p):
        here = world_q.place_of(w, p.id)
        return tuple([p.id] if p.body < p.body_ceiling else []) + tuple(
            q.id for q in sorted(w.persons.values(), key=lambda x: x.id)
            if q.id != p.id and q.body < q.body_ceiling and world_q.place_of(w, q.id) == here)
    bad = _lawful_input_violations(true_bodies)
    assert "an unwitnessed wound is stamped for a stranger" in bad, bad
    assert len(bad) >= 2, bad


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


# ---- (iv) hash: mover, and the revert -----------------------------------------------------------------------------

@pytest.mark.parametrize("seed", [0, 1, 2])
def test_hash_post_item_and_revert(seed, monkeypatch):
    # CR-79's credit term (a later mover of the told deposit) is reverted in process: POST_ITEM reads this item alone.
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)
    # B11 lane A (the duel chain's reach, a later formation mover of every season) is reverted in process, so
    # POST_ITEM still reads this item alone.
    from .test_b11a_duel_reach import revert_b11a
    revert_b11a(monkeypatch)
    from .test_b11a_scores_and_obstacle import revert_b11a_scores
    revert_b11a_scores(monkeypatch)   # B11 lane A (persons hold scores; the obstacle by task: a mover of the build and every season), the same way
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == POST_ITEM[seed] != PRE_ITEM[seed]
    revert_cp_t03_08(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == PRE_ITEM[seed]


def test_rem52s_fall_is_tended_whole_the_same_season():
    """THE REALM READING THE ITEM MAKES, PINNED (seed 0, one season): REM-52's hunger lowers every short cohort's body in
    MATTER, `wounded_with` stamps each for himself below his ceiling, and `_eff_tend` restores the whole headroom -- so
    every short person stands whole at the season's end, each named by a `body.tended`. A finding about `_eff_tend`'s
    whole-headroom magnitude (CP-T10-04's `tend_share`, unbuilt), not a claim that it is right."""
    w = build_realm(0)
    run(1, 0, w=w)
    short = {pid for pid in w._subsistence_shortfall if pid in w.persons}
    tended = {c.subject for e in w.log if e.kind == "body.tended" for c in e.changes}
    assert short, "setup: nobody went hungry"
    assert short <= tended, sorted(short - tended)
    assert all(w.persons[pid].body == w.persons[pid].body_ceiling for pid in short)
    # B11 lane A (the duel chain's reach; re-pinned in B01.02): (37, 37) -> (37, 38): one person tended who was not short
    # (`p_npc_033`, wounded by the reach's new formations). With `revert_b11a_scores` alone it reads (37, 38); with
    # `revert_b11a` too, (37, 37) (scratch, not kept).
    # B01a.99 (every person's attributes are drawn, a population change): (37, 38) -> (37, 37): the duels the drawn sheets
    # resolve do not wound `p_npc_033`, so the tended are exactly the short (`tended - short` and `short - tended` both empty,
    # read in process at PYTHONHASHSEED=0).
    assert (len(short), len(tended)) == (37, 37)
    assert tended == short


def test_build_hash_is_unmoved(monkeypatch):
    from .test_b11a_scores_and_obstacle import revert_b11a_scores
    revert_b11a_scores(monkeypatch)   # B11 lane A (persons hold scores: a later mover of the build), so BUILD stands
    assert build_realm(0).content_hash() == BUILD
