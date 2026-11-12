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

