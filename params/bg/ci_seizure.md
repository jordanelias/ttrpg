## CI Generation — Seasonal (canonical: military_layer_v30 §3, tc_political_redesign_v30 §§1–3)
**Starting CI: 28. CI runs to 100 (no freeze). Milestone system: see victory_v30 §7.**

Seasonal CI at Accounting (execute in order, per military_layer_v30 §3):
1. **Conditional Passive (§3.2):** CI +1 only if Church L > controlling faction L in ≥ 2 territories.
2. **Piety Yield (§3.3):** CI += Σ(PT tier × SW/5) per prominent territory, floored. SW = Spiritual Weight per territory (tc_political_redesign_v30 §1).
3. **Charity Advantage (§3.4):** Church Wealth spent on charity → CI +1 per 2 Wealth, cap 2/season.
4. **Templar Presence (§3.5):** +1 CI per territory with Church military unit AND Church Prominence.
5. **Assert (§3.6):** Optional Church action. Influence vs Ob 2. Success: CI +1. Failure: Stability −1.
6. **Suppress (§3.7):** Optional opponent action. L vs Ob = floor(Church L / 2) + 1. Success: negate Step 1. Failure: Stability −1.
7. **Hafenmark Structural Suppression (§3.8):** While Baralta L ≥ 4, CI −1/season.

**CI seasonal cap (PP-504):** ±3 per season from player-initiated Domain Actions. ±5 per season from all sources combined (includes Conditional Passive, Piety Yield, Calamity Drift, event cards).

Legacy CI sources (AER momentum, Attention Pool threshold, Emergency Powers, Free Trade Decree, Church unit presence) are subsumed into the Piety Yield system — Church prominence in high-PT territories captures the same dynamics. AER ≥ 3 still bypasses Hafenmark structural suppression (PP-203).


## Faction Political Pool (tc_political_redesign_v30 §3.4)
**Church:** Political pool = L + floor(CI/20).
**Non-Church (anti-Church motions):** Political pool = L − floor(CI/30).
**Non-Church (non-Church motions):** Political pool = L (no CI modifier).
CI creates asymmetric legitimacy: Church gains political bonus proportional to CI; opponents pay a legitimacy cost proportional to CI when directly opposing Church.


## Church Mass Seizure (one-shot — per victory_v30.md §3.2, §7)
**CI ≥ 60 makes Mass Seizure available. One-time event. Declaration probability per season: P = ((CI−60)/40)^3.3 — 1% at CI 70, 10% at CI 80, 39% at CI 90, 100% at CI 100. Exponential shape models institutional restraint. CI runs to 100 (no freeze).**

**Pre-Seizure accumulation path (PP-TBD):** Bishop Appointment (faction_actions.md, Church — Ecclesiastical Appointment) is the settlement-level precursor to Mass Seizure. Church accumulates governance of individual settlements via bishop-governor installation before CI 60+ triggers the formal peninsula-wide political formalization. Mass Seizure converts accumulated settlement-level Church governance into recognized territorial control.

### Seizure Ob
Ob = 10 − PT − infrastructure modifiers (floor 1). See victory_v30 §3.2 for infrastructure table.
Prominence required: Church L > controlling faction's L in target territory.
Church L ≥ 4 required to attempt seizure.

### Seizure Results
Per victory_v30.md §7. Overwhelming seizure: PT +1 in target territory. This is a consequence effect — NOT subject to the ±1 PT seasonal cap. State-change consequences from seizure are exempt from action caps. (PP-502)

### Seizure Constraints
One seizure attempt per season. Cannot target T15 (Askeheim) or T16 (Schoenland).

### Church Mass Seizure (one-shot, replaces PP-494)
**Available:** CI ≥ 60. Declaration probability per season: P = ((CI−60)/40)^3.3, clamped [0,1]. 1% at CI 70, 10% at CI 80, 100% at CI 100. One attempt only. (Replaces Graduated Seizure PP-494.)
**Pool:** Influence + floor(CI / 15). At CI 60: 10D. At CI 100: 12D.
**Ob:** 10 − PT − infrastructure modifiers (floor 1). PT 5 with full infra = Ob 1. PT 0 no infra = Ob 10.

| PT | Seizure Ob |
|----|-----------|
| 5 (Piety) | 2 |
| 4 | 6 (before infra) |
| 3 | 7 (before infra) |
| 2 | 8 (before infra) |
| 1 | 9 (before infra) |
| 0 (Restoration) | 7 |

**Prerequisites:** Church L ≥ 4. Prominence (Church L > controlling faction L). Prominence assessed at seizure declaration. (PP-509)
**Overwhelming:** PT +1 in target territory (consequence, not cap-governed). (PP-494, PP-508)
**Failure:** Stability −1.
**Political cost:** Casus Belli granted to controlling faction on every seizure attempt. (See §Casus Belli.) (PP-510)
**Fort Level:** Fort Level does NOT modify Seizure Ob. Seizure is a political act. (PP-506)
**Battle requirement:** If the target territory has a garrison (Fort ≥ 1 AND at least one military unit present from the controlling faction), Church must first win a Battle before Seizure proceeds. Battle uses standard rules; Fort Level adds bonus dice to defender. If Church wins: Seizure roll proceeds immediately. If Church loses: no Seizure this season; Casus Belli still granted. An ungarrisoned fortified territory (Fort ≥ 1, no units present) may be Seized without Battle. (PP-506)
**Early Seizure political visibility:**
- CI < 50: all factions observe the seizure attempt. No concealment.
- CI ≥ 50: only factions with Intel ≥ 3 in the target territory observe. (PP-507) [PROVISIONAL]
**Mandatory Assert post-CI 75:** Suspended. Assert optional only once CI caps. (PP-511)
**[ED-355 RESOLVED — PP-506. ED-365 RESOLVED — PP-507. ED-366 RESOLVED — PP-508. ED-367 RESOLVED — PP-509. ED-368 RESOLVED — PP-506. ED-369 RESOLVED — PP-511.]**

