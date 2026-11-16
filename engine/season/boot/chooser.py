"""`boot.chooser` -- the game's composition of its chooser (`04` §A.2's `boot/` row).

`make_chooser` over a world's fixtures, the act-id mint, and the per-candidate draw. It imports
nothing from `harness/`; `harness/probes.py` imports it for the instruments that play a season on
the shipped policy.
"""

from __future__ import annotations

from ..decision import make_chooser
from ..state.ids import H, draw_factory


def chooser(w, only=None, verbs=None, draw_seed=None):
    """§F2's default policy, built the way the barrier builds it -- the composition of
    `make_chooser` over a world (act-id mint, `verbs`, the per-candidate draw) that every instrument
    which plays a season on the shipped policy calls: `populated`, `soak` and `storybar` through
    here. `interactions` alone still composes it by hand, because its `run` reads `mint` and `draw`
    again below the composition (`CH.sample_order(..., draw)`, `mint(p.id, ...)`,
    `attribute_top(..., draw, ...)`), so it needs the parts and not only the chooser. `only`
    narrows to one person so a probe can watch a single decision; `verbs` narrows the option set to
    the ones under test; `draw_seed`, when given, replaces `w.world_seed` as the seed of the
    CHOOSER'S `draw_factory` and of nothing else (the act-id mint keeps `w.world_seed`) -- the
    `--draw-seeds` arm's seam (`storybar.draw_seed_arm`).

    ⚠ IT DOES NOT TAKE A ROSTER, and it cannot: `opening_set` computes from the verb table now.
    A probe that wants a verb in the set must put the verb in `verb_table.yaml`."""
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    inner = make_chooser(w.fixtures, mint, verbs=verbs,
                         draw=draw_factory(w.world_seed if draw_seed is None else draw_seed,
                                           lambda: w.tick))
    def choose(p, v, s, ask_budget):
        return inner(p, v, s, ask_budget) if (only is None or p.id == only) else []
    return choose
