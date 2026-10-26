# Personal combat — completion proposal (T03 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2). **Home of v10 positions** since the v10 adoption (`ED-IN-0299`): this file holds the full spec of the v10 positions whose plan row names it (rows: `workplans/valoria_master_workplan_v10_part3.md` §1; handles: `workplans/valoria_master_workplan_v10_part12.md` §1; where `workplans/valoria_master_workplan_v10_part13.md` amends a home, the amendment governs), and is deleted with a `FORK:` row when its last position lands (v10 head §9 step 6).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/…-04-t03-personal-combat.md` (T03), `…-00-overview.md` §3, §6 (OV); `research/game_precedent_suite/dispositions/D_T03.md` (D); `research/game_precedent_suite/THROUGHLINES.md` (TL); `proposals/2026-10-16-verbs/…-09-lexicon-personal-combat.md` (L09), `…-19-gap-register-pc-and-np.md` (G19, PC half); `proposals/2026-10-21-v9-remediation/` parts 02–04 (REM2, REM3, REM4); `proposals/pc_formation_system.md`; `proposals/weapon_physics_and_concentration_model.md`; `skills/ners/SKILL.md`; sibling proposals T01, T04, T10 in this directory where cited; the orchestrator's cross-file rulings R1, R5, R6, R7; code opened where cited.

Abbreviations follow T03's: `MC/` = `modules/combat/`; `SW` = `engine/season/seam/wrappers/combat.py`; `EC` = `engine/season/loop/effects_combat.py`;
`VT` = `engine/season/verb_table.yaml`; `ROS` = `engine/season/rosters.yaml`; `FX` = `engine/season/data/fixtures.py`; `EI` =
`engine/season/loop/effects_information.py`. `D:#n` is row n of `D_T03.md`. Evidence grades are T03's (RUNS-IN-LOOP, TESTS-ONLY,
DESIGN-ONLY) and are carried, never upgraded.

