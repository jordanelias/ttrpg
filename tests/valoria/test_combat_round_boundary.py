"""PCR-1 (A-101): a round ends at every separation, and says how it ended.

A round is one `wrapper.engagement` call. Before this item two branches (the longer weapon's created-moment reopen and
the clean fighting withdrawal) `continue`d into a second approach inside the same round: the fighters separated and
closed again with no round boundary. Now each returns, and the reason a round ended is one of `vocabulary.ROUND_ENDS`.

  (1) a reach-mismatched fight never re-closes inside a round (red before the returns);
  (2) every `separation` reason and every `round_end`'s `ended_by` is a member of the closed set (red before it existed);
  (3) at equal reach neither re-opening branch draws, so neither new ending appears (the control).

The reading of a round is `workbench/round_probe.py::rounds_of`, the one owner of it; the same probe prints the table.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1', 'workbench'))
import round_probe as P   # noqa: E402

from modules.combat import vocabulary as V   # noqa: E402

_MISMATCHED = ((('staff', 'none'), ('dagger', 'none')), (('poleaxe', 'heavy'), ('longsword', 'heavy')))
_MIRROR = (('arming', 'light'), ('arming', 'light'))
_WITHDRAWING = (('rapier', 'none'), ('arming', 'light'))   # the pair the clean fighting withdrawal fires in


def _rounds(pair, seeds):
    out = []
    for s in seeds:
        out += P.rounds_of(P.play(pair, s)[1])
    return out


def test_no_round_closes_twice():
    """Over 200 seeds of each reach-mismatched pair, no round has an `approach` after a beat at closed measure."""
    checked = 0
    for pair in _MISMATCHED:
        for r in _rounds(pair, range(200)):
            if r['exchanges'] or r['reopened']:   # the round had a closed beat to be followed by an approach
                checked += 1
            assert not r['reopened'], f"{P._name(pair)}: a round re-closed inside itself (ended by {r['ended_by']})"
    assert checked >= 200


def test_separation_reasons_are_closed():
    """Every `separation` reason and every returned `ended_by` is in `ROUND_ENDS`; a reopen and a withdrawal are seen."""
    seen_sep, seen_end, rounds = set(), set(), 0
    for pair in _MISMATCHED + (_WITHDRAWING, _MIRROR):
        for s in range(200):
            for e in P.play(pair, s)[1]:
                if e['kind'] == 'separation':
                    seen_sep.add(e['reason'])
                elif e['kind'] == 'round_end':
                    seen_end.add(e['ended_by']); rounds += 1
    assert rounds >= 800
    assert seen_sep <= set(V.ROUND_ENDS) and seen_end <= set(V.ROUND_ENDS), (seen_sep, seen_end)
    assert {'reopen', 'disengage'} <= seen_sep   # the two new endings are reachable, so the closed-set check observes them


def test_equal_reach_is_untouched():
    """The arming mirror at seeds 0-199 never reaches either re-opening branch: no `disengage` event, neither new ending."""
    checked = 0
    for s in range(200):
        _, tr = P.play(_MIRROR, s)
        assert not any(e['kind'] == 'disengage' for e in tr)
        assert not any(e['kind'] == 'separation' and e['reason'] in ('reopen', 'disengage') for e in tr)
        checked += sum(e['kind'] == 'round_end' for e in tr)
    assert checked >= 200
