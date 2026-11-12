# Digest tests6

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane `tests6`: 77 files under `tests/valoria/` (alphabetical `test_combat_invariants.py` .. `test_wiring_validation.py`), read in assignment order, each to its end. `F-TEST-nn` ids are those of `proposals/2026-11-12-subsystem-audit-suite/audits/01_CORE_audit_addendum_C_tests.md` (read first; not repeated). Every file is a pytest file (no status line of its own; "Status" below is therefore "none stated" plus my reading). Line refs are `:line` in the named file.

### tests/valoria/test_combat_invariants.py
- **What it is:** pytest file, 1,656 lines, ED-PC-0035..0053 era; architecture-invariant guards for `modules/combat/` (single-source, no weapon-name table, vocabulary ownership, select_mode emergence, I2..I8 closing-distance redesign gates, plate-participation roster guard and its mutation meta-gate).
- **Status:** none stated; reading: live (the largest PC guard file). Heavy dated comment/docstring log (about 55% prose); several comments are re-baseline history, some contradict the assertion and say the assertion governs (:625-628).
- **Bears on:** PC, DICE (resolution pool), GO (typed Godot contract params).
- **Content that matters:**
  - Single-owner guards by AST scan with a stated blind spot: `resolution_pool` three scans (hardcoded clamp, borrowed `POOL_FLOOR`/`BASE_POOL`, bare-literal offset), `:164-222`; `Combatant.pool` must stay absent (`:245`); `core.PERC_AUTH_REF is WP.PERC_CAP` by identity plus an AST check (`:308-341`); `core.damage`/`strike_impact` may not divide by a bare 8.0 (`:344-373`). `CFG['ADEF_PERC_REF']` is deliberately NOT bound (config is a zero-import leaf and overridable), so `:320` holds it equal by value.
  - The blunt-heft branch test isolates its channel by asserting coupling is flat across `[PERC_AUTH_REF_SOFT, PERC_CAP]` first, then `checked >= 15` (`:376-413`): a good falsifier-with-precondition example (§0.1 pt 2).
  - `test_use_mode_selection_emerges_from_primitives` pins an exact ordered list of 14 weapons whose selected head changes with armour (`:670`); `test_jd9_grip_target_converges` pins five absolute g* values to 0.001 (`:895`) and reach anchors to 0.01 (`:876`). These are count/value pins that move on any physics recalibration (the comments record 5+ re-pins).
  - `test_reach_class_beats_arming_not_inverted` (slow) is a sampled win-share test (n=60, n=600 at heavy) with hardcoded crc32 seeds; many bands are one-sided floors (`>0.42`, `>0.5`, `<0.75`, `<=0.97`), and the comments admit the heavy cells decide about 6% of fights (`:1295-1482`). `test_plate_participation_tracks_armour_defeat_capability` derives membership from `AP.capability` (not listed) and asserts `len(clears)>=10 and marginal and len(under)>=28` first (`:1553`); the converse 40% ceiling was deleted by Jordan 2026-08-27 ("stop arbitrary fiat capping", `:1508`), report-only print remains (`:1585-1590`).
  - A mutation meta-gate (`:1593-1655`) patches `core.strike` to return 0 for declared weapon sets at plate and requires the participation guard to fail AND to name the zeroed weapons: the strongest control in the file. It runs n=24, slow-marked.
  - Source-text pins: `wrapper.py` marker order (`:1195-1221`), `src.count('opening_created=True') == 5` (`:1211`), a regex reader-exists scan for nine circumstance fields (`:1230-1243`); these observe text position, not behaviour. The reader scan matches `'field'` anywhere in three source files, so a docstring mention satisfies it.
  - Imports `armour_participation` and `structure_scan` from `systems/combat/combat_engine_v1/workbench/` via `LEFT` (:28, :54, :64): the test tree reaches a workbench outside `modules/`.
- **Conflicts / stale:** comments cite `designs/audit/2026-07-02-...plan_r1_RATIFIED.md` and `audit/2026-07-23-...wiring_audit_v1.md` (dissolved `designs/`, `audit/` paths; archived referents only). `LEFT` path `systems/combat/combat_engine_v1` is still consulted as a fallback location (`_engine_file`, :32-34) though CLAUDE.md §3 says `modules/combat/` is the live head [UNVERIFIED whether `LEFT` still exists]. Docstring at `:1627` of the participation guard says "806-test suite"; stale count in a comment only.
- **Open items:** the file itself names the known-open residual that the ranseur settles ~12% of plate fights (`:1524-1529`) and `PEN_DEFICIT_K` is the lever; "ED-PC-0012 sabre/scimitar" residual was resolved (:634-642).

### tests/valoria/test_combat_lapse.py
- **What it is:** pytest file, PC-19 / ED-IN-0347: Focus lapse term `LAPSE_K*consistency(defender)` in `mode_sigma`.
- **Status:** none stated; reading: live.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Docstring names its own falsifier: deleting the `sig += LAPSE_K*consistency` line reddens two tests; K=0 keeps the control tests green (`:5-7`).
  - Fresh reserve gives consistency exactly 0, a drained one negative (`:57-62`); at the shipped K the drained defender chooses the same mode with sigma lower by exactly `-K*consistency*cap` (`pytest.approx(abs=1e-12)` on a derived identity, `:77`, `:125`), and K=0 is bitwise the pre-item tree (`:83-95`).
  - Every loop ends in `assert checked == N` (4, 24, 12, 5): the conditional-assert-without-asserting-it-asserted failure is excluded throughout.
  - Monotone fall over eight hit counts (`:133-141`).
- **Conflicts / stale:** none.
- **Open items:** none.

### tests/valoria/test_combat_lever_sign_safety.py
- **What it is:** pytest file, PC-17 / ED-PC-0059 (2026-11-06) plus PC-18; sign-safety probes for seven GENERIC ability levers (visual, precommit, tactile, tempo, balance, edge_read, choke_control) at every consuming site; ~620 lines, 182 parametrized cases.
- **Status:** none stated; reading: live.
- **Bears on:** PC, CHAR (equipment/ability as capability data).
- **Content that matters:**
  - Property: investing in a generic ability never worsens its owner at levels 0..8, at each site (`:402-416`). Every signed-differential probe first asserts the owner is BEHIND against a mirrored reference (`:409-412`), so a sign-blind form would show as a worsening.
  - Anti-vacuity half: untaught (`tradition='none'`) exactly inert, taught moves, except the Agility1/Strength1 balance probes that must stay inert (`:419-431`); also coverage count `len(GENERICS)==21`, placement Latin square (7 traditions x 3 levers) (`:394-399`, `:526-546`).
  - The header records a mutation run (inverted factors at ~15 sites, tradition gate deleted: 76 failed) with counts; this is the documented control, not re-run by the test.
  - Cross-lever: the edge_read refined tier was REVISED to x1.40 (from plan x1.50) because at 1.50 a single generic floors legibility (`:468-494`); stacked generics are floored at 0 and the test asserts the unfloored value is negative first (`:505-523`).
  - PC-18: `reading(c)` is `c.att` alone (cog removed; `Combatant(cog=5)` raises TypeError, `:559-576`); the attack's suddenness adds `AGI_READ_K*(agi-NEUTRAL['agi'])` inside the visual factor, placement verified with an invested lever (`:584-618`). `approx(abs=1e-12)` is on a derived identity, not an exactness claim.
- **Conflicts / stale:** none found.
- **Open items:** the header says the counter_select probe measures selection frequency, not benefit; the benefit was measured once by duel (ED-PC-0059), not in the test.

### tests/valoria/test_combat_pob_bands.py
- **What it is:** pytest file, U1/JD-1/ED-PC-0010 (2026-07-08): derived point-of-balance bands and unchanged total mass for named weapon classes.
- **Status:** none stated; reading: live.
- **Bears on:** PC.
- **Content that matters:**
  - Eight weapons asserted inside ratified cm bands (rapier 3-11, 1H 6-14, greatsword 8-20, poleaxe class 20-55, staff ~0) via `WP.derive(...)['PoB_cm']` (`:16-42`); violations dict reported.
  - Mass-unchanged check is a six-weapon hardcoded literal table of masses to 1e-9 (`:48-52`): pins data, not behaviour; it is a record that the weapon table was not edited.
- **Conflicts / stale:** cites `designs/audit/...consolidation_v1.md` §6 (dissolved path).
- **Open items:** weapons outside the five named classes have no band by design.

