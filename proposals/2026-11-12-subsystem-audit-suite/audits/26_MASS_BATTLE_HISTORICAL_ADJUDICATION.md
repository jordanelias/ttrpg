# 26 · Mass battle against history: adjudication of movement, behaviour and results

## Status: REFERENCE (an adjudication; resolves nothing at runtime, CLAUDE.md §0.05; queues nothing)

## Read at: `4573158` (working tree, 2026-11-12)

Jordan, 2026-11-12: *"Refer to historical battles and military academic works and step by step diagrams of
military maneuvers and war games for mass battle, regarding how it should be functioning re movement and
behaviours and results; Fable to adjudicate and fold."* Standing rules: *"All ungrounded information should
have info available on repository"*; *"Do not guess."*

## 0. Verdict

**The engine's skeleton agrees with the history that could be read at the page, and its results do not yet,
for one reason: it decides a battle by wearing a body down to a casualty band, and stops there, where the
sources decide a battle by a shock to a body's will at small loss and do most of the killing afterwards.**
Local morale that breaks in sections and spreads, depth as a store of fresh men, facing and the cost of being
taken in flank or rear, a braced line that stops horse, giving ground as a state between holding and running,
conditional orders and a prearranged signal: each of these is in `modules/mass_battle/` and each is what
Sabin, Krentz, du Picq and the battle accounts describe. What history asks for and the engine lacks is
narrower than the earlier lanes' lists suggest and is the same handful every time: a break that can come
before the casualties do; a rout that has an aftermath (rally, pursuit, prisoners) which costs the pursuer;
orders that take effect by a draw; a battle that is several bouts with lulls in which a commander relieves,
commits and re-forms; fatigue that arrives with the army and is spent by moving fast; and one stated scale,
because at the only scale where a body has ranks the missile range in the code is a javelin's. Seven of the
suite's MB proposals are confirmed by the sources and amended in place; five new proposals carry what was
missing; one conflict with a value Jordan set (the 15% floor of the rout band) survives the ladder and is in §7.

**What was sourced.** Two peer-reviewed articles were read in full at the page image (Krentz 1985 on
hoplite casualties; Sabin 2000 on Roman infantry combat). Du Picq and Clausewitz were read in part through
the fetch tool. Eleven battle pages, eight topical pages and three wargame rule sources were read through
the fetch tool. **Not reached at any tier above a snippet:** Delbrück, Oman, Keegan, Dupuy, Goldsworthy,
Hanson, Engels, Vegetius's own text, the *Strategikon*, any drill regulation or diagram. The four research
notes say so in their own "not established" sections; nothing in this file rests on those works.

## 1. Sources: where each is filed, and at what tier

