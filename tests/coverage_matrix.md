# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

|-----|-----------|--------|
| Linear HP (End×6+16) | Reduces End dominance | Tested ✓ |
| Pool DR (Agi >4 → +1D) | Compresses Agi advantage | Tested ✓ |
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
| D1-D5 ratifiable package confirmed | HP, Pool DR, Crit, Mace, Triangle — all tested ✓ |

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
| Mode C (interaction chains) | PASS — 2 downstream flags (mass combat TC, pool DR × crit double reduction) |
| D1 MW Cap NERS | N✓ E✓ R~ S✓ |
| D2 Pool DR NERS | N✓ E~ R✓ S✓ |
| D3 Crit ≥4 NERS | N✓ E✓ R✓ S~ |
| D4 Mace +2D NERS | N~ E✗ R✓ S~ — recommend redesign (remove Blunt TN penalty) |
| D5 Wrong def +2 NERS | N~ E✓ R~ S✓ — too small to matter (5% HP/duel) |
| All-directions | Top-down ✓, Bottom-up ✓, Vertical ✓, Diagonal ✓ (init×triangle weak), Lateral ~ (pool DR combat-only), Horizontal ~ (Heavy arena 0 still fails) |

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
| Throughlines | 5 derived (TE-1..TE-5); 3 partial, 1 fail (TE-4 Smooth: combat-only DR) |
| 6 directions | TD/BU/L/V/D/H — 21 findings across all six |
| Severity | 2 P1 (stale Vitality formula in params/core; stale Concentration formula in params/contest), 8 P2, 11 P3 |
| Unifications | 9 proposed; U-1 (PP-716/PP-717 propagation) ready for no-call commit; U-2..U-7 need design call |
| Self-review | Three radical reframings applied: designer-theater (most findings player-invisible); productive-inconsistency (deviations as features); descriptive-vs-prescriptive (throughlines as observation not principle). Recovered finding count after self-review: ~5 substantive |
| File | tests/audit/engine_ners_2026-05-15.md |
