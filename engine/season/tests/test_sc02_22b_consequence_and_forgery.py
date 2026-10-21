"""v9 SC-02 `22b`, piece 1 -- proceedings `19_PLAN.md` steps 24 and 25.

STEP 24, *conviction moves by consequence* (the plan's `convictions` is `(Person, pursuits)` since
`ED-IN-0261` item 1): a determination moves ITS MAKER'S OWN held pursuits, at RESOLVE, by
`pursuit_shift x DEGREE_STEP[band] x pursuit_lean(determine, pursuit)` (`queries/person_q.py::
consequence_pursuits`, written by `loop/effects_information.py::_eff_determine`; `H-221`). Its
FALSIFIER, observed against `(Person, pursuits)`: *"a conviction moves at witness; or the emission cites a
deposit rather than an act"*. The `Failure` arm (*against their own axis*) is NOT built (`H-221`'s
`cite:`), and the band is pinned writing nothing so the day it is built this file says so.

STEP 25, *the forged record is a proof until it is examined* -- the half re-added to `22b` (`H-210`):
`forge` WRITES `Record.forgery_quality` and an examination CONTESTS it, in one change -- an inquiry's
roll on the Record carries the quality into its obstacle (`seam/wrappers/sigma.py::contest_input` ->
`modules/social_contest/roll.py::obstacle`), and what a finding then deposits is FI-03's, unchanged.
Its FALSIFIER: *"the forgery quality still has zero readers after this lands."* The rest of step 25 (the
examiner witnessed examining; a forged record counted as a proof until examined) is not built.

Worlds: `test_u7_remit.py`'s `tiny_world` bench (step 24) and `test_fi03_trail.py`'s `trail_world`
(step 25), every act through the real fold and the real adapter.
"""
from __future__ import annotations

import dataclasses
import inspect
import random
import re

import yaml

from ..data import files
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass, matrix_row
from ..data.pursuits import pursuit, to_axes
from ..data.rosters import DEGREE_BANDS, DEGREE_STEP, PURSUIT_AXES
from ..data.verbs import VERB_TABLE, align
from ..loop.driver import mint_token
from ..queries import person_q
from ..queries.inputs import Margin
from ..seam.wrappers import sigma
from ..state import carriers as C
from .test_fi03_trail import (
    INVESTIGATOR, chooser_research, forged_claims, research, step, trail_world,
)
from .test_sc01_obstacle_ceiling import _module
from .test_u7_remit import DUKE, JUDGE, PARTY, _determine, _fold, _kinds, _open, _world

# [JUSTIFIED: authored test character, not a game value -- three pursuits whose leans on `determine` differ in sign, so a move is visible in both directions]
HELD = {pursuit("honour"): 0.5, pursuit("liberty"): 0.3, pursuit("stability"): 0.2}
# [JUSTIFIED: a test-fixture search bound, not a game value -- the act ids tried for a band; asserted reached]
SWEEP = 40


def _sweep_of(hid):
    """A register row's declared points and the fixture its `site:` names (`test_sc02_reception.py`'s
    reading): the arms come from the register, never from this file."""
    rows = yaml.safe_load(files.HOLE_REGISTER_YAML.read_text())["rows"]
    (row,) = [r for r in rows if r["id"] == hid]
    return row["sweep"], row["site"].split(",")[0].split()[-1]


def _lean(e):
    """`pursuit_lean`, recomputed here from the two tables so the expected move is not the code's own
    function read back."""
    proj = to_axes({e: 1.0})
    return sum(proj[ax] * align("determine", ax) for ax in PURSUIT_AXES)


def _expected(before, band, gain):
    return {e: float(w) + float(gain) * DEGREE_STEP[band] * _lean(e) for e, w in before.items()}


def _determined(n, **fx):
    """A fresh bench, the judge holding `HELD`, the matter docketed, then ONE determination `dt<n>`
    through the fold at the shipped pool. Returns `(w, d, out, before)`."""
    w, d = _world(**fx)
    w.persons[DUKE].pursuits = dict(HELD)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    before = dict(w.persons[DUKE].pursuits)
    return w, d, _fold(w, d, _determine(f"dt{n}")), before


def _by_band(**fx):
    """`{band: n}` for the first act id `n` in `SWEEP` drawing each band."""
    got = {}
    for n in range(SWEEP):
        _w, _d, out, _b = _determined(n, **fx)
        band = out[0].degree if out else None
        if band in DEGREE_BANDS and band not in got:
            got[band] = n
        if len(got) == len(DEGREE_BANDS):
            break
    return got


