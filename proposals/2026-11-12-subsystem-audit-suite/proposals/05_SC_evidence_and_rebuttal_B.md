# Evidence filed, presented and answered: the case file as the board, one standing rule, one evidence term

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-01 — striking by weight replaced by the answering act's graded draw (FI E-6 adopted, banded); filing stays draw-free bookkeeping.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-01, C-05, C-10) — three changes. (1) Entry: an item is entered by the band of the speech that cites it (`19_LACUNA_admission_rides_the_citing_draw.md` decides the question this file had deferred): the "recorded without a roll" sentence and the **file** row are rewritten. (2) The evidence term: standing items reach the roll as `proofs` levels on the leverage channel for the side they stand for, never as an obstacle subtraction (Jordan, A-25; `U5c_SC_one_obstacle_form.md` §3); "The evidence term" is rewritten and `proof_step` is not added. (3) "Falsehood, forgery" no longer has a false item fall to a heavier one or a forgery's origin struck with certainty: both go by the answering draw's band (rule 2).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row EVID_B (VIOLATES), §2 row `answer_ob + proof_step`, §7, §7b-9, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger R-25, S-01, S-02, §2 *evidence* edge; `unified/U1_GLOSSARY.md` *exhibit*; `unified/U3_CONFLICT_LEDGER.md` C3-C1, C3-Y3, §9, §11). Layer 1 rewrite (`holonic` §43: a module is reached by a composition row, never an import; `04` §A.2: the adapter owns nothing, ever; `04` PART D row 30: one ladder): `standing` runs **inside** `modules/social_contest/` (called by `roll.py` and `hearing.py`), the host passes the case file's exhibits in as data and reads the `proofs` levels back from the roll's record, so edit 7 is true; `Exhibit.answered_band` is the answering act's own degree from the one ladder, not a host-side second grading call; rule 2's same-side case is an eligibility refusal at filing, not a fixed outcome (the standing rule); the answer's weight difference is in `answer_step` units now that `proof_step` is deleted (R2 §7b-9 #4, `[ASSUMPTION]`; U3 §11 left the unit to U1, which did not decide it); `Exhibit` is HEAR_B's record, cited (C3-C1); the stale "lower by `3 × proof_step`" and "the items move the obstacle" are replaced by the levels reading (A-25); named tests; lands-it and tier.

**Lands in batch:** B24, after HEAR_B's records and ADM's entry draw and before FI_05_B's interface (C3-Y3). **Depends on:** `05_SC_playable_hearing_B.md` (B24), `19_LACUNA_admission_rides_the_citing_draw.md` (B24), `U5c_SC_one_obstacle_form.md` (B05, the `proofs` source), `05_SC_contest_record_on_event.md` (B05, the record), plan positions CR-61 (the case file) and SC-02 (the re-source) `[PL]`.

## Status: PROPOSED — supersedes `05_SC_evidence_and_rebuttal.md` (SC-P8). Consumes `08_FI_05_evidence-interface_B.md` (FI's E-1 to E-8) and differs from it at one point, named below.

Source: `audits/05_SC_audit_addendum_B.md` §B3 (the kernel's `Dossier`, `rebut`, `EVIDENCE_CAP`
carried), §B4.2, G-42 to G-45, C-4; `audits/05_SC_audit.md` F-SC-14 and §16; `08_FI_05_…_B.md`;
`12_ARCS_cited_evidence.md`. It is the evidence half of `05_SC_playable_hearing_B.md` and fills the
`proofs` leverage source of `U5c_SC_one_obstacle_form.md` §3 (SC-B's `evidence` term is superseded). No code is made to read
`.designs/` or `.audit/`.

## What it changes in `engine/season/` at runtime

With no `speak` carrying `cites` (every computed `speak` until the chooser forms the variants, edit
6): nothing; the `proofs` source reads today's `world_q.proofs` (the control arm, kept until the gate
passes). With citing on: a `speak` on a docketed matter may name held items; each admitted item is
entered on the matter's case file by the speech's band and told to the room; the closing draw of the
matter's `determine` (or of the sitting) reads the items left standing through one function, inside the
module. Items never touch the pool (`ED-SC-0034` (3)) and never lower the obstacle (A-25): they are levels.

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

**Whether an item is entered is the citing speech's draw; whether it stands against an answer is the
answering act's draw.** Citing a held item is an act the citer may attempt (an eligibility: he holds it,
the row admits its kind). What the file then holds is read off the band of that speech
(`19_LACUNA_admission_rides_the_citing_draw.md`): `Failure` enters nothing, `Partial` enters the item at
half weight, `Success` enters it, `Overwhelming` enters it with the `first` mark (an answer to it meets the
`first_heard` obstacle term). Whether a presented item survives a contradiction or an impeachment could go
either way for the people in the room, so it goes by a draw, at the answering act (FI's E-6). The
division the three-lens audit recovered (`3L/05` §4.2: an orator cannot make a contract more probative)
is kept by putting the items' **weights into the answer's odds**, not the orator into the weights: the
answerer's pool is his own (`speak`'s pool through the one roller); a heavier answered item adds the
hostile term `answer_step × (w_answered − w_answer)` to the answer's obstacle, a heavier answer reaches the
answerer as `proofs` levels (never a subtraction, A-25), so a heavy answer to a light item is likely and
never certain.
What E-6 protects survives: no item decides a case, the verdict is still a draw, and one rule serves the
room and the out-of-room path (`present` adds no draw of its own: it orders items already entered;
`answer` is rolled in both).

