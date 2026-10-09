"""v9 IN-22 · CARRY-SHORTFALL, THE REACH HALF (#457 `:162`; `H-160` limit 2): a shortfall reaches the
governors whose seat's purview contains the drained larder.

EXIT (#457, verbatim): *a governor's `questions_for` holds the claim and a candidate forms in
`harness/scarce.py`'s world.* FALSIFIER: *the claim held by a governor outside the shortfall's reach and
purview, or by none -> fail.*

The world is `scarce.governed`: `scarce.build` plus two reeves, each seated on a territory and living
there, so neither stands at `set_hungry` nor holds it. One seat's rung contains the hungry town, the
other's is a sibling territory. Everything else is the shipped loop: MATTER's draw records the
shortfall on the drained larder's write, WITNESS deposits it, `questions_for` admits it through
`reach`, `opening_set` forms the `transfer`.

Each assertion below is paired with the arm that would show it wrong: the far reeve (outside purview),
`observation_deposit_mode: none`, `fan_out_mode: presence_only` (the seat channel off), and an ACT's
reads (which stay the actor's). Every loop that asserts per item asserts that it asserted.

WHAT THIS DOES NOT CLAIM: the candidate's `from` is the reeve's own containing rung (`H-160` limit 1,
`containing_rung_of`), a territory with no larder, so the fold would refuse it. Paying out of a seat's
own rung needs `Act.via` on a computed `transfer` (`H-158`), which is not this half's.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.requires import SHORTFALL_PREDICATE
from ..data.rosters import CHANNEL_CLAIM_SOURCE
from ..decision import make_chooser
from ..decision.options import opening_set
from ..harness import probes as P
from ..harness import scarce as S
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..loop.witness import SEAT_CHANNEL
from ..queries import world_q
from ..state.carriers import View
from ..state.ids import H, draw_factory

GOVERNORS = (S.REEVE, S.FAR_REEVE)


def _season(w, choose=P.NOCHOOSE, question=None, d=None):
    d = d or SeasonDriver(w)
    d.season(choose, question=question, subsistence=P.SUBSIST,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    return d


def _recorded(w) -> dict:
    """What MATTER recorded at the hungry larder: `{predicate: units}`, off the log."""
    return {o.predicate: o.value for e in w.log for o in e.observed
            if o.subject == S.HUNGRY and str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE}


def _held(w, pid) -> dict:
    return {c.predicate: (c.value, c.source) for c in w.persons[pid].ledger
            if c.subject == S.HUNGRY and str(c.predicate).partition(":")[0] == SHORTFALL_PREDICATE}


def _one_season(fixtures=DEFAULT_FIXTURES):
    # `steward_holds=False`: nobody HOLDS the hungry town, so the document channel admits nobody to
    # its larder write and the only route left to a person not standing there is the one under test.
    w = S.governed(fixtures=fixtures, steward_holds=False)
    _season(w)
    return w


def test_in22_the_world_isolates_purview_as_the_only_difference():
    """THE PRECONDITION, ASSERTED SO THE FALSIFIER CANNOT PASS FOR ANOTHER REASON: neither reeve
    stands at the hungry town or holds it, both hold a live seat with a rung, and exactly one seat's
    purview contains the town."""
    w = S.governed(steward_holds=False)
    assert S.HUNGRY not in {world_q.place_of(w, g) for g in GOVERNORS}
    assert not [t for t in w.tenures if t.live and t.object == S.HUNGRY and t.kind == "hold"]
    for g, seat in ((S.REEVE, S.REEVE_SEAT), (S.FAR_REEVE, S.FAR_SEAT)):
        assert w.offices[seat].rung is not None
        assert any(t.kind == "hold" and t.live and t.object == seat for t in w.persons[g].tenures)
    assert world_q.governors_of(w, S.HUNGRY) == [S.REEVE]
    assert S.HUNGRY in world_q.reach(w, w.persons[S.REEVE])
    assert S.HUNGRY not in world_q.reach(w, w.persons[S.FAR_REEVE])


def test_in22_the_governor_inside_purview_holds_the_claim_and_the_one_outside_does_not():
    """THE FALSIFIER, BOTH WAYS. The reeve whose seat contains the town holds every shortfall MATTER
    recorded there, at the recorded units, with the seat channel's source; the far reeve holds none.
    Checked per recorded kind, and the count is asserted so an empty record cannot pass."""
    w = _one_season()
    recorded = _recorded(w)
    assert recorded, "MATTER recorded no shortfall at the hungry larder; nothing below is observed"
    inside, outside = _held(w, S.REEVE), _held(w, S.FAR_REEVE)
    checked = 0
    for pred, units in sorted(recorded.items()):
        assert inside.get(pred) == (units, CHANNEL_CLAIM_SOURCE[SEAT_CHANNEL]), (pred, inside)
        assert pred not in outside, (pred, outside)
        checked += 1
    assert checked >= 1
    assert outside == {}, "a governor outside the shortfall's purview holds it"
    assert inside, "no governor holds the shortfall"


def test_in22_the_governor_learns_the_reads_and_not_the_write():
    """A REPORT, NOT A WITNESSING: the reeve holds no event-kind or `seen` claim about the larder's
    write -- only what MATTER recorded. The hungry cohort, standing there, holds both (CONTROL that
    the write was witnessed at all)."""
    w = _one_season()
    reeve_other = [c for c in w.persons[S.REEVE].ledger
                   if c.subject == S.HUNGRY and c.predicate not in _held(w, S.REEVE)]
    assert reeve_other == [], [(c.predicate, c.source) for c in reeve_other]
    people = {c.predicate for c in w.persons[S.POPULACE].ledger if c.subject == S.HUNGRY}
    assert "stores.changed" in people and set(_recorded(w)) <= people, people


def test_in22_the_governors_questions_for_holds_the_claim_and_a_transfer_forms_from_it():
    """THE EXIT: the reeve's `questions_for` holds a `claim_landed` question about a shortfall claim,
    and `opening_set` on it forms a `transfer` to the hungry town carrying the claim's own kind and
    amount. The far reeve has no such question."""
    w = _one_season()
    reeve = w.persons[S.REEVE]
    q = S.shortfall_question(w, S.REEVE)
    assert q is not None and q.source == "claim_landed", [x.about for x in world_q.questions_for(w, reeve)]
    claim = next(c for c in reeve.ledger if c.id == q.about)
    (cand,) = [c for c in opening_set(reeve, View(reeve.id, [], 99, q), q, w.fixtures)
               if c.verb == "transfer"]
    ops = cand.operands
    assert ops["to"] == S.HUNGRY
    assert (f"{SHORTFALL_PREDICATE}:{ops['kind']}", ops["amount"]) == (claim.predicate, claim.value)
    assert S.shortfall_question(w, S.FAR_REEVE) is None


def test_in22_control_the_none_arm_deposits_nothing_to_a_governor():
    w = _one_season(DEFAULT_FIXTURES.sweep("observation_deposit_mode", "none"))
    assert _recorded(w), "the record was still made; only its deposit is the arm's"
    assert _held(w, S.REEVE) == {} and _held(w, S.FAR_REEVE) == {}


def test_in22_control_the_route_rides_the_seat_channel_and_is_off_under_presence_only():
    w = _one_season(DEFAULT_FIXTURES.sweep("fan_out_mode", "presence_only"))
    assert _recorded(w)
    assert _held(w, S.REEVE) == {}
    assert _held(w, S.POPULACE), "presence still admits the people standing at the larder"


def test_in22_an_acts_reads_do_not_reach_a_governor():
    """ACTORLESS ONLY. The steward's executed `transfer` out of the granary carries the fold's reads of
    the granary's stores, and the granary lies inside the reeve's purview -- yet those reads stay the
    steward's (`H-122`'s `actor` arm). Asserted that the transfer EXECUTED, or the absence is vacuous."""
    w = S.governed()
    d = _season(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    real = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                        draw=draw_factory(w.world_seed, lambda: w.tick))
    only_steward = lambda p, v, s, b: real(p, v, s, b) if p.id == S.STEWARD else []
    n = len(d.resolved)
    _season(w, only_steward, S.shortfall_question(w, S.STEWARD), d)
    made = {e.causes[0] for e in w.log if e.kind == "transfer.made"}
    assert [a for a in d.resolved[n:] if a.verb == "transfer" and a.id in made], "no transfer executed"
    assert S.GRANARY in [r for r in world_q.reach(w, w.persons[S.REEVE])]
    steward = [c for c in w.persons[S.STEWARD].ledger
               if c.subject == S.GRANARY and str(c.predicate).startswith("stores:")]
    reeve = [c for c in w.persons[S.REEVE].ledger
             if c.subject == S.GRANARY and str(c.predicate).startswith("stores:")]
    assert steward and not reeve, (len(steward), [(c.predicate, c.source) for c in reeve])
