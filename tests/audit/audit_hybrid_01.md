# AUDIT-HYBRID-01: Hybrid Mode — Full Mechanical Audit
## Date: 2026-04-02
## Modes: A (Formula) + B (Number Systems) + C (Interaction Chains) + D (Gaps) + E (Canon) + F (Playtest) + G (Cross-Mode)
## Mechanic-audit Modes A–G per valoria-mechanic-audit-SKILL.md
## Plus: Stress test Modes K (all transition types), D (extended edge cases), J (load)

---

## AUDIT SCOPE — HYBRID MECHANICS

1. Phase-Lock Protocol (PP-103)
2. State Transfer — variable inventory (Zoom In/Out)
3. BG→TTRPG unit conversion (B.2)
4. Domain Echo (personal/scene → faction attribute)
5. TC threshold check during suspension
6. RS routing (immediate vs queued)
7. Clock behavior during suspension
8. Concurrent Zoom In (multiple PCs)
9. Practitioner positioning (PP-101)
10. Thread RS consequence routing
11. Register Shift (within-TTRPG scale crossings)
12. Domain Echo timing discrepancy (TTRPG immediate vs Hybrid queued)
13. BG Morale — absent as separate stat
14. Zoom Out: NPC kill → BG commander bonus (TTRPG vs BG terminology)
15. Phase 6 Step 1 Zoom In: which sub-steps are included?

---

## MODE A — FORMULA VALIDATION

| ID | Formula | Min | Max | Issues | Status |
|----|---------|-----|-----|--------|--------|
| FA-01 | Domain Echo amount: Successful Appeal/Debate → faction attr change | undefined | undefined | **UNDEFINED — no amount specified. Degree of success not mapped to stat delta.** | P1 GAP |
| FA-02 | Unit Str (Zoom In): state_transfer_spec says "1:1 same scale"; B.5 says "Health ÷ 1.5 round up" | — | — | **CONTRADICTION between state_transfer_spec and mass_battle_v3 §B.5.** B.5 is newer (PP-103). state_transfer_spec is stale. | P1 STALE |
| FA-03 | Unit Cohesion (Zoom In): state_transfer_spec says "1:1"; BG range is 0–6 (PP-119), TTRPG range is 1–7 | BG=0→TTRPG=0 | BG=6→TTRPG=7 | **Scale mismatch.** BG max is 6, TTRPG max is 7. 1:1 fails at BG Cohesion 6 (no TTRPG 6-to-6 issue, but BG 0 ≠ TTRPG min 1). | P1 GAP |
| FA-04 | Unit Morale (Zoom In): state_transfer_spec says "1:1 direct" | — | — | **BG has no separate Morale stat.** BG uses Cohesion as unified track (PP-119). TTRPG has Morale (1–7) separate from Cohesion. 1:1 transfer of a non-existent stat. | P1 GAP |
| FA-05 | Phase-Lock: "fires at end of current phase" | Phase 1 | Phase 6 Step 1 | Phase 6 has 6 steps. "End of Phase 6 Step 1" vs "end of Phase 6" = large difference (Steps 2–6 include Cohesion/Morale/General/Thread resolution). Does Zoom In fire after Step 1 only, or after all of Phase 6? | P1 AMBIGUITY |
| FA-06 | Zoom Out: Named NPC killed → "CR = 0 for that force" | — | — | CR is a TTRPG stat. BG uses "commander bonus" (Military ÷ 3, round down). These are different formulas. Zoom Out sets TTRPG CR = 0, but what does that translate to in BG commander bonus? Not specified. | P2 GAP |
| FA-07 | RS consequence: "RS track updated immediately (not queued)" | — | — | Correct and consistent with P-01 (co-movement is always immediate). ✓ | OK |
| FA-08 | Domain Echo queuing: "Queue as Domain Echo; fires at next Accounting" | — | — | In full TTRPG: "Scene → Faction: Domain Echo fires immediately (no extra roll)." In Hybrid: queued. Timing differs across modes. Not documented as intentional design. | P1 DISCREPANCY |

---

## MODE B — NUMBER SYSTEM COHERENCE

