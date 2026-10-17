"""v9 SC-02 `22b`, proceedings `19_PLAN.md` step 23 -- PRESSURE SURFACES AS A STANDING BAND CROSSING,
ABOUT SOMEONE.

*"Add person-keyed [crossings]: recompute the standing gap over past claims versus all claims; if the
band differs, record a crossing whose causes are the deposits that composed the gap. The question's
referents are the people whose claims made it."* Falsifier: *"a crossing produces a write rather than a
question."* Artifact: *"the bailiff is told three things about himself; his standing crosses; his first
question next season names the tellers; he opens a case against one of them -- who may have said
nothing."*

BUILT ON A HAND-BUILT WORLD (v9 §0.5, RULED 2026-10-13): in the seed-0 realm no deposit mints a claim on
a `person_predicates` member (`hole_register.yaml` H-222; the writer is step 19, H-218), so the gap is
the constant `condition_scale` there and the crossing cannot fire in computed play. Here the cause is
controlled: the bailiff's own firsthand claims about himself are PLANTED (what step 19 would write), and
what he is told arrives through the REAL told channel (`loop/witness.py`), one WITNESS barrier, so every
told claim has a real `claim.deposited` Event and a real `chain`; the crossing is MATTER's
(`loop/matter.py::_standing_crossings`) and the question `questions_for`'s.

The fixture is `probes.tiny_world` with everybody moved into `S` beside `p_high` (`test_told_by_channel.
py::_t5_world`'s construction). `p_high` is the bailiff: he holds `off_duke` (grant includes `open_case`,
scope `D`). `p_low` is an ORIGIN who never speaks to him -- `p_mid` retells `p_low`'s claim -- so `p_low`
is the teller who "may have said nothing".
"""

from __future__ import annotations

import yaml

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..decision import aggregate_questions, opening_set, standing_of
from ..decision.choose import pack_scenes
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..queries.world_q import STANDING_CROSSED
from ..state.carriers import Act, Claim, Event, Said, View
from ..state.ids import H
from pathlib import Path

BAILIFF, SEAT = "p_high", "off_duke"
ORIGIN = "p_low"                    # told p_mid; never spoke to the bailiff
TELLERS = (ORIGIN, "p_mid", "p_other")
# What the bailiff holds true of himself BEFORE he is told anything (planted: step 19's writer, H-218).
OWN_BEFORE = {"grade": "noble"}
TOLD = (                            # (teller, prior chain, predicate, value)
    ("p_mid", (ORIGIN,), "residence", "S"),      # p_low's claim, retold by p_mid
    ("p_other", (), "grade", "base"),            # contradicts what he holds
    ("p_mid", (), "church_standing", "lay"),
)
# What he comes to hold true himself AFTER the telling, in the same season (planted, as above). ⚠ IT
# MUST COME AFTER: `loop/witness.py`'s exact-triple guard (`T5`) deposits no told claim the hearer
# already holds firsthand, so a telling that AGREES with a belief he already had never lands, and the
# told side of `agreement` can agree only with a belief formed after it
# (`test_step23_a_telling_that_agrees_with_a_belief_already_held_never_lands_so_nothing_crosses`).
OWN_AFTER = {"residence": "S", "church_standing": "lay"}
LIVE, CONTROL = (500,), ()
T = 3                               # the season of the telling


def _own(w, beliefs, when):
    for pred, value in sorted(beliefs.items()):
        w.persons[BAILIFF].ledger.append(Claim(f"c_own_{pred}_{when}", BAILIFF, BAILIFF, pred, value,
                                               when, "firsthand", 100, "own"))


