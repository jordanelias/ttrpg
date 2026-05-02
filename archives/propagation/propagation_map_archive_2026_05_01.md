# Propagation Map Archive — Batch 2026-05-01

# Archived from references/propagation_map.md to maintain size limits.
# Entries dated 2026-04-19 through 2026-04-19
# 3 entries archived.

## 2026-04-19 — PP-668 OPEN ITEMS propagation (completes PP-667)

**Commit:** (this commit)
**Scope:** propagate PP-667 gap-sweep resolutions into the source-doc OPEN ITEMS tables. Closes the deferred propagation work flagged in PP-667.

**Files:**
- designs/territory/settlement_layer_v30.md §9 — 9 items with final status (4 RESOLVED, 1 CONFIRMED, 1 SUPERSEDED by PP-666, 2 DEFERRED, 1 N/A).
- designs/provincial/military_layer_v30.md §5 — 9 items (6 RESOLVED, 3 DEFERRED).
- designs/provincial/peninsular_strain_v30.md §8 — 7 items (4 CONFIRMED, 1 RESOLVED, 1 SUPERSEDED by PP-663, 1 N/A).
- designs/provincial/faction_layer_v30.md §10 — 9 items (7 RESOLVED, 2 DEFERRED).
- designs/provincial/victory_v30.md §11 — ED-311 CLOSED.

All new statuses reference PP-667 and the resolution document `designs/audit/gap_resolution_2026-04-19.md`.

**Registers:**
- canon/patch_register_active.yaml: PP-668 entry.
- references/canonical_sources.yaml: co-file touch.

**Consequences:** none new. Completes PP-667 propagation. No new editorial ledger entries needed (resolutions already logged under ED-713/714/715 in PP-667).

## 2026-04-19 — PP-670 Label accuracy audit

**Commit:** (this commit)
**Scope:** audit of all files with deprecation-suffix names (`_deprecated`, `_legacy`, `_historical`, `_superseded`). 71 files reviewed.

**Findings:**
- `designs/npcs/npc_roster_caste_annotations_deprecated.md`: correctly labeled. Merge into `npc_roster_v30.md §14` verified.
- `designs/threadwork/threadwork_v25_historical.md`: mislabel — filename said historical but no internal banner. **Fixed** — banner added pointing to canonical `threadwork_v30.md`.
- `tests/sim/sim_ttrpg_batch_legacy_02/03/04.md`: filename-only labels, no internal banners. Deferred as low-priority test-layer work.
- All 57 files in `deprecated/` directory correctly placed per `deprecated/README.md` policy.
- `params/threadwork_superseded.md`: correctly labeled internally, location intentional.

**Registers:**
- canon/patch_register_active.yaml: PP-670 entry.
- canon/editorial_ledger.yaml: ED-716 resolution entry.
- references/canonical_sources.yaml: co-file touch.

**Deferred:** sim_ttrpg_batch_legacy banner pass — not a blocker. Low reader-hazard; names are self-describing.

## 2026-04-19 — PP-671 Meta-throughline synthesis

**Commit:** (this commit)
**Scope:** synthesize 5 meta-throughlines from the 25 game throughlines; provide evaluative criteria for design proposals.

**New file:** references/throughlines_meta.md (15k chars)

**Meta-throughlines identified:**
- M-1 Decay-as-default — entropic baseline, instantiated by 8 throughlines
- M-2 Substrate-as-universal-medium — rendering/thread ontology across all systems, instantiated by 8 throughlines
- M-3 Institutional identity = mechanical attractor — each faction's distinct substrate-relationship, instantiated by 5 throughlines
- M-4 Scale-preserving chains — same throughlines fire at multiple scales, instantiated by 9 throughlines
- M-5 Forced-choice architecture — irreducible tradeoffs at every significant choice point, instantiated by 6 throughlines

**Findings:**
- Hafenmark, Löwenritter, and RM all lack their own institutional-attractor throughlines (M-3 gap). ED-717 logs this.
- PP-666's three new systems (settlement adjacency, fractional ownership, succession split) each strongly satisfy multiple meta-throughlines — validates PP-666 as vision-aligned design.
- Throughline-interaction matrix is sparse (7 throughlines covered of 25); recommended for future expansion.

**Registers:**
- canon/patch_register_active.yaml: PP-671 entry.
- canon/editorial_ledger.yaml: ED-717 entry (M-3 faction under-spec).
- references/canonical_sources.yaml: cross-reference note.

**No mechanical changes.** Pure synthesis / meta-analysis document.

