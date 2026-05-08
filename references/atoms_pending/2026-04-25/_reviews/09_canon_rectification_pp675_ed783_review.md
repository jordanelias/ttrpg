# Exhaustive Review — `09_canon_rectification_pp675_ed783`

**Topic:** Canon Rectification PP-675 / ED-783 (consolidated)
**Atoms:** 18
**Method:** strict ID-presence check in primary registers (definition-pattern aware: YAML `id: X-N` for ED/PP, `| T-N |` table-row or `## T-N` heading for T/M) + repo path-existence + substantive-claim extraction with best-match canon excerpt.

## Summary

### ID classification

- **DEFINED-IN-CANON:** present as a defined entry in primary register (YAML `id:` for ED/PP; table row or heading for T/M).
- **MENTIONED-IN-CANON:** appears in canon corpus but not as a primary-register definition (likely cross-reference or editorial marker).
- **PARTIAL:** defined in canon, but atom's discussion is materially richer.
- **NEW:** not present in any fetched canon file.

| status | count |
|---|---|
| DEFINED-IN-CANON | 11 |
| MENTIONED-IN-CANON | 2 |
| PARTIAL | 0 |
| NEW | 0 |

### Path verification

| status | count |
|---|---|
| EXISTS | 31 |
| MISSING-FROM-REPO | 1 |

### Substantive claims surfaced: 29

## ID-by-ID comparison

