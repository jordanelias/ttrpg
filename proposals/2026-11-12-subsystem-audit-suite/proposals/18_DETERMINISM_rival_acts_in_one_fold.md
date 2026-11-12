# 18 · DETERMINISM · C — when two acts in one RESOLVE want the same thing, a draw decides who comes first

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — the precedence draw is the one sampler's (A-5). Under Jordan's answer A-9 the fold orders scenes, so a rivalry group is a group of scenes and is re-ordered among the positions it holds. First reading for gate 1: reversing the hash order flips 1 of 175 round-0 acts (realm, seed 0; `audits/16_PESSIMIST_CORE.md` E-07). Layer 1: this fills `04` F.26 and keeps D-36 (rank never breaks a tie).

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
   (so no outsider moves) by a draw per act: `roll_net(pool, rng)` through the one roller, pool from the
   one pool reader (`sigma.faculty` for the act's verb), on `draw_factory(seed, tick)(actor,
   f"precedence:{a.id}")`; highest net first; a tied net is re-drawn on the same stream. The odds are
   the rivals' capabilities; the order is the draw.
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

1. Count: realm seeds 0, 1, 2, two seasons: rivalry groups formed (reported; the number decides whether
   this is live today).
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
- **S**: one roller, one pool reader; the fold's order rule is untouched outside the tie.
- **E** (last): one derived key, one re-order, one fixture.

## Cost class

Small build.
