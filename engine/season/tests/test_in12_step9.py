"""Plan position IN-12 step 9 (`workplans/valoria_master_workplan_v9_part5.md`, table row 9), #453 §10.4
step 9 -- `sabotage` (with `work`'s declared delta restricted to >= 0), `tend`, `argue`, `train` (with
`Person.capability` un-retired; `Person.pursuits`' `unproduced:` line already struck by SC-02 `22b` step 24).

⚠ A PROPERTY, NOT A REALM COUNT. Every falsifier drives its verb on a HAND-BUILT world through the real
fold (`SeasonDriver.resolve`, the gate, and for `argue` the social contest seam); `sabotage`, `tend` and
`train` are FORMED by the real `opening_set` and packed by the real `pack_scenes` first. NO TEST HERE
ASSERTS A REALM EXECUTION COUNT (v9 §0.5, RULED 2026-10-13 *"Relax exit rules"*).

The four EXIT clauses (#453 §10.4 step 9, verbatim), one block each:

  1. `sabotage` -- *"condition falls with a `sabotage` among its causes"*: a computed `sabotage` at a
     site the saboteur stands at lowers `Site.condition`, and the `site.damaged` Event cites the act.
     CONTROLS: a fabric at 0 is refused and unmoved; `work`'s declared delta < 0 is declined (K-09)
     while a declared delta > 0 still stages.
  2. `tend` -- *"`Person.body` rises"*: a computed `tend` of a wounded person who stands with the tender
     raises his body to the scale. CONTROLS: a whole body is refused; an absent patient is refused.
  3. `argue` -- *"`Person.pursuits` moves"*: a won argument moves the hearer's held pursuits toward the
     arguer's; a lost one moves nothing. CONTROLS: `pursuit_shift` 0 moves nothing at any band; a subject
     that is no Proposition is refused.
  4. `train` -- *"`sigma.faculty` varies by person"* [under J-13 (iii): only where a case names a
     vocation]: in NPC-088's case world, Carin (`p_a`, `{copying: 3}`) forms `train` carrying `copying`,
     the fold raises it to 4, and `faculty` reads 4 for her and `pool_default` for the others. CONTROLS:
     a pupil holding none is refused at the effect and nothing is minted; the formation is the same
     whatever the actor's capability (#353 §9.2, probe P11) -- J-13 (iii)'s *"forms ... only where"*
     half is NOT built, because it would be a capability gate (the receipt names this).

MUTATIONS, each run at the build 2026-10-21 (RED, then restored and GREEN):
  * sabotage: `loop/effects_economy.py::_fall` returning 0 -> block 1's falsifier RED (`sabotage.refused`,
    condition unchanged). Also run IN-TEST (`test_mutation_sabotage_with_no_fall_is_refused`).
  * tend: `loop/effects_combat.py::_eff_tend` writing `p.body` back unchanged -> block 2's falsifier RED.
  * argue: `queries/person_q.py::argued_pursuits` moving AWAY from the arguer (`w - ...`) -> block 3's
    direction assertion RED; returning `None` -> the falsifier RED (`argument.refused`). The `None` arm is
    also run IN-TEST (`test_mutation_argue_with_no_pursuit_move_is_refused`).
  * train: `rosters.yaml: vocation_sourced` emptied -> block 4's formation RED. Run IN-TEST
    (`test_mutation_without_the_vocation_line_train_is_not_formed`). And the write:
    `loop/effects_combat.py::_eff_train` raising by 0 -> block 4's falsifier RED (`train.refused`).
  * work (K-09): the `d < 0` decline in `loop/effects_economy.py::_eff_work` disabled -> block 1's
    `test_k09_works_declared_delta_is_restricted_to_non_negative` RED.
"""

from __future__ import annotations

import pytest

from ..data import verbs as VERBS
from ..data.matrix import MATRIX, MATRIX_RETIRED, WriteClass
from ..data.rosters import PURSUIT_AXES, PURSUITS, table, table_meta
from ..data.verbs import KIND_VERB, VERB_TABLE
from ..decision import assemble
from ..decision import options as OPT
from ..decision.options import opening_set
from ..gaps import Forbidden
from ..harness import probes as P
from ..loop import effects_economy as ECON
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import person_q as PQ
from ..seam.wrappers import sigma
from ..state.carriers import Act, Person, Question, StateChange
from .test_in10_record_operands import _acts, _resolve

