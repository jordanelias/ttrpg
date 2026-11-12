# VERBS SOCIAL1 · D — grievance and settlement: `forgive`, `challenge` beyond lane A, `carry` to a room, `commit` by degree

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-22, C-27) — `challenge`: MATTER emits `challenge.declined` at the due tick and writes no `Person.stance`; the challenger's satisfaction is his own later `forgive`. `commit` and `forgive` take the route shape with flat `writes:` (`U5c_VERBS_residue_and_governance_owner.md` §1). `carry`'s draw in §1 supersedes the docketing row of `13_SC_draw_for_unrolled_contests.md`.

Folded: 2026-11-12 by `audits/28_SCENE_ACCESS.md` (ruling A-64). Nothing here is deleted; four edges are named, the last under A-81 (no scene is still). (4) Two Failure bands here write nothing: §1's `carry` (*declined by the room*) and §4's `commit`. For `carry`, the declining band appends `(tick, "declined", act id)` to the petition Record's stages, so the paper carries its own history (`28_CORE_scene_access_C_the_petition_that_waits.md`, commit 4). For `commit`, a Failure on a Proposition whose `value` names another person deposits `commitment.refused` to that person where present, so one refused leave learns of it (`28_CORE_scene_access_B_appointments.md`, the A-81 table); that deposit is this lane's row to write. (1) §1's `carry` draw gains a leverage source on the carrier's side, `waiting`: one level per rebuff the log records of the petition carried (`28_CORE_scene_access_C_the_petition_that_waits.md` §2). `backlog` stays the obstacle term it is, so a much-rebuffed paper meets a full docket with both in the roll. (2) `carry.refused` (*declined by the room*) is one of the rebuff kinds that file counts, so this row's Failure is what later strengthens the same paper. (3) §4's drawn `commit` is the grant of an appointment when its Proposition is an ask for audience, and then carries a declared term (`28_CORE_scene_access_B_appointments.md` §2); §3's `challenge` and §2's `forgive` are two of the ways a petitioner kept waiting ends the matter, the first through the `dispute` conjunct once CR-88 counts his rebuffs as origins, the second by his own draw.

## Status: PROPOSED

Batch S1-D of `audits/14_VERBS_SOCIAL1.md` §14. Authored in part by Fable; completed by Opus after the
Fable usage limit (2026-11-12). Reference only (CLAUDE.md §0.05). Read at `84d2a02`. Needs S1-B (delivery,
`served`), lane A step 2 (the duel fires) and PHYSICAL's `accept`. Builds on `03_PC_duel_chain_reach.md`;
does not redesign it.

## What it changes in `engine/season/` at runtime

