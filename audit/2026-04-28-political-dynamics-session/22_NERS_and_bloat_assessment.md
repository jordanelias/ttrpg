<!-- [PROVISIONAL: 2026-04-29 — NERS + bloat assessment of v1.2 and chain artifacts] -->
<!-- STATUS: PROVISIONAL — critical assessment for cleanup/v1.3 planning -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/22_NERS_and_bloat_assessment.md -->

# NERS + Bloat Assessment — doc 12 v1.2 and Chain Artifacts

**Method:** Critical pass against project's four criteria — **N**ecessary, **E**legant, **R**obust, **S**mooth — plus explicit bloat audit. Honest assessment; no flattery. Findings actionable for v1.2.1 cleanup or v1.3 planning.

---

## §1 OVERALL VERDICT

**v1.2 spec passes R and S strongly. E is good with one structural blemish. N is the weakest dimension — the spec contains some completionist bloat that doesn't pass the "would the game break without this?" test.**

Specifically:
- **Robust:** ✓ — extensively simulation-validated; supports strategic depth, customization, emergence.
- **Smooth:** ✓ — integrations across directions verified; transitions clean.
- **Elegant:** ✓ with one structural blemish (§17 addendum pattern is inelegant).
- **Necessary:** ⚠️ — three sections are borderline-or-unnecessary for v1.2 timing.

**Recommended action:** v1.2.1 cleanup pass to address bloat findings without altering core mechanics.

---

## §2 NECESSARY — gaps in the "must have for game function" test

### 2.1 ✗ NOT NECESSARY for v1.2 — recommend deferring

**§5.4.2 Leader Challenge / Coup Mechanic (PATCH v1.2-20).**

The simulation surfaced this gap (SIM-H-G3), but it's spec-completion, not gameplay-critical. Faction succession on leader-death (§5.4.1) handles the dominant case. Coup-by-living-peer is a rare Renaissance phenomenon — many campaigns will never see one. The mechanic adds ~25 lines of spec surface area for an event that may never fire.

**Recommendation:** Cut from v1.2.1. Defer to v1.3 if Jordan wants it. The pre-existing emergent-Memory-drift dynamics (per SIM-H Sc 2 trace) handle coup-precursor pressures without an explicit mechanic.

---

**§8.2 War State + §8.2.1 Peace Treaty (PATCH v1.2-22, v1.2-23).**

Adds an aggregation layer over individual military Domain Actions. The spec without these still handles inter-faction conflict — Crown and Hafenmark trade military DAs each Accounting; Settlement Signals carry war-context organically; Concerns generate. War-state is an *abstraction*, not a *new mechanic*. Same for peace treaty (which is just a diplomatic Domain Action with binding terms — already supported by general DA framework).

**Recommendation:** Cut from v1.2.1 spec body. Defer to v1.3 (or content-authoring stage where war-themed campaigns might benefit). The 50+ lines added by these two sections are aggregation/bookkeeping that existing mechanics already support implicitly.

---

### 2.2 ✓ NECESSARY (despite size)

**§2.5.2 Knot Rupture.** P1-critical gap; spec referenced state without defining process. 67 lines justified by being the engine's strongest intimate-political dramatic mechanic. Keep.

**§5.4.1 Faction Succession.** Without it, leader-death has no resolution path. Keep.

**§5.2 routing logic + cross-border + salience + repeated-Signal handling.** Each addresses an implementation-determinism gap. Keep all.

**§8.1 strict counter definition + counter state + rounding.** Resolves SIM-B-G8 (P1-critical). Keep.

---

### 2.3 Borderline P3 entries that could compress

Several P3 patches in §17 are 1-line notes wearing patch ceremony:

