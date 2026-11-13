# A-100 — mass battle as an abstraction of personal combat: the contact draw, the calibration instrument, the two separate layers

## Status: PROPOSED (design lane for ruling A-100, `unified/DECISIONS_ANSWERED.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; not canon; nothing here is applied)

## Read at: the working tree of 2026-11-12 (branch head of the suite). Producer: Opus design lane `master/mb_abstraction/`. One round. Parts: this file (verdict, §1 the contact draw, §2 the calibration instrument); `MBA_DESIGN_part2.md` (§3 the two separate layers, §4 targets and controls, §5 preconditions and order, §6 NERS); `MBA_DESIGN_part3.md` (§7 coding items, §8 supersession table, §9 evidence log and what was not checked). Items for Jordan: `MBA_FOR_JORDAN.md`.

**Words.** The suite's glossary (`unified/U1_GLOSSARY.md`) and the mass-battle lexicon (`unified/MB_LEXICON*.md`): *unit*, *subformation*, *army*, *cell*, *contact*, *frontage*, *field tick*, *bout*, *casualty* (a man put out of the fight, before his kind is drawn), *loss* (dead, captured, injured, fled), *martial skill* (a person's skill score in arms), *prowess* (a unit's, never a person's), *posture*. A personal-combat **duel round** is A-101's round: two men close, exchange attempts to attack, and separate; it is bounded by its count of exchanges, not by a fixed duration (A-101 as amended), so every seconds figure below is marked an estimate. Words this design introduces, each with its plain reading (owed to the glossary, §8.3): **contact draw** (the one draw that sets how many men one side of a contact loses in one field tick); **felling chance** (the chance that one man is put out of the fight in one duel round against one opponent); **exposure** (Jordan's word: how many duel rounds a front-rank man fights in one field tick); **matchup row** (a row of data saying how one class of troops meets another in one situation); **range band** (a distance band in which a missile arm hits at a stated rate). "Exchange" is not used for the mass-battle step: the glossary gives it to personal combat's phase.

---

## Verdict

**Decided (ladder steps 3 to 5; one item survives for Jordan, `MBA_FOR_JORDAN.md`).**

1. **The contact draw replaces the pool against an obstacle.** Each field tick, at each contact, each side's casualties are one keyed draw from a bell curve (A-5, A-30) whose centre and spread are set by: the attacker's arm in hand, the defender's armour, both men's martial skill, the defender front's rounds fought (fatigue and accumulated wounds), the attacker's support ranks, the exposure of the defender (posture, the arc he is struck from, crowding, cover) and the named levels of morale and discipline. Numbers act only through frontage, depth and how long a unit lasts (A-60). `subunit_combat_pool`, `pair_pool_contribution`'s pool, `roll_pool`/`roll_pool_fractional` in melee, the opposed `compute_degree`, `DAMAGE_BY_DEGREE`, `K_LINEAR`, `LANCHESTER_STRENGTH_REF`, `POOL_QUALITY_SCALE`, the `- eff_dr` subtraction and the side-wide multiplier `MB_FRICTION` leave the melee contact (§1.6).
2. **The weapon-on-weapon and weapon-on-armour numbers are measured, not tuned.** A calibration instrument (`tools/calibrate_mb_contact.py`, slow, run by hand at a calibration pass) runs the real duel engine over a grid of matchups and writes a measured table (`references/mb_contact/duel_grid.json`); an exporter (`tools/export_mb_contact.py`) derives the typed artifact the module reads (`engine/engine_params/mb_contact.json`) with a blocking `--check` round-trip that also refuses a table measured on a duel engine other than the one in the tree (§2).
3. **What personal combat cannot supply today is named, not invented.** The duel engine carries no shield, pike, lance, horse or missile weapon (its catalogue has 54 keys, none of them; §9 E-3). So pike against cavalry, bows against cavalry and every charge are **matchup rows** on the existing brace-and-shock idiom, calibrated against orderings the sources support and flagged uncalibrated in magnitude; missile fire is a **range-band model** whose per-hit felling chance is derived from the duel engine's own armour model once a missile head record exists there (§3). Whether personal combat should gain those kinds of equipment, so that those rows too are derived, is the one question for Jordan.
4. **Two numbers no source gives are carried as uncalibrated, never invented**: exposure (duel rounds a front man fights in a field tick; the sources give no casualty rate per minute) and the dead-to-injured split. Exposure is set by army-level ratio and ordering targets, and its absolute level is flagged (§4).
5. **Order.** The instrument runs only after personal combat's own batches land (B14, B15, B16: the typed outcome, the longer fight and the riposte at the deciding blow, the duel round); the contact draw lands inside the field calibration batch B19, replacing CR-12 steps 2 and 3 and the pair rule's edits 1 to 3, with one re-record (§5, §7).

