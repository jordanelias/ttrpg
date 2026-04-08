# Social Contest — Audit (Modes A–E) + Simulation (Modes A+D)
## Date: 2026-04-08
## Source: debate_system_redesign_v1.md v1.7 (input) → v1.8 (output after fixes)
## Patches applied this pass: PP-465–PP-468

---

## FETCH LOG
- designs/debate/debate_system_redesign_v1.md: ✓ 821 lines (v1.7 input)
- references/params_debate.md: ✓ 406 lines (v0.14+design-ST4-R2 input)
- canon/02_canon_constraints.md: ✓ 25 lines
- references/propagation_map.md: ✓ 375 lines

---

## AUDIT MODE A — Formula Validation

22 formulas checked. 3 issues found.

| ID | Formula | Status |
|---|---|---|
| F-01–F-06 | Presence modifier, Focus defence, Composure, Concentration, Argue pool, Appraise pool | ✓ All clean |
| F-07 | Refute: Recall alone, Ob 2 | ✗ P1 — Recall 1 = ~18% success. Near-impossible at low Recall. Fixed PP-465: Ob→1 |
| F-08–F-10 | Bonds, effective_margin (Revealing), CT movement | ✓ Clean |
| F-11 | CROSS effective_margin: floor(succ/2 × GW). At succ=1, GW=0.5: floor(0.25)=0 | ⚠ P2 — single-success CROSS in Opposed genre always produces 0 effective_margin. Intentional: Opposed genre should be near-inert. Confirmed design intent. No fix needed. |
| F-12–F-16 | Strain, AMPLIFY strain, resistance, Regroup restore, Concentration depletion | ✓ Clean |
| F-17 | BG vote effective_vote: genre_weight unspecified | ✗ P2 — scope unclear. Fixed PP-466: explicitly PP-453 adjacency weights |
| F-18–F-22 | AMPLIFY cap, Doubt Marker, Total Victory, Fatigue trigger, Prep pool | ✓ Clean |

---

## AUDIT MODE B — Number System Coherence

10 systems checked. 1 finding.

| System | Range | Status |
|---|---|---|
| Conviction Track | 0–10 | ✓ Unique to Social Contest; no cross-system conflict |
| Composure | 7–13 (Cha+6) | ✓ PP-460 aligned to Health formula. Consistent |
| Concentration | Focus+Presence (2–14) | ⚠ P2 — Wide range vs Stamina (2–8). High-Focus+Presence characters near-immune to Spent in Grand Debate. Noted B-01. No structural fix warranted — Concentration is a build investment; immunity is a valid character archetype at cost of other stats. |
| Strain | 0→Composure | ✓ |
| Genre weights | 0.5/0.75/1.0/1.25 | ✓ PP-453 adjacency. Four clean levels. |
| Audience resistance | 1–2 | ✓ Narrow by design; prevents impassable audiences |
| Doubt Marker | Binary | ✓ |
| Debate Fatigue | 0 or 1/session | ✓ |
| BG CT | 0–10 | ✓ Structural parity with TTRPG CT |
| Hybrid offset | ±0–2 capped | ✓ PP-120 clamp correct |

**B-01 [P2 — no fix]:** Concentration range 2–14 allows Focus 5 + Presence 5 = 10 Concentration. Grand Debate (5 exchanges): 5×−1 standard + up to 5×−1 loss = maximum −10. Character with Concentration 10 can lose every exchange without Spending. This is a deliberate build-investment tradeoff, not a flaw. Confirmed as design intent.

---

## AUDIT MODE C — Interaction Chains

20 chains mapped. 1 gap found (C-01, resolved PP-466).

No circular dependencies. No dead-end mechanics. No amplification loops.

Notable chain analysis:
- **Doubt Marker feedback:** One-time consumed effect. Not a loop. ✓
- **Rattled deepening:** Persistent state, not a re-triggering threshold. FocusDef loss accelerates strain but does not loop. ✓
- **Regroup neutrality (PP-454):** Regroup now feeds 0 to CT. Clean isolated recovery action. ✓
- **BG→TTRPG Hybrid chain:** BG offset → clamped 4–6 → TTRPG CT start → personal debate → outcome. One-way, no feedback. ✓

---

## AUDIT MODE D — Gap Detection

