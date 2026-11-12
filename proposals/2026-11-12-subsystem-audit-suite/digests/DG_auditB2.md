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
- **Conflicts / stale:** note that `hunt_combat_minmax.json` DOES exist in this directory (assigned file 17), so gap at `:16-18` was closed after the critic ran (or the critic checked a different place); the content of that hunt is the one file where the claim was re-checked below.
- **Open items:** none that any later artifact seems to answer; the audit was superseded by the 2026-10 ners audit (`references/ners_audit_2026-10-14.md` exists).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/deferred_unverified.json
- **What it is:** 28 findings that were neither confirmed nor refuted (deferred, unverified), each with subsystem, claim, cite, criterion, direction, severity, novelty; 397 lines.
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
  - `:149-158` `gm-controls-npc-votes` P1: faction_layer_v30 §5.8 said "GM controls NPC faction votes (Guilds, Niflhel)" (Guilds reduced to 3 hard-coded if/then rules); contradicts no-GM. The sentence is STILL in `.designs/systems/factions/reference/faction_layer_v30.md` (grep) but that is an archived doc; the refuted status is recorded in refuted.json (see that entry).
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
  - `:170-179` `sim-conviction-taxonomy-stale` (claimed sim CONVICTIONS = legacy 9 vs ratified 13) - later REFUTED per the critic; today `engine/season/harness/conviction_spread.py:13` refers to "the thirteen CONVICTIONS", so the 13-set is the live reading.
  - `:156-168` module_contracts' social_contest and npc_behavior blocks disagree on whether the 2-cycle damper is BOUNDED; the live line at `references/module_contracts.yaml:475` still says BOUNDED with "affect_axis clamp is NOT in canon".
- **Conflicts / stale:** `sim/personal/conviction.py` is gone. `designs/npcs/` now `.designs/systems/npcs/`. `canon/mechanics_index.yaml` now `registers/mechanics_index.yaml`.
- **Open items:** P-09 (memory must be messy/costly/detectable) has no mechanical surface for `npc_memory` (doc:null at the time).

### .audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_personal_combat.json
- **What it is:** dossier on personal combat (combat_engine_v1: wrapper.fight/engagement, continuous sigma-leverage engine, scene_combat_design_v1); 6 findings; 192 lines.
- **Status:** none. Reading: historical; the engine now lives in `modules/combat/` (verified: `wrapper.py`, `config.py`, `combatant.py` exist there).
- **Bears on:** PC, DICE, CHAR.
- **Content that matters:**
  - `:3` loop: Approach, AwaitTempo, Exchange (commit depth 2-5, mode select, sigma via `core.roll_net`/degree), Bind/Riposte/HitLanded, Felled/Separation; pool = max(5, History+6); bilateral-Ob wounds (ED-1041).
  - `:123-133` `pc-no-player-input-hook` P1 (NEW): `engagement(A,B,first,cfg,rng)` has no player-decision parameter; commit depth, mode, grip-choke, retreat-vs-press are all engine/RNG-resolved, "build-time loadout plus autoresolve". Matches the PC design intent in AUDIT_BRIEF (player-held choice) and is the strongest PC finding in this folder.
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
- **What it is:** dossier on settlement_layer_v30 / territory (17 provinces, 37 settlements, governance verb, Mandate<->L/PS loop); 7 findings; 255 lines. Written to fill the critic's "unaudited" gap? No: it is dated alongside the critic and is the only settlement dossier.
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

