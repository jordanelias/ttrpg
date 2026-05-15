# Mass Battle Comparative Audit — Pre-Firearms Research × Canon × Sim v25

**Date:** 2026-05-15
**Session token:** b855617689574332
**Scope:** Mass battle only. Personal combat, social contest, peninsula-strategic resolution beyond `peninsular_strain_v30 §3` excluded.

**Corpora compared:**
- **R** — `research/pre_firearms_formations/` parts 09–16 (synthesis: throughlines T-1..T-43, meta-throughlines M-1..M-13, 13-class matchup matrix, 8-phase framework, 9 battle reconstructions).
- **C** — `designs/provincial/mass_battle_v30.md` (SHA `2a1211d3`, canonical 2026-04-17) + `params/mass_combat.md` + `designs/provincial/military_layer_v30.md` + `designs/provincial/peninsular_strain_v30.md` + infill.
- **S** — `tests/sim/sim_mb_06_v25.py` (2,415 lines) + `sim_mb_06_v16_manifest.md` + `audit_sim_mb_06_v16.md` + `sim_mb_06_handoff_2026-05-12.md`.

**Methodology:**
1. Per-domain extraction from each corpus with citations.
2. Three-way comparison table (Aligned ✓ / Partial ~ / Conflict ✗ / Silent ∅).
3. Bottom-up sanctity check — every mechanic must compose up from primitives; no top-down recognition (M-9 anti-pattern).
4. Top-down historical validation against R's 9 reconstructions.
5. Lateral gameplay validation against acclaimed precedents.
6. Throughlines surfaced (continuing T-/M- sequence from T-44 / M-14 onward).
7. Severity-tagged findings (P1 correctness-critical / P2 significant unspecified intersection / P3 polish).

`[SELF-AUTHORED — bias risk]` Author contributed to R audit files 11/14/15/16. Independent reviewers may prioritize differently.

---

## Chunk 0 — Framing & Inventory

### Three corpora

**R · Research** — Tactical-layer pre-firearms warfare across ~2,750 years. Operational deliverables: 8-phase framework (Approach → Pursuit), 13-formation matchup matrix, 43 throughlines, 13 meta-throughlines, 13 gameplay opportunities, 9 moment-by-moment battle reconstructions with primary-source citations (Cannae, Pharsalus, Adrianople, Hastings, Crécy, Agincourt, Marignano, Pavia, Panipat). Already self-audited in files 11, 14, 16.

**C · Canon** — `mass_battle_v30.md` three-mode (TTRPG / Hybrid / Board Game): Part A §A.1–§A.14 zoom-in, Part B §B.1–§B.5 board-game form, §B.5 Hybrid Handoff, Part D world bridge, Part E battle consequences. Plus `params/mass_combat.md` (PP-233 core formula, DR tables, weapon effectiveness, ~50 PP patches), `military_layer_v30.md` (board↔mass bridge), `peninsular_strain_v30.md §3` battle-consequence cascade.

**S · Sim** — Cell-level implementation. 41×42 connected battlefield, 21×41 per-unit grid, 19×11 formation area. Five canonical spatial patterns (Line / Arrowhead / Horseshoe / GappedLine / RefusedFlank). Continuous TroopCount HP at BLOCK_SIZE=100. F-i cell-support stacking + F-ii puncture momentum + F-iii cascading sub-phase resolution + v25 octagon (GREEN/YELLOW/RED) + sightline arc (135°, 15 cells) + ANGLE_DMG_MULT + FLANKED_BONUS + attention split. Multi-turn orchestrator + multi-unit battle with morale cascade / freed-attacker / pursuit / recall.

### Chunking plan

| # | Domain | Status |
|---|---|---|
| 0 | Framing & inventory | **committed (this commit)** |
| 1 | Scale, geometry, phase structure | **committed (this commit)** |
| 2 | Unit primitives + formation taxonomy | next |
| 3 | Resolution mechanics + command/timing | pending |
| 4 | Cohesion → rout → pursuit pipeline | pending |
| 5 | Environment / terrain | pending |
| 6 | Thread integration | pending |
| 7 | Force generation / supply / levy / reinforcement | pending |
| 8 | Scale transitions + consequences propagation | pending |
| 9 | Doctrine-substrate-opponent + cultural filter + perfect-system trap | pending |
| 10 | Cross-corpus throughlines synthesis | pending |
| 11 | Cross-corpus meta-throughlines synthesis | pending |
| 12 | Findings consolidation + recommendations | pending |

### Tag convention

New throughlines start at **T-44**, continuing the file-9/file-14 sequence. New meta-throughlines at **M-14**. Findings use `F<chunk>.<n>` numbering with severity tags per PI.

---

## Chunk 1 — Scale, Geometry, Phase Structure

### Scope

Battle scale (troops, tile, time), battlefield geometry (frontage, depth, buffers, sightline), phase structure (count, duration, sequencing). Excludes phase content (Chunks 3, 4, 7) and force composition (Chunk 2).

### Primitives at this layer

| Corpus | L0 atomic | Aggregation |
|---|---|---|
| R | Soldier (T-42 free param; 10–50 historical per L0 recommended) | Files × ranks → formation footprint |
| C | Soldier → block_size → Size 1 (`§A.3`; PP-235); T1–T4 = 100/200/400/800; Company scale | TroopCount = Size × block_size |
| S | Soldier as HP unit (`BLOCK_SIZE=100`); cell as positional atom | TROOPS_PER_TIER → Size → HP = TroopCount; effective_size = HP / BLOCK_SIZE (continuous) |

All three ground at the soldier level. HP-as-TroopCount in S means damage = casualties; no scaling indirection. **Bottom-up substrate aligned.**

### R says

**8-phase descriptive framework** (file 10 §I): Approach → Deployment → Skirmish → Missile attrition → Main contact → Decisive commit → Collapse → Pursuit. Total active combat 2–9 hr; typical 3–6 hr.

