"""v9 SC-01 STEP 16 -- THE BAR, M2's first gate (`workplans/valoria_master_workplan_v9_part6.md` §SC-01,
the CARRIED *Step 16* bullet and the entry's FALSIFIER): *two seeded proceedings run end to end with
zero authored acts, twice, byte-identical including the hash, and `causes[]` walks from the
determination back to the date that raised it* -- and the closure test: *a planted
`if arrangement.id == "tribunal"` in an effect must redden it*.

WHAT A PROCEEDING IS HERE, every act chosen by the real chooser (`decision.make_chooser`, built as
`harness/populated.py::run` builds it) through the real `SeasonDriver.season`; the test injects no Act,
calls no `resolve`, and only builds the world and turns the seasons:
  convene (the Duke, via his seat, at a place) -> `date.scheduled` -> next season CALENDAR fires it
  (`date.fired`, `docket.formed`: an empty slot, the date being held) -> WITNESS deposits the firing in
  the Duke's ledger -> `open_case` on the clerk fills the slot -> the sitting question
  (`world_q.questions_for`'s `q:sitting:<date>:<matters>`) -> `determine` -> `matter.determined`, whose
  `causes[]` reach the `date.fired` Event of the Date whose slot held the matter.

THE WORLD IS HAND-BUILT STATE ONLY (v9 §0.5): `probes.tiny_world` (`R` > `D` > `S` > `Hh`; the Duke
`p_high` holds `off_duke`, rung `D`, and stands in `S`; the clerk `p_mid` lives in `Hh`), plus two
pieces of character data, the kind the realm's builder authors for every person: one conviction
(`Person.pursuits`), and one ambition -- an OUGHT Proposition about the clerk the Duke `commit`s to
(`harness/populated.py`'s tie shape), so a standing `need` question about the clerk recurs every season
(`questions_for` Q4). No Date, docket item, claim or Act is planted.

⚠ THE TWO SEEDS ARE SELECTED, AND THE RATE IS MEASURED -- THE BAR IS AN EXISTENCE CLAIM, NOT A RATE.
MEASURED 2026-10-16 at eb9ba4e2 (a one-off sweep, not kept): this world at each of the 15 convictions x
seeds 0..15, ten seasons, 240 runs -- 72 `matter.determined`, and 4 of them walk to a `date.fired`
(doctrine 12, family 13, reputation 13, scholastics 6); this file first ran scholastics 6 and family 13;
the seeds it runs now are those of `PROCEEDINGS` below (re-traced at v10 REM-25 and at CR-16, which left no family proceeding). The other 68 are raised by the ambition (`need`, whose occasion is `[ROOT]`,
`world_q.occasioned_by`): the chooser docketed the clerk BEFORE any sitting fired, so `_eff_open_case`
appended a dateless item, `docketed` then declines every later `open_case` on him, no slot ever holds
him, and `determine`'s docket conjunct (existence of a DocketItem, dated or not) admits the
determination without a sitting. That ordering -- a matter docketed before a sitting is never called
to one, and a dateless item is determinable -- is the link that keeps the rate low; it is recorded at
`hole_register.yaml` H-163 with a prototype measurement, and lifting it is a design choice this step
does not take. Without the ambition (the Duke given only a firsthand claim that the clerk exists,
`test_u7_remit.py`'s plant; 15 convictions x seeds 0..5, five seasons) nobody is determined at all:
the Duke is asked about a person almost never, and a sitting's slot is filled by whatever he is asked
about when he next opens a case (a rung, a Record, the date's own id), on which `determine` refuses
on `party`.

THE FALSIFIERS, each seen red before it was trusted (2026-10-16, mutations run and reverted):
  * AN INJECTED ACT REDDENS THE BAR: a chooser wrapper replacing the first act of the Duke's first
    scene with a hand-written `open_case` Act -- `_zero_authored` fails naming `authored_oc` (kept
    as `test_an_injected_act_reddens_the_bar`).
  * A DIFFERENT RNG ON THE SECOND RUN REDDENS THE BAR: the chooser's draw stream seeded one higher
    on run two of family/13 (world and world seed unchanged) -- hashes f0aa1e93 vs e4cc794a.
  * A BROKEN CAUSE LINK REDDENS THE BAR: the sitting question built with `about=None` in
    `world_q.questions_for` -- scholastics/6 *no determination's causes reach a date.fired (1
    determined, 1 fired)*.
  * THE CONTROL beside them, kept as a test (virtue, seed 2 since v10 CP-T05-04; doctrine/8 until it; community/13 until SC-03b): a held date fires and, after it,
    the Duke determines the clerk out of his ambition -- the walk is False there, so THE BAR's walk is
    not satisfied by a firing merely preceding a determination.
  * THE CLOSURE TEST: the planted `if arrangement.id == "tribunal":` written into the real
    `_eff_determine` (`loop/effects_information.py`) reddened both closure tests (the package scan
    reports the line; the real effect no longer scans clean); the same plant is kept as a test over
    the real effect's own source.
No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit).

v9 SC-03b (RE-RECORDED): `determine` is a CONTESTED act now, rolled by the Duke's `pool_default` against the
clerk's obstacle, so at the shipped judge (pool 2, obstacle 2) most determinations are `Failure`
(`matter.undetermined`, nothing opens). MEASURED 2026-10-17, this world at each of the 15 convictions x
seeds 0..23, ten seasons, shipped fixtures: 360 runs, ONE proceeding walks (scholastics/6) -- family/13
drew `Failure` in its fifth season (counts from a one-off sweep, not kept). So the bar runs a STRONG JUDGE
(`BAR_FIXTURES`: `pool_default` 30), at which the same 15 x seeds 0..15 sweep gives three (family/13,
reputation/13, scholastics/6), and the two seeds and season counts of this file are unchanged. ⚠ 30 IS OFF
THE SWEEP: `H-126` declares `[1, 2, 4]` and `Fixtures.sweep` does not check the value, so this is a fixture
chosen to make the finding open, not a declared arm; at the declared top arm (4) family/13 draws `Failure`
(read 2026-10-17). It is GLOBAL: every contested verb without a `verb_capability` row falls to
`pool_default`, so `speak` and `tell` roll at 30 here too, and a saturated roll hides the contest's draw
stream from the twice-identical-hash check. The bar's claim is an EXISTENCE claim (the chain can close
from a conviction by choices alone), which the strong judge removes the lottery from; the three falsifiers
above were seen at SC-01's shipped fixtures and are not re-run at 30.
The `Failure` band and the shipped judge are observed in `test_u7_remit.py` (section 10), not here.

v9 FI-01 (RE-TRACED 2026-10-17, NOT RE-PINNED): `research`, `examine` and `surveil` are graded through
`sigma.faculty` too, so at `BAR_FIXTURES` every graded inquiry these runs reach draws `Overwhelming`
(scholastics/6: 3 `surveil`; family/13: 4 `surveil`, 1 `research`; doctrine/8: 2 `surveil`), and the
skip arm deposits nothing for `finding.none` (15 / 11 / 19 `finding.none` claims held at the base, 0
now). Each run's hash moved (213c3aca... -> faf13c18..., 7e3578b5... -> 07ed5a02..., b1a4c665... ->
74bcb320..., read off a one-off trace, not kept), and both proceedings still walk to their `date.fired`
in the same season counts while the control still does not, so the two seeds, the season counts and the
control are unchanged. The saturation hides the inquiries' draw stream from the twice-identical check,
as it does `speak`'s and `tell`'s.
"""

