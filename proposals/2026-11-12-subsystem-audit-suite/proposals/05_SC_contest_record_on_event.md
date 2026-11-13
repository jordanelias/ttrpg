# SC-P1 — a contested act's Event carries the roll that decided it

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-06) — `margin_endings` values are `[pool, ob, net, margin, terms, levels, leverage]`: `terms` and `levels` replace `room`, because the room is no longer one number subtracted from the obstacle (`U5c_SC_one_obstacle_form.md` §5).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-P1, §3 row `margin_endings`, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-06, ledger R-29; `unified/U1_GLOSSARY.md` *margin*; `unified/U3_CONFLICT_LEDGER.md` C3-L1, C3-L5, C3-C16). Changed: the body follows the head (`room` → `terms` and `levels` in edit 1, its explanation and the gate); "settled margin" → the margin (A-5 removes settling; the real margin is quantised once at the ladder, C3-L1); this file carries the persistence of lane A's `ob_terms` (F-SC-04) in B05 (C3-L5); the use of `Event.ending` is named as a departure from `04` §B.9 at the site (B4 third disposition, C3-C16), consistent with D-U1-06 (no new Event field; `observed` is not used, so no hearer learns the speaker's pool; `margin_endings` is the roll record's owner, U1 ledger R-29); falsifier (b)'s `[UNVERIFIED]` is narrowed by a grep; lands-it and tier added.

**Lands in batch:** B05 (OBS §4 step 2). **Depends on:** `U5c_SC_one_obstacle_form.md` steps 0–1b (B05; `Margin.terms`, `levels`). **Read by:** `11_GO_player_surface_contract_B.md` (B34, reads the record, adds no store).

## Status: PROPOSED

Source: `audits/05_SC_audit.md` F-SC-04; closes `engine/season/hole_register.yaml` H-284.

## What it changes in `engine/season/` at runtime

Every Event a contested or graded act emits through the social contest provider gains a non-empty
`Event.ending` tuple naming the pool, the obstacle, the net and the margin of the draw that graded it,
with the obstacle's `terms` and the leverage `levels`. The content hash of every world in which a social roll executes moves once (a declared
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
provider's own record of how the contest ended and is read resolver-side. **Layer 1:** `04` §B.9's
`Event` record names `degree?` and no `ending`; the field already ships for combat (H-266). Its use for a
margin provider's tuple is named here as a departure (`skills/layer-conformance` B4, third disposition;
C3-C16), with its readers named (`harness/chronicle.py`, the GO surface's account): it carries no actor,
target or subject (`04` PART D row 9). This file also carries the persistence of lane A's `ob_terms`
(`c5bf18a` kept them on the roll's in-memory result, F-SC-04): they persist as `terms` here, in B05 (C3-L5).

Rejected: a driver-side map (`SeasonDriver.resolution_of`) — it is outside `World`, so it is neither
hashed nor saved, and "recoverable from the log" would be false after a load. Rejected: a new `Event`
field (`margin`) — a second carrier for one fact per provider (shape divergence, CLAUDE.md §10).

## Exact edits, by owner

1. `engine/season/rosters.yaml` — beside the roster `loop/effects_combat.py::fight_ending` reads
   (`data/rosters.py:1164`), add the social provider's ending shape as data:

   ```yaml
   margin_endings:
     source: "SC-P1 (H-284): what a margin provider's contest leaves on its Events"
     values: ["pool", "ob", "net", "margin", "terms", "levels", "leverage"]     # ordered; the tuple's keys
   ```

   `terms` is `Margin.terms`, the obstacle's named terms in roster order summing to `ob` (OBS §2, §5);
   `levels` is `sigma.resolve`'s `((source, aggressor n, defender n), …)` (OBS §5); `leverage` the act's net
   sigma: what a narrative needs to say WHY (the bench was against him; he pressed; the proofs stood).
   The module returns `terms` beside the obstacle from one helper and `sigma.resolve` returns `levels`
   (it already returns `leverage`), so the host does no arithmetic.

2. `engine/season/loop/resolve.py::_fold` — after `_degree` is bound (`:406`), where
   `resolution is not None` and `resolution.result` carries a `net`/`ob` pair (the same test
   `seam/ladder.py::degree_of` makes at `:256`), build
   `tuple((k, resolution.result[src]) for k, src in MARGIN_ENDING)` with `margin` read from the
   result's margin (today's key `settled_margin`, `sigma.py:555`; A-5 removes settling, so the key names a
   real margin quantised once at the ladder, C3-L1), and seed `carried["ending"]` with it before the write loop. The fold's existing
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
net, margin, `terms` and `levels` for that act (read by calling `sigma.resolve` with the act's own generator),
and that `seam/ladder.py::degree_of` over that tuple reproduces `Event.degree`. Re-pin the seeded
goldens in the same commit and say so (CLAUDE.md §7). Named test:
`test_sc01_provider.py::test_a_social_roll_event_carries_its_margin_ending`; and
`::test_no_claim_predicate_is_a_margin_ending_after_witness` (falsifier (b)).

## Falsifier

(a) Plant a second `Margin` (net + 3) at the entry: the test must go red (the tuple follows the roll,
not a recomputation). (b) After a WITNESS barrier, no `Claim` in any ledger has a predicate drawn from
`margin_endings` — if one does, the record leaked person-side and the edit is wrong.
Narrowed: `grep -n "\.ending" engine/season/loop/witness.py engine/season/loop/epistemic.py` finds no
read of `Event.ending` at this tree; the falsifier test stays the check (an absence by grep is not a run).

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

**Lands it and tier.** The B05 batch at OBS §4 step 2, an SC `valoria-author` session on `sonnet` (`high`),
closed by the batch's `methodology-close` once. **Hash movers.** Every world in which a social roll executes
(declared; re-pinned once with B05).
