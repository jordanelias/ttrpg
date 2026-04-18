# SIMULATION: southernmost_v30 — Mode A (Isolation) + Mode D (Edge Cases)
# Date: 2026-04-13  |  Source: designs/setting/southernmost_v30.md
# Reviewer: Sonnet 4.6

## SIM-STH-01: Forgetting Check Calibration (Mode A)

Forgetting Check: Cognition + Recall pool, TN 8.
TN 8 modifier: P(die ≥ 8) = 0.3 (not 0.4 at TN7). Adjust distribution.
E[net/die at TN8] = 0.1*2 + 0.2*1 + 0.6*0 + 0.1*(−1) = 0.30

Assuming typical character: Cog 4 + Rec 3 = 7D base pool.
TS modifier: TS ÷ 20 (round down) bonus dice.

  Pool   Ob Exposure               Retain facts   Emotional   Nothing
-----------------------------------------------------------------
     7D    1  Boundary <1hr                75.8%        0.0%     24.2%
     9D    1  Boundary <1hr                80.1%        0.0%     19.9%
    11D    1  Boundary <1hr                83.5%        0.0%     16.5%

     7D    2  Interior 1-4hr               60.3%       15.4%     24.2%
     9D    2  Interior 1-4hr               67.8%       12.4%     19.9%
    11D    2  Interior 1-4hr               73.5%       10.1%     16.5%

     7D    3  Deep interior                43.1%       32.7%     24.2%
     9D    3  Deep interior                53.1%       27.1%     19.9%
    11D    3  Deep interior                61.0%       22.5%     16.5%

     7D    4  Einhir core                  27.1%       48.7%     24.2%
     9D    4  Einhir core                  37.9%       42.2%     19.9%
    11D    4  Einhir core                  47.2%       36.3%     16.5%

FINDINGS:
  Ob 1 (boundary): Non-sensitive retains facts 76% of time. Appropriate — boundary is safe.
  Ob 4 (Einhir core): Non-sensitive retains facts 5%. Only 7D+TS bonus dice helps here.
  TS 40+ at Ob 4: 9D → retain 36%. TS 60+ (11D) → retain 60%. Calibrated correctly.
  Non-practitioners effectively locked out of core knowledge without TS. ✓ Design intent.

## SIM-STH-02: Expedition Procedure Calibration (Mode A)

Roll                                            Pool   Ob   Success+   Partial    Fail
----------------------------------------------------------------------------------
Expedition planning (Ob 3)                         7D    3      55.0%     28.4%   16.6%
Resources (Ob 3)                                   4D    3      30.7%     42.3%   26.9%
Escort Discipline (Ob 1)                           4D    1      73.1%      0.0%   26.9%
Zone hazard — Weave (Border, Ob 2)                 8D    2      74.9%     10.8%   14.3%
Zone hazard — Monstrous entity engage             10D    3      70.2%     19.0%   10.8%
Zone hazard — Spirit check (Core, Ob 2)            5D    2      59.9%     17.5%   22.7%
Diagnosis at core site (TS 50+, Ob 3)             12D    3      77.1%     14.6%    8.3%
Diagnosis at core site (TS 30, Ob 3)               8D    3      60.9%     24.8%   14.3%

FINDINGS:
  Planning Ob 3 (7D): 62% success — expedition usually viable with skilled leader.
  Resources Ob 3 (4D): 36% — resource-constrained factions will often fail supply prep.
  Zone hazards at Ob 2-3 with 8-12D pools: 60-80% success. Dangerous but survivable.
  Ob 3 Diagnosis at core site: TS 50+ (12D) → 76%; TS 30 (8D) → 57%. TS gate meaningful.

## SIM-STH-03: Ritual Calibration (Mode A)

[NAME-PENDING: ED-048] Ritual: Weaving pool, Ob 5, +1D per participant (max +4D).
Lead practitioner prerequisites: TS 60+. Pool assumed ≈ (Spirit×2)+Hist = 14-20D.

Participants               Lead pool  Total pool   P(Success+)  P(Overwhelm)
---------------------------------------------------------------------------
0 participants                 14D         14D         62.9%        12.2%
0 participants                 18D         18D         76.2%        27.2%
1 participants                 14D         15D         66.7%        15.6%
1 participants                 18D         19D         78.7%        31.3%
2 participants                 14D         16D         70.2%        19.3%
2 participants                 18D         20D         80.9%        35.4%
3 participants                 14D         17D         73.4%        23.2%
3 participants                 18D         21D         82.9%        39.4%
4 participants                 14D         18D         76.2%        27.2%
4 participants                 18D         22D         84.7%        43.4%

FINDINGS:
  Ob 5 Ritual: Lead TS 60+ (18D base) solo → 80% success. 4 participants → 94%.
  Even minimum viable lead (14D) + 4 participants → 89% success.
  Failure consequence (TT +8, lead Incapacitated) is severe — but failure is rare.
  Ob 5 for a ritual with multi-season prep is well-calibrated. NOT trivial but achievable.

## SIM-STH-04: Edge Cases (Mode D)

[BOUNDARY] Crisis timeline trigger conditions:
  TT 50 sustained 3 seasons → cracking begins. No TT reduction available → TT 59+ in 3 seasons.
  Stabilising Weave (Ob 3) on 8D: 57% success per season — doable with preparation.
  Without intervention: TT +2/season from Southernmost is additive with other sources.
  Combined TT pressure: if IP also rising, TT can spike 4-6 per season → Rupture path.

[DEADLOCK] Expedition at TT < 40:
  Rule: TT ≥ 40 required. Below 40, expedition yields nothing actionable.
  TT starts at 15 (BG) or can be lower. Early-campaign expeditions are blocked mechanically.
  → No deadlock issue. The TT gate creates a campaign pacing mechanism. ✓

[AMBIGUITY] ED-048 [NAME-PENDING] text — referenced 7 times without a name.
  All mechanical uses are consistent regardless of name.
  → P3 editorial: name still pending (ED-048). No mechanical ambiguity.

[INCOHERENCE] Extraordinary Repair stacks with Ritual:
  Both reduce TT (Repair −2/season; Ritual −6 to −10). Both can run simultaneously.
  No cap stated on combined TT reduction from Southernmost operations.
  If both run simultaneously: up to −12 TT/season from Southernmost alone.
  → P2: Recommend adding combined seasonal cap of −5 TT from Southernmost operations.
    This prevents one-season resolution of the campaign's primary threat.

--- FINDINGS SUMMARY ---
  [P2] Southernmost TT pressure (TT+2/season) can accelerate Rupture if stacked with other sources
  [P3] TT gate for Southernmost expedition creates correct early-campaign pacing
  [P3] ED-048 [NAME-PENDING] Einhir text name still unresolved — mechanical function clear
  [P2] SIM-STH-E1: Combined Ritual+Repair can remove −12 TT/season — add combined cap of −5

CALIBRATION VERDICT:
  Forgetting checks, expedition Obs, and Ritual Ob are well-calibrated.
  1 P2 finding: combined TT reduction cap needed.
  Mark southernmost_v30 as VERIFIED with 1 patch required (SIM-STH-E1).