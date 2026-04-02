# BAL-BG-01 — Board Game Win Probability Balance Analysis
## Date: 2026-04-02
## Status: COMPLETE — 6 patches applied

### Method
Per-faction analysis: deeds achievable from starting state, seasons to win at median play, structural blocking exposure, win probability index.

### Starting State
TC 28, RS 72, IP 20, PI 5. Standard 12-16 round game.

### Pre-Patch Win Index
| Faction | Index | Primary Blocker |
|---------|-------|-----------------|
| Crown | LOW-MEDIUM | Torben Loyalty Clock undefined state if IP < 30 |
| Church | LOW (structural) | Valorsplatz requires TC 70+ military seizure; ~S28+ |
| Hafenmark | MEDIUM | Church Excommunication attacks both Deed 1 and 3 |
| Varfell | MEDIUM | Intel 6 requires ~16 seasons; exceeds standard game |
| Guilds | MEDIUM-LOW | Favour grind slow; military vulnerability |
| Niflhel | MEDIUM | Intel advancement undefined |

### Patches Applied
PP-171: Church Deed 4 — 'Control Valorsplatz' -> 'Crown Mandate <= 2 for 2 consecutive seasons'
PP-172: Crown Deed 4 — Add 'OR Institutional Pressure < 30 at game end' escape clause
PP-173: Intel advancement mechanic defined (+0.25/successful Intel season)
PP-174: Mandate recovery defined (Govern Overwhelming in own capital = +1 Mandate)
PP-175: Guild Favour advancement explicitly stated
PP-176: Varfell Deed 1 — Intel 6 -> Intel 5

### Post-Patch Win Index
| Faction | Index | Seasons to Win (median) | Notes |
|---------|-------|------------------------|-------|
| Crown | MEDIUM | 8-12 | Deed 4 now checkable even if IP stays low |
| Church | MEDIUM | 10-14 | New Deed 4 contested via Excommunication vs Crown Govern recovery |
| Hafenmark | MEDIUM | 6-10 | No structural change; TC suppression mechanically viable |
| Varfell | MEDIUM | 8-12 | Intel 5 achievable S8-10; alt path via Revolution viable earlier |
| Guilds | MEDIUM | 8-12 | Favour advancement now explicit; T8+T11 hold is militarily risky |
| Niflhel | MEDIUM | 6-10 | Intel 5 achievable S8 with consistent Intel ops |

### Remaining Notes
- Guilds remain militarily vulnerable (Military 2). P2 balance note: if Crown or Varfell pursues T8/T11, Guilds cannot defend. This is asymmetric design (economic faction), not a structural break.
- Church-Crown dynamic is now the load-bearing rivalry for TC and Mandate tracks. This is thematically correct.
- Hafenmark Deed 4 ('Parliamentary ruling') remains mechanically undefined — PG-10 open gap.
- Niflhel Deed 3 (hidden info persistence) remains undefined — PG-12 open gap.

### Params Gaps Still Open
PG-10: Parliamentary ruling mechanic — what action produces a ruling token?
PG-12: Hidden information persistence — does revealed info expire?
PG-09: Torben Loyalty Clock advancement/decrease mechanics (partial — Clock starts at 8 on I-01, but what reduces it beyond coup tracker cross-refs?)