# ======================================================================================
# STEP 24 -- the determiner's own pursuits, by band
# ======================================================================================

def test_step24_each_band_moves_the_judges_held_pursuits_by_its_step_and_no_other_person():
    """Through the real fold at the shipped arm, each band the roll draws: `Overwhelming` and `Success`
    move every held pursuit by exactly `pursuit_shift x DEGREE_STEP[band] x lean` and publish
    `pursuit.moved` beside `matter.determined`; `Partial` (the held matter) moves nothing and publishes
    `matter.determined` alone; `Failure` moves nothing (the unbuilt arm, `H-221`) and publishes
    `matter.undetermined` alone. Nobody else's pursuits move. Every band is reached -- asserted. The
    shipped pool (2 against 2) draws three bands; `Overwhelming` is drawn by the strong judge (`JUDGE`),
    the pool being all that differs."""
    bands = {b: (n, {}) for b, n in _by_band().items()}
    bands.setdefault("Overwhelming", (_by_band(**JUDGE).get("Overwhelming"), JUDGE))
    assert set(bands) == DEGREE_BANDS and None not in [n for n, _ in bands.values()], bands
    gain = DEFAULT_FIXTURES.get("pursuit_shift")
    assert gain, "the shipped arm is the control: nothing below could move"
    checked = 0
    for band, (n, fx) in sorted(bands.items()):
        w, _d, out, before = _determined(n, **fx)
        assert out[0].degree == band, (band, out[0].degree)
        others = {pid: dict(p.pursuits) for pid, p in w.persons.items() if pid != DUKE}
        after = w.persons[DUKE].pursuits
        if DEGREE_STEP[band] > 0:
            assert after == _expected(before, band, gain), (band, before, after)
            assert after != before, band
            assert _kinds(out) == ["matter.determined", "pursuit.moved"], (band, _kinds(out))
        else:
            assert after == before, (band, before, after)
            assert "pursuit.moved" not in _kinds(out), (band, _kinds(out))
        assert {pid: dict(p.pursuits) for pid, p in w.persons.items() if pid != DUKE} == others
        checked += 1
    assert checked == len(DEGREE_BANDS)
    # The two moving bands differ in REACH, not only in sign: Overwhelming moves twice Success's step.
    assert DEGREE_STEP["Overwhelming"] == 2 * DEGREE_STEP["Success"] > 0 == DEGREE_STEP["Partial"]


def test_step24_the_sweep_runs_and_zero_is_the_control():
    """`H-221`'s declared points, run: at `0` a determination that draws a moving band writes exactly
    what it wrote before this step -- one Event, `matter.determined`, whose changes name the edge alone --
    and the judge's pursuits are untouched; each larger point moves them strictly further."""
    points, fixture = _sweep_of("H-221")
    assert fixture == "pursuit_shift" and len(points) == 3 and 0 in points, (fixture, points)
    n = _by_band(**JUDGE).get("Overwhelming")
    assert n is not None, "the strong judge drew no Overwhelming"
    dist = []
    for point in sorted(points):
        w, _d, out, before = _determined(n, **{**JUDGE, fixture: point})
        assert out[0].degree == "Overwhelming", out[0].degree
        after = w.persons[DUKE].pursuits
        if point == 0:
            assert _kinds(out) == ["matter.determined"], _kinds(out)
            assert [c.subject for c in out[0].changes] == [t.id for t in w.tenures
                                                         if t.subject == PARTY and t.kind == "oblige"]
            assert after == before
        dist.append(sum(abs(after[e] - before[e]) for e in before))
    assert dist[0] == 0 < dist[1] < dist[2], dist


