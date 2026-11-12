# DICE — the face rule and the band edges as exported facts; the two samplers named for what they are

## Status: PROPOSED

Carries findings F-DICE-05 and F-DICE-09 of `../audits/10_DICE_audit.md`. Lane: IN (the dice engine and
its exporter); cross-listed to GO (the port reads the artifact).

## What it changes in `engine/season/` at runtime

Nothing. No draw, band or hash moves. Two facts the game computes with (which face scores what; where
the four bands fall) move from function bodies into module-scope literals that the existing exporter
already reads, and two docstring claims that are false are corrected. The effect is on the port and on
any odds display, not on the Python loop.

## The problem, with evidence

1. **The two facts every draw depends on are not in the typed layer.** `engine/engine_params/sim_params.json`
   carries six scalars for `engine.dice_engine` (`MU_PER_DIE`, `SIGMA_PER_DIE`, `M_MAX`, `OB_MIN`,
   `SIGMA_N_COEFF`, `TN_STANDARD`; audit §12, E-11). The face rule lives in an `if` chain
   (`dice_engine.py:153-161`) and the band edges `0`, `1`, `3` in comparisons (`:291-306`).
   `tools/export_sim_params.py` reads module-scope literals only, so neither is exported. Layer 1 types
   `seam/ladder` as reading *"the exported band edges"* (`04_CODE_ARCHITECTURE.md:181`); there are none.
   CLAUDE.md §5: until the typed layer covers a value, it reaches Godot by hand transcription.
2. **`MU_PER_DIE` and `SIGMA_PER_DIE` are a second statement of the face rule.** They are literals
   (`0.40`, `0.800`), correct today (probe: mean 0.4, s.d. 0.8 over the ten faces), and nothing derives
   them from the faces, so a face-rule change would leave the Normal sampler and `net_boost` on the old
   pair. `tests/valoria/test_per_die_one_owner.py` pins that `sigma_leverage` reads the owner's pair,
   not that the pair is the faces'.
3. **"Statistically equivalent" is false at the level the game reads.** `dice_engine.py:222` and
   `sigma_leverage.py:420` say the continuous engine is statistically equivalent to the discrete one, and
   `:420` adds *"Canonical for Godot"*. The first two moments agree. The bands do not: the ladder reads
   `margin >= 0`, and a Normal has no mass at the integers, so the continuous sampler is half a success
   harder. Probe (audit §12, E-06), Failure share, discrete against continuous: pool 6 / Ob 3, 53.04 %
   against 62.03 %; pool 8 / Ob 3, 38.58 % against 46.48 %; pool 11 / Ob 4, 37.31 % against 44.01 %.
   Sampled at seed 7, n = 200,000, pool 8 / Ob 3: 38.59 % against 46.42 %. A Normal shifted by +0.5
   reproduces the discrete bands within a point. Combat is tuned on the continuous sampler
   (`modules/combat/core.py:62`); the social roll and `band_odds` are the discrete one. A port that took
   *"canonical for Godot"* as covering the social roll would deal odds 7 to 12 points below the ones
   `band_odds` shows.

## The resolution, decided

Ladder step 5 for (1) and (2): the architecture's own rule (§0.05, *a fact the engine uses must live
where code reads it*) and Layer 1's row 181 name the edit.

For (3) the offset is left in place. Combat's balance is measured on its sampler, no surface compares a
duel exchange's odds with a social roll's (their pools already differ: `faculty + 6` against
`faculty`), and re-centring the sampler would move every combat golden for a comparability nobody
reads. What is corrected is the claim, and the port is told which sampler each provider draws from by a
field code reads.

