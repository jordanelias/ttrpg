# WR-30-A — the era is a named period: who rules, and whether the realm is whole and fed; how it ends, and what the next one is called

## Status: PROPOSED (it rewords three sentences of the ratified strife master, `ED-IN-0316`; listed for Jordan in `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §11, J-30-1; nothing here is applied)

Source: `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` F-30-01, F-30-02, F-30-03. Jordan, 2026-11-12: *"work to improve era endings (like death of monarch, change of rule, civil war breaks out, etc)"*; *eras, regimes and strife are three distinct things* (`AUDIT_BRIEF.md`, last sections). Reference only (`CLAUDE.md` §0.05). Lane WR; the owner file is IN's (`engine/season/queries/world_q.py`).

Composes on, and restates none of: `09_WR_strand_conclusion.md` (an opening move is never terminal; the bounded same-doer link, A-45; the A-46 move), `22_HAPPENINGS_A` and `16_PESSIMIST_WR_C` (a death is rare, caused and drawn; illness on the body ladder; A-15), `22_HAPPENINGS_B` and `14_VERBS_BINDING_C` (the deed race for a vacant seat, A-19; `succeed` a draw; Partial a provisional hold), `15_INSTITUTIONS_SYNTHESIS_B` (the deed ledger that sets a claimant's odds), `06_FA_war_lives_in_seats_B` (A-20), `U5d_FA_land_and_seats_pass_on_a_won_march.md` (A-57 to A-70), `09_WR_B_weather_with_memory_and_the_year.md` (A-54), `23_STORY_B_a_house_continues.md` (A-75; minority), `20_NARRATIVE_C_who_holds_what.md` (`held_by`), `20_NARRATIVE_E` edit 1 (the year), `12_ARCS_arcs_as_staged_goals.md` (the `mandatory` mark, A-47), plan positions CR-97, CR-100, CR-104.

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | `world_q.Era` gains four fields and `_eras` cuts an era at a change of rule; a new world reading `era_turns`. No step of the loop reads either (`world_q.py:4749-4752`) | EQUAL |
| 2 | a person-side reading `person_q.era_known(p, head_seats)`; read by the player surface (`30_GO_F`) and the harness only | EQUAL |
| 3 | `questions_for` marks the `vacancies` stamp `mandatory` for a person who may claim a vacant head seat (A-47) | **declared mover** in any season with a vacant head seat (none at build: no seat is vacant) |
| 4 | the realm conditions other than `troubled` are read as their emitters land; each is a reading | EQUAL |

No era is stored, no counter is kept, no Event kind is added, and the era fires nothing (T-a, T-b; `ED-IN-0225`; `ED-IN-0352`).

## The problem, with evidence

- `world_q.Era` is `(id, moves, strands, concluded)` (`world_q.py:4929-4935`). It opens on the first strife move under the realm and concludes on a terminal move placed at the realm rung with no open referent (`_eras`, `:5233-5252`). It has no ruler, no kind, no cause of ending and no successor.
- Read: seed 0, two seasons, `PYTHONHASHSEED=0`, `python -m engine.season.harness.strife 2 0 --strands`: `3 strands, 1 era(s)`; the era `OPEN`, 38 moves, opening kinds `march.declared, petition.filed` (audit §12, P-1). The WR and NARRATIVE lanes read one open era at four and at six seasons (`audits/20_NARRATIVE_CHURN.md` W3). No run in the suite shows an era conclude.
- One season at seed 0 holds none of the Events an era turn would be read from: `person.died` 0, `tenure.closed` 0, `tenure.opened` 0, `succession.claimed` 0, `rung.seized` 0, `field.won` 0 (audit §12, P-2).
- A ruler's death is a `joins` kind (`rosters.yaml:3390`), opens a strand only when caused by `fight` or `accept` (`world_q.py:4782`), and by natural causes cannot occur (`data/fixtures.py:690-691`). The route check prints `NO ROUTE … -> DN` for all 13 opening kinds (P-1).
- The charge names endings the scope cannot express: under "first strife move opens, last terminal closes", *a civil war breaking out* opens or joins an era and can never end one.

## The resolution, decided

**An era is the span during which two facts about the realm stand unchanged: who rules it, and whether it is troubled.** It is a reading of the log (recomputed, never stored). There is always exactly one.

1. **RULE**: the live `hold` on the realm's head seat, where the head seat is `rosters.yaml: factions.head_seat` of the faction that `governing_hold(w, realm)` coheres under (`faction_q.head`'s own derivation, CR-86; no id is named). Its standing is one of a closed roster: `held`, `vacant`, `minority` (the holder is under `majority_age`; `23_STORY_B`), `captive` (the holder is under a live `detain`; A-23).
2. **CONDITION**: the set of realm conditions standing. Until the emitters of commit 4 land there is one, `troubled`: an open strand read at the realm rung that holds an opening other than a content opener (a field, a seizure, a razing, an arrest, a requisition, compliance withheld, a damaged site, a challenger's or an outsider's march, a killing: `OPENS_KINDS` and the side-aware openers, `world_q.py:4768-4817`), until that strand concludes (`_concluded`, the open-referent test). Two petitions on one matter are a movement and a strand (`strife-01` ruling 4); they are of the era and do not make it troubled. This narrows today's scope, which opens on any strife move under the realm: in this lane's run two of the three realm-rung strands are petitions only (audit §12, P-1), and a realm is not at odds with itself because two men petitioned. `[ASSUMPTION; medium; Jordan to correct; revert: any strife move under the realm, today's rule]`. When every row of commit 4 has landed, `troubled` is retired and the named conditions stand alone.

