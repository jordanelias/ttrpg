# Digest auditB2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Scope: the surviving `.audit/` corpus not read in full by DG_audit1 / DG_audit2: the 2026-07-02 closing-distance research JSON, the 2026-07-04 NERS qualitative audit workings (JSON), `_workings_joined.md`, `ed_options.md`, and the 2026-07-04 weapon-morphology-granularity set. All of it is archived-not-canon (`.audit/`, CLAUDE.md §3). Paths such as `designs/...`, `references/arcs/...`, `canon/mechanics_index.yaml`, `Key` types and `module_contracts` Key rows cited INSIDE these files name a tree that no longer exists (`designs/` dissolved; Key substrate RETIRED, ED-IN-0232); where I say "fixed/stale/live" I checked the working tree with one grep or listing.

Working-tree facts used throughout (verified this session): `designs/` does not exist; `.designs/` holds `README.md engine systems`; `modules/` holds `combat fieldwork mass_battle settlements social_contest`; `registers/mechanics_index.yaml` exists (moved from `canon/`); `references/roadmap_state.yaml` and `references/arcs/` are gone; `engine/season/` is the live loop.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_measure_gap.json
- **What it is:** Fact-gathering JSON (not a proposal), 2026-07-02, scene-combat closing-distance redesign lane ("R0 research"): HEMA treatise and biomechanics facts on how a shorter weapon closes on a longer one; 232 lines.
- **Status:** none stated (research dump). Reading: historical; its premise (polearms win 84-96% vs arming sword) was the motive for the R2 closing-distance redesign (PR#72) and R3 weapon-model consolidation (PR#76) that the later NERS critic names. Research is tier 3.
- **Bears on:** PC (primarily), DICE.
- **Content that matters:**
  - `:3-57` lists the engine baseline it read (checkout `C:/Github/ttrpg-morph-rearch`, `designs/scene/combat_engine_v1/systems.py`): `approach_displace`, `close_rate`, `leverage` (= grip_len - LEVER_HEAD_K*head_len, absolute-difference form adopted to fix a "dagger 0.140 > spear -0.066" ratio inversion; LEVER_K 0.22, LEVER_HEAD_K 0.2, LEVER_REF 0.32, LEVER_2H 0.20, all [SIM-CALIBRATE]), `grip_target/can_choke`, `close_tempo`, `recoverability_factor`, `beat_aside`/`slip_inside` (wrapper.py:220-240), `reach_threat` FIX-1, `halfsword_target` (gated on closed AND armour, not on closed-measure alone), `reach_sigma`.
  - `:57` the symptom: polearm-class weapons win 84-96% of matchups vs an arming sword; mechanisms exist but magnitudes/gating do not reproduce the attested "closing is live" outcome.
  - `:64-97` Fiore (Zogho Largo/Stretto, spear fol. 39r "off-line step + beat while passing the back foot" = void and close are ONE motion), Silver true-times (hand before foot), Meyer (Zufechten/Handtarbeit/Abzug), Liechtenauer Vor/Nach/Indes/Fuhlen: all medium-high confidence, secondary sources.
  - `:128-132` flagged GAP: forte/foible is contact-point-on-own-blade dependent (within-exchange), whereas `leverage()` is a fixed per-weapon scalar.
  - `:198-201` explicit GAP: no source gives a quantified minimum distance for a full-power strike; the "50 cm" intuition is UNSUPPORTED by what was retrieved.
  - `:206-209` cross-cutting: treatises convergently describe closing as a DISCRETE regime boundary (different technique repertoire), and attribute the short weapon's success to a specific mechanism (voiding+closing, shaft seizure, long weapon's own moment of inertia), never to generic "faster"; no mechanism wholly absent from the engine was found.
- **Conflicts / stale:** engine file paths (`designs/scene/combat_engine_v1/`) are retired; the live combat code is under `modules/combat/` [UNVERIFIED that `leverage()` etc. still carry these names; one grep would tell]. The 84-96% figure predates R2/R3 and should not be quoted as current. Many "confidence" notes say folios not verified against facsimiles.
- **Open items:** forte/foible as a contact-point (not scalar) quantity; whether a discrete close/wide regime (Fiore) should be modelled; minimum-distance threshold left unquantified.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/confirmed.json
- **What it is:** 5 findings that survived refutation in the 2026-07-04 NERS qualitative audit (of 157 candidates), each with the refuter's verdict, intent reading and revised severity; 103 lines.
- **Status:** none (JSON working). Reading: historical; individual findings checked below.
- **Bears on:** SE, WR (emergence), GO/UI, CORE (articulation), FA (victory).
- **Content that matters:**
  - `:3-22` `settlement-governance-thin-loop`: ratified seasonal governance = one mandatory free action over four +1 stat-pumps (Develop/Fortify/Pacify/Administer); the corpus's own redesign proposal said it collapses to "roll one die a season" with no GM; CONFIRMED, severity P1 trimmed to P2 (politics is "held one tier up"; fix authored, gate G1 closed).
  - `:24-41` `collision-engine-has-no-engine`: the 8 Convergence-Marker collisions exist only as hand-authored trigger+payload text; no resolver detects trigger coincidence or applies the combined (non-summative) payload; CONFIRMED P1->P2; intent UNDETERMINED; T-23 NPC Arc Emergence is "Fully implemented" so base emergence has independent channels.
  - `:43-62` `ui-spec-stranded-off-index`: UI/UX v4.1 (CANONICAL, 2026-04-16) predates the generation, absent from CURRENT.md, its v4.2 repair workplan (69 findings, 20 P1) never executed; PLAUSIBLE; refuter notes the "only comprehensive spec" framing is wrong (v4.md is the larger content spec) and P1 is inflated (pre-implementation).
  - `:64-82` `articulation-battle-concluded-trigger-gap`: articulation §3.1's 10-trigger ruleset omits scene.battle_concluded / investigation_resolved / combat_resolved though the registry declares them consumed and §6.4 falsely says battle_concluded "already triggers Tier 2"; CONFIRMED P2. The belief_revised precedent (trigger #10 had to be ADDED) shows §6 defaults are not self-executing.
  - `:84-102` `peninsular-strain-partition-unmarked`: peninsular_strain_v30 §6.3 Partition co-victory (about 8 sites) survives despite GD-1 striking it; already tracked in `canonical_sources.yaml` FACTION-SPECIFIC-VICTORY-PATHS (pending-batch-Pass-2k); P3.
- **Conflicts / stale:** all five cite `designs/...` paths and the Key-type registry (retired). Finding 1: `modules/settlements/` is live; whether the governance verb menu was thickened is [UNVERIFIED]. Finding 4 concerns the articulation layer and Key `scene.*` types, which no longer exist (Key substrate retired) so it is STALE as phrased; the underlying question (does a decisive battle/trial verdict render a cut scene) is not answered here. Finding 5: GD-1 victory model; check `engine/season/ENDINGS_CLASSIFIED.yaml` [UNVERIFIED].
- **Open items:** the emergent-collision detector; the governance verb menu; the stale CANONICAL UI doc; none show a closing ED.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/critic/critic.json
- **What it is:** a critic pass over the audit's own coverage (11 gaps + overall verdict); 48 lines.
- **Status:** none. Reading: historical; the one summary of what the NERS audit did NOT cover.
- **Bears on:** PROCESS (audit coverage), PC, SC, SE, WR, CHAR.
- **Content that matters:**
  - `:3-6` settlement_territory "effectively unaudited": no dossier, hunt or refute; densest coupling edge (Mandate = clamp(round(7T/(T+6))), LPS-2e math, L/PS drift) and mass-battle location substrate.
  - `:8-10` only 5 of 12 lanes have a real six-direction dossier (mass_battle, faction_political, articulation, victory_strategic, registers_graphs); the summary's `missing_dossier_lanes:[]` is misleading. Personal combat and threadwork, the two the charter foregrounds, have none.
  - `:12-14` npc_behavior returned empty: both candidate findings refuted, no positive dossier; absence there is "under-evidenced".
  - `:16-18` hunt_combat_minmax missing (4 of 5 hunts exist); the combat degenerate-play item describes the PRE-R2/R3 model; no fresh sweep of the new model.
  - `:32-34` `scene.combat_resolved` down-seam (declared consumed by npc_behavior/faction_layer/articulation, absent from their `consumes:`) is verdicted by no lane.
  - `:44-46` refutation files scattered across 6+ sibling subdirs with no manifest, so a synthesiser could resurrect a refuted finding.
- **Conflicts / stale:** `hunt_combat_minmax.json` and `dossier_settlement_territory.json` DO exist in this directory, so gaps at `:3-6` and `:16-18` are not real. The folder's own README (`_workings_joined.md:411-423`) says the critic "misread scratch placement as missing coverage" (7 dossier lanes returned JSON only, a scratch-discipline artifact). Treat this critic as superseded by that README note.
- **Open items:** none that any later artifact seems to answer; the audit was superseded by the 2026-10 ners audit (`references/ners_audit_2026-10-14.md` exists).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/deferred_unverified.json
- **What it is:** 32 findings that were neither confirmed nor refuted (deferred, unverified), each with subsystem, claim, cite, criterion, direction, severity, novelty; 397 lines.
- **Status:** none. Reading: historical candidate list; many are design-level claims about the then-current docs, some now overtaken.
- **Bears on:** PC, SC, MB, FA, WR (threadwork), CHAR, CORE, PROCESS.
- **Content that matters:**
  - `:98-134` combat hunt: heavy armour has no wearer-side cost (`armor-no-encumbrance-pure-upside`); impose_node rewards counter/measure traditions (refuse-riposte asymmetry); `overcommit_exposure` subtracts additive terms from a floored multiplicative cost giving exactly 0 for a light hand-balanced weapon (`commit-recovery-axis-nulled-light-weapon`) - cites systems.py lines 502-513, 740-743.
  - `:136-170` social hunt: uncapped Recall (+2D binary per exchange) plus Corroborate/Prep/Findings flatten the base pool; Appraise's audience boost is a public deterministic lookup (solved); strain->Rattled->Face channel unwired so the stamina/standing/merits tradeoff is decorative.
  - `:172-182` `pp508-split-dominance`: canon states splitting beats concentration by +9-45% win-rate except Narrow Pass / Size=1, resolved in ED-358 as "intended" without applying the Omega non-dominance lens.
  - `:185-208` Domain Echo capped per scene not per season (Debate-spam farms Mandate); Crown Enforce (Ob 2) strips insurgent Presence markers choking the GD-3 Revolt->Insurgency->Faction pipeline.
  - `:211-234` threadwork: Mending §3.2 table (Coherence -1) vs §2.4 asymmetry (0) contradicts and under 0 strictly dominates the RS sub-tree; a practitioner-leader's Territorial Weave yields Domain Action + Stability +1 + Echo Mandate +1.
  - `:312-346` roster conflicts: glossary 7 attributes vs descriptor_registry/names_index 9; `resonance_style` retired in the registry but live in npc_behavior §1.3; glossary unmirrored by `ci_names_consistency`.
