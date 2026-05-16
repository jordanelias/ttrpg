# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

|-----|-----------|--------|
| Linear HP (End×6+16) | Reduces End dominance | Tested ✓ |
| Pool Softcap (Agi >4 → +1D) | Compresses Agi advantage | Tested ✓ |
| 1H commit bonus (+2D) | Specialist viability | Tested ✓ |
| Wrong def +2 dmg | Simplified triangle | Tested ✓ |
| **Combined result** | **None: PASS (63%). Heavy: PASS at 75% (Strong 75%)** | **Iteration complete** |

### Iterations 5-6 (2026-05-14)
| Finding | Status |
|---------|--------|
| Crit rate 60% at canonical >= 3 | P1 — threshold needs raising to >= 4 or >= 5 |
| Mace-only commit bonus (+2D for TN > 7.0, 1H) | Tested ✓ — best specialist fix |
| HP End×5+20 | Tested ✓ — Tough drops to 62% unarmoured |
| **Best config unarmoured PASS (62%)** | **Iteration 6 final** |

### v23 Complete Audit (2026-05-14)
| Phase | Tests | Status |
|-------|-------|--------|
| 1. Half-point TN | T1.1-T1.3 | 3 PASS |
| 2. Weapon-armour | T2.1-T2.4 | 1 PASS, 3 PARTIAL |
| 3. Multi-attack | T3.1-T3.3 | 2 PASS, 1 PARTIAL |
| 4. Defense triangle | T4.1-T4.4 | 4 FAIL → simplified |
| 5. Distance | T5.1-T5.3 | 1 PASS, 2 PARTIAL |
| 6. 2H/Longsword | T6.1-T6.3 | 2 PARTIAL, 1 FAIL |
| 7. Equal-budget | T7.1-T7.2 | 2 PASS (arena 3+5 unarmoured), 4 FAIL |
| 8. Crits | T8.1-T8.3 | 2 PASS, 1 P1 |
| 9. Integration | T9.1 | 1 PASS |
| **TOTAL** | **26 tests** | **12 PASS, 8 PARTIAL, 10 FAIL** |
| **Open decisions** | **12** | **D1-D12 in audit** |

### D6/D8 Tests (v24, 2026-05-15)
| Decision | Status |
|----------|--------|
| D6 Shield +3D/+4D | DEFERRED — amplifies Tough dominance, needs loadout system design |
| D8 Bash table +4→+3 | REJECTED — barely changes results (75→74%), gap is STR×3 not table |
| D1-D5 ratifiable package confirmed | HP, Pool Softcap, Crit, Mace, Triangle — all tested ✓ |

### All-Directions Audit (v25, 2026-05-15)
| Finding | Status |
|---------|--------|
| End ROI +34-48pp per point (P1) | Wound snowball root cause. D15 proposed (wound cap −2D) |
| Dagger overperformance (P1) | D14 short −2D vs Med/Heavy fixes it (79%→65%) ✓ |
| Arming sword fails N without shield (P2) | D6 deferred to loadout |
| Liechtenauer Vor/Nach | +7-14pp init advantage ✓ |
| Harnischfechten attack selection | Correct (Cut→Thrust at Medium) ✓ |

### P0: Stamina Quantization Cliff (v25, 2026-05-15)
| Finding | Root Cause | Fix |
|---------|-----------|-----|
| End +42.5pp/point | Stamina 24→25 cliff (4.0→4.17 rounds at cost 6) | Stam=20+End |
| HP contribution only +10.5pp | HP is not the dominant factor | D1 (End×5+20) helps but secondary |
| Wound cap has no effect | Fights end by yield, not wounds | D15 unnecessary |

