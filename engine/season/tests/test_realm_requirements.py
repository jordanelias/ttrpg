"""R-01, R-02 and their controls, read on the PLAYED REALM at three seeds.

`test_season_shape.py` asserts the claim-to-act chain on worlds built from corpus cases; these tests
read it on the world the game ships: `populated.build_realm(seed)` played one season on the shipped
policy (`probes.chooser` over `resolvable_verbs()`).

R-01.b, read here: an act formed from a `claim_landed` question, where the Event the question walks
back to (`world_q.occasioned_by`) was emitted by an act of a DIFFERENT person. The control removes the
cause: with `SeasonDriver.witness` returning 0 no claim is deposited through the witness, yet
`claim_landed` questions still form from the other deposit paths (`landed > 0` is asserted, so the zero
is not by construction), and the count of those walking back to another person's act must read 0. A
count that is positive with the witness cut would mean the counter reads something other than the chain.

R-02.a, read here: withholding what acts observe changes the acts that follow. One season at the shipped
fixtures and one with `observation_deposit_mode` swept to `none` (no act deposits what it read) give two
`(actor, verb, subject)` sequences that part, after a common prefix (the worlds start equal). The control
plays one seed twice at the shipped fixtures and must read one sequence; a parting there would mean the
sequence moves with nothing varied, and the parting above would prove nothing. ⚠ This reads that the
sequence parts when deposits are cut; it does not read that the fork-and-follow test's divergence is
caused by deposits (`test_season_shape.py` shows divergence in both arms).

R-07.d, read here: a feeling, attitude or relationship changes a decision. The first person (by id) who holds a
candidate about another person is ranked by the shipped ranker (`choose.make_ranker`, on his own View), then
again in a world where one stance row toward that subject was written through the gate (`World.write` on the
`(Person, stance)` row, with a token minted for the step). The top candidate about that subject must differ
in at least one seed. Two controls: the unplanted world ranks equal twice, and a row toward a person the
holder has no candidate about leaves the ranking equal (so the move is the row's term, not a write's side effect).
"""
from __future__ import annotations

import pytest

from ..data.cast import STANCE_VALENCE_SCALE
from ..data.fixtures import DEFAULT_FIXTURES, Fixtures
from ..data.matrix import Step, WriteClass
from ..data.verbs import VERB_TABLE
from ..decision import assemble, choose as CH
from ..harness import decision_spread as DS
from ..boot.realm import build_realm
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries.world_q import occasioned_by
from ..seam.wrappers import pool, sigma
from ..state.carriers import Act, subject_of
from ..state.gate import Change, Subject
from ..state.ids import draw_factory
from ..state.world import World

SEEDS = (0, 1, 2)


def _play(seed: int, fx: Fixtures | None = None) -> tuple[World, SeasonDriver]:
    """The shipped realm at `seed` (built on `fx`, None: the shipped fixtures), played one season."""
    w = build_realm(seed, fixtures=fx)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())
    d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


def _occasioned_by_another(w: World, d: SeasonDriver) -> tuple[int, int]:
    """(resolved acts whose scene's occasion is a `claim_landed` question and walks back to an Event
    emitted by an act of a different person, resolved acts whose occasion is `claim_landed`)."""
    hit = landed = 0
    for a in d.resolved:
        occ = getattr(w.acts.scene_of(a.id), "occasion", None)
        if getattr(occ, "source", None) != "claim_landed":
            continue
        landed += 1
        causes = (d.act_of.get(c) for c in occasioned_by(w, occ))
        if any(c is not None and c.actor != a.actor for c in causes):
            hit += 1
    return hit, landed


def _sequence(d: SeasonDriver) -> list[tuple[str, str, str | None]]:
    """The season's resolved acts in order, as `(actor, verb, subject)` (`subject_of`: None where none)."""
    return [(a.actor, a.verb, subject_of(a) or None) for a in d.resolved]


def _common_prefix(a: list, b: list) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


@pytest.mark.parametrize("seed", SEEDS)
def test_r01_an_act_is_occasioned_by_a_claim_that_walks_back_to_another_persons_act(seed):
    w, d = _play(seed)
    assert d.resolved, "no act resolved: the count below would read an empty season"
    hit, landed = _occasioned_by_another(w, d)
    assert landed > 0, "no resolved act came from a claim_landed question"
    assert hit > 0, (f"seed {seed}: {landed} acts came from a claim_landed question and none walks "
                     "back to another person's act")


