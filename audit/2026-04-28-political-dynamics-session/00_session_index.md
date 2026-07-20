<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration index, not canonical -->
<!-- UPDATED: integrates all session work through document 12 -->

# Political Dynamics Design Session — 2026-04-28

## Session Token
`d964fd13158349fa`

## Scope
Comprehensive examination of how interpersonal relationships operate in Valoria and how those dynamics radiate through character advancement, arcs, settlements, governance, and faction politics. Originated from inspiration document `faction_dynamics_audit_v2.md`.

## Current Source of Truth

**`12_development_specification.md`** is the current consolidated specification for development and testing. All earlier documents are preserved for design history; their specific mechanisms may have been superseded.

## Documents in Session

| # | File | Purpose | Status |
|---|---|---|---|
| 00 | `00_session_index.md` | This index | Current |
| 01 | `01_interpersonal_audit.md` | 8-gap audit identifying structural problems | **Foundational** — gaps still valid |
| 02 | `02_initial_proposals_with_historical_precedents.md` | First-pass proposals with Renaissance/medieval/Ottoman/Byzantine/Habsburg precedents | **Historical research preserved**; specific proposals superseded |
| 03 | `03_revision_directionality_emergence.md` | RP-balance system attempt addressing vertical-only chains | **Superseded** by autonomous-actor reframing; reasoning preserved |
| 04 | `04_autonomous_actors_philosophical_reframe.md` | Conceptual pivot to NPCs as persons with inner lives | **Foundational** — informs all subsequent work |
| 05 | `05_groundup_mechanical_proposal.md` | First full mechanical specification | **Superseded** by iterative + streamlining; reasoning preserved |
| 06 | `06_iterative_test_audit_patch_critique.md` | 3 iterations of test → audit → patch → critique | **Reasoning preserved**; specifics superseded by 09/10/12 |
| 07 | `07_armature_system_vetting.md` | Class A vetting per throughlines_meta.md framework | **Vetting outcome PASSES** but needs re-vetting against current spec (12) |
| 08 | `08_event_matrix_meta_armatures.md` | Architectural addition: Event Impact Matrix + meta-armatures + Domain Action integration | **Concepts current**; specifics updated in 09/10/12 |
| 09 | `09_integration_test_streamlined.md` | Integration testing + streamlining (eliminated Procedure A, Threat-sensitivity, etc.) | **Integrated into 12** |
| 10 | `10_stress_tests_all_modalities.md` | 12 stress tests, 17 issues found, 16 patched | **Patches integrated into 12** |
| 11 | `11_top_down_audit.md` | Holistic audit identifying inconsistencies | **Findings drove 12** |
| 12 | `12_development_specification.md` | **CURRENT SPEC — single source of truth for development/testing** | Current |

## Key Architectural Outputs

**The Armature System** — Conviction + Personality + Project domain + Scar count produce weighted interpretive armatures across three dimensions (Agency, Intent, Mechanism). NPCs interpret events through their armatures, generating Concerns that drive autonomous behavior. Replaces original 630-template approach with characteristic-derived weights.

**Three-Scale Meta-Armatures** — NPCs, settlements, and factions all interpret events at their own scale.
- Settlement Meta-Armature: tenure-scaled governor + Passive NPCs + institutional character + population (weights normalized for sparse settlements)
- Faction Meta-Armature: Standing-weighted inner-circle aggregate + leader 1.5× amplification + single institutional_stability term that decays with inner-circle Scars

**Event Impact Matrix** — Computed once per event, scoped to inner-circles of affected factions. Consumed by all armatures interpreting the event. Reduces redundant per-NPC computation while enriching armature input.

**Four Procedures + Real-Time Mood:**
- Mood: real-time (set at event resolution, not batched)
- B: Concern generation/resolution (with calcification, Knowledge-triggered Concerns)
- Domain Action proposal phase (between B and C)
- C: Project advancement (established vs new gating, completed-Project legacy)
- D: Opinion drift (with hard clamp on bounds, Memory salience floors)
- E: Off-screen interactions (60% ambient, 10% Distant Contact, Distracted reduces to 20%)

**Domain Action Integration** — Inner-circle NPCs propose Domain Actions advancing their Projects; Faction Meta-Armature resolves competition; Conviction-aligned supporters give -1 Ob, opposers give +1 Ob.

**Cascade Attenuation** — ×0.7 signal decay per scale boundary; salience below 2 generates Concerns but doesn't influence Domain Action selection.