**Spatial reference values** (file 10 §V, file 12 §IV):
- First-contact distance: 250–800 m.
- Skirmish zone: 50–300 m forward of main line.
- Killing arc: 30–250 m weapon-dependent.
- Lethal density step-change at compression: ~12–20 m²/man.
- Cavalry final gallop: 30–50 m only (non-sustainable).
- Decisive commit window: 5–30 min clock time — single most important phase per M-4.

**Manual primitives** (file 12 §II): Hellenistic `pyknōsis` 0.9 m/file; `synaspismos` 0.45 m/file; sarissa-phalanx 16 ranks deep; Roman cohort 4–5 deep at 0.9 m/legionary; Swiss Gewalthaufen 60–70 m square at 16+ ranks; Mongol 5-deep at ~200 m / 1,000 men.

### C says

**Battle scale** (`mass_battle_v30 §A.3`; `params/mass_combat.md §Battle Scale`): Size 1 = block_size soldiers; T1=100, T2=200, T3=400, T4=800; Company scale specified.

**Battlefield geometry** (`§A.3b`, 2026-05-15): 41×42 connected map; 41×21 per-unit grid; 19×11 formation area; 11-cell side buffers + 5-cell front/back. Sightline = 135° arc × 15-cell range from cell facing octagon.

**Phase structure** (`§A.7` revised 2026-04-02 ED-050; PP-235): seven-phase consolidated to five — **Planning → Volley → Manoeuvre → Offensive Thread → Engagement → Cascade**. Offensive Thread elevated to its own phase between Manoeuvre and Engagement (ED-050 Option D). Volley + Thread + Engagement damage applied simultaneously at Cascade Phase 6 Step 1.

**Engagement cap** (Jordan direction; S v22 header): 3 phases per simultaneous engagement per battle turn. Battle = 5–8 battle turns.

### S does

**Geometry constants** (lines 171–200): `BATTLEFIELD_HEIGHT=42`, `WIDTH=41`; `UNIT_GRID_HEIGHT=21`; `FORMATION_AREA_WIDTH=19`, `DEPTH=11`; `FRONT_BACK_BUFFER=5`; `SIDE_BUFFER=11`; `WING_LATERAL_BUFFER=3`. Sightline: `SIGHTLINE_ARC_HALF=67.5°`, `SIGHTLINE_DISTANCE=15` — exact match to C §A.3b.

**Scale constants** (lines 209–247): `TROOPS_PER_TIER = {1:100, 2:200, 3:400, 4:800}`, `BLOCK_SIZE=100` — exact match to C.

**Time structure** (line 238): `TICKS_PER_PHASE=6`; `run_battle(max_turns=18)` = 3-phase engagement cap; `run_multi_turn_battle(max_battle_turns=8)` = canonical 5–8 turns.

**Position anchors** (lines 198–200): A formation center row 31, B at row 10; col 20 centered → 21-row separation at start.

### Three-way comparison

| Element | R | C | S | Alignment |
|---|---|---|---|---|
| Soldier → unit aggregation | T-42 free param | Size × block_size | BLOCK_SIZE=100, TROOPS_PER_TIER | ✓ all three |
| Battlefield extent | 1–3 km frontage at scale | 41×42 cells | 41×42 cells | C↔S ✓ exact; R↔C/S ✓ if cell ≈ 50 m |
| Side buffer | Mongol 200 m/1k men implies wide deployment | 11-cell side buffers | SIDE_BUFFER=11 | C↔S ✓ exact |
| First-contact distance | 250–800 m | Not specified | 21-cell separation = ~1.05 km @ 50m/cell | R↔S close at upper band |
| Phase count | 8 descriptive | 5 mechanical (PP-235) | 18-tick engagement turn | Different abstraction layers — T-45 |
| Decisive-commit phase | R Phase 5; 5–30 min window; M-4 universal command skill | Reserve formation (§A.6) — commits Phase 3 of N+1 | Reserve mechanic **absent** | **C↔S drift, F1.1 P1** |
| Collapse phase | R Phase 6 distinct | Folded into morale ≤ 0 → routed | `rout_resolution` line 364 | R↔C/S ~ partial |
| Pursuit phase | R Phase 7 — bulk of casualties | §A.12 Fast-only | `pursuit_damage`, `recall_check` lines 2067–2108 | R↔C/S ✓ principle; severity not yet calibrated — F1.5 |
| Sightline | Implicit (scouts 1–20 km) | 135° / 15 cells (§A.3b) | SIGHTLINE 67.5° / 15 cells | C↔S ✓ exact; R↔C/S aligned |
| Cavalry final gallop | 30–50 m only | Not specified | Cavalry deferred (G-11) | F1.2 |
| Lethal density step-change | 12–20 m²/man at compression | Not specified | Continuous damage; no compression multiplier | R↔C ∅; R↔S ∅; F1.3 |
| Total battle duration | 2–9 hr; typical 3–6 hr | 5–8 battle turns | max_battle_turns=8 default | C↔S ✓ exact |

### Bottom-up sanctity check

| Element | Bottom-up? | Where the primitive lives |
|---|---|---|
| HP = TroopCount; damage = casualties | ✓ S | `__post_init__` line ~1193 |
| effective_size continuous | ✓ S | `recalc_size` line 1206 |
| Sightline → flanking emerges | ✓ C+S | `in_sightline` 583–616 + `_rotate_defender_facing` 699–747 |
| 5 spatial patterns → matchups emerge | ✓ S | `CELL_PATTERN_FN` line 535; per-shape combat mods all zero (lines 460–469) |
| Cell speed → per-cell movement → momentum | ✓ S | `cell_speed` 776 |
| Buffers → maneuver room | ✓ C+S | `SIDE_BUFFER=11` enables Horseshoe wide-wing wrap |
| Phase=6 ticks; turn=3 phases | ~ C+S | Time-structure primitive; `TICKS_PER_PHASE` is constant not derived |
| Lethal density step-change | ✗ S | Not modeled — F1.3 |
| Decisive commit timing | ✗ S | Reserve formation canonized in C but absent from S — F1.1 |
| Cavalry gallop limit | ∅ S | Deferred G-11 — F1.2 |

