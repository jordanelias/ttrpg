# 07 · SE — a population that can shrink without vanishing: CR-08's CENSUS writer, specified

Reconciled: 2026-11-12, U5d closure — folded **A-56** and **A-15**. The clause leaving growth undecided (§3 R4) is superseded by `07_SE_population_regrowth_B.md` (the register's ladder table: a population may recover, bounded by food and room). Thinning's body loss is drawn on the ladder (A-54; `09_WR_B_draws_not_thresholds.md` edit 2), with `body_step × short // weight` as the Partial band's magnitude. Who leaves is the cohort's own `migrate`, one of its heavy moves (`U5d_SE_cohort_heavy_moves_and_caste.md`). A-15's natural death is of named persons with authored ages; no births or ageing pass is added to a cohort by it (A-51 says so for the prologue).

Reconciled: 2026-11-12, U4 fact check (`unified/U4_FACT_CHECK.md` F-05) — "38 settlements" in §2 counts settlement rungs (37 on the map plus the foreign `set_alt_1`), where every other file's "37 settlements" counts the map's settlements; `build_realm(0)` read at the tree: settlement rungs 38, Sites at 37 of them (`audits/25` L-04). "Population 120" is the sum of `Person.weight`, over 83 persons (read at the tree).

Reconciled: 2026-11-12, wave 3 (W3-3) — C3-C3 and R3 §1 (writer placement): the thinning moves from CENSUS to MATTER's bodies pass, where `sub.falls` is in hand (`loop/matter.py:690-711`), so neither branch of the weight writer is a CENSUS pass polling a floor (`holonic` §29: no clock at census); `04` §A.2 gives `weight` to CENSUS and `holonic` §25/§29 put deaths at MATTER, and the ambiguity is named here and picked by layer-conformance B4 (CENSUS keeps individuation). The matrix row `(Person, weight)` gains `MAT` (`steps: [MAT, CEN]`, the `(Rung, envelope)` precedent, `write_matrix.yaml:375-381`), so the "Grounded" line's "no matrix edit is owed" no longer holds. R3 §2 (A-54): §4 (a) names `09_WR_B_draws_not_thresholds.md` edit 2 as the owner of the drawn loss and keeps the per-head scaling as the Partial band's magnitude. The head's supersession of R4 is carried into the body (R4, the source paragraph). Tier and batch added (R3 7b-0; U3 B12); the test file is written as the batch's first commit (U3 §6.1).

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), after `U5d_SE_owed_edits.md` and before `07_SE_population_regrowth_B.md` (U3 §1 item 13).
Depends on: `09_WR_B_draws_not_thresholds.md` edit 2 (B12, the drawn body loss); `07_SE_population_regrowth_B.md` (B12, the rising branch of the same writer).

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-24) — the `(Person, weight)` matrix row already holds `CEN` (`write_matrix.yaml:300-306`); no matrix edit is owed by this proposal. [Superseded by the wave-3 line above: the row gains `MAT`.]

Carries finding F-SE-02 and resolutions R-SE-04, -05, -06 of `audits/07_SE_audit.md`. It specifies an
open position (CR-08, `workplans/valoria_master_workplan_v11_part4.md:35`) and corrects one query. The
growth half is `07_SE_population_regrowth_B.md`'s (the head; survivor S-SE-1 in the audit's §11 is
answered there).

## 1. What changes in `engine/season/` at runtime

1. `loop/matter.py`'s bodies pass gains the falling branch of the one writer of `(Person, weight)`: a
   cohort whose body stands under a floor after its hunger fall loses weight and emits `weight.changed`;
   its body is not reset.
2. `loop/matter.py`'s hunger pass stops removing a cohort at body 0 while it has weight left to lose;
   the cohort is removed when its weight reaches the floor of 1.
3. `modules/settlements/subsist.py` computes the body loss per head (H-305).
4. `queries/world_q.py::hunger` answers `empty` for a settlement with no cohort under it instead of
   `fed`.

All four ship behind fixtures at today's arms, so every pinned hash is unchanged until a flip.

## 2. The problem, with evidence

- **Population is a constant.** `Person.weight` has a matrix row and no writer (H-49; CR-08). In every
  arm run for this audit the realm's population is 120 at build and 120 at the end (three seasons of
  play at seeds 0 and 1; twenty seasons with no acts), less only the named persons who died.
