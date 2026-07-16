<!-- [PP-686 v2 NOTE 2026-05-01] Mandate is now derived per designs/provincial/faction_behavior_v30.md §4: `Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)`. Existing Mandate consumers in this file (Excommunication Ob Cap, RDT/TD escalation rows, Turmoil Mandate checks) continue to function via this derivation; no behavioral change. Refactor of consumers to read Legitimacy or Popular_Support directly is opportunistic. -->


## Trade Network Investment — Hafenmark Wealth Sink (PP-178)
Consul Inward, 2 Wealth cost. Ob 2. Places Trade Route tokens for +1D Trade bonuses.
Success: Trade Route token placed (+1D Trade this territory this season). Token persists until control transfer.
Overwhelming: As above + token links adjacent territory + Guild Favour +1 in non-capital territory.
Partial: Token placed, no bonus. Persists.
Failure: No token, Stability −1.


<!-- [REMOVED 2026-05-04] AER (Altonian Ecclesiastical Relationship) track removed. Church-Altonian diplomacy → Altonian hooks. -->
## RDT (Reformed Doctrine Track) (PP-181, v04 B5 confirmed)
Hafenmark private track 0–5. (PP-555)
[Full mechanics in PP-181 section — confirmed by v04 B5]


## TD (Theological Dissatisfaction) (PP-181, v04 B5 confirmed)
Hafenmark private track 0–5.


