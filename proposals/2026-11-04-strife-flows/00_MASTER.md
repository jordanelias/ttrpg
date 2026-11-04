# Strife flows: master design

## Status: PROPOSED (2026-11-04), HELD BACK IN FULL. Reference under CLAUDE.md §0.05, not a mechanism; merging this file ratifies nothing and applies no ED-1094 default. Nothing in it is built except the draft instrument of §8 S1.
## Lane: IN

**What this is.** One current statement of the design, collated from a working session of 2026-11-04 and revised once after two independent critiques (an opus critic and a Fable 5.1 critic at high effort). It replaces the patched `00_DESIGN.md`. Source study: "Mechanics of Strife to c. 1600" (claude.ai artifact XDjCCRvbxiPS6sumpRtnte, read at its rev 769 for the mechanics tab and rev 69 for the dossiers). Code home: PR 553 (the draft instrument).

**What it adds to `engine/season/`**, if built: one World-first query module (`queries/situation_q.py`), one count per code in `strife_moves.yaml`, one stamp in `questions_for`, one verb row (`execute`). No stored flow, no step, no clock. A term grading what a person credits is **not** part of the design: it has no lawful landing under the ratified axioms and is held for a ruling (§5, §10).

**The plan.** The master workplan v10 is the one active plan for every lane (CLAUDE.md §2). This file is a design, not a plan: §8 names batches for the plan's owner to turn into positions and schedules none.

---

## 1. Aim and model, in one page

Every kind of strife in the study must be able to occur in the season loop, none of it triggered. Strife arises from events that happen in play (a tax raised, a drought and then famine, a succession crisis). Several can be open together, and people living through them do not parse them apart: the realm was turbulent, and eventually things happened.

- A **strand** is a narrative chain of strife moves around shared referents, with an opening, a course and a conclusion. The study's 102 cases are strands.
- The realm's one flow is an **era**: the strife in the realm taken as a whole, into which the strands beneath it drain, comorbid, tributaries into a river and the river into a funnel. Everything operating within an open era is of the era.
- A flow's **rung is its stakes**. The higher the rung, the fewer flows a reading holds there. A flow beyond a rung's capacity is grouped under the flow above it in the reading.
- A flow **concludes on a terminal move**, taken from the study's own endings. No timer retires it.
- People, offices and factions are **within** flows by where they sit on the rung ladder, aware of them or not. What happens to them, and what they attend to, is shaped by the flow; the flow never fires an outcome. Whether it may also shape what they credit is **blocked** (§5) and is Jordan's.
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
| R1 | Outcomes must all be possible. Nothing is triggered. | §6 |
| R2 | Flows condition how people behave. They arise from events that happen in play, and all of them must be possible. | §4, §8 |
| R3 | Too many live strifes are illegible, so everything can happen but new events fold into existing flows. The precedent cases, with their deviations and shared primitives, show the flows are mutable. | §4 |
| R4 | A rung is the stakes of a flow. The realm holds one flow, which conditions every flow beneath it; a duchy a tributary and an isolate. | §4 |
| R5 | Capacities below the duchy: "n+1". | §4 |
| R6 | A flow has no quiet seasons. It terminates or resolves with a concluding outcome, or it is not a flow. The artifact tells the concluding outcomes; use those. | §4 |
| R7 | Define "executed". | §9 |
| R8 | People exist within flows, as in Foucault's regime of truth. | §5 |
| R9 | Awareness is not required to be within a flow. | §5 (lived events and attention; grading blocked, §10) |
| R10 | The tension between top-down conditioning and bottom-up awareness and decision is acceptable: flows condition the rungs into legible narratives with subplots without determining outcomes. | §6 |
| R11 | Simultaneous crises are one era in lived terms; narrative chains within it sit at lower levels, since specifics are the opposite of a universal. Everything operating within an era is of the era. | §4 |
| R12 | Flows condition factions at their relevant scale, and offices, as well as persons. | §5 |
| R13 | A regime in Foucault's sense is an assemblage of institutions with commensurate dominant modes of understanding and behaving, not a political regime. | §5 |

## 4. Flows: strands, eras, stakes, capacity, conclusion

