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

## 0. Verdict

**Mass battle does not do what its five plain sentences say, and the reason is one rule nobody had
tried from the side: a melee pair is winner-take-all on a pool proportional to each body's own
headcount, so the engine rewards an army for being one undivided block and punishes every unit it is
divided into.** Nine hundred heavy infantry in three companies lose sixty fields of sixty to the same
nine hundred in one body, taking sixty percent losses to its one (friction off); through the season's
own entry with the shipped friction on, an attacker who **doubles** his army and forms it into six
units wins 22 fields in 100 where an equal single block wins 42. That is the opposite of the structure
Jordan asks for (army → unit → subformation → troops; squads; mixed arms), and it is why a flank attack
by a detachment breaks a line no sooner than leaving the detachment in camp, why two wings on two flanks
never break it at all, and why the first two lanes' lever tables kept reading "worse than doing
nothing". Over that rule sits the ruled friction draw, which this lane measured rather than re-raised:
in an even field the winner is the side with the higher of two numbers drawn before the first tick in
275 of 287 decided fields, and in 199 of 199 where the two differ by more than a factor of two; with
the draw removed the rule under it is a cliff (ten percent more men is a 70% field, fifty percent a
certainty). So the field offends the standing rule in both directions at once: a near-fixed function of
state, with one unseen multiplier laid over it that then decides alone. The other three sentences fail
separately: the pike is heavy infantry in every braced field at three ranks as at one, and what holds
against horse is the brace, half the time; fatigue works, but on a ledger that is never reported and
never carried, while the reported ledger never leaves 100 and changes nothing; and a rout has no exit
at all (rally is an empty hook; pursuit is called by nothing, and no cavalry the season can build is
ever "Fast"). Integer armour against integer power makes whole match-ups certain: three thousand
spearmen, light infantry or archers do no harm whatever to three hundred levies behind a wall, sixty
fields of sixty. In computed play the subsystem tells two of its nine possible stories, no attacker has
won a field in eighteen seed-seasons at the shipped scale or the proxy one, and the people it touches
are ground to a thousandth of a body and go on acting. **The steelman holds where it was tried:** two
single blocks give a sound, mirror-fair, monotone size curve under the shipped friction; the octagon
orders front, flank and rear correctly for a whole force; the brace and the column fatigue do what
their words say. The engine is a good duel between two blobs. It is not yet a battle between armies.

## 1. NERS — cut tests, executed

Definitions `CLAUDE.md` §0.06; method `skills/ners/SKILL.md`; the draw's properties by
`skills/resolution-diagnostic/SKILL.md` (§1.3). A cut is executed here by building the same field with
and without the thing and comparing results field for field (same seeds). "Free" means nothing but the
thing's own bookkeeping differs.

### 1.1 False N-lines found (cuts that turn out free, or better than free)

