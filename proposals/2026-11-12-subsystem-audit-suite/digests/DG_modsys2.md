# Digest modsys2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: code under `modules/mass_battle/`, `systems/` and `engine/`-adjacent oracles (assignment `N_modsys2`). Entries in assignment order. Line references are to the working tree at read time (2026-11-12).

### modules/mass_battle/hierarchy/units.py
- **What it is:** Layer-2 code, 3083 lines; the `Order`, `Subunit`, `Officer`, `Unit` dataclasses plus all per-cell movement, facing, collision (time-of-impact), morale-cell and rout methods; "Stage-1 behaviour-frozen extract from orchestration.py".
- **Status:** none (code). Live: the default field path (`FIELD_MOVEMENT`, `MB_NODE_COHESION`) runs here; the integer-grid path (`advance_cells` below the early return) is a frozen regression oracle kept only for `bat.py` digests.
- **Bears on:** MB, PC (formation/cell structure shared), CHAR (Officer command), DICE (pool/degree callers).
- **Content that matters:**
  - Troop-type, formation and cell structure: a `Subunit` is `shape` + `troop_type` + `tier` (legacy) or `troops` + `concentration` or `width x depth` (continuous mode) + `distribution` ('uniform'/'front'/'rear') (`:392-462`, `:571-600`). Per-cell state is dicts keyed by pattern id `(orig_r, orig_c)`: `cell_troops`, `cell_morale`, `cell_breakpoint`, `cell_facing_vec`, `cell_offsets` (`:405-425`). A `Unit` aggregates subunits; `ncells`, `col_grid = build_column_grid` (`:2872-2892`). There is no per-cell weapon/loadout field at all: `Subunit.troop_type` is the only equipment key, resolved by `troop_types.registry` (`stats_for`, `reach_for`) (`:637`, `:130-139`). Confirms F-MB-19 (loadout not read, no second weapon) and F-MB-22.
  - Troop-type behaviour is keyed on a string table `ROLE_INSTRUCTION_PRIMITIVES` (`:71-101`): 8 keywords wired (`brace`, `envelop`, `sweep`, `kite`, `reserve`, `hold`, `push`, `charge`, `lure`), 7 explicitly `None` (`pin`, `loose`, `harass`, `screen`, `pursue`, `volley`, `shoot_move`) with a reason string. Confirms F-MB-10 (seven unwired role keywords) and F-MB-23 (behaviour keyed on type names: `fast = troop_type in ('cavalry','light_cavalry')` at `:1491`, `charge_pen` is `3 if troop_type == 'cavalry'` at `:943`).
  - Hierarchy is 3 levels in code: `Unit` -> `Subunit` -> cell; `Officer(name, command, charisma, cognition)` is bookkeeping only ("nothing at resolution time reads it", `:2845-2849`, `:558`); `Subunit.officer` is also unread (`:552-558`). Confirms F-MB-17 (hierarchy three levels, not four).
  - 12 `os.environ` toggles at import (`MB_ENVELOP_PATH`, `MB_SWEEP`, `FIELD_MOVEMENT`, `FIELD_CONTACT`, `CONTACT_REACH`, `MB_FACING_*`, `MB_ROLE_INSTRUCTIONS`, `MB_REACH_FACING_GATE`) (`:23-70`, `:166`): hidden inputs, confirms F-MB-09. Comment at `:53` says facing slew `MB_FACING_SLEW_BASE` is "ungrounded placeholder ... do not enable" and `:47` says "DEFAULT-OFF; F2 is NOT enabled", yet `MB_FACING_MODEL` defaults to `'1'` at `:51` (comment contradicts code; see F-MB-25 family).
  - Order system: `Order(trigger, behavior)` with triggers `immediate | tick:N | enemy_range:D | ally_at:D | own_strength:F | signal:NAME`; behavior restricted to `_ORDER_SAFE_FIELDS` incl. `stance`, `instructions`, `route`, `yielding`, `conceded`, `fire_signal`, `feign_retreat` (`:271-389`). This is the only command surface in the module; the season reaches it through `massbattle._retreat_orders`/`_role_fields`, not these. Route clamp: budget `0.5*speed*ROUTE_BUDGET_TICKS` (`:1203-1287`).
  - Per-cell morale (`MB_CELL_MORALE`): `eff_morale` is the troop-weighted mean of cells, `erode_morale`/`pull_morale`/`set_morale` route across cells; `check_cell_breaks` draws a per-cell breakpoint from `rngsource.get()` (`:683-727`, `:2260-2298`). `rekey_cells` deliberately does NOT re-key `cell_morale`/`cell_breakpoint` on a shape drift (`:1108-1115`): morale state is silently dropped when a Column/Arrowhead drifts to Line (confirms F-MB-18 "per-cell morale comes loose when shapes change").
  - Dead: `halt_before_enemy` is `pass` (`:2363-2370`, F-MB-10); `role_at_contact` "diagnostic label helper never wired" (`:2372`) -- a grep for callers is owed; `Subunit.charge_pen` hard-codes 3 for cavalry (`:943`); `Unit.base_combat_pool` is a second owner of the pool base term (`:2998-3033`, F-MB-10); `Unit.officers`, `Subunit.officer` unread.
  - Hard-coded in-file: discipline tiers `1.0 / 0.7 / 0.4` for discipline >=5 / >=3 / else appear at `:253`, `:1738`, `:2075` (three copies; each tagged `[canonical: mass_battle_v30.md A.4]`); wheel step 0.9 rad at `:1536`; `_FACE_BALANCE_TOL = 0.1` at `:2580` described as "an ASSUMPTION of this module, not canon"; `_SEPARATE_PASSES=400`, `_MOVE_PASSES=24`, `_SEPARATE_ROUNDS=6` marked CALIBRATED-DEBT (`:2418-2420`).
