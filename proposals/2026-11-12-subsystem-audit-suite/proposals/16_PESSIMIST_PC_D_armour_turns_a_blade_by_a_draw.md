# 16 · PESSIMIST · PC · D — armour turns a blade by a draw: the coverage gap is a chance, not an average

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.5) — order only. It is the third step of the one combat calibration batch (after the damage scale, A-31, and the commit window) and shares its single re-record (`U5b_PC_rulings_in_the_fight.md` §5 row 5). Its `rng` argument to `core.strike` is the round's private stream once `03_PC_duel_round_and_approach_B.md` step 2 lands; the roster census that gates an inventory (`U5b_PC_residue.md` §3) is run after it.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS; the draw key fixed as PC_A's: U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "the riposte" (`18_DETERMINISM_no_certain_matchup.md`) → "the riposte" (glossary *riposte*). A-101 round lane (2026-11-12, `master/pc_round/PC_ROUND_SPEC.md`, glossary §K): "twelve turns" and every fight length "in turns" here are **rounds** (the engine's round budget, `max_bouts=12`, rename PCR-3); the title's "turns" (armour turns a blade) is the ordinary verb and stays.
A-30), §7/§7b (tests extend an existing file, tier); U3 B15, §9 (the duel round's "stream → key": the `rng` the head
line calls the round's private stream is a keyed `Draw`, not a threaded generator), §6.2 (`pC_armour.py`, `pQ2_gap.py`,
`pQ_knee.py` are not in the repository); U1 glossary *faculty* (retired as a suite word: "trained score" in the
tables). Changed: the resolution's draw wording, the edits table's `strike` signature, the gate's test names, two table
labels. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "trained score/rank" → skill score (3).

## Status: PROPOSED

Lands in batch: **B15** (PC; the calibration batch), after `16_PESSIMIST_PC_B` and before `18_DETERMINISM_no_certain_matchup.md`
(UPR §5 row 5). Depends on: `engine/dice_engine/draw.py` (B06) for the keyed `Draw`; the A-31 damage scale (B15).

Source: `audits/16_PESSIMIST_PC.md` §2.3 (F-PES-PC-07). Standing rule: `AUDIT_BRIEF.md` (Jordan,
2026-11-12). Complements `18_DETERMINISM_no_certain_matchup.md` (the riposte at a deciding felling),
which cannot reach the armour cases measured here: a plate mirror has no felling to turn, and a turned
blow against plate is still divided by plate. Reference only (`CLAUDE.md` §0.05); not ratified by being
written.

## What it changes in `engine/season/` at runtime (first)

Nothing in today's realm beyond the draw stream: every person wears `light`, where the reading is
unchanged in distribution (below). It adds one draw per landed blow against any armour, so it is a
**declared hash mover for every world with a fight**. It changes outcomes as soon as a `medium`
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
| skill score 6 in light against score 2 in heavy | the novice in plate felled 2.5%; the master felled 59.5% |
| skill score 10 in light against score 2 in heavy | the novice felled 22.2%; 74.0% undecided |

The engine's history is right (a mace, an estoc or a half-sworded longsword answers plate: plate
mirrors with those resolve 96.5 to 100%), so the model is sound for a full inventory. The defect is that
the *chance* part of armour was averaged away, which makes the mismatches certainties.

## The resolution, decided (ladder step 1: the standing rule; step 5 for the site)

**The coverage gap is drawn per blow, at the one damage call.** In `core.strike` (the single call-site
for every blow, `:647`), given a keyed draw `H(seed, tick, scene id, "gap:<turn>:<blow>")` from the one
keyed-draw owner (A-30; the same shape as PC_A's yield roll), not a generator threaded through the scene:

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
| skill score 6 in light against score 2 in heavy | 59.5 / **2.5** / 38.0 | 47.8 / **33.2** / 19.0 |

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
| `modules/combat/core.py::strike` | takes `draw` (the keyed `Draw` for `"gap:<turn>:<blow>"`); draws the bare zone once; calls `damage` with `armor='none'` or with the gap suppressed (a keyword `gap_on=False` threaded to `coupling`/`_transmit`, default `True` so every ranking caller is byte-identical) |
| `modules/combat/core.py::_transmit` | `gap_on` parameter; the comment at `:321-322` restated (the average is for ranking; the blow draws) |
| `modules/combat/wrapper.py` | every `core.strike(...)` call (nine: `:216`, `:248`, `:348`, `:349`, `:354`, `:357`, `:369`, `:393`, `:436`) passes the keyed `draw` for its turn and blow; `_wound` emits `bare`; a `turned` event where a harness blow deals 0 |
| `systems/combat/combat_engine_v1/workbench/probabilities.py`, `narrate.py` | read `bare` and `turned` `[grep at landing]` |
| `engine/engine_params/combat_engine_v1.json` | unchanged in content (`COVERAGE_GAP` is `core`'s, already exported); `--check` green |

## Gate (execution artifacts)

The probes were lane scratch (not in the repository). `tests/valoria/test_combat_armour_reference.py` (exists) gains
`test_success_against_heavy_has_more_than_one_damage_value` (gate 1), `test_light_against_heavy_plated_man_felled_sometimes`
(gate 2), `test_coverage_gap_zero_gives_no_bare_zone_blows` (gate 3), `test_no_turned_event_between_unarmoured_men`
(the falsifier's second clause). Command: `python -m pytest tests/valoria/test_combat_armour_reference.py -q -m combat`.

1. The `pC_armour.py` C1 reading, committed as gate 1's test: a Success against `heavy` has more than one damage value, and the share of
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

Small build (one stream mover; a reference re-record). Tier: `sonnet`, effort `high`. Hash movers declared: every world
with a fight (one draw per landed blow on armour), in B15's one re-record. Lands it: B15, order `_transmit`'s
`gap_on` (default true, hash-equal) → `strike` takes the keyed draw → the nine call sites → the trace events → the
workbench readers (found by `rg -n "bare|turned" systems/combat/combat_engine_v1/workbench`).
