---
atom_id: valoria_session_2026-04-25_master__05__section-5-cross-reference-audit
source_file: VALORIA_SESSION_2026-04-25_MASTER.md
source_section: "Section 5 — Cross-Reference Audit"
section_index: 5
total_sections: 11
line_count: 24
char_count: 1060
source_sha256: dedb9b7e51dc8e7b
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## Section 5 — Cross-Reference Audit

### Corpus

39 active spec files audited. 220+ unique sections indexed.

### Findings (initial scan)

7 broken cross-references:

1. `mass_battle L446 §5.2.2` → fixed to `threadwork_v30 §3.2` (Coherence Reduction).
2. `mass_battle L447 §5.2.3` → fixed to `threadwork_v30 §3.2` per-operation cap.
3. `mass_battle L575 §4.3.4 brittleness` → fixed to `threadwork_v30 §2.4` (MS ≤ 40 Shifting Object trigger).
4. `npc_behavior L561 §16.3 Foundations` → fixed to `canon/02_foundations_amendment_leap_mechanism Amendment 2 + threadwork_v30 §3.2 + §6`.
5. `peninsular_strain L231 §2.4.2` → fixed to `§2.4b` (Accord vs Order Scale Distinction).
6. `combat_v30 L363 §11.8` — deprecated-file reference, acceptable, not fixed.
7. `threadwork_v30 §5.10/§5.11` — historical preservation references, acceptable, not fixed.

Plus `social_contest L268` and `faction_politics L659`: `npc_behavior §3.2` → `§3.3` (Scar Accumulation, not Belief Revision). Fixed in ED-777.

All non-deprecated cross-references valid after these commits.

---
