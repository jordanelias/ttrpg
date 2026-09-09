<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: geography_v30_infill.md -->

<!-- v30 baseline — renamed from designs/setting/geography_design.md on 2026-04-13 -->
# VALORIA — Geography & Territory Design
## Status: CANONICAL — approved 2026-04-05
## Scope: Physical geography, territory map (17 territories), adjacency graph, starting control
## Supersedes: compilation/v0.14/stage7_territories_deprecated.md §7.2, §7.3

---

## Physical Geography

Valoria occupies a north-south peninsula attached to a continental landmass. An east-west mountain range separates Valoria from the Empire of Altonia at the northern boundary. No navigable sea passage exists around the north. The peninsula narrows southward, terminating at the Southernmost — the epicenter of the Einhir Catastrophe.

### Terrain Regions

**Northern Mountains (east-west barrier):** Continuous range across the northern boundary. Two passes: Lowenskyst (NE, primary, Crown fortress) and Spartfell (NW, secondary, Hafenmark border castle). Altonian invasion funnels through these chokepoints unless Schoenland grants naval passage.






### Continental Context


### Geographic Unity



### Church Geography


### Restoration Movement Geography


### Maritime Forgetting Zone


### Calamity Bleed Gradient

**Superseded by `designs/setting/calamity_radiation.md`** (canonical, 2026-04-06). The full RS-band × node-distance radiation matrix replaces this static table. Summary of node distances:

| Distance | Territories |
|---|---|
| 0 | T15 Askeheim |
| 1 | T6 Stillhelm, T13 Oastad |
| 2 | T5 Feldmark, T12 Sigurdshelm |
| 3 | T1 Valorsplatz, T14 Ehrenfeld, T4 Grauwald, T11 Halvardshelm |
| 4 | T2 Kronmark, T16 Schoenland, T9 Himmelenger, T7 Rendstad, T10 Spartfell |
| 5 | T3 Lowenskyst, T8 Gransol, T17 Halvarshelm |

See calamity_radiation.md for full effects by RS band.

---

## Territory Map (17 Territories)

| T# | Name | Starting Control | Fort | Sub | Adjacent |
|---|---|---|---|---|---|
| T1 | Valorsplatz | Crown | 2 | Capital | T2, T5, T14, T16 |
| T2 | Kronmark | Crown | 1 | Heartland | T1, T3, T9, T14 |
| T3 | Lowenskyst | Crown | 3 (max 4) | Border Fortress | T2, T9, T17 |
| T4 | Grauwald | Varfell | 0 | Highland Timber | T7, T12, T14 |
| T5 | Feldmark | Crown | 0 | Breadbasket | T1, T6, T14 |
| T6 | Stillhelm | Crown | 0 | S. Farmland | T5, T13, T15 |
| T7 | Rendstad | Hafenmark | 0 | Timber Valley | T4, T8 |
| T8 | Gransol | Hafenmark | 1 | Hafenmark Capital | T7, T9, T10, T17 |
| T9 | Himmelenger | Church | 2 | Cathedral City | T2, T3, T8, T14, T17 |
| T10 | Spartfell | Hafenmark | 2 | Border Castle | T8, T11 |
| T11 | Halvardshelm | Varfell | 0 | Central Fjords | T10, T12 |
| T12 | Sigurdshelm | Varfell | 1 | Varfell Seat | T4, T11, T13 |
| T13 | Oastad | Varfell | 0 | Southern Fjords | T6, T12, T15 |
| T14 | Ehrenfeld | Crown | 3 (max 4) | Military Hinge | T1, T2, T4, T5, T9 |
| T15 | Askeheim | Uncontrolled | 0 | Southernmost | T6, T13 |
| T16 | Schoenland | Schoenland | 1 | Island Republic | T1 (sea) |
| T17 | Halvarshelm | Hafenmark | 0 | Northern Mines | T3, T8, T9 |

### Starting Control Summary

| Faction | Territories | Count |
|---|---|---|
| Crown | Valorsplatz, Kronmark, Lowenskyst, Feldmark, Stillhelm, Ehrenfeld | 6 |
| Varfell | Grauwald, Halvardshelm, Sigurdshelm, Oastad | 4 |
| Hafenmark | Rendstad, Gransol, Spartfell, Halvarshelm | 4 |
| Church | Himmelenger | 1 |
| Uncontrolled | Askeheim | 1 |
| Schoenland | Schoenland | 1 |
| **Total** | | **17** |

### Points of Interest (POI) — Per Territory

POI are discovered through the Survey action (fieldwork_v30 §8.1, BG Consul Inward). Each territory contains 1–4 undiscovered POI at game start. Categories: Resource, Secret, Remnant, Anomaly (see fieldwork_v30 §8.1 for BG bonuses).

**POI availability by RS band:**

