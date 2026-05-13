# Module Manifest — Settlement Management Stress Test
## Sim name: settlement_mgmt_stress_01
## Date: 2026-05-13
## Mode: G (Incremental Build Protocol)
## Status: PROVISIONAL — manifest under Jordan review; module-1 begins after greenlight.

---

## Scope

General validation of settlement management as canonically specified across
`settlement_layer_v30.md` and supporting docs. Full simulations: every
sub-system isolated (Mode A), every documented interaction chained (Mode B),
multi-season campaign runs with full state tracking (Mode C), 9-category
edge-case sweep (Mode D), and a 50+ seed batch.

**This is a new full-stack sim across 12 mechanical modules.** Existing
sim_settlement_economy.md (2026-04-18) checked three narrow items (treasury
income, Order→Accord, siege attrition) — not reusable as harness. Existing
sim_mb_06_* covers mass-battle internals only. No prior end-to-end settlement
harness exists.

The 13th module is the integration + stress runner.

---

## Decisions locked-in (defaults; Jordan may override before any module begins)

1. **Mode-13 ordering:** A → B → C → D → batch. Edge-case sweep (D) follows
   isolation/interaction/scenario to ensure prior probability is well-mapped
   before pushing thresholds.
2. **Companion depth in Module 8:** settlement-side effects only. Companion
   spec read only where it bears on faction emergence (§6.2) and Stature
   ladder (§6.1). Full companion sim is out of scope.
3. **Module 11 — videogame collapse:** stress canon as written (3-mode
   TTRPG/BG/Hybrid) AND the videogame-mode collapse per
   `designs/architecture/videogame_mode_spec.md`. Any divergence between the
   two is flagged explicitly in the module 11 report rather than silently
   reconciled.
4. **Pre-Module-13 prior-sim mining:** dedicated short session before Module 13.
   Mine `sim_faction_ambition_*`, `sim_companions_*`, `sim_run22_*`,
   `sim_open_items_*`, `sim_settlement_economy.md`, `sim_territory_ops_*` for
   prior findings to avoid re-discovery. Adds ~1 session.
5. **Stop condition:** Module 13 completes when (a) Mode D produces no
   unfixed P1 or P2 findings, (b) 50-seed batch shows no canon-contradicting
   outcomes, (c) coverage matrix lists every §-level mechanic touched by at
   least one mode. Each gate is hard; partial completion is not done.

---

## Session-budget summary

| Phase | Sessions |
|------|----------|
| Manifest commit (this session) | 1 |
| Modules 1–12 build + verify | 12–15 |
| Pre-13 prior-sim mining | 1 |
| Module 13 stress runner | 2–3 |
| **Total** | **16–20 sessions** |

Quality > efficiency > completion. Per-module session that cannot complete
within budget writes a checkpoint and resumes next session — no compression.

---

## Module dependency graph

```
   1 ── settlement primitives (substrate)
   ├── 2 ── political hierarchy + adjacency
   ├── 3 ── facility tiers + capacity pressure
   │    └── 4 ── church/parish/pastoral
   │         └── 5 ── dual-authority governance
   │              ├── 6 ── settlement events + thread ops
   │              ├── 7 ── military granularity (also needs 2)
   │              │    └── 8 ── player progression (also needs 5)
   │              │         └── 9 ── extended timeline
   │              ├── 10 ── fractional province ownership (also needs 2)
   │              ├── 11 ── scale transitions (also needs 6)
   │              └── 12 ── faction layer integration (also needs 8)
   │
   13 ── integration + stress runner (depends on ALL)
```

---

## Modules

