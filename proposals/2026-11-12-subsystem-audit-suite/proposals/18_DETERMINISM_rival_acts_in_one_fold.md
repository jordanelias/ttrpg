# 18 · DETERMINISM · C — when two acts in one RESOLVE want the same thing, a draw decides who comes first

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — the precedence draw is the one sampler's (A-5). Under Jordan's answer A-9 the fold orders scenes, so a rivalry group is a group of scenes and is re-ordered among the positions it holds. First reading for gate 1: reversing the hash order flips 1 of 175 round-0 acts (realm, seed 0; `audits/16_PESSIMIST_CORE.md` E-07). Layer 1: this fills `04` F.26 and keeps D-36 (rank never breaks a tie).

Folded: 2026-11-12 by `audits/28_SCENE_ACCESS.md` (ruling A-64). Nothing here is deleted; one rivalry key is added and the Layer-1 sentence in the line above is narrowed for that key alone. (1) `rival_key` gains `("round", person)`: a person's own scene and every scene holding a face-to-face interaction that names him are one group, re-ordered by this file's rule, among the positions the group already holds. For that key the draw's pool is the untrained score with levels for office rank and a kept appointment, since a claim on a person's time has no skill of its own; the roller, the stream and the re-order are this file's (`28_CORE_scene_access_A_occupancy_and_precedence.md` §4). (2) *"keeps D-36"* holds for this file's own keys (a seat, a Record, a larder). For the person key A-64 makes office rank a weight of the draw and never a sort; the amendment to `04` PART D row 36 is APPLIED (2026-11-12, A-97, node `L1-A64`; `04:1065`). (3) Gate 1's count should report the person key apart: 2, 5 and 4 executed and 31, 48 and 26 attempted rounds with rival visitors at seeds 0, 1, 2 (two seasons; audit §1.3).

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row rival_acts (CONFORMS for this file's keys; the person key AMBIGUOUS), §2 rows person key and A-9, §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-K8; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-08; `unified/U3_DEPENDENCY_ORDER.md` §1 item 9, §4.1 row 33). Changed: (1) item 2 states the scene-group reading of A-9 and the landing order (`16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edit 1 first, then this, both B08); (2) the person key `("round", person)` folded above is added by `28_CORE_scene_access_A_occupancy_and_precedence.md` (its order commit 6, B28; the Layer 1 row 36 text that file once drafted as edit 8 is now applied, `L1-A64`, `04:1065`, and B28's own control, `precedence_level` `None`, is stated in that file); this file's B08 commit carries the seat, Record and larder keys only, and gate 1's person-key count is 28A's reading at B28; (3) the roll is the one sampler (A-5), the pool the one pool rule through `seam/wrappers/pool.py::faculty` (D-U1-08), the draw keyed through the one `Draw` owner (A-30), and a tie is re-drawn under a fresh key, not "on the same stream"; (4) tests named; (5) batch and tier lines. `04` is not edited. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "ordinary score" → "untrained score" (glossary *untrained score*).

