# Edge inventory — the seams under audit

## Status: RATIFIED (Jordan, 2026-07-05 — "Ratify all", with the report)
_Assembled by the Fable orchestrator from `references/module_contracts.yaml` (27-module contract
spine, schema-2), `designs/architecture/scale_transitions_v30.md` (§3 eight handoffs + §3.9
fieldwork table + §4 zoom + §5 Domain Echo family + §12 all-directions rule), the key-type
registry consumer matrix, and #77's grounding map
(`designs/audit/2026-07-04-ners-qualitative-audit/00_grounding/02_interdependency_map.md`).
Working tree at commit `28be79c`._

Gameplay subsystems in scope (tooling-only modules — scene_timer, audit, clock_registry —
excluded): personal combat · social contest · fieldwork/investigation + knots · threadwork ·
mass battle · domain actions · faction (faction_state + faction_politics) · settlement/territory
(+ settlement_economy phantom) · NPC behavior (+ npc_memory) · conviction/piety (personal
piety_track; territorial_piety + ci_political church cluster) · peninsular strain · victory/era ·
articulation (rendering) · scene slate / game_director / zoom protocol (mode bridge) ·
miraculous_event / scenario_authoring (injectors) · dice/resolution substrate (under every edge).

## Cluster A — scene-scale lateral seams
Fieldwork→Combat (F-TRANS-01) · Combat→Fieldwork (F-TRANS-09/12) · Fieldwork→Contest
(F-TRANS-10/11) · Contest→Fieldwork (F-TRANS-10/05) · Fieldwork→Thread (F-TRANS-07) ·
Personal→Thread (§3.1 Leap) · Thread↔Combat (ED-911 KNOWN) · Thread↔Contest ·
Combat↔Contest (mid-scene transitions) · investigation_systems_v30's own edge set (#77 GAP-1).

## Cluster B — bottom-up transport
Personal→Faction (§3.2) · Scene→Faction Domain Echo (§3.4/§5.1–5.3) + Sufficient Scope §7 (7
conditions) · Debate→Mandate (§5.4) · Accord Echo (§5.5) · Thread Echo (§5.6) · PC embedding (§9) ·
Fieldwork→BG Echo (§3.9) · scene.{contest,battle,investigation,combat}_resolved → faction/NPC
consumption.

## Cluster C — top-down transport
Mandatory Zoom-In §4.3.2 (8 rows) · overflow rule ("present but overwhelmed") · world-state
triggers §4.3.3 (5 rows) · "Where Were You?" §4.4 · Scene Opportunity Ob shifts §4.1 · §12.3/§12.4
down-seams (4 emitter families, KNOWN) · da.* → personal experience · succession/coup → player ·
env.disaster/crisis → scene.

## Cluster D — mass-battle seams
Thread→Mass (§3.6/A.10/A.7) · Mass→Personal General Duel (§3.7) · Scene→Mass one-turn bonuses
(§3.8) · Mass→Faction (battle_concluded) · Mass↔Settlement (adjacency, Fort→Ob, Part E) ·
Fieldwork↔Mass (suspend/freeze) · mandatory "Mass Battle at Settlement" zoom · Contested Figure
§11 · zoom in/out mid-battle (§4.1/§4.2) · aftermath/officer scene generation.

## Cluster E — strategic lattice
Mandate↔L/PS loop (§1.8 LPS-2e) · settlement→Treasury · domain_actions→faction_state (the
player's five strategic verbs; doc:null KNOWN) · faction_politics↔faction_state↔player
(standing/coup/succession; doc:null-vs-existing-doc check) · strain→faction/settlement (env.*) ·
IP gates→occupation→counterplay · victory/era transitions (unkeyed KNOWN) · church cluster
(CV/CI/TC ↔ ci_political cards/pool ↔ faction) · governance verb menu ↔ faction (F-1 seam only).

## Cluster F — NPC / personal fabric
Contest↔NPC 2-cycle (opinion_revised ↔ dialogue/contest_resolved; Procedure-D cadence) · ambient
fabric (interaction/gossip/witness) → player · npc_memory legibility · piety_track inbound
(da.*, witness, battle) + Scars 2/3 gates as experience · scar→faction/knot-crisis chain · knot
lifecycle (formed/ruptured/strain/decay; Bonds≥5) · companion arcs (§5 FSM + §4.3.2 + §7 modifier)
· Disposition as cross-system currency · belief_revised dual attribution (playability angle).

## Cluster G — rendering seam (edge → screen)
Per edge family: combat outcomes · battle conclusions · contest resolutions · investigation
findings · thread events (incl. ED-681 crisis beats) · faction accounting deltas · settlement
drift/revolt · era transitions · coup/succession/standing · knot + scar events · env shocks.
Verdicts: RENDERED-RICH / RENDERED-GENERIC (salience only) / UNRENDERED; plus why-traceability
(causes[] payload sufficiency) and the "Why?" diagnostic surface.

## Cluster I — mode bridge & temporal cadence
Mode boundaries (§1, §6.1–6.3 incl. empty stubs) · Zoom In/Out round-trip (§4.1/§4.2) · Coherence
across the bridge (§6.4/§6.5) · Hybrid thread timing (§10) · BG Survey↔TTRPG Discovery
(§3.9 rows 7–9, fieldwork_hybrid §9) · scene slate + budget (player_agency §4.2; settlement_layer
§4.1) · season/accounting cadence (accounting_sequence; engine_clock doc:null KNOWN; propagation
spec ordering flags) · BG params currency vs v40 heads (spot checks).

## Known-issue calibration (inherited from #77 — assess impact, never rediscover)
F-1 governance four-verb loop · F-2 convergence markers undetected · F-3 playability bar homeless ·
F-4 articulation trigger omissions · F-5 strain co-victory residue · S-1 register back-propagation ·
S-2 steering fragmentation · ED-911 combat thread absence · scene.combat_resolved
declared-unconsumed · §12.4 down-seams · doc:null ×10–11 (domain_actions, engine_clock …) · MS/RS
fork · ED-1010/1011 · seeded-sim degenerate win-share · Godot skeleton non-compilable.
