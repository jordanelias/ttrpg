# SC-B2 — Negotiation as the same sitting under a mutual disposal: no draw decides consent

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-06 — no *contest* roll decides consent, but the consenting party's choice is sampled (the one chooser's sampler), so acceptance is a draw whose odds his pursuits set.

Folded: 2026-11-12 by `audits/28_SCENE_ACCESS.md` (rulings A-63, A-64). Nothing here is deleted. A meeting of two parties under a `disposal: mutual` row is a scene with both in it: each party who moves is engaged for that round, and the meeting is a scene received for the one who did not open it (`28_CORE_scene_access_A_occupancy_and_precedence.md` §2, §3). A party already engaged elsewhere that round is not at the table and the meeting does not open: the opener's act is refused at `engaged`, and he may call again, ask for an appointment or send his terms on paper (`28_CORE_scene_access_B_appointments.md` §4). Consent is unchanged: still each party's own sampled act.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-B2 (AMBIGUOUS), §2 row SC-B2 (A-21, A-81), §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger S-16; `unified/U3_CONFLICT_LEDGER.md` §9; `U5_CONFLICTS_U5c.md` C-07). Layer 1 rewrite (`04` AX-1 / §B.9 `Act.actor : PersonId`; PART D row 10a, a write by a non-owner; C-07, one person's roll cannot open another's edge): "the host's two `oblige` acts" are replaced by **each party's own act** — the accepter's `accept` move is his own `oblige`, chosen by his own decider through the one chooser's sampler, and the offerer's `offer` is his own standing, conditional `oblige`, formed when he made it; the module returns data, the effect writes each edge under the act of the party it binds, and the host forms no act on anyone's behalf. `PlayHost.decide` → `PlayHost.deciders["social_contest.hearing"]` (C-U5a-04). A-21: covenants stay in person, which a sitting is. A-81: a negotiation that ends without acceptance still writes (the case file's stages and the witnessed exchanges), named in the falsifier. The design-first items stay INCOMPLETE with their blocking reason; named tests, lands-it and tier added.

**Lands in batch:** B24 (after `05_SC_playable_hearing_B.md`). **Depends on:** `05_SC_playable_hearing_B.md` (B24), `28_CORE_scene_access_A_occupancy_and_precedence.md` (B28, the engagement read the Folded line names; at its control the sitting assumes attendees free), plan position CR-63 (the opening verb) `[PL]`, `exchange`'s operands (MISSING: no carrier in the suite).

## Status: PROPOSED — design-first (depends on the `exchange` verb's operands and on `05_SC_playable_hearing_B.md`)

Source: `audits/05_SC_audit_addendum_B.md` §B4, G-51. Intent of high weight, not ruled: R-19 (fears
are leverage), R-23 (the act is inviolate), R-29 (consent, not command), as recorded in
`PD/2026-10-30-social-contest-primitives-and-kinds.md` §1 (addendum C-7 on their provenance).
Precedents as the tree sources them: Griftlands' negotiation (arguments on a board, a hand that
depletes, concession to keep what is unspent), Burning Wheel's Duel of Wits (stakes declared before
the first exchange; a compromise scaled to what was lost).

## What it changes in `engine/season/` at runtime

Nothing until built. At the control arm (`sitting_exchanges` 0) the seeded `negotiation` row is
unchanged. Built: a meeting of two parties under a row with `disposal: mutual` runs the hearing's
sitting with no bench and no closing draw, and ends either in an `oblige` both parties opened by their
own acts, or in nothing.

## The problem (evidence)

- The seeded row exists: `engine/season/arrangements.yaml: negotiation` —
  `disposal: mutual`, `disposes: oblige`, `order: alternating`, `proofs: [record, testimony]`,
  `bench_basis: none` (read at this lane's completion). `data/arrangements.py:278` reports a mutual
  row only by whether any verb opens an `oblige`; nothing reads `order:` or `proofs:` for it, and no
  act can conclude it.
- A roll cannot decide consent without making one person's choice another's outcome (R-29 as
  recorded; `holonic` §44.3, a wrapper never decides). The live `oblige` verb is a person's own act on
  a seat (`verb_table.yaml: oblige`, `eligibility: own`); `exchange` swaps stores between two sides
  whose stores cover the exchange (`uncontested_material`). Neither is offered as the end of a
  negotiation.
- The first audit's SC-P3 had no negotiation; the kernel's `negotiation` venue preset is `[SEED]`
  numbers with no producer (addendum §B3, dead table).

## The resolution, decided

**The same module entry, `social_contest.hearing`, with the row's `disposal: mutual` changing three
things and nothing else.** Ladder: step 3 (the row's own keys), step 4 (the hearing's sitting; the
`oblige` opener), step 5 (one entry, not a second scene).

1. **No bench, no closing draw.** `HearingInput.bench` is empty and `closing` is `None` on a mutual
   row; `HearingOutcome.margin` is `None`. The module never names an agreement.
2. **Two moves are added by row, from `hearing_moves`:** `offer` (needs: a term set the offerer can
   meet — an `oblige` term and, when `exchange`'s operands land, stores each side gives; no draw;
   the offer stands on the board, replacing his previous one) and `accept` (needs: a standing offer
   of the other side; no draw; ends the sitting). `present`, `answer`, `argue`, `impugn`, `concede`
   and `rest` keep their rows. `concede` on a mutual row withdraws one of the conceder's own demands
   from his standing offer (Griftlands' concession), and is witnessed.
3. **What a draw does in a negotiation.** `argue` rolls as in a hearing; at Success or better the
   arguer's argued claim is deposited to the counterparty as a told claim (the told channel, E-3 of
   `08_FI_05_…_B.md`), with the arguer on its chain. The roll changes what the other believes, never
   what he does. His decider then values the offers on the board with that belief. A presented item
   the counterparty would not want told (a deed claim about him) is leverage by the same path: his
   decider prices the consequence of its being told elsewhere (R-19).

**The end.** `accept` returns `HearingOutcome.accepted = (offer id, accepter)`. The disposal opens by two
acts, each the act of the party it binds and each formed from that party's own choice (R-23: each act is
its own; R-29: each is chosen; C-07): the offerer's `offer` move is his own conditional `oblige` under the
offer's term, formed when he made it (it stands on the board and binds only on acceptance); the
accepter's `accept` move is his own `oblige`, chosen by his own decider. The module returns data only; the
effect writes each `oblige` edge under the act of the party it binds (`Act.actor` = that party), never
under the opener's act and never by an act the host forms on a party's behalf (`04` PART D row 10a).
`exchange`'s store swap, where the offer has one, is a third act with its own precondition; if a party's
stores no longer cover it at MATTER, his act is refused and the agreement is broken as any `oblige` is.
All rest without acceptance: nothing is opened; the sitting's exchanges are still written to the case
file and witnessed, so the failed negotiation leaves a durable write (A-81).