### PP-717 NERS Audit (v26, 2026-05-15)
| Assessment | Result |
|------------|--------|
| Mode A (formula validation) | PASS — no boundary issues |
| Mode C (interaction chains) | PASS — 2 downstream flags (mass combat TC, Pool Softcap × crit double reduction) |
| D1 MW Cap NERS | N✓ E✓ R~ S✓ |
| D2 Pool Softcap NERS | N✓ E~ R✓ S✓ |
| D3 Crit ≥4 NERS | N✓ E✓ R✓ S~ |
| D4 Mace +2D NERS | N~ E✗ R✓ S~ — recommend redesign (remove Blunt TN penalty) |
| D5 Wrong def +2 NERS | N~ E✓ R~ S✓ — too small to matter (5% HP/duel) |
| All-directions | Top-down ✓, Bottom-up ✓, Vertical ✓, Diagonal ✓ (init×triangle weak), Lateral ~ (Pool Softcap combat-only), Horizontal ~ (Heavy arena 0 still fails) |

## v25 (2026-05-15) — Geometry expansion + dynamic wide-wing pathing + sightline

**Architecture:** 41×42 connected battlefield (was 25×25); 19×11 formation area within 41×21 per-unit grid; 11-col side buffers; 5-row front/back buffers. Dynamic Horseshoe wing pathing relative to enemy widest column. Sightline mechanic (135° arc, 15-cell range) gating defender rotation. Cell-level adjacency damage zones. Sticky Phase 2 transitions via Subunit.wing_phase_2_cells.

**Status:** in-progress calibration; battery 3/11 in-band at LATERAL_BUFFER=3. Battles 5–7 ticks (target 18+ across 3+ turns).

