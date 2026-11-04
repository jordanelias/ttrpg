# Strife flows: master design

## Status: PROPOSED (2026-11-04), HELD BACK IN FULL. Reference under CLAUDE.md §0.05, not a mechanism; merging this file ratifies nothing and applies no ED-1094 default. Nothing in it is built except the draft instrument of §8 step 1.
## Lane: IN

**What this is.** One current statement of the design, collated from a working session of 2026-11-04. It replaces the patched `00_DESIGN.md`. Source study: "Mechanics of Strife to c. 1600" (claude.ai artifact XDjCCRvbxiPS6sumpRtnte, read at its rev 769 for the mechanics tab and rev 69 for the dossiers). Code home: PR 553 (the draft instrument).

**What it adds to `engine/season/`**, if built: one pure query module (`queries/situation_q.py`), one count per code in `strife_moves.yaml`, one stamp in `questions_for`, later one term in `teller_weight`, one verb row (`execute`). No stored flow, no step, no clock.

**The plan.** The master workplan v10 is the one active plan for every lane (CLAUDE.md §2). This file is a design, not a plan: §8 names the positions the plan's owner would add and schedules none.

---

## 1. Aim and model, in one page

Every kind of strife in the study must be able to occur in the season loop, none of it triggered. Strife arises from events that happen in play (a tax raised, a drought and then famine, a succession crisis). Several can be open together, and people living through them do not parse them apart: the realm was turbulent, and eventually things happened. The design reads that.

- A **strand** is a narrative chain of strife moves around shared referents, with an opening, a course and a conclusion. The study's 102 cases are strands.
- The realm's one **flow** is an **era**: a confluence of the strands open beneath it, comorbid, tributaries into a river and a river into a funnel. Everything operating within an era is of the era.
- A flow's **rung is its stakes**. The higher the rung, the fewer flows a reading holds there. Overflow is subsumed into the flow above.
- A flow **concludes on a terminal move**, taken from the study's own endings. No timer retires it.
- People, offices and factions are **within** flows by where they sit on the rung ladder, aware of them or not. A flow conditions how they credit what they hear (the **regime**, an assemblage of institutions with commensurate modes of understanding and behaving) and what they attend to. It never fires an outcome.
- Top-down conditioning and bottom-up decision stand in tension. It is accepted, and guarded by a measurement (§6).

## 2. The study, by category

The study codes 102 cases into 40 moves (plus NOTE and OTH) and 16 links that recur in at least 6 cases and beat shuffled order; 74 cases leave and rejoin those links, 93 end off them, and the mean case spends about a quarter of its moves on them. The study finds the categories alike between opening and ending; only A (natural shock) and B (ruler dies, regime change, claim) have distinctive moves, and those are what the labels name. The categories differ in occasion, carrier and ending. The study labels the military and persecution cases HI-1 to HI-7 and HI-8 to HI-11.

