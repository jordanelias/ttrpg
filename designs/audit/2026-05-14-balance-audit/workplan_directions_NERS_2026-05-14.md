# COMPREHENSIVE WORKPLAN — Directions × NERS Testing
## Valoria Balance Audit · 2026-05-14 · Test Phase Specification
## Authority: peninsular_strain_v30 + canon/02_canon_constraints.md (P-01..P-15) + throughline_registry.md + throughlines_meta.md
## Scope: 7 proposals from `comprehensive_audit_all_directions_2026-05-14.md` §7 ratification slate

---

# §0 PURPOSE AND SCOPE

This document specifies the test plan for validating the 7 ratification-slate proposals. Each proposal is tested across:
- **6 directions** (top-down · bottom-up · vertical · diagonal · lateral · horizontal)
- **4 NERS dimensions** (Necessary · Elegant · Robust · Smooth)
- **P-01..P-15 canonical compliance** (universal applicability)
- **Throughline + meta-throughline impact** (extension or break)

The plan is **phase-structured** because tests have dependencies. Phase N+1 tests presume Phase N tests passed.

Test outputs feed a **granular mechanical log** (specified in companion `mechanical_log_specification_2026-05-14.md`) that auditors use to verify claims.

---

# §1 PROPOSAL ROSTER

The 7 proposals under test, with proposal-class per PP-674:

| PID | Proposal | Class | NERS avg | Test priority |
|-----|----------|-------|----------|---------------|
| **P1** | Q-21 — Ecclesiastical Appointment every-other-arc throttle | C (parameter) | 4.75 | TIER-1 |
| **P2** | Threshold 11/15 — Co-Victory partition | C (parameter) | 4.75 | TIER-1 |
| **P3** | Treaty Expiration — 40%/arc lapse on Crown Treaties | B (rule extension) | 4.75 | TIER-1 |
| **P4** | Vaynard's Settlement — Varfell post-conquest consolidation | B (new action) | 4.75 | TIER-2 |
| **P5** | Crown Initiative — 3 modes (Progress / Great Work / Coronation) | B (new card) | 4.0 | TIER-2 |
| **P6** | Charter of Liberties — Hafenmark institutional codification (pure W cost) | B (new action) | 4.25 | TIER-2 |
| **P7** | Vaynard's Hall — Varfell military-court L-gain | B (new action) | 3.5 | TIER-3 (defer/conditional) |

---

# §2 TEST ID NAMING CONVENTION

```
T<phase>-<proposal>-<direction>-<NERS>-<sequence>
```

Examples:
- `T1-P1-TD-N-001` = Phase 1 test, Proposal P1, Top-Down direction, Necessary dimension, sequence #1
- `T2-P3-BU-R-003` = Phase 2 test, Proposal P3, Bottom-Up direction, Robust dimension, sequence #3
- `T3-ALL-PXX-005` = Phase 3 test, all proposals, P-XX canonical constraint check, sequence #5
- `T4-INT-MULTI-001` = Phase 4 integration test, multi-proposal interaction, sequence #1

Direction codes: `TD`/`BU`/`VT`/`DG`/`LT`/`HZ`
NERS codes: `N`/`E`/`R`/`S`

---

# §3 PHASE 1 — Per-Proposal Independent Tests

Each proposal tested in isolation. Other proposals NOT applied. Establishes single-intervention baseline.

## §3.1 Phase 1 Test Matrix

For each proposal P (P1–P7), generate test cases across 6×4=24 cells. **Not all cells are equally informative.** Cells marked ⊘ are "not applicable" for that proposal (no testable surface in that direction × NERS intersection); skip them.

### §3.1.1 P1 — Q-21 EA Throttle (every-other-arc)