### The three operations, one owner each

| operation | when | rule | owner |
|---|---|---|---|
| **file** | a `speak` on a docketed matter carrying `cites` (the filing act; entered by its band: `Failure` none, `Partial` at half weight, `Success` whole, `Overwhelming` whole with the `first` mark) | one `filed` stage per held, admitted item the band enters: `(tick, "filed", side, rung, Said or record id, weight, origin, act id)`. The speech's band still decides its own matter effect (`matter.advanced` …) | host: `loop/effects_information.py`, the `speak` effect, under its own token |
| **present** | in a sitting, the `present` move; with no sitting, every filed item is presented at close | an item counts only once presented | module: `modules/social_contest/evidence.py`, called by `hearing.py` / `roll.py` |
| **stand** | at every board change, and at close | `standing(presented, findings) -> (standing, struck, faults)`, the rules below | module, one pure function, World-free, called only from inside `modules/social_contest/` |

`side` is relative to the matter as docketed: `for` (supports what the docket asks: the charge, the
petition) or `against` (the party's answer). `rung` is derived from the kind: every member of
`rosters.yaml: proofs` bears on `fact` today, by a new column on that roster (`bears_on`); a fifth
member (precedent, bearing on `definition`) is FI's "left to SC" item and is not added here.
`weight` is FI's derived weight (1 for a firsthand claim or a Record, `teller_weight`'s hop discount
for a told one); `origin` is the root of the claim's chain, or the Record's maker as far as a held
claim says, else the Record itself.

### `standing`: the rules, in order

Rules 1 and 2 no longer decide from weight; they apply the **band of the answering act's draw**
(`Exhibit.answered_band`), which is one ladder's band, never a second grading call by the host: out of a
sitting, the `Event.degree` of the answering `speak` act (a `speak` that declares `contests:` and carries
`answers: [stage index, …]`), set by `seam/ladder.py::degree_of`; in a sitting, the `answer` move's margin
graded in-module by the one ladder owner `degree_from_net` (as HEAR_B grades every in-run draw).
`standing` stays pure and World-free and rolls nothing. The answer's odds: pool = the answerer's `speak`
pool (the one pool builder); obstacle = the one form (OBS §2) with the hostile terms `answer_ob` (a fixture,
proposed 2, NUMBER row) and `answer_step × max(0, w_answered − w_answer)` for a contradiction
(`answer_step`: control 0, first value 0.25, `[ASSUMPTION: a new fixture rather than reviving `proof_step`,
which OBS §3 deletes; basis R2 §7b-9 #4]`); a heavier answer, and for an impeachment the finding's
confidence, reach the answerer as `proofs` levels (A-25); plus the room's existing hostile terms
(reception, venue). Each term is written to `Margin.terms` and each level to `levels` (the reason trail).

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
   never struck. Same side, opposing values: refused at the filing act — the `speak` carrying a cite that
   contradicts an item already standing for the citer's own side is refused with the refusal kind
   `self_contradiction` at its `cites` cell (an eligibility refusal, which emits and decides no outcome),
   so no item is withdrawn by a fixed rule.