**Crisis Behaviors** — Faction crisis threshold (≥40% Distracted/Grieving → institutional autopilot), Anomaly detection (≥3 NPCs simultaneously divergent → faction Concern), Minimum inner-circle friction (count <3 → +1 Ob), City-state Domain Actions (limited to Influence/Wealth).

## Throughline Impact

**Throughlines extended/completed:**
- T-14 Conviction Architecture (mechanizes how Conviction structures interpretation)
- T-23 NPC Arc Emergence (explicit Concern → Memory → Belief Revision → Scar chain)
- T-25 Generational Arc (Project shifts toward succession positioning)
- T-27 Effects Real Explanation Wrong (**mechanically functional for the first time** — was canonically committed but deferred)
- T-30 Information Asymmetry (Knowledge structure + interpretive-frame access)

**Meta-throughlines extended:**
- M-1 Pressure continuous (NPC autonomous Outreach generation)
- M-5 Scales connect (3 new scale-bridges: Settlement Signal, Knowledge propagation, Outreach generation cascade)
- M-8 Vertical-position gating (new gate type: interpretive-frame access)

## Canonical Vetting Block (from 07; pending re-vetting against 12)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-β, Μ-α, Μ-δ]
  m_ratings:
    M-1: "+"
    M-2: "○"
    M-3: "✓"
    M-4: "✓"
    M-5: "+"
    M-6: "✓"
    M-7: "✓"
    M-8: "+"
    M-9: "○"
    M-10: "○"
    M-11: "✓"
  q: pass
```

## Outstanding Items Requiring Jordan Decision

**Design decisions:**
1. Wrong-Belief Investigation interaction: Option A (forgiving) vs Option B (harsh, recommended per Ω-d)
2. Authoring scope: full ~1,190 entries vs reduced ~700-800 (impact: what's authored vs dynamically generated)
3. Carryover: Restoring Intelligence as 6th faction stat
4. Carryover: LICENSE / GOV-08

**Content authoring scope** (full per §10 of doc 12):
- Conviction → armature weights (105 entries)
- Personality → armature modifiers (12)
- Event dimension profiles (~270)
- Sentence frame templates (~15)
- Conviction × event symbolic resonance (210)
- Settlement institutional character bias (6)
- Faction institutional_stability values (7)
- Domain Action sponsor mapping (~30)
- Starting Projects per Active NPC (35)
- Personality dimension calibration (~140)
- Starting Opinions, NPC-NPC (~200 recommended)
- Knowledge seeding (~100 recommended)
- Knot integration dialogue fragments (~30)
- Gossip text templates (~30 recommended)

## Promotion Path

To promote from PROVISIONAL to canonical (see §13 of doc 12 for full checklist):

1. Re-vetting against current spec (12)
2. Outstanding decisions resolved
3. Editorial ledger entries (ED-XXX) for each major component
4. Patch register entries (PP-XXX) with vetting blocks
5. Integration patches drafted against existing canonical documents
6. Content authoring scope agreed
7. Stage-1 simulation pass demonstrating viable basic behavior

## Implementation Stages (per §9 of doc 12)

1. Per-NPC inner state + three-dimension armature + Event Impact Matrix
2. Add Procedure E (off-screen interactions, Gossip)
3. Add Settlement and Faction Meta-Armatures
4. Add Domain Action proposal mechanism
5. Add long-run mechanisms (Memory salience floors, calcification, Project legacy)

Profile at each stage. Each stage produces a working partial system that can be tested independently.

## Items Deferred Until Simulation

- Computational budget profiling (estimates throughout — never measured)
- Concern template within-Conviction variation calibration
- Ambient interaction rate validation (60% with dampening)
- Knowledge propagation latency validation
- Player experience validation (will players notice Gossip? Will Witness Mode feel dramatic?)

## Session Summary

A 12-document arc traversing: gap audit → historical research → directionality revision → philosophical reframe → mechanical specification → 3 iterations of test/patch/critique → canonical vetting → architectural completion (Event Matrix + meta-armatures) → streamlining pass → 12 stress tests with 16 patches → top-down audit → consolidated development specification.

**Primary deliverable:** `12_development_specification.md` — single source of truth, ready for re-vetting and (after decisions) promotion.

**Design knowledge encoded across the journey:** the iterative pattern (test → audit → patch → critique → integrate) preserved in 06, 09, 10, 11 demonstrates a methodology applicable to future Class A subsystem proposals.
