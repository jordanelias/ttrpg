# A-100 design, part 2: the two separate layers, targets and controls, preconditions and order, NERS

## Status: PROPOSED (part 2 of `master/mb_abstraction/MBA_DESIGN.md`; nothing here is applied; resolves nothing at runtime)

Read part 1 first (the verdict, the contact draw §1, the instrument §2). Sources cited by short name, as `26_MASS_BATTLE_calibration_targets.md` cites them: **CR** `research/historical/mass_battle_casualties_and_results_grounding.md`; **MV** `…_movement_and_behaviour_grounding.md`; **SQ** `…_maneuver_sequences_grounding.md`. Tier marks are the notes' own (`[D]` page read, `[T]` tool read).

---

## §3 · The two separate layers

Ruling A-100 keeps two things apart from the contact draw: (1) range at army level; (2) matchups that depend on geometry and the charge. Both are **layers around** the contact draw, not modifiers inside it: the first decides who is struck before contact and by what; the second decides whether and how a contact forms and what its first moments cost. Neither adds a scalar to a side.

### §3.1 (a) Range at army level: the missile regime by range band

**Today** (`orchestration.py:1574-1688`, opened): each ranged body picks the nearest target in `[VOLLEY_MIN_RANGE, VOLLEY_MAX_RANGE]` = `[2, 8]` cells (`config.py:188-189`), rolls its `power` in d10s less a discipline step, subtracts the target's `dr` from the net, multiplies by `K_SQUARE x eff_size` (aimed fire lifts the frontage cap, the square law) and by the target's density (`MB_VOLLEY_DENSITY_*`, `config.py:190-193`), and spends one volley (`MB_VOLLEYS_START` 10, `config.py:503`). Distance changes nothing inside the band; an armoured target's `dr` subtracts dice.

**Decided: a stated model with a calibration target, not a duel simulation** (the duel engine has no missile weapon; §9 E-3). For each shooting body `s` and its target `d` in tick `t`:

1. **Range bands per arm** (data, `troops.yaml: arms.<missile>.range` and `bands`): the arm's range is `26_MASS_BATTLE_cell_scale_and_time.md` §2's per-arm values (`javelin [1, 6]`, `bow`, `crossbow [2, 40]`, `sling`, `siege [2, 8]` not established and kept). Inside it, three bands by distance as a share of the arm's maximum: **close** (up to a quarter), **effective** (up to a half), **long** (the rest). [ASSUMPTION: three bands at a quarter and a half — basis: the sources give a maximum and a "final 50 yards" for the charge (MV H4), no band edges for missiles; reversible: two numbers of data.]
2. **Shots this tick** `S = men shooting x shots_per_tick[arm]`. Men shooting are the body's men not in contact and with volleys left (the ammunition rule stays, `orchestration.py:1607-1608`, `:1663-1664`). `shots_per_tick` is data, seeded from the sourced rates (bow "up to ten arrows per minute", crossbow "about twice a minute", `26_MASS_BATTLE_cell_scale_and_time.md` §2, W-CRE `[T]`) times the field tick [estimate: four seconds, `deployment.scale.tick_s`]: bow 0.67, crossbow 0.13. The volley counter counts ticks of shooting, as today.
3. **Hits** `Hh = S x hit[arm, band] x density_d x cover_d x profile_d`. `hit` decreases from close to long [seeds, ordering only]; `density_d` is today's density multiplier (kept, its owner unchanged); `cover_d` is the same factor the contact draw reads (§1.4); `profile_d` is the target's size class: foot 1.0, mounted 1.6 [seed]: a horse is a larger mark.
4. **Felling chance per hit** `f[arm, armour_d, mounted_d]`. For a mounted target a hit on the horse puts the rider out too: `f_mounted = 1 - (1 - f_rider[armour]) x (1 - f_horse)` with the horse unarmoured [ASSUMPTION: horses unbarded — basis: no troop row carries horse armour; reversible: a troop column]. **Derivation:** from personal combat's own armour model, once a missile head record (a bodkin and a broadhead point, a bolt) exists in its catalogue: the instrument's missile mode (§7 item MBA-02, stage 2) draws `N` unopposed hits at a stated impact per arm through the duel engine's damage function (`core.damage`, `modules/combat/core.py:609`) against each tier and counts the share that reach a fresh man's full health (felled) and his wound interval (wounded). Until that record exists, `f` is a **seed table** ordered by the canonical ranged armour table (none 0, light 1, medium 2, heavy 3 vs piercing, `armour.py:37-40`): strictly decreasing with the tier, the crossbow's `armour_piercing` keyword (`weapons.py:45`) raising medium and heavy; magnitudes **uncalibrated** and flagged.
5. **The draw.** `C = clip(mu + z x sqrt(var), 0, men of d in range)`, `mu = Hh x f`, `var = Hh x f x (1 - f)`, `z` keyed `(field, bout, tick, shooter, target, "volley")` (A-30, A-5). The square law is kept by construction: every shooter in range contributes, not only a frontage.