| Dir × NERS | Test ID | Hypothesis | Method | Pass criterion | Fail criterion |
|-----|--------|-----------|--------|---------------|----------------|
| TD × N | T1-P1-TD-N-001 | Without throttle, Church mean L compounds to 6.45 (canonical max 7) in 36s; with throttle, drops to ≤5.5 | Sim: 500 campaigns each (control: per-season EA; treatment: every-other-arc EA) | Mean L_Church_treatment ≤ 5.5 AND ≥ 0.5 below control | Treatment mean L_Church > 5.8 |
| TD × E | T1-P1-TD-E-001 | Rule is restatable in <15 words | Manual reading | Single-sentence statement, no nested conditions | Requires multiple sentences or branching logic |
| TD × R | T1-P1-TD-R-001 | Three Church strategic approaches remain viable post-throttle | Sim: per-Church-action frequency across 500 campaigns | EA + CF + AI all >5% selection rate | One Church path drops below 2% |
| TD × S | T1-P1-TD-S-001 | Integration: throttle affects only EA timing, not other Church mechanics | Code audit: confirm no spillover to CF/AI/Seizure | Only EA's per-action gate changes; no cross-effect | Other Church actions inadvertently affected |
| BU × N | T1-P1-BU-N-001 | Bottom-up: in canon v5 sim, Church wins 51.4%; with P1 only, drops to 25-35% | Sim 500 campaigns each | Church win-share treatment in [25, 35] | Outside [20, 40] |
| BU × E | T1-P1-BU-E-001 | Implementation change is single-line code diff | Code review | One conditional added | Multi-file change |
| BU × R | T1-P1-BU-R-001 | Within-Church choices forced: when EA unavailable, pick CF or AI? | Per-season Church action log analysis | Both CF and AI rates rise by ≥20% in EA-blocked seasons | Church idles when EA unavailable |
| BU × S | T1-P1-BU-S-001 | No cascade failures: throttle doesn't break PT/CF dependencies | Sim: stress test 100 campaigns; assert all canonical invariants hold | Zero invariant violations | Any sim-mechanic invariant breaks |
| VT × N | T1-P1-VT-N-001 | Vertical: throttle reduces Church territorial gain rate | Sim: Church territory mean at season 36 | Treatment territory ≤ control - 1 | No territorial impact |
| VT × R | T1-P1-VT-R-001 | Cardinal's character-scale survival unaffected | Sim: track Cardinal-equivalent-Sta proxy (Church L) | Cardinal-L mean ≥ 4 across campaigns | Cardinal-L mean drops below 3 |
| DG × N | T1-P1-DG-N-001 | Time-window: 24s vs 36s vs 50s campaigns show consistent throttle effect | Sim sweep across campaign lengths | Church L drop ≥ 0.5 across all 3 lengths | Effect inverts or zeros at any length |
| DG × R | T1-P1-DG-R-001 | Late-game Church strategy survives throttle | 50s sim: Church win-rate ≥ 20% | Church 20-30% at 50s | Church <15% at 50s |
| LT × N | T1-P1-LT-N-001 | Lateral: throttle creates Church-other parity, not Crown dominance | 4-faction win-share with only P1 applied | Crown ≤ 50% AND Church 25-35% | Crown >55% |
| LT × R | T1-P1-LT-R-001 | Other factions' decisions unchanged by Church throttle | Non-Church action selection diff | Per-action rate diff <10% for non-Church | Non-Church actions distorted |
| HZ × R | T1-P1-HZ-R-001 | Forced-choice symmetry: throttling Church doesn't asymmetrically penalize them under high-pressure states | Stratified sim analysis by Turmoil level | Church win-rate in high-Turmoil ≥ Church win-rate in low-Turmoil × 0.7 | Church collapses in high-pressure |

**P1 Phase 1 coverage:** 16 testable cells (8 cells ⊘ — TD×N covers vertical-elegant by inheritance; lateral-smooth not meaningful for parameter change).

### §3.1.2 P2 — Threshold 11/15

