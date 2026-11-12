# U5d-STORY — owed edits: five story-enablement decisions that named an owner and no file

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

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
  `07_SE_ground_and_granaries.md` §4 d edits); the posture is `rosters.yaml: march_postures`'
  (`[unverified]` that `besiege` is a rostered posture at HEAD; the field band `Invested` and
  `siege.pressed` exist, `data/rosters.py:1256`).
- **Edit.** While an `Invested` field stands on a rung, the walk for cohorts beneath it stops at that
  rung (eligibility: which rungs may feed whom). The besieger's ration is
  `07_SE_campaign_supply_and_muster.md`'s standing ration, once a season.
- **Gate.** A hand-built siege of four seasons: the town's stores fall and its cohort's body is drawn
  down by the hunger draw (`09_WR_B_draws_not_thresholds.md` edit 2), while a twin town with the siege
  lifted eats from the duchy. **Falsifier.** The besieged town drawing from above its rung.
- **Movers.** Runs with an `Invested` field (none in computed play today; `march` by army verbs is
  withheld). Declared.

## §2 — a burned granary (R-08; owed to the MATERIAL lane's `sabotage` row)

- **Owner.** `verb_table.yaml`, row `sabotage`; its drawn form is `14_VERBS_MATERIAL_A_mending.md`'s.
- **Edit.** `sabotage`'s referent class gains a rung's store of a kind beside a Site; the loss is the
  band's (Overwhelming most of the store, Success half, Partial a tenth and the doer's trail is left,
  Failure nothing and the trail is left) `[ASSUMPTION; medium; Jordan to correct]`; the trail is
  `16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md`'s.
- **Gate.** All four bands occur across 20 dice seeds on one hand-built world. **Falsifier.** A store
  lost at Failure; a certain loss. **Movers.** Runs where a `sabotage` forms on a store. Declared.

## §3 — who is blamed under an empty seat (R-11; an amendment to `20_NARRATIVE_B_what_he_was_owed.md`)

- **Owner.** `queries/person_q.py::dues_unmet` (NARR-B's reader).
- **Edit.** A due that lapses while the owing seat is vacant is attributed to the person the wronged man
  **believes** holds a seat that may fill it (`may_fill`, read through his own `held_by` claims,
  `20_NARRATIVE_C`), else to nobody. Under A-33 he may still believe the dead holder holds it: then the
  dead man is blamed until the death is learned.
- **Gate.** NARR-F's clause for G2 on a hand-built vacancy: the blamed person is the believed filler.
  **Falsifier.** Blame laid by reading World truth. **Movers.** None in the loop until NARR-B lands.

## §4 — the opener's edge (R-12; the ladder's D-41, following A-16)

- **Owner.** `rosters.yaml: context_terms` (`14_VERBS_PHYSICAL_A_custody_and_force.md` A3), contexts
  `enmity` (`22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md`) and `war`.
- **Edit.** One entry, `unready`: a named level for the attacker in the first exchange when the
  victim's notice draw (`18_DETERMINISM_notice_is_a_draw.md`) failed. It modulates one exchange and
  decides nothing.
- **Gate.** With the notice draw forced to each band on one hand-built attempt, the first exchange's
  pool differs by the level and the scene's outcome still varies across dice seeds.
  **Falsifier.** An ambush that always kills. **Movers.** Runs with an `enmity` or `war` scene. Declared.

## §5 — two men who kill each other (R-21; owed at PC's owner)

- **Owner.** `modules/combat/` exchange resolution (`wrapper.py:418-419` as the PC pessimist cites it;
  `[not re-opened]`).
- **Edit.** Both parties' blows drawn in one exchange are applied before the felling check, so a
  mutual felling is an outcome of draws already taken. No new draw.
- **Gate.** The PC pessimist's 5,000-duel reading shows mutual fellings above 0. **Falsifier.** 0 of
  5,000 again. **Movers.** Every fought scene's log. Declared; lands with A-31's recalibration.

## NERS (E last)

N: five stories (S-22's siege, S-36's fire, S-33's blame, S-09's ambush, S-28's double death) have no
other carrier for these links. R: each adds an outcome that can go either way. S: each is a row or a
term at an existing owner. E: five short items.

## Cost class

Edits (§1, §3, §4, §5); a small build (§2).
