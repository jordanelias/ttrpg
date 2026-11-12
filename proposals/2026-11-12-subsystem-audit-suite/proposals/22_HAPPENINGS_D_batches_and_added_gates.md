# HAPPENINGS-D — the landing batches, the gates added to proposals already on file, and one content repair

## Status: PROPOSED

Source: `audits/22_HAPPENINGS.md` §2, §3. Reference only (`CLAUDE.md` §0.05). This file redoes no
proposal. It says in what order the suite's proposals stop the happenings a player would find odd, adds
to four of them a reading their own gates do not take, and writes one small content edit no lane holds.

## What it changes in `engine/season/` at runtime

By itself: the `home:` of a handful of `npcs.yaml` rows (§3; a declared mover of every world hash, as
residence is build state). Everything else here is ordering and gate text for other proposals.

## 1. The batches, in order, and why in that order

The order is by harm stopped per edit, with one constraint: a batch that removes senseless acts lands
before a batch that makes acts consequential, or the senseless acts become consequential first. The
King's death at seed 2 is that failure in miniature: `capture` was made executable (CP-T03-09) before it
was given a cause.

| # | batch | lands | then stops (audit rows) | depends on |
|---|---|---|---|---|
| 1 | violence has a cause and a mercy | `14_VERBS_PHYSICAL_A` A2 first, then A3, A0, A1, A4; `03_PC_duel_chain_reach`; `16_PESSIMIST_PC_A`; `18_DETERMINISM_no_certain_matchup` | H-01, H-11, H-12 | `06_FA_remit_grant_by_row` (PHYSICAL_A's own stated dependency) |
| 2 | offer what makes sense | `02_CHAR_offer_what_can_be_done`; the `14_VERBS_*_A_formation` files; `16_PESSIMIST_CORE_a_refusal_is_remembered` | H-03, H-04, H-09, H-10, H-28 | — |
| 3 | outcomes are drawn and written | `18_DETERMINISM_task_draw_for_uncontested_verbs`; `10_DICE_*`; `05_SC_obstacle_difficulty_and_modifiers_B`; `13_SC_*`; `19_LACUNA_*`; `14_VERBS_BINDING_D`; `14_VERBS_SOCIAL1_B` | H-06, H-16, H-17, H-18, H-20, H-32 | batch 2 (F-PES-DICE-02: with everything drawn at the shipped pool and obstacle the realm does a sixth of what it does; fewer wasted attempts first) |
| 4 | seats pass | `06_FA_decree_binds`; `14_VERBS_BINDING_C`; `15_INSTITUTIONS_BYZANTINE_E`; `16_PESSIMIST_FA_A`, `_B`, `_C`; `06_FA_seat_terms_*`; `15_INSTITUTIONS_SYNTHESIS_B` edit 6; **`22_HAPPENINGS_B`** | H-07, H-23, H-24 | batch 3 (the contested rows' obstacle owner) |
| 5 | bodies and time | `16_PESSIMIST_SE_A`; `03_PC_exits_withdrawal_recovery` Part C; `16_PESSIMIST_GAME_the_world_draws`; `21_PROCEDURAL_B`; **`22_HAPPENINGS_A`** | H-02, H-15, H-29, H-30 | batch 4 (a death should open a seat that can pass); Jordan's item 1 |
| 6 | crimes, cases and news | `08_FI_02`, `_06`, `_07`; `16_PESSIMIST_FI_A`; `18_DETERMINISM_notice_is_a_draw`; `21_PROCEDURAL_C`; `16_PESSIMIST_GAME_standing_occasions_carry_their_cause`; **`22_HAPPENINGS_C`** | H-21, H-22, H-33 | batches 1 and 2; Jordan's item 2 |
| 7 | persons differ and remember | `16_PESSIMIST_CHAR_A`, `_B`, `_C`; `02_CHAR_relations_have_a_ground`; `02_CHAR_which_ground_moves_whom`; `20_NARRATIVE_*` | H-08, H-19, H-27, H-34 | batch 2 |
| 8 | places differ and the world can end | `07_SE_ground_and_granaries`; `16_PESSIMIST_SE_B`; `21_PROCEDURAL_A`; `04_MB_headcount_grade_and_scale`; `06_FA_war_lives_in_seats_B`; `16_PESSIMIST_FA_B` edit 4; `09_WR_strand_conclusion`; `09_WR_B_readings_of_closure_and_tension`; `16_PESSIMIST_GAME_consequence_reading`; §3 below | H-05, H-13, H-14, H-25, H-26, H-31 | — |

Batch 1's first commit can land today and alone: PHYSICAL_A A2 is two data lines
(`violence_contexts: capture: [war, crime]`, `referent_class: Person`) and one effect edit, and it is
what keeps the King alive at seed 2.

## 2. Gates added to proposals already on file (requests; those files are not edited)

Each is a reading the owning proposal's gate would pass without making, and that this lane's runs show
is needed.

**G-1, for `14_VERBS_PHYSICAL_A` A2.** Its gate reads `aperture 2 0` and `aperture 2 1`. The King dies in
the **fourth** season at seed **2**. Add: `PYTHONHASHSEED=0`, `populated.build_realm(2)`, four seasons:
(i) no `capture.declared` whose actor meets no listed context; (ii) the holder of `off_king` at build is
alive at the end; (iii) at seeds 1 and 2 the holder of `off_cardinal_prudence` does not die as the actor
of his own `capture`. Before the edit all three fail (`runs/HAPPEN/king_1.json`, `king_2.json`). The
control that the instrument can see a capture at all: with a planted warrant addressed to the Spymaster
naming a person where he stands, `capture.declared` occurs.

**G-2, for `16_PESSIMIST_PC_A_the_yield_is_a_draw` and PHYSICAL_A A3.** Read at seeds 1 and 2, four
seasons, today: `capture.declared` 9, `person.captured` 0, `person.died` 3. After: over the same scenes
replayed (or 200 seeded `capture` scenes between two season persons), `person.captured` is the most
common outcome and a death the rarest; all three of captured, escaped-wounded and dead occur.

**G-3, for `02_CHAR_offer_what_can_be_done`.** Add the per-target reading its table does not carry: at
seed 0, one season, the count of refused acts by other persons whose subject is the holder of `off_king`
(today 27: `train` 13, `tend` 6, `capture` 2, `sabotage` 2, `release` 2, `challenge` 2) falls to at most
the number refused for a reason the actor could not know of himself (the `with` clause: he is not where
the King is). No `train`, `tend` of an unwounded body, or `sabotage` with a person as `site` is formed.

**G-4, for `03_PC_duel_chain_reach` and PHYSICAL_A A4.** Today, four seasons: seed 1 `challenge.refused`
180 of 180 issued; seed 2 174 of 174, `accept.refused` 81. After: at least one challenge per seed is
heard and answered by an `accept` that reaches a scene, and `challenge.refused` is under half of the
challenges issued.

## 3. One content repair: where the seat-holders live

**Problem.** `engine/season/npcs.yaml` authors each cast row's `home:`. Read at build: the King's is
`b_s_002_cottage` (`npcs.yaml:186`; probe `king_0.out`); F-PES-FA-03 reads the Duchess of Hafenmark at
`b_s_001_court` in the Crown's territory, the Duke of Varfell at an inn there, the Confessor in a market
there, and 18 of 34 seat-holders off their seat's ground. `16_PESSIMIST_FA_C_under_the_seat` makes
governance stop depending on the home and says the homes themselves are *"WR's and CHAR's, cross-listed"*.
Nobody holds them.

**Decision** (ladder step 5; content, so each value is `[ASSUMPTION; medium; Jordan to correct]`):

1. A holder of a seat anchored on the realm rung lives in a building of the court kind in the capital
   settlement. The King, the Queen, the Prince and the Princess move to `b_s_001_court` (the building
   the Duchess is recorded at).
2. A holder of a ducal seat lives in his duchy's own seat settlement, in its largest dwelling. The
   Duchess of Hafenmark and the Duke of Varfell move home. Whether either keeps a second residence at
   court is not expressible today (one `reside` edge) and is not added.
3. The Confessor lives at `b_s_036_cathedral` (the building his representative's row names).
4. Every other row is left. A councillor who lives at court and sits on a duchy's council is ordinary.

**Owner and edit.** `engine/season/npcs.yaml`, the `home:` key of those seven rows. The two ducal
buildings are named at landing from `build_realm(0)`'s settlements (the largest dwelling Site of the
territory that PES-FA-A edit 2 names as each duchy's seat) `[UNVERIFIED: the ids; not read here]`.
Nothing in code changes. A declared mover of every world hash and of every seeded pin: co-location
decides who witnesses whom, so this is a large mover for seven lines and lands in the batch-8 commit
that re-records, never alone.

**Gate.** `python -m engine.season.harness.populated` builds; a probe prints, for every seat-hold,
whether the holder's home lies under the seat's rung (`state/gate.py::purview_reaches` over
`world_q.home_of`): the realm seats and the three named heads read true; the count off-ground falls from
18 by at least seven. The capacity of `b_s_001_court` is read first (`world_q.capacity`): if the court
cannot house four more, the edit names a second court building and says so.

**Falsifier.** The probe's count unchanged; or the build refusing a home that is over capacity.

**NERS.** N: a reader meets the King at his court; a spy who watches the court sees the royal family,
which is what co-location is for. R: where a lord lives is now a fact a player can use (who is near him,
who guards him: `guard_weight` reads the principal's own place). S: no rule added. E, last: seven values.

## Cost class

§1 and §2: none (text for other proposals). §3: edit (data), one large declared mover.
