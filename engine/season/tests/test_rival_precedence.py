"""B08.05 (`18_DETERMINISM_rival_acts_in_one_fold.md`, "Gate"; rulings A-5, A-9, A-30): RIVALS FOR ONE EXCLUSIVE THING ARE ORDERED BY A DRAW.

Two acts by different persons that want one thing only one can have (a vacant seat, a Record held by another, the stores of a
larder beyond its stock) used to be folded in the canonical content-hash order, so who got the grain was a fixed function of the
acts' content. `loop/resolve.py::_canonical_order` now re-orders such a group among the positions the group already holds by a
keyed draw per act, through the one sampler and the one pool rule; `Fixtures rival_precedence: draw | hash` (`hash` = today).

  FALSIFIERS: a rivalry group whose winner is the same at every seed; an act outside a group whose position moved; a rival
  whose better pool does not win more often; `hash` that does not reproduce the base; `draw` that moves a world with no group.
  CONTROLS: `rival_precedence: hash` (today's order, pinned below); a world with no rivalry group at `draw` equal to `hash`.

Hand-built worlds (`tiny_world`), not realms: the group needs two seats and one scarce thing, and a seed is a `world_seed`.
`task_draw_arm` is `off` for the larder (a requisition's own draw would let the first claimant lose and the second take it, which is
the task's, not the order's), and the seat turnover is folded at Success (`seat_at_success`, as `test_in61_succession.py` does).
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..loop.resolve import _canonical_order
from ..seam.wrappers.pool import faculty
from ..state.carriers import Act, Office, Tenure
from ..trace_log import TRACE
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_u7_remit import _fold, _requisition

SEEDS = 200
CHARISMA = "attr.social.charisma"          # `requisition`'s and `succeed`'s one governing attribute (`verb_table.yaml`)
HIGH, MID = "p_high", "p_mid"             # the two rivals; `p_high` is the better pool wherever a test says so
STRONG = 7                                 # [JUSTIFIED: a test-fixture pool, not a game value -- the top of the attribute scale against the untrained 2, so the odds are far from even and a 200-seed count separates them]
THRONE, HEIR, REGENT = "off_king", "off_heir", "off_widow_regent"      # `rosters.yaml: successions`' own ids

# The content hash of the larder world after the fold (`_two_requisitions`), at `rival_precedence: hash`, seeds 0-2, `p_high` at STRONG,
# `PYTHONHASHSEED` 0 and 7 alike: reading @715f5f5, B08.04's head, before B08.05 edited any game code. A TEST-LOCAL PIN: `hash` is today's
# order, so these values are the order's own and move only if something else moves the fold.
HASH_ARM_BASE = {0: "df1baf950bb196af844536e57a4c82d0", 1: "7261c5a7e858343f1f52f62dd365dca5", 2: "c1d2f2779709dc79de7e2c7b81da6ea0"}


def _arm(arm, **fx):
    f = DEFAULT_FIXTURES.sweep("task_draw_arm", "off")
    for k, v in fx.items():
        f = f.sweep(k, v)
    return f if arm is None else f.sweep("rival_precedence", arm)


def _larder(seed, arm=None, stock=4, strong=STRONG):
    """One larder (`Hh`) of `stock` grain; two seats at the duchy, each with a holder -- `p_high` (charisma `strong`) and `p_mid` (untrained)."""
    w = P.tiny_world(_arm(arm))
    w.world_seed = seed
    w.offices["off_duke2"] = Office("off_duke2", "Duke", "D", ["issue"], faction="Valorsmark")
    w.add_tenure(Tenure("t_duke2", MID, "off_duke2", "hold", since=0))
    w.rungs["Hh"].stores = {"grain": stock}
    if strong is not None:
        w.persons[HIGH].attributes = {CHARISMA: strong}
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _two_requisitions(subject_a="Hh", subject_b="Hh", amount=4):
    return [_requisition("rq_a", subject=subject_a, amount=amount),
            _requisition("rq_b", subject=subject_b, amount=amount, actor=MID, via="off_duke2")]


def _heirs(seed, arm=None):
    """A vacant throne and two heirs, each holding a title the throne's `successions` lists: `p_high` (charisma STRONG) and `p_mid`."""
    w = P.tiny_world(_arm(arm))
    w.world_seed = seed
    w.offices[THRONE] = Office(THRONE, "King", "R", ["issue"], faction="Valorsmark", conferral="inheritance")
    w.offices[HEIR] = Office(HEIR, "Heir", "R", ["issue"], faction="Valorsmark", conferral="appointed")
    w.offices[REGENT] = Office(REGENT, "Regent", "R", ["issue"], faction="Valorsmark", conferral="appointed")
    w.add_tenure(Tenure("t_heir", HIGH, HEIR, "hold", since=0))
    w.add_tenure(Tenure("t_regent", MID, REGENT, "hold", since=0))
    w.persons[HIGH].attributes = {CHARISMA: STRONG}
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _claims():
    return [Act(id="claim_a", actor=HIGH, verb="succeed", payload={"subject": THRONE}),
            Act(id="claim_b", actor=MID, verb="succeed", payload={"subject": THRONE})]


