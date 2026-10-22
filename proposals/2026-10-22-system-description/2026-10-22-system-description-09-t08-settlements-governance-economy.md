# Tutorial: Settlements, Governance and Economy (GV + EC) — hold a seat, feed a place, pay your men, and build

Repo `jordanelias/ttrpg`, written at HEAD `a4ca9a5`; revised in round 3 against `51d7b05` (PR #494 included) and the precedent suite
(`research/game_precedent_suite/`, reference, tier 3). The round-3 changes are listed under §8 "Round-3 corrections". Paths below
are under `engine/season/` unless written in full.

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that spends a per-season budget
of scene actions (base `scene_budget=5`, `data/fixtures.py:228`; see "Your budget" below) on acts from a closed table of
verbs (`verb_table.yaml`). "You" below means
the acting person: a player's character if one is ever seated, an NPC today. The tutorial teaches what you can do, what
the rules do with it, and what you must arrange to reach a goal; anything that exists only in a proposal is tagged
**[PROPOSED]** and kept in §7.

**What you need from other subsystems.**
- *Persons* (NP): who you are, where you stand (`contain`), where you live (`reside`), and your ledger of claims.
- *Decision layer*: forms your candidate acts from questions about things you hold claims on; it never reads the world.
- *Information* (WITNESS): how you learn that a larder ran dry, or that a man swore to your seat.
- *Factions* (FA): a faction is a Proposition plus `commit` edges; it decides who may revoke whom ("same faction").
- *Mass battle* reads garrison condition (`fortification_of`) and who holds a place; *social contest* opens the
  `ban`/`detain` restraints that block conferral and movement.

**Status, one line.** The seasonal economy (MATTER: draw, yield, wear, term lapse) is **RUNS-IN-LOOP** (hunger→body
at control: inert); `move`, `issue`, `dispatch` and `release` execute in all three seeds; plain `transfer` executes at
seeds 0 and 2 (1 and 5), not seed 1 (37/0), and never through a seat; `oblige` (24/22) and `confer` (5/1) execute at
seed 1 only, `convene` (5/1) at seed 2 only; upkeep renewal, the shortfall→relief loop, CENSUS individuation, `requisition`,
`revoke`, `establish`, `work`, `restore`, `sabotage`, `found`, `build` and `migrate` are **TESTS-ONLY** (0 successes in
seeds 0–2); tax, ration, proclaim, arrest, pardon, craft, exchange, hire and
debt are **DESIGN-ONLY**. Grades follow the audit's rule (ERRATA G1): RUNS-IN-LOOP = a non-refusal outcome inside
`SeasonDriver.season` over `build_realm`; "at control" = runs but inert at shipped fixture values; TESTS-ONLY = wired,
with zero successes in the realm run; DESIGN-ONLY = no executing code. A refusal firing is not the verb executing.

**Your budget.** A season gives you `max(1, 5 + 1 per live hold − body bands fallen − 1 per travel leg)` *scene
actions* (`decision/budget.py:19-20, 57-61`; `budget_office_bonus=1`, `data/fixtures.py:526`). *Every* live `hold`
counts: a seat, a founded place, a held Record or Proposition — so `create_record`, `issue`, `petition`, `survey`,
`forge`, `utter` and the like raise next season's budget. The budget is a **cost** budget: a scene of one act costs 1, a
scene of 2–3 acts (`interactions_per_scene=3`) is *extended* and costs `extended_scene_cost=2` (`data/fixtures.py:488-489`),
and an extended chunk is cut to one act when only 1 is left (`decision/choose.py:643-657`). The driver releases at most
one scene per round over 5 rounds (`loop/driver.py:456`; `loop/deliberate.py:250-260`). So budget 5 buys 3+3+1 = 7 acts
(cost 2+2+1); budget 6 (one seat) buys 3+3+3 = 9; a travel leg takes a seat-holder back to 7. The ceiling is 5 scenes, 10
cost. Observed: about 7.6 acts per person-season (basis: `d.resolved` 1,132 acts / ~74 persons / 2 seasons, seed 0).

No act in this subsystem rolls dice. Every effect is a deterministic write behind a typed precondition; the only
chance is *which* act a person chooses (sampler at `choice_temperature=0.1`, `data/fixtures.py:286`).

## 0a How it plays

**As built.** Paths under `engine/season/`; run figures are `ctl/realm_seed{0,1,2}_2seasons.txt` ("attempted" = acts that reached the
fold, "ok" = a non-refusal event; ERRATA G2) and the round-3 re-runs at `51d7b05` listed in §8. Grades are ERRATA G1, per seed
(s0 · s1 · s2).

**Setup choices.** At world build the only choice is the seed: `build_realm(seed)` gives every one of the 37 settlements one harbour and
one seam at condition 1000 (`harness/populated.py:772-777`), a dwelling per hearth (`:793-797`) and a garrison per settlement
(`:815-818`), 32 seats (31 rows in `offices.yaml` plus the derived `off_npc_084`, `harness/populated.py:1241-1250`) and empty stores
everywhere (§1). The shipped controls are fixed: `body_step=0`, `oblige_term=4`, `default_upkeep=1` (`data/fixtures.py:594, 892, 905`).
The seed changes what the choosers form, not what is built (the 32 seats and their conferral bases are identical in seeds 0-2): seed 1
swears 22 obliges (24 attempted), seeds 0 and 2 none (§4). The season loop has no player interface of its own; a person at the callback
(`harness/play_surface.py:41-52`, `dispatching_chooser`, reached only by tests today) chooses which acts to submit and their payloads.
Any of the 47 resolvable verbs with any extra fields is folded; a non-resolvable one aborts the season (round-3 re-run). There is no
settlement, policy or faction to pick before play.

**The loop.** One tick is one season: CALENDAR, then MATTER, then five rounds of DELIBERATE, RESOLVE, ENCOUNTER, WITNESS, then CENSUS
(`loop/driver.py:447-457, 514`). MATTER is wholly automated (`loop/matter.py:165-709`): works stages ripen, terms lapse (`:296-303`),
claims decay (`:317-347`), cohorts draw grain and salt from the nearest store (`queries/world_q.py:905, 1020`), bodies would fall
(`:513-520`, inert at 0), Sites yield `int(base × condition / 1000)` (`:589-591`) and wear. Each person then spends a cost budget of
`5 + 1 per live hold − body bands − 1 per leg` (`decision/budget.py:57-61`): a lone act costs 1, a scene of 2-3 acts costs 2
(`data/fixtures.py:488-489`), so 5 buys 7 acts and a seat-holder's 6 buys 9 (round-2 C1). Nothing in this subsystem rolls dice (§0).

**The choice menu.** Cost is the scene cost above plus the matter named.

| verb | cost | effect | when a person picks it | grade (s0 · s1 · s2) |
|---|---|---|---|---|
| `oblige` | 1 | swears service to a seat for 4 seasons | from anywhere, to any seat he does not hold (§2.4) | RUNS-IN-LOOP at s1 only (24/22) |
| `transfer` | 1 + the amount | moves stores; through a seat to its obligees, renews terms | from a claim's referent; only cohort → own person rung executed (§4) | RUNS-IN-LOOP at s0, s2 (1, 5); renewal TESTS-ONLY |
| `requisition` | 1 | stock from a rung in purview into the seat's rung | through a seat granting `issue` | TESTS-ONLY (2/0, 5/0, 5/0) |
| `confer` | 1 | seats a person; refills a vacancy | through a seat granting `confer` | RUNS-IN-LOOP at s1 only (5/1, a self-conferral) |
| `revoke` | 1 | strips a seat; bans an appointee | through a seat on the rung directly above | TESTS-ONLY (6/0, –, 4/0) |
| `establish` | 1 | a new seat or remit | through a seat granting `confer` | TESTS-ONLY (–, 5/0, 4/0) |
| `release` | 1 | resigns a seat, quits service | on any edge of his own | RUNS-IN-LOOP (45/3, 44/5, 46/3) |
| `issue` | 1 | a writ for one executor; +1 hold | through a seat granting `issue` | RUNS-IN-LOOP (6/5, 12/5, 14/8) |
| `dispatch` | 1 | nothing but `order.given`, told to every ledger | through a seat granting `dispatch` | RUNS-IN-LOOP (18/6, 18/7, 10/10), writes nothing |
| `convene` | 1 | a dated sitting | through a seat granting `convene` | RUNS-IN-LOOP at s2 only (5/1) |
| `create_record` works → `found` / `build` | 1 + 1; grain 10 or timber 10 | a new hearth or community, or a Site at 0 | own; a computed `create_record` never mints a works | TESTS-ONLY (found 24/0, build 19/0 at s0) |
| `work` / `restore` / `sabotage` | 1 each | raise or lower a Site by 1/n of headroom | own, present; formed on non-Site referents | TESTS-ONLY (77/0, 23/0, 34/0 at s0) |
| `migrate` / `move` | 1 + a leg | residence and presence / presence only | own | migrate TESTS-ONLY (81/0); move RUNS-IN-LOOP (42/16) |

**First season, step by step (seed 0).** Tick 0 MATTER: every cohort wants grain 4 and salt 2 and finds no store, so nothing is drawn and
no shortfall is written; then each settlement yields grain 40, salt 30, ore 50, timber 10 and its harbour and seam wear to 990 (§3; over
two MATTERs the ctl file shows `yield.taken` 74 = 37 settlements × 2 and `stores.changed` 111). Five rounds follow: 1,132 acts reach the
fold over the two seasons (ctl seed 0, line 1) out of 1,407 formed (the story-bar run's act count, re-run at `51d7b05`); the rest are
refused before the fold. What executes in this subsystem is `move` 16 of 42, `issue` 5 of 6, `dispatch` 6 of 18, `release` 3 of 45 and
`transfer` 1 of 45; `work` 0 of 77, `restore` 0 of 23, `found` 0 of 24, `build` 0 of 19, `migrate` 0 of 81, `requisition` 0 of 2,
`revoke` 0 of 6 (ctl seed 0). Tick 1 MATTER: the Valorsplatz cohort eats 4 grain and 2 salt from its own larder and the harbour at 990
yields 39, not 40 (§3). A callback playing the Lord Treasurer can do what the chooser never does: three men swear (`oblige`), she
requisitions 2 grain from `set_s_001` into `terr_T1` and pays them at the court hearth; two terms run to tick 9, the third closes at
tick 5 (§3, re-run at `51d7b05`). A callback can also found: `create_record {kind: works, plan: hearth}` in one season, `found` in the
next, `rung.founded` (round-3 re-run). By the end of season 2, persons are 83 → 74 (nine `person.died`; every death is combat, ERRATA G9).

**What changes later.** Only time and deaths. Harbours and seams lose 10 condition a season and nothing repairs them in computed play, so
yield truncates a unit early and reaches 0 near tick 100 (§5d). At tick 5 the first act-opened terms mature: seed 1's live obliges fall
47 → 35 and none is ever renewed (§5c). Seats empty as holders die. The King (`p_npc_020`) is dead after the first season in all three
seeds; his seat and the Duke of Valorsmark's (his second seat), both null-conferral, are vacant at the end of season 2 in all three and
can never refill; by then 8, 7 and 10 seats have been vacated, and the only refill in the three seeds is seed 1's self-conferral (§5b).
With the Duke's seat gone no `revoke` can pass anywhere (§5c). Stores keep rising (0 → 9,250 by season 2, §5d). The legitimacy and
stability Queries PR #494 added (IN-23) change nothing here: each is one person's own windowed estimate (`queries/person_q.py:451, 480`),
read by the story-bar report and by no chooser or MATTER step (`hole_register.yaml` H-224).

**Failure and ending.** There is none. The loop has no fail state and nothing halts the run (ERRATA G17). The season now reports
`endings_reached` (`queries/world_q.py:1764`; `loop/driver.py:515-518`; PR #494), a read of the `rosters.yaml: endings` rows and never an
actor, and the realm as built reaches none (`rosters.yaml:2494-2522`; empty after each of seasons 1 and 2 in seeds 0-2, re-run at
`51d7b05`). MATTER kills nobody at shipped values (ERRATA G9); no place starves, rebels or empties for economic reasons. The losses that
exist are permanent but local: a dead holder's null seat, a banned appointee, a lapsed oblige.

**Consequential vs cosmetic choices.** Consequential: staying alive (a death closes every seat and service naming the person, overview
§5.1); `confer` into a vacancy, the only refill; `oblige`, whose term schedules its own end. Inert or cosmetic at shipped values: which
person holds a seat (no act's effect reads the holder, H-164), `dispatch` (writes nothing), `issue` (a held writ seeds its holder's own
operands, `decision/options.py:915-930`, but nobody must act on one and the executor holds it only after a `give`, 1 of 56 executed in
ctl), every food decision (surplus from tick 1), `transfer` into a person rung (it leaves the food supply, §4), and any reading of
legitimacy or stability.

**[PROPOSED]** (none of this runs; §7; ERRATA G16, G18). *Played mode:* D-2 (RULED yes) has RB-3 build IN-46 (a paused, played fight) and
IN-47 (character-sheet space), so one person's choices become the player's through the existing callback seam. *Remediation:* RB-2a's
REM-22 gives `work` and `restore` a Site referent; H-165 would mint the works inside `found`/`build`; RB-5 (REM-50/51/52, JQ-6) adds a
`hunger(w, S)` reading and `body_step = 10`, which binds only before the first yield at today's ratio (ERRATA G18). *Verbs:* `tax`,
`ration` and `proclaim` as one `edict` Record kind; `arrest`/`pardon`; `craft` with a recipes roster; `exchange` with a `price_of` Query;
`hire`; `borrow`/`lend`/`debt` (§7). With those, the menu above would gain a standing-rule verb, a wage and a price; precedent puts the
decisions there in Victoria 3, Tropico 6 and Patrician IV (`research/game_precedent_suite/tutorials/T01_realm.md` Vic3 §3,
`T11_policy_sims.md` Tropico 6 §3, `T10_npc_economy.md` Patrician IV §2.3).

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **Rung** | a node of the place ladder; the one class for every scale ("THE HOLON") | `kind` ∈ person < hearth < community < settlement < territory < province < duchy < realm; holds `stores` and `yield`; refuses any social aggregate as a field | `state/carriers.py:1040`; `rosters.yaml:256` |
| **the ladder** | rungs joined child→parent by `contain` Tenures that must ascend | realm 1, duchy 3, territory 17, settlement 37, community 60, hearth 211 in `build_realm(0)`; **no province rung** is built; a territory hangs off its duchy, except the Church's T9 and unheld territories, which hang off the realm (`harness/populated.py:734-738`); Schoenland's T16 is built outside the tree | `state/containment.py:40` (`descendants`), `:95` (`ancestry`) |
| **hearth** | the lowest place rung: a building (court, market, wharf…) | 211 in the realm; each has one `dwelling` Site | built by `harness/populated.py` from `venues.yaml` |
| **Site** | a built fabric on a rung that yields, houses or fortifies | `kind` ∈ harbour, seam, dwelling, garrison (the roster also lists `body`, which "IS NOT A SITE": it is the person's body band row, `rosters.yaml:1386`); `condition` 0..1000 | `state/carriers.py:737`; `rosters.yaml:1376` |
| **condition** | a Site's state on `condition_scale` | 1000 = full; every realm Site starts at 1000 | `data/fixtures.py:217` |
| **yield** | what a Site mints each season | harbour {grain 40, salt 30}; seam {ore 50, timber 10}; nothing else yields; scaled by condition/1000 × `season_factor` (1.0) | `rosters.yaml:2491`; `loop/matter.py:589-591` |
| **wear** | condition lost per season | harbour 10, seam 10, body 10, dwelling 0, garrison 0 | `rosters.yaml:1422`; `loop/matter.py:663` |
| **band floor** | a named use-threshold on condition; crossing it downward emits `condition.band_crossed` | harbour {bulk_shipping 800, fishing 100}; seam {deep_mining 700, surface_gleaning 50} | `rosters.yaml:2520` |
| **stores** | integer stock by matter kind held on a rung (the larder, and a seat's treasury) | empty everywhere at build | `Rung.stores`, `state/carriers.py:1040` |
| **matter kind** | a registered good | grain, salt, timber, ore, coin; `coin` is registered but nothing produces or reads it | `rosters.yaml:1409` |
| **cohort** | a person of `weight > 1`: "the people of" a settlement | 37, one per settlement, weight 2 each; the only eaters (ED-IN-0255) | `state/carriers.py:655`; `cohorts.yaml` |
| **subsistence weight** | food wanted per unit of weight per season | grain 2, salt 1 → a weight-2 cohort wants 4 grain + 2 salt | `rosters.yaml:1540`; `queries/world_q.py:1017` |
| **nearest store** | the larder a cohort eats from: first rung up its ladder holding the kind | walk stops at the first rung with stock; the remainder is not walked further | `queries/world_q.py:902` |
| **shortfall** | the unfed part of a draw, carried as an `Observation(rung, "shortfall:<kind>", units)` on the drained larder's write | fires only when a larder drains with a mouth unfed | `loop/matter.py:469-474` |
| **body** | a person's condition; would fall with hunger | `body_step=0` shipped: no body falls | `data/fixtures.py:594` |
| **Office / seat** | a post anchored to a rung, with powers | 32 in the realm: 31 authored in `offices.yaml` + `off_npc_084` (guild leader), derived with no row, rungless, so it reaches nothing (`harness/populated.py:1240-1244`); loop-built seats take ids `off_npc_NNN` (the King's seat is `off_npc_020`), while six minted rows keep their row ids (`off_duke_valorsmark`, `off_lord_steward`, `off_cardinal_fortitude`, `off_cardinal_temperance`, `off_senior_inquisitor`, `off_restoration_leader`; `offices.yaml:120-127`); fields `post, rung, remit_acts, conferral, revocation, upkeep, body, faction` | `state/carriers.py:899`; `offices.yaml` |
| **remit act** | a power a seat grants its holder | six values: issue, determine, confer, revoke, dispatch, convene. **The tree contradicts itself**: the roster is declared `open: true` (`rosters.yaml:316`; H-52 turns on it) while its own `source:` (`:315`) and `verb_table.yaml:257, 801, 1478` call it CLOSED. Loop-built seats are seated with `remit_default` (a "NOT CANON" test fixture) and keep `dispatch` through `remit_unruled` (`offices.yaml:100-119, 141`) | `rosters.yaml:314-322` |
| **hold** | a Tenure Person→Office (or Rung, Record, Proposition): you sit in the seat / own the place | one live hold per object; its payload snapshots the seat's remit (`granted_acts`) | `state/carriers.py:77` |
| **purview** | where a seat's writ runs: its own rung and every rung below, plus the ground of seats whose holders are sworn to it (one edge deep, IN-40) | asked of the seat exercised (`Act.via`), never of the actor | `state/gate.py:353` |
| **conferral basis** | how a seat is filled | appointed, elected, annex, or none; realm authored: appointed 17 / elected 8 / none 6; the derived guild-leader seat `off_npc_084` also has none (its `conferral` is read from a row that does not exist, `harness/populated.py:1241-1250`), so 7 of the 32 built seats. A **none** seat (King, Duke of Valorsmark, Duchess of Hafenmark, Widow Regent (post "Queen"), Heir (post "Prince"), Princess, guild leader) can never be conferred, so once vacant it stays empty: `succeed` has no effect | `rosters.yaml:2234`; `offices.yaml:188-266`; `loop/predicates.py:126-127` |
| **revocation basis** | who may strip a seat | `rung_above_same_faction`, `rung_above_in_holdings`, or none ("strippable by nobody") | `rosters.yaml:2254`; `state/gate.py:568` |
| **ban** | a restraint Tenure: banned persons cannot be seated or sworn | opened permanently on an *appointed* holder who is revoked | `state/gate.py:599`; `queries/world_q.py:1242` |
| **oblige** | a Tenure Person→Office: you serve this seat | an act-opened edge carries a `Term`, `oblige_term=4` seasons; the two authored at world-gen (NPC-070 → the King's seat, NPC-041 → `off_restoration_leader`) carry **no term** and never lapse | `loop/effects_governance.py:377`; `data/fixtures.py:882`; `harness/populated.py:1317-1339` |
| **chronicle** | a witness channel that is an **event-kind filter**: any Event whose kind some `binding_decision` row emits is deposited for **everyone alive**, as `told_by` hearsay | so `tenure.opened/closed`, `order.given`, `date.scheduled`, `dispensation.issued`… are public, whoever produced them — including MATTER's `tenure.closed` lapses and `pursuit.moved` from `determine` | `epistemic.py:652-654, 685-686` |
| **Term** | `(matures_at, declared_by)` on a Tenure; MATTER closes the edge when `matures_at <= tick` | `declared_by` = the act that last wound it | `state/carriers.py:43`; `loop/matter.py:296-303` |
| **establishment** | the persons with a live `oblige` to a seat | a Query, stored nowhere | `queries/world_q.py:1739` |
| **upkeep** | grain (any kind) per obligee that one payment must cover to renew his term | `Office.upkeep`, else `default_upkeep=1` | `queries/world_q.py:1768`; `data/fixtures.py:895` |
| **treasury** | the `stores` of the seat's own rung (no Treasury class) | a territory seat's treasury is the territory rung, which yields nothing | `loop/effects_governance.py:426-464` |
| **works** | a `Record` of kind `works` with `{plan, at}`: a plan to found a rung kind or build a Site kind at a rung | one live works per (plan, at); its stages ripen into a ceiling | `state/carriers.py:751`; `queries/world_q.py:353` |
| **ceiling** | how high `work`/`restore` may raise a Site | full scale (1000) if no works names it; else scale × matured stages / declared stages | `queries/world_q.py:382` |
| **share** | the commons: one act moves `1/n` of the headroom, n = persons present at the Site's rung | `(1, max(1, n))` | `queries/world_q.py:422` |
| **works cost** | what founding or building takes from the paying rung | hearth / community {grain 10}; harbour, seam, dwelling, garrison {timber 10}; none for settlement or above | `rosters.yaml:1501` |
| **population** | sum of `weight` over live `reside` edges in a rung's subtree | e.g. `set_s_001` = 12 (one cohort of 2 + 10 cast) | `queries/world_q.py:1262` |
| **capacity** | how many may live under a rung: dwelling Sites in the subtree, floor 1 | `set_s_001` = 9; gates newcomers only | `queries/world_q.py:1310`; `rosters.yaml:1472` |
| **governors** | persons holding a seat whose purview reaches a rung; they receive shortfall claims | | `queries/world_q.py:835` |
| **MATTER** | the actorless barrier that runs once per season before any scene | order: works stages, term lapses, claim decay, draw, body fall, yield, travel clear, wear | `loop/matter.py:165-709`; `loop/driver.py:448` |

## 2 How it works

### 2.1 Where you are: the ladder, presence and residence

A "settlement" is nothing more than a Rung of kind `settlement`; it has no settlement-specific state. Its larder is its
`stores`, its buildings are hearth rungs beneath it (each with one `dwelling` Site), and its harbour, seam and garrison
are Sites on the settlement rung itself (`set_s_001` holds `s_s_001_harbour`, `s_s_001_seam`, `s_s_001_garrison`).
You relate to places by two edges, kept apart on purpose:

- **presence** — a live `contain` edge to where you stand (`home_of`, `queries/world_q.py`). `move` changes it.
  Presence decides which larder a cohort eats from, who is "present at" a Site, and where upkeep lands.
- **residence** — a live `reside` edge to where you live (`residence_of`, `queries/world_q.py:1208`). Only `migrate`
  changes it. Residence decides `population` and therefore the capacity test.

Everything aggregate (population, capacity, purview, establishment, governors) is a Query computed on demand and stored
nowhere; a Rung refuses such attributes at `__setattr__` (`state/carriers.py:1040`).

### 2.2 The season's economy runs before you act (MATTER)

The driver runs `calendar → matter → 5 × (deliberate, resolve, encounter, witness) → census → tick+1`
(`loop/driver.py:447-448, 514`). MATTER is actorless; nobody chooses it. In order (`loop/matter.py`):

1. **Works stages** due this tick mature, if the works still has a live holder (`:219-263`).
2. **Terms lapse.** Every live Tenure with `term.matures_at <= tick` closes (`until = tick`), citing the act that last
   wound it (`:296-303`). This is how unpaid service ends: nobody has to act.
3. **The draw.** For each cohort (individuals do not eat), for each kind: `want = subsistence_weight[k] × weight`;
   `src = nearest_store(...)` walking up from where the cohort is present; `take = min(want, held)`
   (`queries/world_q.py:1017-1094`). If `take < want` and a larder was drained, the larder's `stores.changed` write
   carries `Observation(src, "shortfall:<kind>", demanded − delivered)` (`loop/matter.py:469-474`).
4. **Body fall.** `lost = body_step × units short`; shipped `body_step = 0`, so nothing happens (`:513-534`).
5. **Per rung: debit the draw, then credit yield.** For each Site on the rung,
   `produced[k] += int(base[k] × max(0, condition) / 1000 × season_factor)` (`:589-591`). `int()` truncates, so a
   harbour at 990 yields 39 grain and 29 salt, not 39.6 and 29.7.
6. **Travel legs clear; Sites wear** by their kind's rate, floored at 0; each downward crossing of a band floor emits
   `condition.band_crossed` (`:643-691`).

Two consequences you must plan around. First, the draw comes *before* the yield in the same barrier, so at the first
MATTER (tick 0) every larder is empty when the cohorts eat. Second, because no larder actually *drains* at tick 0 (there
was nothing to take), no shortfall Observation is written; `matter.py:463-468` records that no shipped world drains a larder with a
mouth unfed.

### 2.3 Seats: holding, remit, purview, acting "through" a seat

To exercise a remit act you need a live `hold` on an Office whose snapshot (`granted_acts`) contains that act. A verb row's
`eligibility` is a list of alternatives; the first that admits decides (`decision/options.py:_admitted_through`). When the
admitting alternative is `remit:<act>`, the act carries `Act.via = <seat>` (`decision/options.py:528`, `seat_of`), and
**every authority test is asked of that seat, not of you**:

- **Purview** (`state/gate.py:353`): the seat's own rung and all its descendants; also, since IN-40, the ground of any
  seat whose holder owes this seat a live `oblige` (one edge deep). Never upward.
- **May fill** (`state/gate.py:675`, for `confer`): you sit in `via`; `via` is not the seat being filled; the target seat
  has a conferral basis; `via`'s purview reaches the target's rung. The basis value is not otherwise read: appointed,
  elected and annex all pass. Conferring an *occupied* seat additionally needs `may_revoke` over it and a holder with no
  live `commit` (`loop/predicates.py:141-160`).
- **May revoke** (`state/gate.py:660`): you sit in `via`; the target declares a revocation basis; and that basis's rule
  admits `via`. `rung_above_same_faction` = `via` sits on the *parent* rung of the target's rung and is of the same
  faction (`state/gate.py:452`); `rung_above_in_holdings` = `via` sits on the parent rung **and you hold the
  target seat's own rung** (`in_holdings(w, actor, off.rung)`, `:547-565`), with no faction clause. A seat with no
  basis, a rungless seat, or a top-rung seat is strippable by nobody.
- **Revocation disposal** (`state/gate.py:599`): revoking an *appointed* holder opens a permanent `ban` on him (no
  term; only death ends it); elected, annex and none open nothing.
- **May renew** (`state/gate.py:698`, for upkeep): `via` is the very seat being paid for, and you sit in it.

The treasury of a seat is the `stores` of its own rung. In the built realm most seats sit on territory or duchy rungs,
which have no Sites and therefore never yield: a territory seat's treasury starts empty and stays empty until someone
moves stock into it.

### 2.4 Service and upkeep: oblige, term, renewal, lapse

`oblige` is the joiner's own act: he opens `oblige` Person→Office with `Term(tick + 4, <the oblige act>)`
(`loop/effects_governance.py:377-422`; `effects_shared._new_oblige_term`). He must not hold that seat, must have no live
`oblige` to it already, and must not be banned (`loop/predicates.py:338-399`). He may swear from anywhere.

The term runs out at MATTER unless the seat pays. A `transfer` is an upkeep payment **only when all four clauses hold**
(`loop/effects_economy.py:287-356`): (1) it is exercised through the seat by its seated holder (`may_renew`); (2) it is
paid *from the seat's own rung*; (3) matter moves (another rung, amount > 0); (4) it is paid *to the rung where the
obligees are present* (`home_of`). Then it renews, of that seat's termed obligees present at the receiving rung,
`covered = min(due, amount // upkeep_of(seat))` of them (all of them if upkeep is 0), **soonest-maturing first, ties by
edge id**, each by `oblige_term` seasons *from where its old term stood*, and at most one term per man per payment. The
remainder of the payment is simply transferred. A payment that fails any clause is an ordinary transfer that renews
nobody: paying from your own hearth is a gift, and moving the treasury to your own hearth is (in effect) embezzlement —
the terms you did not pay lapse at MATTER, with no special code for it (`:320-324`).

### 2.5 Works: the only road to new places and new Sites

Founding and building are two-step. First a `create_record` act declaring `kind: works` and
`subject_matter: {plan, at}` mints a works Record held by its maker; a second live works on the same `(plan, at)` is
refused (`loop/effects_information.py:73-90`). Then:

- `found` (plan is a rung kind) mints `Rung("<plan>:<works id>")`, its `contain` edge to `at` (must ascend), and the
  founder's `hold` on it, and moves `works_cost[plan]` from the paying rung (the works' own rung) into the new rung
  (`loop/effects_founding.py:91-181`). Settlement and above have no cost row, so they cannot be founded this way.
- `build` (plan is a Site kind) mints `Site(..., condition=0)` at `at` and consumes the cost one-sided (`:184-242`). A
  new Site yields nothing until raised.
- `work` and `restore` raise a Site by `_rise = (ceiling − condition) × 1 // n` (`loop/effects_economy.py:109-138`).
  With one person present the whole headroom is filled in one act; with n present each act moves 1/n.
  `ceiling` is 1000 where no works names the Site, else `1000 × matured stages // declared stages`
  (`queries/world_q.py:382-419`): the pace of a works is its ripened stages, not a rate. `work` stages a rise only when a
  live works names the Site's kind at its rung; with none, it stages 0 and is refused (`work.unavailable`). For a `dwelling` or a
  `garrison` no works helps: their `band_floors` cells are empty on purpose (`rosters.yaml:2631-2632`), and the `floor` read raises a
  typed `Unspecified` before any rise is staged (`queries/world_q.py:2783-2799`), so the act is refused (`work.unavailable` on a dwelling at condition 0
  with a works naming it, and at 1000; round-3 re-run). So `work` can never run on 248 of the realm's 322 Sites
  (211 dwellings + 37 garrisons). `restore` needs no works and repairs wear up to full scale.
- `sabotage` stages `−condition × 1 // n` (`:141-177`): one saboteur alone takes a Site to 0 in one act. It never
  removes the Site.
- **In the realm nobody is alone at a producing Site.** Harbour, seam and garrison sit on the settlement rung, where
  that settlement's cohort is always present (`harness/populated.py:439-442`), and `share` counts *persons* present at
  the rung (`queries/world_q.py:422-436, 1181-1186`; the cohort counts as one, whatever its weight). So any individual's
  `restore`, `work` or `sabotage` there has n ≥ 2: at most half the headroom (or half the condition) per act.

There is no degree term in any of these: the rows are uncontested, so `f(degree)` is the identity (H-164).

### 2.6 Capacity and migration

`capacity(rung) = max(1, number of dwelling Sites in the subtree)` (`queries/world_q.py:1310-1334`). `migrate` refuses a
**newcomer** (no residence, or a residence outside the destination's subtree) when
`population(dest) + your weight > capacity(dest)`; the test is at the destination only (`loop/effects_migration.py:122-217`).
Population may already exceed capacity (at build `set_s_001` has population 12 against capacity 9; after two seasons of
seed 0, 10 against 9, and `set_s_036` 8 against 6), because only newcomers are tested. A hearth has exactly one dwelling, so its capacity is 1. Building a dwelling
raises capacity at its rung and every ancestor.

### 2.7 The governor feedback: shortfall → claim → transfer

When a larder drains with a mouth unfed (§2.2 step 3), WITNESS deposits the shortfall Observation, as a claim, into those
present and into every holder whose seat's purview reaches the drained rung (`governors_of`, `queries/world_q.py:835`;
`SEAT_CHANNEL`). A governor's `claim_landed` question can then form a `transfer`: `kind` and `amount` are read off the
claim (`decision/options.py:859`), `to` is the drained rung (the claim's referent), and `from` is where the giver stands
or, through a seat, the seat's rung. Built, tested (`tests/test_in22_shortfall_reach.py`), and silent in the realm,
because no realm larder ever drains (§3).

### 2.8 Refusals are events

A refused act changes nothing and emits its row's refusal kind (`confer.refused`, `work.unavailable`,
`requisition.unauthorized`…). Typed preconditions are three-valued and "false dominates unknown": an unevaluable
precondition refuses. Nothing in this subsystem raises an error into the season for an ordinary failure.

## 3 A worked example

**Scenario.** Valorsplatz (`set_s_001`, canon S-001, under `terr_T1` < `duchy_valorsmark` < `r_valoria`). Its
harbour `s_s_001_harbour` and seam `s_s_001_seam` start at condition 1000; its people are one cohort,
`cohort_set_s_001` ("the people of Valorsplatz", weight 2), present and resident at the settlement rung. All stores
are empty at build. Then a seat-holder recruits and pays three men. Run read-only with `python3 -I` against
`build_realm(0)`: MATTER driven alone (no chooser acts), and the seat acts hand-built and passed through the real fold
(`SeasonDriver.resolve`), the way `tests/test_term_upkeep.py` does it. Script and output: §9.

**MATTER at tick 0 (the first MATTER).**

| step | arithmetic | result written |
|---|---|---|
| draw | cohort wants grain 2×2 = 4, salt 1×2 = 2; `nearest_store` finds no rung holding either | record `grain (4, 0, None)`, `salt (2, 0, None)`: 6 units short; no larder drained, so **no shortfall Observation**; `body_step = 0`, body stays 1000 |
| yield | harbour `int(40×1000/1000×1.0)` = 40 grain, `int(30×1.0)` = 30 salt; seam 50 ore, 10 timber | `set_s_001.stores = {grain 40, salt 30, ore 50, timber 10}`; `yield.taken`, `stores.changed` (37 of each realm-wide) |
| wear | harbour 1000 − 10, seam 1000 − 10, garrison and dwellings − 0 | harbour 990, seam 990; 322 `condition.worn` events |

**MATTER at tick 1.**

| step | arithmetic | result |
|---|---|---|
| draw | nearest store for both kinds is `set_s_001` itself; take = min(4, 40) and min(2, 30) | grain 36, salt 28; record `grain (4, 4, set_s_001)` |
| yield at 990 | `int(40×0.99)` = int(39.6) = **39**; `int(29.7)` = **29**; `int(49.5)` = 49; `int(9.9)` = 9 | stores `{grain 75, salt 57, ore 99, timber 19}` |
| wear | − 10 each | harbour 980, seam 980 |

The truncation matters: from the first point of wear the harbour gives one grain and one salt less than the proportion
would, every season. Run on to tick 5 (with only the 2-grain requisition below taken out) and the larder reads grain
108 → 142 → 176 → 210 (net +34 or +35 a season against 4 eaten; yield 39, 38, 38, 38 at conditions 980–950) and the
harbour 940. The one mouth here never goes short again.

**The seat play (tick 1, after MATTER).** Annalie Reichard (`p_npc_037`) holds the Lord Treasurer's seat
(`off_npc_037`: rung `terr_T1`, remit `[dispatch, issue]`, appointed, revocable `rung_above_same_faction`, Crown,
`upkeep` unset → `default_upkeep = 1`).

1. Three persons present at the court hearth `b_s_001_court` — Inge Baralta, Hedda Kronvald, Nessa Grindvold — each
   act `oblige {subject: off_npc_037}`. Each emits `duty.taken`; each edge gets `Term(matures_at = 1 + 4 = 5,
   declared_by = <their own oblige act>)`. `establishment_of(off_npc_037)` = the three.
2. Her treasury (`terr_T1.stores`) is empty: a territory rung has no Sites. She acts
   `requisition {subject: set_s_001, kind: grain, amount: 2}` *through* the seat. Purview: `set_s_001` is a descendant of
   `terr_T1`; stores 75 ≥ 2. Result `requisition.taken`: `set_s_001` grain 75 → 73, `terr_T1` grain 0 → 2 (conserved).
3. She pays: `transfer {from: terr_T1, to: b_s_001_court, kind: grain, amount: 2}` through the seat. All four clauses
   hold (via = the seat she sits in; from = its rung; 2 > 0 to another rung; the obligees are present at the court).
   `due` = the three termed edges at the court, sorted by `(matures_at 5, edge id)`; `covered = min(3, 2 // 1) = 2`.
   Result: `transfer.made` + `term.renewed`; Baralta's and Kronvald's terms → `matures_at = 5 + 4 = 9`,
   `declared_by = pay1`; Grindvold's stays at 5. `terr_T1` grain 0; the court hearth now holds grain 2 (which nobody
   eats: individuals do not draw).
4. Ticks 2–4: nothing happens to the edges. **Tick 5 MATTER:** Grindvold's edge matures and closes (`tenure.closed`,
   `until = 5`, cause = her own `oblige` act). `establishment_of` = Baralta, Kronvald.

**What this shows.** Food was never the constraint; the bind was getting stock into a treasury that produces nothing,
and getting payment to *where the men stand*. One grain per man per four seasons keeps an establishment; the
settlement's surplus could pay for dozens.

## 4 What you can do

Acts are paid from the cost budget in §0 (a lone act costs 1; an extended scene of 2–3 acts costs 2). None rolls; "outcome" is either the write or the refusal. The last column is the
control run (`ctl/realm_seed{0,1,2}_2seasons.txt`: `build_realm(seed)`, 2 seasons, chooser-formed acts; "ok" = the act
caused at least one non-refusal event; "attempted" = acts that reached the fold, so acts refused at admission are not
counted); "–" = none reached the fold in that seed. Columns are attempted/ok. Rows from `verb_table.yaml` (line in
brackets); effects in `loop/effects_*.py`.

| verb | who may (eligibility) | prerequisites | writes / emits on success | refusal | realm att/ok s0 · s1 · s2 |
|---|---|---|---|---|---|
| **confer** [223] | a seat granting `confer` (`via`) | target is an Office with a conferral basis; `via`'s purview reaches it; `via` ≠ target; conferee living and not banned; if the seat is held: the holder is not the conferee, has no live `commit`, and `via` may revoke him (or he is you) | opens conferee's `hold` (optional declared `term ≥ 1`), closes the prior hold with no ban; `tenure.opened`/`.closed` | `confer.refused` | – · 5/1 · – |
| **establish** [387] | a seat granting `confer` | the establishing seat's conferral basis; a rung to put it at | a new Office, or a new `remit_acts` on an existing one (live holds re-stamped); `office.established` / `remit.changed` | `establish.refused` | – · 5/0 · 4/0 |
| **revoke** [1004] | a seat granting `revoke` | target Office declares a revocation basis whose rule admits `via` (§2.3); a live hold exists | closes the holds; an *appointed* ex-holder gets a permanent `ban`; `tenure.closed` | `revoke.refused` | 6/0 · – · 4/0 |
| **release** [965] | yourself (`own`) | a live edge of yours of kind tie, hold, succeed, commit, knot or oblige toward the subject | `Tenure.until` — resign a seat, abandon a place, quit service | `release.refused` | 45/3 · 44/5 · 46/3 |
| **convene** [243] | a seat granting `convene` | subject ranks above a person, or none | a dated sitting `{venue, holder = via, due_at}`; `date.scheduled` (what the sitting decides is not here) | `convene.refused` | 1/0 · – · 5/1 |
| **oblige** [878] | yourself | subject is a seat; you do not hold it; no live oblige to it already; not banned | `oblige` to the seat, `Term(tick + 4)`; `duty.taken` | `duty.refused` | – · 24/22 · – |
| **requisition** [766] | a seat granting `issue` | subject rung within `via`'s purview; `stores(subject, kind) ≥ amount` | `amount` moves subject rung → seat's rung; `requisition.taken` | `.unauthorized` / `.refused` | 2/0 · 5/0 · 5/0 |
| **transfer** [1475] | a seat granting `issue`, or yourself, or a holder of the store | `stores(from, kind) ≥ amount`; both sides rungs; not a self-transfer; amount > 0 | `amount` moves from → to (conserved); through a seat, from its rung, to obligees' place: renews terms (§2.4); `transfer.made`, `term.renewed` | `transfer.refused` | 45/1 · 37/0 · 43/5 |
| **work** [1506] | yourself (`own`; `presence:<site>` is only a second alternative) | typed precondition is `condition ≥ floor` and nothing else (floor = the least demanding use: harbour 100, seam 50; dwelling and garrison have no floor, so the read refuses there, §2.5) — **no presence clause**; the rise is staged only if a live works names this Site's kind at its rung, else `work.unavailable` | stages `+_rise` on condition; `site.worked` | `work.unavailable` | 77/0 · 70/0 · 63/0 |
| **restore** [982] | yourself, present at the Site | the Site exists; you are present at it; it has headroom below its ceiling (a Site at 1000 refuses, `restore.refused`; a Site below its ceiling rises, `site.restored`; round-3 re-run) | stages `+_rise` up to the ceiling; `site.restored` | `restore.refused` | 23/0 · 31/0 · 30/0 |
| **sabotage** [1019] | yourself, present at the Site | the Site exists; you are present | stages `−condition // n`; `site.damaged` | `sabotage.refused` | 34/0 · 22/0 · 33/0 |
| **found** [487] | yourself | subject is a works you hold, planning a rung kind that ascends to `at`; the works' rung covers `works_cost` | new Rung + `contain` + your `hold` on it; cost moves payer → new rung; `rung.founded` | `found.refused` | 24/0 · 27/0 · 23/0 |
| **build** [510] | yourself | subject is a works you hold, planning a Site kind; cost covered | new Site at condition 0; cost consumed; `site.built` | `build.refused` | 19/0 · 17/0 · 21/0 |
| **migrate** [839] | yourself | not detained; a contain path to `to`; as a newcomer, room (§2.6) | presence and residence both move; `residence.changed` | `migrate.refused`, `travel.blocked`; every computed call is refused at the capacity test on an occupied hearth (§5c) | 81/0 · 143/0 · 143/0 |
| **move** [863] | yourself | not detained; a contain path | presence only; a travel leg cleared at next MATTER; `travel.moved` | `travel.blocked` | 42/16 · 35/17 · 40/12 |
| **dispatch** [372] | a seat granting `dispatch` | the named person exists | **nothing** (`writes: []`); `order.given`. Naming an absent id emits `person.demanded`, which makes CENSUS individuate a person — TESTS-ONLY: `person.individuated` is 0 in all three seeds | `dispatch.refused` | 18/6 · 18/7 · 10/10 |
| **comply** [183] | yourself (`own`); formed only on a writ you hold and your own ledger names (`referent_class: Record`, H-203) | typed: the subject is a `dispensation`, and a claim of its terms is in your own ledger | **nothing** (`writes: []`); `compliance.given`. The act the writ asks for is your own separate act | `compliance.impossible` | – · – · – |
| **issue** [561] | a seat granting `issue` | executor is a Person within purview; terms from your own ledger | a `dispensation` Record (a writ) you hold; `dispensation.issued` | `issue.unauthorized` / `.refused` | 6/5 · 12/5 · 14/8 |

Also on the table but inert here: `exchange` [416] (row declared, no effect; not in `resolvable_verbs()`, `loop/driver.py:101`, so a
callback that submits it raises `Unspecified` and aborts the season rather than being refused; round-3 re-run), `succeed` [1096] (no effect),
`evade / defy` [401] (not resolvable: `requires_typed: none` and no predicate, `verb_table.yaml:403-408`; it would
emit `compliance.withheld` only), `seize` [1042] (FA/MB: closes a holder's hold on an occupied settlement or Record).
`create_record` (FI) is the works producer; a computed `create_record` carries no payload and always mints `text`
(`loop/effects_information.py:81-83`).

**Why the zeros, read from the refusals** (seed 0, 2 seasons, my probe; §9): the chooser names the wrong *kind* of
thing. `restore`, `sabotage`, `work`, `found` and `build` were formed on settlements, hearths, persons and Records, never
on a Site or a works (e.g. `work` 77: settlement 31, person 21, hearth 7…); `migrate` 81 times, always to a hearth
(capacity 1, already occupied); `revoke` on persons and a Record, never an Office; `requisition` from a hearth (empty —
stock sits on the settlement rung) or outside the seat's purview. A computed `transfer` gives 1 grain from where the
giver stands (an empty hearth) or from its seat's rung (an empty territory) to the question's referent, usually a person
(every person is also a `person` rung): refused at `stores(from) ≥ amount`. The executions in seeds 0 and 2 (1 and 5)
are all a cohort moving 1 grain from its own settlement's larder into its own person rung, which lies *below* the
larder walk, so that grain leaves the food supply. No seed formed a seat-paid upkeep transfer (0 `term.renewed`).

## 5 Pursuing goals here

### 5a The goals and how the code holds them

| goal | what "done" is in state | Query that reads it |
|---|---|---|
| feed a place | its cohort's draw is met (`take = want`) every season | `subsistence_draw`, `demanded`/`delivered` (`world_q.py:1017-1178`) |
| grow a place | more Sites (yield), more dwellings (capacity), a founded hearth/community beneath it | `capacity`, `descendants` |
| pay your men | your seat's `oblige` edges carry terms in the future | `establishment_of`, `upkeep_of` |
| keep your men | the same edges still live after MATTER | `establishment_of` |
| remove a rival from a seat | his `hold` closed (and, if appointed, a `ban` on him) | `hold_force`, `restrained` |
| fill a seat with your man | his live `hold` on it | `hold_force` |
| fund a founding | the works' rung holds `works_cost` when you act | `stores` |

No goal here is stored as a goal. A person's pursuits come from his value axes and commitments (other tutorials); this
subsystem supplies the state those pursuits are about. Cohorts have no pursuit vector at all (ED-IN-0296 (2)).

### 5b The plays, step by step

**Feed a place.** Nothing to do at today's numbers: a settlement's own harbour feeds its own cohort from the tick-1
MATTER on (§3). If a larder does drain (only in `harness/scarce.py` today), sit in a seat whose purview reaches it; the shortfall
claim lands on you; your `claim_landed` question forms `transfer {to: drained rung, kind, amount from the claim}` out of
your seat's rung — which must already hold stock, so step 1 is to `requisition` from a surplus rung in purview.

**Pay a man.** (1) He swears: `oblige` to your seat (his act, not yours). (2) You hold a seat granting `issue` — the
*same* seat he swore to. (3) Its rung's stores hold ≥ 1 unit per man (requisition first if the treasury is a territory).
(4) `transfer` through that seat, from its rung, to the rung where he stands, amount ≥ men × upkeep. Repeat before his
term matures; paying early is not wasted (the new term runs on from the old one).

**Keep men.** The same, every four seasons. Pay where they *stand*, not where they live (`home_of`, H-174 unruled).

**Remove a rival.** Sit in a seat granting `revoke` on the rung *directly above* his seat's rung, of his faction
(`rung_above_same_faction`), or on that parent rung while you hold *his seat's own rung* as a holding, any faction
(`rung_above_in_holdings`); act `revoke` naming the office. If his seat was appointed, he is banned for life: he cannot be conferred or sworn again. A seat with no
revocation basis (the King's, `off_npc_020`) cannot be taken this way at all. In the built realm only the Duke of Valorsmark's seat
qualifies (§5c). **The other route is `confer`:** a
*vacant* seat needs only purview; displacing a holder needs the same revocation authority *and* a holder with no live
`commit` (`loop/predicates.py:141-160`), and it closes his hold without a ban. Seed 1's one executed `confer` was the
Confessor (`off_npc_021`, remit includes `confer`) seating himself on the Senior Inquisitor's seat beside him at `terr_T9`.

**Secure a succession.** Only for seats with a conferral basis. The seven null-conferral seats (six authored `conferral: null`,
plus the rowless guild-leader seat `off_npc_084`) — the throne (`off_npc_020`), the Duke of Valorsmark, the Duchess of Hafenmark,
the Widow Regent, the Heir, the Princess and the guild leader — refuse every `confer` (`loop/predicates.py:126-127`;
`offices.yaml:188-266`; `harness/populated.py:1241-1250`), and `succeed` has no effect, so if the holder
dies or releases the seat it stays empty for the rest of the run. Keeping the holder alive is the only play. Measured (seeds 0-2,
2 seasons, round-3 re-run at `51d7b05`): null seats are 3 of 8, 5 of 7 and 6 of 10 vacated seats; the King (`p_npc_020`) dies in the
first season in all three seeds, and his seat and the Duke of Valorsmark's are vacant at the end of season 2 in all three.

**Fund a founding.** (1) `create_record` with `kind: works`, `subject_matter: {plan: hearth, at: <settlement>}`,
`rung: <the paying rung>`. (2) Hold the works. (3) The paying rung holds grain 10 (timber 10 for a Site). (4) `found`
(or `build`). (5) For a Site: stand at it and `restore`, or `work` while a works names it, to raise it from 0.

### 5c Costs, risks, counter-play, blocks in the realm run

| play | what blocks it today (seeds 0–2, 2 seasons; ctl/ files) |
|---|---|
| work / restore / sabotage | the chooser forms them on non-Site referents (REM-22's `referent_class: Site` is unbuilt): work 77/0, 70/0, 63/0; restore 23/0, 31/0, 30/0; sabotage 34/0, 22/0, 33/0 |
| found / build | no computed act ever creates a works (computed `create_record` mints `text`; H-165): found 24/0, 27/0, 23/0; build 19/0, 17/0, 21/0. A hand-built `create_record {kind: works}`, then `found` or `build` in the next season, does run inside a real season (`rung.founded`, `site.built`; round-3 re-run), so the block is formation, not the effect |
| pay / keep men | `oblige` forms in seed 1 only (24 attempts, 22 sworn), and there everyone swore to `off_senior_inquisitor`, whose remit is `[determine]` alone: no `issue`, so its holder can never pay through it. Over 6 seasons of seed 1: 0 `term.renewed`; live obliges 47 → 35 at the tick-5 MATTER as the first terms lapsed |
| requisition | computed acts name a hearth (stock is on the settlement) or a rung outside purview: 2/0, 5/0, 5/0 |
| remove a rival | `revoke` is formed on persons and Records, never an Office (H-203): 6/0, –, 4/0. Even with an `office` payload, only six (seat, target) pairs can ever revoke in the seeded world, all through `off_duke_valorsmark` (the rung directly above `terr_T1`, `state/gate.py:452-487`); that seat is null-conferral and held by the King, who dies in the first season, so it is vacant by season 2 in every seed and after that no `revoke` can pass. Hand-built with an `office` operand through that seat, `revoke` closes the hold and opens a `ban`; through the King's own seat it is refused (round-3 re-run) |
| migrate | always to an occupied hearth (capacity 1), though 185 of 211 hearths are empty at build: every effect call was `hearth, ascends, FULL` (81/81 in seed 0, re-run; 142/142 and 141/141 in seeds 1 and 2), the `to` operand being the question's subject (`decision/options.py:1045-1046`). A hand-built `migrate` to an empty hearth executes (`residence.changed`; round-3 re-run): 81/0, 143/0, 143/0 |
| secure a succession | seven seats have no conferral basis and cannot be refilled (§5b); the King dies in the first season in all three seeds, leaving the throne and the Duke of Valorsmark's seat vacant; the only refill in the three seeds is seed 1's `confer` of the Senior Inquisitor's seat, a self-conferral |
| relief transfer | no larder drains with a mouth unfed at any MATTER (at tick 0 there is nothing to drain; after it, surplus), so no shortfall claim exists; 0 shortfall Observations in seeds 0 and 1 |

**Counter-play that exists:** a rival in a seat above yours may `revoke` you (and ban you, if you were appointed); the same
rival may `confer` your seat on another if you hold no live `commit`; your men may `release` their oblige; a
steward who sends the treasury to his own hearth simply lets the terms lapse. **Seat business is
public**: the chronicle channel deposits, for everyone alive, any Event whose *kind* a `binding_decision` row emits —
your `tenure.opened`, `order.given`, `dispensation.issued`, and also every MATTER lapse (`tenure.closed`)
(`epistemic.py:652-654, 685-686`). `requisition.taken`, `transfer.made` and `duty.taken` are not such kinds.

### 5d What the mechanics structurally reward and punish

- **Production needs no labour.** Yield is base × condition; nobody has to work a harbour. A Site at full condition with
  no works cannot be worked or restored higher; the only thing that changes yield is wear (−1% a season, truncated). This is the
  accrual-by-structure shape the repo's precedent companion lists as absent (I-22, written against `facility_tier`, which the
  season loop does not carry: `research/valoria_game_precedent_companion_v1.md:553`, `..._part4.md:297`); Heroes of Might and
  Magic's town dwellings are the precedent shape (`research/game_precedent_suite/tutorials/T17_repo_strategy_a.md`, HoMM §2.3).
- **Food is in surplus within any plausible horizon** at shipped numbers: ~38 grain made against 4 eaten per settlement
  per season. Not forever: harbours wear 10 a season and nothing repairs them in the realm (`restore` 0 successes), so
  condition reaches 0 after 100 MATTERs and grain yield truncates to 0 a few ticks earlier (`int(40 × c/1000) = 0` once
  c < 25). The cover reading D02 quotes (21.7 → 41.7 seasons) sums *all* stores, ore and timber included; grain alone
  is 40/4 = 10 seasons after the tick-0 MATTER.
- **Every settlement is the same economy.** `build_realm` gives each of the 37 settlements one Site of every yielding kind at
  full condition (`harness/populated.py:772-777`), so each makes grain 40, salt 30, ore 50, timber 10 and none lacks what another
  has; nothing gives a reason to move goods between places. [precedent: `research/game_precedent_suite/tutorials/T10_npc_economy.md`,
  Anno 1800 §2.7 and §7, where island fertilities decide what each can make and trade routes move the surplus]
- **Stores never cap, spoil or cost anything.** Wear touches Sites only (`rosters.yaml:1422`); realm stores rise 0 → 9,250 in two
  seasons (37 settlements × 250 after the tick-1 MATTER; round-3 re-run, §8). Ore has no reader at all (no `.py` under `loop/`,
  `queries/`, `state/` or `seam/` names it, grep at `51d7b05`); timber's only sink is `works_cost` (10 per Site, `rosters.yaml:1501`).
- **War costs no production.** Yield has no labour term (`loop/matter.py:589-591`) and one Felled deletes a cohort whole (ERRATA C1,
  personal combat), so a lost fight removes a settlement's eaters and none of its yield.
- **The horizon is measured on two seasons and three seeds**, plus the yield arithmetic above; no campaign-level instrument exists
  (`CLAUDE.md` §7).
- **Treasuries are hollow.** Seats sit on territory/duchy rungs, which yield nothing; paying anyone needs a requisition
  first. Upkeep is cheap (1 unit per man per 4 seasons) relative to settlement surplus.
- **Governing leaves no rule behind.** No act sets a standing parameter: `issue` mints one writ for one executor that nothing at
  MATTER reads (`verb_table.yaml:561`; a held writ seeds its holder's own act operands, `decision/options.py:915-930`, but nobody is
  bound to act on one), and `tax`, `ration` and `proclaim` are DESIGN-ONLY (§7). Nor is there a standing tribute: a treasury refills
  only when its holder spends one of his own acts on a `requisition`, each time (`loop/effects_governance.py:426-464`). A seat's
  power lasts as long as the act that uses it. [precedent: `research/game_precedent_suite/tutorials/T01_realm.md`, Victoria 3 §3
  (a law is a standing parameter) and Crusader Kings III §2.6 (vassal contracts deliver tax and levies automatically)]
- **Population is fixed and only falls.** Cohort weight is set at build; nothing births or attracts a person (the only mint is CENSUS
  individuation, `loop/census.py:106`, TESTS-ONLY; the closed cast of 46 is ruled, ED-WR-0011, Jordan 2026-09-13, Option A, "for
  now"), and persons fall 83 → 74 in two seasons of seed 0 (every death is combat, ERRATA G9). Capacity therefore gates movement
  inside a fixed population.
- **Holding is never penalised.** Each live `hold` adds 1 to the budget up to the 10-cost ceiling (`decision/budget.py:57-61`), and
  nothing charges for holding more: one person may hold several seats (seed 1's self-conferral seated a holder who already held a seat),
  so no assignment is an opportunity cost. [precedent: `T01_realm.md`, CK3 §3 (the domain limit); `T18_repo_strategy_b.md`, Stellaris
  §3 (Empire Size)]
- **Governance does not touch output.** Yield reads a Site's condition only (`loop/matter.py:589-591`), so a vacant seat, or the
  vacant throne, costs no yield. [precedent: `T13_koei.md`, Knights of Honor II §3 and §7, where a governor is the output multiplier]
- **Upkeep must be paid to where men stand.** Men scattered across hearths need one transfer per hearth.
- **Unseating has one gate, two exits.** Both `revoke` and a displacing `confer` need revocation authority over the
  seat; `confer` also needs a holder with no live `commit`, and in exchange seats your man in the same act and bans
  nobody. Only `revoke` of an appointed holder bars him from returning. A seat with no revocation basis can only be
  filled when vacant — and a seat with no *conferral* basis cannot be filled at all, so the throne never refills.
- **Crowds dilute labour and damage.** One person truly alone at a Site raises it to its ceiling, or (sabotage) to 0,
  in one act (`[ASSUMPTION]` on `_fall`); n present means 1/n per act. At a realm settlement's Sites the cohort is
  always present, so an individual gets at most half per act, and the cohort acting alone (n = 1) gets the whole.
- **Dead ends:** `dispatch` writes nothing (an order no decision reads); `exchange` and `succeed` rows have no effect;
  `coin` exists and no shipped world uses it.

### 5e What success leaves in the world

New `hold` and `oblige` Tenures with terms and `declared_by` citations (who last paid whom); moved `stores`; new Rungs and
Sites with a founder's `hold`; `ban` edges on revoked appointees; and public `told_by` hearsay, in every ledger, of
every event whose kind a binding-decision row emits. Lapses cite the act that last wound the clock, so an establishment's collapse is traceable to the last
payment.

## 6 How it connects

| other subsystem | you feed it | you draw from it |
|---|---|---|
| Persons / NP | cohort bodies (would fall with hunger if `body_step > 0`); individuation by CENSUS when a `dispatch` names an absent id | who is present / resident; deaths close seats and service |
| Decision layer | seats in your tenure set (tier-1 attention to your purview); `granted_acts` decide which remit acts you are offered | candidates; operands for relief transfers from shortfall claims |
| Information | shortfall Observations; chronicle hearsay of every event whose kind a binding-decision row emits; `post_remit` channel to obligees | the claims that tell a governor a place is short |
| Factions | seats carry a faction (from `body`); `holder_faction_of` a place is read by `seize` and mass battle | "same faction" for `rung_above_same_faction` revocation |
| Mass battle | `fortification_of` = mean garrison condition / 1000 in a subtree; `mustered` | `march` relocates claimants (`_relocate`); `seize` changes who holds a settlement |
| Social contest | — | `determine` opens `ban` (blocks confer, oblige) and `detain` (blocks move, migrate) |

**Combinations.** Requisition → transfer is the only built way to put food anywhere but its source. Confer → (others
swear) → upkeep would build a paid establishment, and IN-40 makes a sworn seat-holder's ground part of your purview, so
vassals extend where you can requisition and confer. `build` a dwelling → capacity rises at the rung and every ancestor
→ `migrate` admits a newcomer.

## 7 Playing it as proposed

All **[PROPOSED]**: none of these runs. GV is planned at 20 rows (12 shipped + 3 planned + 5 new; the 5 parked names are
not rows), governed by `proposals/2026-10-16-verbs/` verbs-03 §III.5 where a lexicon body disagrees (ERRATA G19).

- **[PROPOSED] Hunger as a settlement reading (RB-5, REM-50/51/52; JQ-6).** A Query `hunger(w, S) → (band, cover,
  unmet)`: `cover = A/D` (stores at S and beneath ÷ demand per season), `unmet = (D − G)/D`; bands `starving` if
  unmet > 0, `hungry` if cover < 1, `lean` if cover < 2, else `fed` [ASSUMPTION; JQ-6]. REM-51 attaches a hunger
  Observation to the existing larder write, so governors and cohorts hold `(town, hunger, band)` claims; REM-52 ships
  `body_step = 10` (a cohort short 6 units falls 1000 → 940). Even built, it binds only before the first yield and in
  scarce worlds: at today's ratio the realm cannot go hungry after the tick-0 MATTER (ERRATA G18; cover figure caveat in §5d).
  A cohort that falls or dies would also lower no yield (yield reads a Site's condition only, `loop/matter.py:589-591`), so no famine
  spiral could form. [precedent: `research/game_precedent_suite/tutorials/T04_colony_b.md`, Banished §6-7, where dead workers stop
  producing]
- **[PROPOSED] tax / ration / proclaim** — one `edict` Record kind (M-EDICT). `tax` (waits on M-TAX; its other named wait, IN-23, has
  landed since PR #494 as the person-side Queries `legitimacy(p, holder, window)` and `stability(p, rung, window)`,
  `queries/person_q.py:451, 480`, each one person's own windowed estimate, read by the story-bar report and by no chooser or MATTER
  step, `hole_register.yaml` H-224, so MATTER still has no world-level legitimacy to read): MATTER moves
  `amount × yield` of a rung into the seat's treasury each season, capped by stores, `f(legitimacy) = 1`; `defy` withholds
  that season, `evade` reduces the evader's hearth share. `ration` (waits on M-DRAW and Jordan's draw-policy ruling) cuts
  the per-mouth draw. `proclaim` publishes a notice to the residents of a place's subtree. Whether all three take
  `remit:issue` is open (H-52 / L-18). The EC lexicon would instead fold `tax` into `requisition`.
- **[PROPOSED] arrest / pardon** (IN-12 step 5). `arrest` opens `detain` (prisoner → warrant's seat; contested);
  `pardon` closes `detain`/`ban`. The readers already exist: detained persons cannot `move`/`migrate`.
- **[PROPOSED] craft** (M2): inputs → product at one workshop rung, no partials; needs a recipes roster, a workshop Site
  kind, arms/tool kinds; `mint` folds in (coin from ore).
- **[PROPOSED] exchange** (M10, M14): two-sided swap, 4 store writes, price a Query `price_of(rung, kind)` never stored,
  co-located counterparty's consent read off his own prices. The row exists; its effect was declined.
- **[PROPOSED] hire** (M11): the employer opens a paid service edge with a first wage; lapse at MATTER on non-payment.
- **[PROPOSED] borrow / lend / debt** (M9): an advance plus a `debt` Record that MATTER marks lapsed at its due season.
- **[PROPOSED] works fixes**: `build`/`found` minting the works inside the act (one step, H-165); `work` producing via a
  labour tally on yield (M1, factor ≡ 1 control); `restore` narrowed to fabric; `raze` (M-RAZE, re-housing rule open).
- **[PROPOSED] formation fixes**: REM-22 gives `restore`/`work` a `Site` referent class; REM-29 a `room` stem so a refused
  migrant learns.
- **Open decisions named:** D-V1 (depose a living top-seat holder); draw policy; EC-G22/H-159 (unpaid upkeep: lapse, as
  shipped, or arrears debt; precedent has both: desertion in Bannerlord, Total War: Warhammer III and Jagged Alliance 2, carried debt
  in Crusader Kings III, all [V3]; `research/game_precedent_suite/tutorials/` `T02_warband.md` Bannerlord §2.2, `T07_mass_battle.md`
  Total War §6, `T14_squad_settlement.md` JA2 §2, `T01_realm.md` CK3 §6); `dispatch` → `order` rename held (D-V7); H-174 (upkeep to
  presence or residence); IN-48 (delegation without a `hold`, `hole_register.yaml` H-108: no standing order exists, so every
  requisition, payment and conferral is a fresh act against the same budget; DESIGN-ONLY) [precedent: `T01_realm.md` CK3 §3 council
  row, `T02_warband.md` Bannerlord §3 governor row].
- **Stubbed / inert at shipped defaults:** `body_step 0`, `age_step 0`, `illness_rate 0`, `season_factor_draw ()`;
  `Rung.envelope` has no producer; `faction_q.head` always None; Parliament "RULED AND NOT BUILT" (H-90).

## 8 Common mistakes and traps

**Traps in the rules.**
- *A settlement is not an object.* It has no population, unrest or treasury field; all of those are Queries or another
  rung's stores. A seat's treasury is its own rung, and almost no seat sits on a rung that yields.
- *Individuals do not eat* (ED-IN-0255). Grain paid to a person's hearth feeds nobody.
- *MATTER runs before your scenes.* The tick-0 draw always finds empty larders; your acts at tick 0 already see stock.
- *Shortfall is not hunger.* A shortfall Observation needs a larder that *drains*; an empty larder that nobody could draw
  from writes nothing.
- *`work` is not production.* It only advances a works; yield has no labour term.
- *Upkeep goes to presence, not residence* (`home_of`; H-174 unruled), and only through the very seat sworn to, from its
  own rung. Paying from your hearth renews nobody.
- *Through a seat, authority is the seat's.* Purview is asked of `Act.via`, never of the actor's own position.
- *There is no province rung* in `build_realm`: "the rung directly above" a territory seat is its duchy, or the realm for
  the Church's T9 and for unheld territories (`harness/populated.py:734-738`). So a T9 seat could be revoked only from a
  realm seat (and, under `rung_above_same_faction`, only one of the Church's faction).
- *A vacant null-conferral seat never refills* — the throne included (§5b).
- *`requisition`'s second eligibility alternative (`presence:<rung>`) admits an act the effect then declines*, because
  the effect needs a seat to name a destination (`loop/effects_governance.py`, `_eff_requisition`: `dst` is `None` without
  `via`).
- *`dispatch` writes nothing*; an order is an emission no decision reads.
- *Truncation.* `int()` on yield costs a unit of each kind as soon as wear starts.

**Where the draft appendices (GV §A5, EC §A6) were wrong, and the correction used here.**
1. *GV §4 "`transfer` incl. upkeep renewal RUNS-IN-LOOP (barely)" and EC §4 "`transfer` + upkeep renewal RUNS-IN-LOOP".*
   Upkeep renewal never executes: 0 `term.renewed` in seeds 0–2 (2 seasons) and in seed 1 over 6 seasons. The
   executed transfers (1, 0, 5) are cohorts moving grain from their settlement into their own person rung (my probe, §9).
   Renewal is TESTS-ONLY (`tests/test_term_upkeep.py`).
2. *GV §4 "`confer`, `establish`, `oblige` TESTS-ONLY; P1 attempted 0".* Seed 0 only. Seed 1: `oblige` 24/22, `confer`
   5/1, `establish` 5/0; seed 2: `convene` 5/1 (ctl/ files; ERRATA G2).
3. *GV §7 "0 live `oblige` … did not check whether never built or closed by a death".* Two term-less obliges are built at
   world-gen (`harness/populated.py:1317-1339`) and cannot lapse; in seed 0 both closed at tick 1 and both subjects are
   absent from `w.persons` (dead); seed 1 ends with 24 live (ERRATA C5).
4. *"32 offices vs 31 authored — source of the 32nd NOT READ".* It is `off_npc_084` (guild leader), derived with no row
   and no rung (`harness/populated.py:1240-1244`).
5. *GV §1/§2 remit acts as a closed roster.* The tree contradicts itself: `remit_acts` is declared `open: true`
   (`rosters.yaml:316`) while `:315` and `verb_table.yaml:257, 801, 1478` call it CLOSED. Both readings are in the tree.
6. *GV §2 table: `work` gate "presence at the Site".* `work`'s typed precondition is `condition ≥ floor` only, no
   presence clause (`verb_table.yaml:1509-1517`); the rise needs a live works naming the Site (ERRATA C5).
7. *EC §4 "`work`, `restore`, `sabotage` RUNS-IN-LOOP (bodies)", "`requisition` RUNS-IN-LOOP (body)", "`found`, `build`
   RUNS-IN-LOOP (bodies)".* By the grade rule (ERRATA G1) all are TESTS-ONLY: 0 successes in all three seeds.
   Unresolved conflict kept open: `requirements.yaml:165-166` and `rosters.yaml:1461-1463` say `restore` executes on the
   realm's settlement fabrics, while the control runs show 0/23, 0/31, 0/30, and my probe finds every computed `restore`
   formed on a non-Site referent.
8. *GV §3 "no act publishes to a purview".* True of purview-addressed publication, but the chronicle channel deposits, for
   everyone alive, every Event whose *kind* a binding-decision row emits — whoever produced it, MATTER's `tenure.closed`
   included (`epistemic.py:652-654, 685-686`; ERRATA C5 as narrowed by round-2 C5).
9. *"5 scene actions per season".* The budget is `max(1, 5 + live holds − body bands − legs)` cost units; an extended
   scene (2–3 acts) costs 2; budget 5 buys 7 acts (§0; round-2 C1, which resolves ERRATA G11).
10. *GV §6 "R-05 … the lexicon contradicts itself" and L14's "20 vs 25 rows".* Per the verbs override rule
    (verbs-03 §III.5): GV is 20 rows (12 shipped, 3 planned, 5 new; the 5 parked names are not rows), and the
    `dispatch` rename is held as D-V7 (ERRATA G19).
11. *GV §7 links the missing obliges to "9 deaths" without saying what kills.* At shipped values MATTER kills nobody
    (`body_step 0`, ageing and illness skipped); every realm death is combat (ERRATA G9), so the two authored servants in
    seed 0 died in fights, not of hunger.
12. *GV §2, EC §2 MATTER order omits claim decay.* MATTER also decays claim confidence (`claim_decay_per_season=5`,
    `loop/matter.py:317-347`) (ERRATA G8).

**Doc/code mismatches inside the tree.**
- `loop/effects_economy.py:330-337` and `loop/predicates.py:381-385` say no computed act forms an `oblige`; `loop/matter.py:292-295`
  says one does since IN-10 (a), and seed 1 executes 22. The first two notes are stale.
- `epistemic.py:652-665` says the chronicle channel "matches nobody"; its own later paragraph (`:666-684`) measures it as
  the only channel minting `told_by` in the realm.
- The D02 cover figure (21.7 → 41.7 seasons) is reproduced only if A sums every kind (130 / 6 after the tick-0 MATTER,
  250 / 6 after tick 1, my run): ore and timber count as food in that reading.
- Population may exceed capacity (`set_s_001` 12 vs 9 at build; after two seasons of seed 0, `set_s_001` 10 vs 9,
  `set_s_006` 8 vs 7, `set_s_036` 8 vs 6): capacity gates newcomers only.

**§8 Round-2 corrections** (audit2; each cited line opened before accepting).
1. *F1 (S1).* My §5d said a seat with no revocation basis "can only be filled when vacant", implying every seat can be
   refilled. False for the six `conferral: null` seats: `_req_confer` refuses on `has_conferral_basis`
   (`loop/predicates.py:126-127`; `offices.yaml:188, 201, 214, 240, 253, 266`) and `succeed` has no effect. Added §1 row
   note, a "Secure a succession" play in §5b, and a §8 trap.
2. *F4.* `rung_above_in_holdings` is "parent rung *and you hold the target seat's own rung*" (`state/gate.py:553-565`,
   `in_holdings(w, actor, off.rung)`), not "you hold the parent rung". Fixed in §2.3 and §5b.
3. *F8.* The rung above a territory seat is the realm for T9 and unheld territories (`harness/populated.py:734-738`).
   Fixed in §1 and §8.
4. *F9.* At realm settlement Sites the cohort is always present (`harness/populated.py:439-442`), so an individual's
   share is at most 1/2. Added to §2.5 and §5d.
5. *F12.* `transfer` executes at seeds 0 and 2 (1, 5), not seed 1 (37/0). Fixed in §0.
6. *F14.* Six minted seats keep their row ids (`offices.yaml:120-127`). Fixed in §1.
7. *F15.* `evade / defy` is not resolvable (`verb_table.yaml:403-408`). Fixed in §4.
8. *F16.* CENSUS individuation is TESTS-ONLY: `person.individuated` 0 in all three ctl seeds. Fixed in §0 and §4.
9. *F19.* "Permanent surplus" overstated: unrepaired harbours reach 0 after 100 MATTERs; `body` is not a Site
   (`rosters.yaml:1386`). Fixed in §5d and §1.
10. *X1 / C1.* "Each act costs one of your 5 scenes" was wrong: cost budget, extended scenes cost 2
    (`data/fixtures.py:489`; `decision/choose.py:643-657`; `loop/driver.py:456`). Fixed in §0 and §4.
11. *X7 / C4.* The remit roster is both "open" and "CLOSED" in the tree; and `remit_default` is applied in the shipped
    build. Fixed in §1 and §8 item 5.
12. *X8 / C9.* The cover-figure caveat is kept in §5d and now referenced from §7.
13. *X16.* Added a `comply` row to §4 (`verb_table.yaml:183-206`).
14. *X17 / C5.* The chronicle is a kind filter, not "every binding-decision act". Fixed in §1, §5c, §5e, §6, §8.
15. *X19 / C2.* Run columns are attempted/ok throughout, with "attempted" defined as reaching the fold.
16. *X20 / C3.* Tick numbers replace "season 0/1" in §2.2, §3, §5, §7 and §8.
No round-2 finding assigned to T08 was rejected. One I did not verify myself: `pursuit.moved` (from `determine`) is among
the broadcast kinds (C5); I took it from the audit.

## 9 Checks

Opened at HEAD `a4ca9a5` (paths under `engine/season/`): `loop/effects_economy.py:20-356` (work, `_rise`, `_fall`,
sabotage, restore, transfer, `_renewals`); `loop/matter.py:280-305, 455-475, 575-610` (term lapse, shortfall, yield);
`state/gate.py:353-410, 452-500, 560-575, 590-730` (purview, rung-above rules, `REVOCATION_DISPOSAL` at :599, `may_revoke`
:660, `may_fill` :675, `may_renew` :698); `loop/predicates.py:97-165, 337-399` (`_req_confer`, `_req_oblige`);
`loop/effects_governance.py:426-464` (requisition); `loop/effects_shared.py:139-144`; `loop/effects_information.py:60-90`
(works producer); `decision/options.py:528-560, 859-900`; `decision/budget.py:50-64`; `loop/deliberate.py:86-98`;
`data/fixtures.py:217, 228, 286, 495-503, 526, 594, 606-607, 882, 895`; `rosters.yaml:314-322` (and grep of row lines
101-2520); `verb_table.yaml` rows dumped by `yaml.safe_load` for the 21 verbs in §4, and `:1509-1517`;
`requirements.yaml:163-167`; `rosters.yaml:1459-1464`; `harness/populated.py:1236-1246`; `epistemic.py:649-690`.

Ran (read-only, `python3 -I`, scripts and outputs in
`t08/`):
- `worked.py` — §3: `build_realm(0)`, MATTER at ticks 0–5 alone, hand-built `oblige` ×3, `requisition`, `transfer`
  through `off_npc_037`. Results as tabled in §3 (stores 40/30/50/10 → 75/57/99/19; harbour 990, 980 … 940; terms 5 → 9
  for two men; third edge closed at tick 5; `capacity(set_s_001)` 9).
- `why.py 0`, `why.py 1` (`why_seed{0,1}.txt`) — refusal kinds per in-scope verb, fate of the authored obliges, record
  kinds, transfer payloads, seat-act payloads; 0 shortfall-bearing `stores.changed`.
- `payloads.py` (`payloads_s0.txt`) — referent class of every computed `restore`/`sabotage`/`work`/`found`/`build`/
  `migrate`/`revoke`; settlement population vs capacity.
- `follow.py 1 6`, `follow.py 0 2`, `follow.py 2 2` (`follow_s{0,1,2}.txt`) — executed transfers (all cohort → own
  person rung), the seed-1 `confer` (Confessor onto `off_senior_inquisitor`), live obliges per season (seed 1: 2, 24,
  40, 43, 47, 35), `term.renewed` 0 throughout.
- Control counts from `ctl/realm_seed{0,1,2}_2seasons.txt` (script `ctl/control.py`), compared by `diff`.

Could not confirm: why `p_npc_004` no longer held `off_senior_inquisitor` when the seed-1 `confer` passed (vacancy
not traced); the in-tree claim that `restore` executes in the realm (§8 item 7).
