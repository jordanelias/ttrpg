# 08 · FI · 05-B — The evidence interface a contest consumes (supersedes `08_FI_05_evidence-interface.md`)

## Status: PROPOSED (an interface statement; the consumer is SC's and design-first there)

Supersedes `08_FI_05_evidence-interface.md` (first FI lane). Carries `audits/08_FI_audit.md` F-FI-09, R-29 and
`audits/08_FI_audit_addendum_B.md` §B4, R-41, R-42, R-43. Written against `05_SC_evidence_and_rebuttal.md`
(SC-P8) and `05_SC_playable_hearing.md` (SC-P3), which it cites and does not redo. Where it meets a ruled
item the conflict is named in §7 and not resolved. No code is made to read `.designs/` or `.audit/`.

## What this changes in `engine/season/` at runtime

Nothing until SC schedules the consumer. It fixes five things so that the consumer can be built once:
the operand's name and shape, what is entered on the case file, what is deposited to the room, the three
relations by which an item is answered, and the one precondition (`08_FI_06`). With no item cited, every
contest rolls as today (the control).

## Why the first version is superseded

Three statements of this interface now exist and disagree in shape:

| | first FI lane (`08_FI_05`) | SC lane (SC-P8) | ratified 2026-07-05 on the retired Key substrate (ED-IN-0011; narrative-engine design v2 §5, in `.audit/`, intent only) |
|---|---|---|---|
| operand | `payload["cites"]`: ids | `speak`'s `proofs: [{kind, ref}]` | `evidence{key_ref, witnesses, chain_strength, recency, asserter_standing}` |
| record of what was cited | none | a stage on the case-file Record | a precedent store, a commitment store |
| the room learns it | yes (a citation is a telling) | no | — |
| answering | `rebuttals: float` | a `struck` stage on a held contradiction | unbound claim = *bluster*, attackable |
| forgery | answered by a cited finding | an `examine` whose finding *names it forged*, as a new finding term | — |

The full reading also found two things neither lane had: a cited killing names nobody (addendum F-FI-11),
and a case-file entry that is a claim id cannot be compared with an answer without opening the first
speaker's ledger, which the fold may not do (F8).

## The interface, decided

**E-1. One operand, references only.** `Act.payload["cites"]`: a tuple of ids, each a `Claim` in the
citer's own ledger or a `Record` on his live `hold`. Choice-sourced (`rosters.yaml: choice_sourced`), so a
chooser and a player pick from the same Candidates (SC-P3 edit 2 forms the variants). An id he does not
hold is refused at the cell, before any draw, as `tell`'s unheld claim is. **The proof kind is derived,
never declared:**

| the item | derived kind (`rosters.yaml: proofs`) | derived weight |
|---|---|---|
| a deed claim, untold | `testimony` | 1 |
| a deed claim with a chain | `testimony` | the hop discount `teller_weight` already owns |
| a claim of a `confession.*` kind about its own subject | `confession` | 1 |
| a Record | `record` | 1 |
| a live `commit` or `oblige` edge | `oath` | it is an edge, cited by its Tenure id |

One reader: `queries/person_q.py::proof_kind(c) -> str` for claims (World-free), and the host's hold check
for a Record. The arrangement row's `proofs:` list admits or drops a kind (its first reader, as SC-P8 has
it).

**E-2. The case file holds what was said.** When a `speak` that cites grades `Success` or better, the host
appends one stage per cited item to the matter's case file (CR-61's Record; SC-P8 edit 2). For a claim the
stage carries the `Said` (`state/carriers.py`: subject, predicate, value, confidence, chain), the citer and
the act id; for a Record, the Record's id. `Said` is the carrier the told channel already uses for "what
was said", so no carrier is added. A later answer is compared with the stage, never with a ledger.

**E-3. A citation is a telling.** `loop/witness.py`'s told deposit also fires for an Event whose act
carries `cites`: each cited claim lands in every admitted hearer's ledger as a told copy, chain extended by
the citer, through the same guard, refraction and credit as any telling. A cited Record's content lands as
a `content:<kind>` claim with no hold. The bench and the bystanders leave holding the evidence, with the
citer on its chain.

