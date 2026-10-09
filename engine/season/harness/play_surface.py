"""THE PLAY SURFACE'S DISPATCH SEAM — a `choose` that hands named persons to a callback and everyone
else to the chooser the caller already built. v9 PC-06 `S-1`.

    from engine.season.harness.play_surface import dispatching_chooser
    choose = dispatching_chooser(make_chooser(fx, mint, verbs, draw), {"p_carin": my_callback})
    driver.season(choose, None, subsistence, contest_max_depth=...)

**This is the whole single-player hook, and it edits no engine file.** `SeasonDriver.season` already
RECEIVES its chooser (`loop/driver.py`, `season(self, choose, ...)`) and DELIBERATE calls it once per
person as `choose(p, v, s, ask_budget)` (`loop/deliberate.py`). So a client that wants to decide for
one person needs no engine change: it passes a `choose` that dispatches on `p.id`. That is all this
module is.

⚠ **THE CALLBACK SEES WHAT `choose` SEES AND NOTHING MORE.** It is called as
`callback(p, v, s, ask_budget, auto)`: the same four person-side arguments DELIBERATE passes (a
`Person`, a `View`, a `Sensation`, the budget QUERY), plus `auto`, the delegate chooser itself. No
`World` reaches it, so a client built on this seam is held to the same boundary `make_chooser` is
(`test_choose_receives_no_world` pins the four-argument call). `auto` is passed so a client can show
or replay what the shipped policy would have done; calling it is the caller's choice.

⚠ **THE SEAM ADDS NO RULE.** It does not validate what the callback returns: DELIBERATE already
refuses a return over the person's budget (S26.3), a scene over the interaction bound, and an Act
whose actor is not the person deciding (L1). Re-checking here would be a second owner of those
rules. Nor does it build the delegate: the caller constructs `auto` exactly as it would have passed
it to `season` (`headless.run`, `populated.run`), so with no overrides the run is the shipped run.

The control (`test_play_surface_dispatch.py`): a callback that returns `auto`'s own pick leaves
`World.content_hash()` equal to the plain run on the same seed; a planted deviation for one person
moves it.
"""
from __future__ import annotations

from typing import Any, Callable, Mapping

# `(p, v, s, ask_budget) -> list[Act | Scene]` — DELIBERATE's call, the delegate's shape.
Chooser = Callable[..., list]
# `(p, v, s, ask_budget, auto) -> list[Act | Scene]` — the same four arguments, plus the delegate.
Callback = Callable[..., list]


def dispatching_chooser(auto: Chooser, overrides: Mapping[str, Callback]) -> Chooser:
    """A `choose(p, v, s, ask_budget)` for `SeasonDriver.season`: person ids in `overrides` go to
    their callback as `callback(p, v, s, ask_budget, auto)`; every other person goes to `auto`.

    `overrides` is read at each call, not copied, so a client may add or remove a person between
    seasons. With an empty mapping the returned chooser is `auto` behind one dictionary lookup."""
    def choose(p: Any, v: Any, s: Any, ask_budget: Callable[[], int]) -> list:
        cb = overrides.get(p.id)
        if cb is None:
            return auto(p, v, s, ask_budget)
        return cb(p, v, s, ask_budget, auto)
    return choose
