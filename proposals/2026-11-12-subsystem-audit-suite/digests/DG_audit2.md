# Digest audit2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: the surviving audit corpus under `.audit/` (archived-not-canon; context and referents). For each file: what the audit found, how it found it, and whether the finding looks fixed, stale or live at the working tree (one grep where cheap). Entries in assignment order.

### .audit/2026-07-04-weapon-morphology-granularity/u9_adversarial_review_v1.md
- **What it is:** Adversarial review of the U9 ablation capstone for the six morphology levers (PC-lane critic node, 2026-07-23, subject ED-PC-0021 / PR #220).
- **Status:** none stated (header "Outcome": shipped K=0 survives, 3 corrections + 1 test-isolation defect). Reading: historical; its verdict was superseded by U10 (see capstone).
- **Bears on:** PC, DICE (ablation method).
- **Content that matters:**
  - Method = break the "sub-noise" reading: P1 (constant never reaches its site) and P2 (enabling state never occurs) are the two ways an ablation reads Δ≈0 for a reason unrelated to the lever being situational (:19-26).
  - Site-firing probe: every consumption site instrumented over a real `winrate` (n=200, seed 3, K=1.0); all six fire. Choke levers fire only in pole matchups (poleaxe/spear, grip up to 0.865) and are correctly silent for dagger/arming (:79-98).
  - Consumption sites listed (:61-68): `combat_systems.legibility:709/710`, `bind_sigma:760`, `facing_target:376`, `contact.grab_sigma:47`, `weapon_physics.phi_grip:247`; `CHOKE_THRUST_K` is a `weapon_physics` module global, not in cfg (:57).
  - Extreme-K sweep (n=500, 5 seeds): BIND_SPINE K=2.0 mean +5.3pp (strongest, all positive), FACING +2.4, GRAB +1.2, LEGIB +1.1 (matchup floor-compressed: arming loses ~94% to estoc), CHOKE_ACCURACY +0.3 (weakest), CHOKE_THRUST K=0.9 -2.1 (:119-126).
  - Test-isolation defect: `test_combat_choke.py::test_both_channels_live_not_dead` writes the module global `weapon_physics.CHOKE_THRUST_K` and resets it in `finally`, leaking 0.0 to later modules and masking the D2 gate `test_thrust_protection_grip_invariant` in a full-suite run; the D2 gate fails only in isolation (:156-164).
  - Tolerance correction: D2 gate is `phi>=0.9` (<=10% loss); the wired 25% floor (phi=0.75) would widen a ratified gate, not rebase a pin (:166-169).
- **Conflicts / stale:** Reports a result for constants at K=0; the working tree no longer has K=0 for at least `LEGIB_EDGELINE_K` (`modules/combat/config.py:55` = 0.04), consistent with U10 activation. The `workbench/` and `systems/combat/combat_engine_v1/` paths it cites have moved to `modules/combat/` (path claims `[UNVERIFIED]` beyond the config.py hit).
- **Open items:** The leaked-global test-hygiene follow-up (use monkeypatch/cfg override) was "flagged"; whether it was done is not verifiable from this file. `[UNVERIFIED]`

### .audit/2026-07-04-weapon-morphology-granularity/u9_capstone_v1.md
- **What it is:** U9 joint-recalibration capstone / ablation-gate verdict for six edge/choke/facing levers (PC implementation node, 2026-07-22, ED-PC-0021).
- **Status:** "SUPERSEDED by U10 (ED-PC-0022, 2026-07-23)"; original status RATIFIED PR #220 (:7-16). Reading: superseded/historical; the ablation and "winrate is the wrong instrument" analysis are said to stand as the basis of U10.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Six levers and homes: `LEGIB_EDGELINE_K`, `BIND_SPINE_K`, `GRAB_EDGE_K`, `CHOKE_ACCURACY_K`, `FACING_REGIME_K` (config) and `CHOKE_THRUST_K` (weapon_physics), each with a stated HEMA/physics claim (:32-41).
  - Instrument and gate: `workbench/balance.py` winrate matrix; noise floor about +-4pp at n 350-500; a lever clears only if |Δ|>=4pp same sign across seeds (:49-63).
  - Result: no lever clears even in its best-case matchup at n=500 (:80); the early "CHOKE_THRUST robustly live" reading was a seed artefact (:125-139).
  - Verdict: activate none, cut none, re-charter the gate: "winrate is the wrong instrument" for situational levers; activation should be scenario-specific micro-calibration (:170-197).
  - The held-back design call (admit a floored choke exception to the grip-invariant thrust D2 gate vs hold the principle) is now recorded as DISSOLVED by U10, which re-homed the cost to the control/legibility channel so D2 stays byte-identical (:7-13).
- **Conflicts / stale:** The "K=0 byte-identical" state is superseded; `modules/combat/config.py:55` has `LEGIB_EDGELINE_K=0.04`. Cited `u10_activation_v1.md` and `consolidation_v1.md` are not in this assignment `[UNVERIFIED]` for where they live now.
- **Open items:** None live; the needs_jordan item is declared dissolved.

### .audit/2026-07-05-emergent-narrative-engine/_workings_joined.md
- **What it is:** Verbatim join (tools/join_audit_workings.py, 43 fragments, 10,678 lines) of the working papers of the Emergent Narrative Engine design effort (25-agent workflow, lane IN, 2026-07-05): charter, groundings, three architectures, dossiers, judges, refutes (v1 and v2), five spec sections, synthesis, verifiers, churn amendments.
- **Status:** each fragment "SUPERSEDED (working record ... head RATIFIED as narrative_engine_design_v2_churn.md + v1-as-amended + spec/churn_amendments.md, ED-IN-0011)". Reading: historical process record; the substrate it targets (Keys, Domain Echo transport, `meta.*` Key types) is RETIRED (ED-IN-0232).
- **COVERAGE NOTE (honest):** read in full: lines 1-3984 (charter, groundings 01-03, README, arch A/B/C, critic, dossiers combinatorial/content/forecast/nlg/register/transport, draft_s1..s5 notes) and 10258-10678 (verify_register_roundtrip, churn_amendments). NOT read: 3985-10257 (judges x3, refute_* x5 + refute_v2_* x5, spec_sections s1-s5, synthesis) and 10455-10582 (verify_trace_accounting tail, verify_contract_coherence). `[SKIPPED: .audit/2026-07-05-emergent-narrative-engine/_workings_joined.md lines 3985-10257 and 10455-10582 — context budget; their conclusions are summarised in the draft_* notes and churn_amendments that were read]`.
- **Bears on:** WR (narrative), CORE (season loop, seams), CHAR (NPC variables), FI (trails/investigation), SC (precedent stores), PROCESS.
- **Content that matters:**
  - Charter C1-C7 (:43-60): authored templates only/no runtime LLM; no narratological surfacing (Jordan's doc-12 veto: no "Rising Action" labels); engine books venues, never owns resolution; closes ED-IN-0003/0004; no new progression currency; thread beats (ED-681's four Rendering-Crisis beats) must render; never railroads.
  - Grounding 01 (:240-278): T-23 NPC arc emergence is implemented (npc_behavior state machine + domain_echo), T-24 "Convergence as Crisis" is prose-only; no runtime module consumes ARC-IDs (`references/arcs/` is a data source nothing ingests).
  - Census correction (:1897-1917): arc register is 138 entries (clocks 7, threads 8, territory 29, factions 81, events 13), not "~110"; ~13 structural shapes collapse all 138. Key registry declared 44 / physical 48 / 43 articulation-relevant (:1747-1783). Live Key-instance space is order 10^3 per season (:1860). Faction count in corpus ranges 4-8 depending on doc (:1795).
  - Register formalizability (:3039-3326): about 45% compiles now, 40% needs a new field/Key, 15% GM-judgment-irreducible; blockers: no per-arc lifecycle field outside NPC arc state, Coup Counter STRUCK (ED-781) with no remap to the 4-stage Löwenritter Autonomy track, ARC-T04 "Southernmost Ritual" dangling and mis-cited to two unrelated ED-416 rows, Axis 9 has no clock home, PI missing from clock_registry.
  - Forecast tractability (:2433-2699): analytic layer for continuous clocks plus seeded ensemble for discrete branches is tractable; flags that faction AI action choice is stochastic (`faction_action.py:55`, `:159`) contrary to "deterministic per GD-2"; ~19 sim stubs; frozenset iteration (`ALL_PLAYABLE_15`) is a determinism hazard; `mc_v18.py:89` falls back to wall-clock seed.
  - Verifier finding F8 (:10375-10382): Torben Loyalty is 8->0 in register and sim_arc_01 but 0-7 start 3 in `clock_registry_v30.md:27`; under start-3 the traced multi-season escalation does not hold. Also F2/F3/F5 cross-section divergences in the ARC-S07 compile (:10330-10358).
  - churn_amendments (:10583-10676): v2 replaces s2's detector and salience economy with "actual + potential" discovery over a forecast ensemble and a "Light Function"; adds rules R-F1/R-F2/R-HB/R-CL/R-AI/R-RL and fixtures F1-F8.
- **Conflicts / stale:** Engine homes it claims (`game_director`, `scenario_authoring`, `scene_slate`) were `doc:null` module_contracts rows; whether `engine/season/` realises any of them `[UNVERIFIED]`. Dossier counts (stubs, 35 vs 37 settlements, 17 vs 15 territories) are July 2026 and likely moved.
- **Open items:** Fork 8 tension-curve ownership, ED-609 (Torben Conviction emergence), ED-1009 (multi-emitter attribution), Certainty-in-bake-key swing (350-450 vs 1,200-2,700 authored units, :2022-2028), ERA (Expressive Range Analysis) unbuilt as the anti-oatmeal gate (:2915).

### .audit/2026-07-05-emergent-narrative-engine/integration_with_ners_audit.md
- **What it is:** Crosswalk from the Emergent Narrative Engine design to the 2026-07-04 NERS audit findings (2026-07-05, lane IN).
- **Status:** "RATIFIED (Jordan, 2026-07-05, PR #78; ED-IN-0011 — companion to the v1+v2 design docs)". Reading: historical; the design it maps is Key-substrate based, and the Key substrate is RETIRED (ED-IN-0232).
- **Bears on:** WR, CORE, SE, FI, PROCESS.
- **Content that matters:**
  - Finding dispositions: F-2/ED-IN-0003 (no engine for Convergence Markers) "closed by design" via L2 detector, COLLISION A-J as edge-triggered typed predicates (:10); F-4/ED-IN-0004 (articulation trigger omissions) closed at Stage 0 (:11); F-1/ED-SE-0001 settlement governance "composes, not closed" (:12); F-3 playability bar honoured (:13).
  - Wire-it ranking: #2 (articulation render of thread beats) executed; #1/#3 combat/General-Duel thread interface remains ED-PC-0001 post-R3; #4-#10 (faction math, NPC trees, settlement verb, npc_memory P-09, insurgency->Gap, spine payload) inherit "the engine's Key surface" (:17).
  - Standing constraint C2: no "Rising Action" / arc-label surfacing, enforced by lint on fragments and lifecycle labels (:27).
  - Open arcs corpus defects carried: COLLISION-C blocked on ARC-T04, Coup-Counter-dependent markers blocked (:10).
  - Explicit non-goals: no combat thread interface, no rebalancing of seeded-sim win-share, no runtime LLM, no new progression currency (:39-43).
- **Conflicts / stale:** Everything keyed on the "Key surface" is retired (CLAUDE.md §0, ED-IN-0232); "closed by design" is not "executes" (§0.2). Not checked whether a detector exists in `engine/season/` `[UNVERIFIED]`.
- **Open items:** F-1 (settlement governance loop) and F-5/S-2 deferred to other lanes with no tracking visible here.

### .audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md
- **What it is:** Design spec + module contract for an "Arc-Vector Engine with a Subordinate Director" (6 layers L0-L5), 25-agent adversarial workflow (2026-07-05, lane IN).
- **Status:** "RATIFIED as amended by v2 (Jordan, 2026-07-05, PR #78; ED-IN-0011 — fork defaults adopted incl. fork 8 subtract-only)". Reading: historical design intent; prose, not mechanism; Key-based so partly retired.
- **Bears on:** WR, CORE, CHAR, FI.
- **Content that matters:**
  - Layers: L0 offline compile of arc register into frozen typed arc-vector corpus; L1 `game_director` vector store and lifecycle FSMs per season; L2 two-tier convergence detector (8 authored COLLISION conjunctions + cosine backbone) at Accounting boundary; L3 subordinate director rationing into 3-5 scene envelope (ceiling never floor, C7); L4 tie-graph casting into the 7-priority slate; L5 NLG realizer (:21-38).
  - Staging: Stage 0 render-gap close; Stage 1 compile gate (~45% compiles now, ~40% needs lifecycle field, ~15% declared non-firing); Stages 2-3 behind Gate-0/ED-1051 (:76-90).
  - Nine open forks incl. Coup-Counter remap onto Löwenritter Autonomy, ARC-T04 strike-or-author, 4-season +-0.40 cosine window, two new Key types, fork 8 director is subtract-only (reverses charter "owns the tension curve") (:101-126).
  - NOT-list: no heroic-arc guarantee, no authored mystery/reveal arcs, no designed dramatic timing, no failure-of-the-world model, no arc labels surfaced (:128-136).
  - Determinism rules: integer basis-point salience, content-addressed fragment selection, ordered `convergence_fired_set` (:94-99).
- **Conflicts / stale:** New Key types `meta.convergence_detected`, `meta.arc_state_changed` (:65) assume the retired Key substrate. Whether `game_director`/`scenario_authoring` exist as code: `[UNVERIFIED]`.
- **Open items:** Forks 1-9 (Torben Loyalty range 8->0 vs clock_registry 0-7 start 3 is a registered data conflict, :122-123) have no answer visible here.
