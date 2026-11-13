# Digest modsys1
## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: code under `engine/` (outside `engine/season/`), `modules/`, and the typed exports in `engine/engine_params/`. Finding ids cited are from `audits/03_PC_audit*.md` (F-PC-nn) and `audits/04_MB_audit*.md` (F-MB-nn). Reader/consumer claims come from one grep each unless stated. `[UNVERIFIED]` marks what I did not open.

### engine/__init__.py
- **What it is:** package docstring only (code, ED-IN-0071 P3 / ED-IN-0284), 10 lines.
- **Status:** none; live.
- **Bears on:** CORE.
- **Content that matters:**
  - Declares `engine/season/` "the only thing here that is the engine"; `substrate/`, `engine_params/`, `dice_engine/` serve it (:1-5).
  - States ONE path seam, `PATH_SEAM_ALLOWED`, "holds a single entry" (:7-9).
- **Conflicts / stale:** the docstring lists substrate as "descriptors, composition, names" but the directory also holds `battle_orders`, `combat_kit`, `pc_engine`, `stubwire` (ls). `[UNVERIFIED]` whether `PATH_SEAM_ALLOWED` still holds exactly one entry.
- **Open items:** none.

### engine/engine_params/battle_orders.json
- **What it is:** generated artifact (`tools/export_battle_orders.py`) holding the closed sets of mass-battle standing-order vocabulary.
- **Status:** `_generated ... do not hand-edit` (:2); live.
- **Bears on:** MB, CORE.
- **Content that matters:**
  - 15 roles: ShieldWall, Hold, Anvil, Push, Skirmish, Screen, Pursue, Shock, Flanker, Feint, VolleyLine, Harass, Kite, Support, Reserve (:5-21). Sourced from `ORDER_ROLES` / `config.ROLE_SPEC` in `modules/mass_battle/massbattle.py` (:2,:4).
  - `retreat_at` closed set is the strings `"none"`, `"0.5"`, `"0.25"` (:22-26), so retreat-at-fraction is a three-value choice, stored as strings.
  - Single runtime reader is `engine/substrate/battle_orders.py`; grep shows it is imported by `engine/season/data/rosters.py`, `loop/effects_information.py`, `queries/inputs.py`. This is the season's only carrier for the "manager's vocabulary" (relevant to F-MB-26).
- **Conflicts / stale:** none found; the vocabulary is exactly two sets (roles, retreat_at) with no targeting/aggression field, which is what F-MB-26 and F-MB-13 describe.
- **Open items:** none.