| | category (cases) | occasion and carrier | how they end | what the loop must be able to do |
|---|---|---|---|---|
| A | Subsistence and environment (8) | a shock (plague, eruption, flood, drought, earthquake) or a ration or wage dispute; workers, a sect, country people, soldiers, bound people | rations arrive or the shortage eases, unpunished; a new dynasty; bands broken; removal of the rebels; a reform annulled, then war; a law meeting no rising | a shock on matter and bodies; mobilization; spread |
| B | Succession and dynastic (12) | double elections with papal sanction, brothers or sons after a death or capture, a regency joined to a city rising, houses over an heir, usurpers, annexation | a claimant killed and the other recognized; a shared title; deposition and re-election; the rival's surrender; annexation; withdrawal with no winner | ruler dies; successor; claim and deposition; outside recognition; regime change |
| C | Fiscal, monetary, debt (20) | four kinds: subject states leaving a league; soldiers' pay and service protests; debt risings and reform; long wars | surrender or a penalty on the place; concession; a new dynasty; independence; a court that lost control | a new burden; concession; debt relief; penalty on place |
| D | Governance, privilege, constitution (12) | elite houses (7), town risings, circus factions with a claimant, soldiers and plebs | defeat with executions; submission and imprisonment; a written grant or settlement; regime change | petition; grant, revocation and settlement; rival government |
| E | Foreign rule, conquest, territory (13) | subject peoples against an empire; an invasion; one foreign king replacing another; peasants against nobles | the authority wins (most); challengers hold or gain control (E-1, E-5, E-12); withdrawal (E-10) | outside powers; subject polities; penalty on place |
| F | Religion, doctrine, identity (11) | religious carriers (7), elite houses | a settlement with the authority holding; leaders executed after defeat; leaders dead; surrender; penalties without a battle | religious sanction; settlement and revocation; execution |
| G | Social order, servitude, status (15) | slaves (4), peasants (4), towns and guilds (3), citizens and allies (2) | main force defeated and leaders executed (8); gains partly kept; gains reversed; a leader killed | servile wars (rising, mobilization, rising wins); city regimes; laws |
| H | Military mutiny, unpaid armies (7) | soldiers; exhaustion and discharge (4), pay owed (3) | three stayed inside the army (turned back, reconciled, ringleaders executed); four widened (ruler deposed and killed, Carthage won, the Company took Athens, sacks then a pacification) | army, pay, refusal, concession |
| I | Persecution, civic purity (4) | a ruling power imposes a burden on a subject people, or a contest inside a city republic over moral and church discipline | the authority wins; a leader executed; a parley | a burden imposed; religious sanction; refusal |

## 3. Rulings ledger

Jordan, 2026-11-04, in conversation. These are rulings in that conversation, not ledger rows; each names where this file applies it.

| | ruling | applied in |
|---|---|---|
| R1 | Outcomes must all be possible. Nothing is triggered. | §7 |
| R2 | Flows condition how people behave. They arise from events that happen in play, and all of them must be possible. | §4, §8 |
| R3 | Too many live strifes are illegible, so everything can happen but new events fold into existing flows. The precedent cases, with their deviations and shared primitives, show the flows are mutable. | §4 |
| R4 | A rung is the stakes of a flow. The realm holds one flow, which conditions every flow beneath it; a duchy a tributary and an isolate. | §4 |
| R5 | Capacities below the duchy: "n+1". | §4 |
| R6 | A flow has no quiet seasons. It terminates or resolves with a concluding outcome, or it is not a flow. The artifact tells the concluding outcomes; use those. | §4 |
| R7 | Define "executed". | §9 |
| R8 | People exist within flows, as in Foucault's regime of truth. | §5 |
| R9 | Awareness is not required to be within a flow. | §5 |
| R10 | The tension between top-down conditioning and bottom-up awareness and decision is acceptable: flows condition the rungs into legible narratives with subplots without determining outcomes. | §6 |
| R11 | Simultaneous crises are one era in lived terms; narrative chains within it sit at lower levels, since specifics are the opposite of a universal. Everything operating within an era is of the era. | §4 |
| R12 | Flows condition factions at their relevant scale, and offices, as well as persons. | §5 |
| R13 | A regime in Foucault's sense is an assemblage of institutions with commensurate dominant modes of understanding and behaving, not a political regime. | §5 |

## 4. Flows: strands, eras, stakes, capacity, conclusion

