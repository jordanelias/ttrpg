# Valoria — Comprehensive Workplan (Final)
## Derived from Complete System Audit (2026-04-18)
## Organized by priority tier → dependency order → estimated effort
## All 19 review amendments integrated
## Target: Godot 4.3 videogame implementation

---

# HOW TO USE THIS DOCUMENT

**Execution order matters.** Items within each phase are sequenced by dependency — later items may depend on earlier items completing first. Cross-references to audit flags (AUD-*), editorial items (ED-*), simulation debt (SIM-*), and propagation map entries are provided to enable verification.

**Canon compliance is non-negotiable.** Before any design decision in Phase 1–3, read `canon/00_philosophical_foundations_rules.md`. Every mechanical change must be verified against the 15+ philosophical principles (P-01 inseparability, P-03 rendering, P-08 epistemological barrier, etc.). If a proposed resolution would violate a principle, the resolution must be redesigned — the principle does not bend. State the principle and compliance rationale in every commit message that modifies a design doc.

**Standard commit protocol.** Every commit that modifies a design doc must:
1. Update `references/propagation_map.md` per its Step A–D auto-update protocol
2. Update `references/canonical_sources.yaml` SHA for every modified file
3. Update `canon/editorial_ledger.yaml` for any resolved or newly raised ED items
4. Include `references/canonical_sources.yaml` for co-file compliance (enforced by `safe_commit`)
5. Run `h.safe_commit()` — the only valid commit path

**Inconsistency detection.** This workplan is one lens. Five other lenses catch uncommitted work and inconsistencies:

| Lens | Location | What It Catches |
|------|----------|----------------|
| **Propagation Map** | `references/propagation_map.md` | Files changed without downstream propagation. Run `tools/broken_dependency_checker.py` to detect broken refs. Check BROKEN DEPENDENCIES section and all `[PROP-STALE]` markers. |
| **Session Log** | `session_log_current.md` | `open_items` list shows work acknowledged but not yet committed. `files_modified` shows what changed last session. Compare against editorial ledger to find items listed as "resolved" in session log but still "open" in ledger (or vice versa). |
| **Editorial Ledger Summary** | `canon/editorial_ledger_summary.yaml` | `p0_blocker_ids`, `p1_blocker_ids`, `open_ids` — the definitive list of unresolved editorial items. Cross-reference `external_blockers` section for sim_debt and unsimulated canonical content. |
| **Coverage Matrix** | `tests/coverage_matrix.md` | Open findings table, SIM-DEBT items, cross-simulation findings. Any item marked "Open — ED-NNN" that doesn't appear in the active editorial ledger is an inconsistency. |
| **File Index** | `references/file_index_summary.md` | `Propagation-pending` count. `Known stale sync gaps` count. Each propagation-pending item is uncommitted downstream work. |

**Inconsistency sweep protocol (run at session start):**
1. Bootstrap (establishes session token, reads all registers)
2. Compare `editorial_ledger.yaml` open items against `coverage_matrix.md` open findings — flag mismatches
3. Compare `session_log_current.md` `open_items` against `editorial_ledger.yaml` — flag items in one but not the other
4. Run `tools/broken_dependency_checker.py` against `propagation_map.md`
5. Check `file_index_summary.md` `propagation-pending` — each item is uncommitted downstream work
6. Check `editorial_ledger_summary.yaml` — if `p1_blocker_count` doesn't match the count of P1 items in active ledger, summary is stale

---

# PHASE 0: HOUSEKEEPING (prerequisite to all other work)

Estimated effort: 1 session. No design decisions required.

## 0.1 — Rebuild editorial_ledger_summary.yaml
**Why:** Summary is stale (last updated 2026-04-17). P1 blockers ED-576/577/578/581/582/663 were resolved 2026-04-18 but summary still lists old P1s. `next_id` shows 673 but active ledger has entries beyond that.
**Action:** Read active ledger + archive. Rebuild summary with correct counts, IDs, and next_id.
**Verify:** `p1_blocker_count` matches actual count of `status: open, severity: P1` entries in active ledger.
**Cross-ref:** `canon/editorial_ledger_summary.yaml`, `canon/editorial_ledger.yaml`

## 0.2 — Deduplicate ED-663 in active ledger
**Why:** Two ED-663 entries exist in active ledger — one `status: open` (the old gap-logged version) and one `status: resolved` (the new resolution from this session). The old one should have been archived.
**Action:** Archive the old ED-663 entry. Scan for any other duplicate IDs across the active ledger.
**Cross-ref:** `canon/editorial_ledger.yaml`, `canon/editorial_ledger_archive.yaml`

## 0.3 — Update file_index_summary.md propagation-pending count
**Why:** Currently lists 13 propagation-pending items. Some may have been resolved in recent sessions without updating the count.
**Action:** Read `references/file_index.md` (full, 446 lines). Count actual propagation-pending items. Update summary.
**Cross-ref:** `references/file_index_summary.md`, `references/file_index.md`

## 0.4 — Run broken_dependency_checker against propagation_map
**Why:** 3 known broken dependencies exist (stage3_thread, stage9_social, stage_bg_board_game — all deprecated compilations). Additional broken deps may have accumulated from recent commits.
**Action:** `python3 tools/broken_dependency_checker.py`. Log any new broken deps. No action needed on known deprecated compilation breaks.
**Cross-ref:** `references/propagation_map.md` BROKEN DEPENDENCIES section

## 0.5 — Verify session_log open_items against editorial_ledger
**Why:** Session log lists ED-671, ED-666, ED-667, ED-632, ED-633, ED-629, ED-663, ED-670/672/673 as open. ED-666/667/663 were resolved this session. ED-632/633/629 may have been archived in a prior session but not removed from the session log template.
**Action:** Cross-check each item. Update session log or ledger as needed.
**Cross-ref:** `session_log_current.md`, `canon/editorial_ledger.yaml`

## 0.6 — Triage P0 blockers ED-668–672
**Why:** 5 P0 blockers (Thread horizontal integration items from stress register) are listed in the editorial ledger summary but not addressed in any workplan phase. P0 outranks P1 by definition.
**Action:** Read `tests/stress/thread/threadwork_audit_register.md`. For each ED-668–672: determine resolved (archive), still open (add to Phase 1 at P0 severity), or reclassify (change severity with rationale). These may correspond to successor items from ED-629 (Thread stress test).
**Cross-ref:** `canon/editorial_ledger_summary.yaml` `p0_blocker_ids`, `tests/stress/thread/threadwork_audit_register.md`

