"""v11 CR-32 (B21c.01), H-181: a faction's rank ladder as POSTS ON SEATS (`offices.yaml: ladders:`), the `marks` a witness holds of an actor
who holds one, and the one scale `person_q.rank` reads.

FALSIFIER (the entry's EXIT): a witness of a Church-ladder post-holder's act holds that post in `marks`; a witness of a Riskbreaker-ladder
post-holder (that ladder shows no livery) holds none; Church rank 2 told by a teller seen at rank 6 reads `rank == +1` (rank 6 told by rank 2,
-1; the same rank, 0); a Varfell-only teller with no title reads 0; an unseen teller 0; a post and a title never compare. CONTROL: an empty
`ladders:` map stamps no post on a hold and shows no post in `marks`, so every hold and every `seen` claim is what it was before the item, and
`rank` is 0 for every pair.

Every test drives a HAND-BUILT world (`tiny_world`) through the real fold and the real WITNESS; none asserts that a ladder post is held in the
seed-0 realm (the realm's reading is the batch's hash reading, not a pin here).
"""
from __future__ import annotations

import pytest

from ..data import rosters
from ..data.rosters import SEEN_PREDICATE
from ..epistemic import Seen
from ..queries.person_q import rank
from ..state.carriers import Claim
from ._gov_fixtures import seat
from .test_in12_conceal import DUKE, WATCHER, _convene, _witness, _world

CHURCH, CROWN = "Church of Solmund", "Valorsmark"


def _seat(w, who, post, faction, key):
    """Seat `who` on a new office of `post` (a hand-built seat: the hold is stamped by `add_tenure`, as every world-built one is)."""
    seat(w, f"off_{key}", post, None, ["issue"], who, f"t_{key}", faction=faction)


def _marks_after_convening(post, faction):
    """The `marks` of the one `seen` claim `WATCHER` holds of `DUKE` after the Duke, who also holds `post`, convenes where they both stand."""
    w, d = _world()
    _seat(w, DUKE, post, faction, "x")
    out, _e = _convene(w, d)
    _witness(w, d, out)
    seen = [c.value for c in w.persons[WATCHER].ledger if c.predicate == SEEN_PREDICATE]
    assert len(seen) == 1, f"the co-located witness holds {len(seen)} `seen` claims: the comparison is vacuous"
    return seen[0].marks


def _told(p, who, marks, n=0):
    """Plant `p`'s own sighting of `who` carrying `marks` (the claim `_term_marks` deposits, as the witness would hold it)."""
    p.ledger.append(Claim(f"c_seen_{who}_{n}", p.id, "S", SEEN_PREDICATE, Seen(who=who, marks=marks), 0, "witnessed", 100, "own"))


def _person_holding(post, faction):
    w, _d = _world()
    _seat(w, WATCHER, post, faction, "mine")
    return w.persons[WATCHER]


# ======================================================================================
# THE MARKS
# ======================================================================================

def test_a_church_post_shows_in_marks():
    assert "Cardinal" in _marks_after_convening("Cardinal", CHURCH)


def test_riskbreaker_post_shows_nothing():
    """The Riskbreaker ladder's Livery cells all read "None", so its posts are held and never shown; a Church post held the same way is."""
    assert "Riskbreaker Commander" not in _marks_after_convening("Riskbreaker Commander", CROWN)
    assert "Cardinal" in _marks_after_convening("Cardinal", CHURCH), "the control: the same plumbing shows a visible ladder's post"


# ======================================================================================
# THE RANK: one scale, never two
# ======================================================================================

def test_rank_reads_one_scale():
    me = _person_holding("Deacon", CHURCH)                       # Church ordinal 2
    _told(me, "p_high", ("Cardinal",))                           # Church ordinal 6
    assert rank(me, "p_high") == 1
    assert rank(_person_holding("Cardinal", CHURCH), "p_high") == 0, "no sighting: the teller is unseen"
    higher = _person_holding("Cardinal", CHURCH)
    _told(higher, "p_high", ("Deacon",))
    assert rank(higher, "p_high") == -1
    same = _person_holding("Deacon", CHURCH)
    _told(same, "p_high", ("Deacon",))
    assert rank(same, "p_high") == 0
    other = _person_holding("Deacon", CHURCH)
    _told(other, "p_high", ("Jarl",))                            # a Varfell post, no title: no scale both stand on
    assert rank(other, "p_high") == 0
    assert rank(me, "p_nobody") == 0, "an unseen teller"
    # the NEWEST sighting is the one read
    _told(me, "p_high", ("Deacon",), n=1)
    assert rank(me, "p_high") == 0


def test_rank_through_the_witness_reads_the_post_the_witness_deposited():
    w, d = _world()
    _seat(w, WATCHER, "Deacon", CHURCH, "mine")
    _seat(w, DUKE, "Cardinal", CHURCH, "his")
    out, _e = _convene(w, d)
    _witness(w, d, out)
    assert rank(w.persons[WATCHER], DUKE) == 1
    assert rank(w.persons[DUKE], WATCHER) == 0, "the Duke never saw the watcher act: an unseen teller"


def test_a_ladder_post_never_compares_with_a_title():
    ladder = _person_holding("Deacon", CHURCH)
    _told(ladder, "p_high", ("Duke",))                           # a title, to a person who holds a ladder post
    assert rank(ladder, "p_high") == 0
    w, _d = _world()                                             # the Duke holds the title `Duke` and no ladder post
    duke = w.persons[DUKE]
    _told(duke, "p_other", ("Cardinal",))
    assert rank(duke, "p_other") == 0
    # the title scale, where both stand on it: `rung_kinds` ordinal (a realm outranks a duchy, a territory does not)
    _told(duke, "p_king", ("King",))
    _told(duke, "p_low", ("Lord",))
    assert (rank(duke, "p_king"), rank(duke, "p_low")) == (1, -1)


# ======================================================================================
# THE CONTROL
# ======================================================================================

def test_empty_ladders_is_the_prior_hash(monkeypatch):
    """With `ladders: {}` a seat's `hold` carries only the grant (`remit_acts`, `seat_rung`), a witness's `marks` are CR-30's heritage alone, and
    `rank` is 0 -- every thing the world's digest folds is what it was. With the shipped ladders the same world carries a stamped post."""
    def build():
        w, d = _world()
        w.persons[DUKE].heritage = "altonian"
        _seat(w, DUKE, "Cardinal", CHURCH, "his")
        out, _e = _convene(w, d)
        _witness(w, d, out)
        return w

    shipped = build()
    assert {k for t in shipped.persons[DUKE].tenures if t.kind == "hold" for k in t.payload} == {"remit_acts", "seat_rung", "post"}, "vacuous control"
    monkeypatch.setattr(rosters, "LADDERS", {})
    w = build()
    assert {k for t in w.persons[DUKE].tenures if t.kind == "hold" for k in t.payload} == {"remit_acts", "seat_rung"}
    marks = [c.value.marks for c in w.persons[WATCHER].ledger if c.predicate == SEEN_PREDICATE]
    assert marks == [("altonian",)]
    me = _person_holding("Deacon", CHURCH)
    _told(me, "p_high", ("Cardinal",))
    assert rank(me, "p_high") == 0
