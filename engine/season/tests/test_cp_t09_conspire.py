"""B21b.18 (CP-T09-09, AM-F-17; `FA §3.3` S7): `conspire` -- A PLOT WITH BACKERS.

Any person (`own`) invites a known person `to` a plot against the holder of a seat (`subject`, a `Target`-classed holder `world_q.plot_targets` offers). The invitation is a
draw on the invitee (`contests: "a standing"`), its obstacle the one composer's, with the invitee's bond to the target (`invitee_tie_to_target`) and his regard of the
target (`regard_of_target`) among its terms. A plotter who holds no plot LAYS one (the OUGHT Proposition and his own `commit`, `plot.laid`); one who holds a plot RECRUITS:
won, the invitee's own `commit` to it opens (`plot.joined`, the gate's `recruitment` basis); lost, `plot.refused` and nothing opens. All drive the built realm, the uncapped
arm (`obstacle_ceiling` None: `H-213`'s control, where every term is read), folding through the shipped `SeasonDriver.resolve`. The Duke of Varfell plots against the
Duchess of Hafenmark (the first act's occasion at tick 0: he reads her below 0), inviting a Varfell man with no seat and no oath.
"""
from __future__ import annotations

import functools

from engine.season.boot.realm import build_realm
from engine.season.data.matrix import WriteClass
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q as Q
from engine.season.state.carriers import Act, Claim, Tenure

PLOTTER, TARGET, TARGET_SEAT, MAN, OTHER = "p_npc_052", "p_npc_050", "off_duchess_hafenmark", "p_npc_002", "p_npc_005"


def _world(seed=0):
    """The realm at `seed`, uncapped."""
    w = build_realm(seed)
    w.fixtures = w.fixtures.sweep("obstacle_ceiling", None)
    return w


def _conspire(w, name, to=MAN, actor=PLOTTER, subject=TARGET):
    d = SeasonDriver(w)
    out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(name, actor, "conspire", payload={"subject": subject, "to": to})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return d, out


@functools.lru_cache(maxsize=None)
def _lay_act(seed):
    """The first act id (of 40) whose first invitation at `seed` folds at a band that writes (a lost first act changes nothing, so the search is one world)."""
    w = _world(seed)
    for n in range(40):
        if _conspire(w, f"a_lay_{n}", OTHER)[1][0].kind == "plot.laid":
            return n
    raise AssertionError("no first invitation of 40 laid a plot")


def _laid(seed=0):
    """A fresh world where the plotter has laid his plot (a world is rebuilt, never copied: a copy's act store does not take a later act's events)."""
    w = _world(seed)
    assert _conspire(w, f"a_lay_{_lay_act(seed)}", OTHER)[1][0].kind == "plot.laid"
    return w


def _commits(w, who, plot):
    return [t for t in w.tenures if t.kind == "commit" and t.subject == who and t.object == plot.id and t.live]


def _terms(event):
    return [name for name, _ in dict(event.ending)["terms"]]


def test_the_first_conspire_mints_a_plot_and_the_plotters_commit():
    """The first conspire of a man who holds no plot lays one: an OUGHT Proposition (subject the target's holder, predicate naming the seat) with the plotter's own live
    `commit` and his maker's `hold`, and the invitee is not yet a backer. The control: before it he holds none and no plot is in the world. The reader is built: the plot is
    his ambition (`ambitions`)."""
    w0 = _world()
    assert Q.plot_held(w0, w0.persons[PLOTTER]) is None and not any(p.id.startswith("plot:") for p in w0.propositions.values()), "control failed -- a plot existed"
    w = _laid()
    plot = Q.plot_held(w, w.persons[PLOTTER])
    assert plot is not None and plot.mood == "OUGHT" and plot.subject == TARGET and plot.predicate == f"plot:{TARGET_SEAT}"
    assert _commits(w, PLOTTER, plot) and any(t.kind == "hold" and t.object == plot.id and t.live for t in w.persons[PLOTTER].tenures)
    assert plot.id in Q.ambitions(w, w.persons[PLOTTER]) and not _commits(w, OTHER, plot), "the invitee was enlisted by the act that laid the plot"


