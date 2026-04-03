# THREADWORK AUDIT — AUD-TW-001
## Date: 2026-04-02
## Scope: Full threadworking internal audit + cross-system stress test
## Source: threadwork_redesign_v25.md (v3.1), all params files
## Model: Claude Sonnet 4.6

---

## THREE AXES (philosophical_reference.md)
- **Actuality:** presence in the world (here vs. merely possible)
- **Intelligibility:** the face consciousness can render/apprehend
- **Temporality:** accumulated past (spooled depth) + trajectory toward becoming

---

## PHASE A — INTERNAL AUDIT

### A1 — Axis Coverage: PASS
All three axes mechanically expressed:
- Actuality: Weaving (drives toward), Dissolution (tears from), Locking (freezes)
- Intelligibility: Thread Sensitivity, Diagnosis, Rendering Stability, Coherence
- Temporality: Past-Oriented Pulling, temporal weight in Diagnosis, co-movement temporal auto-effect

### A2 — Co-movement: PASS (with note)
Co-movement fires on all three dimensions. Temporal=temporality, epistemic≈intelligibility, actual d6=below-waterline residue. Philosophically consistent.

### AUD-TW-01 (P2) — Temporal weight mechanically inert for non-POP ops
Temporal weight revealed by Diagnosis but has no Ob modifier for Weaving/Lock/Dissolution. Old vs new configurations at same actualization level are mechanically identical.
Recommendation: +1 Ob for Relational+ ops targeting generational+ configurations. [EDITORIAL]

### AUD-TW-02 (P1) — P-22 paradox window: no resolution mechanic
POP + actual d6=6: 1d3-scene paradox window. No procedure for resolution. Blocks POP simulation.
Recommendation: Define auto-resolution at window end (no action) OR define a Mending-like procedure to close early.

### AUD-TW-03 (P2) — Lock axis attribution ambiguous
Design text attributes Lock to actuality ("full actualization"), intelligibility ("freezes intelligible face"), AND temporality ("unable to become"). Three-way tension, no math error.
Recommendation: Establish Lock as primarily actuality axis (over-actualization), with temporality/intelligibility as secondary consequences.

### AUD-TW-04 (P2, editorial) — Coherence/RS independence
Coherence and RS are mechanically independent. Practitioner at Coherence 1 causes no additional RS damage. RS 20 does not accelerate Coherence loss. May be intended.
[EDITORIAL: confirm intended independence vs philosophical implication of same underlying process]

### AUD-TW-05 (P1) — Rendering Crisis resolution procedure missing
Coherence 0: resolution described narratively only. No Ob, no roll, no timeline. Compare: Coherence recovery (§3.5) has specific procedures.
Recommendation: Add campaign-arc resolution mechanic (e.g., Bonds check + season commitment, more severe than §3.5).

### AUD-TW-18 (P2, editorial) — POP RS ≤ 60 gate: perverse incentive
POP easier in degraded world. Late-game (RS 20-40) = default state. May create incentive to degrade RS to enable POP.
[EDITORIAL: confirm intended]

---

## PHASE B — CROSS-SYSTEM STRESS TEST

### B1 — Thread × Personal Combat

#### AUD-TW-06 (P1) — Diagnosis+Leap combat action economy ambiguous
Diagnosis = Priority 4 standard action. Leap = Priority 5 full-round action.
Can share a round (non-combat). In combat: is it 1 round or 2?
Interpretation 1: Diagnosis is absorbed by the full-round Leap (1 round total).
Interpretation 2: Diagnosis is a separate action in a prior/same round (2 rounds minimum in combat).
"Preceding round" language in §2.2 favours Interpretation 2.
Recommendation: In combat, Diagnosis must occur in the round immediately preceding the Leap (2-round minimum). In non-combat, same-round permitted.

#### B1b — Wound disruption check: PASS
Attunement-only disruption check consistent with system.

#### B1c — Mode 3 Dissolution (R-64): PASS (minor wording note)
Intent clear. Overwhelming bypasses Mode 3 exception; all else → Partial.

### B2 — Thread × Mass Combat

#### AUD-TW-07 (P1) — Lock in both Phase 4 (offensive) and Phase 6 (support): contradiction
Phase 4 = "Offensive Thread: Dissolution, Pulling, Locking."
Phase 6 Step 5 = Support Thread (lists Lock in some references).
Recommendation: Offensive Lock (targeting enemy configuration) = Phase 4. Support Lock (stabilizing own configuration) = Phase 6. Must be declared at Phase 1.

#### AUD-TW-08 (P1) — ×3 RS multiplier not operationalized
ST-TW-03 references ×3 RS multiplier for mass battle Thread ops. Not in params_mass_combat or params_threadwork degradation table.
Recommendation: Add explicit rule in params_mass_combat §Thread Integration: "All RS costs from Thread operations in mass battle scale ×3 (e.g., Dissolution Success = −15 RS)."

#### AUD-TW-09 (P2, editorial) — FR surcharge nullified by §3.2 cap at Territorial scale
§3.2 cap = −1 max per op. Territorial Lock = −1 (scale) + −1 (FR surcharge) → capped to −1.
Result: Territorial Lock costs same Coherence as Territorial Pull.
Compare: Dissolution residue exempted from cap. Should FR surcharge be similarly exempted?
[EDITORIAL: (a) exempt FR from cap; (b) raise cap to −2 for FR; (c) intended — FR danger expressed in RS cost not Coherence]

