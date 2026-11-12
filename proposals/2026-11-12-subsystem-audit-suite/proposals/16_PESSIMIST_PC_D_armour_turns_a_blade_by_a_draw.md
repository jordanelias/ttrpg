# 16 · PESSIMIST · PC · D — armour turns a blade by a draw: the coverage gap is a chance, not an average

## Status: PROPOSED

Source: `audits/16_PESSIMIST_PC.md` §2.3 (F-PES-PC-07). Standing rule: `AUDIT_BRIEF.md` (Jordan,
2026-11-12). Complements `18_DETERMINISM_no_certain_matchup.md` (the riposte at a deciding felling),
which cannot reach the armour cases measured here: a plate mirror has no felling to turn, and a turned
blow against plate is still divided by plate. Reference only (`CLAUDE.md` §0.05); not ratified by being
written.

## What it changes in `engine/season/` at runtime (first)

Nothing in today's realm beyond the draw stream: every person wears `light`, where the reading is
unchanged in distribution (below). It adds one draw per landed blow against any armour, so it is a
**declared hash mover for every world with a fought scene**. It changes outcomes as soon as a `medium`
or `heavy` kit exists (`rosters.yaml: arms_kinds`, empty today).

## The problem (evidence)

`modules/combat/core.py:321-322`, in `_transmit`: `g = COVERAGE_GAP; return t*(1-g) + 1.0*g` with the
comment *"some blows reach a bare zone"*. That is the expectation of a chance event (15% of blows reach
unarmoured flesh) written as arithmetic; `damage` then applies the penetration knee (`:637-644`) to the
average. The result is that armour never decides whether a given blow bites; it divides every blow.
`pC_armour.py`, 1,500 fights a cell, `PYTHONHASHSEED=0`: an arming sword's Success deals exactly one
value per tier (15, 13, 8, **1**), and the share of Success rolls that draw no blood is 60.5 to 61.9% in
every tier, plate and bare skin alike (it is the defence mode's neutralise coin).

The fixed outcomes that follow (tracker-true):

| matchup (arming swords) | reading |
|---|---|
| light against heavy, equal skill | the plated man felled 0 of 500, 0 of 400 and 0 of 400 in three runs here (0 of 1,000 in the PC audit's E5); unarmoured against heavy, 0 of 1,500 |
| heavy mirror, `death` terms | 99.8% undecided at twelve turns (0% at 200 turns: the cap decides) |
| heavy mirror, `yield` terms | 90.1% undecided; `blood` terms 39.5% undecided |
| faculty 6 in light against faculty 2 in heavy | the novice in plate felled 2.5%; the master felled 59.5% |
| faculty 10 in light against faculty 2 in heavy | the novice felled 22.2%; 74.0% undecided |

The engine's history is right (a mace, an estoc or a half-sworded longsword answers plate: plate
mirrors with those resolve 96.5 to 100%), so the model is sound for a full inventory. The defect is that
the *chance* part of armour was averaged away, which makes the mismatches certainties.

## The resolution, decided (ladder step 1: the standing rule; step 5 for the site)

**The coverage gap is drawn per blow, at the one damage call.** In `core.strike` (the single call-site
for every blow, `:647`), given the scene's `rng`:

- with probability `COVERAGE_GAP` the blow reaches a bare zone: damage is computed against material
  `none` (no resistance, no knee);
- otherwise it meets the harness: damage is computed with the gap term absent (`t` alone), and the
  penetration knee applies as shipped.

`_transmit` keeps its averaged form for the callers that *rank* (`select_mode`'s comparator,
`cut_thrust_arm`, `adef_cap`): choosing a head on expected coupling is a fighter's judgment, not an
outcome. Only the landed blow draws. `COVERAGE_GAP` stays the one constant; no new one is added. The
trace's `wound` event gains `bare: bool`, and a harness blow that rounds to 0 emits `turned` (today
nothing is emitted for it), so "the blade was turned" becomes an event a viewer and the scene record
(`16_PESSIMIST_PC_C`) can carry.

Expectation: equal to today's before the knee; after it, slightly higher against rigid armour (today
the knee divides the averaged blow, here it divides only the harness blow). That difference is the
point: the bare-zone blow is the upset.

## Prototype reading (`pQ2_gap.py`: in-process patch of `core.damage`, per-fight generator, 400 fights a cell)

