# Generation register — G_generation currency layer (NS4)

Deterministic, working-tree only. **Measures; does not gate** — `tools/ci_generation_consistency.py` is the (WARN-only) gate for the currency invariant this reuses. LIVE head = registered in `references/canonical_sources.yaml` (`canonical_docs()`), recognized `## Status:` (`status_of()`/`RECOGNIZED`), and NOT a `superseded_ids()` entry — everything else, including registered-but-unrecognized-status docs, is HISTORICAL by default (never flagged for a stale pointer). See the script docstring for the disclosed scope limits (no `head_pointers.yaml` yet; `extract_file_refs()` only catches directory-prefixed, quoted/backtick paths — a bare shorthand citation like `derived_stats_v1` with no path is invisible to it).

**Scorecard:** live-heads=54 (strict currency-rule count 54, 0 demoted by the path/banner tie-break — see below), historical=1814 (of 1868 `.md` files classified); registered-canonical-docs=88 (34 registered-but-not-live); stale-pointers-in-live-heads=97 (across 30 head(s)); unregistered-canonical=0; currency-drift=1.

> **Scope disclosures (capstone reconciliation, ED-IN-0056):**
> - **#9 — this measures currency-partition HEALTH, not v40 ADOPTION.** All three detections (stale pointers, unregistered heads, drift) can read zero while ZERO live heads carry a legible `v40` marker — a green scorecard here is compatible with no v40 transition at all. Measuring v40-marker adoption needs the WS3 `head_pointers.yaml` + a `Generation: v40` stamp, which do not exist yet; until they do, "NS4 meter" means "the live/historical partition is clean," NOT "v40 is adopted."
> - **#11 — `canon/`, `registers/`, `references/`, and `params/` paths can NEVER be LIVE heads here.** The reused `ci_generation_consistency.DOC_KEYS` extraction hard-anchors captured paths to a literal `designs/` prefix, so a current head such as `params/core.md` (named live in `CURRENT.md`) is unconditionally HISTORICAL to this layer — a structural, corpus-wide blind spot beyond the four detection-2 DOC_KEYS examples already disclosed. Widening it is a `ci_generation_consistency.py` change (that rule lives once, §8), not a gen_audit patch.

## Currency drift — registered as a canonical head AND recorded as superseded (reuses `ci_generation_consistency.py`'s own drift check)

- `systems/combat/combat_v30.md`

## Stale version-pointers in LIVE heads — a `_vNN.md` reference that is superseded, moved (successor exists), or genuinely nonexistent (the `combat_v30`-partial-supersession class)

**Severity triage** — a missing target is NOT automatically dead. Split by reason: **1 superseded** (target exists but is a supersession-register entry — repoint at the successor head); **53 moved** (target missing, but the restructure ledger `references/restructure_ledger.md` maps it to a NEW path that exists on disk — a trivial one-line repoint to the shown `new_home`, NOT an investigation; reused from `broken_dependency_checker._load_restructure_map()`); **43 genuinely nonexistent** (no restructure-ledger successor — a real dead/drifted citation, a typo, OR a still-open forward-reference to explicitly-flagged pending future work; this tool does not distinguish those last three). Only the nonexistent bucket needs a human; superseded/moved are mechanical repoints.

