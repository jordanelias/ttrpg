# Digest auditB3

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: auditB3. Corpus: `.audit/` (archived-not-canon, lesser weight than `.designs/`; context and referents only). Every file below is a generated join (`tools/join_audit_workings.py`) or a working paper of a July 2026 audit; every old finding is a lead, not a fact.

### .audit/2026-07-05-emergent-narrative-engine/_workings_joined.md
- **What it is:** generated verbatim join (`tools/join_audit_workings.py`, 43 fragments, 10,678 lines, read in full) of the 2026-07-05 "emergent narrative engine" design effort (lane IN, branch `claude/ners-audit-fable5-9cpfdz`; 25-agent workflow `wf_f9afc9b0-703`): charter (:19-200), three groundings (:202-455), manifest (:457), architectures A/B/C (:482-1513), completeness critic (:1515), dossiers (:1729-3638), drafters' notes (:3640-3983), judges (:3985-4503), v1 refutes (:4505-5168, 6142), v2 "churn" refutes (:5170-6140), spec sections s1-s5 (:6312-9767), synthesis (:9769), verifiers (:10088-10581), churn amendments (:10583).
- **Status:** every fragment "SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05)"; the churn_amendments fragment itself says RATIFIED (:10586). Reading: historical. Its whole mechanism sits on the Key substrate, Domain Echo and emit/consume interface, which are RETIRED (ED-IN-0232), so none of it is buildable as written. Its problem statement (Q1-Q4, C1-C7), defect lists and census figures remain usable referents.
- **Bears on:** WR, ARCS, CORE, CHAR, FA, SC, DICE (determinism), GO (render/bake)
- **Content that matters:**
  - The charter's measuring stick: Jordan's four questions (player affects world / world affects player / events legible as narrative / narratives present) and hard constraints C1-C7 (:36-60), incl. C2 (no narratological surfacing; the 2026-04-30 doc-12 veto: "real life doesn't tell you you are now in the Rising Action", :382-384) and C7 (never railroads: pricing over gating, foreclosure only via arc events, windows real). Twelve capstone requirements incl. a factionless PC getting playable seasons (:172-183).
  - Arc register census (:1899-1950): 138 arc entries not ~110 (clocks 7, threads 8, territory 29, factions 81, events 13); sampled 24 collapse to ~13 structural shapes (range 12-15). Register defects: ARC-T04 "Southernmost Ritual" is a dangling ID (cited at arc_register_territory.md:33 and arc_register_events.md:38, defined nowhere; the cited ED-416 resolves to two unrelated ledger rows, :3146-3154); Coup Counter STRUCK by ED-781 with no remap to the four-stage Löwenritter Autonomy track (:3136-3144); Axis 9 Pressure has no clock (:3156); TC/RS legacy names for CI/MS; Torben Loyalty range conflict register 8-to-0 vs clock_registry 0-7 start 3 (:10375-10382).
  - Formalizability finding (:3099-3120): about 45 percent of register arcs compile to a typed vector now, 40 percent need one new field (a per-arc lifecycle state, "the concrete form of ED-IN-0003"), 15 percent are GM-judgment-irreducible (ARC-P05, ARC-S29, ARC-T06, NPC-ARC-JAR, ARC-S52, ARC-S56; :5688-5699). Proposed `arc_vector` schema at :877-901 and :7234-7265.
  - Winner of the three architectures: B arc-vector engine (judges 85/84/82 on three lenses, :4308); grafts from A (render-trigger completion, C2 lint) and from C (rationing, texture as demotion destination, watching/participating counters). A's honest verdict: eight COLLISION markers are a whitelist, not a discriminator (:779-786).
  - Determinism hazards the refutes found (:4535-4717, 5190-5342): a `set()` gating convergence emission order is a second ORD-2 violation; Top-N rationing needs a total-order tiebreak (salience DESC, tier_rank, id ASC); cosine 0.40 and float products need integer or fixed-point arithmetic pinned in the port; renderer fragment selection must be zero-randomness or a dedicated sub-stream; builtin `hash()` is process-salted so seeds need sha256; integer basis points relocate rather than remove the Phi quantization boundary.
  - v2 "churn" refutes: the forecast organ reasons are Layer A analytic horizons (continuous clocks, closed form) vs Layer B sampled ensemble (discrete branches; EV-averaging a discrete branch yields a phantom half-attack, :2574-2580); per-lever cost multiplies by L (:5255-5283); a forecast that drives casting and NPC behaviour is self-fulfilling across Accountings (:5972-6017); the Light Function any-seed theorem proves legibility not plot, and engaged-thread exemption plus finite budget starves the imminence term (:5767-5838). Content figures: authored bake 230-450 units under lexicon-swap, 1,200-2,700 if Certainty gates the frozen pool; ~10^3 live Key instances per season; NPC cap about 35 active.
  - Defect-of-the-record notes: the 10-trigger articulation table omits scene.combat_resolved (an [ASSUMPTION] under ED-936), investigation_resolved and the four ED-681 Rendering-Crisis thread beats; mechanical.scene_entered double-emitter (scene_slate vs game_director) contradicts key_substrate §8.5 L510 (:4759-4776); solmund_voice §18 Certainty table has no Cert-0 row and an out-of-range "6+" (:2178-2194).