**Known issues for next iteration:**
- ANGLE_DMG_MULT and FLANKED_BONUS constants present but not wired into damage formula; pool-averaging via ANGLE_DEF_MOD dilutes single-cell RED zones
- 17-row vertical gap (formation to formation) may need tightening for current speeds
- Arrowhead tip mechanic underperforms (H2 Arrowhead vs Line = 25% A; H9 Line vs Arrowhead = 75% A → both indicate tip isn't delivering proportional damage)

**File:** tests/sim/sim_mb_06_v25.py

**Status update v25 (post-commit):** sim file landed (this commit). 18+ constants ledger entries reference §A.3b. Calibration work continues — battery 3/11 in-band, known issues documented above.

### Fiore TN System (v27, 2026-05-15)
| Finding | Result |
|---------|--------|
| Fiore TN: base 7.0 all, 2H -0.5 only | Weapon matchups excellent with distance |
| Dagger vs AS: 76% → 31% | **Fixed** — dagger penalized at Mid, must close to Short |
| Mace vs LS Heavy: 60% | Mace wins at Heavy via positional advantage ✓ |
| T5.1 directionality | PASS — 74%/83% at optimal |
| T7.1 None: Tough 92% | FAIL — Mid-start favors Mid-reach weapons |
| Root cause | Distance + stamina system needs engagement mechanic, not fixed Mid start |
| **Status** | Fiore TN validated for weapon identity. Build matrix needs distance engagement. |

### Fiore TN + Engagement (v27 continued)
| Test | Result |
|------|--------|
| Agi engagement + Fiore TN | Tough 84% (None), 90% (Heavy) — improved but not passing |
| Brute (STR6 mace) vs Tough | 19-40% — HP outlasts damage at all tiers |
| Root cause | Fights end by stamina (4 rounds), not damage. HP >> DPR × rounds. |
| Sim limitation | Simplified chassis lacks feint/taunt/initiative declaration — full BW tactical layer would create non-attrition win paths |
| **Fiore TN verdict** | Correct for weapon identity and matchups. Build matrix needs full duel system, not more formula patches. |


### v9 Full Chassis + Fiore TN (v27 final)
| Finding | Result |
|---------|--------|
| Fiore TN in v9 chassis | Tough 94% at canonical stamina — stamina timer dominates |
| Stamina cliff | stam 24→4rds, stam 25→5rds — ±1 stam flips outcome |
| Arena 0 (cost 5) | Fast 69%, Tough 53%, spread 31pp — best balance |
| **Proposal: stunt cost +1→+0** | Preserves stamina, eliminates quantization cliff |

### Videogame Baseline — BEST RESULT (v27)
| Test | Result |
|------|--------|
| None, arena 0 | Fast 68%, spread 30pp |
| **Heavy, arena 0** | **Tough 63%, spread 25pp — PASS** |
| Mace vs AS | 45%/73% crossover ✓ |
| Dagger vs AS | 46%/45% (fixed from 76%) ✓ |
| Mace vs LS Heavy | 52% — both effective vs plate ✓ |
| **Config** | **Fiore TN (base 7.0, 2H -0.5) + D1-D3 + v9 chassis + distance + arena 0** |
| Remaining | None at 68% (3pp over). Fiore TN + stunt cost not yet ratified to params. |

### Fiore TN Ratified (v27)
PP-717 Fiore: base 7.0, 2H -0.5. Distance Short/Mid/Long. Action cost 5. Three-axis system superseded.

### All-Directions NERS Audit (v27)
| Layer | Status |
|-------|--------|
| 5 throughlines | All PASS NERS |
| 4 meta-throughlines | All PASS NERS (3 minor flags) |
| 6 directions | 5 PASS, 1 PARTIAL (Vertical: STR uncapped) |
| Internal consistency | 5/5 PASS |
| External consistency | 4 flags: stamina (End×5 vs 15+End×2), taunt canonicalization, 2H stacking, mass combat untested |
| P1 actions | Stamina reconciliation, taunt canonicalization |

### Combat Integration Session A (2026-05-15)
Phase machine + Strike/Guard/Breath. Canonical values, full ledger. Smoke test passes.

### Session A NERS Audit
All 5 throughlines pass NERS. All 3 meta-throughlines pass. STR mult ambiguity flagged.

### Engine NERS All-Directions Audit (2026-05-15)
| Layer | Status |
|-------|--------|
| Scope | First engine-design NERS at architectural level (dice engine + derived stats + Ob/Pool channels) |
| Throughlines | 5 derived (TE-1..TE-5); 3 partial, 1 fail (TE-4 Smooth: combat-only Pool Softcap) |
| 6 directions | TD/BU/L/V/D/H — 21 findings across all six |
| Severity | 2 P1 (stale Vitality formula in params/core; stale Concentration formula in params/contest), 8 P2, 11 P3 |
| Unifications | 9 proposed; U-1 (PP-716/PP-717 propagation) ready for no-call commit; U-2..U-7 need design call |
| Self-review | Three radical reframings applied: designer-theater (most findings player-invisible); productive-inconsistency (deviations as features); descriptive-vs-prescriptive (throughlines as observation not principle). Recovered finding count after self-review: ~5 substantive |
| File | tests/audit/engine_ners_2026-05-15.md |

### Phase 4 Agi-Dominance Re-check (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Decision A (ED-828) — PP-717 D2 Pool Softcap rejected at canon |
| Scope | Verify whether Agi-6 vs Agi-3 dominance manifests at current canon |
| Mechanics | Universal pool (no DR), MW cap 3 (PP-717 D1), Crit threshold ≥4 (PP-717 D3) |
| Fast vs Strong | 95.6% conditional win — DOMINANT |
| Build-investment ROI Agi 3→7 | +46.6pp conditional win at top — steep, never inverting |
| Tough vs Strong (End 6 vs 4) | 99.6% conditional — End-dominance also persists |
| Fast+Tough vs Strong | 100% — compound dominance unrecoverable |
| Conclusion | Agi-dominance reopens at current canon. PP-717 D2 was addressing real problem. Recommend Jordan reconsider. |
| Sim limitations | Strike-only; 50/50 split; single weapon/armour; lower-bound estimate |
| Files | tests/sim/phase4_agi_dominance_2026-05-15.py + phase4_results.md + sim_verification_ledger.json |

### v17 Full-Workstream Integration (2026-05-15 — in progress)
| Test | Result |
|------|--------|
| Trigger | Phase 1a finding: v16 structurally incomplete (Church 0%, Varfell 0%) |
| Scope | Gap analysis of mc_v16.py against all canonical design docs |
| Finding | 27 mechanics missing across 5 workstreams (7 Critical, 11 High, 7 Medium, 2 Low) |
| Root cause | Church dies because settlement infrastructure (Religious Buildings, Templar Stations) not modeled; CI generation depends on PT which RM destroys; Mass Battle absent |
| Module manifest | 7 modules, ~7 sessions, critical path M1→M2→M6→M7 |
| Status | Module manifest and gap analysis committed; Module 1 (Church Settlement Infrastructure) next |
| Files | tests/sim/v17-integration/gap_analysis.md + module_manifest.md |

### Phase 5 Continuous Engine Prototype (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Jordan 2026-05-15 — accepted Path 3 (full continuous engine) |
| Sim A: Distribution equivalence | EQUIVALENT — max deviation 0.029 in mean, 0.022 in std at pool 5-17 |
| Sim B: Phase 4 re-run on continuous | Matches Phase 4 discrete within sampling noise |
| Sim C: Discrete vs Continuous head-to-head (N=5000) | 97.8% (discrete) vs 97.5% (continuous) — Δ -0.3pp |
| Build ROI curve | Identical shape — Agi 7 reaches 99.2% in continuous, 99.5% in discrete |
| Key finding | **Continuous engine works but does NOT solve Agi-dominance** — doubling is the structural driver, not the dice mechanism |
| Implication | Adopting continuous engine: yes (independently valuable for fractional modifiers + degree continuity). Solving dominance: requires separate decision (drop doubling, pool cap, or re-ratify softcap) |
| Files | tests/sim/phase5_continuous_engine_2026-05-15.py + phase5_results.md + phase5_sim_verification_ledger.json |

### Phase 6 Dominance-Solver Comparison (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Phase 5 showed continuous engine alone doesn't solve dominance |
| Candidates | (A) status quo, (B) drop doubling, (C) cap 14, (D) cap 12, (E) PP-717 softcap |
| Fast vs Strong | A: 97.8% / B: 90.2% / C: 89.1% / D: 72.3% / E: 92.6% — **ALL DOMINANT** |
| Build ROI spread Agi 4→7 | +20pp / +36pp / +8pp / +0pp / +17pp |
| End-dominance (Tough vs Strong) | 99.6-99.9% across ALL formulas — formula-independent |
| KEY FINDING | **Pool formula does NOT solve dominance** — structural drivers are wound spiral, HP/stamina window, crit cascade |
| Next path | Phase 7 with action triangle (Feint/Defend) OR wound-spiral lever |
| Implication for canon | Pool/doubling decision becomes design-feel choice, not balance choice |
| Files | tests/sim/phase6_dominance_solvers_2026-05-15.py + phase6_results.md + phase6_sim_verification_ledger.json |

### Phase 7 Action Triangle Test (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Phase 6 showed pool formula doesn't solve dominance; test action triangle (PP-294 Feint) |
| Fast vs Strong, Strike-only baseline | 96.7% Fast cond (matches Phase 6) |
| Fast vs Strong, Underdog (Strong) actively Feints | **34.9% Fast cond — Strong wins 65%** |
| Tough vs Strong, Smart play both sides | 6.8% Tough cond (down from 82% Strike-only) |
| KEY FINDING | **Action triangle (PP-294 Feint) is the load-bearing balance lever** — not the pool formula |
| Interpretation | When disadvantaged side actively Feints, dominance INVERTS. End-dominance collapses with tactical play. |
| Implication | Pool formula and Decision A stand. Doubling is design-feel. Combat IS balanced via tactics. |
| Caveat | Smart AI under-tuned; numbers indicate direction but not point estimates |
| Files | tests/sim/phase7_action_triangle_2026-05-15.py + phase7_results.md + phase7_sim_verification_ledger.json |

### Workstream Meta-Audit (2026-05-15)
| Aspect | Result |
|--------|--------|
| Subject | 10-commit chain (02e2dd7f..5de02b07) from engine NERS through Combat Balance Note |
| Method | Six-direction audit + NERS rubric, objective neutral, initial pass |
| NERS scorecard | N=~, E=✓, R=~, S=✓ — two partials (scope/validation), two passes (execution/integration) |
| Findings | 0 P1, 4 P2, 5 P3 — all P2/P3 are Robustness concerns; zero correctness defects |
| What stands | F1/F2/F4/F5/F12/F13 propagation fixes; DR→Softcap; continuous engine validation; hook compliance |
| At-risk | Balance Note canonization timing; Decision E scope-validation mismatch; F13/Decision E bundling; Phase 7 End-dominance possibly artifact |
| Open | Phase 8 (better Smart AI); cross-system audit; End-dominance follow-up; SHA refresh |
| File | tests/audit/workstream_meta_audit_2026-05-15.md |

### Phase 8 Smart AI v2 (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | WS-H-3, WS-H-4 (meta-audit 2026-05-15) — Phase 7 Smart AI under-tuned |
| Smart v2 AI fixes | Take Breath threshold ≤8, Full Guard last-stand only, Feint alternation per PP-294 |
| Fast vs Strong, Smart v2 symmetric | **100% Fast — pool advantage structurally dominant** |
| Tough vs Strong, Smart v2 symmetric | 63.7% Tough — moderate End-dominance (Phase 7 7.5% was artifact) |
| Calibration: Agi 3 vs Agi 3 symmetric | 51.2% — sim balanced |
| KEY FINDING | Phase 7 "34.9% Feint inverts dominance" was partly stamina-management artifact; pool advantage at 17D vs 11D is structurally dominant in skilled-vs-skilled play |
| Combat Balance Note status | Needs revision — 34.9% claim misleading without stamina-asymmetry caveat |
| Files | tests/sim/phase8_smart_ai_v2_2026-05-15.{py,md} + phase8_sim_verification_ledger.json |

### Phase 10 STR + Stamina Reform (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | Jordan design questions: "stamina from endurance should be doing a lot more work; strength isn't having enough impact" |
| Methodology corrections | (a) TN vs Ob conflation in prior wound-penalty sims (Ob is net-success threshold, not per-die TN shift); (b) Disarm AI threshold bug fix (opp_weapon_mod >= 3 not >= 4); (c) **stamina-formula error in Phase 4-9: sim used 15 + End*2, canon (ED-694) is End*5 with partial Take Breath restore and +1 stam cost per wound** |
| Stamina correction impact | Every End-investing matchup shifts 4-9pp from prior sim baseline. Fast vs Titan: 81.8% → 72.6% before any reform applied. Phase 8 ED-838 End-dominance magnitude (63.7%) understated; direction unchanged, magnitude larger |
| STR bonus dice (proposed reform) | floor(STR/3) on Strike/Disarm offense pool: STR 4→+1, STR 7→+2, STR 10→+3. Pending Jordan ratification |
| Best config: canonical stam + STR-strong | Fast vs Titan 67.5/32.5 — meaningful upset rate. Fast vs Tough-heavy 77/23. Calibration symmetric matchups 47-51% |
| Persistent finding | Pool dominance survives all reforms. Fast vs Titan 70/30 at full reform stack. Further levers (pool cap, static defense, smaller pools) untested |
| STR + light blade gap | Mighty (Agi 3, STR 7, light) sits at 98.5% loss to Fast under STR-strong. Light weapon str_mult=1.0 + 2pp hit-rate gain cannot overcome 3-die pool gap. Open design question |
| Sim limitations | Tie Up, Establish Distance, Reach mechanics still unmodeled; symmetric AI assumption persists; Phase 7 PP-294 inversions not retested under reform; cross-system audit (CC-1) in backlog |
| Open canonical questions | (1) Update Combat Balance Note with stamina-correction erratum; (2) ratify STR bonus dice mechanic; (3) accept pool dominance as designed or push further; (4) design light-weapon STR archetype or accept gap |
| Files | tests/sim/phase10_str_stam_reform_2026-05-16.md + tests/sim/scripts/phase10_str_stam_reform.py |

### M1 Church Settlement Infrastructure (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest (74b7f29) — Module 1 of 7 in strategic-sim integration plan; canonical primitives for four-axis Church infrastructure |
| Module scope | Settlement dataclass, 37-settlement registry from settlement_layer §2.1, Seizure Ob formula (10 − PT − infra, floor 1, −4/settlement cap), SW-weighted Piety Yield, Mass Seizure declaration P((CI−60)/40)^3.3, Parish Order yields, Pastoral Assumption eligibility, Ascendant PT drift, Unification phase tracking |
| Test groups | T1 registry integrity (24 checks) / T2 starting state (38) / T3 Seizure Ob boundaries (9) / T4 PT generation (12) / T5 CI generation (8) / T6 Inquisitor/Parish/Pastoral (9) / T7 Mass Seizure mechanics (7) / T8 Unification (7) / T9 PT drift (10) |
| Result | **128 PASSED, 0 FAILED** |
| Canonical sources verified | settlement_layer_v30 §1.5 §1.6 §1.7 §2.1 §2.2 (full read), ci_political_v30 §1 §2.1 §2.2 (full read), victory_v30 §3.2 (full read), mc_v15.py PT_MAP + ADJACENCY (full read), campaign_architecture_v30 (full read), params/bg/victory.md (full read) |
| Ledger | 49 entries citing each constant to canonical source + section + quoted text |
| Provisional assumptions held | 6 (ASSUMPTION_ONE..ASSUMPTION_SIX corresponding to GAP-A..GAP-F): registry source-of-truth, starting infrastructure seeding, playable territory count, Cathedral adjacency stacking rules, PT drift granularity, Warden Cooperation gate. All documented in ledger.provisional_assumptions; held for Jordan ratification before integration sim runs. |
| Known canonical conflicts | (A) settlement_layer_v30 §2.1 vs valoria_geography_v30.yaml — different settlement-registry schemas; M1 sourced from §2.1; geography YAML needs editorial migration. (B) Compliance shows canon/editorial_ledger.yaml auto-fixable but cc052aa landed clean (likely cache/eventual-consistency artifact). |
| Files | tests/sim/v17-integration/m1_church_infrastructure.py + m1_church_infrastructure_tests.py + m1_sim_verification_ledger.json |
| Next module | M2 CI Political Revision (depends M1) — CI milestones 55/65 verification, revised Mass Seizure cross-territory, ±5/season CI cap audit |

### M2 CI Political Revision (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest (74b7f29) — Module 2 of 7; CI cap mechanics, milestone effects, political legitimacy modifiers |
| Module scope | Seasonal CI cap (±5/season total, ±3 from Domain Actions), CI milestones 28/40/55/65/80/100 with effect queries, Bonus Dice floor(CI/20) and Obstacle Modifier floor(CI/30), Hafenmark suppress (-1 at L≥4), Unification simultaneous-seizure target-list generator (Chapel+ ∩ Church Prominent), Accord-on-Seizure-success formula |
| Test groups | T1 constants (11 checks) / T2 seasonal cap (5) / T3 DA sub-cap (5) / T4 mixed sources (6) / T5 hard bounds (3) / T6 Bonus Dice + Obstacle Modifier (15) / T7 milestone effects (17) / T8 Hafenmark + Unification targets (10) / T9 Accord (6) |
| Result | **78 PASSED, 0 FAILED** |
| Canonical sources verified | ci_political_v30 §2 + §3 + §4.1 + §7.1 (full read), victory_v30 §3.2 (full from M1 session), faction_layer_v30 §5 (full read for default slot cost), mc_v15 mass_seizure_check (Accord formula source) |
| Ledger | 26 entries; cross-references M1 module constants for Religious-Building / Prominence / PLAYABLE_TERRITORIES |
| Provisional assumptions held | 5 (ASSUMPTION_ONE..ASSUMPTION_FIVE): source classification by caller, sub-cap precedence ordering, threshold-inclusive milestone semantics, action-classification responsibility, Unification target composition |
| Dependencies | Module 1 (settlement registry, has_any_church_building, PLAYABLE_TERRITORIES, SPIRITUAL_WEIGHT) |
| Files | tests/sim/v17-integration/m2_ci_political_revision.py + m2_ci_political_revision_tests.py + m2_sim_verification_ledger.json |
| Next module | M4 Unit State Management (foundational, no deps) or M5 Settlement-Territory Aggregation (depends M1); per manifest M3 depends on M4 |