### Battle Ob Formula (PP-499, ED-343 resolved)
**Battle Ob = floor(defender Military / 2) + 1.**
Attacker rolls: Military pool vs Ob. Degree table per standard BG degree table (PP-249).
**[PROVISIONAL ED-316] Weight-of-numbers (PP-570):** A faction attacking with Military ≥ 2× defending faction Military forces the defender to Stability −1 at Accounting regardless of battle outcome (the sheer scale is demoralising). Applies once per Accounting regardless of attack count.
[Resolved by PP-548. Battle Ob = floor(defender Military / 2) + 1. Min 1 prevents auto-success vs Military 0 factions (RM). Flagged for simulation confirmation.]




**Pre-Seizure accumulation path (PP-TBD):** Bishop Appointment (faction_actions.md, Church — Ecclesiastical Appointment) is the settlement-level precursor to Mass Seizure. Church accumulates governance of individual settlements via bishop-governor installation before CI 60+ triggers the formal peninsula-wide political formalization. Mass Seizure converts accumulated settlement-level Church governance into recognized territorial control.

### Seizure Ob
Ob = 10 − PT − infrastructure modifiers (floor 1). See victory_v30 §3.2 for infrastructure table.
Prominence required: Church L > controlling faction's L in target territory.
Church L ≥ 4 required to attempt seizure.


### Seizure Results
Per victory_v30.md §7. Overwhelming seizure: PT +1 in target territory. This is a consequence effect — NOT subject to the ±1 PT seasonal cap. State-change consequences from seizure are exempt from action caps. (PP-502)


### Seizure Constraints
One seizure attempt per season. Cannot target T15 (Askeheim) or T16 (Schoenland).


### Church Mass Seizure (one-shot, replaces PP-494)
**Available:** CI ≥ 60. Declaration probability per season: P = ((CI−60)/40)^3.3, clamped [0,1]. 1% at CI 70, 10% at CI 80, 100% at CI 100. One attempt only. (Replaces Graduated Seizure PP-494.)
**Pool:** Influence + floor(CI / 15). At CI 60: 10D. At CI 100: 12D.
**Ob:** 10 − PT − infrastructure modifiers (floor 1). PT 5 with full infra = Ob 1. PT 0 no infra = Ob 10.

| PT | Seizure Ob |
|----|-----------|
| 5 (Piety) | 2 |
| 4 | 6 (before infra) |
| 3 | 7 (before infra) |
| 2 | 8 (before infra) |
| 1 | 9 (before infra) |
| 0 (Restoration) | 7 |

**Prerequisites:** Church L ≥ 4. Prominence (Church L > controlling faction L). Prominence assessed at seizure declaration. (PP-509)
**Overwhelming:** PT +1 in target territory (consequence, not cap-governed). (PP-494, PP-508)
**Failure:** Stability −1.
**Political cost:** Casus Belli granted to controlling faction on every seizure attempt. (See §Casus Belli.) (PP-510)
**Fort Level:** Fort Level does NOT modify Seizure Ob. Seizure is a political act. (PP-506)
**Battle requirement:** If the target territory has a garrison (Fort ≥ 1 AND at least one military unit present from the controlling faction), Church must first win a Battle before Seizure proceeds. Battle uses standard rules; Fort Level adds bonus dice to defender. If Church wins: Seizure roll proceeds immediately. If Church loses: no Seizure this season; Casus Belli still granted. An ungarrisoned fortified territory (Fort ≥ 1, no units present) may be Seized without Battle. (PP-506)
**Early Seizure political visibility:**
- CI < 50: all factions observe the seizure attempt. No concealment.
- CI ≥ 50: only factions with Intel ≥ 3 in the target territory observe. (PP-507) [PROVISIONAL]
**Mandatory Assert post-CI 75:** Suspended. Assert optional only once CI caps. (PP-511)
**[ED-355 RESOLVED — PP-506. ED-365 RESOLVED — PP-507. ED-366 RESOLVED — PP-508. ED-367 RESOLVED — PP-509. ED-368 RESOLVED — PP-506. ED-369 RESOLVED — PP-511.]**


## Church Influence Starting Value — Canonical
CI starts at **28**. (P-32, PP-189 correction. The 22 value from v04 B2 was superseded by P-32 in v05.)


## CI 75 Seizure — Territorial Seizure (PP-421)
Cap: 2 territory transfers per seizure event (v04/v05 P-23). Previously set to 4 by PP-183 — reverted.


## CI 75 Seizure — Territory Values — SUPERSEDED
**See TCV table in §Victory Conditions above.** Per-territory seizure Ob = 10 − PT − infrastructure modifiers (floor 1). See victory_v30 §3.2 for infrastructure table. Fort levels per geography_v30.md territory table.
[TERRITORY-DEBT: RESOLVED 2026-04-08 — PP-493. All T# references verified against geography_v30.md.]

## CI Threshold Check — Zoom In Interaction (ED-056 resolved 2026-04-03)
CI threshold check fires at turn-end regardless of Zoom In suspension.
Zoom In cannot delay CI threshold check. Clocks continue during Zoom In personal phase.


## Church CI Gain — Redesign Required (ED-110 resolved 2026-04-03)
Church must have more CI gain routes than Baralta has suppression capacity.
Baralta is one person, not a nation. Church spans multiple territories and actors.
Expand CI gain table before next BG simulation. Options under consideration: AER-linked gain, territory-hold bonuses, non-Hafenmark suppression routes.
