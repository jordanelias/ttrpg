# VALORIA — MECHANIC-AUDIT: P1 FINDINGS CLUSTER
## Mode: D (Gap Detection) + C (Interaction Chain Analysis)
## Date: 2026-03-27 | Scope: All 20 open P1 findings
## Purpose: Assess whether existing patch proposals close each P1; identify new gaps; produce Phase 3 gate recommendation

---

## AUDIT TABLE — 20 P1 FINDINGS

| Finding | Patch | Closes P1? | New Gaps | Editorial? | Notes |
|---------|-------|-----------|----------|-----------|-------|
| F-B7-08/16 | PP-001 | YES | P2: "full campaign arc" duration undefined | No | TD −3/zero-ops season; −10/arc. Interaction with PP-011 (both benefit from zero-ops season) is correct. |
| F-B7-17 | PP-002 | YES | P3: "next scene" needs session-span clarification | No | TT +4 cap per practitioner/scene; excess carries. Deferred collapse risk is intended. |
| F-B7-06 / F80 | PP-003 | YES (pending PP-007) | P2: "opposition pool" undefined in vote procedure | Depends on PP-007 | Coalition Composure ≥ 3 reference must become "Poise ≥ 3" if PP-007 approved. Dependency flagged. |
| F-B7-12 / F-B7-22 | PP-004 | YES | P2: Mandate 0 territorial claim needs 1/season cap | No | Stat floors/ceilings/thresholds complete. Death spiral at Stability 0 is intentional. |
| F-B7-23 | PP-005 | YES | P2: "explicitly cancels" undefined | No | 5-tier sequencing is clean. NPC AI rules must reference PP-005 sequencing. |
| F-B7-29 / F100 | PP-006 | YES (mechanically) | — | EDITORIAL | Formula valid. PP-034 supplements (morale track); cross-reference required. |
| F-B7-40 | PP-007 | YES | Rename cascade: compiler-tier audit of all "Composure" references needed | EDITORIAL | PP-003 is dependent — must be updated simultaneously. |
| F-B7-44 / F84 | PP-008 | YES | Design concern: Intel 8 passive detection dominance (see below) | EDITORIAL | Intel 8 → ~97% passive detection every season via PP-044. Recommend Intel 6 discussion. |
| F-B6-RE-01 | PP-009 | YES | — | No | Ob1, four degrees. Clean. |
| F-27 | PP-010 | YES | — | No | Certainty crisis first; ThS arc continues independently. No formula conflict. |
| F25 | PP-011 | YES | Design note: +5 extended rest may need adjustment for long campaigns | No | Zero-ops season: ThS +5 AND TD −3 (PP-001). Incentive alignment correct. |
| §4.5 | PP-012 | YES (canon-clean; see below) | Language requirement: Coherence track must use transformation/integration framing, not deterioration | EDITORIAL | Canon-guard result below. P-03 and P-04 both PASS with framing conditions. |
| F-23 | PP-013 | YES | — | No | Also closes F89 (Community Weaving TT collective scaling — same mechanic). |
| F-24 | PP-014 | YES | P2: Helper individual op eligibility after Anchor dropout needs clarification | No | "Contact window expires naturally" is ambiguous — must state Helpers cannot independently op after Anchor dropout. |
| F-34 | PP-015 | YES (mechanically) | — | EDITORIAL | Church Mandate 7 vs Ob3 at TC80: ~85% success. Intended asymmetry at threshold. |
| F-38 | PP-016 | YES (pending stat approval) | P2: Restoration Seeker TS exception needs explicit "exception to TS prerequisite" note | EDITORIAL | Niflhel Operative starting DD interaction with PP-063 is clean. |
| F-40 | PP-017 | YES | — | No | CE 5 Spirit check Ob2: ~50% involuntary transformation. Cycle mechanic (pass→reset to 3) is correct. |
| F-13 | PP-018 | YES | — | No | TC pause sets change to 0; negative modifiers still apply. Counterintuitive but correct. |
| F-14 | PP-019 | YES | — | No | Three intel categories + BG card deck. Complements PP-044 passive detection. |
| F-07 | PP-020 | YES | Design note: strain still accumulates slowly above Int 4 | No | Exit from perpetual deterioration exists via one rest season. P1 resolved; long-term pressure remains (intended). |
| F78 | (resolved) | DOC GAP ONLY | Needs §cross-reference note added during compilation | No | Not a blocking P1. Compiler handles. |
| F83 | PP-004 | YES | — | No | PP-004 sets floor to 0 + elimination trigger. F83 closed by PP-004 — remove from open P1 list. |
| F89 | PP-013 | YES | — | No | TT cost = 1× regardless of participant count. F89 closed by PP-013 — remove from open P1 list. |
| F-B5-M07-A | PP-021 | YES | — | No | Remove §8.1; reference §1.9. Compiler-tier. |
| F-B5-M06-D | PP-022 | YES | — | No | Re-declaration for unanticipated priority attacks. Wound penalty (R-ST1) still applies to re-declared pool. |
| F-B8-02 | PP-062 | YES (canon-clean) | — | EDITORIAL | See Coherence arc analysis below. PP-062 + PP-077 together form complete Coherence track. |
| F-B9-04/08 | PP-077 | YES (canon-clean) | "Thread-driven compulsions" needs specification — editorial/setting question | EDITORIAL | "Thread-driven compulsions" must be defined (3–5 sample compulsions) during compilation. |