- **Conflicts / stale:** (1) everything keyed on Keys / `meta.convergence_detected` / `meta.arc_state_changed` / total-accounting-of-Keys is retired with ED-IN-0232. (2) `game_director`, `scene_slate`, `scenario_authoring` stubs still exist in `references/module_contracts.yaml` (grep: `scene_slate` :378, `game_director` :401, with the same attribution-conflict note :411) [partly live as a registry conflict]. (3) `ARC-T04` still appears only in `.audit/`, `.designs/` and the IN handoff history; I did not check `references/arcs/` presence. (4) The "director owns the tension curve" reversal to subtract-only (:8268-8278) was carried as an [OPEN - Jordan] fork by every spec section; nothing in the join records a ruling. (5) `engine/season/` now holds the real season loop (verb_table.yaml, offices.yaml, governance_spine.yaml, goals.yaml, hole_register.yaml); the join never saw it. (6) Join cites `designs/...` paths that were dissolved; they now sit under `.designs/`.
- **Open items:** Certainty-in-bake-key fork; Cert-0 register row; temporal_window for convergence; lifecycle-state ownership; the ~15 percent GM-judgment arcs (non-firing default); ERA (Expressive Range Analysis) unbuilt as the anti-oatmeal gate; per-NPC voice is a ~1,050-unit authoring line nobody budgeted; the factionless on-ramp was only demonstrated in Appendix A (:9636-9709) and COLLISION-B effect-bearing path in Appendix B (:9713-9765).
### .audit/2026-07-12-governance-compendium/40_roster_officer_system.md
- **What it is:** Part 40 of the 2026-07-12 governance compendium (lane IN, cross-cutting FA/SE/PC/MB): a preserved-in-full integration of the 2026-07-11 "rise to power / roster system" research pass (about 96 historical cases in ten categories A-J) into a proposed NPC roster/officer/advancement layer. 621 lines. [READ lines 1-390 of 621 only; see SKIPPED note]
- **Status:** "PROPOSED / provisional ... nothing here is ratified canon" (:3-9). Reading: historical reference / unratified proposal; its host docs (`governance_play_redesign_v1.md`, `faction_politics_v30.md`) are `.designs/` material and the Key types it leans on are retired.
- **Bears on:** FA, CHAR, SE, CORE (offices/rosters), PC/MB (naming collision with "officer")
- **Content that matters:**
  - Eight general power-acquisition mechanisms M1-M8 (patronage, credentialed merit, kinship, court proximity, bureaucratic chokepoint, purchased office, armed retinue, ideological authority), each carrying its own characteristic downfall shape (:18-52); the design claim is that the same field that types a rise types its exploitable vulnerability (Omega-d non-dominance, "every action pays what it buys", :240-261).
  - Proposed organising field `power_base` in {patronage, merit, kinship, bureaucratic, military, purchased, ideological}: one Accounting loop with seven drivers (:196-207) and an "Ascendancy card" menu (install successor, capture the gate, cohort capture, press a banked claim, force ratification, purge predecessor, seize Mandate custody; :209-220).
  - Shared rank space: NPCs climb the same Standing ladder as the player; Standing-substitute meters (`moral_authority`, `renown`, `shadow_standing`, `service_rank`, `mandate.custody_bonus`, `Dignity`) are bounded auxiliary scalars, not a second ladder; "can an NPC depose the player at a held rank" is a `player_seats_are_contestable` policy toggle (:92-125).
  - One engine, three scale bindings (settlement, court, lineage) via a `scale_binding` field; court binding is ladder-gated and does not need the unbuilt settlement registry; lineage binding (clan object above the single NPC; C5 Wang Mang, I10 malikane) is the biggest structural ask (:61-90, :354).
  - Naming ruling proposed: system called "Ascendancy"; roles Retainer/Patron/Advisor/Conduit/Favorite; "officer" reserved for the mass-battle unit commander (about 20 of 96 entries flag the collision; :270-299).
  - Per-entry catalogue tables A1-A9 patronage, B1-B9 merit, C1-C10 kinship, D1-D10 court favourites, E1-E4 (of 8) bureaucratic with new fields/Keys, failure dynamic and naming flags (:309-390); several answer open HAB-2 (Valido) questions (e.g. D6 answers "does the binary collapse ever soften").
