# CORE — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Scope: the season loop's spine — `engine/season/loop/{driver,calendar,census,deliberate,encounter,effects,effects_shared,matter,predicates,resolve,sides}.py`,
`state/`, `seam/`, `manifest/`, `data/`, `queries/{cache,inputs}.py`, the YAML registries the loop opens
(`verb_table`, `write_matrix`, `rosters`, `requirements`, `hole_register`) and the `harness/` instruments.
Subsystem effect bodies, `decision/` and the strife harness are other lanes'; they are cited here only where
the core's contract with them is the thing judged.

## 0. Verdict

(written first, on the spine; revised at the end of the reading — see the final paragraph of this section)

## 1. What it is, as coded

### 1.1 The loop (execution order, read at `loop/driver.py:388-563`)

One function, `SeasonDriver.season(choose, question, actorless, contest_max_depth, host)`, is the game's
only clock. Per call:

1. `w.draw = 0`; season-local driver state cleared (`round`, `_queued`, `_spent`, `_deliberated_at`,
   `_inputs`, `_realised`) — `driver.py:468-473`.
2. **CALENDAR** once (`loop/calendar.py:36`): fires `w.dates` due this tick, forms docket items, re-slots
   undated matters. Token `CALENDAR`.
3. **MATTER** once (`loop/matter.py`): wear, yield, subsistence, term maturation, the modules' `step_call`
   entries; ends by setting `w.frozen = True`. Token `MATTER`.
4. **R rounds**, `R = fixtures.scene_budget` (`driver.py:479,486`). Each round: `w._rehome()`; freeze;
   **DELIBERATE** (no token; a per-person map calling `choose(p, view, sensation, ask_budget)`,
   `deliberate.py:131-320`); **RESOLVE** (token `ACTS`; canonical order = stratum, then a seeded hash;
   eligibility → `requires` → contest/grade/fold → effect through `World.write`, `resolve.py:996-1200`);
   **ENCOUNTER** (same barrier; fights the acts RESOLVE declared and deferred, `encounter.py:43`);
   the round's Events appended to the one log; **WITNESS** (token `INTERIOR`; fan-out into ledgers).
5. **CENSUS** once (`loop/census.py:35`): individuates a person only on a `person.demanded` Event.
6. `world_q.endings_reached(w)` read (no write); `w.tick += 1`; returns
   `{acts, events, rounds, deposits, hash, endings}`.

The seven steps are module functions bound onto the class at `driver.py:597-620`; RESOLVE's helpers
(`_eligible`, `_admits`, `_fold`, `_apply_write`, `_contest`, `_grade`, `_survives`) are bound the same way.

### 1.2 State and the gate

`state/world.py::World` owns six entity stores (`persons`, `rungs`, `offices`, `sites`, `records`,
`propositions`), `dates`, `docket`, the append-only `EventLog` (`state/log.py`) and `ActStore`
(`state/acts.py`). Tenures are owned by their subject Person; `w.tenures` is a read-only concatenation
rebuilt on every access (`world.py:455-471`).

`World.write(...)` (`world.py:1138-1555`) is the single write path. Per call it checks, in order: a real
`Token` at the current tick; the `(record_kind, field)` row of `write_matrix.yaml` admits the current step
and write class; `social: true` rows are written only by `driver="Act"`; `(Person, coherence)` only by the
seam; an actorless `Tenure.until` only through a death or a matured term; a MATTER write on an emitting row
names a declared kind; then it opens the gate, snapshots tenures, applies, refuses an unauthored tenure
change (`gate.refuse_unauthored` → fourteen named bases, `gate.py:1137-1481`), refuses a `Change` whose
named subjects read the same after as before (`NoOpReceipt`), mints receipts and emits. `EventLog.append`
refuses a receipt the gate did not mint and a `causes[]` id that resolves to no prior Event, no stored Act
and not `ROOT` (`log.py:64-101`).

Determinism: ids and draws are `H(seed, tick, subject, purpose)` (`state/ids.py:16`); a contest's RNG is
`random.Random(int(H(...),16))` (`ids.py:90`, `resolve.py:833`). `World.content_hash()` folds the entity
stores, docket, tenures and the whole log (`world.py:1667-1726`).

### 1.3 Seam, manifest, data

`seam/contest.py` routes a contested act to a provider registered by `@provider(role, module)` and found
through `manifest.resolve("contest", prize)`; providers are `seam/wrappers/{sigma,combat,mass_battle,fieldwork}.py`,
each a host adapter that builds a typed input, calls a module entry recorded by `manifest/registrar.py`
from `references/module_contracts.yaml`'s composition rows, and returns a scene dict whose degree
`seam/ladder.py::degree_of` reads. `SeasonDriver.__init__` runs the registrar and six refusals
(`driver.py:285-302`) on every construction. `data/` is the loader layer for the YAMLs; `data/__init__.py::load_all`
is called from the driver constructor.

### 1.4 Execution evidence (full log in §12)

| what ran | seed / seasons | result |
|---|---|---|
| `python -m engine.season.harness.register --requirements` | — | 0.5 s; `met 3 · not_met 1 · partial 5`; reads `status:` strings and validates each row carries a `measured:` or names one |
| `python tools/m1_acceptance.py --summary` | seed 20260819, 1 season ×2; 24 seeds ×4 seasons + 2 populated ×1 | 20.6 s; stub invocations 0 PASS; same-seed hash equal PASS (`bbf88d55e218…`); nine met 3/9 FAIL (declares itself DOC-DERIVED); 0 invariant violations over 49,735 events / 32,974 claims PASS; verdict NOT MET |

(corpus sweep, four-season realm aperture and the size measurement are reported where the findings use them.)
