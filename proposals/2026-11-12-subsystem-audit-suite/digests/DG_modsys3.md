# Digest modsys3

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: `systems/settlements/valoria_geography_v30.yaml` (read in full, 930 lines), the two `social_contest` package inits, the threadwork package inits and the six `threadwork/sim` modules (`co_movement`, `coherence`, `collective`, `operations`, `opposing`, `threadcut`). `rendering.py` (41 lines) is not on the list; it was opened only for its header. Every file on the list was read to its end. Readers were found by one grep each, run over `*.py` and `*.yaml` outside `.designs/`, `.audit/` and `.claude/worktrees/`.

### systems/settlements/valoria_geography_v30.yaml
- **What it is:** Hand-authored geographic data canon, ED-779 / PP-707 / PP-709, "Phase 2 data", with 17 provinces, 37 settlements, two adjacency graphs, terrain, cost matrices and overlays. Reconciled to the PP-726 scheme on 2026-07-13.
- **Status:** Line 1 reads `# Status: CANONICAL`. Line 6 reads `# Status: PROVISIONAL — calibration values tunable in Phase 4`. `meta.status` is `PROVISIONAL`. Reading: live, as a data file the engine reads. Its Status is self-contradictory.
- **Bears on:** SE, MB, CORE, FI (POI catalog), WR (radiation bands).
- **Content that matters:**
  - 17 `provinces` (T1..T17; keys are territories, though the sections and engine call them provinces). Each carries `faction`, `region`, `anchor`, `polygon`, `fort_level`, `spiritual_weight`, `proximity_calamity`, `starting_pros` and a `settlements` list (:18-239). T15 Askeheim has `faction: Uncontrolled` and `settlements: []`. The `starting_pros` values sum to 48.
  - 37 `settlements` (S-001..S-037; :246-543). Each has `territory`, `type`, `controller`, `coords` and `stats: [Prosperity, Defense, Order]`. The 21 PP-726 settlements have "inferred, not hand-tuned" coordinates and stats, and the file says "flag before treating as balance-calibrated" (:244). I checked by script that every settlement appears in its province's list and that `controller` equals the province `faction` everywhere. S-014 additionally carries `controller_subordinate: Löwenritter`.
  - Two adjacency graphs. The territory graph `adjacency:` has 26 edges, typed road, coastal, mountain_pass or gate (:548-574). The settlement graph `settlement_adjacency:` has 55 edges by script count (54 road, 1 sea; :594-669). The header comments claim 55 (:589) and 56 (:602) in different places. The script confirms S-037 Schoenland is the only node with degree 1. This is the "foreign-exempt" case awaiting ED-055 naval scope.
  - Mechanism-bearing layers: `terrain` polygons (:675-755), `terrain_cost_matrix` (:760-771; mountain 999, fjord_coast 2.5, road_overlay 0.7), `vision_range` (:775-796; base 240 px with terrain, weather and season factors), `march_budget` (:800-803; 100 px per Military point, cavalry 1.5, skirmish 1.3), `water`, `bridges`, `forgetting_zone` polygon (:835-838; "TS≥30 individual gating; no faction-property exemption (PP-703)"), `radiation_bands` (:842-872; concentric circles at (980,2700), radii 120/400/900/1450/2050/2700), `altonian_passes` (:875-889), `poi_catalog` (:893-910; per-territory counts of resource, secret, remnant and anomaly) and `scale_anchors` (:915-918).
  - Readers, by grep. `engine/season/data/files.py:147` names the path. `data/geography.py` reads the territory `adjacency:` only (:58). `harness/populated.py` reads `provinces` and `settlements` (:1136-1975). `modules/mass_battle/terrain.py` reads `terrain:` polygons and cites `terrain_cost_matrix` and `altonian_passes`. `engine/season/data/rosters.py:448` and `cohorts.yaml:111` cite the file in comments. `tests/test_in35_lattice_coupling.py` uses `radiation_bands` as an independent control, per `geography.py:52`.
  - Keys with no reader that I found under `engine/season` or `modules` (python only): `settlement_adjacency`, `vision_range`, `march_budget`, `poi_catalog`, `scale_anchors`, `forgetting_zone`, `terrain_cost_matrix` (cited in a comment only), `altonian_passes`, `water`, `bridges`. Consistent with F-SE-06, "the geography feeds the battlefield and nothing else" (`07_SE_audit.md:309`), and with the SE ordered-work row that `settlement_adjacency` "gets its first reader" (`07_SE_audit.md:588`). [UNVERIFIED for non-.py readers such as Godot or json.]
