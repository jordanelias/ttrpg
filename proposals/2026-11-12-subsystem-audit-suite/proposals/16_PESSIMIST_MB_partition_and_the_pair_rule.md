# MB · an army in units must fight as well as the same men in one block: the melee pair's rule, and the row that proves it

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — three joins. (1) **A-5**: the `net` each side is paid by is the continuous net of the one sampler (`roll_net_continuous` plus `net_boost`), so edit 2's "net successes" is the margin above zero, not a count of faces, and `PAY_PER_NET`'s seed (1/6) is re-read on it; `U5a_DICE_owed_edits.md` §1 row 4 says the module's opposed roll "stays and is named", and for the melee pair this file's edit 2 governs: the pair is not opposed (`U5b_MB_rulings_in_the_field.md` §1 row 2). (2) **D-35 is answered: A-60** (numbers out of the melee dice), so CR-12 proceeds; this file is CR-12's step 3 and lands in the field calibration batch before the grid arm (same file §6 row 4). (3) **D-34 is answered: A-59** takes this audit's option (b) (the uncertainty keeps, its seat moves) and goes further: a static side-wide value is misleading, so the multiplier is lowered and tested for removal by `proposals/27_MB_*`, on the pair rule this file supplies. Nothing here edits its magnitude, as written; that lane's test does.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-5: every "today" figure in the problem
and the gate is marked pre-A-5, as recorded; the gate rows are relations and are re-taken on the A-5 sampler in the
calibration batch), §1 (CONFORMS; `PAY_PER_NET` a declared float, A-29), §7/§7b (test file and names, order, tier); A-59
and A-77 (the friction options "for Jordan" are answered: lowered, and shipped at zero if `27_MB_C`'s first test arm
passes; that lane's test sets it, this file does not); A-79 (the opposition rule is ruled for fights and arguments; the
melee pair is not an opposed roll, `U5b_MB_rulings_in_the_field.md` §1 row 2, so the form not taken stays not taken);
U1 D-U1-11c (`PAY_PER_NET` and `WALLS_DEFENDER_DEF_D` are scalar engine constants: literals in the module's config,
exported by `tools/export_engine_params.py`); U3 B19, §6.2 (the eight probes are not in the repository), C3-L1 (the
net is continuous; quantised only at the ladder, which the pair no longer reads). Changed: the head paragraph's
friction sentence, "The form not taken", the gate's "today" marks and test names, the cost line. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "trained score/rank" → skill score (1).

## Status: PROPOSED

Lands in batch: **B19** (MB; the field calibration batch), as CR-12's step 3: after `04_MB_cr12_linear_law.md` steps 1-2
and `16_PESSIMIST_MB_one_stamina_ledger.md` steps 1-2 (B19), after `04_MB_headcount_grade_and_scale.md` (B17). Depends on:
those; `U5b_MB_rulings_in_the_field.md` (B19).

Lane MB. Carries resolutions 1 to 4 and 8 of `audits/16_PESSIMIST_MB.md` §5 and its findings
F-PES-MB-01, -02 (the rule under the draw, not the draw), -04 and -05. **Extends, and does not
replace, `04_MB_cr12_linear_law.md`:** this is what that proposal's step 3 has to contain and one row
its exit has to gain. It edits no ruled value: the friction magnitude (`ED-MB-0016`, `ED-MB-0080`) is
untouched here; the audit's two options for it are answered by A-59 and A-77 and carried by `27_MB_C`'s
test. Reference, not mechanism (`CLAUDE.md` §0.05).

**Pre-A-5 figures.** Every count in "The problem" and every "Today" in the gate was measured on the whole-dice
sampler A-5 retires; they are kept as recorded. The gate's assertions are relations (a split row inside the
sampling band of its one-body row; the smaller side wins some and fewer than half), which survive.

## What it changes in `engine/season/` at runtime

Who wins, and what it costs, in every field in which a side is more than one body, is not a block, or
stands behind a wall; and the losses in every field. A declared hash mover wherever a field is fought
(in natural play today: the few `field.lost` a season produces, all at a scale the first audit's
`04_MB_headcount_grade_and_scale.md` changes first). The goldens under `engine/tests/` that include a
fought field are re-recorded once, with CR-12's.

## The problem (evidence: `audits/16_PESSIMIST_MB.md` §1.3, §2.3, §2.4, F-PES-MB-04)