| Dir × NERS | Test ID | Hypothesis | Pass criterion |
|-----|--------|-----------|----------------|
| TD × N | T1-P2-TD-N-001 | Threshold change raises direct sovereignty rate from 2.8% to 10-40% | Direct rate in [10, 50] across configs |
| TD × E | T1-P2-TD-E-001 | Change is single-number canonical edit | True |
| TD × R | T1-P2-TD-R-001 | Three strategic paths emerge: rush-11, block-11, build-toward-11 | All three faction action histories show distinct strategies |
| BU × N | T1-P2-BU-N-001 | Sim confirms decisive endings emerge | Mean campaign-end-season ≤ 28 in winner-found campaigns |
| BU × R | T1-P2-BU-R-001 | Winner identity correlates with strategic choice, not random | Per-strategy-cluster win rate variance ≥ 15pp |
| VT × N | T1-P2-VT-N-001 | Vertical: 11/15 produces partition that includes treaty-bound territories | Co-Victory captures Crown-Treaty-bound paths |
| VT × R | T1-P2-VT-R-001 | Both direct-control and treaty-hegemony paths viable | Win distribution: ≥30% direct-control + ≥20% treaty-network |
| DG × N | T1-P2-DG-N-001 | Time-window: short campaigns favor rush-11; long campaigns favor build-11 | Strategy frequency varies by length |
| LT × N | T1-P2-LT-N-001 | Lateral: threshold doesn't disproportionately favor one faction | Win-share spread ≤ canon-baseline-spread + 10pp |
| HZ × R | T1-P2-HZ-R-001 | Forced-choice: blocking rival's 11th territory creates dramatic mid-game | Per-campaign log shows blocking actions in ≥40% campaigns |

### §3.1.3 P3 — Treaty Expiration

| Dir × NERS | Test ID | Hypothesis | Pass criterion |
|-----|--------|-----------|----------------|
| TD × N | T1-P3-TD-N-001 | Without expiration, Crown Treaty path compounds to ≥65% win-rate; with expiration drops to ≤50% | Win-rate diff ≥ 15pp |
| TD × E | T1-P3-TD-E-001 | Rule: "At each arc-Accounting, each Crown Treaty has 40% probability of lapsing." | Single sentence |
| TD × R | T1-P3-TD-R-001 | Three Crown approaches: ignore-and-renew, hedge-multiple, single-strong-partner | All three appear in winning Crown campaigns |
| BU × N | T1-P3-BU-N-001 | Per-treaty lapse events generate ≥ 1.5 events per arc on average (network of ≥4 treaties) | Lapse-event count |
| BU × R | T1-P3-BU-R-001 | Treaty renewal becomes meaningful action category (>10% of Crown actions) | Renewal action frequency |
| VT × N | T1-P3-VT-N-001 | Treaty lapse triggers partner-faction Accord re-evaluation at scale-cross | Lapse → partner's territory Accord drift visible |
| VT × R | T1-P3-VT-R-001 | Hegemony-loss is recoverable (partner can be re-bound) | Re-bound rate >40% within 2 arcs |
| DG × N | T1-P3-DG-N-001 | 50-season campaigns: ≥5 expiration events per Crown faction on average | Average expiration count |
| LT × N | T1-P3-LT-N-001 | Lateral: other factions can exploit Crown lapse window | Non-Crown territorial gain rate in lapse-window ≥ baseline × 1.3 |
| HZ × N | T1-P3-HZ-N-001 | Pressure-state interaction: lapse risk higher in high-Turmoil arcs | Stratified lapse rate correlates with Turmoil |

### §3.1.4 P4 — Vaynard's Settlement

| Dir × NERS | Test ID | Hypothesis | Pass criterion |
|-----|--------|-----------|----------------|
| TD × N | T1-P4-TD-N-001 | Without P4, Varfell conquered territories revolt 70%+ in 4 seasons | Revolt rate confirmed |
| TD × E | T1-P4-TD-E-001 | One-sentence rule: "Mil+W vs Ob 3, Accord +1 (or +2 OW), Order +1" | Single sentence |
| TD × R | T1-P4-TD-R-001 | Two approaches: rush-conquest-then-settle vs hold-and-secure | Both visible in Varfell action logs |
| BU × N | T1-P4-BU-N-001 | Varfell territory retention rate rises ≥20pp with P4 | Retention diff |
| BU × R | T1-P4-BU-R-001 | Settlement attempts adapt to threat: high-MS = more cautious | Settlement frequency correlates inversely with MS |
| VT × N | T1-P4-VT-N-001 | Settlement consolidates territory at settlement-scale (Order ↑) and territory-scale (Accord ↑) | Both effects fire |
| VT × R | T1-P4-VT-R-001 | Cross-scale: territory-scale gain creates faction-scale Mil pressure on rivals | Rival Mil deployment increases post-Settlement |
| DG × N | T1-P4-DG-N-001 | Settlement timing matters: too early (no conquests) wasted, too late (already revolted) ineffective | Optimal timing in turns 4-12 post-conquest |
| LT × N | T1-P4-LT-N-001 | Lateral: Vaynard's Settlement doesn't grant non-Varfell factions analog (single-faction mechanic) | No other faction can use |
| HZ × R | T1-P4-HZ-R-001 | Settlement under high-pressure: prereqs (Mil≥3) constrain availability | Settlement availability scales with Mil stat |