from __future__ import annotations

import ast
import inspect
import textwrap
from pathlib import Path

import pytest

from ..data import files
from ..data.arrangements import ARRANGEMENTS
from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..harness.corpus_run import attribute
from ..loop import effects_information
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.carriers import Act, Proposition, Tenure
from ._closure_scan import branches_on_ids, game_code
from .test_sc01_fired_slot import _walks_to

DUKE, SEAT, PARTY, WANT = "p_high", "off_duke", "p_mid", "prop_bar_duke_want"

# (conviction, world seed, seasons): the two seeded proceedings, and the control run. The season count
# is the first season after which the determination stands (traced at build), so each run is no longer
# than its proceeding.
# v10 REM-25 (B10-05): RE-TRACED, scholastics/6 -> scholastics/16, the conviction and season count unchanged --
# `carry`, `found` and `build` declare `referent_class: Record`, so they form only on a Record the person holds
# (the Duke and the clerk hold none here), and the act mix of this world moved: scholastics/6 now fires TWO dates
# and determines one matter whose causes reach neither (`_proceeding`: "no determination's causes reach a
# date.fired (1 determined, 2 fired)"). The bar is an existence claim on SELECTED seeds (above), not a rate. A sweep
# of scholastics x seeds 0..39 at 6 seasons for a run meeting every assertion of `_proceeding` finds seeds 13, 16 and
# 21 (scratch, not kept); 16 is taken, the first that is not family's seed. family/13/5 is unmoved (it meets them
# all). CONTROL, run: this file on the REM-24 tree (`f2381695`) meets them all at scholastics/6, so the move is this
# unit's.
# v10 CP-T05-04 (B10-05): RE-TRACED AGAIN, scholastics/16 -> scholastics/21, the conviction and season count unchanged --
# `open_case` declares `referent_class: Person` (and `argue` declares `Proposition`, and `docket_question` asks the
# witness of a docketing), so the Duke's `open_case` stops forming on the rungs and the Sites he is asked about, and the
# act mix of this world moved: scholastics/16/6 now fires ONE date and determines nobody (`_proceeding`: "no
# determination's causes reach a date.fired (0 determined, 1 fired)"). ATTRIBUTION, in-process on this tree (the same
# script on each arm): with neither column nor the docket question (the REM-25 behaviour) scholastics/16/6, family/13/5
# and the control all meet their assertions; the docket question alone moves none of the three (their hashes are the
# REM-25 tree's); the `open_case` column alone breaks scholastics/16/6 and the control (the `argue` column alone moves
# every hash and breaks neither); family/13/5 still meets every assertion with a moved hash. The bar is an existence
# claim on SELECTED seeds (above), not a rate. A sweep of scholastics x seeds 0..39 at 6 seasons for a run meeting every
# assertion of `_proceeding` finds seeds 13, 21 and 22 (scratch, not kept); 21 is taken, the first that is not family's
# seed.
# v10 CR-16 (B10-07b): RE-TRACED AGAIN, scholastics/21/6 and family/13/5 -> scholastics/13/6 and scholastics/33/6, the season
# count unchanged -- `Fixtures stance_polarity` ships `declared` (H-194), so the Duke's `determine` on the clerk is scored with the
# grudge's sign and the act mix of this world moved: scholastics/21/6 now fires ONE date and determines nobody and family/13/5
# determines nobody in three firings (`_proceeding`: "no determination's causes reach a date.fired"). The CONTROL test below
# (virtue/2) still meets its assertions. The bar is an existence claim on SELECTED seeds (above), not a rate. A sweep of
# scholastics x seeds 0..39 at 6 seasons for a run meeting every assertion of `_proceeding` finds seeds 13 and 33 (seed 39 raises
# in a different assertion); a sweep of family x seeds 0..39 at 5 seasons finds none, so both proceedings are scholastics' (scratch,
# not kept; the two worlds differ by seed, and the file's own distinct-hash assertion holds). ATTRIBUTION, in process on this tree:
# `stance_polarity` swept back to `legacy` on `BAR_FIXTURES` meets every assertion at scholastics/21/6 and family/13/5 again.
PROCEEDINGS = (("scholastics", 13, 6), ("scholastics", 33, 6))
BAR_FIXTURES = DEFAULT_FIXTURES.sweep("pool_default", 30)       # v9 SC-03b: a judge whose finding opens
# v9 IN-12 step 9: RE-TRACED, the conviction and season count unchanged -- `argue`/`sabotage`/`tend`/`train`
# are new members of the Duke's and the clerk's option sets, so doctrine/8's trajectory moved (it now fires
# TWO dates). A sweep of the 15 convictions x seeds 0..23 at 5 seasons for a run meeting every assertion of
# the control test below finds doctrine/22 first (scratch, not kept); the two PROCEEDINGS are unmoved.
# v9 IN-12 step 10: RE-TRACED AGAIN, the conviction and season count unchanged -- `conceal` is a new member
# of every option set (untyped, one Candidate per referent), and doctrine/22 now fires no date. A sweep of
# doctrine x seeds 0..399 at 5 seasons for a run meeting every assertion of the control test below finds
# doctrine/83 first (scratch, not kept; seeds 0..82 each fail one assertion); the PROCEEDINGS are unmoved.
# v10 REM-22 (B10-05): RE-TRACED AGAIN, the conviction and season count unchanged -- `restore`, `work` and `examine`
# declare `referent_class: Site`, so they stop forming on the clerk, the rungs and the Records the Duke is asked
# about, and the act mix of this world moved: doctrine/83 now fires TWO dates (the control's `f, = ...` needs
# one). A sweep of doctrine x seeds 0..8 at 5 seasons for a run meeting every assertion of the control test below
# finds doctrine/8 first (scratch, not kept; seeds 0..5 and 7 fire no date, seed 6 determines nobody); the
# PROCEEDINGS are unmoved. CONTROL, run: on the REM-21 tree doctrine/83 meets every assertion.
# v10 CP-T05-04 (B10-05): RE-TRACED AGAIN, THE CONVICTION MOVES TOO (doctrine -> virtue), the season count unchanged --
# `open_case` declares `referent_class: Person`, and the control's pattern (the Duke convenes and opens the clerk's case
# in one season, ONE date fires, he determines the clerk out of his ambition after it) no longer occurs in doctrine at any
# seed swept: doctrine x seeds 0..239 at 5 seasons finds no run meeting every assertion of the control test below (at
# seed 8 two dates fire, `f, = ...` raises; most seeds fire none). A sweep of all 15 convictions x seeds 0..24 at 5
# seasons finds justice/8, virtue/2, virtue/6 and virtue/15 (scratch, not kept); the lowest seed, virtue/2, is taken.
# CONTROL, run: on the REM-25 tree (the same script) doctrine/8 meets every assertion.
CONTROL = ("virtue", 2, 5)      # was ("community", 13, 5) until v9 SC-03b; ("doctrine", 8, 5) until IN-12 step 9; 22 until step 10; 83 until REM-22; 8 until CP-T05-04


