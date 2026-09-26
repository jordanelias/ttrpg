# Squad Engagement Engine v5, reconciled against mass-battle canon: what to build, what not to, what Jordan decides

## Status: RULED (Jordan, 2026-09-25) — design decided; unimplemented

**Date:** 2026-09-25 · **Lane:** MB · **Ledger:** `ED-MB-0067` (two rows — the second records this ruling; the
last row governs).
**Ratify-on-merge (ED-1094):** merging ratifies **Parts A, B and C** — Jordan ruled Part C directly, in session,
after this document was first drafted; the ruling is recorded in Part C below and in `ED-MB-0067`'s second row.
**Not yet done:** nothing in this document has been built. Directive d.1 (below) overwrites PP-711 and still
needs its own propagation into `mass_battle_v30.md`; the exact mechanical coupling for C2–C4 is follow-up design
work, not settled by the ruling itself.

**Inputs.**

1. *Squad Engagement Engine — Concept Proposal v5* (2026-09-23; self-described "CONCEPT · non-canonical · not
   bootstrapped"; 748 lines). **Not in this tree** — uploaded to the 2026-09-25 session. `concept:N` below is its
   line N. By its own account it never read this repository's canon (concept:4), and what it grounds on
   (`valoria_authoritative_map_v1.md`, `valoria_authoritative_graph_v1.md`, a v4 critique) is not in this tree
   either, so its `[READ: map_v1]` / `[READ: graph_v1]` values are unverified here.
2. A **read-only adversarial comparative audit** of v5 (2026-09-25) against `mass_battle_v30.md` and
   `mass_battle_integration_v30.md` (both `## Status: CANONICAL`), the executable oracle `systems/mass_battle/sim/`,
   `proposals/multiunit_envelopment_plan.md`, `proposals/mass_battle_fighting_withdrawal_v1.md` and the MB ledgers.
   It was returned to the orchestrating session, not committed. Its finding labels **F1–F21** are kept below as
   labels only; every item carries its own citations, so the audit need not be opened. The orchestrator
   spot-checked its four highest-stakes claims; this synthesis re-opened ED-1090, ED-MB-0039/0041/0045, ED-780 and
   `ROUT_CASCADE_FRAC`'s own rule, and corrects the audit in two places (C3, A7).

**Conventions.** A `.py` path with no top-level directory (`config.py:N`, `core/exchange.py:N`,
`hierarchy/units.py:N`) is under `systems/mass_battle/sim/`. `*_v30.md` names are design documents, named by bare
filename as `CURRENT.md` names them. They are cited for intent and for what Jordan ruled — **never as the reason a
behaviour is correct**; the code is the mechanism (CLAUDE.md §0.05).

---

## The concept, reframed

v5 presents itself as an engine rewrite founded on retiring the Mass pool. **That retirement already happened:**
ED-MB-0006 (2026-07-08, Jordan) made the pool "solely derived from the subunit troop type, quality and numbers",
shipped default-ON as `POOL_QUALITY_MODEL`. Of the rest, much renames shipped default-ON mechanics (fighting
withdrawal, fatigue, volley density, role presets), contradicts rulings the concept never read (continuous morale,
the single degree ladder, prepared brace, the cell as the route and facing primitive), or is written for a
substrate this repository retired (Keys). **What survives is real and absent from the sim: a command / perception /
plan layer** — routed waypoints, order conditions limited to what a unit can see, orders that take time to arrive
(messengers, go-codes, signal relay), subordinate officers holding their own Cmd — plus missile ammunition,
battlefield terrain, a value for one deliberately-unchosen constant, and a per-cell quality refinement in the
direction ED-MB-0006 already sanctioned. All of it composes on the shipped `Order` / `instructions` / `stance`
machinery and replaces none of it. **Read v5 as that layer on top of the shipped engine, not as a new engine.**
Where the concept bought its elegance by amputation (Discipline, fatigue, the degree ladder), the amputation is
declined, not debated; Part A adds friction and perception the sim lacks and removes nothing it has, so its E is
judged per item as each lands, as a ratio against what N and R find (CLAUDE.md §0.06).

---

## Part A — Build now: no further ruling

Every item composes on a shipped primitive; none replaces one. By precedent, each ships **default-ON** under the
standing flags-ON rulings (`config.py:331`; `registers/handoffs/HANDOFF_MB_history.md:186`, *"implement all
proposals. nothing is golden here"*); an item that moves a seeded golden re-records it **and says so** (CLAUDE.md
§7). **Done means a test runs the behaviour** (§0.2); each *done when* names that test's assertion.

**A1. Routes with waypoints.** Compose on `_resolve_maneuver_goal` (`hierarchy/units.py:1103`), whose docstring
names routes as its unbuilt extension, and on the sequential orders queue (`hierarchy/units.py:316-356`). Jordan's
ruled path-length budget `0.5·speed·max-ticks` (`hierarchy/units.py:1121-1128`) already bounds a route.
*Done when* a sub-unit ordered through waypoint B passes B before C, and the path budget still binds.

**A2. Order conditions limited to what the unit can know** (concept §4.3, :230-244). The five trigger kinds —
`immediate`, `tick:`, `enemy_range:`, `ally_at:`, `own_strength:` (`core/contact.py:14-67`) — are omniscient today:
`enemy_range:` reads every enemy cell. Filter them through what the observer can see; terrain cover joins when A7
lands. *Done when* an enemy inside range but out of sight does not fire `enemy_range:`, and the same enemy in sight
does.

**A3. Subordinate-officer Cmd — ED-1090's lieutenancy.** ED-1090 (2026-07-02) left this open: Command clamps 1–7,
so fielding more commanded sub-units "implies a future Command-exceeding mechanism (e.g. subordinate
officers/lieutenancy) — a future ED, not silently invented in the constructor". **`ED-MB-0067` is that ED.** The
concept supplies the officer: a post holding Cmd, from the named character in it, else a default by quality tier
(concept:193, :197). Build the post over one or more sub-units, reusing the Command derivation
(`core/exchange.py:42-51`), so the general's cap (`engine.py:90-99`) counts the officers he commands rather than
every sub-unit. The ladder an officer's own reach follows is C5 (default: the existing "= Command"); the concept's
⌊Cmd/2⌋ Steadiness contribution belongs to C3, not here. *Done when* a general with Command *c* fields more than
*c* sub-units through officers.

