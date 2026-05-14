# Module 08 Report — Stature ladder + faction emergence + collapse + retroactive throughline audit

**Date:** 2026-05-13
**Session:** Mode G Module 8 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_08_progression.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §6.1, §6.2, §6.3
- `references/throughlines_meta.md` (full skeleton)
- `references/throughlines_meta_infill.md` (§3.1 T→М tag table)

## Summary

Module 8 wires the player-progression layer that closes the **Stature ladder loop** Jordan asked for at session open: settlement-level work accumulates Renown, Renown produces a Stature scope, scope unlocks new action surfaces, accumulated work eventually emerges as a national faction OR collapses to a city-state. Three primary mechanisms:

- **§6.1 Stature Ladder** — Renown 0–10 maps to five scope tiers (None / Settlement Governor / Multi-Settlement / Provincial Authority / National Actor).
- **§6.2 Faction Emergence** — five stages (Cell → Organization → Movement → Faction → Hegemon) with canonical stage-transition requirements + ED-790 founded-faction starting stats.
- **§6.3 Faction Collapse** — province-loss sequence, city-state contraction, full-collapse threshold.

Module 8 also **rebinds the provisional `renown_delta` signals from M3-M7** to the canonical Renown track via `apply_renown_delta(state, delta)`. Per the canonical Stature catalog (T-15 + player_agency_v30 §5.4), Module 8 takes ownership of the Renown side of the player_action_loop signal pipeline.

## Isolation tests — 38/38 PASS

Highlights:
- T1–T10: Stature ladder + Renown clamping behaviour
- T11–T21: Emergence stage transitions with all three Stage 2→3 conditions tested independently + Stage 3→4 Declaration roll mechanic + Stage 4→5 multi-Seat requirement
- T22–T26: ED-790 founded faction starting stats + Mandate Recovery preconditions
- T27–T34: Collapse mechanics including holdout settlements + city-state contraction + full-collapse threshold
- T35: T-23 binding test — `count_recruitment_candidates` correctly counts Local Actors at Disposition ≥ 3 (the M6 §4.5 recruitment-threshold from F-23 canonical lineage)
- T36–T37: Throughline coverage tables are queryable for Module 13 audit consumption
- **T38: Emergent cross-module chain** — simulates the renown_delta signal flow from M3 (install Chapel +1) + M5 (Pacify success +1) + M6 (Flourishing +1) → reaches Renown 5 → scope transitions to MULTI_SETTLEMENT. **This proves the player-action loop closes end-to-end across modules without authored coordination.**

## Throughline bindings — explicit per-module

### Primary throughline this module serves: T-15 Player Progression

Per `throughlines_meta_infill.md §3.1`:

> **T-15 Player Progression** — Primary М: М-5 scale-connecting. Justification: *"personal Standing ladder produces settlement→province→faction progression"*. Load-bearing systems: `scale_transitions, settlement_layer, faction_layer, factions`.

**Module 8 IS this throughline mechanically.** The Stature ladder + emergence stages + the rebinding of M3-M7 renown deltas to a single canonical Renown track is precisely the mechanical instantiation T-15 names.

### Secondary throughline: T-23 NPC Arc Emergence

> **T-23** — М-5 scale-connecting. Justification: *"personal arc → faction Domain Echo → political shift → new arc triggers."*

Module 8's `count_recruitment_candidates` wires M6 §4.5 Local Actor Dispositions into Stage 2→3 emergence requirements. The Local Actor at Disposition +3 becomes an "NPC officer" the player can claim. T-23's canonical chain (personal arc → political shift) lands here as: Local Actor's individual Disposition track (personal arc) accumulates → player crosses Stage 2→3 threshold (political shift) → Movement stage opens new player action surface (new arc triggers).

### Tertiary throughlines: T-25 Generational Arc, T-20 Two Contests

- **T-25** — Module 8 surfaces the Stature progression; Module 9 (timeline) will wire the 30-year clock that makes the progression generational. Module 8 prepares the substrate.
- **T-20** — Faction collapse to city-state per §6.3 is a Two-Contests outcome: a faction faced with conquest cannot keep its national stat sheet AND keep a city-state foothold; the leader's choice between provincial restoration vs. city-state consolidation IS the Two-Contests tension at faction scale.

### Meta-throughlines (per `throughlines_meta.md §3`)