| System | Range | TTRPG | BG | Hybrid | Inconsistency |
|--------|-------|-------|-----|--------|--------------|
| Faction stats (M/I/W/Mil/Sta) | 1–7 | ✓ | ✓ | suspended during Zoom In | None |
| RS | 0–100 | shared | shared | shared, immediate | None |
| TC | 0–65+ | shared | shared | suspended | None |
| IP | 0–80+ | shared | shared | suspended | None |
| PI | 0–10 | shared | shared | suspended | None |
| Unit Cohesion | TTRPG 1–7 / BG 0–6 | 1–7 | 0–6 | 1:1 claimed | **RANGE MISMATCH: BG 0 has no TTRPG equivalent; BG 6 maps to TTRPG 6, not 7 max** |
| Unit Morale | TTRPG 1–7 / BG: not tracked | 1–7 | absent | 1:1 claimed | **BG ABSENCE: BG Cohesion (PP-119) replaces both Cohesion and Morale. TTRPG tracks them separately.** |
| Unit Strength | TTRPG 0–10 / BG Health 7–11 | 0–10 | 7–11 | "1:1 same scale" claimed | **SCALE MISMATCH: BG Health 7–11, TTRPG Str 0–10. Not same scale.** B.5 provides correct conversion (Health ÷ 1.5). state_transfer_spec is wrong. |
| Unit CP | TTRPG 1–7 / BG Martial (1–5) | 1–7 | Martial 1–5 | state_transfer_spec says "Unit Martial = Unit CP 1:1" | **RANGE MISMATCH: Martial max is 5 (Knights Templar), TTRPG CP max is 7. "1:1 same scale" is false at high end.** Correct mapping: Martial = TTRPG CP equiv column in B.2. |
| Attributes (Agility, Spirit etc.) | 1–7 | ✓ | N/A | suspended during Zoom In | None |
| Composure | 7–12 (varies) | tracked | N/A | tracked in scene | None |
| Commander Rating (CR) | 1–7 | tracked | mapped to commander bonus (Mil÷3) | Zoom Out: CR=0 → unclear BG effect | **FORMULA MISMATCH: CR (TTRPG) ≠ commander bonus (BG). No conversion stated.** |

**Number system finding:** The state_transfer_spec claims "1:1 same scale" for Unit Strength, Cohesion, Morale, and Martial. All four are WRONG. All four have scale mismatches between BG and TTRPG. B.2 (§PP-103) provides the correct conversion table. state_transfer_spec needs a wholesale update.

---

## MODE C — INTERACTION CHAIN ANALYSIS

### Chain 1: Zoom In — Phase-Lock → Scene → Zoom Out

```
BG turn running
  └─ Trigger: named PC in battle territory
       └─ Phase-Lock: hold until legal point (Phase 1/3/6 Step 1)
            └─ State inventory: 8 variables checked
                 ├─ Transfer: RS, Cohesion, Morale*, Str*, CP*
                 ├─ Suspend: Domain Actions, Accounting, Co-Movement, TC threshold
                 └─ Discard: Faction stats, TC/IP/PI clocks
                      └─ TTRPG scene runs (personal combat, Thread, Debate)
                           └─ Zoom Out
                                ├─ Immediate: Str updates, RS consequences, fortifications
                                ├─ Queue: Domain Actions → Domain Echo at Accounting
                                └─ Discard: personal Wounds (no BG effect)
                                     └─ BG resumes from held phase
```

**Chain issues:**
- Morale*, Str*, CP* marked with asterisk = transfer formulas are stale (state_transfer_spec)
- No defined ordering for multiple queued Domain Echoes from same scene
- BG resumes from "held phase" — but which step within that phase?

