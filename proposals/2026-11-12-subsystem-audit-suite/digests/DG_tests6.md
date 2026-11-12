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

### tests/valoria/test_import_cycle_game_state_npe.py
- **What it is:** pytest file (OI-52a, ED-IN-0097; renamed in practice to a cycle census): runs `skills/valoria-vector-audit/scripts/structure_audit.py`'s `tarjan_scc`/`_cycles` over the real repo and requires exactly four import cycles in four named families.
- **Status:** none stated; reading: live as a count pin on a process instrument's output over the game tree; names are stale.
- **Bears on:** CORE, MB, SC, PROCESS.
- **Content that matters:**
  - Pinned: `len(cycles) == 4`: (1) the 9-module `systems.social_contest.sim.contest.*` cycle ("documented intentional-during-rebuild"), (2) the `modules.mass_battle` canon family, (3) `modules.mass_battle.battle_loop <-> orchestration` (matched by exact member set; `run_battle` reads orchestration's ~40 module globals by function-local import, so tests that `monkeypatch.setattr(orchestration, ...)` still reach it), (4) `engine.season.harness.exercises <-> run_cases` (a `__main__`-guarded import: not a runtime cycle) (:107-160).
  - The `massbattle <-> units` cycle must not return (:137-142). `checked == 4` and `len(accounted) == len(cycles) == 4` close the loop against vacuity (:153-160).
  - Structural note: the AST-only graph builder counts function-local and `__main__`-guarded imports as edges; ten modules repo-wide carry `__main__`-guarded imports and the consolidation of that rule was declined (:84-91).
- **Conflicts / stale:** the file name, the first line of its docstring, and the test name still say `game_state_npe` / "exactly_four" while the docstring's first sentence says "THREE since step 8"; the assertion is four. `engine/autoload/game_state.py` and `canon_buckets.py` are deleted (history paragraphs). The 9-module SC cycle is stated as intentional but is a counted exception, not a retirement item.
- **Open items:** the SC contest cycle and the MB battle_loop cycle carry "goes when ..." conditions that nothing schedules.

### tests/valoria/test_knot_pool_formula.py
- **What it is:** pytest file (ED-FI-0005 / OPT-AV-9): asserts three ARCHIVED `.designs/` documents contain the formula `(Spirit*2)+History(Relevant)+3` and the `floor(Bonds/2)+1` count cap, and not `(Bonds*2)+3`.
- **Status:** none stated; reading: stale and a test of archived prose (confirms addendum F-TEST-04).
- **Bears on:** FI (knot pool), CHAR (attributes), PROCESS.
- **Content that matters:**
  - Surfaces: `.designs/systems/_architecture/reference/derived_stats_v30.md`, `.designs/systems/fieldwork/reference/knots_v30.md`, `fieldwork_editorial.md` (:17-21); reads them as text and normalises whitespace/glyphs (:24-27).
  - The docstring says "There is no sim/ oracle that computes the Knot Pool, so this is a doc-content guard" (:6-8); per the addendum the code is now `pool = spirit * 2` with the History addend deleted by CR-85 (`systems/fieldwork/sim/knots.py:216`), so the test is green while pinning text the code contradicts.
  - It pins a retired attribute: `Bonds` is retired and `Spirit` is an alias of `attr.mind.will` in `test_descriptor_registry.py:27,60`.
- **Conflicts / stale:** vs the code (above) and vs the CR-84 attribute roster (Bonds retired). Reads `.designs/` as test input, which the brief says proposals must not make tests do.
- **Open items:** none (delete candidate per addendum T-03).

### tests/valoria/test_link_values_pointers.py
- **What it is:** pytest file for `tools/link_values_pointers.py` (value-to-pointer link, ED-IN-0079): committed link map equals a fresh build; every link token literally occurs in the linked constant's name or dict keys.
- **Status:** none stated; reading: live; process/tooling over `sim_params.json`.
- **Bears on:** PROCESS, CORE (sim params).
- **Content that matters:**
  - Anti-fabrication: token must be in the value's `name` or its dict keys (:29-38); no authoring-abbreviation tokens (`lvp._EXCLUDE_ABBR`, :41-44); the by-pointer index agrees with the flat link list (:47-52).
  - Each loop iterates `lvp.build()["links"]` with no population floor, so an empty link list passes all three; `test_links_current` calls `lvp.check()`.
- **Conflicts / stale:** `lvp.build()` is called three times per run (cost only). Uses the `generated_layer` fixture.
- **Open items:** none.

### tests/valoria/test_m1_acceptance_probe.py
- **What it is:** pytest file (S2, ED-IN-0112): the probe rows of `tools/m1_acceptance.py` (stub invocations, determinism) are measured on `engine/season/` (the head) and reproducible under the fixed probe seed.
- **Status:** none stated; reading: live; the addendum read it in full (F-TEST-12 row 9).
- **Bears on:** CORE (the milestone instrument), PROCESS.
- **Content that matters:**
  - The head is asserted by module path (`m1._headless.__name__.startswith('engine.season.')`, :57) after a re-point from the superseded campaign driver (six days certified the wrong tree, 2026-09-13, :9-13). `test_engine_probe_import_succeeded` fails if the harness import fell back to blocked.
  - Determinism row must pass and not be `(empty)`; `_run_probe_season(M1_PROBE_SEED)` twice agrees on `content_hash` and `stub_hits`; `collect()` reports at least 4 of 5 rows measured or partial; `main(['--check'])` exit code equals `1 if failed else 0` (:60-132).
  - The different-seed test ends `... != ... or fixed.events == 0` (:112-113): when the fixed-seed season has zero events the assertion is satisfied vacuously (F-TEST-12 row 9).
  - It deliberately does not pin the stub-call count ("the relation, not the number").
- **Conflicts / stale:** comment at :74 says "identical seed -> identical KeyLog.content_hash()": KeyLog is retired; the code reads `World.content_hash()`. The docstring cites `return_to_game_queue.yaml S2`.
- **Open items:** none.

### tests/valoria/test_mass_battle_ammo.py
- **What it is:** pytest file, A6 / ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md): per-SUBUNIT missile ammunition ledger (`volleys`, `eff_volleys`, `drain_volleys`, `resupply_volleys`) and its gate on `volley_phase`.
- **Status:** none stated; reading: live; strong, with controls; one stale sentence.
- **Bears on:** MB (ranged units, ammunition, supply at the between-turn lull, kiting), SE (supply), CHAR (none).
- **Content that matters:**
  - Ledger lives on the Subunit, own-else-inherited-Unit like `stamina`; a first version on `percell._ColBlock` was reworked because a column is shared among subunits (ammo regenerated free or went unmetered); `test_ammo_is_independent_of_column_identity` shifts `cell_offsets_c` by 50 and asserts ammo unchanged (:151-167).
  - `MB_AMMO_ENABLED` defaults ON, checked in a SUBPROCESS with the env var unset (:72-84); the autouse fixture sets it True and restores. `volley_phase` returns `shots`, `loss_a`, `loss_b`.
  - Controls: the in-range control (`shots >= 1` before any exhaustion claim, :93-100); exhausted archers deal 0 loss and record 0 shots after `exhausted_at`, with `exhausted_at is not None` and `fired_ticks >= 1` asserted (:102-119); melee atoms are never gated, `volley_phase` is a no-op for two melee sides (:138-148).
  - Resupply at `between_turn_recovery`: from 0 to `min(MB_VOLLEYS_START, MB_VOLLEYS_RESUPPLY)`, clamped at start (:122-135).
  - F4 [HIGH]: `build_army` did not forward `volleys`, so every ranged subunit shared the parent Unit pool and melee siblings' resupply refilled it each turn; the test builds three subunits through `build_army` and checks the archer's own drain+resupply (:186-214); explicit spec override still wins (:217-222).
  - F7: a `kite` instruction's far bound keys on ammo: with ammo it holds the volley band, with `volleys = 0` `_kite_goal` returns None (close in) (:225-243). This is the only ranged-to-melee behaviour change in the file: ammo exhaustion changes a movement goal; there is no weapon-in-hand state, no switch cost, and `troop_type='archers'` carries no secondary weapon in these fixtures.
- **Conflicts / stale:** the docstring says campaign-adapter armies are melee-only per `massbattle.py`'s `_faction_to_unit`; that function was deleted at plan position 29b (`test_flow_skeletons.py` RETIRED_SYMBOLS). Cites `config.py`'s note and `bat.py`'s EXPECTED comment for the golden re-record.
- **Open items:** none stated.

### tests/valoria/test_mass_battle_army_record.py
- **What it is:** pytest file, ED-IN-0306 phase 2: the rules under the season's army verbs: `troop_types/recruitment.py` (how many troops a place can raise) and `armyrecord.py` (the pure army record and its operations, `A.apply(ArmyCommand)`).
- **Status:** none stated; reading: live; strong refusal and conservation tests; some `[ASSUMPTION]`-grade data.
- **Bears on:** MB (army record, subformations, recruitment), SE (population, infrastructure bound the army), FA (army verbs), CORE (`MassBattleInput`, rosters), CHAR (troops are counts per cohort, not characters).
- **Content that matters:**
  - Recruitment: `recruit_limit(type, weight, sites, raised, FULL)` is bounded by population (`under_arms_cap(w) = int(w * TROOPS_PER_WEIGHT * MUSTER_FRACTION)`), by a per-type training site (`levy` needs none; `archers` need an `archery_range` at proportional completion; `knights_templar` have an elite floor of 0.5 of a stable), and the two bounds compose; unknown type or `full == 0` raises ValueError (:27-71). Verified in source: `TRAINING_SITE` maps 13 types to four site kinds (barracks, archery_range, stable, siege_workshop) and is tagged `ASSUMPTION; Jordan to correct` (`recruitment.py:55-69`).
  - Record: a frozen-dict-like state `(trained, subformations, strategy)`; `raised`, `form` (max 11, a 12th refused; roles such as `ShieldWall`), `assign`/`release` conserve every trooper and never mutate (`A.by_type` unchanged, `release` undoes `assign`, :97-106); 14 ValueError refusals (over-assign, unknown cohort, duplicate name, non-string name, bad role, fractional count, bad stance, `fall_back_at` above 1, bad strategy, :109-132); `order` changes only the fields named (stance, target, fall_back_at) (:135-141); `to_order_of_battle` scales each cohort's contribution by a `fitness(cohort)` and drops empty subformations (:144-153); `validate` rejects malformed records (:156-161).
  - `test_an_army_record_fights` runs `massbattle.resolve_field(MassBattleInput(... orders_of_battle=(a, b)))` and asserts `min(size_pct) < 1.0` ("vacuous: nobody took a casualty" guard), noting subunits under 80 troops rout at the first check (:171-179).
  - `rosters.RECORD_KIND_KEYS['army'] == A.KEYS` (:188-190); `A.apply` dispatches `recruit, form, assign (negative count = release), order, validate` and refuses `march`, missing fields, over-cap and wrong-type recruits (:193-223); the recruit limit is per cohort.
  - The unit of an army is (cohort, troop type, count): soldiers are counts, not named characters.