| # | Name | Depends On | Sessions | sim_gate systems |
|---|------|-----------|----------|------------------|
| 1 | Settlement primitives | — | 1 | settlement_layer, territories |
| 2 | Political hierarchy + adjacency | 1 | 1 | territories, settlement_layer |
| 3 | Facility tiers + capacity pressure | 1 | 1 | settlement_layer |
| 4 | Church / parish / pastoral | 1, 3 | 1 | settlement_layer, campaign_architecture |
| 5 | Dual-authority governance | 1, 4 | 1 | settlement_layer, faction_layer, factions |
| 6 | Settlement events + thread ops + actors | 1, 5 | 1–2 | settlement_layer, threadwork, clocks |
| 7 | Military granularity | 1, 2, 5 | 1 | settlement_layer, military_layer, mass_combat |
| 8 | Player progression — Stature + emergence/collapse | 1, 5, 7 | 1–2 | settlement_layer, player_agency, companion_spec |
| 9 | Extended timeline — clocks + succession | 5, 8 | 1 | settlement_layer, clocks, faction_succession_split |
| 10 | Fractional province ownership | 2, 5 | 1 | territories, faction_layer |
| 11 | Scale transitions at territorial scope | 1, 5, 6 | 1 | scale_transitions, videogame_mode_spec |
| 12 | Faction layer integration | 1, 5, 8 | 1 | faction_layer, peninsular_strain, factions |
| 13 | Integration + stress runner (Modes A/B/C/D + batch) | ALL | 2–3 | ALL above |

---

## Module 1 — Settlement primitives

**Purpose.** Build the substrate every later module imports: settlement
type enumeration, the §1.3 stat block, and the 35+1 settlement registry
(35 Kingdom settlements across 14 provinces in 3 duchies, plus
Himmelenger as Church city-state).

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §1.1 (Two-Tier Map), §1.2
  (Settlement Types), §1.3 (Settlement Stats), §2.1 (Settlement Registry).

**Build:** `module_01_primitives.py` — dataclasses for Settlement, Duchy,
Province; registry loader; stat-block validators.

**Isolation tests:** registry parses to 35 Kingdom + 1 city-state; every
settlement has all §1.3 stats; settlement-type enum exhaustively covers
the §1.2 list.

**Ledger requirement:** every numeric in §1.3 (stat ranges, defaults) +
the 36 registry entries (settlement ID, type, province, duchy) cited to
file + section + quoted text.

---

## Module 2 — Political hierarchy + adjacency

**Purpose.** PP-726 hierarchy (Valn → Kingdom → Duchy → Province →
Territory=Settlement). Adjacency graph: 56 edges including 5 Himmelenger
inter-province edges + 1 Schoenland sea-edge. ≥2-march-route rule per
settlement (except Schoenland exempt). Province fracturing rule.

**Canonical sources (force_full=True):**
- `designs/territory/valoria_political_hierarchy_v30.md` (full doc).
- `designs/territory/settlement_adjacency_v30.md` (full doc).
- `designs/territory/valoria_geography_v30.yaml` (the adjacency YAML — full).
- `designs/territory/march_layer_v30.md` (skeleton — referenced from
  canonical_sources.yaml :: territories.march_layer_skeleton).

**Build:** `module_02_hierarchy.py` — graph loader, adjacency validator
(every settlement ≥2 edges with Schoenland exempt), duchy/province
aggregators, fracturing-rule predicate.

**Isolation tests:** every settlement passes ≥2-edge rule (Schoenland
exempt); duchy → province → settlement totals match canon (14 provinces,
35+1 settlements); Himmelenger has exactly 5 connections.

---

## Module 3 — Facility tiers + slot allocation + capacity pressure (PP-661)

**Purpose.** §1.4 mechanism — facility slot capacity per settlement type,
allocation rules (§1.4.2), capacity pressure as political mechanic
(§1.4.3), cross-faction wing allocation (§1.4.4).

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §1.4.1, §1.4.2, §1.4.3,
  §1.4.4 (PP-661 — 1,798 tokens consolidated).

**Build:** `module_03_facilities.py` — slot-capacity tables per settlement
type; allocation rules; pressure-counter; cross-faction wing predicate.

**Isolation tests:** every settlement type's slot-capacity matches §1.4.1
table; allocation rules enforce §1.4.2 constraints; pressure correctly
fires the §1.4.3 political mechanic threshold.

---

