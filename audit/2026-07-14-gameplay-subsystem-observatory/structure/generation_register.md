# Generation register — G_generation currency layer (NS4)

Deterministic, working-tree only. **Measures; does not gate** — `tools/ci_generation_consistency.py` is the (WARN-only) gate for the currency invariant this reuses. LIVE head = registered in `references/canonical_sources.yaml` (`canonical_docs()`), recognized `## Status:` (`status_of()`/`RECOGNIZED`), and NOT a `superseded_ids()` entry — everything else, including registered-but-unrecognized-status docs, is HISTORICAL by default (never flagged for a stale pointer). See the script docstring for the disclosed scope limits (no `head_pointers.yaml` yet; `extract_file_refs()` only catches directory-prefixed, quoted/backtick paths — a bare shorthand citation like `derived_stats_v1` with no path is invisible to it).

**Scorecard:** live-heads=56 (strict currency-rule count 57, 1 demoted by the path/banner tie-break — see below), historical=1707 (of 1763 `.md` files classified); registered-canonical-docs=93 (36 registered-but-not-live); stale-pointers-in-live-heads=16 (across 7 head(s)); unregistered-canonical=4; currency-drift=1.

> **Scope disclosures (capstone reconciliation, ED-IN-0056):**
> - **#9 — this measures currency-partition HEALTH, not v40 ADOPTION.** All three detections (stale pointers, unregistered heads, drift) can read zero while ZERO live heads carry a legible `v40` marker — a green scorecard here is compatible with no v40 transition at all. Measuring v40-marker adoption needs the WS3 `head_pointers.yaml` + a `Generation: v40` stamp, which do not exist yet; until they do, "NS4 meter" means "the live/historical partition is clean," NOT "v40 is adopted."
> - **#11 — `canon/`, `references/`, and `params/` paths can NEVER be LIVE heads here.** The reused `ci_generation_consistency.DOC_KEYS` extraction hard-anchors captured paths to a literal `designs/` prefix, so a current head such as `params/core.md` (named live in `CURRENT.md`) is unconditionally HISTORICAL to this layer — a structural, corpus-wide blind spot beyond the four detection-2 DOC_KEYS examples already disclosed. Widening it is a `ci_generation_consistency.py` change (that rule lives once, §8), not a gen_audit patch.

## Currency drift — registered as a canonical head AND recorded as superseded (reuses `ci_generation_consistency.py`'s own drift check)

- `designs/scene/combat_v30.md`

## Stale version-pointers in LIVE heads — a `_vNN.md` reference that is superseded, moved (successor exists), or genuinely nonexistent (the `combat_v30`-partial-supersession class)

**Severity triage** — a missing target is NOT automatically dead. Split by reason: **1 superseded** (target exists but is a supersession-register entry — repoint at the successor head); **10 moved** (target missing, but the restructure ledger `references/restructure_ledger.md` maps it to a NEW path that exists on disk — a trivial one-line repoint to the shown `new_home`, NOT an investigation; reused from `broken_dependency_checker._load_restructure_map()`); **5 genuinely nonexistent** (no restructure-ledger successor — a real dead/drifted citation, a typo, OR a still-open forward-reference to explicitly-flagged pending future work; this tool does not distinguish those last three). Only the nonexistent bucket needs a human; superseded/moved are mechanical repoints.

- `designs/arcs/throughline_resolutions_v30.md` -> `designs/mechanics/baralta_crown_claim_v30.md` (moved) — now at `designs/provincial/baralta_crown_claim_v30.md`
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/caste_integration_v1.md` (nonexistent)
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/faction_politics_expanded_v1.md` (moved) — now at `designs/provincial/faction_politics_v30.md`
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/npc_behavior_v30.md` (moved) — now at `designs/npcs/npc_behavior_v30.md`
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/player_agency_v30.md` (moved) — now at `designs/architecture/player_agency_v30.md`
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/rank_ladder_v1.md` (nonexistent)
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/settlement_layer_v30.md` (moved) — now at `designs/territory/settlement_layer_v30.md`
- `designs/arcs/throughline_resolutions_v30.md` -> `designs/systems/throughline_resolutions_v1.md` (moved) — now at `designs/arcs/throughline_resolutions_v30.md`
- `designs/provincial/faction_politics_v30.md` -> `designs/conviction_track/conviction_track_v30.md` (moved) — now at `designs/scene/conviction_track_v30.md`
- `designs/provincial/mass_battle_integration_v30.md` -> `designs/scene/combat_v30.md` (superseded)
- `designs/provincial/parliamentary_transfer_v30.md` -> `designs/provincial/einhir_revival_v30.md` (nonexistent)
- `designs/world/calamity_radiation_v30.md` -> `designs/fieldwork/fieldwork_v30.md` (moved) — now at `designs/scene/fieldwork_v30.md`
- `designs/world/calamity_radiation_v30.md` -> `designs/ttrpg/threadwork_redesign_v25.md` (moved) — now at `designs/threadwork/threadwork_v25_historical.md`
- `designs/world/calamity_radiation_v30_infill.md` -> `designs/ttrpg/threadwork_redesign_v25.md` (moved) — now at `designs/threadwork/threadwork_v25_historical.md`
- `designs/world/insurgency_pipeline_v30.md` -> `designs/audit/2026-05-15-handoff/handoff_2026-05-15_v15.md` (nonexistent)
- `designs/world/insurgency_pipeline_v30.md` -> `designs/provincial/restoration_movement_v30.md` (nonexistent)