**How it meets the contact draw.** Missiles act before contact and between bouts' closings, never through a melee: a body in contact does not shoot, and shooting at a body in contact with one's own side is refused (`26_MASS_BATTLE_cell_scale_and_time.md` gate 3 and falsifier, kept). A missile troop that is reached fights with its sidearm (`dagger` in the duel grid, §2.1), or switches by a standing order (`volleys_spent`, `04_MB_unit_loadout_and_weapon_in_hand_B.md` §4). Casualties from missiles are casualties of the same kind and feed the same rout and morale readers; a body under fire it cannot answer erodes its morale through the existing per-cell morale erosion (`percell._erode_cell_morale_from_damage`, `percell.py:195`), unchanged.

**What it reproduces (orderings, §4):** shooting before contact where bows outrange (SQ §5 steps 2-3: "decided by rate and range"); the archers' switch when arrows run out (SQ step 5, `:133`); a pike block "weak to missiles" (SQ `:96-101`, Bannockburn); horse "fail on the obstacle and the arrows" (SQ `:129`).

### §3.2 (b) Matchups that depend on geometry and the charge

**Today**: a charge's moral shock is `_charge_shock_sigma` (`resolution.py:176-207`): `MB_CHARGE_SIGMA` 0.55 at most, scaled by the arc (`MB_SHOCK_FRONT` 0.15, flank 1.0, `MB_SHOCK_REAR` 1.6), by a brace product (`MB_SHOCK_HOLD_BRACE` 0.35 for `hold` or braced, discipline and depth retentions through `_disc_prep`/`_depth_prep`, floor `MB_SHOCK_BRACE_FLOOR` 0.05) and by how shaken the defender is (`MB_SHOCK_SHAKEN_GAIN`). A charger hitting a prepared braced wall pays `MB_CHARGE_RECOIL` 6 net successes x preparedness x `SIGMA_PER_D` (`config.py:392`, its own note: "CALIBRATED vs Courtrai/Swiss/Waterloo pike-vs-cavalry: braced+deep+disciplined wall beats a frontal charge ~75%"), gated on the charger being `cavalry` literally and the wall's reach at least the charger's (`config.py:394`). Brace needs a tick to set (`MB_BRACE_SETUP_DELAY`, `config.py:393`). The idiom is sound and is kept; what changes is the currency (sigma on a pool becomes levels on the contact draw and inputs to the stand draw) and that the special cases become **rows of data** keyed by class and situation.

**Decided: the matchup layer is a table of rows** `troops.yaml: matchups`, one row per `(attacker class, defender class, situation)`, each a small record:

```yaml
matchups:
  - {a: horse_shock, d: foot_pike, situation: charge_front_braced,
     closes: draw,              # closes | draw | evades | refused
     close_ob: 2,               # the will check the charger must pass to close (on the one sampler)
     first_tick: {exposure_a: 2.0, exposure_d: 1.0, levels_a: 0, levels_d: 0},
     stand: 0.05,               # multiplier on the charge's moral shock to the defender's stand draw (the brace product's floor)
     status: seed}              # seed | calibrated | derived
```

