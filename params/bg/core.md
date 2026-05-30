

<!-- [SUPERSEDED 2026-04-19] CULTURAL REFORMATION STRUCK + VTM STRUCK -->
<!-- Per Jordan decision 2026-04-19 (session): Cultural Reformation was incompatible with Vaynard's identity. -->
<!-- Vaynard is a military conqueror. He does not convert populations ideologically. Varfell expansion is purely military. -->
<!-- VTM (Vaynard Thread Mastery) was also STRUCK — placeholder mechanic with no canonical advancement. -->
<!-- Tribune intel (reveals enemy stats for target selection) remains. Thread operations remain as personal-scale actions -->
<!-- available to Varfell first due to southern TS baseline + RM proximity, NOT as BG-layer combat/territorial bonuses. -->
<!-- See commits: 297f892 (engine), 13b8f30 (workplan), 13b8f30 (canon audit workplan). -->
<!-- [CORRECTED 2026-05-29, ED-880] The 'Varfell expansion is purely military / does not convert populations ideologically' claim above is SUPERSEDED. The 2026-04-19 strike validly removed the VTM-dependent Cultural REFORMATION (VTM remains struck); the Conviction-Track redesign (designs/scene/conviction_track_v30.md) reintroduced the ideological-conversion capability VTM-free as Cultural RECLAMATION (Varfell: Influence vs Ob 2, target-territory Piety -1 toward Einhir Restoration). This acts on religious/cultural ALIGNMENT (Piety), NOT territory control, and is NOT a victory path. Varfell also takes all universal faction actions. Per GD-1 the SOLE victory condition for all factions is Peninsular Sovereignty (control 11+ of 15 territories) — no faction-specific or non-military victory path exists. -->

## FACTION ASSIGNMENT (canonical, v04 B1)

### Playable Factions
| Faction | Player Count |
|---------|-------------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) — statless faction; operates through PT and Presence only |
| Löwenritter | Conditional: Split stage only |

### NPC-Only Factions (never playable)
Löwenritter (pre-Split), Riskbreakers, Inquisitors, Guilds, Schoenland, Altonia, Edeyja/Wardens.
<!-- Niflhel deleted 2026-04-30 (was: STRUCK per conflict_architecture_proposal §Niflhel Dissolution). Functions distributed to settlement-level phenomena (black markets, intelligence brokers, Thread exploitation sites). -->
Ministry: NPC faction (source document not yet identified — [GAP: Ministry NPC design doc not found in any read document. User confirmed it exists. Design blocked until source located.])

Note: Guilds do NOT have player victory conditions. All Guilds victory condition text from prior params versions was struck (PP-191).


### Playable Factions
| Faction | Player Count |
|---------|-------------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) — statless faction; operates through PT and Presence only |
| Löwenritter | Conditional: Split stage only |


### NPC-Only Factions (never playable)
Löwenritter (pre-Split), Riskbreakers, Inquisitors, Guilds, Schoenland, Altonia, Edeyja/Wardens.
<!-- Niflhel deleted 2026-04-30 (was: STRUCK per conflict_architecture_proposal §Niflhel Dissolution). Functions distributed to settlement-level phenomena (black markets, intelligence brokers, Thread exploitation sites). -->
Ministry: NPC faction (source document not yet identified — [GAP: Ministry NPC design doc not found in any read document. User confirmed it exists. Design blocked until source located.])

Note: Guilds do NOT have player victory conditions. All Guilds victory condition text from prior params versions was struck (PP-191).


## Dice System (v05 correction)
d10 pool. TN 7 (standard).
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes |

Net successes = sum of contributions. May be negative (treated as 0 for degree purposes = Failure).
Ob minimum: 1. No modifier may push Ob below 1.
**Majority-1s (Catastrophic Failure) override: STRUCK** (v05 DESIGN DECISION 2026-04-02). All rolls resolve through standard degree table only. Low-pool results produce Failure; no additional consequence category exists.