- **Reads / readers:** imported by `orchestration.py:164` (star import), `massbattle.py:66` (`Order, Subunit, Unit, unit_conceded`), `armies.py:15` (`Officer, Subunit, Unit`), `orderofbattle.py:36` (`Order, _INSTRUCTION_STANCE`), `geometry.py:238` (lazy toggle read). `engine/season` never imports it; it reaches it through `seam/wrappers/mass_battle.py` -> `massbattle.resolve_field`. One test touches it directly: `engine/season/tests/test_cp_t04_03_retreat.py:46`.
- **Conflicts / stale:** the `:47-53` comments say facing model is DEFAULT-OFF / "do not enable" while the code defaults every `MB_FACING_*` to ON `[verified by reading :51-55]`. `:1491` carries `# light_cavalry: ED-IN-0306` so the troop-type list is hand-extended. `Unit.__post_init__` comment (`:2801`) says "default ON" for `MB_FEIGNED_RETREAT`, which the file itself had to correct once.
- **Open items:** the unresolved shape-drift policy for cell morale (ruling left open at `:1108-1115`, "plan-v2 B1c"). Verified by grep: `role_at_contact` has NO caller in `modules/` or `engine/` (dead; not in F-MB-10's list). Verified: `MB_CELL_MORALE` defaults ON (`config.py:106`), so the `rekey_cells` gap at `:1108-1115` ("inert today" at the shipped OFF) is now live: the comment is stale and the dropped-morale case is reachable on the default path (strengthens F-MB-18).

### modules/mass_battle/orchestration.py
- **What it is:** Layer-2 code, 2497 lines; the tick-engagement resolver (`resolve_engagements`, `resolve_engagements_cascading`), volley phase, phase-boundary hooks, pursuit / feigned-retreat / freed-attacker rules, and the two legacy multi-turn drivers; ~150 lines of v9-v20 changelog comment at the head. `run_battle` itself lives in `battle_loop.py` and is re-exported (`:1798`).
- **Status:** none (code). Live path: `resolve_engagements_cascading` -> `resolve_engagements` (octagon-damage + sigma head + Lanchester), `volley_phase`, `phase_boundary`. Oracle-only: `run_multi_turn_battle`, `run_multi_unit_battle`, `reset_positions`, `pursuit_damage`, `recall_check`, `freed_attacker_damage` (see below).
- **Bears on:** MB, DICE (roll_pool, compute_degree, `_sigma_net_boost`), CHAR (Command stat).
- **Content that matters:**
  - Pair resolution (`:710-1381`): per contact pair, pool from `subunit_combat_pool` split by `pair_pool_contribution` (POOL_VARIANT `"C-ii"` live; `"baseline"`, `"C-i"` still coded, `:778-830`); advantages enter as a delta-sigma `ns_a/ns_b` (SIGMA_HEAD_ENABLED) built from puncture, charge shock, brace recoil, ranged-in-melee, morale sigma, fatigue sigma, intent (`STANCE_COMMITMENT`), terrain dice `Unit.terrain_off_d/def_d` (`:1108-1260`). A second, LEGACY pool-modifier path (`:1276-1297`) and the legacy `ENCIRCLEMENT_PENALTY` are kept beside it behind flags. Damage = `K_LINEAR * lanchester_strength * max(0, DAMAGE_BY_DEGREE[deg](eff_power) - eff_dr) * octagon_mult` (`:1349-1368`): armour is `Subunit.eff_dr` (a per-unit integer), not a per-troop item. Armour/weapon identity beyond `troop_type`, `eff_power`, `eff_dr` and `reach_for` is not consulted (confirms F-MB-19, F-MB-22).
  - Octagon: three overlapping facing models. `_per_cell_angle_mod` (`:861-993`; wrapper / pocket / roll-up pool penalties, feeds `a_angle_mod` used only for charge-shock zone gating and the legacy path), `_octagon_cell_mods` (`:1012-1092`; the live damage-multiplier arc, with a per-cell reaction clock `_react_since`), and `_compute_atom_sides` (`:561-601`; distinct faces for multi-side shock). Also `_compute_front_fixers` (`:678-707`). Three owners of "what angle am I struck at" in one function: a doubled mechanism worth the MB lane's attention (extends F-MB-12/F-MB-23 family).
  - Cell damage: `MB_CELL_DAMAGE` splits a pair's casualties across the defender's contact cells by `troops * facing mult` (`:604-651`, `:1369-1374`). `_convergence_scale` renormalises N subunits converging on one target (`:467-558`; ED-MB-0041 fix replaced a mean with a sum).
  - Command surface: `Unit.command` enters only through `subunit_combat_pool` (external to this file) and the oracle-only `recall_check` (`roll_pool(pursuer.command)`, Ob 2, `:2093-2098`), `feigned_retreat_recognized` (Command Ob 2, `:2101-2107`) and `feigned_retreat_check` (Discipline Ob 1, `:2110-2116`). No player decision enters mid-battle here; the only authored levers are `Order` objects and stance (`STANCE_COMMITMENT`, `:1250-1253`). Confirms F-MB-15 (no intervention) and F-MB-16.
  - Volley (`:1574-1688`): pool = shooter `eff_power` minus a hard-coded discipline penalty ladder `0/1/2/99` at `:1642`; TN 7 via `resolution.roll_pool` (ED-MB-0066); target DR from `best_target.eff_dr`; ordered targeting by `order_target_idx`/`'weakest'`; ammo via `eff_volleys` (`MB_AMMO_ENABLED`). A THIRD copy of the discipline-tier thresholds (5 / 3 / 1) in addition to the three copies in `units.py`.
  - Phase hooks (`:257-329`): `stamina_check` (real), `rally_check` `pass`, `threadwork_check` `pass`, `reform_check` (real, `REFORM_CHECK_ENABLED` default ON though its comment at `:277` says "default OFF"). Threadwork is a documented no-op slot (F-MB-10; links to F-WR-05 threadwork not a module).
  - Oracle-only block (`:1801-2495`): `run_multi_turn_battle`, `run_multi_unit_battle` (pairings, morale cascade, freed attackers, pursuit by Fast units) are called only from `systems/mass_battle/sim/engine.py:294,296`, `workbench/trace.py`, `bat.py`; `massbattle.py:387` records that `pursuit_damage` and `run_multi_unit_battle` are "not reachable from here". Verified by grep: nothing in `engine/season` or `massbattle.py` calls them. `Unit.speed` ("Slow/Standard/Fast"), the pursuit mechanic, `RECALL_OB`, `REARGUARD_PENALTY` and `MORALE_CASCADE_OB` therefore never run in a season battle. In `run_multi_unit_battle` the "same-engagement morale cascade" branch is two empty `pass` arms (`:2370-2375`).
  - Hard-coded in-file: `BETWEEN_TURN_STAMINA_RECOVERY=30`, `BETWEEN_TURN_MORALE_RECOVERY=0` (so morale never recovers within a battle; the recovery code is inert), `REARGUARD_PENALTY=2`, `RECALL_OB=2`, `MORALE_CASCADE_OB=1`, `FREED_ATTACKER_FLANK_PENALTY=1`, `max_battle_turns=8` (`:1810-1811`, `:2053-2054`, `:2155-2157`, `:1989`); 8 `MB_ROLLUP_*`/`MB_*` env toggles (`:440-464`) plus `REFORM_CHECK_ENABLED` (`:278`) = the 11 environ reads F-MB-09 counts.
- **Reads / readers:** star-imports `config`, `core.exchange/state/attrition/contact`, `troop_types.registry`, `hierarchy.units`, `resolution`, `geometry`, `percell` (`:158-165`, `:365`, `:454`) and re-exports ~60 names in `__all__` (`:2497`). Read by `battle_loop.py`, `massbattle.py`, `systems/mass_battle/sim/*`. `engine/season` reaches it only through `massbattle.resolve_field` via the seam wrapper.
- **Conflicts / stale:** `:277` "default OFF" vs code default `'1'`. Header comments (`:1-152`) describe v9-v20 battery results (12/13 in band, H5 open) that are historical, not current. `:1180-1189` records a prior false comment ("TROOP_TYPE_REACH is deliberately empty") corrected in place: the same stale-comment class F-MB-12/F-MB-25 count. `:157-168` cite `designs/provincial/mass_battle_v30.md` (path dissolved; now `.designs/systems/mass_battle/reference/`). Many `[canonical: mass_battle_v30.md ...]` tags assert design prose as the source of a number, contrary to CLAUDE.md 0.05, while the code is the actual owner. `:925` and `:1058` admit the octagon model is "NOT in mass_battle_v30.md": the central damage mechanism has no design-document owner at all.
- **Open items:** Which of the three angle owners should survive; `POOL_VARIANT` "baseline"/"C-i" and the legacy pool-modifier path appear unreachable on the live configuration (unverified; needs a config read); whether `Unit.speed`/pursuit should ever reach the season (F-MB-11: after a won field the loser stays).

### modules/mass_battle/percell.py
- **What it is:** Layer-2 code, 321 lines; the per-column density/stamina/depth grid (`_ColBlock`), the single casualty-application primitive and its three distributors, fatigue sigma and defender depth. "Behaviour-frozen P-A extract."
- **Status:** none (code). Live: `battle_loop.py:366-390` calls `distribute_casualties_cellwise`, `sync_col_grid`, `update_stamina`; `Unit.__post_init__` builds `col_grid` (`units.py:2892`, under `PER_CELL`).
- **Bears on:** MB.
- **Content that matters:**
  - `_apply_with_spill(targets, dmg)` (`:107-142`) is the SINGLE owner of casualty application with overflow spill (ED-MB-0041: 4400 of 5000 damage had been silently discarded); every path that kills men (melee, volley, pursuit, freed-attacker) rides it and erodes the struck cell's morale through `_erode_cell_morale_from_damage` (`:195-211`, scaled by fraction of the cell destroyed, capped by `MORALE_PHASE_CAP`). It is duck-typed (`getattr(atom,'cell_morale')`) because test doubles pass fake atoms.
  - `_ColBlock` (`:9-36`) holds ONE stamina/density/depth per FILE, shared across whatever subunits occupy the file. So stamina is per-column, not per-cell or per-subunit, while `Subunit.stamina` also exists as a per-subunit ledger (`units.py:476`) and `Unit.stamina` a third: three stamina ledgers (`_ColBlock.stamina` read by `_fatigue_sigma`; `Subunit.stamina` via `stamina_check`; `Unit.stamina`). Doubled state; whichever feeds the pool is chosen by `_stamina_pool_penalty` in `core/exchange.py` (not in this file).
  - `distribute_casualties` takes casualties from the ENGAGED columns of each subunit, falling back to "all living cells" when no pair references the unit (`:145-192`); `distribute_casualties_cellwise` weights by the resolver's per-cell facing shares (`:214-245`); `apply_to_subunit` concentrates ordered volley fire on one subunit (`:248-264`).
  - `_defender_depth` and `_fatigue_sigma` return 0.0 whenever `col_grid` is absent, i.e. whenever `PER_CELL` is off (`:272-299`).
  - Hard-coded: `adjacent_to_front = abs(b.col - ec) <= 1` (`:319`); bounded spill passes `range(8)` (`:123`); constants `MB_STAMINA_DRAIN`, `MB_DEPTH_ROTATE`, `MB_STAMINA_REST`, `MB_STAM_SIGMA` come from `config`.
  - `__all__` lists `_erode_cell_morale_from_damage`, `_apply_with_spill`, `_ColBlock`, etc. (underscore names) because `orchestration.py` star-imports it (`:7`).
- **Reads / readers:** star-imported by `units.py:17` and `orchestration.py:454`; `battle_loop.py:32-34,366-390`. `engine/season` does not import it.
- **Conflicts / stale:** the `_ColBlock` docstring (`:13-25`) records an ammo ledger that was moved off it after review (history, not current). No reference to `perimeter` or loadout.
- **Open items:** none stated; the three stamina ledgers are not reconciled in this file.

### modules/mass_battle/perimeter.py
- **What it is:** Layer-2 code, 173 lines; pure-geometry convex-hull perimeter faces, major (face midpoint) and minor (corner) target points with outward normals, `SHARP_TIP_DEG = 60`, and `approach_alignment`.
- **Status:** none (code; docstring says the behavioural wiring "is a separate, Jordan-gated step"). Live only through one call.
- **Bears on:** MB.
- **Content that matters:**
  - Only `perimeter_faces` is called from outside, once: `Subunit._envelop_goal` for a NON-fast enveloper (`units.py:1494-1503`). `target_points`, `nearest_target`, `approach_alignment`, `TargetPoint`, `SHARP_TIP_DEG` have no caller (verified by grep over `modules engine systems`: only the lazy import at `units.py:1494`). So the "alignment gate / interception" the docstring names (`:13-14`, `:162-167`) is unbuilt: `approach_alignment` is dead and a sharp-tip flag nothing reads (confirms F-MB-10 on `perimeter.py`, and adds that most of the file's API is dead, not just the file's reach).
  - Known limitation recorded in the header: concave footprints (GappedLine's lane) are bridged by the hull (`:17-18`).
  - Pure functions of the cell set; deterministic.
- **Reads / readers:** `units.py:1494` only.
- **Conflicts / stale:** header cites `audit/2026-07-22-mass-battle-stress-test/perimeter_targeting_geometry_v1.md` (an `audit/` path; the corpus is now hidden `.audit/`, and a code comment may not point there per CLAUDE.md 3). The mechanism's scope (cavalry bypasses it: `fast` branch uses `_envelop_wheel_goal`) means perimeter geometry never influences a cavalry envelopment.
- **Open items:** hard-gate vs soft-bonus alignment policy "Jordan-gated" and unanswered; concave-face handling "documented follow-up".

### modules/mass_battle/terrain.py
- **What it is:** Layer-2 code, 290 lines; geography-derived battle terrain: point-in-polygon lookup of a province anchor in the geography file's `terrain:` polygons, river-crossing test, the A.9 row constants. Opens no file; takes the parsed geography.
- **Status:** none (code). Live: `massbattle.py:71-73,417,423` imports `SPEED_TIERS`, `UPHILL*`, `WALLS`, `WALLS_DEFENDER_DR`, `river_crossed`, `terrain_row_for_territory`; the seam wrapper feeds `fort_level` from `world_q.fortification_of`.
- **Bears on:** MB, SE (geography file `systems/settlements/valoria_geography_v30.yaml`, garrison fortification), CORE (seam), WR.
- **Content that matters:**
  - Six rows only (`NARROW_PASS`, `UPHILL`, `FOREST_BROKEN`, `WALLS`, `RIVER_CROSSING`, `OPEN_FLAT`, `:44-50`); priority `WALLS > RIVER_CROSSING > smallest-area polygon match > OPEN_FLAT` (`:174-193`); one row, never combined (stated as an `[ASSUMPTION]` at `:117-127`). Polygon `type` -> row table `_TYPE_TO_ROW` is hard-coded in this file (8 entries, `:66-75`); `coast`/`plains` -> OPEN_FLAT, `fjord_coast`/`marsh` -> FOREST_BROKEN. It is a rule table in code, not a registry.
  - Anchor point-test, not area-weighted: T3 and T10 each "gate" a pass but their `anchor` lies outside the pass polygon, so neither can resolve to NARROW_PASS (`:28-38`). Known gap, disclosed.
  - River crossing: counted from the straight line between two province anchors against `water: rivers:` polylines; bridges are not read (`:234-242`, flagged `[ASSUMPTION; medium; Jordan to correct]`), lakes not read; no route model exists.
  - Numeric facts hard-coded here with `[canonical: mass_battle_v30.md]` tags: `WALLS_DEFENDER_DR = 3`, `UPHILL_ATTACKER_OFF_D = -1`, `UPHILL_DEFENDER_DEF_D = 1`, `RIVER_CROSSING_OFF_D = -1`, `SPEED_TIERS` (`:272-290`). Per CLAUDE.md 0.05 these are code-owned facts whose "canonical" tag is only a pointer. Dice become sigma through `config.SIGMA_PER_D`, a CALIBRATED-DEBT conversion (`:277-279`).
  - Not applied: NARROW_PASS (identified, no effect per `massbattle.py:396`), forest's speed half, the Walls "no flanking; Slow cannot advance" clauses, the river "Discipline check" (argued a no-op, `:286-288`); `SPEED_TIERS` demotion is "inert on the season path" because `Unit.speed` affects only pursuit, which the season never reaches (see orchestration.py entry). So terrain rows contribute dice and DR only.
- **Reads / readers:** `massbattle.py` (single production caller), `tests/valoria/test_mass_battle_terrain.py` per its own docstring. Reads geography keys `provinces`, `terrain`, `water`.
- **Conflicts / stale:** the "Done when" test uses a synthetic province because real T3/T10 cannot reach NARROW_PASS (`:35-38`). A note at `:271` cites `tests/valoria/test_flow_skeletons.py` as anchoring a line position of the lookup (a line-number coupling between prose skeleton and code `[UNVERIFIED]`).
- **Open items:** bridges; area-weighted match; UPHILL-vs-crossing priority "Jordan's to state" (`:120-125`); who crosses (A.9 silent; attacker assumed).

### modules/mass_battle/troop_types/__init__.py
- **What it is:** Layer-2 package marker, 2-line docstring.
- **Status:** none; live (package).
- **Bears on:** MB
- **Content that matters:** Docstring names the package "what a troop type IS: its canonical B.2 stat preset and its gated role menu". The three modules actually in the directory are `presets.py`, `recruitment.py`, `registry.py` (the data home for `stats_for`, `reach_for`, `TROOP_TYPE_ROLES`, `TROOP_TYPE_STATS`; read in the units/orchestration entries). `presets.py` and `recruitment.py` are not in this lane.
- **Conflicts / stale:** Docstring says "Stage-1 of the re-architecture"; the troop-type data lives in Python dicts in `registry.py`, not in a YAML registry code reads, which is the F-MB-22/F-MB-23 shape (types keyed by name, weapon-only differences collapse).
- **Open items:** none.

### modules/social_contest/__init__.py
- **What it is:** Layer-2 package marker, 2-line docstring.
- **Status:** none; live (package).
- **Bears on:** SC, CORE
- **Content that matters:** States the module `social_contest` is "A-25; plan position `31a`" and that its one entry is the composition row whose target is `roll.py`'s `roll` (`entry: verb_call`, `verb: tell`). So the whole social-contest module has a single verb-call entry (`tell`). (Docstring claim; the composition row is in `references/module_contracts.yaml` `[UNVERIFIED here]`.)
- **Conflicts / stale:** No reference to the resolver that `systems/social_contest/` holds; the two directories are separate (`systems/social_contest/__init__.py` exists but is not in this lane).
- **Open items:** Whether `tell` is the only social verb the module exposes is not stated here.

### systems/__init__.py
- **What it is:** Package marker for `systems/`, 6-line docstring (ED-IN-0071 P4, section 2a).
- **Status:** none; live (package).
- **Bears on:** PROCESS
- **Content that matters:** Says `systems/` holds "Valoria design docs by subsystem" and that doc-only subsystems (`npcs`, `articulation`, `ui`) are plain directories; sim-bearing ones add `__init__.py`.
- **Conflicts / stale:** STALE: `systems/` now holds NO `.md` (CLAUDE.md 3; design documents are under `.designs/systems/`), and `npcs`, `articulation`, `ui` are not present under `systems/` (verified by `ls`: characters, combat, fieldwork, mass_battle, overview, settlements, social_contest, threadwork, world).
- **Open items:** none.

### systems/characters/__init__.py
- **What it is:** Package marker, 8-line docstring.
- **Status:** none; live (package).
- **Bears on:** CHAR
- **Content that matters:** Says the folder is the doc home for `conviction_track_v1/v30` and character histories, and that `sim/` holds the conviction oracle; `beliefs` and `companion` are retired (FORK rows).
- **Conflicts / stale:** Stale: the docs it names are not in `systems/` any more.
- **Open items:** none.

### systems/characters/sim/__init__.py
- **What it is:** Package marker, one-line docstring.
- **Status:** none; live (package).
- **Bears on:** CHAR
- **Content that matters:** Names the oracle: conviction only (`beliefs`, `companion` retired).
- **Conflicts / stale:** none beyond the sibling note.
- **Open items:** none.

### systems/combat/__init__.py
- **What it is:** Package marker, 10-line docstring (PC lane; ED-900/904).
- **Status:** none; live (package).
- **Bears on:** PC
- **Content that matters:** Records what remains under `systems/combat/`: `combat_engine_v1/` (`capabilities.py`, `state_graph.py`, `workbench/`, a NON-package scripts dir). The v30 oracle `sim/combat.py` was deleted at plan position PC-12; the resolver (core, wrapper, combatant, config, weapons) moved to `modules/combat/` at plan position `31b`; `combat_engine_v1/systems.py` was renamed `combat_systems.py`. Verified by `ls`: `systems/combat/combat_engine_v1/` holds `capabilities.py`, `state_graph.py`, `workbench/` only (no `combat_systems.py`; it left with the resolver or was retired `[UNVERIFIED which]`).
- **Conflicts / stale:** Docstring mentions `combat_systems.py` which is not in the directory.
- **Open items:** none.

### systems/fieldwork/__init__.py
- **What it is:** Package marker, 8-line docstring (FI lane, ED-IN-0071 P4).
- **Status:** none; live (package).
- **Bears on:** FI
- **Content that matters:** Says `sim` imports as `systems.fieldwork.sim.*`; "knots still imports sim.personal.conviction (stays until the character slice) + systems.threadwork.sim". Directory now has only `sim/knots.py` (verified).
- **Conflicts / stale:** Stale: `sim.personal.conviction` was relocated to `systems.characters.sim.conviction`; `fieldwork`/`investigation` sim modules named as moved are no longer present, only `knots.py` is (F-FI-07 flags `knots.py` as holding state and drawing unseeded).
- **Open items:** none.

### systems/fieldwork/sim/__init__.py
- **What it is:** Package marker, one-line docstring.
- **Status:** none; live (package).
- **Bears on:** FI
- **Content that matters:** Names the oracle as "was sim.personal.{fieldwork,investigation,knots}"; only `knots` remains.
- **Conflicts / stale:** As above.
- **Open items:** none.

### systems/mass_battle/__init__.py
- **What it is:** Package marker, 7-line docstring (MB lane, ED-IN-0071 P4 provincial split part 1).
- **Status:** none; live (package).
- **Bears on:** MB
- **Content that matters:** Says the folder holds the `mass_battle_v30` / `mass_battle_integration_v30` / `military_layer_v30` docs and the `massbattle/units/tactic_cards/altonian_reinforcements` sim, and that `faction_action` "lazy-imports massbattle across the lane boundary until the factions slice".
- **Conflicts / stale:** STALE: no docs here; `massbattle.py` and `units.py` moved to `modules/mass_battle/`; `tactic_cards.py` and `altonian_reinforcements.py` are still present in `systems/mass_battle/sim/` and imported by nothing (F-MB-10).
- **Open items:** none.

### systems/mass_battle/sim/__init__.py
- **What it is:** Empty package marker (0 lines).
- **Status:** none; live (package).
- **Bears on:** MB
- **Content that matters:** Empty. The directory holds `bat.py`, `engine.py`, `lanchester_signature.py`, `stress.py`, `validators.py`, `walkthrough.py`, `test_persubunit_stress.py`, `workbench/`, plus `tactic_cards.py`, `altonian_reinforcements.py`, `stress_scenarios.json`, `walkthrough_example.json`, `walkthrough_template.html`.
- **Conflicts / stale:** none.
- **Open items:** none.

### systems/overview/__init__.py
- **What it is:** Package marker, 6-line docstring.
- **Status:** none; live (package).
- **Bears on:** WR, SE
- **Content that matters:** Says the folder is the doc home for `clock_registry_v30` and `peninsular_strain_v30`, and that `sim/` holds the MS (Mending Stability) world-track oracle.
- **Conflicts / stale:** Stale: docs live in `.designs/`. Per `sim/__init__.py` the MS track has no importer left.
- **Open items:** none.

### systems/overview/sim/__init__.py
- **What it is:** Package marker, 15-line docstring, marked `Status: [PROVISIONAL - Pass 2l armature stub 2026-05-17]`.
- **Status:** `[PROVISIONAL - Pass 2l armature stub 2026-05-17]`; stale (a 2026-05 stub label on a package whose other modules were retired at plan positions 29a/29b).
- **Bears on:** WR
- **Content that matters:** Lists one module, `ms_track` "no importer left since plan position 27; its own retirement is plan position 29a-ms"; retired: `accounting`, `rs_track`, `ip_track` (29a), `ci_track` (29b). Verified: `grep` for `systems.overview` / `ms_track` outside the package finds only `engine/substrate/composition.py:6` (a comment mentioning `systems.overview.sim.season`) and `engine/season/data/cast.py:438`, no importer. So `ms_track.py` is an orphan the package docstring itself flags for retirement.
- **Conflicts / stale:** Retirement "29a-ms" is not recorded as done; the file still exists.
- **Open items:** Whether `29a-ms` is open or abandoned.

### systems/characters/sim/conviction.py
- **What it is:** oracle code, 285 lines; per-Conviction Scar accumulation with thresholds 1/2/3+, season cap, Truth scaling, module-level state (PP-718 / PP-684 under `conviction_track_v1`).
- **Status:** none (code). Oracle-only; one live-ish caller.
- **Bears on:** CHAR, FI, WR (knots / threadwork scar source).
- **Content that matters:**
  - The roster is NOT defined here: `CONVICTIONS = descriptors.PURSUITS` (`:60`), read from `references/descriptor_registry.yaml:pursuit_roster` -> `engine/engine_params/descriptors.json` -> `engine.substrate.descriptors` (`:44-60`). A model single-owner chain, and the header records why: a hard-coded 9-name tuple plus `npe.py`'s different 8 made `knots.py`'s `conviction='Loyalty'` a silent magnitude-0 no-op (`:50-58`). `apply_conviction_scar` now raises on an unknown name via `descriptors.resolve_pursuit` (`:206`).
  - Hard-coded rules: `SCAR_DESTABILISE=1`, `SCAR_SHIFT=2`, `SCAR_CRISIS=3`, `SCAR_SEASON_CAP_THREAD=1` (declared at `:70` but never read: the cap is enforced inline by `season == last_season`, `:211-220`, so the constant is dead), `CERTAINTY_SCALING = {0:-1,1:-1,2:0,3:0,4:0,5:+1}` (`:76-78`; "Certainty" axis renamed Truth per ED-IN-0075 but identifiers kept).
  - State is module-level (`_conviction_state`, `:83`) with a `_store(world)` router that uses `world.convictions` if present; the season `World` has no such field (header `[ASSUMPTION]` `:17-20`), so under the season this state would be process-global and unseeded for save/load (cf. F-FI-07 for `knots.py`, which holds state the same way).
  - Thread-source detection is a string test: `source.lower().startswith('thread') or 'witness' in source.lower()` (`:213`): the season cap fires on free-text wording, not on a typed source.
  - Resonant/crisis flags are set (`:231-234`) but `ConvictionState.pending_belief_revisions` / `mark_belief_revision_pending` exist for a `beliefs` module that is retired (docstring `:13-27`, `systems/characters/__init__.py`); `mark_belief_revision_pending` therefore has no caller `[UNVERIFIED by grep; only knots.py and tests import this module]`.
- **Reads / readers:** `systems/fieldwork/sim/knots.py:349` (late import, `apply_conviction_scar`); `engine/tests/test_knots_ed912.py:141-174` (tests); `references/module_contracts.yaml:232` and `registers/mechanics_index.yaml:167` name the file as the "PERSONAL piety_track's code". `engine/season` does not import it: the season's own scar/interior path is elsewhere (see F-CHAR-03 "the interior does not move", F-CHAR-04 "the scar runs away").
- **Conflicts / stale:** docstring path `sim/personal/conviction.py` and `designs/personal/conviction_track_v1.md` (dissolved paths); "Cyclic dependency with sim/personal/beliefs ... co-defined in single commit" refers to a retired module. `module_contracts.yaml` registers it as a module code path but the season does not reach it: a registered-but-unreached oracle (candidate for F-CHAR-12 context: Layer-1's frozen `PersonInterior` is not built).
- **Open items:** whether the season should own scar state (carrier) instead of module-level dicts; `SCAR_SEASON_CAP_THREAD` dead constant.

### systems/overview/sim/ms_track.py
- **What it is:** oracle code, 92 lines; Mending Stability world-track: clamp to [0,100], baseline decay -1 per year, `apply_ms_delta`.
- **Status:** none (code; package docstring `PROVISIONAL`, retirement named as plan position `29a-ms`). Dead.
- **Bears on:** WR, SE (Mending Stability clock).
- **Content that matters:**
  - Defines `MS_FLOOR=0`, `MS_CEILING=100`, `MS_BASELINE_DECAY_PER_YEAR=-1`, `SEASONS_PER_YEAR=4`, `MS_START=60` (`:41-52`) and two functions that mutate `world.clocks['MS']` (`:60-92`). `MS_START=60` records a Jordan ruling (2026-06-06) replacing 80 and the "60/72 mode split" (`:11-17`).
  - Its dependency, the `game_state` module, "was deleted at `29b`"; "no caller passes a season `World` (which carries no `clocks`)" (`:27-29`). Verified by grep: no importer in `engine/`, `modules/`, `tests/`; only prose mentions (`engine/season/loop/matter.py:160` describes it as a prior "stored 0-100 scalar and yearly" model; `tests/valoria/test_flow_skeletons.py:345,414` mention `ms_track` seam as struck at plan position 27). So the current MS owner is `engine/season/loop/matter.py` (not read in this lane) and this file is an orphan with duplicate constants.
  - `[DRIFT]` note about `accounting._ms_decay` (`:19-25`) is stale: `accounting` was retired at 29a.
- **Reads / readers:** none.
- **Conflicts / stale:** the clock described (a scalar MS with yearly -1 decay) vs `matter.py` (stock/lattice model; `hole_register.yaml:4932` "THE LATTICE COUPLING"). Whether the MS ruling `60` still holds in the live model is not answerable from this file. Delete candidate per its own package docstring.
- **Open items:** retirement `29a-ms` pending; which carrier replaced `world.clocks['MS']` ("`33` decides the carrier").

### systems/combat/combat_engine_v1/capabilities.py
- **What it is:** PC oracle/instrument code, 173 lines; the weapon-morphology affordance gates as one table (scene-combat WS-2 / req 5) plus a self-test that checks each predicate against the live engine.
- **Status:** none (code). Oracle/dev tooling; not read by `engine/season`.
- **Bears on:** PC (weapon/kit structures), DICE (armour-defeat).
- **Content that matters:**
  - `CAPABILITIES` (`:37-58`) has four gates only: `halfsword` (`name in HALFSWORD_FORM or HALFSWORD_BASE`, i.e. a hand-listed set in `combatant`), `gap_thrust` (`head in V.THRUST_FAMILY_HEADS` or derived `S.afforded_heads` contains a point), `percussive_blow` (`head == blunt`), `open_contact` (`head_len <= CFG['GRAB_SHORT_REACH_M']`). Each names the state-graph node it gates. Everything else (blade guard to bind quality, mass to heft, armour-defeat effectiveness) is declared CONTINUOUS, "not a gate" (`:10-12`, `:59-66`). So the weapon "capability" structure is a head-token plus a few lengths, not a per-weapon authored capability list.
  - The roster is `combatant.WEAPONS` (pure data, imported at module scope; `:20`), excluding auto-switched FORMS (records carrying a `base`) (`:76`). The weapon record carries at least `head`, `head_len`, `base`, afforded heads, mode elements (`_affords_point` comment: poleaxe's spike). There is no off-hand, shield or second-weapon slot anywhere in this table (confirms F-PC-13 equipment half and F-PC-12 no unarmed record).
  - Self-test (`__main__`, `:96-173`) is the only execution artifact: checks (a)-(f) compare each predicate with `halfsword_target`, `core.HEAD_MODE`, `contact.grab_available`, and a 4000-draw reachability of `contact.GRAB_OUTCOMES`. Check (f) greps `weapons.py` source text for `pull_capable`/`hook_affordance`/`clinch=` (a prose-grep guard standing in for a rule).
  - Sets `sys.path` to `modules/combat` at import (`:15-17`), the F-PC-11 pattern; `import vocabulary as V` is a bare flat name.
- **Reads / readers:** no `engine/season` reader. Tests: `tests/valoria/test_combat_capabilities.py`, `test_combat_invariants.py:26,458` (VOCAB_CONSUMERS list names it), `_draw_stream.py:63`. `markdown_table()` generates the capability x weapon annotation table; nothing loads it back.
- **Conflicts / stale:** docstring says the engine gates "through its physics ... this module makes them EXPLICIT", i.e. the table is a second statement of rules code already enforces (a doubled owner by design, checked only when this file is executed as a script, not on each import). Header cites `06-13 consolidated-master` (a dissolved document).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/state_graph.py
- **What it is:** PC oracle/instrument code, 286 lines; the engagement/fight state graph as a data dict `STATES` (22 nodes) with `to`/`emits`/`site`, `TRACE_KINDS`, `SEPARATION_REASONS`, `INJECTION_POINTS`, and a coverage self-test (WS-1).
- **Status:** none (code); header: "supersedes the 2026-06-09 flow-and-state-map prose as the source of truth". Dev tooling.
- **Bears on:** PC, DICE (where levers read).
- **Content that matters:**
  - Node/edge structure (`:41-72`): FightInit -> EngagementInit | Yielded | Withdrawal; inner loop Approach / AwaitTempo / Exchange / Bind / Riposte / HitLanded / Contact; terminals Felled | Separation -> InterTurn; Decided -> UpsetCheck -> FinalResult; plus `Yielded` (declaration at Phase 1, ends at FinalResult with no UPSET_FLOOR draw) and `Withdrawal` (early UNRESOLVED exit). `site` strings are `wrapper.py` line numbers (`wrapper.engagement:66-85` etc.) that drift; the injection table drops line numbers on purpose (D12b, `:84`).
  - `SEPARATION_REASONS = {collapse, burst_ceiling, clean_defence, beat_exhaustion, terms}` and a dead-branch note: `collapse` and `beat_exhaustion` were flagged "never fired" by an under-powered sweep, and measured at 164 and 1,135 firings over 5,184 fights, so "NOT dead; do not re-litigate" (ED-PC-0042, `:33-39`). A model of a negative claim withdrawn after a control.
  - `INJECTION_POINTS` (`:88-128`): 12 named points saying where an invested ability's lever enters the graph (e.g. `exchange.roll`: measure lever, balance lever, tempo lever, `anti_overcommit`; `contact.axis`: `edge_grab`). States "a tradition does NOT bias a branch ... gates ACCESS to its kit (`ability_primitives._invested`)" (`:77-81`). This is the only place the lever -> graph map exists, as prose strings in code; no reader.
  - The only in-fight choice surface the graph shows is the Phase-1 `yield` declaration and the decider's `withdraw`/`ENGAGE`; "the feint lives inside the Exchange read" (`:82`). Consistent with F-PC-05 (the one in-fight choice is free) and F-PC-13 (no approach / grid round).
  - Self-test (e) sweeps 4 matchups x 30 seeds plus WIDE builds; `KNOWN_RARE = {'Felled'}`; the self-test and `trace.run_traced_fight` are the execution artifact.
- **Reads / readers:** `tests/valoria/test_combat_invariants.py:26,515-518` (data module list), `_draw_stream.py:63-64`; no engine/season reader; `engine/season` reaches the fight via the seam wrapper to `modules/combat/fight.py`. The graph is a check on the engine, not an input to it.
- **Conflicts / stale:** `site:` line refs (`wrapper.fight:282`, `wrapper.engagement:16-34`) can drift from `modules/combat/wrapper.py` `[UNVERIFIED; not opened]`. The check that every node is reachable passes on the graph the file declares, not on the wrapper's control flow (that is check (e), run only as a script).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/armour_participation.py
- **What it is:** PC dev tooling, 287 lines; the armour-interaction instrument (ED-PC-0040): `capability`, `participation`, `strike_profile`, `tier_table`, and a committed reference table with `drift()` / `--update`.
- **Status:** none (code); "DEV TOOLING, not a gate"; `tests/valoria/test_combat_armour_reference.py` turns the reference into a gate.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - `capability(name)` = max over modes {blunt, point, edge} and over base AND `HALFSWORD_FORM` of `S.adef_cap(WEAPONS[f], cfg, m)` (`:58-68`): a weapon's armour-defeat capability is derived from its record, not authored; four armour tiers `none/light/medium/heavy` (`:170`, `:209`); `ADEF_THRESHOLD[armor]` from `CFG`. Bands `clears >= 0.9`, `marginal >= thr`, `under >= 0.45` are hard-coded here (`:105`).
  - The committed `data/combat_armour_reference.json` (whole roster x 4 tiers, n=40, `generated_at_sha`) is a recorded golden for the whole PC balance picture; `drift(tolerance=0.15)` reports moved cells (`:184-236`). The file's own history: ED-PC-0038/0039 moved mail and the odachi by 41pp and 18pp unnoticed until a human read numbers (`:11-23`).
  - Finds F24 "SELECTED-BUT-INERT": `select_mode` repeatedly picks a head that lands zero damage (`strike_profile`, `:117-161`, monkey-patching `core.strike`); the podao's `point` at 0.00 against `curved_cut` 2.40 is the demonstration.
  - The reference opponent is always `'arming'` (`:48`); all measured armour is symmetric on both sides in `_duel` (`:71-86`).
- **Reads / readers:** `tests/valoria/test_combat_armour_reference.py`, `test_combat_invariants.py::test_plate_participation_tracks_armour_defeat_capability`; no engine reader.
- **Conflicts / stale:** the ED-PC-0038 claim "spear/yari/estoc -> 0 at plate" was false for the estoc per this file's header (a retracted claim; reference only). `sys.path` insert into `modules/combat` (F-PC-11).
- **Open items:** none stated. The golden JSON is data this lane did not open.

### systems/combat/combat_engine_v1/workbench/balance.py
- **What it is:** PC dev tooling, 232 lines; the variable-balancing harness: weapon-matchup, attribute-parity, tradition-field, tradition-context and weapon-armour matrix sweeps, position-swapped, Wilson-CI'd.
- **Status:** none (code). Dev tooling.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - A hand-listed `WEAPONS` roster (50 names, `:31-41`) separate from `combatant.WEAPONS` (the engine roster, 53 non-form + forms): a SECOND roster that can drift (the engine roster is derived elsewhere; this list excludes `*_halfsword` forms). Also `TRADITIONS = ["none","german","italian","spanish","japanese","chinese","filipino","english"]` (`:42`; 7 traditions + none, matching F-PC-09's seven) and `ATTRS = attributes.KEYS` (the engine owner, correctly sourced).
  - `_mk(spec)` builds a Combatant from `attrs`, `weapon`, `armor`, `tradition` only (`:78-81`): the loadout structure the harness can express is exactly {nine attributes, one weapon, one armour tier, one tradition}. It cannot express skills, equipped abilities, cross-training, or asymmetric armour (stated in `build_levers.py` docstring).
  - Imports `r8_parity_harness` from `tests/sim/v32-combat-balance` (a frozen validation station) for `FINAL_TRIALS`, `WILSON_Z`, `BAND_LO/HI` (`:28-29`), so this dev tool depends on a frozen test directory; `_wilson` is duplicated in `workbench/server.py:40` (PC audit §4 notes this).
  - CLAUDE.md names this file as the combat-balance instrument (§9 task routing); the weapon-armour matrix and tradition context test (`:121-176`) are the C1 "does the leader flip across contexts" test.
- **Reads / readers:** run as CLI (`python workbench/balance.py`); `server.py` and `catalogue.py` import helpers `[UNVERIFIED]`; no engine reader.
- **Conflicts / stale:** comments cite `designs/scene/combat_engine_v1/weapons.py` (dissolved path, `:34`).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/build_levers.py
- **What it is:** PC dev tooling, 230 lines; "what a PLAYER can change about a fighter, and what each change is worth": sweeps over skills, abilities, disposition, armour, familiarity, archetypes, plus a `mirror()` fairness control.
- **Status:** none (code). Dev tooling; modified most recently of the workbench files (file mtime 2026-11-12 vs Nov 7).
- **Bears on:** PC, CHAR (build surface), DICE.
- **Content that matters:**
  - Names the engine's four player-build levers balance.py cannot measure: `c.skills` (six axes `bind, parry, dodge, balance, technique, grab`, `:33`), learned techniques with an invested level `c.equipped` (e.g. `{'shinogi': 4.0}`), cross-training `c.known_traditions` (set via `setattr` after construction, `_POST_INIT`, `:34`, `:53-61`), and asymmetric armour. These are the kit / approach structures a person could carry; the season supplies none of them (F-PC-02, F-PC-09).
  - Armour has no wearer cost: "`c.armor` is consumed only as the TARGET's protection ... no mass, tempo, stamina or mobility cost" (`:157-162`). `c.skills` is "UNCAPPED at the engine layer ... bounding it is a character-gen/economy job that does not exist yet" (`:111-113`). Disposition `disp` runs 1-7 with 4 neutral (`:149`). Both are completeness gaps at an extreme (cf. F-PC-12).
  - The file's own finding: "most of this file's abilities rows are inside the noise floor" (n=600 gives about +/-4pp), and the ED-PC-0023 review "established the ability layer's aggregate win-rate edge is ~0 and its real effect is per-fight texture" (`:15-18`, `:122-126`). Direct support for F-PC-09 (the layer is near-silent).
  - Archetype rows build five composite builds (duellist, binder, armour-breaker, grappler, reach specialist) from weapon+armour+attributes+skills+equipped (`:186-208`): the only authored "build" objects, held in this dev script, not in a registry the engine reads.
  - `familiarity()` documents the residual tradition effect: with the imposition gate retired (ED-PC-0023) an ability-less tradition differs only through `traditions.familiarity()` feeding `WARINESS_K`; values 0.85 (unfamiliar), 0.93 (adjacent), 1.0 hard-coded in row labels (`:178-183`).
- **Reads / readers:** CLI only; no engine reader.
- **Conflicts / stale:** `WILSON_Z = 1.96` re-declared at `:31` with the comment "same constant balance.py imports" (a third copy of the method constant, with balance.py's import and server.py's `_wilson`).
- **Open items:** "bounding skills" (character-gen/economy job) is still unowned.

### systems/combat/combat_engine_v1/workbench/calibrate_generics.py
- **What it is:** PC dev tooling, 403 lines; calibration instrument for the PC-17 GENERIC lever abilities (ED-PC-0059 item 7): per-cell fights, controls, and a pre-declared PASS/INCONCLUSIVE/FAIL analysis.
- **Status:** none (code); header: "re-run it now that CR-85 has replaced `history` with `faculty` and deleted its five sigma terms (the plan's PC-17 RE-BASE), and read its limits in ED-PC-0059 before quoting a number" (`:10-11`), i.e. its recorded numbers are acknowledged stale.
- **Bears on:** PC, DICE
- **Content that matters:**
  - Defines the ability-lever structure as three parallel tuples: `LEVERS` (`visual, precommit, tactile, tempo, balance, edge_read, choke_control`), `STEMS` (`keen_eye, reading_intent, blade_feel, timing, footing, hidden_return, quiet_gather`), `TIERS` (`basic, practiced, refined`) (`:21-23`) = 21 generic abilities named `{stem}_{tier}`, taught by a Latin square over the 7 traditions: `teaching_tradition` = `trads[(lever_idx - tier_idx) % 7]` (`:44-46`). Asserted against `AP.ABILITIES[name]['lever'/'tradition']` at run time (`:71-73`): the data lives in `modules/combat/ability_primitives.py`; this file re-derives it (a second statement of the Latin square). Matches F-PC-09 "30 abilities of which 21 are generic calibration instruments".
  - `BUILD` fixes one (weapon, armour) per lever (`:25-29`; e.g. `choke_control` on poleaxe, `edge_read` on longsword); `KZERO` lists the CFG constants zeroed for the null control (`:31-41`). Control kinds: `main`, `k0`, `k0b`, `mirror`. Discovery recorded in the header: a first run's K-zero control did not null because `LEGIB_SWING_ROOM_K` is a module-level constant outside `CFG` (`:9-10`, `:80-82`) (supports F-PC-10: constants outside the config surface).
  - Method is rigorous: cluster-ratio Wilson with `n_eff = p(1-p)/Var`, Newcombe CI on differences, pre-declared MONOTONE / WRONG SIGN / CLIFF / DETECTABLE rules set "before the n=10000 run was read" (`:222-235`).
  - It monkey-patches `S.read_contest`, `S.bind_sigma`, `wrapper._TRACE` and restores them in `finally` (`:115`, `:143`); equipped abilities reach the combatant via `build_levers.build()` forwarding `equipped=` (`:3`).
  - About 12 minutes on 4 cores at n=10000; output is a JSONL file the caller names; nothing committed.
- **Conflicts / stale:** `setup(repo)` inserts paths and rebinds module globals (`global BL, wrapper, S, CFG, AP, TRADS`) on every `run_cell` call (`:49-59`, `:68`), a packaging smell (F-PC-11). The three `sys.path.insert` lines use the post-`31b` layout, so the file is current in paths; its numbers are not (header).
- **Open items:** Re-run after CR-85 (the file says so itself); nothing in the tree records that it was.

### systems/combat/combat_engine_v1/workbench/catalogue.py
- **What it is:** PC dev tooling, 301 lines; generated value + mechanics catalogue: every per-weapon derived quantity over the startable roster against a neutral fighter, the head x armour coupling matrix, constants and the CFG surface.
- **Status:** none (code); output header says "GENERATED - do not hand-edit".
- **Bears on:** PC, DICE
- **Content that matters:**
  - `QUANTITIES` (`:88-142`) is a hand-listed registry of 52 per-weapon derivations in four layers: L0 stored (`hands, mass, head_len, grip_len, head`), L1 `geometry.bake` (`curvature, point_concentration, cross_section, edge_keenness, cut, thrust, gap, halfsword`), L2 `weapon_physics` (`heft, agility, percussion_authority, puncture_pressure, handling, hand_guard, blade_guard, spine, edge_lines, grab_hazard, edge_vibration, distraction, facing_pref, hilt_mass, ... defense_affinities`), L3 `combat_systems` (`reach_base, wield_heft, weapon_tempo, close_tempo, leverage, recoverability, lunge_quality, str_demand, ...`). This is the best single map of the weapon structure in PC: a weapon record is `hands, mass, head_len, grip_len, head, geometry` and everything else is derived. It tells the kit/weapon audit that a "weapon" has no authored per-weapon capability list beyond those stored primitives.
  - `PAIRWISE` (35 functions) and `FIGHTER_ONLY` (20) are hand-listed lists of engine functions with no per-weapon value (`:145-161`): both are import-time references to `S.*`/`core.*` symbols, so a renamed function breaks the catalogue at import (a drift alarm, not a guard).
  - The neutral fighter is `attributes.DEFAULT`, no skills, no tradition, light armour (`:20-22`, `:48`); every value is "this weapon in a neutral hand".
  - `coupling_matrix()` documents the A7 finding that native cut tokens return an IDENTICAL coupling for every weapon at a tier because `core.coupling` ignores `eff` for `straight_cut`/`curved_cut` (`:190-194`).
  - Constants half prints `core.HEAD_MODE, DELIVERY, RESIST, TIER2MAT, GAP_EXPOSURE, PEN_THR, QUAL, COVERAGE_GAP, ...` and the whole `CFG` (`:244-265`); the CFG count is printed, not asserted.
- **Conflicts / stale:** It imports `capabilities as CAP` (`:42`), so the capability table and the catalogue are coupled; generated output is not stored in the repo (no committed catalogue file found in this lane). The header (`:1-22`) states the principle "the catalogue is a QUERY ... cannot drift from the code" which is the CLAUDE.md 0.05 shape done right.
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/commentary.py
- **What it is:** PC dev tooling, 210 lines; sports-commentator transcript of a traced fight with the mechanics underneath each beat (WS-6).
- **Status:** none (code). Presentation of oracle output.
- **Bears on:** PC, GO
- **Content that matters:**
  - Maps the engine event stream to prose through hand-written tables: `COMMIT_LINE`, `COMMIT_MECH`, `MODE_LINE`, `DEG_LINE`, and `_commit_band(commit)` with hard-coded edges 2.75 / 3.5 / 4.25 (`:15-32`) (the band edges also appear in `probabilities.beta_band_probs` as 0.25/0.5/0.75 of a `2 + 3*Beta` draw: two statements of one bucketing).
  - Gap: the `separation` reasons table lists `collapse, burst_ceiling, clean_defence, beat_exhaustion` and omits `terms` (`:95-98`) although `state_graph.SEPARATION_REASONS` includes `terms`; a duel-terms separation falls to the default "they separate".
  - Hard-coded prose facts: "a 5% upset chance is always live" (`:108`; `UPSET_FLOOR=0.05`, `config.py:305`) and "12 turns elapsed" (`:111`; `max_bouts=12`, `wrapper.py:555`) are literals in text rather than reads of the owners.
  - The beat call weaves commit-depth -> read -> mode -> roll -> outcome (`:115-174`) and attaches `branches` (distribution at each node) from `probabilities.py`: this is the only existing "explain the odds to the player" surface for personal combat; it consumes events, so it is a lead for the GO/UI "explain" surface (F-DICE-14 chooser odds).
- **Conflicts / stale:** The two literals above can drift from `config.py` and `wrapper.py`. Fighters named in the self-test (`Bryn`, `Halla`) are demo data.
- **Open items:** The player-facing rendition of a fight (this is the only legible one) is not wired to any season output.

### systems/combat/combat_engine_v1/workbench/narrate.py
- **What it is:** PC dev tooling, 114 lines; beat-by-beat narration of one traced fight with alternate-branch odds; "text backbone the visual workbench renders".
- **Status:** none (code).
- **Bears on:** PC, GO
- **Content that matters:**
  - A second narrator beside `commentary.py` (the first is play-by-play with mechanics; this is a terser trace with odds): both consume the same event stream and both call `probabilities`. Two renderers of one stream, each with its own event-kind switch (`commentary.commentate` and `narrate.render`), so a new event kind (`yield`, `withdraw`, `contact`, `disengage`, `wound`) must be added in both; neither handles `yield`, `withdraw`, `contact` or `disengage` events (`narrate.py:39-99`, `commentary.py:55-111`) `[verified by reading both switches]`. The engine has them (`state_graph.TRACE_KINDS`).
  - Banner "n = 1 - ONE OUTCOME, NOT A PROBABILITY" (`:13`) is the honest-instrument convention.
- **Conflicts / stale:** Header says it runs as `python -m workbench.narrate (from the engine dir)`; the engine dir is no longer where the code is (31b), so that invocation is stale `[UNVERIFIED]`.
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/presets.py
- **What it is:** PC dev tooling, 104 lines; the class-aware tuning surface for the workbench (A canonical read-only, B sim-seed, C tunable CFG, M method) and scratch overlays that never write canon.
- **Status:** none (code).
- **Bears on:** PC, DICE
- **Content that matters:**
  - `param_surface()` returns four classes: A from `m1_dice_sigma_core` (`PER_DIE[7]`, `TN_STANDARD`) and `r8_parity_harness` (`ATTR_AVG`, `ATTR_MAX`, `EXPECTED_BUDGET`); B from `m1` `LEVEL_SIGMA` (`minor/moderate/strong/major`), `M_MAX`, `SIGMA_N_COEFF`; C = every numeric `config.CFG` entry; M = statistics (trials, Wilson z, band). The dice constants are read from the frozen `tests/sim/v32-combat-balance` harness (`m1`), not from `engine/dice_engine`: the workbench's idea of the canonical d10 numbers is a second owner (cf. F-DICE-05 two samplers, F-DICE-09 typed layer omits dice facts).
  - `effective_cfg(overrides)` deep-copies `CFG` and REJECTS unknown keys ("a typo, not a new mechanic"); `promote_diff` renders a patch + ledger stub and writes nothing; `save_scratch` writes JSON to `workbench/presets/` (directory not present in the tree).
  - The `_PRESET_DIR` is created on demand; no presets are committed (verified: `ls workbench` shows `data/`, `static/` only).
- **Conflicts / stale:** Depends on the frozen `tests/sim/v32-combat-balance` directory (declared "BY DESIGN" at `:19`).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/probabilities.py
- **What it is:** PC dev tooling, 129 lines; branch-probability math for the narrator: degree distribution of one roll, outcome map from degree and mode, commit-band probabilities, per-node distributions.
- **Status:** none (code).
- **Bears on:** PC, DICE
- **Content that matters:**
  - `degree_distribution(pool, net_sigma, ob)` reconstructs the continuous engine: `net ~ Normal(mu*pool + soft_cap(net_sigma)*sigma_n(pool), sigma_n(pool))`, `sigma_n = 0.8*sqrt(pool)`, banded at `core.band_floor(band, ob)` (`:30-50`). It reads `core.band_floor` (the owner) but gets `mu` and `sigma_n` from `m1_dice_sigma_core` (frozen harness): a copy of the sampler model beside `engine/dice_engine` (F-DICE-05/07). Its falsifier is `tests/valoria/test_combat_ob_from_defender_consumers.py` (`:13-15`).
  - `outcome_distribution(degree, mode, cfg)` re-implements the wrapper outcome mapping (`wrapper.py:173-198`) from CFG constants (`NEUTRALIZE_PARRY/DODGE/WIND`, `RIPOSTE_CAP`, `RIPOSTE_ON_FAIL`, `PARTIAL_*_GRAZE`, `WIND_BIND_P`, `NEUTRALIZE_OVERWHELM_DROP`) (`:53-80`): a second statement of the outcome rules, and it ignores `exposure` (default 0.0) so the displayed odds are not the engine's for an over-committed attacker.
  - `beta_band_probs(a,b)` integrates the `commit = 2 + 3*Beta(a,b)` draw numerically with numpy (`:90-101`); the draw form is another second statement of `commit_depth`.
  - `node_distribution(ev)` covers `commit, read, roll, stophit, approach` only (`:104-118`).
- **Conflicts / stale:** Line reference `wrapper.py:173-198` in the docstring is a drifting citation `[UNVERIFIED whether still accurate]`. Uses numpy inside a module whose docstring elsewhere says the kernel is "numpy-free since ED-1085" (the engine is numpy-free; this tool is not).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/server.py
- **What it is:** PC dev tooling, 143 lines; a stdlib HTTP server for the Combat Workbench (`/api/trace`, `/api/montecarlo`, `/api/promote`, `/api/save_preset`, `/api/params`), serving `static/index.html`.
- **Status:** none (code).
- **Bears on:** PC, GO
- **Content that matters:**
  - Builds a fighter from `{label, attrs per attributes.KEYS, weapon, armor, tradition}` only (`_make_fighter`, `:32-36`): no skills, equipped abilities or cross-training reach the UI, so the workbench GUI cannot express the build surface `build_levers.py` measures.
  - `_wilson` is re-declared here (`:39-46`), identical in form to `balance._wilson` and `build_levers._wilson` and `calibrate_generics.wilson_wins`: four copies of one interval (confirms the PC audit §4 note about `_wilson` in both server.py and balance.py).
  - Montecarlo is position-swapped (`:65-89`); binds to 127.0.0.1:8765; no auth; dev only.
- **Conflicts / stale:** `from trace import run_traced_fight` shadows the stdlib `trace` module once this directory is on `sys.path` (F-PC-11 names exactly this).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/structure_scan.py
- **What it is:** PC dev tooling AND a CI guard dependency, 270 lines; AST structural-debt scan of the combat engine: duplicate definitions, zero-caller functions, magic numbers, repeated domain strings, module shape, sys.path inserts, and dead exported keys.
- **Status:** none (code); "IMPORTABLE (ED-PC-0042): the analysis runs at import; only the REPORT is under __main__".
- **Bears on:** PC, GO (export), PROCESS
- **Content that matters:**
  - Section [H] `dead_exported_keys()` (`:214-218`) compares the typed export `engine/engine_params/combat_engine_v1.json` (sections `cfg`, `core`) with an AST-derived read set of the engine package and returns exported params with no live reader. `tests/valoria/test_combat_invariants.py:59-66,test_no_dead_exported_engine_params` imports it: this is a CLAUDE.md 0.1 pt 5 load-bearing guard (crosses into the exported params). It excludes the workbench as a reader on purpose.
  - Reads `vocabulary.GUARDED_TOKENS` (the owner) rather than re-listing the 18 tokens (`:133-135`). `zero_caller_functions()` is lazy (about 20 s) and "text-matched, a CANDIDATE list" with two prior false positives recorded (`WoundTracker`, `can_choke`) (`:59-110`).
  - Shape reading: [C] counts inline numeric literals except `{0,1,2,0.0,1.0,0.5,2.0,3,100,-1}`; [D] vocabulary tokens; [G] counts `sys.path.insert` across engine and workbench files; so the file is the instrument behind F-PC-10 (18 constants outside the export) and F-PC-11 (sys.path smell) `[counts not re-run here]`.
  - Importing it at module scope parses every `.py` in `modules/combat` + `combat_engine_v1` + `workbench` (`:18-35`): import cost is paid by the shipping gate.
- **Conflicts / stale:** Docstring on `sys.path` says the import cost was the cause of making section B lazy. Lives under `systems/` while being consumed by `tests/valoria/` as a code import (a test imports a `systems/` dev script).
- **Open items:** none stated.

### systems/combat/combat_engine_v1/workbench/trace.py
- **What it is:** PC dev tooling, 27 lines; runs one fight with `wrapper._TRACE` set and returns `(result, events)`.
- **Status:** none (code).
- **Bears on:** PC
- **Content that matters:**
  - `run_traced_fight(A, B, cfg=None, seed=0, max_bouts=12, **fight_kw)`: sets `wrapper._TRACE = events.append`, seeds a stdlib `random.Random(seed)`, restores `_TRACE` in `finally` (`:14-27`). The only trace seam; used by `state_graph.py`, `commentary.py`, `narrate.py`, `server.py` and `armour_participation.py`/`calibrate_generics.py` use `_TRACE` directly. Passes `terms=`, `decide=`, `yield_decl=` to `wrapper.fight`, the only entry showing the fight can take a decider and a Yield.
  - Module-global `wrapper._TRACE` is held state set and restored around calls: not re-entrant across threads (the server is `ThreadingHTTPServer`: concurrent `/api/trace` calls would race on `_TRACE`; the docstring says "so concurrent callers are unaffected", which holds only for sequential restore) `[reasoned, not run]`.
- **Conflicts / stale:** The filename `trace.py` shadows stdlib `trace` (F-PC-11).
- **Open items:** none stated.

### systems/mass_battle/sim/altonian_reinforcements.py
- **What it is:** oracle stub, 21 lines; one function that raises `NotImplementedError`.
- **Status:** `[PROVISIONAL - Pass 2l armature stub 2026-05-17 (Pass 2e canon authoring pending faction contamination audit. Jordan 2026-05-17: "choice lock" ...)]`. Dead.
- **Bears on:** MB, FA (Hafenmark faction ability), PROCESS.
- **Content that matters:**
  - `invoke_altonian_reinforcements(world: GameState)` raises `NotImplementedError` (`:20-21`); `GameState` is an undefined name (annotation is a string only because of `from __future__ import annotations`). Dependencies listed (`sim/autoload/dice_engine`, `sim/peninsular/ip_track`) no longer exist (`ip_track` retired at plan 29a).
  - The only recorded design fact: Jordan 2026-05-17 "choice lock": once invoked, Hafenmark Standing with the other parliamentaries is permanently locked at <= +1 (`:5`). Nothing implements it.
  - Verified by grep earlier: imported by nothing (F-MB-10 names it).
- **Conflicts / stale:** canon source paths `designs/audit/...` and `designs/provincial/altonian_reinforcements_v30.md` are dissolved paths.
- **Open items:** the "choice lock" mechanism is an unbuilt design commitment (a faction-ability that costs relationship permanently); F-MB-10 recommends deletion with a `FORK:` row.

### systems/mass_battle/sim/engine.py
- **What it is:** oracle code, 303 lines; "public API wrapper for the mass-battle engine": star-re-exports the whole `modules/mass_battle` namespace, a `MECHANICS` registry with a self-test, and the oracle builders `build_unit`, `build_envelopment`, `build_refused_flank`, `resolve_battle`.
- **Status:** none (code). Oracle/gauge-facing (`bat.py`, `stress.py`, validators); `engine/season` uses `modules/mass_battle/armies.py` / `orderofbattle.py` instead.
- **Bears on:** MB.
- **Content that matters:**
  - `MECHANICS` (`:41-77`): 31 registered mechanics, each `{fn, toggle, source, status}` with every status `WIRED`; `mechanics_selftest()` asserts each `fn` resolves to a symbol in the module list (`:79-82`). It checks that a name exists, not that it is called: `pursuit`, `recall`, `morale_cascade`, `multi_turn`, `between_turn_recovery` are all "WIRED" here while the season battle never reaches them (see orchestration.py entry). Registry `source` strings cite `mass_battle_v30 section ...` and `audit/lane-c/...` (prose as provenance).
  - `build_unit` (`:90-124`) builds a single-subunit `Unit` with `troop_type='infantry'` default and derives `unit_type` from `unit_type_for(troop_type)` via the loadout (Jordan 2026-07-02: "Ranged is troop type as per the weapon assigned to troop", `:104-110`): the only place weapon assignment affects behaviour is melee/ranged. Stats `power=4, command=4, discipline=5, morale=6, dr=1` are hard-coded defaults tagged `[canonical: sim_mb_06_v9_historical_spec.md ...]` (a baseline T3 stat line repeated in four signatures).
  - `build_envelopment` (`:127-221`) and `build_refused_flank` (`:224-281`) are unit-level posture presets (Cannae, Leuctra/Leuthen) composed from `build_army` + timed `Order` queues: `release_tick=4` (CALIBRATED-DEBT), `refuse_range=10` (fixed by measurement after a prior default of 3 never fired because the geometry made it unsatisfiable, ED-MB-0041 FIX, `:225-231`), `APEX=2`, `ENVELOP_WING_GAP`, `REFUSE_ECHELON`. These are the only authored "formation" structures: a spec is a dict `{shape, troop_type, tier, starting_position, role, instructions, stance, orders...}`. `Horseshoe`/`RefusedFlank` shapes are retired (LC-8; Jordan "those are emergent outcomes", `:147`).
  - `resolve_battle(kind='single'|'multi'|'multi_unit')` routes to `run_battle` / `run_multi_turn_battle` / `run_multi_unit_battle` (`:284-297`): the oracle's three battle shapes; the season uses none of the last two.
  - Final `__all__` is computed from the union of module `__all__`s (`:302-303`), so adding a name anywhere exports it.
- **Reads / readers:** `systems/mass_battle/sim/bat.py`, `stress.py`, `validators.py`, `workbench/*`, `test_persubunit_stress.py` import it (`from systems.mass_battle.sim.engine import *`); the walkthrough uses `orderofbattle.build_unit` instead. `engine/season` does not.
- **Conflicts / stale:** docstring mentions "the sim_mb_sigma.py shim" (not in the tree `[UNVERIFIED]`); `build_unit` parameter comment `speed='Standard'` feeds only the pursuit path the season never runs.
- **Open items:** none stated.

### systems/mass_battle/sim/walkthrough.py
- **What it is:** oracle harness, 56 lines unread of 257 (read in full); runs the example battle behind the mass battle walkthrough page and rebuilds the page from `walkthrough_template.html`.
- **Status:** none (code); declares itself "Reference only, not a source of any value (CLAUDE.md section 0.05)".
- **Bears on:** MB, GO (page as a presentation of tick state), PROCESS.
- **Content that matters:**
  - It fights two `OrderOfBattle`s (`Subformation(name, troop_type, troops, role)` + one `strategy`) built from `walkthrough_example.json` through `orderofbattle.build_unit` and `orchestration.run_battle`, the same path `massbattle.resolve_field` uses for army records (`:3-8`). So the example is the only authored sample of the season-facing army shape: subformation list + one strategy + `morale_start`, `max_turns`, `page_seed`, `sweep_seeds`, `round_digits`.
  - `_Recorder` uses `sys.setprofile` to log the order of `run_battle`'s direct callees (`:80-111`): an execution artifact of the tick stage order (what the code actually calls, per tick), unusually good evidence for stage-order claims.
  - It takes the grade from `massbattle._grade(a, b, by_troops=True)` (private import, `:32`) and constants for the page from `config` (`VOLLEY_LETHALITY_SCALE`, `K_SQUARE`, `K_LINEAR`, `TICKS_PER_PHASE`, `ROUT_ONSET_FRAC`, `ROUT_CAP_FRAC`, `SUBUNIT_ROUT_FLOOR`, `ROUT_CASCADE_FRAC`) (`:207-210`): the page reads numbers from the engine, not from prose.
  - `--role` gives side A's `light_cavalry` a role (`Flanker`, `Feint`): `light_cavalry` is hard-coded as the role-bearing type (`:45`).
- **Reads / readers:** run as CLI; `tests/valoria/test_design_prose_quarantine.py` mentions "walkthrough" only as a fixture name. Uses `sys.setprofile`, so it must not run under another profiler.
- **Conflicts / stale:** none found.
- **Open items:** none stated.

### systems/mass_battle/sim/bat.py
- **What it is:** oracle gauge, 792 lines (about 530 are comment): the byte-exact DIGEST harness (the "G5 gate"): a fixed battery of 10 matchups x 24 seeds through `engine.resolve_battle(kind='multi')`, hashing the full end-state vector of every trial.
- **Status:** none (code). Live as a CI gate: `tools/ci_golden_modes_check.py` (three modes) and `tests/valoria/test_mass_battle_byte_exact.py` (two legacy-lattice modes) per the comments (`:32`, `:474-480`).
- **Bears on:** MB, PROCESS (golden discipline), DICE.
- **Content that matters:**
  - Battery (`:112-125`): `mirror, wedge, envelop, cannae, oblique, manipular, cav_charge, cav_braced, cav_shaken, ranged`; all at tier 3 with stats `P4/C4/D5/M6` (`TIER=3`, `N_SEEDS=24`, `SEED_BASE=1_000_000`, `MAX_TURNS=20`, `:51-54`). Shapes are `Line`, `Arrowhead`, `GappedLine`, plus the composed envelopment and refused-flank armies. Only three of the shapes in `ANCHOR_MAP` exist (`Line`, `Arrowhead`, `GappedLine`, `Column`).
  - Five golden digests in `EXPECTED`: `unit_legacy_mor0`, `cell_legacy_mor0`, `unit_field_mor0`, `cell_field_mor0`, `cell_legacy_mor1` (`:244-653`); key = `{unit|cell}_{legacy|field}_{mor0|mor1}` (`_mode_key`, `:662-717`). Two legacy modes are "gated by nothing in this tree and were NOT re-recorded" (`:248-249`) and are known to mismatch; the three CI-gated modes were re-recorded 2026-11-08 under Python 3.11 (`:245-248`): "the field digests differ under 3.13", so the goldens are interpreter-bound (a determinism limit relevant to the port).
  - The battery drives `run_multi_turn_battle` (kind `'multi'`): the oracle driver the season does not use. The comment at `:222-224` records "campaign armies are built melee-only (`massbattle.py:84` unit_type='melee'), so volley is unreachable from a campaign" (as of 2026-08-25). The golden digests therefore pin behaviour of the oracle path, with the season's `resolve_field` entry covered by separate tests, not by this file.
  - The comment history (about 400 lines) is the richest single record of what moved each digest: DG-3/DG-4 pool and sibling morale (2026-07-04), partition invariance (07-08), pool by troop type/quality/numbers not Command (ED-MB-0006, 07-08), octagon as damage multiplier (ED-MB-0018), degree-epsilon (ED-MB-0051), same-side exclusion (ED-MB-0059), the ruled degree ladder (ED-IN-0187), Volley TN 6->7 (ED-MB-0066, "TN7 always. Never change TN anywhere ever."), ammo (A6), `ROUT_CASCADE_FRAC` 1.0->0.6, envelopment-shock as a post-damage discipline check (ED-MB-0075). Each states a control (attribution run or direct instrumentation).
  - Jordan 2026-08-14 vocabulary ruling embedded here: "We have no 'grid' mode in mass battle. It always occurs on a coordinate field. Only the subunits can be said to be a grid." (`:173-203`); `FIELD_MOVEMENT=0` is "kept ONLY as a byte-exact regression arm", so the audit should treat the integer lattice as legacy (cf. F-MB-20 on the cell grid at season scale).
  - `trial_vector` hashes `winner, battle_turns, hp, hp_max, morale, discipline, routed` of both units (`:133-143`): not per-cell state, not casualties by source.
- **Reads / readers:** CLI (`--check`); the two CI/pytest gates above; imports `systems.mass_battle.sim.engine`. `engine/season` does not read it.
- **Conflicts / stale:** the header refers to `tests/sim/gauge_mb.py` and `coverage_matrix.md` as sources; `ci_golden_modes_check` and `test_mass_battle_byte_exact` are said not to cover the two legacy modes. A `[canonical: ...]` tag on `ANCHOR_MAP` points to `mass_battle_v30.md section deployment`. The `MB_CELL_MORALE` mode key assumes the flag is a recorded axis; the default is ON (`config.py:106`) while the bare 'cell' key says `mor0`.
- **Open items:** the two ungated legacy digests; the 3.11-vs-3.13 split; "a session with real reference-CI access" to resolve the pre-existing drift (`:628-632`).

### systems/mass_battle/sim/lanchester_signature.py
- **What it is:** oracle regression, 407 lines; the P-L Lanchester signature checks: LINEAR (melee 4:1), SQUARE (volley 4:1), NO-ANNIHILATION (mirror), and a conserved-quantity exponent fit.
- **Status:** none (code); run as `python3 -m systems.mass_battle.sim.lanchester_signature` (`:17`). Class-B tolerances, "NOT canonical magnitudes" (`:19-21`).
- **Bears on:** MB, DICE (attrition law, friction).
- **Content that matters:**
  - Thresholds: `LINEAR_BIG_WIN_BAND = (74, 83)` (Dupuy DLEDB "74-83% at 3:1+", cited to a `audit/` doc), `LINEAR_MIN_CASDIFF=20`, `SQUARE_MIN_RATIO=4`, `NOANNIH_MAX_CAS=60`, `BIG_TIER=4` / `SMALL_TIER=2` (800 vs 200 troops = 4:1) (`:43-51`). Seeds 2,000,000+, N=100.
  - Its own header records that the exponent apparatus was MIS-CITED (ED-MB-0050) and that on repaired data "melee has a clean interior minimum at p=3.20 (cv 0.00245) and volley at p=2.00 (cv 0.00327)" (`:190-197`). The check bars are `LIN_EXP_MAX = 1.4` (melee must fit linear) and `SQ_EXP_MIN = 1.6` (`:169-170`). So by the file's own recorded numbers the melee exponent is 3.2, far above the 1.4 bar: `check_law_exponents` should FAIL on the shipped engine `[UNVERIFIED: not run; reasoned from the file's own header]`. If true, the engine does not obey the "linear melee" law the Lanchester substrate claims (affects F-MB-02, the headcount path's survivor ratio, and the Lanchester design ruling).
  - Repairs recorded: the no-rout pin did not disable rout because `core.state._stochastic_break` keys on casualty fraction not morale (ED-MB-0050 REPAIR 1; 40/40 melee trajectories routed, fit window 30 of 160 ticks, before the repair); the volley scenario never fired under `stance='hold'` (REPAIR 2; now `balanced + kite`, `VOLLEY_STANCE`, `VOLLEY_INSTRUCTIONS`, `:228-229`). `_best_exponent` refuses a fit whose argmin is on a grid endpoint ("identifiable"), and a non-vacuity assert (`d['checked'] >= n`) guards the loop (`:392-394`). A model of CLAUDE.md 0.1 pts 2 and 3.
  - `_mk` builds a single-subunit `infantry` Unit with `P4 C4 D5 M6 dr1` (`:69-83`); `_LINE_ANCHOR` columns `{2:10, 3:9, 4:8}` are "inherited" magnitudes the file could not derive (`:53-66`).
  - `_rout_disabled()` patches `core.state.MB_STOCHASTIC_ROUT` by module global at call time and restores in `finally` (`:232-245`).
- **Reads / readers:** run as a module; `run()` asserts `LANCHESTER_ENABLED`. `tests/valoria` has a wrapper test `[UNVERIFIED]`. `engine/season` does not read it.
- **Conflicts / stale:** several `[canonical: mb_lanchester_design.md ...]` tags were found not to resolve and re-labelled JUSTIFIED in-file; the module-wide `LINEAR_MIN_CASDIFF`, `SQUARE_MIN_RATIO`, `NOANNIH_MAX_CAS` tags are "a WEAKER case of the same thing ... filed rather than swept" (`:166-168`).
- **Open items:** the melee p=3.2 versus the linear-law bar; the three weaker tolerance citations.

### systems/mass_battle/sim/stress.py
- **What it is:** oracle stress harness, 362 lines; fights armies of at least `troops_floor` per side at battle scale with flags on and measures overlap, idle, edge, fit and fight stats from per-tick snapshots (`walkthrough._Recorder`).
- **Status:** none (code); "Reference only, not a source of any value (CLAUDE.md section 0.05)". Data: `stress_scenarios.json` (not read in this lane; the file says it holds every tunable number).
- **Bears on:** MB (season-scale behaviour), GO (port cost: BATTLEFIELD_SIZE), PROCESS.
- **Content that matters:**
  - Builds sides four ways: `oob` (the season path: `OrderOfBattle` + `orderofbattle.build_unit`), `army` (`build_army`), `envelopment`, `refused` (`:120-157`). So the army-description shapes in use are exactly these four; the first is the one the season uses.
  - Measures per battle: `overlap` (body interpenetration by `body_depth`, split same-subunit / same-side other subunit / cross), `idle` (subunit-ticks a live, not-holding subunit did not move and was not in contact; and of those, ones where a same-side subunit WAS in contact: "an ally watching an ally fight"), `edge` (nodes within `edge_margin`, pinned nodes), `fit`, `fight` (`:9-18`, `:182-276`). These are the instruments behind F-MB-20 (the cell grid is not the battlefield at season scale) `[verify against that finding]`.
  - `--grid N` sets `BATTLEFIELD_SIZE = N` before module load and moves `orderofbattle._A_FRONT_ROW`, `_ANCHOR_COL`, `_MAX_COL` with it (`:70-74`): the season path's deployment rows/columns are module-private constants that must be patched to resize the field (hard-coded deployment geometry in `orderofbattle.py`).
  - Flags read at import, so "run one arm per process" (`:21`); arms (`shipped`, `all_on`) are in the JSON. Uses `multiprocessing` fork pool and `sys.setprofile`.
  - `concentration` default is `cell_cap_for(troop_type)` (`:89`): a per-troop-type cell capacity from `config`, i.e. the density by type.
- **Reads / readers:** CLI only; reuses `walkthrough._Recorder`; imports `modules.mass_battle.armies`, `orderofbattle`, `geometry`, `config`, and `systems.mass_battle.sim.engine`.
- **Conflicts / stale:** none found.
- **Open items:** none stated.

### systems/mass_battle/sim/test_persubunit_stress.py
- **What it is:** oracle regression script, 285 lines (named `test_*` but a script with `main()`, not collected by pytest by default); 18 checks S1-S18 on per-subunit rout/morale/discipline and the typed constructor.
- **Status:** none (code). Run: `PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 MB_BRACE_ENABLED=1 python3 systems/mass_battle/sim/test_persubunit_stress.py` (`:8`).
- **Bears on:** MB.
- **Content that matters:**
  - Pins per-subunit semantics: `Subunit.of_type` draws `TROOP_TYPE_STATS` presets, unknown type inherits (S1, S12); all-routed unit routs (S2); morale-0 routs (S3); Levy (D1) + Knights Templar (D6) differentiate (S4: "templar pool > levy pool"); `cascade_morale_hit` has no double count (S7); a broken subunit (Disc 0) has pool 0 while siblings fight (S8); `restore_discipline` capped at start (S10); discipline degrades from the subunit's OWN loss not the unit's (S11); between-battle reset restores morale, keeps discipline (S13); `check_drift` is per-subunit (S14); `advance_cells` uses per-subunit discipline (S15); `recalc_size` at 0 routs subunits (S16); `agg_discipline` is troop-weighted (S17).
  - S18 overrides `BETWEEN_TURN_MORALE_RECOVERY = 1` (`:259-266`) to test the recovery path because the shipped value is 0 (`orchestration.py:1811`): the recovery logic is exercised only under an override, so morale never recovers within a battle in the shipped configuration.
  - Uses the legacy `advance_cells(...)` signature with `enemy_cells=None` and integer `cell_offsets` (S15), i.e. the legacy-lattice arm's state, not `_node_pos` (the field path).
- **Reads / readers:** nothing imports it; a manual script. CI coverage `[UNVERIFIED]`.
- **Conflicts / stale:** `[canonical: designs/provincial/mass_battle_v30.md ...]` and `canon/editorial_ledger.jsonl` citations are dissolved paths.
- **Open items:** none stated.

<!-- ENTRIES-NEXT -->
