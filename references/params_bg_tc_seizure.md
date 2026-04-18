## TC Generation — Seasonal (canonical: military_layer_v30 §3, tc_political_redesign_v30 §§1–3)
**Starting TC: 28. TC runs to 100 (no freeze). Milestone system: see victory_v30 §7.**

Seasonal TC at Accounting (execute in order, per military_layer_v30 §3):
1. **Conditional Passive (§3.2):** TC +1 only if Church Mandate > controlling faction Mandate in ≥ 2 territories.
2. **Piety Yield (§3.3):** TC += Σ(PT tier × SW/5) per prominent territory, floored. SW = Spiritual Weight per territory (tc_political_redesign_v30 §1).
3. **Charity Advantage (§3.4):** Church Wealth spent on charity → TC +1 per 2 Wealth, cap 2/season.
4. **Templar Presence (§3.5):** +1 TC per territory with Church military unit AND Church Prominence.
5. **Assert (§3.6):** Optional Church action. Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
6. **Suppress (§3.7):** Optional opponent action. Mandate vs Ob = floor(Church Mandate / 2) + 1. Success: negate Step 1. Failure: Stability −1.
7. **Hafenmark Structural Suppression (§3.8):** While Baralta Mandate ≥ 4, TC −1/season.

**TC seasonal cap (PP-504):** ±3 per season from player-initiated Domain Actions. ±5 per season from all sources combined (includes Conditional Passive, Piety Yield, Calamity Drift, event cards).

Legacy TC sources (AER momentum, Attention Pool threshold, Emergency Powers, Free Trade Decree, Church unit presence) are subsumed into the Piety Yield system — Church prominence in high-PT territories captures the same dynamics. AER ≥ 3 still bypasses Hafenmark structural suppression (PP-203).


## Faction Political Pool (tc_political_redesign_v30 §3.4)
**Church:** Political pool = Mandate + floor(TC/20).
**Non-Church (anti-Church motions):** Political pool = Mandate − floor(TC/30).
**Non-Church (non-Church motions):** Political pool = Mandate (no TC modifier).
TC creates asymmetric legitimacy: Church gains political bonus proportional to TC; opponents pay a legitimacy cost proportional to TC when directly opposing Church.


## TC 75 Territorial Seizure (PP-421 — per victory_v30.md §7)
**Note: TC no longer freezes at 75 (see tc_political_redesign_v30 §2). TC 75 marks the milestone where seizure becomes Church's primary mode, but seizure is available from TC ≥ 15 (PP-507). TC continues to 100.**

### Seizure Ob
Ob = 2 + Fort Level + max(0, 3 − PT).
Prominence required: Church Mandate > controlling faction's Mandate in target territory.
Church Mandate ≥ 4 required to attempt seizure.

### Seizure Results
Per victory_v30.md §7. Overwhelming seizure: PT +1 in target territory. This is a consequence effect — NOT subject to the ±1 PT seasonal cap. State-change consequences from seizure are exempt from action caps. (PP-502)

### Seizure Constraints
One seizure attempt per season. Cannot target T15 (Askeheim) or T16 (Schoenland).

### Church Graduated Seizure (PP-494, PP-506–PP-511)
**Available:** Any TC value from TC ≥ 15 (PP-507). Not gated on TC 75. TC 75 freeze marks the phase transition where seizure becomes Church's primary mode, but seizure was always available.
**Pool:** Influence + floor(TC / 15). At TC 28: 7D. At TC 75: 11D (frozen cap). (PP-494)
**Ob:** 7 − PT (target territory Piety value). PT 5 = Ob 2. PT 0 = Ob 7. (PP-494)

| PT | Seizure Ob |
|----|-----------|
| 5 (Piety) | 2 |
| 4 | 3 |
| 3 | 4 |
| 2 | 5 |
| 1 | 6 |
| 0 (Restoration) | 7 |

**Prerequisites:** Church Mandate ≥ 4. Prominence (Church Mandate > controlling faction Mandate). Prominence assessed at seizure declaration. (PP-509)
**Overwhelming:** PT +1 in target territory (consequence, not cap-governed). (PP-494, PP-508)
**Failure:** Stability −1.
**Political cost:** Casus Belli granted to controlling faction on every seizure attempt. (See §Casus Belli.) (PP-510)
**Fort Level:** Fort Level does NOT modify Seizure Ob. Seizure is a political act. (PP-506)
**Battle requirement:** If the target territory has a garrison (Fort ≥ 1 AND at least one military unit present from the controlling faction), Church must first win a Battle before Seizure proceeds. Battle uses standard rules; Fort Level adds bonus dice to defender. If Church wins: Seizure roll proceeds immediately. If Church loses: no Seizure this season; Casus Belli still granted. An ungarrisoned fortified territory (Fort ≥ 1, no units present) may be Seized without Battle. (PP-506)
**Early Seizure political visibility:**
- TC < 50: all factions observe the seizure attempt. No concealment.
- TC ≥ 50: only factions with Intel ≥ 3 in the target territory observe. (PP-507) [PROVISIONAL]
**Mandatory Assert post-TC 75:** Suspended. Assert optional only once TC freezes. (PP-511)
**[ED-355 RESOLVED — PP-506. ED-365 RESOLVED — PP-507. ED-366 RESOLVED — PP-508. ED-367 RESOLVED — PP-509. ED-368 RESOLVED — PP-506. ED-369 RESOLVED — PP-511.]**