## Degree Table (PP-179 + PP-249 — matches TTRPG)
| Net Successes | Degree |
|--------------|--------|
| ≥ 2× Ob AND ≥ 3 | Overwhelming |
| ≥ Ob | Success |
| 0 < net < Ob | Partial |
| ≤ 0 | Failure |
Overwhelming floor: net must be ≥ 3 regardless of Ob (matches PP-232 TTRPG rule). (PP-249)
ED-031 (Ob+1 surplus) is SUPERSEDED by PP-179 (2×Ob). PP-179 is canonical.
Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5.
[FLAGGED FOR REVIEW: ED-142-R — confirm 2×Ob canonical; confirm floor of 3 applies to BG; confirm Ob 10 exception carries.]


## Starting Values (v04 B2, PP-188 correction)
| Track | Start | Range | Notes |
|-------|-------|-------|-------|
| Mending Stability (MS) | 72 | 0–100 | Rupture = shared loss |
| Church Influence (CI) | **28** | 0–100 (no freeze) | CI 60 = Mass Seizure available (one-shot). CI 100 = cap. P-32 sets starting value at 28. |
| Invasion Pressure (IP) | 20 | 0–100 | IP 75 = Altonian Vanguard appears. IP 80+ = sustained Vanguard presence + skirmishes / small unit border incursions through mountain passes. IP ≥ 100 = Altonia regularly invades through one or both mountain passes (T10 Spartfell NE pass; second pass location TBD) — large-scale military invasion, not just political occupation. See peninsular_strain §6.4. |
| Parliament Integrity (PI) | **7** | 0–20 | Cumulative pressure meter. Auto-resolves at PI ≥ 20 (Crown elimination). |
| | 2 | 0–5 | Near IP clock. |
| Torben Loyalty | **7** | 0–7 | Active from game start. No IP trigger. On Crown elimination: Torben Loyalty track transfers to Löwenritter (they inherit the succession claim). Löwenritter wins or loses Torben via Influence actions the same way Crown did. Church and Hafenmark may contest via Senator Outward Diplomacy (Ob = current Torben Loyalty ÷ 2). (PP-599: start 7, range 0–7. PP-498 start 3 superseded.) |
| Elske Loyalty | 4 | 0–7 | Off-board card near T4. |
| Löwenritter Autonomy | Loyal | Loyal→Restless→Autonomous→Split | Graduated autonomy (conflict_architecture_proposal). Replaces binary Coup Counter. See below. |

#### Löwenritter Graduated Autonomy (replaces Coup Counter)

| Stage | Trigger | T14 Status | Crown Effect |
|-------|---------|------------|--------------|
| **Loyal** | Start | S014 Barracks answers to Crown via Ehrenwall. Garrison deployable. | Normal. Crown controls T14 fully. |
| **Restless** | Crown Stability ≤ 3, OR no military action 4+ seasons, OR Crown loses a province | S014 follows Löwenritter orders for defensive actions. Crown +1 Ob offensive deployment. | Fragmentation checks at T14 Ob +1. |
| **Autonomous** | Crown Stability ≤ 2, OR Ehrenwall Disposition toward Almud < 0, OR 4+ seasons Restless without resolution | S014 does not respond to Crown. T14 garrison under Ehrenwall exclusively. Crown retains sovereignty claim. | Crown Military reduced by T14 garrison. Cannot access Fort 3. PI −1. |
| **Split** | Crown attacks Löwenritter, OR Crown eliminated, OR 4+ seasons Autonomous without resolution | T14 becomes Löwenritter territory. Löwenritter = separate faction (L3/PS3/Inf2/W3/Mil5/Stab5). PI −3. | Crown Military drops to 2 AND loses most units. Crown loses T14, PV drops by 3. Löwenritter negotiates independently. |