| the thing | the N-line it is kept on | the cut, executed | what dies |
|---|---|---|---|
| **the unit stamina ledger** (`Unit.stamina`, `Subunit.stamina`, `STAMINA_DRAIN_PER_CONTACT_CELL`, `_stamina_pool_penalty`, `STAMINA_POOL_THRESHOLDS`, `stamina_check`, `BETWEEN_TURN_STAMINA_RECOVERY`, `run_battle`'s `a_stamina` / `b_stamina`) | "a tired unit fights worse" | entering at 50 or 10 instead of 100: identical in 100 of 100 fields; a fresh 18-tick field ends at 99.5 and 100.0 | nothing. Fatigue is carried by the column ledger (`percell._ColBlock.stamina`), which the cut leaves alone. **Free.** |
| **the pike troop type** as distinct from heavy infantry | "reach 0.3 is the sole, isolated differentiator" (`registry.py`) | pike for heavy infantry, braced, three ranks, against a charge: identical in 60 of 60; one rank: 440 of 440 (addendum) | a name and a row. **Free today.** It stops being free only when a loadout the resolver reads exists (addendum proposal) |
| **nine role rows** (cavalry `Pursue`, `Screen`, `Feint`; light cavalry `Pursue`, `Screen`; light infantry `Pursue`, `Screen`; archers `VolleyLine`; heavy infantry `Anvil` against foot) | "the FM position → role model" | the role named against no role: identical in 60 of 60, each | nothing. `ROLE_INSTRUCTION_PRIMITIVES` already says seven of its sixteen keywords drive nothing; the menu still offers them. **Free.** |
| **an army's division into units**, as the resolver treats it | none stated; assumed harmless | merge the units into one body: the army goes from 0 wins of 60 to 30 (v an equal block), from 0 to 55 (v two-thirds its size) | nothing the resolver values; everything the design wants (mixed arms, squads, a flank, a reserve). **Better than free, which is the defect** (F-PES-MB-01) |
| **`_convergence_scale`**, "the partition-invariance fix" | the result does not depend on how a force is split | measured: it does, by 60 fields in 60 | its line is false as built; the requirement it names is right |
| **`rally_check`, `threadwork_check`** | hooks in the canonical phase order | bodies are `pass` | nothing; cut, or build (§2.7) |
| **the `Flanker` role on a single cavalry body** | envelopment | cut it (no role): the cavalry's wins go from 13 to 42 of 60 | a manoeuvre that costs 29 fields in 60. **Better than free** |

### 1.2 N-lines that survive, and what they survive as

- **Friction** (ruled, `ED-MB-0016`; not cut; first audit F-MB-08 and §11). N from all directions.
  Top-down: holds, it produces the banded win-share curve (§2.3). Bottom-up: fails, it arises from
  nothing in the units. Lateral: fails, no sibling contest multiplies a pool by a per-contest
  LogNormal; personal combat and the social contest set odds by named sigma levels through
  `sigma_leverage`, soft-capped at 1.5 (S: calculations not consistent in methodology with siblings).
  Diagonal (a commander's choice crossing into the result): fails, §2.4 to §2.6 show each choice inside
  the draw. Vertical (season to field and back): fails, the draw is not returned, so nothing above can
  tell a lucky field from a good plan. **Narrowed: it holds in one direction, as a patch over the rule
  under it.** The cut is not free today, and the reason is new: with the draw removed the pair rule is
  a cliff. Its N-line depends on the cliff staying.
- **The brace** (`ShieldWall`, `Hold`): survives. Cut it and a heavy block goes from 30 holds of 60 to 8.
- **The octagon** (arc multipliers, multi-side shock): survives for a whole force (30 / 41 / 55 routs of
  60 from front, flank, rear) and is defeated in composition by the pair rule (§2.4).
- **The column fatigue ledger**: survives (36 → 15 → 10 wins of 100).
- **The size curve of two blocks under shipped friction**: survives, mirror-fair to sampling error.

### 1.3 The draw, by the resolution diagnostic (evidence for the above, not a verdict)

Phase 0, the draws in a field: (1) the friction factor, `math.exp(gauss(0, 1.1))` per side, a bespoke
draw outside the engine (P-v); (2) the melee pair, `roll_pool_fractional` plus `_sigma_net_boost` in
`modules/mass_battle/resolution.py`, the declared second sigma path (DICE lane F-DICE-07, F-DICE-08;
not re-filed); (3) volleys; (4) discipline checks, `roll_pool(discipline)` against Ob 1; (5) the
stochastic rout point between 15% and 30% losses; (6) contention ties.

| property | finding on the melee pair | reproduce |
|---|---|---|
| **P-iv graded, recoverable** | `a_deg = compute_degree(a_net, max(1, b_net))` and the mirror (`orchestration.resolve_engagements`): each side's net is graded against the **other side's roll** as its obstacle, so at most one side reaches Success. Casualties are `K_LINEAR x lin x max(0, DAMAGE_BY_DEGREE[deg](power) - dr)` with `Failure 0, Partial 1, Success p, Overwhelming 1 + p` and a default `dr` of 1: **Failure and Partial both deal nothing.** A four-band ladder with two live bands, on the irreversible outcome | `t2.py`: degree pairs over one field (A Failure, B Overwhelming) 14, (Failure, Success) 1, (Failure, Partial) 1; A's casualties dealt: 0 |
| **P-iii bounded, monotonic** | the integer subtraction has reachable zeros: power 1 (levy) deals nothing on a Success; any power up to 3 deals nothing in any band against `dr` 4 (walls). A discrete boundary jumping a continuous input, to certainty | `p10_edges.py`: 3,000 light infantry, spearmen or archers against 300 levy behind walls, the defender loses nobody in 60 of 60, each; levy 600 v levy 600 on open ground, the defender loses nobody in 48 of 60 |
| **P-ii uniform leverage** | the pool is `eff_power x (troops / 100) x 0.8`: from 1 die (under 60 men) to 320 (10,000). A sigma modifier moves the net by `softcap x 0.8 x sqrt(pool)`, a headcount edge by `0.4 x pool difference`: the worth of morale, fatigue, stance and shock against numbers falls as `1 / sqrt(pool)`. CR-12's design names this as the fourth route (first audit §5.3) | by construction, algebra shown |
| **P-i legible odds** | no caller can state a field's odds: `field_estimate` exists (first audit §1.1) and cannot see the friction draw, which decides | §2.3 link 4 |
| Phase 4, loops | casualties → smaller pool → lower net → the other side's degree rises and one's own falls to Failure → more casualties, none dealt. Undamped; bounded only by the rout point. This loop is the cliff of §2.3's OFF column and the collapse of §2.3's partition table | `p1_size.py` OFF rows |
| Phase 5, intent | the pair rule's one-sidedness is not a documented intent: the code's own citation for the damage rule reads "Damage is simultaneous. Both sides deal and receive damage" (PP-233, at `battle_loop.py`'s simultaneous-HP block). `[INTENT UNDETERMINED]` for the opposed-degree gate | |

Landing on NERS: P-iv and P-iii on R-COMPLETE; P-ii and the bespoke friction draw on S (a second
convention for one quantity); P-i on E-LEGIBILITY.

### 1.4 R, S, and E last

- **R.** Strategic thought: the dominant order of battle is one body (§2.3). Customisation: fourteen
  troop names, at most nine behaviours (addendum), and a role menu half of which is inert (§3.3).
  Variety in approach: flank, envelop, reserve and pursuit are each worth less than nothing or
  unreachable. The half with no player: two stories of nine (§3). Completeness at the extremes: §3.3,
  and certainty at the integer edges (§1.3). **Fails on every clause but one** (a player can feel
  important in a duel of two blocks).
- **S.** Pauses correctly: a field that is undecided at the one engagement turn a season fights is
  given a winner by arithmetic (first audit F-MB-04); the share undecided is 4% for two season-density
  blocks, 28% at three ranks, 58 to 65% in the flank arms, 33% at 2,400 against 12,000. Consistent in
  methodology: two stamina ladders; walls as armour where the other two terrain rows are dice
  (`terrain.py`: UPHILL and RIVER_CROSSING go onto `terrain_off_d` / `terrain_def_d`, WALLS onto `dr`);
  the opposed-roll obstacle where the tree's rule for an obstacle is the opponent's score halved plus
  modifiers; a LogNormal multiplier where siblings use capped sigma levels.
- **E, as a ratio against the above.** 11,600 lines buy one sound contest between two blocks and a
  hidden draw. The parts that carry the design's ambition (cells, facing, envelopment, reach, roles,
  orders, routes, feints, reserves) are either defeated by the pair rule, inside the friction, or
  unreached. E's second test (the player intuits complex outcomes from simple choices) fails at the
  simplest choice there is: more units should not be worse.

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

**The control that shows the octagon itself works** (`p4_pike.py`, same harness, friction OFF): when the
attacker is ONE body, a 600-horse charge on a braced 600-man block breaks it in 30 of 60 from the front,
41 of 60 from the flank and 55 of 60 from the rear. Front < flank < rear, as the words say. A flank
attack "breaks the line" when the whole army arrives on the flank and stops doing so when a part of the
army does, which is the only way an army ever flanks.

**Through the season's own entry, shipped configuration** (`p7_field.py`, `massbattle.resolve_field` with
`orders_of_battle`, friction ON, open ground, n 100): attacker 1 x 900 against 1 x 900 wins 42; 3 x 300
against 1 x 900 wins **14**, with 48% of its men left against the defender's 96%; **3 x 400, a third
larger, wins 25; 6 x 300, twice the defender's size, wins 22** and never does better than `Partial` in
the other 78. The control the other way (1 x 900 against 3 x 300) wins 66. An army that doubles its
numbers and forms them into six units halves its chance.

### 2.5 P3 — "a pike block holds against cavalry": a braced block holds half the time, and the pike has nothing to do with it

**Verdict: does not hold as worded (EXECUTES, module scale). What holds is "heavy infantry told to
brace"; the pike is a name on the same body.** The addendum showed pike and heavy infantry identical in
one-rank season bodies (F-MB-22, 440 of 440). This lane gave the pike its best case: three ranks, so
that its three support ranks exist (`registry.support_ranks_for`), and a cavalry charge
(`role='Shock'`) at equal numbers.

`p4_pike.py`, n 60 a row, 600 foot (defending) against 600 cavalry, 50 a cell; "holds" = not routed at
the end of the field.

| defender | friction OFF: holds | cavalry wins / foot wins | friction ON (shipped): holds | cavalry / foot |
|---|---|---|---|---|
| pike, no role | 11/60 | 46 / 10 | 36/60 | 24 / 33 |
| heavy infantry, no role | 8/60 | 48 / 8 | 35/60 | 24 / 34 |
| spearmen, no role | 0/60 | 60 / 0 | 30/60 | 30 / 25 |
| light infantry | 0/60 | 60 / 0 | 26/60 | 32 / 17 |
| levy | 0/60 | 60 / 0 | 8/60 | 52 / 0 |
| archers | 0/60 | 60 / 0 | 21/60 | 39 / 12 |
| **pike, ShieldWall** | **30/60** | 27 / 20 | 35/60 | 25 / 30 |
| **heavy infantry, ShieldWall** | **30/60** (identical to pike in 60 of 60 fields) | 27 / 20 | 35/60 | 25 / 30 |
| spearmen, ShieldWall | 4/60 | 56 / 0 | 30/60 | 30 / 22 |
| pike ShieldWall, charged in flank | 19/60 | 39 / 6 | 35/60 | 25 / 29 |
| pike ShieldWall, charged in rear | 5/60 | 55 / 4 | 31/60 | 29 / 26 |
| pike ShieldWall, cavalry not charging (no role) | 41/60 | 17 / 30 | 40/60 | 20 / 32 |
| control: cavalry Shock against cavalry in line | (the line holds 41/60) | 16 / 41 | 38/60 | 21 / 35 |

| # | link | O predicted | C observed | verdict · cause |
|---|---|---|---|---|
| 2 | cavalry does markedly worse against pikes than against other foot | pike well above the rest | unbraced: pike 11, heavy infantry 8, the rest 0 (of 60). Braced: pike 30, heavy infantry 30 | DEPARTS: the difference is the brace and the stat line (power 4, discipline 4), which heavy infantry shares |
| 3 | "holds", usually | well over half | braced, equal numbers: 30 of 60, and the pikes win 20 fields to the horse's 27 | DEPARTS (EDGE of a tuned value, reported as order only: a braced pike block is the underdog against an equal number of charging horse) |
| 4 | frontal and conditional on order | flank and rear much worse | 30 / 19 / 5 | FOLLOWS |
| 5 | pikes are not good at everything | ordinary against foot | heavy infantry against pike is the pike mirror in 60 of 60 fields; light infantry never beats pike (0 of 60) | pike is heavy infantry, so neither better nor worse than it |
| 6 | the word is the weapon | take the pike away and it goes | pike ShieldWall = heavy infantry ShieldWall in 60 of 60 fields: winner, both losses, tick count | **INERT · WORD.** The reach of 0.3 and the third support rank change nothing a braced field can see; unbraced they change 45 of 60 fields and net three more holds, inside the noise |
| E12 | no value changes nothing; no option always best | | under the shipped friction every row from pike to spearmen holds 30 to 36 of 60 and ShieldWall adds nothing (35 against 36): the role, the troop type and the direction of the charge are all inside one draw | DEPARTS |
| E11 | neighbours differ | a charge is better than no charge | charging cavalry (Shock, Arrowhead) loses to the same cavalry standing in line, 16 to 41 (OFF) and 21 to 35 (ON): `H-361`'s "Shock moves the field the wrong way", now with its control | INVERTED · the Shock role |

Finding F-PES-MB-05 (the pike), F-PES-MB-06 (Shock). The addendum's `04_MB_unit_loadout_and_weapon_in_hand_B.md`
is the carrier that would make the weapon a datum the resolver reads; nothing here changes that
proposal, and this table is its falsifier with depth added.

### 2.6 P4 — "a tired unit fights worse": true of a number nobody is shown, false of the number that is

**Verdict: holds inside one field on the column ledger (EXECUTES); INERT on the unit ledger, which is the
one reported; ASSERTED as a state that arrives from a march, a siege or a kit.**

There are two stamina ledgers for one quantity. The **unit ledger** (`Unit.stamina`, `Subunit.stamina`,
0 to 100; drained by `STAMINA_DRAIN_PER_CONTACT_CELL` in `battle_loop.run_battle`; read by
`core/exchange.py::_stamina_pool_penalty`, which takes one die off at exactly zero and nothing above it)
and the **column ledger** (`percell._ColBlock.stamina`, 0 to 100; drained by `MB_STAMINA_DRAIN` 12 a
clash in `percell.update_stamina`; read by `percell._fatigue_sigma`, up to `MB_STAM_SIGMA` 1.5).
`run_battle` returns `a_stamina: unit_a.agg_stamina()`, the unit ledger.

`p5_tired.py`, heavy infantry 600 v 600, friction OFF, n 100 a row; side A enters the field at stamina s.

| A enters at | on the unit ledger: A / B / undecided | on the column ledger | on both |
|---|---|---|---|
| 100 (control) | 36 / 54 / 10 | 36 / 54 / 10 | 36 / 54 / 10 |
| 50 | 36 / 54 / 10 (identical field for field) | **15 / 79 / 6** | 15 / 79 / 6 |
| 10 | 37 / 54 / 9 | 10 / 86 / 4 | 8 / 86 / 6 |
| 0 | **43 / 49 / 8** | 10 / 86 / 4 | 5 / 90 / 5 |

At three ranks the column ledger reads 29 / 40 / 31 fresh and 2 / 87 / 11 at 50. Fresh against fresh,
at the end of 18 ticks (n 40): the unit ledger stands at **99.5 and 100.0 of 100** and reached zero on
0 of 80 sides; the column ledger stands at 35.

| # | link | O predicted | C observed | verdict · cause |
|---|---|---|---|---|
| 1 | tiredness rises with fighting, marching, charging, kit; falls with rest | a state with several sources | the column ledger rises with fighting only; nothing writes either ledger before the field (`seam/wrappers/mass_battle.py` builds both sides new; no stamina field on `MassBattleInput`) | ASSERTED for march, charge, kit, supply |
| 2-3 | monotone; shows in the outcome | more tired, more losses | column ledger: 36 → 15 → 10 wins of 100 | FOLLOWS (column) |
| 2-3 | the same, on the stamina the engine reports | the same | unit ledger: no change at 50 or 10; at 0, with the die off, A wins **more** (43 against 36, inside sampling error of no effect) | INERT; "a number shown that is not the number used" (E12) |
| 5 | persists and recovers on a readable clock | carried between fields | both ledgers are born at 100 in every field; `between_turn_recovery` and `stamina_check` are reached only from `run_multi_turn_battle`, which no season path calls | ASSERTED |
| 7 | heavier troops tire faster | per type or per kit | `MB_STAMINA_DRAIN` is one constant for every troop type; no loadout term (first audit F-MB-19) | ASSERTED: the half of Jordan's carry rule that is a fatigue cost has no carrier |
| S | one quantity, one ladder | | two ledgers, two drain rules, two penalties (a die at zero; a sigma that grows), one of them reported and inert | S defect (two ladders for one quantity) |

Finding F-PES-MB-04.

### 2.7 P5 — "a routed army can be rallied or destroyed in pursuit": neither

**Verdict: does not hold at any depth. Rally is ASSERTED (an empty hook). Pursuit EXECUTES only when
called by hand on a unit whose speed was set by hand, and is then one roll that removes most of what is
left; it does not FORM and cannot FIRE.**

`p6_rout.py`:

| # | link | O predicted | C observed | verdict · cause |
|---|---|---|---|---|
| 1 | rout is not destruction | most of the routed are alive | mirror 600 v 600, n 200, 182 decided by rout: the loser has lost 37% at the end (16% to 88%), the winner 7% | FOLLOWS |
| 2, 4 | it can be rallied | a commander's act, with a draw | `orchestration.rally_check` is `pass` ("Empty hook — rally lands in a future cycle (G-7)"). A routed side put through three further between-turn recoveries, phase boundaries and engagement turns came back in **0 of 60**. `between_turn_recovery` returns at once for a routed unit. `reset_morale_between_battles` clears every rout with no roll and no caller in `engine/` or `modules/` | ASSERTED; and the only code that un-routs anything is unconditional (the standing rule) |
| 2, 3 | or run down in pursuit | the winner's act, best with fast troops | `orchestration.pursuit_damage` is called only by `run_multi_unit_battle`, which nothing in `engine/season/` or `modules/mass_battle/massbattle.py` calls (grep; `massbattle.py`'s own docstring says so) | INERT at EXECUTES from the season's entry |
| 3 | fast troops pursue | cavalry | pursuit is gated on `pursuer.speed == "Fast"`. A side of cavalry, light cavalry or mounted archers built by the season constructors has `Unit.speed == 'Standard'`: speed is a `Unit` field no constructor derives from troop type. Standard pursuer: damage 0 in 115 of 115 | INERT a second way; and "only Fast may pursue" is an eligibility rule that no cavalry can meet |
| 5-6 | pursued against not pursued differs largely | most of the dead fall in the pursuit | by hand (speed set to Fast): one call removes on average **73%** of the routed side's survivors (and up to four times their number); zero in 1 of 115 | EXECUTES by proxy; the size is right for the premise and the form is one roll with no defence, no recall in reach and no choice |
| E11 | the role called Pursue pursues | | `ROLE_SPEC['Pursue']` carries the instruction `pursue`, which `hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES` maps to `None` ("nothing to select") | WORD: a role on two troop types' menus that does nothing |
| 7 | the beaten army is somewhere, weaker | on the map, to be met again | first audit F-MB-11: the loser stays where he stood and the winner stands beside him; the loser's `body` is scaled by the survivor ratio | DEPARTS (theirs) |
| 8 | the record tells rout, rally and pursuit apart | three kinds | `field.won` / `field.lost`; no rout, rally or pursuit kind in `verb_table.yaml`'s `march` row | ASSERTED |