| RS Band | Effect |
|---------|--------|
| 100–60 (Stable/Strained) | All categories discoverable. Standard Survey Ob. |
| 59–40 (Fragile) | Anomaly POI activate in territories at Proximity ≤ 2. +1 Anomaly per affected territory. |
| 39–20 (Fractured) | Remnant POI may shift location (1-in-6 at Accounting). Thread-scarred landscape reconfigures. |
| 19–1 (Critical) | Secret POI may self-reveal (1-in-4 at Accounting). Institutional collapse exposes hidden things. |

**Starting POI per territory:**

| T# | Territory | Res | Sec | Rem | Ano | Total | Rationale |
|----|-----------|-----|-----|-----|-----|-------|-----------|
| T1 | Valorsplatz | 1 | 1 | 0 | 0 | 2 | Capital trade hub |
| T2 | Kronmark | 1 | 0 | 1 | 0 | 2 | Crown heartland, old sites |
| T3 | Lowenskyst | 0 | 1 | 0 | 0 | 1 | Border fortress, military secrets |
| T4 | Grauwald | 1 | 0 | 1 | 0 | 2 | Highland timber, Einhir ruins |
| T5 | Feldmark | 1 | 0 | 0 | 0 | 1 | Breadbasket |
| T6 | Stillhelm | 0 | 1 | 1 | 1 | 3 | Calamity-proximate, Southernmost staging |
| T7 | Rendstad | 1 | 0 | 0 | 0 | 1 | Timber valley |
| T8 | Gransol | 1 | 1 | 0 | 0 | 2 | Trade city, Hafenmark capital |
| T9 | Himmelenger | 0 | 1 | 1 | 0 | 2 | Cathedral city, Church archives |
| T10 | Spartfell | 0 | 1 | 0 | 0 | 1 | Border castle, military intel |
| T11 | Halvardshelm | 1 | 0 | 1 | 0 | 2 | Fjords, old Einhir settlement |
| T12 | Sigurdshelm | 0 | 1 | 1 | 0 | 2 | Varfell seat, Niflhel presence |
| T13 | Oastad | 0 | 0 | 1 | 1 | 2 | Calamity-proximate, Einhir ruins |
| T14 | Ehrenfeld | 1 | 1 | 0 | 0 | 2 | Military hinge, Löwenritter |
| T15 | Askeheim | 0 | 0 | 2 | 2 | 4 | Calamity epicentre |
| T16 | Schoenland | 0 | 1 | 0 | 0 | 1 | Island, foreign secrets |
| T17 | Halvarshelm | 1 | 0 | 0 | 0 | 1 | Northern mines |

[EDITORIAL: ED-NEW-01 RESOLVED — POI catalog established. Specific POI content (names, narrative hooks, exact mechanical bonuses) deferred to per-territory design pass.]

### Adjacency Notes

- **Valorsplatz (T1):** 4 connections including Schoenland sea route. River-sea nexus, trade hub.
- **Lowenskyst (T3):** Primary Altonian land crossing. Fort 3 (max 4). 3 connections — chokepoint.
- **Sigurdshelm (T12):** Varfell Seat. Central hub of Varfell's territory (3 connections).

### Altonian Invasion Routes

| Route | Entry | Character |
|---|---|---|
| Primary (NE pass) | Lowenskyst (T3) | Main force from Altonian heartland |
| Secondary (NW pass) | Spartfell (T10) | Flanking force from periphery |
| Naval | Via Schoenland permission | At Institutional Pressure (IP) 75+: Schoenland grants passage |

### Southernmost Access


---

## Open Items from This Session

| ID | Description |
|---|---|
| ED-049 | Territory renames confirmed this session. Propagation needed across all docs. |
| ED-302 | Calamity radiation framework — RESOLVED 2026-04-06. See designs/setting/calamity_radiation.md. |
| ED-054 | Hafenmark food dependency — mechanical constraint needed. |
| ED-055 | Maritime Forgetting zone — mechanical specification for naval movement. |
| ED-058 | NW pass (Spartfell) Institutional Pressure (IP) delay value — confirm IP +10. |
| ED-061 | "Revolution" → "Restoration Movement" naming standardisation across all docs. |
| BALANCE-001 | Equal win probability for Crown/Varfell/Hafenmark requires asymmetric victory conditions. |
| BALANCE-002 | Varfell chain fragility — monitor in playtesting. Sigurdshelm is single point of failure. |
| BALANCE-003 | Himmelenger (Church) at 5 connections is kingmaker territory. |
| BALANCE-004 | Askeheim needs board game victory condition or scoring mechanic to justify existence. |
| BALANCE-005 | Hafenmark food dependency has no mechanical teeth — Feldmark unreachable by Hafenmark. |


[PROVISIONAL: compilation path references updated to _deprecated suffix — no content change]
