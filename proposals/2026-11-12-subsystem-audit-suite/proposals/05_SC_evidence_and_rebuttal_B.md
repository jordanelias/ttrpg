# Evidence filed, presented and answered: the case file as the board, one standing rule, one evidence term

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-01 — striking by weight replaced by the answering act's graded draw (FI E-6 adopted, banded); filing stays draw-free bookkeeping.

## Status: PROPOSED — supersedes `05_SC_evidence_and_rebuttal.md` (SC-P8). Consumes `08_FI_05_evidence-interface_B.md` (FI's E-1 to E-8) and differs from it at one point, named below.

Source: `audits/05_SC_audit_addendum_B.md` §B3 (the kernel's `Dossier`, `rebut`, `EVIDENCE_CAP`
carried), §B4.2, G-42 to G-45, C-4; `audits/05_SC_audit.md` F-SC-14 and §16; `08_FI_05_…_B.md`;
`12_ARCS_cited_evidence.md`. It is the evidence half of `05_SC_playable_hearing_B.md` and the
`evidence` term of `05_SC_obstacle_difficulty_and_modifiers_B.md`. No code is made to read
`.designs/` or `.audit/`.

## What it changes in `engine/season/` at runtime

With no `speak` carrying `cites` (every computed `speak` until the chooser forms the variants, edit
6): nothing; the `evidence` term reads today's `world_q.proofs` (the control arm, kept until the gate
passes). With citing on: a `speak` on a docketed matter may name held items; each admitted item is
entered on the matter's case file and told to the room; the closing draw of the matter's `determine`
(or of the sitting) reads the items left standing through one function. Items never touch the pool
(`ED-SC-0034` (3)).

## The problem (evidence)

1. Evidence is typed where held (`Claim`, `Record`) and one float where used:
   `SocialContestInput.proofs`, the sum of `remove_weight` over the speaker's unmirrored deed claims
   about the subject (`queries/world_q.py:852-879`). No act names an item, so none can be answered,
   struck or remembered (SC-P8 problem 1; first audit F-SC-14).
2. The only answer to an item is the silent mirror: the opponent merely *holding* the same cell zeroes
   it, whoever he is and whether he speaks, and WITNESS makes that total (H-216: 49 of 49).
3. Three statements of the operand disagree in shape (`cites: (ids)`; `proofs: [{kind, ref}]`; an
   automatic count) — FI's comparison table in `08_FI_05_…_B.md`.
4. SC-P8 names `decision.agreement` as the owner of "contradicts". That function pairs by predicate on
   the `person_predicates` roster; the one pairing step is `_pair`
   (`decision/options.py:1491-1521`: same key, whole value, `==`) — addendum C-4. FI's `_B` repeats
   SC-P8's citation `[as cited; not opened]`.
5. At the shipped ceiling arm the evidence term is clipped to nothing against a strong opponent
   (F-SC-16, measured: pool 2 against a score of 8, proofs 0 to 4, obstacle 2.842 in every row).

## The resolution, decided

### What is taken from FI unchanged

E-1 (the operand `Act.payload["cites"]`, ids only, refused before the draw if not held; the kind
derived by `person_q.proof_kind`, never declared; the arrangement's `proofs:` admits), E-2 (the stage
carries the `Said` for a claim, the id for a Record, so no answer ever reads the citer's ledger), E-3
(a citation is a telling, through the existing told deposit), E-4 (the stage and the told copies are
two facts), E-5 items 2 and 3 (a document impeached by a held `(record, record.forged, True)` claim,
which the found deposit already mints; a witness impeached through `reception`), E-7 (citing nothing
is the control; citing costs disclosure), E-8 (homicide waits on `08_FI_06`). Ladder step 4: FI owns
the carriers.

### Where this differs from FI's E-6, and why

*(Reconciled by `audits/18_DETERMINISM_SWEEP.md` D-01: the earlier text of this section made entering
and striking deterministic; that breaks the standing rule. The section now agrees with FI's E-6, graded.)*

**Filing is bookkeeping; whether an item stands against an answer is a draw.** Putting a held item on
the case file is an act the citer may attempt (an eligibility: he holds it, the row admits its kind) and
is recorded without a roll; whether a presented item survives a contradiction or an impeachment could go
either way for the people in the room, so it goes by a draw, at the answering act (FI's E-6). The
division the three-lens audit recovered (`3L/05` §4.2: an orator cannot make a contract more probative)
is kept by putting the items' **weights into the obstacle**, not the orator into the weights: the
answerer's pool is his own (`speak`'s pool through the one roller), the obstacle is the answer's task
difficulty plus the weight difference, so a heavy answer to a light item is likely and never certain.
What E-6 protects survives: no item decides a case, the verdict is still a draw, and one rule serves the
room and the out-of-room path (`present` stays draw-free as filing; `answer` is rolled in both).
Whether admission to the file should itself ride the citing act's band (FI's E-2) is
`19_LACUNA_admission_rides_the_citing_draw.md`'s question; this file defers to it.

### The three operations, one owner each

| operation | when | rule | owner |
|---|---|---|---|
| **file** | a `speak` on a docketed matter carrying `cites` (the filing act; any band) | one `filed` stage per held, admitted item: `(tick, "filed", side, rung, Said or record id, weight, origin, act id)`. The speech's band still decides its own matter effect (`matter.advanced` …) | host: `loop/effects_information.py`, the `speak` effect, under its own token |
| **present** | in a sitting, the `present` move; with no sitting, every filed item is presented at close | an item counts only once presented | module: `modules/social_contest/evidence.py` |
| **stand** | at every board change, and at close | `standing(presented, findings) -> (standing, struck, faults)`, the rules below | module, one pure function, World-free |

`side` is relative to the matter as docketed: `for` (supports what the docket asks: the charge, the
petition) or `against` (the party's answer). `rung` is derived from the kind: every member of
`rosters.yaml: proofs` bears on `fact` today, by a new column on that roster (`bears_on`); a fifth
member (precedent, bearing on `definition`) is FI's "left to SC" item and is not added here.
`weight` is FI's derived weight (1 for a firsthand claim or a Record, `teller_weight`'s hop discount
for a told one); `origin` is the root of the claim's chain, or the Record's maker as far as a held
claim says, else the Record itself.

### `standing`: the rules, in order

Rules 1 and 2 no longer decide from weight; they apply the **band of the answering act's draw**, which
the host rolled once through `engine/dice_engine` (`degree_from_net`) and hands to `standing` as data
(`Exhibit.answered_band`). `standing` stays pure and World-free and rolls nothing. The answer's odds:
pool = the answerer's `speak` pool (the one pool builder); obstacle = `answer_ob` (a fixture, proposed 2,
NUMBER row) `+ proof_step × (w_answered − w_answer)` for a contradiction, `− forged_claim.confidence` for
an impeachment, plus the room's existing modifiers (reception, venue). Each term is written to
`Margin.terms` (the reason trail).