**Reading a flow.** A **move** is a ledger claim whose Event kind classifies to one of the 40 codes in `strife_moves.yaml`. A claim carries its kind, subject and, for the holder's own deeds, a `doer`; it carries no verb, degree or actor's faction. So the **person reading is kind-level**, and the study's side-split pairs (WA/WR, XE/KL) are told apart only by the **world reading**, which can follow `causes[]` into the act store. Non-strife claims never join a strand; while an era is open they are still of it.

**Linking.** Two moves link when (i) they share a referent, (ii) one's referent is the parent or child of the other's, one rung step apart, or (iii) the same person did both. Linking never passes through the realm rung (the realm is the era's scope, not a referent that joins strands) and never reads who holds a rung, so a seizure does not re-link the past. A **strand** is a connected component under these links, read at the lowest rung covering its moves, so it zooms: a hearth's grain dispute is a hearth strand; across a settlement it is read at the settlement; across territories, at the duchy. Membership never requires the 16 links, or a detour would end a strand. Its **opening kind** is the category of its oldest move. `[A9]`

**Organic openings.** Each is read off state the loop already holds; nothing fires on it.

| opening, as it arises | read from | exists today |
|---|---|---|
| tax or levy raised (C) | `dispensation.issued`, `requisition.taken`, `duty.taken` | yes: 401 events over seeds 0 and 1 at 4 seasons |
| shortage, then famine (A) | a settlement's hunger band; a yield below its floor | hunger is read (`hunger_by_settlement`); whether it binds rests on CR-22 (B10-18; status not checked); the shock behind it is dark (`season_factor_draw` ships `()`) |
| succession crisis (B) | a seat emptied by `person.died`, then `succeed` or a rival claim | deaths occur (15 over seeds 0 and 1); no natural death (`age_step`, `illness_rate` are 0.0); rival claims 0 observed, cause not yet found |
| army unpaid (H) | a levy that does not reach its troops | source not yet located |
| burden on a subject people, foreign rule, religious or status grievance (D, E, F, G, I) | the same moves, opened by a foreign actor or a church or caste seat | foreign off; no church seat issues sanctions |

**The era.** The era is a **scope**, not a connected component. It opens at the first strife move in the realm and holds the realm's one slot. Its moves are the strife moves at the realm rung and the strands beneath; its opening kind is the set of categories open beneath it. A succession crisis, a foreign invasion, a famine and a tax crisis can all be open at once and are read as one era. A strand is always at a lower rung than the era it feeds. The era is read generally (the crown, the realm's seats); strands carry the particulars. **Everything operating within an open era is of the era**: every act, claim and institution beneath the realm's rung, strife or not (a merchant's trade, a marriage, a harvest), is conditioned by it as a raid is. After the era concludes nothing is of an era until a new one opens.

**Stakes and capacity.** A succession crisis at a territory is small; at a duchy larger; at the realm the largest. The realm holds 1 flow; a duchy 2 (a *tributary* strand that drains into the era and an *isolate* that does not). Below the duchy "n+1": each rung holds one more than the rung above. By the order of the existing `rung_kinds` roster (`person, hearth, community, settlement, territory, province, duchy, realm`) read from the top: realm 1, duchy 2, province 3, territory 4, settlement 5, community 6, hearth 7, person 8. Capacity is a function of position in a roster that exists, not a second table. No slots are typed below the duchy. The built realm has no province rung (census), so 3 binds nothing yet. A person's ladder sums to 33 such slots, but he holds only what his ledger holds, so the cap binds chiefly the world reading and the instrument. `[A1]`

**Identity and presentation are different things.** A strand's **rung** is its identity: the lowest rung covering its moves, fixed by §4's linking. **Capacity** governs only how a reading *presents* strands at a rung. A strand with no slot at its rung is grouped under the flow at the nearest ancestor rung that has one; its rung does not change and its moves are not deleted. At the realm a second realm-wide event while an era is open joins the era. At a duchy a strand sharing referents with the era takes the tributary slot, one that does not takes the isolate slot, and a third is grouped under the era.

**Which flow takes a scarce slot.** The one whose moves reach the most distinct rungs below; then the one with the most moves; then the most recent; ties by claim order. (At hearth and person the first criterion is zero, so those rungs rank on the next.) `[A2]`

**Conclusion.** No timer retires a flow. A strand concludes on a terminal move when **no open referent remains** on it: no live restraint (`detain`, `ban`) among its parties, no `at_war` between its parties, no docketed matter on its referents. These are engine-side predicates, so no historian is asked to say when it ended. A strand cannot conclude on its own opening move. The **era** concludes on a terminal move at the realm rung under the same open-referent test; its slot then frees, and the strands beneath carry on as their own flows. A realm-wide event after that opens a new era.