**The pilot (measured on the real duel engine, §2.4).** 2.3 ms a duel for a mirror of arming swords in light armour (5,000 duels, 11.7 s), 3.1 ms with one side in heavy armour, 0.76 ms for spear against sword; mean 3.5 duel rounds a duel. Per side, the felling chance of a fresh man in a mirror is 0.073 in round 1 and rises to about 0.20 by round 4 (the accumulated wounds and fatigue of the duel itself). A spear against an arming sword wins 94.5% of duels and fells in the first round in 92.7%; heavy armour against light wins 92.4%. Controls: the same seed twice gives the identical table; the mirror's two sides agree (50.1% / 49.6%, per-round damage 0.230 / 0.230 of full health); a two-point skill edge reads 0.740 and 0.744 when the sides are swapped.

---

## §1 · The contact draw

### §1.1 What the draw is a function of (the matchup vector)

One contact `p` (a pair of engaged bodies, as `find_contacts` builds it today) and one receiving side `d` (the other is `a`). The **matchup vector** is a frozen record, `ContactVector`, built per tick per pair per side:

| field | meaning | source today (opened) | owner after |
|---|---|---|---|
| `arm_a` | the arm in the attacker's hand | `TROOP_LOADOUT` (`equipment/__init__.py:21-42`), `Subunit.in_hand` once `04_MB_unit_loadout_and_weapon_in_hand_B.md` §4 lands | `references/troops.yaml: arms`, `troops.<type>.primary/secondary` (B17) |
| `armour_d` | the defender's armour tier, `none | light | medium | heavy` | `armour.py:27` `TIERS` (same four keys as personal combat's `TIER2MAT`, `modules/combat/core.py:216`) | `troops.yaml: troops.<type>.armour` |
| `skill_a`, `skill_d` | each side's men's martial skill, on the duel engine's `faculty` scale | the troop row's `power` (`troop_types/registry.py:44-71`, 1 to 5) | `troops.yaml: troops.<type>.skill` (§1.7, the `power` column renamed by meaning) |
| `rounds_d` | duel rounds the defender's front men have fought since they were fresh (fatigue and accumulated wounds together) | the column stamina ledger (`percell.update_stamina`, `percell.py:301`; `16_PESSIMIST_MB_one_stamina_ledger.md`) | read as a share `s` in [0, 1]: `rounds_d = 1 + (K - 1) x (1 - s)`, `K` = the table's last round index (§2.3) |
| `support_a` | the attacker's ranks that reach the defender's front | `registry.support_weight(depth, troop_type)` (`registry.py:151-158`), the one owner of support depth | unchanged owner; the arm's class (`troops.yaml: classes`) |
| `exposure_d` | duel rounds a front-rank defender fights per field tick | none (the concept is new); its parts exist: posture (`STANCE_COMMITMENT`, `config.py:286`), the arc struck from (`_octagon_cell_mods` and `OCTAGON_DMG_MULT`, `orchestration.py:1320-1344`), crowding (`MULTI_SIDE_SHOCK`, same lines), cover (`terrain.py`) | `troops.yaml: contact.exposure` (§1.4) |
| `levels_d`, `levels_a` | named levels in skill steps: morale band, discipline, terrain dice, intent, charge shock, a missile arm fighting hand to hand | the sigma head (`orchestration.py:1230-1260`; `resolution._morale_sigma`, `_charge_shock_sigma`) | `troops.yaml: contact.levels` (§1.3) |
| `frontage` | the men of the two fronts facing each other in this contact: engaged files, each contact cell shared among the pairs it is in | `core/attrition._lanchester_strength` (`attrition.py:12-43`) counts engaged columns and body-average density | the same owner, re-stated as men: `engaged_files(...)` (§1.6) |

**Kit is data on the unit row** (A-2, A-59 (2)); **no number is the side's** (A-59 (3)): every field of the vector belongs to the two bodies in contact, and a unit's prowess is a vector that only has a value against an opponent. This is A-59's *"a static fighting value is misleading"* made structural: there is no scalar to sum over an army.

