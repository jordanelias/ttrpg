# SC — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

## 0. Verdict

(PROVISIONAL, written before the reading finished; replaced at the close.) The social contest as the
season loop runs it is a sound **resolution primitive** and not yet a **contest**: one party's pool
against a halved score, one draw, four bands, folded into the log by the one ladder. The 6,700-line
kernel under `systems/social_contest/sim/contest/` is a second, richer model of the same subject that
the loop does not call.

## 1. What it is, as coded

Two bodies of code carry the name, and only one is reached by the season loop.

**(a) The roll the loop runs.** `modules/social_contest/roll.py` (166 lines): `obstacle(inp)` and
`roll(inp, rng) -> Margin(net, ob)`. Reached by string through the composition row `social_contest.roll`;
the host adapter and input builder is `engine/season/seam/wrappers/sigma.py` (`contest_input`, `resolve`,
`odds_of`, `believed_chance`), the pool reader `seam/wrappers/pool.py::faculty`, the dispatcher
`seam/contest.py::contest` / `grade`, the band `seam/ladder.py::degree_of` (a call into
`engine/dice_engine/dice_engine.py::degree_from_net`), the fold `loop/resolve.py::_contest` / `_grade` /
`_fold`.

**(b) The kernel the loop does not run.** `systems/social_contest/sim/contest/` (16 files): an
exchange-by-exchange bout (`resolver.py::Bout.resolve`) over venue specs (`modules.py`→`modes.py`),
per-side Standing/Reserve/Room trackers, a stasis ladder, evidence dossiers, fault clinches, win
conditions, an adjudicator armature and a narrative summariser. Its only importer outside itself is
`engine/tests/test_contest_kernel.py`.

(Entry points, state and execution evidence are appended below as the reading completes.)