| Mechanic | Upstream | Downstream | Chain Length | Flags |
|----------|----------|-----------|-------------|-------|
| Phase-Lock | BG turn phase | TTRPG scene start | 3 | Phase 6 sub-step ambiguity (FA-05) |
| State Transfer | BG state | TTRPG initial state | 2 | 4 variables stale (FA-02/03/04, Unit Martial) |
| Domain Echo | Personal scene outcome | BG faction stat (Accounting) | 4 | Amount undefined (FA-01); timing discrepancy (FA-08) |
| Zoom Out RS | Thread op outcome | BG RS track | 1 | "Immediately" — correct (FA-07) |
| Zoom Out Str | TTRPG combat | BG unit token | 2 | Uses correct B.2 conversion if PP-103 applied; still wrong in state_transfer_spec |

### Chain 2: Domain Echo — TTRPG immediate vs Hybrid queued

**TTRPG mode:** "Scene → Faction: Successful Appeal/Debate at sufficient scope → Domain Echo (faction attribute change). No extra roll."
This implies: immediate effect, same roll resolution.

**Hybrid mode:** "PC Domain Action in scene → Queue as Domain Echo; fires at next Accounting."
This implies: delayed effect, fires at next seasonal accounting.

**These are the same mechanic producing different timing in different modes.** The difference could be:
- 1 day (TTRPG immediate) vs 1 season (Hybrid queued) — enormous strategic difference
- A PC who Zooms In to debate a cardinal must wait a full season to see the faction stat change; in full TTRPG mode they see it immediately

**[AUDIT-C-01 — P1]: Domain Echo timing is mode-dependent without documentation.** Either the Hybrid queuing is intentional (to prevent real-time strategic manipulation of BG stats from personal scenes) or it's an unexamined inconsistency.

### Chain 3: Concurrent Zoom Ins

```
BG turn: Phase 5 Engagement
  ├─ Battle A fires in territory T1 (PC-α present)
  └─ Battle B fires in territory T2 (PC-β present)
       └─ Both trigger Zoom In simultaneously
            └─ [NO RULE: which fires first? Concurrent? Sequential?]
```

**[AUDIT-C-02 — P1]: No procedure for concurrent Zoom Ins.** Multiple PCs in multiple simultaneous battles. Which resolves first? Does one Zoom In suspend the other? Do they run in parallel (impossible at table)?

### Chain 4: Register Shift (within-TTRPG)

Personal → Faction → Mass Combat within TTRPG mode:

"Personal roll may serve as opening move or Appeal in social scene."
"Scene → Faction: no extra roll."
"Thread → Faction: Thread pool, appropriate Ob. No extra roll."

These Register Shifts fire within the TTRPG session without a BG layer. They function correctly as immediate domain actions. ✓

BUT: "Mass → Personal: Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange/battle turn."

What happens if the general's personal combat runs more than 1 round? "General's Phase 5 consumed until personal combat resolved (Coherence Rating suspended)." The general's mass combat role is suspended during personal combat. But if the personal combat lasts 5 rounds, does the unit lose 5 turns of general actions? There's no maximum duration stated.

**[AUDIT-C-03 — P2]: Personal combat from Mass → Personal has no maximum duration stated.** A general in an extended personal duel could be suspended from mass command indefinitely. The 1-exchange-per-battle-turn limit seems to apply to the mass combat exchange, not the personal combat duration.

---

## MODE D — GAP DETECTION