1. **Forgery.** On an impeaching answer (a presented `(record, record.forged, True)` claim, E-5 item 2):
   `Failure` the Record stands and the impeacher bears `failed_impeachment` (a told deposit, so his
   `reception` falls by the existing path); `Partial` the Record's weight is halved; `Success` the
   Record's item is struck; `Overwhelming` it and every item of the same origin are struck and the
   `forgery_found` fault is recorded against that side.
2. **Contradiction** (the answer). Two presented items of opposing sides on the same
   `(subject, predicate)` with different values, by `_pair`'s rule exposed once as
   `decision/options.py::contradicts(a, b) -> bool` (no second copy): `Failure` the answered item
   stands; `Partial` both are halved; `Success` the answered item is struck; `Overwhelming` it is struck
   and its citer bears the `self_contradiction` fault only if he cited it knowingly (a held contrary
   claim), else `discredited_source` against its origin. An item presented with no answering act is
   never struck. Same side, opposing values: the `self_contradiction` fault, no draw (bookkeeping: the
   citer's own file disagrees with itself), and the lighter is withdrawn.
3. **Agreement** (the mirror made public). The same cell, same value, presented by both sides: it
   counts for neither. This is SC-02's commit mirror with "held" replaced by "put before the room"; an
   item merely held by the opponent no longer zeroes anything (problem 2).
4. **Corroboration.** The same cell, same value, same side, from **distinct** origins: one item whose
   weight is `1 − Π(1 − wᵢ)` (FI's ruled noisy-OR, `ED-IN-0322`), capped at `evidence_cap`; the same
   origin twice counts once. This is the kernel's diminishing corroboration, on the tree's own rule.

### The evidence term

`proofs = Σ weight(standing, side = for)`, `rebuttals = Σ weight(standing, side = against)`, both
carried raw on `SocialContestInput` (FI: `proofs` stays one float; `rebuttals` is
`05_SC_obstacle_difficulty_and_modifiers_B.md` edit 4's). For the determiner's draw the `evidence`
term is `proof_step × (rebuttals − proofs)`: what supports the docket lowers the obstacle to carry
it, the party's standing answers raise it. For a party's own `speak` the sign is the speaker's
side. The favourable half is subtracted after the ceiling (the obstacle proposal's bound; G-41), so
four standing items against a strong opponent are four different obstacles.

### How an NPC builds a case and is answered by another

No branch for a player. The one chooser forms `speak` variants with `cites` (edit 6): none, all held
admitted items about the subject, and each held item that contradicts an item already filed against
his side (an answer). It scores them with its existing terms; what a variant costs is what E-7 says
(disclosure: the room learns the item and its chain). A second NPC who holds the contradicting cell
files it the same way. In a sitting the NPC decider (`05_SC_playable_hearing_B.md`) chooses order and
what to withhold; out of a sitting, everything filed is presented at close.

### Falsehood, forgery, concealment, and later trust

- A false claim filed in good faith stands until answered by a heavier contradicting item; a false
  item can strike a true one (no verifier, 2026-08-18 Q5, kept).
- A forged Record counts as any Record until someone who holds the forged claim presents it; then it
  and everything of its origin is struck, and the finding's told deposit (E-3) lowers the citer's
  `reception` and `teller_weight` in every hearer by the existing paths. Nothing new is written for
  trust.
- A concealed item is unheld and cannot be cited; no rule.

## Exact edits, by owner

1. `engine/season/rosters.yaml: proofs` — a `bears_on` column (`fact` for all four members); a
   fixture `evidence_cap` (proposed 2.0, NUMBER row, three-point sweep).
2. `engine/season/decision/options.py` — `contradicts(a, b)`, the predicate `_pair` already applies,
   exposed once; `_pair` calls it.
3. `modules/social_contest/evidence.py` (new) — `Exhibit` (as `05_SC_playable_hearing_B.md` types it)
   and `standing(presented, findings) -> (standing, struck, faults)`. The module names no
   `engine/season` module and restates no pairing rule: the host builder computes the relation with
   `contradicts` and hands it over as data, each `Exhibit` gaining `pairs: ((exhibit id, "contradicts"
   | "agrees"), …)` over the other filed exhibits. `standing` reads only that field, so the rule lives
   once, in `decision/options.py`.
4. `engine/season/loop/effects_information.py` — the `speak` effect writes `filed` stages for its
   admitted cites (CR-61's case-file Record; FI E-2's `Said`).
5. `engine/season/seam/wrappers/sigma.py::contest_input` — for a docketed matter, `proofs` and
   `rebuttals` from `standing` over the case file's filed stages (every filed item presented); the
   control arm (`evidence_from: ledger`, a fixture) keeps `world_q.proofs`.
6. `engine/season/decision/options.py` — the `speak` variants above (FI `08_FI_05` edit 3's
   Candidate variants; SC-P3 edit 2's place).
7. `references/module_contracts.yaml` — `social_contest.evidence` is not a composition role: it is
   called by `roll`'s host builder and by `hear`, never by the loop.

## Gate (execution artifacts)

On `build_hearing(seed)` (`05_SC_playable_hearing_B.md` edit 9), `PYTHONHASHSEED=0`:

1. The accuser files two firsthand deed claims and a Record: three `filed` stages; each judge holds
   the told copies with the accuser on the chain; at close, `proofs` = 3.0 and the determiner's
   obstacle is lower by `3 × proof_step` than with nothing filed (both read off `Margin.terms`).
2. The accused answers one of the accuser's cells with a different value and weight 1, over 200
   seeds: all four bands occur; the answered item stands at `Failure`, both halve at `Partial`, the
   item is struck at `Success`/`Overwhelming`; the struck share rises when the answer's weight rises
   (control: answer weight 0.5 against 1.0 strikes less often than 1.0 against 0.5, and neither share
   is 0 or 1).
3. The examiner, holding `(record, record.forged, True)` from a `Partial` find, answers with it over
   200 seeds: the Record is struck in a share strictly between 0 and 1, and every origin-wide strike is
   an `Overwhelming`; on a strike the next `speak` by the accuser shows a lower `reception` term than
   in step 1.
4. Two items of the same cell and value from distinct origins, weights 0.5 and 0.5: one item of 0.75.
   From one origin: 0.5.
5. Control: `cites` empty throughout reproduces the base commit's content hash.

## Falsifier

An answer of the same value strikes nothing (it is agreement, rule 3). A cited id the citer does not
hold is refused before the draw. If an item of a kind the row does not admit changes `proofs`, the
admission read is wrong. If any step reads a ledger other than the actor's own or a judge's own, the
stage is not carrying the `Said`. If pool 2 against a score of 8 gives the same obstacle with 0 and 4
standing items, the bound order has not landed.

## Conflicts with ruled items — named, not resolved

- `ED-SC-0034` (3) "pool only": the items move the obstacle, the built placement; the archived
  *"+1D per Finding cited"* is not restored.
- Investigation is not a contest (SM-3): examining a cited paper stays an ordinary inquiry.
- Hearing by presence (H-323): a filing reaches everyone in the room; private exhibition to one judge is
  not representable.

## NERS reading

- **N**: top-down a trial is evidence answered; bottom-up every carrier exists (ledger, Record, `Said`,
  told deposit, found deposit, `_pair`, noisy-OR); lateral it is `tell`'s held-claim rule on `speak`;
  diagonal fieldwork's product is the hearing's input and the case file is fieldwork's next object.
- **R**: what to file and what to withhold, whether to stake a forgery, whom to bring as a second
  origin; without a player, an NPC holding the answer strikes the proof and the bench carries the
  record out of the room. Complete at its extremes: nothing filed is today's roll; everything struck
  is a matter decided on argument alone.
- **S**: one standing rule in the room and out of it; one corroboration rule (FI's); the term in the
  obstacle's units; no second trust arithmetic.
- **E**, last: one operand, one stage kind, one pure function, one column, against a trial a player can
  read item by item.

## Cost class

Small build, after CR-61 (the case file), SC-02 (the re-source) and FI's edits 1 and 2.
