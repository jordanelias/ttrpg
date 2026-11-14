"""R-01, R-02 and their controls, read on the PLAYED REALM at three seeds.

`test_season_shape.py` asserts the claim-to-act chain on worlds built from corpus cases; these tests
read it on the world the game ships: `populated.build_realm(seed)` played one season on the shipped
policy (`probes.chooser` over `resolvable_verbs()`).

R-01.b, read here: an act formed from a `claim_landed` question, where the Event the question walks
back to (`world_q.occasioned_by`) was emitted by an act of a DIFFERENT person. The control removes the
cause: with `SeasonDriver.witness` returning 0 no claim is deposited, no `claim_landed` question forms,
and the count must read 0. A count that is positive with the witness cut would mean the counter reads
something other than the chain.

R-02.a, read here: withholding what acts observe changes the acts that follow. One season at the shipped
fixtures and one with `observation_deposit_mode` swept to `none` (no act deposits what it read) give two
`(actor, verb, subject)` sequences that part, after a common prefix (the worlds start equal). The control
plays one seed twice at the shipped fixtures and must read one sequence; a parting there would mean the
sequence moves with nothing varied, and the parting above would prove nothing. ⚠ This reads that the
sequence parts when deposits are cut; it does not read that the fork-and-follow test's divergence is
caused by deposits (`test_season_shape.py` shows divergence in both arms).
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES, Fixtures
from ..harness import populated
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries.world_q import occasioned_by
from ..state.carriers import subject_of
from ..state.world import World

SEEDS = (0, 1, 2)


def _play(seed: int, fx: Fixtures | None = None) -> tuple[World, SeasonDriver]:
    """The shipped realm at `seed` (built on `fx`, None: the shipped fixtures), played one season."""
    w = populated.build_realm(seed, fixtures=fx)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())
    d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


def _occasioned_by_another(w: World, d: SeasonDriver) -> tuple[int, int]:
    """(resolved acts whose scene's occasion is a `claim_landed` question and walks back to an Event
    emitted by an act of a different person, resolved acts whose occasion is `claim_landed`)."""
    hit = landed = 0
    for a in d.resolved:
        occ = getattr(d.scenes.get(getattr(a, "scene", None) or ""), "occasion", None)
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
    hit, _landed = _occasioned_by_another(w, d)
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