3. **Agreement** (the mirror made public). The same cell, same value, presented by both sides: it
   counts for neither. This is SC-02's commit mirror with "held" replaced by "put before the room"; an
   item merely held by the opponent no longer zeroes anything (problem 2).
4. **Corroboration.** The same cell, same value, same side, from **distinct** origins: one item whose
   weight is `1 − Π(1 − wᵢ)` (FI's ruled noisy-OR, `ED-IN-0322`), capped at `evidence_cap`; the same
   origin twice counts once. This is the kernel's diminishing corroboration, on the tree's own rule.

### The evidence term

`proofs = Σ weight(standing, side = for)`, `rebuttals = Σ weight(standing, side = against)`, computed
**inside the module** from `standing` over the exhibits the host passes in (`SocialContestInput.exhibits`,
`HearingInput.exhibits`: the case file's `filed` stages as HEAR_B's `Exhibit`s, each with its `pairs`) and
reported back on the roll's record (`levels`, SC-P1). Neither sum enters the obstacle. Each reaches the roll
as the `proofs` leverage of `U5c_SC_one_obstacle_form.md` §3: one `proof_level` per whole unit of weight
standing for the roller's side, and the same against him for the other side's; for a docketed matter with
exhibits the module adds these levels to the leverage it applies (`proof_level` carried raw on the input),
and the host's `proofs` source returns nothing for it `[ASSUMPTION: the module composes the proofs levels
when exhibits are present, so the standing rule is never computed host-side — basis R2 §7b-9 #1 and `holonic`
§43]`; with no exhibits the host's `proofs` source reads `world_q.proofs` (the control). For
the determiner's draw the roller's side is the docket's; for a party's own `speak` it is the speaker's.
Four standing items against a strong opponent are then four different odds at every pool, bounded by the
soft cap (F-SC-16; Jordan, A-25: what a party brings raises the party).

### How an NPC builds a case and is answered by another

No branch for a player. The one chooser forms `speak` variants with `cites` (edit 6): none, all held
admitted items about the subject, and each held item that contradicts an item already filed against
his side (an answer). It scores them with its existing terms; what a variant costs is what E-7 says
(disclosure: the room learns the item and its chain). A second NPC who holds the contradicting cell
files it the same way. In a sitting the NPC decider (`05_SC_playable_hearing_B.md`) chooses order and
what to withhold; out of a sitting, everything filed is presented at close.

### Falsehood, forgery, concealment, and later trust

- A false claim filed in good faith stands until an answering act is drawn against it, and then stands
  or falls by that draw's band (rule 2), whatever the weights; the weights move the odds. A false item
  can strike a true one (no verifier, 2026-08-18 Q5, kept).
- A forged Record counts as any Record until someone who holds the forged claim answers it with that
  claim. The answer is drawn (rule 2): at `Success` the Record's item is struck, at `Overwhelming` every
  item of its origin is struck too, at `Partial` it is halved, at `Failure` it stands. The finding's told
  deposit (E-3) lowers the citer's `reception` and `teller_weight` in every hearer by the existing paths.
  Nothing new is written for trust.
- A concealed item is unheld and cannot be cited; no rule.

## Exact edits, by owner

1. `engine/season/rosters.yaml: proofs` — a `bears_on` column (`fact` for all four members); a
   fixture `evidence_cap` (proposed 2.0, NUMBER row, three-point sweep).
2. `engine/season/decision/options.py` — `contradicts(a, b)`, the predicate `_pair` already applies,
   exposed once; `_pair` calls it.
3. `modules/social_contest/evidence.py` (new) — `standing(presented, findings) -> (standing, struck,
   faults)`, over the `Exhibit` record of `05_SC_playable_hearing_B.md` (C3-C1: defined there, in
   `queries/inputs.py`; not re-described here). Called by `roll.py` and `hearing.py` only. The module names
   no `engine/season` module and restates no pairing rule: the host builder computes the relation with
   `contradicts` and hands it over as data, each `Exhibit` carrying `pairs: ((exhibit id, "contradicts"
   | "agrees"), …)` over the other filed exhibits. `standing` reads only that field, so the rule lives
   once, in `decision/options.py`.
4. `engine/season/loop/effects_information.py` — the `speak` effect writes `filed` stages for its
   admitted cites (CR-61's case-file Record; FI E-2's `Said`).
5. `engine/season/seam/wrappers/sigma.py::contest_input` — for a docketed matter, `exhibits` from the
   case file's filed stages (every filed item presented), with `pairs`, and `proof_level` carried raw; the
   host does not call `standing` and imports nothing from `modules/`. The control arm (`evidence_from:
   ledger`, a fixture) keeps `world_q.proofs` through the host's `proofs` source.
5a. `modules/social_contest/roll.py` and `hearing.py` — call `evidence.standing` on the input's exhibits and
   add the `proofs` levels (above) to the leverage they apply; report them in `levels`.
6. `engine/season/decision/options.py` — the `speak` variants above (FI `08_FI_05` edit 3's
   Candidate variants; SC-P3 edit 2's place).
7. `references/module_contracts.yaml` — `social_contest.evidence` is not a composition role: it is
   called by `roll` and `hear` inside the module, never by the host or the loop.

## Gate (execution artifacts)

On `build_hearing(seed)` (`05_SC_playable_hearing_B.md` edit 9), `PYTHONHASHSEED=0`:

1. The accuser files two firsthand deed claims and a Record: three `filed` stages; each judge holds
   the told copies with the accuser on the chain; at close, `proofs` = 3.0, the determiner's `levels` show
   `proofs` +3 (one `proof_level` per unit) and his obstacle equals the obstacle with nothing filed (read
   off SC-P1's record: `terms` and `levels`).
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

**Named tests** (new, `engine/season/tests/test_sc_hearing_evidence.py`, inside the kernel file's
`test_sc_hearing_*.py` glob): `test_three_filed_items_give_three_proof_levels_and_no_obstacle_change` (1);
`test_an_answer_strikes_by_its_band_in_a_share_strictly_between_0_and_1` (2);
`test_an_impeachment_strikes_origin_wide_only_at_overwhelming` (3); `test_corroboration_is_noisy_or_by_origin` (4);
`test_no_cites_is_hash_equal` (5); `test_a_same_side_contradicting_cite_is_refused_at_filing`;
`test_the_host_imports_nothing_from_modules_social_contest_evidence` (a source scan of `seam/wrappers/sigma.py`).

## Falsifier

An answer of the same value strikes nothing (it is agreement, rule 3). A cited id the citer does not
hold is refused before the draw. If an item of a kind the row does not admit changes `proofs`, the
admission read is wrong. If any step reads a ledger other than the actor's own or a judge's own, the
stage is not carrying the `Said`. If pool 2 against a score of 8 gives the same odds with 0 and 4
standing items, the levels are not applied; if the obstacle changes with them, a favourable term was
subtracted (A-25).

## Conflicts with ruled items — named, not resolved

- `ED-SC-0034` (3) "pool only": the items reach the roll as named levels on the leverage channel (A-25;
  OBS §3), neither the pool nor the obstacle; the archived *"+1D per Finding cited"* is not restored.
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
- **S**: one standing rule in the room and out of it; one corroboration rule (FI's); the weight in the
  leverage channel's units; one ladder for the answer's band; no second trust arithmetic.
- **E**, last: one operand, one stage kind, one pure function, one column, against a trial a player can
  read item by item.

## Cost class

Small build, after CR-61 (the case file), SC-02 (the re-source) and FI's edits 1 and 2.

**Lands it and tier.** The B24 batch (`methodology-execute`; one commit per edit in the order 1, 2, 3, 5a, 5,
4, 6, 7), `valoria-author` on `sonnet` (`high`), one `methodology-close` with its terminal `opus` critique.
**Hash movers.** None until `cites` is on (control: `cites` empty); then every world in which a cited
`speak` folds (declared).
