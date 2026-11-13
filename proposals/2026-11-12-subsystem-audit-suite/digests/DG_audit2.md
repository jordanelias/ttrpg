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

### .audit/2026-07-12-governance-compendium/_workings_joined.md
- **What it is:** Verbatim join (16 fragments, 2,734 lines) of the compendium's working parts: event-card integration map, 10 event-card category files (HEV-* cards), 12 ripple chains (THR-01..12), and four `reeval/` files (chn_byz, hab_it, jp_se, ven_hre).
- **Status:** fragments are PROPOSED / "extracted verbatim ... not yet vetted against the live card corpus"; reeval files "PROPOSED / provisional re-evaluation artifact". Reading: reference; the reeval fragments are the only surviving copy of the per-proposal re-evaluations.
- **COVERAGE NOTE:** read lines 1-40 (header, integration map start), 1250-1310 (ripple chains THR-01/02), 1546-1585 (reeval_chn_byz start), 2307-2393 (reeval_jp_se, in full). NOT read: event-card bodies (:19-1249), THR-03..12 (:1310-1545), rest of reeval_chn_byz/hab_it/ven_hre (:1585-2306, :2393-2734). `[SKIPPED: .audit/2026-07-12-governance-compendium/_workings_joined.md lines 40-1249, 1310-1545, 1585-2306, 2393-2734 — context budget]`.
- **Bears on:** SE, FA, WR, CORE.
- **Content that matters:**
  - Catalogue count: 94 HEV cards confirmed by direct enumeration of every `### HEV-` heading, not the "~124" in the task brief (:33-37).
  - Re-evaluation vs BUILT substrate for the 8 Japan items (:2307-2389): SE-JP1 RECONCILE (Local-Actor representation is three-way inconsistent: `npc_ids` unbounded list, Goldenfurt 9 named actors, stress harness count-per-type; the NERS "1-2 actor cap" MERGE reason does not survive); SE-JP2 COLLIDES (built Settlement schema has no `assessed_base` field; Compact vs Leverage); SE-JP3 COLLIDES ("Charter" is not among built `TAG_KINDS`; `charter_age_seasons` not tracked); SE-JP4 SUPERSEDED/stay CUT; FA-JP2/3/4 STILL-VALID (no built FA oracle); FA-JP5 RECONCILE (single scalar `suspicion` + G606 +1/season cap would be forked).
  - Built facts used as judging substrate: ledger `TAG_KINDS={Precedent,Grudge,Debt,Reputation,Leverage}` (no Compact, no Charter); legitimacy/popular_support "inert"; `AP=2+tier(+1 Seat/Cathedral)`; province Accord = floor-average Order; effective_prosperity = SUM; the §1.8 Mandate formula is design-only (:2314).
  - Coverage-gap flag: the built substrate only reaches SE-lane settlement mechanics; FA-lane content has no built oracle to re-judge against (:2388).
  - Ripple chains encode multi-step causality as `follow_on` seeds writing tags that the next card's trigger reads, e.g. THR-01 debasement->famine->coup and THR-02 toll->private army->Toluid contest (:1267-1309).
- **Conflicts / stale:** Contradicts `tier3_proposal_status_closure.md` :28 ("`reeval/` directory is empty") and 00_index.md :45 — the reeval files exist here, so tier3's claim is stale or reflects a different moment. Built substrate cited is the dissolved `sim/territory/` (Settlement schema, `ledger.py` TAG_KINDS) — equivalents in `engine/season/` `[UNVERIFIED]`.
- **Open items:** the Compact/Charter/Leverage tag-family reconciliation; Local-Actor representation decision.

### .audit/2026-07-12-settlement-season-stress-sim/_workings_joined.md
- **What it is:** Verbatim join (7 fragments, 853 lines) of the seven per-seed play-out traces S1 Brixholm, S2 Dunmark, S3 Sanct Vaduz, S4 Kronmark, S5 Eisgrund, S6 Valholt March, S7 Hohenfels (5 seasons each, Opus seed agents).
- **Status:** fragment statuses not read; the parent synthesis is "FILED ... NOT canon". Reading: historical raw traces underlying the synthesis and Appendix B.
- **COVERAGE NOTE:** only the fragment index (:19, :125, :253, :360, :525, :646, :763) was read; the per-season traces were not. `[SKIPPED: .audit/2026-07-12-settlement-season-stress-sim/_workings_joined.md bodies — context budget; their depth-3 failure rows are reproduced in appendix_B_roll_failures.md, which was read]`.
- **Bears on:** SE, FA, CHAR.
- **Content that matters:** seed set covers port/guild politics, frontier fortress under Crown Directive, cathedral seat with Seggio, famine town under Compact lock, mine under patron-lapse, 3-settlement territory Mandate aggregation, absentee court seat under Performance Audit (per synthesis :11-17).
- **Conflicts / stale:** the "simulation" was agent-driven paper play (no executable settlement-season engine existed, synthesis :5-8) — traces are not execution artifacts in the §0.2 sense.
- **Open items:** none beyond the synthesis.

### .audit/2026-07-12-settlement-season-stress-sim/appendix_B_roll_failures.md
- **What it is:** Table of all 57 traced major-roll failures (depth-3 L1/L2/L3 cascades) across 7 seeds, each with resolver and stated P(success) (2026-07-12, lane IN).
- **Status:** none stated (appendix to the synthesis). Reading: historical evidence table.
- **COVERAGE NOTE:** read lines 1-50 (S1 and S2 rows, and S3-S4 starts); S4 remainder through S7 not read.
- **Bears on:** SE, FA, CHAR, DICE.
- **Content that matters:**
  - Rows show the chain Need-jaw/Directive-jaw `resolution_quality` Key -> Duty-failure input -> §1.0a Demotion after 3 failures; Appeals ~22-25% vs Std-7 adjudicator (:30, :41).
  - R-4 cliff: S1 Π 7->8 on a single failed vote (:13); Cell Revolt Crisis from 3 Collective-Liability stacks (:28); Seggio lock makes heresy case permanently unadjudicable (:41); Locked Survey at Prosperity-3 era stale-high once Prosperity falls to 2 (:49).
  - Example realised-roll demonstration of the §1.3c ordenanza gap having teeth: blocked ambition -> uprising -> disruption -> quota fail -> demotion (:17).
- **Conflicts / stale:** pool sizes were engine-assigned; no character attribute block existed (synthesis §3 HIGH).
- **Open items:** none beyond the synthesis.

### .audit/2026-07-12-settlement-season-stress-sim/ground_truth_odds.md
- **What it is:** Computed ground-truth odds tables: `dice_pool` P(net>=Ob) at TN6/TN7 for pools 3-18 and `d_sigma` P by base_Ob/pool/advantage, from `skills/valoria-dice-model/valoria_dice.py` and `sim/autoload/sigma_leverage.py::p_success` (2026-07-12).
- **Status:** none stated. Reading: reference numbers; the dice model and sigma engine are DICE-lane referents and may have changed (`engine/dice_engine/dice_engine.py` is the CLAUDE.md §5 owner).
- **Bears on:** DICE, SE, FA.
- **Content that matters:**
  - Die model: 1 -> -1, 10 -> +2, >=TN -> +1 (:7); e.g. TN7 pool 7 Ob3 = 55%, pool 10 Ob4 = 57% (:36, :39).
  - net_sigma by advantage level: minor .25 / moderate .5 / strong .75 / major 1.0 (:50); d_sigma base_Ob3 pool7 neutral 46%, +major 78% (:66).
- **Conflicts / stale:** cites dissolved `sim/autoload/sigma_leverage.py`; numbers should be re-derived from current dice owner before reuse `[UNVERIFIED]`.
- **Open items:** the legible-vs-engine odds contract (see synthesis §0.4).

