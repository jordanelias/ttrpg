<!-- [PROVISIONAL: 2026-05-01 — PP-686 v2 Phase B Stage 6: per-territory public temperament authoring] -->
<!-- STATUS: PROVISIONAL — Class A authoring document. Authors public temperament per province for the 17 canonical Valoria provinces. Settlement-level temperament deferred to Stage 6b. -->
<!-- AUTHORITY: PP-686 v2 (faction_behavior_v30.md §3.4.1) -->

# Per-Territory Public Temperament (PP-686 v2 Phase B Stage 6)
## Status: CANONICAL

## §1 Purpose

PP-686 v2 §3.4.1 defines a 5-temperament typology authored per territory:

| Temperament | α (outcomes weight) | β (conduct weight) | Period example |
|---|---:|---:|---|
| pragmatic | 0.7 | 0.3 | Florentine merchant class |
| traditional | 0.3 | 0.7 | rural devout populace |
| balanced | 0.5 | 0.5 | mixed urban populace |
| principled | 0.2 | 0.8 | reformist enclaves |
| outcomes-only | 0.9 | 0.1 | hardship populations under direct threat |

A faction's effective temperament is the population-weighted average across its territories (§3.4.1). A territory's temperament can drift toward `outcomes-only` under sustained `env.peninsular_strain_shock` Keys (§3.4.2).

This document authors initial values for the 17 canonical Valoria provinces (T1–T17).

**Authority:** geographic data per `designs/territory/valoria_geography_v30.yaml`.
**Co-files updated:** `references/canonical_sources.yaml`.

---

## §2 Per-Territory Temperament Table

| T | Name | Faction | Region / Sub | Temperament | α | β | Rationale |
|---|---|---|---|---|---:|---:|---|
| T1 | Valorsplatz | Crown | Eastern Lowlands / Capital | pragmatic | 0.7 | 0.3 | Crown capital + river-sea trade nexus → urban-merchant outcomes-favoring populace |
| T2 | Kronmark | Crown | Eastern Lowlands / Heartland | traditional | 0.3 | 0.7 | Italian-coded farmland heartland → rural devout populace; conduct-weighted |
| T3 | Lowenskyst | Crown | Northern Mountains / Border Fortress | balanced | 0.5 | 0.5 | NE Altonian-pass garrison + civilian mixed; military presence balances populace |
| T4 | Grauwald | Varfell | Central Highlands / Highland Timber | traditional | 0.3 | 0.7 | Einhir heritage + highland timber communities → strong precedent / community register |
| T5 | Feldmark | Crown | Eastern Lowlands / Breadbasket | traditional | 0.3 | 0.7 | Crown breadbasket; agrarian populace; Hafenmark food-dependency anchor |
| T6 | Stillhelm | Crown | Southern Approaches / S. Farmland | outcomes-only | 0.9 | 0.1 | Calamity-adjacent (southern Crown gate to Askeheim T15); hardship populace prioritizes outcomes |
| T7 | Rendstad | Hafenmark | Hafenmark Highlands / Timber Valley | traditional | 0.3 | 0.7 | Remote forested valley → traditional communal populace |
| T8 | Gransol | Hafenmark | Hafenmark Highlands / Constitutional Capital | pragmatic | 0.7 | 0.3 | Hafenmark constitutional capital + west-sea trade + Schoenland route → merchant pragmatism |
| T9 | Himmelenger | Church | Mountain Ridge / Cathedral City | principled | 0.2 | 0.8 | Church seat / cathedral city; devout populace strongly conduct-weighted |
| T10 | Spartfell | Hafenmark | Northern Mountains / Border Castle | balanced | 0.5 | 0.5 | NW Altonian-pass garrison + Hafenmark mining hinterland; mixed |
| T11 | Halvardshelm | Varfell | Central Fjords | traditional | 0.3 | 0.7 | Fjord communities + Spartfell border → traditional populace |
| T12 | Sigurdshelm | Varfell | Western Fjords / Varfell Seat | balanced | 0.5 | 0.5 | Vaynard's court (urban administrative) + surrounding fjord population (traditional); aggregate balanced |
| T13 | Oastad | Varfell | Southern Fjords | outcomes-only | 0.9 | 0.1 | Calamity-adjacent (Varfell southern gate to Askeheim T15); hardship populace |
| T14 | Ehrenfeld | Crown | Central Plains / Military Hinge | balanced | 0.5 | 0.5 | Crown military hinge + Löwenritter base + 5-way connection → mixed military/civilian |
| T15 | Askeheim | Uncontrolled | Southernmost / Calamity Epicenter | outcomes-only | 0.9 | 0.1 | Calamity epicenter / forgetting zone; populace under direct threat (where any populace remains) |
| T16 | Schoenland | Schoenland | Eastern Sea / Island Republic | pragmatic | 0.7 | 0.3 | Independent island republic + Altonian trade + naval choke → merchant pragmatism |
| T17 | Halvarshelm | Hafenmark | Northern Mountains / Northern Mines | balanced | 0.5 | 0.5 | Iron/copper mining + Guild operations → mixed mining-pragmatic + procedural-guild populace |

