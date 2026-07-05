# Dossier — Combinatorial Census (Lane: COMBINATORIAL CENSUS)

## Status: working record (not canonical). Author: sonnet lane, 2026-07-05.
## Question: turn Jordan's "generative churn" frame — character ambitions × world states × event
## cards × scene resolutions = thousands of live permutations and dynamic Keys, prose load
## factorizes at authored 10³-10⁴ vs rendered 10⁶+ — into GROUNDED NUMBERS, cited to file+section.

Method note per charter (`00_grounding/00_engine_charter.md` "Method rules"): working tree only;
every count cites file+section; anything not directly verifiable is tagged `[UNGROUNDED]`;
figures the task handed me as priors are treated as **unverified claims to check**, not facts —
several turned out wrong (flagged below, not silently corrected).

---

## 1. KEY SPACE

### 1.1 Key types by family

`designs/architecture/key_type_registry_v30.md` §9 "Type Count Summary" declares **7 families,
44 types total**:

| Family | Declared subtypes | Notes |
|---|---|---|
| `scene_event` (scene.*) | 10 | +Class B `scene.interaction`/`scene.gossip` (physically filed under §8, not §2) |
| `da_outcome` (da.*) | 5 | public_governance / covert_betrayal / diplomatic_alliance / antinomian_action / economic_intervention |
| `mechanical_event` (mechanical.*) | 8 | season_change / accounting / cascade_resolution / mission_shift / scene_entered / scene_exited / scene_skipped / project_advanced |
| `state_transition` (state.*) | 8 | scar_acquired / standing_change / coup_attempted / succession / project_completed / project_failed + 2 Class B relocated to §8 |
| `environmental` (env.*) | 4 | peninsular_strain_shock / crisis / disaster / population_change |
| `scene_outcome` (scene.*) | 4 (declared) / 7 (physical) | contest_resolved / battle_concluded / investigation_resolved / combat_resolved + combat_strike/combat_hit/combat_felled (physically present under §7, not counted in the §9 arithmetic) |
| `system_meta` (meta.* + relocated state.*/scene.*) | 5 (declared) / 10 (physical) | knot_formed / knot_ruptured / thread_woven / miraculous_event / legacy_event + relocated state.belief_revised, state.opinion_revised, state.concern_resolved, scene.interaction, scene.gossip |
| **Total** | **44 declared** | **48 physical `###` entries** (direct grep) |

The registry's own footnote names this a **known** drift ("master item 11 / A9," out of scope) —
not a new finding. `01_workings/dossier_content_economics.md` §1.1 independently verified the same
44-vs-48 split and further narrowed it: of the 48 physical entries, **43 list `articulation` as a
`consuming_systems:` member** (explicitly or via `[all]`); 5 do not (`mechanical.scene_skipped`,
`env.population_change`, `scene.combat_strike`, `scene.combat_hit`, `meta.legacy_event`). **Working
number: 44 declared / 48 physical / 43 articulation-relevant** — three consistent, independently
re-derived figures, not three competing guesses.

**By literal `type_id` prefix** (the task's exact ask — `scene.*`/`state.*`/`mechanical.*`/
`meta.*`/`env.*`/`da.*` — a second, independently re-derived pass, physical-entry count):

| Prefix | Count |
|---|---|
| `scene.*` | 17 (scene_event's 8 + scene_outcome's 7 physical + 2 relocated-to-§8 Class B) |
| `state.*` | 9 |
| `mechanical.*` | 8 |
| `meta.*` | 5 |
| `da.*` | 5 |
| `env.*` | 4 |
| **Total** | **48** |

Root cause of the 44→48 drift, pinned exactly: §9's `scene_outcome` row says 4 but §7 physically
holds 7 (3 original + 4 ED-935 combat-path additions — `combat_resolved/strike/hit/felled` —
never rolled into the §9 arithmetic, **undercount 3**); §9's `system_meta` row says 5 but §8
physically holds 6 net of Class-B relocations (**undercount 1**). 3+1=4, exactly reconciling
44→48.

### 1.2 Target-population axes — the task's numbers checked against source