| **Coup** | Löwenritter loses faith in monarch AND has candidate (Torben, Elske, or a Duke with Löwenritter support) | T14 under Löwenritter. Crown faction SUSPENDED. Löwenritter installs new monarch. | If Torben/Elske/Lenneth installed: Crown resumes under new monarch; Löwenritter recedes into Crown military arm. If Duke (Vaynard/Baralta) installed: Crown absorbed into that Duke's faction; Crown ceases as independent faction. Löwenritter recedes into new monarch's military. Crown Military was 5 only because it WAS Löwenritter — without them, Crown Military = 2. |

**Reversal:** Stages 1–3 reversible. Crown can return to Loyal by: raising Stability above 3, conducting military action validating Löwenritter identity, or improving Ehrenwall Disposition through diplomatic engagement. Stage 4 (Split) is irreversible without reconquest.
| Warden Cooperation (WC) | 0 | 0–3 | Peninsula-wide. WR ≥ 2 required to advance. (PP-605) |
| Warden Recognition (WR) | 0 | 0–3 | Varfell-only private track. Gates WC. (PP-605) |
| Turmoil (= Strain) | 0 | 0–10 | Public. Also called "Strain" in peninsular_strain docs and phases.md §4d. Advances from inter-faction battles (+1/season), faction eliminations (+2), revolts (+1). Decays −1/peaceful season. See peninsular_strain_v1.md §4. |

**Accord (per-territory attribute, range 0–3):** Tracks population acceptance of controller. Modifies effective Prosperity. Accord ≥ 2 required for TCV contribution toward victory. See peninsular_strain_v1.md §2 for full rules.

| Accord | Name | Effective Prosperity | Other Effects |
|--------|------|---------------------|---------------|
| 3 | Aligned | Base (full) | Defender +1D in Battle. |
| 2 | Compliant | Base (full) | Normal operations. |
| 1 | Resistant | 0 | Govern Ob +1. Garrison required (≥ 1 unit) or Accord → 0 at Accounting. |
| 0 | Revolt | N/A | Territory becomes Uncontrolled at Accounting. Garrison fights Popular Uprising (Military vs Ob 2). |

**Starting Accord:** Faction capitals = 3 (Aligned). All other home territories = 2 (Compliant). T15 Askeheim: no Accord (no settled population). T16 Schoenland: not in play.

**Starting Piety Track (PT) values:**

| T# | Territory | Starting PV | Rationale |
|----|-----------|-------------|-----------|
| T1 | Valorsplatz | 5 | Crown Capital |
| T2 | Kronmark | 2 | Crown Heartland |
| T3 | Lowenskyst | 3 | Border Fortress (Fort 3) |
| T4 | Grauwald | 2 | Highland Timber |
| T5 | Feldmark | 2 | Breadbasket |
| T6 | Stillhelm | 1 | Southern Farmland |
| T7 | Rendstad | 1 | Timber Valley |
| T8 | Gransol | 4 | Hafenmark Capital |
| T9 | Himmelenger | 5 | Church Cathedral City (co-equal with Crown capital) |
| T10 | Spartfell | 3 | Border Castle (Fort 2) |
| T11 | Halvardshelm | 1 | Central Fjords |
| T12 | Sigurdshelm | 4 | Varfell Seat |
| T13 | Oastad | 1 | Southern Fjords |
| T14 | Ehrenfeld | 3 | Military Hinge (Fort 3) |
| T15 | Askeheim | 0 | Southernmost (Uncontrolled, hard-fixed) |
| T16 | Schoenland | 1 | Island Republic |
| T17 | Halvarshelm | 2 | Northern Mines |

PV hierarchy: 5 = Crown/Church capital · 4 = duchy/faction seat · 3 = fortress · 2 = economic importance · 1 = other · 0 = Southernmost. Total: 40. Jordan-confirmed 2026-04-23.

**Turmoil Threshold Effects:**

| Strain | Name | Effect |
|--------|------|--------|
| 0–2 | Peace | No effect. |
| 3–4 | Tension | All factions: L check at Accounting (L pool vs Ob 1). Failure: L −1. |
| 5–6 | Fracture | All factions: Accord −1 in one territory (lowest-Accord first, controller choice). |
| 7–8 | Crisis | All factions: Accord −1 in ALL non-capital territories. L check Ob 2. |
| 9–10 | Collapse | Non-capital territories: Accord cap 2. L check Ob 3. MS −1/season additional. |

