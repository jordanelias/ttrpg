## Ministry — NPC Faction (PP-193)
### Ethical Framework: Procedural Consequentialism
The Ministry evaluates actions by whether they preserve the procedural conditions for governance. It is not loyal to Crown, Church, or Hafenmark — it is loyal to the functioning of the state itself. It is the civil service: clerks, administrators, record-keepers, tax collectors, enforcement officers.

**Ministry is always NPC-controlled.** It has no player victory condition and cannot be captured by any faction's card play.

### Ministry Stats
| Stat | Value | Notes |
|------|-------|-------|
| Mandate | 3 | Institutional legitimacy of the administrative apparatus |
| Influence | 4 | Reach into all territories via clerks and administrators |
| Wealth | 2 | State treasury access (limited — Crown controls the purse) |
| Military | 0 | Ministry has no military capacity |
| Stability | 5 | The civil service is hard to destroy |

### Ministry Tokens
Ministry maintains **Administrative Presence** tokens (AP-tokens, not to be confused with Attention Pool).
One AP-token per territory in which Ministry has clerks active. Starts with AP-tokens in T14 (Ehrenfeld), T2 (Kronmark), T5 (Feldmark), T1 (Valorsplatz). These represent the administrative apparatus of Parliamentary governance. (PP-204 corrected.)

### Parliament Connection — Direct Mechanics
Ministry is the mechanical engine behind Parliament Integrity (PI).

**Ministry Stabilisation (fires at Accounting Step 11, before Hollow Victory totals):**
Each season Ministry has an AP-token in T1 (Valorsplatz, Parliament seat): PI degradation from Crown Emergency Powers is reduced by 1 (to a minimum of −0 — i.e. Ministry can prevent one Emergency Powers PI loss per season). This represents clerks managing the parliamentary record and maintaining continuity despite political disruption.

**Ministry Legislative Record:**
At each Year-End Accounting: Ministry produces a Legislative Record for the prior year. Any Parliamentary Manoeuvre that succeeded (Hafenmark) this year is recorded as a Parliamentary Ruling. Effect: the first time each year a Parliamentary Ruling is recorded, PI +1 (the institution acknowledges the precedent). This is in addition to the standard Hafenmark Parliamentary Manoeuvre PI recovery.

**Ministry and Crown Policy:**
Crown Policy Instruments require Ministry countersignature. If Ministry Mandate < 2 (collapsed or compromised): Crown Policy actions cost +1 Ob (the administrative apparatus is too compromised to implement the decree cleanly). If Ministry Mandate = 0: Crown Policy actions unavailable until Ministry Mandate recovers.

**Ministry and Church Seizure (CI 75):**
Church Territorial Seizure of T1 (Valorsplatz) requires removing the Ministry AP-token first. If AP-token present: seizure Ob +1 (the administrative apparatus resists institutional capture). If seizure succeeds despite the token: Ministry AP-token in T13 is removed. All Crown Policy actions are now +1 Ob until Ministry reestablishes presence in T13 (requires 1 season of Ministry NPC action in T13).

**Ministry and Hafenmark:**
Hafenmark's Parliamentary Manoeuvre benefits from Ministry presence. If Ministry has AP-token in T13: Hafenmark Parliamentary Manoeuvre Ob −1 (the clerks facilitate process). If Ministry AP-token absent from T13: Parliamentary Manoeuvre Ob +1 (no procedural infrastructure to execute the manoeuvre).

**Ministry and Löwenritter Coup:**
If Löwenritter Coup fires: Ministry AP-tokens in T13 and T12 are removed immediately. Ministry Mandate −2. PI −3 (standard coup effect) but Ministry Stabilisation does not fire next season (Ministry is recalibrating). Ministry attempts to re-establish AP-tokens in recouped territories at rate of 1/season.

### Ministry NPC AI Priority Tree (runs at Phase 4, Priority 4 — Domain Actions tier)
| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | PI ≤ 3 | Ministry plays Consul Inward (Govern) in T13: roll Ministry Mandate (3D) vs Ob 1. Success: PI +1 (clerks shore up parliamentary function). |
| 2 | T13 has no Ministry AP-token | Ministry plays Consul Inward in T13: roll Mandate 3D vs Ob 1. Success: AP-token placed in T13. |
| 3 | Any territory with AP-token has PI loss pending from Church Seizure | Ministry files automatic procedural objection: Church Seizure in that territory delayed 1 season. No roll required. AP-token in that territory is consumed. *(PP-564: Ministry institutional role — procedural delay, not combat)* |
| 4 | Crown Mandate ≥ 4 AND PI < 5 | Ministry plays Senator Inward (Decree support): PI +1 (Ministry facilitates Crown constitutional governance). Requires Crown Mandate ≥ 4 — Ministry does not support a weakened Crown. |
| 5 (default) | None of above | Ministry plays Consul Inward in highest-Prosperity uncontested territory with AP-token: Prosperity maintained. |

