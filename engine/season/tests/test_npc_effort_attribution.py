"""B08.01 (H-249's residue, CF-E8-2) -- WHERE A FORMED NPC EFFORT IS LOST, COUNTED BEFORE THE CHOOSER IS REWRITTEN.

`decision/choose.py::settle_efforts` forms `effort` variants; `pack_scenes`' inner `take()` can lose one of them in three
places. THE COUNTER (test-side, read-only, it draws nothing and writes nothing to the world):
  * LOST AT THE BUDGET BREAK -- `take()` stops at `left <= 0`, so a chunk it never reaches never builds a Scene: no Scene is
    constructed carrying the effort act.
  * LOST AT THE STRIP -- the chunk is built, but the effort act is rebuilt at effort 0 (`Candidate(.., without EFFORT)`):
    the first-built Scene held the act at `effort e > 0`, the Scene that was kept holds the same act with no `effort`.
  * REACHES AN ACT -- the kept Scene holds the act with its `effort` payload untouched.
B08.04 (CF-E8-2's conditional, UNDECIDED (5)): the reading put the loss at the BUDGET BREAK, so the same counter also runs the control
`pack_scenes` with `hangs_on` off (every `Act.after` None, the chooser as it was before B08.04) beside each real call, and
`test_pack_scenes_keeps_the_first_ranked_effort_variant` compares the Scenes: setting `after` must move nothing else.
`take()` has a fourth, unnamed way to lose one: `chunk[:1]` drops the chunk's later acts, effort or not. It is counted
apart (`trimmed`) so the three named bins stay what CF-E8-2 asked for.

HOW THE BINS ARE TOLD APART WITHOUT REIMPLEMENTING `take()`: `CH.Scene` is rebound to a recording subclass for the span of
one `pack_scenes` call, and `CH.pack_scenes` to a wrapper (`make_chooser` reads both by bare name). `take()` builds the
Scene of one chunk one to three times, all under the same scene id (`mint(.., "scene", n)`); the FIRST build holds the whole
chunk, the LAST is the one kept. Each formed effort in `ranked` is looked up in those builds: absent from every first
build -> break; in the first build and kept untouched -> reaches an act; in the first build, kept at effort 0 -> strip;
anything else -> trimmed. `break` is the result of a failed lookup (an absence), so a reading of it is only as good as the counter's
lookup finding the other bins: the strip and the reach were seen to be found when the counter was written, a control run once and not kept.
"""
from __future__ import annotations

import pytest

from ..boot.realm import build_realm
from ..decision import choose as CH
from ..harness.populated import run
from ..state.carriers import EFFORT

SEED = 0
SEASONS = 2
FORMATIONS = 20             # CF-E8-2's reading size: the first 20 formed efforts, in the order the chooser formed them
BINS = ("break", "strip", "reach", "trimmed")


def _effort_of(c) -> int:
    return (c.operands or {}).get(EFFORT, 0)


def _same(act, verb, payload) -> bool:
    return act.verb == verb and (act.payload or {}) == (payload or {})