- **Conflicts / stale:** relies on the Key substrate (`standing_change`, `officer_deaths`, `npc_standing_climb_attempt`, `state.succession_vacancy`, `access.correspondence_filtered`; :180-188), which is retired (ED-IN-0232). `engine/season/` now has `offices.yaml`, `rosters.yaml`, `npcs.yaml`, `governance_spine.yaml` that the proposal predates [UNVERIFIED how far they cover `power_base`]. It uses the struck "Coup Counter" (A9, I1) as a live buffer (:252).
- **Open items:** the `player_seats_are_contestable` toggle; how many parallel status/power tracks the game wants (needs_jordan item 3, :108); lineage-scope entity; D9/BYZ-8 duplicate coverage to be consolidated; a sourcing caveat on B6 (Napoleon) deferred to part 40.5 which I did not read.

### .audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md
- [SKIPPED: .audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md - my reading budget for the turn ran out after the first two files; file not opened]

### .audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md
- **What it is:** Part 42 of the governance compendium (2026-07-12, lane IN; touches FA, SE, MB, GO): a deduped, verb-grouped re-index of about 90 "Introduces (Action)" lines from the 2026-07-10 historical-concerns action catalogue (about 94 event cards, §2.1-2.10). 254 lines. [READ lines 1-130 of 254 only; remaining verb groups (Levy, Investigate, Directive, NEW bucket, §2.11 reskin clusters) not opened]
- **Status:** "PROPOSED - compiled 2026-07-12"; "none of this has been ratified into governance_play_redesign_v1.md, faction_politics_v30.md, or settlement_layer_v30.md" (:3-14). Reading: unratified catalogue; nothing newly invented.
- **Bears on:** FA, SE, GO (verb table), CORE
- **Content that matters:**
  - The parent-verb frame is eight base verbs (Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate) plus Directive (PA-issued order) and a NEW bucket for freestanding actions (:16-22).
  - Table columns Action / Extends / Mechanic / Cost / Motivating event / § (:24-32); many actions write durable Precedent or tag entries (`Rebuild-to-Code`, `route-diversified`, `Overcrowding`, `planned capital`).
  - Develop family (:42-57) pairs with the long-fuse stats in Part 45 (Dredge Harbor resets SiltLevel; Charter Reclamation Corporation plants SubsidenceRisk; Crop Substitution answers SalinityLevel; Ever-Normal Granary / Civic Granary answer drought).
  - Several actions are rank-gated or pre-bank-only: Sovereign Bargain is Standing-6+ only (:123); Alternate Corridor must be pre-banked (:122); Lighthouse unlocks only after a storm Crisis (:55); Standing Fleet gates a Defy branch (:65).
  - Consolidated rows flag same-mechanic reskins for a ratification pass (:34-38, §2.11 not read).
