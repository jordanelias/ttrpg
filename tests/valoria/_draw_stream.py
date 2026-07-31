"""[W8d] Single owner of the personal-combat RNG DRAW-STREAM instrument.

WHY THIS MODULE EXISTS — the measuring device, not the thing measured.

`combat_completion_plan_v4.md` §4 W8d: every acceptance criterion in that plan rests on a
PAIRED-SEED comparison ("same seeds, ablate the term, measure the delta"), and nobody had ever
audited whether `wrapper.engagement`'s RNG stream supports that inference. It does not, in general.
The engagement loop takes `rng` as a parameter and consumes it through ~30 call sites whose
*order and count depend on the inputs* — `wrapper.py:93` documents one such gate in its own comment
("represent_p==1.0 (none/light) draws NO rng — the gate is inert on the stream off-plate"). So a
change that adds, removes, or re-orders a single draw re-shuffles every subsequent draw, and
`fight(seed=N)` before the change and `fight(seed=N)` after it are **different random experiments
wearing the same seed**.

This is the §0.1 hazard verbatim: an adversarial pass that attacks a result's *statistics* while
never attacking its *setup*. The two arms were never the same experiment.

WHAT LIVES HERE, AND WHY ONLY HERE (CLAUDE.md §8 — every rule lives once):

  · `static_draw_sites()`  — AST inventory of every `rng.<method>(...)` call site in the engine.
    DETERMINISTIC and reachability-independent, so it catches a new draw site even on a branch no
    sweep exercises. This is the recurrence guard.
  · `RecordingRandom`      — a `random.Random` subclass that records the ordered ENGINE-LEVEL draw
    sites actually consumed, and separately counts underlying `random()` consumption.
  · `underlying_random_calls()` / `engine_draw_sites()` — the two projections guards assert on.

Any future batch that wants to claim "ablated at K=0 reproduces the prior engine" pins
`RecordingRandom(...).trace` before its change and asserts equality after. That is what makes the
plan's §3.6 criterion ("assert the ablated run is stream-identical") *checkable* rather than
aspirational, and it is the reason this is a shared owner and not a local fixture.

TWO MEASURED FACTS THIS MODULE EXISTS TO KEEP TRUE (both verified 2026-07-30, `8535cea`):

 1. **Draw count is input-conditional, strongly.** One fixed seed, longsword vs arming: 57
    underlying `random()` draws at `armour='none'` and **168 at `'heavy'`** — 2.9x. Seed parity
    across armour contexts is not experimental control.
 2. **`random.Random.gauss` carries a parity latch.** It caches the second Box-Muller variate in
    `self.gauss_next`, so k `gauss` calls consume `2*ceil(k/2)` underlying draws — 2 on odd calls,
    0 on even. `core.resolve` -> `sigma_leverage.roll_net_continuous` -> `dice_engine` calls `gauss`
    on the SAME object the engine draws `random()` from, so the bare-`random()` sub-stream is
    shifted by 0 or 2 depending on how many resolutions happened first. The interleaving is
    non-uniform, which is why "off by a constant number of draws" is not a usable correction.

NOT A BEHAVIOUR CHANGE. This module is test-side only: `wrapper.fight(A, B, cfg, rng)` already
accepts the RNG as a parameter, so nothing in the engine is touched, no golden can move, and the
instrument cannot perturb what it measures beyond the draws the engine itself requests.
"""
import ast
import os
import random
import sys

# The complete set of `random.Random` methods the engine calls. Verified exhaustive by grep over the
# engine package (`rng.<method>(`): random, randrange, uniform, betavariate — plus `gauss`, which the
# engine reaches indirectly through core.resolve -> sigma_leverage.roll_net_continuous -> dice_engine.
# A method absent from this tuple is invisible to the recorder, so `test_draw_site_inventory_is_pinned`
# cross-checks the STATIC scan (which needs no such list) against the dynamic trace.
RNG_METHODS = ('random', 'randrange', 'uniform', 'betavariate', 'gauss')

_ENGINE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'systems', 'combat', 'combat_engine_v1')
_DICE_ENGINE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'engine', 'autoload', 'dice_engine.py')


