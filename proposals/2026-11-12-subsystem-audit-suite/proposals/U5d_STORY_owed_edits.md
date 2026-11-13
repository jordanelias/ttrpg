# U5d-STORY — owed edits: five story-enablement decisions that named an owner and no file

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §2 / U3 §9 (§1's `[unverified]` `besiege` posture) checked at the tree: `rosters.yaml: march_postures` (`:1159`) has `values: [storm]` only; its note says `besiege` "joins this list in its own declared-mover commit" (CP-T04-06, B10-12), so §1 depends on that commit and is INCOMPLETE until a carrier lands it (no proposal in this set carries it). §5's `[not re-opened]` site opened: `modules/combat/wrapper.py:418` returns on `defender.felled` right after the aggressor's blow, before the defender's blow of the same exchange is applied, which is the defect §5 names. Named tests added per section (R3 §7: none were named); batch and tier (U3 B39; R3 7b-0). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*).

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Lands in batch: B39 (procedural generation and cases), after `U5d_STORY_owed_edits`'s predecessors in U3 §1 item 39 (`21_PROCEDURAL_C`, `_D`), before `23_STORY_B`.
Depends on: `07_SE_ground_and_granaries.md` (B12, the walk); `09_WR_B_draws_not_thresholds.md` (B12); `14_VERBS_MATERIAL_A_mending.md` (B12); `16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md`, `18_DETERMINISM_notice_is_a_draw.md` (B11); `22_HAPPENINGS_C` (B37); the `besiege` member of `march_postures` (CP-T04-06, plan position; MISSING until STAGES.md step 5 carries it) for §1.

Author: U5d closure lane (Fable), 2026-11-12. Carries `audits/23_STORY_ENABLEMENT.md` §8.1 R-07, R-08,
R-11, R-12 and R-21, each "listed for" another lane with no file. Each lands in that lane's batch; this
file states the edit, gate and falsifier so the item is not lost. Nothing is deterministic: every
outcome below is a draw on the one ladder; the eligibility checks are marked as such.

## What it changes in `engine/season/` at runtime

§1: a besieged place's cohorts cannot draw on larders above the besieged rung. §2: a store can be
sabotaged, by a draw. §3: a lapsed due under an empty seat is laid at the door of whoever could have
filled it. §4: an attacker whose victim failed to notice him has a named level in the first exchange.
§5: two blows drawn in one exchange are both applied before the felling check.

## §1 — a besieged town's larder (R-07; owed to SE and MB)

- **Owner.** The larder ladder's walk in `modules/settlements/subsist.py` (the walk
  `07_SE_ground_and_granaries.md` §4 d edits); the posture is `rosters.yaml: march_postures`' (verified
  at `main`: `values: [storm]` only, `:1159`; `besiege` joins in CP-T04-06's own declared-mover commit,
  so this section waits on it; the field band `Invested` and `siege.pressed` exist, `data/rosters.py:1256`).
- **Edit.** While an `Invested` field stands on a rung, the walk for cohorts beneath it stops at that
  rung (eligibility: which rungs may feed whom). The besieger's ration is
  `07_SE_campaign_supply_and_muster.md`'s standing ration, once a season.
- **Gate.** A hand-built siege of four seasons: the town's stores fall and its cohort's body is drawn
  down by the hunger draw (`09_WR_B_draws_not_thresholds.md` edit 2), while a twin town with the siege
  lifted eats from the duchy. Test, in `07_SE_ground_and_granaries.md`'s `engine/season/tests/test_endowment.py`:
  `test_an_invested_rung_stops_the_walk_for_the_cohorts_beneath_it`. **Falsifier.** The besieged town
  drawing from above its rung.
- **Movers.** Runs with an `Invested` field (none in computed play today; `march` by army verbs is
  withheld). Declared.

## §2 — a burned granary (R-08; owed to the MATERIAL lane's `sabotage` row)

