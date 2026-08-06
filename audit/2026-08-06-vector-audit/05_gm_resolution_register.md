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
