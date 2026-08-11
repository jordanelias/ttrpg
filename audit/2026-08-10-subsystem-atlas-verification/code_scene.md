# Independent code trace — social contest kernel + mass-battle (two trees)

Method: whole-file Read only, no grep/rg/find-pattern. Did not open any `*_flow_skeleton_v1.md`.

## Scope covered
- systems/social_contest/sim/contest/: wrapper.py, resolver.py, modes.py, primitives.py (full),
  plus __init__.py, contract.py, policy.py, faction.py, appraise.py, narrative.py, rhetoric.py,
  dictionaries.py, armature.py, agon_harness.py (all full); _kernel_tests.py skimmed (first 120
  of 1650 lines — test harness/suite, confirms symbol wiring only).
- systems/social_contest/sim/parliamentary_vote.py, parliamentary_stay.py, contest_legacy_stub.py — full.
- systems/mass_battle/sim/: __init__.py, altonian_reinforcements.py, tactic_cards.py, units.py,
  massbattle.py — all full (1905/1905 lines of massbattle.py read).
- tests/sim/mass_battle/: config.py (full, 501 lines), engine.py (full, 532 lines),
  orchestration.py (read ~1000 of 2864 lines: header/history, phase_boundary hooks, and the full
  run_battle per-tick body lines ~1780-2183; large middle section of helper functions not read
  line-by-line). Package listing (not read): bat.py, geometry.py, lanchester_signature.py,
  percell.py, perimeter.py, provenance.py, resolution.py, test_persubunit_stress.py, validators.py,
  core/{__init__,contact,state,attrition,exchange}.py, hierarchy/{__init__,units}.py,
  troop_types/{__init__,registry}.py, equipment/{__init__,_base,armour,weapons}.py,
  workbench/{server,trace}.py. Note: this package is imported as top-level `mass_battle.*`
  (`from mass_battle.config import *` etc.) — not as `tests.sim.mass_battle.*` — so something
  outside this directory (conftest/sys.path) roots it; not chased further (out of scope).

---

## 1. Social contest resolution loop + Agôn vs. parliamentary-vote code-path question

**resolver.Bout.resolve()** loop order (resolver.py ~L421-447):
```
for i in range(venue.budget):           # one "exchange" = both sides move once
    for side in (A, B):
        move = policy[side](view)
        apply(side, move)               # mutates state.adv, standing/face, reserve, fault
        if faults.check(...): return (winner, "clinch:...")   # immediate defeat-condition
    w = win.resolve(state, closing=False)
    if w: return (w, "win")             # early win (ThresholdRace/ProofBar/GraceThreshold can fire mid-budget)
w = win.resolve(state, closing=True)    # forced close after budget exhausted
return (w, "draw" if w=="draw" else "win")
```
Terminates on: (a) a fault-clinch after either side's move (barred-device / self-contradiction /
evasion-strikes / yield-strikes, venue-configured via DefeatCatalogue), (b) an early win-condition
hit after a full exchange (ThresholdRace/ProofBar/GraceThreshold can resolve before budget is
spent; TallyAtClose/PersuasionTrack/VoteAtClose only resolve at `closing=True`), or (c) budget
exhaustion forcing `closing=True`.

**Agôn kernel vs. parliamentary vote — two entirely separate resolvers, not two paths through one
resolver.** Established by reading imports/call sites, not searching:
- `parliamentary_vote.py`'s `run_parliamentary_vote()` never imports or calls `resolver.Bout`,
  `Contestant`, `Venue`, `Adjudicator`, or `roll_net`. It calls `engine.autoload.dice_engine.roll_pool`
  directly on a single "Mandate pool" per side (sum of `Faction.L`), with its own resistance/
  lobbying-offset/committee logic (§10 BG-vote). No stasis, no styles, no faults, no per-exchange loop.
- The only thing `parliamentary_vote.py` imports from the contest package is four numeric constants —
  `PERSUASION_WIN_THRESHOLD` (7), `PERSUASION_LOSS_THRESHOLD` (3), `PERSUASION_TOTAL_VICTORY` (9),
  `PERSUASION_TOTAL_DEFEAT` (1), `PERSUASION_TRACK_START_DEFAULT` (5) — imported via
  `from systems.social_contest.sim.contest import (...)`. Reading `contest/__init__.py` shows these
  four are **re-exported from `contest_legacy_stub.py`** (the DEPRECATED single-compare stub,
  `contest_legacy_stub.py`'s own docstring: "Do NOT import this module directly in new code"), not
  from `resolver.py`.
- `resolver.py`'s `PersuasionTrack.resolve()` (the Agôn kernel's live win-condition) hardcodes its own
  band literals directly (`t>=9`, `t>=7`, `t>3`, `t>1`) — it does **not** import or reference
  `PERSUASION_WIN_THRESHOLD` etc. So the two trees currently hold the *same* four numbers as two
  independently-maintained encodings (one a module constant re-exported through a deprecated stub,
  one a set of inline literals in the live kernel) — a genuine SHARED-CONSTANT-VALUE-not-SHARED-CODE
  situation, and a latent drift hazard (nothing enforces the two stay equal).