### B3 — Thread × Social/Debate

#### AUD-TW-10 (P2) — POP displacement of debate subject: no ruling
POP can displace historical events. If debated event is displaced, Past-genre argument loses factual basis. No mechanic for this interaction.
Recommendation: Displaced event → debating party loses Memory bonus for that argument. Debate not restarted. [EDITORIAL: confirm or revise]

#### B3b — Composure × Coherence stacking: PASS
Coherence degradation penalties apply to Argue rolls. Clean.

### B4 — Thread × Factions

#### AUD-TW-11 (P1) — Community Weaving procedure undefined
RS restoration from Community Weaving listed in degradation table (+1 to +2 RS). No pool, Ob, or failure condition.
Recommendation: Define as Revolution Domain Action: Mandate + History, Ob 3. Success=RS+1, Overwhelming=RS+2, Failure=Mandate−1.

#### AUD-TW-12 (P3) — TC Investigation failure outcome
PP-182: Church investigates (Domain Action Ob 2) → TC +1. No ruling on failure.
Recommendation: Failure = wasted action, TC unchanged. Low priority; GM call acceptable.

### B5 — Thread × Clocks

#### AUD-TW-13 (P3) — RS→Stability→Mandate cascade missing from propagation_map.md
Add cross-reference to propagation_map.md. §5.3 threshold table documents it but propagation map doesn't.

### B6 — Thread × Hybrid

#### AUD-TW-14 (P2) — §9.13 reference: verify exists
§7.2 references opposing operations procedure (§9.13). P-24 covers this in mode index. Verify §9.13 is a named section in full doc.

#### AUD-TW-15 (P2) — "Narratively leads" Hybrid Coherence qualifier: ambiguous
Current: "Player Character who narratively leads the Strategic Phase order pays Coherence cost."
"Narratively" creates wiggle room for cost avoidance.
Recommendation: Replace with: "Player Character who declared leadership at start of Cascade Phase pays cost. No declaration = no cost."

### B7 — Thread × Board Game

#### AUD-TW-16 (P2) — P-23 BG degree table truncated
Mend order partial/failure outcomes not visible in doc extract. Verify in source.

#### AUD-TW-17 (P2) — Coherence initialization BG→Hybrid undefined
First activation of Hybrid from BG context: Coherence must be initialized. No ruling.
Recommendation: Coherence = 10 on first activation. Subsequent activations: GM carries narrative Coherence from prior Personal Phase sessions.

---

## FINDINGS REGISTER

| ID | Sev | System | Summary |
|----|-----|--------|---------|
| AUD-TW-01 | P2 | Temporality axis | Temporal weight inert for non-POP ops |
| AUD-TW-02 | P1 | Temporality axis | P-22 paradox window: no resolution mechanic |
| AUD-TW-03 | P2 | Actuality axis | Lock axis attribution ambiguous |
| AUD-TW-04 | P2 (ed) | Intelligibility axis | Coherence/RS independence: confirm intended |
| AUD-TW-05 | P1 | Coherence | Rendering Crisis resolution procedure missing |
| AUD-TW-06 | P1 | Combat × Thread | Diagnosis+Leap action economy: 1 or 2 rounds? |
| AUD-TW-07 | P1 | Mass Combat × Thread | Lock in Phase 4 AND Phase 6: contradiction |
| AUD-TW-08 | P1 | Mass Combat × Thread | ×3 RS multiplier not operationalized |
| AUD-TW-09 | P2 (ed) | Mass Combat × Thread | FR surcharge nullified by §3.2 cap at Territorial |
| AUD-TW-10 | P2 | Social × Thread | POP displacement of debate subject: no ruling |
| AUD-TW-11 | P1 | Faction × Thread | Community Weaving procedure undefined |
| AUD-TW-12 | P3 | Faction × Thread | TC Investigation failure outcome |
| AUD-TW-13 | P3 | Clocks × Thread | RS→Stability→Mandate not in propagation_map |
| AUD-TW-14 | P2 | Hybrid × Thread | §9.13 reference: verify exists |
| AUD-TW-15 | P2 | Hybrid × Thread | "Narratively leads" ambiguous: replace with binary |
| AUD-TW-16 | P2 | BG × Thread | P-23 BG table truncated: verify |
| AUD-TW-17 | P2 | BG/Hybrid × Thread | Coherence init BG→Hybrid undefined |
| AUD-TW-18 | P2 (ed) | Temporality axis | POP RS≤60 gate: perverse incentive confirm intended |

## CONFIRMED PASSES
- A1: All three axes mechanically expressed
- A2: Co-movement consistent with philosophical framing
- A3b: Trajectory perception scales correctly with scale principle
- A4b: Over-actualization philosophically consistent and clean
- B1b: Wound disruption check consistent
- B3b: Composure/Coherence stacking clean
- B4b: Mandate 0 → Community Mending blocked: intended feedback loop

## SIM-DEBT ADDITIONS
- SIM-DEBT-TW-01: P-22 paradox window stress test — blocked on AUD-TW-02
- SIM-DEBT-TW-02: Rendering Crisis resolution arc — blocked on AUD-TW-05
- SIM-DEBT-TW-03: Mass battle ×3 RS multiplier validation — blocked on AUD-TW-08
- SIM-DEBT-TW-04: Hybrid Coherence 10-session campaign — blocked on AUD-TW-15

---
*valoria-mechanic-audit (Sonnet 4.6) | 2026-04-02*