# ---------------------------------------------------------------------------
# static inventory — deterministic, reachability-independent
# ---------------------------------------------------------------------------
def static_draw_sites(paths=None):
    """Every `rng.<method>(...)` call site in the engine, as a sorted list of
    (basename, lineno, method).

    AST-based rather than regex-based so a mention inside a comment or string cannot register as a
    draw (`vocabulary.py:67` names `rng.randrange(3)` in prose — a regex counts it, this does not).

    Reachability-independent BY DESIGN. The dynamic sweep reaches `wrapper.py:363`/`:367` only 3 and
    1 times in 256 fights, so a dynamic-only pin would be one tuning change away from missing a new
    draw on a cold branch. A static count cannot miss it."""
    if paths is None:
        paths = [os.path.join(_ENGINE_DIR, f)
                 for f in sorted(os.listdir(_ENGINE_DIR)) if f.endswith('.py')]
        paths.append(_DICE_ENGINE)
    found = []
    for p in paths:
        if not os.path.exists(p):
            continue
        try:
            tree = ast.parse(open(p, encoding='utf-8').read(), filename=p)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            if (isinstance(fn, ast.Attribute) and fn.attr in RNG_METHODS
                    and isinstance(fn.value, ast.Name) and fn.value.id == 'rng'):
                found.append((os.path.basename(p), node.lineno, fn.attr))
    return sorted(found)


def static_site_shape(paths=None):
    """The static inventory projected to {(module, method): number_of_distinct_lines}.

    This is the form guards assert on: it is INVARIANT to edits that move a draw up or down a file
    (the thing that would make a line-number pin flake) and STRICTLY SENSITIVE to adding or removing
    one (the thing the guard is for)."""
    shape = {}
    for mod, _line, method in static_draw_sites(paths):
        shape[(mod, method)] = shape.get((mod, method), 0) + 1
    return shape


# ---------------------------------------------------------------------------
# dynamic recorder
# ---------------------------------------------------------------------------
_THIS_FILE = os.path.basename(__file__)


class RecordingRandom(random.Random):
    """`random.Random` that records the ordered ENGINE-LEVEL draw sites it is asked for.

    Two counters, deliberately distinct — conflating them is what made the first version of this
    instrument report 31 sites, one of which was the instrument itself:

      · `trace`      — one entry per draw the ENGINE requested, as (module, lineno, method). Nested
                       draws that a stdlib method makes internally (`gauss` calling `random()`,
                       `betavariate` calling `gammavariate`) are NOT separate entries; they belong to
                       the outer engine site. Enforced by `_depth`, not by frame heuristics.
      · `underlying` — every `random()` consumed, including those nested calls. This is the quantity
                       that determines whether two runs are the same experiment.

    Subclassing (rather than wrapping) is required: `dice_engine` calls `rng.gauss(...)`, and
    `random.Random.gauss` calls `self.random()` — only a subclass sees that inner call."""

    def __init__(self, seed):
        super().__init__(seed)
        self.trace = []
        self.underlying = 0
        self._depth = 0

    def _site(self):
        """The engine frame that asked for this draw.

        Offset 2 is exact, not tuned: frame 0 is the generated wrapper, frame 1 is `_site`'s own
        caller inside it, frame 2 is the engine line. The while-loop is a belt-and-braces skip for
        stdlib/self frames, and an earlier revision of this instrument mis-set the offset to 3 —
        which silently attributed 6,470 draws to a single wrapper line. Hence the cross-check against
        the static scan; an off-by-one here is not visibly wrong on its own."""
        f = sys._getframe(2)
        while f is not None and os.path.basename(f.f_code.co_filename) in ('random.py', _THIS_FILE):
            f = f.f_back
        return (os.path.basename(f.f_code.co_filename), f.f_lineno) if f is not None else ('?', 0)


def _make_recorder(method_name):
    base = getattr(random.Random, method_name)

    def wrapped(self, *args, **kwargs):
        if method_name == 'random':
            self.underlying += 1
        if self._depth == 0:
            self.trace.append(self._site() + (method_name,))
        self._depth += 1
        try:
            return base(self, *args, **kwargs)
        finally:
            self._depth -= 1
    wrapped.__name__ = method_name
    return wrapped


for _m in RNG_METHODS:
    setattr(RecordingRandom, _m, _make_recorder(_m))
del _m


# ---------------------------------------------------------------------------
# projections
# ---------------------------------------------------------------------------
def engine_draw_sites(rec):
    """The DISTINCT (module, lineno, method) sites a recorded run touched."""
    return set(rec.trace)


def dynamic_site_shape(rec_or_traces):
    """{(module, method): distinct_lines} for one recorder or an iterable of traces — the dynamic
    counterpart of `static_site_shape`, so the two can be compared directly."""
    traces = ([rec_or_traces.trace] if hasattr(rec_or_traces, 'trace')
              else list(rec_or_traces))
    seen = set()
    for t in traces:
        seen.update(t)
    shape = {}
    for mod, _line, method in seen:
        shape[(mod, method)] = shape.get((mod, method), 0) + 1
    return shape


def underlying_random_calls(rec):
    """Total `random()` consumption, nested calls included. Two runs with different values here are
    NOT a paired-seed comparison, whatever their seeds."""
    return rec.underlying
