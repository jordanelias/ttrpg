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


_v25 section (2026-05-15) archived to `tests/coverage_matrix_archive.md` 2026-05-18 (Step 4.2 commit) per pre_commit_gate size discipline. Section covered: Geometry expansion + dynamic wide-wing pathing + sightline. Recover via git or archive file._

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

## Phase 7 (2026-05-18) — v18 mass-battle bare port (Mode G manifest)

| Field | Value |
|---|---|
| Scope | Infrastructure: Mode G module manifest for Phase 7 mass-battle port. Scope C2 narrow — canon §4.1 Step 1 + §4.10 sub-step 3. Steps 2–9 deferred. |
| Sim | tests/sim/v18-integration/module_manifest.md (this commit); subsequent port commits land in sim/provincial/{massbattle,units,tactic_cards,faction_action}.py + sim/mc_v18.py |
| Writeup | This manifest + designs/provincial/mass_battle_integration_v30.md §4 |
| Trials | None — manifest only. Battery (tests/sim/battery_v22.py) deferred to Step 5 of canon §4.1, not in C2. |
| Coverage | Phase 7 modules declared; tactic_cards.py stub remains BLOCKED on contamination audit per integration_plan_v18 §1.4. |
| Findings | Source-engine is sim_mb_06_v22.py (per canon §4.1), not m3_mass_battle.py. v22 dataclass extraction needs late-binding to avoid circular import (units.py ↔ massbattle.py constants). |
| Provisional assumptions | Bare-port flex acceptable per canon §4.1 PROVISIONAL clause (signatures may shift if statistical equivalence holds on Mirror Cmd 4v4 p>0.05). |
| Dependencies | designs/provincial/mass_battle_v30.md; designs/provincial/mass_battle_integration_v30.md; designs/provincial/military_layer_v30.md; designs/scene/derived_stats_v30.md; params/mass_combat.md; params/core.md. |
| Status | Manifest committed. Port commit follows. |
| Open | Verification ledger (per sim_gate) deferred — bare-port replicates v22 constants verbatim. Phase 8 strategic AI successor. |

## Phase 7 C2 (2026-05-18) — regression fix: Subunit.__eq__ recursion

