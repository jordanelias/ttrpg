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

### .audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md
- **What it is:** Informational review of how far social contest is wired to settlement management and faction actions (SC lane, cross-cutting FA/SE, 2026-07-08); method: canon-doc read + `sim/` code trace + research-lineage read.
- **Status:** "FILED (informational review) ... Advisory only"; its top recommendation (ED-SC-0002) said to be executed by the same commit. Reading: historical snapshot; code paths it cites (`sim/...`) no longer exist (`sim/` dissolved, CLAUDE.md §3), so the "thin interface" finding is stale as to files but the design gap it names is likely still the live question for engine/season/.
- **Bears on:** SC, FA, SE, CORE.
- **Content that matters:**
  - Verdict "thin": the only live contest path (Stability Crisis in `scene_dispatch.py`, parties derived from one faction's own stats `side_a=round(L)`, `side_b=round(7-Sta)`, proceeding `guild_arbitration`, all [SEED]) resolved through the kernel and then discarded its verdict (no `echo` block) (:89-109); `parliamentary_vote.py` was a complete tested mutating path (`adjust("L",...)` :115) never called by the campaign loop (:111-124).
  - Only 1 of 8 mandatory zoom-in triggers was evaluated (`evaluable={"Stability Crisis"}`); Settlement Revolt, Faction Leader Removal, Rank Advancement recognition were deferred though contest-shaped (:89-95, :232-243).
  - No settlement-scale contest exists; `governance_play_redesign_v1` verbs Hold Court / Treat / Bargain / Recall are all explicit asymmetric-§7 contests but unbuilt; the party-derivation bridge for settlement stats (Order/Legitimacy/Popular Support) is the missing piece (:146-169, :217-231).
  - Doctrine AU-1 ("faction stat has no setter"; writes terminate at settlement/territory cells or decaying national-event-modifier Keys) and AU-5 wiring contract name the same seam as a structural incompleteness, not a nicety (:195-215); open HIGH D.6 double-count risk between settlement stat_deltas and faction aggregate (:269-275).
  - Consensus (Type-3) proceeding is a gap: "by consensus" collapses to a Mandate-weighted sigma vote; `coalition_vote` pools N parties onto two poles; `wrapper.py` GAMES marks consensus STUB (:277-308).
  - Research lineage claim: the deliberation research (Venice, Florence, conciliarism, Putnam two-level games, liberum veto, sortition) is institutional/collective-body material imported DOWN into the personal-scale contest, so the faction/settlement interface is the design intent, with the engineering lagging (:327-476).
- **Conflicts / stale:** Says there is "no Mandate stat in code" (`Faction` has L/Sta/W/I/Mil) (:171-175) and that `domain_echo` output shape is the pre-inversion scalar-delta shape; both about the dissolved `sim/` model. ED-SC-0002 is now `resolved` in `registers/editorial_ledger_sc_archive.jsonl:2` though the report calls it Jordan's open P0 pick. `echo_transport.py`/Key substrate it relies on are RETIRED.
- **Open items:** ED-SC-0007 (Bout verdict to echo degree) and the settlement-scoped `_emergency_council_parties` analogue; whether `engine/season/` now routes any contest verdict into settlement state `[UNVERIFIED]` — an SC/SE/FA audit should test this by execution.

### .audit/2026-07-08-mass-battle-gauge-architecture-audit/01_wave1_synthesis.md
- **What it is:** Synthesis of 7 producer+critic investigations into why `tests/sim/gauge_mb.py` scored 7/20 under the live defaults (PER_CELL=1, POOL_QUALITY_MODEL=1, n=60) (MB lane, 2026-07-08).
- **Status:** none stated in-file. Reading: historical/diagnostic ("diagnostic, not curative", :209); many named defects may since be fixed or re-ruled.
- **Bears on:** MB, DICE.
- **Content that matters:**
  - Seven root causes: #1 footprint/`ncells` Lanchester-density artifact (two unreconciled cell-count generators; composed-army 133-200-troop subunits collapse to 1 cell, ~8x density ratio; reversal ablation flips H3 100%->0% and H10 0%->100%) (:24-39); #2 super-linear resolution, melee exponent p~3.2 under PER_CELL=1 vs Linear-Law target <=1.4, old p 1.65-2.5 measured on the wrong path because `lanchester_signature.py:24` hardcodes PER_CELL=0 (:41-50); #3 side-dependent Arrowhead asymmetry (100/0/0 on side A vs 43/43/13 on side B), root line untraced (:52-55); #4 `hold` stance never closes to range (R3 guaranteed 0-casualty draw) (:57-61); #5 `recalc_size` force-routes every subunit when aggregate floors (:63-66); #6 n=60 noise makes C3,H9 not real fails so true divergence ~11/20 (:68-71).
  - Refuted: morale/rout as independent driver (no-op `rout_resolution` still 100/0), `MORALE_SIBLING_PULL` as H4 cause, post-rout pursuit unreachable in gauge (:83-87).
  - Per-cell QUALITY granularity is provably inert for all 20 rows; cell COUNT/density is the dominant bug (:160-170). Dead constants: `MORALE_EROSION_DAMP`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR` never consumed; `MORALE_PHASE_CAP` shadowed by hardcoded 3.0 at `core/state.py:60` (:78).
  - Five Jordan rulings requested: DG-A resolution architecture/exponent, DG-B canonical cell-count generator, DG-C morale floor of 1 while general present, DG-D cavalry vs infantry envelopment, DG-E per-cell scope + two stamina systems (:189-201).
  - Warning that pass count is not monotonic: fixing #1 or #2 alone may knock C4/C7 out of band (:222).
- **Conflicts / stale:** Cites `tests/sim/gauge_mb.py` (still exists), `core/attrition.py`, `units.py:1603-1611`; grep shows `_lanchester_strength`/`recalc_size` still present in `modules/mass_battle/core/attrition.py` and `hierarchy/units.py`, so some defects may be live. Whether DG-A..E were ruled: see later MB-lane docs in this assignment (wave2, README); `[UNVERIFIED]` otherwise.
- **Open items:** Trace the Arrowhead A/B asymmetry; ablate H7/H8; confirm `recalc_size` guard rescues H4/H5; decompose H2 edge vs amplifier (:203-209).

### .audit/2026-07-08-mass-battle-gauge-architecture-audit/02_wave2_synthesis.md
- **What it is:** Wave-2 synthesis (movement/pathing, stances/tactics/orders, reach/targeting, ranged/volley) feeding RC-5; includes a new probe by the synthesizer (MB lane, 2026-07-08). Begins mid-conversation ("I have what I need").
- **Status:** none stated. Reading: historical diagnostic, merged into README.md (third-level synthesis); numbering is wave-local (DG-6a..6f), final numbering is in README.
- **Bears on:** MB, DICE, CHAR (troop-type grounding of behaviour).
- **Content that matters:**
  - R1 (ranged side wins 65% vs band 0-30) is a harness bug: ranged side built `troop_type='infantry'` (4/5/6) not archers (3/3/3); archers flips R1 to 0% (:18, :59).
  - R3 (100% draw) is hold + out-of-range deployment (both hold, 19 rows apart vs `VOLLEY_MAX_RANGE=8`); `kite` fixes it only with disc-5 stats; with correct disc-3 archers `_node_advance` computes `floor(0.7)=0` and re-freezes (probe table :38-51). Live `_node_advance` lacked the legacy `_speed_accum` fractional accumulator (:49).
  - Troop type grounds STATS not BEHAVIOUR: `ROLE_SPEC`/`role_allowed` are 0% exercised by the 20-row battery, ~11-12 of ~15 instruction strings are inert (byte-identical outcomes), only `brace/envelop/sweep/kite/yield` do anything; `hold` and `volley` as instructions do nothing; Orders substrate built in 2 places using 2 of 4 trigger kinds (:85-94).
  - Melee pool bakes `eff_size` in (`exchange.py:110`); volley pool `max(1, eff_power-_vpen)` does not (`orchestration.py:1154-1166`); folding it in while keeping post-roll `K_SQUARE*eff_size` would double count numbers (:98-107).
  - `TROOP_TYPE_REACH={}` makes the recoil gate's reach half a no-op; filling it flips currently-passing C2/C6, which are the same scenario built twice (:67, :143).
  - Frozen momentum / flat `charge_pen=3` every tick (contributor to C1-C7, unquantified) and volley/melee standoff collision (`VOLLEY_MIN_RANGE=2` == melee standoff 2.0 so locked archers fire unreciprocated volleys, 15-36% max HP) (:62-66).
- **Conflicts / stale:** Stale-comment claim: config/orchestration comments calling ROLE_SPEC "INERT" are wrong (Stage D wired the gate) (:79). Working-tree check: `_speed_accum` is now used in `modules/mass_battle/hierarchy/units.py:2097`, so the node-path floor may have been addressed `[UNVERIFIED]` for `_node_advance` specifically.
- **Open items:** DG-6a..f (node-path speed floor, speed granularity, volley pool, reach ratification, hold for ranged, tactics grounding); quantify charge_pen; C3 mirror asymmetry; `sweep` transit.

### .audit/2026-07-08-mass-battle-gauge-architecture-audit/README.md
- **What it is:** Final combined engineering audit (third-level synthesis of two Opus-max waves, 11 surfaces, ~24 subagents) of why `tests/sim/gauge_mb.py` scored 7/20; MB lane / RC-5, 2026-07-08.
- **Status:** none stated. Reading: historical, but the best single index of MB engine defects E1-E10, harness artifacts and rulings DG-6..DG-16; ED-MB-0006 is its reference.
- **Bears on:** MB, DICE, CORE (harness instrument).
- **Content that matters:**
  - Row count: 13 nominal fails -> ~11 real (C3,H9 noise) -> ~9 deep engine divergences (H2-H8,H10,H11) after R1/R3 treated as harness (:31-39).
  - E1 density defect proven by reversal ablation (H3 100->0, H10 0->100) and D1 amplifier p~3.2 vs target <=1.4; they are multiplicative, no single fix lands a row in band ("diagnostic, not curative") (:95-97, :250).
  - H4 "Cannae" failure is a compound: ED-MB-0006 flipped it from WIN-OUT to losing; symmetric-thirds split gives pin centre 133 of 400; wing-release inert in H4 slot but decisive in H11 slot; `recalc_size` cascade; 33% draws are a turn-cap artifact (:146-156).
  - E2 Arrowhead side asymmetry (100/0/0 on side A vs 43/43/13 on side B) root line untraced; every cavalry row C1-C7 has Arrowhead on side A so all are provisional (:101, :259).
  - Rulings DG-6..DG-16 list with crosswalk to wave labels; DG-1..5 already ruled (symmetric-at-parity, fighting withdrawal/yield, intensive bottom-up pool, blended sibling-pull morale, racing-clocks closed) (:206-230, :268-284). Morale-floor-of-1 (DG-8) vs `mass_battle_v30.md:294`.
  - Granularity directive verdict: cell-count/density half necessary; per-cell quality half provably inert for the gauge; speed, dr, stamina and volley still ungrounded; two stamina systems run simultaneously under PER_CELL=1 (:160-170, :222).
  - Method note: ~4.5M subagent tokens (:4) as an example of cost for this style of audit.
- **Conflicts / stale:** All file:line cites are July 2026 and `units.py` has grown (recalc_size now at :2982 still without the guard, per one grep); `PER_CELL`/`POOL_QUALITY_MODEL` defaults and gauge band results should be re-run before relying on any pass count. Whether DG-6..16 were ruled later: `[UNVERIFIED]` here (check HANDOFF_MB / ED-MB ledger).
- **Open items:** Section 7c list (trace E2; ablate H7/H8; E4 rescue test; quantify E7); DG-6 is named the rate-limiting ruling.

### .audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md
- **What it is:** Round-2 historical-precedent research (Byzantium, China, Japan, HRE, Venice, Renaissance Italy, Habsburg Spain) with a 58-proposal judge pass; 22-agent workflow, Sonnet research/fact-check then one Opus judge (FA+SE lanes, 2026-07-09).
- **Status:** "FILED ... Not itself canon — a research/synthesis artifact the docket items cite as provenance." Reading: research (tier 3), historical; items filed as ED-FA-0018..0034 / ED-SE-0018..0044.
- **Bears on:** FA, SE, CHAR (rank ladders), CORE (Directive/AP model).
- **Content that matters:**
  - Premise corrections: the Guild ladder is NOT missing (`faction_politics_v30.md` §2.5 already authors Apprentice..Grand Guildmaster; finding A-03 describes the superseded five-rank draft); the one truly empty rank surface is the Crown Administrative branch (§1.1b) (:19, :144-145).
  - Result 44 kept / 14 cut; seven proposals competed for the Administrative void and CHN-2 Imperial Examination Ladder won, shipped `needs_jordan` (:145-147, :166).
  - Synthesis bundles: S-1 Consolidated Command = BYZ-6 (doux, pooled AP `2+ΣFacilityTier`) + IT-5 (Legation split); S-2 governor-oversight toolkit = Podestà (appointer-liability) + Corregidor overlay on prior SE-7; S-3 guild-regulation suite; S-4 guild ladder fork; S-5 locked-extraction-figure substrate = SE-JP2 Kokudaka Survey + HAB-5 Encabezamiento (:280-290).
  - Twenty-one `needs_jordan` forks listed (:306-326), e.g. Office/Dignity split, Valido track, Chancellery Gatekeeper deception of the player, irreversible Crush the Estates, Reichsacht, Mediatize.
  - Execution record: 12 P1 items authored as PROPOSED prose into `faction_politics_v30.md` §1.0b/§1.0c/§1.0d/§2.5a, `governance_play_redesign_v1.md` §1.1a/§1.3a/b/c, `settlement_layer_v30.md` §3.3b/c; Compact opened as a 5th Ledger tag family (:332-355).
  - Anti-fabrication: every magnitude is a "shape proposal", not sim-calibrated (:359).
- **Conflicts / stale:** All landings are into design `.md` (now `.designs/`) — prose, not mechanism (CLAUDE.md §0.05); whether `engine/season/` models Directive/AP/Ledger/Π/Compact at all is `[UNVERIFIED]`. References `sim/*.py` (dissolved) and `faction_action.py`. The ED rows named should be checked against `registers/editorial_ledger_fa*.jsonl` for current status.
- **Open items:** the whole needs_jordan queue, unauthored promote-ready P2/P3 (CHN-6, HRE-2/3/4, VEN-SE-2, IT-1/2, HAB-1/4), card-deck triggers (Cell Revolt etc.) only noted inline.

### .audit/2026-07-12-governance-compendium/00_index.md
- **What it is:** Index of the Governance Consolidated Compendium v1: parts 21-210 (94 event cards), 30 (12 ripple chains), 40-45, tier3/tier4 registers, 44 re-evals (lane IN, cross-cutting SE/FA/GO, 2026-07-12).
- **Status:** "PROPOSED ... Read-only research consolidation. NOT canon; nothing here flips a Status: line." Reading: reference-only; the decision surface lives in `architecture/governance_consolidation_v1.md` §6 (named :13-16, :58) which is outside this assignment.
- **Bears on:** SE, FA, CORE (Directive/AP/Π model), WR (event deck).
- **Content that matters:**
  - Event corpus: 94 historical cards in 10 categories (succession 8, blockade 10, siege 10, earthquake 9, flood/drought 10, famine 9, plague 9, climate 9, debasement 10, trade-monopoly 10) plus 58-card grounded deck and 28-card Goldenfurt deck, about 180 cards combined (:22-29).
  - Four pre-existing built substrates it reconciles against: `sim/territory/`, `goldenfurt_slice`, 500-seed `settlement_mgmt_stress_01`, the march/hierarchy layer (:53).
  - Proposed canon touchpoints: `faction_politics_v30.md`, `settlement_layer_v30.md`, `governance_play_redesign_v1.md`, `governance_ripple_substrate_v1.md` (:54).
  - Triage of the 58 comparative-governance proposals: 12 authored / 9 promote-ready / 23 needs-Jordan / 14 cut (:44).
- **Conflicts / stale:** `sim/territory/` and `tests/sim/settlement_mgmt_stress_01/` named as built substrate; `sim/` is dissolved so the reconciliation claims need re-checking against `engine/season/` `[UNVERIFIED]`. Links `event_cards/*` and `reeval/*` are not in this assignment (not on disk list given).
- **Open items:** all of it is unratified; start-here pointer is the consolidation doc's five architecture reconciliations (Compact vs Leverage, §1.0d vs Goldenfurt recall, event-model fork, Mandate carrier, AP model) (:13-15).

### .audit/2026-07-12-governance-compendium/40_roster_officer_system.md
- **What it is:** Part 40, NPC Roster / Officer / Advancement ("Ascendancy") system: 8 mechanisms, ~96 historical cases in categories A-J, system design and open rulings (lane IN, 2026-07-12).
- **Status:** "PROPOSED / provisional ... Jordan-vetoable; nothing here is ratified canon". Reading: reference/design proposal.
- **COVERAGE NOTE:** read lines 1-330 and 560-621 plus the heading map; categories B-J case tables (:326-489) and the cross-reference §40.4 (:490-532) not read line by line.
- **Bears on:** CHAR (NPC ambition/advancement), FA (Standing ladder), SE, CORE.
- **Content that matters:**
  - Eight mechanisms M1 patronage, M2 credentialed merit, M3 kinship, M4 court favoritism, M5 bureaucratic chokepoint, M6 venality, M7 armed retinue, M8 ideological authority; each carries its own downfall shape (:30-39).
  - Design: one `ConsolidationEngine` with `scale_binding` in {settlement, court, lineage}, reusing the settlement ambition engine's field grammar (`goal/method/timeline/progress/trajectory`); the court binding is gated on the Standing ladder and Knots graph (existing), not the unbuilt settlement registry (:61-90).
  - NPCs climb the SAME Standing ladder as the player; off-ladder auxiliary meters (`shadow_standing`, `moral_authority`, `renown`, `service_rank`, Dignity, custody-bonus) substitute or force ratification; flag `player_seats_are_contestable` is the Jordan toggle (:92-125).
  - `power_base` enum {patronage, merit, kinship, bureaucratic, military, purchased, ideological} types both the climb driver and the exploitable downfall ("every action pays what it buys") (:196-268).
  - Naming: system "Ascendancy"; roles Retainer/Patron/Advisor; "officer" reserved for mass-battle unit commander (~20 of 96 entries collide) (:270-298).
  - Genuine architectural gaps: Mandate separable-from-possession (`custodian_id` != `holder_id`), in-transit Key interception, dormant/hidden tags, co_leadership state (:561-569); all depend on the retired Key substrate for emission (:222).
- **Conflicts / stale:** Emission "through the Key substrate" (:222) conflicts with ED-IN-0232 retirement. Mass-battle "officer" term collision is real in the MB lane vocabulary.
- **Open items:** `player_seats_are_contestable` ruling; parallel-track-count question (needs_jordan item 3); lineage binding Jordan-gated (:84).

### .audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md
- **What it is:** Part 41, proactive player-action menus at four scales (Organization / Settlement / Territory / Faction) from ~72 historical proposals (lane IN, 2026-07-12).
- **Status:** "PROPOSED / research-derived ... Numbers are deliberately absent by design". Reading: reference/design proposal.
- **COVERAGE NOTE:** read lines 1-200 (framing; settlement S1-S14, organization O1-O15, territory T1-T19, faction F1-F14, cross-scale X1-X2) and the heading map; X3+, §2F, §3 concrete menus, §4 reuse ledger, §5 cross-refs, §6 gaps (:200-494) not read in full.
- **Bears on:** SE, FA, CORE (action menus), GO (UI menus).
- **Content that matters:**
  - Four scales are four kinds of managed thing: Organization = membership dispersed across places it doesn't own; Settlement = one place's homeostat (only scale with built machinery); Territory = connective tissue between settlements (explicitly unbuilt gap, BYZ-6/IT-5); Faction = the polity's rules (:22-89).
  - Organization and Territory are orthogonal axes (Ottoman sanjak vs akıncı corps) (:81-89).
  - New levers proposed with named identity: Relay Tier 0-3 (T1), Territory Reserve Pool (T2/T10), Cordon-Complete flag (T4/T5), Beacon Network tier 0-3 (T6), Surveyed flag (T7), Grant Ledger (T8), Governance-Mode Local/Appointed (T9), Muster tag (T11), Centralization dial (F12), `codified_law` propagation-scope flag (F5) (:151-190).
  - Org-scale proposals reuse the Investigate resolver inward (Visitation, Audit Branch) and give Org its own AP pool and Standing ladder (O1, O5, O14) (:129-143).
  - Governing constraint: reuse Prosperity/Order/Defense/Treasury/Weight; add state only when it changes the KIND of decision (:14-18).
- **Conflicts / stale:** Settlement scale "only scale with fully-built machinery" cites `governance_play_redesign_v1` which is itself a PROPOSAL (per interface_report). Whether `engine/season/` has any Territory/Org entity: `[UNVERIFIED]`.
- **Open items:** §6 design-taste rulings owed (:438); BYZ-6/IT-5 cross-reference in §5A.

### .audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md
- **What it is:** Part 42, deduped catalogue of 109 domain-action/verb proposals extracted from the 94 event cards, grouped by parent verb (Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate, Directive, NEW) (lane IN, 2026-07-12).
- **Status:** "PROPOSED ... none of this has been ratified". Reading: reference index.
- **COVERAGE NOTE:** read lines 1-70 (Develop and part of Fortify groups); remaining groups and §2.11 reskin clusters (:70-254) not read.
- **Bears on:** SE, FA, CORE.
- **Content that matters:**
  - Eight base verbs already in the governance model: Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate (+ Directive) (:20-22).
  - Many verbs gate on hidden environmental stats (SiltLevel, SalinityLevel, SubsidenceRisk) and on tags (`Overcrowding`, `route-diversified`, `Rebuild-to-Code`) (:47-70).
  - Gated unlocks: Lighthouse only purchasable after a storm Crisis; Standing Fleet / Coalition Fortify Pool must be banked before the Crisis (:55, :65-66).
- **Conflicts / stale:** Depends on the HEV-* event-card files and the 2026-07-10 catalogue (not in this assignment).
- **Open items:** §2.11 reskin clusters flagged for a ratification pass (:36-38).

### .audit/2026-07-12-governance-compendium/43_directive_types.md
- **What it is:** Part 43, proposed Directive-type expansion beyond the six live types (Extract, Tax, Suppress, Install, Host, Cede): Embargo, Multilateral Embargo, Recall, Quarter, Nationalize Charter, Sovereign Bargain (lane IN, 2026-07-12).
- **Status:** "PROPOSED (research-derived; not yet ratified ...)". Reading: reference design proposal.
- **Bears on:** SE, FA, CORE (Directive enum).
- **Content that matters:**
  - Central finding: all six live Directives target the settlement they are issued to; Embargo/Multilateral Embargo target a THIRD party via own trade, Recall targets a standing force, Quarter compels a method (:11, :109).
  - Embargo's Comply/Bargain/Defy is resolved by the settlement asked to enforce it (License Exception as Bargain); Multilateral Embargo structurally removes Bargain, leaving Comply/Defy (:19-34).
  - Recall (disband appanage military) vs Toluid/Kongo; Quarter creates a ratchet (Force-method hardens Actor-Disposition and removes Consent method) (:37-55).
  - Nationalize Charter and Sovereign Bargain are Directive-adjacent (arbitration-resolved / Standing-6+ rank-gated), unresolved as enum members (:57-76, :109).
  - Trigger predicates are written as pseudo-code over Π, Grudge, Standing, Fiscal Stance (e.g. :23, :34).
- **Conflicts / stale:** The "six live types" claim is the catalogue's framing; the working tree's Directive enum in `engine/season/` (if any) is `[UNVERIFIED]`.
- **Open items:** enum membership of Nationalize Charter and Sovereign Bargain (:109).

### .audit/2026-07-12-governance-compendium/44_standing_institutions.md
- **What it is:** Part 44: catalogue of build-once "standing crisis-defusing institutions" plus a synthesis classifying crises as recoverable dips vs terminal doom-loops and mapping stress-test patterns A-H to institutions (lane IN, 2026-07-12).
- **Status:** "PROPOSED (research-derived; not yet ratified ...)". Reading: reference design synthesis; the strongest bridge document between the event research and the stress test.
- **Bears on:** SE, FA, CORE (balance/crisis architecture), WR.
- **Content that matters:**
  - Class definition: build-once, family-scoped, self-consuming/self-funding, and its signature is DECOUPLING (Water Board decouples flood funding from war Directive; Granary StockLevel decouples famine buffer from Treasury) (:23-36). Anti-institution example: Refuge Walls writes the `Overcrowding` tag that triggers Epidemic (:36).
  - Stress-test patterns: A Demotion spiral 7/7 ("tragic-downfall arc is the default"); B Π runaway pinning at the R-4 cliff Π7->8 ~6/7; C Compact/Assessment deterministic strip below subsistence ~4/7; D cell-revolt stacking ~6/7; E patron-lapse un-shielding; F Clerk-Corruption loaded gun ~6/7; G Suspicion->Recall on undefined threshold; H Mandate saturation hides collapse (`Mandate=clamp(round(7T/(T+6)))`, a revolt moved rounded Mandate not at all) (:149-160).
  - Appeals succeed 0/6 across seeds (~20-31% vs a Std-7 adjudicator); mid dice_pool rolls ~55% (:160).
  - The "Loop" clause in each card is a latent recoverability classifier; the discriminating bit is whether a standing institution was built before the trigger (:166-182).
  - Load-bearing result: every material-axis doom-loop (Prosperity, Order, Treasury, Defense, Π) has an institution circuit-breaker; NO institution breaks the Standing/rank loops (A, E, G) which need substrate tuning (survivable Appeal Ob, successes retiring failure Keys, defined Suspicion->Recall constant) (:245-252).
  - Odds-contract divergence: deck promises linear `d_sigma` (base 50% + 10%/pt, floor .05, cap .90) but the engine `sigma_leverage.p_success()` is a normal-CDF (base_Ob 3, pool 7, +major: 78% vs ~90%) (:266).
  - Beacon Network / Relay Tier contingent on an unauthored inter-settlement latency model (`engine_clock` doc:null) (:267); tag-family proliferation (Compact, Concession, Outlawed, Capital-Posture, Muster) needs consolidation (:268); Organization economy unspecified (:269).
- **Conflicts / stale:** Pattern H quotes a Mandate formula that may differ from the current `engine/season/` Mandate carrier; `sigma_leverage.p_success` named as CANONICAL is in dissolved `sim/` (the DICE owner is now `engine/dice_engine/dice_engine.py` per CLAUDE.md §5) `[UNVERIFIED]`. Stress-test run is on the PR#119 provisional governance mechanics, not `engine/season/`.
- **Open items:** subsistence-floor clamp on §1.3a; Π relief valve (VEN-SE-5 Scuole Grandi) and Grudge half-life; Suspicion->Recall constant; ship the institution menu and Crisis-card system as one loop (:271).

### .audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md
- **What it is:** Part 45: proposed hidden long-fuse environmental stats (SiltLevel, OreGrade, SalinityLevel, SubsidenceRisk, ...) with a per-stat "track vs abstract to Prosperity" decision framework (lane IN, 2026-07-12).
- **Status:** "PROPOSED — needs a granularity ruling". Reading: reference; honours Jordan's standing "abstract, don't over-granulate" ruling.
- **COVERAGE NOTE:** read lines 1-70 (framework, SiltLevel, OreGrade, SalinityLevel); SubsidenceRisk onward and the per-stat recommendation table (§3) at :70-151 not read.
- **Bears on:** SE, WR, CORE.
- **Content that matters:**
  - Default for every stat is "folds into Prosperity/Order drift, no dedicated tracker" unless one of three tests holds: fuse is cross-settlement, multi-decade, or an institution needs a legible number to gate on (:11-27).
  - The crux: Prosperity is local, so cross-settlement fuses (Yellow River siltation->downstream RisingWaterLevel; Fens reclamation->SubsidenceRisk) cannot be abstracted without a tracked handoff (:15).
  - SalinityLevel crossing a final threshold is irreversible (Sumer->Akkad), vs SiltLevel recoverable via Dredge/Magistracy (:59-68, :37-46).
- **Conflicts / stale:** none checked.
- **Open items:** per-stat ruling (§3), which the file frames as owed to a follow-up authoring pass.

### .audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md
- **What it is:** Proposal-Status Closure Register: triage of all 58 comparative-governance proposals against NERS audit (2026-07-11) and the stress test (2026-07-12) (lane IN, 2026-07-12).
- **Status:** "PROVISIONAL / consolidation artifact ... Nothing here is ratified canon". Reading: reference map; verdicts are advisory.
- **COVERAGE NOTE:** read lines 1-110 (provenance, cohorts, 12 authored + 9 promote-ready tables); needs-Jordan table (:105+), cut list, vindicated-rejected (§3.7), collected rulings (§3.9) and un-adjudicated list (§3.10) up to :448 not read.
- **Bears on:** FA, SE, CORE.
- **Content that matters:**
  - Cohorts 12 authored (PR#119) / 9 promote-ready / 23 needs-Jordan / 14 cut; EDs ED-FA-0018..0034, ED-SE-0018..0044 (:38-51).
  - The `reeval/` directory (44 per-proposal re-evals) is EMPTY: the re-evaluation was delivered only as the stress-test synthesis (:28-34) — so the 00_index claim of "44 re-evaluated" is stale.
  - Only 2 of the 12 built PR#119 items are clean KEEP (HAB-5, HAB-7); 8 REFINE, 2 MERGE (SE-JP1 Bind the Cells, CHN-9 Kaochengfa) requiring deletion of landed subsections; ED-1094 means merge = ratification so fixes had to land inside the PR (:79-85).
  - IT-7 Seggio: stress test found a terminal lock (no governance-scale force/seizure resolver); §1.3a Compact/Survey lock substrate is a deterministic below-subsistence strip needing a clamp (:66-68, :74).
  - HRE-4 Borrow is a canonical pledge shape that other Levy pledge variants should collapse into (:95); IT-2 condotta touches four flat-scalar `faction.Mil` read sites including `massbattle.py::_faction_to_unit` (:103).
- **Conflicts / stale:** Contradicts 00_index claim that `reeval/reeval_*.md` re-evaluates all 44 (directory empty, :28). Whether PR#119 merged and which fixes landed `[UNVERIFIED]`.
- **Open items:** the 23 needs-Jordan forks; 3 un-adjudicated (IT-6, CHN-7, VEN-SE-3).

### .audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md
- **What it is:** Discovered Open-Work Register: pre-existing open items from Goldenfurt v1.1 backlog, the 2026-06-22 baseline territory audit and the 500-seed stress test (lane IN, 2026-07-12).
- **Status:** none stated (scope note: "not new design content ... work-intake queue"). Reading: reference register, partly stale.
- **Bears on:** SE, FA, CORE, WR.
- **Content that matters:**
  - Settlement-type taxonomy drift F1/H3: canonical §1.2 defines 8 types but the registry has 11 (adds Village, Fortress-City, Cathedral-City); "Village" is used by ~18 spoke settlements with no stats/facility slots/actor counts; "structural root of 7 stress-test findings" (:70, :88).
  - Open gaps G2 (church infrastructure keyed per-territory not per-settlement) and G3 (unused `PT_GAIN_*/CI_GAIN_TEMPLAR/ORDER_GAIN_*` constants never applied) (:68-69).
  - Ledger-family divergence: built `ledger.py` `TAG_KINDS={Precedent,Grudge,Debt,Reputation,Leverage}` vs proposed `Compact` as 5th family; and §1.0d Performance Audit likely duplicates Goldenfurt G606 recall (:96-105).
  - Numeric tuning still pending the §9 sweep: AP curve `AP=2+facility_tier(+1 Seat/Cathedral)`, Π band, suspicion->recall threshold (:30-32).
  - 24 NERS probes in the stress harness specified but never executed, so NERS "confirmed" verdicts may be unvalidated (:90).
  - Predicate grammar too weak for event-history triggers (sim-F4, High) (:26).
- **Conflicts / stale:** `sim/territory/registry.py` and `tests/sim/settlement_mgmt_stress_01/` named as built; `sim/` is dissolved. G1 reported closed; `Compact` vs `Leverage` conflict named as unreconciled.
- **Open items:** everything in the tables marked ⏳/Open.
