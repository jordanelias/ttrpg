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

*Audit continues. Subsequent chunks committed incrementally to this file.*