## Module 4 — Church infrastructure + parish + pastoral assumption

**Purpose.** §1.5 four independent Church axes (campaign_architecture_v1
Part 1); §1.6 parish social services; §1.7 pastoral assumption.

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §1.5, §1.6, §1.7.
- `designs/architecture/campaign_architecture_v30.md` Part 1 (four-axis
  Church infrastructure source).

**Build:** `module_04_church.py` — axis tracker (4 independent counters per
settlement); parish service register; pastoral-assumption modifier; cross-
links to Module 3 facility allocation (Church facilities consume slots).

**Isolation tests:** four axes track independently; parish services
trigger per §1.6; pastoral assumption modifier applies per §1.7 conditions.

---

## Module 5 — Dual-authority governance

**Purpose.** §3 governor assignment + subnational faction governance. Two
tiers: faction (national) authority over the settlement and governor
(local) authority. Loyalty, succession edge cases, subnational faction
visibility.

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §3.1, §3.2, §3.3.
- `designs/provincial/faction_layer_v30.md`.
- `designs/provincial/factions_personal_v30.md`.
- `designs/provincial/faction_canon_v30.md` (Stage 1 consolidation).

**Build:** `module_05_governance.py` — Governor + Faction authority
classes; assignment rules per §3.2; subnational faction registry; loyalty
tracker.

**Isolation tests:** governor assignment rules match §3.2 cases; subnational
faction tracker matches §3.3 cases; loyalty cascade does not produce
incoherent dual-claim states.

---

## Module 6 — Settlement events + thread ops + local actors + POI templates

**Purpose.** §4 settlement-as-gamespace mechanics: scene-slate anchoring
(§4.1), subnational visibility (§4.2), settlement events (§4.3), thread
ops at settlement level (§4.4 / Throughline T1), local actors (§4.5 / T7),
POI templates (§4.6 / T3).

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §4.1–§4.6.
- `designs/threadwork/threadwork_v30.md` (relevant sections for settlement-
  scale ops).
- `designs/provincial/clock_registry_v30.md` (events feed clocks).

**Build:** `module_06_events.py` — event generator with §4.3 event table;
thread-op handler (settlement-scope); local-actor registry; POI templates;
clock-feed integration.

**Isolation tests:** every §4.3 event type fires under its canonical
trigger; thread ops at settlement level resolve per §4.4; clock feeds
match clock_registry §settlement entries.

---

## Module 7 — Military granularity (invasion + garrison)

