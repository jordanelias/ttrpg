# G — Setup & Ignition Audit
## setup_ignition_stress_01

**Date:** 2026-05-10
**Mode:** A coverage (state audit) across three setup-phase mechanics.
**Scope:** B4 Tensions Deck, B17 Geography Phase 2, B19 Niflhel dissolution.

This module is a state audit — for each backlog item, verify canonical state, identify gaps, and route to next-step PP or carryover.

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| G-L01 | niflhel_dissolved_struck | Niflhel STRUCK; four-arm structure eliminated | designs/npcs/npc_behavior_v30.md | §2.12 | "**STRUCK** — Niflhel dissolved (conflict_architecture_proposal). Four-arm structure eliminated. Functions distributed to settlement-level phenomena." |
| G-L02 | ed777_arc_reframe_standing | 5 arcs require reframe; standing | canon/editorial_ledger.yaml | ED-777 | "[STANDING] arc_register_factions.md — 5 arcs require reframe. Niflhel is not a faction. Crime and underground networks exist in Valoria but are not threadwork-related. Affected: ARC-S11, ARC-S54, ARC-S55, NPC-ARC-VIR, ARC-T25." |
| G-L03 | ed777_jordan_decision | Niflhel not faction; crime/underground exists but not threadwork-related | canon/editorial_ledger.yaml | ED-777 | "2026-05-09 — Niflhel not a faction. Crime/underground exists but not threadwork-related. Reframe 5 arcs around that." |
| G-L04 | phase_2_geography_executed | Phase 2 geography canon executed per ED-779 | canon/patch_register_active.yaml | PP-710 | "Phase 2 geography canon executed (ED-779). Authors designs/territory/valoria_geography_v30.yaml as the data canon for Valoria geography at canonical 1920×2880: 17 territory anchors (jsx-derived via" |
| G-L05 | ed780_phase_3_standing | Phase 3 spec rewrite + march_layer authored; ED-780 standing | canon/editorial_ledger.yaml | ED-780 | "[STANDING] Phase 3 of geography canon work — spec rewrite (depends on ED-779 completion). Approved scope 2026-05-09: (a) rewrite settlement_adjacency_v30 to query geography data rather than abstract edge-types; (b) author march-bubble + encounter-trigger spec (new doc designs/territory/march_layer_v30.md); (c) update mass_battle_v30 §A.9 / §B.5 for geographic battle-terrain derivation at engagement coordinates." |
| G-L06 | ed781_phase_4_stress_tests | Phase 4 stress tests queued (3 scenarios); standing | canon/editorial_ledger.yaml | ED-781 | "[STANDING] Phase 4 of geography canon work — stress tests (depends on ED-780 completion). Three scenarios queued: (1) Mountain Pass battle (T2/T11 Halvardshelm pass — geometry-constrained engagement, narrow-pass clamp emergence); (2) Open-field cavalry encounter (T2 Kronmark plains — flanking-as-position vs declaratory); (3) Coastal landing (Schoenland → T13 Oastad — amphibious sequencing, no naval mechanics per ED-780 scope)." |

**Note:** B4 Tensions Deck does not have a canonical source in cached canon. It appears to be a backlog item not yet designed — see Section 4.

---

## 2. State audit per sub-module

### G2.1 — B4 Tensions Deck

**Canonical state:** **NOT YET DESIGNED.** No matches for "Tensions Deck" in mass_battle_v30, npc_behavior_v30, fieldwork_v30, social_contest_v30, conviction_taxonomy_v30, derived_stats_v30, params files, patch_register_active, or editorial_ledger.

**Inferred intent:** From the F/G/A/D handoff context, "Tensions Deck B4" appears to be a game-startup mechanic that scaffolds initial faction tensions, NPC dispositions, and territory pressures at campaign begin. Common in 4X / RPG systems (Crusader Kings, Stellaris) as a "starting situation" composer.

**Recommended action:** Design item. Author a PP defining:
- What the Tensions Deck is (a card-based initial-conditions composer? A procedural generator? A pre-defined scenario set?)
- What it composes (faction Disposition initial values? Territory ownership? NPC Conviction starting weights? Economic state? Active arcs?)
- Where it sits in the campaign-startup pipeline (before character creation? After? Per-campaign or per-territory?)
- Interaction with ED-734's character-creation pipeline (if any).

