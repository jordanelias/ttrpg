# Mass battle — completion proposal (T04 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/2026-10-22-system-description-05-t04-mass-battle.md` (cited `T04 §n` / `T04:L`) and `…-00-overview.md` §2.1-§3, §5.2, §6; `research/game_precedent_suite/dispositions/D_T04.md` (cited `D_T04 #n`); `research/game_precedent_suite/THROUGHLINES.md` (`P##`, `TM##`); `proposals/2026-10-16-verbs/2026-10-16-verbs-10-lexicon-mass-battle.md` (`L10 §n`) and `…-20-gap-register-mb-and-fa.md` MB half (`MB-G##`); `proposals/2026-10-21-v9-remediation/` parts 02-04 (RB-3, REM-27, REM-32, JQ-1…JQ-6); `workplans/valoria_master_workplan_v9_part4.md` IN-52; `proposals/mass_battle_fighting_withdrawal_v1.md`, `proposals/multiunit_envelopment_plan.md`, `proposals/2026-10-16-troop-stock-design*.md`; code opened at HEAD as cited.

Path abbreviations as T04: `MM/` = `modules/mass_battle/`, `MB.py` = `MM/massbattle.py`, `SW` = `engine/season/seam/wrappers/mass_battle.py`,
`EC` = `engine/season/loop/effects_combat.py`, `VT` = `engine/season/verb_table.yaml`, `RY` = `engine/season/rosters.yaml`, `orch` =
`MM/orchestration.py`, `units` = `MM/hierarchy/units.py`, `cfg` = `MM/config.py`. Evidence grades are the suite's (RUNS-IN-LOOP, TESTS-ONLY,
DESIGN-ONLY), carried and never upgraded. `[UNVERIFIED]` marks a claim whose code I did not open at `2decf4a`.

**The one-line reading of the subsystem today.** A battle laboratory of about 10,000 lines (`MM/`) sits behind one season verb, `march`,
that hands it two one-subunit armies of 1-6 troops built from defaults; both rout on tick 1, the defender takes every tie, and no natural
run at seeds 0-2 names a settlement, so no field is fought (T04 §0 Status, §3.1, §3.3). The remediation already repairs two of the three
reasons no field is fought (REM-27 the target, REM-32 the scale form; JQ-4 the scale value). This proposal builds what a campaign-war
player expects on top of those repairs, and nothing they already do.

## §0 The genre loop

The yardstick is TM09, *campaign war* (`THROUGHLINES.md:136`): P20 upkeep → P18 capped roster → P36 pre-battle intent → P35 automatic
resolution (or played) → P34 cohesion and break → P32 lasting mark → P37 supply then attrition, with "when and on whose terms to engage;
fight or delegate" as the choice it leaves. Every campaign-war title in the suite (Total War, Field of Glory II, Dominions, Brigandine,
Unicorn Overlord, Bannerlord) affords the nine opportunities below; the tenth is the half with no player in it (throughline 6).

| # | opportunity (what a person chooses · at what cost · with what lasting consequence) | precedent | today | evidence grade |
|---|---|---|---|---|
| G1 | **Raise a force.** Choose whom to call up and from where; pay in consent, stores or the callers' own working time; the raised force exists across seasons until disbanded. | D_T04 #1, #2, #36, #52; P18, P20; L10 Suite 1 | ABSENT. The army is whoever of the seat's faction happens to live at the marcher's home settlement (`loop/sides.py:115`, T04 §5b). No `levy`/`muster` verb among 56 `VT` rows (grep at HEAD). | — (DESIGN-ONLY in L10) |
| G2 | **Keep a force.** It eats and is paid each season; unfed or unpaid it loses heart and leaves. | D_T04 #2, #48; P20; TW Recruit/Disband (D_T04 #2) | ABSENT. IN-52's `field_provisioning` (levied stores bound a field) is planned, unbuilt (grep: 0 hits in `engine/`, `modules/`). | DESIGN-ONLY (v9 IN-52) |
| G3 | **Set the plan before battle.** Who leads, formation, stance, a reserve, when to pull back: written once, executed by the engine unwatched. | D_T04 #22, #27, #40, #42; P36, P17 | PARTLY. Orders, roles, stance, officers all act engine-direct (T04 §3.2: Arrowhead without charge 36.0 % v 43.5 %; command 0 0/200). The season fixes one Line `infantry` block, command 4 (`MB.py:170-232`). | TESTS-ONLY (engine) |
| G4 | **Choose where and when to engage.** March on a place; the force travels; arrival meets the defender. | D_T04 #3, #9; P35 | PARTLY. `march` folds and fights the same round; the natural run names no settlement (REM-27 repairs the target). | wiring RUNS-IN-LOOP (refusal only); field TESTS-ONLY |
| G5 | **Decide at contact.** Read the odds; fight, withdraw at a price, or offer terms. | D_T04 #3, #13, #34, #41, #55, #59; P23 shown odds | ABSENT. No decision point between Declared and the battle; the chooser sees verb identity, not odds (overview §6 #1). | — |
| G6 | **A battle that the force's quality and its commander decide**, with rout and rally. | D_T04 #15-#18, #29; P34, P35 | PARTLY. Flank/rear lethality and the 60 % break exist (HAS, TESTS-ONLY); rally is an empty hook (`orch:288-290`); command is not in the pool and acts only at 0 (T04 §3.2). At season scale the 100-troop size line routs both sides on tick 1 (T04 §2.1 step 6). | TESTS-ONLY |
| G7 | **Besiege or storm a walled place; campaign under supply.** Time spent before walls wears the defender's stores; the attacker pays in rations. | D_T04 #9, #10, #53; P37, P04 | ABSENT. WALLS is a binary DR +3 on all 37 settlements that never decays (garrison wear 0, `RY:1451-1470`; T04 §3.3). | — |
| G8 | **Aftermath.** Captives, occupation, sack; the winner keeps what it won; persons carry the field (wounds, a grudge, a name). | D_T04 #7, #20, #49, #62; P32, P14 | PARTLY. Won moves presence (`_relocate`), losers lose body and gain two stance rows (`EC:257-310`); `seize` moves title, `raze` ends a place (B-R, `VT:1107-1124`); no captive, no winner's cost or gain. | TESTS-ONLY (`test_march.py`) |
| G9 | **Defend.** Reinforce the threatened place, hold, sally or yield it. | D_T04 #34, #44, #55; L10 Suite 4 | ABSENT. Defence is presence; walls apply by themselves; the defender has no chooser (T04 §5a, trap 8). | — |
| G10 | **Wars happen unwatched.** Rival seats raise forces, march, win and lose, and the map's holders and grudges move whether or not anyone plays them. | throughline 6; overview §5.2 "treaty/war → mustering → march: open" | ABSENT. 0 fields at seeds 0-2 in the control run (T04 §0 Status). | — |