**The seam this file repairs first.** The initiator of violence cannot die (OV §6 #7; D:#25 CONTRADICTS): the seam returns both
parties' wound states (`SW:230`) and `_eff_kill` reads the subject's only (`EC:108`, `:125`). No remediation part or workplan position
names the repair (grep of both for `_eff_kill|two-sided|both parties` → 0), and L09 M1, which names it (`L09:316`), is an unratified
lexicon. It is therefore this file's item **CP-T03-00**, and every other item is written on the repaired seam.

## §0 The genre loop

The yardstick is warband and duel play with consequence (Battle Brothers, Kenshi, Bannerlord, Jagged Alliance 2, Kingdom Come:
Deliverance). Each row is a play opportunity a player of that genre expects: what a person chooses, at what cost, and what stays. Grade
is today's, with the evidence grade.

| # | play opportunity | precedent evidence | today | evidence grade |
|---|---|---|---|---|
| G1 | **Kit and build decide fights.** What a person carries (weapon, armour) and what he has learned (training) changes who wins; acquiring kit is a choice with a price | D:#1 DIFFERS (BB kit is the consequential lever), D:#10 HAS, D:#15 LACKS (JA2 I.M.P.); TL P23 | **ABSENT** in the season: only `end` varies (`MC/fight.py:45`; `SW:130-138`); armour, reach and history decide fights in the engine (T03 §3: plate 90.0 %, spear 95.5 %, history 5 87.8 %) | engine TESTS-ONLY; season RUNS-IN-LOOP at defaults |
| G2 | **Choosing a fight is a risk to the chooser.** The attacker can be hurt or die; whom to risk, and when, is the decision | D:#24 LACKS, D:#25 CONTRADICTS (all seven precedents); XCOM T18 §7 | **ABSENT**: actor never written (`EC:107-109`; 33 of 59 realm calls felled the actor, none written, T03 §5c) | RUNS-IN-LOOP (the defect runs) |
| G3 | **Read the odds before committing.** The chooser weighs its chance against the opponent (shown odds or an estimate) | D:#5, #14, #22, #29 LACKS; TL throughline 2, P23 | **ABSENT**: the score reads verb identity and stance only (`decision/choose.py:149-151`; OV §6 #1) | DESIGN-ONLY (`WB probabilities.py:109-123` is a workbench) |
| G4 | **Formal duel with terms.** Offer a fight before witnesses on stated terms (first blood, until one yields, to the death); refuse at a cost in face | D:#7, #12 LACKS, D:#26 CONTRADICTS; L09 F2–F3 | **ABSENT**: `challenge` (`VT:751`) writes nothing (`VT:764-765`); 0 of 39 `accept`s answer a challenge (T03 §8 #6) | RUNS-IN-LOOP as emission only |
| G5 | **A fight can end short of death.** Yield, be spared or killed; be taken captive, ransomed or rescued | D:#17, #33, #36 LACKS, D:#27 HAS (TESTS-ONLY); TL P02 (outcome fork) | **ABSENT** in the season: no `yield_decl` passed (`MC/fight.py:52`); custody only by judgment or warrant | Yield TESTS-ONLY; capture DESIGN-ONLY |
| G6 | **Injury is a ledger.** Wounds cost availability now; some leave a lasting mark that changes the person for good | D:#4, #35 DIFFERS (risk), D:#34 LACKS, D:#23 HAS; TL P32, throughline 7 | **PARTLY**: lowered body carries and costs scene actions (`decision/budget.py:57-61`); no permanent mark exists (`MC/core.py:191-193`, hit location out of scope) | body carry RUNS-IN-LOOP; mark absent |
| G7 | **Recovery has a price and a place.** Rest, a healer, time; the wounded miss what they would have done | D:#23 HAS (availability), TL P40 LACKS (D_T10 #23: `tend` gated by place, not priced) | **PARTLY**: `tend` restores to 1000 in one act; 0 of 75 computed `tend`s executed (T03 §4) | TESTS-ONLY |
| G8 | **Veterans grow.** Fighting (or training) makes a person better at it | D:#8 LACKS (KCD build-by-doing); TL P33 | **ABSENT**: `train` writes `capability`, unread by combat (`EC:397`) | DESIGN-ONLY |
| G9 | **A killing has an aftermath.** Grudges in the survivor and the dead man's kin; standing among witnesses; a sanction where there is law | D:#13, #18 LACKS; TL P11, P27, P29 | **PARTLY**: witnesses judge a killing by their own pursuits through `deed:person.died` / `deed:body.changed` cells (`ROS:3423-3424`, `:3485-3486`) read by `person_q.regard` (`judged_gain` 0.5 shipped, `FX:822`), but the chooser reads `regard` only under a non-`legacy` `stance_polarity` (`FX:833`, `decision/choose.py:56-62`); the survivor holds no grudge (only `march`, `forgive` write stance, `EC:183-323`, `:431-450`); no sanction follows (H-209) | `regard` RUNS-IN-LOOP as a Query, unread by the shipped chooser arm |
| G10 | **Who dies matters.** A ruler's death is a prize and a crisis; a played person's death has a defined outcome | D:#6, #19 LACKS; TL P30, P42 | **PARTLY**: Felled closes every tenure (`EC:178`, RUNS-IN-LOOP); no succession for null-conferral seats (OV §6 #11); no outcome for a played person's death (`GMS` silent, D:#6) | cascade RUNS-IN-LOOP |
| G11 | **Defend and be defended.** Guard a person; a third party joins; the attacked can flee or refuse | D:#21 LACKS; L09 F10–F11 | **ABSENT**: two claimants only (`SW:207-216`); no co-location test on an attack | DESIGN-ONLY |
| G12 | **Play the fight or let it resolve.** Decide moves in a fight that matters; auto-resolve the rest | D:#2 LACKS, D:#16 DIFFERS, D:#9 DIFFERS (justified); TL throughline 5, P35 | **ABSENT** today; ruled to build (IN-46, REM-31, D-2) | DESIGN-ONLY |

G12 is REM-31's. G2 is CP-T03-00's. G1 and G8 wait on JQ-2. G11 is v9 IN-59's (§1 gap L). The rest are the completion work.

**What HEAD already gives this file to build on** (opened at `2decf4a`; the T03 description is as of `51d7b05`):
- `arrest` (`VT:167-204`) opens a `detain` edge, prisoner → the issuing seat, admitted under the gate's `warrant` basis
  (`state/gate.py:809-831`, `may_warrant`: the seat sits, grants `WARRANT_ACT`, and its purview reaches the prisoner) plus
  `_may_close_custody` (`EI:1005-1010`, the seat's holder could close it under `determination`), and mints its own literal
  `Tenure(…, "detain")` (`EI:1041-1050`). `determine` opens its disposals through `_disposal` (`EI:587-610`); `pardon` (`VT:960`)
  closes `detain` and `ban` under `determination` (`ROS:126-129`). **`may_warrant` does not read the warrant Record** (`gate.py:822-826`).
- `conceal` (`VT:245`) mints a `cover` Record (`ROS:231-238`); `state/attribution.py::anchor_of` (`:105-124`) re-anchors every act of a
  covered actor on the alias, `fight` included, while `seen.who` still names him to those present.
- Guard cohorts (`harness/populated.py:447-530`, B-V): a cohort of weight > 1 posted where a seat's holder stands, with a live `oblige`
  to the seat; `build_realm(guards=…)` ships OFF (`:738-740`). `world_q.guard_weight` (IN-60) is named in that docstring (`:494`), in
  `cohorts.yaml:105`, `:126`, and as a test-local `_guard_weight` (`tests/test_in36_foreign.py:317`), and **does not exist** in
  `queries/world_q.py`. Its designated reader is v9 **IN-59** (`v9_part5.md:143-147`, B-Y): a `with` conjunct on `fight`, `accept`,
  `challenge` and an `audience` stem on `move`, `migrate`.
- `PC-10a` / `PC-10b` (duel terms, the challenge Record) are v9 positions in batch B-Y (`v9_part7.md:56-60`) and are **not built**:
  `challenge` still writes nothing (`VT:764`) and `accept` still reads no challenge (`VT:784`).
- `train` writes `Person.capability` only on a key the subject already holds (`EC:397-423`); `capability` is empty on every corpus
  person, its writers being a `cast:` overlay and `train` (`seam/wrappers/sigma.py:122-124`). `tend` raises body to `condition_scale`
  (`EC:371-393`). `stance_polarity` has a `declared` arm in which a grudge raises `fight` on its object (`FX:824-833`; H-194).
- T10's CP-T10-04 (sibling proposal) adds MATTER's rising body arm and `tend_share` [ASSUMPTION 0.5]: after it, MATTER raises bodies too.

## §1 Gap ledger

Rows are `D_T03.md`'s: every LACKS row (19), the DIFFERS rows the dispositions mark as a risk the precedent shows or as less legible
(#1, #4, #16, #31, #35, #39: 6), and every CONTRADICTS row (5). #9 and #43 are DIFFERS rows the dispositions judge justified and are
not re-raised. **30 rows addressed.**

| gap | rows | ending |
|---|---|---|
| **A. The initiator is never written; the middle band records a defeat** | #24, #25, #39 | **closed by CP-T03-00** |
| **B. No in-fight control; mode by party test** | #2, #16 | **closed by REM-31** (IN-46, D-2). CP-T03-05 gives REM-31's decider its odds input (#29) |
| **C. Build: kit and training do not reach the fight** | #1, #8, #15 | **Jordan ask, carried: JQ-2** (REM4:32-55). Option (b), "identical fighters are intended at those two scales" (REM4:47-48), withdraws both CP-T03-03 (kit) and CP-T03-04 (training); option (a) admits them in the shapes given. Not re-asked |
| **D. No odds at the decision** | #5, #14, #29, #31 | **closed by CP-T03-05** (the Act-interface half: the player sees the true odds; REM-31's decider reads them). Whether an NPC's score reads expected success is **AQ-X1** (T01 §6), cited, not re-asked. #31's "less legible" gradient is closed by the same odds |
| **E. The upset floor reaches nothing** | #22 | **declined.** (1) not superseded; (2) **irrelevant to the world**: the floor flips `result`, and nothing in `engine/season/` reads `result` or `winner` (T03 §1); CP-T03-00 reads trackers, so it stays unread. Its intent, "a chance at winning", is JQ-2's constraint text |
| **F. A formal duel has no carrier; the challenged never answers** | #7, #12, #26 | **closed by v9 PC-10a / PC-10b** (B-Y: terms, the challenge Record, `accept` requires it) |
| **G. Every fight ends in death or nothing** | #17, #36 | **closed by CP-T03-09** (`capture`, on PC-10a's `yield` stop). The rescue half is **declined (parked as CP-T03-10)**: (5) closing another man's restraint by force has no gate basis (`state/gate.py:109-117`), and adding one is a Layer 1 amendment the narrow N-line does not earn now |
| | #33 | **declined.** (3) answered by design: the moves inside a fight are the scene's and IN-46's (`L09:23`); a played person's `yield` is a move of REM-31's decider |
| **H. No lasting injury** | #4, #34, #35 | **closed by CP-T03-07** (a body ceiling, on the ruled `Site.condition` model). #35's hit location is ruled out of scope (ED-PC-0055, J-20 (B)) and is not re-raised |
| **I. A killing leaves no relationship** | #18 | **Jordan ask, carried: ED-IN-0296** (open; it decides `stance_polarity: declared`). The survivor's grudge (CP-T03-06) is **parked** on it: under the shipped `legacy` arm a grudge lowers `fight` on its object (T03 §8 #5), the same ground T04 cut CP-T04-09 on. The witnesses' judgment is already carried by `regard` (§0 G9) |
| **J. No law answers a witnessed killing** | #13 | **declined here.** (3) answered by design: the dead victim's claim becoming a question is H-209, whose owner (IN-12 step 5) REM-04 (ii) names. Interface demand to GV/SC in §5 |
| **K. A death changes nothing larger** | #6, #19 | **declined here.** #19: (3) the empty throne is GV's null-conferral seats (OV §6 #11) and the vacancy claim is H-206 (K-PC-10; L09 PC-G28). #6: (5) architecture: a played person is a callback on a person id (`harness/play_surface.py::dispatching_chooser`); his death is a `person.died` Event (after CP-T03-00, on either side), the loop runs on, and which person the host seats next is the host's; an heir has no carrier while births are set aside (ED-WR-0011, provisional, "for now") |
| **L. Nobody can be protected; attacks cross any distance** | #21 | **closed by v9 IN-59** (B-Y, after IN-60): guards gate entry to a guarded rung and an attack needs `with`. This file adds `with` to its own contested rows (CP-T03-09) so none acts across distance. The N-party scene (L09 M7) is declined: (5) at warband size the fight is `march` (MB) |
| **M. Suite claims the dispositions corrected** | #48, #49, #50 | **description edits, not gaps**, applied in T03 round 3 (OV §5.2's loop row; T03 §5a's wound row; T03 §7's IN-46 menu) |

Tally: closed by items 12 · by a remediation item or v9 position 6 · declined 5 · carried Jordan asks 4 (JQ-2 for gap C; the open stance-polarity question for gap I) ·
description edits 3.

## §2 Items

Layer: every item binds **Layer 2** (the game code and its data). Hash: behaviour lands behind a fixture or roster whose control arm
reproduces today's outcomes; where an item adds a `Person` field or a formation, it is a **schema or formation mover** even at its
control (`state/world.py:176-177`: `_entity_digest` hashes the dataclass `repr`; H-208, "moved by SCHEMA alone"), and says so.

### CP-T03-00 · Both parties of a fight take their band (the repair; L09 M1)

| | |
|---|---|
| adds | `_eff_kill` reads `wound_state` for **each** party (both already returned, `SW:230`, `:237`) and writes each its own band by the existing rule: Felled → body 0 and `World.remove_person`; Wounded → `wound_harm_model`'s magnitude; Untouched → nothing. The `Change` names two Subjects, each earning its own band's kind (`_eff_march`'s `earns=` shape, `EC:321-323`), so a felled attacker emits `person.died` and `contest.undecided` is emitted only when neither party took a band. The rows' `writes_source_note` (`VT:716`) is corrected from "`wound_state[THE ACT'S SUBJECT]`" to each party |
| owner | `loop/effects_combat.py::_eff_kill`; `fight` / `accept` rows in `verb_table.yaml` (notes; the band cells are unchanged) |
| primitives | P23 (the draw), TL throughline 3 (failure lands on whoever lost) |
| reads / writes | writes `(Person, body)`, `(Person, exists)`, `(Tenure, until)` — rows already licensed — on the actor as well. Asymmetry: no getter changes; the one writer `EC:156` now runs per party |
| joins | MB: `march` writes losers only (`EC:184-187`); whether a won field writes the winner is **T04's Ask B** (R7), cited, not settled here. REM-31: its AUTOMATED = PLAYABLE control is pinned after this lands |
| chooser / world | attacking now risks the attacker's life; unwatched, the killers of seeds 0-2 who were felled in the scene die |
| falsifier | through the real seam, T03 §3's recipe (n = 400): every one of the 205 felled actors emits `person.died` and leaves `w.persons`; 0 of the 94 Untouched-subject fights emit `contest.undecided` with a felled actor; mutation: read `wound_state[subject]` for both and the actor deaths return to 0 |
| control | paired seeds 0-2, two seasons, against the pre-item tree: today 26 Felled subjects and 33 felled actors unwritten (T03 §5c) |
| hash / revert | **declared mover, and it roughly doubles combat deaths** (up to 33 more over seeds 0-2, fewer as dead attackers stop acting); every seeded season that fights re-pins in its own commit; revert: the one effect |
| size | S |

Why an item and not an ask: (5) architecture: the seam returns both parties; reading only the subject's is a defect (OV §6 #7 files it
so). The quote at `EC:4-6` ("accept the result") rules the magnitude of harm, not who is written, and is not cited for this.

### CP-T03-01 · Cohorts are never a party to a personal fight (weight bound; L09 M2)

| | |
|---|---|
| adds | T10's **`individual` CELL stem** (CP-T10-08: weight 1) as a conjunct in the typed `requires` of `fight`, `accept` and `capture`, on both parties. One stem, T10's. A `@requires_predicate` would never run: the fold evaluates a typed cell **or** a `REQUIRES_PREDICATES` entry, never both (`loop/resolve.py:273-283`), and these rows are typed (`VT:653-656`) |
| owner | `verb_table.yaml` rows; the stem is CP-T10-08's (`data/requires.py`) |
| primitives | P24 (a typed precondition) |
| reads / writes | reads `Person.weight`; writes nothing; emits the row's refusal kind |
| joins | T10 (the stem); MB: a population is fought by `march` only (L09 PC-G16); B-V: guard cohorts are never felled whole by one blow |
| chooser / world | removes an act no person should have; unwatched, a cohort is no longer deleted whole by one Felled band (OV §6 #7) |
| falsifier | a hand-built `fight` on a cohort through `dispatching_chooser` is refused and leaves its `weight`, `body` and tenures; mutation: drop the conjunct and the cohort is removed |
| control | `build_realm(0)` 2 seasons: equal wherever no cohort was a party (L09's 1 of 63 [UNVERIFIED at HEAD]) |
| hash / revert | mover where a cohort fought; revert: the conjunct |
| size | S |

### CP-T03-02 · The band's Event says how the fight ended, and what the body now is (L09 M12, widened)

| | |
|---|---|
| adds | (i) the band Event's payload carries, per party, `felled` / `yielded` / `undecided`, read off the lifted `wound_state` and `surrender` (`SW:230-243`); (ii) each `body.changed` carries an Observation `(person, "body", new value)` — REM-51's precedent of an Observation riding a body write (`REM3:349-369`), the claim shape WITNESS already deposits for `stores:<kind>` and `condition` (`loop/witness.py:163`, `:661`) |
| owner | `_eff_kill`; the kinds in `verb_table.yaml` |
| primitives | P27: a believed body is a claim like any other, and decays like one |
| reads / writes | reads the Resolution only; writes no new field |
| joins | IN (WITNESS): no new channel. FI: a believed body is evidence. T10: its rising arm's `body.changed` should carry the same Observation, so a healed rival is believed healed |
| chooser / world | gives CP-T03-05 (mode b) and CP-T03-08 their lawful input: a person knows a rival is weakened from what he saw or was told (04 PART D row 2) |
| falsifier | after a Wounded band, an observer holds `(subject, "body", v)` with `v` the written body; a non-witness holds none; mutation: emit before the write and `v` is the pre-fight body |
| control | the trace and band kinds are unchanged (`test_combat_trace_returned.py`) |
| hash / revert | mover (payloads and deposits are hashed); revert: payload and Observation |
| size | S |

### CP-T03-03 · Kit reaches the fight (exists only under JQ-2 (a))

| | |
|---|---|
| adds | (i) arms as `matter_kinds` members (`ROS:1423`, an open registry, `ROS:1413`); (ii) a roster `arms_kinds` mapping each arms kind to one Combatant field (`weapon` or `armor`), one key and a declared `rank`, **validated at load against a typed export of `modules/combat/weapons.py`'s `WEAPONS` keys and the armour tiers** under `engine/engine_params/` behind an exporter with a blocking `--check` — T04's export shape (its CP-T04 role export), one `engine_params` loader for both files and CP-T03-05's table, never a copied list in `rosters.yaml`; (iii) `world_q.kit_of(w, pid) -> (weapon, armor)`: per field, the top-ranked arms kind with a positive count in the stores of the rungs the person `hold`s, else of his `reside` rung (`world_q.py:1215`), else the Combatant default; (iv) `PersonalCombatInput` gains `kits`, a tuple per party in `claimants` order, `ends`' shape (`queries/inputs.py:100-114`); `MC/fight.py:45` passes them to `Combatant(…, weapon=, armor=)`; (v) `arms_at_build`, keyed on the rung kind of a holding [ASSUMPTION; medium], seeding arms into stores |
| owner | `rosters.yaml: arms_kinds`, `arms_at_build`; the export and its exporter; `world_q.kit_of`; `queries/inputs.py`; `MC/fight.py` |
| primitives | P23 (the draw's modifiers); the stock is `Rung.stores` moved by `_shift` (`loop/effects_shared.py:128`) |
| reads / writes | reads `Rung.stores`, `hold`, `reside`; writes nothing at the fight (kit is **read, not consumed**, [ASSUMPTION; medium]); acquisition writes `Rung.stores` through the shipped `transfer` and `requisition` |
| joins | **EC**: `craft` (verbs-16 S2, DESIGN-ONLY) is the arms producer. **MB**: no shared reader is claimed; MB's arsenal is `modules/mass_battle/equipment/__init__.py:21` (`TROOP_LOADOUT`, `ARSENAL`, `ARMOURY`). If MB wants persons' arms to equip levies, it maps its arsenal from the same matter kinds (MB's call) |
| chooser / world | choose to move arms into one's holding at the cost of the act and the goods; unwatched, armoured houses win the fights they start (T03 §3: plate 90.0 %, spear 95.5 %, "knight" 93.2 %), so wealth turns into martial safety |
| falsifier | `kit_of` on a holder of a stocked rung returns the roster's top-ranked kind; at stock 0 the default; a seeded `fight` with the subject's holding stocked with plate fells the actor at T03 §3's 97.5 % ± sampling (n = 400, real seam); `--check` fails on an `arms_kinds` key not in the export; mutation: read the actor's kit for both parties and the asymmetry vanishes |
| control | `arms_at_build: {}` and no arms in any store: every Combatant at `arming`/`light`, today's outcomes. Hash equal unless `Rung.stores` is built keyed on every matter kind, in which case adding kinds is a schema mover [UNVERIFIED; measured at the item] |
| hash / revert | mover where any party holds arms; revert: the empty build roster |
| size | M |

**Gated on JQ-2 for its existence, not only its magnitude.** JQ-2 option (b) is "identical fighters are intended at those two scales"
(REM4:47-48); kit makes fighters non-identical, so under (b) this item is withdrawn. Under (a), JQ-2's other clause, "don't deprive the
player of a chance at winning", bounds the ranks: plate against cloth leaves the underdog about 7.5 % (T03 §3).

### CP-T03-04 · Training and fighting make a person better at it (exists only under JQ-2 (a))

| | |
|---|---|
| adds | (i) a vocation `arms` in `verb_capability`'s range, so `train` (`EC:397-423`) can raise it; (ii) the seam derives the Combatant's skill term from `capability["arms"]` by one formula in `SW` beside `party_end`; (iii) **producer:** a `cast:` overlay with authored `arms` values for named fighters (the overlay is `capability`'s existing writer, `sigma.py:122-124`) [ASSUMPTION: which persons, authored in the cast data]; (iv) build-by-doing: `_eff_kill` raises `capability["arms"]` by one on each surviving party who already holds the key (`train`'s never-mint rule, `EC:404-409`) |
| owner | the vocation row; the cast overlay; `SW` (derivation); `_eff_kill` (the write) |
| primitives | P23's skill input; no TL primitive names growth by use, so this composes P23 with `train`'s write |
| reads / writes | reads and writes `Person.capability` (a second writer beside `_eff_train`, whose one assignment is `EC:420`) |
| joins | NP owns `train`; SC's pool reads `capability` through `sigma.py::_pool_of`, so `arms` must stay out of social pools (`verb_capability` maps each verb to one key) |
| chooser / world | spend acts training, or gain by surviving; unwatched, the authored fighters who keep winning grow, and become the feared. Persons the overlay does not name never grow (narrowed, §3) |
| falsifier | a person with `arms` 5 against defaults reproduces T03 §3's history-5 row (87.8 %) through the seam; a surviving holder gains one; a non-holder gains none |
| control | **formation mover even at control**: adding `arms` to the vocation range adds one `train` Candidate per vocation (`decision/options.py:182-193`, `:279-280`), whether or not anyone holds the key |
| hash / revert | formation mover at landing; outcome mover once a key is held; revert: the vocation row and overlay |
| size | M |

Under JQ-2 (a) "through the pool only", the derivation feeds the pool term `round(history) + 6` (`MC/core.py:54-56`) and must not
move the Ob term `defender.history / 2` (`MC/core.py:100-115`), which reads the same field: a `modules/combat` split, PC lane.

### CP-T03-05 · Combat's odds, as an input to T01's odds function (Act-interface half)

| | |
|---|---|
| adds | (i) a typed artifact `engine/engine_params/pc_matchup.json`: for every `(end_a, end_b, kit_a, kit_b)` cell over `end` 1–4 and the `arms_kinds` roster, the shares of actor felled / subject felled / yielded / undecided, produced by running `MC/fight.fight` over a fixed seed list; (ii) its exporter `tools/export_pc_matchup.py` with a blocking `--check`, so an `arms_kinds` edit that leaves the table stale fails (`CLAUDE.md` §5); (iii) **no new function**: T01 owns the odds reader (`odds_of(w, act)`, true; `estimated_odds(p, c)`, believed; T01 CP-T01-03, R1). For a row contesting `"the body"`, those functions read this table instead of `band_odds`. Mode (a), the player's Act interface: the true `end` and `kit_of` of both parties. Mode (b): own body and kit, the rival's believed body (CP-T03-02's Observation) and kit; where the person holds no claim about the rival's body or kit, mode (b) returns `None` for that factor (R1) |
| owner | the artifact and exporter; the combat branch inside T01's function |
| primitives | P23 ("odds may be shown"); throughline 2 (mode (a) shows the dealt odds; AX-7, `architecture/meta/01_AXIOMS.md:299-304`) |
| reads / writes | reads the table, the world (mode a) or the person's ledger (mode b); writes nothing |
| joins | **T01**: the combat branch of its function. **REM-31**: IN-46's decider reads mode (a) (D:#29). **T02 / AQ-X1**: whether an NPC's score reads expected success is the one consolidated ask, carried by T01 §6; **no score term is proposed here** (R1; `ARCHITECTURE_V2.md:508-528` rules the score's shape) |
| chooser / world | the player sees, before choosing `fight` or `capture`, the odds the engine will deal; NPCs choose as today until AQ-X1 is answered |
| falsifier | `--check` fails after an `arms_kinds` rank edit with the table unregenerated; mode (a) at `end` 4 vs 1 returns the table's cell, within sampling of T03 §3's 80.2 % subject-felled; mode (b) for a person holding no Observation of the rival returns `None` for the rival's factors |
| control | no loop caller: the season is hash-equal |
| hash / revert | neutral (read-only); revert: the branch |
| size | M |

### CP-T03-06 · The survivor's grudge — PARKED (trigger: ED-IN-0296)

The item: after a fight, each surviving party who took a Wounded band appends `(other party, -1.0, combat_grudge_weight)` to his
stance, `_eff_march`'s row shape (`EC:301-306`), symmetric by role. **Parked**, by one cut test applied as T04 applied it to CP-T04-09:
at the shipped `stance_polarity = "legacy"` (`FX:833`) a grudge **lowers** `fight` on its object (T03 §8 #5), so the item would make
revenge rarer; `declared` rides ED-IN-0296, which is open. Trigger: ED-IN-0296 answered for `declared` (or `regard`); then the item
lands with a control arm that writes no row. The refusal-cost cell L09 paired with it is **dropped**: PC-10b's challenge Record has
no term or expiry (`v9_part7.md:58`), so nothing lapses for a cell to judge, and this file names no lapse owner.

### CP-T03-07 · A lasting mark: the body ceiling (this file owns `body_ceiling` and the marks; R5)

| | |
|---|---|
| adds | (i) `Person.body_ceiling: int`, built at `condition_scale`; (ii) when a party survives a fight with `wounds >= max_wounds` on his lifted tracker (both `wound_quantities` members, `ROS:808-822`: the engine's own deepest gate short of felling), his ceiling falls to one below the next `body` band floor beneath it (800 → 799, 500 → 499, 100 → 99; floors `ROS:2682-2685`), at most three times; (iii) **every raiser of body heals toward `body_ceiling`**: `tend` (`EC:389`) and T10's CP-T10-04 (its MATTER rising arm and its `tend_share`), which reads this field as its cap (or `condition_scale` where none is set); (iv) a fixture `body_mark_model ∈ {none, deepest_gate}` [ASSUMPTION; medium; revert `none`], REM-52's precedent for shipping a harm live with a named revert |
| owner | `state/carriers.py` (the field), `write_matrix.yaml` row `(Person, body_ceiling)`, `_eff_kill` (writer); readers `_eff_tend` and CP-T10-04's arm |
| primitives | **P32** (permanent injury mark); P05 (the budget already reads body bands, `decision/budget.py:57-61`) |
| reads / writes | writes `(Person, body_ceiling)` from `_eff_kill` only. **Asymmetry (§0.1 pt 1):** assignments of `.body` at HEAD outside tests and harness are `EC:156`, `:297`, `:299`, `:392` and `loop/matter.py`'s body clock; at HEAD only `_eff_tend` (`:392`) raises a body, and after CP-T10-04 MATTER's rising arm raises one too. Both raisers read the ceiling; no lowering writer needs it |
| joins | **T10** (CP-T10-04 reads `body_ceiling`; both files say so); NP owns `tend`; MB's field survivors could take the same rule (MB's call) |
| chooser / world | a maimed veteran fights at `end` 3 and acts one scene fewer for life; whether to risk a crippled champion becomes a choice; unwatched, the realm accumulates marked men whose history shows in their numbers |
| falsifier | a survivor at `wounds == max_wounds` holds `body_ceiling` 799; `tend` on him at body 250 under T10's `tend_share` 0.5 gives `250 + 0.5 × (799 − 250)` = 524 (floor rounding [ASSUMPTION: T10's]), where the same `tend` on an unmarked man gives 625; at T10's rising arm he never passes 799; his budget sits one below whole; mutation: a raiser reading `condition_scale` lifts him past 799 |
| control | `body_mark_model: none` reproduces today's outcomes; the field itself is a **schema mover** at landing (H-208) |
| hash / revert | schema mover at landing; outcome mover at `deepest_gate`; revert: `none` |
| size | S |

**Not a re-raise of D:#4 or #35.** Those rulings keep hit location out (ED-PC-0055, J-20 (B)) and make the body one recoverable
scalar on the `Site.condition` model (H-38). A Site's condition is bounded by a ceiling (`queries/world_q.py:389`, `ceiling`), and
`tend`'s own docstring reads its magnitude as "the headroom to the ceiling" (`EC:374-376`). This item gives the body the ceiling its
model has; it adds no location and no second scalar the fight reads.

### CP-T03-08 · `tend` forms on the wounded

| | |
|---|---|
| adds | a stamper `wounded_with(…, cls="Person")` on REM-21's `STAMPERS` registry: the asker himself when his own body is below his ceiling, and each person `with` him whom **he believes** below whole — the newest `(person, "body", v)` Observation he holds (CP-T03-02) under `v < condition_scale`. It reads no other person's true body, so it does not repeat the AX-7 tension H-207 records for `vacancies` (`hole_register.yaml:4523`). `tend` declares `referent_class: Person` (REM-21 (iii)) |
| owner | `queries/world_q.py` (REM-21's registry); `verb_table.yaml`'s `tend` row |
| primitives | P40 (recovery at a place: `with` the tender), TM01 |
| reads / writes | reads own body and ceiling, the asker's ledger, `with`; writes nothing new |
| joins | NP / T10 own `tend` (and its `tend_share`); REM-21 lands first; REM-52's hungry and T10's sick are its other customers |
| chooser / world | the wounded, or the one who saw him hurt and stands beside him, has the act in front of him at the cost of a scene; unwatched, the wounded recover where someone who knows is with them |
| falsifier | seeds 0-2, two seasons: `tend` executes > 0 times (today 0 of 75, T03 §4); every executed `tend` names a body below its ceiling; a wounded man nobody saw hurt is stamped only for himself; mutation: stamp from true bodies and an unwitnessed wound is tended by a stranger |
| control | REM-21's base: no row declares the class, hash equal; this commit is the mover |
| hash / revert | mover; revert: the row's class |
| size | S |

### CP-T03-09 · `capture`: take a beaten man into a seat's custody (L09 M5; a named fold of `fight`)

| | |
|---|---|
| adds | a row `capture` (L09 Suite A: own key on `_eff_kill`), `contests: "the body"`, `requires_typed`: the subject exists, is `with` the actor (IN-59's conjunct, so this row never acts across distance) and is an `individual` (CP-T03-01). The scene runs under PC-10a's **`yield`** terms. Bands as `fight` (CP-T03-00, both parties), plus: a **subject who yields** is not removed — a `detain` opens, prisoner → the seat the act was exercised through (`a.via`), **by arrest's admission and nothing new**: `may_warrant(w, actor, via, prisoner)` (the gate's `warrant` basis, `state/gate.py:809-831`, which reads no warrant Record) and `_may_close_custody(w, via, prisoner)` (`EI:1005-1010`), and a literal `Tenure(…, "detain")` in the effect as `_eff_arrest` mints one (`EI:1049`), so `_derive_openers_from_effects` reads the opener. A custody the seat could not close is never opened (H-231 (2)'s uncloseable case). Emits `person.captured` (one emitter, so `KIND_VERB` maps it). A Felled subject is dead as under `fight`; an actor who yields walks away with his band |
| owner | `verb_table.yaml` row; `_eff_kill` (the branch on the lifted `surrender`, `SW:243`). **`state/gate.py` is unchanged**: the `warrant` basis already admits a `detain` whose object is a seat granting `WARRANT_ACT` and reaching the prisoner [UNVERIFIED: that the gate clause keys the edge's object to `via`, not to an issuing seat read elsewhere] |
| primitives | P02 (the fork at the yield: taken or dead), P14 (the captive is a token FA's ransom spends) |
| reads / writes | writes `(Tenure, since)` for `detain`, plus `fight`'s writes; reads `surrender` |
| joins | **GV**: `pardon` closes it under `determination`; `determine` disposes; the `detain` readers apply unchanged (`ROS:121-123`). This is **the one custody-from-combat route**: T04's Ask B (d) (captives from a field) reuses it. **FA**: ransom (verbs-15 V152, DESIGN-ONLY). **Lexicon**: `arrest` and `capture` are now two keys on one admission (L09 §3.8's recommendation): `arrest` needs a held warrant and contests standing (`VT:182-183`); `capture` needs a yield in a fight |
| chooser / world | a seat-holder who may take men into custody chooses to take a rival alive (worth more to his faction than a corpse); the beaten man lives. Unwatched: enforcement seats take rivals prisoner, and their factions have a captive to pay for |
| falsifier | a seeded `capture` whose subject yields leaves him in `w.persons` with one live `detain` to the actor's `via` seat, `person.captured` emitted, `move` by the captive declined; a `capture` by an actor whose `via` seat grants no `WARRANT_ACT`, or whose holder could not close the custody, opens nothing; a `capture` across settlements is refused; mutation: route the yield to `remove_person` and the captive is gone |
| control | no person forms `capture` (row absent from `resolvable_verbs`): hash equal |
| hash / revert | mover once formed; revert: the row |
| size | M |

Narrowed by the precedent it follows: only a seat that may warrant can capture. Which realm seats grant `WARRANT_ACT` (J-8 is open,
`VT:170`) is not measured here [UNVERIFIED]; if none do, the row never forms, and that is the reading to take at the item.

### CP-T03-10 · `rescue` — PARKED (trigger: a gate basis for closing another's restraint by force)

L09 Suite C's `rescue` closes a live `detain` by defeating its keeper. A `detain` is owned by the prisoner and closable only under
`determination` (`ROS:126-129`; F3's clauses, `state/gate.py:109-117`); a third party closing it by force has no basis, and adding one
is a Layer 1 amendment (04 §C.2). The N-line is narrow (§3), so it is parked with that trigger, not raised as an ask.

### CP-T03-11 · Guards turn an open attack away — CUT (composed into IN-59)

v9 IN-59 (`v9_part5.md:143-147`) is `guard_weight`'s designated reader: guards gate **entry** to a guarded rung (the `audience` stem on
`move` / `migrate`), and an attack needs `with`. A second guard gate on the blow would put two rules on one path, and its "hash equal
at `guards=False`" would not hold: IN-60 counts any sworn weight, and FA-04's oath is live at shipping (`offices.yaml:191`, obligees
`["NPC-070"]`). What survives of this item is the `with` conjunct on `capture` (CP-T03-09).

## §3 NERS

Method per `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. Every person is a seat a player can occupy through the Act
interface, so R-PLAYER binds wherever a person fights; R-WORLD binds the unwatched realm.

| object | N-line (cut it and the game can no longer…) | attack | verdict |
|---|---|---|---|
| CP-00 both parties | …make starting a fight a risk | nothing else writes the actor; `wound_state[actor]` is discarded (`EC:125`) | **HOLDS** in all directions |
| CP-01 cohorts not parties | …keep a population from being deleted by one sword-blow | `march` fights populations, but `fight` still admits them | **HOLDS, narrowed** (R-COMPLETE at an extreme) |
| CP-02 how it ended + believed body | …let anyone know a rival is weakened without being omniscient | the trace (`SW:252`) is returned and never folded; no claim carries a value | **HOLDS** (the lawful input of CP-05 mode b and CP-08, NERS C3) |
| CP-03 kit | …make wealth or preparation decide a fight | body bands vary `end`, but nothing a person can acquire does | **HOLDS, conditional on JQ-2 (a)**; the MB-sharing direction claimed earlier is withdrawn |
| CP-04 training / growth | …have veterans | `train` writes `capability`, which the fight never reads; with no producer the key is never held (disqualifier 2), so the cast overlay is named | **HOLDS, narrowed** to authored fighters; conditional on JQ-2 (a) |
| CP-05 odds | …let the player see what a fight will deal | T01's function has no combat input; WB's odds are a workbench | **HOLDS, narrowed** to the player and REM-31's decider; the R-WORLD half is AQ-X1's |
| CP-06 grudge | …make a fight start a feud | under `legacy` it does the opposite | **PARKED** (ED-IN-0296) |
| CP-07 body ceiling | …let a fight leave a permanent mark | no other store bounds a body; T10's arm heals to scale without it | **HOLDS**. Meta-rule: one field, argued on the ruled `Site.condition` model |
| CP-08 `tend` stamper | …recover by another's hand at all (0 of 75 today) | REM-21 supplies the shape, not this occasion; T10's arm heals by time | **HOLDS, narrowed** to care (time is T10's) |
| CP-09 `capture` | …end a fight with a living, held enemy | `arrest` needs a warrant and contests standing; `determine` needs a proceeding | **HOLDS, narrowed** to seats that may warrant |
| CP-10 `rescue` | …free a captive except by pardon | needs a basis the gate lacks | **PARKED** |
| CP-11 guards | …protect a person | IN-59 already gates entry with guards | **FALSE N-LINE** (disqualifier 1): cut |

**Other cuts taken.** `assassinate` as a key (L09 M6): false N-line, disqualifier 1 — a covered actor's every act is re-anchored on the
alias (`state/attribution.py:114-124`); what dies, a separate valuation of treachery, is D-V6's (Jordan's). `ambush` as a first-mover
content: the cadence draw, not the coin's `first`, decides who swings first (T03 §2.3), so the residue is a label. `shoot` (L09 M9):
no ranged weapon exists (disqualifier 2). The N-party scene (L09 M7), the `fight.refused` rename (L09 M14), kit consumption and
looting: not proposed. The challenge-refusal cell: dropped (no lapse).

**R.** R-PLAYER gains: whom to fight at a real risk (CP-00), seen odds (CP-05), kill or take alive (CP-09), when to risk a marked
champion (CP-07), whom to tend (CP-08); kit and training under JQ-2 (a). R-WORLD gains: attackers die, captives with factions behind
them, marked veterans, wounded recovering where someone saw them fall. **R-COMPLETE at the extremes:** a cohort party, the felled
attacker, the yielded man, the man at three marks (ceiling 99: alive, `end` 1, budget floored by `budget.py`'s `max(1, …)`).

**S.** One resolver: every act fights through the `"the body"` prize and `_eff_kill`'s band reading. **Consistent methodology:** the
ceiling steps on the body band floors the budget and `end` already read; custody uses arrest's admission; odds go through T01's one
function. **Pauses correctly:** under REM-31 `capture` defers to ENCOUNTER with `fight`. **Zoom:** a captured commander leaves a
muster (`loop/sides.py` excludes a `detain` holder). **The one S question left open:** `march` writes losers only (`EC:184-187`)
while `fight` writes both parties after CP-T03-00; whether a won field writes the winner is **T04's Ask B** (R7: ED-IN-0279 is
resolved for the loser only), cited, not settled here.

**E (last, as a ratio).** In: 1 row (`capture`), 1 field (`body_ceiling`), 2 rosters (`arms_kinds`, `arms_at_build`), 1 exported
table and 1 export, 2 Queries (`kit_of`, a stamper), 2 fixtures, 1 combat branch in T01's function; under JQ-2 (a) only for the kit
and training halves. Out: `assassinate`, `ambush`, `rescue` (parked), the guard gate, the grudge (parked), the refusal cell, the score
term. Every kept object holds an N-line. **E-intuition:** better kit, better odds (seen); a beaten man yields if you meant to take
him; a wound past the last gate marks you for life. **Holds.**

## §4 One season, after

Figures are from T03's runs on the shipped engine unless marked `illustrative`. Persons are seed-0 realm ids; their choices are
illustrative (the chooser draws them). Kit assumes JQ-2 (a).

1. **CALENDAR / MATTER.** `p_npc_011` holds a rung whose stores carry mail and a spear (`arms_at_build`, illustrative); `kit_of`
   returns `(spear, medium)`. `p_npc_082` holds nothing armed: `(arming, light)`. Both are in one settlement.
2. **DELIBERATE.** If a player has `p_npc_011`, the Act interface shows `capture` on `p_npc_082` at the true odds (CP-T03-05 mode a):
   spear against defaults fells the subject in 99.8 % of fights and the actor in 0.2 % (T03 §3; mail would add to it). As an NPC he
   draws among his candidates as today (AQ-X1 open).
3. **RESOLVE → ENCOUNTER** (under REM-31). The scene runs under `yield` terms; `p_npc_082` yields in turn 1 (illustrative). His seat
   may warrant, so a `detain` opens to it; `person.captured` is witnessed. `p_npc_082` took two wounds: `body.changed` carries his new
   body (`1000 × 18 ÷ 40 = 450`, T03 §0a step 1's arithmetic) as an Observation.
4. **Elsewhere, unwatched.** `p_npc_006` attacks `p_npc_020`, the King, as in today's trace #0 (`p_npc_006` felled, the King at two
   wounds, health 18 of 40). Now the felled attacker **dies** (CP-T03-00). Under IN-59 the attack needs `with`; inside a guarded
   court the stranger never reaches him. Had the King taken a third wound and stood (illustrative), he would hold `body_ceiling` 799:
   `end` 3 and one scene action fewer, for life.
5. **The captive's side.** `p_npc_082`, detained, forms `tend` on himself (CP-T03-08): below his ceiling, `with` himself. Under T10's
   `tend_share` 0.5 his body rises `450 + 0.5 × (1000 − 450)` = 725 (illustrative arithmetic on T10's [ASSUMPTION]); T10's rising arm
   adds its step each season after, never past his ceiling. His faction's road to him runs through FA's ransom or GV's `pardon`.
6. **WITNESS / CENSUS.** Those present hold `person.died` for `p_npc_006` with his actor named, and `person.captured`; each judges each
   deed by his own pursuits (`regard`).

## §5 Order and dependencies

**Within the proposal:** CP-00 → CP-01 → CP-02 → CP-05 → CP-07 → CP-08 → CP-09; CP-03 and CP-04 wait on JQ-2; CP-06 on ED-IN-0296;
CP-10 on a gate basis.

**Where CP-T03-00 lands.** It edits `_eff_kill`, which B-Y edits (PC-10b emits `duel.yielded`, `v9_part7.md:58-59`), and it must
precede REM-31's golden re-pin so IN-46's AUTOMATED = PLAYABLE control is pinned on the repaired seam: **its own declared-mover commit
inside B-Y**, before REM-31.

**Dependencies (named, not repeated):** PC-10a / PC-10b (B-Y): CP-09; IN-59 / IN-60 (B-Y): the `with` conjunct and guards; REM-21:
CP-08; REM-31: every item defers to ENCOUNTER with `fight`; REM-51 (Observation precedent): CP-02; JQ-2: CP-03, CP-04; ED-IN-0296:
CP-06; AQ-X1 (T01): the NPC half of CP-05.

**What this needs from other subsystems:**
- **T01:** a combat branch in `odds_of` / `estimated_odds` that reads `pc_matchup.json` for rows contesting `"the body"` (CP-05).
- **T10:** CP-T10-04's rising arm and `tend_share` cap at `body_ceiling` (or `condition_scale` where none is set); CP-T10-08's
  `individual` stem (CP-01); its rising `body.changed` carrying the body Observation (CP-02).
- **T04:** the export shape and one `engine_params` loader (CP-03, CP-05); Ask B for the winner's write; Ask B (d) reusing CP-09's
  custody route.
- **EC:** `craft` producing arms matter kinds (CP-03's producer).
- **MB:** none required; mapping `ARSENAL` from the same matter kinds is MB's option.
- **GV / SC:** `pardon` and `determine` over `detain` as built; H-209 (a witnessed killing becoming a seat's question); H-206; succession
  for null-conferral seats (OV §6 #11); J-8 (which seats grant `WARRANT_ACT`), which bounds CP-09.
- **FA:** ransom over a CP-09 `detain`.
- **NP:** `tend`, `train`, `forgive`, unchanged in owner; the cast overlay's authored `arms` values (CP-04).

**What this gives them:** a two-sided combat write (MB's symmetry question gets a person-scale answer to compare), captives (GV, FA,
T04), a body ceiling T10's healing reads, believed bodies (FI, T10), combat odds through T01's one function, REM-31's decider odds.

## §6 Jordan asks

**No new ask.** Carried, not re-asked: **JQ-2** (whether fighters may differ: CP-03, CP-04), **AQ-X1** (T01 §6: whether expected
success enters an NPC's score), **ED-IN-0296** (stance polarity: CP-06), **T04 Ask B** (what a won field writes on the winner). Each
candidate this file could have raised, answered:
- **Custody by a seatless captor** (L09 §3.9 item 2). (4) precedent: custody is "prisoner -> a seat" (ED-IN-0288, as intent) and the
  built opener from force of office, `arrest`, detains under the `warrant` basis; CP-09 follows it exactly.
- **A personal guard edge** (L09 §3.9 item 1). (1)/(4): B-V seats guards as cohorts obliged to a seat (`harness/populated.py:489-500`),
  read by IN-59; CP-11 is cut into it.
- **The felled attacker's death.** (5) architecture: CP-T03-00.
- **What a played person's death does.** (5) architecture (§1 gap K).
- **A gate basis for rescue.** Not raised: the N-line does not earn a Layer 1 amendment now (CP-10 parked).
- **Magnitudes** (mark trigger, kit ranks). (4) each ships behind a control arm with a named revert, on REM-52's precedent; kit ranks
  answer to JQ-2's "chance at winning".

**Rulings the items touch (none overwritten):** ED-IN-0261 (the three verbs); RS-25 (a duel need not be lethal: PC-10a, CP-09);
Jordan 2026-09-03 (degrees read off scene combat: CP-00, CP-07's trigger); ED-IN-0288 (custody to a seat: CP-09); H-38 and ED-PC-0055 /
J-20 (B) (body model, no hit location: CP-07); ED-PC-0056 (Yield declared before the scene: PC-10a); ED-IN-0279 (resolved for the loser
only, R7); ED-WR-0011 (closed cast, provisional: §7); D-2 (IN-46 builds).

## §7 Risks and what this deliberately does not do

- **Lethality against a closed cast.** CP-T03-00 roughly doubles combat deaths (33 of 59 realm calls fell the actor, T03 §5c, beside
  26 Felled subjects) in a cast that cannot grow (ED-WR-0011, "for now"), and no NPC reads its odds until AQ-X1 is answered. Duel terms
  (PC-10a), `capture` and IN-59's `with` pull the other way. **Measurement at CP-00's commit:** seeds 0-2, two seasons, deaths and acts
  per season; control: the pre-item tree on the same seeds. No number is predicted here.
- **Kit read, not consumed; kit by household.** One harness can arm a household's every fight; a settlement-resident commoner shares
  the town's stores [ASSUMPTION; medium]. Exclusive possession needs an allocation rule (TL P16) this file does not propose.
- **Belief inputs are thin.** Nothing deposits a `stores:<arms>` claim today, so mode (b) returns `None` for a rival's kit.
- **Not done:** looting, ransom (FA's), execution (R-1, Jordan's), escape (NP's), rescue (parked), ranged arms, the N-party scene, odds
  shown on a screen, a played person's heir, a person's choice at the moment of felling (REM-31), any guard or audit over this file.
- **`[UNVERIFIED]`:** L09's "1 of 63 cohort parties" at HEAD (CP-01); whether named persons' `reside` rungs are hearths or settlements
  (CP-03); whether `Rung.stores` is keyed on every matter kind (CP-03's hash); that WITNESS deposits a `(person, "body", v)`
  Observation by REM-51's mechanism unchanged (CP-02); that the gate's `warrant` clause keys the edge's object to `via` (CP-09); which
  seats grant `WARRANT_ACT` (CP-09); T10's rounding in `tend_share` (CP-07's 524). No `engine/season` module reads `engine/engine_params/`
  today (grep), so CP-03/CP-05's loader is the first, shared with T04's.
