"""B24.11 -- a bench of several votes seat by seat, in one place (`U5c_SC_proceedings_residue.md` §6; HEAR_B gate).

A `determine` on a docketed row that CLOSES `declared` is the bench's own sitting: each seat who decides draws once at the close and the matter carries
by the quorum-th best seat's margin (`sigma.act_band`). The seats' live commits on the motion are where each seat's TRACK starts (`sigma._ballot_start`, one
`lean_level` a commit), so the count is the odds and gates nothing (`determine`'s `vote` conjunct is deleted).

The world is `test_cr34_declared_disposal.py`'s (`tiny_world` with its Duke's seat ended and the Church's seats at the duchy `D`), with two more seat holders: FIVE
seats, the accused `p_mid`, the row `excommunication_deliberation` at its own quorum (2).
"""
from __future__ import annotations

from engine.dice_engine.dice_engine import DEGREE_ORDINAL, Degree, degree_from_net

from ..data.arrangements import ARRANGEMENTS
from ..queries import world_q
from ..seam.wrappers import sigma
from .test_cr34_declared_disposal import CHURCH, JUDGE_SEAT, ROW, _church_world, _commit
from .test_sc_proceeding_module import _key
from .test_u7_remit import DUKE, PARTY, _determine, _fold, _kinds

SEEDS = 200
CARRIED = DEGREE_ORDINAL[Degree.SUCCESS]
FOR, AGAINST = ("p_high", "p_low", "p_other"), ("p_x", "p_y")


def _sitting(lean_level="minor", modifier=None, **fx):
    """The planted sitting: five Church seats at `D` (the three of the hand-built world, `p_x` and `p_y`), the accused docketed under the declared row; three seats
    commit FOR the ban and two AGAINST it (a commit to the same Proposition's negation, `value` false). `modifier` is given to `p_x`'s seat row."""
    from ..harness import probes as P
    from ..state.carriers import Office, Tenure
    w, d = _church_world(**{"pool_floor": 5, "lean_level": lean_level, **fx})
    for n, who in enumerate(AGAINST):
        P.place_person(w, who, who, "Hh")
        off = Office(f"off_cs_{who}", "Dicastery", "D", ["issue", "determine"], faction=CHURCH, modifier=modifier if who == "p_x" else None)
        off.scope_rung = "D"
        w.offices[off.id] = off
        w.add_tenure(Tenure(f"t_hold_{who}", who, off.id, "hold", since=0))
    for who in FOR:
        _commit(w, who, "prop_ban_mid")
    w.propositions["prop_spare_mid"] = type(w.propositions["prop_ban_mid"])("prop_spare_mid", "OUGHT", PARTY, "ban", False, 0)
    for who in AGAINST:
        _commit(w, who, "prop_spare_mid")
    return w, d


def _carried(w, seed):
    """One closing of the planted sitting at `seed`: did the matter carry (Success or better, the ladder's reading of the quorum-th best seat's margin)?"""
    act = _determine("dt", via=JUDGE_SEAT, actor="p_high")
    row, form, _move, _item = world_q.proceeding_row(w, act)
    out = sigma.resolve(w, ["p_high", PARTY], ["dt"], "a verdict", verb="determine", subject=PARTY, rng=_key("ballot", seed),
                        proceeds=(row, form, None, None), topic=PARTY)
    assert out["status"] == "RESOLVED" and row["close"] == "declared" and len(out["read"]) == 1, out.get("status")
    return DEGREE_ORDINAL[degree_from_net(out["net"], out["ob"])] >= CARRIED


def _share(w):
    return sum(_carried(w, i) for i in range(SEEDS)) / SEEDS


def test_a_declared_sitting_carries_at_some_seeds_only():
    """PRES §6 gate: a planted `declared` sitting of five seats with commits three for and two against, 200 seeds: the matter carries at some seeds and fails at
    others (the draw is live, the sitting is not one outcome); with one seat's row given `modifier: minor` the share that carries moves; and the commits are the
    ODDS, not a gate: at `lean_level` None (the control) the same sitting carries less than with them, and the commits turned over carry less than either.
    FALSIFIER: a sitting whose outcome is the same at every seed, or whose share does not move with the commits."""
    w, _ = _sitting()
    assert sorted(world_q.judging_set(w, "D", PARTY)) == sorted((*FOR, *AGAINST))
    assert world_q.declared_votes_by_member(w, PARTY, ARRANGEMENTS[ROW]) == {"p_high": 1, "p_low": 1, "p_other": 1, "p_x": -1, "p_y": -1}
    carried = [_carried(w, i) for i in range(SEEDS)]
    assert len(carried) >= 200 and 0 < sum(carried) < SEEDS, sum(carried)       # carries at some seeds and fails at others
    share = sum(carried) / SEEDS
    checked = len(carried)

    with_modifier, _ = _sitting(modifier="minor")
    moved = _share(with_modifier)
    assert moved != share, (moved, share)                                         # one seat's `modifier:` moves the share that carries
    checked += SEEDS

    control, _ = _sitting(lean_level=None)
    ctrl = _share(control)
    flipped, _ = _sitting()
    for t in flipped.tenures:                                                     # the same bench, the commits turned over: the three against, the two for
        if t.kind == "commit" and t.subject in FOR:
            t.object = "prop_spare_mid"
        elif t.kind == "commit" and t.subject in AGAINST:
            t.object = "prop_ban_mid"
    turned = _share(flipped)
    assert turned < ctrl < share, (turned, ctrl, share)                           # the commits are the odds: for-heavy > none > against-heavy
    checked += 2 * SEEDS
    assert checked >= 200


def test_a_declared_determine_resolves_through_the_proceeding_at_no_exchanges():
    """Item 1: a `determine` on a row whose close is `declared` resolves through `social_contest.proceeding` also at `sitting_exchanges` 0 -- the sitting spoke
    nothing (no beat) and drew one close for each of the five seats, and the fold admits it with no `vote` conjunct (two commits for it carry the matter's odds, not its form)."""
    w, d = _sitting()
    assert w.fixtures.get("sitting_exchanges") == 0 and "vote" not in world_q.VERB_TABLE["determine"].requires_typed.conjuncts()
    act = _determine("dt", via=JUDGE_SEAT, actor="p_high")
    row, form, _move, _item = world_q.proceeding_row(w, act)
    out = sigma.resolve(w, ["p_high", PARTY], ["dt"], "a verdict", verb="determine", subject=PARTY, rng=_key("ballot", 0),
                        proceeds=(row, form, None, None), topic=PARTY)
    assert (row["id"], row["close"], out["status"]) == (ROW, "declared", "RESOLVED")
    assert out["proceeding"].beats == () and len(out["proceeding"].verdicts) == 5 and out["arrangement"] == ROW
    assert sorted(dict(out["starts"])) == sorted((*FOR, *AGAINST, PARTY)) and dict(out["starts"])["p_x"] < 0 < dict(out["starts"])["p_low"]
    w2, d2 = _sitting()
    assert _kinds(_fold(w2, d2, _determine("dt2", via=JUDGE_SEAT, actor="p_high")))[0] in ("matter.determined", "matter.undetermined")