def test_r01_control_with_witness_cut_no_act_is_so_occasioned(monkeypatch):
    # the cause removed: no deposit, so no claim lands and nothing walks back to another's act
    monkeypatch.setattr(SeasonDriver, "witness", lambda self, token, events: 0)
    w, d = _play(0)
    assert d.resolved, "no act resolved with the witness cut: the zero below would be an empty season"
    hit, landed = _occasioned_by_another(w, d)
    assert landed > 0, "no claim_landed question formed with the witness cut: the zero below would hold by construction"
    assert hit == 0


@pytest.mark.parametrize("seed", SEEDS)
def test_r02_withholding_what_acts_observe_changes_later_acts_at_the_shipped_budget(seed):
    _w, shipped = _play(seed)
    _w, withheld = _play(seed, DEFAULT_FIXTURES.sweep("observation_deposit_mode", "none"))
    a, b = _sequence(shipped), _sequence(withheld)
    assert a and b, "an arm resolved no act: the comparison below would read an empty season"
    assert a != b, f"seed {seed}: cutting observation deposits left the resolved sequence unchanged"
    prefix = _common_prefix(a, b)
    assert prefix > 0, f"seed {seed}: the arms part at the first act, so they did not start equal"


def test_r02_control_one_seed_played_twice_is_one_sequence():
    _w, first = _play(0)
    _w, again = _play(0)
    a, b = _sequence(first), _sequence(again)
    assert a, "no act resolved: the equality below would read an empty season"
    assert a == b


def _not_the_top(seed: int, fx: Fixtures | None = None) -> tuple[int, int]:
    """(deliberations in which the sampler's pick was not the leading candidate, deliberations with a strict
    top), one season through `decision_spread.play_season` (the chooser watched, never steered)."""
    sp = DS.play_season(build_realm(seed, fixtures=fx), 1)["split"]
    return sp["strict_outvoted"], sp["strict"]


@pytest.mark.parametrize("seed", SEEDS)
def test_r08_some_chosen_acts_were_not_the_top_candidate_and_none_at_zero_temperature(seed):
    shipped, deliberated = _not_the_top(seed)
    zero, zero_deliberated = _not_the_top(seed, DEFAULT_FIXTURES.sweep("choice_temperature", 0.0))
    assert deliberated > 0 and zero_deliberated > 0, "an arm deliberated over no strict top: the counts below read nothing"
    assert shipped > 0, f"seed {seed}: no deliberation chose other than its leading candidate at the shipped temperature"
    assert zero == 0, f"seed {seed}: {zero} deliberations chose other than the leading candidate at zero temperature"


def _tell(actor: str, to: str) -> Act:
    return Act(id=f"a:{actor}:{to}", actor=actor, verb="tell", payload={"to": to})


def test_r09_two_persons_of_different_skill_score_read_different_odds_in_the_realm():
    """R-09 (mechanism half) on the built realm: two persons alike in what governs `tell`'s pool and in body, holding
    skill scores 4 and 0 in `tell`'s skill, read different `sigma.odds_of` for `tell` to one third person. The control
    sets both to 4 and the tuples are equal. Nothing is patched: the persons' ranks are set on the `World` the reader reads.
    (The shipped-cast arm, no rank set by the test, moves to BA1's gate: the cast holds no skill scores yet.)"""
    w = build_realm(0)
    key = VERB_TABLE["tell"].capability
    assert key and key != "none", "`tell` names no skill: the test would set a key nothing reads"
    alive = [i for i, x in w.persons.items() if getattr(x, "alive", True)]
    assert len(alive) >= 3, "the realm holds fewer than three living persons"
    pair = next(((a, b) for n, a in enumerate(alive) for b in alive[n + 1:]
                 if w.persons[a].body == w.persons[a].body_ceiling and w.persons[b].body == w.persons[b].body_ceiling
                 and pool.governing_score(w, w.persons[a], "tell") == pool.governing_score(w, w.persons[b], "tell")), None)
    assert pair is not None, "no two living, unwounded persons are equal on `tell`'s governing score"
    p, q = pair
    r = next(i for i in alive if i not in pair)
    w.persons[p].capability = {key: 4}
    w.persons[q].capability = {key: 0}
    assert pool.score(w, w.persons[p], "tell") != pool.score(w, w.persons[q], "tell"), "the pair's skill scores do not differ"
    odds_p, odds_q = sigma.odds_of(w, _tell(p, r)), sigma.odds_of(w, _tell(q, r))
    assert odds_p is not None and odds_q is not None, "`tell` deals no social roll for the pair: nothing to compare"
    assert odds_p != odds_q, f"skill scores 4 and 0 read the same odds {odds_p}: the skill score does not reach the roll"
    w.persons[q].capability = {key: 4}                      # the control: the cause removed
    assert sigma.odds_of(w, _tell(p, r)) == sigma.odds_of(w, _tell(q, r)), "equal skill scores read different odds"


