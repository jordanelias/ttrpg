# U5d-SE — the common people move in a few heavy ways, and caste is felt in regard, in vote blocks and in informal tiers of right, privilege and wealth

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Author: U5d closure lane (Fable), 2026-11-12, on Jordan's answers A-56 (D-73), A-41 (D-52), A-42 (D-53)
and the ladder-closed D-68 (`unified/DECISIONS_ANSWERED.md`). Carries `audits/07_SE_audit.md` F-SE-14,
`audits/16_PESSIMIST_SE.md` F-PES-SE-01, `audits/16_PESSIMIST_FA.md` F-PES-FA-04 ("the governed are in
none"), `audits/16_PESSIMIST_GAME.md` §7.3 J-2, and the caste rows of the institutions kit that A-41
re-decided (no corvée instrument, no caste seat, no caste audit).

## The rulings, quoted

- A-56: *a few heavy moves (petition, migrate, work, tend, comply or refuse, riot)*.
- A-41: *"express caste not only in regard, but also vote blocks and informally tiered
  rights/privileges/wealth"*.
- A-42: franchise authored as the vote-block carrier (taken from A-41's words; to confirm).
- D-68 (ladder): farm work is an act, sequenced after the cohorts' heavy moves land.

## What it changes in `engine/season/` at runtime

1. A cohort (a `Person` with `is_cohort`, weight above 1) forms candidates only for the rostered heavy
   moves. Today it is offered the whole verb table and makes 708 of 1,529 resolved acts at seed 0
   (`create_record` 115, `utter` 70, `challenge` 60, `forge` 47; `audits/07_SE_audit.md` F-SE-14).
2. One verb row is added, `riot`, the only heavy move with no row today (the roster is 67 rows; `tie` and
   `knot` split makes 68 under A-28; this makes 69 and the requirement instrument's count moves).
3. Caste enters three ways, each as odds or as data and none as a gate: regard (built: 
   `queries/person_q.py::heritage_regard`, CR-31); a territory and caste weight a ballot's draw reads
   (`U5d_FA_owed_edits.md` §4); and a practice table that tiers what a heritage earns, is trusted to hold
   and is heard on.

Hash movers (declared): (1) moves every seeded realm run (cohort acts are 43% of acts by the GAME
pessimist's count); (2) moves runs in which a cohort riots; (3) moves nothing until its rows are
authored (every tier 1.0 is the control).

## Exact edits, by owner, in order

**1. `engine/season/rosters.yaml`**: a closed roster `cohort_moves: [petition, migrate, work, tend,
comply, "evade / defy", riot]` with its source line (A-56). Loader `data/rosters.py` exposes
`COHORT_MOVES` and refuses a member that is no verb row.

**2. `engine/season/decision/options.py`** (`:132-139`, where `withheld_verbs` already holds a verb out
of formation for every NPC): for an actor with `is_cohort`, the opening set is intersected with
`COHORT_MOVES`. One conjunct at the one formation site; no branch on a person id. The control arm is a
fixture `cohort_moves_on: False` (today's full table), so the flip is its own declared mover with a
before-and-after reading.

**3. `engine/season/verb_table.yaml`, a row `riot`** (design-first; the row's cells are proposed, not
ruled): eligibility `own`, formed only by a cohort; subject a Site or a seat's rung of the place the
cohort resides in; contested on the one ladder (pool: the cohort's body and weight; obstacle: the
place's garrison condition, `settlements.fortification`, plus the composer's named terms); bands:
Overwhelming and Success wear a Site and emit `riot.made`; Partial emits `riot.made` and wears nothing;
Failure emits `riot.put_down` and writes the cohort's body. `riot.made` joins `UNREST_KINDS` (the deeds
`stability` counts per rung). Every cell `[ASSUMPTION; medium; Jordan to correct; revert: drop the row
and the roster member]`. What forms it: a cohort short at the last MATTER
(`World._subsistence_shortfall`) or holding a grievance claim against the place's holder; the chooser
ranks it against `petition`, `migrate` and `evade / defy` as it ranks any candidates.

**4. `engine/season/rosters.yaml`**: a table `caste_practice`, keyed by `Person.heritage` value, with
three columns, each a factor whose shipped value is 1.0 for every row (the control) and whose authored
values are Jordan's content `[ASSUMPTION; Jordan to author; canon reach: the southern Einhir]`:
`earns` (the share of a place's yield a cohort of that heritage keeps, read by plan CP-T08-01's labour
reader and by the store split of `16_PESSIMIST_SE_A` edit 1), `holds` (an obstacle term on a `confer`
whose conferee is believed of that heritage, read by the one obstacle composer), `heard` (an obstacle
term on a `petition` or `argue` by a person believed of that heritage). The last two read what the
**other party believes** of the man's descent, as `heritage_regard` does, never `Person.heritage`
itself: the tier is a practice of people, not a statute, and a man who passes is treated as what he is
taken for.

**5. Vote blocks.** `U5d_FA_owed_edits.md` §4 (`faction_q.weight` and the territory weight). No second
table.

**6. Farm work (D-68).** `work` is already a verb row and a member of `COHORT_MOVES`; its yield reading
is plan CP-T08-01's. Sequenced after edits 1–2 land.

## Gate (execution artifact)

`python -m engine.season.harness.aperture 3 0` before and after the flip of `cohort_moves_on`: the
share of resolved acts by cohorts, and the count of cohort `forge`, `challenge` and `create_record`
acts (must read 0 after). The named persons' acts: the GAME pessimist read 5 of 798 changed when cohort
deliberation was removed entirely; the after-arm should sit near that. For `riot`: the fail arm of the
SE pessimist's two-arm run (eleven towns short) shows at least one `riot.made` or `riot.put_down`
across the swept dice seeds and neither in every seed. For edit 4: with every factor 1.0 the realm hash
equals the pre-edit hash (control).

## Falsifier

A cohort forging a document after the flip; a riot in every short town in every seed (a fixed
outcome); a caste factor that refuses an act outright; a reader of `Person.heritage` in edit 4's two
belief-read columns.

## Not decided here (marked)

The numbers of every tier and the `riot` row's cells are content. Whether an individual commoner (not a
cohort) is limited to the same list is not stated by A-56 and is not assumed: this plan limits cohorts
only. The colonial kit's corvée instrument is not built (A-41).

## NERS (E last)

N: without it the realm's log is mostly the populace's paperwork (F-SE-14) and a failing place moves no
one (F-PES-SE-01). R: the populace becomes a force the named persons act against; a famine has
petitions, flight, refusal and riot, with nobody watching; caste is a lever a ruler can pull (reform) or
exploit. S: one conjunct at the one formation site; riot is an ordinary contested row; caste terms enter
through the one obstacle composer. E: seven moves a player can name; three caste channels, each a single
table or reader.

## Cost class

Edit (1, 2, 5), design-first (3), data with a small build (4).
