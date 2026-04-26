---
atom_id: master_document_2026-04-25__29__6-1-three-mode-architecture-gaps
source_file: master_document_2026-04-25.md
source_section: "§6.1 Three-mode architecture gaps"
section_index: 29
total_sections: 50
line_count: 14
char_count: 1449
source_sha256: 312f97236be6f341
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## §6.1 Three-mode architecture gaps

`[GAP-1: Goal-parsing system for Trajectory mode is technically nontrivial. Player writes a sentence; engine must extract target NPCs, target territories, target Conviction-types, target factions, completion criteria. This is the largest engineering question in the proposal. Recommend: start with template-only Trajectory (P0); authored Trajectory deferred to P1.]`

`[GAP-2: Mode-shift recognition scenes need authored content per shift type. Six shift directions × variant scenes per direction = ~18 scene templates needed. Could be reduced via parameterized templates.]`

`[GAP-3: Wanderer "ambient inflation" is underspecified. How much more frequent should Priority 5 entries be? What kinds of ambient texture? Settlement seasonal festivals? Local NPC family dramas? Travel rumors? Needs content design, not just mechanical specification.]`

`[GAP-4: Strategy failure rituals are described but not specified. Faction Funeral, Rupture Scene, Altonian Surrender each need scene templates with named NPC parts.]`

`[GAP-5: Cross-character continuity (Wanderer grandfather → Wanderer grandson playing same world) requires data persistence design. Hall of Lineage data structure not yet specified.]`

`[GAP-6: Multiplayer/shared-world design entirely absent. If two human players are in the same Valoria world, can one be Wanderer and the other Strategist? Probably yes, but the implications are unexplored.]`