def _ranked(w: World, pid: str, q) -> list[tuple[str, str | None]]:
    """`(verb, subject)` of `pid`'s candidates for `q`, in the shipped ranker's order, read on his own View
    (the draw is `(seed, tick, person, purpose)`, so the same world ranks the same way twice)."""
    rank = CH.make_ranker(w.fixtures, resolvable_verbs(), draw_factory(w.world_seed, lambda: w.tick))
    p = w.persons[pid]
    return [(c.verb, c.subject) for c in rank(p, assemble(p, q, w.fixtures.get("view_k")))]


def _plant_stance(w: World, pid: str, row: tuple) -> None:
    """One stance row onto `pid`'s own `Person.stance`, through the gate: `World.write` on the `(Person, stance)`
    row at RESOLVE with a token minted for the step, a `Change` naming the one subject (as `_eff_forgive` builds its own)."""
    p = w.persons[pid]

    def perform() -> None:
        p.stance = [*p.stance, row]
    prior, w.step = w.step, Step.RESOLVE
    try:
        w.write("stance", mint_token(w, WriteClass.ACTS), None, record_kind="Person", fieldname="stance",
                driver="Act", actor=pid, change=Change((Subject.entity("persons", pid, fields=("stance",)),), perform))
    finally:
        w.step = prior


def _top_about(order: list, subject: str) -> tuple | None:
    return next((c for c in order if c[1] == subject), None)


def test_r07_a_planted_regard_changes_what_a_person_ranks_first():
    changed, checked = [], 0
    for seed in SEEDS:
        w = build_realm(seed)
        q = DS.decision_question(DS.common_referents(w)[0][1])
        # the first person, by id, who holds a candidate about another person; his subject is the best-ranked such one's
        pid, before = next((i, o) for i, o in ((i, _ranked(w, i, q)) for i in sorted(w.persons))
                           if any(s not in (None, i) for _v, s in o))
        subject = next(s for _v, s in before if s not in (None, pid))
        assert _top_about(before, subject) is not None
        assert _ranked(w, pid, q) == before, f"seed {seed}: the unplanted world ranked {pid} differently on a second read"
        row = (subject, -float(STANCE_VALENCE_SCALE), float(STANCE_VALENCE_SCALE))     # a grudge at the row type's bound
        # the falsifier: a row toward a person he holds no candidate about moves nothing
        held = {s for _v, s in before}
        elsewhere = next(i for i in sorted(w.persons) if i != pid and i not in held)
        off = build_realm(seed)
        _plant_stance(off, pid, (elsewhere, row[1], row[2]))
        assert off.persons[pid].stance[-1][0] == elsewhere, "the off-subject row did not land"
        assert _ranked(off, pid, q) == before, f"seed {seed}: a row toward {elsewhere}, about whom {pid} holds no candidate, moved his ranking"
        planted = build_realm(seed)
        _plant_stance(planted, pid, row)
        assert planted.persons[pid].stance[-1] == row, "the planted row did not land"
        # a grudge also OPENS candidates (`forgive`, `opening_set`'s own-stance declines): the order is read over the ones he held before
        after = [c for c in _ranked(planted, pid, q) if c in before]
        checked += 1
        assert sorted(after) == sorted(before), "planting a regard removed a candidate he held"
        if _top_about(after, subject) != _top_about(before, subject):
            changed.append(seed)
    assert checked >= len(SEEDS), f"{checked} seeds were read, not {len(SEEDS)}"
    assert changed, "no seed's top candidate about the planted subject moved when a grudge toward him was written"