All runs `PYTHONHASHSEED=0`, heavy infantry, friction off unless said, through the season's
constructors and `run_battle`.

1. **The result depends on the split.** On the same six cells, against a block of 900: one body wins
   36 of 60; three bodies, one file each, win **0**. On the same three cells in one rank: 36 of 100
   against 19. `ED-MB-0003` (ratified; Jordan, 2026-07-05) rules the pool semantics "Intensive
   (per-troop, partition-invariant)"; `ED-MB-0004` (Jordan, 2026-07-08) rules the dependence "a
   genuine defect -- fix it". `orchestration._convergence_scale` fixed the direction in which
   splitting adds dice. This direction was not tried.
2. **The shape a divided army gets loses by itself.** `orderofbattle._place` sets units side by side,
   each its own shallow line; a one-rank line of 900 wins 3 of 60 against a block of 900 even as one
   body. Through `resolve_field`, shipped friction: an equal block wins 42 of 100; the same men in
   three units 14; **twice the men in six units 22.**
3. **A detachment on a flank is worth less than nothing.** 600 in front and 300 on the flank rout a
   line of 600 in 15 fields of 60; 600 alone, in 21; 150 on each flank, in none.
4. **The bare rule is a cliff.** One body each, n 300: 10% more men wins 70%, 50% more wins 98%,
   twice the men win 299 of 300 at a cost of 1%.
5. **Whole match-ups are certain.** `max(0, DAMAGE_BY_DEGREE[degree](power) - dr)`: 3,000 spearmen,
   light infantry or archers do no harm at all to 300 levy behind walls (60 of 60 each, shipped
   friction on); levy against levy, the defender loses nobody in 48 of 60.

**The cause, read at the site and in the trace.** `orchestration.resolve_engagements`: each side's net
is graded against the other side's roll (`compute_degree(a_net, max(1, b_net))`), and the casualties a
side deals are `K_LINEAR x (its engaged frontage) x max(0, DAMAGE_BY_DEGREE[its degree](power) - dr)`
with `Failure 0, Partial 1` and a default `dr` of 1, so the lower net of a pair deals nothing. The pool
behind the net is the body's own headcount (`core/exchange.py::subunit_combat_pool`). So the larger
body in a pair deals all the damage in it, and a large body fights every small body it touches at
close to its whole pool at once: in the trace of 3 x 300 against 1 x 900 the pairs read 9 dice against
22 and 4 against 16 (22 + 16 from a pool of 28), the degrees are (Failure, Overwhelming) in 14 of 18
rolls, and the three companies deal no casualty in the field.

**What three proxies showed** (monkeypatches for the run; `p9_proxy.py`, `p12_proxy3.py`,
`p15b_shape_proxy.py`). CR-12's step 3 alone (pool from troop quality only) removes the shape collapse
(3 → 16 of 60) and the size cliff, and leaves the same-cells split at 2 of 60. Adding pay-by-own-net
(edit 2 below) makes a flank detachment break the line more often than its absence for the first time
(39 routs of 60 against 27; two wings, 58), leaves the same-cells split at 0 of 60, and, with the
integer armour subtraction kept, makes levy against levy bloodless in 60 of 60. So three owners are
involved and none of the three edits below is optional.

## The resolution, decided

**The requirement** (already ruled; ladder step 1): a force's result does not depend on how many
bodies its cells are grouped into.

**The pair rule that meets it**, in three edits at their owners:

1. **The pool is troop quality.** As `04_MB_cr12_linear_law.md` step 3 states it (`eff_power x
   REFERENCE_SIZE x POOL_QUALITY_SCALE`, less the discipline term). Not restated here. Numbers act
   through the engaged-frontage term only.
2. **Each side is paid by its own roll.** The casualties a body deals in a pair are
   `K_LINEAR x (its engaged frontage in that pair) x PAY_PER_NET x max(0, its net) x (1 + its power)`.
   This is the law `orchestration.pursuit_damage` already uses in the same file (`net x (1 + power)`,
   cited there as PP-233), and it is what the code's own citation at the simultaneous-damage block
   says ("Both sides deal and receive damage"). The opposed comparison and `DAMAGE_BY_DEGREE` leave
   the melee pair. `ED-MB-0045` already records "two damage laws" and that the table's citation does
   not exist; this makes it one. The four-band ladder stays where an outcome is declared, the field's
   band; a tick's casualties are the roll's own count.