- **М-5 SCALES CONNECT THROUGH SUBSTRATE** — PRIMARY. Module 8 is the per-player scale-connecting mechanic. Renown earned at settlement scope echoes up through province and faction scopes.
- **М-6 CHOICE IS FORCED** — SECONDARY. The Stage 3→4 declaration is a forced-choice commitment point: declare formally (incur visibility + counter-attack risk + gain full faction stat sheet) or remain a Movement (operate locally but cannot issue national-level Domain Actions).

Module 8 surfaces both bindings as queryable Python dicts (`THROUGHLINE_COVERAGE_BY_THIS_MODULE`, `META_THROUGHLINE_COVERAGE_BY_THIS_MODULE`). Module 13 integration audit will consume these to verify the simulation covers the throughlines the design documents commit to.

## Retroactive throughline audit — Modules 1 through 7

Throughline framework adoption was added in PP-672 (2026-04-19). Prior modules in this sim were built before throughline-binding was made explicit. Audit pass below for retroactive coverage:

### M1 — Settlement primitives
- **T-18 Radiation Gradient** (М-2 geography-holds-pressure, secondary М-3 substrate-grounded): M1 supplies the canonical 37-settlement registry + SettlementStats {Prosperity, Defense, Order}. The Stats values are the substrate state T-18 names; the registry is the geographic skeleton T-18 requires.
- **М-3 SUBSTRATE GROUNDS ALL** (parent meta of T-18). The integer stats are the substrate.

### M2 — Hierarchy + adjacency
- **T-18 Radiation Gradient** (continued) — M2's EDGES graph realizes the geography.
- **T-19 Southernmost Hidden Front** (М-2 secondary М-1) — M2 specifically encodes Schoenland as a degree-1 foreign-exempt special case; this is the "Southernmost" peninsular boundary T-19 references.
- **М-2 GEOGRAPHY HOLDS PRESSURE** primary; **М-5 SCALES CONNECT** secondary (province ↔ settlement aggregation via `province_accord_from_settlements`).

### M3 — Facility tiers + capacity pressure
- **T-15 Player Progression** (secondary) — M3's `expand_institutional_capacity` (Treasury 300, +1 Wing) is a player improvement action that creates rank-holder slots. Wing slots gate Standing 6+ advancement per §1.4.2 — directly M5/T-15 territory.
- **М-4 INSTITUTIONS STAKE SUBSTRATE-POSTURES** — capacity tiers (Wing/Suite/Chamber/Billet) are institutional substrate per faction_politics_expanded_v1.

### M4 — Church four-axis + parish + pastoral
- **T-08 Church Rendering Reinforcement** (М-4 PRIMARY) — Church's substrate-posture is rendering-reinforcement. M4 implements the four axes (Religious Building / Templar / Inquisitor / Governor) which ARE the rendering-reinforcement infrastructure. **This is the strongest single-throughline binding in any module so far.**
- **T-22 Belief Lattice** (М-6) — §1.6 Geneva trap (Church infrastructure becomes instrumentally useful to secular governors) is a Belief Lattice mechanic: cooperation across belief boundaries is forced by mechanical interdependence.
- **М-4** primary; **М-1** secondary (CI accumulation pressure).

### M5 — Dual-authority governance
- **T-15 Player Progression** (М-5 PRIMARY for §3.2 standing-tier table) — the four-tier governor-eligibility ladder (Operative/Counselor/Lieutenant/Successor) IS T-15's "personal Standing ladder produces settlement → province → faction progression."
- **T-11 Crown Pragmatic, T-15a Hafenmark Unmediated Sovereigntist, T-15b Löwenritter Substrate-Agnostic, T-15c RM Substrate-Heritage** (all М-4) — M5's seven-subnational-faction table (§3.3) encodes each faction's distinct substrate-posture via management effects.
- **М-5** primary; **М-4** secondary.

### M6 — Settlement events + Thread ops + Local Actors
- **T-01 Everything Is Thread** (М-3 PRIMARY) — §4.4 explicitly labels Thread Operations as Throughline T1 in the design doc. M6's `apply_thread_op` with 7 canonical operations + ±1-per-stat cap directly realizes T-01.
- **T-23 NPC Arc Emergence** (М-5) — §4.5 Local Actor recruitment-pool mechanic. Note: §4.5 design doc parenthetical says "Throughline T7" but this predates the post-ED-738 throughline reorganization. **F16 NEW.**
- **М-3** primary (Thread operations); **М-5** secondary (Local Actor → faction emergence wire to M8).

