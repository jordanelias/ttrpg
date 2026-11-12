# PC — a typed combat outcome, one door onto the engine, and the small edits that ride with them

## Status: PROPOSED

Lane: PC. Source: `audits/03_PC_audit.md` F-PC-06, F-PC-07, F-PC-08 (a), F-PC-10, F-PC-11; resolutions
R-PC-01 to R-PC-05, R-PC-09, R-PC-10, R-PC-15 to R-PC-18, R-PC-20. Read at `601e715`. Reference only
(CLAUDE.md §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime

Part A: the shape of what crosses the combat seam, with one declared hash mover (an `Event.ending`
value is renamed for the fighter left standing, and a felled party's death Event gains one
Observation). Part B: nothing in a season run; it makes the workbench call the same entry the loop
calls. Part C: nothing, except a possible one-unit-in-the-last-place difference in one float, declared.

## The problem, with evidence

- `modules/combat/fight.py:115-117` returns a `dict`. `engine/season/seam/wrappers/combat.py:403-423`
  wraps it in a second dict of twelve keys. The fold reads two, `wound_state` and `surrender`
  (`loop/effects_combat.py:56-58`, `:157`, `:322`). Grep for non-test readers of `winner`, `bouts`,
  `unresolved`, `seed`, `parties` under `engine/season`: none. Siblings return typed records
  (`modules/social_contest/roll.py:157` → `Margin`; `modules/settlements/subsist.py:40` →
  `SubsistOutcome`).
- `winner` contradicts the scene: 11 of 200 hand-built fights (H-119 measured 6.06% of 300), because
  `modules/combat/wrapper.py:621-624` flips `result` after the felling and leaves the trackers alone.
- The fighter left standing is recorded `undecided` in every decided fight (H-348; 200 of 200).
- The scene's trace is returned and folded nowhere, so the log says that A killed B and never how.
- The workbench (`systems/combat/combat_engine_v1/workbench/server.py`, `trace.py`, `balance.py`) calls
  `wrapper.fight` on `Combatant`s; the loop calls `fight.py` on a `PersonalCombatInput`. The record
  cannot say tradition, techniques, skill axes or disposition, which the engine reads. The trace hook is
  a module attribute rebound by two callers, one of them a threaded HTTP server
  (`workbench/server.py:18`).

## The resolution, decided

### Part A — the outcome is a typed record carrying only what something reads

In `engine/season/queries/inputs.py`, beside `PersonalCombatInput`:

```python
@dataclass(frozen=True)
class PartyWounds:            # one party's lifted tracker, in `rosters.yaml: wound_quantities` order
    felled: bool
    wounds: int
    max_wounds: int
    health_remaining: int
    health_full: int

@dataclass(frozen=True)
class Surrender:              # the scene's `yield` event, as `surrender_of` lifts it today
    by: str
    turn: int
    accepted: bool

@dataclass(frozen=True)
class DecisiveBeat:           # the wound that ended it, read off the trace's last felling `wound` event
    by: str                   # the striker's id
    victim: str
    source: str               # wrapper's own site names: exchange | bind | stophit | pursuit | displace_graze
    weapon: str               # the striker's weapon key at that beat
    turn: int

@dataclass(frozen=True)
class CombatOutcome:
    claimants: tuple                  # (A, B), as the input
    wounds: Mapping[str, PartyWounds] # keyed by claimant id; a party with no tracker is absent (the host refuses)
    surrender: Optional[Surrender]
    beat: Optional[DecisiveBeat]      # None when nobody was felled
    turns: int
    trace: tuple                      # the scene's events, for a viewer; folded nowhere
```

- `modules/combat/fight.py::fight` returns `CombatOutcome`. It builds `PartyWounds` from the fields the
  input names, as `_lift` does now; a field the tracker lacks still refuses in the host by name.
- `seam/wrappers/combat.py::resolve` returns `dict(status="RESOLVED", module=…, resolver="d_sigma",
  wound_state=…, surrender=…, beat=…, turns=…, trace=…)`. `winner`, `result`, `unresolved`, `bouts`,
  `parties` and `seed` are deleted (ladder rung 2: no reader). `fight_estimate` reads `wounds` and
  `surrender` off the record. The integer `wrapper.fight` returns is no longer lifted; the upset flip
  therefore has no season-side surface at all, which is what the 2026-09-04 ruling already made true.
- `rosters.yaml: fight_endings` gains `standing`. `loop/effects_combat.py::fight_ending` returns
  `standing` for a party who is neither felled nor the yielder when the other party is; `undecided`
  only when neither is. **Declared hash mover** for every log that carries the field.
- `loop/effects_combat.py::_eff_kill`: a felled party's Subject carries
  `Observation(victim, "fell_to", f"{beat.source}:{beat.weapon}")` beside what it carries now, on
  `CP-T04-01`'s `broke_observed` precedent (an Event has no payload, so a cause rides `Event.observed`).
  `[ASSUMPTION; medium; Jordan to correct; revert: drop the Observation]`. **Declared hash mover** for
  every log with a felling.

### Part B — one door

- `PersonalCombatInput` gains four fields, each defaulting to `()` so every existing record is the
  record it was: `traditions`, `techniques` (each party's `{name: level}`), `skills` (each party's
  `{axis: bonus}`) and `dispositions`. `fight.py` passes them to `Combatant` as it passes kits. The
  season fills none of them until a carrier exists (`03_PC_person_inputs_content.md`).
- `fight(inp, rng, decide=None, cfg=None, max_bouts=None)`: the two extra parameters are the
  workbench's (a config overlay and a bout cap), forwarded to `wrapper.fight`; the host never passes them.
- `wrapper.fight(..., trace=None)`: the engine binds and restores `_TRACE` itself from the argument, so
  no caller touches the module attribute (the note at `wrapper.py:541-543` already names the rebinding as
  the precedent not to follow). `fight.py` passes a list's `append`.
- `workbench/trace.py::run_traced_fight` and `workbench/balance.py::winrate` build a
  `PersonalCombatInput` and call `modules.combat.fight:fight`; `server.py::_make_fighter` becomes a
  record builder. `workbench/server.py` uses `HTTPServer` in place of `ThreadingHTTPServer` (one trace
  hook, one request at a time).

### Part C — appendix of small edits (each its own commit-sized change)

| id | file (owner) | edit |
|---|---|---|
| R-PC-01 | `engine/season/hole_register.yaml` H-98; `engine/season/requirements.yaml` R-09 | H-98: grade to closed, cite CP-T03-00 (each party is written by his own band, so a decisive win is the victor `Untouched` and a narrow one the victor `Wounded`). R-09 `blocks:` re-pointed from H-98 to the two things that block it for combat: reach and per-person inputs |
| R-PC-03 | `modules/combat/config.py`, the `UPSET_FLOOR` comment | add one sentence: the flip has no effect in a season; the fold reads the trackers |
| R-PC-15 | `hole_register.yaml` H-123 `site:`; `registers/handoffs/HANDOFF_PC.md`; sixteen `designs/audit/` citations in `modules/combat/*.py` | H-123's site to `loop/effects_combat.py`; the handoff names its two documents by bare filename (CLAUDE.md §1); each dead citation rewritten to the bare filename or deleted where the file no longer exists |
| R-PC-16 | `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md`, Status line | "PROPOSED; ratification withdrawn (ED-IN-0351). Its combat build is in the tree (`modules/combat/attributes.py`, `core.py`, `fight.py`) and stands on this unratified design" |
| R-PC-17 | `modules/combat/core.py:135` | `net = roll_net(pool, rng) + SL.net_boost(net_sigma, pool)`. Measured equal to the inline form to one unit in the last place at four points; a golden that moves is re-recorded and said so |
| R-PC-18 | `modules/combat/combat_systems.py` (18 module constants) → `modules/combat/config.py` `CFG` | move `REAR_CLEARANCE_TEMPO_K`, `REAR_CLEARANCE_STR_K`, `RANGE_AVAIL_FLOOR`, `RANGE_COMMIT_PEAK`, `RANGE_COMMIT_FLOOR`, `LEGIB_SWING_ROOM_K`, `STOPHIT_RANGE_K`, `FACING_VOID_K`, `FACING_PROFILE_K`, `FACING_VOID_GAIN`, `MODE_PERC_MIN`, `CLOSE_EFF_GAP_REF`, `CLOSE_EFF_FLOOR`, `MODE_EDGE_MIN`, `MODE_TIP_MIN`, `SELECT_EPS`, `TRUE_TIME_REF`, `ARREST_POB_REF` into `CFG`, values unchanged, readers through `cfg[...]`; re-derive the export with `tools/export_engine_params.py --build`. Functions that take no `cfg` today (`close_efficacy`, `range_utilization`, `_commit_range_factor`) gain it |
| R-PC-20 | `systems/combat/combat_engine_v1/state_graph.py` docstring | state that the graph is reference for the Plan-layer proposal and is not read by `wrapper.engagement` |

## Gate (execution artifacts)

- `engine/season/tests/test_combat_module.py`'s oracle comparison, re-pointed at the record's fields,
  run once at the close.
- Season hashes: seeds 0 to 2 equal to the pre-change hashes with the `standing` value and the
  `fell_to` Observation each reverted; each one moved alone and named in the commit body.
- A workbench trace and an entry call at one seed and one matchup produce identical event lists.
- `python tools/export_engine_params.py --check` green after R-PC-18; the count of `combat_systems.py`
  module-level numeric constants absent from the export is 0.

## Falsifier

- For Part A: any reader of a deleted key (the build fails at that reader); a hand-built fight whose
  log names the felled party `standing`.
- For Part B: one seed at which the workbench's result differs from the entry's on the same record.
- For R-PC-17: the combat goldens under `engine/tests/` and `tests/valoria/r3_identity_golden.json`;
  a moved golden is the finding, re-recorded only with the move stated.

## NERS reading

- N: from above, the fold needs two facts and a cause and receives twelve keys, one of them wrong one
  time in twenty; from below, the engine computes a decisive blow and discards it; laterally, every
  other module's outcome is a record. Removing the change keeps a contradiction on the seam.
- R: the world gains the first statement of how a person died, which the chronicle and a witness's
  telling can carry; the standalone scene and the season scene become the same call.
- S: one shape at every module seam; the trace hook has one owner; one substrate call for the boost.
- E, last: a net deletion on the seam and in the workbench's fighter factory. High.

## Cost class

Small build (Part A and Part B); edits (Part C). Two declared movers.