3. **Armour and walls shift the roll; they are not subtracted from the damage.** A defender's `dr`,
   and the walls' `WALLS_DEFENDER_DR`, become die-equivalents against the attacker's net, entering
   where the two sibling terrain rows already enter (`terrain_def_d`, converted by `SIGMA_PER_D`
   through `_sigma_net_boost`, soft-capped). No match-up has a zero it cannot leave.
4. **A cell's engaged strength is divided among the pairs it is in.** Where the tick's pairs are
   assembled, each contact cell's contribution to a pair's frontage is `1 / m`, `m` the number of
   pairs that cell is in this tick. With edit 1 nothing sums pools any more, so
   `_convergence_scale` and `pair_pool_contribution`'s share are deleted with their "known accepted
   residual".

**The form not taken, and why.** Banding each side's net against an obstacle derived from the
opponent's quality would also end the winner-take-all, and it is how the rest of the tree states an
obstacle. The opposed obstacle has since been ruled (A-79: the defender's skill score at
`opposition_rate`, for fights and arguments; `degree_from_net`'s docstring's 2026-08-21 suspension is the
superseded text, `OWED_TO_UNIFICATION.md` §A). The melee pair is not an opposed roll (`U5b_MB_rulings_in_the_field.md`
§1 row 2): each side is paid by its own roll, so edit 2 needs no obstacle and the form stays not taken.

## Exact edits