- **Conflicts / stale:**
  - Doubled fact, a real disagreement: `provinces.T8` and `T17` carry `proximity_calamity: 4`, but `radiation_bands` band 5 lists T8 and T17 (:870-872; verified by script). Every other territory agrees. The band label and the province field are two copies of one distance, and `geography.py:52` says the bands are meant to be the node distance (a breadth-first reading of the edges).
  - The cross-reference block (:921-929) points to `designs/world/…`, `designs/territory/…` and `designs/provincial/…`. `designs/` is dissolved (CLAUDE.md §3), and the paths now resolve only through the restructure ledger.
  - The `scale_anchors` comment says "2880÷48 = 60 hex rows", but the only authored value is `hex_grid_size_px: 32` (2880/32 = 90 rows). The comment and the datum disagree.
  - The file mixes "Halvardshelm" (T11, S-028) and "Halvarshelm" (T17, S-023); the spelling difference is deliberate but easy to mistake.
  - The `provinces` key is "stale" per `populated.py:1136` (the rows are territories), and the T-number scheme still appears in comments as "pre-canon T-numbers".
- **Open items:** Phase 4 calibration (ED-781) of the cost matrix, vision and march values is left open. Naval scope (ED-055) is open for S-037. `march_layer_v30` was a skeleton, and nothing reads `march_budget` or `terrain_cost_matrix` as movement cost [UNVERIFIED beyond the python grep].

### systems/social_contest/__init__.py
- **What it is:** Package docstring only (6 lines). It records the ED-IN-0071 P4 extraction of the social_contest docs and the contest sim package.
- **Status:** none. Reading: live as a namespace marker; the content is historical.
- **Bears on:** SC, PROCESS.
- **Content that matters:**
  - The docstring says sim imports as `systems.social_contest.sim.*` and that `tribunal` "stays in sim/personal/ (faction-side, deferred)" (:1-5). It defines nothing else.
  - It still names `sim/personal/`, a path that is gone (CLAUDE.md §3 dissolved `sim/`).
- **Conflicts / stale:** The "design docs from designs/scene/" and `sim/personal/tribunal` referents are dissolved or archived.
- **Open items:** none.

### systems/social_contest/sim/__init__.py
- **What it is:** One-line docstring, "social-contest oracle (was sim.personal.contest package + parliamentary_*)".
- **Status:** none. Reading: namespace marker; historical wording.
- **Bears on:** SC.
- **Content that matters:**
  - It imports nothing and exports nothing, so submodules are reached by their full path.
- **Conflicts / stale:** It refers to `sim.personal.*`, which no longer exists.
- **Open items:** none.

### systems/threadwork/__init__.py
- **What it is:** Package docstring, 5 lines. It says the package was moved from `designs/threadwork/` and `sim/thread/` (ED-IN-0071 P4) and imports as `systems.threadwork.sim.*`.
- **Status:** none. Reading: namespace marker.
- **Bears on:** WR.
- **Content that matters:**
  - The docstring says "design .md at root + sim/ oracle", but the tree has no `.md` here and only `sim/`; the design doc is quarantined at `.designs/systems/threadwork/reference/threadwork_v30.md` (see `module_contracts.yaml:302`).
- **Conflicts / stale:** The "design .md at root" claim is false today (CLAUDE.md §3: `systems/` holds no `.md`).
- **Open items:** none.

### systems/threadwork/sim/__init__.py
- **What it is:** Module docstring, "Thread layer operations and substrate mechanics". Status line: `[PROVISIONAL — Pass 2l armature stub 2026-05-17]`. It lists the modules.
- **Status:** `[PROVISIONAL — Pass 2l armature stub 2026-05-17]`. Reading: stale as a status; the modules are no longer stubs. The module list was updated for position 27.
- **Bears on:** WR.
- **Content that matters:**
  - The list matches the files on disk, including "rendering: STRUCK, no entry point — holds only its record (plan position 27)" and the note that the 10→0 track is retired and Part 3 is superseded (ED-WR-0010) (:5-13).
  - It imports nothing.
