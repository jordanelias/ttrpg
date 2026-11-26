"""B24.30 -- a negotiation is the same sitting under a consent row (NEG edits 1-4, as V2 corrects them; `IS-B2-SC-03` step 4).

A hand-built two-person sitting on the SEEDED `negotiation` row (`close: consent`, nobody seated), called through `proceed`: an offer is a raised point, an accept the
other side's `concede` under the rite's `concede: accepts`, and nothing is drawn to close it. Lane: `sc_season` (the social contest's season-side tests, by file name).
"""
from __future__ import annotations

import hashlib
from types import SimpleNamespace

from engine.dice_engine import draw

from ..data import arrangements as A
from ..data.rosters import PROCEEDING_MOVES
from ..loop.effects_information import _docket_item
from ..queries import world_q
from ..queries.inputs import PlayHost
from ..seam.ladder import degree_of
from ..seam.wrappers import sigma as S
from ..state.attribution import actor_of
from ..state.carriers import Act, Claim
from . import test_sc_proceeding_module as M
from . import test_u7_remit as U
from .test_sc_proceeding_host import _build, _world

SEEDS = range(40)


def _sitting(seed, *, claim=None, host=None):
    """`(Input, Outcome)` of the negotiation between `p_low` (the bearer, `for`) and `p_mid`, both decided by the NPC decider, or by `host`'s where it plays one of them.
    `claim` is planted in `p_mid`'s own ledger: `(subject, truth)`, a held claim at full sureness."""
    w = _world()
    if claim is not None:
        w.persons["p_mid"].ledger = [Claim("c_plant", "p_mid", claim[0], "breached:p_low", claim[1], 0, "firsthand", w.fixtures.get("confidence_default"), "own")]
    inp, _card = _build(w, ("p_low",), row=A.ARRANGEMENTS["negotiation"], subject="p_mid", verb="argue", effort=2)
    deciders = S._played_by(w, host, inp).get("deciders") if host is not None else None
    if deciders is None:
        npc = S._npc_decider(w, inp)
        deciders = {p.id: npc for p in inp.room}
    return inp, M.P.proceed(inp, M._key("neg", seed), deciders=deciders)


def _digest(out) -> str:
    return hashlib.sha1(repr(out).encode()).hexdigest()


def test_two_npc_negotiation_auto_twice_same_hash():
    """GATE 1 (NEG gate 1; the `oblige` arm is `test_each_oblige_is_opened_by_its_own_partys_act`, below): the seeded `negotiation` row builds a consent sitting nobody adjudicates (two people, no seat), and its
    sitting is the same value twice over the same seeds, whatever the seed's ending. It ends in an accept, a withdrawal, an all-rest or the turns running out, over the seeds.
    FALSIFIER: two digests of one seed, or a row that seats an adjudicator, or a run that never ends in an accept."""
    ends, checked = set(), 0
    for seed in SEEDS:
        (inp, a), (_, b) = _sitting(seed), _sitting(seed)
        assert (inp.rite.close, [p.id for p in inp.room if p.decides]) == ("consent", []), seed
        assert _digest(a) == _digest(b), seed
        ends.add((a.ended, a.ended_by))
        checked += 1
    assert checked == len(SEEDS)
    assert ("yielded", "p_mid") in ends and ("yielded", "p_low") in ends, ends         # the accepter's accept and the bearer's withdrawal both occur


def test_a_held_breach_claim_changes_acceptance():
    """GATE 2: a claim the accepter holds of the matter (a told breach, in his OWN ledger and so in his `believes` and his hand) changes what he does at the table: over the same 40
    keyed sittings the NPC decider's pick ends the sitting differently in some of them, and he accepts a different number of times. CONTROL: the same claim held of another
    matter changes nothing, to the sitting (the claim must bear on THIS matter). FALSIFIER: an identical outcome at every seed, the claim being read nowhere."""
    held, unmoved, differ, accepts, base_accepts = 0, 0, 0, 0, 0
    for seed in SEEDS:
        _, plain = _sitting(seed)
        planted_in, planted = _sitting(seed, claim=("m1", True))
        _, elsewhere = _sitting(seed, claim=("m_other", True))
        assert planted_in.room[1].believes == 1.0 and _digest(elsewhere) == _digest(plain), seed        # the claim reaches his belief; one about another matter does not
        differ += _digest(planted) != _digest(plain)
        accepts += (planted.ended, planted.ended_by) == ("yielded", "p_mid")
        base_accepts += (plain.ended, plain.ended_by) == ("yielded", "p_mid")
        held += 1
    assert held == len(SEEDS) and differ > 0 and accepts != base_accepts, (differ, accepts, base_accepts)


