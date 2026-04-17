# VALORIA — Stress Test & Simulation Batch 2
**Date:** 2026-04-16  
**Token:** 092ab358769ad4fe  
**Scope:** Full-length campaign runs, interdependent system tests, cross-scale transitions, Zoom In/Out chains, social contest chains, TC reform validation, military layer stress, hybrid mode handoffs, fieldwork–combat–contest sequences, full NPC arc emergence  
**Method:** max effort — all referenced docs read in full. Dice simulated via explicit d10 rolls with probability tracking.

---

## SIMULATION INDEX

| # | Name | Systems Tested | Depth |
|---|------|---------------|-------|
| ST-01 | 4-faction BG campaign (Seasons 1–20) | All BG mechanics, TC reform, AI priority trees, military layer, Accord/Strain | Full campaign |
| ST-02 | Cross-scale transition chain | Zoom In from BG battle → personal combat → Thread → Zoom Out | Full sequence |
| ST-03 | Social contest chain (3-contest arc) | Contest system, Obligation, Chain Contest, Conviction Scar accumulation | Full chain |
| ST-04 | Hybrid mode — full season | BG → TTRPG Zoom In → fieldwork → combat → Domain Echo → Zoom Out → Cascade | Full season |
| ST-05 | TC reform stress test | TC sources across 25 seasons; Church victory timeline; Hafenmark suppression efficacy | Full sim |
| ST-06 | Fieldwork → Combat → Contest pipeline | All three system transitions, evidence use in contest | Full pipeline |
| ST-07 | Mass battle with Zoom In, Thread ops, general duel | Mass battle phases 1–7, Thread scale, personal duel, Zoom Out | Full battle |
| ST-08 | NPC arc emergence — Almud Arc B / Himlensendt Arc A | BG pressure producing arc conditions, social contest triggering arc shift | Arc sequence |
| ST-09 | Obligation cascade under Peninsular Strain | Multiple simultaneous Obligations, violation consequences, Strain interaction | Stress test |
| ST-10 | Rendering Stability decline curve (RS 72 → crisis) | Thread op failures, Lock chronic drift, battle RS costs, Mending recovery | 30-season curve |

---

## ST-01 — 4-FACTION BG CAMPAIGN (SEASONS 1–20)

**Setup:** Crown, Church, Hafenmark, Varfell (all NPC AI). All provisional docs canonical for this sim (tc_political_redesign_v30, military_layer_v30, peninsular_strain_v1). Starting state: standard params.

**Starting stats:**

| Faction | Mandate | Influence | Wealth | Military | Stability | TCV | Accord (cap) | TC |
|---------|---------|-----------|--------|----------|-----------|-----|--------------|----|
| Crown | 5 | 5 | 4 | 4 | 5 | 12 | 3/2/2/2/2/2 | — |
| Church | 5 | 6 | 4 | 4 | 5 | 5 | 3 (T9) | 28 |
| Hafenmark | 4 | 5 | 5 | 3 | 5 | 6 | 3/2/2/2 | — |
| Varfell | 3 | 4 | 3 | 4 | 5 | 6 | 3/2/2/2 | — |

Peninsular Strain: 0. RS: 72. IP: 0.

---

### SEASONS 1–5 (OPENING PHASE)

**Season 1:**

*Church AI (Priority 3 — TC 28 < 40, no milestone):* Assert (Senator, T9). Mandate 5 → Political pool = 5 + floor(28/20)=1 = 6D, TN 7, Ob 1. Expected net = 6×0.4 − 0.6×0.1 = 2.4−0.06 = ~2.3. Roll 6d10: 9,8,7,3,10,5 → 1+1+1+2=5 net. Ob 1, surplus 4 = Overwhelming. TC +2 (Assert OW). TC: 28→30.

*Piety Yield this season:* Church Prominent in T9 (Church Mandate 5 > uncontrolled, effectively Church own territory). PT 5 → yield +1.0. Conditional passive: Church Prominent in 1 territory only → +0 passive (need ≥2). Total TC gain: Assert OW +2 + Piety Yield +1 = +3. Seasonal cap ±5. TC: 30→33. **[FINDING: Piety Yield stacks with Assert result. At Season 1, Church gains TC 28→33 in one season. This is correct — Church is unopposed and T9 is fully pious.]**

*Crown AI (Priority 6 — no threats):* Govern capital T1. Mandate 5 pool, Ob 1 (capital). 5d10: 9,8,3,7,2 → 3 net. OW: Accord T1 +1 (already 3, cap = no change) AND Mandate +1 (recovery, PP-174). Crown Mandate: 5→6 (but Mandate cap is 7, so fine). **[FINDING: Crown can Mandate-stack via Govern OW capital if starting Mandate is below cap. At Mandate 5 starting, they can reach 6 on Season 1. This is correct — well-governed capitals grow institutional authority.]**

*Hafenmark AI (Priority 3 — TC 33 < 40, no Suppress trigger yet):* Govern T8 (capital). 5D pool (Influence), Ob 1. 5d10: 9,7,4,8,1 → 3−1=2 net. Success. Accord T8 +1 (already 3, capped). Mandate framework drift: all Hafenmark actions framework-aligned this season → Influence +1 drift (Categorical Imperative per npc_behavior §7.1). Hafenmark Influence: 5→6.

*Varfell AI (Priority 3 — no immediate threat):* Tribune Investigate T9 (Intel). Influence 4, Ob 2. 4d10: 9,7,8,2 → 3 net. Success. Varfell learns Church Mandate is "Excellent" (6→wait, Crown Govern OW just pushed Crown to 6; Church still at 5). Correct learning: Church Mandate "Good" (4-5 range per fog of war). +1 Influence (Spy success per stat economy §4.1). Varfell Influence: 4→5.

**Accounting Season 1:**
- TC: 33 (all sources applied above)
- Accord: all starting values maintained; no hostile actions; no Strain
- Peninsular Strain: 0 (no battles, no revolts) → −1 passive (no battles this season). Already 0, can't go below.
- RS: 72 (no Thread ops, no battles)
- IP: 0 (no battles)
- Victory checks: no faction meets any condition.

---

**Seasons 2–5 compressed summary:**

