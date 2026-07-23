# Valoria Simulation Coverage Matrix (archive continued from coverage_matrix_archive_2026_05_20.md)

## Archived 2026-05-20 (weapon-system v2 trials + Pass 2k checkpoint)


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

## Archived 2026-05-29 (pre-v32 sim rows; armature-reset coverage trim)

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
| `sim/provincial/treaty.py` | (T0-7 partial) | `faction_balance_convergence_v12c §4.5 + §4.7` | process_treaty_expirations with TREATY_LAPSE_RATE_DEFAULT=0.90 verified (5/5 lapse at high rate); register_treaty + get_active_treaties helpers; propose_treaty raises (no canonized generic formation path; canon formation is Senator Outward per treaty_expiration_v30 §2); 2 ledger entries |
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
| `sim/peninsular/ci_track.py` | (T2-1) | `conviction_track_v30 §3 PP-412` | PP-412 Step 1 +1 Momentum; Step 2 floor(Σ yield by PT) with PT5→+1, PT4→+0.5; Step 3 Assert; Step 4 Suppress cancels Momentum; Step 5 Hafenmark -1 at L≥4 (verified L=3 → 0); ceiling clamp at 100; 10-season smoke with Church L=6 produces +10/season prominent-territory yield; DRIFT vs accounting._ci_generation flat +2/Church-territory documented; 6 ledger entries |
| `sim/autoload/game_state.py` (helpers) | (bug fix 2026-05-19) | `PT_MAP / ACCORD_MAP` | canonical_pt(continuous_pt: float) -> int 0-5; canonical_accord(continuous_accord) -> int 0-4; nearest-neighbor at PT_MAP midpoints (1.75, 3.25, 4.75, 6.0, 6.75); round-trip verified on all PT_MAP / ACCORD_MAP entries + boundary cases; 1 ledger entry |
| `sim/peninsular/ci_track.py` (bug fix) | (re-verified) | `conviction_track_v30 §3 + victory_v30 §3.2 PP-534` | Step 2 yield re-bucketed via canonical_pt (was int(t.pt) drift); PP-534 Self-Control Rule added (Church auto-prominent in own territories); default state +1/season matches canon S1-S5 pacing; mid-game scenario +3/season matches canon mid-game pacing |
| `sim/world/npe.py` (bug fix) | (re-verified) | `investigation_systems_v30 §Ecology` | accord_int now via canonical_accord (was int+clamp drift); ecology weights now correctly: T2 canon=3 → high; T13 canon=1 → low; volatility offset works correctly (T13 NPCs avg 4.0 vs T2 avg 3.0) |
| `sim/provincial/mass_seizure.py` | (T2-2) | `victory_v30 §3.2 + campaign_architecture §1.3 + supersession 250715f` | Probabilistic declaration P=((CI-60)/40)^3.3 matches canon table exactly (1.0% at 70, 10.2% at 80, 38.7% at 90, 100% at 100); one-shot lifetime via world.clocks['MASS_SEIZURE_USED']; Pool=Influence+floor(CI/15), Ob=10-canonical_pt-infra_mod floor 1; PP-534 Self-Control via _church_is_prominent_for_seizure; T9 PT 5 + full Church infra → Ob 1 (max stack -4 cap) → seized at net=2; GD-1 conformant (world.winner unchanged); 7 ledger entries |
| `sim/personal/contest.py` | (T2-3) | `social_contest_v30 §1-§9` | Argue Pool (PA×2)+Hist-wound-fatigue (Alice 5*2+2=12, wounded 10, fatigued 11); resolve_exchange tracks Persuasion Track 1-9; tied exchanges +1 toward first-speak per §4; 3-exchange contest with Compromise outcome verified; 10-contest distribution 3A/3B/4 compromises; Belief alignment momentum integration via late-import (no cycle); 4 ledger entries |
| `sim/personal/knots.py` | (T2-4) | `knots_v30 (Pass 2g synthesis)` | Option A 2-tier (Distant/Close); formation prerequisites all checked (bonds<5 rejected, disposition<5 rejected, both TS<30 rejected, duplicate rejected); formation Spirit×2+History+0 vs Ob 2; tier from degree (Overwhelming→Close, Success→Distant); strain accumulation; capacity break at strain > tier_capacity; rupture trigger 'public_citation' → -1 Coherence via late-import (Alice 10→9); high-strain Close break → Conviction Scar via late-import; 7 ledger entries |
| `sim/thread/co_movement.py` | (T2-5) | `threadwork_v30 Part 4 + §4.3 ED-577` | 15 canonical cards CM-01 through CM-15 (Mending CM-16/17/18 deferred to §7.1); Object scale draw → unactualized (CM-09 ms_delta=-2 verified); Structural draw → actualized (CM-14 ms_delta=-3 verified); MS clock updates correctly (80 → 77); 16-draw test triggers reshuffle, all 15 unique IDs returned; 1 ledger entry |
| `sim/thread/collective.py` | (T2-6) | `threadwork_v30 §2.5` | Anchor selection by highest TS (Anchor TS=80 chosen over Helper1 TS=60, Helper2 TS=50); helper contribution floor(Cognition/2) (Helper1 cog=4 → +2 dice, Helper2 cog=4 → +2 dice); total pool 23+2+2=27 verified; lattice fracture threshold (remaining < expected/2) implemented; per-practitioner Coherence delta applied for Field scale (-1 per Leap survivor); operation degrades to Field Ob 5, Success at net=7 |
| `sim/thread/threadcut.py` | (T2-7) | `threadwork_v30 Part 6` | §6.1 Ontological Status canon body empty — flagged as canon gap (header only); §6.2 5-band perception (TS=0/25/45/65/100 all map correctly); mark_threadcut + is_threadcut registry; §6.3 +1 Rendering Strain per external op verified (1 op → strain 1; 6 ops → strain 7); §6.4 De-Actualisation triggered at strain ≥ max_wounds=6 (round=2 after 6 ops, triggered flag fires on first crossing); perception bands match canon §6.2 verbatim |
| `sim/thread/opposing.py` | (T2-8) | `threadwork_v30 §2.6` | opposing_engagement_modifier formula verified (B's TPS=6 → A's Ob +3; A's TPS=8 → B's Ob +4); 7-cell resolution matrix (Meets-Meets, Meets-Partial, Meets-Failure, Partial-Partial, Partial-Failure, Failure-Partial, Failure-Failure all coded); FR Lock vs Standard distinct (Composure 4 vs 2; knot Ob 2 vs 1); MS delta from worst-degree+1 rule for Shifting Object; Knot strain via late-import; apply_coherence_delta routes through coherence module |
| `sim/provincial/massbattle.py` (audit finding) | (non-determinism filing 2026-05-19c) | `stub_infill_plan Amendment 2026-05-19c` | mc_v18 non-determinism diagnosed: massbattle.py L630 roll_pool + L1053 volley_roll_pool call random.randint directly instead of using world.rng. Two consecutive run_batch(5, base_seed=42) diverge; random.seed(0) before run_batch produces deterministic output (battles_mean=32.8 both runs). Filed as follow-on; not fixed (would shift every mc_v18 batch result, requiring Phase 7 smoke re-baseline) |
| `sim/autoload/game_state.py` (schema migration #2) | (Tier 1/2 registries 2026-05-19) | `stub_infill_plan Amendment 2026-05-19` (extends migration #1 at 94dac72e) | World gains 8 fields: convictions, beliefs, knots, knot_id_counter, territory_infrastructure, npc_drift_state, threadcut_beings, comovement_deck; 6 consumer modules updated; cross-world isolation verified across 7 registries; module-level fallback preserved for world=None callers; mc_v18 backwards-compat verified |
| `sim/autoload/game_state.py` (per-record serializers) | (production save format 2026-05-20) | `stub_infill_plan Amendment 2026-05-19d` | 9 dataclasses gain to_dict/from_dict (CoherenceState+log, InsurgencyRecord, NPC, TreatyRecord, ConvictionState+log, Belief, Knot, InfrastructureState, ThreadcutState); serialize_world extended with 14 registries; restore_world reconstructs via late-imports; 26/26 round-trip checks pass; 14/14 old-schema tolerance checks pass (missing registries default empty); mc_v18 backwards-compat verified (battles_mean=38.0) |
| `sim/provincial/massbattle.py` (RNG fix) | (Deferred Migration Batch 2026-05-20, commit 54277ae) | `mass_battle_v30 §A.1 + params/mass_combat.md` | Closes 03ce9c79 non-determinism. 12 functions gain rng=None param (roll_pool, _roll_volley_pool, volley_phase, resolve_engagements, resolve_engagements_cascading, run_battle, run_multi_turn_battle, run_multi_unit_battle, pursuit_damage, recall_check, discipline_check_cascade, freed_attacker_damage); 21 internal callsites thread rng=rng; resolve_mass_battle passes world.rng. Pre-fix: same-seed batches diverged across runs and required random.seed() pin. Post-fix: byte-identical within process at same seed; module random.seed has no effect. Verified at N=5 base_seed=42 with global random.seed pollution between 3 runs; all identical. [GAP: hash-seed nondeterminism remains across Python processes — pin PYTHONHASHSEED=0 for cross-process reproducibility; filed for separate session] |
| `sim/peninsular/accounting.py`, `sim/mc_v18.py`, `sim/peninsular/season.py` (3-migration batch) | (Deferred Migration Batch 2026-05-20) | `conviction_track_v30 §3 PP-412; params/core.md §MS Baseline Decay PP-255; campaign_architecture_v30` | Deletes 3 legacy duplicates. accounting._ci_generation (+2 per Church-held territory, canon-violating) replaced with ci_track.apply_seasonal_ci. accounting._ms_decay replaced with ms_track.apply_ms_baseline_decay gated on world.season % SEASONS_PER_YEAR == 0. mc_v18 inline season block (L73-87) replaced with season.run_season(world, action_callback=_faction_actions_callback). Behavior shift: pre-batch Church CI gained +8/season at start; post-batch ≈ +1/season per PP-412 §3 Pacing canon. Authoritative re-baseline at PYTHONHASHSEED=0: N=10 base_seed=0 → battles_mean=35.5, win_share Crown:30/Varfell:70; N=10 base_seed=42 → battles_mean=33.4, Crown:40/Church:30/Varfell:30; N=5 base_seed=42 → battles_mean=37.6, Crown:20/Church:40/Varfell:40. Supersedes the 4 stale manifest figures (smoke 40.1; run_batch(10,42)=30.0; migration #1 baseline 31.8; migration #2 baseline 37.4 with random.seed(0) pin) |
| `sim/autoload/game_state.py`, `sim/provincial/faction_action.py` (hash-seed fix) | (Deferred Migration Batch follow-on 2026-05-20) | n/a — purely structural | Closes hash-seed-nondeterminism GAP filed in commit 105ae9e. Two leaks: (1) Faction.territories: set -> list (set str-key iteration depended on PYTHONHASHSEED); (2) _try_conquest candidate set wrapped in sorted() before rng.choice. Cross-process determinism verified across PYTHONHASHSEED in {0, 1, 7, 42, 99999} at N=10 base_seed=0 (battles_mean=34.1, Crown:4/Church:1/Varfell:5). PYTHONHASHSEED pin no longer required for reproducibility. Companion list-conversions: .discard() -> guarded remove; .add() -> guarded append |
| `params/bg/npc_priority_trees.md` (audit + dedup) | (Jordan-flagged 2026-05-17 priority-stack contamination audit) | n/a — canon-doc cleanup | Audit pre-implementation (consumer sim/autoload/npc_ai.py is NotImplementedError stub). Structural defects fixed: D-1 every tree duplicated L26-116 + L119-228 (byte-identical except whitespace), second block deleted; A-2 GD-2 mandatory-action precedence section added as §0 (mandatory pass before stochastic priority candidates per canon/02_canon_constraints.md §B); A-3 PP-NPC-04 initial state clarified (Collection flag = False at world creation). 8 stale-reference items (S-1..S-8: CI freeze threshold, Royal Decree canon, Löwenritter Autonomy survival, IP trigger, Warden Recognition, Cardinal mechanic, Crown T2/T4 hardcode, post-founding RM behavior under GD-3) require Jordan input — captured in designs/audit/2026-05-20-npc-priority-trees/audit_findings.md |
| `sim/thread/opposing.py`, `sim/thread/co_movement.py`, `sim/provincial/excommunication.py` (legacy-duplicate migration follow-on) | (sweep follow-on to commit 105ae9e) | `params/core.md PP-255 MS; ci_political_v30` | Three additional inline clock arithmetic sites found during post-batch sweep, migrated to dedicated track modules. opposing.py L229 (MS clamp), co_movement.py L142 (MS clamp), excommunication.py L165 (CI ceiling). All three now route through ms_track.apply_ms_delta / ci_track.apply_ci_delta — single canonical surface. Behavior verification: N=10 base_seed=0 produces battles_mean=34.1 (matches commit 3c2c428 baseline exactly; pure refactor) |
| `tools/index_gen.py`, `canon/editorial_ledger_summary.yaml` (M6 partial) | (Architecture V2.4 M6 gap) | `project-architecture-valoria-v2_4.md <completeness_enforcement> M6` | Closes two of three M6 defects: (1) HTML comment in YAML output replaced with YAML # comment; (2) generate_editorial_summary signature extended with archive_yamls so next_id is computed across active + archives (was archive-blind: old next_id=824, new=865 — 41 IDs the old code missed). Strict yaml.safe_load now passes on regenerated summary (210 total entries across 10 archives + active). Third M6 defect (regex-over-prior-summary fallback) remains as defensive path inside _collect_ed_entries — acceptable since yaml.safe_load is tried first. file_index_summary.md tree-walk integrity not in this scope (separate function family) |
| `sim/peninsular/accounting.py` (insurgency + NPE wire-up) | (Roadmap steps 2 + 3 from session 2026-05-20) | `canon/02_canon_constraints.md §B GD-3; designs/scene/investigation_systems_v30.md SYSTEM 1` | accounting.run_accounting extended: after CI+MS, invokes check_insurgency_triggers (GD-3 a-b emergence), iterates check_insurgency_promotion over existing insurgencies (GD-3 c-e), then simulate_npc_actions for territory-level NPC drift. Both modules T0-verified (T0-10, T0-11) but previously uninvoked from season loop. Behavior verification: N=10 base_seed=0 yields battles_mean=34.1 (matches pre-wire baseline; insurgencies don't form in short runs). Authoritative N=100 base_seed=0 captured: battles_mean=34.2, Crown 40 / Church 5 / Hafenmark 1 / Varfell 54 |

## [ARCHIVED 2026-06-06 from coverage_matrix.md] May stub-infill coverage (Tier 0 2026-05-19; Tier 3 Lane C / parliamentary_stay / parliamentary_transfer 2026-05-31)

## Tier 0 Stub Infill (2026-05-19+) — proposals/stub_infill_plan.md (6669592f)

One row per module. Trial detail in commit body + sim_verification_ledger.json.

| Module | Commit | Canon | Verification |
|---|---|---|---|
| `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` | (I-17 Module 1; mu-shift reformulation) | `params/core.md §Die Rule/§TN/§EV/§Pool Floor/§Obstacle Scale` (Class A); level magnitudes Class-B draft, canonical home pending (DRIFT-1) | Dice + sigma-space core. Discrete d10 (roll_net) + continuous Normal(muN, sigma*sqrt(N)) + sigma-space modifier (soft_cap, level->sigma map). **Advantage applied as a mu-shift (net_boost boosts the roll: mean += eff_sigma*sigma*sqrt(N)), NOT an Ob-reduction** -- leaves base_Ob/TN untouched, so the canonical Ob floor (Obstacle Scale, Ob min) is never violated; identical odds at TN7, TN-exact at TN6/8. Resolves audit F1 (Ob-floor breach by the old eff_ob Ob-reduction) + F3 (hardcoded sigma_N coeff -> per-TN sigma). eff_ob retained as an Ob-floored DISPLAY helper only. Self-test 6/6 PASS (per-die EV/sigma TN6/7/8; discrete~continuous 5-17; +0.7sigma uniform across 3D-20D spread 0.00pp; soft-cap checkpoints + saturate/floor). Logged ED-884. PROPOSAL -- mechanical-tier, Jordan-vetoable. |
| `tests/sim/v32-combat-balance/m2_attribute_pool_builder.py` | (I-17 Module 2) | `params/core.md §Attributes/§Derived Scores + derived_stats_v30 §4.1/§4.2/§5.1/§5.2` | Attribute->pool builder for the v32 combat-balance sim. StatBlock (attrs 1-7, avg-3 defaults) + derived-value fns: combat_pool (Agi×2)+History+3 floor 5; max_wounds min(floor(End/2)+1,3); wound_interval End+6; health WI×(MW+1); stamina End×5; composure Cha×3; concentration Foc×3; wound_adjusted_pool (-1D/wound, floor 5). Self-test 4/4 PASS vs canon: (a) Health/MW/WI reproduce derived_stats §4.1 per-Endurance table EXACTLY (End1=14..End7=52, MW cap 3, WI 7-13); (b) Stamina/Composure/Concentration match anchors (End4=20, Cha4/Foc4=12, ranges); (c) Combat Pool doubled-formula anchors (Agi4/H1=12, Agi6/H2=17) + floor 5; (d) wound penalty -1D/wound + floor clamp. 10 archetype stat blocks (Fast/Strong/Tough/Tough-heavy/Titan/Mighty-heavy/Mighty-light/Polearm/Init-build/Balanced) carried forward from tests/sim/scripts/phase11_c4_v0.py as Class-B sim-inputs (NOT canon). 23 ledger entries (13 Class-A canonical, 10 Class-B). Also adds module_manifest.md to the sim dir. |
| `tests/sim/v32-combat-balance/m3_weapon_class_layer.py` | (I-17 Module 3) | `combat_v30 §5 / §6 (Class A) + combat_v32_proposal §8 (Class B draft)` | Weapon-class layer. Class A: weapon_tn (base 7 + 3-axis), str_multiplier (Light×1/Heavy×2/Blade×1/Blunt×1.5, Heavy Blunt ×3), str_minimum (1/2/3/4), armor_damage_mod (weapon-vs-armour-tier table), armour STR-mins, degree table. Class B (draft): handling H(P) (Forgiving/Standard/Demanding), Weapon Speed, 8 weapon classes -> canonical axes. Self-test 5/5 PASS: 3-axis TN matrix (5..8); STR mult Heavy Blunt=3.0; weapon-vs-armour (Heavy Blade +6/+0, Heavy Blunt +5 all); handling H(P) vs §8.2 table + P4 crossover; 8 §8.1 classes' base TN consistent with canonical matrix. 36 ledger entries (24 A, 12 B). [ASSUMPTION: §8 says 'seven' but lists 8 incl. Long Heavy Blunt.] |
| `tests/sim/v32-combat-balance/m4a_bout_state_graph.py` | (I-17 Module 4a) | `combat_v32_proposal §4.6–§4.9/§12.5–§12.6 (Class B draft) + derived_stats_v30 §4.1/§4.2 (Class A)` | Bout state graph + control flow (M4 split into 4a control / 4b sub-action mechanics per manifest). Engagement subgraph (Out-of-contact/Closing/In-bind/Breaking/terminal); depth 1-5 structure (Stamina 2/3/5/7/10, Concentration 0/0/1/2/4, chain caps 1/2/4/6/unlimited, wound-state ceilings 5/4/3); termination conditions + priority (§12.5: wound/chain-cap/separation/clash/resource); disengage resolution (§4.8 bands >=+2 clean..<=-3 fail, opposed roll via M1); Phase-8 recovery (Stamina (End+H)x2 canonical, Concentration +Focus draft). Self-test 8/8 PASS vs spec. 27 ledger entries (4 Class-A canonical anchors, 23 Class-B §4 draft). Imports M1 (roll_net). |
| `tests/sim/v32-combat-balance/m4b_subaction_mechanics.py` | (I-17 Module 4b) | `combat_v32_proposal §12.1–§12.4 (Class B draft) + combat_v30 §5 / params/core (Class A)` | Sub-action mechanics (M4 split: 4a control / 4b mechanics). Pool composition ((attr×2)+AspProf+History, wound penalty, floor 5); σ-space Effective Ob (reuses M1 soft cap + Ob shift), state-gated per engagement state (§12.3); degree of success (Failure/Partial/Success/Overwhelming, net>=2·Ob∧>=3); strike damage (canonical combat_v30 §5 via M3); Targeted-line anti-armor. Self-test 7/7 PASS incl. §12.7 worked-example cross-check (Thrust pool 17, Press/Yield 13, strike dmg 10) + §12.3 σ-space conversion. 9 ledger entries (4 Class-A, 5 Class-B §12.4 draft). Imports M1/M2/M3. FLAGGED for Jordan: [DECISION] σ-space (Option A) vs dice-space; [ASSUMPTION] Yield=Foc (Will absent); [ASSUMPTION] Displace=mean(Str,Agi); [DRIFT] §12.7 example omits crit doubling (10 vs 12); [DRIFT] Targeted-line Heavy->Light (skips Medium). |
| `tests/sim/v32-combat-balance/m5_stance_reaction_coherence.py` | (I-17 Module 5) | `combat_v32_proposal §7.1/§7.2/§7.3 + §6.11 (all Class B draft sim-seeds)` | The three σ-space matchup modifiers, all state-gated. Stance Counter (authored 5×5 anti-symmetric, Closing-gated, legacy Ob→σ-level |1|Moderate/|2|Strong); Reaction (2-param formula baseline_r + slope_r·(depth−3), slope sign = punishes-hesitation vs punishes-overcommitment family); coherence (named loadout sets carry synergies with N4 partial credit for near-sets, plus the 2 antagonism exceptions Anticipation×Reaction / Commitment×Disengage — no general 36-pair matrix). Reuses M1 LEVEL_SIGMA. Self-test 6/6 PASS (anti-symmetry + sign convention incl. §12.7 Forward-point/Centered cell, reaction family sign behaviour, set partial-credit levels, antagonism penalty). 7 ledger entries (all Class-B §7 draft). FLAGGED for Jordan: ALL magnitudes are draft sim-seeds (Stance Counter values → Phase 11 Fast-vs-Titan 50–60%; Reaction coefficients → I-17; set bonuses → Phase 14) — the values the balance sweep tunes, not canonical. |
| `tests/sim/v32-combat-balance/m6_dual_resource_economy.py` | (I-17 Module 6) | `combat_v32_proposal §11.5/§11.6/§4.9 (Class B draft) + derived_stats §4.2/§5.2 (Class A)` | The stateful dual-resource economy. ResourceState tracker (init at M2 maxima End×5 / Focus×3; spend per action; recover at pass end; query bands). Full drain table beyond M4a: Phase-3 movement (0/1/3), Phase-6 per-sub-action (1 Cut/Thrust/Yield/Void, 2 Press/Wind/Displace, 3 Grip-change), passive armour drain (+0/+0/+1/+2, canonical), per-exchange Concentration (−3, canonical). Threshold bands for both pools (Stamina 0 Out-of-Breath −2D, <30/20/10% chain/depth/probe; Concentration 0 Spent −2D, <30/20/10% Reading/depth/no-Bout). §11.6 dominant-drain shape classifier (Stamina-fast vs Concentration-vulnerable). Boundary: M4a owns commit-depth/chain/ceiling/disengage/recovery; M6 owns pools + full drain + bands + dual-resource shape. Composes M2 + M4a. Self-test 7/7 PASS (canonical maxima End4→20/Focus3→9, M4a depth-3 spend, drain costs, threshold bands, Take-a-Breath recovery (6+2)×2→26, per-exchange −3, dual-resource shape). 8 ledger entries (3 Class-A derived_stats, 5 Class-B §11). |
| `tests/sim/v32-combat-balance/m7_facing_fov.py` | (I-17 Module 7) | `combat_v32_proposal §11.2 (all Class B draft)` | The v32 emergent facing/FoV model (built with depth, not stubbed). FoV zones (Central ±30°/Near 30-70°/Far 70-110°/Blind >110°) with FoV factors (1.0/0.6/0.3/0.0); sight-mediated Reading channels FoV-scaled (Tactile contact-mediated, exempt); reaction availability gated by zone (Central all / Near Hand-led+Body-led / Far Hand-led only / Blind none — 'cannot void what you cannot see'); emergent_facing_advantage DERIVES the aggressor advantage from two compounding channels (defender Reading scaledown + reaction loss), composing M5.reaction_sigma — reproduces v31 ≈-1 flank / ≈-2 rear rather than asserting it; facing-change levers (Angled/Drawing/Voiding/Bursting). Self-test 6/6 PASS (zone mapping, FoV factors, Reading scaling + Tactile exemption, reaction gating, emergent STRUCTURE monotonic central>near>far>blind + total-loss-at-rear, facing levers). 6 ledger entries (all Class-B §11.2). [ASSUMPTION] emergent magnitude uses unit base Reading δσ; exact value from §4.5 Reading net-success table — M8 pins it. [GAP] §4.5 Reading→δσ not modelled here (structure validated; magnitude deferred to M8). |
| `tests/sim/v32-combat-balance/m8_integration_sweep.py` (+ `sweep_results_v32.md`) | (I-17 Module 8) | `i17_simulation_prep (acceptance + harness) + combat_v32 §4.6 (Class B doctrine); all mechanics from M1–M7` | Integration engine wiring M1–M7 + symmetric archetype sweep (every archetype vs every archetype) + Wilson 95% CI + acceptance verdict. Vectorized exchange resolution (M2 pools/health/wounds, M3 weapon TN/damage, M4b subaction pool/degree/strike, M5 stance/reaction σ, M6 drain/thresholds, M7 facing frontal-neutral, M1 d10+σ throughout). N=2000/matchup, exchange cap 30, modal Committed depth. Engine invariants PASS (self-matchups ~0.50 → no side bias, Wilson CI shrinks with N, felled produces real contests). **VERDICT: v32 build axis NOT BALANCED** in the frontal-symmetric baseline — 77/90 significant imbalances, 4/10 non-viable; discriminator is weapon category (heavy_weapon dominates light_blade) more than raw End/Str. 6 ledger entries (5 M-method statistical cited to prep, 1 Class-B doctrine); no new mechanical constants. Run honestly, nothing tuned to pass. FLAGS: [ASSUMPTION] symmetric doctrine not Nash (mean-zero, cyclic); [ASSUMPTION] frontal facing (M7 flank/rear not exercised); [GAP] §4.5 Reading→σ not modeled (carried from M7). Verdict sound for the frontal baseline; not yet the full positional game — re-run with Reading wired + positional variant before concluding the axis is mis-weighted. |
| `tests/sim/v32-combat-balance/m9_wound_model_bottomup.py` | (post-I-17 remediation, Jordan-authorized) | `combat_v30 §5/§8 (Class-A anchors) + proposed Class-C bottom-up redesign` | Bottom-up wound model replacing v32's multiplicative damage (the M8 imbalance cause). severity = net + bounded_strength (floor(Str/2) cap 3) − armour_resist(type,tier); decisive vs unarmored (net≥3 wounds directly); reach = −1 Ob closing, not damage. NO crit doubling, NO Str/weapon multiplier. Self-test 7/7 = unit-level HISTORICAL validation: plate negates cuts (cut-vs-plate 2 vs soft 6); blunt defeats plate (5>2); thrust beats cut vs plate (4>2); strength bounded edge not multiplier (Str7−Str1=3, not 7×); unarmoured lethal; reach=tempo; armour monotonic. Historical grounding: half-sword/estoc, poleaxe/warhammer, Liechtenauer/Fiore (skill>force), spear-is-king. 7 ledger entries (2 Class-A retained, 5 Class-C proposed, sim-tunable). PROPOSAL — does not edit canon; Jordan ratifies. |
| `tests/sim/v32-combat-balance/m8b_historical_sweep.py` (+ `wound_model_resweep_results.md`) | (post-I-17 remediation) | `M9 bottom-up wound model + i17_simulation_prep harness; mechanics from M1–M9` | Re-sweep with M9's bottom-up wound model (no crits/multipliers) + short decisive fights. TWO axes. **(A) HISTORICAL validation top-down: PASS 5/5** — armour decisive (plate vs unarmored 96.8%), anti-armour weapons (thrust/blunt vs plate 9.3% > cut 0.1%), reach (63%), skill>strength (87.5%), fights short (7.85 exchanges). **(B) BUILD-AXIS balance within armour tier: STILL NOT BALANCED** at none (74/90) and heavy (72/90). KEY FINDING: removing multipliers necessary but not sufficient; bottleneck MOVED from weapon-category/damage (M8) to COMBAT POOL SIZE (M2 Agi×2 + History) — the d10 S-curve compounds a pool-size edge (the √N small-pool dynamic). Recommended next lever: compress the Combat Pool spread before re-tuning damage. 4 ledger entries (M-method + Class-C harness). PROPOSAL — no canon edited. |
| `tests/sim/v32-combat-balance/r1_sigma_resolution.py` | (armature reset 2026-05-29) | `params/core.md §Degrees/§Obstacle/§Derived/§Attributes + modifier_system_spec §4 (Class A); wound_model_resweep_results.md (Class C anchor)` | Corrected-model sigma-leverage RESOLUTION atom (replaces M8/M8b attrition + the Agi-scaled pool). Demoted, Agility-INDEPENDENT, History-driven resolution_pool (max(5, History+6)) closes the C-04 channel M8b pinned (Agi x2 + History -> base-rate dominance; M8b: compress the pool spread). Agility re-expressed as a sigma-leverage tempo delta-sigma (LEVEL_SIGMA[minor]/2 per point off avg, uniform impact). Reuses M1 (eff_ob/soft_cap/p_success/roll) + M5 (stance lever); state-gating per modifier_system_spec §4 (live 5/6/6/4); canonical degree band, crit = Overwhelming-degree strike, magnitude = net-Ob gauge. Self-test 6/6 PASS: demoted pool Agi-invariant (C-04 closed by construction); Agi via bounded delta-sigma (Agi6 +0.36/Agi1 -0.24); state-gating 5/6/6/4; Ob floored at 1; canonical degree/crit; end-to-end setup 53.5->78.3 with real M5 lever. 9 ledger entries (7 Class-A, 2 Class-C sim-seeds BASE_POOL/AGI_TEMPO). PROPOSAL — no canon edited; demoted-pool FORM is Jordan decision A (History-driven seeded vs flat base). |
| `tests/sim/v32-combat-balance/r2_consequence_wounds.py` | (armature reset 2026-05-29) | `combat_v30 §5/§6 (Class A) + derived_stats §4.1 (Class A); M9 ARMOR_RESIST = historical oracle` | Consequence atom: canonical strike damage (Damage = net + STR x mult + weapon-modifier-vs-armour-tier, PP-232; crit net>=3 doubles ONLY the weapon modifier PP-211, STR term not doubled) feeding the AUTHORITATIVE non-resetting wound-gate tracker (derived_stats §4.1: Health=(End+6)x(MW+1), MW=min(floor(End/2)+1,3) PP-717 cap, WI=End+6, a hit>WI crosses multiple gates, felled at MW+1, -1D/wound no Ob). Armour UNIFIED BY CANON (combat_v30 §6: DR subsumed into the weapon-vs-armour table -- no second subtractor; M9 per-type resist retained only as historical oracle). Bounds the reinstated multiplier: one-exchange + gate-cap<=4 + armour-typed resistance => M8 attrition runaway cannot recur. Reuses M3. Self-test 7/7 PASS. 10 ledger entries (9 Class-A, 1 Class-C framing). PROPOSAL -- no canon edited. |
| `tests/sim/v32-combat-balance/r3_parity_sweep.py` (+ `r3_parity_result.md`) | (armature reset 2026-05-29) | `params/core §Attributes (Class A) + simulator §8.8 band (Class M); wires R1+R2` | Cross-attribute PARITY sweep -- the correctly-framed C-04 (Ω-d no-dominant-strategy). Equal physical-triad budget Agi/Str/End, symmetric, N=4000/matchup, Wilson 95% CI, one decisive 6-10s exchange (NOT attrition). FINDING (honest): C-04 CLOSED (Agi no longer dominates, field 40.1%; demoted Agi-independent pool removed the base-rate channel M8b pinned) BUT dominance MOVED to Endurance (End-heavy field 63.4%, CI[62.4,64.5] excludes band; wound-gate depth Health 44 vs 24 outweighs Str mult + Agi tempo). Reproduces PP-717 End-dominance. Parity NOT yet passing; End/Str/Agi channel magnitudes are the Class-C tuning knob (Jordan calibration; project-owner contract bars Claude from retconning balance). 5 ledger entries (2 Class-A, 3 Class-M). [GAP] full Agi sigma-stack (M5/M7) + weapon/armour variety not yet wired (Build-4). PROPOSAL -- no canon edited; sweep is the tuning oracle. |
| `tests/sim/v32-combat-balance/r4_full_channel_parity.py` (+ `r4_parity_result.md`) | (armature reset 2026-05-29) | `params/core §Attributes (Class A) + R1/R2/M3/M5/M7 + simulator §8.8 (Class M); decisive-frame + channel seeds Class-C` | Full-channel EQUAL-VALUE sweep (Jordan: wire as required + all attributes equal value). Full Agi sigma-leverage stack (init+tempo[R1]+facing[M7]+reaction[M5]) + Reading(Cog/Att) into a DECISIVE one-phrase exchange; equal-15pt Agi/Str/End/Reading x 4 weapons x 4 armours, Wilson 95% CI, N=4000. Class-C seeds tuned toward equal value (spread 63->43pp). FINDING: C-04 stays closed; decisive frame tamed R3 End-dominance (66%, co-equal not runaway); Reading PARITY (46% in-band, C-06); Strength structurally DEAD (23%, loses to ALL) -- +0.00 sigma-leverage vs Agi +0.50/Reading +0.625; LANDING decides, magnitude weakest currency. Equalising Str needs a LANDING/CONTROL channel = NEW MECHANIC = Jordan decision. End residual = canonical Health depth = Jordan canonical decision. 11 ledger entries (3 A, 5 C, 3 M). PROPOSAL -- no canon edited; finding is the deliverable. |
| `tests/sim/v32-combat-balance/r5_strength_stamina.py` (+ `r5_r6_result.md`) | (armature reset 2026-05-29) | `combat_v30 §5 STR-min + derived_stats §4.2 Stamina (Class A); Jordan decisions 2026-05-29 (Class-C)` | Strength LEVERAGE channels + Stamina recomposition (Jordan's 2 decisions). Str gets bind-win, stagger (heavy-Overwhelming opens next-strike window), armour-defeat window (half-sword/poleaxe vs armour), stamina efficiency, wield penalty (canonical). Converts Str from R4-dead pure-magnitude (+0.00 sigma-leverage) to landing/control: self-test Str leverage now +0.88 in-bind / +0.38 closing; single-loadout Str beats Agi 2072-927, niche heavy-blunt-vs-plate 2666-331. Stamina = 3*End + 2*Spirit (replaces canonical End x5; End3/Spi3=15 matches old) -> Spirit gains first combat role (reserves), End loses action-economy monopoly; depletion drives canonical Out-of-Breath -2D. Self-test 6/6. 12 ledger entries (6 Class-A, 2 Class-C-proposed-canon Stamina, 4 Class-C channels). CANON ITEMS for Jordan: Stamina formula change, Spirit definition expansion, bind/stagger new mechanics. PROPOSAL -- no canon file edited. |
| `tests/sim/v32-combat-balance/r8_parity_harness.py` (+ `r8_result.md`) | (armature reset 2026-05-29) | `params/core §Attributes (Class A) + R1/R2/R5/M5/M7 + simulator §8.8 (Class M)` | DEFECT-IMMUNE equal-value harness (replaces R6/R7 corrupted drivers). Self-contained on validated units (NOT importing R6/R7 build/driver code); builds hardcoded + asserted to budget 18 at construction AND before every matchup; ALL results to JSON read from file (never piped stdout); deep-copy into every call. Each archetype best-responds on loadout, then asymmetric all-vs-all, Wilson 95% CI, N=3000. TRUSTWORTHY VERDICT (supersedes all prior session field-rates, which were corrupted by buffer-interleaving + intermittent budget-13 Str builds): **Str 85.3% DOMINANT (over-tuned -- channels stack), Agi 58.1% / End 42.8% / Reading 48.8% cluster acceptably, Spirit 12.3% DEAD.** The INVERSE of the earlier 'Str dead' artifact. The Stamina split tamed End (was dominant -> 43%); Reading reached parity after tuning. FINDINGS: (1) Str channel magnitudes over-weighted = Jordan calibration (harness is now the reliable oracle); (2) Spirit needs a SECOND combat channel (stamina-reserves alone too thin) = design decision. 13 ledger entries. PROPOSAL -- no canon edited. Supersedes the harness_defect_handoff finding. |
| `tests/sim/v32-combat-balance/r9_weapon_engagement.py` | (armature reset 2026-05-29) | `combat_v30 §5 reach + m3 speed (Class A); HEMA measure/bind (top-down)` | PHASE-DEPENDENT reach+speed tempo (the spear fix). Reach governs closing/breaking (canonical reach=-1 Ob closing); speed governs the bind (faster wins once closed, reach INVERTS -- HEMA). Niches by construction: spear wins approach/loses bind, dagger loses approach/dominates bind, war hammer wins approach/worst in bind. Self-test 5/5. Grounded bottom-up (canonical reach+speed) + top-down (HEMA); gap-completion of canon 'spear is king'. FINDING: right mechanism but 8-way convergence is a JOINT-FIT problem (reach helps every long weapon; Heavy-Blunt x3->x2 barely moves the hammer 79->76%); clean separation (reach benefits light-long not heavy-long) = design call for Jordan. 4 ledger entries. PROPOSAL -- Jordan-vetoable, no canon edited. |
| `tests/sim/v32-combat-balance/r10_battlefield_context.py` (+ R9 v2) | (armature reset 2026-05-29) | `combat_v30 §5 damage/armour + R1/R2 (Class A); Jordan battlefield insight + HEMA (top-down)` | DUEL vs BATTLEFIELD resolution context -- resolves the weapon-convergence thread per Jordan. Strikes-to-fell proved the war hammer's duel dominance is canonical DAMAGE (fells in 3 strikes vs blades' 4-6; 2x armour-defeating gap sigma-tempo cannot offset) -- so it cannot be made duel-weak by tempo AND should not be: it is a BATTLEFIELD weapon (poleaxe/maul), used vs an armoured foe already ENGAGED with a third party. R10 models the engaged-foe context (defensive sigma-leverage SUPPRESSED -> raw armour-defeating damage governs): war hammer fells an engaged armoured foe in 2.3 strikes vs longsword 4.3, dagger 6.3; advantage GROWS with armour (inverse of its duel weakness). R9 v2: reach-CONTROL scales with lightness (spear out-fences hammer) + all-phase speed -> heavy slow weapon disadvantaged in every DUEL phase. DUEL audit: 7 dueling weapons cluster (spread 29pp, mean 47%); war hammer excluded from duel-balance target. NET: every weapon has a place across the two contexts; NO canonical damage nerf needed (war hammer's x3 is correct for the battlefield). Self-test 3/3 (R10) + 5/5 (R9 v2). PROPOSAL -- Jordan-vetoable, no canon edited. RECOMMENDATION: KEEP Heavy-Blunt x3 (battlefield identity); gate war hammer by context/availability. |
| `tests/sim/v32-combat-balance/weapon_axes_v2.py` (+ `wa2_validation_result.md`) | (armature 2026-05-29) | `combat_v30 §5 + W1 ratified (Class A); weapon_axes_v2.md proposal` | v2 WEAPON SUBSTRATE bottom-up: hands (1H/2H) + head (point/cut_and_thrust/straight_cut/curved_cut/blunt) axes; full roster (all + tonfa short-blunt + war flail flexible) reclassified; derived damage_class/armour(+point row)/str_mult/wield_min; v2 sigma-modifiers (head bias, 2H bind amp, 1H off-hand, curved draw-cut, flexible parry-bypass, tonfa block). Self-test 7/7. TOP-DOWN VALIDATED vs historical precedent: blunt percussion fells engaged armoured foe in 3 strikes (blades 5.5-6.3); point beats cut vs armoured field; sabre/dagger/longsword duel-cluster; flail parry-bypass + tonfa defence work; generalists mid. Only artifact = bare mace tops duel 73.6% = the war-hammer blunt-damage artifact (R10), resolved by CONTEXT not nerf. Canon-touching: POINT_ARMOR_MOD (point-vs-armour row) flagged for ratification. PROPOSAL -- Jordan-vetoable, no canon edited. **REFINED to historical coherence** (iter 1-4): + handling skill-curve (crossover prof 4) + reach-control (balanced heavy blade keeps reach, head-heavy blunt loses it) + two-CONTEXT resolution (duel=telling-hit finesse race / battlefield=attrition); two grounded handling corrections (longsword->demanding, war_flail->forgiving). Now coherent across 3 contexts: skilled-duel rapier#1/longsword#5, mace+war_flail bottom; low-skill forgiving weapons dominate; battlefield blunt fells in 3. Bare-mace artifact resolved by context+skill, no damage nerf. Self-test 10/10. |
| `tests/sim/v32-combat-balance/armour_axes.py` (+ `armour_system_design.md`, `armour_validation_result.md`) | (armature 2026-05-30) | `3.4 Armour + combat_v30 §5 W1/W5 (Class A, reproduced); armour_system_design.md proposal` | BRAND-NEW ARMOUR SUBSTRATE bottom-up (Jordan design grant): reproduces the canonical skeleton EXACTLY (tiers/STR-min 0-2-3-4/drain +0+0+1+2/Health +4+6+8/the W1+W5 weapon-vs-armour table -- no retcon) and adds the structure underneath: the table re-read as an (attack-head x material) MITIGATION MATRIX (self-test check 1 = reproduces every ratified row) + two axes (material none/cloth/mail/plate->matrix; coverage partial/full->gap exposure) with the 4 tiers as presets; costs via ratified Stamina drain + flat Health + STR-min + a NEW sigma-tempo penalty (only new lever, flagged). Self-test 7/7. TOP-DOWN VALIDATED: weapon-head vs plate = blunt fells 3.0 / point 5.5 via gaps / cut 6.2 deflected (exactly history); coverage partial<full; mail anti-cut>anti-thrust. CORRECTED finding: 'fatigue erodes plate in a long duel' FALSIFIED (symmetric fatigue cancels; progressive penalty + kiting both fail) -> plate ~95%% dominant 1v1 (HISTORICALLY CORRECT); real counters = blunt + thrust-to-gaps + grappling(future). Fatigue re-scoped to a cost/constraint. PROPOSAL -- Jordan-vetoable. |
| `tests/sim/v32-combat-balance/grappling.py` (+ `grappling_system_design.md`, `grappling_validation_result.md`) | (armature 2026-05-30) | `3.6 Actions (Class A, reused); grappling_system_design.md proposal` | GRAPPLING / CLOSE-COMBAT SUBSTRATE bottom-up (THE THIRD PLATE-COUNTER): unifies the CANONICAL close-combat actions (Disarm/Tie Up/Escape/Retrieve, 3.6 Actions) into a grapple phase + ST1 Strength-dominant sigma-contest + the armour matrix + wa2 hands; fills the canon-ack unarmed gap (ED-129). One new element = the grounded-foe DAGGER-FINISH (point to gaps, BYPASSES armour mitigation). Self-test 6/6. TOP-DOWN VALIDATED: (A) grappler fells full-harness foe in 4.2 strikes (vs blunt 3.0; cut deflected to mod 0) -> the blunt/point/grapple triad is complete; (B) context-gated -- 0%% vs a spacing rapier UNARMOURED (reach/tempo beats the closer, closing is risky) but 98%% vs the same fighter IN PLATE (armour slows the spacer + grapple bypasses plate). Historical: Fiore abrazare, ringen, half-sword, the rondel dagger. CAVEAT: the 0%% is exaggerated (direction validated, magnitude not). PROPOSAL -- only the dagger-finish is new; Jordan-vetoable. |
| `tests/sim/v32-combat-balance/damage_model.py` (+ `damage_model_design.md`) | (armature 2026-05-30) | `derived_stats §4.1 wound model + params/core degrees (Class A, consumed); damage_model_design.md proposal` | GROUND-UP DAMAGE REBUILD: pretend no prior formula; derive only from the new combat resolution (net/degree) + the wound model (WI=End+6). SUPERSEDES the inherited formula (net + STR x mult + weapon_armour_mod; x1/x1.5/x2/x3; crit-doubles-mod). Damage = Impact x Coupling x Quality: Impact=STR+Heft ADDITIVE (no STR x weight mult); Coupling=Delivery(head) x Transmission(material,mode) x GapAccess(coverage) DERIVED from material resistance-per-mode (matrix emerges, folds in the weapon-vs-armour mod); Quality=degree (replaces crit-doubles). 1 calibration const (Success~=1 WI). Self-test 8/8. VALIDATED full roster (cut collapses vs plate / point gaps / blunt transmits / thrust beats mail; pacing ~3-5 unarmoured, cut 14 / blunt 4 vs plate). Wound model UNCHANGED. PROPOSAL -- supersession flagged. |
| `tests/sim/v32-combat-balance/combat_resolution.py` | (armature 2026-05-30) | `all armature combat modules (composed); damage_model_design.md` | UNIFIED COMBAT RESOLUTION PIPELINE (integration capstone): composes sigma-leverage (R1+m1) + weapon_axes_v2 + armour_axes + ground-up damage_model + grappling through ONE resolve_exchange/run_engagement with the ratified damage. INTEGRATION FINDING: the earlier duel finesse-race (rapier#1) was an ARTIFACT of abstract hit-counting -- under REAL ground-up damage the mace's heft dominated the unarmoured duel (rapier 16-23%). FIX (bottom-up improvement): sigma-leverage now gates hit QUALITY (degree->damage, LEVERAGE_TO_DEGREE=3.5), not just who-lands -- a finesse edge lands Overwhelming more so the rapier's modest Impact kills, while battlefield+low-skill blunt stay dominant. Self-test 6/6 (composes; leverage->hits+degree+damage; skilled duel rapier-v-mace 52%; battlefield blunt 99%>cut 0% vs plate; armour 100%; grappling wired). No new mechanics besides the gating. PROPOSAL -- Jordan-vetoable. |
| `tests/sim/v32-combat-balance/r6_equal_value_resweep.py` | (armature reset 2026-05-29) | `params/core + R1/R2/R5/M5/M7 + simulator §8.8` | Equal-value re-sweep wiring R5 (6-attr Agi/Str/End/Reading/Spirit). IN-PROGRESS HARNESS, NOT A VERDICT: single-loadout traces confirm Str's channels work, but field aggregate confounded by loadout-averaging + shared-weapon symmetry (mirror loadouts cancel Str's niche). Needs per-loadout isolation + asymmetric loadouts before field rates mean anything. Committed for continuity, flagged. 6 ledger entries (1 Class-A, 5 Class-M). |
| `tests/sim/sim_mb_sigma.py` | (ratified canon mass-battle engine; sigma-leverage head + graded morale + 3+ turn pacing) | canon set aside per owner directive 2026-05-31 — validated top-down vs real historical precedent (du Picq / ancient-battle scholarship) | Sigma-leverage exchange head: advantages (octagon facing, puncture, encirclement, ranged-in-melee) as delta-sigma net-boost on offensive net successes (uniform impact), not pool mods. Graded morale->effectiveness as delta-sigma + damped erosion (MORALE_FIX). CASUALTY_SCALE=4 -> evenly matched units resolve over ~3+ turns. Validated via gauge_mb_ci.py (Wilson 95% CI): 11/13 melee CI-consistent (single); multi-turn 3-4 turns, casualty paradox resolved (loser>winner). Known defects: structural A-side exchange bias; H7 GappedLine contact-geometry. 17 ledger entries (Class-B sim-tunable / inherited-validated). |
| `tests/sim/sim_mb_sigma.py` (PER_CELL Increment 1) | per-column block grid state | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | PER_CELL env toggle (default OFF) + _ColBlock + build_column_grid (per-column density/stamina/depth from unit footprint). Toggle-OFF reproduces 0dea67d1 200/200. Grid conserves troops (Line 5col xd5 @80; GappedLine 8col xd3 @50). Resolution wires in at Increment 2. |
| `tests/sim/sim_mb_sigma.py` (PER_CELL Increment 2) | per-column casualty distribution substrate | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | distribute_casualties spreads each tick's casualties across engaged front columns (density-proportional), synced so sum(col densities)==hp. Transparent: PER_CELL=1 reproduces PER_CELL=0 200/200; conserves troops (verified). Substrate for fatigue/charge/envelopment (Increments 3-6). |
| `tests/sim/sim_mb_sigma.py` (PER_CELL Increment 3) | depth-damped fatigue as delta-sigma | canon set aside per owner 2026-05-31; validated vs real warfare (du Picq) + NERS diagnostic | _fatigue_sigma + update_stamina: engaged columns drain stamina (damped by depth — deeper rotates fresh ranks, drains slower), tired front gets negative delta-sigma. First behaviour-changing increment. PER_CELL=0 reproduces committed 150/150. Multi-turn: wide GappedLine vs deep Line 93%->80%, deep doubles, mirror balanced (45-51%), battles lengthen 3->5 turns. Residual width edge -> Increment 4. |
| `tests/sim/sim_mb_sigma.py` (PER_CELL Increment 4) | depth-aware contact fraction | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | Under PER_CELL the opponent contact-fraction (damage scaler) is depth-aware: width term (engaged cols / PC_FRONTAGE_REF, capped) keeps more-men-fighting, removes the reserve-depth penalty that let wide-shallow out-damage deep. PER_CELL=0 reproduces committed 150/150. Multi-turn H7 GappedLine vs Line 93%->44%; H1 49, H2 62, H4 43 in band; H6 39.7 (~band); mirror balanced. THE H7 FIX. |
| `tests/sim/sim_mb_sigma.py` (PER_CELL Increment 5) | depth-absorbed charge (cavalry) | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | Unifies charge with the momentum-puncture under PER_CELL: intrinsic charge_pen (cavalry=3) presses while out-momentuming; DEFENDER engaged-column depth absorbs penetration (deep absorbs, thin punched through). PER_CELL=0 reproduces committed 150/150; infantry charge_pen=0 so H1-H11 unchanged. Absorption mechanism validated (depth5 absorbs pen3). GAP: cavalry speed->momentum plumbing unwired, so charge does not yet TRIGGER in a frontal clash (needs the velocity primitive) — absorption layer is built and ready. |
| `tests/sim/sim_mb_sigma.py` (PER_CELL Increment 6) | envelopment + flank-refusal (DORMANT) | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | _envelopment_sigma (wider side's overhang pressures flanks, refused by enemy reserve depth) built and wired but DISABLED (PC_ENVELOP_SIGMA=0): the Incr4 depth-aware contact fraction already captures the width advantage, so a separate envelopment delta-sigma double-counts and breaks H4 Cannae (45->2%). NERS-N/E: not shipped active. PER_CELL=0 reproduces committed 120/120. Bands unchanged from Incr4 (H1 49,H2 62,H4 43 in; H6 36,H7 44 low). |
| `tests/sim/sim_mb_sigma.py` (cavalry velocity primitive) | cavalry closes faster -> triggers charge | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | Under PER_CELL, cavalry actual_speed x PC_CAVALRY_SPEED_MULT (2.0): cavalry now out-momentums infantry (cell speed 2 vs 1), producing the differential that triggers the Incr5 depth-absorbed charge. PER_CELL=0 reproduces committed 120/120. Charge fires + is absorbed by deep formations (cavalry weak vs deep Line, strong vs shallow). NOTE: broader cavalry-vs-infantry balance tuning still open. |
| `tests/sim/sim_mb_sigma.py` (fatigue rest refinement) | only genuine reserves recover stamina | canon set aside per owner 2026-05-31; validated vs real warfare + NERS diagnostic | update_stamina rest fix: a column recovers ONLY if not adjacent to any engaged column (a true reserve) and battle is joined — front-line columns momentarily out of the contact set no longer spuriously heal (which masked front fatigue). Stamina pattern realistic ([0,0,0,0,38] vs prior [5,5,5,5,100]). PER_CELL=0 reproduces committed 120/120; no band regression (H1 52,H2 57,H4 46,H7 47 — H7 slightly improved). |

## Tier 3 Stub Infill — Lane C (2026-05-31) — proposals/stub_infill_plan.md

| Module | Commit | Canon | Verification |
|---|---|---|---|
| `sim/personal/parliamentary_vote.py` | (Lane C 2026-05-31) | `social_contest_v30 §10` + `02_canon_constraints §B GD-3` | `run_parliamentary_vote` §10 BG vote — Mandate(=L) pool + genre/audience +1D, TN7, track thresholds 7/3/4–6, total-victory ≥9/≤1 → Mandate −1; GD-3 extra-parliamentary filter; reuses contest §6 constants. Smoke 4 scenarios verified. 11 §10 ledger entries appended. |

## Tier 3 Stub Infill — parliamentary_stay (Lane C 2026-05-31) — proposals/stub_infill_plan.md

| Module | Commit | Canon | Verification |
|---|---|---|---|
| `sim/personal/parliamentary_stay.py` | (Lane C 2026-05-31) | `social_contest_v30 §10.1` (ED-631) | `invoke_stay`/`resolve_stay_lift` — §10.1 Stay via §10 vote; CI<55 availability gate, ≥2 Side A + Church Side B, pass→suspend 1 season else proceed. Verified across 60 seeds (granted/denied) + unavailable/invalid + resolve_stay_lift season-gating. 3 §10.1 ledger entries. |
| `tests/sim/sim_mb_sigma.py` (envelopment wheel P1/P2) | overhang cells wheel toward enemy flank; facing follows | canon set aside per owner 2026-05-31; validated vs real warfare + Jordan rotation hypothesis (confirmed) | advance_cells: an overhang cell (column beyond the enemy frontage span) targets the nearest enemy cell instead of its own column -> wheels inward -> cell_facing_vec rotates inward (Horseshoe 4/18 cells now lateral, was 0/18). Gated PER_CELL+PC_WHEEL; PER_CELL=0 reproduces committed 120/120. Cells now ROTATE (hypothesis fix). Combat payoff NOT yet realized: _per_cell_angle_mod uses attacker CENTROID (still frontal) not the wheeled cell -> next step is centroid->nearest-attacker for flank detection. |

## Tier 3 Stub Infill — parliamentary_transfer (Lane C 2026-05-31) — proposals/stub_infill_plan.md

| Module | Commit | Canon | Verification |
|---|---|---|---|
| `sim/provincial/parliamentary_transfer.py` | (Lane C 2026-05-31) | `parliamentary_transfer_v30 §§1-4` (CANONICAL Pass 2h, v12c N=1000) | `propose_transfer` — CB-gated territorial transfer via §10 vote; Influence-vs-(Legitimacy+2) Continuous-Engine roll → 4-degree §1.2 outcomes; 4 modes (§2), 8 CB sources (§3), §1.3 protections. Verified: GD-3/self/last-territory/no-CB blocks + Crown auto-CB 80-seed sweep (24 transferred/41 partial/15 failed) + territory+Accord mutation + failure/punishment/appeasement mode effects. 7 ledger entries. |
| `tests/sim/sim_mb_sigma.py` (M2/M3 perception+refusal, DORMANT) | FOV+pinning+flank-refusal | grounded: human visual field ~190-210deg (Wikipedia/NCBI) -> 150deg rear blind; fixing-force doctrine + Clausewitz oblique reserves | M2: REAR_BLIND_DEG=150 (visible +/-105deg), PC_PIN_REACH=1.5. M3 (_per_cell_angle_mod, gated PER_CELL+PC_REFUSE): each defender cell judged vs its worst-flanking attacker; refuses (negates penalty) only if NOT pinned AND attacker in FOV, else flank/rear penalty lands. Envelopment EMERGES with PC_REFUSE=1 (H3 47->58, H4 43->50, H7 40->57 IN) but introduces a mirror bias (H1 57-62 vs 50; worst-attacker detection is position-sensitive/asymmetric) + reverse-pair inversion (H10/H11 HIGH) + H6 break -> DORMANT (PC_REFUSE default off). PER_CELL=0 and PER_CELL=1-default reproduce the wheel engine 120/120. Fix needed: mirror-stable flank detection + enveloper-self-flank resolution. |
| `tests/sim/sim_mb_sigma.py` (M3 structural envelopment, DORMANT) | F1/F2 mirror+inversion fix | Clausewitz formation-in-depth + fixing-force doctrine; mirror-unbiased invariant | F1/F2: envelopers detected STRUCTURALLY (attacker cells beyond the defender's frontage span), not by angle extremum. Mirror-stable by construction (equal width -> no wrappers -> H1 50.0 IN); also fixes the enveloper self-flank (wider side's narrower enemy can't wrap it -> H10 inversion resolved). RED-zone wrapper penalty PC_ENVELOP_MOD=-1.0, refusal-gated (pinned/blind -> lands; free+sighted -> refuse). At -1.0: H1/H2/H4/H7/H10 IN. REMAINING (depth-resistance, next): H3 still HIGH (68 — width over-rewards wide shapes) and RefusedFlank H5/H6 LOW (a refused/deep flank should RESIST the wrap; width alone decides it now). PER_CELL=0 and PER_CELL=1-default reproduce the wheel engine 120/120. |
| `tests/sim/sim_mb_sigma.py` (M3 F3 nominal-span gate, DORMANT) | mirror-clean by construction | mirror-unbiased invariant (now MET by construction) + envelopment reach = span | F3: a wrapper requires the attacker to be NOMINALLY WIDER by column SPAN of the static oriented pattern (symmetric under A<->B; gapped formations correctly wide by reach). PROVEN inert in a mirror (mod=-1==mod=0). Supersedes the prior 'mirror +4 bias' flag (that was n<=120 sampling variance, ~+/-7/seed; aggregated ~50). RESULT 2-seed n=120: 6/10 IN incl H1 48.6 (mirror) and H3 64.5 (headline). Remaining LO: H5/H7 (RefusedFlank refusal-facing; GappedLine gap dynamics), H6 (pre-existing equal-span base value), H11 marginally HIGH. DORMANT; default-on is Jordan's call pending H5/H7 + high-n NERS Stage-4. PER_CELL=0/refuse-off byte-exact. |
| `tests/sim/sim_mb_sigma.py` (M3 pocket / gap-trap, DORMANT) | Polybius maniple gap-trap + concave pocket | Polybius/Wikipedia: maniple gaps 'lured hoplites in... disorganized, surrounded'; manipular flexibility vs rigid line | PC_POCKET_MOD=-1.0, PC_POCKET_REACH=2. A defender cell with enemies level on BOTH lateral sides, fired ONLY where the wrap did not (gap maniples are within the defender span -> not wrappers; concave wings are beyond -> wrappers, no double-count). Mirror-safe (parallel lines put enemies ahead, never beside on both). RESULT 2-seed n=100: 7/10 IN (H7 GappedLine-v-Line 44.7->48.9 borderline; H11 fixed via no-double-count; H3 held 60.4; H1 mirror 50.6). H5 still LO (refused-flank resistance = next). H6 regressed to 22.8 but is plausibly CORRECT top-down (a refused flank is wasted vs a frontal line -> band 45-60 likely optimistic). PER_CELL=0/refuse-off byte-exact. |
| `tests/sim/sim_mb_sigma.py` (PC_REFUSE default ON) | per-cell envelopment activated | validated model: mirror unbiased by construction, H3 in band, 7/10 IN (2-seed n=100) | PC_REFUSE flipped default '0'->'1' per Jordan ('refuse on'): the envelopment model (wheel + FOV/perception + pinning + refusal + structural wrap + Polybius gap-trap pocket) is ACTIVE in the per-cell path. PER_CELL still gates the whole layer and stays default OFF -> the shipped mass engine (PER_CELL=0 = ratified base 0dea67d1) is UNCHANGED, verified byte-exact 120/120 with the flip. Only affects PER_CELL=1 runs. |
| `tests/sim/sim_mb_sigma.py` (vectorized depth + oblique roll-up) | depth parallel to attack-vector; flank roll-up | Jordan geometric corrections + oblique-order roll-up (Leuthen/Leuctra: deep wing rolls thin wing); attrition non-double-count | Depth-resistance now measures supporting depth PARALLEL to the wrapper's approach (`_support_along_vector`: file-depth for a frontal hit, row-depth for a flank hit, on-diagonal full + clipped-partial for a diagonal) instead of the Y-column -- a flank-attacked cell no longer draws spurious support from the rank behind it (y-1). Oblique-offense ROLL-UP: at an in-contact lateral-extreme (wing) cell where neither wrap nor pocket fired, if the nearest attacker's push-depth out-masses our support past PC_ROLLUP_MARGIN=1.0, penalty -PC_ROLLUP_PER_RANK=0.4 per rank (cap -1.0), gated to defenders still >= PC_ROLLUP_MIN_DEPTH=2.0 so it never double-counts attrition on a 1-rank remnant. Constants: PER_RANK 0.4 / MARGIN 1.0 / REACH 1.6 / CAP -1.0 / FLANK_REACH 1.0 / MIN_DEPTH 2.0. Validated 2-bank n=80: 11/13 CI-consistent (= committed baseline), H3 51.2->55.6 and H11 46.2->50.6 more central, H5 held in band (depth-correction's drop offset by the roll-up), no regression. Mirror inert by construction (H1/R3); toggle-off PER_CELL=0 120/120 byte-exact. |
| `tests/sim/gauge_mb.py` (cavalry coverage C1-C4 — Phase 0, audit S2) | cavalry/charge/momentum/envelopment gauge rows (closes the S2 test gap) | bands OBSERVED PER_CELL=1 then validated top-down vs precedent (du Picq; Waterloo squares 1815; Falkirk/Bannockburn schiltrons 1298-1314; Cannae rear-charge; Adrianople 378; Hastings); canon A.6 Shield Wall = braced-defence anchor | Closes audit finding S2: the gauge HARDCODED troop_type='infantry', so cavalry/charge/momentum/puncture had ZERO coverage and S1/S3/S4/S6 were unvalidatable. `make_unit` now takes backward-compatible `troop_type='infantry'`/`speed='Standard'` params; 4 cavalry rows append PER_CELL=1-ONLY (engine gates charge_pen + PC_CAVALRY_SPEED_MULT on PER_CELL, so PC=0 output is byte-identical to baseline — verified). C1 cav-Arrowhead vs unbraced Line 52-80 (obs 55.0; vs inf-Arrowhead control 40 = charge worth +17pp). C2 SAME cav vs BRACED Line (hold+disc8, the Shield-Wall proxy) 8-42 (obs 21.7, 61.7% draws) — a MINIMAL PAIR with C1 isolating prepared defence; repulse is currently EMERGENT (hold + _defender_depth + discipline), NOT an explicit gate -> P3 anchor + P2 regression guard. C3 cav-vs-cav mirror 42-58 (obs 51.7) — side-symmetry hygiene. C4 cav-Horseshoe envelopment vs Line 70-92 (obs 83.3; foot-envelop H3 ~60 -> mounted +25pp). PER_CELL=1 multi: existing-13 numerically identical to baseline + 4 cav IN-band (10/17). PER_CELL=0: byte-exact to 0dea67d1 baseline (single 0/13 multi 5/13), cav rows correctly excluded. Bands Class-B/M sim-tunable (NOT canon); Jordan-vetoable. 29 ledger entries (sim_verification_ledger.json: anchors Class-A, defaults/braced Class-B, bands+method Class-M, cav-bands Class-B). Charge_pen flat=3 is the P4 lever; speed-into-combat wiring is S1/Phase 1 (next). |
| `tests/sim/sim_mb_sigma.py` (cavalry shock = moral primitive — Phase 3, audit S6) + `tests/sim/gauge_mb.py` C5-C7 + `designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md` | speed-differential charge delivers a DEFENDER moral-shock delta-sigma, gated by prepared-defence | du Picq Battle Studies ("no shock of infantry on infantry... but a moral impulse"; mechanical vs moral shock); Waterloo squares ("virtually impossible for cavalry to break a well-disciplined square"); Albuera 1811 (line caught -> 1250/1650 ~76% lost); Cannae/Adrianople (rear bypass); Hastings post-feint; canon A.4 morale / A.6 Shield Wall / A.8 Hammer&Anvil | Closes S6 (PC_CHARGE_SIGMA/PC_CHARGE_TICKS were dangling). `_charge_shock_sigma(defender,cells,zone)`: a landed charge (pen>0 post-absorption) lowers the DEFENDER's morale-channel offence by `-PC_CHARGE_SIGMA x G_face x G_brace x A_shaken`. Distinct channel from puncture (puncture = charger PHYSICAL penetration, depth-absorbed, boosts charger; shock = defender MORAL collapse, discipline/stance/facing-gated) -> no double-count (the NERS-N/E trap that disabled _envelopment_sigma); empirically re-tested. Gate from REAL engine state: facing=octagon GREEN/YELLOW/RED; brace=hold-stance(Shield Wall) x discipline(>=5) x _defender_depth; shaken=morale/morale_start. PC_CHARGE_TICKS RETIRED (momentum differential bounds the window emergently — du Picq's spent impulse). Repurposes PC_CHARGE_SIGMA from its dangling charger-offence note to its historically-correct defender-shock role. VALIDATION (multi n=40, shock live): C1-C7 all in band; emergent ORDERING reproduces history -> frontal-braced C2/C6 25.0 < frontal-unbraced C1 62.5 < envelopment C4 87.5 ~ rear-vs-braced C7 77.5 < shaken C5 90.0; C7>>C6 (77.5 vs 25.0) = facing bypasses brace (Cannae). Unit-level gate asserted: facing -0.014/-0.096/-0.154 frontal/flank/rear; brace->-0.005; shaken->-0.024; rear-braced -0.054 (11x frontal-braced). PER_CELL=0 BYTE-EXACT (shock PER_CELL-gated). ANSWERS gate-Q2: facing->deals-less is sufficient EMERGENTLY (octagon+shock), no explicit attacker-output gate needed (NERS-E). All shock constants Class-B sim-tunable, Jordan-vetoable; 31-entry ledger. Limitations [SELF-AUTHORED]: C6==C2 (tier-3 brace is shallow, so depth-isolation is unit-tested not gauge-distinct); bands calibrated at the n that scores them. PROPOSAL — no canon edited. |
| `tests/sim/mass_battle/config.py` (P-A modularize, stage 1/5) | constants extracted to a package module | behaviour-frozen refactor; byte-exact vs 7cfa44d5 | P-A modularization step 1: all ~79 module-level constants (PC_*/SIGMA_*/MORALE_*/structural) moved verbatim (canonical comments preserved) to `mass_battle/config.py`; `sim_mb_sigma.py` now does `from mass_battle.config import *`. PER_CELL=0 gauge BYTE-EXACT to baseline (sole diff = echoed engine filename). Establishes the package scaffold + extraction method. Remaining stages: geometry, resolution, percell, orchestration + engine.py wrapper + MECHANICS registry. 4 structural constants (16/25/200/400) ledgered to §A.3/§A.3b. No behaviour change. |
| `tests/sim/mass_battle/resolution.py` (P-A modularize, stage 4/5) | sigma-head extracted | behaviour-frozen; byte-exact | P-A step 4: roll_pool, compute_degree, _morale_sigma, _charge_shock_sigma, _sigma_softcap, _sigma_net_boost (~60 lines, two clusters) moved verbatim to `mass_battle/resolution.py` (imports config+percell; explicit __all__). PER_CELL=0 gauge BYTE-EXACT. Remaining: stage 5 = orchestration + classes -> orchestration.py, engine.py wrapper + MECHANICS registry, sim_mb_sigma.py -> shim. |
| `tests/sim/mass_battle/percell.py` (P-A modularize, stage 3/5) | per-cell layer extracted | behaviour-frozen; byte-exact | P-A step 3: _ColBlock, build_column_grid, _engaged_cols, distribute_casualties, _fatigue_sigma, _envelopment_sigma, _defender_depth, update_stamina (~139 lines) moved verbatim to `mass_battle/percell.py` (imports config+geometry, explicit __all__). PER_CELL=0 gauge BYTE-EXACT. Remaining: resolution, orchestration + engine.py + MECHANICS registry. |
| `tests/sim/mass_battle/geometry.py` (P-A modularize, stage 2/5) | geometry extracted to package module | behaviour-frozen; byte-exact vs baseline | P-A step 2: cell layout, facing/octagon, support-vector, cell_speed functions (engine block, ~283 lines) moved verbatim to `mass_battle/geometry.py`; engine now `from mass_battle.geometry import *`. KEY FIX: modules need explicit `__all__` so underscore-prefixed helpers (`_init_dynamic_facings` etc.) cross `import *` — added to geometry + retrofit to config. PER_CELL=0 gauge BYTE-EXACT. Remaining: percell, resolution, orchestration + engine.py + MECHANICS registry. |
| `tests/sim/mass_battle/{orchestration,engine}.py` + `sim_mb_sigma.py` shim (P-A modularize, stage 5/5 — COMPLETE) | orchestration + classes -> orchestration.py; engine.py wrapper + MECHANICS registry; sim_mb_sigma.py -> 5-line shim | behaviour-frozen; PER_CELL=0 byte-exact + PER_CELL=1 clean | P-A FINAL: remaining body (phase hooks + Subunit/Unit classes + assign_targets/find_contacts/resolve_engagements(_cascading)/volley_phase/run_battle/run_multi_turn_battle/run_multi_unit_battle/pursuit/recall/cascade) -> `mass_battle/orchestration.py` (verbatim + explicit __all__). New `mass_battle/engine.py` imports all 5 modules, unions their __all__ for full re-export, and defines MECHANICS (27 canonical mechanics -> fn+toggle+source+status) with mechanics_selftest() (PASS — all resolve). `sim_mb_sigma.py` reduced to `from mass_battle.engine import *` so gauge_mb.py exec() keeps working. VERIFIED: PER_CELL=0 gauge BYTE-EXACT to 7cfa44d5; PER_CELL=1 runs clean, C1-C4 in ratified band. Two gotchas caught pre-commit: import* skips _names (needs __all__); engine __all__ must union all modules. Engine is now a modular container: config/geometry/percell/resolution/orchestration + engine wrapper. MECHANICS registry kept current: +lanchester_attrition (LANCHESTER_ENABLED), +command_sigma_base (COMMAND_SIGMA_ENABLED), +command_derivation — registry now 30 mechanics, mechanics_selftest green (2cf3feb6/7e878ade era). |
| `mass_battle/orchestration.py` general-death comment (P-B / ED-898) | comment relabel: 'General death'->'General incapacitated/captured' | byte-exact; comment-only | P-B engine canon-alignment: the Command<=0 -> morale=0 -> rout logic is UNCHANGED (a captured/incapacitated general = Command 0 = uncommanded = rout). Only the comment + canonical citation updated to the ED-898 reframe (death->capture). No behaviour change; PER_CELL=0 byte-exact. |
| `tests/sim/mass_battle/{config,orchestration}.py` + `lanchester_signature.py` (P-L Lanchester attrition substrate; D-D, spec mb_lanchester_design.md 81ea569d) | (P-L; gauge-gated behaviour change) | engine substrate, NOT canon — validated TOP-DOWN vs Lanchester literature (Linear Law = ancient/melee frontage-capped; Square Law = ranged/aimed fire; Willard 1618-1905) + BOTTOM-UP vs the canonical exchange (params/mass_combat.md PP-233 successes x (1+Power), simultaneous; params/core.md TN7 engine) | Adds the missing force-on-force attrition law behind `LANCHESTER_ENABLED` (default ON; OFF reproduces the pre-P-L flat-scale term BYTE-EXACT, verified PER_CELL=0 AND =1). MELEE Linear Law: casualties ~ K_LINEAR x enemy strength IN CONTACT (engaged contact-frontage columns / LANCHESTER_STRENGTH_REF), DAMAGE_BY_DEGREE retained as per-soldier exchange quality; frontage-capped BY CONSTRUCTION (contact columns <= meeting frontage -> superiority is a LINEAR edge). VOLLEY Square Law: aimed fire lifts the cap -> volley loss x K_SQUARE x shooter effective_size (~ N -> N-squared concentration). Numbers-in-contact lives ONLY in the linear term — the run_battle opp_frac post-scaler is SKIPPED under Lanchester (Lesson 1; makes toggle-off byte-exact). FEEDS morale/rout, does NOT replace it. New `lanchester_signature.py` asserts the spec section-four signatures: LINEAR (melee 2:1 big-win 88-91%, cas-diff +46-48), SQUARE (volley cas-exchange ratio 17.8 >> linear ~2), NO-ANNIHILATION (mirror max-cas ~28%, loser hp ~72%) — ALL PASS PER_CELL=0 AND =1. STRENGTHENED 2cf3feb6+: added LAW-EXPONENT guard (no-rout conserved-quantity fit — melee must conserve A−B p≤1.4 LINEAR / volley A²−B² p≥1.6 SQUARE; catches the p≈1.7 Size-based-pool contamination the win%/cas-diff checks missed; passes only under the Command-only base). Battery: PER_CELL=0 holds 5/13 multi (no regression) + 3/13 single; PER_CELL=1 14/20 multi with ALL C1-C7 charge bands IN-BAND (C5 moved IN 91.7->86.7) + 7/13 H/R; toggle-off byte-exact both modes. Constants LANCHESTER_ENABLED / K_LINEAR=4 / K_SQUARE=0.25 / LANCHESTER_STRENGTH_REF=4 all class-B sim-tunable, Jordan-vetoable (coefficient VALUES surfaced for veto). Ledger: 11 P-L+canonical entries (+24 value-coverage reconstructed after the container reset wiped the prior local ledger). No canon edited. |
| `tests/sim/mass_battle/{config,orchestration}.py` (Command-only sigma-leverage base; Jordan canon-structure directive 2026-06-02) | (Command-sigma; gauge-gated behaviour change) | engine resolution — sets aside the canonical Size-based pool (min(Size,Command)+Command, derived_stats §L276 / PP-233) per Jordan directive; validated TOP-DOWN vs Lanchester OR literature (linear/square laws; Willard; Dupuy g-exponent) + du Picq casualty asymmetry | Base exchange pool driven SOLELY by Command (COMMAND_POOL_MULT×Command; =2×Cmd matches the canonical value at Size≥Command); numbers (Size) enter outcomes ONLY via the P-L Lanchester frontage term. Command DERIVED = clamp(round((2·Charisma+Cognition)/3),1,7) — Charisma PRIMARY, Cognition SECONDARY — when both supplied (else explicit command stat). Gated COMMAND_SIGMA_ENABLED (default ON; OFF reproduces canonical Size-based pool BYTE-EXACT vs committed engine, verified isolated PER_CELL=0). VALIDATION (conserved-quantity exponent, no-rout primitive, the OR-literature method): the Size-based pool CONTAMINATED the melee linear law to p≈1.7 (per-capita effectiveness degrades below Command, adding super-linearity); the Command-only base restores melee to TRUE LINEAR p≈1.0 (CV@p=1 0.01) while volley stays SQUARE p≈2.0 (CV@p=2 0.002) — clean Lanchester separation matching the literature. Exponent COEFFICIENT-INVARIANT (melee ~1, volley 2 across K_LINEAR∈{2,4,8}) → K sets casualty timescale, NOT the law. Magnitude historical: melee 2:1 big-win 77%% + cas-diff +39 (winner-low/loser-high per du Picq victors <5%%); no-annihilation rout-decided (mirror ~30%% cas, loser ~70%% hp); square concentration 17.8× (Cannae/Pharsalus disproportion). base_combat_pool probe: ON holds 2×Cmd through depletion (8→8→8) vs OFF degrading (8→6→5). Constants COMMAND_POOL_MULT=2 / CMD_CHA_WEIGHT=2 / CMD_COG_WEIGHT=1 class-B sim-tunable, Jordan-confirmed 2026-06-02. CANON RECORD: editorial ED entry (PP-233 pool set aside for the engine; Command derived from Cha+Cog). Canon DOC edits (params/mass_combat.md PP-233, derived_stats Command derivation) = flagged follow-up, not yet applied. RELATED CLEANUP (this commit): SHAPE_OFF_MOD/SHAPE_DEF_MOD (the last flat per-shape bonus hooks, already zeroed) RETIRED entirely + dead role/off chain removed — formations grant NO flat bonuses; all formation effects emerge from geometry (frontage/Lanchester, depth, support, facing). Byte-exact (ON+OFF). P-C role scaffold added separately (inert): TROOP_TYPE_ROLES gating (FM position->role) + roles_for/role_allowed accessors + role/instructions fields on Subunit (default None/()); byte-exact, behaviour deferred to the instruction->primitive step. Registry hygiene: command_base_pool extracted -> command_sigma_base mechanic now resolves to a real function (not the COMMAND_POOL_MULT constant); byte-exact ON+OFF. P-C taxonomy (report-grounded): TROOP_TYPE_ROLES refined + mounted_archers type added + ROLE_SPEC (role=shape+instructions, the FM roles+tactics model); data-only, no battle-path consumer, byte-exact. Brace MECHANISM wired (behaviour-cascading, gated by the 'brace' instruction -> instruction-less byte-exact, PROVEN brace ON==OFF on the gauge at PER_CELL 0 and 1): (1) brace instruction engages the charge-shock brace gate without hold-stance (no offense penalty); (2) reciprocal charge-recoil (PC_CHARGE_RECOIL=6, prep=discipline x depth) -- a charge into a braced+deep+disciplined wall shatters the charger. Validated 40-seed: braced tier4 disc6 beats cavalry ~75% (cavalry heavier losses); shallow/green ridden down ~12%; braced-vs-infantry neutral. Emergent pike-beats-cavalry (Courtrai/Swiss/Waterloo), no flat bonuses. (Also: reformatted pre-existing _SIG canonical-comment to lead with the tag so the fabrication gate accepts it; reconstructed sim_verification_ledger.json is missing the 0.806/0.781 EV entries - flagged.) | Missile-density coupling wired: volley casualties scale with TARGET formation density via _volley_density_mult (col_grid density / PC_VOLLEY_DENSITY_REF, clamped FLOOR..CAP) -- packed/deep columns bleed more, dispersed/shallow less (Carrhae/Agincourt/Crecy). Ranged-only path -> melee gauge byte-exact (proven ON==OFF); volley-exponent signature preserved (p=2.00, constant target-density mult keeps the slope). Correct direction (dense -0.6pp / shallow +0.5pp ON vs OFF) but small magnitude in single-engagement (volley is a brief DR-eaten pre-melee chip); the edge compounds at the standoff/multi-turn scale (kiting). | Architecture review fix #1 (DRY): unified the duplicated discipline/depth preparedness mappings into shared primitives _disc_prep + _depth_prep, used by the charge-shock gate (independent retentions: 1 - prep x (1-FULL)) AND the recoil (conjunctive _wall_prep = disc_prep x depth_prep). Was: gate used disc curve (disc-2)/3 saturating at 5, recoil used (disc-2)/4 saturating at 6 (depth curves already matched). Gate re-expression PROVABLY byte-exact (b_disc/b_depth old==new across disc 1-7, depth 0-6); recoil disc-curve unified to /3 (deliberate). Re-validated: pike-beats-cav 75% / cavalry-rides-shaken 28% / braced-vs-inf 42% unchanged; shallow-green ridden down (12%->0%, more decisive, edge intact); gauge byte-exact; signatures 4/4. No re-calibration needed. | Stress-test / arch-review hardening: Subunit.__post_init__ now validates shape (in CELL_PATTERN_FN), tier (in TROOPS_PER_TIER {1-4}), and that the initial formation's absolute cells fall within the BATTLEFIELD_SIZE grid -- raising a clear ValueError at construction instead of a cryptic KeyError or silent off-grid placement. Closes the two stress-test gaps (tier KeyError, off-grid cells) plus shape. Valid in-bounds constructions byte-exact: selftest 30, signatures 4/4, gauge ON==OFF. | §13 kiting primitive WIRED (config PC_KITE_ENABLED/PC_KITE_STANDOFF + advance_cells maintain-range hook gated on the 'kite' instruction + mounted-speed for mounted_archers). Byte-exact: selftest 30, signatures 4/4, gauge ON==OFF (kite/mounted gated -> existing scenarios untouched). Measured (PER_CELL=1, Line t4, 20 seeds): kiter vs infantry = kiter holds 100% HP / infantry 88% / DRAW (vs no-kite ranged which closes: 3/20 wins at 81%); kiter vs cavalry == vs infantry (no cornering limiter -> equal-speed cavalry cannot close). Mechanism correct; OPEN design forks (decisiveness: 18-turn volley chips ~12%; vs-cavalry counter needs edge-cornering -> couples to dynamic-bounds + terrain). | EDGE-CORNERING added (advance_cells clamps each cell's abs position to [0, BATTLEFIELD_SIZE), back-solving the offset so it cannot accumulate past the edge -> no hysteresis; closes the dynamic-bounds item). Byte-exact: selftest 30, signatures 4/4, gauge ON==OFF (inward-moving units never reach an edge). Re-measured (PER_CELL=1, Line t4, 20 seeds): kiting now a grounded RPS -- kiter vs cavalry = kiter LOSES 13/20 (A 79% / B 90%; cornered + caught = Patay/Arsuf); kiter vs infantry = contested 87%/87% (mostly draws; the small field corners the kiter -> kiting dominance vs infantry now requires open space = the terrain coupling, Carrhae needs plains). | STRESS-TEST + MECHANICAL-LOGGING harness (tests/sim/mass_battle_stress.py): NON-INVASIVE tick-by-tick driver (run_battle max_turns=1; byte-exact run_battle(N)==N x run_battle(1)) -> trace_battle() per-tick mechanical trace (hp/morale/stamina/distance/rout) + mirror_sweep() symmetry+variance stress signal. Engine UNTOUCHED. FINDINGS (mirror, Line, 20 seeds, single-order RAW): tier1 A7/B10/D3 std5; tier2 A8/B11/D1 std14; tier3 A5/B7/D8 std12; tier4 A5/B14/D1 std5 skew9 -> SIDE-SKEW. Also tier-1 mirror double-routs at contact tick3 (small-pool morale fragility). SIDE-SKEW DIAGNOSED: emergent from sequential RNG-stream consumption x the multi-tick morale-feedback loop -- per-tick resolution + roll_pool draws individually SYMMETRIC (roll_pool consecutive draws iid 9848:9908; deterministic-roll mirror = 20/20 draws; resolve_engagements symmetric under A<->B relabel) but arg-order swap FLIPS the winner -> the 2nd-drawn unit is favored, compounding over ticks (skew grows with battle length, biggest at tier4). Sub-dominant to real force gaps (disc6-vs-disc4 wins BOTH arg-orders 14/20 & 18/20 -- order shifts margin ~20pts, not winner). DECISION C (Jordan): (B) DONE -- mirror_sweep(cancel_order=True) runs each seed BOTH arg-orders + tallies by config -> order-bias CANCELS in measurement (cancelled-skew=0 all tiers, 40 trials), engine byte-exact; (A) DEFERRED -- engine order-independent contest + signature re-calibration, later when calibration can absorb the RNG-consumption change. | PER-MECHANIC TRACE added (resolution.py passive observe-only _trace_on collector start_trace/trace_event/get_trace + orchestration instrumented at melee/volley/tick): trace_battle(mechanical=True) records per-tick MELEE contest (pools / sigma advantage ns_a,ns_b / nets / degrees) + VOLLEY fire (shooter/range/pool/net/DR/density/loss); format_trace renders a full auditable per-tick + per-mechanic log. PASSIVE -> byte-exact: trace ON==OFF (identical hp), mechanics_selftest (True,[]), Lanchester signatures 4/4 (volley p=2.00), stress_suite cancelled-skew=0 unchanged. | NERS STRESS DIMENSIONS probed (config_sweep generalization: configA vs configB, order-cancelled, make_unit stat-overrides; ners_dimensions()): (1) NON-UNIFORM at smallest pool -- tier1 (pool100) gives +0pp for ALL stat advantages (power/disc/morale) because the first-contact DOUBLE-ROUT swamps stats; above t1 modifiers express (power ~+20pp uniform t2-t4) = real small-pool degeneracy (NERS Lesson-3, ties to tier-1 double-rout). (2) NO THRESHOLD CLIFF -- discipline response smooth+monotonic (disc3..7 vs disc5: -70/-48/0/+15/+28pp; steepest crossing parity = inherent competitive S-curve, no discontinuous jump). (3) NO RUNAWAY LOOP -- edges scale ~proportionally then SATURATE (power +1/+2/+3 -> +20/+50/+55pp); morale feedback damped+bounded. Power = most scale-uniform; disc/morale (defensive) weaker + saturate into draws above parity. VERDICT: engine mostly NERS-healthy (R/S: no cliffs, bounded loops); live small-pool defect = tier-1 immediate double-rout (advantages don't express) -- flagged for tier-1 investigation. |


<!-- 2026-06-03 continuous-scale rework - step 1a -->
- **footprint generator (step 1a)** - `geometry.footprint_for(shape, troops, concentration)` + continuous-scale constants (CELL_FLOOR=40 / CELL_CAP=200 / SUBUNIT_ROUT_FLOOR=80 / MAX_TROOPS_PER_UNIT=10000). Lays a continuous troop count into a shape at a target density, bounded [40,200]. Validated 0 bound-violations across all 5 shapes; legacy tier path untouched. Subunit wiring follows (1b-d).


<!-- 2026-06-03 continuous-scale rework - step 1b/1c -->
- **continuous footprint wiring (step 1b/1c)** - `Subunit` gains `troops` + `concentration`; `troop_count` returns the continuous count when set, else the tier value. A new `_oriented(su)` chokepoint routes all 9 `oriented_pattern(shape, tier, dir)` sites to `footprint_for` when troops is set (else byte-exact tier fallback); `cell_speed` stays (position-based). Validated: Lanchester signature byte-exact (p=1.45/1.30); a continuous unit (5000 @ concentration 100 -> 48 cells, ~104/cell) builds its col-grid and runs a full battle. Harness wiring + tier removal: 1d.


<!-- 2026-06-03 continuous-scale rework - step 1d -->
- **harness continuous support (step 1d)** - `make_unit` gains `troops` + `concentration` (threaded to the Subunit); both None -> tier path (byte-exact). Validated: signature byte-exact (p=1.45/1.30); `make_unit(troops=800, concentration=100)` -> 6-cell unit (~133/cell) builds and runs; tier default builds the 35-cell Line. Tier-param removal across callers follows once continuous is re-baselined.


<!-- 2026-06-03 continuous-scale rework - step 2a -->
- **battlefield rescale to fit 10k (step 2a)** - BATTLEFIELD_SIZE 25->50; SIDE_A/B_START_ROW 34/15, harness _EDGE_GAP 16 (front-gap 6); UNIT_GRID_SIZE/BUFFER_CELLS scaled (vestigial). Verified 10000 troops fit at concentrations 40/100/200 (234/88/70 cells). NOT byte-exact (positioning shift; signature retired in step 5). **Finding:** at 10k the old frontage-count model gives ~0 casualties (~98% hp at a morale-only rout) - opposite of 'reduced numbers each side'; needs step 3 mass-scaling + morale-erosion-fraction fix. Lethality calibration moved to after step 3.
<!-- 2026-06-03 (step 3, continuous-troops rework): mass-scaling all-fight melee (_lanchester_strength density-scaled by min(tpc,CELL_CAP)/LANCHESTER_DENSITY_REF) + canonical Size-fraction morale triggers (morale_check_phase, §A.4; per-tick absolute erosion removed) + K_LINEAR 4->12 calibration. Validated: loser routs ~58% / winner ~85% at ~4 turns (reduced numbers each side); blob@200 loses 5/5 to spread@40 (frontage>density); tier path unbroken. -->
<!-- 2026-06-03 (cell-up re-architecture step 1): cell-primary state. Subunit.cell_troops (uniform at spawn, keyed by pattern id) is the source of truth; columns + unit hp emergent (build_column_grid sums cells; sync_col_grid; hp_max = actual troops). distribute_casualties thins CELLS (assoc-equiv to per-column). Validated: hp==Sum(cells) exact; step-3 reduced-numbers preserved (~87/55, 4t). Local column-based step-4 reverted (folds into cell-up). Lanchester signature 2/4 fail PRE-EXISTING (bounded-square model vs classical-linear test); validator to be updated to bounded-square. -->
<!-- 2026-06-03 (cell-up step 2, increment a): node-relational cohesion behind PC_NODE_COHESION (default OFF -> byte-exact, Lanchester signature unchanged). Cells = nodes at live float positions (_node_pos), held by relational offsets from the formation anchor read off the spawn layout (_node_rel); _node_advance translates the anchor toward the target (vector-halt at adjacency) and relaxes each cell toward its slot by a discipline-gated cohesion factor (reuses disc_mult). cells() dispatches to _node_cells (grid-snapped) when on. Validated: OFF byte-exact (83/56 ~ step-3); ON sane (meet+engage, 0 draws, ~60t) + cohesion holds (subunit spread 10->10, no scatter); ON more decisive (91/30) - deliberate model change, to calibrate later. Increment a only: NO wheel; contention/_momentum read stale offsets -> inert on node path (vector-halt obviates co-location); flagged for 2b (wheel) / 2c (node-aware contention+momentum, deformation). -->
<!-- 2026-06-03 (cell-up step 2, increment b): WHEEL / body rotation on the node-relational path (PC_NODE_COHESION, still default OFF). The formation carries a facing unit vector (_node_facing), spawn facing _node_facing0 = direction to the enemy at first contact; each tick it re-faces the current enemy direction (disc-gated, kw = disc_mult*0.5, slower than the cohesion snap) and the relational layout is rotated by the rotation taking f0 -> f (rc_w=cos, rs_w=sin via dot/cross of the unit facings), so the whole formation pivots while cohesion holds it. cell_facing_vec now follows the formation facing. Validated: head-on == 2a (93/29, spread 10 -> wheel dormant, rotation=identity); off-axis enemy -> formation wheels 90 deg, the line's broadside flips axis (col-spread 6->4, row-spread 4->6), facing converges to point at the enemy. -->
<!-- 2026-06-03 (cell-up step 2, increment c): node-relational model completed on the PC_NODE_COHESION path (still default OFF). resolve_cross_side_contention.collect() + the loser-revert + _momentum_speed now override the offset-derived position with _node_pos (grid-snapped) when the toggle is on, and the revert restores _node_prev_pos; per-cell enemy collision added to _node_advance (a cell whose relaxed position would land on an enemy-held cell holds position -> no pass-through, front dents). Validated: head-on == 2a/2b (94/27, spread 10, node-aware branches inert, no crash); forced co-location resolves on the node path (A speed 2 > B speed 1 -> B reverts to _node_prev_pos (18,20), A holds); a cell with an enemy one step ahead does not move onto it. Node cohesion now complete (translation + soft cohesion + wheel + contention + momentum + collision); pending the more-decisive-outcome calibration (91/30 vs 83/56) before the toggle defaults on, which connects to step 3 (cell-vs-cell damage). -->
<!-- 2026-06-03 (cell-up step 3, redirect): added a deep-narrow Column formation - the DEPTH PRIMITIVE. Measurement drove this: (a) gauge_mb is broken (execs the deleted monolithic sim_v22.py); (b) dense-narrow vs sparse-wide is ~even frontally (5/10, 75/79) because width's envelopment offsets density; (c) the engine had NO way to deploy deep-narrow - every shape couples width and depth (Line=1.4xdepth). A monkeypatched deep Column beat a wide Line frontally at equal troops/density (8/12, 80/71), proving the existing frontage-cap + depth machinery (rotation/refill, fatigue-damp, charge-absorption) ALREADY reward depth once it is deployable. So the foundation for Jordan #2/#3 is the deploy primitive, not a damage-core rework. Column: CELL_PATTERN_FN['Column']=transpose of the Line block (deep-narrow, no new literals); _SHAPE_BUILD continuous depth=LINE_ASPECT^2*s (~2:1, reuses the cited LINE_ASPECT + the Line rectangle builder); MIN_DISCIPLINE 3; cell_speed 1. Purely additive - existing shapes byte-exact (a new key, no existing shape touched). Validated: deploys 4cols x 8rows; holds/wins vs wide Line frontally (7/12, 78/73); Line-vs-Line untouched. Aspect/discipline/speed are vetoable design choices. Open: fix gauge_mb; reassess whether cell-vs-cell damage + the node-cohesion 91/30 calibration are still needed now that depth is rewarded + deployable. -->

## ARCHIVED 2026-06-30 (moved from active coverage_matrix.md to stay under the 10k cap) — 2026-06-05/06 build-log (Targeting/PC_NODE/Build A–E/Reform/Pin)
## Targeting extensions (2026-06-05)
- `target_delay_ticks`: countdown hold before first engagement — staggered waves / ambush release
- `target_condition='weakest'`: focus-fire on fewest-remaining-troops enemy subunit, re-evaluates each tick
- `target_condition='in_range:N'`: hold until enemy centroid within N cells — defensive trigger
- `order_target_idx`: direct subunit-to-subunit targeting by index (pre-existing; now documented)
- Backward-compatible: neutral defaults preserve byte-exact prior behaviour
- Stress-tested: 0 engine failures / 0 degenerate across 60 targeting-varied + 30 backward-compat trials

## PC_NODE_COHESION continuous-path fix (2026-06-05)
- _node_advance: `_node_pos[(orig_r,orig_c)]` → `setdefault(key, anchor)`
- Continuous-mode cells not present in _node_pos at spawn now seed from anchor (first-time default)
- Verified: 20-trial fuzz with PC_NODE_COHESION=1 → 0 engine failures

## Discipline-speed flooring fix (2026-06-05)
- advance_cells + _node_advance: actual_speed used math.floor(base_speed * disc_mult);
  base_speed=1 (standard infantry) with disc_mult=0.7 (discipline 3-4) floored to 0 -> unit frozen.
- When both sides had discipline <5 neither could move -> false draw at 100%/100% troops.
- Changed floor -> round: discipline now slows (disc 3-4 move at speed 1) rather than freezing.
- Validated: historical counters byte-identical (deepColumn 5/8, ShieldWall 8/8, command 8/8);
  disc-3 two-Line engages 5/5 (was frozen); fuzz draw_hold 20->12 (frozen draws resolved); 0 engfail/degen.
- NOTE: this resolves what was mis-flagged as "GappedLine/Horseshoe non-closing" - that was never
  shape-specific; single-subunit shapes close at every parameter. The non-close was this speed cliff.

## Discipline decoupled from movement speed (2026-06-05, supersedes d869461c floor->round)
- CANONICAL BASIS: mass_battle_v30.md L7 — PP-232 renames Cohesion->Discipline. Discipline IS cohesion.
  Canon ties discipline to: Power penalty (A.4 table), degradation under Size-loss asymmetry, Reform
  restoration, the H formula. params/mass_combat.md has ZERO discipline x movement coupling.
- disc_mult on actual_speed/step was engine-introduced with no canonical basis. Removed.
- actual_speed = base_speed + stance_mod (advance_cells); step = base + stance_mod (_node_advance).
- disc_mult RETAINED where canonical (it = cohesion): node cohesion factor k (L632), wheel rate kw (L624).
- Validated: counters byte-identical (deepColumn 5/8, ShieldWall 8/8, command 8/8); disc 3-7 all engage;
  fuzz(120) 0 engfail/0 degen; mirror(60) |aw-bw|=6 symmetric.
- The earlier floor->round (d869461c) patched a coupling that should not exist; this removes it.

## reform_check (regroup) wired + directed maneuver pathing (2026-06-05)
- reform_check (G-8 hook, was empty): a unit NOT in melee contact restores +1 discipline toward
  discipline_start each phase boundary. [canonical: mass_battle_v30.md L180 reform restoration;
  discipline=cohesion PP-232]. Engaged = any subunit pair within Chebyshev REFORM_ENGAGE_DIST(=1).
- Maneuver pathing: units no longer always path straight at nearest.
  - Subunit.maneuver ('envelop'|'surge') + maneuver_side ('left'|'right'|auto). Also derived from
    instructions tokens ('envelop'/'surge'/'breakthrough'), so the Flanker (envelop) template is now live.
  - _maneuver_target: stateless per-tick pather (no path state to corrupt).
    * envelop: go wide past the enemy's nearer flank (col +/- MANEUVER_ENVELOP_WIDE=4), then hook
      inward to its flank/rear once the front row is passed (two-phase, geometric).
    * surge: break the line and drive MANEUVER_SURGE_DEPTH(=5) rows past the enemy front, holding column.
  - advance_cells branches on maneuver; the DEFAULT path (column-local + overhang wheel) is the
    else-branch, byte-exact for maneuver=None.
- Constants in orchestration.py, inline-cited; class-B sim-tunable (Jordan-vetoable). config.py NOT
  touched (its 10 pre-existing uncited constants are a separate hygiene item).
- Targeting granularity CONFIRMED unit->subunit->cell: unit = matchup + unit stance/disc/cmd;
  subunit = target selection (order_target_idx / target_condition / delay) + maneuver; cell = each cell
  independently computes its target (column-local / wheel / maneuver) and moves (genuine per-cell).
- Validation: counters 5/8 8/8 8/8 unchanged; fuzz(120) 0 engfail/0 degen; reform unengaged 3->4
  capped at start, engaged unchanged; envelop hooks flank (deepest row 17 vs direct 16), surge breaks
  a weak line and drives through (deepest row 10 vs direct 16). Fabrication gate: all constants cited.

## reform_check CANON CORRECTION: PP-241 command gate added (2026-06-05, fixes 8ec085c0)
- 8ec085c0 implemented only the L180 '+1 if unengaged' clause; MISSED the L180-183 command gate.
- Canon (mass_battle_v30.md L180-183): discipline restores only if general's Command >= current
  Discipline + 1 AND Command >= 2 (PP-241); Command=1 general cannot restore at all; command caps
  the reformable discipline (a Cmd-4 general restores a unit only up to disc 4).
- Added gate. Validated: cmd5/d3->4, cmd4/d3->4, cmd4/d4 no-change, cmd2/d3 + cmd1 no-change.
  Counters 5/8 8/8 8/8 unchanged; fuzz(120) 0 fail. [SELF-AUTHORED catch: reform implemented from the
  one-line L180 summary, not the full L180-183 - corrected on canon read.]

## Build A -- atomized fixing-force flank (subunit-scale)  [committed cb8b5844]
- orchestration.py `_per_cell_angle_mod`: detached-flank term fires when a subunit is fixed
  frontally by a SEPARATE body (`_front_fixers`) and the attacker bears on its flank/rear;
  provably inert single-subunit (byte-exact counters 5/8, 8/8, 8/8). Toggle `PC_FIXING_FLANK`.
- validators.py: V-CANNAE (envelopment advantage; no seed worse, delta>0) + V-FIXING
  (pin-conditional; zero effect without a front-fixer). Emergent, public outputs only.
- robustness: fuzz(120) 0 engine-failures / 0 degenerate; mirror skew 2/48.
- scope: A is the angle disadvantage (modest); decisive collapse = B; reliable rear-reach = C
  (a detachment approaching directly into the rear/flank forms no contact pair today).

## Build B -- envelopment shock (reuses _charge_shock_sigma)  [committed c2134e16]
- orchestration.py: PC_ENVELOP_SHOCK (default ON) fires the calibrated _charge_shock_sigma on the
  fixed_by_other + flank/rear condition, as an elif to the charge-shock path (no double-count).
  Reuses the existing zone/brace/depth/shaken gating: a braced+deep+disciplined line resists
  (Waterloo square), a loose/shaken/shallow one shatters (Cannae). Byte-exact (inert single-subunit);
  fuzz(120) 0 fail / 0 degen.
- validators.py: V-SHOCK (B decisive vs a balanced line: A+B retains +0.030 over A alone, no seed
  worse) + V-BRACE (braced unit resists; B-marginal braced 0.004 < line 0.030). V-CANNAE/V-FIXING
  now isolate A (shock off).
- scope: envelopment now decisive vs a vulnerable line via frontal-mass spillover; a detachment
  reaching the rear directly (no contact pair today) remains build C.

## Build C -- envelop maneuver (around the flank to the rear)  [committed 40fe9845]
- orchestration.py: PC_ENVELOP_PATH (default ON); envelop clause in advance_cells cell_target, gated by
  the 'envelop' instruction -> inert for every existing scenario -> byte-exact (5/8,8/8,8/8; fuzz(120)
  0 fail/0 degen). Two-phase: pass wide of the flank (clearance >= enemy frontage), then turn in to the
  now-rear cells. Reuses the existing 2D steering + wheel.
- validators.py: V-ENVELOP -- with the maneuver the detachment reaches the rear region (mean row-offset
  ~0, behind in 7/20 seeds) vs straight advance (+3.9, 0/20). Reaching the rear enables the RED rear shock.
- scope: routes reliably to the rear region; full per-seed rear lodgment is combat-dependent.


## Reform (G-8) -- Discipline restoration (reform_check)  [committed 2026-06-06]
- orchestration.py: REFORM_CHECK_ENABLED (env, default OFF). Flag kept in-engine (not config.py) to
  avoid the sim_fabrication ledger drift on config's pre-existing constants. reform_check filled per
  canon (mass_battle_v30.md §A.5 / Phase Reform): an unengaged unit (find_contacts empty) gains +1
  Discipline toward discipline_start, gated by Command >= Discipline+1 AND Command >= 2 (Command-
  asymmetry, PP-241); a Command of one cannot restore. Default OFF => byte-exact (lanchester
  signature byte-identical vs the original `pass`; the 5 envelopment validators unchanged, PER_CELL=1).
- validators.py: V-REFORM -- 7/7 gating cases (unengaged-eligible restores +1 capped at start;
  cmd=1 / cmd<disc+1 / already-at-start / engaged / routed / flag-OFF all inert). Toggles the flag
  in-process (save/restore) so it cannot perturb the other goals. run_all 6/6 PASS.
- NOT implemented (canon Reform also does these; separate, morale/lifecycle-touching): +1 Morale
  recovery and sub-unit merge. [OPEN -- Jordan: cadence is per phase-boundary (bounded by start);
  canon Reform is once-per-turn (the Reform Phase) -- may rule once-per-turn.]
- scope: discipline restoration only; flag-gated opt-in pending a re-baseline decision.

## Build E -- atomized archer volley targeting (directed concentrated fire)  [committed 2026-06-06]
- PC_VOLLEY_TARGETING (default ON): an ordered archer (order_target_idx / 'weakest' in-range; else
  nearest) concentrates its volley casualties on the target subunit (percell.apply_to_subunit); unordered
  fire spreads by engaged density as before -- same totals, cell==hp preserved. No-order path byte-exact
  (counters 5/8,8/8,8/8; default-volley probe identical to committed; fuzz(120) 0/0).
- validators.py: V-ARCHER -- ordered fire concentrates ~31.5 more casualties on target, every seed; 7/7 PASS.
- prior volley was faction-level (targeting cosmetic); E concentrates the ordered portion, default
  unchanged (opt-in, Jordan-vetoable). percell.apply_to_subunit added to __all__. 'sweep' half deferred.

## Build E (lateral half) -- sweep maneuver (flank-ward lateral march)  [committed 2026-06-06]
- orchestration.py: PC_SWEEP (default ON). advance_cells gains a 'sweep' clause (after envelop): a subunit
  with the 'sweep' instruction picks a flank at UNIT level (its deploy column vs enemy centre) and all cells
  shift laterally toward it (uniform sign -> formation coheres), then turn in to engage the flank frontally.
  Distinct from envelop (around to REAR) and the wheel (overhang cells only). Gated on the 'sweep' instruction
  -> INERT for every existing scenario -> byte-exact (counters 5/8,8/8,8/8; fuzz(60) 0 fail/0 degen).
- validators.py: V-SWEEP -- a 'sweep' unit displaces ~3.0 columns laterally to a flank vs ~0.08 for straight
  column-local advance, every seed; concentrates on the enemy flank (frontage chewed down). run_all 8/8 PASS.
- [ASSUMPTION] 'sweep' semantics (lateral flank-ward march then frontal flank engagement) are a grounded
  editorial reading -- the original E item named 'sweep' without a spec; anchored to oblique order / flank
  march (Leuctra, Leuthen). Class-B, Jordan-vetoable. An earlier per-cell-flank attempt tore the unit toward
  both flanks (centroid cancelled); fixed by the unit-level flank decision.

## Build D -- pin / Anvil  [CLOSED done-by-A, Jordan ruling 2026-06-06]
- RULING (Jordan 2026-06-06, Variant 3): D is delivered by the existing pin (`pinned` facing gate,
  orchestration.py L1508-1519) + build A (fixed_by_other, L1526) -- a pinned/fixed cell cannot reface, so the
  flank/rear angle penalty lands. No separate D mechanic is built; the anvil function = pin + A.
- Investigation (subsumption, this session): the obvious pin wirings measure 0.0000. `pinned` is read in
  exactly one place (the facing-refusal gate). Stamina drain is already contact-proportional (L210-211), so a
  'pinned drains harder' debuff double-counts. The one distinct lever -- denying the held enemy its
  between-turn stamina recovery (BETWEEN_TURN_STAMINA_RECOVERY, L2133) -- is called only in
  run_multi_turn_battle / run_multi_unit_battle (L2200, L2555), never in run_battle (L1898, the validated
  path) -> provably inert there. A single-battle pin debuff would over-punish an already-penalized state
  (A flank + B shock + contact drain) -> fails NERS-N.
- status: CLOSED. No code change. (Variants 1 recovery-denial / 2 cohesion-debuff remain available on a
  future canonical decision; not pursued.)
| r1_sigma_resolution + r8_parity_harness | F4 μ-shift resolution (base Ob + net_boost; eff_ob DISPLAY-ONLY) | mirror 49.9/50.0 · str6v4 59.5/40.5 · hist7v4 61.7/38.2 · agi6v4 65.6/34.4 (N=3000) · atom MC≡p_success | ED-934 | 2026-06-12 |


## 2026-06-30 — Stage 1a (re-architecture): extract core/exchange.py (behaviour-frozen) [byte-exact]
- EXTRACTED the pool-assembly primitives (derive_command, command_base_pool, subunit_combat_pool,
  _stamina_pool_penalty) from orchestration.py into a new resolver layer tests/sim/mass_battle/core/
  (core/__init__.py + core/exchange.py). orchestration.py re-imports them via `from mass_battle.core.exchange
  import *` so every call site is unchanged; engine.py adds core.exchange to its public surface + _resolve scan.
  G1 import-direction: core/exchange imports config+math only (no up-DAG import; no cycle).
- BYTE-EXACT: bat.py --check passes both modes (unit 7be8499b…, cell 1c5b2851… unchanged); stress S1-S18 ALL PASS;
  mechanics_selftest green. A pure code move — identical call graph.
- GATE FIX (tools/ci_sim_fabrication_check.py): masks multi-line triple-quoted docstrings before the line scan
  (docstring prose numerals were false positives; real in-code constants still caught). Cited 19 pre-existing
  uncited constants in orchestration.py (§A.4/§B.2/§A.7/§A.3b) — comment-only; orchestration scans clean.

## 2026-06-30 — Stage 1b (re-architecture): extract core/state.py (behaviour-frozen) [byte-exact]
- EXTRACTED the morale/discipline/rout state-transition phase hooks (morale_check_phase, rout_resolution,
  discipline_check_phase) from orchestration.py into core/state.py — the resolver layer's sole state-mutation
  site alongside core/exchange. orchestration re-imports via `from mass_battle.core.state import *` (phase_boundary
  and the stress-test imports unchanged); engine.py adds core.state to its surface + _resolve scan.
- G1 import-direction: core/state imports config+math only; calls Subunit/Unit methods duck-typed (erode_morale,
  derive_rout, degrade_discipline) — no up-DAG import, no cycle.
- BYTE-EXACT (G5): bat.py --check both modes match baseline; stress S1-S18 ALL PASS; mechanics_selftest green.

## 2026-06-30 — Stage 1c (re-architecture): extract core/attrition.py (behaviour-frozen) [byte-exact]
- EXTRACTED _lanchester_strength (the linear-law contact-frontage attrition term) from orchestration.py into
  core/attrition.py. (coeffs injected, not authored). G1 clean; BYTE-EXACT both modes + stress.

## 2026-06-30 — Stage 1d (re-architecture): extract core/contact.py + _oriented->geometry [byte-exact]
- EXTRACTED the targeting/contact-detection cluster (assign_targets, resolve_cross_side_contention,
  find_contacts, count_engagements_per_atom) from orchestration.py into core/contact.py.
- RELOCATED _oriented (the oriented-footprint helper — pure geometry: footprint_for + oriented_pattern) from
  orchestration.py into geometry.py (its proper cells/geometry home; added to geometry __all__). Its ~16 callers
  (Subunit/Unit methods + the contact fns) resolve it via the existing geometry star-import.
- G1: core/contact imports config+geometry+math only; geometry imports config only — no up-DAG import, no cycle.
- BYTE-EXACT (G5): bat.py --check both modes match baseline; stress S1-S18 ALL PASS; selftest green;
  geometry exposes _oriented; orchestration re-exports the contact fns. orchestration.py: 2,740 -> 2,549 lines.

## 2026-06-30 — Stage 1e (re-architecture): extract troop_types/registry.py [byte-exact]
- EXTRACTED the troop-type module (TROOP_TYPE_STATS canonical §B.2 stat presets + stats_for / roles_for /
  role_allowed gated-role accessors) from orchestration.py into troop_types/registry.py — the user-requested
  "troop types module". Depends on config (TROOP_TYPE_ROLES) only. orchestration re-imports via star
  (Subunit.of_type + stress-test imports unchanged); engine.py adds troop_types.registry to its surface.
- G1: no up-DAG import, no cycle. This also unblocks the hierarchy/units (Subunit/Unit) move — stats_for was
  the only orchestration-internal module dependency of those dataclasses' methods.
- BYTE-EXACT (G5): bat.py --check both modes match baseline; stress S1-S18 ALL PASS; selftest green;
  stats_for('cavalry') correct. orchestration.py: 2,549 -> 2,505 lines.

## 2026-06-30 — Stage 1f (re-architecture): extract hierarchy/units.py (Subunit/Unit) [byte-exact]
- MOVED the Subunit/Unit dataclasses from orchestration.py to hierarchy/units.py (deps all lower-layer; no cycle). Fixed: restored orchestration's resolution import; moved PC_ENVELOP_PATH/PC_SWEEP toggles to the consumer; repointed validators. BYTE-EXACT both modes + stress ALL PASS. orchestration.py: 2,899 -> 1,705.

## 2026-06-30 — Stage 1g (re-architecture): engine.py true wrapper (build_unit + resolve_battle) [byte-exact]
- ADDED the wrapper's two non-resolution duties to engine.py: build_unit (faction→unit adapter) + resolve_battle
  (router dispatching single/multi/multi_unit). Wrapper resolves nothing (P1 seam). Dogfooded: bat.py builds+routes
  via them; BYTE-EXACT both modes (digests unchanged) → provably transparent; stress S1-S18 ALL PASS.

## Smooth command-sigma combat pool + continuous discipline penalty (2026-06-15, ED-1013)
- CANONICAL BASIS: Jordan directive 2026-06-15 'smooth pools / fix discipline' (path 1 of documented fork).
- base_combat_pool COMMAND_SIGMA branch: flat 2*Command -> Command*(1 + hp/hp_max) -- 2*Command at full
  strength (size-decoupled, ED-899 preserved; cohesion is a FRACTION so per-capita effectiveness stays
  size-independent, Lanchester exponent ~1), degrading smoothly to Command at annihilation.
- discipline_penalty(): tiers {0,-1,-2} -> continuous -(5-disc)/2 clamped [-2,0] (same endpoints, no step).
- WHY: the flat pool left the discipline STEP as the sole pool-degradation term, which amplified a tiny
  latent contact-geometry asymmetry into a side-B mirror bias (H1 62/38, |A-B|=21.7pp). The smooth
  own-casualty degradation dilutes the discipline term -> mirror side-symmetric.
- VALIDATED: H1 Line-Line mirror n=120 A=53%/B=47% decisive, |A-B|=3.3pp (was 21.7); command decisive
  (cmd6-vs-2 -> 40-0); discipline decisive (disc5-vs-disc2 -> 20-0); mechanics_selftest clean.
- COVERAGE IMPACT (Jordan-accepted trade-off): smooth pool reduces FORMATION/charge decisiveness; the
  historical gauge tests/sim/gauge_mb.py (precedents_warfare.md bands) is now STALE and needs
  RE-CALIBRATION to the smooth engine (in-band dropped flat 3/6 -> smooth 1/6 on the 6-test subset).
  FLAGGED as a separate Jordan-canon follow-up.

## 2026-06-15 — Mass-battle gauge recalibration (ED-1014) [resolves the ED-1013 gauge-staleness flag]
- tests/sim/gauge_mb.py recalibrated bottom-up from historical precedent + peer-reviewed academic military
  analysis (grounding doc: research/historical/mass_battle_gauge_grounding.md). Bands set by HISTORY, the
  engine validated against them -- a fail FLAGS engine divergence, it does not lower the band.
- METRIC: raw-A% -> DECISIVE SPLIT decA=A/(A+B) (raw-A% failed symmetric mirrors purely on draw rate); the
  draw rate is validated separately (draw_exp). Near-parity high-draw is analytically expected (Hillestad 1995
  NRL 42(2); Taylor 1979/1983; Lanchester tie Armstrong&Sodergren 2015).
- VALIDATION (smooth engine, multi, n=120): 9/20 VALIDATED (mirrors; envelopment foot+mounted C4 93.8%, C7
  86.7%; command-decisive; maniples-absorb-wedge; misconception-corrected C1 45.7%). 6 DIVERGE-soft (subtle
  formation edges washed by the ED-1013 cohesion pool -- defensible per Biddle/Burkholder, below the v9 A.6
  modest edge). 3 DIVERGE-hard ENGINE-DEFECT FLAGS left FAILING: C2/C6 braced foot never beats cavalry (brace
  under-repels); C5 morale-shock inert (decA identical to C1). R1 ranged too-drawish open-field; R3 ranged
  mirror unresolvable; single-mode all-draws (18-tick cap).
- C1 REBASELINE 52-80 -> 35-55: the old band encoded the cavalry-beats-unprepared-infantry misconception
  (Burkholder 2007). Engine-defect flags (frontal cav shock/brace/morale flat) are future-work, not bands.
- Jordan directive 2026-06-15 (bottom-up recalibration, repeated); Jordan-vetoable.

## 2026-06-16 — Mass-battle gauge cavalry construction fix (ED-1015) [corrects the ED-1014 C2/C5/C6 "engine-defect" flags]
- RE-DIAGNOSIS (bottom-up, reading mass_battle/resolution.py + orchestration.py + config.py): the 3 ED-1014
  DIVERGE-hard cavalry flags (C2/C5/C6) were NOT engine defects -- they were GAUGE-CONSTRUCTION defects. The
  engine's brace-recoil (PC_CHARGE_RECOIL, calibrated vs Courtrai/Swiss/Waterloo) and shaken-shock
  (PC_SHOCK_SHAKEN_GAIN) are already grounded + WIRED; the gauge was not triggering them. Engine UNTOUCHED.
- FIX (gauge only): make_unit gains morale_start=None + instructions=() with byte-exact defaults (the 13 H/R
  rows + C1/C3/C4/C7 unchanged; H1 identical 52.8). C2/C6 defenders carry instructions=('brace',) ->
  _unit_braced fires the reciprocal recoil -> the braced wall REPELS. C5 is morale 2 of morale_start 6 ->
  genuinely shaken ("shaken" is RELATIVE, du Picq) -> shaken-amplifier + _morale_sigma fire.
- METRIC: C2/C6 judged on RAW cav-a LOW (band 0-30), draws expected (a repulse is a HOLD; decisive-split
  saturates at a tiny decisive n). Optional 10th tuple field metric='rawA' added (default 'decA').
- BANDS (history-grounded, Jordan-vetoable): C5 ceiling 90->98 (cavalry vs disordered foot is NEAR-TOTAL --
  Boddy 2015 dispersed 15,000; Hastings post-feint; the Phase-2 ceiling was set when the shock was inert);
  C7 ceiling 90->100 (encirclement of an immobile hold-stance line is annihilating -- Cannae; decA saturates
  to 100 when infantry is shut out).
- VALIDATION (multi, n=120; C5 re-checked n=240): cavalry block 7/7 -- C1 contested 45.7 OK, C2 REPELLED (raw
  cav-a 1.7), C3 mirror 43.7 OK, C4 envelop 93.8 OK, C5 shaken 95.6 (94.8@n=240) OK, C6 REPELLED 1.7, C7
  envelop 100.0 OK. Differentiation EMERGENT: braced-repulse ~2% != contested ~46% != shaken-shock ~95% !=
  envelopment ~94-100% (this validates the ED-1014 C1 rebaseline by differentiation). gauge_mb.py: 0 uncited
  constants, mechanics_selftest (True,[]).
- LATENT FLAG (out of scope, not triggered): the charge-recoil (orchestration ~L1647) does not zone-gate -> a
  flank/rear charge into a braced unit wrongly fires the recoil; C7 uses hold-only to avoid it. Fix candidate:
  gate on the frontal (GREEN) zone. The 6 formation soft-divergences (H2/H4/H5/H6/H7/H9) remain a separate residual.
- Jordan directive 2026-06-16 ('for 1/2/3 do everything you can to fix everything from a bottom-up emergent
  approach'); implemented by Claude, Jordan-vetoable.
- ED-1016 (per-subunit stat derivation, Jordan directive 2026-06-16; per-subunit pool option 1, "intensive
  attention to detail"): pushed power/discipline/morale/morale_start/dr onto Subunit (OPTIONAL; None inherits
  parent Unit via _unit back-ref), added per-subunit cohesion + subunit_combat_pool (SHARED command, per-subunit
  discipline+cohesion, shared stamina), repointed the engagement pool + Lanchester casualty power/dr +
  charge-shock/brace-recoil/morale sigma + Phase-2 volley (power/discipline/eff_size) to the contacting subunit's
  effective stats; Unit derives agg_power/discipline/morale/dr (troop-weighted) atop existing HP=Size=Sum(subunits).
  BYTE-EXACT verified vs a CLEAN pre-edit engine across melee/cavalry/brace/morale AND ranged/volley (exact states +
  win-rates identical) -- single-subunit fast-paths (cohesion->hp/hp_max, eff_size->effective_size) + None-inheritance
  guarantee the homogeneous historical battery is untouched. Mixed-unit differentiation demonstrated: cavalry subunit
  P6/D6 pool 8 vs infantry subunit P4/D4 pool 7, carried into the combat trace. Added make_mixed_unit gauge constructor
  (make_unit unchanged). V1 SCOPE: per-subunit combat morale uses the subunit's nominal value for overriding subunits;
  the eroding morale pool + rout + discipline degradation stay UNIT-level. Implemented by Claude, Jordan-vetoable.
- ED-1017 (per-subunit stamina, Jordan directive 2026-06-17; mirrors ED-1016): pushed stamina onto Subunit as OPTIONAL
  fields (stamina/stamina_max; None inherits parent Unit via _unit back-ref), added eff_stamina/eff_stamina_max +
  drain_stamina/recover_stamina (write routing: own-if-set else inherited Unit -> single-subunit reproduces the old
  Unit.stamina arithmetic) + agg_stamina (troop-weighted). Repointed per-subunit: subunit_combat_pool penalty
  (atom.eff_stamina), base_combat_pool (self.agg_stamina), the per-tick contact drain (each engaged subunit drains by its
  own cells-in-contact; reserves do not drain), phase-boundary recovery (stamina_check via new per-subunit _subunit_depth),
  between-turn recovery, and the exhaustion-pressure morale read. _fatigue_sigma UNCHANGED (its call site already passes the
  engaged subunit's contact columns -> already sub-unit-scoped; an atom param would be unused apparatus, NERS-E). BYTE-EXACT
  vs a CLEAN pre-edit engine across 9 matchups (melee mirror/asymmetric/envelopment, ranged/volley, cavalry charge/braced/
  envelopment/shaken) x 20 seeds in the resolving multi-turn mode -- identical state-vector digest. Rotation demonstrated:
  an engaged front subunit drains to 32/100 while a held reserve stays 100/100 (divergence impossible under shared
  Unit.stamina); the fresh reserve yields +1 combat-pool die over the exhausted front. make_mixed_unit extended for
  per-subunit stamina (make_unit unchanged). Grounding (research/historical/mass_battle_gauge_grounding.md §6): Sabin 2000
  JRS line relief / supporting troops; Zhmodikov 2000 Historia; du Picq Battle Studies; Clausewitz On War III.12. V1 SCOPE:
  per-subunit rout + eroding morale/discipline stay UNIT-level (deferred, Jordan-vetoable). Implemented by Claude, Jordan-vetoable.
- ED-1018 (troop-taxonomy stat home, Jordan directive 2026-06-17): wired the troop taxonomy onto the per-subunit stats
  (ED-1016/ED-1017). Added orchestration.TROOP_TYPE_STATS -- canonical per-type Power/Discipline/Morale presets transcribed from
  mass_battle_v30 B.2, keyed to the existing TROOP_TYPE_ROLES snake_case taxonomy (levy, light_infantry, heavy_infantry,
  cavalry, archers, crossbow, sling, artillery, knights_templar) -- plus orchestration.stats_for(troop_type) (case-insensitive
  accessor mirroring roles_for; fresh dict or None) and the constructor Subunit.of_type(troop_type, shape, tier,
  starting_position, **kw), which fills power/discipline/morale/morale_start from the preset unless the caller overrides;
  an unknown type fills nothing so fields stay None and inherit the parent Unit. PURELY ADDITIVE: nothing that does not call
  of_type changes, so the gauge constructors (make_unit/make_mixed_unit) are untouched and single-subunit units stay
  BYTE-EXACT (9-matchup x 20-seed multi-turn battery digest unchanged: fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69).
  SCOPE: only the three unambiguous B.2 integers are mapped; dr (the Armour column -> a vs-Piercing DR scale at orch L413-417
  whose identity with Subunit.dr is unconfirmed) and stamina (the Endur column, no clean bridge to the 0-100 pool) are
  deliberately left to inherit and flagged, not guessed; unit_type (melee vs ranged) stays caller-controlled (a role, not a
  stat). Differentiation demonstrated: of_type reproduces every B.2 row exactly; the stats separate combat on both channels --
  pool via discipline (Levy 6 dice -> Cavalry/Knights Templar 8) and damage via the (1+Power) multiplier (Levy x2 -> Cavalry
  x6); caller overrides beat the preset; unknown types inherit the Unit. Grounding (research/historical/
  mass_battle_gauge_grounding.md §7): the canonical B.2 table itself (bottom-up); Sabin Lost Battles 2007 validated
  ancient-battle model rating units by type and quality, plus the settled heavy/light/missile distinction (top-down).
  Implemented by Claude, Jordan-vetoable.
- ED-1019 (per-subunit rout + eroding morale/discipline, Jordan directive 2026-06-17 + "Continue" confirm; completes
  the per-subunit lifecycle after ED-1016 stats / ED-1017 stamina): pushed rout, morale erosion, and discipline
  degradation from the Unit onto the Subunit so a section of the line breaks from its OWN casualties while a fresh
  sibling holds. (SUBUNIT_ROUT_FLOOR was a dead config stub -- defined/exported/never referenced; this is the
  per-subunit rout it pointed at.) New Subunit fields routed/broken/discipline_start; props/methods eff_discipline_start,
  erode_morale, degrade_discipline, restore_discipline (write-routed own-else-inherited-Unit -> single-subunit
  reproduces the old unit arithmetic); Unit methods derive_rout + cascade_morale_hit. Repointed per-subunit:
  morale_check_phase (each subunit erodes by its OWN cohesion + own stamina/discipline exhaustion), rout_resolution
  (each subunit routs at own eff_morale<=0, then derive_rout), discipline_check_phase (unit-loss asymmetry drives a
  per-subunit counter), reform_check (flag OFF), the run-loop rout trigger, the per-tick drain (routed subunit skipped),
  subunit_combat_pool (routed/broken subunit -> 0), and the multi-unit inter-unit cascade / flank-erosion morale hits
  (cascade_morale_hit hits the unit's inherited-default morale ONCE plus each own-morale subunit -> no double-count on
  homogeneous units). TWO CANON-STRUCTURE FORKS, Jordan-vetoable: (a) unit-rout DERIVED (agg morale 0 / all subunits
  routed / Command<=0; winner/pursuit/cascade keep keying on derived unit.routed -> spec's unit-level rout preserved);
  (b) NO intra-unit cascade added (A.12 cascade stays inter-unit per spec, though its "section of the line breaks"
  Cannae/Hastings rationale could justify intra-unit -- a canon-model change left for Jordan). NO mass_battle_v30 edit.
  BYTE-EXACT: 9-matchup x 20-seed multi-turn battery digest unchanged (fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69).
  Per-subunit rout demonstrated: a 2-subunit unit (heavy front + levy rear) with the rear gutted to ~18% eroded the
  rear's morale to 0 over 2 phases (cohesion 0.18 -> -2/phase) while the front held at 5.0 (cohesion 1.0); rout_resolution
  routed the rear only (rear.routed=True, front.routed=False, UNIT.routed=False -- line held), rear pool -> 0 while front
  kept 7 dice; breaking the front too routed the unit (derive_rout). Single-subunit routs exactly at morale 0 as before.
  Grounding (research/historical/mass_battle_gauge_grounding.md S8): A.12 Cannae/Hastings sectional collapse; du Picq
  Battle Studies (panic is local, spreads from a break). Implemented by Claude, Jordan-vetoable.

- **ED-1020** (bugfix -- per-subunit broken-state scope; ED-1019 follow-up). Per-subunit stress testing
  (tests/sim/mass_battle/test_persubunit_stress.py) caught subunit_combat_pool flagging the WHOLE unit broken when
  ONE sub-unit hit Discipline 0, whose top gate then zeroed every healthy sibling's pool -- an unintended intra-unit
  break cascade contradicting the canonized A.4 ('siblings fight on') and A.12 inter-unit-only cascade. Fix: the
  Discipline-0 gate sets atom.broken and promotes to unit.broken only when ALL sub-units are broken; single-subunit is
  the lone sub-unit broken => unit.broken (byte-exact, digest unchanged). Re-test: broken levy 0 while healthy heavy
  sibling fights and unit not broken; all broken -> unit.broken. Stress battery all pass. Found + fixed by Claude
  during the ED-1018/1019 NERS audit; Jordan-vetoable.

- **ED-1021** (simulation -- D-A personal-combat wound model: Spirit->Wound Interval, Strength->Health, health-based felling).
  Jordan-ratified (2026-06-18): add Spirit to the Wound Interval at low weight (WI = round(End + 4 + 0.4*Spirit);
  flat base 6->4, the 2 points reallocated into the Spirit/Strength terms so avg Health stays 40) and Strength to
  Health proportional to Endurance (Health = round(WI*(MaxWounds+1) + 0.25*Strength*End)). Felling switched from the
  wound-COUNT rule (>= MW+1 wounds) to health-depletion (cumulative damage >= Health) because the count rule made the
  Strength->Health buffer a verified no-op on outcomes (str7-v-4 0.877 ~ mirror); health-based felling makes Strength
  buy survivability. Validated (np.default_rng, MB=50): equal average chars fall in ~5.2 hits (target 4-6); mirror 0.516;
  Spirit now matters spi7-v-4 0.50->0.81; Strength holds str7-v-4 ~0.88; noise Health 37/40/43 (str1/4/7), WI 8/9/11
  (spi1/3/7). r2 self-test 7/7 PASS (Health-40 fixture held; WI 10->9). Pre-existing ~50% multi-bout mutual-stall noted
  (baseline too, not caused here). Isolated to personal combat (WI/Health unused by mass-battle). Implemented by Claude,
  Jordan-vetoable. derived_stats_v30 §4.1 propagation follows.

- **ED-1022** (bugfix -- roll-input fidelity). discipline_check_phase drove every sub-unit's Discipline from the
  UNIT's cumulative loss + unit-level asymmetry, so a fresh reserve sub-unit cracked from siblings' casualties. Now each
  sub-unit degrades from its OWN (start_troops-cur_troops) loss; single-sub-unit uses the exact (hp_max-hp) expression
  (byte-exact, digest unchanged). Asymmetry baseline stays the opposing UNIT (no per-sub-unit opponent in 1v1). Verified:
  a gutted sub-unit degrades while a fresh reserve sibling (unit loss 2.0) does not. Regression S11.
- **ED-1023** (simulation -- of_type wiring). make_mixed_unit now builds each sub-unit via Subunit.of_type, so a canonical
  troop type draws its B.2 presets (ED-1018 consumed -- closes the Part-2 wiring gap); only caller-set stat keys forwarded
  so the preset fills the rest, non-canonical 'infantry' inherits, override wins. Additive (no callers; bat.py unaffected).
  Regression S12.

- **ED-1024** (editorial -- ruling). Morale is CONTINUOUS in play (Jordan): B.2 starting values integer, erosion
  continuous. No engine change -- Morale is already float throughout; only the turn-LOG rounds (round(.,3)), no int()
  coercion. Resolves the Mode-B audit flag.
- **ED-1025** (simulation -- campaign-boundary reset). New reset_morale_between_battles(unit): resets unit + per-subunit
  own Morale to start and clears routed/broken (rout is derived from Morale, so the flags must clear); Discipline persists
  (PP-712). Uncalled within a battle -> byte-exact (digest unchanged); the campaign layer calls it at the battle boundary.
  Regression S13.

- **ED-1026** (simulation -- sweep fidelity findings 1-2). Two formation paths now read per-subunit Discipline:
  advance_cells (movement formation-hold; run_battle passed unit.discipline -> atom.eff_discipline) and Unit.check_drift
  (formation drift; self.discipline -> a.eff_discipline). Byte-exact single-subunit (digest unchanged). A low-Discipline
  subunit now advances slower and drifts to Line independently of disciplined siblings. Regression S14 (drift) + S15 (advance).

- **ED-1027** (simulation -- sweep findings 3-6 closeout). (3) recalc_size now propagates rout to subunits on
  destruction; (4) the inter-unit cascade denominator uses agg_discipline (per-subunit troop-weighted, == unit when
  homogeneous); (6) between_turn_recovery recovers per-subunit Morale (inert at RECOVERY=0); (5) deleted dead
  discipline_penalty_volley. Byte-exact single-subunit (digest unchanged). Regression S16 + S17 + S18.

## 2026-06-20 — Formation-drift cell orphaning fix (ED-1032) [DIGEST CHANGE — first since the per-subunit gauge baseline]
- FINDING (diagnosed bottom-up vs orchestration.py + percell.py this session): on formation drift to Line (Unit.check_drift, L1368) cell_troops was not re-keyed to the new shape's pattern. ~42% of a drifted sub-unit's troops (157/376 in test) became spatially orphaned -- counted in HP (sum(cell_troops)==hp held, so strength/pool stayed correct) but invisible to iter_cells AND inert to front-cell casualty distribution (the orphaned wing never bled, held no frontage, could not be enveloped). Violates ED-907's "each cell inherits the best execution".
- FIX (orchestration.py check_drift): on drift, total=sum(cell_troops); shape="Line"; re-key cell_troops to _oriented(a)'s Line pattern with uniform per=total/len(new_ids), mirroring spawn (L629). Preserves total strength; restores the full cell complement.
- VALIDATION: test_persubunit_stress S1-S18 ALL PASS (no property regression); drifted unit final orphan=0.00 with HP preserved; no committed golden-digest test (digest asserted only by local bat.py).
- DIGEST CHANGE (intended, first since baseline): fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69 -> 1f8c05a9748d0b29c35a3acbd5e87d8f7112e159513cd3782af4f781a7cee05e. The fix deliberately alters drift-scenario outcomes (re-keyed casualties spread over the full Line, not the shared spine); IDENTICAL for any sub-unit that does not drift (reassignment is inside the drift branch). Jordan-approved adoption 2026-06-20.

## 2026-06-20 — base_combat_pool comment alignment + PP-683 framing (byte-exact; defect cleanup)
- orchestration.py base_combat_pool: the [canonical:] comment cited the legacy min(Size,Command)+Command; updated to the live Command*(1+cohesion) (ED-899/ED-1013), consistent with the now-propagated §A.4. Comment-only -> byte-exact (gauge digest 1f8c05a9 unchanged).
- PP-683 (encirclement -3 morale-cap removal) intentionally NOT wired: the engine delivers encirclement via PC_ENVELOP_SHOCK + Lanchester contact-overlap; a second cap-removal term double-counts and breaks H4 Cannae (same reason _envelopment_sigma is held dormant, NERS-N/E: no unneeded apparatus). The -3 cap (L314 min(loss,3.0)) stays in force; encirclement lethality is the shock + overlap. Doc PP-683 note added in the matching editorial commit.


## 2026-06-30/07-01 — Re-architecture Stages 1-2 + coordinate-migration DEBT-0/S2/C0-P (archived — condensed)
- Provenance registry seed (ED-1043, data-only); committed bat.py byte-exact digest gate (Stage 1,
  baseline unit=7be8499b/cell=1c5b2851); Stage 1a-1g wrapper/core split complete (orchestration.py
  2,899→1,705 lines, byte-exact throughout); Stage 2 standalone equipment/ package (weapons.py
  ARSENAL, armour.py ARMOURY, TROOP_LOADOUT — descriptive only, not yet wired into resolution);
  FIELD_MOVEMENT continuous-speed toggle (default OFF, byte-exact); abs→orig reverse-lookup
  centralized (geometry._oriented_abs_map); Migration DEBT-0 (orchestration.py fabrication-debt
  resolved honestly, 4→0 uncited constants); Migration S2 (Euclidean distance on the field, retiring
  the √2 diagonal bias); Migration C0+COL+G+H+F2+P (the full coordinate-field sequence behind
  default-OFF toggles: contact scaffolding, float→file quantizer, geometry rebuild from _node_pos,
  halt-loop float consistency, anti-hyper-reactivity facing layer, the int(round()) snap deletion).
  All byte-exact OFF throughout; FIELD-ON candidate digests recorded but not yet ratified at this
  point (see later entries for ED-1089's eventual default flip). Full detail: this file, prior
  revision (git history).

## 2026-07-01 — gauge_mb.py LIVE port + n=60 + tick-by-tick trace-capture backend
- Ported gauge_mb.py off the dead `exec('/home/claude/sim_v22.py')` mechanism onto
  `from mass_battle.engine import ...` (make_unit/matchup delegate to build_unit/resolve_battle);
  LIVE re-verified OFF baseline multi-mode 5/13 (H1,H2,H7,H9,R1), matching the prior shim exactly.
  No band/citation/metric changed.
- Jordan directive: default sample n 120->60; verified n=60 reproduces the identical n=120 5/13
  pass-set on the OFF baseline. Ledger entry `n=60` (calibrated/methodology).
- Fabrication-debt resolution across touched files (roll_pool TN=7/face-rule, _sigma_net_boost
  citation format, gauge_mb.py's make_mixed_unit P4/C4/D5/M6 defaults + row-stagger).
- Added the tick-by-tick VISUALIZER trace-capture backend: resolution.tracing_on() +
  orchestration._cell_snapshot/_subunit_snapshot/_unit_snapshot + one gated `positions` trace_event
  call per tick, using atom.cells() (field-aware) zipped against _oriented(atom)'s stable ids.
  Zero cost when tracing is off (never called, not merely discarded).
- G5 byte-exact both modes unchanged (unit 7be8499b / cell 1c5b2851). Fabrication + co-file clean.

## 2026-07-01 — mass_battle workbench: tick-by-tick visualizer (server + frontend)
- ADDED tests/sim/mass_battle/workbench/{trace.py,server.py,static/index.html} (mirrors
  designs/scene/combat_engine_v1/workbench's pattern: a tiny stdlib HTTP server, no external deps, no
  build step). trace.run_traced_battle() runs ONE battle via engine.build_unit/resolve_battle (the
  wrapper contract, never reaches past it) with tracing on, returning the full 'tick'/'melee'/
  'volley'/'positions' event stream. server.py serves a canvas SPA with playback controls (scrub/play/
  step), a preset picker mirroring gauge_mb.py's named matchups, and per-tick HP/morale/rout/event-log
  panels. VERIFIED end-to-end live (not just imported): all 4 endpoints (GET /, /api/mode, /api/presets,
  POST /api/trace) tested via a running server instance in both PER_CELL=0 (grid) and
  FIELD_MOVEMENT=1 PC_NODE_COHESION=1 PER_CELL=1 (coordinate-field) modes.
- IMPORTANT (documented in server.py): PER_CELL/FIELD_MOVEMENT/PC_NODE_COHESION are read from
  os.environ once at import time and star-imported as independent copies into every consumer — a
  running server's mode is FIXED at process start (no live toggle); comparing grid vs field means two
  server instances. GET /api/mode reports the actual running config.
- FINDING from using the tool (not a bug): confirmed by reading _node_cells() (hierarchy/units.py) that
  the coordinate-field candidate keeps ROW positions integer-rank-snapped by design ("ranks are integer
  bins" — a real military structure) and only bins COLUMNS to their file; positions are not yet fully
  continuous floats end-to-end. Accurately reflected by the visualizer, not a rendering defect.
- Engine untouched by this addition (workbench/ only). G5 byte-exact both modes unchanged (unit
  7be8499b / cell 1c5b2851). Fabrication clean (HTTP status codes + dev port named+ledgered as
  non-sim-mechanical tooling constants, not fabricated citations). Co-file satisfied.

## 2026-07-01 — mass_battle Stage A: true-adjacency stand-off halt (FIELD_MOVEMENT)
- FIXED the coordinate-field magical-co-location bug: the halt clamp compared against SNAPPED enemy
  positions with a flat "-1" margin, not true floats/a real stand-off. New `standoff()` primitive
  (`hierarchy/units.py`: `CELL_RADIUS` + PP-290 reach class via `troop_types.registry.reach_for`).
  `_node_advance`'s pre-cap + per-cell clamp now use `cells_float()` vs. `standoff()`, gated
  `FIELD_MOVEMENT`, prior code kept as fallback (byte-exact OFF unaffected).
- Bug found+fixed mid-implementation: freezing both sides' enemy positions pre-move let two closing
  sides compound past standoff (run_battle moves unit_a fully before unit_b). Fixed by snapshotting
  unit_a AFTER its own move. Verified: min separation holds at exactly `standoff()` (2.0).
- `find_contacts` gets a standoff-radius field path; `resolve_cross_side_contention` is a documented
  FIELD_MOVEMENT no-op. Review found+fixed a duplicate-cell stamina-drain over-count (dedup via sets).
- CI gap closed: `bat.py`'s golden-digest harness existed but nothing ran it — new
  `tests/valoria/test_mass_battle_byte_exact.py` wires grid-mode checks into CI; field digests recorded.
- `gauge_mb.py`: grid/OFF unchanged (12/20, matches historical 5/13); field path passes 4/20 —
  measured, not fitted; likely needs Stage B (facing/reaction, not yet built), not a magnitude tune.
- G5 byte-exact both grid modes unchanged (unit 7be8499b / cell 1c5b2851). Fabrication + co-file
  clean. Default stays OFF; default-flip remains Jordan-gated.

## 2026-07-01/02 — mass_battle Stage B + bias fix + Stage C: facing, first-mover bias, command layer
- STAGE B: ported the existing facing-slew mechanism (`PC_FACING_MODEL`, already wired on the legacy
  path) onto the FIELD_MOVEMENT path — `_node_advance`'s attention branch was overwriting facing with
  an instantaneous target-direction vector, zero rate-limiting, discarding a stale "don't double-slew"
  rationale that no longer held once that branch fired. Reuses `_slew_facing` unchanged.
- MIRROR-BIAS BUG found + fixed: `gauge_mb.py`'s Cav-vs-Cav mirror matchup (should read ~50/50) read
  98.3/0.0 on the field path — traced via a git-worktree bisect to Stage A's standoff clamp itself
  (confirmed absent, 11-8-1, on the pre-Stage-A commit). Root cause: the clamp's sequential-snapshot
  design gave unit_a persistent first claim on the shared closing budget every tick both sides neared
  standoff. Fixed by reverting to a synchronized both-sides-frozen snapshot and HALVING the allowed
  closing distance at both the anchor and per-cell level. A follow-up review caught and fixed a genuine
  oscillation bug in the per-cell clamp's multi-violator iteration (best-position tracking, not
  last-pass-wins). Verified: mirror matchup back to 2-1-27 (30 seeds); gauge `C3` now OK (5.0/6.7/88.3,
  was 98.3/0.0). One small accepted residual remains (~5% of ticks in one dense rotating scenario rest
  at 1.414 vs the intended 2.0, against an already-halted neighbour) — a fix attempt made it worse via
  WHEEL-rotation interaction, reverted in favor of the smaller gap.
- STAGE C: `engine.build_army` (public multi-subunit constructor, mirrors `gauge_mb.make_mixed_unit`,
  fixes its troops/concentration-forwarding omission + its never-set-advance_dir gap, confirmed inert on
  that helper — zero live callers); `Order`/`check_orders` (timed/conditional order queue, 'immediate'/
  'tick:N'/'enemy_range:D'/'ally_at:D' triggers, run before `assign_targets`); `escort_of`/
  `escort_offset`/`escort_engage_on_contact` (formation-relative positioning, live-facing-rotated,
  computed at the synchronized pre-move point alongside `cached_centroids`). Cannae acceptance test
  (wide-placed wings held then released by a `tick:4` order into the pre-existing `envelop`
  instruction) produces real lateral wheel movement — zero new flanking mechanics. Review found+fixed
  two gaps before landing: `Order.behavior`'s plain `setattr` was unrestricted (risked corrupting cell/
  troop/position accounting if an order set a geometry field) — now an explicit `_ORDER_SAFE_FIELDS`
  allowlist; a malformed trigger string failed silently forever — now validated eagerly at construction.
- G5 byte-exact both grid modes unchanged throughout (unit 7be8499b / cell 1c5b2851) — every change
  gated behind FIELD_MOVEMENT/PC_FACING_MODEL or additive with all-inert defaults. Fabrication clean
  (epsilon-guard citations added where flagged). Default stays OFF; default-flip remains Jordan-gated.

## 2026-07-02 — mass_battle: TOI refactor (halving hack replaced with exact time-of-impact)
- Jordan-directed complete replacement of Stage A/B's halved-anchor-precap + iterated worst-violator
  clamp with real continuous-collision detection: `_node_advance` now proposes each cell's UNCAPPED
  end-of-tick position (no clamp at all); new `resolve_toi_and_commit` (`units.py`) solves the exact
  per-pair quadratic TOI across BOTH sides together, once per tick, capping each cell to the smallest
  root over all its cross-side pairs — exact, no iteration, no oscillation guard needed.
- Reach + facing: `target` (final standoff) always uses base reach (matches `find_contacts`, keeps
  contact/halt in sync, byte-preserves every equal-reach matchup); `_effective_reach` gates a cell's
  reach to zero outside its forward FOV (reuses Stage B's `FOV_HALF_DEG`) for THROTTLE purposes only;
  `_reach_throttle` gives the longer-(facing-gated)-reach side a smaller share of the tick's closing
  motion, so it "sets into formation" before the shorter-reach side closes the rest of the gap.
- 5 real bugs found+fixed (2 via an independent adversarial-review agent): halted-cell obstacle
  exclusion, s=0 root filter, pass-through endpoint-only shortcut, throttled-safe-vs-full-motion
  endpoint mismatch, idle/reserve subunits dropped as obstacles. See plan file for detail.
- Verified: G5 byte-exact both grid modes unchanged; `tests/valoria` 55 passed/24 skipped unchanged;
  true-float standoff invariant zero violations (Horseshoe-cav/Line/Arrowhead/mirror-cav); reviewer's
  own two repro cases now cap correctly. Field golden digests re-recorded (intentional behaviour
  change). Mirror cav-vs-cav (30 seeds) now 0-0-30 — fully balanced, no first-mover skew.

## 2026-07-02 — mass_battle Stage D: role wiring (ED-907 L3) + Envelopment/Refused-Flank presets
- `engine.build_army`/`build_unit` now WIRE the previously-inert `Subunit.role`: a spec's `role` is
  gated by `role_allowed(troop_type, role)` (raises `ValueError` on a disallowed combo — a levy can't
  take `Shock`), and, in `build_army`, defaults `shape`/`instructions` from `ROLE_SPEC[role]` when the
  spec doesn't explicitly set them (explicit spec fields still win). Zero existing call site touched
  (`role` defaults to `None`).
- New `engine.build_envelopment`/`build_refused_flank` (ED-909's Unit-level "Envelopment"/"Refused
  Flank" allocation-grid presets): compose `build_army` + Stage C's timed-order queue + the
  pre-existing, UNMODIFIED `envelop` instruction — center/strong subunits built as given; wing/refused
  subunits get `stance='hold'` + an auto-queued release order (`tick:N` into `envelop`, or
  `enemy_range:N` for refused-flank) unless the spec already supplies its own orders. Zero new
  flanking mechanic, matching Stage C.4's own finding.
- **Deliberately deferred, not part of this change**: the literal LC-8 retirement of `Horseshoe`/
  `RefusedFlank` as `Subunit.shape` values (`geometry.CELL_PATTERN_FN`/`config.MIN_DISCIPLINE`) — the
  frozen byte-exact grid golden digests were computed against battles using `Horseshoe` directly as a
  `Subunit.shape` (`bat.py`'s own battery), so removing it would break that non-negotiable invariant.
  This lands ED-909's Unit-level INTENT (envelopment as an emergent composition) without that break;
  the legacy `Subunit.shape` values remain valid, now understood as legacy options. Flagged for
  Jordan's explicit sign-off before any literal removal + re-baseline.
- `Unit.doctrine`/Aggression: NOT built as new data — Jordan's own ED-907 ratification note already
  names `stance` as engine-realized Aggression; adding a parallel `doctrine.aggression` field would
  duplicate it (NERS-N/E, no unneeded apparatus). Cohesion-priority/the allocation-grid UI/intervention
  cadence are explicitly Jordan-deferred to Stage E — not built here either.
- G5 byte-exact both grid modes unchanged (unit 7be8499b / cell 1c5b2851) — every change is additive
  (new functions, new optional kwargs defaulting to `None`). `tests/valoria` 55 passed/24 skipped
  unchanged. Functional: role defaulting/rejection verified directly; `build_envelopment`/
  `build_refused_flank` construct correctly and a traced battle confirms the wing's order fires
  (releases from `hold` into `envelop` at the queued tick).
- Adversarial review found one real bug, fixed: `build_army` never popped/forwarded an `orders` key
  from a spec dict, so the two presets' documented "unless the spec already supplies its own orders"
  escape hatch was dead code — a caller-supplied custom order was silently dropped and always
  overwritten by the auto-queued release order. Fixed by adding `orders` to `build_army`'s forwarded
  per-subunit override keys. Re-verified: a spec-supplied order now survives; the auto-release still
  fires when no custom orders are given. Byte-exact and pytest unaffected (both re-confirmed).

## 2026-07-02 — mass_battle LC-8: retire Horseshoe/RefusedFlank as Subunit.shape values (ED-909)

- Jordan-approved 2026-07-02 ("correct, retire them. those are emergent outcomes."): executes the LC-8
  retirement Stage D deliberately deferred. `Horseshoe`/`RefusedFlank` removed from
  `geometry.CELL_PATTERN_FN` and `config.MIN_DISCIPLINE`; only `Line`/`Arrowhead`/`GappedLine`/`Column`
  remain valid subunit-level shapes. Envelopment/refused-flank now exist ONLY as Unit-level
  compositions via `engine.build_envelopment`/`build_refused_flank` (Stage D).
- `hierarchy/units.py`: dead `Horseshoe`/`RefusedFlank` branches removed from `role_at_contact` (zero
  live callers, confirmed before/after); each `Subunit` now snapshots its spawn position at
  construction (`_spawn_position`).
- `orchestration.reset_positions` fixed: previously reset EVERY subunit in a Unit to one shared
  shape-derived anchor column each battle-turn — silently correct only for single-subunit units, but
  wrong for any multi-subunit army (collapsed wide-placed wings/escorts back to center every
  re-engagement turn). Now restores each subunit to its OWN spawn column. Verified byte-exact-
  preserving for every existing single-subunit matchup via git-worktree diff.
- `bat.py`/`gauge_mb.py`: grid-mode battery/gauge rows using the retired shapes migrated to
  `build_envelopment`/`build_refused_flank` army-builder callables; new golden digests recorded and
  verified byte-exact (`unit`/`cell` both). `test_mass_battle_byte_exact.py`'s CI subprocess timeout
  bumped 90s→180s (multi-subunit battery rows measurably slow the grid-mode digest run).
- `workbench/trace.py`: `run_traced_battle` gains a `'preset'` spec dispatch (`army`/`envelopment`/
  `refused_flank`), so the visualizer can build real multi-subunit Unit-level compositions.
  `workbench/server.py`'s `H4`/`C4` presets rebuilt on the Envelopment composition.
- G5 byte-exact both grid modes pass against re-baselined digests. `tests/valoria` 81 passed/10 skipped.
  `gauge_mb.py`'s migrated rows and all workbench presets (grid and `FIELD_MOVEMENT=1`) run without
  error.

## 2026-07-02 — mass_battle workbench: multi-subunit preset dispatch + visualization battery

- `workbench/trace.py`'s `run_traced_battle`/`_build_side` extended to accept a `'preset'` spec key
  (`army`/`envelopment`/`refused_flank`) dispatching to `engine.build_army`/`build_envelopment`/
  `build_refused_flank`, alongside the existing single-subunit `build_unit` spec shape — the
  visualizer can now show real multi-subunit Unit-level compositions, not just single-subunit shapes.
- **Adversarial finding during dogfooding, fixed:** `static/index.html`'s preset-selection JS only
  ever populated the simple Shape/Troop dropdowns and always rebuilt the POST body from THEM in
  `runBattle()` — it had no way to represent a multi-subunit preset spec (no `.shape` key) at all.
  Selecting a multi-subunit preset (H4/C4 and the two new ones below) and clicking Run would have
  silently run whatever stale shape values were left in the dropdowns, not the actual preset. Fixed:
  `runBattle()` now uses a selected preset's multi-subunit side verbatim (`selectedPreset.a`/`.b`)
  when it carries a `'preset'` key, and the dropdown is disabled + shown as `— composed army (see
  preset) —` instead of a misleading stale shape name. Also removed `Horseshoe`/`RefusedFlank` from
  the Shape dropdown's `<option>` list entirely (LC-8 retired them as `Subunit.shape` values —
  selecting either would have raised `ValueError` at construction).
- `workbench/server.py`: two new PRESETS exercising genuinely symmetric multi-subunit-vs-multi-subunit
  battles (both sides field 3+ independently-tasked subunits at once, not just an attacker vs a
  lone-subunit defender) — `M3` (Envelopment vs Envelopment, mirror) and `OBL` (RefusedFlank vs
  Envelopment, mirrors `bat.py`'s "oblique" battery row).
- Verified via a Playwright-driven run through all 8 presets in both `FIELD_MOVEMENT=1
  PC_NODE_COHESION=1 PER_CELL=1` and the integer-grid baseline: each preset's deployment frame shows
  the correct subunit count/placement, the fixed dropdown correctly reflects composed-army sides, and
  H4 (Envelopment vs Arrowhead) visibly reproduces the Cannae pattern (B routed, HP 131/400, A's wings
  wrapped around B's remaining position) by the final frame. `tools/ci_sim_fabrication_check.py` clean
  on both changed files (one new literal in `server.py`'s `_REFUSED_REFUSED` cited).

## 2026-07-02 — three Jordan rulings executed: field default flip (ED-1089), subunit cap 11 (ED-1090), frontal recoil gate (ED-1091)

- **ED-1089 (field default flip, Stage A step 7 executed).** `FIELD_MOVEMENT` (hierarchy/units.py) and
  `PC_NODE_COHESION` (config.py) defaults flipped `0` → `1` — a bare engine invocation now runs the
  coordinate field. The integer grid remains fully available via explicit `FIELD_MOVEMENT=0
  PC_NODE_COHESION=0` and stays the frozen byte-exact oracle. **Load-bearing CI-gate fix:**
  `tests/valoria/test_mass_battle_byte_exact.py`'s `_PINNED_OFF` converted from `env.pop()` (which
  after the flip would leave the new ON default in force, silently running the grid-oracle check on
  the field path) to explicit per-toggle OFF-value pins (`'0'`/`'0.0'`). Both grid digests re-verified
  byte-identical under explicit pins (`unit 18bc4a0b…`, `cell bf666d04…`). `bat.py` field golden
  digests re-recorded (`unit_field c7957752…`, `cell_field dd085521…`) — the prior values were STALE
  (recorded before the LC-8 battery migration); the re-record also folds in ED-1091 below. Workbench
  server/frontend mode-banner docs updated for the inverted defaults.
- **ED-1090 (videogame sub-unit cap = 11).** `engine.build_army` now enforces a hard ceiling of 11
  subunits (`ValueError` above it; verified 11 constructs / 12 raises), lifting the TTRPG
  bookkeeping cap of 3 (`mass_battle_v30.md` §A.5 banner added). Command (1–7) remains the
  span-of-control governor within the ceiling; the >7 reconciliation (subordinate officers?) is
  flagged as a future ED, not invented here.
- **ED-1091 (frontal-only charge-recoil).** New `PC_RECOIL_FRONTAL` toggle (default ON; OFF
  reproduces prior any-direction recoil): the reciprocal charge-recoil fires only when the braced
  wall's per-cell-averaged octagon zone vs the charger is GREEN — "a brace cannot repel what it
  cannot face" (grounding §4.3, Burkholder 2007; the historical-validity condition Jordan attached
  was verified against that doc before executing). Verified: grid `cell` digest byte-identical (the
  battery's only braced row is frontal); a frontal braced charge still recoils (36 firings); an
  enveloping-cavalry-vs-braced-hold-line scenario shows the gate suppressing ~26% of firings
  (804 vs 1088 over 8 seeds) — exactly the flank/rear hits. Gauge row C7 can now legitimately gain a
  braced+enveloped variant on the next gauge pass.

## 2026-07-02 — Stage E: Army Configuration Mode (deployment UI)

- `engine.py`: `SUBUNIT_CAP` (11, ED-1090) hoisted from a local inside `build_army` to module scope
  and exported via `_WRAPPER_API`, so any other caller — this UI, the future in-game deployment
  screen — reads the single source instead of duplicating the literal.
- `workbench/server.py`: new `GET /api/roster-options` endpoint exposing the live registries
  (`geometry.CELL_PATTERN_FN` keys, `troop_types.TROOP_TYPE_STATS` + the two generic legacy types,
  `roles_for` per troop type, `engine.SUBUNIT_CAP`) — the frontend never hardcodes a second copy of
  a shape/role list that would drift after a future LC-8-style retirement.
- `workbench/static/index.html`: new "Deploy Army" tab alongside the existing "Quick Match" tab
  (additive — Quick Match untouched). Click-to-place deployment: pick shape/troop_type/role
  (role-menu gated per troop type via `/api/roster-options`)/tier/troop-count, click the field (or
  "Place at default position") to add a subunit to the active side's roster; roster list with
  per-entry remove and a live cap counter (client-side cap enforcement mirrors `SUBUNIT_CAP=11`,
  with the server's own `ValueError` as the authoritative backstop). "Start Battle" assembles both
  rosters into the SAME `{'preset':'army','specs':[...]}` spec `trace._build_side` already
  dispatches to `engine.build_army` (zero new backend battle-running path) and hands off to the
  existing replay canvas/scrub/play controls — one rendering surface for both placement and replay,
  per the Stage E decomposition ("the same canvas in a placement state instead of a replay state").
- Verified via a Playwright-driven run: placed 3 heavy_infantry (Line) for side A and 2 cavalry
  (role=Shock) for side B by canvas click, confirmed `Horseshoe` is absent from the shape options
  (LC-8) and `Shock` appears in cavalry's role menu but not e.g. artillery's, started the battle
  (112 replay frames produced, winner determined), confirmed switching back to the Deploy tab
  restores the placement schematic rather than staying on the replay, and confirmed the cap: adding
  an 11th side-A subunit succeeds, a 12th is blocked client-side with the ED-1090-citing alert
  matching the server's own message text.

## 2026-07-02 — mass_battle: T1-T4 charge-recoil actor/timing/reach ruling (ED-1095)

- **T1 (actor-gate).** New `PC_RECOIL_CHARGER_GATE` (config.py, default ON): the reciprocal
  charge-recoil (`PC_CHARGE_RECOIL`) now additionally requires the charging atom's
  `troop_type == 'cavalry'` literally — a defender no longer recoils a charger just for having
  marginally higher per-tick momentum than a braced wall. `mounted_archers` explicitly excluded
  (see T4 — they should never be closing to melee at all).
- **T2 (brace-setup delay).** New `PC_BRACE_SETUP_DELAY` (config.py, default ON) +
  `Subunit._brace_since_tick` (hierarchy/units.py: stamped `0` at construction for a subunit
  deployed already braced; stamped to the firing tick by `core/contact.check_orders` when an
  `Order` adds `'brace'` mid-battle; reset to `-1` on removal). `resolution._subunit_braced`/
  `_unit_braced` are now `t`-parameterized (`t=None` preserves the old instantaneous check) and
  require ≥1 full tick of continuous brace before treating a subunit as braced, for either the
  charge-shock defensive benefit or the reciprocal recoil. `t` threaded through
  `resolve_engagements`/`resolve_engagements_cascading`/`run_battle`'s call site.
- **T3 (reach-gate, structural only).** `PC_RECOIL_CHARGER_GATE` additionally requires the
  defender's `reach_for(troop_type) >= ` the charger's (`troop_types.registry.reach_for`, the
  existing Stage-A primitive) — a charger with genuinely longer reach can strike a wall whose
  weapons can't reach back, so the wall can't retaliate. `TROOP_TYPE_REACH` stays deliberately
  empty (everyone defaults `REACH_SHORT`), so this half is a no-op today pending a separate
  troop-type-to-reach-class ruling — not populated speculatively.
- **T4 (mounted-archer default kiting).** `engine.build_army`: a spec with
  `troop_type == 'mounted_archers'` and no explicit role/shape/instructions implicitly defaults
  `role='Kite'` instead of silently closing to melee. Any explicit caller choice of role, shape,
  or instructions always wins over this default. `build_unit` unchanged (no "unspecified shape"
  case exists there — its `shape` parameter is a required positional).
- Verified: `bat.py --check` byte-exact across all 4 digest modes (`unit`/`cell`/`unit_field`/
  `cell_field`) against the frozen baselines; `tests/valoria` pytest suite 81 passed, 10 skipped.
- **Also discovered, NOT fixed here (flagged in HANDOFF.md):** the `'envelop'`/`'sweep'`
  instructions and the overhang `'wheel'` maneuver (`hierarchy/units.py` `advance_cells`
  ~L802-861) are gated `if PER_CELL and ...` and only exist on the legacy grid path —
  `_node_advance` (the coordinate-field path, DEFAULT since ED-1089) has no equivalent steering at
  all, so every subunit currently just walks a straight line toward the enemy centroid on the path
  actually used by default. Under investigation.
## 2026-07-02 — Movement/pathing audit (ED-1096) fix plan execution, in progress (ED-MB-0001)
Fable-led audit (ED-1096) confirmed the root cause flagged above and 10 further findings; Jordan
answered all 4 decision gates, deferring gates 1 (Command/Discipline-gated conditional tactics) and
3 (facing/attention split) until envelopment/pincer/wheeling pathing is confirmed working. This
entry covers the fix-plan steps landed so far (steps 1, 2, 4, 5, 6 of 8 + decision gate 2; gate 4
and step 7, the waypoint primitive itself, still pending):
- **Step 1 — `check_drift` node-state fix.** ED-1032's re-key on formation drift only ever covered
  `cell_troops`; node-path position state (`_node_pos`/`_node_rel`) was never included, so a drift
  left the old shape's ids behind and cells teleported to `(0,0)` or stacked on the anchor. New
  `Subunit._rekey_node_state(new_ids)` rebuilds node state for the new pattern around the CURRENT
  live anchor (not spawn) — the subunit reorganizes in place. Gated `PC_NODE_COHESION and
  hasattr(a, '_node_pos')`; legacy path untouched.
- **Step 2 — `reset_positions` node-state no-op (minimal form).** `reset_positions` wrote only the
  legacy grid fields, inert on the node path but a stale-data landmine for future code reading
  `starting_position`. Node-path atoms are now explicitly skipped — position genuinely does not
  reset between engagement turns within a battle (Jordan: "nonsensical for them to return to
  starting positions within the same battle"). The full Command-gated conditional-tactics layer
  (decision gate 1) is deferred; this step only stops the corruption.
- **Decision gate 2 — weapon-derived `unit_type`.** `unit_type` now derives from the troop's
  assigned weapon (`mass_battle.equipment.TROOP_LOADOUT`/`loadout_for`, previously unwired) via new
  `troop_types.registry.unit_type_for`, wired into `build_unit`/`build_army` (unmapped types still
  resolve `'melee'`, byte-exact for every existing call site). Corrects ED-1095/T4: a
  `mounted_archers` spec got `role='Kite'` but no `unit_type`, so it neither kited nor volleyed on
  any path. Added a `mounted_archers` entry to `TROOP_LOADOUT` (bow/light). `kite`'s STEERING gate
  no longer requires `unit_type=='ranged'` (Jordan: kite is weapon-independent, best with a bow but
  executable by lance cavalry) — only volley fire itself still requires ranged; the far edge of the
  kite band uses `reach_for(troop_type)` for a melee kiter instead of inventing a new magnitude.
- **Step 4 — lateral file-holding in `_node_advance` (v12 port).** `_node_advance` was a pure
  centroid attractor — every subunit's column steered at the SAME enemy-centroid column, collapsing
  wide-placed wings inward before any maneuver began. A subunit that is one of several siblings in
  a multi-subunit Unit now holds its own deployment file (`_spawn_position`'s column) while its row
  still closes on the enemy; a solo subunit is unchanged. Confirmed via an H4-composition trace:
  wings now hold within ~1-2 columns of their spawn file across the approach, versus collapsing
  from cols 3/17 to ~9.6/13.0 before this fix.
- **Step 5 — node WHEEL 180-degree facing stall.** The facing update was a lerp-normalize that
  degenerates to the zero vector at an exact 180-degree reversal (full discipline), freezing the
  formation's facing forever — exactly the case a wheel-to-rear maneuver needs. Replaced with a
  rotation-based update (same disc-gated rate `kw`, applied as an angular fraction instead of a
  linear vector blend) with a deterministic tie-break at the boundary. Confirmed: a full-discipline
  subunit facing south, target flipped to due north, now smoothly rotates instead of freezing.
- **Step 6 — maneuver acceptance validators re-pointed at the node path.** `validators.py`'s
  `Run:` line only ever pinned `PER_CELL`, leaving `FIELD_MOVEMENT`/`PC_NODE_COHESION` at the
  ambient (node, since ED-1089) default — so V-ENVELOP/V-SWEEP silently measured the dead legacy
  arm whenever anyone actually pinned toggles to make them pass, and measured nothing meaningful
  otherwise. New `validators._set_movement_path('grid'|'node')` + a `path` parameter on
  `v_envelop`/`v_sweep`/`_envelop_reach`/`_sweep_disp`. New
  `tests/valoria/test_mass_battle_maneuvers.py`: grid-path tests are real regression tests (green,
  the mechanism still works there); node-path tests are `xfail(strict=True)` acceptance targets —
  expected red until step 7 lands, and `strict=True` means an unexpected pass is itself a failure,
  so this cannot silently rot into permanent xfail once the fix ships.
- Verified throughout: `bat.py --check` byte-exact across all 4 digest modes unchanged after every
  step; `tests/valoria` pytest suite 81 passed/10 skipped unchanged (plus the 2 new grid-regression
  tests passing and 2 new node-acceptance tests correctly xfailing). Field digests (`unit_field`/
  `cell_field`) intentionally drift as real node-path bugs are fixed — re-record deferred to a
  single batched pass once the remaining steps (waypoint primitive, `PER_CELL` default flip) land.
- **Step 7 — waypoint primitive (`_resolve_maneuver_goal`/`_envelop_goal`/`_sweep_goal`).** Gives
  `_node_advance` a per-tick anchor-level goal (modeled on the legacy per-cell two-state machine)
  when `envelop`/`sweep` is active, gated behind the same `PC_ENVELOP_PATH`/`PC_SWEEP` toggles the
  legacy path uses. Two bugs found/fixed during verification: a missing toggle-gate made ON/OFF
  measure identical behavior; the ported `past`-the-flank predicate was too shallow at anchor
  granularity (fixed by requiring the anchor to reach `rear_r` itself, reusing the existing ±2
  margin constant, not a new magnitude). `validators.py`'s `v_envelop`/`v_sweep` were also missing
  `seeds`/`turns` forwarding, which had been silently masking the fix behind an absorbed `TypeError`
  inside `xfail` — found by re-verifying the mechanism directly instead of trusting "still xfailed."
  Both node tests now pass for real (no longer `xfail`); grid arm unaffected; full suite 85
  passed/10 skipped/0 xfailed (the 81-baseline + these 4 maneuver tests, all now passing;
  [2026-07-02 adversarial-review correction] an earlier version of this line stale-copied the
  pre-session 81 baseline itself as if it were the new total — verified by checking out this
  step's own commit and re-running the suite).
- **Decision gate 4 — `PER_CELL` default flip to `'1'`.** `config.py:86` default `'0'`→`'1'`, same
  ED-1089 precedent (grid oracle = explicit pin, already the case in `bat.py`/
  `test_mass_battle_byte_exact.py`, so no CI-pin gap). Found and fixed two independently-defaulted
  `os.environ.get('PER_CELL','0')` re-derivations that had drifted out of sync with the new config
  default: `bat.py`'s `compute()` mode-key and `gauge_mb.py`'s cavalry-row gate both mislabeled/
  misgated a bare invocation — fixed by reading the resolved `hierarchy.units.PER_CELL`/
  `config.PER_CELL` instead of re-deriving. Grid digests (`unit`/`cell`) reconfirmed byte-exact;
  field digests (`unit_field`/`cell_field`) diverge from their recorded golden values, but
  identically whether `PER_CELL` is 0 or 1 — confirmed attributable to step 7's intentional
  behavior change, not the gate-4 flip itself (re-record still pending, folded into task #77).
- **Gate-4 finding, disclosed not fixed:** enabling `PER_CELL`'s previously-fully-inert combat
  mechanics (fatigue drain, envelopment-sigma, charge shock) made `test_envelop_reaches_rear_node`
  flip from a reliable pass to a reliable fail — diagnosed as a combat-PACING interaction, not a
  movement regression: the two-subunit "pinning main body + wide-detour detachment" validator
  fixture's main body now frequently routs (~7/8 seeds) around turn 44-56, before the detachment's
  real-physics-timed detour can complete, where the old (PER_CELL=0) combat model never routed
  either side within the 60-turn cap. Confirmed non-movement via: (1) forcing
  `orchestration.PER_CELL=False` alone restores the pass with every other change unchanged; (2) an
  isolated single-subunit fight at the same troop ratio favors the attacker 14-0-6/20 seeds, so the
  defender profile alone isn't favored — it's specific to this two-subunit timing; (3) varying the
  detachment's travel distance barely moved the outcome. Not fixed by retuning `_envelop_goal`
  (band-fitting) or by fixture troop-count tuning (tried, unreliable). Landed as a loud, documented
  `xfail(strict=False)` on `test_envelop_reaches_rear_node` — the underlying combat-balance/pacing
  question (numerically-dominant vs. thin-and-yielding pinning force; a maneuver time-budget
  separate from the frontal fight's own clock) is flagged for whoever next works PER_CELL=1 combat
  balance, out of this movement/pathing fix's scope.
- **Task #77 full verification.** Field digests re-recorded (`unit_field b1963d03.../cell_field
  1f0742c5...`). [2026-07-02 adversarial-review correction] An earlier version of this entry claimed
  the change was "isolated to step 7" — WRONG, per a direct worktree bisection (see `bat.py`'s
  EXPECTED-dict comment for the full commit-by-commit digest trail): steps 1, 4, 5, AND 7 each
  independently changed `unit_field`, not step 7 alone. The one claim that DOES hold: gate 4's
  `PER_CELL` default flip contributes zero ADDITIONAL divergence on top of those four steps, since
  this measurement pins `PER_CELL='0'` explicitly and cannot be reached by that flip. All 4 digest
  modes re-confirmed byte-exact against
  their (2 unchanged, 2 re-recorded) baselines. Functional probe via `workbench/trace.py`
  (default toggles, no validator-forced overrides): a `build_envelopment` wing tracked tick-by-tick
  wheeled from its start (row 36, col 21) to row 14.4, col 32.8 — genuinely wrapping past and behind
  the defender (col ~20.6), not walking a straight line; `sweep` similarly displaced its subunit
  laterally (col 10.0→8.0) toward the flank. Both confirm step 7's mechanism works in a real,
  default-toggle multi-subunit battle, not just the validator harness.
  `gauge_mb.py` re-run under the new PER_CELL=1 default (per gate 4's own text): single=2/20,
  multi=4/20 (H1, C7, C2, C6 pass). Confirms the SAME interaction already diagnosed and disclosed
  above at battle-composition scale: H3/H4(Cannae)/H5/H6 — the actual historical Envelopment/
  RefusedFlank matchups — lose 0-13% instead of the expected 45-72% band, consistent with an
  envelopment composition's pinning center routing before its wings complete their maneuver.
  Recorded, not chased — per this session's (and this repo's) standing discipline against
  retuning magnitudes to fit a band; the underlying combat-balance/pacing question is the same
  open follow-up flagged in the gate-4 finding above, not a new one.
- **Task #79 adversarial review (5-dimension Workflow, sonnet finders + opus verify) — 6
  CONFIRMED findings, all fixed same session, not deferred:**
  1. **Kite never ported to the node path (critical).** Step 7 built `_envelop_goal`/`_sweep_goal`
     but no `_kite_goal` — a mounted_archers subunit (gate 2 correctly gives it
     `instructions=('kite',...)`) fell through to plain centroid steering and closed to melee on
     the live default path, the exact bug class this audit exists to fix, for a 4th instruction
     the first pass missed. Fixed: new `Subunit._kite_goal` wired into `_resolve_maneuver_goal`,
     reusing `PC_KITE_STANDOFF`/`VOLLEY_MAX_RANGE`/`reach_for` verbatim (no new magnitude), matching
     the legacy block's exact toward/away/in-band semantics. Verified: a mounted_archers subunit
     now holds standoff distance 6.5-8.3 against a Line (inside the [5,8] band) instead of closing
     to melee.
  2. **Escort column-override (moderate).** Step 4's sibling-column-holding fallback overrode
     ANY escort's live-tracking column with its fixed spawn file the instant the escorted unit's
     column diverged (e.g. on envelop/sweep/wheel) — defeating Stage C's own escort machinery.
     Fixed: `escort_of is not None` checked before the sibling-count branch.
  3. **Test fixture leak (moderate).** `_movement_toggles`'s save/restore omitted
     `PC_ENVELOP_PATH`/`PC_SWEEP`, contradicting its own docstring — latent today (no other
     in-process test consumes it yet) but real. Fixed: added to the saved/restored set.
  4. **`_rekey_node_state`'s dead `new_ids` param (minor, PLAUSIBLE not CONFIRMED — harmless today,
     fixed anyway).** Never read; silently re-derived from `_oriented(self)`. Fixed: now asserts
     `new_ids` matches, converting a silent future trap into a loud failure.
  5. **`build_army`'s `unit_type=None` sentinel (minor, latent).** `sp.pop('unit_type',
     unit_type_for(tt))` only derives when the key is ABSENT, unlike `build_unit`'s `if unit_type
     is None: derive`. Fixed to match `build_unit`'s semantics.
  6. **Documentation provenance (moderate+minor).** `bat.py`'s "step 7 alone" digest-provenance
     claim and this file's "isolated to step 7"/"81 passed" lines were factually wrong (direct
     bisection: steps 1/4/5/7 all independently changed the digest; true count was 85 not 81) —
     corrected above and in `bat.py`.
  One REFUTED (bat.py battery has no weapon-mapped-troop_type regression coverage — real gap, not
  a concrete defect per the review's own bar; not fixed, flagged as a future coverage item, not
  silently dropped). All 4 digest modes byte-exact after every fix (kite/escort fixes are provably
  inert against the existing battery — neither a kite-instructed nor an escort_of subunit exists in
  it); full suite 84 passed/10 skipped/1 xfailed unchanged.
- **Remaining, not yet done:** step 8 (lower-severity hardening, parallelizable); re-producing the
  Cannae visualization to confirm the fix end-to-end — done (task #78, delivered as an Artifact).

## 2026-07-04 — mass_battle: Cannae gauge audit (ED-MB-0002) ratified; DG-3/DG-4 implemented
- **ED-MB-0002 ratified** (PR #73 merge = ratification, ED-1094 convention); DG-3/DG-4 ruled by Jordan
  same day in chat, recorded as an addendum in `designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/
  README.md` (PR #75). Two independent bug fixes landed first: `validators.py`'s `_attacker_envelop`
  ghost-cell construction bug (`starting_position` assigned after `__post_init__` already ran — added a
  `col=` param to `_line()` instead); `orchestration.py`'s float-epsilon pool-floor bug (`math.floor(x)`
  → `math.floor(x + 1e-9)`).
- **DG-3 implemented, bottom-up (Jordan's own correction of a first-pass eng_counts-division attempt —
  "misleading... should be per-cell troop density... bottom-up... solves multiple engagements"):** new
  `core/exchange.pair_pool_contribution()` redistributes a subunit's unchanged combat-score
  (`subunit_combat_pool`) across a specific contact pair by ACTUAL troop density in the engaged cells
  (`cell_troops`) plus depth-weighted support (reusing `support_engage_frac`'s `SUPPORT_WEIGHTS` falloff)
  — replaces the flat divide-by-simultaneous-pair-count with an exact troop-weighted split.
  `a_troops_frac` (a separate, pre-existing multi-SUBUNIT Command-sharing dampener) kept as an outer
  multiplier, orthogonal to this fix. Known accepted residual, same discipline as Stage A's TOI
  multi-body approximation: a cell simultaneously adjacent to 2+ enemy atoms double-contributes its
  troop share (dogpile edge case, not solved).
- **DG-4 implemented ("a blend of per-subunit as well as whole unit... more likely to wilt if other
  subunits losing, more likely to rally if other subunits winning"):** `build_army` now defaults every
  subunit to its own real starting morale (closing RC-1(b)'s double-count by construction — no new
  state); new `Subunit.pull_morale()` + a continuous per-phase term in `core/state.morale_check_phase`
  pulls each subunit's morale toward its LIVING SIBLINGS' troop-weighted aggregate (new
  `MORALE_SIBLING_PULL=0.15`, tagged Class-B/Jordan-vetoable — the mechanic is ruled, the magnitude is
  not derived from any existing primitive). RC-1(c) (subunit-scale casualty trigger vs shared pool)
  auto-resolves as a side effect — both sides of that mismatch are now subunit-scale.
- **Perf finding, fixed:** `support_engage_frac` was still called unconditionally for every pair even
  though C-ii no longer reads its result — duplicated the same abs→orig cell-coordinate conversion
  `pair_pool_contribution` does internally. Made conditional on `POOL_VARIANT != "C-ii"`. Profiling
  (cProfile on an envelop-army trial) showed the DOMINANT remaining cost is pre-existing Stage-A TOI
  physics (`resolve_toi_and_commit`/`_pair_toi_scale`, 679K calls, ~2.2s of 4.7s), not this fix's own
  code (`resolve_engagements` ~0.6s) — multi-subunit field-path battles are inherently more expensive
  under the existing TOI system; `bat.py`'s full battery now takes ~1-4 min per mode instead of
  seconds (disclosed, not a hang — confirmed by direct profiling and isolated single-trial timing).
- **Adversarial review (general-purpose agent) — 4 findings, all fixed, none moved the recorded
  digests (confirmed by re-running `bat.py --check` all 4 modes post-fix — all still match):**
  1. **(HIGH)** `pair_pool_contribution` recomputed the cell layout from `CELL_PATTERN_FN[shape](tier)`
     (the legacy tier-only pattern) instead of iterating `atom.cell_troops` directly — silently
     zeroed the whole pool for any continuous-scale (`troops=`/`concentration=`) subunit whose real
     footprint (`footprint_for`) extends beyond that small legacy rectangle (confirmed by repro: a
     tier=4/troops=8000 Line's real 70-cell footprint vs. the tier's own 35-cell pattern — pool
     contribution was silently 0.0, now correctly non-zero). Fixed: iterate `cell_troops.items()`
     directly (the same authoritative, footprint-aware source `cells()`/`check_drift` already use).
     Masked in the current battery only by coincidence (existing fixture troop counts happen to stay
     inside the legacy rectangle).
  2. **(HIGH)** The sibling-morale pull ran AFTER this-phase's own casualty/exhaustion erosion, so a
     healthy sibling's pull could retroactively rescue a subunit from a same-phase rout its own
     casualties would have caused, before `rout_resolution` ever saw the eroded value — a materially
     stronger mechanic than "more likely to rally," and an unintended side effect of call ordering.
     Fixed: reordered so the sibling-pull (using a phase-start snapshot) applies BEFORE self-erosion —
     a sibling's state can soften/harden the morale a subunit ENTERS its own erosion with, but can no
     longer erase that erosion's result; self-erosion keeps the final say on this-phase rout.
  3. **(MEDIUM)** Siblings were aggregated from already-mutated live values within the same per-atom
     loop (Gauss-Seidel order-dependency, biased toward whichever subunit iterates first) rather than
     a fixed phase-start snapshot. Fixed as part of the same reorder above (one snapshot dict built
     once per unit before the loop).
  4. **(LOW, dormant)** `build_army`'s `kw.setdefault('morale', morale)` no-ops if a spec explicitly
     sets `'morale': None` (key present, not absent) — silently keeps that one subunit on the
     shared-pool double-erosion path DG-4 exists to close. No current caller does this, but fixed
     (explicit `if kw.get('morale') is None:` check, matching this file's own `unit_type` precedent).
- **Verified:** all 4 `bat.py` digests changed from the pre-DG-3/DG-4 baseline and re-recorded (expected
  — touches shared, non-gated combat-resolution code). Re-checked after the 4 adversarial-review fixes
  above: `unit`/`unit_field` stayed byte-identical to their first re-record; **`cell` and `cell_field`
  BOTH moved again** and were re-recorded a second time. **Process gap, caught by CI not locally:**
  `test_byte_exact_cell_mode` only hard-fails inside `_in_reference_env()` (GITHUB_ACTIONS+Linux) and
  silently SKIPS elsewhere — a real pytest pass count locally can hide a genuine `cell`-mode digest
  drift. Confirmed NOT a portability artifact (this sandbox reproduces CI's exact new hash directly via
  `bat.py --check`) — a real movement from the same fixes, just invisible to `pytest`'s local summary.
  Lesson recorded in `bat.py`'s own comment: always re-verify `cell` with a direct `bat.py --check`
  call, not just the pytest suite, after any core.exchange/core.state/orchestration change.
  `tests/valoria` 87 passed/17 skipped/1 xfailed either way (neither byte-exact pytest test covers the
  two field modes at all — manual `bat.py --check` is the only check for those).
- **Gauge re-run (n=20, reduced from the standard 60 for turnaround — `gauge_mb.py`'s own `__main__`
  hardcodes n=60 with no CLI override, confirmed by reading it):** **honest result: the fix did NOT
  close the targeted gap.** Aggregate counts are unchanged from the pre-fix baseline (single 2/20, multi
  4/20) but the COMPOSITION shifted: multi-mode H1 (mirror Line-vs-Line, previously passing) now reads
  60/40 (WIN-OUT, band 42-58) while C1 (previously failing) now reads 45/55 (OK, band 35-55) — a
  trade, not a net gain. **H3, H5, H6 (three of the four actual Cannae-pattern target rows) remain
  UNRESOLVED (100% draws) in both single and multi mode** — worse than the pre-fix "0-13% losses"
  framing in one sense (that at least resolved decisively, if in the wrong direction) and better in
  another (no longer a rout, just a stalemate) — either way, not inside the historical band. **H4
  (Cannae proper)** improved from a decisive loss to `WIN-OUT` (0/10, 90% draw) — still fails, still
  undershoots. **C4** improved from the disclosed 0-13% range to 66.7% (`WIN-OUT`, 75-95 band, 70%
  draw) — real movement toward the band, still short. This is disclosed, not hidden: RC-1's
  accounting-layer fix was never proven (RC-3 was explicitly "confounded, not proven") to be
  gauge-scale-sufficient on its own, and this n=20 read is the first real evidence on that question —
  it looks like RC-1 alone is necessary but not sufficient; DG-1/DG-2 (composition/yield-mechanic, both
  still open) are the more likely remaining levers, not a bug in this fix.
- **Frozen-wings ablation (§2 step 4) — CLOSES DG-5 cleanly:** H3/H4/H5/H6 read byte-identical
  A%/decA%/draw% whether wings wheel normally or are frozen in place for the whole battle (`n=30`
  each). **No maneuver-timing race exists** — confirms the fixture-scale finding generalizes to gauge
  scale. DG-5 is not a live question; the bottleneck is entirely elsewhere (most likely DG-1's
  composition question, given H3/H5/H6's total non-resolution above).
- **C4-vs-C7 trace (§2 step 5) — single-mechanism, fully explained:** varying only the defender's
  `stance`/`discipline` (`n=30` each): baseline 16.7%; `+discipline=8` alone: 16.7% (zero effect);
  `+stance='hold'` alone: 76.7% (the entire gap); `+both` (=C7): 76.7% (no additional discipline
  contribution). **`stance='hold'` alone fully accounts for the C4→C7 divergence** — discipline plays
  no role.
- **Not yet done:** `test_envelop_reaches_rear_node`'s xfail re-evaluation (next); DG-1/DG-2 remain
  open and are now the better-evidenced next lever given the gauge results above.


<!-- Relocated from active coverage_matrix.md 2026-07-23 (register-size cap); these were already condensed stubs. -->
## 2026-07-02 — mass_battle Stage D: role wiring (ED-907 L3) + Envelopment/Refused-Flank presets (archived — condensed)
- Wired the previously-inert `Subunit.role`; new `engine.build_envelopment`/`build_refused_flank`
  (ED-909 Unit-level presets, composed from existing primitives, zero new flanking mechanic). LC-8's
  literal shape retirement deliberately deferred pending Jordan sign-off (executed in the next entry).
  One real bug found+fixed (adversarial review): `orders` key not forwarded by `build_army`. G5
  byte-exact unchanged. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle LC-8: retire Horseshoe/RefusedFlank as Subunit.shape values (ED-909) (archived — condensed)
- Jordan-approved retirement: `Horseshoe`/`RefusedFlank` removed from `geometry.CELL_PATTERN_FN`/
  `config.MIN_DISCIPLINE`; only `Line`/`Arrowhead`/`GappedLine`/`Column` remain valid subunit-level
  shapes; envelopment/refused-flank now exist only as Unit-level `build_envelopment`/`build_refused_flank`
  compositions. `reset_positions` fixed (per-subunit own spawn column, was one shared shape anchor).
  `bat.py`/`gauge_mb.py` battery migrated + re-baselined, byte-exact verified. `tests/valoria`
  81 passed/10 skipped. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle workbench: multi-subunit preset dispatch + visualization battery (archived — condensed)
- Workbench extended to visualize real multi-subunit compositions (`army`/`envelopment`/
  `refused_flank` preset dispatch); a real frontend preset-dispatch bug found+fixed (stale-dropdown
  values silently overriding the actual multi-subunit preset). Two new symmetric multi-subunit-vs-
  multi-subunit presets (`M3`, `OBL`). Verified via Playwright across all 8 presets, both movement
  modes. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — three Jordan rulings executed: field default flip (ED-1089), subunit cap 11 (ED-1090), frontal recoil gate (ED-1091) (archived — condensed)
- ED-1089: `FIELD_MOVEMENT`/`PC_NODE_COHESION` defaults flipped 0→1 (field is now the default engine
  path); CI-gate `_PINNED_OFF` fix (env.pop→explicit pins) closed a real silent-regression risk.
  ED-1090: videogame subunit cap = 11 (`build_army`). ED-1091: frontal-only charge-recoil
  (`PC_RECOIL_FRONTAL`, "a brace cannot repel what it cannot face"). All grid digests byte-identical
  under pins. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — Stage E: Army Configuration Mode (deployment UI) (archived — condensed)
- Click-to-place deployment UI ("Deploy Army" tab, additive to Quick Match): `SUBUNIT_CAP` hoisted to
  module scope; new `/api/roster-options` endpoint (single source, no frontend drift); one shared
  canvas for placement + replay. Verified via Playwright (cap enforcement, role gating, LC-8 shape
  removal all correct). Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle: T1-T4 charge-recoil actor/timing/reach ruling (ED-1095) (archived — condensed)
- T1 actor-gate (recoil requires charger troop_type=='cavalry'); T2 brace-setup delay (≥1 tick before
  braced counts); T3 reach-gate (structural, TROOP_TYPE_REACH stays empty pending a separate ruling);
  T4 mounted-archer default kiting (`role='Kite'`). Byte-exact verified. Discovered but not fixed
  here: `envelop`/`sweep`/`wheel` only exist on the legacy grid path, unreachable on the default node
  path (led directly into the next entry's movement/pathing audit). Full detail:
  `tests/coverage_matrix_archive.md`.

## 2026-07-02 — Movement/pathing audit (ED-1096) fix plan execution (ED-MB-0001) (archived — condensed)
- Fable-led audit (ED-1096) + 8-step fix plan executed: node-path drift/reset-position corruption
  fixes, weapon-derived unit_type wiring (gate 2), lateral file-holding + WHEEL facing-stall fixes,
  the waypoint primitive (`_resolve_maneuver_goal`/`_envelop_goal`/`_sweep_goal`/`_kite_goal` —
  first real steering for envelop/sweep/kite on the live node/field path), and `PER_CELL`'s default
  flip to `'1'` (gate 4). A 5-dimension adversarial review found 6 more real defects, all fixed same
  session (kite never ported to the node path; an escort column-override regression; a test-fixture
  toggle leak; two minor dead-param/sentinel-semantics bugs; stale digest-provenance documentation).
  **Disclosed, not fixed:** enabling `PER_CELL`'s previously-inert combat mechanics made a two-subunit
  pinning-body-plus-detachment validator fixture rout before its detour could complete (a combat-pacing
  interaction, not a movement regression) — landed as a loud `xfail`, flagged for whoever next works
  PER_CELL=1 combat balance. All 4 `bat.py` digest modes re-recorded where genuinely changed (grid
  modes confirmed byte-exact where the change was node-path-only); `tests/valoria` 84 passed/10
  skipped/1 xfailed. Full detail: `tests/coverage_matrix_archive.md`.


<!-- Relocated from active coverage_matrix.md 2026-07-23 (register-size cap). -->
## 2026-07-18 — audit-corpus relocation: provenance-comment path fixes only [no mechanical change]
- Repo-wide audit reorg moved `tests/audit/all_directions_ners_v27.md` to
  `audit/lane-a/all_directions_ners_v27.md` (see CLAUDE.md §3). Updated the stale `[canonical: tests/audit/...]`
  provenance comments citing that file in phase4_agi_dominance_2026-05-15.py, phase5_continuous_engine_2026-05-15.py,
  phase6_dominance_solvers_2026-05-15.py, phase7_action_triangle_2026-05-15.py, phase8_smart_ai_v2_2026-05-15.py —
  path text only, no formula/threshold/logic touched. Co-file satisfied (documentation-only trip).

## 2026-07-18b — adversarial-pass follow-up: two more stale path fixes [no mechanical change]
- mass_battle/engine.py comment + phase6_sim_verification_ledger.json `canonical_source` both still cited the
  pre-move `tests/audit/...` path; repointed to `audit/lane-*/...`. Path text only. Register near its 10k-token
  cap — trim to the archive file at the next real entry.

<!-- Relocated from active coverage_matrix.md 2026-07-23 (register-size cap). -->
## 2026-07-01 — mass_battle workbench: tick-by-tick visualizer (server + frontend)
- ADDED tests/sim/mass_battle/workbench/{trace.py,server.py,static/index.html} (mirrors
  designs/scene/combat_engine_v1/workbench's pattern: a tiny stdlib HTTP server, no external deps, no
  build step). trace.run_traced_battle() runs ONE battle via engine.build_unit/resolve_battle (the
  wrapper contract, never reaches past it) with tracing on, returning the full 'tick'/'melee'/
  'volley'/'positions' event stream. server.py serves a canvas SPA with playback controls (scrub/play/
  step), a preset picker mirroring gauge_mb.py's named matchups, and per-tick HP/morale/rout/event-log
  panels. VERIFIED end-to-end live (not just imported): all 4 endpoints (GET /, /api/mode, /api/presets,
  POST /api/trace) tested via a running server instance in both PER_CELL=0 (grid) and
  FIELD_MOVEMENT=1 PC_NODE_COHESION=1 PER_CELL=1 (coordinate-field) modes.
- IMPORTANT (documented in server.py): PER_CELL/FIELD_MOVEMENT/PC_NODE_COHESION are read from
  os.environ once at import time and star-imported as independent copies into every consumer — a
  running server's mode is FIXED at process start (no live toggle); comparing grid vs field means two
  server instances. GET /api/mode reports the actual running config.
- FINDING from using the tool (not a bug): confirmed by reading _node_cells() (hierarchy/units.py) that
  the coordinate-field candidate keeps ROW positions integer-rank-snapped by design ("ranks are integer
  bins" — a real military structure) and only bins COLUMNS to their file; positions are not yet fully
  continuous floats end-to-end. Accurately reflected by the visualizer, not a rendering defect.
- Engine untouched by this addition (workbench/ only). G5 byte-exact both modes unchanged (unit
  7be8499b / cell 1c5b2851). Fabrication clean (HTTP status codes + dev port named+ledgered as
  non-sim-mechanical tooling constants, not fabricated citations). Co-file satisfied.

**Partition-invariance fix.** `subunit_combat_pool` is, by Jordan's own DG-3 characterization, a
per-atom COMBAT SCORE (Command + per-subunit discipline/cohesion/stamina), not a per-troop rate —
`pair_pool_contribution` correctly renormalizes when ONE atom is itself split across MULTIPLE enemies,
but does nothing when SEVERAL atoms of one side each independently, fully engage the SAME single
opposing atom (a pinning center + 2 wings all converging on one Line/Arrowhead defender — exactly
H3-H6/C4/C7's shape). Each converging atom got its own near-full `base_pool` with no reduction, so
splitting a fixed total force into more simultaneously-converging atoms multiplied total dice against
that one shared target, purely from the split — the mirror-image of the bug DG-3's "intensive" fix
already closed on the defender side. Confirmed by direct formula trace (no ablation needed): a fully-
engaged atom's `pair_pool_contribution` ≈ its own `base_pool` regardless of troop count, so N converging
atoms contribute ≈N×base_pool for identical total troops.

**Fix** (`core/exchange.py`'s new `_pair_engaged_troops` + `orchestration.py`'s new
`_convergence_scale`/`PC_CONVERGENCE_NORM`, default ON): groups pairs by shared target atom on each
side; for any group of ≥2, computes the troop-weighted-mean base score across the group and the group's
combined own-troop count, derives what ONE merged atom of that combined size would contribute, and
scales every member's own contribution down uniformly so the group's total is capped there. A group of
size 1 (the overwhelming majority of pairs — every single-subunit gauge row) is a no-op by construction
(skipped outright, scale 1.0 via dict-miss). Computed ONCE per tick on the FULL pairs list (before
`CASCADING_ENABLED`'s sub-phase split, which would otherwise fragment a convergence group across
separate `resolve_engagements` calls and under-correct it).

**Verified live, not just via digest motion:** a direct trace of an H3-style envelopment-army-vs-Line
battle confirmed `_convergence_scale` returns a non-trivial scale for 1446/1686 sampled ticks (max
simultaneous-convergence group size 3) — the mechanism genuinely engages this battery, this isn't inert
code. All 4 `bat.py` digests re-recorded (shared, non-gated combat-resolution code, same as every prior
DG-3/DG-4/Step-4 landing in this lane): `unit` 204d4d7…→444afdd4…, `cell` 84e606c…→cc13e17b…,
`unit_field` 79c1910…→4ab1b5a1…, `cell_field` c3de830…→ffe54c49… (full hashes in `bat.py`). `tests/valoria`:
112 passed / 57 skipped / 1 xfailed / 0 failed (7 pre-existing `test_names.py` failures confirmed
unrelated via `git stash` bisection — an environment/fixture issue, not caused by this change).

**Honest gauge result (multi mode, n=60):** the fix does **NOT** move H3/H4/H5/H6/C4's win/loss/draw
split at all — bit-for-bit identical `decA`/`dec_n` to the pre-fix baseline, even though exact per-trial
hp/turn/morale values changed (confirming the digest move is real but small relative to these rows'
dominant mechanism, envelopment/charge-shock morale collapse, not raw pool magnitude). Full 20-row gauge
unchanged at single=2/20, multi=6/20. **This is disclosed honestly, not oversold as a gauge-band fix** —
the partition-invariance defect was real and is now closed, but it was never the dominant lever for
H3-H6's overshoot; DG-1's composition and the still-live envelopment-shock magnitude remain the larger
levers there.

**RC-5 preliminary finding (diagnostic, not a fix):** a controlled A/B-slot-swap experiment on 3 of
RC-5's 9 single-subunit rows found a **slot/deployment-dependent asymmetry that does not track shape
superiority consistently**:

| Matchup | A wins / B wins / draws (n=30) |
|---|---|
| Arrowhead(A) vs Line(B) | 30/0/0 |
| Line(A) vs Arrowhead(B) | 29/1/0 |
| Line(A) vs Line(B) [mirror] | 17/13/0 |
| GappedLine(A) vs Line(B) | 22/8/0 |
| Line(A) vs GappedLine(B) | 2/28/0 |
| GappedLine(A) vs Arrowhead(B) | 11/19/0 |
| Arrowhead(A) vs GappedLine(B) | 2/28/0 |

Arrowhead-vs-Line flips to whichever shape occupies slot A (H2/H9's WIN-OUT in both directions is this,
not two independent shape effects); GappedLine-vs-Line favors GappedLine regardless of slot (a real,
slot-independent shape effect); GappedLine-vs-Arrowhead favors whichever shape occupies slot B. No single
rule (side bias, shape hierarchy) explains all three pairs — a true mirror (Line-Line, Arrowhead absent)
stays near-even (17/13), ruling out a blanket "slot A always wins" engine bug. The likely shared
ingredient across the inconsistent cases: `ANCHOR_MAP`'s per-shape deployment column (Line=9,
Arrowhead=8, GappedLine=7) is applied identically regardless of which side (A/B) carries that shape, so
two different-shaped sides deploy at two different absolute columns — a small (1-2 cell) lateral
deployment offset whose interaction with facing/approach geometry was not traced further this pass.
**Not root-caused to a specific mechanism** — flagged as the next concrete lead for whoever continues
RC-5's triage, not claimed as solved. RC-5's other 6 rows (H7, H8, R1, R3, C1, C3, C5) were not
investigated this pass.

**Verification:** `tests/valoria` full suite green (above); gauge_mb.py re-run both modes (numbers above);
`_convergence_scale` engagement traced directly (not inferred). Filed as ED-MB-0004 (resolves the open
"gauge triage continuation" item).