### §3.1.5 P5 — Crown Initiative (3 modes)

| Dir × NERS | Test ID | Hypothesis | Pass criterion |
|-----|--------|-----------|----------------|
| TD × N | T1-P5-TD-N-001 | Mode III (Coronation Renewal) lifts Excommunication; without it, Excomm is irrecoverable | Mode III effect verifiable |
| TD × E | T1-P5-TD-E-001 | Three modes share resolution mechanism (W cost, I vs Ob roll, degree-table effects) | Common spine verifiable |
| TD × R | T1-P5-TD-R-001 | Three distinct strategies — Progress (fast/cheap), Great Work (long/big), Coronation (Church-dependent) | Mode selection varies by campaign state |
| TD × S | T1-P5-TD-S-001 | Mode II Open Pledge integrates with seasonal-action paradigm | Multi-season pacing tracked correctly |
| BU × N | T1-P5-BU-N-001 | Almud deposition rate drops from 16% canon to ≤8% with P5 | Deposition rate diff |
| BU × R | T1-P5-BU-R-001 | Mode selection varies by Crown faction state | Per-state mode distribution non-uniform |
| VT × N | T1-P5-VT-N-001 | Character-scale (Almud) Sta recovery cascades to territory-scale (Accord +1) | Both effects observable |
| VT × R | T1-P5-VT-R-001 | Mode I scales with own territories Accord — geography holds pressure (М-2) | Ob varies with territory state |
| DG × N | T1-P5-DG-N-001 | Mode II's 3-season Open Pledge creates time-bound risk window | Pledge-window failure mode observable |
| DG × R | T1-P5-DG-R-001 | Mid-campaign Crown Initiative shifts from Progress (early) to Coronation (late, post-Excomm) | Mode frequency vs season correlation |
| LT × N | T1-P5-LT-N-001 | Lateral: Coronation Renewal creates Crown-Church interdependence | Mode III usage requires Church L ≥ 4 |
| LT × R | T1-P5-LT-R-001 | Other factions react to Crown Initiative (e.g., Inquisitor placed during Open Pledge) | Rival counter-response visible |
| HZ × N | T1-P5-HZ-N-001 | Initiative cost (W -2) competes with other Crown W-using actions | Crown W deficit observable post-Initiative |

### §3.1.6 P6 — Charter of Liberties (pure W cost)

| Dir × NERS | Test ID | Hypothesis | Pass criterion |
|-----|--------|-----------|----------------|
| TD × N | T1-P6-TD-N-001 | Hafenmark mean L rises ≥ 0.5 with Charter vs without | L diff |
| TD × E | T1-P6-TD-E-001 | Pure W cost (no Token consume); single resolution rule | Single sentence |
| TD × R | T1-P6-TD-R-001 | Three Hafenmark approaches: Charter-after-Token-build vs Charter-as-PI-management vs Charter-emergency-L-recovery | All three observable |
| BU × N | T1-P6-BU-N-001 | Hafenmark win-share rises from 19.6% canon to ≥22% with P6 only | Win-share diff |
| BU × E | T1-P6-BU-E-001 | No Token economy distortion (refuted by Part 12; revised version pure W) | Token economy preserved |
| VT × N | T1-P6-VT-N-001 | PI reduction (clock) propagates to territory-scale Order improvement | PI-Order link observable |
| DG × N | T1-P6-DG-N-001 | Charter timing: most effective mid-campaign (turn 16-24) | Charter usage frequency vs season |
| LT × N | T1-P6-LT-N-001 | Lateral: Charter doesn't strip other factions' Tokens | No spillover |
| HZ × N | T1-P6-HZ-N-001 | Pressure-state: Charter Ob 4 succeeds 65-75% at canonical I=4 | Success rate range |