**Warden Cooperation (WC) Effects:**
| WC | Effect |
|----|--------|
| 0 | No effect. |
| ≥ 1 | +1D to all Thread operations peninsula-wide. |
| ≥ 2 | MS decay rate halved (seasonal baseline −1 becomes −0.5, rounded down). |
| 3 | MS +2/season at Accounting. |


<!-- [PP-686 v2 NOTE 2026-05-01] Mandate is now derived per designs/provincial/faction_behavior_v30.md §4: Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support). Starting Mandate values below are preserved as initial conditions: Legitimacy_init = Popular_Support_init = current authored Mandate. After first Accounting, dynamics replace seed values. See L+PS Starting Values section below. -->

## Faction Starting Stats (v04 B5)
| Faction | Legitimacy | Popular_Support | Influence | Wealth | Military | Intel | Stability |
| --------- | ------------ | ------------------ | ----------- | -------- | ---------- | ------- | ----------- |
| Crown | 5 | 5 | 5 | 4 | 5 | 3 | 4 |
| Church | 5 | 5 | 6 | 5 | 4 | 4 | 5 |
| Hafenmark | 4 | 4 | 4 | 5 | 3 | 3 | 4 |
| Varfell | **4** | **4** | 4 | **4** | 4 | 4 | 4 |
| Restoration Movement | — | — | — | — | — | — | — | No faction stats. Operates via Presence markers and Community Weaving only. (PP-460) |
| Löwenritter (Split) | 3 | 3 | 2 | 3 | 5 | 3 | 5 |
| Guilds (NPC) | 3 | 3 | 4 | 6 | 2 | 4 | 5 |
<!-- [RECONCILED 2026-05-30, session 801b97c5: Intel column added per canonical 7-stat schema (ED-787; values from params/factions/stats_1_7_scale.md — Crown 3, Church 4, Hafenmark 3, Varfell 4, Löwenritter 3, Guilds 4). Gap-fill only; existing values untouched. UNRESOLVED (Jordan): Crown Military here=5 CONFLICTS with stats_1_7_scale.md=4 (direction undetermined). See ED-869. Jordan-vetoable. ] -->

CORRECTIONS (PP-191/PP-195/ED-809/ED-810): Varfell L 4, PS 4 (seed equal per PP-686 v2 / 2026-05-02 ED-784 — was unsplit Mandate 4), Wealth 4. Varfell starts with 4 territories (T4/T11/T12/T13). Handicap is defensive: mountain range + Thread Wounds hem in expansion. Handicap is defensive: mountain range + Thread Wounds hem in expansion. Intelligence path is correct. Fortification constraint (PP-191) applies to outward expansion, not inward security. CI = 28 (P-32). CI Mass Seizure threshold = 60, cap = 100 (per victory_v30.md §7).



### Legitimacy + Popular Support — Starting Values (PP-686 v2)

At engine init, both scalars seed equal per the L and PS columns above (post-2026-05-02 ED-784 finalization; the prior Mandate column has been split):
- `Legitimacy_init = L value in column 2`
- `Popular_Support_init = PS value in column 3`
- (For factions with seed-equal authoring, L_init = PS_init = the previously-unsplit Mandate value.)

Range [0, 7] for both. After first Accounting, dynamics replace seed values per `designs/provincial/faction_behavior_v30.md §3.4–3.5`. Factions with no L+PS at start (Restoration, Löwenritter) start with Legitimacy = Popular_Support = 0; PS may climb via successful Mission outcomes from zero.