def test_scripted_player_reproduces_auto_hash():
    """GATE 3: a host that plays the bearer and returns the NPC decider's own pick each turn (`sigma._played_by`, the host's decider closed over) leaves the sitting the automated
    run leaves, over the seeds. FALSIFIER: two digests, there being two code paths. CONTROL: a host that plays him and always rests leaves another sitting."""
    from ..queries.inputs import Choice

    checked, moved = 0, 0
    for seed in SEEDS:
        w = _world()
        inp, _card = _build(w, ("p_low",), row=A.ARRANGEMENTS["negotiation"], subject="p_mid", verb="argue", effort=2)
        npc = S._npc_decider(w, inp)          # the decider the room gives him: the host's pick is his, asked for the mover
        auto = M.P.proceed(inp, M._key("neg", seed), deciders={p.id: npc for p in inp.room})
        mirror = PlayHost(frozenset({"p_low"}), None, deciders={S.PROCEEDING_ROLE: lambda view: npc(view, SimpleNamespace(id=view.mover))})
        played = M.P.proceed(inp, M._key("neg", seed), deciders={**{p.id: npc for p in inp.room}, **S._played_by(w, mirror, inp)["deciders"]})
        silent = PlayHost(frozenset({"p_low"}), None, deciders={S.PROCEEDING_ROLE: lambda view: Choice("rest")})
        rested = M.P.proceed(inp, M._key("neg", seed), deciders={**{p.id: npc for p in inp.room}, **S._played_by(w, silent, inp)["deciders"]})
        assert _digest(played) == _digest(auto), seed
        moved += _digest(rested) != _digest(auto)
        checked += 1
    assert checked == len(SEEDS) and moved > 0


def test_an_accept_is_a_concession_and_nothing_is_drawn():
    """An accept is the other side's `concede` (no move `offer` or `accept` is rostered; V2 p2 §B `concede: accepts`): it ends the sitting `yielded` with `ended_by` naming the
    accepter, the act's band is Success for the bearer (the bearer's own withdrawal Failure, the sitting that ends in neither an impasse), and under `close: consent` the sitting
    takes ONLY its exchanges' own draws: no closing normal (a counting `Draw`), no verdict. FALSIFIER: a verdict, a normal beyond the exchanges', or an accept that is not Success."""
    assert "offer" not in PROCEEDING_MOVES and "accept" not in PROCEEDING_MOVES and PROCEEDING_MOVES["concede"]["effect"] == "yield"
    bands, checked = {}, 0
    for seed in SEEDS:
        w = _world()
        inp, _card = _build(w, ("p_low",), row=A.ARRANGEMENTS["negotiation"], subject="p_mid", verb="argue", effort=2)
        npc, rng = S._npc_decider(w, inp), M._Counting(draw.H2("neg", seed))
        out = M.P.proceed(inp, rng, deciders={p.id: npc for p in inp.room})
        assert out.verdicts == () and rng.normals == len(out.beats) * M.P.DRAWS_PER_EXCHANGE(len(inp.grounds)), seed       # no closing normal
        band = S.act_band(out, inp.rite)
        if out.ended == "yielded":
            concede = out.beats[-1]
            assert (concede.move, concede.mover) == ("concede", out.ended_by) and band["status"] == "RESOLVED"
            bands[out.ended_by] = degree_of(band)
        else:
            assert band["status"] == "IMPASSE"
        checked += 1
    assert checked == len(SEEDS) and bands == {"p_mid": "Success", "p_low": "Failure"}, bands


def _opener(w, edge):
    """WHO ACTED to open `edge`: the actor of the logged Event whose receipt names it (`state/attribution.py::actor_of`, the cause's act)."""
    return next(actor_of(w, e) for e in w.log if any(c.subject == edge.id for c in e.changes))


def test_each_oblige_is_opened_by_its_own_partys_act():
    """GATE 1's `oblige` arm (NEG edit 5, B24.31): an `oblige` an agreement opens is opened by the act of the party it binds. A determination does not agree: it is a bench's, and `determine`
    opens no edge for a `consent` row (the judge's act would be the opener, C-07). The real fold on `tiny_world`: (1) CONTROL, a bench row (`arbitration`) determined by the Duke opens the party's
    edge under the DUKE's act, so the reading below can tell a bench's opening from a party's; (2) `open_case` refuses to dock the `negotiation` row, and a determination of a hand-planted
    docket item under it is refused and opens nothing; (3) each party's own `oblige` act opens his edge, and the act that opened every edge is his. FALSIFIER: an edge whose opener is
    not the party it binds, or a `consent` row a determination opens an edge for."""
    w, d = U._world(**U.JUDGE)
    assert U._kinds(U._fold(w, d, U._open("oc", arrangement="arbitration"))) == ["case.opened"]
    assert U._kinds(U._fold(w, d, U._determine("dt"))) == ["matter.determined"]
    sentence, = U._obliges(w)
    assert (_opener(w, sentence), sentence.subject) == (U.DUKE, U.PARTY)             # control: the judge's act opened a party's edge

    w, d = U._world(**U.JUDGE)
    assert A.ARRANGEMENTS["negotiation"]["close"] == "consent"
    assert U._kinds(U._fold(w, d, U._open("oc", arrangement="negotiation"))) == ["case.refused"] and world_q.docketed(w, U.PARTY) == []
    w.docket.append(_docket_item(U.PARTY, "negotiation", None))
    assert U._kinds(U._fold(w, d, U._determine("dt"))) == ["determine.refused"] and U._obliges(w) == []

    seat, parties = "off_dicastery", ("p_low", "p_mid")
    for who in parties:
        assert U._kinds(U._fold(w, d, Act(id=f"ob_{who}", actor=who, verb="oblige", payload={"subject": seat}))) == ["duty.taken"], who
    edges = [t for t in w.tenures if t.kind == "oblige" and t.object == seat and t.live]
    assert sorted(t.subject for t in edges) == sorted(parties)
    assert all(_opener(w, t) == t.subject for t in edges)