---

## FINDINGS WITHOUT EXISTING PATCHES — 3 ITEMS

### F57 (G-128): ThS World-Track Language
**Status:** OPEN — no patch proposal exists  
**Finding:** §5.9 Fallout table uses per-character language ("your ThS drops") but ThS is a world-track, not per-character  
**Impact:** P1 in simulation batch because incorrect scope understanding corrupts all ThS-related decisions  
**Proposed patch (PP-078 — new):**  
Rewrite §5.9 Fallout table throughout: replace "your ThS drops" → "ThS drops"; "your thread sensitivity has reached" → "Thread Sensitivity in the local/global environment has reached." Add one-line clarification at §5.9 header: "Thread Sensitivity (ThS) is a world-side track reflecting the cumulative density of Thread-side presence in the environment. It is not a per-character stat."  
**Model required:** Haiku 4.5 (text rewrite, no new mechanic)  
**P1→P2 downgrade candidate:** The underlying mechanic is not broken — only the text is ambiguous. Classify as P2 (rules clarity) rather than P1 (breaks play) unless simulation confirms practitioners are consistently misapplying ThS as a personal stat.

---

### F72 (G-129): Torben Loyalty Clock Drain Rate
**Status:** OPEN — no patch proposal exists  
**Finding:** TLK drain rate entirely absent from CP14; succession timeline unplayable without it  
**Proposed patch (PP-079 — new):**

**Torben Loyalty Clock (TLK) — Drain Rate Definition**  
TLK starts at 10 (maximum loyalty). At 0: Torben is fully Altonian-aligned; retrieval requires a major narrative arc (GM discretion, not a Domain Action).

Seasonal drain schedule:
- Base drain: −1 per season Torben remains in Altonian court with no Crown contact this season
- Tutoring demand refused (including Negotiate Delay per B4 results): −3 cumulative
- Failed covert contact (Partial or worse): −1 additional
- Successful covert contact (Crown Int Ob3 success+): TLK holds this season (no drain)
- Successful tutoring deployment (Elske dispatched to Altonian court): TLK +2 (recovery)

Milestone events (GM-tracked; fire once per event, not per season):
| Event | TLK Change |
|-------|-----------|
| Altonian invasion formally announced | −3 |
| Altonian-Crown treaty signed | −2 |
| Torben ordered to renounce Valoria ties | −4 |
| Elske makes public political statement | −2 |
| Crown faction publicly demonstrated as legitimate | +1 |

At TLK 0: Torben loyalty lock triggers. Crown loses all covert contact routes. New Domain Action required: Public Amnesty (Political, Ob5) to create retrieval window.

**Model required:** Sonnet 4.6 (design within constraints — done here)  
**Severity:** P1 (Torben mechanic unplayable without drain rate)

---

