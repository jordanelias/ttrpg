# 18 · DETERMINISM · D — no matchup is certain in the season: the upset becomes a blow the trackers record

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §1) — the form is closed by the decision register (the upset happens inside the fight, at the deciding blow); the option not taken stays not taken. Combat already draws from the one sampler; A-31 (longer fights) recalibrates the damage this riposte carries.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row no_certain_matchup, §2 row head and "Option not taken", §7, 7b; `unified/U3_DEPENDENCY_ORDER.md` §1 item 15, §3.1, §4.1 rows 51, 58; `unified/U1_GLOSSARY.md` "riposte"). Changed: (1) the riposte's draw is keyed `H(seed, tick, scene id, "upset:<turn>")` through the one `Draw` owner (A-30; B06), replacing "the same draw position the flip uses today", an ordinal-stream argument A-30 retires; gate 3's control is restated for a keyed draw; (2) the tracker restore is specified (a snapshot taken at the site that sets `result`); (3) "Option not taken, for the orchestrator" is closed by ladder step 5 (this file's own reading; R5 §2): not a Jordan item; (4) the chance is re-read after A-31/A-79 only if the deciding-blow rate changes; (5) the E5 probe becomes a named test in a named file; (6) batch and tier lines. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): U4d first renamed this file's draw at the deciding felling "riposte" → "counterblow", and Jordan reversed it the same day ("it's still a riposte"; ordinary English and the combat module's own fencing riposte, `config.py` `RIPOSTE_ON_FAIL`, name the same kind of event: the struck fighter answers in the same tempo). The word is **riposte** in prose; the proposed code ids carry the trigger: `finalblow_riposte(turn, by)`, `_wound('finalblow_riposte', …)`, `test_combat_finalblow_riposte.py`, `test_finalblow_riposte_event_changes_the_tracker` (Jordan: "call it differently in code for clarity, but do it like finalblow_riposte"). A-101 round lane (2026-11-12, `master/pc_round/PC_ROUND_SPEC.md`): a fight is a sequence of rounds, so the key is `"upset:<round>"` and the event `finalblow_riposte(round, by)` (were `<turn>`, `turn`; the round index is the engine's `turn_start` count, rename PCR-3); "turn" elsewhere in this file for the duel is the round.

Depends on: `03_PC_typed_outcome_one_door.md` (B14; R-PC-03 is superseded by this file, U3 §4.1 row 51); `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (B15; the mortal-wound draw that follows any felling); `16_PESSIMIST_GO_keyed_draw_no_recorder.md` and `11_GO_one_draw_owner.md` (B06, the keyed draw). `03_PC_duel_round_and_approach_B.md` (B16) depends on this file, not the reverse (§4.1 row 58, REV).
Lands in batch: B15 (lane PC), after `16_PESSIMIST_PC_D` and before `16_PESSIMIST_PC_A`; one commit with its test, inside B15's one re-record of the combat goldens.
Tier: sonnet / high.

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
proposal takes the smallest diegetic form (ladder step 5); the option not taken is recorded below as
closed, not as a question.

- **The riposte.** At the felling that decides a fight, before the trackers are final, draw once, keyed
  `H(seed, tick, scene id, "upset:<round>")` through the one `Draw` owner (A-30; B06), so the draw consumes
  no position of the fight's own stream: with
  probability `UPSET_FLOOR` the felling blow is turned — the would-be-felled party lands a counter
  through **the one damage site** (`_wound('finalblow_riposte', loser, winner, d)`, `d` = the damage the felling
  blow carried), the felling is undone on his tracker (the loser's wound state is set to the snapshot
  taken immediately before the deciding blow was applied; the snapshot is taken at the site that sets
  `result`, `wrapper.py:618-624`), and the fight continues from that state (it is not ended by fiat; the riposte may itself fell, or the
  fight may run on and end otherwise). Emitted as `finalblow_riposte(round, by)`, an in-model event.
- **Graded and recoverable.** Because the fight continues, the riposte is not a reversed verdict: the
  underdog may fell, wound or merely survive, by the dice that follow. The `result` integer is whatever
  the continued fight ends with; the flip is deleted.
- **Odds.** `UPSET_FLOOR` stays the designer's number (ED-PC-0036), now the chance that a decisive
  blow is turned. The mortal-wound draw (`14_VERBS_PHYSICAL_A` A3) still follows any felling. A-31's
  longer fights and A-79's fight obstacle (0.8) change how many blows a fight has, not this chance; the
  floor is re-read after B15's calibration only if the deciding-blow rate per fight changes.

Option not taken (closed at ladder step 5 by this file's reading; not a Jordan item): a per-exchange
critical opening inside `core.resolve` (a floor on the defender's landing chance). It changes every
exchange's odds and every calibration figure; the riposte changes one point per decided fight. Either
satisfies the rule; two would not be allowed.

## Exact edits, by owner

1. `modules/combat/wrapper.py:618-624` — the flip deleted; at the deciding felling (the site that sets
   `result`), the riposte as above, through `_wound`; the loop continues.
2. `modules/combat/config.py` — `UPSET_FLOOR`'s comment restated: the chance a deciding blow is turned;
   it moves the trackers.
3. `03_PC_typed_outcome_one_door.md` R-PC-03's comment edit is superseded by edit 2.

## Gate (execution artifacts)

Tests: NEW `tests/valoria/test_combat_finalblow_riposte.py`, beside `tests/valoria/test_combat_duel_terms.py`
(exists), written as the batch item's first commit:
`test_finalblow_riposte_event_changes_the_tracker`, `test_upset_floor_zero_gives_zero_of_1000_and_pinned_hash`,
`test_light_fells_or_survives_heavy_in_some_season_fights` (the E5 probe as a test, n = 1,000 seeded).

1. The 03 PC audit's E5 probe, now `test_light_fells_or_survives_heavy_in_some_season_fights` (heavy
   against light, 1,000 seeded season fights): the light fighter fells or survives the heavy in a share
   strictly above 0, and the fold's Events show it (`Event.ending`).
2. Workbench: the roster's head-to-head win-rates at n = 1,000 lie within the sampling interval of
   today's (the riposte replaces a same-probability flip), read with
   `systems/combat/combat_engine_v1/workbench/balance.py` (CLAUDE.md §9).
3. Control: `UPSET_FLOOR = 0` → 0 ripostes of 1,000, and the season hash equal to the same tree with the
   riposte branch deleted at `UPSET_FLOOR = 0`. Because the draw is keyed (it consumes no stream
   position), this control holds by construction; the one re-pin is today's flip leaving the stream
   (`wrapper.py:622` calls `rng.random()` on every decided fight), recorded once at B15's close.

**Declared hash movers:** every world with a decided season fight.

## Falsifier

A `riposte` event whose trackers do not change; a season run in which the light fighter never prevails
in 1,000 mismatches at `UPSET_FLOOR` 0.05.

## NERS reading

- **N**: the designer's 95 % cap was meant to make no matchup certain; at the season it does not; this
  makes it do so.
- **R**: a lucky blow becomes a story the witnesses carry; a feared champion can fall.
- **S**: one damage site, one keyed draw, one outcome the fold reads; the workbench and the season
  agree.
- **E** (last): one deleted line, one call through an existing function.

## Cost class

Small edit in `modules/combat/wrapper.py`; re-pin of combat goldens.