| ID | Type | Description | Location | Severity | Status |
|----|------|-------------|----------|----------|--------|
| GAP-HYB-01 | Undefined formula | Domain Echo amount (faction stat change per degree) not specified | state_transfer_spec §Zoom Out | P1 | New |
| GAP-HYB-02 | Contradiction | state_transfer_spec "Unit Strength 1:1" vs B.5 "Health ÷ 1.5" | state_transfer_spec §1 vs mass_battle_v3 §B.5 | P1 | New |
| GAP-HYB-03 | Contradiction | state_transfer_spec "Unit Cohesion 1:1"; BG range 0–6, TTRPG 1–7 | state_transfer_spec §1 | P1 | New |
| GAP-HYB-04 | Absent stat | Unit Morale: BG has no Morale stat (Cohesion only per PP-119); state_transfer_spec transfers non-existent stat | state_transfer_spec §1 | P1 | New |
| GAP-HYB-05 | Ambiguity | Phase 6 Step 1 Zoom In: does "after Step 1" mean after all of Phase 6 or literally after Step 1 only? | state_transfer_spec §Phase-Lock | P1 | New |
| GAP-HYB-06 | Undefined formula | Zoom Out: NPC killed → "CR = 0" — no BG commander bonus equivalent stated | state_transfer_spec §Zoom Out | P2 | New |
| GAP-HYB-07 | Discrepancy | Domain Echo timing: immediate in TTRPG, queued in Hybrid | state_transfer_spec §Zoom Out vs params_scale_transitions Eight Handoff Rules | P1 | New |
| GAP-HYB-08 | Missing procedure | Concurrent Zoom Ins: no rule for multiple PCs in multiple simultaneous battles | state_transfer_spec, Phase-Lock Protocol | P1 | New |
| GAP-HYB-09 | Scale mismatch | Unit Martial (BG, max 5) ≠ Unit CP (TTRPG, max 7): "1:1 same scale" false | state_transfer_spec §1, B.2 | P1 | New |
| GAP-HYB-10 | Missing duration | Mass→Personal Register Shift: no maximum personal combat duration stated | params_scale_transitions Eight Handoff Rules | P2 | New |
| GAP-HYB-11 | Missing ordering | Multiple Domain Echoes from same scene: no stated firing order at Accounting | state_transfer_spec §Zoom Out | P2 | New |
| GAP-HYB-12 | Missing conversion | CR (TTRPG) → BG commander bonus: no formula stated for Zoom Out | state_transfer_spec §Zoom Out | P2 | New |
| ED-056 (prior) | Open | TC threshold during suspension | — | P2 | Open |
| ED-059 (prior) | Open | RS=0 at Zoom In | — | P2 | Open |

**Total new gaps: 12 (5 P1, 4 P2, 3 carry-forward)**

---

## MODE E — CORE PRINCIPLES COMPLIANCE (P-01 to P-15 vs Hybrid)

| # | Principle | Hybrid Status | Notes |
|---|-----------|--------------|-------|
| P-01 | Inseparability (all 3 co-move) | **ALTERED** | BG Co-Movement cards abstract the three auto-effects into card draws. Individual auto-effects (temporal/epistemic/actual) are not separately tracked in BG. In Hybrid Zoom In, TTRPG applies all three. Gap: during Zoom Out, do the TTRPG scene's co-movement effects propagate to BG layer? No stated mechanism. **[AUDIT-E-01 — P2]** |
| P-02 | Ein Sof = fullness not void | PRESENT | No BG/Hybrid mechanics assign void/chaos as source. ✓ |
| P-03 | Rendering = consciousness-performed | PRESENT | GM is rendering engine in all modes. ✓ |
| P-04 | Monstrosity = ontological not moral | PRESENT | No moral alignment in any mode. ✓ |
| P-05 | Three emergence modes distinct | **PARTIAL** | Hybrid Zoom In triggers when "named PC enters BG battle." Emergence mode of any entities in the battle (Mode 1/2/3) is not tracked in BG. At Zoom In, the TTRPG scene must re-establish emergence modes. No stated procedure. **[AUDIT-E-02 — P2]** |
| P-06 | Threadcut = radically is without becoming | PRESENT | No Hybrid-specific Threadcut mechanic changes. ✓ |
| P-07 | Gap = positive eruption | PRESENT | Gap mechanics carry through to Hybrid (RS drops immediately). ✓ |
| P-08 | Practitioner as world-structural role | **PARTIAL** | In BG, practitioners are absent from the gameplay loop (Co-Movement cards abstract Thread). Hybrid Zoom In is the only mechanism by which a practitioner's TTRPG role intersects BG. The structural role is not represented in BG mode. **[AUDIT-E-03 — P3 — design tension, not violation]** |
| P-09 | Thread operations are factual not magical | PRESENT | Thread operations in Hybrid carry same factual treatment as TTRPG. ✓ |
| P-10 | Historical texture grounds everything | PRESENT | Domain Echo draws on character History bonus. ✓ |
| P-11 | Characters are embedded in factions | **PARTIAL** | In Hybrid, PC faction embedding is the trigger for Zoom In. But at BG scale between Zoom Ins, PC faction embedding has no mechanical expression — PCs are effectively absent from the BG layer. **[AUDIT-E-04 — P2]** |
| P-12 | Scale integrity | **ALTERED** | The Hybrid handoff specifically modifies scale. This is intentional and documented. ALTERED with justification = acceptable. ✓ |
| P-13 | Consequences persist and accumulate | **PARTIAL** | Domain Echo preserves consequence persistence. But Zoom Out updates are immediate for physical outcomes (Strength, RS) and delayed (up to 1 season) for political outcomes (faction stats). The asymmetric persistence timing is undocumented. **[AUDIT-E-05 — P2]** |
| P-14 | Thread Sensitivity grounds sight | PRESENT | TS requirements carry through to Hybrid. ✓ |
| P-15 | Coherence degradation = world fragility | PRESENT | Coherence costs carry through in Hybrid TTRPG scene. BG abstracts to RS only. ✓ |