**Completeness yardstick.** After this proposal and the remediation it depends on, G1-G10 must each be AFFORDED at least at
TESTS-ONLY, and G4, G6, G8 and G10 must be observable in a natural run (a non-zero `field.won + field.lost` at `aperture 1 s`, s = 0-2,
REM-27's own reading, M-11). G3's played form (a person commanding inside the battle) is not in the yardstick: J-C-31 is open and IN-46
designs a paused personal fight only (§6).

**What this proposal stands on and does not repeat.** REM-27 (RB-2b: `march` gains `referent_class: Rung`, so the chooser is offered
settlements its ledger names; `remediation-02:450-472`). REM-32 (B-T tail: one weight→troop fixture at `_weighted_unit`, shipped
hash-equal; `remediation-02:591-601`) and JQ-4 (its value). REM-31 (IN-46, the deferral at ENCOUNTER that also gives `fight`
`march`'s Declared pair; `remediation-02:570-589`). The troop-stock design (`proposals/2026-10-16-troop-stock-design*.md`, cited `TS1`,
`TS2`): the recruit pool, `levy`, the stock eating at the larder, the per-side order of battle, held on its own J-1. The lexicon
(`L10`): the verb names `levy`, `disband`, `marshal`, `march` postures `storm`/`besiege`, `surrender`, under verbs-03's rulings R-01
(coin is a terms parameter of `levy`; `recruit` is FA's), R-03 (`raze` is GV's), R-08 (`forage` MB's; `encamp` WT's, parked), R-19
(`surrender` MB's).

**The architectural stance.** Layer 1 says a side is its persons at weight (`MB.py:316-333`, quoting §C.5.1: "units = PersonId[] at
weight — one type"). Every item below except CP-T04-10 is built on that sentence as ratified. CP-T04-10 is the one that changes what a
side fields, and it rides TS's J-1 (§6 Ask A); CP-T04-04 amends Layer 1's ENCOUNTER line and rides Ask C. The items read a side only through the typed record that
already crosses the seam (`queries/inputs.py:118-148`, `MassBattleInput`), widened by named fields, so J-1's answer changes how that
record is filled and not the items' interfaces.

## §1 Gap ledger

Rows are `D_T04 #n`. Every LACKS row (23) and every DIFFERS row whose judgment names a risk to play (7) is addressed: **30 rows**. The
other seven DIFFERS rows (#6, #14, #30, #33, #44, #46, #57) record a difference of calibration, of a ruled single resolver, or of a
precedent with a player that Valoria does not have; their judgments name no risk and they are not gaps.

| gap | rows | ends in |
|---|---|---|
| **A. No force is raised, paid, fed or let go** | #2, #36, #48 (LACKS) | **Jordan ask A** (TS's J-1, carried), and **CP-T04-10** once it is answered |
| **B. The army is an unchosen headcount with one fixed shape** | #1, #27 (LACKS) | **CP-T04-01** (a side is its persons, one subunit each) + **CP-T04-02** (`marshal`) |
| **C. A field is too small to be fought** | #51 (LACKS), #61 (LACKS: the rout has a cause no person owns) | **REM-32 + JQ-4** for the scale; **CP-T04-01** for the authorship (a rout is a named commander's subunit breaking) |
| **D. No decision at contact** | #3, #55 (LACKS) | **CP-T04-03** (retreat in good order) + **CP-T04-07** (surrender, against a siege) now; **CP-T04-04** (a round between declaration and a storm) once **Jordan ask C** allows it |
| **E. No odds read before committing** | #13, #41, #59 (LACKS: odds half) | **CP-T04-08** (`field_estimate`) |
| **F. Neither side can cut its losses** | #34 (LACKS) | **CP-T04-03** (attacker and defender), **CP-T04-07** (defender) |
| **G. Walls are a binary row that never wears; no siege** | #10 (LACKS), #9 (LACKS: posture half) | **CP-T04-05** (graded walls) + **CP-T04-06** (`besiege`) + **CP-T04-07** |
| **H. No campaign supply or attrition** | #9 (attrition half), #53, #59 (logistics half) (LACKS) | **declined.** Five steps: not superseded; not irrelevant; no document rules a supply line; precedent (L10 M-1) needs a force that holds its own stores away from walls, which amends ratified Layer 1 and rides J-1 (L10 §3.9 item 3), so step 5 cannot take it here. Under persons-at-weight the only attrition is RB-5's hunger at home (REM-50, JQ-6); a besieger pays in budget instead (CP-T04-06). Re-enters with Ask A's option (A+M-1) |
| **I. Routed units never return; no rally** | #17 (LACKS), #23 (DIFFERS, risk: the first rout is final) | **declined.** Five steps: not superseded (`orch:288-290` still empty); not irrelevant; no document rules the form; precedent (L10 Suite 2, M-4: a Command pool against Ob 2) exists, but step 5: every season commander's Command is the constant 4 (`MB.py:182-186`) until JQ-2 rules where a person's Command comes from, so a filled `rally_check` hands no chooser a decision and changes every field identically. Note that `MB_YIELD_RALLY` already ships on (`cfg:270`), so an engaged subunit's yield-rally exists. Re-enters at JQ-2 |
| **J. A general cannot fall in battle** | #18 (LACKS) | **declined.** Five steps: superseded by two open asks: death (J-C-19, K-MB-9) and the mass→personal yield (K-MB-10, parked in L10 §3.6 MB-G09). Not raised again here |
| **K. A won field leaves no captive, loot or lasting mark; the winner pays and gains nothing** | #7, #20, #49, #62 (LACKS); #8, #38 (DIFFERS, risk: a loss is only a body scaling) | **Jordan ask B** (what a fought field may write beyond ED-IN-0279's three; carries TS's J-5 and J-C-4). Title after a win is already `seize` (TESTS-ONLY, `test_march.py:793-823`) and `surrender` (CP-T04-07); `raze` is GV's (R-03). `sack` is declined: it waits on M-1 and its tone is held (L10 §3.9 item 4). Death stays J-C-19 |
| **L. No field result moves an ending** | #25 (LACKS) | **declined.** Step 3/4: the ending read is T09's (`world_q.endings_reached` reads holds and seats, `world_q.py:1764`); a field moves a hold through `seize` or `surrender` (CP-T04-07), which that read already counts. Nothing MB-local to build |
| **M. The field does not say why, or who holds the place** | #62 (LACKS: "surfacing that names causes") | **CP-T04-01** (the field's events name the first commander whose subunit broke). The `held_by` half is **CP-T04-09, cut** in §3 |
| **N. One resolver only because nobody plays** | #4, #19 (DIFFERS, risk) | **declined.** Step 4: the single-resolver shape is ruled (auto/manual duality, 2026-07-08, D_T04 #4) and matches the verified precedents (Dominions, FoG2). J-C-31 (may a player command a field) is open and not raised: step 5, the pre-battle order (CP-T04-02) is Dominions' answer, and it is the same for a player and an NPC |
| **O. Friction can swing a whole battle** | #12 (DIFFERS, risk) | **declined as a change; made visible.** Step 4 is silent (precedent cannot set a calibration, D_T04 #30); step 5 cannot choose σ. CP-T04-08 shows the spread an order buys, and CP-T04-02's falsifier says outright if friction drowns the order |
| **P. The defender takes every tie** | #24 (DIFFERS, risk: 44 % between equal armies) | **declined.** Step 4: a draw that does not take the place leaves it with its holder, the UG and siege convention; the draw is graded `Lost` and writes on the attacker only, which is ED-IN-0279's losing side. MB-G38 stays the module's grading rule. CP-T04-03 lowers the cost of a lost draw to the attacker who orders a retreat |

**Count:** 30 rows addressed: **12 closed by items** (#1, #3, #10, #13, #27, #34, #41, #55, #61, plus #9 (posture half), #59 (odds half)
and #62 (cause half)); **1 closed by remediation** (#51, REM-32 + JQ-4, with CP-T04-01 stating the floor JQ-4's value must clear); **11 declined** with a five-step answer (#9 attrition
half, #53, #59 logistics half, #17, #23, #18, #25, #4, #19, #12, #24); **9 to two Jordan asks** (A: #2, #36, #48; B: #7, #20, #49, #62's
stake half, #8, #38). Rows split across two outcomes are counted under each. **Re-tallied after the fix pass:** #3 and #55 stay
closed, but only in part until Ask C: today by CP-T04-03 and CP-T04-07 against a siege; the storm warning (CP-T04-04) is held on the
third ask, which closes no row of its own. #13, #41 and #59 (odds half) are closed for a player's seat only (CP-T04-08, mode (a)).

## §2 Items

Common to every item, so not repeated per block. **Layer:** every item binds Layer 2 (the game code: `engine/season/` and
`modules/mass_battle/`); none edits `architecture/` except CP-T04-10, through Ask A, and CP-T04-04, through Ask C (the ENCOUNTER line it
amends is quoted in its block). **Shipping:** every behaviour ships behind one fixture in `engine/season/data/fixtures.py` whose shipped arm reproduces today's
hash, each with a `hole_register.yaml` row (REM-32's precedent; 04 PART D row 38); the flip ON is its own declared-mover commit (IN-52's
precedent). **Control:** the shipped arm is the control (hash-equal by construction); battle-shape claims use paired seeds
(`random.Random(0..199)` in both arms, T04 §3's method, ±7 points at a 45 % share). **Seam:** everything crosses at the existing
`mass_battle.resolve_field` composition row and `SW`; no `engine/` import of `modules/` is added, so
`test_importing_every_engine_module_pulls_in_no_subsystem` stays the execution artifact. **Revert:** the fixture's shipped arm, then the commits.

### CP-T04-01 · A side is its persons: one subunit per commanding person, casualties by that subunit

- **Adds.** `resolve_field` builds each side as one `Unit` with **one `Subunit` per person on the side**, sized `Person.weight × k`
  (REM-32's fixture `k`), that person its officer. The record that comes back carries, per person id, his subunit's survivor ratio and
  whether it routed. `_eff_march` scales each loser's `body` by **his own subunit's** ratio, not the side's (`EC:260` reads
  one `pct`). The field's band Event names, in its payload, the person whose subunit broke first (the cause D_T04 #61-#62 ask for).
  Fixture `field_subunits: side | person` (shipped `side`).
- **Owner artifacts.** `MM/massbattle.py::_weighted_unit` (becomes per person) and `_run_and_grade`'s return; `SW` passes the person ids
  beside `weights` (`MassBattleInput.weights` is already one weight per member in side order, `inputs.py:123-125`); `EC::_eff_march`.
- **Primitives.** P34 (cohesion and break per subunit), P35 (the unwatched run), P32's precursor (a per-person mark).
- **Reads / writes.** Reads `Person.weight` (as today). Writes `Person.body`, `Person.stance` on losers (as today; magnitudes now per
  person). No new write pair. **Asymmetry (§0.1 pt 1):** the getter that changes is `_eff_march`'s `pct`; the writers of
  `Person.body` are `_eff_march`, `fight`'s effect, MATTER's subsistence and `tend` (`VT:1248` note); only `_eff_march` changes, so no
  writer becomes a no-op.
- **Joins.** JQ-4 (the value): with one subunit per person, `k` must keep a weight-1 subunit at or above `SUBUNIT_ROUT_FLOOR = 80`
  (`cfg:117`) and each side at or above the 100-troop size line (T04 §2.1 step 6), or every subunit routs on tick 1 again. TS (Ask A):
  under option A the subunit is (officer, stocks led), TS2 §4.2 step 5 (`men_led`), so "every subunit has a commanding person" is the
  shape both answers to J-1 fill.
- **Decision handed over.** None by itself; it is what makes CP-T04-02's choices land on named persons. Unwatched: each loser's body
  now depends on where he stood, so a field leaves its persons unequal.
- **Falsifier.** A hand fold of `set_s_036` at a `k` above the floor (REM-32's own falsifier fold): two attackers on a losing side, one
  whose subunit routed and one whose did not, end with different bodies under `person`, and identical bodies under `side`. If they are
  equal under `person`, the per-person ratio is not reaching the write. Mutation: feed the side's ratio to every person; the test reds.
- **Control.** `field_subunits: side` reproduces today's bodies exactly. **Hash.** Equal shipped; mover on flip in any fought field.
  [UNVERIFIED] that `run_battle` fights a multi-subunit `Unit` cleanly on the season's terrain rows (TS2 §4.4 item 5 left it open); the
  falsifier's first run shows it. **Size** M.

### CP-T04-02 · `marshal`: the standing order of battle, read when the force fights, attacking or defending

- **Adds.** A verb row `marshal` (L10 Suite 2; verbs-03:73), `remit:dispatch` (march's eligibility, `VT:838` row), subject the
  settlement where the seat's people stand. Its write is `Record.exists` through the one document mint (`loop/effects_information.py:172`, `_mint_document`,
  the body `create_record` uses) with a new `record_kinds` member `order_of_battle: [at, role, retreat_at, reserve, general]`.
  `works`' precedent: a Record kind minted by an act and read later by another (`RY:200-206`). `field_input` (`SW`) reads, for each
  side, the live `order_of_battle` held by a seat of that side's faction about the side's settlement (origin for the attacker, target
  for the defender) and passes it as a new `MassBattleInput.orders` field. `resolve_field` maps `role` onto the module's own role
  table (each subunit's shape, stance and instructions, `cfg:582-616`), `reserve` onto which persons' subunits are held back and
  released at `own_strength`/`tick` triggers (`units:395-403`), replacing `RESERVE_COMMIT_TURN` (`cfg:258`) for that field,
  `retreat_at` onto CP-T04-03, and `general` onto who commands the Unit. No order: the module's defaults stand, so the shipped
  behaviour is unchanged.
- **Owner artifacts.** `VT` (`marshal` row); `RY: record_kinds` (one member); `SW::field_input`; `queries/inputs.py::MassBattleInput`
  (one field); `MM/massbattle.py::resolve_field`. **The role roster's owner is the module** (`cfg: ROLE_SPEC`); the season reads the
  role names from a typed export under `engine/engine_params/` behind an exporter with a blocking `--check` (`CLAUDE.md` §0.05), never
  from a second list in `rosters.yaml`.
- **Primitives.** P36 (pre-battle intent), P17 (an order set once, executed unattended), P08 (one role per subunit).
- **Reads / writes.** Writes `Record.exists`, `Record.stages` at RESOLVE (the `create_record` pair, already in the matrix). Reads the
  Record at ENCOUNTER (a read). The Record is a `hold` (`_eff_create_record` mints one), so each order adds one to its holder's budget
  (`decision/budget.py:57-58`); this is H-92's known drift, named, not new.
- **Joins.** Decision layer (`decision/options.py::operand_bags`): a computed `marshal` must range `role` and `retreat_at` over their
  closed sets, as it ranges `confer`'s `to` (`VT:271` note), or no NPC ever marshals. FI: an order is a document; its holder learns it
  as content (`RY:236-250`), and a spy who comes to hold it learns it too, which is the information game's hook into the field.
- **Decision handed over.** Shape, stance, who leads, who is held back, when to pull back: written before contact, for attack and for
  defence. Unwatched: the defender, which today has no chooser at all (T04 trap 8), now has one act that changes the field it will fight.
- **Falsifier.** Paired seeds, the same two sides, two orders (a `Shock` role against a `ShieldWall` role on the attacker): band
  distributions differ beyond ±7 points. If they do not, the order is cosmetic under the shipped friction (`MB_FRICTION_SIGMA = 1.1`,
  `cfg:335`), and the item fails its N-line (§3). Second: a defender order changes a defended field, not only an attack.
- **Control.** No `order_of_battle` held → today's field, hash-equal. **Hash.** Equal until a `marshal` executes. **Size** M.

### CP-T04-03 · Retreat in good order: a fired retreat concedes the field and ends that side's fight

- **Adds.** `retreat_at` (a fraction, closed set `{none, 0.5, 0.25}` in the order's key) becomes, per subunit, an `own_strength:FRAC`
  Order whose action is the `retreat` stance (`units:402-403` names "withdraw a spent body" as the trigger's use). In `_run_and_grade`,
  a side every one of whose subunits has retreated or routed **concedes**: it cannot be graded the winner, and the battle stops for it
  as a rout stops it, without rout's facing flip. Casualties are then the engine's actual losses (CP-T04-01), so an orderly retreat
  costs fewer bodies than a rout. No new band: `Won`/`Lost` stay the two fought bands (`RY:875`).
- **Owner.** `MM/massbattle.py::_run_and_grade`; `MM/orchestration.py::run_battle`'s stop test (`if unit_a.routed or unit_b.routed:
  break`, per `proposals/mass_battle_fighting_withdrawal_v1.md:24-30`). The fighting-withdrawal yield (built, `MB_YIELD_*`) is the
  in-battle half and is not touched.
- **Primitives.** P34 (an army break it chooses rather than suffers), P23 (the threshold as a known trigger).
- **Reads / writes.** Module-internal; the season writes nothing new.
- **Joins.** M-5 (L10 §3.7): this is M-5's season half done without a band. Pursuit of a retreating side (`pursuit_damage`, `orch:2549`)
  runs only in `run_multi_turn_battle`, which the season does not call; so a retreat is safe from pursuit until a later item, and that
  is named.
- **Decision.** How much of the force to risk before giving up the field. Unwatched: NPC orders vary `retreat_at` by the draw; armies
  that retreat survive to march again, so the realm's grudges and bodies diverge by order.
- **Falsifier.** Paired seeds: an attacker with `retreat_at 0.5` against an equal defender loses fewer troops than with `none`, and is
  graded the winner in **zero** seeds where its retreat fired. A win with a fired retreat is a grading defect. **Control.** `none`
  everywhere reproduces today. **Hash.** Equal shipped. **Size** S.

### CP-T04-04 · The field is fought a round after it is declared: the warning and the defender's turn

- **Adds.** The `a field` prize row (`RY:1281`) gains one column, `fought_after: 1` (rounds), read by ENCOUNTER: the selection
  becomes "every declared, unfought act of this prize whose declaration is at least `fought_after` rounds old", read from the Event
  log and `w.acts` (both persistent `World` state, `state/world.py:207, 236`), instead of "this round's declarations" (`encounter.py:51-58`).
  Nothing new is stored: the declaration Event is the carrier, as it is today. A round-5 declaration is fought at the next season's
  round-1 ENCOUNTER (MATTER runs between: legs end, larders draw), so no round is safe from warning. `_survives` still refuses an act
  whose actor died meanwhile (`resolve.py:61`). Fixture `field_fought_after` (shipped `0`, today's same-round field).
- **Owner.** `engine/season/loop/encounter.py`; `RY: contest_subsystems.prizes` (the column, by prize, so `fight`'s deferral under
  REM-31 is untouched unless its own row sets it: no verb special case).
- **Primitives.** P23's information half (the defender sees the threat), P07 inverted (a commitment the attacker cannot take back
  once declared, except by CP-T04-03).
- **Reads / writes.** Reads the log. Writes nothing new; the field's own writes move one round later.
- **Joins.** **FI / WITNESS:** the defender must perceive `march.declared`. The act's place is the marcher's rung, so a presence
  channel delivers it at the origin, not the target; the interface needed is that a declaration whose subject is a Rung is also
  deposited for persons present in that Rung's subtree [UNVERIFIED which channel does this today]. **Decision layer:** REM-27's
  `fields_named` already offers a Rung the ledger names to `march`, so a defender told of the threat can march his own people to his
  own town (an `Unopposed` relocation, `loop/sides.py:121-132`): that is reinforcement, and it arrives a round after the attack it
  answers (relief comes late; named). **PC / REM-31:** both edit `loop/encounter.py`; this lands after REM-31 merges and re-runs its
  hash control, but it is **not bundled** with REM-31, which amends no Layer 1 text (`remediation-02:570-589`).
  **Layer 1 — this item amends it, so it waits on Ask C.** Ratified Layer 1 says `loop/encounter` reads "RESOLVE's own `Event[]`
  (selects `degree == Declared`)" (`architecture/meta/04_CODE_ARCHITECTURE.md:177`) and that the step "folds RESOLVE's own deferrals"
  (`:541-545`). Reading the log and `w.acts` across rounds is outside both lines.
- **Decision handed over.** The defender, between declaration and field: marshal a defence (CP-T04-02), surrender (CP-T04-07), leave
  (`move`), or call in relief. The attacker: the cost of warning the enemy. Unwatched: every NPC defender's chooser now gets a question
  about a real threat.
- **Falsifier.** A march declared in round r against a holder who surrenders in round r+1 fights no field (the place passes, no body
  or stance row is written); with `field_fought_after: 0` the same script fights the field before the surrender can fold. Plus the
  order-independence permutation REM-31 runs (`remediation-02:579-584`), with the delay on. **Control.** `0` is today, hash-equal.
  **Hash.** Mover on flip: every fought field moves a round. **Size** M.

### CP-T04-05 · Graded walls: the walls' armour follows the garrison's condition

- **Adds.** The WALLS row's defender DR becomes `round(WALLS_DEFENDER_DR × fort_level)` instead of a flat `+3` at any `fort_level > 0`
  (`MB.py:272-273`; `terrain.py:174-178`). `fort_level` is already on the record (`MassBattleInput.fort_level`, `fortification_of`,
  `world_q.py:1497`). A garrison at full condition is today's walls; a worn one is weaker; at 0 it is no wall (as today). This is H-150's
  "walls graded by condition" (T04 §7). Fixture `field_walls_graded: false | true`.
- **Owner.** `MM/massbattle.py::_run_and_grade`. **Primitives.** P01 (a condition meter read in bands), P40's counterpart (`restore`
  repairs it).
- **Reads / writes.** Reads `fort_level`. Writes nothing.
- **Joins.** GV/EC: `restore` raises a garrison Site's condition and `sabotage` lowers it (`VT:1045, 1082`), so both gain a field
  consequence. Garrison wear is 0 by design (`RY:1454-1473`), so only acts move it: CP-T04-06 is the army-scale one.
- **Decision.** Repair the walls or not; sap them or not. Unwatched: towns whose walls an NPC let lapse become the ones that fall.
- **Falsifier.** Paired seeds at fixed sides: defender win share falls monotonically as `fort_level` steps 1.0 → 0.67 → 0.33 → 0.
  Flat → the grading does not reach the engine. **Control.** `false` is today's flat row. **Hash.** Equal at every settlement whose
  `fort_level` is exactly 1.0; [UNVERIFIED] that all 37 are (T04 §1 measured "> 0", and 1.0 at `set_s_036` only), so the flip is a
  declared mover until read. **Size** S.

### CP-T04-06 · `besiege`: a march that sits before the walls instead of storming them

- **Adds.** `march` gains a posture operand (L10 Suite 3 fold; T04 §7), roster `march_postures: [storm, besiege]` in `RY`, default
  `storm` (today). An act-declared payload key on `confer`'s `term` precedent (`VT:275`, `_declared_term`). Under `besiege` the act
  declares as today; at its ENCOUNTER no battle is run. A target with no opposing side (held by the marcher's faction, by nobody,
  or with none of its holder's people present) resolves `Unopposed` and arrives exactly as a storm would (`loop/sides.py:131-132`;
  `SW:238-249`): an empty place needs no siege. If the side is opposed, each garrison Site in the target's subtree loses `siege_wear`
  condition (a fixture, a `hole_register.yaml` NUMBER row for Jordan's value) scaled by `min(1, attackers' Σ weight / defenders' Σ
  weight)`, the two sums the provider already holds, so a lone marcher cannot wear walls as fast as a host; the band is a new
  `field_degree_bands` member `Invested`, emitting `siege.pressed`. Nobody relocates, nobody is hurt, and **no `travel_leg` is
  written**: a leg is what a journey writes, through `_relocate`'s one body (`loop/effects_migration.py:91-99` names a second copy as
  the drift hazard), and a besieger makes no journey. The besieger's price is the act itself, one scene action per besieging act
  (`decision/budget.py`, P05), repeated for as long as the siege is kept. A siege is sustained by declaring it again: one act per round or season, never a standing
  state (T-i, `architecture/meta/01_AXIOMS.md:482`; the "fresh act each season" shape D_T06 #45 records). A storm is a later `march`
  with `storm`, now against graded walls (CP-T04-05).
- **Owner.** `VT` (`march`: the posture's operand note, `Invested` band, `siege.pressed`); `RY` (`march_postures`,
  `field_degree_bands`); `SW` (the provider's besiege branch, no engine call); `EC::_eff_march` (the wear); `write_matrix.yaml`
  `(Site, condition)` gains `ENC`, on `(Person, body)`'s precedent (TS2 §4.6).
- **Primitives.** P04 (progress by repeated acts), P06 (the act's own price, one scene action), P02 (the walls cross 0 and the town
  falls to any force, TS2 §4.1's inverted row under A).
- **Reads / writes.** Writes `Site.condition` (ENC, new cell). Reads `fortification_of`.
  **Asymmetry:** `Site.condition`'s writers are MATTER's wear, `restore`, `sabotage` and now this; the getter `fortification_of` is
  unchanged, so no writer goes silent.
- **Joins.** Decision layer: `operand_bags` must range the posture for a computed `march`, or NPCs never besiege (a computed `confer`
  declares no `term`, `VT:275`). EC (optional, not built here): a `transfer` into a place with a `siege.pressed` this season refused,
  which would add starvation; named as an interface, not assumed.
- **Decision.** Blood now (storm) or time and scene actions (besiege), the besieger's defining choice (L10 Suite 3 R). The defender's
  counter: `restore`, relief, or `surrender`. Unwatched: a long NPC siege wears a town down whether or not anyone watches.
- **Falsifier.** After k besieging acts a target's garrison condition reads start − k × `siege_wear` × the side ratio (floored at 0), and a besieger at half the defenders' weight wears half as fast, and a storm
  afterwards wins more often over paired seeds than a storm at full walls (with CP-T04-05 on). Mutation: ignore the posture → the
  condition never moves and the test reds. **Control.** No act declares `besiege` → hash-equal. **Size** M.

### CP-T04-07 · `surrender`: the holder yields a threatened place on terms, and no field is fought

- **Adds.** A verb row `surrender` (L10 Suite 4; R-19), `remit:dispatch`, actor a member of `holder_faction_of(subject)` present in
  the subject's subtree, subject a settlement against which a declared, unfought `march` (CP-T04-04) or a `siege.pressed` this season
  (CP-T04-06) names it. **Who receives the place:** the actor of that threatening act (named on its `march.declared` or
  `siege.pressed` Event), the person whose own hold `seize` would have opened had he taken the place (`seize` opens under T-m, the
  actor's own hold, `VT:1141-1143`). Effect: a `hold` on the settlement Rung opens to him, and the yielding seat's live hold on that
  Rung, if any, closes (seeded settlements are not held directly, T04 trap 9, so usually nothing closes and the territory's holder
  keeps the territory), in one effect, `seize`'s pair shape. `holder_faction_of(subject)` is then the receiver's faction, so the pending
  march resolves `Unopposed` by `sides_of`'s own rule (`loop/sides.py:131-132`) and relocates the marchers. No body or stance row is
  written on either side. Emits `place.surrendered`, a cession under arms, distinct from `rung.seized` (L10 Suite 4).
  **The gate basis is new and named:** no basis at HEAD lets one person open a `hold` owned by another of an enemy faction (`seize`'s
  close runs under `seizure` on occupation, its open under T-m, `VT:1141-1143`). The row needs one `state/gate.py` basis, `cession`:
  the closer holds a seat of `holder_faction_of(subject)` and the opened hold's owner is the actor of a live threatening act naming the
  subject. [ASSUMPTION; medium] that a gate basis is Layer 2 (`state/gate.py`) and not one of Layer 1's enumerated authorship rules;
  if it is enumerated there, this row joins Ask C as a second amendment rather than proceeding alone.
- **Owner.** `VT` (row); its effect beside `_seize_rung` in `loop/effects_information.py` (the pair shape reused, not copied); the
  `cession` basis in `state/gate.py`; the event kind.
- **Primitives.** P14 (a cession under threat as an obligation honoured), P12's lower rung (yield before war's cost).
- **Reads / writes.** Writes `Tenure.until`/`Tenure.since` at RESOLVE (the `seize` pair's cells, already in the matrix; the new part is
  the gate basis). Reads the log for the pending threat.
- **Joins.** GV (the title primitive). SC/FA: the terms are not bargained here (parley is SC's `negotiation`, L10 MB-G33); whether the
  garrison's persons are spared custody is Ask B's (captives). T09: a surrendered place moves a hold, which `endings_reached` reads.
- **Decision.** The defender: lose the place now, or risk bodies and grudges on a field. Unwatched: a weak holder facing a large
  declared march yields, so towns change hands without a battle.
- **Falsifier.** A surrendered and a stormed town (the same pair, paired seeds) both end with the hold moved, but only the stormed one
  writes body and stance rows; identical end states → the row is redundant with `march`. **Control.** No `surrender` formed → hash-equal.
  **Size** M.

### CP-T04-08 · `field_estimate`: the field prize's input to the one odds reader, for the player's Act interface

- **Adds.** No second odds function. T01 owns the odds reader (`band_odds` / `estimated_odds`, `seam/wrappers/sigma.py`; cross-file
  ruling R1); this item is the field prize's **caller**: `field_estimate(w, actor, via, target, order=None) -> (won_share, samples)` in
  `SW`, beside `field_input`, which builds the `MassBattleInput` the provider would build for that act and samples `resolve_field`
  `field_estimate_samples` times on an rng keyed `(world_seed, tick, actor, "estimate")` (the season's keying, overview §2.2), because a
  field does not resolve on a pool/Ob ladder that a closed form could enumerate. It is handed to T01's reader as this prize's case.
  **Mode (a) only:** the player's Act-interface display, computed at the seam or the play surface (`harness/play_surface.py:41`), never
  in DELIBERATE, since `decision/` holds no World (`architecture/meta/04_CODE_ARCHITECTURE.md:142`). It reads world truth, including the
  defender's real muster: AX-7 binds what the character's acts would meet, so the display shows the odds of the act as it would resolve
  (R1 (a)). **Mode (b), an NPC's believed odds, is not built here:** the chooser score term is cut (R1; the question is AQ-X1, carried by
  T01 §6 and cited here, not re-asked), so no NPC reads this.
- **Owner.** `SW` (`field_estimate`); `data/fixtures.py` (`field_estimate_samples`); T01's reader for the display contract.
  **Primitives.** P23 with odds shown (throughline 2: an estimate that says it is one, Shadow Empire's answer, D_T04 #59).
- **Reads / writes.** Reads what `field_input` reads. Writes nothing; `resolve_field` never reads or writes `World` (`MB.py:306-320`).
- **Joins.** T01 (the reader and its two modes). The play surface (where mode (a) is called). AQ-X1 (whether any NPC ever reads odds).
- **Decision.** The player's: whether to march, and with which order, knowing roughly what it buys. Unwatched: nothing.
- **Falsifier.** Over held-out seeds, the realised `Won` share of a field lies within the estimate's sampling interval at
  `field_estimate_samples = 50` in at least 19 of 20 pairs tested; and a season run through `dispatching_chooser` whose callback calls
  `field_estimate` before every act it hands in ends at the same `content_hash` as the same run without the call (no season draw
  consumed). **Control.** The callback without the call. **Hash.** Equal by construction. **Size** S.

### CP-T04-09 · The field tells witnesses who holds the place — CUT (§3)

- **Was.** The field's events carry `holder_faction_of(target)`, so WITNESS deposits a `held_by` claim, and H-195's holder operand
  (`hole_register.yaml:4364-4375`) regards a Rung's holder. **Cut** in §3: its N-line holds only under `stance_polarity: declared`,
  which rides ED-IN-0296 (1) (`remediation-01:234`). Re-entry trigger: that ruling, plus H-195's own M0g trigger (≥ 5 % of persons
  holding a `held_by` claim).

### CP-T04-10 · Raise and keep a force: the recruit pool, `levy`, the stock at the larder, and `disband` (rides Ask A)

- **Adds, if Ask A answers A.** TS's positions as written, adopted as v9 positions: TS-3 (the pool, `recruits` in `Rung.stores`,
  regrowth at MATTER toward a ceiling from resident cohort weight, R-POOL), TS-L (re-keying the old `levy` citations), TS-4 (`levy`,
  `remit:dispatch`, with coin as a terms parameter, R-01), TS-11 (a stock eats where it stands, after the people), TS-5/TS-6/TS-8 (the
  order of battle at the seam and write-back on stocks and garrison), TS-7 (the computed levy). **One addition TS lacks:** `disband`
  (L10 Suite 1), `troops_<g>` → `recruits` on the same rung, capped at the pool's ceiling, grade lost, `army.disbanded`; without it a
  raised stock's only end is hunger or a field (TS1 §2.9; TS2 §9 lists "no stand-down verb" as a consequence of A). **What it
  supersedes:** IN-52's feed (TS1 §0 item 10 withdraws LF-1..LF-3), so v9's IN-52 is retired in the same commit that adopts TS-11.
- **Owner.** As TS2 §7 names them (`RY: matter_kinds`, `pool_rung_kinds`; `queries/world_q.py::fielded`, `settlement_above`;
  `loop/matter.py`; `VT` rows `levy`, `disband`; `SW::order_of_battle`). CP-T04-02's `marshal` Record replaces TS2 §4.3's `order`
  payload on `march` (L10's one-owner condition), and CP-T04-01's subunit-per-officer is TS2 §4.2 step 5.
- **Primitives.** P18 (a force capped by the pool), P20 (it eats each season), P02 (unfed, men leave), P16 (who is raised from where).
- **Layer.** Amends `04:793` and `04:802` (and their copies, TS1 §2.4): **Layer 1, by Ask A only.**
- **Decision.** Levy now (the pool's seasons of regrowth, and food) or keep the pool; keep a stock (food) or disband it (lose its
  grade). A consent cost (L10's cohort stance row, M-8) is TS's "weighed, not adopted" (TS1 §2.10) and is not added here. Unwatched: an
  over-levying NPC seat empties its larders (R-POOL's draw order feeds the people first, TS1 §2.5).
- **Falsifier.** TS's per position (TS2 §7), plus: a disbanded stock is re-levyable next season and draws nothing from the larder the
  season it is disbanded. **Control.** TS's arms. **Size** L.

## §3 NERS

Method: `skills/ners/SKILL.md` instrument A (no new draw is designed, so instrument B is not run; CP-T04-08 reuses the engine's draw).
Each item is cut in turn; the loss is walked step by step; the false N-line disqualifiers (§3 of the skill) are tried on each.

| item | N-line (cut it and the game can no longer…) | attack tried | verdict |
|---|---|---|---|
| 01 per-person subunits | …let a field fall unequally on the persons who fought it, or let an order place one person in the reserve and another in the line; the rout has no named owner (D_T04 #61) | disqualifier 1, "the carrier exists": TS's order of battle has subunits with officers. Walk: TS needs J-1; until then nothing carries a per-person subunit, and under A TS2 §4.2 step 5 *is* this shape | **N holds**, all directions but diagonal (no cross-subsystem read yet). Residual: its magnitude is JQ-4's |
| 02 `marshal` | …let the defender choose anything, or let any built formation, role or reserve reach a season field (M-MB-5: "the only decision in mass battle is whether and where to march") | disqualifier 1: `march`'s payload could carry it (TS2 §4.3). Walk: the defender does not march, so a payload leaves it no act (L10 Suite 2); no shipped act writes an order (`dispatch` writes nothing) | **N holds** top-down, bottom-up, lateral. ⚠ Its own falsifier can still kill it: if friction (σ 1.1) drowns a role's effect, the N-line is false in play, and the item is cut at build |
| 03 retreat in good order | …let a side give up a field and keep most of its people | disqualifier 1: `own_strength` Orders and the `retreat` stance exist (`units:395-403`; `cfg:290`). Walk: no season act sets them (02 does), and no grading treats a retreat as conceding, so a retreating side could be graded the winner. The step with nothing to carry it is the concession rule | **N holds, narrowed:** the item is the concession rule only; the threshold is 02's content |
| 04 a round's warning | …let a defender answer a threat before it lands, by surrender, flight, a defensive order or relief | disqualifier 1: CP-T04-06's siege already gives a window across rounds. Walk: a `storm` has no window, so the defender's chooser still has nothing to answer before a storm; and without 04 a player storms in the round that gives no warning | **N holds** laterally (attacker ↔ defender) and top-down; it is the most expensive item (a loop step's selection and a Layer 1 amendment, Ask C), so it is ordered last and waits on the ask |
| 05 graded walls | …make wear, sapping or repair change a battle before a garrison reaches 0 | disqualifier 5, "flat bonus": the residue is a DR that scales, not "+X", and it makes `restore`/`sabotage` (already shipped) bite | **N holds, narrowed** to "walls are a resource, not a switch"; one line of code |
| 06 `besiege` | …trade time and scene actions for blood against walls; a siege cannot exist | disqualifier 1: `sabotage` already lowers `Site.condition`. Walk: `sabotage` needs its actor standing at the Site (`VT:1030-1035` at `51d7b05`), inside the walls; nothing lets an army outside wear them, and nothing charges it for sitting | **N holds, narrowed** to the army-scale, from-outside writer; the starvation half is not built (an interface) |
| 07 `surrender` | …end a threat without a field; a town changes hands only by blood | disqualifier 1: `give` moves a hold by consent. Walk: `give` writes no pending-march resolution and names no threat, and its event (`record.given`) would read as consent | **N holds** laterally and diagonally (MB → GV title) |
| 08 `field_estimate` | …let a player choose whether to march knowing roughly what it buys | disqualifier 2, "no producer": it has one (the engine). Walk on R-WORLD: no NPC reads it (the score term is cut, R1; AQ-X1 is T01's). Disqualifier 1: T01's reader exists, but a field has no pool/Ob it can enumerate, so the field's case still needs a sampler; it is that caller, not a second function | **N holds, narrowed:** one direction (top-down, for an occupied seat). Kept because it is the E-LEGIBILITY repair for an opaque draw and costs no draw |
| 09 `held_by` from the field | …let a grudge from a lost field drive a march on the winner's places | walk: the shipped polarity is `legacy`, under which a Rung subject reads 0 whatever the ledger holds (`decision/choose.py:89-94`; `hole_register.yaml:4366`) | **FALSE N-LINE at the shipped control** (disqualifier 2 in its own terms: the reader it would feed is switched off). **CUT**; trigger ED-IN-0296 (1) |
| 10 force (J-1) | …raise, feed or release a force: an army is whoever lives where its general lives | none survives: nothing in the tree raises men (no `levy` among 56 rows) | **N holds** in all six directions; it waits only on Ask A |

**Cuts proposed and what dies.** 09 is cut (above). Rally (gap I) was cut before drafting: it hands no chooser a decision while every
commander's Command is 4. Cutting 08 would kill only the player's odds read; kept for E-LEGIBILITY. Cutting 05 would leave 06's wear
invisible until the walls hit 0, so 06 would be a countdown to one flip; 05 stays. No other cut is free.

**R.** R-PLAYER (seats a player can occupy: any seat granting `remit:dispatch`): storm against besiege, fight against surrender, a role
and a retreat line, levy against keep (under A). None dominates by construction; whether one dominates in play is the falsifiers'
(02's especially). R-WORLD: NPC seats besiege, surrender and retreat by their choosers; with uncelled alignment the choice among postures
and roles is the draw's (JQ-1's 72 % outvoted share applies), so NPC war is varied but not yet characterful. That residual is the
cell-value pass's, not this proposal's.

**S.** S-UP: a field's per-person bodies feed budgets (P05) and the next field; surrender and storm move holds the ending read sees.
S-DOWN: a seat's order reaches each subunit; walls read the garrison Sites the economy maintains. Lateral: attacker and defender each
have acts (02, 04, 07). Diagonal: GV (`restore`, `seize`), FI (orders as documents; warnings), EC (larders under A). *Pauses correctly:*
04 is the pause, a declared field waits one round for the other side's DELIBERATE; the battle itself stays one atomic call. *Methodology:*
every new magnitude is a fixture read through one owner (`fortification_of`, the provider's two sums, the subunit's own ratio); walls
and wear read the same condition. ⚠ One S defect introduced and named: 04 makes relief arrive a round after the attack it answers.

**E, last, as a ratio.** Added: verb rows `marshal`, `surrender` (+ `levy`, `disband` under Ask A); one Record kind; one posture roster
(two members); one band (`Invested`); one prize-row column; one Query; one exported role list; five fixtures (`field_subunits`,
`field_fought_after`, `field_walls_graded`, `siege_wear`, `field_estimate_samples`). Removed or replaced: the constant reserve turn for
any field with an order; the one-block army; the flat walls row; IN-52's feed under A; the hand-built `Resolution("Won")` dependence
in tests once fields can be won. The vocabulary grows by two verbs and one posture against ten genre opportunities moved from ABSENT
or PARTLY; no item adds a guard, a store outside `World`'s existing carriers, or a second resolver. E-LEGIBILITY: every choice's
consequence has a predictable shape (more walls, slower fall; a retreat line, fewer dead; surrender, no field), and the one opaque
part, the draw, gets an estimate. The ratio is favourable but it is an addition-led design, not a deletion-led one; the meta-rule's
presumption is answered item by item in the N column, not waived.

## §4 One season, after

Built-after-this-proposal, REM-27 and REM-32 landed, J-1 unanswered (persons at weight). Figures the code produces today are marked
(T04); every other figure is `illustrative`, because JQ-4's `k`, `siege_wear` and the estimate's samples have no value yet.

**The person.** `p_npc_033`, Crown, holds `off_npc_033` (grants `remit:dispatch`), home settlement `set_s_014`; with him is `p_npc_035`.
Σ weight 2 (T04). The Church of Solmund holds `set_s_036` with 6 members present (Σ 6), garrison condition 1.0 (T04). A player picks
`p_npc_033`'s acts through the play surface (`harness/play_surface.py:41`); everyone else is on the shipped chooser. Steps 4-5 assume
Ask C allows CP-T04-04.

1. **Round 1, DELIBERATE.** REM-27 puts `set_s_036` in his menu (his ledger names it). The Act interface shows the player
   `field_estimate` for a storm (mode (a), true odds): a low
   `won_share` (illustrative: 2 v 6 at `k = 100` is 200 against 600 troops, behind full walls). He forms `marshal` at `set_s_014`:
   role ShieldWall, `retreat_at 0.5`, `p_npc_033` as general. One scene action; the order is a Record he holds (+1 budget, H-92).
2. **Round 2.** He declares `march {subject: set_s_036, posture: besiege}`. At ENCOUNTER (with CP-T04-04 on, one round later, round 3)
   the provider finds the side opposed and returns `Invested`: each garrison Site in `set_s_036`'s subtree loses
   `siege_wear × min(1, 2/6)` condition (illustrative: 0.1 × 0.33). The siege cost him one scene action; nobody moved.
   `siege.pressed` is witnessed at the target.
3. **The defenders, unwatched.** A Church member present forms `restore` on the garrison Site (EC's verb, shipped), undoing the wear; the
   seat-holder of the territory forms `marshal` at `set_s_036` (role ShieldWall, `retreat_at none`). No one surrenders: the draw
   among their candidates does not pick it this round (no NPC reads odds, R1).
4. **Next season, round 1.** He has learnt the siege does not outpace `restore` at 2 v 6. He storms anyway (`posture: storm`), declared
   round 1, fought round 2. The defenders were warned in WITNESS of round 1; one marches his household in from a neighbouring Church
   town, and arrives in round 3, too late (the S defect in §3).
5. **The field.** One subunit per person: two of 100 troops (illustrative) against six. Walls are graded at condition 1.0 → DR +3 (as
   today). At tick N (illustrative) `p_npc_035`'s subunit routs; `p_npc_033`'s falls to half strength and retreats. The Crown side has
   conceded: `Lost`. Bodies by subunit: `p_npc_033` about 1000 × his survivor ratio (illustrative 0.5 → 500), `p_npc_035` lower; each
   gains `(fac_church_of_solmund, −1, w)` and `(fac_crown, −1, w)` as today (`EC:300-305`). `field.lost` names `p_npc_035` as the first
   to break.
6. **After.** `p_npc_033` keeps 500 body (illustrative), below only the 800 floor of the three (800 / 500 / 100, T04 §1): his budget
   falls by one band, not the three the routed hand fold costs today (body 20, budget 6 → 3, T04 §0a); he can march again next season.
   Had he not ordered a retreat, he would have routed with the rest.

**What the world did unwatched that season** (illustrative, given REM-27's own [CONFIDENCE: low] that fields form at all): other
dispatch-holding seats formed `march` on settlements their ledgers name; those against empty enemy places arrived `Unopposed` and a
`seize` could follow; a small holder facing a declared march yielded by `surrender`, and the place changed hands with no field.

## §5 Order and dependencies

**Inside the proposal.**

| step | items | after | why |
|---|---|---|---|
| 0 | REM-27, REM-32 (+ JQ-4) | — | no field is fought, and none is winnable, before them |
| 1 | CP-T04-01, CP-T04-05 | REM-32 | both edit `MM/massbattle.py` (`_weighted_unit`, `_run_and_grade`); one batch, one hash control |
| 2 | CP-T04-02 → CP-T04-03 | 01 | the order needs subunits to assign; the concession rule reads the order's `retreat_at` |
| 3 | CP-T04-08 | 02 | estimates the same input, order included |
| 4 | CP-T04-06 → CP-T04-07 | 05 | the siege's wear matters only against graded walls; surrender's first threat is a siege |
| 5 | CP-T04-04 | Ask C answered yes; REM-31 merged; 07 | it amends Layer 1's ENCOUNTER line; it edits the file REM-31 edits (serial, not bundled); 07 then widens to declared storms |
| 6 | CP-T04-10 | Ask A; TS-L | the only item that amends Layer 1 |

**What it needs from other subsystems (interface, as expected).**

- **Decision layer / chooser (IN, NP):** `operand_bags` ranges `march`'s posture and `marshal`'s `role` and `retreat_at` over their
  closed sets. No score term is demanded (R1); whether odds ever enter an NPC's score is AQ-X1 (T01 §6).
- **Resolution (T01):** its odds reader accepts a prize-supplied sampler as the field's case (CP-T04-08), mode (a) only.
- **Information / WITNESS (FI):** a declaration whose subject is a Rung is deposited for persons present in that Rung's subtree
  (04), and `siege.pressed` likewise (06).
- **Governance (GV):** `seize`'s Tenure pair callable by `surrender`'s effect without copying (one title primitive); `restore` and
  `sabotage` unchanged.
- **Economy / settlements (EC, SE):** optionally, a `transfer` into a besieged place refused that season (starvation); under Ask A, TS's
  pool data (MB-G54).
- **Faction actions (FA, T09):** a war gate on `march` (K-MB-5) is FA's to raise; nothing here reads `at_war`. **Title after a won
  field** rests on `seize`'s #453 exit (vii) as built: an opposed `Won` removes no defender (`test_march.py:913`), and occupation still
  licenses the seizure because "it asks nothing of the defenders" (`loop/effects_information.py:955-959`). T09's CP-T09-04 (b) (a
  strict plurality over the holder's members) would refuse that seizure wherever the defenders outnumber the winners, and re-records
  `test_march.py:918-930`. **Demand on T09:** CP-T09-04 (b) applies to unfought towns by default, leaving a town just won in a field
  under exit (vii); T09 has said it will. **`sides_of`:** T09's CP-T09-07 (b) owns widening the claimants at `loop/sides.py:115` to the
  seat's obligees; this proposal edits `sides.py` only through CP-T04-10 (TS's `settlement_above` extraction at `:82-84`'s inline walk,
  TS2 §4.1). The two edits are serial in one file; whichever merges second re-runs its hash control. Nothing else here edits `sides.py`.
- **Personal combat (T03):** the one combat-to-custody opener (CP-T03-09) for Ask B (d), with its `state/gate.py` basis. **Arms: this
  proposal reads no arms or kit.** The module's own kit owner is `modules/mass_battle/equipment/__init__.py:21` (`TROOP_LOADOUT`, read by
  `kind_for_kit`), reachable only under Ask A (TS1 §0 item 5). If T03's `arms_kinds` roster lands, the mapping from each arms kind to a
  mass-battle kit kind is one more column on T03's roster, exported by the same `engine/engine_params/` exporter shape CP-T04-02 uses for
  role names; it is not built here, and T03's "shared with MB" is a design intent until Ask A.
- **World / travel (T10), D-4:** accepted as (a). `march`'s legs on `Won` and `Unopposed` are written by `_relocate` (`EC` `perform`,
  `_relocate(w, a, target, mover=pid)`), the journey's one body, so T10's route pricing and exposure reach them with no edit here.
  CP-T04-06 writes no leg (a besieger makes no journey). `march_budget` has no reader in this proposal; nothing is demanded.
- **Engine params:** an exporter for the module's role names under `engine/engine_params/` with a `--check`.

**What it gives them.** GV: walls that matter, and title that moves by surrender. FA: places that change hands, and grudges whose
holders are persons who fought. FI: orders as documents a spy can hold; threats and sieges as witnessed events; a field's cause.
NP: unequal bodies after a field. T09: holds that move by war, which `endings_reached` already reads.

## §6 Jordan asks, and the rulings these items touch

### Ask A · What is a raised troop? (TS's J-1, carried, not new)

- **Question.** TS2 §9 escalated it on 2026-10-16 and no plan has scheduled it (grep: TS is named only in v9's rename note,
  `workplans/valoria_master_workplan_v9.md:8`). Your demand D1 (TS1:22-24): armies are "troops levied from settlements as their own
  resource", differing "in quantity and quality based upon equipment and experience and their commanders". R-POOL forbids raising from
  the cohort.
- **Options.** (A) a troop stock in `Rung.stores` (TS's default): amends Layer 1 `04:793` and `04:802` and their copies, strains three
  clauses, keeps every ruling's content. (P/P′) a company `Person`: breaks ED-WR-0011 (no runtime Person) and RR-2 or J-16. (B) a typed
  troop row: amends the most Layer 1. (A + M-1) A, plus a field force that travels with its marchers and holds its own stores (L10 M-1),
  which is what supply, foraging and camps need (gap H).
- **Consequence.** Under A, armies are counts that eat where they stand and fight for whoever holds their walls; a won march arrives
  without its men until M-1. Under P, armies are people who choose, desert and witness, and the cast is no longer closed.
- **Ladder.** 1: not superseded. 2: not irrelevant (G1, G2). 3: no document decides it. 4: no precedent in the tree fits. 5: every
  option overwrites ratified Layer 1 or a ruling, so it survives.
- **Recommendation.** A now; M-1 as a separate later answer. CP-T04-01's subunit-per-commander shape is the same under A and P.
- **Unblocks.** CP-T04-10; gap H; IN-52's retirement.

### Ask B · What may a fought field write beyond casualties, morale and a grudge? (TS's J-5 and J-C-4, extended by one option)

- **Question.** ED-IN-0279 is RESOLVED for the loser only (`registers/editorial_ledger_in.jsonl:34`): a lost field writes "casualties
  only, decrease in morale, and a grudge token" on the losing side, "nothing else, and nothing specified for the winner". The genre's
  aftermath (D_T04 #7, #20, #49, #62) needs more. This is the single question for the mass-battle winner; T03 cites it for its
  cross-scale symmetry (R-M1) rather than settling it (cross-file ruling R7).
- **Options.** (a) As built. (b) Winners take their engine casualties too, by CP-T04-01's per-subunit ratio. (c) Survivors move one
  grade up (only meaningful under Ask A's A). (d) **Captives:** on `Won`, each defending person whose body falls below the lowest band
  floor is taken into custody by the marching seat. There is **one** combat-to-custody route and it is T03's CP-T03-09 (`capture`):
  `_disposal("detain", …)` (`loop/effects_information.py:585-611`), the opener `determine` already uses, with the `state/gate.py` basis
  that route needs to admit a custody taken by force rather than by warrant. `_eff_arrest` is not that route: it mints its own literal
  `detain` (`:1049`) under the `warrant` basis and `_may_close_custody` (`:1037-1048`). (d) adds no second mint; the field's effect
  calls T03's opener. Released by `pardon` (shipped). Death is not here: it is J-C-19.
- **Consequence.** (a) winning is free; nothing in a campaign grows or wears. (b) every field costs both sides; a winner walks away
  hurt. (d) a field makes prisoners, leverage the information and proceedings lanes already handle (P14).
- **Ladder.** 1-4 silent beyond TS2 §9 and the comparative analysis's J-C-4 row (`research/by_lane/00_COMPARATIVE_ANALYSIS.md:529`).
  5: (b), and (c)'s winners' half, overwrite nothing (the ruling specifies nothing for the winner), but they choose between two
  materially different games (a free victory or a costly one); (d) and (c)'s losers' half overwrite the ruling's "nothing else". So it
  survives on both counts.
- **Recommendation.** (b) + (d); (c) with Ask A.

### Ask C · May ENCOUNTER fight a field declared in an earlier round? (CP-T04-04; a Layer 1 amendment)

- **Question.** Ratified Layer 1 says `loop/encounter` reads "RESOLVE's own `Event[]` (selects `degree == Declared`)"
  (`architecture/meta/04_CODE_ARCHITECTURE.md:177`) and "folds RESOLVE's own deferrals" (`:541-545`): a field is fought in the round it
  is declared. CP-T04-04 fights it a round later, selecting declarations from the log and `w.acts` across rounds and seasons.
- **Options.** (a) Keep the same-round field: the defender never answers a storm; surrender and relief act only against a siege
  (CP-T04-06/07). (b) Amend both lines to "the declared, unfought acts of a prize whose row sets `fought_after` rounds have passed":
  every storm is preceded by a round in which the defender is warned and may answer.
- **Consequence.** (a) storms are surprise blows; defence is pre-commitment only (CP-T04-02). (b) every field is a two-round exchange;
  relief arrives a round late; every seeded season that fights re-pins.
- **Ladder.** 1: not superseded (REM-31 amends no Layer 1 text, `remediation-02:570-589`). 2: not irrelevant (gap D). 3-4: no document
  or precedent in the tree times a field. 5: overwrites ratified Layer 1, so it survives. **Not bundled with REM-31:** Jordan's D-2 lets
  IN-46's designs build with no gate, and a Layer 1 call carried inside that build is the bundling `CLAUDE.md` §2 forbids.
- **Recommendation.** (b).

### Not raised (each answered by the five steps)

- **Does a march need a war?** (K-MB-5, D-8.) Step 5 for this proposal: no item reads `at_war`; FA owns the gate and will raise it.
- **May a player command a field?** (J-C-31.) Step 4: Dominions' single resolver with a pre-battle order is the verified precedent
  (D_T04 #27); CP-T04-02 is that order. Not raised.
- **Death in battle.** (J-C-19, K-MB-9.) Superseded by its own open row; not duplicated.
- **Command from a person.** JQ-2 (remediation part 04); referenced by gap I and CP-T04-02 (`general` matters only through span until it
  is answered).
- **The weight→troop value.** JQ-4; this proposal adds only its floor (CP-T04-01: a weight-1 subunit at or above 80 troops).
- **The `declared` polarity.** ED-IN-0296 (1); CP-T04-09's re-entry trigger.
- **The mutual-rout tie-break.** (MB-G38.) Step 4 (gap P).
- **`sack`.** L10 §3.9 item 4 holds its tone; declined here (gap K).
- **A separate `muster` row.** Step 5: under A, TS moves troop kinds with `transfer` between settlements; a second mover would be a
  second owner of one operation. L10's case for `muster` returns if `transfer`'s eligibility (`remit:issue`) proves wrong for a commander
  at build.
- **`remit:dispatch` itself.** It comes from the `remit_default` testing fixture (T04 §0); J-8 is open and every row here moves with it,
  as `march`, `arrest` and `raze` already do.
- **`march_budget`** (WT-G07, `valoria_geography_v30.yaml:800-803`): no item here reads it, so nothing is demanded of T10 about it,
  and T10's D-4 is answered in §5.

**Rulings the items touch and keep.** ED-IN-0279 (01 changes per-person magnitude, still casualties on the losing side only; 06's
`Invested` writes walls, not a loss; 07 writes no loss). ED-WR-0011 (no item mints a Person). R-POOL (no item writes cohort weight).
T-i (06 is sustained by fresh acts, no clock). The 2026-07-08 single-resolver doctrine (one `run_battle`; 08 runs the same engine). The
garrison ruling (05 reads condition as walls only; TS's reading of it as men too stays with Ask A). R-01, R-03, R-08, R-19 (verbs-03).

## §7 Risks, and what this deliberately does not do

**Risks.**
- **Friction may drown every order.** `MB_FRICTION_SIGMA = 1.1` (`cfg:335`) gives one lognormal factor per army per battle (middle half
  0.48-2.1, T04 §1). If 02's paired-seed falsifier shows roles inside noise, 02 and 03 are cut at build, and the honest finding is that
  the engine's calibration, not the season's interface, is what makes command cosmetic (gap O).
- **JQ-4 below the floor makes 01 worse than today.** With per-person subunits a `k` under 80 per weight routs every subunit on tick 1.
- **Multi-subunit season fields are untested on the season's terrain rows** [UNVERIFIED] (TS2 §4.4 item 5).
- **04 moves every fought field by a round** (a declared hash mover over every seeded season that fights, on REM-31's re-record rule,
  remediation K1), and it amends Layer 1 (Ask C). Relief arrives late (§3 S).
- **Uncelled alignment** makes NPC postures, roles and surrenders the draw's; a town may be surrendered to a weak march by chance. That
  is churn the world shows unwatched; whether it reads as drama or noise is the cell-value pass's to settle.
- **Every `marshal` mints a hold** (+1 budget), H-92's drift, one more producer of it.
- **REM-27's own [CONFIDENCE: low]** that a seeded realm fights at all: if no defended enemy settlement enters a marcher's ledger,
  the natural run still fights nothing, and G10 stays ABSENT whatever this proposal builds.

**Deliberately not done.** A played field (J-C-31). Supply lines, foraging, camps and a field force (gap H; Ask A's M-1). Rally (gap I).
Death or pursuit on the season path (J-C-19; `run_multi_turn_battle` is not called). `sack` (L10 §3.9 item 4). Multi-unit envelopment,
Path B (`proposals/multiunit_envelopment_plan.md`, PROPOSED, held; engine-direct and unreachable from a season field of one `Unit`).
Zone of control (D_T04 #14, a difference, not a gap). `tactic_cards` (an empty dict) and `threadwork_check` (TW's). Any screen: the
estimate is a Query, and how it is shown is not designed here.