**Verdict:** Chunk 1 substrates predominantly bottom-up. No top-down macro-recognition rules — all three corpora respect M-9. Three structural gaps (commit-window absent from S despite C canonization, lethal-density compression, cavalry physical limits).

### Top-down historical validation

Against R's 9 reconstructions, using Chunk 1 primitives only:

| Battle | Critical Chunk-1 element | S reproducible structurally? |
|---|---|---|
| Cannae | Convex deploy → envelopment → compression damage | ⚠ Envelopment YES; compression NO (F1.3) |
| Pharsalus | Hidden 4th-line reserve → commit-timing ambush | ✗ Reserve absent from S despite C canonization (F1.1) |
| Adrianople | Cavalry encirclement → pocket compression | ⚠ Outflanking YES; compression NO (F1.3) |
| Hastings | 9-hr battle, slope, repeated cycles | ⚠ Multi-turn YES; slope NO (Chunk 5); feigned retreat NO (Chunk 2 F2.5) |
| Crécy | Slope + longbow attrition + stakes | ⚠ Volley + DR YES; slope/stakes NO (Chunk 5) |
| Agincourt | Funnel + missile + mud + dismounted heavy | ⚠ Volley YES; funnel/mud NO (Chunk 5) |
| Marignano | Overnight pause + artillery + arquebus | ⚠ between_turn_recovery partial; artillery NO |
| Pavia | Park-wall breach + arquebus cover | ✗ Terrain/concealment NO (Chunk 5) |
| Panipat | Wagon-line + tulughma + firearm shock | ✗ Fortification NO; sally-points NO |

**Direction surfaced:** F1.1 (Reserve) unlocks Pharsalus; F1.3 (compression) unlocks ~4 of 9; Chunk-5 terrain unlocks the prepared-ground reconstructions. Chunk-1 primitives alone don't *block* any reconstruction — the gaps are at adjacent layers.

### Lateral gameplay validation

| Precedent | Phase model | Reserve mechanic | Sightline | Field scale | Valoria relation |
|---|---|---|---|---|---|
| **Total War** (Medieval II, Three Kingdoms, Rome II) | Continuous real-time; phases emergent | "Hold" stance + cavalry-charge-as-commit | Visibility cone + height occlusion | Continuous m, ~2 km maps | Different paradigm (RT vs tick) but comparable field scale |
| **Ultimate General: Civil War** | Continuous real-time | Reserve formation + commit timing | Line-of-sight + smoke | Continuous m, ~2 km maps | Acclaimed for reserve — Valoria currently lacks |
| **Field of Glory II Digital** | Turn-based, 1 turn = 1 phase | Reserve units explicit, "Wait" order | Line-of-sight + facing | Hex ~100 m | Closest hex precedent; FoG2 has 3-state reserve (held/committed/spent) |
| **Combat Mission** (WEGO) | 1-min turns, simultaneous orders | Cover/move/halt orders | Per-unit vision modeled | Continuous m, 1 km² | Same simultaneous-resolution paradigm; Valoria 5-min ticks comparable |
| **Mount & Blade Bannerlord** | Real-time + formation orders | Hold-position + manual commit | Visibility cone | Continuous m | Commander-as-character (different scope); explicit reserve hold |
| **Unicorn Overlord** (Vanillaware 2024) | Pre-battle squad construction + auto-resolved tactical encounters; no per-phase player control during combat | Squad composition IS reserve — players assemble 3–5 unit squads before deploying on strategic map; positioning within squad ↔ "row" | Strategic-layer all units visible; tactical layer auto-resolved | Strategic map = field; tactical encounters in instanced ring | Valoria's tactical engagement layer is what UO compresses to ~3 seconds of animation per encounter; UO validates pre-battle-tactical-setup model |
| **Football Manager** (SI Games) | 90-min match real-time/accelerated + pre-match instructions + half-time pause + sub windows | Bench substitutions (3–5/match); squad rotation across season; in-match tactical changes | Per-player Vision attribute affects passing decisions (bottom-up emergence) | 105×68 m pitch with continuous positioning | FM = canonical bottom-up squad-scale simulation; Valoria mass battle adopts similar emergence philosophy at Company-scale; **FM's match engine validates 90-min-with-half-time ≈ 5–8 turns with between_turn_recovery** |
| **Phantom Brigade** | 5-sec turns + time-scrub preview | N/A | Sensor | Continuous m | **Counter-example: time-scrub conflicts with T-9/T-10** — Valoria's blind simultaneous resolution correctly avoids this (P1 in R file 16) |

**Verdict laterally:**
- Valoria's tick-based simultaneous-resolution + per-cell sightline + 3-phase engagement cap occupies a defensible niche between FoG2 (turn-based) and Combat Mission (1-min WEGO).
- Per-cell sightline (135°/15-cell) is comparable to Total War's visibility cone and FoG2's facing-and-LOS — historically grounded.
- **The conspicuous lateral gap is reserve management.** Total War, Ultimate General, FoG2, Bannerlord, Unicorn Overlord squad composition, FM bench substitution — every comparable game exposes reserves as first-class. Canon §A.6 already specifies it. S does not implement it. This is F1.1 P1.
- **FM specifically validates bottom-up sanctity at squad scale.** SI's match engine is famous for outcomes emerging from per-player attributes + tactics + situation, never from "this is a counter-attack" scripted recognition. Valoria's M-9 (no top-down macro recognition) is the same discipline applied to mass battle. Acclaimed precedent for the design philosophy.
- **UO validates pre-battle tactical setup with bottom-up auto-resolution.** Players configure each unit's behavior tree before combat ("Use [skill] when [condition]"). Once deployed, combat resolves automatically per those rules + position + stats. This validates Valoria's hybrid model (B.5) where strategic-layer combat can auto-resolve when zoom-in isn't desired.