**How each side chooses.** *(Reconciled, D-06: consent stays a choice, and the choice is a draw —
the decider samples through the one chooser's sampler, `05_SC_playable_hearing_B.md` "Who decides", so a
good offer is likely accepted and never certainly; the standing rule and R-29 are both met.)* The
hearing's decider: each legal move is a Candidate, valued
by the believed worth of the board the move leaves. For `accept`, that is the offer's terms in his own
pursuits; for `offer`, his belief of what the other will accept (`closing_odds` has no meaning here;
the decider reads the other's standing offer and its own claims about him). No special case for a
player: `PlayHost.deciders["social_contest.hearing"]` serves a player's person in the same seat.

## Exact edits, by owner

1. `engine/season/rosters.yaml: hearing_moves` — rows `offer`, `accept`, each with
   `rows: [mutual]` (the disposals under which a rite may list it).
2. `engine/season/queries/inputs.py` — `HearingInput.closing: Optional[SocialContestInput]`;
   `HearingOutcome.accepted: Optional[tuple]`; an `Offer` record (`id`, `by`, `terms`, `stores`).
3. `modules/social_contest/hearing.py::hear` — on `closing is None`, skip the closing draw and the
   ballots; apply `offer` and `accept`.
4. `engine/season/seam/wrappers/sigma.py::hearing_input` — for a mutual row, no seats and no closing.
5. `engine/season/loop/effects_information.py` — on an `accepted` outcome, each party's `oblige` is
   written under that party's own act (the offerer's `offer`, the accepter's `accept`, each recorded as
   an `Act` with that party as actor and the sitting as its scene), and the `exchange` act likewise;
   their ordinary preconditions apply at MATTER of the same round. The effect writes no edge under the
   opener's act.
6. `engine/season/verb_table.yaml` — a verb that opens a negotiation (`treat`, contested by nobody,
   `heard_by: none`, deferred to ENCOUNTER on the row's prize) — **design-first**: whether an existing
   verb (`petition` to a person) carries it is CR-63's, and this proposal does not choose.

## Gate (execution artifacts)

1. A hand-built two-NPC negotiation over one `oblige` term: `--auto` twice, identical hash; the log
   holds the offers, the acceptance or the all-rest, and (on acceptance) two `oblige` Tenures, each
   opened by its own party's act.
2. The same with a planted told claim the accepter holds about the offerer's past breach: a different
   acceptance or none, read from the decider's Candidate scores.
3. Parity: a scripted player returning the NPC decider's pick reproduces the `--auto` hash.

**Named tests** (new, `engine/season/tests/test_sc_hearing_negotiation.py`):
`test_two_npc_negotiation_auto_twice_same_hash` (1); `test_each_oblige_is_opened_by_its_own_partys_act`
(1: the `Act.actor` of each edge's opening act is the party it binds);
`test_a_held_breach_claim_changes_acceptance` (2); `test_scripted_player_reproduces_auto_hash` (3);
`test_a_negotiation_without_acceptance_still_writes_the_case_file` (A-81).

## Falsifier

An agreement opened with no `accept` chosen by the accepter (consent decided by a draw). An `oblige` edge
whose opening act's actor is not the party it binds. An `argue` success that changes the outcome without
changing a ledger. An accepted `exchange` that moves stores the giver no longer holds. A negotiation that
ends with no acceptance and no write.

## NERS reading

- **N**: lateral it is the hearing with the bench removed; top-down a bargain is consent; bottom-up the
  row, `oblige`, the told channel and the decider exist.
- **R**: strategy (what to offer, what to reveal, when to concede); without a player two houses can
  bargain and fail; complete at its extremes (no acceptance is a stable ending).
- **S**: one entry, one move vocabulary, one decider; consent stays where every other choice is made.
- **E**, last: two move rows and one outcome field against a negotiation that can be played.

## Cost class

Design-first (the opening verb; `exchange`'s operands); then small builds after
`05_SC_playable_hearing_B.md`.

**INCOMPLETE, not decidable from the repository:** edit 6's opening verb (`treat` or `petition` to a person)
is CR-63's (a plan position); `exchange`'s operands have no carrier in the suite. **Lands it and tier.** A
design pass on `opus` (with `ners`) for edit 6 and the operands; then the B24 batch, `valoria-author` on
`sonnet` (`high`) for edits 1–5, one `methodology-close`. **Hash movers.** None at control
(`sitting_exchanges` 0); declared when built.
