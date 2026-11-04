# Strife flows: every strife move reachable, and a person's reading of the flows around them

## Status: PROPOSED (2026-11-04), HELD BACK IN FULL. Reference under CLAUDE.md §0.05, not a mechanism; merging this file ratifies nothing and applies no ED-1094 default.
## Lane: IN

Source: the study "Mechanics of Strife to c. 1600" (102 cases, nine filing categories A to I, 40 move codes, 16 recurring links; claude.ai artifact XDjCCRvbxiPS6sumpRtnte). Jordan's rulings of 2026-11-04, in conversation: outcomes must be possible, never triggered; the flows are a meta-narrative that conditions how people choose; they begin from events that arise in play (taxes raised, drought then famine, a succession crisis); too many live strifes would be illegible to a player, so new events fold into existing flows.

What this adds to `engine/season/`: one pure query module (`queries/situation_q.py`), one roster of knobs in `rosters.yaml`, one stamp in `questions_for`. Nothing is stored, no step is added, no clock runs.

---

## 1. What the study licenses

A space of chains, not a script. Cases share 40 moves and 16 recurring links, spend about a quarter of their moves on those links, and leave and rejoin them constantly; 93 of 102 end off the links. Categories differ in how they open and how they end, and in almost nothing between (only A's natural shock and B's death, regime change and claim are distinctive, and those are what the labels name). So: **a flow is an open chain of moves around shared referents; its category is only the kind of event that opened it.** Membership must not require the 16 links, or a detour would end a flow.

## 2. Two readings, and where each may be read

| reading | over | read by | AX |
|---|---|---|---|
| **world reading** `flows_in(log)` | the whole Event log | the harness and the port's debug views only | an instrument, never an input to any person |
| **person reading** `flows_known(w, p)` | `p.ledger` alone: claims `p` witnessed or was told | `questions_for`, so the person's choices | AX-7: a character has a reading of the world, never the world |

Both are pure functions: same input, same output, nothing written. The person reading is the design. The world reading exists so the instrument can check the person reading against what happened.

## 3. How a flow is read

A **move** is a ledger claim whose Event kind and act classify to one of the 40 codes (`strife_moves.yaml`, to be made side-aware by classifying on the act: verb, degree, and the actor's faction against the holder of the rung). Non-strife claims never join a flow.

A **flow** is a maximal set of moves linked by shared referents, with referents compared through the rung ladder (`ancestry`, `place_of`, `holder_faction_of`): two moves are linked if their referents are the same, or one is an ancestor of the other, or they share a faction. It sits at the lowest rung that covers its moves, so a flow zooms: a hearth's grain dispute is a flow at the hearth; when its referents join others' under one territory it is read at the territory.

Its **opening kind** is the category of the oldest move in it:

| opening, as it arises | read from | exists today |
|---|---|---|
| tax or levy raised (C) | `dispensation.issued`, `requisition.taken`, `duty.taken` | yes: 401 events over seeds 0 and 1 at 4 seasons |
| shortage, then famine (A) | a settlement's hunger band; a yield below its floor | hunger is read (`hunger_by_settlement`) and whether it binds rests on CR-22 (B10-18; status not checked); the shock that causes it is dark (`season_factor_draw` ships `()`) |
| succession crisis (B) | a seat emptied by `person.died`, then `succeed` or a rival claim | deaths occur (15 over seeds 0 and 1 at 4 seasons); no natural death (`age_step`, `illness_rate` are 0.0); rival claims 0 observed, cause not yet found |
| army unpaid (H) | a levy that does not reach its troops | source not yet located |
| burden on a subject people, foreign rule, religious or status grievance (D, E, F, G, I) | the same moves, opened by a foreign actor or a church or caste seat | foreign off; no church seat issues sanctions |

Opening conditions are read off state the loop already holds; nothing fires on them.

## 4. Folding, and the limit

The limit sits on the person, not the world. A world-level cap would be an omniscient narrator suppressing events; a person's attention is limited by being a person.

- `flows_known(w, p)` returns flows ranked by salience to `p` by the order `attention_key` already uses (own ambition and need, then office, then conviction).
- `p` holds at most `K` of them in mind. A flow beyond the `K`th **folds upward**: merged into the known flow at the nearest ancestor rung that covers it, else left in the ledger as ordinary claims. Nothing is deleted. The event still happened; the person has not placed it in a larger picture.
- A flow with no new move in `T` seasons is no longer active in `p`'s reading. The study ends 93 of 102 cases without a closing move, so retiring by quiet is the case, not the exception.
- `K` and `T` are roster values in `rosters.yaml`, `[ASSUMPTION; medium; Jordan to correct; revert: delete the stamp and the roster rows]`, with **no value proposed here**. `T` can be measured from the dates in the 102 dossiers; `K` is a legibility choice and is Jordan's.

Because a witness and a person who was only told hold different claims, they read different flows from the same events. That is deliberate.

## 5. How it conditions choice

No new channel. `questions_for` already stamps standing occasions onto a person's first question as classed referents: vacancies, writs held, places named, larders in purview (`_stamped`). `flows_known` adds one more stamp: the rungs, persons and offices at stake in each held flow, as referents of the existing closed classes (`Office, Record, Rung, Site, Proposition, Person`). No `Flow` class is added.

Effect: a person aware of a rising at his settlement finds that rung and its holder among his occasions, ranked by `attention_key`, so verbs form on them (`march`, `petition`, `migrate`, `arrest`, `commit`) and each is chosen by his own convictions as now. Two people in one flow choose differently; none is told what the flow does next.

The flow's opening kind and last move are not read by any chooser in this design. Whether they should weight options (fear on a quiet rung, hope on a petition) is a second step, after the stamp is measured.

## 6. What it refuses

- No stored flow, state, phase or counter (T-a; ED-IN-0225: no arc carrier). Recomputed from claims each time.
- No date, deadline, firing condition or outcome on anything (T-c, M16(b)). A flow has no next move.
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

## 8. Build order, each with its falsifier

1. **Instrument, side-aware** (no hash change). Classify by act, add the 16 links and the leave-and-rejoin profile. Control: the same log with moves shuffled within each case must complete the links no more often than chance. Falsifier: a planted log that completes a known link must read as completing it.
2. **Gaps in §7**, each through its own existing position, each a hash mover declared as such.
3. **`flows_known`** as a pure query with no consumer. Falsifier: a witness and a hearsay holder of the same events read different flows; a person with an empty ledger reads none.
4. **The stamp** in `questions_for`, switch shipped off. Control: switch off reproduces the base hash. Measure: the stamp changes which verbs form for a person in a held flow, and the `confer` and `oblige` counts CR-49 watches do not fall to 0.
5. **Deck**: world-build seeds per category through the CL-EVENTS commit (3) schema, measured by step 1.

## Needs Jordan

1. `K` and `T` (§4). Nothing else in the design depends on their values.
2. Execution (§7): a `determine` sentence or a new verb.