- `faction.py`'s `coalition_vote()` (a *third*, groundup demonstration of "§10 coalitions pooling onto
  the two-pole engine") **does** call into the real kernel (`resolver.ContestState`, `resolver.roll_net`,
  `resolver.PersuasionTrack`) — so the kernel package contains two structurally different §10
  implementations: the promoted, faction-scale `parliamentary_vote.py` (dice_engine.roll_pool, no
  Bout) and the groundup `faction.coalition_vote()` demo (resolver.roll_net + PersuasionTrack). These
  are not cross-called.
- `contest_legacy_stub.py`'s own `run_contest`/`resolve_exchange` (a third, independent single-compare
  resolver, kept only for two other live importers — `scene_dispatch.py` and, for constants only,
  `parliamentary_vote.py`) is a fourth resolution path, sharing no code with `resolver.Bout` either.

So: **Agôn kernel (resolver.Bout), parliamentary vote (dice_engine.roll_pool), the legacy stub
(contest_legacy_stub.run_contest), and faction.py's coalition_vote (resolver.roll_net direct) are
four distinct resolution code paths in this package**, sharing only the four PERSUASION_* band
numbers (and those via two independent encodings, not one).

---

## 2. Mass-battle per-tick phase order — the two trees

### Tree A — `systems/mass_battle/sim/massbattle.py::run_battle()` (campaign-LIVE; retired per
Jordan ruling J2 2026-08-03 but still the code faction_action.py calls)
```
for t in 1..max_turns:
  0. break if either unit already routed
  1. volley_phase()                      — Phase 2 ranged fire, damage banked not applied
  2. find_contacts() (pre-move) -> set halted_cells
  3. assign_targets()
  4. cache target centroids (simultaneous-resolution snapshot)
  5. advance_cells() both sides (using cached centroids)
  6. halt_before_enemy() both sides       — documented no-op ("pass")
  7. resolve_cross_side_contention()      — speed-priority cell contention
  8. find_contacts() (post-move)
  9. stamina drain proportional to contact cells (unit-level, not per-subunit)
 10. resolve_engagements_cascading() (or resolve_engagements() if CASCADING_ENABLED off)
 11. apply Volley+Engagement damage simultaneously to both units' hp; recalc_size() both
 12. check_drift() both (shape reversion below MIN_DISCIPLINE)
 13. morale erosion EVERY TICK: erosion = total_dmg/(discipline*command); Command<=0 -> morale=0 (instant)
 14. rout check (morale<=0 -> routed=True) after both erosions applied
 15. if t % TICKS_PER_PHASE==0: phase_boundary(): stamina_check -> discipline_check_phase ->
     morale_check_phase -> rout_resolution -> rally_check(no-op) -> reform_check(no-op) ->
     threadwork_check(no-op)
```

### Tree B — `tests/sim/mass_battle/orchestration.py::run_battle()` (CANON per J2)
```
for t in 1..max_turns:
  0. break if either unit already routed
  1. volley_phase()                      — Phase 2 ranged fire, damage banked not applied
  2. find_contacts() (pre-move) -> set halted_cells (field-movement-aware coordinate resolution)
  3. compute a_cells_set/b_cells_set
  4. check_orders(unit_a,...) / check_orders(unit_b,...)   *** NEW: Order/trigger system, not in Tree A
  5. assign_targets()
  6. cache target centroids (simultaneous-resolution snapshot)
  7. escort/screening positioning pass (latch engage-on-contact; escort-offset centroid override) *** NEW
  8. advance_cells() both sides (per-subunit eff_discipline; FIELD_MOVEMENT float-position variant)
  9. resolve_toi_and_commit() if FIELD_MOVEMENT — cross-side continuous time-of-impact commit *** NEW
 10. halt_before_enemy() both sides       — same call as Tree A (still present)
 11. resolve_cross_side_contention()
 12. find_contacts() (post-move)
 13. per-SUBUNIT stamina drain proportional to that subunit's own contact cells (finer-grained than A)
 14. resolve_engagements_cascading() (or resolve_engagements())
 15. apply Volley+Engagement damage; distribute_casualties() (+ cellwise variant under PC_CELL_DAMAGE,
     + PC_CLOSE_RANKS rank-refill, + update_stamina() under PER_CELL); recalc_size() both
 16. check_drift() both
 17. Command<=0 -> set_morale(0.0) (instant); **no other per-tick morale erosion** — a 2026-06-03
     Jordan directive explicitly REMOVED per-tick absolute-damage morale erosion (comment: "step 3
     ... per-tick ABSOLUTE-damage morale erosion REMOVED. Morale degrades by canonical Size-fraction
     triggers at the phase boundary")
 18. per-SUBUNIT rout check: atom.routed=True if eff_morale<=0 OR troop_total<SUBUNIT_ROUT_FLOOR;
     then u.derive_rout() aggregates to the unit
 19. if t % TICKS_PER_PHASE==0: phase_boundary(): stamina_check -> discipline_check_phase ->
     morale_check_phase -> rout_resolution -> rally_check(no-op) -> reform_check(REAL,
     flag-gated REFORM_CHECK_ENABLED default ON) -> threadwork_check(no-op)
```