### Ministry Compromise and Corruption
Factions may attempt to corrupt Ministry via Diplomacy.

**Corrupt Ministry (Consul Outward, any faction, Ob = floor(Ministry Mandate / 2) + 1):**
Success: Ministry NPC Priority 4 fires in favour of the corrupting faction this season (Ministry supports that faction's Crown Policy or Parliamentary action regardless of current priorities).
Overwhelming: As above + Ministry AP-token in one territory of choice acts as if that territory is the corrupting faction's capital for one season (−1 Ob on all their actions there).
Failure: Ministry notes the attempt. Corrupting faction Stability −1. Ministry sends record to Riskbreakers (Riskbreaker Priority 6 now includes the corrupting faction's territory).

**Ministry Collapse (Mandate 0):** Ministry ceases NPC actions for 2 seasons. All Ministry AP-tokens removed. During collapse: Crown Policy +1 Ob, Parliamentary Manoeuvre +1 Ob, all Hafenmark Deed 3 (Parliamentary Consolidation) checks suspended. Collapse exit: Hafenmark or Crown plays Govern Inward in T13 (Ob 2). Success: Ministry Mandate returns to 1, AP-token placed in T13, collapse ends.

### Ministry and PI Track — Summary
| Ministry State | PI Effect |
|---------------|-----------|
| AP-token in T13, Mandate ≥ 2 | Emergency Powers PI loss −1 (Ministry prevents one loss/season) |
| AP-token in T13, Mandate ≥ 2, Hafenmark Manoeuvre success this year | Additional PI +1 at Year-End (Legislative Record) |
| AP-token absent from T13 | Hafenmark Parliamentary Manoeuvre Ob +1 |
| Ministry Mandate ≤ 1 | Crown Policy unavailable |
| Church seizes T13 with AP-token present | Seizure Ob +1; if seized: AP-token removed, Crown Policy +1 Ob |
| Löwenritter Coup | T13+T12 AP-tokens removed; Ministry Mandate −2; Ministry Stabilisation suspended 1 season |


### Ethical Framework: Procedural Consequentialism
The Ministry evaluates actions by whether they preserve the procedural conditions for governance. It is not loyal to Crown, Church, or Hafenmark — it is loyal to the functioning of the state itself. It is the civil service: clerks, administrators, record-keepers, tax collectors, enforcement officers.

**Ministry is always NPC-controlled.** It has no player victory condition and cannot be captured by any faction's card play.


### Ministry Stats
| Stat | Value | Notes |
|------|-------|-------|
| Mandate | 3 | Institutional legitimacy of the administrative apparatus |
| Influence | 4 | Reach into all territories via clerks and administrators |
| Wealth | 2 | State treasury access (limited — Crown controls the purse) |
| Military | 0 | Ministry has no military capacity |
| Stability | 5 | The civil service is hard to destroy |


### Ministry Tokens
Ministry maintains **Administrative Presence** tokens (AP-tokens, not to be confused with Attention Pool).
One AP-token per territory in which Ministry has clerks active. Starts with AP-tokens in T14 (Ehrenfeld), T2 (Kronmark), T5 (Feldmark), T1 (Valorsplatz). These represent the administrative apparatus of Parliamentary governance. (PP-204 corrected.)


### Parliament Connection — Direct Mechanics
Ministry is the mechanical engine behind Parliament Integrity (PI).

**Ministry Stabilisation (fires at Accounting Step 11, before Hollow Victory totals):**
Each season Ministry has an AP-token in T1 (Valorsplatz, Parliament seat): PI degradation from Crown Emergency Powers is reduced by 1 (to a minimum of −0 — i.e. Ministry can prevent one Emergency Powers PI loss per season). This represents clerks managing the parliamentary record and maintaining continuity despite political disruption.

**Ministry Legislative Record:**
At each Year-End Accounting: Ministry produces a Legislative Record for the prior year. Any Parliamentary Manoeuvre that succeeded (Hafenmark) this year is recorded as a Parliamentary Ruling. Effect: the first time each year a Parliamentary Ruling is recorded, PI +1 (the institution acknowledges the precedent). This is in addition to the standard Hafenmark Parliamentary Manoeuvre PI recovery.

**Ministry and Crown Policy:**
Crown Policy Instruments require Ministry countersignature. If Ministry Mandate < 2 (collapsed or compromised): Crown Policy actions cost +1 Ob (the administrative apparatus is too compromised to implement the decree cleanly). If Ministry Mandate = 0: Crown Policy actions unavailable until Ministry Mandate recovers.

**Ministry and Church Seizure (CI 75):**
Church Territorial Seizure of T1 (Valorsplatz) requires removing the Ministry AP-token first. If AP-token present: seizure Ob +1 (the administrative apparatus resists institutional capture). If seizure succeeds despite the token: Ministry AP-token in T13 is removed. All Crown Policy actions are now +1 Ob until Ministry reestablishes presence in T13 (requires 1 season of Ministry NPC action in T13).

**Ministry and Hafenmark:**
Hafenmark's Parliamentary Manoeuvre benefits from Ministry presence. If Ministry has AP-token in T13: Hafenmark Parliamentary Manoeuvre Ob −1 (the clerks facilitate process). If Ministry AP-token absent from T13: Parliamentary Manoeuvre Ob +1 (no procedural infrastructure to execute the manoeuvre).

**Ministry and Löwenritter Coup:**
If Löwenritter Coup fires: Ministry AP-tokens in T13 and T12 are removed immediately. Ministry Mandate −2. PI −3 (standard coup effect) but Ministry Stabilisation does not fire next season (Ministry is recalibrating). Ministry attempts to re-establish AP-tokens in recouped territories at rate of 1/season.


### Ministry NPC AI Priority Tree (runs at Phase 4, Priority 4 — Domain Actions tier)
| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | PI ≤ 3 | Ministry plays Consul Inward (Govern) in T13: roll Ministry Mandate (3D) vs Ob 1. Success: PI +1 (clerks shore up parliamentary function). |
| 2 | T13 has no Ministry AP-token | Ministry plays Consul Inward in T13: roll Mandate 3D vs Ob 1. Success: AP-token placed in T13. |
| 3 | Any territory with AP-token has PI loss pending from Church Seizure | Ministry files automatic procedural objection: Church Seizure in that territory delayed 1 season. No roll required. AP-token in that territory is consumed. *(PP-564: Ministry institutional role — procedural delay, not combat)* |
| 4 | Crown Mandate ≥ 4 AND PI < 5 | Ministry plays Senator Inward (Decree support): PI +1 (Ministry facilitates Crown constitutional governance). Requires Crown Mandate ≥ 4 — Ministry does not support a weakened Crown. |
| 5 (default) | None of above | Ministry plays Consul Inward in highest-Prosperity uncontested territory with AP-token: Prosperity maintained. |


### Ministry Compromise and Corruption
Factions may attempt to corrupt Ministry via Diplomacy.

**Corrupt Ministry (Consul Outward, any faction, Ob = floor(Ministry Mandate / 2) + 1):**
Success: Ministry NPC Priority 4 fires in favour of the corrupting faction this season (Ministry supports that faction's Crown Policy or Parliamentary action regardless of current priorities).
Overwhelming: As above + Ministry AP-token in one territory of choice acts as if that territory is the corrupting faction's capital for one season (−1 Ob on all their actions there).
Failure: Ministry notes the attempt. Corrupting faction Stability −1. Ministry sends record to Riskbreakers (Riskbreaker Priority 6 now includes the corrupting faction's territory).

**Ministry Collapse (Mandate 0):** Ministry ceases NPC actions for 2 seasons. All Ministry AP-tokens removed. During collapse: Crown Policy +1 Ob, Parliamentary Manoeuvre +1 Ob, all Hafenmark Deed 3 (Parliamentary Consolidation) checks suspended. Collapse exit: Hafenmark or Crown plays Govern Inward in T13 (Ob 2). Success: Ministry Mandate returns to 1, AP-token placed in T13, collapse ends.


### Ministry and PI Track — Summary
| Ministry State | PI Effect |
|---------------|-----------|
| AP-token in T13, Mandate ≥ 2 | Emergency Powers PI loss −1 (Ministry prevents one loss/season) |
| AP-token in T13, Mandate ≥ 2, Hafenmark Manoeuvre success this year | Additional PI +1 at Year-End (Legislative Record) |
| AP-token absent from T13 | Hafenmark Parliamentary Manoeuvre Ob +1 |
| Ministry Mandate ≤ 1 | Crown Policy unavailable |
| Church seizes T13 with AP-token present | Seizure Ob +1; if seized: AP-token removed, Crown Policy +1 Ob |
| Löwenritter Coup | T13+T12 AP-tokens removed; Ministry Mandate −2; Ministry Stabilisation suspended 1 season |


## Ministry AP-Token Starting Positions (PP-203)
T14 (Ehrenfeld), T2 (Kronmark), T5 (Feldmark), T1 (Valorsplatz — primary Parliament seat).


## Guilds CP-Token Starting Positions (PP-203)
T11 (Halvardshelm), T8 (Gransol), T3 (Lowenskyst), T1 (Valorsplatz), T9 (Himmelenger). [PP-199 numbering confirmed — all correct.]


## Niflhel Network Starting Depth (PP-203)
T12 (Sigurdshelm) depth 2. T1 (Valorsplatz) depth 1. T9 (Himmelenger) depth 1. [Confirmed correct numbering.]
