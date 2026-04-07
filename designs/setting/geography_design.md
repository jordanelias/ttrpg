# VALORIA — Geography & Territory Design
## Status: CANONICAL — approved 2026-04-05
## Scope: Physical geography, territory map (17 territories), adjacency graph, starting control
## Supersedes: compilation/v0.14/stage7_territories.md §7.2, §7.3

---

## Physical Geography

Valoria occupies a north-south peninsula attached to a continental landmass. An east-west mountain range separates Valoria from the Empire of Altonia at the northern boundary. No navigable sea passage exists around the north. The peninsula narrows southward, terminating at the Southernmost — the epicenter of the Einhir Catastrophe.

### Terrain Regions

**Northern Mountains (east-west barrier):** Continuous range across the northern boundary. Two passes: Lowenskyst (NE, primary, Crown fortress) and Spartfell (NW, secondary, Hafenmark border castle). Altonian invasion funnels through these chokepoints unless Schoenland grants naval passage.

**Northwestern Highlands (Hafenmark):** Landlocked highland territory. Swiss in character. Rocky terrain, glacial lakes, mineral deposits, limited arable land, no coastal access. During Altonian occupation, Hafenmark was squeezed between Altonian-controlled mountains above and Altonian-controlled Valoria below — no coastal escape. Concentrated Altonian oversight (mineral wealth most valuable to empire) produced a cultural emphasis on institutional order, procedural compliance, and constitutional governance.

**Western Fjords (Varfell):** Norwegian in character. Deep fjord inlets, rocky coastline, isolated communities connected by sea. Varfell has port access (fjord harbours face west/southwest) but is commercially isolated — no sea route connects east coast to west coast. The northern landmass blocks circumnavigation above; the Forgetting blocks passage around the southern tip. Minor western ocean trade exists but is marginal. Low mountain ridges run north-south along the western third of the peninsula (Scandinavian mountain chain analogue — traversable but defining).

**Eastern Lowlands (Crown heartland):** Italian in character. A major river runs through Valorsplatz to the eastern sea. Fertile floodplain, farmland, accessible coastline. Valorsplatz sits at the river-sea junction — nexus for river transport, sea trade, and agricultural production. Schoenland's primary trade route terminates here.

**Central Peninsula:** South of the northern power centres, the peninsula narrows. Rolling farmland gives way to wilder country as the Calamity's influence increases. A large lake (Eidursjø) sits in the central-south interior, creating a natural barrier between the western and eastern southern corridors.

**The Southernmost (southern tip, offset southeast):** No cities. Einhir ruins, Locked Zones, Snapped Zones, Oscillating Zones. Calamity epicenter.

### Continental Context

Altonia occupies the continent east and north of the peninsula. Its heartland faces Schoenland and Lowenskyst (NE pass). The NW pass opens into Altonia's less populous periphery. Beyond Altonia to the northwest, other nations exist but cannot easily trade with Valoria due to Altonian naval and territorial control.

### Geographic Unity

Pre-Calamity: The Einhir site-network radiated from the Southernmost outward along both branches. Thread infrastructure connected west and east through the southern interior. Same language, same Thread practices, same cultural foundation. Regional differences are provincial, not national.

Post-Calamity: Neither half of the peninsula is defensible alone against Altonia. The peninsula is one country because geography demands it.

### Church Geography

The Church is a transnational institution. Altonia's dominant religious tradition (Almaic Kyriakos) could not stamp out the Church but could quarantine it. Himmelenger's location was an Altonian containment decision — place the Cathedral on the mountain ridge between the passes where it can be monitored and project inward. The Church's power in Valoria is a consequence of this concentration.

### Restoration Movement Geography

Strongest in the southwest (closest to Southernmost, strongest surviving Einhir folk practice). Creeps northeast. Weakest in Hafenmark (most thorough Einhir suppression during occupation). Roughly the inverse of Church influence.

### Maritime Forgetting Zone

The Calamity's Forgetting extends into coastal waters around the southern peninsula. No reliable sea route around the southern tip. East coast and west coast are separate maritime theatres. Schoenland cannot reach Varfell's western ports by sea. Varfell perceives this as Crown/Schoenland trade conspiracy — the rational explanation (Calamity blocks the route) is literally unrememberable without Thread Sensitivity (TS).

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

- **Ehrenfeld (T14)** and **Himmelenger (T9)** are the most connected territories (5 each). Ehrenfeld is Crown's military hinge; Himmelenger is the Church's crossroads position on the mountain ridge.
- **Valorsplatz (T1):** 4 connections including Schoenland sea route. River-sea nexus, trade hub.
- **Lowenskyst (T3):** Primary Altonian land crossing. Fort 3 (max 4). 3 connections — chokepoint.
- **Spartfell (T10):** Hafenmark border castle. Fort 2. Secondary Altonian crossing (NW pass). The Spartfell-Halvardshelm (T10-T11) border is the Hafenmark-Varfell contact point.
- **Sigurdshelm (T12):** Varfell Seat. Central hub of Varfell's territory (3 connections).
- **Askeheim (T15):** Two gates — Oastad (T13, Varfell) and Stillhelm (T6, Crown). Sea approach blocked by maritime Forgetting.
- **Schoenland (T16):** Island. 1 connection (Valorsplatz, sea). Naval dominance controls Altonian sea access.
- **Lake Eidursjø:** Natural barrier in the central-south interior. Prevents direct connection between western Varfell territories and eastern Crown farmland.

### Altonian Invasion Routes

| Route | Entry | Character |
|---|---|---|
| Primary (NE pass) | Lowenskyst (T3) | Main force from Altonian heartland |
| Secondary (NW pass) | Spartfell (T10) | Flanking force from periphery |
| Naval | Via Schoenland permission | At Institutional Pressure (IP) 75+: Schoenland grants passage |

### Southernmost Access

Askeheim (T15) accessible from Oastad (T13, Varfell — Gate 1) and Stillhelm (T6, Crown — Gate 2). Sea approach blocked by Forgetting. Vaynard controls one gate; Crown controls the other.

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