**Reading a flow.** A **move** is a ledger claim whose Event kind and causing act classify to one of the 40 codes in `strife_moves.yaml` (to be made side-aware: verb, degree, and the actor's faction against the holder of the rung). Non-strife claims never join a strand; they are still of the era beneath whose rung they fall. A **strand** is a maximal set of moves linked by shared referents, compared through the rung ladder (`ancestry`, `place_of`, `holder_faction_of`): the same referent, or one an ancestor of the other, or a shared faction. It is read at the lowest rung covering its moves, so it zooms: a hearth's grain dispute is a hearth strand; across a settlement it is read at the settlement; across territories, at the duchy. Membership never requires the 16 links, or a detour would end a strand. Its **opening kind** is the category of its oldest move.

**Organic openings.** Each opening is read off state the loop already holds; nothing fires on it.

| opening, as it arises | read from | exists today |
|---|---|---|
| tax or levy raised (C) | `dispensation.issued`, `requisition.taken`, `duty.taken` | yes: 401 events over seeds 0 and 1 at 4 seasons |
| shortage, then famine (A) | a settlement's hunger band; a yield below its floor | hunger is read (`hunger_by_settlement`); whether it binds rests on CR-22 (B10-18; status not checked); the shock behind it is dark (`season_factor_draw` ships `()`) |
| succession crisis (B) | a seat emptied by `person.died`, then `succeed` or a rival claim | deaths occur (15 over seeds 0 and 1); no natural death (`age_step`, `illness_rate` are 0.0); rival claims 0 observed, cause not yet found |
| army unpaid (H) | a levy that does not reach its troops | source not yet located |
| burden on a subject people, foreign rule, religious or status grievance (D, E, F, G, I) | the same moves, opened by a foreign actor or a church or caste seat | foreign off; no church seat issues sanctions |

**Era and strand.** A succession crisis, a foreign invasion, a famine and a tax crisis can all be open at once. The realm's one flow is an **era**: a *confluence* whose opening kind is the set of categories open beneath it. A strand is always at a lower rung than the era it feeds. The era is read generally (the crown, the realm's seats); strands carry the particulars. **Everything operating within an era is of the era.** Membership of an era is by scope: every act, claim and institution beneath the realm's rung, strife or not, is of it. A merchant's trade, a marriage and a harvest in a famine-and-war era are conditioned by its regime as a raid is. The era's *moves*, which rank and conclude it, are strife moves; its *conditioning* reaches everything beneath it (§5).

**Stakes and capacity.** A succession crisis at a territory is small; at a duchy larger; at the realm the largest. The realm holds 1 flow; a duchy 2 (a *tributary* strand that drains into the era and an *isolate* that does not). Below the duchy "n+1": each rung holds one more than the rung above. By the order of the existing `rung_kinds` roster (`person, hearth, community, settlement, territory, province, duchy, realm`) read from the top: realm 1, duchy 2, province 3, territory 4, settlement 5, community 6, hearth 7, person 8. Capacity is a function of position in a roster that exists, not a second table. No slots are typed below the duchy. The built realm has no province rung (census), so 3 binds nothing yet. Capacity limits what a *reading* holds at a rung, never an event. `[A1]`

**Which flow takes a scarce slot.** The one whose moves reach the most distinct rungs below, then the most recent; ties by claim order. `[A2]`

**Overflow is subsumed, not dropped.** A flow with no slot at its rung is read as part of the flow at the nearest ancestor rung that has one. At the realm a second realm-wide event is read inside the era. At a duchy a strand sharing referents with the era takes the tributary slot, one that does not takes the isolate slot, and a third folds into the era. Nothing is deleted; the moves stay in ledgers.

**Conclusion.** No timer retires a flow. A strand concludes on a terminal move; an era concludes when every strand draining into it has concluded. The terminal moves are the study's own: the last substantive move (NOTE and OTH set aside) of each of its 102 cases, which I read from the nine case-mapping tables and tallied by script. The study does not state them. `[A3]`

| ends the most cases | cases |
|---|---|
| XP trouble persists | 20 |
| PC penalty on place | 12 |
| CO concession | 10 |
| WA authority wins | 7 |
| XE leader executed (rebel side 5) | 5 |
| RV grant revoked | 5 |
| KL leader killed (rebel side 4, other 1) | 5 |
| XN regime or border | 4 |
| XS settlement | 4 |
| IM new burden | 4 |

Fifteen further base codes end fewer: OW, IN, SB, PU (3 each); FA, NG, FR (2 each); DN, CL, CP, RF, WN, PT, CA, XA (1 each). Twenty-five base codes end at least one case. The other fifteen never do and cannot conclude a strand: SH, DR, BR, MO, OP, RU, VI, SZ, RG, SP, CH, WR, RT, DA, AM. `strife_moves.yaml` is to carry each code's count, so a code ending a single case reads as a single case.