### Verdict: do they match?
**Same coarse skeleton, same phase-boundary hook ORDER, but NOT identical.** Both trees run the
same six-stage envelope in the same sequence — volley → pre-halt → target/advance → cross-side
contention → contact/engage → damage-apply/recalc → morale/rout check → (every 6th tick)
phase-boundary hooks in the exact order `stamina → discipline → morale → rout → rally → reform →
threadwork`. That macro-order is identical across both files (verified by direct comparison, not
by the shared v9-v22 comment history, which both files also still carry verbatim).

They diverge in three concrete ways:
1. **Tree B inserts two whole new steps Tree A does not have at all**: an order/trigger check
   (`check_orders`) before targeting, and an escort-positioning + continuous-time-of-impact
   commit layer (`resolve_toi_and_commit`, gated on `FIELD_MOVEMENT`) between advance and
   contention resolution.
2. **Morale erosion changed cadence, not just granularity**: Tree A erodes morale continuously,
   every tick, from total damage taken. Tree B *removed* that per-tick channel (explicit ED note)
   and now only erodes morale at phase boundaries via `morale_check_phase`'s Size-fraction
   triggers — a real behavioral divergence in *when* morale moves, not merely unit-vs-subunit
   granularity.
3. **Rout is unit-scalar in Tree A, per-subunit-aggregated in Tree B** (`SUBUNIT_ROUT_FLOOR` +
   `derive_rout()`), consistent with config.py's documented ED-MB-0041 "army breaks by contagion,
   not to the last section" rework — Tree B implements a fundamentally different rout-propagation
   model layered on top of the same tick skeleton.

So "do the phase orders match" is a well-posed but two-part answer: **yes at the macro-sequence
level** (both papers over the same six stages plus the same 7-hook phase-boundary order,
`rally_check`/`threadwork_check` still no-ops in *both*), **no at the mechanism level** (Tree B
added an Order layer, a continuous-movement/TOI layer, and removed Tree A's per-tick morale
erosion in favour of phase-boundary-only morale changes).

---

## 3. Declared-but-doesn't-happen inventory (file:line, from files actually read)

1. `systems/social_contest/sim/contest/dictionaries.py:229-232` (`DOUBT_MARKER["scope_note"]`) —
   the entire Obscuring-win "Doubt Marker" terminal-value mechanism (−2 to a marked side's next
   winning margin/tally) is explicitly a **DESIGN-TABLE COMMITMENT ONLY**: "the resolver does NOT
   yet consume orientation ... so NO resolution-path number changes this pass." `resolver.py`'s
   `_apply`/`_advance` never reads a move's Orientation (Revealing/Obscuring) at all.
2. `systems/social_contest/sim/contest/dictionaries.py` `derive_interaction()` / `INTERACTIONS_TABLE`
   (CLASH/REINFORCE/CROSS/TIE) — confirmed dead-in-resolution by the kernel's own harness comment,
   `agon_harness.py:458-462`: "derive_interaction() is a descriptive typed-surface lookup ..., not
   consumed by resolver.py's live resolution (each side's argument resolves via its own additive
   _advance() call, not a pairwise compare)." Only ever called for print-flavor in `agon_harness.py`.
3. `systems/social_contest/sim/contest/primitives.py:36` — `Standing.strip(deg)` is defined (scales
   a degree by `STRIP=0.8`) but every strip call site actually read (`resolver.py`'s CR5 path,
   `rhetoric.py`) uses `strip_points(points)` instead (a fixed-point strip, added specifically
   because `strip(deg)` mis-applies the cited magnitude — `rhetoric.py`'s own docstring, judge
   finding 3). No call to `.strip(` on a `Standing`/`Face` instance was found in any file read.
