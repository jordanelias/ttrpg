# Strife flows: every strife move reachable, and a person's reading of the flows around them

## Status: PROPOSED (2026-11-04), HELD BACK IN FULL. Reference under CLAUDE.md §0.05, not a mechanism; merging this file ratifies nothing and applies no ED-1094 default.
## Lane: IN

Source: the study "Mechanics of Strife to c. 1600" (102 cases, nine filing categories A to I, 40 move codes, 16 recurring links; claude.ai artifact XDjCCRvbxiPS6sumpRtnte). Jordan's rulings of 2026-11-04, in conversation: outcomes must be possible, never triggered; the flows are a meta-narrative that conditions how people choose; they begin from events that arise in play (taxes raised, drought then famine, a succession crisis); too many live strifes would be illegible to a player, so new events fold into existing flows.

What this adds to `engine/season/`: one pure query module (`queries/situation_q.py`), one roster (rung capacities, terminal moves) in `rosters.yaml`, one stamp in `questions_for`. Nothing is stored, no step is added, no clock runs.

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

A **move** is a ledger claim whose Event kind and act classify to one of the 40 codes (`strife_moves.yaml`, to be made side-aware by classifying on the act: verb, degree, and the actor's faction against the holder of the rung). Non-strife claims never join a flow.

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

## 4. Stakes, scarcity and subsumption

**A flow's rung is its stakes.** A succession crisis at a territory is a small event; at a duchy it is larger; at the realm it is the largest there is. Scarcity follows from where a rung sits in the hierarchy: the higher the rung, the fewer flows it can hold in a reading. Jordan's rulings of 2026-11-04, in conversation:

- **Realm: one flow.** It conditions every flow beneath it.
- **Duchy: up to two** (a *tributary* flow, which belongs to the realm's flow, and a *discrete* or *isolate* flow, which does not).
- Rungs below the duchy hold more; their capacity is not yet ruled (see Needs Jordan).

Capacity is a roster in `rosters.yaml` keyed by `RUNG_KINDS` (the closed list), `[ASSUMPTION; medium; Jordan to correct; revert: delete the roster and §4's fold]`. It replaces the earlier per-person limit `K`. It limits what a *reading* holds at a rung; it limits no event.

**Which flow takes a scarce slot.** The one whose moves reach the most distinct rungs below, then the most recent; ties by claim order. A rule, with no number invented. [ASSUMPTION; medium; Jordan to correct; revert: any other ordering of the same kind.]

**Overflow is subsumed, not dropped.** A flow that finds no slot at its rung is read as part of the flow at the nearest ancestor rung that has one. At the realm, a second realm-wide event (a foreign invasion during a succession war) is read inside the realm's one flow. At a duchy, a flow that shares referents with the realm flow takes the tributary slot; one that does not takes the isolate slot; a third folds into the realm flow. Nothing is deleted: the moves stay in the ledger as claims, and the person has placed them in a larger picture.

**A flow grows up the ladder.** A flow is read at the lowest rung covering its moves (§3). A grain dispute at a hearth is a hearth flow; when other moves at other hearths of the same settlement join it, it is read at the settlement; when it spreads across territories it is read at the duchy and contests for a duchy slot. Its stakes rise as its reach does, and the capacity at each rung is what a player meets.

**The larger flow frames the smaller, for everyone within it.** Every flow beneath the realm's is lived inside it. Whoever lives at a rung the realm flow covers is within it (§5a), aware of it or not. Awareness adds something different: it lets him place his local events in the larger chain and act on its referents (§5). A person with no concept of the war still has his grain requisitioned, his neighbours conscripted and his market shut. Those are his own firsthand claims, and they are moves of the flow whether or not he reads them as one.

**A flow ends by a concluding outcome, never by quiet.** No timer retires a flow, so a slot frees only when its flow concludes. Reading the study's category "Endings" lines, the outcomes that conclude a case fall into six classes:

| class | the study's cases | moves that show it |
|---|---|---|
| settlement | a charter reissued, a Dictum, treaties, the Compactata, the Edict of Nantes, the Pacification of Ghent, a shared title by agreement | XS, with CO or IN |
| change of regime or border | a new dynasty, independence, annexation, a ruler deposed and killed | XN, with IN or CL |
| defeat of the challengers | main force beaten, leaders executed or dead, a city taken, bands broken | WA with CA, XE, KL or DN of the leader; SB; PC |
| defeat of the authority | the Company took Athens, a challenger held or gained control, a commander independent for seventeen years | WR with KL, FA or XN |
| relief of the cause | rations arrive or the shortage eases, unpunished; a burden repealed; a reform annulled | the cause's own state: hunger fed, the levy withdrawn, RV |
| withdrawal or extinction | a retreat to Vilcabamba, removal to Naupactus, a partition of the contest, the rung razed or emptied | RT with the parties gone; PC on a rung that no longer holds the quarrel |

The classes are a reading of the study. Which moves are terminal, and whether a class is one outcome or several, is Jordan's (Needs Jordan). A concluded flow may be followed by another whose first move shares its referents (the study's XP, later trouble). That is two flows, and nothing links them but the shared referents.

What a person can place is open until a claim of a terminal move lands in his ledger. Someone who has not heard the war is over still believes it on and acts on that belief; that follows from AX-7. What binds him by where he lives is the world reading's, and ends when the flow does.

Because a witness and a person who was only told hold different claims, they read different flows from the same events. That is deliberate.

## 5. How it conditions choice

No new channel. `questions_for` already stamps standing occasions onto a person's first question as classed referents: vacancies, writs held, places named, larders in purview (`_stamped`). `flows_known` adds one more stamp: the rungs, persons and offices at stake in each held flow, as referents of the existing closed classes (`Office, Record, Rung, Site, Proposition, Person`). No `Flow` class is added.

Effect: a person aware of a rising at his settlement finds that rung and its holder among his occasions, ranked by `attention_key`, so verbs form on them (`march`, `petition`, `migrate`, `arrest`, `commit`) and each is chosen by his own convictions as now. Two people in one flow choose differently; none is told what the flow does next.

The flow's opening kind and last move are not read by any chooser in this design. Whether they should weight options (fear on a quiet rung, hope on a petition) is a second step, after the stamp is measured.

## 5a. People exist within flows: a regime of truth

Jordan, 2026-11-04: people exist within flows as in Foucault's hypothesis of a regime of truth. In that account a society holds a regime: the discourse it accepts and makes function as true, the means of telling true from false, how each is sanctioned, the techniques valued for obtaining truth, and the standing of those charged with saying what counts. It is produced by relations of power, not laid over them. For this design:

**Within and aware are different relations.**

| relation | what makes it so | what it does |
|---|---|---|
| **within** | structural: the flow's rung is `p`'s own rung or an ancestor of it (`ancestry`) | the regime bears on `p` whether or not he has any concept of the flow: what happens to him is a move of it, and what he credits is graded by it |
| **aware** | epistemic: `p`'s ledger holds the flow's moves | `p` can place events in it and act on its referents (§5) |

Awareness is not required to be within a flow, and requiring it would put a person outside the events he is living through. Someone who has never heard of a pandemic still falls ill, finds the market closed and is told what to do by someone who has; the concept is not what exposes him to it. Having the concept changes what he can do about it, not whether it reaches him.

Everyone is within the realm's flow (§4). A hearth-dweller who has heard nothing of the war is within it by two routes, neither of which hands him the flow as a fact. The first is **lived events**: matter and bodies reach him as they reach anyone (stores requisitioned, hunger, a neighbour dead), together with the acts and words of those who are aware (the tax-collector, the recruiter, the neighbour who was told), which arrive as witnessed events and told claims. The second is **grading**: the engine grades what he credits by the regime he is within (below). Neither deposits a claim in his ledger; AX-7 is kept.

**The regime is immanent.** It is made of what the flow's participants say and do and of the seats that pronounce (`determine`, `issue`, a held `dispensation`), not stored anywhere. A flow has at least two, authority's and the challengers', and each credits its own speakers: the side the study gives every move (A, R, O, N) is what separates them. The side-aware classification of §8 step 1 is therefore load-bearing here, not cosmetic.

**The engine already has the mechanism, dark.** `decision/options.py::teller_weight` grades a told claim when it is read, by the hearer's relation to the teller (rank, regard, track record) and by the retelling count; at its shipped control values (`told_weight` 1.0, all gains 0) every claim weighs 1.0 and nothing is conditioned. The four parts of a regime map onto it as follows:

| part of a regime | where it already stands |
|---|---|
| what is accepted as true | `weigh`: how far a hearer credits a claim; the noisy-OR over distinct origins |
| telling true from false | the inquiry verbs (`examine`, `interview`, `interrogate`, `research`) and `confidence.broken` |
| standing of those who pronounce | `rank(p, teller)`; the seat a speaker acts through |
| what is valued | the verbs a seat can form and the remits it holds |

The proposed addition is one term in `relation`: the teller's standing in the flow `p` is within, which sets whether `p` credits him more or less. It reads the world reading, not `p`'s ledger, so it binds an unaware `p` as it binds an aware one. It is a **second step**, after the stamp (§5) is measured, for three reasons: it reorders every told claim in the loop and so moves the hash widely; its effect cannot be told apart from the stamp's until the stamp is measured alone; and AX-2 binds `decision/`, so the flow's standing must arrive there as data (as `fx` and the stamped questions do), never as a read of the World. `layer-conformance` Lens B settles that placement before any code.

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
| execution of a held person (XE) | **a design choice, Jordan's if no precedent answers it**: a sentence through `determine`, or a new verb |
| declared, none seen (RF, RG, CL, NG, CA, AM, DA, XN) | the aperture funnel per verb first (which clause refuses it); change nothing before that |
| a later rising linked to this case (XP) | read by `flows_known` itself; no verb |
| **a terminus from every opening** | for each opening kind and each of the six classes in §4, an act route exists whose last move is terminal. Where none does the flow can never conclude and holds its slot for good: the realm's single slot is the worst case. This is a requirement of the loop, checked by the instrument (§8 step 1) |

## 8. Build order, each with its falsifier

1. **Instrument, side-aware** (no hash change). Classify by act, add the 16 links and the leave-and-rejoin profile. Control: the same log with moves shuffled within each case must complete the links no more often than chance. Falsifier: a planted log that completes a known link must read as completing it. Add the terminus check: for each opening kind, run seeds forward and report which of the six classes any flow reached; a class never reached over several seeds is a finding about default play, not proof of absence, and the same run at more seeds is its control.
2. **Gaps in §7**, each through its own existing position, each a hash mover declared as such.
3. **`flows_known`** as a pure query with no consumer. Falsifiers: a witness and a hearsay holder of the same events read different flows; a person with an empty ledger reads none; two realm-wide flows planted in one ledger read as one realm flow with the second inside it; the same ledger with a terminal claim added reads the flow as concluded and frees the realm slot; a ledger with the claim missing still reads it open; a person within the realm flow whose ledger holds none of its moves reads no realm flow (he can place none), yet the world reading lists him as within it, and the §5a credit term (when built) grades his told claims by it.
4. **The stamp** in `questions_for`, switch shipped off. Control: switch off reproduces the base hash. Guard of §0: over the same seeds, the set of concluding classes reached with the stamp on contains the set reached with it off, and the number of distinct classes reached does not fall. Measure: the stamp changes which verbs form for a person in a held flow, and the `confer` and `oblige` counts CR-49 watches do not fall to 0.
5. **Deck**: world-build seeds per category through the CL-EVENTS commit (3) schema, measured by step 1.

## Needs Jordan

1. Capacities for the rungs below the duchy: territory, settlement, community, hearth and person (§4). Realm 1 and duchy 2 are ruled; nothing else depends on the others' values.
2. The terminal moves (§4): confirm or change the six classes, and which moves show each. Nothing is built on a class until this is answered.
3. Execution (§7): a `determine` sentence or a new verb.
4. Whether the credit term of §5a is a second step as proposed or part of the first build.