### M7 — Military granularity
- **T-19 Southernmost Hidden Front** (М-2 with М-1 secondary) — load-bearing systems include `mass_combat, military_layer` per the canonical T-NN catalog. M7's Assault/Siege/Bypass + Fortress chokepoint mechanics are exactly the military-layer hooks T-19 names.
- **T-20 Two Contests** (М-6) — §5.1 capture sequence forces the attacker to choose Assault vs Siege vs Bypass (each with distinct cost/time/risk profile) — Two Contests at the tactical scale.
- **М-2** primary (geography holds the chokepoints); **М-6** secondary (action choice forced).

### Coverage summary across M1-M8

| Throughline | Title | Primary M | Module binding |
|---|---|---|---|
| T-01 | Everything Is Thread | М-3 | M6 (§4.4 Thread ops) |
| T-08 | Church Rendering Reinforcement | М-4 | M4 PRIMARY |
| T-11/T-15a/T-15b/T-15c | Faction postures | М-4 | M5 §3.3 |
| T-15 | Player Progression | М-5 | M5 (governance), M8 PRIMARY |
| T-18 | Radiation Gradient | М-2 | M1, M2 |
| T-19 | Southernmost Hidden Front | М-2 | M2 (Schoenland), M7 (military) |
| T-20 | Two Contests | М-6 | M7 (military choice), M8 (collapse) |
| T-22 | Belief Lattice | М-6 | M4 (Geneva trap) |
| T-23 | NPC Arc Emergence | М-5 | M6 (Local Actors), M8 (recruitment bridge) |
| T-25 | Generational Arc | М-5 | M8 (substrate; M9 wires clock) |

10 distinct throughlines bound across 8 modules. **Major coverage gaps for Module 13 to track:**

- **T-04 MS Decay**, **T-05 CI Accumulation**, **T-06 IP Accumulation**, **T-07 Turmoil** (all М-1 PRESSURE clocks) — load-bearing system `clocks`. **Not yet bound by any module in this sim.** Module 9 (extended timeline) will own the clock-pressure family.
- **T-12 Practitioner Arc**, **T-13 Certainty Journey**, **T-17 Companion Moral Mirror** (М-6 forced-choice personal-scale) — these are character-layer throughlines outside settlement-management primary scope. Module 13 should confirm they're handled in another sim.
- **T-16 Knot Propagation** (М-5) — `threadwork` system. Not yet bound. Module 6's Thread ops touch the surface but don't propagate knots.
- **T-21 Thread Political Warfare** (М-4 + М-3) — M4 + M5 touch the surface (Church + RM substrate postures) but the warfare layer is Module 12 territory.
- **T-24 Convergence as Crisis** (М-5) — multi-throughline convergence; explicitly a Module 13 integration target.

## Meta-throughline patterns across M1–M8

Counting primary bindings:
- **М-3 SUBSTRATE GROUNDS ALL** — M1, M2, M6 (3 modules)
- **М-4 INSTITUTIONS STAKE SUBSTRATE-POSTURES** — M3, M4, M5 (3 modules)
- **М-5 SCALES CONNECT THROUGH SUBSTRATE** — M5, M8 (2 modules — and М-5 is secondary in M2, M6, M8)
- **М-2 GEOGRAPHY HOLDS PRESSURE** — M2, M7 (2 modules)
- **М-6 CHOICE IS FORCED** — M7, M8 (2 modules secondary; primary not yet)
- **М-1 PRESSURE IS CONTINUOUS** — secondary in M4; **no primary binding yet** — Module 9 will provide.

**Pattern:** the settlement-management sim leans heavily on М-3 / М-4 / М-5 (substrate, institutions, scales). It's structurally weak on М-1 (continuous pressure). This is **expected**: settlement-management is about the static substrate; continuous pressure is the timeline + clocks layer. Module 9 must close the М-1 gap.

## Audit-facing finding NEW this session

### F16 — design-doc parenthetical "Throughline T7" in §4.5 doesn't match canonical T-NN catalog

`settlement_layer_v30.md` line: *"### §4.5 Local Actors (Throughline T7)"*. But per `throughlines_meta_infill.md §3.1`:
- **T-07 = "Turmoil"** (М-1 PRESSURE — clocks, peninsular_strain, victory, tensions_deck, royal_assassination_fuse). NOT Local Actors.
- **T-23 = "NPC Arc Emergence"** (М-5 scale-connecting — load-bearing systems include `factions`, `faction_succession_split`). This is the canonical match for Local Actor mechanics.