def test_step24_falsifier_witness_never_moves_a_pursuit_and_the_emission_cites_the_act():
    """THE PLAN'S FALSIFIER, observed against `(Person, pursuits)`. (a) WITNESS moves no one's pursuits:
    every person's map is snapshotted after RESOLVE and read again after WITNESS runs over the very
    Events that carry the move. (b) The `pursuit.moved` Event cites THE ACT -- its first cause is the
    determination's id, an Act the store holds -- and no cause is a claim or a `claim.deposited` Event."""
    n = _by_band(**JUDGE)["Overwhelming"]
    w, d, out, before = _determined(n, **JUDGE)
    (moved,) = [e for e in out if e.kind == "pursuit.moved"]
    assert w.persons[DUKE].pursuits != before, "nothing moved, so (a) below would be vacuous"
    snap = {pid: dict(p.pursuits) for pid, p in w.persons.items()}
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    assert {pid: dict(p.pursuits) for pid, p in w.persons.items()} == snap, "WITNESS moved a pursuit"
    assert any(e.kind == "claim.deposited" for e in w.log), "WITNESS deposited nothing: (a) is vacuous"
    assert moved.causes[0] == f"dt{n}" and w.acts.get(moved.causes[0]) is not None, moved.causes
    claim_ids = {c.id for p in w.persons.values() for c in p.ledger}
    deposits = {e.id for e in w.log if e.kind == "claim.deposited"}
    assert not (set(moved.causes) & (claim_ids | deposits)), moved.causes
    assert DUKE in [c.subject for c in moved.changes], moved.changes


def test_step24_the_interior_shift_is_no_deed_and_is_judged_as_none():
    """`pursuit.moved` is emitted by `determine` alone, so `KIND_VERB` maps it there and it is a DEED kind
    (the premise the authored cells answer); with no `deed:pursuit.moved` cell a claim of it would be
    valued by `determine`'s own alignment -- the judge's private shift judged a second time beside
    `matter.determined`, and chronicled to everyone (`_ch_chronicle`). The authored `0.0` cell on every
    axis makes a claim of it worth nothing, observed through `person_q.deed_valence` on a holder with
    pursuits (CONTROL: `determine` itself is non-zero on some axis, so the zero is the cell's doing)."""
    from ..data.verbs import ALIGNMENT, DEED_KINDS, KIND_VERB, align_kind
    # ⚠ RE-RECORDED AT v9 IN-12 step 9 -- THE SECOND EMITTER THE CELL'S OWN NOTE FORESAW (`rosters.yaml`, the
    # `deed:pursuit.moved` cell: *"Held at 0.0 it also survives a second emitter"*): `argue`'s won bands emit
    # it too, so the kind is SHARED and leaves `KIND_VERB`; it is still a deed kind, and `align_kind` now reads
    # the authored 0.0 cell through the shared-kind branch. The assertions below are unchanged.
    emitters = sorted(v for v, r in VERB_TABLE.items() if "pursuit.moved" in set(r.emits))
    assert emitters == ["argue", "determine"] and "pursuit.moved" not in KIND_VERB, emitters
    assert "pursuit.moved" in DEED_KINDS
    axes = sorted(ALIGNMENT)
    assert len(axes) >= 2 and any(align("determine", ax) != 0.0 for ax in axes), axes
    for ax in axes:
        assert align_kind("pursuit.moved", ax) == 0.0, ax
    w, _d = _world()
    w.persons[PARTY].pursuits = dict(HELD)
    axis_w = person_q.projected_axes(w.persons[PARTY])
    deed = C.Claim("moved", PARTY, DUKE, "pursuit.moved", True, 0, "firsthand", 100, "own", 0)
    control = C.Claim("decided", PARTY, DUKE, "matter.determined", True, 0, "firsthand", 100, "own", 0)
    assert person_q.deed_valence(axis_w, deed) == 0.0
    assert person_q.deed_valence(axis_w, control) != 0.0, "the control kind reads zero: the fixture is inert"


def test_step24_three_findings_move_one_judges_lean_toward_judging_by_a_printed_amount():
    """`19_PLAN.md` step 24's artifact, its first half: three determinations by one judge, each over a
    different party, each drawing a moving band, move his weight by the printed amount -- and the move
    is toward the act (`Σ_e weight[e] x lean(e)`, the chooser's pursuit term for `determine`, rises
    each time: a positive loop, which is the risk the plan names for the forty-season run)."""
    w, d = _world(**JUDGE)
    w.persons[DUKE].pursuits = dict(HELD)
    term = lambda: sum(w.persons[DUKE].pursuits[e] * _lean(e) for e in HELD)
    readings = [term()]
    for i, party in enumerate(("p_mid", "p_low", "p_other")):
        assert _kinds(_fold(w, d, _open(f"oc{i}", subject=party))) == ["case.opened"]
        out = _fold(w, d, _determine(f"dtt{i}", subject=party))
        assert out[0].degree in ("Overwhelming", "Success"), out[0].degree
        readings.append(term())
    assert readings[0] < readings[1] < readings[2] < readings[3], readings