- **Conflicts / stale:** The "armature stub" Status predates the rewrite of `coherence.py` and the Mending work (WR-01..03).
- **Open items:** none.

### systems/threadwork/sim/co_movement.py
- **What it is:** The Co-Movement deck, 15 cards (CM-01..CM-15), drawn per Thread operation. 141 lines, ED-577.
- **Status:** none in-file; module header claims canon source `threadwork_v30.md` Part 4. Reading: oracle-only and unreached by the game.
- **Bears on:** WR, CORE.
- **Content that matters:**
  - `CO_MOVEMENT_CARDS` is a hard-coded list of tuples `(id, name, actualized_ms_delta, actualized_notes, unactualized_ms_delta, unactualized_notes)` (:42-59). The card effects are English strings in `notes`. No effect is implemented except the reported `ms_delta`.
  - `draw_comovement_card(op_type, depth, world, rng)` (:94). `actualized = depth not in ("Object","Personal")` (:108), so Object and Personal depth take the unactualized `ms_delta`.
  - The deck state is module-level `_deck_state` unless the world has a `comovement_deck` attribute (:73-81). `grep -rn comovement_deck engine` found no such World field, so the module-level fallback is the only live path.
  - `apply_comovement_effects` was struck at plan position 27 (:15-21). A drawn card still reports `ms_delta`, and nothing writes it.
  - Readers: `grep` over `.py` found no importer outside `systems/threadwork/sim` and no test call of `draw_comovement_card`. The card draw is dead outside the file itself. `op_type` is unused in the body.
- **Conflicts / stale:** The comment at :117 says "Reshuffle when all 18 cards drawn", while the deck holds 15. CM-16..18 (Mending-specific, §7.1) are not implemented. The docstring at :24-25 lists `sim/autoload/dice_engine` as a dependency; the import actually used is `random`.
- **Open items:** CM-16/17/18 (Mending deck) "will land with Mending sim integration"; nothing builds them. Every card effect other than `ms_delta` is a note string with no implementation.

### systems/threadwork/sim/coherence.py
- **What it is:** Coherence as a distance from the human equilibrium, with two stored quantities (`resting_point` and `elastic_displacement`) and derived bands. 445 lines, position 27.
- **Status:** none in-file. It cites `canon/philosophy/07_drift.md` §7.1/§7.4 and RULINGS.md Batches 8 and 9, and says the old `threadwork_v30.md` Part 3 10→0 track is SUPERSEDED (ED-WR-0010) (:9-14). Reading: live, as an oracle.
- **Bears on:** WR, CHAR (the `(Person, coherence)` cell), FI (knots rupture), CORE.
- **Content that matters:**
  - Constants, all tagged `[JUSTIFIED]` and "invented, and licensed" (:92-139): `ELASTIC_RANGE = 6`, `HUMAN_BAND_LIMIT = 5`, band lows 2/4/6, `ELASTIC_RETURN_PER_SEASON = 6`, `RESTING_POINT_START = 0`. The file states the canonical orderings that are not invented (`ELASTIC_RANGE >= FRACTURED_LOW`, `DISSONANT_LOW <= HUMAN_BAND_LIMIT`, `HUMAN_BAND_LIMIT > RESTING_POINT_START`) and that `tests/valoria/test_coherence_elastic_plastic.py` asserts them (:97-105).
  - `apply_coherence_delta` takes a cost ≤ 0, adds it to the elastic stretch, and moves the excess over `ELASTIC_RANGE` into the resting point (permanent set) (:298-338). A positive delta raises `ValueError` (:322). `recover(...)` requires `environment_in_equilibrium` with no default, and never assigns the resting point (:341-377). `mend_resting_point` refuses past the crossing (:380-408). `check_coherence_failure_transition` is a once-only latch (:411-432).
  - `band`, `resting_band`, `present_displacement` and `crossed` are derived properties, not fields (:210-238). The old `from_dict` shape (no `resting_point`) is refused and not migrated (:264-272).
  - State store: `world.practitioners` when a world is passed, else module-level `_practitioner_state` (:141-151). The docstring says a World exposes `.practitioners`; `grep -rn practitioners engine --include=*.py` found no such field, so the module-level store is the only live one. [UNVERIFIED for `engine/autoload/`, which does not exist.]
  - Readers: `operations.py` imports `apply_coherence_delta`, `get_state`, `mend_resting_point`, `recover`; `systems/fieldwork/sim/knots.py:375` imports `apply_coherence_delta` for rupture; `tools/export_game_constants.py:69,155` cites `CoherenceState.band`. Tests: `test_coherence_elastic_plastic.py`, `test_threadwork_mending_parity.py`, `test_threadwork_resilience.py`.
  - No `engine/season` or `modules` file imports it (confirms F-WR-05, `09_WR_audit.md:276-291`).
