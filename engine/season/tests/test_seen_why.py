"""B09.17 -- A WITNESS MAY CONNECT WHAT HE HOLDS: `Seen.why` is a claim in the witness's own ledger, by a keyed draw.

`why` (`epistemic._term_why`) is the id of a claim the witness HOLDS that was deposited from an antecedent Event of the one he
witnessed, filled where his channel supplies the term (`rosters.yaml: observation_terms.supplied_by`) and `connection_chance`
(`data/fixtures.py`, `H-458`) says he connects them. At the shipped 0.0 nothing is read, nothing is drawn, and the realm is today's.
The on-arm is run here, in the test's own fixtures (`DEFAULT_FIXTURES.sweep("connection_chance", p)`); the shipped value stays 0.0.

Five claims, each executed and each able to fail:
  1. at 0.0 no draw is taken, no `seen` claim carries `why`, and the hash equals a run whose `why` reader is replaced by `None`;
  2. every `why` read on-arm names a claim the holder held AT THE READ (the barrier before that Event's deposits), `checked >= 100`;
  3. over the eligible deposits (he holds an antecedent and his channel supplies `why`) the share that connect is inside the
     binomial 99% band of the fixture's chance, and is neither 0 nor 1 (the draw is a draw, not decoration);
  4. a witness admitted by the document channel alone never carries `why`, and the run holds at least one such witness;
  5. `chronicle(p).threads` is empty for everyone at the control and non-empty on-arm, each thread a `seen` claim and the claim it
     names, both held.
"""
from __future__ import annotations

import math

import pytest

from .. import epistemic
from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..decision.sheet import chronicle
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.attribution import actor_of, causing_act, event_by_id

CHANCE = 0.6                  # the on-arm's own value; the shipped one is 0.0
SEASONS = 1                   # the fewest that give `checked >= 100` (CLAUDE.md §0.4 pt 6)
SEED = 0


def _play(chance=None, seasons=SEASONS, seed=SEED):
    fx = DEFAULT_FIXTURES if chance is None else DEFAULT_FIXTURES.sweep("connection_chance", chance)
    w = build_realm(seed, fixtures=fx)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())
    for _ in range(seasons):
        d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w


class _Tap:
    """What the barrier reads, recorded at the read: every `why` reader result with whether the holder held it THEN, every
    antecedent look-up, and every draw requested."""

    def __init__(self):
        self.reads, self.antecedents, self.draws = [], {}, 0


def _tapped(chance, mp, seasons=SEASONS):
    tap = _Tap()
    real_why, real_ante = epistemic.TERM_READERS["why"], epistemic._antecedent_claim
    real_draw = epistemic.draw_factory

    def why(w, e, act, pid):
        res = real_why(w, e, act, pid)
        held = res is None or any(c.id == res for c in w.persons[pid].ledger)
        tap.reads.append((pid, e.id, res, held))
        return res

    def ante(w, e, pid):
        res = real_ante(w, e, pid)
        tap.antecedents[(pid, e.id)] = res
        return res

    def draw_factory(*a, **k):
        tap.draws += 1
        return real_draw(*a, **k)

    mp.setitem(epistemic.TERM_READERS, "why", why)
    mp.setattr(epistemic, "_antecedent_claim", ante)
    mp.setattr(epistemic, "draw_factory", draw_factory)
    return tap, _play(chance, seasons)


def _antecedent_pairs(tap):
    return [key for key, claim in tap.antecedents.items() if claim is not None]


def _why_claims(w):
    return [c for p in w.persons.values() for c in p.ledger
            if c.predicate == epistemic.SEEN_PREDICATE and getattr(c.value, "why", None) is not None]


@pytest.fixture(scope="module")
def control():
    """The shipped world, tapped, and the same world with the `why` reader replaced by `None`."""
    mp = pytest.MonkeyPatch()
    try:
        tap, w = _tapped(None, mp)
    finally:
        mp.undo()
    mp = pytest.MonkeyPatch()
    try:
        mp.setitem(epistemic.TERM_READERS, "why", lambda w, e, act, pid: None)
        w_none = _play(None)
    finally:
        mp.undo()
    return tap, w, w_none


@pytest.fixture(scope="module")
def on_arm():
    mp = pytest.MonkeyPatch()
    try:
        tap, w = _tapped(CHANCE, mp)
    finally:
        mp.undo()
    return tap, w