**Purpose.** §5.1 invasion mechanics: armies march along adjacency edges
(Module 2); each settlement is a siege target; §5.2 garrison and defense.

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §5.1, §5.2.
- `designs/provincial/military_layer_v30.md`.
- `designs/provincial/mass_battle_v30.md` (skeleton — battle internals
  remain sim_mb_06's scope; settlement sim uses results at outcome-level).

**Build:** `module_07_military.py` — invasion route resolver (uses Module
2 adjacency); siege-attrition (extends sim_settlement_economy.md prior
finding); garrison composition; defense-vs-attack predicate that delegates
detailed combat to sim_mb_06 outputs at integration time.

**Isolation tests:** invasion only traverses valid adjacency edges; siege
attrition matches the 1-year-for-Size-4 prior finding; garrison rules
match §5.2.

---

## Module 8 — Player progression — Stature ladder + faction emergence/collapse

**Purpose.** §6.1 Stature ladder (canonical reference for player_agency §5.4),
§6.2 faction emergence (local → national), §6.3 faction collapse (national →
local).

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §6.1, §6.2, §6.3.
- `designs/architecture/player_agency_v30.md` §5.4 (Stature ladder
  canonical reference).
- `designs/npcs/companion_specification_v30.md` (settlement-side effects
  only per locked-in decision 2; full companion sim out of scope).

**Build:** `module_08_progression.py` — Stature tracker; emergence
threshold predicate (settlement-faction → provincial → national);
collapse cascade (national → provincial → settlement subnational).

**Isolation tests:** Stature ladder transitions match §6.1; emergence
fires at canonical thresholds (§6.2); collapse cascades per §6.3 without
producing incoherent governance states.

---

## Module 9 — Extended timeline — clock recalibration + succession

**Purpose.** §7.1 clock recalibration for 10–30 year games; §7.2 extended
succession system.

**Canonical sources (force_full=True):**
- `designs/territory/settlement_layer_v30.md` §7.1, §7.2.
- `designs/provincial/clock_registry_v30.md` (clock pacing).
- `designs/provincial/faction_succession_split_v30.md` (succession edge cases).

**Build:** `module_09_timeline.py` — clock-pacing modifier per §7.1;
succession event generator per §7.2; integration with Modules 5 (governor
succession), 8 (faction collapse via missing succession).

**Isolation tests:** clock recalibration matches §7.1 for 10y/20y/30y
games; succession produces canonical outcomes for each §7.2 case.

---

## Module 10 — Fractional province ownership

**Purpose.** A province whose settlements align to different factions
fractures; canonical fracturing rules and political-value computation
(PP-726 §2.3 + fractional_province_ownership_v30).

**Canonical sources (force_full=True):**
- `designs/provincial/fractional_province_ownership_v30.md` (full doc).
- `designs/territory/valoria_political_hierarchy_v30.md` §2.3.

**Build:** `module_10_fractional.py` — fracturing predicate; PV
re-aggregation under fractional ownership; integration with Module 5
(governance under fractional state).

**Isolation tests:** fracturing fires per §2.3; PV computation matches
fractional canon; mixed-faction provinces produce no contradictory
governance.

---

## Module 11 — Scale transitions at territorial scope

**Purpose.** Settlement (Territorial scale per scale_transitions §2 table:
Base Ob 4, Min Thread Sensitivity 50+, Coherence auto-cost −1). Handoff
rules §3.4 (Scene→Faction Domain Echo), §3.5 (Thread→Faction), §5 Domain
Echo amount/timing/cap. Plus videogame-mode collapse per
videogame_mode_spec.

**Canonical sources (force_full=True):**
- `designs/architecture/scale_transitions_v30.md` (full doc — esp. §2
  scale table, §3.4, §3.5, §5 Domain Echo, §6 mode transitions, §7
  sufficient scope).
- `params/scale_transitions.md` (full doc).
- `designs/architecture/videogame_mode_spec.md` (full doc — for
  videogame-only collapse per PI; locked-in decision 3 stresses both
  representations).

**Build:** `module_11_scale.py` — Domain Echo handler with ±2/scene cap;
sufficient-scope predicate per §7; videogame-mode collapse handler that
maps canonical 3-mode states to videogame events.

**Isolation tests:** Domain Echo cap enforced; Sufficient Scope trigger
matches §7 conditions; videogame collapse preserves canonical mechanical
outcomes (no silent reconciliation; divergences flagged).

---

## Module 12 — Faction layer integration

**Purpose.** Settlement-level state feeds Accord, Turmoil, peninsular
strain. Subnational faction → national faction transitions integrate
with peninsular-strain mechanics.

**Canonical sources (force_full=True):**
- `designs/provincial/faction_layer_v30.md` (full).
- `designs/provincial/faction_canon_v30.md` (Stage 1 framework + Crown +
  Church sheets).
- `designs/provincial/peninsular_strain_v30.md` (full — Accord, Turmoil,
  victory-condition surface).

**Build:** `module_12_faction_integration.py` — Accord aggregator from
settlement-level Order; Turmoil feed; strain-event handler.

**Isolation tests:** Accord aggregation matches peninsular_strain canon
for sample configurations; Turmoil feeds match Module 6 event outputs;
strain-event triggers match peninsular_strain §canonical thresholds.

---

## Module 13 — Integration + stress runner

**Prerequisite:** Modules 1–12 all `status: verified` in manifest.

**Sub-prerequisite session:** prior-sim mining. Read
`sim_faction_ambition_2026-04-16.md`, `sim_companions_2026-04-16.md`,
`sim_run22_*`, `sim_open_items_2026-04-16.md`,
`sim_settlement_economy.md`, `sim_territory_ops_SIM-TERR-0[12].md`.
Extract prior findings that bear on settlement validation. Produce
`tests/sim/settlement_mgmt_stress_01/prior_findings.md` so Module 13
doesn't re-discover known issues.

**Integration session:** wire all modules. No new mechanics. If a module's
API mismatches, flag for rebuild (do not patch inline).

**Stress-run sessions:**

### Mode A — isolation
Probability tables for every dice-resolved mechanic surfaced across
Modules 1–12. Reference table from skill: TN7 pool {4D/6D/8D/10D/12D/15D}.

### Mode B — interaction chains
Documented chains:
1. Capacity pressure (§1.4.3) → political fracture → subnational faction
   visibility (§4.2) → faction emergence (§6.2)
2. Governor assignment (§3.2) → loyalty cascade → garrison reliability
   (§5.2) → invasion outcome
3. Church axis competition (§1.5) → cross-faction wing allocation (§1.4.4)
   → subnational faction realignment
4. Settlement event (§4.3) → clock feed → strain (peninsular_strain) →
   faction collapse (§6.3)
5. Stature climb (§6.1) → faction emergence (§6.2) → Domain Echo (§5
   scale_transitions) → national-faction state delta

### Mode C — full campaign scenarios
Two sizes: 10-year and 30-year. Track all 35+1 settlements across the
campaign. Inject succession event at multiple points per §7.2. Record
faction emergence + collapse arcs.

### Mode D — edge-case discovery (9-category sweep)
- **Boundary:** every settlement-stat threshold; §1.4.3 pressure
  thresholds.
- **Cascade:** capacity pressure overflow; faction collapse propagation.
- **Regression:** §1.4.2 allocation rules; recursive subnational faction
  emergence.
- **Deadlock:** every facility slot dual-claimed by competing factions.
- **Crunch cascade:** player decision load at peak settlement count
  (videogame UX surface).
- **Ambiguity:** governor-dispute boundaries; province-fracture at exactly-
  even split.
- **Incoherence:** fractional + subnational faction overlap that produces
  contradictory authority.
- **Optimal play:** stature-ladder exploits; emergence stacking.
- **Degenerate:** 0-settlement faction, saturated-faction-emergence state.

### Batch run
50+ seeds across diverse starting conditions: each duchy as starting
power; Almund pre/post hypothetical assassination; Calamity-zone
propagation vs healing.

---

## Hook expectations (per module session)

1. Bootstrap → `h.assert_bootstrap()`.
2. `h.task_gate('simulation')`.
3. `g.read_files_graphql([...module canonical sources...], force_full=True)`.
4. Verify with `g.read_depth_report(paths)` — every path reads `full`.
5. Populate `/home/claude/sim_verification_ledger.json` with every
   mechanical constant for this module: sim_variable, value,
   canonical_source, section, quoted_text. Quoted_text must literally
   appear in the fetched content.
6. `h.sim_gate('custom', systems=[...module systems list per table...])`.
7. Write module code with inline `# [canonical: path §section]` comments
   on every mechanical constant.
8. Run module in isolation against canonical fixtures.
9. `h.safe_commit([(module_path, content), (manifest_update, content),
   (ledger_snapshot, content), (coverage_matrix_update, content)],
   deletions=[], message='[simulation] module N <name> — settlement_mgmt
   stress 01 build')`.
10. Update `session_log_current.md` via `g.update_session_log` /
    `g.close_session_log`.

---

## Anti-patterns (re-stated from skill Mode G)

- No multi-module code in a single session.
- No mechanical constant without ledger entry or inline citation.
- No assumption that a previously-built module is still correct — each
  session re-fetches what it imports.
- No cross-module patching during integration — flag for rebuild.
- All artifacts commit to `tests/sim/settlement_mgmt_stress_01/`.

---

## Open items

- Status: PROVISIONAL — Jordan reviews. Decisions 1–5 above are defaults
  that may be overridden before module 1 begins.
- Companion specification scope may need to widen if Module 8 isolation
  tests reveal companion mechanics gate emergence.
- Module 11 dual-representation (canonical 3-mode + videogame collapse)
  may produce divergences requiring a design decision; flagged in the
  module 11 report, not silently reconciled.
- Module 13 stop condition is hard. If P1/P2 findings cascade beyond fix
  scope, escalate to canon editorial rather than weakening the bar.

---

## 2026-05-13 Scope addendum — player action loop (Jordan)

The stress test validates not just system mechanics in isolation but the
**player action loop**: characters manage settlements (improve / maintain /
problem-solve), settlement state mutates per canonical rules, faction Order
and Accord shift, faction standing and renown deltas surface, available
player actions update.

**Loop structure:**

1. Player chooses an action at settlement scope (improvement, maintenance,
   or problem resolution).
2. Action resolves per the responsible module's mechanic:
   - Improvement → Module 3 (facility tier upgrade), Module 4 (Church axis)
   - Maintenance → Module 7 (garrison/defense), Module 9 (clock pacing)
   - Problem-solve → Module 6 (settlement event), Module 7 (invasion)
3. Settlement state mutates (Module 1 substrate: Prosperity / Defense /
   Order; Module 3 substrate: facility allocation; etc.).
4. Province Accord recomputes (Module 1 `province_accord_from_settlements`).
5. Faction Order / Turmoil propagates (Modules 5, 12).
6. Faction standing delta surfaces; Stature ladder may shift (Module 8).
7. Domain Echo if Sufficient Scope (Module 11).
8. Player-visible feedback: renown change, new actions unlock or close.

**Module 13 Mode B chains** must each be triggerable by a player action.
**Mode D** includes:
- Action that produces no settlement-state delta (broken loop)
- State delta with no faction-standing feedback (broken loop)
- Unintended cascading feedback (over-coupled loop)
- Action whose feedback is delayed past the player's planning horizon
  (unreadable loop)

This addendum reframes the stress target without changing the module
decomposition.

---

## Count correction (2026-05-13)

Total settlements is **37** (35 Kingdom + 1 Church city-state + 1 foreign
tributary), not "35+1" as drafted in V1 of this manifest. Schoenland
(S-037) is foreign Altonian per §2.1.

---

## Module status

| # | Name | Status | Date |
|---|------|--------|------|
| 1 | Settlement primitives | **verified** (15/15 isolation tests; F1–F4 surfaced) | 2026-05-13 |
| 2 | Political hierarchy + adjacency | **verified** (22/22 isolation tests; F5-F6 surfaced; F3 resolved; F4 partial) | 2026-05-13 |
| 3 | Facility tiers + capacity pressure | pending | — |
| 4 | Church / parish / pastoral | pending | — |
| 5 | Dual-authority governance | pending | — |
| 6 | Settlement events + thread ops | pending | — |
| 7 | Military granularity | pending | — |
| 8 | Player progression — Stature | pending | — |
| 9 | Extended timeline | pending | — |
| 10 | Fractional province ownership | pending | — |
| 11 | Scale transitions | pending | — |
| 12 | Faction layer integration | pending | — |
| 13 | Integration + stress runner | pending | — |

---

## Changelog

- 2026-05-13 — manifest created. Mode G Session 1.
- 2026-05-13 — Module 1 verified (15/15 tests). 2026-05-13 scope addendum:
  player action loop targets added. Count correction: total is 37
  (35 + Himmelenger + Schoenland). Findings F1–F4 surfaced.
- 2026-05-13 — Module 2 verified (22/22 tests). F3 resolved (rebuild §2.1
  reconciles 17 vs 14+3); F4 partially resolved (stats exist in geography
  YAML); F5 NEW (adjacency header math: 56 asserted vs 55 actual); F6 NEW
  (intra-YAML S-ID granularity drift — settlements block at pre-rebuild
  granularity blocks Module 13 Mode C campaign sim).