20 targeted gap checks. Findings:

| ID | Severity | Description | Resolution |
|---|---|---|---|
| D-G19 | **P1** | Refute Ob 2 inaccessible at Recall 1–2 | PP-465: Ob→1 |
| D-G01/D-G20 | **P2** | §6.13 BG vote genre_weight unscoped to PP-453 | PP-466 |
| D-G04 | **P2** | [EDITORIAL: Concentration attribute] in §5.1 still open | PP-468: marked resolved |
| D-G06 | P3 | Corroborator cannot Refute on behalf of orator (undefined) | Confirmed: Refute is primary orator only. P3 — document implicitly covers this |
| D-G16 | P3 | §5.1 editorials in deprecated Parts 1–4 | Not operative; no action needed |
| D-G03 | — | SIM-DEBT-02 (corroboration CLASH calibration) still open | Carried forward |
| All others | — | 15 gap checks passed ✓ | — |

---

## AUDIT MODE E — Core Principles Compliance

13 principles checked.

| Principle | Status |
|---|---|
| P1: Roll only when meaningful | ✓ PRESENT |
| P2: Let It Ride | ✓ PRESENT |
| P3: Fail Forward | ✓ PRESENT |
| P4: Histories, not Skills | ✓ PRESENT |
| P5: Pool = Attribute + History | ✓ ALTERED (justified — role specialisation) |
| P6: Wound/escalating Ob | ~ ABSENT (deliberate — threshold debuff model instead) |
| P7–P8: Spirit, Virtues | – NOT APPLICABLE (Momentum/Belief interface present) |
| P9: Social combat via Rhetoric | ✓ PRESENT |
| P10–P12: Reach, Phase-based, Beginner's Luck | – NOT APPLICABLE or PARTIAL |
| P13: Circles/Resources | – ADJACENT (Domain Echo interface present) |

**0 compliance failures.**

---

## SIMULATION MODE A — Genre Weight Model Verification

Post-PP-453 adjacency model confirmed effective.

CT movement at R=1:

| Margin | Opposed ×0.5 | Adjacent ×0.75 | Primary ×1.0 | Boosted ×1.25 |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 1 | 1 |
| 3 | 0 | 1 | 2 | 2 |
| 4 | 1 | 2 | 3 | 4 |
| 5 | 1 | 2 | 4 | 5 |

**Dominant strategy disrupted: YES.**
- Adjacent genre (×0.75) produces CT+1 at margin 3, CT+2 at margin 4. Viable alternative to primary.
- Boosted primary (×1.25) remains strongest at each margin level — correct.
- Opposed genre remains inert at margins 1–2 (correct — opposite of audience resonance).
- Strategic space: characters with Adjacent-domain History can compete; going Primary is still optimal but not overwhelmingly dominant.

**Appraise false signal:** Playing Opposed as if Primary at margin 3 = CT+0. Meaningful punishment. Fail Forward satisfied.

---

## SIMULATION MODE D — New Mechanic Edge Cases

4 cases tested:

| ID | Severity | Finding | Resolution |
|---|---|---|---|
| SD-01 | P3 | Refute multi-opponent: second Refute against already-denied Memory bonus has no target | PP-465: rule clarified — denied bonus may not be Refuted again |
| SD-02 | P3 | Regroup during Deadlock State: legal but implicit | PP-467: confirmed and stated explicitly |
| SD-03 | P2 | Deadlock State + Doubt Marker: applies but unstated | PP-467: Doubt Marker confirmed active in Deadlock |
| SD-04 | P3 | Concentration minimum-loop: Regroup-loop is surrender in slow motion, not an exploit | Confirmed. No fix. |

---

## OVERALL STATUS POST-AUDIT

**P1 findings: 0 remaining** (1 found, 1 resolved — PP-465)
**P2 findings: 1 remaining** (B-01: Concentration range — confirmed design intent, no fix)
**P3 findings: 0 requiring action** (SD-04 confirmed non-exploit; SD-01/02 resolved PP-465/467)
**SIM-DEBT-02: open** (corroboration CLASH calibration — carried from prior session)

Design doc: v1.8. Params: v0.14+design-ST4-R3.
Social Contest system is **simulation-clean** after PP-449–PP-468.
