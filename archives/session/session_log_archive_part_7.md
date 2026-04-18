
session_id: sim_alternate_branches2_2026-04-17
session_close: 2026-04-17
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []
resolutions_this_session:
  - Alternate branches batch 2: Branches K-T (10 new alternates)
  - K: Olafsson wins College vote — extra-territorial heresy designation as legal shadow on Hafenmark inner circle
  - L: Thale defects to Vaynard — trilateral intelligence arrangement; collapses cleanly at Coup
  - M: Himlensendt Arc C public during Grand Contest — Klapp framework saves him; TC-5; Vaynard-Himlensendt scholarly alliance
  - N: Baralta Arc B triggers — Niflhel arrangement creates permanent constitutional precedent; Feldhaus crisis
  - O: Stenskald endorses bloodline — Varfell succession locked to hereditary; Incapacity Assessment cascade at S28
  - P: Linder reports RS comment fully — Himlensendt sermon; offhand comment becomes public political theology
  - Q: Vaynard no practitioner at S3 Discovery Event — Arc C from absence of support, not excess of exposure
  - R: Feldhaus no addendum — forced Parliamentary motion creates broader precedent than addendum would have
  - S: Haelgrund refuses synthesis request — both parties build Thread-perception map independently; neutrality dataset more consequential
  - T: Almud enters Arc A at S14 — reform prevents Counter advance; Ehrenwall moral ledger shifts
  - Cross: neutrality always political; smallest actions most consequential; reform requires voluntary uncertainty
files_modified:
  - tests/sim_alternate_branches2_2026-04-17.md (new)
  - canon/editorial_ledger.yaml (ED-670/671/672/673; 15 P2 EDs archived; next_id: 674)
  - canon/editorial_ledger_archive.yaml (15 P2 EDs archived)
  - tests/coverage_matrix.md (batch 2 alt findings; Batches 1-2 findings trimmed to archive)
  - tests/coverage_matrix_archive.md (Batches 1-2 CM content archived)
open_items:
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
  - ED-670/672/673 (P2)
  - All prior open items carried forward

---

session_id: repo_restructure_cleanup_2026-04-18
session_close: 2026-04-18
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
  description: >
    Restructure cleanup complete. file_index regenerated, 36 skeleton headers
    fixed, editorial_gate bypass removed, canonical_sha__ keys updated,
    freshness gate re-synced, file_index trimmed below threshold.
    Remaining CI items: 11 missing_skeleton errors on gm_ref arc docs and
    3 audit docs (pre-existing, never had skeletons). These are auto-fixable
    but not critical.
blockers: []
commits:
  - 3069849: "file_index regen, 36 skeleton header fixes, editorial_gate bypass removed"
  - ea543dc: "canonical_sha__ key fixes pass 1"
  - 67672f7: "canonical_sha__ key fixes pass 2"
  - 38bad89: "canonical_sha__ key fixes pass 3"
  - freshness_gate: "SHA re-sync (49 fields)"
  - a76d5bd: "file_index trimmed below 8k threshold"
open_items:
  - "11 missing_skeleton errors (gm_ref arcs + audit docs) — generate in future session"
  - "arc_register.md freshness — pre-existing, needs params re-sync"
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