- **Conflicts / stale:**
  - The header says no deplete-track and no sensitivity term; `CHAR` audit `02_CHAR_audit_addendum_B.md:209,681` records the Person `coherence` attribute as an orphan "marked unread at the loader", consistent with no carrier here.
  - `Dependencies: none` is correct, but the "Entry points" list omits `get_state` and `reset_all`.
  - R-14's resilience term lives in `operations.py`, not here, as the file says.
- **Open items:** the routing of post-crossing load (§7.5 reality strain) has no carrier. The R-14 arithmetic is unruled (shipped gain 0). `environment_in_equilibrium` has no producer in the season loop (callers pass a bool).

### systems/threadwork/sim/collective.py
- **What it is:** Collective (multi-practitioner) Thread operations per §2.5: an Anchor plus Helpers, a lattice, and a fracture rule. 229 lines.
- **Status:** none in-file. Reading: oracle-only; imported by tests only.
- **Bears on:** WR.
- **Content that matters:**
  - `attempt_collective_operation(actors, op_type, target, world, rng, environment_in_equilibrium)` ranks actors by `.ts`, the highest being Anchor (:71-110). Every actor makes an `attempt_leap`; if the Anchor fails there is no lattice (:121-128).
  - Pool: `total_pool = anchor_solo_pool + sum(floor(cognition/2))` over helpers whose Leap succeeded. `cognition` falls back to `.spirit`, defaulting to 3 (:62-68).
  - Fracture rule (:134-160): the first `lattice_fractured` expression at :140 is dead (overwritten at :160). The live rule is `total_pool < expected_pool / 2`, with `expected_pool = anchor_solo + all helpers' contributions`. A long self-argument comment (:141-158) records that the canon wording ("below half the Anchor's solo pool") can never fire as written. The file's own reading chosen instead is an interpretation that departs from the canon sentence it cites at :41-42.
  - Fracture adds `LATTICE_FRACTURE_OB_PENALTY = 1` to Ob (:43,175).
  - Coherence is charged to each successful Leap participant through `operations.charge_working` (R-14), and Mending is priced through the three shared owners (`mending_priced_scale`, `price_mending`, `apply_mending_feedback`) (:166-211). Own-configuration Mending aim raises `ValueError` (:108-111).
  - Readers: `tests/valoria/test_threadwork_mending_parity.py` only (grep). No game reader.
- **Conflicts / stale:** Dead first assignment of `lattice_fractured` at :140. A stale "Wait — re-read canon" stream-of-thought comment is left in the code (:141-158). The fracture condition uses `expected_pool/2`, contradicting the cited canon wording (:41-42). Cognition fallback to Spirit (`or 3`) is a duck-typed assumption (:12-15). The `import random as _r` inline (:179) duplicates the idiom in `operations.py` and `opposing.py`.
- **Open items:** the real fracture rule is an interpretation; it is not ruled.

