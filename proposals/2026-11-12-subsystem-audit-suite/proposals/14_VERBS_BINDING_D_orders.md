# VB-D — an order orders something, goes down the chain, and takes hold by a draw

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-25) — the prize `an order` is not added: `issue` and `dispatch` contest `a standing` (same hearer, same step; `U5c_VERBS_residue_and_governance_owner.md` §2). The term `standing` is `rank_gap`; a writ's band is the content key `force`. §13.4 decision 1 is answered (Jordan, A-22: command): commit D2 ships behind its revert. A decree is proclaimed (A-21).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.1, §2, 7b.3): every `an order` → `a standing` and edit 7 deleted; `standing` (the term) → `rank_gap` (U1 R-21, D-U1-01); A-21 answers FA §11 item 1 and corrects item 10 and gate D3 (an answer forms on any writ that is learned of; `force` enters the answer rows' obstacle); D4's dependency corrected at the tree (`loop/effects_migration.py::_relocate` exists, `:98`; the missing piece is a `dispatch` effect and its destination operand, CP-T09-08, which no suite proposal carries: `unified/U3_DEPENDENCY_ORDER.md` §6.3); A-81 (C3-C11), A-30 keys, U3 batch B21, R4 7b.0 block.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5a_DONE.md` row 13 and Close, "for another lane"): D2 edits 3-5 compose on `16_PESSIMIST_FA_C_under_the_seat.md`'s one `commands` body in `queries/world_q.py`; edit 3 no longer writes `state/gate.py::commands`.

## Status: PROPOSED

