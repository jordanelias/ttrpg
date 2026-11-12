# SE — pessimist audit: NERS, premise and emergent narrative, of settlements, territory and economy

## Status: REFERENCE (an audit; resolves nothing at runtime)

Scope: `modules/settlements/`, the season loop's economy, migration, founding and hunger effects
(`engine/season/loop/effects_economy.py`, `effects_migration.py`, `effects_founding.py`), geography, the
campaign supply layer that feeds mass battle, and six premise sentences of a place. The first audit
(`audits/07_SE_audit.md`) and its addendum (`07_SE_audit_addendum_B.md`) and the ten `07_SE_*` proposals
are cited, not redone. Everything measured here is new work unless a finding id of theirs is named.

All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_SE/`.

(Sections below are appended as the work proceeds; §0, the verdict, is written last and placed first.)

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the six sentences the work order names). The
ordinary account O in §2.1 was written before this lane opened any settlement, economy, migration or
founding file, any SE audit or any SE note; it is from the words.

### 2.1 O — what each sentence should mean (written first)

**P1 "A town that cannot feed itself starves, shrinks and is blamed."**
1. A town has mouths (people) and food (what its ground yields, what it stored, what it bought or was
sent). 2. "Cannot feed itself" is a comparison the game makes each season or year: food available against
food needed; the shortfall has a size. 3. A store delays hunger: a town with a full granary survives one
bad year; hunger starts when the store is gone. 4. "Starves" is a state of the town with degrees (short
rations, hunger, famine), proportionate to the shortfall and its duration. 5. "Shrinks": people die or
leave; the loss is proportionate to the shortfall (a 10% shortfall is not a 50% loss), and it is by a
draw, not a fixed fraction (standing rule). 6. Shrinking lowers the need, so hunger is self-limiting: a
town shrinks toward what its ground can feed, it does not go to zero unless the ground gives nothing.
7. Zero: a town that can feed itself does not starve, shrink from hunger or get blamed for hunger.
8. "Is blamed": somebody is held responsible by somebody. The ordinary reading is that the hungry blame
whoever rules them (the lord, the steward, the council), and a neighbour or rival may be blamed if he
caused it (a siege, a seized harvest). The words "is blamed" with the town as subject could also mean the
town is blamed by its lord for failing its dues; the first reading is the commoner one. 9. Blame has a
consequence: lost standing, unrest, a deposition, a grievance somebody acts on. Blame with no consequence
is a log line. 10. Blame fits the cause: a ruler who emptied the granary for a war is blamed more than
one who met a drought with an open store. 11. Feedback: the player can see the town is hungry before it
starves, see why, and see who is blamed. 12. [GENRE] the player can do something: send food, buy grain,
cut the levy, move people. 13. Hunger also weakens what the town gives: fewer levies, less tax.

**P2 "A good harvest and a bad one differ."**
1. A harvest is the yearly (or seasonal, at the season it falls) yield of a place's ground. 2. It varies
by a draw: weather or luck, not a constant. 3. Its size depends on the ground (fertile land yields more),
the hands (too few workers lowers it), and disturbance (war on the fields, a siege). 4. "Differ": the
difference is visible in the stores and then in what follows: a good year fills the granary, lets the
town grow, sell or feed an army; a bad one draws the store down and, if repeated or severe, starts P1.
5. The difference is in proportion: one bad year after good ones is a tight winter, not a collapse; two
or three are a famine. 6. Neighbouring places share weather to a degree (a regional bad year) and differ
to a degree (one valley's flood). 7. The spread is wide enough to matter and narrow enough that the
ground still matters more than the luck over ten years. 8. Feedback: the record says "a poor harvest at
X", so a later hunger traces back to it. 9. Zero: a place with no farmland has no harvest and lives by
trade. 10. [GENRE] the season matters: harvest comes in autumn, hunger bites in late winter and spring.

**P3 "People leave a failing place."**
1. A place fails when it is hungry, unsafe (raided, besieged, lost a battle nearby), ruinously taxed or
badly ruled. 2. People are counted; leaving reduces the count there. 3. They go somewhere: a named
destination that gains them, near enough to walk to, and better off than where they left (conservation:
those who leave arrive, less those lost on the road). 4. The rate is proportionate to how badly the
place fails, and by a draw. 5. Not everyone can leave: the bound, the poor and the old stay; the first
to go are those with means or nothing to lose. 6. Zero: a thriving place does not lose people this way,
and it attracts them. 7. Leaving has consequences at both ends: the origin's labour, levy and tax fall
(a spiral or a relief, since fewer mouths); the destination gains hands and mouths, perhaps strain and
resentment. 8. A ruler notices and can respond (hold them, lure them, fix the cause). 9. A place can
empty and be abandoned; that is an ending the record states. 10. Named persons leave too, or pointedly
stay. 11. Feedback: the record says who left where and why.

**P4 "A founder builds something that lasts or fails."**
1. A founder is a person (named) who starts a new thing: a settlement, in this scope (it could be a
house, an order or a company). 2. Founding takes an act, a site, people and stock; it costs the founder
and the place the people came from. 3. The site matters: good ground, water, a road. 4. The outcome is
open at the founding: it "lasts or fails" over the following years by its ground, its luck (a draw),
its neighbours and what the founder does. 5. Failing means the place is abandoned or absorbed, its
people dead or returned, and the record says so. 6. Lasting means it grows into a place like the
others, with its own people and character, and outlives the founder. 7. The founder is bound to it: it
is his name on it, his standing rises or falls with it, his death early matters. 8. Both outcomes occur
in computed play in a visible share; a founding that always lasts or always fails is not this sentence.
9. Zero: nobody founds, nothing new appears. 10. [GENRE] the player can found, and choose where.

**P5 "Trade moves goods to where they are wanted."**
1. Goods are kinds (grain, timber, iron, cloth), held in amounts at places. 2. "Wanted" is a shortage or
a higher price at a place: demand over supply. 3. Trade is a movement along a route between places that
are connected (a road, a river, a neighbour), by somebody (a merchant, a caravan) or by an abstract flow.
4. Goods move from surplus to shortage: the source's stock falls, the destination's rises (conservation,
less a loss on the way). 5. The amount moved is proportionate to the difference and limited by the route
and the distance. 6. Trade relieves shortage: a hungry town with a rich neighbour and an open road is
less hungry than the same town cut off (the control). 7. Trade can be cut: war, a closed road, an
embargo, a siege, bandits; cutting it hurts the one that depended on it. 8. Somebody profits: the
carrier or the selling town gains coin. 9. Zero: no difference in want, nothing moves; no route, nothing
moves. 10. Feedback: the record names what moved and from where to where. 11. A draw: caravans are lost.

**P6 "A place has a character from its ground and its people."**
1. Ground: terrain, soil, water, resources, position (coast, pass, river). 2. People: how many, of what
callings, faiths, loyalties, origin. 3. Character: a set of traits of the place a player could name
("a poor hill town of shepherds, stubborn, loyal to the old house") that follow from those two.
4. Character has effect: what the place yields, what troops it raises, how it takes a tax, a new lord
or a faith, what it resists. 5. Two places on different ground differ; the same ground with different
people differs. 6. Character changes slowly when its causes change: migrants change the people; a mine
changes the ground's use; a sack leaves a mark. 7. It is not arbitrary: a trait with no cause in ground
or people is a label; a cause with no trait is unused data. 8. Feedback: the player can read it and
predict from it. 9. [GENRE] character gives a place a reason to be wanted or avoided.

### 2.2 N — what the code's notes say in aggregate (the second account)

Built from the docstrings and roster notes of `modules/settlements/*.py`, `loop/matter.py:585-800`,
`loop/effects_economy.py`, `effects_migration.py`, `effects_founding.py`, `rosters.yaml` (`site_yield`,
`works_cost`, `capacity_floor`, `hunger_bands`), `data/fixtures.py` and `seam/wrappers/mass_battle.py`.

- **Hunger.** Only a cohort eats (`larder.py`, ED-IN-0255). It draws `weight × Person.weight` of each
  weighted kind from the first rung up its ladder that holds any. A shortfall "emits nothing and decides
  nothing" (L5, `matter.py:651-663`); it falls the cohort's body by `body_step × units short`; death is at
  body 0. A shortfall is *reported* only when a stocked larder runs dry with a mouth unfed, as an
  Observation on that larder's write; a larder never stocked and every later empty season are silent by
  declaration (`matter.py:627-631`). The consequence of a report is "somebody's own later choice". There
  is no note anywhere about blame, fault, grievance or unrest: the word does not occur in the engine
  outside a probe label (`grep -i blame engine/season`: four hits, none a mechanism).
- **Harvest.** Yield is a Site's base times its condition times a season factor; "WHAT A HARBOUR PRODUCES
  IS INVENTED" (`rosters.yaml:3516`). The factor is a constant 1.0; a per-territory draw exists and ships
  off (`season_factor_draw=()`).
- **Leaving.** `migrate` is "a verb persons take" (RR-2); it re-homes presence and residence and is
  refused at capacity. Nothing in the notes ties leaving to failing; the cause of a migration is whatever
  the chooser scored.
- **Founding.** `found` mints a hearth or a community (never a settlement: "unpriced", `rosters.yaml:1973`),
  moves a 10-grain stake into it and opens the founder's `hold`. `build` mints a Site at condition 0.
  "The world only decays" (ARCH F.20) is the stated reason for the pair. No note says how a founded place
  ends; `raze` ends an occupied *settlement* only.
- **Trade.** `exchange` is two store moves between two rungs, of fixture kinds and fixture amounts
  ("the design names an exchange's two sides and supplies no ..." `fixtures.py:627`). No note speaks of
  want, price, route or distance. `transfer` is a gift or a payment.
- **Character.** No note. A settlement is a Rung with Sites; every settlement is stamped with the same
  Sites (`populated.py:1215-1261`); the canon map's descriptors are untyped strings nothing reads.
- **Supply.** A treasury provisions a field at the larder's ration; shipped off; the treasury is the
  marching seat's rung.

The notes are candid: they describe an accounting kernel and say what it does not do. The aggregate N
account is therefore much narrower than O, and narrower than the six sentences: N contains no blame, no
cause of leaving, no failing of a founded thing, no want, and no character.

### 2.3 The running code, link by link

Runs: `kernel.py` (pure module calls); `pes_noacts.py famine|harvest|room` (the built realm, the real
`SeasonDriver`, a chooser that returns nothing); `pes_play.py SEED 2 fed|fail` (computed play, two arms
that differ only in whether eleven towns can feed themselves); `pes_found.py` (`tiny_world`, the
founding test's own helpers); `pes_supply.py`. Each row names the run; the control is the other arm.

**P1 "A town that cannot feed itself starves, shrinks and is blamed."**

| O link | running code | verdict |
|---|---|---|
| 2 a shortfall with a size | yes: `want − take` per kind (`kernel.py` K1) | holds |
| 3 a store delays hunger | yes at the home rung; at a rung above it only if home holds exactly 0 of the kind (K1: home 1 grain, granary 1,000 above → short 3; home 0 → fed). Known as H-303 | holds, with a known defect |
| 4 starving has degrees | four bands (`hunger_bands`), read by `census` and nothing else | holds as a label |
| 5 shrinks, in proportion, by a draw | **no.** Population is `Person.weight`, which no rule writes. The famine arm: eleven towns with no food, bodies 1000 → 598 → 196 → all eleven cohorts dead at season 2 (`body_step` 67); population per town steps from 2 to 0 in one season; nothing drawn (`subsist.py` takes no rng) | **fails**: whole or nothing, no draw |
| 6 self-limiting | no: want does not fall as the body falls; the town goes to zero | fails |
| 7 zero case | yes: the 26 lowland cohorts stay at 1000 | holds |
| 8-10 is blamed, with consequence, fitted to cause | **nothing.** Famine arm: 0 shortfall Observations in six seasons; no person holds a claim; `person.died` carries `causes=[ROOT]`, `observed=()` (`matter.py::_die`). Play arm: 0 Observations, 0 persons holding a shortfall claim, in two seasons with eleven starving towns | **fails**: no link exists |
| 11 visible before it starves | the band is computed and not delivered to any person | fails |
| 12 somebody can act | `transfer` exists; in the play arm no `transfer`, `exchange` or `requisition` entered a starving town (0 of the 10 `transfer` and `exchange` attempts by highland residents executed) | fails in computed play |
| 13 hunger weakens the town's dues | no: yield reads no person (the eight emptied towns go on mining 49 ore a season each with population 0); levy reads weight, which did not fall until death | fails |
| named residents | the eleven named persons living in the eleven starving towns hold body 1000 and all survive: only a cohort eats (ruled, ED-IN-0255) | by ruling; surprising to a genre player |

Under computed play the sentence fails earlier still: each starving cohort spends an act on `tend` and
restores itself to 1000 in the season it fell (`body.tended` 11 and 10 in the two seasons of the fail arm,
0 and 1 in the fed arm), so a town with no food at all never weakens. Known as H-304; measured here against
its control.

**P2 "A good harvest and a bad one differ."**

| O link | running code | verdict |
|---|---|---|
| 2 varies by a draw | shipped: no. Every season yields the same (4,810 units, falling 1% a season with wear). With the draw arm on, a factor of 0.5, 1 or 2 per territory per season (144 territory-seasons at seed 0: 52 / 43 / 49, mean 1.16) | fails as shipped |
| 3 depends on ground, hands, disturbance | no ground (every settlement has one harbour and one seam), no hands (yield reads no person), no disturbance (a march through a territory does not touch a Site) | fails |
| 4 differs in what follows | weather arm on, shipped realm, eight seasons: every settlement `fed` every season, 0 deaths, one body value. The realm produces about 21 times what it eats, so half a harvest is still ten times enough | **fails**: a difference in a number nobody uses |
| 6 regional | independent per territory; no correlation between neighbours | partial |
| 8 the record says so | no. `yield.taken` carries one receipt with `delta=None` and `observed=()`; no Event or Observation in the run names a factor, a harvest or weather (count 0) | fails |
| 9 no farmland, no harvest | grain is yielded by a **harbour**; timber by a **seam**. There is no field, farm or forest Site kind | names fail |
| 10 the season matters | no: all four seasons yield alike; with the arm on, winter draws from the same table as autumn | fails |
| what the weather touches | the factor multiplies every Site on the rung: ore and timber move with it (ore 2,375 → 1,688 → 1,806 across three seasons while grain moves 1,900 → 1,343 → 1,436) | a bad harvest halves the mine |

**P3 "People leave a failing place."**

| O link | running code | verdict |
|---|---|---|
| 1 failing is a state the game knows | hunger band only, and no person is told it | partial |
| 2-3 they go somewhere that gains them | **nobody goes.** Play, seed 0, two seasons: starving-town cohorts attempted `migrate` 16 times (fail arm) against 12 (fed arm) and executed 0 in both; lowland cohorts attempted 36 and 35, executed 0. Every executed `move` in both arms names the mover's own rung | **fails** |
| 4 rate proportionate to failing | attempts per cohort per two seasons: starving 1.45, the same towns fed 1.09, thriving lowland 1.35-1.38. One seed; the starving and the thriving are not separable | fails |
| can they | yes by ladder and room: at build a cohort has 1,116 of 1,369 other-settlement pairs open (`room_s0.txt`). The refusals are of what the chooser names, not of the map | the block is the choice of destination |
| 6 a thriving place attracts | no rule reads a destination's stores, hunger or safety | fails |
| 7 consequences at both ends | none could occur: a cohort's leaving would move weight 2 and its whole draw; the origin's yield would not change (reads no person) | fails |
| 9 a place can empty and the record says so | it empties by death and then reads `fed`; no Event names an abandonment | fails |
| 10 named persons leave or stay | named persons do change residence (first audit: 16 in three seasons, five people, the Spymaster four times), for reasons unrelated to any failing | not this sentence |

**P4 "A founder builds something that lasts or fails."**

| O link | running code | verdict |
|---|---|---|
| 1 a founder starts a settlement | a settlement cannot be founded: `found` of a `settlement` under a duchy is `found.refused` (no price row). A hearth and a community can | narrowed to a household plot |
| 2 it costs | 10 grain, moved into the new rung (so the founder's side loses nothing that leaves the world) | holds |
| 3 the site matters | no: `_eff_found` reads no draw, no capability, no condition, no terrain, no yield | fails |
| 4-5 open outcome; can fail | **cannot fail.** A founded hearth left alone for 40 MATTER barriers: still exists, stores `{grain: 10}`, 0 residents, 0 Events naming it. With a dwelling built: the dwelling stands at condition 0 for 40 seasons and the hearth's capacity reads 1. No rule ends a Rung but `raze`, which targets settlements | **fails**: every founding lasts, as an empty lot |
| 6 lasting means it grows | no: nothing moves in unless a person chooses `migrate` there; nothing grows | fails |
| 7 the founder is bound to it | a `hold` edge, opened at founding. No standing, no name, no consequence of his death on it | partial |
| 8 both outcomes in computed play | neither: `found` 0 executed of 7 attempted and `build` 0 of 4 (first audit, seed 0, three seasons); here 0 of 2 and 0 of 1 per arm in season 0 | fails |
| the draw | none; certain on eligibility (determinism sweep C-15) | fails the standing rule |

**P5 "Trade moves goods to where they are wanted."**

| O link | running code | verdict |
|---|---|---|
| 2 wanted is a shortage or a price | no price exists; a shortage is known to the engine and, when never stocked, to no person | fails |
| 3 a route | none: any rung to any rung, at no cost of distance (H-328) | fails |
| 4-6 moves from surplus to shortage, relieves it | **nothing moved.** Fail arm, two seasons: the eleven hungry towns hold ore 1,639 and timber 319 and no food; the 26 others hold a growing food surplus; `exchange.made` 0, `transfer.made` into a hungry town 0, `requisition.taken` 0. Highland food at the end: 0 grain, 0 salt | **fails** |
| direction of attempts | hungry-town cohorts attempted `exchange` 4 times against 10 by the same towns when fed, and `transfer` 4 against 12: **want lowers the attempt to trade**, because the fixture offers `grain` for `salt` and a town with neither has nothing the row can name | inverted |
| 7 can be cut | nothing to cut | fails |
| 8 somebody profits | `coin` is a registered kind that nothing yields, holds or reads | fails |
| what is produced for trade | of 4,810 units a season, 222 are eaten; ore (1,850 a season, the largest yield) has no reader in any roster, cost or rule; timber's one use is `works_cost`, never paid in play | goods with no want |

**P6 "A place has a character from its ground and its people."**

| O link | running code | verdict |
|---|---|---|
| 1 ground | every settlement: one harbour, one seam, one garrison (first audit F-SE-01); terrain reaches the battlefield only (F-SE-06) | fails |
| 2 people | every settlement: one cohort of weight 2 (`room_s0.txt`: 37 of 37), with no calling, faith or loyalty of its own | fails |
| 3-5 a nameable character with effect | the only per-place variation at build is the venue list by settlement type and how many named persons live there (population 2 to 12, capacity 1 to 9). No yield, levy, tax response or resistance reads either | fails |
| 6 changes slowly with causes | no writer | fails |
| 8 readable and predictive | a player can predict every place exactly, because they are the same place | fails by sameness |

### 2.4 The three accounts compared

| sentence | O (ordinary) | N (notes) | running code | genre surprise | intent | names |
|---|---|---|---|---|---|---|
| P1 hunger | starves in degrees, shrinks in proportion, blame lands on a ruler and costs him | a cohort's body falls; a crossing is reported; nothing is decided | falls whole, silently when it matters most, erased by `tend` under play; nobody blamed | high: the lord of a dead town is untouched and unremarked | fails at "shrinks" and "is blamed" | "starving" names a band nobody reads |
| P2 harvest | a yearly draw with consequences and a record | a constant, with an off-arm draw | no difference shipped; with the arm on, a difference in an unused number | high: no seasons, no bad year | fails | grain from a harbour, timber from a seam |
| P3 leaving | the failing place loses people to a better one | a verb persons take, throttled by room | nobody leaves anywhere; the hungry try no more than the fed | high | fails | `migrate` executes only for courtiers |
| P4 founding | an open bet that pays or fails | a hearth is minted and held | certain, never fails, never used; a town cannot be founded | high | fails | "found" founds a plot |
| P5 trade | goods flow down a gradient of want along routes | two store moves of fixture kinds | nothing moves; want lowers attempts | high | fails | "exchange" has no price |
| P6 character | ground and people make places differ, with effect | none | 37 copies | high | fails | — |

**All six premises fail by execution.** Three fail at a link the notes never claimed (blame, the cause of
leaving, character): those are absent mechanisms, and the notes are honest about it. Three fail at a link
the notes do claim (hunger falls a body and may kill; a harvest varies; a works grows the world): there
the code does what the note says and the result is not what the sentence means, because the surrounding
world erases it (`tend`), dwarfs it (a 21-fold surplus) or never reaches it (`exists:works=0`).

## 1. NERS

Method: `skills/ners/SKILL.md`, instrument A (the object ledger). Instrument B (`resolution-diagnostic`)
has almost nothing to act on, and that is its finding: **the settlement layer contains no live draw.**
`larder_draw`, `subsist`, `produce`, `housing`, `fabric`, `fortification` and `provision` each say "draws
nothing, so it takes no rng" in their own docstrings; `work`, `restore`, `sabotage`, `transfer`,
`exchange`, `move`, `migrate`, `found`, `build` and `raze` are uncontested and certain on eligibility
(`18_DETERMINISM_SWEEP.md` C-09, C-15, C-08); the one draw the layer owns, the season factor, ships as the
empty table. So who goes hungry, how much body is lost, who dies, what a site yields, whether a wall
holds its value, whether a founding takes and whether a saboteur succeeds are each a fixed function of
state. The one draw that exists when its arm is on is not the engine's: `season_factor_of` takes
`draw.choice(outcomes)` over equally likely multipliers (`world_q.py:1203-1205`), a second way of being
uncertain beside the pool, obstacle and four-band ladder (`degree_from_net`), which is an S defect in
itself (calculations consistent in methodology). F-PES-SE-02.

**A correction owed to another lane.** `18_DETERMINISM_SWEEP.md:110` lists `world_q.subsistence_draw`
among the code that is "not a finding (checked) ... (drawn)". The word is a homonym: it is the *draw on
the larder*, arithmetic over stores in sorted id order, with no rng in its signature (`larder.py:39`,
`world_q.py:1361-1401`). Hunger is not drawn. Listed for the sweep's owner in §6.

### 1.1 The object ledger: each object's N-line, the cut, and what died

"Computed play" is the two-arm run of §2.3 and the first audit's `aperture 3 0`; "in principle" is the
hand-built or barrier-only run. A cut that costs nothing in computed play is a **false N-line today**;
one that would cost nothing even in the worlds built to exhibit it is a **false N-line**.

| object | its N-line as the notes give it | the cut | what died (measured) | verdict |
|---|---|---|---|---|
| `settlements.produce` (grain, salt) | the economy's only source | zero the harbour table | the famine arm: eleven cohorts fall and die | **true**, the layer's one unconditional N-line |
| `settlements.produce` (ore) | a seam yields | delete the `ore` cell | nothing, in any world: no rule, cost, weight or roster reads `ore` (grep: three hits, all the registry and the yield cell). 1,850 of 4,810 units a season | **false N-line** |
| `settlements.produce` (timber) | pays for fabric | delete the cell | nothing in computed play (`build` 0 executed); hand-built `build` would refuse | false today |
| `Rung.yield` | "last season's product" | delete the field and its write | nothing: written 37 times a season, read by no code outside `harness/` and tests (grep) | **false N-line** (a write-only field) |
| `larder_draw` + `subsist` | scarcity binds a body | remove the shortfall (the fed arm against the fail arm; `body_step` 0 itself was not run) | barrier-only: the eleven starving cohorts live instead of dying. Computed play: `body.changed` and `body.tended` vanish and no settlement reading moves (41 of 44 starving cohort-seasons end at body 1000 anyway) | true in principle; **false in computed play** (H-304) |
| the shortfall Observation | a dearth reaches a person | drop `short_seen` | nothing in the realm in either arm, two seeds (0 Observations); one `transfer` of 8 salt in `scarce` | false today; true in one fixture |
| `world_q.hunger` and its bands | a settlement's need is readable | delete | nothing: read by `census` and a probe label | **false N-line** |
| `settlements.housing` (capacity) | the throttle that makes `found` and `build` matter | set the floor to 99 | `migrate` refusals for room stop (79 of 116 at seed 0); the acts they refused are courtiers re-homing; `found`/`build` do not execute either way | holds as a refusal, **false as a throttle** |
| `settlements.fabric` (ceiling, share) | a works paces its fabric | return scale and 1/1 | nothing in computed play (`work`, `restore` 0 attempted; `sabotage` 0 executed) | false today |
| `settlements.fortification` | walls are the garrison's condition | return 1.0 | nothing outside a siege: `wear_per_season.garrison` is 0, so every settlement reads 1.0 until `besiege` wears one (MB's) | narrowed to one consumer |
| `settlements.provision` | stores bound the troops fielded | ships off (identity) | nothing shipped; **on**, every side of every field is cut to nothing (§1.2 A-2) | false shipped, destructive on |
| the season factor | weather | ships `()` | nothing shipped; on, a change in stores nobody draws on (§2.3 P2) | false today |
| Site wear | a worn place produces less | zero the rates | yield stays 4,810 instead of falling 1% a season; first band crossing is at season 21 (first audit F-SE-05) | false inside any run length used |
| `found`, `build`, `works_cost` | the world grows | delete | nothing: 0 executed in every realm run read (first audit; both arms here) | false today (cited from `16_PESSIMIST_GAME.md` §3) |
| `raze` | a town ends | delete | nothing: 0 executed | false today |
| `exchange`, `default_return_kind` | both sides' stores move | delete | nothing: 0 executed in any realm run | false today |
| `transfer` | matter moves by an act | delete | per season, one unit of grain no longer moves from a town into its own cohort's person-rung, where no draw reaches it | false today |
| `migrate` (cohort) | the people move | forbid cohorts | nothing: 0 of 155 cohort attempts executed across both arms and two seeds (and 0 of 84 by named persons in those four runs) | **false N-line today** |
| the geography file's adjacency, costs, budget | the map | delete the keys | nothing (first audit F-SE-06, grep) | false N-line |
| `coin` | a matter kind | delete the row | nothing: no yield, no holder, no reader | **false N-line** |

**Count.** Of twenty objects, one N-line is true without qualification (food production), two are true
in principle and erased in computed play (the larder's bite; the shortfall report), one is narrowed
(fortification), and sixteen are false today, of which five are false in every world (ore, `Rung.yield`,
the hunger bands, the unread geography keys, `coin`). N tested from the six directions: every false line
above is false top-down (no realm reading changes), bottom-up (no person's options change), vertically
(nothing crosses a scale: the field's troops ignore the stores), laterally (no sibling subsystem reads
it) and horizontally (no settlement differs); the one direction in which several hold is diagonal, by
way of a hand-built fixture (`scarce`, `test_works_founding`), which is the narrowing the charter names.

### 1.2 The other attack: what survives because nothing was tried against it

**A-1. The granary feeds towns in id order, and the town that loses eats nothing and is not reported**
(`kernel.py` K2). Two towns on one territory granary holding half of what both want: the first in sorted
id takes its whole ration; the second takes nothing, its body falls by 60, and `shortfalls` is empty,
because the first eater drained the rung *exactly*, so the second eater's walk finds no rung holding
more than 0, records `source None`, and `subsist` marks nothing as drained (`larder.py:55-64`,
`subsist.py:55-57`). So the one moment the notes say a dearth is reported (the crossing, `matter.py:629`)
is missed whenever the last fed mouth empties the store to the unit. The control: give the granary one
unit more and the second town's shortfall is reported. Under the first lane's granary proposals
(`07_SE_ground_and_granaries.md`, `07_SE_treasury_granary_B.md`) every relief stock is a shared rung, so
which town starves in a dearth would be decided by settlement number, every time, with no draw and no
rationing. F-PES-SE-03.

**A-2. Turning the shipped supply fixture on disarms the realm** (`pes_supply.py`). `provision` fields
`min(weight, min_k stores[k] // ration[k])` from the marching seat's rung (attacker) or the nearest held
rung (defender). After two seasons of yield the realm's 34 offices sit at 17 territory, 10 duchy, 4 realm
and 2 foreign-settlement rungs and one sits nowhere; **none** of those rungs could ration one man, and
the defender's treasury of all 37 settlements is a territory rung holding nothing, while 9,250 units lie
at settlement rungs no army reads. So `field_provisioning=True` (a registered sweep arm, H-241) makes
every side field 0, lifted to 1 by the crash floor (`massbattle.py:212`), or to one man per commanding
person in the `person` arm (`:328`): army size stops mattering in every field. The edges of the entry
itself: 100 men on 10,000 grain and no salt field 0; on 10,000 grain and 1 salt, 1; a side with no seat
fields 0 whatever it holds. The first lane's F-SE-17 and F-SE-20 name the misplaced treasury; what is
added is the reading that the arm is not merely unbalanced but inverts the field. F-PES-SE-05.

**A-3. A second garrison never strengthens a town, and a new one halves it** (K4). `fortification` is the
mean of garrison conditions: (1000) reads 1.0; (1000, 1000) reads 1.0; (1000, 0) reads 0.5. `build` mints
a Site at condition 0 (`effects_founding.py:234`), so building a garrison in a walled town is an act of
self-harm until it is restored, and at full repair it has bought nothing. F-PES-SE-08.

**A-4. One hand, one act, the whole fabric** (`effects_economy.py:131-157`, read; never executed in
play). Alone at a rung, one `restore` raises a Site from 0 to its ceiling and one `sabotage` takes a
harbour from 1000 to 0, with no draw. The share is one over the *persons* present, so a cohort of any
weight counts as one hand, and a bystander halves the worker's effect: a busy town mends more slowly per
act than an empty one. Tagged `[ASSUMPTION; medium; Jordan to correct]` in the code; determinism is the
sweep's C-15. Recorded here for its size: the day `sabotage` first executes in the realm, a town loses a
harbour's whole yield to one act by anyone standing there.

**A-5. A founding's stake is food nobody can eat, and a built dwelling is a zero that counts** (`found.txt`).
The 10 grain staked into a founded hearth is drawn on only by a cohort residing at or under that hearth;
none does, so it is inert, forever. A dwelling built and never restored sits at condition 0 for 40
seasons, counts 1 toward capacity (H-307, known), and emits `condition.worn` every season for a wear of
zero (F-SE-08, known). `build` also leaves a `timber: 0` key in the payer's stores, the digest pollution
`provision.py`'s own docstring says it avoids.

**A-6. Hunger's toll grows with the size of the town, not with how hungry it is** (K3; known as H-305 and
resolved per head by `07_SE_population_census.md` R1; re-measured so the size is on record). At the same
total shortfall a weight-2 cohort dies in 17 seasons, a weight-10 in 4, a weight-50 in one; a weight-400
cohort dies in one season of a **10%** shortfall. Every shipped cohort is weight 2, so this is latent
until any census writer lands; it must land with R1 or before it.

### 1.3 R: the half with no player, and the extremes

- **No player.** Barrier-only, the layer emits `yield.taken`, `stores.changed`, `condition.worn` and (in
  a hungry world) `body.changed` and `person.died`, identically on every seed (the first audit's table:
  seeds 0 and 1 agree to the unit). It throws no hook: no Event names a place as short, rich, emptied,
  founded or cut off. R-WORLD fails for every settlement seat.
- **Zero population** (famine arm, seasons 2-5). A town with no people reads `fed`, keeps capacity, keeps
  yielding from its seam (about 49 ore a season each), keeps its named residents at full body, and is
  marked by nothing. First audit F-SE-02 measured this at ×20 need; here it is measured in a world where
  only some towns die, so the contrast is inside one realm.
- **One person.** A settlement whose only resident is a named person has no eater and no hunger; all of
  P1 is undefined for it.
- **Large weights.** A-6.
- **A hundred claimants on one granary.** A-1: the first by id eats.
- **Negative, zero and fractional amounts.** First audit F-SE-10.

### 1.4 S: pauses, and one methodology per quantity

1. **One ration, two clocks.** `subsistence_weight` is what a cohort eats *per season* (`larder.py`) and
   what a soldier eats *per field* (`provision.py`: "a field eats as the people it is made of eat"). An
   army that fights twice in a season eats two seasons' food; one that marches all year and never meets a
   field eats nothing from its treasury, and its cohort also eats at home (first audit F-SE-20). Two
   ladders for one quantity.
2. **One crowd, three sizes.** A cohort is `weight` mouths at the larder, `weight` places in housing
   (so the people of a town occupy two dwellings, as much room as two courtiers), and one hand at a
   fabric (`share`) and one person on the ladder.
3. **Two ways of being uncertain** (above): the four-band ladder everywhere else, a uniform choice among
   multipliers here.
4. **"Fed" has two meanings.** A town of the well-fed and a town of the dead read the same band.
5. **Pauses correctly.** The layer never pauses for another scale and never needs to: nothing in it asks
   a person, a contest or a field for an answer. A dearth does not open a question a player is put (the
   question forms only from a held claim, and no claim is deposited: §2.3 P1). That is smoothness by
   absence.
6. **Zooming.** The campaign scale reads the settlement scale at one point (the treasury) and reads the
   wrong rung (A-2); the settlement scale reads the personal scale nowhere (yield reads no person's
   labour); the personal scale reads the settlement scale through `tend` alone.

### 1.5 E, last, against what N and R found

Counted as overhead against what it buys: eight module entries, ten verbs, some twenty roster tables and
fixtures, and the larger part of `loop/matter.py`, buying one unconditional possibility in computed play
(food is produced) and three more in hand-built worlds (a dearth relieved once; a hearth founded; a
fabric raised). The kernel is small and clear; the ratio is poor because the possibilities are missing,
not because the code is large. E does not improve by cutting the kernel (the first audit's steelman 5
holds: it is the architecture). It improves by deleting what is false in every world: the `ore` cell or
else a reader for it, `Rung.yield`, `coin` until something mints it, the hunger bands until a person can
be told one. And it worsens with each new table added before one of the six sentences executes.

