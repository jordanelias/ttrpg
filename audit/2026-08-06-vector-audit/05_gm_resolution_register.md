# "GM Decides" Resolution Register — populated

## Status: PROPOSED (ED-IN-0148, 2026-08-06)

**This file populates the register that `systems/_architecture/videogame_mode_spec.md` §3 specifies
and leaves empty.** That section defines five resolution types and then says:

> "This register is **not exhaustive here**. Each design doc should be audited for 'GM' references
> and resolved per the above types during Godot extraction."

That audit had never been run. This is it. The trigger was Mode G of the 2026-08-06 vector audit
(`02_weakness_register.md`), which surfaced "Game Master" as the top vocabulary-debt term — 70
occurrences in 20 docs by the audit's own corpus, **84 across 22 files** by direct grep over
`systems/ canon/ engine/ godot/ proposals/`.

**Why this matters beyond hygiene.** `CLAUDE.md` opens with *"There is no GM — the engine resolves
everything."* Every unresolved row below is a decision the engine must make that no document says
how to make. These are not stylistic leftovers; they are unimplemented resolvers, and the Godot port
walks into each one.

---

## Method, and what would falsify this

Source set: `grep -rin 'game master'` over `systems/ canon/ engine/ godot/ proposals/` →
84 occurrences / 22 files, captured verbatim at `data/gm_occurrences_raw.txt`. Every row below is
traceable to `file:line` in that capture and was read in full context, not classified from the
grep line.

**17 occurrences in `systems/threadwork/threadwork_v25_historical.md` are excluded** — it is a
superseded historical doc (`_v25` against a live `_v30` head), and `videogame_mode_spec.md` §4
formally discards "Mode-split file naming... Deprecated. Historical only." That leaves **67 live
occurrences across 21 files**, every one of which is dispositioned below.

