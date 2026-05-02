# Combat Stress Test — Chunk 4/7
## Q2 — What is the spatial substrate of scene combat?

**Brief:** Canonical combat_v30 uses zone abstraction inherited from TTRPG framing — Melee range / Ranged distance, no maps or grids (§5 zone terminology). The videogame medium permits real space. This is the central question Jordan flagged: *moving away from the abstract zone of TTRPG means we have a lot to figure out for both TTRPG and mass battle.*

**Method:** NERS-all-directions per primary candidate. Five primary substrate choices (one must win at scene scale). Three orthogonal extensions evaluated separately.

---

## Primary substrate candidates

| ID | Substrate | Source reference |
|---|---|---|
| **S1** | Continuous euclidean 2D — free position, distance-as-real | RimWorld, Dwarf Fortress combat, Crusader Kings character scenes |
| **S2** | Square grid | XCOM 2, BG3, Wasteland 3 |
| **S3** | Hex grid with facing | Battle Brothers, Final Fantasy Tactics, King Arthur |
| **S4** | Slot / rank formation | Darkest Dungeon, Wizardry, Etrian Odyssey |
| **S7** | Zoned-but-mapped — canonical zones rendered as regions | Pillars of Eternity 2 (engagement zones), Dragon Age tactical pause |

(S5 side-on is for C duel only — covered as extension below. S6 hybrid and S8 elevation also extensions.)

---

### S1 — Continuous euclidean 2D

Free positioning on a 2D plane. Reach matrix becomes a distance threshold (Short = ≤1.5m, Long = ≤3m, Ranged = LoS only). Cover = LoS occlusion against geometry. Movement = free vector pathing. Group combat triggers from proximity clusters.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ✓ | Highest fit with videogame-medium intent; depth tax on legibility |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Reach matrix → distance threshold compose cleanly; weapon TN, damage, wounds unaffected |
| Vertical | ✓ | ✓ | ✓ | ✓ | **Same substrate hosts mass battle** (units as actors with footprint) — zoom is granularity, not mode-switch |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Fieldwork shares the map; combat erupting from fieldwork is mode-shift, not place-shift |
| Lateral | ✓ | ✓ | ⚠ | ⚠ | Social contest is conceptual (discourse, not space) — substrate is unused at lateral scale, not contradicted |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Map persists across campaign; battle sites accumulate history (post-combat fieldwork §11.5 native) |

**Verdict:** Highest-fit primary substrate. Strongest vertical scale-traversal of any candidate. Depth tax on UI legibility (continuous values are harder to display than discrete) — mitigated by visible reach indicators, cover icons, range rings.

**Mass-battle implication:** Mass battle adopts same substrate. Each unit is an actor with a position and footprint. Zone Collapse (§8) and Fibonacci trigger from proximity at unit scale. **Eliminates canonical "operational zones" abstraction in mass_battle_v30.** Cost: mass_battle spec rework. Payoff: scene↔mass is a granularity zoom, not a mode change.

**Reach matrix translation (concrete):**

| Canonical | Continuous distance |
|---|---|
| Short (S) reach | ≤ 1.5 m to target center |
| Long (L) reach | ≤ 3 m to target center |
| Melee range (engaged) | Within either reach threshold |
| Ranged distance | LoS to target, weapon-specific max range |
| Ranged at Close zone (Def TN 8) | Adjacent enemy melee threat present while wielding ranged |

---

### S2 — Square grid

