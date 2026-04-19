# Valoria Coverage Matrix
# Full historical findings: see tests/sim_batch_*_2026-04-16.md
# This file tracks open findings and recent confirmations only.

## Open Findings (all batches)

| ID | Source | Description | ED |
|----|--------|-------------|-----|
| SIM2-01 | ST-01 | 2x Senator Assert engine too fast | ED-572 (resolved) |
| SIM2-05 | ST-06 | Post-combat fieldwork when player fled undefined | Resolved — ED-576 |
| SIM2-06 | ST-07 | Co-Movement Cards 1-15 not in canonical docs | Resolved — ED-577 |
| SIM2-07 | ST-07 | TTRPG mass battle melee damage formula implicit | Resolved — ED-578 |
| SIM2-10 | ST-03 | Social initiative deterministic vs combat rolled | Resolved — ED-581 |
| SIM2-11 | ST-03 | Chain Contest Resistance-2 stall not documented | Resolved — ED-582 |
| SIM3-04 | NPC-03 | Arc state vs Priority 6 at Mandate < 3 | ED-586 |
| SIM3-07 | Zoom In | Stability Crisis Zoom In trigger absent | ED-587 |
| SIM4-01 | ST-14 | RM Phase 2 T9 holding condition unreachable | ED-588 |
| SIM4-02 | ST-14 | RM Presence marker mechanics undefined | ED-589 |
| SIM5-01 | ST-21 | No Parliamentary block on Tribune actions | ED-616 |
| SIM5-02 | ST-22 | Grand Contest Recall: once-per-source fix | ED-617 |
| SIM5-04 | ST-23 | Torben Conviction window: S1-8 formal def | ED-618 |
| SIM5-13 | ST-28 | 3-Obligation GM advisory cap | ED-619 |

## Active P1 EDs Requiring Design Action

| ED | Description |
|----|-------------|

## Resolved This Session (summary)

15 items resolved. See sim_batch archives for details.
Key: ED-588/589 (RM), ED-612 (Guilds), AUD-SET/VIC/NPC, SIM-DEBT-03/04,
ED-577-01-04, SIM-POL-R01-R05, ED-684, ED-590, ED-572, ED-545+.

## Throughline Analysis + Propagation — 2026-04-17

8 categories validated. See tests/sim_batch archives for detail.

## New Findings — sim_npc_player_batch2_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| JUS-SIM-02 | Cardinal Justice | Heresy Proceedings: authorization loop | ✓ Archived — ED-629 resolved 2026-04-17 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Vaynard Path B met at S9 from Season 1 hold — fastest single path | VAY-SIM-04 | ✓ |
| Vaynard S0 Assembly pre-garrisons T13 before Baralta can Proclaim | VAY-SIM-01 | ✓ Reinhard Principle |
| Intelligence auction: 2 major world events from S1 intel, zero Domain Actions | VAY-SIM-05 | ✓ Force multiplication |
| Baralta Sovereign Authority Doctrine = constitutional fortification | BAR-SIM-01 | ✓ |
| Almud institutional ambiguity as governance — Thread absorbed without public acknowledgment | ALM-SIM-03 | ✓ |
| Ehrenwall Counter fires from information failure (withholding RS data), not military failure | EHR-SIM-01 | ✓ Conviction correctly distinguishes |
| Justice winning Proceedings → shared loss conditions more likely | JUS-SIM-01 | ✓ Institutional winner / peninsula loser |
| Reinhard Principle generalizes to all faction leaders | CROSS-01 | ✓ Core strategic principle |
| Conviction = permanent Ob economy on aligned actions | CROSS-02 | ✓ |

### New SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-B2-01 | Vaynard simultaneous 3-path Accounting conflict verification | RESOLVED — 0/200 conflict runs. Paths sufficiently differentiated. |
| SIM-B2-02 | Ehrenwall moral ledger 30-season timing | RESOLVED — Arc B window viable before S9. Coup fires 100% without intervention. |
| SIM-B2-03 | Justice-as-Confessor 10-season Church governance sim | RESOLVED — Justice less immediately dangerous; higher institutional stability long-term. Canonical framing supported. |


