# 18 · DETERMINISM · A — every consequential verb draws: the uncontested fold becomes bookkeeping only

## Status: PROPOSED

Source: `audits/18_DETERMINISM_SWEEP.md` C-01, C-03, C-05, C-08, C-09, C-15 (and D-05, D-10). Standing
rule: `AUDIT_BRIEF.md` (Jordan, 2026-11-12, *"we do not do deterministic"*). Reference only (CLAUDE.md
§0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

Every act of a verb that writes or finds something a person in the fiction could see go otherwise now
rolls once through the route `research` already takes, and folds at the band it gets. In the realm
that is about 727 outcomes in five seasons over three seeds that today take effect on eligibility
alone (`reconstruct`, `tend`, `forge`, `conceal`, `issue`, `move`, `survey`, `open_case`, `interview`,
`migrate`, `carry`, `requisition`, `thread_read`, `release`), plus every act of the rows refused today
once they are admitted (`train`, `sabotage`, `raze`, `seize`, `found`, `build`, `confer`, `pardon`,
`establish`). Pure bookkeeping (writing one's own record, uttering, committing oneself, scheduling,
moving one's own stores) is declared and stays draw-free. A hash mover for every world in which any
converted verb executes: every realm and case golden.

## The problem (evidence)

- `engine/season/loop/resolve.py:1079-1111`: an act goes to the seam only if its row has `contests:`
  or a `graded_inquiries` route; otherwise `_fold(w, token, a)` runs with `resolution=None`, and
  `_fold`'s own docstring says that is *"every uncontested act, which is every act the corpus
  produces"*: the effect applies once `_admits` passes.
- 53 of the 67 verb rows take that path (11 contested, 3 graded): `…/scratchpad/runs/DET/verbs.txt`.
- Realm probe (`…/scratchpad/det_probe.py`; seeds 0 ×1 season, 1 and 2 ×2 seasons; 3,826 resolved
  acts): 2,159 success events, of which 1,995 carry no degree (92 %). Per verb, success events without a
  draw: `reconstruct` 244, `tend` 118, `forge` 90, `conceal` 72, `issue` 49, `move` 45, `survey` 32,
  `open_case` 23, `interview` 18, `migrate` 13, `carry` 8, `requisition` 6, `thread_read` 5,
  `release` 4 (plus bookkeeping: `create_record` 645, `utter` 350, `commit` 142, …).
- `_eff_tend` (`loop/effects_combat.py:767-790`) restores a body to its ceiling; `_eff_forge` mints every
  forgery at `Fixtures.default_forgery_quality`; `_seize_rung` *"asks nothing of the defenders"*;
  `_eff_succeed`: *"the first valid claim wins"*.

## The resolution, decided

Ladder step 4 (precedent: `research`, `examine`, `surveil` already roll through `graded_inquiries` →
`seam.grade` → `social_contest.roll` → `degree_of` → `_fold(…, Resolution)`) and step 5 (one route, one
roller, one loader refusal; no second resolver).

1. **Three resolution classes, one per writing row, derived — not a new column.** `contest` = the row
   has `contests:`; `task` = the row has a route in the roster below; `bookkeeping` = the row is a
   member of a new closed roster `bookkeeping_verbs`, each with a `why:` line. A row that writes or
   emits a finding and is in none of the three is **refused by the verb loader** (`data/verbs.py`),
   naming the verb. The loader also refuses a `bookkeeping` row whose `writes:` touch `Person.body`,
   `Person.capability`, `Person.exists`, `Person.body_ceiling`, a seat-`hold` Tenure, a Tenure whose
   holder is not the actor, or `Rung.stores` of a rung the actor does not hold, or whose `emits:`
   include `finding.made`. This is the loader's refusal per data family (CLAUDE.md §0.05), not a
   tree-wide guard.
2. **The route roster is renamed for what it now holds.** `rosters.yaml: graded_inquiries` →
   `graded_tasks` (`GRADED_INQUIRIES` → `GRADED_TASKS` in `data/rosters.py`, its three readers updated);
   its three rows carried unchanged; `check_graded_inquiries` → `check_graded_tasks`, same three
   refusals. Every `task` row is `{provider: "social_contest", module_entry: "social_contest.roll"}`,
   the pair a prize row already binds, so **no roll and no resolver is added** (the provider's name is
   historical; the roll is the generic pool-against-obstacle draw, `engine/dice_engine` underneath).
3. **Odds, from state; outcome, from the draw.** Pool = `seam/wrappers/sigma.py::faculty` (the verb's
   `verb_capability` key, else `pool_default`). Obstacle = `roll.py::obstacle` — the task's difficulty
   (the `difficulty` column `13_SC_tuning_tables.md` T1 puts on the verb row; until it lands,
   `obstacle_default`) plus the named modifiers that already exist (a person subject's opposition, the
   room). Each term lands in `Margin.terms` (the reason trail), unchanged machinery.
4. **Graded, recoverable effects.** Each converted row gains `writes_by_degree` / `emits_by_degree`
   (the existing columns). Default band map, used where the owning verb lane has not stated one —
   **the verb lane's row supersedes this default** (one owner per row):

   | band | writes | emits |
   |---|---|---|
   | Failure | none | `<verb>.failed` (a new kind per row, so the act is witnessed and can be retried) |
   | Partial | the effect at half magnitude where it has one (the `f(degree)` hook H-164 already names in `effects_economy.py::_rise`: `task_fraction: {Failure: 0, Partial: 0.5, Success: 1, Overwhelming: 1}`, one roster); for a finding, the claim at half confidence and the hand withheld (`_found_claims`' existing Partial shape); for a document, a flawed one (below) | the success kind |
   | Success | as today | as today |
   | Overwhelming | as today (13 measured Overwhelming at 0 of 284 at pool 2: nothing is hung on it) | as today |

   Magnitude rows read `res.degree` through that one fraction: `tend` (D-05), `work`, `restore`,
   `requisition` (the share of `amount` taken), `train` (Partial: no point, a `practice` mark the
   practice addend already reads), `recruit` (turnout; `14_VERBS_MILITARY` states its own map). Quality
   rows: `forge` and `conceal` write their band as the document's or cover's quality
   (`Record.forgery_quality = forge_quality[band]`, a roster replacing the constant
   `default_forgery_quality`; the examining draw already reads it as obstacle). Travel rows (`move`,
   `migrate`): Partial arrives one leg short, Failure stays (`travel.failed`).
5. **The classes, as decided here** (the verb lanes may move a row between `task` and `contest`; none
   may leave a consequential row unrolled):

   | class | rows |
   |---|---|
   | bookkeeping | `create_record`, `utter`, `commit`, `oblige`, `convene`, `dispatch`, `petition` (filing; the addressee's answer is his act), `give`, `transfer`, `exchange` (consent is each side's sampled choice), `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit`, `forgive`, `tie / knot`; rows writing nothing and finding nothing (`comply`, `construe`, `evade / defy`) are outside the refusal; their outcome is the obedience draw `14_VERBS_SOCIAL1_B` gives them |
   | task | `tend`, `train`, `recruit`, `work`, `restore`, `build`, `found`, `raze`, `sabotage`, `requisition`, `forge`, `conceal`, `survey`, `reconstruct`, `thread_read`, `move`, `migrate`, `open_case`, `carry`, `marshal`, `issue`, `destroy_record` |
   | contest (owed to the lane named) | `seize`, `confer`, `revoke`, `succeed`, `pardon`, `release`, `establish`, `surrender` (`14_VERBS_BINDING_*`); `interview`, `covenant`, `challenge` (13, `14_VERBS_SOCIAL*`) |

## Exact edits, by owner

1. `engine/season/rosters.yaml` — `graded_inquiries` renamed `graded_tasks`, the `task` rows added
   (one line each, the pair above); new rosters `bookkeeping_verbs` (`{verb: why}`), `task_fraction`,
   `forge_quality`; `default_forgery_quality` retired from `data/fixtures.py` (its reader reads
   `forge_quality`).
2. `engine/season/data/rosters.py` — `GRADED_TASKS`, `BOOKKEEPING_VERBS`, `TASK_FRACTION` exported;
   `GRADED_INQUIRIES` deleted (readers: `loop/resolve.py`, `manifest/registry.py`, `data/verbs.py`).
3. `engine/season/data/verbs.py` — the two refusals in item 1, at load.
4. `engine/season/verb_table.yaml` — for each `task` row: `writes_by_degree` / `emits_by_degree` per item
   4, and the `<verb>.failed` kind in `emits_on_refusal`'s neighbour column; `EVENT_KINDS` gains them.
5. `engine/season/loop/effects_*.py` — each magnitude/quality effect reads `res.degree` through
   `TASK_FRACTION` / `forge_quality`; no effect names a band.
6. `engine/season/loop/resolve.py` — `_route = GRADED_TASKS.get(a.verb)`; nothing else (the branch
   exists).
7. `engine/season/data/fixtures.py` — `task_draw_arm: on | off` (off = today's flat fold, the
   control), shipped `on` once the gate reads.

## Gate (execution artifacts)

1. Realm, `PYTHONHASHSEED=0`, seeds 0, 1, 2, two seasons each (the probe above, extended to print the
   band of each act): for every converted verb with ≥ 10 resolved acts, at least two bands occur, and
   no such verb is 100 % one band; success events carrying a degree rise from 164 to at least 90 % of
   non-bookkeeping success events.
2. Control: `task_draw_arm: off` reproduces `5ab73af282d0779646c38839fbab85d8` (seed 0, one season),
   `8aae8412c221edb44ffd45d91bae2671` and `891092133b77dfb4fc789fb9bd9446c2` (seeds 1, 2, two seasons).
3. Odds respond to state: `tend` by a tender holding `healing` 3 against `pool_default`, 200 planted
   `tend` acts each — the trained tender's Failure share is lower, and neither is 0.
4. Loader: plant `tend` into `bookkeeping_verbs` → load refuses naming `tend`; delete `reconstruct`'s
   route → load refuses naming `reconstruct`.

**Declared hash movers:** every realm, spine and case world in which a converted verb executes (all
goldens); re-pinned once, in the landing commit, saying so.

## Falsifier

A converted verb that resolves in one band in all of ≥ 10 acts at three seeds; a `bookkeeping` row that
writes another person's body, tenure or stores and loads; an effect that names a band literal.

## NERS reading

- **N**: from the top, the standing rule; from the bottom, the route, the roller, the band columns and
  the fraction hook all exist; laterally, `research` already works this way; diagonally, a tended man
  who stays wounded is a standing fact others can act on.
- **R**: a forgery's quality, a steward's mending, a journey's arrival become things that go wrong
  without a player; the extremes hold (Failure writes nothing and is witnessed; Overwhelming is
  today's write).
- **S**: one route, one roller, one fraction, one loader refusal; the methodology of a `tend` is that of
  a `research`.
- **E** (last): two rosters and a rename against 727 outcomes per five realm seasons brought under the
  rule.

## Cost class

Medium build (one loader refusal, one rename, about twenty band rows, five effects reading a fraction),
after 13's `difficulty` column for the obstacle's task term (it ships at `obstacle_default` without it).
