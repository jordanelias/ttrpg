# LENS: cohesion_interdependency (BARRIER LENS)

## Verdict
The corpus has ONE delivery idiom (Key emit/observe) but the state riding it is not one language,
and a large fraction of its richest cross-scale edges are declared but not delivered. Consequence
computes and then dies in transit at two structural seams — emitter-side (strategic Keys don't
populate sub-scale `targets[]`) and consumer-side (registry names consumers whose own `consumes`
lists omit the type) — and finally at the terminal renderer, which subscribes to `*` but fires no
trigger for the richest collisions (Thread, battle_concluded). The Key pipe is uniform; the fluid
is not.

## Flattened declared-vs-implemented edge table (from all 12 dossiers)

### DIVERGENT — declared consumer does not actually consume (consequence reaches the bus, dies there)
- scene.combat_resolved -> npc_behavior/faction_layer/articulation. CONFIRMED module_contracts.yaml
  L844 gap_note A4: "declared with consuming_systems [npc_behavior, faction_layer, articulation]...
  those modules' contract `consumes` lists do not yet name them." Also L808/L823. Flagship break.
- social_contest <-> npc_behavior 2-cycle: social side asserts BOUNDED w/ numeric bounds;
  npc_behavior block asserts dampers unconfirmed [OPEN-Jordan] (module_contracts ~L153 vs ~L442).
- threadwork -> settlement_layer §4.4 (ED-675, divergent); threadwork -> articulation (no
  consuming Key/trigger); threadwork -> combat_engine_v1 (only superseded combat_v30 §10).
- settlement -> territory_temperaments: zero mechanical consumption of alpha/beta anywhere.
- mechanics_index/canonical_sources <-> sim: mass_battle ratifications never round-trip back.

### DECLARED-ONLY — edge stated, mechanism unbuilt/gated (consequence never leaves the emitter)
- domain_actions -> {npc_behavior, piety_track, settlement_economy} §12.4 down-seams. CONFIRMED
  scale_transitions_v30 L331-332: consume intent registry-canonical, "strategic emitters do not yet
  populate sub-scale targets." domain_actions itself doc:null, consumes:[] (module_contracts L470-475).
- faction_politics -> npc_behavior; peninsular_strain -> {npc_behavior, settlement_economy,
  settlement_layer}; scenario_authoring -> settlement_layer (same §12.4 block).
- social_contest -> faction (Domain Echo/Mandate, faction.py Stage-4); -> faction_politics/
  domain_actions (Obligations; faction_politics doc:null); fieldwork -> social_contest (no import).
- personal/scene -> faction Domain Echo (faction dossier declared-only); npc_behavior -> npc_memory
  (doc:null [ASSUMPTION] sink); npc_behavior -> faction Cascade (PP-686); victory era-transitions ->
  articulation (UNKEYED, ED-1006); governance_play_redesign -> settlement (orphaned proposal);
  Key -> Godot Resource (1/27 ported).

### IMPLEMENTED (the working cohesion) — mostly bottom-up + intra-provincial
- faction <-> settlement Mandate<->L/PS loop (both directions, sim-bounded); mass_battle -> faction/
  settlement (Part D/E); threadwork -> faction_state Domain Echo (ED-673); threadwork <-> knots;
  Thread §A.10 -> mass battle; General Duel §3.7 in-edge; settlement -> victory Accord gate.

## Where consequence dies in transit — two structural death-points + a terminal sink
1. EMITTER-SIDE (top-down blind): strategic Keys resolve at the faction-stat ledger; `targets[]`
   left sparse, so npc/settlement observers never see them. §12.4 names 8 seams / 15 type-edges.
2. CONSUMER-SIDE (lateral/up unreached): registry lists consumers; their contract `consumes` omits
   the type. scene.combat_resolved is the canonical instance — an entire physics-rich subsystem
   whose output escapes to nothing (and the payload is health-bar-shaped anyway: double bottleneck).
3. TERMINAL SINK: articulation consumes `*` (module_contracts L768) so it RECEIVES thread/combat
   Keys — but its §3.1 10-trigger ruleset fires no cut scene for Thread, battle_concluded, or
   investigation_resolved. The renderer of emergence is blind to the flagship emergent moments.

## Q-smooth corpus verdict: one pipe, many dialects
Does state cross boundaries in one idiom? NO, at the vocabulary layer, even though YES at the
transport layer. Evidence: (a) same world-track dual-named MS vs RS across live-canonical docs
(threadwork); (b) same victory-track 'Political Stability' (GD-1 canon) vs 'Turmoil' (every design
doc); (c) 3 Key types declare permanence/time_horizon outside the substrate's own §2.2 enum
(architecture dossier); (d) a single 2-cycle whose two contract blocks disagree on resolution;
(e) faction_politics doc:null yet emits coup/succession Keys both it and faction_state consume.
The Key substrate is a genuine Q-smooth win in the abstract; the naming/enum/wiring drift on top of
it is a corpus-wide Q-smooth failure that no shape-layer instrument currently gates.

## doc:null / [ASSUMPTION] / orphan set — North-Star cost (NOT a re-listing; KNOWN via ED-1051)
The 10 doc:null + 11 [ASSUMPTION] modules are not evenly distributed debt — they cluster on the
CONNECTIVE tissue. domain_actions (player's primary strategic verb) and engine_clock (temporal
spine) are both doc:null AND the source of most §12.4 down-seams: the two modules most load-bearing
for cross-scale consequence are the least-specified. npc_memory doc:null is the sink npc_behavior
emits into, so P-09 memory has no mechanical surface. Cost: the collision engine's inputs are
authored (rich faction/thread/combat state) but its wiring is [ASSUMPTION]-grade, so emergent
narrative depends on edges that are declarations, not implementations. Inert state + untraceable
consequence is the direct North-Star tax.

## 5 worst cohesion breaks, ranked by North-Star impact
1. scene.combat_resolved divergent + thin payload — flagship personal->strategic output both
   unconsumed and health-bar-shaped. (P1)
2. domain_actions §12.4 down-seams unpopulated + doc:null — headline strategic choice never reaches
   sub-scale. (P1)
3. Threadwork's two highest-value sinks dead (combat ED-911 + articulation) — P-14 spine's richest
   collisions can't surface. (P1)
4. Vocabulary non-uniformity (MS/RS, Turmoil/Political-Stability, enum-fork, self-contradicting
   2-cycle contract) — state does not cross in one idiom. (P2)
5. Shape-layer drift (mechanics_index stale, no sim back-propagation) — the currency map a session
   bootstraps the interdependency picture from is false where the corpus is most alive. (P2)
