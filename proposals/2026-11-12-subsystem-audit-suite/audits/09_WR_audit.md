# WR — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Lane: world, threadwork, clocks, travel, survival, strife flows, narrative engine. Every reading below is a
dated reading of the command in §12 (seed and season count stated with it, `PYTHONHASHSEED=0`). Design
documents are cited for intent and vocabulary only (CLAUDE.md §0.05); `.designs/` is not cited as authority.

## 0. Verdict

VERDICT_PLACEHOLDER

## 1. What it is, as coded

**The lane has no module of its own.** Unlike combat, mass battle, social contest, settlements and fieldwork,
nothing under `modules/` is "world", "threadwork" or "narrative". WR as coded is four things inside
`engine/season/`, plus an unplugged oracle:

| piece | file | what it is | reached by the loop? |
|---|---|---|---|
| CALENDAR, barrier 1 | `engine/season/loop/calendar.py` (109 lines) | fires a `Date` whose `due_at == w.tick` (`date.fired`), forms an empty docket slot per held date (`docket.formed`), re-slots waiting person-matters (CR-56). Decides nothing | yes: `loop/driver.py::season`, once per season, before MATTER |
| MATTER, barrier 2 | `engine/season/loop/matter.py` (903 lines) | the licensed clocks: record-stage maturation, `Tenure.term` maturation, docket lapse, claim-confidence decay, standing-band crossing, the larder draw (`settlements.subsist`), the body fall and death at zero, the bodies clock (age, illness), yield (`settlements.produce`), travel-leg end, site wear plus the lattice coupling, band crossings | yes: once per season, after CALENDAR |
| ENCOUNTER, step 7 | `engine/season/loop/encounter.py` (84 lines) | fights the contests RESOLVE declared and deferred (`Declared` degree), in `_canonical_order`; the one step a playable host may suspend at | yes: once per round, after RESOLVE |
| the world-first Queries | `engine/season/queries/world_q.py` (5,556 lines, 251 top-level definitions) | every resolver-side read: containment, docket, works, bench, reception/proofs, place, reach, larder projections, housing, hunger, polity (`members`, `leaders`, `provinces_of`, `uncontrolled`), `endings_reached`, ambitions and stages, the standing-occasion stampers, `questions_for`, `occasioned_by`, `WorldReader`, and the strife readings (`flows_in`, `flows_known`, `flow_stakes`) | yes: `questions_for` at every DELIBERATE round; the rest by their callers |
| the narrative instruments | `engine/season/harness/storybar.py`, `chronicle.py`, `arc.py`, `strife.py`, `strife_data.py`, `strife_moves.yaml` | observers over a finished log: cross-person antecedent share and chain depth; the deepest consequence chain rendered; the thrust-arc reader with two nulls; the strife-move reach table and the strand reading | **no**. None is imported by `loop/`. One strife reading has a loop consumer: `world_q.flow_stakes`, stamped by `questions_for` when `Fixtures stamp_flow_stakes` is on (shipped on) |
| `ENDINGS_CLASSIFIED.yaml` | `engine/season/ENDINGS_CLASSIFIED.yaml` (224 lines) | a blind agent classification of 50 arc `ends_when` strings into DECIDER / ROLL / THRESHOLD / NEVER / UNCLEAR. Its own header: "AN AGENT CLASSIFICATION OF PROSE, NOT AN EXECUTION" | no code reads it for a game fact (§4.2) |
| the threadwork and overview oracles | `systems/threadwork/sim/*.py` (1,950 lines), `systems/overview/sim/ms_track.py` (92 lines) | the pre-season-loop thread operations (Leap, Weave, Pull, Lock, Dissolve, Mend), coherence, co-movement, the Mending Stability track | **no**. The season loop reaches none of it; `thread_read` is the one thread verb the loop resolves (through fieldwork) |

**State the lane owns** (by write-matrix cell, written only at the barrier named): `Date.fired`, the
`DocketItem` (CALENDAR; MATTER lapses it); `Record.matured`, `Tenure.until` on a matured term,
`Claim.confidence`, `Person.body` and `Person.exists` (hunger, age, illness), `Rung.stores`, `Rung.yield`,
`Person.travel_leg`, `Site.condition` (MATTER). Nothing in `world_q.py` or the harness owns state; every
Query recomputes (T-a).

**How the season reaches it** (`loop/driver.py::season`, read at `:388-563`): `calendar` then `matter` once;
then `scene_budget` rounds (shipped 5) of `deliberate → resolve → encounter → witness`; MATTER's and
CALENDAR's Events join round 0's WITNESS fan-out only; `w.tick` advances once; `world_q.endings_reached(w)`
is read once at the end of the season and returned in the season summary. The run does not halt on an
ending.

Execution evidence is in §12; the readings that carry the findings are quoted where they are used.
