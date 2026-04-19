## Faction Unique Actions — Board Game (PP-428–442, 2026-04-07)
<!-- PATCHES APPLIED: PP-428–442 + PP-431-COR + PP-441-COR -->
<!-- Status: applied -->

### Church — Piety Spread (PP-428)
**Type:** Consul Inward (Church only). **Prerequisite:** AP ≥ 1.
Roll: Mandate vs Ob = floor(controlling faction Mandate / 2) + 1 + Fort Level.
Doctrine-aligned territory: −1 Ob.
**Post-CI 75:** Range-limited to adjacent territories only.

| Degree | Effect |
|--------|--------|
| Overwhelming | PT +1 in territory + AP +1 |
| Success | PT +1 in territory |
| Partial | AP +1 |
| Failure | Stability −1 |

---

### Church — Active Inquisition (PP-429)
**Type:** Senator Inward (Church only).
Roll: Mandate vs Ob = floor(territory Stability / 2) + 1.
**First Inquisitor threshold:** AP ≥ 3 (ED-322 confirmed). Second: AP ≥ 6.

| Degree | Effect |
|--------|--------|
| Overwhelming | AP +3 + immediate Inquisitor deployment if at threshold |
| Success | AP +2 |
| Partial | AP +1 |
| Failure | AP −1 + Stability −1 |

**Sustained AP (≥ 8 sustained across Accounting):** Territory Stability −1 at Accounting.

---

### Church — Cardinal Focus (PP-430)
**Timing:** Phase 1 declarative. No cost. Once per season.
Designate one Cardinal as Focused:

| Cardinal | Focus Effect |
|----------|--------------|
| Fortitude | Templar deploys without Legionary card this season |
| Justice | AP threshold for first Inquisitor −1 this season |
| Prudence | Wealth +1 (integer) this season |
| Temperance | AER +1 this season |

**Schism interaction:** Schisming Cardinal ignores Focus. Focus has no effect if the designated Cardinal is in schism this season.

---

### Hafenmark — Parliamentary Challenge (PP-431 + PP-431-COR)
**Type:** Senator Inward (Hafenmark only). **Once per season.**
Roll: Mandate vs Ob 2 (−1 Ob if PI ≥ 5 → Ob 1 minimum).