Play-back of a won field, as the engine has it: *two lines met; after a third of one side had fallen the
rest ran; the winners stood where they were; the losers stood where they were too, each man of them
two-thirds the man he had been; next season nobody remembered which way anyone had run.* Finding
F-PES-MB-03.

### 2.8 The premises that failed, in one place

| premise | verdict | first broken link | depth reached |
|---|---|---|---|
| a larger army usually wins but not always | holds for two single blocks; **inverted** for an army in units; the "not always" is one unseen draw | "larger" | EXECUTES (module); INERT at FIRES (first audit) |
| a flanked line breaks | does not hold | "breaks": no sooner than unflanked; an encircled line never | EXECUTES (module, three ranks only) |
| a pike block holds against cavalry | does not hold as worded | "pike": the brace holds, half the time; the pike is inert | EXECUTES |
| a tired unit fights worse | holds on an unreported ledger inside one field; inert on the reported one; no carrier from march or kit | "tired" as a state that arrives | EXECUTES |
| a routed army can be rallied or destroyed in pursuit | does not hold | "rallied" (empty hook); "pursuit" (unreachable; no unit is ever Fast) | none; pursuit EXECUTES by hand only |

## 3. Emergent narrative

Method: enumerate from the code what stories the subject can produce; count them in computed play with
no player, with a control; follow each to what answers it. The story instruments' verdicts are not used
as evidence here; the Event log and `causes[]` are (`p8_season.py`, which reuses the GAME lane's
`pes.py` driver and edge reader; `build_realm(seed)`, the shipped chooser, three seasons).