Depends on: `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edit 1 (B08, the scene key; lands first); the one sampler (B05) and the keyed draw (B06). `28_CORE_scene_access_A_occupancy_and_precedence.md` (B28) depends on this file (§4.1 row 33, REV).
Lands in batch: B08 (lane IN), after `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edits 1-4; one re-pin at B08's close, shared with the scene order.
Tier: sonnet / high; the PART D row 36 text for the person key is Layer 1's (APPLIED, `L1-A64`, `04:1065`).

Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A64`, `unified/work/L1_PROPAGATION.md`): the "stays Jordan's" and "applied only by Jordan" clauses of the Folded and W3-5b lines and the Tier line are rewritten to the applied state. Row 36 now reads, for several scenes claiming one person's round, that office rank is a declared weight of a keyed precedence draw and never a sort key (`04:1065`); F.26 (`04:1227`) is amended to match. The line-3 sentence "keeps D-36 (rank never breaks a tie)" stays true for this file's own keys (a seat, a Record, a larder).

## Status: PROPOSED

Source: `audits/18_DETERMINISM_SWEEP.md` C-11. Standing rule: `AUDIT_BRIEF.md` (Jordan, 2026-11-12):
*"not 'the senior office always wins'"* and the task's *"fixed-order tie-breaks that decide outcomes"*.
Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

Only where two or more acts by different actors in one RESOLVE would write the same exclusive thing (a
seat-`hold` on one Office, a `hold` on one Record, the stores of one rung beyond its stock): their fold
order is set by a precedence draw instead of by the canonical content-hash order. Every other act keeps
its canonical position. Today's frequency is not measured; the gate's first artifact counts it. If
the count is zero at the shipped configuration, this changes nothing at runtime today and says so.

## The problem (evidence)

- `loop/resolve.py:51::_canonical_order` and `:1015`: acts fold in five strata, then a content-derived
  hash key; *"each act sees the world its predecessors left"* (S27.1).
- Scarcity is decided by that order. `_eff_requisition`'s docstring: *"two requisitions on one larder,
  and the second finds it short and emits `requisition.refused`"*. `_eff_succeed`'s: *"the first valid
  claim wins (a later one finds the seat held)"*. The same holds for `confer` onto one seat by two
  conferrers and `seize` of one Record by two warrant-holders.
- The hash key is uncorrelated with anything in the fiction and reads no capability: who gets the
  throne, the grain or the paper between two rivals is a fixed function of the acts' content, with no
  odds and no grade. Neither rival's strength, standing or right moves it.

## The resolution, decided

Ladder step 5 (the architecture: the fold's order semantics stay; only the tie between rivals is drawn).

1. **Rivalry key, derived, one owner.** `loop/resolve.py::rival_key(w, a) -> tuple | None`: for a row
   whose `writes:` open a seat-`hold` or a `hold` on a Record, `("hold", subject)`; for a row whose
   `writes:` debit `Rung.stores` of a rung the actor does not hold, `("stores", rung, kind)` only when
   the summed `amount` of the group exceeds the stock; else `None`. Read off the verb row and the act's
   operands; names no verb.
2. **Precedence draw.** Inside `_canonical_order`, after the stratum sort, each group of ≥ 2 acts by
   distinct actors sharing a rivalry key is re-ordered among the positions the group already occupies
   (so no outsider moves) by a draw per act: one draw through the one sampler (A-5,
   `roll_net_continuous`), pool from the one pool rule through `seam/wrappers/pool.py::faculty` for the
   act's verb (D-U1-08), keyed `H(seed, tick, actor, "precedence:" + a.id)` through the one `Draw` owner
   (A-30; B06); highest net first; a tied net (the margin is quantised to milli-units, C3-L1, so a tie is
   an exact equality) is re-drawn under the key `"precedence:" + a.id + ":" + str(n)` for the n-th
   re-draw. The odds are the rivals' capabilities; the order is the draw. **Under A-9 the fold orders
   scenes:** with `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edit 1 landed (first, in B08), a
   rivalry group is a group of scenes, re-ordered among the positions those scenes hold, and the
   act-level wording above applies as written only to a scene of one interaction. Both files edit
   `_canonical_order`; the scene order lands first.
3. **Graded consequences already exist downstream.** The first act folds and takes; the next finds the
   seat held or the larder short and is refused by the row's existing scarcity refusal (or, once the
   verb lanes land them, gets a Partial share through its own band). A refused rival's act is witnessed
   with its causes, so a contested succession is a story, not a silent loss.
4. **Reason trail.** The group's draws ride the trace (`TRACE.decision("rival precedence", …)`) and each
   act's Events' `observed` (`("precedence", net)`).

## Exact edits, by owner

1. `engine/season/loop/resolve.py` — `rival_key`, and the group re-order inside `_canonical_order`
   (shared with `loop/encounter.py` already, so one copy).
2. `engine/season/data/fixtures.py` — `rival_precedence: hash | draw` (`hash` = today, the control).

## Gate (execution artifacts)

Tests: NEW `engine/season/tests/test_rival_precedence.py`: `test_two_requisitions_on_one_larder_each_win_sometimes`
(gate 2, 200 seeds), `test_higher_pool_wins_more_often` (gate 2), `test_two_heirs_each_reign_in_some_seeds`
(gate 3), `test_hash_control_reproduces_base` and `test_no_group_world_is_byte_identical` (gate 4).

1. Count: realm seeds 0, 1, 2, two seasons: rivalry groups formed by this file's three keys (reported;
   the number decides whether this is live today). The person key's count is
   `28_CORE_scene_access_A_occupancy_and_precedence.md`'s reading at B28.
2. Planted: two persons, one larder of 4 grain, each `requisition` 4, 200 seeds: each wins in some
   seeds; the one holding the higher pool wins more often; neither share is 0 or 1.
3. Planted: two heirs whose titles both claim one vacant seat: each reigns in some seeds.
4. Control: `rival_precedence: hash` reproduces the base hashes; at `draw`, a world with no rivalry
   group is byte-identical to `hash`.

**Declared hash movers:** only worlds with a rivalry group.

## Falsifier

A rivalry group whose winner is the same at every seed; an act outside a group whose position moved.

## NERS reading

- **N**: S27.1's sequence stays; what goes is a tie-break nobody in the fiction could explain.
- **R**: a disputed throne, a fought-over granary, a document two men reach for — each now has odds a
  player can improve.
- **S**: one sampler, one pool rule; the fold's order rule is untouched outside the tie.
- **E** (last): one derived key, one re-order, one fixture.

## Cost class

Small build.