def _world(floors=LIVE, told=TOLD, before=OWN_BEFORE, after=OWN_AFTER):
    """The bailiff, holding `before`, told `told` in ONE WITNESS barrier at tick `T`, then holding
    `after` too; returns `(w, d)` with the tick advanced to `T + 1` and nothing of that season run."""
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("standing_band_floors", floors))
    for pid in ("p_mid", "p_other", "p_low"):
        edge = next(t for t in w.tenures if t.subject == pid and t.kind == "contain" and t.live)
        edge.object = "S"
    _own(w, before, 0)
    w.tick = T
    d = SeasonDriver(w)
    evs = []
    for n, (teller, chain, pred, value) in enumerate(told):
        act = Act(id=f"a_tell_{n}", actor=teller, verb="tell",
                  payload={"subject": BAILIFF, "said": Said(BAILIFF, pred, value, 100, chain)})
        w.acts.append(act)
        ev = Event(H(w.world_seed, w.tick, teller, f"ev:news.told:{act.id}"), "news.told",
                   [], [act.id], w.tick, "Success", ())
        w.log.append(ev)
        d.act_of[ev.id] = act
        evs.append(ev)
    d.witness(mint_token(w, WriteClass.INTERIOR), evs)
    _own(w, after, w.tick)
    w.tick += 1
    return w, d


def _told(w):
    return [c for c in w.persons[BAILIFF].ledger if c.subject == BAILIFF and c.source == "told_by"]


def _crossings(w):
    return [e for e in w.log if e.kind == STANDING_CROSSED]


def _matter(w, d):
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _state_digest(w):
    """`World.content_hash` over the STATE alone -- every collection, tenure and the docket, the log
    swapped out -- so two arms that differ only by a logged record read equal, and any write differs."""
    log, w.log = w.log, []
    try:
        return w.content_hash()
    finally:
        w.log = log


def _crossing_question(w):
    xs = _crossings(w)
    return [q for q in world_q.questions_for(w, w.persons[BAILIFF]) if xs and q.about == xs[0].id]


# ======================================================================================
# THE ARTIFACT
# ======================================================================================

def test_step23_the_bailiff_told_three_things_crosses_and_his_question_names_the_tellers():
    """Told three things about himself, through the real told channel; his standing gap moves from
    `condition_scale` (no pair) to 333 (three pairs, one contradiction) across the shipped floor (500);
    MATTER records ONE crossing whose causes are the three told claims' deposits; the next season's
    question about it names the tellers, origin first -- `p_low` among them, who never spoke to him."""
    w, d = _world()
    told = _told(w)
    assert len(told) == 3 and all(c.chain for c in told), [(c.predicate, c.chain) for c in told]
    assert [c for c in told if c.predicate == "residence"][0].chain == (ORIGIN, "p_mid")
    assert not any(a.actor == ORIGIN for a in w.acts), "p_low spoke; he must have said nothing"
    bailiff = w.persons[BAILIFF]
    scale = w.fixtures.get("condition_scale")
    assert standing_of(bailiff, w.fixtures) == scale // 3, "the gap did not move to 1 of 3"

    _matter(w, d)
    xs = _crossings(w)
    assert len(xs) == 1, f"{len(xs)} standing crossings for one band change"
    x = xs[0]
    assert x.id == world_q.standing_crossing_id(w, BAILIFF) and x.emitted_at == w.tick
    deposits = {w.last_emission_of("claim.deposited", c.id) for c in told}
    assert None not in deposits and set(x.causes) == deposits, (
        f"the crossing's causes {x.causes} are not the deposits that composed the gap {deposits}")

    q, = _crossing_question(w)
    assert q.source == "claim_landed" and q.referents == TELLERS, q
    assert world_q.occasioned_by(w, q) == [x.id], "an act formed from the question would not cite the crossing"