The terminal moves are the study's own: the last substantive move (NOTE and OTH set aside) of each of its 102 cases, which I read from the nine case-mapping tables and tallied by script. The study does not state them. `[A3]`

| ends the most cases | cases |
|---|---|
| XP trouble persists | 20 (not terminal here; see below) |
| PC penalty on place | 12 |
| CO concession | 10 |
| WA authority wins | 7 |
| XE leader executed (rebel side 5) | 5 |
| RV grant revoked | 5 |
| KL leader killed (rebel side 4, other 1) | 5 |
| XN regime or border | 4 |
| XS settlement | 4 |
| IM new burden | 4 |

Fifteen further base codes end fewer: OW, IN, SB, PU (3 each); FA, NG, FR (2 each); DN, CL, CP, RF, WN, PT, CA, XA (1 each). Twenty-five base codes end at least one case. **XP is not terminal in the loop.** It is the study's mark that later risings are linked to the case, which is a historian's boundary and the absence of an ending; in the loop it is the opening of a successor strand on the referents of a concluded one, read and not produced. So **24 base codes can conclude a strand**; the other sixteen cannot (the fifteen that end no case, SH, DR, BR, MO, OP, RU, VI, SZ, RG, SP, CH, WR, RT, DA, AM, and XP). `strife_moves.yaml` is to carry each code's count, so a code ending a single case reads as a single case.

**A terminal move is not always final in the study:** F-2 holds seven settlements and B-4 follows a settlement with a refusal, a capture and a further settlement. Two rules are candidates: (a) the first terminal move closes the strand, and later conflict on its referents is a new strand; (b) a strand is concluded while its latest move is terminal and the open-referent test holds, and reopens if a conflict move follows. **(b) is the working rule**, because it needs no historian's cut and does not fragment a case. `[A10]` The study's coded paths carry codes and no referents, so they cannot test linking and cannot choose between (a) and (b); replaying them reports how many strands each rule draws per case, as a description only.

A person's reading of a strand is open until a claim of a terminal move lands in his ledger. Someone who has not heard the war is over still believes it on and acts on that belief (AX-7). What binds him by where he lives is the world reading's, and ends when the flow does. A witness and a person who was only told hold different claims and read different flows from the same events. That is deliberate. A person's account of an era is the strands he holds together with the realm-rung moves he knows; no era object exists in his reading.

## 5. People, offices and factions within flows

**Two readings.** Both are World-first queries, read-only and recomputable (`04` §A.2: `queries/` owns nothing, no token). The **world reading** `flows_in(w)` reads the Event log, the act store and the containment tree; the harness and the instrument read it, and **no step of the loop and no decision-side function reads it**. The **person reading** `flows_known(w, p)` reads `p.ledger` and the containment tree; `questions_for` reads it, so it shapes `p`'s choices. AX-7: a character has a reading of the world, never the world.

**Within and aware.**

| relation | what makes it so | what it does |
|---|---|---|
| **within** | structural: the flow's rung is the entity's own rung or an ancestor of it | what happens to the entity is a move of the flow: matter and bodies reach it, and so do the acts and words of those who are aware |
| **aware** | epistemic: the ledger holds the flow's moves | the person can place events in it and act on its referents (the stamp, below) |

Awareness is not required to be within a flow; requiring it would put a person outside the events he is living through. Someone who has never heard of a pandemic still falls ill and finds the market closed. A hearth-dweller who has heard nothing of the war is conditioned by **lived events** alone: stores requisitioned, hunger, a neighbour dead, and what the aware say and do to him. Nothing is deposited in his ledger by the flow; AX-7 holds.

**Persons, offices and factions** sit on the ladder already.

| entity | its rung | precedent |
|---|---|---|
| person | `home_of`, with the ladder above it | `world_q.reach`, limbs 1 to 3 |
| office | `Office.rung`; its purview is that rung and its descendants | `reach` limb 4; `faction_q.purview` |
| faction | the rungs any of its members hold (`faction_q.holdings`), and its relations (`at_war`) | `queries/faction_q.py` |

