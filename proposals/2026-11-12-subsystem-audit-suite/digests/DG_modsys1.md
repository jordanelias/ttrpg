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