def test_a_won_conspire_on_a_held_plot_opens_the_invitees_commit_only_on_won():
    """On a held plot the invitation is the invitee's draw: won (`plot.joined`) his own `commit` to the plot opens, admitted at the gate; lost (`plot.refused`) nothing opens,
    and witnessed, a person at the place holds the refusal as a claim (his claim against the plotter). The control: before the act he holds no commit to it."""
    seen = {}
    for n in range(40):
        w = _laid()
        plot = Q.plot_held(w, w.persons[PLOTTER])
        assert not _commits(w, MAN, plot), "control failed -- the invitee was committed already"
        d, out = _conspire(w, f"a_rec_{n}")
        assert out[0].kind in ("plot.joined", "plot.refused"), [e.kind for e in out]
        seen[out[0].kind] = (w, d, out, plot)
        if len(seen) == 2:
            break
    assert set(seen) == {"plot.joined", "plot.refused"}, sorted(seen)
    w, _d, _out, plot = seen["plot.joined"]
    assert len(_commits(w, MAN, plot)) == 1
    w, d, out, plot = seen["plot.refused"]
    assert not _commits(w, MAN, plot)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    assert any(c.predicate == "plot.refused" for p in w.persons.values() for c in p.ledger), "no one holds the witnessed refusal"


def test_an_invitee_sworn_to_the_target_seat_refuses_more_often():
    """The obstacle reads him: the same invitation on the same dice (seeds 0-9, two acts each), to the man with a live oath to the target seat and to the same man free of it.
    The tied man's obstacle lists `invitee_tie_to_target` and the free man's does not; no invitation the free man refuses is accepted by the tied one (the draw is the act's own,
    so the terms alone differ), and the tied man refuses more of the twenty. The control: with `tie_step` swept to 0 the term is not listed and the two arms are the same."""
    free = tied = checked = 0
    for seed in range(10):
        for n in range(2):
            a, b = _laid(seed), _laid(seed)
            b.add_tenure(Tenure(f"t_tie_{MAN}", MAN, TARGET_SEAT, "oblige", since=0))
            f, t = _conspire(a, f"a_tie_{n}")[1][0], _conspire(b, f"a_tie_{n}")[1][0]
            assert "invitee_tie_to_target" not in _terms(f) and "invitee_tie_to_target" in _terms(t), (_terms(f), _terms(t))
            free_refused, tied_refused = f.kind == "plot.refused", t.kind == "plot.refused"
            assert tied_refused or not free_refused, "a higher obstacle accepted what the lower one refused"
            free, tied, checked = free + free_refused, tied + tied_refused, checked + 1
    assert checked >= 10
    assert tied > free, (free, tied)
    off = _laid(0)
    off.fixtures = off.fixtures.sweep("tie_step", 0.0)
    off.add_tenure(Tenure(f"t_tie_{MAN}", MAN, TARGET_SEAT, "oblige", since=0))
    assert "invitee_tie_to_target" not in _terms(_conspire(off, "a_tie_0")[1][0])


def _heard(w, who=PLOTTER):
    """Two news items landed with the plotter, about two men, the id of the one about OTHER sorting before the one about the target: nothing else distinguishes them."""
    w.persons[who].ledger += [Claim("c_a_other", who, OTHER, "exists:Person", 1, 0, "firsthand", 100, "own"),
                              Claim("c_z_target", who, TARGET, "exists:Person", 1, 0, "firsthand", 100, "own")]


def _tiers(w, who=PLOTTER):
    """`{question id: attention tier}` and the order, for the plotter's two news items."""
    p = w.persons[who]
    qs = Q.questions_for(w, p)
    key = Q.attention_key(w, p)
    ids = [q.id for q in qs]
    return {q.id: key(q)[0] for q in qs}, ids


def test_a_conspirators_first_question_each_lap_is_about_the_target():
    """The reader (M7) is built: a `commit` to an OUGHT is an ambition and an ambition's referent is tier 0 (`attention_key`), so once the plotter holds a plot the news about his
    target is a tier-0 question and is answered ahead of an earlier-sorting item about another man -- where before the plot, on the same two items, it is neither (the control).
    (The realm's Duke answers a tier-1 question about his own guard first, which holds the plot or not; the claim is about the target against the other news.)"""
    w0 = _world()
    _heard(w0)
    tier0, order0 = _tiers(w0)
    assert order0.index("q:claim:c_a_other") < order0.index("q:claim:c_z_target") and tier0["q:claim:c_z_target"] != 0, "control failed -- the target was first before the plot"
    w = _laid()
    _heard(w)
    tier, order = _tiers(w)
    assert tier["q:claim:c_z_target"] == 0 and tier["q:claim:c_a_other"] != 0, tier
    assert order.index("q:claim:c_z_target") < order.index("q:claim:c_a_other"), order