- **When hunger does bind, a town's people die in one write, whole and for good.** `subsist.py:71-76`
  floors the body at 0 and `matter.py:709-711` calls `_die`. Reading (`se_bind.py 0 8 20 0`): all 37
  cohorts die at season 0; `se_bind.py 1 8 10 1`: 19 of 37 by season 7. Nothing re-peoples a settlement:
  no cohort migrated in any run (`se_who.py 0 2`: cohort `migrate` attempted 51, executed 0).
- **The dead town reads as thriving.** `world_q.hunger` answers `fed` when demand is 0 (its docstring:
  *"A settlement with no cohort under it (D = 0) reads `fed`"*), and `produce.py` reads no person, so the
  town yields at full rate into a larder nobody draws. After the 37 deaths above, realm grain rises
  1,480 → 11,322 over seven seasons and the census reports 38 settlements `fed` (38 settlement rungs: the
  37 on the map and `set_alt_1`, the foreign faction's rung with no Site and no cohort; `audits/25` L-04;
  U4 F-05).
- **The loss scales with headcount, not with how hungry each person is** (H-305):
  `lost = body_step × Σ units short` and `want = weight × Person.weight`, so the same half ration costs a
  weight-2 cohort 30 body and a weight-20 cohort 300.

## 3. The resolution, decided

**R1. Body is per head; the loss is per head.** `lost = body_step × Σ_k short_k // weight`. Ladder step
5: `body` is one 0-to-`condition_scale` quantity shared by an individual and a cohort (S9.1, one class),
read by `decision/budget.py` through one `band_floors["body"]` table; a quantity that is intensive on
every reader cannot be decremented by an extensive amount. `body_step` keeps its meaning (body per unit
of unmet need per head).

**R2. A starving cohort thins before it dies (CR-08's falling half).** At MATTER, in the bodies pass,
right after a cohort's hunger fall is written (C3-C3; R3 §1), for each cohort whose body is under
`band_floors["body"]["withdrawal_only"]`: `weight` falls by `max(1, weight × famine_loss
// 1000)`, floored at 1, emitting `weight.changed` with `causes = [the last `body.changed` written on
it]`. A cohort at weight 1 and body 0 is removed by the existing `_die`. Ladder step 3: this is CR-08's
own text (*"a cohort losing weight when its body floors"*) and M6's taken answer; what is added is the
arithmetic, the cause and the order relative to death.

**R3. Hunger's band roster gains `empty`.** A settlement with no cohort under it is not fed. Ladder step
5: a report that prints the best band for the worst outcome inverts the instrument CR-22's exit reads.

**R4. A cohort's weight may also rise** (decided by `07_SE_population_regrowth_B.md`, the head: bounded
by food and room). The writer in R2 is the falling branch; the rising branch is that file's §4 (c'), in
the same MATTER pass, shipped off.

## 4. The exact edits, by owner

**(a) `modules/settlements/subsist.py`, the `lost` line.** The loss itself is drawn on the four-band
ladder (A-54); the owner of that draw is `09_WR_B_draws_not_thresholds.md` edit 2 (the hungry body
drawn in `subsist`). This edit supplies only the per-head scaling, which becomes the **Partial band's
magnitude** of that draw (`body_step × units // weight`); the code below is the arithmetic at the
shipped control (no draw), kept so the `per_head` arm can be read before the draw lands. `SubsistInput`
already carries the eaters with their weights inside `inp.larder.eaters`.

Old:

```python
    for pid in sorted(short):
        lost = inp.body_step * sum(short[pid].values())
```

New:

```python
    weight_of = {e.pid: e.weight for e in inp.larder.eaters}
    for pid in sorted(short):
        units = sum(short[pid].values())
        lost = inp.body_step * units // weight_of[pid] if inp.per_head else inp.body_step * units
```