- `systems/_architecture/derived_stats_v30.md` -> `designs/personal/conviction_taxonomy_v30.md` (moved) — now at `systems/characters/conviction_taxonomy_v30.md`
- `systems/_architecture/holonic_container_doctrine_v1.md` -> `designs/architecture/key_substrate_v30.md` (nonexistent)
- `systems/_architecture/key_substrate_v30.md` -> `designs/architecture/key_type_registry_v30.md` (nonexistent)
- `systems/_architecture/key_substrate_v30.md` -> `designs/architecture/propagation_spec_v1.md` (nonexistent)
- `systems/_architecture/key_substrate_v30.md` -> `designs/articulation/articulation_layer_v30.md` (nonexistent)
- `systems/_architecture/key_substrate_v30.md` -> `designs/personal/conviction_axis_matrix_v30.md` (moved) — now at `systems/characters/conviction_axis_matrix_v30.md`
- `systems/_architecture/key_substrate_v30.md` -> `designs/personal/conviction_track_v1.md` (moved) — now at `systems/characters/conviction_track_v1.md`
- `systems/_architecture/key_substrate_v30.md` -> `designs/provincial/faction_behavior_v30.md` (moved) — now at `systems/factions/faction_behavior_v30.md`
- `systems/_architecture/key_type_registry_v30.md` -> `designs/architecture/key_substrate_v30.md` (nonexistent)
- `systems/_architecture/propagation_spec_v1.md` -> `designs/architecture/holonic_container_doctrine_v1.md` (nonexistent)
- `systems/_architecture/propagation_spec_v1.md` -> `designs/architecture/key_echo_armature_v1.md` (nonexistent)
- `systems/_architecture/propagation_spec_v1.md` -> `designs/architecture/key_substrate_v30.md` (nonexistent)
- `systems/_architecture/propagation_spec_v1.md` -> `designs/architecture/scale_transitions_v30.md` (nonexistent)
- `systems/_architecture/scale_transitions_v30.md` -> `designs/audit/2026-06-11-orchestration/valoria_authoritative_graph_v1.md` (nonexistent)
- `systems/articulation/articulation_layer_v30.md` -> `designs/architecture/key_substrate_v30.md` (nonexistent)
- `systems/articulation/articulation_layer_v30.md` -> `designs/architecture/key_type_registry_v30.md` (nonexistent)
- `systems/articulation/articulation_layer_v30.md` -> `designs/personal/conviction_taxonomy_v30.md` (moved) — now at `systems/characters/conviction_taxonomy_v30.md`
- `systems/articulation/articulation_layer_v30.md` -> `designs/provincial/faction_behavior_v30.md` (moved) — now at `systems/factions/faction_behavior_v30.md`
- `systems/articulation/articulation_layer_v30.md` -> `designs/world/narrative_voice_canon_v30.md` (nonexistent)
- `systems/characters/conviction_axis_matrix_v30.md` -> `designs/architecture/key_substrate_v30.md` (nonexistent)
- `systems/characters/conviction_axis_matrix_v30.md` -> `designs/personal/conviction_taxonomy_v30.md` (moved) — now at `systems/characters/conviction_taxonomy_v30.md`
- `systems/characters/conviction_migration_roster_v30.md` -> `designs/personal/conviction_axis_matrix_v30.md` (moved) — now at `systems/characters/conviction_axis_matrix_v30.md`
- `systems/characters/conviction_migration_roster_v30.md` -> `designs/personal/conviction_taxonomy_v30.md` (moved) — now at `systems/characters/conviction_taxonomy_v30.md`
- `systems/characters/conviction_taxonomy_v30.md` -> `designs/personal/conviction_axis_matrix_v30.md` (moved) — now at `systems/characters/conviction_axis_matrix_v30.md`
- `systems/characters/conviction_taxonomy_v30.md` -> `designs/personal/conviction_migration_roster_v30.md` (moved) — now at `systems/characters/conviction_migration_roster_v30.md`
- `systems/factions/faction_behavior_v30.md` -> `designs/architecture/key_substrate_v30.md` (nonexistent)
- `systems/factions/faction_behavior_v30.md` -> `designs/architecture/key_type_registry_v30.md` (nonexistent)
- `systems/factions/faction_behavior_v30.md` -> `designs/personal/conviction_axis_matrix_v30.md` (moved) — now at `systems/characters/conviction_axis_matrix_v30.md`
- `systems/factions/faction_behavior_v30.md` -> `designs/personal/conviction_taxonomy_v30.md` (moved) — now at `systems/characters/conviction_taxonomy_v30.md`
- `systems/factions/faction_canon_v30.md` -> `designs/npcs/character_canon_v30.md` (nonexistent)
- … 67 more (see `data/g_generation.json`)

## Unregistered canonical heads — confidence caveat before acting

These are flagged because their `## Status:` HEADING leads with CANONICAL/CURRENT, and `status_of()` (the reused, first-match-wins parser) reads only that heading line. Several docs in this corpus carry a CANONICAL/CURRENT heading immediately contradicted by a later bolded `**Status:** PROVISIONAL …` line the parser never sees (real, swept 2026-07-13: ≥11 docs, incl. `designs/territory/march_layer_v30.md`, `designs/territory/settlement_adjacency_v30.md`, `systems/factions/fractional_province_ownership_v30.md`). "Declares a canonical-family heading" therefore ≠ "is settled CANONICAL" — verify the body's `**Status:**` line before registering any of these. Not fixed in-tool: writing a second, laxer status-line parser is exactly what §8 (every rule lives once) forbids — the one parser is `ci_generation_consistency.status_of()`.

## Unregistered canonical heads — genuinely never mentioned in `canonical_sources.yaml` (the true `conviction_track_v1.md` class, PR #131 P1-B; NOTE: that exact example is not reproduced here — its Status line is an HTML comment `status_of()` cannot parse, see the script docstring)
(none)

## Unregistered canonical heads — mentioned in `canonical_sources.yaml`, but under a key name `canonical_docs()`'s `DOC_KEYS` regex does not match (e.g. `adjacency:`, `social_contest_design:` — a regex blind spot in the reused function itself, not a true missing-registration; disclosed separately, not silently merged into the class above)
(none)

## Lower-confidence — registered canonical docs that do not qualify as LIVE (no `## Status:` line, or a non-standard one; not itself a finding, context only)

- `systems/_architecture/campaign_architecture_v30_index.md` (no_status)
- `systems/_architecture/complete_systems_reference.md` (nonstandard_status:PARTIALLY SUPERSEDED (combat sections) — banner added 2026-07-01 (ED-1084))
- `systems/_architecture/player_agency_v30_index.md` (no_status)
- `systems/_architecture/videogame_mode_spec_index.md` (no_status)
- `systems/characters/character_histories_v30_index.md` (no_status)
- `systems/characters/conviction_track_v30.md` (no_status)
- `systems/characters/conviction_track_v30_index.md` (no_status)
- `systems/combat/combat_v30.md` (superseded)
- `systems/factions/ci_political_v30.md` (no_status)
- `systems/factions/faction_layer_v30.md` (no_status)
- `systems/factions/faction_politics_v30_index.md` (no_status)
- `systems/fieldwork/fieldwork_v30_index.md` (no_status)
- `systems/fieldwork/investigation_systems_v30_index.md` (no_status)
- `systems/mass_battle/mass_battle_v30_index.md` (no_status)
- `systems/mass_battle/military_layer_v30.md` (no_status)
- `systems/npcs/baralta_v30.md` (no_status)
- `systems/npcs/companion_specification_v30.md` (no_status)
- `systems/npcs/npc_behavior_v30_index.md` (no_status)
- `systems/npcs/npc_relational_graph_v30.md` (no_status)
- `systems/npcs/npc_roster_v30.md` (no_status)
- … 14 more (see `data/g_generation.json`)
