# Critic pass — C4 (Tracks & clocks)

Antagonist relay over `dossier_C4.md` (independent read-only verification).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| C4-F1 | **soften** (P1→P2) | Confirmed: clock_registry_v30.md registered at canonical_sources.yaml:419-423, cited at module_contracts.yaml:255,276,516,543,644,654,663 (itself a module at :789-802), zero CURRENT.md hits. But this is a navigation/index gap, not a wrong-value ingestion path — contracts' inline comments carry the real numerics (e.g. IP start :516). The wrong-value risk is separately captured in F2. |
| C4-F2 | **uphold** | Torben Loyalty start=3 (PP-498) on the self-declared CANONICAL page vs params/bg/core.md:82 "PP-599: start 7... PP-498 start 3 superseded"; corroborated by npcs_special.md:2 and arcs_46_55_resolved.md:80. HANDOFF_IN.md:177 names it, uncited to any ED. P1/KNOWN-UNTRACKED stands. |
| C4-F3 | **uphold** | All four assertions verified: BG=28 (bg/core.md:82; ci_seizure.md:120; parliament.md); campaign_modes.md:46 TTRPG=15 citing nonexistent params_factions_ttrpg.md; factions_personal.md has no CI start (only generation rates :97-101); clock_registry:17 unqualified 28. |
| C4-F4 | **uphold** | Full-file grep of factions_personal.md (120 lines): no "Clock Starting Values" table, no CI starting value. Census citation fabricated; retraction correct. |
| C4-F5 | **uphold** | Renown fully defined (derived_stats_v30.md:409-420 bridge); orphan_terms_registry.yaml:59-61 "confidence: DONE"; mechanical_terms_index.md:1618-1735 RESOLVED trail. Census "ORPHANED" flatly contradicted by grep-able closure markers. Residual cap ambiguity real (10-cap simulation_workplan_v1.md:387 vs uncapped derived_stats:565; distinct Shadow Renown 0-10 at faction_politics_v30.md:383-411). |
| C4-F6 | **uphold** | module_contracts.yaml:256 carries TC as a separate writable clock beside CI (:255); conviction_track_v30.md §3 (:167) fully retitled to CI Generation (TC dead, so striking is sync, not invention); infill (:7,23-26) never renamed; ED-782 (ledger:44) is a mass-battle PP-renumbering with an ID-CONFLICT flag — citation misattributed. |
| C4-F7 | **soften** (P1→P2; kind collision→crosswalk gap) | Facts right (registry:20,44 vs contracts:318,335-338 g_bond5), but knots_v30.md:17,28 explicitly cross-maps ("Bonds (attribute, 1-7)... Gates Knot eligibility (Bonds >= 5)", citing params/core.md) — "no cross-map anywhere in the corpus" is false. Same value, one definition, mismatched bucket-vs-KIND vocabulary: not a collision per the audit's own kind definitions; a machine-readability gap. |
| C4-F8 | **uphold** | IP name split confirmed at all cited lines; matches baseline FIX-03. |
| C4-F9 | **sharpen** (P2→P1) | Worse than filed: glossary.md:100,110 gives the BG faction Standing 0-10 ("no benefit above 7"), while clock_registry_v30.md:48-53 gives the SAME faction-scoped quantity 0-5 (bg_v05 P-15) — a direct range collision within one scope, on top of the cross-scale homonym with contest-kernel Standing (params/contest.md:144, 0-10 start 5). Also: name_collision_database.yaml:139 already partially acknowledges the overload ("Standing # faction attribute (also Key type - exempt)") — prior context U6 should have surfaced. Absorbs C4-M1. |
| C4-F10 | **uphold** | params/core.md:101: "TTRPG default = 60; Board Game default = 72"; campaign_modes.md:42-47's TTRPG table lists 72. All three cited filenames nonexistent. Session-zero seeding surface → P1 justified. |
| C4-F11 | **uphold** | WA (victory.md:14,53,89,130) vs WR (geography.md:408-431, "Replaces provisional conditions in victory_v30.md §3.4"); victory.md never updated. ED-311 verified as the corpus-wide citation for this redesign (victory_v30.md:761). KT stands. |
| C4-F12 | **uphold** | tracks.md:22,100-101 "VTM — STRUCK (PP-663)" vs victory.md:14,53,88-90,129-130 still gating numerically. Live contradiction. |
| C4-F13 | **uphold** | Consistent with armature §5.11 docket language; correctly KT/P3, not re-litigated. |
| C4-F14 | **uphold** | registry:109 (clock) and contracts:319 (bucket: clock) agree; only fieldwork_v30.md's informal prose label says "Track". Correctly scoped to P3. |
| C4-F15 | **uphold** | Consistent with cited surfaces and baseline; KT/P3. |
| C4-U1 | **uphold** | Index bookkeeping, no design call. |
| C4-U2 | **uphold** | Correctly DOCKETed; recommends the MS-precedented mode-split discipline. |
| C4-U3 | **uphold** | Pure propagation of params/core.md:101's stated TTRPG default. |
| C4-U4 | **uphold** (lane caveat) | Sync-to-decided-canon, but touches FA/provincial docs — FA co-sign per §4 lane convention, not pure IN. |
| C4-U5 | **soften** | Correct fix, wrong premise: say the prose cross-map exists (knots_v30.md:17,28) and the gap is registry/machine visibility. |
| C4-U6 | **soften** | Fork correctly docketed, but (a) understates: range collision within one scope, not just a homonym; (b) misses name_collision_database.yaml:139's exempt annotation; (c) feeds SC + FA, not just the collision DB. |
| C4-U7 | **uphold** | Reclassifies Renown; cap docketed to Jordan. |
| C4-U8 | **soften** (lane) | Sound fix; clock_registry's faction-track content is FA-lane material — route via FA (or IN citing an FA-owned correction), not default IN allocation. |

## Missed findings

**C4-M1 · P1 · collision · NEW** — Same-scope Standing range collision (glossary 0-10 vs
clock_registry 0-5 for the identical BG faction track). *Synthesis note: absorbed into the
sharpened C4-F9; counted once.*

**C4-M2 · P2 · stale · KNOWN-TRACKED (ED-781; censured_vocabulary.yaml)** — "Coup Counter"
(0-4, valoria_canonical_definitive_r2.md:129; retired for Löwenritter Graduated Autonomy, ED-781)
is tracked with residual_count 6 as of 2026-04-30, is squarely C4-scope, and the dossier never
names it despite quoting the very handoff line that lists it (HANDOFF_IN.md:177). Live grep
additionally surfaces it in arc_register_events.md:12,50, numeric_bounds_report.yaml:348,353,
throughlines_complete.md:46 — none in the censured file's residual list, so the tracked count
itself undercounts (2+ months stale).

## Conformance note

No hard violations. Kind slip: F7's "collision" label vs the audit's own definitions (crosswalk
gap; prose cross-map exists at knots_v30.md:17,28 — a surface the dossier never cited). No forks
ruled: CI provenance, Standing, Renown cap all DOCKETed with defaults. Build-state language
(placeholder/STRUCK) used as routing/context only, never sole verdict evidence (rule b clean).
Recurring soft spot on rule (f): U4/U8 route FA-owned file fixes through default ED-IN allocation
without flagging FA sign-off (and Standing spans SC+FA) — IN is legitimately cross-cutting here,
but the feeds should be explicit; corrected in the docket.