## 0.7 — Params file staleness audit
**Why:** The simulation framework (Phase 4) reads mechanical values from `params/*.md` files. If params are stale (don't match their source design doc), the simulation produces incorrect results. This must be resolved before Phase 4, not after.
**Action:** For each params file (`params_core`, `params_combat`, `params_mass_combat`, `params_contest`/`params_debate`, `params_threadwork`, `params_factions`, `params_board_game`, `params_scale_transitions`): compare against its canonical source design doc per `references/canonical_sources.yaml`. Mark stale entries. Refresh values. Clear `KNOWN STALE SYNC GAPS` in file_index.
**Cross-ref:** `references/propagation_map.md` §PARAMS-SKILL DEPENDENCY MAP

---

# PHASE 1: P1 BLOCKERS — DESIGN GAPS (blocks implementation)

Estimated effort: 2–3 sessions. Requires design decisions.

**Canon compliance gate:** Before starting any Phase 1 item, read `canon/00_philosophical_foundations_rules.md`. Every design resolution must be checked against the relevant principles before committing. State the principle and compliance rationale in the commit message.

## 1.1 — Knot Formation During Play [AUD-NPC-01]
**Why:** The Solidarity Resonant Style requires an active Knot with the target NPC. Knots are currently only acquirable through lifepath (character creation) or "GM-granted" — the latter doesn't exist in a videogame. This blocks Solidarity targeting for every NPC acquired after character creation, which means the most powerful social tool against NPCs with Solidarity vulnerability (Vossen, Ehrenwall, Torben) is mechanically inaccessible.
**Canon check:** P-12 (relational contagion through Knots) — Knot formation must respect the constitutive nature of Knot connections. A Knot is not a contract; it is a structural relational binding. The formation procedure must reflect this ontological weight. P-15 (three-layer being-persistence) — Knot formation engages the second layer (unconscious self-rendering), not just surface Disposition.
**Design task:** Define a Knot formation procedure for videogame mode. Proposed approach: at Disposition +5 with a TS ≥ 30 character, a Knot formation scene fires (Spirit check TN 7, Ob 2). Success: Knot established. Failure: Disposition maintained but Knot attempt costs 1 season cooldown. For non-sensitive characters (TS < 30): Knot formation is impossible — Knots require Thread contact. The relationship remains at Disposition +5 with all non-Knot benefits (+1D social, no decay) but without relational contagion or Solidarity targeting.
**Affected docs:** `npc_behavior_v30.md` (§6.3 Solidarity — add Knot formation subsection), `fieldwork_v30.md` (§5.6 Knot Integration — add formation procedure), `companion_specification_v30.md` (§2.1 eligibility — Knot path already references this but no procedure exists).
**Propagation:** `params/core.md` (Bonds/Knot rules), `references/propagation_map.md`, `canon/editorial_ledger.yaml` (new ED or resolve ED-391).

## 1.2 — Accord Propagation to Settlement Order [AUD-SET-02]
**Why:** Settlement layer (§1.3) changed Accord derivation: Province Accord = floor(mean settlement Order). But every existing doc that references "Accord −1 in territory" still uses direct Accord modification. These rules now need to specify WHICH settlement's Order is affected. Without this propagation, the settlement layer's Accord derivation is canonical but not exercised — downstream systems still bypass it.
**Canon check:** P-03 (rendering = consciousness-performed) — settlement Order is the rendered-level experience of governance; province Accord is the abstracted measure. The propagation must preserve this distinction: events that the player experiences at a settlement affect that settlement's Order; events that occur at the province level (Domain Actions, military control changes) affect all settlements proportionally or target the Seat settlement by default.
**Design task:** Audit every Accord change rule across all docs. For each, determine: does this affect one settlement (which one — Seat, specific combat location, NPC's home settlement?), all settlements in a province (distribute evenly), or the province directly (bypass settlement Order — reserved for Domain Actions that target the province abstraction layer)?
**Affected docs (non-exhaustive):**
- `peninsular_strain_v30.md` §2.3–2.4 (Accord gaining/losing rules) — each rule needs settlement targeting
- `victory_v30.md` §0.2 (Accord system) — cross-reference to peninsular_strain for Accord rules
- `mass_battle_v30.md` §A.14 (battle consequences → Accord) — target the Seat settlement of the province where battle occurred
- `scale_transitions_v30.md` §5.5 (Accord Domain Echo) — already specifies "in one territory" but needs settlement targeting
- `npc_behavior_v30.md` (priority tree Govern actions) — Govern targets a settlement, not a province
- `combat_v30.md` §13.2b (Settlement Combat Consequences) — already settlement-level, confirm alignment
- `designs/provincial/strategic_layer_v30.md` §9 (Hybrid Accounting) — Accord changes at Accounting
**Scope estimate:** 15–25 individual rule references to update. Large propagation footprint. Each modified doc requires propagation_map update and canonical_sources SHA update.
**Propagation:** Every modified doc → `references/propagation_map.md`, `references/canonical_sources.yaml` SHAs.

## 1.3 — Derived Stats Numerical Calibration [AUD-DS-01]
**Why:** All multipliers in derived_stats_v1 are explicitly PROVISIONAL (§6). Treasury ×100, Legitimacy ×20, Reputation ×15, Discipline ×10. Income and drain rates need simulation to confirm: (a) each faction has sustainable economics at starting stats, (b) drain rates create pressure without immediate collapse, (c) stat damage triggers fire once every 5–10 seasons not every season, (d) starting derived values give factions 3–5 seasons of runway before economic pressure forces Trade actions.
**Design task:** Build a per-faction economic model. For each of Crown, Church, Hafenmark, Varfell: calculate seasonal Treasury income (Σ(settlement Prosperity) × 10 per settlement + Haushalt Competence bonus if Crown + Trade action results), seasonal drains (unit upkeep at −25/professional/season, Campaign Supply at −100/season if in hostile territory, construction at −200/action, Muster costs), and time-to-zero at starting values with no income actions. Adjust multipliers if any faction collapses within 3 seasons or never faces economic pressure within 20 seasons.
**Dependencies:** 1.2 (Accord propagation affects which settlements contribute Prosperity income — Accord 0 settlements contribute nothing, Accord 1 settlements contribute nothing, only Accord ≥ 2 contributes).
**Simulation:** `tests/sim_derived_stats_calibration.md` (new). Register in `tests/coverage_matrix.md`.
**Propagation:** `designs/scene/derived_stats_v30.md` (multiplier updates if adjusted), `params/board_game.md` (faction economic parameters).

## 1.4 — Faction Politics Simulation [AUD-FP-01]
**Why:** 947 lines of faction_politics_v30 committed without simulation coverage. 5 SIM-POL items deferred (SIM-POL-R01 through R05 in coverage_matrix). The rank ladders, branch specialization, Ministry Competence/Corruption tracks, and caste viability matrix have no simulation coverage.
**Design task:** Run SIM-POL-R01 through R05. Key questions: (a) Can a player reach Standing 7 within 30 seasons (120 seasons = 30 years) through normal Duty completion? At what rate? (b) Do Ministry Competence decay rates (unfunded → −1/season) produce meaningful economic pressure on the Crown? (c) Does the caste viability matrix correctly gate faction access — can a Southern Einhir character reach Standing 5+ in the Church (should be Closed)? (d) Do branch specializations (Martial/Administrative/Intelligence for Crown) produce meaningfully different play experiences — different Duty types, different NPC relationships, different Standing advancement paths? (e) Are the 5 rank ladders balanced in advancement rate — does one faction reach Standing 7 significantly faster than others?
**Dependencies:** 1.3 (derived stats affect Duty success conditions via Treasury/Legitimacy thresholds, which affect Standing advancement rate).
**Simulation:** `tests/sim_faction_politics.md` (new). Update `tests/coverage_matrix.md` SIM-POL items from DEFERRED to results.
**Propagation:** `designs/provincial/faction_politics_v30.md` (if adjustments needed), `params/board_game.md` (Standing thresholds).

## 1.5 — Resolve Coverage Matrix P1 EDs [ED-588, ED-589, ED-612]
**Why:** Active P1 EDs in coverage matrix not captured by the system audit because they're victory/faction design gaps, not system quality issues. But they affect simulation accuracy — the simulation framework cannot model RM or Guild victory paths without these resolved.
- **ED-588: RM Phase 2 T9 PT ≤ 1 holding condition unreachable.** The RM victory Phase 2 requires PT ≤ 1 in T9 (Himmelenger), but T9 starts at PT 5 with Church infrastructure generating PT. Under normal play, T9 PT never reaches 1. Design decision needed: is this intentional (RM must conquer T9 and dismantle Church infrastructure before Phase 2)? Or is the condition too strict (change to PT ≤ 2)?
- **ED-589: RM Presence marker mechanics undefined.** RM uses "Presence markers" for Community Weaving and Cultural Reclamation but the placement, accumulation, and removal rules are not specified. Define: how does RM place Presence? What does each marker cost? How many can exist per territory? How are they removed by Church/Crown suppression?
- **ED-612: Guilds have no solo victory condition.** Guilds are an NPC faction with no player-accessible victory path. Is this intentional (Guilds are a tool, not a protagonist)? Or should Guilds have a victory condition for a hypothetical Guild-aligned player path?
**Design task:** Resolve each. Small-scope design decisions with victory_v30 and faction implications.
**Propagation:** `designs/provincial/victory_v30.md`, `tests/coverage_matrix.md`, `canon/editorial_ledger.yaml`.

---

# PHASE 2: P2 ITEMS — SIMULATION DEBT & CALIBRATION

Estimated effort: 3–5 sessions. Mix of simulation, design, and propagation.

## 2.1 — Social Contest Re-simulation [AUD-SC-02, AUD-SC-03]
**Why:** SIM-DEBT-03/04 outstanding since PP-234 genre restructure. The two-genre system (Memory/Projection) with integer bonus dice (+1D genre, +1D audience, max +2D) has never been simulated. The prior three-genre simulation baselines are invalidated. Additionally, CROSS interaction's floor(successes ÷ 2) formula may make it non-viable against Resistance 2+ audiences — a 6-success CROSS exchange produces effective margin 3, which only moves the track 1 point against Resistance 2.
**Tasks:** (a) Simulate 100+ contest exchanges under the PP-234 system across all three adjudicator types (Cognition pools for Expert Judge, Charisma pools for Crowd, Attunement pools for No Adjudicator). Vary pool sizes from 5D to 13D. (b) Specifically test CROSS viability: how often does a CROSS exchange produce track movement at Resistance 1, 2, 3? If success rate at Resistance 2 is <10%, CROSS needs rebalancing (e.g., floor(successes × 2/3) instead of floor(÷2), or effective margin = successes − 1 instead of floor(÷2)). (c) Test Chain Contest deadlock stall-break (ED-582) against high-Focus orators (Focus 5+, Resistance 2 both sides): does the Resistance drop to 1 produce meaningful track movement, or does it always resolve as forced Compromise?
**Simulation:** `tests/sim_contest_pp234.md` (new). Resolve SIM-DEBT-03/04 in coverage_matrix.
**Propagation:** If CROSS is rebalanced → `designs/scene/social_contest_v30.md` §4 CROSS section, `params/contest.md`.

## 2.2 — Co-Movement Card Calibration [ED-577-01/02/03/04] ⚠ HARD DEPENDENCY FOR PHASE 4
**Why:** 15-card table added this session (ED-577) but effects are entirely unsimulated. Four open flags. The simulation framework uses Co-Movement cards in every Thread operation — uncalibrated cards produce unreliable MS trajectories, which invalidates the entire Phase 4 simulation.
**Tasks:**
(a) **CM-13 "temporary Thread perception" mechanically undefined [ED-577-01].** Propose: non-Sensitive NPC gains TS = 15 (enough to perceive Thread events per visibility table but not enough to perform Thread-Read or Leap). Duration = 1 scene. Scope = passive perception only. The NPC sees something impossible and must process it through their existing Conviction framework — this is a Certainty pressure point, not a Thread capability grant.
(b) **Deck reshuffle timing unspecified [ED-577-02].** Propose: global deck (not per-territory), reshuffle when all 18 cards have been drawn. This means the deck cycles every 18 Thread operations across the entire peninsula. A territory with high Thread activity draws more cards per cycle. Card counting is possible but requires tracking all Thread operations peninsula-wide — strategically valuable information but not trivially available.
(c) **MS swing variance [ED-577-03].** Simulate: model 30 seasons × 3 Thread operations/season (average across all factions and practitioners) = 90 card draws per campaign. Calculate mean cumulative MS impact and standard deviation. If std dev > 15 MS points, the deck is too volatile — individual campaigns would have wildly different MS trajectories purely from card draw luck. Fix: adjust individual card MS values to mean-center the deck (sum of all MS effects across 18 cards ≈ 0, with variance from Actualized/Unactualized split).
(d) **CM-06 +1D scope [ED-577-04].** CM-06 "Resonance Bloom" grants "+1D to next Thread operation" to "all Practitioners in territory." In a territory with 3+ practitioners, this is extremely powerful — it compounds with existing pool bonuses. Propose: +1D applies to the next operation per practitioner (not all operations), expires unused at season end.
**Simulation:** `tests/sim_comovement_calibration.md` (new).
**Propagation:** `designs/threadwork/threadwork_v30.md` §4.3 (card revisions if needed), §4.1 (Core Principle — write foundational text explaining why Co-Movement produces random effects), §4.2 (Why Random — write design rationale).

## 2.3 — NPC Stat Gaps [AUD-NPC-02]
**Why:** 7 NPCs missing TS and/or Certainty values: Ehrenwall (ED-392/393), Torben (ED-394/395/396), Maret Uln (ED-397/398). These values are needed for: NPC priority tree evaluation (TS gates Thread actions), Conviction Scar matrix (Certainty scaling), and arc transition triggers (TS threshold crossing).
**Design task:** Assign values consistent with characterization:
- **Ehrenwall:** TS 0 (military career, no practitioner exposure), Certainty 4 (Faithful — conventional piety, not deep theology). Consistent with her Order/Autonomy Conviction and martial background.
- **Torben:** TS 0 (court-raised, no practitioner exposure), Certainty 4 (Faithful — conventional education). But note: Conviction window (ED-618) means Certainty is mutable through play if a faction invests in Torben before Season 8. If Varfell invests, Certainty may drop; if Church invests, Certainty may rise.
- **Maret Uln:** TS 35 (from sustained Varfell Thread exposure under Vaynard's program — she was part of the intelligence apparatus that handled Thread-adjacent information), Certainty 2 (Skeptic — secular intellectual like Vaynard but more community-oriented). TS 35 means she crosses the Active threshold and can perform Thread-Read, which affects her arc behavior if Vaynard is eliminated and she takes over.
**Propagation:** `designs/npcs/npc_behavior_v30.md` (NPC profiles §2.5, §2.8, §2.10), `designs/arcs/arc_expansion_v30.md` (arc profiles reference these values), resolve ED-392–398 in editorial ledger.

## 2.4 — NPC Priority Tree Cross-Faction Simulation [AUD-NPC-03]
**Why:** 9 faction priority trees (§8.2–§8.10) have never been tested against each other. Each tree has 6–8 priority levels with conditional behaviors. A single incorrect priority ordering (e.g., Church §8.2 prioritizing CI expansion over territorial defense during Stability ≤ 2) produces faction behavior that breaks verisimilitude — the Church would expand aggressively while its institutions are crumbling.
**Tasks:** Simulate 10 seasons of 4-faction (Crown/Church/Hafenmark/Varfell) AI priority tree interaction. For each season: each faction evaluates its priority tree, selects a Domain Action, resolves it, and the results modify game state for the next season's evaluation. Check: (a) Does any faction repeatedly choose the same action for 5+ consecutive seasons (action repetition = broken priority evaluation)? (b) Do factions respond to each other's actions — specifically, does reactive Priority 6 fire when a rival faction expands into adjacent territory? (c) Does the Constrained sub-arc (ED-586, Mandate < 3) correctly suspend expansion priorities and switch to institutional rebuilding (Govern, Trade)?
**Dependencies:** 2.3 (NPC stats needed for priority tree evaluation — TS gates Thread-related priorities for Varfell and Wardens).
**Simulation:** `tests/sim_priority_trees.md` (new). Update `tests/coverage_matrix.md`.

## 2.5 — Settlement Economy Simulation [AUD-SET-01, AUD-SET-03]
**Why:** 36-settlement economy entirely unsimulated. The settlement layer is the game's largest unsimulated canonical system (53k chars, 497 lines). Two specific concerns: (1) Order averaging → Accord derivation may have unintended effects (one settlement at Order 0 can cap a 3-settlement province's Accord at floor((5+5+0)/3) = 3, even if two other settlements are perfectly governed); (2) the 36-settlement Prosperity → Treasury income pipeline hasn't been verified against faction starting positions.
**Tasks:** (a) Model all 36 settlements' starting stats and derived values (from settlement_layer §2.1 registry). Calculate per-faction Treasury income at game start from Σ(settlement Prosperity) × 10 per settlement. Verify Crown (12 settlements, mixed Prosperity 0–4) has adequate income vs Church (3 settlements, Prosperity 2–3) vs Hafenmark (8 settlements, Prosperity 2–5) vs Varfell (7 settlements, Prosperity 0–3). (b) Test the Order → Accord derivation: simulate a province with 3 settlements where one revolts (Order drops to 0). Verify resulting Accord = floor((other1 + other2 + 0) / 3) produces the intended design outcome. If Order 0 in one settlement tanks a well-governed province's Accord, consider: weighted average by settlement type (Seats count double), or floor of median instead of mean, or minimum Order as a separate Revolt trigger independent of Accord. (c) Test siege attrition: a settlement at Prosperity 0 causes units stationed there to lose Size −1/season from attrition. How fast does this drain a 4-unit garrison? At Size 4 per unit, attrition destroys a unit in 4 seasons — is this too fast or appropriate for "starving siege"?
**Dependencies:** 1.2 (Accord propagation must be resolved first — need to know how Accord rules target settlements), 1.3 (derived stat multipliers must be set — Treasury income formula uses them).
**Simulation:** `tests/sim_settlement_economy.md` (new).

## 2.6 — RM Victory Probability [AUD-VIC-02]
**Why:** RM is "hardest mode" (explicitly stated) but win probability against 4 AI factions has never been simulated. RM victory has two phases: Phase 1 (Cultural Majority: PT ≤ 1 in ≥ 4 territories) and Phase 2 (Cultural Uprising: Weaver pool vs Ob = CI ÷ 10, round up, min 1, max 5). Both are gated by variables the player has indirect control over (PT through Cultural Reclamation/Community Weaving, CI through counter-pressure). The key question: can RM achieve Phase 1 before CI reaches 60+ (which makes Phase 2 Ob 6 — near-impossible at typical Weaver pools of 7–9D)?
**Tasks:** Simulate RM-as-player vs 4 AI factions over 120 seasons (30 years). Use the Restorationist player policy. Key metrics: season at which Phase 1 first achieved, CI value at that season, Phase 2 success probability, number of runs (out of 5) that achieve victory. If RM wins <5% of runs, the victory condition may need adjustment (lower Phase 1 threshold, or cap Phase 2 Ob at 4 instead of 5, or give RM a PT erosion bonus from Community Weaving).
**Dependencies:** 2.4 (AI priority trees must be validated first — Church AI CI advancement rate directly determines RM viability).
**Simulation:** `tests/sim_rm_victory.md` (new).

## 2.7 — Mass Battle Editorial Items [AUD-MB-02]
**Why:** Part C of mass_battle_v30 has 7 editorial items pending approval: Command-EDIT-01 (Military stat → unit Power/Discipline ceiling), Command-EDIT-02 (battle outcome → faction stat consequences), Command-EDIT-03 (Muster → unit stats: Size=2, Power = floor(Military/2)+1), BG-EDIT-01 (commander bonus formula: floor(Military/2)), BG-EDIT-02 (faction-specific tactic cards), CLOCK-EDIT-01 (IP 75+ Altonian invasion unit stats), CLOCK-EDIT-02 (Church military victory → CI change).
**Action:** Review each proposed resolution. Accept or modify. These are confirmations of proposals already stated in the doc — acceptance commits them as canonical, rejection requires alternative resolution.
**Propagation:** `designs/provincial/mass_battle_v30.md` Part C (strike editorial flags, mark as resolved), `params/mass_combat.md` (update extracted values).

## 2.8 — Combat Ranged TN Integration [AUD-COM-04, ED-129]
**Why:** Melee weapons use a clean 3-axis binary TN matrix (Reach × Weight × Type → 8 profiles, TN 5–8). Ranged weapons (Bow TN 7, Crossbow TN 6, Sling TN 8) exist as a separate table outside this matrix. This means the combat system has two parallel weapon frameworks — one combinatorial, one lookup. For Godot implementation, the engine needs either one unified framework or an explicit architectural justification for two.
**Design task:** Either integrate ranged weapons into the 3-axis matrix (propose: add a 4th binary axis "Delivery: Melee/Ranged" that shifts TN and removes STR minimum for Ranged) or formalize ranged as a distinct weapon category with explicit justification (ranged weapons don't share the Reach/Weight characteristics that define melee — a bow is neither Short nor Long in the melee sense).
**Propagation:** `designs/scene/combat_v30.md` §5, `params/combat.md` (weapon tables).

## 2.9 — Threadwork Foundation Text [AUD-TW-01]
**Why:** §4.1 (Core Principle) and §4.2 (Why the Actual Effect Is Random) are empty stubs. The Co-Movement card table exists (ED-577, this session) but the explanatory text for why random effects occur when a practitioner operates on Thread is missing. For a system this philosophically grounded (the entire metaphysics is about rendering, consciousness, and the inseparability of observer and substrate), empty philosophical sections are conspicuous.
**Design task:** Write §4.1 and §4.2 prose. These are philosophical/design rationale sections, not mechanical specs. ~200 words each. §4.1 should explain that Co-Movement is constitutive — Thread operations affect the substrate, and the substrate's response is not deterministic because the substrate is not a mechanism (it is constitutive ground, per Foundations A1). §4.2 should explain why the game uses random card draws rather than deterministic outcomes — the randomness models the practitioner's inability to predict how the substrate will respond to intentional intervention.
**Propagation:** `designs/threadwork/threadwork_v30.md` §4.1, §4.2.

## 2.10 — UI/UX Integration: Derived Stats + Settlement Map [AUD-UI-01, AUD-UI-02]
**Why:** UI spec (v4.1) predates derived_stats_v1 and settlement_layer_v30. The faction overview display proposed in derived_stats §3.3 (stat bars for capability + resource numbers with income/drain breakdown) hasn't been incorporated into the UI spec. The 36-settlement map view (province zoom shows settlement nodes with type icons and stat indicators) isn't specified anywhere in the UI doc.
**Design task:** (a) Add Part 11 subsection for derived stats display: render the §3.3 proposed layout as a UI spec with Godot-facing implementation notes. Stat bars show 1–7 capability. Resource numbers show derived values with seasonal net (green = positive, red = negative). Income/drain breakdown on hover. (b) Add Part 3 subsection for settlement map: province-level zoom replaces the flat territory view with a settlement node graph. Each node shows: settlement type icon, current stats (P/D/O as 3 small bars), governor name, Church infrastructure indicators (4 small icons for the 4 axes). Settlement selection opens the settlement detail panel.
**Dependencies:** 1.3 (derived stat multipliers must be finalized before UI displays them — the numbers shown to the player must be correct).
**Propagation:** `designs/ui/valoria_ui_ux_v4_1.md` (new subsections in Part 3 and Part 11), cross-reference from `derived_stats_v30.md` §3.3 and `settlement_layer_v30.md` §4.1.

## 2.11 — Generational Transition Throughline
**Why:** When a PC dies/retires and a new character enters via Conviction Legacy (T8), the transition's effect on tracked state is only partially specified. Evidence Tracks persist (fieldwork §4.1). Disposition resets (new character). Standing resets to 0. Knots break. Coherence resets to 10. But these aren't all stated in one place, and some transitions aren't stated at all (what happens to the PC's Resources? Their Exposure per territory? Their Combat Reputation? Their active Obligations? Their companion relationships?).
**Design task:** Write a Generational Transition section (either in player_agency §10/§11 or as a standalone reference document). Enumerate every tracked value and its transition behavior:
- **Preserve:** Evidence Tracks (knowledge persists in notes), world state (all faction stats, clocks, NPC states, settlement states)
- **Transform:** One Conviction (Legacy Conviction, per T8 — inherits as transformed version)
- **Reset:** Disposition (all NPCs, back to faction-default), Standing (to 0), Coherence (to 10), TS (per new character's lifepath), Certainty (per new character's lifepath), Wounds (0), Stamina (full), Momentum (0), Combat Reputation (0), Exposure (0 all territories)
- **Break:** All Knots (relational threads sever — Knotted NPCs receive Knot rupture strain)
- **Transfer:** Companions depart (departure scene for each — the companion was bonded to the person, not the player). Active Obligations transfer to the new character's faction (the institution remembers the commitment even if the individual doesn't).
- **Open question:** Resources — does personal wealth persist (inheritance) or reset (new character starts fresh)? Propose: Resources = floor(predecessor's Resources / 2) + new character's starting Resources (partial inheritance).
**Propagation:** `designs/architecture/player_agency_v30.md` (§10 Conviction Legacy or new §11), `designs/provincial/clock_registry_v30.md` (add generational transition column per track).

## 2.12 — params_threadwork Ob Alignment [AUD-TW-02]
**Why:** Threadwork design doc (threadwork_v30) references "canonical: params_threadwork.md §Three-Axis Ob System" for all Thread operation Ob values, but the in-document Ob tables are struck (crossed out) without clear cross-reference to the params file. If the two sources specify different Ob values, a developer reading the design doc sees struck (wrong) values with no inline replacement — they must know to look in the params file.
**Action:** Fetch `params/threadwork.md`. Compare three-axis Ob values against the struck tables in threadwork_v30. Confirm alignment or flag discrepancies. If aligned: add inline cross-reference note under each struck table ("Current Ob values: see params_threadwork.md §Three-Axis Ob System"). If misaligned: determine which is authoritative (canonical_sources.yaml says), update the other.
**Propagation:** If discrepancies found → update one source to match the other. Update `references/canonical_sources.yaml` SHA.

---

# PHASE 3: P3 ITEMS — CLEANUP, PROPOSALS, POLISH

Estimated effort: 2–3 sessions. No blockers. Can be done in any order.

**Simulation-relevant items (complete before Phase 4 if capacity allows):** 3.1, 3.2, 3.9, 3.11. These affect simulation accuracy — incorrect action priority (3.1), wrong stat names (3.2), wrong track name (3.9), or missing tracks in the registry (3.11) produce simulation errors.

## 3.1 — Combat §4 Action Priority Resolution [AUD-COM-01] ⚠ SIM-RELEVANT
**Problem:** §4 has a priority table (Strike = Priority 1, Feint = 2, etc.) AND §2 states all declarations are simultaneous. A note in the doc says "THIS DOESN'T MAKE SENSE RE PRIORITY. IT'S ALL SIMULTANEOUS." This is an unresolved internal contradiction in a canonical doc.
**Resolution options:** (A) Remove the priority table — all actions resolve simultaneously as §2 states. (B) Redefine priority as resolution order within simultaneous declarations — actions are declared simultaneously but resolve in priority order (Strike first, then Feint, then Disarm, etc.). Option B adds tactical depth (a Rescue at Priority 3 resolves before a Strike at Priority 1 targeting the same character) but complicates the simultaneous model.
**Action:** Choose A or B and implement. Propagate to params_combat.

## 3.2 — Combat §9 Stat Name Propagation [AUD-COM-02] ⚠ SIM-RELEVANT
Rename Strength→Size, CP→Power, Cohesion→Discipline, Morale→Morale in combat §9 unit stat block to match mass_battle PP-232 renames. Simple find-replace within one section.

## 3.3 — Combat §9 Deprecated Doc Reference [AUD-COM-03]
Replace PP-089/090 reference to `deprecated/compilation/v0.14/stage11_scale_transitions_deprecated.md` with reference to `designs/architecture/scale_transitions_v30.md`. The relevant content (Hybrid Phase Order and Mode-Switch) should be in scale_transitions_v30 — if it's not, migrate it.

## 3.4 — Stamina Merge Proposal [AUD-COM-05]
**Proposal:** Evaluate merging Stamina into Combat Pool depletion. Currently combat tracks three resources: pool dice (allocated per round), wound progress (accumulated damage within current wound interval), and Stamina (depletes 1/round, 0 = Out of Breath = −2D). Stamina could be folded into pool depletion: each round, pool depletes by 1 (fatigue). Take a Breath restores Endurance dice. Armor penalty applies as starting pool reduction rather than Stamina modifier. This eliminates one tracking axis without losing the tactical decision.
**Action:** Write design proposal with pros/cons. If approved, implement and simulate.

## 3.5 — Social Contest §1 Core Principle [AUD-SC-01]
§1 (Core Principle: Format Follows Context) is empty — no text. Either write the philosophical foundation (~200 words explaining why contests use exchange structure rather than single rolls: the exchange structure models the iterative nature of persuasion, where each argument responds to the prior) or strike the section header.

## 3.6 — N-Way Opposing Operations [AUD-TW-03]
**Current rule:** 3+ practitioners with opposing intentionalities on the same configuration = automatic lattice collapse. All operations fail. Gap forms at target's scale. MS −(2 × number of practitioners).
**Concern:** This is a blunt ceiling that prevents degenerate scenarios but also prevents interesting 3-way Thread conflicts. A 3-way Weaving contest (Crown practitioner + Varfell practitioner + Warden, all targeting the same configuration with different intentions) could produce rich emergent outcomes.
**Proposal:** Graduated collapse: 3 practitioners = contested resolution at +2 Ob each (hard but not impossible); 4+ = auto-collapse (current rule). Write design proposal.

## 3.7 — Independent Player Path [AUD-PA-02]
**Current state:** An independent character (no faction) generates Scene Slate entries from Convictions only (max 3 scenes from §4.2 Step 4) plus territorial (1–2) and ambient (1). Total: ~5 scenes. Faction-aligned characters get 7–9. The independent path is thinner by design — but is this documented as an intentional difficulty increase?
**Action:** Either document "thin Slate is the intended independent difficulty" in player_agency §5.3, or add supplementary scene sources for independent characters (e.g., Renown-gated NPC Outreach — at Renown 3+, NPCs seek out the independent character based on personal reputation rather than faction status).

## 3.8 — Conviction Crisis Table Weighting [AUD-NPC-04]
**Current rule:** At 3+ Conviction Scars, NPC decisions use a flat d6 table (1–2 primary, 3–4 secondary, 5 Autonomy, 6 relational pull). This means a Faith NPC with 3 Scars has equal probability of acting on Faith (33%) as acting on Autonomy (17%) or relational pull (17%).
**Concern:** Flat d6 may produce faction-incoherent behavior — a Crown NPC acting on Autonomy takes self-preservation actions that contradict Crown institutional interests.
**Proposal:** Weight the table by Scar source: if Scars came from Evidence targeting, weight toward Reason-adjacent behavior; if from Solidarity, weight toward relational. Or: Conviction-indexed d6 where the NPC's current primary Conviction gets weight 1–3 (50%) and all other options share the remaining 50%.

## 3.9 — CV→PT Terminology Unification [AUD-CT-01] ⚠ SIM-RELEVANT
conviction_track_v30 uses "CV" throughout. Newer docs (tc_political_redesign, victory_v30, peninsular_strain) use "PT." ED-644 acknowledges equivalence but defers the rename. A developer (or simulation framework) reading both docs must know CV and PT are the same stat.
**Action:** Rename CV→PT throughout conviction_track_v30. Consider file rename conviction_track_v30.md → piety_track_v30.md (requires canonical_sources, propagation_map, file_index updates).

## 3.10 — Coherence → Recall → Skill Access [AUD-CH-01]
**Concern:** Coherence degradation at Fragmented (4–3) applies "effective Recall −1" and at Fractured/Severed (2–1) applies "effective Recall −2." Recall governs skill access via the sparking system (learning speed = floor(Recall/2) bonus dice). A practitioner at Coherence 3 with Recall 3 has effective Recall 2 → floor(2/2) = +1D learning. At Coherence 2 with Recall 3: effective Recall 1 → +0D. A practitioner who invested heavily in Thread operations may lose access to skills they depend on for non-Thread activities.
**Action:** Map common practitioner builds (Spirit 5+, Focus 4+, typical Recall 2–4) against Coherence thresholds. Verify that critical skills (combat, fieldwork investigation, governance) remain accessible at Coherence 4–3. If a typical practitioner loses combat skills at Coherence 4, the penalty may be too harsh — consider: Recall reduction applies only to Thread-related skill checks, not all skills.

## 3.11 — Clock Registry: Settlement Derived Tracks [AUD-CK-01] ⚠ SIM-RELEVANT
Settlement stats (Prosperity/Defense/Order) have derived values defined in derived_stats_v30 §4 (Local Economy, Garrison Strength, Public Order) but these aren't listed in the clock registry. The registry is the single source of truth for all tracked values — the simulation framework will read it to initialize state.
**Action:** Add Local Economy, Garrison Strength, Public Order to clock_registry_v30 Settlement Tracks section.

## 3.12 — Mass Battle §A.5 Deduplication [AUD-MB-01]
The PP-249 Coherence/Command clarification paragraph appears twice verbatim in §A.5. Remove the duplicate.

## 3.13 — T6 Throughline Tag Assignment
Throughline tags jump from T5 (Martial Law at Settlement Level) to T7 (Local Actors). No T6 designation exists. This may correspond to TL-6 (Hall Tier Settlement Integration) from the numbered throughline scheme — but TL-6 and T6 are different numbering systems.
**Action:** Either assign T6 = Hall Tier (aligning the two schemes) or formally strike T6 with a note that TL-6 covers this space.

## 3.14 — Simultaneous Domain Echo Cap Verification [AUD-ST-01]
**Concern:** The 1-Echo-per-scene-per-faction cap (PP-329) and the ±2 per-stat-per-Echo cap interact. If a player triggers Sufficient Scope in 3 different scenes in one season (each involving a different faction), up to 3 Echoes fire. Each is capped at ±2 per stat. But do the 3 Echoes stack on the same stat? (E.g., Combat Domain Echo +1 Mandate in scene 1, Investigation Domain Echo +1 Mandate in scene 2, Contest Domain Echo +1 Mandate in scene 3 = total +3 Mandate from Echoes this season?) The seasonal faction-attribute cap of ±2 per season (scale_transitions §5, from stage11 §11.5) should govern — but the interaction isn't explicitly tested.
**Action:** Construct the scenario. Apply the cap rules. Verify the correct maximum is ±2 per stat per season from all Echo sources combined.

## 3.15 — Fieldwork Demand Deflection Ob [AUD-FW-01]
**Concern:** NPC Demand deflection Ob = floor(NPC highest stat ÷ 2) + 2. Against a Stat 6 NPC: Ob 5. A mid-game character with Attunement 4 + History 3 has pool = (4×2)+3+3 = 14D. At TN 7, 14D vs Ob 5: ~49% success. This is challenging but not impossible. Against a Stat 7 NPC: Ob 5.5 → 6 (if rounded up). 14D vs Ob 6: ~35%. Harder. Against Stat 4: Ob 4. 14D vs Ob 4: ~72%. Manageable.
**Action:** Simulate across pool sizes 8–14D and NPC stats 3–7. If deflection is <20% success rate at any reasonable pool size, reduce the formula (e.g., floor(stat ÷ 2) + 1 instead of + 2).

## 3.16 — Thread-Read Investigation Superiority [AUD-FW-02]
**Concern:** Thread-Read at Depth ≥ 4 provides +2/+3 Evidence Track progress per action (same as conventional investigation) but also fires co-movement and advances Coherence degradation. The P1-16 ruling gates Thread-Read to Depth ≥ 4 questions only, which prevents it from trivializing mundane investigation. But at Depth 4+, Thread-Read has no additional cost beyond the standard co-movement — it's strictly superior to conventional investigation for any Thread-related question.
**Proposal:** Thread-Read Evidence Track progress at ×0.5 (round down) for investigation questions that don't directly concern Thread phenomena. Thread-Read remains full-progress for Thread-specific questions (Gap investigation, practitioner identification, Dissolution forensics). This preserves Thread-Read's unique value for Thread topics while preventing it from dominating general investigation.

## 3.17 — Victory Accord Rule Consolidation [AUD-VIC-01]
Accord rules are split across victory_v30 §0.2 and peninsular_strain_v30 §2. A developer implementing Accord must read both documents. Either add explicit cross-references ("Full Accord rules: see peninsular_strain_v30 §2") to victory_v30 §0.2, or move all Accord rules to one canonical location and have the other reference it.

## 3.18 — NPE Volatility Convergence [AUD-INV-01]
**Concern:** The NPC Population Engine (investigation_systems) has an off-screen social pressure mechanic: at season end, NPCs with shared worldview and adjacent Stance positions make a Volatility check, and on pass, both shift toward each other's Stance by 1. Over 30+ seasons, this convergence may flatten NPC diversity — all NPCs in a high-Piety territory converge to Church-aligned positions, eliminating the heterodox NPCs that make investigation interesting.
**Action:** Simulate the convergence mechanic over 30 seasons in a territory with starting ecology weights (e.g., T9 Himmelenger: 60% Church-aligned, 20% neutral, 20% heterodox). Track Stance distribution at seasons 10, 20, 30. If heterodox population drops below 5% by season 20, add a divergence mechanic: per-season random events that shift 1–2 individual NPCs against the local consensus (representing external influence, personal crisis, or exposure to new information).

---

# PHASE 4: FULL-CAMPAIGN SIMULATION FRAMEWORK

Estimated effort: 8–12 sessions. This is the single biggest remaining risk AND the single most valuable pre-implementation investment.

**Hard dependencies:** Phase 1 complete, Phase 2.2 (Co-Movement calibration) complete, Phase 0.7 (params refresh) complete. Sim-relevant Phase 3 items (3.1, 3.2, 3.9, 3.11) strongly recommended.

**Scope:** A 30-year (120-season) campaign simulator exercising every gameplay feature. Not a single simulation — a reusable framework with configurable player policies, faction configurations, and random seeds.

**Mode:** The simulator models Hybrid mode — the Godot videogame's primary mode (BG strategic layer + TTRPG personal scenes via Zoom In/Out). Pure TTRPG and pure BG are subsets of Hybrid. Mode transition rules (scale_transitions §6) are exercised through Zoom In/Out triggers in the feature checklist.

---

## 4.0 — Framework Architecture

**Season loop (×120):**

```
SEASON LOOP:
  Phase 0: Briefing
    ├── Read global clocks (MS, CI, IP, PI, Strain)
    ├── Read faction states (stats, derived values, units, territories, card hands)
    ├── Read settlement states (P/D/O, governors, facilities, Church infrastructure)
    ├── Read NPC states (Disposition, Scars, Beliefs, arc position, Coherence, TS, alive/dead)
    └── Read PC state (attributes, skills, Wounds, Stamina, Coherence, TS, Momentum,
        Convictions, Duties, Standing, Resources, Knots, Renown, companions)

  Phase 1a: Duty Assignment
    ├── Faction AI evaluates priority tree → assigns Duty to PC
    └── If Standing 0: Initiation Duty gate

  Phase 1b: Scene Slate Generation (player_agency §4.2)
    ├── Step 1: Mandatory Crisis (Priority 0) — check all 7 mandatory Zoom In triggers
    ├── Step 2: Crisis Events (Priority 1) — Accord, Scar count, arc triggers, clock thresholds
    ├── Step 2b: Thread-State Scenes — MS band, Gaps, Locks, WC
    ├── Step 3: Duty-Aligned (Priority 2)
    ├── Step 4: Conviction-Aligned (Priority 3) — scan Conviction text against game state
    ├── Step 5: NPC Outreach/Demand (Priority 3) — Disposition/priority tree conditions
    ├── Step 6: Territorial (Priority 4)
    └── Step 7: Ambient (Priority 5)

  Phase 1c: Personal Phase — PLAYER ACTIONS (3–5 scene actions)
    For each scene action, player policy selects a scene and resolves it:
    ├── FIELDWORK SCENE: select action type →
    │     Exploration: pool roll vs Depth Ob → POI discovery/failure + Exposure
    │     Investigation: pool roll vs Depth Ob → Evidence Track ±progress + Exposure
    │     Socializing: pool roll vs action Ob → Disposition shift + information gate
    │     Thread-Read: Leap roll → Spirit pool → co-movement + Evidence + Coherence
    ├── COMBAT SCENE: initiative → rounds of pool-split/roll/damage →
    │     Wound tracking, Stamina, incapacitation stages →
    │     Post-combat: Death Cascade if kill, Combat Reputation, Settlement Echo, Domain Echo
    ├── CONTEST SCENE: setup (adjudicator, genre, resistance) → exchanges →
    │     Argue rolls, CLASH/REINFORCE/CROSS/TIE resolution →
    │     Track movement, strain, Concentration → outcome (Decisive/Compromise) →
    │     Obligation, Conviction Scar, Domain Echo, Chain Contest generation
    ├── THREAD SCENE: Leap roll → Contact Duration → operations →
    │     Weaving/Pulling/POP/Locking/Dissolution/Mending degree tables →
    │     Coherence loss, MS change, Co-Movement card draw, co-movement 3-axis →
    │     Opposing Operations (if contested) → Settlement Echo, Thread Domain Echo
    ├── MASS BATTLE: 7-phase turn structure →
    │     Strategy → Volley → Manoeuvre → Thread → Engagement → Cascade → Reform →
    │     Unit damage, Discipline/Morale checks, General Duel (if triggered) →
    │     Rout/Pursuit, Morale Cascade, battle consequences →
    │     Territory control change, MS cost, IP/Strain advancement
    ├── GOVERNANCE SCENE: Develop/Fortify/Pacify/Administer →
    │     Settlement stat change → Order → Accord recalculation
    └── COMPANION SCENE: companion interaction → Disposition/Conviction/departure

  Phase 2: Strategic Phase — FACTION AI
    For each active faction (Crown, Church, Hafenmark, Varfell + conditionals):
    ├── Check conditional faction activation:
    │     Löwenritter: Coup Counter = 3 → activate with §8.7 priority tree
    │     RM: Popular Will threshold → Founding → activate with §8.9 tree
    │     Altonian Vanguard: IP threshold → activate with §8.8 tree
    │     Wardens: WC threshold → activate with §8.10 tree
    │     Each activated faction joins the priority tree loop
    ├── Card-hand constraint: select Domain Action from available cards only
    │     (4 shared + 2 faction-specific per faction per season)
    ├── Priority tree evaluation (npc_behavior §8.2–8.10)
    ├── Domain Action selection and resolution (faction stat pool vs Ob)
    ├── Military orders (Muster, March, Battle — subject to Levy Restriction)
    ├── Thread orders (Varfell: VTM advancement; Church: Attention Pool)
    ├── Diplomatic actions (Treaty, Intel, Seizure — subject to card availability)
    ├── Apply Framework Drift (passive stat changes per faction ethical framework)
    └── Card hand refresh

  Phase 3: Accounting — CASCADE (13 steps)
    ├── Step 1: Derived value income/drain calculation (all factions, all settlements)
    ├── Step 2: Stat damage checks (derived value at 0 → stat −1 triggers)
    ├── Step 3: Domain Echo application (queued from Phase 1c/2)
    ├── Step 4a: CI calculation (Church infrastructure + PT-based generation)
    ├── Step 4b: PT movement (faction actions + Calamity Drift + Thread Op CV Drift)
    ├── Step 4c: Accord Domain Echoes → settlement Order recalculation → Accord
    ├── Step 4d: Turmoil advancement
    ├── Step 4e: IP advancement (inter-faction battle check)
    ├── Step 5: MS update (Thread operations + battle costs + Calamity Drift)
    ├── Step 6: NPC arc evaluation (Scar count, Stability triggers, Certainty shifts)
    ├── Step 6b: NPC death/replacement — if named NPC died this season:
    │     check succession per arc profiles (npc_behavior §5.2),
    │     generate replacement NPC if faction requires a leader/officer,
    │     track roster size against 30-NPC cap (npc_behavior §11),
    │     Background-tier demotion if over cap
    ├── Step 7: Obligation tracking (duration countdown, violation check)
    ├── Step 8: Victory condition check (all factions, universal + faction-specific)
    ├── Step 9: Exposure reset (per territory)
    ├── Step 10: Seasonal clock ticks (VTM, Altonian diplomacy, Torben Loyalty, Coup Counter, etc.)
    ├── Step 11: Coherence recovery check (full season of non-practice → +1)
    ├── Step 12: Seasonal event generation — per settlement d6 roll:
    │     1 = negative event (Prosperity −1 or Order −1, 50/50)
    │     6 = positive event (Prosperity +1 or Trade opportunity)
    │     2–5 = no event
    │     Events generate Scene Slate entries for next season. Affect derived values.
    └── Step 13: Knot strain from NPC arc transformations (per npc_behavior §5.0b)

  Phase 4: Aftermath
    ├── Conviction revision opportunity (player policy decides whether to revise)
    ├── Companion scene (if companion present — may fire departure if conditions met)
    ├── Standing advancement/loss evaluation (Duty success/failure → Standing ±1)
    ├── Renown update (per player_agency §5.4 sources)
    ├── "Where Were You?" retrospective generation (for missed events)
    ├── Portrait Retirement option check (≥2 Convictions resolved, non-Unresolved)
    └── Character death check → if dead: Conviction Legacy → new character init
```

---

## 4.1 — State Initialization

**Task:** Build the game-start state from canonical sources. **Validate every loaded value against its canonical source doc.** If a params file value doesn't match the design doc, flag the discrepancy and use the design doc value (it is authoritative per canonical_sources.yaml).

**Global clocks:** MS 72, CI 28, IP 5, PI 7, Strain 0 (from clock_registry_v30).

**Faction stats (4 playable + 4 conditional):**

| Faction | Man | Wea | Mil | Inf | Sta | Territories | Status |
|---------|-----|-----|-----|-----|-----|-------------|--------|
| Crown | 5 | 4 | 4 | 5 | 4 | T1,T2,T3,T5,T6,T14 (6) | Active |
| Church | 4 | 3 | 4 | 6 | 5 | T9 (1) | Active |
| Hafenmark | 4 | 5 | 3 | 4 | 4 | T7,T8,T10,T17 (4) | Active |
| Varfell | 3 | 3 | 4 | 3 | 3 | T4,T11,T12,T13 (4) | Active |
| Löwenritter | — | — | — | — | — | — | Dormant (Coup Counter 0) |
| RM | — | — | — | — | — | — | Dormant (Popular Will 0) |
| Altonian | — | — | — | — | — | — | Dormant (IP 5) |
| Wardens | — | — | — | — | — | — | Dormant (WC 0) |

**Derived values:** Calculated per derived_stats_v30 §2 (Treasury = Wealth × 100, Legitimacy = Mandate × 20, etc.).

**Card hands:** 4 shared + 2 faction-specific per faction (mass_battle §B.4). Cards refresh each season.

**36 settlements:** Per settlement_layer §2.1 registry (P/D/O starting values, type, controller, Church infrastructure axes). Derived values: Local Economy = Prosperity × 50, Garrison Strength = Defense × 20 + Fort Level × 30, Public Order = Order × 20.

**15 territory tracks:** PT per conviction_track §1.1, Fort Level per geography, Prosperity per params_board_game, Church AP all 0.

**14 named NPCs:** Initialize per npc_behavior §2: Conviction (primary + secondary), Resonant Style (primary + secondary), Ethical Framework, TS, Certainty, 3 Beliefs, Disposition 0 toward PC, Scar count 0, arc position A (default).

**PC:** Generated per character_histories lifepath. Configurable origin/formation/vocation/catalyst. Starting attributes (7 attributes, 1–7 each), skills (per lifepath), Certainty (per origin), TS (per origin — 0 for most, +5/+8 for Einhir Descendant), 3 Convictions (player-authored), 3 Knots (per lifepath stages 1–3), Standing 0, Resources (per background, 1–3), Momentum 0.

---

## 4.2 — Season Resolution Engine

**Task:** Implement the season loop described in §4.0. Each season resolves all phases in sequence. State changes are recorded for post-run analysis.

**Player policy system (10 configurable):**

| Policy | Scene Priority | What It Tests |
|--------|---------------|---------------|
| **Investigator** | Fieldwork first, avoid combat, use Thread-Read when TS ≥ 30 | Fieldwork pacing, Evidence Track completion, Exposure management, Thread-Read vs conventional |
| **Warrior** | Combat first, accept military Duties, join mass battles, build Combat Rep | Combat frequency, Death Cascade rate, Combat Reputation trajectory, wound/recovery |
| **Diplomat** | Contest + socializing, build Disposition with faction leaders, seek Standing | Contest outcomes, Obligation generation, Standing progression, NPC arc influence |
| **Practitioner** | Thread first, 2+ ops/season, pursue Mending, accept Coherence risk | Coherence curve, MS impact, Co-Movement variance, Rendering Crisis timing |
| **Governor** | Governance Duties, develop settlements, build institutional Standing | Settlement stats, Prosperity→Treasury, Order→Accord, facility slot pressure |
| **Balanced** | Equal weight all types, accept Duties and pursue Convictions | The "intended" playstyle — balanced mix without specialization |
| **Independent** | No faction, Convictions only, build Renown to 7+ | Independent viability, Slate thinness, Renown progression without faction |
| **Aggressive** | Military expansion, conquer by force, ignore Accord | Conquest death spiral, Campaign Supply drain, Accord 1 penalty |
| **Theocrat** | Church, maximize CI, rush Graduated Seizure | Church victory timeline, CI acceleration, counter-pressure |
| **Restorationist** | RM, Cultural Reclamation + Community Weaving, Phase 1/2 victory | RM victory probability, PT erosion vs CI advancement, Founding timing |

**Run configuration:** 10 policies × 5 random seeds = **50 campaign runs** for baseline analysis.

---

## 4.3 — Feature Coverage Checklist

Every feature must fire at least once across the 50 campaign runs. This checklist tracks coverage:

### Personal Scale (11 items)
- [ ] All combat actions (Strike, Defend, Feint, Disarm, Rescue, Dodge, Full Guard, Take a Breath, Establish Distance, Escape, Tie Up)
- [ ] Wound accumulation across wound intervals → incapacitation (Stage 1 → Stage 2)
- [ ] Stamina depletion → Out of Breath → recovery via Take a Breath
- [ ] Fibonacci group bonus (3+ combatants engaging single target)
- [ ] Death Cascade (named NPC killed: 5-step cascade — Knot rupture, Scene Slate, faction Stability, Exposure, Conviction)
- [ ] Combat Reputation accumulation → NPC behavior modification (Rep 2+ → NPCs avoid combat)
- [ ] Combat Domain Echo (kill/defeat faction officer → faction stat shift)
- [ ] Settlement Combat Consequences (public combat → Order −1)
- [ ] Fled combat → battle site becomes POI with evidence degradation (ED-576)
- [ ] Weapon TN matrix differentiation (at least 3 different weapon profiles used across runs)
- [ ] Armor DR interaction (at least Light, Medium, Heavy armor encountered)

### Fieldwork (13 items)
- [ ] Exploration at Depth 0, 1, 2, 3, 4, 5 (each depth accessed at least once)
- [ ] All 6 investigation actions: Examine, Interview, Research, Surveil, Thread-Read, Reconstruct
- [ ] Evidence Track completion at all 3 thresholds (Simple 3, Complex 5, Structural 8)
- [ ] Failed Reconstruct (wrong conclusion — player acts on false information)
- [ ] Desperate Trail activation (3 consecutive failures → TN 8)
- [ ] All 7 social actions: Read, Converse, Connect, Impress, Rumour, Negotiate, Gift/Bribe
- [ ] Disposition progression from −3 to +5 (full range traversed across runs)
- [ ] Sincerity Gate (Spirit check on instrumental socializing — at least 1 failure producing consequences)
- [ ] Exposure accumulation → Noticed → Watched → Compromised (all 3 thresholds crossed)
- [ ] NPC-Initiated Social: Outreach scene (Disp ≥ +2), Demand scene (Disp ≤ −2), deflection attempt
- [ ] Knot formation during play (once Phase 1.1 resolved)
- [ ] Investigation Domain Echo (Finding with faction-level scope → stat change)
- [ ] Combined Findings cited in Contest (+1D/Finding, max +2D)

### Social Contest (14 items)
- [ ] All 4 interaction types: CLASH, REINFORCE, CROSS, TIE
- [ ] All 3 adjudicator types: Expert Judge (Cognition), Crowd (Charisma), No Adjudicator (Attunement)
- [ ] Genre bonus + audience boost (+1D each, max +2D combined)
- [ ] Recall bonus (+2D from Documentary evidence citation)
- [ ] Grand Contest Recall (once-per-source exhaustion across 5 exchanges)
- [ ] Composure threshold crossed → Rattled (+1 Ob cumulative)
- [ ] Concentration depletion → Spent (−2D next exchange)
- [ ] Forfeit actions: Regroup (restore Concentration) and Concede a Point (+1D next exchange)
- [ ] Piety Track → Decisive win (≥7 or ≤3) → Obligation generated
- [ ] Piety Track → Compromise (4–6) → Chain Contest generated for next season
- [ ] Deadlock stall-break (ED-582): 2 zero-movement exchanges → Resistance drop → 3rd → forced Compromise
- [ ] Conviction Scar via correct Resonant Style targeting (at least 1 per run)
- [ ] Debate Domain Echo (Decisive → Winner/Loser Mandate ±1)
- [ ] Total Victory effects (Track ≥9 or ≤1: Contest Fatigue, Momentum, Disposition shift)

### Threadwork (16 items)
- [ ] Leap at all 4 degrees: Overwhelming / Success / Partial / Failure
- [ ] All 5 operations performed: Weaving, Pulling, POP (Past-Oriented Pulling), Locking, Dissolution
- [ ] Mending at multiple Gap severities (Shifting Object, Micro-Gap, Standard Gap, Entrenched)
- [ ] Collective operations (Anchor + at least 1 helper)
- [ ] Opposing Operations (contested Thread — at least 1 contested engagement)
- [ ] Co-Movement card draw covering all 18 cards (across 50 runs)
- [ ] Coherence degradation through all thresholds (10→8→5→3→2→1→0 — at least 1 Rendering Crisis)
- [ ] Coherence recovery (+1/season non-practice AND +1 from Anchoring Scene)
- [ ] Rendering Crisis resolution (4-beat narrative arc: Withdrawal → Knot Anchoring → Place Anchoring → The Choice)
- [ ] TS advancement (at least 1 practitioner crosses 30 or 50 threshold)
- [ ] Over-Actualisation triggered (Relational+ Weaving → +1 Ob to subsequent operations on same config)
- [ ] Dissolution residue used (bonus dice + Coherence cost)
- [ ] Thread Domain Echo (Dissolution → Stability −1 or Mending → Mandate +1)
- [ ] Thread Operation CV Drift (public Dissolution → PT −1)
- [ ] Wound disruption during contact (Spirit check when Wounded in Leap)
- [ ] Thread perception visibility table exercised (TS 0/10/30/50/70+ producing different perceptions)

### Mass Battle (14 items)
- [ ] All 7 phases executed: Strategy → Volley → Manoeuvre → Thread → Engagement → Cascade → Reform
- [ ] All formations used: Line, Shield Wall, Wedge, Skirmish, Column, Feigned Retreat, Reserve
- [ ] All tactics used: Envelopment, Feigned Retreat, Ambush, Concentration, Refused Flank, Hammer & Anvil
- [ ] General Duel (personal combat within mass battle via §3.7)
- [ ] General death (Stage 1 → Stage 2, −2 Morale all units, Command = 0)
- [ ] Morale Cascade (unit rout → Discipline Ob 1 check → adjacent Morale −1)
- [ ] Discipline degradation (deterministic: Size loss > Discipline + asymmetric loss)
- [ ] Campaign Supply (Treasury −100/season in hostile territory)
- [ ] Levy Restriction (Levy units cannot campaign offensively outside home territory)
- [ ] Siege (attacker Treasury drain + defender attrition at Prosperity 0)
- [ ] BG battle resolution (single-roll abstraction with tactic cards)
- [ ] Hybrid handoff (Zoom In at phase-lock points: after Phase 1, after Phase 3, after Phase 6 Step 1)
- [ ] Thread operations in mass battle (Phase 4 offensive, Phase 6 support)
- [ ] Battle consequences (MS −1/−2, IP +2, Strain +1, territory control, Accord set to 1)

### Scale Transitions (8 items)
- [ ] All 11 upward transitions (DE-1 through DE-11) fired at least once
- [ ] All 9 downward transitions (ZI-1 through ZI-9) fired at least once
- [ ] All 10 lateral transitions (LT-1 through LT-10) fired at least once
- [ ] Zoom In at all 3 legal entry points (after Phase 1, after Phase 3, after Phase 6 Step 1)
- [ ] Zoom Out with correct state transfer (personal outcomes → Domain Echo → Accounting)
- [ ] "Where Were You?" retrospective scene generated and delivered through appropriate channel
- [ ] Sufficient Scope tested: all 7 conditions fire at least once across runs
- [ ] Domain Echo timing difference: TTRPG immediate vs Hybrid queued-to-Accounting

### Player Agency (10 items)
- [ ] Conviction creation, pursuit (Momentum granted), fulfillment, failure, transformation, unresolved (all 4 resolution states)
- [ ] Conviction strain from NPC contest victory using Resonant Style (player Conviction shaken)
- [ ] Duty assignment, success (+Standing), failure (−Standing), exceeding (+2 Standing)
- [ ] Standing progression 0→7 (at least one Diplomat or Governor policy run reaches Standing 6+)
- [ ] Scene Slate generation at each priority level (0, 1, 2, 3, 4, 5 — all levels produce entries)
- [ ] Opportunities not pursued → NPC AI resolution (consequences without player input)
- [ ] Stature progression → leadership acquisition (Standing 7 → faction leader offer)
- [ ] Scene Action Budget at each difficulty level (3/Hard, 4/Normal, 5/Narrative)
- [ ] Portrait Retirement trigger (≥2 Convictions resolved + ≥2 scene actions per Conviction)
- [ ] Conviction Legacy (character death → new character with transformed Conviction)

### NPC Behavior (9 items)
- [ ] All 14 named NPCs: at least 1 arc transition per 50-run baseline
- [ ] Conviction crisis (3+ Scars → d6 table → unpredictable behavior)
- [ ] Belief revision (decisive contest via Resonant Style → Belief rewritten)
- [ ] All 4 Resonant Styles targeted: Evidence, Consequence, Authority, Solidarity
- [ ] Framework Drift (all 4 faction frameworks produce passive stat changes)
- [ ] Constrained sub-arc (Mandate < 3 → expansion priorities suspended)
- [ ] NPC Outreach generation (Disposition ≥ +2 NPC seeks player)
- [ ] NPC Demand generation (Disposition ≤ −2 NPC summons player)
- [ ] Faction elimination (Stability 0 → NPC Autonomy collapse → unaffiliated actors)

### Settlement & Governance (10 items)
- [ ] All 4 governance actions: Develop (Prosperity), Fortify (Defense), Pacify (Order), Administer (maintenance)
- [ ] Settlement stat progression across full range (0→5 for at least one stat in one settlement)
- [ ] Order → Accord derivation (floor of mean settlement Order) producing correct province Accord
- [ ] Institutional Facility slot pressure (full capacity → pending rank scenario)
- [ ] Church infrastructure growth across all 4 axes (Religious Building, Templar, Inquisitor, Governor)
- [ ] Parish Social Services (Church building → Order bonus applied)
- [ ] Pastoral Assumption (governance vacuum + Church infrastructure → Church Governor installed at Ob 1)
- [ ] RM Cell Resilience (+1 Ob to suppression when RM has Presence in ≥3 settlements in province)
- [ ] Subnational faction governance (grant management to Guild/Church/Löwenritter + revoke)
- [ ] Companion-as-governor (1 free action/season, social OR governance)

### Victory & Endgame (12 items)
- [ ] Universal victory condition checked each Accounting (Peninsular Sovereignty: 15 territories, Accord ≥2, Strain ≤6, held 2 Accountings)
- [ ] Crown-specific victory (TCV ≥14, rival suppression, IP <60, PI ≥3)
- [ ] Church-specific victory (TCV ≥8, PT ≥3 in all held, Accord ≥3 in ≥3 non-capitals)
- [ ] Hafenmark-specific victory (TCV ≥13, Mandate ≥4, Stability ≥3, PI ≥5, Crown Mandate ≤3)
- [ ] Varfell Path A (Intelligence Hegemony), Path B (Southernmost), Path C (Thread Supremacy)
- [ ] RM Phase 1 (Cultural Majority) → Phase 2 (Cultural Uprising) → victory
- [ ] Co-victory (at least one compatible pairing achieves partition conditions)
- [ ] Peninsular Sovereignty achieved and held for 2 consecutive Accountings
- [ ] Faction elimination (Stability 0 → faction removed from play)
- [ ] Altonian Vanguard emergence (IP crosses threshold → invasion force activates)
- [ ] Löwenritter Coup (Coup Counter = 3 → Crown faction under Löwenritter control)
- [ ] Total Domination (all other factions eliminated — extreme edge case)

### Derived Stats Economy (8 items)
- [ ] Treasury income/drain cycle (Prosperity income, Trade, Haushalt, unit upkeep, Campaign Supply, Muster, construction)
- [ ] Legitimacy income/drain cycle (Accord-based income, Govern, emergency invocation drain)
- [ ] Reputation income/drain cycle (diplomatic relationship income, Intel/Diplomacy, exposure drain)
- [ ] Discipline income/drain cycle (peaceful season income, battle loss drain, crisis drain)
- [ ] Levies Available ceiling enforcement (Military ×2 cap, disband if over)
- [ ] Stat damage from derived value depletion (Treasury 0 stays through Accounting → Wealth −1)
- [ ] Settlement derived values (Local Economy → Treasury income, Garrison Strength display, Public Order → riot events)
- [ ] Haushalt Competence income with cap (Competence × 25, max Wealth × 50 per season — ED-663)

### Companion & Knot (8 items)
- [ ] Companion acquisition (Disposition ≥ +3 → Companionship Scene → acceptance)
- [ ] Companion combat AI (5-rule priority tree: wound guard, Rescue, aggressive, support, default)
- [ ] Companion departure scene (release or condition-triggered)
- [ ] Companion Proxy Command (PC general incapacitated → Cognition + History vs Ob 3)
- [ ] Knot formation → Solidarity Resonant Style activation
- [ ] Knot strain from NPC arc transformation (TS threshold crossing → strain per npc_behavior §5.0b)
- [ ] Knot rupture from Death Cascade (named NPC killed → all Knots rupture)
- [ ] Knot-mediated remote investigation (Thread-Read through Knot connection without physical presence)

### Character Lifecycle (5 items)
- [ ] Character creation via lifepath (all 4 stages producing attributes, skills, Certainty, TS, Knots)
- [ ] Skill sparking (SaGa-style: Spirit + floor(Recall/2) check after Ob ≥2 scenes)
- [ ] Certainty shifts (Thread exposure at Depth 3+, investigation revealing Thread reality, NPC Conviction engagement)
- [ ] Character death → Conviction Legacy → new character initialization
- [ ] Renown accumulation 0→10 (Conviction fulfillment, Duty exceeding, Domain Echo, NPC arc influence, investigation)

---

## 4.4 — Simulation Output & Analysis

**Per-run output:**
- Season-by-season state log (all tracked values, all state changes, all events fired)
- Clock trajectories (MS, CI, IP, PI, Strain over 120 seasons)
- Faction stat trajectories (each stat and derived value over time, per faction)
- NPC arc timeline (which NPCs transitioned, when, which arc, triggered by what)
- Victory condition proximity (how close each faction got to each condition, at what season)
- Player character lifecycle (Standing, Renown, Coherence, Wounds, Conviction resolutions, Knot count)
- Feature coverage bitmap (which checklist items fired this run)

**Cross-run analysis (50 runs):**
- Mean time-to-victory by faction and policy (target: Season 60–100 / Year 15–25)
- MS trajectory distribution: mean ± std dev. Target: Fractured band (39–20) reached between Season 40–80.
- CI trajectory distribution. Target: Graduated Seizure (CI 75) available between Season 30–60.
- Treasury depletion frequency: how often does any faction hit Treasury 0? Target: rare event (< 20% of runs), not routine.
- NPC arc transition frequency. Target: ≥4 of 14 named NPCs undergo arc transitions by Season 60.
- Feature coverage union: across all 50 runs, which checklist items fired? Target: 100%.
- Death spiral detection: any run where a faction enters unrecoverable decline before Season 30? Target: none.
- Stasis detection: any run where no faction stats change by >1 over a 10-season window? Target: none.
- Player impact: does the player's faction perform measurably better (2+ stat points, 1+ territory, or faster victory) than the same faction under AI-only control? Target: yes, in ≥80% of runs.

---

## 4.5 — Stress Tests (8 scenarios, run after baseline calibration)

### 4.5.1 — Church Theocracy Rush
Church AI maximizes CI every season (Preach + Assert + Church infrastructure investment). Player is Crown. Question: Does Crown AI + player intervention prevent Church from reaching CI 75 before Season 40? If not, what is the counter-strategy, and does the game provide sufficient tools?

### 4.5.2 — Military Conquest Death Spiral
Player conquers 3 territories by force in 5 seasons (Aggressive policy). All at Accord 1 (no Prosperity income contribution). Campaign Supply active (−100 Treasury/season). Question: Does Treasury reach 0 before Accord recovers to 2 through Govern actions? Is the economic penalty sufficient to deter pure military expansion?

### 4.5.3 — Thread Practitioner Coherence Arc
Player practitioner (Practitioner policy): 2 Thread operations per season for 15 seasons. Track Coherence trajectory. Questions: At what season does Rendering Crisis fire (Coherence 0)? After recovery (if successful), can the practitioner resume meaningful Thread work? At TS 30–35, does recovery cost Thread access permanently (TS −1 → TS 29, below Leap minimum)?

### 4.5.4 — Five-Faction Simultaneous Race
All 4 playable factions pursuing victory simultaneously. RM active as 5th faction (post-Founding). AI-only (no player). 20 runs with different seeds. Question: Which faction wins most often? Target per BALANCE-001: each wins 20–30% of the time. If any faction wins >40% or <10%, the victory architecture needs rebalancing.

### 4.5.5 — Altonian Invasion
IP reaches activation threshold. Altonian Vanguard activates and begins invasion. Question: How long do Valorian factions survive? Does the invasion create the intended "existential threat that forces cooperation" dynamic — do factions that were fighting each other redirect military resources against the Altonian threat?

### 4.5.6 — NPC Cascade
Player deliberately targets 3 named NPCs with Resonant Style contests across 3 seasons (producing 3 Conviction Scars each = Conviction Crisis for all 3 simultaneously). Question: Do the resulting arc transitions produce coherent narrative (3 NPCs simultaneously in crisis, each generating Scene Slate entries), or does the simultaneous crisis overwhelm the Scene Slate (too many Priority 1 entries, not enough scene actions to address them)?

### 4.5.7 — Settlement Economic Engine
Player governs 3 settlements for 20 seasons (Governor policy), maximizing Prosperity. Question: Does the settlement → Treasury income pipeline produce meaningful faction economic advantage? How does the governed faction's Treasury trajectory compare to an ungoverned faction? Does the independent path (Renown-based authority, no settlement governance) produce comparable economic outcomes through different means?

### 4.5.8 — Long Campaign NPC Turnover
Run for full 120 seasons (30 years). Question: How many of the 14 starting named NPCs survive to Season 100? Does the NPC roster capacity system (30-NPC cap, Background-tier demotion per npc_behavior §11) produce a recognizable cast at Season 100, or has turnover replaced everyone the player built relationships with? If turnover is too high, consider extending NPC lifespan or adding NPC "legacy" mechanics (children who inherit modified Stance Triangles).

---

## 4.6 — Calibration Report & Issue Triage

**Output:** `tests/sim_framework/calibration_report.md` — THE GATE DOCUMENT for Godot implementation.

**Contains:** Recommended multiplier adjustments (derived stat ×N values), clock speed tuning (CI/IP advancement rates), priority tree corrections (faction AI behavior fixes), feature coverage gaps (features that never fired), and all discovered design issues with severity triage.

**Issue triage protocol for sim-discovered issues:**
- **P1 (balance-critical):** Victory timing outside S60–100, death spirals before S30, stasis windows >10 seasons, feature coverage <100%, MS never reaches crisis. **Must resolve before Phase 5.** These become new Phase 1/2 items. Simulation re-runs after fixes (Phase 4.7).
- **P2 (system-specific):** Specific system behavior incorrect but doesn't affect overall balance. Resolve during Phase 5 or early Godot implementation.
- **P3 (cosmetic/theoretical):** Edge cases that rarely fire, minor numerical adjustments. Track but don't block.

---

## 4.7 — Regression Testing

**Trigger:** After any calibration adjustment from Phase 4.6 is committed to design docs.

**Protocol:**
1. Re-run Balanced policy × 5 seeds.
2. Verify: (a) all previously-passing calibration questions still pass, (b) no new death spirals or stasis introduced, (c) feature coverage union unchanged from baseline.
3. If regression fails: identify which adjustment caused the failure. Revert or iterate.
4. Repeat until regression clean.

**Exit criterion:** Balanced policy ×5 passes all calibration checks after final adjustments. No regressions.

---

## 4.8 — Simulation Infrastructure

**Implementation:** Python script. Not a Godot prototype — pure mechanical simulation. No graphics, no UI, no user interaction. Input: player policy + random seed. Output: season log + analysis.

**File structure:**
```
tests/
  sim_framework/
    engine.py           — season loop, phase sequencing, state management
    state.py            — game state: factions, settlements, NPCs, PC, clocks, card hands
    init_validator.py   — canonical value validation (§4.1 design doc comparison)
    faction_ai.py       — priority tree implementation for all factions (incl. 4 conditionals)
    scene_slate.py      — Scene Slate generation algorithm (player_agency §4.2)
    combat.py           — personal combat resolution (pool split, roll, damage, wounds)
    fieldwork.py        — fieldwork resolution (exploration, investigation, socializing)
    contest.py          — social contest exchange resolution (all interaction types)
    threadwork.py       — Thread operation resolution + Co-Movement card system
    mass_battle.py      — mass battle resolution (7-phase TTRPG + single-roll BG)
    domain_echo.py      — all 16 echo types + Sufficient Scope evaluation
    accounting.py       — 13-step Accounting sequence
    npc_arcs.py         — NPC arc state machine + death/replacement + roster management
    seasonal_events.py  — per-settlement random event generation
    player_policies.py  — 10 configurable player policies
    analysis.py         — cross-run analysis, calibration checks, regression verification
    coverage.py         — feature coverage bitmap tracking (~130 items)
  sim_results/
    baseline/           — 50 baseline runs (10 policies × 5 seeds)
    stress/             — 8 stress test scenario runs
    regression/         — post-adjustment verification runs
    calibration_report.md — THE GATE DOCUMENT
```

**Canonical source loading:** The simulator reads mechanical values from `params/*.md` files (refreshed in Phase 0.7). `init_validator.py` compares every loaded value against the canonical design doc and flags discrepancies before running. Design doc values are authoritative if discrepancy found.

---

# PHASE 5: GODOT IMPLEMENTATION PREP

Estimated effort: 3–4 sessions. Prerequisite: Phase 4 calibration report accepted (all calibration checks pass, no P1 issues remaining).

## 5.1 — GM-to-Engine Rule Conversion
**Why:** Multiple systems reference "GM" actions that don't exist in videogame mode. Each needs a deterministic engine rule.
**Instances:**
- Contest §2 Step 7: "GM records on hidden ledger" → engine handles all contest bookkeeping
- NPC Behavior §3.3: "GM judgment" for Scar progression → deterministic threshold: Scar fires on any decisive contest win via correct Resonant Style (binary, no GM discretion)
- Combat §4 Stunt: "GM sets N, max 5" → environmental modifier table indexed by POI type and terrain (e.g., Fortress interior +2, open field +0, Einhir ruins +3)
- Threadwork §3.6: "GM determines domain type" for Lock MS drift → domain-type lookup from settlement type (Seat = slow-change, Town = moderate, Outpost = fast-change)
- Fieldwork §4.1: "GM sets threshold at investigation opening" → threshold = scope-based (Simple 3, Complex 5, Structural 8) as already defined; the "GM sets" language is a TTRPG artifact
- Social Contest §2 Step 4: "GM narrates partial outcome proportional to final position" → outcome table indexed by final Piety Track position (4 = slight compromise toward A, 5 = true middle, 6 = slight compromise toward B)
- Investigation Systems: NPE "GM grants Belief revelation" → Belief revealed deterministically on Observation (NPC acts on Belief in player's presence) or Appraise Overwhelming
**Action:** For each instance, define the deterministic rule. Compile into a "Videogame Mode Appendix" or inline into each doc with `[VIDEOGAME: ...]` tags.

## 5.2 — Godot Implementation Sequence
**Why:** After calibration, developers need a build order for which systems to implement first.
**Recommended sequence (based on interdependency matrix — systems with highest fan-out built first):**
1. **Core engine** — dice pool resolution (d10, TN, Ob, degree table). Everything depends on this.
2. **State management** — all clocks, tracks, derived values. Use `sim_framework/state.py` as schema reference.
3. **Season loop + Scene Slate generation** — the game's session structure.
4. **Fieldwork** — highest player interaction frequency (60%+ of scene actions).
5. **Personal combat** — second-highest interaction frequency.
6. **Social contest** — third system the player encounters regularly.
7. **Threadwork** — unlocks for practitioner characters (TS 30+).
8. **Mass battle** — faction-scale combat (lower frequency than personal).
9. **NPC AI** — priority trees + arc state machines. Can run headless during development.
10. **Settlement governance** — requires settlement UI (Part 3 map view).
11. **Victory conditions** — requires all faction stats and clocks functional.
12. **UI/UX progressive disclosure** — capability-gated chrome. Build last because it wraps everything.

## 5.3 — Data Serialization Specification
**Why:** Design docs are markdown. Godot needs GDScript-compatible data structures (.tres/.res resource files).
**Action:** Define the format for translating design doc tables into Godot resources. Produce templates:
- `faction_data.tres` — stats (1–7), derived values, card hand, units, territories
- `settlement_data.tres` — all 36 settlements with type, stats (P/D/O), controller, Church infrastructure (4 axes), governor, facility slots
- `npc_data.tres` — all 14+ NPCs with Stance Triangle, Beliefs, TS, Certainty, Disposition, Scar count, arc state
- `weapon_data.tres` — TN matrix (3 axes × 2 values), DR tables, STR minimums, ranged weapon table
- `clock_data.tres` — all clocks/tracks with range, start, direction, source reference
- `territory_data.tres` — 15 territories with PT, Fort Level, Prosperity, Accord, Church AP
**Schema reference:** `sim_framework/state.py` data structures map 1:1 to these Godot resource schemas.

## 5.4 — Godot Scene Tree Architecture
**Why:** UI/UX v4.1 §1.1 defines 14 states (Main Menu, Character Creation, 8 season phases, Endgame, plus scene modes within Personal Phase). Each maps to a Godot scene or scene tree node.
**Action:** Produce `designs/godot/scene_tree_architecture.md` mapping each UI state to Godot scene tree implementation. Reference UI/UX v4.1 Appendix E (Godot Implementation Reference). Define: scene transitions (signals), shared state (autoloads), UI layer management (CanvasLayer hierarchy for persistent chrome vs modal scenes).

## 5.5 — Cross-Repo Propagation Protocol
**Why:** Design docs live in `jordanelias/ttrpg` (design source of truth). Godot implementation lives in `jordanelias/valoria-game`. No protocol exists for propagating design changes to implementation code.
**Action:** Define cross-repo protocol:
- ttrpg commit messages include `[GODOT-IMPACT: system]` tag when the change affects implementation (mechanical value changes, new rules, formula adjustments). Tag identifies which Godot system needs updating.
- `references/propagation_map.md` gets a new "Cross-Repo Propagation" section listing pending ttrpg→valoria-game updates.
- valoria-game maintains `design_sync.md` listing the ttrpg commit SHA it's current with. Any ttrpg commit with `[GODOT-IMPACT]` that postdates this SHA is a pending update.

---

# PHASE 6: ONGOING MAINTENANCE PROTOCOL

Not a one-time phase — a permanent protocol for the duration of Godot implementation and beyond.

## 6.1 — Session Start
Run inconsistency sweep (6 steps from HOW TO USE). Address any mismatches before new work.

## 6.2 — After Design Doc Changes
Run sim_framework regression (Phase 4.7 protocol). Verify no calibration regressions from the change.

## 6.3 — Per Commit
Follow standard commit protocol (5 steps from HOW TO USE). Update propagation_map. Tag `[GODOT-IMPACT: system]` if the change affects Godot implementation.

## 6.4 — New Issues
New issues enter as ED items in editorial_ledger. Triage to P0/P1/P2/P3 per standard severity definitions. P0/P1 issues gate further implementation work until resolved. P2/P3 tracked but don't block.

## 6.5 — Quarterly Review
Re-run full simulation baseline (50 runs with current design doc values). Compare against prior calibration report. Flag any metric drift (victory timing shifted, MS trajectory changed, feature coverage dropped). If drift detected, investigate cause and adjust.

---

# COMPLETE FLAG INDEX

## P0 (5 items — Phase 0.6 triage)
| ID | Description |
|----|-------------|
| ED-668 | Thread horizontal integration (triage: resolve/escalate/reclassify) |
| ED-669 | Thread horizontal integration |
| ED-670 | Thread horizontal integration |
| ED-671 | Thread horizontal integration |
| ED-672 | Thread horizontal integration |

## P1 (7 items — Phase 1)
| Flag | Phase | Item |
|------|-------|------|
| AUD-NPC-01 | 1.1 | Knot formation during play — blocks Solidarity Resonant Style |
| AUD-SET-02 | 1.2 | Accord propagation to settlement Order — 15–25 rule references |
| AUD-DS-01 | 1.3 | Derived stats numerical calibration — all multipliers PROVISIONAL |
| AUD-FP-01 | 1.4 | Faction politics simulation — 947 lines, 5 SIM-POL items |
| ED-588 | 1.5 | RM Phase 2 T9 PT ≤ 1 unreachable |
| ED-589 | 1.5 | RM Presence marker mechanics undefined |
| ED-612 | 1.5 | Guilds no solo victory condition |

## P2 (13 items — Phase 2)
| Flag | Phase | Item |
|------|-------|------|
| AUD-SC-02/03 | 2.1 | CROSS viability + SIM-DEBT-03/04 |
| ED-577-01/02/03/04 | 2.2 | Co-Movement card calibration (HARD DEP for Phase 4) |
| AUD-NPC-02 | 2.3 | 7 NPC stat gaps (TS/Certainty) |
| AUD-NPC-03 | 2.4 | Priority tree cross-faction simulation |
| AUD-SET-01/03 | 2.5 | Settlement Order averaging + economy simulation |
| AUD-VIC-02 | 2.6 | RM win probability |
| AUD-MB-02 | 2.7 | Mass battle editorial items (7 pending) |
| AUD-COM-04 | 2.8 | Ranged TN integration (ED-129) |
| AUD-TW-01 | 2.9 | Threadwork §4.1/4.2 empty |
| AUD-UI-01/02 | 2.10 | UI derived stats display + settlement map |
| — | 2.11 | Generational transition throughline |
| AUD-TW-02 | 2.12 | params_threadwork Ob alignment |

## P3 (18 items — Phase 3)
| Flag | Phase | Item | Sim-Relevant? |
|------|-------|------|---------------|
| AUD-COM-01 | 3.1 | Action priority contradiction | ⚠ Yes |
| AUD-COM-02 | 3.2 | §9 stat name propagation | ⚠ Yes |
| AUD-COM-03 | 3.3 | Deprecated doc reference | No |
| AUD-COM-05 | 3.4 | Stamina merge proposal | No |
| AUD-SC-01 | 3.5 | §1 Core Principle empty | No |
| AUD-TW-03 | 3.6 | N-Way graduated collapse | No |
| AUD-PA-02 | 3.7 | Independent path documentation | No |
| AUD-NPC-04 | 3.8 | Conviction crisis weighting | No |
| AUD-CT-01 | 3.9 | CV→PT rename | ⚠ Yes |
| AUD-CH-01 | 3.10 | Coherence→Recall→skill access | No |
| AUD-CK-01 | 3.11 | Settlement derived tracks in registry | ⚠ Yes |
| AUD-MB-01 | 3.12 | §A.5 deduplication | No |
| — | 3.13 | T6 tag assignment | No |
| AUD-ST-01 | 3.14 | Domain Echo cap verification | No |
| AUD-FW-01 | 3.15 | Demand deflection Ob | No |
| AUD-FW-02 | 3.16 | Thread-Read investigation superiority | No |
| AUD-VIC-01 | 3.17 | Accord rule consolidation | No |
| AUD-INV-01 | 3.18 | NPE Volatility convergence | No |

---

# EFFORT ESTIMATES

| Phase | Items | Sessions | Dependencies |
|-------|-------|----------|------------|
| 0 Housekeeping | 7 | 1 | None |
| 1 P1 Blockers | 5 | 2–3 | 1.2→1.3→1.4 chain |
| 2 P2 Calibration | 12 | 3–5 | 2.2 hard dep for Phase 4; 2.5 dep on 1.2+1.3; 2.6 dep on 2.4 |
| 3 P3 Polish | 18 | 2–3 | Sim-relevant items (3.1/3.2/3.9/3.11) before Phase 4 |
| 4 Full-Campaign Sim | 8 sub-items | 8–12 | Phase 1 + 2.2 + 0.7 complete |
| 5 Godot Prep | 5 | 3–4 | Phase 4 calibration accepted |
| 6 Ongoing | Permanent | — | — |
| **Total** | **55+** | **19–28 sessions** | |

**Phase 4 breakdown:**
| Sub-item | Sessions | Notes |
|----------|----------|-------|
| 4.0–4.1 Architecture + initialization + validation | 2 | Python infrastructure, canonical source loading |
| 4.2 Season resolution engine | 3–4 | Core implementation: 18 systems × resolution procedures |
| 4.3 Feature coverage validation | 1 | Initial runs, verify all ~130 features fire |
| 4.4 Baseline analysis (50 runs) | 1–2 | Run + analyze; identify calibration issues |
| 4.5 Stress tests (8 scenarios) | 1–2 | Targeted runs on specific failure modes |
| 4.6 Calibration report | 1 | The deliverable: what needs to change |
| 4.7 Regression | 1 | Post-adjustment verification |

---

# CRITICAL PATH

```
Phase 0 (1 session)
  ├── 0.1–0.5 (register cleanup)
  ├── 0.6 (P0 triage — may add items to Phase 1)
  └── 0.7 (params refresh — Phase 4 prerequisite)
  │
  ▼
Phase 1.1 (Knot formation) ──────────────────────────────────────┐
Phase 1.2 (Accord propagation) ──→ Phase 1.3 (Derived stats) ──→ Phase 1.4 (Faction pol sim)
Phase 1.5 (Coverage matrix P1s)                                   │
  │                                                               │
  ▼                                                               ▼
Phase 2.2 (Co-Movement calibration) ⚠ HARD DEP                Phase 2.5 (Settlement economy)
Phase 2.1, 2.3, 2.4, 2.7–2.12 (parallel)                      Phase 2.10 (UI integration)
  │                                                               │
  ▼                                                               │
Phase 2.6 (RM victory) ← depends on 2.4                          │
  │                                                               │
  ▼                                                               │
Phase 3 (parallel, sim-relevant items first) ◄────────────────────┘
  │
  ▼
Phase 4.0–4.2 (Sim framework build) ← depends on Phase 1 + 2.2 + 0.7
  │
  ▼
Phase 4.3–4.4 (Baseline runs + analysis)
  │
  ▼
Phase 4.5 (Stress tests)
  │
  ▼
Phase 4.6 (Calibration report)
  │
  ▼
Phase 4.7 (Regression) ← loops back if issues found
  │
  ▼
Phase 5 (Godot prep) ← depends on Phase 4 calibration accepted
  │
  ▼
Phase 6 (Ongoing maintenance) ← permanent
```

**Critical path:** 0 → 1.2 → 1.3 → 1.4 → 2.5 → 4.0 → 4.2 → 4.4 → 4.6 → 4.7 → 5.
**Minimum critical-path sessions: ~16.**

**Phase 4 is the gate.** No Godot implementation begins until the calibration report confirms:
- No death spirals (no faction enters unrecoverable decline before Season 30)
- No stasis (no 10-season window where nothing changes)
- Victory timing within Season 60–100 (Year 15–25)
- All ~130 features fire at least once across 50 runs (100% coverage)
- MS crisis reaches Fractured band (39–20) between Season 40–80
- NPC arcs transition: ≥4 of 14 named NPCs by Season 60
- Player impact measurable: player's faction outperforms AI-only by ≥2 stat points

If the calibration report identifies P1 issues, those issues loop back to Phase 1/2 → fix → regression → re-gate. The gate does not open until the game works on paper.