- PATCH v1.2-26 (confidence boundary `< 3`): a sed-and-replace operation across §6.2 — should have been applied directly, not added as an addendum entry.
- ~~PATCH v1.2-29 (banker's rounding): already applied surgically in §8.1; the §17 entry is duplicative.~~ **Retracted per AUDIT-4 (`23_chain_audit.md`):** the line-1946 reference is a tracking entry in §17.3 Application Audit, not content duplication. Ignore this finding.
- PATCH v1.2-30 (mood-suppressed accounting): spec already says this in §8.1 strict counter scope clause; §17 entry is redundant.
- PATCH v1.2-31 (salience-0 lifecycle): one-line note that belongs inline in §2.6.

**Recommendation:** v1.2.1 cleanup should apply these surgically and remove from §17 addendum.

---

## §3 ELEGANT — one structural blemish

### 3.1 ✗ §17 v1.2 PATCH ADDENDUM is INELEGANT

Twenty-one P2/P3 patches consolidated as prose summary. This was a pragmatic shortcut to land all 39 patches in one v1.2 commit, but it produces a spec where:
- Some clarifications live in their target sections (surgical patches).
- Other clarifications live in §17 (addendum entries).
- A reader implementing the spec must check both locations to find authoritative behavior for any single feature.

**Per project's E definition:** *"logically simple; clear approach; no unnecessary overhead; easy to understand."*

The addendum pattern fails this. A reader looking up `select_proposal()` should find all relevant clarifications in §6.2, not bounce between §6.2 and §17.4.

**Recommendation:** v1.2.1 cleanup pass should:
1. Apply each §17 patch surgically in its target section.
2. Delete §17 entirely.
3. Reduce spec to ~1850-1900 lines (small reduction; structural improvement is the point).

This is mechanical work, ~30 minutes. Strongly recommended for promotion-candidate spec.

---

### 3.2 ✓ Other elegance dimensions hold

- Patch numbering convention (v1.2-N with cross-references) is clean.
- Pseudocode is generally readable.
- New mechanics (Knot rupture, succession) follow the doc's existing style.
- Featured-behavior commentary pattern is consistent with v1.1 conventions.

---

## §4 ROBUST — strongly satisfied

The simulation chain (51 scenarios across 8 directions) systematically tested:
- Strategic-thinking support: ✓ (SIM-F engaged playthrough demonstrates multi-Act narrative production)
- Customization: ✓ (NPCs/factions/settlements with distinct armatures produce distinct dynamics)
- Creativity/variety in approach: ✓ (Knot rupture, coalition negotiation, deadlock-via-stall, etc., all support divergent player approaches)
- Player feels important to game world: ✓ (PATCH 3.12 player-amplification scope reliably indexes player actions to faction attention)
- Player feels impact: ✓ (engaged player can shift faction Conviction-share by ~10% over 4 Years)
- Emergent narrative without player involvement: ✓ (chronicle-level texture confirmed at 3-faction scale)
- Mechanics fully formed and complete: mostly — see N findings; coup/war/peace are *spec-completionist* additions that may not be needed.

**Robustness is the spec's strongest dimension.**

---

## §5 SMOOTH — strongly satisfied

Integration verified across all six pairwise direction pairs (A↔B, A↔C, A↔D, B↔C, B↔D, C↔D). Scale transitions traced (single-mechanic → multi-faction → engaged-player → long-horizon → pathology) without breakdowns. Mechanic transitions (e.g., Settlement Signal → Concern → DA Proposal → Standing recalc → Meta-Armature recomputation) flow without friction. Pause-and-sequence behaviors (Faction Crisis state, Mood-suppressed proposals) handled cleanly.

**Two minor friction points:**
- The §17 addendum pattern violates "integrates cleanly into game" because implementors must consult two places. (See §3.1 above.)
- Knot rupture cascades through Memory generation, Concern propagation, Mood shifts, Faction Meta-Armature impacts, and Belief revision potential — five mechanic systems touched simultaneously. Spec'd well in §2.5.2 but a reader has to mentally aggregate the cross-reference web. Could benefit from a "cascade diagram" in v1.2.1.

Otherwise smooth.

---

## §6 BLOAT AUDIT

### 6.1 doc 12 v1.2 — line accounting

| Region | Lines | Bloat verdict |
|---|---|---|
| Header + change logs | ~85 | OK |
| §1.1 Featured Behaviors | ~30 | OK (Knot Rupture entry justified) |
| §2 NPC data structures | ~250 | OK; §2.5.2 long but necessary |
| §3 Armature | ~220 | OK |
| §4 Event Impact Matrix | ~120 | OK |
| §5 Meta-Armatures | ~310 | **§5.4.2 Coup (~25 lines) cuttable**; rest OK |
| §6 Procedures | ~435 | OK; pseudocode-heavy by necessity |
| §7 Player-Facing Surfaces | ~65 | OK |
| §8 Integration | ~150 | **§8.2 War + §8.2.1 Peace (69 lines) cuttable** [AUDIT-5 correction] |
| §9-§13 Computational/Authoring/Testing/Promotion | ~130 | OK |
| §14-§16 References + stubs + Jordan-decisions | ~75 | OK |
| **§17 v1.2 Patch Addendum** | **~85** | **CUTTABLE — apply surgically, delete §17** |

**Total cuttable:** ~178 lines (24 + 69 + 85 = 178; AUDIT-5 corrected from initial ~160). Cleaned v1.2.1 → ~1780 lines.

### 6.2 Simulation chain artifacts

| Doc | Lines | Bloat verdict |
|---|---|---|
| SIM_A | 850 | Some redundant verification subsections |
| SIM_B | 850 | Some redundant verification subsections |
| SIM_C | 734 | Some redundant verification subsections |
| SIM_D | 379 | Tight |
| SIM_E | 360 | Tight |
| SIM_narrative_arc_pass | ~120 | Tight, valuable |
| SIM_F | 397 | Tight |
| SIM_G | 366 | Tight |
| SIM_H | 469 | Tight |

**Verdict: simulation docs are within reason for audit/development artifacts.** They're history, not active spec. SIM-A/B/C have some scenario-end "Verification" boilerplate that could compress, but they're already-committed audit history; not worth re-touching. **Not bloat in the operational sense.**

### 6.3 doc 19 (synthesis) and doc 21 (patches)

- doc 19: 359 lines. Synthesis report. Some overlap with doc 21 in gap descriptions. Acceptable — different audiences (validator-readers vs implementers).
- doc 21: 893 lines. Long because it contains exact patch directives. Some patches are 30+ lines of pseudocode; appropriate for the format.

**Verdict: not bloat.** Both serve distinct purposes; minor overlap is acceptable for cross-reference convenience.

---

## §7 RECOMMENDED v1.2.1 CLEANUP PASS

Single editorial session addressing structural and necessity findings:

1. **Cut §5.4.2 Coup Mechanic** — defer to v1.3.
2. **Cut §8.2 War State + §8.2.1 Peace Treaty** — defer to v1.3.
3. **Apply §17 addendum patches surgically** in their target sections.
4. **Delete §17** entirely.
5. **Update §0.1 v1.2 change log** to note the v1.2.1 cleanup.

**Estimated impact:** -178 lines (per AUDIT-5 corrections). v1.2.1 → ~1780 lines. Same semantic content (minus the deferred mechanics) in cleaner structure.

**Estimated effort:** ~30-45 minutes editorial session.

**Justification:** v1.2 is the canonical-promotion candidate. Promotion-grade spec should pass NERS rigorously. Current v1.2 fails N (necessary) on three sections and E (elegant) on one structural pattern. v1.2.1 fixes both with no semantic loss.

---

## §8 FORWARD-LOOKING — what to defer vs cut entirely

### 8.1 Defer to v1.3 (post-canonical)

- Coup mechanic (§5.4.2 in current v1.2).
- War-state + peace-treaty (§8.2 + §8.2.1 in current v1.2).
- The 18 forward-looking design observations from SIM-E/F/G/H + narrative pass (already tracked in doc 19 §5; not in spec).

### 8.2 Cut entirely

Nothing recommended for permanent removal — all current mechanics are at minimum *useful* even if not *necessary* for v1.2 timing.

### 8.3 v1.3 candidate features (from forward-looking observations)

- **Player Move mechanic** (SIM-E-O2): explicit Memory-seeding action for proactive player agency. Largest narrative-strength gain.
- **Aging/mortality mechanic** (SIM-G-O1): would justify the coup mechanic by making leader-vacancy events more frequent.
- **Conviction-diversity bonus in institutional_stability** (SIM-G-O3): would address the homogeneous-faction ossification trajectory observed in SIM-G Sc 4.
- **Faction Watershed event class** (narrative-N4): discrete dramatic beat at cumulative-drift threshold.

---

## §9 CONCLUSION

**v1.2 is a strong spec but not maximally rigorous against NERS.** Three sections are completionist-bloat (coup, war, peace); one structural pattern is inelegant (§17 addendum). v1.2.1 cleanup pass would address all findings in ~30-45 minutes editorial work.

**For canonical promotion: recommend v1.2.1 first.** The cleanup is mechanical; the gain is meaningful — promotion-grade spec should be tighter than promotion-candidate spec.

If Jordan wants v1.2 promoted as-is, that's defensible (the bloat is not fatal), but v1.2.1 would be a stronger artifact and is cheap.

---

**END OF NERS + BLOAT ASSESSMENT.**
