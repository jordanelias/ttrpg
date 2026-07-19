# VALORIA — Corpus Fix Manifest
## Remaining sweep work from mechanical_terms_index audit
**Date:** 2026-05-07
**Status:** MANIFEST — file list for future sweep sessions. Not all items require changes; some may be contextual references that are acceptable.

---

## SWEEP 1: Four-Cardinal Structure → Four-Virtue Structure (§V.2 #3)

**Severity:** LOW
**Rationale:** "Cardinal" as NPC role collides with "Cardinal" as cardinal-virtues structural frame. Rename frame only; preserve NPC title.

### Active files containing "Four-Cardinal":
| File | Hit count | Notes |
|------|-----------|-------|
| designs/world/worldbuilding_v30_index.md | 2 | Auto-generated index — will regenerate |
| references/glossary.md | 1 | Definition entry — primary rename target |
| canon/03_canonical_timeline.md | — | Check context |
| designs/world/worldbuilding_v30_infill.md | — | Check context |
| designs/provincial/faction_canon_v30.md | 5+ | Heavy usage: cascade roots, member list, officer structure |
| designs/provincial/faction_state_authoring_v30.md | — | Check context |
| designs/provincial/faction_politics_v30_index.md | — | Auto-generated |
| designs/provincial/faction_politics_v30.md | 5+ | Heavy usage: Church institutional logic, rank ladder, Dicastery |
| designs/world/worldbuilding_v30.md | — | Primary definition source |

### Rename rules:
- "Four-Cardinal Structure" → "Four-Virtue Structure"
- "Four-Cardinal" (when referring to the structural frame) → "Four-Virtue"
- "Cardinal" (when referring to the NPC role) → KEEP unchanged
- "four-cardinal apparatus" → "four-virtue apparatus"
- Compound phrases like "the Cardinal of the player's specialty branch" → KEEP (NPC reference)

---

## SWEEP 2: Legacy Ethical-Framework Labels (§V.2 #7)

**Severity:** MEDIUM
**Rationale:** PP-684 replaced all legacy ethical frameworks with the 13-Conviction taxonomy. Active docs should use Conviction names.

### Per-label file lists (active docs only, excluding deprecated/archives/tests):

#### "Categorical Imperative" (~36 active files)
<<<<<<< HEAD
Includes: params/bg/core.md, params/contest.md, params/factions/npc_stance_triangles.md, designs/personal/conviction_taxonomy_v30.md, designs/arcs/arcs_31_35.md, designs/npcs/npc_foils_v30_infill.md, designs/npcs/npc_behavior_v30.md, designs/ui/valoria_ui_ux_v4.md, designs/npcs/character_canon_v30.md, designs/arcs/gm_ref/arcs_05_09.md, designs/arcs/gm_ref/arcs_41_45.md, references/alias_registry.yaml, designs/arcs/emergent_scenarios.md, canon/patch_register_active.yaml, designs/arcs/arc_expansion_v30.md, references/valoria_complete_systems_r2.md, references/numeric_bounds_report.yaml, audit/lane-a/valoria_holistic_audit.md, designs/provincial/faction_canon_v30.md, designs/scene/investigation_systems_v30.md, designs/provincial/faction_politics_v30.md, designs/npcs/npc_character_analyses_v30_infill.md, designs/scene/social_contest_v30.md, designs/scene/social_contest_system_v2.md, designs/provincial/factions_personal_v30.md, designs/provincial/faction_behavior_v30.md, and others.
=======
Includes: params/bg/core.md, params/contest.md, params/factions/npc_stance_triangles.md, designs/personal/conviction_taxonomy_v30.md, designs/arcs/arcs_31_35.md, systems/npcs/npc_foils_v30_infill.md, systems/npcs/npc_behavior_v30.md, systems/ui/valoria_ui_ux_v4.md, systems/npcs/character_canon_v30.md, designs/arcs/gm_ref/arcs_05_09.md, designs/arcs/gm_ref/arcs_41_45.md, references/alias_registry.yaml, designs/arcs/emergent_scenarios.md, canon/patch_register_active.yaml, designs/arcs/arc_expansion_v30.md, references/valoria_complete_systems_r2.md, references/numeric_bounds_report.yaml, designs/audit/valoria_holistic_audit.md, designs/provincial/faction_canon_v30.md, designs/scene/investigation_systems_v30.md, designs/provincial/faction_politics_v30.md, systems/npcs/npc_character_analyses_v30_infill.md, designs/scene/social_contest_v30.md, designs/scene/social_contest_system_v2.md, designs/provincial/factions_personal_v30.md, designs/provincial/faction_behavior_v30.md, and others.
>>>>>>> origin/main

#### "Divine Command" (~28 active files)
Similar distribution as above.

#### "Virtue Ethics" (~39 active files)
Largest footprint. Includes character_canon, npc_roster, npc_behavior, conviction_taxonomy, conviction_migration_roster, faction_politics, worldbuilding, arc docs.

#### "Epistemic Reason" (~9 active files)
Smaller footprint: params/bg/core.md, conviction_taxonomy, conviction_migration_roster, character_canon, strategic_layer.