NEW = ("argue", "sabotage", "tend", "train")


def _kinds(events):
    return [e.kind for e in events]


def _world(fixtures=None):
    w = P.tiny_world(fixtures) if fixtures is not None else P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _formed(w, pid, verb, referent):
    """`pid`'s own option set on one question about `referent` -- the `verb` Candidates it forms."""
    p = w.persons[pid]
    q = Question(f"q:{verb}:{referent}", "claim_landed", (referent,), None)
    return [c for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == verb]


# ======================================================================================
# 0 -- THE ROWS
# ======================================================================================

def test_the_four_rows_are_resolvable_and_declared_uncelled():
    assert set(NEW) <= set(resolvable_verbs())
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    for v in NEW:
        assert str(uncelled.get(v) or "").strip(), v
        assert not [ax for ax in PURSUIT_AXES if v in cells[ax]], v
    assert VERB_TABLE["sabotage"].writes == ("Site.condition",) and not VERB_TABLE["sabotage"].counterparty
    assert VERB_TABLE["tend"].writes == ("Person.body",)
    assert VERB_TABLE["train"].writes == ("Person.capability",)
    assert VERB_TABLE["argue"].contests == "a proposition" and VERB_TABLE["argue"].counterparty == "to"


def test_capability_is_unretired_with_its_producer_and_pursuit_moved_is_a_shared_kind():
    assert ("Person", "capability") in MATRIX and ("Person", "capability") not in MATRIX_RETIRED
    assert not MATRIX[("Person", "capability")].unproduced
    assert not MATRIX[("Person", "pursuits")].unproduced, "SC-02 22b step 24 struck it; nothing left"
    emitters = sorted(v for v, r in VERB_TABLE.items() if "pursuit.moved" in set(r.emits))
    assert emitters == ["argue", "determine"], emitters
    assert "pursuit.moved" not in KIND_VERB, "a second emitter makes the kind shared"


# ======================================================================================
# 1 -- SABOTAGE: CONDITION FALLS WITH A SABOTAGE AMONG ITS CAUSES
# ======================================================================================

SITE, SABOTEUR = "site_harbour", "p_high"           # the Duke stands at S, where the harbour is


def _sabotage_acts(w):
    cands = [c for c in _formed(w, SABOTEUR, "sabotage", SITE) if c.operands.get("site") == SITE]
    assert cands, "no computed sabotage formed on the site the saboteur was asked about"
    return _acts(w, SABOTEUR, cands[:1])


def test_condition_falls_with_a_computed_sabotage_among_its_causes():
    w, d = _world()
    before = w.sites[SITE].condition
    assert before > 0
    (act,) = _sabotage_acts(w)
    assert act.verb == "sabotage"
    out = _resolve(w, d, act)
    assert _kinds(out) == ["site.damaged"], _kinds(out)
    after = w.sites[SITE].condition
    assert after < before, (before, after)
    (ev,) = out
    assert act.id in ev.causes, ev.causes


def test_control_a_fabric_at_zero_is_refused_and_unmoved():
    w, d = _world()
    w.sites[SITE].condition = 0
    (act,) = _sabotage_acts(w)
    assert _kinds(_resolve(w, d, act)) == ["sabotage.refused"]
    assert w.sites[SITE].condition == 0


def test_mutation_sabotage_with_no_fall_is_refused(monkeypatch):
    """THE NAMED MUTATION, RUN IN-TEST: `_fall` returning 0 stages nothing and the falsifier's fall is gone."""
    w, d = _world()
    before = w.sites[SITE].condition
    (act,) = _sabotage_acts(w)
    monkeypatch.setattr(ECON, "_fall", lambda w, site: 0)
    assert _kinds(_resolve(w, d, act)) == ["sabotage.refused"]
    assert w.sites[SITE].condition == before


