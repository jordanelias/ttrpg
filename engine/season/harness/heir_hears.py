"""`harness.heir_hears` -- CR-26's SEEDED READING: does the heir hear the throne's vacancy?

Plan position CR-26 (IN-61's design-first check (4)). The chain is four links (`test_in61_heir_hears_vacancy.py`
names them and owns the PLANTED arms, which are that file's assertions). This module is the other half:
the SEEDED arm, which the plan calls a reading the commit quotes and never asserts (V2: a reading is a
harness reader). For each seed it builds `build_realm(seed)`, ticks it, records every question set the
heir is handed, and prints: whether the throne was vacated while the heir lived, whether a living heir heard
it at a later DELIBERATE, whether it was vacated but UNHEARD, and the control (how many sets named the throne
as a classed referent while it was HELD; expected 0).

It was a parametrized test of three module-scoped fixtures, about 220 CPU-seconds of the season suite, and it
passed with "none" by design; it moved here so the suite stops paying for a reading it never asserted.
What it still enforces, as an instrument: it exits 1 when a seed handed the heir fewer question sets than
seasons (it did not look) or when the control is not clean.

Entry point: `python -m engine.season.harness.heir_hears --seeds S S ... --seasons K`. Both are required and
neither has a default (this file is inside `tools/ci_sim_fabrication_check.py`'s blocking scope, the reason
`harness/storybar.py` gives for the same shape).
"""
from __future__ import annotations

import argparse
import sys

from ..decision import make_chooser
from ..decision.questions import aggregate_questions
from ..loop import driver as DRV
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..queries.person_q import ledger_names
from ..state.ids import H, draw_factory
from .populated import build_realm

THRONE, HEIR_SEAT = "off_king", "off_heir"


def holder(w, seat):
    """The one live holder of `seat` (`None` when it is vacant): a live `hold` edge on it."""
    held = [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == seat]
    assert len(held) <= 1, f"{seat} has {len(held)} live holders: {held}"
    return held[0] if held else None


def classed(q):
    return (THRONE, "Office") in q.classes if q is not None else False


def reading(w, heir, qs):
    """What the four links read at ONE question set handed to `heir` (the barrier-2 projection)."""
    rule = w.fixtures.get("question_aggregation_rule")
    answered = aggregate_questions(qs, rule) if qs else None
    return {"in_ledger": THRONE in ledger_names(heir.ledger),
            "seats_named": THRONE in world_q.seats_named(w, heir),
            "stamped": any(classed(q) for q in qs),
            "answered": classed(answered) and THRONE in answered.referents_for("Office")}


class HeirSpy:
    """A spy on `loop.driver.questions_for` (the barrier-2 call site), recording every question set handed
    to the heir with the tick, whether the throne was held and whether he lived. `questions_for` is
    imported by name into `loop.driver`, which is why the spy names that module. `install` takes anything
    with `setattr(obj, name, value)` (pytest's `monkeypatch`, or `Patch` below)."""

    def __init__(self, heir_id):
        self.heir_id, self.sets = heir_id, []

    def install(self, patcher):
        orig = DRV.questions_for

        def spy(w, p, since=None):
            out = orig(w, p, since)
            if p.id == self.heir_id:
                self.sets.append({"tick": w.tick, "throne_held": holder(w, THRONE) is not None,
                                  "reading": reading(w, p, out), "n": len(out)})
            return out
        patcher.setattr(DRV, "questions_for", spy)


class Patch:
    """The part of `pytest.MonkeyPatch` the spy needs, so a harness module does not import pytest."""

    def __init__(self):
        self._undo = []

    def setattr(self, obj, name, value):
        self._undo.append((obj, name, getattr(obj, name)))
        setattr(obj, name, value)

    def undo(self):
        while self._undo:
            obj, name, old = self._undo.pop()
            setattr(obj, name, old)


def one_season(w, d):
    """One real season: MATTER, CALENDAR, the rounds of DELIBERATE, RESOLVE and WITNESS."""
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    return d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))


def seeded_reading(seed: int, seasons: int) -> dict:
    """`build_realm(seed)`, `seasons` seasons, the heir's question sets recorded."""
    patch = Patch()
    try:
        w = build_realm(seed)
        heir_id = holder(w, HEIR_SEAT)
        assert heir_id and holder(w, THRONE) and heir_id != holder(w, THRONE), "fixture moved"
        spy = HeirSpy(heir_id)
        spy.install(patch)
        d = SeasonDriver(w)
        vacated = None
        for season in range(seasons):
            one_season(w, d)
            if vacated is None and holder(w, THRONE) is None:
                vacated = {"season": season + 1, "heir_alive": heir_id in w.persons}
        return {"seed": seed, "heir": heir_id, "sets": spy.sets, "vacated": vacated}
    finally:
        patch.undo()


def summarize(r: dict, seasons: int) -> tuple[str, list[str]]:
    """The printed line for one seed, and the instrument defects (an empty list when it looked and the
    control is clean)."""
    checked = len(r["sets"])
    vac = r["vacated"]
    heard = bool(vac and vac["heir_alive"] and any(
        s["reading"]["answered"] and not s["throne_held"] for s in r["sets"]))
    unheard = bool(vac and vac["heir_alive"] and not heard)
    pre = sum(1 for s in r["sets"] if s["throne_held"] and s["reading"]["answered"])
    line = (f"CR-26 SEEDED READING seed {r['seed']} x {seasons} seasons: checked={checked} heir "
            f"question sets; throne vacated: {vac or 'none'}; heard by a living heir: "
            f"{'yes' if heard else 'none'}; vacated but UNHEARD: {'yes' if unheard else 'none'}; "
            f"classed off_king while the throne was HELD: {pre} (control, expected 0)")
    defects = []
    if checked < seasons:
        defects.append(f"seed {r['seed']}: the heir was handed only {checked} question sets")
    if len({s["tick"] for s in r["sets"]}) < seasons:
        defects.append(f"seed {r['seed']}: the seed skipped a season")
    if pre:
        defects.append(f"seed {r['seed']}: a set named the held throne as a classed referent: "
                       "the control is not clean")
    return line, defects


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.heir_hears",
                                 description=__doc__.split("\n\n")[0])
    ap.add_argument("--seeds", type=int, nargs="+", required=True)
    ap.add_argument("--seasons", type=int, required=True)
    a = ap.parse_args(argv)
    bad = []
    for seed in a.seeds:
        line, defects = summarize(seeded_reading(seed, a.seasons), a.seasons)
        print(line)
        bad.extend(defects)
    for b in bad:
        print("INSTRUMENT DEFECT:", b, file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
