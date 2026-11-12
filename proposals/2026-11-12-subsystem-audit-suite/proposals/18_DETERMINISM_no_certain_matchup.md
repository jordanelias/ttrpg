# 18 · DETERMINISM · D — no matchup is certain in the season: the upset becomes a blow the trackers record

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §1) — the form is closed by the decision register (the upset happens inside the fight, at the deciding blow); the option not taken stays not taken. Combat already draws from the one sampler; A-31 (longer fights) recalibrates the damage this riposte carries.

## Status: PROPOSED

Source: `audits/18_DETERMINISM_SWEEP.md` C-13; `audits/03_PC_audit.md:332` (*"at season scale heavy
against light is certain (E5: 0 deaths in 1,000); the cap is a workbench scoreboard rule only"*),
F-PC-06. Standing rule: `AUDIT_BRIEF.md` (Jordan, 2026-11-12). Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

Every season `fight`, `accept` or `capture` that reaches a decided result now carries, with the same
probability as today's flip (`UPSET_FLOOR` 0.05), a reversal that the **trackers** record, so the fold
— which reads the trackers, not `result` — sees it: the man who would have been felled lands the
blow instead. Hash mover for every world in which such a fight is decided. Workbench win-rates are
unchanged in distribution (same probability, same point in the fight).

## The problem (evidence)

- `modules/combat/wrapper.py:618-624`: with probability `UPSET_FLOOR` the decided `result` is negated,
  after the felling, and nothing else changes. `config.py` calls it *"the one place the engine
  deliberately OVERRIDES its own emergent outcome … no in-model event corresponding to the reversal"*.
- The season fold reads the per-party trackers (`seam/wrappers/combat.py`; F-PC-06), so the flip never
  reaches a season: heavy against light, 0 deaths of the heavy in 1,000 (03 PC audit, E5). A
  consequential outcome is a fixed function of the matchup at the scale where it matters.
- `config.py`'s own note names the alternative: *"If the design ever wants upsets to be diegetic … the
  in-fight home for them is a critical-opening mechanic, not a post-hoc flip — Jordan's call."*

## The resolution, decided

**Conflict named:** the form of the upset was recorded as Jordan's call (`config.py`, ED-PC-0036;
`03_PC_duel_round_and_approach_B.md:261` and the PC audit §11 item 3). The standing rule (2026-11-12,
later) answers whether: the season must see upsets (ladder step 1). It does not answer the form; this
proposal takes the smallest diegetic form (ladder step 5) and the two options are listed below for the
orchestrator.

- **The riposte.** At the felling that decides a fight, before the trackers are final, draw once on the
  fight's own `rng` (the same draw position the flip uses today, so the stream is unmoved): with
  probability `UPSET_FLOOR` the felling blow is turned — the would-be-felled party lands a counter
  through **the one damage site** (`_wound('riposte', loser, winner, d)`, `d` = the damage the felling
  blow carried), the felling is undone on his tracker (restored to the wound state before that blow),
  and the fight continues from that state (it is not ended by fiat; the riposte may itself fell, or the
  fight may run on and end otherwise). Emitted as `riposte(turn, by)`, an in-model event.
- **Graded and recoverable.** Because the fight continues, the riposte is not a reversed verdict: the
  underdog may fell, wound or merely survive, by the dice that follow. The `result` integer is whatever
  the continued fight ends with; the flip is deleted.
- **Odds.** `UPSET_FLOOR` stays the designer's number (ED-PC-0036), now the chance that a decisive
  blow is turned. The mortal-wound draw (`14_VERBS_PHYSICAL_A` A3) still follows any felling.

Option not taken, for the orchestrator: a per-exchange critical opening inside `core.resolve` (a floor
on the defender's landing chance). It changes every exchange's odds and every calibration figure; the
riposte changes one point per decided fight. Either satisfies the rule; two would not be allowed.

## Exact edits, by owner

1. `modules/combat/wrapper.py:618-624` — the flip deleted; at the deciding felling (the site that sets
   `result`), the riposte as above, through `_wound`; the loop continues.
2. `modules/combat/config.py` — `UPSET_FLOOR`'s comment restated: the chance a deciding blow is turned;
   it moves the trackers.
3. `03_PC_typed_outcome_one_door.md` R-PC-03's comment edit is superseded by edit 2.

## Gate (execution artifacts)

1. The 03 PC audit's E5 probe (heavy against light, 1,000 seeded season fights): the light fighter fells
   or survives the heavy in a share strictly above 0, and the fold's Events show it (`Event.ending`).
2. Workbench: the roster's head-to-head win-rates at n = 1,000 lie within the sampling interval of
   today's (the riposte replaces a same-probability flip).
3. Control: `UPSET_FLOOR = 0` → 0 of 1,000, and every season hash equal to today's tree run at
   `UPSET_FLOOR = 0` (today's `rng.random()` at `wrapper.py:622` is called on every decided fight
   whatever the floor, so the riposte must keep that one call in the same position; read at
   `wrapper.py:622`).

**Declared hash movers:** every world with a decided season fight.

## Falsifier

A `riposte` event whose trackers do not change; a season run in which the light fighter never prevails
in 1,000 mismatches at `UPSET_FLOOR` 0.05.

## NERS reading

- **N**: the designer's 95 % cap was meant to make no matchup certain; at the season it does not; this
  makes it do so.
- **R**: a lucky blow becomes a story the witnesses carry; a feared champion can fall.
- **S**: one damage site, one draw position, one outcome the fold reads; the workbench and the season
  agree.
- **E** (last): one deleted line, one call through an existing function.

## Cost class

Small edit in `modules/combat/wrapper.py`; re-pin of combat goldens.
