# CHAR — the interior that moves: a season cap on the scar, one unit for regard, a bound on the stance term

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-06) — item 1 is amended by `02_CHAR_scar_is_a_wound.md` (F-CHAR-17: a cap per element bounds the rate, not the stock). There is one fixture `scar_season_cap` with the domain `None | element | person`; this file's cap is its `element` arm and its gate (*median per-person maximum ≤ 4*) is replaced by that proposal's (a share strictly between 0 and 1 at eight seasons), because the old gate passes while every person is in crisis. Items 2 and 3 and the Addendum stand; item 3 gains the `stance_scale` fixture of `U5a_CHAR_owed_amendments.md` §2.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (AMBIGUOUS, same pick as U1 §1, for the `regard_sign` column), §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` §3 *regard* (the stance row's unit), ledger S-13, S-14; `unified/U3_CONFLICT_LEDGER.md` C3-K3, C3-Y8; `unified/U3_DEPENDENCY_ORDER.md` node B10, §6.2). The body follows its head: item 1's gate (*median ≤ 4*) is replaced by `02_CHAR_scar_is_a_wound.md`'s (a share strictly between 0 and 1 at eight seasons) and the fixture's domain is `None | element | person`; the per-tick tally's reset site is settled at the tree (`loop/driver.py:468`, `w.draw = 0` at the start of each tick, the precedent; driver-local scratch, `04` PART D row 34); the Addendum's `regard_sign` column names its Layer 1 ambiguity at the site (`04` §B.13 against §C.4, picked as the column by U1 §1's reasoning; B4 third disposition) and carries `17_CENSUS_C1A_02` W4's term once (C3-K3); scratch probes marked; named tests; lands-it and tier.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5b_DONE.md` "For another lane", W3-2 item; `20_NARRATIVE_C_who_holds_what.md` edit 5): the Addendum's proposed first `regard_sign` values gain `-1` on `release` (the one row listing `tie` in its `domain:`; later tie-ending rows take it by the same reading). The W4 (`beneficiary`) carriage is unchanged: already here.

