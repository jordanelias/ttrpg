# SE — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: f83534e (working tree)

Addendum to `audits/07_SE_audit.md` (read at `601e715`). `git diff --stat 601e715 f83534e -- engine
modules systems references tools workplans registers` is empty: the only commits between the two reads
are this suite's own files, so every reading the first audit took stands at this HEAD unless this file
says otherwise. Finding numbers continue the first audit's (`F-SE-17` on); resolution numbers continue
its §6.2 (`R-SE-26` on). This file edits neither the first audit nor its six proposals; where it
supersedes one of them it does so by a `_B` proposal and says which section is replaced.

Scope of this addendum, by the work order: (1) the reading the first lane reported as not done;
(2) corrections and new findings; (3) the settlement as a playable, living game; (4) the campaign supply
and muster layer owed to mass battle; (5) decisions on the first lane's placeholders; (6)
capability-authoring consequences; (7) proposals; (8) evidence log.

`.designs/` and `.audit/` are ARCHIVED-NOT-CANON and are cited below as referents by path, never as the
reason a behaviour is correct (CLAUDE.md §0.05). Research is tier 3 (`engine/season/rosters.yaml`
source-precedence note): it informs and settles nothing, and the sourcing floor binds every figure.

## 3. The settlement as a playable, living game

### 3.1 What the design set intends (read in full; ARCHIVED-NOT-CANON, intent only)

Written before the rest of the reading was finished (CLAUDE.md §10 pt 2); §3.2 onward and §1, §2 follow.
Paths are under `.designs/systems/settlements/reference/` unless given otherwise.