`SubsistInput` gains `per_head: bool`, projected by `world_q.subsist_input` from a fixture
`hunger_loss="per_cohort"` (shipped, today's) `/ "per_head"`. At the shipped weight 2 the `per_head` arm
halves every loss, so `body_step` is re-read at CR-22 under it (CR-22 already re-derives `body_step`).

**(b) `engine/season/loop/matter.py`, inside the `for fall in sub.falls:` loop (`:690-711`), after the
body write and before the death test** (C3-C3; not `loop/census.py`):

```python
        loss = w.fixtures.get("famine_loss")        # per-mille of weight; 0 is the control (no write)
        floor = (w.fixtures.get("band_floors") or {}).get("body", {}).get("withdrawal_only")
        if loss and floor is not None and person.is_cohort and person.body < floor:
            after = max(1, person.weight - max(1, person.weight * loss // 1000))
            if after != person.weight:
                w.write("weight", token, lambda person=person, after=after: setattr(person, "weight", after),
                        record_kind="Person", fieldname="weight", driver="Event",
                        emits="weight.changed", subject=pid, causes=[fell.id] if fell else [ROOT])
```

The cause is the `body.changed` just written (`fell`, in hand at `:704`), not a log search. Fixture
`famine_loss=0` in `data/fixtures.py` (swept `0 / 250 / 500`), with its hole-register row (H-49 gains the
arm). **Matrix edit owed:** `engine/season/write_matrix.yaml:300-306`, the `(Person, weight)` row,
`steps: [CEN]` → `steps: [MAT, CEN]` (the `(Rung, envelope)` row's two steps, `:375-381`, are the
precedent); CENSUS keeps individuation. `04` §A.2 lists `weight` under `loop/census` while `holonic` §25
and §29 put deaths at MATTER and bar a clock at CENSUS: the ambiguity is named at this site and picked
(layer-conformance B4); `04` is not edited.

**(c) `engine/season/loop/matter.py:709-711`.**

Old:

```python
        if fall.body_after <= 0:
            # death through the one owner: see _die
            _die(w, token, pid)
```

New: `if fall.body_after <= 0 and (person.weight <= 1 or not w.fixtures.get("famine_loss")):`. With
`famine_loss` 0 the condition is today's.

**(d) `engine/season/rosters.yaml: hunger_bands`.** `values: [starving, hungry, lean, fed, empty]`;
`world_q.hunger` returns `("empty", Fraction(0), 0)` when `D == 0` and no cohort resides under the rung,
and `world_q`'s unpack of first and last members reads `fed` by name rather than by position. The
census line `hunger_by_settlement` then prints `empty` for a depopulated town. `test_hunger.py` gains
the case; its `test_g` limit text is corrected.

**(e) The asymmetry sweep (CLAUDE.md §0.1 pt 1).** `weight` gains a writer where every reader assumed a
constant: list in the commit every reader of `Person.weight` found by grep at the build (`larder_draw`'s
want, `housing`'s population, `has_room`, `sides.py`'s muster weight, `effects_army.py`'s `recruit`,
`seat_guards`' ceiling check) and state for each whether a falling weight is read correctly.

## 5. The gate and the falsifier

- **Execution artifact.** `engine/season/tests/test_cr08_census_weight.py` (new; absent on `main`, written
  as the batch's first commit, U3 §6.1; the name is kept though the writer is at MATTER), on `harness/scarce.build`
  with `famine_loss 500` and `hunger_loss per_head`: the hungry cohort's weight falls 10 → 5 → 3 → 2 → 1
  across the seasons its body stands under the floor, each fall emits `weight.changed` whose cause is a
  `body.changed`, its `demanded` falls with it, and it is removed only at weight 1 and body 0. Control:
  `famine_loss 0` reproduces `scarce.build`'s shipped hash and the cohort dies as it does today.
- **CR-08's own exit** stands: `grep -rn "weight.changed" engine/season` finds the writer.
- **Falsifier.** A cohort under the floor that keeps its weight; a cohort over the floor that loses any;
  a `weight.changed` with `[ROOT]` as cause on a cohort whose body was ever written. Mutation: read
  `p.body <= 0` instead of the floor, and the 10 → 5 step never fires before death.
- **On the realm** (a reading at CR-22's exit, not a pass condition): the count of settlements `empty`
  after eight seasons at the shipped arms, seeds 0 to 2.

## 6. NERS reading

- **N.** Cut the thinning and a famine has two states, untouched and extinct; cut `empty` and extinction
  is invisible. It holds from MATTER (the fall and the write), from the larder (a thinner
  cohort wants less, so a famine damps itself: the first declared damping loop in the economy) and from
  the battlefield (`recruit` and muster read the same weight).
- **R.** The world generates decline with nobody watching, and a governor's delay now costs people
  rather than an abstraction. Completeness: weight floors at 1 and death stays where it was.
- **S.** One writer, at MATTER beside the fall that causes it (the barrier is picked under a named Layer 1
  ambiguity, §4 (b)); the loss uses the band table the body already reads. Two ladders for one quantity are avoided: `body` stays per head everywhere.
- **E, last.** Four small edits. "They went hungry, some died or left, fewer mouths now" is a sentence a
  player can predict.

## 7. Cost class

Small build. Hash EQUAL at the shipped arms; each flip (`hunger_loss`, `famine_loss`) a declared mover.
The `hunger_bands` edit moves no hash (the loop does not read `hunger`); it moves the census text.
Tier: the writer placement was an `opus` decision made once in U3 (C3-C3); the build is `sonnet` (R3 7b-0).