**Falsifier:** if any row classified DISCARD or ALREADY-RULED turns out to gate a mechanic the
engine must implement, this register is wrong in the direction that matters (it would under-report
the port's obligations). The rows most exposed to that are the four §4 mode-table rows in
`campaign_modes_v30.md` — flagged inline. Counts are reproducible by re-running the grep; the
classification is a judgment call and is marked as such per row-class.

---

## Summary

| Disposition | Rows | Meaning |
|---|---:|---|
| **A — OPEN: needs a design decision** | 30 | No rule exists. Real port-blocking work. |
| **B — RESOLVABLE: rule already in the doc** | 6 | The mechanic is fully specified; only the "GM" framing needs removing. |
| **C — ALREADY RULED by spec §1** | 12 | `"GM tracks" → **Engine tracks**` already decided; the source docs simply were never rewritten. |
| **D — DISCARD per spec §4** | 16 | TTRPG-only mode, session boundaries, BG-only, mode-comparison tables. Formally abandoned. |
| **E — not a defect** | 3 | The spec itself (×2) and one rejected option quoted inside a vetting doc. |
| **Total live** | **67** | |

**The honest headline is not "70 problems".** It is: **30 genuine open decisions**, 6 mechanical
rewrites, and 12 rows where the decision was already made and the docs lagged. Roughly half the raw
count is not work.

---

## A — OPEN: needs a design decision (30)

Ordered by port impact. Resolution-type column is the *proposed* §3 type, not a ruling.

### A1. Combat — free parameters with no formula

| # | Location | The delegation | Proposed type | Note |
|---|---|---|---|---|
| A1.1 | `systems/combat/combat_v30.md:106` | Stunt: "+N dice to Offence from environmental/positional narrative (**Game Master sets N, max 5**)" | Deterministic | **Highest severity in this register.** An unbounded-within-5 dice-pool modifier with no derivation. A combat resolver cannot ship with this open. |
| A1.2 | `systems/combat/combat_design_v1.md:111` | Identical Stunt text | Deterministic | Duplicate of A1.1 — **same rule stated twice in two docs**; resolve once, propagate. |
| A1.3 | `systems/combat/combat_v30_infill.md:44` | "The GM determines whether a physical obstacle is present in the zone" (Cover) | **Authored** | Clean fix: Cover is a property of the authored zone/map, not a judgment. |
| A1.4 | `systems/combat/combat_design_v1.md:234` | Identical Cover text | Authored | Duplicate of A1.3. |

⚠ **Currency caveat:** `CLAUDE.md` §4 records the live combat head as `systems/combat/combat_engine_v1/`, with `combat_v30.md` *PARTIALLY SUPERSEDED*. Confirm whether A1.1–A1.4 still bind before spending design effort — they may already be resolved inside the engine and merely stale in prose.

### A2. World-state consequence generation

| # | Location | The delegation | Proposed type |
|---|---|---|---|
| A2.1 | `systems/_architecture/campaign_modes_v30.md:193` | MS threshold crossing: "the GM determines a narratively appropriate consequence from the current situation. **No event deck.** The current political, social, and thread-level state should generate the threshold consequence organically." | AI-driven | 
| A2.2 | `systems/_architecture/campaign_modes_v30.md:180` + `campaign_modes_v30_infill.md:42–43` | §12.6 "The Game Master as Rendering Engine" — ontical presentation for non-sensitive characters, ontological layering for sensitive ones | Authored + engine | 
| A2.3 | `systems/world/calamity_radiation_v30.md:120` | Threadcut beings "may be indifferent, curious, or territorial — GM determines based on the being's configurational character" | Authored / AI-driven |

**A2.1 is the second-most load-bearing row here.** It explicitly forbids the easy answer ("no event
deck") and demands emergent generation from world state — which is the project's stated design
goal, stated as a GM instruction. It has no owner.

**A2.2 is not debt — it is a specified feature wearing GM clothing.** Perception layered by
character sensitivity is implementable and desirable; only the label is wrong.

### A3. Social contest format

| # | Location | The delegation | Proposed type |
|---|---|---|---|
| A3.1 | `systems/social_contest/social_contest_v30_infill.md:19` | "Exchange count, role structure, audience weight, and available actions vary by institutional context and adjudicator type. **The GM sets the format at setup**" | Authored |
| A3.2 | `systems/social_contest/social_contest_system_v2.md:36` | Identical text | Authored — duplicate of A3.1 |
| A3.3 | `systems/social_contest/social_contest_v30.md:485` | "Inquisitor death from non-player causes is a **Game Master event**" | AI-driven |

A3.1/A3.2 are a clean, high-value conversion: four format parameters keyed by institutional context
→ an authored contest-format table. This is a data deliverable, not a mechanic invention.

### A4. Faction behaviour and politics

| # | Location | The delegation | Proposed type |
|---|---|---|---|
| A4.1 | `systems/factions/factions_personal_v30_infill.md:20` | Nine political axes "are **not tracked numerically** — they are qualitative GM tools for scene generation" | AI-driven / Authored |
| A4.2 | `systems/factions/factions_personal_v30_infill.md:11` | "When a personal action has faction-level scope, the GM recognises it as a Domain Action" | Deterministic |
| A4.3 | `systems/factions/factions_personal_v30_infill.md:35` | Church seizure at CI 60: "the Church player (or GM) may attempt seizure" | AI-driven |
| A4.4 | `systems/factions/factions_personal_v30.md:165` | PC excommunication → "faction reverts to institutional tendency (GM-run)... or GM succession" | AI-driven |

**A4.1 is a structural gap, not a wording gap.** Nine named axes that drive campaign events and NPC
motivation, explicitly *not* numerically tracked, in a system with no GM to hold them qualitatively.
Either they get a representation or they are not in the game.

### A5. Threadwork

| # | Location | The delegation | Proposed type |
|---|---|---|---|
| A5.1 | `systems/threadwork/threadwork_v30_infill.md:66` | Brittleness: "the GM **may rule** it shatters into a Shifting Object at its scale rather than simply failing" | Deterministic / Default |
| A5.2 | `systems/threadwork/threadwork_v30_infill.md:43` | Leap first attempt: "The GM describes the approach and the perceptual boundary" | Authored |
| A5.3 | `systems/threadwork/threadwork_v30_infill.md:94` | Collective Diagnosis is "a shared GM exchange, not sequential individual rolls" | Default |
| A5.4 | `systems/threadwork/threadwork_v30_infill.md:124` | Dissonant-entry protocol: GM names the state to the player. "This is not a mechanical rule; it is a table protocol." | Player-facing UI |

A5.1 needs a severity threshold ("non-Thread event of sufficient severity") — currently unquantified.
A5.4 converts cleanly to a UI notification; the doc already says it carries no mechanical weight.

### A6. Hybrid / cascade

| # | Location | The delegation | Proposed type |
|---|---|---|---|
| A6.1 | `systems/_architecture/hybrid_gaps_v30_infill.md:52` | "CP award uses the same criteria as TTRPG (Belief engagement, significant Domain Action, Maxim expression). **GM adjudicates** at Cascade/seasonal accounting." | Deterministic |
| A6.2 | `systems/_architecture/hybrid_gaps_v30_infill.md:18` | NPC-only orders generate no scene — "the GM narrates the outcome so players have the information" | Deterministic + authored summary |
| A6.3 | `systems/_architecture/hybrid_gaps_v30_infill.md:39` | No-proxy faction: "The GM executes orders according to the faction's artificial intelligence algorithm" | AI-driven |
| A6.4 | `systems/_architecture/hybrid_gaps_v30_infill.md:45` | "Let the faction pass to a named NPC (GM-controlled)" | AI-driven |
| A6.5 | `systems/_architecture/campaign_modes_v30_infill.md:47` | "When a thread operation resolves, the Game Master ⟨truncated in source⟩" | Needs source repair |

A6.3/A6.4 name an AI algorithm that already exists in principle — these are near-C rows, promoted to
A only because the algorithm is referenced rather than specified here.

**A6.5 is a source defect, not just a delegation:** the sentence is incomplete in the file.

### A7. Authored NPC/world content

| # | Location | The delegation | Proposed type |
|---|---|---|---|
| A7.1 | `systems/npcs/edeyja_npc.md:20` | "Stats (approximate — exact values for **GM reference**)" | Authored |
| A7.2 | `systems/npcs/edeyja_npc.md:40` | "warden count: small (**GM's discretion** — single digits to low teens)" | Authored |
| A7.3 | `systems/npcs/edeyja_npc.md:81` | "## Game Master Notes" (section heading) | Authoring metadata — may stay |
| A7.4 | `systems/world/southernmost_v30_infill.md:31` | "The GM selects or rolls; encounters should reflect the zone type" | Authored + deterministic |
| A7.5 | `systems/world/southernmost_v30_infill.md:33` | "GM delivers a brief description of what Thread sight reveals" | Authored |

These are content-authoring obligations, not rule design. Cheapest tier of the OPEN set.

---

## B — RESOLVABLE: the rule is already in the doc (6)

Each of these states a complete mechanic and *then* attributes it to a GM. The engine performs the
stated operation; only the attribution is removed. **No design decision required.**

| # | Location | Rule as written | Action |
|---|---|---|---|
| B1 | `systems/world/worldbuilding_v30.md:117` | "GM **rolls Riskbreaker Intel vs Ob 2**. Success: comply. Failure: refuse or sabotage." | Engine rolls. |
| B2 | `systems/factions/factions_personal_v30_infill.md:12` | "GM **rolls the relevant faction stat as a dice pool (d10s, TN 7) against the Domain Ob**. For contested actions, both roll; higher net successes wins. Ties go to the defender." | Engine rolls. Fully specified. |
| B3 | `systems/world/calamity_radiation_v30.md:126` | "the GM (or facilitator) **performs one lookup per territory: current MS band × Proximity Rating → instability state from the radiation matrix**" | Engine performs lookup. Table exists. |
| B4 | `systems/threadwork/threadwork_v30_infill.md:69` | "The GM determines which states revert **based on their causal source** — physical-fact-triggered states revert..." | The causal rule is stated in the same paragraph. Engine applies it. |
| B5 | `systems/world/worldbuilding_v30_infill.md:53` | "One Ministry (GM choice **or random**) ceases to function for 1 season" | Take the random branch. |
| B6 | `systems/combat/combat_v30.md:242` | "targets the *single most-adjacent* friendly actor (**GM arbitration if multiple equidistant**)" | Needs only a deterministic tie-break (seeded random or lowest-index). |

---

## C — ALREADY RULED by spec §1 (12)

`videogame_mode_spec.md` §1.4 already carries the row:

> `| "GM tracks" entries | **Engine tracks.** All "Game Master tracks" items become engine-tracked state. | — |`

and §2 restates it: *"No 'GM tracks' — the engine IS the GM."* **The decision exists.** These rows
are documentation lag: the source docs were never rewritten to match. No new ruling needed; this is
a mechanical sweep.

| Location | Tracked state |
|---|---|
| `systems/world/worldbuilding_v30.md:49` | Jarnstal Drift (0–3, "GM-tracked, private") |
| `systems/world/worldbuilding_v30_infill.md:20` | Jarnstal Independence Counter — **already gives the operational trigger** |
| `systems/factions/factions_personal_v30_infill.md:74` | Löwenritter Autonomy (0–3, "private") |
| `systems/mass_battle/mass_battle_v30_infill.md:37` | Shifting Object status for post-battle Thread consequences |
| `systems/_architecture/hybrid_gaps_v30_infill.md:16` | Cascade consequence ledger |
| `systems/_architecture/hybrid_gaps_v30_infill.md:33` | Cascade phase sequencing |
| `systems/_architecture/hybrid_gaps_v30_infill.md:34` | Domain Echoes application from ledger |
| `systems/_architecture/hybrid_gaps_v30_infill.md:35` | Board state update |
| `systems/_architecture/hybrid_gaps_v30.md:51` | Faction stat change → personal consequence |
| `systems/_architecture/hybrid_gaps_v30.md:52` | NPC action → personal character impact |
| `systems/_architecture/hybrid_gaps_v30.md:53` | Clock threshold → institutional response queueing |
| `systems/_architecture/hybrid_gaps_v30.md:69` | Thread clock/tracker effects batched to Cascade |

---

## D — DISCARD per spec §4 (16)

`videogame_mode_spec.md` §4 formally abandons: TTRPG-only mode, BG-only mode, mode switching,
session boundaries, GM adjudication, and physical components. These rows fall entirely inside that.

| Location | Why discarded |
|---|---|
| `systems/combat/combat_v30.md:250` | Explicitly labelled "**Tabletop fallback**" |
| `systems/combat/combat_v30.md:378` | Explicitly labelled "**Tabletop fallback**" |
| `systems/world/worldbuilding_v30_infill.md:48` | Explicitly "**TTRPG only**" |
| `systems/world/worldbuilding_v30_infill.md:36` | "If a TTRPG scenario requires..." |
| `systems/factions/factions_personal_v30.md:392` | "**Board game representation**... GM-driven" |
| `systems/_architecture/campaign_modes_v30.md:42` | Endgame indicators — session boundaries; victory is owned by `systems/victory/victory_v30.md` |
| `systems/_architecture/campaign_modes_v30_infill.md:14` | "campaign ends when the GM and players agree" — session boundaries |
| `systems/_architecture/campaign_modes_v30_infill.md:15` | "signal endgame 2–3 sessions before" — session boundaries |
| `systems/_architecture/campaign_modes_v30_infill.md:23` | "GM may compress" a session |
| `systems/_architecture/campaign_modes_v30_infill.md:24` | "GM may expand" across 2 sessions |
| `systems/_architecture/campaign_modes_v30.md:149` | Mode-comparison table row — §1 rules "**Collapse to single column**" |
| `systems/_architecture/campaign_modes_v30.md:174` | Mode-comparison table row — same |
| `systems/_architecture/hybrid_gaps_v30.md:41` | "GM judges... simple enough to track inline. This is a GM call, **not a player option**" — the batching default stands; the exception is a table convenience |
| `systems/_architecture/hybrid_gaps_v30.md:136` | G-080 gap-ledger row recording a past TTRPG resolution |
| `systems/_architecture/hybrid_gaps_v30.md:143` | G-094 gap-ledger row recording a past TTRPG resolution |
| `systems/threadwork/threadwork_v30_infill.md:67` | "the GM **should ask**..." — table advice, carries no mechanic |

⚠ **The four `campaign_modes_v30.md` rows (42/149/174) and the two gap-ledger rows (136/143) are the
weakest classifications in this register.** They are discarded because they sit inside mode-comparison
tables or historical resolution logs — but a reader could reasonably argue rows 149 and 174 encode
live strategic/personal-phase behaviour. Flagged rather than buried.

---

## E — not a defect (3)

| Location | Why |
|---|---|
| `systems/_architecture/videogame_mode_spec.md:81` | This *is* the §1 ruling row |
| `systems/_architecture/videogame_mode_spec.md:161` | This *is* the §3 register definition |
| `systems/characters/conviction_track_v1_pp718_vetting.md:29` | Quotes "(b) rely on GM adjudication" as a **rejected** option in an explicit either/or, and rejects it |

---

## Two other struck terms from Mode G (not triaged here)

The vector audit surfaced two further vocabulary-debt terms. They are recorded for completeness and
**not** dispositioned by this register:

- **Coup Counter** — 46 occurrences in 19 docs (top: `systems/_architecture/early_game_ignition_analysis.md`)
- **Cultural Reformation** — 24 occurrences in 10 docs (top: `systems/overview/peninsular_strain_v30.md`)

---

## Recommended sequence

1. **C (12 rows)** — mechanical sweep, no decision. Rewrite "GM tracks" → engine-tracked state.
2. **B (6 rows)** — mechanical rewrite, no decision. Strip the attribution; the rule stays.
3. **A1 currency check** — confirm whether `combat_v30.md` still binds before designing A1.1/A1.2.
4. **A3.1 + A4.1 + A2.1** — the three highest-value open decisions (contest format table, nine-axis
   representation, MS threshold consequence generation). Each is a design call, not a rewrite.
5. **A7 (5 rows)** — content authoring, parallelisable, no dependencies.

Steps 1–2 remove **18 of 67 rows with zero design risk**, which is the cheapest way to make the
remaining signal legible.

**Nothing in this register has been executed.** No source doc was edited by this audit.

---

## Appendix — itemized: all 67 live rows

Every live occurrence, numbered, grouped by disposition then file. Each row is traceable to
`file:line` in `data/gm_occurrences_raw.txt`. Quoted text is verbatim from the source, trimmed
for width. **Resolution types in group A are PROPOSED, not rulings.**


### A — OPEN — needs a design decision (30)

| # | Location | Delegation (verbatim) | Proposed type | Note |
|---:|---|---|---|---|
| 1 | `systems/_architecture/campaign_modes_v30.md:180` | ## 12.6 The Game Master as Rendering Engine | Authored + engine | §12.6 heading. The perception-layer feature, not debt — only the label is wrong. |
| 2 | `systems/_architecture/campaign_modes_v30.md:193` | When Mending Stability crosses a threshold (downward), the Game Master determines a narratively appropriate consequence from the current situation. No event deck. The current political, social, and thread-level state of the world should generate the threshold consequence organically. See §5.4.3 for the full Mending Stability threshold table. | AI-driven | Explicitly forbids an event deck and demands emergent generation from world state. No owner. |
| 3 | `systems/_architecture/campaign_modes_v30_infill.md:42` | ## 12.6 The Game Master as Rendering Engine | Authored + engine | §12.6 body. |
| 4 | `systems/_architecture/campaign_modes_v30_infill.md:43` | For non-sensitive characters, the Game Master presents the ontical world — things as they appear. For sensitive characters, the Game Master layers ontological information beneath the ontical presentation: faint thread-structures visible beneath surfaces, distortions around monstrous presences, warmth or tension at knot-points. | Authored + engine | Ontical vs ontological presentation by character sensitivity — implementable feature. |
| 5 | `systems/_architecture/campaign_modes_v30_infill.md:47` | When a thread operation resolves, the Game Master: | Needs source repair | THE SENTENCE IS INCOMPLETE IN THE FILE. Source defect, not just a delegation. |
| 6 | `systems/_architecture/hybrid_gaps_v30_infill.md:18` | **Zoom In is for player-involved interactions only.** Any order that resolves entirely between NPCs (no Player Character present) does not generate a TTRPG scene — the Game Master narrates the outcome so players have the information for their next scene. | Deterministic + authored | NPC-only resolution plus outcome summary generation. |
| 7 | `systems/_architecture/hybrid_gaps_v30_infill.md:39` | If **no Player Character can proxy**: the faction runs on Non-Player Character artificial intelligence logic for the duration. The Game Master executes orders according to the faction's artificial intelligence algorithm (as established in the board game Non-Player Character rules). The faction leader Player Character may send one instruction per season (a Belief-level directive) which the artifici … | AI-driven | Names a faction AI algorithm that is referenced rather than specified here. |
| 8 | `systems/_architecture/hybrid_gaps_v30_infill.md:45` | 3. **Let the faction pass to a named Non-Player Character** (Game Master-controlled). The dying player creates a new personal character unaffiliated with that faction. | AI-driven | Faction passes to a named NPC. |
| 9 | `systems/_architecture/hybrid_gaps_v30_infill.md:52` | Board game successes generate CP and personal advancement. The character performed those actions; the zoom level does not affect whether the experience counts. CP award uses the same criteria as TTRPG (Belief engagement, significant Domain Action, Maxim expression). Game Master adjudicates at Cascade/seasonal accounting. | Deterministic | CP criteria are listed; needs a formula. |
| 10 | `systems/combat/combat_design_v1.md:111` | \| Stunt \| Declared with Strike. +N dice to Offence from environmental/positional narrative (Game Master sets N, max 5). Chain dice (10s) chain normally, independent of Stunt effect. \| | Deterministic | Duplicate of #1 — same rule stated in two docs. |
| 11 | `systems/combat/combat_design_v1.md:234` | Cover must be declared in Phase 1 (Movement) to take effect. Cover does not move with the defender. The Game Master determines whether a physical obstacle is present in the zone. A character who does not declare Cover in Phase 1 receives no DR benefit that round, even if physically behind an obstacle. [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit] | Authored | Duplicate of #5. |
| 12 | `systems/combat/combat_v30.md:106` | \| Stunt \| Declared with Strike. +N dice to Offence from environmental/positional narrative (Game Master sets N, max 5). Chain dice (10s) chain normally, independent of Stunt effect. \| | Deterministic | Unbounded-within-5 dice-pool modifier with no derivation. Highest severity in the register. |
| 13 | `systems/combat/combat_v30_infill.md:44` | Cover must be declared in Phase 1 (Movement) to take effect. Cover does not move with the defender. The Game Master determines whether a physical obstacle is present in the zone. A character who does not declare Cover in Phase 1 receives no DR benefit that round, even if physically behind an obstacle. [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit] | Authored | Cover is a property of the authored zone, not a judgment. |
| 14 | `systems/factions/factions_personal_v30.md:165` | **Player Character excommunication — faction succession (PP-244):** If the excommunicated target is a PC faction leader, the faction reverts to institutional tendency (Game Master-run) until: (a) the PC is reinstated via Reversal above, or (b) a replacement leader is designated through narrative play (Influence Domain Action Ob 2 by any PC, or Game Master succession). | AI-driven | Institutional-tendency fallback and succession. |
| 15 | `systems/factions/factions_personal_v30_infill.md:11` | When a personal action has faction-level scope, the Game Master recognises it as a Domain Action. The personal roll resolves both the personal outcome and the faction effect simultaneously. | Deterministic | Faction-scope detection from a personal roll. |
| 16 | `systems/factions/factions_personal_v30_infill.md:20` | The nine political axes generate campaign events, Non-Player Character motivations, and faction conflicts. They are **not tracked numerically** — they are qualitative Game Master tools for scene generation. | AI-driven / Authored | STRUCTURAL GAP: nine axes driving events and NPC motivation, explicitly not numerically tracked. |
| 17 | `systems/factions/factions_personal_v30_infill.md:35` | At Church Influence 60, the Church may attempt to seize territories through institutional claim rather than military force. This is triggered once per season at seasonal accounting; the Church player (or Game Master) may attempt seizure on any number of territories, resolving each separately. | AI-driven | NPC faction AI must decide seizure attempts. |
| 18 | `systems/npcs/edeyja_npc.md:20` | ## Stats (approximate — exact values for Game Master reference) | Authored | Needs concrete authored values. |
| 19 | `systems/npcs/edeyja_npc.md:40` | **Current warden count: small (Game Master's discretion — single digits to low teens). This is functionally a dying institution.** | Authored | Needs a concrete warden count. |
| 20 | `systems/npcs/edeyja_npc.md:81` | ## Game Master Notes | Authoring metadata | Section heading — may legitimately stay as authoring notes. |
| 21 | `systems/social_contest/social_contest_system_v2.md:36` | The contest system does not have a fixed format. Exchange count, role structure, audience weight, and available actions vary by institutional context and adjudicator type. The Game Master (GM) sets the format at setup; players know it before the contest begins. | Authored | Duplicate of #52. |
| 22 | `systems/social_contest/social_contest_v30.md:485` | - Pursue Inquisitor reassignment / death by political maneuver (Niflhel-broker assassination is hypothetically available but radically undermines the player's Conviction; Inquisitor death from non-player causes is a Game Master event). | AI-driven | World-sim event. |
| 23 | `systems/social_contest/social_contest_v30_infill.md:19` | The contest system does not have a fixed format. Exchange count, role structure, audience weight, and available actions vary by institutional context and adjudicator type. The Game Master (GM) sets the format at setup; players know it before the contest begins. | Authored | Four format parameters keyed by institutional context → an authored table. High value, data deliverable. |
| 24 | `systems/threadwork/threadwork_v30_infill.md:43` | The first time a character attempts the Leap, it is run as a full event scene. The Game Master describes the approach and the perceptual boundary. | Authored | Leap scene content. |
| 25 | `systems/threadwork/threadwork_v30_infill.md:66` | **Game Master sidebar — Brittleness in volatile contexts:** Weaving at Relational+ scale stabilises a configuration but makes it rigid. A Woven diplomatic agreement, stabilised faction, or reinforced institution cannot adapt to stress the way an unworked configuration can. If a non-Thread event of sufficient severity strikes a Woven configuration — a siege, betrayal, institutional collapse — the G … | Deterministic / Default | Needs a severity threshold — "sufficient severity" is unquantified. |
| 26 | `systems/threadwork/threadwork_v30_infill.md:94` | **Collective Diagnosis:** Multiple practitioners may Diagnose in the same round as part of collective preparation. This is a shared Game Master exchange, not sequential individual rolls — all practitioners listen to the same description of the target configuration and set their intentionality together. | Default | Collective Diagnosis resolution mode. |
| 27 | `systems/threadwork/threadwork_v30_infill.md:124` | **Game Master protocol — Dissonant entry:** When a practitioner's Coherence drops to 7 (entering Dissonant), the Game Master names this to the player explicitly: "Your Coherence is now 7 — Dissonant. Each operation at Relational+ scale costs −1 Coherence. At this pace, Fragmented is [N] operations away." This is not a mechanical rule; it is a table protocol. The practitioner's rendering is still s … | Player-facing UI | Doc already says it carries no mechanical weight. |
| 28 | `systems/world/calamity_radiation_v30.md:120` | **Behaviour:** Threadcut beings are not hostile by default. They have no relationship to organic life's concerns. They exist. Their existence draws on the same substrate practitioners use, which is why their presence adds +Ob to Mending operations (threadwork_v25 §9.7, P-17). They may be indifferent, curious, or territorial — Game Master determines based on the being's configurational character. | Authored / AI-driven | Per-being disposition. |
| 29 | `systems/world/southernmost_v30_infill.md:31` | Encounters fire once per zone during Exploration (Season 2). The Game Master selects or rolls; encounters should reflect the zone type. | Authored + deterministic | Per-zone encounter table. |
| 30 | `systems/world/southernmost_v30_infill.md:33` | **Discovery Event** (Approach, automatic): Lead practitioner perceives the boundary configurations. No roll. Game Master delivers a brief description of what Thread sight reveals at the Southernmost's edge. This scene counts as the character's first exposure for Forgetting Check purposes. | Authored | Per-POI descriptive text. |

### B — RESOLVABLE — rule already stated in the doc (6)

| # | Location | Delegation (verbatim) | Proposed type | Note |
|---:|---|---|---|---|
| 31 | `systems/combat/combat_v30.md:242` | 3. The secondary roll targets the *single most-adjacent* friendly actor (Game Master arbitration if multiple equidistant); allocates Defence per that actor's Combat Pool as normal. | Deterministic | Rule complete; needs only a tie-break for equidistant targets. |
| 32 | `systems/factions/factions_personal_v30_infill.md:12` | **Non-Player Character faction rolls:** When a faction acts without a player character driving it, the Game Master rolls the relevant faction stat as a dice pool (d10s, TN 7) against the Domain Ob. For contested actions, both roll; higher net successes wins. Ties go to the defender. | Deterministic | Formula fully stated: d10s TN 7 vs Domain Ob, contested + tie rules given. |
| 33 | `systems/threadwork/threadwork_v30_infill.md:69` | > **Past-Pull reversion (P-21):** When Past-Oriented Pulling displaces an event, mechanical states triggered by that event may or may not revert. The Game Master determines which states revert based on their causal source: - **Physical-fact-triggered states revert.** Knot strain from "external events" (territory conquest, death of a Knot entity) was caused by a physical fact. If the fact is displa … | Deterministic | The causal rule is stated in the same paragraph. |
| 34 | `systems/world/calamity_radiation_v30.md:126` | Each territory card includes a **Proximity Rating** (0–5, printed, based on node distance from Askeheim). At Accounting, the Game Master (or facilitator in competitive BG) performs one lookup per territory: current MS band × Proximity Rating → instability state from the radiation matrix. | Deterministic | Pure lookup: MS band × Proximity → matrix. Table already exists. |
| 35 | `systems/world/worldbuilding_v30.md:117` | Riskbreakers have hidden Conviction: Valoria (nation as idea). When ordered to act against this conviction: Game Master rolls Riskbreaker Intel vs Ob 2. Success: comply. Failure: refuse or sabotage. | Deterministic | Formula fully stated: Intel vs Ob 2, success/failure branches given. |
| 36 | `systems/world/worldbuilding_v30_infill.md:53` | - Effect: One Ministry (Game Master choice or random) ceases to function for 1 season. Effects by Ministry: | Deterministic | "or random" already gives the engine branch. |

### C — ALREADY RULED by spec §1 ("GM tracks" → Engine tracks) (12)

| # | Location | Delegation (verbatim) | Proposed type | Note |
|---:|---|---|---|---|
| 37 | `systems/_architecture/hybrid_gaps_v30.md:51` | \| Faction stat change → personal consequence \| Game Master narrates consequence in next Personal phase scene \| | Engine tracks | Faction stat change → personal consequence. |
| 38 | `systems/_architecture/hybrid_gaps_v30.md:52` | \| Non-Player Character action → personal character impact \| Game Master narrates; fires in correct scene sequence (see G-081) \| | Engine tracks | NPC action → personal character impact. |
| 39 | `systems/_architecture/hybrid_gaps_v30.md:53` | \| Clock threshold → institutional response \| Fires in Cascade step 3; Game Master queues response for next Personal phase \| | Engine tracks | Clock threshold → institutional response queueing. |
| 40 | `systems/_architecture/hybrid_gaps_v30.md:69` | Personal-scale Thread operations performed during the Personal phase resolve as TTRPG narrative consequences. Their clock and tracker effects (Thread Tension, ThS, Coherence, co-movement) are noted by the Game Master and batched to the Cascade phase. | Engine tracks | Thread clock/tracker effects batched to Cascade. |
| 41 | `systems/_architecture/hybrid_gaps_v30_infill.md:16` | Default: all TTRPG personal-scene consequences batch to the **Cascade phase** for application to the board. Game Master tracks consequences on a ledger during the Personal phase and applies them in bulk. | Engine tracks | Cascade consequence ledger. |
| 42 | `systems/_architecture/hybrid_gaps_v30_infill.md:33` | The Cascade phase is Game Master-controlled accounting. Players do not take actions during it. The Game Master works through the following steps in order: | Engine tracks | Cascade phase sequencing. |
| 43 | `systems/_architecture/hybrid_gaps_v30_infill.md:34` | 1. **Domain Echoes** — apply all TTRPG personal-scene consequences from the Game Master ledger to faction stats on the board. | Engine tracks | Domain Echoes application from ledger. |
| 44 | `systems/_architecture/hybrid_gaps_v30_infill.md:35` | 5. **Board state update** — Game Master physically updates the board to reflect all of the above. This is the final state players see at the start of the next Strategic phase. | Engine tracks | Board state update. |
| 45 | `systems/factions/factions_personal_v30_infill.md:74` | **Coup Threshold:** Grandmaster Ehrenwall is keeping count. The Game Master tracks a private Löwenritter Autonomy (0–3). When it reaches 3, the Split fires at the next seasonal accounting. | Engine tracks | Löwenritter Autonomy (0–3, private). |
| 46 | `systems/mass_battle/mass_battle_v30_infill.md:37` | > **Clarification:** "A Woven unit configuration that shatters (Size loss in a single turn > current Discipline) does not become a Shifting Object during the battle. For the remainder of the battle, it fights at Line formation, Discipline 1. The Shifting Object status is registered for post-battle Thread consequences — the Game Master tracks this and applies it in the narrative aftermath. This pre … | Engine tracks | Shifting Object status for post-battle Thread consequences. |
| 47 | `systems/world/worldbuilding_v30.md:49` | **Jarnstal Drift (0–3, Game Master-tracked, private):** Increments each season Jarnstal deploys Templars without Holy See authorisation. At 3: Church Military controlled by Jarnstal, not the Confessor. Church Stability −2, Church Influence (CI) +2. | Engine tracks | Jarnstal Drift (0–3, "GM-tracked, private"). |
| 48 | `systems/world/worldbuilding_v30_infill.md:20` | - Trigger: Jarnstal Independence Counter reaches 3 (Game Master-tracked; increments when Church Military is deployed without explicit Confessor authorisation — operationally, when Church plays a Military card in a territory where Confessor token is absent). | Engine tracks | Already gives the operational trigger. |

### D — DISCARD per spec §4 (16)

| # | Location | Delegation (verbatim) | Proposed type | Note |
|---:|---|---|---|---|
| 49 | `systems/_architecture/campaign_modes_v30.md:42` | **Endgame indicators (Game Master guidance — not triggers):** | — | Session boundaries; endgame is owned by systems/victory/victory_v30.md. |
| 50 | `systems/_architecture/campaign_modes_v30.md:149` | \| Domain Actions \| Implicit — Game Master recognises faction-scope from personal roll \| Explicit — Order Set with placement and resolution \| Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes \| | — | Mode-comparison table row; §1 rules "collapse to single column". WEAK CLASSIFICATION. |
| 51 | `systems/_architecture/campaign_modes_v30.md:174` | \| Threshold events \| Game Master narrates and runs scenes \| Event card or table lookup \| Board game trigger; Game Master may run TTRPG scene for narratively significant thresholds \| | — | Mode-comparison table row. WEAK CLASSIFICATION. |
| 52 | `systems/_architecture/campaign_modes_v30_infill.md:14` | There is no explicit victory condition. The TTRPG campaign ends when the Game Master and players agree the central dramatic questions have been resolved or exhausted. Endgame is emergent, not mechanical. | — | Session boundaries. |
| 53 | `systems/_architecture/campaign_modes_v30_infill.md:15` | The Game Master should signal endgame 2–3 sessions before the final session: *"We're approaching the end of this story. What does your character want to resolve?"* | — | Session boundaries. |
| 54 | `systems/_architecture/campaign_modes_v30_infill.md:23` | **Game Master may compress:** Skip Personal Phase for a season when no TTRPG scenes are dramatically necessary. Announce "quiet season" — resolve Strategic + Cascade only (~30 min). | — | Session boundaries. |
| 55 | `systems/_architecture/campaign_modes_v30_infill.md:24` | **Game Master may expand:** Split one season across 2 sessions when TTRPG scenes demand it (siege, expedition, major social confrontation). Strategic Phase deferred to session 2. | — | Session boundaries. |
| 56 | `systems/_architecture/hybrid_gaps_v30.md:41` | Exception: if the Game Master judges a consequence is simple enough to track inline (single stat change, no threshold risk), they may apply it immediately. This is a Game Master call, not a player option. | — | The batching default stands; the inline exception is a table convenience. |
| 57 | `systems/_architecture/hybrid_gaps_v30.md:136` | \| G-080 \| Resolved \| Batch to Cascade; Game Master ledger; inline exception at Game Master discretion \| | — | G-080 gap-ledger row recording a past TTRPG resolution. WEAK CLASSIFICATION. |
| 58 | `systems/_architecture/hybrid_gaps_v30.md:143` | \| G-094 \| Resolved \| 5-step Cascade sequence; Game Master-only; not skippable \| | — | G-094 gap-ledger row recording a past TTRPG resolution. WEAK CLASSIFICATION. |
| 59 | `systems/combat/combat_v30.md:250` | **Tabletop fallback.** Game Master may waive the secondary roll for cinematic clarity if the table prefers simpler resolution (declare narrative miss, no friendly damage). The mechanic is intentionally light-touch — it surfaces tactical risk without bookkeeping ceiling. | — | Explicitly labelled "Tabletop fallback". |
| 60 | `systems/combat/combat_v30.md:378` | **Tabletop fallback.** Game Master narrates the encounter as fixed-position regardless of UI mode. The B-mode flag is a videogame-specific UX optimization; tabletop doesn't need it. The flag is documented here to ensure videogame implementation has a well-defined trigger criterion rather than designer-by-designer judgment. | — | Explicitly labelled "Tabletop fallback". |
| 61 | `systems/factions/factions_personal_v30.md:392` | **Board game representation:** Territory 15. Modifies Trade orders. Game Master-driven. | — | "Board game representation" — BG-only mode, discarded by §4. |
| 62 | `systems/threadwork/threadwork_v30_infill.md:67` | Before Weaving in a politically volatile context, the Game Master should ask: is this configuration likely to face severe stress before it can be Pulled or allowed to expire naturally? If yes, Weaving may be counterproductive. The practitioner cannot know this during Diagnosis — brittleness is a consequence of over-actualisation that manifests only when external stress arrives. | — | "The GM should ask…" — table advice, carries no mechanic. |
| 63 | `systems/world/worldbuilding_v30_infill.md:36` | **CUT.** The lore fact (Crown can raise 2/3 of vassal/Church levies) is already reflected in starting Military stats. Crown Military 4 already incorporates levy access. Löwenritter Military 5 is the professional core. No standalone levy mechanic needed. If a TTRPG scenario requires requisitioning Church troops specifically, the Game Master resolves it as a standard Domain Action. | — | "If a TTRPG scenario requires…". |
| 64 | `systems/world/worldbuilding_v30_infill.md:48` | **Ducal Presence (Game Master note):** Dukes absent from Imperial Court for a full season: halved Parliamentary Influence. TTRPG only. | — | Explicitly "TTRPG only". |

### E — Not a defect (3)

| # | Location | Delegation (verbatim) | Proposed type | Note |
|---:|---|---|---|---|
| 65 | `systems/_architecture/videogame_mode_spec.md:81` | \| "GM tracks" entries \| **Engine tracks.** All "Game Master tracks" items become engine-tracked state. \| — \| | — | This IS the §1 ruling row. |
| 66 | `systems/_architecture/videogame_mode_spec.md:161` | Every instance of "GM decides," "Game Master sets scope," "Game Master determines," or similar language in the design docs must be resolved to one of: | — | This IS the §3 register definition. |
| 67 | `systems/characters/conviction_track_v1_pp718_vetting.md:29` | **N-5: What is lost without this fix?** Either (a) leave aggregate semantics in place and accept that multi-primary NPCs crisis no faster than single-primary (functionally equivalent to the structured-concentration update being silently ignored at the Scar layer), or (b) treat the spec as undefined and rely on Game Master adjudication. (a) makes PP-684's structured concentration cosmetic at the cr … | — | Quotes GM adjudication as a REJECTED option in an explicit either/or. |

**Totals:** A 30 · B 6 · C 12 · D 16 · E 3 = **67**. Raw grep returns 84; the 17-row difference
is `systems/threadwork/threadwork_v25_historical.md`, excluded as a superseded historical doc
per spec §4.