**Scarcity.** The design never treats food as a stock that is simply short. It treats dearth as an
*entitlement failure a governor answers* (`settlement_layer_v30.md` §4.3a, after Sen, Scott and Thompson):
a dearth fires when a settlement's Prosperity is 0, when a grain route to it is cut, or when a levy is
taken from a place already poor; the ruler's *invariance* under dearth (taking the standard levy anyway)
is what detonates. The response menu is five acts, each with a loser: Open Granary (stock down, support
up), Fix Prices (merchants wronged, a black market risked), Requisition (*"relieves this settlement by
stripping a neighbor: displaces the Dearth to that neighbor next season"*), Ignore (riot, *"millers and
merchants first, then the governor"*), Provision (pay now to stock before the crisis). So the intended
scarcity is three things at once: a stock (a granary of 0 to 3 per settlement), a route, and a
governor's choice among people to wrong.

**Differentiation.** Three layers of it, none built. (i) A settlement's *type* sets what it produces and
who has a natural claim to run it (§1.1 "the CK3 principle", §1.2: Seat, City, Town, Fortress, Port,
Cathedral, Mine, Outpost; the registry in §2.1 adds Village, Fortress-City, Cathedral-City, a taxonomy
drift the generation sourcebook lists as blocker B3). (ii) A *province's ground* sets dependency: T5
Feldmark and T6 Stillhelm are tagged grain sources, Port-type settlements import, and *"every
non-breadbasket settlement needs a traced route on the existing adjacency graph to a grain source or a
Port"*; a cut route puts dependants one season from dearth (§4.3b), the stated purpose being to give
teeth to *"Hafenmark food dependency has no mechanical teeth"*. (iii) A *sub-feature* carries the
specific asset: the Feldmark Storehouse (*"controls food supply to northern provinces"*), the
Halvarshelm Mines, Gransol Harbour, the Ehrenfeld Barracks (*"standing-army production capacity"*), the
Lowenskyst Garrison Town (*"supply depot"*) (§2.2). The settlement generator states the same thing as a
conditioning rule: P8 Economy (grain, toll, trade, mineral; grain-route dependency) is drawn from P1
Location and P4 Type, and the coupling *"P8 (grain) ↔ P14 (Crisis): grain dependency arms the Dearth
fuse"* must be sampled jointly, never independently (`settlement_generator_v1.md` §1, §2).

**Population dynamics.** The design's population is a settlement **Weight** (`W_s = base(Type) +
Prosperity + FacilityTier`, 1 to 11, §1.8) and it moves both ways: a settlement in dearth or disorder for
two consecutive seasons loses 1 Weight to emigration; it recovers +1 per four stable seasons up to its
structural ceiling; and the leavers arrive somewhere, *"the nearest higher-Order settlement reachable on
the adjacency graph"*, as labour (§1.8c, *Weight loss as Exit*, after Hirschman). The 2026-09-10 proposal
set, ratified as intent, gave the same quantity a clock (`proposals/2026-09-10-settlements-factions-populations/02_PROPOSALS_SUBSTRATE.md`
P2, births scaled by `fed_ratio`, deaths raised by shortfall), and Jordan ruled its bound on 2026-09-17:
*"MATTER PLUS HEARTH CAPACITY … `found` (P4, 'found and build') is the throttle. SCOPED TO POPULATIONS"*
(`proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml` RR-2; `registers/editorial_ledger_se.jsonl`
ED-SE-0051, last row `ruled`). A ruling on what bounds growth presupposes growth. This bears on the first
audit's survivor S-SE-1 (§5 below).

**Ground and movement.** Armies and travellers move over a settlement graph with typed edges (road,
river, mountain pass, coastal, gate; `settlement_adjacency_v30.md` §1.1), on a per-season march budget
(`march_layer_v30.md` §1: `Military × 100` pixels, cavalry ×1.5, a skirmish column ×1.3, capped ×1.7;
the older rule, `Military ÷ 2` edges a season, is in the adjacency document §1.3); an invader must
engage or bypass the settlement its edge enters (§3 there); a bypassed garrison sorties against the
supply line; a fortress cannot be bypassed without a margin of 3 (`settlement_layer_v30.md` §5.1);
*"armies operating beyond a finite supply radius (default 8 settlements from a friendly Mine, Cathedral
or Port supply node) accumulate Attrition strain"* that converts to losses at Accounting
(`march_layer_v30.md` §1.3); winter closes passes (§2.4 there). Every figure here is marked provisional
in its own document (ED-781's calibration was never run).

**The loop a player plays.** Two descriptions exist. The canonical-by-status one is four stat-raising
acts, one free per season (`settlement_layer_v30.md` §3.2: Develop, Fortify, Pacify, Administer). The
redesign's own diagnosis of it is the best sentence in the set: *"governing collapses toward 'roll one
die a season and watch numbers' unless a GM carries it"* (`governance_play_redesign_v1.md`, head). Its
answer is governing as *choosing under constraint*: a bounded budget (2 to 5 points), eight verbs each
forcing a *method* that hands power to someone (Develop by treasury, guild charter or corvée; Fortify by
garrison, militia or walls; Keep Order by consent, force or clergy), a mandatory order from above each
season answered by comply, bargain or defy, needs from below that conflict with it, and a durable
per-settlement record (precedent, grudge, debt, reputation). That redesign is tier 4 in the engine's
source precedence (`engine/season/rosters.yaml`: *"just for ideas. do not treat as required"*), its
event deck and ambition tick were refused as unlicensed clocks (`05_COLLISIONS_AND_RESIDUE.md` rows 5,
16: *"REFUSE the tick · RE-EXPRESS (it already exists)"*), and its worked example, the Goldenfurt
slice, was verified by its own authors to contain a one-way ratchet, a no-acceptable-out vise and seven
fields its deck read that its schema never held (`goldenfurt_slice/reference/verification_findings.md`:
32 findings, 15 high). What survives of it as intent, and is nowhere contradicted by a ruling: *the
settlement is where an order from above meets a need from below in front of a person who cannot serve
both* (§1.4, §1.5 of the redesign), and *a place remembers what its governors did* (§1.6).

**What the design does not contain.** No rule for what a newly founded place is for; no labour
allocation (who works which Site); no spoilage, storage capacity or transport cost for goods; no price.
Those are the colony-sim core (§3.3), and they are the 2026-10 workplan's additions (CP-T08-01, -03,
-05), not the archived design's.

### 3.2 What the present kernel is against that intent (readings at this HEAD)

The first audit's readings stand (no code moved). Read against §3.1, and with one probe added
(`realm_probe.py`, §8 E-2):

| intended | at HEAD | reading |
|---|---|---|
| a stock, a route, a governor's choice | a stock with no ceiling and no decay; no route; a choice formed once per crossing | first audit §1.4; unchanged |
| type sets production; ground sets dependency | every settlement mints `harbour` and `seam`; `type` selects buildings only | `site kinds {harbour: 37, seam: 37, dwelling: 211, garrison: 37}` |
| population moves both ways and arrives somewhere | 37 cohorts, every one weight 2, no writer | `weights {2: 37}`; population 120, capacity 212 |
| a place has a holder who answers for it | 17 of 34 seats sit at three territory rungs (T1, T9, T15), 10 at duchy rungs, 4 at the realm, none at a kingdom settlement | `office rung kinds {territory: 17, duchy: 10, realm: 4, settlement: 2, None: 1}`; the two settlement seats are the foreign pair at `set_alt_1` |
| an army is raised somewhere and fed from somewhere | no army Record at build; no training Site of any kind; a ration per field, off | `armies: []`; `training kinds present: {}` |

Two facts in that table were not in the first audit and change its proposals: where the seats are
(F-SE-17) and that the realm can train nothing (F-SE-19).

### 3.3 The colony-sim and policy-sim precedents, as sourced

Sourcing floor first. `tables/R3a`, `R3b`, `R8`, `R9` are second-pass verified copies that tag every cell:
`[V2]` a page body read, `[S2]` a search snippet, `[M]` memory. Only `[V2]` cells are used below as
evidence of a shape; no figure is taken from any of them; `[M]` and `[S2]` cells are named as leads.
Research is tier 3 and settles nothing.

**Shapes on which three or more independently sourced games converge** (the test `research/00_INDEX.md`
§1 sets for weight):

| shape | sourced in | the kernel today | what it would take |
|---|---|---|---|
| **Labour is the scarce input.** Output is bounded by hands, and the player's main lever is who works what | Banished (a *count* per profession, `[V2]` Citizens); RimWorld (priorities 1 to 4 per pawn, `[V2]` Work); Dwarf Fortress (work details as permissions, the engine picks the dwarf, `[V2]` Labor); Songs of Syx (workers per room, a priority screen, `[V2]` V63, V71); Anno 1800 (a workforce pool per tier, shortage lowers efficiency to zero, `[V2]` Workforce); Frostpunk (assign per building, shift laws, `[V2]` gamepressure) | yield reads no person | CP-T08-01, as planned. The plan's own stop rule (*"a worker is assigned or refused"*) declines allocation; the precedent says allocation is the lever, so the kernel will have labour as a bound and not as a choice. That is a deliberate narrowing and should be read as one |
| **Population answers conditions.** People arrive when a place is safe, fed and has room, and leave or die when it is not | Dwarf Fortress (waves scale with created wealth; a five-year danger score from deaths deters them, `[V2]` Immigration); Songs of Syx (immigration rate, riots on low loyalty, natural reproduction since V71, `[V2]`); Anno 1800 (residents per house rise as needs are met; an unlinked house empties, `[V2]` Population, Residences); Manor Lords (migration by approval tier, `[S2]` for the tiers, `[V2]` for the older thresholds); Banished (homeless villagers have no children: one forum post, anecdotal) | weight is a constant | the falling arm (first lane) and the rising arm (§5, `07_SE_population_regrowth_B.md`) |
| **Unmet needs become refusal.** Mood is the channel from scarcity to disorder: people stop working, stop paying, riot | Anno 1800 (rioters stop working and paying, `[V2]` City incidents); Songs of Syx (law trades happiness for loyalty; riots, `[V2]` V71); Frostpunk (Hope and Discontent; sustained failure ends the game, `[V2]` Wikipedia); Tropico 6 (approval, faction loyalty in three levels, `[V2]` gamepressure) | hunger lowers a body and nothing reads it socially | CP-T08-06 (`unrest`), then the cohort's own reasons (CHAR). The engine's rule that no social quantity moves at MATTER means the channel must be claims and acts, which no surveyed game does: a null, below |
| **Places differ, so goods move.** | Patrician IV (each city makes about five of twenty goods, `[V2]` Cities); Anno 1800 (island fertilities, by way of `D_T08` row 32); Total War: Rome II (a general musters *that region's* troop types only, `[V2]` manual, by way of `R6`) | identical places | the first lane's endowment table (§5) |
| **Governing acts do not roll.** A policy takes effect; its cost is in its consequences | Democracy 4 (policies always apply, delayed by inertia, `[V2]` manual mirror); Tropico 6 (no source gives an edict a failure roll, `[V2]`); Suzerain (no dice; bills fail by vote count, `[V2]` wiki). R9's own attack on this claim found it false for Dragon Age: Inquisition's war table | no settlement verb is a test | nothing: this is the one precedent the kernel already has by construction, and it is the right one to keep. The uncertainty belongs in the world (the weather draw, the field), not in whether a steward manages to open a door |
| **An army is fed and paid every turn, cheaply at home and dearly abroad** | Total War: Rome II (upkeep from the treasury each turn; replenishment only in friendly land; a siege starves, `[V2]` manual); Songs of Syx (rations mandatory, a supply depot, supply anywhere in one's own territory, `[V2]` V66 to V69); the tree's own historical pass (*"Campaign Supply … flat … for any units in hostile territory"*, committed 2026-04-17, `research/historical/precedents_warfare.md` §8) | one ration per field, off | §4 |

**Named, not understood** (the tree cites it; the code has nothing of it): storage and haulage as a
constraint (Dwarf Fortress stockpiles and hauling labour; Manor Lords storehouses, mostly `[M]`); price as
a function of local stock (Patrician IV: `[V2]` for the four-step indicator and the 200-brick example;
*"the stock-to-price equation itself was not found; do not quote one"*, R8). CP-T08-05's formula is
therefore the repository's own, as the first audit said.

**Nulls** (problems no surveyed game solves; findings, not gaps to paper over):

- No surveyed game runs a population that is *both* an aggregate that eats *and* a single deliberating
  agent. The individual sims (Dwarf Fortress, RimWorld, Banished, Songs of Syx, Tropico) simulate every
  head; the aggregate sims (Anno, Frostpunk) give the crowd no agency. The cohort is the repository's own
  object, which is why F-SE-14 has no precedent answer and why ARC-14 (a marginalised population's
  spontaneous solidarity) needs exactly the property F-SE-14 complains of.
- No surveyed game carries scarcity to disorder through what individuals *know and say*. Every one of
  them uses a meter. The engine's rule (L4, no social quantity at MATTER) is therefore unprecedented, and
  the price is the one the first audit measured: the chain exists and fires once.
- None of the colony sims has rival holders of one population (first audit, restated here for the wider
  set: Songs of Syx's vassalage and Manor Lords' region claims are over land, not people).
- Rationing as a decision is sourced only as law (Frostpunk's Soup against Food Additives, `[V2]`); no
  surveyed game lets a private person hoard against the commons as an act with a trail.

### 3.4 The loop a player plays, verb by verb, and the shortest faithful path

The work order names six: build, supply, tax, migrate, found, ration. Each against the engine's verbs.

| the player wants to | the verb or verbs | executes in computed play (seed 0, three seasons, first audit §1.4) | what is missing, smallest first |
|---|---|---|---|
| **build** (raise, mend) | `build`, `restore`, `work` | `build` 0 of 4; `restore`, `work` 0 attempts | works rows (content, Jordan's: `venues.yaml`); the cause of `restore`'s silence (first audit R-SE-16, still unread); a rate that is the builder's (§6) |
| **supply** (move stock to where it is needed) | `transfer`, `exchange`, `requisition` | `transfer` 2 of 70, both into the giver's own rung; `exchange` 0 of 79; `requisition` 0 of 5 | a destination that is another place (CR-49's class, first lane R-SE-19); an amount (first lane); unlike places (first lane) |
| **tax** | `requisition` (one taking); `tax` (CP-T08-07, a standing order collected by the holder's act) | once in three seasons at seed 1 | CP-T08-07 as planned; a treasury that is where the taxer sits (F-SE-17) |
| **migrate** | `migrate` | 16 of 116, all named persons; no cohort | room and path are the refusals; a cohort's flight is the population dynamic the design intends, and it is an act, not a barrier write (§5, R-SE-27) |
| **found** | `found` | 0 of 7 | works rows; and a founded place that can hold people, which under the ruled capacity bound is what lets a cohort grow (§5) |
| **ration** | none by that name | n/a | **nothing new** (R-SE-29, R-SE-37 below) |

**Ration, read from the code.** Subsistence is ruled territorial (ED-IN-0255): a cohort's draw walks its
home, then every rung above it (`queries/world_q.py::_larder_parts`, `ancestry(home)` cut at the first
non-rung; probe: settlement, territory, duchy, realm). So stock at any rung above a town is *open to that
town by rule, with no act*. A store *off* that ladder (a hearth beneath the settlement, a person-rung, a
sibling settlement) is closed to it. Rationing and hoarding are therefore already expressible, as the
inverse of what the archived design assumed: the granary is open by default, and **withholding is the
act** (`transfer` to an off-ladder store, then `transfer` back in the amounts the holder chooses). The
five dearth responses of `settlement_layer_v30.md` §4.3a map onto built verbs without a sixth: Open
Granary is the default; Provision is `requisition` or `transfer` into the treasury beforehand;
Requisition (strip a neighbour) is `requisition`; Ignore is to withhold, or to spend the treasury on a
field or on one's sworn men instead; Fix Prices waits on a price (CP-T08-05). This is better for a game
with no GM than the designed order: a town does not starve beside a full granary because a chooser
failed to form the right act (F-SE-04), and a famine amid plenty, when it happens, has an author and an
Event trail. What it needs is what the first lane already proposed (an amount that is chosen, a
destination that is a place) and nothing else.

**The shortest faithful path from the present kernel**, as an order. Steps marked (1st) are the first
audit's and are not restated; the rest are this addendum's.

1. Kernel repairs (1st). Spoilage, CP-T08-03 (1st, as planned).
2. Unlike places behind `endowment_mode` (1st), with the table as annotated in §5.
3. **Stock where a holder sits**: world-gen seeds the relief stock at the nearest seat-bearing rung up
   each settlement's ladder, not at every territory rung (`07_SE_treasury_granary_B.md`). This single
   change gives relief, pay and the field's ration one stock and one answerable person.
4. Population that moves both ways at CENSUS: thinning (1st) and regrowth
   (`07_SE_population_regrowth_B.md`).
5. Labour, CP-T08-01 (1st, as planned), reading hands *net of those under arms* (§4).
6. Amount and destination as choices (1st); with them, withholding and relief are both playable.
7. The valley scenario (1st), with its granary moved to the steward's seat rung so that its two policies
   differ by an act the engine already has.
8. `unrest`, `tax`, price, as planned.

Steps 1 to 6 touch no new verb, no new carrier and no new barrier. That is the faithful part: the design's
loop is reached by making the built verbs reachable and their operands a person's, not by adding the
design's stat blocks.

## 4. The campaign supply and muster layer SE owes to mass battle

Cited, not redone: `audits/04_MB_audit.md` §1.2 (the seam: `fortification_of`, `training_sites`,
`settlements.provision`, `Site.condition` wear on `Invested`), §10 (the SE row: *"fortification executed;
provisioning and siege built and off; no training site exists in the built realm"*), §17 (Total War's
supply: *"named at campaign scale"*; campaign to battle and back: *"understood, dark"*), §18.1 (the
referents' sourcing: Bannerlord's wages are memory-grade there; recruitment at settlements and upgrade are
sourced); `audits/06_FA_audit.md` F-FA-03 (who may march is an unruled placeholder), F-FA-04 (no war, no
response), §10 (the SE row: `requisition.taken` 0, 1 and 6 at seeds 0, 1 and 2). The MB and FA addenda B
were being written while this file was; their heads were read (`04_MB_audit_addendum_B.md` B1.1 lists
`military_layer_v30.md`: *"muster output and prerequisites by territory Prosperity, Wealth and a named
officer's history … unpaid professionals lose Discipline … garrison supply"*), their bodies were not.

**What the campaign layer is, in the referents, as sourced.** Total War: Rome II (`tables/R6`, `[V2]`
manual pages): units muster to a general *standing in a region, from that region's troop types only*;
upkeep leaves the treasury every turn; replenishment happens only on friendly ground; a siege starves;
raiding lowers upkeep at a cost in unrest. Bannerlord (`tables/R2`): troops are recruited from every
non-hostile settlement and upgraded with experience and gold (`[V2]`); wages, food and the absence of
supply lines between fiefs are `[M]`. The archived design agrees in shape: Treasury pays for muster by
troop class, upkeep per professional unit, a flat Campaign Supply charge for units in hostile territory,
and a levy ceiling from Military (`.designs/systems/_architecture/reference/derived_stats_v30.md` §8.1);
supply attrition beyond a radius from a friendly node (`march_layer_v30.md` §1.3, uncalibrated). The
tree's own historical pass then *cut* per-unit supply costs and service timers as bookkeeping and kept
one flat rule and one restriction (`research/historical/precedents_warfare.md` §8). The durable shape,
on which the manual, the patch notes and the tree's own pass converge: **an army is raised from the
people of a place by that place's infrastructure, and while it stands away from home it costs its
holder's stock every season.**

**What SE supplies today, and what it owes.**

| the layer needs | SE's part | state at HEAD | owed |
|---|---|---|---|
| **who can be raised** | population (`Person.weight` of cohorts); `raisable_by` (the cohort lives where the faction holds, or is committed to it) | built (`queries/world_q.py:2186`); cohorts hold no `commit` (probe: 0 of 37) | nothing new from SE; CR-107b (FA) |
| **what kind** | training Sites at the cohort's residence (`world_q.training_sites`), read by the MB module's `recruit_limit` | reader built; **no such Site exists in the realm** (probe), so every faction can raise levy and nothing else | Sites from the canon file's own `type` field (F-SE-19, R-SE-35) |
| **what raising costs the place** | nothing | `recruit` writes the army Record only; weight is untouched by ruling (J-C-2, uncoupled); yield reads no person | hands under arms do not work (R-SE-33) |
| **what keeping it costs** | `settlements.provision`: a ration per field from the seat's rung | built, off; the treasury it reads is empty everywhere at build (`stores total: 0`) | a treasury with stock (R-SE-28), then IN-52's flip (planned) |
| **what being away costs** | nothing: the troops are counts in a Record; their cohort eats at home whatever the army does | H-212 (*"an occupied town's stores are untouched by the army standing in it, and a besieged one does not starve"*) | the standing ration (R-SE-34, R-SE-36) |
| **where it can go, and how fast** | the geography file's `settlement_adjacency` (55 edges: 54 road, 1 sea), `terrain_cost_matrix`, `march_budget` | no reader (first audit F-SE-06; re-run: the keys parse and nothing imports them) | design-first, unchanged; not proposed here |
| **walls** | `fortification_of`, garrison condition | executed; garrisons never wear, so every settlement is walled forever (first audit §10) | a siege that wears is built and off (`Invested`); nothing new |

**One stock, three claimants.** The attacker's treasury is the rung of the office the march is exercised
through (`seam/wrappers/mass_battle.py::_seat_treasury`); the defender's is the nearest held rung at or
above the target (`_defender_treasury`); upkeep of sworn men is paid out of a seat's rung
(`loop/effects_economy.py::_renewals`); `requisition` lands at the seat's rung
(`loop/effects_governance.py:538-549`); and a hungry cohort draws at every rung above its home. Put the
realm's stock at the seat rungs and these are one `Rung.stores` with three calls on it: the hungry (by
rule, at MATTER), the sworn (by the holder's act) and the field (by the act of marching). That is the
guns-and-butter decision of every referent, assembled from parts that exist, and it is the reason
F-SE-17's correction matters more to mass battle than to hunger.

**The muster the realm can make** (probe, arithmetic on the MB module's shipped constants, no run of a
field): `under_arms_cap(2)` is 60 troops for a town's cohort and 3,600 for all 120 weight. A cohort of
weight 2 therefore fields 60 levies, below the engine's 100-troop block that the module's own comment
says *"routs at once"* (`troop_types/recruitment.py:38-44`). So the present weights cannot raise a unit
from one place at all; armies exist only by pooling cohorts, and the weights CR-107 will author are a
mass-battle input as much as a settlement one. Cross-listed to MB (its headcount-grade proposal).

Proposal: `proposals/07_SE_campaign_supply_and_muster.md`.

## 2. Corrections to the first audit, and new findings

(Placed after §3 and §4 in the file because it was written after them; numbered as the work order
numbers it.)

### 2.1 Corrections

**C-1 · S-SE-1 does not survive the ladder.** The first audit's §11 says *"No design document supplies a
growth rule; no precedent in the tree settles it."* Both halves are wrong on the reading done here.
(i) `registers/editorial_ledger_se_archive.jsonl` ED-SE-0051, last row `ruled`, records Jordan's answer to
*"the bound on the demographic loop: matter only, or matter plus hearth capacity?"*: **matter plus
capacity, `found` the throttle, scoped to populations**, with ED-WR-0011's closed-cast rider expressly
discharged for populations (`RULINGS.yaml` RR-2, opened at `:1791-1850`). A ruling on what bounds births
is not consistent with a population that may only fall. (ii) The proposal that ruling answered is
ratified as intent (`2026-09-10-settlements-factions-populations/00_INDEX.md`: *"P2/P3 → SE-01"*), and its
P2 states the rule's shape (births scaled by how well the place is fed, bounded by the larder).
(iii) The archived design states a recovery rate (§1.8c). (iv) A recorded ruling on calibration says the
same in general: *"Every negative must be able to be offset by some kind of positive … every decay needs
a growth path"* (`settlement_generator_v1.md` §7 item 4, RULED 2026-07-13, read as archived reference; its
companion ruling in the ledger, ED-IN-0047, is Jordan's *"Build the counter to cumulative"*). Ladder step
1 and step 3. Resolution R-SE-26; what remains is a rate, which is content.

**C-2 · The relief stock was proposed where no one holds it.** F-SE-17 below. The first lane's R3 says
the granary is filled by *"`requisition` into a territory seat's rung (built)"*. The verb is built; the
seats are not there.

**C-3 · ARC-20's gate cannot be met as worded, and the dependency it tests has a recorded ruling the first
audit did not open.** F-SE-22 below.

**C-4 · The Layer-1 conformance claim is no longer `[UNVERIFIED]`.** `architecture/holonic_ARCHITECTURE.md`
§43, §45, §46 and §47 were read. The settlements module conforms: attached by a row naming a role and a
provider and resolved at boot (§43; the first audit's registrar evidence); typed input and output and no
state between calls (§45's `modules/<name>/` line); a cohort is the one `Person` class (§46: *"reviewers
will itch to subclass a cohort: refuse"*, which is also why the first lane's remedy for F-SE-14, a
declared requirement on the verb row and never an `is_cohort` test, is the conforming one). Two notes:
§46 still types **Envelope** as a value, so the first audit's R-SE-20 (delete `Rung.envelope`) is a
Layer-1 edit and not a code deletion, as it said; and §45 puts authored world data under generated
`data/`, so a scenario world built in `harness/` is a port debt, as it said.

**C-5 · The first lane's capability edit would be refused by the CORE lane's loader, and it adds a second
ladder.** F-SE-21 below; §6.

**C-6 · "Irrelevant by ladder step 2" is right for the stress sim's mechanics and wrong for two of its
findings**, which return at this HEAD in the season engine. F-SE-18 below.

**C-7 · The endowment table**: annotated, not replaced (§5).

### 2.2 New findings

Severity as in the first audit: **B** blocks a requirement, **D** degrades narrative, **H** hygiene.

**F-SE-17 · D (B for the campaign layer) · The proposed granary tier has no steward, and is not the rung
the field or the pay chest reads.**
Evidence: probe E-2: seats sit at `terr_T1` (ten Crown court seats), `terr_T9` (five Church seats),
`terr_T15` (one, a territory with no settlement), the three duchy rungs (ten) and the realm (four). Of the
16 territories that hold a settlement, **14 have no seat at the territory rung**. `requisition` deposits at
`seat.rung` and nowhere else (`effects_governance.py:538-549`: *"THE TREASURY IS THE SEAT'S RUNG AND
NOTHING ELSE"*); the field's ration is read at `_seat_treasury` and `_defender_treasury`; upkeep is paid
from a seat's rung.
Falsifier: a seat whose `rung` is one of `terr_T2`..`terr_T8`, `terr_T10`..`terr_T14`, `terr_T16`,
`terr_T17`. Outcome: none.
Consequence: under the first proposal 14 granaries are world-gen stock that no act of governing can
refill, that pays nobody and provisions no field. A granary nobody keeps is a countdown, not an
institution.
Touches R-04, R-01. Fix: `07_SE_treasury_granary_B.md` (R-SE-28).

**F-SE-18 · D · Every settlement quantity has one working arm, so any binding arm is a ratchet.**
Evidence (first audit's runs, re-read as a set): `Site.condition` falls by wear and rises by `restore`,
which is attempted 0 times; `Person.body` falls by hunger and is reset whole by `tend` in the same season
(H-304); `Person.weight` has no writer, and under the first lane's proposal would only fall; `Rung.stores`
only rise. Under the binding arms the first audit ran, nothing came back: 19 of 37 cohorts dead by
season 7 (×10, weather on, seed 1) and all 38 settlements then `fed`.
This is the returning form of the one finding in `.audit/2026-07-12-settlement-season-stress-sim/` that
two methods confirmed (its reconciliation file, §B.1: *"near-universal faction elimination … Flourishing
crowded out … the system is biased to death-spirals"*, the 500-seed batch and the seven-seed play-out
agreeing), on mechanics that are retired. The old finding is not evidence about this engine; the first
audit's own table is. What the old corpus adds is the ruling it produced (C-1 (iv)).
Falsifier: one quantity among the four whose rising and falling arms both execute in a seeded realm run.
Outcome: none at seed 0, three seasons.
Touches R-01, R-09, NERS-R (completeness at the extremes). Fix: the rising arm of weight (R-SE-26);
spoilage for stores (planned); `restore`'s cause (first audit R-SE-16); `tend` is the PC lane's.

**F-SE-19 · D · The realm can raise only levy, raising costs the place nothing, and one town cannot raise
a unit.**
Evidence: probe E-2 (`training kinds present: {}`; `armies: []`; `under_arms_cap(2) = 60`);
`loop/effects_army.py:68-88` (`recruit` writes the Record; no stores, no weight, no yield);
`modules/mass_battle/troop_types/recruitment.py:55-69` (every type but levy needs a Site of a kind the
realm does not contain). The canon file types three settlements as fortresses (S-007, S-014, S-021:
`Fortress`, `Fortress-City`, `Fortress`) and authors one military tenant, `controller_subordinate:
Löwenritter` on S-014, which nothing reads (grep at this HEAD: the YAML line only; the
`2026-08-11-world-schema-gap-audit` row G-37 is still true).
Falsifier: a `barracks`, `archery_range`, `stable` or `siege_workshop` Site in `build_realm(0)`. Outcome:
none.
Touches R-04, R-05 (`recruit` and its siblings are never attempted: MB audit §1.3).
Consequence: mobilisation is free and uniform, so it cannot be a decision. Fix:
`07_SE_campaign_supply_and_muster.md`.

**F-SE-20 · D · Supply has no place and no duration.** The troops are numbers in a Record; the people
they were drawn from stay home, at full weight, eating from their home ladder; the one ration is taken
at the instant of a field from the marcher's seat rung wherever the army stands; a march costs one leg
(H-328). H-212 has stood `absent` since 2026-10-16 with the direction undecided. Fix: same file
(R-SE-34, R-SE-36).

**F-SE-21 · H (cross-lane) · Two lanes' capability edits collide.**
`proposals/07_SE_capability_and_chooser_surface.md` §4 (a) adds `restore`, `work` and `build` to
`rosters.yaml: verb_capability`. `proposals/01_CORE_capability_authoring_surface.md` Edit 4 deletes that
roster, and its Edit 3 has the verb loader refuse *"a `capability:` on a row that neither contests nor is
graded (a column nothing reads)"*, which is exactly those three rows. The same SE proposal maps a held
score to a per-mille through its own table, while `proposals/02_CHAR_capability_uses_table.md` already
defines the form by which a held value becomes a factor (`about_mid`), and the DICE audit's §14 (c)
already defines `score(person, verb)`. Two ladders for one quantity (CLAUDE.md §0.06, S). Fix:
`07_SE_capability_rate_B.md` (R-SE-32).

**F-SE-22 · D · The food dependency has a recorded resolution that points at trade, and the ladder cannot
express dependence between duchies.**
Evidence: `registers/editorial_ledger_archive.jsonl:477`, BALANCE-005, `resolved` 2026-04-13: *"Hafenmark
operates through trade and diplomacy, not territorial control of food supply. The dependency is narrative
pressure, not mechanical."* ED-SE-0009 proposed the reverse on 2026-07-08 and was superseded on the
quarantine of the design tree without the two being reconciled; the world-schema audit's G-32 flagged
exactly this for a ruling. At HEAD the question has moved: subsistence is mechanical for everyone
(ED-IN-0255, ruled after both), so a Hafenmark with no food Site starves whatever the April row says.
What the April row still decides is the *channel*. And the ladder agrees with it by construction: a
Hafenmark settlement's ladder is its territory, `duchy_hafenmark`, `r_valoria` (probe); no rung of
another duchy is on it. So the first audit's gate for ARC-20 (*"Hafenmark's settlements drawing at a rung
another duchy fills"*) can only be met at the realm rung.
Fix: R-SE-30. The gate becomes a store move by a person between a rung under one duchy and a rung under
another.

**F-SE-23 · D · The relief ladder's top is the Crown's, for three duchies and not for the other two
polities.** Probe E-2: the three duchies' settlements end at `r_valoria`; the Church's (`set_s_036`)
goes territory then realm, with no duchy; Schoenland's ends at its own territory. Under any arm in which
the realm rung holds stock, the King's treasury feeds every hungry town of both other dukes and of the
Church, by rule, with no act and no choice of whom. This follows from the ruled ladder and is named, not
re-raised; its consequence is that a king withholds from a rebel duchy only by moving stock off the
realm rung, which is an act with a trail (§3.4). Schoenland has no reserve above its territory at all.
No fix proposed.

**F-SE-24 · H · `amount_shares` at 1000 is the old "strip below subsistence" with no consequence path.**
The first lane's `07_SE_arc_needs.md` §3 (b) offers a share of the *whole* known stock. The stress sim's
third-ranked finding was a deterministic strip with no floor (its §6 item 3), on retired mechanics;
re-read here, the engine's version is the design's intended detonator (Scott: taking the standard levy in
a dearth), and it is only a story once something answers it. Until `unrest` (CP-T08-06) or a cohort's own
reasons exist, the largest share produces deaths that reach nobody. Resolution R-SE-38: sequencing only.

### 2.3 `.audit/` findings re-verified at this HEAD

| old finding | source | at HEAD |
|---|---|---|
| "37 near-identical settlements" | `2026-08-11-world-schema-gap-audit/03_discussion.md:71` | **true**, in a different engine (first audit F-SE-01) |
| the geography and movement layer has no owner and no reader (G-12) | `01_gap_register.md:292` | **true** for adjacency, costs, budget, vision (first audit F-SE-06; keys re-parsed here: 55 settlement edges, 26 territory edges, an 11-row cost matrix, a 3-key budget) |
| province scalars (`fort_level`, `spiritual_weight`, `proximity_calamity`, `starting_pros`) authored and unread (G-48) | `01_gap_register_part4.md:55` | **true**; CR-40 deletes one |
| a second faction role per settlement is authored and dropped (G-37) | `01_gap_register_part3.md:147` | **true**; the loader it blamed is gone and the new builder does not read the key either |
| no persistent military unit, garrison a bool (G-33) | `01_gap_register_part3.md:73` | **false now**: the `army` Record (ED-IN-0306) persists; a garrison is a Site with a condition |
| governor identity has no carrier (G-04) | `01_gap_register.md:148` | **false in form, true in effect**: a holder is a `hold` Tenure; no kingdom settlement has a seat (probe) |
| grain routes against BALANCE-005 (G-32) | `01_gap_register_part3.md:55` | **moved**: F-SE-22 |
| the negative spiral is the default regime | stress-sim reconciliation §B.1 | **not evidence here**; the engine's own form is F-SE-18 |
| a levy strips a declined settlement below subsistence (§1.3a) | stress-sim synthesis §6 item 3 | subject retired; its shape returns in F-SE-24 |
| Π relief valve, recall escape, Seggio lock, Compact against Leverage | stress-sim synthesis and reconciliation | **irrelevant** (ladder step 2): none of AP, Π, the deck, the Ledger families or the Seggio exists in `engine/season/` |
| settlement type taxonomy drift (Village, Fortress-City, Cathedral-City outside the eight) | reconciliation §C.6; sourcebook B3 | **true in the canon file** (probe: types include `Village`, `Fortress-City`, `Cathedral-City`); harmless today because the only reader maps types to buildings in `venues.yaml` |

### 2.4 Provided arcs: cases the first audit's §13 did not list

A second pass over every `need:` line of the case files (regex over all eleven files, the six `chain/`
files included, which do not parse as YAML because they are fenced; 46 cases carry a `core` or
`important` need with a settlement-layer word, 36 of them outside the first table). Most are false hits
(`drain`, `tax` used figuratively). The real additions:

| case | need (short) | hardness | represented today? | change required | owner |
|---|---|---|---|---|---|
| ARC-37, ARC-39, NPC-007 | an ordinary supply chain carries a good whose hazard is invisible; an investigator traces the chain from another case | core | no chain exists to trace: `exchange.made` 0, `transfer.made` 2, both to self | SE's half is only that goods move between places by acts that leave Events (first lane's endowment, CR-49); the hidden property and the tracing are FI's and WR's | FI, WR; SE first |
| EMG-11 | a finite per-location capacity gates a rank, with a named provisional state when none is free | core | no: `capacity` counts dwellings and gates `migrate` only | a second counted Site kind on the same Query (the roster's own note: *"a second housing kind is a roster row"*) and a `requires` cell on the conferral; the rank is FA's | FA, SE |
| NPC-082 | a commander commands levies distinct from the council's | important | in mechanism: `recruit` from cohorts his faction may raise; never attempted | §4 | MB, FA, SE |
| ARC-R17 | a faction's allegiance is a per-location quantity | core | no: cohorts hold no `commit` | CR-107b | FA |
| ARC-14 | a marginalised population's spontaneous solidarity turns a one-axis crisis into two | core | partly, and only *because* a cohort acts as a person (F-SE-14's other face) | CR-107's `label:` and `heritage:` rows, so the population in question exists | CHAR, SE |
| NPC-087 | many small private acts aggregate into a settlement-scale outcome | important | no settlement-scale reader of persons' claims | CP-T08-06's reader is the first | SE |

## 5. Decisions on the first lane's placeholders

Taken by the five-step ladder; the step is named. *Survives* means it goes to Jordan as a question; a
value shipped behind a control arm with the repository's `[ASSUMPTION; Jordan to correct]` mark is not a
survivor (the precedent is every row of `venues.yaml: planned_works`).

| # | placeholder (first lane) | decision | step | survives? |
|---|---|---|---|---|
| P-1 | **The endowment's key**: a table keyed by territory code in `rosters.yaml`, with a settlement override | **stands.** The canon file's `sub:` label (*Breadbasket*, *Northern Mines*, *Timber Valley*) has no reader and is not typed; a table keyed by the canon id is the typed head. CP-T08-02's polygon derivation stays dropped | 5 | no |
| P-2 | **The endowment's rows** | **annotated, not replaced.** Canon-backed (the file's `sub:` and description, or `settlement_layer_v30.md` §2.2, §4.3b as intent): T1 harbour (river-sea nexus), T2 field (heartland farmland), T5 two fields (breadbasket), T6 field (southern farmland; one of the design's two grain sources), T8 harbour (west sea trade), T16 harbour (island republic), T17 two seams (iron and copper). **Unbacked**, shipped as marked assumptions: T3, T9, T10 (seam), T11, T12, T13 (harbour), T14 (field). T4 and T7 are *timber* in canon and receive `seam`, which yields ore 50 and timber 10: mislabelled, and mechanically the same as any seam | 3 for the backed rows; the convention for the rest | no |
| P-3 | *(not raised by the first lane)* a timber Site kind for T4 and T7 | **not added.** Cut it and nothing in play changes: ore and timber have one consumer each (`works_cost`), identically priced. It fails N today. Re-read at CP-T08-04, when goods acquire different uses | 5 | no |
| P-4 | **The one row that changes the political map**: the fjord harbours (T11 to T13) give Varfell fish and salt, so Varfell feeds itself and only Hafenmark depends on the Crown's grain | **stands as marked.** Canon is explicit for Hafenmark (*"Hafenmark food dependency anchor"*) and silent for Varfell. It is the row to look at first, because it decides whether the food question is two-sided or three-sided | convention | no (named for his eye) |
| P-5 | `field` yields grain 40; `harbour` under `ground` yields salt 30 and grain 10 | **stands as shape**; the magnitudes are JQ-6's sweep and CR-22's reading rule, which already exist to choose them | 4 | no |
| P-6 | a settlement starts with one season of its own yield | **stands** (CR-22's own floor rule) | 4 | no |
| P-7 | **the granary's tier and size**: every territory rung, `granary_seasons × deficit` | **superseded**: the nearest seat-bearing rung (F-SE-17). `granary_seasons` keeps its sweep | 4 | no |
| P-8 | `larder_walk: first / through` | **stands**, and matters more under P-7: a town with a little at home must reach the duchy's stock | 5 | no |
| P-9 | `hunger_loss: per_head`; `famine_loss` 0 / 250 / 500 | **stand** as fixtures with a control | 5, 3 | no |
| P-10 | *whether weight may rise* (the first lane's S-SE-1) | **decided: yes**, bounded by food and room (C-1) | 1, 3 | **no longer** |
| P-11 | `amount_shares`: one member shipped, `[250, 500, 1000]` as the flip | **stands**, flipped after `unrest` exists (F-SE-24) | 4 | no |
| P-12 | the `world:` overlay's numbers for NPC-083, NPC-013, NPC-037 | **stand**: case fixtures, authored per case | 4 | no |
| P-13 | the valley scenario's numbers | **stand** as a fixture bannered not canon; **one structural change**: the granary sits at the steward's seat rung (it already does, `terr_valley`), and the `hoard` policy is to move stock off the ladder, not to refuse candidates | 5 | no |
| P-14 | `capability_rate` and the name `building` | **superseded** (§6). The capability's *name* remains Jordan's content | 4 | no |
| P-15 | `field_ration_kinds: [grain]` (first audit R-SE-22) | **stands** | 5 | no |
| P-16 | H-309: a seat holder who migrates keeps the seat | **stands**, with one consequence under P-7: an absentee duke's treasury still feeds his duchy and still provisions a field marched through his seat. That is the absentee the first audit said the engine already carries | 4 | no |

**What survives to Jordan from the SE lane, after both passes:** S-SE-2 only (custody, H-293), unchanged
and not re-adjudicated here: it is a governance question, the FA audit does not take it up, and nothing
read for this addendum bears on it. S-SE-1 is closed.

**Resolutions decided in this addendum** (continuing the first audit's §6.2):

| id | what | resolution | step | carried by |
|---|---|---|---|---|
| R-SE-26 | may a population recover (S-SE-1) | yes: a fed cohort with room regains weight at CENSUS, bounded by matter and capacity as ruled | 1 (ED-SE-0051), 3 | `07_SE_population_regrowth_B.md` |
| R-SE-27 | is flight a barrier write or an act | an act: a cohort's own `migrate`. Births and deaths are the licensed bodies clock; who leaves is a decision (L5). Partial flight waits on CR-107 (several cohorts a place) | 4 | same |
| R-SE-28 | where the relief stock sits | at the nearest seat-bearing rung up the ladder | 4 (`_seat_treasury`, `_renewals`, IN-22's test) | `07_SE_treasury_granary_B.md` |
| R-SE-29 | is relief an act or a rule | the rule (ruled, ED-IN-0255); withholding is the act | 1 | same |
| R-SE-30 | BALANCE-005 against ED-SE-0009; ARC-20's gate | whether hunger is mechanical is superseded by ED-IN-0255; the channel is trade, as the April row says; the gate is a person's store move across two duchies | 1 | same |
| R-SE-31 | the endowment rows | P-2 to P-4 above | 3, convention | none (annotations for the first proposal's builder) |
| R-SE-32 | the capability rate against the CORE, CHAR and DICE surfaces | one form (`about_mid`) on one score (`faculty`), declared on the verb row | 4 | `07_SE_capability_rate_B.md` |
| R-SE-33 | mobilisation costs the place nothing | hands under arms do not work: the labour reader is net of them | 4 (CP-T08-01) | `07_SE_campaign_supply_and_muster.md` |
| R-SE-34 | supply has no duration | a standing ration: an army whose holder stands on land his faction does not hold eats from his seat's treasury each season | 3 (the committed flat rule), 4 (IN-52) | same |
| R-SE-35 | the realm trains nothing | a settlement the canon file types `Fortress` or `Fortress-City` is built with a `barracks` | 3, 4 (`venues.yaml` keys on `type`) | same |
| R-SE-36 | H-212: what an occupier does to the occupied larder | nothing, by rule: the cost falls on the occupier's treasury (R-SE-34). Living off the occupied place is a taking, and the verb for a taking is `requisition` | 3 | same |
| R-SE-37 | is `ration` a missing verb | no: withhold and release, both `transfer` | 5 | none |
| R-SE-38 | when `amount_shares` flips | after CP-T08-06 | 4 | none (a note on the first proposal) |

Thirteen resolutions decided here; with the first audit's twenty-five, thirty-eight. One survivor (S-SE-2).

## 6. Capability-authoring consequences

The first audit's §14 stands for (a) and (b): the settlement layer reads no capability, every magnitude
is data, nothing is doubled. Its (c) and (e) are superseded by what the other lanes proposed after it.

**The surfaces as they now stand** (cited, not redone): `proposals/01_CORE_capability_authoring_surface.md`
(a `capabilities:` block in `references/descriptor_registry.yaml`, a `capability:` column on the verb's
own row, the cast row's `capabilities:` map; `rosters.yaml: verb_capability` deleted);
`proposals/02_CHAR_capability_uses_table.md` (the two closed forms by which a held value becomes a
factor, `about_mid` and `at_least`, implemented once beside the attribute scale);
`audits/10_DICE_audit.md` §14 (c) (the four calls the roller needs, `score(person, verb)` first, and the
list of what a capability may *not* say: no flat bonus to a net, no change of target number, no
reduction of an obstacle, no gate on attempting).

**What SE needs from them, as an interface** (replacing the first lane's):

```
score(person, verb)  -> whole number                        # DICE's; pool.py::faculty today
rate(person, verb)   -> about_mid(score, floor, ceiling, gain)   # one factor, 1 at mid-scale; 1 when the row names none
```

and one declaration: an **uncontested** verb row may name a `capability:` when it also declares that its
effect has a magnitude (`magnitude: rate`). That is a third licence beside *contests* and *is graded* in
the CORE loader's rule, and the only change SE asks of another lane's proposal.

**The four skills the work order names, as data.**

| what a designer wants to author | where it enters, by declaration | axiom, in the tradition's words | state |
|---|---|---|---|
| **labour** (husbandry, mining, fishing: a people's trade) | the cohort's cast row in `cohorts.yaml` carries `capabilities:` exactly as a named person's row would (a cohort is a `Person`); CP-T08-01's labour reader weights hands by `rate(cohort, work)` | *a people is good at what it does*: skill sets the yield of untested work | CP-T08-01 planned; the cohort row has no such key today; CR-107's rows are where it would be authored |
| **craft** (smith, mason, shipwright) | `restore`, `build`, `work` (and `craft`, CP-T08-04) name a capability and `magnitude: rate` | *extended or downtime work: the skilled hand accomplishes more per act* | proposed (`07_SE_capability_rate_B.md`) |
| **stewardship** | through the steward's *acts* only: the amount he takes or gives (a choice, first lane), the rate of what he raises. **No passive bonus from a holder to his domain's yield** | the *domain turn* axiom (a holding yields by its holder's ability) is deliberately not implemented: a yield that reads who sits over it is a quantity moving with no act, and no ruling licenses it | declined, with the reason |
| **trade** | none yet: `exchange` is two store moves with no magnitude a skill could scale. When CP-T08-05 gives it a price, the price the trader obtains is the magnitude | *haggling as an opposed or rated test* | design-first (CR-67); named so that the surface is not built without it |

**A consequence the first audit did not draw: capability is the second way places differ.** The
endowment makes ground unlike; cohort capabilities make *peoples* unlike, and the second is cheaper to
author and richer to play (a mining people moved to farmland farms badly; a conquered town's skill is
the prize). It needs no mechanism beyond the cast row the CORE proposal already gives every `Person`.

**Axioms the settlement layer contradicts**, restated against the wider surface: helping is inverted
(`share` divides one act by those present; first audit); *unskilled use* is indistinguishable from the
default (DICE §14 (d)), so a rate centred at mid-scale must read "no capability named" as exactly 1 and
never as "unskilled".

Proposal: `proposals/07_SE_capability_rate_B.md`.

## 7. Proposals written by this lane

| file | supersedes | carries |
|---|---|---|
| `proposals/07_SE_treasury_granary_B.md` | `07_SE_ground_and_granaries.md` §3 R3 and the territory-rung clause of §4 (c) only; its endowment, stocking, walk and gate text otherwise stand | F-SE-17, F-SE-22, F-SE-23; R-SE-28, -29, -30 |
| `proposals/07_SE_population_regrowth_B.md` | `07_SE_population_census.md` §3 R4 (growth left undecided) only | F-SE-18; R-SE-26, -27 |
| `proposals/07_SE_campaign_supply_and_muster.md` | nothing (new) | F-SE-19, F-SE-20; R-SE-33 to -36 |
| `proposals/07_SE_capability_rate_B.md` | `07_SE_capability_and_chooser_surface.md` §3 and §4 (the roster rows and the per-mille table); its §5 and §6 stand | F-SE-21; R-SE-32 |

No proposal is written for R-SE-31, -37 or -38 (annotations and an order) or for F-SE-23 and F-SE-24.

## 1. What this lane read

**F** read in full to the end; **S** read in the sections named; **G** read by search, each hit opened in
context; anything not listed was not read.

| item | how | note |
|---|---|---|
| `AUDIT_BRIEF.md`; `CLAUDE.md`; `dossiers/07_SE.md` | F | |
| `audits/07_SE_audit.md` §0 to §14; the six `proposals/07_SE_*.md` | F | |
| `.designs/systems/settlements/reference/settlement_layer_v30.md` | F | all ten parts, 1,224 lines |
| `march_layer_v30.md`, `settlement_adjacency_v30.md`, `settlements_flow_skeleton_v1.md`, `settlements_currency_v1.md`, `governance_play_redesign_v1.md`, `lps_wiring_v1.md`, `settlement_generator_v1.md`, `generation_sourcebook_v1.md`, `valoria_political_hierarchy_v30.md`, `territory_temperaments_v30.md` | F | the flow skeleton traces `systems/settlements/sim/`, which is retired; read as history |
| `goldenfurt_slice/reference/` (README, sim build spec, generation methodology, verification findings, NPC cast, event deck) | F | |
| `.designs/systems/_architecture/reference/`: `campaign_modes_v30` and its infill, `campaign_architecture_v30`, `scale_transitions_v30` and its infill, `derived_stats_v30`, `complete_systems_reference`, `engine_atlas_v1` | F | the `_index` files are generated heading tables and were not opened |
| `research/game_precedent_suite/tables/R3a`, `R3b`, `R8`, `R9` | F | |
| `tables/R6`, `R2` | G | supply, upkeep, recruitment, garrison rows only |
| `research/fa_se_historical_precedent_research_v1.md` | S | T1, T2, T8; FA-1 to FA-4; the first lane read SE-2, SE-3 |
| `research/proactive_governance_scale_research_v1.md` | S | the four-scale framing, §2C (territory, nineteen rows), §3B |
| `research/historical/precedents_warfare.md` | S | §1.3a, §1.3b, §3.2, §8 (committed and cut) |
| `architecture/holonic_ARCHITECTURE.md` §43, §45, §46, §47 | F | |
| `.audit/2026-07-12-settlement-season-stress-sim/` | S | README, ground-truth odds, reconciliation in full; the synthesis by its headings and §6 |
| `.audit/2026-08-11-world-schema-gap-audit/` | S | the plan's head; `03_discussion` at P4 and the pass-C note; register rows G-04, G-12, G-32, G-33, G-37, G-48 in full |
| `audits/04_MB_audit.md` | S | §1.2, F-MB-08, F-MB-11, §5.6, §10, §11, §17, §18.1; its addendum's head |
| `audits/06_FA_audit.md` | S | F-FA-03, F-FA-04, §8, §10; its addendum's head |
| `proposals/01_CORE_capability_authoring_surface.md`, `02_CHAR_capability_uses_table.md` | F | |
| `audits/10_DICE_audit.md` §14 | F | |
| ledgers | G | ED-SE-0008, -0009, -0016, -0045, -0051, -0052, -0053; ED-IN-0047, -0255; BALANCE-005; `RULINGS.yaml` RR-2 |
| `proposals/2026-09-10-settlements-factions-populations/` | S | the index head; P2 in full |
| plan | S | the B10-16 card; the build text for CR-40, CP-T08-01, -02, -07; CR-08's entry |
| code | S | `modules/settlements/larder.py`, `provision.py`; `modules/mass_battle/troop_types/recruitment.py`; `loop/effects_army.py` (recruit to order); `effects_governance.py::_eff_requisition`; `seam/wrappers/mass_battle.py:286-351`; `world_q.py` (`larder_input`, `training_sites`, `raisable_by`, `march_origin`); `rosters.yaml` (`site_kinds`, the precedence note); `venues.yaml` (`planned_works`); the `transfer` row; H-212 |
| tests | names | every test name in eight settlement test files (131 tests); no body |
| cases | G | every `need:` line of all eleven case files by pattern; `proposals/2026-08-30-arc-reachability/04_SYNTHESIS.md` §1 to §3 |

`[SKIPPED: research/governance/ (three files, about 400 KB) and research/historical/precedents_analysis.md,
mass_battle_gauge_grounding.md — not opened; the first is the FA lane's ground and nothing here rests on it]`
`[SKIPPED: the rest of research/by_lane/SE_…md beyond what the first lane read — outline only]`
`[SKIPPED: the stress sim's _workings_joined.md and appendix_B — workings of retired mechanics]`
`[SKIPPED: test bodies; the case files' bodies beyond their need lines; arc-reachability files 01 to 03]`
`[SKIPPED: tutorials T03, T04, T10, T11 and D_T08_also — the tables they annotate were read instead]`

## 8. Evidence log

`PYTHONHASHSEED=0`, at `f83534e`, working tree; `git diff --stat 601e715 f83534e` over the code trees is
empty. Outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/SE_B/`. No `pytest`;
no `aperture`; no timing was read.

| # | command | seed · seasons | outcome |
|---|---|---|---|
| E-1 | `geo_probe.py` (parses `valoria_geography_v30.yaml`) | none | 17 provinces with `sub:` labels; 37 settlements with `type`, `stats`, no `port` or `sub_features` key; `settlement_adjacency` 55 edges (54 road, 1 sea); `adjacency` 26; `terrain_cost_matrix` 11 rows; `march_budget` 3 keys (`geo_probe.txt`) |
| E-2 | `realm_probe.py` (`build_realm(0)`, no season run) | 0 · 0 | 414 rungs, 83 persons, 322 Sites, 34 offices; cohort weights `{2: 37}`; ladders as quoted in F-SE-23; office rung kinds `{territory: 17, duchy: 10, realm: 4, settlement: 2, None: 1}`, the territory seats at T1, T9, T15 only; cohorts with `commit` 0; population 120, capacity 212, four settlements over; no training Site; `under_arms_cap` 60 at weight 2, 3,600 at 120; no army; stores 0; `content_hash 600d8b271474…` (`realm_probe.txt`) |
| E-3 | ledger lookups by id (a `python -c` over `registers/**/*.jsonl`) | none | the rows quoted in C-1 and F-SE-22 |
| E-4 | `grep -n controller_subordinate` over `engine modules systems tools` | none | one hit, the YAML line |
| E-5 | regex over the eleven case files for `need:` lines | none | 46 cases with a keyword need; §2.4 |
| E-6 | `git status --short` before return | none | see the receipt |

The two probe scripts are instruments of this addendum, a few dozen lines each, and write nothing.
Not re-run: any reading of the first audit (its code is this HEAD's code).