**A4. Orders that take time to arrive — messengers, go-codes, signal relay** (concept §6.2–6.3, :363-380). Today
an Order fires on the tick its trigger is met (`hierarchy/units.py:316-356`); **no transmission latency exists.**
Add an issue→effect delay by messenger distance from the general's cell; go-codes as pre-issued Orders whose
trigger is a signal (a sixth kind beside the five in `core/contact.py`); relay through A3's officers. Canon Command
uses that are orders ride the same latency (recall, Ob 2, `orchestration.py:2469-2474`). ⚠ `target_delay_ticks`
(`core/contact.py:74-78`; `hierarchy/units.py:377`) is a one-shot **reserve hold before first targeting**, not
transmission latency — reuse its countdown pattern, do not overload its meaning. *Done when* an order issued at
tick *t* to a sub-unit *d* cells from the general takes effect only after the messenger delay, and a go-code fires
on its signal in every sub-unit holding it.

**A5. Role instincts.** Extend `TROOP_TYPE_ROLES` / `ROLE_SPEC` (`config.py:462-499`, "the FM position→role
model"), applied at construction (`engine.py:197-199`, `:292-300`; engine half built per
`proposals/pc_formation_system.md`). The concept's one addition: a role's *instinct* is the first rule of its
preset — what the sub-unit does absent a live order (concept §4.5, :269-302). The instinct is data in `ROLE_SPEC`,
not code per role. *Done when* a sub-unit with an empty or exhausted order queue acts on its role's instinct.

**A6. Missile ammunition and resupply** (concept:489-490). Nothing in the sim counts volleys (`volleys|ammo` hits
only two comments, `orchestration.py:107`, `:371`); canon has sling ammunition *types* only
(`mass_battle_v30.md:93-101`). Add a volleys track on missile cells — per cell, as stamina already is
(`percell.py:254-309`) — spent by the volley phase (`orchestration.py:1550-1637`) and refilled by a resupply rule.
Density stays `MB_VOLLEY_DENSITY_*` (`config.py:184-187`). *Done when* a missile sub-unit that has spent its volleys
stops shooting, and resupply restores it.

