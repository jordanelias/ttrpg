# U5d-GO — owed edits: the save snapshot, two cross-lane orders, and one card line

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.4 row 163 and §2 row A-30 (CONFORMS; §1 stands; the A-30 sentence now names the keyed mix as `11_GO_one_draw_owner.md` carries it), §7 (lands-it and tier added; §1's gate given its test names and expected reading); `U3_DEPENDENCY_ORDER.md` B06 (after `11_GO_float_contract.md` Parts A and C and `16_PESSIMIST_GO_keyed_draw_no_recorder.md`, before `11_GO_pointer_and_stale_text_resolutions.md` item 5) and the `test_go07_canonical_digest.py` chain (B03 → B06: item 11 of the pointer file deletes the spent control in B03; §1's round trip is added here after it); §2 (a)'s order checked by batch (`10_DICE_believed_odds_have_a_prior.md` B05 before `11_GO_player_surface_contract_B.md` B34) and §2 (b)'s (`03_PC_typed_outcome_one_door.md` B14 before B34); `U3_CONFLICT_LEDGER.md` C3-L4 (§2 (b) is the witness's claim; the doer's own claim is `_B` §3's).

**Depends on:** `11_GO_float_contract.md` Part A (B06); `16_PESSIMIST_GO_keyed_draw_no_recorder.md` and `11_GO_one_draw_owner.md` (B06); `11_GO_pointer_and_stale_text_resolutions.md` item 11 (B03).
**Lands in batch:** B06 (`B06-keyed-draw`), §1 last in the batch after the declared re-pin; §2 and §3 are orders and a card line read by B34 and B41.

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Author: U5d closure lane (Fable), 2026-11-12. Carries `audits/11_GO_audit.md` F-GO-09 and R44 (which
said "no proposal this pass"), and `audits/16_PESSIMIST_GO.md` resolutions 4, 7 and 8 (F-PES-GO-05,
F-PES-GO-13), under A-29, A-30 and A-49.

## What it changes in `engine/season/` at runtime

§1 adds a decoder beside the canonical encoder and changes no game behaviour. §2 and §3 are an order
and a card line.

## §1 — a save is a state snapshot (F-GO-09, R44; A-29, A-30)

- **Decision.** Under A-29 state holds declared floats, so cross-machine re-simulation from seed and
  acts is not promised and a save is a snapshot of state. Under A-30 a draw is a function of its key
  (`H(seed, tick, subject, purpose)`, its uniforms an owned mix of `(key, n)`, `11_GO_one_draw_owner.md`),
  so a loaded world continues with the draws the unbroken run would have made, on the oracle and on
  the port; no generator state is saved.
- **Owner.** `engine/season/state/world.py`, beside the GO-07 encoder (`:210-340`).
- **Edit.** One snapshot format: the GO-07 encoding of the hashed frames (`_STATE_COLLECTIONS`,
  `_STATE_SEQUENCES`, `:1660-1665`) plus four named extras the digest omits: `world_seed`, `tick`, the
  act store, and the fixtures digest. A `decode` that rebuilds a `World` from it and refuses a
  fixtures digest that does not match the running build.
- **Gate.** `engine/season/tests/test_go07_canonical_digest.py` gains one round trip at seeds 0–2 after
  two seasons: `decode(encode(w)).content_hash() == w.content_hash()`, and one more season run on the
  decoded world equals the same season run on the original (the control that the act store and tick
  came back). *(W3-1, test 9.)* Test names: `test_snapshot_round_trip_hash_equal` and
  `test_a_decoded_world_runs_the_same_next_season` (both red before `decode` exists), and
  `test_decode_refuses_a_foreign_fixtures_digest` (expects `decode` to refuse, as a typed value
  `[ASSUMPTION: the port loads saves, so `decode` is port-reached and refuses by value, not by a raise —
  basis: `hol` §53 as `U5b_PC_residue.md` §4 applies it]`). Order: write the three tests red; add `decode` beside the
  encoder; green.
- **Falsifier.** Any field of state the round trip drops (the second assertion moves); a decode that
  accepts a foreign fixtures digest.
- **Movers.** None (no game path reads the snapshot).
- **Depends on.** `11_GO_float_contract.md` A (so a float's encoding is its bits) and
  `16_PESSIMIST_GO_keyed_draw_no_recorder.md`. The end-of-campaign reveal (A-49) reads a finished
  world's log and needs no save.

## §2 — two orders across lanes (PES-GO resolutions 4 and 7)

(a) Believed odds: the three edits the GO pessimist lists (`believed_chance` passes the believer's own
`believed_room`; a believed form for a module estimate; the prior) land in
`10_DICE_believed_odds_have_a_prior.md`'s order, before `11_GO_player_surface_contract_B.md` §2 shows
an odds column; until then the column is absent, not `None`. (b) A watched fight's account: WITNESS
deposits the band Event's `ending` to a co-located witness, at PC's owner
(`03_PC_typed_outcome_one_door.md`), before SURF-B's rule 4 is gated.

## §3 — exit line 4 of the port-gate card (F-PES-GO-13)

At B10-20's open, the card's line 4 names `export_npc_roster --check` apart from the round-trips:
"reports hand-corrected rows; fails only on a row naming no case, place or seated person". Text; no
code.

## NERS (E last)

N: without §1 a session cannot be resumed on either side. R: completeness. S: one encoding for the
digest and the save. E: one decoder, four extras.

## Cost class

Small build (§1), notes (§2, §3). Lands it (W3-1): the IN/GO B06 session, after the batch's declared
re-pin; `sonnet`.