- **Conflicts / stale:** cites `designs/audit/...` paths (dissolved; `.designs/` or `.audit/` now). `engine/season/verb_table.yaml` exists and is the code-side verb owner; whether any of these actions are in it was not checked [UNVERIFIED; one grep of `verb_table.yaml` for "Dredge"/"Underwrite"/"Quarter" would answer].
- **Open items:** the reskin clusters (§2.11) and which proposed actions become real verbs.

### .audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md
- **What it is:** Part 45 of the governance compendium: a catalogue of eight proposed "hidden long-fuse" environmental stats distilled from the 2026-07-10 historical-concerns action catalogue §2.4-2.6 (lane IN, read-only research; 151 lines, read in full).
- **Status:** "PROPOSED - needs a granularity ruling" (:3). Reading: unratified proposal; explicitly not typed params (:151).
- **Bears on:** SE (settlement/economy), WR (environment, crises), FA (province-tier institutions)
- **Content that matters:**
  - Standing ruling it must not override: food supply and similar granular meters may ABSTRACT to Prosperity (:11); default for every stat is "folds into Prosperity/Order drift, no dedicated tracker" (:13).
  - Three-question framework for track vs abstract: cross-settlement fuse? multi-decade fuse? does institutional counter-play need a legible number (:19-27).
  - Eight stats: SiltLevel, OreGrade, SalinityLevel, SubsidenceRisk, RisingWaterLevel, FloodIndex, DroughtIndex, StockLevel, each with raise/defuse/crisis/institution/historical case (:37-123).
  - Recommendation (not ruling): track RisingWaterLevel (the defining cross-settlement case: an upstream Fortify choice silently loads a downstream Crisis the downstream governor cannot see; a local Prosperity number cannot carry it, :137); SiltLevel only where a province-tier Water Magistracy consumes it; abstract the other six; StockLevel is blocked on a binary yes/no on adopting an Ever-Normal Granary mechanic at all (:140, :142).
  - SubsidenceRisk is the one stat with no institutional defuse (only an upstream method choice; :78).
- **Conflicts / stale:** cites `designs/...` paths now under `.designs/`; "Crisis", "Grudge", "Standing", "Sponsor/Fortify/Develop" are settlement-ambition-engine verbs from `governance_play_redesign_v1.md` (a proposal) [UNVERIFIED whether `engine/season/` has equivalents]. Settlement count/registry gate not re-checked.
- **Open items:** the granularity ruling itself; whether any cross-settlement hidden-debt mechanism exists in `engine/season/` (one grep for `rising`/`siltation` was not run).

### .audit/2026-07-12-governance-compendium/_workings_joined.md
- [SKIPPED: .audit/2026-07-12-governance-compendium/_workings_joined.md - reading budget exhausted; file not opened (2,734 lines, about 299 KB)]

### .audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md
- [SKIPPED: .audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md - reading budget exhausted; file not opened]

### .audit/2026-07-12-settlement-season-stress-sim/_workings_joined.md
- [SKIPPED: .audit/2026-07-12-settlement-season-stress-sim/_workings_joined.md - reading budget exhausted; file not opened]

### .audit/2026-07-12-settlement-season-stress-sim/appendix_B_roll_failures.md
- [SKIPPED: .audit/2026-07-12-settlement-season-stress-sim/appendix_B_roll_failures.md - reading budget exhausted; file not opened]