**Lands in batch:** B10, co-landing with `02_CHAR_scar_is_a_wound.md` (C3-Y8). **Depends on:** `U5a_CHAR_owed_amendments.md` §2 (B10, `stance_scale`).

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md`, findings F-CHAR-03, F-CHAR-04, F-CHAR-08).
Ratifies nothing. Reference under `CLAUDE.md` §0.05.

## What this changes in `engine/season/` at runtime

Three edits, each behind a fixture whose control value reproduces today's hash:

1. `loop/resolve.py::_scar_witnesses` writes at most one count per (person, element) per season at
   `scar_season_cap: element`, one per person at `person` (`02_CHAR_scar_is_a_wound.md`). Control `None`
   (uncapped, today).
2. `queries/person_q.py::regard` reads its judged and told halves in the stance row's unit, as
   `heritage_regard` already does. Control arm `regard_unit: raw` (today). Proposed live arm `stance`.
3. `decision/choose.py::stance_term` clamps the regard it reads to `±STANCE_MAX` before the gain.
   Control `stance_clamp: false` (today). Proposed live `true`.

Each is a declared hash mover when flipped. Nothing else moves.

## The problem, with evidence

**The scar runs away.** `ED-IN-0261` rules the thresholds: 1 destabilise, 2 weight shifts, 3+ crisis.
`_scar_witnesses` writes one count per observer per violated element per act, with no bound. Read on
`build_realm(0)`, two seasons, shipped chooser, `PYTHONHASHSEED=0`
(scratch `probe3.py`; `probe2.py` on the same seed and season count printed hash `bacd687f`; both not in
the repository, `main`'s readings): 83 of 83
persons hold a scar; the median of each person's largest count is **41**, the maximum 61; 83 of 83 are
at or over 3 on some element. A ladder whose top rung is 3 and which every person passes thirteen-fold
in two seasons separates nobody. Two of its three readers ship at their control (`scar_weight_shift`
0, `refusal_axis` None), so on the pursuit side the count is state no decision reads
(`research/by_lane/NPC_npc_cast.md` T-NPC-5, T-NPC-9; that file read 61 → 508 entries at 3+ after two
seasons at an earlier tree). The third reader is live and is fed by the runaway: the threshold-3
crisis (`loop/resolve.py::_conviction_crisis`) rewrote `Person.conviction` for **0 of 46** cast at seed
0 and **6 of 46** at seed 1 within two seasons (`probe2.py`, hashes `bacd687f`, `8aae8412`). A creed
folded or destroyed in two seasons by the ordinary acts of a realm at peace is the terminal rung of the
ladder reached as background noise.

The quarantined design carried the closer and the build dropped it. `systems/characters/sim/conviction.py`
(the retained oracle) holds `SCAR_SEASON_CAP_THREAD = 1`, citing *"Max 1 Scar per season from Thread
witnessing per NPC"* (`conviction_track_v1.md:90`, quarantined, intent only). In that design Thread
witnessing was the witnessing source; the season loop widened the source to every violating act of any
verb and kept no cap, so the reading here extends the design's cap to the widened source. `_scar_witnesses` has no such bound and its docstring calls the violation
predicate *"A CANDIDATE READING, NOT A RULING"*.

**Regard's three addends are in two units.** `regard = stance_toward + judged_gain·judged +
told_valence_gain·told + heritage_regard`. `stance_toward` is `valence × weight`, whole numbers up to
`STANCE_MAX` (25). `heritage_regard` is built in that unit on purpose: `heritage_gain · STANCE_MAX ·
mean(...)`, *"In `regard`'s own units"* (`person_q.py`, its docstring). `judged` and `told` are raw sums
of pursuit dot products (`deed_term`), *"the sum is unnormalised"* [ASSUMPTION, H-192]. Read after two
seasons at seed 0: of 2,070 cast (holder, person) pairs, 656 hold a regard that differs from stored
stance; the median size of the computed half is **0.051** and the maximum 12.9, on a ±25 scale. So what
a person has seen another do moves regard by about a five-hundredth of what one build-time loyalty step
moves it. Stored stance moved for 0 of 83 persons in the same run. The attitude half of R-07 is live in
code and imperceptible in size.

**The stance term has no ceiling.** H-339 (register line 6264) measured twenty grudges of weight 5
reading −60 against a stated scale of 25, and the chooser's term is unclamped. In the built realm the
term's variance across one person's candidates is 1.88 where it is non-zero against 0.008 for the
pursuit term (scratch `probe3.py`, 276 readings), so one stored row already outweighs the whole of a
person's values by two orders; an unbounded stack makes that worse without limit.

## The resolution, decided

| # | decided | ladder step |
|---|---|---|
| 1 | One scar per (person, element) per season, behind `scar_season_cap` | 3 (the design document gives the cap) and 4 (the oracle's `SCAR_SEASON_CAP_THREAD` is the precedent in the tree) |
| 2 | Judged and told halves counted in stance steps: each deed contributes the COSINE of the holder's projected pursuits against the deed kind's alignment row (in `[−1, +1]`; a paired deed's cosine times its `_bond`), so one deed is worth at most one valence step before the gain, and the sum is bounded by item 3's clamp | 4 for the unit (`heritage_regard`, CR-31, inside the same function, and `data/pursuits.py::pursuit_cosine_axes`, the one cosine); 3 for the size: `ED-IN-0335` rules that a major betrayal needs a series of events, so one deed must not outweigh a loyalty row and several must be able to |
| 3 | `stance_term` reads `clamp(regard, −STANCE_MAX, STANCE_MAX)` | 5 (the row type's own bound, `data/cast.py::STANCE_MAX`; a sum past the type's bound is a type error, not a tuning) |

The gains themselves (`judged_gain`, `told_valence_gain`, `stance_gain`, `hostile_stance_gain`) are
Jordan's shipped values and are not touched. Item 2 changes what the two regard gains multiply, so it
ships as a swept arm and its live flip is a declared mover read against the control at seeds 0–2.

## The exact edits, by owner

1. **`engine/season/data/fixtures.py`** — three rows, each with its hole-register row (the tree's
   declare · default · sweep discipline): `scar_season_cap` (default `None`, domain `None | element |
   person`, `02_CHAR_scar_is_a_wound.md`),
   `regard_unit` (default `raw`, arms on a new roster `rosters.yaml: regard_units: [raw, stance]`; the live
   arm `stance` is the one unit of regard, U1 §3),
   `stance_clamp` (default `False`).
2. **`engine/season/loop/resolve.py::_scar_witnesses`** — before the write, drop every (observer,
   element) pair (or person, at `person`) already counted this tick. The tally is a per-tick scratch on
   the driver, reset where the draw ordinal is reset at the start of each tick (`loop/driver.py:468`,
   `w.draw = 0`; `World.new_draw`, `state/world.py:1632`, *"reset at the start of every tick by
   `season()`"*): a local of the driver's step, not world state (`04` PART D row 34). No new `Person` field, no `write_matrix.yaml` row: the count written is still
   `(Person, scar)`.
3. **`engine/season/queries/person_q.py`** — `deed_term` and `deeds_judged` are unchanged (three other
   readers use the raw sums: `legitimacy`, `world_q.reception`, `holds_dispute`). A sibling
   `deed_steps(p, axis_w, c) -> float` returns the same deed's worth as a cosine:
   `pursuit_cosine_axes(axis_w, kind_row(c.predicate))` for an unpaired kind, that cosine times
   `_bond(p, c.subject, lean)` for a paired one, `0.0` where either vector is zero. `regard`, at arm
   `stance`, sums `deed_steps` over the same `attributed_deeds` walk `deeds_judged` takes (split by
   `firsthand` exactly as there) and reads `jg * judged_steps + tg * told_steps`.
4. **`engine/season/decision/choose.py::_stance_arm`** — at `stance_clamp`, clamp `r` (and the
   `legacy` arm's `stance_toward`) to `±STANCE_MAX` before the polarity sign.

## Gate (an execution artifact, §0.2)

- Scar: `02_CHAR_scar_is_a_wound.md`'s gate replaces this file's (C-U5a-06): seeds 0–2, eight seasons, the
  share of cast persons with some element at 3 or more lies strictly between 0 and 1 at the live arms (the
  old *median ≤ 4* rule passed while every person was in crisis). Named test there:
  `test_scar_stock.py::test_at_the_live_arms_the_share_at_three_lies_strictly_between_0_and_1`.
- Regard: `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`
  already prints pairs differing beyond stance (3,270 of 11,449 at shipped gains). The new reading is
  the size, not the count. Reading rule, stated before the run: at arm `stance`, after two seasons, the
  median computed half among pairs that hold one is at least 0.5 (half a valence step) and no pair's
  exceeds `STANCE_MAX`.
- Clamp: H-339's hand-set rows read ±50 at most through `stance_term` (2 × 25 at `stance_gain` 1);
  `build_realm(0)`'s one-season hash is EQUAL with the clamp on, because no shipped row stacks past 25
  (if it moves, a shipped row stacks, and that is a finding).
- Named tests (new, `engine/season/tests/test_regard_unit.py`): `test_one_deed_is_at_most_one_step_at_arm_stance`;
  `test_six_deeds_outweigh_a_loyalty_row_of_weight_two`; `test_stance_term_is_clamped`;
  `test_a_capped_witness_holds_one_count_for_five_sights`; the existing
  `engine/season/tests/test_told_by_channel.py::test_r07_…` stays green.

## Falsifier

A planted person who witnesses the same violating act five times in one season holds a count of 1 at
cap 1 and 5 at cap `None`. Two holders with opposite pursuits who each saw one deed hold regards of
opposite sign, of size at most `judged_gain` (one step times the gain) at arm `stance` and of the raw
size at `raw`; a holder who saw six such deeds holds a regard that outweighs a loyalty row of weight 2.

## NERS reading (§0.06)

- **N.** Cut the cap and the scar ladder stays decorative from every direction: bottom-up nothing reads
  it, top-down the conviction crisis fires on nobody for a reason, laterally `chronicle` shows numbers
  no rule ever used. Cut the unit fix and a witnessed betrayal weighs less than rounding.
- **R.** The no-player half is the point: a person who watches his lord act against what he holds
  should, over seasons, come to regard him differently and act on it without a player present. Complete
  at the extremes: the cap bounds the count, the clamp bounds the term.
- **S.** One unit for one sum (methodology consistent with `heritage_regard` and `teller_weight`'s
  `regard / STANCE_MAX`). The cap is per season, the loop's own tick, so it scales with the calendar.
- **E (last, as a ratio).** Three fixtures and about thirty lines buy a ladder that discriminates and
  an attitude a player can see move. No new carrier and no new event.

## Cost class

Small build. Shared files: `data/fixtures.py`, `rosters.yaml`, `hole_register.yaml`,
`loop/resolve.py`, `queries/person_q.py`, `decision/choose.py`.

**Lands it and tier.** The B10 batch with `02_CHAR_scar_is_a_wound.md`, an IN `valoria-author` session on
`sonnet` (`high`), closed by B10's `methodology-close` once. **Hash movers.** None at the controls; each flip
declared.

## Addendum — the sign of regard by the act's character (H-337, H-282)

**Problem.** `stance_term` negates regard only where the subject is the act's contested opponent
(`options.subject_is_opponent`: arrest, determine, fight, capture, march, speak, interrogate). Every
other row takes `+`. H-337 (register line 6240) measured +50 and −50 at stance ±25 for `challenge`,
`forge`, `conceal`, `interview` and `move`, so a friend is the likelier object of sabotage and a hated
man the least; H-282 (line 5552) measured the same for `petition` and `open_case` (a grudge lowers
them). The polarity is inferred from a column that says who is contested, and is silent on who is
harmed.

**Resolution, decided (ladder step 4, with the values left as content).** The sign becomes a column
of the row, read by `stance_term`, in the way `beneficiary:`, `subject_may_be_self` and
`counterparty_may_be_self` are columns of the row. **Layer 1, named at the site:** a verb column meets
`04` §B.13 (*a property of a roster member travels with the roster*) against §C.4 (*a verb needing more
columns is one the design has not finished thinking about*); the column is picked, as U1 §1 picks
`capability:`, because a loader default makes a missing value explicit and refusable (B4's third
disposition); `04` is not edited. This is the one term `17_CENSUS_C1A_02_wires_and_corrections.md` W4
(`beneficiary`) also carries: it is written once, here (C-U5a-16; C3-K3), and `20_NARRATIVE_C`'s
`holder_gain` arm is added after it in B38. The column: `regard_sign: +1 | -1 | 0`, on a closed roster
`rosters.yaml: regard_signs`. The loader's DEFAULT reproduces today exactly (`-1` where
`contested_against_subject()`, else `+1`), so adding the column moves no hash. Authoring a row's sign
is then verb-table content. Proposed first values, each [ASSUMPTION; medium; Jordan to correct; revert:
delete the cell]: `-1` on `challenge`, `sabotage`, `seize`, `raze`, `requisition`, `open_case`,
`petition` and `forge`, and on `release` (the row that ends a tie to its subject: uncontested, so under
`declared` it took `+regard` and a man was likelier to leave a lord he honours; `20_NARRATIVE_C` edit 5 and
its gate 4 read this cell; `release` is the one row whose `domain:` lists `tie`, `verb_table.yaml:1341`, so
any later row that ends a tie to its subject takes `-1` by the same reasoning); `0` on `interview`, `surveil`, `examine`, `research` and `move` (regard for a
person says nothing about whether to look into him or travel to him). `subject_is_opponent` keeps its
other reader, the self-subject decline, untouched.

**Edits.** `verb_table.yaml` (the column), `data/verbs.py::VerbRow` (the field and its default),
`rosters.yaml` (the roster), `decision/choose.py::_stance_arm` (`return row.regard_sign * r` under
`declared`; `legacy` and `regard` arms unchanged).

**Gate and falsifier.** With no cell authored the one-season hash is EQUAL. H-337's own probe re-run
(restated as `engine/season/tests/test_regard_unit.py::test_sabotage_on_a_hated_person_scores_positive_with_the_cell`):
at stance −25 the term for `sabotage` on the hated person is positive after the cell and negative
before. `engine/season/tests/test_told_by_channel.py -k g2` (H-194's falsifier) stays green.

## What it does not do

It does not arm `scar_weight_shift` or `refusal_axis`; those wait on the cap's reading (a shift read
off a runaway count would hit everyone at once). It writes no `Person.stance` row: opinion persistence
is CR-83's question, decided by measurement, and this proposal supplies the measurement's unit.