**E-4. Two carriers, one fact each.** The case file is the proceeding's record (it persists across
sittings and can be forged, seized or burned, like any Record). The told copies are what people believe.
Neither restates the other: the stage is what was put before the room, the claim is what a hearer made of
it.

**E-5. Three ways to answer an item.** Each compares held things; none reads the Event log.

1. *Contradiction.* An answering `speak` cites a claim on the same `(subject, predicate)` with a different
   value. Asked of the one owner of "pairs and disagrees" that SC-P8 names (`decision.agreement`, already
   called resolver-side by `loop/matter.py::_standing_crossings`) `[as cited by SC-P8; not opened here]`.
2. *Impeachment of a document.* An answering `speak` cites a held deed claim whose subject is the cited
   Record and whose kind is a `rosters.yaml: covert_kinds` member (today `record.forged`). The found deposit
   mints exactly that claim, `(record id, record.forged, True)`, source `inferred`, to whoever examined the
   paper and graded `Partial` or better (`loop/witness.py::_found_claims`; at `Partial` the hand is withheld
   and the claim on the written thing still lands). So **no finding term is added** (SC-P8's request 2 is
   met by an existing claim), and a finder who told someone has made that person able to impeach too: the
   kind is unpaired, so the told copy keeps its subject.
3. *Impeachment of a witness.* No operand. `world_q.reception` already sums what each judge holds of the
   speaker's deeds, signed by the judge's own pursuits; a speaker the bench knows as a forger or a liar
   stands lower by the path that exists, and each judge's `record` of him re-grades whatever he passed on.

**E-6. An answer is a rolled act; no item decides a case.** A contradiction or an impeachment strikes an
entered item only when the answering `speak` itself grades `Success` or better (SC-P8 edit 3). The verdict
remains `determine`'s roll, moved by `proof_step` per standing item through `world_q.hearing` (SC-P8 edit
4). A false item that answers a true one strikes it; that is the risk a forger runs and the reason a
finding matters.

**E-7. Bluster is the control; citing costs disclosure.** An act that cites nothing rolls exactly as
today. There is no penalty number for an unsupported claim. What citing costs is what E-2 to E-5 already
do: the room learns what the citer holds and from whom (the chain names his source), a forged paper is put
where anyone present may examine it, and the item can be struck on the record.

**E-8. Precondition: a killing's hand must travel.** Until `08_FI_06` lands, a claim of a death, a wound
or a seat's closing cited before a bench deposits "it happened" and names no one, and only an eyewitness
holds a proof against the accused at all. This interface is buildable without it for every deed kind one
verb row emits (forging, seizure, requisition, arrest, a field won) and not for homicide.

## What FI supplies (edits at FI's owners)

1. `queries/person_q.py`: `proof_kind(c)` (the table in E-1); `impeaches(c, record_id) -> bool`
   (`is_deed(c)`, subject is the Record, predicate in `COVERT_KINDS`). Both World-free.
2. `loop/witness.py`: the told deposit's trigger widened from "the act carries `said`" to "the act carries
   `said` or `cites`", one loop over the cited claims; nothing else in the deposit changes.
3. `08_FI_06` (the pairing travels), so a cited paired deed carries its hand into E-2's `Said` and E-3's
   told copies.
4. `08_FI_03` §2 as amended by `08_FI_07` §2 (an admitted look teaches its reads), so that an inquirer comes
   to hold the firsthand cell that contradicts a told one.

## What SC builds (named, by SC-P8's own numbering; not authored here)

SC-P8 edit 1 with `cites` in place of `{kind, ref}`; edit 2 with the `Said` in the stage; edits 3 and 4
unchanged; edit 5 read as E-5 item 2; SC-P3 edits 2 and 3. `queries/inputs.py::SocialContestInput` gains
no field: `proofs` stays one float, now computed from standing stages.

## Left to SC, with the options stated

- *Precedent as a proof kind.* A held claim of an earlier `matter.determined` on a like matter. It needs a
  fifth `proofs` member and a rule for "like"; the ratified 2026-07-05 design called it the precedent store.