This is a substantial design initiative requiring Jordan's authoring direction. **Recommend: separate session for Tensions Deck design.**

### G2.2 — B17 Geography Phase 2

**Canonical state:** **COMPLETE per G-L04 (PP-710 / ED-779; commit 2026-05-01).** `designs/territory/valoria_geography_v30.yaml` exists at 28,319 bytes with:
- 17 territory anchors (jsx-derived via 01_coord_transform pattern)
- 17 hand-authored Voronoi-style province polygons
- 36 settlement coordinates with type-bias placement
- 26 adjacency edges (incl. T15 gates T6+T13, T1↔T16 coastal, T10↔T11 mountain_pass per PP-709 §2.4)
- 20 terrain polygons (8 canonical types from PP-709 §2.1)
- Lake Eidursjø, river Valoris + 2 bridges, forgetting_zone overlay
- 6 calamity radiation bands
- march_budget formula (Military×100px; cavalry 1.5×, skirmish 1.3×)
- vision_range multiplicative composition

**Open downstream:** ED-780 (Phase 3 spec rewrite — settlement_adjacency_v30, march_layer_v30, mass_battle_v30 §A.9/§B.5) and ED-781 (Phase 4 stress tests — Mountain Pass, Open-field cavalry, Coastal landing) per G-L05 and G-L06. Both standing.

**Recommended action:** Phase 2 done. Carryover: ED-780 + ED-781 are queued downstream.

### G2.3 — B19 Niflhel dissolution

**Canonical state:** **STRUCK per G-L01.** `npc_behavior_v30 §2.12` confirms: "Niflhel dissolved (conflict_architecture_proposal). Four-arm structure eliminated. Functions distributed to settlement-level phenomena."

**Open downstream:** ED-777 standing (G-L02 + G-L03). 5 arcs require reframe:
- ARC-S11
- ARC-S54
- ARC-S55
- NPC-ARC-VIR
- ARC-T25

Jordan's 2026-05-09 decision (G-L03): Niflhel is not a faction. Crime/underground exists in Valoria but is not threadwork-related. Reframe 5 arcs around that.

**Recommended action:** Niflhel canon dissolution complete in core docs. ED-777 reframe of 5 arcs is a separate editorial task.

---

## 3. NERS at full grain — setup & ignition coherence (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ✓ | ⚠ | ⚠ N: B4 Tensions Deck not designed — game-startup pipeline has a gap. ⚠ S: setup-phase systems are partial; B17 (geography) and B19 (Niflhel dissolution) are coherent but B4 absent leaves a hole in initial-conditions composition. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Bottom-up: territory anchors (G-L04) + Niflhel-functions-distributed-to-settlements (G-L01) + character creation = startup elements present except Tensions Deck. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Cross-scale: territory anchors (faction scale) + settlement coordinates (settlement scale) + Niflhel functions distributed to settlement phenomena. Vertical coverage adequate. |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | ⚠ E, ⚠ S on ED-777: 5 arcs reference Niflhel as faction — pending reframe. Cross-system narrative authoring blocked until reframe done. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Lateral: geography (territory) + Niflhel-dissolved (npc/factions) integrate cleanly without further crossover until B4 designed. |
| Horizontal | ⚠ | ⚠ | ⚠ | ⚠ | Campaign-arc Horizontal: a campaign begins with B4 Tensions Deck composing initial conditions (currently unimplementable), B17 geography (complete data canon), B19 Niflhel dissolved at start. The Tensions Deck gap means campaigns currently begin with NO initial-conditions composer — defaults to a hardcoded scenario or designer-authored single state. |

**Verdict:** 17/24 ✓, 7 ⚠ — most ⚠s tied to B4 Tensions Deck gap. B17 and B19 individually pass; the system-level coherence flag is the missing B4 component.

---

## 4. Decision-shape findings

**Recommendation per sub-module:**

1. **B4 Tensions Deck — design needed.** Open new PP (e.g., PP-X) authoring the Tensions Deck specification. Substantial initiative requiring Jordan's design direction. Defer to separate design session.