- **Conflicts / stale:** none found; cites "RTK / Total War unit classes" as the source of the training pairing, flagged as the module's assumption.
- **Open items:** the pairing and the 0.5 elite floor await Jordan's correction (per the source tag).

### tests/valoria/test_mass_battle_maneuvers.py
- **What it is:** pytest file, ED-1096/1097 (movement/pathing audit fix plan step 6): runs the mass-battle maneuver validators `v_envelop` and `v_sweep` on both movement paths, grid (legacy) and node (live default).
- **Status:** none stated; reading: live, with the standing non-strict `xfail` (addendum F-TEST-10).
- **Bears on:** MB (envelop, sweep, movement paths, discipline-degraded speed tiers).
- **Content that matters:**
  - Four tests call `systems.mass_battle.sim.validators.v_envelop/v_sweep(path=..., seeds=8)` and assert `r.passed`: `envelop_reaches_rear_grid`, `sweep_displaces_laterally_grid`, `sweep_displaces_laterally_node`, plus `envelop_reaches_rear_node` marked `xfail(strict=False)` (:71-175). The measurement instruments (`validators.py`) live in `systems/`, driving `modules/` through toggled process globals (`FIELD_MOVEMENT`, `MB_NODE_COHESION`, `PER_CELL`, `MB_ENVELOP_PATH`, `MB_SWEEP`), saved/restored in an autouse fixture (:43-68).
  - The xfail reason records: a limit-cycle bug (no hysteresis between phase-1/phase-2) and a step-freeze bug were fixed; the fixture's small detachment (base cell speed 1) still stalls because discipline-degradation speed tiers `floor(base*disc_mult)` floor to exactly 0 below the top discipline tier ("disclosed-not-chased"); 11 of 20 seeds reach behind the defender; an XPASS was seen once at 2026-07-08 and not re-verified (:86-111).
  - History worth knowing: the 'envelop'/'sweep' instructions "exist only on the legacy grid path" until fix-plan step 7 (the waypoint primitive `_resolve_maneuver_goal`); before this file every bare validator run measured the dead arm (:1-19). Gauge rows H3-H6 overshoot their historical bands in the attacker's favour after DG-1/DG-3 (unresolved partition-invariance question, ED-MB-0004 `_convergence_scale`, :150-163).
- **Conflicts / stale:** cites `designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/README.md` and `tests/coverage_matrix.md` (archived paths). The "live default" claim (node path) is unverified in this file beyond the history.
- **Open items:** the speed-floor edge case for low-base-speed bodies is flagged "for a future movement-tier pass"; the H3-H6 overshoot question is "explicitly not decided".

### tests/valoria/test_mass_battle_officers.py
- **What it is:** pytest file, A3 + C5 (ED-MB-0067 Parts A and C, ED-MB-0073): subordinate officers and a span-of-control ladder in `build_army`.
- **Status:** none stated; reading: live; behaviour tests of the constructor, no resolution.
- **Bears on:** MB (command hierarchy, army -> officer -> subunit), CHAR (officers as characters with charisma/cognition), FA (none).
- **Content that matters:**
  - `Officer(name, command | charisma, cognition)` derives Command the same way a general's is (`derive_command`, ED-899), defaults to 4 (the tier-3 baseline), clamps to 1..7 (:28-46).
  - The ladder (Jordan, ruled 2026-09-25, "one ladder... max commanded = Command... at every echelon, including the new officer post"): each officer's subunit count must not exceed that officer's own Command, and the general's direct reports (distinct officers plus un-officered subunits) must not exceed the general's Command; ValueErrors with specific messages (`commands 5 subunits, exceeding their own Command 3`, `general commands 5 direct reports`, unknown officer, duplicate name) (:77-114).
  - The "done when": a general of Command 3 fields 12 subunits (above the flat `SUBUNIT_CAP = 11`) through three Command-4 officers (:60-74). With `officers=()` the flat cap is unchanged ("exceeds the videogame cap") (:49-57).
  - Everything asserted is at construction; whether an officer's Command affects resolution (orders delivery, morale, pool) is not tested here.
- **Conflicts / stale:** `SUBUNIT_CAP` is imported from `systems.mass_battle.sim.engine` while `Officer` is in `modules.mass_battle.hierarchy.units`: constant owned by the sim wrapper.
- **Open items:** officers carry only a name and Command; the brief's "named, distinct characters" intent is not reached by this record.

### tests/valoria/test_mass_battle_order_of_battle.py
- **What it is:** pytest file, ED-IN-0306 phase 1: a faction's `OrderOfBattle` (named `Subformation`s with troop type, size, role, stance, target, `fall_back_at`, plus a strategy) reaches the mass-battle engine through `massbattle.resolve_field`.
- **Status:** none stated; reading: live; the file states a control and a falsifier up front (:1-12).
- **Bears on:** MB (order of battle, formations, troop-type roster, loadout), SE/FA (the army the season fields), CORE (`MassBattleInput.orders_of_battle`).
- **Content that matters:**
  - Control: no orders of battle equals `(None, None)` bit for bit, and `_weighted_unit` still builds a single infantry subunit (:46-51). Falsifier: 1,000 heavy infantry vs 1,000 levy fight differently over 12 seeds, heavy wins more and keeps more, with a vacuity assertion that both took casualties (:65-72).
  - Ten boundary refusals through `validate` and `build_unit` (empty, unknown strategy, duplicate name, unknown type "no stat preset", non-positive size, role outside the menu, bad stance/target, `fall_back_at=1.0`, more than 11 subformations "cap", :83-99).
  - Deployment: melee front, ranged behind (opposite the advance), horse on the flanks, no overlapping cells (`len(seen) > 10`), sides on opposite rows (:109-139). Stance precedence is subformation, then role, then strategy (`STRATEGIES['advance']['melee'] != ['defend']['melee']`; `ShieldWall` under the neutral strategy holds, an explicit stance wins; :143-150, :228-236). `fall_back_at` 0.4 becomes an Order `own_strength:0.4 -> stance retreat` on the subunit (:153-157). A `mounted_archers` body with no role defaults to role `Kite` with instructions; another type has none (:160-168).
  - Roster: `spearmen`, `skirmishers`, `light_cavalry` each have stats, a role menu entry and a `loadout_for(t) = (weapon, armour)` pair: the loadout is ONE weapon and one armour per troop type; reach (spearmen 0.2 vs light infantry 0.1), support ranks, mounted set `{cavalry, mounted_archers, light_cavalry}` (:178-190). Every stat preset has a loadout and a reach (:193-199).
  - `ob._UNIT_POWER == massbattle._SEASON_FORCE_POWER` and command/discipline baselines equal `_MVP_UNIT_COMMAND` (:202-206): constants kept equal by a test across two modules. Survivor shares never exceed 1.0 (falsifier `by_troops=False` in `resolve_field`, 12 seeds, :209-220). A barracks's capacity is shared between its types (:239-248).
- **Conflicts / stale:** none found; `SEEDS` comment says losses are one-sided per seed so a type's effect shows in the aggregate.
- **Open items:** no per-subformation secondary weapon, no weapon-in-hand state, no loadout weight/fatigue/speed cost appears anywhere in this file or the roster tests (relevant to the mixed-weapons-per-unit intent).

### tests/valoria/test_mass_battle_perception.py
- **What it is:** pytest file, A2 / ED-MB-0067 Part A: `enemy_range:` order conditions see only what the unit's facing cone shows (`core/contact._visible_enemy_cells`, `FOV_HALF_DEG = 105`).
- **Status:** none stated; reading: live; includes its own live-flag control.
- **Bears on:** MB (perception, orders, facing), FI/CHAR (what a unit knows), SC (none).
- **Content that matters:**
  - Cone: a cell dead ahead of facing (1, 0) is visible; one dead behind (180 degrees, past 105) is not (:35-44); with `_node_facing` unset it falls back to `(advance_dir, 0)` (:47-55).
  - `enemy_range:10` fires for an enemy at distance 5 ahead and not for one at distance 5 behind; an enemy inside the cone but beyond D=5 does not fire (the distance axis is separate, :58-88).
  - Composition: the filter is a no-op when `MB_FACING_MODEL` is off, and when only `MB_FACING_FOV_GATE` is off (an AND of both flags, :93-125); control: both flags default ON at shipped values (:128-136). The facing model is pinned OFF in every golden-battery mode (`test_field_golden_pins.py`), so no golden observes this filter.
  - The unit's knowledge is its own facing cone: no fog beyond that, no distance-limited sight (`MB_SIGHT_RANGE` was removed as provably dead).
- **Conflicts / stale:** none.
- **Open items:** the oblique-row digest control for `build_refused_flank` "is run separately (see the session report)": a claim with no artifact here.