**XP is not a move the loop produces.** It is the study's mark that later risings are linked to the case. In the loop a strand concludes by persistence when a new strand opens on its referents, and that opening is the event. **A terminal move is not always final in the study:** F-2 holds seven settlements and B-4 follows a settlement with a refusal, a capture and a further settlement. Two rules are candidates: (a) the first terminal move closes the strand, and later conflict on its referents is a new strand; (b) a strand is concluded while its latest move is terminal and reopens if a conflict move follows. They are chosen by measurement: replay the study's 102 coded paths through each and keep the rule that draws one strand per case most often (§8 step 1).

A person's reading of a strand is open until a claim of a terminal move lands in his ledger. Someone who has not heard the war is over still believes it on and acts on that belief (AX-7). What binds him by where he lives is the world reading's, and ends when the flow does. A witness and a person who was only told hold different claims and read different flows from the same events. That is deliberate.

## 5. People, offices and factions within flows

**Two readings.** The **world reading** `flows_in(log)` is a pure function of the whole Event log. The harness reads it, and the engine reads it as data when it grades what a person credits; it is never deposited in anyone's ledger as a claim and never read by a chooser. The **person reading** `flows_known(w, p)` is a pure function of `p.ledger` alone; `questions_for` reads it, so it shapes `p`'s choices (AX-7: a character has a reading of the world, never the world).

**Within and aware.**

| relation | what makes it so | what it does |
|---|---|---|
| **within** | structural: the flow's rung is the entity's own rung or an ancestor of it | the regime bears on the entity whether or not it has any concept of the flow: what happens to it is a move of the flow, and what it credits is graded by the regime |
| **aware** | epistemic: the ledger holds the flow's moves | the person can place events in it and act on its referents |

Awareness is not required to be within a flow; requiring it would put a person outside the events he is living through. Someone who has never heard of a pandemic still falls ill and finds the market closed. A hearth-dweller who has heard nothing of the war reaches it by two routes, neither handing him the flow as a fact: **lived events** (stores requisitioned, hunger, a neighbour dead, and the acts and words of those who are aware) and **grading** (the engine grades what he credits by the regime he is within). Neither deposits a claim in his ledger.

**Persons, offices and factions** sit on the ladder already.

| entity | its rung | precedent |
|---|---|---|
| person | `home_of`, with the ladder above it | `world_q.reach`, limbs 1 to 3 |
| office | `Office.rung`; its purview is that rung and its descendants | `reach` limb 4; `faction_q.purview` |
| faction | the rungs it holds (`faction_q.holdings`, `holder_faction_of`), and its relations (`at_war`) | `queries/faction_q.py` |

*Within* is one structural test for all three (for a faction, of any rung it holds). Only a person acts (AX-1), so offices and factions are conditioned through the persons who act for them. **Offices** condition their holder in his capacity: his `reach` already admits claims about his purview, and the seat's remit decides which verbs answer (a mayor's `requisition`, a duke's `march`). **Factions** are conditioned through their heads and seat-holders; a faction belongs to a regime through its creed and the institutions it is linked to, and its *side* in a strand (authority, challengers, outside power: the study's A, R, O) is a separate fact that classifies moves and does not grade credit. Flows never write a faction's goal rows; they change what a leader attends to, not what the organisation wants. **Scale** is the rung: a guild's strand at a settlement and the Crown's era at the realm are one relation at two rungs.

**The regime.** In Foucault's account a society holds a regime of truth: the discourse it accepts and makes function as true, the means of telling true from false, how each is sanctioned, the techniques valued for obtaining truth, and the standing of those charged with saying what counts. It is produced by relations of power, not laid over them. **It is not a political regime.** Jordan's definition (R13): an assemblage of institutions with commensurate dominant modes of understanding the world and behaving. In the engine's terms:

| part of the definition | where the engine has it |
|---|---|
| institutions | offices, factions, venues and arrangements |
| a mode of understanding | the affiliations a person holds and how intensely (`Person.conviction`); a faction's creed, committed to by its leader |
| a mode of behaving | what an affiliation engages or condemns (`affiliation_engagement`: the acts that scar an observer holding it) and the remit a seat holds |
| commensurate | not `incompatible` in the strain matrix (`true` strains, `false` is compatible, `null` has no source and is read as not incompatible) |

