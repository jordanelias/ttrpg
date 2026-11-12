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

<!-- ENTRIES-NEXT -->