### §1.2 What it returns: casualties, one kind

**Decided: the contact draw returns casualties** (men put out of the fight, a continuous count, A-29's declared floats), **per side per contact per tick, and nothing else.** Grounds:

- A-60: numbers act through frontage, depth and endurance; a unit's endurance is its men present (`unit.hp`) plus its columns' stamina, both owned today (`attrition.py:41`, `percell.py`). Casualties are the one quantity both read; an "endurance loss" separate from men would be a second ledger for one quantity (S).
- The lexicon (`MB_LEXICON_part2.md:37-38`; `MB_LEXICON_part3.md` D-17): **casualty** is "a man put out of the fight during the battle, before his kind is drawn"; **loss** has four kinds. Of the four, two cannot arise at a contact: **captured** and **fled** come from the rout and the pursuit (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`, `16_PESSIMIST_MB_rout_has_two_exits.md`). The split of a contact's casualties into **dead** and **injured** is drawn once, at the field's end, by `27_MB_E_what_an_army_carries_back.md`'s share table, whose values do not exist in the tree (`research/historical/mass_battle_casualties_and_results_grounding.md:124`, "Nothing on wounded"; IS-MB-B3). The contact draw does not split them.
- What the duel can add later (§2.2, column `felled_mortal`): once personal combat's mortal-wound draw lands (`03_PC_exits_withdrawal_recovery.md` Part B, which adopts `14_VERBS_PHYSICAL_A` A3; B15/B16), the instrument records, per matchup, the share of fellings whose wound is mortal. That share is a **candidate** for `27_MB_E`'s dead share per matchup (a mace against plate may kill less and injure more than a spear against cloth). It is recorded and flagged; it becomes the split only by a decision recorded in B19's close, since a duel felling and a field death are different events (a felled man in the press is trampled; one in a duel is not).

Wounded men who stay in the line are not casualties; their effect is carried by `rounds_d` (§1.1), which is the duel's own accumulated wounds and fatigue.

### §1.3 How the bell curve enters, and where the keyed draw sits

For receiving side `d` of contact `p` in tick `t`:

1. **The felling chance per duel round** `h = H[arm_a, armour_d, skill_a, skill_d, rounds_d]`, read from the artifact (§2.3) by log-odds interpolation on `skill` and `rounds` (the grid holds skill at 1, 3, 5 and rounds 1 to `K`).
2. **Named levels, one ladder.** `logit(h') = logit(h) + beta x sum(levels_d)`, where each level is in **skill steps** and `beta` is the table's own measured slope of `logit(h)` against the skill difference at that cell (§2.3, column `slope`). So a morale band "worth one skill step" moves the felling chance exactly as one point of martial skill does in the duel. One ladder for one quantity (S; A-8's form for wounds). The level sizes are seeds transcribed from today's sigma terms by the tree's own conversion, `SIGMA_PER_D = 0.2` sigma units per die-equivalent (`config.py:306`) and one die per point of `faculty` (`modules/combat/attributes.py:21`, `pool = faculty + 6`): `INTENT_OFFENSE_D` 0.5 and `INTENT_DEFENSE_D` 1.0 step (`config.py:292-293`); terrain dice one step a die (`orchestration.py:1257-1260`); `MB_CHARGE_SIGMA` 0.55 becomes 2.75 steps at its cap (`config.py:365`); `MORALE_SIGMA_SCALE` 0.8 becomes 4 steps near rout (`config.py:333`); `RANGED_MELEE_SIGMA` -1.0 is dropped (the missile troop's sidearm is its own arm in the grid, §2.1). `MB_STAM_SIGMA` (`config.py:358`) is dropped: fatigue is `rounds_d`, measured. Every transcribed level is marked a seed and swept in B19 (§4.3).
3. **Per man per tick.** With `r = exposure_d` duel rounds per tick and `m = support_a` (the attacker's reaching ranks, weighted by `support_weight`): `q = 1 - (1 - h')^(r x m)`.
4. **The centre and the spread.** With `F = frontage` (men in the defender's front facing this contact): `mu = F x q`; `var = F x q x (1 - q)` (independent men; the binomial). The spread is the count's own; no second variance layer is added (A-77: the side-wide multiplier ships at zero).
5. **The draw.** `z = draw.normal(key=(field, bout, tick, pair, side, "contact"))` through the one keyed draw owner (A-30; `11_GO_one_draw_owner.md`, B06); one key per purpose, so a replay reproduces the tick and a change elsewhere in the field never re-keys it. `C = clip(mu + z x sqrt(var), 0, men in the contact cells)`. The bell curve of A-5 is the binomial's normal form, which is what the count of many independent duel rounds is.
6. **Where it lands.** `C` goes where `dmg_a`/`dmg_b` go today (`orchestration.py:1362-1374`): `MB_CELL_DAMAGE`'s per-cell allocation by exposure weight stays as it is (the arc changes where the men fall, and through `exposure_d` how many).

**One accepted bias, measured not hidden.** Clipping at zero raises the mean where `mu` is small (a contact of a few men). Item MBA-05's test reads the drawn mean against `mu` over the domain and reports the bias by `mu`; above `mu = 5` it must be within 1% (the normal form's own accuracy), below it the bias is printed in the close. [ASSUMPTION: a small positive bias at a thin contact is acceptable — basis: A-5 rules the bell curve everywhere, and a discrete sampler for small counts would be a second sampler.]

### §1.4 Exposure: the share of a field tick spent in a duel round

The sources say why a raw duel cannot be the field's clock. Sabin's bound: if a front rank of 5% of an army struck every five seconds with under 1% of strikes killing, "each army would suffer 5 per cent fatalities every ten minutes", which battles of hours exclude (`mass_battle_casualties_and_results_grounding.md:67`, A10). Lines spent most of a battle at a safety distance and closed in flurries (A8, D2; `MB_LEXICON_part2.md:13-14`). The pilot gives a fresh man's felling chance near 0.07 a round (§2.4): at one round a tick a 16-man cell's four front men would lose about 5 men in an 18-tick bout of about seventy seconds [estimate: `26_MASS_BATTLE_cell_scale_and_time.md` §1, `tick_s: 4` rests on a snippet]. So **exposure is well below one round a tick**, and it is the field's own quantity, not the duel's.

`exposure_d = EXPOSURE_BASE x posture[d, a] x arc_d x crowding_d x cover_d`:

| factor | values (seeds unless said) | owner today, reused |
|---|---|---|
| `EXPOSURE_BASE` | one number, rounds a front man fights per tick in an even, faced, balanced contact. **Uncalibrated in absolute level**: set in B19 by T-1 and T-2 of `26_MASS_BATTLE_calibration_targets.md` (ratios) and Sabin's bound read as a ceiling (§4) | new `troops.yaml: contact.exposure.base` |
| `posture` | each side's commitment raises its own and the enemy's rounds: `1 + 0.5 x (cA + cB)`, floored at 0.25, `c` from `STANCE_COMMITMENT` (`config.py:286`): two aggressors trade fast and bloody, two holders grind slowly (the comment at `orchestration.py:1246-1248`, kept) | `STANCE_COMMITMENT` (kept); the 0.5 is a seed |
| `arc_d` | the existing octagon multiplier, front 1.0, flank 1.5, rear 2.0, as `_a_dmg_mult` computes it (`orchestration.py:1331-1332`) | `OCTAGON_DMG_MULT` (kept, re-read as exposure: a man struck from the flank cannot keep his distance, D2) |
| `crowding_d` | `1 + MULTI_SIDE_SHOCK x (sides - 1)` (`orchestration.py:1343-1344`) | kept |
| `cover_d` | walls and terrain cover; `WALLS_DEFENDER_DR = 3` becomes `cover: 0.5` for the defender behind walls [seed] | `terrain.py`; `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edit 3's walls row is superseded by this |

The rounds a man fights are also what wears him: the column stamina drain per contact tick (`MB_STAMINA_DRAIN`, `config.py:355`) is scaled by `exposure_d / EXPOSURE_BASE`, so a man in a hot contact tires faster (one quantity, one owner: `16_PESSIMIST_MB_one_stamina_ledger.md` keeps the ledger).

### §1.5 What the abstraction drops from the duel, and how the distribution carries it

| dropped (per man, per round) | how its average effect is carried |
|---|---|
| initiative (the Vor/Nach state, `combatant.py:157`), who strikes first (`wrapper.py:593`) | measured inside `H`: the duel draws first striker per round; the felling chance is averaged over it |
| measure, reach and the closing phase (stop-hits, the soft closed-latch, `wrapper.py:96-100`) | inside `H`: every duel round opens at measure (`wrapper.py:83-90`), which is A-101's close-exchange-separate round and Sabin's safety distance. **Not carried:** a press that never separates (crowding) — carried as exposure only until the duel can start a round at closed measure (§2.5, MISSING) |
| binds, poise, concentration, stamina within a round | inside `H` |
| individual wounds and their obstacle | inside `H` by `rounds_d`: the duel's felling chance rises with the round index because wounds and fatigue accumulate (§2.4: 0.073 at round 1 to about 0.20 at round 4, per side); the field reads it from the column's stamina share, so fresh men fighting tired ones is the duel's own fact (CR D3) |
| the per-turn decider, yields and duel terms | not carried: the field's men fight under the lethal terms; a man who yields in the press is a casualty. Yield and withdrawal belong to the rout (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`) |
| the riposte at the deciding blow (`18_DETERMINISM_no_certain_matchup.md`, B15) | inside `H` once B15 lands; this is why the instrument runs after B15 (§5) |

### §1.6 What replaces what, and what stays

**Leaves the melee contact (deleted at landing, §7 item MBA-04):**

| symbol (file:line opened) | what replaces it |
|---|---|
| `subunit_combat_pool` (`core/exchange.py:77-148`) | nothing in melee: a unit has no pool. Its routed/broken/disordered tests (`:86-100`) move to the pair assembly as "this body contributes no attacker" (`m = 0`); its yield multiplier (`:139-140`) becomes a posture (`retreat`, exposure) |
| `pair_pool_contribution` (`:151-185`) | deleted; `_pair_engaged_troops` (`:188-222`) stays as the owner of "which men of a body are engaged" and feeds `frontage` and `support_a` |
| `command_base_pool`, `COMMAND_POOL_MULT`, `COMMAND_SIGMA_ENABLED` branches | already off the default path (`POOL_QUALITY_MODEL`, `config.py:552`); deleted with the legacy harness (`04_MB_typed_outcome_and_one_path.md` §2) |
| `roll_pool_fractional`/`roll_pool` and `_sigma_net_boost` in the melee pair (`orchestration.py:1261-1297`) | the contact draw (§1.3) |
| the opposed degree `compute_degree(a_net, max(1, b_net))` (`orchestration.py:1308-1309`) | none: there is no obstacle in the contact draw. `compute_degree` stays for the discipline, rally, recall and stand checks (will checks keep a stated obstacle) |
| `DAMAGE_BY_DEGREE` (`config.py:303`), `K_LINEAR`, `LANCHESTER_STRENGTH_REF` (`config.py:512-514`), `CASUALTY_SCALE` in melee, `POOL_QUALITY_SCALE` (`config.py:583`) | the measured felling chance and exposure |
| `- atom.eff_dr` (`orchestration.py:1360-1361`) | armour enters through `H` (measured), never subtracted |
| `MB_FRICTION`, `_draw_friction` (`config.py:310-331`, `orchestration.py:1725-1736`) | removed, as `27_MB_C` 27C-3 already specifies, in the same re-record |

**Stays:** command and the obedience draw (A-59 (1); `27_MB_A`); the stand, rally and recall draws; frontage, depth and endurance (A-60), with `engaged_files` the re-stated owner of frontage; the contact-cell share among pairs (`16_PESSIMIST_MB_partition_and_the_pair_rule.md` edit 4 and its five gate rows, which become this draw's gates); the cell damage allocation (`MB_CELL_DAMAGE`); the brace and charge idiom (§3.2); the nested duel at a window, cap 1 (A-4, A-72; `U5b_MB_rulings_in_the_field.md` §3), which is the same personal combat the table was measured on; the end state won, lost or drawn (A-3).

### §1.7 The troop row's `power` becomes `skill`

The troop table's `power` (1 to 5) is today two things: dice (`eff_power x eff_size`, `exchange.py:124`) and a damage multiplier (`DAMAGE_BY_DEGREE`'s `p`). Under A-100 the weight of blow belongs to the arm and the armour (measured), and the men's quality is their **martial skill** (A-98 (3)). **Decided (ladder step 5, architecture; and A-59 (2): prowess is troops and equipment):** the column is read as the men's martial skill score on the duel's `faculty` scale, transcribed one for one (levy 1, archers 3, heavy infantry 4, cavalry and templars 5), and renamed `skill` in `references/troops.yaml` when the table lands (B17). The lexicon row **power** ("a troop type's weight of blow", `MB_LEXICON.md:185`) is retired by this; owed to the glossary (§8.3). [ASSUMPTION: the one-for-one transcription — basis: `faculty` default 3 is the duel's average man (`attributes.py:51`) and light infantry, archers and spearmen carry power 3; reversible: one column of data.]

---

## §2 · The calibration instrument

### §2.1 The grid

| axis | levels | why these |
|---|---|---|
| arm (each side) | `arming` (for `light_cut`), `falchion` (for `heavy_cut`), `mace` (for `heavy_blunt`), `spear` (for `spear`), `dagger` (a missile troop's sidearm) | each mass-battle arm with a duel key (`modules/combat/weapons.py`, 54 keys, §9 E-3). The map is data: `troops.yaml: arms.<key>.duel_key`. `falchion` for `heavy_cut` and `dagger` for the sidearm are seeds for Jordan's content pass [ASSUMPTION: nearest duel weapon by kind — basis: `04_MB_unit_loadout_and_weapon_in_hand_B.md` "content for Jordan"]. **No duel key:** `pike`, the lance, every missile arm, `siege` (§3). For the ordinary contact after the first tick, `pike` reads `spear`'s cells and a mounted man reads his arm and armour on foot, each tagged `duel_key_status: proxy` in the troop file and printed in the field report; the difference a pike or a horse makes is carried by the matchup rows (§3.2) until personal combat carries the kit (J-MBA-01). Missile arms in contact read their sidearm (`dagger`) |
| armour (each side) | `none`, `light`, `medium`, `heavy` | the four tiers both engines share (`armour.py:27`; `core.py:216`) |
| martial skill (each side) | 1, 3, 5 | the troop table's span; 2 and 4 are interpolated and checked (below) |
| round index | 1 to `K = 6` | the pilot's hazard is flat from round 4 to 8 within sampling (§2.4); 6 holds the plateau with margin |

A **fighter type** is `(arm, armour, skill)`: 5 x 4 x 3 = 60. A duel between two types yields both sides' rows, so the grid is the unordered pairs with mirrors: 60 x 61 / 2 = **1,830 cells**. Twelve **interpolation check cells** run skill 2 and 4 against 3 for each arm in light armour (5 arms, both skills, plus two mirrors).

Every duel runs with the default attributes of `modules/combat/attributes.py` (`end` 4, `spirit` 3, `strength` 4, `agi` 4, `focus` 3, `att` 3, `disp` 4) except `faculty`, under the lethal terms, through the module's round entry. [ASSUMPTION: a troop's men have the average body — basis: no troop row carries attributes; reversible: a troop column `body:` and an axis.]

### §2.2 Duels per cell, and why

The stored quantities are per-side felling chances by round index, `h_k`, and the damage quantiles. Their precision decides `n`.

- **The floor.** A cell stops when, for each side, the Wilson 95% half-width of `h_1`, `h_2` and `h_3` is at most `max(0.10 x h, 0.002)`, and never before **2,000 duels**.
- **Derived from the pilot's variance** (§2.4): a fresh man in a mirror has `h_1 = 0.073`; ±10% relative at 95% needs `n = 1.96^2 x (1 - h) / (h x 0.1^2) = 3.84 x 0.927 / 0.00073`, about **4,900 round-1 observations**, which is 4,900 duels (every duel has a round 1). A heavily armoured defender's `h_1` near 0.01 needs about 38,000 for ±10%; the cap below gives ±0.0014 absolute there.
- **The tail.** The damage quantile `q99` per round needs at least 100 rounds above it: 10,000 rounds, which at the pilot's 3.5 rounds a duel is about 2,900 duels; satisfied wherever the hazard floor is.
- **The cap: 20,000 duels.** A cell that reaches it is stored with its measured half-width and the flag `precision: absolute`; a side with no felling in 20,000 rounds is stored as the Wilson upper bound with `below_resolution: true`, never as 0 (the standing rule: no certain matchup).
- **The rounds `k >= 4`** are read where at least 400 duels reached round `k`; otherwise `h_k` carries forward the last estimated index and is flagged `carried`.

**Cost of a full run [ESTIMATE].** The pilot's per-duel time is 0.76 to 3.1 ms (§2.4). Taking 2.5 ms and a mean of 6,000 duels a cell (most cells stop near 5,000; heavy-armour cells run longer, reach-dominated cells end in one round and run fast): 1,842 cells x 6,000 x 2.5 ms, about **27,600 core-seconds, 7.7 core-hours**; about 2 hours on four workers (`calibrate_generics.py`'s precedent: "About 12 minutes on 4 cores for the whole grid at n=10000", `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:17`). It is re-run only when the duel engine's fingerprint changes (§2.3).

### §2.3 What is stored, the schema, the exporter and the `--check`

**Two files, one owner each.**

1. **The measured table** (the head; written by the instrument, never by hand): `references/mb_contact/duel_grid.json`.

```json
{
  "schema": 1,
  "engine_fingerprint": "<sha256 of engine/engine_params/combat_engine_v1.json + the sorted sources of modules/combat/*.py>",
  "round_source": "<the round entry the duels were read through, e.g. combat.round>",
  "terms": "death",
  "K": 6,
  "seed_rule": "crc32(repr(cell_key)) % 100000",
  "cells": [
    {"a": {"arm": "spear", "armour": "light", "skill": 3},
     "b": {"arm": "arming", "armour": "light", "skill": 3},
     "duels": 5000, "outcome": {"a": 0.9452, "b": 0.0548, "unresolved": 0.0},
     "sides": {
       "a": {"h": [..K..], "h_lo": [..], "h_hi": [..], "rounds_at_k": [..], "flags": [],
             "damage": {"p_zero": 0.958, "mean": 0.027, "q50": 0.0, "q90": 0.0, "q99": 0.775},
             "felled_mortal": null},
       "b": {"...": "the same fields"}
     }}
  ]
}
```

`h` is the felling chance of that side's man in round `k` among rounds of index `k` that were fought; `damage` is the damage that side **takes** per round as a fraction of full health (the pilot's columns); `felled_mortal` is null until personal combat's mortal-wound draw exists (§1.2).

2. **The typed artifact** (derived; read by the module): `engine/engine_params/mb_contact.json`, written by `tools/export_mb_contact.py` from the measured table and `references/troops.yaml`. It holds, per ordered pair of fighter types, the `K` felling chances of the receiving side, the slope `beta` (the change in `logit(h_1)` per skill step, measured at that cell from its two skill neighbours), and the flags; plus `contact.exposure`, `contact.levels` and the arm-to-duel-key map copied from the troop file with their `seed` / `calibrated` tags. **Summary statistic: the empirical felling chance by round index, with its interval** (non-parametric: the pilot's per-round damage is zero in 60% of rounds and its tail passes 1.0 of health, which no two-parameter family fits without a stated test). Interpolation across skill is linear in log-odds; the twelve check cells test it (§2.5).

**The exporter's blocking `--check`** (the pattern of `tools/export_battle_orders.py`: re-derive and diff, exit 1 on drift): (a) re-derives `mb_contact.json` from the two heads and diffs it; (b) **refuses a stale calibration**: recomputes the duel engine's fingerprint and fails, naming the re-run command, if it differs from the measured table's `engine_fingerprint` (a personal-combat change that would move a felling chance cannot ship with an old table); (c) refuses a troop arm with a `duel_key` absent from the measured table, and a cell missing for any pair of fighter types the troop file can field. This guard is load-bearing on the game: its output is an exported parameter the engine reads (CLAUDE.md §0.1 pt 5, kept class). It runs in the season job beside `export_battle_orders.py --check` (Jordan owns the workflow file; the line is proposed in the PR body, as that exporter's registry note does, `references/ci_checks_registry.yaml:312-318`).

**The instrument** `tools/calibrate_mb_contact.py`: `run OUT [--workers W] [--cells FILTER]` writes the measured table; `--cell KEY N` re-derives one cell and prints it (the `calibrate_generics.py` form); `--spot M` re-runs `M` cells chosen by a fixed rule and compares with the committed table (each `h_1` within its stored interval); `--trust` runs the trust checks of §5.2 and stops on the first failure. It reads the duel engine through `engine/substrate/pc_engine.py` (the one path seam), builds `Combatant`s and reads the duel per round from the round entry's typed result (`master/pc_round/`, A-101; until it exists, the `engagement_end` and `wound` trace events, `wrapper.py:24-34`, `:596`, which is what the pilot read). It never imports `modules/mass_battle`; the module never imports it.

### §2.4 The pilot: measured numbers and the controls run

Scratch only (`/tmp/claude-0/.../scratchpad/pilot/pilot.py`, `pilot2.py`; not in the repository), `PYTHONHASHSEED=0`, Python 3, `modules/combat` at the working tree, `CFG` as shipped, lethal terms, default attributes, one `random.Random(crc32(repr(cell)) % 100000)` per cell; total wall time about 65 s.

| cell (A against B) | duels | ms a duel | A wins / B wins / unresolved | rounds a duel (mean, sd) | damage B takes per round (mean, sd; share zero; q90; q99) | round 1: any felling |
|---|---|---|---|---|---|---|
| arming light, skill 3 / arming light, skill 3 | 5,000 | 2.33 | 0.501 / 0.496 / 0.003 | 3.48, 2.14 | 0.230, 0.350; 0.62; 0.725; 1.35 | 0.145 |
| arming light / arming **heavy** | 5,000 | 3.10 | 0.047 / 0.924 / 0.028 | 4.83, 2.89 | 0.0135, 0.033; 0.80; 0.075; 0.15 | 0.080 |
| **spear** light / arming light | 5,000 | 0.76 | 0.945 / 0.055 / 0.000 | 1.07, 0.27 | 1.13, 0.28; 0.01; 1.45; 1.575 | 0.927 |
| arming light, skill **5** / arming light, skill 3 | 3,000 | 2.1 | 0.740 | — | round 1 mean 0.355 (mirror 0.251) | 0.150 |

**The felling chance by round index** (mirror, 3,000 duels; any felling in the round, both sides): rounds 1 to 8: 0.145, 0.279, 0.327, 0.382, 0.394, 0.397, 0.416, 0.402. Per side, half: 0.073 at round 1, about 0.19 to 0.20 from round 4. With a skill-5 man: 0.150, 0.298, 0.344, 0.374, 0.421 (the skill edge moves who is felled more than how often someone is).

**Controls run.** (1) Reproducibility: the mirror cell run twice in one process at one seed gave identical summaries to the last digit. (2) Side symmetry: the mirror's win shares 0.5008 and 0.4962 (Wilson half-width about 0.014) and per-round damage taken 0.2302 against 0.2302. (3) Position swap: skill 5 against 3 wins 0.740; 3 against 5 wins 0.2557, i.e. 0.744 for the skilled side. (4) The variance that sizes `n` is from these runs (§2.2).

**What the pilot shows beyond its numbers.** (a) The per-round damage is zero-inflated and heavy-tailed (60% of rounds no damage; q99 above full health): a felling chance by round, not a mean damage, is the right stored quantity. (b) Reach dominates the duel: a spear fells an arming sword in the first round 93% of the time. A contact draw built on this table will make spearmen near-certain winners over swordsmen at equal kit, unless the duel's closed-measure press (§2.5) or shields change it; this is reported to the PC lane as a finding about the duel, not tuned here (§6.3). (c) Heavy armour turns almost every blow of an arming sword (B takes 1.35% of full health a round); the armour-as-a-draw proposal (`16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw.md`, B15) changes exactly this, which is why the instrument waits on B15.

### §2.5 What the instrument cannot yet do (named, each MISSING with its owner)

| missing | why it matters | owner |
|---|---|---|
| a duel round that starts at closed measure (`wrapper.fight` always opens at measure, `wrapper.py:575`, and resets each round, `:83-90`) | a crowded or pressed contact (D2: the safety distance cannot be re-established) fights inside measure, where reach counts for less; without it crowding is carried by exposure only | PC lane: a `start_closed` input on the round entry (`master/pc_round/`) |
| a start-of-fight stamina below full (`_init_live` sets stamina to its maximum, `wrapper.py:42-47`) | entering tired is carried by `rounds_d`; a direct axis would separate fatigue from wounds | PC lane; optional |
| shield, pike, lance, horse, missile heads | §3; `MBA_FOR_JORDAN.md` J-MBA-01 | PC lane, on Jordan's answer |
| a mortal-wound reading per felling | the dead share candidate (§1.2) | B15/B16 (`03_PC_exits_withdrawal_recovery.md` Part B) |

**The interpolation check.** The twelve check cells at skill 2 and 4: each measured `h_1` must lie inside the interval of the log-odds interpolation between 1, 3 and 5 at that cell; if more than one of the twelve does not, skill 2 and 4 join the grid (cost: 60 to 100 fighter types, about 2.8 times the cells) and the close says so.