- **Conflicts / stale:** `designs/...` paths all dead. Verified live today: `references/glossary.md:53` carries an "IN FLUX" banner for the 7-vs-9 attribute conflict and `references/descriptor_registry.yaml:9` says the roster is now 10 and "IN FLUX until Jordan confirms"; `descriptor_registry.yaml:266` carries the ED-IN-0025 correction on resonance_style (retirement status left unchanged, NEEDS-JORDAN). So those two are TRACKED, not fixed. `roadmap_state.yaml` entries (`:63-72`, `:361-371`) are STALE: file no longer exists. `mechanics_index.yaml` now at `registers/` (`:15-61`). The workplan/decision_queue contradictions (`:75-96`) concern files outside the current trees [UNVERIFIED].
- **Open items:** armour wearer-side cost; the recall cap; per-season Domain Echo cap; Mending Coherence value; phenomenology tier T-31..T-41 "Proposed" with no implementing head (`:237-247`).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_architecture_spine.json
- **What it is:** six-direction dossier on the Key/propagation "architecture spine" (substrate, registry, scale_transitions, propagation_spec); 8 findings; 220 lines.
- **Status:** none. Reading: historical AND largely superseded: the whole object (Key substrate, key_type_registry, echo transport) is RETIRED (ED-IN-0232).
- **Bears on:** CORE, PROCESS (retired architecture).
- **Content that matters:**
  - `:34-54` N/Q notes: 3 of 44 Key types used out-of-enum permanence/time_horizon values; termination proven, cross-tick convergence not; Domain Echo's 7-trigger Sufficient Scope list is "best-specified direction".
  - `:76-111` edge table: 8 down-seams (domain_actions -> npc/piety/settlement) emitter-unpopulated; `scene.combat_resolved` declared-but-unconsumed; domain_actions `doc:null`.
  - `:121-218` findings: cross-tick-convergence-unproven (P1, tracked), domain-actions-central-and-unspecified (P1), CASCADE_DEPTH_MAX / EMISSIONS_PER_TICK_MAX unbacked integers, three incompatible RNG contracts (substrate per-emission seed vs single global stream vs named-draw service), `causes[]` overload, scene.thread_operation payload [STUB].
- **Conflicts / stale:** every finding is about Key plumbing that no longer exists; verified `battle_concluded` has zero hits in `engine/` or `modules/`. The one durable question carried forward is "does a declared consumer actually consume" (see `two-structural-death-points` in deferred_unverified.json), which now is a seam/registry question in `engine/season/seam/` and `write_matrix.yaml` [UNVERIFIED].
- **Open items:** RNG-model collision was never reconciled in this file; check against current dice/seed owner in `engine/season/`.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_articulation_layer_pp_688_designs_articu.json
- **What it is:** dossier on the Articulation layer (Tier 1 UI reframing, Tier 2 cut scenes on 10 triggers, Tier 3 annual chronicle); 6 findings; 181 lines.
- **Status:** none. Reading: historical; the Key-stream subscription premise is retired.
- **Bears on:** CORE, WR (narrative), GO (UI).
- **Content that matters:**
  - `:3` core loop: pure sink (`emits: []`); wildcard Key subscription; 10 trigger conditions then significance scoring; Tier 3 yearly top-N chronicle.
  - `:110-131` findings: battle_concluded/investigation_resolved trigger gap (P2, confirmed in confirmed.json); `unarticulated_weight` only boosts an already-firing trigger so non-matching Bonded NPCs are permanently un-rendered (the §3.3 anti-starvation claim is unbacked).
  - `:133-143` `articulation-thread-silence` P1: zero Thread/Coherence/Calamity/Gap/Dissolution hooks in the layer that renders emergence (P-14 smell).
  - `:145-156` `articulation-victory-era-blind` P1 (tracked as ED-1006): era transitions (Post-Calamity, Phased Occupation, Anarchy) are unkeyed so the renderer is blind to them.
  - `:42-44` Stage 10 sim A1-A6 6/6 pass incl. determinism hash match; file carries four disagreeing status markers (`:169-179`).
- **Conflicts / stale:** `designs/articulation/` is dissolved; its design doc survives only as `.designs/systems/articulation/`. Whether any live season-loop module renders cut scenes/chronicle is unchecked here [UNVERIFIED]; the era-blindness point has an analogue in `engine/season/ENDINGS_CLASSIFIED.yaml` which would be the place to check.
- **Open items:** whether chronicle/legend should feed back into NPC renown (`articulation-zero-mechanical-emission`, intent UNDETERMINED).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_faction_political.json
- **What it is:** dossier on faction layer/canon/behavior (Domain Actions, Parliament, Treaty, 4-component disposition engine, GD-1 victory); 8 findings; 241 lines.
- **Status:** none. Reading: historical; the design docs read are now in `.designs/systems/factions/`.
- **Bears on:** FA, WR (threadwork), CHAR.
- **Content that matters:**
  - `:3` loop: 7 turn priorities, 10-step Accounting, GD-1 victory check (11+ territories for 2 seasons), Mandate gates one signature action per faction.
  - `:149-158` `gm-controls-npc-votes` P1: faction_layer_v30 §5.8 said "GM controls NPC faction votes (Guilds, Niflhel)" (Guilds reduced to 3 hard-coded if/then rules); contradicts no-GM. The sentence is STILL in `.designs/systems/factions/reference/faction_layer_v30.md` (grep) but that is an archived doc. LATER REFUTED (refuted.json:21-40, NOT-INTENDED, P3): §5.8 L492 already supplies a deterministic Guilds vote rule (+ED-752 broker shift), Niflhel is STRUCK (does not vote), the doc is tri-mode (BG/TTRPG/Hybrid), and ED-1061 fixed the sibling "GM picks" defect. Residual: the L362 "GM adjudicates" partial-ratification clause and unnamed other NPC-only factions (Schoenland/Altonia) have no vote rule.
  - `:85-88` degenerate candidates: Institutional Consolidation passive recovery (Stability+1, Accord+1 for inaction); all 6 factions default single-root Cascade.
  - `:184-193` thread-absent-from-faction-engine-math (alpha/beta/gamma/lambda take only env.* shocks): P-14 smell.
  - `:217-227` Mass Seizure has 3 non-reconciled canon formulas (pending Pass 2f).
- **Conflicts / stale:** `faction-politics-doc-null-mismatch` refers to `module_contracts.yaml` rows that may have changed [UNVERIFIED].
- **Open items:** faction stat lineup (6- vs 7-stat) "re-litigated three times" with no typed engine surface (`:229-238`).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_mass_battle.json
- **What it is:** dossier on mass_battle_v30 (7-phase Battle Turn, aftermath scene, Levy vs Professional); 7 findings; 246 lines.
- **Status:** none. Reading: historical; engine since moved (`modules/mass_battle/` is live).
- **Bears on:** MB, PC (General Duel), WR (threadwork).
- **Content that matters:**
  - `:3` loop: Muster, March, 7-phase turn (Strategy Declaration, Volley, Manoeuvre, Offensive Thread, Engagement, Cascade, Reform), Part D aftermath scene, Part E consequences.
  - `:53-58` §A.1 axiom "Command=7 vs Command=1 produces a near-certain outcome before a die is rolled" is DELIBERATE but strains Omega non-dominance (finding `generalship-dominance-axiom`, `:189-198`).
  - `:177-187` the §A.8 splitting-doctrine evidence (+9% to +45%) may be contaminated by the invincibility-bug baseline of ED-MB-0002 RC-2 (frozen multi-subunit cohesion under PER_CELL=0).
  - `:95-144` edges: Scene->Mass bonus §3.8 declared-only (no hook in the mass battle turn); General Duel §3.7 Thread-blind (ED-911); sim engine `config.py` is "leading canon" and geometry §A.3b is flagged superseded pending LC-8.
  - `:30-34` strongest decision points: Part D aftermath (Tend/Survey/Address); Levy vs Professional under Campaign Supply.
- **Conflicts / stale:** the doc is superseded by the code. DG-3/DG-4 and ED-MB-* referenced here are in `registers/editorial_ledger_mb.jsonl`. Whether Scene->Mass bonuses exist in `modules/mass_battle/` [UNVERIFIED].
- **Open items:** motive/goal field for named generals (`legibility-motive-gap`, `:200-209`); HUD parity for per-sub-unit float morale (`:234-243`).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_npc_behavior_designs_npcs_npc_behavior_v.json
- **What it is:** dossier on npc_behavior_v30 + conviction_track_v1 (Conviction/Scar/Certainty/Resonant Style, 9 BG Priority Trees, Outreach/Demand, authored Arc maps); 8 findings; 248 lines.
- **Status:** none. Reading: historical; the critic noted this lane "returned empty" once two findings were refuted.
- **Bears on:** CHAR, SC, FA, WR.
- **Content that matters:**
  - `:3` loop: Conviction(s) + Resonant Style + Certainty; players target vulnerabilities by RS-matching; per-Conviction Scars gate Belief revision and fire authored Arc branches; BG Priority Trees (7 levels) per faction; Outreach/Demand surfaces up to 3 NPC-initiated scenes per season.
  - `:97-100` degenerate: fully deterministic Priority Trees; fixed 1:1 Resonant Style + stacking Wrong-Style Penalty (§6.4.3) collapses contest tactics to lookup.
  - `:82-91` only Varfell §8.5 and Wardens §8.10 trees have Thread-conditioned rows; the other six trees have none.
  - `:170-179` `sim-conviction-taxonomy-stale` (claimed sim CONVICTIONS = legacy 9 vs ratified 13) - REFUTED (refuted.json:41-59, DELIBERATE, P3: the sim mirrored the still-canonical conviction_track_v1 §3 matrix, which kept legacy names pending PP-718; ED-1050 forbids fixing the oracle in place); today `engine/season/harness/conviction_spread.py:13` refers to "the thirteen CONVICTIONS", so the 13-set is the live reading.
  - `:156-168` module_contracts' social_contest and npc_behavior blocks disagree on whether the 2-cycle damper is BOUNDED; the live line at `references/module_contracts.yaml:475` still says BOUNDED with "affect_axis clamp is NOT in canon".