### .audit/2026-07-12-settlement-season-stress-sim/stress_test_synthesis_v1.md
- **What it is:** the max-effort synthesis of a 2026-07-12 agent-played stress test of the PR#119 provisional governance mechanics (7 seeds x 5 seasons, 13-agent workflow, plus a main-session verification layer); 275 lines, read in full.
- **Status:** "FILED - 2026-07-12 . Lane: IN (cross-cutting; SE, FA, PC) . Read-only review artifact - NOT canon" (:3). Reading: historical; it was played "by the resolution engine acting as the ruleset" because no executable settlement-season engine existed in `sim/` (:7-9), which is no longer true (`engine/season/` exists), so its dynamics are a hypothesis set for a real run, not a measurement of the current game.
- **Bears on:** SE, FA, CHAR (Standing/Demotion), DICE (d_sigma), CORE
- **Content that matters:**
  - Verification layer (§0): two headline "dead-end by construction" findings (event deck has zero resolvable Crisis cards; §1.3c Ordenanza unreachable because no Gu-Std2-to-3 rung) were digest artifacts, not canon holes (:42-62). The lesson recorded: a compressed kernel digest manufactured phantom gaps; verify against the full source before authoring effort (:269-275).
  - Odds ground truth (§0.3-0.4): agents under-estimated P(net>=3) on 7D TN7 by 5-7 points (48 vs 55 percent, :64-70); `d_sigma` rolls scored with the deck's legible "50 percent + 10 per point, floor .05 cap .90" diverge at the tails from `sim/autoload/sigma_leverage.p_success` (a continuous normal CDF; example engine 78 vs linear 90; :72-78). A "which odds are canon" reconciliation item.
  - Eight recurring cascade patterns A-H (:111-145): demotion spiral 7/7 (tragic downfall is the default, appeals succeeded 0/6), Pi runaway past the R-4 band cliff (Pi 7-to-8, no Grudge decay, no circuit breaker), Compact/Assessment lock-in strips a worsening town below subsistence (deterministic, ~8-season cooldown), Collective-Liability stacking turns the Order tool into a revolt accelerant, patron-lapse un-shielding queued demotions, clerk-corruption loaded gun, Suspicion-to-Recall on an undefined threshold, Mandate `clamp(round(7T/(T+6)))` is saturating and Seat-dominated so peripheral collapse does not register (cross-scale drag refuted; Standing/ledger Keys are the real collapse carrier).
  - Tiered gaps: CRITICAL: Seggio "seized by force" with no governance-scale seizure resolver (:151-153); HIGH: no subsistence floor, no Pi relief valve, Bind-the-Cells (5-household cells) vs one-to-two named Local Actors (§1.3b vs §4.5), sanctioned Defy mis-scored as Duty failure, undefined territory-scale governor AP economy, audit vs Recall double path, no character attribute block in any seed (:155-172).
  - Rejected-proposal vindication: IT-3 Sforza Gambit (bounded seizure/emergence resolver) and VEN-SE-4 Dedizione (negotiated extraction cap) are the strongest reinstatement candidates; VEN-FA-2 stays cut but its AP accounting should be harvested (:195-209).
  - 13 prioritised findings for Jordan (:236-267); bottom line: the resolution substrate "earned ratification", §1.3a failure mode, §3.3c and Mandate-at-scale should not be ratified as-is (:269-275).
- **Conflicts / stale:** runs on retired Key language ("registered Keys", Standing Keys, ledger tags). Its cut-proposal ids (IT-3, VEN-SE-4 ...) belong to the governance-compendium lineage in `.designs`. No check made of which gaps `engine/season/` has since closed [UNVERIFIED]; a grep of `engine/season/hole_register.yaml` for "subsistence", "seggio", "Pi" would be the cheap test.
- **Open items:** all 13 prioritised findings are left as recommendations; the `d_sigma` odds-contract decision; the seed/roster attribute schema.

### .audit/2026-07-22-combat-engine-stress-test/adversarial_pass.py
- **What it is:** report-only Python probe (107 lines, read in full), 2026-07-22: falsifies the stress-test report's own claims about the personal-combat engine.
- **Status:** none stated ("Report-only; monkeypatches are in-process, nothing committed"). Reading: historical instrument; **no longer runnable as written**: it inserts `systems/combat/combat_engine_v1` on `sys.path` (:6-7) and imports `core, combat_systems, weapon_physics, combatant, config, weapons` from there, but those modules now live in `modules/combat/` (`ls`: combatant.py, combat_systems.py, core.py, config.py ... present there; `systems/combat/combat_engine_v1/` now holds only capabilities.py, state_graph.py, workbench/).
- **Bears on:** PC, DICE
- **Content that matters:**
  - Method: ablate `S.halfsword_target` to "never switch" and compare win rates vs LIVE for longsword/estoc across armour (:17-27); result stated in the file: half-swording is a net liability at medium/heavy armour (overturns an earlier report claim, :17).
  - Mechanism claim: `adef_cap(point)` reads only gap, never leverage, while the half-sword has about 3x leverage (:29-36); prototype fix crediting leverage into gap-thrust armour-defeat (K sweep 0/0.4/0.8, :39-56) is explicitly "NOT a committed fix" and would lift every thrust weapon.
  - Falsifies report claim C1 ("5 distinct context-leaders at N=120"): at N=400 margins are 0.2-0.6 pp, i.e. noise; the real C1 result is the 2.9 pp unconditional spread (:58-64).
  - Confirms agility dominance at an all-4 baseline (`agi` still top at +1 attribute, :66-74).
  - Three attempted adef fixes (leverage credit, bounce standing cut_thrust, partial standing gap-thrust f=0.6/0.4/0.2) all fail the two bars "switch benefit positive" and "arming mirror ~50" (:76-107); conclusion: the half-sword liability is coupled to reach over-weighting (Phase-C/G4), not an independent bug.
