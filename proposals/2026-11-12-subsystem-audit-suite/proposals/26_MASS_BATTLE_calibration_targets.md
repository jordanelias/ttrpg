# MB · calibration targets from the sources: what to read, against what band, with what control

## Status: PROPOSED

Lane MB. Carries rows R-1 to R-5, B-10 and B-11 of `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`.
Sources: `research/historical/mass_battle_casualties_and_results_grounding.md` (**CR**),
`…_movement_and_behaviour_grounding.md` (**MV**), `…_wargame_models_grounding.md` (**WG**). Reference, not
mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing. It adds one read-only instrument beside the engine's existing ones and states what its readings
are compared with.

## The problem

- The gauge's bands are a list of matchup win shares with sources cited by DOI and no page read recorded;
  two of its ceilings were raised after the engine exceeded them, and one row reads 100 of 100
  (`research/historical/mass_battle_gauge_grounding.md:70-72`, `:95`, `:115-116`). The first MB audit calls
  them decorative (`audits/04_MB_audit.md` §7).
- Nothing in the tree reads **results** against a source: who loses how much, when, how often a field is
  decided. Those are the quantities for which a page-read source now exists (Krentz's table, Sabin's
  summary).
- History counts the dead; the engine counts men lost to the fight. A target stated in the engine's unit
  against a historical percentage would be a comparison of two different things.

## The resolution, decided

### 1. Targets are ratios and orderings, never a historical percentage

A ratio of two engine losses has no unit, so it can be set beside a ratio of two historical death rates
without claiming the two measure the same men.

| id | reading (per scenario, n at least 400 seeded fields) | band | source and tier | status of the band |
|---|---|---|---|---|
| T-1 | the winner's share lost in a decided even field | reported; flagged if its median exceeds 0.10 | victors "never lost more than 10%"; average 5% dead (CR A1 `[D]`); "rarely … more than 5 per cent" (CR A11 `[D]`) | a flag, since the unit differs |
| T-2 | loser's loss ÷ winner's loss, even field, no pursuit possible (no horse, no `Pursue` role) | **1.7 to 5.2**, centre near 3 | Krentz's table: average 1 : 2.9, extremes 1 : 1.7 and 1 : 5.2 over 11 battles (CR A1, A2 `[D]`) | target |
| T-3 | loser's loss with mounted pursuit ÷ loser's loss without, same seeds | **2 to 5** | 14% against "over half … killed or taken prisoner" (CR A1, A6 `[D]`); the low end from Krentz's 20% ceiling | target; wide on purpose |
| T-4 | share of even fields decided (won or lost) within 1 bout, and within `max_bouts` | reported; the second must exceed the first | "sometimes decided very quickly … more usually … a drawn-out engagement" (CR C1 `[D]`) | ordering only. **No historical share exists** |
| T-5 | share of decided fields in which the loser broke at a `fight_loss` below the casualty floor (0.15) | above zero with `stand_draw: on`; zero with it off | clashes "decided at or before the first shock" (CR D5 `[D]`) | ordering against the control |
| T-6 | horse charging frontally: win share against unbraced foot > against braced pole-armed foot > 0; against shaken foot highest | the ordering | MV H1–H3 `[T]`; the gauge's own rows C1, C2, C5 | ordering |
| T-7 | **no scenario's win share is 0 or 1** at n 400 | every share inside (0, 1) | the standing rule (`AUDIT_BRIEF.md:36-51`); Cannae is one battle, not a rate | target; the gauge's C7 fails it today as recorded |
| T-8 | fresh against tired: a side entering at `entry_stamina` 0.5 against 1.0 | loses more often than the mirror by more than the sampling band | "fresh men fighting tired ones" (CR D3 `[D]`) | ordering; already measured by the one-ledger proposal (36 wins to 15) |
| T-9 | numbers: win share of the larger side at 2 : 1 and 3 : 1 on a frontage that fits both | rises with the ratio and stays below 1 | the linear law for hand-to-hand fighting (CR D8 `[T]`); depth alone did not win (CR D3) | ordering. **No historical win probability by force ratio was found** |
| T-10 | of men lost in flight under mounted pursuit, the share taken | between 0.2 and 0.8 as a mean, not constant across seeds | Zama, Cynoscephalae, Pharsalus (CR A6, §B) | flag; three battles |