def test_a_sabotage_a_restore_cancels_is_refused_after_the_fact():
    """One formula, two signs, one accumulator (S27.3): at a fabric standing at half its scale, a `restore`
    stages +headroom and a `sabotage` -footroom, equal, by the same actor (the same share). The sum is 0,
    the clamp writes nothing, and BOTH are refused in place (`_refuse_after_the_fact`), the site unmoved.
    CONTROL: the `sabotage` alone lowers the same fabric."""
    w, d = _world()
    half = w.fixtures.get("condition_scale") // 2
    w.sites[SITE].condition = half
    acts = [Act(id=k, actor=SABOTEUR, verb=v, payload={"site": SITE, "subject": SITE})
            for k, v in (("cx_r", "restore"), ("cx_s", "sabotage"))]
    out = _resolve(w, d, *acts)
    assert {e.causes[0]: e.kind for e in out} == {"cx_r": "restore.refused", "cx_s": "sabotage.refused"}, (
        [(e.causes[0], e.kind) for e in out])
    assert w.sites[SITE].condition == half
    w2, d2 = _world()
    w2.sites[SITE].condition = half
    assert _kinds(_resolve(w2, d2, acts[1])) == ["site.damaged"]
    assert w2.sites[SITE].condition < half


def _work(delta, key):
    return Act(id=key, actor=SABOTEUR, verb="work", payload={"site": SITE, "subject": SITE},
               changes=[StateChange(SITE, "alter", "Act", "condition", delta)])


def test_k09_works_declared_delta_is_restricted_to_non_negative():
    """K-09: each verb owns one sign. A hand-built `work` declaring a NEGATIVE delta is declined
    (`work.unavailable`) and the site is unmoved; CONTROL, one change: the same act declaring a positive
    delta on a site below the scale still stages and raises it."""
    w, d = _world()
    before = w.sites[SITE].condition
    assert _kinds(_resolve(w, d, _work(-50, "wk_neg"))) == ["work.unavailable"]
    assert w.sites[SITE].condition == before
    assert _kinds(_resolve(w, d, _work(+50, "wk_pos"))) == ["site.worked"]
    assert w.sites[SITE].condition == before + 50


# ======================================================================================
# 2 -- TEND: PERSON.BODY RISES
# ======================================================================================

TENDER, PATIENT = "p_low", "p_mid"                  # both stand at the hearth Hh


def _tend_acts(w, patient=PATIENT):
    cands = [c for c in _formed(w, TENDER, "tend", patient) if c.subject == patient]
    assert cands, "no computed tend formed on the person the tender was asked about"
    return _acts(w, TENDER, cands[:1])


def test_person_body_rises_under_a_computed_tend():
    w, d = _world()
    scale = w.fixtures.get("condition_scale")
    w.persons[PATIENT].body = scale * 2 // 5
    (act,) = _tend_acts(w)
    assert _kinds(_resolve(w, d, act)) == ["body.tended"]
    assert w.persons[PATIENT].body == scale


def test_control_a_whole_body_is_refused():
    w, d = _world()
    scale = w.fixtures.get("condition_scale")
    assert w.persons[PATIENT].body == scale
    (act,) = _tend_acts(w)
    assert _kinds(_resolve(w, d, act)) == ["tend.refused"]


def test_control_an_absent_patient_is_refused_and_unmoved():
    w, d = _world()
    absent = "p_king"                                  # at the realm, not at the hearth
    low = w.fixtures.get("condition_scale") // 2
    w.persons[absent].body = low
    (act,) = _tend_acts(w, absent)
    assert _kinds(_resolve(w, d, act)) == ["tend.refused"]
    assert w.persons[absent].body == low


# ======================================================================================
# 3 -- ARGUE: PERSON.PURSUITS MOVES
# ======================================================================================

ARGUER, HEARER = "p_low", "p_mid"


def _argue_world(shift=None):
    fx = P.DEFAULT_FIXTURES if shift is None else P.DEFAULT_FIXTURES.sweep("pursuit_shift", shift)
    w, d = _world(fx)
    a, b = sorted(PURSUITS)[:2]
    w.persons[ARGUER].pursuits = {a: 0.9, b: 0.1}
    w.persons[HEARER].pursuits = {a: 0.1, b: 0.9}
    out = _resolve(w, d, Act(id="ar_u", actor=ARGUER, verb="utter"))
    assert _kinds(out) == ["proposition.uttered"]
    return w, d, "prop:ar_u", (a, b)


def _argue(pid, key, to=HEARER):
    return Act(id=key, actor=ARGUER, verb="argue", payload={"subject": pid, "to": to})


def _bands(shift=None, n=40):
    """`{band: [(kinds, hearer pursuits before, after)]}` over `n` act ids, each on a fresh world."""
    seen: dict = {}
    for i in range(n):
        w, d, pid, keys = _argue_world(shift)
        before = dict(w.persons[HEARER].pursuits)
        out = _resolve(w, d, _argue(pid, f"ar_{i}"))
        assert len({e.degree for e in out}) == 1, [(e.kind, e.degree) for e in out]
        seen.setdefault(out[0].degree, []).append((_kinds(out), before, dict(w.persons[HEARER].pursuits), keys))
    return seen