- **Conflicts / stale:** `sim/personal/conviction.py` is gone. `designs/npcs/` now `.designs/systems/npcs/`. `canon/mechanics_index.yaml` now `registers/mechanics_index.yaml`.
- **Open items:** P-09 (memory must be messy/costly/detectable) has no mechanical surface for `npc_memory` (doc:null at the time).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_personal_combat.json
- **What it is:** dossier on personal combat (combat_engine_v1: wrapper.fight/engagement, continuous sigma-leverage engine, scene_combat_design_v1); 6 findings; 192 lines.
- **Status:** none. Reading: historical; the engine now lives in `modules/combat/` (verified: `wrapper.py`, `config.py`, `combatant.py` exist there).
- **Bears on:** PC, DICE, CHAR.
- **Content that matters:**
  - `:3` loop: Approach, AwaitTempo, Exchange (commit depth 2-5, mode select, sigma via `core.roll_net`/degree), Bind/Riposte/HitLanded, Felled/Separation; pool = max(5, History+6); bilateral-Ob wounds (ED-1041).
  - `:123-133` `pc-no-player-input-hook` P1 (NEW): `engagement(A,B,first,cfg,rng)` has no player-decision parameter; commit depth, mode, grip-choke, retreat-vs-press are all engine/RNG-resolved, "build-time loadout plus autoresolve". LATER REFUTED in refuted.json:3-19 (verdict REFUTED, DELIBERATE, P3): the file is the balance ORACLE (`wrapper.py:352` "fight() is the multi-turn SIM harness ... the GAME calls one engagement per turn"), `module_contracts` lists `scene.combat_strike` from `[scene_slate, player_input]`, and player_agency_v30 specified 14 combat actions. The residual (mapping the 14 actions onto the wrapper's decision nodes `exchange.commit/.read/.mode/...`) is unbuilt. AUDIT_BRIEF's PC design intent (player-held choice) makes this residual live.
  - `:37-40` spear/polearm 84-96% dominance pre-R2; voulge/bardiche 81-88% retention flagged borderline (JD-1).
  - `:57-72` combat_engine_v1 had zero threadwork integration (ED-911, P1); combat_v30 §10 Leap-in-combat text never migrated (regression, not original absence).
  - `:147-157` `scene.combat_resolved` payload carries only scene_id/outcome/participants/casualties/wounds_inflicted.
- **Conflicts / stale:** `scene.combat_strike`/`scene.combat_resolved` are retired Key types; whether current `modules/combat` exposes an agency hook is not answered here [UNVERIFIED]. 53-weapon roster and U0-U9 sequence: see weapon-morphology files below.
- **Open items:** retreat-as-default (U6) PENDING; player-input surface and threadwork not slotted into U0-U9.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_recent_infra_sequence_lane_last_month_in.json
- **What it is:** process/steering dossier: whether workplan v5, roadmap_state.yaml, decision_queue.md and CURRENT.md agree; 7 findings; 211 lines.
- **Status:** none. Reading: historical/stale; the four-surface steering picture was replaced by CLAUDE.md §1 (CURRENT.md + HANDOFF.md as pointer indexes, one plan per lane).
- **Bears on:** PROCESS (no game bearing), PC (R2/R3 context).
- **Content that matters:**
  - `:127-137` `roadmap_state.yaml` stale (updated 2026-06-28): file now DOES NOT EXIST in `references/` (verified), so FIXED by deletion.
  - `:139-148` workplan v5 vs decision_queue item 18 vs CURRENT.md disagree on J-38 (propagation spec) status; CLAUDE.md §2 now mandates one active plan per lane, so superseded.
  - `:173-183` R2 cut spear/polearm dominance 84-96% -> 78-93%; declared contested band 55-75% not met; R3 (PR#76) assigned the remainder.
  - `:185-195` `sim-winshare-untouched` P1: sim/mc_v18 seeded win-share about 87%/0%/0%, "no regression oracle beyond a smoke test" (decision_queue item 8; CLAUDE.md §7 now says the campaign-level instrument has no live successor, so the gap is still open at the instrument level).
  - `:162-171` propagation_spec and the holonic container doctrine contain zero threadwork/Coherence mentions.
- **Conflicts / stale:** `sim/mc_v18` and `decision_queue.md` no longer exist in this form; `tools/observability/` is gone.
- **Open items:** campaign-level balance instrument (CLAUDE.md §7 admits it is open).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_registers_graphs_shape_lane_mechanics_in.json
- **What it is:** "SHAPE" lane dossier on the registries (mechanics_index, canonical_sources, supersession_register, DECISIONS.md, coverage_matrix); 7 findings; 179 lines.
- **Status:** none. Reading: partly fixed, partly still live.
- **Bears on:** PROCESS, MB, SC.
- **Content that matters:**
  - `:100-111` `mechindex-massbattle-stale`: mechanics_index's mass_battle row `not_implemented, "<5% of v22 feature surface"` vs `tests/coverage_matrix.md` log of a mature engine. Verified at the working tree: `registers/mechanics_index.yaml:514` now carries a "STALE (ED-IN-0025 ... do not hand-flip it)" banner but `test_status: not_implemented` at line 499 is unchanged. TRACKED, not fixed.
  - `:112-122` mass-battle ratifications (ED-1089..1096, ED-MB-0001/2) not back-propagated to canonical_sources pins or supersession_register.
  - `:145-155` DECISIONS.md: 507/957 items P1 (53%), the P1 tag does not discriminate; `tools/observability/` no longer exists, so STALE.
  - `:156-166` `tests/coverage_matrix.md` title ("Weapon System v2 (Active)") no longer describes its mass-battle content; file and `coverage_matrix_archive.md` both exist.
  - `:167-177` mechanics_index and module_contracts: two overlapping registries, divergent schemas, no cross-reference.
- **Conflicts / stale:** `canon/mechanics_index.yaml` moved to `registers/`. DECISIONS.md retired.
- **Open items:** mechanics_index.yaml `test_status` for mass_battle and social_contest still need a re-survey (the banner says so).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_settlement_territory.json
- **What it is:** dossier on settlement_layer_v30 / territory (17 provinces, 37 settlements, governance verb, Mandate<->L/PS loop); 7 findings; 255 lines. It is the only settlement dossier, although the critic.json pass still lists settlement_territory as "effectively unaudited", so the critic ran on an earlier state.
- **Status:** none. Reading: historical for the design docs; the thin-loop diagnosis is the best-evidenced SE content here.
- **Bears on:** SE, FA, MB, WR.
- **Content that matters:**
  - `:3` loop: Province (17) contains Settlements (37, S-001..S-037); governor has one seasonal verb (Develop/Fortify/Pacify/Administer); Order -> province Accord (floor-mean); L/PS aggregate size-weighted into Mandate = 7T/(T+K), saturating, mean-reverting L/PS back +-1/season.
  - `:28-34, :194-205` Thread Exploitation Sites (§4.9) = uncapped, uncontested Wealth+1/RS-0.5 faucet; no governance verb to respond to Thread (§3.2 vs §4.4/§4.9).
  - `:36-40, :182-193` governance_play_redesign_v1 (8 AP verbs, Directive comply/bargain/defy, Petition/Friction/Crisis deck) is a PROPOSAL gated on an unbuilt settlement registry (G1), absent from CURRENT.md and HANDOFF_SE.
  - `:218-229` settlement_adjacency_v30 worked examples cite pre-PP-726 IDs (S-015/S-023/S-026 vs live S-018/S-036/S-031).
  - `:242-252` territory temperament alpha/beta has zero mechanical consumption in settlement layer or module_contracts. The working tree agrees in part: `modules/combat` greps hit "temperament" only for combat traditions; no settlement consumer was found by one grep over `modules engine` for settlement files (the grep returned only combat files) - consistent with the claim.
- **Conflicts / stale:** `modules/settlements/` is a live implementation (fabric, fortification, housing, larder, produce, provision, subsist) - not the governance verb menu; the redesign's status in the live `engine/season/` is not answered here [UNVERIFIED].
- **Open items:** the redesign's G1 prerequisite; Thread response verb for governors.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_social_contest.json
- **What it is:** dossier on the rebuilt social contest (Stages 0-3 of the sim/personal/contest kernel, social_contest_v30, Adjudicator Armature); 6 findings; 226 lines.
- **Status:** none. Reading: historical; the rebuild's stage list is the content, and `modules/social_contest/` is now the live home.
- **Bears on:** SC, CHAR, FA, WR.
- **Content that matters:**
  - `:3` per-exchange loop: Appraise, pick Style (Genre x Orientation), Argue roll (pool + genre/audience/Recall/armature bonuses), resolve CLASH/REINFORCE/CROSS/TIE, Persuasion Track moves, Face/Concentration deplete, Decisive/Compromise/Total, then Domain Echo + Obligation + Thread co-movement.
  - `:156-166` only "agon" wired in the GAMES router; Consensus/Negotiation/Inquiry were stub rows raising NotImplementedError (Stage 4 next), so "one game wearing eight venue skins".
  - `:168-190` Orientation's CR5 risk/reward (Doubt Marker + self-Face backfire) and the strain->Rattled->Face channel were design-table only, not consumed by the resolver (orientation-payoff-unwired later REFUTED, refuted.json:258-278: `rhetoric.py cr5_self_backfire` is called at `resolver.py:404-419`, ED-1062 "now-WIRED"; only the Doubt Marker's terminal-at-close -2 is unconsumed = ED-1060, open for Jordan); Terminal Doubt (ED-1060) existed because Obscuring was strictly dominated in single-exchange proceedings.
  - `:204-213` Adjudicator Armature: continuous 4-axis style-vs-conviction dot product via delta-sigma leverage with coarse Appraise bands; contest and combat share one sigma-leverage substrate (CR2/CR6); asymmetry vs npc_behavior's categorical Resonant Style +1D flagged for future reconciliation.
  - `:193-202` zero thread/Leap/Weaving hooks in the rebuilt kernel despite §9.3/9.4/9.4b being specified.
- **Conflicts / stale:** `sim/personal/contest/` is gone; whether Stage 4 games now exist in `modules/social_contest/` is [UNVERIFIED] (one `ls`/grep would settle). The dossier relies on retired `scene.contest_resolved` / `state.opinion_revised` Keys.
- **Open items:** recall near-costless (+2D); orientation payoff unwired; the 2-cycle damper claim.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_threadwork_coherence_ms_rs_calamity_risk.json
- **What it is:** dossier on threadwork (Leap, 6 ops, personal Coherence, world track), knots, calamity radiation and the horizontal integration spec; 6 findings; 227 lines.
- **Status:** none. Reading: historical; the MS-vs-RS naming split is the durable item.
- **Bears on:** WR (threadwork), PC, CORE (articulation), FA, SE.
- **Content that matters:**
  - `:2` loop: practitioner (TS >= 30 + Approach Training) Leaps (Spirit x2 + History + TPS, TN7) then performs one op at Depth x Breadth x Distance Ob, paying personal Coherence (10 -> 0) plus a world-track cost; the world track's band x node-distance from Askeheim sets ambient Gap/Shifting-Object pressure for everyone.
  - `:152-164` `ms-rs-split-live`: the world track is "MS (Mending Stability)" in threadwork_v30/calamity_radiation/knots_v30 but "RS (Rendering Stability)" in params/threadwork.md; ED-428 (keep RS), ED-731 (propagate MS), ED-772 (continue MS) flip-flopped. Verified: "Mending Stability" / "Rendering Stability" both still appear across `references/` (names_index, deprecated_terms_registry, alias_registry, censured_vocabulary), so the split is a tracked vocabulary row, not clearly settled [UNVERIFIED which is canonical now].
  - `:54-60` Structural/Foundational Mending intentionally about 22-58% even at max pool (non-dominance by design).
  - `:103-105, :189-200` ST-TW-01 free Object-scale Weaving in protected combat rounds cites "ED-046", which does not exist (orphan).
  - `:201-211` ED-679 (Thread Warfare NPC AI doctrine) never propagated; its Niflhel §8.8 target was independently STRUCK.
  - `:84-98` combat_engine_v1 and articulation have zero thread hooks; Church is "Thread-resistant by design" (ED-679, absent-deliberate).
- **Conflicts / stale:** threadwork_v30 pre-PP-622 single-axis Ob tables retained inline (P3 elegance). `.designs/systems/threadwork/` now holds the doc.
- **Open items:** MS/RS single name before any typed export; thread hook in combat.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_victory_strategic_peninsular_sovereignty.json
- **What it is:** dossier on GD-1 Peninsular Sovereignty, peninsular_strain (Accord/Turmoil/MS/IP), GD-3 insurgency pipeline and player_agency Scene Slate; 6 findings; 198 lines.
- **Status:** none. Reading: historical; the GD-1 text is live canon (`canon/02_canon_constraints.md:70`).
- **Bears on:** FA, SE, WR, CORE.
- **Content that matters:**
  - `:3` all factions share one endpoint: hold all 15 territories, Accord >= 2, Turmoil <= 6, sustained 2 Accountings (GD-1); four faction toolkits reach Accord 2 cheaper than conquest; neglected territory decays to Uncontrolled, triggering GD-3 insurgency.
  - `:129-140` `insurgency-11-vs-15-threshold`: insurgency_pipeline_v30 §7 says "11+ territories"; GD-1, victory_v30 and sim `VICTORY_THRESHOLD=15` say all 15. LATER REFUTED (refuted.json:477-496, duplicate_of ED-1031): ED-1031 (2026-06-19, Jordan J-22) ratified ALL 15; residual stale "11" sites are insurgency §7, `canonical_sources.yaml:26` ("11/15"), params/bg/core.md, `sim/mc_v18.py:41` (`VICTORY_THRESHOLD: 11`) and `sim/provincial/mass_seizure.py:17`. NOTE the faction dossier (above, `:3`) wrongly says "11+ territories" for GD-1: the two dossiers disagree and verified canon (`canon/02_canon_constraints.md:70`) says all 15.
  - `:164-174` GD-1 canon calls the track "Political Stability" while every design doc says "Turmoil"; still true in the canon row.
  - `:186-196` GD-1 collapsed about 9 victory shapes into 1 (Omega tension, severity P2, deferred). `engine/season/ENDINGS_CLASSIFIED.yaml` is the season-loop's endings owner [UNVERIFIED how many shapes].
  - `:41-45` four-pressure design (Accord/Turmoil/MS/IP) is the anti-rush device.
  - `:79-82` insurgency formation cites only adjacency/Uncontrolled, not Gap/Knot/calamity_radiation.
- **Conflicts / stale:** `sim/autoload/victory.py` and `designs/provincial/` are gone. `canon/02_canon_constraints.md:86-87` still lists the GD-1 strike propagation as "pending" with old `designs/` paths.
- **Open items:** MS clock ownership at era transitions (tracked in module_contracts gap_notes); GD-3 sim modules "pending Pass 2l".

### .audit/2026-07-04-ners-qualitative-audit/01_workings/hunts/hunt_combat_minmax.json
- **What it is:** min-max exploit hunt on combat_engine_v1 (4 candidate "lines" + 4 findings); 76 lines. (The critic's claim that this file was missing is wrong for the tree as it stands.)
- **Status:** none. Reading: historical; engine file names from the then-checkout; code now at `modules/combat/`.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - `:6-9` armour has no wearer-side cost: `armor_defeat_sigma` (systems.py 502-513), `reach_sigma`(590)/`reopen`(644) use `REACH_W[def.armor]`; `combatant.py` never reads own armour; `equipment_health=0` unwired; ADEF_CUT -0.9. One grep of `modules/combat/*.py` for "encumb" returns nothing, consistent with the finding still being live [UNVERIFIED beyond that grep].
  - `:12-15` `impose_node` (544-557) gives counter/measure traditions a bind->riposte reward; 4 of 7 traditions hold the better imposition payoff.
  - `:18-21` `overcommit_exposure` (740-743) subtracts additive anti_overcommit + true_times(+0.25) from a floored multiplicative cost: net 0 for light hand-balanced weapon; ATTACKER_BIAS 0.12; WOUND_DEF_OB .25 > WOUND_ATK_OB .15.
  - `:24-27, :65-75` the "affinity budget" cited by config.py §153 and tradition_decomposition_v1 does not exist in `ability_primitives.py` (ability_factor/ability_bonus iterate `c.equipped` with no cap); mezzo_tempo x1.40, misura x1.15, atajo x1.18, staerke x1.20. `modules/combat/ability_primitives.py` still exists; grep for "affinity budget" in `modules engine` returned nothing, so no budget enforcement is present.
- **Conflicts / stale:** pre-R2/R3 (code re-based since; line numbers invalid).
- **Open items:** all four lines, each Omega; none shows a later fix.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/hunts/hunt_faction_minmax.json
- **What it is:** min-max exploit hunt on faction/victory/Domain Echo/GD-3; 4 lines + 4 findings; 79 lines.
- **Status:** none. Reading: historical design-level hunt on the v30 docs.
- **Bears on:** FA, SE, WR.
- **Content that matters:**
  - `:5-8, :31-41` `hegemony-accord-exemption-solves-gd1` P1 (only P1 in the faction hunt): treaty territory counts toward the 15, is EXEMPT from Accord >= 2 (peninsular_strain §6 L432, L351, ED-791) and lowers Turmoil, so sign treaties + hold one province beats conquer-and-govern; the settlement/Accord/Govern tree becomes optional. LATER REFUTED (refuted.json:120-139, DELIBERATE, P3): Turmoil <= 6 is GLOBAL (§4.1 L296 advances Strain per territory at Accord <= 1 held by ANY playable faction) so Govern is delegated not optional; treaty decay -2/season cannot outrun +3 territory instability; ED-791 restricts qualifying treaties to genuine-subordination types; treaties are breachable. A residual propagation-drift bug: §6.1 L430 over-lists Peace/Alliance vs ED-791.
  - `:11-14` Domain Echo capped 1 per scene per faction (scale_transitions §5.1) not per season; Debate Track >= 7 gives winner +1 Mandate, loser -1 (§5.4).
  - `:17-20` Mandate = clamp(round(7T/(T+6))) size-weighted means one metropolis gets Mandate 5; judged intended/N-grounded (P3).
  - `:23-26` Crown Enforce (Military vs Ob 2, -1 Presence marker/season; marker cap 5; RM spread only at Stability >= 3) can choke GD-3 emergence.
- **Conflicts / stale:** the 15-territory/treaty-counting rule is live canon in `canon/02_canon_constraints.md:70` ("treaties counting"), so the exemption concern is about subordinate docs [UNVERIFIED in code].
- **Open items:** none tracked.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/hunts/hunt_massbattle_minmax.json
- **What it is:** min-max exploit hunt on mass battle; 5 lines + 5 findings; 97 lines.
- **Status:** none. Reading: historical design-doc hunt.
- **Bears on:** MB, PC, WR (threadwork).
- **Content that matters:**
  - `:5-9, :37-48` `massbattle-general-duel-decap` P1: open every battle with a General Duel (scale_transitions §3.7, priority-8 every turn); PC cannot die (ED-898, worst case recoverable capture) while a wounded enemy general goes Stage 1 -> Stage 2 -> Command 0, flooring the whole army (1 die, Line, no tactics; PP-273 uncommanded floor). "The general IS the battle" makes Part A optional. LATER REFUTED (refuted.json:100-119, DELIBERATE, P3): the duel is bilateral (both generals must enter; unilateral entry only PAUSES the battle), §A.5 suspends BOTH sides' Command, Stage 1 only halves Command, Stage 2 needs a failed Medicine Ob 2 save the next turn; the enemy-AI-decline behaviour is unspecified (minor spec gap).
  - `:11-15` canon states split beats concentration by +9% to +45% (PP-508/ED-358) except Narrow Pass or Size=1; see contamination in dossier_mass_battle (ED-MB-0002).
  - `:17-21` Thread scale cost: §A.10 War -2/op vs a "-1/op cap, no additional surcharge" note and PP-501 example; Company-scale engagements cost 0.
  - `:23-27` Walls (+3 DR, no flanking) x Shield Wall (+2D Def) x Phase-7 idle-Morale waiver gives a cost-free siege turtle.
  - `:29-33` §3.8 pre-battle scene bonuses are free and uncapped in count.
- **Conflicts / stale:** the General-Duel exploit is a design-level claim; whether `modules/mass_battle/` has a duel path at all is [UNVERIFIED].
- **Open items:** only the splitting finding has a ledger ref (ED-358).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/hunts/hunt_social_minmax.json
- **What it is:** min-max exploit hunt on social contest (6 lines + 6 findings); 111 lines.
- **Status:** none. Reading: historical; built on the v30 doc plus the Stage 0-3 kernel (`sim/personal/contest/`).
- **Bears on:** SC, CHAR.
- **Content that matters:**
  - `:5-9` Formal-Contest Recall +2D binary per exchange (ED-617 nerf is Grand-only) + Corroborate +1D + Ex1 Prep +1D + Findings +2D; the +2D cap at v30:85 covers only genre+boost; base Charisma x2 pool becomes noise (+8D Ex1, +5D sustained).
  - `:11-15` Appraise boost is a public deterministic lookup (Church=Obscuring, Crown=Revealing, Varfell=Projection, Hafenmark=Memory; Guilds venue rule); the armature (<= 0.5 sigma) was the protected lever.
  - `:17-21` Orientation inert in the resolver (DOUBT_MARKER scope_note) while CR5 self-Face backfire is wired, so Obscuring styles are pure downside; 4 styles collapse to 2.
  - `:23-27` coalition REINFORCE (~5 track per exchange) vs solo CLASH (~0 at median), ratified in ED-297; ED-295 erosion only every 2 exchanges.
  - `:29-33` strain -> Rattled -> Face channel unwired so defensive stats are decorative.
  - `:101-109` `four-games-collapse-one-pattern` P1: a single venue-invariant optimum (coalition + matching Revealing style + Recall spam, skip Appraise/Obscuring/defence).
- **Conflicts / stale:** `modules/social_contest/` today contains only `roll.py` (+ `__init__.py`), verified by `ls`; the rebuilt Stage 0-3 kernel is NOT there, so which of these lines survive in code is [UNVERIFIED] and the SC lane should treat the kernel's location as an open question. `params/contest.md` is not present under `references/`.
- **Open items:** the P1 composite; ED-1060 terminal doubt; ED-297 coalition-dominance ratification.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/hunts/hunt_threadwork_exploit.json
- **What it is:** min-max exploit hunt on threadwork/knots/Coherence; 4 lines + 4 findings; 79 lines.
- **Status:** none. Reading: historical, design-level.
- **Bears on:** WR (threadwork), MB, FA.
- **Content that matters:**
  - `:5-9, :31-41` `coherence-cap-arbitrage` P1 (tracked ED-1010): the "-1 per-operation Coherence cap" is cited by PP-196 §3.2 and mass_battle §A.10 line 533 but defined nowhere, while the tables cost Structural/War at -2.
  - `:11-15, :43-53` Mending: §3.2 line 624 lists -1 Coherence but §2.4 asymmetry (lines 476-481) says 0; under 0 it is Coherence-free, RS +1 (Adept/Master +2), Mandate +1 via Domain Echo, and unopposable (params/threadwork.md Mending Immunity).
  - `:17-21` a practitioner-leader's Territorial Weave counts as the Domain Action, Stability +1, Echo Mandate +1 (partly checked by negative Church-territory echo, §5.6).
  - `:23-27, :66-76` Knot Anchoring Scenes uncapped (knots §8.2): +1 Coherence per Close Knot per cycle, max Knots = floor(Bonds/2)+1; makes the descent to Rendering Crisis opt-in (confidence low; bounded by rupture strain at +5).
- **Conflicts / stale:** ED-1010 reference: look in `registers/editorial_ledger*.jsonl` [UNVERIFIED]. `params/threadwork.md` gone.
- **Open items:** the cap definition, Mending's Coherence cost.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_centralization_schema.json
- **What it is:** cross-cutting lens on single-source naming machinery (names_index, descriptor_registry, glossary, engine_params); verdict MODERATE-WEAK; 8 findings; 118 lines.
- **Status:** none. Reading: historical; parts are tracked in the current registries.
- **Bears on:** PROCESS, CHAR (attribute roster), SC/WR (resonance_style, MS/RS), DICE (Combat Pool).
- **Content that matters:**
  - `:6-9, :26-35` attribute roster has two authorities (glossary 7 vs descriptor_registry/names_index 9); working tree: `references/glossary.md:53` carries an "IN FLUX" banner and `descriptor_registry.yaml:9` says "10-attribute roster ... IN FLUX until Jordan confirms", so the roster now has a THIRD count (10) and is still unsettled.
  - `:37-45` resonance_style is deprecated in the registry but live in npc_behavior §1.3; `descriptor_registry.yaml:266` records the correction (ED-IN-0025) and leaves retirement "NEEDS-JORDAN".
  - `:10, :82-92` in names_index only `world.solmund` is enforce:block; everything else is warn.
  - `:71-80` only `combat_engine_v1.json` was a typed engine_params export (the other 26 modules prose-only); CLAUDE.md §5 still states a typed layer exists for few values.
  - `:94-104` Combat Pool verified single-sourced = max(5, History+6) at core.md:161 and module_contracts:801; do not report as divergent.
  - `:12-16` Command formula (Presence+Cognition, PP-232) is written against legacy attribute names; `references/glossary.md:149` still shows it.
- **Conflicts / stale:** `references/engine_params/` and `params/*.md` no longer exist under those names (`engine/engine_params/` is the typed home per CLAUDE.md §0.05). The glossary-vs-mirror point is stale as phrased (glossary now carries its own flux banner).
- **Open items:** attribute count (7/9/10), mass_battle Command formula names, `resonance_style` retirement ruling.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_cohesion_interdependency.json
- **What it is:** cross-cutting lens on declared-vs-implemented edges between subsystems (Key emit/observe); verdict "one pipe, many dialects"; 7 findings; 105 lines.
- **Status:** none. Reading: historical and tied to the RETIRED Key substrate; the class of defect (declared consumer that does not consume) is still a valid question for the seam registry.
- **Bears on:** CORE, PC, FA, WR, PROCESS.
- **Content that matters:**
  - `:6-8` module_contracts L844 gap_note A4: `scene.combat_resolved` consumers [npc_behavior, faction_layer, articulation] do not list it; scale_transitions §12.4 L331-332: 8 down-seams / 15 type-edges with sparse targets[].
  - `:8, :34-44` domain_actions `doc:null`, `consumes:[]` (module_contracts L470-489) is the source of 3 of 8 down-seams.
  - `:11, :80-91` doc:null/[ASSUMPTION] debt clusters on connective modules (domain_actions, engine_clock, npc_memory).
  - `:58-67` `two-structural-death-points`: emitter-side sparse targets[] and consumer-side contract omission are one defect class; no gate checks that a declared consumer actually consumes.
  - `:68-79` vocabulary-layer dialects: MS/RS, Turmoil vs Political Stability, 3 enum-fork Key types, 2-cycle contract disagreement.
- **Conflicts / stale:** Key types retired; the replacement check would be `engine/season/write_matrix.yaml` / seam registry [UNVERIFIED]. `canon/mechanics_index.yaml` now `registers/`.
- **Open items:** whether the current season loop has an analogue gate.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_emergent_narrative.json
- **What it is:** lens testing whether the corpus produces emergent narrative (collision engine, autonomous world, cross-scale compounding); 8 findings; 115 lines.
- **Status:** none. Reading: historical; the strongest statement of "the emergent engine does not exist as an engine".
- **Bears on:** WR, CORE, FA, CHAR, PC.
- **Content that matters:**
  - `:3, :22-31` verdict: the 8 Convergence Markers are hand-authored annotations (arc_register_events §VI) with non-summative payloads; no resolver detects coincidence. Verified `references/arcs/` no longer exists, so the referent is gone; the "emergent engine" question now lives in `engine/season/` (loop, hole_register) [UNVERIFIED].
  - `:44-53` COLLISION C (T-24's worked example, RS+8/IP+2/TC+2) is triggered by ARC-T04 "[UNNAMED - ED-416]".
  - `:66-77` autonomous-world hole: faction_layer_v30 L490 "GM controls NPC faction votes", L362 "GM adjudicates" (still present in `.designs/systems/factions/reference/faction_layer_v30.md`, verified by grep).
  - `:78-89` autonomy trends to solvable: 9 deterministic priority trees; sim win-share about 87%/0%/0%.
  - `:90-101` cross-scale consequence propagates one hop (Domain Echo) but does not compound; cross-tick convergence unproven.
  - `:102-113` personal transformation best served but absent in combat (ED-911); arc destinations are authored menus.
- **Conflicts / stale:** all cited design docs are in `.designs/`. The AUDIT_BRIEF's measuring stick ("dynamic emergent narrative game") matches this lens's framing.
- **Open items:** a runtime home for collision markers.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_playability_legibility.json
- **What it is:** lens applying the three dramatic-legibility questions and player load to each scale; 6 findings; 104 lines.
- **Status:** none. Reading: historical for the UI docs; the cognitive-load numbers are a reusable benchmark.
- **Bears on:** GO (UI), PC, SE, FA, WR, SC.
- **Content that matters:**
  - `:3, :32-42` only Agon contest has a current-era player-interaction model (the DRAFT contest walkthrough); about 6 of 7 scales have none.
  - `:44-54` the player must hold about 27-30 named trackers across scales vs the 2026-05-08 immersion audit's own ceilings (3-4 personal, 7 strategic).
  - `:56-66` UI/UX v4.1 (CANONICAL, 2026-04-16) still specifies Taint (0-6) and CD tracks that threadwork_v30 STRUCK; proposed repair EDs (638/639/641) are occupied by other entries.
  - `:68-78` combat legibility FAILS all three questions (no per-exchange player decision, stakeless Wounds, no season hook).
  - `:7-8, :10` per-scale walk: contest PASS; faction PARTIAL; governance WEAK; combat FAIL; thread PARTIAL; season-close UNEVEN.
- **Conflicts / stale:** `designs/ui/` now `.designs/systems/ui/`; `.designs/systems/ui/` is the only copy. CLAUDE.md §0.05 says UI "Layer 3" is an unrelated sense.
- **Open items:** the commission of player-interaction models per scale (the AUDIT_BRIEF standing requirement "each subsystem is a playable game" supersedes this open question).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_sequence_lineage.json
- **What it is:** lens on the build order toward Godot, steering surfaces and supersession lineage; 7 findings; 106 lines.
- **Status:** none. Reading: stale; the Gate-0 / Key-v2 migration premise is dead (Key substrate retired) and the steering files have been replaced.
- **Bears on:** PROCESS, GO, PC, CORE.
- **Content that matters:**
  - `:5-9` Gate-0 (Key v1->v2 migration, three-doc reconciliation, Key-type registrations) unexecuted while combat (1/27 ported) received R2 (merged 07-04), R3 (PR#76), morphology audit (PR#74); engine_clock home doc "unlocated [GAP]"; no playable-season milestone.
  - `:10, :72-82` ED-912 supersession entry cites `designs/scene/articulation_layer_v30.md`, which moved; `supersession_register.yaml` frozen at ED-912 (2026-06-28), no GD-1, no mass-battle ED-MB entries.
  - `:12-13, :48-70` workplan v5 vs CURRENT.md/decision_queue contradiction on J-38; `roadmap_state.yaml` (2026-06-28, phase 2, items_done 0) stale.
  - `:94-104` no steering doc names an end-to-end playable slice; the later M1/`m1_acceptance` instrument (CLAUDE.md §0.2) answers this.
- **Conflicts / stale:** FIXED/overtaken: `roadmap_state.yaml` deleted (verified); CLAUDE.md §0.2 and `tools/m1_acceptance.py` define "done"; the one-plan-per-lane rule (CLAUDE.md §2) replaced the multi-surface steering. `registers/supersession_register.yaml` still exists [UNVERIFIED whether mass-battle rows were added].
- **Open items:** none that still bind.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_threadwork_applicability.json
- **What it is:** lens on where threadwork (P-14 inseparability) is wired vs absent, with a ranked "wire-it" list; 8 findings; 122 lines.
- **Status:** none. Reading: historical but the ranking is a usable checklist for the WR lane.
- **Bears on:** WR, PC, FA, CHAR, SE, MB, CORE.
- **Content that matters:**
  - `:3, :6` P-14's live failure shape is "a whole play mode is thread-impossible", not co-movement omission; wire-it rank: 1 combat_engine_v1 (ED-911), 2 articulation render path, 3 General Duel, 4 faction_behavior engine math, 5 NPC Priority Trees (7/9 blind), 6 settlement governance verb, 7 Scene->Mass thread channel, 8 npc_memory P-09, 9 insurgency->Gap, 10 propagation-spec.
  - `:7, :26-36` verified method: combat_engine_v1's 20 "thread" grep hits are all data-threading (no Leap/Coherence). Re-checkable today by grepping `modules/combat/*.py` for Leap/Coherence [UNVERIFIED].
  - `:12` DELIBERATELY ABSENT: Church thread-resistance (ED-679); do not wire.
  - `:13` DEFER: contest kernel thread hooks (Stage 4) and territory_temperaments coupling.
  - `:110-119` hidden preconditions: MS/RS naming fork and ED-1010/1011 per-op Coherence-cost contradictions gate wire-its 1, 4, 6, 10.
- **Conflicts / stale:** code paths dead; priority trees live in `.designs/systems/npcs/`.
- **Open items:** all ten wire-its.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_throughlines_tree.json
- **What it is:** lens mapping the throughline registry (T-01..T-41, meta-patterns M-alpha..M-11) onto subsystem dossiers as trunk/branch/orphan; 6 findings; 137 lines.
- **Status:** none. Reading: historical; the throughline registry is now `references/throughlines_meta*.md`.
- **Bears on:** WR, CORE, PROCESS.
- **Content that matters:**
  - `:16-21` four TRUNKS: cross-scale (M-delta/M-5), pressure and forced choice (M-alpha/M-1+M-6), substrate-grounds-all (M-gamma/M-3, P-14), autonomous-agent-composition (M-beta); five single-limb branches (institutions, geography, personal-transformation arcs, strategic clocks, emergent narrative).
  - `:44-55` orphan throughlines: T-31, 33, 34, 35, 37, 38, 39, 40 (M-7..M-11 phenomenology tier) "Proposed", no head; T-02/T-30 home to investigation_systems_v30, un-audited; T-26..29 prose-only.
  - `:56-61` trunkless mechanics: territory temperament alpha/beta (no consumer), Institutional Consolidation passive recovery, Recall +2D.
  - `:65-75` the M-3 trunk is the most severed (declared universal, severed at combat, articulation, faction math, 7/9 NPC trees).
  - `:125-135` no fieldwork/investigation lane in the 12-dossier set.
- **Conflicts / stale:** `references/throughlines_complete.md` is gone; `references/throughlines_meta.md` (+ infill, appendix) exists. The fieldwork gap is addressed by a live `modules/fieldwork/` (only `find.py` per `ls`) [UNVERIFIED depth].
- **Open items:** the orphan tier.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/p3.json
- **What it is:** flat list of the 33 P3-severity candidate findings (id, claim, cite, criterion, source dossier/lens/hunt) that were set aside without refutation; 410 lines.
- **Status:** none. Reading: historical bucket; every entry also appears in a dossier/lens/hunt entry above (no new claim).
- **Bears on:** PC, MB, SC, FA, SE, WR, CHAR, PROCESS.
- **Content that matters:**
  - `:2-25` pc-tradition-vacuum-balance-tension (equal affinity budget narrows build differentiation; 6.8pp spread) and pc-elegance-drift (5-tuple mode-select, per-element percussion, grip-reach oscillator JD-9).
  - `:26-61` MB: no motive/goal field for named generals; Scene->Mass bonus magnitude trivial; per-sub-unit float morale has no HUD surface.
  - `:98-121` faction: single-root Cascade default for all 6 factions; Institutional Consolidation turtle.
  - `:135-160` threadwork: orphan "ED-046"; pre-PP-622 Ob tables retained inline in threadwork_v30 §2.4.
  - `:210-233` Political Stability vs Turmoil naming (GD-1 canon text); stale Varfell Path B citation (ED-311) in victory_v30 header.
  - `:282-333` pairs with the mass-battle and faction hunt P3s (thread-scale cost contradiction, siege turtle, scene-bonus farm, Mandate saturation).
- **Conflicts / stale:** `canon/02_canon_constraints.md:70` still says "Political Stability <= 6" (verified), so the naming drift is live; the Varfell header cite is in an archived doc.
- **Open items:** none distinct from the entries above.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/refuted.json
- **What it is:** 25 candidate findings, each carrying a full refutation record (verdict, intent, revised severity, long evidence text, duplicate_of); 496 lines. The densest single source of design-intent evidence in this folder, because each refutation cites the governing ED/GD/ratification.
- **Status:** none. Reading: historical, but the refutations are the best digest of WHY the corpus is as it is; the cited docs live in `.designs/`.
- **Bears on:** PC, SC, MB, FA, SE, WR, CHAR, CORE.
- **Content that matters:**
  - `:3-19` `pc-no-player-input-hook` REFUTED (DELIBERATE, P3): `wrapper.py:352` calls `fight()` "the multi-turn SIM harness ... the GAME calls one engagement per turn"; `module_contracts` `scene.combat_strike` from `[scene_slate, player_input]` (L803); player_agency_v30:15 "14 combat actions, 6 fieldwork actions, 7 Thread operations, 4 contest styles"; state_graph.py:59-99 lists pluggable decision nodes (exchange.commit/.read/.mode/.bind_entry/.counter, burst.continuation, contact.axis). Residual: map the 14 actions onto those nodes (combat slice ports 2 of 11 modules).
  - `:80-98` `four-games-collapse-one-pattern` REFUTED to P2 (duplicate of workplan #39 / J-31-extended -> LA-19 and ED-297/ED-1060): attribute varies by venue (Expert Judge Cognition x2, Crowd Charisma x2, No Adjudicator Attunement x2); Church Tribunal opens Conjectural stasis; armature buys up to 0.50 sigma; HANDOFF_SC L60-88 Stage 4 "four games" next. Genuine residuals: no global bonus cap (L-A) and the +1D boost is a memorizable 7-row public lookup (L-B).
  - `:141-159, :21-40` GM-vote findings REFUTED (see dossier_faction): deterministic Guilds rule at §5.8 L492; `videogame_mode_spec.md` §3 L171/§4 L185 states the corpus-wide "GM adjudication -> Engine handles all resolution" translation; ED-1061 precedent.
  - `:239-257` `generalship-dominance-axiom` REFUTED: dominance means "context-independent"; Command is a derived scarce stat (Charisma+Cognition, clamp 1-7), parity decided by formations/terrain/composition/thread; ED-753, ED-1014 (Biddle 2004), ED-875 (Jordan resolve-all 2026-06-20) keep high leverage "as intended".
  - `:399-416` `deterministic-priority-trees` REFUTED: GD-2 "deterministic threat response PRECEDES stochastic action selection" (canon/02:39, HR-9) and ED-874 set the faction resolver to deterministic+stochastic; ED-693 Church repetition intentional; non-dominance is about the PLAYER strategy space, not NPC randomness. Residual: npc_behavior §8 predates and does not cite GD-2.
  - `:418-435` `resonant-style-lookup-collapse` REFUTED: NPCs have Primary AND Secondary RS; styles mutate (§5.1 triggers, arcs); §6.4 "Church Martyrdom Extension" scopes the penalty to Church NPCs and fires only on a loss; ED-519 SIM-validated the +3D stack "not degenerate".
  - `:298-317, :338-358` settlement: governance-redesign-orphaned REFUTED (G1 settlement registry IS built: `sim/territory/registry.py`+`ledger.py`, 6 passing tests; `goldenfurt_slice/` 5 artifacts, stages S0-S1 landed); legibility-partial-settlement-tier REFUTED (partial duplicate of the playability lens; governor tenure risk is readable from Order/Defense, §4.3/§1.4.3/§5.1). Thread Exploitation Faucet REFUTED (`:318-337`): shared-RS commons externality, Warden interdiction, Wealth+1/RS-0.5 is the cost.
  - `:219-238` scene-mass-bonus-unconsumed REFUTED (duplicate_of ED-151; the table lives in scale_transitions as the single home; ED-151 PROVISIONAL / P1-BLOCKER in `tests/sim/sim_h01_to_h07`); `:456-476` key-vocabulary-enum-fork REFUTED as dup of KC-1 (`open_decisions.md:18`: "structural->persistent, medium->near"; `compute_salience` would KeyError on "medium").
- **Conflicts / stale:** `refute` notes cite scratch files under `designs/audit/...` (dead) and one writes the literal path `/home/user/ttrpg/undefined/` (a bug in the audit pipeline, three occurrences: `:116, :354, :414`). The tracked ED numbers are real ledger rows to check in `registers/editorial_ledger*.jsonl`; I did not verify them. Notably `mass-battle default flips` are not discussed.
- **Open items:** the unbuilt 14-action mapping; the L362 "GM adjudicates" clause; the global-bonus cap; Scene->Mass "most relevant unit" adjudication for a no-GM engine.

### .audit/2026-07-04-ners-qualitative-audit/01_workings/tracked.json
- **What it is:** 62 findings labelled KNOWN-TRACKED (an existing ED, queue item or register row already covers them), each with its tracked_ref; 807 lines.
- **Status:** none. Reading: historical index; no new claim beyond the dossier/lens entries, but the `tracked_ref` column is the map from finding to ED.
- **Bears on:** all, mainly PC, WR, CORE, FA, PROCESS.
- **Content that matters:**
  - ED-911 (open, P1) is the recurring ref: combat_engine_v1 has zero threadwork integration (`:3-14, :29-40, :757-768, :783-794`, plus 6 other entries). The ED lives in `registers/editorial_ledger_pc.jsonl` or the main file [UNVERIFIED].
  - ED-1006 (open): era transitions unkeyed + 3-way piety/conviction_track collision (`:237-248, :471-482, :484-495`); ED-1051: doc:null `[ASSUMPTION]` backlog; ED-1010/1011: per-op Coherence-cost contradictions (`:432-443`); ED-428/731/772: MS/RS (`:172-183, :575-586, :666-677`); ED-1060: Terminal Doubt (`:406-417`); ED-297: coalition dominance (`:419-430`); ED-MB-0002 invincibility baseline (`:42-53`); propagation_spec item 18 cross-tick convergence.
  - `:588-599` `combat-resolved-double-bottleneck` (module_contracts L808/L823/L844 gap_note A4): payload scene_id/outcome/participants/casualties/wounds_inflicted, not consumed by the three declared consumers.
  - `:680-690` only `combat_engine_v1.json` typed export; `:692-703` Combat Pool = max(5, History+6) reconciled.
  - `:718-742` Gate-0 (Key v1->v2) unexecuted; engine_clock home "unlocated [GAP]".
  - `:380-391` sim win-share about 87%/0%/0%, decision_queue item 8.
- **Conflicts / stale:** All Key-substrate refs (`scene.*`, Gate-0 Key v2 migration, key_type_registry) are retired with ED-IN-0232. Whether ED-911 / ED-1006 are still open: [UNVERIFIED], one `grep ED-911 registers/*.jsonl` would tell.
- **Open items:** the ED-911 combat-thread gap; the 87% win-share.

### .audit/2026-07-04-ners-qualitative-audit/_workings_joined.md
- **What it is:** a generated verbatim concatenation (`tools/join_audit_workings.py`, Jordan 2026-08-04 "join them all together and purge the excess") of 41 fragments of the 2026-07-04 qualitative NERS audit: charter + 3 grounding files, the workings README, critic notes, 5 dossier .md, hunts, lenses, and 22+ per-finding refutation notes; 3492 lines. I read all of it.
- **Status:** none of its own ("A fragment's Status line still describes the FRAGMENT"); the grounding files and README say `RATIFIED (Jordan, 2026-07-05, accepted as filed; PR #77)`. Reading: historical record; the markdown versions largely duplicate the JSON entries above, with extra prose and full refutation reasoning.
- **Bears on:** PROCESS (audit method), PC, SC, MB, FA, SE, WR, CORE, CHAR, GO.
- **Content that matters:**
  - `:25-124` the charter: North Star (Godot emergent grand-strategy / tactical-management / political-sim / narrative RPG), master question, criteria (Intent-of-game, Omega 4 clauses cross-scale / personal transformation / autonomous world / non-dominance, Q-robust/smooth/elegant with the dramatic-legibility test "whose position is at risk; what does each named actor want; what happens if no one acts next season", N-Necessity tier-0), six directions, severity scale P1/P2/P3, KNOWN-item calibration list (`:91-118`: spear dominance 84-96%, ED-911, ED-1010/1011/913/414/931, 10 doc:null modules, values_master quarantined, ~87% win-share, Godot 1/27).
  - `:129-224` criteria lineage: NERS informal definition (`references/simulation_workplan_v1.md` §2.1) superseded by throughlines_meta (PP-672/674); N is tier-0 "flag, never auto-reject"; dramatic-legibility is a game-state/screen bar, not per-subsystem in isolation (this is why `pc-legibility-fails` was refuted).
  - `:227-309` interdependency map: 11 coupling edges (Faction-Settlement densest; Domain Echo bottom-up channel; Thread-Faction §3.5 "the thread op IS the Domain Action"; General Duel §3.7; Fieldwork "9 named handoffs" highest fan-out §3.9; contest-npc 2-cycle; faction_state self-loop drift_coef 0.6/season; Peninsular Strain gates g_ip100/85/80; settlement-mass battle; dice substrate; articulation sink); module_contracts: 10 doc:null, 11 [ASSUMPTION], 6 orphan/thin.
  - `:312-396` threadwork surface: Leap pool `(Spirit x2)+History+TPS`, TS >= 30, Mending the only Coherence-free op, Three-Axis Ob (PP-622/623); declared junctures; silent junctures; ED-679 never propagated; open flags ED-911, ED-1010, ED-1011, ED-913, ED-414, ED-931.
  - `:399-428` workings README: 55 agents (12 dossiers + 5 hunters + 7 lenses + 30 refuters + critic); 157 candidates = 5 confirmed + 25 refuted + 62 tracked + 33 P3 + 32 deferred; synthesised deliverable was `../ners_qualitative_audit_v1.md` (one level up; not in my assignment).
  - `:2267-3491` the per-finding refutation notes (full text) for 22 findings; the long ones that matter for design intent: articulation-thread-silence (ED-936 "articulation universal"), four-games-collapse (workplan #39, ED-297, ED-1060, HANDOFF_SC Stage 4: Dowlen weighted lottery, liberum-veto consensus, Putnam two-level), general-duel (consent-gated, symmetric Command suspension), hegemony (Turmoil global), deterministic priority trees (GD-2 `canon/02:39`, HR-9, ED-874), governance-redesign (G1 registry built, goldenfurt_slice), ui-spec (stale-CANONICAL v4.1; per-subsystem walkthrough method, decision 5, 2026-07-01).
- **Conflicts / stale:** Everything cites `designs/`, Key types and `sim/` paths that no longer exist (verified `designs/` absent; `registers/mechanics_index.yaml` replaces `canon/`). `canon/definitions.yaml` "does NOT exist" (`:63`). One verified live item: `canon/02_canon_constraints.md:70` still uses "Political Stability" and `:86-87` lists the GD-1 propagation as "pending". Two internal inconsistencies: the faction dossier text (`:665`, `:780`) says GD-1 is "11+ territories" whereas GD-1 is all 15 (ED-1031).
- **Open items:** ED-151 modifier calibration; the L362 "GM adjudicates" clause; ED-1060 Terminal Doubt; the 14-action combat mapping; none has a visible closing artifact in this folder.

### .audit/2026-07-04-ners-qualitative-audit/ed_options.md
- **What it is:** 12 drafted ED candidates (E-1..E-12) from the NERS audit, each as a ready JSON ledger line; 104 lines; 2026-07-04, ratification addendum 2026-07-05.
- **Status:** `RATIFIED (Jordan, 2026-07-05 - ALL 12 accepted and FILED in the ledger; forks resolved to audit defaults)`. Reading: historical decision record; the filing table at `:91-104` is the useful part.
- **Bears on:** SE, WR, PC, SC, MB, FI, CORE, PROCESS.
- **Content that matters:**
  - Filing map (`:93-104`): E-1 `ED-SE-0001` (settlement governance: adopt the redesign path), E-2 `ED-IN-0003` (Convergence Marker detector/applier), E-3 `ED-IN-0004` (articulation trigger omissions), E-4 `ED-IN-0005` (per-subsystem walkthrough policy for UI/UX v4.1 staleness), E-5 `ED-WR-0001` (sweep peninsular_strain), E-6 `ED-IN-0006` (steering surfaces), E-7 `ED-IN-0007` (register back-propagation gate), E-8 `ED-WR-0002` (MS wins over RS), E-9 `ED-PC-0001` (combat player-interface + ED-911 as named increments), E-10 `ED-SC-0001` (dominance sweeps), E-11 `ED-IN-0008` (naming authority), E-12 `ED-FI-0001` (audit the investigation lane).
  - `:20-22` E-2's proposed design: a registry of trigger-pairs checked per Accounting, emitting a convergence-marker event; candidate home `game_director`.
  - `:55-57` E-9: "wrapper.engagement() has no player-decision parameter (verified; DELIBERATE sim-first staging per refutation R-1)" - the final audit adopted DELIBERATE staging but asked to schedule both the input surface and ED-911 post-R3.
  - `:60-62` E-10 lists the unverified hunt lines to re-sweep: Recall/Corroborate/Prep stacking vs a global cap; boost-lookup vs Appraise; solo floor under ED-297; armour no-downside; imposition asymmetry; ability-stacking budget ("config prose claims one while ability_primitives enforces none").
  - `:69-72` E-12: `investigation_systems_v30` and fieldwork overlap un-audited; orphan T-02/T-30.
- **Conflicts / stale:** I grepped `registers/editorial_ledger*.jsonl`: `ED-SE-0001`, `ED-WR-0001`, `ED-WR-0002`, `ED-PC-0001`, `ED-SC-0001`, `ED-FI-0001` appear in the `*_archive.jsonl` files (rows show a later `superseded` or `closed` status for SE-0001, WR-0001, WR-0002, PC-0001, FI-0001 - file order, last-wins reading [UNVERIFIED]); `ED-IN-0004`, `ED-IN-0008` in `editorial_ledger_in_archive.jsonl`; `ED-IN-0003` and `ED-IN-0005` were not found by that grep. So most of these 12 were closed or superseded by later work; E-9's "ED-PC-0001" was reused as U0 in the PC sequence (consolidation_v1 allocates ED-PC-0001 to U0), an ID collision worth a look [UNVERIFIED which row the ledger holds].
- **Open items:** whether the Convergence Marker detector (E-2) was built (the `engine/season/` loop is where it would live); whether UI/legibility walkthroughs exist for scales other than contest.

### .audit/2026-07-04-weapon-morphology-granularity/README.md
- **What it is:** 18-line abstract of the weapon-morphology granularity audit set (lane PC, 2026-07-04).
- **Status:** `PROPOSED, Jordan-vetoable - lane PC - no ED-PC IDs allocated yet - no canonical file touched` (stale: audit_v1 was later ratified by PR #74 merge and its sequence executed). Reading: superseded by the status lines inside `audit_v1.md` and `consolidation_v1.md`.
- **Bears on:** PC.
- **Content that matters:**
  - `:5-11` trigger: a silhouette-reconstruction exercise showed a faithful renderer had to INVENT blade width and edge symmetry (the latter as a hand-authored 21-weapon set).
  - `:12-18` the audit's output: four primitives P1-P4 with "absent => identity" defaults, S-graded grounding, mass-closure anti-fabrication loop, five tranches T1-T5; HIGH balance risk is the `cross_section` -> `gap` armour-defeat chain.
- **Conflicts / stale:** status line predates ratification; files `u9_adversarial_review_v1.md` and `u9_capstone_v1.md` sit in the same folder but were not assigned to me.
- **Open items:** none.

### .audit/2026-07-04-weapon-morphology-granularity/audit_v1.md
- **What it is:** Fable-tier design audit of how to add morphology primitives (edge topology, blade profile, grippable zone, guard axis) to the bottom-up weapon model; 437 lines; 2026-07-04, lane PC.
- **Status:** `RATIFIED-by-merge (PR #74, ED-1094) - T1-T5 SUPERSEDED-IN-PART` (by `consolidation_v1.md` section 4). Reading: analysis still the rationale source for P1-P4; tranche plan superseded.
- **Bears on:** PC, DICE, GO (port re-export).
- **Content that matters:**
  - `:43-80` inventory of stored primitives (`elements[]{x_m,extent_m,mass_kg}`, `guards[]`, `haft`, `pommel`, `edge_undulation`, `adornments`, `head` token, `mode_elements[]`) and five baked geometry scalars (`curvature`, `point_concentration`, `cross_section`, `edge_keenness`, `strike_concentration`) with their consumers; states "what it cannot say" is anything transverse or topological about the blade.
  - `:88-178` ranked gaps G1 edge topology (single/double/edgeless + false-edge fraction), G2 width/thickness profile, G3 grippable element (retires name-keyed `HALFSWORD_FORM`), G4 guard axis ambiguity (`guards[].extent_m` transverse vs `elements[].extent_m` axial), G5 flexibility derived, G6 taper.
  - `:190-320` P1 `elements[].edges = dict(sides, false_edge_frac)`; P2 `profile = dict(width_base_m, width_tip_m, thickness_base_m, thickness_tip_m, section_fill)` staged P2-a data + closure, P2-b `rigidity_derived` parity, P2-c cross_section swap (Jordan-gated); P3 `grippable`; P4 guard `span_m`/`depth_m`.
  - `:323-338` wiring map: P2-c is the HIGH-risk surface (`w['gap']` -> `adef_cap` armour-defeat tier list); oracle rule: re-export from Python, never edit the port (ED-1050).
  - `:411-426` anti-fabrication register: every new constant `[SIM-CALIBRATE]`; mass-closure +/-20% report-only; rho_iron 7860 and `UNIT_M` 0.30 are existing sourced constants.
  - `:428-437` four loud questions for Jordan (T5 ordering, flamberge half-sword, P2 campaign scope, renderer home).
- **Conflicts / stale:** `consolidation_v1.md` F1-F3 correct it: `clinch` was deleted by R2 I7b; the P4 rename `extent_m -> span_m` is wrong for langets (guards already carry `orient_deg`); `geo['halfsword']` has zero readers. Working tree (grep in `modules/combat`): `false_edge_frac`, `grippable`, `edge_lines`, `affords_halfsword`, `LEGIB_EDGELINE_K` exist (P1/P3 built); `section_fill`, `rigidity_derived`, `span_m`, `has_spine`, `SPINE_WIND_K` do NOT (P2 profile data and P4 rename not built, spine renamed); `HALFSWORD_FORM` still defined at `weapons.py:926`.
- **Open items:** P2 profile data campaign and rigidity parity table (T-P2); the cross_section swap (T5); the renderer script is "confirmed genuinely gone" (JD-8).

### .audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md
- **What it is:** Fable adjudication that merges the R3 plan (A, closing-distance/weapon-model, 9 increments) with the morphology audit (B) into one PC-lane sequence U0..U9 + T-P2 + T5; 162 lines; 2026-07-04, with 2026-07-08 and 2026-07-22 status updates in the header.
- **Status:** `RATIFIED - plan-of-record for the PC lane, ratified by merge of PR #72 per ED-1094`; header records JD-1 RULED, JD-4 and JD-9 DETERMINED (2026-07-08), U3/U5/U7 executed byte-identical and U9 executed (2026-07-22: "capstone ablation found NO lever robustly clears the ~+/-4pp noise floor"). Reading: live as record of the PC build sequence; JD-2/3/5/6/7/8 stay OPEN per the header.
- **Bears on:** PC (primary), DICE, GO.
- **Content that matters:**
  - `:21-55` verified-facts pass: V1/V2 `thrust_factor` and `geo['halfsword']` dead (zero readers); V3 `HALFSWORD_FORM` is a 2-name dict `{longsword, estoc}`; V6 live percussion mace 8.00 pinned at `PERC_CAP`, poleaxe 7.48 (cap inversion); V8 baseline `8 failed, 166 passed, 1 xfailed`; V7 PoB bias table (cinquedea -1.8 cm, greatsword 30.4); F1-F6 misreads (clinch deleted, guard `orient_deg`, renderer script never committed).
  - `:59-91` per-overlap verdicts: edges encoded as B's `{sides, false_edge_frac}` with A's table as migration data; half-sword = B's `grippable` flag + A's derived-form generator, REJECT A's threshold-tuned predicate ("a whitelist smuggled through thresholds"); one channel per physical fact: cut-line entropy -> legibility only (`LEGIB_EDGELINE_K`), spine -> `bind_sigma` (drop `SPINE_WIND_K`), grab hazard -> `contact.grab_sigma`, thrust-trueness deferred behind P2 and U2.
  - `:109-122` the table U0 units honesty (x0.30 into metres), U1 PoB recalibration (ED-PC-0010 done 2026-07-08), U2 graded mode affordance + percussion enactment (ED-PC-0008/0009/0011 done, residual ED-PC-0012 sabre-class `THRUST_AUTH_REF` open), U3 edges, U4 half-sword from attested grip, U5 polearm choke counterbalance, U6 retreat-as-default with cost, U7 weapon-class-aware facing, U8 guard hygiene, U9 capstone, T-P2, T5.
  - `:124-132` ordering is forced: PoB -> graded modes+percussion -> capstone -> cross_section swap; "there is no separate future Phase C left after U9".
  - `:150-158` open forks: JD-2 edge FLAG rows (tsurugi double, yari, paired_short, falchion clip, kissaki 0.15, estoc edgeless), JD-3 half-sword roster expansion (flamberge, greatsword, bastard/war swords = new anti-plate capability), JD-5 back-swing framing, JD-6 P2 scope (blades-first), JD-7 T5 sequencing, JD-8 renderer.
  - `:153` JD-4 resolved: `weapon_physics.reversed_grip_percussion(w)` (hilt assembly mass, `REVERSED_GRIP_EFFICIENCY=0.25` [FIAT, HEMA-grounded Mordhau], reads 1.4-1.8/8 for two-handed swords); `:158` JD-9: `thrust_factor` floor dropped, `MODE_EDGE_MIN`/`MODE_TIP_MIN` = 0.15.
  - `:162` U2 scope note: `core.coupling`'s `DELIVERY` constants do not scale with percussion magnitude except vs mail/plate, so any weak blunt option wins selection vs unarmoured targets (a separate architectural gap).
- **Conflicts / stale:** the header names U3/U5/U7/U9 as executed but is silent on U6 (retreat-as-default with cost) and U8; the PC dossier (`dossier_personal_combat.json:80`) had U6 PENDING. One grep of `modules/combat/*.py` for `RETREAT_GATE` and `retreat_prob` (the U6 symbols) returns NOTHING, so U6 appears not to be built, or was removed, in the live module [UNVERIFIED which]; the AUDIT_BRIEF PC intent (retreat as a player choice) makes this a live question. The ED-PC numbering reuses ED-PC-0001 (U0) while ed_options.md E-9 filed `ED-PC-0001` as a different item.
- **Open items:** JD-2, JD-3, JD-5, JD-6, JD-7, JD-8 (header lists them open as of the last edit); ED-PC-0012 sabre-class thrust fix; T5 re-baselines; P2 profile data.

### .audit/2026-07-04-weapon-morphology-granularity/edges_data_v1.md
- **What it is:** worker output table: per-element `edges = {sides, false_edge_frac}` with S-grades for 51 non-`base` weapons (half-sword forms skipped); 158 lines; no date, PC lane (U3 migration data).
- **Status:** none. Reading: historical data input; the live data are the `edges` in `modules/combat/weapons.py`. Cites `/home/user/ttrpg/systems/combat/combat_engine_v1/weapons.py` (`systems/combat/combat_engine_v1` still exists in the tree; the live code is `modules/combat/`).
- **Bears on:** PC.
- **Content that matters:**
  - `:7-40` the invariant-1 conflict table: `edge_keenness` of a multi-mode composite must be read per `mode_elements[i].geometry`, not top-level (poleaxe beak/spike 0.00, bec_de_corbin 0.00, hook_sword crescent 0.05, guandao notch 0.10, fauchard hook 0.05; voulge heel spike 0.15 genuinely blocks `sides=0`).
  - `:28-37` data-gap forced calls (S3): dangpa flank tines, spetum and partisan wings, voulge rear_fluke inherit whole-weapon ek > 0.1, so an edgeless reading is structurally unavailable; "good candidates for future per-element mode_elements".
  - `:54, :61, :103, :115` flagged JD-2 calls: paired_short sides=2 (lowest-confidence, S2), yari sides=2, tsurugi sides=2 (counter to "Japanese = single"), estoc sides=0 confirmed.
  - `:76, :100-102, :107-110, :116` false-edge fractions: katana/tachi/odachi 0.15 (kissaki), naginata 0.15, sabre 0.2, szabla 0.2, falchion 0.2, scimitar 0.15, changdao 0.1, shamshir/pulwar/nandao 0.
- **Conflicts / stale:** invariant `sides == 0 => edge_keenness <= 0.1` is the CI invariant named in audit_v1; `modules/combat/weapons.py:878` assigns `_el['edges'] = _ed` from an edge table, so the data are applied by a table at import; whether every row here matches that table is [UNVERIFIED].
- **Open items:** JD-2 FLAG rows were landed "provisional" per consolidation default; no later ruling visible here.

### .audit/2026-07-04-weapon-morphology-granularity/u10_activation_v1.md
- **What it is:** U10 implementation record (ED-PC-0022): reverses the U9 "keep all six levers at K=0" verdict by re-homing the choke-thrust cost, building a tradition-modulation surface and activating the levers to small values; 198 lines; 2026-07-23.
- **Status:** `RATIFIED (by merge of PR #226, 2026-07-23, per ED-1094 - no section was held back)`; abilities "illustrative/provisional content". Reading: live record of how the five morphology levers and four seed abilities came to be; later edited by ED-PC-0026 and ED-PC-0035 per code comments.
- **Bears on:** PC (primary), DICE, CHAR (traditions/abilities).
- **Content that matters:**
  - `:24-31` the four fiats that kept levers inert: F1 wrong instrument (aggregate winrate), F2 amputated tradition surface (`ability_primitives.eff_cw`/`ability_factor` not wired to any of the six levers), F3 choke-thrust cost parked against the D2 force invariant, F4 near-invisible facing constants (`FACING_VOID_K=0.08`, `FACING_PROFILE_K=0.03`).
  - `:44-49` `phi_grip('point')` is now grip-invariant unconditionally; `CHOKE_THRUST_K`/`CHOKE_THRUST_FLOOR` retired; the choke control cost lives only in `CHOKE_ACCURACY_K`. This dissolved the U9 `needs_jordan` (no D2 amendment).
  - `:50-56` baselines: `LEGIB_EDGELINE_K=0.04`, `BIND_SPINE_K=0.03`, `GRAB_EDGE_K=0.07`, `CHOKE_ACCURACY_K=0.03`, `FACING_REGIME_K=0.12`; verified live in `modules/combat/config.py:55-68, :223`.
  - `:58-66` four seed abilities `shinogi` (japanese, spine_press x1.6), `zwerchhau` (german, edge_read x1.6), `ringen_am_schwert` (german, edge_grab x0.4), `guardia` (italian, facing_regime x1.5); `choke_control` has a hook but no ability. Working tree: `ability_primitives.py:22-27, :57-59` shows `zwerchhau` was RE-HOMED to `counter_select` x1.4 and `guardia` REMOVED (ED-PC-0026), so this table is partly superseded.
  - `:83-103` RETRACTION of a "+2.8pp specialist edge" (a confound: `german+ability` vs `none+empty`); isolated, the abilities' aggregate edge is about 0.
  - `:138-168` four-perspective adversarial review (ED-PC-0023): correctness CLEAN, NERS pessimist SAFE (no runaway, no new degenerate win-share), balance found the confound, grounding found `winden` a category error (a longsword technique wired to a single-edge lever).
  - `:172-198` the correct instrument for a situational lever is event-divergence with outcome preservation: levers-on vs off at identical seeds, katana vs arming 16% of fights differ, 3% change winner; dagger vs arming 28%/8%; sabre vs longsword 21%/8%. Decision: keep the activation.
- **Conflicts / stale:** the dossier-era claim that choke/retreat were open is superseded; `modules/combat/config.py:130` records ED-PC-0035 removed `CHOKE_BIND_K` (a structural zero). The claim "combat suite: 9 accepted-red baseline" is date-bound (2026-07-23).
- **Open items:** broader grounded ability content across more traditions (this record's own admission: aggregate effect about 0 so far); `choke_control` ability gap; C1 polearm facing direction unresolved (`:31`).

