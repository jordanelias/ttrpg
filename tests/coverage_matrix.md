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

### M1-M5 (v17 modules; archived 2026-05-16)
M1 Church Settlement Infrastructure (commit `4f27949e`, 128 tests, 49 ledger entries), M2 CI Political Revision (`29b52428`, 78 tests, 26 ledger), M4 Unit State Management (`e33849c8`, 95 tests, 22 ledger), M3 Mass Battle Resolution (`dc9a71a0`, 63 tests, 23 ledger), M5 Settlement-Territory Aggregation (`4e1d00dd`, 95 tests, 28 ledger). **Detailed test surfaces archived in** `tests/coverage_matrix_archive_v17_modules.md`. Cumulative for M1-M5: 459 tests passing, 148 ledger entries. All five modules built canonical-fidelity (no fabricated mechanics; every constant cited to canonical source).

### M6 Faction Action Expansion (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 6 of 7; Crown Initiative + faction analogues + Excommunication + Absolution + RM Uprising + tactic card effects deferred from M3 |
| Module scope | Crown Initiative 3 modes (Royal Progress / Great Work / Coronation Renewal) per part10 §3.2-§3.4 with full pool/Ob/outcome tables including Mode III Excommunication-recovery (canon §6.4 Q-11 resolution); Church Excommunication per faction_canon §9 + Church sheet (L≥3 prereq, Ob=target_L leader / Ob 2 non-leader, 3-tier outcomes); Church Absolution per §8.2 with M6-declared Pool/Ob/cost; faction analogues (Council of Solmund Ob=floor(CI/30)+2, Charter of Liberties Pool=Inf+tokens Ob=4, Vaynard's Hall Pool=Mil+tribune_active Ob=3) per part10 §5.1-§5.3; RM Cultural Uprising of T9 per victory §3.5 Phase 2 with Phase 1 check (PT≤1 in ≥4 territories), MS≥25 prereq, Ob=clamped(ceil(CI/10)) + 3 modifiers; parametric tactic card effects (10 cards with constant pool modifiers) + 6 cards raising NotImplementedError for resolution-time hooks deferred to M7 |
| Test groups | T1 Royal Progress (15 checks) / T2 Great Work (10) / T3 Coronation Renewal (16) / T4 Excommunication (11) / T5 Absolution (8) / T6 Faction analogues (15) / T7 RM Uprising (18) / T8 Tactic card effects (16) / T9 Action registry (6) |
| Result | **125 PASSED, 0 FAILED** |
| Canonical sources verified | part10_crown_initiative_design §3.1-§3.7 + §5 + §6 + §7 (full 21.2k); faction_canon §8.2 + §9 + Church sheet (full 47.0k); victory_v30 §3.1 + §3.2 + §3.5 + §8 (full 57.2k); peninsular_strain (full 49.8k); mass_battle §B.4 faction-specific tactic cards (cached from M3); factions_personal_v30 + params/factions.md (fetched for sim_gate) |
| Ledger | 45 entries; per-mode citations to part10 §3.2-§3.4 outcome tables, Excommunication degree table to faction_canon Church sheet, RM Uprising mechanics to victory §3.5 Phase 2 |
| Provisional assumptions held | 5 (M6_ASSUMPTION_ONE..FIVE): Church Absolution Pool/Ob/cost declared by M6 (canon underspec), Standing as integer modifier (pending canonical track), parametric-vs-hook tactic card split (6 cards deferred to M7 with explicit dispatch reason), Weaver Thread pool as caller-supplied integer, 4-degree outcome semantics with {} default for canon-undefined degrees |
| Dependencies | M1 (settlement registry for Uprising Phase 1 territory enumeration), M2 (CI milestone queries for Coronation Renewal interactions), M3 (TACTIC_CARDS registry — M6 extends with parametric effects + hook-deferred set) |
| Files | tests/sim/v17-integration/m6_faction_actions.py + m6_faction_actions_tests.py + m6_sim_verification_ledger.json |
| M7 integration hooks needed | Stratagem 2-pass init inversion, Crusade Fervour check_route override, Inquisitor's Mark per-unit targeting, Calculated Retreat outcome override, Disappear outcome override, Ducal Call resolution-time state mutation — see TACTIC_CARDS_REQUIRING_HOOKS frozenset in m6_faction_actions.py |
| Next module | M7 Integration + Balance Sweep — all 6 module dependencies satisfied |

### M7 Integration + Balance Sweep (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 7 of 7 (final). Wires M1-M6 into mc_v17 runner + balance sweep with Wilson 95% CI verification |
| Module scope | mc_v17.py — extends mc_v15 baseline (Faction/Territory/World/Logger preserved) with M-module wiring: Faction.units (M4 UnitRoster), Faction.tactic_hand (M3 6-card hand 4 shared + 2 specific), World.settlements (M1 37-settlement registry), World.governance (M5 SettlementGovernance map), CI starting value from M2; ACTION_REGISTRY dispatch table (Govern/Muster/MilitaryConquest + Crown Initiative 3 modes + Excommunication + Absolution); ci_generation with M2 CI cap; settlement_event_pass + aggregate_to_territory using M5; minimal AI policy (30% faction-unique / 35% Conquest / 20% Muster / 15% Govern). m7_resolution_hooks.py — 6 hook-deferred tactic card implementations (Stratagem 2-pass init inversion, Crusade Fervour route suppression, Inquisitor's Mark -2 opponent pool, Calculated Retreat withdrawal, Disappear withdrawal+pursuit-block, Ducal Call pre-resolution Muster) via ResolutionContext + HookedBattleResult + resolve_battle_hooked pipeline. m7_balance_sweep.py — Wilson 95% CI computation + N=1000 sweep harness with band-overlap check |
| Test groups | T1 ResolutionContext (4) / T2 Stratagem hook (2) / T3 Calculated Retreat + Disappear (6) / T4 Ducal Call (2) / T5 Crusade Fervour route suppression (2) / T6 Inquisitor's Mark pool penalty (2) / T7 mc_v17 World construction (10) / T8 ACTION_REGISTRY dispatch (3) / T9 Settlement event loop (1) / T10 Smoke run 5 campaigns (1) / T11 Batch telemetry (3) |
| Result | **38 PASSED, 0 FAILED** |
| Balance sweep N=1000 result | **Crown 67.7% / Church 0.8% / Hafenmark 1.8% / Varfell 29.7%** (5.7s runtime, 175 campaigns/sec). Wilson 95% CIs: Crown [64.74, 70.53], Church [0.41, 1.57], Hafenmark [1.14, 2.83], Varfell [26.95, 32.61]. **`all_factions_in_band [20%, 30%] = False`** — only Varfell overlaps target band. battles_per_campaign=12.88, mean_season_ended=50.0. **Per integration_plan §10 R-03: the harness correctly DETECTS balance failure; tuning balance is downstream work, not in M7 scope.** |
| Canonical sources verified | integration_plan_v3 §5 Phase 2a-2d + §5 Phase 5 (full); mc_v15.py full reference architecture (full 46.0k cached); mass_battle_v30 §B.4 faction tactic cards (cached); factions_personal_v30 + params/factions.md (cached) |
| Ledger | 23 entries; resolution hook specs to §B.4 + canon Stratagem PP-690 / Crusade Fervour / Inquisitor's Mark / Calculated Retreat / Disappear / Ducal Call rows; Wilson CI to standard statistical reference; ACTION_REGISTRY architecture decisions to integration_plan §5 Phase 2 |
| Provisional assumptions held | 7 (M7_ASSUMPTION_ONE..SEVEN): ResolutionContext+HookedBattleResult architecture; ACTION_REGISTRY dispatch table; Inquisitor's Mark aggregate-count approximation (-2 opponent pool); Ducal Call Levy-default class; hook firing order (stratagem→ducal_call→crusade_fervour→inquisitors_mark→calculated_retreat→disappear); minimal AI probabilistic mix; standard_advance default tactic card selection |
| Dependencies | M1, M2, M3, M4, M5, M6 — ALL 6 dependencies satisfied |
| Files | tests/sim/v17-integration/mc_v17.py + m7_resolution_hooks.py + m7_integration_tests.py + m7_balance_sweep.py + m7_sim_verification_ledger.json |
| **v17 integration plan status** | **PHASE 2D COMPLETE per integration_plan §5: mass-battle + Workstream C surface wired; N=1000 Wilson CI verification executed; harness correctly flags balance band failure. Downstream tuning (rebalance AI / faction-action calibration) is post-M7 work surfaced to Jordan.** |
| Pass-3 findings | (1) Crown 67.7% dominance reflects AI policy more than mechanic balance — fixing AI before tuning mechanics. (2) Church 0.8% — Excommunication's Failure -1 L without recovery path creates a death spiral. (3) Hafenmark 1.8% — no faction-unique action wired (Charter of Liberties not in AI dispatch). (4) Royal Progress Ob formula floor(sum_accord/2) makes the action HARDER as Accord rises (canonical text says "easier when Accord is high" — possible canon defect, surface to Jordan). (5) Mean season=50 = no Crown territory-threshold victory before campaign end; all wins are tie-break-by-territory-held. |


## Phase 11 (2026-05-17) — Scene combat C4 (M1+M2+M3) empirical test

| Field | Value |
|---|---|
| Scope | Personal-scale combat. Test M1 (reach gate) + M2 (4-stance counter) + M3 (init preempt) atop Phase 10 baseline. |
| Sim | tests/sim/scripts/phase11_c4_v0.py |
| Writeup | tests/sim/phase11_c4_v0_2026-05-17.md |
| Trials | N=3000 per matchup; symmetric calibrations 49.9% and 48.5% (~50/50 ✓) |
| Coverage | Light/light (incl. Mighty-light F3 gap), light/heavy, light/polearm, M3 preempt, balanced-vs-Fast |
| Findings | M1 dominant; M2/M3 secondary. Dominance redistributed not eliminated: light-vs-light 94% Fast; light-vs-heavy 22% Fast (inverted). Polearm vs Fast 56/44 cleanest. F3 gap mostly persists. Balanced non-viable. |
| Provisional assumptions | M2 counter magnitudes empirical (−3D Decisive-v-Patience, degree-cap-1.0 Cautious-v-Pressure); M3 preempt heuristics (HP<0.6, init gap >= 2); STARTING_DISTANCE=2; closing-action 1-stam per band |
| Dependencies | Phase 10 baseline (params/combat.md ED-694 stamina; STR-strong bonus dice; 1/End Ob wound; Disarm) |
| Status | Implemented + run. Reframing 2 verdict deferred pending Phase 12 mass-battle archetype test. |
| Open | Tune M1 softer vs accept Reframing 2 vs add C2 hybrid — decision after Phase 12. |


## Phase 12 (2026-05-17) — Mass-battle archetype test (Reframing 2 verification)

| Field | Value |
|---|---|
| Scope | Mass-battle scale. Test whether Heavy/Strong archetypes dominate at mass scale at comparable or greater magnitude to scene-scale Agi dominance. Cross-scale balance check for Reframing 2. |
| Sim | tests/sim/scripts/phase12_mass_archetype_v0.py |
| Writeup | tests/sim/phase12_mass_archetype_v0_2026-05-17.md |
| Trials | N=2000 per matchup; Levy vs Levy calibration 46.7%/48.5% cond |
| Coverage | Light/Heavy archetype matchups; weapon-class penetration; Power-tier diffs; HeavyBlunt anti-armor |
| Findings | Mass-battle dominance is CATEGORICAL (100/0) when weapon-class fails to penetrate armor-class, not statistical. Light vs Heavy: 0/100. Heavy vs Heavy: 100% draw (canonical stalemate without tactical levers). HeavyBlunt (Knights Templar): 100/0 vs everything — anti-armor universal. Reframing 2 supported with asymmetric magnitudes. |
| Provisional assumptions | Default pool split ½/½; H baseline +2 per worked example; max_rounds=40; draw threshold ratio 1.2x; tactic cards / flanking / Command / terrain UNMODELED |
| Dependencies | params/mass_combat.md Core Formula PP-233; DR Table PP-104; Weapon Effectiveness table |
| Status | Implemented + run. Reframing 2 ratified. Two audit flags surfaced: HeavyBlunt universal anti-armor; Heavy-vs-Heavy stalemate needs tactical levers to produce interesting resolution. |
| Open | Verify Heavy-vs-Heavy resolves interestingly via tactic cards / flanking / Command in M3-engine sim (deferred). HeavyBlunt audit deferred. |


## Phase 13 (2026-05-17) — Intermediating layer test (Reframing 2 floor analysis)

| Field | Value |
|---|---|
| Scope | Test three intermediating layer candidates (Layer A Posture, Layer B Advantage Bar, Layer C Stamina-primary) atop Phase 10 baseline. Question: which layer compresses within-class Agi dominance from 99% baseline to 60-70% target? |
| Sim | tests/sim/scripts/phase13_layers.py |
| Writeup | tests/sim/phase13_layers_2026-05-17.md |
| Trials | N=2000 per matchup per layer |
| Coverage | Calibration matchups; within-class Agi gap; End-investment; F3 gap; cross-class via heavy; balanced build |
| Findings | All three layers structurally compress within-class dominance. Layer A inverts (36% Fast — STR/End rebalanced); Layer B floors via binomial exchange (83% — mathematical bound); Layer C modest compression (88% — preserves current dynamics). None hit 60-70% target cleanly at first-pass tuning; structural mechanisms validated. Calibration draw rates high for Layers A and B. |
| Provisional assumptions | All Phase 13 magnitudes (POSTURE_NET_PER_STEP, POSITION_PER_NET, HP_DAMAGE_THRESHOLD etc.) are first-pass; tuning sensitive; smart-AI strike-when-vulnerable applied but more sophisticated AI would shift results |
| Dependencies | Phase 10 baseline; planning_v0.md root cause identification |
| Status | Three layer candidates implemented and tested. Reading split: A) tuning works; B) layer + companion mechanism; C) layer insufficient at current pool magnitudes. Decision: Jordan to choose layer or reject. |
| Open | F4 calibration draws need tuning resolution. F5 cross-class still requires reach gate (M1). F6 balanced builds non-viable across all layers. Reading C poses deeper question about pool magnitudes themselves. |
