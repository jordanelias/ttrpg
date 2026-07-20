# Completeness critic — full working notes (2026-07-04)

Role: completeness critic for the whole qualitative-NERS audit. Assessed the audit scratch dir
against the charter (12 dossier lanes, 7 lenses, 5 hunt arenas, six directions/subsystem,
threadwork-at-every-juncture, shape/sequence artifacts first-class). cwd working tree only.

## Method
- Read charter + all three grounding files (00/01 charter/criteria, 02 interdependency, 03 threadwork).
- Full file listing w/ sizes + wordcounts of every dossier/lens/hunt.
- Full read: dossier_registers_graphs (519 w — thinnest), lens_sequence_lineage.
- Spot-read heads: refute_sim-conviction-taxonomy-stale (npc), refute_collision-engine-has-no-engine (arch).
- Grepped for per-lane coverage of settlement/npc/architecture/combat-hunt + artifact consultation.

## What EXISTS (artifact census)
Dedicated dossier files (5 of 12 lanes): mass_battle, faction_political, articulation (in articulation/),
victory_strategic, registers_graphs.
Lens files (7 of 7): throughlines_tree, emergent_narrative, playability_legibility,
cohesion_interdependency, centralization_schema, sequence_lineage, threadwork_applicability. COMPLETE.
Hunt files (4 of 5): social, massbattle, faction, threadwork. **MISSING: hunt_combat_minmax.**
Refutations (~13 refute_*.md scattered across findings/ refutation/ refutations/ refutation_notes/
verify/ lanes/ articulation/ — inconsistent foldering).

## Coverage gaps (concrete)

### G1 — settlement_territory lane effectively unaudited (P1 completeness gap)
No dossier_settlement_territory, no hunt, no refute. Only incidental mentions inside cross-lane lens
files. This is the DENSEST coupling edge in the corpus (interdependency §a.1 Faction↔Settlement,
Mandate=clamp(round(7T/(T+6))), LPS-2e math, mean-reverting L/PS drift) and the mass-battle location
substrate (§a.9). Its threadwork junctures (grounding-03 §2: settlement_layer §4.4 thread ops, §4.9
thread-exploitation sites, governance_play Thread event family) are named in grounding but verdicted
present/absent by NO dossier. Single weakest lane; must become an explicit [GAP:] in the report.

### G2 — 7 of 12 lanes have no consolidated six-direction dossier
personal_combat, social_contest, threadwork, npc_behavior, architecture_spine, recent_infra,
settlement_territory lack a dossier_*.md. Coverage summary's `missing_dossier_lanes:[]` is misleading:
these lanes were touched via lens/hunt/refute fragments, not a per-subsystem six-direction pass. Lead
subsystems personal_combat and threadwork — the two the charter foregrounds most — have NO dossier;
their signal is dispersed across refutes + one hunt + one lens. Synthesis will read fragments and risks
implying full six-direction coverage where none was assembled. (Fragment quality is high — the refutes
are deep and well-grounded — but the six-direction discipline was not applied per-subsystem for these 7.)

### G3 — npc_behavior collapsed to refutations
Both npc candidate findings (sim-conviction-taxonomy-stale, gm-controls-npc-votes) were REFUTED.
No surviving NPC dossier signal. conviction_track_v1.md (an explicit lane target) is examined only
through the refuted taxonomy finding, whose own verdict points at KNOWN-TRACKED ED-1006/PP-718 as the
true root. So the NPC/conviction lane produced zero retained NEW findings and no positive dossier — a
lane that ran but returned empty. Worth a note that absence-of-finding here is under-evidenced (was the
concern/opinion/project/arc engine and npc_memory writer actually swept? No artifact shows it).