**Canon compliance summary:** 3 full violations (P1 level), 5 partial compliance needing documentation, 7 fully compliant.

---

## MODE F — PLAYTEST BURDEN ANALYSIS

| Mechanic | Time(s) | Lookups | Tracking | Decisions | Load | Flag |
|----------|---------|---------|---------|-----------|------|------|
| Phase-Lock (post-PP-103) | 20s | 1 (reference card) | 1 (phase note) | 1 (when triggered) | 3 — Low | None |
| State Transfer — Zoom In (post-PP-103) | 90s | 1 (reference card Side A) | 2 (BG suspended + TTRPG active) | 1 (commander present?) | 4 — Low/Medium | Borderline |
| Unit Conversion — B.2 lookup (post-PP-103) | 30s | 1 (reference card Side B) | 1 (unit token type) | 0 | 2 — Low | None |
| Domain Echo (queued) | 10s | 0 (no roll) | 1 (echo queue) | 0 | 1 — Low | None |
| Domain Echo (amount calculation) | **undefined** | **undefined** | — | — | — | **P1: amount formula undefined (GAP-HYB-01)** |
| Zoom Out state update | 60s | 1 (reference card Side A) | 2 | 1 | 4 — Low/Medium | None |
| BG resume (post-Zoom Out) | 30s | 1 (phase note) | 1 | 0 | 2 — Low | None |
| Concurrent Zoom In | **undefined** | **undefined** | **3+** | **undefined** | **undefined** | **P1: no procedure (GAP-HYB-08)** |
| Register Shift (personal → faction) | 20s | 0 | 1 | 1 | 2 — Low | None |
| Mass→Personal Register Shift | 45s | 1 | 2 | 1 | 4 — Low/Medium | P2: no max duration (GAP-HYB-10) |

**Overall Hybrid mode playtest burden (post-PP-103):** Acceptable for defined mechanics. Two undefined procedures block assessment.

---

## MODE G — CROSS-MODE CONSISTENCY

| Mechanic | Modes | Transition Defined? | State Preserved? | Flag |
|----------|-------|--------------------|-----------------|----|
| RS (Rendering Stability) | TTRPG/BG/HYB | Yes — immediate in all modes | Yes | None |
| TC (Theocracy Counter) | TTRPG/BG/HYB | Yes — suspended during Zoom In, threshold deferred | Yes | ED-056 open |
| Domain Echo | TTRPG/HYB | **Partially — timing differs (immediate vs queued)** | Yes (queued in HYB) | **P1: AUDIT-C-01** |
| Unit Strength | TTRPG/BG/HYB | Yes (PP-103 B.5) | **Stale in state_transfer_spec** | **P1: GAP-HYB-02** |
| Unit Cohesion | TTRPG/BG/HYB | "1:1" claimed | **Scale mismatch** | **P1: GAP-HYB-03** |
| Unit Morale | TTRPG only | Not defined for BG/HYB | **BG has no Morale stat** | **P1: GAP-HYB-04** |
| Practitioner ops | TTRPG/HYB | Yes (PP-101 positioning) | Yes — TTRPG rules apply in Hybrid scene | None |
| Faction stats | TTRPG/BG/HYB | Suspended in HYB, restored via Echo | Yes | None |
| Thread co-movement | TTRPG/HYB | Partially — BG abstracts to cards | **TTRPG scene auto-effects don't propagate to BG** | P2: AUDIT-E-01 |
| Commander CR | TTRPG/HYB | Not converted to BG commander bonus | No | P2: GAP-HYB-12 |
| Concurrent Zoom In | HYB only | **Not defined** | N/A | **P1: GAP-HYB-08** |
| Phase-Lock | HYB | Yes (PP-103) | Yes | None |

