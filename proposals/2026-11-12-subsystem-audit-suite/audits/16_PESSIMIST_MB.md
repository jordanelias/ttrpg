# MB — pessimist audit: NERS, premise and emergent narrative, of mass battle

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `modules/mass_battle/`, `systems/mass_battle/sim/`, `engine/season/loop/effects_army.py`, the host
seam (`engine/season/seam/wrappers/mass_battle.py`, `loop/sides.py`, `loop/effects_combat.py::_eff_march`),
Jordan's stated intent for mass battle (`AUDIT_BRIEF.md`: the cell-based army → unit → subformation →
troops hierarchy; mixed weapons at a fatigue and movement cost, archers carrying arming swords; Football
Manager, Total War, Ogre Battle, Unicorn Overlord, Bannerlord; the commanded and the auto-resolved battle
as one resolver), and five premise sentences of a battle. The first audit (`audits/04_MB_audit.md`,
F-MB-01..19) and its addendum (`04_MB_audit_addendum_B.md`, F-MB-20..26) and the ten `04_MB_*` proposals
are cited, not redone. Everything measured here is new work unless a finding id of theirs is named.

All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_MB/`.

(Sections below are appended as the work proceeds; §0 is written last and placed first.)

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the five sentences the work order names). The
ordinary account O in §2.1 was written before any module file was opened by this lane; what this lane
already knew of the code came from the first audit's §0 and §1 and the addendum's §B0, and O was written
from the words, not from those.

### 2.1 O — what each sentence should mean (written first)

**P1 "A flanked line breaks."**
1. A line is a body with a front; its front faces one way. 2. Flanked means an enemy body is in contact
with its side or rear while (or instead of) its front. 3. The flanked body fights worse on the flanked
side than it would on its front (fewer men can bring weapons to bear, no shields that way). 4. It also
loses heart faster than from the same losses taken frontally. 5. "Breaks" is a morale event (rout), not
annihilation: it should come sooner, at a lower loss, than in the frontal control. 6. Proportion: rear
worse than side, side worse than front; two flanks worse than one. 7. Not certainty: a steady, deep or
elite body sometimes holds a flank attack; "breaks" is the usual outcome, not a fixed one (standing
rule). 8. Zero: a line with nobody on its flank gets none of this. 9. Feedback: the record says it was
taken in flank. 10. [GENRE] the flanker needs to get there: flanking costs time or a manoeuvre, and a
commander can order it or guard against it (refuse a flank, reserve).

**P2 "A larger army usually wins but not always."**
1. Size is headcount. 2. Equal quality, equal ground, even numbers: about even, and swapping sides swaps
the result (mirror). 3. Win rate rises monotonically with the size ratio, with no cliff: 1.2:1 a modest
edge, 2:1 a strong one, 3:1 near-certain but still under 100% over many fields. 4. "Not always": at
ordinary ratios (1.5:1) the smaller side wins a visible share, and quality, ground or luck can be the
reason. 5. It holds at every scale the game fights at: 30 against 20 and 3,000 against 2,000 give
similar odds (or differ for a reason the words give). 6. The winner pays: the larger army's losses are
smaller in proportion but not zero. 7. Bounds: 1 man against 100 loses; 0 does not fight. 8. Feedback:
the result says who won and by how much.

**P3 "A pike block holds against cavalry."**
1. A pike block is infantry whose weapon is the pike, in close order, facing the charge. 2. Cavalry
charging its front does markedly worse than the same cavalry charging the same number of other infantry
(swords, levy, archers): control by troop type. 3. "Holds" means it does not rout and keeps its ground
for the engagement, usually; cavalry sometimes breaks in (draw). 4. The protection is frontal and
depends on order: cavalry into the flank or rear of pikes does well; disordered, tired or thinned pikes
hold less. 5. Pikes are not thereby good at everything: against swordsmen who close, or archers, they
should be ordinary or worse (otherwise "pike" is a dominant choice). 6. The word is the weapon: remove
the pike (same men, other weapon) and the effect goes.

**P4 "A tired unit fights worse."**
1. Tiredness is a state that rises with marching, fighting, charging and (per Jordan) carried kit, and
falls with rest. 2. More tired, worse fighting: monotone, starting before exhaustion. 3. "Worse" shows
in the outcome: the tired side of an otherwise even field loses more often and takes more losses.
4. Tiredness that arrived before the battle (a forced march) counts: a campaign-scale state enters the
field. 5. It persists and recovers on a readable clock. 6. A fresh reserve committed late beats a tired
front line (the reason reserves exist). 7. Heavier troops tire faster. 8. Bounds: at maximum tiredness a
unit still fights, badly; it does not vanish or become immune.

**P5 "A routed army can be rallied or destroyed in pursuit."**
1. Rout is a state distinct from destroyed: the men are alive and running. 2. Two exits: rallied (they
re-form and can fight again, now or later, at a cost) or run down. 3. Pursuit is an act by the winner
(or a standing order), most effective with fast troops, and kills or captures the routed. 4. Rallying
is an act by a commander, depends on him (presence, leadership) and on not being pressed, and may fail
(draw). 5. So the same rout has different ends depending on what both commanders do and on a draw.
6. Most of a pre-firearms battle's dead fall in the pursuit, so pursued-against-not-pursued should
differ largely in the loser's losses. 7. After the field: a routed army that was not destroyed exists
somewhere on the map, weaker, and can be met again. 8. Feedback: the record tells rout, rally and
pursuit apart.

### 2.2 How the runs were made (one harness, two controls on every row)

`h.py`: sides are built through the module's own season constructors (`orderofbattle._spec_for`, `_place`,
`armies.build_army`: the same calls `orderofbattle.build_unit` makes) and fought through
`battle_loop.run_battle(a, b, max_turns=18)` under `rngsource.using(random.Random(seed))`, seeds
`0..n-1`. Two things are varied on every table, because each hides the other:

- **Friction ON / OFF.** ON is the shipped engine (`config.MB_FRICTION`, a LogNormal(0, 1.1) factor per
  side per battle, `orchestration._draw_friction`, multiplying the side's pool at
  `core/exchange.py::subunit_combat_pool`). OFF (`orchestration.MB_FRICTION = False` for the run) is the
  mechanism with that one draw removed: it is the control that shows what the rule under the noise does.
- **Density.** "Season density" is what every season constructor uses (`cell_cap_for`: 200 troops a
  cell, so 600 men are 3 cells in one rank; addendum F-MB-20). "50 a cell" is the same men as 12 cells
  in three ranks, the least depth at which a body has a flank, a rear and support ranks.

Module scale has no Event log; the trace (`resolution.tracing()`) carries `melee` rows with both pools,
both nets and both degrees, and is what §2.4 reads.

### 2.3 P2 — "a larger army usually wins but not always": the numbers hold, the cause does not, and it inverts when the larger army is organised

**Verdict: holds as a win-share curve for two single bodies (EXECUTES, module scale); the "not always"
is one hidden draw and nothing in the fiction; INVERTED as soon as the larger army is more than one
body.** At season scale it is INERT at FIRES for the reasons the first audit gives (F-MB-01, F-MB-03);
not redone.

| # | link | O predicted | C observed (n 300 a row, heavy infantry, open ground) | verdict · cause |
|---|---|---|---|---|
| 2 | even numbers are even; swap flips | ~50/50 | friction ON, 600 v 600: A 133, B 154, 13 undecided. OFF: 134 / 136 / 30 | FOLLOWS |
| 3 | monotone, no cliff | 1.2:1 modest, 2:1 strong, 3:1 near-certain | ON, larger side's share of all fields at 1.1 / 1.25 / 1.5 / 2 / 3 / 5 to 1 (600 the smaller): 50-55% / 56-58% / 61-63% / 69-73% / 81-83% / 90-91%. **OFF: 70% / 89% / 98% / 99.8% / 100% / 100%**, and at 2:1 the larger side loses 1% of its men, at 3:1 0.1% | ON: FOLLOWS. OFF: a cliff (EDGE): ten percent more men is a 70% field, fifty percent is a certainty |
| 4 | "not always" has a reason in the world | quality, ground, luck in the fighting | ON, 600 v 600: the winner is the side with the higher friction draw in **275 of 287** decided fields; where the two draws differ by more than 2x (199 of 287 fields, 69%) the higher draw wins **199 of 199**. ON, 1200 v 600: the smaller side wins 85 of 300; in **85 of 85** it drew the higher friction, in 83 more than twice the larger side's | DEPARTS · BEHAVIOUR (ruled: `ED-MB-0016`; F-MB-08). The outcome of a field is, to within a few percent, a function of two numbers drawn before the first tick and returned to nobody |
| 5 | same odds at every scale | similar at 300, 600, 2400 | ON, 2:1: 69% / 69-73% / 59-65%; 5:1: 92% / 90% / **67%, with 29-33% of fields undecided at 18 ticks** (2,400 v 12,000) | FOLLOWS to 600; EDGE above: a large field does not finish in the one engagement turn a season fights |
| 6 | the winner pays | smaller share, not zero | ON, 2:1: larger loses 11-13%, smaller 33%. OFF: 1% against 45% | FOLLOWS (ON) |
| 8 | the record says who won and by how much | yes | `resolve_field` returns `{attacker_wins, degree, attacker_size_pct, defender_size_pct}`; neither friction draw is in it (first audit F-MB-06) | DEPARTS · E10: the one number that decided the field is the one number not reported |

**Control for the friction reading.** With friction OFF the same 600 v 600 field still splits 134 / 136
with 30 undecided, so the per-tick dice do decide an even field when nothing else does; the 96% is not
an artefact of a field that is otherwise fixed. With friction ON the dice decide only the fields where
the two draws happen to be close (88 of 287, in which the higher draw wins 76).

**The standing rule, read against this.** *We do not do deterministic* asks that state set the odds and
the draw set the outcome. The shipped field meets the letter (there is a draw) and misses the sense in
both directions at once: under the draw the rule is a near-fixed function of headcount (the OFF column),
and the draw laid over it is not the engine's graded roll over a pool and an obstacle but a single
pre-battle multiplier with a 4.7x one-sigma spread on the ratio, which then decides the field alone.
What a commander does between the draw and the result (§2.4, §2.6, §2.7) is small against either.

**Link 1 inverted: "larger" stops meaning "stronger" when the army has units** (`p3_partition.py`, n 60
a row; the same 900 heavy infantry in one line, as one, two, three or six bodies; `attacker graded the
winner` is `massbattle._grade`'s rule, B routed or more of A left):

| A's 900 men as | v B 1 x 600, 50 a cell, OFF | v B 1 x 900, 50 a cell, OFF | v B 1 x 900, season density, OFF | v B 1 x 600, 50 a cell, **ON (shipped)** |
|---|---|---|---|---|
| 1 x 900 | A graded winner **55**/60; loss A 5%, B 29% | 31/60; 17% / 18% | 30/60; 21% / 24% | 33/60 |
| 600 + 300 | **2**/60; 21% / 4% | 9/60; 19% / 10% | **0**/60; 57% / 0.6% | 21/60 |
| 450 + 450 | 47/60; 11% / 19% | 7/60; 27% / 9% | 0/60; 63% / 3% | 30/60 |
| 3 x 300 | **0**/60; 30% / 5% | 0/60; 34% / 2.5% | **0**/60 (B wins 60 of 60 in 13 ticks); 60% / 0.7% | 16/60 |
| 6 x 150 | **0**/60; 33% / 0.5% | 0/60; 55% / 0.2% | 0/60; 57% / 1.5% | 8/60 |

Side-swap control (B split, A whole): A 1 x 900 against B 3 x 300 at season density, A wins 59, B 1; B's
loss 60%, A's 1%. The effect follows the split, not the side.

So nine hundred men in three companies lose sixty fields of sixty to the same nine hundred in one block,
losing sixty percent to its one, and lose every graded field to six hundred in one block. Under the
shipped friction the same ordering survives the noise (33, 21, 16, 8 of 60).

**Why** (trace, `t2.py`, seed 3, season density, friction OFF). In `3 x 300 v 1 x 900` the first melee
rows read `a_pool 9, b_pool 22` and `a_pool 4, b_pool 16`: each 300-man body brings its own pool
(`eff_power x eff_size x POOL_QUALITY_SCALE`, so 9 for 300 men and 28 for 900,
`core/exchange.py::subunit_combat_pool`), while the 900-man body brings to **each** pair the share of
its pool that its engaged cells and their supports make (`pair_pool_contribution`), and one cell in
contact with two enemy bodies counts toward both (the function's own "known accepted residual": 22 + 16
is more than its 28). Each pair is then an opposed roll graded on the four-band ladder, and
`DAMAGE_BY_DEGREE` gives the lower net **nothing**: over the field the degree pairs were (A Failure, B
Overwhelming) 14, (Failure, Success) 1, (Failure, Partial) 1, and one each way otherwise; A dealt no
casualty at all and took 578. A melee pair is winner-take-all on a pool that is proportional to the
body's own headcount, so the bigger body in each pair deals all the damage in it, and a big body fights
every small body in reach at close to its whole pool at once. The same root gives the OFF column of the
size table its cliff.

`orchestration._convergence_scale` is the tree's own "[partition-invariance fix]": its docstring records
that Jordan ruled the dependence of the result on how a force is split "a genuine defect (2026-07-08)".
That fix caps the case in which splitting multiplies the splitter's dice. It does nothing for, and by
shrinking each member's pool worsens, the case measured here.

**What this does to the intent.** The structure Jordan asks for is army → unit → subformation → troops,
with units of distinct troop types and, from Ogre Battle and Unicorn Overlord, many small squads. In the
engine as it runs, every unit an army is divided into is a loss: the optimal order of battle is one
subformation, and the first audit's and the addendum's lever tables (F-MB-21: "advance" and "defend"
lose to "line"; "no horse" 27 against 76) are instances of this one rule read without it. Finding
F-PES-MB-01.

### 2.4 P1 — "a flanked line breaks": it breaks no sooner than an unflanked one, and the men who went round are worth less than men who stayed home

**Verdict: does not hold (EXECUTES, module scale; not reachable at season density, where a body is one
rank and has no flank, addendum F-MB-20).**

`p2_flank.py`, n 60 a row, B = 600 heavy infantry in one body of three ranks; A's main body 600 in front
of it; A's extra 300 placed in the line, on B's flank (same rows, five columns out), or behind B.

| A | friction OFF: B routed | B's mean loss | A's mean loss | A / B / undecided | friction ON: B routed | A / B / undecided |
|---|---|---|---|---|---|---|
| control: no extra men, 600 v 600 | **21**/60, at a loss of 26% | 17.6% | 19.5% | 20 / 23 / 17 | 21/60 | 21 / 33 / 6 |
| 300 more, in the line | **0**/60 | 4.3% | 20.7% | 0 / 0 / 60 | 14/60 | 14 / 0 / 46 |
| 300 more, on B's flank | **15**/60, at 26% | 18.2% | 9.6% | 15 / 6 / 39 | 19/60 | 18 / 25 / 17 |
| 300 more, in B's rear | **25**/60, at 30% | 22.4% | 5.0% | 25 / 0 / 35 | 24/60 | 24 / 8 / 28 |
| two bodies of 150, both in the line | 0/60 | 1.4% | 41.5% | 0 / 17 / 43 | 5/60 | 5 / 32 / 23 |
| two bodies of 150, one on each flank | **0**/60 | 8.4% | 5.5% | 0 / 0 / 60 | 12/60 | 12 / 0 / 48 |

| # | link | O predicted | C observed | verdict · cause |
|---|---|---|---|---|
| 3-5 | the flanked body breaks sooner, at a lower loss | more routs than the frontal control, at fewer casualties | flank: 15 routs of 60 against the no-extra-men control's 21; the loss at which B routs is 26% in both. Rear: 25 against 21, at 30% | DEPARTS · COMPOSITION |
| 6 | rear worse than flank worse than front; two flanks worse than one | ordered | rear 25 > flank 15 > front 0, so the order of the three positions is right; **both flanks: 0 of 60**, the worst of all for the encircler | DEPARTS at the top of the order (EDGE) |
| 8 | zero: no flanker, no effect | the control is the floor | the control (no extra men at all) routs B **more often** than a flank attack by 300 extra men does | INVERTED against the zero |
| 9 | the record says it was taken in flank | yes | the `melee` trace row has no arc or side field; `resolve_field`'s return has none | DEPARTS · E10 |
| 10 [GENRE] | flanking is ordered and can be guarded against | an order, a reserve | the body told nothing turns on its own toward the nearest enemy: in the rear arm B's `_node_facing` reads (-0.996, 0.09) at tick 1, its back to A's main body, and it walks toward the 300 | note |

Reading. The octagon machinery is real (`OCTAGON_DMG_MULT` 1.5 / 2.0, `MULTI_SIDE_SHOCK`,
`MB_ENVELOP_SHOCK`) and is visible in A's losses, which halve (flank) and quarter (rear): the flanker
does hurt B and spares A. But B's fate is set by §2.3's rule: the flanking body is a second, smaller
body, its pool loses the pair's roll, and what a flank multiplies is the damage of a body that mostly
deals none. A commander who sends 300 of his 900 round the flank does worse at breaking the enemy than
one who leaves them in camp; one who sends 150 round each flank never breaks him at all. Three further
facts under the table: (a) an 18-tick field ends before most flank attacks finish (39 and 35 of 60
undecided), and the season fights exactly one such turn (`massbattle._run_and_grade`); (b) the flanked
line needs no order to face about, so "flanked" is a state that lasts two ticks
(`FACING_REACTION_TICKS`) unless the front is also pinned; (c) with friction ON the table's ordering is
largely gone (B wins 25 of 60 when flanked, 33 when not): the draw is larger than the manoeuvre. Finding
F-PES-MB-02.