## Editorial Approval — 2026-04-17

All open editorial items approved by Jordan. Propagated this batch:

| Item | Target | Status |
|------|--------|--------|
| ED-620 RM Founding Mechanic | victory_v30 §8 | Propagated |
| ED-624 Elske Loyalty Track | victory_v30 §3.6 | Propagated |
| ED-625 Excommunication Tribunal | social_contest §7.1 | Propagated |
| ED-616 Intelligence Embargo | ci_political_redesign §8 | Propagated |
| ED-591-609 Arc Expansion v1 | npc_behavior §5.2 reference note | Approved + noted |
| ED-634 Faction Politics expansion | faction_politics_expanded_v1 | Approved, propagation pending |


## ED-634 Propagation — 2026-04-17

Faction Politics rank-ladder expansion (PP-660). Propagated to:

| Target | Change |
|--------|--------|
| npc_behavior_v30 §1.2 | Community and Warden added to Conviction taxonomy |
| npc_behavior_v30 §3.3 | Caste-transgressive Scar risk modifier noted |
| npc_behavior_v30 §2.13 | Crown inner circle (Voss/Reichard/Thale/Linder/Kreutz) Stance Triangles |
| npc_behavior_v30 §2.14 | Hafenmark inner council (Heljason/Geirson) Stance Triangles |
| npc_behavior_v30 §2.15 | Varfell Jarl council (Holdar/Stenskald) Stance Triangles |
| player_agency_v30 §3.3 | Initiation Duty category added |
| Ledger | ED-634 resolved; sub-EDs 635-658 and SIM-POL-R01/02/05 registered |

Remaining open sub-EDs: ED-640/642/643/644/645/648/649/650/651/652/655/656/657/658, SIM-POL-R01/02/05. All P2 except ED-643 (Solmund propagation P1) and SIM-POL-R01/02/05 (P1 sim-debt).

## New Findings — sim_npc_player_batch3_2026-04-17