def test_step24_the_matrix_row_has_its_producer_and_the_lean_has_one_owner():
    """The row's `unproduced:` is struck (the loader's invariant 2 refuses it once a verb writes the
    pair), the bands that move declare the pair, and the scar's sign test reads the same lean."""
    assert matrix_row("Person", "pursuits").unproduced == ""
    row = VERB_TABLE["determine"]
    assert [b for b in sorted(DEGREE_BANDS) if "Person.pursuits" in row.writes_at(b)] == [
        "Overwhelming", "Success"]
    assert row.writes_at("Failure") == () and "pursuit.moved" not in row.emits_at("Failure")
    for e in HELD:
        assert person_q.pursuit_lean("determine", e) == _lean(e)
        assert (e in person_q._pursuits_violated_by("determine")) == (_lean(e) < 0)


# ======================================================================================
# STEP 25 -- the forgery's quality: written by forging, contested by examination
# ======================================================================================

def _fx(**kv):
    f = DEFAULT_FIXTURES
    for k, v in kv.items():
        f = f.sweep(k, v)
    return f


def _research_out(n, **fx):
    """`trail_world` at `fx`, then the investigator's chooser-formed `research` `n` on the forged Record,
    resolved and witnessed. Returns `(w, rid, finding Event)`."""
    w, d, rid = trail_world(fixtures=_fx(**fx))
    cand = chooser_research(w, rid)
    assert cand is not None
    (finding,) = step(w, d, research(n, cand))
    return w, rid, finding


def test_step25_forge_writes_the_quality_and_survey_does_not():
    """THE WRITER, through the fold, at each of `H-210`'s declared points: the forged Record carries the
    arm's quality; a SURVEY (the same body, `_mint_sheet`, the same id and hand) carries `0`."""
    points, fixture = _sweep_of("H-210")
    assert fixture == "default_forgery_quality" and 0 in points and len(points) == 3, (fixture, points)
    for point in points:
        w, _d, rid = trail_world(fixtures=_fx(**{fixture: point}))
        assert w.records[rid].forgery_quality == point, (point, w.records[rid].forgery_quality)
    w, _d, rid = trail_world(verb="survey", kind="faction.surveyed")
    assert w.records[rid].forgery_quality == 0


def test_step25_falsifier_the_examination_reads_the_quality_into_its_obstacle():
    """THE READER, through the real adapter and module entry: an inquiry (no prize) on the forged Record
    rolls against `obstacle_default + quality` where the ceiling allows it (the uncapped `None` arm),
    and against the default at quality `0`. A CONTEST naming a prize on the same Record reads no quality
    (only an examination contests it; the gate is observed by
    `test_step25_a_prize_contest_examines_nothing...`). At the SHIPPED ceiling (2, `= obstacle_default`) the forgery is
    bounded to the default -- the stated limit, pinned so a ceiling change shows here."""
    obs = {}
    for q in (0, 1, 3):
        for ceiling in (None, DEFAULT_FIXTURES.get("obstacle_ceiling")):
            w, _d, rid = trail_world(fixtures=_fx(default_forgery_quality=q, obstacle_ceiling=ceiling,
                                                  pool_default=30))
            out = sigma.resolve(w, [INVESTIGATOR], ["root"], None, verb="research", subject=rid,
                                rng=random.Random(0), module_entry="social_contest.roll")
            assert out["status"] == "RESOLVED", out
            obs[(q, ceiling)] = out["ob"]
            inp = sigma.contest_input(w, [INVESTIGATOR], verb="research", subject=rid)
            assert inp.forgery_quality == 0.0, "a contest with no `examined` read the quality"
    base = DEFAULT_FIXTURES.get("obstacle_default")
    shipped = DEFAULT_FIXTURES.get("obstacle_ceiling")
    assert [obs[(q, None)] for q in (0, 1, 3)] == [base, base + 1, base + 3], obs
    assert [obs[(q, shipped)] for q in (0, 1, 3)] == [min(base, shipped)] * 3, obs


def test_step25_a_prize_contest_examines_nothing_and_an_inquiry_examines_its_subject(monkeypatch):
    """The adapter's gate, `examined = subject if prize is None else None`: an inquiry (no prize) hands the
    Record to the input builder, a contest a prize names hands it nothing, so a `speak` on the same
    Record reads no forgery quality. Observed through a spy on `contest_input`'s `examined` (the
    gate is a branch in `resolve`, and the builder's own default is not it)."""
    w, _d, rid = trail_world(fixtures=_fx(obstacle_ceiling=None))
    seen = []
    real = sigma.contest_input

    def spy(*args, **kw):
        seen.append(kw.get("examined"))
        return real(*args, **kw)
    monkeypatch.setattr(sigma, "contest_input", spy)
    sigma.resolve(w, [INVESTIGATOR], ["root"], "a matter", verb="speak", subject=rid,
                  rng=random.Random(0), rung=None)
    sigma.resolve(w, [INVESTIGATOR], ["root"], None, verb="research", subject=rid,
                  rng=random.Random(0))
    assert seen == [None, rid], seen