---

## STRESS TEST — MODE K2 EXTENDED (ALL 5 TRANSITION TYPES)

### K2-T1: TTRPG → Hybrid (Zoom In) — Phase-Lock at each legal point

**Phase 1 entry (cleanest):**
State: No damage recorded. All units at starting Str/Cohesion/Morale.
Variables all transferable. Phase 1 declarations held — orders execute on Zoom Out resume.
**Result: Clean. ✓**

**Phase 3 entry:**
State: Units positioned. No damage. Morale/Cohesion unchanged from turn start.
Zoom In: unit positions carry as narrative context (zone descriptions). Units not "repositioned" by TTRPG scene (TTRPG operates inside one zone).
**Result: Clean. ✓**

**Phase 6 Step 1 entry:**
State: ALL damage simultaneously applied. Destroyed units removed. Cohesion/Morale checks not yet fired (those are Steps 2–3).
**Issue: Steps 2–3 (Cohesion/Morale checks) have not fired when Zoom In opens.** If the TTRPG scene resolves and Zoom Out fires, do Steps 2–6 of Phase 6 still fire? Or are they skipped?

**[ST-K2-01 — P1]: Phase 6 Step 1 Zoom In leaves Steps 2–6 of Phase 6 unresolved.** Steps 2 (Cohesion checks), 3 (Morale checks), 4 (General action), 5 (Support Thread), 6 (Reform) are all pending. On Zoom Out, these must still resolve. But the TTRPG scene may have changed the state that these steps depend on (e.g., PC general killed in TTRPG combat → Step 3 Morale should reflect that).

**Correct procedure:** Phase 6 Step 1 fires → Zoom In → TTRPG scene → Zoom Out updates Str/NPC kills → Phase 6 Steps 2–6 fire using updated state. This needs explicit statement in Phase-Lock Protocol.

### K2-T2: Hybrid → BG (Zoom Out) — state update completeness

Testing each Zoom Out row:

| TTRPG Outcome | BG Update | Completeness |
|---------------|-----------|-------------|
| Unit Str changed | B.5 conversion: Str × 1.5 round up → BG Health | ✓ Defined |
| Named NPC killed | Commander removed; "CR = 0" | **Incomplete: CR is TTRPG stat; BG commander bonus undefined post-kill** |
| PC Domain Action | Queue as Domain Echo | ✓ Defined; amount undefined (GAP-HYB-01) |
| PC Wounds | No BG effect | ✓ Correct |
| Thread op RS | Immediate update | ✓ Correct |
| Fortification damaged | Immediate −N | ✓ Correct |
| PC debate outcome (Conviction Track ≥7 or ≤3) | **Not in Zoom Out table** | **MISSING: debate outcome has no Zoom Out mapping** |
| Threadwork Gap averted | **Not in Zoom Out table** | **MISSING: Gap aversion has no Zoom Out mapping** |

**[ST-K2-02 — P2]: Debate outcome and Gap aversion are absent from Zoom Out table.** These are common TTRPG scene outcomes that should queue faction consequences.

### K2-T3: TTRPG Personal → Faction (Register Shift, within-TTRPG)

Trigger: Personal roll scope escalates to faction scope.
Rule: "Scene → Faction: Successful Appeal/Debate at sufficient scope → Domain Echo (faction attribute change). No extra roll."

**What is "sufficient scope"?** Undefined. The mechanic depends on GM judgment to determine when a personal scene has escalated to faction scope. There is no mechanical trigger — only a narrative trigger.