Discrete tiles. Movement = N tiles per round. Reach = N adjacent tiles. Cover = tile occlusion + per-edge cover flag (XCOM full/half).

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Mature CRPG idiom; high legibility |
| Bottom-up | ✓ | ✓ | ✓ | ⚠ | Reach matrix → tile count is discrete; canonical Short/Long compose but lose nuance (a 1.6m positioning advantage doesn't exist) |
| Vertical | ⚠ | ⚠ | ⚠ | ⚠ | Mass battle on grid = unit-per-tile RTS-adjacent; loses the abstraction mass currently uses |
| Diagonal | ⚠ | ✓ | ⚠ | ⚠ | Fieldwork on grid feels 4X — different tone than freeform exploration |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other systems don't conflict (social is conceptual) |
| Horizontal | ✓ | ✓ | ⚠ | ✓ | Tile-by-tile scenes can feel rote across many encounters; mitigation: tile variety + terrain features |
| **Diagonal-tile asymmetry** | — | ✗ | — | ✗ | Square grids penalize diagonal movement (1.41× cost) — tactical artifact players exploit |

**Verdict:** Solid second choice. Strong legibility, but vertical (mass battle) and diagonal (fieldwork tone) frictions are real, and the diagonal-cost asymmetry is an awkward UX artifact every CRPG must paper over.

**Mass-battle implication:** Mass battle on grid would be tile-based RTS — fundamental rework, off-genre for Valoria.

---

### S3 — Hex grid with facing

Six-direction movement. Facing matters (front/flank/rear). No diagonal asymmetry.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ⚠ | Niche idiom (tactics genre); high tactical depth, lower mass-market legibility |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Reach + facing compose cleanly; canonical mechanics extend with facing modifier (net-new canon) |
| Vertical | ⚠ | ⚠ | ⚠ | ⚠ | Hex mass battle is wargame-traditional but visually different from rest of game |
| Diagonal | ⚠ | ✓ | ✓ | ⚠ | Hex fieldwork is 4X-style |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other systems unaffected |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Tactics scenes hold up over campaign with terrain variety |

**Verdict:** Better than S2 mechanically (no diagonal asymmetry, native facing) but **niche genre signal**. If Valoria positions itself as tactics-game-adjacent, hex is strong; if it's CRPG-with-sim, hex narrows the audience read.

**Mass-battle implication:** Hex mass battle (Total War: Warhammer-style at army scale) is feasible and traditional. Substrate match between scales.

---

### S4 — Slot / rank formation

No spatial substrate per se — position is rank index (1–4). Reach = rank-targeting rules.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ✗ | Combat scene becomes a UI mode separate from rest of game — substrate doesn't extend outside combat |
| Bottom-up | ✓ | ✓ | ⚠ | ✓ | Reach matrix translates to rank-targeting (Short = adjacent rank only; Long = +1 rank); canonical math intact |
| Vertical | ✗ | ⚠ | ✗ | ✗ | **Cannot host mass battle** — slot abstraction at army scale is meaningless |
| Diagonal | ✗ | ⚠ | ⚠ | ✗ | Fieldwork is on world map, combat enters slot mode — hard mode-switch with no spatial continuity |
| Lateral | ⚠ | ✓ | ⚠ | ⚠ | Slot UI doesn't share with social/investigation — three separate UI modes at personal scale |
| Horizontal | ✓ | ✓ | ⚠ | ✓ | Routine combat is fast (DD's strength); deep-tactical scenes feel constrained |

**Verdict:** **Cannot serve as primary substrate** because of vertical (mass) and diagonal (fieldwork) mode-switch costs. **Strong as B mode for routine combat** if Valoria adopts a multi-architecture stack — slot UI offers fast resolution for high-volume encounters while A handles set-pieces.

**Mass-battle implication:** Slots cannot host mass battle; if S4 is primary, mass battle needs an entirely different substrate — mode-switch tax recurs.

---

### S7 — Zoned-but-mapped (canonical-faithful)

Map regions are visible zones (rendered polygons or implicit areas). Within a zone, position is abstract (everyone in same zone is in melee range of each other). Movement = zone-to-zone transition. Reach matrix collapses to zone-membership + zone-edge ranged interaction.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ⚠ | ✓ | Closest to canon; legibility good; loses some emergent-positioning depth |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Canonical reach + zones map directly — minimal canon rework |
| Vertical | ✓ | ✓ | ✓ | ✓ | **Mass battle's operational zones reuse same primitive at larger scale** — clean vertical match |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Fieldwork POIs and combat zones are the same primitive; transitions are smooth |
| Lateral | ✓ | ✓ | ✓ | ✓ | Social contest can be zone-aware (court chamber, town square) without conflicting |
| Horizontal | ✓ | ✓ | ⚠ | ✓ | Zones across campaign are stable — but emergent-positioning narrative variance lower than S1 |

**Verdict:** **Highest canonical fidelity. Strongest vertical+diagonal scores.** Lower depth ceiling than S1 — within-zone positioning isn't expressive — but every other direction is clean. **Standout candidate alongside S1.**

**Mass-battle implication:** Mass battle uses larger operational zones. Same primitive, different scale. Zoom is just zone-resolution change. Canonical mass_battle_v30 already uses this — **zero rework needed at mass scale.**

---

## S1 vs S7 — the actual decision

These are the two passing primaries. The choice is between:

| | S1 continuous | S7 zoned-but-mapped |
|---|---|---|
| Player-felt depth | Higher — emergent positioning, micro-tactics matter | Lower — within-zone positioning is abstract |
| Implementation cost | Higher — pathfinding, LoS, projectile physics, continuous reach checks | Lower — zone graph, edge transitions, simpler LoS |
| Canonical rework | Mass battle spec needs rework | Near-zero — canonical zones already in place |
| Vertical scale-traversal | Seamless if mass battle also goes continuous | Seamless natively (mass already zoned) |
| Mass-battle interface | Granularity zoom | Resolution zoom |
| Reach matrix expressiveness | Full nuance (1.5m vs 3m matters) | Compressed (in-zone or not) |
| Cover system | LoS occlusion | Per-zone cover tags + edge-crossing rules |
| Fibonacci proximity check | Distance-radius cluster | Zone-membership count |
| Stunt opportunities | Emergent — any geometry feature | Authored — per-zone tagged opportunities |

**Composite read:** S7 is the **lower-risk, canon-respecting** choice with stronger vertical alignment and faster shipping. S1 is the **higher-ceiling, higher-cost** choice that opens emergent depth at the price of mass-battle rework.

**Recommendation:** **S7 with optional sub-zone positioning at scene scale only.** That is — the world is zoned (mass + fieldwork + scene all share the zone primitive), but within a scene-combat zone, *micro-positioning is enabled* (S1-style continuous within the zone). This is the **hybrid**: vertical scale uses zones; horizontal granularity at the scene tier uses continuous space within a zone. Canon-faithful at large scale, expressive at small scale.

This hybrid resolves the S1/S7 tension:

```
mass battle    = operational zones (canonical, mass_battle_v30 unchanged)
fieldwork      = world zones (canonical, fieldwork_v30 unchanged)
scene combat   = enters a single zone, opens a sub-zone continuous-space combat
                 with full reach matrix, cover, Fibonacci proximity
```

Mass-battle implication: zero rework at mass scale. Canonical operational zones survive. Scene combat earns continuous-space depth within a zone without imposing it on mass.

---

## Extensions (orthogonal additions)

### S5 — Side-on duel arena (single-axis)

C-architecture only. Already covered Chunks 1–2. Layers cleanly on S7-hybrid: a scene-zone tagged as "duel arena" opens a side-on view rather than top-down.

| Direction | N | E | R | S |
|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ |
| Bottom-up | ✓ | ✓ | ✓ | ✓ |
| Vertical | — | — | — | — |
| Diagonal | ✓ | ✓ | ✓ | ✓ |
| Lateral | — | — | — | — |
| Horizontal | ✓ | ✓ | ✓ | ✓ |

Within-scope of C; passes cleanly.

### S6 — Hybrid (different substrate per system)

Already absorbed into the S7-hybrid recommendation above. Not a standalone variant; it's the natural conclusion.

### S8 — Vertical / elevation in 2D top-down

Multi-floor buildings, towers, ramparts, mine shafts. Adds a Z-coordinate to the chosen 2D substrate.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | High depth payoff (fortress assault, cathedral interior, tower duels); UX cost on visualization |
| Bottom-up | ⚠ | ⚠ | ✓ | ⚠ | Cover and ranged become height-dependent; canonical Cover §5 needs height extension |
| Vertical | ✓ | ✓ | ✓ | ✓ | Maps to fortress tier in territory layer (siege § PP-088) — vertical substrate matches vertical scale concept literally |
| Diagonal | ⚠ | ✓ | ✓ | ⚠ | Stealth from above is new; fieldwork investigation across floors of a building is rich |
| Lateral | — | — | — | — | Other systems unaffected |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Vertical sites (towers, fortresses, mines) become signature scenes across campaign |

**Verdict:** **High-value extension to recommend** for important scenes (Himmelstift cathedral, Sankt-Athra towers, Eisengrund mines, fortress assaults). Author per-scene rather than required globally. Adds Stunt opportunities ("knock enemy off rampart"), reinforces canonical Environmental Factors (§5 wall climb), gives fortifications real videogame weight (PP-088 Siege Assault Linkage).

**Implementation:** simplest path is layered 2D — top-down view per floor, ramps/stairs/ladders as transitions between floors, ranged shots can target adjacent floors with TN penalty. Not 3D voxel — 2.5D layered.

---

## Cross-substrate Stunt translation (canonical §4 stunt mechanic)

Each substrate translates Stunt differently:

| Substrate | Stunt source | N range |
|---|---|---|
| S1 continuous | Player exploits geometry — "kick over brazier in path," "use pillar as cover-then-strike" | Engine determines from interaction tags; cap +5 canonical |
| S7 zoned (in-zone abstract) | Per-zone tagged opportunity list — author-curated | Zone-tagged values; cap +5 |
| S7-hybrid (sub-zone continuous) | **Both** — zone-tagged opportunities AND emergent geometry exploits within sub-zone | Combined; cap +5 |
| S2/S3 grid | Per-tile tagged opportunity | Tile-tagged values; cap +5 |
| S4 slot | Scene-tag predefined opportunity | Author-curated; cap +5 |
| S5 duel arena | Arena-set 1–2 deliberate Stunt opportunities | Author-curated; cap +5 |
| S8 elevation | All of the above + height-specific (push from height, drop on enemy) | Combined; cap +5 |

S7-hybrid + S8 = richest Stunt vocabulary.

---

## Mass-battle implications synthesis

| Substrate | Mass-battle impact | Cost |
|---|---|---|
| S1 continuous | Mass becomes continuous (Total War-style) — full rework | High |
| S2 grid | Mass becomes tile-RTS — full rework, off-genre | High + tonal |
| S3 hex | Mass becomes hex tactics — fits wargame tradition; rework | Medium |
| S4 slot | Mass cannot use slots — must adopt different substrate, dual-mode | High dual-tax |
| S7 zoned | Mass unchanged — canonical operational zones retained | **Zero** |
| **S7-hybrid (recommended)** | Mass unchanged; scene gains sub-zone continuous depth | **Zero at mass; medium at scene** |

The recommended S7-hybrid is the **only choice that requires zero mass-battle canonical rework** while still giving scene combat the spatial depth the videogame medium permits.

---

## Canon gaps surfaced (Q2)

1. **Sub-zone position spec.** Canonical §5 zone terminology (Melee/Ranged) is binary in-zone. S7-hybrid requires a sub-zone position model — net-new canon needed for "within-zone reach thresholds."
2. **Cover within zone.** Canonical Cover (§5) is a flat DR modifier. S7-hybrid sub-zone needs LoS-aware cover at sub-zone scale — extension to canonical table.
3. **Fibonacci proximity radius.** Canonical Fibonacci (§8) counts attackers per target without specifying spatial scope ("zone" implied). S7-hybrid needs explicit radius (e.g., melee threshold = 1.5m, count attackers within Long reach of target = 3m).
4. **Vertical/elevation extension.** S8 requires §5 Cover and Environmental Factors to support height — net-new rules for Z-axis.
5. **Stunt determination at sub-zone scale.** Already flagged in Q1 chunk; intersects with substrate decision.

---

## Godot implementation notes

- **S7-hybrid + S8** has tractable Godot path: TileMap or polygon-zone authoring at world scale; per-scene Node2D parent with continuous-position children for sub-zone; layered scenes (Y-sort or per-floor occluder masks) for elevation. Pathfinding inside sub-zones via NavigationAgent2D with reach-radius queries.
- Cover is the highest implementation cost — requires LoS raycasts every frame for every actor pair. Mitigation: occlusion only on action commit, not continuous.
- Reach-radius visualization (highlighting targets within Long reach of selected actor) is essential UX — inexpensive to implement.

End Chunk 4.
