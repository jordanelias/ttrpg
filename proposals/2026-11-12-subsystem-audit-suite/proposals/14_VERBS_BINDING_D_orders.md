# VB-D — an order orders something, goes down the chain, and takes hold by a draw

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-25) — the prize `an order` is not added: `issue` and `dispatch` contest `a standing` (same hearer, same step; `U5c_VERBS_residue_and_governance_owner.md` §2). The term `standing` is `rank_gap`; a writ's band is the content key `force`. §13.4 decision 1 is answered (Jordan, A-22: command): commit D2 ships behind its revert. A decree is proclaimed (A-21).

## Status: PROPOSED

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
3. `issue` and `dispatch` are contested (a new prize `an order`): a writ is minted at every band with its
   `force` written on it; an order to go is obeyed, grudged or refused by a draw.

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
  ordered. One predicate, `state/gate.py::commands(w, actor, via, person) -> bool`, beside
  `purview_reaches`; one `requires` basis value, `command`.
- **The draw**: prize `an order`, opponent `to`, through SC-B's obstacle: `difficulty` `routine`,
  `opposition` (his score), `regard` (his stance toward the issuer), `standing` (VB-C's term).
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

3. `state/gate.py`: `commands(w, actor, via, person) -> bool`, the three clauses above, each read through
   its one owner (`w.tenures` for the `oblige`; `may_revoke` over the person's live seats;
   `purview_reaches` and `seat_holds` for the unseated). Docstring names decision 1 and the revert.
4. `data/requires.py`: the `basis` form gains the value `command`, dispatched to `commands` exactly as
   `purview` is (a value of an existing form, not a new stem).
5. `verb_table.yaml`, `issue`: the `authority` conjunct's `basis: purview` → `basis: command`;
   `requires:` prose and `refusal_note` amended (*"`issue.unauthorized` -- the SEAT: none exercised grants
   `issue`, or it does not command the executor"*). `[ASSUMPTION; medium; Jordan to correct; revert:
   `basis: purview`]`.
6. `decision/options.py::operand_bags`: for a row whose `authority` conjunct is `basis: command`, fan `to`
   over the persons the actor can read as commanded person-side: his own seats' obligees (his ledger's
   `duty.taken` claims naming his seat) and the holders his ledger names of seats beneath his. What he
   cannot read stays the fold's refusal.

**Commit D3 — the draw on `issue`.**

7. `rosters.yaml: contest_subsystems.prizes`: add `"an order"` (the `a seat` row's fields).
8. `verb_table.yaml`, `issue`: `contests: "an order"`, `difficulty: routine`; `writes` at every band
   `["Record.exists"]`; `emits` O/S/P `["dispensation.issued"]`, Failure `["dispensation.ignored"]`;
   `emits_on_refusal` flattened to one kind, `issue.refused`, keyed under every clause (a contested row
   keys one kind unless it keys `counterparty`; `determine`'s v9 SC-03b precedent) — `issue.unauthorized`
   is retired into it, and the refusal's `observed` reads still say which clause failed.
9. `loop/effects_information.py::_eff_issue`: pass `res.degree` into the content as `force` (a
   `dispensation` key; `rosters.yaml: record_kinds` gains `force` for that kind).
10. Cross-lane, listed for FA (not edited): FA-P1's answer formation reads `force` (no answer forms on a
    `Failure` writ), and the answer rows' obstacles read it (`evade / defy` harder against a strong writ).

**Commit D4 — `dispatch` (after CP-T09-07 (b) and CP-T09-08).**

11. `verb_table.yaml`, `dispatch` (CP-T09-08's rebuilt row): `contests: "an order"`, `difficulty:
    routine`, `counterparty: to`; the `authority` conjunct `basis: command`; writes CP-T09-08's
    `contain` pair and `Person.travel_leg` at O/S/P, `[]` at Failure; emits `order.given` at O/S,
    `order.given`, `order.grudged` at Partial, `order.refused` at Failure.
12. Until CP-T09-08 lands, D2's fan applies to the current row (`referent_class: Person`, `writes: []`):
    no order goes up the chain and no self-order forms.

Order: D1, D2, D3 (after SC-B and FA-P1), D4 (after CP-T09-08).

## Gate (execution artifact)

- D1: `aperture 2 0` and `2 1` with the probe: 0 writs whose `terms` is not a Proposition; `argue` and
  `commit` formed counts recorded before and after.
- D2: same: 0 writs and 0 orders whose addressee the seat does not command (the probe's one writ to the
  King and four orders to him → 0).
- D3: FA-B4's `recall` scenario, 40 seeds: all four `force` bands occur; at Failure no answer forms; at
  Success the Count is offered his answers (FA-P1's gate).
- D4: a seeded run in which a dispatched obligee's `contain` moves at O/S/P and does not at Failure.

## Falsifier

Revert D1's class: person-terms return. Swap `command` for `purview`: the writ to the King returns. Pin
the roll: one `force` band only.

## What it does not do

It does not decide which Propositions are orders (R-27), whether a decree is proclaimed or delivered (FA
§11 item 1), or how an addressee answers (FA-P1). It adds no relocation body (CP-T09-08's `_relocate`).

## NERS reading

N: without D1–D2 writs order persons and run up the chain; without D3–D4 a decree is a switch. R: a weak
lord's writ may be a dead letter, a strong one's may be grudged; the realm produces both unwatched. S:
one predicate for command; one prize; `force` read by the answers rather than a second ladder. E (last):
one basis value and one written band replace a class of nonsense and a certainty.

## Cost class

Medium: one class column and a stamp term, one gate predicate and basis value, one prize, two contested
rows, one Record key; cross-lane items for FA.