Tiers: `[D]` page images read in full by this lane; `[T]` page fetched and read through the fetch tool (a
small model's reading; a lead stronger than a snippet); `[S]` search snippet; `[M]` memory, not used.

| filed at | covers | strongest tier in it |
|---|---|---|
| `research/historical/mass_battle_casualties_and_results_grounding.md` | who loses how much, when; duration; what decides (rows A1–A14, B, C1–C7, D1–D8) | `[D]` Krentz, Sabin |
| `research/historical/mass_battle_movement_and_behaviour_grounding.md` | rates, frontage, formation change, fatigue, command, cohesion, rout, rally, pursuit, horse against foot (rows M, F, X, T, E, R, P, H) | `[D]` Sabin; most rows `[T]`; four `[S]` |
| `research/historical/mass_battle_maneuver_sequences_grounding.md` | eleven numbered sequences (approach, formation change, horse on pikes, horse on a line, archery to melee, feigned retreat, envelopment, line relief, fighting march, rout and pursuit, siege assault) | `[T]`, each step cited |
| `research/historical/mass_battle_wargame_models_grounding.md` | Kriegsspiel, DBA, Lost Battles, Total War: Rome II; Field of Glory by the tree's own R6; a convergence table | `[T]`; R6's rows are that lane's `[V2]` |

Cited below as **CR** (casualties and results), **MV** (movement and behaviour), **SQ** (sequences), **WG**
(wargames), with the row id.

### What the repository already held, and its tier

| path | what it sources | tier, by its own statement | open issue |
|---|---|---|---|
| `research/pre_firearms_formations/01`–`09` | formations by period; 29 throughlines; a matchup matrix | memory; no Status line; no source list | the matrix cites Marignano as a pike win against chunk 05's defeat (`DG_researchB2.md:274`); chunk 06 orders Chaldiran after Marj Dabiq |
| `…/10_battle_phase_choreography.md` | eight-phase frame; speed, range and frontage tables (`:300-347`) | memory; "observations, not specification" | frontage table internally inconsistent (`DG_researchB2.md:287`); none of its numbers is page-sourced |
| `…/12_moment_by_moment_dynamic_spacing.md` | nine battles; generic windows | memory; minute figures derived (`:936-938`) | **two factual errors never edited back**: Panipat sally gaps (about 90–180 m apart, not 30–50 m), Lodi's elephants (about 1,000, not 100+); four P2 errors (`13_…:18-154`) |
| `…/13_verification_corrections.md` | a web cross-check of file 12 | self-authored, web-checked, sources named loosely ("Goldsworthy via Cassell's") | Hastings and Adrianople not checked (`:314`) |
| `…/14`, `15` | a method: 50 m tile, 5-minute turn, 36–72 turns (`14:89`, `15:311-318`) | proposal | **rival to the engine's grid**; see row S-1 |
| `…/16_historical_vs_gamedesign_audit.md` | drift findings against Football Manager and Unicorn Overlord shapes | self-audit | its Drift 1 (no enemy-plan preview) agrees with the suite's `FieldWindowView` (own side only) |
| `research/historical/mass_battle_gauge_grounding.md` | the gauge bands; fresh-against-tired (Sabin, Zhmodikov, du Picq, Clausewitz) | DOIs given; **no record that any page was read** | ceilings raised after the engine exceeded them (C5 to 98, C7 to 100, `:115-116`); C7 saturates at 100 |
| `research/historical/precedents_warfare.md`, `precedents_analysis.md` | 2026-04-17 precedents | memory | several proposals cut in their own §8 |
| `research/game_precedent_suite/tables/R6`, `tutorials/T07`, `dispositions/D_T07`, `R2` | Total War, Field of Glory II, Ultimate General, Bannerlord | `[V2]` manual pages read | relied on here for Field of Glory and Total War |
| `.audit/2026-07-04-…-cannae-gauge-audit`, `2026-07-08-…-gauge-architecture-audit`, `2026-07-02-…-movement-pathing-audit`, `2026-07-22-…-stress-test`, `2026-07-26-…-fable-audit` | earlier engine audits | referents only | read at their entry points; nothing below relies on an old finding that the suite's lanes did not re-verify |

Sabin's article is cited by the gauge note (`:130`) for line relief. This lane's full read confirms that use
and adds what the note did not take from it: the casualty asymmetry, the first-shock decision, and the
stand-off model (CR A5–A11, D1–D6).

## 2. Reading disclosure

Read in full: `AUDIT_BRIEF.md`, `unified/DECISIONS_ANSWERED.md`, `CLAUDE.md`,
`research/historical/mass_battle_gauge_grounding.md`, `research/pre_firearms_formations/13`, the suite
proposals amended in §8, `proposals/16_PESSIMIST_MB_*` (two of three), `14_VERBS_MILITARY_A`, `_D`. Read
through the suite's digests and not in the original: `research/pre_firearms_formations/01`–`12`, `14`–`16`
(`digests/DG_researchB2.md:152-288`, `DG_researchB3.md:7-91`). Read at head and at the sections cited:
`audits/04_MB_audit.md` (§0, §1.1, §3.A, §7, §8), `research/game_precedent_suite/tables/R6`. **Not read:**
`audits/04_MB_audit_addendum_B.md`, `16_PESSIMIST_MB.md`, `14_VERBS_MILITARY.md`, `14_VERBS_PHYSICAL.md` as
whole files (their proposals were read); `.designs/systems/mass_battle/reference/*` beyond two greps;
`proposals/2026-09-25-squad-engagement-*`, `multiunit_envelopment_plan.md`,
`mass_battle_fighting_withdrawal_v1.md`, `pc_formation_system.md`,
`weapon_physics_and_concentration_model.md`; the five `.audit/` directories beyond their file lists;
`research/historical/precedents_*.md`. Engine claims below cite the code line opened, or the suite file that
measured them, named as that lane's evidence. No engine run was made by this lane.

## 3. The adjudication table

"Engine says" cites what was opened at `4573158` or the suite lane that measured it. "Decision" is what the
game should do. "Owner" is the single file that carries the fact. "Gate" is the execution artifact.

### 3.1 Movement

| id | topic | history and wargame practice | engine and suite | decision | owner file | gate |
|---|---|---|---|---|---|---|
| S-1 | **What a cell and a tick stand for** | A man in close order takes about 3 ft of front, up to 6 in open order (MV F1, `[D]`). Bodies stood 6 to 16 deep (MV F3). Bow and crossbow reach about 200 m, a heavy javelin 20–25 m (SQ 5; CR via ACOUP). Stated wargame steps run 2 to 15 minutes (WG K1, D1, L1). | No metric anywhere: `registry.py:92-93` declines "an unratified meters-per-lattice-unit conversion". Field 51 x 51, 18 ticks, volley 2–8 cells (`config.py:14`, `:188-189`, `:425`), approach 3 rows (`orderofbattle.py:67`). Season armies are 60 to 900 men (`04_MB_headcount_grade_and_scale.md`). The tree's research proposes 50 m tiles and 5-minute turns (`14_…:89`), which gives foot 0.6 km/h at one cell a tick. | **One scale, stated once as data, at the size the game fights:** a cell is 16 men in close order, about 4 m square (four files by four ranks at Polybius's interval); a tick is about four seconds of ordinary pace; an 18-tick engagement is **one bout** of about a minute. The 50 m, 5-minute proposal is rejected for this engine. At this scale the 8-cell volley is javelin range and bows reach the whole board, so range becomes per arm and the sides deploy a missile range apart. | `references/troops.yaml: deployment.scale`, `arms.*.range`, `formations.*.approach_rows` | `26_MASS_BATTLE_cell_scale_and_time.md` gates 1–4 |
| M-1 | Pace of formed foot | Battlefield pace before 1700 **not established** (MV M9). Around 1800: 57 and 82 m a minute `[S]`. Lost Battles gives all foot one move (WG L4). | Every foot type one cell a tick (`geometry.py:328-338`); first contact tick 3 for all (`04_MB_audit.md` F-MB-19). | **Agree; abstraction is right.** No source read separates heavy from light formed foot on the field. A `pace` column exists so Jordan can separate them; its seeds reproduce today. A foot body is slowed only by its load (the carry factor) and by ground. | `troops.yaml: troops.<kind>.pace` | `26_MASS_BATTLE_movement_and_fatigue_as_data.md` gate 1 (digests equal) |
| M-2 | Horse to foot | Trot 13 km/h against foot 3.4–4.9: 2.7 to 3.8 (MV M1, M3). Lost Battles 2 : 1 (WG L4). | `MB_CAVALRY_SPEED_MULT = 3.0` (`config.py:376`), keyed on `is_mounted`. | **Agree on the value.** It moves from a constant behind a name test to the mounted rows' `pace: 3`. | same | same |
| M-3 | Speed costs wind | A horse gallops 1.5–3 km before it must rest (MV M1). Total War's manual: "do not run everywhere" (WG T3). Richard waits for the enemy's horses to tire (MV T6). | An enveloping body moves at twice its pace for nothing (`config.py:385`); a mounted body at three times for nothing. Stamina drains only per clash (`percell`, as `16_PESSIMIST_MB_one_stamina_ledger.md` tabulates). | **Conflict; history is stronger.** A tick moved above base pace drains the column ledger. One rule for foot and horse. The magnitude is not sourced and is a seed. | `troops.yaml: fatigue.fast_move_drain` | movement proposal gate 3 |
| M-4 | Ground | Kriegsspiel: cavalry 250 of 400 paces in light forest, 100 uphill (WG K1). Lost Battles: rough ground costs horse double, foot nothing extra (WG L4). Mud at Agincourt (SQ 5). | Terrain is a row for the whole field and changes dice only (`massbattle.py:411-422`); no effect on movement. | **Conflict; history is stronger, for horse.** The terrain row gains a `pace` multiplier for mounted troops (seeds from Kriegsspiel: broken ground 0.6, uphill 0.25). Foot stays at 1.0: no figure was read, and a slower approach for everyone only spends ticks. | the terrain table beside A.9's rows (`modules/mass_battle/terrain.py` today; `troops.yaml: terrain` when the file lands) | movement proposal gate 2 |
| M-5 | Changing formation | Takes time; fatal within reach of the enemy; done in a pause (MV X1–X4; SQ 2). Pre-gunpowder times not established (X6). | `shape` is not order-settable (`units.py:271-290`); `check_drift` changes a shape at once when Discipline is below a floor, and loses per-cell morale (`04_MB_audit.md` F-MB-18). | **Conflict.** `shape`, `ranks` and `files` become order-settable **only out of contact**, for a cost in ticks during which the body's pools are zero, shorter for drilled troops. Same rule as the weapon switch ("costs a tick"). | `hierarchy/units.py::_ORDER_SAFE_FIELDS`, `rekey_cells`; `troops.yaml: reform_ticks` | manoeuvre proposal gate 4 |
| M-6 | Fatigue in the fight | Front-rankers tire fast; supports held out of reach stay fresh; "fresh men fighting tired ones" was the Roman edge (CR D3; MV T1–T4, `[D]`). | The column ledger does this (drain per clash, rest out of contact, damped by depth); the unit ledger is inert and is the one reported (`16_PESSIMIST_MB_one_stamina_ledger.md`). | **Agree with the column ledger and with that proposal.** Confirmed by the strongest source read. | that proposal | its gate |
| M-7 | Arriving tired | The French at Crécy attacked after a 12-mile march against men "rested and fed"; Arsuf marched only in the cool (MV T5). | No input: every field starts at full stamina. `entry_stamina` is proposed with no writer. | **Decide the writers:** the march's band (an army that "arrives spent" enters at a lower share), a second field in one season round, and the carry factor. Values are seeds. | `engine/season/seam/wrappers/mass_battle.py::field_input` | movement proposal gate 4 |
| M-8 | A second weapon's cost | **No sourced magnitude** (MV T7). That archers closed with swords, hatchets and mallets is sourced (SQ 5). | Proposed: carry factors from personal combat's function (`04_MB_unit_loadout_and_weapon_in_hand_B.md` §5). | **Agree with the proposal's form.** The trade is Jordan's design; its numbers are content and stay marked as seeds. | that proposal | its stage 4 |