**PP-431-COR:** In any season Hafenmark plays Parliamentary Challenge, structural CI suppression (Baralta's Mandate ≥ 4 automatic −1/season) does NOT fire. Challenge replaces structural — the replacement triggers on card play regardless of roll outcome.

| Degree | Effect |
|--------|--------|
| Overwhelming | CI −2 + Church must Uphold or Appease |
| Success | CI −1 |
| Partial | Stability −1 |
| Failure | Stability −1 + Church Mandate +1 |

---

### Hafenmark — Parliamentary Session (PP-432)
**Type:** Senator Outward (Hafenmark only). **Once per arc.**
All factions vote (Support / Oppose / Abstain). Ministry vote = Support if AP-token in T1.
Blocking factions generate Resentment tokens per PP-405.

| Outcome | Effect |
|---------|--------|
| Majority Support | PI +1 + Hafenmark Mandate +1 |
| Majority Oppose | Hafenmark Stability −1 |
| Tie | CI +1 (institutional paralysis) |

**Diplomatic Token interaction (PP-320-ED):** Each active Diplomatic Token on a faction mat counts that faction as Support regardless of declared vote.

---

### Hafenmark — Diplomat Card (ED-320 RESOLVED)
**Type:** Senator Outward. **Card type:** Hafenmark faction card. **Once per season.**
Roll: Influence vs Ob = floor(target Mandate / 2) + 1.
**Restriction:** Cannot target Church if PI < 3.

| Degree | Effect |
|--------|--------|
| Overwhelming | Place 1 Diplomatic Token on target mat + target Stability +1 + PI +1. Target faction's actions against Hafenmark: +1 Ob this season and next. |
| Success | Place 1 Diplomatic Token on target mat + PI +1 |
| Partial | PI +1 (no Token) |
| Failure | Hafenmark Stability −1 |

**Diplomatic Token (PP-517/521):** Permanent marker on target faction mat. Removed on: (a) military conflict with Hafenmark — any season either faction plays Legionary targeting the other's held territory (intent of play; March to uncontested territory excluded); (b) target faction elimination; (c) Formal Crown Treaty formed with the token-holding faction (PP-521). Maximum 1 per faction mat. Public. Token effects: target faction counts as Support in Parliamentary Sessions. Token effect suspended while token-holding faction is in submitted (vassal) state or has Mandate 0 from submission. (PP-555 / ED-373)

---

### Crown — Royal Charter (PP-433)
**Type:** Consul Inward (Crown only).
Roll: Mandate vs Ob = floor(territory Prosperity / 2) + 1. Virtue Ethics: −1 Ob.
**Limit:** Max floor(Mandate / 2) + 1 active Charters simultaneously.

Success: Territory becomes Crown Charter Territory:
- All factions: Govern/Trade −1 Ob
- Church Seizure: +1 Ob
- Crown own actions: −2 Ob
Charter dissolves on control transfer.

---

### Crown — Royal Decree Enhancement (PP-435)
**Type:** Special/Unique Power. Ob 2. Once per season (existing mechanic).
**Enhancement (Overwhelming only — net ≥ 2×Ob AND ≥ 3):**
Choose one:
(a) Stat ±2 to one faction
(b) Stat ±1 to two different factions
(c) Stat ±1 to one faction AND suspend one threshold effect for one season

Success (unchanged): Stat ±1 to one faction. Consecutive: +1 Ob/season.
Cannot target Intel.

---

### Crown — Thread Liaison (PP-436)
**Timing:** Phase 1 declarative. No roll.
Crown designates one allied faction. Liaison's Thread operations in Crown-held territories count toward Crown's co-victory RS threshold tracking.
**Allied definition:** Active Treaty partner OR same-side Parliamentary Session voter OR common Resentment target.

**Thread Liaison 'Allied' scope (PP-520):** For Thread Liaison designation only, 'Allied' = Active Crown Treaty partner. Parliamentary voter and Resentment conditions do not qualify for Liaison designation.
**Dissolves on:** Military conflict between Crown and Liaison.
**Dissolution timing (ED-372):** Prospective only. Thread operations already credited before dissolution remain valid. Future operations after dissolution provide no Liaison benefit.

---

### Crown — Diplomatic Outreach to Schoenland (PP-437)
**Type:** Senator Outward (Crown only). Cannot use same season as Formal Crown Treaty.
Roll: Influence vs Ob = current AER level, min 1. Virtue Ethics: −1 Ob.
**Fragmentation modifier:** +1 Ob if 3+ factions have Stability ≤ 2. *(PP-562: was +2 — punished Crown most when Decree most needed)*

| Degree | Effect |
|--------|--------|
| Overwhelming | IP −2 + AER +1 |
| Success | IP −1 + AER +0.5 |
| Partial | AER +0.5 |
| Failure | AER −0.5 |

---

### Varfell — VTM Discretion (PP-438)
**Type:** Accounting action. **At VTM 3+.**
Spend 1 Patience Counter at Accounting to suppress VTM CI contribution for that season.
**VTM CI contribution (PP-563):** Once VTM is publicly visible (VTM 3+), it generates Church institutional pressure: VTM 3 = +0.5 CI/season; VTM 4 = +1 CI/season; VTM 5 = +1.5 CI/season (applied at Accounting, rounded to nearest 0.5, tracking half-CI fractionally). Matches "low"/"high" labels in Discretion cost text.
**Cooldown:** Once per 2 consecutive seasons (Discretion Cooldown marker, cleared at Year-End).
Does not suppress other CI sources.

**Cost:** 0 PC at VTM 3 (cooldown-only gate; CI contribution is low). 1 PC at VTM 4+ (CI contribution is high; cost is proportional). (ED-323 resolved 2026-04-08.)

---

### Varfell — Revelation Tokens / Path A (PP-439)
**Full reveal criteria:** Overwhelming result on Tribune Investigate OR 4 consecutive PC Spy successes.
On full reveal: place Revelation Token on target faction mat (public, permanent).
**Path A condition:** Two Revelation Tokens on two different rival faction mats = "fully revealed" condition met.
Target faction knows they've been revealed (public token).

---

### Varfell — Ethical Framework (PP-440)
**Consequentialism −1 Ob applies to:**
- Tribune Intel actions (Investigate, Spy, VTM-building, Counter-Narrative)

**+1 Ob penalty applies to:**
- Public ideological campaigns
- Open diplomatic commitments
- Relationship investments with no Intel yield

---

### Varfell — Counter-Narrative (PP-441 + PP-441-COR)
**Type:** Tribune Outward (Varfell only). Target = Church-held or Church-prominent territory.
Church-prominent = Church global Mandate > controlling faction global Mandate (assessed at action declaration).
Roll: Intel vs Ob = floor(Church Mandate / 2) + 1. Consequentialism: −1 Ob.
**+2 Ob modifier:** If territory has an active Inquisitor (applies to all Tribune Intel actions).

| Degree | Effect |
|--------|--------|
| Overwhelming | CI −0.5 + AP +2 in territory |
| Success | AP +2 in territory |
| Partial | AP +1 |
| Failure | Intel network exposed: Church notified of Varfell presence, AP +1 tagged as Varfell (+2 Ob to Counter-Narrative in this territory next season) |

**CI tracking:** Fractional CI values accumulate. Track running decimal on CI track. Round to integer for threshold checks only.
**AP note (ED-325):** AP is tracked per-territory (PP-185). Counter-Narrative AP in a territory contributes to that territory's AP pool, not a global pool. Inquisitor deploys in the territory where threshold is crossed.

---

### Counter-Intelligence Postures (PP-442)
All three are passive faction abilities (no card required, no roll):

**Crown — Royal Guard** (Phase 4, Priority 1 — fires before all other Phase 4 actions):
Once per season, cancel one successful Intel action targeting Crown. No card cost.

**Hafenmark — Procedural Objection:**
On any Varfell Tribune Investigate success, Hafenmark may declare Procedural Objection. Cost: consumes Parliamentary Challenge use for this season (if Challenge already used: cannot declare Objection). Effect: if Hafenmark Mandate ≥ 4, revealed stat is replaced with a false value for all non-Varfell observers. Varfell sees true value; others see false.

**Church — Sanctuary Extension:**
Existing Sanctuary card: extended to also block Varfell 4-PC Spy action once per season (in addition to existing Sanctuary effects).

---


### Church — Piety Spread (PP-428)
**Type:** Consul Inward (Church only). **Prerequisite:** AP ≥ 1.
Roll: Mandate vs Ob = floor(controlling faction Mandate / 2) + 1 + Fort Level.
Doctrine-aligned territory: −1 Ob.
**Post-CI 75:** Range-limited to adjacent territories only.

| Degree | Effect |
|--------|--------|
| Overwhelming | PT +1 in territory + AP +1 |
| Success | PT +1 in territory |
| Partial | AP +1 |
| Failure | Stability −1 |

---


### Church — Active Inquisition (PP-429)
**Type:** Senator Inward (Church only).
Roll: Mandate vs Ob = floor(territory Stability / 2) + 1.
**First Inquisitor threshold:** AP ≥ 3 (ED-322 confirmed). Second: AP ≥ 6.

| Degree | Effect |
|--------|--------|
| Overwhelming | AP +3 + immediate Inquisitor deployment if at threshold |
| Success | AP +2 |
| Partial | AP +1 |
| Failure | AP −1 + Stability −1 |

**Sustained AP (≥ 8 sustained across Accounting):** Territory Stability −1 at Accounting.

---


### Church — Cardinal Focus (PP-430)
**Timing:** Phase 1 declarative. No cost. Once per season.
Designate one Cardinal as Focused:

| Cardinal | Focus Effect |
|----------|--------------|
| Fortitude | Templar deploys without Legionary card this season |
| Justice | AP threshold for first Inquisitor −1 this season |
| Prudence | Wealth +1 (integer) this season |
| Temperance | AER +1 this season |

**Schism interaction:** Schisming Cardinal ignores Focus. Focus has no effect if the designated Cardinal is in schism this season.

---


### Hafenmark — Parliamentary Challenge (PP-431 + PP-431-COR)
**Type:** Senator Inward (Hafenmark only). **Once per season.**
Roll: Mandate vs Ob 2 (−1 Ob if PI ≥ 5 → Ob 1 minimum).

**PP-431-COR:** In any season Hafenmark plays Parliamentary Challenge, structural CI suppression (Baralta's Mandate ≥ 4 automatic −1/season) does NOT fire. Challenge replaces structural — the replacement triggers on card play regardless of roll outcome.

| Degree | Effect |
|--------|--------|
| Overwhelming | CI −2 + Church must Uphold or Appease |
| Success | CI −1 |
| Partial | Stability −1 |
| Failure | Stability −1 + Church Mandate +1 |

---


### Hafenmark — Parliamentary Session (PP-432)
**Type:** Senator Outward (Hafenmark only). **Once per arc.**
All factions vote (Support / Oppose / Abstain). Ministry vote = Support if AP-token in T1.
Blocking factions generate Resentment tokens per PP-405.

| Outcome | Effect |
|---------|--------|
| Majority Support | PI +1 + Hafenmark Mandate +1 |
| Majority Oppose | Hafenmark Stability −1 |
| Tie | CI +1 (institutional paralysis) |

**Diplomatic Token interaction (PP-320-ED):** Each active Diplomatic Token on a faction mat counts that faction as Support regardless of declared vote.

---


### Hafenmark — Diplomat Card (ED-320 RESOLVED)
**Type:** Senator Outward. **Card type:** Hafenmark faction card. **Once per season.**
Roll: Influence vs Ob = floor(target Mandate / 2) + 1.
**Restriction:** Cannot target Church if PI < 3.

| Degree | Effect |
|--------|--------|
| Overwhelming | Place 1 Diplomatic Token on target mat + target Stability +1 + PI +1. Target faction's actions against Hafenmark: +1 Ob this season and next. |
| Success | Place 1 Diplomatic Token on target mat + PI +1 |
| Partial | PI +1 (no Token) |
| Failure | Hafenmark Stability −1 |

**Diplomatic Token (PP-517/521):** Permanent marker on target faction mat. Removed on: (a) military conflict with Hafenmark — any season either faction plays Legionary targeting the other's held territory (intent of play; March to uncontested territory excluded); (b) target faction elimination; (c) Formal Crown Treaty formed with the token-holding faction (PP-521). Maximum 1 per faction mat. Public. Token effects: target faction counts as Support in Parliamentary Sessions. Token effect suspended while token-holding faction is in submitted (vassal) state or has Mandate 0 from submission. (PP-555 / ED-373)

---


### Crown — Royal Charter (PP-433)
**Type:** Consul Inward (Crown only).
Roll: Mandate vs Ob = floor(territory Prosperity / 2) + 1. Virtue Ethics: −1 Ob.
**Limit:** Max floor(Mandate / 2) + 1 active Charters simultaneously.

Success: Territory becomes Crown Charter Territory:
- All factions: Govern/Trade −1 Ob
- Church Seizure: +1 Ob
- Crown own actions: −2 Ob
Charter dissolves on control transfer.

---


### Crown — Royal Decree Enhancement (PP-435)
**Type:** Special/Unique Power. Ob 2. Once per season (existing mechanic).
**Enhancement (Overwhelming only — net ≥ 2×Ob AND ≥ 3):**
Choose one:
(a) Stat ±2 to one faction
(b) Stat ±1 to two different factions
(c) Stat ±1 to one faction AND suspend one threshold effect for one season

Success (unchanged): Stat ±1 to one faction. Consecutive: +1 Ob/season.
Cannot target Intel.

---


### Crown — Thread Liaison (PP-436)
**Timing:** Phase 1 declarative. No roll.
Crown designates one allied faction. Liaison's Thread operations in Crown-held territories count toward Crown's co-victory RS threshold tracking.
**Allied definition:** Active Treaty partner OR same-side Parliamentary Session voter OR common Resentment target.

**Thread Liaison 'Allied' scope (PP-520):** For Thread Liaison designation only, 'Allied' = Active Crown Treaty partner. Parliamentary voter and Resentment conditions do not qualify for Liaison designation.
**Dissolves on:** Military conflict between Crown and Liaison.
**Dissolution timing (ED-372):** Prospective only. Thread operations already credited before dissolution remain valid. Future operations after dissolution provide no Liaison benefit.

---


### Crown — Diplomatic Outreach to Schoenland (PP-437)
**Type:** Senator Outward (Crown only). Cannot use same season as Formal Crown Treaty.
Roll: Influence vs Ob = current AER level, min 1. Virtue Ethics: −1 Ob.
**Fragmentation modifier:** +1 Ob if 3+ factions have Stability ≤ 2. *(PP-562: was +2 — punished Crown most when Decree most needed)*

| Degree | Effect |
|--------|--------|
| Overwhelming | IP −2 + AER +1 |
| Success | IP −1 + AER +0.5 |
| Partial | AER +0.5 |
| Failure | AER −0.5 |

---


### Varfell — VTM Discretion (PP-438)
**Type:** Accounting action. **At VTM 3+.**
Spend 1 Patience Counter at Accounting to suppress VTM CI contribution for that season.
**VTM CI contribution (PP-563):** Once VTM is publicly visible (VTM 3+), it generates Church institutional pressure: VTM 3 = +0.5 CI/season; VTM 4 = +1 CI/season; VTM 5 = +1.5 CI/season (applied at Accounting, rounded to nearest 0.5, tracking half-CI fractionally). Matches "low"/"high" labels in Discretion cost text.
**Cooldown:** Once per 2 consecutive seasons (Discretion Cooldown marker, cleared at Year-End).
Does not suppress other CI sources.

**Cost:** 0 PC at VTM 3 (cooldown-only gate; CI contribution is low). 1 PC at VTM 4+ (CI contribution is high; cost is proportional). (ED-323 resolved 2026-04-08.)

---


### Varfell — Revelation Tokens / Path A (PP-439)
**Full reveal criteria:** Overwhelming result on Tribune Investigate OR 4 consecutive PC Spy successes.
On full reveal: place Revelation Token on target faction mat (public, permanent).
**Path A condition:** Two Revelation Tokens on two different rival faction mats = "fully revealed" condition met.
Target faction knows they've been revealed (public token).

---


### Varfell — Ethical Framework (PP-440)
**Consequentialism −1 Ob applies to:**
- Tribune Intel actions (Investigate, Spy, VTM-building, Counter-Narrative)

**+1 Ob penalty applies to:**
- Public ideological campaigns
- Open diplomatic commitments
- Relationship investments with no Intel yield

---


### Varfell — Counter-Narrative (PP-441 + PP-441-COR)
**Type:** Tribune Outward (Varfell only). Target = Church-held or Church-prominent territory.
Church-prominent = Church global Mandate > controlling faction global Mandate (assessed at action declaration).
Roll: Intel vs Ob = floor(Church Mandate / 2) + 1. Consequentialism: −1 Ob.
**+2 Ob modifier:** If territory has an active Inquisitor (applies to all Tribune Intel actions).

| Degree | Effect |
|--------|--------|
| Overwhelming | CI −0.5 + AP +2 in territory |
| Success | AP +2 in territory |
| Partial | AP +1 |
| Failure | Intel network exposed: Church notified of Varfell presence, AP +1 tagged as Varfell (+2 Ob to Counter-Narrative in this territory next season) |

**CI tracking:** Fractional CI values accumulate. Track running decimal on CI track. Round to integer for threshold checks only.
**AP note (ED-325):** AP is tracked per-territory (PP-185). Counter-Narrative AP in a territory contributes to that territory's AP pool, not a global pool. Inquisitor deploys in the territory where threshold is crossed.

---


### Counter-Intelligence Postures (PP-442)
All three are passive faction abilities (no card required, no roll):

**Crown — Royal Guard** (Phase 4, Priority 1 — fires before all other Phase 4 actions):
Once per season, cancel one successful Intel action targeting Crown. No card cost.

**Hafenmark — Procedural Objection:**
On any Varfell Tribune Investigate success, Hafenmark may declare Procedural Objection. Cost: consumes Parliamentary Challenge use for this season (if Challenge already used: cannot declare Objection). Effect: if Hafenmark Mandate ≥ 4, revealed stat is replaced with a false value for all non-Varfell observers. Varfell sees true value; others see false.

**Church — Sanctuary Extension:**
Existing Sanctuary card: extended to also block Varfell 4-PC Spy action once per season (in addition to existing Sanctuary effects).

---

---

## Dynastic Proclamation (Hafenmark only) — PP-649, peninsular_strain_v30.md §5.3

**Card:** Diplomat (Hafenmark faction card). Once per season.
**Pool:** Influence.
**Ob:** floor(target faction Stability / 2) + 1. +1 Ob if target territory PT ≤ 1. −1 Ob if Diplomatic Token on target faction.
**Prerequisites:** Hafenmark Mandate ≥ 4. Hafenmark Mandate > target controller Mandate. Target adjacent to Hafenmark territory.

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory transfers. Accord 2. Target Mandate −1. Hafenmark Mandate +1. +1 Standing. No CB. |
| Success | Territory transfers. Accord 2. Target Mandate −1. |
| Partial | No transfer. Hafenmark gains CB vs target. Target territory Accord −1. |
| Failure | Hafenmark Stability −1. |

**Defensive:** Target may invoke Institutional Mandate (PP-189) if Mandate ≥ 4 to cancel.

---

## Cultural Reformation (Varfell only) — PP-650, peninsular_strain_v30.md §5.4

**Card:** Colonist. Once per season.
**Pool:** Influence + floor(VTM / 2).
**Ob:** PT + 1 (target territory). PT 0 → Ob 1. PT 3 → Ob 4. PT 5 → Ob 6.
**Prerequisites:** VTM ≥ 2. Target PT ≤ 3. Target adjacent to Varfell territory OR has Varfell intelligence presence.

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory transfers. Accord 2. PT −1 in target. CI −1. |
| Success | Territory transfers. Accord 2. PT −1. |
| Partial | No transfer. PT −1 (cultural seed). Varfell gains intelligence presence. |
| Failure | Varfell Stability −1. CI +1. Church Attention Pool +1. |

**Anti-Altonian:** Territories gained via Reformation: Altonian intel ops +1 Ob.
**Defensive:** Target may invoke Institutional Mandate (PP-189). Church Counter-Reformation: if Church Prominent in target AND plays Senator same Phase 4, +1 Ob to Reformation.

---

## Martial Governance (Löwenritter only) — PP-653, peninsular_strain_v30.md §2.6

**Card:** Legionary (Govern variant).
**Pool:** Military (not Influence).
**Ob:** floor(Prosperity / 2) + 2 (harder than standard Govern).
**Effect:** Accord +1 on Success (cap 2 via Martial Governance — Accord 3 requires standard Govern with Influence).