#### "Rawlsian" (~31 active files)
Wide distribution: npc_roster, npc_behavior, arc_expansion, faction_canon, faction_behavior, conviction_track, social_contest.

### Replacement rules:
Per conviction_migration_roster_v30.md. Each legacy label maps to specific Conviction(s):
- "Categorical Imperative" → varies by character; check migration roster
- "Virtue Ethics" → "Virtue (Conviction #12) + Self-Other orientation"
- "Divine Command" → "Faith (Conviction #1) + Authority (Conviction #2)"
- "Epistemic Reason" → "Scholastic (Conviction #4)"
- "Rawlsian" → "Equity (Conviction #6)"
- "Military Honor" → "Honor (Conviction #13)"

**IMPORTANT:** Some occurrences are in historical/contextual passages explaining the migration itself. These should retain the legacy label with a note like "(legacy — now Conviction #N)". Only active mechanical references should be renamed.

### Recommended approach:
1. Read conviction_migration_roster_v30.md for per-character/faction mappings
2. Process files in groups: params/ first (3 files), then designs/scene/ (canonical system docs), then systems/npcs/ (character docs), then designs/provincial/ (faction docs)
3. Each file: check context — is the label used mechanically (rename) or historically (annotate)?

---

## SWEEP 3: TC Residuals (§V.2 #8)

**Severity:** LOW-MEDIUM (mostly cosmetic; no mechanical error)
**Rationale:** ED-782 renamed Theocracy Counter (TC) → Church Influence (CI). Residual TC abbreviations in non-canonical docs.

### Fixed this session:
- ✓ designs/provincial/mass_battle_v30.md (1 TC→CI)
- ✓ systems/npcs/npc_character_analyses_v30_infill.md (2 TC→CI)
- ✓ references/throughlines_meta_infill.md (0 hits — clean)

### Remaining files with TC (active, non-deprecated):
From GitHub code search — includes both "Theocracy Counter" and standalone `\bTC\b`:

**High priority (canonical system docs):**
| File | Notes |
|------|-------|
| references/glossary.md | Definition entry — update |
| references/alias_registry.yaml | Collision table entry — may be intentional (documenting the rename) |
| references/censured_vocabulary.yaml | Should list TC as censured — verify |
| references/values_master.yaml | Check if TC appears as a value key |
| references/canonical_sources.yaml | Check references |
| designs/scene/conviction_track_v30.md | §3 heading: "TC Generation" — this is the canonical doc; rename to "CI Generation" |
| designs/provincial/ci_political_v30.md | Already uses CI; check for residual TC |

**Medium priority (design docs):**
| File | Notes |
|------|-------|
| designs/architecture/campaign_modes_v30.md | |
| designs/provincial/factions_personal_v30.md | |
| designs/provincial/factions_personal_v30_infill.md | |
| designs/provincial/strategic_layer_v30_infill.md | |
| designs/provincial/faction_canon_v30.md | |
| designs/provincial/faction_politics_v30.md | |
| designs/world/southernmost_v30.md | |
| designs/scene/combat_v30.md | |
| systems/npcs/npc_foils_v30.md | |
| systems/threadwork/threadwork_v30_infill.md | |
| designs/arcs/narrative_scenario_chains.md | |
| designs/arcs/gm_ref/arcs_10_18.md | |
| designs/arcs/gm_ref/arcs_36_40.md | |
| designs/arcs/gm_ref/arcs_46_55.md | |
| designs/arcs/gm_ref/arcs_46_55_resolved.md | |

**Low priority (audit/reference docs):**
Multiple audit docs, atoms_pending, UI docs, architecture docs.

### Replacement rule:
- "Theocracy Counter" → "Church Influence"  
- "TC" (standalone abbreviation in mechanical context) → "CI"
- "TC" in headings like "TC Generation" → "CI Generation"
- "TC" in alias_registry collision_table → KEEP (documenting the rename history)
- "TC" in censured_vocabulary → KEEP (it should be there as censured)

---

## SWEEP 4: Conviction-Name Mechanic-Context Cross-References (§V.2 #6)

**Severity:** LOW (documentation hygiene)
**Scope assessment:** Every place a Conviction word (Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor) appears in a mechanic description context, add an inline cross-reference to the §1.5 Conviction definition.

This is primarily relevant in:
- designs/scene/social_contest_v30.md — Contest Style names
- designs/provincial/faction_behavior_v30.md — faction Cascade math
- params/contest.md — Pressure Point types (now Sanction replaces Authority)

**Approach:** Deferred to a documentation pass. Low mechanical risk.

---

## SESSION CHANGES LOG

| File | Change | Status |
|------|--------|--------|
| params/contest.md | Pressure Point "Authority" → "Sanction" | COMMITTED |
| designs/provincial/mass_battle_v30.md | TC → CI (1 occurrence) | COMMITTED |
| systems/npcs/npc_character_analyses_v30_infill.md | TC → CI (2 occurrences) | COMMITTED |
| references/mechanical_terms_index.md | New file: diagnostic glossary with GAPs resolved | COMMITTED |
| references/corpus_fix_manifest.md | New file: this manifest | COMMITTED |
