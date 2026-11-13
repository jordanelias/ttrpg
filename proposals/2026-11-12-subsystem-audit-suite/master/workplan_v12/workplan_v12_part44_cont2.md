# Workplan v12 — part 44, continued (2): batch B98-dials, from B98.61, its readings, B98.99 and its close

## Status: PROPOSED (the second continuation of part 44's batch B98-dials; drafted under `master/workplan_v12/`; unratified until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block's head, its position table and items B98.01 to B98.22 are in `workplan_v12_part44.md`; B98.23 to B98.60 in `workplan_v12_part44_cont.md`. Paths, words and the reads `HASH`, `FIX` and the control arm as stated in the head.

---

### B98.61 — a grievance can occasion a march · row 72; B23.12; `IS-B3-FA-04` · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 72 ("TARGETED (A44 sweeps)"); part 37's line: "`march_grievance_regard` = `None`; set by B98; target: `IS-B3-FA-04`'s GATE, '`aperture 2 0` and `2 2`: `march` formed on an occasion other than `war` at least once across the two seeds once the setting leaves control' (no value stated: B98 sweeps it on that reading; `UNDECIDED` 4)"; B23.12: "`grievance` is true when his regard for the holder, in the unit `02_CHAR_scar_cap_and_regard_unit.md` defines, is below the setting `march_grievance_regard`".
- SETTING: `engine/season/data/fixtures.py` (`march_grievance_regard`) = `None`. New value: from the realm's own values (U9): the regards, in the unit B98.09 shipped, that persons able to march hold toward the holders of seats anchored on rungs in their reach, at build, seeds 0 and 2, listed.
- INSTRUCTION: at each listed value, from the most hostile, `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` and `2 2` with the value swept in-process (the instrument's run on a swept world; the producer records how the sweep is passed): `march` formed per occasion (`war`, `claim`, `grievance`). Rule (U4): the most hostile value at which `march` forms on an occasion other than `war` at least once across the two seeds. None: ship nothing.
- FALSIFIER and CONTROL: B23.12's ("with `march_grievance_regard` at `None` and no title planted the realm hash at seeds 0 to 2 equals its base"). Control arm: `HASH(0, 2; march_grievance_regard = None)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_march.py -q` → pass; per occasion counts and CI-11's `mass_battle.resolve_field` count quoted before and after; `HASH(0, 2)` and `HASH(2, 2)` recorded.
- HASH MOVERS: every world in which a grievance forms a march. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers, field goldens with a march.
- REVERT: `march_grievance_regard` → `None`.
- DEPENDS ON: V12 Batch B23, B23.12; V12 B98.09 (the regard unit).
- COST and TIER: calibration; `sonnet`, high; `opus` reads the occasions. LANDS IT: B98's producer; `Item: B98.61`, `[skip ci]`.

### B98.62 — an unopposed entry onto held land is drawn, if B23 did not switch it on · row 73; B23.05, B23.07; U5d-LAND · BUILD (flip, conditional) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 73 ("IN-BATCH (B23.07 if B23.01 has merged), else TARGETED"); part 37's line: "`entry_draw` = `off`; set by B23.07 if B23.01 has merged at B23.07's turn, else by B98; target: U5d-LAND arms (g) and (h) ('trespass in most seeds and not all'; 'aggression in most seeds and not all'), with arm (i) the control"; B23.07 ("`HELD (B23.01 unmerged)` if B23.01's design has not merged at this item's turn").
- CONDITION (U5): `FIX(entry_draw)` and B23.07's state on `main`. If `on`, record "set by B23.07 @<sha>"; POINTER. If `off` and B23.01's design is still unmerged at B98's open, this position is `BLOCKED (design: B23.01)` and flips nothing. Otherwise run.
- SETTING: `engine/season/data/fixtures.py` (`entry_draw`) = `off`. New value: `on`.
- INSTRUCTION: read arms (g), (h) and (i) at `on`, seeds 0 to 2, two seasons, in `test_b23_land.py`'s form and on the realm: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 --seeds 0 1 2` → per seed the count of unopposed entries onto held land and the band each drew. If (g) and (h) hold ("in most seeds and not all") with (i) the control, `entry_draw` → `on`, its `[JUSTIFIED: …]` tag naming B23.01's file and A-68.
- FALSIFIER and CONTROL: arm (i). Control arm: `HASH(0, 2; entry_draw = off)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_b23_land.py -q` → green; the per-seed counts and bands quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world with an unopposed entry onto held land. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `entry_draw` → `off`.
- DEPENDS ON: V12 Batch B23, B23.01, B23.05, B23.07.
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.62`, `[skip ci]` (if it runs).

### B98.63 — three Thread settings stay at control · rows 74 to 76; B35; CP-T07-04, AM-E-07, WR-01 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 74 to 76 (row 76 decided there, C-08); part 36's line.
- SETTINGS, each with its reason: (74) `self_mend_ob_step` = 0: "the share is the measurement; it must differ between arms or the knob is dead" (CP-T07-04); (75) `coherence_band_floors` = `()`: "`[OPEN — Jordan tuning]`, AM-E-07"; (76) `RESILIENCE_GAIN` = 0, swept `(0, 1, 3)`: "WR-01's falsifier is a sign, 'at gain > 0 a practitioner with resilience takes strictly less'": a sweep with no reading that chooses among its arms.
- INSTRUCTION: none. OWNER OF THE TARGET: the WR lane (74, 76); Jordan (75, "tuning").
- GATE: each read on the closing tree → its control (R2). B99 QUOTES: the three as left.
- DEPENDS ON: V12 Batch B35. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.64 — `legibility_curve` stays empty · row 77; B35; `IS-B3-WR-04` · BLOCKED (content: Jordan's curve) · HASH EQUAL
- SOURCE: part 2 §4 row 77; part 36's line ("`legibility_curve` = `()` (legibility 1.0 for everyone) … 'Jordan to author', `U5d_WR_zero…`; `IS-B3-WR-04` `[BLOCKED: the curve's values — Jordan]`").
- SETTING: `legibility_curve` = `()`. INSTRUCTION: none. OWNER: Jordan (D-19), listed in the PR body.
- GATE: read → `()` (R2). B99 QUOTES: everyone legible at 1.0; A-43's zero-coherence person is not unknowable yet.
- DEPENDS ON: V12 Batch B35. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.65 — the thread's seed values and `crossing_step` stay as seeded · rows 78, 79; B35, B35.18; `09_WR_B…` · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 78, 79; part 36's line: "`overweave_step`, `fatigue_scale_per_will`, `ops_per_contact`'s `k`, the `fatigue_cost` column = the design set's values (+1 obstacle, ×5, Focus − 1) `[ASSUMPTION; medium; Jordan to correct]`, shipped as data `status: seed`; set by B98 ('the joint calibration' …; `IS-B3` §5.6 `[BLOCKED: CONTENT]`); target: none stated"; with them the thread pool's re-expression on `pool_of`; `crossing_step` = 1 `[ASSUMPTION]`, `status: seed`, "odds from how far past", no target.
- SETTINGS: as listed, at their seed values. INSTRUCTION: none. OWNER: the joint calibration (WR lane, no batch) and Jordan for the content (PR body).
- GATE: each read on the closing tree → its seed value (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B35, B35.18. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.66 — the Thread ground's amounts and the knot strain: set in B35 or left · row 80; B35.01, B35.02, B35.24, B35.26 · BLOCKED (design: no target reading), unless B35 set them · HASH EQUAL
- SOURCE: part 2 §4 row 80 ("IN-BATCH (B35.26, B35.24) if the design items B35.01, B35.02 state a target, else BLOCKED (design: no target reading)").
- CONDITION (U5): read B35.24's and B35.26's commits. If they set the values on their designs' targets, record "set by B35.2x @<sha>" (not a member). Otherwise the values stand as shipped and this position records why.
- INSTRUCTION: none beyond the record. OWNER OF THE TARGET: B35.01's and B35.02's designs.
- GATE: the ground operation's amounts and `knot_strain` read on the closing tree (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B35, B35.01, B35.02, B35.24, B35.26. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.67 — veterancy, troop upkeep and the drill step stay at control · rows 81 to 83; B31; `04_MB_campaign_party_economy`; `IS-MB-B2` · BLOCKED (design: no target reading; carrier for 82) · HASH EQUAL
- SOURCE: part 2 §4 rows 81 to 83; part 39_cont's line.
- SETTINGS, each with its reason, in `references/troops.yaml`: (81) `veterancy.arm` = `off`, `veterancy.ob` unset: "a reading of mechanism, not a balance target; `ob` has no value in any source"; (82) `troops.<kind>.upkeep` = 0 on every row: BLOCKED (carrier: FA's and SE's payment path and the `arrears` write; "Who pays, and how, is not designed here"); (83) the drill step absent: "the build B31.01's design schedules (no batch; `IS-MB-B2`); target: a calibration against `26_MASS_BATTLE_calibration_targets`".
- INSTRUCTION: none. OWNER: the MB lane (81, 83); FA and SE (82, the payment path).
- GATE: `python tools/export_troops.py --check` → exit 0; the three read → control (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B31, B31.01. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.68 — four of the money institutions' settings stay at control · rows 84 to 87; B33; VEN_A, VEN_B, PAP · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 84 to 87; part 38's line.
- SETTINGS, in `engine/season/data/fixtures.py`, each with its reason: (84) `obligation_level` = `None`, `obligation_arrears` = 1.0, `sealed_obligation` = 1.0 (proposed `minor`, 0.5, 0): "VEN_A's gate reads Arm 1's band counts 'read and reported'; 'every value is recalibrated with OBS §4 step 5'"; (85) `penance_weight` = 0 (first value 2): "`pardon` odds printed exactly at `penance_weight` 0 and 2"; (86) `credit_terms` flat 1.0 (proposed `{Overwhelming: 1.1, Success: 1.25, Partial: 1.5}`): none stated; (87) `stakes_ob.debt` = `off` (sweep {off, on}): none stated.
- INSTRUCTION: none (the proposed values have no reading to keep them by). OWNER OF THE TARGET: OBS §4 step 5's re-centring (84), the FA/SC lanes (85 to 87).
- GATE: each read → its control (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B33, B33.38. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.69 — the Church's goal of its liberties stays off · row 88; B33.24; PAP_C · BLOCKED (carrier: a place filter on `deed_doers`) · HASH EQUAL
- SOURCE: part 2 §4 row 88; part 38's line: "`goal_church_liberties_kept` shipped off (written commented out, B33.24); set by no batch until `data/goals.py`'s owner builds a place filter for `deed_doers` (PAP_C: 'requested, not built here')".
- SETTING: the goal row in `engine/season/goals.yaml`, commented out. INSTRUCTION: none. OWNER: `data/goals.py`'s owner (the carrier, `V12_STRUCTURE_part2.md` §5.7).
- GATE: the row is still commented out on the closing tree (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B33, B33.24. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.70 — a seat's believed holder enters the stance term · row 89; B38.06; `20_NARRATIVE_C` gates 3, 4 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 89; part 40's line: "`holder_gain` = 0; set by B98; target: `20_NARRATIVE_C` gate 3 and gate 4 (among `march`, `petition`, `challenge`, `speak`, `release` acts on a seat or rung, the actor's mean regard for its believed holder differs between `holder_gain 1` and 0 by more than the control's seed spread for at least one verb; march targets over at least three believed holders at two seeds), swept 0 / 0.5 / 1".
- SETTING: `engine/season/data/fixtures.py` (`holder_gain`) = 0 (B38.06). New value: from `{0.5, 1}`.
- INSTRUCTION: B38.06's GATE reading on this base at each value, seeds 0 to 2, two seasons (four in the source; A-114), and `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms basis_off on --overlaps --executed-only` (gate 6, G4). Rule (U4): the smallest value at which gates 3 and 4 hold against 0. None: ship nothing.
- FALSIFIER and CONTROL: `test_held_by.py`. Control arm: `HASH(0, 2; holder_gain = 0)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_held_by.py engine/season/tests/test_told_by_channel.py -q` → pass; the per-verb means and the march targets quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every deliberation over a seat or rung with a believed holder. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `holder_gain` → 0. DEPENDS ON: V12 Batch B38, B38.06.
- COST and TIER: calibration; `sonnet`, high; `opus` reads gates 3 and 4. LANDS IT: B98's producer; `Item: B98.70`, `[skip ci]`.

### B98.71 — an unmet due lowers regard for its holder · row 90; B38.07; `20_NARRATIVE_B` gates 2 to 4 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 90; part 40's line: "`dues_valence` = 0.0; set by B98; target: `20_NARRATIVE_B` gates 2 to 4 on the planted world (i) at 2 (swept 0 / 2 / 4); world (ii)'s six-season reading is B99's conjunct `argv` (A-114)".
- SETTING: `engine/season/data/fixtures.py` (`dues_valence`) = 0.0 (B38.07). New value: 2 (the gate's arm).
- INSTRUCTION: B38.07's world (i) reading at 2, copied there (gate 2: "persons with `dues_unmet(p, x) > 0` for some `x` more than zero; the holders blamed number at least three; no holder draws a larger share of the grievances than his share of the seats sworn to"; gate 3: "grievances only among the unpaid half"; gate 4: at least one of `petition`, `speak`, `tell`, `challenge`, `release` differs against 0). If they hold, `dues_valence` → 2.
- FALSIFIER and CONTROL: `test_narrative_dues.py`. Control arm: `HASH(0, 2; dues_valence = 0.0)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_narrative_dues.py engine/season/tests/test_strife_credit.py -q` → pass; gates 2 to 4 quoted; `HASH(0, 2)` recorded. World (ii) (`build_realm`, six seasons) is B99's (B99.01 step 6).
- HASH MOVERS: every world with a lapsed due. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `dues_valence` → 0.0. DEPENDS ON: V12 Batch B38, B38.07, B38.10.
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.71`, `[skip ci]`.

### B98.72 — a teller's credit reads graded accord · row 91; B38.22; `30_WR_G` commit 4 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 91; B38.22: "Flip only on the strife guard passing and not blind, as CR-79 shipped `regime_gain` (H-275's method)"; "`accord` a **declared mover** at every telling between two persons with a shared axis"; B38.22's GATE recorded the strife guard's reading at `accord` as "the evidence B98 reads".
- SETTING: `engine/season/data/fixtures.py` (`credit_form`) = `sign`. New value: `accord`.
- INSTRUCTION: `PYTHONHASHSEED=0 python -m engine.season.harness.strife 2 0 1 2 --strands` at `accord` against `sign` on this base, read by H-275's method (the guard passing, and not blind: its planted failure still reds); and `test_strife_credit.py::test_a_fringe_teller_is_credited_between_a_stranger_and_the_core`. If both hold, `credit_form` → `accord`.
- FALSIFIER and CONTROL: "Any hash moving at … `credit_form` `sign`". Control arm: `HASH(0, 2; credit_form = sign)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_strife_credit.py engine/season/tests/test_storybar.py -q` → pass; the guard's two readings quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every telling between two persons with a shared axis. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `credit_form` → `sign`. DEPENDS ON: V12 Batch B38, B38.21, B38.22; Batch B11F2 (the strife guard).
- COST and TIER: calibration; `sonnet`, high; `opus` reads the guard. LANDS IT: B98's producer; `Item: B98.72`, `[skip ci]`.

### B98.73 — the pull of one's own custom · row 92; B38.23; `30_WR_G` commit 5 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 92; part 40's line ("`30_WR_G` commit 5's gate (1) to (4) at `custom_shift 0.25` against `custom_off`, two seasons (six in the source; A-114), (2) read with `30_WR_E`'s shape E-10"); B38.23's GATE (the four readings copied there).
- SETTING: `engine/season/data/fixtures.py` (`custom_shift`) = 0.0. New value: 0.25.
- INSTRUCTION: `PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 2 --arms custom_off custom_on --stories --overlaps` at 0.25: readings (1) to (4) as B38.23 copies them, (2) now read with shape E-10 (B38.71). If all four hold, `custom_shift` → 0.25.
- FALSIFIER and CONTROL: reading (4) ("four draw seeds do not give four equal vectors"). Control arm: `HASH(0, 2; custom_shift = 0.0)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_custom.py engine/season/tests/test_loops_instrument.py -q` → pass; `python -m engine.season.harness.loops` → "amplifiers derived equal declared"; the four readings quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every person whose circle keeps a custom. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `custom_shift` → 0.0. DEPENDS ON: V12 Batch B38, B38.23, B38.71.
- COST and TIER: calibration; `sonnet`, high; `opus` reads (1) to (4). LANDS IT: B98's producer; `Item: B98.73`, `[skip ci]`.

### B98.74 — a member who thinks ill of his own side argues its creed · row 93; B38.53; `20_NARRATIVE_D` gate 3 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 93; part 41's line: "`20_NARRATIVE_D` gate 3, 'executed `argue` acts whose subject is the actor's own creed: above zero at two seeds; the control arm: zero', seeds 0 to 2 at two seasons (four in the source; A-114)"; B38.53's GATE read the arm in a scratch override.
- SETTING: `engine/season/data/fixtures.py` (`stamp_own_side`) = `False`. New value: `True`.
- INSTRUCTION: read gate 3 on this base (counted from `harness/corpus_run.py::attempts`, as B38.53 did); if it holds, `stamp_own_side` → `True`.
- FALSIFIER and CONTROL: the control arm reads zero. Control arm: `HASH(0, 2; stamp_own_side = False)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_own_side.py -q` → pass; the counts per seed quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every member with a hostile stance toward his own side. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `stamp_own_side` → `False`. DEPENDS ON: V12 Batch B38, B38.53.
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.74`, `[skip ci]`.

### B98.75 — the Revival gathers: the sway draw's dial leaves 0 (lands after B98.76) · row 94; B38.55; `31_WR_B`; A-92 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 94 ("TARGETED (A-92)"); A-92: "The dial ships at zero until the calibration batch sets it"; `proposals/31_WR_B_the_revival_gathers.md` "The gate", expected on `sway_on` against `sway_off` "with `cohort_convictions` on in both": "2. Steps per person-season are above 0 and below 1 at the median seed, and the set of persons who moved is not the same at every seed. The calibration target for the four numbers is a house's live core moving by no more than one step on any axis in four seasons at the median seed `[ASSUMPTION; Jordan to correct]`. 3. Varfell's gap on the two Einhir affiliations is `rising` at some seeds and `stalled` or `falling` at others over five seeds … 4. The Church's core does not shrink in the seeds where the Revival's grows by more than the off arm's seed spread … 5. Entrenched-world arm (`sway_hold` at its highest swept value): stands barely move, and executed acts per person-season and the story census's rate (`23_STORY_D`) are not below the off arm's by more than its seed spread (A-80). 6. The no-null-scene reading is unchanged between arms (A-81)." Read at two seasons (six and four in the source; A-114).
- SETTING: `engine/season/data/fixtures.py` (`sway_gain`) = 0.0, with `sway_level` `minor`, `sway_hold` 2.0, `sway_link` 1 (B38.55, each `[ASSUMPTION; medium; Jordan to correct]`). New value: `sway_gain` from its swept `{2, 4}`; the other three stay at their shipped values (their sweeps are the source's, read only if `sway_gain` at 2 and 4 both fail).
- STOPS IF: B98.76 shipped nothing (`cohort_convictions` still `False`): the source's gate is stated with it on in both arms.
- INSTRUCTION: `PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 2 --arms sway_off sway_on --regimes --stories` at each value, `sway_on` carrying it. Rule (U4): the smallest value at which readings 1 to 6 hold, reading 2's calibration target read at two seasons (a house's core moving by no more than one step on any axis, half the source's four-season span, quoted beside). None: ship nothing.
- FALSIFIER and CONTROL: B38.55's three ("The same persons stepping the same way at every seed …"; "A step with no claim landing that round …"; the 200-planted-draw link arm) through `test_sway.py`. Control arm: `HASH(0, 2; sway_gain = 0.0)` equals B98.76's after-reading.
- GATE: `python -m pytest engine/season/tests/test_sway.py engine/season/tests/test_territorial_subsistence.py -q` → pass; readings 1 to 6 quoted per value; `HASH(0, 2)` recorded.
- HASH MOVERS: "a declared mover for every person who has taken in a deed by a member of a faction with a `creed:` row". EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `sway_gain` → 0.0. DEPENDS ON: V12 Batch B38, B38.55; V12 B98.76.
- COST and TIER: calibration; `sonnet`, high; `opus` reads readings 2 to 5 (the A-92 node). LANDS IT: B98's producer; `Item: B98.75`, `[skip ci]`.

### B98.76 — the populace starts at its house's core (lands before B98.75) · row 95; B38.56; `31_WR_B` commit 2; A-91 (3) · BUILD (flip) · HASH MOVER(behaviour), and the build hash
- SOURCE: part 2 §4 row 95; part 41's line: "`cohort_convictions` = `False` (B38.56); set by B98; target: `test_a_cohort_under_a_house_with_a_core_starts_within_half_a_step_of_it` green with the setting on and `build_realm` hashes moved, declared (A-91 (3): 'the populace starts at the core')".
- SETTING: `engine/season/data/fixtures.py` (`cohort_convictions`) = `False` (B38.56; read at build by `boot/realm.py::seat_cohorts`). New value: `True`.
- INSTRUCTION: `cohort_convictions` → `True`, one line; read the named test with it on.
- FALSIFIER and CONTROL: the test red at `True`; B38.56's ("a cohort under a faction with no `REGIME_CORES` row given a conviction; the same half-step settled the same way at every seed"). Control arm (a build-time key: `HASH`'s after-build sweep cannot reach it): with `DEFAULT_FIXTURES` overridden to `False` before the build (a scoped override restored in `try/finally`), `build_realm(0).content_hash()` and the two-season hash equal the previous flip's after-readings.
- GATE: `python -m pytest engine/season/tests/test_territorial_subsistence.py -q` → pass (the named test green at `True`); `build_realm(0).content_hash()` → moved, recorded; `HASH(0, 2)` recorded.
- HASH MOVERS: the build hash and every seeded world (A-91 (3), declared). EXPECTED RED UNTIL B98.99: `test_go07_canonical_digest.py` (`BUILD[0]`, `SHIPPED`), the `_realm_goldens` readers.
- REVERT: `cohort_convictions` → `False`. DEPENDS ON: V12 Batch B38, B38.56.
- COST and TIER: edit; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.76`, `[skip ci]`.

### B98.77 — a vacant head seat is a mandatory question · row 96; B38.61; `30_WR_A` commit 3; `30_WR_E` C7 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 96; part 41's line: "target: `30_WR_E` clause C7's lift for LOOP row L9 (whose switch it is, `30_WR_D` §2) above the spread across fork groups, eight draw seeds, window two seasons"; B38.71: "**C7 it compounds** — reads 'the fork lift of §2 for each loop row of `30_WR_D` §2 (a = the loop's first event, b = its next), eight draw seeds, window two seasons'; fails 'the lift is within the spread across fork groups …, or a occurs in all forks or none'; control 'the loop's switch at control'".
- SETTING: `engine/season/data/fixtures.py` (`era_mandatory_vacancy`) = `False`. New value: `True`.
- STOPS IF: `Question.mandatory` is absent on the base (B38.61 was HELD on it).
- INSTRUCTION: `PYTHONHASHSEED=0 python -m engine.season.harness.storybar --cascade` (B38.71's gate block) at `True`: clause C7 for L9, eight draw seeds, two seasons, with the switch at `False` as its control. If C7 holds for L9, `era_mandatory_vacancy` → `True`.
- FALSIFIER and CONTROL: "a person who may not claim receiving the mandatory mark" (`test_strife_flows.py`). Control arm: `HASH(0, 2; era_mandatory_vacancy = False)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_strife_flows.py engine/season/tests/test_storybar.py -q` → pass; C7's L9 line quoted; `HASH(0, 2)` recorded (moved only in a season with a vacant head seat: "none at build").
- HASH MOVERS: "any season with a vacant head seat". EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if a head seat falls vacant in two seasons.
- REVERT: `era_mandatory_vacancy` → `False`. DEPENDS ON: V12 Batch B38, B38.61, B38.70, B38.71.
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.77`, `[skip ci]`.

### B98.78 — the stake sizes stay off: no row is staked · row 97; B38.66; `23_STORY_A` · BLOCKED (carrier: no item declares stake cells on any verb row) · HASH EQUAL
- SOURCE: part 2 §4 row 97; part 41's line: "`shortfall_scale` = `off`, `stake_body`, `stake_stores`, `stake_standing` at their proposed sizes (B38.66); B98 member `BLOCKED (v12: a carrier is owed — no item declares stake cells on any verb row)`; target once a row is staked: `23_STORY_A` gate 2 ('step 3 occurs at two seeds or more and on fewer than one failure in five')".
- SETTINGS: `shortfall_scale` = `off` and the three stake sizes. INSTRUCTION: none. OWNER: a carrier that declares stake cells on verb rows (none in v12).
- GATE: read → `off` (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B38, B38.66. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.79 — the caste practice factors stay at 1.0 · row 98; B38.85 · BLOCKED (content: Jordan's) · HASH EQUAL
- SOURCE: part 2 §4 row 98; part 41's line: "`caste_practice` factors `earns`, `holds`, `heard` = 1.0 on every row (B38.85); … the values are Jordan's content ('Jordan to author')".
- SETTING: the three factors on every `caste_practice` row. INSTRUCTION: none. OWNER: Jordan (D-19), listed in the PR body.
- GATE: read → 1.0 (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B38, B38.85. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.80 — the world is generated from its tables · row 99; B39.01 to B39.03; `PROC_A` PG-1, `PROC_B` PG-2; A-50 · BUILD (flip) · HASH MOVER(behaviour), and the build hash
- SOURCE: part 2 §4 row 99; part 42's line: "`variable` = False (`build_realm`'s switch); set by: no batch names a flip (`PROC_A` §3 item 1: 'each later batch that flips a default is its own declared mover'; A-50 licenses the flip, 'each table a declared mover at its flip'); target: `PROC_A` §5 PG-1's `--range 20` reading and PG-2's play reading at two seasons"; B39.02's and B39.03's GATEs (copied there).
- SETTING: `engine/season/boot/realm.py::build_realm` (`variable` default) = `False`. New value: `True`.
- INSTRUCTION: on this base: `python -m engine.season.harness.worldgen --range 20` → PG-1 ("20 of 20 seeds pass V1; rejection rate printed and under one in five; distinct settlement signatures per world at least 10 (today 1); scarcity index … has a non-zero range across seeds") and PG-2 ("cast size within `cast_cap` in every world; 0 name collisions; V1 clean"); play, seeds 0 to 2, two seasons at `variable=True`: B39.02's ("at least one of `exchange.made`, `requisition.taken`, a hunger band crossing or an executed cohort `migrate` per world, against the `uniform` arm") and B39.03's ("every generated person acts at least once; acts whose subject is a generated person number more than zero"). If all hold, the default → `True`.
- FALSIFIER and CONTROL: B39.01's ("If two `variable=True` seeds build equal sites and stores, the planner is not reading the seed. If a table edit on one territory moves a draw in another, the draws are not keyed"). Control arm: `build_realm(0, variable=False)` and `HASH(0, 2)` on it equal the previous flip's after-readings.
- GATE: `python -m pytest engine/season/tests/test_worldgen_switch.py -q` → pass; PG-1, PG-2 and the play readings quoted; `build_realm(0).content_hash()` and `HASH(0, 2)` recorded.
- HASH MOVERS: the build hash and every seeded world (the realm is drawn from the tables). EXPECTED RED UNTIL B98.99: `test_go07_canonical_digest.py` (`BUILD[0]`, `SHIPPED`), the `_realm_goldens` readers, the NPC-088 headless pin; `test_variable_false_reproduces_the_pinned_hash` stays green (it passes `variable=False`).
- REVERT: the default → `False`. DEPENDS ON: V12 Batch B39, B39.01, B39.02, B39.03, B39.05, B39.08.
- COST and TIER: calibration; `sonnet`, high; `opus` reads PG-1 and PG-2. LANDS IT: B98's producer; `Item: B98.80`, `[skip ci]`.

### B98.81 — the prologue stays off: its target is twenty seasons · row 100; B39.10; `PROC_C` PG-4; A-51 · BLOCKED (A-114: target past two seasons) · HASH EQUAL
- SOURCE: part 2 §4 row 100 ("TARGETED at two seasons"; corrected here, U6, U9); B39.10: `worldgen.yaml` "`prologue_years: 5` (A-51) … converted to seasons as `5 × len(SEASONS_OF_YEAR)` … (20 at four seasons)"; "The shipped build passes `prologue=0`"; PG-4's reading "seeds 0–19 at `prologue=2` (twenty seasons in the source; A-114)". The shipped value A-51 rules is five years, twenty seasons: flipping it makes every later build run twenty seasons before tick 0, past the cap of every reading after it, B98.99's re-pin included; flipping to 2 would ship a value no source states.
- SETTING: `build_realm`'s `prologue` = 0.
- INSTRUCTION: read PG-4 at `prologue=2` on this base for the record (`python -m engine.season.harness.worldgen --range 20 --prologue 2`, from the cache, B39.10's reading) and quote it; flip nothing.
- GATE: the shipped build passes `prologue=0` on the closing tree (R2).
- B99 QUOTES: PG-4's story inventory at A-51's twenty seasons (B99.01 step 6, "twenty seasons in the source: B99's argv"); whether to ship the prologue on is Jordan's (P10).
- DEPENDS ON: V12 Batch B39, B39.10. COST and TIER: reading; `sonnet`, high (the cached runs). LANDS IT: no commit; B98.99's body.

### B98.82 — world cards are drawn, if their pools hold rows · row 101; B39.15; `PROC_D` PG-6 · BUILD (flip, conditional) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 101; B39.15: "The source's pooled reading ('With the 27 Tensions rows and a drafted set-piece pool: over 20 seeds the variety instrument … shows mean similarity lower than the cards-off arm by more than the dice-only spread', and the share of drawn cards opened 'within 4 seasons') needs content no item here authors (the 27 Tensions rows are `08_decks…` §1's; the set-piece pool is CL-OPEN's): it is read where those rows land, at two seasons (four in the source; A-114), and is the target named under DIALS for `cards`".
- SETTING: `build_realm`'s `cards` = `False`. New value: `True`.
- STOPS IF: the card pools in `engine/season/world_cards.yaml` hold no Tensions or set-piece rows on the base (only B39.17's two case rows): the reading cannot be taken; the position is then `BLOCKED (content: the Tensions rows and the set-piece pool)` and flips nothing.
- INSTRUCTION: `python -m engine.season.harness.variety` over seeds 0 to 19 at `cards` on and off, two seasons: mean similarity against the cards-off arm and the dice-only spread; the share of drawn cards opened within two seasons. If the similarity falls by more than the spread, `cards` → `True`.
- FALSIFIER and CONTROL: `test_world_cards.py`. Control arm: `HASH(0, 2; cards = False)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_world_cards.py -q` → pass; the variety reading quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world that draws a card. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `cards` → `False`. DEPENDS ON: V12 Batch B39, B39.15, B39.17; B12b.45 (the Tensions registry).
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.82`, `[skip ci]` (if it runs).

### B98.83 — the trail of a covert deed does not fade: no rate is stated · row 102; B39.17; `PROC_C` PG-5 (d) · BLOCKED (design: no value stated) · HASH EQUAL
- SOURCE: part 2 §4 row 102 (TARGETED there; corrected here, U9); `proposals/21_PROCEDURAL_C_prologue_and_case_seeds.md`: every `fade` row "`{per_season: 0, cap: 0}`  # 0 ships: the control arm, today's behaviour"; the reading "(d) **Erosion is real.** With `fade.per_season > 0`, the right rate falls as the proxy is seated later" names no value for `per_season` or `cap`.
- SETTINGS: `engine/season/rosters.yaml` (`covert_kinds.fade`, every member `{per_season: 0, cap: 0}`).
- TARGET, recorded: PG-5 (d), read at seasons 0, 1, 2 (4, 8, 12 in the source; A-114).
- INSTRUCTION: none (U9). OWNER OF THE VALUE: the FI lane (PROC_C's reading names none).
- GATE: every `fade` row read → `{per_season: 0, cap: 0}` (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B39, B39.17. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.84 — a marriage may bear a child · row 103; B39.24, B39.26; `STORY_B` gate 2 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 103; part 42's line: "`birth_rate` = 0.0, with `birth_pool`, `birth_ob`, `birth_level`, `birth_step`, `fertile_ages`, `fertile_peak` at their starting points; set by B98 ('set at the calibration with the A-5 sampler', `STORY_B` edit 2); target: `STORY_B` gate 2 ('a birth at some seeds and none at others; at least three of the four bands' outcomes across seeds')"; B39.26 step 2: "starting points: `pool_default` and the `routine` difficulty level; `birth_level` and `birth_step` have none"; `fertile_ages`, `fertile_peak` "authored in years … values are calibration content, none given here".
- SETTINGS: `engine/season/data/fixtures.py` (`birth_rate` = 0.0; `birth_pool` `pool_default`; `birth_ob` `routine`; `birth_level`, `birth_step` none; `fertile_ages`, `fertile_peak` as B39.26 shipped them). New value: `birth_rate` 1.0 (the gate's arm, B39.26's GATE); the rest stay at their starting points.
- STOPS IF: `fertile_ages` or `fertile_peak` is unset on the base (content, "none given here"): no bearer is in age; the position is then `BLOCKED (content: the fertile ages)` and flips nothing (U7).
- INSTRUCTION: B39.26's gate on the valley fixture with one seeded marriage, seeds 0 to 19, two seasons (eight in the source; A-114), at 1.0 against 0.0: "a birth at some seeds and none at others; at least three of the four bands' outcomes across seeds" (`assert checked >= 20`). If it holds, `birth_rate` → 1.0, `[ASSUMPTION; medium; Jordan to correct]`.
- FALSIFIER and CONTROL: "A birth with `birth_rate` 0.0 … The same couple bearing at every seed". Control arm: `HASH(0, 2; birth_rate = 0.0)` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_births.py -q` → pass; the reading quoted; `HASH(0, 2)` recorded (moved only if a realm marriage bears within two seasons).
- HASH MOVERS: every world with a marriage of bearing age at the year's turn. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if moved.
- REVERT: `birth_rate` → 0.0. DEPENDS ON: V12 Batch B39, B39.24, B39.26; Batch B37 (the authored ages, A-15).
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.84`, `[skip ci]`.

### B98.85 — the age of majority, if B39 did not set it · row 104; B39.27, B39.28; `STORY_B` gate 4; A-15 · BUILD (flip, conditional) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 104 ("IN-BATCH (B39.28 if the ages are authored), else TARGETED"); part 42's line: "`majority_age` = 0; set in this batch by B39.28 if the cast's ages are authored at the batch's open (`STORY_B` head: 'ships on with the ages'), otherwise by B98; target: `16 × len(SEASONS_OF_YEAR)` and `STORY_B` gate 4".
- CONDITION (U5): `FIX(majority_age)`. If non-zero, record "set by B39.28 @<sha>"; POINTER. If 0 and the cast's ages are still unauthored, `BLOCKED (content: the ages, A-15)`. Otherwise run.
- SETTING: `engine/season/data/fixtures.py` (`majority_age`) = 0. New value: `16 × len(SEASONS_OF_YEAR)` (read from `rosters.yaml: seasons_of_year`, the year's one owner).
- INSTRUCTION: B39.28's GATE on this base, copied: the count of persons under majority at `build_realm(s)`, s = 0 to 2, with the ages that make them so; `aperture 1 s`: no person under majority is offered a row; `STORY_B` gate 4 on the valley fixture, seeds 0–19, two seasons, the minor heir planted to come of age in season 2: "the heir's claim at his majority seats him at some, is contested at others, and at one or more the regent's hold is confirmed first by his own `succeed` or was full from the start". If it holds, `majority_age` → the value.
- FALSIFIER and CONTROL: a person under majority offered a row. Control arm: `HASH(0, 2; majority_age = 0)` equals the previous flip's after-reading.
- GATE: the readings quoted; the test file B39.27 names → pass; `HASH(0, 2)` recorded.
- HASH MOVERS: "every seeded world with a person under majority". EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `majority_age` → 0. DEPENDS ON: V12 Batch B39, B39.27, B39.28; Batch B37 (the ages).
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.85`, `[skip ci]` (if it runs).

### B98.86 — an empty founded place may be abandoned · row 105; B39.30; `STORY_C` gates 2, 3; A-55 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 105; part 42's line: "`abandonment_draw` = 'off', with `abandonment_pool`, `abandonment_ob`, `abandonment_patience`; set by B98 (A-55: 'licenses turning it on as a declared mover after its reading'); target: `STORY_C` gate 2 and 3 ('the rung stands at the end at some and is abandoned at others'; 'the season of abandonment differs between seeds')"; B39.30 step 4: "their values set at the calibration with the A-5 sampler (starting points: `pool_default`, the `routine` difficulty level, two seasons)".
- SETTINGS: `engine/season/data/fixtures.py` (`abandonment_draw` = `"off"`; `abandonment_pool`, `abandonment_ob`, `abandonment_patience` at their starting points). New: `abandonment_draw` `"on"`; the three at the starting points (`pool_default`, `routine`, 2), each `[ASSUMPTION; medium; Jordan to correct]` (U7).
- INSTRUCTION: B39.30's GATE on this base: the valley fixture with one works whose plan is a `hearth`, seeds 0–19, two seasons, `on`: "the founded rung stands at some seeds and is abandoned at others; the season of abandonment differs between seeds; no rung with a resident or a Site above zero drawn for … expected 0; realm matter by kind equal before and after every abandonment". If it holds, `abandonment_draw` → `"on"`.
- FALSIFIER and CONTROL: B39.30's ("A settlement, or any rung not of a `abandonment_kinds` kind, ended by this pass … Matter lost at an abandonment"). Control arm: `HASH(0, 2; abandonment_draw = "off")` equals the previous flip's after-reading.
- GATE: `python -m pytest engine/season/tests/test_abandonment.py engine/season/tests/test_storybar.py -q` → pass; the reading quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world with an empty founded rung. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if moved.
- REVERT: `abandonment_draw` → `"off"`. DEPENDS ON: V12 Batch B39, B39.30, B39.31.
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.86`, `[skip ci]`.

## Readings

(E-10. This batch has no source text to copy here byte for byte: each position's source text is in its own body. R1 and R2 are what B98.99 assembles, from the positions' commit bodies, for the close and for B99.)

**R1 — the flips** (positions B98.02, .04, .05, .06, .09, .10, .11, .12, .14, .15, .18, .21, .27, .29, .36, .39, .46, .47, .48, .50, .51, .54, .59, .60, .61, .62, .70, .71, .72, .73, .74, .76, .75, .77, .80, .82, .84, .85, .86, in landing order). One line per position: the setting, its control value, the value shipped (or "not flipped: <the reading>", or "set by <handle> @<sha>" for an IN-BATCH row its owner set, or "stopped: <the STOPS IF condition read>"), the target as its body quotes it, the reading taken (seeds, seasons, the printed figures), the control arm's `HASH(0, 2)` against the previous flip's, the after-reading `HASH(0, 2)`, and the `opus` reader's verdict line. A flip whose reading the `opus` reader judged short of its target was reverted (U8) and its line says so.

**R2 — the settings left at control** (positions B98.01, .03, .07, .08, .13, .16, .17, .19, .20, .22 to .26, .28, .30 to .35, .37, .38, .40 to .45, .49, .52, .53, .55 to .58, .63 to .69, .78, .79, .81, .83, and every R1 position that did not flip). One line per table row (105 rows, U1's groupings opened out): row number, setting and owner file, the value read on the closing tree (its `FIX` or named read), the status kind (`design: no target reading` · `design: no value stated` · `content` · `carrier` · `CR-103 held` · `A-114: target past two seasons`), the owner who must supply the target or value, and what B99 quotes. The `content` rows are listed again in the PR body for Jordan's correction (D-19): rows 36, 40, 54, 55, 59, 63, 77, 98, and the `[ASSUMPTION]` values any flip shipped (rows 6, 35, 103, 105 and `mark_ob` with row 4).

### B98.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2, E-10; `V12_STRUCTURE_part2.md` §5.9, §5.12; `workplan_v12.md` §6 (B98 re-pins once, at `B98.99`); `IS-A-12`; CLAUDE.md §7 ("say plainly when you re-record one").
- ADVANCES: the tree B99 re-takes the nine on (D-22: "B99 then reads the nine on the settings as set").
- INSTRUCTION: one commit, the batch's last `Item:` commit (no `[skip ci]`):
  1. Re-record, once, every pin the flips moved, against B40's close (`reading @<sha>`): `engine/season/tests/_realm_goldens.py` `SHIPPED` and `CENSUS` at seeds 0, 1, 2 (one season, `build_realm(s)` then `populated.run(1, s)`, `PYTHONHASHSEED=0`), and `BUILD[0]` if B98.21, B98.76 or B98.80 flipped; the NPC-088 headless hash; the corpus pins, `test_fi03_trail.py`'s realm hash, `test_season_weather.py`'s pins and the combat and field goldens (`python tools/ci_golden_modes_check.py`) only where a flip moved them; each old → new in the body. The commit says: "re-pin: B98, behaviour movers <the R1 positions that flipped>; the BLOCKED positions moved nothing".
  2. Re-derive what a flip touched with the repository's own tools: `python tools/export_sim_params.py --build`, `python tools/export_troops.py --build`, `python tools/export_engine_params.py` (only those whose `--check` reports drift), never by hand (CLAUDE.md §0.05 cl. 3).
  3. Assemble R1 and R2 in the commit body; record each IN-BATCH condition read (B98.18, .39, .59, .62, .85), each STOPS IF read (B98.02, .04, .05, .06, .09, .10, .12, .13, .21, .29, .34, .51, .54, .57, .75, .77, .82, .84), the BACKGROUND RUN wall times, and the batch's measured wall time.
  4. Write no `reading:` record and no `status:` in `engine/season/requirements.yaml` (REQUIREMENT: none; B99 writes them).
- WHERE: `engine/season/tests/_realm_goldens.py`; the other pin files the producer names from `git grep -ln "content_hash\|_GOLDEN" engine/season/tests engine/tests` at the item's open; `engine/engine_params/sim_params.json`, `engine/engine_params/troops.json`, `engine/engine_params/combat_engine_v1.json` (re-derived, where drifted).
- TESTS: none new. EXPECTED RED UNTIL B98.99 ends here: every test the flips' lines named is green on this commit's tree.
- FALSIFIER and CONTROL: a pin a flip moved and this commit did not re-record (the full suite reds on it); a `status:` line edited; a flip in R1 with no control-arm reading. Control: each BLOCKED position's value read at its control on this tree (R2).
- GATE: the head's BATCH GATE, read once on this commit's tree; the realm hash (`HASH READING`) at seeds 0 to 2, one season → the re-pinned values, each run twice, equal; the full suite once (`python -m pytest tests/valoria -q -n auto` and the engine suites `python tools/tests_for_diff.py --base <batch-start-sha>` names; CLAUDE.md §0.4: this batch edits engine fixtures, so the local run can observe what CI will).
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B98.01 to B98.86.
- GLOSSARY: none (no term introduced, renamed or retired).
- COST and TIER: edit (the re-pin) and reading; `sonnet`, high; `opus` reads R1 against each target once more as the batch's judgment node.
- LANDS IT: B98's producer; `Item: B98.99`, no `[skip ci]` (the batch's last `Item:` push, which opens BATCH-CLOSE).

| STOP. Batch B98-dials closes here |

SERIAL EDGES (written last, `V12_STRUCTURE_part4.md` E-11):
  within the batch: every flip edits `engine/season/data/fixtures.py` or a registry and changes the tree the next flip's control arm reads against, so the flips land one at a time in the position table's landing order, each after the last committed flip (the control arm's chain, the head's definition); B98.09 → B98.11 (the clamp bounds the regard unit) → B98.61 (the march threshold reads regard in the unit B98.09 shipped); B98.50 → B98.51 (UPR §6: "after `enmity_floor`"); B98.76 → B98.75 (`31_WR_B`'s gate "with `cohort_convictions` on in both"); B98.18 → B98.19 (row 21's "may read row 20's gate 1", recorded only); B98.36 after B98.29 (no file shared; landing order only); every position → B98.99. BLOCKED positions commit nothing and are read at B98.99. The probes that share an instrument run in the background once per arm and are read by each item that names them: `storybar` (B98.70, .73, .75, .77), `aperture 2` (B98.14, .61, .62), the MB gauge (B98.39, .54).
  with other batches, by file (`→` is landing order; part 2 §5 completes it by script): `engine/season/data/fixtures.py` … → B39 → B40 → B98; `engine/season/hole_register.yaml` (the flipped settings' NUMBER rows, text only) … → B40 → B98; `engine/season/tests/_realm_goldens.py` B02 → … → B40 → B98; `engine/season/rosters.yaml` (`stakes_ob`'s Tenure kinds if a table there, B98.02; `management_orders` read only) … → B98; `references/troops.yaml` (`fatigue.carry`, `carry_laps`, B98.54) B17 → B19a → B19 → B20 → B22 → B31 → B98; `modules/mass_battle/config.py` (`orders.obey.arm`, B98.39) B19 → … → B98; `engine/season/boot/realm.py` (`wound`, `variable`, `cards` defaults, B98.21, B98.80, B98.82) B03c → … → B39 → B98; `engine/season/requirements.yaml`: not edited here (B40 → B99).

FILE CENSUS (this batch's edits, for H2): `engine/season/data/fixtures.py` (B98.02 if `stakes_ob` is there, .04, .05, .06, .09, .10, .11, .12, .14, .15, .18, .21, .27, .29, .36, .46, .47, .48, .50, .51, .59, .60, .61, .62, .70, .71, .72, .73, .74, .75, .76, .77, .84, .85, .86); `engine/season/rosters.yaml` (B98.02 if `stakes_ob` is a roster there); `engine/season/hole_register.yaml` (each flip's NUMBER row text: the positions above, and H-235 at B98.21); `engine/season/boot/realm.py` (B98.21 `wound`; B98.80 `variable`; B98.82 `cards`); `references/troops.yaml` (B98.54); `modules/mass_battle/config.py` (B98.39); `engine/season/tests/test_sc_tuning_tables.py` (B98.02, one NEW test); `engine/season/tests/_realm_goldens.py` and the pin files named at the item's open (B98.99); `engine/engine_params/sim_params.json`, `troops.json`, `combat_engine_v1.json` (B98.99, re-derived where drifted). Read, not edited: `engine/season/requirements.yaml`, every owner item's test file, `modules/combat/config.py` (B98.26, .38), `engine/season/world_cards.yaml` (B98.82's STOPS IF), `engine/season/goals.yaml` (B98.69). Differences from part 2's census: B98's rows did not exist when it was generated.