| matchup | shipped (averaged): A felled / B felled / undecided | gap as a draw |
|---|---|---|
| season default mirror (light) | 47.5 / 52.2 / 0.2; 3.39 turns; 3.21 blows | 47.2 / 52.5 / 0.2; 3.40 turns; 3.19 blows |
| light against heavy | 97.5 / **0.0** / 2.5 | 92.8 / **5.0** / 2.2 |
| light against medium | 73.2 / 26.2 / 0.5 | 69.0 / 30.8 / 0.2 |
| heavy mirror, `death` terms | 0.0 / 0.2 / **99.8** | 15.8 / 15.8 / **68.5** |
| heavy mirror, `yield` terms | 9.2% yield, **90.8** undecided | 53.5% yield, 3.5% felled, **43.0** undecided |
| mace against arming, heavy both | **0.0** / 87.5 / 12.5 | **8.0** / 79.5 / 12.5 |
| estoc in light against arming in heavy | 25.0 / 75.0 / 0.0 | 24.0 / 76.0 / 0.0 |
| faculty 6 in light against faculty 2 in heavy | 59.5 / **2.5** / 38.0 | 47.8 / **33.2** / 19.0 |

Controls: the light mirror is unchanged (the gap term against cloth is small and the knee is inert);
the estoc, which already defeats plate, is unchanged. Bare-zone share of blows on armour: 14.4 to 15.3%
in every cell. A first attempt, the *knee* as a draw (`pQ_knee.py`), was tested and does not cure it
(light against heavy: 0.0 → 0.2% of 500): the knee is the smaller part of plate's divisor.

What it buys in the words of the premises: armour turns most blades and not all; a blow that gets
through still hurts; skill buys back armour (a master now fells the plated novice a third of the time);
no armour mismatch between swords is certain.

## Exact edits, by owner

| file | edit |
|---|---|
| `modules/combat/core.py::strike` | takes `rng`; draws the bare zone once; calls `damage` with `armor='none'` or with the gap suppressed (a keyword `gap_on=False` threaded to `coupling`/`_transmit`, default `True` so every ranking caller is byte-identical) |
| `modules/combat/core.py::_transmit` | `gap_on` parameter; the comment at `:321-322` restated (the average is for ranking; the blow draws) |
| `modules/combat/wrapper.py` | every `core.strike(...)` call (nine: `:216`, `:248`, `:348`, `:349`, `:354`, `:357`, `:369`, `:393`, `:436`) passes `rng`; `_wound` emits `bare`; a `turned` event where a harness blow deals 0 |
| `systems/combat/combat_engine_v1/workbench/probabilities.py`, `narrate.py` | read `bare` and `turned` `[grep at landing]` |
| `engine/engine_params/combat_engine_v1.json` | unchanged in content (`COVERAGE_GAP` is `core`'s, already exported); `--check` green |

## Gate (execution artifacts)

1. `pC_armour.py` C1 re-run: a Success against `heavy` has more than one damage value, and the share of
   landed blows that draw no blood is higher against `heavy` than against `none` by more than the
   interval.
2. Light against heavy, 1,500 fights: the plated man is felled a share strictly above 0.
3. Control: `COVERAGE_GAP = 0` gives 0 bare-zone blows and the plate mirror returns to undecided; the
   season default mirror's shares stay inside the pre-change interval.
4. The workbench's armour reference (`--drift`) re-recorded and said so.

## Falsifier

After the build, 1,500 light-against-heavy sword fights with no felling of the plated man; or a
`turned` event in a fight between unarmoured men.

## NERS reading

- **N.** Top-down: the standing rule. Bottom-up: the code's own comment states a chance and computes an
  average. Lateral: the mass-battle armour participation reads the same tiers
  (`workbench/armour_participation.py`); it is not changed here and should be checked for the same
  averaging by its lane. Diagonal: the riposte proposal covers decided fights between near-equals; this
  covers the armour mismatch it cannot reach. Cut it and the first plate in the world is an immunity.
- **R.** Completeness: `none` draws nothing; `light` is unchanged in distribution.
- **S.** One constant, one site, the scene's own stream; ranking stays an expectation, outcomes draw.
- **E, last.** No new constant; one parameter and one draw. High.

## Cost class

Small build (one stream mover; a reference re-record).