### tests/valoria/test_combat_ob_from_defender_consumers.py
- **What it is:** pytest file, PC-03 / ED-PC-0058 critique: three readers of the per-defender Ob (workbench probability bands, `core.strike` overwhelming-quality tail, the single-channel claim for faculty).
- **Status:** none stated; reading: live. Docstring flags the CR-85 design as UNRATIFIED (ED-IN-0351), an `[ASSUMPTION; medium; Jordan to correct]` (:18-22).
- **Bears on:** PC, DICE (Ob ladder, `degree_from_net`).
- **Content that matters:**
  - Falsifier is stated and structural: workbench `P.node_distribution` vs `core.resolve` frequencies over 20,000 seeded rolls at 5 binomial SE per band, `checked == 12` (:59-81). Statistical but the seeds are fixed (`range(n)`), so deterministic; the tolerance is not a fudge on an exactness claim.
  - Trace-event test requires `rolls >= 50 and stophits >= 1` (:102), so it asserts it asserted; it sets module global `wrapper._TRACE` and restores it in `finally`.
  - Overwhelming-quality test uses a test-local bisection for the owner bar (independent of core's helper, :123-134), parametrised over five faculties, with `nextafter` edge checks both sides, and exact equality to `1.5 + (OW_MAX-1.5)*tanh(z/OW_Z)` (:164): a constant duplicated from `core` in the test (`1.5`).
  - `test_faculty_enters_the_roll_through_exactly_one_channel` is the CR-85 conversion of a strict xfail: Ob moves by exactly 1.0 for faculty 3 to 5 and no net-sigma term moves for parry/dodge/wind; bind and counter probabilities equal (:195-215). `set_attr('faculty', 7)` reads pool 13, Ob 3.5 (:218-226): the faculty-to-Ob ladder is `faculty/2`, pool `faculty+6`.
- **Conflicts / stale:** line 33 adds `systems/combat/combat_engine_v1/workbench` to `sys.path` ("stayed at plan position 31b"); `systems/combat/` still holds that directory, so it resolves today. Cites `DECISIVE_OB = 3` as retired.
- **Open items:** CR-85 (faculty rename, deletion of History from sigma) is stated UNRATIFIED while the code and the test already encode it.

### tests/valoria/test_combat_reversed_grip.py
- **What it is:** pytest file, U2 partial / ED-PC-0009 (2026-07-08): `thrust_factor` floor drop (JD-9) and `reversed_grip_percussion` (JD-4, Mordhau).
- **Status:** none stated; reading: live but thin.
- **Bears on:** PC.
- **Content that matters:**
  - Mace/staff thrust below 0.05; needle-class cut below 0.10, mace/staff cut exactly 0.0 (:23-44): threshold pins on derived geometry.
  - `test_thrust_factor_is_wired` checks `afforded_heads(w)['cut_thrust'][0] == max(cut, thrust)` to 1e-9 for four swords (:47-62): the formula equals itself recomputed, a duplication of the production expression in the test.
  - Two-handed swords' reversed-grip percussion is nonzero and below 2.5 and below 0.35 of mace/poleaxe (:65-76); 1H weapons give exactly 0.0 (:79-85).
  - `test_reversed_grip_percussion_uses_hilt_mass_not_whole_weapon` (:88-96) does NOT observe hilt mass: it asserts a rapier's hilt fraction is above 0.5 and that a rapier's reversed-grip value is 0.0, which the `hands==2` gate alone produces. The test name claims a bottom-up property its body cannot see (§0.1 pt 2).
- **Conflicts / stale:** the module docstring says the formulas are NOT wired into `element_afforded`'s live selection (:7-11); `test_combat_invariants.py:696-704` and `test_combat_tradition_levers` show later work (U2/ED-PC-0011) wired graded secondary affordances, so that docstring is probably stale [UNVERIFIED]. The dissolved citation `designs/...` appears via sourcing text only.
- **Open items:** none stated.

### tests/valoria/test_combat_strength_jobs.py
- **What it is:** pytest file, PC-20 / ED-IN-0347 (AR-10, AR-12, AR-13): four Strength jobs in personal combat (damage by head, weapon mass in demand, armour demand paid in stamina, arrest of own swing).
- **Status:** none stated; reading: live; the best-controlled file of this lane.
- **Bears on:** PC, CHAR (Strength as a capability axis feeding levers).
- **Content that matters:**
  - Each of four jobs names its own falsifier (the deleted term) and its control (coefficient at 1.0 or 0), and has a "pre-item bitwise" control test (`test_all_ones_is_the_pre_item_impact`, `test_d_mass_zero_is_the_pre_item_demand`, `test_armour_demand_zero_is_the_pre_item_cost`, `test_arrest_k_zero_is_the_pre_item_recoverability`) with `checked == N` after each loop.
  - Slope ordering blunt > every edge head > point holds at 12 heft/Strength combinations and additively (:75-95); `K_STR_HEAD` keys equal `V.HEADS` (:69-72).
  - A fixture (`heavy_twin`) creates a heavier weapon of equal derived inertia and asserts the premise (equal `wield_heft`, `handling`, `reach_base`, `rear_clearance`) before testing (:136-149): the roster's mass field matters only through `D_MASS`.
  - Armour: fighter below the tier's demand pays `COST_SCALE*ACT_WEIGHT/D_WT*(demand-s)` more stamina per act, at-or-over pays identical (:216-234); `ARMOR_DEMAND` rises with tier and heavy demand is at most 7 (:205-213); a Strength-1 fighter in plate empties in fewer acts, a Strength-7 in the same number (:237-249).
  - `approx(abs=1e-12)` and `rel=1e-9` used only on derived-expression identities (:85-86, :166, :186, :229, :343), not on an exactness claim.
- **Conflicts / stale:** none found. This is the same kit/penalty mechanism as the individual loadout weight penalty the brief asks MB to share (fatigue and speed from carried kit): here per-weapon `D_MASS*mass` and per-armour `ARMOR_DEMAND` are cfg constants in `config.CFG`, not data on the weapon record.
- **Open items:** none.

### tests/valoria/test_combat_tradition_levers.py
- **What it is:** pytest file, U10 / ED-PC-0022 (2026-07, re-baselined ED-PC-0034/0058): tradition-ability modulation of morphology levers.
- **Status:** none stated; reading: live.
- **Bears on:** PC, CHAR (techniques/abilities as capability data), DICE.
- **Content that matters:**
  - Lever surface is inert by default (factor 1.0 for five channels, :37-42); every ability's lever must be in a closed live set of 15 channel names (:45-64); shinogi->spine_press, ringen_am_schwert->edge_grab, zwerchhau->counter_select, atajo->leverage, `guardia` absent.
  - Per-event effects are tested directly (shinogi raises `bind_sigma` on a katana, no effect on a spineless arming sword :226-232; ringen raises `grab_sigma`): deterministic, no aggregate claim, after an ED-PC-0023 review found the earlier aggregate "+2.8pp edge" was a confound (:72-76).
  - `test_levers_add_texture_without_shifting_balance` runs 400 seeded fights x 2 pairings with levers on vs off and asserts at least 2% of fights diverge in event signature and at most 20% flip the winner (:153-163); the docstring records the true rate halved (12-13% to 5-8%) after Ob-from-defender, and the floor was lowered twice. Bounds are generous by design; it can observe dead levers (reads 0).
  - Level semantics: list equals dict level 1.0, level 0 inert, amplifier monotone up, mitigator monotone down in (0,1], additive path scales with level (:166-188); investment capped at `MAX_INVESTMENT_LEVEL`, factor bounded `[ABIL_FACTOR_FLOOR, ABIL_FACTOR_CEIL]`, an extreme-investment fight resolves with no `OverflowError` (:191-213); tradition gate: a german fighter equipping japanese `shinogi` gets 1.0, cross-training via `known_traditions` works, traditionless equip is inert (:235-250).
- **Conflicts / stale:** imports `trace.run_traced_fight` from `systems/combat/combat_engine_v1/workbench` by `sys.path.insert` and the name `trace` shadows the stdlib module (:137-138). Cites `audit/2026-07-04-weapon-morphology-granularity/u10_activation_v1.md` (dissolved path). Header says edge_read/choke_control carry only PC-17 GENERIC abilities, consistent with the sign-safety file.
- **Open items:** `facing_regime` is a BARE lever with no authored ability, "awaiting grounded content" (:49-51).

### tests/valoria/test_combat_units_refactor.py
- **What it is:** pytest file, U0 / ED-PC-0002: weapon lengths converted to honest metres; compares ~60 derived quantities per weapon with `tests/valoria/r3_identity_golden.json` at 1e-9.
- **Status:** none stated; reading: live; a golden pin of data that "NEVER" may be hand-edited, by its own docstring.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - The golden covers the full roster: `set(golden) == set(C.WEAPONS)` (:55); golden has 54 weapons (checked), the docstring and test text say "53-weapon roster" (:51): the number is stale prose, the assertion is by set equality.
  - The golden has no generator; it has been hand-edited twice (PC-11 removed a key, PC-20 (2) recomputed `systems[*].str_demand` with the live code after a D_MASS-0 control, :13-17). So the pin is partly self-referential: part of it was produced by the code it now checks.
  - Collects `errs` and asserts empty with first 10 printed; no `checked` count, but the set-equality assertion guarantees a non-empty loop.
  - `UNIT_M` must not exist; rapier overall 1.14 m and spear 2.01 m (`math.isclose` abs_tol 1e-9, :134-135).
- **Conflicts / stale:** the "53" in the docstring versus 54 in the fixture [verified by loading the JSON]. The test bears on §5 (never take a number out of prose): the golden is a JSON read by tests only, not by the engine.
- **Open items:** "a deliberate re-baseline increment regenerates it" but no generator is named.

### tests/valoria/test_combat_yield.py
- **What it is:** pytest file, PC-01 / ED-PC-0056: Yield as a declaration on `wrapper.fight`, no fourth band.
- **Status:** none stated; reading: live; strong.
- **Bears on:** PC, CORE (seam: `engine.season.seam.wrappers.combat.surrender_of`, `seam.ladder.combat_degree`, `data.rosters.COMBAT_BANDS`), SC (surrender/capture).
- **Content that matters:**
  - Falsifier (a): a planted yield at turn 1..3 by A or B ends the exchange with exactly `turn-1` bouts, nothing but `fight_result` after the yield event, and the RNG draw count (via `valoria._draw_stream.RecordingRandom`, which counts `gauss` as well) is unchanged after the declaration and below the control's; the pre-yield trace equals the control's draw for draw (:63-84).
  - Falsifier (b): a yield while the objective is contested is refused and the fight is the control's bout for bout and draw for draw (:119-129).
  - `accepted=False` (opponent declines) ends the fight identically to accepted; the engine has no free-strike resolver, "the opponent's disposition is the caller's, carried on the yield event" (:95-106). `surrender_of(trace)` returns `{by, turn, accepted}` (:104).
  - A yielder is read by the existing three combat bands as `Untouched`/`Wounded`, never `Felled`; `len(COMBAT_BANDS) == 3` (:132-144). Invalid yields (non-combatant, turn 0, turn > max_bouts, string `by`) raise ValueError (:109-116).
  - `_seed_lasting(min_bouts)` finds a qualifying seed rather than assuming one (:54-60).
- **Conflicts / stale:** none. Note the design point: "refused" has two meanings (objective contested = engine refusal; `accepted=False` = caller's disposition) and both are visible only on the trace.
- **Open items:** no resolver for the consequence of a refused yield (a free strike) exists in the combat module by design.

### tests/valoria/test_conditional_orders.py
- **What it is:** pytest file, 2026-07-23 Jordan directive and ED-MB-0030: conditional stance/withdraw orders on the mass-battle `Order` primitive (`enemy_range:D`, `own_strength:F`).
- **Status:** none stated; reading: live; the only direct tests of the standing-order surface the brief asks MB to judge (Ogre Battle / Unicorn Overlord style "priorities set in advance").
- **Bears on:** MB (orders, retreat conditions), PC (none).
- **Content that matters:**
  - Trigger names validate at construction (`enemy_rnge:5` and `own_strenght:0.5` raise ValueError, :41-46, :78-82); `behavior` may set `stance` and `yielding` (:48-51).
  - Behaviour is run through `systems.mass_battle.sim.engine.resolve_battle` (the sim oracle, not `modules/mass_battle`) with a global `random.seed(...)`: an advancing line flips to `stance='retreat'`, `yielding=True` once the enemy is within 5 cells (`_order_idx == 1`, :54-63); a 0.5-cell trigger never fires (control, :66-75); `own_strength:0.9` fires after attrition (:85-98).
  - Only one test imports the shipped module: `modules.mass_battle.core.contact.check_orders` for the no-fire-at-full-strength arm (:104-110). So the order tests run on the `systems/` sim engine and one on `modules/`: two engines for one primitive [UNVERIFIED whether `systems.mass_battle.sim.engine` re-exports `modules`].
  - The fire tests assert end-of-battle state only (`_order_idx`), not the tick it fired, so "fires when the enemy closes" is observed as "fired some time in 40 turns" with a fixed seed.
- **Conflicts / stale:** `_SIM` path points at `tests/sim` (a directory CLAUDE.md §3 calls unrelated to the retired `sim/`); `systems/mass_battle/sim/` exists. Docstring says "No new engine mechanism".
- **Open items:** no trigger for morale, supply, flank exposure or ammunition exists in the tested set (only two triggers are tested).

### tests/valoria/test_conviction_roster_single_owner.py
- **What it is:** pytest file: the pursuit (ex-Conviction) roster has one owner (`references/descriptor_registry.yaml:pursuit_roster`, read as `engine.substrate.descriptors.PURSUITS`), and a source walk fails on a second roster.
- **Status:** none stated; reading: live; a recurrence guard that carries its own §0.1 pt 5 predicate and passes it (game code, defect was real).
- **Bears on:** CHAR (pursuits/convictions), CORE (registry owner), PROCESS.
- **Content that matters:**
  - `len(descriptors.PURSUITS) == 15` (:64): a count pin, re-pinned 13 to 15 at IN-08 (ED-IN-0261's fifteen pursuits). `conviction.CONVICTIONS is descriptors.PURSUITS` and `rosters.PURSUITS is descriptors.PURSUITS` by identity (:72-73).
  - AST walk over `engine/` plus `ci_common.MODULE_CODE_DIRS`: any Tuple/List/Set/Dict literal holding 2 or more canonical names fails (dict keys AND values inspected, :98-109). Floors: `len(walked) >= 100` and a named non-engine witness file `systems/characters/sim/conviction.py` must be walked (:113-115): the derived roots cannot silently drop a tree.
  - Twenty legacy names (`Justice, Survival, ... Scholastic, faith, warden`) raise `ValueError` in `resolve_pursuit`, no `CONVICTION_ALIASES` attribute may exist; legacy tags migrate per character, not by alias (:124-148).
  - The control is the docstring's stated mutation (re-hardcode two names, "Mutation-verified 2026-08-24"): not re-run by the test; the floors are the in-test observation.
- **Conflicts / stale:** the module still uses the word "Conviction" for the roster (deliberately, stated). It reads `systems/characters/sim/conviction.py`, which still exists as the named witness.
- **Open items:** none.

### tests/valoria/test_definitions_store.py
- **What it is:** pytest file for `tools/definitions_store.py` (the unified definitional surface, ED-IN-0077): store equals a fresh rebuild and equals the union of `names_index` and `descriptor_registry`.
- **Status:** none stated; reading: live but its subject is a process/definition store.
- **Bears on:** PROCESS, CORE (names registry).
- **Content that matters:**
  - `ds.check()` returns `(ok, msgs)`; the store is UNTRACKED (ED-IN-0194, culling wave 5) and written by the `generated_layer` conftest fixture, so "store is current" is now determinism, not staleness (:20-26). The set-identity with the union of the two registers and the name-field parity on overlapping keys (:29-43) are the real content.
  - The overlap loop (`for key in set(names) & set(desc)`) has no count and no check that the overlap is non-empty (:41): a loop that asserts only if the overlap exists (conditional-assert-without-asserting-it-asserted). The addendum's `valoria · CORE` loops row covers this pattern in aggregate.
  - `test_every_definition_has_a_canonical` likewise loops with no population floor (:46-48), though the set-identity test beside it implies non-empty if `names_index` is.
- **Conflicts / stale:** none.
- **Open items:** none.

### tests/valoria/test_degree_boundary_epsilon.py
- **What it is:** pytest file, ED-MB-0051 / plan v2 A2: a 1-ulp float error must not move a mass-battle damage degree; `compute_degree` epsilon and the sigma-zero snap.
- **Status:** none stated; reading: live; a strong falsifier-aware file.
- **Bears on:** MB, DICE (degree ladder in mass battle: Failure/Partial/Success/Overwhelming at margins 0, 1, 3).
- **Content that matters:**
  - Uses `math.nextafter` at every boundary because the v1 guard (`ob - 1e-16`) equals `ob` in float64 for ob 3 and 6 and "could not fail"; the file proves that in-suite (`test_guard_is_not_vacuous...`, :168-180): exemplary §0.1 pt 2.
  - The ruled MB ladder (2026-08-14): margin `net - ob` below 0 is Failure, 0 to <1 Partial, 1 to <3 Success, 3 or more Overwhelming, each boundary with an ulp-below case at ob in (1, 3, 6, 9) (:66-100). `_DEGREE_EPS == 1e-9` is pinned (:134) and `_SIGMA_ZERO_SNAP < _DEGREE_EPS` (:158).
  - Ceiling test: a net `1000*eps` below each boundary must still demote to the adjacent lower band, so the epsilon cannot become a balance change (:126-148). Symmetry test: dust above the Partial boundary is not promoted (:103-123).
  - Imports `modules.mass_battle.resolution.compute_degree`, `_sigma_net_boost`, private constants `_DEGREE_EPS`, `_SIGMA_ZERO_SNAP`: the test pins private names.
- **Conflicts / stale:** `compute_degree` in MB is a separate implementation of the ladder from `engine.dice_engine.dice_engine.degree_from_net` which PC consumes (see `test_combat_ob_from_defender_consumers.py:131`) and the next file tests (`test_degree_ladder_single_owner.py`) [UNVERIFIED whether MB's `compute_degree` delegates; the SC/MB/PC three-ladder question belongs to the next entry].
- **Open items:** none.

### tests/valoria/test_degree_ladder_single_owner.py
- **What it is:** pytest file, ED-IN-0187 sweep, 478 lines (about 60% comment): one degree ladder for the whole game; enrolls each ladder and evaluates it cell-for-cell against `engine.dice_engine.dice_engine.degree_from_net` over three domains (about 600 integer cells, about 890 quarter-net cells, about 1,780 half-integer-Ob cells), plus a source sweep for a new hand-rolled ladder.
- **Status:** none stated; reading: live. Several comments are corrections of earlier comments and say so ("a claim about a data structure that a targeted string edit never forces anyone to re-read", :174-283, :406-416); one comment states `HELD` is empty so the divergence test "asserts nothing" (:274-284).
- **Bears on:** DICE, MB, PC, SC, FA (threadwork), PROCESS.
- **Content that matters:**
  - Enrolled ladders: owner; `systems/threadwork/sim/operations.py`; `modules/mass_battle/resolution.py`; `skills/valoria-dice-model/valoria_dice.py`; `systems/social_contest/sim/contest/degree_extension.py` (pool-less form); `modules/combat/core.py` (:154-172). The MB ladder is SPELLED OUT, not imported, in `modules/mass_battle/resolution.py:104-120` (verified by grep: three `if margin` branches with `_DEGREE_EPS`), its docstring naming this test as the only link: a second implementation of the ruled ladder, held equal by measurement (:116-130, :376-381).
  - `test_every_ladder_is_behaviourally_the_owner` carries floors `len(LADDERS) >= 5`, `len(DOMAIN) >= 1000`, and checks that the domain has fractional nets and fractional obstacles (:334-339); it deleted its own arithmetically-forced `checked == ...` assertion as vacuous (:324-331).
  - `test_the_held_site_still_diverges` loops over `HELD = {}` and asserts nothing: a standing no-op test (:284-300).
  - `test_three_band_shorthand_is_a_declared_fold_not_a_ladder`: threadwork `opposing._degree_label` equals the owner's four bands folded to three (Meets/Partial/Failure), over the whole domain (:346-357).
  - `test_no_new_hand_rolled_ladder` is a regex sweep over `engine, MODULE_CODE_DIRS, skills, tools, tests` for files that PRODUCE two or more distinct band literals, with a registry of owners/adapters/frozen oracles and floors `scanned >= 100` and `'systems' in roots_seen` (:451-477). The `_FROZEN_ORACLE` entries name five `tests/sim/v32-combat-balance/*.py` files that carry the old `2*Ob` ladder on purpose (:364-368, :397-401).
  - A `RULINGS` dict (:185-269) records Jordan's verbatim rulings in a test module: the margin ladder (2026-08-14); "systems should not need different degree bands ... the wrapper needs to inject the engine in such a manner that it can be modified cleanly" (2026-08-15; executed as `dice_engine.BandExtension`); "DECISIVE_OB for combat is stupid as hell ... Ob should be determined by your opponent" (2026-08-15, executed ED-PC-0058 / PC-02); "yes accept. if you don't have enough dice you don't have enough dice" (a pool-2 contest can never resolve Overwhelming, 2026-08-27, SETTLED); "stop arbitrary fiat capping" (2026-08-27); "one faction write mechanism" (ED-FA-0038); "key contracts and module contracts etc need to be explicitly defined in a centralized hierarchical manner" (ED-IN-0200, RULED NOT EXECUTED). `RULINGS` is read by no assertion: it is prose-in-code that the file's own §0.05 reading makes reference, not mechanism.
- **Conflicts / stale:** `RULINGS` cites `tests/valoria/test_faction_write_sweep.py` as the guard for "one faction write mechanism"; no such file exists (Glob: none) and the faction block was deleted at plan position 29b, so the cited guard is gone [verified]. The mass-battle ladder is not the single "ONE" implementation the docstring claims for the bands: `modules/mass_battle/resolution.py` keeps its own copy (`:104`). Docstring cites `audit/2026-08-12-degree-vocabulary-census/` (archived). Paths `tests/sim/mass_battle/` are stale (the engine moved to `modules/mass_battle/`).
- **Open items:** the SC ladder keeps a "declared extension" (pool-aware Overwhelming bar) that is off the tested two-argument domain; its contract lives in `engine/tests/test_sigma_leverage_parity.py::TestPoolAwareDegree` (the addendum marks the kernel for retirement under `05_SC_sc05_kernel_retirement.md`). The "centralized hierarchical contracts" ruling is recorded here as unexecuted.

### tests/valoria/test_deployment_primitives.py
- **What it is:** pytest file, ED-MB-0025/0026: explicit subunit deployment primitives (density bounds cell count, depth distribution gradient, explicit width x depth) and the `build_envelopment` / `build_refused_flank` explicit-placement fixes.
- **Status:** none stated; reading: live; one of the few direct tests of the "unit = formation on a cell grid with its own troops" structure the brief asks MB to judge.
- **Bears on:** MB (geometry, hierarchy, cell grid, formation shapes).
- **Content that matters:**
  - `footprint_for(shape, troops, density, None)` bounds troops-per-cell within 40..200 for troops in (133, 200, 400, 1200) and density in (40, 50, 67, 100); 133 troops at 40/cell spans at least 3 cells (:15-25); lower density means more cells (:28-32); shapes `Line`, `Arrowhead`, `GappedLine`, `Column` build 6..10 cells at 400 troops, density 50 (:35-39). The 40/200 bounds (`CELL_FLOOR`, `CELL_CAP`) are hardcoded in the test.
  - `Subunit(... distribution='front'|'rear'|'uniform')` conserves troops within 1e-6 and shifts density between ranks (:42-59). Width x depth fixes exact cell count (8x2 and 2x8 both 16, :117-125), and the spec path `build_army` forwards `width`, `depth`, `distribution` (:128-144).
  - `build_envelopment`: wings straddle an explicitly placed centre; explicit wing columns are kept (2 and 20); `build_refused_flank` echelons the refused wing back near the strong wing (:62-114). These test the army-builder helpers in `systems.mass_battle.sim.engine`, not `modules/mass_battle`.
  - Hierarchy observed: a `Subunit` carries `cell_troops`, `shape`, `troop_type`, `tier`, `starting_position`, `distribution`: the army-to-unit-to-subunit-to-cells nesting is real in the data model at build time; the file does not test whether resolution reads it per level.
- **Conflicts / stale:** `build_army` imported from `systems.mass_battle.sim.engine` while `Subunit` and `footprint_for` come from `modules.mass_battle` [UNVERIFIED how the two relate]. Unused `import os, sys`.
- **Open items:** no loadout (primary/secondary weapon) key appears in any spec here; troop type is a single string, which bears on the brief's mixed-weapons question.

### tests/valoria/test_descriptor_registry.py
- **What it is:** pytest file, W1.13, revived 2026-07-08 (OPT-AV-7), re-pinned at CR-84 (ED-IN-0328): the descriptor registry loads, the ten attributes, alias preservation.
- **Status:** none stated; reading: live.
- **Bears on:** CHAR (attribute roster), CORE (registry).
- **Content that matters:**
  - The ten attributes in order: body strength, endurance, agility; mind focus, acuity, will, perception; social attunement, charisma, grace (3/4/3 by category, :29-33, :55-57). Aliases resolve case-insensitively (Spirit to will, Cognition/Reason to acuity, Presence to charisma, Vitality to endurance, Dexterity/Coordination to agility, :60-72). `Recall` retired and unresolvable (:75). `Bonds`, `Sincerity`, `Affability` resolve to `attr.social.bonds` with `deprecated: True` (:119-127). Composure and Resolve are derived values, not attributes (:130-137).
  - Alias preservation is a function `_lost(reg)` run both on the real registry and on a planted copy (Dexterity dropped; Charisma retargeted) which must name exactly that loss (:93-108): a planted control for the assertion.
  - Uniqueness of every name/alias/key across the roster (:140-147).
  - The registry is opened with a CWD-relative path (`open('references/descriptor_registry.yaml')`, :37, :101), so the file passes only when run from the repo root.
- **Conflicts / stale:** the docstring's path `tests/registry/test_descriptor_registry.py` (:1) is old. The combat files use attribute names `att`, `agi`, `strength`, `faculty` (`test_combat_lever_sign_safety.py:79-81`); the mapping from the ten registry keys to those combat inputs is not tested here.
- **Open items:** none.

### tests/valoria/test_descriptor_registry_category_b.py
- **What it is:** pytest file, W3 item 4 / OI-30a / ED-IN-0059 / ED-IN-0096: known-answer parse test for the eight "Category-B" scalar registrations in `references/descriptor_registry.yaml`.
- **Status:** none stated; reading: live but weak; guards a registration list, not behaviour.
- **Bears on:** CORE (registry), CHAR/FA/SE/WR (the eight scalars span personal, province, settlement, clock, faction).
- **Content that matters:**
  - Exactly eight entries with keys `pc.wounds, pc.poise, pc.initiative, prov.turmoil, set.accord, clock.season_counter, fac.coup_posture, fac.succession_status`, one kind `personal_track`, and eight pinned names (:31-54): a count and set pin on a registry listing.
  - `source` of each entry must contain `module_contracts.yaml` (:57-61); `personal_track` must appear in the first 2000 bytes and `# KIND:` exactly once there (:64-74), a text-position pin because "no code enforces" the KIND enum (:65-67).
  - `test_category_b_note_flags_registrations_not_schema_bindings` ends with `section_comment_present = True; assert section_comment_present` (:81-82): an assertion that cannot fail. It asserts only that `note` is non-empty.
- **Conflicts / stale:** the faction rows (`fac.coup_posture`, `fac.succession_status`) are in `category_b_scalars` while `test_descriptors_runtime.py:8` says the `fac.*` registry block was deleted at plan position 29b [UNVERIFIED whether category_b rows survive that deletion; the test is presumably green].
- **Open items:** "C2 stays out of scope (fork 11, J)" (:35).

### tests/valoria/test_descriptors_runtime.py
- **What it is:** pytest file: the engine reads the cooked `engine/engine_params/descriptors.json`, not the YAML; the ten-attribute sentinel; the ratified-but-unimplemented register.
- **Status:** none stated; reading: live, with two tautological assertions.
- **Bears on:** CORE, CHAR.
- **Content that matters:**
  - Source-text test: `engine/substrate/descriptors.py` source contains `descriptors.json` and, after the docstring (`split('"""')[2]`), not `descriptor_registry.yaml` (:23-28): observes text, fragile to docstring layout.
  - `len(descriptors.ATTRIBUTES) == 10`, `ATTRIBUTES_PENDING_TENTH is None`, `attr.mind.perception` and `attr.social.grace` present, `attr.social.bonds` absent (:31-38); the falsifier test feeds the exporter a nine-attribute registry via monkeypatch and requires `count == 9` and the sentinel (:41-55).
  - `EXPECTED_UNIMPLEMENTED = set()` and `unimpl` from `descriptors.json['unimplemented']` must equal it (:72-99); every present row needs `needs` and `why_it_matters`. The register is EMPTY, so the loop at :97-99 iterates nothing. `test_the_unimplemented_register_guard_can_observe_an_unauthorised_deletion` asserts `{'faction_L'} != set()` and two similar inequalities (:102-114): constant comparisons that cannot fail on any code change.
  - `tools/export_descriptors.py --check` returns 0 (:117-121): a round-trip check for the exporter (a kept pattern under §0.1).
  - Prose records that `fac.intel`, `faction_L`, `per_stat_floors` rows left the register by deletion of `game_state.py`, `Faction` and the `fac.*` block at plan position 29b (:66-71); "An empty register is ... not evidence the register is complete".
- **Conflicts / stale:** docstring says "same discipline as keys.py vs key_types.json" (:24); the Key substrate is RETIRED (ED-IN-0232) and `keys.py` is gone; the reference is to a retired thing, in a docstring only.
- **Open items:** the file itself says nothing catches a ratified item that never reaches the `unimplemented` block.

### tests/valoria/test_design_prose_quarantine.py
- **What it is:** pytest file, ED-IN-0231 (Jordan 2026-09-16): the game trees hold no markdown; `.designs/` is hidden and every archived doc carries a banner.
- **Status:** none stated; reading: live; subject is process (the quarantine), kept as the named falsifier of `tools/ci_design_prose_quarantine.py`.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Falsifier for the gate: monkeypatches `_tracked_md` to return a markdown path under `systems/combat/` or `modules/x/` and requires `offenders()` to report it (:33-40); `engine/season/` is exempt, other `engine/` markdown is not (:43-48).
  - `gate.ARCHIVE.startswith('.')` and `.designs/` exists (:51-57); `test_archived_documents_announce_themselves` requires at least 230 `.designs/**/*.md` and each to start with `<!-- ARCHIVED-NOT-CANON -->` (:60-71) (found 231 on disk by `find`, so the floor sits 1 below the live count).
  - `pathres.resolve('systems/mass_battle/reference/mass_battle_v30.md')` must be `ALIASED` into `.designs/` (:74-79); the CLI returns 0 (:82-87).
- **Conflicts / stale:** none. This reads `.designs/` (allowed: it asserts banners, loads no content into the game).
- **Open items:** none.

### tests/valoria/test_dg2_yield_residuals.py
- **What it is:** pytest file, ED-MB-0024 (proposals/mass_battle_fighting_withdrawal_v1.md): the three deferred fighting-withdrawal residuals: emergent auto-entry into yielding (§2.2), rally exit and pocket exit (§2.4).
- **Status:** none stated; reading: live; the docstring's claim "All three are GATED OFF by default" is STALE.
- **Bears on:** MB (yield/fighting withdrawal, morale, discipline), SC (none).
- **Content that matters:**
  - Each feature is tested ON and OFF by setting env vars `MB_YIELD_EMERGENT` / `MB_YIELD_RALLY` / `MB_YIELD_POCKET` to '1'/'0' and `importlib.reload`ing six modules (`modules.mass_battle.config`, `core.exchange`, `core.state`, `hierarchy.units`, `systems.mass_battle.sim.engine`, `orchestration`) (:18-33); `teardown_module` pops the vars and reloads (:143-146). Module reload mid-session changes class identities for any other test holding old references.
  - Emergent: a unit at 40% hp with discipline 5 (>= `D_YIELD`) enters yielding at `morale_check_phase`; discipline `D_YIELD-1` does not; flag off is inert (:44-66). Rally: recovered morale (>= 0.75 of start) reverts yielding at `between_turn_recovery`; morale 3 of 6 stays yielding; off is inert (:70-95). Pocket: map edge in the flee direction and an enemy in the retreat path are pocketed, open retreat is not (:105-127); a pocketed yielding subunit's `subunit_combat_pool` exceeds the malused pool (:130-140).
  - The ON/OFF pairs give each feature its own control.
- **Conflicts / stale:** `modules/mass_battle/config.py:262,266,272` read `os.environ.get('MB_YIELD_EMERGENT', '1')`: the default is ON (verified), while this docstring and the config comments (:260, :265, :271) still say "ships OFF by default / Gated OFF". Either the comments are stale or the default was flipped without them; the shipped behaviour is ON. `__all__` in that config lists about 150 constants, many `MB_*` flags read from environment variables at import time: module configuration by env var.
- **Open items:** the config comment says the erosion-brake calibration "stays deferred (needs_jordan)"; `YIELD_RALLY_MORALE_FRAC` and `YIELD_POCKET_REACH` are tagged `[CALIBRATED-DEBT]`.

### tests/valoria/test_dice_engine_properties.py
- **What it is:** pytest file, S2 action 3: seeded property sweeps on the dice primitive (`engine/dice_engine/dice_engine.py`), ahead of the season loop.
- **Status:** none stated; reading: live.
- **Bears on:** DICE.
- **Content that matters:**
  - Die Rule and Pool Minimum: `roll_pool(pool, tn=7)` has effective pool `max(1, pool)`, rolls in 1..10, and net within `[-1*n, 2*n]` ("1 = -1 success, 2-6 = 0, 7-9 = +1, 10 = +2", PP-246) over 500 seeded trials with `checked == N_TRIALS` (:45-73); deterministic under identical seeds (:76-83).
  - `_expected_degree` re-types the margin ladder (>=3 Overwhelming, >=1 Success, >=0 Partial, else Failure) independent of the owner and sweeps 500 fractional pairs (:97-125), exact boundary examples at 2.999/0.999/-0.001 (:128-136), and totality over uniform floats (:139-150). This is another hand-written copy of the ladder, held by the same measurement idea as `test_degree_ladder_single_owner.py` but not enrolled there.
  - `tn = 7` is pinned ("TN7 always", ED-IN-0196), so the target-number axis is never varied here; the addendum's F-TEST-08 notes the engine refuses TN 6/8.
  - No `hypothesis` dependency by design (CI installs only pyyaml, pytest, numpy, pytest-xdist, :12-18).
- **Conflicts / stale:** cites `params/core.md §Pool Minimum` and `return_to_game_queue.yaml` (dissolved `params/` path; prose referents).
- **Open items:** states it is "a beginning, not the M1 acceptance row itself".

### tests/valoria/test_engine_does_not_import_systems.py
- **What it is:** pytest file, 772 lines (A-25, plan S5a/`30`): `engine/` names no `systems/` or `modules/` code by import (top-level or function-local), by `sys.path` insert, or by loaded-module file path; composition roles resolve; a computed roster of retained `systems/` homes.
- **Status:** none stated; reading: live. The docstring is explicit that a green result does NOT mean the engine runs without `systems/` (:27-30).
- **Bears on:** CORE (the seam, composition roles, rosters), PC (the one `sys.path` seam), MB, SC, PROCESS.
- **Content that matters:**
  - Two shrink-only ratchets pinned at zero: `BASELINE_TOTAL = 0` (top-level imports) and `NESTED_BASELINE = 0` (function-local); `ALLOWED = {}` (:116-130, :157-200). A pair test shows indenting an import moves it between the two counts (:203-214).
  - `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}`: the only file allowed to insert a code root on `sys.path` (bare-name import of `combatant`/`wrapper`), kept because a dotted import would give the flat-loaded `workbench/balance.py` a second module identity (:228-250). The predicate (`_inserts_a_systems_path`) reads the inserted expression, follows one local assignment, then one hop into a relatively-imported anchor module (:350-400); a planted two-file case proves the hop (:510-554). It is `@pytest.mark.slow` (78.8 s measured 2026-09-11, :464-470).
  - `test_importing_every_engine_module_pulls_in_no_subsystem` imports every non-test engine module in one subprocess and asks each loaded module's FILE path whether it lies under `systems/` or `modules/`; floor `len(mods) >= 20` (:427-461). Its probe is shown able to see both a dotted leak and a bare-name `sys.path` leak, and both roots in a planted tree (:557-609).
  - `composition.require('no_such_role')` raises KeyError (:612-624); `kind: value` roles (e.g. `systems.social_contest.sim.contest:A`) are exported through `tools/export_composition._resolve`, and a missing attribute still fails (:633-667); every declared role resolves, `checked >= 1` (:670-684).
  - Retention is computed: `R04_PENDING_SUBSYSTEMS` = `systems/` directories no `home:` in `engine.season.data.rosters.MODULES` names; `R04_PENDING_ROLES = set()` so no composition role may target an unretained directory; on the real tree `{combat, mass_battle, social_contest} <= retained` (:700-771). That set is read at import time from the directories present on disk, so a checkout with an extra untracked `systems/<dir>` computes a different pending set (the docstring says this is intended).
- **Conflicts / stale:** the file name and the `TOP_LEVEL_SYSTEMS_IMPORT` names say `systems` but the roots are `ci_common.MODULE_CODE_DIRS` (stated at :82-87). Mentions the retired `game_state.py`, `echo_transport`, `parliamentary_bridge`, `combat_bridge` and the campaign driver, all as history. References `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` in a docstring (:512): that filename says retired.
- **Open items:** the converse (a role target whose module never loads) is covered only by "every role resolves".

### tests/valoria/test_engine_params_bridge.py
- **What it is:** pytest file, plan S5e (2026-08-22): one writer per `engine/engine_params/` artifact (hard), and shrink-only ratchets on engine readers and tools/ parsers of authored surfaces.
- **Status:** none stated; reading: live; subject is the runtime input to the engine and the Godot bridge (§0.1 pt 5 predicate met), though it scans `tools/`.
- **Bears on:** CORE, GO (the bridge artifacts), PROCESS.
- **Content that matters:**
  - `ENGINE_READERS` = three artifacts, one leaf each: `composition.json` by `substrate/composition.py`, `descriptors.json` by `substrate/descriptors.py`, `combat_engine_v1.json` by `substrate/combat_kit.py` (only the `kit` section; `cfg`, `core`, `attributes` sections "are read by no engine module", :57-59). `key_types.json` and `world_initial_state.json` entries are gone (retired ED-IN-0232 and 29d-ii).
  - `AUTHORED_PARSERS`: `descriptor_registry.yaml` has six parsers in `tools/`, `module_contracts.yaml` four (`export_composition`, `build_engine_atlas`, `ci_quantity_vocabulary_check`, `m1_acceptance`) and "no exporter and no destination for a new reader" since the Key exporter retired (:87-104). Counts are frozen sets of tool paths, so a legitimate new parser fails until the set is edited.
  - Writer test: every artifact in `engine/engine_params/` has exactly one writer by regex (an `OUT = ...` binding or `open(...,'w')` naming it, :189-199); non-vacuity: `len(arts) >= 7` and `composition.json`'s writer is exactly `tools/export_composition.py` (:202-208).
  - The reader/parser detectors are regex heuristics (`_PATHISH`, `_BINDING`, two-line window) corrected twice in one day by adversarial passes (comments :162-185); a docstring records the repo-wide number of module_contracts.yaml parsers as 21 (tools 10, skills 6, tests 5) though the test walks only `tools/` (:233-257).
  - The "distance to target" test asserts every engine reader set has one member inside `engine/substrate/` (:271-297).
- **Conflicts / stale:** the file describes `engine/engine_params/combat_engine_v1.json` sections `cfg`/`core` as unread by the engine while `test_combat_invariants.py:545` counts them (>150 and >20 keys) as the typed Godot contract: consistent (they are for the port, not the engine).
- **Open items:** `module_contracts.yaml` has no exporter and no destination for a new reader (stated :87-95).

### tests/valoria/test_export_game_constants_ambiguity.py
- **What it is:** pytest file: `tools/export_game_constants.py` (the Godot constants bridge) must never pick a value by directory-walk order when `sim_params.json` has one key with two values.
- **Status:** none stated; reading: live; load-bearing on the port.
- **Bears on:** GO, CORE, MB (the live collision is `mass_battle.SEED_BASE`).
- **Content that matters:**
  - The collision set is computed from the live `sim_params.json` rows (non-table, numeric/bool values); `egc._load_sources()` must not contain any such key and `egc._AMBIGUOUS == collisions` (:39-51). It asserts the collision set is non-empty and says the test is then vacuous if it empties (:44-48), i.e. the test depends on a defect persisting.
  - Every `egc.MAPPING` key must resolve in `_load_sources()` (:54-61); agreeing duplicates are still exported (:64-76), a loop without a floor.
  - Falsifier named: deleting the `for k in ambiguous: del vals[k]` loop fails the first test.
- **Conflicts / stale:** `tests/valoria/test_export_sim_params.py:65` pins the ambiguous set to exactly `['mass_battle.SEED_BASE']`: two tests share the same dependency on one live collision.
- **Open items:** `mass_battle.SEED_BASE` is defined with two values in `bat.py` (1,000,000) and `lanchester_signature.py` (2,000,000) per `test_export_sim_params.py:34-37`; the MB seed base is a doubled constant.

### tests/valoria/test_export_sim_params.py
- **What it is:** pytest file for `tools/export_sim_params.py` (typed values layer, ED-IN-0079): committed `sim_params.json` equals a fresh extract; every value is an AST literal from its definition site; the scan roots are derived.
- **Status:** none stated; reading: live; a round-trip `--check` pattern §0.05 counts as a mechanism.
- **Bears on:** CORE, GO, MB, PC (scan roots), PROCESS.
- **Content that matters:**
  - `esp.check()` returns ok; indexed by (key, file) because `key` alone collides; `(key, file)` unique is its own test (:22-54). The set of keys with more than one value is pinned to exactly `['mass_battle.SEED_BASE']` (:57-69).
  - Scan roots come from `ci_common.sim_reference_roots()` (engine, `systems/*/sim`, `modules/*`), floor `len(dirs) >= 8`, monkeypatch shows the exporter follows the owner (:72-85); a planted tree proves `modules/<name>` joins and `__pycache__`/files are skipped (:88-98).
  - `ci_common.MODULES_WITH_OWN_EXPORT` (combat) is skipped by the sim-params scan because `modules/combat/` ships through `export_engine_params.py` (:101-117); `count == len(params)` (:120-123).
- **Conflicts / stale:** none. The task note in `CLAUDE.md` §0.05 says the live count of constants still in `systems/` comes from `export_sim_params.py --build`; this file is what keeps that artifact honest.
- **Open items:** none.

### tests/valoria/test_face_aggressors.py
- **What it is:** pytest file: `hierarchy.units.turn_to_face_aggressors`: a mass-battle CELL under attack rotates toward its aggressor(s) at a limited slew rate (Jordan's rule), per cell, once per tick.
- **Status:** none stated; reading: live; direct evidence that facing, aggressors and perception are per-cell state in the shipped module.
- **Bears on:** MB (cell state: `_node_pos`, `cell_facing_vec`; facing; rear blind arc; stance `hold`), PC (none).
- **Content that matters:**
  - A cell facing -row with an aggressor at +col (90 degrees off) turns by exactly `MB_FACING_SLEW_BASE` per tick, then reaches 0 error on the second tick (`pytest.approx(abs=1e-6)`, a derived-geometry equality, :61-70); requires `eff_discipline >= 5` as a precondition (:63).
  - Control: `MB_FACING_ATTENTION=False` leaves facing unchanged and the step returns 0 (:73-78). Between two aggressors it faces their average; between opposite-side aggressors it holds; an aggressor in the rear blind arc is not turned toward; a body on `hold` still turns (:81-106).
  - `_val._set_movement_path('node'|'grid')` selects the movement model; with 'grid' (called "the grid oracle") `turn_to_face_aggressors` returns 0 (:109-113). The fixture saves and restores `FIELD_MOVEMENT` and `MB_NODE_COHESION` on both modules.
- **Conflicts / stale:** `_set_movement_path` is in `systems.mass_battle.sim.validators`, i.e. the test selects the engine's path through the `systems/` sim package while the code under test is `modules.mass_battle`. Two movement paths ('node' and 'grid') coexist; facing exists on one only.
- **Open items:** the test depends on a 9-troop-per-cell `build_unit('Line', 3, 'A', 'A', 9)` fixture.

### tests/valoria/test_feigned_retreat.py
- **What it is:** pytest file, PP-256 / mass_battle_v30 §A.12, §B.4 / ED-MB-0022 and ED-MB-0067 Part C / ED-MB-0071: Feigned Retreat resolution (recognise roll, Discipline check, overextend penalty) and the order-writable `feign_retreat` trigger.
- **Status:** none stated; reading: live. Docstring corrects an earlier "default OFF" to "default ON since the flags-ON ruling" (:9-11).
- **Bears on:** MB (orders, deception, discipline, command), SC/FI (a ruse a commander declares, resolved by a recognition roll against a general's Command: fog stands, no automatic reveal).
- **Content that matters:**
  - The mechanic: a Fast victor pursuing a feigning enemy makes Command d10s vs Ob 2 to recognise; if deceived, a Discipline check at Ob 1; failing it sets `overextended`, cutting the pursuer's next engagement pool by `OVEREXTEND_PENALTY` (:1-8, :141-155). Realised Discipline-1 hold about 40% (matches PP-256), Discipline-4 about 74.5% (the doc's 87% was a no-botch idealisation; the file refuses a bespoke botch-free counter as a "scale-local dialect", :20-25).
  - Rate tests are sampled with a global `random.seed(...)`: 20,000 trials, bands `0.36..0.44` and `0.70..0.79`, monotone in Discipline (:58-69); recognition rises with Command (one-sided `low < high`, :72-78).
  - `test_resolve_marks_overextended_only_when_deceived_and_failing` carries its own anti-vacuity counter (`n_recognized >= 1000`, measured 1560 of 2000, floor at half, :96-107), a conditional-assert-with-counter example added at ED-MB-0045 S12; `n_over > 0` for low-Discipline low-Command pursuers.
  - The trigger: before ED-MB-0067 C4 nothing assigned `.feigned` (dead by construction); now an `Order` with `behavior={'feign_retreat': True}` sets the issuing Unit's `.feigned` through `core.contact.check_orders`, never as an attribute on the Subunit (:164-222); a later-trigger order (`tick:5`) does not pre-declare (:189-200).
  - Gate-off (`MB_FEIGNED_RETREAT=0`) is inert/byte-exact; flag toggling reloads four modules and `teardown_module` resets to OFF (:35-45, :225-227).
- **Conflicts / stale:** `teardown_module` reloads with `on=False` while the shipped default is ON (as the module docstring says): after this file runs, the in-process `config` module sits at OFF until another reload, a cross-test order effect [UNVERIFIED]. Cites PP-256's "~87%" as a doc figure the code deliberately does not match.
- **Open items:** no NPC chooser that DECIDES to feign exists in this file's scope; the trigger is an order a scenario author writes.

### tests/valoria/test_field_golden_pins.py
- **What it is:** pytest file, plan-v2 A1b / ED-MB-0053 / ED-MB-0061: drift guard for `tools/ci_golden_modes_check.py`'s `FIELD_PINS` and `MODES` (the pin vector for the mass-battle field goldens) against the `environ.get` defaults in `modules/mass_battle` and `systems/mass_battle/sim`.
- **Status:** none stated; reading: live. Its own comments mark ten pins as "transition debt" ("THIS SET MUST BE EMPTY AFTER THE RE-BASE", :136-137).
- **Bears on:** MB (shipped configuration vs golden configuration), CORE (golden discipline), GO.
- **Content that matters:**
  - Jordan's flags-ON ruling (2026-07-29) flipped 15 `MB_*` defaults ON at once; the goldens still record the pre-flip configuration (re-basing first "would bake nine defects into the definition of correct"). `_PENDING_REBASE` (:141-145) names the ten pinned flags whose pin differs from the source default: `MB_CELL_DAMAGE, MB_CELL_MORALE, MB_CLOSE_RANKS, MB_FRACTIONAL_POOL, MB_FRICTION, MB_INTENT_RESOLUTION, MB_TROOP_DENSITY_CAP, FIELD_CONTACT, MB_FACING_MODEL, REFORM_CHECK_ENABLED`. So the golden battery certifies a configuration that is not the shipped one for ten flags (`test_pending_rebase_set_is_exactly_the_transition`, which pins the set both ways and `len == 10`, :148-168).
  - `_KNOWN_INERT` lists env-read flags that cannot move a battery digest: including `MB_YIELD_EMERGENT/RALLY/POCKET`, `MB_FEIGNED_RETREAT`, `MB_RESERVE_COMMIT`, `MB_ROLE_INSTRUCTIONS`, `MB_FACING_*` (no-ops while `MB_FACING_MODEL` is pinned '0'), `COMMAND_SIGMA_ENABLED` (dead while `POOL_QUALITY_MODEL=1`). Five of those were justified circularly ("inert because off") and were re-established by measurement (cell_field, 6 seeds, digest `71fdb844...` identical ON vs OFF, :64-77). So facing, yield, feigned retreat, reserve commit and role instructions are NOT exercised by the golden battery at all.
  - `test_pins_match_source_defaults` has `checked == expected` arithmetic (:189-191), `test_no_unclassified_env_reads` makes every engine `environ.get` classified, `test_every_pin_is_read` detects rot, `test_mode_selectors_cover_every_out_of_budget_golden_mode` pins the exact mode set `{unit_field_mor0, cell_field_mor0, cell_legacy_mor1}` and reads geometry (cell/unit), movement (field/grid) and morale axes out of the key (:220-248).
  - `test_known_inert_reasons_are_not_self_referential` reads THIS FILE'S OWN SOURCE text (`open(__file__)`) and looks for the string `MEASURED-INERT` within 1,400 characters before each flag name (:258-302): a self-referential text-position guard whose subject is a comment.
  - The comment at :269-270 says `test_dg2_yield_residuals` "fails at the new defaults"; that test sets its env vars explicitly in `_reload`, so it should be default-independent [UNVERIFIED].
- **Conflicts / stale:** a header line says tests moved to `tests/sim/mass_battle/` then `systems/mass_battle/sim/` then `modules/mass_battle/` (three relocations recorded in comments, :24-36). The shipped MB configuration (flags ON) is not the configuration any hash in this lane certifies.
- **Open items:** the re-base itself ("the defects the flip exposed" nine of them) is the exit condition; nothing in this file schedules it.

### tests/valoria/test_flow_skeletons.py
- **What it is:** pytest file, 726 lines: checks every `` `path:line symbol` `` anchor in the ARCHIVED `<sub>_flow_skeleton_v1.md` documents (roster parsed from the archived format spec) plus `engine_atlas_v1.md`: file exists, line in range, symbol within +-3 lines or enclosing the cited span; required section order; `**Contracts:**` header names real modules.
- **Status:** none stated; reading: live as a test, subject archived and frozen (addendum F-TEST-04 recommends deletion; confirmed below).
- **Bears on:** PROCESS (guard of archived prose), CORE, MB, PC, SC, FA, SE, FI, WR (every subsystem skeleton is anchored here).
- **Content that matters:**
  - Roster comes from `.designs/systems/_architecture/reference/subsystem_flow_skeletons_v1.md` §3 at import time (`_roster`, :130-146); `len(ROSTER) >= 15`; each row's path must equal `systems/<name>/reference/<name>_flow_skeleton_v1.md` (:158-163). The test reads `.designs/` (and, through `QUARANTINE_MIRRORS`, `.audit/`) for its inputs (:56-90): the brief says nothing outside `.audit/` may load anything inside it (RULED) [UNVERIFIED whether any anchor currently resolves into `.audit/`].
  - Mutation record M1a-M8 (10/10) is in the docstring and not re-run; the docstring states what it does not catch: line drift within the named definition (:39-45).
  - Exemption machinery makes the guard soft where code moved: `RETIREMENT_SHIFTED` (14 live paths plus census sidecars) turns bare-line anchors into advisory ("281 of the 587 anchors are bare line numbers", :315-327), `LINE_UNSTABLE_TARGETS` (1), `RETIRED_SYMBOLS` (about 30 names, many Key-substrate), `RETIRED_CALL_SITES` (4), `RETIRED_GENERATED` (6), `RETIRED_CONTRACTS` (3: `articulation_layer`, `personal_combat`, `fieldwork_knots`). Roughly 60 exemption strings; the comments admit "what is lost is real" (:322-327).
  - Anti-vacuity floors: `MIN_ANCHORS_PER_SKELETON = 3`, `MIN_TOTAL_ANCHORS = 150`, symbol checks `>= 75` (:589-609), `len(known) >= 20` module rows (:693-696). Several tests `pytest.skip` when a skeleton is missing (:177, :199, :583, :631, :690), delegating to the roster test.
  - `_is_retired` uses `pathres.resolve(...).status == FORKED`, and its docstring records the directory-prefix hazard as wanted here (:457-469).
- **Conflicts / stale:** `_CENSUS_SIDECARS` is computed at import from `os.listdir(ROOT/'systems')`, a directory that on a fresh clone lacks five subsystem dirs (`_architecture`, `articulation`, `npcs`, `ui`, `victory`), fixed by unioning with `.designs/systems`; a failure documented as red in CI and green locally. `modules/mass_battle/terrain.py:269-270` (per the addendum) keeps a constant below a lookup so a skeleton's line anchor stays put: code placement is decided by an archived document's citation.
- **Open items:** the file documents that 12 anchors point into untracked generated files and calls the durable fix (cite by symbol) "a design-surface call, flagged for Jordan" (:574-581), later taken by the symbol-binding rule.

### tests/valoria/test_fractional_pool.py
- **What it is:** pytest file, ED-MB-0032 (Jordan 2026-07-23 "pool must be fractional"): `roll_pool_fractional` in mass battle keeps the pool at full precision (integer dice plus one extra die rolled with probability `frac`).
- **Status:** none stated; reading: live; test name `test_default_gated_off` is stale (it asserts the default is ON).
- **Bears on:** MB, DICE (fractional pool / sub-1D floor), PC (contrast), CHAR.
- **Content that matters:**
  - `C.MB_FRACTIONAL_POOL is True` (default ON since Jordan 2026-07-29, ED-MB-0061; "it does move goldens", :23-26); `PER_DIE_NET_EV == 0.4` ((-1 + 3 + 2)/10 for faces 1, 2-6, 7-9, 10; `approx` on an arithmetic constant, :29-31).
  - Sampled with global `random.seed`: a 0.5 pool has mean 0.2 within `abs=0.05` over 8,000 draws (a 25% relative tolerance, :34-40; the addendum flags this as a `[not adjudicated: DICE]` row), pool 0.6 can net below 0 and exactly 0 (the Failure boundary survives, :43-49), 3.7 vs 3.0 differ by 0.28 within `abs=0.08` (:52-57), integer pool equals `roll_pool` for the same seed (:60-66), means rise across 2.0..3.0 (:69-76).
  - Contrast with PC: personal combat rounds faculty to an integer die count (`core.resolution_pool`, `int(round(faculty))+6`, `test_combat_invariants.py:225-242`), so two pool conventions (fractional for MB, rounded for PC) coexist.
- **Conflicts / stale:** the function name `test_default_gated_off` contradicts its assertion; comment cites "Fable-audit A3". `_SIM` sets `tests/sim` on the path (unused here).
- **Open items:** none.

### tests/valoria/test_friction.py
- **What it is:** pytest file, ED-MB-0016 / DG-6 (renamed from CEV at ED-MB-0045): per-battle per-side LogNormal combat-effectiveness "friction" drawn once to keep outcome variance scale-invariant.
- **Status:** none stated; reading: live; the file records an open defect.
- **Bears on:** MB (variance, decisiveness, Clausewitzian friction), DICE.
- **Content that matters:**
  - Assertion text at :91-95 records that the shipped default (`MB_FRICTION` ON, ED-MB-0061) "confers a large SYSTEMATIC one-sided advantage (mean end-state hp A 0.9910 / B 0.8634 over the 20 historical rows, 13 of 20 at exactly 1.0000; with it alone off, A 0.8625 / B 0.9390)... an open engine defect, not a reason to re-gate the mechanic" (F1). The test asserts the flag is ON; it does not assert the defect is absent.
  - Each module that star-imports config holds its OWN copy of the flag (`_cfg`, `_exch`, `_orch`), so the file's fixtures patch all three and the OFF test patches `_orch` only (caught by a failure at 5.717 != 1.0, :96-100): the "multiple owners at the flag layer" hazard in miniature.
  - Properties: OFF makes `_friction == 1.0` exactly (:85-108); drawn once per battle (a second `_draw_friction` call does not redraw, :113-124); mean of log over 400 draws within 0.15 of 0 (~3 SE, :127-140); at 1,600 base troops a 2:1 matchup is at least 95% decisive without friction and under 90% with it, difference at least 10 points over 40 seeds each (`@pytest.mark.slow`, :145-163); the 400-troop A/B has off > on and off >= 90 (:166-179); conservation via the shared `_conservation.assert_troop_conservation` with `checked >= 2`, and same-seed determinism of the outcome tuple including `_friction` (:184-211).
  - Win-rate bands are sampled, n=40, seeds `9000+`.
- **Conflicts / stale:** cites `audit/2026-07-22-mass-battle-stress-test/dg6_friction_resolution.md` (archived). The F1 defect text conflicts with leaving the default ON; no test pins F1 as fixed.
- **Open items:** F1 (one-sided end-state advantage with friction ON) is stated open here.

### tests/valoria/test_front_fixer_scope.py
- **What it is:** pytest file, ED-MB-0041 Tier-2: the fixing-force relation (`_compute_front_fixers`) must be computed over the whole tick, not per cascade sub-phase group.
- **Status:** none stated; reading: live; small.
- **Bears on:** MB (envelopment, flanking, Cannae shape).
- **Content that matters:**
  - Relation: only an enemy in the defender's GREEN (front) arc registers as a fixer; a flank enemy does not (:50-58).
  - Partition-dependence: evaluating the flank pair alone gives an empty fixed-by-other set, the whole tick retains the frontal fixer (:61-78): the defect that motivated hoisting the computation.
  - `resolve_engagements` must accept a `front_fixers` parameter (a signature pin, :81-84).
  - Scenario builder `_scenario()` places D at `SIDE_A_START_ROW` col 20, front enemy +6 rows, flank enemy +12 cols (:38-47).
- **Conflicts / stale:** none. Documents "CASCADING_ENABLED" sub-phase groups.
- **Open items:** none.

### tests/valoria/test_frontage_conservation.py
- **What it is:** pytest file, spatial-model v2 Stage D (ED-MB-0013): the continuous front-overlap width (`geometry.engaged_frontage`) replaces the last integer on the contact path; the Lanchester term stays linear.
- **Status:** none stated; reading: live; one dead variable.
- **Bears on:** MB (cell geometry, Lanchester attrition, contact, conservation of troops).
- **Content that matters:**
  - Geometry properties: aligned head-on rows give frontage equal to the file count (n=1,3,5 at `abs_tol=1e-9`), a half-file offset gives exactly 2.5, depth-2 does not inflate frontage, frontage is capped at the enemy's covered span (an 11-file side against 3 files gives 3.0: numerical superiority is a linear edge, never square), empty sides give 0 (:66-114).
  - `_lanchester_strength(cells, unit=None, front_width=w)` scales linearly in `front_width` (1, 2, 2.5); `front_width=None` reproduces the legacy distinct-column count; `front_width=0` gives 0 (:119-143).
  - `test_field_pairs_carry_continuous_frontage` computes `seen_fractional` but never asserts it ("not asserting seen_fractional strictly ... keep it informative", :180-182): a dead variable; only `seen_front` is asserted.
  - Conservation: sum of `cell_troops` equals `hp` for both units at battle end over seeds 1, 7, 42, 101, 2026 through `_conservation.assert_troop_conservation` with `checked >= 2` (:185-202); same-seed determinism (:205-217). The addendum notes `_conservation.py:99` uses `approx` on a conservation claim `[not adjudicated: MB]`.
  - The "grid oracle" path (`front_width=None`) and node path coexist (see `test_face_aggressors.py`).
- **Conflicts / stale:** none found. Two movement paths ('grid' oracle and 'node' field) both live.
- **Open items:** none.

### tests/valoria/test_generated_layer.py
- **What it is:** pytest file (culling wave 5, ED-IN-0194): the session-scoped `generated_layer` conftest fixture builds the untracked generated artifacts; this file asserts each exists non-empty.
- **Status:** none stated; reading: live; process only.
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - Every declared artifact path is a file and non-empty (:38-48); floor `len(generated_layer_paths) >= 4`, with the floor-lowering history (10 to 7 at ED-IN-0232, 7 to 4 at plan position 28-i, :51-65).
  - States that determinism of each builder is left to per-artifact tests (`test_engine_atlas.py`, `test_execution_map.py`), two of which retired with their builders.
- **Conflicts / stale:** the docstring says `test_execution_map.py::test_the_render_is_deterministic` exists while the execution-map cluster retired at 28-i [UNVERIFIED].
- **Open items:** none.

