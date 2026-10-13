"""Shared fixtures for `engine/season/tests`.

`realm_4s` IS THE ONE 4-SEASON RUN OF `build_realm(0)` THROUGH THE REAL CHOOSER (v9 IN-10 close, after
`Season Loop Tests` was `cancelled` at its 20-minute cap, run 38362814770): `aperture 4 0` is the plan's
exit instrument for every verb position of B-I, each position's falsifier needs the same run, and a
module-scoped copy per file costs about twelve CPU-minutes per pytest worker that touches it. A
test that needs the realm after four seasons takes this fixture instead of building its own; one that
needs a different horizon, seed or instrumentation builds its own.

The run is instrumented only by RECORDING: `choose.opening_set` is wrapped to note, for every `oblige`
Candidate any person forms, whether his own ledger named the seat at that moment (`formed`), and the
wrapper returns what the real function returned, so the run is the same run with or without it.
"""
import pytest

from engine.season.harness import populated as POP
from engine.season.harness.corpus_run import attribute
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.decision import make_chooser
from engine.season.state.ids import H, draw_factory

SEASONS_4S = 4


@pytest.fixture(scope="session")
def realm_4s():
    """`(w, d, rows, formed)`: the world and driver after `SEASONS_4S` seasons of
    `populated.run`'s construction, `corpus_run.attribute`'s rows for it, and the `oblige`
    formations recorded as `(person, subject, subject_was_named_in_his_ledger)`."""
    from engine.season.decision import choose as CH
    from engine.season.queries.person_q import ledger_names
    formed = []
    real = CH.opening_set

    def watching(p, v, q, fx):
        out = real(p, v, q, fx)
        for c in out:
            if c.verb == "oblige":
                formed.append((p.id, c.subject, c.subject in ledger_names(p.ledger)))
        return out
    w = POP.build_realm(0)
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(CH, "opening_set", watching)
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                          draw=draw_factory(w.world_seed, lambda: w.tick))
        for _ in range(SEASONS_4S):
            d.season(ch, question=None, subsistence=POP.P.SUBSIST,
                     contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d, attribute(w, d, SEASONS_4S), formed
