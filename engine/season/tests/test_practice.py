"""CP-T01-02 -- the practice arm: doing well makes you better, for a while.

A pool addend registered THROUGH `seam/wrappers/sigma.py::register_pool_addend` (so `faculty`, the one pool
reader, sums it): the count of the actor's own acts in the verb's capability key that resolved at Success or
better within the last `practice_window` closed seasons, divided by `practice_step` (floor), capped at
`practice_cap`. Derived from `w.log`; no store, no field. It raises the ACTOR'S pool only: `_opposition_of`
reads the held key and never `faculty`.

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * FIVE SUCCESS-OR-BETTER `tell`s give pool `pool_default` + 2 at the swept arm (window 4, step 2, cap
    `pool_default`): 5 // 2 = 2. A later season in which the oldest two leave the window drops it to 3
    (3 // 2 = 1). Wrong if the pool ignores the window or the step, or exceeds `pool_default + practice_cap`.
  * THE OB AGAINST HIM DOES NOT MOVE: the person practised holds no key, so the opposition is `None` and the
    module composes `obstacle_default` (2.0) before and after. Wrong if practice reached `_opposition_of`.
  * THE SHIPPED ARM IS OFF: `practice_cap` 0 reads `pool_default` for every pool whatever the log holds.
  * WHAT COUNTS: his own acts (another's do not), in the verb's KEY (`speak` shares `copying` with `tell`;
    `research` is `inquiry`), at Success or Overwhelming (Partial and Failure do not), in CLOSED seasons (an act
    of this tick does not: a pool must not depend on the order a barrier resolves its acts).
  * THE ODDS FOLLOW: `odds_of` reads the same pool, so the number shown is the number dealt.
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import VERB_CAPABILITY
from ..seam.wrappers import sigma
from ..state.carriers import Act, Event
from . import test_in12_step9 as T9

ACTOR = "p_a"          # NPC-088's Carin holds `copying`; the practised person below is someone who holds nothing


def _world():
    """NPC-088's realm at tick 0, a person holding no capability key, and the swept arm (window 4, step 2,
    cap `pool_default`) installed on its fixtures."""
    w, _d = T9._npc088()
    who = next(pid for pid, p in sorted(w.persons.items()) if pid != ACTOR and not p.capability)
    w.tick = 10                                           # room behind the window; nothing below reads it
    return w, who


def _swept(w, *, window=4, step=2, cap=None):
    cap = w.fixtures.get("pool_default") if cap is None else cap
    w.fixtures = (w.fixtures.sweep("practice_window", window).sweep("practice_step", step)
                  .sweep("practice_cap", cap))


_n = [0]


def _plant(w, pid, verb, season, degree):
    """One resolved act of `pid`'s, its Event in the log at `season`, as the fold writes it: the Event cites the
    act and carries the roll's degree."""
    _n[0] += 1
    a = Act(id=f"pr_{_n[0]}", actor=pid, verb=verb)
    w.acts.append(a)
    w.log.append(Event(id=f"ev_{a.id}", kind="news.told", changes=[], causes=[a.id], emitted_at=season,
                       degree=degree))
    return a


def _pool(w, who, verb="tell"):
    return sigma.faculty(w, w.persons[who], verb)


def test_the_shipped_arm_is_off_and_reads_pool_default_whatever_the_log_holds():
    w, who = _world()
    fx = w.fixtures
    assert fx.get("practice_cap") == 0, "the arm ships off (CR-18 ships it live)"
    for s in range(6, 10):
        _plant(w, who, "tell", s, "Success")
    assert _pool(w, who) == fx.get("pool_default")


def test_five_successes_give_pool_4_the_window_drops_it_to_3_and_the_ob_stays_2():
    w, who = _world()
    _swept(w)
    default = w.fixtures.get("pool_default")
    assert default == 2
    other = ACTOR
    ob = lambda: sigma._composed_obstacle(                                    # noqa: E731
        sigma.contest_input(w, [other], verb="tell", subject=who, room=None, examined=None))
    inp0 = sigma.contest_input(w, [other], verb="tell", subject=who)
    assert inp0.opposition is None and ob() == 2.0
    assert _pool(w, who) == default                                           # nothing in the log yet
    for s in (6, 7, 8, 9, 9):                                                 # five, the window is [6, 9] at tick 10
        _plant(w, who, "tell", s, "Success")
    assert _pool(w, who) == default + 2 == 4
    assert sigma.contest_input(w, [who], verb="tell", subject=other).pool == 4          # the dealt record
    inp = sigma.contest_input(w, [other], verb="tell", subject=who)
    assert inp.opposition is None and ob() == 2.0                              # the Ob against him did not move
    w.tick = 12                       # the window is [8, 11]: the two acts at 6 and 7 are out, three remain
    assert _pool(w, who) == default + 1 == 3
    assert ob() == 2.0
    w.tick = 14                       # [10, 13]: all out
    assert _pool(w, who) == default