### Throughlines surfaced (Chunk 1)

- **T-44 (R/C/S) — Cell ≈ 50 m is the implicit metric substrate.** C's 41×42 grid + 11/5-cell buffers + 15-cell sightline maps coherently to R's "1–3 km frontages with skirmishers 50–300 m forward" only at ~50 m/cell. Never explicit in C. `[ASSUMPTION: cell ≈ 50 m — basis: 41 × 50 = 2.05 km field matches R typical-army frontage; 15-cell sightline = 750 m matches R reconnaissance-by-eye range; 50 m² × ~2.5 m²/man = ~25 men/cell densest, ~5 open — both plausible.]`

- **T-45 (R/C/S) — 8-phase R framework and 5-phase C/S framework operate at different abstraction layers.** R describes *what observers see across the battle's duration*; C/S describes *what resolves within a turn*. Mapping mostly clean except R Phase 5 (Decisive Commit) has no direct C/S analog at the phase level — it lives in C as the Reserve formation (§A.6), which is a unit-state primitive operating across turn boundaries (Phase 3 commit → Phase 5 engage next turn). Cross-layer mapping is coherent; absence in S is implementation drift, not design drift. See F1.1.

- **T-46 (C/S) — The 3-phase engagement-turn cap is a stamina/cohesion budget, not a commit-window primitive.** Jordan's directive "limit of 3 phases per simultaneous engagement per turn" produces stamina-exhaustion + disengage-and-reform dynamics across battle turns. Structurally distinct from R's decisive-commit window (one-shot per battle). The 3-phase cap reproduces hoplite-style rotation cycles (Hastings); the commit-window mechanic (Reserve, canonized in C) reproduces Pharsalus-style hidden-reserve ambush. **Both primitives needed — they are not interchangeable.**

- **T-47 (C/S validates R/M-9) — Sightline geometry is the bottom-up mechanism producing R's flanking patterns.** R T-7 (Mongol mangudai), T-25 (Cannae closure), Hastings shield-wall depletion all require defenders not perceiving attackers. C/S 135°/15-cell sightline + facing rotation only toward visible attackers (`_rotate_defender_facing` 699–747) produces this emergently. No "is this flank?" recognition. **M-9 done right.**

### Findings (Chunk 1)

**F1.1 — P1 (C↔S):** Reserve formation canonized in C §A.6 (+ PP-MB-04, PP-499 clarification) — "Cannot engage; commits at Phase 3 start of NEXT turn; commitment at Phase 3 of Turn N+1 makes the unit immediately available for Phase 5 Engagement that same turn." **S has no Reserve mechanic.** This is C→S correctness drift on an existing ratified canon mechanic. Pharsalus structurally non-reproducible. Severity P1 because canon→sim drift on a named mechanic blocks T-39 phase-1 validation for any battle where Reserve is decisive.

*Resolution path (bottom-up):* Add `committed: bool = False`, `commitment_pending: bool = False` to `Unit`. Reserve unit: doesn't advance, doesn't engage, doesn't drain stamina. Order "Commit at Phase 3 N+1" → `commitment_pending = True`. At Phase 3 of N+1: `commitment_pending → committed=True`. From Phase 5 N+1 onward unit operates normally per existing primitives. Reserve first-engagement Off/Def split = equal (round down to Off) per C §A.6 clarification. No top-down recognition; mechanic is generic.

**F1.2 — P3 (R↔S):** Cavalry final-gallop physical constraint (30–50 m only). When G-11 cavalry lands, F-ii puncture momentum (line 1483) should respect *peak speed sustains ~1 cell, then degrades to canter (~2 cells), then trot*. Bottom-up: emerges from `max_gallop_distance` per cell, not from cavalry-class special rule. Design the constraint into G-11 from the start.

**F1.3 — P2 (R↔C↔S):** Lethal-density step-change at compression absent. R T-32 explicit: "linear casualty math cannot produce Cannae, Adrianople, Agincourt, Panipat." S continuous-TroopCount damage is mechanically smooth; lacks non-linear spike when a unit is pressed into smaller area than its formation footprint can use. Highest-leverage primitive missing — unlocks ~4 of 9 reconstructions structurally.