def _taker(out, d, kind):
    """The act ids whose Events are `kind`, in fold order."""
    return [d.act_of[e.id].id for e in out if e.kind == kind]


def _signature(w, out):
    """What a fold left: the world's content hash and every Event's id, kind and reads, in order."""
    return w.content_hash(), [(e.id, e.kind, tuple(repr(o) for o in e.observed)) for e in out]


def _precedence_of(out, d):
    """`{act id: net}` -- the `precedence` read each act's Events carry (the reason trail)."""
    return {d.act_of[e.id].id: o.value for e in out for o in e.observed if o.predicate == "precedence"}


# ---------------------------------------------------------------------------------------------------------------------
# GATE 2 -- ONE LARDER, TWO CLAIMANTS
# ---------------------------------------------------------------------------------------------------------------------

def test_two_requisitions_on_one_larder_each_win_sometimes():
    """Two persons, one larder of 4 grain, each `requisition` 4, 200 seeds: each wins in some seeds (the falsifier is one winner at every seed).
    ⚠ The hash order's key holds `world_seed` too, so this claim alone does not tell `draw` from `hash`; `test_higher_pool_wins_more_often` and
    `test_hash_control_reproduces_base` do. The act outside the group keeps its position and the group keeps its positions."""
    wins = {"rq_a": 0, "rq_b": 0}
    checked = 0
    for seed in range(SEEDS):
        w, d = _larder(seed)
        out = _fold(w, d, *_two_requisitions())
        took, refused = _taker(out, d, "requisition.taken"), _taker(out, d, "requisition.refused")
        assert len(took) == 1 and len(refused) == 1 and took != refused, (seed, [e.kind for e in out])
        assert set(_precedence_of(out, d)) == {"rq_a", "rq_b"}, (seed, "the order was not drawn: no `precedence` read on the rivals' Events")
        wins[took[0]] += 1
        checked += 1
    assert checked >= SEEDS
    assert wins["rq_a"] > 0 and wins["rq_b"] > 0, f"one claimant won every seed: {wins}"

    # AN OUTSIDER DOES NOT MOVE: `bystander` asks a different larder; the two rivals trade the two positions they hold and nothing else.
    held = {}
    for arm in ("hash", "draw"):
        positions = []
        for seed in range(SEEDS):
            w, _d = _larder(seed, arm=arm)
            acts = [_two_requisitions()[0],
                    _requisition("bystander", subject="S", amount=1, actor=MID, via="off_duke2"),
                    _two_requisitions()[1]]
            order = [a.id for a in _canonical_order(w, acts)]
            positions.append((order.index("bystander"), sorted(order.index(i) for i in ("rq_a", "rq_b"))))
        held[arm] = positions
    assert len(held["draw"]) >= SEEDS
    assert held["draw"] == held["hash"], "a position the draw had no business moving moved (the bystander's, or the set the rivals hold)"


def test_higher_pool_wins_more_often():
    """Same world, `p_high` at STRONG against `p_mid` untrained: the better pool wins more of 200 seeds, and neither share is 0 or 1. The reason trail
    reads true: each act's Events carry the `precedence` net it drew, the winner's the higher; the group rides the trace."""
    pools = _larder(0)[0]
    assert (faculty(pools, pools.persons[HIGH], "requisition") > faculty(pools, pools.persons[MID], "requisition")), \
        "the fixture does not give the rivals different pools"
    wins = {HIGH: 0, MID: 0}
    ordered = 0
    for seed in range(SEEDS):
        w, d = _larder(seed)
        with TRACE.recording():
            before = len(TRACE.rows)
            out = _fold(w, d, *_two_requisitions())
            rows = [r for r in TRACE.rows[before:] if r.channel == "DECISION" and r.what == "rival precedence"]
        assert rows, f"seed {seed}: a rivalry group was folded and the trace holds no `rival precedence` decision"
        nets = _precedence_of(out, d)
        assert set(nets) == {"rq_a", "rq_b"}, (seed, nets)
        won = _taker(out, d, "requisition.taken")[0]
        assert nets[won] > nets["rq_b" if won == "rq_a" else "rq_a"], (seed, nets, won)
        wins[HIGH if won == "rq_a" else MID] += 1
        ordered += 1
    assert ordered >= SEEDS
    assert 0 < wins[MID] and wins[HIGH] < SEEDS, wins
    assert wins[HIGH] > wins[MID], f"the better pool did not win more often: {wins}"