### ED-667 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > | (cross-faction) | Thread political warfare | — | — | Mutual deterrence via shared RS |  ### Editorial + Cleanup  | Commit | SHA | What | |--------|-----|------| | 13 | `fb16bd3` | ED-717 resolved, ED-667 resolved in editorial ledger. P1 count 2→1 | | 14 | `7b96edd` | Residual Niflhel/Coup refs in arcs_31_35, emergent_campaign_arcs, factions_personal_v30_infill | | 15 | `ef19887` | PP-675 backsto
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > ermaster, Quiet One) — dead. Session B Niflhel dissolution. STRUCK in arc_expansion_v30.md (bdf8a6a2)."     status: resolved     severity: P2     source: "Session B dissolution (2026-04-18)"    - id: ED-667     date: 2026-04-19     description: "Coup Counter readiness gap — binary trigger lacked intermediate posture. Resolved by Löwenritter graduated autonomy (4-stage Loyal/Restless/Autonomous/Spl

### ED-710 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger.yaml`.
- **atom context** (`valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close`):
  > ## Section 9 — Open Items at Session Close  ### Final open EDs (4)  | ED | Description | Status | |---|---|---| | ED-710 | Settlement adjacency graph | Workplan-scale, deferred | | ED-711 | Fractional province ownership | Workplan-scale, deferred | | ED-768 | 13 orphaned PROVISIONAL markers | Jordan-blocked review | | TC→CI bulk propagation | ~675 residual TC references in active spec | Queued cle
- **canon context** (`canon/editorial_ledger.yaml`):
  > # Valoria Editorial Ledger — Active (open items only) # next_id: 739 # Archival batch 2026-04-23: 16 resolved entries migrated to canon/editorial_ledger_archive.yaml.  entries:    - id: ED-710     date: 2026-04-19     description: "Settlement adjacency graph — new mechanical layer. Invasions occur at settlement-scale via inter-settlement edges (road/river/mountain/coastal). Spec: designs/territory

### ED-711 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger.yaml`.
- **atom context** (`valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close`):
  > ## Section 9 — Open Items at Session Close  ### Final open EDs (4)  | ED | Description | Status | |---|---|---| | ED-710 | Settlement adjacency graph | Workplan-scale, deferred | | ED-711 | Fractional province ownership | Workplan-scale, deferred | | ED-768 | 13 orphaned PROVISIONAL markers | Jordan-blocked review | | TC→CI bulk propagation | ~675 residual TC references in active spec | Queued cle
- **canon context** (`canon/editorial_ledger.yaml`):
  > ttlement-scale via inter-settlement edges (road/river/mountain/coastal). Spec: designs/territory/settlement_adjacency_v30.md (PP-666)."     status: open     severity: P2     source: "PP-666"    - id: ED-711     date: 2026-04-19     description: "Fractional province ownership — province PV fractionalizes by settlement Prosperity share when Seat and non-Seat settlements have different controllers. 7

### ED-717 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > ## Context Window 3 — ED-717 + Cleanup  ### ED-717: Faction Substrate-Postures (М-4 Throughlines)  Every faction now has a defined relationship to Thread/substrate. М-4 count: 4 → 7.  #### T-15a: Hafenmark — Unmediated Sovereigntist  Baralta is the Protestant faction. Shares Church theology entirely (Solmund is divine, threadw
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > ded. sim_ttrpg_batch_legacy_* files flagged for follow-up banner pass (low priority). See designs/audit/label_audit_2026-04-19.md."     status: resolved     severity: P3     source: "PP-670"    - id: ED-717     date: 2026-04-19     description: "Meta-throughline synthesis (PP-671): 3 substrate-posture gaps (Hafenmark/Löwenritter/RM lacking М-4 characterization). Framework resolution: T-15a/b/c in 

### ED-768 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger.yaml`.
- **atom context** (`valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close`):
  > al open EDs (4)  | ED | Description | Status | |---|---|---| | ED-710 | Settlement adjacency graph | Workplan-scale, deferred | | ED-711 | Fractional province ownership | Workplan-scale, deferred | | ED-768 | 13 orphaned PROVISIONAL markers | Jordan-blocked review | | TC→CI bulk propagation | ~675 residual TC references in active spec | Queued cleanup |  ### Tests not run  21, 23, 25, 32, 37, 61, 
- **canon context** (`canon/editorial_ledger.yaml`):
  > ers. 75%-share threshold triggers Consolidation Domain Action. Spec: designs/provincial/fractional_province_ownership_v30.md (PP-666)."     status: open     severity: P2     source: "PP-666"    - id: ED-768     date: 2026-04-24     description: "Orphaned PROVISIONAL markers identified across active spec corpus. 13 markers reference low-numbered EDs (ED-063, ED-071, ED-074, ED-098, ED-137, ED-147, 

### ED-779 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close`):
  > spec | Queued cleanup |  ### Tests not run  21, 23, 25, 32, 37, 61, 62, 64, 65.  ### Belief mechanic propagation  Canonical Belief content still resides in `deprecated/valoria_ttrpg_complete §10.2`. ED-779 (Inspiration) §5.3.4 includes a TODO note flagging this for separate future propagation.  ### True blockers  - D-4 Altonian invasion timeline revision (separate workplan per session log). - D-5 
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > rement carried over from base spec. Cross-references generational_transition_v30 (canonical PC successor mechanism). Source: 2026-04-25 stress-test 49."     status: resolved     severity: P3    - id: ED-779     date: 2026-04-25     description: "Inspiration mechanic propagated to canonical derived_stats §5.3. Closes propagation defect surfaced by stress-test 52: canonical Inspiration spec existed 

### ED-783 — **MENTIONED-IN-CANON**

- **detail:** Appears in `canon/00_philosophical_foundations.md` but not as a defined entry in primary register.
- **atom context** (`valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close`):
  > this conversation: - `b14f067` — `[editorial] §16 rewrite (Drift From Human-Mode Being) + censure rectification across foundations, rules, canon/01 cross-refs, canon/02 P-02/P-06/P-10/P-12 — PP-675 / ED-783` - `aae1e72` — `[editorial] §16.1 close — operational origin of Coherence loss (alignment vs opposition to substrate tendency) — PP-675 / ED-783`  These are flagged for awareness; they were not
- **canon context** (`canon/00_philosophical_foundations.md`):
  > ir tension.  **Part Seven: Coherence and the Drift of the Practitioner's Configuration**  **16. The Drift From Human-Mode Being**  [EDITORIAL: PP-675 ED-783 — resolved 2026-04-25; §16 rewritten as "The Drift From Human-Mode Being." Integrates layer-two dual facings (reflexive / outward apperception), tridimensional manifestation per inseparability, equilibrium-decoupling phenomenology, and reality

### M-4 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta.md`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > ## Context Window 3 — ED-717 + Cleanup  ### ED-717: Faction Substrate-Postures (М-4 Throughlines)  Every faction now has a defined relationship to Thread/substrate. М-4 count: 4 → 7.  #### T-15a: Hafenmark — Unmediated Sovereigntist  Baralta is the Protestant faction. Shares Church theology entirely (Solmund is divine, threadwork is heresy, Solmundian ethics are correct) but rejec
- **canon context** (`references/throughlines_meta.md`):
  > l.md --> <!-- [EDITORIAL: PP-672 — throughlines hierarchical framework, canonical vetting guide, 2026-04-19] --> <!-- [EDITORIAL: ED-717 — T-15a/b/c Hafenmark/Löwenritter/RM substrate-postures added, М-4 count 4→7, ED-717 CLOSED] --> <!-- [EDITORIAL: Session B — T-10 struck (Niflhel dissolved), М-4 count 5→4] --> <!-- [EDITORIAL: PP-674 — added tier N (Necessity Test), framework enforcement via ve

### PP-675 — **MENTIONED-IN-CANON**

- **detail:** Appears in `canon/00_philosophical_foundations.md` but not as a defined entry in primary register.
- **atom context** (`valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close`):
  > duced by this conversation: - `b14f067` — `[editorial] §16 rewrite (Drift From Human-Mode Being) + censure rectification across foundations, rules, canon/01 cross-refs, canon/02 P-02/P-06/P-10/P-12 — PP-675 / ED-783` - `aae1e72` — `[editorial] §16.1 close — operational origin of Coherence loss (alignment vs opposition to substrate tendency) — PP-675 / ED-783`  These are flagged for awareness; they
- **canon context** (`canon/00_philosophical_foundations.md`):
  > by their tension.  **Part Seven: Coherence and the Drift of the Practitioner's Configuration**  **16. The Drift From Human-Mode Being**  [EDITORIAL: PP-675 ED-783 — resolved 2026-04-25; §16 rewritten as "The Drift From Human-Mode Being." Integrates layer-two dual facings (reflexive / outward apperception), tridimensional manifestation per inseparability, equilibrium-decoupling phenomenology, and r

### T-08 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta_infill.md`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > Löwenritter + T-15c RM |  ### Complete М-4 Map  | T | Faction | Substrate-Posture | Conscious? | TS | Revelation Crisis | |---|---------|-------------------|------------|-----|-------------------| | T-08 | Church | Rendering reinforcement | Yes | Varies | Substrate reality threatens essentialist theology | | T-09 | Varfell | Thread progressive | Yes | High | Vindicated but politically exposed | | 
- **canon context** (`references/throughlines_meta_infill.md`):
  > momentum. | | T-06 | IP Accumulation | М-1 | — | Clock — continuous pressure from external intervention. | | T-07 | Turmoil | М-1 | — | Clock — continuous pressure from accumulated war. | | T-08 | Church Rendering Reinforcement | М-4 | — | Institutional — Church's substrate-posture is rendering-reinforcement. | | T-09 | Varfell Thread Progressive | М-4 | — | Institutional — Varfell's pos

### T-09 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta_infill.md`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > on Crisis | |---|---------|-------------------|------------|-----|-------------------| | T-08 | Church | Rendering reinforcement | Yes | Varies | Substrate reality threatens essentialist theology | | T-09 | Varfell | Thread progressive | Yes | High | Vindicated but politically exposed | | T-11 | Crown | Pragmatic instrumentalist | Yes | 0 | Tool becomes uncontrollable force | | T-15a | Hafenmark |
- **canon context** (`references/throughlines_meta_infill.md`):
  > r Strain | М-1 | — | Clock — continuous pressure from accumulated war. | | T-08 | Church Rendering Reinforcement | М-4 | — | Institutional — Church's substrate-posture is rendering-reinforcement. | | T-09 | Varfell Thread Progressive | М-4 | — | Institutional — Varfell's posture is thread-progressive. | | T-10 | **STRUCK** (Niflhel dissolved) | — | — | Niflhel dissolved as faction. Thread exploita

### T-11 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta_infill.md`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > -08 | Church | Rendering reinforcement | Yes | Varies | Substrate reality threatens essentialist theology | | T-09 | Varfell | Thread progressive | Yes | High | Vindicated but politically exposed | | T-11 | Crown | Pragmatic instrumentalist | Yes | 0 | Tool becomes uncontrollable force | | T-15a | Hafenmark | Unmediated sovereigntist | Yes | 0 | Divine right without divine access | | T-15b | Löwen
- **canon context** (`references/throughlines_meta_infill.md`):
  > utional — Varfell's posture is thread-progressive. | | T-10 | **STRUCK** (Niflhel dissolved) | — | — | Niflhel dissolved as faction. Thread exploitation distributed to settlement-level phenomena. | | T-11 | Crown Pragmatic | М-4 | — | Institutional — Crown's posture is instrumentalist. | | T-15a | Hafenmark Unmediated Sovereigntist | М-4 | М-6 | Primary institutional (divine-right governance rejec

### T-21 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta_infill.md`.
- **atom context** (`valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup`):
  > e access | | T-15b | Löwenritter | Substrate-agnostic protector | Yes | 0 | Wrong war — enemy is physics | | T-15c | RM | Substrate-heritage reclaimer | **No** | 0 | Vindication + identity crisis | | T-21 | (cross-faction) | Thread political warfare | — | — | Mutual deterrence via shared RS |  ### Editorial + Cleanup  | Commit | SHA | What | |--------|-----|------| | 13 | `fb16bd3` | ED-717 resolv
- **canon context** (`references/throughlines_meta_infill.md`):
  > c convergence point). Secondary pressure-feeding (expedition failure advances decay). | | T-20 | Two Contests | М-6 | — | Forced-choice — sovereignty vs survival, insufficient resources for both. | | T-21 | Thread Political Warfare | М-4 | М-3 | Primary institutional (distinct faction doctrines). Secondary substrate-grounded (shared RS track). | | T-22 | Belief Lattice | М-6 | М-3 | Primary forced

## Path verification

| path | status | atom occurrences |
|---|---|---|
| `canon/00_philosophical_foundations.md` | EXISTS | 9 |
| `canon/02_canon_constraints.md` | EXISTS | 7 |
| `canon/01_foundations_amendment_self_rendering.md` | EXISTS | 6 |
| `canon/00_philosophical_foundations_rules.md` | EXISTS | 5 |
| `canon/02_foundations_amendment_leap_mechanism.md` | EXISTS | 5 |
| `canon/03_canonical_timeline.md` | EXISTS | 3 |
| `references/censured_vocabulary.yaml` | MISSING-FROM-REPO | 2 |
| `canon/editorial_ledger_summary.yaml` | EXISTS | 2 |
| `references/canonical_sources.yaml` | EXISTS | 2 |
| `canon/README.md` | EXISTS | 2 |
| `canon/editorial_ledger_index.md` | EXISTS | 2 |
| `canon/patch_register_index.md` | EXISTS | 2 |
| `canon/session_checkpoint.md` | EXISTS | 2 |
| `references/throughlines_complete.md` | EXISTS | 2 |
| `references/alias_registry.yaml` | EXISTS | 2 |
| `references/file_index_summary.md` | EXISTS | 1 |
| `designs/threadwork/threadwork_v30.md` | EXISTS | 1 |
| `designs/npcs/npc_behavior_v30.md` | EXISTS | 1 |
| `designs/ui/valoria_ui_ux_v4_1.md` | EXISTS | 1 |
| `designs/arcs/arc_expansion_v30.md` | EXISTS | 1 |
| `designs/provincial/faction_politics_v30_index.md` | EXISTS | 1 |
| `designs/architecture/player_agency_v30.md` | EXISTS | 1 |
| `designs/audit/throughlines_transitions_hierarchy.md` | EXISTS | 1 |
| `designs/audit/valoria_systems_workplan.md` | EXISTS | 1 |
| `designs/scene/fieldwork_godot.md` | EXISTS | 1 |
| `designs/world/worldbuilding_canon_audit_v30_infill.md` | EXISTS | 1 |
| `references/throughlines_meta_infill.md` | EXISTS | 1 |
| `references/propagation_log.md` | EXISTS | 1 |
| `params/board_game.md` | EXISTS | 1 |
| `params/bg/ministry.md` | EXISTS | 1 |
| `designs/scene/conviction_track_v30.md` | EXISTS | 1 |
| `params/core.md` | EXISTS | 1 |

## Substantive claim findings

_29 substantive claims (max 3 per atom) with best-match canon excerpts._

### Matched claims (27)

- **atom** `valoria_session_2026-04-25_master__09__section-9-o`
  - claim: > ED-779 (Inspiration) §5.3.4 includes a TODO note flagging this for separate future propagation.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 6/7)
  - canon excerpt: > es generational_transition_v30 (canonical PC successor mechanism). Source: 2026-04-25 stress-test 49."     status: resolved     severity: P3    - id: ED-779     date: 2026-04-25     description: "Inspiration mechanic propagated to canonical derived_s

- **atom** `valoria_session_2026-04-25_master__09__section-9-o`
  - claim: > - SIM-NPC-01 + sim-validation queue: requires `engine_v4`.
  - best match: `canon/editorial_ledger.yaml` (overlap 2/4)
  - canon excerpt: > izure available, 75 = Phase Transition / Territorial Seizure, 100 = Unification (per ci_political_v30 §2). Residual ~675 TC references in active spec queued as known cleanup item; not propagated in this commit. Source: 2026-04-25 stress-test 60."    

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Scope

This work consolidates a single coherent batch:

1.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/5)
  - canon excerpt: > ation arc (3+ caste-transgressive engagements within 4-season window triggers mandatory Priority 0 Zoom-In; Spirit pool TN 7 Ob 3 resolution; Success consolidates transgressive Conviction permanently; Partial = caste-default Conviction crisis with PC

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Rewrite `canon/00_philosophical_foundations.md` to remove censured terminology and execute Jordan's directives on P-02 (Lacanian Real grounding for monstrosity), P-10 (Coherence-as-commensurability), P-12 (drift propagation), philosophical foundation
  - best match: `canon/patch_register_active.yaml` (overlap 3/8)
  - canon excerpt: > # Patch Register — Active # Applied/approved/consumed patches archived to canon/patch_register_archive_*.yaml # Next PP number: 664  patches:  - id: PP-297   date: 2026-04-02   severity: P1   description: Mass battle stalemate resolution — Tactical W

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Audit the rewrite for logical consistency against existing canon (canon/01 self-rendering amendment, canon/02 leap mechanism amendment) and against Jordan's articulated philosophical content on Coherence (apperception, intersubjective judgment, etymo
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > ister entries from PP-674 forward. New task type design_proposal requires loading throughlines_meta.md. Tier N added above Ω: subject-grounding check against Renaissance-era political-leadership dynamics. Four new Failure Lexicon terms (fantasy impos

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Patch O: +1 strain/season on Close Knots at Taint 4–6" |

### `canon/00_philosophical_foundations_rules.md` — 4 lines

A11 (axiom heading), C4 (constraint heading), B-table glossary row, D enforcement-line — all named "Epistemic Seduction" structural
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/8)
  - canon excerpt: > : P2     source: "PP-667"    - id: ED-715     date: 2026-04-19     description: "OPEN ITEMS sweep across settlement_layer, military_layer, peninsular_strain, faction_layer, victory_v30, threadwork_v30 — 26 items resolved, 5 superseded by PP-663/PP-66

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > corruption"  → rewritten as Coherence-commensurability
  P-12 referenced "Taint 4–6"  → rewritten as tridimensional drift propagation
       ↑ cited by ↓
canon/01_foundations_amendment_self_rendering.md (§16.1 cross-ref)  → updated
[+ ~30 design file
  - best match: `canon/patch_register_active.yaml` (overlap 3/8)
  - canon excerpt: > sa Vossen.     43 instances of 'Yrsa Vossen' replaced across 25 files. 2 standalone 'Maret'     instances in Aldric Hann's belief quote (RM context) rewritten to 'Yrsa'.     Remaining standalone 'Maret' instances refer to Maret Uln and are unchanged

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Anything appearing 5+ times but unregistered is a candidate for review.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/6)
  - canon excerpt: > ion target is designs/world/ (worldbuilding), NOT canon/02_foundations_amendment_leap_mechanism.md (prior mis-mapping corrected). Specific home TBD — candidates: new designs/world/einhir_site_network.md or expansion of designs/world/calamity_radiatio

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > needs-replacement-decision).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/3)
  - canon excerpt: > ed names (Stark/Voss/Vorn/Kald) replaced with faction_politics §3.5 + npc_roster §13 canonical (Jarnstal/Olafsson/Aldric Tormann/Klapp). Bulk surname replacement applied across arc_expansion. Closes ED-591/592/593/594."     status: resolved     sever

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > The first-pass §16 rewrite under-articulated this.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: > _strain §5.2 adds explicit Uncontrolled exclusion — Seizure requires Mandate-bearing controller (no Mandate to exceed). Uncontrolled territories must first come under control via Pastoral Assumption, Conquest, or RM Founding before Seizure can target

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > The Leap-mechanism amendment Amendment 1 already distinguished reflexive and outward facings of layer 2; the first-pass §16 specified only reflexive.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > esponsive Warden-era reactive + ambient/not-scheduled). Integration target is designs/world/ (worldbuilding), NOT canon/02_foundations_amendment_leap_mechanism.md (prior mis-mapping corrected). Specific home TBD — candidates: new designs/world/einhir

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > canon/01 Amendment 3 explicitly stated apperception by others as a Coherence diagnostic; the first-pass §16 missed this entirely.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > # Valoria Editorial Ledger — Archive (resolved entries) # Migrated 2026-04-20 from canon/editorial_ledger.yaml. # New resolutions accumulate in main; migrate on next cap pressure.  entries:    - id: ED-713     date: 2026-04-19     description: "Mine 

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Others — whose renderings must work harder to integrate the drifting practitioner as a coherent human subject — register the failure first, through the somatic and perceptual labour of attempting to apperceive what their rendering's specification can
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/8)
  - canon excerpt: > de the original province-scale Cultural Uprising trigger. Eliminates need for separate designs/provincial/faction_succession_split_v30.md — mechanism integrates into existing canonical specs rather than spinning out new doc."     status: resolved    

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > This is why Coherence diagnostics depend on intersubjective observation in canon/01's "Fragmented" and "Fractured" bands, where the practitioner is apperceived differently by different observers.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > ixes (4 broken refs across 3 spec files). (1) mass_battle L446/447: §5.2.2/§5.2.3 (nonexistent in mass_battle's flat structure) → threadwork_v30 §3.2 Coherence Reduction (correct referent for per-operation Coherence cap). (2) mass_battle L575: §4.3.4

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Categorical distinction from Coherence-0 practitioners explicit.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/5)
  - canon excerpt: > equence-Resonant-Style loophole. Historical anchor: Privy Counsellor's oath, medieval evil-counsellor doctrine, curia regis great-council/small-curia distinction."     status: resolved     severity: P2    - id: ED-662     date: 2026-04-17     descrip