4. `systems/social_contest/sim/contest/wrapper.py` `Contest.resistance` — computed by
   `_derive_resistance()` (real audience-Stability formula) but explicitly METADATA-ONLY (F10):
   "the resolver reads no resistance and Venue.base_ob is not set from it" — downgraded to
   `"status":"PARTIAL"` in the `MECHANICS` self-test registry (wrapper.py ~L312-318) precisely so
   the WIRED self-test doesn't over-claim it.
5. `systems/social_contest/sim/contest/wrapper.py` `GAMES` table — `consensus`/`negotiation`/
   `inquiry` are registered STUB rows (`_stub()`, returns `stubwire.StubResult`); only `agon` is WIRED.
6. `systems/social_contest/sim/contest/modes.py` `DyadicMode`/`NegotiationMode`/`CeremonialMode`
   `.play()` — all three unconditionally return `stubwire.stub_resolve(...)`.
7. `systems/social_contest/sim/contest/dictionaries.py` `panel_win_condition(aggregation=...)` —
   the `'unanimity_required'` branch (documented as "sketched but not selected") returns
   `stubwire.stub_resolve(...)` rather than an implementation; only `weighted_by_standing` and
   `simple_majority` resolve.
8. `systems/mass_battle/sim/tactic_cards.py:33` — `FACTION_TACTIC_CARD_POOL_MODIFIERS: dict = {}`,
   permanently empty, explicitly "BLOCKED — Phase 7 stub"; `massbattle.py` never references it
   (confirmed by tactic_cards.py's own docstring: "v22 does not have
   FACTION_TACTIC_CARD_POOL_MODIFIERS").
9. `systems/mass_battle/sim/altonian_reinforcements.py:20-21` — `invoke_altonian_reinforcements`
   unconditionally `raise NotImplementedError(...)`; its signature also annotates a parameter as
   `world: GameState` with `GameState` never imported anywhere in the file (silently tolerated only
   because `from __future__ import annotations` defers evaluation of the annotation string).
10. `systems/mass_battle/sim/massbattle.py:293-303` — `rally_check`/`reform_check`/`threadwork_check`
    are empty `pass`-only hooks, called every phase boundary via `phase_boundary()`. In the CANON
    tree (`tests/sim/mass_battle/orchestration.py`) `reform_check` was later actually implemented
    (flag-gated `REFORM_CHECK_ENABLED`, default ON) but `rally_check`/`threadwork_check` remain
    empty `pass` stubs there too (orchestration.py:287-289, :332-334) — the stub gap was only
    partially closed between the two trees, not resolved.
11. `systems/mass_battle/sim/units.py:218-225` (`Subunit.halt_before_enemy`) — documented no-op
    ("pass"), called unconditionally every tick in both `massbattle.py:1196-1197` and
    `orchestration.py:1937-1938`: "v11: over-run correction disabled ... removed after causing
    ordering asymmetries."
12. `systems/mass_battle/sim/units.py` `Subunit.resolve_internal_collisions()` — a fully-implemented
    discipline-gated formation-hold method with real d10-roll logic, but never called from
    `run_battle()` in *either* tree; both files carry the identical comment: "implemented but not
    invoked here — it over-tuned battery (12/13 -> 9/13)."
13. `systems/mass_battle/sim/massbattle.py::resolve_engagements()` (~L951-952, and the
    `freed_attacker_damage` sibling at ~L1517) — `a_deg`/`b_deg` are computed every engagement pair
    via `compute_degree(...)` and the code's own comment calls them "narrative degree label only,"
    but they are not attached to the function's *returned* dict (`{"dmg_a","dmg_b","engagements"}`)
    or used anywhere else in the function — a genuinely dead per-pair computation, not merely unused
    externally.
14. `tests/sim/mass_battle/config.py` — dozens of `PC_*` toggles are declared with rich mechanism
    documentation but are explicitly flagged inert/off in the default configuration the byte-exact
    goldens pin against (e.g. `PC_CLOSE_RANKS` "Default OFF (byte-exact)"; several others are
    default-ON but *conditionally* inert, e.g. `PC_FEIGNED_RETREAT`/`PC_RESERVE_COMMIT`, which are
    "GATED OFF so the multi-unit RNG stream is unchanged unless explicitly enabled" per their own
    comments even though the env-var default currently reads `'1'`) — a large declared-vs-live
    surface, self-documented rather than hidden.
15. `tests/sim/mass_battle/config.py:77-107` — `PC_CELL_MORALE`'s own comment block documents that
    the flag was **flipped ON, measured, and retracted to OFF the same day** because
    `between_turn_recovery`/`reset_morale_between_battles` wrote the old scalar morale field while
    `eff_morale` had already switched to reading from cells — a confounded A/B the file's own author
    caught and disclosed in-line (see "surprised me" below).

---

## 4. Import cycles noticed while reading

- **`systems/social_contest/sim/contest/modes.py` ↔ `dictionaries.py`.** `dictionaries.py` imports
  `from . import modes as _modes` at module scope (top of file). `modes.py` does NOT import
  `dictionaries` at module scope; instead `modes.proceeding_venue()` does
  `from .dictionaries import panel_win_condition` **inside the function body**, and the file's own
  comment names this explicitly: "Lazy import breaks the dictionaries<->modes cycle (dictionaries
  imports modes)." Confirmed by reading both files' import blocks directly, not by search.