def test_person_pursuits_moves_under_a_won_argue_and_toward_the_arguer():
    seen = _bands()
    won = seen.get("Success", []) + seen.get("Overwhelming", [])
    assert won, f"no argue reached a moving band over 40 acts: {sorted(seen, key=str)}"
    checked = 0
    for kinds, before, after, (a, b) in won:
        assert kinds == ["argument.won", "pursuit.moved"], kinds
        assert after != before
        assert after[a] > before[a] and after[b] < before[b], (before, after)   # toward the arguer
        checked += 1
    for kinds, before, after, _ in seen.get("Failure", []) + seen.get("Partial", []):
        assert after == before, (kinds, before, after)
        assert kinds in (["argument.lost"], ["argument.won"]), kinds
        checked += 1
    assert checked == 40


def test_control_at_pursuit_shift_zero_no_band_moves_a_pursuit():
    seen = _bands(shift=0, n=24)
    checked = 0
    for band, rows in seen.items():
        for kinds, before, after, _ in rows:
            assert after == before, (band, before, after)
            assert "pursuit.moved" not in kinds, (band, kinds)
            checked += 1
    assert checked == 24


def test_mutation_argue_with_no_pursuit_move_is_refused(monkeypatch):
    """THE NAMED MUTATION, RUN IN-TEST: `argued_pursuits` answering `None` -> a won argument moved nothing
    and is refused at its write; no band moves the hearer."""
    import importlib
    eff = importlib.import_module("engine.season.loop.effects_information")
    monkeypatch.setattr(eff, "argued_pursuits", lambda *a, **k: None)
    seen = _bands(n=24)
    refused = 0
    for band, rows in seen.items():
        for kinds, before, after, _ in rows:
            assert after == before
            if band in ("Success", "Overwhelming"):
                assert kinds == ["argument.refused"], (band, kinds)
                refused += 1
    assert refused >= 1, f"no won band among the 24 acts, so the mutation was not observed: {sorted(seen, key=str)}"


def test_control_a_subject_that_is_no_proposition_is_refused():
    w, d, _pid, _ = _argue_world()
    before = dict(w.persons[HEARER].pursuits)
    assert _kinds(_resolve(w, d, _argue("p_other", "ar_np"))) == ["argument.refused"]
    assert w.persons[HEARER].pursuits == before


def test_argued_pursuits_moves_only_held_keys_and_needs_a_moving_band():
    """The reader alone, on planted persons: a pursuit the hearer does not hold is never minted; Partial
    and Failure move nothing; Overwhelming moves twice as far as Success (the one ladder)."""
    a, b, c = sorted(PURSUITS)[:3]
    h, r = Person("h", "h"), Person("r", "r")
    h.pursuits, r.pursuits = {a: 0.2, b: 0.0}, {a: 1.0, c: 1.0}
    s = PQ.argued_pursuits(h, r, "Success", 0.1)
    o = PQ.argued_pursuits(h, r, "Overwhelming", 0.1)
    assert set(s) == {a, b} and s[b] == 0.0, s
    assert s[a] == pytest.approx(0.2 + 0.1 * 1 * 0.8) and o[a] == pytest.approx(0.2 + 0.1 * 2 * 0.8)
    assert PQ.argued_pursuits(h, r, "Partial", 0.1) is None
    assert PQ.argued_pursuits(h, r, "Failure", 0.1) is None


# ======================================================================================
# 4 -- TRAIN: SIGMA._POOL_OF VARIES BY PERSON, WHERE A CASE NAMES A VOCATION (NPC-088)
# ======================================================================================

def _npc088():
    from ..harness import corpus_run as C
    from ..harness import run_cases as R
    npc = {c["id"]: c for c in R.load_cases("NPC")}
    w = C.build_at(npc["NPC-088"], seed=0)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


CARIN = "p_a"


