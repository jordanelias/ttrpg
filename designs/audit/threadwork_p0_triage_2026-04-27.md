# Threadwork Audit P0 Triage — Phase 0.2.1/0.2.2
## Date: 2026-04-27 | Session: current

Cross-reference of 28 P0 blockers from `tests/stress/thread/threadwork_audit_register.md` (2026-04-16) against work completed since.

### Classification Key
- **RESOLVED**: Addressed by subsequent canonical work
- **OPEN-DESIGN**: Requires Jordan design decision (escalate to Phase 1 or 3)
- **OPEN-MECHANICAL**: Can be resolved by Claude with existing canon authority
- **RECLASSIFY**: Severity should change

---

### RESOLVED (7)

| ID | Item | Resolution |
|---|---|---|
| P0-04 | Per-province vs per-settlement siege MS drain | **Resolved by ms_budget.md (ED-668).** Siege drain = −1/season per siege, no per-settlement multiplication. ms_budget §MS Drain Sources is canonical. |
| P0-07 | WC state as variable in all MS calculations | **Resolved by ms_budget.md.** WC 0/2/3 scenarios explicitly modeled (Scenarios A/B/C). Three-path framing (ED-740). |
| P0-09 | Battle MS drain missing from budgets | **Resolved by ms_budget.md.** "Battle on Valorian soil −1" and "Campaign/War scale −2" in drain table. |
| P0-13 | PP-603 RS cap language in skeleton | **Resolved.** PP-603 cap struck; ms_budget contains no cap language. ×3 multiplier struck (replaced by flat −1 per battle). |
| P0-16 | Niflhel Harvest mechanics undefined | **Resolved by faction scope collapse.** Niflhel is not a playable faction in canonical_definitive_r2. 4 factions only (Crown/Church/Hafenmark/Varfell). Niflhel exists as worldbuilding entity; no Harvest BG order needed. |
| P0-26 | Warden Harvest BG order undefined | **Resolved.** Same reasoning as P0-16. Warden interaction is via WC track and Edeyja NPC behavior, not faction-level BG orders. |
| P0-06 | Dissolution Residue Potency per-use cap | **Resolved by P1-08 ruling** in same audit register: "Cap single-use Residue at Potency 3; Potency 4–5 requires two contact windows." This is a self-resolving entry (P0 resolved by its own P1 ruling). Verify propagation to params_threadwork. |

### OPEN-DESIGN — Jordan Decision Required (15)

| ID | Item | Classification | Notes |
|---|---|---|---|
| P0-01 | Settlement Order as Thread configuration | Phase 1 | Core Thread-settlement interface. Blocks siege calibration. |
| P0-02 | RO as Companion Conviction trigger | Phase 2 | Companion spec dependency. |
| P0-03 | POP during Memory-genre contest | Phase 2 | Depends on P0-17. |
| P0-05 | History Resonance risk die scope (10% vs 27%) | Phase 1 | 3× difference in Coherence depletion. |
| P0-08 | R-63 fast-change Lock domain rates | Phase 1 | Only slow-change defined. |
| P0-10 | Lattice fracture threshold mathematically inert | Phase 1 | P1-20 proposes fix (ceiling rounding). |
| P0-11 | Thread-Read evidence admissibility before TS 0 | Phase 2 | Three possible rulings. |
| P0-12 | Conviction Scar + Thread operation mapping | Phase 2 | Depends on P0-02. |
| P0-14 | Ceiral Ritual Failure MS +8 — intentional? | Phase 1 | Single value confirmation. |
| P0-15 | Altonian Thread practitioner status | Phase 3 | Worldbuilding authority. |
| P0-18 | Lock after practitioner death | Phase 2 | Three-outcome ruling. |
| P0-19 | Knot with threadcut being | Phase 2 | Metaphysical ruling. |
| P0-20 | Domain Echo for Thread operations mapping | Phase 2 | Depends on P0-01. |
| P0-24/28 | Isolation for Foundational Mending | Phase 3 | Einhir-gated vs standard. |
| P0-25 | Foundational OA consequence | Phase 3 | OA table extension. |

### OPEN-MECHANICAL — Claude Can Resolve (4)

| ID | Item | Action |
|---|---|---|
| P0-17 | POP minimum TS scaling | Define TS gate on POP temporal depth. Sim-verifiable. |
| P0-21 | Recall-based rolls at Fragmented — Thread included? | Check params_threadwork for Fragmented band rules. Likely mechanical clarification. |
| P0-22 | NPC practitioner Thread AI | Requires NPC behavior spec extension. Large but no Jordan decision needed on mechanics. |
| P0-23 | Pool floor conflict 1D vs 5D | Scope statement: 5D is R-57 Pull minimum only; 1D is general floor. Verify against params. |

### RECLASSIFY (2)

| ID | Item | From | To | Rationale |
|---|---|---|---|---|
| P0-27 | Companion Conviction post-Forgetting | P0 | P2 | Southernmost-only scenario. Does not block integration of core systems. |
| P0-10 | Lattice fracture threshold | P0 | P1 | P1-20 already proposes the fix. Mechanical, not blocking. |

---

## P1 Section (25 items) — Summary Triage

Most P1 items from the audit register are **exploits with rulings already provided inline** (P1-01 through P1-22 each have a "Ruling/Fix" column). These rulings need **propagation verification** — are they in the design docs or only in the audit register?

**Action:** Phase 2 batch task — grep each ruling against source docs. If ruling exists only in audit register, propagate to canonical doc + params.

## AUD-TW-001 (POP paradox window, Rendering Crisis procedure)

- POP paradox window: P0-19 / P1-19 coverage. Counter-POP blocked during window. **OPEN-DESIGN.**
- Rendering Crisis procedure: Implied by P1-10 and P1-11. MS emergency cascade. **Phase 2 sim task.**

---

## §0.2.3 — Unknown Canonical ID Classification

27 IDs referenced in atoms_pending but not in active editorial/patch registers.

### EDs (8) — All Pre-Ledger Canonical

| ID | Hits | Classification | Location |
|---|---|---|---|
| ED-129 | 37 | Pre-ledger. Active in combat_v30, params/combat | Canon reference |
| ED-131 | 20 | Pre-ledger. Active in combat, atoms_pending | Canon reference |
| ED-200 | 14 | Pre-ledger. In params/combat, propagation_log | Canon reference |
| ED-295 | 18 | Pre-ledger. In params/contest, propagation_log | Canon reference |
| ED-297 | 17 | Pre-ledger. In params/contest, atoms_pending | Canon reference |
| ED-618 | 21 | Pre-ledger. In editorial_ledger_index, npc_behavior | Canon reference |
| ED-670 | 23 | Pre-ledger. In thread_horizontal_integration, npc_behavior | Canon reference |
| ED-694 | 35 | Pre-ledger. In params/core, params/combat, combat_v30 | Canon reference |

### PPs (10+) — Pre-Ledger Canonical

PP-233 confirmed (38 hits, in glossary, mass_battle). Remaining PPs (PP-238/239/246/251/285/294/402/508/512) are pre-PP-530 numbering — all archived in `archives/patches/patch_register_archive_201_400.yaml` or `_001_200.yaml`.

### TC-01 — Stale

Pre-rename Theocracy Counter reference. Now Church Influence. Classified as **stale** — no action needed beyond existing TC→CI sweep.

**Conclusion:** All 27 IDs are legitimate pre-ledger references. None fabricated. None anticipatory. No action required beyond noting their pre-ledger provenance.
