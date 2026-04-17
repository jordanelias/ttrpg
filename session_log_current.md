session_id: faction_politics_throughline_resolutions_2026-04-17
session_close: 2026-04-17
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: await Jordan direction
blockers: []
resolutions_this_session:
  - ED-659: Faction politics throughline resolutions PP-661 — 10 findings addressed with 4 applied fixes. Committed dea7656a85be45138ccba0481d3c30c5d70c4582.
  - Character creation caste + Viability Matrix + advisory text (player_agency §7.1).
  - Standing 0 Petitioner carve-out (player_agency §3.2) + §3.4 range 0-7 with floor-protection above Std 1.
  - Institutional Facility Tiers (settlement_layer §1.4) — Wing/Suite/Chamber/Billet slots with capacity-pressure mechanics.
  - Named NPC Roster 3-tier capacity (npc_behavior §11) — ~35 Active + ~30 Passive + unlimited Background.
  - Generational × Coup × IP × Baralta three-clock interaction (baralta_crown_claim §7) with sequencing rules.
  - SIM-POL-R01 through R05 DEFERRED in tests/coverage_matrix.md for discoverability.
  - Warden × TC pressure scale + RM-when-active stub ladder (throughline_resolutions §3).
  - Register-split future marker (throughline_resolutions §8).
  - ED-629 Thread stress dependency flagged as cross-reference (not blocking).
  - Ledger split at session close: ED-659 archived; SIM-POL-R01/R02/R05 removed from ledger (duplicates — canonical locus is coverage_matrix).
  - editorial_ledger_summary.yaml rebuilt (was stale at next_id 629; now accurate at next_id 660).
files_modified_this_session:
  - designs/systems/throughline_resolutions_v1.md (new, 32,868 chars)
  - designs/systems/player_agency_v30.md (§3.2 carve-out, §3.4 0-7 range, §7.1 expanded)
  - designs/systems/settlement_layer_v30.md (§1.4 new)
  - designs/systems/npc_behavior_v30.md (§11 new)
  - designs/mechanics/baralta_crown_claim_v30.md (§7 new)
  - tests/coverage_matrix.md (SIM-POL-R01-R05 DEFERRED block)
  - canon/editorial_ledger.yaml (ED-659 added in PP-661 commit, then archived at close; SIM-POL dupes removed)
  - canon/editorial_ledger_archive.yaml (6 items archived in PP-661 commit, 1 more at close)
  - canon/editorial_ledger_summary.yaml (rebuilt)
  - canon/patch_register_active.yaml (PP-661)
  - references/canonical_sources.yaml (throughline_resolutions entry added)
  - references/propagation_map.md (PP-661 section)
  - references/file_index.md (throughline_resolutions row)
  - references/file_index_summary.md (canonical entry)
commits:
  - PP-661 commit: dea7656a85be45138ccba0481d3c30c5d70c4582
  - Ledger-split close commit: (this session_close commit)
open_items_carry_forward:
  - ED-542 (P2 battle consequences)
  - ED-586 (P2 arc behavioral state)
  - ED-587 (P2 Stability Crisis Zoom In)
  - ED-589 (P1 RM Presence marker mechanics)
  - ED-591-609 (P2 arc expansion items, various)
  - ED-611 (P2 Niflhel asset placement)
  - ED-615-627 (P1/P2 arc expansion batch)
  - ED-620 (P1 RM Founding mechanic)
  - ED-628 (P2 Vaynard Season 0 Jarl Assembly)
  - ED-629 (P0 Thread stress test — 28 blockers in separate register)
  - ED-630 (P2 Coup Counter moral ledger proposal)
  - ED-631 (P2 Heresy Proceedings resolution time)
  - ED-632 (P1 Shadow Renown full spec)
  - ED-633 (P1 Deniability Debt full spec)
  - ED-640 through ED-658 (P2/P3 faction politics sub-items from PP-660 register)
  - SIM-POL-R01 through R05 DEFERRED (tracked in coverage_matrix)
  - ED-647 rank dismissal mechanics — partially resolved by PP-661 §3.4 floor-protection; full spec pending
next_session_priorities:
  - Jordan direction. PP-660 + PP-661 together complete the faction politics expansion package.
  - ED-629 Thread stress test resolution remains highest-priority external (28 P0 blockers, separate session track).