- *The opponent's own word.* His live `commit` to a Proposition that contradicts his plea, cited against
  him (that design's commitment store; SC-02's mirror made public).
- *A judge whom evidence moves more, or less.* The archived Pressure Points (Evidence, Consequence,
  Authority, Loyalty) and corpus cases NPC-001 and NPC-071 want it; SC-P7's `trait_advantages` roster is
  the door, with `side: subject`.
- *Not taken now:* the companion's softened Triangle Strategy rule (an unsupported case may not reach
  Overwhelming, through `dice_engine.BandExtension`). `determine`'s three non-Failure bands open the same
  edge today (H-301; H-162 item 2), so the veto would change nothing. It becomes worth building the day a
  disposal edge's `degree` has a reader.

## Gate (execution artifact)

On SC-P3's `build_hearing` world, extended with one forged Record and one examiner:
(a) the accuser cites a firsthand deed claim: the case file gains one stage carrying its `Said`; `hearing`
rises by `proof_step`; each judge holds the told copy with the accuser on its chain.
(b) the accused answers with a held claim on the same cell and a different value, at a planted `Success`:
one `struck` stage; `hearing` returns.
(c) the accuser cites the forged Record: `hearing` rises as for a true one.
(d) the examiner, holding `(record, record.forged, True)` from a `Partial` find, answers: the Record's stage
is struck; after the barrier each judge holds the forging as a told claim and `reception` of the accuser in
the next `speak` is lower than in (a).
(e) with `08_FI_06` on, a cited `(victim, person.died, True)` leaves each judge able to name the accused
(`deed_doers`); with it off, nobody but the eyewitness can.
Control: `cites` empty throughout reproduces SC-P3's `--auto` content hash.

## Falsifiers

- An answer whose item has the same value strikes nothing.
- A cited id the citer does not hold is refused before the draw.
- If any step reads a ledger other than the actor's own or a judge's own, the entry is not carrying the
  `Said` and E-2 is not built.
- If (d) lowers nobody's `reception`, the forging's deed cell is unauthored for the bench's pursuits; report
  it and do not add a term.

## §7 Conflicts with ruled items, named and not resolved

- **Proofs on the obstacle, not in the pool** (ED-SC-0034; the archived *"+1D per Finding"* and *"+2D
  Recall"*): the built placement is kept; SC's audit lists the difference (G-33).
- **One `speak` is one act.** Presenting item by item inside one sitting needs the nested run
  (`21_RECONCILIATION.md` step 15), which is unbuilt. Here a hearing is several `speak` acts over rounds
  (SC-P3), each with its chosen subset.
- **Hearing by presence** (H-323; private whispers are not built). A citation reaches everyone in the
  room. Showing evidence privately to one judge is not representable and is not proposed.
- **No verifier** (2026-08-18 Q5). Kept: every comparison is between two held items, and a false one can
  win.
- **Investigation is not a contest** (SM-3). Kept: examining a cited paper is an ordinary inquiry; nothing
  here adds a prize to one.

## NERS reading

N: without it the bench rules on a default roll and the inquiry game has no destination; top-down (a trial
is evidence answered), bottom-up (ledger, Record, `Said`, told channel, found deposit and `reception` all
exist), lateral (it is `tell`'s rule applied to `speak`), diagonal (fieldwork's product is the hearing's
input and the hearing's record is fieldwork's object). R: which item to cite, which to hold back, whether
to stake a forgery; without a player, an NPC who holds the answering item strikes the proof, and a bench
carries what it heard out of the room. S: no second arithmetic for reliability (the hop discount, the
corroboration rule and `reception` are the existing owners); *pauses correctly* is SC-P3's to show. E, last:
one operand, one deposit trigger, two small readers, against trials that today are rolls.

## Cost class

FI's four edits: edit (items 1 and 2), small build (`08_FI_06`), small build (`08_FI_07` §2). SC's consumer:
design-first, then small builds, after CR-61, SC-02 and SC-P3.