def test_faculty_varies_by_person_once_train_raises_carins_vocation():
    w, d = _npc088()
    fx = w.fixtures
    carin = w.persons[CARIN]
    assert carin.capability == {"copying": 3}, carin.capability
    others = [p for pid, p in sorted(w.persons.items()) if pid != CARIN and not p.capability]
    assert others, "no person without a capability to compare against"
    cands = _formed(w, CARIN, "train", CARIN)
    assert cands and all(c.operands.get("kind") == "copying" for c in cands), [c.operands for c in cands]
    (act,) = _acts(w, CARIN, cands[:1])
    assert act.payload["kind"] == "copying"
    assert _kinds(_resolve(w, d, act)) == ["capability.raised"]
    assert carin.capability == {"copying": 4}
    pools = {p.id: sigma.faculty(w, p, "tell") for p in [carin, *others]}
    assert pools[CARIN] == 4, pools
    assert {pools[p.id] for p in others} == {fx.get("pool_default")}, pools
    assert len(set(pools.values())) > 1, pools


def test_a_planted_addend_registered_through_faculty_is_read_by_the_roll_and_the_odds(monkeypatch):
    """CP-T01-01's falsifier: the registry is what `faculty` sums, so a rename that ignored it would
    not see this addend. It is read by the dealt record (`contest_input`) and by the person's own odds
    (`odds_of` mode (b)), the two ways the pool is read; and it moves nobody who is not its subject."""
    w, _d = _npc088()
    carin = w.persons[CARIN]
    other = next(p for pid, p in sorted(w.persons.items()) if pid != CARIN and not p.capability)
    base = {p.id: sigma.faculty(w, p, "tell") for p in (carin, other)}
    monkeypatch.setattr(sigma, "POOL_ADDENDS", list(sigma.POOL_ADDENDS))
    sigma.register_pool_addend(lambda w_, p, verb: 2 if (p.id == CARIN and verb == "tell") else 0)
    assert sigma.faculty(w, carin, "tell") == base[CARIN] + 2
    assert sigma.faculty(w, other, "tell") == base[other.id]            # keyed by the person it names
    assert sigma.faculty(w, carin, "determine") == w.fixtures.get("pool_default")   # the addend names a verb
    inp = sigma.contest_input(w, [CARIN], verb="tell", subject=other.id, room=None, examined=None)
    assert inp.pool == base[CARIN] + 2, inp.pool


def test_capability_gates_no_train_the_formation_never_reads_the_actors_capability():
    """#353 §9.2 / probe P11: the option set does not move with the actor's capability -- none, a zeroed
    key, a high one. So J-13 (iii) is built as its WRITE half (the effect), never as a formation gate."""
    w, _d = _npc088()
    other = next(pid for pid, p in sorted(w.persons.items()) if pid != CARIN and not p.capability)
    seen = []
    for cap in ({}, {"copying": 0}, {"copying": 9}):
        w.persons[other].capability = dict(cap)
        seen.append(sorted((c.subject, c.operands.get("kind")) for c in _formed(w, other, "train", other)))
    assert seen[0] and seen[0] == seen[1] == seen[2], seen


def test_control_a_pupil_holding_no_vocation_is_refused_at_the_effect():
    w, d = _npc088()
    pupil = next(pid for pid, p in sorted(w.persons.items()) if pid != CARIN and not p.capability)
    act = Act(id="tr_pupil", actor=CARIN, verb="train", payload={"subject": pupil, "kind": "copying"})
    assert _kinds(_resolve(w, d, act)) == ["train.refused"]
    assert w.persons[pupil].capability == {}, "a key was minted below pool_default"


def test_mutation_without_the_vocation_line_train_is_not_formed(monkeypatch):
    """THE NAMED MUTATION, RUN IN-TEST: `vocation_sourced` emptied -> `train` forms on Carin with no
    vocation on it, and the act the falsifier folds can no longer carry `copying`."""
    w, _d = _npc088()
    assert _formed(w, CARIN, "train", CARIN), "precondition: the shipped line forms it"
    monkeypatch.setattr(OPT, "VOCATION_SOURCED", {})
    assert not [c for c in _formed(w, CARIN, "train", CARIN) if c.operands.get("kind") == "copying"]


def test_a_vocation_sourced_line_naming_no_capability_writer_is_refused_at_load():
    assert VERBS._load_vocation_sourced({"train": "kind"}) == VERBS.VOCATION_SOURCED == {"train": "kind"}
    for planted in ({"tend": "kind"}, {"train": "no_such_operand"}, {"no_such_verb": "kind"}):
        with pytest.raises(Forbidden, match="vocation_sourced"):
            VERBS._load_vocation_sourced(planted)
