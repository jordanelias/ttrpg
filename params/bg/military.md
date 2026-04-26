## Unit Muster Ob Table (from v04 B8 + compilation B6)
| Unit Type | Muster Ob | Prerequisites |
|-----------|----------|---------------|
| Light Infantry | 1 | None |
| Heavy Infantry | 2 | Prosperity ≥ 5 + Wealth Ob 2 |
| Cavalry | 3 | Prosperity ≥ 6 or officer History |
| Ranged | 2 | Officer with Ranged proficiency |
| Artillery | 4 | Wealth Ob 4 + 1 season construction |
| Knights Templar | Church only | Not standard Muster |

Unit starting Discipline: Light Infantry 3, Heavy Infantry 4, Cavalry 4, Ranged 3, Artillery 3.


## BG Co-Movement Resolution Protocol (PP-182, ED-086 resolved 2026-04-03 — P-14 compliant)

**Serialization (PP-503):** When multiple Thread operations fire in the same season, resolve each operation's Co-Movement card fully (draw → apply all three dimensional effects → discard) before the next operation draws. Effects from earlier cards may alter conditions for later draws (e.g., MS threshold crossings).
[Full protocol in PP-182 section — three-dimensional auto-effects for all Thread operations]
History Resonance markers (temporal), Attention Pool (epistemic), Primary result (actualized).
Thread Tension (TT) = sum of all History Resonance markers across board.
| TT | Effect |
|----|--------|
| 0–9 | Normal |
| ≥ 10 | All Thread operation Obs +1 globally |
| ≥ 15 | Thread Wound formation triggers automatically in any territory with ≥ 2 markers |


## Drawn Battle Rule (PP-180)
Equal net successes: Stalemate. Both Discipline −1. No territorial change.
Both at Discipline 0: both units destroyed simultaneously. Territory uncontrolled.


## Ranged Faction Military Modifier (ED-087 resolved 2026-04-03)
No BG Military modifier for ranged-specialist factions. BG correctly abstracts above weapon-type level. Intentional design decision — revisit only if faction asymmetry design requires it.


## Co-Movement Card Effects — BG Reference (PP-187)
20-card deck. Draw on: Partial Community Weaving, ~~Niflhel Harvest~~ (struck per ED-764; replaced by Settlement-Broker Harvest event triggered by Intel ≥ 4 broker activity at black-market settlements), VTM preview.
| Category | Count | Effect |
|----------|-------|--------|
| CI effect | 4 | CI +1 immediately |
| MS stabilisation | 3 | MS +1 at next Accounting |
| Faction intel leak | 3 | One random faction learns Thread operation occurred here |
| Thread Debt adjacent | 3 | Thread Debt token in adjacent territory |
| History Resonance adjacent | 3 | History Resonance marker in adjacent territory |
| Benign | 4 | No mechanical effect |


## Casus Belli (PP-510)
A one-season political token granted to the controlling faction on every Church Graduated Seizure attempt (successful or not). Also granted by other actions where specified.

**When CB is granted:** receiving faction places a CB marker on their mat (colour-coded to offending faction).

**Effects (fire at next Accounting after CB granted):**
1. Free Senator Outward (Diplomacy) action targeting the offending faction this season — no card slot required.
2. Legionary actions against the offending faction this season: Ob −1 (min 1). Military action is politically legitimised.
3. All factions observe the grant (public). Any faction may invoke the CB to justify coalition this season (coalition Ob −1 while CB-holder is primary, this season only).

**CB marker removed** at next Accounting regardless of whether effects were used.

**Limit:** One CB marker per offending faction at a time. New CB from same source resets the timer.

[PROVISIONAL: Multiple simultaneous CB markers from different sources (e.g. Church CB + Crown CB on same holder) — confirm whether stacking is permitted. Default: permitted, markers are distinct per source.]



### Battle Ob Formula (PP-499, ED-343 resolved)
**Battle Ob = floor(defender Military / 2) + 1.**
Attacker rolls: Military pool vs Ob. Degree table per standard BG degree table (PP-249).
**[PROVISIONAL ED-316] Weight-of-numbers (PP-570):** A faction attacking with Military ≥ 2× defending faction Military forces the defender to Stability −1 at Accounting regardless of battle outcome (the sheer scale is demoralising). Applies once per Accounting regardless of attack count.
[Resolved by PP-548. Battle Ob = floor(defender Military / 2) + 1. Min 1 prevents auto-success vs Military 0 factions (RM). Flagged for simulation confirmation.]




## Battle Resolution — Formal Outcome Table (PP-476)
Both attacker and defender apply their own degree result independently.
For each side: margin = (own net − opponent net), if positive; 0 if own net ≤ opponent net.
Apply: margin 0 → no outcome for that side; margin 1 to Ob−1 → Discipline −2 on opponent unit;
margin = Ob → Discipline −4 on opponent unit; margin > Ob → opponent unit destroyed.
Drawn battle (equal net): no degree for either side; both Discipline −1.

Discipline floor: 0. Any result pushing Discipline to ≤ 0 destroys the unit.
Multi-unit territory: one roll per faction using Military stat pool. Player assigns Discipline loss to specific unit card of their choice.
Unit removed (by stat cap reduction): returned to reserve with Discipline reset on next Muster.


## Fortify — Pool Stat (ED-338 provisional)
[PROVISIONAL: Fortify uses Military stat pool. Confirmation pending.]


## Casus Belli — Stacking Cap and Consumption (PP-519)
- **Stacking cap:** Maximum 1 active Casus Belli against any single target at a time. A second CB vs the same target replaces the first. A faction may hold CBs vs multiple different targets simultaneously (no cross-target cap).
- **Consumption:** A Casus Belli grants −1 Ob to one declared Military action against the target. Consumed when that Military roll is made. Treaty-derived CBs (permanent until used, per PP-510) follow the same consumption rule.
- **CB declaration timing:** Declared at Phase 4 start (before resolution, after cards played). Cannot be transferred to a different action once declared.


## Conflict Marker — Church + Hafenmark Partition (PP-479)
Conflict Marker: flip token on Church or Hafenmark mat. Placed when either faction plays Legionary targeting the other's territory. Removed at second Accounting after placement.
"No active military conflict" condition for Partition co-victory = no Conflict Marker active on either mat.
