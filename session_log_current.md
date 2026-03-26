# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-stages12-13
phase: 2
status: Phase 2 - Stages 12+13 complete (Campaign Modes, NPCs)
completed_stages:
  - Stage 4: Southernmost - 214 lines, 8 sections
  - Stage 5: Clocks (TT/TC/IP) - 237 lines, 6 sections
  - Stage 6: Factions - 419 lines, 12 sections (8.1-8.12)
  - Stage 9: Social Systems - Part Nine, 8 sections (9.1-9.8)
  - Stage 10: Advancement - Part Ten, 6 sections (10.1-10.6)
  - Stage 11: Scale Transitions - Part Eleven, 7 sections (11.1-11.7)
  - Stage 12: Campaign Modes - Part Twelve, 8 sections (12.1-12.8)
  - Stage 13: NPCs + Institutional Actors - Part Thirteen, 8 sections (13.1-13.8)
compilation_progress: 10/28 stages complete
notes:
  - Stages 7 (Territories) and 8 (Combat) still outstanding; jumped to 9-13 per user requests
  - Stage 12 sources: batch_f_designs.md (G-018 hybrid timing, G-021 endgame, G-023 branching), Patched ruleset §12, stage11
  - Stage 13 sources: Patched ruleset §8+§9, Design Doc revised (Church/Hafenmark), succession_mechanic.md (Torben/Elske), lowenritter_faction_card.md (Ehrenwall)
  - Stage 13 covers: Crown NPCs (Almud, Lenneth, Torben, Elske), Church NPCs (Himlensendt, Olafsson, Klapp, Jarnstal), Hafenmark (Baralta), Varfell (Vaynard, Maret), Löwenritter (Ehrenwall), Institutional Actors (Royal Investigators, Riskbreakers, Inquisitors, Templars)
  - Torben full Loyalty Clock mechanics in succession_mechanic.md on GitHub (designs/); Stage 13 references §7.x (Succession Mechanic) - needs cross-ref inserted at compile time
  - Niflhel, Revolution, Schoenland named NPCs not yet compiled - no detailed stat blocks exist in source; flagged below
patches_integrated:
  - Hybrid timing table (G-018) integrated into Stage 12
  - Endgame conditions (G-021) integrated into Stage 12
  - Mode branching catalogue (G-023) integrated into Stage 12
editorial_pending:
  - Renown permission table (Renown 1-10 tiers) - only Renown 6 data point exists
  - Varfell Private Collection transfer (PC takeover scenario)
  - Niflhel primus inter pares decision
  - Revolution named elder NPC contact (optional)
  - E-TAINT Taint track scale
  - Territory names
  - Varfell victory condition tuning
  - 10 seasonal event cards
  - Named Restoration NPCs
  - E-01 assassination perpetrator
  - E-03 AG calendar name
  - Niflhel named NPC stat blocks (Rolf Dunmark, Solvind Brak - referenced in source but not compiled)
  - Revolution named NPC stat blocks (Edith Varn referenced but not compiled)
next_action:
  stage: Stage 7
  task: Territories (zone-based for TTRPG, territory properties shared with board game)
  model: Sonnet 4.6
  source_files: batch_e_designs.md (territory table), Valoria_Design_Document_Revised__1_.md, compilation/stage6_factions.md
output_files:
  - compilation/stage12_campaign_modes.md committed (f9911e7f)
  - compilation/stage13_npcs.md committed (092450ef)