*Within* is one structural test for all three. Only a person acts (AX-1), so offices and factions are conditioned through the persons who act for them. **Offices** condition their holder in his capacity: his `reach` already admits claims about his purview, and the seat's remit decides which verbs answer (a mayor's `requisition`, a duke's `march`). **Factions** are conditioned through their seat-holders. (A faction's `head` is `None`, and `at_war` is `False` for every pair, in every world the tree can build today; only the seat-holder route is live.) A faction's *side* in a strand (authority, challengers, outside power: the study's A, R, O) classifies moves and is not a regime. Flows never write a faction's goal rows; they change what a leader attends to, not what the organisation wants. **Scale** is the rung: a guild's strand at a settlement and the Crown's era at the realm are one relation at two rungs.

**The stamp.** `questions_for` already stamps standing occasions as classed referents onto the person's first question *after* the sort, so they displace nothing (vacancies, writs held, places named, larders in purview; `_stamped`, `world_q.py` ~3509-3517). `flows_known` adds one: the rungs, persons and offices at stake in each held flow, as referents of the existing closed classes (`Office, Record, Rung, Site, Proposition, Person, Detainee`). No `Flow` class. A person aware of a rising at his settlement finds that rung and its holder among his occasions, so verbs form on them (`march`, `petition`, `migrate`, `arrest`, `commit`) and each is chosen by his own convictions. Two people in one flow choose differently; none is told what the flow does next. No chooser reads a flow's opening kind or last move.

**The regime.** In Foucault's account a society holds a regime of truth: the discourse it accepts and makes function as true, the means of telling true from false, how each is sanctioned, the techniques valued for obtaining truth, and the standing of those charged with saying what counts. It is produced by relations of power, not laid over them. **It is not a political regime.** Jordan's definition (R13): an assemblage of institutions with commensurate dominant modes of understanding the world and behaving. In the engine's terms:

| part of the definition | where the engine has it |
|---|---|
| institutions | offices, factions, venues and arrangements |
| a mode of understanding | the affiliations a person holds and how intensely (`Person.conviction`); a faction's creed, committed to by its leader |
| a mode of behaving | what an affiliation engages or condemns (`affiliation_engagement`: the acts that scar an observer holding it) and the remit a seat holds |
| commensurate | no `incompatible` pair between the affiliations held (`true` strains, `false` is compatible, `null` has no source) |

Operationally, and person-side: **the regime a person stands in is his own held affiliations and the institutions he holds seats in.** Two persons are commensurate when no pair across their held affiliations is `incompatible`, the shape `person_q.confliction` already computes. An institution is described by the affiliations of its holders, as counts, with no single "dominant" one. `null` is read as not incompatible, which settles pair 6 that the roster leaves to Jordan. Corpus worlds hold no `conviction`, so the report is empty there. `[A4]` This replaces an earlier clique reading, which was not a partition: with `null` read as compatible, `altonian_civics` joins every set. A regime is not a side. The authority and the challengers may share one, and strife between regimes is where their affiliations strain; strife inside one is a contest over what its own terms require. The instrument reports, for each strand, whether any incompatible pair spans its parties. `[A5]`

**The word.** Layer 1 refuses `regime` in the governance sense ("a coinage for a thing `band` already covers", `01_AXIOMS.md:719-721`). This design uses Foucault's sense, defined here. CLAUDE.md §4 requires a defined term to be defined where it is invoked; no code identifier is named `regime`, and the identifier is chosen at build. Whether the term stands is a Jordan item (§10).

**The era is a regime's unity.** "The realm was turbulent" is how a regime makes simultaneous crises one. That is a reading, so persons, offices and factions can hold different accounts of one era and the engine holds none as the true one.

**Grading what a person credits: blocked.** `decision/options.py::teller_weight` grades a told claim when it is read, by the hearer's relation to the teller (rank, regard, track record) and the retelling count. It is live at shipped values (`told_weight` 0.5, each gain 0.5; the control arm is 1.0 and 0), and `rank` is dormant because it reads 0 for every pair (`H-181`). The parts of a regime map onto it: what is accepted as true (`weigh`), telling true from false (the inquiry verbs, `confidence.broken`), the standing of those who pronounce (`rank`, dormant), what is valued (the verbs a seat can form). A term that makes a hearer credit a teller more or less by the teller's regime would need the teller's institutions and affiliations, which are world truth about another person. It has no lawful landing:
- `decision/` has no World in scope, and `choose` cannot read another person, an aggregate or world truth (`04` §A.2:142, :171, :249). `fx` is flat numbers, identical for every person, and the stamp lands on a `Question`, which `teller_weight` never sees.
- It also puts the engine's own resolution into belief formation, which AX-7 forbids.