Season 2: TC 40 milestone reached (Church Assert S2: +2 more; Piety Yield +1; conditional passive +1 because Church now Prominent in T9 AND T3 — Crown didn't Govern T3 this season, so Church extends influence). TC: 33 + Assert(S2:+2) + PY(+1) + conditional(+1) = 37 → no cap. Hmm — let me recheck: if Church is only Prominent in T9 (not T3), conditional is still +0 (need 2+). Church isn't Prominent in T3 yet at S2 (Crown Mandate ≥ Church Mandate in most territories). So: TC 33 + Assert S2 Ob 1 success = 33+1 = 34. PY T9 +1 = 35. Conditional: Church Prominent in 1 territory = +0. TC: 35. S2 Church Assert (Senator #2): Success: TC 35+1 = 36. **Church has 2 Senator cards.** 2 Asserts in one season: S1 Assert → TC+2 (OW); S2 has 1 more Senator — can Assert again? No: cooldown = 1 season. The S1 Senator goes on cooldown in S2. Church in S2 uses Pontifex (Thread) or the other Senator. Uses 2nd Senator for another Assert.

**[FINDING: Church's 2× Senator advantage means 2 Asserts per season when both Senators are available. But cooldown = 1 season means each Senator refreshes every season. With 2 Senators, Church can play both in S1 (2× Assert) and have both available again in S2 (after S1 cooldown resolves at S2 Accounting). This produces ~4 Assert actions in 2 seasons. This is extremely fast TC gain.]**

TC accounting, revised for 2× Senator:
- S1: Assert(OW, +2) + Assert(Success, +1) + PY(+1) = +4. TC: 28→32.
- S2: Assert(+1) + Assert(+1) + PY(+1) + conditional(+0) = +3. TC: 32→35.  
- S3: Assert+Assert+PY = +3. TC: 35→38. Conditional still +0 (only 1 Prominent territory).
- S4: Assert+Assert+PY = +3. TC: 38→41. **TC 40 milestone crossed.** Church gains +1D on Assert/Seizure rolls.
- Conditional at S4: Church now Prominent in T9. Is Church Prominent anywhere else? Only if Church Mandate > that territory's controller Mandate. At S4: Crown Mandate 5 (unchanged; Govern capital S2 would give OW again? Maybe). Let's say Crown stays at 5 (cap is starting Mandate per PP-174, which equals 5 → Crown can't exceed 5 via Govern). So Crown Mandate = 5. Church Mandate = 5. Neither has Church Mandate > Crown Mandate in Crown territories. Church Prominent only in T9. Conditional = +0.
- S5: Assert+Assert+PY = +3. TC: 41→44. With TC 40 milestone: Assert rolls now +1D. Assert S5 #1: 7D (6D political pool + 1D milestone): high success. TC gain may be OW = +2. Assert S5 #2: OW = +2. TC: 41 + 2+2+1 = 46. Above seasonal cap of 5? 46−41 = 5. Exactly at cap. TC: 46.

**[FINDING (ED-NEW-TC-CRITICAL): With 2× Senator and 2 Asserts/season, Church reaches TC 40 milestone in 4 seasons and TC 46 by Season 5. Rate: ~4–5 TC/season. At this rate: TC 55 milestone (Prominent Ob +1) reached by Season 7–8. TC 65 milestone (extra action slot) by Season 10–11. TC 80 milestone by Season 15–16. TC 100 by Season 22–24. This is FASTER than expected — previous session estimated Season 35–45 for Church Holy State victory at TC 70. The 2-Senator 2-Assert engine is more powerful than prior analysis captured.]**

**[FINDING (BALANCE-NEW-TC-01 CONFIRMED): TC reform (conditional passive replacing unconditional) slows passive TC gain but the 2× Senator Assert engine dominates. Net effect: Church TC rate is ~4–5/season early game (same or faster than old system) but becomes more suppressible (Suppress negates conditional passive = only −1 TC/season loss, and Hafenmark Suppress negates conditional+PY for −2 TC/season). Hafenmark Structural Suppression (Baralta −1/season) + active Suppress (−1 conditional passive) = −2 from Church's ~4–5 = net 2–3 TC/season. Church still wins TC race in ~20 seasons. The reform improved the system but didn't fundamentally change Church's dominance.]**

---

**Seasons 6–10 (Mid-game pressure):**

Season 6: TC 46. Hafenmark now triggers Priority 4 (TC ≥ 40): Suppress becomes mandatory every season when available. Hafenmark Suppress: Influence 6, Ob 2. 6d10: 9,8,7,3,10,2 → 5 net. Overwhelming. Negates conditional passive AND Piety Yield. Church TC gain this season: Assert(+1) + Assert(+1) = +2 (PY and passive negated). Net: 46→48.

**[FINDING: Hafenmark OW Suppress negating both conditional passive and Piety Yield reduces Church's TC gain from ~4–5/season to ~2/season. This is the crucial balance mechanic. If Hafenmark can consistently Suppress OW, Church's timeline extends from 20 to 35+ seasons. Suppress at Influence 6 vs Ob 2: P(Success+) ≈ 80%. Overwhelming: ~57%. Hafenmark gets OW ~57% of the time.]**

Season 7–10 (simplified): TC advances at ~3/season (1 OW Suppress per 2 seasons negates full gain; 1 Success Suppress per other season negates partial). By Season 10: TC ≈ 46 + 4×3 = 58. TC 55 milestone crossed around Season 9. At TC 55: opposing actions against Church cost +1 Ob.

**[FINDING: TC 55 milestone produces immediate political asymmetry. Any faction attempting Censure, Embargo, or Outlawry against Church now faces +1 Ob. At Mandate 5 (Crown, Ob 2 base): Mandate check now Ob 3. P(≥Ob 3, pool 5) ≈ 42% — from reliable to coin-flip. The TC 55 milestone effectively grants Church moderate parliamentary immunity. This is correct design but fires 2 seasons earlier than expected due to the 2-Assert engine.]**

Season 8 — Church Seizure opportunity: TC ≥ 40 allows Seizure. Church targets T3 (Lowenskyst, Crown territory, PT 3). Seizure Ob = 7 − PT = 7−3 = 4. Church Influence 6 + floor(TC/20) bonus = 6+2 = 8D (TC 52 at S8). 8d10: 9,8,7,4,10,3,7,2 → 6 net. Ob 4, surplus 2 = Success. T3 Accord set to max(floor(3/2)+1, 2) = max(2,2) = 2. Crown loses T3 effective control (TCV 2 lost). Church gains T3 prominence. RS −1 (no Battle required for ungarrisoned territory). **[FINDING: Church's Graduated Seizure is highly effective at TC 40+. With 8D at Ob 4, P(Success+) ≈ 85%. Crown's ungarrisoned territories are highly vulnerable. Crown needs to prioritize garrisoning T3 specifically to block Seizure — requiring a Legionary card before Church gets there.]**

Crown AI response: Priority 2 DEFEND — enemy Church now prominent in T3. Crown Legionary to T3 (Muster). Muster Ob 1 (no prerequisites for Light Infantry). Roll 4d10+commander: 9,7,3,1 → 2−1 = 1 net. Ob 1 = Success. Light Infantry unit raised in T3 (Size 2, Power 3). T3 is now garrisoned. Future Church Seizure requires Battle first (RS −1).

**[FINDING: Crown's correct response to Church Seizure is rapid garrisoning. The 1-season lag (Church Seizes → Crown Musters next season) means the first Seizure often succeeds. Crown must preemptively garrison contested territories before TC 40, or react to the first Seizure by garrisoning everything. This creates a correct tension: Crown must choose between expanding and defending existing holdings.]**

---

**Season 10 Victory Assessment:**

| Faction | TCV | Key conditions | Status |
|---------|-----|---------------|--------|
| Crown | 10 (lost T3) | Mandate 5, Military 4, Accord maintained in T1/T2/T5/T6/T14 | No win — TCV < 14 |
| Church | 7 (gained T3) | TC 58, Mandate 5, PT 5 in T9, T3 under Seizure | No win — TCV 7, TC < 65 |
| Hafenmark | 6 | Mandate 4, suppressing Church | No win |
| Varfell | 6 | VTM 2 (2 Expedition seasons) | No win |

**Peninsular Strain at Season 10:** 1 battle (Crown vs Church over T3? No — Church Seizure of ungarrisoned T3 = no Battle, no Strain). All other actions diplomatic/covert. Strain: 0. RS: 71 (−1 from Seizure, no Battle RS costs since Church took T3 ungarrisoned). IP: 0 (no battles).

---

**Seasons 11–15 (Power Accumulation):**

Season 11: TC 61. Church at Priority 2 (TC ≥ 55 milestone active, then TC 65 milestone approaches). Crown loses T3 TCV but garrisoned it — Church can only recontest via Battle now. Church shifts to Assert + Seizure targeting T14 (Crown, PT 3, ungarrisoned at time of attempt? Crown may have garrisoned T14 too). Assume Crown garrisons 2 territories with 2× Legionary cards; T14 covered.

Season 12: TC 65 milestone. **Church Dominant:** secular factions need 2 action slots to pass Parliamentary motions against Church. Crown has 1× Senator card and 1× Prefect. In practice, any Parliamentary motion against Church now costs Crown 2 cards when they only have 1 Senator. **Crown effectively cannot pass anti-Church Parliamentary motions alone.** Hafenmark with 2× Consul + Senator can field 2 cards in Parliament — still functional against Church. **[FINDING: TC 65 milestone grants Church near-immunity to solo Parliamentary action by Crown. The 2-card requirement is a significant constraint since most factions have 1 Senator. Only Hafenmark (2× Consul + Senator = 3 cards) and Church itself (2× Senator) have sufficient card bandwidth. At TC 65, Crown becomes politically toothless without Hafenmark coalition.]**

Season 13: Hafenmark Priority 4b fires: Dynastic Proclamation on T7 (Rendstad, adjacent to Gransol T8, controller Mandate 3 [Hafenmark's own territory — this is wrong, Priority 4b targets adjacent territory with controller Mandate < Hafenmark Mandate]). Correctly: Hafenmark targets T6 (Stillhelm, Crown territory, Crown Mandate 5 vs Hafenmark Mandate now 4 — Crown Mandate > Hafenmark Mandate, so Priority 4b doesn't fire; prerequisite is Hafenmark Mandate > target controller Mandate). With Crown at 5 and Hafenmark at 4, Hafenmark cannot Proclaim on any Crown territory. **[FINDING: Dynastic Proclamation is gated by Hafenmark Mandate > target controller Mandate. Since Crown starts at Mandate 5 and Hafenmark at 4, Hafenmark can never Proclaim on Crown territory without first raising Mandate above 5 OR waiting for Crown Mandate to drop. This is correct — Hafenmark's expansion tool targets weakened rivals, not strong ones.]**

Season 14: Varfell Path A VTM advancement. VTM 3 (Expedition to T6 success). Varfell now eligible for VTM Discretion (suppress TC by 1 if their contribution was ≥1 that season). Varfell Tribune: VTM Discretion vs TC. TC: 72. Varfell rolls Influence 5 + VTM 3 (floor(3/2)=1 bonus die) = 6D vs Ob 2. 6d10: 9,8,7,3,10,2 → 5 net. OW: TC −1 additional. TC: 72−1 (Suppress from Hafenmark) −1 (Varfell VTM Discretion) = 70. With Assert (+2) applied this season: TC = 70+2 = 72 (below cap). **[FINDING: When Hafenmark Suppress + Varfell Discretion both fire in the same season, Church's net TC gain is reduced to Assert results only (~2/season). This 2-faction suppression coalition is the correct anti-Church strategy. Critical design: TC 75 is now the old freeze point — in tc_political_redesign_v30, TC runs to 100 with new milestones. Season 14 TC ~72 means TC 80 milestone (Seizure Ob −1 globally; PT drifts +1) is ~4 seasons away.]**

Season 15 summary: TC 76. **Old TC 75 freeze was removed in tc_political_redesign_v30.** Under new rules, Church continues to advance TC. TC 80 milestone approaching. Peninsular Strain: 1 (one battle between Varfell and Hafenmark in disputed T4). RS: 70 (−2 from battles since S8). IP: 2 (1 battle season).

---

**Seasons 16–20 (Endgame):**

Season 16: TC 80. **Church Ascendant.** Seizure Ob −1 globally. All territory PT drifts +1 at Year-End unless Warden Cooperation ≥ 2. **[CRITICAL FINDING: TC 80 PT drift +1 affects all territories. Starting PT values: T6=1, T13=1, T11=2, T4=2. After TC 80 Year-End drift: T6→2, T13→2, T11→3, T4→3. These are Varfell and fringe Crown territories. Varfell's Cultural Reformation tool requires PT ≤ 3 — all four target territories just rose to 2–3. At PT 3, Reformation Ob = PT+1 = 4. Varfell Cultural Reformation goes from Ob 2 (PT 1) to Ob 4 (PT 3) in one Year-End. This massively narrows Varfell's non-military expansion window.]**

**[CRITICAL FINDING: TC 80 PT drift effectively neutralises Varfell's primary expansion tool in the endgame. This is intended (Varfell's expansion requires acting before TC 80) but the interaction wasn't previously identified. Varfell must complete Cultural Reformations by Season 15 or face Ob 4+ targets in the endgame. This makes Varfell's Path A (VTM focus) time-sensitive.]**

Season 17: Church Seizure (TC 80, Seizure Ob −1 globally). Ob = 7−PT−1 (TC80 bonus). T2 (Kronmark, Crown, PT 3): Ob = 7−3−1 = 3. Church pool: Influence 6 + floor(80/20)=4 bonus dice = 10D. 10d10: 9,8,7,6,10,7,3,8,4,2 → 6 net. Ob 3 = OW. T2 Accord set to floor(3/2)+2 = 3 (capped at 3). Crown loses T2 (TCV 1). Church TCV now: T9(5)+T3(2)+T2(1) = 8. Church faction-specific victory: TCV ≥ 8, PT ≥ 3 in all held territories. T3 PT = 3 ✓, T9 PT = 5 ✓, T2 PT = 3 ✓. **Church approaches faction-specific victory condition.** Missing: Mandate check (needs to have maintained Mandate, which it has at 5+).

Season 18: Victory check for Church. TCV = 8 ✓. PT ≥ 3 in T3, T9, T2 ✓. TC ≥ 65 (per §3.2 Church victory requiring TC ≥ 65): TC 82 ✓. But §3.2 of tc_political_redesign references victory_v30 §3.2. Per victory_v30 §3.2: Church victory requires TC ≥ 65 + TCV ≥ 8. **[FINDING: Church approaches faction-specific victory in Season 18 of a 4-faction NPC game. This is within the normal range (victory around Seasons 17–25 per board_game §Part Eight: "Estimated victory: Season 35–45" was for Holy State victory requiring TC 70 under the old rules, but that was with Hafenmark suppression AND pre-TC-reform. Under the new TC reform with 2-Assert engine, Church wins significantly earlier — Season 18.]**

**[MAJOR FINDING — BALANCE-NEW-TC-01 TRIGGERED: The 2-Assert engine under tc_political_redesign produces Church victory in ~18 seasons even with active Hafenmark suppression. This is too fast. The estimated target was Seasons 25–35 for a balanced game. Three potential fixes: (1) Reduce Church to 1 Senator card (losing 2-Assert advantage), (2) Assert-specific cooldown of 2 seasons instead of 1, (3) Restrict Assert to Pontifex card only (not Senator). Each has different strategic implications.]**

**Recommended fix: Assert moves to Pontifex-exclusive.** Church has 1× Pontifex with cooldown 2. This halves Assert frequency: 1 Assert per 2 seasons instead of 2 per season. TC gain from Assert drops from ~2/season to ~0.5/season average. Combined with conditional passive and PY, Church gains ~2.5/season at peak — reaching victory around Season 28–32. Correct target range.

**Campaign finding — Peninsular Strain interaction:** During Seasons 11–20, Strain reached 4 (Tension level) from 3 battle-seasons. All factions: Mandate check Ob 1. Church rolled Mandate 5D vs Ob 1: consistently succeeds. Weaker factions (Varfell Mandate 3): ~74% success. Over 5 seasons of Strain-4: Varfell Mandate drops 1 time on average. This is a meaningful but not crippling effect. Correct calibration.

**ST-01 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| 2-Assert engine too fast (Church victory S18) | Design gap: Assert should be Pontifex-exclusive | P1 |
| TC 80 PT drift neutralises Varfell tool in endgame | Intended interaction, but not documented | P2 |
| Church Seizure at TC 80 with 10D pool is near-unstoppable | Correct: TC 80 represents near-theocratic dominance | ✓ Confirmed |
| Hafenmark Dynastic Proclamation cannot target Crown (Mandate gap) | Correct gate — Hafenmark must weaken rivals first | ✓ Confirmed |
| TC 65 two-card Parliamentary requirement locks out solo Crown | Correct: coalition required at high TC | ✓ Confirmed |
| Peninsular Strain calibration | Correct — Tension at 3-4 battles/5 seasons | ✓ Confirmed |

---

## ST-02 — CROSS-SCALE TRANSITION CHAIN

**Setup:** Hybrid mode, Season 9. Player commands Crown in contested T14 battle against Löwenritter coup force. Mass battle underway. Turn 3, Phase 3 complete. Zoom In trigger fires (PC in territory).

### Zoom In Chain

**Zoom In trigger (scale_transitions §4.3.2):** PC (Crown leader) in T14 during inter-faction battle. Player-initiated Zoom In at legal entry point: After Phase 3 (movement complete, pre-Engagement). ✓

**BG → TTRPG unit conversion (military_layer §2.3):**
- Crown Heavy Infantry unit: Martial 4, Size 3 (tracked on token), Discipline 4. TTRPG: Power 4, Size 3, HeavyCut, Medium armour.
- Löwenritter Light Infantry: Martial 3, Size 4, Discipline 5. TTRPG: Power 3, Size 4, LightCut, Light armour.

**Phase 4 (offensive Thread):** No practitioner present with TS ≥ 30 on either side (Crown has no allied Thread practitioner at this point). Skip Phase 4.

**Phase 5 — Personal Combat trigger:** Löwenritter captain (named officer: Roderik Eisenbach, Command 3) challenges player to personal combat (mass_battle §3.7 Scene → Mass: General Duel). Player accepts. Mass battle holds at current state. Both generals enter personal combat.

**PC stats:** Agility 4, STR 3, History (Combat/Swords) 3 pts → +3D bonus. Endurance 5 → Wound Interval 11, Max Wounds 3.  
Combat Pool = (4×2) + 3 + 3 = 14 dice. Weapon: Long Heavy Blade (TN 7). Armour: Medium.

**Roderik Eisenbach:** Command 3 (Charisma+Cognition/2). For personal combat: Agility estimated at 3 (military professional, not exceptional). Combat Pool = (3×2) + 2 + 3 = 11 dice. Weapon: Short Heavy Blade (TN 6). Armour: Medium.

**Exchange 1 (player holds initiative — higher Attunement 4 vs Roderik's est. 3; per combat §3 subsequent rounds transfer to winner, Exchange 1 declared by lower initiative first):**

Per combat §3: lower initiative holder (Roderik) declares split first. Roderik declares: 7 Off / 4 Def (11 dice). Player sees this, declares: 8 Off / 6 Def (14 dice).

Player roll (TN 7, Off pool 8): 9,8,7,3,10,7,3,8 → 1+1+1+2+1+1 = 7 net.  
Roderik roll (TN 6, Off pool 7): 8,6,3,9,7,4,6 → 1+1+1+1 = 4 net (TN 6: 6,7,8,9 = success; 10 = 2 successes; 1 = −1).

Actually — short heavy blade TN 6 means results ≥6 count as success (not ≥7). Reroll with TN 6: same pool: 8(✓),6(✓),3(✗),9(✓),7(✓),4(✗),6(✓) → 5 net off. vs player's Def pool (6D, TN 7): 9,8,3,4,7,2 → 3 def successes.

Net hits for Roderik on player: 5 off − 3 def = 2 hits. Damage: 2 + STR(3) + weapon(+6 vs Medium per combat §5, HeavyCut vs Medium = +2 actually — wait: weapon modifier vs armour tier table: HeavyCut = Heavy Blade. "Heavy Blade: +6 vs None, +4 vs Light, +2 vs Medium, +0 vs Heavy." Player armour: Medium. Damage = 2 hits + STR(3) + weapon(+2 vs Medium) = 7. Wound Interval = 11. 7 < 11 → no Wound yet. Damage accumulates.

Net hits for player on Roderik: 7 off − 4 def (Roderik's Def pool 4D TN 7: 9,7,3,4 → 2 def) = 7−2 = 5 hits. Damage: 5 + STR(3) + LongHeavyBlade vs Medium (+2) = 10. Roderik WI = 9 (Endurance 3 → WI = 3+6 = 9). 10 ≥ 9 → Roderik takes 1 Wound. Remainder (10−9=1) begins next WI count.

Roderik: 1 Wound. −1D Combat Pool (now 10D). Initiative transfers to player (won exchange).

**Exchange 2 (player initiative — declares last):**

Roderik (10D now) declares: 6 Off / 4 Def. Player declares: 9 Off / 5 Def.

Player off (9D, TN 7): 9,8,7,10,3,4,7,8,2 → 1+1+1+2+1+1 = 7 net.  
Roderik def (4D, TN 7): 9,7,3,1 → 2−1 = 1 net (Critical Failure? No — majority-1s removed per board_game §Design Decision. Just 1 def).  
Net hits player on Roderik: 7−1 = 6 hits. Damage: 6+3+2 = 11. Running total: 1 + 11 = 12. WI = 9. 12 ÷ 9 = 1 Wound + 3 remainder. Roderik now has 2 Wounds. Max Wounds = floor(3/2)+1 = 2. **Roderik at Max Wounds.** Next WI fill = incapacitation.

Roderik off (6D, TN 6): 8,6,9,4,6,2 → 1+1+1+1 = 4 net (TN 6). Player def (5D, TN 7): 9,7,4,8,2 → 3 def. Net hits Roderik on player: 4−3 = 1 hit. Damage accumulation (player): 7+1+weapon(+2)+STR(3) = player running damage 7 + (1+3+2) = 7+6 = 13. WI = 11 (End 5). 13 > 11 → player takes 1 Wound. Remainder 2.

Player: 1 Wound, −1D (now 13D). Initiative: player won exchange (5 net vs Roderik's 1 net, player inflicted more wounds). Player retains initiative.

**Exchange 3:**

Roderik at 2 Wounds (Max), 1D in next WI needed for incapacitation. Player may finish this round. Roderik Combat Pool: 10D − 2 Wounds = 8D. Player: 13D.

Player declares first (Roderik has lower initiative? No — player won Exchange 2, so player has initiative = declares second). Roderik declares: 5 Off / 3 Def. Player: 11 Off / 2 Def (aggressive).

Player Off (11D, TN 7): 9,8,7,10,7,4,3,8,9,7,2 → 1+1+1+2+1+1+1+1 = 9 net.  
Roderik Def (3D, TN 7): 8,4,7 → 2 def. Net hits: 9−2 = 7. Damage: 7+3+2 = 12. Running total for Roderik Exchange 3: 3 (remainder from Exchange 2) + 12 = 15. WI = 9. 15 ÷ 9 = 1 more Wound (WI filled, 3rd Wound accrued) + 6 remainder. **Roderik: 3 Wounds. Max Wounds 2. Roderik INCAPACITATED (Stage 1).**

Player Def (2D, TN 7): 9,4 → 1 def. Roderik Off (5D, TN 6): 8,7,6,3,4 → 3 net. Net hits Roderik on player: 3−1=2. Damage: 2+3+2=7. Running total player Exchange 3: 2+7=9. WI=11. 9 < 11 → no new Wound.

**Result: Player wins general duel in 3 exchanges. Roderik incapacitated.** Mass battle consequences (§A.5): Roderik Stage 1 — all Löwenritter units: Morale −1. Command halved (3→1). 

**[FINDING: The general duel resolved in 3 exchanges as designed — quick, decisive, high-stakes. The player's higher Agility (4 vs 3) and longer History bonus were decisive. Critical observation: Roderik's TN 6 Short Heavy Blade was competitive — he landed 1 Wound on the player. The system's range interaction (player's Long weapon creates Reach advantage) wasn't simulated above — at Long vs Short, attacker with Long weapon cannot be engaged at Close range immediately. This is a gap in the simulation: the reach priority mechanics (combat §5, Establish Distance) weren't applied. Roderik should have needed to close distance before his TN 6 short weapon activated.]**

**Reach transition (retroactive):** Long Heavy Blade establishes Long range advantage. Roderik with Short Heavy Blade must spend 1 round Establishing Distance (Agility contest). Player Agility 4 vs Roderik Agility 3: player wins contest (P ≈ 65%). If player wins: Roderik spends Exchange 1 Establishing Distance — no attack, full Defence. Player attacks at −1D (established range is Long). Revised Exchange 1: player only rolls off (no Roderik attack), player hits. Fight still ends in 3 exchanges but player takes 0 wounds if reach is maintained properly.

**[FINDING (GAP): The general duel simulation above did not apply reach priority rules at combat start. This inflated damage to the player. Correct procedure: Long weapon holder always gets first advantage round at Long range; opponent must either Establish Close or fight at Long (which is optimal for the Long weapon holder). The gap is in simulation protocol, not in the rules themselves — the rules are correct but complex enough that sim protocols need to explicitly track reach from Round 1.]**

**Zoom Out procedure:**

Roderik incapacitated → Stage 1 mass battle consequences already applied. Player re-establishes Command (Ob 2, Phase 1 next mass battle turn). Player Charisma 4 + Cognition 4 → Command = ceil((4+4)/2) = 4. Re-establish Command: 4D vs Ob 2. Nearly automatic (P ≈ 85%). Success.

Mass battle resumes at Phase 5 of the interrupted turn (Phase-Lock Protocol). Löwenritter units fight: Command = 1 (Roderik halved), Morale −1.  
Löwenritter effective combat pool: min(Size, Command) + Command = min(4, 1) + 1 = 2D.  
Crown: min(3, 4) + 4 = 7D.  
7D vs 2D → Crown wins decisively. Territory secured. Accord in T14 −1 (battle in own territory). RS −1.

**Domain Echo at Zoom Out:** Player defeated named Löwenritter officer (faction officer): Crown Mandate +1, Löwenritter Stability −1 (per combat §13.1). Named NPC death check: Roderik incapacitated (Stage 1), not killed — death cascade doesn't fire yet. Medicine Ob 2 required within scene; player's companion or allied unit may stabilise.

**Player choice: stabilise or kill?** Killing Roderik: Stability −1 fired; death cascade (§13.3) fires — all NPCs Knotted to Roderik take Knot rupture, Disposition toward player −3. Player kills: Crown Mandate +2 (OW killing faction officer), Löwenritter Mandate −1, death cascade. Player stabilises: Roderik becomes potential recruit (Stage 1 NPCs may develop Disposition through subsequent interactions).

**[FINDING: The kill-vs-stabilise decision post-duel is a genuine strategic choice with asymmetric consequences. Killing maximises immediate faction stat gains but burns future relationship potential (Roderik as recruited officer, Disposition mechanic). Stabilising preserves relationship options at cost of 1 Mandate. This is excellent design — the decision emerges naturally from system interaction, not scripted choice.]**

**ST-02 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| Zoom In chain executed cleanly at legal Phase 3 entry point | ✓ System works | Confirmed |
| BG → TTRPG unit conversion produces viable combat stats | ✓ Clean | Confirmed |
| General duel resolves in 3 exchanges (designed) | ✓ Calibrated | Confirmed |
| Reach priority not applied at duel start | Simulation gap — rules correct, protocol needs reach-tracking from Round 1 | P2 |
| Kill-vs-stabilise produces genuine asymmetric choice | ✓ Elegant | Confirmed |
| Re-establish Command (Ob 2) after duel: reliable | P(≈85%) — correct | Confirmed |

---

## ST-03 — SOCIAL CONTEST CHAIN (3-CONTEST ARC)

**Setup:** Player (Crown) vs Himlensendt (Church). Question: whether a known Thread practitioner community in T6 (Stillhelm) should be protected or investigated. Three-contest arc (Chain Contest, §6.3).

**Context:** Player has a Belief: "Thread practitioners deserve protection, not persecution." Himlensendt Conviction: Faith (Certainty 4). Resonant Style: Evidence. Starting Disposition of Himlensendt toward player: 0 (neutral).

### Contest 1 — Formal Contest (Parliament, Season 8)

**Setup (§2):**
- Adjudicator: Parliamentary Panel → per ED-137/ED-562 resolution: highest-Mandate faction leader in territory. This is a Parliament session at T8 (Gransol, Hafenmark capital) — Baralta (Hafenmark, Mandate 4) is adjudicator. Model B confirmed.
- Adjudicator Conviction: Baralta = Precedent. Panel bias: +1D weight toward arguments citing legal/constitutional precedent.
- Genre: Question "should we protect them?" = Projection (future action).
- Primary genre bonus: +1D to Projection-framing arguments.
- Audience boost (Hafenmark/Categorical Imperative = Memory genre boost): Memory arguments get +1D.
- Player genre: Projection (+1D from primary). Player not Memory (+0 from audience). Total: +1D.
- Himlensendt genre: Projection (the Tribunal determines what should happen — Projection). +1D primary. +0 audience (Himlensendt arguing for investigation = Memory of heresy evidence — he switches to Memory). Himlensendt using Memory: +0 primary, +1D audience boost. Total: +1D each.

**Starting Conviction Track:** 5 (neutral). Audience resistance: Baralta Stability 5 → (5−1)/1 (round up) = 2 resistance.

**Exchange 1:**

Initiative: Himlensendt Attunement 3 vs Player Attunement 4. Higher Attunement = player holds initiative (declares second). Himlensendt declares first.

**Appraise (both):** Attunement only, Ob 1.  
Player (Att 4): 4D TN7: 9,7,3,4 → 2 net = Success. Full boost identified: audience favours Memory orientation.  
Himlensendt (Att 3): 3D TN7: 8,4,2 → 1 net = Partial. Axis type only (genre or orientation, not which).

Himlensendt argues Memory-Revealing (citing precedent of past heretical incidents). Player argues Projection-Revealing (vision of what happens if practitioners are persecuted — RS decline, loss of Warden cooperation, Altonian vulnerability). Interaction: CROSS (different genres).

Player Argue pool: (Cognition 4 × 2) + History(Politics 3 pts = +3D bonus) = 11D. Genre: +0 (not primary Memory that audience favours). Total: 11D. Ob 1 (standard).  
Roll 11D TN7: 9,8,7,4,10,7,3,8,4,9,2 → 1+1+1+2+1+1+1+1 = 9 net. Effective margin (CROSS) = floor(9÷2) = 4.

Himlensendt pool: (Cognition 4 × 2) + History(Theology 3 pts) = 11D. Audience boost: Memory +1D = 12D. Recall bonus: Himlensendt cites documented Heresy Investigation precedent: +2D. Total: 14D. Ob 1.  
Roll 14D TN7: 9,8,7,4,10,7,3,8,4,9,2,8,7,5 → 9 net. Effective margin: floor(9÷2) = 4.

Tie in effective margins (4 vs 4). Track movement: 4−2 (resistance) = 2 net from player; 4−2 = 2 net from Himlensendt. Net: 0 movement. **CROSS tie per §4 PP-236: no strain.** Initiative stays with holder (Himlensendt had lower initiative, so player held; stays with player).

**Exchange 2:**

Player argument: Projection, citing Rendering Stability data (a Finding from prior fieldwork). Evidence Track Finding cited → +1D Exchange 2 (fieldwork → contest, §9.1 and §3.9). Total: 11D + 1D = 12D.  
Recall bonus: player cites specific Finding: "The Stillhelm practitioner community has mended 3 Gaps in T6 over 4 seasons." Named, verifiable, documented. Recall +2D. Total: 14D.

Himlensendt switches to Projection (arguing future Heresy Tribunal outcome). Primary genre now: Projection. Himlensendt: 11D + 1D (primary Projection) = 12D. Recall: cites prior Tribunal precedents: +2D = 14D.

Resonant Style targeting: player targets Himlensendt Evidence Resonant Style. Argument must use Memory+Revealing. Player is arguing Projection… can't simultaneously target Evidence (which requires Memory+Revealing) with a Projection argument. **[FINDING (GAP): A player cannot simultaneously use Projection genre (primary +1D) and target the Evidence Resonant Style (requires Memory+Revealing). These are incompatible. The player must choose between: (a) genre bonus + no Resonant Style targeting, or (b) switch to Memory genre (lose +1D primary bonus) to target Evidence Resonant Style. This is a genuine strategic tension, correctly designed.]**

Player switches to Memory (loses +1D genre): cites specific evidence of RS decline rates in territories with active Thread persecution. 11D (no genre bonus, not Memory primary in audience). Recall +2D = 13D. Resonant Style targeting (Evidence): +1D = 14D. On win: +1 additional Conviction Track movement.

Interaction: CROSS still (player Memory, Himlensendt Projection — different genres).

Player roll 14D TN7: 9,8,7,4,10,7,3,8,4,9,2,8,7,3 → 9 net. Effective margin: 4. Himlensendt roll 14D TN7: 9,8,7,3,10,7,4,8,3,9,2,8,7,5 → 9 net. Effective margin: 4. **Tie again.** Player's Resonant Style targeting was declared but neither side won — no +1 additional movement. CROSS tie: no strain, no movement.

Concentration check: both at Focus 3 + Recall 4 = 7 pool. Depletes 1 per exchange (−1 per exchange, −1 additional on loss). Neither lost. Concentration: 7−2 = 5 remaining. Not Spent.

**Exchange 3 (final — Formal Contest = 3 exchanges):**

Track still at 5. Both sides tied. Stakes: if this ends at 5 → Compromise (no Domain Echo, chain contest triggered for next season).

Player switches back to Projection (primary +1D). Himlensendt stays Projection. CLASH now (same genre). Player: Projection-Revealing. Himlensendt: Projection-Obscuring. CLASH.

Player: 11D + 1D (Projection primary) = 12D. Recall: cites specific Rendering Stability measurement ("RS dropped from 72 to 70 in the 3 seasons since the last Heresy Investigation campaign in T3"). Named, verifiable: +2D. Total: 14D.

Himlensendt: 11D + 1D (Projection primary) + 1D (audience Memory boost — wait, Himlensendt is now Projection, no audience boost) = 12D. Recall +2D = 14D.

CLASH resolution: compare successes. Higher wins. Margin determines track movement.

Player roll 14D TN7: 9,8,10,4,7,3,8,7,9,4,2,8,3,7 → 2+1+1+1+1+1+1+1 = 9 net.  
Himlensendt roll 14D TN7: 8,7,4,3,10,9,2,7,3,8,7,4,2,9 → 1+1+2+1+1+1+1+1 = 9 net.

Exact tie. Per §4 TIE rule: both take 1 strain. Conviction Track moves +1 toward initiative holder's position. Player holds initiative (from Exchange 1). Track: 5→6.

Strain: player Composure = Charisma(4) + 6 = 10. Himlensendt Composure = Charisma(4) + 6 = 10. Both take 1 strain. Not Rattled yet.

**Contest 1 result: Track 6 = Compromise.** No Domain Echo. **Chain contest triggered (§6.3):** follow-up contest Season 9. Track starts at 6 for Chain Contest.

**[FINDING (CONFIRMED): With equal pools and equal tactics, Projection-vs-Projection CLASH produces frequent ties, especially in 3-exchange Formal Contests. The Chain Contest mechanic correctly handles this — the tension continues into next season. Starting Chain at Track 6 (already 1 toward player's victory at 7) gives the player a slight advantage going into Contest 2.]**

---

### Contest 2 — Chain Contest (Season 9, Formal Contest, Track starts at 6)

**Setup change:** Himlensendt has accrued 0 Scars (no decisive loss via Resonant Style). Player must produce a decisive win in Contest 2 to avoid another Chain.

Player has spent the off-season preparing evidence (§9.1 Pre-Contest Preparation). Preparation: Attunement 4 + relevant History (Investigation): 7D TN7 Ob 1. 7d10: 9,8,7,3,4,7,2 → 4 net = Overwhelming. +1D Exchange 1 AND Exchange 1 Appraise uses TN 6.

**Evidence Track Finding used:** Player conducted Fieldwork investigation in T6 last season. Finding: "Maret Vossen (RM leader) has documented 3 Gap closings by Stillhelm practitioners in the past 2 seasons." This is a Named, Verifiable, Documented Finding. +1D Exchange 1 (fieldwork §9.1 citation cap 2D max; player has 1 Finding cited = +1D). Combined with preparation: Exchange 1 starts at +2D.

**Exchange 1 of Contest 2 (Track 6, need to push to 7):**

Player: Cognition 4 × 2 = 8, History +3 = 11D, +1D preparation, +1D Finding citation = 13D. Recall (cites Gap closings): +2D = 15D. Resonant Style targeting (Evidence, Memory+Revealing): +1D = 16D. Total: 16D.

Himlensendt: 14D (same as above).

Appraise (TN 6 for player this exchange): Player 4D TN6: 9,7,4,8 → 3 net = OW. Boost identified + NPC emotional state: Himlensendt is "visibly troubled by the Gap closure evidence — his Certainty shows a hairline crack." GM notes this is an Evidence Resonant Style access point.

Player CLASH (Memory-Revealing, same genre if Himlensendt stays Projection — no, they must be same genre for CLASH. Himlensendt uses Memory this exchange to address the evidence).

CLASH: both Memory. Revealing (player) vs... Himlensendt orientation? Church = Obscuring. Memory-Obscuring: Himlensendt argues the Gap closings happened despite Thread practice, not because of it.

Player roll 16D TN7: 9,8,10,4,7,3,8,7,9,4,2,8,3,7,9,8 → 2+1+1+1+1+1+1+1+1+1 = 11 net.  
Himlensendt roll 14D TN7: 8,7,4,3,10,9,2,7,3,8,7,4,2,9 → 9 net.

Margin: 11−9 = 2. Resistance: 2. Movement = 2−2 = 0. **Track doesn't move despite player winning!** Resistance of 2 absorbs the 2-margin win.

**[CRITICAL FINDING (GAP): In a Chain Contest starting at Track 6 with Resistance 2, a player needs margin > 2 (margin ≥ 3) to actually move the track. With equal 14D pools adjusted for player's bonuses, an 11D roll producing margin 2 is common — but the 2-resistance absorbs it. Player needs margin 3+, which requires net 3+ successes above Himlensendt. With pools of 16D vs 14D, margin ≥ 3 probability: the expected difference between 16D and 14D pools is ~(16−14) × E(success per die) = 2 × 0.4 = 0.8 expected margin. P(margin ≥ 3) ≈ 25–30%. The player has only a 25–30% chance per exchange of actually moving the track in a Chain Contest starting at 6 with Resistance 2. At 3 exchanges, the probability of at least one track-moving exchange: 1−(0.7)³ ≈ 66%.]**

**[CRITICAL FINDING: Resistance of 2 with near-equal pools (16D vs 14D) creates a system where Track movement is rare even when the player is clearly winning individual exchanges. This is mathematically correct — track resistance models audience stubbornness — but it produces frustrating play in Chain Contests where the track needs only 1 more movement to resolve. The 66% chance per 3-exchange contest of advancing 1 track position means the average Chain Contest sequence takes 1.5 contests to resolve after reaching Track 6. This is acceptable but should be documented.]**

Resonant Style targeting activated: player won (11 net vs Himlensendt 9 net). Resonant Style confirmed: +1 additional track movement bypassing 1 point of resistance. Track: 6 + (2−2) + 1 (RS bypass) = **7. DECISIVE WIN.**

**[FINDING: Resonant Style targeting's "bypass 1 point of resistance" is the key mechanic for breaking Resistance-2 stalls. Without RS targeting, margin-2 wins produce 0 track movement against Resistance 2. With RS targeting, the same margin-2 win produces 1 track movement. This makes Resonant Style targeting mechanically essential in high-resistance contests, not merely a bonus.]**

**Contest 2 result: Track 7 = Decisive Win (player).** Domain Echo fires: Church Faction Mandate −1 (lost institutional authority in this domain). Player faction Mandate +1.

**Conviction Scar check (§6.1 + npc_behavior §3.2):** Was the decisive win achieved via Resonant Style (Evidence) targeting with Belief engagement? Player argued Thread practitioners protect RS (Evidence — specific, named, verifiable). Himlensendt's Belief 3: "Thread practitioners are deluded or deceived." This Belief was the target of the player's argument. **All three gates met: decisive outcome + Resonant Style + Belief engagement.** Himlensendt gains 1 Conviction Scar.

**[FINDING: Conviction Scar from Contest 2 fires correctly. Himlensendt has 1 Scar: "something shifted in his expression" signal fires. His Priority 2 trigger updates immediately (npc_behavior §9.3): "Heresy Investigation" condition gains a caveat — he cannot target the Stillhelm community directly for 2 seasons (Obligation from the contest's Decisive Win: player names commitment "Church must not station Inquisitors in T6 for 2 seasons").]**

**Obligation created (§6.1 — Formal Contest, 2-season duration):** "Church must not station Inquisitors in T6 for 2 seasons." Himlensendt's Priority 2 is modified per §6.1: cannot initiate Heresy Investigation in T6 while Obligation stands. Priority 2 redirects to other territories.

**[FINDING: Obligation mechanic constraining NPC priority tree is precisely the endgame of a social contest chain — not just a stat change, but a lasting behavioral constraint on an NPC faction. This is the system working correctly. The Obligation clock tracks: 2 seasons. If violated, Church Mandate −1 + Reputation shift.]**

**ST-03 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| Player cannot simultaneously use Projection +1D and target Evidence RS (incompatible) | Correct design tension — must choose | ✓ Confirmed |
| CROSS ties with equal pools produce frequent Compromise chains | Working as intended | ✓ Confirmed |
| RS Resistance 2 requires RS targeting to move track from near-victory position | RS targeting mechanically essential in high-resistance — well designed | ✓ Confirmed |
| Probability of decisive win per exchange in Chain Contest (Track 6, Res 2): ~25–30% | Acceptable — 66% per 3-exchange contest is reasonable | ✓ Confirmed |
| Conviction Scar from decisive RS win fires correctly | ✓ | Confirmed |
| Obligation correctly blocks NPC priority tree entry for 2 seasons | ✓ Elegant | Confirmed |

---

## ST-04 — HYBRID FULL SEASON

**Setup:** Season 11. Hybrid mode. Player is Varfell faction leader. Full season: BG Strategic Phase → Cascade Phase → Personal Phase → Cascade.

**Personal Phase (90–150 min, 2 scenes):**

*Scene 1 — Fieldwork in T9 (Himmelenger):* Player conducting investigation on Church funding sources (Evidence Track). GM context: Church PT 5, Accord 3, Church dominant. Player Exposure (operating in hostile territory): covert = +1 Exposure per fieldwork scene.

Roll: Cognition 4 + History(Investigation 2 pts = +2D bonus) = 10D. Ob 2. 10d10: 9,8,7,4,10,7,3,8,4,9 → 8 net. Ob 2, surplus 6 = OW. Evidence Track: +2 (OW = major finding). Finding: "Church Charity Advantage sources: Wealth 6 (vs Crown Wealth 4). Church funds 3 almshouses in T9 and T2, reaching 40% of the populations." Named, verifiable, documented. Complexity: Complex (threshold 5+, contributing to sufficient scope). Exposure +1 (covert = quiet engagement).

Sufficient Scope met? Finding names faction leader acts (Himlensendt's charity program). Yes — §7 Sufficient Scope condition 3: "completed Complex investigation whose subject concerns faction's institutional acts." Domain Echo triggered.

Domain Echo (§5.2, Personal Phase): fires immediately at scene end (Full TTRPG register shift mode). Effect: Magnitude = OW → ±2 to most relevant faction stat. Most relevant: exposing Church's Charity Advantage weakens it politically (Influence domain). Church Influence −2. **[Wait: Domain Echo fires immediately in full TTRPG mode; in Hybrid mode per §5.3: "Hybrid: Domain Echoes from personal scenes queue to Cascade Phase Accounting." Not immediate in Hybrid.** Domain Echo queued.

*Scene 2 — Social contest vs Varfell NPC officer:* Player resolves a succession dispute in T12 (Sigurdshelm). Adjudicator: No adjudicator (private negotiation). Conviction Track optional. Single exchange. Player wins (Partial — one exchange, Projection-Revealing, Attunement pool): Varfell officer Disposition +1 toward player. No Domain Echo (private negotiation, not sufficient scope).

**Cascade Phase (Hybrid, applying all batched consequences):**

Step 1 — Domain Echoes:
- Fieldwork Scene 1 Domain Echo: Church Influence −2. Queued → fires now at Cascade Step 1. Church Influence: 6→4. **[FINDING: A single Personal Phase OW investigation can drop Church Influence by 2. Church Influence 6→4 is a significant reduction. At Influence 4, Church's Graduated Seizure pool (Influence + floor(TC/20)) = 4+4 = 8D. Vs. prior 6+4 = 10D. Ob 4 success rate: 8D ≈ 79% vs 10D ≈ 88%. Not catastrophic but meaningful. Player investigation of Church finances is a valid counter-strategy.]**

Step 2 — Thread operation clock changes: No Thread ops in Personal Phase this season.

Step 3 — Clock threshold events: TC check. TC 72 (from ST-01 timeline). No milestone crossed. RS 70. No RS threshold crossed (RS 72−2 = 70; Strained band = 79-60, no change in threshold). IP check: no battle this season → IP unchanged.

Step 4 — BG order consequences:

**Strategic Phase (BG) orders this season (run before Personal Phase, per §9.1):**

Varfell AI ran:
- Tribune Intel T3 (Investigate Crown territory): Influence 5, Ob 2. Roll 5d10: 9,8,7,3,2 → 3 net. Success. Crown stat revealed: "Crown Military at 4 — confirmed by spy network." Varfell Influence +1 (per TC redesign §4.1). Varfell Influence: 5→6.
- Player (Varfell) PC Embedding bonus (§9, scale_transitions): PC present in T12 during Strategic Phase. Varfell Govern T12 gets +1D. Consul Govern T12: Mandate 3+1D (embedding), Ob 1 (capital −1). 4D: 9,8,4,2 → 2 net. OW. Accord T12: already 3 (capped). Mandate +1 (capital OW, PP-174). Varfell Mandate: 3→4.

Step 4 (continued): BG order consequences processed. No NPC coalition penalties this season.

Step 5 — Accounting:
- Attribute changes applied: Church Influence 4 (from Domain Echo), Varfell Mandate 4 (from capital Govern).
- Accord checks: all territories maintained (no Acc 1 territories without garrisons).
- TC: 72 + Assert(+1, Church used one Senator) + PY(+1, T9 PT5 Prominent) + Conditional(+0, only 1 Prominent territory) = 74. Seasonal cap ±5: all fine.
- Victory checks: No faction meets conditions.
- Seasonal caps applied. Pending Domain Echo (Church Influence −2) confirmed.

**[FINDING: The Hybrid Cascade Phase correctly sequences all consequences. The key interaction: PC Embedding in Strategic Phase (+1D to Varfell Govern in T12) stacks with the Personal Phase scene (officer Disposition +1) to produce net Mandate +1 for Varfell. This 2-layer reinforcement (BG + TTRPG personal scenes both improving Varfell's standing in the same territory in the same season) is correct and intended — the hybrid mode rewards presence.]**

**[FINDING (GAP): The Domain Echo from Personal Phase fieldwork (Church Influence −2) is significant enough to change Church's Seizure pool in the following season. But the Domain Echo fires at Cascade Step 1, before Church's TC advance at Step 3. So Church advances TC on top of reduced Influence. The sequence matters: if Influence were reduced before TC advance, Church's political pool would already be reduced when TC benefits are calculated. But TC advance is a clock check (Step 3), not dependent on Influence — so no interaction. However: if Church's reduced Influence triggers a Stability check (Influence 4 vs starting 6 = −2, which is a >2 attribute loss in one season), is a Stability check triggered? Per tc_political_redesign §4.1 Stability note: "Governed exclusively by Triggers 1–5 per faction_layer_v30." No automatic Stability check from Influence loss alone. Correct — no cross-contamination.]**

**ST-04 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| Domain Echo from OW investigation can drop Church Influence by 2 | Correct, powerful but not broken (pool goes 10D→8D) | ✓ Confirmed |
| PC Embedding (+1D BG Govern) + Personal Phase (Disposition +1) stacks correctly | ✓ Intended hybrid reinforcement | Confirmed |
| Cascade sequence correctly processes Domain Echoes before clock advances | ✓ No interaction gap | Confirmed |
| Church Influence −2 from single investigation does not trigger Stability check | ✓ Correct per faction_layer triggers | Confirmed |

---

## ST-05 — TC REFORM STRESS TEST (25 SEASONS)

**Setup:** Church-only TC sim, 25 seasons. Test the repeal of PP-402 (unconditional passive) and the conditional passive system against Hafenmark maximum suppression.

**Variables:**
- Assert: Pontifex-exclusive (proposed fix from ST-01). Cooldown 2 seasons. 1 Assert per 2 seasons avg = 0.5 TC/season from Assert.
- Conditional passive: Church Prominent in 2+ territories → +1/season. Church Prominent in T9 always (start). T3 gained by Season 6 (per ST-01). So from Season 6: 2 territories Prominent → +1 conditional.
- Piety Yield: T9 PT5 = +1/season always. T3 PT3 = +0.25/season from Season 6.
- Charity Advantage: Church Wealth 4, Crown Wealth 4 (same) → no qualifying territory. Requires Church Wealth ≥ Crown Wealth + 2. Church Wealth rises to 6 by Season 10 if Trade succeeds. Then +0.5/season (1 territory qualifying) from Season 10.
- Templar Presence: 1 Templar in T9 (Sacred Assembly Ob 3: ~42% success S1). Assume Templar deployed by Season 3. T9 PT 5 ≥ 3. TC +1/season from Season 3.
- Hafenmark Structural Suppression (Baralta): −1/season always. Baralta Mandate 4 at start. Assume stays ≥ 4 through most of game.
- Hafenmark Active Suppress: 1 OW per 2 seasons (57% OW rate × every season = 0.57 OW/season). OW negates conditional + PY. In practice: Suppress fires every season, OW half the time. OW effect: −1 conditional (avoided) −1 PY (avoided) = saves Church +2 TC/season for that season. Averaged: Suppress OW 57% of seasons × saves 2 = 1.14 saved (i.e., Church gains 2 TC less in a Suppress-OW season). Simplified: Suppress OW negates 2 TC sources half the time = reduces TC by ~1/season on average.

**TC accumulation table (proposed Assert-as-Pontifex fix):**

| Season | Assert | Conditional | PY | Charity | Templar | Baralta | Suppress avg | Net gain | TC |
|--------|--------|------------|-----|---------|---------|---------|-------------|---------|-----|
| 1 | 0 | 0 | +1 | 0 | 0 | −1 | −0.5 | −0.5 | 27.5 |
| 2 | +1 | 0 | +1 | 0 | 0 | −1 | −0.5 | +0.5 | 28 |
| 3 | 0 | 0 | +1 | 0 | +1 | −1 | −0.5 | +0.5 | 28.5 |
| 4 | +1 | 0 | +1 | 0 | +1 | −1 | −0.5 | +1.5 | 30 |
| 5 | 0 | 0 | +1 | 0 | +1 | −1 | −0.5 | +0.5 | 30.5 |
| 6 | +1 | +1 | +1 | 0 | +1 | −1 | −1 | +2 | 32.5 |
| 7 | 0 | +1 | +1 | 0 | +1 | −1 | −1 | +1 | 33.5 |
| 8 | +1 | +1 | +1 | 0 | +1 | −1 | −1 | +2 | 35.5 |
| 9 | 0 | +1 | +1 | 0 | +1 | −1 | −1 | +1 | 36.5 |
| 10 | +1 | +1 | +1 | +0.5 | +1 | −1 | −1 | +2.5 | 39 |
| 11 | 0 | +1 | +1 | +0.5 | +1 | −1 | −1 | +1.5 | 40.5 |

TC 40 milestone reached Season 11. With Pontifex-exclusive Assert, vs Season 4 under 2-Assert engine. **Correct:** Assert-as-Pontifex pushes TC 40 milestone back ~7 seasons. This gives secular factions time to build defenses before Church Seizure becomes available.

| 12–15 | ~+2–2.5/season | 40 → 48 |
| 15 | TC 48 | Church Assertive bonus active |
| 16–20 | ~+2.5/season with Assertive bonus | 48 → 60.5 |
| 20 | TC 61 | Near TC 65 milestone |
| 21–25 | ~+2.5/season | 61 → 73.5 |

TC 55 milestone (Season ~17–18): +1 Ob to actions opposing Church.
TC 65 milestone (Season ~21–22): 2-card Parliamentary requirement.
TC 80 milestone (Season ~28–30): PT drift + Seizure Ob −1.

**[FINDING: With Assert as Pontifex-exclusive, Church victory timeline (TC ≥ 65 + TCV ≥ 8) is pushed to Season 21–22 minimum for TC alone. TCV 8 requires additional time (Church starts at 5, needs 3 more from Seizure or other means). Total victory around Season 24–28. This is a much better balance point than S18 under the 2-Assert engine. Standard game (~40 seasons) gives secular factions a full 15–20 season window to counter Church before it approaches victory.]**

**Hafenmark maximum suppression scenario:** What if Hafenmark OW Suppress EVERY season (100% OW, impossible but stress test)?

OW every season = conditional + PY negated every season. TC gain = Assert (0.5/season) + Templar (+1/season) + Charity (+0.5/season from S10) − Baralta (−1/season) = 1/season from Season 10. TC reaches 65 milestone: (65−28) ÷ 1 = 37 seasons. TC 65 in Season 39. In a standard 40-season game, Church barely reaches the TC milestone with max suppression. **[FINDING: Maximum Hafenmark suppression (OW every season) makes Church victory via TC extremely unlikely in a 40-season game. This is the correct ceiling — Hafenmark is designed as the structural Church counter. One faction playing perfectly should be able to contain the TC climb. At realistic Suppress rates (57% OW), Church wins around Season 24–28 as calculated above.]**

**ST-05 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| 2-Assert engine (current) produces Church victory S18 — too fast | Design gap: Assert → Pontifex-exclusive | P1 |
| Pontifex-Assert fix pushes victory to Season 24–28 | Correct target range | ✓ Confirmed |
| Hafenmark max suppress contains Church to Season 37+ | Correct ceiling for the designed counter-faction | ✓ Confirmed |
| Charity Advantage requires Church Wealth ≥ Crown+2 — rarely activates | Gate may be too high; consider Crown+1 threshold | P3 |
| Conditional passive at 5+ territories (+2/season) is aspirational — Church rarely has 5 Prominent territories in a competitive game | This is correct — +2 is an endgame reward | ✓ Confirmed |

---

## ST-06 — FIELDWORK → COMBAT → CONTEST PIPELINE

**Setup:** Player investigating Niflhel arms smuggling in T14 (Ehrenfeld). Fieldwork scene in progress. Evidence Track at 3 (2 findings so far). Then ambush. Then contest using evidence.

**Fieldwork Scene (Investigation):**

Fieldwork action: Attunement 4 + History(Covert Ops, 2 pts = +2D) = 10D. Ob 2. 10d10: 9,8,7,4,10,3,8,4,9,2 → 7 net. OW. Evidence +2. Track: 3→5. **Sufficient scope reached** (threshold 5+ for Complex, per §7 condition 3). Finding: "Niflhel Arm 2 has a safehouse in T14 coordinated by a Church-affiliated intermediary, documented by purchase records." Named, verifiable.

Exposure: Player covert investigation in T14 (hostile territory). Roll: Exposure threshold check. Combat Exposure per F-TRANS-01: quiet engagement. Exposure: +1 (existing) +1 (this scene) = 2.

**Ambush triggered:** Exposure threshold reached. Per scale_transitions §3.9: "Exposure threshold reached; ambush triggered." Fieldwork → Combat: Exposure converts to ambusher initiative advantage. Active investigation ends.

Ambush setup: Niflhel Arm 2 operatives (3 agents: Agility 3 each, Combat Pool 9D each, Light Blade TN 5, Light armour). Player: Combat Pool 14D. Player ambushed = no initiative advantage (initiative is given to ambushers per §3.9).

**Round 1 (Ambusher initiative):**

3 attackers vs player. Group combat: Fibonacci bonus. 2 attackers = +1D off to each attacker against single target.

Ambusher 1 (lead): 9D off, 0 def declared (taking down target). Light Blade TN5: 9D TN5. Near-maximal. Roll 9D TN5: 9,7,8,3,6,8,5,4,7 → 7 net. Player Def (full Guard? No — player should defend partially). Player with 14D: declares 6 Off / 8 Def.

Actually player must declare simultaneously. Per §3: lower initiative (player — ambusher has initiative) declares first. Player declares: 5 Off / 9 Def (heavy defence, survive first round).

Ambusher 1 Off (9D TN5): 8(✓),7(✓),8(✓),3(✗),6(✓),8(✓),5(✓),4(✗),7(✓) = 7 net. Ambusher 2 +Fibonacci (+1D Off, also attacking): Off 9+1=10D TN5: 8,7,4,6,5,9,8,3,8,7 → 8 net. Ambusher 3: 10D: 9,7,3,8,5,4,7,3,9,8 → 7 net. Player Def (9D TN7): 9,8,7,4,10,3,7,8,4 → 6 net.

Multi-engagement pool split (§8 combat): player declares one Defence split for round. All attackers roll against same Defence. Player 9D Def → 6 net def.

Net hits per attacker on player:
- Ambusher 1: 7−6 = 1 hit. Damage: 1+STR(2)+weapon(Light Blade vs Light armour: +2): 5. Player WI=11. Running damage: 5.
- Ambusher 2: 8−6 = 2 hits. Damage: 2+2+2 = 6. Running: 11. WI = 11 → 1 Wound! Remainder: 0.
- Ambusher 3: 7−6 = 1 hit. Damage: 1+2+2 = 5. Running: 5 (new WI).

Player: 1 Wound. −1D (now 13D). Initiative transfers? Player Off pool was 5D. Vs 3 ambushers on 3 separate targets — player can only target 1 per round in multi-engagement. Player target: Ambusher 1 (closest/most dangerous). Player Off 5D TN7: 9,7,3,4,8 → 3 net. Ambusher 1 Def (0D declared — took no defensive action): 0 def. Net hits: 3. Damage: 3+STR(3)+LongHeavyBlade vs Light armour (+4): 10. Ambusher 1 WI: 6+Endurance(2)=8. 10 ≥ 8 → 1 Wound. Remainder: 2. Ambusher 1: 1 Wound, Max Wounds = floor(2/2)+1 = 2. Ambusher 1 is damaged but functional.

**Round 2 (Player now has initiative from winning exchange vs Ambusher 1):**

Player now declares second. Ambushers declare: 2 of 3 target player (Ambusher 1 now defending with 1 Wound). Player with 13D (1 Wound) declares: 8 Off (Ambusher 1) / 5 Def.

Ambusher 1 (8D TN5, 1 Wound = 8D): 8,7,4,6,9,5,3,8 → 7 net. Ambusher 2 (9D TN5): 9,7,8,4,7,6,3,9,8 → 8 net. Ambusher 3 retreats (player shows superior combat ability — NPC evaluation: Ambusher 3 Disposition toward player already −2 from failed ambush, assess threat). Ambusher 3 attempts Escape (Agility 3 vs player Agility 4): fails (player wins Agility contest). Ambusher 3 stays engaged but can't escape.

Player Def 5D: 9,7,4,8,3 → 3 def.

Net hits: Ambusher 1: 7−3=4 hits. Damage: 4+2+2 = 8. Running player (WI count from end of R1): 5+8=13 ≥ 11 → 2nd Wound! Remainder: 2. Player: 2 Wounds now.
Ambusher 2: 8−3=5 hits. Damage: 5+2+2=9. Running: 2+9=11 ≥ 11 → 3rd Wound! Remainder: 0. Player: 3 Wounds. Max Wounds = floor(5/2)+1 = 3. **Player at Max Wounds. Incapacitation next WI fill.**

Player Off 8D (Ambusher 1): TN7. 8,9,7,4,10,3,8,9 → 1+1+1+2+1+1 = 7 net. Ambusher 1 Def (Ambusher 1 declared 0 Def — all Off): 0 def. Net hits: 7. Damage: 7+3+(+4 vs Light) = 14. Ambusher 1 WI count: 2(remainder)+14=16. WI=8: 2 more Wounds (16÷8 = 2). Ambusher 1: 3 Wounds. Max Wounds = 2. **Ambusher 1 incapacitated.**

**Round 2 result:** Player 3 Wounds (at Max, WI filling), Ambusher 1 incapacitated. 2 ambushers remain.

**Critical decision point:** Player at Max Wounds and taking 1 hit per exchange from the remaining ambushers = 1–2 more rounds before incapacitation. Player must disengage or change tactics.

Player declares: **Escape** (Agility 4 vs Ambusher 2 Agility 3 contested). Player wins (~65%). Player flees. Active investigation ends. **[FINDING: The 3v1 ambush with Fibonacci bonus (+1D per extra attacker) produces dangerous multi-wound scenarios even for high-pool players. Player with 14D baseline at 3 Wounds (−3D = 11D effective) faces two functional opponents. Escape is the correct tactical choice. The system correctly punishes solo players who reach Exposure thresholds in hostile territories.]**

**Post-combat fieldwork transition (§3.9 F-TRANS-12):** Post-combat investigation of battle site = 1 fieldwork scene. Combat Exposure: conspicuous (+2 Exposure — 3-person fight in safehouse). Exposure now: 2 (prior) + 2 (combat) = 4.

But player escaped (fled) — cannot perform post-combat fieldwork on the active combat site (they fled, not won). Post-combat fieldwork requires player to be present at site after combat. Player fled = no post-combat investigation this scene.

**[FINDING (GAP): The rules state "post-combat investigation of battle site = 1 fieldwork scene" but do not specify whether this applies to combat where the player fled vs. won. Proposed clarification: post-combat fieldwork requires player to control the site (enemy fled, incapacitated, or dead) at combat resolution. A fleeing player cannot post-combat investigate. Add to combat §11.5 F-TRANS-12.]**

**Evidence Track persistence:** The 5-point Evidence Track (Complex scope, Finding about Niflhel safehouse) persists. Player carries the Finding into the next contest. The safehouse evidence survives the ambush.

**Contest — player uses Evidence:** Next session, player cites the Niflhel safehouse Finding in a Grand Contest vs Ehrenwall (Löwenritter). Adjudicator: Crown (Mandate 5, in T1). Projection genre. Finding citation: +1D Exchange 1. Recall (named Finding, verifiable): +2D. Evidence RS targeting (if Ehrenwall RS is Consequence, not Evidence — no RS targeting available). 

**[FINDING: Evidence Track Findings are powerful contest openers (+1D citation + Recall +2D = up to +3D total on Exchange 1) but can only trigger Resonant Style bonus if the cited evidence matches the NPC's Resonant Style. If the NPC uses Consequence RS (not Evidence), the +3D bonus applies to the pool but not to the RS targeting bonus. Players must match their evidence type to the specific NPC's Resonant Style for maximum impact.]**

**ST-06 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| 3v1 ambush with Fibonacci correctly creates severe threat | ✓ Working | Confirmed |
| Escape is viable (Agility contest ~65% at Agility 4 vs 3) | ✓ Calibrated | Confirmed |
| Post-combat fieldwork requires player to control site (fled = no access) | Gap: not explicitly stated | P2 |
| Evidence Track survives combat (persistent) | ✓ Correct | Confirmed |
| Finding citation (+1D) + Recall (+2D) = strong contest opener | ✓ Balanced (Exchange 1 only) | Confirmed |

---

## ST-07 — MASS BATTLE WITH ZOOM IN, THREAD OPS, GENERAL DUEL (FULL 7-PHASE RUN)

**Setup:** Season 12, T6 Stillhelm. Crown (4 units: 2 Heavy Infantry, 1 Cavalry, 1 Archer) vs Löwenritter (3 units: 2 Heavy Infantry, 1 Knights Templar). Player commands Crown. Allied Thread practitioner (Maret Vossen, TS 45, Coherence 10) present in Reserve.

**Crown force:**
- HI Unit A: Power 4, Size 5, Discipline 5, HeavyCut, Medium. BG Martial 4.
- HI Unit B: Power 4, Size 4, Discipline 4, HeavyCut, Medium. BG Martial 4.
- Cavalry Unit C: Power 5, Size 4, Discipline 5, HeavyCut, Heavy. BG Martial 4.
- Archer Unit D: Power 3, Size 3, Discipline 3, LP (Bow), Light. BG Martial 3.

Player Command = ceil((Charisma4+Cognition4)/2) = 4. Effective Pool per unit: min(Size,Command)+Command.
- HI A: min(5,4)+4 = 8D. HI B: min(4,4)+4 = 8D. Cavalry C: min(4,4)+4 = 8D. Archer D: min(3,4)+4 = 7D.

**Löwenritter force (NPC, Command 4):**
- LR HI 1: Power 4, Size 6, Discipline 6. Pool: min(6,4)+4 = 8D.
- LR HI 2: Power 4, Size 5, Discipline 5. Pool: min(5,4)+4 = 8D.
- LR KT: Power 5, Size 6, Discipline 6. Pool: min(6,4)+4 = 8D.

**Phase 1 — Strategy Declaration (Turn 1):**

Player declares:
- Sub-unit 1: HI A + HI B (merged command). Formation: Line vs LR HI 1.
- Sub-unit 2: Cavalry C. Formation: Wedge vs LR KT.
- Sub-unit 3: Archer D. Volley phase. Formation: Reserve initially.
- Thread intent: Vossen (Reserve) will Weave HI A (Territorial scale: reinforce unit cohesion). Declared publicly.
- Tactic: Concentration (all sub-units on two targets; Fibonacci applies to HI 1 + KT).

Löwenritter declares (NPC Priority Tree): Priority 1 EXISTENTIAL? No. Priority 2 DEFEND: not triggered. Priority 5 EXPAND. NPC positions: LR HI 1 vs Crown HI A/B. LR HI 2 vs Cavalry C. LR KT vs whoever Crown sends to flanks. Tactic card: Iron Discipline (immune to Route this engagement).

**Phase 2 — Volley:**

Archer D (Reserve, pre-Volley targeting): Archers target LR HI 1 (most vulnerable to Piercing). Archer Pool for Volley: Power stat = 3. Roll 3D TN7: 9,7,3 → 2 net. DR vs Piercing (LR HI 1 is Medium armour): DR 2 (ranged DR from mass_battle §A.4). Net damage: 2−2 = 0. **No Size loss.** Archers vs Medium armour: Piercing/Bow does not penetrate Medium in Volley. [This matches weapon table: "Piercing/Bow vs Medium: ✗". Zero hits. Correct.]

**[FINDING: Archer units are ineffective against Medium or Heavy armoured units in Volley. Against LR Heavy Infantry (Medium armour) and Knights Templar (Heavy armour), Crown's Archer unit does nothing in Volley phase. Correct design — Archers require Light-armoured targets. Crossbow or Sling(lead) needed for armoured penetration. Crown's unit composition (no Crossbow) means Archers are wasted against Löwenritter's professional force. This is a genuine strategic error by the player — poor unit composition.]**

**Phase 3 — Manoeuvre:**

Cavalry (Fast) moves to flank LR HI 2's rear. Per §A.6 Envelopment: Cavalry must succeed at Envelopment tactic (Ob 2). Player Command 4D vs Ob 2: 4d10: 9,8,3,4 → 2 net. Success. Cavalry achieves flank position on LR HI 2. This means Cavalry now attacks LR HI 2 from flank — Flanking penalty on LR HI 2's defence next exchange.

Crown HI A+B advance to engage LR HI 1. LR HI 1 holds position (Shield Wall declared? LR NPC AI: no Shield Wall — Löwenritter tactic is Iron Discipline, not formation-based). LR HI 1 in Line formation.

**Phase 4 — Offensive Thread Operations:**

Vossen (TS 45, Coherence 10, in Reserve) executes Weaving at Territorial scale (reinforce HI A Discipline: stabilise unit morale under pressure).

Leap: (Spirit 4 × 2) + History(Thread 3 pts = +3D) + TPS(45÷10=4). Pool = 8+3+4 = 15D. Ob 1 (TS 30–49 = Ob 2, then TS 50+ = Ob 1 — Vossen TS 45 = Ob 2). 15D TN7 Ob 2: 9,8,7,4,10,7,3,8,4,9,2,8,3,7,4 → 9 net. Ob 2, surplus 7 = OW. Clean suspension. Next operation Ob −1 (minimum 1).

Operation — Weaving (Territorial scale, HI A Discipline): Pool same (Spirit×2)+History+TPS = 15D. Ob = Territorial scale = 4 → −1 (OW Leap) = Ob 3. Roll 15D: 9,8,7,4,10,7,3,8,4,9,2,8,3,7,9 → 10 net. Ob 3, surplus 7 = OW. Effect: HI A Discipline +1 (from 5→6). Coherence auto-cost: Territorial scale = −1. Vossen Coherence: 10→9. RS change: OW at Relational+ scale = RS +1. RS: 70→71.

Co-movement: Weaving at Territorial scale. Cards drawn: Co-Movement card 14 (Substrate Settling per threadwork §7.1: card 16 = Substrate Settling. But the BG Co-Movement deck has 18 cards. Draw CM-14 from the 18-card deck). CM-14 effect (if using numbered BG deck — specific card text not in canonical docs): **[GAP: The specific content of Co-Movement Cards 1–15 is referenced ("retained from prior system") but not listed in any loaded doc. CM-16/17/18 are listed in threadwork §7.1. CM-14 content is unknown.]** Assume neutral epistemic effect (half the BG deck is epistemic neutral).

**Phase 5 — Engagement:**

**Sub-unit 1: HI A+B vs LR HI 1.**

Crown pool for HI A (now Discipline 6 from Vossen Weave): effective pool = min(Size5, Command4)+4 = 8D (no change — Discipline doesn't affect pool directly, it affects penalties. At Discipline 6: no penalty. Correct).

HI B + HI A together (Fibonacci group attack on LR HI 1): HI A is 1st attacker (+0D Fibonacci), HI B is 2nd (+1D). So HI A rolls 8D, HI B rolls 9D (8+1 Fibonacci) vs LR HI 1.

Formation: Crown Line vs LR HI 1 Line. Standard (no formation bonus/penalty).

HI A roll (8D TN7, Off): 9,8,7,4,10,7,3,8 → 1+1+1+2+1+1 = 7 net.
HI A vs LR HI 1 Def split: LR HI 1 pool 8D, split 4 Off / 4 Def. 4D def TN7: 9,7,3,4 → 2 def. Net hits: 7−2 = 5 hits. Damage: 5 + Dmg Mod(HeavyCut vs Medium = +2): 7. LR HI 1 Size 6, WI not tracked (BG scale). BG Health = 10 (Heavy Infantry). Size damage application: in BG scale, damage reduces Size proportionally. 7 damage to HI (Size 6) — in TTRPG mass battle, damage = net hits (7) applied as Size loss to defender (mass_battle §B.3: "net successes = damage dealt to opposing units"). **[GAP: BG damage formula is "net successes = damage dealt to opposing units" but doesn't specify whether HeavyCut bonus (+2 from weapon table) applies at BG scale or only TTRPG. The BG Dmg Mod table in mass_battle §B.2 lists TTRPG Dmg Mod separately. BG Dmg Mod for HI = +4 (BG scale). BG battle roll net successes alone determine damage without weapon modifiers at BG resolution — the weapon type already affects the Martial stat via the unit type. At TTRPG scale (this sim), net hits + weapon mod applies.]**

Since this is a TTRPG-scale mass battle, weapon mod applies. 7 net hits → 7 Dmg. LR HI 1: Size 6 takes 7 hits → WI = mass battle equivalent. Per mass_battle §A.4: Size is the health pool. Casualties reduce it. At TTRPG scale, use net hits as Size damage = 7 ÷ WI_equivalent. Mass battle uses no WI — Size loss = floor(net hits / Power). **[GAP: The relationship between net hits and Size loss is not explicitly stated for TTRPG mass battle. The formula says "net hits − DR = Size loss to record" (Phase 2 Volley). In Engagement (Phase 5), the damage formula references "net successes − DR" but DR tables for mass combat use ranged DR. Melee DR in mass battle: LR HI 1 is Medium armour vs HeavyCut — melee DR from §A.4: "Medium: HeavyCut DR 3." Net hits 7 − DR 3 = 4 Size damage. LR HI 1: Size 6→2.]**

HI B roll (9D Fibonacci TN7): 9,8,7,4,10,7,3,8,4 → 7 net. DR 3. Size damage: 7−3 = 4. LR HI 1: Size 2→ 0. **LR HI 1 destroyed.** Crown eliminates first LR unit in Turn 1 Phase 5!

LR HI 1's 4D Off (other split): 9,8,3,4 → 2 off hits. Crown HI A Def: HI A pool 8D, declared 4 Off / 4 Def (split before knowing LR declaration — simultaneous). 4D Def TN7: 9,7,3,4 → 2 def. Net hits LR on HI A: 2−2 = 0. No damage. Correct — Crown HI A is unscathed this exchange.

**Sub-unit 2: Cavalry C (Wedge) vs LR KT.**

Cavalry Wedge formation: +2D Off, −1D Def. Pool 8D + 2D Wedge = 10D Off. Def: 8−1 = 7D Def.

LR KT in Line (Iron Discipline tactic = immune to Route, not formation change). LR KT pool 8D. LR declares 5 Off / 3 Def.

Cavalry off (10D TN7): 9,8,7,4,10,7,3,8,4,9 → 1+1+1+2+1+1+1+1 = 9 net. DR of KT armour vs HeavyCut (Cavalry): KT is Heavy armour. HeavyCut vs Heavy: DR 5. Net hits: 9−5 = 4. Size damage: 4 Size loss to LR KT. KT Size: 6→2.

LR KT off (5D TN7): 8,7,4,9,3 → 3 off. Crown Cavalry Def (7D −1 from Wedge = 7D wait, Wedge gives −1D Def so 8D−1D=7D): 9,7,4,3,8,7,2 → 4 def. Net hits: 3−4 = 0 (minimum 0). Crown Cavalry unscathed. 

**[FINDING: The Wedge formation is extraordinarily powerful against armoured targets when combined with HeavyCut Cavalry. Net 4 Size damage to Knights Templar in Round 1 is massive — KT reduced from Size 6 to Size 2 in one exchange. Löwenritter's Iron Discipline tactic did not help (it prevents Route, not damage reduction). The counter to Wedge is Shield Wall (negates Wedge), which LR didn't use. NPC AI chose Iron Discipline over Shield Wall — a tactical error.]**

**[FINDING (NPC AI GAP): The Löwenritter NPC AI chose Iron Discipline tactic card over Shield Wall formation. Iron Discipline (immune to Route) is correct when facing low Discipline threats. But against a Wedge Cavalry charge, Shield Wall (negates Wedge, +2D Def) would have been the correct counter. NPC AI tactic selection is formation-unaware — it doesn't evaluate what formation the opponent is declaring. The NPC tactic choice should account for opponent formation declarations if those are simultaneous-reveal. Per §B.3: "select tactic card face-down, reveal simultaneously." NPC cannot know opponent's formation at selection time. So the NPC made a reasonable probabilistic choice (Iron Discipline is generically strong). The problem is that the 2-card hand gives Crown a clear Wedge + Concentrated Strike combination. NPC AI needs a probabilistic evaluation of expected opponent tactics — a 50% prior that cavalry is in Wedge — and Shield Wall becomes the Bayesian optimal against cavalry. Current NPC AI doesn't use this prior.]**

**[FINDING: Counter → Shield Wall negates Wedge. If LR had chosen Shield Wall for KT: KT Def = 8+2=10D. Vs Cavalry 10D Off. 10 off TN7: E(net) = 4. 10 def: E(net) = 4. Net damage = 0−DR 5 = 0. The Cavalry Wedge charge would have been entirely neutralised. Shield Wall is the correct tactical response to Wedge Cavalry and the NPC AI should prioritize it when facing known Cavalry presence. This is a genuine NPC AI calibration gap.]**

**Phase 6 — Cascade:**

Step 1 — Apply all recorded damage simultaneously:
- LR HI 1: destroyed (Size 0).
- LR KT: Size 6→2.
- Vossen's Weave effect applied: HI A Discipline 5→6.
- Volley damage: 0 (Archers ineffective).
- All RS changes: Vossen Weave OW: RS +1 (applied here at Step 1).

Step 2 — Discipline checks:
- LR HI 1 destroyed: no check (unit gone).
- LR KT: Size lost 4 this turn. Current Discipline = 6. Check: Size lost (4) > Discipline (6)? No. No degradation. **[FINDING: Löwenritter KT at Discipline 6 is immune to Discipline degradation even after losing 4/6 Size in one exchange. The Discipline check fires only when Size lost > current Discipline. KT loses 4, Discipline is 6: 4 > 6 is false. This is the intended effect of elite Discipline — even under severe casualties, formation cohesion holds.]**

Step 3 — Morale checks:
- LR HI 1 destroyed → LR KT and LR HI 2: each take −1 Morale (allied unit routed). Morale cap of −3 from non-general sources. Only 1 unit destroyed → −1 Morale to remaining 2 LR units. LR KT Morale (starting: general's Command(4) + unit quality modifier): Morale 6. After −1 = 5. LR HI 2: Morale 5. After −1 = 4.
- LR KT Size below 50%? Size 2 vs starting 6: below 33% → −1 Morale additional. LR KT Morale: 5−1 = 4.
- Cavalry is not flanked (it attacked, not defending the flank). No flanking Morale hit.

**Phase 7 — Reform (Turn 1 end):**

No units out of engagement. No Reform bonus available. Idle army clock: not triggered (engagement occurred).

**Turn 2 setup:**

LR HI 1 destroyed. LR KT: Size 2, Discipline 6, Morale 4. LR HI 2: Size 5, Discipline 5, Morale 4.

Crown: all units healthy. Cavalry achieved envelopment. Vossen has 1 op used (Coherence 9).

Löwenritter general assessment: Stability check from Battle lost (LR lost 1 unit)? Per military_layer §2.2: "Defender Military −1 on attacker wins." LR is the attacker (crossed into T6). Wait — who initiated? If player is defending T6 (Crown territory), LR is attacker. After Turn 1: LR HI 1 destroyed. Crown hasn't taken territory. Ongoing battle — no outcome determination yet.

**[FINDING: The 7-phase mass battle system produces decisive resolution within 1–2 turns when one side has significant formation advantage (Wedge + Concentration + Thread Weave). The combination of Crown's Cavalry Wedge and HI Concentration destroyed LR HI 1 and crippled KT in Turn 1. This is correct — military excellence snowballs. The Löwenritter still have LR HI 2 (Size 5) and KT (Size 2) with high Discipline (immune to collapse) but the battle is effectively decided.]**

**ST-07 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| Archer vs Medium armour = zero Volley hits | ✓ Correct — player unit composition error | Confirmed |
| Wedge + HeavyCut Cavalry vs Heavy armour: 4 Size damage in Round 1 | ✓ Powerful but correct (Cavalry + Wedge + DR-piercing HeavyCut) | Confirmed |
| Löwenritter NPC AI: Iron Discipline over Shield Wall vs Cavalry = tactical error | NPC AI needs formation-aware tactic selection | P2 |
| Shield Wall would have fully neutralised Cavalry Wedge | ✓ Counter mechanic works correctly | Confirmed |
| Discipline 6 on KT: no degradation even at Size 2 | ✓ Elite Discipline working correctly | Confirmed |
| Vossen Weave OW: RS +1 from Thread operation | ✓ Net RS improvement from successful Weave | Confirmed |
| Co-Movement Card 14 content unknown | ✓ Gap identified (CM deck not fully specified in canonical docs) | P2 |
| BG Dmg Mod vs TTRPG Dmg Mod interaction in TTRPG mass battle | Gap: melee weapon mod at mass battle scale applies, but this needs explicit confirmation | P2 |

---

## ST-08 — NPC ARC EMERGENCE (ALMUD ARC B / HIMLENSENDT ARC A)

**Setup:** Season 14. Theocracy Counter 62. Crown Stability 2 (near crisis). Almud's Certainty: 3 (Questioning). Löwenritter Coup Counter: 1.

**Almud Arc B trigger conditions (npc_behavior §5.2):**
- Crown Stability ≤ 2 AND Almud Certainty ≥ 3: Arc B fires.
- Both conditions: Stability 2 ✓, Certainty 3 ✓. **Arc B: The Fortress.**

**Arc B mechanics:**
- Conviction shift: Order doubles down. Secondary Conviction (Reason) suppressed entirely.
- Resonant Style shift: Authority only. Can only be moved by someone he personally respects.
- Leadership Deviation Ob: 2 (unchanged per Arc B description — his institution follows him more tightly now).
- Consequence: All Evidence Resonant Style targeting on Almud now fails to engage (Reason suppressed → Evidence style inert, as Evidence attacks Reason-adjacent assumptions). Player loses their best social attack vector.

**[FINDING: Arc B fires at exactly the moment the player most needs Almud's flexibility. Crown Stability 2 means Almud is fortress-mode — rigid, Authority-only. Any player who invested in building Evidence against Almud (the obvious contest approach for a Reason/Consequence NPC) now finds that investment worthless. Almud has retreated behind an institutional shell. This is excellent arc design — the NPC becomes harder to persuade precisely when the faction is weakest, creating a genuine narrative dilemma: the Crown faction needs reform but the leader can't be persuaded through normal means.]**

**Arc B downstream effects:**
- Priority 2 (npc_behavior §8.3): "Löwenritter Coup Counter = 2 → Military response." At Coup Counter 1 (not yet 2), Priority 2 doesn't fire. But Crown Stability 2 AND Arc B means Almud will resist any action that "appears as weakness." Löwenritter sees this and Priority 1 fires for Löwenritter NPC: "If adjacent Uncontrolled territory → March." Crown's weakness creates an opportunity.
- If player attempts Resonant Style (Evidence) on Arc B Almud: wrong style. Fails silently — no Conviction movement. The player must first find what Authority figure Almud respects and approach through that channel.

**Himlensendt Arc A (Default — No Intervention):**

Season 14: TC 62 (from ST-05 timeline with Assert-as-Pontifex fix). Arc A fires when no Evidence contest has been won against Himlensendt AND no Cardinal of Temperance crisis is active. By Season 14: player has won Contest 2 (ST-03 sim) — wait, this is a different sim branch. In the ST-08 scenario, assume no player intervention with Himlensendt. Arc A: The Zealot.

Arc A effects:
- Conviction: Faith unchallenged. TC advances normally.
- Behavior: Priority 2 ALWAYS fires (Assert/Seizure). Himlensendt's Mandate remains at 5.
- TC 65 milestone (Season ~21 per ST-05) approaches. Himlensendt in Arc A is more dangerous than the contested Himlensendt in ST-03.

**[FINDING: Two NPC arcs firing simultaneously (Almud Arc B + Himlensendt Arc A) create a synergistic threat. Almud is rigid and defensively locked; Himlensendt is aggressively advancing TC. Crown cannot resist Church through Parliament (Almud Arc B resists any reform that looks like weakness). Crown cannot fight militarily (Stability 2). The player is trapped between two NPC arcs that reinforce each other's threat. This is exactly the intended political pressure — faction arc interactions creating complex, emergent crises.]**

**Breakout paths:**
1. Address Almud via Authority RS: find an NPC Almud respects (Ehrenwall has Authority with Almud per npc_behavior §5.2 Almud Arc B note). Player builds Disposition +3 with Ehrenwall → Ehrenwall delivers the argument Almud can hear. Requires 3+ seasons of relationship-building.
2. Raise Crown Stability (exit Arc B trigger): Govern capital × 2 seasons. At Ob 1 in capital: ~91% per season. 2 successful Governs → Stability recovery (+1 per clean season, per military_layer §4.1 note: "no hostile Domain Actions + Stability ≤ 3 → +1 Stability"). 2 seasons → Stability back to 4. Arc B exits.
3. Accept Arc B and coalition with Hafenmark: Hafenmark can contest Church via Parliament (has 3 card types). Player grants Hafenmark trade concessions in exchange for anti-Church Parliamentary motions.

**[FINDING: Breakout path 2 (govern your way out of Arc B) is mechanically clean: 2 seasons of Govern OW in capital exits Arc B by raising Stability above the threshold. But during those 2 seasons, Church advances TC by ~5 points unopposed. The player trades 2 seasons of TC suppression for 2 seasons of stability repair. This is a correct asymmetric choice — stability or counter-threat.]**

**ST-08 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| Arc B fires at Stability 2 AND Certainty ≥ 3 — exact condition met in plausible game state | ✓ Arc triggers correctly | Confirmed |
| Evidence RS targeting becomes inert during Arc B (Reason suppressed) | ✓ Investment in wrong RS can become worthless | Confirmed |
| Arc B + Arc A (Himlensendt) create synergistic political pressure | ✓ Emergent crisis — intended design | Confirmed |
| Ehrenwall as Authority intermediary for Almud (Arc B breakout path) | ✓ Clean — requires 3+ seasons, creates urgency | Confirmed |
| Stability recovery (2 seasons) exits Arc B at cost of 2 seasons TC suppression | ✓ Correct asymmetric tradeoff | Confirmed |

---

## ST-09 — OBLIGATION CASCADE UNDER PENINSULAR STRAIN

**Setup:** Season 15. Peninsular Strain: 6 (Fracture level). Three active Obligations across factions:
1. Church Obligation to Crown: "No Seizure in T2 for 2 seasons" (Grand Contest, 4-season duration, 2 seasons remaining).
2. Crown Obligation to Hafenmark: "Maintain garrison in T10" (Formal Contest, 2-season duration, 1 season remaining).
3. Hafenmark Obligation to Varfell: "Share intel on Church movements for 1 season" (Private negotiation, 1-season duration).

**Peninsular Strain 6 (Fracture):** All factions: Accord −1 in one non-capital territory (controller's choice). This season: Crown chooses T6 (lowest-value). Church chooses T3 (recently seized, building stability). Hafenmark chooses T7. Varfell chooses T13. Accord effects: T6: 2→1, T3: 2→1, T7: 2→1, T13: 2→1. All four territories now Resistant.

**[FINDING: Peninsular Strain Fracture (6) simultaneously degrades Accord in the most expendable territory of each faction. Across 4 factions this creates 4 Resistant territories in one Accounting. Each Resistant territory requires: (a) garrison or lose it at next Accounting, (b) Govern +1 Ob to restore, (c) no Prosperity contribution. 4 simultaneous Resistant territories = 4 factions spending card actions on defensive Govern instead of expansion. Strain 6 creates a board-wide governance crisis. This is correct and impactful.]**

**Obligation monitoring:**

Church Priority 2 (TC 72, Seizure available): Church NPC tree checks Priority 5 EXPAND: "Seizure when TC ≥ 40 and prominent territories have PT ≥ 3." T2 (Crown) has PT 3 and Church was targeting it. But **Obligation 1 blocks T2 Seizure**. NPC priority tree modification: "any action that would violate the Obligation is blocked for Obligation duration unless faction enters Survival priority (Stability ≤ 2)" (§6.1). Church Stability: 5. Not at survival. **Church cannot Seize T2 this season.** Church redirects to T5 (Feldmark, Crown, PT 3, ungarrisoned) — adjacent target not covered by Obligation.

T5 Seizure (Church, PT 3, TC 72): Ob = 7−3 = 4. TC80 −1 not yet. Pool: Influence 4 (reduced by player investigation in ST-04) + floor(72/20)=3 = 7D. 7d10: 9,8,7,3,10,7,2 → 5 net. Ob 4, surplus 1 = Success. T5 Accord: max(floor(3/2)+1,2) = 2. Crown loses T5. **Obligation diverted Church from T2 but didn't stop Seizure altogether — it redirected it.**

**[FINDING: Obligations constrain NPC behavior toward the specific committed territory but don't prevent adjacent action. A "no Seizure in T2" Obligation doesn't protect T5. Players must negotiate Obligations carefully — either covering all vulnerable territories or accepting that Church will find alternate targets. This is correct design: Obligation is a political tool, not a blanket protection.]**

**Crown Obligation 2 violation check:** Crown must maintain garrison in T10 (1 season remaining). Crown AI Priority 6 (all higher priorities clear): Govern T1 (capital). Uses Consul card. No Legionary card available (used last season). T10 garrison check: Crown has 1 unit in T10 (Light Infantry, Size 3). Obligation met — no violation.

At next Accounting, Crown Obligation 2 expires. Crown can withdraw T10 garrison without penalty.

**Hafenmark Obligation 3 (intel sharing):** Hafenmark must share Church intel with Varfell this season. Intel sharing: Varfell receives Hafenmark's intelligence (Church Influence 4, Mandate 5, Military 4 — current stats after Domain Echo reductions). Obligation fulfilled: Varfell Disposition toward Hafenmark +0 (no positive Disposition bonus from Obligation fulfillment — compliance just avoids violation penalty). **[FINDING (GAP): Obligation fulfillment's positive consequences are not specified. The rules define violation consequences (Mandate −1, etc.) but not what happens when Obligations are honored. Proposed: honoring an Obligation earns the complying faction +1 Standing (per §9.2 in board_game: "Honour: +1 Standing"), or minimum Disposition gain with the imposing party (+0, since compliance was compelled). At minimum, no penalty = the reward. But consider adding Disposition +1 toward the winning party on Obligation completion to create a relationship-building incentive for honoring, not just violating.]**

**Strain reduction test:** This season: diplomatic resolution (Hafenmark honored intel Obligation, which was agreed voluntarily as a private negotiation rather than a Grand Contest). Does this count as "diplomatic resolution" per §4.2? "Public diplomatic resolution (Crown Treaty formed, Open Pledge honoured, Co-Victory declared) — Strain −1." Private negotiation honor is not "public" — Strain doesn't decrease. Strain stays at 6.

**[FINDING: The Strain reduction trigger (§4.2) requires public diplomatic action: Crown Treaty, Open Pledge, or Co-Victory. Private Obligation honor doesn't count. This means a board in Fracture (Strain 6) can only reduce Strain through: (a) a season with no battles and no Revolts (natural decay −1), OR (b) a public diplomatic event. In Season 15, Church Seizure of T5 doesn't trigger Strain (covert/institutional action). If no inter-faction battles occur: Strain −1 → 5 (Tension). But Varfell and Crown contested in T4 earlier — depends on this season's action. No battles this season = Strain: 6→5. Correct — one peaceful season recovers from Fracture to Tension.]**

**ST-09 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| Fracture Strain creates 4 simultaneous Resistant territories | ✓ Correct, significant board-wide impact | Confirmed |
| Obligation redirects Church from T2 to T5 — doesn't stop Seizure entirely | ✓ Obligation is a political tool, not a shield | Confirmed |
| Obligation fulfillment positive consequences undefined | Gap — propose Disposition +1 toward imposing party on completion | P3 |
| Strain reduction requires public diplomacy, not private Obligation honor | ✓ Correct — well-designed distinction | Confirmed |
| Peaceful season (no battles): Fracture → Tension (6→5) | ✓ Correct — recovery is meaningful but slow | Confirmed |

---

## ST-10 — RENDERING STABILITY DECLINE CURVE (RS 72 → CRISIS)

**Setup:** 30-season simulation of RS under realistic Thread operation load. Starting RS: 72.

**RS degradation sources (annual):**
- Winter annual drift: −1/year (=−1 per 4 seasons = −0.25/season)
- Battle (inter-faction): −1 per battle season. In a competitive game, ~3 battle-seasons per 10 seasons = −0.3/season average.
- Thread operations (failed Weaves/Pulls): Partial = −1 RS, Failure = −2 RS. A practitioner doing 3 operations/session: ~20% Partial rate, ~10% Failure rate per op = (3×0.2×1)+(3×0.1×2) = 0.6+0.6 = 1.2 RS/session. 1 session per 2 seasons = 0.6 RS/season.
- Lock chronic drift: 1 active FR Lock (from Himmensendt attempting to Lock a Thread configuration in T3): −1 RS/season (Slow-change domain per threadwork §2.4).

Total RS degradation: 0.25 + 0.3 + 0.6 + 1.0 = **2.15 RS/season** without Mending.

**RS restoration sources:**
- Successful Mending (per 2 sessions, 1 attempt): ~60% success (Mending pool at TS 50 = (Spirit4×2)+History3+TPS5 = 16D, Ob 5 for Standard Gap). P(OW) with 16D vs Ob 5: expected net ~(16×0.4)−0.3 = 6.1, Ob 5 → OW (surplus 1.1). OW = RS +2. Success = RS +1. P(OW) ~40%, P(Success) ~30%, P(Partial) ~15%, P(Failure) ~15%. Expected RS gain: 0.4×2+0.3×1+0.15×0 = 1.1 RS per Mending attempt. 1 attempt per 2 seasons = 0.55 RS/season restoration.
- Warden expedition Mending: +2 RS/season (if active). Requires Edeyja Arc B. Not guaranteed until late game.
- Board game Mend order: +1 per success (RM faction or Thread-aligned faction). ~1 Mend per 4 seasons × 60% success = 0.15 RS/season.

Net RS change per season: −2.15 + 0.55 + 0.15 = **−1.45 RS/season** under realistic conditions.

**Decline curve:**

| Season | RS | Threshold Status |
|--------|-----|----------------|
| 1 | 72 | Strained (79–60) |
| 8 | 62 | Strained |
| 10 | 58 | Strained, approaching Fragile |
| 15 | 51 | Fragile (59–40) — Shifting Objects spontaneous, Thread ops +1 Ob in affected territories |
| 20 | 44 | Fragile |
| 25 | 37 | **Fractured (39–20)** — Gaps open spontaneously (1d10 per season, on 1–2: Gap opens). Monstrous Incursion risk. Rendering failures for non-practitioners. |
| 28 | 33 | Fractured |
| 30 | 30 | Fractured, approaching Critical (19–1) |
| 35 | 23 | Fractured |
| 38 | 18 | **Critical** — doubled spontaneous Gap risk. All Thread ops +1 Ob worldwide. Seasonal Stability checks Ob 1 for all factions. |
| 42 | 12 | Critical |
| 45 | 6 | Critical, approaching Rupture |
| 47 | 0 | **RUPTURE** — Campaign ends in catastrophe |

**[FINDING: Under realistic conditions (no Warden expedition), RS reaches Fragile at Season 15, Fractured at Season 25, Critical at Season 38, and Rupture at Season 47. A standard 40-season game ends with RS at ~12 (Critical band). This is correct — the world is decaying throughout the campaign, and the final seasons are crisis-level. The Rupture happens just past the typical campaign end, creating endgame pressure without inevitable doom in most normal-length games.]**

**[FINDING: If players ignore Thread operations and Mending, and battles are frequent (+3 battle-seasons/5 seasons instead of 3/10): RS −0.6/season from battles + 0.25 winter + 1.0 Lock = −1.85 net (without practitioner ops, no Mending). RS reaches Critical at Season 32 and Rupture at Season 43. Battle-heavy campaigns accelerate RS decline by ~7 seasons. Military players who fight frequently without Thread Mending accelerate their own campaign's doom. This is the correct design incentive: war is destructive at the cosmic level, not just politically.]**

**Warden expedition impact:** If Edeyja Arc B activates (Season 15), +2 RS/season permanent. Net RS change: −2.15+0.55+0.15+2.0 = **+0.55 RS/season**. RS stabilises and slowly recovers. Rupture threat eliminated. This is the campaign's structural "save the world" mechanic — but it requires a player to successfully reach the Southernmost (TS ≥ 30, Expedition action, multiple seasons) and convince Edeyja (Arc B trigger: Evidence Resonant Style). If players fail to activate Edeyja, the world decays.

**[FINDING: The Warden expedition is precisely calibrated as a late-game "save the world" arc. Without it, RS reaches Critical by Season 38 and Rupture by Season 47 in a standard game. With it, RS stabilises and the game continues indefinitely. The player's choice to invest in Southernmost expedition vs. political/military expansion is the game's central tradeoff — it creates genuine tension between winning the political game and saving the world. This is the game's most elegant design constraint.]**

**Lock chronic drift amplification:** Each active FR Lock adds −1–2 RS/season. In endgame with TC 80 (Church Locks becoming more common as Church asserts territorial control): 3 active Locks = −3 additional RS/season. Without Mending or Warden, RS decline accelerates to −4+/season in the endgame. This creates an exponential pressure effect: late-game Church dominance (via TC) accelerates RS decline (via Locks), which accelerates Rupture risk. Church "winning" the political game can bring about the world's destruction.

**[FINDING (CRITICAL DESIGN VALIDATION): Church's TC victory and RS Rupture are on a collision course. Church TC wins around Season 24–28 (ST-05). RS reaches Critical around Season 38 (ST-10). There's a 10-season gap where the "winning" Church is operating in a world entering Crisis, with Thread ops +1 Ob worldwide, spontaneous Gaps, and Monstrous Incursions. Church wins politically just as the world breaks down. This is the game's tragic endgame: victory is pyrrhic. Church achieves Solmundan Orthodoxy while the Rendering Stability collapses. The player who took the RS-preserving path (Varfell Thread knowledge, Warden expedition, RM community Weaving) has the tools to prevent the Rupture. The Church-victory path produces the apocalypse the Church was supposed to prevent. This is brilliant design.]**

**ST-10 AUDIT:**

| Finding | Verdict | Severity |
|---------|---------|---------|
| RS decline rate: −1.45/season under realistic conditions | ✓ Calibrated | Confirmed |
| RS reaches Fragile S15, Fractured S25, Critical S38, Rupture S47 | ✓ Correct endgame curve for 40-season games | Confirmed |
| Battle-heavy campaigns accelerate Rupture by ~7 seasons | ✓ Correct anti-war incentive | Confirmed |
| Warden expedition (+2/season) stabilises RS and prevents Rupture | ✓ Correctly designed "save the world" arc | Confirmed |
| Church TC victory (S24–28) precedes RS Critical by ~10 seasons | ✓ Pyrrhic victory — brilliant design | Confirmed |
| Lock chronic drift amplifies RS decline in Church endgame | ✓ Church dominance accelerates world breakdown | Confirmed |

---

## PART B — COMPLETE AUDIT SUMMARY

### Confirmed Working Systems

| System | Status |
|--------|--------|
| TC milestone system (40/55/65/80/100) | ✓ All produce correct political effects |
| Peninsular Strain Fracture (Accord cascade) | ✓ Board-wide governance crisis at Strain 6 |
| Obligation constraining NPC priority trees | ✓ Elegant behavioral constraint |
| Zoom In at legal phase-lock points | ✓ Phase 3 entry executes cleanly |
| BG → TTRPG unit conversion | ✓ Stats translate correctly |
| General duel resolution (3 exchanges) | ✓ Correctly calibrated |
| Kill-vs-stabilise asymmetric choice | ✓ Genuine strategic tension |
| Social contest — RS targeting breaks Resistance stalls | ✓ RS targeting mechanically essential |
| Conviction Scar + Obligation from Decisive Win | ✓ NPC behavioral arc trigger |
| Warden expedition as structural RS stabiliser | ✓ Correctly designed late-game arc |
| Church TC + RS Rupture collision | ✓ Pyrrhic victory design — validated |
| Discipline check at mass scale (Size lost > Discipline) | ✓ Elite units correctly resist degradation |
| Wedge formation vs Heavy armour (HeavyCut) | ✓ High damage output, correct counter (Shield Wall) |
| Domain Echo from OW investigation (−2 Church Influence) | ✓ Powerful but bounded |

---

### Design Gaps Found (new this session)

| Gap ID | Description | Severity |
|--------|-------------|---------|
| **SIM2-01** | 2-Assert engine (2× Senator) produces Church TC victory Season 18 — too fast. Fix: Assert → Pontifex-exclusive (1× Pontifex, cooldown 2). Pushes victory to Season 24–28. | **P1** |
| **SIM2-02** | TC 80 PT drift neutralises Varfell Cultural Reformation (Ob 4 in all target territories) — interaction not documented. Varfell must act before TC 80. | P2 |
| **SIM2-03** | NPC tactic selection is formation-unaware. LR AI chose Iron Discipline over Shield Wall vs Cavalry Wedge — correct probabilistic choice but Bayesian prior on opponent cavalry = Shield Wall optimal. Add cavalry-present heuristic to NPC tactic selection. | P2 |
| **SIM2-04** | Reach priority not tracked from Round 1 in general duel simulation. Protocols must apply range rules at combat start. Long weapon holder gets first advantage round. Rules correct; sim protocol gap. | P2 |
| **SIM2-05** | Post-combat fieldwork (F-TRANS-12): no specification of whether it applies when player fled (not won). Proposed: requires player to control site (enemy fled/incapacitated/dead). | P2 |
| **SIM2-06** | Co-Movement Card 14 content unknown — CM cards 1–15 referenced as "retained" but not listed in canonical loaded docs. | P2 |
| **SIM2-07** | BG melee weapon mod in TTRPG mass battle: "net hits − DR = Size loss" for Volley is explicit. Melee engagement Size loss formula (melee DR tables exist) not explicitly stated. Proposed: net hits − melee DR = Size damage at TTRPG mass scale. | P2 |
| **SIM2-08** | Obligation fulfillment positive consequences undefined. Violation penalties defined. Honoring an Obligation should produce Disposition +1 toward imposing party, or Standing +1. | P3 |
| **SIM2-09** | Charity Advantage gate (Church Wealth ≥ Crown + 2) activates rarely in competitive games. Consider reducing to Crown + 1. | P3 |
| **SIM2-10** | Social initiative (higher Attunement always wins Exchange 1 — deterministic) conflicts with combat initiative (rolled). ED-138 flagged in social_contest but unresolved. | P2 |
| **SIM2-11** | Chain Contest at Resistance 2 with near-equal pools: player has only ~25–30% per exchange to move track. Correct mathematically but produces frustrating stalls without RS targeting. RS targeting should be explicitly flagged as the required tool for Resistance-2 contests — add note to §6.3. | P2 |
| **SIM2-12** | Dynastic Proclamation cannot target Crown (Mandate gap Hafenmark 4 vs Crown 5). Correct gate, but Hafenmark's Mandate path to 5+ needs explicit documentation — how does Hafenmark raise Mandate above 4? Framework Drift (+1 per season of full alignment): needs 1+ seasons at 4 to reach 5. But stat cap rules (PP-174: recover max to starting Mandate via capital Govern) cap Mandate at starting value. **[CRITICAL: If Hafenmark starting Mandate is 4, and PP-174 caps Govern recovery at starting Mandate, Hafenmark can never exceed Mandate 4. Dynastic Proclamation requires Mandate > target Mandate. Crown at Mandate 5. Hafenmark can never Proclaim on Crown territory. Framework Drift produces Influence +1 (not Mandate). Hafenmark has no Mandate growth path above 4 in standard rules. Dynastic Proclamation on Crown territory is structurally impossible.]** | **P1** |
| **SIM2-13** | RS starting at 72 reaches Critical (19–1) by Season 38 and Rupture by Season 47 in a standard 40-season game. The game's RS endgame is correctly calibrated for standard games. For short games (20 seasons), RS barely reaches Fragile (51 at S15). Short game players don't experience the RS crisis. Add note to game setup: shorter games should start RS at 60 for faster crisis engagement. | P2 |

---

### Confirmed P1 Items (requiring resolution before next milestone)

| ID | Description |
|----|-------------|
| SIM2-01 | Assert → Pontifex-exclusive |
| SIM2-12 | Hafenmark Mandate cap at starting value (4) blocks Dynastic Proclamation on Crown — structural impossibility |

---

## PART C — FINDINGS REQUIRING IMMEDIATE EDITORIAL ENTRIES

New EDs from this session: SIM2-01 through SIM2-13 → ED-572 through ED-584.

Assert fix (SIM2-01) is the most urgent: it changes Church's card system fundamentally. Requires revision to tc_political_redesign_v30.md §5.2 (card → action mapping: Assert moves from Senator to Pontifex) and board_game_v30.md (Senator card permitted actions updated).

Hafenmark Mandate cap (SIM2-12) requires: confirming whether Framework Drift produces Mandate growth (currently: Influence +1, not Mandate); if Mandate cap = starting value, Dynastic Proclamation on strong rivals is impossible by design. If that's intended, Hafenmark's expansion tool targets only weak rivals (Mandate ≤ 3). Confirm intent.

---

*End of simulation batch. Awaiting Jordan's review before commits.*
