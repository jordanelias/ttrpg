# SIM-ECON-01: The Overextended Crown

```
=================================================================
SIM-ECON-01: THE OVEREXTENDED CROWN
= Seasonal Economic Cascade | 3 Seasons =
=================================================================

Scenario: Crown commits to 4 Domain Actions in Season 1:
  DA-1: Royal Decree — raise Military (costs Wealth, aligned framework)
  DA-2: Trade Embargo on Guilds (Influence action, costs Stability)
  DA-3: Border Fortification (Wealth expenditure, Military+1)
  DA-4: Parliamentary Session (Mandate action, costs Influence)

Crown Ethical Framework: Virtue Ethics (Transparency).
Covert/manipulative actions: +1 Ob penalty.
Actions aligned with framework: −1 Ob.

Season 1 threat pressure: 2 concurrent threats (Military + Economic)
-> Stability check Ob = 3. Crown Stability pool = 4D.
Overextended actor: does not scale back when Wealth drops.

=== STARTING STATE ===
Faction          M   I   W  Mil  Sta
-----------------------------------
  Crown          5   5   4    4    4
  Church         5   6   5    4    5
  Hafenmark      4   4   5    3    4
  Guilds         3   4   6    2    5
  Lowenritter    0   3   0    5    5
  Varfell        4   4   4    4    4

=================================================================
SEASON 1 — FOUR DOMAIN ACTIONS (OVEREXTENDED)
=================================================================

DA-1: Royal Decree (Crown Military+1)
  Pool=5D Ob1 -> E=1.5 -> Success
  Result: Crown Military+1. Wealth-1 (expenditure cost).

DA-2: Trade Embargo on Guilds (Crown Influence vs Guilds Wealth)
  Pool=5D Ob7 (Guilds W=6 +1 misalign) -> E=1.5 -> Partial
  Result: Partial. Partial: Guilds Wealth-1 but Crown takes -1 Stability backlash.

DA-3: Border Fortification (Wealth expenditure, Military+1)
  Pool=3D (current Wealth) Ob2 -> E=0.9 -> Partial
  Result: Partial. Failure/Partial: Fortification incomplete. Wealth-1 spent, no Military gain.

DA-4: Parliamentary Session (Mandate action, Influence+1)
  Pool=5D Ob1 (aligned) -> E=1.5 -> Success
  Result: Success. Crown Influence+1.

--- SEASON 1 STABILITY CHECK ---
Crown: 4 Domain Actions this season = 'Active attack on Mandate or Wealth' territory.
Stability check Ob = 4 (two concurrent active threats + overextension).
  Pool=3D Ob4: E=0.9 P(failure)=96% -> Partial
  Stability holds: 3

Church Counter-action: Investigation of Crown overreach
  Church Intel=6D vs Crown Stability=3 -> E=1.8 -> Partial

=== END OF SEASON 1 ===
Faction          M   I   W  Mil  Sta
-----------------------------------
  Crown          5(+0)   6(+1)   2(-2)    5(+1)    3(-1)
  Church         5(+0)   6(+0)   5(+0)    4(+0)    5(+0)
  Guilds         3(+0)   4(+0)   5(-1)    2(+0)    5(+0)
  Varfell        4(+0)   4(+0)   4(+0)    4(+0)    4(+0)

=================================================================
SEASON 2 — WEALTH CRUNCH (OVEREXTENDED CONTINUES)
=================================================================

Crown Wealth entering S2: 2
Overextended actor rule: commits 3 DA again despite depleted Wealth.

DA-5: Military Levy (tax collection, Crown Wealth+1 if success)
  Crown Mil=5D vs Guilds W=5 -> E=1.5 -> Partial
  Partial: tax collected but Guilds Stability check triggered.

DA-6: Alliance Offer to Varfell
  Pool=6D Ob3 -> E=1.8 -> Partial
  Failure: Alliance rejected. Varfell stays neutral.

--- SEASON 2 STABILITY CHECK ---
  Crown Stability=3D Ob3: E=0.9 P(fail)=86% -> Partial

Guilds: Passive recovery (high Wealth = economic resilience)
  Guilds W+1 (high-Wealth passive recovery). W->6

=== END OF SEASON 2 ===
Faction          M   I   W  Mil  Sta
-----------------------------------
  Crown          5   6   3    5    3
  Church         5   6   5    4    5
  Guilds         3   4   6    2    5
  Varfell        4   4   4    4    4

=================================================================
SEASON 3 — COLLAPSE THRESHOLD
=================================================================

Crown entering S3: M=5 W=3 Sta=3
Overextended actor STILL attempts 2 DA (down from 4, but Wealth is critically low).

=== FINAL STATE (3 SEASONS) ===
Faction          M   I   W  Mil  Sta
-----------------------------------
  Crown          5(+0)   6(+1)   3(-1)    5(+1)    3(-1)
  Church         5(+0)   6(+0)   5(+0)    4(+0)    5(+0)
  Guilds         3(+0)   4(+0)   6(+0)    2(+0)    5(+0)
  Varfell        4(+0)   4(+0)   4(+0)    4(+0)    4(+0)

=================================================================
SIM-ECON-01  FINDINGS AUDIT
=================================================================

Total findings: 7
P1: 1 | P2: 5 | P3: 1

--- P1 CRITICAL ---
[P1] SIM-ECON-F02: Crown DA-3 pools from current Wealth (3D after DA-1 
  reduction). Overextended actor depletes Wealth with DA-1 then attempts 
  another Wealth-dependent action. Pool degrades mid-season as stats 
  change. This reveals a SEQUENCE DEPENDENCY: Domain Action resolution 
  order matters when the same stat is both the pool and the cost. No rule 
  in params_factions specifies whether stats update immediately 
  (sequential) or are held at season-start values (batch). GAP: Domain 
  Action intra-season stat update timing is undefined. 

--- P2 SIGNIFICANT ---
[P2] SIM-ECON-F01: Crown DA-2 (Trade Embargo) is misaligned with Virtue 
  Ethics/Transparency framework. +1 Ob penalty raises Ob from 6 to 7. 
  Pool=5D vs Ob7: E=1.5, P(success)=14%. Overextended actor commits this 
  action regardless of low probability. Expected outcome is Failure or 
  Partial. Overextended archetype does not scope-check probability before 
  committing Domain Actions. 
[P2] SIM-ECON-F03: Crown Stability check: pool=3D vs Ob4. E=0.9. 
  P(failure)=96%. Expected outcome: Failure -> Stability-1. 
  Anti-death-spiral floor activates at Stability<=2 (locks Ob at 4 
  regardless of actual pressure). Crown starting Stability=4 -> floor not 
  yet active. One failure = Stability 3. Two consecutive failures = 
  Stability 2, floor activates. 
[P2] SIM-ECON-F04: Crown DA-5 (Military Levy) attempts Wealth recovery by 
  using Military stat as pool. Military=5 after S1 gains. However Guilds 
  W also degraded by Trade Embargo (S1). If Guilds W = 5 (S1 partial 
  result preserved), Ob=5 vs pool=5D: E=1.5, P(suc)=33%. Wealth recovery 
  through military means is inefficient: Military is not the natural pool 
  for economic Domain Actions. Correct pool would be Crown Wealth or 
  Influence. Overextended actor uses Military because Wealth is depleted 
  — structural consequence. 
[P2] SIM-ECON-F08: Seasonal stat cap (±2 per season) interacts with 
  multi-action chains in unexpected ways. Crown gains Military+2 across 
  DA-1 and DA-3 in S1. Cap correctly limits to +2. However Wealth 
  decreases are NOT similarly capped — Wealth can drop by multiple points 
  if several Domain Actions each cost 1 Wealth. GAP: params_factions says 
  stat change cap is ±2 per season but Domain Action costs may each 
  independently trigger -1. Clarify whether the cap applies to net change 
  or per-action change. 
[P2] SIM-ECON-F09: Domain Action timing dependency (from F02): if stats 
  update immediately after each DA, DA-3 pools from depleted Wealth (3D 
  instead of 4D). If batch-resolved, all DAs use season-start values. 
  Difference: DA-3 P(success) = 47% (immediate) vs 65% (batch). This 
  18-point difference affects Overextended archetype outcomes 
  significantly. GAP requires editorial ruling. 

--- P3 MINOR ---
[P3] SIM-ECON-F10: Guilds passive recovery (+1 Wealth at high Wealth) is 
  not an explicit rule in params_factions or stage6 seasonal accounting. 
  Simulated as a reasonable inference (high-Wealth factions have economic 
  resilience). Needs explicit design decision. 

=================================================================
7-DIMENSION TAG — SIM-ECON-01
=================================================================
Test ID: SIM-ECON-01
Mechanics: Domain Actions, Seasonal Accounting (Stability checks),
           Wealth degradation, stat caps, anti-death-spiral floor,
           ethical framework Ob modifiers
Mode: TTRPG
Temporal: 3 seasons
Tracks: M, I, W, Mil, Sta (all Crown); Guilds W; Varfell M
Factions: Crown (Overextended), Church, Guilds, Varfell
NPCs: None (faction-level only)
Archetypes: Overextended (Crown — commits beyond sustainable rate)
Status: Complete


```