def _world(conviction: str, seed: int):
    """`tiny_world` at `seed`, the Duke given one conviction and one ambition about the clerk."""
    w = P.tiny_world(BAR_FIXTURES)
    w.world_seed = seed
    w.persons[DUKE].pursuits = {conviction: 1.0}
    w.propositions[WANT] = Proposition(WANT, "OUGHT", PARTY, "the clerk should answer", True, 0)
    w.add_tenure(Tenure("t_bar_duke_want", DUKE, WANT, "commit", since=0))
    return w


def _run(conviction: str, seed: int, seasons: int, wrap=None):
    """Turn the seasons through the real chooser. Returns `(world, driver, chosen)`: `chosen` holds every
    Act OBJECT the chooser returned -- an observation, it decides nothing. Objects, not ids: the driver
    re-derives a re-deliberated act's id with its round (`loop/deliberate.py`, `:r<n>`), so an id the
    minter produced is not the id RESOLVE sees. `wrap` is the mutation hook a falsifier uses (a wrapper
    OUTSIDE the recorder, as an injection would be); THE BAR passes none."""
    w = _world(conviction, seed)
    d = SeasonDriver(w)
    real = P.chooser(w, verbs=resolvable_verbs())
    chosen: list = []

    def choose(p, v, s, ask_budget):
        scenes = real(p, v, s, ask_budget)
        chosen.extend(a for sc in scenes for a in sc.acts)
        return scenes
    if wrap is not None:
        choose = wrap(choose)
    for _ in range(seasons):
        d.season(choose, question=None,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d, chosen


def _zero_authored(w, chosen: list) -> None:
    """Every act that reached RESOLVE is an object the chooser returned: none was injected. Read off
    `w.acts`, the store every act entering RESOLVE is recorded in -- not `SeasonDriver.resolved`,
    which a contested act refused at admission (e.g. `speech.unheard`) never enters."""
    assert len(w.acts), "the run resolved no act at all"
    ours = {id(a) for a in chosen}          # `chosen` keeps every object alive, so no id is reused
    authored = [(a.id, a.actor, a.verb) for a in w.acts if id(a) not in ours]
    assert not authored, f"acts the chooser did not return reached RESOLVE (authored): {authored}"


def _executed(w, d, seasons: int, verb: str, subject: str) -> list:
    """The resolved acts of `verb` on `subject` that executed (`corpus_run.attribute`'s act-id rule)."""
    return [a for a, made, _ in attribute(w, d, seasons)
            if a.verb == verb and (a.payload or {}).get("subject") == subject and made]


def _proceeding(conviction: str, seed: int, seasons: int) -> str:
    """ONE SEEDED PROCEEDING, end to end, every link read off the log; returns the content hash."""
    w, d, chosen = _run(conviction, seed, seasons)
    _zero_authored(w, chosen)
    acts = {a.id: a for a in d.resolved}
    # THE DETERMINATION, and the firing its `causes[]` walk back to.
    done = [e for e in w.log if e.kind == "matter.determined"]
    fired = [e for e in w.log if e.kind == "date.fired"]
    raised = [(e, f) for e in done for f in fired if _walks_to(w, e, f.id)]
    assert raised, (f"{conviction}/{seed}: no determination's causes reach a date.fired "
                    f"({len(done)} determined, {len(fired)} fired)")
    e, f = raised[0]
    det, = [acts[c] for c in e.causes if c in acts]
    assert (det.verb, det.actor, det.via, det.payload.get("subject")) == ("determine", DUKE, SEAT, PARTY), det
    # THE DATE THAT RAISED IT: the held Date at the firing's venue, due the tick it fired, whose slot
    # CALENDAR formed and an `open_case` on the clerk filled.
    venue = world_q.anchor_of(w, f)
    did, = [k for k, v in w.dates.items()
            if v.get("venue") == venue and v.get("due_at") == f.emitted_at and v.get("fired")]
    assert w.dates[did]["holder"] == SEAT, w.dates[did]
    assert any(i.get("date") == did for i in w.docket), f"no slot names the raising date {did}: {w.docket}"
    formed = [x for x in w.log if x.kind == "docket.formed" and f.id in x.causes]
    assert formed, "the raising firing formed no docket slot"
    # The clerk's case was opened AFTER the firing (so it filled the slot, not a dateless item), and the
    # determination was formed from THAT sitting's question, which names only a slot's docketed matters.
    opened = [x for x in w.log if x.kind == "case.opened" and x.emitted_at >= f.emitted_at
              and any(c in acts and (acts[c].verb, acts[c].via, acts[c].payload.get("subject"))
                      == ("open_case", SEAT, PARTY) for c in x.causes)]
    assert opened, "no open_case put the clerk before the sitting after it fired"
    occ = d.scenes[det.scene].occasion
    assert occ.id.startswith(f"q:sitting:{did}:") and PARTY in occ.referents, occ
    # ... AND THE CONVENE THAT SCHEDULED IT WAS CHOSEN, NOT INJECTED.
    sched, = [x for x in w.log if x.kind == "date.scheduled" and any(ch.subject == did for ch in x.changes)]
    conv, = [acts[c] for c in sched.causes if c in acts]
    assert (conv.verb, conv.actor, conv.via, conv.payload.get("subject")) == ("convene", DUKE, SEAT, venue), conv
    assert sched.emitted_at < f.emitted_at
    return w.content_hash()


# ======================================================================================
# THE BAR
# ======================================================================================

def test_the_bar_two_seeded_proceedings_with_zero_authored_acts_run_twice_byte_identical():
    hashes = []
    for conviction, seed, seasons in PROCEEDINGS:
        first = _proceeding(conviction, seed, seasons)
        assert _proceeding(conviction, seed, seasons) == first, (
            f"{conviction}/{seed}: the same seeded proceeding hashed differently on its second run")
        hashes.append(first)
    assert len(set(hashes)) == len(PROCEEDINGS), "the two proceedings are one world, not two"


@pytest.mark.parametrize("verb", ["open_case", "speak"])
def test_an_injected_act_reddens_the_bar(verb):
    """THE BAR's first falsifier, kept: a wrapper OUTSIDE the recorder replaces the first act of the
    Duke's first scene with a hand-written act, and `_zero_authored` names it. `speak` is the act a
    `SeasonDriver.resolved` reading missed: refused `speech.unheard` at admission (no docketed
    matter yet), it never enters `resolved`, but it is in `w.acts`."""
    injected = []

    def wrap(choose):
        def inject(p, v, s, ask_budget):
            scenes = choose(p, v, s, ask_budget)
            if p.id == DUKE and not injected and scenes and scenes[0].acts:
                a = Act("authored_oc", DUKE, verb, via=SEAT, payload={"subject": PARTY})
                scenes[0].acts[0] = a
                injected.append(a)
            return scenes
        return inject
    conviction, seed, seasons = PROCEEDINGS[0]
    w, _, chosen = _run(conviction, seed, seasons, wrap=wrap)
    assert injected and injected[0].id in w.acts, "the injection never reached RESOLVE"
    with pytest.raises(AssertionError, match="authored_oc"):
        _zero_authored(w, chosen)


def test_the_walk_is_false_for_a_determination_the_ambition_raised_beside_a_fired_date():
    """THE CONTROL. Same world, virtue at seed 2 (re-traced at v10 CP-T05-04 against the assertions below only, from
    doctrine at seed 8; doctrine at 83 and at 22 before it, re-traced at IN-12 step 10 and step 9; the narrative that
    follows was traced at seed 8, SC-03b; community at seed 13 before it): the Duke convenes at `S` AND
    opens the clerk's case in the same season, so the case is docketed dateless before the sitting
    fires; the sitting's slot forms empty, and after the firing the Duke determines the
    clerk out of his ambition (`need`, occasion `[ROOT]`). That determination's `causes[]` reach no
    firing -- so THE BAR's walk is not satisfied by a firing merely preceding a determination."""
    conviction, seed, seasons = CONTROL
    w, d, chosen = _run(conviction, seed, seasons)
    _zero_authored(w, chosen)
    f, = [e for e in w.log if e.kind == "date.fired"]
    done = [e for e in w.log if e.kind == "matter.determined"]
    assert done and all(e.emitted_at > f.emitted_at for e in done), (f.emitted_at, [e.emitted_at for e in done])
    assert _executed(w, d, seasons, "determine", PARTY), "the control determined somebody else"
    assert world_q.docketed(w, PARTY) == [] and any(i.get("date") and i.get("matter") is None
                                                    for i in w.docket), w.docket
    assert not [e.id for e in done if _walks_to(w, e, f.id)]


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
    return branches_on_ids(tree, ARRANGEMENTS)


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