### Battle Ob Formula (PP-499, ED-343 resolved)
**Battle Ob = floor(defender Military / 2) + 1.**
Attacker rolls: Military pool vs Ob. Degree table per standard BG degree table (PP-249).
**[PROVISIONAL ED-316] Weight-of-numbers (PP-570):** A faction attacking with Military ≥ 2× defending faction Military forces the defender to Stability −1 at Accounting regardless of battle outcome (the sheer scale is demoralising). Applies once per Accounting regardless of attack count.
[Resolved by PP-548. Battle Ob = floor(defender Military / 2) + 1. Min 1 prevents auto-success vs Military 0 factions (RM). Flagged for simulation confirmation.]




### Seizure Ob
Ob = 2 + Fort Level + max(0, 3 − PT).
Prominence required: Church Mandate > controlling faction's Mandate in target territory.
Church Mandate ≥ 4 required to attempt seizure.


### Seizure Results
Per victory_v30.md §7. Overwhelming seizure: PT +1 in target territory. This is a consequence effect — NOT subject to the ±1 PT seasonal cap. State-change consequences from seizure are exempt from action caps. (PP-502)


### Seizure Constraints
One seizure attempt per season. Cannot target T15 (Askeheim) or T16 (Schoenland).


### Church Graduated Seizure (PP-494, PP-506–PP-511)
**Available:** Any TC value from TC ≥ 15 (PP-507). Not gated on TC 75. TC 75 freeze marks the phase transition where seizure becomes Church's primary mode, but seizure was always available.
**Pool:** Influence + floor(TC / 15). At TC 28: 7D. At TC 75: 11D (frozen cap). (PP-494)
**Ob:** 7 − PT (target territory Piety value). PT 5 = Ob 2. PT 0 = Ob 7. (PP-494)

| PT | Seizure Ob |
|----|-----------|
| 5 (Piety) | 2 |
| 4 | 3 |
| 3 | 4 |
| 2 | 5 |
| 1 | 6 |
| 0 (Restoration) | 7 |

**Prerequisites:** Church Mandate ≥ 4. Prominence (Church Mandate > controlling faction Mandate). Prominence assessed at seizure declaration. (PP-509)
**Overwhelming:** PT +1 in target territory (consequence, not cap-governed). (PP-494, PP-508)
**Failure:** Stability −1.
**Political cost:** Casus Belli granted to controlling faction on every seizure attempt. (See §Casus Belli.) (PP-510)
**Fort Level:** Fort Level does NOT modify Seizure Ob. Seizure is a political act. (PP-506)
**Battle requirement:** If the target territory has a garrison (Fort ≥ 1 AND at least one military unit present from the controlling faction), Church must first win a Battle before Seizure proceeds. Battle uses standard rules; Fort Level adds bonus dice to defender. If Church wins: Seizure roll proceeds immediately. If Church loses: no Seizure this season; Casus Belli still granted. An ungarrisoned fortified territory (Fort ≥ 1, no units present) may be Seized without Battle. (PP-506)
**Early Seizure political visibility:**
- TC < 50: all factions observe the seizure attempt. No concealment.
- TC ≥ 50: only factions with Intel ≥ 3 in the target territory observe. (PP-507) [PROVISIONAL]
**Mandatory Assert post-TC 75:** Suspended. Assert optional only once TC freezes. (PP-511)
**[ED-355 RESOLVED — PP-506. ED-365 RESOLVED — PP-507. ED-366 RESOLVED — PP-508. ED-367 RESOLVED — PP-509. ED-368 RESOLVED — PP-506. ED-369 RESOLVED — PP-511.]**


## Theocracy Counter Starting Value — Canonical
TC starts at **28**. (P-32, PP-189 correction. The 22 value from v04 B2 was superseded by P-32 in v05.)


## TC 75 Seizure — Territorial Seizure (PP-421)
Cap: 2 territory transfers per seizure event (v04/v05 P-23). Previously set to 4 by PP-183 — reverted.


## TC 75 Seizure — Territory Values — SUPERSEDED
**See TCV table in §Victory Conditions above.** Per-territory seizure Ob = 2 + Fort Level + max(0, 3 − PT). Fort levels per geography_v30.md territory table.
[TERRITORY-DEBT: RESOLVED 2026-04-08 — PP-493. All T# references verified against geography_v30.md.]

## TC Threshold Check — Zoom In Interaction (ED-056 resolved 2026-04-03)
TC threshold check fires at turn-end regardless of Zoom In suspension.
Zoom In cannot delay TC threshold check. Clocks continue during Zoom In personal phase.


## Church TC Gain — Redesign Required (ED-110 resolved 2026-04-03)
Church must have more TC gain routes than Baralta has suppression capacity.
Baralta is one person, not a nation. Church spans multiple territories and actors.
Expand TC gain table before next BG simulation. Options under consideration: AER-linked gain, territory-hold bonuses, non-Hafenmark suppression routes.
