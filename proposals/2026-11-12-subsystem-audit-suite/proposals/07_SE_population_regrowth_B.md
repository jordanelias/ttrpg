# 07 · SE — a population that comes back: the rising arm of CR-08's CENSUS writer (supersedes one clause of `07_SE_population_census.md`)

## Status: PROPOSED

Carries finding F-SE-18 and resolutions R-SE-26 and R-SE-27 of `audits/07_SE_audit_addendum_B.md`. It
supersedes **only** resolution R4 of `proposals/07_SE_population_census.md` (*"whether a cohort's weight
may also rise is not decided here"*) and closes the first audit's survivor S-SE-1. That proposal's
per-head loss, its thinning, its `empty` band and its asymmetry sweep stand. Nothing is ratified by being
written.

## 1. What changes in `engine/season/` at runtime

With the shipped fixture (`regrow_seasons: 0`): nothing; the branch writes nothing and every hash is the
base. With it on: at CENSUS a cohort that is whole, has gone a stated number of seasons without loss and
lives where there is room gains one weight and emits `weight.changed`. Nothing else moves. No person is
minted, no verb is added, MATTER is untouched.

## 2. The problem, with evidence

- **The first audit escalated a question the ledger had answered.** Its §11 (S-SE-1): *"No design
  document supplies a growth rule; no precedent in the tree settles it."*
  `registers/editorial_ledger_se_archive.jsonl`, ED-SE-0051, last row `ruled` (recorded 2026-09-19 for a
  ruling given 2026-09-17): the question was *"the bound on the demographic loop: matter only, or matter
  plus hearth capacity?"* and the answer **matter plus hearth capacity, a `capacity(w, rung)` Query over
  dwellings with a floor, `found` the throttle, scoped to populations**
  (`proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml` RR-2, `:1838-1845`). The same block
  records that ED-WR-0011's closed-cast ruling *"makes E-1 moot for NPC generation (though not for
  populations)"*. A ruling that chooses what bounds births presupposes births.
- **The intent it bounded is ratified as intent.**
  `proposals/2026-09-10-settlements-factions-populations/00_INDEX.md` (Status: *"P2/P3 → SE-01"*); P2
  (`02_PROPOSALS_SUBSTRATE.md:142-215`) is births scaled by how well the place is fed, deaths raised by
  shortfall, on the licensed bodies clock, with *"no Person exists because time passed"*.
- **The archived design has a rate** (`.designs/…/settlement_layer_v30.md` §1.8c, PROPOSED, intent only):
  recovery of one step per four consecutive stable seasons, to the structural ceiling.
- **A recorded ruling on calibration says so in general.** `settlement_generator_v1.md` §7 item 4 (RULED
  2026-07-13, as that archived file records it): *"every decay needs a growth path"*. ED-IN-0047's own
  row carries Jordan's *"Build the counter to cumulative."*
- **Without it, every binding arm is a ratchet.** The first audit's binding runs end with 19 of 37
  cohorts dead by season 7 (×10, weather on, seed 1) and nothing in the engine that returns a person.

## 3. The resolution, decided

**R-SE-26. Weight may rise, by the bodies clock, bounded as ruled.** At CENSUS, a cohort gains 1 weight
when all of: (i) its body stands at `condition_scale` (it is whole); (ii) neither a `body.changed` fall
nor a `weight.changed` was written on it in the last `regrow_seasons` seasons; (iii) the settlement it
resides in has room for one more (`population < capacity`, the ruled bound); (iv) its last draw was met
in full (matter, the other half of the ruled bound). Ladder steps 1 and 3. `regrow_seasons` is a fixture
(shipped 0, the control; swept `0 / 4 / 8`; 4 is the archived design's figure and is intent, not a
source).

**R-SE-27. Flight is an act, not a barrier write.** The archived design also moves leavers to a
neighbour at Accounting. That half is not built here: births and deaths are a clock nobody winds; *who
leaves, and for where* is a decision, and the engine's rule is that every consequence of a shortfall is
some person's later act. A cohort is a `Person` with a chooser and a `migrate` verb; its flight is that
verb, made reachable by the destination class the first audit already asks for (R-SE-19). A *partial*
flight needs a place to hold more than one cohort (CR-107, held) so that one of several can go; until
then a people leaves whole or stays. No weight is moved between cohorts by any barrier.

**What this does to the capacity ruling's throttle.** `found` and `build` are meant to be the throttle
on growth (ED-SE-0051). They become one the moment a cohort can grow: a settlement at capacity stops
regrowing until someone builds. Today the realm has room (population 120, capacity 212; four settlements
over), so the first effect of the arm is slow growth toward the dwellings that exist.

## 4. The exact edits, by owner

**(a) `engine/season/loop/census.py`**, in the same pass the first proposal's thinning block opens (one
writer of `(Person, weight)`, two branches):

