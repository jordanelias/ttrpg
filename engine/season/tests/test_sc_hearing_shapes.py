"""B24.32 -- the run's shape (KERN_B check 10): `harness/governance_spine.py::run_shape`, a reader of `Outcome.beats` in the harness.

The kernel's `narrative.py` named a bout's arc; the hearing carries four of them, computed from the beats a sitting returned and stored nowhere: `rout`, `reversal`,
`collapse` and `split`. The lean it reads is `Beat.mood`, the room's lean toward `for` after each exchange."""
from __future__ import annotations

from dataclasses import replace

from ..harness.governance_spine import PLAIN, ROUT_MARGIN, RUN_SHAPES, run_shape
from .test_sc_proceeding_host import _beat
from .test_sc_proceeding_module import P, _carried, _inp, _key, _p, _rite


def _run(moods, fault=None, at=-1):
    """a hand-built exchange list: one beat a lean, the beat at `at` recording `fault` where given."""
    beats = [_beat(n + 1, "a" if n % 2 == 0 else "b", "for" if n % 2 == 0 else "against", m) for n, m in enumerate(moods)]
    if fault is not None:
        beats[at] = replace(beats[at], fault=fault)
    return tuple(beats)


def test_four_run_shapes_from_hand_built_exchange_lists():
    """Each of the four shapes is produced by a hand-built exchange list, and each has a neighbouring list that is NOT that shape, the rule broken in one place (so the shape
    is the list's, not a constant): a ROUT, the room leaning `for` throughout and past `ROUT_MARGIN` at the end, never behind; a REVERSAL, the winner crossing from behind to
    ahead in the back half; a COLLAPSE, the last exchange recording a fault; a SPLIT, the close carrying the side the room did not end leaning to."""
    assert 0.0 < ROUT_MARGIN < 1.0 and set(RUN_SHAPES) == {"rout", "reversal", "collapse", "split"}
    rising, crossing = [0.1, 0.25, 0.4, 0.55], [-0.3, -0.2, 0.1, 0.35]
    cases = [
        (_run(rising), None, "rout"),
        (_run(rising), True, "rout"),                                   # the close carried the side the room leans to: no split
        (_run(crossing), True, "reversal"),
        (_run(crossing), None, "reversal"),                             # the winner read from the room where no close is given
        (_run([0.1, 0.2, 0.5], fault="silence"), True, "collapse"),      # a rout but for the fault its last exchange recorded
        (_run([0.1, 0.2, 0.5], fault="silence"), False, "collapse"),     # a fault ends it whoever the close carried
        (_run(rising), False, "split"),                                 # the room ends leaning `for` and the close carried `against`
        (_run([-0.55, -0.4, -0.25, -0.1]), True, "split"),               # and the other way about
        # the neighbours, each the shape's own rule broken in one place
        (_run([-0.3, 0.2, 0.3, 0.4]), True, PLAIN),                      # crossed in the front half: not a reversal; he trailed: not a rout
        (_run([0.05, 0.1, 0.2, 0.3]), True, PLAIN),                      # never behind but not past the margin: not a rout
        (_run([0.1, -0.1, 0.2, 0.5]), True, "reversal"),                 # control for the line above: trailed, then crossed at the half: a reversal, not a rout
        (_run([0.1, 0.2, 0.5], fault="irrelevance", at=0), True, "rout"),   # a fault earlier in the run does not end it
        ((), None, PLAIN),
        (_run([0.2, 0.0]), None, PLAIN),                                # the room ends level and nobody carried
    ]
    checked = 0
    for beats, carried, want in cases:
        assert run_shape(beats, carried) == want, (want, [b.mood for b in beats], carried)
        checked += 1
    assert checked == len(cases) == 14
    assert {want for _, _, want in cases} >= set(RUN_SHAPES)            # all four are reached
    assert run_shape(list(_run(rising))) == "rout"                      # any sequence of beats is read, a list as a tuple


def test_a_run_of_the_module_has_one_shape_and_the_shapes_occur():
    """The reader on `Outcome.beats` of the module's own sitting (two parties and one bench, three turns, the automatic policy): over 200 seeds each run reads as one of the five
    names and, with the close's own ruling beside it, a rout, a reversal and a split each occur (a reader that never saw one would be no reader). Nothing is stored."""
    seen, checked = {}, 0
    for i in range(200):
        inp = _inp([_p("a", "for", reason=5.0 + (i % 3)), _p("b", "against", reason=5.0 + (i % 2)), _p("j0", decides=True, precedence=1)],
                   _rite(close="bench", turns=3, silence="refusal"))
        out = P.proceed(inp, _key("shape", i))
        shape = run_shape(out.beats, _carried(inp, out))
        assert shape in (*RUN_SHAPES, PLAIN) and shape == run_shape(out.beats, _carried(inp, out)), shape
        seen[shape] = seen.get(shape, 0) + 1
        checked += 1
    assert checked >= 200
    assert {"rout", "reversal", "split"} <= set(seen), seen
