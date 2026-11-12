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