```python
    regrow = w.fixtures.get("regrow_seasons")           # 0 is the control: no write
    if regrow:
        scale = w.fixtures.get("condition_scale")
        homes = residence_of(w)
        draw = subsistence_draw(w)                       # the draw MATTER wrote from this season
        for pid in sorted(w.persons):
            p = w.persons[pid]
            home = homes.get(pid)
            if not p.is_cohort or home is None or p.body < scale:
                continue
            if quiet_since(w, pid, ("body.changed", "weight.changed")) < regrow:
                continue
            if not met_in_full(draw, pid) or population(w, home) >= capacity(w, home):
                continue
            prior = w.last_emission_of("weight.changed", pid, written=True)
            w.write("weight", token, lambda p=p: setattr(p, "weight", p.weight + 1),
                    record_kind="Person", fieldname="weight", driver="Event",
                    emits="weight.changed", subject=pid, causes=[prior] if prior else [ROOT])
```

`quiet_since` (seasons since the newest written Event of the named kinds on the subject, or since tick 0)
and `met_in_full` (every cell of the cohort's draw row has `take == want`) are two small readers in
`queries/world_q.py`; neither stores anything. A first regrowth with no prior `weight.changed` is the
clock's genuine first emission, which is the one lawful `[ROOT]` (P2's own note).
`[UNVERIFIED: the exact name of the reader that returns this season's draw record at CENSUS; the first
audit cites `world_q.subsistence_draw` at `:1273`. If CENSUS runs before MATTER in the season, the read is
last season's draw, which is the ordering P2 defends.]`

**(b) `engine/season/data/fixtures.py`**: `regrow_seasons=0`, with H-49's register row gaining the arm
beside the first proposal's `famine_loss`.

**(c) The asymmetry sweep the first proposal already requires** (`Person.weight` gains a writer where
readers assumed a constant) covers a rising weight with no further edit: every reader it lists
(`larder_draw`'s want, `housing`, `has_room`, the muster cap, `recruit`) is monotone in weight.

**(d) No edit to `modules/settlements/`.** The module reads weights from its input records.

## 5. The gate, and the falsifier

- **Execution artifact.** `engine/season/tests/test_cr08_census_weight.py` (the first proposal's file)
  gains, on `harness/scarce.build` with `regrow_seasons 2` and the hungry cohort fed from tick 0: its
  weight rises by 1 every second season until `population == capacity`, then stops; build a dwelling
  there and it rises once more. Each rise emits `weight.changed`; `|w.persons|` is unchanged throughout.
- **The two arms together** (`famine_loss 500`, `regrow_seasons 2`): starve the cohort for three
  seasons, then feed it. Its weight falls, then returns. This is the first reading in the settlement
  layer of one quantity whose two arms both execute.
- **Falsifier.** A rise in a season the cohort was short; a rise past capacity; a rise within
  `regrow_seasons` of a fall; any change in the count of persons. Mutation: drop clause (iii) and the
  capacity assertion reds.
- **Control.** `regrow_seasons 0` reproduces the shipped hashes.
- **On the realm** (a reading, not a pass condition): population at season 12 under `ground`, seeds 0 to
  2, with both arms on, against both arms off.

## 6. What this does not cross

ED-WR-0011 (a closed authored cast, *"for now"*): no `Person` is created; the count of persons is
asserted constant. ED-IN-0255 (only cohorts eat): untouched. L4 (no social quantity at MATTER): the
write is at CENSUS, on a quantity Layer 1 gives CENSUS. The engine's refusal of unwound clocks
(`05_COLLISIONS_AND_RESIDUE.md` rows 5 and 16) is honoured: the bodies clock is the one the same file
licenses.

## 7. NERS reading (definitions: `CLAUDE.md` §0.06; E last)

- **N.** Cut it and a famine, a lost field and a levy each spend the realm for good; long runs hollow
  out, which is the regime two earlier methods found on the retired mechanics and one ruling answered.
  Bottom-up it is one branch of one writer; top-down it is what makes `found` and `build` matter;
  laterally it is the supply of the muster (`07_SE_campaign_supply_and_muster.md`); across scales a
  duchy's strength recovers at the pace its towns are fed and housed.
- **R.** A lord's neglect becomes reparable at a price in seasons, so governing well is distinguishable
  from governing badly over time. With no player, settlements breathe. Completeness: the arm stops at
  capacity and at shortfall; it cannot run away because its bound is the ruled one.
- **S.** One writer at the barrier Layer 1 names; the same capacity Query `migrate` reads; the same draw
  record hunger reads. No second ladder.
- **E, last.** One branch, two readers, one fixture. "Fed, housed and left in peace, they multiply" is a
  rule a player predicts without being told.

## 8. Cost class

Small build, on top of the first proposal's writer. Hash EQUAL at the shipped arm; the flip a declared
mover.