**The turn rule** (ladder step 4: it is `_eras`' own rule, kept, plus R11):
- a change of RULE always ends the era;
- a condition **opening** ends the era only when none stood (a quiet reign ends when the first trouble breaks: "civil war breaks out"). A further condition opening while one stands is *of the era* and does not end it (R11: simultaneous crises are one era);
- a condition **closing** ends the era only when it was the last standing ("a peace", "a famine's end").

So eras alternate and nest in the ordinary way: *the reign of Almud, in peace*; *the reign of Almud, troubled* (named by its conditions in the order they opened); *the vacancy*; *the minority of his son*. Nothing here is a count crossing: every turn is one logged Event, and that Event came from a draw (table below). The era reading itself is bookkeeping over those Events, which the standing rule permits.

**The successor is named from the turn.** `Era.opened_by` is the turn Event; its causing act and strife code (`harness/strife.py::move_codes`: DN died, KL killed, XE executed, IN installed, WA or WR a field, XS settled, CO conceded, XN a regime or border changed) say what happened; `Era.rule` and `Era.conditions` say what now stands. The rendered name is `30_GO_F`'s (a table of templates, data); the engine holds only the tuple.

### How an era ends: the turn, the draw behind it, and what follows

Each row: the Event the reading turns on (structural test, no id named) · the draw that produced it and its single owner · the readings that set its odds · the four bands · the era that follows · today.

| ending | turn Event | the draw, and its owner | odds read from | bands (Overwhelming / Success / Partial / Failure, from the ruler's or actor's side) | successor | today |
|---|---|---|---|---|---|---|
| the monarch dies in his bed | `tenure.closed` naming the head seat (`Subject.seat` receipt, `harness/arc.py` docstring), no causing act | MATTER's body draw per person per season (`world_q.death_chance`, `:1253-1270`; rewritten as a graded illness by `16_PESSIMIST_WR_C`, `22_HAPPENINGS_A`; A-15) | age, body, the season's hardship, tending | recovers / holds / sickens a band (a visible warning, and the foreshadowing `30_GO_F` shows) / dies | `vacant`, or `held` at once if a claim lands the same round; opened by DN | cannot occur: both rates 0 |
| the monarch is killed | the same Event, caused by `fight`, `accept` or `capture` | the personal-combat seam; the murder attempt of A-16 (`22_HAPPENINGS_C`) | the killer's grievance and hatred, the guard (reaching him is a draw), the fight | A-16's: unseen kill / kill and seen / wounded and caught / caught before the blow | `vacant`, opened by KL (or XE if he was held); a strand opens on the death (`OPENING_DEATH_VERBS`) | occurs only by `capture` at seed 2, season 4 (`audits/22_HAPPENINGS.md` §1.3) |
| the monarch is taken | `arrest.made` whose `detain` edge's subject is the holder | `arrest` or `capture` (contested) | the taker's force and warrant, the holder's guard | taken / taken with blood / escapes wounded / repelled, and the attempt is a deed against the taker | `captive`: his seat forms no act (A-23); who acts for him is whoever claims a regency (`23_STORY_B` edit 4) | no live `detain` observed in default play (`strife-00` §9) |
| he abdicates, or the head of a creed resigns | `tenure.closed` on the head seat caused by the holder's own `release` | `release` as a drawn act (`14_VERBS_BINDING_C`; A-24's D-31; A-46 makes it a strife move) | his own opinion of his side, his regard for the heir, the seat's hold on him | leaves and names his heir / leaves / leaves contested / is held to the seat (and seen to have tried) | `vacant` or `held`; the Split joins a strand | `release` of a head seat: 0 observed |
| he is deposed | `tenure.closed` on the head seat caused by another's act | `revoke` by one who may (A-35: a head strips an officer, resistibly); for the realm's own head, nobody may by office (A-36 for the Confessor), so the route is force or a rival's installation | the stripper's standing, the officer's resistance | stripped and barred / stripped / stripped and disputed (a provisional hold on both sides) / withstood | `vacant` or `contested` | `revoke` 0 of 11 (`audits/23` S-10) |
| a change of rule: a successor is installed | `tenure.opened` on the head seat | `succeed`, a draw per claimant (`14_VERBS_BINDING_C`), within the deed race (A-19; `22_HAPPENINGS_B`) | what each estimator holds of the claimant's deeds and his predecessors' (`person_q.legitimacy` with the chain term, `15_INSTITUTIONS_SYNTHESIS_B`), his title, living rivals | acclaimed / installed / a provisional hold (the claim stands and so does a rival's) / refused, and the refusal is remembered | `held`; if a second claim stands, `troubled` by `contested`. Opened by IN | `succeed` never forms (S-04) |
| the line fails and a house takes the crown | the same, the new holder of another line | the same race, the founding order a head start and never a right (A-19) | the deed ledger | as above | `held`, a change of dynasty the name states | impossible: `successions` one title deep |
| a minor comes of age | none of his own: majority is a tick (bookkeeping). The tick **opens a mandatory scene** for the regent and the heir (A-47) | the regent's `release` or refusal, the heir's `succeed` | the regent's opinion of the heir, what he would lose | yields with honour / yields / yields late and contested / holds on, which is a usurpation others may answer | `held`, or `troubled` by `contested` | no ages, no births |
| a civil war breaks out | the first live war between two factions that both hold under the realm: a `commitment.made` to a WAR Proposition by a seat that may muster (A-20); or a march into held land read as aggression (A-68) | the waging seat's `utter` and `commit`; the trespass draw of A-68 (`U5d_FA_land_and_seats_pass_on_a_won_march.md`) | A-68's: the holder's regard for the entrant, grievances between them, whether a realm bench is working (A-76). Pairwise state, not a flow (audit §11, J-30-2) | tolerated / resented (regard falls) / a provocation (a claim or grievance others may march on, A-74) / war | the quiet reign ends; `troubled` by `civil_war` | no WAR Proposition is ever uttered (`world_q.at_war` docstring) |
| a foreign war | the same with a faction of `rosters.yaml: foreign_factions` | the same; a foreign march needs a claim (`ED-IN-0317`) | the same, with side O | the same | `troubled` by `foreign_war` | O marches occur; no war is declared |
| a conquest | `rung.seized` on a rung one step below the realm, by a faction that does not cohere under the head | the field's end state (A-3), then the victor's own choice to seize, occupy or withdraw (A-57, A-58, A-66) | the field's named draws (A-59); the victor's goals | won and seized (seats pass) / won and occupied / drawn (both home, A-67, A-70) / lost | `troubled` by `occupation` or `conquest`; if the head seat's own faction is displaced, a change of RULE | 0 `field.won` in any run (S-21) |
| a schism | a `commitment.ended` or `tenure.closed` whose object is a faction's creed or head seat (A-46), by the holder of a seat whose institution covers the realm (`faction_q.influence_rung`, CR-104) | his `release` (drawn), then a rival head `establish`ed or a creed `commit`ted to | his opinion of his own side (`20_NARRATIVE_D`), credit across the fault line (`20_NARRATIVE_A`) | reconciled / leaves quietly / leaves and is followed / is stripped first (A-35) | `troubled` by `schism` | 0 commits opened or closed in play |
| a famine ends | the year's draw at the realm rung leaving its worst band (`09_WR_B` edit 2's spell, A-54), or the last `shortfall` under the realm clearing | the world's drawn year; relief by `transfer`, `requisition`, `exchange` | the place's endurance and the steward's skill against the season's hardship | plenty / enough / lean again / dearth | the condition `dearth` closes; if it was the last, the troubled era ends | the weather arm ships `()` |
| a peace | the last live war commit by a waging seat closes: by `release`, by a `covenant` whose terms end it, by surrender, by the last waging seat's death (A-20) | `covenant` (`13_SC_draw_for_unrolled_contests.md`), `release`, the field | each party's exhaustion (stores, men, A-69, A-78), regard, what is held | terms kept by both / terms / a truce (a term on the covenant) / talks fail, and the failure is a deed | the troubled era ends if nothing else stands; opened by XS or CO | `covenant` 0 of 47 (S-18) |
| an occupation ends | the occupier's presence leaves a rung it does not hold | his withdrawal, a later seizure, a treaty or a counter-march (A-66) | the same as a peace | as a peace | as a peace | not built |
| the troubles settle (today's rule, kept) | a terminal move at the realm rung leaving no open referent (`_eras`) | whatever act closed the last restraint, docket or war | the closing act's | the closing act's | the troubled era ends | never observed |

**A campaign ending is not an era ending.** `rosters.yaml: endings` and `world_q.endings_reached` (`:2619`) say when a campaign is over (A-49's reveal follows it). An ending row reached is read on top of the era and changes nothing here.

**What an era changes in what people want.** Nothing writes a goal (`strife-00` §5: "flows never write a faction's goal rows"). An era's conditions are standing occasions that existing stamps already carry; the era decides which are on the table, and each person's own pursuits and convictions decide what he does with them:

| the era's fact | the stamp that carries it (owner) | acts that form on it |
|---|---|---|
| `vacant` | `world_q.vacancies` (`:3121`); mandatory for one who may claim (commit 3) | `succeed`, `commit` to a claimant, `oblige`, `argue` |
| `captive` | `detainees_held` (`:3602`) for the holders; `flow_stakes` for the rest | `pardon`, `petition`, `march`, `covenant` |
| a war | `at_war` through CP-T09-02's enemy targets; `flow_stakes` | `march`, `recruit`, `covenant`, `commit`, `migrate` |
| `schism` | `propositions_heard` (CR-28); the own-side creed (`20_NARRATIVE_D`) | `argue`, `commit`, `release` |
| `dearth` | `larders_in_purview`; the cohort moves of A-56 | `transfer`, `requisition`, `petition`, `migrate`, `riot` |

**Order of attention.** Among within-stakes (CR-100) a stake of a higher-rung strand sorts first inside its tier (CR-101's slot), by `world_q.flow_capacity(kind)` ascending, the one position-in-roster computation the tree has (`:4896`); no second table (`ED-IN-0352`'s FORBIDDEN list). The era's bearers are the referents of its realm-rung moves, so they come first; this is "a rung is the stakes of a flow" (R4) read as an order.

**The person's era.** `era_known(p)` is what he believes: the holder his newest `held_by` claim on the head seat names (`20_NARRATIVE_C`), and the conditions his own open strands at the realm rung show (`flows_known`). He may serve a dead king (A-33) and believe a war on that has ended (AX-7). This is "a person's account of an era is the strands he holds together with the realm-rung moves he knows" (`strife-00` §4) returned as a tuple; nothing is stored and the world reading is not read.

## Instructions to code

Order of edits. Tier: commits 1 and 2 second tier (sonnet) with a third-tier critic on the turn rule; commit 3 second tier; commit 4 one row per landing proposal, in that proposal's commit.

**Commit 1 (EQUAL).** `engine/season/queries/world_q.py`, the strife world reading.
1. `rosters.yaml`: a closed roster `era_rule_standings`, `values: [held, vacant, minority, captive]`, and `era_conditions`, `values: [troubled, contested, civil_war, foreign_war, occupation, schism, dearth]`, each with `source:` this file and `cite:` the ledger id allocated at build (IN lane, `references/id_reservations.yaml`). Loader: `data/rosters.py` exports `ERA_RULE_STANDINGS`, `ERA_CONDITIONS` (the `roster_map` route `STRIFE_KINDS` uses).
2. `Era` (`:4929`): append `rule: tuple = ()`, `conditions: tuple = ()`, `opened_by: Optional[str] = None`, `closed_by: Optional[str] = None`. Defaults keep every existing constructor and test.
3. New `def realm_head_seat(w) -> Optional[str]`: `HEAD_SEAT.get(faction_holding(w, governing_hold(w, realm).subject))` for the one rung of `REALM_KIND`; `None` when the realm rung is unheld. Reuses the roster `faction_q.head` reads (`data/rosters.py:1315`, `HEAD_SEAT`; read at `queries/faction_q.py:150`); no literal.
4. New `def era_turns(w, flows) -> tuple`: one pass over `w.log`. A **rule turn** is an Event with a change or a `Subject.seat` receipt naming the head seat whose kind is `tenure.opened` or `tenure.closed` (`state/gate.py::TENURE_CLOSED` and its opened twin), or an `arrest.made` / `detention.ended` whose `detain` edge's subject is the seat's holder at that point of the replay. The holder is tracked by replay (a local), never read live. Returns `Turn(event, index, fact, before, after)` rows. `[ASSUMPTION; medium; Jordan to correct; revert: rule turns on tenure Events only]` for the two custody kinds.
5. `_eras` (`:5233`): keep the loop; add the cut. Merge `era_turns`' rule turns into the move walk by log index; on a rule turn, `close(done=True, closed_by=turn.event)` and start the next era with `opened_by=turn.event`. The first era opens at log index 0 with `opened_by=None` (the built realm), so there is always one. A **condition turn** for `troubled` is read off the strands already built: it opens at the first move of a realm-rung strand that is a non-content opening (`m.opens and m.kind not in CONTENT_OPENING_KINDS`), and closes at the terminal move after which no such strand is open (`_concluded` evaluated over the strand's moves up to that index, with `open_referents` as today, its stated live-state limit kept and named in the docstring). The turn rule above decides whether a condition turn cuts the era.
6. `open_era` (`:5255`): returns `flows.eras[-1]` always (there is always one); `presented` (`:5267`) reads `era.moves` as before.
7. `harness/strife.py::strands_block` (`:400-404`): the era line gains `rule=<standing> holder=<id> conditions=<…> opened_by=<kind>/<code> closed_by=<kind>/<code>`.
8. Tests, `engine/season/tests/test_strife_flows.py` (the covering file): `test_an_era_ends_when_the_head_seat_closes` (planted: a hold on the head seat, a `tenure.closed` naming it; reads two eras, the second `vacant`, `opened_by` the close); `test_a_second_trouble_does_not_end_a_troubled_era` (R11); `test_a_quiet_reign_ends_when_a_realm_strand_opens_by_force`; `test_two_petitions_do_not_trouble_the_realm`; `test_the_last_condition_closing_ends_the_era` (today's rule, re-pinned); `test_there_is_always_one_era` (an empty log reads one era, `held` or `vacant`, no conditions); `test_rename_falsifier_for_the_era` (rename every id in the planted world: equal reading; move the head seat's hold to another person: the reading follows). Each planted world asserts it asserted (`assert checked >= 6`).

**Commit 2 (EQUAL).** `engine/season/queries/person_q.py`: `def era_known(p: Person, head_seats: tuple) -> tuple` returning `(believed_holder or None, standing, conditions)` from `believed_holder` (`20_NARRATIVE_C` edit 3) and the kinds of his own open realm-placed strand claims; no World. Caller passes `head_seats` (the caller's, as `legitimacy` takes `holder`: `person_q.py:537`). Test in `tests/test_strife_flows.py`: `test_a_man_who_has_not_heard_still_serves_the_dead_king` (his `era_known` names the old holder while the world reading is `vacant`). **Depends on `20_NARRATIVE_C` commits 1 and 2**; before them the function returns `(None, "unknown", ())` and its test is skipped by name, not silently (`pytest.mark.skip(reason=…)` naming the dependency).

**Commit 3 (declared mover).** `engine/season/queries/world_q.py::questions_for` (`:4260-4267`): the `vacancies(w, p)` term's ids that are head seats (`set(HEAD_SEAT.values())`) and that `state/gate.py::may_claim` (`:770`; called with its own arguments, the Office and the `successions` titles, as `succeed`'s admission calls it) admits for `p` are passed with `mandatory=True` to `_stamped`; `state/carriers.py::Question.mandatory` is the field `12_ARCS_arcs_as_staged_goals.md` adds (**dependency**; if it lands later, this commit waits). `attention_key` (`:3857`) sorts a mandatory question first inside tier 0. Behind `Fixtures era_mandatory_vacancy` (`False` the control, EQUAL; `True` the mover). Test `engine/season/tests/test_strife_flows.py::test_a_vacant_head_seat_corners_those_who_may_claim` (planted vacancy: the claimant's first question is the seat; a person who may not claim is unmoved; with the fixture off, byte-identical).

**Commit 4 (EQUAL each).** One `ERA_CONDITION_READERS` table in `world_q.py`, `{condition: (opens(e, a, rd) -> bool, closes(e, a, rd) -> bool)}`, read by `era_turns`. A condition with no reader, or whose Event kind no verb row or MATTER pass emits (computed from `data/verbs.py::EVENT_KINDS`), reads `n/a` in the instrument, never absent. Rows land with their emitters:

| condition | opens on | closes on | lands with |
|---|---|---|---|
| `contested` | the second `succession.claimed` on the head seat (`_content_matter`, `:5033`) | `tenure.opened` on it with no other claim standing | `14_VERBS_BINDING_C`, `22_HAPPENINGS_B` |
| `civil_war`, `foreign_war` | a `commitment.made` to a WAR Proposition by a mustering seat; side by `FOREIGN_FACTION_IDS` | the last such commit's `commitment.ended` | `06_FA_war_lives_in_seats_B` |
| `occupation` | the occupier's presence Event on a rung it does not hold | its leaving or `rung.seized` | `U5d_FA_land_and_seats_pass_on_a_won_march.md` |
| `schism` | an A-46 move by a holder whose `influence_rung` is the realm | the strand it opened concluding | `09_WR_strand_conclusion.md` (A-46 step), CR-104 |
| `dearth` | the realm-rung spell Event in its Failure band | the next year's spell Event above it | `09_WR_B_weather_with_memory_and_the_year.md` |
| `minority` (a RULE standing) | `tenure.opened` on the head seat by a holder under `majority_age` | his majority tick | `23_STORY_B` |

## The gate (execution artifacts)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.strife 2 0 --strands           # commit 1
python -m pytest engine/season/tests/test_strife_flows.py -q                      # the covering file, at the close
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 8 --arms off bodies --stories   # after 22_HAPPENINGS_A, 23_STORY_D
```

Expected. First: every era line names `rule=held` and the head seat's holder; the first era has `opened_by=None`; the march strand of P-1 (`7ebe96bc…`, opening `march.declared`) opens `troubled` and the two petition strands do not; and `build_realm(0)` and the one- and two-season hashes are EQUAL. How many eras the seed prints depends on whether that strand reads concluded, which `09_WR_strand_conclusion.md` edit 1 changes; the count is recorded in the commit, not predicted here. Third (the ending gate, read through `30_WR_E`'s shapes E-01 to E-03): with natural death live, a change of RULE occurs at 2 seeds or more of 5 and not at all 5 with the same count; the turn's code is not the same at every seed where it occurs; with the bodies arm at control it occurs at none.

## The falsifier, and its control

- An era count that differs between `strands_block` read before and after a no-op season (the reading stored something or read live state): the replay is wrong.
- Two eras with the same `rule` and both with no conditions, adjacent (a cut with no turn).
- The rename falsifier failing (a key crept in).
- Control: the planted world with no hold on any head seat reads one era, `vacant`, at every length of log.
- Commit 3: any hash moving with the fixture off; a person who may not claim receiving the mandatory mark.

## Dependencies

Commit 1: none. Commit 2: `20_NARRATIVE_C`. Commit 3: `12_ARCS_arcs_as_staged_goals.md`, `22_HAPPENINGS_B` (so more than one person may claim). Commit 4: per row. Feeds: `30_WR_C`, `30_WR_E`, `30_GO_F`, CR-97 (its era line), CR-100 (the bearers it stamps).

## Layer 1

`04_CODE_ARCHITECTURE.md` §A.2 (`queries/` owns nothing, holds no token): kept; graded **STRUCTURAL**, conformed to. §B.9 (an Event has no actor; the doer through `causes[]`): kept, **STRUCTURAL**. AX-2 (`decision/` reads no World): `era_known` is person-side and takes no World, **STRUCTURAL**. AX-7: kept. ID-16 (loops declared): no loop is added by commits 1, 2 and 4; commit 3 lengthens L1's path by nothing (it reorders one question), **CONVENTION**, recorded on L1's row when CR-98 lands. No hunk is asked of Layer 1.

## NERS reading

- **N.** Remove it and the charge's own examples cannot be said: no reader can tell a reign from the war that ended it. It holds top-down (the realm's history as a sequence of named spans), bottom-up (one death ends a reign), laterally (WR's strands, FA's seats and wars, SE's dearth and CHAR's ages each supply a turn), and diagonally (the person's `era_known` against the world's). Narrowed in one direction: at the scale of a duchy the same reading would give a duchy its own eras; that is not built and not asked.
- **R.** The no-player half: a king dies in a hard winter and the realm is a different place for everyone. Completeness: an empty log has one era; a realm with no head seat reads `vacant` and says so; a condition with no emitter is `n/a`.
- **S.** One reading, one roster of standings, one of conditions; it pauses nothing; it reuses `_eras`' own conclusion rule for troubles, so there are not two ladders for "when did it end".
- **E, last.** Two facts and three clauses. A player can state the rule in a sentence and predict the next era from an event. High.

## Cost class

Commit 1: small build. Commit 2: edit. Commit 3: edit, a declared mover. Commit 4: one edit per row.
