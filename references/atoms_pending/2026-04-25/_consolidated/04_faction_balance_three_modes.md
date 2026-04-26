# Faction Balance & Three-Mode Architecture (consolidated)

## Consolidation front matter

- **topic_id:** `04_faction_balance_three_modes`
- **atom_count:** 50
- **scope:** master_document_2026-04-25.md + PP-540/541 simulation atoms. Three-mode emotional-engagement architecture; Monte Carlo balance findings.
- **source distribution:**
  - `master_document_2026-04-25.md`: 50 atoms
- **drift surface:** cross-source
- **post-audit canon target:** `designs/provincial/faction_*, simulations/`
- **status:** assembled (pending audit Stage 3)
- **assembled_from_commit:** atoms committed at `83c37da7001defdf3bb3425b17dda3f934d262d3`

## Audit checklist (Stage 3 input)

- [ ] Three-mode architecture is described once authoritatively.
- [ ] Simulation methodology and result claims are reproducible (params/inputs documented).
- [ ] §6.5 framework propagation gaps are real gaps, not artifacts of partial source views.
- [ ] Companion-deliverable references (`faction_balance_audit_2026-04-25.md`, `balance_simulation_report_2026-04-25.md`, etc.) point to actual files in the repo.

## Known drift dimensions

- P1 vs P2 vs P3 framing of three-mode importance — check no priority disagreement.
- PP-540/541 simulation result interpretations across sources.
- Faction-balance audit findings vs holistic audit findings — possible drift.

## Cross-source drift table

Rows = canonical IDs. Columns = source documents. Cells list atom IDs in this topic that reference the row's canonical ID. Empty cell = source does not reference that ID. Multiple atom IDs in a cell = potential per-source drift to verify during audit.

| id | m_document_2026-04-25 |
|---|---|
| **PP-540** | 2-1-initial-factio, 2-2-monte-carlo-si, p1-essential-for-m, p3-designer-hygien, 6-2-strategic-laye, 6-5-framework-prop, 8-9-faction-balanc |
| **PP-541** | 2-2-monte-carlo-si, p1-essential-for-m, p3-designer-hygien, 6-2-strategic-laye, 6-5-framework-prop, 8-9-faction-balanc |
| **PP-664** | 6-5-framework-prop |

## Content

Atoms grouped by source. Within each source, ordered by section_index. Read across sources to identify drift.

### From `master_document_2026-04-25.md` (50 atoms)

<!-- atom: master_document_2026-04-25__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# Valoria Faction Balance & Player Fulfilment — Master Document

<!-- atom: master_document_2026-04-25__01__date-2026-04-25-session-9f2f99bae771869f-c85d4e42c | section_index: 1 | source_section: "Date: 2026-04-25 | Session: 9f2f99bae771869f → c85d4e42c75417c9 → dcd1fe787654eb12" -->


## Date: 2026-04-25 | Session: 9f2f99bae771869f → c85d4e42c75417c9 → dcd1fe787654eb12

<!-- atom: master_document_2026-04-25__02__scope-consolidates-all-outcomes-deliverables-simul | section_index: 2 | source_section: "Scope: Consolidates all outcomes, deliverables, simulation findings, and open questions from a multi-stage conversation that began with strategic-layer faction balance and concluded with a three-mode emotional-engagement architecture." -->


## Scope: Consolidates all outcomes, deliverables, simulation findings, and open questions from a multi-stage conversation that began with strategic-layer faction balance and concluded with a three-mode emotional-engagement architecture.

<!-- atom: master_document_2026-04-25__03__companion-deliverables-reference-only-do-not-re-re | section_index: 3 | source_section: "Companion deliverables (reference only — do not re-read except as needed):" -->


## Companion deliverables (reference only — do not re-read except as needed):

<!-- atom: master_document_2026-04-25__04__faction-balance-audit-2026-04-25-md-47kb | section_index: 4 | source_section: "- faction_balance_audit_2026-04-25.md (47KB)" -->


## - faction_balance_audit_2026-04-25.md (47KB)

<!-- atom: master_document_2026-04-25__05__balance-simulation-report-2026-04-25-md-21kb | section_index: 5 | source_section: "- balance_simulation_report_2026-04-25.md (21KB)" -->


## - balance_simulation_report_2026-04-25.md (21KB)

<!-- atom: master_document_2026-04-25__06__faction-balance-audit-player-experience-2026-04-25 | section_index: 6 | source_section: "- faction_balance_audit_player_experience_2026-04-25.md (51KB)" -->


## - faction_balance_audit_player_experience_2026-04-25.md (51KB)

<!-- atom: master_document_2026-04-25__07__leadership-win-proposal-2026-04-25-md-21kb | section_index: 7 | source_section: "- leadership_win_proposal_2026-04-25.md (21KB)" -->


## - leadership_win_proposal_2026-04-25.md (21KB)

<!-- atom: master_document_2026-04-25__08__three-modes-of-fulfilment-2026-04-25-md-39kb | section_index: 8 | source_section: "- three_modes_of_fulfilment_2026-04-25.md (39KB)" -->


## - three_modes_of_fulfilment_2026-04-25.md (39KB)

<!-- atom: master_document_2026-04-25__09__sim-balance-py-36kb-monte-carlo-simulator | section_index: 9 | source_section: "- sim_balance.py (36KB Monte Carlo simulator)" -->


## - sim_balance.py (36KB Monte Carlo simulator)

---

# 0. EXECUTIVE SUMMARY

The session began as a faction balance audit and developed through five reframes, each shifting the design problem fundamentally. The terminal frame is **three emotional engagement modes** with mode-specific fulfilment shapes. Faction-balance work remains valid as Mode 3 (Strategy) sub-tuning but is no longer the primary design question.

| Stage | Frame | Primary Question | Status |
|---|---|---|---|
| **1. Strategic-layer audit** | Faction win-rate equality | Are factions equal in PV/milestone victory rate? | Complete; superseded as primary frame |
| **2. Monte Carlo simulation** | Numerical balance verification | Do mechanical changes equalize win rates? | Complete; calibration found at 6.9 pp spread |
| **3. Player-experience reframe** | Conviction/Duty/Slate richness | Does each faction reward Conviction-driven play? | Complete; ranking inverts strategic ranking |
| **4. Leadership felt-win** | Stature 7 attainment as victory | Does ascending to leadership feel like winning? | Complete; 3-scene Ascension Arc proposed |
| **5. Three modes of fulfilment** | Multi-shape fulfilment architecture | What does winning *mean* across player engagement scales? | Complete; primary frame |

Each subsequent stage subsumed prior work. Stage 5 (Three Modes) is the canonical recommendation. Stages 1–4 remain as sub-component support for Stage 5's mechanical realization.

---

# PART I — THE TERMINAL FRAME

<!-- atom: master_document_2026-04-25__10__1-1-three-modes-of-fulfilment-the-design-recommend | section_index: 10 | source_section: "§1.1 Three Modes of Fulfilment (the design recommendation)" -->


## §1.1 Three Modes of Fulfilment (the design recommendation)

The Valoria videogame must support three distinct emotional-engagement modes, each a complete game in itself within the same engine:

### Mode 1: Lived Simulation (Wanderer)
- **Engagement question:** What does it mean to live in this world?
- **Fulfilment terminus:** Portrait Sequence (a record of who the character became)
- **Reference design space:** Mount & Blade sandbox, Pathologic 2, Disco Elysium, Manor Lords immersion
- **Mechanical posture:** Predominantly personal-scale, no declared trajectory
- **Failure mode:** None. Wanderers cannot lose; they can only end.

### Mode 2: Open-World RPG (Trajectory)
- **Engagement question:** What does it mean to pursue something to completion?
- **Fulfilment terminus:** Endgame Sequence (declared Campaign Goal resolved or transformed)
- **Reference design space:** CK3 vassal play, Pentiment, Witcher 3 main quest, Disco Elysium central mystery
- **Mechanical posture:** Mixed personal + strategic, oriented around a declared goal
- **Failure modes:** Mechanical impossibility, player abandonment, time-out (8+ seasons no progress)

### Mode 3: Grand Strategy (Conquest)
- **Engagement question:** What does it mean to shape the peninsula?
- **Fulfilment terminus:** Victory Scene (faction-specific dramatic resolution)
- **Reference design space:** Romance of the Three Kingdoms, CK3 dynastic, Total War, Europa Universalis
- **Mechanical posture:** Predominantly strategic-scale, faction-aligned
- **Failure modes:** Faction collapse, peninsula rupture, Altonian conquest, S40 timeout