- **atom** `valoria_session_2026_04_25_master_consolidation__0`
  - claim: > Violation test catches single-dimension reductions, moral-standing framing, and Coherence-0/threadcut conflation.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/8)
  - canon excerpt: >  2026-04-24     description: "Settlement Revolt Mandatory Zoom-In gains deduplication: settlement-events at same settlement same season collapse into single Mandatory entry. Source: 2026-04-24 audit §3.5."     status: resolved     severity: P3    # M

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Outstanding Work

### 10.1 Term-governance enforcement infrastructure (NEXT)

Implementation of Layers A/B/D/E from §4 architecture.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/7)
  - canon excerpt: >   severity: P1     source: "session_master_2026_04_20.md + handoff"    - id: ED-723     date: 2026-04-20     description: "D-2 resolved: pre-Calamity governance author-determined, surfaced through fragments. Altonian overlays do not map to pre-Calami

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Now that canon is clean, the gates can prevent reintroduction:

1.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/5)
  - canon excerpt: > # Valoria Editorial Ledger — Archive (resolved entries) # Migrated 2026-04-20 from canon/editorial_ledger.yaml. # New resolutions accumulate in main; migrate on next cap pressure.  entries:    - id: ED-713     date: 2026-04-19     description: "Mine 

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Add status-block line: "Censured terms: [N loaded]."
3.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/5)
  - canon excerpt: > ling faction. Guild management +1, Trade Network token +1. Cap 4 Wealth/Mine/year. See designs/audit/gap_resolution_2026-04-19.md §1.1 (PP-667)."     status: resolved     severity: P2     source: "PP-667"    - id: ED-714     date: 2026-04-19     desc

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Key Decisions