**A7. Terrain, battle-wide, from the strategic map.** This closes the concept's `[OPEN — Jordan decision]`
(concept:439): canon already answers "where terrain comes from" with the concept's own first candidate, territory
data. A.9's six rows (river crossing, uphill, forest/broken, walls, narrow pass, open flat;
`mass_battle_v30.md:544-553`) plus ED-780's derivation (`:555-556`): the battle's row is found by querying the
geography at the engagement coordinates, dominant polygon by area. The coordinates come from the battle's caller
(`massbattle.py:99-146`, the campaign adapter). ⚠ **Correction to the audit and to canon's text:** the data lives at
`systems/settlements/valoria_geography_v30.yaml`, key **`terrain:`** (typed polygons, `:675`), with crossings from
`water:` / `bridges:` and walls from each province's `fort_level`; canon's `designs/territory/…::terrain_polygons`
is stale in both path and key. The sim has no terrain today. Per §0.05, A.9's rows become data the code reads, with
the geography-type→row map authored once beside them — never parsed out of the `.md`. *Done when* a battle placed
in a `mountain_pass` polygon resolves under A.9's narrow-pass row and one on open ground resolves unmodified.

**A8. Choose `ROUT_CASCADE_FRAC` by its sweep — do not assert 0.5.** `config.py:116` (default `1.0`, "magnitude
UNCHOSEN"), read by `_broken_share` / `derive_rout` (`hierarchy/units.py:2431-2466`). Its own rule
(`config.py:51-54`): "chosen on evidence rather than asserted — the sweep over candidate values is the experiment",
and the value "is CALIBRATED-DEBT until something outside the engine supports it". The concept's army-breaks-at-half
rule (concept:506-519) is the candidate **0.5** — the value the cell→sub-unit sibling `CELL_BREAK_ROUT_FRAC`
already holds (`config.py:113`), so landing it would put both break ladders on one methodology. Target the
historical 15–30% loser-casualty band the comment names (`config.py:44-47`), never the gauge rows
(`tests/sim/gauge_mb.py:55-56`). *Done when* the sweep's table is committed with the value it chose, marked
CALIBRATED-DEBT, and the goldens it moved are re-recorded and named.

**A9. Causes on trace rows — only if the concept's turning-points report is wanted** (concept:630). The
observe-only trace seam (`resolution.py:10-34`: `start_trace` / `trace_event` / `get_trace`), per-source casualty
attribution (`orchestration.py:1714-1746`), position snapshots (`:1666-1695`), `workbench/trace.py`, and seeded
replay (`rngsource.py:24-30`; `massbattle.py:124`) already exist. The whole delta is a `causes` field on
`trace_event` rows. *Done when* a seeded battle's trace names the events behind its decisive rout, and two runs on
one seed give the same report.

### Sequenced — build when the named prerequisite lands

| item | waits on | then |
|---|---|---|
| **Per-cell quality (Q)** — F1's live residue | something that makes cells of one sub-unit differ in type or quality; and ED-MB-0041's Tier-3 depth-cap item for the engaged-rank count, against the live `SUPPORT_WEIGHTS` stack (`core/exchange.py:204-206`) | Direction sanctioned by ED-MB-0006's follow-up, "subunit power is the aggregate or derivation of cell power"; `core/exchange.py:100-109` records per-cell troop type "doesn't exist yet". Until cells differ, `pair_pool_contribution` / `_pair_engaged_troops` (`core/exchange.py:137-207`) already weight the exchange by real per-cell troops and give the same answer. The concept's "grade" is canon's Power tier ladder, Levy…Elite (`mass_battle_v30.md:182-191`) — use that name (CLAUDE.md §4). Its type profile maps onto `troop_types/registry.py:36-54` (stats), `:87-100` (reach), `hierarchy/units.py:2373-2377` (speed tiers, `[ASSUMPTION]`), `equipment/weapons.py:38-45` (provisional, unwired). *Falsifier:* a sub-unit whose cells differ in Q pools differently from its troop-weighted mean Q. |
| **Army-scale plans and envelopment** | `proposals/multiunit_envelopment_plan.md` Phase 1 — one engagement field across Units (Path B, confirmed by Jordan 2026-06-22 at `:74`; never started). `run_multi_unit_battle` still resolves isolated pairs (`orchestration.py:2662-2673`) with a 2v1 stub (`:2745-2749`) | A1–A4 then span Units unchanged. That plan's Phase 0 spike (`:42`) is its cheapest first step. |
| **A generated battlefield map** — the concept's second terrain candidate (concept:439) | A1's routes existing to be shaped by it | A seeded generator whose input is A7's terrain row; never a hand declaration (ED-780: "no separate declaration required"). |
| **AI generals authoring plans** (concept §4.7; "unbuilt core deliverable", :323) | A1–A4 | Until then, headless battles take their plans from the Unit-level presets that already emit Orders (`engine.py:355-509`); the concept's "templates" (§4.6) are those presets. |
| **Headless NPC-vs-NPC duels** (concept:409-415) | a mass_battle provider on the season seam — the loop does not call mass_battle (`engine/season/seam/contest.py:142-179`; `engine/season/rosters.yaml:751-757`, "NO PROVIDER") | Cadence is already canon (F16, Part B). |
| **Strategic outputs** — killed / scattered / present, grade progress, familiarity, deeds (concept:589-598) | the seam calling mass_battle, and an owner in the strategic lane; today the adapter returns `{attacker_wins, degree, attacker_size_pct, defender_size_pct}` (`massbattle.py:99-146`) to `systems/factions/sim/faction_action.py:393-395` | "Familiarity" competes with Discipline's between-battle persistence (PP-712, `mass_battle_v30.md:651-662`) for one campaign role; pick one owner then. |

---

## Part B — Do not build: superseded, irrelevant, or already shipped

Each entry is closed. **Re-proposing one needs a new argument, not the concept's.**

- **F1 — Retire the Mass pool** (concept:8, :18-23, :565, :683) and file a ledger row for directive b (:727).
  **Superseded** — ED-MB-0006, above. `min(Size,Cmd)+Cmd` has been the OFF-path ablation branch since 2026-06-02,
  and the head already carries the supersession banner: no row, no propagation list. "Size" survives only as the
  pool's numbers term `cur_troops/BLOCK_SIZE` — the concept's own N — and is not spatial (cells come from troop count
  and density). The live residue is per-cell Q, sequenced above. — `config.py:405-440`; `core/exchange.py:89-110`;
  `hierarchy/units.py:831-835`; `mass_battle_v30.md:49-78`; `registers/editorial_ledger_mb_archive.jsonl:6`
- **F2 — Casualties drawn straight from a continuous Normal on output** (concept:470-478). **Precedent: ONE degree
  ladder for every scale** (S39.4): roll → `compute_degree` → `DAMAGE_BY_DEGREE` → frontage-capped Lanchester →
  octagon multiplier. The concept's continuous sampler exists (`engine/autoload/dice_engine.py:209-224`) and may be
  used — to sample **net successes** into the ladder, never casualties. A deterministic μ-shift was already rejected
  (`resolution.py:62-69`). — `engine/season/seam/contest.py:181-184`; `resolution.py:104-120`;
  `config.py:297-298`; `core/attrition.py:12-43`; `orchestration.py:1346-1365`; guard
  `tests/valoria/test_degree_ladder_single_owner.py`
- **F3 — A discrete morale clock, "quantization intended"** (concept:96-117), plus adjacency contagion (:128-133).
  **Superseded:** morale is continuous, never rounded (ED-1024, Jordan 2026-06-17); the break point is drawn
  stochastically in the 15–30% casualty band (standing order: `MB_STOCHASTIC_ROUT` ON). Three contagion ladders are
  already live — sibling pull (ED-MB-0002), per-cell break propagation with the cell morale pull (`propagate_cell_breaks`, `cohere_cells`), the inter-unit cascade — and
  any contagion from the concept composes on one of them, never as a fourth. — `registers/editorial_ledger.jsonl:197`;
  `registers/handoffs/HANDOFF_MB.md:20`; `config.py:108`, `:153-177`, `:323-330`; `core/state.py:17-49`, `:82-89`;
  `hierarchy/units.py:671-692`, `:1992-2022`; `orchestration.py:2529-2540`, `:2766-2779`
- **F5, the stat — Drop Discipline to a UI label** (concept:192). **Precedent:** Discipline 1–7 persists between
  battles (PP-712) and has live consumers across the sim — speed, the node model's formation stiffness, brace preparation, rout resilience,
  degradation, reform, the cascade — and is on Jordan's cell-primitive list. Keep the stat and its name; do not coin
  "Steadiness" for it (CLAUDE.md §4). Whether any *check* moves to Pressure/Steadiness is C3. —
  `mass_battle_v30.md:209-228`, `:662`; `config.py:55`, `:191-197`; `core/exchange.py:23`;
  `hierarchy/units.py:1423`, `:1594`; `resolution.py:159-162`; `core/state.py:17-32`, `:197-238`;
  `orchestration.py:297-331`, `:2200-2204`, `:2534-2540`
- **F6 — Edit GD-2 to permit bounded variance** (directive d.2; concept:12, :27). **Irrelevant:** GD-2 is
  "deterministic threat response precedes stochastic action selection" — faction-AI ordering, nothing about battle
  randomness. The real constraint is seeded determinism, which the concept's seeded variance already meets. No GD-2
  edit (mutable canon needs Jordan's ratification), no row. — `canon/04_game_design_constraints.md:24`, `:29`;
  `rngsource.py:24-30`; `massbattle.py:108-113`; `engine/season/state/ids.py:38-46`
- **F7, the mechanics — Envelopment "not a special rule"** (concept:333). **Already shipped inside a Unit:** front
  fixers, the envelopment shock, `build_envelopment`, the orbital wheel (ED-MB-0035). Its *payoff* is C2; its
  *army-scale* reach is sequenced above. — `orchestration.py:695-724`, `:1156-1171`; `engine.py:355-449`;
  `hierarchy/units.py:1204-1238`; `config.py:374`
- **F8, the mechanics — Ordered Withdraw, a give-ground posture, withdraw-as-flight** (concept:253, :266, :287,
  :335). **Shipped under other names, default ON:** stance `'retreat'` and the `yielding` / `pocketed` states — entry
  gate, one-cell-per-tick cap, facing lock, pool malus, emergent entry, no-volley, rally exit. Compose on `yielding`.
  (`proposals/mass_battle_fighting_withdrawal_v1.md`'s status line still reads "GATED OFF"; the flags are `'1'`.)
  Its entry gate is C3. — `hierarchy/units.py:455-468`, `:597-604`, `:1344-1383`, `:1477-1478`, `:1522-1523`,
  `:1670-1672`; `core/exchange.py:18-29`, `:115-126`; `core/state.py:97-106`; `orchestration.py:1581-1587`;
  `config.py:256-267`; `tests/valoria/test_mass_battle_yield.py`; `tests/valoria/test_dg2_yield_residuals.py`
- **F9 — Leave fatigue out** (concept:441). **Shipped and ratified ON:** per-cell fatigue with depth-damped drain
  and reserve rest; `PER_CELL` defaults `'1'` under Jordan's "yes, all options/modules must be turned on"
  (ED-MB-0001). Keep. — `config.py:331`, `:344-348`; `percell.py:254-309`; `orchestration.py:1958-1978`; ED-1017
- **F10 — Brace as a passive per-type stat, armed by standing still, re-armed each contact** (concept:148-153).
  **Superseded by ED-1095:** brace "must be prepared ahead of time and intentionally set" — an Order, at least one
  full tick of setup, frontal- and reach-gated. The concept's "excess brace multiplies output" is the shipped
  reciprocal recoil `MB_CHARGE_RECOIL`; map its per-type B onto `'brace'` + `TROOP_TYPE_REACH`. Whether brace should
  become a *multiplier* is ED-MB-0041's queued cavalry item, not reopened here. —
  `registers/editorial_ledger.jsonl:288`; `resolution.py:132-157`; `core/contact.py:58-66`; `config.py:380-383`;
  `orchestration.py:1189-1198`, `:1220-1228`; `troop_types/registry.py:87-100`
- **F11 — A second gauge, `T_break ≥ 1.5 × T_flank`** (concept:547-555). **Precedent: one instrument.** If the
  timing race is measured, it is a row in the existing gauge, calibrated to independent history, never to its own
  rows. The race is already measured and flagged (ED-MB-0001). The 1.5 is a placeholder with no control and gets no
  home until history supplies one. — `tests/sim/gauge_mb.py:1-28`, `:55-56`;
  `research/historical/mass_battle_gauge_grounding.md`; `bat.py:1-16`
- **F12, density — Missile density = ranks ÷ reference** (concept:488). **Shipped:**
  `MB_VOLLEY_DENSITY_ENABLED/REF/FLOOR/CAP`, default ON. Ammunition is A6. — `config.py:184-187`;
  `orchestration.py:1550-1562`
- **F15 — Pre-, in- and post-battle Keys; a `causes[]` Key log** (concept:386, :415, :574, :630). **The Key
  substrate is retired** (ED-IN-0232): `keys.py`, the echo transport and the emit/consume interface are gone and
  nothing is built on them. `provenance.py` is a constant-grounding registry, not an event log (and slated for
  deletion, ED-MB-0057). Build A9 instead. — `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:3779-3808`;
  `engine/season/state/ids.py:40-45`; `provenance.py:1-30`
- **F16, cadence — The battle pauses; one duel per pair** (concept:409-415). **Answered by canon:** §3.7 PP-111 —
  one personal exchange per battle turn, at most five, Command suspended; A.5's unilateral pause and PP-506's
  bilateral no-freeze; ED-898, no death. The headless path is sequenced above. — `scale_transitions_v30.md:76-77`;
  `mass_battle_v30.md:336-360`
- **F18, the rule — Squads and armies break at 50%** (concept:506-519). **Existing knobs, not a new rule:** the squad
  half is `CELL_BREAK_ROUT_FRAC = 0.5`; the army half is `ROUT_CASCADE_FRAC`, whose value A8 chooses. Mutual
  disengagement and nightfall are PP-297's Stalemate Break and the 18-tick end. — `config.py:113`, `:116`;
  `orchestration.py:1787`; `mass_battle_v30.md:647`
- **F20 — Commit to `designs/proposals/` after a bootstrap run** (concept:741, :748). `designs/` is dissolved and no
  bootstrap runner exists; new design work is a flat `proposals/<name>.md` — this document. — CLAUDE.md §3
- **F21, the scaffold — Role presets; position constrains role** (concept:51-67). **Already data-only** as the FM
  position→role model. Extend it (A5); do not re-derive it. — `config.py:462-499`; `engine.py:197-199`, `:292-300`;
  `proposals/pc_formation_system.md`
- **Dead primitives — Wire `resolve_internal_collisions` or revive `_reach_throttle` for the concept.** Neither.
  `resolve_internal_collisions`'s case was ED-MB-0056's co-location defect, which is closed by ED-MB-0059's same-side
  field exclusion — explicitly "NOT the grid-era resolve_internal_collisions discipline roll" — and the concept's
  cells never move alone anyway: delete it with ED-MB-0057's dispositions. `_reach_throttle` retired with the
  reach-standoff model; the OBB front-reach contact already gives the concept its reach predicate. —
  `hierarchy/units.py:130-142`, `:2062-2139`, `:2229-2232`, `:2254-2279`; `core/contact.py:297-343`;
  `registers/editorial_ledger_mb_archive.jsonl:56`

---

## Part C — Ruled by Jordan, 2026-09-25

Six items; Jordan ruled all six directly, in session, after this document was first drafted. **`ED-MB-0067`'s
second row is the ledger record.** Three extend items already queued rather than opening new ones (C1 →
ED-MB-0045; C2 → ED-MB-0041/0039; C3 touches ED-MB-0041's yield-split item). Where the ruling settles the
*direction* but not the exact mechanical form, that is marked explicitly — it is follow-up design work, not a
further ruling needed.

1. **C1 — Movement and facing: per cell.** (F4; one arm of ED-MB-0045's emergence verdict.) **RULED: per-cell.**
   The 2026-07-25 directive stands — route and facing are per-cell, not squad-rigid. The concept's formation
   grammar is rebuilt on cells steering toward the sub-unit's goal, as the node model already does. This closes
   the movement/facing arm of ED-MB-0045; the verdict's other arms are untouched.

2. **C2 — Envelopment payoff: the multiplier stands, and feeds morale collapse, checked against Discipline.**
   (F7's payoff; ED-MB-0041's Tier-3 item.) **RULED.** Keep ED-MB-0018's rear/flank damage multiplier — a rear or
   flank attack still does more damage. The multiplied damage is a *contributing cause* of morale collapse, not a
   parallel, independent effect: the envelopment morale shock should scale with the casualties the multiplier
   actually produced. Whether the affected cell's morale then actually breaks under that pressure is checked
   against Discipline — see C3.
   `[ASSUMPTION: read as a causal chain (damage → contributes to morale collapse → gated by a Discipline check)
   rather than three independent mechanisms — basis: Jordan's "multiply damage, which in turn helps collapse
   morale and checks against discipline." The coupling formula — how much realized damage should scale the shock
   — is follow-up mechanical design, not resolved by this ruling.]`
   ED-MB-0039's separate (A)/(B) geometry fork is untouched. The concept's plan-based envelopment (§5) is a
   compatible framing for *how* an envelopment is executed, not a competing answer to *what it does on contact* —
   this ruling settles the latter only.

3. **C3 — Control state: retain Discipline; fold Pressure in carefully.** (F5's replacement half + F8's entry
   gate.) **RULED.** Discipline remains the persisting stat (PP-712) and keeps its existing gates — the inter-unit
   cascade check, the reform gate, the fighting-withdrawal entry gate (`D_YIELD`). The concept's Pressure condition
   is not adopted as a second, parallel gate; it is folded into how a Discipline check resolves.
   `[ASSUMPTION: "fold in carefully" is read as Pressure modifying a Discipline check in the moment (an Ob shift or
   an effective-Discipline shift), never as a second independent pass/fail test alongside it — basis: avoiding the
   two-ladders defect the audit flagged (F5/F14), and the explicit instruction to do this carefully rather than by
   simple addition. Which of the two mechanical forms applies is follow-up design work.]`
   The concept's officer Steadiness contribution (`⌊Cmd/2⌋`) has no stat to attach to now that "Steadiness" is not
   adopted as a name; if a squad leader's Cmd should modify a Discipline check the way it was meant to modify
   Steadiness, that is part of the same follow-up.
   ⚠ Correction carried from the audit stage: F8's entry gate is *this* question applied to `D_YIELD`, not
   ED-MB-0041's "yield split" (which is the separate `YIELD_POOL_MULT` offence/survivability split) — folded in
   here; the yield split stays queued, untouched.

4. **C4 — Feigned retreat: fog, with a roll to identify it.** (F13.) **RULED.** Observers still see only "enemy
   moving away" — there is no automatic "enemy routing" flag; the concept's fog model stands. A roll exists for
   the observing side to attempt to identify what it is actually seeing.
   `[ASSUMPTION: the roll is PP-256's existing Command Ob 2 recognition check, re-purposed to resolve under fog
   rather than retired outright — basis: it is the only "identify a feint" roll in canon, and reusing it avoids a
   second recognition mechanic for the same purpose (CLAUDE.md §4's idempotent-vocabulary rule). Whether the
   feigning side's Discipline Ob 1 "hold" check survives alongside it is not settled by this ruling and is
   follow-up design work.]`
   PP-256's automatic-reveal framing does not survive as previously worded; its recognition roll does, repurposed.

5. **C5 — Span of control: one ladder.** (F14's ladder half.) **RULED: default.** Every echelon commands up to its
   holder's Cmd — the existing "max simultaneous commanded = Command" rule stands at every scale, including A3's
   new officer post. The concept's separate `3 + Cmd` span-and-budget ladder is not adopted.

6. **C6 — Directives a–d: confirmed real and ruled.** **RULED.** Jordan confirmed directly that a–d are genuine
   prior rulings, not unverified inheritance. This repository's ledgers held no record of them because they were
   made outside this repository; `ED-MB-0067`'s second row closes that gap.

   | directive | disposition |
   |---|---|
   | **a** — FM/Total War inform formation | Confirmed; already the shipped position→role model. Nothing changes. |
   | **b** — the Mass pool is retired | Confirmed; already shipped (ED-MB-0006, F1). Nothing changes; no row. |
   | **c** — routes, feints, delays, conditional orders | Confirmed; routes are A1, feints are C4, conditional orders already exist. Nothing beyond Part A and C4. |
   | **d.1** — faction state sets the morale baseline | **Confirmed — overwrites PP-711.** `[ASSUMPTION: "sets the baseline" is full replacement of PP-711's general's-Command-+-quality term with faction Stability, per the concept's own unqualified wording (concept:11) and this confirmation — basis: no blending language appears in either. The Stability→s₀ mapping itself is still [PLACEHOLDER] in the concept (concept:580) — unresolved implementation detail, not a further ruling needed.]` **Correction (ED-MB-0067's 4th row):** PP-711's Command+quality formula was never implemented — `massbattle.py:_faction_to_unit` hardcodes `morale=5, morale_start=5` with its own `[GAP]` comment admitting no canonical spec exists there. There is no formula to change; d.1 is a new derivation. **Still to do, not done in this pass:** replace that hardcoded default with a value derived from `Faction.Sta` at `massbattle.py:_faction_to_unit`, and file PP-711's supersession. `mass_battle_v30.md` is reference (CLAUDE.md §0.05): editing its prose would not change what the engine computes, so it is not the fix and is not gating anything here — it may be updated afterward as documentation, once the code changes. |
   | **d.2** — variance allowed "under GD-2" | Confirmed as directive, but GD-2 is unrelated (F6) — nothing to propagate; drop it. |
   | **d.3** — the player character is a duelling commander | Confirmed; already consistent with canon (PP-111, ED-898). Nothing changes. |
   | **d.4** — "Channellers" are not a thing | Confirmed. Propagation is a Thread-lane matter, out of this lane's scope — flag it there. |

**Follow-up work this ruling opens, not yet done:** the C2/C3 coupling formula (how realized envelopment damage
scales the morale shock; how Pressure modifies a Discipline check); the C4 mechanics (which roll, whose Ob, under
fog); d.1's landing as a new derivation at `massbattle.py:_faction_to_unit` (replacing its hardcoded
`morale=5, morale_start=5` with a value derived from `Faction.Sta` — PP-711 was never actually implemented, so
this is not editing an existing formula) and its own PP-711-supersession ledger entry. `mass_battle_v30.md` is
reference and is not where any of this is fixed. None of this blocks Part A, which was already clear to build.

**Not reopened by this ruling:** a discrete morale clock (ED-1024 stands), casualties off the degree ladder
(S39.4 stands), instantaneous brace (ED-1095 stands), dropping fatigue (the flags-ON ruling stands) — Part B's
dispositions on these are unchanged.

**Already queued, touched by the concept, unchanged by this ruling:** ED-MB-0039's (A)/(B) geometry fork;
ED-MB-0041's depth cap, graded cavalry refusal and Command σ-ceiling; ED-MB-0045's CEV naming and dual 2:1
targets; the mass_battle contract's `state: []` (`references/module_contracts.yaml:636`).

---

## The concept's own §13, answered

| concept §13 (:723-734) | disposition |
|---|---|
| 1. Ledger entries and propagation for directives b and d | b: none (F1). d: C6. |
| 2. Q profile (J-10); muster → cells (J-9); where generic officers' Cmd comes from | Q profile: per-cell Q, sequenced in Part A, type profile mapped there. Muster → cells has partial canon the concept did not read: `military_layer_v30.md:98-121` (Muster output Size=2, Power=floor(Mil/2)+1; merging). `derived_stats_v30.md:307`'s "Levies Available = Military × 2" caps unit *count*; it is not a troop formula. Generic officer Cmd: A3's quality-tier default. |
| 3. D5 — morale as one concept with two expressions | Its shape is ruled: continuous (ED-1024), stochastic break (standing order). Whether it also scales output was not examined; it stays the concept's open item. |
| 4. Where terrain comes from; objective zone; nightfall cap | Terrain: A7 (ED-780). Nightfall: the 18-tick end + PP-297 (F18). Objective zone: no canon; not examined. |
| 5. Mapping onto the 7 canon phases; aggregated Key types (J-2); attached-character Steadiness (J-12 / J-33) | Phases: not examined. Keys: retired (F15). Steadiness: C3. |
| 6. Parley or deception planting false signals or ghosts | Not examined; cannot arise before A2's perception layer exists. |

The concept's `J-n` ids are its uploaded map's decision ids and have no counterpart in `registers/`.