<!-- atom: master_document_2026-04-25__11__1-2-crucial-design-properties-of-the-three-mode-ar | section_index: 11 | source_section: "§1.2 Crucial design properties of the three-mode architecture" -->


## §1.2 Crucial design properties of the three-mode architecture

1. **Mode is declared, not deduced.** The player explicitly selects mode at character creation. Behavior overlap (Wanderers fight battles, Strategists develop relationships) makes deduction impossible.

2. **Mode is editable mid-campaign.** At any season transition, the player can shift mode. Each shift is recognized via a scene. The world doesn't know modes exist; only the engine does.

3. **The world is the same; the win condition varies.** Each mode's content remains accessible to all modes. Strategy players still encounter Conviction-driven scenes; Wanderers still see factions rise and fall. The mode determines what is *rewarded*, not what is *shown*.

4. **Each mode has its own UI emphasis but identical mechanics.** Wanderer foreground = Memoir; Trajectory foreground = Goal Track; Strategy foreground = Strategic dashboard. The mechanical engine and rendered world are identical.

5. **Each failure mode produces a performed conclusion.** No "Game Over" screens. Faction Funeral, Rupture Scene, Altonian Surrender, failure-conclusion Endgame, truncated Portrait — defeat is also dramatic.

<!-- atom: master_document_2026-04-25__12__1-3-cross-mode-interactions | section_index: 12 | source_section: "§1.3 Cross-mode interactions" -->


## §1.3 Cross-mode interactions

- **Wanderer → Trajectory**: declare a Campaign Goal. Goal Track activates.
- **Wanderer → Strategy**: declare faction alignment, Stature ambition, Victory target. Strategic dashboard becomes primary.
- **Trajectory → Wanderer**: archive Goal Track to Memoir as "trajectory abandoned." Memoir becomes primary.
- **Trajectory → Strategy**: Campaign Goal preserved as major Conviction; Strategy victory becomes overlay.
- **Strategy → Trajectory**: faction alignment preserved as Conviction; new Campaign Goal authored.
- **Strategy → Wanderer**: faction abandonment, drift to Independent. Memoir activates.

Multi-character campaigns allow different Lineage-successor characters in different modes. The world persists across modes and across generations. The Hall of Lineage records cross-mode legacy.

---

# PART II — STRATEGIC-LAYER WORK (Mode 3 sub-tuning)

This section preserves the strategic-layer faction-balance work for use within Mode 3 calibration. It is **not the primary design frame** but remains valid as input.

<!-- atom: master_document_2026-04-25__13__2-1-initial-faction-balance-audit-findings | section_index: 13 | source_section: "§2.1 Initial faction balance audit findings" -->


## §2.1 Initial faction balance audit findings

**Aggregate strategic-layer ranking (heuristic 6-axis scoring, 5 = best):**

| Faction | Starting position | Solo milestone | Universal path | Co-victory access | Leader tempo | Geography | TOTAL |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Hafenmark** | 3 | 4 | **5** | **5** | **5** | **5** | **27** |
| **Crown** | **5** | **5** | **5** | 3 | 4 | 4 | **26** |
| Church | 4 | 3 | 1 | 1 | 4 | 3 | 16 |
| Varfell | 3 | 3 | 1 | 3 | 2 | 1 | 13 |
| RM (cond.) | 1 | 3 | n/a | 3 | 2 | 3 | 12 |
| Löwenritter (cond.) | 1 | 2 | n/a | 1 | 3 | 2 | 9 |

**Key strategic-layer findings:**