def test_step23_he_opens_a_case_against_one_of_them_who_may_have_said_nothing():
    """The crossing changes what can be chosen: the bailiff's opening set over the crossing's question
    holds `open_case` on `p_low`, the origin who never spoke to him; released and folded as DELIBERATE
    would, it opens the case and the case's Event walks back to the crossing. CONTROL, the same world at
    the control arm `()`: no crossing, and NO question he holds names `p_low`, so no candidate on him
    forms at all -- the telling's own claims are about the bailiff, and `p_low` reaches him only
    through the crossing."""
    w, d = _world()
    _matter(w, d)
    bailiff = w.persons[BAILIFF]
    q, = _crossing_question(w)
    cands = [c for c in opening_set(bailiff, View(BAILIFF, [], w.fixtures.get("view_k"), q), q, w.fixtures)
             if c.verb == "open_case" and c.subject == ORIGIN]
    assert cands, "no `open_case` on the silent origin formed from the crossing's question"
    acts = []
    for sc in pack_scenes(bailiff, cands[:1], 5, w.fixtures, lambda pid, verb, s: f"s23:{verb}:{s}",
                          occasion=q):
        d.scenes[sc.id] = sc
        for a in sc.acts:
            a.scene = sc.id
            acts.append(a)
    out = d.resolve(mint_token(w, WriteClass.ACTS), acts, contest_max_depth=w.fixtures.get("contest_max_depth"))
    opened = [e for e in out if e.kind == "case.opened"]
    assert opened, f"the case was not opened: {[e.kind for e in out]}"
    assert _crossings(w)[0].id in opened[0].causes, (opened[0].causes, "the case does not cite the crossing")

    wc, dc = _world(CONTROL)
    _matter(wc, dc)
    assert _crossings(wc) == []
    qs = world_q.questions_for(wc, wc.persons[BAILIFF])
    assert qs and not any(ORIGIN in q.referents for q in qs), [q.referents for q in qs]
    assert not any(c.verb == "open_case" and c.subject == ORIGIN for q in qs
                   for c in opening_set(wc.persons[BAILIFF], View(BAILIFF, [], wc.fixtures.get("view_k"), q),
                                        q, wc.fixtures))


# ======================================================================================
# THE FALSIFIER: a crossing produces a write rather than a question
# ======================================================================================

def test_step23_falsifier_a_crossing_writes_nothing_and_only_raises_a_question():
    """The live arm and the control arm `()`, the same world through the same MATTER barrier: the
    WORLD STATE is byte-identical (`content_hash` over every collection, tenure and the docket, the log
    swapped out), and the logs differ by exactly the one crossing, which carries no change. So the
    crossing wrote nothing -- through the gate (a gate write emits, and would show in the log) or
    around it (a direct mutation shows in the state) -- and what it adds is the question.

    MUTATION (run 2026-10-17): `_standing_crossings` appending a claim to the person's ledger beside
    the record (a write around the gate) -- this goes RED on the state digest. Restored, GREEN. (A gate
    write would also emit, and so fail the log comparison; that arm was not run.)"""
    w, d = _world(LIVE)
    wc, dc = _world(CONTROL)
    assert _state_digest(w) == _state_digest(wc), "the arms differ before MATTER; fixture moved"
    _matter(w, d)
    _matter(wc, dc)
    x, = _crossings(w)
    assert x.changes == [], f"the crossing carries changes {x.changes}"
    assert _state_digest(w) == _state_digest(wc), "the crossing wrote to the world"
    live = [(e.id, e.kind) for e in w.log]
    control = [(e.id, e.kind) for e in wc.log]
    assert [k for k in live if k != (x.id, x.kind)] == control and len(live) == len(control) + 1, (
        "the crossing emitted something besides its own record")
    assert any(x.id == q.about for q in world_q.questions_for(w, w.persons[BAILIFF]))


# ======================================================================================
# ONCE, AND THE SWEEP
# ======================================================================================

def test_step23_a_crossing_is_new_once_neither_after_he_deliberates_nor_next_season():
    """The record precedes round 0, so the question is new until the bailiff deliberates this season
    (`since = (tick, 0)` hides it) -- and the next MATTER, with nothing landed since, records nothing."""
    w, d = _world()
    _matter(w, d)
    bailiff = w.persons[BAILIFF]
    assert _crossing_question(w)
    assert not [q for q in world_q.questions_for(w, bailiff, since=(w.tick, 0))
                if q.about == _crossings(w)[0].id], "a crossing asked again after he deliberated"
    w.tick += 1
    _matter(w, d)
    assert len(_crossings(w)) == 1, "a second crossing with nothing landed"
    assert not [q for q in world_q.questions_for(w, bailiff) if q.about == _crossings(w)[0].id]