### systems/threadwork/sim/operations.py
- **What it is:** Thread operations (Leap, Weaving, Pulling, Past-Pulling, Locking, Dissolution, Mending), the Three-Axis Ob tables, the R-14 resilience hook and the single Mending pricing owner. 611 lines.
- **Status:** none in-file (a header lists `canon source threadwork_v30.md Part 2` and `params/threadwork.md`). Reading: live as an oracle and the most-tested threadwork file; unreached by the game.
- **Bears on:** WR, DICE, CHAR.
- **Content that matters:**
  - `TN_STANDARD = 7` for every operation (:73); the PP-619 differential was superseded (ED-IN-0196, Jordan 2026-08-25). The file argues the old differential was inert, because `roll_pool` never read `tn`; only the reported `OperationResult.tn` changed (:57-64).
  - Hard-coded tables: `DEPTH_OB` Fibonacci 1/2/3/5/8/13 (:77), `MENDING_OB` (:87), `DEPTH_TS_MINIMUM` 30/30/50/50/70/90 (:95), `BREADTH_OB`, `DISTANCE_OB` (:105-119), `COHERENCE_COST_BY_SCALE` (:128), `FR_SURCHARGE = -1` (:140), and `LEAP_OB_TS_LOW/HIGH = 2/1` (:123-124).
  - Dead tables (grep over all `.py`, repo-wide, 0 other hits): `DEPTH_TS_MINIMUM`, `BREADTH_OB` and `DISTANCE_OB` are defined and read nowhere. The Leap eligibility check uses the literal 30 at :360 instead of `DEPTH_TS_MINIMUM`.
  - `_actor_pool = spirit*2 + 3 + ts//10` (:235-247). `.history` is no longer read (CR-85, ED-IN-0330). `.focus` is mentioned in the docstring and never read.
  - R-14: `RESILIENCE_GAIN = 0` is the shipped control and `RESILIENCE_GAIN_SWEEP = (0,1,3)` the swept fixture (:156-157). `resist_coherence_cost` returns the cost unchanged at gain 0, and `charge_working` is the one place a cost reaches `apply_coherence_delta` (:250-287). Test: `tests/valoria/test_threadwork_resilience.py`.
  - `_resolve_operation` applies a blanket -1 on Partial or Failure to everything except Mending (:321-323). The file itself says this "mis-hits Leap" (C-TW-3, left unfixed, :317-320). Locking and Dissolution report a flat `ms_delta = -1` (:335-336), which the file says diverges from the degree tables in the design doc. The P-25 scale term on Weaving/Pulling is a formula on `COHERENCE_COST_BY_SCALE` (:331-334), and the file says that reuse is "its own uncited choice".
  - Mending: priced by the owner trio (`mending_priced_scale`, `price_mending`, `apply_mending_feedback`) (:443-509). `attempt_mending` routes `target['configuration_of']` of `'self'` or the actor id to `mend_resting_point` via `RESTING_POINT_MEND_BY_DEGREE` (:168,512-611), and the file marks a `[GAP]` that nothing makes own-aim Mending difficult (:159-167).
  - Readers: tests (`engine/tests/test_thread_mending_ed871.py`, `tests/valoria/test_tn7_always.py`, `test_threadwork_mending_parity.py`, `test_threadwork_resilience.py`, `test_degree_ladder_single_owner.py`), `collective.py`, `opposing.py`. None under `engine/season` or `modules`.
- **Conflicts / stale:** The header lists `sim/autoload/dice_engine` and `sim/cross_scale/handoff_rules` (TS-banded coherence cost for mass battle) as dependencies; the actual import is `engine.dice_engine`, and `handoff_rules` is not imported (dead dependency note). `attempt_past_pulling` hard-codes a `pop_recency_ob` dict inline and a `max(-1, coh)` cap for Object/Personal scales (:406-412). Territorial appears in `COHERENCE_COST_BY_SCALE` but not in `DEPTH_OB`, so a Territorial target falls to `DEPTH_OB.get(scale, 1)`, Ob 1. `attempt_leap` returns `actor='unknown'` when `actor_id` is absent, ignoring `.name` (:362), unlike `_resolve_operation`.
- **Open items:** the R-14 arithmetic and the slot name for resilience (GO-01 / J-9) are unruled. The ladder for Mending Stability (steeper MS -1..-5 in the archived doc) is unruled. Leap's blanket -1 (C-TW-3) is unfixed. The own-aim Mending difficulty is open and carried in HANDOFF_WR.

### systems/threadwork/sim/opposing.py
- **What it is:** Opposing operations per §2.6, with a six-row resolution table, the engagement Ob modifier and the Knot Strain table. 269 lines.
- **Status:** none in-file. Reading: oracle-only; imported by tests only.
- **Bears on:** WR, FI (Knot Strain), SC (contested pools).
- **Content that matters:**
  - `opposing_engagement_modifier(tps) = max(1, tps//2)` (:79-84); each side's Ob is raised by the opponent's value (:138-155).
  - A hard-coded nine-branch `if/elif` over `{Meets, Partial, Failure}²` sets `outcome`, `ms_delta` and per-side consequences (:175-239). `ms_delta` is "scale cost as proxy" for canon's "A's degree-table MS cost +1" (:187). `Partial/Partial` draws `rng.randint(1,6)` and shifts one scale below on 1-2 (:212). The outcome is a string, with no effect applied.
  - Knot Strain constants (:54-60) become `knot_ob_penalty` and `composure` fields in the consequences. They are reported only: the writes to the fieldwork Knot store and the MS clock were struck at position 27 (:112-117). The only state written is each side's Coherence, through `charge_working`.
  - A Mending is re-priced per side by the owner (`price_mending` on the four-band label, :243-250), replacing the table's Coherence and MS values; own-aim raises `ValueError` (:133-136).
  - `_degree_label` folds Overwhelming and Success into 'Meets' (:87-99).
