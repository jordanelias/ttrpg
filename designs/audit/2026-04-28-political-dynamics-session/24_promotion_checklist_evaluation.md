<!-- [PROVISIONAL: 2026-04-29 — §13 Promotion Checklist evaluation against doc 12 v1.2.1] -->
<!-- STATUS: PROVISIONAL — promotion-readiness assessment -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/24_promotion_checklist_evaluation.md -->

# §13 Promotion Checklist Evaluation — doc 12 v1.2.1

**Method:** Systematic evaluation of v1.2.1 (commit `52fb1292`) against §13 Promotion Checklist (7 items). Each item: status, evidence, verdict, blockers (if any).

**Companion:** `19_v1_1_validation_report.md`, `22_NERS_and_bloat_assessment.md`, `23_chain_audit.md`.

---

## §1 EXECUTIVE SUMMARY

**Verdict: 3 PASS, 2 BLOCKED ON JORDAN, 1 SUBSTANTIVE PASS WITH FORMAT GAP, 1 NOT DONE.**

| # | Item | Status |
|---|---|---|
| 1 | Re-vetting against current spec | ✓ PASS |
| 2 | Outstanding Design Decisions in §11 resolved | ⚠ BLOCKED ON JORDAN |
| 3 | Editorial ledger entries for each major component | ✓ PASS (with one gap noted) |
| 4 | Patch register entries (PP-XXX) with full vetting blocks | ⚠ FORMAT GAP |
| 5 | Integration patches against external designs | ✗ NOT DONE |
| 6 | Content authoring scope agreed | ⚠ BLOCKED ON JORDAN |
| 7 | Stage-1 simulation pass | ✓ PASS (far exceeds requirement) |