(1) A forgiveness mark that the one grievance reader honours, written by a drawn `forgive` that now forms on
any grievance. (2) `challenge` is drawn (the Record's `standing`), its `stakes` chosen by grievance size, its
Record answered by a due tick at which an unaccepted challenge is declined and the challenger's
satisfaction is drawn. (3) `carry` is drawn (admission to the docket) and names the venue and arrangement.
(4) `commit` is drawn and its band is the Tenure's `degree`. Declared hash mover.

## The problem, with evidence

- `forgive`: formed 2, attempted 0 (`aperture 1 0` and `[2s]`); it removes stance rows (`held_against`),
  which only `march` writes, while the grievance that drives `challenge` is `person_q.holds_dispute` over
  deed claims, which `forgive` never touches.
- `challenge`: a computed challenge carries `stakes: None` (H-229 limit 3); nothing resolves a challenge
  nobody accepts; its mint is certain (Standing rule).
- `carry`: the docket item names no arrangement (`_eff_carry`'s own [ASSUMPTION]); admission is certain.
- `commit`: every act that reaches the effect opens the edge — a fixed function of state; the row's
  `commitment.refused` is never emitted.

## The resolution, decided

### 1. `carry`

- `queries/world_q.py::petition_venue(w, actor, matter) -> (venue, arrangement) | None`: the first venue
  up the actor's containment chain (`place_of`, then rung ancestry) whose arrangement row has
  `admits_petition: true` (new key in `engine/season/arrangements.yaml`, default true on court rows,
  `data/arrangements.py` loader), skipping a venue whose docket already determined `matter` (appeal).
  `None` → the effect declines (`carry.refused`, reason `no room`), and person-side the act is not formed
  when he holds no claim of such a venue (`[UNVERIFIED]` a person-side venue claim exists; if not, the
  world-side decline stands and is the next link).
- Drawn: `verb_capability: carry: procedure` †; obstacle `plain` + `standard` (SC-OB, the arrangement's) +
  `reception` + `backlog` † (`backlog_step` × items on that venue's docket). Row Degree-keyed: Overwhelming
  / Success / Partial write as today plus the arrangement; the item's `date` is the next sitting (head of
  the queue at Overwhelming, one sitting later at Partial — `slot_for`'s existing dated slots); Failure
  writes nothing, emits `carry.refused` (reason `declined by the room`); the petition stays held.

### 2. `forgive`

- Formation: `rosters.yaml: own_stance_declines` reads `held_against(p, r)` **or** `holds_dispute(p, r)`
  (the one grievance owner; CR-88's `grievance_against` if it has landed) — inside CHAR-OFFER's one decline
  where landed.
- Drawn: `verb_capability: forgive: resolve` † (CHAR's `02_CHAR_resolve_and_temper.md` owns the key);
  obstacle `routine` + `grievance` † (`grievance_step` × |judged + told| from `deeds_judged`) + `scar`.
- Bands → mark factor via `forgive_factor_by_band` (`Overwhelming 0, Success 0, Partial 0.5`); Failure
  writes nothing, emits `forgive.refused` (reason `could not let it go`).
- The mark: `_eff_forgive` removes (or at Partial halves) the `held_against` rows and appends
  `(referent, 0.0, 0.0, tick, factor)` to `Person.stance`. `queries/person_q.py::forgiven_since(p,
  referent) -> (tick, factor) | None` reads the newest such row; `attributed_deeds` multiplies a deed
  claim's term by `factor` when `c.when <= tick` (it yields `(claim, factor)` pairs to `deeds_judged` and
  `world_q.reception`, its two summing readers — `[ASSUMPTION; medium]`: a signature change to a shared
  owner, both callers edited in the same commit; revert: a `Person.forgiven` dict). `stance_toward` and
  `held_against` read rows of length ≥ 3 and see 0 × 0; unchanged.
- At Overwhelming the Event names the forgiven as a second subject so WITNESS deposits it to him when
  present (`stance.moved`); his judgement of it is by authored `deed:stance.moved` cells.

### 3. `challenge` (on lane A)

- Drawn issue: pool `argue`; obstacle `plain` + `rank_gap` † (`rank_step` × max(0, the challenged's seat
  depth advantage)) + witnesses' mean `regard` of the challenger (favourable). Row Degree-keyed:
  Overwhelming / Success / Partial write the Record with `standing` 3 / 2 / 1 (new `challenge` key);
  Failure writes nothing and emits `challenge.refused` with reason `laughed off`, and an authored
  `deed:challenge.refused` cell makes witnesses judge it against the challenger.
- Stakes: `rosters.yaml: choice_sourced` `challenge: [stakes]` ranging `challenge_terms` `[yield, blood,
  death]`; `decision/choose.py` ranks the three by `stakes_by_grievance` (fixture: grievance magnitude bands
  → preferred term; control: every term ties, so the draw's tie-break picks, and `None` is no longer
  formed). The choice is the challenger's; the outcome stays the duel's draw (PHYSICAL).
- Answer window: `_eff_challenge` appends a stage `(served_tick + challenge_answer_ticks, "answer")` once
  `world_q.served(w, rid, to)` (S1-B) is True — at the give, or at a refused tender. At MATTER, a challenge
  Record whose `answer` stage matures with no `accept` naming it emits `challenge.declined` † (doer: the
  challenged), deposited to every holder of a claim of the challenge, judged by `deed:` cells scaled by
  `standing` (claim confidence). Then MATTER draws the challenger's satisfaction: pool `resolve`, obstacle
  `routine` + `grievance` − `standing` (favourable); bands → the same mark as §2 written on the
  challenger toward the challenged (factor 0 / 0 / 0.5; Failure no mark).
- After a fought duel, PHYSICAL's `accept` effect writes the same mark on both parties by its own outcome
  band (owner: PHYSICAL; named here).
- A second challenge on the same `to` while one is live is declined person-side (`held_document_declines`'
  shape over his held challenge Records).

### 4. `commit`

- Drawn: pool `resolve` †; obstacle `plain` + `cross_pressure` † (`cross_pressure_step` × his live commits
  to Propositions contrary to this one) + `violated` † (the Proposition's lean against his pursuits). Row
  Degree-keyed: Overwhelming / Success / Partial write the edge with `degree` = the band (the Tenure field
  `determine`'s `_disposal` already fills); Failure writes nothing and emits `commitment.refused`.
- `degree_weight` (fixture table, `Overwhelming 1.5, Success 1.0, Partial 0.5`): read by `faction_q`'s
  membership readers, `argue`'s `commitment` term (S1-C) and `covenant_in_force` (S1-B). A `commit` edge
  with `degree None` (seeded, pre-change) weighs 1.0.

## Exact edits, by owner, in landing order

1. `arrangements.yaml` / `data/arrangements.py`: `admits_petition`.
2. `rosters.yaml`: `verb_capability` (`carry: procedure`, `forgive: resolve`, `commit: resolve`,
   `challenge: argue`); `challenge` key `standing`; `choice_sourced` `challenge: [stakes]`;
   `obstacle_terms` (`backlog`, `grievance`, `rank_gap`, `cross_pressure`); `own_stance_declines`' reader
   note; `deed:` cells (`challenge.declined`, `challenge.refused`, `stance.moved`).
3. `data/fixtures.py`: `backlog_step`, `grievance_step`, `rank_step`, `cross_pressure_step`,
   `forgive_factor_by_band`, `stakes_by_grievance`, `challenge_answer_ticks`, `degree_weight` (NUMBER rows,
   controls named).
4. `verb_table.yaml`: rows `carry`, `forgive`, `challenge`, `commit` made Degree-keyed and contested; new
   kinds in their `emits:`.
5. `queries/person_q.py`: `forgiven_since`; `attributed_deeds`' factor; `queries/world_q.py`:
   `petition_venue`, the `reception` caller.
6. Effects: `_eff_carry` (venue, band date), `_eff_forgive` (mark), `_eff_challenge` (standing, stage),
   `_eff_commit` (degree; keep the `"commit"` literal for the opener walk); `loop/matter.py`: the `answer`
   maturation and the satisfaction draw (through the same seam roll; `[UNVERIFIED]` that MATTER may call the
   social roll — if not, the draw is the `challenge` row's own second resolution, owned by `loop/resolve.py`).
7. `decision/choose.py`: the stakes ranking.

## Gate (execution artifact)

- Planted grievance world (A holds a firsthand deed of B's judged against B; both co-located), 20 seeds:
  `forgive` resolves at ≥ 3 bands; after the ending bands `holds_dispute(A, B)` is False, after Partial the
  judged sum halves, after Failure it is unchanged; a later planted deed makes it True again.
- Same world with `challenge`: Records carry ≥ 2 `standing` values and a non-`None` `stakes`; in the arm
  where B does not accept, `challenge.declined` at the due tick in every seed whose challenge was served, and
  the satisfaction draw's band distribution moves with `standing`.
- `aperture 2 s`: every `petition.carried` item names an arrangement; `carry.refused` with reason
  `declined by the room` appears; `commitment.refused` > 0 and commit Tenures carry ≥ 2 degrees.

## Falsifier

A forgiveness at an ending band after which `holds_dispute` is still True (the mark is not read); a
challenge that is never served and never declines (the dead end remains); a docket item with `None`
arrangement; any of the four whose band distribution does not move when its named term moves. Control: all
new fixtures at control reproduce the S1-C hash except for the draws the rows now take.

## NERS reading

- **N:** a grievance must be endable without a duel, a challenge must resolve if refused, a petition must
  reach a named room, and a commitment must have a strength; each is now a draw.
- **R:** feuds start, are forgiven, are refused at a price, or end in blood, with nobody watching; a strong
  position still fails sometimes.
- **S:** one grievance reader for `forgive`, `challenge` and the duel's end; one mark; one roll.
- **E, last:** one mark, one stage and a band table per verb, against four verbs that today either never
  form or never resolve.

## Cost class

Small-to-medium build. Lanes: CHAR (`resolve`, the grievance owner), PC/PHYSICAL (`accept`'s mark), SC
(the seam operands), FA (arrangements), CORE (`choose`).