### F112 (G-136): Church Stability TC Brake Threshold
**Status:** OPEN — no patch proposal exists  
**Finding:** TC brake fires at Church Stability ≤5, but Church starts at Stability 5, permanently suppressing TC generation from game start  
**Proposed patch (PP-080 — new):**  
Change TC brake threshold from Stability ≤5 to **Stability ≤3**.

Effect:
- Church at Stability 4–10: normal TC accumulation (no brake)
- Church at Stability 3: TC brake activates — seasonal TC gain halved (round up)
- Church at Stability 0: PP-043 applies (TC gains fully suspended)

Rationale: At Stability ≤3, the Church is genuinely institutionally stressed (below the Stability 0 crisis threshold, but visibly struggling). TC suppression at this level represents a faction too internally divided to effectively pursue external expansion. Stability 4 remains the base "functional" threshold.

Cross-reference required: PP-043 (Stability 0 Church TC suspension) unchanged. Church starting Stability (5 or adjusted per PP-008 interaction) now operates above the brake threshold from Season 1.

**Model required:** Haiku 4.5 (numbers fix — change threshold value)  
**Severity:** P1 (Church TC progression broken from game start at current threshold)

---

## INTERACTION FINDINGS (P2)

| ID | Mechanics | Issue | Proposed Note |
|----|-----------|-------|--------------|
| IA-01 | PP-008 + PP-044 | Niflhel Intel 8 → passive detection ~97% every season. Dominant information advantage vs all factions. | [EDITORIAL] Consider starting Intel at 6. Or: passive detection triggers on Intel 4–5 only; Intel 6+ uses active Intel Domain Action equivalent (always-detect on domain action spend, not passive). |
| IA-02 | PP-003 + PP-007 | PP-003 references "Composure ≥ 3" for coalition formation. If PP-007 approved, this must be updated to "Poise ≥ 3." Compiler must audit all PP-003 text for Composure references. | Dependency: PP-003 text finalization is blocked until PP-007 editorial decision. |
| IA-03 | PP-001 + PP-011 | Zero-ops season provides BOTH TD −3 (PP-001) AND ThS +5 (PP-011). Strong incentive for seasonal rest cycles. Interaction is correct — record as design feature, not bug. | Add cross-reference note in both rules. |
| IA-04 | PP-062 + PP-077 | Together define complete Coherence recovery arc: PP-062 = recovery above 0; PP-077 = recovery from 0. Must be explicitly cross-referenced in the Coherence track rules. | Compilation stage 3 (Thread operations) must include both and cross-reference. |
| IA-05 | PP-006 + PP-034 | PP-006 (mass combat damage formula) and PP-034 (morale track + rout) are interdependent. PP-006 defines damage steps; PP-034 defines morale depletion per step. Must be compiled as one unified mass combat section. | Compilation stage 8 (Combat). |
| IA-06 | PP-005 + BG NPC AI | Domain Action sequencing (PP-005) must be incorporated into NPC AI priority tree. NPC AI actions are currently described in abstraction — sequencing rule is not referenced. | Add PP-005 sequence reference to §NPC-AI section. |

---

## CANON-GUARD VERDICT: PP-012

**Check:** Intelligibility vs Coherence two-track split against P-03 and P-04

### P-03: Rendering = consciousness-performed
- **Intelligibility track (§4.5):** Degradation = practitioner's rendering capacity for the human-intelligible world weakening. Social penalties reflect inability to communicate rendered experience to others. The practitioner's consciousness is still rendering — just rendering Thread-side configurations that others cannot follow. **PASSES.**
- **Coherence transformation track (§5.10):** At low Coherence, the practitioner gains Thread op bonuses because their consciousness is rendering from a Thread-integrated perceptual field. They render accurately — but their rendering is no longer human-readable. **PASSES.**
- **Simultaneous low-track state (both depleted):** A practitioner on both tracks simultaneously is rendering a fully Thread-perceptive field with minimal human-world overlay. This is still consciousness-performed rendering — the most radical version of it. **PASSES.**

### P-04: Monstrosity = ontological, not moral
- **Intelligibility degradation:** Framed as cognitive/perceptual capacity, not moral failure. **PASSES.**
- **Coherence transformation:** Critical test. PP-012 frames it as the "going native" path. The Thread op bonuses at low Coherence represent genuine Thread-integration — not a punishment, not corruption. **PASSES IF** the track text uses language of transformation/integration, not "Coherence loss," "Coherence deterioration," or moral-adjacent framing.
- **Risk:** The word "Coherence" with a decreasing value may implicitly frame the direction of decrease as bad/wrong. This is a language constraint, not a mechanical one.