| Field | Value |
|---|---|
| Scope | Surgical regression fix for c6ecb5b9 (Phase 7 C2 bare port). RecursionError in Subunit.__eq__ via target_atom cycle after assign_targets blocked every Conquest battle silently (mc_v18.faction_take_action's try/except Exception:pass masked the raise). |
| Sim | mc_v18.run_batch(10, base_seed=42) — direct invocation smoke against resolve_mass_battle(Crown Mil=5, Church Mil=4.5). |
| Writeup | tests/sim/v18-integration/module_manifest.md (status updates) + commit body. |
| Trials | 10 batch runs (n=10). Pre-fix: battles_mean=0 (silent fail). Post-fix: battles_mean=30.0. Direct invocation returns degree dict {'attacker_wins': True, 'degree': 'Success', 'attacker_size_pct': 0.89, 'defender_size_pct': 0.775}. |
| Coverage | sim/provincial/units.py: @dataclass(eq=False) on Subunit + Unit. Falls back to object identity __eq__/__hash__. Zero call-site changes. |
| Findings | Cycle source: assign_targets (massbattle.py L619/622/627/630) sets atom.target_atom as direct Subunit reference on both sides; A.target_atom→B and B.target_atom→A form a cycle. Literal trigger: list.remove of tuple-of-Unit at massbattle.py L1488/1494/1511/1537 (pursuit/rout tracking). Audited: zero `subunit == subunit` value-equality sites; existing set/dict keys already use id() (L749-750). |
| Provisional assumptions | Identity-eq does not change observable mass-battle outcomes — basis: canon §4.1 PROVISIONAL flex clause; target_atom set-by-reference throughout the engine, never compared by value. win_share spread Crown 40 / Varfell 50 / Church 10 (no pathological degenerate state) confirms _faction_to_unit MV-defaults are tolerable for C2; GAP-1 not escalated. |
| Dependencies | designs/provincial/mass_battle_integration_v30.md §4.1 PROVISIONAL clause; canon/02_canon_constraints.md §B GD-1. |
| Status | Verified end-to-end. Conquest path unblocked. |
| Open | Phase 7 follow-on splits into separate handoffs (Step 4.2 LETHALITY; Steps 4.3-4.6 flanking/ripple/tiebreakers; Steps 4.7-4.9 phase hooks/collision/cleanup; Step 10.1 domain_echo; Step 10.2 accounting + faction→unit richening — resolves GAP-1). |

## Phase 7 Step 4.2 (2026-05-18) — LETHALITY restoration + PP-233 formula correction

| Field | Value |
|---|---|
| Scope | Step 4.2 of canon §4.2 (designs/provincial/mass_battle_integration_v30.md §3.1, Audit Issue 1 highest severity). Restore LETHALITY_SCALE per §3.1 PROVISIONAL clause; calibration sweep at T3 mirror per §3.1 spec; commit calibrated value. Patch surface: 3 HP-damage sites in sim/provincial/massbattle.py (engagement, pursuit_damage, freed_attacker_damage). |
| Sim | mc_v18.run_batch(10, base_seed=42) smoke + multi-turn calibration sweep at L = [0.02, ..., 10.0] across N=40-60 mirror T3 Line vs Line runs. |
| Writeup | sim_verification_ledger.json (new); module_manifest.md (status updates); commit body (full diagnosis). |
| Trials | Sweep N=40-60 per LETHALITY value; robustness check N=40 across 5 seed batches (1000-5000); asymmetric matchup spot-check N=20 each. |
| Coverage | sim/provincial/massbattle.py — (1) PP-233 continuous net_successes formula replaces discrete DAMAGE_BY_DEGREE buckets at engagement L915-922 + freed_attacker L1475-1481. Pursuit already used PP-233 form; only LETHALITY wrap added. (2) LETHALITY_SCALE = 1.25 declared at L122. (3) DAMAGE_BY_DEGREE dict retained as narrative degree label for downstream logging. DR-as-reduction subtractor preserved (HP/H/DR architecture rationalization deferred). |
| Findings | **Root cause diagnosis deeper than §3.1**: §3.1 attributed lethality collapse to 20× HP inflation from v19 BLOCK_SIZE change. True diagnosis is TWO compounding defects: (a) HP inflation (per §3.1); (b) discrete DAMAGE_BY_DEGREE buckets cap damage at (1+power) regardless of net_successes, violating PP-233 canon "Damage dealt = successes × (1+Power)". PP-233 worked example: 4 successes × 4 = 16 damage; bucket model yields max 4. Bucket cap dominates (4× loss at typical net). Required formula rewrite, not just multiplier restoration. Spec §3.1 PROVISIONAL range 0.05-0.20 was a v17-era assumption; with PP-233 correction, LETHALITY=1.25 fine-tunes near baseline rather than gross compensation. |
| Calibration | Target: 14-16% per-turn casualties at T3 mirror Line vs Line P4/C4/D5/M6. Calibrated LETHALITY_SCALE=1.25: mean 14.48% / median 16.45% per-turn at N=60; battle-turns mean 1.9; winners 26A/32B/2draw (balanced). Robustness across 5 seed batches: 14.25-16.03% — all in band. Asymmetric matchups behave correctly (Power advantage → win share; Discipline edge → casualty asymmetry). mc_v18 smoke: battles_mean=40.1 (was 30.0 pre-Step-4.2). |
| Provisional assumptions | DR retained as damage-reduction subtractor — PP-233 originally folded DR into H (Health per Size = min(Disc,Cmd) + DR), but v22 HP model uses Size×BLOCK_SIZE and drops H entirely. Keeping DR-as-reduction preserves DR's defensive role; HP/H/DR architecture rationalization deferred to separate audit. |
| Dependencies | designs/provincial/mass_battle_integration_v30.md §3.1; params/mass_combat.md PP-233 Core Formula. |
| Status | Landed. Calibration in band. |
| Open | (1) Church win-share dropped 10% → 0% at L=1.25 vs b0185f05 baseline (n=10 too small, re-test in Step 4.2b). (2) T2 outperforms T3 at equal stats in spot-check — likely morale-erosion pathology (bigger units accumulate damage→morale faster); not introduced by Step 4.2, flagged for separate audit. (3) tests/sim/battery_v22.py existence unverified; battery validation gate (§3.2) deferred to Step 4.2b. (4) sim_verification_ledger.json created for v18-integration; future sim_gate calls must use this ledger. |

## Tier 0 Stub Infill (2026-05-19+) — designs/proposals/stub_infill_plan.md (6669592f)

One row per module. Trial detail in commit body + sim_verification_ledger.json.

| Module | Commit | Canon | Verification |
|---|---|---|---|
| `sim/territory/settlement.py` | (T0-1) | `settlement_layer_v30.md §1.2-1.3` | SettlementState/ProvinceState derivation per §1.3 multipliers; smoke on T1 Seat + T9 Cathedral; 5 ledger entries with canon-verified quoted_text |
| `sim/thread/coherence.py` | (T0-2) | `threadwork_v30.md Part 3` | Coherence 10-0 track with §3.3 band transitions; smoke run through Stable→Dissonant→Fragmented→Fractured→Severed→Crisis; floor/ceiling clamps verified; just_transitioned fires once; 9 ledger entries with bold-marker-preserving quoted_text |
| `sim/cross_scale/handoff_rules.py` | (T0-3) | `scale_transitions_v30.md §3` | 8 handoff rules dispatched; TS-banded coherence cost (3 thresholds 30/50/70 verified); §3.9 fieldwork pass-through; invalid transition returns valid=False; 3 ledger entries |
| `sim/cross_scale/zoom_in_out.py` | (T0-12) | `scale_transitions_v30.md §4` | zoom_in valid/invalid phase routing; mid-Phase-5 deferral verified; board-degree Ob modifier 4-way table; zoom_out queues Domain Echoes + PC incap + Contested Figure wound; 8 mandatory triggers enumerated; 2 ledger entries |
| `sim/cross_scale/domain_echo.py` | (T0-13) | `scale_transitions_v30.md §5` | §5.2 amount-by-degree (4 cases); §5.5 Accord Echo (governance/destab/transfer/violence + invalid); §5.6 Thread Echo (Dissolution/Mending/Gap/Lock/PublicChurch/PublicVarfell + invalid); 5 ledger entries; PP-329 1-per-faction-per-scene cap documented |
| `sim/__init__.py` | (T0-4) | (declarations) | docstring updated to reflect Tier 0 progress |
| `sim/peninsular/ms_track.py` | (T0-5) | `params/core.md §MS Baseline Decay (PP-255)` | apply_ms_baseline_decay (-1/year) + apply_ms_delta; floor 0 / ceiling 100 clamp verified (100× -5 → 0; 100× +5 → 100); 6 ledger entries; DRIFT vs accounting._ms_decay logged |
| `sim/peninsular/season.py` | (T0-6) | `campaign_architecture_v30.md` | run_season composes advance_season → optional action_callback → run_accounting; 5-season smoke with arc boundary at 1 and 5; MS decay fires at season 4 via existing accounting; DRIFT vs mc_v18 inline logged |
| `sim/provincial/treaty.py` | (T0-7 partial) | `faction_balance_convergence_v12c §4.5 + §4.7` | process_treaty_expirations with TREATY_LAPSE_RATE_DEFAULT=0.90 verified (5/5 lapse at high rate); register_treaty + get_active_treaties helpers; propose_treaty raises explicit canon-gate NotImplementedError pending Pass 2h; 2 ledger entries |
| `sim/world/insurgency_pipeline.py` | (T0-10) | `canon/02_canon_constraints.md §B GD-3` | GD-3 state machine: 2-season streak detection + formation event; L<3 promotion blocked; low-PT (avg=2) → extra-parliamentary RM variant; high-PT (avg=4) → parliamentary candidate; 6 ledger entries |
| `sim/world/npe.py` | (T0-11) | `designs/scene/investigation_systems_v30.md` SYSTEM 1 | Territory Social Ecology weights from prosperity/accord; NPC Genome 5-axis (stance/worldview/affiliation/compromise/volatility); Two-Tier Generation (archetype + d6 deviation, 5-6 flips axis); 10-NPC sample: 50% controlling-faction affiliation, 30% deviation 5+, arc-vector flagging works; 3 ledger entries |
| `sim/provincial/charter_liberties.py`, `sim/provincial/varfell_mandate_action.py`, `sim/autoload/npc_ai.py` | (T0-8/9/14 CANON-GATED) | (canon authoring required) | NOT IMPLEMENTED — Pass 2e (Hafenmark charter), Pass 2d (Varfell contamination audit), priority-stack contamination audit. Reclassified from Tier 0 to canon-gated bucket per stub_infill_plan §Canon-availability blockers. |
| `sim/autoload/game_state.py` (schema migration) | (post-Tier 0) | `stub_infill_plan Amendment 2026-05-19` | World gains 6 registries (practitioners/insurgencies/uncontrolled_streaks/npcs/npc_counter/treaties); 5 Tier 0 modules route through world stores with module-level fallback; 7-test integration smoke verifies cross-world isolation + module fallback + mc_v18 backward compat (battles_mean=31.8 at seed=42 N=5); serialize/restore unchanged (registries not yet in snapshot format) |
| `sim/territory/infrastructure.py` | (T1-1) | `settlement_layer_v30 §1.5-§1.7` | 4-axis Church infrastructure model. T9 seizure Ob smoke: Cathedral(-2)+Templar(-1)+Inquisitor(-1)+ChurchGov(-2)=-6 → capped to -4 per §1.5. Axis 1 mutual exclusion verified (Cathedral→Church removes Cathedral). Templar seed from Territory.templar preserved. 5 ledger entries. |
| `sim/territory/temperaments.py` | (T1-2) | `territory_temperaments_v30` | 17-territory temperament authoring (T1-T17 all assigned). 5-typology α/β coefficients per §1. Drift dynamics: strain_delta=3 on T1/T2 → drift=0.30 each, α shifts toward 0.9; strain_delta=10 accumulates to 1.0 clamp. Faction aggregates per §3 (Church α=0.2 strongly principled, Hafenmark α=0.55 mildly pragmatic). 4 ledger entries. |
| `sim/personal/conviction.py` | (T1-3a) | `conviction_track_v1.md §2-§3` (PP-718) | Per-Conviction Scar accumulation (Almud Order: 1→2→3 → crisis); Precedent independent (no cap collision); season cap suppresses same-season Thread re-Scar on same Conviction (mag=0); Certainty C5→mag+1, C0→mag-1 verified; 4 ledger entries |
| `sim/personal/beliefs.py` | (T1-3b) | `fieldwork_v30.md §5.5 + social_contest_v30.md §9.5` | add_belief/revise_belief/social_success; aligned win m=0→delta+1, m=4→delta=0 (cap); challenging win marks revision_pressure +1 and notifies conviction (pending_belief_revisions populated); cycle broken via late-import; 2 ledger entries |
| `sim/thread/operations.py` | (T1-4) | `threadwork_v30.md Part 2 + params/threadwork.md` | 7 operation entry points; Leap eligibility (TS<30 fail; TS=60 Ob=1); 9-operation smoke covers all degrees; FR Locking Object coh=-1 (FR surcharge only) verified; FR Locking Structural coh=-4 (-2 scale + -1 FR + -1 Partial); Mending Field coh=-2 always; POP recency table verified; coherence track erodes correctly across 8 ops to Crisis; 9 ledger entries |
| `sim/personal/combat.py` | (T1-5) | `combat_v30.md §1-§7 + PP-232` | Combat pool Agi×2+History+3 min 5 verified (Alice Agi=4 → pool=12); Heavy Blade short TN=6 verified; Light Blade vs Heavy armor +0 mod (net=0); Heavy Blunt vs Heavy armor +5 mod with PP-232 multiplicative STR×2×1.5=×3 (dmg=19 at net=2); Strike/Full Guard/Take a Breath/Dodge/Establish Distance resolve; Feint/Rescue/Disarm/Tie Up deferred Tier 2+; round-level resolution ordering per §4; 6 ledger entries |