### 3.1 What mass battle can tell at all (from `verb_table.yaml`'s `march` row and the army verbs)

| # | story shape | owner | can it happen in shipped play? |
|---|---|---|---|
| 1 | walked in: nobody defended, the marchers arrive | `Unopposed` → `field.unopposed`, `army.arrived` | yes |
| 2 | took the field: the defenders lose men, hold a grudge, lose heart; the marchers arrive | `Won` → `field.won`, `army.arrived` | reachable; **never observed** |
| 3 | beaten off | `Lost` → `field.lost` | yes |
| 4 | sat down before the walls | `Invested` → `siege.pressed` | no: `march_postures` ships `[storm]` (first audit) |
| 5 | the place gave itself up | `surrender` → `place.surrendered` | no: withheld verb |
| 6 | a commander set his line and his retreat | `marshal` → `order.marshaled` | no: withheld |
| 7 | an army was raised, formed, ordered, disbanded | the six army verbs | no: withheld |
| 8 | a named man fell in the field | `person.died` on `Won` / `Lost` | reachable; never observed |
| 9 | the beaten rallied; the beaten were run down; a feint drew the pursuit; a reserve was committed late; a general was taken | `rally_check` (empty), `pursuit_damage`, `resolve_feigned_retreat`, `MB_RESERVE_COMMIT`, `command <= 0` | **no path from a season to any of them** (§2.7; first audit F-MB-10) |