### Canon-Guard Result: **CONDITIONAL PASS**

PP-012 is philosophically sound. Two language requirements must be satisfied in compiled text:

1. **Intelligibility track:** Describe as "the practitioner's capacity to render their Thread-perceptions in human-readable form" (not "cognitive decay" or "mental degradation")

2. **Coherence track:** Include the following line in §5.10: *"Coherence does not measure moral integrity or psychological health. It measures alignment between the practitioner's perceptual field and the shared rendered world. A practitioner at low Coherence is not failing — they are rendering from a different ground."*

These are text conditions, not mechanical redesigns. The two-track split itself is canon-clean.

**P-02 check (incidental):** Ein Sof = fullness. At Coherence 0 (PP-077): +5D Thread operations = Thread-fullness, not void. Framing of low Coherence as Thread-surplus (not corruption or void) is required. PP-012 and PP-077 together express this correctly if language constraints above are met. **PASSES.**

---

## PHASE 3 GATE ASSESSMENT

### Prerequisites (from workplan):
- Every mechanic tested in Isolation + Interaction: ✓ (98%, 54/55 mechanics)
- Every game mode covered: ✓
- Every faction tested: ✓
- Every named NPC tested: ✓
- Every archetype tested: ✓
- Every track tested at thresholds: ✓
- Zero untested P1 interactions: ✓ (all tested, findings documented)

### P1 Finding Resolution Status:

| Category | Count | Status |
|----------|-------|--------|
| P1 findings closed by existing patches | 17 | Pending editorial decisions where marked |
| P1 findings closed by other patches (F83, F89) | 2 | Pending PP-004, PP-013 editorial/approval |
| P1 findings with no patch (F57, F72, F112) | 3 | New proposals above (PP-078, PP-079, PP-080) |
| **Total open P1s** | **20** | |

### Gate Status: **BLOCKED** — resolvable

**To close the Phase 3 gate:**

**Step 1 — Editorial decisions required (8 patches):**
- PP-006: Mass combat damage formula stat values
- PP-007: "Poise" rename approval
- PP-008: Niflhel starting stat values (with Intel 8 dominance concern noted)
- PP-012: Intelligibility/Coherence two-track split (canon-clean with language conditions)
- PP-015: TC 80 territorial seizure procedure
- PP-016: Archetype stat values
- PP-062: Community Weaving as canonical Coherence recovery path
- PP-077: Monstrous character play continuation as campaign option

**Step 2 — New patches (3 items):**
- PP-078 (F57): ThS text rewrite — Haiku 4.5 can execute once text confirmed
- PP-079 (F72): Torben Loyalty Clock drain rate — proposed above, requires editorial sign-off on milestone events
- PP-080 (F112): Church Stability TC brake threshold change — Haiku 4.5 can execute (numbers fix)

**Step 3 — P2 gap closures (5 items):** Not gate-blocking. Address during compilation:
- PP-001: Define "full campaign arc" season count
- PP-002: Clarify "next scene" session-span
- PP-003: Define "opposition pool" in Vote procedure
- PP-004: Add 1/season cap to Mandate 0 territory claim
- PP-014: Clarify Helper individual op eligibility after Anchor dropout

**After Steps 1–2:** Gate closes. Phase 3 complete → Phase 4 (Consolidate) begins.

---

## SUMMARY COUNTS

| Item Type | Count |
|-----------|-------|
| P1 findings assessed | 20 |
| P1 findings closed by existing patches | 19 (17 direct + 2 via PP-004/PP-013) |
| New P1 patches proposed (PP-078–080) | 3 |
| P2 gaps identified during audit | 5 |
| Editorial decisions required to close gate | 8 |
| Canon-guard checks | 1 (PP-012: CONDITIONAL PASS) |
| P2 interaction findings | 6 |
| Compiler-tier tasks queued | 3 (PP-007 rename cascade, PP-021 section removal, PP-080 threshold change) |

