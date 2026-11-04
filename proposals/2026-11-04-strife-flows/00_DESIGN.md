# Strife flows: every strife move reachable, and a person's reading of the flows around them

## Status: PROPOSED (2026-11-04), HELD BACK IN FULL. Reference under CLAUDE.md §0.05, not a mechanism; merging this file ratifies nothing and applies no ED-1094 default.
## Lane: IN

Source: the study "Mechanics of Strife to c. 1600" (102 cases, nine filing categories A to I, 40 move codes, 16 recurring links; claude.ai artifact XDjCCRvbxiPS6sumpRtnte). Jordan's rulings of 2026-11-04, in conversation: outcomes must be possible, never triggered; the flows are a meta-narrative that conditions how people choose; they begin from events that arise in play (taxes raised, drought then famine, a succession crisis); too many live strifes would be illegible to a player, so new events fold into existing flows.

What this adds to `engine/season/`: one pure query module (`queries/situation_q.py`), one count per code in `strife_moves.yaml` (capacity is read from the order of `rung_kinds`), one stamp in `questions_for`. Nothing is stored, no step is added, no clock runs.

---

## 0. The accepted tension

Jordan, 2026-11-04: the design holds a top-down, universal conditioning at the level of narrative against bottom-up, granular awareness and decision by characters. The tension is accepted. The flows exist to condition the rungs of play into legible narratives with subplots (the realm's one flow, a duchy's tributary and isolate, the hearth's own quarrel) without determining outcomes.

Where each side acts, so that neither swallows the other:

| top-down (the flow) | bottom-up (the person) |
|---|---|
| which events are read as one chain, at which rung, and how many a reading holds | what a person witnessed, was told and believes (AX-7) |
| how a person's told claims are graded, by the regime he is within (§5a) | which verb he forms and which he chooses, by his own convictions and ambitions |
| which referents appear among his occasions (§5) | what he does with them |
| nothing else | everything else, including every terminal outcome |

The flow writes no state, names no next move and fires nothing; it changes the order and weight of what a person already holds. Where it could harden into a determinant is a loop: flows condition choices, choices make the moves that define the flows, and the realm's one slot makes the loop tightest at the top. The guard against it is measured, not declared: with the conditioning on, each concluding class of §4 that is reachable with it off must remain reachable, and the spread of classes reached across seeds must not narrow to one. A conditioning arm that closes a route or collapses the spread is a defect to remove (§8 step 4).

## 1. What the study licenses

A space of chains, not a script. Cases share 40 moves and 16 recurring links, spend about a quarter of their moves on those links, and leave and rejoin them constantly; 93 of 102 end off the links, which says where on the chain they stop and not that they stop without an ending: every dossier records one (each category section's "Endings" line). Categories differ in how they open and how they end, and in almost nothing between (only A's natural shock and B's death, regime change and claim are distinctive, and those are what the labels name). So: **a flow is an open chain of moves around shared referents; its category is only the kind of event that opened it.** Membership must not require the 16 links, or a detour would end a flow.

## 2. Two readings, and where each may be read

| reading | over | read by | AX |
|---|---|---|---|
| **world reading** `flows_in(log)` | the whole Event log | the harness; and the engine, as data, when it grades what a person within a flow credits (§5a) | never deposited in anyone's ledger as a claim, and never read by a chooser |
| **person reading** `flows_known(w, p)` | `p.ledger` alone: claims `p` witnessed or was told | `questions_for`, so the person's choices | AX-7: a character has a reading of the world, never the world |

Both are pure functions: same input, same output, nothing written. The person reading is what a person can place and act on. The world reading is what binds a person whether or not he can: the engine uses it as it uses the rung tree, to condition how his own readings are graded. The instrument also checks the person reading against it.

## 3. How a flow is read

A **move** is a ledger claim whose Event kind and act classify to one of the 40 codes (`strife_moves.yaml`, to be made side-aware by classifying on the act: verb, degree, and the actor's faction against the holder of the rung). Non-strife claims never join a strand; they are still of the era beneath whose rung they fall (§4).

A **flow** is a maximal set of moves linked by shared referents, with referents compared through the rung ladder (`ancestry`, `place_of`, `holder_faction_of`): two moves are linked if their referents are the same, or one is an ancestor of the other, or they share a faction. It sits at the lowest rung that covers its moves, so a flow zooms: a hearth's grain dispute is a flow at the hearth; when its referents join others' under one territory it is read at the territory.

A flow has a **terminus**: a concluding outcome (§4). A chain of moves that has not reached one is an **open** flow, still unfolding, and is read as such; one that has is **concluded**. A chain that could never reach one is not a flow. That is a defect in the loop, not a state (§7).

Its **opening kind** is the category of the oldest move in it:

| opening, as it arises | read from | exists today |
|---|---|---|
| tax or levy raised (C) | `dispensation.issued`, `requisition.taken`, `duty.taken` | yes: 401 events over seeds 0 and 1 at 4 seasons |
| shortage, then famine (A) | a settlement's hunger band; a yield below its floor | hunger is read (`hunger_by_settlement`) and whether it binds rests on CR-22 (B10-18; status not checked); the shock that causes it is dark (`season_factor_draw` ships `()`) |
| succession crisis (B) | a seat emptied by `person.died`, then `succeed` or a rival claim | deaths occur (15 over seeds 0 and 1 at 4 seasons); no natural death (`age_step`, `illness_rate` are 0.0); rival claims 0 observed, cause not yet found |
| army unpaid (H) | a levy that does not reach its troops | source not yet located |
| burden on a subject people, foreign rule, religious or status grievance (D, E, F, G, I) | the same moves, opened by a foreign actor or a church or caste seat | foreign off; no church seat issues sanctions |

Opening conditions are read off state the loop already holds; nothing fires on them.

## 4. Stakes, scarcity, eras and strands

**A flow's rung is its stakes.** A succession crisis at a territory is a small event; at a duchy a larger one; at the realm the largest there is. Scarcity follows from where a rung sits in the ladder: the higher the rung, the fewer flows a reading holds.

**Capacity.** Jordan's rulings of 2026-11-04: the realm holds one flow, which conditions every flow beneath it; a duchy holds up to two, a *tributary* strand that drains into the realm's flow and an *isolate* that does not. Below the duchy, "n+1", read as each rung holding one more than the rung above. By the order of the existing `rung_kinds` roster (`person, hearth, community, settlement, territory, province, duchy, realm`) read from the top: realm 1, duchy 2, province 3, territory 4, settlement 5, community 6, hearth 7, person 8. So capacity is a function of a kind's position in a roster that already exists, not a second table of numbers. No slots are typed below the duchy. The built realm has no province rung (census), so 3 binds nothing yet. `[ASSUMPTION; medium; Jordan to correct; revert: delete the rule and §4's fold]` Capacity limits what a *reading* holds at a rung, never an event.

**Era and strand.** A succession crisis, a foreign invasion, a famine and a tax crisis can all be open at once, and those living through them do not parse them apart: the realm was very turbulent, and eventually things happened. They are comorbid, tributaries into a river, the river into a funnel. So the realm's one flow is an **era**: a *confluence* whose opening kind is not one category but the set of them open beneath it. A **strand** is a narrative chain of the kind the study's cases are: specific, with its own opening, moves and conclusion, and always at a lower rung than the era it feeds, because specifics are the opposite of a universal. The era is read generally (few referents: the crown, the realm's seats); strands carry the particulars. The study's 102 cases are strands. Both are flows by §3.

**Everything operating within an era is of the era.** The era is not a container with things inside it. Membership of an era is by scope: every act, claim and institution beneath the realm's rung, strife or not, is of it. A merchant's trade, a marriage and a harvest in a famine-and-war era are of that era, conditioned by its regime as a raid is. Strand membership is narrower: strife moves linked by referents (§3). So the era's *moves*, which rank it and conclude it, are strife moves; its *conditioning* reaches everything beneath it (§5a).

**Which flow takes a scarce slot.** The one whose moves reach the most distinct rungs below, then the most recent; ties by claim order. A rule with no number invented. `[ASSUMPTION; medium; Jordan to correct; revert: any other ordering of the same kind]`

**Overflow is subsumed, not dropped.** A flow that finds no slot at its rung is read as part of the flow at the nearest ancestor rung that has one. At the realm, a second realm-wide event is read inside the era. At a duchy, a strand that shares referents with the era takes the tributary slot; one that does not takes the isolate slot; a third folds into the era. Nothing is deleted: the moves stay in ledgers as claims.

**A strand grows up the ladder.** It is read at the lowest rung covering its moves (§3). A grain dispute at a hearth is a hearth strand; when other hearths of the settlement join it, it is read at the settlement; across territories, at the duchy, where it contests for a slot. Its stakes rise with its reach.

**The larger flow frames the smaller, for everyone within it** (§5a), aware of it or not.

**Conclusion.** No timer retires a flow. A strand concludes on a terminal move; an era concludes when every strand draining into it has concluded. The terminal moves are the artifact's own: the last substantive move (NOTE and OTH set aside) of each of its 102 cases, read by me from the nine case-mapping tables and tallied by script. The study does not state them. `[UNVERIFIED: transcription of 102 final moves from the tables]`

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

and a further fifteen base codes end fewer: OW, IN, SB, PU (3 each); FA, NG, FR (2 each); DN, CL, CP, RF, WN, PT, CA, XA (1 each). Twenty-five base codes end at least one case. The other fifteen never do and cannot conclude a strand: SH, DR, BR, MO, OP, RU, VI, SZ, RG, SP, CH, WR, RT, DA, AM. `strife_moves.yaml` carries the count per code, so the codes ending a single case read as single cases.

Two notes on reading these. **XP is not a move the loop produces:** it is the study's mark that later risings are linked to the case. In the loop a strand concludes by persistence when a new strand opens on its referents, and that opening is the event. **A terminal move is not always final in the study:** F-2 holds seven settlements and B-4 follows a settlement with a refusal, a capture and a further settlement. Two rules are candidates: (a) the first terminal move closes the strand, and later conflict on its referents is a new strand; (b) a strand is concluded while its latest move is terminal and reopens if a conflict move follows. They are chosen by measurement, not argument: replay the study's 102 coded paths through each and keep the rule that draws one strand per case most often (§8 step 1).

A person's reading of a strand is open until a claim of a terminal move lands in his ledger. Someone who has not heard that the war is over still believes it on and acts on that belief (AX-7). What binds him by where he lives is the world reading's, and ends when the flow does.

Because a witness and a person who was only told hold different claims, they read different flows from the same events. That is deliberate.

## 5. How it conditions choice

No new channel. `questions_for` already stamps standing occasions onto a person's first question as classed referents: vacancies, writs held, places named, larders in purview (`_stamped`). `flows_known` adds one more stamp: the rungs, persons and offices at stake in each held flow, as referents of the existing closed classes (`Office, Record, Rung, Site, Proposition, Person`). No `Flow` class is added.

Effect: a person aware of a rising at his settlement finds that rung and its holder among his occasions, ranked by `attention_key`, so verbs form on them (`march`, `petition`, `migrate`, `arrest`, `commit`) and each is chosen by his own convictions as now. Two people in one flow choose differently; none is told what the flow does next.

The flow's opening kind and last move are not read by any chooser in this design. Whether they should weight options (fear on a quiet rung, hope on a petition) is a second step, after the stamp is measured.

## 5a. People exist within flows: a regime of truth

Jordan, 2026-11-04: people exist within flows as in Foucault's hypothesis of a regime of truth. In that account a society holds a regime: the discourse it accepts and makes function as true, the means of telling true from false, how each is sanctioned, the techniques valued for obtaining truth, and the standing of those charged with saying what counts. It is produced by relations of power, not laid over them.

**A regime is not a political regime.** Jordan, 2026-11-04: in Foucault's sense it is an assemblage of institutions with commensurate dominant modes of understanding the world and behaving, not a form of governance. In the engine's own terms:

| part of the definition | where the engine has it |
|---|---|
| institutions | offices, factions, venues and arrangements |
| a mode of understanding | the affiliations a person holds and how intensely (`Person.conviction`); a faction's creed, committed to by its leader |
| a mode of behaving | what an affiliation engages or condemns (`affiliation_engagement`: the acts that scar an observer holding it) and the remit a seat holds |
| commensurate | not `incompatible` in the strain matrix (`true` strains, `false` is compatible, `null` has no source and is read as not incompatible) |

Operationally: two institutions are linked where they share a holder, a conferral or remit grant, a bond (`tie`, `knot`) or a venue; a **regime** is a set of linked institutions whose dominant affiliations (the one most held among their holders, by intensity) are pairwise not incompatible. Five affiliations are rostered, so a handful of regimes at most. `[ASSUMPTION; medium; Jordan to correct; revert: delete this paragraph and the term in §5a's credit step]`

A regime is therefore not a side. The authority and the challengers may share one, and two regimes may stand in a realm without strife. Strife between regimes is where their affiliations strain; strife inside one is a contest over what its own terms require. As a reading of the study's categories (not a finding): a quarrel over a charter or a privilege (D) is fought inside a shared understanding of what a charter is, and a quarrel over doctrine (F) between understandings. The instrument can report, for each strand, whether its parties stand in one regime or two.

For this design:

**Within and aware are different relations.**

| relation | what makes it so | what it does |
|---|---|---|
| **within** | structural: the flow's rung is `p`'s own rung or an ancestor of it (`ancestry`) | the regime bears on `p` whether or not he has any concept of the flow: what happens to him is a move of it, and what he credits is graded by it |
| **aware** | epistemic: `p`'s ledger holds the flow's moves | `p` can place events in it and act on its referents (§5) |

Awareness is not required to be within a flow, and requiring it would put a person outside the events he is living through. Someone who has never heard of a pandemic still falls ill, finds the market closed and is told what to do by someone who has; the concept is not what exposes him to it. Having the concept changes what he can do about it, not whether it reaches him.

Everyone is within the realm's flow (§4). A hearth-dweller who has heard nothing of the war is within it by two routes, neither of which hands him the flow as a fact. The first is **lived events**: matter and bodies reach him as they reach anyone (stores requisitioned, hunger, a neighbour dead), together with the acts and words of those who are aware (the tax-collector, the recruiter, the neighbour who was told), which arrive as witnessed events and told claims. The second is **grading**: the engine grades what he credits by the regime he is within (below). Neither deposits a claim in his ledger; AX-7 is kept.

**The regime is immanent.** It is made of what its institutions accept and do and of the seats that pronounce (`determine`, `issue`, a held `dispensation`), and is stored nowhere. The side the study gives every move (A, R, O, N) is a different fact. Side-aware classification (§8 step 1) is needed to tell WA from WR and to read a strand; it does not grade what anyone credits.

**The engine already has the mechanism, dark.** `decision/options.py::teller_weight` grades a told claim when it is read, by the hearer's relation to the teller (rank, regard, track record) and by the retelling count; at its shipped control values (`told_weight` 1.0, all gains 0) every claim weighs 1.0 and nothing is conditioned. The four parts of a regime map onto it as follows:

| part of a regime | where it already stands |
|---|---|
| what is accepted as true | `weigh`: how far a hearer credits a claim; the noisy-OR over distinct origins |
| telling true from false | the inquiry verbs (`examine`, `interview`, `interrogate`, `research`) and `confidence.broken` |
| standing of those who pronounce | `rank(p, teller)`; the seat a speaker acts through |
| what is valued | the verbs a seat can form and the remits it holds |

The proposed addition is one term in `relation`: whether the teller stands in the regime `p` stands in, or in a regime commensurate with it. A commensurate teller is credited more, an incommensurate one less. It reads the world reading, not `p`'s ledger, so it binds an unaware `p` as it binds an aware one. It is a **second step**, after the stamp (§5) is measured, for three reasons: it reorders every told claim in the loop and so moves the hash widely; its effect cannot be told apart from the stamp's until the stamp is measured alone; and AX-2 binds `decision/`, so the flow's standing must arrive there as data (as `fx` and the stamped questions do), never as a read of the World. `layer-conformance` Lens B settles that placement before any code.

**The era is a regime's unity.** Simultaneous crises are not parsed apart by those inside them; "the realm was turbulent" is how the regime makes them one. That unity is itself a reading produced within the regime (what is named, what is said to have caused it, who is entitled to say), so persons, offices and factions can hold different accounts of one era and the engine holds none as the true one. The world reading's confluence is the instrument's. A person's era is as much of it as his ledger and his regime give him.

## 5b. Offices and factions are within flows too

Jordan, 2026-11-04: flows condition factions at whatever scale is relevant, and offices, as well as persons. The engine already places all three on the ladder:

| entity | its rung | precedent |
|---|---|---|
| person | `home_of`, with the ladder above it | `world_q.reach`, limbs 1 to 3 |
| office | `Office.rung`; its purview is that rung and its descendants | `reach` limb 4; `faction_q.purview` |
| faction | the rungs it holds (`faction_q.holdings`, `holder_faction_of`), and its relations (`at_war`) | `queries/faction_q.py` |

So *within* (§5a) is one structural test for all three: the flow's rung is the entity's rung or an ancestor of it (for a faction, of any rung it holds). Only a person acts (AX-1), so offices and factions are conditioned through the persons who act for them, by existing channels:

- **Offices** condition their holder in his capacity. His `reach` already admits claims about his purview; a flow at a rung in his purview or above puts that rung's referents among his occasions, and the seat's remit decides which verbs can answer (a mayor's `requisition`, a duke's `march`). An office is the institutional form of awareness: the holder knows what his claims cover, no more (AX-7).
- **Factions** are conditioned through their heads and seat-holders. A faction belongs to a regime through its creed and the institutions it is linked to (§5a). Its *side* in a strand (authority, challengers or outside power: the study's A, R, O) is a separate fact, read from its holdings, its `at_war` relations and its members' moves; it classifies moves and does not grade credit. A strand's referents, the opposing faction's rungs among them, are put among its leaders' occasions. Flows do not write a faction's goal rows: they change what a leader attends to, not what the organisation wants.
- **Scale** is the rung. A guild's strand at a settlement and the Crown's era at the realm are one relation at two rungs, and a faction in several flows holds a position in each.

## 6. What it refuses

- No stored flow, state, phase or counter (T-a; ED-IN-0225: no arc carrier). Recomputed from claims each time.
- No date, deadline, firing condition or outcome on anything (T-c, M16(b)). A flow has no next move. A terminus is recognized when persons' acts produce it; nothing authors it and nothing makes it happen, so it is not an outcome in M16(b)'s sense.
- No self-worsening condition (M16's fourth motion, ED-IN-0301). Drought is weather on matter, famine is bodies, the rest is persons acting.
- No backbone required for membership (§1).

## 7. Reachability: what must be built so every opening is possible

From the draft instrument's first run (upper bounds; see PR 553 for its defects):

| gap | closes through |
|---|---|
| natural shock (SH) | CL-EVENTS commit (2), the live weather arm; CP-T10-02 calamity bands |
| natural death (DR, DN) | `age_step`, `illness_rate` set by Jordan (CP-T10-05) |
| outside war and power (OW, XA) | the `foreign` switch (IN-36) |
| church sanction (CH) | a church seat issuing ban or detain tenures: data, and the seat |
| execution of a held person (XE) | defined in §9; a verb row `execute`, taken by precedent |
| declared, none seen (RF, RG, CL, NG, CA, AM, DA, XN) | the aperture funnel per verb first (which clause refuses it); change nothing before that |
| a later rising linked to this case (XP) | read by `flows_known` itself; no verb |
| **a conclusion from every opening** | for each opening kind and each of the 25 terminal base codes in §4, an act route exists whose last move is that code. Where none does the flow can never conclude and holds its slot for good: the realm's single slot is the worst case. This is a requirement of the loop, checked by the instrument (§8 step 1) |

## 8. Build order, each with its falsifier

1. **Instrument, side-aware** (no hash change). Classify by act, add the 16 links and the leave-and-rejoin profile. Control: the same log with moves shuffled within each case must complete the links no more often than chance. Falsifier: a planted log that completes a known link must read as completing it. Add the conclusion check: for each opening kind, run seeds forward and report which terminal codes any strand reached; a code never reached over several seeds is a finding about default play, not proof of absence, and the same run at more seeds is its control. Classify `person.died` by its causing act (`execute` is XE, a felling `fight` or `march` is KL, no act is DN; DR and the study's second code are a role the death plays in a strand, not another event). Replay the study's 102 coded paths through §4's two strand rules and keep the one that draws one strand per case most often. Add the per-code count of cases ending on it to `strife_moves.yaml`.
2. **Gaps in §7**, each through its own existing position, each a hash mover declared as such.
3. **`flows_known`** as a pure query with no consumer. Falsifiers: a witness and a hearsay holder of the same events read different flows; a person with an empty ledger reads none; two realm-wide flows planted in one ledger read as one realm flow with the second inside it; the same ledger with a terminal claim added reads the flow as concluded and frees the realm slot; a ledger with the claim missing still reads it open; a person within the realm flow whose ledger holds none of its moves reads no realm flow (he can place none), yet the world reading lists him as within it, and the §5a credit term (when built) grades his told claims by it.
4. **The stamp** in `questions_for`, switch shipped off. Control: switch off reproduces the base hash. Guard of §0: over the same seeds, the set of concluding classes reached with the stamp on contains the set reached with it off, and the number of distinct classes reached does not fall. Measure: the stamp changes which verbs form for a person in a held flow, and the `confer` and `oblige` counts CR-49 watches do not fall to 0.
5. **Deck**: world-build seeds per category through the CL-EVENTS commit (3) schema, measured by step 1.

## 9. Executed, defined (XE)

The study's code is "leader executed; side is the side of the person executed". Its uses: a captured rebel leader put to death by the authority (Ball, Kett, Dózsa, Cade, Egmont and Horn, Aske), a captured authority figure put to death by the challengers (the five XE-A), a rebel leader put to death by another rebel (Bato), and a purge inside the challengers' own side (Želivský, beheaded by the Hussite council of Prague). The robust link is capture then execution (19 of 35 cases). What these share: **a person in custody is put to death by the deliberate act of those holding him, as sentence or order.** The side is the dead person's.

It is not the neighbouring moves. *Killed* (KL) is a death outside custody: in battle, by assassination, by a crowd (Artevelde), by one's own followers. *Died* (DN) is a death with no act of another. *Punished* (PU) is repression short of death.

**In the engine:** a death is an execution when the act that caused it (found by `causes*` into the act store, as `attribution.actor_of` does) is an `execute` act, by a person acting through a seat, on a person who held a live `detain` tenure when it resolved. Any seat with the remit can do it, a rival government's included, so both XE-R and XE-A are producible. A mass execution is one act per person.

**The verb:** a new row `execute`, on the shape of `interrogate` (eligibility `remit:determine`, referent class `Detainee`, the subject a person held in a live `detain`) and `pardon` (`remit:determine`, the subject a person over whom the seat sits as a bench). The pair is deliberate: `pardon` ends the detention, `execute` ends the life. It writes the same death path as a felled combatant (`person.died`, the dead person's seats closed per CP-T02-01). It is a hash mover and is built through its own position, not here. Taken by precedent and by what the architecture allows (CLAUDE.md §0, steps 4 and 5), not put to Jordan. `[ASSUMPTION; medium; Jordan to correct; revert: delete the verb row]`

## Needs Jordan

1. Whether the credit term of §5a is a second step as proposed, or part of the first build.

Taken by precedent or from the artifact, with the reasoning above: capacities (§4: n+1), terminal moves (§4: the artifact's own), execution (§9). Each carries an `[ASSUMPTION]` and a revert.