### G4 — hunt_combat_minmax missing (P2)
No combat min-max artifact. Spear/polearm dominance is deferred to the KNOWN calibration item (R2 merged
PR#72, R3 in flight PR#76). BUT: R2 was a closing-distance REDESIGN and R3 a weapon-model consolidation —
a fresh degenerate-play sweep against the NEW post-R2/R3 model was not done. Deferring the whole combat
hunt to a calibration line that describes the PRE-redesign exploit is a real coverage hole: the redesign
could have opened a new dominant line nobody swept. Charter allows KNOWN-TRACKED + new-scope evidence.

### G5 — top-down direction thin (20 across 12 lanes, <2/lane)
Philosophy→mechanic judgments underdeveloped per-subsystem. N-Necessity (Renaissance-political grounding)
and Ω-non-dominance (no solvable strategy) top-down verdicts are the charter's tier-0/tier-1 instruments
but appear concentrated in the throughlines/emergent lenses, not exercised against each subsystem head.
Several lanes likely have no explicit P-01..15 / GD-1..3 top-down verdict.

### G6 — forwards direction thinnest (15) and concentrated
Nearly all forwards signal lives in lens_sequence_lineage (Gate-0, engine_clock, playable-season
milestone). Per-dossier forward reads (this subsystem's Godot end-state sequencing) are sparse for
combat/social/faction. Acceptable if the sequence lens is treated as the canonical forwards home, but
the report should say so rather than imply each dossier carried its own forwards axis.

### G7 — shape/sequence artifacts unevenly consulted
registers_graphs dossier (the SHAPE lane) is thin (519 w) and SKIMMED several charter §3 artifacts:
03_canonical_timeline (skim), patch_register_active (skim ~150 lines), canonical_sources (first 120
lines + grep). NOT confirmed read anywhere: tools/observability/decisions.json (only DECISIONS.md),
references/id_reservations.yaml, per-lane handoffs/HANDOFF_<LANE>.md. These are named first-class inputs.
The id_reservations/HANDOFF omission means in-flight lane work may not be reflected — resumed-from-stale
risk the audit itself could carry.

### G8 — scene.combat_resolved down-seam under-verdicted
Interdependency §a.2: scene.combat_resolved is declared-but-unconsumed (registry says
npc_behavior/faction_layer/articulation consume it; their consumes: lists don't). refute_scene-mass-bonus
handles the scene→mass side only. The combat_resolved→{npc,faction,articulation} down-seam (a diagonal
juncture) is not verdicted by any dossier — and with no personal_combat OR npc dossier, no lane owns it.

### G9 — surviving-signal synthesis not yet bound
Only 5 of 157 findings verified-survived; 25 refuted, 32 deferred-unverified. The surviving set is small
and cross-corroborating signals are split across lanes without a synthesis artifact reconciling them:
register back-propagation blindness appears in BOTH registers_graphs (supersession/canonical_sources
blind to ED-MB/FIELD_MOVEMENT/PER_CELL flips) AND sequence_lineage (register frozen at ED-912, no GD-1
Partition, no contest-rebuild); steering-surface fragmentation (CURRENT.md vs workplan-v5 vs
roadmap_state contradiction) is a sequence-lens finding that touches every lane's currency. These want a
synthesis pass that names them as corpus-level, not lane-local.

### G10 — refutation files scattered across 6 subdirs
findings/ refutation/ refutations/ refutation_notes/ verify/ lanes/ articulation/ + root all hold
refute_*.md with no manifest. Not a substantive gap but a synthesis-legibility hazard: a synthesizer
globbing one dir will miss refuted candidates and could resurrect a refuted finding as novel.

## Bottom line
Refutation quality is high and the lens layer is complete, so the audit CAN be synthesized — but
structurally uneven: 5/12 lanes have true dossiers, settlement_territory is nearly unaudited, the combat
hunt is missing against a freshly-redesigned model, and top-down/forwards axes are thin per-subsystem.
The report must carry explicit [GAP:] entries for settlement_territory, the dossier-less lanes, the
combat hunt, and the unread shape/sequence artifacts rather than present 12-lane coverage as complete.