def test_step25_a_better_forgery_is_found_less_and_finding_it_deposits_the_forgery():
    """END TO END, at the uncapped ceiling: the same research act (the same roll, `H(seed, tick, ...)`)
    on a forgery of quality `0` and of quality `1`. For EVERY act id tried the band at `1` is no better
    than at `0` (the obstacle rose; the net is the same draw), and for AT LEAST ONE the quality-0 forgery
    is FOUND -- FI-03's deposit lands `record.forged` on the investigator -- while the quality-1 forgery
    finds nothing and leaves him holding no such claim: *finding nothing leaves it standing*."""
    flipped = compared = 0
    for n in range(SWEEP):
        w0, _r0, f0 = _research_out(n, default_forgery_quality=0, obstacle_ceiling=None)
        w1, _r1, f1 = _research_out(n, default_forgery_quality=1, obstacle_ceiling=None)
        assert DEGREE_STEP[f1.degree] <= DEGREE_STEP[f0.degree], (n, f0.degree, f1.degree)
        compared += 1
        if f0.kind == "finding.made" and forged_claims(w0, INVESTIGATOR) and f1.kind == "finding.none":
            assert forged_claims(w1, INVESTIGATOR) == [], n
            flipped += 1
    assert compared == SWEEP and flipped >= 1, (compared, flipped)


# ======================================================================================
# STEP 26 -- "None by default": nothing is built; the falsifier is observed
# ======================================================================================

def _module_state(mod):
    """A module's non-callable, non-module globals, by `repr` -- what a call could leave behind."""
    return {k: repr(v) for k, v in vars(mod).items()
            if not k.startswith("__") and not callable(v) and not inspect.ismodule(v)}


def test_step26_no_momentum_value_survives_a_barrier_outside_a_record():
    """`19_PLAN.md` step 26's FALSIFIER, *"any momentum value surviving a barrier outside a record"*,
    observed two ways, each able to fail. (a) BY CONSTRUCTION: no field of any state carrier
    (`state/carriers.py`'s dataclasses -- every one, counted) and no attribute of a `World` is named
    for momentum or a debate score. (b) BY EXECUTION: a contested act rolled through the real fold
    (the strong judge's `determine`) leaves the `World`'s attribute set, and the roll module's own
    globals, exactly as they were, and no `Margin` -- the roll's only output -- is held by the World
    or by any carrier it stores: the margin dies with the fold, and what survives is the Event's band
    (the log) and the edge the band opened. ⚠ (a) is a NAME scan and cannot see a carrier named for
    something else; (b) is what sees one built inside the contest path."""
    carriers = [c for c in vars(C).values()
                if inspect.isclass(c) and dataclasses.is_dataclass(c) and c.__module__ == C.__name__]
    names = [(c.__name__, f.name) for c in carriers for f in dataclasses.fields(c)]
    assert len(carriers) >= 10 and len(names) >= 100, (len(carriers), len(names))
    w, d = _world(**JUDGE)
    names += [("World", k) for k in vars(w)]
    assert not [n for n in names if re.search(r"momentum|debate", n[1], re.I)], names
    roll_mod = _module()
    before_attrs, before_mod = set(vars(w)), _module_state(roll_mod)
    assert _kinds(_fold(w, d, _open("oc26"))) == ["case.opened"]
    out = _fold(w, d, _determine("dt26"))
    assert out[0].degree in DEGREE_BANDS, "no contest was rolled, so (b) would be vacuous"
    assert set(vars(w)) == before_attrs, set(vars(w)) ^ before_attrs
    assert _module_state(roll_mod) == before_mod
    held = [v for v in vars(w).values() if isinstance(v, Margin)]
    for store in w._STATE_COLLECTIONS:
        for ent in getattr(w, store).values():
            held += [v for v in vars(ent).values() if isinstance(v, Margin)] if hasattr(ent, "__dict__") else []
    held += [v for t in w.tenures for v in vars(t).values() if isinstance(v, Margin)]
    assert held == [], held
