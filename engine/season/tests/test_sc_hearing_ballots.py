"""B24.11 -- a bench of several votes seat by seat, in one place (`U5c_SC_proceedings_residue.md` §6; HEAR_B gate).

A `determine` on a docketed row that CLOSES `declared` is the bench's own sitting: each seat who decides draws once at the close and the matter carries
by the quorum-th best seat's margin (`sigma.act_band`). The seats' live commits on the motion are where each seat's TRACK starts (`sigma._ballot_start`, one
`lean_level` a commit), so the count is the odds and gates nothing (`determine`'s `vote` conjunct is deleted).

The world is `test_cr34_declared_disposal.py`'s (`tiny_world` with its Duke's seat ended and the Church's seats at the duchy `D`), with two more seat holders: FIVE
seats, the accused `p_mid`, the row `excommunication_deliberation` at its own quorum (2).
"""
from __future__ import annotations

from dataclasses import replace

from engine.dice_engine.dice_engine import DEGREE_ORDINAL, Degree, degree_from_net

from ..data.arrangements import ARRANGEMENTS
from ..queries import world_q
from ..queries.inputs import Choice, Item
from ..seam.wrappers import sigma
from .test_cr34_declared_disposal import CHURCH, JUDGE_SEAT, ROW, _church_world, _commit
from .test_sc_proceeding_module import P, _bench, _inp, _key, _p, _rite, _silent, _sit
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
    w, d = _sitting(sitting_exchanges=0)                                          # the control, set here: the shipped realm spends the attendees' effort (B24.37)
    assert w.fixtures.get("sitting_exchanges") == 0 and "vote" not in world_q.VERB_TABLE["determine"].requires_typed.conjuncts()
    act = _determine("dt", via=JUDGE_SEAT, actor="p_high")
    row, form, _move, _item = world_q.proceeding_row(w, act)
    out = sigma.resolve(w, ["p_high", PARTY], ["dt"], "a verdict", verb="determine", subject=PARTY, rng=_key("ballot", 0),
                        proceeds=(row, form, None, None), topic=PARTY)
    assert (row["id"], row["close"], out["status"]) == (ROW, "declared", "RESOLVED")
    assert out["proceeding"].beats == () and len(out["proceeding"].verdicts) == 5 and out["arrangement"] == ROW
    assert sorted(dict(out["starts"])) == sorted((*FOR, *AGAINST, PARTY)) and dict(out["starts"])["p_x"] < 0 < dict(out["starts"])["p_low"]
    w2, d2 = _sitting(sitting_exchanges=0)
    assert _kinds(_fold(w2, d2, _determine("dt2", via=JUDGE_SEAT, actor="p_high")))[0] in ("matter.determined", "matter.undetermined")


# ---- B24.32: the kernel's `VoteAtClose` and the armature are carried -----------------------------------------------------------------

def _ballots(out) -> dict:
    """each seat's ballot as the host grades it: carried is Success or better on his own margin."""
    return {seat: DEGREE_ORDINAL[degree_from_net(m.net, m.ob)] >= CARRIED for seat, m in out.verdicts}


def test_a_seat_can_vote_against_the_board():
    """KERN_B check 7 (`VoteAtClose`: a ballot per seat that can cross the room): a three-seat `declared` bench (quorum 2) with one exhibit standing FOR the party, 200 seeds,
    the seats at 0, 0 and -3 (the third has his own commits against). The board is leverage on EVERY seat's close, so each carries more often with it than without; and the
    third seat votes the other way from the board at some seeds where both others vote with it, and carries less often than either. FALSIFIER: a board that decided the
    ballot (the third seat never crossing the room), or one that reached no seat (no seat carrying more often with it)."""
    base = _bench("declared", 3, quorum=2, starts=[0.0, 0.0, -3.0], turns=1, silence="free")
    exhibit = Item("i1", "record", 3.0, side="for")
    boarded, bare = replace(base, state=_sit(base, board=((exhibit, "stands"),))), replace(base, state=_sit(base))
    with_board, without, crossed, checked = dict.fromkeys(("j0", "j1", "j2"), 0), dict.fromkeys(("j0", "j1", "j2"), 0), 0, 0
    for i in range(SEEDS):
        out = _silent(boarded, _key("board", i))
        assert [(it.id, it.side) for it in out.standing] == [("i1", "for")] and len(out.verdicts) == 3     # the board favours `for`; each seat has his own draw
        said = _ballots(out)
        crossed += said["j0"] and said["j1"] and not said["j2"]
        for seat in with_board:
            with_board[seat] += said[seat]
            without[seat] += _ballots(_silent(bare, _key("board", i)))[seat]
        checked += 1
    assert checked >= 200
    assert all(with_board[s] > without[s] for s in with_board), (with_board, without)        # the board reaches every seat's close
    assert crossed > 0 and with_board["j2"] < min(with_board["j0"], with_board["j1"]), (crossed, with_board)


def test_a_trait_row_moves_one_seats_ballot_odds_only():
    """KERN_B check 8 (`armature`: what moves this judge): what a seat holds (`Present.holds`, B24p.02) is his own row of what moves him, read by the `fit` source of a speech
    framed on it. Two `declared` benches of three alike seats and one speech framed on `t1`, 200 seeds, differing ONLY in what the second seat holds (`t1`, bearing for the
    speaker): his own track rises and so do his close's odds (`p_carried` at his track), and every other seat's track, odds and ballot margin are the same to the digit.
    FALSIFIER: a row that moved another seat (a shared reading), or none (a row nothing reads)."""
    held = (("want", "t1", 0.9, 1.0),)

    def bench(row):
        seats = [_p(f"j{i}", decides=True, precedence=3 - i, **({"holds": held} if row and i == 1 else {})) for i in range(3)]
        return replace(_inp([_p("a", "for"), _p("b", "against")] + seats,
                            _rite(close="declared", quorum=2, turns=1, silence="free", moves=(("for", ("argue", "rest")), ("against", ("rest",))))),
                       frames=(("want", "t1"),))

    def decide(view, me):
        o = next(o for o in view.options if (o.ground == "consequence" if me.id == "a" else o.move == "rest"))
        return Choice(o.move, o.ground, o.item, o.relation)
    plain, planted, checked = bench(False), bench(True), 0
    for i in range(SEEDS):
        a, b = (P.proceed(inp, _key("trait", i), decide=decide) for inp in (plain, planted))
        ta, tb = dict(a.state.tracks), dict(b.state.tracks)
        assert tb["j1"] > ta["j1"] and P.p_carried(planted, tb["j1"]) > P.p_carried(plain, ta["j1"]), i       # his own track and his own odds
        for other in ("a", "b", "j0", "j2"):
            assert tb[other] == ta[other], (i, other)                                                         # nobody else's
        assert dict(a.verdicts)["j0"] == dict(b.verdicts)["j0"] and dict(a.verdicts)["j2"] == dict(b.verdicts)["j2"] and dict(a.verdicts)["j1"] != dict(b.verdicts)["j1"]
        checked += 1
    assert checked >= 200