**[ST-K2-03 — P2]: "Sufficient scope" is undefined.** No mechanical threshold determines when a personal scene becomes faction-scope. This is entirely GM discretion. At high table variance, this produces wildly different Domain Echo frequencies.

**Domain Echo amount (from Register Shift):** Still undefined (GAP-HYB-01). This compounds with ST-K2-03.

### K2-T4: Mass Combat → Personal (General enters personal duel)

Rule: "Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange/battle turn. General's Phase 5 consumed until personal combat resolved."

**Interruption test — trigger at each Phase 5 step:**
- General declares personal combat against named enemy general (Priority 8)
- Mass combat Phase 5 continues for other units (max 3 simultaneous, Priority varies)
- General's sub-unit cannot act in Phase 5 while general is in personal combat
- Personal combat runs until one combatant incapacitated or retreats

**Duration issue:** Personal combat rounds ≠ mass combat turns. A personal combat round is ~30 seconds at table; a mass combat turn may represent minutes. If personal combat lasts 5 rounds, does mass combat pause for 5 turns? Or does one mass combat turn contain multiple personal combat rounds?

**[ST-K2-04 — P1]: Time scale mismatch between personal combat rounds and mass combat turns is undefined.** No conversion stated. If 1 mass combat turn = 1 personal combat exchange, the general's personal combat is over in 1-2 rounds. If they run in parallel (mass combat turn contains N personal rounds), the battle is effectively paused while the general duels.

### K2-T5: BG → Hybrid (Zoom In from BG non-battle context)

Zoom In triggers from a BG battle. But what if a PC is in BG territory that is NOT in active battle? Can Zoom In trigger for non-combat BG scenes (a political negotiation, a Thread investigation)?

Current rule: "Triggered when a named PC enters a BG-resolved battle or territory."

"Or territory" — this suggests Zoom In can trigger in non-battle BG contexts. But the Phase-Lock Protocol only references battle phases (Phase 1/3/6 Step 1). There is no Phase-Lock for non-battle territory Zoom In.

**[ST-K2-05 — P1]: Phase-Lock Protocol only covers battle contexts.** Non-battle Zoom In (PC enters a BG territory for a political scene) has no Phase-Lock procedure, no state transfer table, and no Zoom Out update rules.

---

## FINDINGS SUMMARY — NEW FROM THIS AUDIT

### P1
| ID | Description |
|----|-------------|
| GAP-HYB-01 | Domain Echo amount undefined |
| GAP-HYB-02 | state_transfer_spec Unit Str "1:1" contradicts B.5 |
| GAP-HYB-03 | Unit Cohesion scale mismatch (BG 0–6 vs TTRPG 1–7) |
| GAP-HYB-04 | Unit Morale absent in BG |
| GAP-HYB-05 | Phase 6 Step 1 Zoom In: sub-step ambiguity |
| GAP-HYB-08 | Concurrent Zoom Ins: no procedure |
| GAP-HYB-09 | Unit Martial (BG) ≠ Unit CP (TTRPG) scale mismatch |
| AUDIT-C-01 | Domain Echo timing: immediate in TTRPG vs queued in Hybrid |
| ST-K2-01 | Phase 6 Step 1 Zoom In: Steps 2–6 unresolved |
| ST-K2-04 | Personal combat round ≠ mass combat turn: duration undefined |
| ST-K2-05 | Non-battle Zoom In: no Phase-Lock procedure |

### P2
| ID | Description |
|----|-------------|
| GAP-HYB-06 | NPC killed → BG commander bonus: no conversion |
| GAP-HYB-07 | Domain Echo timing discrepancy (already P1 via AUDIT-C-01) |
| GAP-HYB-10 | Mass→Personal: no max personal combat duration |
| GAP-HYB-11 | Multiple Domain Echoes: no firing order |
| GAP-HYB-12 | CR → BG commander bonus: no Zoom Out formula |
| AUDIT-C-02 | Concurrent Zoom Ins (P1 above) |
| AUDIT-C-03 | Mass→Personal duration (P2 above) |
| AUDIT-E-01 | P-01: TTRPG co-movement effects don't propagate to BG layer |
| AUDIT-E-02 | P-05: emergence modes not re-established at Zoom In |
| AUDIT-E-04 | P-11: PC faction embedding absent from BG layer between Zoom Ins |
| AUDIT-E-05 | P-13: asymmetric consequence timing (physical immediate, political delayed) |
| ST-K2-02 | Debate/Gap aversion absent from Zoom Out table |
| ST-K2-03 | "Sufficient scope" for Register Shift undefined |