Operationally: two institutions are linked where they share a holder, a conferral or remit grant, a bond (`tie`, `knot`) or a venue; a **regime** is a set of linked institutions whose dominant affiliations (the one most held among their holders, by intensity) are pairwise not incompatible. Five affiliations are rostered, so a handful of regimes at most. `[A4]` A regime is not a side: the authority and the challengers may share one, and two regimes may stand in a realm without strife. Strife between regimes is where their affiliations strain; strife inside one is a contest over what its own terms require. The instrument can report, for each strand, whether its parties stand in one regime or two. `[A5]`

**The era is a regime's unity.** "The realm was turbulent" is how the regime makes simultaneous crises one. That unity is a reading produced within the regime (what is named, what is said to have caused it, who is entitled to say), so persons, offices and factions can hold different accounts of one era and the engine holds none as the true one.

**The mechanism exists, dark.** `decision/options.py::teller_weight` grades a told claim when it is read, by the hearer's relation to the teller (rank, regard, track record) and the retelling count; at its shipped control values every claim weighs 1.0. The parts of a regime map onto it:

| part of a regime | where it already stands |
|---|---|
| what is accepted as true | `weigh`: how far a hearer credits a claim; the noisy-OR over distinct origins |
| telling true from false | the inquiry verbs (`examine`, `interview`, `interrogate`, `research`) and `confidence.broken` |
| standing of those who pronounce | `rank(p, teller)`; the seat a speaker acts through |
| what is valued | the verbs a seat can form and the remits it holds |

The **credit term** is one addition to `relation`: whether the teller stands in the regime the hearer stands in, or one commensurate with it (credited more), or an incommensurate one (credited less). It reads the world reading, so it binds an unaware hearer as it binds an aware one. It is a **second step**, for three reasons: it reorders every told claim and so moves the hash widely; its effect cannot be told from the stamp's until the stamp is measured alone; and AX-2 binds `decision/`, so the regime must arrive there as data (as `fx` and the stamped questions do), never as a read of the World. `layer-conformance` Lens B settles that placement before any code.

**The stamp.** `questions_for` already stamps standing occasions onto a person's first question as classed referents (vacancies, writs held, places named, larders in purview; `_stamped`). `flows_known` adds one: the rungs, persons and offices at stake in each held flow, as referents of the existing closed classes (`Office, Record, Rung, Site, Proposition, Person`). No `Flow` class. A person aware of a rising at his settlement finds that rung and its holder among his occasions, ordered by `attention_key`, so verbs form on them (`march`, `petition`, `migrate`, `arrest`, `commit`) and each is chosen by his own convictions. Two people in one flow choose differently; none is told what the flow does next. The flow's opening kind and last move are not read by any chooser in this design.

## 6. The accepted tension, and what refuses it

Top-down, universal conditioning at the level of narrative, against bottom-up, granular awareness and decision by characters. Accepted (R10). Where each acts:

| top-down (the flow) | bottom-up (the person) |
|---|---|
| which events are read as one chain, at which rung, and how many a reading holds | what a person witnessed, was told and believes |
| how a person's told claims are graded, by the regime he is within | which verb he forms and chooses, by his own convictions and ambitions |
| which referents appear among his occasions | what he does with them |
| nothing else | everything else, including every terminal outcome |

The flow writes no state, names no next move and fires nothing. It could harden into a determinant through a loop: flows condition choices, choices make the moves that define the flows, and the realm's single slot makes the loop tightest at the top. **The guard is measured:** with the conditioning on, every terminal code reachable with it off must stay reachable, and the number of distinct terminal codes reached across seeds must not fall. A conditioning arm that closes a route or narrows the spread is a defect to remove.