Decisions made during this work that future sessions need to know:

| # | Decision | Rationale |
|---|---|---|
| K-1 | "Drift" is the working term for the Coherence-indexed phenomenon | Etymology of "Coherence" (cohaerere = to adhere t
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/8)
  - canon excerpt: > lding. Most likely vestigial reference from pre-2026-04-19 mechanism consolidation (Coup Counter struck → Graduated Autonomy; other mechanism strikes during that pass). If a Ministry Protocol surface re-emerges later, established historical seniority

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Cross-references to canon/01 and canon/02 amendments are at the foundations tier (parallel philosophical work), not mechanics tier.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 7/8)
  - canon excerpt: > og carry-over. Source: 2026-04-24 numeric bounds audit."     status: resolved     severity: P3    - id: ED-771     date: 2026-04-25     description: "Cross-reference audit fixes (4 broken refs across 3 spec files). (1) mass_battle L446/447: §5.2.2/§5

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > ~470 lines of TTRPG / board-game / video-game / hybrid mechanics content removed.
  - best match: `canon/patch_register_active.yaml` (overlap 5/7)
  - canon excerpt: > .md   status: applied   applied_commit: pending - id: PP-671   date: 2026-04-19   severity: P2   description: "Meta-throughline synthesis from throughlines_complete.md (25 throughlines,     8 categories). Identified 5 meta-throughlines operating ACRO

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Process / Meta Observations

