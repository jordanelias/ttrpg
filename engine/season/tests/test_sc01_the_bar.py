"""v9 SC-01 STEP 16 -- THE BAR, M2's first gate, RE-PINNED ON THE SHIPPED HEARING (B24.16; `U5c_SC_proceedings_residue.md` §2): *proceedings run with zero authored
acts, twice, byte-identical including the hash*, *a verdict that can be lost*, and the closure test: *a planted `if arrangement.id == "tribunal"` in an effect must
redden it*.

THE WORLD IS `governance_spine.build_hearing(seed)` -- the world `harness/scenarios.py::SCENARIOS["hearing"]` plays -- at the fixtures it builds itself (`DEFAULT_FIXTURES`
with its own two arms, `sitting_exchanges` 1 and the proceeding role as the NPC attendees' decider; the shipped realm keeps its control, so the entry's "`DEFAULT_FIXTURES`"
is the world's own fixtures and not the bare ones). It replaces the world this file used to find by sweeping 1,815 runs of a three-person `tiny_world` at a judge pool of 60
(`BAR_FIXTURES`, off the declared sweep and global to every contested verb), whose proceedings the file re-traced a dozen times as the act mix moved. The hearing's sitting is
opened by the game's own acts at build (a Mayor `convene`s, CALENDAR fires the Date, the Mayor `open_case`s the accused: `premise` below), and every act of the run is the real
chooser's (`probes.chooser`, `harness/populated.py::run`'s), through the real `SeasonDriver.season`; the test injects no Act, calls no `resolve`.

WHAT LEAVES THIS FILE: the claim that a determination's `causes[]` walk back to the `date.fired` that raised it. It held on the swept world only (the hearing's Date fires at
build and no determination's causes reach it, read at 40 seeds); `test_sc01_fired_slot.py` (the walk at its `done`/`fired` pair) owns it.

THE FALSIFIERS, each seen red before it was trusted:
  * AN INJECTED ACT REDDENS THE BAR (kept below): a chooser wrapper replacing the first act of the accuser's first scene with a hand-written Act -- `_zero_authored` names it.
  * A VERDICT THAT CANNOT BE LOST REDDENS THE BAR (run once, not kept): `sigma._resolve_proceeding`'s returned net pinned a whole success over the obstacle, so every sitting
    is `Success` -- `test_a_verdict_can_be_lost_on_the_shipped_hearing` fails on the lost arm (no `matter.undetermined` at any of the 40 seeds).
  * THE CLOSURE TEST: the planted `if arrangement.id == "tribunal":` written into the real `_eff_determine` reddened both closure tests (kept as a test over the real effect's
    own source).
No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit).
"""

from __future__ import annotations

import ast
import inspect
import textwrap
from pathlib import Path

import pytest

from ..data import files
from ..data.arrangements import ARRANGEMENTS
from ..harness import probes as P
from ..harness.governance_spine import ACCUSED, ACCUSER, ACCUSER_SEAT, build_hearing
from ..harness.scenarios import HEARING_VERBS
from ..loop import effects_information
from ..loop.driver import SeasonDriver
from ..queries import world_q
from ..state.carriers import Act
from ._closure_scan import branches_on_ids, game_code

# THE KIND THE LOST ARM READS: `verb_table.yaml: determine` emits `matter.undetermined` at the Failure band -- the bench heard the matter and did not dispose of it, nothing opens.
# [ASSUMPTION: `matter.dismissed` is B27's (`05_SC_acquittal`), not emitted by the tree today -- basis: no `emits` row of `verb_table.yaml` names it; B27 re-points `LOST` here.]
BOUND, LOST = "matter.determined", "matter.undetermined"
SEEDS = range(40)