## Faction Elimination — Territory Status (ED-333 resolved)
When a faction is eliminated (Stability 0 and no recovery action taken):
- All territories previously held enter **Political Vacuum** for 1 season (PP-500). During Vacuum: no faction may March in; Fort level retained; tokens removed. After 1 season: Vacuum lifts, territories become Uncontrolled, normal March rules apply.
- Uncontrolled territories: any faction may March in freely (no Battle roll for entry, no defender).
- Fort level is retained on the territory card (physical fortifications don't vanish).
- Ministry AP-tokens and Guilds CP-tokens in eliminated faction territories are removed immediately.
- Löwenritter Autonomy: if Crown is eliminated, Löwenritter immediately advances to Split (Stage 4). T14 becomes Löwenritter territory.
- CI, IP, MS effects tied to eliminated faction's territory holdings: cease immediately (e.g. T9 CI +1/season bonus stops if Church is eliminated and loses T9 control).



## Stat Ceilings and Floors
| Stat | Floor | Ceiling |
|------|-------|---------|
| Legitimacy | 0 | 7 |
| Popular_Support | 0 | 7 |
| Influence | 1 | 7 |
| Wealth | 0 | 7 |
| Military | 0 | 7 |
| Stability | 0 | 7 |


## Standard Action Ob Reference (P-21, v04 B3)
| Action | Default Ob | Key Modifiers |
|--------|-----------|---------------|
| Muster (Legionary Inward) | 2 | −1 T12 garrison |
| March (Legionary Outward) | No roll | Contested entry = Battle |
| Govern (Consul Inward) | floor(Prosperity / 2) + 1 | −1 own capital |
| Trade (Consul Outward) | floor(Prosperity / 2) + 1 | +1 IP≥30; +1 T2 |
| Diplomacy vs NPC (Senator Outward) | floor(NPC Stability / 2) + 1 | — |
| Diplomacy between players | Negotiated | Not a roll |
| Formal Crown Treaty (Senator Outward) | floor(target L / 2) + 1 | Crown only. PP-512/513/514/523. See victory_v30.md §3.1. |
| Thread Operation (Pontifex/Weaver) | Ob 2 base | See PP-182 co-movement protocol |
| Investigate/Intel (Tribune) | 2 | +2 Ob in Church territory with Inquisitor |
| Spy (Tribune Outward) | floor(target Intel / 2) + 1 | — |
| Survey (Consul Inward) | (5 − Proximity Rating) + 1, min 1 | Askeheim (PR 0) → Ob 6; Lowenskyst (PR 5) → Ob 1. Pool: Influence. On Success: reveal 1 undiscovered POI (Resource: Prosperity +1; Secret: +1D next mil/intel action; Remnant: Thread op Ob −1 ×2 seasons + Thread Debt token; Anomaly: MS −1 immediately + Warden Cooperation +1 eligible). On Failure targeting Depth ≥ 3: +1 Church Attention Pool. See fieldwork_design_v1.md §8.1. (PP-628) |
| Parliamentary Manoeuvre (Hafenmark) | floor(opponent Influence / 2) + 1 | — |
| Community Organising (Restoration) | 2 | Pool: 1D base + 1D per adjacent territory with RM Presence marker. Failure: no Stability cost (RM has no Stability). Try again next season. (PP-460) |
| Community Weaving (Restoration) | (100−MS)÷20 round up min 1 | −1 per Presence marker in territory |
| Dynastic Proclamation (Hafenmark) | floor(target Stability / 2) + 1 | Diplomat card. Hafenmark M ≥ 4, M > target controller M. +1 Ob if PT ≤ 1. −1 Ob if Diplomatic Token on target. See peninsular_strain_v1.md §5.3. |
| Cultural Reformation (Varfell) | STRUCK CR-STRIKE-2026-04-19 (VTM-dependent; VTM struck) | Reformation removed. SUPERSEDED by Cultural Reclamation (conviction_track_v30, Influence-based, VTM-free): a non-military Piety-ALIGNMENT action (PT −1 toward Einhir Restoration) — not a control transfer, not a victory path. 'Military-only' framing corrected per ED-880 (2026-05-29). See canon/supersession_register.yaml. |
| Martial Governance (Löwenritter) | floor(Prosperity / 2) + 2 | Löwenritter only. Military pool. Accord +1 (cap 2). |
| Fortify | Fort level + 1 | — |

All Obs: floor 1.


## ~~Ethical Framework Modifiers (v04 B4)~~ — SUPERSEDED 2026-05-01 (PP-686 v2)

<!-- [SUPERSEDED 2026-05-01 — SUPERSESSION-PP686-001] Replaced by triadic decomposition in designs/provincial/faction_behavior_v30.md §3.7 (mission_alignment + cascade_alignment + expectation_alignment, clamped ±2). Period-anachronistic philosophical-tradition labels (Virtue, Faith, Categorical Imperative, Scholastic, Equity, Honor) replaced by 13-Conviction taxonomy per PP-684. -->

| Faction | ~~Bonus~~ (struck) | ~~Penalty~~ (struck) |
|---------|--------------------|----------------------|
| Crown ~~(Virtue)~~ | ~~−1 Ob public~~ | ~~+1 Ob covert~~ |
| Church ~~(Faith)~~ | ~~−1 Ob doctrine-aligned~~ | ~~+2 Ob thread-supporting~~ |
| Hafenmark ~~(Categorical Imperative)~~ | ~~−1 Ob procedural~~ | ~~+1 Ob ad-hoc~~ |
| Varfell ~~(Scholastic)~~ | ~~−1 Ob evidence-based~~ | ~~+1 Ob emotional~~ |
| Restoration ~~(Equity)~~ | ~~−1 Ob community~~ | ~~+1 Ob hierarchical~~ |
| Löwenritter ~~(Honor)~~ | ~~−1 Ob loyal~~ | ~~+2 Ob disloyal~~ |

**Replacement** per `designs/provincial/faction_behavior_v30.md §3.7`:

```
Ob_modifier(da, faction) =
    mission_alignment_modifier(da, faction.mission)                          # -1, 0, +1 — reads PP-687 da_outcome subtypes
  + cascade_alignment_modifier(da, faction.aggregate_effective_convictions)  # -1, 0, +1 — reads PP-684 13-Conviction projection
  + expectation_alignment_modifier(da, faction)                              # ± strictness × {1, 2}
Ob_modifier = clamp(Ob_modifier, -2, +2)                                     # C1 cap (was ±3 in legacy table)
```

Faction-specific behavior emerges from authored Mission + leader Convictions + public temperament rather than per-faction philosophical tradition. See faction_behavior_v30 §3.3.1 for role templates with Honor as 13th Conviction (D1).


## Faction Conviction Texts (PP-181, ED-080/081 resolved 2026-04-03)
| Faction | Conviction |
|---------|-----------|
| Crown (Almud) | "Order is not made — it is maintained. Everything depends on not flinching." | *(ED-364: revised from cliché; Almud is shrewd and guarded, not indecisive)* |
| Church (Himlensendt) | Faith |
| Hafenmark (Baralta) | "Faith is not mediated — it is lived. Anyone who is truly faithful can hear Solmund. Anyone who cannot should not rule." |
| Varfell (Vaynard) | "The strongest thread is the one others cannot see — and I have spent my life learning to pull it." |
| Restoration (Erikssen collective) | "The community is the only legitimate political unit." |
| Löwenritter (Ehrenwall) | "Valoria endures, whatever the cost." |


## Batch Card Hand (v04 B3 confirmed — Card-Hand system PP-177)
| Faction | Starting Hand |
|---------|--------------|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex, 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat, 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist, 1× Recess |
| Restoration | 1× Pontifex, 2× Praetor, 1× Senator, 1× Tribune, 1× Recess |

Domain Expertise (+1D when playing this card type):
Crown = Legionary | Church = Senator | Hafenmark = Consul/Prefect | Varfell = Tribune | Restoration = Pontifex (Thread) only. RM hand: 2× Praetor (Community Organising/Project), 1× Pontifex (Community Weaving + Cultural Uprising), 1× Recess. No Legionary, no Senator (for stats-based actions), no Tribune. (PP-460)