### §3.1.7 P7 — Vaynard's Hall (DEFER status)

P7 is Tier-3 conditional. Tests only run if Phase 4 integration shows Varfell <15% after P4 alone.

| Dir × NERS | Test ID | Hypothesis | Pass criterion |
|-----|--------|-----------|----------------|
| TD × N | T1-P7-TD-N-001 | Vaynard's Hall adds Varfell L-gain WITHOUT P4 already providing sufficient territorial path | L gain measurable AND not redundant |
| TD × R | T1-P7-TD-R-001 | Token sacrifice creates dual strategy paths | Both Token-rich and Token-poor approaches viable |

---

# §4 PHASE 2 — Pairwise Interaction Tests

Each pair of proposals tested together; other proposals NOT applied. Total pairs: C(7,2) = 21. Skip pairs with no plausible interaction (e.g., P2 + P4 are orthogonal).

## §4.1 High-priority pairs (likely interactions)

| Pair ID | Pair | Hypothesis | Method |
|---------|------|-----------|--------|
| **PAIR-P1-P3** | Q-21 + Treaty Expiration | Both reduce dominant-faction effects. Combined: Crown ~40%, Church ~25% | Sim 500 with both |
| **PAIR-P1-P2** | Q-21 + Threshold 11/15 | Throttle drops Church; lower threshold raises decisive endings | Combined effect |
| **PAIR-P3-P5** | Treaty Expiration + Crown Initiative | Crown Init Mode II (Open Pledge) at risk of mid-pledge treaty lapse | Mode II abort frequency |
| **PAIR-P4-P5** | Vaynard's Settlement + Crown Initiative | Varfell consolidates AND Crown survives — full character-scale + Varfell viability | Win-share both >10% |
| **PAIR-P1-P6** | Q-21 + Charter of Liberties | Hafenmark gets Charter while Church is throttled — Hafenmark closes gap | Hafenmark to 18-23% |
| **PAIR-P3-P6** | Treaty Expiration + Charter | Charter L-gain compounds while Crown Treaties decay — Hafenmark momentum | Hafenmark win-share up |
| **PAIR-P2-P5** | Threshold 11/15 + Crown Initiative | Crown Initiative gives character survival; threshold makes faction wins reachable | Pyrrhic-victory rate <2% |

## §4.2 Lower-priority pairs (skip unless Phase 1 surfaces interaction)

PAIR-P2-P4, PAIR-P2-P6, PAIR-P4-P6, PAIR-P5-P6, etc.

## §4.3 Phase 2 pair test template