- A reading outside a **target** is reported with the scenario and the seeds; the band is not moved to fit
  (the gauge note's own rule, `mass_battle_gauge_grounding.md:4`).
- A **flag** or an **ordering** that fails is a finding about a mechanism, not a number to tune.
- No band here gates a merge. They are read at a calibration pass and when a constant in
  `references/troops.yaml` changes.

### 2. The instrument

`systems/mass_battle/sim/results_readout.py` (the oracle scripts' home, `CLAUDE.md` §3), read-only, one
function per row of the table, each building its scenario through the season's own constructors
(`orderofbattle`, `massbattle.resolve_field`) so that what is read is what a season fights. It prints the
table with the reading, the band, n, and the same-run control for each row. It writes nothing tracked.

Scenarios, each with its control beside it:

| scenario | units | control |
|---|---|---|
| even foot | two equal spear armies, `line` | the same with the seeds' sides swapped (side symmetry) |
| even combined | the preset army of a weight-20 faction against itself | as above |
| pursuit | even combined; one arm with the horse removed from both | the no-horse arm is T-2's and T-3's denominator |
| charge | 200 horse against 400 foot: unbraced levy; braced pike; shaken spear | the horse against itself |
| tired | even foot, one side at `entry_stamina` 0.5 | both at 1.0 |
| numbers | spear 300, 600, 900 against 300 on a field wide enough for all | 300 against 300 |

### 3. Sweeps

One constant at a time, each against its own control arm, n 400, friction as shipped and again pinned off
(so a reading is not the friction multiplier's):

| constant (owner) | arms | rows it should move |
|---|---|---|
| `stand.*` obstacle table, and `stand_draw` on or off | off; seeds; seeds ±1 | T-2, T-4, T-5, T-6 |
| `pursuit_damage`'s scale (`CASUALTY_SCALE` as used there) | today; half; quarter | T-3 (the pessimist lane measured a mean 73% of survivors lost in one call, which puts T-3 near its top) |
| `max_bouts` | 1, 2, 4, 6 | T-4 |
| `fatigue.fast_move_drain` | 0, 2, 4 | the envelopment doctrine's win share; T-8 unaffected |
| `obey_ob` | off; seeds | spread of T-4; the manoeuvre rows' failure shares |
| `deployment.cell_troops` | cap arm; 16 | every row, read twice: the instrument's whole point is that the two arms are reported side by side |
| `MB_FRICTION_SIGMA` (ruled; **read, not proposed**) | 1.1; 0.55; 0 | every row: how much of each reading is the day's luck. For the audit's §7 item 2 |

### 4. Order

After rulings A-5 and A-6 move the battle's sampler to the bell curve and re-centre it
(`unified/DECISIONS_ANSWERED.md:11-12`): every reading moves with the sampler, so a pass before that is spent.
After the `Drawn` band and the amended pessimist proposal: T-3 has no numerator without pursuit.

## Gate (execution artifacts)

1. The instrument runs at the shipped tree and prints all ten rows with n, band and control; rows whose
   mechanism does not exist yet (T-3, T-5, T-10) print "no mechanism" and not a number.
2. A planted defect is seen: with `pursuit_damage` returning 0, T-3 reads 1.0 and is reported outside its
   band; with the winner's and loser's losses swapped in the readout, T-2 reads below 1.
3. Side symmetry: every even scenario's win share for side A is inside the sampling band of side B's.
4. Two runs at the same seeds print the same table.

## Falsifier

A band edited in the same commit as the constant that brought the engine inside it; a row whose scenario is
built by a constructor the season cannot reach; a historical percentage compared directly with an engine
loss.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the designer: every seed in the four `26_MASS_BATTLE` proposals and the troop file needs
  something to be read against. From the sources: results are where the page-read evidence is. Cut it and
  the only reference is the gauge, whose bands moved to fit.
- **R.** Completeness: it reads the extremes (0 and 1; a tired side; no horse).
- **S.** One instrument on the season's constructors; every row with its control; the same methodology as
  the gauge's decisive split where it reads win shares.
- **E, against that.** One read-only file and a table of ten bands.

## Cost class

Small build (one instrument). It is not a guard and gates nothing (`CLAUDE.md` §0.1 pt 5): it is load-bearing
on the game's exported parameters at a calibration pass, and is run then.

## What it does not establish

Any absolute casualty rate, any break threshold, any duration in minutes, any win probability by force ratio.
The sources read give none (the audit's §6).
