# Lens: throughlines_tree — working notes

## Sources read
- references/throughlines_meta.md (SKELETON: Μ 4 modes, М 11 meta-patterns, T-tag summary)
- references/throughlines_meta_infill.md (rationale, §3.1 full T→М tag table, М-7..М-11 specs)
- references/throughlines_complete.md (41 concrete throughlines, T-01..T-41, impl-status column)
- charter + 03_threadwork_surface.md
- 12 dossiers (leads only)

## The map: Μ modes → М patterns → T throughlines → audited subsystems

### Μ causal modes (4)
- Μ-α pressure-as-engagement-driver
- Μ-β autonomous-agent-composition
- Μ-γ substrate-ontology
- Μ-δ cross-scale-consequence

### М meta-patterns (11) and their parent Μ
М-1 pressure continuous (α) · М-2 geography holds pressure (α,δ) · М-3 substrate grounds all (γ) ·
М-4 institutions stake substrate-postures (γ) · М-5 scales connect through substrate (δ) ·
М-6 choice is forced (α) · М-7..М-11 phenomenology/borrowings extensions (γ/α/β; on T-31..T-41).

## TRUNK — meta-patterns load-bearing across MOST audited subsystems

1. **Μ-δ / М-5 "scales connect through substrate"** — the collision-engine spine. Every dossier
   carries a cross-scale edge: combat→faction Domain Echo; contest→Obligations/Mandate;
   mass_battle→settlement/faction (Part D/E); settlement↔faction Mandate (LPS-2e); threadwork→Domain
   Echo (ED-673); victory GD-1 aggregate; architecture_spine IS the Key emit/observe channel
   (scale_transitions §5/§7/§12). Trunk, but half-delivered (see finding xscale-trunk).

2. **Μ-α / М-1 pressure + М-6 forced choice** — clocks and scarcity: MS/RS decay (T-04),
   TC (T-05), IP (T-06), Turmoil (T-07), Campaign Supply, Coherence. Carried by mass_battle,
   faction_political, settlement, victory_strategic, threadwork, peninsular_strain.

3. **Μ-γ / М-3 substrate grounds all (P-14 inseparability)** — T-01 declares "Systems: ALL." This
   is the trunk with the most severed limbs (see finding substrate-severed). The audit's headline.

4. **Μ-β autonomous-agent-composition** — the autonomous world (T-23/24/25, faction accounting,
   priority trees, clocks). Carried by npc_behavior, faction_political, victory. Undermined at the
   letter by faction_layer_v30 §5.8 ("GM controls NPC faction votes") — a Μ-β/Ω-c contradiction.

## KEY BRANCHES — throughlines carrying one major limb

- **М-4 institutions stake substrate-postures** (T-08/09/11/15a/b/c, T-21, T-27, T-39) →
  carries **faction_political + npc_behavior** (6 faction sheets, priority trees, Convictions).
  Limb: institutions.
- **М-2 geography holds pressure** (T-18 Radiation Gradient, T-19 Southernmost) →
  carries **settlement_territory + mass_battle terrain (§A.9) + calamity_radiation**. Limb: geography.
- **Personal-transformation arc cluster** (T-12 Practitioner, T-13 Certainty, T-16 Knot, T-17
  Companion; Ω-b, М-6) → carries **threadwork + npc_behavior/conviction_track**. Limb: character transformation.
- **Strategic-clock cluster** (T-04/05/06/07, T-20 Two Contests, T-25 Generational) →
  carries **victory_strategic + peninsular_strain + faction**. Limb: strategic pressure.
- **Emergent-narrative generation** (T-23 NPC Arc Emergence, T-24 Convergence-as-Crisis) →
  produced by **npc_behavior + faction**, rendered by **articulation**. Limb: the "emergent
  narrative engine" itself — and its rendering terminus is Thread/battle/era-blind.

## ORPHAN THROUGHLINES — declared in registry, no ratified subsystem head (grep-verified)

- **T-31, T-33, T-34, T-35, T-37, T-38, T-39, T-40** (the entire М-7..М-11 phenomenology tier:
  Reflexive Suspension, TS Developmental/Taxonomic receptive-capacity arc, Distal Interoception via
  Knot Tethers, Unified Uncanny, Stimulus-Resistance Triplet, Real-as-Amplitude, Textual-Mode
  Typology). throughlines_complete lists each "Implementation status: Proposed. Wave N workplan."
  grep for their signature vocabulary ("reflexive suspension", "distal interoception",
  "seismographic", "receptive capacity", "Textual Mode") hits ONLY designs/audit/* synthesis +
  workplan docs — **not threadwork_v30.md, not any subsystem head.** An entire meta-throughline tier
  is registry-resident and mechanically absent.
- **T-02 Rendering=Consciousness-Performed, T-30 Information Asymmetry** ("the gap IS the gameplay"):
  home is designs/scene/investigation_systems_v30.md, which **no dossier lane audited** — a whole
  epistemic/perception limb sits outside the audited surface.
- **T-26/T-27/T-28/T-29** (Recursion, Effects-Real-Explanation-Wrong, Confrontation/Leap/Operation
  Triad, Baralta Prophylaxis): "design complete, implementation pending"; partial prose homes in
  world/npc/baralta/faction docs ("prophylaxis" appears in baralta_v30, faction_canon), no mechanical head.

## TRUNKLESS MECHANICS — mechanics serving no throughline (a "why" gap)

- **Territory temperament α/β** (territory_temperaments_v30) — zero mechanical consumption anywhere
  (settlement dossier + grep: no consumer). Mechanic without a throughline.
- **Institutional Consolidation passive recovery** (faction_layer_v30 §1.3) — Stability+1/Accord+1
  for a null season; serves no throughline, actively anti-М-1 (rest state).
- **Recall +2D near-costless citation** (social_contest_v30 §4 Step 3) — no throughline, anti-М-6
  (cost-hidden checkbox).
- **Meta-lanes trunkless by nature (not defects):** registers_graphs (mechanics_index/DECISIONS/
  coverage_matrix) and recent_infra steering docs — shape/process artifacts, no player throughline;
  correct that they carry none, but they are stale exactly where the live trunks are most active.
- Note: Thread Exploitation Site faucet (settlement §4.9) is NOT trunkless — it serves T-21
  (thread-exploitation-sites tragedy-of-commons) but is implemented as a degenerate inert faucet.

## Organizing conclusion for the synthesis
The final report should be organized around the four trunks. The dominant cross-cutting story is
Μ-γ/М-3: the one meta-pattern declared universal (T-01 Systems:ALL, P-14 "every play mode") is the
most-severed — amputated at combat_engine_v1 (ED-911), articulation, faction_behavior math, and 7/9
npc faction trees. Mirror-image defect: the М-7..М-11 phenomenology tier is a full throughline limb
with NO mechanic (orphan), while several live mechanics carry no throughline (trunkless). The
cross-scale trunk (М-5) that carries emergent narrative is delivered bottom-up (Domain Echo) but not
top-down (§12.4 down-seams unpopulated, scene.combat_resolved unconsumed).
