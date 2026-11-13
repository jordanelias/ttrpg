# INST-VENICE-B — the debt: a bond the creditor holds for an undertaking the debtor owns

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-09) — `debt` stays a Record kind as written here and is also a row of `engine/season/instruments.yaml: forms` (`record_kind: debt`, `made_by: covenant`, `bearer: true`, one `due`), so the kit's one set of instrument readers serves it: `debts_owed` and `debts_held` (edit 3) are not added, their occasions are `world_q.dues` and `world_q.breaches`; `debt_state`'s arithmetic is `world_q.owed(w, record, clause)`, the one amount reader for every clause that names an amount. A company's share is this instrument (the colonial lane's "`tribute`-shaped" share is withdrawn). A suit's forum, and a `ban` for debt before a Church bench, are `15_INSTITUTIONS_SYNTHESIS_C_crossings.md` edit 3. The kind, the mint, the discharge, the reckoning, `debt.lapsed`, `debt_suit` and the distraint stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §17). No edit of this file's is changed. What changed: (1) the history this file rests on (audit §1.6, §1.11, §2.4) is still mostly memory-grade: the tree holds nothing on the *commenda*, the sea loan (cited here at "The resolution", defence (a)), the Monte or the bill of exchange; (2) the tree does hold the shapes this file builds: the loan to a prince and the lender's ruin on his default (`research/historical_concerns_action_catalogue_v1.md:148`), the loan secured on a named right (`:161`; `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:190`), and public default as a restructuring, not an end (`…comparative_governance_research_v1.md:130`), which is this file's Partial band (an extension); (3) **a precedent this file did not cite and differs from:** an earlier proposal re-expressed the research's Debt and Compact as "an `oblige` Tenure with a `T-n` declared term" (`proposals/2026-09-10-settlements-factions-populations/05_COLLISIONS_AND_RESIDUE.md:22`; PROPOSED, held back), where this file follows the later K-14 (a Record kind minted by `covenant`). K-14 is the later design and carries what the Tenure cannot (an amount, a kind, a place, a bearer), so this file stands; the difference is named so that nobody lands both; (4) two mechanisms are added on this file's instrument, with no change to it: the pledge and the merchants' own court (`15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` edit 6).

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (VEN_B: `debt.lapsed` at MATTER AMBIGUOUS, F-R4-02), §2 (A-39 row), §7 (INCOMPLETE: the emission; the removed readers), 7b.0, 7b.7 ("delete `debts_held`/`debts_owed`; `debt.lapsed` = `term.matured` of a `debt` Record with `debt_state != met`, read when read"); `U3_CONFLICT_LEDGER.md` C3-C7 (MATTER emits `term.matured` only), C3-C10 (favourable terms are leverage). Changed: the lapse is a reading, not an emitted kind, and edit 5 (`loop/matter.py`) is withdrawn with its `logged_kinds` join; edit 3's two readers, already withdrawn by this file's first `Reconciled:` line, are removed from the body (`world_q.owed`, `dues`, `breaches` serve); the reckoning's `obligation` and `evidence` are levels (`obligation`, `proofs` sources); the suit's appeal is admitted on new grounds only (A-39).

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B33**, after VENICE-A (`U3_DEPENDENCY_ORDER.md` §1 item 33). Depends on: `15_INSTITUTIONS_VENICE_A` (B33, the ask and the `obligation` source), `15_INSTITUTIONS_SYNTHESIS_A` (B32, the `debt` form row and `world_q.owed`), `05_SC_acquittal.md` and `05_SC_arrangement_rows_that_bind.md` (B27, the suit's bands and SC-P6), `07_SE_treasury_granary_B.md` (B12, stocked stores for the seeded reading). Lane tag: FA. Tier: `sonnet` producer, effort `high`; one `opus` read of the reckoning's band table. Named test: `engine/season/tests/test_inst_ven_b.py` (the hand-built chain is its first function). Standing sentences: *Pool* — the reckoning is `petition`'s roll on the one pool rule (A-6, A-7, A-8). *Failure writes* — a refused reckoning is witnessed by those present and deposits their claim of the refusal (a deed against the debtor, which a lender later weighs); a lapsed bond's last `term.matured` is witnessed by the holder and the committed debtors (A-81). *Draw keys* — no draw is added; the reckoning, the suit and the distraint are `petition`'s, `determine`'s and `requisition`'s, keyed per A-30 by their rows.

Source: `audits/15_INSTITUTIONS_VENICE.md` §0 (the largest obstacle), §1.6, §1.11, §2.4, §6.1 part 4,
§6.2, §14.1 rows 1–3 and 10. Batch B. Un-defers #453 K-14
(`proposals/2026-10-03-verb-coverage-and-gap-fill.md:1478`, `:2685-2693`, `:4495`) in the shape that
document gave it. Not ratified by being written.

## What it changes in `engine/season/` at runtime

1. `covenant` mints a Record of kind `debt` when the act names a `kind` and an `amount`; otherwise it
   mints a `dispensation` exactly as today.
2. A `transfer` of that kind to the bond's place, by a person committed to its terms, counts toward it.
3. When the bond's last stage matures at MATTER, MATTER emits its `term.matured` as for any Record
   (C3-C7); a bond whose last stage has matured with less than `amount` counted **reads** as lapsed
   (`world_q.owed(w, rec, clause) > 0`, computed when read). No store, stance or tenure moves at that
   barrier, and no new kind is emitted.
4. A lapsed bond held by a seat-holder answers `requisition`'s operands against the debtor's rung, as a
   warrant; a bench hears a suit on it under a new arrangement row, `debt_suit`.

With no act naming `kind` and `amount` (every computed `covenant` today) nothing moves: hash EQUAL.

## The problem (evidence)

- No stored debt exists. `record_kinds` has no such kind; `rosters.yaml:2427` reserves the `kind` and
  `amount` operands for "the deferred `debt`"; #453 defers it "with its `seize` reader" (K-14).
- `covenant`'s instrument is "in force when both holders are committed — a reading nothing performs yet"
  (`loop/effects_information.py::_eff_covenant`). 0 of 41 formed covenants executed in the plan's reading
  (`workplans/valoria_master_workplan_v11_part2.md:23`; read at the line, not re-run).
- The corpus needs it: ARC-15 N1 (fund two hostile sides for profit), NPC-037 N2 (the treasury post),
  SCN-12 N2 (`audits/12_ARCS_adjudication.md` §3, M-STORES and M-REC).
- At `build_realm(0)` every rung's stores are empty and `coin` is "produced by no site and held by"
  nobody (audit E-1; `data/fixtures.py:613-632`). So an instrument tied to coin would be dead on arrival.
- D-5 (Jordan): *"no creditor verb, no `call_in`, no obligee-side closer on an obligation exists or will"*
  (`state/gate.py:1415-1417`).
- The standing rule (Jordan, 2026-11-12): whether a loan is repaid is a draw.

## The resolution, decided

**The debtor's obligation is his own `commit`; the creditor's asset is a document.** Ladder: step 3 for
the shape (K-14: "a Record kind with an `amount` key, minted by `covenant`"), step 1 for the limit (D-5),
step 5 for the readers.

- **Kind.** `debt: [terms, to, kind, amount, at]`. `terms`: the uttered Proposition undertaken (the
  mint's `read_from`: the act's `subject`). `to`: the counterparty the instrument addresses. `kind`: a
  `matter_kinds` member. `amount`: a whole positive number, **all that is owed**: there is no rate; the
  lender's gain is the difference between what he advanced and `amount`, and may be hidden further in a
  different `kind` or a different `at` (the bill of exchange, audit §2.4). `at`: the rung where it is
  discharged. `Record.stages` are the due dates; the last is the maturity.
- **Parties, derived, stored nowhere.** *Debtor*: every person with a live `commit` to `terms`.
  *Creditor*: whoever holds the Record (`hold_force`). Either party may draw the instrument through a
  seat granting `issue`: a house head lends on his own paper; a treasurer taking a forced loan issues the
  realm's paper to the lender. A successor is not bound until he commits. Handing the bond on by `give`
  assigns the debt; handing it to a debtor extinguishes it (nobody else can present it).
- **Discharge.** The debtor's own `transfer` (or anyone's: a patron may pay a client's debt, and that is
  a favour) of `kind` to `at`, formed on a question about the bond. `world_q.owed(w, rec, clause)` (the
  kit's one amount reader, SYN-A §4) returns the amount less what is counted, computed from the log's
  `transfer.made` Events whose causing act's question referent is the Record (resolver-side, `04` §B.9);
  stored nowhere. The state the original text called `debt_state` (`running`, `met`, `lapsed`) is read
  from it and the Record's stages.
- **The reckoning (the draw).** At a stage's maturity the creditor, or a factor sworn to his seat, may
  present the bond: a `petition` to the debtor with the Record cited. It is the ask of proposal A, with
  the debtor's live `commit` as `obligation` levels for the creditor and the bond as `proofs` levels
  (leverage, C3-C10; a forged bond's quality is the `subject` term against it), `regard`, and `stakes`
  by `amount` against the stores of the debtor's rung. Bands: Overwhelming, paid in full and his standing is unhurt; Success, paid in full; Partial,
  part paid and **one further stage wound on the bond** (an extension, citing this act); Failure,
  refused. What is paid is capped by what the debtor's rung holds (conservation). A debtor may also pay
  unasked; that is his choice and needs no roll.
- **Lapse.** A reading, not a judgment and not a write: after the last stage's `term.matured`, a bond with
  `owed > 0` is lapsed when read (D-48's precedent; C3-C7). WITNESS deposits the `term.matured` to the
  holder and the committed debtors, so each holds the fact from which the lapse is read.
- **Recourse, all ordinary verbs.** (a) *Suit*: `petition` / `open_case` before a bench whose purview
  reaches the debtor, under `debt_suit`; the bench's `determine` is SC's roll; SC-P4's band-keyed
  disposal: Overwhelming `ban` (the debt-bar: no seat under that bench's purview, FA-P3's scope) or
  `detain`; Success an `oblige` to the creditor's seat (service); Partial a new stage on the bond;
  Failure an acquittal (SC-P6), after which the bond can no longer be cited before that bench. An appeal
  (`appeal_basis: determine`) is admitted only on new grounds: excluded evidence, a voided stage, or a new
  item from a distinct source (A-39). The
  defence of loss by force is the debtor's cited claim of a `rung.seized`, `requisition.taken` or
  `field.lost` on the route (the sea loan's rule, as evidence rather than as a clause). (b) *Distraint*:
  a seat-holder who holds a lapsed bond and whose seat's purview reaches the debtor's rung may
  `requisition` up to the uncounted amount of `kind` from it to `at`; a private creditor must first get
  the bond into such an officer's hands (`give`), which is the politics of collection. The requisition
  is rolled as the SE lane's levy is (`06_FA_levy_through_the_seat_B.md`). (c) *Telling*: the lapse is a
  claim; a lender who holds it weighs it as `evidence` against the next loan. (d) *Assignment*.
- **Usury is derived.** A bond whose `amount` exceeds what the creditor's side transferred to the
  debtor's side between the commit and the mint, **in the same `kind`, at the same `at`**, shows gain on
  its face. An inquiry can find it (`reconstruct` over the bond and the transfer); a Church bench can try
  it. Nothing in this lane punishes it.

## Exact edits, by owner

1. **`engine/season/rosters.yaml: record_kinds.values`**: add `debt: [terms, to, kind, amount, at]`, with
   a note stating the derived parties and that it is K-14 un-deferred.
   **`record_sourced_operands.values`**: add `debt: {subject: terms, kind: kind, amount: amount}` (the
   reservation at `:2427`). `to` is **not** mapped: a `transfer`'s `to` is a rung and the bond's `to` is a
   person; the place is read from `at` by the effect (r2's ruling that `at` is no operand stands).
   **`warrant_sourced` is NOT edited.** Its shape is `verb: record kind` and a verb named there is formed
   *only* on a warranted subject (`rosters.yaml: warrant_sourced` note, opened), so a line
   `requisition: debt` would end every unwarranted levy. The distraint instead forms through
   `record_sourced_operands`' second reader (a held Record answers the operands it maps): the officer who
   holds the lapsed bond forms `requisition` with `kind` and `amount` from it, and the effect reads the
   debtor's `reside` rung as the place. The one new check is in `_eff_requisition`
   (`loop/effects_governance.py:511`): an act formed on a `debt` declines unless the bond reads lapsed
   (last stage matured, `world_q.owed > 0`) and takes no more than the uncounted amount.
2. **`engine/season/loop/effects_information.py::_eff_covenant`**: if the act's payload names `kind` and
   `amount`, mint through `_mint_document(w, a, "debt", …)`; refuse (`covenant.refused`) a `kind` off
   `matter_kinds` or an `amount` that is not a positive whole number; else today's body. One mint.
3. **`engine/season/queries/world_q.py`**: no reader of this file's own. The amount is `world_q.owed`
   (SYN-A §4); the creditor's and the debtor's occasions are `world_q.dues` and `world_q.breaches`, which
   stamp a `bearer` form's parties (X-09). `debt_state`, `debts_held` and `debts_owed` are not added.
4. **`engine/season/loop/effects_economy.py::_eff_transfer`**: no new write. When the act's question is
   about a `debt` Record and its `to` is that bond's `at`, the Event carries the Record among its
   subjects so `world_q.owed` can count it. A `transfer` to another rung counts nothing.
5. (Withdrawn, C3-C7: `loop/matter.py` is not edited and `debt.lapsed` is not a kind. MATTER emits the
   last stage's `term.matured`; the lapse is read when read. The `logged_kinds` / `strife_kinds` join goes
   with it: a strand that a lapse should open reads the matured term of a `debt` Record through its own
   reader when the WR lane asks for one.)
6. **`engine/season/arrangements.yaml`**: one row.

   ```yaml
   - id:               debt_suit
     disposal:          bench
     bench_basis:        determine
     floor:              open
     records_dissent:    true
     venue_min_rank:     settlement
     term_required:      true
     appeal_basis:       determine
     interposed:         [person, document]
     order:              alternating
     proofs:             [record, testimony, oath]
     disposes:           ban
     disposal_reach:      settlement
   ```
   `disposes: ban` is the Success-or-better kind until SC-P4's band-keyed form lands, after which the row
   reads as stated above. `[ASSUMPTION; medium; SC's to correct]`.
7. **`engine/season/data/fixtures.py`**: `credit_terms` (owed ÷ advanced by the loan ask's band, used
   only where a computed act names no amount): proposed `{Overwhelming: 1.1, Success: 1.25, Partial:
   1.5}`, shipped flat 1.0, swept. `stakes_ob` (SC's table) gains the `debt` reading in the audit's §8.
8. **`engine/season/write_matrix.yaml`**: no new row: `(Record, exists)`, `(Record, stages)`,
   `(Rung, stores)`, `(Tenure, since)` exist.

## Gate (execution artifact)

- Hand-built, real fold, one test file: utter → commit → covenant (a `debt` exists, held by the lender)
  → advance (`transfer`) → part payment (state `running`, counted) → reckoning rolled at each band by
  seed selection (Partial winds a stage) → last stage matures (`term.matured`; `world_q.owed > 0`; the
  holder holds the WITNESS claim of the maturity) → suit under `debt_suit` → a `ban` that refuses a
  `confer` inside the bench's purview and admits one outside. Asserted: no Event of kind `debt.lapsed`
  exists and `loop/matter.py` wrote no `Record.stages` cell.
- Seeded: a spine fixture with one stocked hearth and its head seat (proposal D's fixture, or a
  hand-stocked `Rung.stores`), seeds 0–2, six seasons: bonds minted, reckoning bands, lapses and suits are
  **read and reported**. If no bond is minted the reading says so: the chooser does not lend, which is
  M-AIM's and not this proposal's claim.
- Conservation: the sum of stores by kind over all rungs is unchanged by every act of the chain.

## Falsifier

- Control: with the `debt` row absent from `record_kinds`, the pre-item hash at build and at three seasons.
- Mutation: count a `transfer` to a rung other than `at`; the "pay the wrong place" arm must then lapse
  and does not.
- D-5: a hand-built act by the creditor that closes the debtor's `commit` is `NotYours` at the gate.
- The draw: over the reckoning's seeds at a fixed position, more than one band occurs (an assertion that
  asserts it observed at least two).

## What it does not do

No interest that accrues, no automatic collection, no coin, no profit-sharing venture, no treaty
readers. It makes nobody lend.

## NERS reading

- **N.** Remove it and there is no credit at any scale: a hearth cannot borrow seed, a duke cannot
  borrow for a campaign, a house cannot rule by what it is owed. Vertical: the same bond from hearth to
  realm. Lateral: the fine, the tax arrear, the condotta's pay and the company's share are this
  instrument (audit §12).
- **R.** A player chooses whom to trust, in what kind, payable where; extends or sues; sells the bond on.
  With no player, lapses chain. Complete at the extremes: a debtor with nothing pays nothing and the
  roll cannot make him; a dead debtor's bond is paper until an heir commits.
- **S.** One clock (`Record.stages`), one mint, one roll form (proposal A), one sanction carrier (`ban`).
  The suit is a sitting like any other. A lapsed bond nobody sues is still a referent its holder and
  every lender who learns of it read (A-80).
- **E, last.** One record kind, one arrangement row, one branch in an effect and one in a check, against
  the largest single gap this family has.

## Cost class

Small build. Depends on proposal A, SC-P4 and SC-P6 (the suit's bands), and the SE lane's stocked
treasuries for the seeded reading.
