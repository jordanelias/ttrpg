# Ripple register — cross-scale propagation map (observatory L3, v1)

QUALITATIVE complement to the vector audit's quantized map. Composed from structure_audit L2 (module wiring) + formula_audit L1 (derivation DAG), bridged across scales. MEASURES, never gates. Provenance-tagged — a `⚠notional` hop runs through a doc:null / [ASSUMPTION]-grade contract module.

**Nodes:** 46 (27 module · 19 quantity)  ·  **Edges:** 135 (43 notional)
**Edge types:** emits_consumes=90, derives=15, produces=15, reads=15  (`produces`/`reads` are COARSE module-granularity bridges — opt-in, excluded from the default precise ripple).

## What / How / Why
- **WHAT** a node is: its `kind` (module = mechanic/subsystem; quantity = value/derived stat/Key output).
- **HOW** two nodes couple: the edge `type` — `emits_consumes` (a Key flows module→module), `derives` (a value is computed from another), `produces`/`reads` (a module writes/consumes a value).
- **WHY** the coupling exists: the edge `provenance` — the Key type, formula, or contract source that established it (never synthesized; read from module_contracts / descriptor_registry).

## Highest change-impact nodes (by precise degree — a change here ripples furthest)
- **npc_behavior** (module) — downstream 6 · upstream 31
- **faction_state** (module) — downstream 3 · upstream 28
- **scene_slate** (module) — downstream 16 · upstream 0
- **piety_track** (module) — downstream 2 · upstream 13
- **domain_actions** (module) — downstream 12 · upstream 0
- **social_contest** (module) — downstream 11 · upstream 1
- **faction_politics** (module) — downstream 8 · upstream 0
- **peninsular_strain** (module) — downstream 7 · upstream 0
- **fieldwork_knots** (module) — downstream 6 · upstream 0
- **game_director** (module) — downstream 6 · upstream 0
- **settlement_layer** (module) — downstream 2 · upstream 3
- **npc_memory** (module) — downstream 0 · upstream 4

### Worked ripple — `module:npc_behavior` (depth ≤2)
**Downstream (a change here affects):**
- npc_behavior --emits_consumes[Key::scene.gossip]--> npc_memory (module) ⚠notional
- npc_behavior --emits_consumes[Key::scene.witness]--> piety_track (module)
- npc_behavior --emits_consumes[Key::state.opinion_revised]--> social_contest (module)
- piety_track --emits_consumes[Key::state.scar_acquired]--> faction_state (module)
**Upstream (this is built from):**
- npc_behavior --emits_consumes[Key::da.antinomian_action]--> domain_actions (module) ⚠notional
- npc_behavior --emits_consumes[Key::env.peninsular_strain_shock]--> peninsular_strain (module)
- npc_behavior --emits_consumes[Key::mechanical.cascade_resolution]--> faction_state (module)
- npc_behavior --emits_consumes[Key::meta.knot_formed]--> fieldwork_knots (module)
- npc_behavior --emits_consumes[Key::meta.miraculous_event]--> miraculous_event (module)
- npc_behavior --emits_consumes[Key::meta.thread_woven]--> threadwork (module)
- npc_behavior --emits_consumes[Key::scene.battle_concluded]--> mass_battle (module)
- npc_behavior --emits_consumes[Key::scene.contest_resolved]--> social_contest (module)
- npc_behavior --emits_consumes[Key::scene.dialogue]--> scene_slate (module) ⚠notional
- npc_behavior --emits_consumes[Key::scene.investigation_resolved]--> faction_politics (module)
- npc_behavior --emits_consumes[Key::state.scar_acquired]--> piety_track (module)
- faction_state --emits_consumes[Key::env.disaster]--> scenario_authoring (module) ⚠notional

## Structural leads
- **Pure sources** (produce, never derived — candidate primitives/inputs): 21
  W_s, attr.body.endurance, attr.body.strength, attr.mind.will, cumulative_damage, domain_actions, engine_clock, faction Mandate, faction_politics, fieldwork_knots, game_director, mass_battle, miraculous_event, peninsular_strain, scenario_authoring, scene_slate, set.defense, set.order, set.prosperity, terr.fort_level, threadwork
- **Pure sinks** (consumed by nothing — candidate terminal outputs or dead ends): 12
  Garrison Strength, Health, Local Economy, Public Order, audit, faction Mandate (cross-module → faction_state), faction Treasury income (cross-module → faction_state), npc_memory, personal_combat, province Accord, scene_timer, settlement_economy
- **Isolated** (in the contracts but wired to nothing): 6
  articulation_layer, campaign_architecture, ci_political, clock_registry, territorial_piety, victory

_Leads, not verdicts — pure sinks/sources are often correct by design (terminal Keys, primitive inputs); triage against the contract before acting._