def _h223_sweep():
    rows = yaml.safe_load((Path(__file__).resolve().parents[1] / "hole_register.yaml").read_text())
    row, = [r for r in rows["rows"] if r["id"] == "H-223"]
    return [tuple(arm) for arm in row["sweep"]]


def test_step23_the_h223_sweep_the_control_arm_crosses_nothing():
    """Every arm of `H-223`'s declared sweep, the shipped one included: a gap moving 1000 -> 333 crosses
    every arm with a floor in (333, 1000], and the control `()` -- one band -- crosses nothing."""
    arms = _h223_sweep()
    assert CONTROL in arms and DEFAULT_FIXTURES.get("standing_band_floors") in arms, arms
    for arm in arms:
        w, d = _world(arm)
        _matter(w, d)
        crossed = any(333 < f <= 1000 for f in arm)
        assert bool(_crossings(w)) == crossed, (arm, len(_crossings(w)))


# ======================================================================================
# WHAT IT DOES NOT DO, PINNED AS IT READS
# ======================================================================================

def test_step23_limit_the_attention_order_puts_the_crossing_question_last():
    """THE LIMIT `H-222` (1) RECORDS: *his first question next season names the tellers* is not
    something this step makes true. `attention_key` (v9 IN-57) puts the crossing's question in tier 1
    (the tellers stand inside his seat's purview) BESIDE the claims about himself, and inside a tier it
    ranks nothing (IN-57's own LIMIT): the tie goes to the question id, a hash. Here it sorts last, so
    `question_aggregation_rule: first` delivers another; under `all` the tellers ARE delivered. Ranking
    a crossing within its tier is IN-57's design, not this step's."""
    w, d = _world()
    _matter(w, d)
    bailiff = w.persons[BAILIFF]
    qs = world_q.questions_for(w, bailiff)
    q, = _crossing_question(w)
    key = world_q.attention_key(w, bailiff)
    assert key(q)[0] == key(qs[0])[0] == 1, (key(q), key(qs[0]))
    assert qs[0] != q and qs[-1] == q, [x.id for x in qs]
    assert ORIGIN not in aggregate_questions(qs, "first").referents
    assert set(TELLERS) <= set(aggregate_questions(qs, "all").referents)


def test_step23_breaks_if_wrong_a_man_told_only_what_he_denies_feels_nothing():
    """`19_PLAN.md` step 23, *breaks if wrong*: *"the standing measure is a gap, so a hated man who knows
    he is hated feels nothing"* (D-4 rules the polarity; the mechanism is the same either way). Told
    only contradictions, the gap stays at `condition_scale` -- the maximum, which is also what no pair
    reads -- so no band changes and nothing crosses."""
    w, d = _world(after={})
    bailiff = w.persons[BAILIFF]
    assert any(c.predicate == "grade" for c in _told(w))
    assert standing_of(bailiff, w.fixtures) == w.fixtures.get("condition_scale")
    _matter(w, d)
    assert _crossings(w) == []


def test_step23_a_telling_that_agrees_with_a_belief_already_held_never_lands_so_nothing_crosses():
    """THE LIMIT `H-222` RECORDS: the bailiff holds all three beliefs BEFORE he is told. The two tellings
    that agree deposit nothing (`loop/witness.py`'s exact-triple guard, `T5`), only the contradiction
    lands, the gap reads `condition_scale` and nothing crosses -- so in this design the told side of the
    gap agrees only with a belief formed AFTER the telling."""
    w, d = _world(before={**OWN_BEFORE, **OWN_AFTER}, after={})
    assert [c.predicate for c in _told(w)] == ["grade"], [(c.predicate, c.value) for c in _told(w)]
    _matter(w, d)
    assert _crossings(w) == []