**Promotion to canonical is achievable but not immediate.** Three blockers require action:
- 2 require Jordan's design calls (#2 §11 decisions, #6 authoring scope).
- 1 requires external-integration work (#5).
- 1 (#4) is a format-style gap — substance is met but PP-XXX register format isn't used.

**Recommendation:** Complete the format and external-integration items; pause for Jordan on the design calls. Items 1, 3, 7 are unambiguous passes; items 2, 6 are organizational/decisional rather than spec-content blockers.

---

## §2 DETAILED EVALUATION

### 2.1 Item 1 — Re-vetting against current spec ✓ PASS

**§13 text:** *"Re-vetting against current spec (the Class A vetting in 07 was pre-streamlining)."*

**Status:** Complete; re-vetting is the largest body of evidence in the chain.

**Evidence:**
- `17_specification_revisions.md` (commit `6de72da1`): 26 patches addressing 68 stress-test issues from docs 13/14/15/16 (the post-streamlining vetting record).
- `19_v1_1_validation_report.md` (commit `b7f2235b`, AUDIT-corrected `dbc8d918`): 8-direction simulation chain validation across 51 scenarios.
- `21_v1_2_specification_revisions.md` (commit `b7f2235b`): 39 patches resolving simulation-surfaced gaps.
- `23_chain_audit.md` (commit `aed39f7a`): 5-phase audit confirming patch-fidelity (39/39), gap counts (39/39), and (after AUDIT-2 correction) invariant counts (25 unique).
- `22_NERS_and_bloat_assessment.md` (commit `09421b5d`): NERS criteria evaluation.
- v1.2.1 (commit `52fb1292`): NERS-cleaned promotion candidate.

**Verdict:** PASS. The chain provides comprehensive re-vetting evidence.

---

### 2.2 Item 2 — Outstanding Design Decisions in §11 resolved ⚠ BLOCKED ON JORDAN

**§13 text:** *"All Outstanding Design Decisions in §11 resolved."*

**Status:** §11 lists 3 items, none formally adopted.

**§11 item-by-item:**

1. **Wrong-Belief Investigation interaction (Option A vs B).** §11 has explicit recommendation: Option B (harsh — wrong Beliefs fire consequences at normal speed) per Ω-d ("every action pays what it buys"). **Recommendation made; formal adoption not recorded.**

2. **Authoring scope (~1,190 vs ~700-800 entries).** No recommendation; awaits Jordan's call. Tracks alongside §16.x and ED-755.

3. **Carryover decisions.** Three sub-items:
   - Restoring Intelligence as 6th faction stat (last touched ED-748 — marked struck per `canonical_definitive_r2`).
   - LICENSE / GOV-08 status carryover.
   These are also in §16.5 ED-755 Jordan-decision items.

**Verdict:** BLOCKED ON JORDAN.

**Recommended close-out path:** Either (a) Jordan reviews §11 and §16, makes calls, calls are recorded as `[RESOLVED-DATE-DECISION]` markers in spec; or (b) §11 is restructured: §11.1 "Recommended for adoption" (Option B), §11.2-3 "Pending Jordan calls" — making the distinction explicit.

---

### 2.3 Item 3 — Editorial ledger entries for each major component ✓ PASS

**§13 text:** *"Editorial ledger entries (ED-XXX) for each major component."*

**Status:** 129 total ED entries (13 active + 116 archived). Major-component coverage is broad.

**Component coverage audit:**

| Major component | Ledger coverage |
|---|---|
| Opinion architecture / single-writer | ✓ active (ED-757 simulation chain; PATCH 1.4-1.6 trail) |
| Domain Action / `select_proposal()` | ✓ active + archived (ED-756 v1.1 production; ED-760 stall-escalator) |
| Settlement Signal | ⚠ indirect — covered via SIM-C gaps (ED-761 archived) and PATCH 2.5/2.7 references in v1.1/v1.2 production entries; no dedicated ED entry |
| Faction Meta-Armature | ⚠ indirect — same as Settlement Signal |
| Standing recalc | ✓ active + archived (PATCH 3.11; AUDIT corrections) |
| Knot rupture | ✓ archived (ED-761 simulation-surfaced gap; SIM-H-G2 trail) |
| Procedure D single-writer | ✓ active |

**Verdict:** PASS substantively. Indirect coverage via simulation/patch trails for Settlement Signal and Faction Meta-Armature is acceptable for development-grade tracking; for canonical promotion, dedicated ED entries naming these mechanics directly would tighten the ledger.

**Recommended improvement (optional):** Add dedicated ED entries for "Settlement Signal flow" and "Faction Meta-Armature aggregation" to make the major-component coverage explicit.

---

### 2.4 Item 4 — Patch register entries (PP-XXX) with full vetting blocks ⚠ FORMAT GAP

**§13 text:** *"Patch register entries (PP-XXX) with full vetting blocks."*

**Status:** PP-XXX register format not used. No PP-XXX references in v1.2.1; no `canon/patch_register.yaml` file; doc 17 and doc 21 use `PATCH N.M` and `PATCH v1.2-N` formats respectively.

**Substance is met:**
- Doc 17 has 81 `PATCH ` references — full directives with LOCATE/REPLACE/RATIONALE for each.
- Doc 21 has 102 `PATCH ` references — same format with v1.2 numbering.
- Both docs serve the function of patch registers with vetting context.

**Format mismatch:** §13 expects `PP-XXX` ID convention with explicit "vetting blocks." Doc 17/21 use a different convention.

**Verdict:** SUBSTANTIVE PASS, FORMAT GAP.

**Recommended close-out paths (Jordan choice):**
- (a) Migrate doc 17/21 patches into a `canon/patch_register.yaml` with PP-XXX IDs, copying the LOCATE/REPLACE/RATIONALE content into structured "vetting blocks." ~2-3 hours of mechanical work.
- (b) Update §13 to accept the `PATCH N.M` and `PATCH v1.2-N` conventions used in doc 17/21 as equivalent to PP-XXX register format.
- (c) Defer this format conversion to post-canonical iteration.

---

### 2.5 Item 5 — Integration patches against external designs ✗ NOT DONE

**§13 text:** *"Integration patches drafted against: `designs/npcs/npc_behavior_v30.md`, `designs/architecture/player_agency_v30.md`, `designs/territory/settlement_layer_v30.md`."*

**Status:** All three external design docs exist in repo but no integration patches drafted.

**External design files:**
- `designs/npcs/npc_behavior_v30.md` — 107k chars, exists.
- `designs/architecture/player_agency_v30.md` — 50k chars, exists.
- `designs/territory/settlement_layer_v30.md` — 55k chars, exists.

**Reasoning for the §13 requirement:** The political dynamics system (doc 12) introduces NPC mechanics, player-agency surfaces (Outreach scenes, Read/Surveil/Witness), and settlement-level mechanics (Settlement Signals, population_disposition) that interact with the existing v3.0 architecture. Integration patches would document how doc 12's mechanics connect to the existing NPC/player/settlement layers — preventing implementation-time confusion.

**Verdict:** NOT DONE.

**Recommended close-out:** Single editorial session producing 3 integration-patch documents (one per external design), each documenting points of contact between doc 12 mechanics and the external design's existing structures. Estimated 3-5k chars per integration doc; total ~12k chars across 3 docs. ~1-2 hours of work. **This is the most concrete blocker.**

---

### 2.6 Item 6 — Content authoring scope agreed ⚠ BLOCKED ON JORDAN

**§13 text:** *"Content authoring scope agreed."*

**Status:** §11.2 explicitly lists authoring scope (~1,190 vs ~700-800 entries) as undecided. §10 documents authoring requirements but doesn't include an "agreed" marker.

**Cross-references:**
- §11.2 says authoring scope is outstanding.
- §16.5 (ED-755) lists overlapping carryover decisions.
- §10 documents content categories: alignment table (42 entries), goal templates (~30 entries), per-domain helpers, scene templates, signal_tag_to_domain mappings, EVENT_CATEGORIES (~50 entries), etc. — total maybe ~200-300 distinct authored entries needed for v1.2.1, plus the authored Beliefs/projects/events at content scale.

**Verdict:** BLOCKED ON JORDAN.

**Recommended close-out path:** Jordan reviews §10 + §11.2, decides on authoring scope (full ~1,190 vs reduced ~700-800), records as `[RESOLVED]` in §11 with rationale.

---

### 2.7 Item 7 — Stage-1 simulation pass ✓ PASS

**§13 text:** *"Stage-1 simulation pass demonstrating viable basic behavior."*

**Status:** Far exceeds requirement.

**Evidence:**
- SIM-A through SIM-D: single-mechanic correctness (Stage-1 equivalent — exactly what the requirement asks).
- SIM-E: composition validation (Stage-1+).
- SIM-F: engaged-player narrative validation (Stage-1++).
- SIM-G: long-horizon equilibrium (Stage-1+++).
- SIM-H: pathology / extreme stress (beyond Stage-1).
- 25 invariants verified (per AUDIT-2 corrected count).
- 39 specification gaps surfaced and resolved in v1.2.1 (architecture validated under load).

**Verdict:** PASS by a wide margin. The simulation chain provides ~5× more validation than §13 requires.

---

## §3 BLOCKERS SUMMARY

### 3.1 Blocker 1 — §11 Outstanding Design Decisions (Item 2)

Three items in §11; one has a recommendation (Option B for Wrong-Belief Investigation), two await Jordan calls (authoring scope, carryover decisions).

**Action required:** Jordan review + decisions.

### 3.2 Blocker 2 — Integration Patches (Item 5)

Three external design docs (npc_behavior_v30, player_agency_v30, settlement_layer_v30) require integration patches.

**Action required:** Editorial session drafting 3 integration patch docs (~1-2 hours).

### 3.3 Blocker 3 — Content Authoring Scope (Item 6)

§11.2 lists authoring scope as undecided. Decision required before canonical.

**Action required:** Jordan decision (full vs reduced authoring scope).

### 3.4 Format gap — Patch Register Format (Item 4)

Substantive content present in doc 17/21, but not in PP-XXX register format §13 expects.

**Action options:** (a) migrate to PP-XXX format, (b) update §13 to accept doc 17/21 conventions, (c) defer post-canonical.

---

## §4 RECOMMENDED PROMOTION SEQUENCE

To achieve canonical promotion, in order:

1. **Editorial session: Integration Patches (Item 5).** Draft 3 patch docs (~1-2 hours editorial work). This is the largest concrete blocker.

2. **Optional editorial session: dedicated ED entries for Settlement Signal flow and Faction Meta-Armature aggregation (Item 3 improvement).** ~15 minutes work; tightens major-component coverage.

3. **Jordan review: §11 + §16 decisions.** Adopt or modify recommendations; record as `[RESOLVED]` markers.

4. **Jordan decision: authoring scope (Item 6).** Records as §11.2 `[RESOLVED]` and §10 update.

5. **Resolve format gap (Item 4).** Jordan call: PP-XXX migration, §13 update, or deferral.

6. **Re-evaluation against §13 with all blockers addressed.**

7. **Promotion to canonical.** Move doc 12 v1.2.1 from `designs/audit/2026-04-28-political-dynamics-session/` to canonical location; update ledger; update file index.

---

## §5 CURRENT PROMOTION-READINESS ASSESSMENT

**doc 12 v1.2.1 is in good standing for canonical promotion, blocked primarily on organizational items (Jordan calls + integration-patch session) rather than spec-content gaps.**

The simulation-validation work, NERS cleanup, and audit corrections collectively demonstrate the spec is implementation-ready. The remaining items are coordination/decision work, not architecture or implementation work. Promotion within 1-2 sessions is achievable once Jordan engages the open decisions.

**Forward-looking design observations (19, tracked in doc 19 §5)** remain out-of-scope for v1.2.1 → canonical promotion. They're candidate features for v1.3+ post-canonical iteration.

---

**END OF §13 PROMOTION CHECKLIST EVALUATION.**