class Counter:
    """A read-only counter over `pack_scenes`: `bins` is a Counter-like dict, `formed` the total of efforts seen in a
    `ranked`. Use as a context manager; it restores both names on exit, raising or not."""

    def __init__(self):
        self.bins = {b: 0 for b in BINS}
        self.formed = 0
        self.order = []          # one bin name per formed effort, in formation order
        self._builds = None
        self.compared = 0        # `pack_scenes` calls also run with `after` off
        self.hung = 0            # of those, the calls whose Scenes hold an act with `after` set
        self.moved = []          # the calls whose Scenes differ, beyond `after`, from the control's

    def __enter__(self):
        counter, real_pack, real_scene = self, CH.pack_scenes, CH.Scene

        class Recording(real_scene):
            def __init__(self, *a, **k):
                super().__init__(*a, **k)
                if counter._builds is not None:
                    counter._builds.setdefault(self.id, []).append(self)

        def pack(p, ranked, n_scenes, fx, mint, occasion=None):
            counter._builds = {}
            try:
                out = real_pack(p, ranked, n_scenes, fx, mint, occasion=occasion)
                counter._classify(ranked, out)
            finally:
                counter._builds = None
            counter._compare(real_pack, (p, ranked, n_scenes, fx, mint), occasion, out)
            return out

        self._saved = (real_pack, real_scene)
        CH.Scene, CH.pack_scenes = Recording, pack
        return self

    def __exit__(self, *exc):
        CH.pack_scenes, CH.Scene = self._saved
        return False

    def _compare(self, real_pack, args, occasion, out):
        """The same call with `after` off: `choose.hangs_on` is the one place `pack_scenes` sets it. Pure -- `mint` is a hash."""
        hangs_on = CH.hangs_on
        CH.hangs_on = lambda prev, c: None
        try:
            control = real_pack(*args, occasion=occasion)
        finally:
            CH.hangs_on = hangs_on
        assert all(a.after is None for sc in control for a in sc.acts), "the control still hangs an act"

        def shape(scenes):
            return [(sc.id, [(a.id, a.verb, a.payload, a.via) for a in sc.acts]) for sc in scenes]

        self.compared += 1
        self.hung += any(a.after is not None for sc in out for a in sc.acts)
        if shape(out) != shape(control):
            self.moved.append((args[0].id, shape(out), shape(control)))

    def _classify(self, ranked, out):
        for c in ranked:
            if _effort_of(c) <= 0:
                continue
            self.formed += 1
            payload = CH._payload_of(c)
            stripped = {k: v for k, v in payload.items() if k != EFFORT}
            where = next(((i, b) for b in self._builds.values()
                          for i, a in enumerate(b[0].acts) if _same(a, c.verb, payload)), None)
            if where is None:
                bin_ = "break"                      # no Scene was ever built holding it
            else:
                i, builds = where
                kept = builds[-1].acts
                if any(_same(a, c.verb, payload) for a in kept):
                    bin_ = "reach"
                elif i == 0 and kept and _same(kept[0], c.verb, stripped):
                    bin_ = "strip"
                else:
                    bin_ = "trimmed"                # `chunk[:1]` dropped it
            self.bins[bin_] += 1
            self.order.append(bin_)

    def first(self, n: int) -> dict:
        """The three-bin reading (plus `trimmed`) over the first `n` formations."""
        return {b: self.order[:n].count(b) for b in BINS}


@pytest.fixture(scope="module")
def season_reading():
    w = build_realm(SEED)
    with Counter() as cnt:
        run(SEASONS, SEED, w=w)
    return cnt


def test_every_formed_effort_lands_in_one_bin(season_reading):
    """GAME STATE: on `build_realm(0)` over two seasons, the counter classifies every effort `settle_efforts` forms (lost at `take()`'s
    break, lost at the strip to effort 0, reaches an act, or trimmed with its chunk) and prints the reading. The bins are one if/elif
    chain with a catch-all, so their sum is the formed total by construction and is not asserted.
    `assert formed >= FORMATIONS`: a counter that saw nothing proves nothing (CLAUDE.md §0.1 pt 2)."""
    cnt = season_reading
    assert cnt.formed >= FORMATIONS, f"the counter saw {cnt.formed} formed efforts, fewer than the {FORMATIONS} the reading needs"
    print(f"\nB08.01 reading (seed {SEED}, {SEASONS} seasons): formed {cnt.formed}; all {cnt.bins}; "
          f"first {FORMATIONS}: {cnt.first(FORMATIONS)}")


def test_pack_scenes_keeps_the_first_ranked_effort_variant(season_reading):
    """GAME STATE (lane `season_loop`, by tree): A CHANGE DETECTOR, NOT A PROOF. B08.01 put every formed NPC effort's loss at `take()`'s
    budget break, and B08.04's `after` is a keyword argument that `take()` does not read, so the equality below holds by construction today;
    it fails only if a future `take()` reads `after` and so changes which candidate a Scene carries. Over every `pack_scenes` call of
    `build_realm(0)`'s two seasons, the Scenes (ids, verbs, payloads -- `effort` included -- and seats) equal those of the same call with
    `after` off. `hung >= 1` and `formed >= 1` show only that the comparison ran over a realm that formed both."""
    cnt = season_reading
    assert cnt.compared >= 1 and cnt.formed >= 1 and cnt.hung >= 1, (cnt.compared, cnt.formed, cnt.hung)
    assert not cnt.moved, f"{len(cnt.moved)} of {cnt.compared} calls differ beyond `after`; first: {cnt.moved[0]}"
    print(f"\nB08.04 reading: {cnt.compared} pack_scenes calls compared, {cnt.hung} hold an act with `after`, "
          f"{cnt.formed} efforts formed, 0 moved")
