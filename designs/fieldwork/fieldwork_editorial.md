# VALORIA — FIELDWORK SYSTEM v1.1 — §12 Open Items and Editorial Flags
## Parent: designs/fieldwork/fieldwork_design_v1.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: ALL

## §12 OPEN ITEMS AND EDITORIAL FLAGS

### New editorial items

| ID | Description | Priority |
|----|-------------|----------|
| ED-NEW-01 | POI catalog per territory. Requires cross-reference with geography_design.md and calamity_radiation.md. Each territory needs 2-6 authored POIs across depth levels with conditional availability gates. | P2 |
| ED-NEW-02 | Named NPC starting Dispositions. Requires cross-reference with existing NPC roster (Vaynard, Baralta, Cardinals, Torben, Elske, Klapp, Almud, Maret Uln, Edeyja). Each named NPC needs faction-indexed starting Disposition values. | P2 |
| ED-NEW-03 | Survey action stat assignment confirmed: Influence. Monitor in simulation — if Survey dominates Govern, consider Ob adjustment. | P2 |
| ED-NEW-04 | Exposure ↔ Church Attention Pool interaction. §6.5 caps at +1/character/season and +2/territory/season from fieldwork. **CONFIRMED SAFE** (PP-581 simulation: fieldwork contributes ~11% of max TC acceleration over 4 seasons — bounded to insignificance relative to primary TC drivers). | P3 |
| ED-NEW-05 | Negotiate vs Contest boundary defined (§5.7). Confirm this does not create edge cases where players attempt to Negotiate situations that structurally require Contest. | P2 |
| ED-NEW-06 | Godot POI node architecture (§10.1). Requires validation against Valoria-game repo Godot project structure. | P3 |
| ED-NEW-07 | Evidence Track persistence. Confirm tracking overhead is manageable across 10+ session campaigns. | P3 |
| ED-NEW-08 | Disposition decay rate (§5.2: −1/season above +3). Requires simulation to confirm pacing. | P2 |
| ED-NEW-09 | Thread-Read co-movement effects (§4.5). Confirmed: uses threadwork_redesign_v25.md §3.2 co-movement table directly. No separate fieldwork co-movement table. | P3 |
| ED-NEW-10 | Breach encounter (Depth 5) + Coherence stacking. **CONFIRMED PROPORTIONAL** (PP-581: each step requires deliberate player decision; no forced spiral. A Coherence ≤ 2 practitioner entering a Breach risks Crisis from Breach −1 + Thread op −1 = 0. This is intentional — the Breach is the rendering's edge). | P3 |
| ED-NEW-11 | Pool formula ×2 — **RESOLVED** by PP-615. params_core.md now confirms (Agility × 2) as canonical. PP-247 note was stale. Fieldwork Ob calibration is correct. | RESOLVED |
| ED-NEW-12 | Sincerity Gate (§5.3) uses Spirit. Confirm Spirit is not already overloaded as an attribute (currently: Resolve = Spirit; no other mechanical role). | P3 |
| ED-NEW-13 | Desperate Trail (§4.4): 3 consecutive failures threshold triggers TN 8 + doubled Exposure + GM complication. Confirm TN 8 does not make recovery impossible for low-pool investigators (4D at TN 8: P(≥1) ≈ 60%, still viable). Confirm Partial +2 progress compensates for increased difficulty. | P2 |
| ED-NEW-14 | Audit finding D-SIM-5 resolved: §4.1 now defines Finding reliability from resolved investigations. Verify Finding + Contest interaction in simulation. | P3 |
| ED-NEW-15 | POP Coherence −1 additional: resolved as subject to per-op cap (not exempt). Confirm this in params_threadwork.md — currently ambiguous. Propagate ruling. | P2 |

### Items resolved by PP-580 extended threadwork simulation (2026-04-13)

| Item | Resolution |
|------|------------|
| KN-01/02 | Knot-mediated remote Thread-Read: §2.6. +1 Knot strain per use. Detection → Disposition −3. |
| DIS-01/02 | Non-sensitive partner Dissonance: §2.7. Spirit check vs Dissonance Factor. Field team rotation. |
| TC-01/02/03/04 | Threadcut being social fieldwork: §2.8. Testimonial tag. P-08 bridged by being's translation. Evidence Track = player-level knowledge. Counter-investigation possible. |
| MA-02/03 | Mending arcs as investigation: §2.4. Severity reduction = evidence. Multi-season campaign pacing. |
| CW-01 | Community Weaving detectable: §2.4 table (Weaving row covers Community Weaving). |

### Items resolved by PP-579 ontological correction (2026-04-13)

| Item | Resolution |
|------|------------|
| PP-578 TW-11 | FALSE CLAIM STRUCK. "Lock/Dissolution produce 0 Evidence progress" was ontologically incorrect. All Thread operations may advance Evidence Track when consequences reveal investigation-relevant information. §2.4 rewritten. |
| PP-578 TW hierarchy | Replaced with contextual yield model. Investigation yield depends on what is targeted and why, not on operation type. GM determines yield. |
| Domain Echo integration | §2.5 added. Resolved Findings fire Domain Echo per stage11 §11.5. NPC arc cascades follow. |
| NPC Disposition on investigation | §2.5 added. Disposition −2 if NPC learns they were investigated; +1 if NPC wanted truth found. |
| Forensic applications | §2.4 added. Dissolution (Gap topology + concealer signature), Lock (resistance pattern diagnostics), POP (paradox window dual-state). |
| Scale/distance/breadth | §2.4 added. Knot-mediated remote Thread-Read. Collective Thread-Read at Structural scale. Temporal reach via POP recency. |

### Items resolved by PP-578 threadwork transition simulation (2026-04-13)

| Item | Resolution |
|------|------------|
| TW-01 | Leap vulnerability timing: window closes when Thread-Read resolves. §2.4. |
| TW-10 | FR ops suppress fieldwork: one Thread op per action, Thread-Read and FR mutually exclusive. §2.4. |
| TW-12 | Wounds → +1 Ob to Thread ops requiring Leap (not −1D pool). §2.4. |
| TW-05 | POP Coherence −1 additional IS subject to per-op cap (not exempt like FR surcharge). Distinct cost profiles. |

### Items resolved by PP-577 transition simulation (2026-04-13)

| Item | Resolution |
|------|------------|
| F-TRANS-01 | Fieldwork → Combat handoff added (§2.3). Exposure → ambusher advantage. |
| F-TRANS-04 | Evidence not consumed by Contest citation — stated explicitly (§2.3). |
| F-TRANS-06 | Mass battle suspends fieldwork — suspension rule added (§2.3). |
| F-TRANS-07 | Thread-Read in Phase 4 = intelligence, not offensive. Co-movement fires. (§2.3). |
| F-TRANS-10 | Contest Appraise → +1 Evidence Track progress (Testimonial). (§2.3). |
| F-TRANS-12 | Post-battle investigation = 1 fieldwork scene. Battle ≠ fieldwork time. (§2.3). |
| F-TRANS-05 | Post-Contest Disposition shift: winner +1, loser −1 with adjudicator. (§2.3). |
| F-TRANS-09 | Combat Exposure codified: quiet +1, conspicuous +2, public +3. (§2.3). |
| F-TRANS-11 | Combined Findings: +1D per additional Finding in Contest, max +2D. (§2.3). |

### Items resolved by PP-576 audit (2026-04-13)

| Item | Resolution |
|------|------------|
| D-2 (Let It Ride) | Added §2.2. Failed fieldwork action on specific target cannot be reattempted same scene. |
| D-9 (Overwhelming floor) | Added §2.2. Fieldwork uses core engine degree table (net ≥ 2×Ob AND ≥ 3). |
| D-3 (Wounds) | Added §2.2. Physical wounds apply to exertion-based fieldwork only. Rattled applies to social. |
| D-5 (Multi-character) | Added §3.2. Leader + max 2 assistants. Assistant success = +1 net to leader. Assistant fail = +1 Exposure. |
| D-6 (Cross-territory) | Added §4.1. One track per investigation regardless of territory. Exposure per territory. |
| D-7 (Desperate Trail persistence) | Added §4.4. Desperate Trail persists through Compromised. Only clears on Success or season change. |
| D-1 (Perception gates) | Added §2.2. Gates are hard — capacity, not skill. No Beginner's Luck for perception gates. |
| D-4 (Non-sensitive +5) | Added §5.6. Non-sensitive Bonded: no decay, +1D, but no Knot formation or P-12 contagion. |
| D-SIM-5 (Finding reliability) | Added §4.1. Resolved investigation produces Finding with strongest tag. |
| B-2 (Cover plateau) | Fixed §6.1. Extended threshold table: Cover 10-11 = 7/9/11; Cover 12+ = 8/10/12. |
| C-1 (Faction support TTRPG) | Fixed §6.4. TTRPG: requires Diplomacy Ob 2 or existing alliance. |
| E (Inspiration spend) | Added §2.2. Spend 1 Inspiration before rolling to reduce Ob by 1 (min 1). |
| E (Gift/Bribe) | Added §5.2. Gift/Bribe improves starting Disposition +1, no roll, once per NPC per season. |

### Simulation debt

| ID | Description |
|----|-------------|
| SIM-DEBT-FW-01 | **RESOLVED** (PP-583). Ob calibration across Depth 1-5 at 5 pool sizes ± hostile/foreign modifiers. Calibration sound: 5D handles D1, 9D handles D1-2, 13D handles D1-3, 17D handles D1-4, 24D challenges at D5. |
| SIM-DEBT-FW-02 | **RESOLVED** (PP-576 partial, PP-583 complete). 5-threshold investigation completes in 3-5 scenes for high-pool (15-19D). Low-pool (9D): 4-6 scenes at D1-2. Pacing confirmed. |
| SIM-DEBT-FW-03 | **RESOLVED** (PP-583). Neutral→Bonded: ~6-8 actions across 3-4 seasons (with failures and maintenance at +3). Sincerity Gate adds ~37% failure on instrumental Connect. Meaningful investment confirmed. |
| SIM-DEBT-FW-04 | **RESOLVED** (PP-581). AP feedback: fieldwork contributes ~11% of max TC acceleration. +1/char/season +2/territory/season cap is sufficient. |
| SIM-DEBT-FW-05 | **RESOLVED** (PP-583). Survey and Govern occupy different niches. Govern dominates mid-proximity (reliable Prosperity). Survey dominates high-proximity (safe northern territories). Neither dominates the other. |
| SIM-DEBT-FW-06 | **RESOLVED** (PP-583). Cover 3: detected in 3 scenes. Cover 9: full season before detection. Cover 12+: near-immune to casual detection, threatened only by combat+Thread stacking. Appropriate differentiation. |
| SIM-DEBT-FW-07 | **RESOLVED** (PP-577). Transition simulation. All 6 directions functional. |
| SIM-DEBT-FW-08 | **RESOLVED** (PP-578/PP-579). Threadwork × fieldwork. All ops advance Evidence contextually. |
| SIM-DEBT-FW-09 | **RESOLVED** (PP-579). NPC arc stress tests. 7 Domain Echo cascades tested. |
| SIM-DEBT-FW-10 | **RESOLVED** (PP-580). Extended threadwork (Knots, Community Weaving, threadcut beings, Mending, Dissonance). |

### Propagation status

| File | Change | Status |
|------|--------|--------|
| references/canonical_sources.yaml | Fieldwork system entry | **DONE** (PP-575) |
| references/params_fieldwork.md | Mechanical values extraction | **DONE** (PP-583) |
| designs/systems/clock_registry.md | Exposure, Evidence Track, Disposition, Cover tracks | **DONE** (PP-575) |
| references/propagation_map.md | Cross-references to combat, contest, threadwork, BG, geography | PENDING |
| references/params_board_game.md | Survey action in Standard Action Ob table | PENDING |
| references/params_core.md | Attribute usage table includes fieldwork roles | PENDING |
| compilation/v0.14/stage11_scale_transitions.md | 9th handoff rule (Fieldwork ↔ all systems) | PENDING |
| tests/coverage_matrix.md | SIM-DEBT-FW-01 through FW-10 (all RESOLVED) | PENDING |