---

## §3 Per-Faction Aggregated Temperament (initial)

Per `faction_behavior_v30.md §3.4.1`, faction effective temperament = population-weighted average across its territories. Population weighting deferred (uniform-weighted approximation here, calibrate at Stage 10).

| Faction | Territories | Distribution | Approximate aggregate (uniform weighting) |
|---|---|---|---|
| Crown | T1, T2, T3, T5, T6, T14 | 1 pragmatic, 2 traditional, 2 balanced, 1 outcomes-only | α≈0.50, β≈0.50 — balanced-leaning |
| Church | T9 | 1 principled | α=0.20, β=0.80 — strongly principled |
| Hafenmark | T7, T8, T10, T17 | 1 pragmatic, 1 traditional, 2 balanced | α≈0.55, β≈0.45 — mildly pragmatic |
| Varfell | T4, T11, T12, T13 | 2 traditional, 1 balanced, 1 outcomes-only | α≈0.50, β≈0.50 — balanced (skewed by traditional) |

**Restoration Movement** and **Löwenritter** do not own territories at scenario init; their effective temperament is derived from the territories they operate within (RM via Presence markers; Löwenritter embedded in Crown territories T3/T14 etc.). No initial aggregate authored at this layer.

**Schoenland** is foreign / NPC; not a player faction at this layer.

---

## §4 Drift Dynamics (per spec §3.4.2)

`env.peninsular_strain_shock` Keys with positive `strain_delta` shift affected territories' temperament drift toward `outcomes-only`:

```
on env.peninsular_strain_shock(strain_delta, affected_territories):
    for territory in affected_territories:
        if strain_delta > 0:
            territory.temperament_drift = clamp(
                territory.temperament_drift + 0.1 × strain_delta, -1, +1
            )
```

Drift bias applies to faction effective-temperament recomputation each Accounting. Calamity-adjacent territories (T6, T13, T15) start near `outcomes-only` and have less headroom to drift further.

---

## §5 Open Items

| Item | Resolution |
|---|---|
| Settlement-level temperament (Stage 6b) | Deferred — 17 provinces is initial coverage; ~50 settlement entries from `valoria_geography_v30.yaml.settlements` deferred to designer authoring at Stage 10 sim observation point |
| Population weighting per territory | Uniform default; per-territory population data in `valoria_geography_v30.yaml.starting_pros` could weight aggregate; calibrate at Stage 10 |
| RM / Löwenritter aggregate when they operate within other factions' territories | Per faction_behavior §3.4.1 — they read effective temperament from territories they operate within; no separate authoring needed |
| Schoenland / Altonia foreign factions | Not authored at this layer; out-of-scope for player-faction temperament |

---

## §6 Sign-off

| Item | Status |
|---|---|
| Temperament authored for 17 provinces (T1–T17) | YES — PROVISIONAL |
| 5-typology coverage | All 5 typologies represented (pragmatic, traditional, balanced, principled, outcomes-only) |
| Per-faction aggregate computed | YES — uniform-weighted approximation |
| Settlement-level temperament | DEFERRED to Stage 6b |
| Drift dynamics specified | Per §4 |

**Stage 6 (territory-level) closed:** PROVISIONAL pending Stage 10 sim verification. Stage 6b (settlement-level) defer.

---

**End Stage 6 authoring. PROVISIONAL pending Stage 10 calibration.**