Nine shapes; two occur.

### 3.2 What it tells in computed play (counted)

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| shipped scale (`field_troops_per_weight` 1), three seasons: `field.unopposed` / `field.lost` / `field.won` | 3 / 1 / 0 (GAME lane) | 5 / 1 / 0 (GAME lane) | 6 / **3** / 0 (this lane, and theirs) |
| PROXY scale 30 (a labelled proxy: the scale at which a field is a battle; `fixtures.sweep`): the same | 3 / 1 / 0 | 5 / 1 / 0 | 8 / 2 / 0 |
| persons who ever marched, of 82 or 83 | 8 (proxy) | 7 (proxy) | 8 shipped, 7 proxy |

- **No attacker has won a field.** Nine fought fields in eighteen seed-seasons across the two arms, nine
  `field.lost`. At the shipped scale that is F-MB-01's certainty. At the proxy scale the field is a
  real contest and the four fields are four separate small-n losses, so this is "0 of 4, not
  observed", not a rate; but shape 2, the only one in which a place changes hands by force, has not
  occurred in any run of this suite.
- **The one recurring story, read off the log (seed 2, shipped):** the settlement `set_alt_1` is marched
  on in season 0 by `p_npc_007` and in season 2 by `p_npc_037`; both are recorded beaten. Its three
  defenders (`p_npc_011`, `p_npc_089`, `p_npc_090`) are written on by every field they are in, including
  the two they won, and in season 2 one of them marches out and is beaten in his turn. At the end the
  three stand at `body` **1 of 1000**, four others caught in the same fields at 10, 14, 18 and 20 of
  1000. Nobody died
  (`person.died` 0). The cause is F-MB-02's ratio (first audit); what is new is what it does over three
  seasons: the only people the subsystem touches are ground to a thousandth and go on acting.
