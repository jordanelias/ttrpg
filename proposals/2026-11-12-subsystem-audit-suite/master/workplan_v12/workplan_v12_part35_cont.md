# Workplan v12 — part 35 (continued): Batch B28-social-verbs from B28.16; Batch B21s-strife-supply

## Status: PROPOSED (the continuation of `workplan_v12_part35.md`, written past that file's size cap, `V12_STRUCTURE_part2.md` §4.1; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

Short names, words and paths are the first file's head. The B28 block's head, its position table and its items B28.01 to B28.15 are in the first file; this file continues the same batch at B28.16 and holds its boundary row, then the whole of B21s.

---

### B28.16 — which rows engage their counterparty, read off the cell · 28A commit 1 · BUILD · HASH EQUAL
- SOURCE: 28A "The resolution, decided" §1; "Exact edits" 1 and 2; "Instructions to code it", row 1; the W3-2 Reconciled line (*occupy* → **engaged**; `ENGAGED_CLAUSE`; `VerbRow.engages`); rulings A-63, A-64 (1), A-80; `unified/U1_GLOSSARY.md` *occupy*.
- ADVANCES: none of the nine directly; A-63 (a visited person is engaged), A-80 (force is not kept waiting).
- INSTRUCTION (28A, copied):
  1. §1: "A row **engages its counterparty** when its typed cell asks the `with` relation of the operand its `counterparty:` column names. That is the cell's own statement that the two must be in one place. Today: `accept`, `argue`, `capture`, `challenge`, `give`, `lie`, `tell`. A paper (`petition`, `issue`), a conferral and an oath to a seat engage nobody. `covenant` joins the day its lane adds `with` to its cell … with no edit here. The counterparty must be an individual (`Person.is_cohort`, the owner the `individual` stem already reads, `queries/world_q.py`): a crowd is not engaged by one speaker." "**Force is not kept waiting (A-80).** A row whose prize is `the body` (`contests: "the body"`: today `accept`, `capture`; `fight` names no counterparty) asks for no one's attention. Such a row **intrudes**: it is never refused at `engaged`, whatever the target is doing, and when it is admitted the target is engaged in it if he was free … Read off the row's `contests:` cell, no verb named."
  2. Edit 1: "**`engine/season/data/verbs.py`** — `VerbRow.engages` (a derived property: `counterparty` set and the typed cell holds a `relation` conjunct `with` of that operand) and `VerbRow.intrudes` (`engages` and the row's `contests` is the prize `the body`: seats the target, never refused at `engaged`); `ENGAGED_CLAUSE = "engaged"` beside `COUNTERPARTY_CLAUSE`, *derived like the other two: a keyed row keys it iff it engages*; the loader's keyed-row rule adds it to the expected clauses." With `KEPT_WAITING_KINDS` (derived: the kinds declared at the `engaged` clause) and "the flat-row exemption list gains the kind" (row 1 of the coding table).
  3. Edit 2: "**`engine/season/verb_table.yaml`** — each of the seven engaging rows declares the one shared kind `visitor.kept_waiting` beside its own refusal kind (so loader invariant 7 derives it; `04` PART D row 25). A keyed row (`tell`) gains the key `engaged: ["tell.refused", "visitor.kept_waiting"]`. A flat row lists it second (`emits_on_refusal: ["argument.refused", "visitor.kept_waiting"]`) and the fold keeps it only at the `engaged` clause: `dispatch`'s `person.demanded` is the precedent for a kind a flat row declares and the act earns (`loop/resolve.py::_demand_earned`; the loader's flat-row exemption). No row is re-keyed." Row 1 of the coding table: "the flat lists of `argue`, `challenge`, `give` gain `"visitor.kept_waiting"`; the keyed rows `tell` and `lie` gain `engaged: […, "visitor.kept_waiting"]`; `accept`, `capture` unchanged (they intrude)". On this tree `lie` is keyed (B08.02) and `give` and `challenge` may be keyed by B28.02 and B28.06: each keyed engaging row gains `engaged:` listing its own refusal kind and `visitor.kept_waiting` (`tell`'s is copied as written; another keyed row's own kind is read off its row `[ASSUMPTION — basis: 28A's flat example lists the row's own refusal kind first]`), and each flat engaging row lists the kind second.
  4. Glossary: NEW row *engaged* (§D, beside *occupy*): "a person is engaged when he is already in a scene this lap, or has no scene action left, so a caller who wants his attention is turned away"; owner `data/verbs.py::ENGAGED_CLAUSE`, `VerbRow.engages` (T); rejected: "occupied" (A-66's army word). NEW row *intrude* (§D): "an act of force on a person that needs no hearing and is never turned away at the door"; owner `VerbRow.intrudes` (T).
- WHERE: `engine/season/data/verbs.py` (`VerbRow.engages`, `VerbRow.intrudes`, `ENGAGED_CLAUSE`, `KEPT_WAITING_KINDS`, the loader's keyed-row rule and flat-row exemption); `engine/season/verb_table.yaml` (`argue`, `challenge`, `give`, `lie`, `tell`); NEW `engine/season/tests/test_scene_access_engagement.py`; `unified/U1_GLOSSARY.md` (*engaged*, *intrude*).
- TESTS (28A coding row 1, in the new file, written before edit 1 and read red): `test_engages_is_read_off_the_cell_and_names_no_verb` ("the set equals the rows whose cell asks `with` of the counterparty; a planted row with the conjunct joins it"); `test_a_body_prize_row_intrudes_and_is_not_in_the_refusable_set`.
- FALSIFIER and CONTROL: an engaging set that names a verb rather than reading the cell; "A `capture` refused at `engaged`" (28A "Falsifier"). Control: "the fixture at `off` / `None` (hash EQUAL)" (28A): nothing reads the clause yet, so the seed-0 realm hash after one season equals B28.13's reading.
- GATE: `python -m pytest engine/season/tests/test_scene_access_engagement.py -q` → the two pass; `python -m engine.season.harness.register --check` → exit 0; seed-0 hash → equal to B28.13's.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `data/verbs.py::COUNTERPARTY_CLAUSE`, the keyed-row loader rule, `loop/resolve.py::_demand_earned`, `data/requires.py` (the `individual` stem reading `Person.is_cohort`); V12 Batch B08 (A-9's edits 1 to 4, 28A coding row 0: "prerequisite, not this batch"); V12 B28.02, B28.06 (the rows' refusal shapes on this tree).
- GLOSSARY: *engaged*, *intrude* (step 4).
- COST and TIER: small build; `sonnet`, `high` (28A "Lands by").
- LANDS IT: B28's producer; `Item: B28.16`, `[skip ci]`.

### B28.17 — the `engagement` setting and the driver's lap-local seat, deferral and receipt sets · 28A commit 2 · BUILD · HASH EQUAL
- SOURCE: 28A §2, §3; "Exact edits" 4, 5, 7 (its `engagement` half); coding row 2.
- ADVANCES: none of the nine; A-63 (both arms: the lap's seat and the season's debit, "one rule at two grains").
- INSTRUCTION (28A, copied):
  1. "**`engine/season/data/fixtures.py`** — `engagement: off | seat | seat_and_debit` (control `off`) … with a `hole_register.yaml` row graded `assumption`" (block slot 13). "The fixture has three values so the two arms can be told apart: `off`, `seat` (§2 only), `seat_and_debit` (§2 and §3)."
  2. Coding row 2: "`loop/driver.py::SeasonDriver`: `_engaged`, `_deferred`, `_received` (season/round locals, reset [with the other season locals] and at the top of the round loop), helper `_remaining(pid)`"; edit 4: "`remaining` built from the same expression `ask_budget` uses (one helper on the driver, called by both; at RESOLVE it hands `budget` the empty `View` the tests build, since `decision/budget.py` reads the person and the fixtures only); `engaged` emptied at the top of each round." §2: "The driver holds a round-local mapping `engaged: person id -> scene id`, emptied before each round's RESOLVE, filled by the fold, read once more by ENCOUNTER …, and never read after it (`04` PART D row 34's lifetime: dropped at the next barrier). It is in no carrier, no hash and no Event." ("round" is the lap throughout: NAMES.)
  3. Edit 5: "**`engine/season/loop/deliberate.py`** — `ask_budget` calls that helper" (the `ask_budget = lambda …: max(0, decision.budget(p, v, k_budget, w.fixtures) - self._spent.get(p.id, 0))` line in `loop/deliberate.py`).
  4. Glossary: row *engagement* (the setting): "whether, and how far, a visit takes up the person visited: not at all, for the lap, or for the lap and from his season's scenes"; owner `data/fixtures.py: engagement` (T).
- WHERE: `engine/season/data/fixtures.py` (`engagement`); `engine/season/loop/driver.py` (`SeasonDriver._engaged`, `_deferred`, `_received`, `_remaining`); `engine/season/loop/deliberate.py` (`ask_budget`); `engine/season/hole_register.yaml` (one assumption row); `engine/season/tests/test_scene_access_engagement.py`; `unified/U1_GLOSSARY.md`.
- TESTS: `test_engagement_off_reproduces_the_base_hash` (coding row 2: "seeds 0, 1, 2; realm, two seasons"; the source's three hash prefixes were read before A-9's re-pin and are not copied: the base is B28.16's reading, `reading @<sha>`), written before the edit.
- FALSIFIER and CONTROL: any hash moved at `engagement: off`. Control: that test.
- GATE: `python -m pytest engine/season/tests/test_scene_access_engagement.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B28.16; EXISTS-IN-TREE `loop/driver.py::SeasonDriver` (`_spent`, `_realised`, `_queued`), `loop/deliberate.py` (`ask_budget`), `decision/budget.py::budget`.
- GLOSSARY: *engagement* (step 4).
- NAMES: "round-local", "each round", "the round loop" → lap-local, each lap, the lap loop (B04.01); `scenes_per_round` → `scenes_per_lap`.
- IDS: H block slot 13 (`engagement`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.17`, `[skip ci]`.

### B28.18 — a call on an engaged person is refused; a received person's own scene waits · 28A commit 3 · BUILD · HASH EQUAL
- SOURCE: 28A §2; "Exact edits" 3 (its `_admits`, `_waiting_earned`, deferral and seating parts) and 4 (the re-queue); coding row 3; "INCOMPLETE" bullet 1 (commit 3's ENCOUNTER half), which `IS-B2-CORE-05` says order now supplies ("both exist after B24 (`HearingInput.speakers` and `bench`, settled in `05_SC_playable_hearing_B.md`'s Folded line), and B28 follows B24"); `IS-B2-SC-05` step (5) (UNDECIDED (U-7)).
- ADVANCES: A-63; `IS-B2-SC-05` step (5) (the negotiation's counterparty is engaged).
- INSTRUCTION (28A, copied): §2, "Walking the scenes in order:
  - **The opener.** If the scene's actor is already engaged in another scene, the whole scene is **deferred**: none of its acts enters the act store … or folds; the scene is handed back to the driver, which puts it at the head of that person's queue and withdraws the release debit (the inverse of [the `_spent` debit at release]). Precedent: `deliberate.py`, *"a queued scene is deferred, not dropped"*. Otherwise the actor is engaged in his own scene.
  - **The counterparty.** For an engaging act that has passed eligibility, its precondition and the counterparty clause: if the counterparty is engaged in another scene, or his budget Query reads 0, the act is refused at `engaged`. Otherwise the counterparty is engaged in this scene. Two interactions with one person in one scene seat him once.
  - **Across rounds** nothing is carried except what the engine already carries … A person received in round 2 is free again in round 3." "At `scenes_per_round` above 1 (swept, H-124) the rule reads 'in at most `scenes_per_round` scenes'." (lap; `scenes_per_lap`: NAMES.)
  Edit 3: "`resolve`: fills the driver's round-local `engaged`; the deferral of an engaged opener's scene (returned as `self._deferred`); `_admits` reads `engaged` and a `remaining(pid)` callable and asks the `engaged` clause after the counterparty clause. `loop/encounter.py` reads the same mapping and adds to it only for a sitting's attendees. A sibling of `_demand_earned`, `_waiting_earned(kinds, at_engaged)`, drops `visitor.kept_waiting` from a refusal at any other clause." Coding row 3: "`loop/resolve.py`: `_admits` (the `engaged` clause after [the counterparty clause]), `_waiting_earned`, the scene-level deferral in `resolve` (before `w.acts.append`), seating on admit"; call sites "`loop/driver.py::season` after `self.resolve(...)`: re-queue `_deferred` at the head of `_queued[actor]`, withdraw the release debit, drop its acts from the round's `acts` before [the promotion pass]; `loop/encounter.py`: read `_engaged`". An intruding row (B28.16) is never refused at `engaged` and seats its target if he was free. Every new reading is behind `engagement != off`.
  The ENCOUNTER half: a sitting's attendees (`HearingInput.speakers`, `bench`, B24) are engaged in the sitting for that lap; "an attendee already engaged elsewhere is absent, and the sitting's own `silence` rule applies to his side" (28B §5).
- WHERE: `engine/season/loop/resolve.py` (`_admits`, `_waiting_earned`, `resolve`: deferral, seating); `engine/season/loop/driver.py` (`season`: the re-queue after `self.resolve(...)`); `engine/season/loop/encounter.py` (reads `_engaged`; seats a sitting's attendees); `engine/season/tests/test_scene_access_engagement.py`.
- TESTS (coding row 3, written before the edit and read red at `engagement: seat`): `test_a_second_caller_is_refused_at_engaged_and_the_first_is_not`; `test_a_person_received_does_not_fold_his_own_scene_that_round_and_folds_it_the_next`; `test_a_capture_is_never_refused_at_engaged` (28A gate row 11: "planted: a host engaged in a scene of his own; one visitor's `tell` and another's `capture` on him, 200 seeds: the `tell` is refused at `engaged` whenever it folds after the host's scene; the `capture` is never refused at `engaged` and resolves by its own draw"; `assert checked >= 200`); `test_a_cohort_is_never_engaged`; and, for `IS-B2-SC-05` step (5), `test_a_negotiations_counterparty_is_engaged_in_the_sitting` `[ASSUMPTION: test name; this item creates it]`.
- FALSIFIER and CONTROL: "A received person who also folds a scene of his own in that round. A deferred scene that is neither released later nor still queued. A refusal at `engaged` whose counterparty was free." (28A.) Control: `engagement: off` → seed-0 hash equal to B28.17's.
- GATE: `python -m pytest engine/season/tests/test_scene_access_engagement.py -q` → pass; seed-0 hash at `off` → equal.
- HASH MOVERS: none at `off`.
- DEPENDS ON: V12 B28.17; EXISTS-IN-TREE `loop/resolve.py::_admits`, `::_demand_earned`, `loop/encounter.py`, `loop/driver.py::SeasonDriver.season`; V12 Batch B24, through B25 (`social_contest.hearing`, `HearingInput.speakers`, `bench`).
- GLOSSARY: none (B28.16's rows).
- NAMES: "round" (season's pass) → lap; `scenes_per_round` → `scenes_per_lap` (B04.01).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.18`, `[skip ci]`.

### B28.19 — the kept-waiting claim is about the host · 28A commit 4 · BUILD · HASH EQUAL
- SOURCE: 28A "Exact edits" 3, last bullet; coding row 4; "No scene is still (A-81)", the no-null-scene reading; rulings A-81.
- ADVANCES: A-81 (a refusal at `engaged` leaves a claim in two ledgers).
- INSTRUCTION (copied): "**The claim is about the host.** An `Event` has no subject (`state/carriers.py`; `04:402`); WITNESS takes a deposit's subjects from the actor, the changes and `epistemic.py::act_refs(act)`, which returns the act's `subject` operand only. For `tell` that is the topic. So `act_refs` gains a second argument, the Event, and for a kind in `data/verbs.py::KEPT_WAITING_KINDS` (derived: the kinds declared at the `engaged` clause) it also returns the operand the row's `counterparty:` names. The one call site passes the Event. Every other kind's deposits are byte-identical." Coding row 4: "`epistemic.py::act_refs(a, e=None)`"; call site "`loop/witness.py` passes the Event".
- WHERE: `engine/season/epistemic.py` (`act_refs`); `engine/season/loop/witness.py` (the one call site of `act_refs`); `engine/season/tests/test_scene_access_engagement.py`.
- TESTS (coding row 4, written before the edit and read red): `test_the_kept_waiting_claim_is_about_the_host_and_lands_in_two_ledgers` ("the no-null reading; mutation arm: the branch removed, red"); `test_every_other_kind_deposits_as_before` ("hash EQUAL at `engagement: off`").
- FALSIFIER and CONTROL: "A refusal at `engaged` that no `claim.deposited` Event cites (a still scene, A-81)." Control: "a unit arm with `act_refs`' new branch removed: the host-about claim is absent and the assertion goes red" (28A).
- GATE: `python -m pytest engine/season/tests/test_scene_access_engagement.py -q` → pass; seed-0 hash at `off` → equal to B28.18's.
- HASH MOVERS: none.
- DEPENDS ON: V12 B28.18, B28.16 (`KEPT_WAITING_KINDS`); EXISTS-IN-TREE `epistemic.py::act_refs`, its call site in `loop/witness.py`.
- GLOSSARY: NEW row *kept waiting*: "turned away at a person's door because he was already seeing someone, or had no time left"; owner the `visitor.kept_waiting` kind (T).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.19`, `[skip ci]`.

### B28.20 — a received scene costs the host one scene action · 28A commit 5 · BUILD · HASH EQUAL
- SOURCE: 28A §3 ("**(decided here: both arms of A-63, as one rule)**"); "Exact edits" 4 (the promotion); coding row 5; gate row 6.
- ADVANCES: A-63 (the *debited* arm).
- INSTRUCTION (28A §3, copied): "`SeasonDriver.season` already promotes realised acts into a season-local set after the fold (`_realised`); in the same pass it adds, for each admitted engaging act, the act's scene id to `self._received[counterparty]` (a set of scene ids, reset with the other season locals). `ask_budget` becomes
  ```python
  max(0, decision.budget(p, v, k_budget, w.fixtures) - self._spent.get(p.id, 0)
         - Scene.PLAIN_COST * len(self._received.get(p.id, ())))
  ```
  `decision/budget.py::budget` is not edited and gains no `World` (S26; AX-2). What is kept is the set of scenes that happened; the number is computed when asked … No gate write, no receipt, no `changes[]` on any Event. A received scene costs the host one scene action whatever it cost the visitor `[ASSUMPTION; medium; Jordan to correct; revert: the visitor's own `cost(ext)`]`." Coding row 5: "promote admitted engaging and intruding acts' scene ids into `_received[counterparty]`; `_remaining` subtracts `Scene.PLAIN_COST * len(...)` at `seat_and_debit`".
- WHERE: `engine/season/loop/driver.py` (`season`: the promotion pass; `_remaining`); `engine/season/tests/test_scene_access_engagement.py`.
- TESTS (coding row 5, written before the edit and read red at `seat_and_debit`): `test_the_budget_query_falls_by_one_per_scene_received_and_no_event_carries_it` (gate row 6: "`ask_budget()` read before and after a received scene differs by one; the log holds no Event with a budget change and no refusal Event with `changes[]` (A-62)"); `test_a_person_with_no_scene_action_left_receives_no_one`.
- FALSIFIER and CONTROL: an Event carrying the debit; a budget that does not fall. Control: `engagement: off` and `seat` → `_remaining` equals today's `ask_budget` (seed-0 hash equal to B28.19's).
- GATE: `python -m pytest engine/season/tests/test_scene_access_engagement.py -q` → pass.
- HASH MOVERS: none at `off`.
- DEPENDS ON: V12 B28.17 (`_received`, `_remaining`), B28.18; EXISTS-IN-TREE `state/carriers.py::Scene.PLAIN_COST`, `loop/driver.py::SeasonDriver` (`_realised`), `decision/budget.py::budget`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.20`, `[skip ci]`.

### B28.21 — office rank, and a precedence draw over the claims on one person's lap · 28A commit 6 · BUILD · HASH EQUAL
- SOURCE: 28A §4 and §5 (the three channels table); "Exact edits" 3 (`rival_key`'s key), 6 (`office_rank`), 7 (the two levels); edit 8's paragraph (the person key ships at control: `precedence_level` `None`; `L1-A64` APPLIED, `04` PART D row 36: "office rank is a declared weight of a keyed precedence draw (Jordan, A-64) and never a sort key: a lower rank is sometimes seen first"); coding row 6; U3 §1.1 serial instrument file `loop/resolve.py::_canonical_order` (C3-K8: B08's edits, then this key); rulings A-5, A-30, A-64 (1).
- ADVANCES: A-64 (1).
- INSTRUCTION (28A §4, copied):
  1. "**The group.** `loop/resolve.py::rival_key` (the function `18_DETERMINISM_rival_acts_in_one_fold.md` adds) gains one key: `("round", person)` for a scene whose actor is that person and for every scene holding an engaging act that names him. Groups that share a scene are merged. As in that proposal, a group is re-ordered **among the positions it already holds**, so no scene outside it moves. A member may thereby fold inside another stratum's run … A visitor drawn first who proves not to be where the host is is refused on `with`, seats nobody, and the host's own scene folds in its turn." The key is spelled `("lap", person)` (NAMES; B08's item names it so).
  2. "**The draw.** One net per scene, drawn once: `roll_net(pool_default, rng)` through the one roller (A-5), on `draw_factory(seed, tick)(actor, f"precedence:{scene id}")` (`04` PART D row 35: a keyed purpose, no counter), with levels added through the one leverage form (`U5c_SC_one_obstacle_form.md` §3, `levels_to_net_sigma`, the soft cap): one `precedence_level` per step by which the scene's actor stands above the lowest-ranked actor in the group, by **office rank**; one `appointment_level` where the actor holds a live appointment with a person the scene names (proposal B's reader `world_q.appointment_with`). Highest net first; a tied net is re-drawn on the same stream." The appointment level is added by B28.25; until then it is never added ("without it that level is never added and the rest stands", 28A "Dependencies").
  3. "**Office rank, one reader.** New `queries/world_q.py::office_rank(w, pid) -> int`: the highest `RUNG_KINDS.index(rung.kind)` over the rungs of the seats `pid` holds live, 0 for the seatless. It is the existing `rank` stem's ordinal … asked of a seat's rung, and it reads every seat held because a visit is an `own` act and carries no `Act.via` (the same reading, and the same `[ASSUMPTION]`, as limb 2 of `world_q.py::admits_audience`). `rank_gap` (`U5c_SC_one_obstacle_form.md` §2 member 6) calls it for an act with no `via`."
  4. "**The host is one of the claimants.** His own scene is in the group with his own office rank. … **(decided here)** Not chosen: the host's scene always first … and the visitor always first".
  5. Edit 7's levels: "`precedence_level` and `appointment_level` (`LEVEL_SIGMA` names; first values `minor` and `major`; control `None`, at which the group is ordered by the bare draw); each with a `hole_register.yaml` row graded `assumption`" (block slots 14, 15). Shipped `None` ("every commit of the order table ships with its fixture at the control so its hash is EQUAL, and the level flips to `minor` / `major` only in commit 8").
  6. Glossary: row *precedence draw* (B08.05's) gains the person key: "and which of the scenes claiming one person's lap folds first; office rank and a kept appointment are declared weights, never a sort"; NEW row *office rank*: "how high the highest seat a person holds stands on the ladder of rungs"; owner `world_q.office_rank` (T).
- WHERE: `engine/season/queries/world_q.py` (`office_rank`; `rank_gap`'s reader for an act with no `via`); `engine/season/loop/resolve.py` (`rival_key`: the `("lap", person)` key; `_canonical_order`: the precedence net); `engine/season/data/fixtures.py` (`precedence_level`, `appointment_level`); `engine/season/hole_register.yaml` (two assumption rows); NEW `engine/season/tests/test_scene_access_precedence.py`; `unified/U1_GLOSSARY.md`.
- TESTS (coding row 6, in the new file, written before the edit and read red): `test_the_higher_office_is_usually_first_and_never_always` (gate row 7: "planted: host of rank 4, visitors of rank 7 and rank 0, both present, 400 seeds: the rank-7 visitor is first more often; neither share is 0 or 1; the host keeps his own scene against the rank-0 visitor more often than not and loses it to the rank-7 visitor more often than not, neither with certainty"; run with `precedence_level` set in the test; `assert checked >= 400`); `test_the_host_is_a_claimant_on_his_own_round`; `test_precedence_changes_no_input_of_the_visits_own_roll`; `test_a_stance_sweep_leaves_every_precedence_net_unchanged` (gate row 8); `test_no_scene_outside_a_group_moves`.
- FALSIFIER and CONTROL: "A visitor of the higher rank first at every seed (a sort, not a draw)"; "A precedence net that changes when a stance row changes" (28A). Control: `precedence_level` `None` and `engagement: off` → seed-0 hash equal to B28.20's; `rank_step` 0 (B21's dial) leaves `rank_gap` at 0, so its new reader moves nothing.
- GATE: `python -m pytest engine/season/tests/test_scene_access_precedence.py engine/season/tests/test_rival_precedence.py engine/season/tests/test_scene_sequence.py -q` → pass (B08's two files guard the shared `_canonical_order`); seed-0 hash → equal.
- HASH MOVERS: none at control ("`precedence_level` or `appointment_level` other than `None` in a world with a rivalry group" is the declared mover, B28.29).
- DEPENDS ON: V12 Batch B08 (B08.03, B08.05: `_canonical_order` by scenes, `rival_key`, the group re-order); V12 Batch B05 (OBS §3: `levels_to_net_sigma`, the soft cap; the one roller); V12 B28.18 (engaging acts); EXISTS-IN-TREE `queries/world_q.py::admits_audience`, `engine/dice_engine/sigma_leverage.py` (`LEVEL_SIGMA`), `state/ids.py::draw_factory`, `loop/encounter.py` (inherits through `_canonical_order`).
- GLOSSARY: *precedence draw*, *office rank* (step 6).
- NAMES: `("round", person)` → `("lap", person)`; "one person's round" → one person's lap (B04.01); `roll_net` → the one sampler B05 left (B08.05 names it `sigma_leverage.roll_net_continuous`) `[ASSUMPTION — basis: B08.05's "one draw through the one sampler (A-5, `roll_net_continuous`)"]`.
- IDS: H block slots 14, 15 (`precedence_level`, `appointment_level`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.21`, `[skip ci]`.

### B28.22 — the access instrument · 28A commit 7 · BUILD · HASH EQUAL
- SOURCE: 28A coding row 7; gate rows 2 to 5, 9, 10, 12; U3 §6.2 (28A's scratch probes `face.py`, `occ.py`, `ordp.py`, "promoted into `harness/access.py`").
- ADVANCES: the instrument B28.29, B28.30 and the batch gate read (A-63's "measure before it ships").
- INSTRUCTION (copied): "`harness/access.py` (new instrument; `python -m engine.season.harness.access SEED SEASONS [--null-scenes] [--strata-cut]`): prints the readings of audit §1.3 and gate rows 2 to 5, 9, 10 and 12 from a run. It promotes this lane's scratch probes (`occ.py`, `face.py`, `ordp.py`); it adds no rule." The readings: executed acts and admitted face-to-face interactions against an `engagement: off` run (rows 2, 3); `visitor.kept_waiting` Events with their cause chains (row 4); scenes deferred, released later or still queued, by office rank, and individuals with a deferred scene who opened zero scenes (row 5); `seat` against `seat_and_debit` (row 9); `--strata-cut` (row 10, the scratch `ordp.py`'s arm); admitted calls by a lower office on a higher one (row 12's first clause); `--null-scenes`: "the count of scenes holding an act refused at `engaged` for which **no** `claim.deposited` Event cites the refusal". It reads a run through the builder B03c moved (`boot/realm.py`) and writes nothing. Its callers: this batch's BATCH GATE, B28.29, B28.30, and B38's 28C items (a named invocation in the plan, the accretion pass's step 1).
- WHERE: NEW `engine/season/harness/access.py`; `engine/season/tests/test_scene_access_engagement.py`.
- TESTS: `test_the_access_instrument_counts_a_planted_kept_waiting` ("one planted world; `assert checked >= 1`"), written before the instrument and read red (no module).
- FALSIFIER and CONTROL: the instrument prints 0 kept-waiting on the planted world that holds one. Control: a run of the instrument leaves the world's content hash and log length unchanged.
- GATE: that test → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.access 0 1` → exit 0, its lines printed (quoted in the commit body with its wall time).
- HASH MOVERS: none (an instrument).
- DEPENDS ON: V12 B28.18 to B28.21; V12 Batch B03c (`boot/realm.py::build_realm`).
- GLOSSARY: none.
- NAMES: `harness/populated.py` (the scratch probes' builder) → `boot/realm.py` (B03c, CI-07).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.22`, `[skip ci]`.

### B28.23 — the termed-promise table and the `appointments` setting · 28B commit 1 · BUILD · HASH EQUAL
- SOURCE: 28B "The resolution, decided" §1 (the table), §2 ("**(decided here)** `appointment_term = 2`"); "Exact edits" 1, 8; coding row 1; rulings A-64 (2) ("an appointment is a commitment between two persons (an existing kind), not a stored schedule; no Layer 1 clock").
- ADVANCES: A-64 (2).
- INSTRUCTION (28B, copied): edit 1: "**`engine/season/rosters.yaml`** — new closed table `termed_promises: {receives: {mood: OUGHT, term: appointment_term, asked_on: [visitor.kept_waiting]}}`, loaded and validated by `data/rosters.py` (`term` a fixture name; `asked_on` Event kinds the verb table derives). Adding a second termed promise later is a row." Coding row 1: "`data/rosters.py`: loader and constant `TERMED_PROMISES` (validates `mood` against the Proposition moods in use, `term` as a `Fixtures` name, `asked_on` against `data/verbs.py::EVENT_KINDS`); `data/fixtures.py`: `appointments` (`off` / `on`, shipped `off`), `appointment_term = 2`". "**(decided here) `appointment_term = 2`**, swept `1 / 2 / 3` `[ASSUMPTION; medium; Jordan to correct; revert: 1]`: at 1 a promise made in a season's last round is closed by the next MATTER before any round in which it could be kept." Register rows for `appointments` and `appointment_term` (block slots 16, 17). Glossary: NEW rows *appointment* ("a host's own termed commitment to receive a named visitor; while it is live the visitor is more often seen first"; owner `world_q.appointment_with`, B28.25) and *termed promise* ("a promise whose kind carries an end, so it lapses on its own when the term comes"; owner `rosters.yaml: termed_promises` (T)).
- WHERE: `engine/season/rosters.yaml` (`termed_promises`, at the end of its family's block); `engine/season/data/rosters.py` (`TERMED_PROMISES` and its loader); `engine/season/data/fixtures.py` (`appointments`, `appointment_term`); `engine/season/hole_register.yaml` (two rows); NEW `engine/season/tests/test_scene_access_appointments.py`; `unified/U1_GLOSSARY.md`.
- TESTS: `test_the_table_refuses_an_unknown_kind_and_an_unknown_fixture` (coding row 1), written before the loader and read red.
- FALSIFIER and CONTROL: the table loads a row whose `asked_on` names no derived kind. Control: "`appointments: off` (hash EQUAL)"; seed-0 hash equal to B28.22's.
- GATE: `python -m pytest engine/season/tests/test_scene_access_appointments.py -q` → pass; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: V12 B28.16 (`visitor.kept_waiting` is a derived kind); EXISTS-IN-TREE `data/verbs.py::EVENT_KINDS`, `data/rosters.py`.
- GLOSSARY: *appointment*, *termed promise*.
- NAMES: "a season's last round", "any round" → lap (B04.01).
- IDS: H block slots 16, 17 (`appointments`, `appointment_term`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.23`, `[skip ci]`.

### B28.24 — a commit to an ask carries a term · 28B commit 2 · BUILD · HASH EQUAL
- SOURCE: 28B §2 ("The term"; "**(decided here)** An appointment is standing leave for its term, not one slot"); "Exact edits" 2, 3; coding row 2; gate row 4; the W3-2 Reconciled line (`Tenure.term` on `commit` is "a check-only second pair exactly as on `oblige`").
- ADVANCES: A-64 (2).
- INSTRUCTION (28B, copied): "`_eff_commit` gives the new edge `Term(w.tick + n, a.id)` when the Proposition is a self-binding promise the table lists: `mood == OUGHT`, `subject == a.actor`, and `predicate` a key of `termed_promises`, `n` being the fixture that row names (`appointment_term`). Any other commit is untermed, as today. The edge is the host's own, opened by his own act (T-m); no one else's act opens or closes it, and nothing is scheduled: the end is a term the opening act declared, matured by MATTER at a season boundary (T-n; `04` PART D row 17's MATTER token), which is what `oblige` already does." Edit 2: "`_declared_term`'s `Term(w.tick + n, a.id)` shape (`loop/effects_governance.py`), moved to `loop/effects_shared.py` so both effects call one constructor"; coding row 2: "`loop/effects_shared.py::declared_term` (moved from `loop/effects_governance.py::_declared_term`); `loop/effects_information.py::_eff_commit`: the term for a self-binding promise the table lists"; call site "`loop/effects_governance.py::_eff_confer` imports the moved helper". Edit 3: "`engine/season/verb_table.yaml` `commit` — `writes:` gains `Tenure.term` (check-only, `oblige`'s and `confer`'s precedent: the fold gates exactly the pairs a verb declares; the second pair is check-only and the effect runs once, on the first …, so `NoOpReceipt` is not asked of it alone)"; coding row 2: "`writes: ["Tenure.since", "Tenure.term"]`" (on this tree the row is B28.08's flat shape (a) row; the pair is added to its flat `writes:`).
- WHERE: `engine/season/loop/effects_shared.py` (`declared_term`, moved); `engine/season/loop/effects_governance.py` (`_declared_term` removed; `_eff_confer`'s import); `engine/season/loop/effects_information.py` (`_eff_commit`); `engine/season/verb_table.yaml` (`commit`: `writes:`); `engine/season/tests/test_scene_access_appointments.py`.
- TESTS (coding row 2, written before the edit and read red): `test_a_commit_to_an_ask_carries_the_term_and_matter_closes_it` (gate row 4: "planted: a commit at tick t, `appointment_term` 2: the edge closes at the MATTER of tick t+2 with `tenure.closed` citing the commit; `appointment_with` is `None` after", the last clause read after B28.25); `test_any_other_commit_is_untermed_and_the_hash_is_equal`.
- EXPECTED RED UNTIL B28.25: the `appointment_with` clause of the first test, under `[skip ci]`.
- FALSIFIER and CONTROL: "A host's `commit` opened or closed by an act that is not his own, or by no act and no matured term. An appointment live past its term." Control: `_eff_confer`'s terms equal before and after the move (the moved helper is the same constructor); seed-0 hash equal to B28.23's.
- GATE: `python -m pytest engine/season/tests/test_scene_access_appointments.py -q -k "untermed or table"` → pass; seed-0 hash → equal.
- HASH MOVERS: none ("commit 2's `Tenure.term` on the `commit` row is check-only and moves nothing", 28B).
- DEPENDS ON: V12 B28.23, B28.08 (`commit` drawn; its degree); EXISTS-IN-TREE `loop/effects_governance.py::_declared_term`, `::_eff_confer`, `loop/effects_information.py::_eff_commit`, `loop/effects_shared.py`, `loop/matter.py` (the term branch), `state/carriers.py::Tenure` (`term`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.24`, `[skip ci]`.

### B28.25 — the appointment reads, and the precedence draw's second level · 28B commit 3 · BUILD · HASH EQUAL
- SOURCE: 28B §3 (the two reads, the outcomes table, "The level"); "Exact edits" 4, 6; coding row 3; gate rows 3 and 4's last clause.
- ADVANCES: A-64 (2).
- INSTRUCTION (28B §3, copied): "`queries/world_q.py`, beside `writs_held` (one owner each; nothing stored):
  ```python
  def appointment_with(w, host: str, visitor: str) -> Optional[Tenure]:
      """The host's LIVE `commit` to a termed-promise Proposition whose subject is `host` and whose value is
      `visitor`, or None. Read by the precedence draw (proposal A §4)."""

  def appointment_outcome(w, t: Tenure) -> str:
      """For such an edge, live or ended: `kept` (an admitted engaging act by the visitor naming the host,
      emitted within the edge's span); `withdrawn` (ended before its term: the host's `release`);
      `turned_away` (ended at its term, or still live, with a `visitor.kept_waiting` of that visitor at
      that host inside the span and no admitted visit); `unused` (ended at its term with neither)."""
  ```" "**The level.** In the precedence draw: `appointment_level` where the edge's `degree` is Overwhelming or Success; one `precedence_level` where it is Partial (a grudging leave)." Edit 6: "`engine/season/loop/resolve.py` — the precedence draw's second level (proposal A §4) calls `appointment_with`."
- WHERE: `engine/season/queries/world_q.py` (`appointment_with`, `appointment_outcome`); `engine/season/loop/resolve.py` (`_canonical_order`'s precedence net: the second level); `engine/season/tests/test_scene_access_appointments.py`.
- TESTS (coding row 3, written before the edit and read red): `test_the_appointed_caller_is_usually_first_and_never_always` (gate row 3: "planted: one host, two visitors of equal office, one holding an appointment, 400 seeds: the appointed visitor is first more often; never always"; `appointment_level` set in the test; `assert checked >= 400`); `test_each_outcome_class_is_reachable_in_a_planted_world`.
- FALSIFIER and CONTROL: "`appointment_level` added for a visitor with no live edge. An outcome class that cannot occur at any seed in the planted worlds." Control: `appointment_level` `None` → seed-0 hash equal to B28.24's.
- GATE: `python -m pytest engine/season/tests/test_scene_access_appointments.py engine/season/tests/test_scene_access_precedence.py -q` → pass (B28.24's red clause turns green).
- HASH MOVERS: none at control.
- DEPENDS ON: V12 B28.24, B28.21 (the precedence net); EXISTS-IN-TREE `queries/world_q.py::writs_held`.
- GLOSSARY: *appointment*'s owner (B28.23) now resolves to `world_q.appointment_with`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.25`, `[skip ci]`.

### B28.26 — a person kept waiting can ask for an audience · 28B commit 4, with B28.01's design · BUILD · HASH EQUAL
- SOURCE: 28B §1 ("Who forms it", "How it reaches the host", "Its draw"); "Exact edits" 5; coding row 4; "INCOMPLETE" bullets 1 and 2; B28.01's design file (its (5)); gate row 5.
- ADVANCES: A-64 (2).
- INSTRUCTION (28B §1, copied): "`Proposition(mood="OUGHT", subject=<host>, predicate="receives", value=<visitor>)`. The predicate and its mood live in one new closed table, `rosters.yaml: termed_promises` (edit 1), read by every site below; no site spells the string." "**Who forms it.** A person holding his own firsthand claim that he was kept waiting at that host's door (proposal A's `visitor.kept_waiting`: the claim WITNESS deposits is about the host, and he is its doer). `decision/options.py` derives the `said` cell from that claim through the operand derivation `14_VERBS_SOCIAL2_B_a_word_with_content.md` §1 adds for `utter` (*"a person says what he holds"*): a claim of a kind listed in `termed_promises.<predicate>.asked_on` yields `Said(host, "receives", actor)` in the `OUGHT` mood." Coding row 4: "`decision/options.py::_derive_operand`: the `said` for an ask, from a held claim of a kind in `asked_on`"; call sites "none (`operand_bags` already calls it)". "**Its draw.** `utter`'s own (S2-B §1: whether the room believes him)." The derivation is read only at `appointments: on` `[ASSUMPTION: the setting gates the ask's formation — basis: 28B "With the new fixture `appointments` at `off` (the control): nothing"]`. Then B28.01's answer: if its (2) states a reach term at `questions_for`, it is written here as the design states it, behind its own control; if (3), no edit and its named test.
  **STOPS IF** B28.01's design is unmerged at this item's turn: the item is `HELD (B28.01's design unmerged)` and leaves for the held list at the expunge (D-18); B28.27 does not depend on it.
- WHERE: `engine/season/decision/options.py` (`_derive_operand`: the ask's `said`); `engine/season/queries/world_q.py` (`questions_for`, only if B28.01 (2) says so); `engine/season/tests/test_scene_access_appointments.py`.
- TESTS (coding row 4, written before the edit and read red): `test_a_person_kept_waiting_can_form_the_ask_and_one_who_was_not_cannot`; `test_two_hosts_alike_but_for_stance_grant_at_different_rates` (gate row 5: "planted: two hosts alike but for their stance toward the asker (minimum, maximum), 400 seeds: the grant rates differ; neither is 0 or 1"; `assert checked >= 400`); B28.01's `test_the_host_has_the_ask_as_a_commit_referent` if its (3) holds.
- FALSIFIER and CONTROL: an ask formed by a person who holds no kept-waiting claim; gate row 5's two rates equal. Control: `appointments: off` → seed-0 hash equal to B28.25's.
- GATE: `python -m pytest engine/season/tests/test_scene_access_appointments.py -q` → pass.
- HASH MOVERS: none at `off`.
- DEPENDS ON: V12 B28.01 (the design), B28.25, B28.19 (the kept-waiting claim is about the host); V12 Batch B25 (`14_VERBS_SOCIAL2_B` §1: typed `utter`, the `holds` conjunct and the `mood` operand); EXISTS-IN-TREE `decision/options.py::_derive_operand`, `::operand_bags`.
- GLOSSARY: NEW row *ask for an audience*: "an uttered request that a named person receive the speaker; the host grants it by his own commitment"; owner `termed_promises.receives` (T).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.26`, `[skip ci]`.

### B28.27 — the chronicle tells what became of an appointment · 28B commit 5 · BUILD · HASH EQUAL
- SOURCE: 28B "Exact edits" 7; coding row 5; the outcomes table of §3.
- ADVANCES: A-64 (2) (the chronicle reads kept, withdrawn, turned away, unused).
- INSTRUCTION (copied): "`harness/chronicle.py`: one line class per `appointment_outcome`; `harness/access.py`: the four outcome counts". Per the §3 table: kept → "nothing more: the meeting's own bands"; withdrawn → "a witnessed vow-break, judged by those who hold it through `person_q.deeds_judged` (authored `deed:commitment.ended` cells)"; turned away → "the visitor's grievance clause (proposal C §2)" (B38); unused → "the term's `tenure.closed` is in the log, citing the host's commit; the chronicle tells it; no rule adds a penalty".
- WHERE: `engine/season/harness/chronicle.py` (the appointment line classes); `engine/season/harness/access.py` (the four outcome counts); `engine/season/tests/test_scene_access_appointments.py`.
- TESTS: `test_the_chronicle_prints_an_appointment_line_for_a_planted_lapse` (coding row 5), written before the edit and read red.
- FALSIFIER and CONTROL: a planted lapse with no chronicle line. Control: instruments only: seed-0 hash equal to B28.26's.
- GATE: that test → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B28.25 (`appointment_outcome`), B28.22 (`harness/access.py`); EXISTS-IN-TREE `harness/chronicle.py`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B28's producer; `Item: B28.27`, `[skip ci]`.

### B28.28 — arguing a proposition one does not hold stays allowed · H-286 · BUILD · HASH EQUAL
- SOURCE: the intake `:441` (H-286, STILL-NEEDED, rows E8:78; carry-forward `master/eval/E8.md` CF-E8-3, line 183; "lane's target: SC lane, join B28 (it edits the `argue` row); editorial, no hash"); E8's INSTRUCTION for H-286, copied; CLAUDE.md §0 ladder step 5; placed at the batch's tail by `V12_STRUCTURE_part2.md` §5.6's third rule (no member names H-286), ahead of the two measurement items (UNDECIDED (U-6)); closes H-286.
- ADVANCES: none of the nine; a stated rule the register row asks for ("`unblocks:` a stated rule, either that argument requires holding the claim or that it need not").
- INSTRUCTION (CF-E8-3, copied): "(H-286) close H-286 at CLAUDE.md §0's ladder step 5 [ASSUMPTION: arguing a claim one does not hold stays allowed, because `lie` is the separate verb that deceives and the hearing proposals let a third party speak for a cause (`05_SC_playable_hearing.md`); basis: no session item requires holding] by correcting the `argue` row's `beneficiary_note` and the register row, text only." In the tree: `verb_table.yaml` row `argue`, `beneficiary_note` ("… THE ARGUER -- he argues for what he holds right; the hearer is the counterparty, not the party served"): "he argues for what he holds right" becomes "he argues a Proposition whether or not he holds it (H-286, ruled at CLAUDE.md §0's ladder step 5 [ASSUMPTION]: `lie` is the verb that deceives; a third party may speak for a cause)". `hole_register.yaml` row H-286 (`kind: "RULING"`): `default:` `"none"` → `"NO -- arguing a Proposition one does not hold stays allowed (`lie` is the separate verb that deceives; the hearing lets a third party speak for a cause) [ASSUMPTION; ladder step 5; revert: a `holds` conjunct on `argue`'s typed cell]"`, the shape the register's other decided RULING rows take (their `default:` states the ruling, e.g. H-row `default: "`remit:determine`, V2's value, …"`); its other fields kept.
- WHERE: `engine/season/verb_table.yaml` (`argue`: `beneficiary_note`); `engine/season/hole_register.yaml` (H-286: `default:`).
- TESTS: none new (text only; E8: "H-286 none (a ruling text)").
- FALSIFIER and CONTROL: a code or data value other than the two text fields changes. Control: seed-0 hash equal to B28.27's; `register --check` exit 0.
- GATE: `python -m engine.season.harness.register --check` → exit 0; `git diff --stat HEAD~1 -- engine` → two files, text fields only.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `verb_table.yaml` row `argue` (`beneficiary_note`), `hole_register.yaml` row H-286; V12 B28.10 (the `argue` row's other edits land first).
- GLOSSARY: none.
- COST and TIER: edit; `haiku` (E8: "H-286 haiku"), or the batch's `sonnet` producer if one dispatch is cheaper (CLAUDE.md §10's arithmetic).
- LANDS IT: B28's producer; `Item: B28.28`, `[skip ci]`.

### B28.29 — scene access measured; engagement and precedence switched on if the rows pass · 28A commit 8 · BUILD · HASH MOVER(behaviour), if the flip fires
- SOURCE: 28A coding row 8 ("the measurement: run rows 2, 3, 5, 9, 10, 12 of the gate on seeds 0 to 4; flip `engagement` to `seat_and_debit` and the two levels to `minor` / `major` only if rows 2, 3, 5 and 12 pass; one declared re-pin"); the gate table; edit 8's paragraph; "INCOMPLETE" bullet 2 (the floors are seeds); `IS-B2-CORE-05` BLOCKED (CONTENT): "the floors are written into the test only after that reading, as its measured values with a stated tolerance"; U3 §1 item 28 ("Gate: 28A's twelve rows"); A-114 (two seasons).
- ADVANCES: A-63, A-64 (1) in play; R-04 contributor.
- INSTRUCTION:
  1. Run, `PYTHONHASHSEED=0`, realm, seeds 0 to 4, **two seasons** (four in the source; row 12 six; A-114), `python -m engine.season.harness.access SEED 2` at `engagement: off` and at `seat_and_debit` with `precedence_level: minor`, `appointment_level: major`, and `--strata-cut`, and record in the commit body the readings of gate rows: 1 ("control: `engagement: off` — content hash equal to the pre-edit tree at every seed"), 2 ("executed acts, `seat_and_debit` against `off` — not below 95% at any seed"), 3 ("admitted face-to-face interactions, `seat_and_debit` against `off` — not below 60% at four seeds of five"), 4 ("`visitor.kept_waiting` Events — above zero at every seed, each with a cause chain to its act"), 5 ("scenes deferred; of those, later released or still queued at season end — reported by office rank; **no individual with a deferred scene opens zero scenes that season**"), 9 ("`seat` against `seat_and_debit` — reported: the persons for whom they differ are those with budget below the round count"), 10 ("DELIBERATE's permutation falsifier (`engine/season/tests/test_rem31_grid_suspension.py`) and the strata-cut arm — the first unchanged; the second reported"), 12, first clause (`appointments: off`: "admitted calls by a lower office on a higher one fall toward zero (reported)"; the story-census clause is B38's, UNDECIDED (U-5)).
  2. The floors (`IS-B2-CORE-05` CONTENT): the 95 % and 60 % of rows 2 and 3 are seeds `[ASSUMPTION; medium; Jordan to correct]` (28A); the measured readings and their seed-to-seed spread are written into `test_scene_access_engagement.py` as `test_the_access_floors_hold_at_their_measured_values` `[ASSUMPTION: test name]`, each floor at its measured value with the spread as its stated tolerance, beside the source's seed, and the PR body lists both for Jordan.
  3. If rows 2, 3, 5 and 12's first clause pass: flip `engagement` to `seat_and_debit` and `precedence_level` / `appointment_level` to `minor` / `major` in `data/fixtures.py`, each `[JUSTIFIED: …]` tag naming the control (`off`, `None`) and the revert. If any fails: no flip; the commit body names the row; the three settings stay at control and join B98 (`DIALS AT CONTROL`), and "A run that misses row 3 is answered by `precedence_level` and by the formation proposals, not by raising `scenes_per_round`" (28A).
  4. The re-pin is B28.99's (E-1), not this commit's.
- WHERE: `engine/season/data/fixtures.py` (`engagement`, `precedence_level`, `appointment_level`: the flip, if it fires); `engine/season/tests/test_scene_access_engagement.py` (the floors test).
- TESTS: `test_the_access_floors_hold_at_their_measured_values` (step 2), green at the flipped tree; the twelve-row tests of B28.16 to B28.22 stay green.
- FALSIFIER and CONTROL: "Gate 3 at or below the crude arm" (28A: "the crude host-always-first arm reads 46% to 50%"); a flip with a failed row. Control: row 1 (the `off` arm hash-equal at every seed).
- GATE: the readings of step 1 in the commit body, each with its expected reading above; `python -m pytest engine/season/tests/test_scene_access_engagement.py engine/season/tests/test_scene_access_precedence.py -q` → pass; `python -m pytest engine/season/tests/test_rem31_grid_suspension.py -q` → pass (row 10's first arm).
- EXPECTED RED UNTIL B28.99: the realm pins, if the flip fires, under `[skip ci]`.
- HASH MOVERS: "`engagement` other than `off`; `precedence_level` or `appointment_level` other than `None` in a world with a rivalry group" (28A) — "22, 37 and 25 such rounds in two seasons at seeds 0, 1, 2" in the source's tree. Declared; B28's one re-pin.
- DEPENDS ON: V12 B28.16 to B28.22, B28.25; EXISTS-IN-TREE `engine/season/tests/test_rem31_grid_suspension.py`; V12 Batch B11 (`14_VERBS_SOCIAL1_A_formation.md`: "before that there are too few meetings to read", 28A "Gate").
- GLOSSARY: none.
- NAMES: "the round count" → the lap count; `scenes_per_round` → `scenes_per_lap` (B04.01).
- COST and TIER: reading and edit; `sonnet` runs, `opus` reads each row against its expected reading (the flip is a judgment node).
- LANDS IT: B28's producer; `Item: B28.29`, `[skip ci]`; instrument wall time quoted (CHECKPOINTS AND BASELINES: sized on one seed first).

### B28.30 — appointments measured; switched on if asks reach hosts · 28B commit 6 · BUILD · HASH MOVER(behaviour), if the flip fires
- SOURCE: 28B coding row 6 ("the measurement (gate row 2) and the flip of `appointments` to `on`; one declared re-pin"); gate rows 1, 2, 6, 7; the paragraph after the gate ("If row 2 reads zero at every seed …"); A-114.
- ADVANCES: A-64 (2) in play.
- INSTRUCTION:
  1. Run, `PYTHONHASHSEED=0`, realm, seeds 0 to 4, **two seasons** (four in the source; A-114), proposal A at the setting B28.29 left, `appointments: on` and `off`, and record: row 1 ("control `appointments: off` — hash equal at every seed"); row 2 ("asks uttered above zero at three seeds; hosts' commits to them above zero at two; outcomes reported in the four classes"); row 6 ("`World.dates` holds the same entries with `appointments` on and off in the planted world; no carrier gains a field"); row 7 (`python -m engine.season.harness.access SEED 2 --null-scenes`, seeds 0 to 4: "0 scenes holding an ask or a grant with no gate write and no `claim.deposited` citing them; control: the planted grant with `_eff_commit`'s write removed reads 1").
  2. If row 2 passes: flip `appointments` to `on` (`[JUSTIFIED: …]` naming the control `off` and the revert). "If row 2 reads zero at every seed, the shipped chooser does not reach the personal route. That is reported as the result; the docket route (§5) then carries A-64 (2) alone, and no further build is started from this file." Between the two (asks but no grants at two seeds): no flip, and B28.01's falsifier (4) is read and quoted.
  3. The re-pin is B28.99's.
- WHERE: `engine/season/data/fixtures.py` (`appointments`, if the flip fires).
- TESTS: the appointment tests of B28.23 to B28.27 stay green; row 6 as `test_no_schedule_is_written_with_appointments_on` in `test_scene_access_appointments.py` `[ASSUMPTION: test name]`, written before the run.
- FALSIFIER and CONTROL: "A host's `commit` opened or closed by an act that is not his own …" (28B "Falsifier"); a flip with row 2 failing. Control: row 1.
- GATE: the readings of step 1 in the commit body; `python -m pytest engine/season/tests/test_scene_access_appointments.py -q` → pass.
- EXPECTED RED UNTIL B28.99: the realm pins, if the flip fires, under `[skip ci]`.
- HASH MOVERS: "`appointments: on` in a world where a host commits to an ask" (28B). Declared; B28's one re-pin.
- DEPENDS ON: V12 B28.29, B28.23 to B28.27.
- GLOSSARY: none.
- COST and TIER: reading and edit; `sonnet` runs, `opus` reads.
- LANDS IT: B28's producer; `Item: B28.30`, `[skip ci]`.

### B28.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; S1-B, S1-C, S1-D "Cost class" ("Declared re-record of the season pins"); 28A and 28B "Cost class" ("Golden re-record … say so plainly in the commit").
- ADVANCES: the batch's REQUIREMENT line (the four `BUILT OUT` verbs; R-03.a; `IS-B2-SC-01` step 9).
- INSTRUCTION: (1) re-record, once, the realm pins in `engine/season/tests/_realm_goldens.py` and every seeded result the items above declared moved, read against the base this batch rebased on in S17 (`reading @<sha>`); the commit says "re-pin: behaviour (B28.02 to B28.12 the drawn social rows; B28.13 where `sitting_exchanges` is above 0; B28.29, B28.30 if their flips fired)". (2) Write the readings of the BATCH GATE into the commit body and the conjuncts' `reading:` records in `engine/season/requirements.yaml` (`IS-A-12`; `status:` not edited). (3) Append the batch's 17 register rows from its H block once, in merge order (`V12_STRUCTURE_part3.md` §7.6), if the items did not each write their own.
- WHERE: `engine/season/tests/_realm_goldens.py`; the pinned digests the items name; `engine/season/requirements.yaml` (`reading:` records only); `engine/season/hole_register.yaml` (if step 3 applies).
- TESTS: the full gates the BATCH GATE names, once (CLAUDE.md §0.4).
- FALSIFIER and CONTROL: a pin moved that no item declared; a behaviour tally moved where every item said EQUAL (B28.01, B28.16 to B28.28). Control: B28.28's seed-0 hash equal to B28.27's (EQUAL items did not move it).
- GATE: the BATCH GATE, read once on this commit's tree.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: B28.01 to B28.30.
- GLOSSARY: the close reads every glossary row the items named against the code (STAGES rule 2).
- COST and TIER: reading; `sonnet` runs; the close's terminal critique `opus`.
- LANDS IT: B28's producer; `Item: B28.99`, the batch's last `Item:` commit, without `[skip ci]` (CI's first run of the batch).

| STOP. Batch B28-social-verbs closes here |

---