Lands in batch: B21 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `16_PESSIMIST_FA_A` and before `06_FA_war_lives_in_seats_B` (C3-D5's order). D4 does not land in B21: it waits on a carrier of CP-T09-08 (none in the suite).
Depends on: `05_SC_obstacle_difficulty_and_modifiers_B.md` and `U5c_SC_one_obstacle_form.md` §4 steps 0–2 (B05: `difficulty`, `opposition`, `regard`; `rank_gap` lands with `14_VERBS_BINDING_A` in B21); `U5c_VERBS_residue_and_governance_owner.md` §2 (B07: the `a standing` row is existing; `rank_gap`, `regard` per its table); `06_FA_decree_binds.md` and `06_FA_remit_grant_by_row.md` (B21).
Lane: FA. Tier (R4 7b.0 (1)): D1, D2 `sonnet` producer, effort `high`; D3 (the contested row and its terms) `opus` producer; one `opus` read of the 40-seed `force` table. Test file: `engine/season/tests/test_vb_d_orders.py` (one function per gate D1–D3; D4's function is written when D4 lands).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the issuer's trained score (A-6), talent as levels (A-7), a wound a level against the roll (A-8); the issuer's exercised seat helps him only as the `office` level (D-U1-01). Draws: `H(w.world_seed, w.tick, <actor id>, "issue.standing")`, `H(w.world_seed, w.tick, <actor id>, "dispatch.standing")` (A-30).

Source: `audits/14_VERBS_BINDING.md` §0.1, §0.2, §4 (`dispatch`), §6 (`issue`), §13.4 decision 1; batch D.
Binds on, and does not redo: `06_FA_decree_binds.md` (FA-P1: terms reach the addressee, answers form,
defiance is an occasion), CP-T09-07 (b) and CP-T09-08 (`dispatch` sends an obligee,
`proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-09-factions-war-diplomacy.md`
`:398-420`), F-FA-18 / R-27 (what a writ may order, design-first, FA's).

## What it changes in `engine/season/` at runtime

1. `issue` forms only on a Proposition (its `terms`), and the Proposition stamp also carries the asker's
   ambitions (the OUGHTs he is committed to).
2. `issue` and `dispatch` admit an addressee only if the exercised seat **commands** him (a new basis,
   `command`), and form `to` over the persons the actor can read as his.
3. `issue` and `dispatch` are contested (the existing prize `a standing`: one person opposite, fought at
   RESOLVE; no prize `an order` is added, C-25): a writ is minted at every band with its `force` written on
   it; an order to go is obeyed, grudged or refused by a draw.

All are declared movers for the realm. (2) is §13.4 decision 1 of the audit and ships behind its revert.

## The problem (evidence)

`binding_probe_2_1.txt` (realm, seed 1, two seasons):

- `issue`: the King's five writs all carry `terms` = `p_npc_020` (himself, a person); `p_npc_040` issues
  to `p_npc_004` about `p_npc_004`; the Lord Steward addresses the King (`to = p_npc_020`), admitted
  because the realm seat's purview reaches the King's residence (`state/gate.py::purview_reaches`: rung
  containment only).
- `dispatch`: four of six orders are addressed to the King by his officers; one is a self-order. 91 later
  acts by others cite an `order.given` at seed 0 and none is constrained by it (FA F-FA-06).
- Both bind with certainty or not at all: `issue` mints and nothing reads it (FA F-FA-01); `dispatch`
  writes nothing. The standing rule wants a decree's force and an order's obedience drawn.

## The resolution, decided

- **Terms are a Proposition** (ladder step 5: a writ's `terms` is *"the OUGHT it carries"*,
  `_eff_issue`'s own docstring; the class column is the tree's way to say it person-side). His own
  ambitions join the stamp because `propositions_heard` excludes what he himself said (`Claim.doer !=
  p.id`), and the OUGHT he holds is the natural content of his writ; `world_q.ambitions` is that rule's
  one owner.
- **Command, not territory** (decision 1, taken here behind a revert): a seat commands (a) its sworn men,
  a live `oblige` to `via`; (b) the holders of seats `via` may revoke (`may_revoke`, the gate's own
  predicate); (c) the unseated persons within `via`'s purview. Everyone else may be petitioned, not
  ordered. One predicate, `commands(w, actor, via, person) -> bool`, whose one body is
  `queries/world_q.py::commands` (`16_PESSIMIST_FA_C_under_the_seat.md` edit 1); one `requires` basis value, `command`.
- **The draw**: prize `a standing`, opponent `to`, through the one obstacle composer: `difficulty`
  `routine`, `opposition` (his trained score, A-79, D-U1-02), `regard` (his stance toward the issuer),
  `rank_gap` (OBS §2 member 6).
  `issue` mints the Record at every band (the paper exists: bookkeeping) and writes the band into its
  content as `force`; Failure is a dead letter. `dispatch` (after CP-T09-08): O/S relocate, Partial
  relocates and emits `order.grudged`, Failure relocates nobody and emits `order.refused`.

## Exact edits, by owner

**Commit D1 — what a writ orders.**

1. `verb_table.yaml`, `issue`: `referent_class: Proposition` with a note naming VB-D and its revert
   (delete the column). The typed cell is unchanged.
2. `queries/world_q.py::questions_for`: add `tuple(ambition_ids(w, p))` to `added` beside
   `propositions_heard(w, p)`, where `ambition_ids` returns the Proposition ids of `ambitions(w, p)` (the
   one owner) — `_stamped` dedups. Declared widening: `argue` (the other `Proposition`-classed row) gains
   these referents; `commit` does not (`held_edge_declines`). Measure both rows' formed counts.

**Commit D2 — command.**

3. *(One owner, wave-3 mop-up: `16_PESSIMIST_FA_C_under_the_seat.md` edit 1 writes the one body,
   `commands(w, actor, via, person_id) -> bool` in `queries/world_q.py`, taking this file's name and the
   tree's `(w, actor, via, …)` signature, and lands first in B21. This commit writes no second body in
   `state/gate.py`; the three clauses (`w.tenures` for the `oblige`; `may_revoke` over the person's live
   seats; `purview_reaches` and `seat_holds` for the unseated) and the docstring naming decision 1 and the
   revert are FA_C's.)*
4. `data/requires.py`: the `basis` form gains the value `command`, dispatched to `world_q.commands`
   (FA_C edit 1) exactly as `purview` is (a value of an existing form, not a new stem). FA_C edit 2 makes
   the same change; whichever of the two lands second finds it made and adds nothing.
5. `verb_table.yaml`, `issue`: the `authority` conjunct's `basis: purview` → `basis: command`;
   `requires:` prose and `refusal_note` amended (*"`issue.unauthorized` -- the SEAT: none exercised grants
   `issue`, or it does not command the executor"*). `[ASSUMPTION; medium; Jordan to correct; revert:
   `basis: purview`]`.
6. `decision/options.py::operand_bags`: for a row whose `authority` conjunct is `basis: command`, fan `to`
   over the persons the actor can read as commanded person-side: his own seats' obligees (his ledger's
   `duty.taken` claims naming his seat) and the holders his ledger names of seats beneath his. What he
   cannot read stays the fold's refusal.

**Commit D3 — the draw on `issue`.**

7. *(Deleted, W3-4a: no prize `an order`; `a standing` exists in `rosters.yaml: contest_subsystems.prizes`.)*
8. `verb_table.yaml`, `issue`: `contests: "a standing"`, `difficulty: routine`; `writes` at every band
   `["Record.exists"]`; `emits` O/S/P `["dispensation.issued"]`, Failure `["dispensation.ignored"]`;
   `emits_on_refusal` flattened to one kind, `issue.refused`, keyed under every clause (a contested row
   keys one kind unless it keys `counterparty`; `determine`'s v9 SC-03b precedent) — `issue.unauthorized`
   is retired into it, and the refusal's `observed` reads still say which clause failed. **Durable write
   of the Failure band (A-81; C3-C11):** the writ exists at every band, and `dispensation.ignored` is
   proclaimed like any decree (A-21): whoever learns of the issue holds a claim of it and of its `force`,
   so a dead letter is itself a remembered deed against the issuing seat.
9. `loop/effects_information.py::_eff_issue`: pass `res.degree` into the content as `force` (a
   `dispensation` key; `rosters.yaml: record_kinds` gains `force` for that kind).
10. Cross-lane, listed for FA (not edited): under A-21 an answer forms for whoever learns a decree was
    issued, at every `force` band, Failure included; the answer rows' obstacles read `force` (`evade /
    defy` harder against a strong writ, `comply` easier). *(W3-4a: the earlier "no answer forms on a
    `Failure` writ" contradicted A-21 and is struck.)*

**Commit D4 — `dispatch` (after CP-T09-07 (b) and CP-T09-08).**

11. `verb_table.yaml`, `dispatch` (CP-T09-08's rebuilt row): `contests: "a standing"`, `difficulty:
    routine`, `counterparty: to`; the `authority` conjunct `basis: command`; writes the `contain` pair and
    `Person.travel_leg` at O/S/P through the existing journey body `loop/effects_migration.py::_relocate(w,
    a, dest, mover=to)` (T, `:98`; the `mover` argument already relocates someone other than the actor,
    `_eff_march`'s precedent), `[]` at Failure; emits `order.given` at O/S, `order.given`, `order.grudged`
    at Partial, `order.refused` at Failure (witnessed by the issuer and the man ordered: the refusal is a
    remembered deed, A-81). **INCOMPLETE (blocked):** the `dispatch` effect and its destination operand
    (where the man is sent) are CP-T09-08's design, which no suite proposal carries
    (`unified/U3_DEPENDENCY_ORDER.md` §6.3 "`_eff_dispatch` … no carrier"); not decidable from the tree.
12. Until CP-T09-08 lands, D2's fan applies to the current row (`referent_class: Person`, `writes: []`):
    no order goes up the chain and no self-order forms.

Order: D1, D2, D3 (after SC-B and FA-P1), D4 (after a carrier of CP-T09-08 exists).

## Gate (execution artifact)

- D1: `aperture 2 0` and `2 1` with the probe: 0 writs whose `terms` is not a Proposition; `argue` and
  `commit` formed counts recorded before and after.
- D2: same: 0 writs and 0 orders whose addressee the seat does not command (the probe's one writ to the
  King and four orders to him → 0).
- D3: FA-B4's `recall` scenario, 40 seeds: all four `force` bands occur; at every band, Failure included,
  the Count is offered his answers once he learns of the issue (A-21; FA-P1's gate), and the answer's
  composed obstacle carries `force` (its value differs between a Failure and a Success writ).
- D4: a seeded run in which a dispatched obligee's `contain` moves at O/S/P and does not at Failure.

## Falsifier

Revert D1's class: person-terms return. Swap `command` for `purview`: the writ to the King returns. Pin
the roll: one `force` band only.

## What it does not do

It does not decide which Propositions are orders (R-27) or how an addressee answers (FA-P1). A decree is
proclaimed (A-21), which answers FA §11 item 1: D3 writes `force` on the Record and `force` enters the
answer rows' obstacle; it does not decide whether an answer forms. It adds no relocation body (the journey
is `_relocate`, existing).

## NERS reading

N: without D1–D2 writs order persons and run up the chain; without D3–D4 a decree is a switch. R: a weak
lord's writ may be a dead letter, a strong one's may be grudged; the realm produces both unwatched. S:
one predicate for command; one prize; `force` read by the answers rather than a second ladder. E (last):
one basis value and one written band replace a class of nonsense and a certainty.

## Cost class

Medium: one class column and a stamp term, one gate predicate and basis value, two contested rows on an
existing prize, one Record key; cross-lane items for FA.