For each pair P-X + P-Y:
- **T2-PAIR-P-X-P-Y-001**: Win-share diff vs P-X alone (does P-Y modify P-X's effect?)
- **T2-PAIR-P-X-P-Y-002**: Win-share diff vs P-Y alone (does P-X modify P-Y's effect?)
- **T2-PAIR-P-X-P-Y-003**: Synergy detection — combined effect > sum of individual effects?
- **T2-PAIR-P-X-P-Y-004**: Antagonism detection — combined effect < either individual?

Pass: combined effects within expected magnitude (no surprise interactions).
Fail: combined effects produce dominant strategy, balance break, or canonical-rule violation.

---

# §5 PHASE 3 — Canonical Constraint Tests (P-01 through P-15)

Every proposal must satisfy all 15 canonical constraints from `canon/02_canon_constraints.md`. Many constraints (P-01 through P-15) apply to thread/ontology mechanics; political-balance proposals here mostly don't engage P-01..P-15 directly, but compliance must be verified.

## §5.1 P-01..P-15 applicability matrix

| P-XX | Applies to political-balance proposals? | Tests required |
|------|----------------------------------------|----------------|
| P-01 (Inseparability) | NO — political mechanics don't invoke thread operations | Confirm none of P1..P7 invokes thread mechanics; if any does → full P-01 test |
| P-02 (Monstrosity in Real) | NO | Confirm no monstrous-entity framing in P1..P7 |
| P-03 (Rendering = consciousness) | NO | N/A |
| P-04 (Monstrosity = ontological) | NO | N/A |
| P-05 (Three emergence modes) | NO | N/A |
| P-06 (Threadcut no layer 2) | NO | N/A |
| P-07 (Calamity = rendered-side) | NO | N/A |
| P-08 (Epistemological barrier) | PARTIAL — Charter of Liberties touches inert/transmitted knowledge metaphorically | Confirm Charter is political institutional codification, not Thread-knowledge transmission |
| P-09 (Memory pulling) | NO | N/A |
| P-10 (Coherence = commensurability) | NO | N/A |
| P-11 (Temporal Disjunction universal) | NO | N/A |
| P-12 (Drift propagation tridimensional) | NO | N/A |
| P-13 (Forgetting = rendering failure) | NO | N/A |
| **P-14 (Board/VG modes express inseparability)** | **YES** — all proposals must work in VG play mode | Verify all P1..P7 implementable in Godot 4.6 |
| P-15 (Three-layer being-persistence) | NO | N/A |

## §5.2 P-14 specific tests (universal)

| Test ID | Proposal | Test |
|---------|----------|------|
| T3-P14-P1-001 | Q-21 | Implementable as arc-counter on Church faction state; verify Godot scene compatibility |
| T3-P14-P2-001 | Threshold 11/15 | Implementable as victory-check parameter; trivial |
| T3-P14-P3-001 | Treaty Expiration | Implementable as per-arc probabilistic check on Crown Treaty register; verify random source matches dice resolution paradigm |
| T3-P14-P4-001 | Vaynard's Settlement | Implementable as Tribune-card UI affordance; verify target-selection UX |
| T3-P14-P5-001 | Crown Initiative | Implementable as Senator-Inward card; verify mode-selection UX; Mode II Open Pledge requires multi-season state tracking |
| T3-P14-P6-001 | Charter of Liberties | Implementable as Legacy card; verify pure-W cost UI |
| T3-P14-P7-001 | Vaynard's Hall | Implementable as Tribune-card alternative; verify Token-sacrifice UI |

## §5.3 P-08 specific test (Charter of Liberties only)

| Test ID | Test |
|---------|------|
| T3-P08-P6-001 | Confirm Charter of Liberties is political institutional codification (Magna Carta / Westphalia analog), NOT Thread-knowledge transmission. Charter does not grant non-sensitives Thread-level precision. |

Pass: Charter mechanics produce L+1 / PI−1 (political/legitimacy effects only). No Thread-rendering or knowledge-precision effect.
Fail: Charter described as conveying Southernmost-derived knowledge or substrate-access.

---

# §6 PHASE 4 — Full Integration Tests

All Tier-1 and Tier-2 proposals applied simultaneously. Tests the recommended ratification package.

## §6.1 Integration configuration (RC-v1)

```
P1: Q-21 EA throttle every-other-arc       [ENABLED]
P2: Threshold 11/15                         [ENABLED]
P3: Treaty Expiration 40%/arc               [ENABLED]
P4: Vaynard's Settlement                    [ENABLED]
P5: Crown Initiative (3 modes)              [ENABLED]
P6: Charter of Liberties (pure W cost)      [ENABLED]
P7: Vaynard's Hall                          [CONDITIONAL]
```

## §6.2 Integration test cases

| Test ID | Hypothesis | Pass criterion |
|---------|-----------|----------------|
| **T4-INT-001** | RC-v1 produces win-share in asymmetric band (Crown 35-45 / Church 20-30 / Hafenmark 15-25 / Varfell 10-20) | All 4 factions in band ±5pp |
| T4-INT-002 | Direct sovereignty rate ≥ 12% | Decisive endings emerge |
| T4-INT-003 | Almud deposition rate ≤ 10% in canon-length campaigns | Character-scale survival |
| T4-INT-004 | No dominant strategy across configs | Win-share spread ≤ 35pp across 8 tested configs |
| T4-INT-005 | RC-v1 robust to consent-rate variation (0.5, 0.6, 0.75) | Crown win-rate variance ≤ 12pp across consent values |
| T4-INT-006 | RC-v1 robust to campaign length (24/36/50 seasons) | Win-shares vary <10pp per faction across lengths |
| T4-INT-007 | All canonical invariants hold | Zero violations of P-01..P-15 + canonical mechanical rules |
| T4-INT-008 | Mechanical log captures every state change for audit | 100% coverage on log replay |
| T4-INT-009 | Two-Accounting-sustained victory check fires correctly | Sovereignty_history mechanic verified |
| T4-INT-010 | Pyrrhic-victory rate (Crown wins but Almud deposed) ≤ 2% | Character-faction alignment |

## §6.3 Stress tests

| Test ID | Stress scenario | Pass criterion |
|---------|----------------|----------------|
| T4-STRESS-001 | All 4 factions at L=1 starting state (rare canonical scenario) | Sim doesn't break; some faction recovers |
| T4-STRESS-002 | High initial Turmoil (10) | Pressure model handles; chronic Strain persists |
| T4-STRESS-003 | Church starts with no territories | Church viability via Seizure path |
| T4-STRESS-004 | Crown starts with all 15 territories | Other factions can challenge via Excommunication / Conquest |

---

# §7 PHASE 5 — Throughline & Meta-Throughline Verification

Validates that the RC-v1 package extends or preserves throughlines (per `comprehensive_audit_all_directions_2026-05-14.md` §2).

## §7.1 T-extension verification

| Test ID | Throughline | Hypothesis | Pass criterion |
|---------|-------------|-----------|----------------|
| T5-T-N2-001 | N2 Sovereignty Is Governance | Mode I (Royal Progress) extends N2 — governance practice generates L | Mode I logs show governance-action sequences |
| T5-T-N4-001 | N4 Every Ending Is Earned | Threshold 11/15 + sustained-2-Accountings make endings earned, not arbitrary | Per-victory log shows ≥2-arc sustain |
| T5-T-N6-001 | N6 Institutions Are Characters | Crown Initiative gives Crown institutional agency | Per-campaign Crown Initiative usage ≥ 0.5 per campaign |
| T5-T-T4-001 | T4 Ministry & Institutional Bureaucracy | Mode II Great Work is institutional codification | Mode II usage observable |
| T5-T-T9-001 | T9 Church Infrastructure Pipeline | Q-21 throttle doesn't break CF/AI/Seizure pipeline | All Church actions still fire at non-zero rates |
| T5-T-T15a-001 | T-15a Hafenmark Unmediated Sovereigntist | Charter of Liberties is institutional codification distinct from Church-mediated authority | Charter doesn't reduce to Church-coronation analog |
| T5-T-T13-001 | T13 Scale Transition Pipeline | Crown Initiative cross-scale: character → territory | Per-card-use, two-scale effects logged |

## §7.2 М-pattern verification

| Test ID | М pattern | Hypothesis | Pass criterion |
|---------|-----------|-----------|----------------|
| T5-M-1-001 | М-1 Pressure continuous | Chronic Turmoil 20-35 persists in RC-v1 | Mean Turmoil in [15, 40] |
| T5-M-2-001 | М-2 Geography holds pressure | Mode I Ob varies with territory Accord | Per-Mode-I-use Ob calc logged with territory state |
| T5-M-4-001 | М-4 Institutions stake substrate-postures | 4-faction differentiated postures preserved | Per-faction action selection differs by >40% |
| T5-M-5-001 | М-5 Scales connect | Character/territory/faction effects all observable | All three scale-effects per-campaign |
| T5-M-6-001 | М-6 Choice forced | Each faction faces meaningful decisions per season | Per-season action count ≥ 2.5 per faction |
| T5-M-11-001 | М-11 Voluntary/involuntary duality | Open Pledge breach = voluntary commit + involuntary consequence | Per-Mode-II-use, breach probability logged |

## §7.3 Failure lexicon clearance test (per proposal)

For each P1..P7, automated checks against 13 failure-lexicon terms (per `throughlines_meta.md`):

```python
failure_lexicon = [
    'fantasy_imposition', 'duplicate_coverage', 'edge_case', 'abstractable',
    'rest_state', 'dominant_strategy', 'flavor_only', 'scale_break',
    'reskinned_attractor', 'cost_hidden', 'strategic_only', 'personal_only',
    'authored_emergence'
]
```

Each proposal × 13 terms = 91 checks. Pass: 91/91 clear (or partial with justification).

---

# §8 EXECUTION SCHEDULE

## §8.1 Sequential dependencies

```
Phase 1 (independent) ─┬─→ Phase 2 (pairwise) ─┬─→ Phase 4 (integration)
                       │                       │
                       └─→ Phase 3 (canonical) ─┘
                                               │
                                               └─→ Phase 5 (throughline)
```

Phase 1 and Phase 3 can run in parallel.
Phase 2 requires Phase 1 of relevant proposals.
Phase 4 requires all of Phase 1, Phase 2, Phase 3.
Phase 5 requires Phase 4.

## §8.2 Resource estimate

| Phase | Tests | Sim runs per test | Total sim campaigns |
|-------|-------|-------------------|---------------------|
| Phase 1 | ~80 tests | 500 each | 40,000 |
| Phase 2 | ~30 tests | 500 each | 15,000 |
| Phase 3 | ~10 tests | Code/manual checks | <100 sim |
| Phase 4 | ~14 tests | 500 each | 7,000 |
| Phase 5 | ~20 tests | 500 each (subset) | 10,000 |
| **Total** | **~154 tests** | | **~72,000 campaigns** |

At v11 simulator throughput (~500 campaigns/30s), Phase 1-5 = ~70 min compute. Realistic.

## §8.3 Iteration order

1. **Iteration A — TIER-1 proposals only.** P1, P2, P3. Phase 1 (single) + Phase 4 (P1+P2+P3 integration).
2. **Iteration B — TIER-2 proposals.** Add P4, P5, P6 to RC-v1.
3. **Iteration C — Full RC-v1.** Phase 4 + Phase 5.
4. **Iteration D — Conditional P7.** Only if Varfell <15% post-Iteration C.

Stop at first iteration that delivers asymmetric balance in band; defer further iterations.

---

# §9 DELIVERABLE STRUCTURE PER PHASE

Each phase produces:

1. **`phase_N_results.json`** — machine-readable per-test result
   ```json
   {
     "test_id": "T1-P1-BU-N-001",
     "hypothesis": "Church win-share drops to 25-35%",
     "config": {...},
     "n_campaigns": 500,
     "result": {"Church_win_share": 28.4, ...},
     "pass": true,
     "fail_reason": null,
     "mechanical_log_path": "logs/T1-P1-BU-N-001.jsonl"
   }
   ```

2. **`phase_N_report.md`** — narrative synthesis per phase
3. **`logs/*.jsonl`** — granular mechanical logs (see companion specification)

---

# §10 FAILURE HANDLING

If any test fails:

1. **Triage**: is it a sim implementation bug, a proposal design flaw, or a canonical-interpretation error?
2. **Sim bug**: fix sim, re-run only affected tests.
3. **Proposal design flaw**: revise proposal; flag in editorial slate.
4. **Canonical interpretation error**: fetch canonical source; resolve interpretation; mark for Jordan editorial review.

Failed test = blocker for any downstream phase that depends on it. Do not proceed to integration phase with unresolved Phase 1 failures.

---

# §11 ACCEPTANCE CRITERIA FOR RATIFICATION

The RC-v1 package is recommended for Jordan ratification if and only if:

1. **All Phase 1 tests pass** for P1..P6 (P7 conditional)
2. **All P-14 implementability tests pass** (Phase 3)
3. **All Phase 5 throughline tests pass** (no T-breaks; ≥5 М-pattern extensions)
4. **Phase 4 integration test T4-INT-001 passes** (asymmetric band ±5pp)
5. **Phase 4 stress tests T4-STRESS-001..004 do not produce sim crashes**
6. **No failure-lexicon violations** detected
7. **Mechanical log integrity verified** (100% coverage; replayable)

If any acceptance criterion fails: iterate (revise proposal, re-test, re-evaluate). Do not ratify prematurely.

---

*Workplan · 2026-05-14*
*Authority: peninsular_strain_v30 + canon constraints P-01..P-15 + throughline registry*
*Companion: mechanical_log_specification_2026-05-14.md*
*Status: ready for execution; Iteration A (TIER-1) recommended first*
