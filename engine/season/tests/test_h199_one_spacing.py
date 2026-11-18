"""B05.64 -- `H-199`: THE ORDINAL OF REMOVE HAS ONE SPACING.

Two functions read `data/rosters.py::REMOVE_ORDINAL`: refraction's `decision/options.py::channel_remove`
(how far a channel puts its witness) and reception's and proofs' `queries/world_q.py::remove_weight`
(how much a claim held under a source counts). They spaced the ranks differently (`k / (K - 1)` against
`(K - k) / K`), so one quantity had two ladders. `data/rosters.py::remove_distance` (`k / K`) is the one
spacing both read: the most removed rank is `(K - 1) / K`, never 1, so it still counts as evidence.
"""

from __future__ import annotations

from ..data.rosters import CHANNEL_CLAIM_SOURCE, REMOVE_ORDINAL, WITNESS_CHANNELS, remove_distance
from ..decision.options import channel_remove, refracted_confidence
from ..harness import probes as P
from ..queries.world_q import remove_weight
from ..state.carriers import Claim

HEARER = "p_mid"


def test_channel_remove_and_remove_weight_read_one_spacing():
    """For every source in the ordinal `remove_weight(s) == 1.0 - remove_distance(s)`, and for every
    channel `channel_remove(ch) == remove_distance(CHANNEL_CLAIM_SOURCE[ch])`, exactly. Falsifier: two
    spacings of one ordinal (`channel_remove` at `k / (K - 1)`) make the second half fail."""
    checked = 0
    for source in REMOVE_ORDINAL:
        assert remove_weight(source) == 1.0 - remove_distance(source), source
        checked += 1
    assert checked == len(REMOVE_ORDINAL)
    channels = 0
    for ch in WITNESS_CHANNELS:
        assert channel_remove(ch) == remove_distance(CHANNEL_CLAIM_SOURCE[ch]), ch
        channels += 1
    assert channels == len(WITNESS_CHANNELS)
    # The spacing is the ordinal's own: firsthand is not removed, and no rank is removed to 1.
    assert remove_distance(REMOVE_ORDINAL[0]) == 0.0
    assert max(remove_distance(s) for s in REMOVE_ORDINAL) < 1.0


def test_the_two_orderings_agree_at_three_gains():
    """One telling at `confidence_default`, heard through every channel, at `refraction_gain` 0, 0.5 and
    1.0. Landed confidence never rises as `remove_distance` rises; the sources ranked by `remove_weight`
    descending are the sources ranked by landed confidence descending; at 0 every landing is the
    teller's own (the control); at 1.0 the most removed channel lands above 0 (`k / (K - 1)` made it 0)."""
    w = P.tiny_world()
    full = w.fixtures.get("confidence_default")
    p = w.persons[HEARER]
    c = Claim("c_h199", "p_low", "Hh", "stores:grain", 8, 0, "told_by", full, "own")
    by_source = {CHANNEL_CLAIM_SOURCE[ch]: ch for ch in reversed(WITNESS_CHANNELS)}
    assert set(by_source) == set(REMOVE_ORDINAL)
    checked = 0
    for gain in (0.0, 0.5, 1.0):
        landed = {s: refracted_confidence(p, c, ch, gain) for s, ch in by_source.items()}
        nearest_first = sorted(REMOVE_ORDINAL, key=remove_distance)
        seq = [landed[s] for s in nearest_first]
        assert all(a >= b for a, b in zip(seq, seq[1:])), (gain, landed)
        if gain == 0.0:
            assert set(landed.values()) == {full}, landed
        else:
            by_weight = sorted(REMOVE_ORDINAL, key=remove_weight, reverse=True)
            by_landed = sorted(REMOVE_ORDINAL, key=lambda s: landed[s], reverse=True)
            assert len(set(landed.values())) == len(REMOVE_ORDINAL), (gain, landed)
            assert by_weight == by_landed, (gain, by_weight, by_landed)
        if gain == 1.0:
            assert landed[REMOVE_ORDINAL[-1]] > 0, landed
        checked += 1
    assert checked == 3