- **Owner.** `verb_table.yaml`, row `sabotage`; its drawn form is `14_VERBS_MATERIAL_A_mending.md`'s.
- **Edit.** `sabotage`'s referent class gains a rung's store of a kind beside a Site; the loss is the
  band's (Overwhelming most of the store, Success half, Partial a tenth and the doer's trail is left,
  Failure nothing and the trail is left) `[ASSUMPTION; medium; Jordan to correct]`; the trail is
  `16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md`'s.
- **Gate.** All four bands occur across 20 dice seeds on one hand-built world; test
  `test_sabotage_of_a_store_reaches_every_band_and_leaves_a_trail_below_success`, in the file
  `14_VERBS_MATERIAL_A_mending.md` names for `sabotage`. **Falsifier.** A store lost at Failure; a certain
  loss. **Movers.** Runs where a `sabotage` forms on a store. Declared.

## §3 — who is blamed under an empty seat (R-11; an amendment to `20_NARRATIVE_B_what_he_was_owed.md`)

- **Owner.** `queries/person_q.py::dues_unmet` (NARR-B's reader).
- **Edit.** A due that lapses while the owing seat is vacant is attributed to the person the wronged man
  **believes** holds a seat that may fill it (`may_fill`, read through his own `held_by` claims,
  `20_NARRATIVE_C`), else to nobody. Under A-33 he may still believe the dead holder holds it: then the
  dead man is blamed until the death is learned.
- **Gate.** NARR-F's clause for G2 on a hand-built vacancy: the blamed person is the believed filler;
  test `engine/season/tests/test_narrative_dues.py::test_a_lapse_under_a_vacant_seat_is_laid_on_the_believed_filler`
  (the file `30_WR_D` and NARR-B open).
  **Falsifier.** Blame laid by reading World truth. **Movers.** None in the loop until NARR-B lands.

## §4 — the opener's edge (R-12; the ladder's D-41, following A-16)

- **Owner.** `rosters.yaml: context_terms` (`14_VERBS_PHYSICAL_A_custody_and_force.md` A3), contexts
  `enmity` (`22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md`) and `war`.
- **Edit.** One entry, `unready`: a named level for the attacker in the first exchange when the
  victim's notice draw (`18_DETERMINISM_notice_is_a_draw.md`) failed. It modulates one exchange and
  decides nothing.
- **Gate.** With the notice draw forced to each band on one hand-built attempt, the first exchange's
  pool differs by the level and the scene's outcome still varies across dice seeds; test
  `test_an_unready_victim_gives_the_opener_one_level_in_the_first_exchange_only`, in the file
  `14_VERBS_PHYSICAL_A_custody_and_force.md` names for `context_terms`. **Falsifier.** An ambush that
  always kills. **Movers.** Runs with an `enmity` or `war` scene. Declared.

## §5 — two men who kill each other (R-21; owed at PC's owner)

- **Owner.** `modules/combat/` exchange resolution (`wrapper.py:418-419`, opened at `main` in wave 3:
  `if defender.felled: _emit_outcome(...); return defender, closed` follows the aggressor's blow, so the
  defender's blow of the same exchange is never applied; the sibling checks at `:395` and `:440` are read
  by the same edit).
- **Edit.** Both parties' blows drawn in one exchange are applied before the felling check, so a
  mutual felling is an outcome of draws already taken. No new draw.
- **Gate.** The PC pessimist's 5,000-duel reading shows mutual fellings above 0; test
  `tests/valoria/` beside the combat module's exchange tests,
  `test_both_blows_of_one_exchange_land_before_the_felling_check` (a planted exchange in which each blow
  fells). **Falsifier.** 0 of 5,000 again. **Movers.** Every fight's log. Declared; lands with A-31's recalibration.

## NERS (E last)

N: five stories (S-22's siege, S-36's fire, S-33's blame, S-09's ambush, S-28's double death) have no
other carrier for these links. R: each adds an outcome that can go either way. S: each is a row or a
term at an existing owner. E: five short items.

## Cost class

Edits (§1, §3, §4, §5); a small build (§2). Tier: `sonnet` (R3 7b-0).