### tests/valoria/test_mass_battle_role_instructions.py
- **What it is:** pytest file, MB-04 (A5 role instincts, #445 U-3): a role's instruction keywords drive engine primitives; `hierarchy.units.ROLE_INSTRUCTION_PRIMITIVES` is the single owner of the keyword-to-primitive map.
- **Status:** none stated; reading: live; falsifier and OFF-arm control present.
- **Bears on:** MB (roles, instructions, stance precedence, feigned retreat), CHAR (none), PC (none).
- **Content that matters:**
  - Before MB-04 a `ShieldWall` and a `Push` fought identically to the last float; with `MB_ROLE_INSTRUCTIONS` ON they differ in advance (ShieldWall 0.0, Push positive) and in density over seeds 11-13 (`checked == len(_SEEDS)`, :55-66); OFF arm reproduces equality (:69-73).
  - Stance precedence for roles: an explicit non-balanced stance beats the role default; an Order or spec that writes `balanced` is remembered as written and beats the role keyword (ShieldWall released at `tick:3`, :76-107); `VolleyLine` no longer carries `hold` (which stops archers via `STANCE_SPEED_MOD['hold'] = -99`, :110-114).
  - `Feint` (lure) declares the Feigned Retreat at the pursuit site: `resolve_feigned_retreat(pursuer, lure)` is non-None for a Feint unit and None for a Shock unit, and inert OFF; the keyword is read at the site, not written onto the Unit (:117-134).
  - Completeness: every keyword `ROLE_SPEC` hands out (at least 10) has a row in the mapping, a primitive or None with the reason (:137-143).
  - It imports the `field_path` fixture from another test file (`from .test_reach_weapon_class import field_path`, :23), a cross-file fixture dependency.
- **Conflicts / stale:** `MB_ROLE_INSTRUCTIONS` is in `_KNOWN_INERT` for the golden battery (`test_field_golden_pins.py:90`): no golden observes roles.
- **Open items:** none.

### tests/valoria/test_mass_battle_routes.py
- **What it is:** pytest file, A1 / ED-MB-0067 Part A (squad-engagement synthesis): waypoint routes on a Subunit (`route`, `_route_idx`, `_resolve_route_goal`, `check_orders` path-length clamp), with two integration fixes.
- **Status:** none stated; reading: live; strong (controls and trace events asserted, waypoints built from the live anchor after a review found fabricated distances).
- **Bears on:** MB (orders, pathing, standing instructions), CHAR/FA (a commander's route is an Order with trigger `immediate`/`tick:N`).
- **Content that matters:**
  - Route is an order-safe field; budget formula `0.5 * speed * ROUTE_BUDGET_TICKS` = 9.0 for infantry (`TICKS_PER_PHASE == 6` asserted as the premise, `ROUTE_BUDGET_TICKS = 3 * 6 = 18`), cavalry gets `MB_CAVALRY_SPEED_MULT` (3.0x) (:79-86, :170-177); a too-long route is clamped to the waypoints inside the budget (not rejected), and a trace event `route_clamped` with `dropped`/`kept` is emitted, none when nothing is dropped (:88-95, :180-200).
  - B is passed before C is reached (anchor-distance record, `tick_at_b < tick_at_c`); with the enemy not in sight and `target_condition='in_range:1'` the route-holder still moves in `run_battle` because `moving_a/moving_b` were widened (:97-141).
  - Abandonment (REVERSED at round 2 on Jordan's correction): an emergent yield, or `stance == 'retreat'`, clears the route and it does NOT resume (trace `route_abandoned` with reason) (:221-263). A waypoint that stalls past the route budget in ticks is force-dropped and the route continues (`route_waypoint_stalled`, :268-289). Re-issuing a route resets the cursor; a resume index is honoured and measured only over the legs ahead; a bare coordinate pair or non-numeric waypoint fails at Order construction (:203-218, :323-355).
  - Legacy-lattice arm (`MB_NODE_COHESION=False`) is documented as "not a way the game can be played, kept only as the byte-exact grid regression oracle"; a route order there must not crash and a route-only atom is excluded from movement (:146-167, :292-320).
- **Conflicts / stale:** none. Confirms the node path is the shipped path and the grid path an oracle.
- **Open items:** `byte-exactness for the untouched default is covered separately by bat.py --check (no BATTERY row sets a route)`: routes are in no golden.

### tests/valoria/test_mass_battle_signals.py
- **What it is:** pytest file, A4 / ED-MB-0067 Part A: go-codes only: an `Order` trigger `signal:NAME` fires once NAME is in the issuing Unit's `fired_signals`, and an order's `fire_signal: NAME` behaviour adds NAME.
- **Status:** none stated; reading: live; messenger latency explicitly out of scope.
- **Bears on:** MB (command and communication between subunits of one unit, order triggers), CHAR/FA (none).
- **Content that matters:**
  - Trigger validation: `signal:advance` accepted; `signl:advance` and `signal:` (empty) raise; `fire_signal` must be a non-empty STRING (int and list raise at Order construction, :43-48, :86-89, :142-151).
  - Behaviour: a `signal:advance` order does not fire before the signal, fires on the next check after `u.fired_signals.add('advance')`, ignores an unrelated signal (:56-81); `fire_signal` adds the name when its own trigger fires and never leaks onto the Subunit (:92-102).
  - Propagation is order-dependent and disclosed: a watcher listed after the signaler sees the signal in the same `check_orders` call; listed before it, one call later (:105-126). `fired_signals` is cleared by `reset_morale_between_battles` (:129-137).
  - Signals are per-Unit transient state: the only "communication" is a shared set, no range, no delay, no loss.
- **Conflicts / stale:** none.
- **Open items:** messenger latency "explicitly out of scope for this item".

### tests/valoria/test_mass_battle_support_rank_cap.py
- **What it is:** pytest file, MB-07 / J-18 (A): cap the depth support stack at the number of ranks a troop type's weapon reaches (`registry.support_weight` is the single owner; `MB_SUPPORT_RANK_CAP` ships ON since MB-07r).
- **Status:** none stated; reading: live; mixes strong structural tests with measured-value pins.
- **Bears on:** MB (formation depth, weapon-reach-derived supporting ranks, troop types), PC (the reach/class idea).
- **Content that matters:**
  - Weapon class to ranks: reach 0.1 gives 1 rank (infantry, non-pole), 0.2 gives 2 (heavy infantry, cavalry, spearmen), 0.3 gives 3 (pike); unmapped = 1; derived from `TROOP_TYPE_REACH` (15 types, `len == 15` pinned), so a reach edit moves its rank (:145-154). A rank past the cap weighs 0 (`support_weight(cap+1, tt) == 0.0`).
  - OFF control reproduces the uncapped stack exactly, with measured float literals as pins: `_UNCAPPED_FULL = {'Line': 560.0000000000002, 'Column': 468.5714285714283}` and eight `_UNCAPPED_BEYOND` values to the last digit, `checked == 8` (:32-40, :86-97): numeric pins taken from a pre-MB-07 commit on Python 3.11.17.
  - Falsifier: a tier-4 Line (7 files x 5 ranks) and Column (5 x 7) with equal troops differ only in depth; uncapped, three of four types differ beyond the cap (infantry ties up to float rounding, asserted `differ == 3`); capped, ranks beyond the cap added to the pool are exactly 0.0 with `removed > 0` anti-vacuity (:102-133).
  - Two `@pytest.mark.slow` tests pin sampled retention values: capped pike 0.9604 > heavy 0.9508 > levy 0.8895 at `abs=1e-4` (and uncapped pike == heavy == 0.9514); standing melee tuples `((0.9588, 0.9151), (0.8851, 0.9697), (0.9415, 0.9527))` by exact tuple equality (:159-196). The docstrings list five re-recordings (POOL_QUALITY_SCALE 0.5 to 0.8 at MB-07r, MB-04 role keywords, ED-MB-0079 cell body becoming a circle one pitch across, 2026-11-01). These are tripwires on one trajectory, not property tests.
  - `resolve_field` at weight 3000 engages 2,700 troops uncapped and 2,000 capped (3 ranks of infantry) (:222-233).
  - `test_shipped_default_is_on` skips if the env var is set ambiently (:80-83).
- **Conflicts / stale:** imports fixtures and helpers (`_charge_vs_brace`, `_standing`, `field_path`) from `test_reach_weapon_class` (:27): cross-file test coupling. The cap is ON by default but the golden battery is pinned to a different configuration (see `test_field_golden_pins.py`).
- **Open items:** none stated.

### tests/valoria/test_mass_battle_yield.py
- **What it is:** pytest file, DG-2 / ED-MB-0005 (proposals/mass_battle_fighting_withdrawal_v1.md, Jordan "build it now" 2026-07-08): the commanded-entry fighting-withdrawal (`yielding`) state, goal, pool malus and facing.
- **Status:** none stated; reading: live; the docstring's scope disclaimer is stale.
- **Bears on:** MB (yield / fighting withdrawal, discipline gate, facing), PC (the duel-level yield is a separate mechanism, `test_combat_yield.py`).
- **Content that matters:**
  - `yielding` defaults False; `yield_active` requires discipline >= `D_YIELD` and a melee `unit_type` (ranged have `kite`) (:42-64). `_yield_goal` is the reflection of the nearest enemy through the anchor (flee vector), only reachable through the node path's `_resolve_maneuver_goal` (:67-88, :119-136).
  - A yielding, sufficiently disciplined subunit fights at `YIELD_POOL_MULT` of its pool, reduced but at least 1; below `D_YIELD` the order is a no-op (:91-109). `yielding` is an order-safe field set by `Order('immediate', {'yielding': True})` (:112-116).
  - Acceptance (§6.b): a yielding subunit's facing stays toward its engaged enemy as it moves away (dot product >= 0 for every cell, :139-171). Two assertions are weak: `assert atk._moved_this_turn or atk.cell_offsets` (:156) is satisfied by any non-empty `cell_offsets` dict, so "never moved" cannot fail [UNVERIFIED that `cell_offsets` is always non-empty]; the per-cell facing loop has no population floor.
- **Conflicts / stale:** the docstring says emergent auto-entry, rally and pocket are NOT built and "should be treated as still-open" (:3-10); `test_dg2_yield_residuals.py` builds and tests all three, and `config.py` ships them ON. Cites `proposals/mass_battle_fighting_withdrawal_v1.md` (live design material per the brief).
- **Open items:** none beyond the stale scope note.

### tests/valoria/test_mass_battle_terrain.py
- **What it is:** pytest file, A7 / ED-MB-0067 Part A / ED-780 / ED-MB-0074 and MB-05 / MB-05r: battle-wide terrain found from the strategic map (province anchor point-in-polygon against the geography file), the six A.9 terrain rows, river-crossing derived from the march origin, and the effects `_run_and_grade` applies.
- **Status:** none stated; reading: live; mixes strong falsifier tests with pins of hardcoded geography ids and with tests of effects nothing reads.
- **Bears on:** MB (terrain), SE (geography, territory ids, fortification), CORE (the host reads geography and passes it in).
- **Content that matters:**
  - Terrain is ONE row for the whole battle (`terrain_row_for_territory(tid, fort_level, river_crossing, geography)`), not per cell: precedence WALLS (fort_level > 0) > RIVER_CROSSING (caller signal) > polygon type via `_TYPE_TO_ROW` > OPEN_FLAT fallback; an unknown territory returns OPEN_FLAT (:89-123). A closed-set test (every province resolves to one of six rows; `len(seen) >= 2`) and a type-coverage test (every geography terrain `type` has a `_TYPE_TO_ROW` entry, since the `.get(..., OPEN_FLAT)` fallback hides a gap, :61-86).
  - Pins of actual data: T4 and T9 UPHILL, T7 and T6 FOREST_BROKEN (marsh maps to forest), T1 OPEN_FLAT; river-crossing for 11 origin/target pairs (e.g. T9 to T3 True, T3 to T5 True through a run-along, T1's anchor ON a vertex: touching is not crossing); a count of bank changes not strict segment crossings; 17 x 17 province pairs with and without `bridges:` give identical answers (MB-05r bridge ruling, `[ASSUMPTION; medium; Jordan to correct]`, `checked == 17*17 and crossings >= 1`, :141-210, :218-227). `NARROW_PASS` is pinned only through a synthetic province at a pass polygon's centroid because the real mountain-pass provinces' anchors lie outside their pass polygons (:230-253).
  - Effects wired in `massbattle._run_and_grade`: UPHILL gives attacker -1D off and defender +1D def; RIVER_CROSSING -1D off on the crosser; WALLS adds `WALLS_DEFENDER_DR` to the defender only (and `walls_dr` int overrides it on a WALLS field only; inert elsewhere); each lands once on the right side (:316-356, :376-391). Falsifier (MB-05): with the row's A.9 dice zeroed the fight equals OPEN_FLAT on all 16 seeds, with canon's dice at least one differs and the defender never has fewer survivors (:406-437). The `resolve_field` test derives the crossing from `origin` over `build_realm(0)` sides (T9 to T3 vs no origin) over 16 seeds, `differs >= 1` (:440-474).
  - Inert effects, stated in the tests: the FOREST_BROKEN "cavalry to Standard" speed write and the RIVER_CROSSING speed step are written but `run_battle` never reads `.speed`, so they change nothing; NARROW_PASS is identified and not applied; the tests pin the writes "the day a reader exists" (:297-313, :393-403). `_run_and_grade` mutates the passed units' `dr` and `speed`.
- **Conflicts / stale:** the docstring says canon's citation `designs/territory/...::terrain_polygons` is stale in path and key; the geography YAML is `systems/settlements/valoria_geography_v30.yaml` [UNVERIFIED current path]. Unfortified ground is "dominant polygon" by anchor point-test, not by area (disclosed).
- **Open items:** forest/river speed effects and the narrow pass have no consumer; battle-wide terrain means no cell-level terrain exists in this path (relevant to the "terrain-bearing battlefield" intent).

### tests/valoria/test_module_registrar.py
- **What it is:** pytest file, 597 lines (plan position `30`, A-25, ED-IN-0284/0285; extended at `31a`, `31b`, `31c`, IN-41, v9 IN-07): one planted violation per refusal, each in a FRESH SUBPROCESS, against `SeasonDriver(World(0))` construction.
- **Status:** none stated; reading: live; strong (a falsifier per refusal, derived-not-named subjects, `checked` counts).
- **Bears on:** CORE (registrar, composition rows, prize rows, verb table, effects, preconditions), PC/MB/SC (the three prize-named entry rows), SE (role-less settlement entries), PROCESS.
- **Content that matters:**
  - Why subprocess: `MODULE_ENTRIES` (`engine/season/manifest/registrar.py`), `PROVIDERS`, `EFFECTS` are process globals other tests can fill; each case runs `python -c` with a 600 s timeout and `eval`s its own repr (:89-94), which is about 30 interpreter spawns in the file.
  - Registrar: a row with `entry:` is registered by string at driver construction (not at import), idempotently (:134-158); deleting a registered row under a live process refuses naming it (within-process form, :161-174); deleting a production row in a fresh process refuses via the prize row's `module_entry:` (`manifest/registry.py::check_contest_prizes`), once per prize-named role, floor `len(named) >= 3` (the rows are `social_contest.roll`, `combat.fight`, `mass_battle.resolve_field`, :185-211). Host-declared role-less needs (`world_q.QUERY_ENTRIES` + `matter.STEP_CALLS`, floor `>= 8`, e.g. `settlements.larder_draw`, `.subsist`, `.produce`, `.housing`, `.fabric`, `.fortification`) are refused if deleted, stripped of `entry:` or re-kinded, `checked == 3 * len(needs)` (:222-259).
  - Agreement refusals: composition target in a module other than the prize row's `module:` ; verb bound to a prize that does not name the entry (rows swap verbs to dodge the one-entry-per-verb refusal first); `verb_call` naming no verb; one entry registered twice (two rows one target, two rows one verb with `[ASSUMPTION, SM-5]`, a second writer showing both entries whole) (:262-348).
  - Verb-row refusals: a prize row with its provider cleared; a verb contesting a prize no row claims; a writing row whose effect is cleared (names `effect_decline_note`); `effect_decline_note` on a row that has an effect or that writes nothing; an untyped precondition nothing evaluates; a stale `requires_decline_note` (:351-501). Subjects are chosen from the tables, never named (no entity special-cased).
  - Sweep honesty: since v10 REM-2B no shipped row is dropped on its precondition, so `test_every_shipped_row_dropped_on_its_precondition_says_why` is vacuous on the shipped tree and is kept able to observe by planting a dropped row with and without a note (:504-535). The populated-realm test wraps the five check functions and asserts each RAN and the registrar registered every production `entry:` row (:538-565). `tools/export_composition.py --check` round-trip returns 0; the exporter refuses 8 malformed `entry:` shapes (:568-596).
- **Conflicts / stale:** the docstring cites positions that "left the plan at B-B's close, `4a2e4494`" and `ID-13` history; `refusal` kind is asserted to be `"Unspecified"` (:99), an exception class name.
- **Open items:** `SM-5` (a grid or map variant as its own module) could change the two-rows-one-verb rule.

### tests/valoria/test_module_shape_check.py
- **What it is:** pytest file for `tools/ci_module_shape_check.py` (ED-1085), the module-shape hygiene guard: synthetic trees in `tmp_path` exercise its rules (no `sys.path` reach-in to `tests/`, no `import tests...` in runtime code; `workbench` and `tests` excluded).
- **Status:** none stated; reading: live; process only, over a checker whose subject is repository hygiene.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Five synthetic cases (clean passes; `sys.path.insert` into `tests/sim/v32-combat-balance` flagged as a reach-in; `from tests.sim import thing` flagged; `workbench/` and `tests/` excluded; a non-`tests` path insert allowed) (:26-77). The checker is pointed at the temp tree by swapping `shape.REPO_ROOT` (:18-23).
  - The tmp layouts use roots `sim/autoload`, `sim/personal`, `systems/combat/combat_engine_v1/...`; the checker's `RUNTIME_ROOTS` still lists `'sim'` and `systems/combat/combat_engine_v1` (verified in `tools/ci_module_shape_check.py:49-54`), though `sim/` is a dissolved tree (CLAUDE.md §3).
- **Conflicts / stale:** the `sim/` root and the frozen `tests/sim/v32-combat-balance` station are named in the checker as patrolled/forbidden; the former no longer exists.
- **Open items:** none.

### tests/valoria/test_modules_reachable_closure.py
- **What it is:** pytest file, SM-7 at plan position `31c` (IN-05): `modules/**` equals the reachable import closure of the composition entry rows, in both directions.
- **Status:** none stated; reading: live; load-bearing on the port (GO-05's manifest lists `modules/**`); has a planted falsifier.
- **Bears on:** CORE (composition rows, A-25 modules), GO (the port's input set), PC (flat module set), MB, SC, FI, SE (every module directory).
- **Content that matters:**
  - Roots are composition rows with `entry:` targeting a package under `modules/`; the walk follows every import (module-scope and function-local) to repository `.py` files, stops at `engine/` (the host is not module code). Direction 1: every `.py` under a module directory is reached; direction 2: nothing reached lies under `systems/` (:94-114, :146-154).
  - Two shapes told apart by whether an `__init__.py` exists: packages (`social_contest`, `mass_battle`) and the FLAT script set `modules/combat/`, whose roots are the entry plus the names `engine.substrate.pc_engine.PCEngine._fields` declares; a flat directory with no declaring seam fails; a bare name resolving nowhere and not stdlib/installed is reported (:139-143, :174-199).
  - Also asserted: no entry row targets outside `modules/`; no directory or loose file under `modules/` that no entry row names (so `modules/` holds the entries' closures only); non-vacuity: `modules/mass_battle` is in the package list and `modules/combat` in the flat list (:157-199). `modules/` currently holds `combat, fieldwork, mass_battle, settlements, social_contest`.
  - Planted-tree falsifier proves it sees an orphan file, a lazy import into `systems/`, a flat-set unresolved bare name and an unreached flat file (:202-229).
  - Not checked (stated): DATA read by path; the geography read moved to the host (`engine/season/data/geography.py`) and `engine/season/tests/test_mass_battle_module.py` is cited as the observer that the module opens no file.
- **Conflicts / stale:** `fieldwork` and `settlements` appear under `modules/` but the file names only the three modules in non-vacuity asserts.
- **Open items:** none.

### tests/valoria/test_morale_write_sweep.py
- **What it is:** pytest file, ED-MB-0042 sweep: every absolute morale write in mass battle must reach the cells (`set_morale`, `erode_morale`, `pull_morale`), plus a field-parameterised guard failing on a NEW bare `.morale =` assignment on the engine path.
- **Status:** none stated; reading: live; the template §0.1 pt 1 cites; one of the KEPT guards.
- **Bears on:** MB (cell-owned state: `eff_morale` reads cells, `cell_morale`), CORE (read/write asymmetry hazard).
- **Content that matters:**
  - The failure: `eff_morale` reads CELLS once seeded and never falls back to the scalar, so every bare `.morale =` became a silent no-op under `MB_CELL_MORALE` (which confounded the flag's first measurement and the flip was retracted). Behaviour tests, each parametrised over an `own`-morale and an `inheriting` subunit (each param asserts which branch it is on): battle reset restores a damaged body; between-turn recovery is a bounded increment and must not re-inflate (a defect the author introduced mid-sweep); a body-wide hit moves cells by exactly its amount; `Unit.set_morale(0.0)` reaches an inheriting body (Command=0 instant rout depends on it); `set_morale(3.0)` sets every cell (:85-134).
  - The sweep: `_CELL_OWNED = {'morale': {'owners': ..., 'allowed': {...}}}` with a line-anchored regex over eight engine files, `_ENGINE_FILES` (orchestration, battle_loop, core/state, core/exchange, hierarchy/units, percell, resolution, and the harness `lanchester_signature.py`); allowed bare writes are annotated by reason (:139-255). The regex was repaired to see a compound statement (`a = f(); a.morale = x`) after mutation testing; `test_the_guard_itself_can_fail` plants a plain and a compound line and requires both to match and not be allowed (:258-278). `morale_start` is out of scope by construction (the pattern is name-bounded), and two whitelist entries written for it were removed after mutation showed they exempted nothing.
  - Comments record that phase 3 will move stamina, discipline, quality, and phase 4 hp and armour onto the cell (not done: only `morale` has a `_CELL_OWNED` key), i.e. today only morale is per-cell state in the guard's registry.
- **Conflicts / stale:** `test_persubunit_stress.py` holds one bare morale write and is deliberately out of scope ("it gates the eventual default FLIP"; plan-v2 A5b); it lives in `systems/mass_battle/sim/` (seen in that directory). A text guard over eight hardcoded paths.
- **Open items:** "It stays on the re-flip checklist in HANDOFF_MB" (A5b).

### tests/valoria/test_names.py
- **What it is:** pytest file: `tools/names.py` loader/resolver and `tools/ci_naming_check.py` (the Solmund-vs-deprecated-name gate): block tier vs warn tier, fail-safes, exclusions.
- **Status:** none stated; reading: live; process (naming gate), with several behaviour-based falsifiers.
- **Bears on:** PROCESS (naming), CORE (names index).
- **Content that matters:**
  - Loader on a synthetic `names_index.yaml` (canonical/aliases/legacy/enforce; `key_for` resolves canonical or alias; missing file returns `{}` not raise, :44-70). The live gate loads the block tier from the real index and the deprecated proper noun is among the block-tier legacy names (:75-90).
  - Tier separation: neither tier's names are caught by the other tier, with both tiers asserted non-empty first (`test_the_two_tiers_do_not_bleed_into_each_other`, :116-131). An empty BLOCK tier means `main([])` returns 1; an empty WARN tier is the legitimate end state (returns 0) unless the index is unreadable (then 1); rewritten from a source-text assertion to a behaviour test after an adversarial pass (:134-171).
  - The block scan returns strings (the edit-time hook slices `h[:120]`) and ONE hit per line even with two block names (a second name is planted, :174-198). The audit-corpus exclusion is rooted: `.audit/...` and `tests/` and `engine/tests/` excluded, `skills/valoria-vector-audit/scripts/...` not (:201-216).
- **Conflicts / stale:** the test strings use the deprecated name by design (the index exempts itself). Uses `designs/x.md` as a notional path.
- **Open items:** none.

### tests/valoria/test_names_chain.py
- **What it is:** pytest file: the naming chain `references/names_index.yaml` -> `tools/export_names.py` -> `names.json` -> `engine/substrate/names.py` leaf: refusals planted and asserted.
- **Status:** none stated; reading: live; load-bearing on the engine (artifact read at import).
- **Bears on:** CORE, CHAR (attribute names and aliases), FA (faction roster derivation), PROCESS.
- **Content that matters:**
  - Leaf refusals: `canonical_for` raises ValueError on an ambiguous display string; `N.AMBIGUOUS` is pinned as `{"Order", "Reason"}` (a conviction/settlement-stat pair and the attribute `attr.mind.acuity`/`conv.reason` pair, joined at CR-84) and the error must name both claimants (:30-49). Legacy tag raises and names its replacement (`N.LEGACY` non-empty precondition); an unknown name raises and names `names_index.yaml` (:118-135).
  - Alias preservation: 17 pre-CR-84 names resolve to the same key through `_names_lost()`, with a planted control (drop `Dexterity`) naming it; `Perception` is its own canonical; the `Reason` group is held by the attribute row, not `conv.reason` (:52-115).
  - Faction roster: `rosters.yaml: factions` carries `from_names: faction` and no `values:`, so `set(N.FACTIONS) == set(rosters.FACTIONS)`; the roster size is deliberately NOT asserted (Jordan 2026-09-19: "faction count should not be pinned"); named members `Schoenland, Church of Solmund, Valorsmark, Guilds` must be present; `Crown` is Valorsmark's alias (CR-86) (:145-167).
  - Exporter refusals each planted in a temp copy of the index and run in a subprocess: alias resolving to two canonicals ("resolves to BOTH"), alias shadowing a canonical, legacy tag also a live alias, legacy tag shadowing a canonical (:191-235). `tools/export_names.py --check` returns 0 (:238-244).
  - Retired: the Key-type flow-list tests were deleted with the Key substrate (:252-260).
- **Conflicts / stale:** the precedent "faction count should not be pinned" (here) vs `test_conviction_roster_single_owner.py:64` which pins `len(PURSUITS) == 15`, `test_descriptor_registry.py` which pins ten attributes, and `test_descriptor_registry_category_b.py` which pins eight entries: pins on rosters are treated inconsistently.
- **Open items:** none.

### tests/valoria/test_no_polling_triggers.py
- **What it is:** pytest file (ED-IN-0084, CLAUDE.md §11): `.claude/settings.json` `permissions.deny` covers every self-scheduling primitive, MCP server-name spellings, hooks survive; CLAUDE.md carries the rule.
- **Status:** none stated; reading: live; guards an AGENT-instruction (Layer 0) artifact, no game bearing.
- **Bears on:** PROCESS.
- **Content that matters:**
  - `REQUIRED_DENY` (the sole owner of the roster): `send_later, create_trigger, ScheduleWakeup, CronCreate, update_trigger, fire_trigger, Skill(loop), watch_url, subscribe_pr_activity`; each must appear in the deny blob (substring over `str(d)`, :101-106); five tools must be denied under all three spellings of the `claude-code-remote` MCP server (:109-121). `Monitor` and `create_session` are deliberately not denied, with reasons (:68-78).
  - `Skill(loop)`'s runtime spelling cannot be executed by the test (stated blind spot, :80-85); no test can observe a hosted session calling the tool (:24-30).
  - Hooks: the PreToolUse naming guard is wired and its `tools/...` target exists; `SessionStart` and `Stop` are pinned EMPTY (no banner, CLAUDE.md §0.3) (:124-164); CLAUDE.md contains `does not self-schedule` and `ED-IN-0084` (:167-171).
  - Cost anecdote in the docstring: 116 `send_later` firings, floor ~2.7M tokens; CLAUDE.md measured 19,228 tokens before a cut.
- **Conflicts / stale:** none.
- **Open items:** none.

### tests/valoria/test_octagon_damage.py
- **What it is:** pytest file, ED-MB-0018 (Jordan 2026-07-22), isolation fixed by ED-MB-0063: the octagon facing arc is a DAMAGE-RECEIVED multiplier (front GREEN 1.0x, flank YELLOW 1.5x, rear RED 2.0x), not a dice-pool penalty; reaction delay; multi-side shock.
- **Status:** none stated; reading: live; honest about two of its tests (one admits it does not observe the window it names).
- **Bears on:** MB (facing, flanking, du Picq flank/rear lethality, Cannae, per-cell perimeter faces), PC (none).
- **Content that matters:**
  - Requirements asserted: (1) a pure rear strike deals exactly 2.0x the identical frontal strike for the same seed (`rear == approx(2*front)`, `checked >= 3`; measured 7 of 12); (2) a cell hit outside its front arc keeps its exposed facing until `FACING_REACTION_TICKS` and a rear (blind-arc) strike is never perceived; (3) a subunit engaged from two or more distinct FACES (front/rear/left/right nearest-perimeter-face) takes an extra `(1 + MULTI_SIDE_SHOCK)` factor, while two co-front bodies are one face (:1-16, :344-380).
  - Isolation (ED-MB-0063): earlier tests flipped `advance_dir` so the two arms contacted different ranks (rank 0 vs rank 2 of a 3-rank body); the pool is support-depth weighted (`SUPPORT_WEIGHTS {1:1.0, 2:0.7, 3:0.5}`, contact rank 0 = 3.6 of 4 vs contact rank 2 = 1.333), so the "rear does less than front" failure was a test-premise defect; the helper `_arc_pair` now holds the body fixed and rotates only `cell_facing_vec`. The docstring concedes that with the body fixed `rear == 2*front` is arithmetically forced wherever `front > 0`; the real falsifier is `test_arc_ratio_is_invariant_to_the_fractional_pool_flag`, parametrised over `MB_FRACTIONAL_POOL` 0/1 (:128-244).
  - `test_rear_penalty_persists_across_reaction_window` states it DOES NOT observe the window it names: `_arc_pair` builds a fresh Subunit per call so the consecutive-tick counter never exceeds 1 while `FACING_REACTION_TICKS` is 2 (critic finding A, pre-existing, "not fixed here", :273-305). `test_visible_flank_refuses_after_delay` ticks a persistent subunit and asserts the counter in `_react_since` reaches the threshold (:308-328). The reaction clock is cleared by `reset_morale_between_battles` (:383-396).
  - Front never exceeds rear/2 (conditional on `rear > 0`, `checked >= 6`, measured 9) so wing cells stay GREEN (local attacker centroid) (:246-270). Multi-side shock seed re-picked at MB-07r because at seed 13 both arms read 0.0; mutation recorded (:352-357).
  - Fixture hygiene: `_mb_modules` reloads `config`, `units`, `orchestration`, `contact` under an env flag set and rebuilds from the restored environment afterwards; measured on `main`: the pair `test_stochastic_rout.py` alone fails one test, the pair with this file fails a different one, so verdicts depended on order and `-n auto` worker mix (0-2 unstable failures, :52-71). The test sets `U.FIELD_MOVEMENT = False` (discrete lattice contact) for determinism.
- **Conflicts / stale:** cites `audit/2026-07-30-mb-session-retrospective/00_lessons.md` (archived). The legacy `-2 dice` path (`MB_OCTAGON_DMG=0`) is "asserted byte-unchanged by the existing bat.py digest" (outside this file). Fixture forces the grid/lattice arm, so the facing multiplier is tested where the shipped path is node (see `test_face_aggressors.py`) [UNVERIFIED that the multiplier code is shared].
- **Open items:** the persistent-subunit form of the blind-arc test is "a separate change with its own expected-delta".

### tests/valoria/test_pathres.py
- **What it is:** pytest file: canary corpus for `tools/pathres.py`, the path-resolution owner (ED-IN-0128, ED-IN-0133, D1): extraction anchors, constructed-path reconstruction, ledger alias/fork resolution, I/O tracing.
- **Status:** none stated; reading: live; process only (no game bearing). It carries its own disclaimers ("THIS GUARD PROVES LESS THAN IT DID", :43-49).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Each fixture binds one branch of `pathres` to one historical defect (table at :6-14): a `.audit/` token must not be extracted from `vector-audit/scripts` (now impossible by spelling since the `audit/` -> `.audit/` rename; the anchor still protects future roots); a joined `os.path.join(..., '.audit', ...)` is reconstructed and a variable segment is skipped, not guessed; a glob is captured whole.
  - Resolution: `params/core.md` resolves to FORKED (the tree evacuated), `references/params_core.md` is a two-hop chain, `max_hops=1` yields DEAD (the dependency checker's single-hop behaviour), a mapped prefix with an absent target is DEAD, a live path needs no alias, a glob is LIVE via `resolve_glob` (:94-141). A `Resolution` is not a string and has no truth value (`bool()` raises TypeError), `same_file` compares resolved targets (:148-167).
  - I/O tracing classifies read/write/scan/delete, ignores a comment mention, follows a module constant, and is non-vacuous on `tools/export_descriptors.py`; a dynamic `open(os.path.join(REPO, rel))` returns nothing and that "blind spot" is pinned so the "lower bound" caveat stays honest (:174-245).
  - Map size floors: `len(exact) > 100`, `len(prefix) >= 10` (:252-256). D1: `broken_dependency_checker._resolve_remap` and `pathres.resolve(max_hops=1)` agree on every FORK row (floor `len(probes) >= 300`, `agreed >= len(probes) - 5`, disagreement allowed only where the path still exists on disk); a repeated ledger key resolves to the LATER row (`designs/arcs/`); `fork_pointer` is idempotent (:268-352).
- **Conflicts / stale:** the corpus is built on dissolved paths (`designs/`, `params/core.md`, `.audit/2026-06-03-contest-groundup/engine.py`) as intended test data; one example cites the retired `engine/substrate/keys.py`. This is a test of a process tool that reads `restructure_ledger.md` (permitted by §0.05 cl. 4).
- **Open items:** CLAUDE.md §8 records that `pathres.resolve()` matches directory prefixes; this file's docstring (:122-128) uses that behaviour as a feature.

### tests/valoria/test_per_die_one_owner.py
- **What it is:** pytest file, REM-42: within `engine/dice_engine/` the per-die mean and sigma are defined once in `dice_engine.py` and `sigma_leverage.py` reads them.
- **Status:** none stated; reading: live; small and strong (a mutation test in a fresh interpreter).
- **Bears on:** DICE, SC (`sigma_leverage` is the social-contest surface), MB (the exception).
- **Content that matters:**
  - `sl.PER_DIE[7] == (de.MU_PER_DIE, de.SIGMA_PER_DIE)` and the two module aliases equal the owner (:25-33). The mutation: in a subprocess set `de.MU_PER_DIE = 0.55`, `de.SIGMA_PER_DIE = 0.91`, then import `sigma_leverage` and require `(0.55, 0.91) 0.55 0.91`, which a copy would not follow (:36-48).
  - It states `modules/mass_battle/` "keeps values of its own and is not asserted" (:2): verified, `modules/mass_battle/config.py:302` defines `PER_DIE_NET_EV = 0.4` (tagged `canonical: params/core.md`) beside `dice_engine.MU_PER_DIE = 0.40` (`engine/dice_engine/dice_engine.py:181`): a second owner of the same constant, equal by value.
  - `SIGMA_N_COEFF` (0.8) is a different quantity, not asserted here; `PER_DIE` keyed by TN is pinned in `test_tn7_always.py`.
- **Conflicts / stale:** the MB per-die constant is not routed through the dice owner and is held equal by nothing in this file.
- **Open items:** none.

### tests/valoria/test_perimeter_geometry.py
- **What it is:** pytest file: Jordan's 2026-07-23 perimeter target-point / face-normal geometry primitive (`modules/mass_battle/perimeter.py`) validated against real formation footprints (`CELL_PATTERN_FN`).
- **Status:** none stated; reading: live; pure geometry, no RNG, no goldens.
- **Bears on:** MB (formation shape as a polygon of cells; attack-face choice; approach alignment; sharp tips of wedge formations).
- **Content that matters:**
  - A `Line` footprint is a 4-face rectangle with 4 major (face-mid) and 4 minor (corner) target points, unit normals pointing outward, no sharp tips (corners at 90 degrees); face normals cover the four cardinal directions (:25-48). An `Arrowhead` (depth 5) has a 3-face hull with at least one sharp vertex (<= `SHARP_TIP_DEG`, 60 degrees) (:51-60).
  - `nearest_target` picks the face an attacker approaches (north attacker gets the north face, normal toward the attacker, :63-75); `approach_alignment` is +1 square-on, 0 grazing, -1 from behind (`approx(abs=1e-6)` on trigonometric results, :78-90); a degenerate footprint (under 3 cells) returns no face and one major target; the primitive is order-independent (:93-105).
  - Only `Line` and `Arrowhead` are tested; `GappedLine` and `Column` shapes (which `test_deployment_primitives.py` builds) have no perimeter test.
- **Conflicts / stale:** none.
- **Open items:** none.

### tests/valoria/test_reach_weapon_class.py
- **What it is:** pytest file, spatial-model v2 Stage E / ED-MB-0014 (Jordan P-DEC-1): per-troop-type front-face reach (non-pole melee 0.1, pole/spear 0.2, pike 0.3, lance 0.2, ranged = projectile band + a 0.1 melee sidearm) and the authored `pike` troop type.
- **Status:** none stated; reading: live; helper functions (`_standing`, `_charge_vs_brace`, `field_path`) are imported by other test files.
- **Bears on:** MB (reach as a weapon-class datum on the troop type, charge/brace, pike), PC (reach as a weapon property), CHAR (none).
- **Content that matters:**
  - `reach_for(t)`: levy and light infantry 0.1, heavy infantry 0.2, pike 0.3 (strictly longest), cavalry and knights 0.2, archers and crossbow 0.1, bare `infantry`, unknown and `None` 0.1 (:58-72). Pike stats mirror heavy_infantry so reach is the sole differentiator; its `loadout_for` weapon has `reach == 'melee'` and keyword `pole`; allowed roles include `ShieldWall` and `Anvil` (:75-84). `loadout_for(troop_type)` returns ONE (weapon, armour) pair per troop type.
  - Reach advantage emerges through the charge-recoil gate (`MB_RECOIL_CHARGER_GATE`: a braced defender whose reach >= the charger's repels the charge): pike and heavy infantry out-retain levy by more than 0.02 over 16 seeds, and pike equals heavy to 1e-6 ("cap OFF fact"); the test pins the uncapped support stack with an `uncapped` fixture because with the cap ON they differ (`test_mass_battle_support_rank_cap.py`) (:119-145, `@pytest.mark.slow`).
  - Disclosed finding: standing melee is UNCHANGED by reach (exchange is mutual once contact fires; reach shifts only contact timing): `_standing('pike','levy') == _standing('levy','levy')` exact equality of 4-dp-rounded means, uncapped (:147-155). Reach is a charge/brace lever, not a standing-melee lever.
  - Facing: a cell facing away gets zero reach, in front the full base (`_hu._effective_reach`, exact `==`); archers' volley range `VOLLEY_MAX_RANGE` exceeds and is independent of their 0.1 melee sidearm reach (:160-178). Conservation with a pike unit (seeds 3, 19, 44) via `assert_troop_conservation`, `checked >= 2`; of four conservation sites this is the only matchup that routs (8 routed units over 60 seeds); determinism (:183-213).
- **Conflicts / stale:** none. The 0.1 "melee sidearm" for archers is a reach datum only; there is no sidearm weapon state, switch or cost in the tested code.
- **Open items:** none.

### tests/valoria/test_references_yaml_parse.py
- **What it is:** pytest file (ED-IN-0121): every machine-read YAML register under `references/` and `registers/` must parse with `yaml.safe_load`.
- **Status:** none stated; reading: live; cheap and general (process data hygiene).
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - One parametrised case per file from the globs `references/**/*.yaml|yml`, `registers/*.yaml|yml`; floor `len(files) > 20` (:36-47). Origin: `references/npc_registry.yaml` had an unquoted colon (`faction: Church (dual-loyalty: ...)`) and was unparseable for its whole history with zero Python loaders (:3-12).
  - Deliberately no schema or content check (:19-21). The module uses `pytest.importorskip('yaml')`, so a missing PyYAML skips the whole file silently (CLAUDE.md §8 says a fresh container has pyyaml only).
- **Conflicts / stale:** `references/npc_registry.yaml` is named as having "zero Python loaders" at that time; whether that is still so [UNVERIFIED].
- **Open items:** none.

### tests/valoria/test_reserve_commit.py
- **What it is:** pytest file, PP-MB-04 / PP-499 / mass_battle_v30 §A.6 / ED-MB-0023: a unit in Reserve cannot engage turn 1 and commits at Phase 3 of the next battle-turn (`RESERVE_COMMIT_TURN = 2`).
- **Status:** none stated; reading: live; the docstring's "default OFF" is stale.
- **Bears on:** MB (reserves, multi-unit battle turns), CHAR/FA (a commander's reserve instruction).
- **Content that matters:**
  - `unit_in_reserve(unit)` is true for `instructions=('reserve',)` and false for `('hold',)` (:46-53). With the gate ON a reserve pair has no engagement on turn 1, no `reserve_commits` key; turn 2 records the commitment (`pair` 0) and engages; OFF the pair engages from turn 1; a battle with no reserve unit engages turn 1 either way (:56-86). Each case builds a one-pair `run_multi_unit_battle` with `max_battle_turns=6` and seed 77.
  - Gate toggling reloads five modules (`config, resolution, units, engine, orchestration`) via env `MB_RESERVE_COMMIT`, and `teardown_module` reloads with the flag OFF (:19-31, :89-91).
- **Conflicts / stale:** `test_field_golden_pins.py:283` lists `MB_RESERVE_COMMIT` among the flags Jordan's flags-ON ruling turned ON, so this docstring's "GATED (default OFF)" is stale and `teardown_module` leaves the process at OFF [UNVERIFIED current config default]. The docstring itself says `run_multi_unit_battle` is not in the bat.py golden battery. The first test line `_, _, O = _reload(on=True), None, None` is a no-op expression.
- **Open items:** none.

### tests/valoria/test_registry.py
- **What it is:** pytest file for `tools/registry.py`, the facade over `tools/names.py`, `tools/descriptor_registry.py` and `tools/quantity_registry.py`: reuse by identity, `resolve()` pinned on verified terms, disagreement disclosure.
- **Status:** none stated; reading: live; tooling over name/descriptor registries (not engine).
- **Bears on:** PROCESS, CORE (name/descriptor vocabulary), CHAR (attribute resolution).
- **Content that matters:**
  - Reuse by identity: `registry.names is real_names` etc. (:51-69). `resolve('Strength')` is `kind=descriptor`, key `attr.body.strength`, `via=descriptor_registry`; `Dexterity` alias to agility; `Solmund` is `kind=name`, `registry_key world.solmund`; `Thread Sensitivity` resolves to `prac.thread_sensitivity` (section `practitioner_stats`) and `Fort` to `terr.fort_level` (`territory_stats`) via the descriptor registry's non-attribute index (:74-162).
  - Standing live disagreement pinned green: `Thread Fatigue` is `thread.thread_fatigue` in names but a keyless hit in `quantity_registry`, and the facade discloses both (:185-196); other disagreement arms use monkeypatched resolvers (:253-301). `collisions()` entries are lowercase, sorted, and have at least two distinct keys, a loop with no population floor (:173-182).
  - Retired subject: the `Influence` and `legitimacy` collisions went with `fac.*` rows at plan position 29b (:166-171).
- **Conflicts / stale:** three overlapping resolvers (names, descriptor registry, quantity registry) plus this facade, each with a different scope: the facade is a fourth layer disclosing disagreements between the three rather than removing them. [`Legitimacy`: see `test_names_chain.py`'s ambiguity set `{Order, Reason}`.]
- **Open items:** none.

### tests/valoria/test_season_invariant_sweep.py
- **What it is:** pytest file, M1 row 5 ("N seeds, zero invariant violations"): `engine/season/harness/invariants.py` sweep plus one planted mutation per predicate.
- **Status:** none stated; reading: live; the mutation half is the best-built in the tree per the addendum (F-TEST-06).
- **Bears on:** CORE (invariants over a played season), CHAR/FA/WR (tenures, offices, claims, bodies, stance rows).
- **Content that matters:**
  - Eight invariants: `tenure_interval, tenure_referent, log_ids_unique, log_not_from_the_future, claim_not_from_the_future, body_in_range, stance_row_shape, office_singly_held`; each has a mutation that must make exactly its own predicate fire with a message attributed to it; `test_every_invariant_has_a_mutation` asserts the mapping is total in both directions (:141-205).
  - Anti-vacuity: `sweep` reports `examined` rows per carrier and `unexercised` carriers; on the headless world it asserts `"offices" in unexercised and "stance_rows" in unexercised` and `examined['events'] > 0 and ['tenures'] > 0` (:37-58): the test PINS that the headless world has no Office and no stance row (F-TEST-06); an empty `World` names every carrier unexercised with no violations (:60-70). An earlier entity set missing `w.records` produced 176 invented violations across 24 seeds; the set is pinned against `World._STATE_COLLECTIONS` and the old `petitions`/`dispensations` stores are asserted gone (:103-136).
  - `test_the_engine_is_clean_under_the_sweep`: 12 seeds x one headless season, no violations and none declared; `DECLARED` is empty and each future entry must cite `ED-` or `F...` (:73-100). A broken world reaches the sweep's violation list (3 broken worlds give at least 3 violations, :208-217).
- **Conflicts / stale:** the instrument runs the headless world (about 0.13 s/season) not the realm; per the addendum a realm season (34 offices, 79 stance rows) is clean in 0.7 s but no test asserts it.
- **Open items:** the sweep's coverage of Offices and stance rows on a played world is the F-TEST-06 fix (T3 row 4).

### tests/valoria/test_season_providers_are_registered.py
- **What it is:** pytest file: importing `engine.season.seam` alone must register every wrapper provider (contest/personal_combat, contest/social_contest, contest/mass_battle, inquiry/...), and emptying the table must refuse driver construction; FI-02/FI-03 `inquiry` role refusals.
- **Status:** none stated; reading: live; load-bearing on the game (an unregistered provider used to remove a verb silently).
- **Bears on:** CORE (manifest, providers, seam), PC/SC/MB (contest providers), FI (the `inquiry` role).
- **Content that matters:**
  - The defect was real: on 2026-09-11 cutting an import cycle left `PROVIDERS` empty, `resolvable_verbs()` returned 17 not 18 and `tell` executed 0 times in `tiny_world` vs 32 over ten seasons, with no error. Test 1 (fresh subprocess, `import engine.season.seam` only) asserts `contest/personal_combat` and `contest/social_contest` registered, `contest/mass_battle` and an `inquiry/` entry named by the prize rows, and every named provider registered (:52-75).
  - Test 2 clears `PROVIDERS` and `MODULE_ENTRIES` after a driver was constructed: construction must refuse naming the prize ("nobody registered"), and `resolvable_verbs()` must not move (the old silent path is gone) (:99-123).
  - `inquiry` role (v9 FI-02 / FI-03): `check_rows()` yields one pair per row of the role's roster; deleting a row's composition entry refuses naming it; a misspelled module refuses naming roster, key and spelling; four `check_inquiry_modules` plants run in ONE fresh process and read by four tests: row with no `module_entry`, unregistered provider, provider without the `module_entry` keyword, row keyed on a covert kind no graded inquiry emits, row keyed on an `undeposited_kinds` kind (WITNESS drops it before the found deposit) (:151-315). Each carries a "RED WHEN PLANTED (run 2026-10-17)" note in prose, not re-run by the test.
  - Imports `_run` from `test_module_registrar` (cross-file helper).
- **Conflicts / stale:** `04 PART E step 10` and the plan positions are prose referents. The `Unspecified` exception class name is asserted as a string.
- **Open items:** none.

### tests/valoria/test_stochastic_rout.py
- **What it is:** pytest file, ED-MB-0031 / ED-MB-0041 (Jordan historical research 2026-07-23: "routs would occur as early as 15% losses with 30% the upper hand"): a stochastic per-subunit rout breakpoint drawn in a 15-30% casualty band, discipline-skewed.
- **Status:** none stated; reading: live; its two long docstrings about `MB_CELL_MORALE`'s default are STALE (and the second states a conclusion that the current config reverses).
- **Bears on:** MB (morale, rout, casualty band), SC (none).
- **Content that matters:**
  - `MB_STOCHASTIC_ROUT is True` (ratified ON at ED-MB-0041 after a casualty scoreboard showed the loser at 61-87% against the band's 15-30%; flip dropped win-share count 10/20 to 7/20); `ROUT_ONSET_FRAC` 0.15 and `ROUT_CAP_FRAC` 0.30 pinned; the draw lies in the band for discipline 2..5; resilience rises with discipline; mean breakpoint at discipline 5 exceeds discipline 2 by more than 0.01 over 200 draws; a pinned breakpoint 0.20 breaks at 25% not at 10% (:36-89).
  - `test_loser_breaks_near_historical_band`: loser mean casualties over 16 seeds greater than 60% with the gate OFF and under 45% ON (difference over 30), PINNED to `MB_CELL_MORALE=False` (:92-138). `test_per_cell_break_subsumes_the_body_level_one`: with cells ON the two arms differ by under 10 points and cells alone hold the loser under 45% (:141-169). Both swap module globals `S.MB_STOCHASTIC_ROUT` and `U.MB_CELL_MORALE` and restore them.
  - The docstrings (corrected 2026-07-29) say per-cell morale is default OFF ("`config.py:100` reads ... '0' RETRACTED") and conclude `MB_STOCHASTIC_ROUT` is "the single mechanism keeping shipped battles out of the ~90% grind". Verified in source: `modules/mass_battle/config.py:106` now reads `MB_CELL_MORALE ... '1'` (default ON, "back ON once E..."), `MB_STOCHASTIC_ROUT` default '1' (:181). So in the shipped configuration cells carry morale, the per-cell break fires first, and by this file's own measurement the body-level flag then does nothing (off vs on within 10 points): the "retirement candidate" reading the docstring called "false and inverted" is, on the current default, the live one. The headline test pins the unshipped arm (`cells=False`).
- **Conflicts / stale:** as above; `_SIM` path points to `tests/sim` (unused). The pair `test_octagon_damage.py` + this file was order-dependent through module reloads (see that entry).
- **Open items:** whether `MB_STOCHASTIC_ROUT` still has a live role under the shipped `MB_CELL_MORALE` default; no test measures the shipped-arm effect (cells ON) beyond the subsumption assertion.

### tests/valoria/test_stubwire.py
- **What it is:** pytest file (ED-IN-0091, P1): falsifier tests for `engine/substrate/stubwire.py`, the stub-wire primitive (`stub_resolve`, a frozen `StubResult`, an `invocations` counter) and for `structure_audit.py`'s `stub_wired` node attribute.
- **Status:** none stated; reading: live as a test; the primitive it tests has no consumer in the head (see below).
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - `StubResult` is frozen with `stub` always True (init=False); `stub_resolve` returns a typed no-op, never raises; `invocations` counts calls and `reset_invocations()` zeroes it (:51-79).
  - Mutation check on a synthetic repo root: a fixture module `engine/fixture_consumer.py` in two variants (with the `stubwire` import and call; without both): the WITH variant bumps `invocations` by 1 and is seen by `structure_audit.stub_wired_modules`, the WITHOUT variant does neither (:84-177). The test copies the real `structure_audit.py` and `tools/ci_common.py` into the temp root.
  - `test_m1_acceptance_probe.py` records that the head (`engine/season/`) calls `stubwire` nowhere (stub count 0); so the primitive, its counter and the `stub_wired` attribute are measured by an acceptance row and used by no game code.
- **Conflicts / stale:** references a `review_core.py` signal retired in culling wave 2 and `audit/2026-07-29-code-shape-open-items/...` (archived). The docstring says "the two whose subject is the executable model", but the head does not call the primitive [per `test_m1_acceptance_probe.py:23-26`].
- **Open items:** none.

### tests/valoria/test_subphase_truncation_counter.py
- **What it is:** pytest file, ED-MB-0048 / plan-v2 A3: `resolve_engagements_cascading` counts engagements dropped when depth groups exceed `MAX_SUB_PHASES` instead of a silent `break`.
- **Status:** none stated; reading: live; strong (forced-truncation control plus non-vacuity).
- **Bears on:** MB (cascading sub-phase resolution of depth groups).
- **Content that matters:**
  - Test 1 lowers `MAX_SUB_PHASES` to 2 on a 4-group staircase (attackers 4 rows apart, each with its own defender) and asserts `n_groups == 4`, `truncated_groups == 2`, `truncated_pairs == 2`, `truncated_troops > 0.0` (the weight, not a fire-count, because truncation drops the DEEPEST-sorted groups so it biases systematically against deep formations, :106-126). Test 2: with bound 9 nothing is reported dropped (:129-137). Test 3: at the shipped bound, staircases of 2, 3, 4 groups truncate nothing, `multi_group_calls >= 3` and `max_groups < MAX_SUB_PHASES` (:140-169).
  - Recorded measurement (orchestrator, 2026-07-29): 64,273 resolver calls over all four bat.py modes plus the gauge, 0 truncations, max depth-group count 3 against a bound of 5 (table in docstring); the agent's larger-N figure (102,260) is stated as not replicated.
  - Mutation record: restoring the bare `break` fails `truncated_groups == 0`; dropping only the `truncated_troops` accumulation fails the weight assertion.
- **Conflicts / stale:** `MAX_SUB_PHASES` is `[CALIBRATED-DEBT]` and "moving it moves goldens" (:166-168).
- **Open items:** none.

### tests/valoria/test_tag_normalizer.py
- **What it is:** pytest file for `tools/tag_normalizer.py`: resolve/strip/render `[[id]]` tags through the names reader (Reconciliation Program §3).
- **Status:** none stated; reading: live; prose-tooling only.
- **Bears on:** PROCESS.
- **Content that matters:**
  - `resolve_id('attr.body.strength')` goes through `tools/names.py` (identity check) and gives `Strength`; `find_tags` parses bare and `[[id|override]]` forms; `render` resolves known ids and honours three unknown policies (`keep`, `humanize`, `raw`); `strip` resolves known and leaves unknown raw; `unknown_tags` is sorted; `stray_open_brackets` detects a raw `[[` as the migration collision lint (:25-74).
  - Pinned to an existing names entry so it does not depend on `conv.*` seeds.
- **Conflicts / stale:** none.
- **Open items:** none.

### tests/valoria/test_threadwork_mending_parity.py
- **What it is:** pytest file, WR-03: Mending is priced by ONE owner (`operations.mending_priced_scale`, `price_mending`, `apply_mending_feedback`) at the three sites that resolve it (single, collective, opposed), plus an R-14 resilience routing arm.
- **Status:** none stated; reading: live as a test of an off-loop oracle (`systems/threadwork/sim/`): the addendum records that no import of `threadwork.sim` exists under `engine/season/` or `modules/`, retained by ED-IN-0283.
- **Bears on:** WR (threadwork: Coherence, Mending, Weaving, Pulling, Locking, Dissolution, POP), DICE (degree labels), CORE.
- **Content that matters:**
  - Hash pins: 10 sha256 digests over 84 records each (7 scales x 12 seeds) for collective and opposing x {Weaving, Pulling, Locking, Dissolution, POP}, plus `BASE_MENDING_DIGEST` over 288 records, all captured at commit `dd91783a` (WR-02) with `RESILIENCE_GAIN = 0`; "1128 pinned"; the SHA will not survive a squash merge so the re-derive recipe (check out the four sim files from before `price_mending`) is the provenance (:134-162, :175-184). Mending in collective/opposing is excluded: it is the declared mover. These are control pins on a frozen commit, not live game hashes; failure prints the first recomputed record.
  - Control non-vacuity: the grid reaches all four degrees (collective) and all nine (A, B) pairs of the three-degree opposed table (:165-172); mending records include `coherence_restored > 0` and `resting_point_mended > 0` (:179-182).
  - Parity: for every (scale, degree, environment) cell the three sites return the same Ob (single vs collective), the same Coherence cost, MS delta and restorative term, with the dice and Leap forced by monkeypatching module names; cost is 0 at every degree (ED-871); `restored_cells == len(scales) * 3` non-vacuity (:245-270). Collective and opposed Mending refuse an own-configuration aim (`configuration_of` self/prac/other) with ValueError, a non-Mending working ignores it; the owner refuses an unpriced scale and an unknown degree (:273-302). With unforced dice over 60 seeds Mending never costs Coherence at any degree (the test notes a Leap's blanket Partial/Failure -1 "C-TW-3, a known separate defect in `_resolve_operation`", :305-332).
  - R-14: collective and opposing hand every cost to `operations.resist_coherence_cost` per practitioner; at gain 0 no difference, at gain > 0 the resilient takes less (`d_steady == -min(0, -d_plain + gain)`) over `RESILIENCE_GAIN_SWEEP` (:345-376).
- **Conflicts / stale:** C-TW-3 is a disclosed open defect in the oracle's `_resolve_operation`. Docstring references "NERS S, calculations consistent in methodology" as the reason for the one-owner rule.
- **Open items:** the oracle is not reached from the season loop; the hash pins protect a tool surface.

### tests/valoria/test_threadwork_resilience.py
- **What it is:** pytest file, WR-01 / R-14: a practitioner-side Resilience term on a working's Coherence cost (`operations.RESILIENCE_GAIN`, swept arms `RESILIENCE_GAIN_SWEEP`); shipped gain 0 is the control.
- **Status:** none stated; reading: live; the arithmetic is "unruled" and ships as a swept fixture at an inert default.
- **Bears on:** WR (threadwork, Coherence), CHAR (a `resilience` attribute on a practitioner), DICE.
- **Content that matters:**
  - Shipped gain is 0 and `RESILIENCE_GAIN_SWEEP[0]` equals it (:66-69): resilience changes nothing in the shipped configuration (`test_at_the_shipped_gain_resilience_changes_nothing`, :71-75). For each gain > 0 a resilient practitioner takes strictly less on a planted pair (same stats, same seed, same working, the roll untouched) and `delta == min(0, plain + gain * resilience)` (:77-89). Falsifier named: with the application line in `_resolve_operation` disabled the planted-pair test fails at every gain above 0.
  - A huge resilience floors the cost at 0, never positive, over five operations x all gains x 20 seeds (:92-105); the owner leaves zero cost alone and refuses negative, float, bool or None resilience (:108-117); at gain 0 the owner is an identity for any odd resilience value (None, -1, 1.5, True, inf, nan) and returns an int (:120-129). Mending is unaffected (the mender is pre-stressed so the restorative path runs) (:132-147).
  - The control is observed across three files: `engine/tests/test_thread_mending_ed871.py`, `test_threadwork_mending_parity.py` digests, and this one.
- **Conflicts / stale:** cites `canon/philosophy/06_operations.md` (ruled 2026-09-09): "What determines their ability to prevent that cost is how resilient their spirit is."
- **Open items:** the arithmetic of the Resilience gain is unruled; nothing in the shipped game exercises it (gain 0, oracle off-loop).