2. **B17 Geography Phase 2 — complete.** ED-779 done. Carryovers: ED-780 (Phase 3 spec rewrite) and ED-781 (Phase 4 stress tests) standing. Both queued in editorial ledger; appropriate next-step structure.

3. **B19 Niflhel dissolution — core canon done; 5 arcs pending reframe.** ED-777 standing addresses arc reframe per Jordan's 2026-05-09 decision. Separate editorial task, not a design gap.

**Setup pipeline composite state:**

| Component | State | Next step |
|---|---|---|
| B4 Tensions Deck | NOT DESIGNED | New PP authoring spec — substantial design initiative |
| B17 Geography Phase 2 | COMPLETE (ED-779) | ED-780 Phase 3 + ED-781 Phase 4 (standing carryovers) |
| B19 Niflhel dissolution | DONE in core canon | ED-777 5-arc reframe (standing carryover) |

**Decision-shape statement for Jordan ratification:**

> Setup & ignition pipeline state: B17 Geography Phase 2 complete (ED-779; ED-780 + ED-781 are standing downstream). B19 Niflhel dissolution complete in core canon (npc_behavior §2.12 STRUCK); 5-arc reframe pending per ED-777. **B4 Tensions Deck is undesigned — a substantial design initiative requiring Jordan's authoring direction in a separate session.** Without B4, campaign-startup composition has a structural gap: initial conditions default to hardcoded scenario or designer-authored single state.

---

## 5. Open follow-ups (consolidated carryover)

From this session (D + A + F + G):

| Priority | Item | Source |
|---|---|---|
| P1 | A1 follow-up PP — fix `npc_behavior_v30 §1.2` redirect to point at canonical `conviction_taxonomy_v30.md`; verify Scar accumulation under structured concentration | A module commit `57bd26f4` |
| P1 | B4 Tensions Deck design initiative — substantial new PP | G2.1 this module |
| P2 | F3 Heresy Investigation lifecycle audit | F module commit `ddccbf9a` |
| P2 | F4 Mending B10/B11 lifecycle audit + PP-716 propagation check | F module commit `ddccbf9a` |
| P2 | ED-777 5-arc reframe (ARC-S11, S54, S55, NPC-ARC-VIR, T25) per Jordan's 2026-05-09 decision | G2.3 / G-L02 |
| P2 | ED-780 Phase 3 geography spec rewrite (settlement_adjacency_v30, march_layer_v30, mass_battle §A.9/§B.5) | G2.2 / G-L05 |
| P3 | ED-781 Phase 4 geography stress tests (Mountain Pass / Open-field cavalry / Coastal landing) | G2.2 / G-L06 |
| P3 | EC-F2.A-01 — sustained Disposition reduction definition (continuous vs cumulative) | F module |
| P3 | R4 C4.3 deferred refinement — context-sensitive Tier-2 default once Q5 T-trigger criteria specified | R4 commit `dea58c26` |
| P3 | R5 C5.3 voluntary stake escalation — separate design initiative if pursued | R5 commit `d46ad908` |
| P3 | R7 stress-FF threshold enumeration | R7 commit `c58bc670` |
| P3 | R9 routine-encounter B reservation trigger spec | R9 commit `1c31109d` |
| Open | VALORIA_PAT exposure rotation | architecture spec |
| Open | read_active_sessions defect (concurrent-session detection unreliable) | hooks |
| Open | fieldwork_v30 §3 line 364 stale "PP-684" citation | per session log |
| Open | canonical_sources.yaml manifest naming drift (clock_system/territory_model vs clocks/territories) | architecture spec |

---

## 6. Module status

| Item | Status |
|---|---|
| Sources surveyed (npc_behavior §2.12 Niflhel; editorial_ledger ED-777/780/781; patch_register PP-710) | ✓ |
| Verification ledger (6 entries) | ✓ |
| State audit per sub-module (B4, B17, B19) | ✓ |
| NERS coherence analysis | ✓ |
| Decision-shape per sub-module | ✓ |
| Consolidated carryover register (D + A + F + G) | ✓ |

**setup_ignition_stress_01 status: verified.**

**Session conclusion — D-A-F-G complete:**