- **Conflicts / stale:** broken import path (above). The half-sword capability gate it criticises as a hard-coded name list is now emergent: `tests/valoria/test_combat_halfsword_affordance.py` (ED-PC-0014) pins that capability derives from a `grippable` element plus `geo['halfsword']`, and `halfsword_target` docstring (modules/combat/combat_systems.py:884) says the HALFSWORD_FORM dicts survive only as a base-to-form NAME mapping. Whether the liability itself (switch cost at plate/mail) was fixed is not checked [UNVERIFIED].
- **Open items:** none answered by the file; the reach-weighting coupling is deferred to "Phase-C".

### .audit/2026-07-22-combat-engine-stress-test/grounding_battery.py
- **What it is:** report-only HEMA/physics grounding battery (101 lines, read in full): falsifiable assertions against the physics layer, each citing Williams "The Knight and the Blast Furnace", Fiore/Talhoffer/Ringeck, Le Jeu de la Hache.
- **Status:** none stated. Reading: historical instrument; same broken `systems/combat/combat_engine_v1` import (:11) [would need `modules/combat`].
- **Bears on:** PC
- **Content that matters:**
  - 10 assertion groups G1-G10: native cuts collapse vs plate (ratio <= 0.30, :24-29); point out-couples cut vs plate (:32-34); blunt/percussion transmits (:36-43); longsword/estoc half-sword vs plate in the close (:46-50); poleaxe affords blunt+point and selects the spike vs plate (:53-58, tagged "KNOWN PHASE-C"); reach threat decays vs plate for a cut polearm (FIX-1, :63-68); damage monotone-non-increasing with heavier armour for every head (:71-75); degree ordering graze<success<overwhelming (:78-80); strength monotone (:83-85); a "vs-plate cliff" probe listing cutting polearms (guandao, fauchard, glaive, podao, voulge, bardiche, sparr_axe, naginata, :88-90).
  - A comment records ED-PC-0036: `core.damage` lost its `close` positional because it was never read (:19), and `stress_battery.py` records the same fix at :100.
- **Conflicts / stale:** import path; the output (MATCH/DIVERGE counts) was never stored in the file, so no pass count is claimed here.
- **Open items:** the polearm vs-plate cliff driver is a probe only.

### .audit/2026-07-22-combat-engine-stress-test/phasec_probe.py
- **What it is:** report-only Phase-C diagnostic probe (51 lines, read in full): localises three coupled levers behind reach-class dominance and the half-sword liability.
- **Status:** none stated. Reading: historical; broken import path (:5-7).
- **Bears on:** PC
- **Content that matters:**
  - Lever 1: reach-class dominance at heavy armour is the approach stop-hit; cutting `STOPHIT_CHANCE` globally (x0.5, x0.3) compresses reach@heavy but collapses spear@none below the grounded 55, so the fix must be armour-conditional (:24-28).
  - Heterogeneity: with STOPHIT=0 spear/yari collapse but poleaxe barely moves, so the "reach class" is not monolithic (:29-33).
  - Lever 2: the half-sword liability is separate (it fights in the close; its loss is reach-volume) (:35-36).
  - Lever 3 (self-corrected): the earlier "1.6 kg spear shaft unmodelled" claim was WRONG; spear heft is high because `PoB_frac` (0.34) is about 3x the swords' (~0.12), so the fix is a PoB_frac normalisation, decoupled from reach (:38-48).
