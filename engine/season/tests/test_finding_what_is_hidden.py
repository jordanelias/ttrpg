"""B11.68 (`IS-B2-FI-07`, the event half) -- A DEED NOBODY SAW IS FOUND BY AN INQUIRY ON ITS TRACE, AND A COVER STANDS AGAINST THE FINDER'S ROLL.

The hand world is `tiny_world` at `notice_arm: on`: `p_other` walks to the duchy `D`, where a Site stands and nobody else does, and damages it
(`sabotage`, a covert kind, `rosters.yaml: covert_kinds`); `p_high`, who was never there, hears the Site exists (`harness/scenarios.py::hear`, the
`own_ledger` cell `reconstruct` asks) and `reconstruct`s it. The deed is folded flat (`task_draw_arm: off`, `_flat_fold.py`: the question is the
find, not the saboteur's own draw) and the arm is turned back `on` for the inquiry, which `reconstruct` is graded under (`armed_by: task_draw_arm`).
A draw is keyed `H(world_seed, tick, actor, "roll:reconstruct:<act id>")`, so the world seed is the sample and the tick must be equal across arms.
"""
from __future__ import annotations

from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.harness import probes as P
from engine.season.harness.scenarios import hear, step
from engine.season.loop.driver import SeasonDriver
from engine.season.state.attribution import live_cover
from engine.season.state.carriers import Act, Site
from engine.season.tests._flat_fold import flat_fold

DOER, FINDER, BYSTANDER = "p_other", "p_high", "p_low"
DEED, SITE, COVER = "site.damaged", "site_x", "rec:cv"
ON = DEFAULT_FIXTURES.sweep("notice_arm", "on")
OFF = DEFAULT_FIXTURES.sweep("notice_arm", "off")
SEEDS = range(200)
# [JUSTIFIED: a test-fixture search bound, not a game value -- the act ids tried for a band; asserted reached]
SWEEP = 60


def _deed(fixtures, seed: int = 1, cover=None, bystander: bool = False):
    """`(w, d)`: the Site at `D` damaged by the doer, alone unless `bystander` (then `p_low` walks there first and the room holds two).
    `cover` is `None` (the doer takes none), or the `forgery_quality` his live cover is set to (a `conceal`, then the Record's quality pinned: the band
    of the `conceal` itself is the doer's own draw, not this test's). A tick passes after the setup in every arm, so every arm's inquiry shares its draw key."""
    w = flat_fold(P.tiny_world(fixtures))
    w.world_seed = seed
    w.sites[SITE] = Site(SITE, "D", "ruin", condition=500)
    d = SeasonDriver(w)
    if cover is not None:
        assert [e.kind for e in step(w, d, Act(id="cv", actor=DOER, verb="conceal", payload={"subject": DOER}))] == ["cover.assumed"]
        assert live_cover(w, DOER) == COVER
        w.records[COVER].forgery_quality = cover
    if bystander:
        assert [e.kind for e in step(w, d, Act(id="by_mv", actor=BYSTANDER, verb="move", payload={"to": "D"}))] == ["travel.moved"]
    assert [e.kind for e in step(w, d, Act(id="mv", actor=DOER, verb="move", payload={"to": "D"}))] == ["travel.moved"]
    assert [e.kind for e in step(w, d, Act(id="sab", actor=DOER, verb="sabotage", payload={"site": SITE}))] == [DEED]
    w.tick += 1
    return w, d


def _reconstruct(w, d, act_id: str):
    """The finder hears the Site exists and reconstructs it, the task draw on: the finding Event."""
    hear(w, FINDER, SITE)
    w.fixtures = w.fixtures.sweep("task_draw_arm", "on")
    (e,) = step(w, d, Act(id=act_id, actor=FINDER, verb="reconstruct", payload={"subject": SITE}))
    assert e.kind in ("finding.made", "finding.none"), e.kind
    return e


def _holders(w, predicate: str = DEED) -> set:
    return {pid for pid, p in w.persons.items() if any(c.predicate == predicate for c in p.ledger)}


def test_an_unnoticed_deed_is_found_only_by_inquiry_on_its_trace():
    """A deed done where nobody stood, at `notice_arm: on`: no ledger but the doer's holds it (the control beside it: with a bystander in the room, at the
    arm `off`, the same deed IS held by him, so the count reads deposits). A `reconstruct` that draws Failure leaves the finder holding nothing; one that
    draws a band showing the hand leaves him holding the deed under the Site and the doer, inferred, and no other ledger moved."""
    w, d = _deed(ON)
    assert _holders(w) == {DOER}, _holders(w)
    w_by, _ = _deed(OFF, bystander=True)
    assert _holders(w_by) == {DOER, BYSTANDER}, _holders(w_by)                                                  # control: the instrument sees a bystander's deposit
    seen = set()
    for n in range(SWEEP):
        w, d = _deed(ON)
        e = _reconstruct(w, d, f"rc_{n}")
        held = {c.subject for c in w.persons[FINDER].ledger if c.predicate == DEED}
        if e.kind == "finding.none":
            assert held == set() and _holders(w) == {DOER}, n
            seen.add("none")
        elif e.degree in ("Success", "Overwhelming"):
            assert held == {DOER, SITE} and _holders(w) == {DOER, FINDER}, (n, held)
            assert {c.source for c in w.persons[FINDER].ledger if c.predicate == DEED} == {"inferred"}
            seen.add("found")
    assert seen == {"none", "found"}, seen


def _share(cover, quality_fixtures=ON) -> list:
    """The finder's find (a `finding.made`) at each world seed, the doer holding a cover at `cover` quality or none."""
    out = []
    for s in SEEDS:
        w, d = _deed(quality_fixtures, seed=s, cover=cover)
        out.append(_reconstruct(w, d, "rc").kind == "finding.made")
    return out


def test_a_concealed_deed_is_found_less_often():
    """The doer's cover (a Success `conceal`: `forgery_quality` 1) stands against the finder's roll: over 200 world seeds the same inquiry on the same trail finds
    the deed less often than where the doer holds none, and at no seed MORE often. The control: a cover at Partial's quality (0) gives the finder exactly
    what no cover gives, at every seed."""
    none, good, partial = _share(None), _share(1), _share(0)
    checked = len(none)
    assert checked >= 200 and len(good) == len(partial) == checked
    assert partial == none, "a cover at quality 0 moved a draw"
    assert all(n or not g for g, n in zip(good, none)), "a seed found the deed through the cover and not without it"
    assert 0 < sum(good) < sum(none) < checked, (sum(good), sum(none), checked)