**Refused, to stay inside ratified rulings:**
- No stored flow, state, phase or counter (T-a; ED-IN-0225: no arc carrier). Recomputed from the log and ledgers each time. `[A6]`
- No date, deadline, firing condition or outcome on anything (T-c, M16(b)). A flow has no next move. A terminus is recognized when persons' acts produce it; nothing authors it and nothing makes it happen.
- No self-worsening condition (M16's fourth motion, ED-IN-0301). Drought is weather on matter, famine is bodies, the rest is persons acting.
- No backbone required for membership.

## 7. Reachability: what must exist so every opening and every conclusion is possible

From the draft instrument's first run (4 seasons, seeds 0 and 1; kind-only grading, so upper bounds): 26 codes had matching events, 10 were declared with none (RF, RG, CL, NG, WA, WR, DA, CA, AM, XN), 4 have no producer (SH, CH, XE, XP). The DARK grade never fired because shared kinds mask it (`march.declared` reads OW and XA as observed although `foreign=False`).

| gap | closes through |
|---|---|
| natural shock (SH) | CL-EVENTS commit (2), the live weather arm; CP-T10-02 calamity bands |
| natural death (DR, DN) | `age_step`, `illness_rate` set by Jordan (CP-T10-05) |
| outside war and power (OW, XA) | the `foreign` switch (IN-36) |
| church sanction (CH) | a church seat issuing ban or detain tenures: data, and the seat |
| execution of a held person (XE) | §9: a verb row `execute`, taken by precedent |
| declared, none seen (RF, RG, CL, NG, WA, WR, DA, CA, AM, XN) | the aperture funnel per verb first (which clause refuses it); change nothing before that |
| a later rising linked to a case (XP) | read by `flows_known` (§4); no verb |
| **a conclusion from every opening** | for each opening kind and each of the 25 terminal base codes, an act route exists whose last move is that code. Where none does, the flow can never conclude and holds its slot for good, the realm's single slot being the worst case. A requirement of the loop, checked by the instrument |

## 8. Build order

Batches, with what each depends on, what it moves, and its test. A position in the master workplan is needed for each; this file names them and schedules none.

| | batch | depends on | hash | builder tier (CLAUDE.md §10) | falsifier and control |
|---|---|---|---|---|---|
| B1 | **Instrument, side-aware.** Classify by act (verb, degree, actor's faction against the rung's holder). Add the 16 links, the leave-and-rejoin profile, the per-code count of cases ending on it, and the one-regime-or-two report. Classify `person.died` by its causing act: `execute` is XE, a felling `fight` or `march` is KL, no act is DN; DR and the study's second code are a role the death plays in a strand, not another event. Transcribe the 102 coded paths as a fixture with provenance. Replay them through §4's two strand rules. | draft in PR 553 | none | sonnet build, opus critic | shuffled-within-case log must complete the links no more often than chance; a planted log completing a known link must read as completing it; the conclusion check below |
| B2 | **Gaps of §7**, one lane each, in parallel worktrees: SH, bodies, foreign, church seat, `execute`, and the funnel for the ten declared-but-unseen codes | independent of each other; the funnel needs B1's side-aware count | each a declared mover; `execute` too | sonnet per lane, opus on the `execute` row | per lane, a code moves from 0 to observed over several seeds without the controls (`confer`, `oblige` counts of CR-49) falling to 0 |
| B3 | **`flows_known`**, a pure query with no consumer | B1 | none | opus (judgment on the linking rule) | a witness and a hearsay holder of the same events read different flows; an empty ledger reads none; two realm-wide flows read as one with the second inside it; a terminal claim added frees the realm slot, missing it leaves it open; a person within the realm flow whose ledger holds none of its moves reads no realm flow, yet the world reading lists him as within |
| B4 | **The stamp** in `questions_for`, switch shipped off | B3 | off equals the base hash; on is a declared mover | opus | the stamp changes which verbs form for a person in a held flow; the §6 guard over the same seeds |
| B5 | **The credit term** in `teller_weight` | B4 measured; Lens B placement | declared mover | opus | credit differs for a commensurate and an incommensurate teller at fixed claims; the §6 guard |
| B6 | **Deck**: world-build seeds per category through the CL-EVENTS commit (3) schema (goal rows or yield scales, drawn once at build) | B1; CL-EVENTS (3) and (4) in B10-18 | equal while shipped off | sonnet for rows, opus for the schema widening | measured by B1's reachability report per category |

**Conclusion check (B1).** For each opening kind, run seeds forward and report which terminal codes any strand reached. A code never reached over several seeds is a finding about default play, not proof of absence; the same run at more seeds is its control.

**Critical path:** B1, B3, B4, B5. B2 runs beside B1. B6 follows B1 and B10-18's CL-EVENTS commits. B1 and B2 are the only batches that change what the loop can do before any conditioning exists.

## 9. Executed (XE), defined

The study's code is "leader executed; side is the side of the person executed". Its uses: a captured rebel leader put to death by the authority (Ball, Kett, Dózsa, Cade, Egmont and Horn, Aske), a captured authority figure put to death by the challengers (the five XE-A), a rebel leader put to death by another rebel (Bato), and a purge inside the challengers' own side (Želivský, beheaded by the Hussite council of Prague). The robust link is capture then execution (19 of 35 cases). What these share: **a person in custody is put to death by the deliberate act of those holding him, as sentence or order.** The side is the dead person's.

It is not the neighbouring moves. *Killed* (KL) is a death outside custody: in battle, by assassination, by a crowd (Artevelde), by one's own followers. *Died* (DN) is a death with no act of another. *Punished* (PU) is repression short of death.

**In the engine:** a death is an execution when the act that caused it (found by `causes*` into the act store, as `attribution.actor_of` does) is an `execute` act, by a person acting through a seat, on a person who held a live `detain` tenure when it resolved. Any seat with the remit can do it, a rival government's included, so both XE-R and XE-A are producible. A mass execution is one act per person.

**The verb:** a new row `execute`, on the shape of `interrogate` (eligibility `remit:determine`, referent class `Detainee`, the subject held in a live `detain`) and `pardon` (`remit:determine`, the subject a person over whom the seat sits as a bench). The pair is deliberate: `pardon` ends the detention, `execute` ends the life. It writes the same death path as a felled combatant (`person.died`, the dead person's seats closed per CP-T02-01). A hash mover, built through its own position, not here. Taken by precedent and by what the architecture allows (CLAUDE.md §0, steps 4 and 5), not put to Jordan. `[A7]`

## 10. Assumptions register and what Jordan still owes

Each assumption carries a revert. All are `[ASSUMPTION; medium; Jordan to correct]`.

| | assumption | revert |
|---|---|---|
| A1 | "n+1" means each rung holds one more than the rung above; capacity is read from the order of `rung_kinds`; no typed slots below the duchy | delete the rule and §4's fold |
| A2 | The slot-ranking rule: reach, then recency, then claim order | any other ordering of the same kind |
| A3 | The 102 final moves in §4, transcribed by me from the case-mapping tables; `[UNVERIFIED]` until cross-checked against the study | rebuild the fixture from the study |
| A4 | The operational reading of a regime (linked institutions, dominant affiliation, pairwise not incompatible) | delete that paragraph and the credit term |
| A5 | The contrast between strife inside a regime (a charter quarrel, category D) and between regimes (doctrine, category F) is a reading of the categories, not a finding | drop the sentence; the instrument reports one regime or two per strand without it |
| A6 | A derived per-person and per-world reading is outside the refusals of T-a, ED-IN-0225 and M16's fourth motion, because it stores nothing and acts only through persons | the plan's owner rules otherwise and the design is withdrawn |
| A7 | `execute` as a new verb row on `interrogate`'s and `pardon`'s shape | delete the row |
| A8 | `strife_moves.yaml` readings: each verb and kind is a reading of `verb_table.yaml` by name, not an execution | delete the file, `data/strife.py` and `harness/strife.py` |

**Needs Jordan.** One item: whether the credit term (B5) is a second step as proposed, or part of the first build. Taken by precedent or from the study, with reasons above: capacities, terminal moves, execution.
