<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: geography_v30_infill.md -->

<!-- v30 baseline — renamed from designs/setting/geography_design.md on 2026-04-13 -->
# VALORIA — Geography & Territory Design
## Status: CANONICAL — approved 2026-04-05
## Scope: Physical geography, territory map (17 territories), adjacency graph, starting control
## Supersedes: compilation/v0.14/stage7_territories.md §7.2, §7.3

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
