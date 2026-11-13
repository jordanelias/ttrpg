# 22 · Happenings: do the things that happen in computed play make sense, and what repairs the ones that do not

## Status: REFERENCE (an audit; resolves nothing at runtime; proposals in `proposals/22_HAPPENINGS_*.md`)

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (L-18 to L-22) — §1.1's seed-2 run re-run and reproduced to the hash (`b4bae063…`: the King dies in the fourth season in the Spymaster's `capture`); `capture` ungated verified at `rosters.yaml:2772-2773`; §0 item 2 corrected: CR-87's roster gates `fight` alone, and `accept`'s gate is PC-10b's held challenge.

Jordan, 2026-11-12, on a digest line reading "the King dies at tick 0 in every seed, which empties seven
seats that can never be refilled": *"why would the King always die?? Anyway, I expect Fable to assess
whether these happenings actually make sense and seem reasonable, and then fix."*

Method (`PESSIMIST_BRIEF.md`): ordinary meaning first, then run. A happening is judged against what a
player of strategy and role-playing games, or a reader of the world, would expect from the words. Scratch
output: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/HAPPEN/`
(called `runs/HAPPEN/` below). Read at the working tree of 2026-11-12 (`54e6661` plus the suite's
uncommitted drafts).

## 0. Verdict

**The King does not die at the first tick any more, and he does not die at every seed. He does still
die, for the same reason as before, by the one verb the repair missed.**

1. *The digest line is stale.* It was measured on 2026-10-22 at commit `51d7b05`
   (`digests/DG_proposalsB4.md:100`, `:114`, `:258`, repeating the tutorials). Re-run at HEAD (§1.1): the
   King, `p_npc_020` Almud Almqvist, is alive after season 0 at seeds 0, 1 and 2.
2. *Why he died then* (§1.2): a person formed `fight` or `accept` against any living person his question
   named; the King is the person most questions name; a fight nearly always felled someone; and `accept`
   needed no challenge. So in the first season of every world somebody near him attacked him: the
   **Queen's `accept`** killed him at seeds 0 and 2 and the **Prince's `fight`** at seed 1. No quarrel, no
   war, no motive. Jordan ruled against it on 2026-11-05 (ED-IN-0337: fighting is rare in civil society
   and needs a context) and v11 CR-87 gated `fight` (`rosters.yaml:2770-2771` *[pointer corrected, U4 F-09: the `fight: [war, crime, duel, defence]` line is `:2771`]*, the one line of
   `violence_contexts`) and put `accept` under `blood` terms (`rosters.yaml:1000-1002`); `accept`'s own
   gate, a held `challenge` Record addressed to the actor, is v10 PC-10b's cell
   (`verb_table.yaml:956-972`).
3. *Why he dies now* (§1.3, new in this lane): CR-87 left `capture` ungated. At seed 2 the King is the
   target of **19 `capture` attempts in four seasons**: seven by his own Spymaster, ten by the Duke of
   Varfell, two by the Duchess of Hafenmark. Seventeen are refused in the fold. In the third season the
   Spymaster's attempt is fought and wounds him; in the fourth the Spymaster tries again and **the King
   is felled and dies**, his two seats close, and the run ends with no King. Both fought attempts cite,
   in their `causes[]`, an order the Grand Master of the Löwenritter had issued naming the King. The same
   verb kills the Cardinal of Prudence at seeds 1 and 2, as the captor. Across the nine `capture` scenes
   fought at seeds 1 and 2, **nobody is ever taken prisoner and three people die**.
4. *Otherwise nobody named can die at all* (§1.4): age and illness ship at 0 and everyone is zero seasons
   old; only cohorts hunger; `fight` never forms; all 48 challenges issued at seed 0 in one season are
   refused, and all 174 at seed 2 in four.

None of the three states is reasonable. A queen who kills the king in the first week of every world is
absurd; a spymaster who arrests his king to death because he saw a letter is absurd; and a realm in which
age, sickness and enmity kill no one is inert. **What it should be:** a ruler's death is rare in peace,
likelier with age, illness, want, a wound, a war or an enemy; it usually gives warning; it is never
certain; it has a cause a chronicle can name; and it opens a succession that can go more than one way.
§1.6 gives the repair link by link: six of twelve links are already carried by other suite proposals
(cited), and the other six are closed by three new ones (proposals A, B, C).

§2 applies the same test to 34 happenings the suite has measured. All 34 fail it; one ruling that looks
odd passes. Their common cause is one sentence: **the engine offers every act on every thing a person has heard of and decides
sense afterwards by refusing**, and what is not refused takes effect with certainty and changes little.
§3 groups the fixes into eight batches; §4 lists three choices that are Jordan's.

## 1. The King

### 1.1 Reproduction at HEAD

Probe: `runs/HAPPEN/king_probe.py <seed> <seasons>` (`PYTHONHASHSEED=0`; `populated.build_realm(seed)`, one
`SeasonDriver`, the shipped chooser, the body of `populated.run`; deaths read with
`harness/aperture.py::deaths_of`, the one reader of `person.died`).

| seed | seasons | King alive after season 0 | King at the end | deaths | seats held, start → end | content hash |
|---|---|---|---|---|---|---|
| 0 | 1 | yes | alive | 0 | 34 → 34 | `5ab73af2…` |
| 1 | 4 | yes | alive | 1 (third season: the Cardinal of Prudence, as captor) | 34 → 33 | `25d23448…` |
| 2 | 4 | yes | **dead, fourth season** | 2 (second season: the Cardinal of Prudence, as captor; fourth: the King) | 34 → 31 | `b4bae063…` |

That the runs happened (CLAUDE.md §0.1 pt 3): the logs grew to 13,379, 115,037 and 126,691 Events and
each verb census is non-empty. Seasons are counted from 0 in the table's "after season 0" and in the
JSON; "third season" means index 2.

Two other lanes read parts of this and are cited: WR addendum B F-WR-22 (*"seed 0 has no `person.died` in
six seasons, seed 1 one (season 3), seed 2 two (seasons 2 and 4)"*: the counts agree; it does not say the
second is the King) and the game pessimist's premise 2.1, which ran three seasons, saw no royal death,
**planted** one to study a succession, and wrote *"he can die … of nothing, shipped"*
(`audits/16_PESSIMIST_GAME.md:252`). One season more at seed 2 shows he can.

### 1.2 Why he died at `51d7b05` (cited at the line; not re-run: the clone is shallow and lacks that commit)

- seed 0: *"Tick 0, `p_npc_006` `fight`s the King … the King takes two wounds (health 18 of 40)"*, then
  *"`p_npc_032`, the Queen, `accept`s against the King, now at `end 2` … the King is Felled"*
  (`proposals/2026-10-22-system-description/…-04-t03-personal-combat.md:73-80`);
- seeds 1 and 2: *"the King also dies in season 0, to the Prince's `fight` (seed 1) and the Queen's
  `accept` (seed 2)"* (`…-10-t09-factions-war-diplomacy.md:109-111`).

Three causes:

1. **Violence formed on anyone a question named.** The tutorial's choice table: `fight` is picked when
   *"a living person is among his question's referents"*; `accept` *"reads no challenge"*; 0 of 39
   `accept`s followed a challenge. The row's one precondition was that the target exist.
2. **The King is the person most questions name.** Still true at HEAD (§1.3).
3. **A fight nearly always felled someone.** Fifteen combat calls in that first season: five Felled,
   four Wounded. F-PC-04 (a plain `fight` kills 200 of 200) is the same fact at HEAD.

ED-IN-0337 (read in `registers/`) closed cause 1 for `fight`; its own record lists *"the Spymaster against
the King"* among 13 fights in one season. The gate is `rosters.yaml: violence_contexts`
(`fight: [war, crime, duel, defence]`), read in `decision/options.py:216-224`.

### 1.3 Why he dies at HEAD, seed 2, fourth season (`runs/HAPPEN/king_2.json`)

The sequence, from the log:

| season | Event | what happened |
|---|---|---|
| 0 to 3 | 17 × `capture.refused` naming the King | the Spymaster (through `off_spymaster`) five times, the Duke of Varfell ten, the Duchess of Hafenmark two; refused in the fold. The deciding clause was not read per act; the PHYSICAL lane's census gives `with` (the captor is not where his target is) as the commonest. The King's row lives in a cottage in one town and the Spymaster's in a barracks in another (H-25) |
| 2 | `order.given` | the Grand Master of the Löwenritter `dispatch`es an order whose subject is the King |
| 2 | `capture.declared`, then `body.changed` (`Wounded`) | the Spymaster's sixth attempt is fought. The King is wounded. Its `causes[]` are the act and the Grand Master's order |
| 2 | `body.tended` | somebody restores the King's body whole |
| 3 | `capture.declared`, then `person.died` (`Felled`), `tenure.closed` on `off_king` and `off_duke_valorsmark` | the Spymaster's seventh attempt. Same two causes. The King is dead |

Why it can happen, at the owner:

1. **`capture` has no context.** `rosters.yaml: violence_contexts` lists `fight` alone; its note says the
   coercion rows *"keep their"* own gates, and `capture`'s gate is that the actor hold a seat granting
   `dispatch` (`verb_table.yaml`, row `capture`, `refusal_note`). Any such officer forms it on any person
   a question names. `aperture 2 0` (PHYSICAL lane): formed 26, attempted 12.
2. **The occasion is having seen something.** Both fought attempts carry the Grand Master's
   `order.given` in `causes[]`: an Event naming the King made the King a referent of the Spymaster's
   question, and `capture` is on the list of things to do about a referent. The narrative lane measured
   the general case: *"a third of all acts are occasioned by having seen someone do something"*.
3. **A capture is a fight, and this fight kills.** It is fought to the yield (`rosters.yaml: duel_terms`,
   `capture: yield`); the modal blow is Overwhelming and is a median 25 of 40 Health
   (`audits/16_PESSIMIST_PC.md` §0). At seeds 1 and 2: nine scenes fought (`capture.declared` 3 and 6),
   **`person.captured` 0**, `person.died` 3.
4. **Nothing follows the first attempt.** Between the wounding and the killing the Spymaster keeps his
   seat and his freedom. The King does not dismiss him (he could only through his second title,
   F-PES-FA-02, and `revoke` is never attempted in computed play), holds no grievance that changes his
   choices (F-PES-CHAR-08), and has no guard (`build_realm`'s `guards` default is `False`).

The cardinal: at seed 1 the Cardinal of Prudence dies trying to capture `p_npc_041`; at seed 2 he dies
trying to capture the Senior Inquisitor. Each time he is the one felled.

And the realm aims itself at the King in other ways, all refused. Seed 0, season 0, 27 refused acts by
others with the King as subject: the Royal Marshal tries to **train the King** in arms, copying and
arguing eight times and the Guard Captain five; the Princess tries to **tend** her unwounded father five
times; two men try to **sabotage the King** (payload `site: p_npc_020`: a person named as a building);
the Queen twice tries to **release** him; one man challenges him twice; the Spymaster tries to capture
him twice.

### 1.4 What cannot kill him

| route | owner | shipped | read (this lane) |
|---|---|---|---|
| age, illness | `queries/world_q.py:1248::body_hazard`, drawn in `loop/matter.py` | `age_step = 0.0`, `illness_rate = 0.0` (`data/fixtures.py:690-691`), deferred by Jordan as shipped values (ED-IN-0317 (c)); `age_at_build = 0` | the pass is skipped. The King's `Person.born` is 0: he is zero seasons old, as is everyone |
| hunger | `modules/settlements/subsist.py` | only a cohort eats (ED-IN-0255, ruled) | not a route for a named person, by ruling |
| a fight | `violence_contexts` | no context is ever met | `fight` resolved 0 at every seed and season run |
| a duel | `challenge`, `accept` | the challenged never holds the challenge | seed 0, one season: 48 issued, 48 refused. Seed 2, four seasons: 174 issued, 174 refused; `accept.refused` 81 |
| the field | `march`, ENCOUNTER | fields are unopposed or lost by the attacker | seed 2: `field.unopposed` 8, `field.lost` 3; no named person dies in one |
| a sentence | `determine` | no verdict carries a death | — |

### 1.5 Judgment, by ordinary sense

*Then.* A queen and a prince who kill the king in the first season of every world, for no stated reason,
are not a story. A Crusader Kings player expects regicide to be possible and expects a plot: a motive, a
rival claim, odds, a risk of discovery. Lenneth's own case (NPC-032) describes a consort *with standing
and no action economy of her own*.

*Now.* A spymaster who lays hands on his king seven times in a year, wounds him, is left in office, and
kills him on the next try has no reading at all: he holds no warrant, there is no war, and the two men
are of one faction. A cardinal who dies personally seizing an inquisitor, twice in three worlds, is the
same accident. And apart from this accident the cast is immortal, in a world whose own history turns on
a royal death (*the first king died in a hunting accident, perpetrator undefined*,
`audits/15_INSTITUTIONS_PAPACY.md:157`) and whose second house is *unmarried, childless, heirless*.

*What it should be.* Stated in §0. In numbers a player would accept: a king of fifty dies in a given
year about once in a few hundred worlds from natural causes, an old man several times in ten, and by
violence only when someone with a reason, an opening and the nerve tries, and then not always.

### 1.6 The repair, link by link, and who carries it

| # | link | what it should be | carried by (cited, not redone) | gap taken by this lane |
|---|---|---|---|---|
| 1 | seizing a person needs a cause | `capture` forms only in war or on a warrant; custody goes to the court | `14_VERBS_PHYSICAL_A_custody_and_force.md` A2 (`capture: [war, crime]`, `referent_class: Person`) | none in design. Its gate is read at two seasons and misses this; `22_HAPPENINGS_D` §2 asks for the four-season reading |
| 2 | a felling is not a death with certainty; a capture takes a prisoner | the mortal-wound draw; the yield as a draw | PHYSICAL_A A3; `16_PESSIMIST_PC_A_the_yield_is_a_draw.md`; sweep D-04, C-12 | none |
| 3 | violence for a cause | duel: the challenged hears and answers; war through a seat; enforcement on a warrant | `03_PC_duel_chain_reach.md`; PHYSICAL_A A1, A4; `06_FA_war_lives_in_seats_B.md`; CR-91 | none |
| 4 | a killing as a crime | the doer's side of the criminal context: a reason, hostility, a guard to pass, a draw at each step | none: the built `crime` context is the officer's side only | `22_HAPPENINGS_C` (design-first; §4 item 2) |
| 5 | an attack has consequences for the attacker | the attacked may answer; an officer who attacks his lord can be dismissed | `defence` exists as a context; `16_PESSIMIST_FA_A_dismissal_survives_the_king.md`; `02_CHAR_relations_have_a_ground.md` | none |
| 6 | a named person has an age | authored, read by the builder | `21_PROCEDURAL_B_cast_and_seats.md` (`age_bands`) for a generated cast; nothing for the 46 authored | `22_HAPPENINGS_A` edit 1 |
| 7 | natural death | a graded draw from age, the body's band, the season and want in the land; a first bad draw sickens and does not kill | `09_WR_world_motion.md` edit 4 (*"not decided here"*); `16_PESSIMIST_GAME_the_world_draws.md` excludes it by name | `22_HAPPENINGS_A` edits 2 to 5: the shape. The on-switch is Jordan's (§4 item 1) |
| 8 | the death has a cause on its Event; the realm hears | the larder, the bout, the blow; a seat-holder's death travels | `16_PESSIMIST_SE_A_…dead_are_accounted.md`; `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`; `08_FI_02_rumour-that-travels.md` | A's Events name their cause |
| 9 | the throne passes by a contest | `succeed` drawn; rivals may claim; a Partial reigns provisionally | `14_VERBS_BINDING_C_turnover.md`; `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` | none |
| 10 | the other seats pass | each has a basis | Valorsmark: PES-FA-A edit 1. Hafenmark: `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` edit 6. Altonia's two: `15_INSTITUTIONS_BYZANTINE_D`, `COLONIAL_B`. Guild leader: `06_FA_remit_grant_by_row.md` | the Queen's and the Princess's rows, `conferral: null` in every lane: `22_HAPPENINGS_B` edit 1 |
| 11 | the throne is never stranded | with King and heir dead someone can still be made King, by a draw among claimants ranked by deed | named and left open by F-PES-FA-11; the deed order is SYN-B's | `22_HAPPENINGS_B` edits 2 to 4 |
| 12 | an instrument over many seeds | deaths by cause and age, warning given, seat refilled and by whom | `harness/aperture.py`'s DEATH CENSUS (by killing verb and seats; pools seeds) | A edit 6: three columns on that census |

**The seven seats.** At `51d7b05` the seven with no basis were King, Duke of Valorsmark, Duchess of
Hafenmark, Queen, Heir, Princess, guild leader. At HEAD the King's is `inheritance` and the Heir's
`appointed` (v10 IN-61), and the seven are: Duke of Valorsmark, Duchess of Hafenmark, Queen, Princess,
the unrowed guild leader, and Altonia's two (`offices.yaml:206, 219, 245, 271, 614, 627`; F-PES-FA-01).
With rows 10 and 11 every one has a basis. At seed 2 the King's death left `off_king` claimable by the
Prince and `off_duke_valorsmark` fillable by nothing; the run ended that season, so no claim was read.

## 2. The happenings inventory

Ranked by how much of play each spoils. "Mine" marks a number read in this lane's runs (§6); every other
number is cited to the finding that measured it. Reasonable? is by ordinary sense. NEW marks a fix this
lane writes; every other fix is another suite proposal's and is not redone.

### 2.1 They spoil the whole game

| # | happening | evidence | reasonable? | cause (owner) | fix | carried by |
|---|---|---|---|---|---|---|
| H-01 | Officers seize people with no cause, take no prisoner, and kill: the King by his Spymaster; a Cardinal twice | §1.3 (mine): seeds 1, 2: 9 scenes fought, 0 custody, 3 dead; 71 refused | **No.** An arrest needs a charge, usually takes its man, and a king is not arrested by his own clerk | `capture` unlisted in `violence_contexts`; fought as a duel to the yield | context; mortal draw; yield draw | PHYSICAL_A A2, A3; PES-PC-A. Gate added: D §2 |
| H-02 | Nobody named dies of age, illness or enmity; everyone is zero seasons old | §1.4 (mine); F-WR-22; `21_PROCEDURAL_B` (`born` 0 for 83 of 83) | **No.** | `age_step`, `illness_rate` 0; `age_at_build` 0; no doer-side context | the bout; ages; `enmity` | **NEW** A, C; `21_PROCEDURAL_B` |
| H-03 | Four in ten acts are refused, the same ones every season | mine, seed 0 s0: 322 refusal Events on 749 acts; `challenge` 48 of 48, `train` 41 of 41, `sabotage` 18 of 18, `exchange` 15 of 15, `raze` 5 of 5, `covenant` 3 of 3. CHAR: 656 of 1,529 | **No.** People do not spend half their year attempting what cannot work | `decision/options.py::opening_set` offers a verb on any referent; nine per-verb decline rosters | one person-side decline read off the row | `02_CHAR_offer_what_can_be_done.md`; `16_PESSIMIST_CORE_a_refusal_is_remembered.md` |
| H-04 | People aim senseless acts at the King: train him, sabotage him as a building, tend him unwounded | §1.3 (mine): 27 in one season | **No.** | the same; a referent's kind is not asked (`site: p_npc_020`) | the same; `referent_class` per row | `02_CHAR_offer…`; `14_VERBS_MILITARY_B_train.md`; `01_CORE_predicates_name_their_clause.md` |
| H-05 | The world is the same whether anyone acts or not | F-PES-GAME-01: persons, seats, sites, stores after three played seasons equal the no-act world at seeds 0 to 2 | **No.** | effects land in ledgers and Records; nothing reads them back | the consequence ring | `16_PESSIMIST_GAME_consequence_reading.md` |
| H-06 | Nine acts in ten have a certain outcome | F-PES-GAME-04: 7.8 to 10.8% of attempted acts drawn; 50 of 67 verbs certain | **No** (standing rule) | `loop/resolve.py` folds with `resolution=None` | every writing row declares its draw | `18_DETERMINISM_task_draw_for_uncontested_verbs.md` and siblings |
| H-07 | No seat changes hands, no one changes side, no oath is paid, no writ is obeyed | narrative lane §0: 0 of 193 writs complied with; 123 petitions, 2 determined; no seat change at seeds 0 to 2 in four seasons | **No.** | `issue` binds nothing; `revoke` refused at clause 1; `confer` never attempted | decrees bind; seats turn over by draws | `06_FA_decree_binds.md`; `14_VERBS_BINDING_C`, `_D`; `20_NARRATIVE_A` to `_F` |
| H-08 | Everyone behaves alike: a man who holds only `love` puts `forge` first in 266 of 276 situations, as do men of `family`, `wealth`, `reputation` | F-PES-CHAR-01 | **No.** A name on a character should predict his acts | two tables whose product was never read against the names | say in data what each pursuit means in acts | `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md`; `02_CHAR_choice_alignment.md` |
| H-09 | The realm's main business is paperwork about itself | FI §0: 73.7% of acts are information verbs; mine, seed 0 s0: 12,115 of 13,379 Events are `claim.deposited` | **No.** Cut the information verbs and persons march, move and rule more (FI §1.1) | information verbs form on everything known | formation on what is known and needed | `14_VERBS_SOCIAL2_A_formation_on_what_is_known.md`; `08_FI_*` |
| H-10 | Villages forge documents and assume cover identities | F-PES-GAME-09: the 37 cohorts forge 34 and take 18 covers in three seasons; `migrate` refused every time | **No.** A strategy player does not expect a village to be a spy | a cohort is offered every individual's row | a declared aperture for a population | `02_CHAR_offer_what_can_be_done.md` |

### 2.2 They spoil a subsystem

| # | happening | evidence | reasonable? | cause (owner) | fix | carried by |
|---|---|---|---|---|---|---|
| H-11 | No duel is ever fought | mine: 48 of 48 and 174 of 174 challenges refused; `accept.refused` 17 and 81 | **No.** | the challenge Record stays in the challenger's hand; a challenge needs a recorded wrong nobody holds | the challenged hears and answers | `03_PC_duel_chain_reach.md`; PHYSICAL_A A4 |
| H-12 | A fight is two blows between identical men; a felling is always a death | PES-PC §0: 70% of deaths in two blows; 92.6% of duels one blow; F-PC-04: 200 of 200 | **No.** | exchange roll centred 2.2 above its obstacle; one loadout; default terms | length before levers; the mortal draw | `03_PC_duel_round_and_approach_B.md`; PHYSICAL_A A3; `18_DETERMINISM_no_certain_matchup.md` |
| H-13 | Anyone declares war for anyone; marches meet nobody; a defended field is lost by the attacker 60 of 60 | F-PES-FA-05; mine, seed 2: `field.unopposed` 8, `field.lost` 3; sweep C-06 | **No.** | `utter` of mood WAR has no precondition; army is who stands at home; `_weighted_unit` | a war has two parties and a declarer; one scale owner | `16_PESSIMIST_FA_B` edit 4; `06_FA_war_lives_in_seats_B.md`; `04_MB_headcount_grade_and_scale.md` |
| H-14 | Every town is the same town and every year the same year: a planted famine kills all 37 cohorts in the same season | F-PES-GAME-05; F-PES-GAME-04 (the built world identical at every seed) | **No.** | `subsist.py` and wear draw nothing; identical Sites per settlement | hunger and wear drawn; ground that differs | `16_PESSIMIST_GAME_the_world_draws.md`; `07_SE_ground_and_granaries.md`; `21_PROCEDURAL_A` |
| H-15 | A starving town changes nothing anyone does, and rest cures starvation | F-PES-SE-01; F-PES-GAME-06; mine, seed 0 s0: `tend` 47, `body.tended` 37 (the 37 cohorts) | **No.** | `tend` restores a body whole, free; nobody reads a shortfall | food mends hunger; `tend` drawn | PES-SE-A edit 4; `03_PC_exits_withdrawal_recovery.md` Part C |
| H-16 | A verdict reads nothing of the case, the bench or the proofs | PES-SC §0: `determine` deals 105 / 33 / 12 in all six cells | **No.** | the obstacle has one term | difficulty plus named modifiers | `05_SC_obstacle_difficulty_and_modifiers_B.md`; `13_SC_*`; `19_LACUNA_*` |
| H-17 | A lie is as easy to a man who knows the truth; nothing is ever caught | PES-SC §0: 0.74 Failure against knower and ignorant alike | **No.** | `lie`'s roll reads no knowledge | the hearer's knowledge is opposition | `14_VERBS_SOCIAL1_C_persuasion_and_deceit.md`; `05_SC_evidence_and_rebuttal_B.md` |
| H-18 | A hearing never ends; the winner receives nothing; the convict ends his own sentence | PES-SC §0 | **No.** | the bench may ask again without limit; disposal is a service to the judge's seat | a verdict ladder and reversal; acquittal | `19_LACUNA_verdict_ladder_and_reversal.md`; `05_SC_acquittal.md` |
| H-19 | A crisis of faith strikes the same six persons at every seed, silently, and converts them to the rival creed | F-PES-CHAR-03 | **No.** | `person_q.py:903`, *"ROLLS NOTHING"* | a drawn crisis that is told | `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` |
| H-20 | Everyone rolls two dice at everything; 77% of rolls fail; the top band never occurs | F-PES-CHAR-05; F-PES-DICE-02 | **No.** Nobody is good at anything | `pool_default`; one obstacle | capabilities; task difficulty | `02_CHAR_capability_definitions.md`; `10_DICE_*`; `03_PC_person_inputs_content.md` |
| H-21 | No crime is ever committed, so no case can begin; 52 forgeries never leave the forger's hand; no inquiry finds anything | FI §0; §1.4 (mine: `fight` 0) | **No** for a game whose fieldwork is a detective's | no doer-side context; `forge` writes and stops | a crime someone commits; case seeds; a paper that travels | **NEW** C; `21_PROCEDURAL_C_prologue_and_case_seeds.md`; `08_FI_07`; `14_VERBS_MATERIAL_D_paper.md` |
| H-22 | News does not travel: a king's death is known to 16 of 82, and to 17 three seasons on | F-PES-GAME-07; FI §2.1 (no rumour passes a second mouth) | **No.** | the second teller says only that he was told | a rumour that travels and garbles | `08_FI_02_rumour-that-travels.md`; `16_PESSIMIST_FI_A_what_a_rumour_can_garble.md` |
| H-23 | The King cannot dismiss anyone as King; a dismissal is permanent and unpardonable | F-PES-FA-02: 6 of 34 seats strippable, all through one seat; `pardon` refused through 33 of 33 | **No.** | the rung-directly-above rule over anchors placed two rungs apart | the anchors brought under the rule | `16_PESSIMIST_FA_A_dismissal_survives_the_king.md` |
| H-24 | The throne can be stranded for ever; a consort can seat herself as Confessor; a cohort can be King | F-PES-FA-01; premise 2.1 link 8 | **No.** | `successions` one title deep; `may_fill` unnarrowed | a set of claimants; a seat is held by an individual | **NEW** B; `16_PESSIMIST_FA_B` edits 1, 2 |
| H-25 | The King lives in a cottage in one town, the Queen at an inn in another, their children at court in a third; the Duke of Varfell at an inn; the Confessor in a market | mine (`npcs.yaml` rows NPC-020, -032, -031, -030, -052, -021; `king_0.out`); F-PES-FA-03: 18 of 34 seat-holders live off their seat's ground | **No.** A duchess at court is defensible; a king in a cottage apart from his queen is not | `npcs.yaml: home:`; the four heads with `institution: null` are the four so housed | governance no longer reads the home; the homes are content | `16_PESSIMIST_FA_C_under_the_seat.md`; the homes: **NEW**, D §3 |
| H-26 | The world never ends and never ends differently | WR audit: no ending in six seasons at seeds 0 to 2; `endings == []` every season | **No.** | `peninsular_sovereignty` unreachable; nothing concludes a strand | strand conclusion; readings of closure | `09_WR_strand_conclusion.md`; `09_WR_B_readings_of_closure_and_tension.md` |
| H-27 | A player-king who does nothing loses nothing | F-PES-GAME-10 | **No.** | no duty, no neglect, no cost of a vacancy | what he was owed; the ring | `20_NARRATIVE_B_what_he_was_owed.md`; `16_PESSIMIST_GAME_consequence_reading.md` |

### 2.3 They degrade what is otherwise sound

| # | happening | evidence | reasonable? | cause (owner) | fix | carried by |
|---|---|---|---|---|---|---|
| H-28 | A refused act is tried again at once: 4 of 309 retries succeed | CORE pessimist §2; F-PES-DICE-05 | **No.** | the retry licence, `driver.py:508-518` | a refusal is remembered | `16_PESSIMIST_CORE_a_refusal_is_remembered.md` |
| H-29 | A death by hunger is recorded as a death by nothing | F-PES-SE-04 | **No.** | `_die` cites only an earlier death | the death cites its fall | PES-SE-A edit 3 |
| H-30 | A shared granary feeds towns in id order and the unfed town is not reported | F-PES-SE-03 | **No.** | `kernel.py` K2 | the granary shares | PES-SE-A |
| H-31 | Armour does not turn a blade; a second garrison adds nothing and a new one halves the walls | PES-PC §0; F-PES-SE-08 | **No.** | armour is a constant multiplier; `fortification` averages | — | armour: the PC lane's order of fixes (`audits/16_PESSIMIST_PC.md` §6), no proposal identified here; walls: `16_PESSIMIST_SE_B` edit 3 |
| H-32 | Acts fire and write nothing: a challenge, an order, an argument; the degree of a roll changes no state in 282 of 284 | F-PES-DICE-01; PES-SC (five of seven contested rows write `[]`) | **No.** | band-keyed writes are empty | bands that write | `14_VERBS_BINDING_D_orders.md`; `14_VERBS_SOCIAL1_B`; `13_SC_draw_for_unrolled_contests.md` |
| H-33 | The record cannot retell: a fight of 110 trace events is three log lines; a succession does not cite the death | PES-PC §0; F-PES-GAME-03 | **No.** | standing occasions fold with `causes == [the act]` | occasions carry their cause; the record holds what changed | `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`; `16_PESSIMIST_CORE_the_record_holds_what_changed.md` |
| H-34 | A ruler's first reaction to being attacked is nothing | §1.3 (mine): between the wounding and the killing the Spymaster keeps his seat and tries again | **No.** | `defence` forms no act he chooses; regard does not move with the deed (F-PES-CHAR-08) | what is done to a man moves his regard | `02_CHAR_relations_have_a_ground.md`; `02_CHAR_which_ground_moves_whom.md` |

The one happening judged reasonable: only a population, never a named lord, goes hungry (ED-IN-0255).
It is a ruling and it reads as one: a duke does not starve in his hall. Proposal A leaves it standing
and lets want in the town raise the lord's chance of sickness.

### 2.4 The pattern

Twenty-eight of the thirty-four come down to three causes.

1. **Offer first, sense afterwards** (H-01, H-03, H-04, H-09, H-10, H-11, H-13, H-21, H-28). A candidate is
   formed for a verb on anything the person has heard of; whether the act means anything is decided at
   the fold, by refusal, and the refusal is not remembered. The old regicide, the present one and the
   Marshal training his King are one defect seen three times. Each earlier repair gated one verb
   (`fight`, then `accept`); the verb beside it (`capture`) then did the same thing.
2. **What is not refused is certain** (H-06, H-12, H-14, H-15, H-18, H-19, H-30). No draw, so no spread:
   every world is the same world.
3. **What happens is not read** (H-05, H-07, H-08, H-16, H-17, H-20, H-22, H-27, H-29, H-32, H-33,
   H-34). The effect lands in a ledger or a Record and no person's next choice depends on it.

The other six (H-02, H-23, H-24, H-25, H-26, H-31) are values, rows or arithmetic never authored against
the rule that reads them: rates left at 0, a roster one title deep, homes, an ending nothing can reach.

## 3. Batches a lane can land

Ordered by what stops the worst happenings first. Every batch is another lane's set of proposals plus,
where marked, one of this lane's. Detail, order within a batch and the added gates:
`proposals/22_HAPPENINGS_D_batches_and_added_gates.md`.

| batch | happenings | proposals | new here |
|---|---|---|---|
| **1 · violence has a cause and a mercy** | H-01, H-11, H-12, H-34 | PHYSICAL_A (A0 to A4); `03_PC_duel_chain_reach`; PES-PC-A; `18_DETERMINISM_no_certain_matchup` | the four-season gate (D §2) |
| **2 · offer what makes sense** | H-03, H-04, H-09, H-10, H-28 | `02_CHAR_offer_what_can_be_done`; the `14_VERBS_*_A_formation` files; PES-CORE (a refusal is remembered) | — |
| **3 · outcomes are drawn and written** | H-06, H-16, H-17, H-18, H-20, H-32 | `18_DETERMINISM_task_draw…`; `05_SC_obstacle…_B`; `13_SC_*`; `10_DICE_*`; `19_LACUNA_*` | — |
| **4 · seats pass** | H-07, H-23, H-24 | `06_FA_decree_binds`; VB-C; BYZ-E; PES-FA-A, -B, -C; `06_FA_seat_terms_*`; SYN-B edit 6 | **B** |
| **5 · bodies and time** | H-02, H-15, H-29, H-30 | PES-SE-A; `03_PC_exits…` Part C; `16_PESSIMIST_GAME_the_world_draws`; `21_PROCEDURAL_B` | **A** |
| **6 · crimes, cases and news** | H-21, H-22, H-33 | `08_FI_02`, `_06`, `_07`; PES-FI-A; `18_DETERMINISM_notice_is_a_draw`; `21_PROCEDURAL_C`; PES-GAME (occasions carry their cause) | **C** |
| **7 · persons differ and remember** | H-08, H-19, H-27 | PES-CHAR-A, -B, -C; `02_CHAR_*`; `20_NARRATIVE_*` | — |
| **8 · places differ and the world can end** | H-05, H-13, H-14, H-25, H-26, H-31 | `07_SE_ground_and_granaries`; PES-SE-B; `21_PROCEDURAL_A`; `04_MB_headcount_grade_and_scale`; `06_FA_war_lives_in_seats_B`; `09_WR_*`; PES-GAME (consequence reading) | the homes (D §3) |

Hash movers are declared in each proposal. This lane's: A edit 1 (`Person.born`, every world hash);
everything else in A and C is dark at its control; B moves only runs that contain a royal death.

## 4. For Jordan (three items; each survives the ladder because a ruled item or the world's shape is touched)

1. **Natural death ships on or stays off** (ED-IN-0317 (c) defers the values to you).
   (a) On, in A's shape, after the 46 ages are authored: about one to three natural deaths in a
   twelve-season campaign, almost all after a season of visible illness.
   (b) Off as now: named persons die by violence alone, and successions open only when someone is killed.
   Recommended: (a). A changes the shape either way and is dark until you set a rate.
2. **Whether a person may commit a killing** (ED-IN-0337 names *"criminal contexts"*; the code built the
   officer's side).
   (a) Yes, by C's `enmity` context: a reason and hostility, a guard to pass, a draw at each step, held
   to fewer than one attempt per seed-season by its gate.
   (b) No: violence stays to war, duel, enforcement and defence; murders exist only as seeded history
   and case seeds (`21_PROCEDURAL_C`).
   Recommended: (a). Under (b) the detective game investigates only what the world was built with.
3. **Who may claim the throne when the royal line fails** (your fixed point: king, then the first Duke
   of Hafenmark, then the first Duke of Varfell).
   (a) B's list: the heir, the consort, the Princess, and the heads of both houses may each claim; the
   deed order is odds, through the founders' seeded deeds.
   (b) The royal family only; a house takes the throne by conquest (`march`, `seize`) or not at all.
   Recommended: (a).

## 5. Corrections owed in files this lane does not edit

| file | line | correction |
|---|---|---|
| `digests/DG_proposalsB4.md` | `:100`, `:114`, `:258` | "King dies tick 0 in all seeds" is of `51d7b05`. At HEAD: alive after season 0 at seeds 0 to 2; dead at seed 2 in the fourth season by `capture` (this file §1) |
| `audits/16_PESSIMIST_GAME.md` | `:252` (premise 2.1 link 1) | *"he can die … of nothing, shipped"* holds for three seasons; at seed 2 the fourth season kills him. The lane's "two deaths … the same cardinal in a `capture`" stands for its horizon |
| `audits/09_WR_audit_addendum_B.md` | `:159-161` (F-WR-22) | seed 2's second death (its "season 4") is the King's; H-230's premise does occur at HEAD at that seed |
| `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` | Gate | add the four-season, seed-2 reading (D §2) |

## 6. Evidence log

All under `runs/HAPPEN/`, `PYTHONHASHSEED=0`.

| run | command | what it showed |
|---|---|---|
| K0 | `king_probe.py 0 1` → `king_0_s1.out`, `king_0_s1.json` | seed 0, one season (32 s): King alive; 0 deaths; 749 acts; 13,379 Events of which 12,115 `claim.deposited`; the 27 refused acts on the King; `challenge.refused` 48, `train.refused` 41, `accept.refused` 17 |
| K1 | `king_probe.py 1 4` → `king_1.out`, `king_1.json` | seed 1, four seasons (52, 125, 220, 382 s): King alive; one death, the Cardinal of Prudence as captor of `p_npc_041`; `capture.declared` 3, `capture.refused` 27; `challenge.refused` 180 |
| K2 | `king_probe.py 2 4` → `king_2.out`, `king_2.json` | seed 2, four seasons: the Cardinal dies as captor of `p_npc_004` (index 26,672); the King wounded by the Spymaster's `capture` (63,100), tended (67,336), felled (111,995); `tenure.closed` on `off_king`, `off_duke_valorsmark` (111,996); `capture.declared` 6, `capture.refused` 44, `person.captured` 0. `king_events` in the JSON is capped at 400 of 416, so the 19 attempts on the King are a lower bound |
| B1, B2 | `bout_calc.py`, `bout_calc2.py` → `.out` | design arithmetic for proposal A (exact band odds from `dice_engine`; simulated lives). Not engine runs |
| cited | `proposals/2026-10-22-system-description/` files 04, 10, 13 | the `51d7b05` regicide; opened at the lines quoted in §1.2 |

Not done: no run past four seasons; no seed above 2; the season-0 `capture` refusals' deciding clause
was not read per act (PHYSICAL lane: `with` 7, `exists:Person` 3, `individual` 2 of 12); the Event at
63,100 carries a `Tenure.since` receipt naming the King whose meaning (a custody opened, or not) was not
resolved; H-05 to H-33 are cited, not re-run.
