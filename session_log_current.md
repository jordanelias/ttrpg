session_id: faction_politics_rank_expansion_2026-04-17
session_close: 2026-04-17
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []
resolutions_this_session:
  - ED-635: Cardinal Prudence naming sync — worldbuilding_v30 §3.1 updated to Aldric Tormann (npc_roster_v30 §13 canonical). ED-NEW-06 closed.
  - ED-636: Solmund naming correction applied — conviction_track_v30 line 16 "Galbadian Orthodoxy" → "Solmund Orthodoxy".
  - Faction politics rank-ladder expansion PP-660 committed (13 files, single atomic commit).
  - Standing ladder expanded 0-5 → 0-7 with Skyrim-guild progression patterns.
  - 8-rank ladders specified for Crown/Hafenmark/Varfell/Church with named inner circles.
  - 7 sub-office rank ladders (Löwenritter, Riskbreakers, Inquisitors, Templars, Guilds, Niflhel, Wardens).
  - Caste integration layer (Northern/Central/Southern Einhir modifiers).
  - TC × rank interaction integrated into tc_political_redesign_v30 §3.5.
  - Baralta Crown Claim × rank interaction + new Hafenmark-to-Crown Recognition Ceremony mechanic.
  - Ministry system expanded to Hafenmark Committees, Church Dicasteries, Varfell Councils.
  - Generational Shift Torben maturation fix (4-trigger replacement for unreachable 10-year spec).
  - Cross-faction parity table.
  - player_agency §5.1 rewritten for 0-7 ladder; §6.2 scene action modifier extended.
  - scale_transitions §4.3.2 Rank Advancement Recognition Event added to Mandatory Zoom In triggers.
files_modified:
  - designs/systems/faction_politics_expanded_v1.md (new — 944 lines, 139,940 chars)
  - canon/editorial_ledger.yaml (ED-634, ED-635, ED-636 added; next_id → 637)
  - canon/patch_register_active.yaml (PP-660 appended)
  - references/canonical_sources.yaml (faction_politics_expanded entry added)
  - references/propagation_map.md (PP-660 section appended)
  - references/file_index.md (DESIGNS — SYSTEMS row added)
  - references/file_index_summary.md (canonical list entry added)
  - designs/conviction_track/conviction_track_v30.md (Solmund fix line 16 + CV≡PT equivalence note §1)
  - designs/worldbuilding/worldbuilding_v30.md (§3.1 Cardinal Prudence = Aldric Tormann)
  - designs/mechanics/baralta_crown_claim_v30.md (§5 Recognition Ceremony cross-reference)
  - designs/hybrid/scale_transitions_v30.md (§4.3.2 Rank Recognition Event row)
  - designs/board_game/tc_political_redesign_v30.md (§3.5 TC × Rank Ladder Interaction)
  - designs/systems/player_agency_v30.md (§5.1 Stature Levels rewrite, §6.2 modifier extension)
open_items:
  - ED-634 (batch): 23 sub-items from faction politics register tracked in designs/systems/faction_politics_expanded_v1.md §10.2
  - 5 SIM-DEBT items (SIM-POL-R01 through R05) — per Jordan instruction, simulation deferred
  - Solmund propagation: grep for any remaining "Galbadian"/"Galbados" occurrences across designs/, references/, canon/ (conviction_track line 16 done; other files unchecked)
  - CV ≡ PT full rename deferred (ED-644) — file rename conviction_track_v30.md → piety_track_v30.md pending future cleanup pass
  - All prior open items carry forward (ED-542, ED-586, ED-587, ED-589, ED-591-609, ED-611, ED-615-627, ED-631-633, ED-629 Thread stress)
commit: 04c4c6e23b3232874fb6f8213fc5598c0b288d5a