- **Conflicts / stale:** The "[ASSUMPTION: op_a and op_b are pre-resolved OperationResults…]" docstring (:17-21) does not match the signature, which takes raw actors. Table values hard-code `-1` and `0` where `COHERENCE_COST_BY_SCALE` exists. `ms_delta` for Meets/Meets is a flat `-1`. Neighbouring rows differ in whether `ms_delta` is clamped (`ms_delta if ms_delta < 0 else -1` vs `else 0`): rows 2 and 4 use -1; rows 3 and 7 use 0. [Not a defect finding, but the two clamps are inconsistent.] The "Dependencies" docstring says nothing outside threadwork is imported, but `engine.dice_engine` is (the point is "systems", not engine).
- **Open items:** the canon MS rule ("worst single degree-table MS cost +1") is approximated by the scale-cost proxy and is unruled.

### systems/threadwork/sim/threadcut.py
- **What it is:** Threadcut beings (P-06): a registry, observer perception bands, +1 Rendering Strain per external operation and the De-Actualisation rounds. 200 lines.
- **Status:** none in-file. The module records "§6.1 Ontological Status canon body is empty in the doc" (:13-14). Reading: oracle-only and unreached.
- **Bears on:** WR, CHAR (observer TS), PC (wounds).
- **Content that matters:**
  - Hard-coded `PERCEPTION_BANDS` by observer TS (10/30/50/70/101) (:37-43). `perception_band()` iterates it (:105-111).
  - Constants: `RENDERING_STRAIN_PER_EXTERNAL_OP = 1`, `DEACTUALISATION_R1_OB = 2`, `R2_OB = 4` (:47-56). The registry is module-level `_threadcut_registry` unless the world has a `threadcut_beings` attribute (:59-68). `grep` found no World field of that name, so the module-level store is the only live one.
  - `resolve_threadcut_interaction` triggers De-Actualisation when `rendering_strain >= health` (with `health = actor.max_wounds`, default 6) or `wounds >= max_wounds//2` (:164-185). Rounds advance 1 → 2 → 3, but the code stores the round and applies no Ob penalty anywhere. The R1/R2 Ob constants are used only in note strings.
  - `RENDERING_STRAIN_PER_BEYOND_SCENE` is defined and never used (:47).
  - The Mending-versus-threadcut Ob adjustment (TS/20, max +4) is described in a comment as "not applied here; caller invokes operations.attempt_mending with the adjusted Ob" (:189-193). Nothing in `operations.py` implements it.
  - Readers: none found by grep outside the file (`grep -rn threadcut` over `.py`, excluding the file and `.claude/worktrees`).
- **Conflicts / stale:** The Dependencies note says it depends on `operations`, but there is no import. "Health" is proxied by `max_wounds`, an acknowledged assumption (:17-19). The `deactualisation_round` field advances to 3 with no terminal effect.
- **Open items:** §6.1 canon is an empty heading. The beyond-observer-capacity strain is not implemented. The P-17 Mending Ob adjustment has no code home.

## Cross-subsystem leads