def test_control_chance_zero_takes_no_draw_and_hash_equal(control):
    tap, w, w_none = control
    assert DEFAULT_FIXTURES.get("connection_chance") == 0.0, "the shipped value is the control"
    assert len(w.log) > 1000, "the control run barely happened: this proves nothing"
    assert tap.draws == 0, "a chance of 0.0 takes no draw"
    assert not _why_claims(w), "no `seen` claim carries `why` at the control"
    assert w.content_hash() == w_none.content_hash()


def test_every_why_names_a_claim_in_the_holders_ledger(on_arm):
    tap, w = on_arm
    checked = 0
    for pid, eid, res, held in tap.reads:
        if res is None:
            continue
        checked += 1
        assert held, f"{pid}'s `why` for {eid} names {res}, which his ledger did not hold at the read"
    assert checked >= 100, f"only {checked} `why` read: the loop checked too little to mean anything"
    assert _why_claims(w), "the on-arm deposited no `seen` claim carrying `why`"


def test_share_with_why_inside_binomial_band(on_arm):
    tap, _ = on_arm
    got = {(pid, eid): res for pid, eid, res, _ in tap.reads}
    eligible = [k for k, a in tap.antecedents.items() if a is not None and k in got]
    n = len(eligible)
    assert n >= 100, f"{n} eligible deposits: too few for a band to mean anything"
    k = sum(1 for key in eligible if got[key] is not None)
    assert all(got[key] == tap.antecedents[key] for key in eligible if got[key] is not None), "a connection names the antecedent"
    band = 2.576 * math.sqrt(CHANCE * (1 - CHANCE) / n)           # the 99% band (z = 2.576)
    assert 0 < k < n, f"{k} of {n} eligible witnesses connected: the draw is decoration"
    assert abs(k / n - CHANCE) <= band, f"{k}/{n} = {k / n:.3f} is outside {CHANCE} +/- {band:.3f}"


def test_document_channel_never_carries_why(on_arm):
    """A witness the DOCUMENT channel alone admits, holding an antecedent, at the chance 1.0 at which every eligible witness connects:
    his `seen` carries no `why`. The same witness admitted by presence instead does (the control that makes the first observable)."""
    _, w = on_arm
    fx = w.fixtures
    w.fixtures = fx.sweep("connection_chance", 1.0)
    mp = pytest.MonkeyPatch()
    try:
        w.discard_caches()
        pairs = []
        for pid, eid in _antecedent_pairs(on_arm[0]):
            e = event_by_id(w, eid)
            if e is not None and pid in w.persons and epistemic._antecedent_claim(w, e, pid) is not None \
                    and causing_act(w, e) is not None and actor_of(w, e) != pid:
                pairs.append((pid, e))
        assert len(pairs) >= 20, f"{len(pairs)} witnesses hold an antecedent at the end: too few for the claim to be observable"
        for pid, e in pairs[:20]:
            act = causing_act(w, e)
            for ch in epistemic.WITNESS_CHANNELS:
                mp.setitem(epistemic.CHANNEL_PREDICATES, ch, lambda w, e, pid, ch=ch: ch == "document_key")
            assert epistemic.seen_of(w, e, act, pid, "all_five").why is None, f"{pid} holds a `why` through the document channel"
            for ch in epistemic.WITNESS_CHANNELS:
                mp.setitem(epistemic.CHANNEL_PREDICATES, ch, lambda w, e, pid, ch=ch: ch == "co_located")
            assert epistemic.seen_of(w, e, act, pid, "all_five").why is not None, f"{pid}, present, did not connect at chance 1.0"
    finally:
        mp.undo()
        w.fixtures = fx
        w.discard_caches()


def test_chronicle_threads_empty_at_control(control, on_arm):
    _, w, _ = control
    for p in w.persons.values():
        assert chronicle(p, w.fixtures).threads == ()
    _, won = on_arm
    threaded = 0
    for p in won.persons.values():
        held = {c.id: c for c in p.ledger}
        for claim_id, why_id in chronicle(p, won.fixtures).threads:
            threaded += 1
            assert claim_id in held and why_id in held, "a thread names a claim he no longer holds"
            assert held[claim_id].predicate == epistemic.SEEN_PREDICATE and held[claim_id].value.why == why_id
    assert threaded > 0, "no person's chronicle holds a thread on-arm: the control's emptiness is unobserved"
