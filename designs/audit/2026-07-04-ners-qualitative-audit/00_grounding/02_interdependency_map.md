# Grounding 2 — Cross-subsystem interdependency map

## Status: PROPOSED (audit grounding — Jordan review)
_Explorer output, 2026-07-04 planning phase (sonnet lane). Verified against the working tree at
commit `cb227cf`._

## (a) Strongest coupling edges (flattened)

1. **Faction ↔ Settlement (densest edge, damped both ways).** `Mandate =
   clamp(round(7T/(T+6)),0,7)`, T over controlled settlements' `q_s=0.5L+0.5PS` size-weighted;
   Mandate drifts settlement L/PS back ±1/season (mean-reverting). `settlement_layer_v30.md`
   §1.8; mirrored in `module_contracts.yaml` (settlement_layer `loops`/`derivations`). LPS-2e
   ruling (Jordan 2026-05-30) superseded faction-level L/PS.
2. **Personal/Scene → Faction via Domain Echo (universal bottom-up channel).**
   `scale_transitions_v30.md` §5 (±1/±2 per degree, cap 1 Echo/scene/faction), §5.4
   Debate→Mandate, §5.5 Accord targets settlements, §5.6 Thread Domain Echo. ⚠️ `scene.combat_resolved`
   is **declared-but-unconsumed**: registry says npc_behavior/faction_layer/articulation consume
   it; their own `consumes:` lists don't (module_contracts personal_combat gap_notes).
3. **Thread → Faction (§3.5: the thread op IS the Domain Action) and Thread → Mass Battle**
   (§3.6: scale-tiered Coherence costs, fires in mass battle Phase 4/6; `threadwork_v30.md`
   §2.4/§A.10, ST-TW-05).
4. **Mass Battle ↔ Personal Combat (General Duel §3.7; scene→mass one-turn bonuses §3.8).**
5. **Fieldwork ↔ everything (§3.9, 9 named handoffs)** — highest fan-out single section.
6. **Social Contest ↔ NPC behavior 2-cycle** (`scene.contest_resolved`/`state.opinion_revised`);
   social side dampers specified; **npc_behavior side "dampers unconfirmed [OPEN — Jordan]"**.
7. **faction_state self-loop** (drift_coef 0.6/season, crisis bypass at scars≥3);
   **faction_politics/faction_state module boundary "[OPEN — Jordan]"** (faction_politics is
   doc:null yet emits coup/succession/standing Keys both consume).
8. **Peninsular Strain → settlement/faction env cascade** (`env.disaster`, IP/Turmoil gates
   `g_ip100/85/80` → Occupation Phase read by `victory_v30.md` §5.2).
9. **Settlement location ⇄ mass battle** (`settlement_adjacency_v30.md`: all mass battles occur
   at settlements; Fort Level → Defender Ob; Part E consequences settlement-scoped).
10. **Dice/resolution substrate** (`params/core.md` d+σ, "system-agnostic by construction",
    line ~78) under every resolver.
11. **Articulation = universal sink** (`articulation_layer_v30.md` §5/§9: consumes `*`, emits
    nothing back into mechanics).

## (b) Module-contract state (references/module_contracts.yaml, 27 modules)

- **doc:null (10):** npc_memory, scene_slate, game_director, scene_timer, audit,
  **domain_actions**, settlement_economy, **engine_clock**, faction_politics,
  scenario_authoring. domain_actions + engine_clock are central connective modules;
  engine_clock's candidate home is `propagation_spec_v1.md` §O.2 pending ED-1051.
- **[ASSUMPTION]-grade resolvers (11):** faction_state, npc_behavior, npc_memory, piety_track,
  territorial_piety, domain_actions, peninsular_strain, settlement_economy, faction_politics,
  miraculous_event, scenario_authoring. Biggest bloc = the deterministic-accounting faction
  cluster.
- **Orphan/thin (6):** ci_political (CANONICAL doc, zero Key integration), territorial_piety
  (same; name-collides with piety_track), clock_registry (pure manifest), victory (reader-only;
  gated on **MS, an unowned clock**), settlement_economy (phantom — "RECOMMEND RETIRE"),
  campaign_architecture (stub).

## (c) Scale-transition spine

`designs/architecture/scale_transitions_v30.md` (CANONICAL): §1 three modes → §2 scale table
(Object/Personal/Relational/Territorial/Structural) → §3 eight handoff rules (3.1
Personal→Thread … 3.8 Scene→Mass) + §3.9 Fieldwork↔All → §4 zoom protocol ("Where Were You?"
retrospective) → §5 Domain Echo → §6 mode transitions → §7 Sufficient Scope → **§12
all-directions Key delivery (J-1: direction emergent from `targets[]`/`scale_signature`)**, with
§12.4 naming 4 known down-seam gaps: `domain_actions→{npc_behavior,piety_track,settlement_economy}`,
`faction_politics→npc_behavior`, `peninsular_strain→{npc_behavior,settlement_economy,settlement_layer}`,
`scenario_authoring→settlement_layer`.

## (d) Per-subsystem gist

- **Personal combat** (`designs/scene/combat_engine_v1/`): strike→wound→felled; out-edge
  `scene.combat_resolved` (declared-unconsumed); in-edge General Duel §3.7.
- **Mass battle**: muster/march/battle phases; edges to faction (Military/Stability), settlement
  (location/siege), thread (§3.6), personal (§3.7), scene (§3.8).
- **Social contest** (rebuild in flight, `sim/personal/contest/`): persuasion-track clock; NPC
  2-cycle; Domain Echo §5.4.
- **Faction/political**: stat economy + Mandate loop; consumer of Domain Echo; faction_politics
  boundary open.
- **Settlement/territory**: stat/derived-value engine + LPS-2e Mandate math; env inputs from
  strain; battle location.
- **Threadwork**: Coherence/Fatigue; direct §3.5/§3.6 edges; highest fan-out per size.
- **Architecture** (key_substrate/holonic/propagation): the delivery mechanism every edge rides;
  propagation_spec_v1 is partial engine_clock home.
- **Articulation**: narrative surfacing sink; zero mechanical out-edges.
- **NPCs**: concern/opinion/project/arc engine; dense faction + social edges; npc_memory writes.
- **Dice/resolution**: foundational substrate for all resolvers.