def _hearing(seed: int, wrap=None):
    """`build_hearing(seed)` and ONE season (the sitting is due at its tick) through the real chooser. Returns `(world, chosen)`: `chosen` holds every Act OBJECT the
    chooser returned -- an observation, it decides nothing. Objects, not ids: the driver re-derives a re-deliberated act's id with its round (`loop/deliberate.py`, `:r<n>`).
    `wrap` is the mutation hook a falsifier uses (a wrapper OUTSIDE the recorder, as an injection would be); THE BAR passes none."""
    w = build_hearing(seed)
    real = P.chooser(w, verbs=HEARING_VERBS)
    chosen: list = []

    def choose(p, v, s, ask_budget):
        scenes = real(p, v, s, ask_budget)
        chosen.extend(a for sc in scenes for a in sc.acts)
        return scenes
    if wrap is not None:
        choose = wrap(choose)
    premise = {a.id for a in w.acts}                      # what the build folded: the sitting's opening, made by the game's own acts
    SeasonDriver(w).season(choose, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, chosen, premise


def _zero_authored(w, chosen: list, premise: set) -> None:
    """Every act that reached RESOLVE in the run is an object the chooser returned: none was injected. Read off `w.acts`, the store every act entering RESOLVE is recorded
    in -- not `SeasonDriver.resolved`, which a contested act refused at admission (e.g. `speech.unheard`) never enters. The build's own acts (`premise`) are the opening."""
    ours = {id(a) for a in chosen}          # `chosen` keeps every object alive, so no id is reused
    run = [a for a in w.acts if a.id not in premise]
    assert run, "the run resolved no act at all"
    authored = [(a.id, a.actor, a.verb) for a in run if id(a) not in ours]
    assert not authored, f"acts the chooser did not return reached RESOLVE (authored): {authored}"


def _determinations(w) -> list:
    """The `determine` Events of the hearing's matter (the accused), whoever sat: `(kind, Event)`, off the log."""
    out = []
    for e in w.log:
        act = w.acts.get(e.causes[0]) if e.causes else None
        if e.kind in (BOUND, LOST) and act is not None and act.verb == "determine" and act.payload.get("subject") == ACCUSED:
            out.append(e)
    return out


def _bar(worlds: list) -> None:
    """THE BAR ON THE SHIPPED HEARING: over the worlds, a determination binds at some seed and is lost at some seed, and every binding one carries its terms."""
    assert len(worlds) == 40, len(worlds)                 # it checked 40 worlds (`CLAUDE.md` §0.1 pt 2): a run that built fewer asserts nothing
    kinds, termed, bound = set(), 0, 0
    for w in worlds:
        edges = {t.id: t for t in w.tenures}
        for e in _determinations(w):
            kinds.add(e.kind)
            if e.kind != BOUND:
                continue
            bound += 1
            # THE DETERMINING EVENT CARRIES ITS TERMS: the sitting it was graded by (`ending` holds the arrangement and a verdict) and the edge it opened on the accused,
            # graded the Event's own band, with the term the disposal runs for. (`terms` is no key of a proceeding's `ending`: `queries/inputs.py::UNWRITTEN` keeps the
            # roll's `terms` out of it, and a margin provider's `((key, value), ...)` ending is another shape.)
            assert world_q.ending_arrangement(e) is not None and world_q.ending_verdicts(e), e.ending
            opened = [edges[r.subject] for r in e.changes if r.subject in edges]
            termed += any(t.subject == ACCUSED and t.degree == e.degree and t.term is not None for t in opened)
    assert bound > 0 and termed == bound, (bound, termed)
    assert kinds == {BOUND, LOST}, f"a verdict that cannot be lost: the hearing's determinations, over 40 seeds, were only {sorted(kinds)}"


# ======================================================================================
# THE BAR
# ======================================================================================

def test_a_verdict_can_be_lost_on_the_shipped_hearing():
    """THE BAR's re-pin (B24.16, `U5c_SC_proceedings_residue.md` §2): `build_hearing(seed)`, seeds 0 to 39, one season each. `matter.determined` and the lost arm
    (`LOST`, read where B27's `matter.dismissed` will be) each occur at some seed, and the determining Event carries its terms. THE INSTRUMENT SEES A VERDICT THAT CANNOT
    BE LOST: with the roll pinned to Success `_bar` fails on the lost arm (run once at the build, not kept)."""
    _bar([_hearing(seed)[0] for seed in SEEDS])


@pytest.mark.parametrize("seed", [1, 4])
def test_the_hearing_with_zero_authored_acts_runs_twice_byte_identical(seed):
    """Two runs of the same seeded hearing, every act the chooser's, hash the same (seeds 1 and 4 are the two whose sitting binds, so the run reaches an edge)."""
    hashes = []
    for _ in range(2):
        w, chosen, premise = _hearing(seed)
        _zero_authored(w, chosen, premise)
        assert any(e.kind == BOUND for e in _determinations(w)), "the run did not reach a determination that binds"
        hashes.append(w.content_hash())
    assert hashes[0] == hashes[1], f"hearing/{seed}: the same seeded run hashed differently on its second run"


@pytest.mark.parametrize("verb", ["open_case", "speak"])
def test_an_injected_act_reddens_the_bar(verb):
    """THE BAR's first falsifier, kept: a wrapper OUTSIDE the recorder replaces the first act of the accuser's first scene with a hand-written act, and `_zero_authored`
    names it. `speak` is the act a `SeasonDriver.resolved` reading missed: refused at admission it never enters `resolved`, but it is in `w.acts`."""
    injected = []

    def wrap(choose):
        def inject(p, v, s, ask_budget):
            scenes = choose(p, v, s, ask_budget)
            if p.id == ACCUSER and not injected and scenes and scenes[0].acts:
                a = Act("authored_oc", ACCUSER, verb, via=ACCUSER_SEAT, payload={"subject": ACCUSED})
                scenes[0].acts[0] = a
                injected.append(a)
            return scenes
        return inject
    w, chosen, premise = _hearing(1, wrap=wrap)
    assert injected and injected[0].id in w.acts, "the injection never reached RESOLVE"
    with pytest.raises(AssertionError, match="authored_oc"):
        _zero_authored(w, chosen, premise)


# ======================================================================================
# THE CLOSURE TEST -- NO GAME CODE COMPARES AGAINST A LITERAL ARRANGEMENT ID (scripting drift)
# ======================================================================================
# Moved here from `test_sc01_provider.py` (steps 13+15 wrote it as a first form and named step 16
# its owner). A STATIC scan, and that is the narrowest instrument that can see the plant: a computed
# `open_case` docks every matter under arrangement `None` (`_eff_open_case`), so no seeded run -- THE
# BAR's included -- reaches an effect with `tribunal` in hand, and a behavioural test would pass over
# a planted branch it never executes. It reads comparisons and `match` cases against an
# `arrangements.yaml` id; a lookup keyed by one (`ARRANGEMENTS["tribunal"]`) is not a branch and is not
# read.

# v9 FI-03: the walk and the scope live once, in `_closure_scan.py`; FI-03's entity-id closure calls them.

def _branches_on_an_arrangement_id(tree: ast.AST) -> list:
    """`(line, id)` for every comparison or `match` case whose operand is an arrangement id."""
    # B24p.03: the row `audience` shares its id with the `requires` stem `audience` (`world_q`'s `stem == "audience"`: may an actor enter a rung),
    # a grammar word and no arrangement; a comparison against it is read as the stem. Every other row id is scanned as before.
    from ..data.requires import REQUIRES_STEMS
    return branches_on_ids(tree, set(ARRANGEMENTS) - set(REQUIRES_STEMS))


def test_no_game_code_branches_on_an_arrangement_id():
    """THE PLAN'S SCRIPTING-DRIFT FALSIFIER: no game code special-cases one arrangement by its id.

    SCOPE, EXACTLY: every `.py` under `engine/season/` outside `engine/season/tests/` (the harness
    included), plus every `.py` under `modules/`. In each, an `ast.Compare` or a `match` value case is
    reported when an operand is a string LITERAL (or a tuple, list or set of them) equal to an
    `arrangements.yaml` row id. NOT SCANNED: `engine/` outside `season/`, and any other tree. NOT SEEN:
    an id reached without a literal comparison (a dict keyed by the id, `.get("<id>")`, a named
    constant, an id built at runtime). The floor (`>= 100` files) and the effects-module membership
    assert that the sweep read the package; `test_the_planted_tribunal_branch_in_the_real_effect_is_found`
    is the scan's own falsifier."""
    assert "tribunal" in ARRANGEMENTS, sorted(ARRANGEMENTS)
    paths = game_code()
    assert len(paths) >= 100, len(paths)               # the sweep read the package, not an empty glob
    assert Path(effects_information.__file__).resolve() in {f.resolve() for f in paths}, (
        "the effects module the plant goes in is not scanned")
    found = {str(f.relative_to(files.REPO_ROOT)): h for f in paths
             if (h := _branches_on_an_arrangement_id(ast.parse(f.read_text(encoding="utf-8"))))}
    assert not found, f"game code branches on an arrangement id (scripting drift): {found}"


def test_the_planted_tribunal_branch_in_the_real_effect_is_found():
    """The scan's own falsifier, on the real effect: `_eff_determine`'s own source, scanned clean, then
    with the plan's planted line as its first statement after the docstring, reported."""
    tree = ast.parse(textwrap.dedent(inspect.getsource(effects_information._eff_determine)))
    fn = tree.body[0]
    assert isinstance(fn, ast.FunctionDef) and fn.name == "_eff_determine", ast.dump(fn)[:80]
    assert _branches_on_an_arrangement_id(tree) == []
    plant = ast.parse('if arrangement.id == "tribunal":\n    return []\n').body[0]
    fn.body.insert(1, plant)
    assert [v for _, v in _branches_on_an_arrangement_id(tree)] == ["tribunal"]