## VTM — STRUCK (PP-663, 2026-04-19)
Vaynard Thread Mastery track removed as faction-level stat. Thread capability is now character-scale only (Vaynard's personal TS/Coherence per threadwork_v30). Faction-level gates re-specced: see PP-663.


## Church Excommunication Ob Cap (PP-180)
Ob = floor(target L / 2) + 1.


## Partial Mend — Thread Wound Risk (PP-184)
Partial or Failed Mend still places History Resonance marker (temporal auto-effect fires regardless of degree).
2 existing markers + Partial Mend = Thread Wound. Warning token required at 2 markers.


## Church Attention Pool — Per-Territory Rules (PP-185)
Per-territory ceiling: 10. **First Inquisitor at AP ≥ 3. Second Inquisitor at AP ≥ 6.** Max 2 Inquisitors/territory. (ED-322 confirmed 2026-04-08.)
Community Organizing success: AP −2 + expels one Inquisitor if AP drops below deployment threshold.



## Hafenmark — RDT/TD Tracks (ED-321 RESOLVED)

### Reformed Doctrine Track (RDT) — Range 0–5
Advances: Reformed Settlement event = +1 (max once per arc). Requires: Hafenmark controls territory where Church has Parish/Cathedral AND Hafenmark M ≥ 3 AND PI ≥ 4.

| RDT | Effect |
|-----|--------|
| 0 | Reformed Settlement blocked: Church may Appease at no cost |
| 1 | Parliamentary Manoeuvre targeting CI: −1 Ob |
| 2 | Formal Reformed Settlement. TD track activates. |
| 3 | Church L −1 (institutional strain) + Diplomatic actions vs Church: −1 Ob |
| 4 | CI suppression extends: −1 CI/season while Hafenmark L ≥ 3 (was ≥ 4). Reformed territory PT actions +1 Ob for Church. |
| 5 | Excommunication against Hafenmark costs +2 L (Church loses procedural authority equivalent to Hafenmark's PE-driven institutional resilience). Baralta: −2 Ob on CI Suppress actions. All diplomatic actions targeting Hafenmark from any faction: +1 Ob. |

### Theological Dissatisfaction (TD) — Range 0–5
Activates at RDT 2. Advances: +1 per arc when RDT ≥ 2 AND Church plays Assert. Church may freeze TD by playing Accommodate Reformed Settlement.
Regression: TD −1 if Church Excommunicates Hafenmark AND RDT does not advance that arc.

| TD | Effect |
|----|--------|
| 0 | No effect |
| 1 | Templar deployment costs +1 Wealth in Hafenmark-adjacent territories |
| 2 | Cardinal of Fortitude schism risk when Church Stability < 3 |
| 3 | Any season Church loses PI: Hafenmark gains PI +1 |
| 4 | Church Seizure in Hafenmark territories: Ob +2 |
| 5 | Church cannot seize T8 Gransol (Hafenmark capital) regardless of CI or PT. Permanent. |

---


### Reformed Doctrine Track (RDT) — Range 0–5
Advances: Reformed Settlement event = +1 (max once per arc). Requires: Hafenmark controls territory where Church has Parish/Cathedral AND Hafenmark M ≥ 3 AND PI ≥ 4.

| RDT | Effect |
|-----|--------|
| 0 | Reformed Settlement blocked: Church may Appease at no cost |
| 1 | Parliamentary Manoeuvre targeting CI: −1 Ob |
| 2 | Formal Reformed Settlement. TD track activates. |
| 3 | Church L −1 (institutional strain) + Diplomatic actions vs Church: −1 Ob |
| 4 | CI suppression extends: −1 CI/season while Hafenmark L ≥ 3 (was ≥ 4). Reformed territory PT actions +1 Ob for Church. |
| 5 | Excommunication against Hafenmark costs +2 L (Church loses procedural authority equivalent to Hafenmark's PE-driven institutional resilience). Baralta: −2 Ob on CI Suppress actions. All diplomatic actions targeting Hafenmark from any faction: +1 Ob. |


### Theological Dissatisfaction (TD) — Range 0–5
Activates at RDT 2. Advances: +1 per arc when RDT ≥ 2 AND Church plays Assert. Church may freeze TD by playing Accommodate Reformed Settlement.
Regression: TD −1 if Church Excommunicates Hafenmark AND RDT does not advance that arc.

| TD | Effect |
|----|--------|
| 0 | No effect |
| 1 | Templar deployment costs +1 Wealth in Hafenmark-adjacent territories |
| 2 | Cardinal of Fortitude schism risk when Church Stability < 3 |
| 3 | Any season Church loses PI: Hafenmark gains PI +1 |
| 4 | Church Seizure in Hafenmark territories: Ob +2 |
| 5 | Church cannot seize T8 Gransol (Hafenmark capital) regardless of CI or PT. Permanent. |

---


## VTM 5 — STRUCK (PP-663, 2026-04-19)
Once-per-game tracking removed with VTM track. Thread-scaled abilities at faction scale dissolved.

---

## Accord (Per-Territory, 0–3) — PP-645, peninsular_strain_v30.md §2

Population acceptance of current controller. Modifies effective Prosperity and TCV.

| Accord | Name | Effective Prosperity | Other Effects |
|--------|------|---------------------|---------------|
| 3 | Aligned | Base (full) | Defender +1D in Battle. |
| 2 | Compliant | Base (full) | Normal operations. |
| 1 | Resistant | 0 | Govern Ob +1. Garrison required (≥ 1 unit) or Accord → 0 at Accounting. |
| 0 | Revolt | N/A | Territory becomes Uncontrolled. Garrison fights Popular Uprising (Military vs Ob 2). |

**TCV counts only at Accord ≥ 2.** Military conquest → Accord 1. Non-military acquisition → Accord 2+.

**Starting Accord:** Faction capitals = 3. Home territories = 2. T15 Askeheim: no Accord. T16 Schoenland: not in play.

---

## Turmoil (Global, 0–10) — PP-646, peninsular_strain_v30.md §4

Tracks cumulative civil war damage to peninsular unity. Starts at 0.

**Advance:** +1 per season with inter-faction battle. +2 per faction elimination. +1 per Revolt.
**Decay:** −1 per peaceful season (no battles, no revolts). −1 per diplomatic resolution (max 1/season).

| Strain | Name | Effect |
|--------|------|--------|
| 0–2 | Peace | None. |
| 3–4 | Tension | All factions: L check at Accounting (pool vs Ob 1). Failure: L −1. |
| 5–6 | Fracture | All factions: Accord −1 in one territory (lowest first). |
| 7–8 | Crisis | All factions: Accord −1 in ALL non-capital territories. L check Ob 2. |
| 9–10 | Collapse | Non-capital Accord cap 2. L check Ob 3. RS −1/season additional. |

---

## Starting Piety Track (PT) — PP-652 (provisional), peninsular_strain_v30.md §2.2

| T# | Territory | Starting PT | Rationale |
|----|-----------|-------------|-----------|
| T1 | Valorsplatz | 3 | Capital, moderate piety |
| T2 | Kronmark | 3 | Heartland, orthodox |
| T3 | Lowenskyst | 3 | Border fortress, practical |
| T4 | Grauwald | 2 | Highland, old Einhir traditions |
| T5 | Feldmark | 3 | Agricultural, conventional |
| T6 | Stillhelm | 1 | Calamity proximity erodes faith |
| T7 | Rendstad | 3 | Conventional |
| T8 | Gransol | 3 | Baralta devout but parliamentary moderation |
| T9 | Himmelenger | 5 | Cathedral city (canonical) |
| T10 | Spartfell | 3 | Practical |
| T11 | Halvardshelm | 2 | Old Einhir ways |
| T12 | Sigurdshelm | 2 | Varfell seat, Restoration-sympathetic |
| T13 | Oastad | 1 | Calamity proximity, Restoration stronghold |
| T14 | Ehrenfeld | 3 | Institutional piety |
| T15 | Askeheim | 0 | Hard-fixed (canonical) |
| T17 | Halvarshelm | 3 | Conventional |

[PROVISIONAL — pending user review]