### .audit/2026-07-12-settlement-season-stress-sim/stress_test_synthesis_v1.md
- **What it is:** Max-effort synthesis of a 7-seed x 5-season adversarial play-out of the PR#119 provisional governance mechanics, with a main-session verification layer (13-agent workflow, lane IN, 2026-07-12).
- **Status:** "FILED ... Read-only review artifact — NOT canon." Reading: historical findings; method was paper play by agents, not execution.
- **COVERAGE NOTE:** read lines 1-275 in full (except nothing skipped; file is 275 lines).
- **Bears on:** SE, FA, CHAR, DICE, CORE.
- **Content that matters:**
  - Verification layer downgraded two loud findings to digest artifacts: "Crisis family has ZERO resolvable cards" (Crisis cards route to `d_sigma`) and "no Gu-Std2->3 rung" (Guild ladder authored through Gu-Std 6) (:42-62).
  - Agents under-estimate `P(net>=3)` on 7D TN7 by 5-7 points (truth 55%) (:64-70); `d_sigma` legible linear model (50% + 10%/pt, floor .05 cap .90) diverges from the canonical normal-CDF `p_success()` at tails (78% vs ~90%) (:72-78).
  - Mechanic verdicts: HOLD §5 resolution_quality->Standing bridge, §1.0a magnitudes, §3.3b Za patron-lapse; BREAK §1.3a (no subsistence floor, ~8-season cooldown), §3.3c Seggio (no governance-scale force/seizure resolver), Mandate-at-scale; MERGE confirmed for §1.0d and §1.3b (:90-107).
  - Cascade patterns A-H (see Part 44), e.g. demotion spiral 7/7, Appeals 0/6, Mandate `clamp(round(7T/(T+6)))` hides collapse (:116-143, :147-150).
  - Gaps: no character attribute block in any seed so no dice validation possible; territory-scale governor AP economy undefined; §5 mis-scores a sanctioned Defy as a Duty-failure (:149-165, :184-188).
  - Vindicated rejected proposals: IT-3 Sforza Gambit the strongest reinstatement candidate (bounded force-seizure/emergence resolver), VEN-SE-4 Dedizione, VEN-SE-7, BYZ-4 price-control half (:196-215); prioritised 13 findings (:235-265).
- **Conflicts / stale:** Examples of stale cites: `sim/autoload/sigma_leverage.py`, `sim/provincial/faction_action.py`. The simulated "ruleset" is paper design (`governance_play_redesign_v1` PROPOSAL), so the findings test design prose, not `engine/season/` code.
- **Open items:** all 13 prioritised findings; need a seed/roster attribute schema (CHAR) so dice validation is possible.

### .audit/2026-07-22-combat-engine-stress-test/adversarial_pass.py
- **What it is:** Report-only script falsifying the stress-test report's own claims and tracing the half-sword result to its mechanism (in-process monkeypatches; PC lane, 2026-07-22).
- **Status:** none (script). Reading: historical instrument; read head only (:1-14).
- **COVERAGE NOTE:** read first 14 lines (docstring, imports); body (107 lines) not read.
- **Bears on:** PC, DICE.
- **Content that matters:** imports `systems/combat/combat_engine_v1` (path `ENG = ../../systems/combat/combat_engine_v1`) and `workbench.balance.winrate`; uses `HALFSWORD_FORM` from `weapons` to ablate the switch (:1-14).
- **Conflicts / stale:** hard-coded path `systems/combat/combat_engine_v1` — the live combat head is now `modules/combat/` (CLAUDE.md §4), so the script would not run as written `[UNVERIFIED]`. `HALFSWORD_FORM` still defined at `modules/combat/weapons.py:926`.
- **Open items:** none.

### .audit/2026-07-22-combat-engine-stress-test/grounding_battery.py
- **What it is:** 20-assertion HEMA/physics/treatise grounding battery over the deterministic physics layer (select_mode/coupling/core.damage/adef/halfsword), citing Williams, Fiore, Talhoffer, Ringeck, Le Jeu de la Hache; MATCH/DIVERGE reporting (2026-07-22).
- **Status:** none. Reading: historical instrument; read head only.
- **COVERAGE NOTE:** read first 14 lines; body (101 lines) not read.
- **Bears on:** PC.
- **Content that matters:** grounds on cited authorities and reports divergence not pass/fail (:1-8); report states 19 MATCH / 1 DIVERGE (PHASE-C poleaxe spike).
- **Conflicts / stale:** same stale engine path as above.
- **Open items:** none.

### .audit/2026-07-22-combat-engine-stress-test/phasec_probe.py
- **What it is:** Phase-C diagnostic probe localising three coupled levers (approach stop-hit, close-range reach, heft/PoB_frac) with deep-copied CFG (2026-07-22).
- **Status:** none. Reading: historical.
- **COVERAGE NOTE:** read first 14 lines of 51; body not read.
- **Bears on:** PC.
- **Content that matters:** report-only, commits nothing; baseline harness `workbench.balance.winrate` (:1-14). Findings it supports are in stress_test_findings.md.
- **Conflicts / stale:** stale engine path.
- **Open items:** target win-rate bands for spear vs arming in plate are a design call (see findings).

### .audit/2026-07-22-combat-engine-stress-test/primitives_probe.py
- **What it is:** Adversarial probe of the L0 primitive-law claim (behaviour emerges from five geometry primitives via `geometry.bake`, no weapon-name tables): dead-coefficient, name-table-vs-emergence, dead-primitive ablation (2026-07-22).
- **Status:** none. Reading: historical.
- **COVERAGE NOTE:** read first 14 lines of 79; body not read.
- **Bears on:** PC.
- **Content that matters:** three tests A/B/C; asserts `geo['halfsword']` orphan, half-sword capability as a 2-name fiat list `HALFSWORD_FORM`, and zero/max ablation of each raw primitive (:1-14). Findings P1 (ratified-but-unimplemented) and P2 (all raw primitives live, moves basket 29-87pp) are reported in findings.
- **Conflicts / stale:** `HALFSWORD_FORM` still present in `weapons.py:926`; PC-1 per the register was built (ED-PC-0014) so the name-table was reportedly retired as behaviour gate while the dict remains `[UNVERIFIED]` which sites still read it (`combat_systems.py:11` imports it).
- **Open items:** none.

### .audit/2026-07-22-combat-engine-stress-test/stress_battery.py
- **What it is:** 24-check mechanical correctness battery over 51 weapons x 4 armours x 8 traditions: robustness, extremes, determinism, mirror symmetry, numerical sanity, attribute monotonicity, 95% upset cap, termination (2026-07-22).
- **Status:** none. Reading: historical instrument.
- **COVERAGE NOTE:** read first 14 lines of 161; body not read.
- **Bears on:** PC, DICE, CHAR (attribute monotonicity).
- **Content that matters:** result recorded in findings: all green except M1 unguarded logistic overflow; 6.8 ms/fight; upset cap clamps maximal vs minimal fighter to 94.7% (`UPSET_FLOOR` 0.05).
- **Conflicts / stale:** stale engine path; `math.exp` logistic sites named in M1 (`combat_systems.py` L782/703/909/914) — one grep shows `modules/combat/combat_systems.py` no longer matches `math.exp` (only `weapon_physics.py:663` does), so M1 may be fixed `[UNVERIFIED]`.
- **Open items:** none.

### .audit/2026-07-22-combat-engine-stress-test/trace_backward.py
- **What it is:** Explicit-trace plus backward-causal analysis: wires the engine's `_TRACE` seam and spies on `assemble_net_sigma` and `core.strike`, then walks each battle from terminal state to origin (2026-07-22).
- **Status:** none. Reading: historical instrument; the method (trace every consumed input, walk causal chain backward) is reusable for any lane.
- **COVERAGE NOTE:** read first 14 lines of 156; body not read.
- **Bears on:** PC, CORE (trace-based verification method).
- **Content that matters:** three archetypal battles reproduced in findings: half-sword longsword loses by volume (11 vs 5 attacking beats), spear kills by stop-hit at gap 2.37 before closing, rondel wins on armour-defeat σ 0.53 (findings :175-190).
- **Conflicts / stale:** stale path.
- **Open items:** none.