- **Conflicts / stale:** import path. Whether Phase-C (armour-conditional stop-hit, PoB_frac normalisation) shipped is not checked [UNVERIFIED; one grep for `STOPHIT_CHANCE` / `PoB_frac` in `modules/combat/` would answer].
- **Open items:** armour-conditional stop-hit; PoB_frac normalisation.

### .audit/2026-07-22-combat-engine-stress-test/primitives_probe.py
- **What it is:** report-only adversarial probe (79 lines, read in full) of the engine's claim that weapon behaviour emerges from five geometry primitives {curvature, point_concentration, cross_section, edge_keenness, strike_concentration} baked by `geometry.bake`.
- **Status:** none stated. Reading: historical; its finding A and B appear FIXED at the working tree.
- **Bears on:** PC
- **Content that matters:**
  - Finding A: `geo['halfsword']` (`can_halfsword_thrust`) was computed for every weapon and read by nothing (:31). Now live: `modules/combat/combat_systems.py:867` reads it and `tests/valoria/test_combat_halfsword_affordance.py` pins it (ED-PC-0014).
  - Finding B: half-sword capability was a 2-name fiat list `HALFSWORD_FORM`; the primitive was too broad (no length/2H term, would wrongly include daggers and spears; :33-41). Fixed by the `grippable` field plus geo flag per the test docstring.
  - Method C: dead-primitive ablation: set each raw primitive to 0 and 1 roster-wide, re-bake, measure max win-rate shift over an 8-matchup basket; verdict DEAD <3 pp, weak <10 pp, LIVE otherwise (:44-78). No result is stored in the file.
- **Conflicts / stale:** import path; findings A/B superseded as above; finding C result unknown without a re-run (the instrument would be reusable once repointed to `modules/combat`).
- **Open items:** which primitives are inert (C) is unanswered in the file.

### .audit/2026-07-22-combat-engine-stress-test/stress_battery.py
- **What it is:** report-only mechanical stress battery (161 lines, read in full): robustness, extremes, determinism, mirror symmetry, numerical sanity, monotonicity, upset cap, termination for `wrapper.fight`.
- **Status:** none stated. Reading: historical instrument; broken import path (:9-11).
- **Bears on:** PC, DICE, CORE (determinism)
- **Content that matters:**
  - Eight categories (:38-144): weapon x armour grid and tradition grid must not crash; extreme/negative/huge/float attributes must return -1/0/1; same-seed reproducibility on 12 weapons; mirror match within 0.08 of 50 percent (WARN at 0.15) at N=400; `core.damage` finite, int, non-negative over weapon x armour x degree x strength; `core.degree`/`core.resolve` valid bands; raising any attribute must not lower win rate (tolerance 0.05); extreme mismatch < 100 percent (config `UPSET_FLOOR`); 200 fights bounded under 30 s.
  - A comment records ED-PC-0036: the `numerical` category was silently recording FAIL (the call raised inside try/except) until the retired `close` positional was dropped (:100); a lesson that an assertion inside try/except can hide that it tested nothing.
- **Conflicts / stale:** import path; stored outcomes absent.
- **Open items:** none.

### .audit/2026-07-22-combat-engine-stress-test/trace_backward.py
- **What it is:** explicit-trace plus backward-causal analysis tool (156 lines, read in full): wires the engine's `wrapper._TRACE` seam, spies on `S.assemble_net_sigma` and `core.strike`, and walks a battle backwards from the felling blow to the engagement origin.
- **Status:** none stated. Reading: historical/reusable instrument; broken import path (:13-17).
- **Bears on:** PC, CORE (trace discipline)
- **Content that matters:**
  - Captures every consumed input per decision node: reach/measure, stop-hit probability, commit depth and Beta, read margins, mode sigma, net-sigma components (attack, defence, reach penalty, armour-defeat, initiative), the roll, the blow (:20-82).
  - Backward walk: felling blow -> its roll -> net-sigma components -> commit/read/mode -> engagement origin (:84-129); undecided fights are reported as volume/attrition asymmetry (:97-99).
  - Three cases: half-sword loss (longsword vs arming, both plate), reach win (spear vs arming, none), gap-thrust dagger vs plate (rondel vs arming, heavy); seeds are scanned (0-199) for a wanted outcome (:131-156).
