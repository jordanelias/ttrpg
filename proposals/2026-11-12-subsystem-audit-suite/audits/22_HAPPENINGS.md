# 22 · Happenings: do the things that happen in computed play make sense, and what repairs the ones that do not

## Status: AUDIT (a terminal pass; proposals in `proposals/22_HAPPENINGS_*.md`; not canon; resolves nothing at runtime, CLAUDE.md §0.05)

Jordan, 2026-11-12, on a digest line reading "the King dies at tick 0 in every seed, which empties seven
seats that can never be refilled": *"why would the King always die?? Anyway, I expect Fable to assess
whether these happenings actually make sense and seem reasonable, and then fix."*

Method (`PESSIMIST_BRIEF.md`): ordinary meaning first, then run. A happening is judged against what a
player of strategy and role-playing games, or a reader of the world, would expect from the words. Scratch
output: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/HAPPEN/`.

## 0. Verdict

**The King does not die at the first tick any more. The digest line is true of an old tree and false of
this one.** It was measured on 2026-10-22 at commit `51d7b05`; the digest (`digests/DG_proposalsB4.md:100`,
`:114`, `:258`) repeats it without a re-run. Re-run at HEAD (§1.1): at seed 0 the King, `p_npc_020` Almud
Almqvist, is alive after season 0, nobody in the realm dies, and all 34 seats are still held.

**Why he died then** (§1.2): at `51d7b05` a person formed `fight` or `accept` against **any living person
his question named**; the King is the person most questions name; a fight then ended with somebody felled in
most calls; and `accept` needed no challenge. So in the first season, at every seed, somebody near him
attacked him: at seed 0 `p_npc_006` wounded him and then **the Queen's `accept` killed him**; at seed 1 **the
Prince's `fight`** killed him; at seed 2 the Queen's `accept` again. No motive, no quarrel, no war. That was
a formation defect, and v11 CR-87 (`rosters.yaml: violence_contexts`, ED-IN-0337) closed it: violence now
needs a context (war, crime, duel, defence).

**What is true now is the opposite failure, and it is no more reasonable** (§1.3): at HEAD the King cannot
die of anything in shipped play. Age and illness hazards ship at 0, nobody starves but a cohort, `fight`
never forms, and every one of the 48 challenges issued at seed 0 in one season is refused. A realm where
the royal family murders the King in the first season is absurd; a realm where no named person can die is
inert. The repair (§1.5, proposal `22_HAPPENINGS_A_*`) makes a ruler's death what it is in the world: rare,
caused, graded, drawn, and followed by a succession that can go more than one way.

The rest of this file is the same test applied to everything else the suite has measured (§2), ranked by
how much of play each spoils, with the fix and who carries it.

## 1. The King

### 1.1 Reproduction at HEAD: he lives

Probe: `runs/HAPPEN/king_probe.py <seed> <seasons>` (`PYTHONHASHSEED=0`; `populated.build_realm(seed)`, one
`SeasonDriver`, the shipped chooser; deaths read with `harness/aperture.py::deaths_of`, the one reader of
`person.died`). Outputs `king_<seed>.out`, `king_<seed>.json`, `king_0_s1.*`.

| seed | seasons run | King alive after season 0 | King alive at the end | deaths in the run | seats held, start → end |
|---|---|---|---|---|---|
| 0 | 1 | yes | yes | 0 | 34 → 34 |
| 1 | 4 | yes | see §1.6 | see §1.6 | see §1.6 |
| 2 | 4 | yes | see §1.6 | see §1.6 | see §1.6 |

Seed 0, season 0: 749 resolved acts, 13,379 Events, no `person.died`, content hash `5ab73af2…`. The
check that the run happened (CLAUDE.md §0.1 pt 3): the log grew 0 → 13,379 and the verb census is
non-empty. Two other lanes read the same at longer horizons and are cited, not redone: WR addendum B
F-WR-22 (*"at HEAD, seed 0 has no `person.died` in six seasons, seed 1 one (season 3), seed 2 two"*) and
the game pessimist's premise 2.1, which had to **plant** the King's death to study a succession
(`audits/16_PESSIMIST_GAME.md:244-248`).

So the digest's sentence fails its own falsifier. It is a correct report of a document
(`proposals/2026-10-22-system-description/…-13-errata-and-audit-record.md:350`) and an incorrect report of
the game.

### 1.2 Why he died at `51d7b05` (cited, not re-run: the clone is shallow and does not hold that commit)

Opened at the line, the 2026-10-22 tutorials say what killed him:

- seed 0: *"Tick 0, `p_npc_006` `fight`s the King … the King takes two wounds (health 18 of 40) … body
  becomes 450"*, then *"`p_npc_032`, the Queen, `accept`s against the King, now at `end 2` … the King is
  Felled"* (`…-04-t03-personal-combat.md:73-80`);
- seeds 1 and 2: *"the King also dies in season 0, to the Prince's `fight` (seed 1) and the Queen's
  `accept` (seed 2)"* (`…-10-t09-factions-war-diplomacy.md:109-111`).

Three causes, each a line of that tree:

1. **Violence formed on anyone a question named.** The same tutorial's choice table: `fight` is picked
   when *"a living person is among his question's referents"*; `accept` *"reads no challenge … no
   challenge is needed"*; 0 of 39 `accept`s followed a challenge. The row's only precondition was that
   the target exist.
2. **The King is the person most questions name.** Still true at HEAD: in one season at seed 0, 107
   Events touch him, and other persons aim 27 acts at him that the fold refuses (§1.3).
3. **A fight nearly always felled someone.** Fifteen combat calls in that first season: five Felled,
   four Wounded. The PC lane's F-PC-04 (a plain `fight` kills 200 of 200) is the same fact at HEAD.

Jordan closed cause 1 himself on 2026-11-05 (ED-IN-0337, read in `registers/`): *"fighting is actually
really rare in civil society, no?"* The ruling's own record lists *"the Spymaster against the King"* among
13 fights in one season. v11 CR-87 built it: `rosters.yaml: violence_contexts`, read in
`decision/options.py::opening_set` (`:216-224`). `accept` now needs a challenge Record.

### 1.3 What is true now: nothing can kill him

Every route to a named person's death at HEAD, with its owner and what ships:

| route | owner | shipped | read at seed 0, season 0 (this lane) |
|---|---|---|---|
| age, illness | `queries/world_q.py::body_hazard`; drawn in `loop/matter.py` (the bodies pass) | `age_step = 0.0`, `illness_rate = 0.0` (`data/fixtures.py:690-691`), deferred by Jordan as shipped values (ED-IN-0317 (c)); `age_at_build = 0` | the pass is skipped. The King's `Person.born` is 0: **he is zero seasons old**, as is everyone |
| hunger | `modules/settlements/subsist.py`, `_die` | only a cohort eats (ED-IN-0255, ruled) | not a route for a named person, by ruling |
| a fight | `violence_contexts` (`war`, `crime`, `duel`, `defence`) | no war is declared by a seat, no warrant is addressed, no challenge is accepted | `fight` resolved 0 |
| a duel | `challenge` then `accept` | the challenge is held by the challenger; the challenged never forms `accept` on it | `challenge` 48 issued, **48 refused**; `accept` 17 formed, **17 refused** |
| capture | `capture` | forms on a person under no context | 5 refused, two of them **the King's own Spymaster trying to capture the King** through `off_spymaster` |
| the field | `march`, ENCOUNTER | fields are unopposed | `field.unopposed` 3; no named person fights |
| a sentence | `determine` | no verdict carries a death | `determine.refused` 1 |

The realm still aims itself at the King, harmlessly and oddly. In that one season, refused by the fold:
the Royal Marshal tries to **train the King** in arms, copying and arguing eight times and the Guard
Captain five; the Princess tries to **tend** her unwounded father five times; two men try to
**sabotage the King** (payload `site: p_npc_020`: a person named as a building); the Queen twice tries to
**release** him; a Jarl's man challenges him twice. This is cause 2 of §1.2 without cause 1: formation that
does not ask what the verb means for its target. CR-87 repaired one verb. The general repair is on file
(`proposals/02_CHAR_offer_what_can_be_done.md`) and is not redone here.

### 1.4 Judgment, by ordinary sense

*Then.* A queen and a prince who kill the king in the first season, at every seed, for no stated reason,
are not a story: there is no quarrel before, no concealment, no trial after, and the same hands do it in
every world. A player of Crusader Kings expects regicide to be possible and expects it to be a plot: a
motive, a rival claim, odds, a risk of discovery. A reader of this world expects less still: Lenneth's own
case (NPC-032) describes a consort *with standing and no action economy of her own*.

*Now.* A realm with famine, old cardinals, armed factions and no funeral in six seasons is equally not a
story. The world's own backstory contains the event the engine cannot produce: the first king *died in a
hunting accident, perpetrator undefined* (`audits/15_INSTITUTIONS_PAPACY.md:157`). Hafenmark's arc is a
duchess *unmarried, childless, heirless*: that arc is about a death that must be able to come.

*What it should be.* A ruler's death is rare in peace (a few chances in a thousand per season for a man in
his prime), likelier with age, illness, hunger in the land, a wound, a war or a plot; it usually gives
warning (he sickens, he is wounded, he is threatened) and that warning is itself news that others act on;
it is never certain and never scheduled; and when it comes it has a named cause that a chronicle can
state. Then the succession is a contest that can be won, delayed or lost.

### 1.5 The repair, link by link, and who carries it

| # | link | what it should be | carried by (cited, not redone) | gap taken by this lane |
|---|---|---|---|---|
| 1 | a named person has an age | authored, read by the builder | none. WR's research file (T-WR-8) notes no source authors one; `09_WR_world_motion.md` edit 4 says *"`age_at_build` authored first"* and stops | `22_HAPPENINGS_A` edit 1 |
| 2 | natural death | a graded draw whose odds come from age, the body's band, the season and want in the land; a first bad draw sickens, it does not kill | `09_WR_world_motion.md` edit 4 (*"not decided here"*: one value, Jordan's); `16_PESSIMIST_GAME_the_world_draws.md` excludes it by name | `22_HAPPENINGS_A` edits 2 to 5: the **shape**. The on-switch stays Jordan's (§4) |
| 3 | a felling is not a death with certainty | the mortal-wound draw | `14_VERBS_PHYSICAL_A_custody_and_force.md` A3; sweep D-04, C-12 | none. A asks that A3 and the bout read one `(pool, obstacle)` owner |
| 4 | violence forms for a cause | duel: the challenged hears and answers; war: declared through a seat; enforcement: a warrant | `03_PC_duel_chain_reach.md`, PHYSICAL_A A1, A2, A4; `06_FA_war_lives_in_seats_B.md`; CR-91 | none |
| 5 | a killing as a crime | the commission of a crime (a murder, an attempt on a ruler) is a context of violence with a motive read from state, guarded against, noticed by a draw | none: the `crime` reader is the constable's side only (a warrant addressed to the actor, or a detainee) | `22_HAPPENINGS_C` (design-first; §4 gives Jordan the two readings) |
| 6 | the death has a cause on its Event | the larder, the bout, the blow | `16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted.md` (hunger); `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md` | A's Events name their cause from the start |
| 7 | the realm hears | a seat-holder's death travels | `08_FI_02_rumour-that-travels.md` (and F-PES-GAME-07's added gate) | none |
| 8 | the throne passes by a contest | `succeed` drawn; rivals may claim; a Partial reigns provisionally | `14_VERBS_BINDING_C_turnover.md`; `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` (who may claim; the deed presumption as odds) | none |
| 9 | the other seats pass | each seat has a basis | Valorsmark: `16_PESSIMIST_FA_A_dismissal_survives_the_king.md` edit 1. Hafenmark: `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` edit 6 (`15_INSTITUTIONS_COLONIAL_D` edit 4). Altonia's two: `15_INSTITUTIONS_BYZANTINE_D`, `COLONIAL_B`. The guild leader: `06_FA_remit_grant_by_row.md` | the Queen's and the Princess's rows, still `conferral: null` in every lane: `22_HAPPENINGS_B` edit 1 |
| 10 | the throne is never stranded | with King and heir both dead somebody can still be made King | named and left open by F-PES-FA-11 | `22_HAPPENINGS_B` edits 2, 3 |
| 11 | seats end otherwise than by death | terms where a body rotates | `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md` | none |
| 12 | an instrument over many seeds | deaths by cause and age, warning given, seat refilled and by whom | `harness/aperture.py`'s DEATH CENSUS (by killing verb and seats) exists and pools seeds | A's gate adds the cause, the warning and the refill columns to that census |

**The seven seats.** At `51d7b05` the seven with no basis were King, Duke of Valorsmark, Duchess of
Hafenmark, Queen, Heir, Princess, guild leader. At HEAD the King's is `inheritance` and the Heir's
`appointed` (v10 IN-61), and the seven are: Duke of Valorsmark, Duchess of Hafenmark, Queen, Princess,
the unrowed guild leader, and Altonia's two (`offices.yaml:206, 219, 245, 271, 614, 627`;
F-PES-FA-01). With row 9 every one has a basis.

### 1.6 The longer runs (appended when they finish)

*(pending at the time of writing; see `king_1.out`, `king_2.out`)*