For future sessions and for general project hygiene:

1.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/7)
  - canon excerpt: > tion"    - id: ED-742     date: 2026-04-24     description: "social_contest §6.1 Obligations extended to permit Wager Obligation framing — verifiable-future-condition commitment in Grand Contest using Projection genre + Consequence Resonant Style. Ge

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > **The amendment-exceeds-foundations pattern is a documentation anti-pattern.** When canon/01 and canon/02 amendments accumulated philosophical content, that content should have been upstreamed into foundations rather than living only in amendments.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 7/8)
  - canon excerpt: > e scheduled + responsive Warden-era reactive + ambient/not-scheduled). Integration target is designs/world/ (worldbuilding), NOT canon/02_foundations_amendment_leap_mechanism.md (prior mis-mapping corrected). Specific home TBD — candidates: new desig

- **atom** `valoria_session_2026_04_25_master_consolidation__1`
  - claim: > Future amendments should explicitly upstream their philosophical work to the foundation document at the time of the amendment.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/8)
  - canon excerpt: >  TC-density design docs (npc_faction_arc_interdependency, narrative_scenario_chains, conviction_track_v30, arcs_46_55_resolved, faction_politics_v30) explicitly stating TC = Theocracy Counter (Conviction Track is always written in full). Manual revie

- **atom** `valoria_session_master_2026-04-25__03__context-win`
  - claim: > Shares Church theology entirely (Solmund is divine, threadwork is heresy, Solmundian ethics are correct) but rejects two things: that the Holy Confessor has exclusive access to Solmund, and that the Church should govern.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/8)
  - canon excerpt: > Einhir suppression DA — resolved as non-mechanics. Both exist only as worldbuilding texture. Existing mechanics (Trade Network, Heresy Investigation, Church AP, Parliamentary Motion) cover the design space. See designs/audit/gap_resolution_2026-04-19