- **Conflicts / stale:** import path; `_TRACE` seam may have moved with the module (unchecked).
- **Open items:** none.

(Note: the same directory also holds `stress_test_findings.md`, `ratified_unimplemented_register.md` and `pc2_halfsword_expansion.md`; they were not in my assignment and I did not open them. The PC lane should, since they carry the findings these probes produced.)

## Cross-subsystem leads
- WR / ARCS / CORE: the arc register's recorded defects (ARC-T04 dangling, Coup Counter struck with no remap, Axis 9 clockless, Torben Loyalty 8-to-0 vs 0-7 start 3, 138 not ~110 entries) were never fixed in the join; a grep shows ARC-T04 only in `.audit/`, `.designs/` and IN handoff history, so check `references/arcs/` and `engine/season/` before repeating them.
- CORE / DICE: the determinism rulings (total-order tiebreak on every Top-N, no `set()` gating emission, integer or fixed-point thresholds pinned in the port, zero-randomness or dedicated-substream rendering, sha256 not builtin `hash()` for seeds) are generic and transfer to `engine/season/`'s seeded loop and the Godot port even though the Key substrate is gone.
- FA / CHAR / SE: part 40's `power_base` typing (rise driver = downfall shape) and shared rank space are a candidate design for `engine/season/offices.yaml` / `rosters.yaml`; check whether a `power_base`-like field already exists before proposing it.
- PC / MB: part 40 reserves "officer" for the mass-battle commander; any FA proposal naming a political "officer" collides.
- WR / GO: the realizer/bake numbers (230-450 authored units vs 1,200-2,700 if Certainty gates the pool; per-NPC voice ~1,050; ERA unbuilt) bear on any text-render claim.

## Likely stale or superseded
- The entire emergent-narrative-engine join: Key / Domain Echo / `meta.*` types / total-accounting-of-Keys machinery is retired (ED-IN-0232); the architecture B "arc-vector engine" with `game_director` ownership is superseded by whatever `engine/season/` actually runs.
- `designs/...` path citations throughout (dissolved; now `.designs/`).
- Part 40 PROPOSED status (not ratified), and its use of the struck Coup Counter.

## Items that could change an audit finding
- The join records, as unanswered, Jordan forks about director tension-curve ownership (subtract-only), `mechanical.scene_entered` ownership, Cert-0 register row, temporal_window, ARC-T04 author-or-strike; an audit that finds these unresolved in `engine/season/` should note they are old and recorded (:6755-6774, :8889-8947, :9578-9632).
- The 15 percent of register arcs that are GM-judgment-irreducible (ARC-P05, ARC-S29, ARC-T06, NPC-ARC-JAR, ARC-S52, ARC-S56) is a standing "no GM, so who decides" gap relevant to any CHAR/FA decision-layer finding (:3109-3115, :5688-5699).
- Finding ids: none cited from `audits/*.md`; I did not open that directory.
- The `d_sigma` legible-vs-engine odds divergence (deck's linear +10 percent per point vs `sigma_leverage.p_success` normal CDF) was found 2026-07-12 and recorded as unreconciled; a DICE or SE audit that finds two ladders for one quantity should know it is a returning finding.
- Probe scripts in the combat stress test cannot run as written (they import `systems/combat/combat_engine_v1`, whose engine modules now sit in `modules/combat/`); their half-sword findings A/B are fixed (ED-PC-0014), finding on the liability itself is unverified.
- Coverage warning for the orchestrator: of 14 assigned files I read in full: the emergent-narrative join, 45_hidden_longfuse_stats, stress_test_synthesis_v1 and the six .py probes (9); partly: 40_roster_officer_system (lines 1-390 of 621) and 42_action_verb_catalogue (lines 1-130 of 254); NOT opened: 41_proactive_scale_menus, governance-compendium `_workings_joined.md`, tier3_proposal_status_closure, settlement-season `_workings_joined.md`, appendix_B_roll_failures (about 500 KB). Reason: my reading budget for the turn ran out, not a tooling failure.
<!-- ENTRIES-END -->
