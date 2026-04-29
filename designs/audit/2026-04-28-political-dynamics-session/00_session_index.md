<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration index, not canonical -->

# Political Dynamics Design Session — 2026-04-28

## Session Token
`d964fd13158349fa`

## Scope
Comprehensive examination of how interpersonal relationships operate in Valoria and how those dynamics radiate through character advancement, arcs, settlements, governance, and faction politics. Originated from inspiration document `faction_dynamics_audit_v2.md`.

## Documents in Order

| # | File | Stage | Status |
|---|---|---|---|
| 01 | `01_interpersonal_audit.md` | Gap audit identifying 8 structural gaps | Foundational; still valid |
| 02 | `02_initial_proposals_with_historical_precedents.md` | First-pass proposals with Renaissance/medieval/Ottoman/Byzantine/Habsburg precedents | Superseded by later iterations; historical research preserved |
| 03 | `03_revision_directionality_emergence.md` | Structural revision addressing vertical-only chains and pattern-matching | Superseded by autonomous actor reframing |
| 04 | `04_autonomous_actors_philosophical_reframe.md` | Reframing NPCs as persons with inner lives | Conceptual pivot; informs all subsequent work |
| 05 | `05_groundup_mechanical_proposal.md` | First full mechanical specification | Superseded by iterative version |
| 06 | `06_iterative_test_audit_patch_critique.md` | Three iterations of test → audit → patch → critique | **Primary proposal document** |
| 07 | `07_armature_system_vetting.md` | Full vetting per throughlines_meta.md framework | PASSES; vetting block included |
| 08 | `08_event_matrix_meta_armatures.md` | Event Impact Matrix + multi-scale meta-armatures + Domain Action integration | Architectural completion of the political loop |

## Key Outputs

**The Armature System** — replaces the original 630-template library with weighted interpretive armatures derived from existing NPC characteristics (Conviction, Personality, active Projects, Scar count). NPCs interpret events through their armatures, generating Concerns that drive autonomous behavior.

**Three-Scale Meta-Armatures** — NPCs, settlements, and factions all interpret events at their own scale. Faction Meta-Armature is a Standing-weighted aggregate of inner-circle armatures + institutional inertia + ethical framework anchor. Settlement Meta-Armature is governor + Passive NPCs + institutional character + population baseline.

**Event Impact Matrix** — computed once per event, consumed by all armatures interpreting the event. Reduces redundant per-NPC computation while enriching armature input.

**Domain Action Integration** — Domain Actions are both event-sources (interpreted by armatures across scales) and outputs of armature-driven Projects (proposed by inner-circle NPCs, evaluated by Faction Meta-Armature, modified by armature-induced support/opposition).

## Canonical Vetting Block (for future register entry)

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

1. **Personality dimension calibration** — 4 dimensions × ~35 Active NPCs = ~140 values
2. **Conviction → armature weight mappings** — 7 Convictions × 4 dimensions × ~5 options = ~140 weights (one-time, shared)
3. **Event dimension profiles** — ~30 event types × ~3 active dimensions × ~3 options = ~270 entries (one-time, shared)
4. **Sentence frame templates** — ~20 frames covering Agency × Mechanism × Intent
5. **Wrong-Belief Investigation interaction** — Option A (forgiving) vs Option B (harsh, recommended per Ω-d)
6. **Conviction × Event-type symbolic resonance table** — 210 entries (single-cell ratings)
7. **Settlement institutional character bias profiles** — 6 entries (one per settlement type)
8. **Domain Action sponsor mapping** — ~30 entries (which inner-circle NPC roles propose which Domain Action types per faction)

Total content authoring obligation: ~620 entries before implementation.

## Items Deferred Until Simulation

1. Computational budget profiling
2. Concern template within-Conviction variation calibration
3. Ambient interaction rate validation (60% with dampening)
4. Knowledge propagation latency validation

## Next Steps (when promoted from PROVISIONAL)

1. Jordan decisions on outstanding items above
2. Editorial ledger entries (ED-XXX) for each major component
3. Patch register entries (PP-XXX) with full vetting blocks
4. Integration with existing systems (`designs/npcs/npc_behavior_v30.md`, `designs/architecture/player_agency_v30.md`, `designs/territory/settlement_layer_v30.md`)
5. Simulation design pass before implementation
