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

