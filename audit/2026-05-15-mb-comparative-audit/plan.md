# Mass Battle Implementation Plan — Consolidated from 2026-05-15 Comparative Audit

**Date:** 2026-05-15
**Source audit:** `designs/audit/2026-05-15-mb-comparative-audit/audit.md` (commit `ec1a3beb`, 2,486 lines)
**Ledger appends:** ED-900..ED-915 (16 P1 entries; archive rollover to `editorial_ledger_archive_2026-05b.yaml`)

`[SELF-AUTHORED — bias risk]` Plan author = audit author. An independent reviewer would prune differently.

---

## Purpose

This document consolidates the 2026-05-15 mass-battle comparative audit into an actionable plan for v26+ implementation. It applies NERS criteria (Necessary, Robust, Smooth, Elegant per canon `<definitions>`) to the audit itself, prunes bulk, and presents the load-bearing work in **9 work packages**, each NERS-graded N/R/S/E on a 1–4 scale.

The plan's question is honest: **does Valoria really need 115 named patterns and 61 findings to improve mass battle, or can the work be elegantly consolidated?** This document argues for ~85% bulk reduction — and is willing to be wrong about which 85%.

---

## NERS pass on the audit itself

Honest neutrality first.

**N (necessary)? — Yes.** The audit surfaces real canon→sim drift. 16 P1 findings each represent canonized mechanics the sim does not implement. Triangulation (R historical, C canon, S sim) produces convergence-validated findings single-corpus review misses. Without the audit, F4.1 (pursuit 25–30× under-weight, producing 1.4× casualty ratio vs R's 2–5×) and F5.1 (terrain absent despite §A.9 + PP-780 canonization) would persist as unflagged drift indefinitely. **N: 4.**

**R (robust)? — Yes.** Findings have explicit Resolution Paths; throughlines compose with R's prior 43 + 13 meta without contradiction; lateral validation against 9 acclaimed precedents (TW, FoG2, UG, CM, Bannerlord, Unicorn Overlord, Football Manager, HoMM, Phantom Brigade) anchors design defensibility. **R: 4.**

**S (smooth)? — Mixed.** 11 chunks committed incrementally is smooth as session structure, but produces cross-reference friction: F-numbers reference T-numbers reference MT-numbers. A reader who wants the implementation plan must traverse 12 chunks to assemble it. **This document is the smoothing operation. S: 3.**

**E (elegant)? — No.** The audit produced **115 named patterns** (93 throughlines + 22 meta-throughlines) + **61 findings** = **176 indexed items**. Not elegant. A future implementer would spend significant effort just navigating the index. Many throughlines are restatements; many findings cluster naturally; multiple meta-throughlines describe how the audit was conducted rather than what the design should do. **E: 2.**

**Audit aggregate: N4 R4 S3 E2.** Necessary and robust; needs smoothing and elegance work.

This document is that work.

---

## What is bulk vs. what is load-bearing

### Bulk to prune

**Methodology meta-throughlines** (out of plan scope):
- MT-5 (R/C/S triangulation methodology) — about how the audit works.
- MT-6 (lateral validation as forcing function) — about audit method.
- MT-8 (audit itself is bottom-up) — meta-meta about methodology.
- MT-9 (audit as handoff) — purpose statement, not design.

These belong in an audit-methodology document, not a design plan. **Pruned: 4 of 9 meta-throughlines.**

**Throughlines that restate canon or sim implementation:**
- T-44 (cell ≈ 50 m implicit) — a canon-revision line, not a pattern.
- T-51 (PP-502 deterministic Disc) — sim correctly implementing canon; not a cross-corpus pattern.
- T-52 (PP-233 pool formula) — canon specification restated as throughline.
- T-54 (Cmd as master, lateral) — lateral-validation of T-53; collapse to one.
- T-56 (temporal cadence drift) — restates F3.3; not a separate pattern.
- T-65 (PP-780 auto-derivation) — same content as F5.2 finding.
- T-67 (weather universal) — lateral observation = F5.3 content.

**Pruned: ~12 of 50 throughlines as duplicative or restating.**

**P3 findings that are 1-line cleanups:**
- F1.4 cell-scale canonization, F2.9 sub-unit cap assertion, F3.11 dead constants, F3.12 wounds→Cmd, F4.4 idle morale, F8.10 Part D fetch, F9.5 §A.6/§A.8 M-9 refactor (folds into implementation discipline of other work packages), and the F6.10 three-axis Ob fetch.

**Pruned: ~10 of 20 P3 findings, reclassified as "code hygiene checklist."**

**P2 findings that fold into their gateway P1:**
- F2.5 / F2.8 → fold into F2.1 axis split.
- F3.7 / F3.8 → fold into F4.10/F4.11 morale interactions → fold into F4.3 morale-model decision.
- F4.6 → restates F3.10.
- F6.3 / F6.4 / F6.5 / F6.6 / F6.8 → all fold into F6.1 Thread staged implementation.
- F7.2 / F7.3 → fold into F7.4 + F8.4 persistence implementation.
- F7.5 / F7.6 / F7.7 / F7.8 → fold into F8.4 emit-events strategic-layer Accounting.
- F8.5 / F8.6 / F8.8 → fold into F8.3 + F8.4.

**Pruned: ~20 of 25 P2 findings, folded into gateway work packages.**

**Consolidation summary:** Throughlines 50 → ~18 load-bearing. Meta-throughlines 9 → 5. Findings 61 → 10 work packages + 3 canon decisions. **~85% bulk reduction.**

### Load-bearing meta-principles (5)

Renaming MT-1..MT-9 survivors as M-A..M-E:

**M-A — Design integrity preserved; implementation has drifted.** 13 of 16 P1 findings are canon-specifies-S-doesn't-implement. Canon is sound; v26+ work is implementation, not redesign.

**M-B — Implementation has multiplicative leverage.** Six findings (F2.1, F2.2, F8.4, F5.1, F6.1, F4.1+F4.2+F1.3 as a unit) unlock or partially-resolve >30 of the audit's other findings. Implementation order matters.

**M-C — Bottom-up sanctity is the cohesion principle** (reaffirms canon's M-9 + P-01..P-15). Every primitive composes upward; no top-down recognition. Cross-corpus convergence depends on this; future canon and sim additions must respect it or introduce drift.

**M-D — Canon→sim drift is asymmetric.** 13 of 16 P1 are canon-leads-sim-catches-up. Three reverse cases (S-cleaner-than-C — F4.3 continuous morale, T-44 cell-scale, T-58 erosion model) inform canon revisions.

**M-E — Persistence is the largest cross-cutting theme.** Discipline / Coherence / Experience / Gap / MS / Treasury / Mandate / Military all persist across battles in canon; none in current sim. Foundation for strategic depth.

### Load-bearing throughlines (18)

Renumbered PT-1..PT-18 with cross-mapping to audit T-numbers. Each is convergence-validated (≥2 corpora agree) or lateral-validated by acclaimed precedent.

**Foundation:**
- **PT-1** (T-45 + T-46) — Phase abstraction layers operate at different scales: R 8-phase descriptive, C/S 5-phase mechanical; 3-phase engagement cap is a budget primitive, not commit-window.
- **PT-2** (T-47 + T-68) — Sightline geometry produces flanking emergently; forest-flanking refactors to reduced-sightline (bottom-up).
- **PT-3** (T-48 + T-49) — Formation has two orthogonal axes (spatial × combat-mode); class taxonomy + Power tier complementary.
- **PT-4** (T-50 + T-74) — Declarative-intent + emergent-execution is the M-9-compliant tactics pattern; contested intentionality produces emergent counter-magic.

**Resolution & cohesion:**
- **PT-5** (T-55) — Damage formula choice (linear vs degree-stepped) is a mechanical fork, not a calibration variant — `[Q]`.
- **PT-6** (T-57 + T-62) — Kill pipeline (cohesion → rout → pursuit) is central; catastrophic pursuit is the engine of historical casualty distributions.
- **PT-7** (T-58 + T-59) — Continuous morale erosion is M-9-compliant; encirclement is the only canonized special case but composes from retreat-zone primitive.
- **PT-8** (T-60) — Compound failure requires feedback loops between Disc/Stamina/Morale (P3 augmentation).

**Environment & integration:**
- **PT-9** (T-63 + T-64 + T-66) — Environment is first-class via per-cell ground primitives + sub-tile features.
- **PT-10** (T-67) — Weather is orthogonal to ground type (canon revision needed).

**Thread (firearm-analog):**
- **PT-11** (T-69 + T-70) — Threadwork-as-firearm-analog with persistent-Coherence economy (Valoria-distinctive).
- **PT-12** (T-71) — Threadweave-OR-tactic hard tradeoff is the master gameplay-decision primitive at general turn level.
- **PT-13** (T-72 + T-73) — Devout-general and Southernmost are canon's hard-exclusion cultural filters.

**Force generation & persistence:**
- **PT-14** (T-75 + T-76 + T-86) — Persistence across battles is most-consequential strategic mechanic.
- **PT-15** (T-77 + T-78 + T-79) — Faction-substrate gating + per-faction muster paths; faction-specific exceptions are faction-primitive composition, not patches.

**Scale transitions:**
- **PT-16** (T-81 + T-83 + T-87) — Three-mode architecture (medium axis) + cost-in-the-holding cascade (Valoria-distinctive).
- **PT-17** (T-82) — Outcome-propagation cascade is the engine of cross-scale gameplay.

**Doctrine triangle:**
- **PT-18** (T-88 + T-90 + T-92) — Doctrine triangle is master organizing principle; perfect-system trap protection via combination of mechanisms (not single); M-9 mechanics ↔ M-5 doctrine coherence.

---

## Work packages

Nine work packages, each NERS-graded.

### WP-1 — Foundation refactor: axis split + class taxonomy + emit-events

**Scope:**
- F2.1 axis split: `Unit.spatial_pattern × Unit.combat_mode` independent fields.
- F2.2 class taxonomy: `UnitClass(weapon, armour, type, abilities, base_speed)`; Power tier becomes quality multiplier.
- F8.4 emit-events: `BattleOutcome` dataclass + `StrategicLayer.on_battle_resolved(outcome)`.

**Unlocks:** F2.3, F2.4, F2.5, F2.8, F3.6, F5.6, F6.6, F7.1, F7.3, F7.5, F7.6, F7.7, F7.8, F7.9, F8.5, F8.6, F8.8.

**NERS:**
- **N: 4** — Blocks all downstream work.
- **R: 4** — Class diversity (customization), tactical mode variety (strategic thinking), strategic outcome consumption (faction depth).
- **S: 4** — Pure architectural primitives compose with everything else.
- **E: 4** — Two fields on Unit, one dataclass, one method. Logically simple.

**Aggregate N4 R4 S4 E4.** Highest priority. Implement first.

### WP-2 — Historical casualty calibration: pursuit + encirclement + compression

**Scope:**
- F4.1 pursuit damage formula: `dmg_size = max(0, a_net - dr_size_units)` per canon §A.12.
- F4.2 PP-683 encirclement: `morale_cap_lifted` when `retreat_zones == 0` AND flanked from ≥3 directions.
- F1.3 compression damage: when `available_free_cells < cells_in_contact × compression_threshold`, multiplier 1.0–2.0×.

**Produces:** R O-10 historical 2–5× casualty ratio (vs current 1.4×). Unlocks structural reproducibility of Cannae, Adrianople, Agincourt, Panipat compression-phase mortality.

**NERS:**
- **N: 4** — Without these, historical reconstructions structurally non-reproducible.
- **R: 4** — Catastrophic pursuit creates strategic weight; encirclement creates terrain-anchor importance; compression creates positioning-as-tactics.
- **S: 4** — All compose with existing pursuit hooks + retreat-zone primitive.
- **E: 3** — Three findings could be stated as one principle ("casualty asymmetry emerges from pursuit + encirclement + compression"); minor elegance gap from multi-finding framing.

**Aggregate N4 R4 S4 E3.**

### WP-3 — Combat modes: Shield Wall + Reserve

**Scope:**
- F2.3 Shield Wall: `combat_mode = "Shield Wall"` flag with arithmetic effects (Off −1, Def +2, can_advance=False, flank_negation_remaining=1/turn, PP-500 +2D propagates to all simultaneous engagements).
- F2.4 Reserve: `committed: bool, commitment_pending: bool` with Phase 3 transition logic per PP-MB-04 + PP-499.

**Unlocks:** Hastings, Pharsalus structurally reproducible. Tactical depth (defensive vs offensive vs reserved-commit choices).

**NERS:**
- **N: 4** — Canon mechanics; without these, two reconstructions non-reproducible.
- **R: 4** — Tactical choice space at general action layer.
- **S: 4** — Requires WP-1 axis split; then composable.
- **E: 4** — Each is a single combat_mode flag with arithmetic effects.

**Aggregate N4 R4 S4 E4.**

### WP-4 — Environment / terrain

**Scope:**
- F5.1 ground_type primitive per cell (6 canon types: River / Uphill / Forest / Walls / Narrow Pass / Open).
- F5.2 PP-780 geographic auto-derivation from `valoria_geography_v30.yaml :: terrain_polygons`.
- F5.3 weather (canon revision + sim): precipitation × visibility × wind × temperature.
- F5.4 + F5.4b sub-tile features + terrain × sightline interaction (forest reduces `max_sightline_distance` → flanking emerges from reduced perception per PT-2/T-68).

**Unlocks:** 8 of 9 R reconstructions; F5.6 cavalry-terrain, F5.7 anchored refused flank, F6.9 Southernmost cross-layer.

**NERS:**
- **N: 4** — 8 of 9 reconstructions require; lateral universal.
- **R: 4** — Terrain creates strategic choice in army composition and positioning.
- **S: 3** — Cross-layer interactions with sightline, cavalry, Southernmost. Smooth requires careful interface design.
- **E: 3** — Real scope; risk of feature creep producing complex interactions.

**Aggregate N4 R4 S3 E3.** Stage carefully: ground_type first, then weather, then sub-tile features. Each stage verifiable independently.

### WP-5 — Thread integration

**Scope:**
- F6.1 staged: Stage 1 practitioner primitives + Coherence depletion. Stage 2 phase-integration (Phase 1 Diagnosis / Phase 4 combat-type / Phase 5–6 non-combat). Stage 3 battle-Thread scale mapping (§A.10 table). Stage 4 contested resolution (§2.6). Stage 5 persistence + Gap registration.
- F6.2 Threadweave-or-tactic hard tradeoff (PT-12, master decision primitive).
- F6.7 contested thread resolution (§2.6 6-row outcome table).

**NERS:**
- **N: 4** — Threadwork is Valoria's firearm-analog; canon design intent is clear.
- **R: 4** — Practitioner-as-finite-resource creates strategic husband-the-wizard depth; contested resolution creates counter-play.
- **S: 3** — Cross-cuts §A.6 Reserve (collective ops), §A.10 hard tradeoff, §A.11 Southernmost terrain, §A.12 pursuit. Many interfaces.
- **E: 2** — 5 op types + Coherence + 3-axis Ob + scale mapping + contested + persistence is the most complex single system in canon.

**Aggregate N4 R4 S3 E2.** **Highest elegance risk in the plan.**

**Honest critique:** Of all canon systems, Threadwork has the most surface area for v26+ scope creep. Analogical-firearm-validation supports design intent, but implementation risks producing more rules than the rest of mass battle combined. Recommend: implement Stage 1 (practitioner + Coherence) alone first, playtest. If Stage 1 already produces the right strategic weight (practitioner-as-finite-resource economy), Stages 2–5 might be partially deferrable. Don't commit to all 5 stages upfront.

### WP-6 — Persistence layer

**Scope:**
- F7.4 Discipline persistence between battles (PP-712): `unit.discipline_persisted = unit.discipline_current` at battle resolution.
- F7.2 Experience state machine: Fresh (0) → Seasoned (+1 Power) → Veteran (+1 more), earned by surviving won/drawn battle with Size > 0; destroyed unit loses XP.
- Once WP-1 emit-events done, automatically unblocks: F7.3 Reinforcement (+1 Size/season + FR-accelerated), F7.5 Campaign Supply (−100 Treasury/season hostile + Prosperity-0 attrition), F7.6 Levy offensive restriction, F7.7 Templar Sacred Assembly, F7.8 Wealth-Zero degradation, F7.9 battle-outcome → faction cascade.

**NERS:**
- **N: 4** — Master operational-tempo variable; lateral universal (FM strongest analog).
- **R: 4** — Forces player to manage unit rotation across campaign.
- **S: 4** — Composes with WP-1 emit-events cleanly.
- **E: 4** — Two state primitives on Unit; rest consumed by strategic layer.

**Aggregate N4 R4 S4 E4.**

### WP-7 — Mode + scale architecture

**Scope:** F8.3 Level-5+ zoom (StrategicLayer event loop + accounting); F8.1 BG-mode mass battle; F8.2 Hybrid Handoff; F8.7 Auto-resolve dispatch.

**Honest critique: is three-mode actually necessary for the videogame?**

Per project identity ("Valoria is a videogame (Godot 4.6) only"), TTRPG and BG modes are design heritage. The videogame may not need to implement them as separate runtime modes. Hybrid handoff might collapse into a player-facing "zoom in" UX, not a two-mode-engine architecture.

**Scope options:**

| Option | Description | NERS |
|---|---|---|
| (a) Full three-mode | All three modes runtime-selectable; full canon fidelity | N3 R4 S3 E2 — complex engineering, ambiguous user value |
| **(b) Two-effective-mode** | **Auto-resolve (BG-equivalent) + tactical zoom-in (TTRPG-equivalent); no separate "BG mode" UI. Matches TW view-battle toggle.** | **N4 R4 S4 E3 — recommended** |
| (c) TTRPG-only + "skip outcome" button | Simplest; loses BG-mode strategic-prep design intent | N3 R3 S4 E4 — too thin |

**`[QUESTION FOR JORDAN]`** — scope decision required before WP-7 implementation begins. **Recommendation: option (b).** If selected, scope reduces to F8.3 + F8.7 + thinned F8.1 (auto-resolve uses simplified BG-formula at engine level; zoom-in is UX layer).

**NERS for recommended (b):** N4 R4 S4 E3.

### WP-8 — Canon decisions

Three `[QUESTION FOR JORDAN]` items block downstream implementation:

**Q1 (F3.1) — Damage formula direction.** Linear (C PP-233) vs degree-stepped (S). 10× drift in dominant-side damage. **Recommendation:** distinct mass-vs-personal abstractions ratified, with a bridge document explaining cadence-and-cell-decomposition relationship. Sim retains per-tick degree-stepped (cell-level); canon retains per-turn linear (TTRPG-level). Each operates at a different temporal scale; the bridge documents the relationship.

**Q2 (F3.6) — PP-233 vs PARAMS-GAP-05 internal canon drift.** Two damage formulas in canon (PP-233 line 70 linear; PARAMS-GAP-05 line 284 Dmg-Mod-with-net-hits). Resolution required before class-dependent Dmg Mod implementation lands in WP-1's class taxonomy.

**Q3 (F4.3) — Continuous vs stepwise morale.** S has continuous erosion (M-9-cleaner per PT-7; lateral-validated TW/UG/FM). C has stepwise triggers (Size <50%, <25%, etc.). **Recommendation:** continuous as canonical; canon revision in §A.4 replaces stepwise triggers.

**NERS impact:** Each unresolved question freezes downstream WPs (Q1 → WP-2 calibration; Q2 → WP-1 class taxonomy completion; Q3 → WP-2 + WP-6 morale-related work). Resolution collapses option space; the option-space-open state is N0/E0 because work cannot proceed without canonical answer.

### WP-9 — Stretch + hygiene (deferred bucket)

All P3 augmentations and 1-line cleanups consolidated as a single deferred bucket:

**Stretch goals (P3 augmentations, `[QUESTION FOR JORDAN]`):**
- F4.5 compound-failure cross-coupling (Disc × Stamina × Morale feedback).
- F9.2 graded cultural-doctrine score (FM-style preferences vs current binary exclusions).
- F9.3 doctrine evolution per faction (HoI4-style track).
- F9.4 opponent-menu learning (FM-style tactical-familiarity decay).
- F4.7 Stalemate Break (PP-297).
- F4.8 over-pursuing exposes flanks.
- F5.5 time of day.
- F1.2 cavalry final-gallop 30–50 m constraint (constrains G-11 implementation when cavalry lands).

**Code hygiene (1-line cleanups):**
- F1.4 canonize cell ≈ 50 m in §A.3b.
- F2.9 add `len(unit.subunits) <= min(unit.command, 3)` assertion.
- F3.11 remove or document `ANGLE_DMG_MULT` + `FLANKED_BONUS` dead constants.
- F3.12 wounds → Cmd tactic-Ob modifier (when F2.6 tactics layer implemented).
- F4.4 idle 2+ turns morale loss.
- F8.10 fetch Part D World Bridge content; verify cross-references.
- F6.10 fetch params_threadwork.md three-axis Ob system specifics.

**NERS:** N2 R2 S4 E4. Pure deferred bucket; revisit after WP-1 through WP-7 stable. **None block core gameplay.**

---

## Implementation order

```
Phase α — Canon decisions
  └─ WP-8 (Q1, Q2, Q3 answered)

Phase β — Foundation
  └─ WP-1 (axis split + class taxonomy + emit-events)

Phase γ — Calibration + combat modes + persistence (concurrent OK)
  ├─ WP-2 (historical casualty calibration)
  ├─ WP-3 (Shield Wall + Reserve)
  └─ WP-6 (persistence — depends on WP-1's emit-events)

Phase δ — Large systems (sequential, stage carefully)
  ├─ WP-4 (environment / terrain) — stage: ground_type → weather → sub-tile
  └─ WP-5 (Thread integration) — stage: practitioner+Coherence → phase-integration → scale-mapping → contested → persistence

Phase ε — Mode + scale (depends on WP-7 scope decision)
  └─ WP-7 (mode + scale architecture)

Phase ζ — Deferred (anytime)
  └─ WP-9 (stretch + hygiene)
```

**Critical path:** α → β → (γ ∥ δ-WP-4) → δ-WP-5 → ε.

Estimated work-units per phase (relative, not absolute time):

| Phase | Work-units |
|---|---|
| α | 1 (canon decisions, Jordan time) |
| β | 4 (WP-1 is small but foundational) |
| γ | 5 (three concurrent WPs, share infrastructure) |
| δ | 8 (WP-4 + WP-5; WP-5 is the largest single WP) |
| ε | 3 (WP-7 with option-b scope) |
| ζ | varies (deferred — no commitment) |

**Total v26+ scope (excluding deferred):** ~21 work-units, vs the audit's 61 findings naive interpretation (~50–60 work-units). **~60% effort reduction from consolidation.**

---

## Out-of-scope flags

The audit and this plan do NOT cover:

- **Pre-battle scouting / intelligence layer.** Canon implies via §A.10 Diagnosis (Thread-specific); no general scouting mechanic. **Recommend separate audit.**
- **Siege as dedicated battle type.** Walls §A.9 partially covered; multi-day siege phases (PP-499 Reserve commits + Wall +3 DR + Slow halt + sapping + parlay) not. **Recommend focused follow-up audit.**
- **Naval / amphibious operations.** Hafenmark naval power; out of mass-battle-direct scope. **Recommend separate audit.**
- **NPC general AI behavior at mass scale.** Cmd/Cha/Cog stats canonized; AI behavior model needed when computer plays generals. **Out of audit + plan scope.**
- **Asymmetric victory conditions** (escort / hold-N-turns / retrieve). Lateral support (TW scenarios, UO conditions) but not standard-battle scope. **Opportunistic.**
- **Faction-unique class catalogue** beyond Templar / Altonian Vanguard / Restoration TS-enabled (partial coverage in WP-1 class taxonomy). **Folds into WP-1 as work proceeds.**

---

## Acceptance criteria per work package

"Done" means:

- **WP-1:** Battle runs with `Unit.spatial_pattern × Unit.combat_mode` independent; `UnitClass` instances cover at minimum Levy / Light Infantry / Heavy Infantry / Cavalry / Ranged / Artillery; `run_multi_unit_battle` returns `BattleOutcome` with all required fields; one downstream finding (e.g., F7.1 faction Military ceiling) functional as proof of unlock.
- **WP-2:** Verification battle (pure-melee, one side encircled) reproduces R O-10 casualty ratio 2–5× across N=100 runs; v16 manifest 1.4× ratio closed.
- **WP-3:** Pharsalus reconstruction reproducible (Reserve commits at Phase 3 Turn N+1, decides battle at Phase 5 Turn N+1); Hastings reconstruction reproducible (Shield Wall holds 9 battle-turns at slope).
- **WP-4:** 8 of 9 R reconstructions reproducible with appropriate ground_type configuration; weather modulates 3+ reconstruction outcomes (Agincourt mud, Crécy sun, Pavia fog); sub-tile features in place for 5+ of those reconstructions.
- **WP-5:** Stage 1: practitioner with Coherence operates in mass battle, depletes per op, recovers across seasons. Stage 2: phase-integration produces canonical timing. Stage 3: TS gating enforced. Stage 4: contested resolution between two practitioners outputs per §2.6 table. Stage 5: Gap registration to territory card.
- **WP-6:** Multi-battle campaign run (3+ battles) shows Discipline persistence + Experience progression + Reinforcement + Wealth-Zero stacking + Levy offensive restriction enforced.
- **WP-7:** Per Q4 scope decision. If option (b): auto-resolve produces outcome consistent with full tactical resolution within ±10% casualty band over N=100 runs; player can toggle between auto-resolve and tactical zoom at battle declaration.
- **WP-8:** Canon revisions committed with PP-numbers and editorial_ledger updates; F3.6 internal-canon-drift resolved.
- **WP-9:** Each stretch finding either implemented or explicitly status-tagged "deferred" with rationale; hygiene items merged as bundled PR; `[GAP]` flags resolved or escalated to follow-up audit.

---

## NERS pass on this plan

**Necessary:** Plan reduces ~120 audit items to 9 work packages + 5 meta-principles + 18 throughlines + 3 canon decisions = **35 indexed items, of which 26 are action items.** Compared to audit's 176 indexed items, 80% reduction. Without consolidation, v26+ would consume disproportionate time navigating the index. **N: 4.**

**Robust:** Each work package has NERS grading, scope, unlocks, acceptance criteria, dependencies. An independent implementer can pick up any WP and proceed. Cross-WP interactions explicit. **R: 4.**

**Smooth:** Phase α → ζ ordering respects dependencies. Concurrent work flagged. WP-1 unlocks pattern surfaces leverage. **S: 4.**

**Elegant:** 9 work packages, 5 meta-principles, 18 throughlines, 3 canon decisions. Could be more elegant — possibly collapse WP-2/WP-3 (both are "tactical calibration") into one WP, reducing to 8 WPs. Reason for keeping separate: distinct unlock patterns benefit from independent NERS grading. **E: 3.**

**Plan aggregate: N4 R4 S4 E3.** Better than audit's N4 R4 S3 E2.

---

## Honest answer to "do we really need that many?"

**No.** ~85% of the audit's bulk is reference material, not action items. The plan's 9 work packages + 3 canon decisions = 12 actionable units. The audit's framework remains valuable as backing reference (cross-reference for any individual implementation, validation against R reconstructions, lateral comparison), but the plan is what to act on.

**Yes** to one more consolidation pass available:
- **Collapse WP-2 + WP-3 into a single "tactical calibration" WP** (casualty asymmetry + canon-mandated combat modes). Reduces to 8 work packages.
- **Collapse WP-9 stretch + hygiene into truly deferred status** (no WP at all; track in `designs/audit/2026-05-15-mb-comparative-audit/deferred.md`). Reduces to 8 work packages with one explicit deferred-list file.

If both adopted: **8 work packages total.** Recommended.

---

## Where this leaves Valoria mass battle

**Design philosophy:** sound. Canon passes M-1 / M-5 / M-6 audit at the design-intent level; bottom-up sanctity (M-C / M-9) is the cohesion principle preserved across R / C / S; three-mode architecture + cost-in-the-holding cascade + persistent-Coherence economy are Valoria-distinctive design strengths defensible against acclaimed precedents.

**Implementation:** the work that remains. 8 (or 9) work packages, leverage-ordered, each independently verifiable. WP-1 (foundation refactor) is the universal unlock. WP-5 (Thread) is the elegance risk requiring staged rollout. WP-7 (mode + scale) needs a scope decision from Jordan.

**Audit framework as inheritance:** 93 throughlines + 22 meta-throughlines + 16 P1 ledger entries (ED-900..ED-915) are committed and inherited by future audits. v26+ implementation work consumes this plan; future auditors consume the audit; both stand on the R / C / S triangulation that produced them.

**Closing position:** the audit was necessary, robust, smoothly chunked but inelegantly indexed. The plan is the elegance pass. The implementation is what makes both worth having done.

---

*End of plan. Source audit: `designs/audit/2026-05-15-mb-comparative-audit/audit.md` SHA `ec1a3beb`. Ledger appends: ED-900..ED-915.*