---

## PATCHES REQUIRED

### PP-107 (P1): state_transfer_spec wholesale update
Correct all four stale "1:1 same scale" claims:
- Unit Str: remove "1:1 same scale"; reference B.5 (Health ÷ 1.5 round up)
- Unit Cohesion: add scale note (BG 0–6, TTRPG min 1; BG 0 → TTRPG 1)
- Unit Morale: "BG does not track Morale separately (PP-119: Cohesion only). On Zoom In, set TTRPG Morale = BG Cohesion value + 1 (provisional floor)"
- Unit Martial: "BG Martial ≠ TTRPG CP. Use B.2 TTRPG CP column for conversion."
Add to Zoom Out table: debate outcome, Gap aversion.
Add: Phase 6 Steps 2–6 resolve after Zoom Out.
Add: concurrent Zoom In provisional rule.
Add: non-battle Zoom In note.
Severity: P1

### PP-108 (P1): Domain Echo amount — define provisional formula
"Domain Echo: faction stat change = +1 per degree of success above Partial (Success → +1; Overwhelming → +2). Applies to the most relevant faction stat per scene type (Mandate for political scenes, Influence for social, Military for combat). Capped at ±2 per scene. [PROVISIONAL — ED-071]"
Severity: P1

### PP-109 (P1): Domain Echo timing — resolve TTRPG vs Hybrid discrepancy
"In Hybrid mode (during Zoom In), Domain Echoes queue and fire at next Accounting. This is intentional: Zoom In is a personal intervention in a strategic situation; faction-level consequences propagate through the seasonal accounting cycle, not instantly. This differs from full-TTRPG Register Shift (immediate) by design. [Document as intentional, add rationale.]"
Severity: P1 (document the design decision; the inconsistency is intentional but undocumented)

### PP-110 (P1): Phase-Lock — Phase 6 sub-step clarification
"Phase 6 Step 1 Zoom In: after Step 1 damage applied, Zoom In fires. TTRPG scene runs. Zoom Out updates Str/NPC kills. Then Phase 6 Steps 2–6 resume using the updated state from Zoom Out. The general action at Step 4 is available unless the PC general is the Zoom In character (in which case their Step 4 is consumed by the Zoom In scene)."
Severity: P1

### PP-111 (P1): Mass combat time scale — personal combat duration
"One mass combat turn = one personal combat exchange. If the general's personal combat is unresolved after one exchange, it continues into the next mass combat turn's Phase 5. The mass combat unit commanded by the dueling general loses its general bonus (CR = 0 effective) each turn the general is in personal combat. Maximum: 5 exchanges before one combatant is forced to disengage or is incapacitated."
Severity: P1

### PP-112 (P2): Concurrent Zoom In provisional procedure
"If two or more PCs simultaneously trigger Zoom In conditions in different battles: resolve battles in faction-turn order (same as Accounting sequence). The first battle's Zoom In resolves fully (scene + Zoom Out) before the second begins. Other faction turns hold during both Zoom Ins."
Severity: P2 (provisional; marks as ED-072 for editorial)

### Editorial items for this audit
ED-071: Confirm Domain Echo amount formula (PP-108 provisional)
ED-072: Confirm concurrent Zoom In ordering (PP-112 provisional)  
ED-073: Non-battle Zoom In procedure (ST-K2-05 — full design decision needed)
ED-074: "Sufficient scope" definition for Register Shift
ED-075: PC faction embedding in BG layer (AUDIT-E-04 — design decision)
ED-076: P-01 co-movement propagation BG→TTRPG (AUDIT-E-01)