| Claimed | Verified | Source |
|---|---|---|
| "37 settlements" | **Confirmed exactly: 37** — 35 settlements / 14 provinces / 3 duchies + 2 special-case march-targets (Himmelenger Church city-state, Schoenland foreign island) | `designs/territory/settlement_layer_v30.md` line 185, §2.1 (PP-726 corrected granularity) |
| "17 provinces" | **Confirmed as one map layer with two coexisting groupings, not 17+17.** `geography_v30.md` fixes "17 Territories" (T1–T17); `settlement_layer_v30.md §1.1` renames the same 17 nodes to "provinces" once settlements become the base civic unit. A **second, narrower "14 provinces in 3 duchies"** figure (`settlement_layer_v30.md` line 185/577) is the 17 minus the 3 non-Kingdom special-status nodes (Himmelenger Church city-state, Askeheim uninhabited Calamity wilderness, Schoenland foreign tributary) — 17 − 3 = 14. Both "17" and "14" are correct simultaneously, for different scopes (all map nodes vs. Kingdom-proper provinces). | `designs/world/geography_v30.md` L7, L58; `designs/territory/settlement_layer_v30.md` §1.1 L151, L185, L577; `designs/territory/valoria_geography_v30.yaml` `provinces:` (17 entries) |
| "4-6 factions" | **The corpus itself does not agree on a faction count — genuinely unreconciled across docs, before even reaching the "total Key-binding entities" question.** `faction_layer_v30.md:587` (playable core): Crown/Church/Hafenmark/Varfell = **4**. `faction_state_authoring_v30.md:12` ("6 canonical factions"): +Restoration Movement +Löwenritter = **6**. `references/silo_cohesion_analysis.md:72` ("seven factions"): +Guilds = **7**. My own read of `stats_1_7_scale.md`'s Starting Stats table finds **5** carrying the full 6-stat block (Crown/Church/Hafenmark/Varfell/Guilds) + 2 intentionally partial (RM, Löwenritter) + 1 explicit non-faction (Ministry) = **8** named entities total. Niflhel is formally STRUCK/dissolved (§12 D6). **No single number is "the" faction count** — it ranges 4-8 depending which doc and which definition (playable / canonical / stat-bearing / all-named-entities) you read; the task's "4-6" sits inside this range but understates the ceiling once NPC-only and partial-sheet factions are counted as legitimate Key-binding actors/targets. | `designs/provincial/faction_layer_v30.md:587`; `faction_state_authoring_v30.md:12`; `references/silo_cohesion_analysis.md:72`; `params/factions/stats_1_7_scale.md`; `faction_canon_v30.md §5.1, §11` |

### 1.3 Named NPCs

No single roster file is authoritative; three lists partially overlap:
- `designs/npcs/npc_behavior_v30.md §2` ("Named NPC Stance Triangles"): **17 entries** (§2.1-§2.17),
  several collective (Guildmaster Council, Niflhel, Cardinal Officers, Crown Inner Circle, Hafenmark
  Inner Council, Varfell Jarl Council), each carrying **~8 fixed fields** (Primary/Secondary
  Conviction, Ethical Framework, Primary/Secondary Resonant Style, Thread Sensitivity, Certainty,
  Leadership Deviation Ob).
- `designs/npcs/npc_roster_v30.md`: **13 supplementary named NPCs** (Edeyja, Maret Uln, Yrsa Vossen,
  Sæmund Haelgrund, Sigrid Torsvald, Halvar Brandt, Annika Feldhaus, Peder Almstedt, Gerik Strand,
  Dalla Virke, Doux Alexios Laskaris, Rikard Solberg, Aldric Tormann) — several already appear in
  §2's list (Edeyja, Maret Uln, Yrsa Vossen), so this is not a clean addition.
- **Tracking-capacity cap** (`npc_behavior_v30.md §11.2, §11.6`, PP-661): the peninsula supports
  **~35 named NPCs at Active tier** (soft cap; 5 tracked fields each: Disposition/PC, Availability,
  active-Duty ref, Scar count, action flag) + **~30 at Passive tier** (2 fields: Disposition,
  Availability) + **unlimited Background** (identity only, zero tracked state, §11.4). Inner-circle
  appointees are separately enumerated and structurally Active (§11.5: Crown 5, Hafenmark 4,
  Varfell 5, Church 5, Cardinals 4 = 23 — overlapping with the §2 collective entries above, not
  additive).

