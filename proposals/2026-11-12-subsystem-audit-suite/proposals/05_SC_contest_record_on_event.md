# SC-P1 — a contested act's Event carries the roll that decided it

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-06) — `margin_endings` values are `[pool, ob, net, margin, terms, levels, leverage]`: `terms` and `levels` replace `room`, because the room is no longer one number subtracted from the obstacle (`U5c_SC_one_obstacle_form.md` §5).

## Status: PROPOSED

Source: `audits/05_SC_audit.md` F-SC-04; closes `engine/season/hole_register.yaml` H-284.

## What it changes in `engine/season/` at runtime

Every Event a contested or graded act emits through the social contest provider gains a non-empty
`Event.ending` tuple naming the pool, the obstacle, the net and the settled margin of the draw that
graded it. The content hash of every world in which a social roll executes moves once (a declared
mover). No odds, band or write changes.

## The problem (evidence)

- `engine/season/seam/wrappers/sigma.py::resolve` returns
  `dict(status, module, resolver, pool, ob, net, leverage, settled_margin)`; `loop/resolve.py::_contest`
  wraps it as `Resolution(degree_of(r, …), r)` and `_fold` reads only `resolution.degree`
  (`loop/resolve.py:406`, `:866`). The dict is not stored.
- `state/carriers.py::Event` has `degree`, `observed` and `ending`; nothing writes a margin, pool or
  obstacle to any of them for a social roll (H-284's cite, re-read at `601e715`).
- Consequence in play: the log says `argument.lost @ Failure`. It cannot say by how much, against what,
  or whether the room (`reception`, `proofs`), the forgery quality or the ceiling decided it. A hearing
  therefore cannot be explained to a player or to a chronicle, and no later mechanism can read "how
  narrowly he lost" (a recoverable, graded outcome needs the grade's operands).
- Precedent in the tree: personal combat met the same gap (H-266) and closed it with a typed field,
  `Event.ending`, written by the effect through `Change.ending` and folded into the content hash
  (`state/world.py:1695-1725`, `loop/resolve.py:988-990`, `loop/effects_combat.py::fight_ending`).

## The resolution, decided

Reuse `Event.ending` (ladder step 4, the combat precedent). Do not add an `Observation` to
`Event.observed`: WITNESS deposits observed reads into ledgers (`loop/matter.py`'s stock-report note),
and a hearer must not learn the speaker's pool from having been in the room. `ending` is the
provider's own record of how the contest ended and is read resolver-side.

Rejected: a driver-side map (`SeasonDriver.resolution_of`) — it is outside `World`, so it is neither
hashed nor saved, and "recoverable from the log" would be false after a load. Rejected: a new `Event`
field (`margin`) — a second carrier for one fact per provider (shape divergence, CLAUDE.md §10).

## Exact edits, by owner

1. `engine/season/rosters.yaml` — beside the roster `loop/effects_combat.py::fight_ending` reads
   (`data/rosters.py:1164`), add the social provider's ending shape as data:

   ```yaml
   margin_endings:
     source: "SC-P1 (H-284): what a margin provider's contest leaves on its Events"
     values: ["pool", "ob", "net", "margin", "room", "leverage"]     # ordered; the tuple's keys
   ```

   `room` is `reception_gain·reception + proof_step·proofs` as the module composed it and
   `leverage` the act's net sigma: the two terms a narrative needs to say WHY (the bench was against
   him; he pressed). `sigma.resolve` adds `room` to its returned dict (it already returns
   `leverage`); the module exposes the term by returning it beside the obstacle from one helper, so
   the host does no arithmetic.

2. `engine/season/loop/resolve.py::_fold` — after `_degree` is bound (`:406`), where
   `resolution is not None` and `resolution.result` carries a `net`/`ob` pair (the same test
   `seam/ladder.py::degree_of` makes at `:256`), build
   `tuple((k, resolution.result[src]) for k, src in MARGIN_ENDING)` with `margin` read from
   `settled_margin`, and seed `carried["ending"]` with it before the write loop. The fold's existing
   `replace(e, …, ending=_ending)` at `:566` then stamps it on every Event of the act — including the
   Failure band's, which today returns through the same loop with `changed` empty.
   A refusal (`_refuse_party_gap`) carries none: no dice were dealt.
3. `engine/season/state/carriers.py::Event.ending`'s comment — state the two shapes by provider
   (per-party endings for a scene; the margin tuple for a margin provider), naming the two rosters.
4. `engine/season/harness/chronicle.py` (or `aperture.py`'s per-act block) — print the tuple where it
   prints the degree. One line; no new instrument.

`modules/social_contest/roll.py` and `seam/wrappers/sigma.py` are unchanged: the pair is already
returned.

## Gate (execution artifact)

`engine/season/tests/test_sc01_provider.py` gains one test: fold one `argue` on `probes.tiny_world`
at a fixed seed; assert the emitted Event's `ending` equals the provider's returned pool, obstacle,
net and settled margin for that act (read by calling `sigma.resolve` with the act's own generator),
and that `seam/ladder.py::degree_of` over that tuple reproduces `Event.degree`. Re-pin the seeded
goldens in the same commit and say so (CLAUDE.md §7).

## Falsifier

(a) Plant a second `Margin` (net + 3) at the entry: the test must go red (the tuple follows the roll,
not a recomputation). (b) After a WITNESS barrier, no `Claim` in any ledger has a predicate drawn from
`margin_endings` — if one does, the record leaked person-side and the edit is wrong.
`[UNVERIFIED]`: that WITNESS never deposits `Event.ending`; the falsifier is the check.

## NERS reading

- **N**: removing it leaves contests graded and unexplained — the legibility half of ROBUST ("makes
  players feel they impact the world") and the precondition of every later reader of "how he lost".
  Holds bottom-up (the provider already computes it), lateral (combat has the sibling), top-down (the
  chronicle).
- **R**: completes a mechanism that is "fully formed" only on its success side today.
- **S**: one method for both contest providers; no second carrier.
- **E** (last, as a ratio): four numbers on a field that exists, no new type, against a closed hole
  and an unblocked explanation contract (B10-18c's stated reason for holding the narrow options).

## Cost class

Edit (one fold site, one roster, a golden re-pin).