| file · owner | edit |
|---|---|
| `modules/mass_battle/core/exchange.py` | the pool base as CR-12 step 3; `pair_pool_contribution` deleted; `_pair_engaged_troops` stays (it is what says a body is engaged) |
| `modules/mass_battle/orchestration.py::resolve_engagements` | the two `compute_degree` lines and the four `DAMAGE_BY_DEGREE` lines replaced by one helper, `pair_casualties(net, power, frontage)`, beside `pursuit_damage`, which calls it too (one owner of the law); the `- eff_dr` terms removed; `a_pool` / `b_pool` are the quality pools; the `conv_scale` threading removed |
| `modules/mass_battle/orchestration.py::_convergence_scale` | deleted |
| `modules/mass_battle/orchestration.py::resolve_engagements_cascading` | before the sub-phases: one pass over the tick's pairs counting, per side, the pairs each contact cell is in; the count rides on the pair (`a_share`, `b_share`) |
| `modules/mass_battle/core/attrition.py::_lanchester_strength` | takes the share; the frontage it returns is the sum over contact cells of `1 / m` (and, on the continuous path, `front_width` scaled by the same mean share) |
| `modules/mass_battle/orchestration.py`, the sigma head | `ns_a` gains `-(atom_b.eff_dr) x SIGMA_PER_D` and the mirror, at the line where `_ta` / `_tb` (the terrain dice) are added |
| `modules/mass_battle/massbattle.py::_run_and_grade` | the WALLS branch writes `unit_b.terrain_def_d += WALLS_DEFENDER_DEF_D` instead of `unit_b.dr +=`; `walls_dr` (the season's `field_walls_dr` fixture) is read as dice, name kept |
| `modules/mass_battle/terrain.py` | `WALLS_DEFENDER_DEF_D = 3` replaces `WALLS_DEFENDER_DR = 3` (the same number, now in the unit its two siblings use; a seed, Jordan's to tune) |
| `modules/mass_battle/config.py` | `DAMAGE_BY_DEGREE` deleted; `PAY_PER_NET` added, seeded at `1 / 6` (so that a mean heavy-infantry net pays what `Success` pays today before armour: the value the proxy ran); `REFERENCE_SIZE` as CR-12 |
| `modules/mass_battle/resolution.py::compute_degree` | stays for `massbattle._grade`'s neighbours and the discipline checks; no longer read by the melee pair |
| `systems/mass_battle/sim/lanchester_signature.py` | CR-12's exit gains the PARTITION row below |

## Gate (execution artifacts; all friction off unless said, `PYTHONHASHSEED=0`, n at least 100, each
loop asserting it counted)

1. **PARTITION, same cells.** One body against a block, and the same cells as three bodies, on three
   footprints (three files by two ranks, one file each; three cells in one rank, one cell each; six
   files by one rank, two cells each), both as attacker and as defender: every split row's share of
   wins within the sampling band of its one-body row (at n 100, about ten points either way). Today
   (pre-A-5, as recorded): 0 of 60 against 36; 19 of 100 against 36; 2 of 60 against 3.
2. **SHAPE.** A one-rank line against a block of equal men loses more often than it wins and wins
   some (today, pre-A-5: 3 of 60; the proxies 14 to 16).
3. **SIZE.** One body each, 2:1: the smaller side wins some fields and fewer than half (today, pre-A-5:
   0 of 60).
4. **FLANK.** 600 in front and 300 on the flank rout a three-rank line of 600 more often than 600
   alone do (today, pre-A-5: 15 against 21).
5. **NO CERTAIN MATCH-UP.** Through `resolve_field`, shipped configuration: 3,000 spearmen against
   300 levy behind walls: the defender loses somebody in most fields and `attacker_wins` is neither 0
   nor n; levy against levy on open ground: somebody is hurt in most fields.
6. **CR-12's own exit**, unchanged, on its repaired instrument.

Rows 1 to 5 live as tests in NEW `tests/valoria/test_mass_battle_partition.py` (beside `test_mass_battle_yield.py`,
which exists; the mass-battle marker): `test_partition_same_cells_inside_sampling_band`,
`test_shape_one_rank_loses_more_than_wins`, `test_size_two_to_one_smaller_wins_some`, `test_flank_detachment_helps`,
`test_no_certain_matchup_through_resolve_field`, each loop asserting `checked >= n`. They are the committed form of
the scratch runs `p15_shape.py`, `p13_same_cells.py`, `p1_size.py`, `p2_flank.py` and `p10_edges.py` (not in the
repository). Command: `python -m pytest tests/valoria/test_mass_battle_partition.py -q -m mass_battle`, then
`python -m pytest engine/tests -q` (the goldens, re-recorded once with CR-12's, said plainly).

## Falsifier

Any gate row failing after the edits; in particular row 1 on the block footprint, which the two
proxied edits do not move (0 and 2 of 60) and which rests on edit 4 alone. If edit 4 does not move it
either, the cause is not the one named here and this proposal is wrong about the third owner; the row
stays as the test and the search continues from the trace.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** Bottom-up: a cell's men fight what is in front of them, once. Top-down: an order of battle
  can have units. Lateral: one damage law in the file, and armour entering as every other advantage
  in the engine does. Vertical: a season army of several troop types is no longer beaten by its own
  organisation. Diagonal: a detachment's manoeuvre reaches the result. Horizontal: both sides, any
  grouping, the same arithmetic. Cut it and what dies is every story with more than one unit in it
  (`audits/16_PESSIMIST_MB.md` §3.4).
- **R.** Formation, reserve, flank and troop mix become choices with a price instead of a penalty;
  the wall becomes costly instead of immune or irrelevant; the extremes lose their certainties.
- **S.** One damage law (two today); terrain rows all dice (two of three today); no pool summing, so
  no correction for it; consistent with the linear law CR-12 is locked to.
- **E, against that.** Fewer objects than before: a table, a scaling pass, a residual and a
  subtraction go; one helper and one constant arrive. And the simplest intuition a player has, that
  more units of the same men are not worse, becomes true.

## Cost class

Design-first: the edits are small, the re-calibration is not (`K_LINEAR`, `PAY_PER_NET`, the rout
bands and every field golden move together). One change with CR-12's step 3, one re-record. Tier: `opus` for the
calibration judgment (`PAY_PER_NET` re-read on the continuous net), `sonnet`, effort `high`, for the edits. Hash
movers declared: every fought field; the goldens under `engine/tests/` re-recorded once with CR-12's. Lands it: B19,
order edit 1 (CR-12 step 3) → 2 → 3 → 4 → the PARTITION row in `lanchester_signature.py`, each with the tests it
turns green.

## Sequencing

After CR-12's step 1 (the instrument) and step 2 (the consolidation), as its step 3. After
`04_MB_headcount_grade_and_scale.md`. Before `04_MB_cell_hierarchy_as_data.md`'s grid arm is
calibrated (that proposal multiplies the number of cells and bodies a season fights with; on the
present rule it would multiply this defect), and before any decider is built on the strategy roster
(`04_MB_manager_battle_one_resolver.md`): the addendum's "trap" (F-MB-21) is this rule seen through
three strategies.