| Module | Commits this/prior session |
|---|---|
| D combat_arch_residual_stress_01 (R1-R10) | `df2611a1` (manifest), `45c693e2` (R1 v1), `6e3a8aed` (PP-716), `936e1533` (freshness), `13e288a8` (R1 v2), `27e7983c` (R2), `69c4d829` (R3), `dea58c26` (R4), `d46ad908` (R5), `856c6098` (R6), `c58bc670` (R7), `b86b7094` (R8), `1c31109d` (R9), `55d520c4` (R10), `2539c9a8` (manifest cleanup) |
| A conviction_stress_01 | `57bd26f4` |
| F fieldwork_lifecycle_stress_01 (F2 Knot Lifecycle) | `ddccbf9a` |
| G setup_ignition_stress_01 | (this commit) |

D-A-F-G stress sweep done. Next-session priorities are documented in Section 5.


---

## 7. Amendment 2026-05-10 — B4 Tensions Deck IS designed

**Original G2.1 finding was incorrect.** Subsequent canonical-source survey discovered:

- `params/bg/tensions_deck.md` (2,068 bytes) — 6-card spec, draw-1-at-game-start mechanic.
- Source: `designs/architecture/conflict_architecture_proposal.md` (CANON 2026-04-18 per `references/canonical_sources.yaml` L142).
- `references/canonical_sources.yaml` L135-138 declares the canonical entry:
  ```yaml
  tensions_deck:
    design_doc: params/bg/tensions_deck.md
    canonical_sha__params__bg__tensions_deck_md: "c3e77304addce12c41507800bf0c058ea8667d74"
    source: conflict_architecture_proposal.md
  ```

**Tensions Deck cards (per params/bg/tensions_deck.md):**

| # | Card | Amplifies | S8+ Event |
|---|---|---|---|
| 1 | Royal Crisis | T1 Crown-Church friction + succession | Royal family member assassinated (sub-roll per royal_assassination.md) |
| 2 | Feldmark Famine | T5 Crown breadbasket | Prosperity collapse → economic crisis |
| 3 | Cardinal Independence | T1 + T9 Church internal | Rogue Cardinal appoints bishop-governor in Crown settlement |
| 4 | Guild Fracture | T8 Hafenmark-Guild friction | S017 Guild schism → Market Quarter contested |
| 5 | Einhir Incident | T4 + T13 Varfell-RM friction | Public confrontation forces faction position-declarations |
| 6 | Ministry Crisis | T14 Crown-Löwenritter + Crown governance | Ministry collapse → governance vacuum → Church fills |

The Tensions Deck includes a **fuse model** — every card creates a visible fuse from S1 (NPC dialogue, atmospheric events) which the player can investigate and attempt to defuse before the S8+ ignition event.

**Revised G2.1 verdict:** **B4 Tensions Deck is COMPLETE per `conflict_architecture_proposal.md` (CANON 2026-04-18).** No design initiative needed. The G module's earlier "NOT YET DESIGNED" finding stemmed from an incomplete source survey (search was scoped to designs/ paths only and missed the params/bg/ location).

**Revised composite state:**

| Component | State | Next step |
|---|---|---|
| B4 Tensions Deck | **COMPLETE per conflict_architecture_proposal.md** | None — canonical |
| B17 Geography Phase 2 | COMPLETE (ED-779) | ED-780 Phase 3 + ED-781 Phase 4 (standing carryovers) |
| B19 Niflhel dissolution | DONE in core canon | ED-777 5-arc reframe (standing carryover) |

**Revised NERS coherence:** with B4 complete, the structural gap closes. Setup pipeline is fully canonical; remaining work is ED-777 (arc reframes), ED-780 (Phase 3 geography), and ED-781 (Phase 4 stress tests).

**Surfaced editorial item:** the G module's miss of `params/bg/tensions_deck.md` indicates a discoverability defect — readers looking for "setup-phase mechanics" in the canonical-sources index may not navigate to `params/bg/`. Recommend a small editorial note in `references/canonical_sources.yaml` linking the `tensions_deck` entry from a "Setup & Ignition" section header.

**Updated next-session priorities:** B4 design initiative is REMOVED from the open-followups register. P1 remaining: A1 follow-up complete (PP-717 committed `55403f74`).