### 3.2 Behaviour

| id | topic | history and wargame practice | engine and suite | decision | owner file | gate |
|---|---|---|---|---|---|---|
| B-1 | Offering and declining | Battles were declined; armies stood for hours; the side in position first is rested (SQ 1; MV E2). | `field_estimate`, `retreat_at`, `surrender`, `besiege` are built and dark (`04_MB_audit.md` §7). | **Agree with the suite** (`04_MB_playable_field_scenario.md`). Added: the defender who stands gets the missile phase (S-1) and the fresher start (M-7). | that proposal | its gates |
| B-2 | Orders | Few, coarse, set before contact, released by a prearranged signal (SQ 1 step 5; MV E3). Unicorn Overlord's conditions and Ogre Battle's tactic are the same shape (WG). | Triggers and behaviours exist (`units.py:309`, `:271-290`); the suite puts at most four on a unit row and gives the general one action a window. | **Agree; this is the right abstraction.** Two triggers are added that the manoeuvre set needs: `enemy_broken` and `in_lull`. | `04_MB_manager_battle_one_resolver.md` §2; `26_MASS_BATTLE_maneuver_orders.md` | manoeuvre proposal gates |
| B-3 | **Orders are obeyed by a draw** | Friction (MV E1); orders ignored at the decisive moment (Arsuf, Crécy, Bannockburn: MV E4); the Kriegsspiel umpire delays and reinterprets (WG K4); DBA and Lost Battles make command a die (WG D2, L3). | A fired order is applied by `setattr` with certainty. The one stochastic friction is a per-battle multiplier on a side's whole strength, sigma 1.1 (`config.py:331`; ruled, `ED-MB-0016`), which the first audit measures as swamping every choice (F-MB-08). | **Conflict of form.** Each order, signal and general's action takes effect by a draw on the commander's Command and the unit's Discipline: at once, a tick late, or not at this window. This is the standing rule's own case ("obeyed" with no roll). The ruled multiplier is not touched here; see §7 item 2. | `core/contact.py::check_orders` (the one place an order is applied) | manoeuvre proposal gate 1 |
| B-4 | **What breaks a body** | "The breaching of their line, a psychological shock such as the death of the general, or the sheer accumulation of casualties and fatigue" (CR D1). Many clashes "decided at or before the first shock"; "tearless battles" (CR D5). Collapse starts at the rear and spreads (CR D6, D7). | A subunit draws a breakpoint in **casualty fraction** between 0.15 and 0.30 (`config.py:182-183`, Jordan's value); cells break locally and pull on neighbours (`:111-112`); an allied rout forces a Discipline check. A loss of the general sets morale to zero for the whole army (`battle_loop.py:408-413`). | **Conflict; the page-read sources are stronger.** Keep the band as the attrition trigger. Add the **stand draw**: a body charged, struck in flank or rear, or seeing its officer fall draws on Discipline; it stands, gives ground, or breaks, at whatever its losses are. The general's fall becomes that draw for each unit, not an army-wide certainty. The floor of the band is listed in §7 item 1. | `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1; `battle_loop.py`, `orchestration.py` | its gates 1, 2 |
| B-5 | Giving ground | A line could be pushed back hundreds of yards and not break; could win afterwards (CR D4; MV R3). Hail Caesar and DBA have "give ground" and "pushed back" as results (WG). | `yielding` exists with a commanded and an emergent entry, a rally exit and a pocket exit (`config.py:255-270`). | **Agree; built.** It is the middle result of the stand draw (B-4) and the holding unit's order in an envelopment (SQ 7). The report names it. | `proposals/mass_battle_fighting_withdrawal_v1.md` (the tree's); `04_MB_playable_field_scenario.md` §D | rout proposal gate 2 |
| B-6 | When the army is beaten | No historical number. Wargames: a third destroyed (DBA), 60% routed (Field of Glory II), half the divisions (Hail Caesar). | Army routs at 60% of troops in routed bodies (`config.py:114`). | **Agree.** Inside the range independent designs converge on. | none | none |
| B-7 | Rally | Light troops ran, outdistanced pursuit and rallied; heavy troops rarely could (MV P1, `[D]`). A leader stops a panic in person (MV P2). Total War: a general rallies within his radius; shattered troops never (WG T2). | None: `rally_check` is `pass` (`orchestration.py:271-273`). Proposed: one Command draw at the end of the field (`16_PESSIMIST_MB_rout_has_two_exits.md`). | **Agree with that proposal, amended:** the obstacle is a step harder for heavily armoured foot and a step easier for mounted and unarmoured troops; a rally inside a bout (the general's `rally` action) steadies a wavering unit and never recalls a routed one. | that proposal; `troops.yaml: armour.*.rally_step` | rout proposal gate 3 |
| B-8 | Pursuit | Where the dead are made (CR A7, A12, A13). Done by horse and light troops; foot for a few kilometres (MV P3). The pursuer scatters and is exposed; commanders recalled it (MV P4). Half the loser's loss could be prisoners (CR A6). Horse that pursues is gone until it comes back (MV P5). | Unreachable on the season path; gated on a speed no season unit has (`16_PESSIMIST_MB_rout_has_two_exits.md`). One call removes a mean 73% of survivors. | **Agree with that proposal, amended three ways:** the loss is split by draw into dead and taken; a pursuing body is out of the fight and tired afterwards; a body whose opponent breaks **inside** a bout draws on Discipline (and reads its standing order) to pursue, hold or turn on the next enemy. | that proposal; `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §3 | rout proposal gates 3–5 |
| B-9 | Reserves and relief | The commander's chief act (MV E6). Relief happened in lulls, the lines a few yards apart (SQ 8). Lost Battles makes "Fresh" a thing that is spent (WG L6). | A `reserve` post and a held order exist or are proposed; relief is not an order; the season fights one bout. | **Conflict by omission.** A battle is up to `max_bouts` bouts; between them is a lull in which the general may relieve one unit by another, re-form, commit a reserve or withdraw. | `26_MASS_BATTLE_cell_scale_and_time.md` §3; `26_MASS_BATTLE_maneuver_orders.md` | scale proposal gate 5 |
| B-10 | Flank and rear | Decisive by shock and by crowding (CR D2, `[D]`). Field of Glory drops cohesion a state on a flank charge (WG G2). | Rear damage doubled; multi-side shock; envelopment-shock coupled to morale (`config.py:225-231`; `battle_loop.py:416-417`). The gauge's row C7 reads 100 of 100 (`mass_battle_gauge_grounding.md:95`). | **Agree on mechanism.** A matchup at 100% is a certainty, which the standing rule excludes whatever Cannae was; it becomes a calibration reading with a ceiling below one. | `26_MASS_BATTLE_calibration_targets.md` T-7 | its sweep |
| B-11 | Horse on steady foot | Frontal charges "often failed"; success came from the foot breaking; steady pikes and squares held (MV H1–H3; SQ 3). | Brace recoil; contested against unbraced steady foot (46%), repelled by a brace (2%), near-total against shaken foot (`mass_battle_gauge_grounding.md:87-97`). | **Agree in direction.** The gauge's sources for these bands are cited by DOI with no page read recorded; the bands stay readings, not gates. The stand draw (B-4) is the mechanism the sources describe. | none | calibration T-6 |
| B-12 | Archers reached, and archers out of arrows | Archers closed with hand weapons when their arrows were spent, against a tired and crowded enemy (SQ 5 step 5). Unengaged archers shot into a melee from the flank (SQ 5 step 6). | A reached missile body goes on volleying while fought (`04_MB_audit.md` F-MB-19). Proposed: `in_hand`, a `volleys_spent` trigger, a tick to switch (`…_B.md` §4). | **Agree with the proposal, amended:** a body **itself in contact** does not volley, whichever weapon is in hand; a body not in contact may shoot into one. | that proposal | its stage 3, one added row |
| B-13 | The feigned flight | Three uncertain steps: keep order while running; the enemy takes the bait; the turn succeeds (SQ 6). | Two of the three draws exist and are unreached (`config.py:232-245`). | **Agree; reach it.** The first draw (the feigners' own Discipline, failure being a real rout) is added. | `26_MASS_BATTLE_maneuver_orders.md` row 6 | its gate 3 |

### 3.3 Results

| id | topic | history and wargame practice | engine and suite | decision | owner file | gate |
|---|---|---|---|---|---|---|
| R-1 | The victor's loss | About 5% dead, 3–10% typical, never above 10% in 17 hoplite battles; about 5% for Roman victors; 11% at Cannae (CR A1, A5, B). | Mirror field, n 200: winner 7% (as `16_PESSIMIST_MB_rout_has_two_exits.md` records; not re-run). | **Agree**, with the caution that history counts dead and the engine counts men lost to the fight. | calibration T-1 | sweep |
| R-2 | The loser's loss without pursuit | About 14% dead, 10–20% typical; ratio to the victor's 1 : 2.9, range 1 : 1.7 to 1 : 5.2 (CR A1). | Mirror: loser 37% before any pursuit; ratio 1 : 5.3. | **Mild conflict.** The ratio sits at the top edge of Krentz's range before any killing in flight is added. The stand draw (B-4) lowers it: bodies that break on a shock have lost less. Target is the ratio, which has no unit. | calibration T-2 | sweep |
| R-3 | The loser's loss with pursuit or encirclement | "Over half … killed or taken prisoner" often (CR A6); Zama and Cannae near total. | None today; proposed pursuit adds a mean 73% of survivors. | **Target a ratio:** loss with mounted pursuit two to five times the loss without; never certain destruction. | calibration T-3 | sweep |
| R-4 | What the loss is | Dead; and, for the beaten, prisoners (CR A6). Wounded not counted. | A share of `body` written to cohorts and persons (`_eff_march`); no captives (`04_MB_audit.md` §7). | **Decide the unit:** the field returns, per side and per part, `fight_loss` and `pursuit_loss`, and of the latter the share `taken`. Who among the hurt dies is the season's draw, not the field's. Captives go to the custody the PHYSICAL lane's `capture` already owns. | `FieldOutcome` (`04_MB_typed_outcome_and_one_path.md`); `14_VERBS_PHYSICAL_A_custody_and_force.md` | rout proposal gate 5 |
| R-5 | Decisiveness | A bout is often indecisive; a battle is usually decided, sometimes at the first shock, sometimes by night (CR C1, D5; SQ 10 step 7). | An even 18-tick engagement is usually indecisive, and still so over 72 ticks (`04_MB_playable_field_scenario.md`, the problem). | **Agree that a bout is indecisive; conflict that a battle is.** Decision comes from B-4, B-8 and B-9, not from more ticks. | scale proposal §3 | its gate 5; calibration T-4 |
| R-6 | Duration | One to three hours typical; one hour fast; five to eight attested (CR C2, C4, C5). Most of it is stand-off (MV T1). | 18 ticks; no stated time. | **The game counts bouts, not minutes.** A bout with its lull is reported as about half an hour, so six bouts is Vegetius's upper figure. A presentation datum with one reader (the report). | `troops.yaml: deployment.scale.bout_minutes`, `max_bouts` | scale proposal gate 6 |
| R-7 | What a win is | One side "finally broke and fled" (CR A11); the victor holds the field. | Jordan's ruling A-3: won, lost or drawn, read off which side broke or conceded. | **Agree.** The ruling is the historical definition. Lost Battles' margin against the historical result (WG L8) is a scoring device and does not transfer. | `seam/ladder.py::field_degree` (as the suite proposes) | none added |
| R-8 | Numbers | The linear law is the one stated for hand-to-hand fighting (CR D8). Depth alone did not win (CR D3). Lost Battles caps how many units may attack from a zone (WG L5). | `04_MB_cr12_linear_law.md` decides that numbers leave the melee dice and act through frontage. | **Agree with that proposal.** Three independent supports. | that proposal | its gate |
| R-9 | Auto-resolve | Board games have one resolver by construction; the one computer game read with two has two answers (WG reading 7). | Jordan's ruling A-1. | **Agree.** The bouts, the stand draw and the pursuit are all inside the one call or are further calls of it. | none | manager proposal gates 1, 2 |

## 4. Where abstraction is right, and where it is not

Right, and to be kept:

- **One pace for formed foot** (M-1); **one terrain row a field** (M-4), since the season fights on a territory
  and not on a surveyed map.
- **Orders as a short list of conditions set beforehand** (B-2). It is what a pre-modern commander had, and
  what Ogre Battle, Unicorn Overlord and Football Manager give the player.
- **The stand-off is not simulated.** Sabin's default state, the hours in which the lines watch each other,
  is the lull between bouts. The engine models the flurries; the report counts the time.
- **Pursuit and rally as end-of-bout draws**, not as a chase on the grid: no wargame read models pursuit on
  the table except by troop type (WG reading 5).
- **Siege works are not cells** (SQ 11): the choice to invest, treat or storm is the game.
- **Lost Battles' twenty zones would be too coarse** for a game that wants flanks, depth and a line that
  bends; the cell grid is the right middle.

Not right, and decided against:

- **A per-day strength multiplier standing in for friction** (B-3), on form.
- **A casualty band standing in for morale** (B-4).
- **Free speed** (M-3) and **ground that never slows horse** (M-4).
- **A single bout standing in for a battle** (B-9, R-5).
- **The 50 m tile and 5-minute turn** of the tree's research (S-1): it fits armies of tens of thousands and a
  different engine.

## 5. The tree's research: corrections owed, recorded here only

This lane edits no file under `research/pre_firearms_formations/`. For a reader of those files:

- File 12 still carries the figures file 13 corrects (Panipat's sally gaps and elephants; Cannae's frontage;
  Pharsalus's fourth line; the direction of Agincourt's funnel; Marignano's duration). Use file 13.
- Agincourt, from the page read: the English held 690 m; the French lines were about 16 deep; the fighting
  lasted about three hours (SQ; CR C5). The page does not give the funnel's two widths; file 13's are its own.
- "Archers drop bows for mallets" (`05_…:194`, `:218`) is confirmed for Agincourt and **not** found for Crécy.
- The 15–30% rout band's attribution to du Picq is not supported: no percentage was returned from the 200,000
  characters of *Battle Studies* read (CR A14).
- The speed, range and frontage tables in file 10 (`:300-347`) remain memory tier. Three of their rows now
  have a page-read counterpart: horse gaits (MV M1), frontage a man (MV F1, F2), longbow and crossbow rate and
  range at Crécy (SQ 5; W-CRE: "up to ten arrows per minute", crossbows "about twice a minute", range disputed
  between 200 and 300 m).

## 6. Not established (so not quoted, and not built on)

Battlefield pace of formed foot before 1700. Any foot terrain multiplier. Any pre-gunpowder time to change
formation. The length of a bout of hand-to-hand fighting. Any casualty rate per unit of time. The share of a
loser's dead that fell in flight. Any loss at which troops break. A dead-to-wounded ratio. The cost of a
second weapon. Stage distances of a medieval charge. Win probability as a function of force ratio. The text
of Clausewitz on the culminating point. Any drill diagram. "Erwin on march rates" (author not identified).

## 7. Survivors for Jordan

Two. Each was taken down the five steps and stopped at none.

1. **The floor of the rout band.** `ROUT_ONSET_FRAC = 0.15` is Jordan's value ("routs occur as early as 15%
   losses", `config.py:182`). Krentz and Sabin, read at the page, describe routs at or before first contact
   with almost no loss, and put a beaten hoplite army's whole loss at about 14% dead. Option (a): the band
   stays as the *attrition* trigger and the stand draw is added beside it, so a body can break below 15% on a
   shock (the proposal as written; the band is not edited). Option (b): the band is the only way a body
   breaks, and shocks only move the draw inside it. Under (a) a charge that is pressed home can win a fight
   in its first seconds and cavalry, flanks and officers decide battles; under (b) every battle is an
   attrition contest whose loser has already lost a sixth of his men, and pursuit has less left to do. The
   proposal builds (a) behind a switch with (b) as the control.
2. **Friction as a multiplier on a side's whole day** (`ED-MB-0016`, closed again at `ED-MB-0080`), already
   listed by the first MB audit (§11 item 2). This lane adds the evidence and does not re-raise the ruling:
   the sources and three wargames put friction on **orders** (delay, misreading, refusal), and none read puts
   it on a side's whole fighting value. Option (a): keep the multiplier at 1.1 and add order friction (B-3),
   accepting that the day's luck still outweighs most choices. Option (b): once order friction, the stand
   draw and the pursuit draw exist, lower the multiplier so that the sum of chance in a field is what it is
   today. The second is a game in which a manager's orders show in the result.

## 8. Decisions folded (each edited file carries a `Folded:` line; no finding of another lane was deleted)

| file | what was folded |
|---|---|
| `proposals/04_MB_cell_hierarchy_as_data.md` | S-1: the scale block; seeds for `ranks` by the sourced depths; `approach_rows` from the longest missile range |
| `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` | B-12: a body in contact does not volley; per-arm ranges at the stated scale; M-8: the cost has no historical magnitude |
| `proposals/04_MB_manager_battle_one_resolver.md` | B-2, B-3: two triggers; an order takes effect by a draw (and what that does to its gates 1 and 2); B-9: the lull as a window |
| `proposals/04_MB_playable_field_scenario.md` | R-5, B-9: bouts inside the one scene under A-9 |
| `proposals/04_MB_cr12_linear_law.md` | R-8: three supports |
| `proposals/16_PESSIMIST_MB_rout_has_two_exits.md` | B-7, B-8, R-4: rally by troop weight; dead and taken; the pursuer's price; pursuit inside a bout |
| `proposals/16_PESSIMIST_MB_one_stamina_ledger.md` | M-6, M-7, M-3: confirmed by Sabin; the writers of `entry_stamina`; fast movement drains |
| `proposals/14_VERBS_MILITARY_A_movement.md` | M-7: the `Partial` band of a march is what enters a field tired; sourced march rates as a cross-reference |
| `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | B-3: the obedience draw it lists for MB now has an owner |
| `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` | R-4: men taken in a pursuit arrive as captives under its `war` context |

New proposals: `26_MASS_BATTLE_cell_scale_and_time.md`, `26_MASS_BATTLE_movement_and_fatigue_as_data.md`,
`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`, `26_MASS_BATTLE_maneuver_orders.md`,
`26_MASS_BATTLE_calibration_targets.md`.

## 9. Evidence log

No engine run. Web: 2026-11-12, some fifty fetches and searches; search terms carried no repository, project
or user detail. Page images read: Krentz (8 pages), Sabin (17 pages), from the two PDFs the fetch tool saved
outside the repository. Refused or missing: `clausewitz.com` (403, three pages), a Vegetius text (two
addresses), the *Medieval: Total War* community wiki (403), the Battle Brothers wiki (402), an Army Heritage
bibliography (404). Code opened at `4573158`: `modules/mass_battle/config.py` (constant lines cited),
`troop_types/registry.py:1-110`, `geometry.py:328-338`, `terrain.py:1-80`, `hierarchy/units.py:271-340`,
`orchestration.py:2054-2102`, `:271-273`, `battle_loop.py:405-416`, `orderofbattle.py:67`.