- **`systems/mass_battle/sim/units.py` ↔ `massbattle.py`.** `units.py` does
  `from systems.mass_battle.sim import massbattle as _mb` at module scope and reaches constants/
  helpers via `_mb.NAME` at *call* time, not import time. `massbattle.py` imports `Subunit, Unit`
  from `units` only at its own file TAIL (after every module-level constant/function `units.py`
  needs is already bound), explicitly documented: "Python's import machinery resolves the circular
  path because all those names are already bound in this module by the time the from-import below
  executes." A genuine ring (A imports B, B imports A), deliberately broken by ordering + late
  binding rather than laziness.
- `contest/wrapper.py`'s own comment ("Stage 2 / Gate B typed dictionaries (imported lazily to avoid
  a cycle...)") is not actually lazy in the deferred-until-call sense — the `from . import
  dictionaries as _dict` sits at module scope, just textually after `resolver`/`modes` are already
  bound in `sys.modules`, so it works, but "lazily" is loose phrasing for "positioned later in the
  same eager import chain," not a real runtime-deferred import like `modes.py`'s.
- No cycle observed within the mass-battle trees beyond the `units.py`↔`massbattle.py` pair (the
  `hierarchy/units.py`↔`core/*` structure in the canon tree was not read closely enough to confirm
  or rule out an analogous pattern there).

---

## 5. What surprised me

- **`config.py`'s `PC_CELL_MORALE` retraction note is, as far as I can tell, the actual incident
  CLAUDE.md §0.1 narrates** (a flag flipped ON, a confounded A/B where a getter switched to reading
  cells while writers kept writing the old scalar, retracted the same day) — I found it independently
  by reading the file top-to-bottom, not by cross-referencing CLAUDE.md. The repo's own governance
  history is visible, in the author's own words, directly in a production config file's comments.
- **Four independent §10/social-contest resolvers coexist**, sharing only four numeric band
  constants (and those via two separate encodings — a shared constant module vs. hardcoded literals
  in the live kernel) rather than any code: `resolver.Bout` (Agôn), `parliamentary_vote.py`
  (dice_engine.roll_pool direct), `contest_legacy_stub.run_contest` (deprecated single-compare),
  and `faction.coalition_vote` (resolver.roll_net direct, a demo). None call each other.
- **The DOUBT_MARKER block in `dictionaries.py` is ~100 lines of fully-reasoned, cited, two-branch
  design-authority documentation for a mechanic that has zero resolution-path effect** — an unusually
  large amount of prose-as-code for something the resolver provably never reads (self-admitted in
  the same file).
- **The same tick-loop, the same v9→v22 comment history, and the same named defects (H5 tension,
  the resolve_internal_collisions "over-tuned battery 12/13→9/13" note) are duplicated verbatim
  across `massbattle.py` and `orchestration.py`** — not paraphrased, but byte-for-byte-similar prose,
  confirming they really are two divergent branches of one lineage rather than independently
  designed engines that happen to agree.
- **`config.py` imports the stdlib `os` module three separate times under three different aliases**
  (`import os`, `import os as _os`, `import os as _sigma_os`, plus a fourth `import os as
  _reform_os` in `orchestration.py`) — harmless, but a visible fossil of the file having been
  assembled by merging several previously-separate modules (P-A extraction, sigma-head prototype,
  G-8 reform) without ever consolidating their imports.
- **`altonian_reinforcements.py` type-annotates a parameter with an undefined name** (`GameState`)
  and it is invisible at import time purely because of `from __future__ import annotations` —  a
  latent `NameError` waiting for anything that ever introspects the signature (e.g. `typing.get_type_hints`).