- **Nothing answers a field.** `field.lost` stands among the causes of no other person's executed act
  in any of the four runs made here (GAME lane: four information acts at seed 2, none at seeds 0 and 1).
  What is answered is the announcement: `march.declared` draws a record, a rumour, a lie and a refused
  challenge from bystanders; `field.unopposed` draws the marcher's own paperwork.
- **A dead-end loop.** Seed 0, proxy arm, season 2: `p_npc_071` forms the same refused march 15 times
  in one season (`march.declared` 16, `march.refused` 15).
- **Control.** The proxy arm moves the marchers' later choices (seed 2: 9 marches in season 2 against
  6) and the size of the wounds (246 to 600 of 1000 instead of 1 to 20), so the
  instrument sees a difference where there is one. It does not move the shape: walk-ins, and attackers
  beaten off.

### 3.3 The questions the work order asks

- **What does a player's choice change?** At module scale, by measurement: how many units he forms (the
  fewer the better, §2.3); whether he braces heavy foot against horse (30 holds of 60 against 8);
  nothing else that survives the friction draw. The role menu, tested row by row against no role
  (`p10_edges.py`, friction OFF, n 60, identical = same winner, both strengths to six places, same tick
  count): cavalry `Pursue`, `Screen` and `Feint`, light cavalry `Pursue` and `Screen`, light infantry
  `Pursue` and `Screen`, archers `VolleyLine`, heavy infantry `Anvil` are **identical to no role in 60 of
  60**; cavalry `Flanker` takes the cavalry from 42 wins to 13; light infantry `Skirmish` from 8 to 5;
  heavy infantry `Hold` and `ShieldWall` from 23 to 36; cavalry `Shock` from 42 to 47 against foot and
  from parity to 16 against 41 against horse. Light cavalry's menu of four is three that do nothing and
  one that loses.