def test_the_pool_never_exceeds_pool_default_plus_the_cap():
    w, who = _world()
    _swept(w)
    for s in (6, 7, 8, 9):
        for _ in range(5):
            _plant(w, who, "tell", s, "Overwhelming")
    assert _pool(w, who) == w.fixtures.get("pool_default") + w.fixtures.get("practice_cap")
    _swept(w, cap=1)
    assert _pool(w, who) == w.fixtures.get("pool_default") + 1


def test_the_step_floors_and_the_window_is_the_fixture():
    w, who = _world()
    _swept(w, step=3, cap=9)
    for s in (9, 9, 9, 9, 9):
        _plant(w, who, "tell", s, "Success")
    assert _pool(w, who) == 2 + 1                                              # 5 // 3
    _swept(w, window=1, step=1, cap=9)
    assert _pool(w, who) == 2 + 5                                              # the window of one closed season: 9
    w.tick = 11
    assert _pool(w, who) == 2                                                  # season 9 is out of [10, 10]


def test_only_his_own_acts_in_the_verbs_key_at_success_or_better_in_closed_seasons_count():
    w, who = _world()
    _swept(w, cap=9, step=1)
    base = _pool(w, who)
    _plant(w, ACTOR, "tell", 9, "Success")                  # another person's act
    _plant(w, who, "tell", 9, "Partial")                    # below Success
    _plant(w, who, "tell", 9, "Failure")
    _plant(w, who, "tell", 9, None)                         # no roll was dealt
    _plant(w, who, "determine", 9, "Success")              # another key (it draws on none)
    _plant(w, who, "research", 9, "Success")                # `research` names no key at HEAD: nothing to practise
    _plant(w, who, "tell", 10, "Success")                   # this tick's: not a closed season
    assert "research" not in VERB_CAPABILITY, "REM-30 landed the inquiry rows: this test now owes a second key"
    assert _pool(w, who) == base
    _plant(w, who, "speak", 9, "Success")                   # the same key as `tell` (`copying`)
    assert VERB_CAPABILITY["speak"] == VERB_CAPABILITY["tell"]
    assert _pool(w, who) == base + 1
    _plant(w, who, "tell", 8, "Overwhelming")
    assert _pool(w, who) == base + 2
    assert _pool(w, who, "research") == base                # a verb with no key practises nothing, whatever it did


def test_one_act_with_several_events_counts_once():
    w, who = _world()
    _swept(w, cap=9, step=1)
    a = _plant(w, who, "tell", 9, "Success")
    for i, kind in enumerate(("confidence.broken", "news.untold")):
        w.log.append(Event(id=f"ev_extra_{a.id}_{i}", kind=kind, changes=[], causes=[a.id], emitted_at=9,
                           degree="Success"))
    assert _pool(w, who) == 2 + 1


def test_the_reader_is_registered_through_faculty_and_called_nowhere_else():
    import inspect
    from ..seam.wrappers import sigma as S
    names = [getattr(f, "__name__", "") for f in S.POOL_ADDENDS]
    assert "practice" in names, names
    src = inspect.getsource(S)
    assert src.count("practice(") == 0 or "register_pool_addend(practice)" in src


def test_odds_of_reads_the_same_pool():
    """The number shown is the number dealt: the practised person's own odds move with his pool."""
    w, who = _world()
    act = Act(id="pr_odds", actor=who, verb="tell", payload={"to": ACTOR})
    for s in (6, 7, 8, 9, 9):
        _plant(w, who, "tell", s, "Success")
    off = sigma.odds_of(w, act)
    _swept(w)
    on = sigma.odds_of(w, act)
    assert off is not None and on is not None and on != off
    assert on[0] < off[0]                                    # fewer Failures with two more dice
    w.tick = 14
    assert sigma.odds_of(w, act) == off                      # the window closed: back to the unpractised odds


def test_an_unregistered_or_nonsense_fixture_is_refused_not_defaulted():
    w, who = _world()
    _swept(w, step=0)
    with pytest.raises(Exception):
        _pool(w, who)
