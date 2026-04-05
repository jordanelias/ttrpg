# SIM-SOC-01: The Parliamentary Inquest

```
=================================================================
SIM-SOC-01  THE PARLIAMENTARY INQUEST
= Grand Contest | Non-Optimal Actor Simulation =
=================================================================

Scenario: Hafenmark Parliament. Motion: 'The Lowenritter dissolution
was Church-directed suppression, not lawful disbandment.'
Side A (PCs): Renn + Holt + Saya argue for suppression.
Side B (Church/Crown): Church Adv + Crown Adv argue dissolution.

Audience: Hafenmark (Categorical Imperative). Stability 4 = resistance 4.
Past genre boosted +0.5 for all (Hafenmark ethical mode).

Pool formula: (Cog x 2) + hist_pts  [PP-232]

Orator            Pool   Composure   Appraise  Archetype
-----------------------------------------------------------------
  Renn              11D          10          5D  Status-Preserving
  Holt              11D          11          3D  Impulsive
  Saya              15D           9          4D  Fatigued
  Church Adv.       14D          11          3D  Optimal
  Crown Adv.        11D          10          4D  Optimal

=== INITIATIVE ===
  Side A max Att=5 (Renn=5)  Side B max Att=4 (Crown=4)
  Initiative: Side A declares last -> information advantage
  [Non-optimal note: Holt (Att=3) always declares simultaneously, ignoring this advantage]

=================================================================
EXCHANGES 1–7
=================================================================

Ex   A-orator Genre/Or (A)       Genre/Or (B)        CT    Δ  Notes
------------------------------------------------------------------------------------------
  1   Renn     Present/Revealing   Past/Revealing     5    +0  CROSS: A(Present,11D,gw=0.5) E=3.3 ->0 | B(Past,14D,gw=1.0) E=4.2 ->0 [Renn refuses Past; CROSS]
  2   Holt     Past/Revealing   Past/Obscuring     5    +0  CLASH Past: A 12D E=3.6 vs B 14D E=4.2 margin=-0.6 gw=1.0 -> CT+0A / CT+0B ComA-1 ComB-0 [Holt Past (anger); Church Past/Obscuring; Holt Mom spent]
  3   Saya     Future/Revealing   Past/Revealing     5    +0  CROSS: A(Future,15D,gw=0.5) E=4.5 ->0 | B(Past,14D,gw=1.0) E=4.2 ->0 [Saya refuses AMPLIFY; solo Future gw=0.5; Church Past gw=1.0]
  4   Renn     Present/Revealing   Present/Revealing     5    +0  CLASH(same orient) Present: A 3.3 vs B 3.3 margin=0.0 gw=0.5 -> CT+0A / +0B [Renn vs Crown; both Present/Revealing; CLASH; initiative unused]

  [CT after Ex4: 5]
  Saya (Fatigued) evaluates: CT=5 is not winning. Considers conceding.
  Fatigued rule: Saya concedes if CT at 4-5 and opponent seems strong.
  5   Holt     Past/Revealing   Past/Revealing     5    +0  CLASH(same orient) Past: A 7.8 vs B 4.2 margin=3.6 gw=1.0 -> CT+0A / +0B [Holt+Saya AMPLIFY]

  [Ex6: Renn checks. P(Composure loss) = 50% > 20% threshold]
  Renn (Status-Preserving) PASSES on Ex6. Will not argue.
  6   (pass)   —/—                 Past/Revealing        5    +0  Unopposed Church E=4.2 Past gw=1.0 -> CT-0

  [CT after Ex6: 5. Side A needs CT >= 7. Currently 5. Need +2 more.]
  Saya (Fatigued): evaluates. Composure=9. Reframe only at Composure<=2.
  CT=5. Needs 2 more to win. Saya pool=15D vs Church 14D.
  Fatigued rule: if Partial is achievable, accept it and stop.
  Saya Past/Revealing vs Church Past/Revealing: margin=0.3 CT move=0
  CT movement = 0 (below resistance). Saya accepts this as 'partial' and concedes.
  7   Saya     Past/Revealing      Past/Revealing        5    +0  Saya final push; Fatigued accepts 0 move

=================================================================
CONTEST FINAL STATE
=================================================================

  Final CT: 5  (Side A wins >= 7 | Side B wins <= 3)

  Outcome: DRAW

  Composure remaining:
    Renn:    10/10
    Holt:    10/11
    Saya:    9/9
    Church:  7/11
    Crown:   10/10

  CP earned: Renn=3 Holt=2 Saya=2
  Momentum remaining: Renn=2 Holt=2 Saya=1

  Narrative: The Parliamentary inquest ends without a decisive verdict.
  Hafenmark council records 'matter contested but unresolved' — no Domain Echo fires.
  Church retains status quo (dissolution classified as lawful). Side A fails to prove.

=================================================================
SIM-SOC-01  FULL FINDINGS AUDIT
=================================================================

Total findings: 14
P1 (critical): 5 | P2 (significant): 8 | P3 (minor): 1

--- P1 CRITICAL ---
[P1] SIM-SOC-F04: Saya (Fatigued) has AMPLIFY opportunity with Holt (both 
  could argue Past: Holt 11D + Saya 15D, cap=30D, effective=26D, E=7.8 vs 
  Church 14D E=4.2, CLASH margin 3.6, Past gw=1.0, CT movement = 
  floor(3.6x1.0x1.0 - 4) = 0 -> actually just at resistance. AMPLIFY 
  would break through resistance with large margin). Instead Saya argues 
  Future alone (15D gw=0.5): E=4.5, CT move = floor(4.5x0.5 - 4) = 0. 
  Fatigued actor sacrifices highest-EV action available. This is a P1 
  finding: Fatigued archetype produces zero CT movement in exchanges 
  where their pool would have been decisive if deployed correctly. 
[P1] SIM-SOC-F08: Critical Ex7: Saya (Fatigued, pool=15D) achieves 0 CT 
  movement arguing Past because margin (4.5-4.2=0.3) x gw(1.0) x ow(1.0) 
  = 0.3 < resistance(4). She accepts this partial result (marginal 
  positive margin) without escalating. Optimal play: Saya should spend 
  her 1 Momentum (+1 success) to push margin to 1.3, CT move = 
  floor(1.3-4) = 0 still insufficient. Alternative: AMPLIFY with any 
  available ally for combined pool. Fatigued actor cannot push through 
  resistance ceiling even with the highest individual pool. This reveals 
  a structural finding: resistance=4 (Stability 4) creates a hard floor 
  that individual pools cannot breach without combined action or Momentum 
  stacking. 
[P1] SIM-SOC-F09: STRUCTURAL: CT resistance=4 (= Stability directly) 
  makes the contest system mechanically inert. At resistance=4, breaking 
  through requires a 13D pool advantage in the best genre (Past) or 27D 
  advantage in non-boosted genres. No realistic PC build can achieve this 
  individually. Even AMPLIFY (26D combined vs 14D = margin 3.6) produces 
  CT+0 (floor(3.6-4)=0). Root cause: resistance = raw Stability (1-7 
  scale) is not scaled to the dice pool math. Proposed fix: resistance = 
  ceil(Stability / 4). At Stability 4 -> resistance 1. At resistance=1: 
  AMPLIFY 26D vs 14D gives CT+2; individual CLASH still hard (4D 
  advantage needed). System becomes playable: AMPLIFY is rewarded, 
  individual clashes require pool advantage. PP-278 proposed. 
[P1] SIM-SOC-F10: COROLLARY to F09: All 7 contest exchanges produced 
  CT+0. Final CT = 5 (identical to starting CT). Contest is mechanically 
  frozen — the narrative result (draw, status quo retained) is entirely 
  determined by resistance, not by the players' choices or pool sizes. A 
  contest at resistance=4 is equivalent to no contest at all from a CT 
  perspective. Domain Echo cannot fire; no faction stats change; no 
  Beliefs can be achieved through contesting. This would make the entire 
  social contest subsystem unusable in Stability 4+ factions. 
[P1] SIM-SOC-F13: Non-optimal actor analysis (Saya, Fatigued): Saya's 
  refusal to AMPLIFY in Ex3/5 is the most consequential non-optimality. 
  At resistance=1 (corrected): AMPLIFY 26D vs 14D gives CT+2. Saya's 
  refusal to AMPLIFY costs Side A 2 CT points per eligible exchange. In a 
  7-exchange contest, 2 potential AMPLIFY opportunities = 4 CT points 
  foregone. Side A starts at CT=5, needs CT=7. Saya's Fatigue alone costs 
  the win. This is a clean, observable non-optimal consequence — design 
  validates correctly once resistance is patched. 

--- P2 SIGNIFICANT ---
[P2] SIM-SOC-F01: Impulsive actor (Holt, Att=3) ignores initiative 
  structure — declares simultaneously with opponent instead of waiting. 
  Renn (Att=5) holds initiative advantage but Status-Preserving archetype 
  will only use it to confirm a safe exchange, not to exploit a winning 
  position. Neither PC leverages the initiative mechanic optimally. 
[P2] SIM-SOC-F02: Renn (Status-Preserving) refuses Past genre despite 
  Past weight=1.0 for Hafenmark audience. Picks Present (weight=0.5). 
  This halves their effective CT movement per exchange. A 
  status-preserving actor systematically underperforms in audiences whose 
  ethical mode boosts the genre they're avoiding. In any Church-adjacent 
  session before Hafenmark or Hafenmark-aligned audience, refusing Past 
  is a persistent 50% CT efficiency penalty. 
[P2] SIM-SOC-F03: Holt (Impulsive) spends Momentum at CT=5 (neutral) — 
  not a winning position. Optimal play reserves Momentum for exchanges 
  where CT is at 6+ (pressing a lead). Impulsive actor burns Momentum for 
  emotional reasons: anger after Ex1's poor result. Net effect: +1 auto 
  success this exchange, but resource depleted for future critical 
  exchanges. 
[P2] SIM-SOC-F05: Renn has initiative advantage (Att=5 > Crown Att=4) in 
  Ex4: sees Crown pick Present/Revealing. Optimal response: shift to 
  Present/Obscuring to force CLASH on own terms, or shift to Past to 
  avoid CROSS and control genre interaction. Status-Preserving Renn does 
  neither — stays Present/Revealing regardless. Initiative advantage 
  completely wasted: same as if no Appraise occurred. 
[P2] SIM-SOC-F07: Renn (Status-Preserving) refuses Ex6 when facing 
  equal-pool Crown advocate. P(Composure loss) ~50% > 20% threshold. Renn 
  passes. This means Side A has only Holt and Saya available — both also 
  sub-optimal. A status-preserving archetype becomes increasingly inert 
  as CT approaches critical moments, because equal-pool exchanges are the 
  norm in competitive social contests. 
[P2] SIM-SOC-F11: Non-optimal actor analysis (Renn, Status-Preserving): 
  Genre avoidance (refusing Past) halves CT weight from 1.0 to 0.5, but 
  at resistance=4 neither weight produces movement. Genre restriction is 
  a non-issue when resistance exceeds any realistic output. After 
  resistance fix: genre avoidance would produce a real cost (0.5 vs 1.0 
  weight). SIM result shows that non-optimal actors cannot be evaluated 
  until resistance is corrected. 
[P2] SIM-SOC-F12: Non-optimal actor analysis (Holt, Impulsive): Momentum 
  spend in Ex2 (+1D, net pool 12D vs Church 14D) produced no CT change. 
  At resistance=4, the +0.3 E[net] from Momentum is irrelevant. After 
  resistance fix: Momentum spend on a losing CLASH is still waste 
  (negative margin). Impulsive Momentum-burning on losing exchanges is a 
  genuine non-optimality, but only observable once the resistance floor 
  is corrected. 
[P2] SIM-SOC-F14: Initiative mechanic finding: Renn (Att=5) holds 
  initiative advantage over all opponents. In 3 of 4 exchanges Renn 
  participates in, she has information advantage (sees opponent genre 
  first). Status-Preserving archetype uses this information only to 
  confirm her pre-decided genre (Present), never to exploit it. Optimal 
  use: shift genre on seeing opponent pick Past to force a CROSS on a 
  neutral genre rather than allowing Church to accumulate Past weight. 
  Initiative advantage is mechanically meaningful but requires proactive 
  genre-switching to leverage. 

--- P3 MINOR ---
[P3] SIM-SOC-F15: Composure damage in contested exchanges is near-zero at 
  equal pool levels (11D vs 14D). Only CLASH margin >= 1 produces 
  composure damage. At equal pools, E[margin] ~ 0. Composure track 
  appears largely decorative in contests between well-matched orators 
  unless one side significantly outmatches the other (3+ pool 
  difference). This aligns with design intent (Composure = buffer before 
  concession) but means Composure is rarely at risk in competitive 
  contests — only in asymmetric ones. 

=================================================================
PATCH PROPOSALS FROM SIM-SOC-01
=================================================================

PP-278 [P1]: params_debate.md — resistance formula
  Change: resistance = raw Stability (1-7) -> resistance = ceil(Stability / 4)
  Rationale: raw Stability produces a floor (res=4) that no realistic pool can breach.
  At resistance=1 (Stability 4): AMPLIFY is rewarded, CLASH requires pool advantage.
  Effect: all 7-exchange simulated contests produce zero CT movement at Stability 4.
  After patch: AMPLIFY 26D vs 14D = CT+2; individual CLASH 4D advantage = CT+1.

PP-279 [P2]: params_debate.md — document genre/orient weight interaction explicitly
  Current: genre weights and orientation weights described separately.
  Gap: no example showing combined effect (gw x ow x margin vs resistance).
  Add: worked example with numbers showing when CT movement occurs.
  Rationale: GMs will miscalculate without a concrete walkthrough.

=================================================================
7-DIMENSION TAG — SIM-SOC-01
=================================================================

Test ID: SIM-SOC-01
Mechanics: Grand Contest (CT, resistance, genre/orient weights, AMPLIFY, initiative, Composure)
Mode: TTRPG
Temporal: Single session (7 exchanges)
Tracks: CT (Conviction Track), Composure (all orators), Momentum
Factions: Church, Crown, Hafenmark (audience)
NPCs: Church Advocate, Crown Advocate
Archetypes: Status-Preserving (Renn), Impulsive (Holt), Fatigued (Saya)
Status: Complete — P1 structural finding (resistance formula), P1 non-optimal finding (AMPLIFY refusal)


```