**Correction to the task's implicit premise: the roster is smaller than the tracking cap, not
bigger.** An independent recount of actually-named individuals across `npc_roster_v30.md` (13),
`npc_behavior_v30.md §2`'s stance-triangle entries (17, several collective), and inner-circle
appointees (§11.5's 23, heavily overlapping with §2) converges on **roughly 25-35 distinct named
individuals total** once duplicates are removed — i.e. the corpus has not yet named enough NPCs to
fill even the ~35-slot Active tier on its own; **the ~35/~30 figures are unused tracking
HEADROOM, not a census of what currently exists.** A further drift: `designs/audit/2026-04-28-
political-dynamics-session/12_development_specification.md` lines 136-137 give the Passive cap as
**~50**, not ~30 — a second, unreconciled version of the same PP-661 number living in an older
audit doc alongside the current `npc_behavior_v30.md §11.2`'s ~30.

**Working number: use ~35 (Active-tier cap) as the per-season NPC-bound multiplier** for Key-
instance-space arithmetic below — it is the tightest defensible ceiling (the actual named census,
~25-35, is close to it and NPCs get promoted into Active as needed, so cap and likely-live-population
nearly coincide); do NOT multiply by 65 (Active+Passive) for scene-eligible/state-writing Keys,
since Passive-tier NPCs are explicitly restricted to "Ceremonial scenes, Scene Slate Priority 3+
only" (§11.1) — most Key types cannot target them at all.

### 1.4 Live Key-instance space per season — worked order-of-magnitude

This is a possibility-space upper bound (what COULD exist as a distinct Key-type × binding-target
instance in one season), not the actual per-season emission count (which is much smaller — see
§4's event-deck draw-rate cross-check: `governance_play_redesign_v1.md §2.4`, "1 + ⌊Π/3⌋ cards,"
1-4/settlement/season). Binding assumptions are flagged; this is a judgment call, not a source fact.

| Family (types) | Assumed binding | Arithmetic | Order |
|---|---|---|---|
| scene_event (10) | scene-budget-bound (player_agency §4.3: 3-5 scene-actions/season) × ~3 actors/scene | 10 × 5 × 3 | ~150 |
| da_outcome (5) | faction (using 6, the mid-point of the 4-8 range in §1.2) × territory (17), upper bound | 5 × 6 × 17 | ~510 |
| mechanical_event (8) | mixed singleton (season_change, accounting) / NPC-bound (mission_shift, project_advanced) | ~4×1 + 4×35 | ~144 |
| state_transition (8) | NPC-bound, Active-tier only (scars, standing, succession, beliefs — Passive tier cannot write most of these) | 8 × 35 | ~280 |
| environmental (4) | settlement/territory-bound | 2×37 + 2×17 | ~108 |
| scene_outcome (7 physical) | scene-budget-bound, same shape as scene_event | 7 × 5 × 3 | ~105 |
| system_meta (10 physical) | NPC-dyad-bound (Knots/Bonds are relational, not per-actor) — ~2-3 active Knots/NPC × 35 NPCs ÷ 2 to de-duplicate dyads ≈ 55 active dyads | ~4 dyadic-relevant types × 55 | ~220 |
| **Total** | | | **≈1,500-1,900** |

**Independent cross-check**: a second, separately-run pass (different family/population
bucketing — NPC-bound 28 types × 35 Active-tier, faction-bound 9 types × 6 factions, settlement/
territory-bound 5 types × 37, singleton 3 types × 1) landed at **≈1,222**. Two independently
derived estimates (~1,500-1,900 and ~1,222) **converge on the same order of magnitude — low
thousands, 10³** — despite using different bucketing schemes and slightly different population
assumptions. That convergence is the actual finding, not either point estimate.

**Verdict: the live Key-instance space per season is order 10³ (roughly 1,200-2,000), not 10⁶.**
This is the mechanical/state substrate layer — it is ONE input multiplier into the render-space
combinatorics of §4, not the render space itself. Conflating "thousands of live Key-instances"
with "millions of rendered permutations" is exactly the trap the render stack must NOT fall into
(see §4). [UNGROUNDED beyond the cited per-axis counts: the binding-cardinality assumptions in the
"Assumed binding" column are judgment calls, not sourced — a different plausible assumption set
could move either estimate 2-3x in either direction without changing the order of magnitude.]

---

## 2. STATE-GRAPH SUBSTRATE

Full detail in the companion research pass; recap table:

| Variable class | Count | Source |
|---|---|---|
| Clocks/tracks, all tables in the registry | **53** rows (Shared Clocks 4, Faction-Specific Tracks 7, Faction Stats in-registry copy 6, Reputation/Standing 2, Per-Territory 6, Personal Tracks 10, Contest 1, NPC-Specific 2, Fieldwork 4, Cooldown/Duration 2, Player 1, Settlement 5, Settlement Derived 3) | `designs/provincial/clock_registry_v30.md`, all tables |
| Clocks cited-but-**unregistered** | **2**: Axis-9 (`ARC-P04`, `references/arcs/arc_register_clocks.md:17`; also `factions_personal_v30.md:203`), PI/Public Instability (`ARC-P07`; `params/factions.md:19,23` PP-325/335; `params/factions/stats_1_7_scale.md` BG starting value PI=5) | Confirmed absent from `clock_registry_v30.md`'s own Shared Clocks table — a registry gap, not a missing mechanic (both have real homes elsewhere); independently corroborated by `dossier_register_formalizability.md §7` |
| Faction stats (canonical lineup) | **6**: Mandate (derived headline) / Influence / Wealth / Military / Intel / Stability | `faction_canon_v30.md §5.1` (Jordan ruling 2026-05-30, LPS-2e — supersedes a stale "7-stat" schema that wrongly put Legitimacy/Popular Support at faction level) |
| Faction count carrying the full 6-stat block | **5** (Crown, Church, Hafenmark, Varfell, Guilds); 2 intentionally partial (RM 3 fields, Löwenritter ~4); 1 non-faction (Ministry, 2 fields) | `stats_1_7_scale.md` Starting Stats table; `faction_canon_v30.md §11` |
| Settlement stats | **6** tracked fields: Prosperity/Defense/Order (0-5, §1.3) + Legitimacy/Popular Support (0-7, §1.8) + FacilityTier (0-3, §1.4); 3 more (Local Economy, Garrison Strength, Public Order) are *derived*, not independently stored | `designs/territory/settlement_layer_v30.md` §1.3, §1.4, §1.8 |
| Settlement count | **37** (35 + 2 special-case) | §2.1, PP-726 |
| NPC tracks, Active tier | **5** required fields (Disposition/PC, Availability, active-Duty ref, Scar count, action flag) | `npc_behavior_v30.md §11.1` |
| NPC tracks, Stance-Triangle sheet (separate schema, 17 principal entries) | **~8** fixed fields (Convictions ×2, Ethical Framework, Resonant Styles ×2, Thread Sensitivity, Certainty, Leadership Deviation Ob) | `npc_behavior_v30.md §2` |
| Active/Passive NPC population | **~35 Active + ~30 Passive** = 65 tracked | §11.2, §11.6 |
| Event deck — the task's "28 cards" | **Does NOT live in `governance_play_redesign_v1.md`** (that doc defines 7 card *families* — Petition/Friction/Opportunity/Crisis/Intrigue/Ambition/Thread — with an explicit OPEN target of "~60-100 base cards," §5.3, still undecided; PROPOSAL status, not canonical). The literal 28-card deck is a **different, narrower doc**: `designs/territory/goldenfurt_slice/event_deck.md`, a single-settlement worked example (Goldenfurt/S-006, PROPOSAL 2026-06-23), whose family coverage sums 3+5+3+4+5+6+2 = 28. Task's number was right about the digit, wrong about which artifact it names. | `governance_play_redesign_v1.md` §2.2-§2.4, line 267; `designs/territory/goldenfurt_slice/event_deck.md` |
| Other decks found | Threadwork Co-Movement deck: **18 cards** CANONICAL (`threadwork_v30.md:936`) — but `params/bg/military.md:34` cites the same deck as "20-card" (unreconciled drift between two canonical-tier docs, a genuine new finding); Mass-battle tactic cards: **20** (4 shared + 2×8 factional), CANONICAL (`mass_battle_v30.md §B.4`, PP-283) | as cited |

**Total distinct state-graph variable estimate**: 53 (clocks) + 6×5=30 (faction stats × full-sheet
factions) + 6×37=222 (settlement stats) + 5×35=175 (NPC Active-tier fields) + (28+18+20)=66 (event
deck cards, three decks) **≈ 546 distinct tracked state variables** feeding the engine in a given
season — the substrate the arc-vector trigger predicates (§3) read from. [UNGROUNDED beyond the
per-row citations: this sum double-counts nothing intentionally, but is sensitive to which
faction-count and NPC-field convention you pick — a genuine range is 450-650, not a single number.]

---

## 3. ARC-TEMPLATE SPACE

### 3.1 The register is bigger than its own grounding doc claims

`00_grounding/01_arc_corpus.md` (a) states "~110 arc IDs." **Direct `grep` count of every
bold-header entry across all 5 `references/arcs/*.md` files gives 138**, not ~110 — a ~25%
undercount in the corpus's own most-cited inventory figure:

| File | Grounding-doc claim | Direct verified count |
|---|---|---|
| `arc_register_clocks.md` §I | 12 | **7** (ARC-P01–P07 — lower, not higher) |
| `arc_register_threads.md` §II | 8 | **8** (confirmed exact) |
| `arc_register_territory.md` §IV | "6 root TE-IDs, tiered" | **29** distinct TE-## entries (no 6-root/tiered structure is visible in the file — every TE-## is a standalone bold-header entry) |
| `arc_register_factions.md` §III | 87 | **81** (ARC-* / NPC-ARC-* bold headers) |
| `arc_register_events.md` §V-VI | 5 BG-CV + 8 COLLISION = 13 | **13** (confirmed exact: 5 BG-CV-01..05, 8 COLLISION A/B/C/D/E/F/G/J) |
| **Total** | **~110** | **138** |

Two files match exactly (threads, events); two are significantly off (clocks overcounted at 12 vs
actual 7; territory badly undercounted at "6" vs actual 29); factions is close (87 vs 81). This is
a genuine, previously-unflagged inventory drift in the grounding doc — not a KNOWN item from the
2026-07-04 audit. **Use 138 as the corpus size going forward**, not ~110.

### 3.2 Distinct structural shapes (sampled classification, 24 arcs across all 5 files)

Sampling method and full per-arc classification: see the parallel research pass (24 arcs spanning
clocks/threads/territory/factions/events, classified by trigger-predicate type × effect type ×
binding-slot pattern). Headline findings:

- **Territory arcs collapse hardest**: one shape — "territory-control-check → persistent
  cascading-multi-stat effect, terminates on reversal" (TE-01-type) — covers roughly **20-25 of the
  29** territory entries.
- **Clock arcs collapse almost entirely into one shape**: passive accrual + rate-modifier +
  threshold-gate, covering 6 of 7 (ARC-P05's GM-judgment qualitative selection is the one outlier).
- **COLLISION entries (8) are one shape by construction** (cross-arc-collision predicate over
  ≥2 other arcs' state); **BG-CV events (5) are one shape** (multi-stat-AND one-time trigger →
  permanent bump). 13 of 138 collapse to two templates trivially.
- **Faction-tier arcs (81) sort into ~7 recurring families**: faction+NPC personal-track threshold
  cascade (~12-15 arcs, the ARC-S07 "Torben Loyalty Clock" shape — the capstone target itself is
  the single most duplicated shape in the corpus), elimination→succession (~6), threshold→
  action-gate (~6-8), personality-driven multi-offer choice (~5), concurrent multi-faction contest
  (~4-5), non-roll bifurcation decision-point (~5-6), opposed-roll/Overwhelming-exposure (~7). A
  residual ~5 arcs (operation-cost-linear-depletion, scene-window checks, the underground cluster)
  don't fold cleanly into the above.

**Working number: ~13 distinct structural shapes (range 12-15)** collapse the 138-entry register —
i.e. the register is much closer to **"13 templates × ~10.6 average bindings each"** (different
faction/territory/NPC names, different numeric thresholds on the same predicate/effect skeleton)
than to 138 independently-authored structures. This is the arc-tier analogue of the render-stack's
own "product becomes a sum" discipline (`03_articulation_nlg_architecture.md §2/§8`, per
`dossier_content_economics.md §2.2`) — and it is corroborated independently by
`dossier_register_formalizability.md`'s typed-schema pass, which found the register compiles to
one `arc_vector` YAML shape (§2 there) with `activity_mode` as essentially a 5-value enum
(`level_triggered`, `edge_triggered_once`, `edge_triggered_retryable`, `clock_escalation`,
`convergence`) — a second, independently-derived shape count in the same low-teens range.

---

## 4. BAKE RECOMPUTED

### 4.1 The task's "Annex B" numbers are not grounded in the corpus — treat as fresh priors

I searched the full audit folder (`spec_sections/*.md`, `00_grounding/*.md`) for "beat-class,"
"decree-class," "circumstance-class," and "skeleton…variant" — **none of these terms or numbers
appear anywhere in the working tree.** There is no literal "Annex B" with beat-classes-per-rung
figures; the task handed me these as **fresh assumption numbers to work with**, not a citable
source. I mark the rung/skeleton figures `[OPEN — Jordan tuning / task-supplied prior, UNGROUNDED]`
and compute using them, cross-checked against what the corpus actually authors (overlay tables,
venue count, NPC/arc caps) — the latter IS grounded and does most of the real work below.

### 4.2 What's actually grounded (recap, not re-derived — full derivation in
`dossier_content_economics.md`, which already did this analysis in depth and whose numbers I
verified independently in §1-§3 above where they overlap)

- **Backbone slot-templates**: Key-type (43 articulation-relevant, §1.1) × render-style (**2**,
  not 3 or 10 — `articulation_layer_v30.md §3.4` names exactly 2 authored template STYLES, "flash"
  5-10s and "scene" 10-15s; the 3-way significance split §3.2 and the 10-trigger table §3.1 are
  both *routing* logic onto these same 2 structures, not additional template shapes) ≈ **86**.
- **Shared lexicon overlays** (reused across all 86, not copied per-template): Coherence×TS weight
  table (6×3=18 cells, already exists, `coherence-tiers.md`) + Certainty register lexicon (**5**
  named clusters, not the mechanical track's 6 values — `solmund_voice_v30.md §18` has a coverage
  gap at Certainty 0 and an out-of-range "6+" entry, a genuine schema defect, `dossier_content_
  economics.md §1.5`) + Spirit closing-register (**2** authored variants, Beckett/Lispector, +1
  free Mid-band) + focalizer (**5**: 4 fixed-Certainty chroniclers + protagonist, already-authored
  voice-canon prose, applied as a splice-time tag not new bake cost).
- **Per-NPC overlay**: bounded by the **~35-Active-NPC cap** (§1.3/§2), not open-ended — a few
  idiolect micro-units per NPC, not a full fragment set per NPC.
- **Per-arc specificity**: bounded by the (now-corrected) **138-arc register**, but per §3.2
  collapses to **~13 structural shapes** — arc color is a data-substitution problem
  (targets[]/causes[] entity names into a shape-level sentence pattern), not 138 (or 110) bespoke
  fragment sets.
- **Venue shapes**: `spec_sections/s3_q4_render.md` Q4.2 table names **10** hosting-venue rows
  (social/political contest, personal combat, thread operation, investigation, mass battle,
  settlement governance, Knot/Bond scene, witness-mode, retrospect/chronicle, travel) — close to
  the task's "~12" estimate but the grounded count is 10; contest alone further subdivides into
  "8 proceedings × 4 games" per the same table, so venue-internal shape variety is higher than the
  row count alone suggests.
- **Regional/settlement idiom axis**: `designs/world/geography_v30.md` "Terrain Regions" (§ line
  16) has only **one populated subsection** (Northern Mountains) out of six named headers
  (Continental Context, Geographic Unity, Church Geography, Restoration Movement Geography,
  Maritime Forgetting Zone, Calamity Bleed Gradient are all empty placeholders in the current
  file). **There is no authored "region" tier distinct from the 17 territories** — regional idiom,
  if built, is really **per-territory idiom (17)**, not a separate smaller "regions" axis; treat
  any regional-idiom line item as bound to 17, not to an undefined smaller region count.

### 4.3 Recomputed total, folding the task's rung/skeleton priors into the grounded backbone

Using the task's own supplied (ungrounded) rung figures as one input alongside the grounded
render-stack numbers:

```
Grounded backbone + shared lexicon + NPC overlay + arc-shape overlay (from §4.2, all cited):
  86 (backbone) + ~35 (shared lexicon net-new: 5 Certainty + 2 Spirit + ~28 misc small units)
  + ~100-175 (35-NPC-bounded idiolect) + ~13-130 (13 arc-shapes × ~10 bindings' worth of
  entity-substitution templates, NOT per-instance fragments)
  ≈ 235-425 authored units — consistent with dossier_content_economics.md's independently-reached
  "~350-450 authored units, low hundreds" (§2.2/§5 there).

If the task's rung/skeleton framing is instead read literally (beat-classes ~6-10 per rung ×
6 rungs [character/family/faction/settlement/territory/world] × 3-5 skeleton variants each):
  ~8 avg beat-classes × 6 rungs × 4 avg skeletons ≈ 192 rung-level skeletons
  — this lands in the SAME low-hundreds order as the grounded backbone above, which is a good
  sign (two differently-derived estimates converge), but the rung numbers themselves remain
  [UNGROUNDED / task-supplied], not independently verified against a corpus doc.
```

**Authored-unit range: ~230-450, most likely low-to-mid hundreds** (not 10³-10⁴ as Jordan's frame
states) **— UNLESS** the open Certainty-in-bake-key discrepancy (`dossier_content_economics.md §3
item 3`: does Certainty gate the frozen fragment pool, or is it a runtime-only lexicon swap?)
resolves toward "yes, it gates the pool," which multiplies the backbone by up to ~5-6× and pushes
the true figure into the **low thousands (~1,200-2,700)** — genuinely within Jordan's stated
10³-10⁴ floor. This one open design decision is the single biggest swing factor in the whole
census, bigger than any counting question in §1-§3.

### 4.4 Rendered-space order, and one worked example

**Naive full cross-product** (never build this — `03_articulation_nlg_architecture.md §2`'s named
failure mode): 43 Key-types × 2 styles × 6 Coherence × 6 Certainty(mechanical range) × 2 Spirit
× 5 focalizer × 35 NPCs = **~5.4 million** (per `dossier_content_economics.md §2.1`, full
derivation there). A more charitable naive reading, dropping per-NPC as a full multiplier: **~31,000**.

**One worked example** (per the task's request — multiply one beat-class through all axes): take
`state.scar_acquired` (a Tier-2-triggering Key-type, `key_type_registry_v30.md §5`) for one NPC:
2 render-styles (flash/scene, though a scar-acquisition beat is almost always "scene" not "flash"
by its own significance math, §1.2 above) × 6 Coherence bands × 5 Certainty registers (the real,
non-broken count) × 2 Spirit variants (audible only at Coherence ≤4, so really 2 bands × 2 Spirit
+ 4 bands × 1 = 8, not 12) × 5 focalizers = a per-Key-type-per-NPC possibility space of
**roughly 2×8×5 ≈ 80 distinct renderable variants** (collapsing the Coherence×Spirit joint
correctly rather than naively multiplying 6×2=12). Across the ~35 Active NPCs who could plausibly
acquire a Scar in a season: **~80 × 35 ≈ 2,800** distinct possible renderings of ONE Key-type in
ONE season — and there are 43 articulation-relevant Key-types. **Rendered combinatoric space is
genuinely 10⁶-10⁷ order** if every axis is read as fully crossed and uncollapsed (matching Jordan's
"10⁶+" claim) — but this is exactly the space the factored/orthogonal composition strategy (§4.2)
is designed to never materialize as stored assets; it is realized at splice time from the ~230-450
(or ~1,200-2,700, per §4.3's open item) authored units, not baked as 10⁶ separate files.

**Per-season render count under a 3-5-scene + texture budget**: `player_agency_v30 §4.3` bounds
slate-scene actions to **3-5/season**; texture and Tier-1 ambient content is continuous but
low-token per beat. Realistic per-season RENDERED OUTPUT (not possibility space) is bounded by:
3-5 slate scenes + a Tier-2 cut-scene rationing gate (director-governed, `articulation_layer_v30
§3.2` significance thresholds, unbuilt pacing director per `02_prose_render_stack.md (e).4`) +
annual Tier-3 chronicle (Top-N beats). **Order of magnitude: ~10-30 distinct rendered prose beats
per season per player** (3-5 played + a handful of cut scenes + texture fragments + one chronicle
entry) — nowhere near either the authored-unit count or the combinatoric possibility space, because
almost all of the possibility space is never realized in any given playthrough. This is the number
that actually matters for player-facing oatmeal risk (capstone criterion 3: 5 seeds must differ in
named actors/stakes/outcomes) — 10-30 beats/season is a small enough sample that per-arc/per-NPC
specificity (not lexicon variety) is what will make or break the anti-oatmeal bar in practice.

---

## 5. EXISTING ASSETS OFFSET

| Asset | Size (verified) | What it actually offsets |
|---|---|---|
| `designs/arcs/gm_ref/` (8 files) | **~300KB** (confirmed — despite its own README claiming "currently empty"; per `01_arc_corpus.md` (c) and `dossier_content_economics.md §1.9`: `arc_narrative_analysis.md` 48K, `arcs_01_04.md` 36K, `arcs_05_09.md` 28K, `arcs_10_18.md` 56K, `arcs_36_40.md` 48K, `arcs_41_45.md` 56K, `arcs_46_55.md` 40K, `arcs_46_55_resolved.md` 40K) | **Per-arc CAUSAL COLOR and narrative-analysis prose** (~2.7KB/arc across ~55+ arcs) — this is the closest existing precedent for "per-arc specificity" (§3, §4.2), proving the register's ~13 shapes CAN carry distinguishing prose at scale. It is NOT lexicon rows, NOT skeleton shapes, and NOT Coherence/Certainty-banded variants — it's single-register (implicitly high-Coherence, neutral-focalizer) prose, so it offsets the "does per-arc color exist as a discipline" question, not the "do we have banded lexicon assets" question. |
| `tests/` narrative-regression corpus (`emergent_arc_skeleton_test_*` batches 2-8 + `tests/sim/sim_arc_*.md`) | **>1MB, not the charter's ~850KB estimate** — batches 2-8 alone total 769,581 bytes (verified `wc -c`; no batch 1 exists), `sim_arc_*` adds ~280KB more | **Causal-chain / mechanical-seed stress-test prose** (mermaid causal charts, exact Ob/dice citations, IP-archetype behavioral variation) — offsets confidence that the *mechanical* trigger-predicate layer (§3) can be exercised and narrated at scale, but per `CLAUDE.md` §3 this is explicitly "prose/audit, not executable spec" — it does NOT offset bake-asset construction (no lexicon, no Coherence/Certainty bands, no focalizer variants appear in this corpus). |
| Register prose (`references/arcs/*.md`, 5 files, ~69KB, 138 entries) | ~500 bytes/entry (uniform header→trigger→effects→"Direction:" sentence) | **Offsets the SHAPE-LEVEL sentence-template pattern** (§3.2, §4.2's per-arc-specificity line item) — proves one authored sentence-shape per arc-family + entity substitution is a viable, already-practiced authoring discipline at this repo's actual production scale. Does not offset lexicon/register work at all — it's mechanically terse by the arc-generator skill's own hard rules (`01_arc_corpus.md` (c): "no single player decision caused this," seasonal ±2 cap). |
| `coherence-tiers.md`, `solmund_voice_v30.md §18`, `prose-writer/SKILL.md`, chronicler voice-canon docs | Not separately sized, but structurally: 6×3=18-cell weight table + a 5-cluster Certainty register (with the §1.5-noted coverage gap) + 4 fully-authored chronicler voice profiles | **This is the actual shared-lexicon-layer asset** the bake needs (§4.2) — already written as design prose, not prototype code. This is the one asset class that DOES directly offset lexicon-table construction, and it's the smallest of the four listed here by raw byte count but the most load-bearing for the factored bake strategy. |

**Net read**: the three largest existing corpora (gm_ref, tests, register) all offset **shape and
causal-color** authoring — proof this repo can produce arc-specific prose at the necessary count
and rate — but **none of them offset lexicon-table construction** (Coherence/Certainty/Spirit
banded fragment pools), which is a genuinely separate, smaller, and mostly-already-drafted asset
class (the voice-canon docs). The task's instinct to ask "NOT lexicon rows?" for each corpus was
correct: none of the three narrative corpora are lexicon assets, and conflating "we have 1.3MB of
arc prose" with "we have banded rendering lexicon" would be a category error.

---

## 6. Summary verdict

C1 (authored-templates-only, no runtime LLM) is **feasible at the anti-oatmeal bar** on the
grounded numbers above, with one swing factor still open (the Certainty-in-bake-key resolution,
§4.3) that determines whether the true authored-unit count is low-hundreds (my recomputation) or
low-thousands (Jordan's stated floor) — both are buildable by hand or offline-LLM bake; neither
requires the 10⁶+ combinatoric space to be materialized as stored assets. See the ~600-word reply
for the compact numbers table and one-sentence verdict.