§4.5's "Throughline T7" parenthetical was likely correct under a pre-ED-738 numbering; the post-ED-738 (post-2026-04-29) renumbering shifted Local Actors to T-23. Same pattern §4.4 line "(Throughline T1)" — T-01 IS "Everything Is Thread" in current canon, which IS correct for Thread Operations. Only the §4.5 T7 parenthetical is stale.

Also §4.6: *"### §4.6 Settlement POI Templates (Throughline T3)"* — T-03 = "Inseparability" (М-3 substrate-grounded). POI templates *plausibly* relate to substrate-grounded geography, but the binding is tenuous. Worth surfacing for editorial consideration.

**Editorial decision needed:** refresh `settlement_layer_v30.md` parentheticals to the post-ED-738 T-NN numbering. Trivial mechanical fix; non-mechanical impact; helps downstream audit traceability.

## Findings from prior sessions

| ID | Status | Module | Type |
|----|--------|--------|------|
| F1 | open | M1 | Canonical type drift |
| F2 | open | M1 | Stats schema |
| F3 | resolved | M2 | (PP-726 §2.1) |
| F4 | partial | M2 | Granularity (F6 blocks) |
| F5 | open | M2 | Edge-count math |
| F6 | open (Mode-C blocker) | M2 | Intra-YAML S-ID drift |
| F7 | open | M3 | §1.4.1 omits extras |
| F8 | open (info) | M4 | §1.5/§1.6 asymmetry |
| F9 | open (info) | M5 | Pacify formula |
| F10 | open | M5 | §3.2 omits extras |
| F11 | open | M5 | §3.3 Guilds Market ref |
| F12 | open | M6 | §4.5 omits extras |
| F13 | open | M6 | §4.5 prose pre-rebuild |
| F14 | open | M7 | §5.1 stale S-IDs |
| F15 | open | M7 | §2.2 omits City |
| F16 | open (info) | M8 | §4.5/§4.6 stale T-NN |

**Type-taxonomy drift family** (F1, F7, F10, F11, F12, F14) — six surfacings, one editorial pass would close all.
**Documentation drift family** (F2, F13, F14, F16) — four surfacings, similar editorial scope.

## Module 8 data model

```
StatureScope (enum) — 5 tiers per §6.1
RENOWN_THRESHOLD_*  (5 thresholds)
RENOWN_MIN = 0, RENOWN_MAX = 10
SETTLEMENT_GOVERNOR_FREE_ACTIONS_PER_SEASON = 1
MULTI_SETTLEMENT_MAX_SETTLEMENTS = 3

stature_scope_from_renown(renown) -> StatureScope

@dataclass StatureState                     # MUTABLE
apply_renown_delta(state, delta) -> int    # rebinds M3-M7 signals

EmergenceStage (enum) — 5 stages per §6.2
STAGE_RENOWN_FLOORS
stage_from_renown(renown) -> EmergenceStage

can_transition_2_to_3(state, npc_officers_at_high_disposition) -> (ok, reason)
can_transition_3_to_4(state, seats, declaration_roll) -> (ok, reason)
can_transition_4_to_5(state, seats_controlled) -> (ok, reason)

@dataclass FoundedFactionStats
founded_faction_starting_stats(renown, settlements) -> FoundedFactionStats
mandate_recovery_eligible(stability, hostile_das_targeting) -> bool

CollapseStage (enum) — 4 stages per §6.3
is_holdout_settlement(order, disposition) -> bool
can_contract_to_city_state(leader_alive, leader_in_own_settlement) -> bool
faction_dissolves(leader_dead, best_successor_standing) -> bool

count_recruitment_candidates(local_actors, faction_name) -> int     # T-23 bridge
THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[T-NN, str]                # audit
META_THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[М-N, str]            # audit
```

## Ledger entries this session

23 new (165 total cumulative).

## Next session — Module 9 (Extended timeline + clocks)

Force-full read: settlement_layer_v30 §7.1 (Clock Recalibration for 10–30 Year Games), §7.2 (Succession System Extended). Module 9 will:
- Wire the 30-year generational clock (T-25)
- Bind the М-1 continuous-pressure pattern (currently unbound primary) via clock ticks: MS Decay (T-04), CI Accumulation (T-05), IP Accumulation (T-06), Turmoil (T-07)
- Per-season Accounting hook that consumes M4 Chapel half-Order accumulator + M5 Ministry decay modifier + M6 governance-transition state machines
- Succession mechanics (player-character mortality, NPC heir promotion)

**5 modules remaining** before Module 13 integration runner.