- **Classes** (from troop columns, not names; `04_MB_unit_loadout_and_weapon_in_hand_B.md` §3): `foot_short` (arm class `non_pole`, not mounted: levy, light infantry), `foot_pole` (`pole`: heavy infantry, spearmen), `foot_pike` (`pike`), `foot_missile` (`missile`, not mounted: archers, crossbow, sling, skirmishers), `crew` (artillery), `horse_shock` (mounted with `charge > 0`: cavalry; knights templar when its `mounted` cell is set, the contradiction the troop file surfaces for Jordan), `horse_light` (mounted, no charge: light cavalry), `horse_missile` (mounted archers). Eight classes.
- **Situations** (read from engine state that exists: the octagon zone, `_unit_braced`/`_subunit_braced`, the brace delay, momentum, the in-hand arm, formation state): `charge_front_braced`, `charge_front_unbraced`, `charge_flank_or_rear`, `marching` (a body in column or moving: no brace possible, `MB_BRACE_SETUP_DELAY`), `in_cover`, `pursuit` (the rout's), `skirmish` (a light body's evade).
- **How a row acts on the contact draw:** it **multiplies** exposure for the first tick of a contact (the impact: the charger's momentum puts more men into rounds at once; a braced wall's points meet the horse) and adds named **levels**, in skill steps on the one ladder (§1.3); it sets whether the contact forms at all (`closes`: always; `draw`: a will check of the charger, H1's "horses refusing to gallop into the dense mass"; `evades`: the light body opens distance on a draw, the kite rule; `refused`: no contact); and it scales the charge's **moral shock** passed to the stand draw (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`; A-61), which is where du Picq's "moral impulse" belongs, not in the casualty count. After the first tick the contact is an ordinary contact draw. **No row replaces the contact draw**; a missing row means the plain contact draw.

**Which rows the troop table needs (the roster).** Of 8 x 8 class pairs, rows are needed only where geometry or momentum makes the plain contact draw wrong. The full roster is 30 rows; **first needed (B19)** marked ★, the rest join in B31 with the troop economy:

| attacker | defender | situations needing a row | why (source) |
|---|---|---|---|
| horse_shock | foot_pike | ★ charge_front_braced, ★ charge_front_unbraced, ★ charge_flank_or_rear, marching | pike stops horse frontally only when set (MV H1-H2, Courtrai; `MB_CHARGE_RECOIL`'s calibration) |
| horse_shock | foot_pole | ★ charge_front_braced, ★ charge_front_unbraced, ★ charge_flank_or_rear, marching | spear wall weaker than pike (reach 0.2 against 0.3, `registry.py:112-115`) |
| horse_shock | foot_short | ★ charge_front_unbraced, ★ charge_flank_or_rear, marching | no points to meet the horse; shock decides (MV H1 "the defending formation breaking up") |
| horse_shock | foot_missile | ★ charge_front_unbraced, charge_flank_or_rear, in_cover | archers ridden down in the open (SQ `:96-97`, Bannockburn) but not behind obstacles (SQ `:129`, stakes) |
| horse_shock | horse_shock, horse_light, horse_missile | charge_front_unbraced, charge_flank_or_rear | horse against horse: both moving, no brace |
| horse_light | foot_missile, horse_missile | charge_front_unbraced, pursuit | light horse disperses unsupported archers (SQ `:96-97`) |
| horse_light | foot_pike, foot_pole | charge_front_braced | **refused** (no charge): `charge: 0`, light cavalry has no lance (`registry.py:70`) |
| horse_missile | any foot | skirmish | evades: the kite (`MB_KITE_*`, `config.py:388-389`) |
| foot_missile (skirmishers) | foot_pole, foot_pike | skirmish | evades: javelins harass, do not close (`registry.py:68`) |
| foot_pike | foot_short, foot_pole | charge_front_unbraced (the push of pike) | depth and reach in the press (MV F3, X5) |
| any | any | pursuit | the rout's pursuit row (`26_…rout…` §3): the pursuer's exposure only, the fleeing side's none |

**How each row is derived.** In order of preference, stated per row in its `status`:

1. **derived** (from personal combat): only when personal combat carries both sides' kit. Today none of the ★ rows can be: there is no horse, lance or pike in the duel engine (§9 E-3). The bridge, once the kit exists, is the squad of named characters (`04_MB_squad_grid_of_named_characters.md`, B30): a squad scene runs real duel rounds between persons placed on a grid; the matchup row's first-tick exposure and levels are fitted so the contact draw on the same scene reproduces the squad's casualties within the sampling band (§7 item MBA-07).
2. **calibrated** (small mass scenes in the real field engine): the charge scenario of `26_MASS_BATTLE_calibration_targets.md` §2 (200 horse against 400 foot: unbraced levy; braced pike; shaken spear; the horse against itself as the control), read for the T-6 ordering and the sources' qualitative outcomes (§4.2). This is how the ★ rows ship. Their **magnitudes stay uncalibrated** (no source gives a casualty or win rate for a charge; `MB_CHARGE_RECOIL`'s "~75%" is its author's reading of three battles, not a sourced rate: flagged as such).
3. **seed**: transcribed from today's constants by the tree's own conversion (`SIGMA_PER_D`), so landing the table moves no ordering. Each seed row is listed in the close with its source constant.

**The brace and shock idiom is reused, not re-implemented.** `_disc_prep`, `_depth_prep`, `_wall_prep`, `_brace_setup_ok` (`resolution.py:132-174`) stay the one owners of "how prepared is this wall"; a row's `stand` and `first_tick` values are multiplied by the wall's preparedness exactly as `_charge_shock_sigma` multiplies today, so a braced, deep, disciplined pike block reads the row at full strength and a shallow, raw one at the floor. The charger gate (`MB_RECOIL_CHARGER_GATE`: the charger must be literal `cavalry`) becomes the class `horse_shock`, which removes the name test (`04_MB_unit_loadout_and_weapon_in_hand_B.md` §3 already removes the other four).

---

## §4 · Targets and controls

**Rule (CLAUDE.md §0.1 pt 4; `26_MASS_BATTLE_calibration_targets.md` §1):** a derived table is read against ratios and orderings the sources support, each with a same-run control; never against a historical percentage taken as the engine's unit; a band is never moved in the commit that moves a constant into it.

### §4.1 What the instrument's table must reproduce inside personal combat (its own controls)

| reading | expected | control |
|---|---|---|
| mirror cells | each side's `h_k` inside the other's interval, every `k` with at least 400 duels | the same cell with sides swapped |
| armour monotone | for each attacker, `h_1` of the defender non-increasing from `none` to `heavy` | the mirror |
| skill monotone | `h_1` of the defender non-decreasing in the attacker's skill and non-increasing in his own | the interpolation check cells (§2.5) |
| round index | `h_k` non-decreasing in `k` up to sampling error (wounds and fatigue accumulate) | the pilot's 0.073 to about 0.20 (§2.4) |
| reproducibility | `--spot 20`: every re-run `h_1` inside its stored interval; the same seed twice is byte-identical | — |

A failure here is a finding about the duel engine, reported to the PC lane; it is never tuned on the mass side.

### §4.2 What the field must reproduce once the contact draw lands (B19's reading)

The rows of `26_MASS_BATTLE_calibration_targets.md` §1 stand and are the gate; this design changes what moves them, not the bands. Added or re-pointed:

| id | reading | band | source | the knob it may set | control |
|---|---|---|---|---|---|
| T-1 | winner's share lost, decided even field | flag if median above 0.10 | CR A1, A11 `[D]` | `EXPOSURE_BASE` (with T-2) | sides swapped |
| T-2 | loser's loss ÷ winner's loss, even field, no pursuit | 1.7 to 5.2 | CR A1-A2 `[D]` | `EXPOSURE_BASE`, the morale levels | sides swapped |
| T-2a (new) | Sabin's bound as a ceiling: an even contact's casualties per bout, front fighting throughout | below what one round a tick gives (the pilot's arithmetic, §1.4); reported as rounds per tick | CR A10 `[D]` (an upper-bound argument, not a rate) | none: a check that `EXPOSURE_BASE` is well under 1 | `EXPOSURE_BASE = 1` arm, read once |
| T-6 | horse charging frontally: unbraced foot > braced pole foot > 0; shaken foot highest | the ordering | MV H1-H3 `[T]` | the ★ matchup rows | the horse against itself |
| T-6a (new) | braced pike against a frontal horse charge: the pike side wins more often than the horse; the horse's loss is larger | ordering | MV H1-H2 (Courtrai `[T]`); CR B Golden Spurs `[T]` | the ★ `foot_pike` rows | the same charge into unbraced pike |
| T-6b (new) | bows against horse in the open versus bows against armoured foot: the horse's casualties per volley higher | ordering | SQ `:129` `[T]` (horse "fail on the obstacle and the arrows") | `profile`, `f_horse` | bows against unarmoured foot |
| T-6c (new) | a pike block under bow fire with no screen loses more than one with a horse screen that charges the archers | ordering | SQ `:96-97` `[T]` (Bannockburn) | the ★ `horse_shock` vs `foot_missile` row | no archers |
| T-8 | fresh against tired | the fresh side wins more than the mirror by more than the sampling band | CR D3 `[D]` | none: the duel's `rounds_d` must deliver it unaided (it is the falsifier of §1.5's carry) | both fresh |
| T-9 | numbers at 2:1 and 3:1 on a frontage that fits both | rises with the ratio, below 1 | CR D8 `[T]` | none (A-60: numbers act through frontage and endurance only) | 1:1 |
| T-11 (new) | dominance (§6.3) | no troop type has a contact ratio above 1 against every other type in every situation at equal men | the standing rule (no certain matchup) | none: a finding, reported | — |

**The Lanchester signature** (`systems/mass_battle/sim/lanchester_signature.py`). Its LINEAR row's band `LINEAR_BIG_WIN_BAND = (74, 83)` (`:43`) is, by its own comment (`:38-41`), the side-wide multiplier's calibration target; `27_MB_C` 27C-3 (h) already turns it into a printed flag with the pass condition "strictly inside (0, 100) and not below the 2:1 reading" in the commit that ships the multiplier at zero (A-77), and CR-12's gate reads the row as that commit leaves it (`04_MB_cr12_linear_law.md` head, C3-C6). **Under this design the same commit (B19's re-record) also removes the pool**, so: (1) the LINEAR row passes on 27C-3 (h)'s condition, read on the contact draw; (2) CR-12's **exponent** check (melee at or below 1.4 with an identifiable fit; the frontage control reading linear) **stands as the gate of A-60** and is read on the contact draw, where it holds by construction (numbers enter only through `frontage`), so it becomes the falsifier of that construction: a melee exponent above 1.4 means numbers have leaked into the draw somewhere; (3) the SQUARE row (volley at or above 1.6, zero melee pairs) stands and is read on the range-band model; (4) NO-ANNIHILATION stands. The **planted collapse** carrier, which `04_MB_cr12_linear_law.md` moves off `MB_FRICTION_SIGMA` when that constant is deleted, becomes a planted `EXPOSURE_BASE = 0` (no casualties: the LINEAR row must then fail as undecided), replacing the `PAY_PER_NET = 0` carrier that the pair rule's deletion removes.

### §4.3 What the sources do NOT establish, and how the design carries it

| not established (source line) | carried as |
|---|---|
| a casualty rate per minute, tick or phase (CR `:117`) | `EXPOSURE_BASE` flagged **uncalibrated in absolute level**; set by T-1/T-2 ratios with T-2a as a ceiling; the report prints rounds per tick and per bout so a reader sees what was assumed |
| pre-1700 loss ratios beyond Krentz's eleven hoplite battles; no medieval aggregate (CR `:122-123`) | T-2's band is Krentz's and is labelled so; no medieval band is invented |
| a break threshold (CR `:121`, A14) | not this design's: the 15% onset stays Jordan's value (A-61) |
| the dead-to-wounded ratio (CR `:124`) | the contact draw returns casualties only (§1.2); the split stays `27_MB_E`'s table, refused when missing; `felled_mortal` is recorded beside it as a candidate, flagged |
| charge outcomes as rates (MV H1-H4 are qualitative; H4: medieval charge stage distances not established) | ★ matchup rows ship as `seed`/`calibrated` to orderings only; magnitudes flagged |
| missile per-hit lethality by armour (no source read) | `f` ordered by the canonical DR table; magnitudes flagged until the duel engine's armour model derives them (§3.1) |
| shield effect (SQ `:105`: arrows "bounced off the shields"; the duel engine has no shield) | not modelled; every foot troop fights as if unshielded; named in `MBA_FOR_JORDAN.md` J-MBA-01 |
| rounds per field tick; the round's duration (A-101 amended: exchange-count-bounded) | no seconds figure enters a resolver; `tick_s` stays a report-only estimate (`26_MASS_BATTLE_cell_scale_and_time.md` §1) |

A cell whose magnitude is uncalibrated carries `status: seed` in the artifact; the field report lists the seeds a battle read, so a reader knows which numbers are measured and which are not (`27_MB_C`'s `report.draws` precedent).

### §4.4 Every number in this design and its control

| number | its control |
|---|---|
| the pilot's per-duel time and rounds | none needed (a cost, not a claim about the game); two cells of very different kind bracket it |
| the pilot's felling chances and damage | the mirror, the position swap, the seed repeat (§2.4) |
| `n` per cell | derived from the pilot's variance (§2.2); `--spot` re-runs check it held |
| the full-run cost | marked estimate; the first real run's time is recorded in its commit and replaces it |
| every transcribed level and exposure factor | B19's one-at-a-time sweep against its control arm, n 400 (`26_MASS_BATTLE_calibration_targets.md` §3's form) |

---

## §5 · Preconditions and order

### §5.1 What must land first, and why

| batch (U3 §2.1) | what the instrument needs from it | consequence if the instrument ran before it |
|---|---|---|
| **B14-pc-outcome** | the typed outcome and `03_PC_weapon_records_in_the_export.md`: the duel engine's weapons and armour exported (`engine/engine_params/combat_engine_v1.json`), which the fingerprint hashes | the fingerprint would not cover the weapon data |
| **B15-pc-calibration** | A-31's lower damage scale (fights longer), A-79's one opposed rule in the fight (`29_DICE_one_opposed_rule_form_and_tuning.md` part), the riposte at the deciding blow replacing `UPSET_FLOOR` (`18_DETERMINISM_no_certain_matchup.md`), armour turning a blade by a draw (`16_PESSIMIST_PC_D`), the yield as a draw (`16_PESSIMIST_PC_A`), the mortal-wound draw (`14_VERBS_PHYSICAL_A` A3) | **every one of these moves `h_k`**: a table measured before them is spent the day they land (the pilot's 92% heavy-armour edge is exactly what `16_PESSIMIST_PC_D` addresses) |
| **B16-pc-round** | the duel round as a returned unit (`03_PC_duel_round_and_approach*.md`; A-101's round, `master/pc_round/`) and the exits (`03_PC_exits_withdrawal_recovery.md` Part B, F-PC-04's resolution) | the instrument would parse trace events instead of reading the round's typed result; the dead share candidate would not exist |
| B05-one-roll, B06-keyed-draw | the field's one sampler and the keyed draw the contact draw uses | — (the contact draw lands in B19, after both) |
| B17-mb-scale | `references/troops.yaml` and its exporter (arms, classes, troop rows), which the arm-to-duel-key map and the matchup rows live in | no home for the map |

**F-PC-04 (a plain `fight` kills every time).** The felling chance per round does not need a non-lethal fight; it needs fights that run several rounds, which the lethal terms give (the pilot: 3.5 rounds a duel). What F-PC-04 blocks is the **kind** of a felling: while every felling is a death the duel can say nothing about the injured, so `felled_mortal` stays null until B15/B16's mortal-wound draw lands, and the dead share stays `27_MB_E`'s uncalibrated table.

### §5.2 What the instrument checks about the duel before it trusts it (`--trust`, run first, stops on failure)

1. **Fingerprint** recorded and equal to the tree's (the exporter's check (b)).
2. **Symmetry**: five mirror cells (one per arm, light armour, skill 3): each side's `h_1` inside the other's interval and win shares within 3 standard errors.
3. **Swap**: two asymmetric cells run both ways agree within their intervals.
4. **Reproducibility**: one cell twice at one seed, byte-identical.
5. **No certainty**: no cell's outcome share is 0 or 1 at its `n` (the standing rule; `18_DETERMINISM_no_certain_matchup.md`'s gate); a cell at 0 or 1 stops the run and is reported to the PC lane, not stored.
6. **Rounds run**: the mirror's mean rounds a duel is at least 2 (a fight decided in one round everywhere would make `rounds_d` empty; the pilot reads 3.48).
7. **Round boundary**: the count of rounds the instrument reads equals the round entry's own count (`master/pc_round/`), for 100 duels.

### §5.3 Where the batches slot (U3 §2.1, amended; the full items are §7)

- **New batch B19a-mb-contact-instrument** (MB lane, with PC review): the instrument, the measured table, the exporter and its `--check`, the module's loader. **After** B14, B15, B16, B17. **Hash EQUAL** (nothing in the field reads the table yet). Wave: W11 (B16 is W10).
- **B19-mb-field-calibration** gains the contact draw, the range-band model and the ★ matchup rows as its central step, in place of `04_MB_cr12_linear_law.md` steps 2-3 and `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edits 1-3; it gains dependencies **B16 and B19a**, so it moves from W10 to **W12**. Its one re-record stays one.
- **Cascade** (dependency levels only; no other edge changes): B20 W11 to W13; B22 W12 to W14; B23 W13 to W15; B30 and B31 W12 to W14. The suite's critical path (18 batches through FI, SC, FA and WR, U3 §2.2) is unchanged: B38 still waits on B23 at W15 and runs at W16, one wave later than U3's W15 — **this lengthens the critical path by one wave**, and the cost is recorded here for v12's serial-edge table. [ASSUMPTION: B38's edge to B23 is the only critical-path edge the MB chain feeds — basis: U3 §2.1 rows 37-38 read; B39's dependencies include B22 (W14 under the cascade), which stays below B38's level.]
- The **missile mode** of the instrument (per-hit felling from the duel's armour model) and the derived matchup rows wait on personal combat carrying the kit (J-MBA-01); they are items MBA-02 stage 2 and MBA-07, in **B31** and **B30** respectively, each behind its kit.

---

## §6 · NERS (`skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06; E last)

### §6.1 The cut test: remove the abstraction, what dies?

Removing the contact draw returns the field to a pool of troop quality against the opponent's net as an obstacle, with a damage table by degree and a hand-tuned scale. What dies:

- **The link between the two scales.** Today a heavy-armoured knight in a duel and a unit of heavy horse in a field are resolved by two unrelated models (the duel's armour coupling; the field's `dr` subtracted from dice). With the contact draw, changing a weapon's head geometry in personal combat changes what that weapon does in a field, through one exported table. Without it, every personal-combat calibration (B15) leaves the field where it was.
- **Kit as a decision.** Today kit is inert in resolution (`equipment/__init__.py:10`: "NOT YET WIRED into resolution"; `weapons.py:17-18`). Under the contact draw, arming a levy in mail changes its felling chance against each enemy arm by a measured amount, which the player can intuit from personal combat.
- **Fatigue and fresh lines as one fact.** The duel's own round index carries wounds and fatigue; without it the field keeps `MB_STAM_SIGMA`, a fitted constant.

### §6.2 From all six directions

| direction | reading |
|---|---|
| **top-down** (the game's goals) | A-59 (no static side-wide value) and A-60 (numbers through frontage, depth, endurance) are met structurally: the draw has no side term and no numbers term. A-3's end state is untouched. N holds |
| **bottom-up** (the primitive) | the duel round is the primitive (A-101); the field aggregates it by frontage, support ranks and exposure. The one owner of "what a blow does to armour" is personal combat; the field reads it. S holds (one methodology across scales) |
| **vertical** (personal to field and back) | the officers' nested duel (A-4, A-72) and the squad grid fight the same duel rounds the table was measured on; the bridge test (MBA-07) checks the field's aggregation against a squad of real duels. R and S hold, conditional on B30 |
| **diagonal** (another subsystem's view) | social contest and personal combat share one opposed rule (A-79); the field deliberately does not use it at the contact (there is no obstacle), and keeps it in the will checks (stand, rally, obey). That is two forms, each where it belongs: the contact is a count of many independent rounds; a will check is one man's decision. S: consistent in methodology because both draw on the one sampler and the contact's felling chance is itself measured under A-79's rule inside the duel |
| **lateral** (sibling mechanisms in the field) | missiles and the charge are layers with the same currency (casualties from a keyed bell-curve draw; levels in skill steps; exposure) as the melee contact; the rout and pursuit read casualties, unchanged |
| **horizontal** (across troop types) | every troop type enters through the same three columns (arm, armour, skill) and its class; no name test survives (`MB_RECOIL_CHARGER_GATE`'s literal `cavalry` goes). But see §6.3: the duel's reach edge propagates |

**R (robust).** Strategic: what to arm a unit with, where to stand it (arc, exposure), when to rotate it (rounds fought), whether to charge a set wall. Customisation: a troop row is three columns plus a class. The half with no player in it: two unplayed armies fight differently by kit and posture with no script. **Completeness at the extremes**: a cell below the duel's resolution is stored as an upper bound, not 0 (no immortal heavy armour); a contact of a few men has a measured clip bias; an arm with neither a duel key nor a declared proxy is refused by the loader, and every proxy is printed in the report, so nothing silently falls through to a default.

**S (smooth).** *Pauses correctly*: the field calls the duel only at a window (A-72), never per tick; the table is read, not run, during a battle. *Calculations consistent in methodology*: one ladder (skill steps) for every level; one bell-curve draw per keyed purpose; one owner for frontage, support and preparedness. The one place two forms coexist (contact count versus will check) is named in the diagonal row.

**N (necessary).** Holds from top-down, bottom-up, vertical and lateral; narrowed horizontally by §6.3 and by the kit gap (J-MBA-01): for pike and horse the layer is stated, not derived, so for those troops A-100's "derived from personal combat" is not yet true.

**E (elegant), last, as a ratio against N and R.** Removed: the pool, the opposed degree, `DAMAGE_BY_DEGREE`, `K_LINEAR`, `LANCHESTER_STRENGTH_REF`, `POOL_QUALITY_SCALE`, `CASUALTY_SCALE` in melee, `MB_STAM_SIGMA`, `RANGED_MELEE_SIGMA`, `MB_FRICTION` with `MB_FRICTION_SIGMA`, `K_SQUARE`, and the `dr` subtraction in both melee and volley; with them `subunit_combat_pool`, `pair_pool_contribution` and `_draw_friction`. Added: one measured table and its exporter, one exposure product of four reused factors, one base number, a matchup table of 30 rows. The player intuits a field from a duel: "spears beat swords, plate turns blades, fresh men beat tired ones" is true at both scales because it is one fact. The ratio is favourable; the cost is the 7.7 core-hour run [estimate], paid once per duel-engine change.

### §6.3 The dominant-strategy check

Read from the pilot (the full grid will re-read it; MBA-06's report):

- **Reach.** A spear against an arming sword in light armour wins 94.5% of duels and fells in round 1 in 92.7% (§2.4). Carried into the field at equal kit, spearmen would trade at a ratio of about 43 to 1 against swordsmen in round-1 damage taken (the sword side takes 1.16 of full health a round, the spear side 0.027). Within the field, three things answer it: horse on the flank (`charge_flank_or_rear` rows), missiles (the spear block is a dense target), and the troop economy (B31). Two things that should answer it are **missing**: a press at closed measure, where historically short weapons recovered (MISSING, §2.5), and shields (J-MBA-01). **Finding, reported to the PC lane, not tuned here**: the duel's reach edge is close to certain at open measure; whether that is the intended duel is personal combat's question (B15's `18_DETERMINISM_no_certain_matchup.md` bounds certainty, it does not move the edge).
- **Armour.** Heavy against light, same arm: 92.4% of duels. Its answers: the carry demand (`04_MB_unit_loadout_and_weapon_in_hand_B.md` §5: armour tires its wearer through the one stamina ledger), cost and upkeep (B31), the blunt arm (`mace`, measured in the grid against heavy), and the crossbow's per-hit edge. `16_PESSIMIST_PC_D` (B15) changes the duel's own armour edge before the table is measured.
- **The check as a gate.** MBA-06 computes, from the artifact, every troop type's contact ratio against every other at equal men and full freshness, in each matchup situation and at range, and reports any type that is above 1 against all others in all situations. A dominant type is reported in B19's close with its answer, or is a finding for Jordan; the table is not tuned to remove it.