### engine/engine_params/combat_engine_v1.json
- **What it is:** generated export (`tools/export_engine_params.py`, "Class-C" calibrated personal-combat constants, schema 7) of `modules/combat/{config,core,attributes,weapons,vocabulary,combatant}.py`.
- **Status:** "CANONICAL combat_engine_v1 (ED-900; re-ratified ED-904)" (:3-4); live as data, but its "canonical" label is a calibration claim (Class-C = calibrated against the harness, :2), not prose canon.
- **Bears on:** PC, CHAR, DICE.
- **Content that matters:**
  - `attributes` (:6-55): 8 combat attributes `agi att disp end faculty focus spirit strength`, each `default` 3-4, all `status: IN_FLUX`. `registry_key` is null for `disp` and `faculty` (:22,:34) and `att` maps to `attr.mind.perception`; the descriptor registry has 10 attributes on a 1-7 scale with default 1 (descriptors.json:7-25). So the combat module keeps its own attribute list and defaults rather than reading the registry (F-PC-10 territory).
  - `cfg` (:56-300): about 240 tuning constants (tempo, initiative, poise, binding, reach, legibility, stamina, grab, riposte, etc.). `core` (:301-389): `BASE_POOL 6`, `POOL_FLOOR 5`, `TN 7` (:388), `DMG_SCALE`, `QUAL` table (graze .25, partial .5, success 1, overwhelming 1.5), `RESIST` by armour material vs shear/puncture/percussion, `TIER2MAT` (heavy->plate, medium->mail, light->cloth).
  - `kit` (:390-457): armour tiers `heavy light medium none`; defaults `armor: light, weapon: arming`; 54 named weapons (arming ... yari). This is the entire personal-combat kit vocabulary a season Person can name; read by `engine/substrate/combat_kit.py` and `engine/season/data/rosters.py` (grep).
  - `APPROACH_DISPLACE_K/MAX` (:79-80) is the one approach-named constant in `cfg`; there is no aggressive/normal/defensive table here, so the approach surface sits in code, not in this export (relevant to the brief's PC intent; F-PC-05, F-PC-13).
  - No `skill`, `loadout` or `second weapon` field exists in `kit`: one weapon and one armour tier per fighter (F-PC-12 "no unarmed fighter" is visible here: no `unarmed` entry in `weapons`).
- **Conflicts / stale:** `game_constants.json` says `TN` is 7 for every weapon (ED-IN-0196) and agrees with `core.TN 7`; `game_constants.json` `POOL_FLOOR` collision note says combat pool floor 5 agrees with this file (:350).
- **Open items:** all 8 attributes are `IN_FLUX` (:11 etc.), i.e. nothing has frozen them.

### engine/engine_params/composition.json
- **What it is:** generated role -> callable registry (schema 3) from `references/module_contracts.yaml#composition_roles`, 16 roles.
- **Status:** "NEVER hand-edit" (:2); live; this is the seam the season loop resolves modules through (`engine/substrate/composition.require`).
- **Bears on:** CORE, PC, MB, SE, SC, FI.
- **Content that matters:**
  - PC: `combat.fight` -> `modules.combat.fight:fight`, entry `verb_call`, verb `fight` (:6-12). Adapter is `engine/season/seam/wrappers/combat.py`.
  - MB has FIVE rows: `mass_battle.army` -> `armyrecord:apply` (:20), `army_options` -> `armyrecord:options` (:27), `army_order` -> `armyrecord:fielded` (:34), `army_preset` -> `troop_types.presets:plan` (:41, "shipped off: nothing in the season loop calls it" :46), `resolve_field` -> `massbattle:resolve_field`, verb `march` (:48-54). So the field resolver is reachable only through the `march` verb; there is no separate "auto-resolve" role and no "playable battle" role (F-MB-05).
  - Fieldwork: `fieldwork.find` -> `modules.fieldwork.find:find`, `step_call` (:13-19). Social contest: `social_contest.roll` -> `roll:roll`, verb `tell` (:111-116). Seven `settlements.*` rows (:55-110).
  - Dead roles: none of the rows are `kind: value`.
- **Conflicts / stale:** `engine/substrate/composition.py:46` describes `contest_side.a`/`.b` roles of `kind: value`; no such roles exist in this file (grep also finds `contest_side` only in composition.py and one test). The docstring is stale. Prose in `needed_by` cites `engine/season/seam/wrappers/mass_battle.py` and plan positions `31b/31c`.
- **Open items:** `mass_battle.army_preset` is registered, resolved at export time, and unused by the loop (:46).

### engine/engine_params/descriptors.json
- **What it is:** generated export of `references/descriptor_registry.yaml` (registry v1, ratified 2026-06-06); attribute roster, pursuits, axes, affiliations, heritages, stat scales.
- **Status:** "NEVER hand-edit ... SOLE reader engine/substrate/descriptors.py" (:2); live.
- **Bears on:** CHAR, SE, CORE, PC.
- **Content that matters:**
  - 10 attributes on scale 1-7, default 1 (:7-25): strength, endurance, agility, focus, acuity, will, perception, attunement, charisma, grace. Alias map folds `faculty`->acuity, `spirit`->will, `dexterity`/`coordination`->agility, `vitality`->endurance (:26-59).
  - 15 pursuits (:62-82), 7 bipolar axes (:83-96), 5 affiliations on 0-5 (:97-124), 5 heritages (:125-139), settlement stats `set.legitimacy` etc. with ceilings 7/7/5/5/5/3 (:140-171), `prac.tps` with null floor and ceiling (:179-183), `terr.fort_level` 0-4.
  - `unimplemented: {}` empty (:192).
- **Conflicts / stale:** `combat_engine_v1.json` attributes use their own defaults (3-4) and a different attribute list (`att`, `disp`, `faculty`) against this roster (default 1). Two ladders for one quantity (CLAUDE.md §0.06 S). `attributes.pending_tenth: null` (:60).
- **Open items:** none in the file.

### engine/engine_params/game_constants.json
- **What it is:** generated bridge (`tools/export_game_constants.py`) of five constants plus named collisions and divergences between the Python oracle and the Godot port.
- **Status:** "NEVER hand-edit" (:2); live as a parity manifest.
- **Bears on:** GO, PC, WR, DICE.
- **Content that matters:**
  - Constants: `COMBAT_POOL_MINIMUM 5`, `KNOT_FORMATION_OB 2`, `KNOT_FORMATION_TN 7`, `SEASONS_PER_YEAR 4`, `TN_STANDARD 7` (:6-10); owners are `combat.core.POOL_FLOOR`, `fieldwork.KNOT_*`, `overview.SEASONS_PER_YEAR` (:12-18).
  - Divergence `weapon_tn_modifiers` (:40-45): port still varies TN 5-8 by weapon (`WeaponData.gd`, `CombatLogic.gd`); engine ruled TN 7 flat (ED-IN-0196). Divergence `accord_range` (:34-39): engine has no accord model, port has integer 0-3. Divergence `coherence_bands` (:46-51): port is the retired 10-0 depleting track, engine is two-quantity distance.
  - `MOMENTUM_MAX` collision: Momentum 0-4 "has no scalar owner in engine/ today" (:29).
- **Conflicts / stale:** `owners` names `overview.SEASONS_PER_YEAR` from `systems/overview/sim/ms_track.py`, a `systems/` oracle file (sim_params.json:2653-2658), not `engine/season/`. `[UNVERIFIED]` whether the season loop reads it or has its own.
- **Open items:** three divergences wait on "port alignment" / a ruling.

### engine/engine_params/names.json
- **What it is:** generated cook of `references/names_index.yaml` (v3, count 122): canonical names, aliases, legacy tags, token classes.
- **Status:** "do not hand-edit" (:2); live.
- **Bears on:** CORE, CHAR, WR, PROCESS.
- **Content that matters:**
  - Faction roster in `by_class.faction` (:231-242): Altonia, Church of Solmund, Guilds, Hafenmark, Löwenritter, Restoration Movement, Schoenland, Valorsmark, Varfell, and the test fixture `faction x`. 10 NPC names (:250-261). The `legacy` block maps the deprecated old world-name to Solmund (:203) and the old `conviction*` names to `pursuit*` (:196-213).
  - Mass-battle terms `mass.command`, `mass.discipline`, `mass.power` (:39-41) are the only mass-battle vocabulary; legacy `Cohesion`->Discipline, `Combat Power`->Power, `Command Rating`->Command (:198-200).
  - `"substrate.key": "Key"` and legacy `EventImpact: Key` (:66,:202) still sit in the index although the Key substrate is retired (ED-IN-0232).
  - Ambiguous strings: `Order` (conv.order / set.order), `Reason` (attr.mind.acuity / conv.reason) (:263-271). Combat's `faculty` attribute folds into `Reason` here.
- **Conflicts / stale:** `substrate.key` row survives the Key retirement. Faction roster contains a fixture (`faction x`) in the canonical set.
- **Open items:** none.

### engine/engine_params/sim_params.json
- **What it is:** generated export (`tools/export_sim_params.py`, schema 2) of 283 literal constants read by AST from sim reference code, 3641 lines; 125 cited, 158 uncited, 8 assumption-grade (:4-9).
- **Status:** "No value is invented ... drift-gated by --check" (:2); live as a tool artifact, NOT a runtime input. Grep for `sim_params` finds readers only in `tools/`, `tests/valoria/`, `engine/dice_engine/dice_engine.py` (a comment at :176) and two proposals scripts; nothing under `engine/season/` reads it.
- **Bears on:** MB, SC, WR, FI, CHAR, CORE, DICE.
- **Content that matters:**
  - By module: mass_battle 164 of 283 (:14), threadwork 36, social_contest 31, engine.season 21, fieldwork 15 (:11-20); no combat entries (combat has its own file).
  - Mass-battle constants that matter: `BATTLEFIELD_SIZE 51`, `BLOCK_SIZE 100`, `CELL_CAP 200`, `CELL_FLOOR 40`, `SUBUNIT_ROUT_FLOOR 80`, `MAX_TROOPS_PER_UNIT 10000`, `UNIT_GRID_SIZE 30`, `SUBUNIT_CAP 11`, `TICKS_PER_PHASE 6`, `MAX_SUB_PHASES 5`, `MB_CAVALRY_SPEED_MULT 3.0`, `ROUT_ONSET_FRAC 0.15`, `ROUT_CAP_FRAC 0.3` (:332-1100). `TROOPS_PER_TIER {1:100,2:200,3:400,4:800}` (:1104-1111), `TROOPS_PER_SIZE 100`.
  - Stance tables `STANCE_COMMITMENT {aggressive 1, balanced 0, hold -1, retreat -1}` (:1002-1009) and `STANCE_SPEED_MOD {hold -99}` (:1018-1025): `hold` and `retreat` share the same commitment value. Orders-of-battle roles (15) are NOT here (see battle_orders.json).
  - Troop types: `TROOP_TYPE_STATS` has 14 types with only `power / discipline / morale` (1-6) (:1722-1802); `TROOP_TYPE_REACH` 15 types (:1695-1720); `TROOP_TYPE_DENSITY_CAP` for 4 mounted types, all 100 (:1120-1133); `TRAINING_SITE` maps each type to a site + number (barracks / archery_range / stable / siege_workshop; knights_templar 0.5, artillery 0.5) (:1598-1660); `ARM_SHARES` melee .45 / missile .25 / mounted .2 (:1546-1585) (sums to .9). `MUSTER_FRACTION 0.1`, `TROOPS_PER_WEIGHT 300` flagged ASSUMPTION (:1587-1596, :1662-1671). A troop type is a (power, discipline, morale, reach) record keyed by name; loadout (weapon/armour) is not in this table (F-MB-19, F-MB-22, F-MB-23).
  - Terrain: `UPHILL_*`, `RIVER_CROSSING_OFF_D -1`, `WALLS_DEFENDER_DR 3` (:1502-1543). Octagon multipliers `OCTAGON_DMG_MULT {GREEN 1, YELLOW 1.5, RED 2}`, `ANGLE_DEF_MOD` (:376-392, :806-818).
  - Test/oracle fixtures are mixed in as "params": `systems/mass_battle/sim/validators.py` `_CMD`, `_DEF_TROOPS` etc. (:2289-2495), `_kernel_tests.py` `GOLDEN_TRACE` (:2664-2724), HTTP codes `HTTP_OK 200` from the workbench server (:2548-2591), `DEFAULT_PORT 8766`. Duplicate keys: `mass_battle.ANCHOR_MAP` twice (bat.py :2039, trace.py :2593); `mass_battle.SEED_BASE` twice (:2077 = 1000000, :2201 = 2000000).
- **Conflicts / stale:** many citations point at dissolved paths (`designs/provincial/mass_battle_v30.md`, `params/core.md`, `tests/coverage_matrix_archive.md`, `designs/audit/...`); `_MORALE_FLOOR/_CEIL` cite `mass_battle_v30.md:230-231`. Source files named under `systems/` (`mass_battle/sim/bat.py`, `fieldwork/sim/knots.py`, `threadwork/sim/*.py`, `social_contest/sim/contest/*.py`, `overview/sim/ms_track.py`, `characters/sim/conviction.py`) - `systems/mass_battle/sim`, `systems/fieldwork/sim`, `systems/threadwork/sim`, `systems/social_contest/sim/contest` exist (ls); `systems/characters/sim` and `systems/overview/sim` `[UNVERIFIED]`. `social_contest` constants are mostly `[SEED]`-tagged. Citing `Jordan design` / `Stage-4 calibration` as "canonical" is a label, not a source (§0.05).
- **Open items:** 158 uncited values; "needs_jordan on the value" for density cap (:1131).

### engine/engine_params/value_pointer_links.json
- **What it is:** generated (`tools/link_values_pointers.py`) token-match links between sim_params values and names-index pointers; 59 links, 57 values, 22 pointers.
- **Status:** "nothing semantic is invented" (:2); live as a tool artifact, no engine reader (grep: only `tools/link_values_pointers.py`, a test and proposals scripts).
- **Bears on:** PROCESS, MB.
- **Content that matters:**
  - Links are by LITERAL SUBSTRING (:2), so they are largely spurious: `TROOPS_PER_TIER` -> Facility Tier (`set.facility_tier`) (:425-431); `SUPPORT_WEIGHTS` / `TIP_SUPPORT_GAP` -> Popular Support (:441-463); `STAMINA_POOL_THRESHOLDS` -> Thread Pool Score (`prac.tps`) (:337-343); `STAMINA_DRAIN_PER_CONTACT_CELL` -> Thread Fatigue (:465-471); `fieldwork._knot_id_counter` -> Church Influence via the token "counter" (:48-55); `RENDERING_STRAIN_*` linked to both Mending Stability and Turmoil.
  - `mass_battle.STANCE_COMMITMENT` / `STANCE_SPEED_MOD` link to `season.stance` (:368-383), a season concept that has no relation to a battle stance.
- **Conflicts / stale:** the links claim a pointer<->value relation that does not exist in the game; any reader treating them as bindings would be misled.
- **Open items:** none.

### engine/reference/contest-groundup/sim_verification_ledger.json
- **What it is:** co-located verification ledger (2026-09-16, ED-IN-0231) for the copied "contest-groundup" parity oracle `engine/reference/contest-groundup/engine.py` (82 lines).
- **Status:** none; live as a data file read by the sim-fabrication gate.
- **Bears on:** DICE, SC, PROCESS.
- **Content that matters:**
  - Ten entries mapping oracle variables (`MU_PER_DIE 0.4`, `SD_PER_DIE 0.8`, `TN 7`, `OB_MIN 1`, `M_MAX 1.5`, `LEVEL.minor/moderate/strong/major` 0.25/0.5/0.75/1.0, `OVERWHELM_SIGMA 0.85`, `OB_MAX 20`) to their live owner in `engine/dice_engine/` (:4-82).
  - `OVERWHELM_SIGMA` and `OB_MAX` are "oracle-local, no other owner" (:68-81): the live copy of `OVERWHELM_SIGMA` at `systems/social_contest/sim/contest/degree_extension.py:46` cites THIS ledger (:3), so a shipped constant's provenance points at a frozen reference.
  - `OB_MAX 20` appears nowhere else (`grep` measured by the file itself, :80); the Ob ceiling has no live owner.
- **Conflicts / stale:** `quoted_text` strings embed line numbers of `dice_engine.py` / `sigma_leverage.py` (`line 174`, `line 104`) that drift; cites `params/core.md` (dissolved path).
- **Open items:** "if the Ob ceiling is ever needed by live code it must be exported, not copied from here" (:80).

### engine/reference/degree-sweep/__init__.py
- **What it is:** package marker for frozen degree-sweep probes, moved from `proposals/2026-09-04-degree-sweep` under the ED-IN-0231 precedent.
- **Status:** none; live as test support.
- **Bears on:** CORE, DICE, CHAR.
- **Content that matters:**
  - Inserts its own directory on `sys.path` so `from sweep_core import S` resolves (:15-20); executed by the blocking `engine/season/tests/test_season_shape.py` (`_WD_SWEEP = files.DEGREE_SWEEP_DIR`, `_wd_arm9()` imports `arm9_forking` unmodified; grep :14247-14256).
- **Conflicts / stale:** `sys.path` mutation is a bare-import dialect that `tests/valoria/test_engine_does_not_import_systems.py` has to accommodate (:9-12).
- **Open items:** none.

### engine/reference/degree-sweep/arm9_forking.py
- **What it is:** frozen instrument "ARM 9, the forking exercise": flips each season-loop deliberation's last in-budget choice and measures whether the next three decisions change.
- **Status:** none; live as a test input (executed by `test_season_shape.py` for the W-D acceptance region).
- **Bears on:** CORE, CHAR, DICE.
- **Content that matters:**
  - Method: record every `pack_scenes` call (`recorder`, :62-119), baseline on the person's real ranked list and real budget, then swap `ranked[t]` into the last in-budget slot at one deliberation; compare the next `LOOKAHEAD = 3` decisions at strictly later ticks (:51-52, :155-257). Four outcomes: NO-LIVE-WINDOW, INERT-BY-CONSTRUCTION, DIVERGED, RECONVERGED (:179-190).
  - Finding recorded in the docstring/log text: the deliberation's `opening_set` has four clauses and none reads world state (:524-531); the only channel is a claim in the actor's ledger, and `belief_contradicts` fires only for `PERSON_PREDICATES` with `value is False`, which the corpus never produces (:533-549, "disjoint ... no claim is ever falsy"). That claim is made by comment in July-September code; `[UNVERIFIED]` against current `engine/season/decision/options.py`.
  - Budget is `scene_budget x interactions_per_scene` slots read from fixtures (:343-345, :388-391); whether choice is ever forced is "fixture-shaped" (:501-508).
  - Patches `PS_CHOOSE.pack_scenes` at module level (:114, :118) - a monkeypatch of the season's decision module for the span of a run.
- **Conflicts / stale:** cites `shape.py:2447`, `:4204-4221`, `:4572-4573` etc., from `engine/season/shape.py`, deleted at ED-IN-0203 step 10 (sweep_core.py:44-46). The docstring numbers (89 worlds, 22 candidates) are historical.
- **Open items:** H-72 / H-94 (typing `requires:` into predicates) described as "unbuilt" (:547-549).

### engine/reference/degree-sweep/arm9_subj.py
- **What it is:** a copy of `arm9_forking.py`; `diff` shows exactly one differing line (:99), where the recorded decision is `(c.verb, c.subject)` instead of `c.verb`.
- **Status:** none; reading: duplicate instrument variant (the "subject-aware" fork). Whether any test imports it: grep for `arm9_subj` finds only the proposal-side `wd_subj.py`/`wd_extra.py` and `sweep_core`; not `test_season_shape.py` `[UNVERIFIED beyond the grep]`.
- **Bears on:** CORE, CHAR.
- **Content that matters:**
  - 559 of 560 lines identical to `arm9_forking.py` (diff); a second 560-line copy to keep in sync by hand (doubled code).
  - Line 99 is the only semantic difference: decisions are keyed by (verb, subject) so a fork that changes only the target registers as a change.
- **Conflicts / stale:** same dead `shape.py` references as `arm9_forking.py`.
- **Open items:** none.

### engine/reference/degree-sweep/sweep_core.py
- **What it is:** shared core of the frozen sweep: ladders, the `S` read-only compatibility shim over `engine.season` owner modules, and the `Log` narrator.
- **Status:** none; live as test support.
- **Bears on:** CORE, DICE.
- **Content that matters:**
  - `S` is a `ModuleType` populated by `setattr` from 16 season modules (`_gaps, _ids, _car, _wld, _ros, _mx, _req, _vb, _fx, _wq, _pq, _qc, _epi, _dec, _seam, _drv`) (:54-72): reads only, rebinding does not reach the owner (:49-53); the instrument imports into season internals by name.
  - Two ladders: C = `("Overwhelming","Success","Partial","Failure")` from `degree_from_net` (margin >=3 / >=1 / 0<=m<1 / <0) vs D = `("Felled","Wounded","Untouched")` from the `kill / wound` verb row, "the only degree-keyed verb in the corpus" (:13-26, :121-129). Degree is exogenous: the sweep supplies it (:3-11).
  - A long comment records a false premise caught by a critic: `arm7_flexibility.py` and `wd_acceptance.py` were claimed unimported but are imported (:104-118).
- **Conflicts / stale:** `LADDER_D_WHY` cites `engine/season/verb_table.yaml`; `VERB_TABLE` now comes from `engine.season.data.verbs` (import :40). `[UNVERIFIED]` whether `verb_table.yaml` still exists at that path.
- **Open items:** none.

### engine/substrate/__init__.py
- **What it is:** package docstring, no code; records the removal of the Key re-export (ED-IN-0232, 2026-09-16).
- **Status:** `[live]`; live.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - States the package imports nothing and re-exports nothing, deliberately (:15-17); lists `descriptors, names, composition, stubwire, pc_engine` as leaves (:4-6).
- **Conflicts / stale:** the list omits `battle_orders.py` and `combat_kit.py`, which exist (ls) and are read by the season (`battle_orders` by `rosters.py` etc.; `combat_kit` by `rosters.py`/`test_cp_t03_03_kit.py`).
- **Open items:** none.

### engine/substrate/battle_orders.py
- **What it is:** 24-line stdlib-only reader of `engine_params/battle_orders.json`.
- **Status:** none in file; live.
- **Bears on:** MB, CORE.
- **Content that matters:**
  - Exports `ROLES` (15 names, in `ROLE_SPEC` order) and `RETREAT_AT` (`none`, `0.5`, `0.25`) (:21-24); docstring says the season "reads these two tuples and spells no role" (:5-6).
  - Importers by grep: `engine/season/data/rosters.py`, `loop/effects_information.py`, `queries/inputs.py`, `tools/export_battle_orders.py`; `modules/mass_battle/massbattle.py` appears in the grep too (likely naming the source, not importing the leaf `[UNVERIFIED]`).
- **Conflicts / stale:** none.
- **Open items:** none.

### engine/substrate/composition.py
- **What it is:** role -> callable resolver over `composition.json`; `require(role)` imports `module:attr` by string and caches (:43-69).
- **Status:** `[live, 2026-08-20]`; live.
- **Bears on:** CORE, PC, MB, SE, SC, FI.
- **Content that matters:**
  - Raises `KeyError` for an undeclared role, no default (:53-65); resolution happens once per role per process (cache `_CACHE`, :40).
  - Docstring promises two `kind: value` roles `contest_side.a`/`.b` that "engine/cross_scale/scene_dispatch.py compares a contest verdict against" (:46-51); `composition.json` has none and `engine/cross_scale/` does not exist (`ls engine`: `__init__ dice_engine engine_params reference season substrate tests`).
- **Conflicts / stale:** stale `contest_side` paragraph (see composition.json entry); the `WHY` paragraph cites the deleted old campaign driver and `systems.factions.sim.faction_action` (:5-8).
- **Open items:** none.

### engine/substrate/names.py
- **What it is:** reader of `names.json`: `CANONICAL`, `ALIASES`, `LEGACY`, `BY_CLASS`, `AMBIGUOUS`, `FACTIONS`, `canonical_for()`, `of_class()` (:51-108).
- **Status:** `[live, 2026-09-16]`; live (importers by grep: `harness/governance_spine.py`, `data/cast.py`, `data/files.py`, `data/rosters.py`).
- **Bears on:** CORE, WR, FA.
- **Content that matters:**
  - `canonical_for` raises on ambiguous display strings, legacy tags, and unknown names rather than guess (:75-102).
  - `FACTIONS` size "is not an invariant", RULED by Jordan 2026-09-19 (:68-72); includes fixture `faction x`.
  - Notes that before 2026-09-16 no code under `systems/` read any naming register, so rulings never arrived (:6-12).
- **Conflicts / stale:** the module docstring still describes the retired Key (:22-25) as history only.
- **Open items:** none.

### engine/substrate/stubwire.py
- **What it is:** the single owner of "explicitly flagged not-built": `StubResult` dataclass, `stub_resolve()`, a process-cumulative `invocations` counter, `reset_invocations()`.
- **Status:** none in file (ED-IN-0091); live. Only importer in my scope: `modules/social_contest/roll.py` (grep); the counter feeds `tools/m1_acceptance.py` row 1 (:15-19).
- **Bears on:** CORE, PROCESS, SC.
- **Content that matters:**
  - `stub_resolve(module, io_contract, *, reason)` returns a frozen `StubResult` with `stub=True` (init=False) and bumps `invocations` (:64-77); the counter is meant to be read as a before/after delta around a seeded probe (:54-61).
  - Two of its three original consumers are gone (`review_core` ratchet, a test surface); it survives for the M1 row (:12-19).
- **Conflicts / stale:** `reset_invocations()` is "test-only" and the counter being a module global means any concurrent probe shares it.
- **Open items:** none.

### engine/tests/test_knots_ed912.py
- **What it is:** regression test (ED-912, ruled 2026-06-28) on `systems/fieldwork/sim/knots.py`'s -5..+5 bond-strain gauge, plus two falsifier tests on the conviction (now pursuit) scar store.
- **Status:** none; live as an oracle test (`engine/tests/` = CI job `sim-regression`).
- **Bears on:** FI, CHAR, WR.
- **Content that matters:**
  - Pins: Distant strain -2..+5 start 0, Close -5..+5 start -2, break at +5, Tempered (-5, Close only) absorbs one rupture, break Disposition -3, Close break from positive strain -> scar +1 (:8-17, :51-125).
  - States "knots/ is an island (no campaign callers)" (:17): this tests oracle-only code under `systems/fieldwork/sim`, not a running module. The running fieldwork module is `modules/fieldwork/find.py`.
  - Falsifier tests assert on the scar STORE, not the announcement, and re-pin after IN-08 to the pursuit `honour` instead of `Honor`; legacy names `Reason`, `Autonomy`, `Continuity`, `Honor` must raise `ValueError` (:140-175).
- **Conflicts / stale:** one assertion still carries `[UNVERIFIED post-ED-912]` on `coherence_delta == -1` (:124).
- **Open items:** the Coherence value after ED-912 is unverified (:124).

### engine/tests/test_settle_margin.py
- **What it is:** CP-T01-04 test of `sigma_leverage.settle_margin` and `band_odds`: the fraction of a margin settled by the act's own draw.
- **Status:** none; live.
- **Bears on:** DICE, PC, SC, MB.
- **Content that matters:**
  - Rule: `m = raw_net + floor(q) + [u < frac(q)]` with `q = boost - ob`; the extra uniform is drawn ONLY when `frac(q) > 0` so whole-Ob rolls keep their stream (:8-11, :99-122).
  - Claims asserted: mean settled margin is `0.4*pool + boost - ob` to 1e-12 over 8*13*13 cells; P(Partial or better) strictly monotone in boost and Ob (`steps > 500` asserted, :96); `band_odds` equals a brute-force walk and agrees with 100,000 seeded draws within 3 SE (:125-173).
  - The ladder it reads through is `DE.degree_from_net(m, 0)` (:148, :167), the single degree owner.
- **Conflicts / stale:** none found.
- **Open items:** none.

### engine/tests/test_sigma_leverage_parity.py
- **What it is:** parity + property tests for `engine.dice_engine.sigma_leverage` against a committed golden table (`engine/tests/goldens/sigma_leverage_parity.json`, 1,758 rows).
- **Status:** none; live.
- **Bears on:** DICE, SC, PC.
- **Content that matters:**
  - Partitions the golden rows: 768 TN-6/8 rows are inverted into "must raise KeyError" (TN 7 only, ED-IN-0196) and the 255 `degree` rows are re-read as the pre-ruling ladder (47 moved, 208 kept; distribution by Ob `{1.0:9, 2.0:15, 3.0:23}`) (:63-107, :180-252). The table is deliberately not regenerated (:29-30).
  - `CD.degree` is `systems.social_contest.sim.contest.degree_extension` (:52): `test_bands_are_the_owners` sweeps >=4000 cells to prove no local re-banding; the extension may only demote Overwhelming to Success (`OVERWHELM_SIGMA` bar, crossover pools `[6, 8, 10]` for Ob 1/2/3) (:453-553).
  - Spec checkpoints for the soft cap `M_MAX * tanh(x/M_MAX)`: 0.5->0.48, 1.0->0.87, 2.0->1.31, 3.0->1.45 (:299-305). F1 uniformity: +0.7 sigma = +25.8 percentage points at any pool (:385-398).
  - The `sigma_leverage` ladder demotion lives in a `systems/` oracle module, not in `engine/dice_engine`: a contest-only rule the engine's single degree owner does not carry.
- **Conflicts / stale:** the docstring names oracle sources `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` and `audit/2026-06-03-contest-groundup/engine.py` (:10-12), the latter now copied to `engine/reference/contest-groundup/engine.py`; the m1 oracle's location was not checked `[UNVERIFIED]`.
- **Open items:** none.

### engine/tests/test_thread_mending_ed871.py
- **What it is:** ED-871 regression (ruled 2026-05-31): Mending costs 0 Coherence at every degree, on `systems/threadwork/sim/operations.py`.
- **Status:** none; live as an oracle test.
- **Bears on:** WR.
- **Content that matters:**
  - 300 seeds of `attempt_mending` must all give `coherence_delta == 0`, and Partial/Failure must occur (:39-49); Weaving at Relational scale keeps `-1`, or `-2` on Partial/Failure via the "blanket penalty" (:52-70).
  - The C-TW-3 defect (the blanket penalty also hits Leap against its own docstring) is "intentionally NOT fixed" (:14-16).
- **Conflicts / stale:** `game_constants.json` coherence divergence says the engine's Coherence is distance-from-equilibrium with no depleting track; this test's "Coherence cost" semantics belong to `systems/threadwork/sim` only. `[UNVERIFIED]` whether `systems/threadwork/sim` reaches `engine/season/`.
- **Open items:** C-TW-3 Leap penalty (ED-WR-0005 Stratum-B tail) unresolved here.

### modules/__init__.py
- **What it is:** package docstring: modules are "reachable running code only, one directory per module" (ED-IN-0284, ED-IN-0285).
- **Status:** none; live.
- **Bears on:** CORE.
- **Content that matters:**
  - "A module is reached by a composition row ... engine/ never imports it. The root is `tools/ci_common.py`'s `MODULE_CODE_ROOTS`" (:1-4).
- **Conflicts / stale:** `modules/combat/` is reached by a path seam (`engine/substrate/pc_engine.py`) in addition to the composition row, per CLAUDE.md §3 `PATH_SEAM_ALLOWED`, and `modules/combat/*.py` bare-import each other (see contact.py / tradition.py entries).
- **Open items:** none.

### modules/combat/contact.py
- **What it is:** 77-line grapple/contact layer of personal combat (D8/D9, I7b): `grab_available`, `grab_sigma`, `GRAB_OUTCOMES`, `grab_outcome`.
- **Status:** none; live; called by `modules/combat/wrapper.py` (docstring :11).
- **Bears on:** PC.
- **Content that matters:**
  - Dialect: `sys.path.insert(0, os.path.dirname(__file__)); import combat_systems as S` (:13-15) - bare imports, the F-PC-11 pattern; contact reads `S.leverage`, `S.WP.grab_hazard`, `S.core.logistic`.
  - `grab_available` is true for any weapon with `head_len <= cfg['GRAB_SHORT_REACH_M']` (0.375, `combat_engine_v1.json`) without an opening; otherwise needs `opening_created` set by the caller (:35-37). The dagger-class exemption is a measured threshold, not a name check (:18-25).
  - Outcome menu `('disarm','throw','pin','control','foot_pin','escape')`: a flat escape chance `GRAB_ESCAPE_P` 0.25 first, then weights `0.15+0.25p, 0.15+0.20p, 0.15+0.15p, 0.35-0.25p, 0.10` with `p = logistic(gsig)` hard-coded in the function (:53-77), not in `cfg`. `[SIM-CALIBRATE]` per its own comment.
  - `edge` term clamps skill mitigation at 0 (ED-PC-0034 fix) (:46).
- **Conflicts / stale:** the grab weights are literals inside the function, outside `combat_engine_v1.json` (F-PC-10: constants outside the designated owner).
- **Open items:** none.

### modules/combat/geometry.py
- **What it is:** pure weapon-geometry -> coefficient derivation (`gap_precision`, `thrust_factor`, `cut_factor`, `percussion_concentration`, `can_halfsword_thrust`, `bake`), build-time only (Jordan 2026-06-02).
- **Status:** none; live; baked at import by `weapons.py` (:826-832).
- **Bears on:** PC.
- **Content that matters:**
  - Input per weapon: five 0..1 primitives (`curvature, point_concentration, cross_section, edge_keenness, strike_concentration`); outputs `gap, thrust, cut, perc_conc, halfsword` (:70-96). Floors removed under ED-PC-0008/0009 so a mace reads ~0 thrust and a stiletto ~0 cut (:37-58).
  - Half-sword eligibility: `curvature <= 0.35 and point_concentration >= 0.35` (:65-68).
  - Same file name as `modules/mass_battle/geometry.py` (a different module, both bare-named `geometry`); `weapons.py` imports it as `import geometry as _geo` (:828), so `modules/combat/` must be on `sys.path`.
- **Conflicts / stale:** none.
- **Open items:** none.

### modules/combat/tradition.py
- **What it is:** 19-line facade re-exporting `traditions.py` and `ability_primitives.py`.
- **Status:** none; live as a facade (`import tradition as TR` call sites).
- **Bears on:** PC, CHAR.
- **Content that matters:**
  - Re-exports `TRADITIONS, FAMILIARITY_*, ADJACENT, familiarity` and `ABILITIES, TRADITION_KIT, kit, ability_bonus, ability_factor, eff_cw` using bare imports `from traditions import` (:13-19).
  - A tradition is "a cognitive mode ... NOT a separate rule-set"; differentiation is bottom-up (learned abilities + familiarity) (:7-9).
- **Conflicts / stale:** the facade's docstring says "`TR.eff_cw(...)/TR.familiarity(...)`" call sites; `combat_systems.py` imports `TR` and calls them at many lines (grep :908-1192).
- **Open items:** none.

### modules/combat/traditions.py
- **What it is:** the TRADITIONS dictionary: 8 tradition ids with `set`/`mode` labels, `FAMILIARITY_DEFAULT 0.85`, `FAMILIARITY_ADJACENT 0.93`, `ADJACENT` pairs, `familiarity()`.
- **Status:** none; live.
- **Bears on:** PC, CHAR.
- **Content that matters:**
  - Traditions: german, italian, spanish, japanese, chinese, filipino, english, none; `set` and `mode` are "flavour metadata ... not read at resolution" (:14-27). The 7-channel weight vector was removed 2026-06-29; `PREFERRED`/imposition gate removed ED-PC-0035 (:38-45).
  - `familiarity(a, b)` = 1.0 if same or either 'none', 0.93 if a historically adjacent pair, else 0.85 (:47-55). Used in `combat_systems.py` (`TR.familiarity(aggressor.tradition, defender.tradition)`, grep :1064-1135).
  - Whether a season Person ever carries a tradition other than `none`: grep of the season combat wrapper finds only a docstring line "tradition `none`" (`engine/season/seam/wrappers/combat.py:39`) and no `tradition` in `fight.py`; so the tradition layer is reachable only from `combatant.py`'s constructor argument (F-PC-09).
- **Conflicts / stale:** `TRADITIONS` metadata (`set`, `mode`) read by nothing; dead data kept as labels.
- **Open items:** none.

### modules/combat/vocabulary.py
- **What it is:** the combat engine's token alphabet, owned once (ED-PC-0042): heads, damage modes, armour tiers, materials, defence modes, hilt types, armour-defeat labels, `GUARDED_TOKENS`.
- **Status:** none; live.
- **Bears on:** PC.
- **Content that matters:**
  - Armour: `ARMOUR_TIERS {none, light, medium, heavy}`, `MATERIALS {none, cloth, mail, plate}`; `DEFENCE_MODES = ('parry','dodge','wind')` with order load-bearing for RNG (`modes[rng.randrange(3)]`) (:50-71).
  - `GUARDED_TOKENS` is asserted to have 18 members at import (:98-105); enforced by `tests/valoria/test_combat_invariants.py::test_no_bare_vocabulary_literal_in_consumers` (:17-19).
  - Homonyms named separately (`TIER_NONE`, `MAT_NONE`, `HILT_NONE`) (:24-27).
- **Conflicts / stale:** `HEAD_CUT` is deliberately unguarded because `geo['cut']` shares the string (:92-97).
- **Open items:** the `geo`/`w` field vocabulary routing "is FILED, not done" (:94-97).

### modules/combat/weapons.py
- **What it is:** the WEAPONS dictionary: one record per weapon as a bundle of physical primitives (mass, head_len, grip_len, hands, head, wclass, hilt, located elements/guards/haft/pommel in metres, geometry), plus import-time bakes (934 lines).
- **Status:** none; live (data half of the weapon split; `weapon_physics.py` derives).
- **Bears on:** PC, CHAR.
- **Content that matters:**
  - Record schema documented :10-70: `elements`, `guards` (with `dual_role_element`), `haft`, `pommel/butt`, `geometry`, optional `mode_elements` (fight modes with their own head + geometry + `element_ref`), `adornments`, `edge_undulation`, `grippable`, `base` (half-sword forms). Weapons with multiple modes: poleaxe, bec_de_corbin, lucerne_hammer, ji, goedendag, guisarme, kama_yari, voulge, guandao, fauchard, hook_sword (:43-56, :227+).
  - `WEAPONS` has 54 keys (matches the 54 in `combat_engine_v1.json kit.weapons`, 4 are `*_halfsword` auto-switched forms with `base=` (:138-150, :233-245, :700-713, :728-741). Mix: bladed (rapier, arming, longsword, greatsword, sabre, dagger, katana, tachi, ...), hafted (spear, yari, glaive, guandao, bardiche, ...), blunt (mace, staff, goedendag, poleaxe). No unarmed record and no shield record exist (F-PC-12).
  - Import-time bakes: `gap`/`geo` via `geometry.bake`; per-element `edges` from the `_EDGES` table with an assert that every non-base weapon has a row (:846-879); `mode_elements[*]['geo']`; `_derived` via `weapon_physics.derive`; `hand_guard`/`blade_guard` (:826-918). `GEOMETRY` back-compat dict, `HALFSWORD_FORM` mapping 4 base weapons to half-sword forms (:922-934).
  - Weapon facts are Python literals, not a registry file an author edits; `combat_engine_v1.json kit.weapons` is only a name list exported from them.
- **Conflicts / stale:** comments cite `designs/audit/2026-07-02-morphology-rearch-phase0/` and `audit/2026-07-04-weapon-morphology-granularity/` (dissolved/archived paths). `reach_adj` per-weapon residual is a hand constant (:14-16). Positional comments (e.g. `U1 PoB recalibration`) record re-balancing of masses to hit target balance bands.
- **Open items:** `material` field "DELIBERATELY INERT in R1 (no live reader)" (:39-40); a half-sword switch re-measure is "never quoted here" (:931-933).

### modules/fieldwork/find.py
- **What it is:** the `fieldwork` module entry: `find(inp: FieldworkInput) -> Findings`, 34 lines (ED-FI-0002, v9 FI-02/FI-03).
- **Status:** none; live; composition role `fieldwork.find`, entry `step_call`; called from `engine/season/seam/contest.py::find_trail` (composition.json:13-19).
- **Bears on:** FI, CORE.
- **Content that matters:**
  - The whole rule: `shown = inp.terms.get(inp.band)`; if empty return nothing; otherwise every trail item `inp.items` is returned as `(event_id, shown)` sorted by `(emitted_at, event_id)` (:28-34). No RNG: the roll belongs to the inquiry (`social_contest.roll`) (:11-14).
  - Self-described "THIN BY DESIGN" (:18-21): a band-to-terms table applied to a list; WHICH items exist is the host's projection (`epistemic.trail_of`).
  - The only module in the set that imports from `engine.season.queries.inputs` (:25), i.e. the module depends on the host's record types.
- **Conflicts / stale:** the 'modules take typed input and import nothing else' rule (CLAUDE.md §3) is satisfied only because the record types live in `engine/season/`; the module cannot be loaded without the season package.
- **Open items:** the playable (non-automated) fieldwork mode is described as "the seam a PLAYABLE fieldwork mode attaches at" (:20-22); nothing here builds it.

### modules/mass_battle/__init__.py
- **What it is:** 2-line docstring: the `mass_battle` module is "the reachable closure of `massbattle.py::resolve_field`", moved from `systems/mass_battle/sim/` at plan position 31c; a package whose files import each other by dotted name.
- **Status:** none; live.
- **Bears on:** MB, CORE.
- **Content that matters:**
  - Directory map (ls): `massbattle.py` (entry, `resolve_field`), `armyrecord.py` (3 of the 5 composition rows), `armies.py`, `orderofbattle.py`, `orchestration.py`, `battle_loop.py`, `percell.py`, `perimeter.py`, `resolution.py`, `rngsource.py`, `terrain.py`, `config.py`, subpackages `core/`, `equipment/`, `hierarchy/`, `troop_types/`.
- **Conflicts / stale:** the sibling `systems/mass_battle/sim/` still exists with `engine.py`, `bat.py`, `lanchester_signature.py`, `validators.py`, `stress.py` (ls), and `sim_params.json` lists 50+ constants from those files; `systems/mass_battle/sim/engine.py:107` still names `TROOP_LOADOUT/loadout_for` (grep), so the move left a second copy of the oracle behind `[UNVERIFIED how much is a duplicate]`.
- **Open items:** none.

### modules/mass_battle/battle_loop.py
- **What it is:** `run_battle(unit_a, unit_b, max_turns=18)`: one engagement turn of up to 18 ticks (3 phases x 6), moved out of `orchestration.py` verbatim (ED-1043).
- **Status:** none; live; `orchestration` re-exports it, "Nothing imports this module directly" (:7-8). Called by `massbattle.py:67` import chain.
- **Bears on:** MB, PC (duel inside a battle: none), CORE.
- **Content that matters:**
  - Per-tick order (:62-466): draw friction once; `volley_phase` (ranged fire before movement); pre-movement contact halts; `check_orders` then `assign_targets`; cache target centroids (simultaneity); escort positioning; `advance_cells` per moving atom; `resolve_toi_and_commit`; `halt_before_enemy`; cross-side contention; `find_contacts`; stamina drain by contact cells; `resolve_engagements(_cascading)`; simultaneous hp update; per-cell casualty distribution; close ranks; recalc size; drift check; envelopment-shock discipline roll; rout check; at `t % TICKS_PER_PHASE == 0` `phase_boundary`; turn-to-face; separate bodies.
  - Return value: `{"winner": "A"|"B"|"draw", "turns", "phases", "tick_in_phase", "a_stamina", "b_stamina", "a_hp_pct", "b_hp_pct", "a_morale", "b_morale", "truncated_*", "max_groups"}` (:468-481). The winner is `A` only if the other side is routed and this one not; `unit_conceded` ends the battle early but is graded by `massbattle._grade` (:66-69) (F-MB-04, F-MB-24).
  - The function imports ~40 names from `orchestration` at call time (:26-35) to avoid a cycle; its flags (`FIELD_MOVEMENT`, `PER_CELL`, `LANCHESTER_ENABLED`, `MB_CELL_DAMAGE`, `MB_CLOSE_RANKS`, `MB_ENVELOP_SHOCK`) are module-level environment-driven switches (F-MB-09). It asserts `FIELD_MOVEMENT => MB_NODE_COHESION` (:42-43).
  - Volley damage is `volley_dmg * VOLLEY_LETHALITY_SCALE (3)` and is stated to be band-fitting debt (:275-286).
  - A dead block: `for u in [unit_a, unit_b]: ... if u.command <= 0: u.set_morale(0.0); continue  # rout check below` (:406-413) does nothing but set morale for a zero-Command general; the comment on the loop mentions erosion that was removed.
- **Conflicts / stale:** the docstring says "max_turns=18 = one battle turn's engagement cap (3 phases)" (:15) but the loop variable `t` is a tick, returned as `turns` (:63, :472), so the return field `turns` means ticks. Several comments cite `designs/provincial/mass_battle_v30.md` and `params/mass_combat.md` (dissolved paths).
- **Open items:** none in file.

### modules/mass_battle/core/__init__.py
- **What it is:** 3-line docstring: the resolver layer ("Stage-1 of the bottom-up re-architecture"): pool assembly, exchange, attrition, state transitions; "never imports up the DAG".
- **Status:** none; live.
- **Bears on:** MB.
- **Content that matters:** `core/` holds `attrition.py`, `contact.py`, `exchange.py`, `state.py` (ls). `contact.py` and `state.py` are read in full in this lane; `attrition.py` is outside the assignment.
- **Conflicts / stale:** `core/state.py` imports `from modules.mass_battle.config import *` and mutates morale on duck-typed objects, so "pure state-in -> state-out" is aspirational: the functions mutate their arguments.
- **Open items:** none.

### modules/mass_battle/core/contact.py
- **What it is:** targeting and contact detection: `check_orders`, `assign_targets`, `resolve_cross_side_contention`, `find_contacts` (3 variants), `count_engagements_per_atom`.
- **Status:** none; live (star-imported into `orchestration`).
- **Bears on:** MB, PC (reach bodies), CORE (orders).
- **Content that matters:**
  - The standing-order vocabulary is a string-trigger mini-language: `immediate`, `tick:N`, `enemy_range:D` (filtered by facing cone, `FOV_HALF_DEG = 180 - REAR_BLIND_DEG/2 = 105`), `ally_at:D` (needs `waypoint_ref`), `own_strength:FRAC`, `signal:NAME` (:66-127). Orders fire in sequence per subunit; an unfired order blocks the later ones (:88-129).
  - An order's `behavior` dict is applied with `setattr(sub, k, v)` for any key, with special pseudo-fields `fire_signal`, `feign_retreat` and `stance` (sets `_stance_explicit`) (:130-162). `route` is clamped to a path-length budget at issue time (:178-181). So the order surface is open-ended attribute assignment on Subunit, not a closed typed record (F-MB-13, F-MB-26).
  - Targeting conditions: `nearest` (default), `weakest` (fewest troops), `in_range:N`, direct `order_target_idx`, delay countdown (:201-229); there is no targeting by troop type or role here, so Ogre Battle/Unicorn Overlord style target priorities are absent.
  - Three contact predicates selected by flags: legacy Chebyshev adjacency (`FIELD_CONTACT` off), snapped-float adjacency (`FIELD_CONTACT`), and the standoff/reach-body version when `FIELD_MOVEMENT` is on (:373-510). Per `hierarchy/units.py:33,40` (grep), `FIELD_MOVEMENT` and `FIELD_CONTACT` default to ON via environment, so the first two are live only when an environment variable or `tools/ci_golden_modes_check.py`'s `FIELD_PINS` turns them off (:34-36).
  - `resolve_cross_side_contention` returns 0 under `FIELD_MOVEMENT`; the comment records that the claim "co-location is now impossible" was refuted by measurement (875 deep body interpenetrations over 140 snapshots, ED-MB-0061) (:290-307).
  - The file embeds the continuous-frontage use: contact pairs carry `a_front`/`b_front` from `engaged_frontage` for the Lanchester term (:468-475).
- **Conflicts / stale:** the docstring's "`dynamic_facings`" and other retired items live in comments only. Heavy historical narration (Crécy, Leuctra) inside docstrings (:238-263) is prose not mechanism.
- **Open items:** `CONTACT_REACH > 0` widening "UNSPECIFIED and pending Jordan" (:485).

### modules/mass_battle/core/exchange.py
- **What it is:** combat-pool assembly primitives: `derive_command`, `clamp_command`, `command_base_pool`, `subunit_combat_pool`, `pair_pool_contribution`, `_pair_engaged_troops`, `_stamina_pool_penalty`, `D_YIELD`, `YIELD_POOL_MULT` (223 lines; the assignment listed 87 unread, 60% partial).
- **Status:** none; live (star-imported into `orchestration`).
- **Bears on:** MB, CHAR (Command from Charisma/Cognition).
- **Content that matters:**
  - Default pool, `POOL_QUALITY_MODEL` ON (config default `'1'`, `POOL_QUALITY_SCALE 0.8`): `raw = atom.eff_power * atom.eff_size * 0.8 + discipline_pen + stamina_pen`, where `pen = -clamp((5 - disc)*0.5, 0, 2)`; Command is absent from this branch (:101-124). The legacy Command branches remain behind `COMMAND_SIGMA_ENABLED` (default `'1'` too) and a plain `min(size, command)+command` branch (:125-128). So a unit's quality is the troop-type's `eff_power` (1-6 from `TROOP_TYPE_STATS`) times headcount; an individual soldier's attributes do not enter (F-MB-14, F-MB-19). Jordan directive 2026-07-08 cited: "abandon combat pools being related to the commander" (:103-113).
  - `derive_command(charisma, cognition)` is the one place individuals' attributes become a battle number: weighted mean by `CMD_CHA_WEIGHT`/`CMD_COG_WEIGHT`, clamped 1-7 (:57-65); and `command` no longer feeds the combat pool, only morale, hold speed, orders, rout (:6-9).
  - `pair_pool_contribution` redistributes the subunit's score across a contact pair by actual troops in contact cells plus depth-weighted support from ranks behind (`support_weight(depth, troop_type)`) (:151-185, :188-222); broken cells stop contributing (:209-216).
  - Per-battle friction: `raw *= unit._friction` (LogNormal draw once per battle, `MB_FRICTION_SIGMA` 1.1, default ON) (:141-147): the battle outcome includes an unattributed random multiplier.
  - `D_YIELD` and `YIELD_POOL_MULT` are read from environment variables (`os.environ`) at import (:25-29): hidden inputs (F-MB-09).
- **Conflicts / stale:** the comment says "`MB_YIELD_POCKET` (default OFF)" (:138) but `config.py:272` defaults it to `'1'` (ON); the module docstring's `[canonical: mass_battle_v30.md §A.4 Effective Combat Pool; ED-899 ...]` cites a design doc as authority. The header line count in the assignment (87 lines) disagrees with the file (223 lines); the whole file was read.
- **Open items:** the [CALIBRATED-DEBT] values for `D_YIELD` (3) and `YIELD_POOL_MULT` (0.35) are reused from other thresholds rather than derived (:19-31).

### modules/mass_battle/core/state.py
- **What it is:** morale / discipline / rout transitions: `morale_check_phase`, `rout_resolution`, `discipline_check_phase`, plus `_rout_resilience` and `_stochastic_break`.
- **Status:** none; live (phase boundary).
- **Bears on:** MB, CHAR (morale/discipline of troop types).
- **Content that matters:**
  - Stochastic rout (du Picq): each subunit draws ONE break point in `[ROUT_ONSET_FRAC 0.15, ROUT_CAP_FRAC 0.3]` of casualties, skewed by `resilience = 0.5*disc_norm + 0.5*morale/7` using START discipline and morale (:15-47). Gate `MB_STOCHASTIC_ROUT` (config default `'1'`).
  - Canonical Size triggers: casualties past 50% lose 1 morale, past 25% lose 1 more, plus unit-broken and exhaustion terms; the sum is capped at 3 then damped by `MORALE_EROSION_DAMP 0.7`, "so the EFFECTIVE cap is -2.1, NOT -3" - a declared divergence (:88-116).
  - Sibling pull `MORALE_SIBLING_PULL 0.15` toward a phase-start snapshot of troop-weighted sibling morale (:60-87); per-cell morale: cell breaks, contagion, cohesion, and `broken_cell_share() >= CELL_BREAK_ROUT_FRAC` routs the subunit (:136-148).
  - Rout floor: `atom.eff_morale <= 0 or troop_total() < SUBUNIT_ROUT_FLOOR (80)` (:187).
  - Discipline degradation: `disc_hits = int(my_loss / DISCIPLINE_LOSS_THRESHOLD)` with cumulative loss over a FIXED threshold, flagged as a shape divergence from canon: "a Discipline-5 veteran degrades on the same loss as a Discipline-1 levy" (:221-235). This is stated and unruled (needs a ruling).
  - Randomness comes from `rngsource.get()` (:8, :44), one owner of engine randomness.
- **Conflicts / stale:** the comments state `MB_YIELD_EMERGENT` is "Gated OFF by default" (:98-101) and `MB_STOCHASTIC_ROUT` "only consumed when ... on (else never called)" (:38-39); `config.py:262,181` default both to `'1'` (ON). The "byte-exact" claims in this file hold only for the OFF configuration that the golden battery pins. Mutates its arguments despite `core/__init__`'s "pure" framing.
- **Open items:** the discipline-degradation shape divergence "can be ruled on deliberately" (:229-230); the yield erosion-brake calibration "stays deferred (needs_jordan)" (:100-101).

### modules/mass_battle/equipment/__init__.py
- **What it is:** the equipment package: re-exports `weapons`, `armour`, `ARSENAL`, `ARMOURY`, and defines `TROOP_LOADOUT` and `loadout_for(troop_type)`.
- **Status:** docstring says "NOT YET WIRED into resolution ... data surface" (:10-12); reading: partly wired.
- **Bears on:** MB, PC (cross-scale mapping), CHAR.
- **Content that matters:**
  - `TROOP_LOADOUT` maps each of 14 troop types to a (weapon, armour) name pair: levy (light_cut, none), light_infantry (light_cut, light), heavy_infantry (heavy_cut, medium), cavalry (heavy_cut, heavy), archers/mounted_archers (bow, light), crossbow, sling, artillery (siege, none), knights_templar (heavy_blunt, heavy), pike (pike, medium), spearmen (spear, light), skirmishers (javelin, light), light_cavalry (light_cut, light) (:21-42). A troop type is thus a name that points at one weapon and one armour; no soldier holds a loadout of its own (F-MB-19, F-MB-22).
  - Contradiction with the docstring: `modules/mass_battle/troop_types/registry.py:10,177` imports `loadout_for` and derives the unit class `'ranged'/'melee'` from the assigned weapon, and `armies.py:283` reads it; `tests/valoria/test_reach_weapon_class.py` pins `loadout_for('pike')`. So the loadout is live for that one derivation (grep).
  - Nothing links these catalogues to `modules/combat/weapons.py` (54 personal-combat weapons); the mass names (`light_cut`, `heavy_cut`, `bow`, `siege`) are a separate vocabulary (F-MB-19, the cross-scale bridge).
  - `ARMOURY` tiers equal personal combat's `none/light/medium/heavy` and its materials (armour.py :27-40), the only shared vocabulary between the two scales.
- **Conflicts / stale:** "INERT (nothing consumes it yet)" (:17-18) is false (registry/armies consume it for unit class). Cites `mass_battle_v30 §B.2` as the source.
- **Open items:** "the primitive mapping (weapon/armour physics -> speed / DR / lethality) is still being worked out" (:19-20).

### modules/mass_battle/equipment/armour.py
- **What it is:** the armour catalogue: `ARMOURY = Registry("armour")`, four records, `get`, `dr_vs_piercing`, `tiers`.
- **Status:** none; live as data.
- **Bears on:** MB, PC.
- **Content that matters:**
  - Four entries `none/light/medium/heavy` with `material` none/cloth/mail/plate and `dr_vs_piercing` 0/1/2/3, all `provisional=True` (:36-40). "The only NUMERIC axis is DR-vs-Piercing ... CANONICAL (Ranged DR table)" (:9-11).
  - Maps to personal combat's `TIER2MAT` (heavy->plate etc.) "in spirit" (:24-26); the bridge is a comment, not code.
  - `RANGED_DR_DEFAULT = 2` and `WALLS_DEFENDER_DR = 3` live in `config`/`terrain`, not here (sim_params.json).
- **Conflicts / stale:** cites `designs/scene/combat_engine_v1/core.py` (path no longer exists; personal combat is `modules/combat/core.py`). Cites `params/mass_combat.md` as canonical.
- **Open items:** all records `provisional`.

### modules/mass_battle/geometry.py
- **What it is:** cell layout, formation shapes, octagon facing, support, and circular cell bodies for the mass-battle grid.
- **Status:** none; live (star-imported).
- **Bears on:** MB.
- **Content that matters:**
  - Formation = one of four shapes in `CELL_PATTERN_FN`: `Line`, `Arrowhead`, `GappedLine`, `Column` (Horseshoe and RefusedFlank retired as Subunit shapes, ED-909 / LC-8) (:48-56). Legacy tier tables: Line `{1:(3,3),2:(5,3),3:(5,5),4:(7,5)}`, GappedLine `{1:(2,2),2:(3,3),3:(4,3),4:(4,4)}`, Arrowhead `tier+2` rows (:11-46); continuous path `footprint_for(shape, troops, concentration, troop_type, width, depth)` builds EXACTLY n cells with n bounded so per-cell troops stay in `[CELL_FLOOR 40, cell_cap_for(troop_type)]` (200, 100 for mounted) (:62-121).
  - A cell has no identity beyond its `(r, c)` footprint id: troops per cell are a count (`cell_troops`), troop type and discipline are subunit-uniform ("per-cell type doesn't exist yet", per `core/exchange.py:160-163`). A formation is a shape, not a role slot or a named character.
  - Facing: `octagon_angle` partitions attack direction into GREEN (<45 degrees), YELLOW (45-90), RED (>=90); damage multipliers 1.0/1.5/2.0 (`OCTAGON_DMG_MULT`), defence modifiers 0/-1/-2 (:138-174). The comment records that two earlier citations for these boundaries were false and removed (ED-MB-0061) (:156-171).
  - Cell body = a circle of radius `CELL_RADIUS 0.5` (Jordan 2026-11-01: "troops have geometry. they cannot overlap"); weapon reach extends only the front along the heading; `reach_reaches(a, b)` is the contact test; `engaged_frontage` is a continuous interval-union width that feeds the Lanchester linear term (:377-532).
  - Speed per cell: `cell_speed(shape, tier, r, c)` returns 1, 2 only for an Arrowhead front rank (:328-338). A comment says the F-iii dynamic-facings helpers were deleted as write-only (:308-324).
  - `_oriented_abs_map` imports `modules.mass_battle.hierarchy.units` inside the function to read `FIELD_MOVEMENT`/`MB_NODE_COHESION` at call time (:238-241): a cycle break and a hidden coupling to environment flags. The Fable-audit B1 fix is recorded: iterating the legacy pattern ids lost cells for density-built Arrowheads (:241-247).
- **Conflicts / stale:** same file name as `modules/combat/geometry.py`. `LINE_ASPECT 1.4` is a "CALIBRATED-DEBT" in `sim_params.json:493` but defines the Column/Line proportions (:70-98).
- **Open items:** none in file.

### modules/mass_battle/hierarchy/__init__.py
- **What it is:** 2-line docstring: the unit/subunit data model ("Subunit and Unit are DATA + their own geometry/state methods; resolution lives in core/").
- **Status:** none; live.
- **Bears on:** MB.
- **Content that matters:**
  - The model file is `hierarchy/units.py` (not assigned); `sim_params.json` shows it carries `COL_WIDTH 1.0`, `_MOVE_PASSES 24`, `_SEPARATE_PASSES 400`, `_SEPARATE_ROUNDS 6`, and `grep` shows ~15 `MB_*`/`FIELD_*` environment switches at its top (lines 23-70, 166).
- **Conflicts / stale:** the docstring says units are "DATA + their own geometry/state methods; resolution in core/"; `battle_loop.py` calls `atom.advance_cells`, `halt_before_enemy`, `close_ranks`, `drain_stamina` on the units and `core/state.py` calls `atom.erode_morale`, `check_cell_breaks`, so movement and morale mutation live on the data classes. `[UNVERIFIED]` against `units.py` itself, which was not in the assignment.
- **Open items:** none.

## Cross-subsystem leads
- **MB + CHAR + CORE (F-MB-14):** the only path from an individual's attributes into a battle number is `derive_command(charisma, cognition)` (`core/exchange.py:57-65`), and since the 2026-07-08 directive Command no longer enters the combat pool; unit strength is `TROOP_TYPE_STATS` power/discipline/morale (1-6) by troop-type name times headcount (`sim_params.json:1722-1802`). Soldiers have no weapon, armour or skill fields in `modules/mass_battle/`.
- **MB + PC (F-MB-19):** two unconnected vocabularies for equipment: `modules/mass_battle/equipment` (`light_cut`, `heavy_cut`, `bow`, `siege`, `heavy_blunt`, `pike`, `spear`, `javelin`, `sling`, `crossbow`; armour tiers none/light/medium/heavy with DR 0-3) and `modules/combat/weapons.py` (54 weapons; the same four armour tier names and `TIER2MAT`). The only code-level shared tokens are the four tier names. A duel arising inside a mass engagement has no bridge.
- **PC + CHAR + CORE (F-PC-09, F-PC-12):** the kit a season Person can name is exactly `combat_engine_v1.json kit` (54 weapons, 4 armour tiers; defaults `arming` / `light`); `tradition` appears only in the season wrapper's docstring (`engine/season/seam/wrappers/combat.py:39`) and `combatant.py:126`. There is no approach (aggressive/normal/defensive) table in the export; the only `APPROACH_*` constants are `APPROACH_DISPLACE_K/MAX` (:79-80). `fight.py` has no occurrence of "approach", "aggress" or "defens" (grep).
- **CORE (composition):** `mass_battle.army_preset` is a registered role the loop never calls (composition.json:41-47). `composition.py`'s docstring describes `contest_side.*` roles that exist nowhere in `composition.json` (and `engine/cross_scale/` does not exist).
- **DICE + SC + CORE:** `sigma_leverage.degree` is gone from the engine and lives in `systems/social_contest/sim/contest/degree_extension.py` as a contest-only demotion of Overwhelming; `OB_MAX 20` has no live owner (`sim_verification_ledger.json:80`). The engine's single degree owner is `dice_engine.degree_from_net`.
- **GO + PC (game_constants.json):** the port still varies TN by weapon (5-8), against the oracle's flat TN 7; `MOMENTUM_MAX` (Momentum 0-4) has "no scalar owner in engine/".
- **FI + WR + PROCESS:** `sim_params.json` mixes game parameters with test fixtures and HTTP status codes; `value_pointer_links.json` links by substring; neither is read by `engine/season/`. The tool artifacts count toward "283 params, 125 cited" but are not a measure of what the loop reads.
- **MB + PROCESS:** about 86 `os.environ` reads in `modules/mass_battle/` (grep count 91 minus pyc hits) decide behaviour flags; the golden battery pins some off (`tools/ci_golden_modes_check.py` FIELD_PINS, per `core/contact.py:34-36`), so the shipped defaults (many `'1'`) differ from the byte-exact configuration the comments describe.

## Likely stale or superseded
- `engine/substrate/composition.py:46-51` - the `contest_side.a/.b` `kind: value` paragraph (no such rows; `engine/cross_scale/` absent).
- `engine/reference/degree-sweep/arm9_forking.py`, `arm9_subj.py`, `sweep_core.py` - cite `shape.py` line numbers, deleted at ED-IN-0203 step 10; their "claims never falsy / opening_set reads no world" findings date from 2026-09 `[UNVERIFIED against current decision/options.py]`.
- `modules/mass_battle/equipment/__init__.py:10-18` - "NOT YET WIRED / INERT" contradicts `troop_types/registry.py:177` and `armies.py:283`.
- `modules/mass_battle/core/state.py:38-39, 98-101` and `core/exchange.py:138` - "default OFF" for `MB_STOCHASTIC_ROUT`, `MB_YIELD_EMERGENT`, `MB_YIELD_POCKET`; `config.py` defaults all three to ON (`'1'`).
- `modules/mass_battle/battle_loop.py:406-413` - a loop that only handles `command <= 0` under a comment about erosion that no longer exists there.
- `engine/engine_params/names.json` - `substrate.key` row and `EventImpact` legacy tag survive the Key retirement.
- `engine/engine_params/sim_params.json` - 50+ rows come from `systems/mass_battle/sim/` oracle/test-fixture files, duplicates (`ANCHOR_MAP`, `SEED_BASE`), and citations to dissolved paths.
- `modules/mass_battle/equipment/armour.py:5-6` - cites `designs/scene/combat_engine_v1/core.py`.
- `engine/engine_params/value_pointer_links.json` - substring "links" with no semantic content.

## Items that could change an audit finding
- **F-MB-19 (loadout not read):** CONFIRM with a nuance. `TROOP_LOADOUT` is read, but only to derive `'ranged'/'melee'` unit class (registry.py:177, armies.py:283) and nothing else; pool strength comes from `TROOP_TYPE_STATS`, not weapon or armour. The `equipment/` docstring's "not wired" is half-false.
- **F-MB-14 (individuals' attributes do not reach the battle):** CONFIRM. `derive_command` is the only attribute-to-battle function and Command is outside the combat pool (`core/exchange.py:101-124`).
- **F-MB-09 (hidden inputs and held state):** CONFIRM and sharpen: ~86 `os.environ` flags, many defaulting ON, with comments describing the OFF state; `D_YIELD` and `YIELD_POOL_MULT` read env at import.
- **F-MB-13 / F-MB-26 (choice surfaces priced wrongly; manager vocabulary has no carrier):** CONFIRM. The season carrier is two closed sets (15 roles, three `retreat_at` strings); the in-battle order surface is open `setattr` on Subunit with six trigger strings, and target selection has no role/type priority (`core/contact.py:201-229`).
- **F-MB-24 / F-MB-04 (field returns a winner / defeat attribution):** CONFIRM at the module level: `run_battle` returns `winner A|B|draw` and `_grade` reads `unit_conceded`.
- **F-MB-10 (dead and unreached code):** supports: the legacy contact paths (`FIELD_CONTACT` off, plain adjacency), the Command pool branches behind `POOL_QUALITY_MODEL`, `army_preset` role, `TRADITIONS[*]['set'|'mode']` metadata, and the dead `command <= 0` loop remainder in `battle_loop.py`.
- **F-MB-20 (at season scale the cell grid is not the battlefield):** neutral; `BATTLEFIELD_SIZE 51`, `UNIT_GRID_SIZE 30`, `MAX_TROOPS_PER_UNIT 10000`, `CELL_CAP 200` are the grid constants (sim_params.json:332-520).
- **F-MB-22 / F-MB-23 (troop types differing by weapon; keyed on type names):** CONFIRM data side: 14 troop types with `(power, discipline, morale)` and `reach` keyed by name in `sim_params.json:1695-1802`; `TRAINING_SITE` is also keyed by name.
- **F-MB-25 (reference surfaces that contradict code):** supports with the "default OFF" comments and `equipment/__init__.py` "INERT".
- **F-MB-17 / F-MB-18 (hierarchy, role shapes):** not examined here beyond `hierarchy/__init__.py`; `units.py` was outside the assignment.
- **F-PC-09 (tradition/ability/morphology-lever layer unreachable from the season):** CONFIRM (tradition appears in the season wrapper only as a docstring; `traditions.py` metadata `set`/`mode` is read by nothing).
- **F-PC-10 (constants outside the declared home):** CONFIRM with an example: grab-outcome weights `0.15+0.25p`, `0.35-0.25p`, `0.10` are literals in `contact.py:63-69`.
- **F-PC-11 (bare-import dialect):** CONFIRM in `contact.py:13`, `tradition.py:13,17`, `weapons.py:828,906`; `degree-sweep/__init__.py` adds a second `sys.path` mutation in `engine/`.
- **F-PC-12 (no unarmed fighter):** CONFIRM: `WEAPONS` has 54 records, none unarmed, none a shield.
- **F-PC-05 / F-PC-13 (approach surface):** CONFIRM no approach table in `combat_engine_v1.json`, and `modules/combat/fight.py` has no approach term (grep).
- **F-PC-08 (draw has second owners):** not examined here.
- **Unanswered question for the designer:** the discipline-degradation rule uses a fixed cumulative-loss threshold rather than a per-turn comparison to the unit's Discipline (state.py:221-235); the author flagged it for a ruling and nothing in the files records one.