- **Crown's PV ≥ 14 milestone is pre-met from S1** (PP-540 reduced 16→14 to match starting PV; Crown starts with exactly 14 PV).
- **Most underbalanced = Varfell**, primarily because CR-STRIKE-2026-04-19 removed Cultural Reformation (Varfell's only non-military Accord-2 acquisition path) without replacement.
- **Most structurally favoured = Hafenmark**: calamity insulation (all territories at radiation distance 4–5), 4 co-victory paths, Sovereign Authority passive CI drain (no action cost), lowest Leadership Deviation Ob 1, BALANCE-005 unenforced.

<!-- atom: master_document_2026-04-25__14__2-2-monte-carlo-simulation-results | section_index: 14 | source_section: "§2.2 Monte Carlo simulation results" -->


## §2.2 Monte Carlo simulation results

Built `sim_balance.py` — 750-line Python Monte Carlo simulator modeling 4 active factions (Crown/Church/Hafenmark/Varfell) across 17 territories, with d10 TN 7+ resolution, Burning Wheel-style outcome tiers, season-by-season action AI.

**Iteration history (37 iterations, ~50,000 total runs):**

| Stage | Win Rates (C/Ch/H/V) | Spread | Key Change |
|---|---|---:|---|
| I0 baseline | 88.7 / 0 / 0 / 0.3 | 88.4 pp | No Treaty consent gate |
| I3 | 61.3 / 0 / 0 / 0.7 | 60.6 pp | Anti-death-spiral floor added |
| I13 (best post-bug-fix) | 19.2 / 12.3 / 17.0 / 18.3 | 6.9 pp | 11-flag calibration |
| I33 (canonical Ob restored) | 15.1 / 6.2 / 15.3 / 6.9 | 9.1 pp | After fixing 2 sim bugs |

**Key sim-validated changes (ranked by leverage):**

1. **Tribune Compact** for Varfell (P0, audit §6.1) — Ob = M/2 + 2, gates Intel ≥ 5 + S ≥ 4
2. **Mass Seizure quadratic** declaration probability (P0) — replace `^3.3` with `^2.0`
3. **Crown all-3-rivals milestone** (P0) — revert PP-540's 2-of-3 softening
4. **Crown Treaty cession on Success+OW** (P0) — operationalizes `peninsular_strain §5.1`
5. **Church PV ≥ 10 + Accord ≥ 2 in 3 non-cap + Mass Seizure must fire** (P1)
6. **Hafenmark PV ≥ 12** (P1) — revert PP-541
7. **Hafenmark Diplomatic Token -1 Ob** (P1) — auto-applied, models `peninsular_strain §5.3`
8. **Sovereign Authority costs Diplomat-card** (P1, audit §6.3)
9. **Calamity Refugee penalty at MS ≤ 35** (P1, audit §6.4, BALANCE-005)
10. **Hafenmark Proclamation Wealth cost** (P0 for sim balance) — without it Hafenmark dominates
11. **Hafenmark PI ≥ 7 milestone** (P0 for sim balance) — was PI ≥ 5, trivially pre-met
12. **Church starting infrastructure pre-built** (P0 for sim balance) — Cathedral/Templar/Governor distribution per PT
13. **Crown Destabilize action** targeting lowest-Stab rival (P1)
14. **Mandate recovery passive** (P1) — factions not Mandate-attacked recover M slowly, capped at starting

<!-- atom: master_document_2026-04-25__15__2-3-critical-findings-beyond-audit-sim-revealed | section_index: 15 | source_section: "§2.3 Critical findings beyond audit (sim-revealed)" -->


## §2.3 Critical findings beyond audit (sim-revealed)

### Universal Sovereignty is unreachable in 40 seasons.
Iteration 2 disabled milestone paths and tested universal sovereignty alone. Result: 0% wins, 75% anarchy. The peninsula collapses before any faction reaches "all 15 territories + Accord ≥ 2 + Strain ≤ 6."

**Implication for canon:** Either retain milestone paths as canonical alternate endpoints (revert peninsular_strain §6.2 framing), or universal path requires faster acquisition mechanics. Under three-mode design (Part I), this becomes acceptable: Universal Sovereignty is an aspirational endpoint for ambitious Strategy campaigns, not a default victory.

### Crown's Treaty mechanic is structurally over-tooled.
Single Treaty action provides: PV-suppression credit, Mandate -1 to target, effective hegemony, optional territory cession. Four concurrent benefits per single action. The "all 3 rivals" tightening is the simplest correction.

### Mass Seizure cubed declaration probability is overcalibrated.
Per canon `((CI-60)/40)^3.3`: P(declare) = 1% at CI 70, 10% at CI 80, 39% at CI 90. Sim shows Mass Seizure rarely fires before campaign anarchy. Quadratic curve recommended.

### Hafenmark structurally locked-out without Diplomatic Token modeling.
Without auto-applied DipTok bonus, Hafenmark wins 6-9% across all calibrations. With DipTok, Hafenmark rises to 17-18%. The mechanic must be modeled; it is essential.

### Anarchy ending is dominant non-winner outcome.
20-50% of simulations end with all factions destabilized to Stab 0. Faction-vs-faction Mandate attacks compound damage faster than passive recovery. Resolution: stronger passive Stability recovery (40%/season when not attacked), Mandate recovery (30%/season capped at start).

<!-- atom: master_document_2026-04-25__16__2-4-strategic-layer-victory-shape-recommendations- | section_index: 16 | source_section: "§2.4 Strategic-layer victory shape recommendations (Victory Scenes)" -->


## §2.4 Strategic-layer victory shape recommendations (Victory Scenes)

Each faction's strategic milestone becomes a scene the player must successfully resolve, not a state vector:

- **Crown Coronation**: PV ≥ 14 + ALL 3 rivals in formal Treaty OR submitted + Crown Heir confirmed (Lenneth or Elske succession established at scene level).
- **Church Theocratic Triumph**: PV ≥ 10 + 3 non-cap territories Accord ≥ 2 + Mass Seizure declared AND Cardinal succession confirmed (specific Cardinal arc resolved).
- **Hafenmark Sovereign Recognition**: PV ≥ 12 + Sovereign Authority Doctrine validated by Crown formal recognition (a *scene*, not just stat values).
- **Varfell Tribune Triumph**: PV ≥ 8 + T4 + T13 held + WR ≥ 3 + an Einhir restoration ceremony performed at T13.
- **Universal Sovereignty Coronation**: every territory at Accord ≥ 2, every faction subordinate, the peninsula unified.
- **Co-Victory Joint Resolution**: two factions perform a joint ceremony — Treaty signing, shared coronation, formal partition.

Each victory is **a scene**, not a stat. The campaign builds toward a moment, not a threshold.

---

# PART III — PLAYER EXPERIENCE WORK (Stage 3 outcomes)

This section preserves the player-experience reframe as input to Mode 1 (Wanderer) and Mode 2 (Trajectory) design.

<!-- atom: master_document_2026-04-25__17__3-1-player-experience-faction-ranking-inverts-stra | section_index: 17 | source_section: "§3.1 Player-experience faction ranking (inverts strategic ranking)" -->


## §3.1 Player-experience faction ranking (inverts strategic ranking)

| Faction | Conviction Surface | Duty Texture | Scene Slate Richness | Stature Path | Mechanical Vocabulary | TOTAL |
|---|---:|---:|---:|---:|---:|---:|
| **Crown** | 5 | 5 | 5 | 5 | 4 | **24** |
| **Church** | 5 | 4 | 5 | 4 | 5 | **23** |
| **Varfell** | 5 | 4 | 4 | 3 | 3 | **19** |
| **Hafenmark** | 3 | 3 | 3 | 4 | 4 | **17** |

**Key inversion:** Hafenmark ranks **first** in strategic-layer score (27), **last** in player-experience score (17). Hafenmark's strategic strengths (calamity insulation, 4 co-victory paths, geographic insularity) translate to **player-experience deficits** — fewer crisis scenes at home, narrower Conviction surface, leaner Faction-Internal Duty texture.

**Varfell has the highest Conviction surface area** (9 distinct Conviction generators vs Crown 7, Church 6, Hafenmark 5) — counter to its lowest strategic-layer ranking. The actual problem is not "Varfell wins less than Crown"; it's "the most narratively rich faction has the thinnest mechanical toolkit."

<!-- atom: master_document_2026-04-25__18__3-2-player-experience-proposals-audit-6-9-6-15 | section_index: 18 | source_section: "§3.2 Player-experience proposals (audit §6.9–§6.15)" -->


## §3.2 Player-experience proposals (audit §6.9–§6.15)

### §6.9 [P0] Convert all faction victory conditions to Victory Scenes
The single largest player-experience deficit. Current arithmetic-victory shape under-rewards the texture of play. Each faction's milestone becomes a scene.

### §6.10 [P0] Connect Calamity track to faction victory paths
T15 Askeheim has PV 0 — "the most narratively rich territory in the game contributes nothing to faction victory." Adding PV 2 post-WC ≥ 3 connects personal-layer engagement to strategic victory.

### §6.11 [P1] Faction-Internal Duty richness floor
Each faction must produce minimum 3 distinct Faction-Internal Duty types per season. Hafenmark and Varfell currently below floor.

### §6.12 [P1] Stature 5 leadership challenge as multi-scene arc
Replace single-roll mechanism with 3-scene arc: Claim Declaration / Coalition Building / Succession Resolution.

### §6.13 [P1] Conviction-Duty alignment bonuses
Aligned Duty completion rewards both Standing AND Conviction reinforcement (mechanical bonus to Conviction-strain resistance for 2 seasons). Conflicting Duty: completion produces Conviction strain.

### §6.14 [P2] Settlement-broker intelligence as Tribune Compact prerequisite
Connects Niflhel-replacement system to §6.1 Varfell mechanic.

### §6.15 [P2] Tensions Deck as Conviction-generator
Each Tensions Deck card explicitly suggests 2–3 Convictions per faction.

<!-- atom: master_document_2026-04-25__19__3-3-the-strong-choice-vs-weak-choice-test | section_index: 19 | source_section: "§3.3 The strong-choice vs weak-choice test" -->


## §3.3 The strong-choice vs weak-choice test

The player's decisions feel **engaging** when scene triage involves real Conviction/Duty trade-offs rather than direct optimization toward strategic-layer numerical goals. The risk: tightening strategic conditions tempts designers to write Duties that direct players to those conditions, which reduces the Conviction-Duty-Slate triad to a single optimal pursuit.

**Fix for faction balance must not collapse into the strategic layer at the expense of the personal layer.**

---

# PART IV — LEADERSHIP WIN ARCHITECTURE (Stage 4 outcomes)

This section preserves Leadership Win mechanics as input to Mode 3 Stature 7 ambition support.

<!-- atom: master_document_2026-04-25__20__4-1-the-3-scene-ascension-arc | section_index: 20 | source_section: "§4.1 The 3-scene Ascension Arc" -->


## §4.1 The 3-scene Ascension Arc

When a player attains faction leadership (Stature 7 succession, Stature 5–6 succession contest, or Standing 4+ leadership challenge), a 3-scene arc fires:

### Scene 1: Vacancy Moment
- **Stature 7 inherited**: Inheritance Scene — Council convenes, formally offers the seat.
- **Stature 5–6 contested**: Council Contest Scene — inner-circle deliberation with player swing-vote performance.
- **Standing 4+ challenge**: Confrontation Scene — public denunciation, Council adjudication.

In every variant: public, witnessed by named NPCs, **assembled from campaign state** (player's Convictions in dialogue, Duties completed referenced, allies/enemies present).

### Scene 2: First Decree
Within 1 season: player's first Domain Action with +2D bonus. Failure structurally impossible. Choice publishes intentions; future Duty queues from AI-advisor reflect this opening move.

### Scene 3: The Recognition
Next Accounting: every faction registers position; named NPCs respond; Renown +3.

<!-- atom: master_document_2026-04-25__21__4-2-personal-victory-registration | section_index: 21 | source_section: "§4.2 Personal Victory registration" -->


## §4.2 Personal Victory registration

The Ascension arc registers as **Personal Victory** in the campaign log:
- UI/log notification
- Lineage Act: Succession unlocked
- Renown +3 (vs normal +1 cap)
- Hall of Lineage entry persists across generations
- Player can choose Portrait Retirement immediately and begin new character with Succession Lineage benefits

<!-- atom: master_document_2026-04-25__22__4-3-multiple-parallel-personal-victory-paths | section_index: 22 | source_section: "§4.3 Multiple parallel Personal Victory paths" -->


## §4.3 Multiple parallel Personal Victory paths

Beyond Stature 7 ascension:
- **All 3 Convictions Fulfilled** counts as Personal Victory
- Each enables Lineage Acts and Hall of Lineage registration

This provides **two independent paths to felt-win at personal layer:**
- Institutional path (Stature 7 → Ascension Arc)
- Personal path (3 Convictions Fulfilled)

Plus strategic-layer paths (Faction Victory, Co-Victory, Universal Sovereignty).

<!-- atom: master_document_2026-04-25__23__4-4-hall-of-lineage-as-persistent-campaign-meta-st | section_index: 23 | source_section: "§4.4 Hall of Lineage as persistent campaign meta-state" -->


## §4.4 Hall of Lineage as persistent campaign meta-state

Cross-character record preserving achievements. Successor characters can reference ancestor achievements. Multi-generational campaigns build a named history. The campaign accumulates legend.

---

# PART V — CONSOLIDATED PROPOSALS BY PRIORITY

<!-- atom: master_document_2026-04-25__24__p0-essential-for-the-design-to-make-sense-three-mo | section_index: 24 | source_section: "P0 — Essential for the design to make sense (Three Modes)" -->


## P0 — Essential for the design to make sense (Three Modes)

| # | Proposal | Source | Description |
|---|---|---|---|
| 1 | **Mode declaration at character creation** | Three Modes §1.2 | Wanderer / Trajectory / Strategy explicit selection |
| 2 | **Mode-specific UI emphasis** | Three Modes §6 | Memoir / Goal Track / Strategic dashboard as primary surface per mode |
| 3 | **Mode-specific endgame rituals** | Three Modes §1.1 | Portrait Sequence / Endgame Sequence / Victory Scene |
| 4 | **Trajectory mode goal-parsing system** | Three Modes §3.2.2 | Translates player-authored Campaign Goal into structured subgoals |
| 5 | **Mode shift mechanic** | Three Modes §5 | Players can change mode at season transitions with recognition scene |

<!-- atom: master_document_2026-04-25__25__p0-essential-for-mode-3-strategy-to-function | section_index: 25 | source_section: "P0 — Essential for Mode 3 (Strategy) to function" -->


## P0 — Essential for Mode 3 (Strategy) to function

| # | Proposal | Source | Description |
|---|---|---|---|
| 6 | **Tribune Compact** for Varfell | Audit §6.1 | Restores non-military acquisition path; M/2+2 Ob; Intel ≥ 5 + S ≥ 4 prereq |
| 7 | **Victory Scene mechanism** for each faction | Audit §6.9 / Three Modes §4.2.3 | Crown Coronation, Church Theocratic Triumph, Hafenmark Sovereign Recognition, Varfell Tribune Triumph, Universal Sovereignty Coronation, Co-Victory Joint Resolution |
| 8 | **Hafenmark Proclamation Wealth cost** | Sim finding | Without resource cost, Hafenmark dominates; required for any balance |
| 9 | **Hafenmark PI ≥ 7 milestone** | Sim finding | Was PI ≥ 5; trivially pre-met from S1 |
| 10 | **Church starting infrastructure pre-built** | Sim finding | Cathedral T9 = 3, T9-adjacent = 3, other PT-3 = 2, PT-2 = 1 |
| 11 | **Calamity track integration with faction victory paths** | Audit §6.10 | Each faction has WC engagement modifier to victory; T15 Askeheim PV 2 post-WC ≥ 3 |
| 12 | **Specify Varfell post-Vaynard succession architecture** | Multiple gaps | Maret Uln primary; Tribune institutional alternative; player Standing 5+ during Discovery Event window |

<!-- atom: master_document_2026-04-25__26__p1-essential-for-modes-to-feel-rich | section_index: 26 | source_section: "P1 — Essential for modes to feel rich" -->


## P1 — Essential for modes to feel rich

| # | Proposal | Source | Description |
|---|---|---|---|
| 13 | **Trajectory templates** (~12) | Three Modes §3.2.6 | Pre-authored Campaign Goal shapes for players who don't author their own |
| 14 | **Memoir tracking system** | Three Modes §2.2.2 | Chronological log of Wanderer activity |
| 15 | **Trajectory failure handling** | Three Modes §3.2.5 | Goal Revision Scene, transformed-goal mechanic, failure-conclusion endpoint |
| 16 | **Stature ambition variants for Strategy** | Three Modes §4.2.4 | Stature 3 / 5 / 7 success conditions distinguished |
| 17 | **Strategy failure rituals** | Three Modes §4.2.5 | Faction Funeral, Rupture Scene, Altonian Surrender — loss must be performed |
| 18 | **Mass Seizure quadratic declaration** | Sim finding | Replace `^3.3` with `^2.0` in victory_v30 §3.2 |
| 19 | **Crown all-3-rivals milestone** | Sim finding | Revert PP-540's 2-of-3 softening |
| 20 | **Crown Treaty cession on Success+OW** | Sim finding | 50% on Success / 100% on OW; operationalizes peninsular_strain §5.1 |
| 21 | **Church Accord ≥ 2 in 3 non-cap + PV ≥ 10** | Sim finding | Aligns with universal sovereignty Accord standard |
| 22 | **Hafenmark PV ≥ 12 (revert PP-541)** | Sim finding | PV-13 overcorrected |
| 23 | **Hafenmark Diplomatic Token -1 Ob auto-applied** | Sim finding | Models peninsular_strain §5.3 |
| 24 | **Sovereign Authority costs Diplomat-card slot** | Audit §6.3 | Mandate vs Ob 2 maintenance roll; opportunity cost vs Proclamation |
| 25 | **Calamity Refugee penalty at MS ≤ 35** | Audit §6.4 | Hafenmark territories Order -1 at Accounting; BALANCE-005 enforcement |
| 26 | **T12 Sigurdshelm Fort cap** | Audit §6.5 | Allow Varfell defensive investment in capital |
| 27 | **Stature 5 leadership challenge multi-scene arc** | Audit §6.12 | 3-scene arc: Claim Declaration / Coalition Building / Succession Resolution |
| 28 | **Conviction-Duty alignment bonuses** | Audit §6.13 | Aligned Duty: Standing + Conviction reinforcement; conflicting Duty: Conviction strain |
| 29 | **Faction-Internal Duty richness floor** | Audit §6.11 | 3+ distinct Faction-Internal Duty types per faction |
| 30 | **Mandate recovery passive** | Sim finding | 30%/season cap-at-start; prevents Mandate cascade |

<!-- atom: master_document_2026-04-25__27__p2-refinement | section_index: 27 | source_section: "P2 — Refinement" -->


## P2 — Refinement

| # | Proposal | Source | Description |
|---|---|---|---|
| 31 | **Wanderer scene density adjustments** | Three Modes §2.2.5 | Ambient inflation, NPC arc moment frequency |
| 32 | **Travel Vignettes for Wanderers** | Three Modes §2.2.6 | Encounter scenes during territorial movement |
| 33 | **Mode-specific Hall of Lineage formatting** | Three Modes §10 | Different mode achievements display differently in multi-generational record |
| 34 | **Trajectory subgoal display refinement** | Three Modes §3.2.3 | Legible parsed goal structure without spoiling player's authored intent |
| 35 | **Co-victory access symmetry expansion** | Audit §6.7 | Crown+Church reconciliation, Church+Varfell post-Vaynard, Church+Löwenritter Templar paths |
| 36 | **Settlement-broker intelligence as Tribune Compact prerequisite** | Audit §6.14 | Connects Niflhel-replacement system to §6.1 |
| 37 | **Tensions Deck as Conviction-generator** | Audit §6.15 | Each card suggests 2–3 Convictions per faction |

<!-- atom: master_document_2026-04-25__28__p3-designer-hygiene-no-direct-player-impact | section_index: 28 | source_section: "P3 — Designer hygiene (no direct player impact)" -->


## P3 — Designer hygiene (no direct player impact)

| # | Proposal | Source | Description |
|---|---|---|---|
| 38 | **Audit residue cleanup** | Audit §6.8 | Sync params/bg/victory.md to PP-540/PP-541; sweep deprecated paths; recompute §10 PV table; sync VTM → WR replacements |
| 39 | **Disambiguate Baralta personal vs faction Mandate** | Audit §5.7 | "Cadet-Branch Claim Weight 7" vs faction Mandate 4 |
| 40 | **§10 Win Probability Assessment table regeneration** | Audit §5.5 | Recompute against canonical PV; separate universal-sovereignty from faction-milestone timelines |

---

# PART VI — OUTSTANDING QUESTIONS

<!-- atom: master_document_2026-04-25__29__6-1-three-mode-architecture-gaps | section_index: 29 | source_section: "§6.1 Three-mode architecture gaps" -->


## §6.1 Three-mode architecture gaps

`[GAP-1: Goal-parsing system for Trajectory mode is technically nontrivial. Player writes a sentence; engine must extract target NPCs, target territories, target Conviction-types, target factions, completion criteria. This is the largest engineering question in the proposal. Recommend: start with template-only Trajectory (P0); authored Trajectory deferred to P1.]`

`[GAP-2: Mode-shift recognition scenes need authored content per shift type. Six shift directions × variant scenes per direction = ~18 scene templates needed. Could be reduced via parameterized templates.]`

`[GAP-3: Wanderer "ambient inflation" is underspecified. How much more frequent should Priority 5 entries be? What kinds of ambient texture? Settlement seasonal festivals? Local NPC family dramas? Travel rumors? Needs content design, not just mechanical specification.]`

`[GAP-4: Strategy failure rituals are described but not specified. Faction Funeral, Rupture Scene, Altonian Surrender each need scene templates with named NPC parts.]`

`[GAP-5: Cross-character continuity (Wanderer grandfather → Wanderer grandson playing same world) requires data persistence design. Hall of Lineage data structure not yet specified.]`

`[GAP-6: Multiplayer/shared-world design entirely absent. If two human players are in the same Valoria world, can one be Wanderer and the other Strategist? Probably yes, but the implications are unexplored.]`

<!-- atom: master_document_2026-04-25__30__6-2-strategic-layer-mechanical-gaps | section_index: 30 | source_section: "§6.2 Strategic-layer mechanical gaps" -->


## §6.2 Strategic-layer mechanical gaps

`[GAP-7: Varfell Path A "2 rival stats fully revealed" — mechanically vague. Which stats? Public reveal vs Tribune-internal? Counts current state or sustained reveal?]`

`[GAP-8: Lenneth TS pathway ceiling 10–20 (D-6 ED-727) — does Lenneth Crown ascension (Arc B) trigger Crown Conviction shift in BG mode? Current BG-layer mechanism for "Crown becomes pro-Einhir" unclear.]`

`[GAP-9: Co-victory pairing thresholds — calibrated against pre-PP-540/PP-541 PV values? Crown+Varfell requires Crown PV ≥ 12, but Crown starts at 14. Threshold trivially met.]`

`[GAP-10: Win probability calibration — no simulation data referenced. ST-48 (RM Victory S15) is the only explicit simulation cited. Others would benefit from per-faction simulation passes.]`

`[GAP-11: Co-victory pursuit AI — sim does not cooperate. §6.7 audit proposal untestable in current sim. Future work.]`

`[GAP-12: Hybrid mode arcs (Lenneth TS, Royal Assassination, Founding Mechanic) not modeled in simulator. RM and Löwenritter excluded by design.]`

`[GAP-13: Schoenland/Altonian invasion phases simplified in sim. Crown defense burden under-represented.]`

`[GAP-14: Stability recovery rate (40% chance Stab +1 when not attacked) is provisional. Empirical playtest required for calibration.]`

<!-- atom: master_document_2026-04-25__31__6-3-player-experience-gaps | section_index: 31 | source_section: "§6.3 Player-experience gaps" -->


## §6.3 Player-experience gaps

`[GAP-15: The five settlement-friction starting points (T1 Cathedral, T8 Market Quarter, T14 Barracks, T4 Lodge, T13 Shrine) are described in conflict_architecture_proposal but the moment-to-moment Scene Slate templates for player engagement are not specified anywhere. Each friction needs ~4–6 Slate templates.]`

`[GAP-16: Victory Scene templates per audit §6.9 not yet drafted. Each faction needs one canonical Victory Scene + 3 alternate paths.]`

`[GAP-17: Calamity-track-to-faction-victory connection per audit §6.10 needs canonical specification. Currently exists as proposal only.]`

`[GAP-18: Stature 5 leadership challenge multi-scene arc per audit §6.12 needs full scene specifications.]`

`[GAP-19: Hafenmark Faction-Internal Duty content beyond cadet-branch family + parliamentary work. At least 2 more strands needed (suggestions: Guild liaison politics, regional governor dynastic claims).]`

`[GAP-20: Post-Vaynard succession architecture for Varfell. Vaynard's Discovery Event arc has consequence (faction destabilization) but no defined succession path.]`

`[GAP-21: Tensions Deck card-to-Conviction mapping per audit §6.15 not specified. Each card needs 2–3 example Convictions per faction.]`

<!-- atom: master_document_2026-04-25__32__6-4-leadership-win-gaps | section_index: 32 | source_section: "§6.4 Leadership Win gaps" -->


## §6.4 Leadership Win gaps

`[GAP-22: Vacancy Scene templates per faction not specified. Each faction needs at least 3 Vacancy Scene variants (peaceful succession, contested, post-coup) with specific NPC speaking parts.]`

`[GAP-23: First Decree action options per faction. Each faction needs ~4–6 canonical First Decree archetypes, drawing from common Conviction patterns.]`

`[GAP-24: Maret Uln's promotion to canonical Varfell successor needs alignment with existing npc_character_analyses. Confirm Maret's stat profile and Conviction set support this role.]`

`[GAP-25: Hall of Lineage data structure not specified. Need format for what's preserved per leader (Convictions declared, First Decree, key Duties completed, Renown at ascension).]`

`[GAP-26: Confirmation that Personal Victory registration triggers the same UI/feedback intensity as strategic-layer victory in the videogame mode. Without parity, the Personal Victory will feel lesser.]`

<!-- atom: master_document_2026-04-25__33__6-5-framework-propagation-gaps-deferred-from-prior | section_index: 33 | source_section: "§6.5 Framework propagation gaps (deferred from prior audit §5)" -->


## §6.5 Framework propagation gaps (deferred from prior audit §5)

`[GAP-27: peninsular_strain_v30 §6.2 declares Universal Sovereignty as canonical victory; victory_v30 §3 retains faction-specific milestones. Under three-mode design (Part I), faction milestones become Mode 3 Strategy victory targets, Universal Sovereignty becomes aspirational endpoint. This resolution needs canonical propagation.]`

`[GAP-28: PP-540/PP-541 inconsistencies between victory_v30 §3 and params/bg/victory.md. Sync needed.]`

`[GAP-29: VTM strike propagation incomplete (ED-706, pending PP-664). VTM → WR replacement in params/bg/victory.md not done.]`

`[GAP-30: Cultural Reformation strike (CR-STRIKE-2026-04-19) violates §0.5 design principle (each faction has non-military Accord ≥ 2 acquisition). Tribune Compact (P0 proposal #6) restores compliance.]`

---

# PART VII — IMPLEMENTATION SEQUENCE

Recommended implementation order based on dependency analysis:

<!-- atom: master_document_2026-04-25__34__phase-a-foundation-p0-set-1 | section_index: 34 | source_section: "Phase A — Foundation (P0 set 1)" -->


## Phase A — Foundation (P0 set 1)
1. Specify Varfell post-Vaynard succession architecture (gap-20)
2. Implement Tribune Compact Domain Action (proposal #6)
3. Implement Hafenmark Wealth-cost on Proclamation (proposal #8)
4. Implement Hafenmark PI ≥ 7 milestone update (proposal #9)
5. Specify Church starting infrastructure distribution (proposal #10)

**Rationale:** these are canon-filling moves that close the most pressing strategic-layer gaps. Without them, no Mode 3 calibration is possible.

<!-- atom: master_document_2026-04-25__35__phase-b-three-mode-declaration-p0-set-2 | section_index: 35 | source_section: "Phase B — Three-mode declaration (P0 set 2)" -->


## Phase B — Three-mode declaration (P0 set 2)
6. Implement mode declaration at character creation (proposal #1)
7. Implement Trajectory templates (proposal #13)
8. Implement mode-specific UI surfaces — at least placeholder-level (proposal #2)
9. Implement Portrait Retirement → Wanderer endgame ritual (proposal #3 partial)
10. Implement Mode shift mechanic — at least mechanical, scenes can be P1 (proposal #5)

**Rationale:** delivers the three-mode architecture's core promise. Players can declare mode and see different campaign shapes.

<!-- atom: master_document_2026-04-25__36__phase-c-mode-3-victory-scenes-p0-set-3 | section_index: 36 | source_section: "Phase C — Mode 3 Victory Scenes (P0 set 3)" -->


## Phase C — Mode 3 Victory Scenes (P0 set 3)
11. Draft Crown Coronation Victory Scene (proposal #7)
12. Draft Church Theocratic Triumph Victory Scene (proposal #7)
13. Draft Hafenmark Sovereign Recognition Victory Scene (proposal #7)
14. Draft Varfell Tribune Triumph Victory Scene (proposal #7)
15. Implement Calamity track integration with each faction victory (proposal #11)

**Rationale:** Mode 3 needs felt-win moments to function. Without Victory Scenes, Strategy mode degrades to arithmetic-completion.

<!-- atom: master_document_2026-04-25__37__phase-d-mode-1-mode-2-enrichment-p1 | section_index: 37 | source_section: "Phase D — Mode 1 + Mode 2 enrichment (P1)" -->


## Phase D — Mode 1 + Mode 2 enrichment (P1)
16. Memoir tracking system (proposal #14)
17. Trajectory failure handling (proposal #15)
18. Stature 5 multi-scene arc (proposal #27)
19. Stature ambition variants for Strategy (proposal #16)
20. Trajectory subgoal display refinement (proposal #34)

<!-- atom: master_document_2026-04-25__38__phase-e-strategic-balance-refinement-p1-sim-valida | section_index: 38 | source_section: "Phase E — Strategic balance refinement (P1, sim-validated)" -->


## Phase E — Strategic balance refinement (P1, sim-validated)
21. Mass Seizure quadratic (proposal #18)
22. Crown all-3-rivals milestone (proposal #19)
23. Crown Treaty cession (proposal #20)
24. Church PV ≥ 10 + Accord ≥ 2 in 3 non-cap (proposal #21)
25. Hafenmark PV ≥ 12 + DipTok auto-applied (proposals #22, #23)
26. Sovereign Authority costs Diplomat-card (proposal #24)
27. Calamity Refugee penalty at MS ≤ 35 (proposal #25)
28. Mandate recovery passive (proposal #30)

<!-- atom: master_document_2026-04-25__39__phase-f-texture-and-content-p1-p2 | section_index: 39 | source_section: "Phase F — Texture and content (P1–P2)" -->


## Phase F — Texture and content (P1–P2)
29. Faction-Internal Duty richness floor (proposal #29)
30. Conviction-Duty alignment bonuses (proposal #28)
31. Strategy failure rituals (proposal #17)
32. Wanderer scene density + Travel Vignettes (proposals #31, #32)
33. Tensions Deck Conviction-generator (proposal #37)

<!-- atom: master_document_2026-04-25__40__phase-g-designer-hygiene-p3 | section_index: 40 | source_section: "Phase G — Designer hygiene (P3)" -->


## Phase G — Designer hygiene (P3)
34. Audit residue cleanup (proposal #38)
35. Baralta Mandate disambiguation (proposal #39)
36. §10 Win Probability table regeneration (proposal #40)

---

# PART VIII — DESIGN DECISIONS REGISTER

These are the explicit design decisions made during the session that supersede prior framings:

<!-- atom: master_document_2026-04-25__41__8-1-faction-win-rate-equality-is-not-the-primary-b | section_index: 41 | source_section: "§8.1 Faction win-rate equality is not the primary balance question" -->


## §8.1 Faction win-rate equality is not the primary balance question

**Decision:** Asymmetric faction win rates are acceptable when the asymmetry tracks distinct strategic textures.
**Rationale:** Three-mode architecture means most players don't need their faction to strategic-win to feel a win. Strategy mode is one of three modes, not the canonical mode.
**Status:** Final. Supersedes the simulator-derived equalization work as primary frame.

<!-- atom: master_document_2026-04-25__42__8-2-universal-sovereignty-is-aspirational-not-defa | section_index: 42 | source_section: "§8.2 Universal Sovereignty is aspirational, not default" -->


## §8.2 Universal Sovereignty is aspirational, not default

**Decision:** Faction-specific milestones become Mode 3 Strategy victory targets. Universal Sovereignty becomes an aspirational endpoint for ambitious campaigns.
**Rationale:** Sim showed Universal Sovereignty is unreachable in 40 seasons. Canon framework's framing ("only Universal Sovereignty is canonical victory") is mechanically incomplete.
**Status:** Final. Resolves peninsular_strain §6.2 vs victory_v30 §3 propagation gap.

<!-- atom: master_document_2026-04-25__43__8-3-victory-is-a-scene-not-a-state-vector | section_index: 43 | source_section: "§8.3 Victory is a scene, not a state vector" -->


## §8.3 Victory is a scene, not a state vector

**Decision:** Each faction's Mode 3 victory becomes a dramatic scene the player witnesses or performs, not just a state-condition check.
**Rationale:** Arithmetic completion of state conditions is the central player-experience deficit. The campaign builds toward a moment, not a threshold.
**Status:** Final. Specified in audit §6.9; expanded in three-modes §4.2.3.

<!-- atom: master_document_2026-04-25__44__8-4-leadership-attainment-is-itself-a-personal-vic | section_index: 44 | source_section: "§8.4 Leadership attainment is itself a Personal Victory" -->


## §8.4 Leadership attainment is itself a Personal Victory

**Decision:** Stature 7 ascension fires a 3-scene Ascension Arc registered as Personal Victory. Independent of strategic-layer faction victory.
**Rationale:** A 20-season Stature climb deserves a felt-win moment regardless of whether the faction subsequently achieves strategic victory.
**Status:** Final. Mode 3 Stature 7 ambition path; also available to Trajectory players who declare leadership as their Campaign Goal.

<!-- atom: master_document_2026-04-25__45__8-5-the-mode-is-declared-not-deduced | section_index: 45 | source_section: "§8.5 The mode is declared, not deduced" -->


## §8.5 The mode is declared, not deduced

**Decision:** Players explicitly select Wanderer / Trajectory / Strategy at character creation. Mode is editable mid-campaign with recognition scene.
**Rationale:** Behavior overlap between modes makes deduction impossible. Player intent is the only reliable signal.
**Status:** Final.

<!-- atom: master_document_2026-04-25__46__8-6-the-world-is-the-same-the-win-condition-varies | section_index: 46 | source_section: "§8.6 The world is the same; the win condition varies" -->


## §8.6 The world is the same; the win condition varies

**Decision:** All three modes share identical mechanical engine and rendered world. Mode determines what is rewarded, not what is shown.
**Rationale:** A Wanderer should still see factions rise and fall. A Strategist should still develop deep Knots. The world doesn't bifurcate.
**Status:** Final.

<!-- atom: master_document_2026-04-25__47__8-7-defeat-is-also-performed | section_index: 47 | source_section: "§8.7 Defeat is also performed" -->


## §8.7 Defeat is also performed

**Decision:** Every failure mode produces a performed conclusion (Faction Funeral, Rupture Scene, Altonian Surrender, failure-conclusion Endgame, truncated Portrait). No "Game Over" screens.
**Rationale:** Defeat is part of the campaign's emotional shape. Strategy players who lose should feel their loss, not see a generic end-card.
**Status:** Final.

<!-- atom: master_document_2026-04-25__48__8-8-the-cultural-reformation-strike-requires-repla | section_index: 48 | source_section: "§8.8 The Cultural Reformation strike requires replacement" -->


## §8.8 The Cultural Reformation strike requires replacement

**Decision:** Tribune Compact replaces Cultural Reformation as Varfell's non-military Accord ≥ 2 acquisition path.
**Rationale:** CR-STRIKE-2026-04-19 violated §0.5 design principle. Tribune Compact restores compliance and ties to Varfell's distinctive Intel stat.
**Status:** Final. Specified in audit §6.1; sim-calibrated Ob = M/2 + 2.

<!-- atom: master_document_2026-04-25__49__8-9-faction-balance-simulation-work-remains-valid- | section_index: 49 | source_section: "§8.9 Faction-balance simulation work remains valid for Mode 3 calibration" -->


## §8.9 Faction-balance simulation work remains valid for Mode 3 calibration

**Decision:** The 37 simulator iterations and ~50,000 runs produced calibration-relevant data for Mode 3 Strategy tuning, not the primary balance frame.
**Rationale:** Simulation cannot model emotional engagement. It can model arithmetic-completion rates of Strategy mode. Useful for one of three modes.
**Status:** Final. sim_balance.py preserved as Mode 3 calibration tool.

---

# PART IX — RELATIONSHIP TO EXISTING CANON

This section maps proposals to canonical document requirements.

| Canonical Document | Required Update | Priority |
|---|---|---|
| `player_agency_v30.md` | Add §0 mode declaration. Update §5.2 to specify 3-scene Ascension Arc. Add Wanderer mode mechanics to §5.3. Add Trajectory mode (entirely new section). | P0 |
| `victory_v30.md` | Convert §3.1–§3.6 from arithmetic milestones to Victory Scene specifications. Update §3.4 with Tribune Compact. Update §10 Win Probability table. | P0 |
| `peninsular_strain_v30.md` | Reconcile §6.2 with three-mode architecture (Universal Sovereignty as aspirational, milestones as Mode 3 targets). | P0 |
| `campaign_architecture_v30.md` | Update §7 (Portrait Retirement) to be primary Wanderer mechanism. Add Trajectory Endgame Sequence. Add Victory Scene templates. | P0 |
| `videogame_mode_spec.md` | Add §6 (or new section) for emotional engagement modes. Specify mode-specific UI surfaces. | P0 |
| `factions_personal_v30.md` | Update Hafenmark Proclamation with Wealth cost. Update Hafenmark PI condition to 7. Add Tribune Compact for Varfell. | P0 |
| `params/bg/victory.md` | Sync to PP-540/PP-541. Apply VTM → WR replacement. Update Co-Victory thresholds against current PV values. | P1 |
| `geography_v30.md` | Operationalize BALANCE-005 (Hafenmark food dependency) via Calamity Refugee penalty. Update T15 Askeheim with PV 2 post-WC ≥ 3. | P1 |
| `npc_character_analyses_v30.md` | Specify post-Vaynard Varfell succession (Maret Uln canonical). Disambiguate Baralta personal vs faction Mandate. | P0 |
| `conflict_architecture_proposal.md` | Already canonical — no changes needed; this proposal underpins three-mode design. | (no update) |
| `scale_transitions_v30.md` | Already supports two-scale architecture; preserved unchanged. | (no update) |
| (new) `three_modes_specification.md` | Author this document from `three_modes_of_fulfilment_2026-04-25.md` proposal. | P0 |
| (new) `trajectory_templates.md` | Author 12 Trajectory Goal templates. | P1 |

---

# PART X — META-OBSERVATIONS ON THE DESIGN PROCESS

Five reframes occurred in this session, each subsuming the prior:

1. **Strategic-layer audit** assumed faction-balance was the question. Output: 6-proposal §6 set targeting strategic equality.
2. **Monte Carlo simulation** assumed mechanical changes could equalize win rates. Output: 11-flag calibration achieving 6.9 pp spread.
3. **Player-experience reframe** revealed strategic-layer ranking inverts player-experience ranking. Output: §6.9–§6.15 proposals targeting Conviction/Duty/Slate richness.
4. **Leadership felt-win** revealed that faction-leadership attainment has no canonical fulfilment moment. Output: 3-scene Ascension Arc as Personal Victory.
5. **Three modes of fulfilment** revealed that "winning" itself is mode-dependent. Output: complete reframe of fulfilment architecture.

Each reframe was triggered by a single sentence from Jordan that exposed a hidden assumption in the prior frame:

- Reframe 3 trigger: "Perform audit from a radically fresh perspective based upon player experience"
- Reframe 4 trigger: "Players need to be able to feel a 'win' if they end up controlling a faction"
- Reframe 5 trigger: "A player needs to be able to find fulfilment in the game ranging from whether they simply want to be wandering within the world... all the way through to conquering the peninsula"

**Process implication:** the simulator-driven approach (Stages 1–2) was working on a substrate where the design problem had not yet been correctly framed. The sim work remains valid as Mode 3 sub-calibration but did not produce primary design conclusions. The primary conclusions came from text-based reasoning about player intent.

**For future similar work:** before extensive simulation, verify the design problem at the player-experience level. Simulators answer "what does the math do" but cannot answer "what does the player want to feel." The latter question must come first.

---

# PART XI — DOCUMENT MAP

For navigation across deliverables produced this session:

```
/mnt/user-data/outputs/
├── faction_balance_audit_2026-04-25.md (47KB)
│   └── Stage 1: Strategic-layer audit. Six §6 proposals.
│       Status: superseded as primary frame; valid as Mode 3 input.
│
├── balance_simulation_report_2026-04-25.md (21KB)
│   └── Stage 2: Monte Carlo simulation report. 14 iterations.
│       Status: sim work valid for Mode 3 calibration.
│
├── sim_balance.py (36KB)
│   └── Monte Carlo simulator. 750 lines. 4-faction d10 TN-7 model.
│       Status: tool preserved for Mode 3 calibration.
│
├── faction_balance_audit_player_experience_2026-04-25.md (51KB)
│   └── Stage 3: Player-experience reframe. Conviction/Duty/Slate analysis.
│       Status: superseded as primary frame; informs Modes 1–2.
│
├── leadership_win_proposal_2026-04-25.md (21KB)
│   └── Stage 4: 3-scene Ascension Arc. Personal Victory mechanic.
│       Status: subsumed into Mode 3 Stature 7 path.
│
├── three_modes_of_fulfilment_2026-04-25.md (39KB)
│   └── Stage 5: Three emotional engagement modes. PRIMARY FRAME.
│       Status: canonical recommendation.
│
└── master_document_2026-04-25.md (THIS DOCUMENT)
    └── Consolidation. Single reference for all session outcomes.
```

For implementation work, this master document is the single entry point. Companion deliverables are reference material only.

---

# PART XII — FINAL STATEMENT

The session began asking: **"Are factions balanced for win rate?"**

It ends answering: **"What does winning even mean?"**

Three answers, each legitimate:

- **Wanderer**: Winning means living a life worth recording in a Portrait.
- **Trajectory**: Winning means reaching the conclusion you authored at the start.
- **Strategy**: Winning means seeing your faction's victory performed as a scene.

The same engine. The same Valoria. Three games. Three fulfilments.

The faction-balance question — whether Crown wins 19% to Varfell's 18% — matters only for the third mode, where it has been mostly resolved. The first two modes don't measure faction win rate at all. They measure whether the player got what they came for.

This is the design.

---

**End of master document. 2026-04-25.**

## Provenance

Atom-by-atom inventory in source/section order:

| atom_id | source | section_index | source_section | lines |
|---|---|---|---|---|
| `master_document_2026-04-25__00__preamble` | `master_document_2026-04-25.md` | 0 | (preamble) | 1 |
| `master_document_2026-04-25__01__date-2026-04-25-session-9f2f99bae771869f-c85d4e42c` | `master_document_2026-04-25.md` | 1 | Date: 2026-04-25 | Session: 9f2f99bae771869f → c85 | 1 |
| `master_document_2026-04-25__02__scope-consolidates-all-outcomes-deliverables-simul` | `master_document_2026-04-25.md` | 2 | Scope: Consolidates all outcomes, deliverables, si | 1 |
| `master_document_2026-04-25__03__companion-deliverables-reference-only-do-not-re-re` | `master_document_2026-04-25.md` | 3 | Companion deliverables (reference only — do not re | 1 |
| `master_document_2026-04-25__04__faction-balance-audit-2026-04-25-md-47kb` | `master_document_2026-04-25.md` | 4 | - faction_balance_audit_2026-04-25.md (47KB) | 1 |
| `master_document_2026-04-25__05__balance-simulation-report-2026-04-25-md-21kb` | `master_document_2026-04-25.md` | 5 | - balance_simulation_report_2026-04-25.md (21KB) | 1 |
| `master_document_2026-04-25__06__faction-balance-audit-player-experience-2026-04-25` | `master_document_2026-04-25.md` | 6 | - faction_balance_audit_player_experience_2026-04- | 1 |
| `master_document_2026-04-25__07__leadership-win-proposal-2026-04-25-md-21kb` | `master_document_2026-04-25.md` | 7 | - leadership_win_proposal_2026-04-25.md (21KB) | 1 |
| `master_document_2026-04-25__08__three-modes-of-fulfilment-2026-04-25-md-39kb` | `master_document_2026-04-25.md` | 8 | - three_modes_of_fulfilment_2026-04-25.md (39KB) | 1 |
| `master_document_2026-04-25__09__sim-balance-py-36kb-monte-carlo-simulator` | `master_document_2026-04-25.md` | 9 | - sim_balance.py (36KB Monte Carlo simulator) | 22 |
| `master_document_2026-04-25__10__1-1-three-modes-of-fulfilment-the-design-recommend` | `master_document_2026-04-25.md` | 10 | §1.1 Three Modes of Fulfilment (the design recomme | 25 |
| `master_document_2026-04-25__11__1-2-crucial-design-properties-of-the-three-mode-ar` | `master_document_2026-04-25.md` | 11 | §1.2 Crucial design properties of the three-mode a | 12 |
| `master_document_2026-04-25__12__1-3-cross-mode-interactions` | `master_document_2026-04-25.md` | 12 | §1.3 Cross-mode interactions | 17 |
| `master_document_2026-04-25__13__2-1-initial-faction-balance-audit-findings` | `master_document_2026-04-25.md` | 13 | §2.1 Initial faction balance audit findings | 19 |
| `master_document_2026-04-25__14__2-2-monte-carlo-simulation-results` | `master_document_2026-04-25.md` | 14 | §2.2 Monte Carlo simulation results | 30 |
| `master_document_2026-04-25__15__2-3-critical-findings-beyond-audit-sim-revealed` | `master_document_2026-04-25.md` | 15 | §2.3 Critical findings beyond audit (sim-revealed) | 19 |
| `master_document_2026-04-25__16__2-4-strategic-layer-victory-shape-recommendations-` | `master_document_2026-04-25.md` | 16 | §2.4 Strategic-layer victory shape recommendations | 19 |
| `master_document_2026-04-25__17__3-1-player-experience-faction-ranking-inverts-stra` | `master_document_2026-04-25.md` | 17 | §3.1 Player-experience faction ranking (inverts st | 13 |
| `master_document_2026-04-25__18__3-2-player-experience-proposals-audit-6-9-6-15` | `master_document_2026-04-25.md` | 18 | §3.2 Player-experience proposals (audit §6.9–§6.15 | 23 |
| `master_document_2026-04-25__19__3-3-the-strong-choice-vs-weak-choice-test` | `master_document_2026-04-25.md` | 19 | §3.3 The strong-choice vs weak-choice test | 12 |
| `master_document_2026-04-25__20__4-1-the-3-scene-ascension-arc` | `master_document_2026-04-25.md` | 20 | §4.1 The 3-scene Ascension Arc | 17 |
| `master_document_2026-04-25__21__4-2-personal-victory-registration` | `master_document_2026-04-25.md` | 21 | §4.2 Personal Victory registration | 9 |
| `master_document_2026-04-25__22__4-3-multiple-parallel-personal-victory-paths` | `master_document_2026-04-25.md` | 22 | §4.3 Multiple parallel Personal Victory paths | 12 |
| `master_document_2026-04-25__23__4-4-hall-of-lineage-as-persistent-campaign-meta-st` | `master_document_2026-04-25.md` | 23 | §4.4 Hall of Lineage as persistent campaign meta-s | 8 |
| `master_document_2026-04-25__24__p0-essential-for-the-design-to-make-sense-three-mo` | `master_document_2026-04-25.md` | 24 | P0 — Essential for the design to make sense (Three | 10 |
| `master_document_2026-04-25__25__p0-essential-for-mode-3-strategy-to-function` | `master_document_2026-04-25.md` | 25 | P0 — Essential for Mode 3 (Strategy) to function | 12 |
| `master_document_2026-04-25__26__p1-essential-for-modes-to-feel-rich` | `master_document_2026-04-25.md` | 26 | P1 — Essential for modes to feel rich | 23 |
| `master_document_2026-04-25__27__p2-refinement` | `master_document_2026-04-25.md` | 27 | P2 — Refinement | 12 |
| `master_document_2026-04-25__28__p3-designer-hygiene-no-direct-player-impact` | `master_document_2026-04-25.md` | 28 | P3 — Designer hygiene (no direct player impact) | 12 |
| `master_document_2026-04-25__29__6-1-three-mode-architecture-gaps` | `master_document_2026-04-25.md` | 29 | §6.1 Three-mode architecture gaps | 14 |
| `master_document_2026-04-25__30__6-2-strategic-layer-mechanical-gaps` | `master_document_2026-04-25.md` | 30 | §6.2 Strategic-layer mechanical gaps | 18 |
| `master_document_2026-04-25__31__6-3-player-experience-gaps` | `master_document_2026-04-25.md` | 31 | §6.3 Player-experience gaps | 16 |
| `master_document_2026-04-25__32__6-4-leadership-win-gaps` | `master_document_2026-04-25.md` | 32 | §6.4 Leadership Win gaps | 12 |
| `master_document_2026-04-25__33__6-5-framework-propagation-gaps-deferred-from-prior` | `master_document_2026-04-25.md` | 33 | §6.5 Framework propagation gaps (deferred from pri | 16 |
| `master_document_2026-04-25__34__phase-a-foundation-p0-set-1` | `master_document_2026-04-25.md` | 34 | Phase A — Foundation (P0 set 1) | 9 |
| `master_document_2026-04-25__35__phase-b-three-mode-declaration-p0-set-2` | `master_document_2026-04-25.md` | 35 | Phase B — Three-mode declaration (P0 set 2) | 9 |
| `master_document_2026-04-25__36__phase-c-mode-3-victory-scenes-p0-set-3` | `master_document_2026-04-25.md` | 36 | Phase C — Mode 3 Victory Scenes (P0 set 3) | 9 |
| `master_document_2026-04-25__37__phase-d-mode-1-mode-2-enrichment-p1` | `master_document_2026-04-25.md` | 37 | Phase D — Mode 1 + Mode 2 enrichment (P1) | 7 |
| `master_document_2026-04-25__38__phase-e-strategic-balance-refinement-p1-sim-valida` | `master_document_2026-04-25.md` | 38 | Phase E — Strategic balance refinement (P1, sim-va | 10 |
| `master_document_2026-04-25__39__phase-f-texture-and-content-p1-p2` | `master_document_2026-04-25.md` | 39 | Phase F — Texture and content (P1–P2) | 7 |
| `master_document_2026-04-25__40__phase-g-designer-hygiene-p3` | `master_document_2026-04-25.md` | 40 | Phase G — Designer hygiene (P3) | 11 |
| `master_document_2026-04-25__41__8-1-faction-win-rate-equality-is-not-the-primary-b` | `master_document_2026-04-25.md` | 41 | §8.1 Faction win-rate equality is not the primary  | 6 |
| `master_document_2026-04-25__42__8-2-universal-sovereignty-is-aspirational-not-defa` | `master_document_2026-04-25.md` | 42 | §8.2 Universal Sovereignty is aspirational, not de | 6 |
| `master_document_2026-04-25__43__8-3-victory-is-a-scene-not-a-state-vector` | `master_document_2026-04-25.md` | 43 | §8.3 Victory is a scene, not a state vector | 6 |
| `master_document_2026-04-25__44__8-4-leadership-attainment-is-itself-a-personal-vic` | `master_document_2026-04-25.md` | 44 | §8.4 Leadership attainment is itself a Personal Vi | 6 |
| `master_document_2026-04-25__45__8-5-the-mode-is-declared-not-deduced` | `master_document_2026-04-25.md` | 45 | §8.5 The mode is declared, not deduced | 6 |
| `master_document_2026-04-25__46__8-6-the-world-is-the-same-the-win-condition-varies` | `master_document_2026-04-25.md` | 46 | §8.6 The world is the same; the win condition vari | 6 |
| `master_document_2026-04-25__47__8-7-defeat-is-also-performed` | `master_document_2026-04-25.md` | 47 | §8.7 Defeat is also performed | 6 |
| `master_document_2026-04-25__48__8-8-the-cultural-reformation-strike-requires-repla` | `master_document_2026-04-25.md` | 48 | §8.8 The Cultural Reformation strike requires repl | 6 |
| `master_document_2026-04-25__49__8-9-faction-balance-simulation-work-remains-valid-` | `master_document_2026-04-25.md` | 49 | §8.9 Faction-balance simulation work remains valid | 112 |
