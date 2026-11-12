# 07 · SE — a population that can shrink without vanishing: CR-08's CENSUS writer, specified

## Status: PROPOSED

Carries finding F-SE-02 and resolutions R-SE-04, -05, -06 of `audits/07_SE_audit.md`. It specifies an
open position (CR-08, `workplans/valoria_master_workplan_v11_part4.md:35`) and corrects one query. The
growth half is not decided here: it is survivor S-SE-1 in the audit's §11.

## 1. What changes in `engine/season/` at runtime

1. `loop/census.py` gains the one writer of `(Person, weight)`: a cohort whose body stands under a floor
   at CENSUS loses weight and emits `weight.changed`; its body is not reset.
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
  1,480 → 11,322 over seven seasons and the census reports 38 settlements `fed`.
- **The loss scales with headcount, not with how hungry each person is** (H-305):
  `lost = body_step × Σ units short` and `want = weight × Person.weight`, so the same half ration costs a
  weight-2 cohort 30 body and a weight-20 cohort 300.

## 3. The resolution, decided

**R1. Body is per head; the loss is per head.** `lost = body_step × Σ_k short_k // weight`. Ladder step
5: `body` is one 0-to-`condition_scale` quantity shared by an individual and a cohort (S9.1, one class),
read by `decision/budget.py` through one `band_floors["body"]` table; a quantity that is intensive on
every reader cannot be decremented by an extensive amount. `body_step` keeps its meaning (body per unit
of unmet need per head).

**R2. A starving cohort thins before it dies (CR-08's falling half).** At CENSUS, for each cohort whose
body is under `band_floors["body"]["withdrawal_only"]`: `weight` falls by `max(1, weight × famine_loss
// 1000)`, floored at 1, emitting `weight.changed` with `causes = [the last `body.changed` written on
it]`. A cohort at weight 1 and body 0 is removed by the existing `_die`. Ladder step 3: this is CR-08's
own text (*"a cohort losing weight when its body floors"*) and M6's taken answer; what is added is the
arithmetic, the cause and the order relative to death.

**R3. Hunger's band roster gains `empty`.** A settlement with no cohort under it is not fed. Ladder step
5: a report that prints the best band for the worst outcome inverts the instrument CR-22's exit reads.

**R4. Whether a cohort's weight may also rise is not decided here** (survivor S-SE-1). The writer in R2
is built so that a rising arm is one more branch of the same function, shipped off.

## 4. The exact edits, by owner

**(a) `modules/settlements/subsist.py`, the `lost` line.** `SubsistInput` already carries the eaters
with their weights inside `inp.larder.eaters`.

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

**(b) `engine/season/loop/census.py`, after the individuation loop.**

```python
    loss = w.fixtures.get("famine_loss")            # per-mille of weight; 0 is the control (no write)
    floor = (w.fixtures.get("band_floors") or {}).get("body", {}).get("withdrawal_only")
    if loss and floor is not None:
        for pid in sorted(w.persons):
            p = w.persons[pid]
            if not p.is_cohort or p.body >= floor:
                continue
            after = max(1, p.weight - max(1, p.weight * loss // 1000))
            if after == p.weight:
                continue
            prior = w.last_emission_of("body.changed", pid, written=True)
            w.write("weight", token, lambda p=p, after=after: setattr(p, "weight", after),
                    record_kind="Person", fieldname="weight", driver="Event",
                    emits="weight.changed", subject=pid, causes=[prior] if prior else [ROOT])
```

Fixture `famine_loss=0` in `data/fixtures.py` (swept `0 / 250 / 500`), with its hole-register row
(H-49 gains the arm). The matrix row `(Person, weight)` gains `CEN` in `steps:` if it does not hold it
[UNVERIFIED: the row's `steps:` cell was not opened; Layer 1 §A.2:179 gives CENSUS `weight`].

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

- **Execution artifact.** `engine/season/tests/test_cr08_census_weight.py` (new), on `harness/scarce.build`
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
  is invisible. It holds from MATTER (the fall), from CENSUS (the write), from the larder (a thinner
  cohort wants less, so a famine damps itself: the first declared damping loop in the economy) and from
  the battlefield (`recruit` and muster read the same weight).
- **R.** The world generates decline with nobody watching, and a governor's delay now costs people
  rather than an abstraction. Completeness: weight floors at 1 and death stays where it was.
- **S.** One writer, at the barrier Layer 1 names for it; the loss uses the band table the body already
  reads. Two ladders for one quantity are avoided: `body` stays per head everywhere.
- **E, last.** Four small edits. "They went hungry, some died or left, fewer mouths now" is a sentence a
  player can predict.

## 7. Cost class

Small build. Hash EQUAL at the shipped arms; each flip (`hunger_loss`, `famine_loss`) a declared mover.
The `hunger_bands` edit moves no hash (the loop does not read `hunger`); it moves the census text.
