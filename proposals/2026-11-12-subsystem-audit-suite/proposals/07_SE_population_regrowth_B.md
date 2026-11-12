# 07 · SE — a population that comes back: the rising arm of a cohort's weight, on the bodies clock at MATTER (supersedes one clause of `07_SE_population_census.md`)

Reconciled: 2026-11-12, U5d closure — folded **A-51** and **A-55**. Regrowth is a cohort's weight rising on the bodies clock at MATTER; it is not a births-and-ageing pass (none is ordered) and it re-peoples only places on the fixed map (A-55). The five-year prologue (A-51) runs this rule for its twenty seasons like any other, so a world's starting weights are the prologue's result, not the authored row alone; the gate's first reading is taken after the prologue.

## Status: PROPOSED

**Revised by its own lane before return (2026-11-12).** The first draft put the rising arm at CENSUS.
Layer 1 forbids that: §29 (`architecture/holonic_ARCHITECTURE.md:1023-1029`) makes CENSUS *"DEMAND-DRIVEN
ONLY. Nothing generates without a demand, and no clock generates anything"*, and a rise that waits
`regrow_seasons` quiet seasons is a clock. The bodies clock's licensed step is MATTER (§25, `:850-866`:
*"bodies, ageing, natural death — one of the three licensed clocks"*; *"envelope weight — births and
deaths"*; §10.3, `:401-405`: births are written at MATTER and reconciled at CENSUS). §1, §3, §4, §5 and §6
below are the corrected text; the decision (R-SE-26) and its bounds are unchanged.