*Resolution path (bottom-up):* Track `available_free_cells` per unit per tick (cells within unit's grid not occupied by friendly or enemy). When `free_cells < cells_in_contact × compression_threshold`, apply damage multiplier scaled by compression ratio (1.0–2.0×). Emerges from cell-count primitive; no "this is encirclement" recognition.

**F1.4 — P3 (C↔S):** Cell-to-meter conversion implicit. Recommend canonizing cell ≈ 50 m in `mass_battle_v30 §A.3b` for stable metric anchor (cavalry gallop window, missile range bands, terrain feature scales).

**F1.5 — P3 (R↔C↔S):** Collapse phase (R Phase 6) not differentiated from Pursuit (R Phase 7) in C/S. R F2 §VI O-10 casualty asymmetry (5–15% winner / 30–60% loser, most losses in 6–7) relies on collapse + pursuit being distinct from main-contact attrition.

*Resolution path (bottom-up):* When morale crosses low threshold (e.g., 0 < morale ≤ 1.0), apply wavering-damage-multiplier to engagement damage taken. Emerges from morale primitive. Threshold tuned, not asserted.

### Carried forward

- **F1.1 (Reserve)** → Chunk 2 (formation taxonomy) — covered as F2.4 with full canon-axis treatment.
- **F1.3 (compression damage)** → Chunk 4 (cohesion/rout) — compounds with morale erosion.
- **F1.4 (cell-scale)** → Chunk 5 (environment) — terrain feature scales need stable metric anchor.
- **F1.5 (collapse distinct from pursuit)** → Chunk 4.

---

## Chunk 2 — Unit Primitives + Formation Taxonomy

`[SELF-AUTHORED — bias risk]` per Chunk 0 framing.

### Scope

What constitutes a unit (stat block, primitives); what constitutes a formation (taxonomy, modes, spatial patterns); how the three corpora encode unit-class diversity. Excludes pool / damage / RPS resolution (Chunk 3) and cohesion / rout (Chunk 4).

### R says

**13 formation classes** (file 9 §III): Heavy cavalry shock · Light cavalry / horse-archer · Mixed cavalry · Heavy pike · Shield-wall heavy infantry · Sword-and-shield modular · Defensive pike circle (schiltron) · Mass missile infantry · Skirmisher light infantry · Wagon-fortress / field fortification · War elephants · War chariots · Pre-Columbian elite infantry. Each class is a composition of {weapon, armour, training tier, equipment-dependent role}. The matchup matrix (R F1 §III tiered, ~30 pairwise findings) is keyed on these classes.

**Stat / primitive guidance:**
- T-32 — Step-change non-linearities are first-class primitives (lethal density ~12–20 m²/man).
- T-33 — Facing as first-class primitive (frontal / flank / rear arcs not equivalent).
- T-35 — Sub-tile vector positions preserve dynamic-spacing fidelity.
- T-42 — Soldier-abstraction granularity is a free parameter; what matters is L0 stability.
- T-43 — Order-of-magnitude calibration sets all derivative scales.

**M-1 application (doctrine triangle):** every class is the product of substrate × opponent-menu × cultural-victory-conditions. Class is not portable in isolation — it brings its institutional substrate.

### C says

**§A.4 Unit Stat Block** (all 1–7):
- **Size** — `floor(TroopCount / block_size)`. TroopCount = granular health; Size = integer for combat formulas. Size 0 = destroyed (ED-694).
- **Power** — dice pool ceiling. Tier mapping: 1 Levy, 2 Militia, 3 Professional, 4 Veteran, 5 Elite, 6–7 Exceptional / Peerless.
- **Discipline** — organizational integrity. Starting = `min(general's Command, Military ceiling)`. **Deterministic degradation (PP-502/PP-251):** Discipline −1 when Size lost this turn > current Discipline AND own loss exceeds opposing loss by ≥ 1. Effective Power penalty: 5–7 none, 3–4 −1D, 1–2 −2D, 0 broken.
- **Morale** — rout threshold (1–7). Starting = general's Command + quality modifier (cap 7). Multiple triggers (Size <50%, Size <25%, Discipline broken, allied unit routed, general incap/killed, flanked-and-lost-exchange, idle). Cap −3 per Cascade Phase except general-kill Stage-2 −2 additive. Encirclement exception (PP-683): cap removed when no valid retreat path. Floor = 1 while general present.
- **Speed** — Slow / Standard / Fast (3 tiers).

**Faction Military stat → unit quality** (FACTION-P2-01 fix, §A.4): Military N caps Max Power at N and Starting Discipline at N+1 (saturating at 7).

**§A.5 Command** — `⌈(Charisma + Cognition) / 2⌉`. Governs: sub-unit limit (cap 3 TTRPG), Discipline ceiling, Morale floor, Tactic Ob rolls. NPC generals assigned directly (Command-P2-02). Two-stage general death (P1-02). Bilateral personal combat (PP-506): both armies fight uncommanded at PP-273 minimum until re-establishment.

**§A.6 Formation Types** — 7 distinct combat modes:

| Formation | Off | Def | Special |
|---|---|---|---|
| Line | Normal | Normal | Standard |
| Shield Wall | −1D | +2D | Cannot advance; negates one flanking direction per turn (PP-500: +2D applies to all simultaneous engagements) |
| Wedge | +2D | −1D | Negated by Shield Wall |
| Skirmish | Normal | Normal | Cannot be flanked; −1D vs Heavy infantry |
| Column | — | — | +1 Speed tier; movement only, cannot engage |
| Feigned Retreat | — | — | See Tactics; PP-256 pursuer Discipline Ob 1 |
| Reserve | — | — | Cannot engage; commits Phase 3 of Turn N+1, available Phase 5 same turn |

**§A.8 Tactics** — 6 declared maneuvers:

| Tactic | Effect | Ob | Counter |
|---|---|---|---|
| Envelopment | All-flank attempt; requires Fast | 2 | Refused Flank |
| Feigned Retreat | Disengage → pursuer Disc check → re-engage with flank next turn | 3 | Cmd Ob 2 to recognise |
| Ambush | First engagement: defender no Defence allocation | 4 | Scouting check |
| Concentration | All sub-units one target; max Fibonacci | 1 | Flanks exposed |
| Refused Flank | Wing anchored on terrain; immune to that flank | 1 | Sacrifices offence |
| Hammer & Anvil | Shield Wall holds + Fast envelops | 3 | Break Anvil first |

Splitting doctrine (PP-508): split dominates concentration by +9–45% win-rate except (a) Narrow Pass terrain limits engagements, (b) sub-unit Size at PP-273 floor.

**`military_layer_v30.md §1.2-1.3`** — Unit token represents 80–800 soldiers (Company–Battalion); per-unit Power gated by faction Military.

### S does

**`Unit` dataclass** (lines 1158–1235): `power`, `command`, `discipline`, `discipline_start`, `morale`, `morale_start`, `subunits: List[Subunit]`, `dr`, `speed: str = "Standard"` (Slow/Standard/Fast), `stamina`, `stamina_max`, plus derived `h_per_size`, `size`, `size_max`, `hp`, `hp_max`, `effective_size`, `routed`, `broken`, `stance`.

**`base_combat_pool()`** (lines 1226–1235): `floor(min(effective_size, command) + command + discipline_penalty + stamina_penalty)`, floor 1. This is **PP-233 implemented**.

**`Subunit` dataclass** (lines 810–1153): `shape`, `troop_type`, `tier`, `starting_position`, `advance_dir`, `stance`, `unit_type: str = "melee"` (with "ranged" branch), per-cell `cell_ref` / `cell_pos` / `cell_vec` / `cell_last_speed` / `cell_facing_vec` / `halted_cells` / `merged_cells` / `wing_phase_2_cells` / `_moved_this_turn` / `_prev_pos`.

**5 spatial patterns** (lines 478–539): Line (3×3 / 5×3 / 5×5 / 7×5 by tier) · Arrowhead (triangular wedge, tip speed 2) · Horseshoe (wings + back row at varying width, wing speed 2) · GappedLine (centred gap, equal cell count to Line) · RefusedFlank (engaging-side block + 1 forward cell at refused column, front-row speed 2).

**`MIN_DISCIPLINE`** (line 470, ED-815): Line 1, Arrowhead 4, Horseshoe 5, GappedLine 5, RefusedFlank 3. Deployment-validity check; non-Line shapes drift to Line at insufficient discipline (`check_drift` line 1237).

**Octagon angle model** (lines 552–630): GREEN (<45°) 0 mod; YELLOW (45–90°) −1 pool / 1.5× damage; RED (≥90°) −2 pool / 2.0× damage. Plus FLANKED_BONUS 1.5× when GREEN attacker is also present non-GREEN. ATTENTION_SPLIT_MIN_POOL = 1.

**No declared tactics layer.** S does not implement §A.8 Envelopment / Feigned Retreat / Ambush / Concentration / Refused Flank / Hammer & Anvil as declared mechanics. Spatial-pattern Horseshoe produces *envelopment-shaped* outcomes emergently; spatial-pattern RefusedFlank produces *refused-flank-shaped* outcomes emergently. The declarative-with-Ob layer is absent.

### Three-way comparison

| Element | R | C | S | Alignment |
|---|---|---|---|---|
| Soldier-level primitive | T-42 free param | block_size = soldiers per Size | BLOCK_SIZE=100 | ✓ exact (Chunk 1) |
| **Class diversity (longbow / pike / horse-archer / etc.)** | 13 classes (master matrix axis) | Power tier (1–7) but no class taxonomy | Single melee + ranged branch | **R↔C/S P2 — F2.2** |
| Power tier (quality) | Implicit via institutional substrate (T-4/5) | Explicit 1–7 (Levy → Peerless) | `Unit.power` field | C↔S ✓ exact; R↔C aligned in principle |
| Faction → unit gating | T-4/T-5 force-generation depth | Military stat → Power ceiling + Discipline ceiling | Not enforced — Unit instantiated freely | C↔S P2 partial |
| Discipline | T-29 morale cascade; deterministic threshold | 1–7 + deterministic degradation PP-502/PP-251 | `discipline_check_phase` line 384 implements PP-502 | C↔S ✓ implemented |
| Morale | T-29 propagating field | 1–7 + multi-trigger + cap −3/cascade + encirclement exception | Continuous float; erosion = `dmg / (disc × cmd)` line 1928 | C↔S **partial** — see F2.7 |
| Command | M-4 timing-as-skill | `⌈(Cha+Cog)/2⌉`; sub-unit cap; tactic Ob | `Unit.command`; dominates pool | C↔S ✓ on basics; tactics layer absent — F2.6 |
| Speed tier | Cavalry asymmetry (T-14) | Slow / Standard / Fast | `Unit.speed: str` default "Standard"; used by pursuit | C↔S ✓ |
| **Formation type / combat mode** | (not explicitly enumerated) | 7 modes: Line / SW / Wedge / Skirmish / Column / FR / Reserve | 5 spatial patterns; no combat-mode axis | **C↔S P1 — F2.3 (Shield Wall), F2.4 (Reserve), F2.5 (FR), F2.8 (Skirmish, Column)** |
| **Spatial pattern** | T-35 sub-tile vectors | Implicit / per-tactic | 5 patterns (Line/Arrow/HS/GL/RF) | R↔S ✓ principle; C silent — F2.1 axis conflation |
| Declared tactics | G-1..G-6 named historical plays | §A.8 6 tactics with Ob+counter | None — emergent only | **C↔S P2 — F2.6** |
| Facing | T-33 first-class primitive | Octagon GREEN/YELLOW/RED (Jordan design) | `octagon_angle` 560–580; ANGLE_DEF_MOD + ANGLE_DMG_MULT | ✓ all three |
| Sub-unit limit | (silent) | Command cap; TTRPG cap 3; PP-504 Cmd applies in full per sub-unit | `Unit.subunits` is unbounded list | C↔S **P3 — F2.9** |

### Bottom-up sanctity check

| Element | Bottom-up? | Notes |
|---|---|---|
| Discipline degradation deterministic threshold | ✓ C+S | Emerges from Size-loss + asymmetry comparison — no special-case patches |
| Morale erosion = dmg / (disc × cmd) | ✓ S | Generalship-dominates emerges from denominator; no morale threshold ladder |
| Spatial pattern produces matchup outcome | ✓ S | SHAPE_OFF_MOD/SHAPE_DEF_MOD all zero (lines 460–469); advantages come from cell arrangement + speed + support_engage_frac |
| MIN_DISCIPLINE per shape | ~ S | "Drift to Line if discipline too low" — deployment-validity gate; bottom-up if interpreted as "can't hold complex shape without trained troops" |
| Octagon GREEN/YELLOW/RED → flank damage | ✓ S | Per-cell angle classification; no shape-class lookup |
| FLANKED_BONUS 1.5× when GREEN + non-GREEN coincident | ✓ S | Composes from per-cell zone classification |
| Class diversity (pike vs longbow vs horse-archer) | ∅ C+S | **No class taxonomy — F2.2 — would need to compose up from {weapon, armour, training, ability} primitives** |
| §A.6 formation combat modes (Shield Wall, Reserve, etc.) | ✗ S | Declarative canon mechanic; S models spatial patterns only; combat modes not implemented — F2.3/F2.4/F2.5/F2.8 |
| §A.8 tactics (Envelopment, Hammer & Anvil, etc.) | ⚠ borderline | Declarative tactic with Ob roll is intent + execute, not pattern-recognition — passes M-9 if implemented as declared-action + Cmd check; would violate M-9 if implemented as "system detects Envelopment-shape" |

**Verdict:** S spatial-pattern layer is bottom-up sanctified. C combat-mode and tactics layers are declarative-with-execution-check — also M-9-compliant if interpreted as "player declares intent, system rolls execution." S simply hasn't implemented these declarative layers yet.

**Risk:** if S adds Envelopment as `if HS_wings_wrap and enemy_facing_blocked: bonus_damage = X`, that's top-down recognition (M-9 violation). Correct: player declares Envelopment intent → Cmd Ob 2 roll → atoms ordered into envelope-shaped advance via existing cell primitives; outcome emerges.

### Top-down historical validation

| Battle | Class+Mode+Tactic critical to outcome | C currently models | S currently models |
|---|---|---|---|
| Cannae | Heavy infantry × Line · Combined arms × Envelopment tactic | ✓ Line; ✓ Envelopment §A.8 | ⚠ Envelopment emerges from Horseshoe; no declared layer |
| Pharsalus | Heavy infantry × Line + Reserve 4th line · Refused Flank tactic | ✓ Line + Reserve §A.6; ✓ Refused Flank §A.8 | ✗ Reserve absent (F1.1/F2.4); RefusedFlank spatial pattern exists but no Refused Flank declared tactic |
| Hastings | Shield-wall heavy infantry × Shield Wall mode · Cavalry × Feigned Retreat tactic | ✓ Shield Wall; ✓ Feigned Retreat | ✗ Shield Wall absent (F2.3); FR absent (F2.5) |
| Crécy / Agincourt | Mass missile (longbow) × Skirmish-defensive + Heavy infantry dismounted × Line | ✓ Line; ~ Skirmish | ⚠ Volley yes; Skirmish mode absent (F2.8); no longbow class |
| Marignano | Heavy pike × Wedge + Heavy infantry × Line · Hammer-and-Anvil tactic | ✓ Wedge; ✓ Hammer & Anvil | ⚠ Arrowhead = Wedge spatial; no Hammer & Anvil declared layer |
| Pavia | Mass missile (arquebus) × Skirmish + Heavy pike × Line | ✓ Line; ~ Skirmish | ✗ Skirmish absent; no arquebus class |
| Panipat | Wagon-fortress × static defensive + Mass missile + Light cavalry × Envelopment | ∅ Wagon-fortress not in §A.6; ✓ Envelopment | ✗ Wagon-fortress absent; cavalry deferred G-11 |

**Direction surfaced:** F2.3 (Shield Wall) unlocks Hastings. F2.4 (Reserve) + F2.6 (declared tactics) unlock Pharsalus. F2.8 (Skirmish mode) unlocks Crécy/Agincourt/Pavia. F2.2 (class taxonomy) unlocks longbow/arquebus/wagon-fortress.

### Lateral gameplay validation

| Precedent | Class axis | Combat-mode axis | Spatial-pattern axis | Declared tactics |
|---|---|---|---|---|
| **Total War** (Medieval II / Three Kingdoms / Rome II) | 30–50 unit types per faction | Formation orders: Phalanx / Wedge / Loose / Spread / Skirmish | Implicit via formation order | Limited (charge, hold, fire-at-will) |
| **Field of Glory II Digital** | Specific class types + quality grade (Average / Superior / Elite) | Implicit in unit type | Implicit | Charge / shoot / regroup |
| **Ultimate General: Civil War** | Historical regiment types + tier | Stance: line / column / skirmish | Stance implies pattern | Push back / hold / withdraw |
| **Combat Mission** WEGO | Specific by force pool (rifle squad, MG, AT) | Cover / move / hunt / target | Orders specify cells | Hunt, advance under fire, etc. |
| **Mount & Blade Bannerlord** | Troop trees with tier progression | Line / Shield Wall / Loose / Square / Skein / Column | Orders specify | Charge / hold / advance |
| **Unicorn Overlord** (Vanillaware 2024) | 60+ classes with role-positioning within squad | Implicit in class | Front row / back row positioning | **Programmable per-unit tactics ("Use [skill] when [condition]") — declared, executed automatically** |
| **Football Manager** (SI Games) | Roles within positions (Box-to-Box midfielder, Deep-Lying Playmaker, etc.) | Mentality + width + tempo + pressing | Formation (4-3-3, 4-4-2, etc.) | Pre-match instructions + in-match shouts |

**Verdict laterally:**
- All acclaimed precedents expose three orthogonal axes: class · combat-mode · spatial-pattern. C+S currently has Power-tier + combat-mode (§A.6) + spatial-pattern (S only). **Missing axis: class diversity** — F2.2.
- UO's programmable per-unit tactics is the strongest lateral analog for §A.8 done bottom-up. Player declares behavior tree per unit; unit executes via per-unit AI. Declarative-intent + emergent-execution. **Recommended pattern for §A.8 implementation.**
- FM's role-within-position is the strongest analog for class-within-Power-tier. A "Box-to-Box midfielder Defensive" differs from "Box-to-Box midfielder Attacking" even though both are midfielders. For Valoria: "Veteran Longbow" and "Veteran Pike" are different primitives even though both are Power 4.
- Total War's 30–50 unit types per faction is the upper bound. Valoria probably wants 8–15 pre-firearm classes across 4 factions × Military tier.

### Throughlines surfaced (Chunk 2)

- **T-48 (R/C/S) — Formation has two orthogonal axes: spatial arrangement × combat mode.** S models spatial-arrangement (5 patterns); C models combat-mode (7 §A.6 formations). Not interchangeable. A Line spatial pattern can be in Engaging or Shield Wall or Reserve combat mode. Unifying under one "formation" field loses expressiveness.

- **T-49 (R/C) — Class taxonomy and Power tier are complementary, not equivalent.** Power = quality (Levy → Peerless); Class = type (longbow vs pike vs heavy cavalry). Matchup matrices require both. C has tier only.

- **T-50 (UO/S validates M-9) — Declarative-intent + emergent-execution is the M-9-compliant pattern for tactics.** UO's per-unit programmable behavior trees, FM's pre-match instructions, C §A.8 declared tactics with Ob roll all share: player declares intent → system executes via existing primitives → outcome emerges. Not pattern-match recognition.

- **T-51 (C/S) — Discipline-as-deterministic-threshold is M-9-compliant primitive.** PP-502/PP-251 deterministic degradation (Size lost > current Disc AND asymmetric) implemented in `discipline_check_phase` (S line 384) is the canonical example of a Chunk-2 primitive done right. Composes from per-tick Size-loss tracking; no special-case shape rules. **Reference pattern for further canon→sim implementations.**

### Findings (Chunk 2)

**F2.1 — P2 (C↔S):** Formation-axis conflation. S `Subunit.shape` mixes spatial arrangement with what should be combat mode. Resolution path (bottom-up):

```
Unit:
  spatial_pattern: Line | Wedge | Horseshoe | GappedLine | RefusedFlank | Open
  combat_mode:     Engaging | Shield Wall | Skirmish | Column | Feigned Retreat | Reserve
```

Two fields, independent. Validates Bannerlord/TW/UO pattern.

**F2.2 — P2 (R↔C↔S):** No unit-class taxonomy. R's 13 classes not encoded; C uses Power tier as proxy for quality but doesn't distinguish longbow class from pike class. Resolution path (bottom-up):

```
UnitClass:
  weapon_primary: WeaponSpec
  weapon_secondary: Optional[WeaponSpec]
  armour: ArmourClass
  unit_type: melee | ranged | mixed
  special_ability_flags: Set[Flag]
  base_speed: SpeedTier
```

Power tier becomes quality multiplier on top of class. Faction Military gates both `max_power` and `allowed_classes`.

**F2.3 — P1 (C↔S):** Shield Wall not implemented in S despite canonization (§A.6 + PP-500). Mechanics: Off −1D, Def +2D, cannot advance, negates one declared flank per turn; PP-500 +2D applies to all simultaneous engagements. **Hastings non-reproducible.** C→S correctness drift on ratified canon mechanic.

*Resolution path (bottom-up):* `combat_mode = "Shield Wall"` flag (F2.1). When set: `can_advance = False`; `off_pool -= 1`; `def_pool += 2`; `flank_negation_remaining = 1` per turn; PP-500 propagates via existing pair-iteration in `resolve_engagements`.

**F2.4 — P1 (C↔S):** Reserve not implemented despite canonization (§A.6 + PP-MB-04 + PP-499). C explicit: "Reserve commitment at Phase 3 of Turn N+1 makes unit immediately available for Phase 5 Engagement that same turn." Restates F1.1. **Pharsalus non-reproducible.**

*Resolution path:* `committed: bool = False` + `commitment_pending: bool = False` on Unit. Reserve unit: doesn't advance, doesn't engage, doesn't drain stamina. Order at Phase 3 Turn N → `commitment_pending = True`. At Phase 3 N+1: `commitment_pending → committed=True`. First-engagement Off/Def split equal (round down to Off) per C clarification.

**F2.5 — P2 (C↔S):** Feigned Retreat not implemented despite canonization (§A.6 + PP-256). PP-256: Discipline Ob 1 for pursuer; defender Cmd Ob 2 to recognize feint.

*Resolution path:* `combat_mode = "Feigned Retreat"` flag. Unit retreats stance="retreat" along advance_dir. Pursuing unit rolls Cmd vs Ob 2; on fail, pursues. Pursuer rolls Discipline vs Ob 1 to halt; on fail, charges past and exposes flanks next turn.

**F2.6 — P2 (C↔S):** §A.8 Tactics absent from S as declarative layer.

*Resolution path (T-50 pattern):* `declared_tactic: Optional[Tactic]` on Unit. Tactic = Cmd Ob roll + execution-via-existing-primitives. Envelopment: Cmd Ob 2 → if pass, atoms ordered into envelope-shaped advance. Hammer & Anvil: requires Shield Wall anvil (F2.3) + Fast envelop (G-11). Each tactic: declarative intent → execution check → existing primitives produce outcome.

**F2.7 — P3 (C↔S):** Morale erosion in S (`erosion = dmg / (disc × cmd)` line 1928) elegantly captures generalship-dominates but does NOT implement C §A.4 stepwise triggers (Size <50% −1, <25% −1 additional, etc.).

`[QUESTION FOR JORDAN]` — keep S's continuous erosion as canonical (canon updates to match S) OR add stepwise triggers (S updates to match canon). Recommendation: continuous erosion is M-9-compliant bottom-up; canon should formalize.

**F2.8 — P2 (C↔S):** Skirmish and Column combat modes not implemented in S despite §A.6 canonization. Skirmish: cannot be flanked, −1D vs Heavy. Column: +1 Speed tier, movement only, cannot engage.

*Resolution path:* Per F2.1 combat_mode field. Skirmish: skip flank zone computation; apply −1D when target classified Heavy. Column: speed_tier += 1; `can_engage = False`.

**F2.9 — P3 (C↔S):** Sub-unit cap (Cmd, TTRPG hard cap 3) not enforced in S. `Unit.subunits` is unbounded.

*Resolution path:* Assertion at battle setup: `len(unit.subunits) <= min(unit.command, 3)`.

### Carried forward

- **F2.1 (axis split)** → enables F2.3 / F2.4 / F2.5 / F2.8.
- **F2.2 (class taxonomy)** → Chunk 3 (per-class pool / TN / DR / range).
- **F2.6 (declared tactics)** → Chunk 3 (Cmd Ob rolls integrate with command/timing).
- **F2.7 (morale model)** → Chunk 4 (cohesion/rout pipeline).

---


*Audit continues. Subsequent chunks committed incrementally to this file.*
