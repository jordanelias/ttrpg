# U5d-GO — owed edits: the save snapshot, two cross-lane orders, and one card line

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Author: U5d closure lane (Fable), 2026-11-12. Carries `audits/11_GO_audit.md` F-GO-09 and R44 (which
said "no proposal this pass"), and `audits/16_PESSIMIST_GO.md` resolutions 4, 7 and 8 (F-PES-GO-05,
F-PES-GO-13), under A-29, A-30 and A-49.

## What it changes in `engine/season/` at runtime

§1 adds a decoder beside the canonical encoder and changes no game behaviour. §2 and §3 are an order
and a card line.

## §1 — a save is a state snapshot (F-GO-09, R44; A-29, A-30)

- **Decision.** Under A-29 state holds declared floats, so cross-machine re-simulation from seed and
  acts is not promised and a save is a snapshot of state. Under A-30 a draw is a function of its key,
  so a loaded world continues with the draws the unbroken run would have made, on the oracle and on
  the port.
- **Owner.** `engine/season/state/world.py`, beside the GO-07 encoder (`:210-340`).
- **Edit.** One snapshot format: the GO-07 encoding of the hashed frames (`_STATE_COLLECTIONS`,
  `_STATE_SEQUENCES`, `:1660-1665`) plus four named extras the digest omits: `world_seed`, `tick`, the
  act store, and the fixtures digest. A `decode` that rebuilds a `World` from it and refuses a
  fixtures digest that does not match the running build.
- **Gate.** `engine/season/tests/test_go07_canonical_digest.py` gains one round trip at seeds 0–2 after
  two seasons: `decode(encode(w)).content_hash() == w.content_hash()`, and one more season run on the
  decoded world equals the same season run on the original (the control that the act store and tick
  came back).
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

Small build (§1), notes (§2, §3).