### .audit/2026-07-22-combat-engine-stress-test/pc2_halfsword_expansion.md
- **What it is:** PC-2 half-sword roster expansion write-up: capability shipped (`grippable=True` on greatsword/flamberge ricassos), activation held; includes ready-to-activate `*_halfsword` form records (PC lane, ED-PC-0016 `needs_jordan`, 2026-07-22).
- **Status:** "CAPABILITY SHIPPED, ACTIVATION HELD" (title). Reading: possibly superseded by U10 and later PC work; not verified.
- **Bears on:** PC.
- **Content that matters:**
  - Naive unconditional switch is a liability for greatsword/flamberge: winrate vs arming at medium 93->50 and 93->49, heavy 71->55 / 72->69 (:27-40); base forms out-fight the half-sword on reach+mass.
  - Cheap per-form conditional (compare single-strike closed damage) is UNSOUND: flips with strength (longsword @heavy BASE at strength 4 contradicting PC-5's validated 73% win) (:44-64).
  - Three options for Jordan: duel-aware wrapper conditional, half-sword as a competing MODE in `select_mode`, or close-efficacy calibration of long weapons (:66-78); until then greatsword/flamberge record `affords_halfsword=True` but never switch.
  - Authored `greatsword_halfsword` / `flamberge_halfsword` records (mass conserved, `head='point'`, thrust_auth 0.92 / 1.0) ready to drop in with `HALFSWORD_FORM` additions (:85-130).
- **Conflicts / stale:** `modules/combat/weapons.py:926` `HALFSWORD_FORM` — whether greatsword/flamberge entries exist `[UNVERIFIED]` (one grep shows the dict at :926 only). Refers to `wrapper.py:123`.
- **Open items:** the activation decision (needs_jordan).

### .audit/2026-07-22-combat-engine-stress-test/ratified_unimplemented_register.md
- **What it is:** Register of 25 items ratified/RULED/plan-of-record but missing or incomplete in code, across PC, SC, IN, FA, SE, WR, FI lanes (2026-07-22).
- **Status:** none; it names itself a proposed generated surface. Reading: partly stale; PC rows reflect July state.
- **Bears on:** PC, SC, FA, SE, WR, FI, CORE, PROCESS (the register motive).
- **Content that matters:**
  - Root cause of rediscovery: no index of ratified-but-unbuilt work; fix proposed as generated `tools/observability/build_ratified_unimplemented.py` plus grep-before-claiming-novel discipline and a reader-existence test for `geometry.bake` outputs (:94-119).
  - PC: PC-1 emergent half-sword via `grippable` BUILT (ED-PC-0014); PC-2 held; PC-3 reversed-grip/JD-9 formula built but not wired (blocked on `core.coupling` fix); PC-4 `THRUST_AUTH_REF=0.52` built (ED-PC-0017); PC-5 Phase-C partially built (ED-PC-0015: spear heavy 85->28%, longsword both-heavy 38->73%); PC-6 U3-U9 not started (:33-40).
  - IN-1 `engine_clock` (T0 blocker for M1 and GO) NOT STARTED at that date; closure ticket ED-1051 still open (:60).
  - SC: ED-SC-0008 module contract refresh, ED-SC-0009 Face/Rattled strain channel (`Standing.strip()` never called), ED-SC-0010 chronicle focalization, ED-SC-0011/13 auto/played parity harness, ED-SC-0014 Standing homonym — all NOT STARTED (:62-66).
  - FA/SE/WR/FI: B12 scale-tier rewrite (no `Territory` symbol in code), ED-FA-0002 domain_actions home, Status-line flips never done for §1.0c, §2.5a, §3.3b, §1.3c; ED-WR-0002 RS->MS sweep gates Godot params export; ED-FI-0002 counter-espionage loop NOT STARTED (:79-90).
  - Mass Battle: no qualifying items (DG-1..5 implemented, DG-6+ not ratified) (:74-75).
- **Conflicts / stale:** Dated 2026-07-22 and cites `systems/...` and `engine/`; the later `engine/season/` (Layer 2) and `ED-IN-0232` Key retirement change several rows (IN-1 engine_clock and anything Key-based). U9/U10 later changed PC-6 status (see capstone). Contradicts `tier4` on whether Compact exists (not same file). Rows can be re-checked by grepping each cited symbol.
- **Open items:** the registry-generation tool (never confirmed built `[UNVERIFIED]`); each NOT STARTED row.

### .audit/2026-07-22-combat-engine-stress-test/stress_test_findings.md
- **What it is:** Combat-engine stress test findings: mechanical correctness battery plus HEMA/physics grounding battery, with a same-day adversarial revision, Phase-C investigation, primitives probe and backward-causal trace (PC lane, 2026-07-22).
- **Status:** none stated. Reading: historical but dense; contains self-retractions, so read the "Adversarial revision" before the TL;DR.
- **Bears on:** PC, DICE, CHAR (attribute dominance).
- **Content that matters:**
  - Mechanical: 447 passed / 9 failed baseline (9 accepted-red); stress battery all green except M1 (unguarded `1/(1+exp(-x))` at four `combat_systems.py` sites overflows only for attributes ~100x outside 1-8) (:13-16, :208-217).
  - Grounding: armour arc is textbook (dagger/rondel/stiletto +55..+62pp from none->heavy; pure cutters collapse vs plate e.g. shamshir 85->8; mace/bec_de_corbin/goedendag rise) (:229-244).
  - RETRACTED: "half-swording engages vs harness" strength and the "5 distinct context-leaders" C1 claim (low-N artifact; at N=400 only 3 leaders, 0.2-0.6pp margins); what holds is the 2.9pp unconditional tradition spread (:42-78, :246-259).
  - Half-sword switch is a net LIABILITY (longsword vs arming at mail/plate 27->62 / 41->73 when ablated); three fix attempts all failed; conclusion: symptom of reach over-weighting (Phase-C/G4), needs joint recalibration (:47-100).
  - Phase C is a three-lever joint problem: approach stop-hit (spear 93->38 at STOPHIT=0 but poleaxe barely moves 91->88), close-range reach decay for the half-sword, PoB_frac normalisation (spear 0.34 vs swords ~0.12) (:104-139); blocker is a missing target win-rate band design call.
  - G1: arbitrary vs-plate cliff among cutting polearms (guandao 96% vs bardiche 9.6%) from authoring coverage of `point` modes, not physics (:263-284). Agility dominance: +29.9..+34.4pp marginal, ~17pp over cognition (:73-74, :320-326).
- **Conflicts / stale:** M1 sites: `modules/combat/combat_systems.py` no longer has `math.exp` (one grep) so M1 may be fixed `[UNVERIFIED]`. U9 capstone says activation of morphology levers later occurred (U10), so the "levers at K=0" context of this report is superseded. Report itself retracts G2.
- **Open items:** target bands for spear/arming in plate; roster-wide joint re-tune; agility budget check; G1 roster audit.

## MB stress-test directory (`.audit/2026-07-22-mass-battle-stress-test/`) — coverage note

Context budget forced head-reads for this directory. For each markdown file I read the first 26-55 lines (status, directive, headline claims) and the line count; for each `.py` the first 6-14 lines (docstring: purpose, question asked, run command); `results.json` and `run_log.txt` first lines only. Each entry says so. Whole-directory facts verified once at the working tree: `modules/mass_battle/perimeter.py` exists (the orphaned-mechanics audit's "perimeter.py never wired" is marked WIRED by ED-MB-0035); `modules/mass_battle/config.py:512` `K_LINEAR` still reads env default 12 while `MORALE_EROSION_DAMP=0.7` (:332) now carries a `[CALIBRATED-DEBT]` tag and notes the `sim_verification_ledger.json` bare-integer self-whitelist was deleted in ED-MB-0041 Tier-0.1 (so audit finding 1.1 looks FIXED). The directory path `tests/sim/mass_battle/` that these files target has a live counterpart at `modules/mass_battle/`.

### .audit/2026-07-22-mass-battle-stress-test/README.md
- **What it is:** Index/narrative of the field-based mass-battle stress test: §1-§6 DG-10 movement-freeze fix (ED-MB-0011, PR #207), §7 spatial-model v2 Stage B+C (ED-MB-0012: CIRCLE->OBB contact, collide-not-decelerate) (MB lane, 2026-07-22).
- **Status:** none stated. Reading: historical record with some still-useful engine-map facts. **Head-read (55/267).**
- **Bears on:** MB, CORE (two-engine question), DICE.
- **Content that matters:**
  - Two mass-battle engines unreconciled: wired bare port `systems/mass_battle/sim/massbattle.py` (no field flags) vs active field engine `tests/sim/mass_battle/` carrying all flags (`FIELD_MOVEMENT`, `PER_CELL`, `PC_NODE_COHESION`, `LANCHESTER_ENABLED`, `POOL_QUALITY_MODEL`) and ED-MB-0001..0007 work (:11-23); ED-IN-0074 D5.
  - DG-10 headline: `_node_advance` computed `step=max(0, floor(base*disc_mult)+stance_mod)` with `disc_mult` 1.0 if disc>=5, 0.7 if >=3, else 0.4, so every sub-Discipline-5 body froze at 0 (:44-52); the grid engine got a clamp-to-minimum-quantum stopgap that flattens the sub-disc-5 speed gradient (discs 1-4 all 1 cell/tick) (:25-37). This is the same bug the gauge audit called E5/DG-10.
  - Guard test `tests/valoria/test_mass_battle_systems_movement.py` (8 tests) (:37-39).
- **Conflicts / stale:** the wired engine is the "older integer engine slated for Stage-G retirement" per the fiat register, but its claim about what `resolve_mass_battle` calls should be re-checked against `engine/season/` `[UNVERIFIED]`.
- **Open items:** Stage G (route game path onto field engine) not started per `ratified_but_unbuilt_backlog.md`.

### .audit/2026-07-22-mass-battle-stress-test/adversarial_deep_audit_v1.md
- **What it is:** Five-critic blind deep adversarial audit of the mass-battle engine on fiat, historical/theory compliance, primitive emergence, sequencing and reachability, with hand verification (MB lane, 2026-07-24).
- **Status:** none stated. Reading: historical but high-value; several findings are verifiably fixed. **Head-read (55/632).**
- **Bears on:** MB, DICE, PROCESS (anti-fabrication gate).
- **Content that matters:**
  - Verdict: "machinery that documents itself as working and does not, on a provenance layer that is largely self-referential" (:8-10).
  - 1.1 `tests/sim_verification_ledger.json` laundered 26 bare-integer constants (`K_LINEAR=12`, `CASUALTY_SCALE=4`, `MAX_SUB_PHASES=5`) through the anti-fabrication gate by citing the engine file itself — working tree now notes it was deleted in ED-MB-0041 Tier-0.1 (looks FIXED) (:14-20).
  - 1.2 fabricated citation: `orchestration.py` cites "mass_battle_v30.md §A.3b — 45deg octagon GREEN/YELLOW boundary" but "octagon" appears 0 times there (:22-25).
  - 1.3 `K_LINEAR=12` (multiplier on ALL melee casualties) is a fit to superseded output where the loser routed at ~58% casualties vs the 15-30% historical band (:27-31).
  - 1.4 Discipline degradation misreads canon ~5x as a ratchet: canon "Total Size lost this turn > current Discipline", code uses cumulative loss since start (`core/state.py:182-185`) (:33-37).
  - 1.5 `MORALE_EROSION_DAMP` makes the canonical -3 cap effectively 2.1 while the comment still asserts -3 (`core/state.py:111`) (:39-42).
  - 1.6 converging bodies are divided by 1/N exactly (`orchestration.py:541-550`): N subunits converging on one target deal the damage of one — which is exactly envelopment geometry (:44-52).
- **Conflicts / stale:** line numbers are July 2026; the rest of the 632 lines (unverified agent items, tiers) not read.
- **Open items:** all findings after 1.6; remaining `[UNVERIFIED]` agent claims.

### .audit/2026-07-22-mass-battle-stress-test/backwards_analysis.md
- **What it is:** Backward trace of a real instrumented battle (heavy infantry Line vs cavalry Arrowhead, seed 3; 128 primitives consumed; outcome draw 64.3% vs 78.8%, 30 turns) from `winner` down to inputs, with the grid integer-snap points flagged (MB lane, 2026-07-22).
- **Status:** none; contains a verified correction. Reading: historical map of the resolution path. **Head-read (55/148).**
- **Bears on:** MB, DICE.
- **Content that matters:**
  - Layer chain: winner <- rout/attrition <- `DAMAGE_BY_DEGREE` x `CASUALTY_SCALE`/`K_LINEAR` <- `compute_degree(pool roll + sigma leverage)` <- pool = `eff_power x eff_size x POOL_QUALITY_SCALE` + `_lanchester_strength` + σ-head terms <- contact (:6-35).
  - The integer grid still sits on the causal path: `contact.py:175/292-294`, `units.py:631/1017` all `int(round())`-snap; correction: `FIELD_CONTACT=1` does NOT remove it (A/B byte-identical over 10 seeds) — there is no toggle that removes the contact grid (:37-55).
- **Conflicts / stale:** later `geometric_contact_proposal_v1.md` supersedes the diagnosis (OBB contact, Stage B+C).
- **Open items:** none beyond those documents.

### .audit/2026-07-22-mass-battle-stress-test/cannae_bait.py
- **What it is:** Probe of Cannae with the commanded bait (ED-MB-0041): the DG-2 `yielding` primitive's entry is commanded via an Order `{'yielding': True}`; `check_orders` measures subunit CENTROID to nearest enemy cell so `enemy_range:3` never fires while `enemy_range:6` does. **Head-read (6/44).**
- **Status:** none (script). Reading: historical probe.
- **Bears on:** MB.
- **Content that matters:** earlier Cannae runs never issued the yield order, which is why feigned retreat/yield showed no effect (:1-6).
- **Conflicts / stale:** targets `tests/sim/mass_battle`; live counterpart `modules/mass_battle/`.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/cannae_calib.py
- **What it is:** Calibration of a matched-granularity Cannae composition for H3 (Envelop vs Line, band decA 55-72), force and density parity at `GAUGE_TROOPS=600` @ `GAUGE_CONC`. **Head-read (6/98).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** imports `gauge_mb` from `tests/sim` and runs `python cannae_calib.py [n]` (:1-6).
- **Conflicts / stale:** none checked. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/cannae_historical.py
- **What it is:** Historically-faithful Cannae (216 BC) test: 5000 Carthage vs 8600 Rome (~1.72:1), granular Roman maniples, Carthaginian thin crescent centre + 2 deep African columns + cavalry superiority ~2:1; subunit cap 11/side; asks whether the engine reproduces an outnumbered Carthaginian win. **Head-read (6/76).**
- **Status:** none. Reading: historical probe. **Bears on:** MB, ARCS-adjacent (historical validation).
- **Content that matters:** monolith cannot be enveloped (ED-MB-0038), so Roman side is granular (:1-6).
- **Conflicts / stale:** outcome not read (see flag_ablation / historical_fidelity_readiness). **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/cell_primitive_damage_v1.md
- **What it is:** Write-up of the aggregate-smear bug and its fix: casualties computed as one scalar per subunit pair (`_octagon_dmg_mod` averaged cells' arcs) then spread by density only; fix `_octagon_cell_mods` per-cell allocation under `PC_CELL_DAMAGE=1` (ED-MB-0040, 2026-07-24).
- **Status:** "BUILT + GATED OFF (`PC_CELL_DAMAGE=1`), byte-exact when off. Measured, not yet default." **Head-read (55/337).**
- **Bears on:** MB.
- **Content that matters:**
  - Jordan directive: "the cell is the primitive", "damage is supposed to be done to cells", "damage only being emitted by cells in direct contact" (:4-6).
  - Aggregate smear made monolithic subunits near-unbreakable by envelopment; ED-MB-0038 and ED-MB-0039 were downstream of this (:18-26).
  - Measured: envelopment vs 3-command line side swing 41.0pp -> 15.5pp; side-symmetric avg 43.8% -> 57.8% (inside the 55-72 band) (:36-44).
  - But re-bases the whole battery: gauge 8/20 (OFF) -> 4/20 (ON); C4 93.2->71.2, H11 45.6->15.4, H10 83.3->59.6, C5 -> 100 (:46-50); ships gated OFF.
- **Conflicts / stale:** current default of `PC_CELL_DAMAGE` not confirmed (one grep for `PC_CELL_DAMAGE =` found nothing at module level) `[UNVERIFIED]`.
- **Open items:** whether to flip default and re-fit bands (the "why ships gated off" section not read).

### .audit/2026-07-22-mass-battle-stress-test/close_ranks_probe.py
- **What it is:** ED-MB-0028 effect probe: does cell-level close-ranks (rear fills front-cell density) change outcomes, moderately-deep column vs wide-shallow line at equal troops and density, flag off vs on via subprocess. **Head-read (6/46).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** flags are import-time, so A/B requires a fresh subprocess per setting (:1-6).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/cluster_probe.py
- **What it is:** Envelop-cluster measurement with matched 3-command (wing-centre-wing) defenders at constant density and force parity; reports decA vs band. **Head-read (6/54).**
- **Status:** none. Reading: historical probe (ED-MB-0038 matched command-granularity). **Bears on:** MB.
- **Content that matters:** plain Line/Arrowhead opponents are matched to 3 commands because the enveloper is already a 3-body composition (:1-4).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/depth_factorial.py
- **What it is:** 24-line script importing `gauge_mb` and `cannae_calib` for a depth factorial. **Head-read (6/24); no docstring.**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** no purpose line; companion to depth_probe.py.
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/depth_probe.py
- **What it is:** Depth-vs-width probe at equal troops and 100/cell density: does depth earn reserve/staying-power value, or is frontage pure-width (with `MB_FRONTAGE_BLEND=0` the wide line wins)? **Head-read (6/51).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** tests a capped-frontage deep column; ties to ED-MB-0028 close-ranks and the frontage blend flag (:1-8).
- **Conflicts / stale:** none. **Open items:** result not read.

### .audit/2026-07-22-mass-battle-stress-test/dg6_friction_resolution.md
- **What it is:** DG-6 resolution: scale-invariant combat friction (per-battle CEV) to fix mass-battle over-decisiveness (ED-MB-0016, Jordan-directed 2026-07-22).
- **Status:** "PROPOSED (grounded + calibrated + gauge-validated)". **Head-read (30/160).**
- **Bears on:** MB, DICE.
- **Content that matters:**
  - Root cause is mathematical: summing N independent per-soldier dice self-averages (CV ~ 1/√N: N=4 0.89, 16 0.49, 64 0.25, 256 0.12, 1024 0.06), so large battles give near-deterministic degree from force ratio alone (:17-27); cites Kingman 2002 and arXiv:1905.03122 on vanishing variance at scale.
  - It is not an implementation bug; the target is outcome bands (2:1 or envelopment advantage won ~65-83%, never certain).
- **Conflicts / stale:** relates to gauge D1 amplifier and later `MB_FRICTION_CEV` flag in flag_ablation.py. **Open items:** remainder not read.

### .audit/2026-07-22-mass-battle-stress-test/envelop_probe.py
- **What it is:** Phase 1.5 diagnostic: do H3 envelop wings reach the enemy flank/rear, and does multi-side shock ever become eligible (>=2 distinct faces on one atom in a tick)? Monkeypatches `resolve_engagements_cascading`. **Head-read (6/87).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** replicates `_atom_sides` before the cascade split drops it (:1-5).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/envelopment_stability_diagnosis_v1.md
- **What it is:** Root-cause of the H3/H10 side asymmetry that survived matched command-granularity (ED-MB-0039, 2026-07-24).
- **Status:** "DIAGNOSTIC + engine-design fork flagged for Jordan." **Head-read (30/88).**
- **Bears on:** MB.
- **Content that matters:** H3 70.7% but reverse row H10 83% for the line (band 28-45): enveloper wins ~71% as A, ~17% as B (~54pp swing); not RNG-stream, not simple side bias (mirrors are symmetric); a deployment-chaotic knife-edge: parity centre (200 troops @ 100/cell = 2 cells) is narrower than the 3-command enemy (6 cells), start-row sweeps move the result 54->9pp, and Lanchester positive feedback amplifies; side-symmetric average ~44% (:7-30). H3's 70.7% is "the favourable side of the chaos, not a robust edge".
- **Conflicts / stale:** superseded in part by cell_primitive_damage_v1 (which damps the swing 62%). **Open items:** engine-design fork for Jordan (rest not read).

### .audit/2026-07-22-mass-battle-stress-test/envelopment_stability_probe.py
- **What it is:** Probe backing ED-MB-0039: shows pure-infantry envelopment is deployment-chaotic (70% as A, ~17% as B), that a deep-narrow centre stabilises the swing 51->~7pp but loses, etc. **Head-read (6/60).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** three facts listed in docstring (:1-9).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/fable_logic_audit_v1.md
- **What it is:** Five Fable-tier read-only auditors, one per logic lane (resolution, rout/morale, cell/frontage/geometry, orders/movement, gauge/harness); Part A = defects introduced in-session (ED-MB-0027..0032), Part B = deep pre-existing bugs (MB lane, 2026-07-24).
- **Status:** Part A "ALL FIXED (ED-MB-0033, 2026-07-24)". **Head-read (30/175).**
- **Bears on:** MB, PROCESS (self-introduced defects).
- **Content that matters:**
  - A1 CRITICAL: routing `make_unit` through `build_army` silently changed gauge cavalry Power 4->5, contaminating C-row verdicts (n=60: C1 45.6 IN/C2 48.3 OUT with P5; C1 11.7 OUT/C2 3.3 IN with P4); A2 `gauge_run.py` dropped both guards (:15-28).
  - Honest re-measurement: baseline 5/20, +stochastic rout 6/20; the earlier 8/20 was inflated (:11-13).
  - Every `PC_*` gated branch keeps byte-exactness (bat.py 4/4 modes) (:9-11).
- **Conflicts / stale:** Part B findings not read. **Open items:** Part B ratification list.

### .audit/2026-07-22-mass-battle-stress-test/fiat_register_v1.md
- **What it is:** Fiat register: every hardcoded value/table/clamp/scripted recipe interfering with emergence, from a 9-agent adversarial sweep plus live `gauge_mb.py` run (6/20 multi) (MB lane, 2026-07-23).
- **Status:** "AUDIT (adversarial, 2026-07-23)". **Head-read (30/348).**
- **Bears on:** MB, CORE (game-path reachability), PROCESS (scripting drift).
- **Content that matters:**
  - Biggest fiat (§0b): the strategic engine the game actually calls, `resolve_mass_battle` via `_faction_to_unit`, collapses every faction to an identical shell (Line, tier 2, command 4, discipline 5, morale 5, one subunit) differing only by `power=int(round(faction.Mil))`; one 18-tick skirmish; ignores terrain; buckets by hardcoded 0.75/0.50/0.25 cutoffs — troop composition, formation, tactics, terrain differentiate nothing (:20-31). The field engine is real but not wired to the game.
- **Conflicts / stale:** this is the single most important statement for the MB and CORE audits about what reaches the player; verify against `engine/season/` how battles are resolved `[UNVERIFIED]`. **Open items:** the per-layer fiat entries (:30-348) not read.

### .audit/2026-07-22-mass-battle-stress-test/flag_ablation.py
- **What it is:** Leave-one-out flag ablation on the historical Cannae OOB with `MB_FRICTION_CEV` pinned ON; baseline = all boolean flags ON; reports each flag's effect on the outnumbered side's win rate averaged over both deployment sides. **Head-read (6/60).**
- **Status:** none. Reading: historical instrument. **Bears on:** MB.
- **Content that matters:** a flag whose removal HURTS is load-bearing; one whose removal HELPS is costing the historical result (:1-5).
- **Conflicts / stale:** result not read. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md
- **What it is:** Steering surface for the multi-stage effort: Part-A flips + Part-B fixes + per-troop damage model, under Jordan's "implement all proposals. nothing is golden here" (2026-07-24).
- **Status:** "PROPOSED (steering surface ...)". **Head-read (30/150).**
- **Bears on:** MB.
- **Content that matters:** regime inversion: the 20-row Dupuy/Sabin honest gauge becomes the primary correctness oracle, goldens (`bat.py`) become a re-recorded regression snapshot, every `PC_*` flag is kept for A/B, each stage its own small PR with independent critic and ED-MB ledger entry (:9-20); per-troop emission = f(weapon[troop_type], quality, intent defend<->aggress, morale) (:24-30).
- **Conflicts / stale:** the "byte-exact golden constraint lifted" contradicts earlier fix notes that preserved byte-exactness; CLAUDE.md §7 says say plainly when re-recording a golden. **Open items:** stage list not read.

### .audit/2026-07-22-mass-battle-stress-test/gauge_run.py
- **What it is:** Full honest-gauge runner with configurable flags (env, import-time): runs the 20-row battery in multi mode and reports pass/OUT. **Head-read (6/26).**
- **Status:** none. Reading: historical instrument (and, per fable audit A2, once dropped the verdict guards). **Bears on:** MB.
- **Content that matters:** validation-loop closure harness (:1-4).
- **Conflicts / stale:** A2 fixed per ED-MB-0033. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/geometric_contact_proposal_v1.md
- **What it is:** Design to de-grid the field engine: geometric contact + weapon reach (Jordan design, 2026-07-22, from the ED-MB-0011 stress test).
- **Status:** "PROPOSED". **Head-read (30/95).**
- **Bears on:** MB.
- **Content that matters:** `CELL_RADIUS=0.5` (cell is a disc diameter 1.0); the live contact decision is already float geometric (`_find_contacts_standoff`: `hypot <= standoff_from_reach`, standoff = (CELL_RADIUS+reach_a)+(CELL_RADIUS+reach_b)); integer cell ids survive in only the engaged-cell recording (`contact.py:292-293`) feeding casualty column matching and `_lanchester_strength` frontage; the integer contention path is dead on the field path (`resolve_cross_side_contention` returns 0 when `FIELD_MOVEMENT`) (:9-32).
- **Conflicts / stale:** supersedes the contact-grid claim in backwards_analysis.md; Stage B+C (OBB) landed as ED-MB-0012. **Open items:** none read.

### .audit/2026-07-22-mass-battle-stress-test/granularity_probe.py
- **What it is:** Tests whether the H3/H4 envelopment inversion is a unit-granularity artifact: a monolithic 600-troop defender dilutes flank/rear damage and never routs while the enveloper's 200-troop subunits rout piecemeal. **Head-read (6/48).**
- **Status:** none. Reading: historical probe (led to ED-MB-0038). **Bears on:** MB.
- **Content that matters:** hypothesis that splitting the defender into N subunits lets outer subunits rout and cascade (:1-6).
- **Conflicts / stale:** confirmed later (cell_primitive_damage_v1 says ED-MB-0038 was a workaround for the smear). **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/hierarchical_units_investigation.md
- **What it is:** Investigation of how the engine realises cells -> subunits -> army, mapped to the Football Manager / Total War paradigm, with an honest implemented/emergent/gap read (Jordan-directed, 2026-07-22).
- **Status:** none (investigation). **Head-read (26/108).**
- **Bears on:** MB, CHAR (decision layer analogue).
- **Content that matters:** Cell = `(orig_r, orig_c)` slot with `cell_troops` and `cell_facing_vec` at continuous field position (no snapping on the live path); Subunit (`hierarchy.units.Subunit`) carries shape/instructions/stance/role/troop_type/tier/orders; Army (`Unit`) carries subunits[], stance, command, morale; cell count emergent from troops/density with `CELL_FLOOR(40)..CELL_CAP(200)` troops per cell; `PC_NODE_COHESION` holds formation (:8-26).
- **Conflicts / stale:** none checked. **Open items:** gaps section not read.

### .audit/2026-07-22-mass-battle-stress-test/historical_fidelity_readiness.md
- **What it is:** Consolidated audit and roadmap on whether the field engine can reproduce Cannae, Leuctra, Gaugamela, Zama (five critics + architecture, granularity, capability-vocabulary, ratified-but-unbuilt sweeps, full-campaign gauge A/B) (2026-07-23).
- **Status:** none. **Head-read (26/118).**
- **Bears on:** MB, ARCS-adjacent (historical validation).
- **Content that matters:** verdict: primitives and aggregation spine are sound and cell-up; the ceiling is (a) three missing capability layers needed to STAGE the battles and (b) the DG-6 variance structure; maneuver goals (`_envelop_goal`, `_sweep_goal`) are hardcoded two-waypoint state machines (scripting drift) while octagon multi-side shock was fixed by ED-MB-0019 (:7-26).
- **Conflicts / stale:** none. **Open items:** roadmap not read.

### .audit/2026-07-22-mass-battle-stress-test/honest_gauge_readout.md
- **What it is:** Measurement-integrity readout: the gauge's #1 distortion M1 (per-cell density mismatch between plain and composed deployment paths) fixed by holding `GAUGE_CONC=100` and `GAUGE_TROOPS=600` across every unit (ED-MB-0027, 2026-07-23).
- **Status:** "DIAGNOSTIC (the gauge now flags engine divergence honestly; bands NOT re-fit)". **Head-read (26/221).**
- **Bears on:** MB.
- **Content that matters:** the ~8x density gap, not flanking geometry, drove envelopment rows to 100%; null test (dense vs thin line, zero envelopment) already reproduced 100% (:9-17); integer-cell quantisation exact because every split divides by 100; the gauge is a manual harness (no `test_` functions, not a CI gate) (:25-29). Fable audit later found ED-MB-0027 itself introduced a P4->P5 cavalry change, so this readout's C-row verdicts were corrected.
- **Conflicts / stale:** see fable audit A1. **Open items:** none read.

### .audit/2026-07-22-mass-battle-stress-test/intent_probe.py
- **What it is:** ED-MB-0029 intent-as-resolution probe: matched-density mirror lines under different stance pairings, `MB_INTENT_RESOLUTION` off vs on. **Head-read (6/56).**
- **Status:** none. Reading: historical probe. **Bears on:** MB, CHAR (intent concept).
- **Content that matters:** expected with intent ON: hold-vs-hold slow low-casualty standoff, aggressive-vs-aggressive fast and bloody, aggressive-vs-hold holder survives longer (:1-8).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/mb_fieldbased_stress.py
- **What it is:** Field-based stress harness for the active engine `tests/sim/mass_battle/` under `FIELD_MOVEMENT=1 / MB_NODE_COHESION=1 / PER_CELL=1` (2026-07-22). **Head-read (14/321).**
- **Status:** none. Reading: historical instrument (the engine under test described as "more-developed ... NOT the wired-but-thin massbattle.py bare port"). **Bears on:** MB.
- **Content that matters:** emits JSON per scenario with `--emit`, consumed by run.py; gates read from os.environ once at import (:1-12).
- **Conflicts / stale:** path now `modules/mass_battle/`. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/octagon_damage_model.md
- **What it is:** Octagon facing as a damage-RECEIVED multiplier (ED-MB-0018), implemented DEFAULT ON, field goldens re-recorded (2026-07-23).
- **Status:** "implemented, DEFAULT ON, field goldens re-recorded." **Head-read (26/179).**
- **Bears on:** MB.
- **Content that matters:** Jordan's three requirements: attacks from behind do ~twice the damage; cells cannot turn instantly (a couple of ticks); multi-side attack is extra bad (shock/distraction, not divide-by-two) (:7-17); previously `ANGLE_DEF_MOD={GREEN:0, YELLOW:-1, RED:-2}` fed the dice pool/sigma head (~a third fewer successes, too weak); octagon zone GREEN <45°, YELLOW 45-90°, RED >=90° (:19-24).
- **Conflicts / stale:** the fiat audit found a fabricated "octagon" citation to `mass_battle_v30.md §A.3b`. **Open items:** none read.

### .audit/2026-07-22-mass-battle-stress-test/orphaned_mechanics_audit_v1.md
- **What it is:** Inventory of built-but-dead mass-battle code with wiring status, under Jordan's "built work is ratified and wired by default" (2026-07-24).
- **Status:** none. **Read in full (47 lines read to :26 plus table; head-read 26/47).**
- **Bears on:** MB, PROCESS.
- **Content that matters:** `perimeter.py` WIRED via ED-MB-0035 into `_envelop_goal`; dead data seeds `provenance.py`; standalone `lanchester_signature.py`, `validators.py`; dead mechanics: `PC_ENVELOP_SIGMA=0.0` hardcoded DISABLED (computed each tick then x0; naive enable rewards the defender, C7 100->20), `PC_FACING_MODEL` family dead by default with explicit "do not enable" calibrated-debt tag (:5-26).
- **Conflicts / stale:** `modules/mass_battle/perimeter.py` exists (matches). **Open items:** `PC_FACING_MODEL` flagged for Jordan.

### .audit/2026-07-22-mass-battle-stress-test/pathing_deployment_diagnosis.md
- **What it is:** Diagnosis that multi-unit formations are geometrically wrong (Jordan-flagged from the hierarchy snapshot) (2026-07-22).
- **Status:** none. **Head-read (26/125).**
- **Bears on:** MB.
- **Content that matters:** `build_army` places subunit `i` at `(start_row, 15+i*4)`: a rightward column-of-columns, so both envelopment wings sit to the RIGHT of the centre (no left wing) and `_envelop_goal` sends both around the same flank; col-spans overlap once width exceeds the 4-col step (:1-27).
- **Conflicts / stale:** fix status not read (ED-MB-0038..0041 later changed deployment). **Open items:** none read.

### .audit/2026-07-22-mass-battle-stress-test/perimeter_targeting_geometry_v1.md
- **What it is:** Spec of perimeter target-points and face normals as the geometric backbone for targeting, approach, contact and octagon facing (Jordan ruling 2026-07-23, from a hand-drawn model).
- **Status:** "SPEC / PROPOSED (un-built)" (since wired as `perimeter.py`, ED-MB-0035). **Head-read (26/87).**
- **Bears on:** MB.
- **Content that matters:** major target points = face midpoints with outward normals; minor = corners with bisector normals; the normal defines required approach angle; attackers en route can be intercepted; pointed formations (tip angle <~60°) have a vertex target (:1-26).
- **Conflicts / stale:** "un-built" is stale: `modules/mass_battle/perimeter.py` exists and orphaned_mechanics_audit marks it WIRED. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/ratified_but_unbuilt_backlog.md
- **What it is:** Exhaustive sweep of MB items classified RATIFIED-but-unbuilt, PROPOSED-not-ruled, built-not-ratified (2026-07-23).
- **Status:** none. **Head-read (26/81).**
- **Bears on:** MB, FA (faction tactic cards), CORE (Stage G).
- **Content that matters:** A1 waypoint primitive + `0.5*speed*max-ticks` path-length budget (ED-1096/ED-MB-0001) not enforced; A2 Stage G / P-DEC-2: route `resolve_mass_battle` + `faction_action` onto the field engine and retire the integer engine, not started; A3 multi-unit Path B (N-on-1) never started; A4 DG-2 emergent auto-yield/rally/pocket exit only commanded entry shipped; A5 Faction Tactic Cards §B.4: `FACTION_TACTIC_CARD_POOL_MODIFIERS = {}` empty stub; A6 Reserve formation Phase-3-commit rule has zero consuming code; A7 Feigned Retreat zero code (:20-30). "Nothing here is a shipped-and-broken player-facing feature: the whole spatial engine isn't live in the game path yet" (:14-15).
- **Conflicts / stale:** `ratified_unimplemented_register.md` said MB had no qualifying items — this file contradicts it (different date, deeper sweep). **Open items:** A1-A7 and rows below.

### .audit/2026-07-22-mass-battle-stress-test/reachability_sweep.py
- **What it is:** ED-MB-0041 sweep: for each failing gauge row, can ANY setting of the engine's toggles move it into its band? Rows invariant to every toggle are blocked by structure, not constants. **Head-read (8/254).**
- **Status:** none. Reading: historical instrument; the method is reusable. **Bears on:** MB, DICE.
- **Content that matters:** distinguishes "needs fitting" from "missing mechanism" per row (:1-8).
- **Conflicts / stale:** results not read. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/reface_probe.py
- **What it is:** Confirms the persistent-defender-reface hypothesis for envelopment over-decisiveness by slewing contacted defender cells' facing toward the nearest attacker each tick (variant A unconditional, B only if threat not in rear arc). **Head-read (6/74).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** hypothesis: flank reface drops H3 toward 55-72 while cavalry rear attacks (unrefaceable) stay near-total (:1-6).
- **Conflicts / stale:** relates to dead `PC_FACING_MODEL`. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/results.json
- **What it is:** Machine-readable output of the field-based stress run (S0 wiring census with 30 registered mechanics, field triad, on_flags list, further sections) (2026-07-22). **Head-read (first 700 bytes of 641 lines).**
- **Status:** none (data). Reading: historical artifact.
- **Bears on:** MB.
- **Content that matters:** `selftest_ok: true`, `n_mechanics: 30`, `field: {FIELD_MOVEMENT, PC_NODE_COHESION, PER_CELL}` all true, `on_flags` includes `LANCHESTER_ENABLED`, `POOL_QUALITY_MODEL`, `COMMAND_SIGMA_ENABLED`, `MORALE_FIX`, `SIGMA_HEAD_ENABLED`, `VOLLEY_ENABLED`, `CASCADING_ENABLED`, `PC_BRACE_*`, `PC_RECOIL_*`.
- **Conflicts / stale:** flag set snapshot 2026-07-22; defaults changed since (PC_CELL_DAMAGE etc.). Read by nothing (an audit artifact). **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/reverse_pair_symmetry.py
- **What it is:** ED-MB-0041 reverse-pair symmetry invariant: run an asymmetric matchup in both orientations; distinct from mirror symmetry (which passes: H1 50.0, C3 50.8); "the cheapest invariant the gauge has, and it fails today". **Head-read (6/117).**
- **Status:** none. Reading: historical instrument; same idea as the wave-1 recommendation of a standing shape-and-side-swap diagnostic. **Bears on:** MB, DICE.
- **Content that matters:** a mirror probe is structurally blind to side-dependent interaction defects (:1-6).
- **Conflicts / stale:** none. **Open items:** the failure itself (E2 Arrowhead asymmetry lineage).

### .audit/2026-07-22-mass-battle-stress-test/rotation_model_v1.md
- **What it is:** Parse-back and build plan for Jordan's two-tier troop rotation + recovery directive, plus foundational primitive landed (ED-MB-0028) (2026-07-23).
- **Status:** none. **Head-read (26/110).**
- **Bears on:** MB.
- **Content that matters:** T1 intra-subunit cell backfill + coverage shrink (rear cells fill engaged cells to prescribed density; coverage shrinks when minimums unmet); T2 inter-subunit rotation via blended cell exchange; losses are not all deaths so recovery of troop count is needed to make rotation worthwhile (:5-26).
- **Conflicts / stale:** none. **Open items:** T2/T3 build not read.

### .audit/2026-07-22-mass-battle-stress-test/rout_probe.py
- **What it is:** ED-MB-0031 stochastic-rout probe: casualty-at-rout and battle length with `MB_STOCHASTIC_ROUT` off/on; target loser breaks at ~15-30% casualties, not ~58%. **Head-read (6/52).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** the 15-30% band is Jordan's historical research figure (:1-4); contrasts with the K_LINEAR fit to a 58% rout trajectory flagged in the deep audit.
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/run.py
- **What it is:** Driver for the field-based stress test S0-S5: wiring census, flag A/B isolation (fresh subprocess per env because gates read os.environ once at import), off-by-default activation, report print. **Head-read (6/329).**
- **Status:** none. Reading: historical instrument. **Bears on:** MB, PROCESS.
- **Content that matters:** the import-time flag pattern is why the byte-exact CI test also uses subprocesses (:1-6).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/run_log.txt
- **What it is:** Printed output of run.py (S0 wiring census table: mechanic, fn, toggle, live, status; mechanics_selftest ok=True, 30 registered mechanics; field-based=True, grid-oracle-active=False). **Head-read (12/175).**
- **Status:** none (log). Reading: historical artifact. **Bears on:** MB.
- **Content that matters:** rows like `cell_layout oriented_pattern None (always) WIRED`, `octagon_facing octagon_angle None (always) WIRED`.
- **Conflicts / stale:** snapshot of 2026-07-22. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/side_face_probe.py
- **What it is:** Does the enveloper's wing wrap work in both orientations? Report the defender-struck faces when the enveloper is side A (advance_dir -1) vs side B (+1); if only FRONT as B there is a directional wheel pathing bug. **Head-read (6/59).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** side-specific pathing hypothesis (:1-4); result superseded by the ED-MB-0039 knife-edge diagnosis (geometry mirror-identical, casualty exchange not).
- **Conflicts / stale:** none. **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/side_probe.py
- **What it is:** Isolates the envelopment side asymmetry: same two armies, swap A/B, same seeds. **Head-read (6/27).**
- **Status:** none. Reading: historical probe. **Bears on:** MB.
- **Content that matters:** if the engine were side-symmetric the enveloper's decisive win rate would match (:1-2); established in ED-MB-0039 that army construction does not consume `random`, so not an RNG-stream artifact.
- **Conflicts / stale:** none. **Open items:** none.

## Cross-subsystem leads

- **MB + CORE (what reaches the player):** `fiat_register_v1.md` §0b says the game-path `resolve_mass_battle` collapses every faction into an identical single-subunit shell differing only by `power=round(Mil)`; `ratified_but_unbuilt_backlog.md` A2 (Stage G: route the field engine into `resolve_mass_battle`/`faction_action`) is "not started" and "the whole spatial engine isn't live in the game path". An MB or CORE audit should test by execution how `engine/season/` resolves a battle today before crediting any of the field-engine findings as player-facing.
- **SC + FA + SE (consequence spine):** `interface_report_v1.md` (SC lane) names the open seam that a contest verdict touches no faction or settlement state (ED-SC-0007, party-derivation bridge for settlement stats); `stress_test_synthesis_v1.md` and `44_standing_institutions.md` show the same seam from the SE/FA side (Pattern H: Mandate saturation hides collapse; Standing/resolution_quality Keys, not Mandate, are the real cross-scale carrier). SC, FA and SE lanes need one agreed carrier.
- **FA + SE + CHAR (rank ladder and NPC advancement):** `40_roster_officer_system.md` proposes NPCs climbing the same Standing ladder as the player with a `power_base` enum, and `44_standing_institutions.md` finds the demotion spiral (A, E, G) is the one universal doom-loop no institution can break (needs substrate tuning: survivable Appeal Ob, failure-retiring successes, defined Suspicion->Recall constant). CHAR and the NPC-chooser lane should read both together.
- **DICE + SE/FA:** `44_standing_institutions.md` §44.9 and `stress_test_synthesis_v1.md` §0.4 report that the deck's legible `d_sigma` odds (50% + 10%/pt) diverge from the canonical normal-CDF `p_success`; `ground_truth_odds.md` gives the tables; no character attribute block existed in any seed, so pool sizes were engine-assigned (CHAR gap).
- **PC + MB (shared structure):** the PC half-sword liability is a symptom of reach over-weighting (`stress_test_findings.md`), the MB analogue is the Lanchester/amplifier family (`README.md` of gauge audit D1). Both audits found that single-knob fixes fail and a joint recalibration against target bands is the real task, and both stalled on "I cannot invent the target win-rate bands" (design call for Jordan).
- **WR + CORE (narrative engine):** the Emergent Narrative Engine design (`_workings_joined.md`, `narrative_engine_design_v1.md`) assumes the retired Key substrate; its goals (convergence detection over settled state at the Accounting boundary, subtract-only director, no arc labels surfaced, total accounting) are the right test for whatever `engine/season/` has. The ARC-S07 Torben Loyalty range conflict (register 8->0 vs `clock_registry_v30.md` 0-7 start 3) bears on ARCS.
- **PROCESS:** `ratified_unimplemented_register.md` and `adversarial_deep_audit_v1.md` §1.1 both describe provenance-laundering/blindspot failure modes (bare-integer ledger citing the engine file; no index of ratified-but-unbuilt work). The first looks fixed (ED-MB-0041 Tier-0.1); the second's proposed generator tool is not confirmed built.

## Likely stale or superseded

- `u9_capstone_v1.md` (self-declared SUPERSEDED by U10, ED-PC-0022; `modules/combat/config.py:55` has `LEGIB_EDGELINE_K=0.04`) and the K=0 byte-identity claims in `u9_adversarial_review_v1.md`.
- `tier3_proposal_status_closure.md` :28 "the `reeval/` directory is empty" and `00_index.md` :45 — the four `reeval_*` fragments exist in the compendium `_workings_joined.md`.
- `perimeter_targeting_geometry_v1.md` "SPEC / PROPOSED (un-built)": `modules/mass_battle/perimeter.py` exists and the orphan audit marks it WIRED (ED-MB-0035).
- `adversarial_deep_audit_v1.md` §1.1 (verification ledger laundering): the working tree notes the self-whitelist file was deleted in ED-MB-0041 Tier-0.1.
- `interface_report_v1.md`, the governance compendium, `stress_test_synthesis_v1.md`: all cite `sim/...` (dissolved) as the built substrate; `ED-SC-0002` is `resolved` in `registers/editorial_ledger_sc_archive.jsonl:2`, not Jordan's open P0.
- The combat stress-test scripts and the gauge audit cite `systems/combat/combat_engine_v1` and `tests/sim/mass_battle` paths; live heads are `modules/combat/` and `modules/mass_battle/`.
- Emergent Narrative Engine `integration_with_ners_audit.md`, `narrative_engine_design_v1.md`, `_workings_joined.md`: Key-substrate based (RETIRED, ED-IN-0232).
- `stress_test_findings.md` finding G2 (self-retracted) and the "5 distinct context-leaders" claim (self-retracted).
- Still live at the working tree per one grep each: `HALFSWORD_FORM` (`modules/combat/weapons.py:926`), `recalc_size` aggregate-floor force-rout (`modules/mass_battle/hierarchy/units.py:2982`, no sibling guard visible), `K_LINEAR` env default 12 (`modules/mass_battle/config.py:512`), `MORALE_EROSION_DAMP=0.7` now tagged CALIBRATED-DEBT.

## Items that could change an audit finding

- **F-PC (U10/levers):** whether the six morphology levers are active (LEGIB_EDGELINE_K=0.04 is) and whether the D2 `test_thrust_protection_grip_invariant` still holds; the test-hygiene hazard (shared `weapon_physics.CHOKE_THRUST_K` global leaking from `test_combat_choke.py`) may still mask a D2 break.
- **F-PC half-sword:** the switch is a net liability for longsword/estoc/greatsword/flamberge (activation HELD, ED-PC-0016; PC-5 `thrust_authority` fixed the longsword case to 38->73% at both-heavy); remaining open: Phase-C target bands, poleaxe spike-vs-plate selection, PoB_frac/heft ordering, G1 cutting-polearm affordance cliff (guandao 96% vs bardiche 9.6%), agility dominance (+30..34pp marginal).
- **F-MB density/amplifier:** E1 Lanchester-density artifact (reversal-proven) and D1 resolution exponent p~3.2 vs <=1.4; later mechanisms ED-MB-0016 (friction CEV), ED-MB-0038/39/40 (matched granularity, deployment chaos, cell-primitive damage; gauge 8/20 -> 4/20 under `PC_CELL_DAMAGE=1`); honest baseline 5-6/20 after ED-MB-0033. Any MB finding should re-run `gauge_mb.py`, not rely on the 7/20 of 2026-07-08.
- **F-MB unbuilt/drift:** Stage G (game path onto field engine) not started; Faction Tactic Cards empty stub; Reserve rule and Feigned Retreat zero code; `PC_ENVELOP_SIGMA=0.0` and `PC_FACING_MODEL` dead by default; `recalc_size` cascade; 1/N convergence division (`orchestration.py:541-550`); Discipline degradation uses cumulative rather than per-turn loss; fabricated octagon citation.
- **F-SC/FA/SE interface:** contest verdict does not reach settlement/faction state; Compact vs Leverage vs Charter tag-family mismatch with built `ledger.py` `TAG_KINDS`; `assessed_base` field absent from built Settlement; Local-Actor representation three-way inconsistent; settlement-type taxonomy 8 vs 11 (Village undefined); Seggio lock with no governance-scale seizure resolver; §1.3a Survey/Compact deterministic below-subsistence strip; Π R-4 cliff with no relief valve; Appeals 0/6; Suspicion->Recall constant undefined; Mandate saturation formula `clamp(round(7T/(T+6)))`.
- **F-WR narrative:** ED-IN-0003/0004 "closed by design" are not executing; Torben Loyalty 8 vs 0-7 start-3; ED-609, ED-1009, Certainty-in-bake-key swing; Certainty register table covers 5 rows with Certainty 0 uncovered and an out-of-range "6+"; faction count ranges 4-8 depending on doc; arc register is 138 entries (not ~110).
- **F-DICE:** legible vs engine `d_sigma` odds contract; agents under-estimated `P(net>=3)` on 7D TN7 by 5-7 points (truth 55%).

## Coverage summary (for the orchestrator)

Entries written for all 75 assigned files, but depth varies and is stated per entry. Read in full: both U9 files, `integration_with_ners_audit.md`, `narrative_engine_design_v1.md`, `interface_report_v1.md`, gauge `01_wave1_synthesis.md`, `02_wave2_synthesis.md`, `README.md`, `comparative_governance_research_v1.md`, `00_index.md`, `43_directive_types.md`, `44_standing_institutions.md`, `tier4_discovered_open_work.md`, `stress_test_synthesis_v1.md`, `ground_truth_odds.md`, `pc2_halfsword_expansion.md`, `ratified_unimplemented_register.md`, `stress_test_findings.md`. Partially read (stated): narrative `_workings_joined.md` (about 40%), compendium parts 40, 41, 42, 45, tier3, compendium `_workings_joined.md`, `appendix_B_roll_failures.md`, settlement `_workings_joined.md` (index only), all six combat `.py` (header only), and the whole MB stress-test directory (heads only).