Three candidate landings, each with its cost: (1) mediation at WITNESS in `_refract`, beside channel, competence and prior (AX-7's three terms), frozen at deposit, which departs from CAT-3's "graded when read"; (2) a hearer-held claim about the teller's affiliation with a producer, of which none exists, `rank` being the measured precedent for a term with no producer; (3) the hearer's own conviction against the claim, person-side and AX-2-clean, with no regime effect on others. The design takes none. Until Jordan rules (§10), the regime conditions a person through lived events and attention only, and R9's "graded by the regime they are within" is not honoured.

## 6. The accepted tension, its loops, and what refuses it

Top-down, universal conditioning at the level of narrative, against bottom-up, granular awareness and decision by characters. Accepted (R10). Where each acts:

| top-down (the flow) | bottom-up (the person) |
|---|---|
| which events are read as one chain, at which rung, and how many a reading holds | what a person witnessed, was told and believes |
| which referents appear among his occasions | which verb he forms and chooses, by his own convictions and ambitions; what he does with them |
| what happens to him as a move of the flow (lived events) | everything else, including every terminal outcome |

The flow writes no state, names no next move and fires nothing. **Loops** (ID-16 asks a design to enumerate and sign them; the signs are asserted and unmeasured):

| loop | path | sign |
|---|---|---|
| L1 | stamp, attention, acts, moves, strand, stamp | positive: persons who know of a strand act on it |
| L2 | grouping under the flow above, fewer distinct strands held, fewer stamps | negative |
| L3 | conclusion frees a slot, a new strand is held, a new stamp | negative |

L1 is the loop that could harden into a determinant, tightest at the realm's single slot. **The guard is measured:** over the same seeds, with the stamp on and off, report the histogram of terminal codes reached per arm. Every code reached with it off must still be reached with it on, **and** no code's share may rise by more than the seed-to-seed spread of the off arm (the spread comes from the control, not from a number set here). A reachability-only guard sees narrowing and not concentration; this sees both. An arm that closes a route or concentrates the endings is a defect to remove.

**Refused, to stay inside ratified rulings:**
- No stored flow, state, phase or counter (T-a; ED-IN-0225: no arc carrier). Recomputed from the log and ledgers each time. `[A6]`
- No date, deadline, firing condition or outcome on anything (T-c, M16(b)). A flow has no next move. A terminus is recognized when persons' acts produce it; nothing authors it and nothing makes it happen.
- No self-worsening condition (M16's fourth motion, ED-IN-0301). Drought is weather on matter, famine is bodies, the rest is persons acting.
- No backbone required for membership.

## 7. Reachability: what must exist so every opening and every conclusion is possible

From the draft instrument's first run (4 seasons, seeds 0 and 1; kind-only grading, so upper bounds): 26 codes had matching events, 10 were declared with none (RF, RG, CL, NG, WA, WR, DA, CA, AM, XN), 4 have no producer (SH, CH, XE, XP). The DARK grade never fired because shared kinds mask it (`march.declared` reads OW and XA as observed although `foreign=False`); IM, XS and NG carry no `needs:` although their kinds are shared with other codes.

| gap | closes through |
|---|---|
| natural shock (SH) | CL-EVENTS commit (2), the live weather arm; CP-T10-02 calamity bands |
| natural death (DR, DN) | `age_step`, `illness_rate` set by Jordan (CP-T10-05) |
| outside war and power (OW, XA) | the `foreign` switch (IN-36), whose default Jordan holds (ED-IN-0301) |
| church sanction (CH) | a church seat issuing ban or detain tenures: data, and the seat |
| execution of a held person (XE) | §9: a verb row `execute`, routed through the personal-combat seam; it forms only on a live `detain`, which needs CP-T03-09's `capture` (B10-11) |
| declared, none seen (RF, RG, CL, NG, WA, WR, DA, CA, AM, XN) | the aperture funnel per verb first (which clause refuses it); change nothing before that |
| a later rising linked to a case (XP) | the opening of a successor strand (§4); no verb |
| **a conclusion from every opening** | for each opening kind and each of the 24 terminal base codes, an act route exists whose last move is that code. Where none does, the flow can never conclude and holds its slot for good, the realm's single slot being the worst case. |

## 8. Build order

Batches, labelled S1 to S6 so as not to collide with CL-THRUST's B0.1 to B6.n in the same plan. Each names what it depends on, what it moves and its test. A position in the master workplan is needed for each; this file names them and schedules none.

| | batch | depends on | hash | builder tier (CLAUDE.md §10) | falsifier and control |
|---|---|---|---|---|---|
| S1 | **Instrument, side-aware.** Classify by act (verb, degree, actor's faction against the rung's holder) in the world reading. Add the 16 links, the leave-and-rejoin profile, the per-code count of cases ending on it, the one-regime-or-two report, and `needs:` on every shared-kind row. Classify `person.died` by its causing act: `execute` is XE, a felling `fight` or `march` is KL, no act is DN; DR and the study's second code are a role the death plays in a strand, not another event. Transcribe the 102 coded paths as a fixture with provenance. Add a **static route check** (verb, `emits:`, code, over the verb table) **beside** the observed run: the first answers "a route exists", the second "default play reaches it". | draft in PR 553 | none | sonnet build, opus critic | shuffled-within-case log completes the links no more often than chance; a planted log completing a known link reads as completing it; **two unrelated hearth strands planted in one duchy stay two, and a duchy-wide levy with the riots against it reads as one**; a planted realm-rung event does not merge them |
| S2 | **Gaps of §7**, one lane each, in parallel worktrees: SH, bodies, foreign (Jordan-held default), church seat, `execute` (after CP-T03-09's `capture`), and the funnel for the ten declared-but-unseen codes | independent of each other; the funnel needs S1's counts | each a declared mover; `execute` too | sonnet per lane, opus on the `execute` row | per lane, a code moves from 0 to observed over several seeds, with CR-49's `confer` and `oblige` counts as the control against being crowded out |
| S3 | **`flows_in` and `flows_known`**, World-first queries with no consumer in the loop | S1 | none | opus (judgment on the linking rule) | a witness and a hearsay holder of the same events read different flows; an empty ledger reads none; two realm-wide events while an era is open read as one era; a terminal claim with the open-referent test met concludes the flow and frees the realm slot, the claim missing leaves it open; a person within the realm flow whose ledger holds none of its moves reads no realm flow, yet the world reading lists him as within |
| S4 | **The stamp** in `questions_for`, switch shipped off | S3 | off equals the base hash; on is a declared mover | opus | the stamp changes which verbs form for a person in a held flow; the §6 guard over the same seeds |
| S5 | **A ruling on where, if anywhere, regime may grade credit** (§5, §10). Not a build. | Jordan | none | none | none until ruled |
| S6 | **Deck**: world-build seeds per category through the CL-EVENTS commit (3) schema (goal rows or yield scales, drawn once at build) | S1; CL-EVENTS (3) and (4) in B10-18 | equal while shipped off | sonnet for rows, opus for the schema widening | measured by S1's reachability report per category; it has no on-arm today |

The longest chain is S1, S3, S4. S2 runs beside S1.

## 9. Executed (XE), defined

The study's code is "leader executed; side is the side of the person executed". Its uses: a captured rebel leader put to death by the authority (Ball, Kett, Dózsa, Cade, Egmont and Horn, Aske), a captured authority figure put to death by the challengers (the five XE-A), a rebel leader put to death by another rebel (Bato), and a purge inside the challengers' own side (Želivský, beheaded by the Hussite council of Prague). The robust link is capture then execution (19 of 35 cases). What these share: **a person in custody is put to death by the deliberate act of those holding him, as sentence or order.** The side is the dead person's.

It is not the neighbouring moves. *Killed* (KL) is a death outside custody: in battle, by assassination, by a crowd (Artevelde), by one's own followers. *Died* (DN) is a death with no act of another. *Punished* (PU) is repression short of death.

**In the engine:** a death is an execution when the act that caused it (found by `causes*` into the act store, as `attribution.actor_of` does) is an `execute` act, by a person acting through a seat, on a person who held a live `detain` tenure **to that seat** when it resolved. It follows `pardon`'s closure basis, which acts only through the seat that is the `detain` edge's object, and `arrest`, which opens that edge only on a held warrant naming the subject. So the rebels' execution of an authority figure (XE-A) needs a rival seat that holds `dispatch` and `determine`, an issued warrant, an arrest, and then `execute`. That chain is producible in principle and **constructed nowhere yet**. A mass execution is one act per person.

**The verb:** a new row `execute`, on the shape of `interrogate` (eligibility `remit:determine`, referent class `Detainee`, the subject held in a live `detain`) and `pardon` (`remit:determine`, the subject a person over whom the seat sits as a bench). The pair is deliberate: `pardon` ends the detention, `execute` ends the life. **It cannot write a death directly.** Jordan ruled on 2026-09-02, of a direct kill: "that would trigger the personal combat scene. you can't just kill or wound imo" (`hole_register.yaml:1087`, carried at `verb_table.yaml` ~695). So `execute` carries `contests: the body` and reaches death only through the personal-combat seam, as `fight` does, with lethal terms (CP-T03-09 gives `PersonalCombatInput` a `terms` field, default lethal). What the seam does with a restrained party, and whether a captive can lose a scene he cannot fight, is the seam's and is **open for the row's build**; this file asserts neither. The death path after the seam is the felled combatant's (`person.died`, the dead person's seats closed per CP-T02-01). The realm has no live `detain` until CP-T03-09's `capture` (B10-11, amended, held on PC-10b's Record route), and no `arrest` was observed in my run, so `execute` forms on no one in default play and S2's falsifier cannot pass before then. A hash mover, built through its own position. Taken by precedent and by what the architecture allows (CLAUDE.md §0, steps 4 and 5), not put to Jordan. `[A7]`

## 10. Assumptions register, and what Jordan owes

Each assumption carries a revert. All are `[ASSUMPTION; medium; Jordan to correct]`.

| | assumption | revert |
|---|---|---|
| A1 | "n+1" means each rung holds one more than the rung above; capacity is read from the order of `rung_kinds`; no typed slots below the duchy | delete the rule and §4's grouping |
| A2 | The slot-ranking rule: reach, moves, recency, claim order | any other ordering of the same kind |
| A3 | The 102 final moves in §4, transcribed by me from the case-mapping tables; `[UNVERIFIED]` until cross-checked against the study | rebuild the fixture from the study |
| A4 | The person-side reading of a regime (own held affiliations; commensurate means no incompatible pair; `null` as not incompatible) | delete that paragraph |
| A5 | Strife inside a regime (a charter quarrel, category D) against between regimes (doctrine, category F) is a reading of the categories, not a finding | drop the sentence; the instrument still reports whether an incompatible pair spans a strand's parties |
| A6 | A derived reading is outside the refusals of T-a, ED-IN-0225 and M16's fourth motion, because it stores nothing and acts only through persons | the plan's owner rules otherwise and the design is withdrawn |
| A7 | `execute` as a new verb row on `interrogate`'s and `pardon`'s shape, acting only through the custody seat and reaching death only through the combat seam | delete the row |
| A8 | `strife_moves.yaml` readings: each verb and kind is a reading of `verb_table.yaml` by name, not an execution | delete the file, `data/strife.py` and `harness/strife.py` |
| A9 | The linking rule of §4 (shared referent, one rung step, same person; never through the realm; never by holder) | any other bounded rule, tested by S1's planted strands |
| A10 | Rule (b) for reopening, the open-referent test for conclusion, XP's exclusion from the terminal set, and the era concluding on a realm-rung terminal move | rule (a); drop the test; restore XP |

**Needs Jordan** (what survives precedent and the architecture):
1. **Where, if anywhere, regime may grade what a person credits** (S5; §5). The three landings each depart from a ratified reading: WITNESS-time mediation from CAT-3, a hearer-held claim from the current absence of any producer, and the hearer's own conviction from R9. Choosing a landing, or choosing "lived events and attention only", decides whether R9's grading half is honoured.
2. **A6**: whether a derived reading is inside ED-IN-0225, which answered "what is an arc, as a thing the engine holds" and bound no future session to answer it. A "no" withdraws the design.
3. **The `foreign` default** (IN-36, held under ED-IN-0301). The OW and XA lane waits on it.
4. **The word `regime`**: Layer 1 refuses it in the governance sense. Confirm the Foucault sense, defined here, may stand, or name another term.

Taken by precedent or from the study, with reasons above: capacities, terminal moves (XP excepted), execution (the custody seat only), the linking rule, the reopening rule.