# ---------------------------------------------------------------------------------------------------------------------
# GATE 3 -- ONE VACANT SEAT, TWO HEIRS
# ---------------------------------------------------------------------------------------------------------------------

@pytest.mark.usefixtures("seat_at_success")        # the turnover's order, not its draw (`_seat_at_success.py`)
def test_two_heirs_each_reign_in_some_seeds():
    """Two heirs whose titles both claim one vacant throne: each reigns in some of 200 seeds. The loser's claim finds the seat held and is refused."""
    reigns = {HIGH: 0, MID: 0}
    checked = 0
    for seed in range(SEEDS):
        w, d = _heirs(seed)
        out = _fold(w, d, *_claims())
        holders = [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == THRONE]
        assert len(holders) == 1, (seed, holders, [e.kind for e in out])
        assert sorted(e.kind for e in out if e.kind.startswith("succession.")) == ["succession.claimed", "succession.refused"], (seed, [e.kind for e in out])
        assert set(_precedence_of(out, d)) == {"claim_a", "claim_b"}, (seed, "the order was not drawn: no `precedence` read on the heirs' Events")
        reigns[holders[0]] += 1
        checked += 1
    assert checked >= SEEDS
    assert reigns[HIGH] > 0 and reigns[MID] > 0, f"one heir reigned in every seed: {reigns}"


# ---------------------------------------------------------------------------------------------------------------------
# GATE 4 -- THE CONTROL, AND A WORLD WITH NO GROUP
# ---------------------------------------------------------------------------------------------------------------------

def test_hash_control_reproduces_base():
    """`rival_precedence: hash` is today's order: the larder world's content hash after the fold equals the base pin at seeds 0-2; and the
    order it gives is blind to the rivals' pools (the same winner at every one of 200 seeds whether `p_high` is STRONG or untrained -- the hash
    key reads the acts, never a skill) while `draw` reads them (the winner moves with the pool at some seed). So the control is not the arm."""
    for seed, pin in HASH_ARM_BASE.items():
        w, d = _larder(seed, arm="hash")
        _fold(w, d, *_two_requisitions())
        assert w.content_hash() == pin, (seed, w.content_hash())
    pool_moved = {"hash": 0, "draw": 0}
    checked = 0
    for seed in range(SEEDS):
        for arm in ("hash", "draw"):
            won = []
            for strong in (STRONG, None):
                w, d = _larder(seed, arm=arm, strong=strong)
                won.append(_taker(_fold(w, d, *_two_requisitions()), d, "requisition.taken")[0])
            pool_moved[arm] += won[0] != won[1]
        checked += 1
    assert checked >= SEEDS
    assert pool_moved["hash"] == 0, f"the hash order moved with a pool ({pool_moved}): the control is not today's order"
    assert pool_moved["draw"] > 0, f"the `draw` arm never read a pool ({pool_moved})"


def test_no_group_world_is_byte_identical():
    """At `draw`, a world with no rivalry group is byte-identical to `hash`: content hash and every Event (id, kind, reads) over 200 seeds, for
    three worlds -- two requisitions on two larders, two on one larder holding enough for both (the summed `amount` does not exceed the stock),
    and two acts by one actor on one larder. None carries a `precedence` read."""
    worlds = {
        "two larders": lambda seed, arm: (_larder(seed, arm=arm, stock=4), _two_requisitions("Hh", "S")),
        "stock for both": lambda seed, arm: (_larder(seed, arm=arm, stock=8), _two_requisitions("Hh", "Hh")),
        "one claimant": lambda seed, arm: (_larder(seed, arm=arm, stock=4),
                                           [_requisition("rq_a", subject="Hh", amount=4), _requisition("rq_c", subject="Hh", amount=4)]),
    }
    for name, make in worlds.items():
        checked = 0
        for seed in range(SEEDS):
            sigs = {}
            for arm in ("hash", "draw"):
                (w, d), acts = make(seed, arm)
                out = _fold(w, d, *acts)
                assert not _precedence_of(out, d), (name, seed, "a world with no rivalry group carries a precedence read")
                sigs[arm] = _signature(w, out)
            assert sigs["hash"] == sigs["draw"], (name, seed)
            checked += 1
        assert checked >= SEEDS, name