- **The shape of the tail: are all runs the same run?** Yes at the season scale (walk in, or be beaten
  off). At the module scale the tail is the friction draw's: a field's result is known, 96 times in
  100, from two numbers drawn before it.
- **Are the reasons readable afterwards?** No. The field's return is a boolean, a band and two shares.
  The draw that decided it, the arc a body was struck from, who broke first (dark: `field_subunits`
  ships `side`), the stamina that mattered, are not in it. The addendum's proposal for a report
  (`04_MB_manager_battle_one_resolver.md` §5) lists "the day's fortune" among its fields; on this
  evidence that field is the report.
- **Does the story survive the extremes?** (`p11_extremes.py`, `resolve_field`, headcount path.)
  Nobody against nobody: the attacker loses, 20 of 20 (the crash floor of one man a side). One man
  against one: the same. 79, 80 and 99 a side: the attacker loses 20 of 20 (F-MB-01). 101 against 99:
  the attacker's "survivor share" is 1.01 (F-MB-02). 10,000 a side, the stated ceiling
  (`MAX_TROOPS_PER_UNIT`): resolves, a quarter of a second a field. 20,000 a side: past the ceiling,
  not refused, resolves. Six units against one: §2.3. 2,400 against 12,000: a third of fields undecided
  at the cap. Integer armour against integer power: §4, F-PES-MB-07.

