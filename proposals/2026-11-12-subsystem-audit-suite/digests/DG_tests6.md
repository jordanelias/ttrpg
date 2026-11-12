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