**This part touches a Jordan decision and is therefore also listed in the audit's §11.** ED-833
(2026-05-15, `jordan_decision`: *"adopt continuous engine; canonical for videogame implementation"*)
made the Normal sampler the videogame's specification for every system, on a validation of mean and
standard deviation at pools 5 to 17 (deviation 0.029 and 0.022). The season's social roll was built
later on whole dice (ED-SC-0037, 2026-09-09: *"we have the sigma leverage d10 resolver in engine to
use"*; `roll.py:165` calls `roll_net`), and B10-08, ratified on merge, built the exact odds function
and the fraction rule on those whole dice. The decided reading here is ladder step 1: for the social
roll the later, specific, ratified build governs, so *"canonical for Godot"* is narrowed to the
provider that draws from the Normal sampler. Because that narrows ED-833 it is Jordan's to confirm; the
other option (every provider samples the Normal, as ED-833 says) is stated in §11 with what it costs.
Edits A, C and D below do not depend on the answer; edit B's second sentence does.

## The edits

**A. `engine/dice_engine/dice_engine.py`.**

```python
# The d10's faces and what each scores. THE face rule; `_die_result` reads it and nothing else spells it.
FACE_NET = {1: -1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 1, 10: 2}

def _die_result(face: int) -> int:
    return FACE_NET[face]

# Per-die mean and s.d., DERIVED from the faces (0.4 and 0.8 exactly at the shipped rule).
MU_PER_DIE = sum(FACE_NET.values()) / len(FACE_NET)
SIGMA_PER_DIE = math.sqrt(sum((v - MU_PER_DIE) ** 2 for v in FACE_NET.values()) / len(FACE_NET))

# Where the bands fall, as margins: Partial from 0, Success from 1, Overwhelming from 3.
BAND_FLOORS = {"partial": 0, "success": 1, "overwhelming": 3}
```

`degree_from_net` compares against `BAND_FLOORS[...]`. The exporter picks up `FACE_NET` and `BAND_FLOORS`
as collections of numbers; `MU_PER_DIE` and `SIGMA_PER_DIE` stop being literals, so they leave
`sim_params.json` as scalars. To keep them exported, the exporter's record for a derived constant is the
evaluated value with `kind: derived` (one branch in `tools/export_sim_params.py::_literal`'s caller, or,
cheaper, two literal lines kept beside an import-time assertion that they equal the derivation). The
cheaper form is taken: keep `MU_PER_DIE = 0.40` and `SIGMA_PER_DIE = 0.800` as literals and add

```python
assert abs(MU_PER_DIE - sum(FACE_NET.values()) / 10) < 1e-12 and \
       abs(SIGMA_PER_DIE ** 2 - sum((v - MU_PER_DIE) ** 2 for v in FACE_NET.values()) / 10) < 1e-12, \
       "the per-die pair is the face rule's; change them together"
```

at module scope, so the pair cannot drift from the faces and the export is unchanged for the two scalars.

**B. The two docstrings.** `dice_engine.py::continuous_engine_sample`: *"Same mean and variance as the
whole-dice roll. NOT the same bands: under the margin ladder it reads about half a success harder (no
mass at the integers). Personal combat is tuned on it; the social roll and `band_odds` are the whole-dice
roll."* `sigma_leverage.py::roll_net_continuous`: the sentence *"Canonical for Godot; statistically
equivalent to the discrete engine"* is replaced by *"The sampler personal combat draws from. The port
uses it where the Python provider does and nowhere else."*

**C. Which sampler a provider draws from, where code reads it.** `references/module_contracts.yaml`
already carries `resolver:` per module, and the three wrappers return it (`combat.py:403` `d_sigma`,
`mass_battle.py:410` `dice_pool`, `sigma.py:110` `d10_sigma`). The social contest contract row says
`dice_pool` while its provider returns `d10_sigma`, and the combat row's comment still says *"base Ob 3
FIXED"* and names `sim.autoload.sigma_leverage`. One vocabulary of three, each a statement of sampler and
advantage: `d10_whole` (whole dice, sigma boost, margin ladder: social contest), `d10_normal` (Normal
sampler, sigma boost, margin ladder per exchange: combat), `d10_whole_cells` (whole dice per cell, sigma
boost: mass battle). The contract rows and the three wrapper strings are set to match;
`tools/export_composition.py --check` is the round-trip that already covers the file.

**D. `engine/dice_engine/sigma_leverage.py:103` — the named levels reach the export.**
`tools/export_sim_params.py:226` reads `ast.Assign` only, so an annotated assignment is skipped. Measured
over the exporter's own roots, two module-scope numeric constants are skipped for that reason:
`engine/substrate/stubwire.py::invocations` (a counter, rightly absent) and
`sigma_leverage.py::LEVEL_SIGMA`, the table `minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00` that
`Fixtures.effort_level` names. The edit is at the owner, not the exporter (widening the exporter would
export the counter): `LEVEL_SIGMA: dict[str, float] = {` becomes `LEVEL_SIGMA = {`. `FACE_NET` and
`BAND_FLOORS` above are written unannotated for the same reason.

## The gate (execution artifacts)

1. `python tools/export_sim_params.py --build && python tools/export_sim_params.py --check`: three new
   keys, `engine.dice_engine.FACE_NET`, `engine.dice_engine.BAND_FLOORS` and
   `engine.dice_engine.LEVEL_SIGMA`; no other row moves. The three wrapper strings of edit C are pinned
   by `engine/season/tests/test_season_shape.py:9759`, `test_social_contest_module.py:108` and
   `test_sc01_speak.py:208`, which re-pin in the same commit.
2. `python -m pytest engine/tests/test_band_odds.py tests/valoria/test_dice_engine_properties.py
   tests/valoria/test_degree_ladder_single_owner.py -q` green; `test_band_odds.py:79`'s edge-swap test
   re-points at `BAND_FLOORS` (it is the falsifier that the ladder reads the table).
3. `PYTHONHASHSEED=0 python -m engine.season.harness.headless --seasons 2 --seed 0`: `CONTENT HASH`
   unchanged.

## The falsifier

Change one entry of `FACE_NET` (say `10: 3`) in a scratch copy: `import engine.dice_engine.dice_engine`
must fail on the assertion, `band_odds(2, 2)` must change, and `roll_pool` must deal the new value. Swap
two entries of `BAND_FLOORS`: `band_odds` moves. If any of the three does not happen, a second statement
of the fact survives somewhere.

## NERS reading (E last)

- **N.** Cut the export and the port transcribes the two facts every roll depends on by hand; cut the
  assertion and the Normal sampler can drift from the dice. Holds bottom-up (one table), vertical (the
  Python oracle to the port) and lateral (three providers named by one vocabulary).
- **R.** No change in play. Completeness of the contract: the resolver named in the registry is the one
  the provider returns.
- **S.** *Calculations consistent in methodology*: the difference between the two samplers is stated
  where it is read instead of denied; a display can then show the right odds for the right provider.
- **E, as a ratio.** Two tables and one assertion against one `if` chain and three comparisons; three
  strings reconciled.

## Cost class

Edit. No behaviour change; one exporter rebuild.
