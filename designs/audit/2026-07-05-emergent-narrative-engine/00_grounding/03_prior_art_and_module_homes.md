# Grounding 3 — Prior art, prior questions, and the candidate module homes

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
_Explorer output, 2026-07-05 planning phase (sonnet lane), verified against the working tree._

## (a) The question has been asked before — and partially answered

`designs/audit/2026-04-30-architecture-session/` docs 10–13:

- **Doc 10** (`10_emergent_arcs_engagement_NERS.md`): the PP-684/686/687 stack is "the strongest
  architectural foundation for emergent narrative the project has produced" (21/24 STRONG).
  Open flags: **causes[] population ~15%** (arcs stay shallow); legibility burden; authored-vs-
  emergent balance; §8.5 "what's NOT supported" (no single-character heroic arcs, no authored
  mystery/reveal arcs, no designed dramatic timing, no failure-of-the-world model).
- **Doc 11** (`11_story_vs_happenings_analysis.md`): without further work ~10-15% of playthroughs
  read as coherent story vs ~40-50% "smattering of happenings"; proposed protagonist frame +
  arc recognition (`meta.arc_detected`) + punctuation (`meta.arc_resolved`) + a
  scenario-authoring layer → ~85%. Recommended PP-688 arc detector / PP-689 chronicle / PP-690
  scenario authoring.
- **Doc 12** (`12_three_tier_articulation_reframe.md`): **Jordan explicitly rejected the
  real-time arc-detector FRAMING** ("real life doesn't tell you 'you are now in the Rising
  Action'") → the three-tier articulation reframe. **This veto is charter constraint C2.**
- **Doc 13**: significance-function weights + "present-moment + year-end omniscient
  retrospective" locked.
- **Resolution state**: three-tier articulation WAS canonized (articulation_layer_v30
  implements Tiers 1/2/3 + doc-13's significance form). But: its §3.1 ruleset is now
  known-incomplete (audit F-4 → ED-IN-0004); the Convergence Markers (T-24, "the game's
  emergent narrative engine") never got a mechanism (F-2 → ED-IN-0003); **PP-690
  scenario-authoring was never authored** (`scenario_authoring` doc:null — doc 11 §7.3 named it
  the home for "campaign skeletons with seed Keys and inflection-point Keys").
- **2026-05-08 immersion meta-audit** (uncaptured by docs 10-13): presentation is a design
  decision, not downstream; personal-scale surface should be 3-4 trackers; **texture between
  cut scenes** is where immersion lives or dies; mechanical vocabulary must not surface.

## (b) Relevant ED inventory (beyond the ratified E-series)

ED-412/ED-479 (resolved): arc-36–40 convergence-season compression formula (GM guidance).
ED-609 (open): Torben Beliefs/Conviction emergence needs formal spec. ED-681 (resolved, but its
render angle is ED-IN-0004's live gap): four authored Rendering-Crisis beats. ED-746/ED-761
(resolved): Scene Slate Step-4 keywords + mandatory-overflow ordering incl. **Witness Mode**.
ED-935/936/937 (resolved): the Key-type registry cluster — ED-936 authored the articulation
§6.4 "already triggers Tier 2" claim under delegated [ASSUMPTION] authority (the F-4 root).
ED-1009 (open): whole-graph module adjudication — `scene.dialogue`/`belief_revised`
multi-emitter attribution conflicts. No ED titled "narrative engine" exists — the E-series
(ED-IN-0003/0004) are the first tracked mechanism items.

## (c) The doc:null narrative-direction module cluster (`references/module_contracts.yaml`)

- **`game_director`** (L368-385): doc:null, scales [scene], resolver `manifest` — "season-loop +
  zoom-stack orchestrator". Emits `mechanical.scene_entered/exited/skipped`; consumes nothing
  declared. Gap: home doc unlocated; scene_entered attribution conflict with scene_slate.
- **`scene_slate`** (L342-366): doc:null, scales [scene], resolver `manifest` — "deterministic
  7-priority slate generation (settlement_layer §4.1; player_agency §4.2)". Emits
  `mechanical.scene_entered` (terminal:false, flagged) + `scene.combat_strike/dialogue/gift/
  insult/investigation_resolved/threat/witness`. Gap: standalone spec [GAP]; **ownership
  conflict with game_director marked [OPEN — Jordan]**.
- **`scenario_authoring`** (L744-760): doc:null, scales [peninsula], resolver `manifest` —
  "[ASSUMPTION] authoring-time event injection". Emits `env.crisis`/`env.disaster`. Gap:
  authoring-time vs runtime classification [OPEN — Jordan]; home doc [GAP]. = PP-690's never-
  authored home.
- **`npc_memory`** (L177-196): doc:null, resolver `state_reader` — Keys→memory store, queried by
  Procedures (doc-12 §2.3 bridge). Consumes gossip/interaction/concern/opinion Keys; emits
  nothing.
- **`scene_timer`** (L387-404): doc:null — observability sidecar OUTSIDE the Key log; not a
  gameplay resolver.

All five are `status: extracted` (registry-inferred, never authored). The scene-orchestration
layer that would host a narrative engine exists only as registry inference with two live
attribution conflicts.

## (d) How scene selection works today

`player_agency_v30.md §4` (canonical, 2026-04-17): per-season Personal Phase slate via a
deterministic 7-priority algorithm — Step 1 Mandatory Crisis (8-item override order, ED-761,
overflow → **Witness Mode**); Step 2b Thread-State scenes (ED-674, MS-band × proximity, max 1);
Step 3 Duty-aligned; Step 4 Conviction-aligned (ED-746 keywords+validator); Step 5 NPC
Outreach; Step 6 Territorial; Step 7 Ambient. §4.3: slate 4-9 entries vs **3-5 scene
actions/season** (the hard envelope). §7.6 "Emergent Arcs": Convictions as "player-authored arc
vectors" that "intersect with NPC arc pressures and clock pressures to produce emergent
narrative" — **aspirational prose, not a mechanism**. The registry-formal `scene_slate` module
that would run this at runtime has never been authored (see (c)).

## (e) Un-re-derived open items a new effort must inherit

1. The immersion audit's presentation-layer/texture questions (a).
2. PP-690 scenario-authoring / campaign skeletons (doc 11 §7.3) — still doc:null.
3. The `game_director`/`scene_slate` `mechanical.scene_entered` ownership conflict.
4. ~850KB of prior emergent-arc drafting unfiled in `tests/` (decision-queue item 25a) — a
   content asset for the bake, currently invisible.
5. causes[] ~15% population (doc 10) — the continuity substrate the chronicle/trails need.
6. ED-609, ED-1009 (above); ED-401–405 absent from the ledger (MISSING-10).