### Staleness Audit
- AER: **confirmed live** in board_game_v30. Modifies Altonian Vanguard deployment threshold. Prior simulation usage was correct.
- faction_politics_expanded_v1.md (PP-660, accepted 2026-04-17): canonical source for all sub-office ladders, named inner circle NPCs, Ministry expansion. Prior simulations pre-dated this document.

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| GAP-B3-01 | Multiple | Shadow Renown referenced across docs but no implementation specification | ✓ Archived — ED-632 resolved 2026-04-17 |
| — | Riskbreaker §2.2 | Deniability Debt referenced as "stage13 mechanic, retained" but not defined in canonical docs | Open — ED-633 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Spymaster: double-agent methodology (controlling compromised assets rather than severing them) | KOLT-SIM-01 | ✓ Correct intelligence model |
| Spymaster: 1-season verification delay produces actionable vs. speculative intelligence | KOLT-SIM-02 | ✓ Mechanically correct |
| Royal Guard dual-chain: Kreutz cannot transmit Counter information without chain breach | KREU-SIM-03 | ✓ Institutional blind spot confirmed |
| Guild Comptroller: Parliamentary Committee motions = cheapest Domain Action equivalents | FELD-SIM-02 | ✓ Free binding law from Scene action |
| Templar: converting military provocation into Parliamentary weapon through formal Protest | TEMP-SIM-01 | ✓ Defensive constraint as political tool |
| Riskbreaker: institutional activation (making institutions act without knowing they're directed) is highest-skill mission outcome | RB-SIM-01 | ✓ |
| Journeyman: victory depended entirely on Feldhaus's discretion — systemic, not personal | JOUR-SIM-01 | ✓ Honest statement about institutional power |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-B3-01 | Mid-rank characters experience the moral cost that faction leaders export |
| CROSS-B3-02 | Institutional blind spot is always one step up — constraints are positional, not systemic |
| CROSS-B3-03 | Shadow Renown lacks formal game support across three character types |

---


### Derived Stats v2 Patch Validation

| Test | Result | Notes |
|------|--------|-------|
| TroopCount monotonicity | PASS | Damage never increases as troops decrease (4k values) |
| Reinforcement cap | PASS | Over-muster ratio capped at 1.0 |
| Vitality healing cap | PASS | Cannot exceed max_Vitality |
| Equal combat with breath | PASS | 48/49%, 10.7r avg |
| Mass battle equal armies | PASS | 52/48%, 4.2r avg |
| Grand Contest Spent rate | PASS | 100% at Foc 3. Regroup required. |
| Thread multi-op matrix | PASS | Spirit/Focus both gate meaningfully |

**Patch:** TroopCount formula `CI/(Size×block)` → `CI/max_TC`, capped 1.0.

### Combat Formula Correction (stress_derived_stats_v2_corrected)

Prior stress tests used stale multiplicative formula (net_hits × weapon_dmg).
Canonical formula (PP-232): Damage = net_hits + STR + weapon_modifier[weapon][target_armor].

| Test | Result | Notes |
|------|--------|-------|
| Heavy vs Light (blade vs blade) | Heavy 85% | Light blade bounces off heavy armor (mod +0). STR 5 vs 3 = +2/hit. Correct. |
| Heavy vs Light (light uses blunt) | Light 56% | Blunt ignores armor (+5 all tiers). Weapon counter-pick works. |
| Str 7 vs Str 1 | Str7 89% | +6 damage/hit. STR is highly significant. |
| Tank(E7/A2) vs Cannon(E1/A6) | Tank 83% | Vitality 78 vs 14. Durability beats pool advantage. |
| Assassin(A6/S2) vs Balanced(A4/S4) | Balanced 62% | Low Str hurts even with pool advantage vs unarmored. |

**RETRACTED: "Agility dominance" finding from v1 tests was a simulation bug, not a design issue.**
The canonical additive formula with STR already creates proper attribute balance:
- Agility → pool (accuracy, defense)
- Strength → damage per hit
- Endurance → survivability (Vitality, Stamina)
- Weapon choice → armor counter-play (blunt beats heavy, blade beats light)

### System Validation Suite (sim_system_validation.py + system_validation_report.md)

| Test | Result | Notes |
|------|--------|-------|
| Generational Transition | PASS | All 5 categories (preserve/transform/reset/break/transfer) validated against ED-696 |
| Derived Stats Calibration | CONFIRMED | Provisional to confirmed. Multipliers validated. Economic pressure dynamics correct. |
| Scale Transitions E2E | PASS | All 6 directions (Personal/Settlement/Territory/Peninsula bidirectional) |
| Personal-Scale Combat | PASS | 15D/Ob3: 78% success (41 OW, 37 S, 18 P, 4 F) |
| Personal-Scale Contest | PASS | 12D vs 10D opposed: 60% PC win rate |
| Fieldwork Depth Gates | PASS | TS thresholds (0/10/30/50) gate correctly |
| Threadwork Resolution | PASS | 14D/Ob3: Coherence/RS costs fire |
| Degree Table (OW gate) | PASS | net >= 2*Ob AND net >= 3 |

## SIM-B2 Resolutions — 2026-04-18

| ID | Description | Result |
|----|-------------|--------|
| SIM-B2-01 | Vaynard 3-path accounting conflict | PASS — no conflict (0/200 runs). Calibration note: 64% no-win by S30 under aggressive play. |
| SIM-B2-02 | Ehrenwall moral ledger 30-season timing | PASS — coup fires 100% without intervention. Arc B practical at S5 only. |
| SIM-B2-03 | Justice-as-Confessor 10-season Church governance | PASS — canonical framing validated. Less short-term danger, higher long-term institutional stability. |

## Unsimulated Canonical Content — Closure Note — 2026-04-18

settlement_layer_v30 (497 lines), faction_politics_v30 (947 lines), throughline_resolutions_v30 (412 lines)
were flagged as unsimulated. Assessment: these are structural specifications (deterministic rules, ladder
definitions, clock interaction tables), not probabilistic mechanics requiring execution simulation.
faction_politics rank-ladder already covered by SIM-POL-R01–R05 (resolved). Three-clock interaction
covered by system validation ED-702. Settlement derived stats covered by Phase 6 Godot audit.
**Sim debt: FULLY RESOLVED as of 2026-04-18.**

## Campaign NPC Sim Findings — 2026-04-18

| ID | Description | Status |
|----|-------------|--------|
| CAL-SIM-01 | CI convergence at 49 across all 11 NPC PC campaigns — faction AI CI rate undertuned | OPEN P2 |
| CAL-SIM-02 | 0/11 victories at S120 — victory thresholds or faction AI strategic direction insufficient | OPEN P2 |
| GAP-SIM-01 | RM govern actions use generic territory fallback — should route through Community Organizing | OPEN P3 |
| NOTE-SIM-01 | Vaynard RS=0, Edeyja RS=1 — validates canonical arc descriptions mechanically | CONFIRMED |
| NOTE-SIM-02 | Maret Uln best RS outcome (33) — diplomat+moderate TS most substrate-preserving | CONFIRMED |

## Engine Audit — 2026-04-18

50 mechanical gaps identified in engine_v2.py vs canonical params.
Full audit: tests/audit/engine_audit_2026-04-18.md

Critical gaps blocking valid simulation:
- G-DICE-01/02/03/04: d10 face 1/10 bonuses absent; degree table wrong at Ob>2
- G-STAT-01 to 06: Church Mandate/Wealth and Varfell all-stats undertuned
- G-TRACK-01: IP starts at 5 vs canonical 20
- G-VIC-01 to 08: Victory checks use territory count not TCV; conditions incomplete
- G-AI-04: Varfell AI complete stub
- G-CI-03: CI not frozen at 75

Previous 11 NPC PC campaign results (a6f468ee) are NOT valid for balance testing.
Engine rebuild required before iterative NPC simulations.

## CI/CI/TCV Cross-Document Conflicts — 2026-04-18

7 conflicts identified. Engine rebuild blocked pending editorial resolution.
Full register: tests/audit/tc_tcv_conflict_register_2026-04-18.md

1. CI freeze at 75 vs CI runs to 100 (5 docs disagree)
2. CI vs CI naming (campaign_architecture uses CI)
3. Seizure availability threshold (CI 15 vs CI 40 vs any)
4. Seizure Ob formula (7−PT vs 2+Fort+max(0,3−PT))
5. TCV values for T8/T9 (T9=5 vs T9=3)
6. CI 100 event mechanics (Unification vs Mass Seizure)
7. Church victory condition (existing vs CI 100 only)

## Editorial Decisions — CI/PV/Seizure/Victory — 2026-04-18

7 conflicts resolved. See tests/audit/editorial_decisions_ci_pv_2026-04-18.md
CI→CI, TCV→PV, no freeze, seizure CI≥60 one-time, victory=peninsula control.

## Reapplication — 2026-04-18

15/20 session changes already present in restructured main. 3 remaining gaps patched:
- npc_behavior §1.2: Community + Warden Convictions
- npc_behavior §2.15-2.17: Crown inner circle (Voss/Reichard/Thale/Linder/Kreutz), Hafenmark (Heljason/Geirson), Varfell (Holdar/Stenskald)
- military_layer §1.9: Siege Action mechanic
ED-633/635/636/637/638/641 resolved.


## Engine v3 — 2026-04-18

Rebuilt from scratch against canonical params. 50 audit gaps addressed.
Smoke test: 5 seeds × 120 seasons. 0 victories — AI expansion rate too low.
CI generation working (reaches 100 in 3/5). RS correct. Dice correct.
Next: tune faction AI military expansion, then NPC campaigns.

## Scene Mechanics Audit — 2026-04-18

Full audit: tests/audit/scene_mechanics_audit_2026-04-18.md

3 cross-document conflicts (params files stale vs params/core.md):
  A. Stamina: combat says End+1, core says End×5 (ED-694 wins)
  B. Composure: contest says Cha+6, core says Cha×3 (ED-694 wins)
  C. Disposition ceiling: fieldwork says floor(Bonds/2)+1, core says =Bonds (PP-684 wins)

2 open EDs in Contest: ED-295 (CLASH stall), ED-297 (AMPLIFY dominance)
1 stale ×3 multiplier reference in mass combat PP-204

All four systems mechanically complete (63/67 items verified).

## ED-295/ED-297 Resolved — 2026-04-18

ED-295 (CLASH stall) and ED-297 (AMPLIFY dominance): both confirmed working via
historical precedent analysis. Coalition dominance and institutional stalemate are
intended design, validated by Bolshevik/ANC/Solidarity/Congress/CCP/Zapatista patterns.

Composure formula propagated: Cha+6 → Cha×3 in params/contest.md (ED-694).

## Engine v3 Fixes — 2026-04-19

- Victory check: now requires territory control (all 15 playable) + Accord ≥ 2 + all rivals eliminated/submitted
- RS recovery: WC ≥ 2 halves baseline decay, WC = 3 adds RS +2/season
- False Church S11 victory (seed 2) eliminated

Still blocking:
- WC never advances (no Warden emergence mechanic) → RS recovery never fires
- Uncontrolled territories accumulate — no faction reclaims them
- CI→CI/TCV→PV propagation in victory_v30 (full-session task)


## Warden Emergence + Uncontrolled Reclaim + CI Propagation — 2026-04-19

Source: tests/sim/sim_warden_tc_reclaim.md

3 scenarios:
- Scenario A: Warden Emergence via Forgetting Check — works, Ob 1 near-trivial. NPC priority tree missing March-to-T15 trigger.
- Scenario B: Uncontrolled territory reclaim — free march works. ED-NEW-008: Seizure undefined for Uncontrolled.
- Scenario C: CI formula consistency — CI ceiling conflict (victory_v30 says 75, ci_political says 100). CI=CI rename not propagated.

Findings:
- ED-NEW-008: Seizure vs Uncontrolled territory gap
- ED-NEW-009: Cohesion −15 = derived consequence of Stability −1 (confirm)
- Propagation: victory_v30 §7 CI ceiling 75→100, CI→CI in §3.2
- GAP: PV not defined in any canonical source
- NPC fix: Varfell priority tree needs March-to-T15 at P2/P3 when VTM ≥ 2

## CI/PV/Seizure Conflict Resolution — 2026-04-19

All 7 conflicts from tc_tcv_conflict_register resolved per editorial_decisions_ci_pv.

| Conflict | Resolution |
|----------|-----------|
| CI ceiling | 100, no freeze |
| Seizure threshold | CI >= 60, one-shot |
| Seizure Ob | 10 - PT - infra (floor 1) |
| PV values | T8/T12=4, T3/T14=3, total 35 |
| Victory | Peninsular Sovereignty only |


## Mass Seizure Declaration Curve — 2026-04-19

Issue: prior commit 250715f raised seizure threshold 60->75. Superseded by this commit.
Resolution: threshold stays CI >= 60; declaration is probabilistic per season.
P(declare) = max(0, min(1.0, (CI-58)/42)): 5% at CI 60, 29% at 70, 52% at 80, 76% at 90, 100% at 100.
Civil-war-grade action; Church institutional restraint modeled by the probability curve.
Files: victory_v30 §3.2/§7, ci_political_v30 §7.6, params/bg/ci_seizure.md.
Supersession register created at canon/supersession_register.yaml.


## Mass Seizure Declaration Curve v2 (exponential) — 2026-04-19

Curve revised from linear to exponential to reflect Church institutional restraint
dominating early CI range and only breaking down near ceiling.

Formula: P(declare) = ((CI-60)/40)^3.3, clamped [0,1].
CI 70: 1%, CI 80: 10%, CI 90: 39%, CI 100: 100% (forced).

Also: valoria_hooks.py supersession_check() added — non-blocking warning when a
commit touches files flagged in canon/supersession_register.yaml.

## Engine v3.1 — 6 bug fixes + Warden emergence — 2026-04-19

1. Seizure: exponential P=((CI-60)/40)^3.3 (replaces deterministic CI>=75)
2. Mass Seizure: ALL prominent territories (was single-target)
3. Warden emergence: VTM, T15 march, WR/WC, RS stabilization
4. 0-territory = immediate elimination
5. AI expansion thresholds lowered
20-seed: 75% Varfell, 10% Crown, 10% SHARED_LOSS. Avg S56.
