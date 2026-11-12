# DICE — the face rule and the band edges as exported facts; the two samplers named for what they are

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — Jordan answered the audit's §11 the other way (A-5: the bell curve everywhere; ED-833 stands for every system). Edits A and D stand (`BAND_FLOORS`; the per-die pair asserted against `FACE_NET`; `LEVEL_SIGMA` exported). **Edit B's wording and Edit C's three-name vocabulary are withdrawn**: there is one sampler and one resolver name. `FACE_NET` is the derivation of the per-die pair, not a dealt rule. The move is `U5a_DICE_owed_edits.md` §1.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.3 and §2 row A-5 (Edits B and C, `Problem` item 3 and the ED-833 paragraph are removed: A-5 settled the question, one sampler, one resolver name `d_sigma` by `U5a_DICE_owed_edits.md` §1 row 7; the gate and falsifier lose their B/C clauses), `U3_CONFLICT_LEDGER.md` C3-L1 (the margin is quantised once at the ladder to integer milli-units, so `BAND_FLOORS` is held in milli-units beside one exported scale constant `MARGIN_SCALE = 1000`; `04:903` and D-29 hold as written); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`).

**Depends on:** `U5a_DICE_owed_edits.md` §1 (B05: the one sampler, the quantised margin) and `10_DICE_one_roller_one_fraction_rule.md` (B05, before it).
**Lands in batch:** B05 (`B05-one-roll`, IN), after `10_DICE_one_roller_one_fraction_rule.md` Edit C, before CAP Part B.

## Status: PROPOSED

Carries findings F-DICE-05 and F-DICE-09 of `../audits/10_DICE_audit.md`. Lane: IN (the dice engine and
its exporter); cross-listed to GO (the port reads the artifact).

## What it changes in `engine/season/` at runtime

Nothing. No draw, band or hash moves. Two facts the game computes with (which face scores what, now the
derivation of the per-die pair only; where the four bands fall) move from function bodies into module-scope
literals that the existing exporter already reads. The effect is on the port and on any odds display, not on
the Python loop.

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
3. *(Removed, W3-1: the first text's item 3, that the whole-dice and continuous samplers grade differently
   at the integers, is moot under A-5: the bell curve is every provider's sampler, `U5a_DICE_owed_edits.md` §1.)*

## The resolution, decided

Ladder step 5 for (1) and (2): the architecture's own rule (§0.05, *a fact the engine uses must live
where code reads it*) and Layer 1's row 181 name the edit.

*(Removed, W3-1: the first text's handling of (3) and its ED-833 paragraph, "Jordan's to confirm", are
answered by A-5: ED-833 stands for every system.)*

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

# Where the bands fall, as margins: Partial from 0, Success from 1, Overwhelming from 3, held in the
# ladder's integer milli-units (W3-1, C3-L1: the margin is quantised once, round(MARGIN_SCALE * margin)).
MARGIN_SCALE = 1000
BAND_FLOORS = {"partial": 0, "success": 1000, "overwhelming": 3000}
```

`degree_from_net` converts the real margin once, `m = round(MARGIN_SCALE * margin)`, and compares `m`
against `BAND_FLOORS[...]` (integer comparison; `04:903`, D-29). The exporter picks up `FACE_NET` and `BAND_FLOORS`
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

**B, C.** *(Withdrawn by the U5a head and removed by W3-1: the two docstring corrections and the
three-name resolver vocabulary described two samplers; A-5 leaves one, and the one resolver name is
`d_sigma`, `U5a_DICE_owed_edits.md` §1 row 7.)*

**D. `engine/dice_engine/sigma_leverage.py:103` — the named levels reach the export.**
`tools/export_sim_params.py:226` reads `ast.Assign` only, so an annotated assignment is skipped. Measured
over the exporter's own roots, two module-scope numeric constants are skipped for that reason:
`engine/substrate/stubwire.py::invocations` (a counter, rightly absent) and
`sigma_leverage.py::LEVEL_SIGMA`, the table `minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00` that
`Fixtures.effort_level` names. The edit is at the owner, not the exporter (widening the exporter would
export the counter): `LEVEL_SIGMA: dict[str, float] = {` becomes `LEVEL_SIGMA = {`. `FACE_NET` and
`BAND_FLOORS` above are written unannotated for the same reason.

## The gate (execution artifacts)

1. `python tools/export_sim_params.py --build && python tools/export_sim_params.py --check`: four new
   keys, `engine.dice_engine.FACE_NET`, `engine.dice_engine.BAND_FLOORS`, `engine.dice_engine.MARGIN_SCALE`
   and `engine.dice_engine.LEVEL_SIGMA`; no other row moves.
2. `python -m pytest engine/tests/test_band_odds.py tests/valoria/test_dice_engine_properties.py
   tests/valoria/test_degree_ladder_single_owner.py -q` green; `test_band_odds.py:79`'s edge-swap test
   re-points at `BAND_FLOORS` (it is the falsifier that the ladder reads the table).
3. `PYTHONHASHSEED=0 python -m engine.season.harness.headless --seasons 2 --seed 0`: `CONTENT HASH`
   unchanged.

## The falsifier

Change one entry of `FACE_NET` (say `10: 3`) in a scratch copy: `import engine.dice_engine.dice_engine`
must fail on the assertion. Swap two entries of `BAND_FLOORS`: `band_odds` moves. Sum two quantised margins
in both orders: equal (C3-L1's falsifier; a planted float margin fails it). If any of these does not happen,
a second statement of the fact survives somewhere.

## NERS reading (E last)

- **N.** Cut the export and the port transcribes the two facts every roll depends on by hand; cut the
  assertion and the Normal sampler can drift from the dice. Holds bottom-up (one table) and vertical (the
  Python oracle to the port).
- **R.** No change in play. Completeness of the contract: the resolver named in the registry is the one
  the provider returns.
- **S.** *Calculations consistent in methodology*: one sampler and one ladder, its edges in one exported table.
- **E, as a ratio.** Two tables, one scale and one assertion against one `if` chain and three comparisons.

## Cost class

Edit. No behaviour change; one exporter rebuild.

**Tests and lands (W3-1).** `engine/tests/test_band_odds.py`, `tests/valoria/test_dice_engine_properties.py`,
`tests/valoria/test_degree_ladder_single_owner.py` (gate 2); `test_band_odds.py`'s edge-swap test re-pointed at
`BAND_FLOORS`; new `tests/valoria/test_degree_ladder_single_owner.py::test_quantised_margins_sum_in_either_order`
(C3-L1). Lands: an IN-lane implementation session under `/methodology-execute` with GO review; `sonnet`.