- **atom** `valoria_session_master_2026-04-25__03__context-win`
  - claim: > **Crisis at revelation:** If Thread access is experiential, Baralta's TS 0 means she cannot personally access what she claims to govern by right of faith.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > battle §A.10. Source: 2026-04-24 audit §3.12."     status: resolved     severity: P3    - id: ED-749     date: 2026-04-24     description: "Stability Crisis Mandatory Zoom-In gains hysteresis: re-arms only after Stab ≥ 3 maintained for 2 consecutive 

### Unmatched claims — possibly NEW or rephrased (2)

- atom `valoria_session_2026_04_25_master_consolidation__0`: > Both must be intact for Coherence.
- atom `valoria_session_master_2026-04-25__03__context-win`: > **Chain:** Shared Solmundian theology → rejection of ecclesial monopoly → divine-right governance → Parliamentary Suppress CI → Dynastic Proclamation → Thread revelation forces confrontation (TS 0 means Baralta can't access what she claims governance

## Recommendation

**Recommendation: INGEST-WITH-PATH-FIXES — 1 repo paths missing.**

- ID classification: {'DEFINED-IN-CANON': 11, 'MENTIONED-IN-CANON': 2, 'PARTIAL': 0, 'NEW': 0}
- Path verification: {'EXISTS': 31, 'MISSING-FROM-REPO': 1}
- Substantive: 27 matched / 2 unmatched