Carries finding F-SE-18 and resolutions R-SE-26 and R-SE-27 of `audits/07_SE_audit_addendum_B.md`. It
supersedes **only** resolution R4 of `proposals/07_SE_population_census.md` (*"whether a cohort's weight
may also rise is not decided here"*) and closes the first audit's survivor S-SE-1. That proposal's
per-head loss, its thinning, its `empty` band and its asymmetry sweep stand. Nothing is ratified by being
written.

## 1. What changes in `engine/season/` at runtime

With the shipped fixture (`regrow_seasons: 0`): nothing; the branch writes nothing and every hash is the
base. With it on: at MATTER, in the bodies-clock pass that already runs after the hunger fall, a cohort
that is whole, was fed in full this season, has gone a stated number of seasons without loss and lives
where there is room gains one weight and emits `weight.changed`. Nothing else moves. No person is minted,
no verb is added, CENSUS is untouched.

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

**R-SE-26. Weight may rise, by the bodies clock, bounded as ruled.** At MATTER, after the hunger fall,
a cohort gains 1 weight when all of: (i) its body stands at `condition_scale` (it is whole); (ii) neither
a `body.changed` fall nor a `weight.changed` was written on it in the last `regrow_seasons` seasons;
(iii) the settlement it resides in has room for one more (`population < capacity`, the ruled bound);
(iv) this season's draw was met in full (matter, the other half of the ruled bound). Ladder steps 1 and 3.
Step: MATTER, because a birth is the bodies clock (Layer 1 §25, §25.1) and CENSUS may run no clock (§29). `regrow_seasons` is a fixture
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

**(a) `engine/season/loop/matter.py`**, in the bodies-clock section (`:713` on, *"THE BODIES CLOCK:
AGEING AND ILLNESS (v9 IN-34)"*), as its own guarded block after the hunger fall (`:690-711`) and before
or beside the ageing hazard. Placing it there answers the first draft's open question for free: this
season's shortfall is already in hand as `short_by_person` (`:666`, `w._subsistence_shortfall`), and the
hunger pass has already removed anyone who starved, so a cohort cannot die and grow in one barrier.

```python
    regrow = w.fixtures.get("regrow_seasons")           # 0 is the control: no read, no write
    if regrow:
        scale = w.fixtures.get("condition_scale")
        homes = world_q.residence_of(w)
        fell = {f.pid for f in sub.falls}
        for pid in sorted(w.persons):
            p = w.persons[pid]
            home = homes.get(pid)
            if not p.is_cohort or home is None or p.body < scale:    # the carrier's one owner of the test
                continue
            if pid in short_by_person or pid in fell:                  # matter: fed in full this season
                continue
            if world_q.quiet_since(w, pid, ("body.changed", "weight.changed")) < regrow:
                continue
            if world_q.population(w, home, homes) >= world_q.capacity(w, home):   # the ruled room bound
                continue
            prior = w.last_emission_of("weight.changed", pid, written=True)
            w.write("weight", token, lambda p=p: setattr(p, "weight", p.weight + 1),
                    record_kind="Person", fieldname="weight", driver="Event",
                    emits="weight.changed", subject=pid, causes=[prior] if prior else [ROOT])
```

`quiet_since` (seasons since the newest written Event of the named kinds on the subject, or since tick 0)
is one small reader in `queries/world_q.py`, beside `body_hazard` (`:1248`), the bodies clock's existing
Query; it stores nothing. `residence_of` (`:1716`), `population` (`:1786`) and `capacity` (`:1856`) are
the readers `migrate`'s `has_room` (`:1884`) already uses: the same room, no second ladder. A first
regrowth with no prior `weight.changed` is the clock's genuine first emission, the one lawful `[ROOT]`
(P2's own note). Placement follows the precedent of the ageing hazard: a host Query plus one writer in
`matter()`, not a module outcome, because every operand is a host read (the Event log, residence, room).

**(b) `engine/season/write_matrix.yaml`**, the `(Person, weight)` row (`:300-306`): `steps: [CEN]`
becomes `steps: [MAT, CEN]`, `class: MATTER` and `social: false` unchanged, and its `by:` cell gains the
ground: Layer 1 §25 (*"envelope weight — births and deaths"* at MATTER; bodies a licensed clock) and §29
(no clock at CENSUS). The sibling `(Rung, envelope)` row (`:375-381`) already carries `[MAT, CEN]` on
DR-1; this is the same shape for the quantity that carries a cohort's population. Without the cell the
write raises at the gate, which is the matrix doing its job.

**(c) `engine/season/data/fixtures.py`**: `regrow_seasons=0`, with H-49's register row gaining the arm
beside the first proposal's `famine_loss`.

**(c′) A note for the builder of `07_SE_population_census.md` R2 (not superseded here).** Its thinning
branch is a death by hunger, and §25's table puts *"births and deaths"* of envelope weight at MATTER
too; the falls it reacts to (`sub.falls`) are in hand at `:690-711`, not at CENSUS. The first proposal's
own phrase, *"one writer of `(Person, weight)`, two branches"*, is kept by moving both branches into
`matter()`; CENSUS then keeps only what §29 gives it (demand-driven individuation and reconciliation).
Whether that move is made is the first proposal's builder's call; this proposal does not depend on it.

**(d) The asymmetry sweep the first proposal already requires** (`Person.weight` gains a writer where
readers assumed a constant) covers a rising weight with no further edit: every reader it lists
(`larder_draw`'s want, `housing`, `has_room`, the muster cap, `recruit`) is monotone in weight.

**(e) No edit to `modules/settlements/`.** The module reads weights from its input records.

## 5. The gate, and the falsifier

- **Execution artifact.** `engine/season/tests/test_in34_bodies_clock.py` (the bodies clock's own file,
  since the writer now lives in that pass) gains, on `harness/scarce.build` with `regrow_seasons 2` and the hungry cohort fed from tick 0: its
  weight rises by 1 every second season until `population == capacity`, then stops; build a dwelling
  there and it rises once more. Each rise emits `weight.changed`; `|w.persons|` is unchanged throughout.
- **The two arms together** (`famine_loss 500`, `regrow_seasons 2`): starve the cohort for three
  seasons, then feed it. Its weight falls, then returns. This is the first reading in the settlement
  layer of one quantity whose two arms both execute.
- **Falsifier.** A rise in a season the cohort was short; a rise past capacity; a rise within
  `regrow_seasons` of a fall; any change in the count of persons; any `weight.changed` written with
  `w.step == Step.CENSUS` by this branch. Mutation: drop clause (iii) and the capacity assertion reds;
  remove `MAT` from the `(Person, weight)` cell and the write raises at the gate.
- **Control.** `regrow_seasons 0` reproduces the shipped hashes.
- **On the realm** (a reading, not a pass condition): population at season 12 under `ground`, seeds 0 to
  2, with both arms on, against both arms off.

## 6. What this does not cross

ED-WR-0011 (a closed authored cast, *"for now"*): no `Person` is created; the count of persons is
asserted constant. ED-IN-0255 (only cohorts eat): untouched. L4 (no social quantity at MATTER): a
cohort's weight is a body count, `social: false` on its matrix row, and births are named in MATTER's own
table (§25). §29 (no clock at CENSUS): honoured, which is why the write is not there. The engine's refusal
of unwound clocks (`05_COLLISIONS_AND_RESIDUE.md` rows 5 and 16) is honoured: the bodies clock is the one
the same file licenses, and §25.1 lists it among the three that are exhaustive.

## 7. NERS reading (definitions: `CLAUDE.md` §0.06; E last)

- **N.** Cut it and a famine, a lost field and a levy each spend the realm for good; long runs hollow
  out, which is the regime two earlier methods found on the retired mechanics and one ruling answered.
  Bottom-up it is one branch of one writer; top-down it is what makes `found` and `build` matter;
  laterally it is the supply of the muster (`07_SE_campaign_supply_and_muster.md`); across scales a
  duchy's strength recovers at the pace its towns are fed and housed.
- **R.** A lord's neglect becomes reparable at a price in seasons, so governing well is distinguishable
  from governing badly over time. With no player, settlements breathe. Completeness: the arm stops at
  capacity and at shortfall; it cannot run away because its bound is the ruled one.
- **S.** One writer at the barrier Layer 1 names for births (MATTER), in the pass that already runs the
  bodies clock; the same capacity Query `migrate` reads; the same shortfall hunger writes. No second
  ladder.
- **E, last.** One branch, one new reader, one fixture, one matrix cell. "Fed, housed and left in peace, they multiply" is a
  rule a player predicts without being told.

## 8. Cost class

Small build, buildable before or after the first proposal's thinning (it shares no writer site with it
unless (c′) is taken). Hash EQUAL at the shipped arm; the flip a declared
mover.
