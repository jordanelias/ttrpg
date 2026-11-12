# 08 · FI · 05 — The evidence interface a contest consumes

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-13) — superseded by `08_FI_05_evidence-interface_B.md`. Kept for its comparison table; no edit of it is to be landed.

## Status: PROPOSED (an interface statement for the SC lane to cite; design-first on the SC side)

Carries audit `audits/08_FI_audit.md` F-FI-09 and resolution R-29. It states what FI supplies; what a
contest does with it is SC's (the obstacle has one owner, the module: ED-SC-0033 clause 3). Where this
meets a ruled item the conflict is named in §6 and not resolved.

## What this changes in `engine/season/` at runtime

Nothing by itself. It fixes the shape of one host-built operand (`cited`) and one deposit (a citation is
a telling), so that `speak`, `argue`, `determine`, `petition` and `interrogate` can take evidence as typed
input instead of a sum over a whole ledger.

## What exists today (opened at the line)

- `queries/world_q.py::proofs` `:852`: every deed claim in the speaker's ledger attributed to the opponent
  counts `remove_weight(c.source)`, unless the opponent holds a claim with the same `(subject, predicate)`
  (the mirror), then zero. Its own docstring names the limits: *"WHAT IS TOLD IS EVERY SUCH CLAIM THE
  SPEAKER HOLDS … one `speak` is one act, so it spends its whole inventory"*; the arrangement's admitted
  `proofs` column is not read.
- `queries/inputs.py::SocialContestInput`: `proofs: float`, `proof_step`, `reception`, `forgery_quality`
  (read for an inquiry's obstacle only).
- `rosters.yaml: proofs`: `[record, testimony, oath, confession]`, read by no production code.
- Only `speak` is heard by a room. `argue` and `determine` read no evidence (H-285: three different
  propositions gave identical bands in 40 of 40; H-301: every judge rolls the default pool at a fixed
  obstacle). `interrogate` writes nothing (H-226).

## The interface

**An item of evidence is a reference to something the citer holds.** Two carriers, both existing; no
third.

| | E1: a belief | E2: a document |
|---|---|---|
| carrier | a `Claim` in the citer's own ledger | a `Record` on the citer's live `hold` |
| says | `(subject, predicate, value)` | `(kind, subject_matter)` |
| provenance | `source`, `chain` (who told whom), `when`, `confidence` | who holds it; nothing about who wrote it (by design: no attribution) |
| proof kind (derived, never stored; `rosters.yaml: proofs`) | `testimony` (firsthand, or hearsay by `len(chain)`); `confession` where the claim was deposited from a `confession.*` Event about its own subject | `record`; `oath` is a live `commit`/`oblige` edge, already an edge, not an item |
| weight | `remove_weight(source)` × the hop discount (`teller_weight`'s owner) | `proof_step` per document of a kind the arrangement admits |

- **Held.** In the ledger or on a `hold`. What is not held cannot be cited (L.A. Noire's rule, which the
  `own_ledger` cells already enforce for `tell`, `survey`, `forge`, `reconstruct`).
- **Cited.** `Act.payload["cites"]`: a tuple of claim ids and Record ids, a choice-sourced operand
  (`rosters.yaml: choice_sourced`; `marshal`'s `role` is the precedent) ranging over the actor's own items
  about the matter's party. The host builds `cited` from exactly those; `proofs()` over the whole ledger
  becomes the control arm. Hoarding a proof is then a choice, for a chooser and a player alike.
- **A citation is a telling.** Each cited claim is deposited to those who hear the act through the told
  channel (`chain` + the citer), and a cited Record's content as a `content:` claim with no hold. Evidence
  presented in a room becomes hearsay the room can carry out of it (corpus case NPC-086's second core need).
- **Forged.** A forged Record cites as a `record` at full weight; no holder can tell. It is answered only
  by a finding: someone who has examined it holds `(record, record.forged, True)` (the found deposit) and
  cites that. A cited `record.forged` claim about a cited Record removes that Record's weight and counts
  against its citer; `decision/options.py::record` then prices him on everything else he says.
- **Concealed.** A deed done under a cover is not an attributed deed in anyone's ledger
  (`attributed_deeds` reads the anchor), so it supplies no proof until the cover is found (B10-14,
  CP-T06-09 and -07). A burned Record (`destroy_record`) cannot be cited as a `record`; what its past
  holders believe of it still can, as `testimony`.
- **Contradicted.** Today: the mirror zeroes a proof. Proposed: an opposing citation on the same cell with
  a different value, or a sighting naming a different hand for the same deed, is `_pair`'s disagreement
  (`decision/options.py`), and each side's cited support is the noisy-OR over distinct origins
  (`LedgerReader._support`), the rule the knowledge model already ruled for corroboration
  (ED-IN-0322). The mirror stays as the special case "he holds the very same thing".
- **What the contest returns to FI.** Nothing new: the act's Event is witnessed as any other. A ruling
  that rested on a cited item later found false is the pair `08_FI_03` §3 leaves to CR-83.

## Edits, by owner (SC's to schedule)

1. `queries/world_q.py`: `cited(w, act) -> tuple` beside `proofs`, the host's typed reading of
   `payload["cites"]` against the actor's ledger and holds (an id he does not hold is dropped, as a
   malformed operand).
2. `queries/inputs.py::SocialContestInput`: `proofs: float` is computed from `cited`; add
   `rebuttals: float` (the opponent's cited contradictions). Raw operands; the module composes.
3. `decision/options.py::operand_bags`: `cites` ranges over the top-`k` items by weight (`k` a fixture,
   control 0 = today's automatic sum).
4. `loop/witness.py`: the told deposit also fires for an Event whose act carries `cites`.
5. `arrangements.yaml`'s `proofs` column gets its reader (which kinds a room admits; H-216, H-281).

## Gate (execution artifact)

On a hand-built hearing: the same `speak` with and without one cited firsthand deed moves the obstacle by
`proof_step`; citing a forged sheet moves it as a true one; the opponent citing a finding of the forgery
reverses it; a bystander on the bench holds the cited claim afterwards with the citer on its chain.
Control: `k = 0` reproduces today's hash.

## Falsifier

A contest whose band is identical with and without any citation, at a non-zero `proof_step` (H-285's
reading, re-run against the new operand).

## §6 Conflicts with ruled items, named and not resolved

- *One `speak` is one act and spends its whole inventory* (`proofs`' docstring; the nested run of
  `21_RECONCILIATION.md` step 15 is unbuilt). Citing one item at a time inside a hearing needs that run;
  this interface gives a single act a chosen subset and does not build the run.
- *The obstacle has a single owner* (ED-SC-0033..0039): respected (raw operands in, the module composes),
  but `rebuttals` is a second party's contribution to one matter's draw, and ED-SC-0038's per-matter pick
  does not say whether an opponent's citations are admitted there.
- *No verifier* (2026-08-18 Q5): respected. A forgery is exposed by a person's finding, cited by a person.

## NERS reading

N: 14 corpus cases need testimony, confession or denunciation to move a ruling, and the bench today hears
none of it. R: a case built from what is held, cited, forged and contradicted is creativity in approach
and the no-player half at once (an NPC prosecutor cites; an NPC defendant rebuts). S: two existing
carriers, one pairing step, one corroboration rule, one deposit channel; no second ladder for
reliability. E, last: one operand and one deposit trigger.

## Cost class

Design-first (SC), then small builds. Lanes: SC (owner), FI (the two carriers, the told deposit), CHAR
(`record`).