- **WR, CORE:** threadwork is a standalone oracle. No file under `engine/season` or `modules` imports it, and the practitioner, deck and threadcut stores are module-level fallbacks because no World field exists (`practitioners`, `comovement_deck`, `threadcut_beings`). This matches F-WR-05 and R-08 (`09_WR_audit.md:276-299,619`).
- **FI, WR:** the Knot Strain and Mending Stability outputs are reported and written nowhere. `fieldwork/sim/knots.py:375` still imports `apply_coherence_delta` for rupture. FI's "knot admits a witness" row (`08_FI_audit.md:742`) therefore depends on a threadwork write that is now the only one.
- **CHAR, WR:** `resilience` (R-14) is a duck-typed slot with gain 0. The CHAR audit marks Person `coherence` as an orphan "unread at the loader" (`02_CHAR_audit_addendum_B.md:209,681`). `_actor_pool` reads `.spirit`, `.ts`, never `.focus`.
- **DICE:** every threadwork roll goes through `engine.dice_engine.roll_pool` and `degree_label`. `TN_STANDARD` is reported only, and the file argues `roll_pool` never read `tn`. Three degree vocabularies appear: four-band (operations), three-label 'Meets/Partial/Failure' (opposing), and `Degree` enum.
- **SE, MB, FI, WR:** the geography file carries data for four subsystems (`poi_catalog` for FI, `radiation_bands`/`forgetting_zone` for WR, `march_budget`/`vision_range`/`terrain` for MB, `stats`/`starting_pros` for SE), but only `provinces`, `settlements`, `adjacency` and `terrain` have readers. See F-SE-06.
- **SE, WR (doubled fact):** `proximity_calamity` on T8 and T17 (value 4) versus `radiation_bands` band 5 (T8, T17). The Calamity distance lives in two places.
- **MB:** `modules/mass_battle/terrain.py` reads `terrain:` polygons from the geography file at module scope and names `terrain_cost_matrix` only in comments. The matrix is not the engine's cost.

## Likely stale or superseded

- `systems/threadwork/sim/__init__.py`: the `PROVISIONAL — Pass 2l armature stub` Status line.
- `systems/threadwork/__init__.py`: "design .md at root", which is false (the design doc is quarantined).
- `systems/social_contest/__init__.py` and `sim/__init__.py`: references to `designs/scene/`, `sim/personal/` and `tribunal` in `sim/personal/` (dissolved).
- `valoria_geography_v30.yaml`: the cross-reference block (:921-929) to `designs/…` paths, the dual `CANONICAL`/`PROVISIONAL` Status lines, the 55-vs-56 edge-count comments and the 60-hex-rows comment (:912-914).
- `co_movement.py`: the "18 cards" comment (:117) and the Dependencies note naming `sim/autoload/dice_engine`.
- `operations.py`: header dependencies on `sim/autoload/dice_engine` and `sim/cross_scale/handoff_rules`.
- `threadcut.py`: the "Dependencies: operations" line, with no import.

## Items that could change an audit finding

- **F-WR-05 / R-08 (`09_WR_audit.md`):** confirmed. The importer grep finds `systems.threadwork` only in tests, in `fieldwork/sim/knots.py` (rupture, a late import) and in `tools/export_game_constants.py` (a comment). Nothing under `engine/season` or `modules` imports it. Additional lead: all three state stores are module-level fallbacks, because no World field exists.
- **F-SE-06 (`07_SE_audit.md:309`):** confirmed and extended. Of the 16 top-level keys in the geography file (`meta` included), only `provinces`, `settlements`, `adjacency` and `terrain` are read by python outside tests. The audit's own ordered-work row 11 (the first reader for `settlement_adjacency`) stands.
- **Doubled fact (new, SE/WR):** the T8 and T17 `proximity_calamity: 4` versus `radiation_bands` band 5 disagreement was verified by script.
- **Hard-coded and dead tables inside threadwork (WR §hard-coded list, `09_WR_audit.md:880-884`):** `DEPTH_TS_MINIMUM`, `BREADTH_OB`, `DISTANCE_OB` are defined and not read in `operations.py` (Leap eligibility uses a literal 30). `RENDERING_STRAIN_PER_BEYOND_SCENE` and the De-Actualisation Ob penalties are never applied. `draw_comovement_card` has no caller. These could bear on any count of "tables the game reads".
- **Departure from canon wording:** the collective lattice fracture rule is implemented as `total < expected/2`, not the cited "below half the Anchor's solo pool", with the first formula left as dead code (`collective.py:140` vs `:160`). A WR finding that treats the §2.5 rule as implemented would need that caveat.
- **Position-27 structure:** `OperationResult.mending_stability_delta`, `OpposingResult.ms_delta`, `CoMovementCard.ms_delta` and the Knot-strain fields are reported and written nowhere, which supports the `09_WR_audit.md` claim that MS and Knot Strain have no season carrier.