## Unregistered canonical heads — confidence caveat before acting

These are flagged because their `## Status:` HEADING leads with CANONICAL/CURRENT, and `status_of()` (the reused, first-match-wins parser) reads only that heading line. Several docs in this corpus carry a CANONICAL/CURRENT heading immediately contradicted by a later bolded `**Status:** PROVISIONAL …` line the parser never sees (real, swept 2026-07-13: ≥11 docs, incl. `designs/territory/march_layer_v30.md`, `designs/territory/settlement_adjacency_v30.md`, `designs/provincial/fractional_province_ownership_v30.md`). "Declares a canonical-family heading" therefore ≠ "is settled CANONICAL" — verify the body's `**Status:**` line before registering any of these. Not fixed in-tool: writing a second, laxer status-line parser is exactly what §8 (every rule lives once) forbids — the one parser is `ci_generation_consistency.status_of()`.

## Unregistered canonical heads — genuinely never mentioned in `canonical_sources.yaml` (the true `conviction_track_v1.md` class, PR #131 P1-B; NOTE: that exact example is not reproduced here — its Status line is an HTML comment `status_of()` cannot parse, see the script docstring)
(none)

## Unregistered canonical heads — mentioned in `canonical_sources.yaml`, but under a key name `canonical_docs()`'s `DOC_KEYS` regex does not match (e.g. `adjacency:`, `social_contest_design:` — a regex blind spot in the reused function itself, not a true missing-registration; disclosed separately, not silently merged into the class above)

- `designs/provincial/fractional_province_ownership_v30.md` — CANONICAL
- `designs/scene/social_contest_v30.md` — CANONICAL — approved 2026-04-17 (editorial batch acceptance). Supersed
- `designs/territory/march_layer_v30.md` — CANONICAL
- `designs/territory/settlement_adjacency_v30.md` — CANONICAL

## Live heads demoted by an authoritative-path tie-break (NOT scanned for stale pointers)

These pass the strict currency rule (registered, recognized `## Status:`, not superseded) but are demoted to HISTORICAL by an AUTHORITATIVE override — a physical archival path (`archives/`/`deprecated/`/`designs/audit/`/`handoffs/`) or a ledger/register path — because a doc filed as a record is a record whatever its `## Status:` line says (e.g. a registered-CANONICAL plan under `designs/audit/`). Since the ED-IN-0055 reconciliation, `vector_audit.banner_classify()`'s weak CONTENT-keyword no longer demotes a registered head (it was false-hitting the word "audit" in live-head prose), so this list is now path/superseded-only. Disclosed, not silently dropped: a demotion here can still mask a real stale pointer in that doc.

- `designs/audit/2026-05-17-v18-integration/integration_plan_v18.md` (archival_path)

## Lower-confidence — registered canonical docs that do not qualify as LIVE (no `## Status:` line, or a non-standard one; not itself a finding, context only)

- `designs/architecture/campaign_architecture_v30_index.md` (no_status)
- `designs/architecture/complete_systems_reference.md` (nonstandard_status:PARTIALLY SUPERSEDED (combat sections) — banner added 2026-07-01 (ED-1084))
- `designs/architecture/player_agency_v30_index.md` (no_status)
- `designs/architecture/videogame_mode_spec_index.md` (no_status)
- `designs/arcs/arc_expansion_v30_index.md` (no_status)
- `designs/arcs/throughline_resolutions_v30_index.md` (no_status)
- `designs/npcs/baralta_v30.md` (no_status)
- `designs/npcs/companion_specification_v30.md` (no_status)
- `designs/npcs/npc_behavior_v30_index.md` (no_status)
- `designs/npcs/npc_relational_graph_v30.md` (no_status)
- `designs/npcs/npc_roster_v30.md` (no_status)
- `designs/npcs/npc_roster_v30_index.md` (no_status)
- `designs/npcs/npc_roster_v30_infill.md` (no_status)
- `designs/provincial/ci_political_v30.md` (no_status)
- `designs/provincial/clock_registry_v30.md` (no_status)
- `designs/provincial/clock_registry_v30_infill.md` (no_status)
- `designs/provincial/faction_layer_v30.md` (no_status)
- `designs/provincial/faction_politics_v30_index.md` (no_status)
- `designs/provincial/mass_battle_v30_index.md` (no_status)
- `designs/provincial/military_layer_v30.md` (no_status)
- … 16 more (see `data/g_generation.json`)
