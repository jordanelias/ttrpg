# 08 · FI · 04 — Small edits: names, wiring, stale rows, pointers, and one Layer-1 hunk

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-15, C-16) — §1's `argument.held` row and §3's second bullet are withdrawn as duplicates (carried once by `16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1 and `16_PESSIMIST_SC_C_a_verdict_names_its_party.md` edit 1). §6 is read as the decision register's D-74, taken B: fix the witness code, not Layer 1. No lane applies a Layer 1 hunk; a read no refactor removes is listed for an amendment text. §4's budget row lands last, with `test_n3` read before and after.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.5 row FI-04 (CONFORMS; §4 budget row same defect as CHAR B1), §7 (INCOMPLETE: §6 names no symbols), §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-L8; `unified/U3_DEPENDENCY_ORDER.md` node B11, §4.1 row 11; `DECISIONS_ANSWERED.md` D-74). The body follows its head and the decisions: §1's `argument.held` row and §3's second bullet are removed (withdrawn as duplicates, carried once by `16_PESSIMIST_SC_D` edit 1 and `16_PESSIMIST_SC_C` edit 1); **§4's budget row is deleted** (C3-L8: `budget_office_bonus` is removed, carried by `U5a_CORE_owed_edits.md` §H; the head's "lands last" is overtaken); §6 is D-74 (fix the witness code, not Layer 1) with its symbols named; §5's `[UNVERIFIED]` on ED-FI-0002 is settled (it lives in `registers/editorial_ledger_fi_archive.jsonl`); named tests; lands-it and tier. The three reads no refactor removes are listed for an amendment text (receipt), not applied.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_4a_DONE.md` "For another lane", second item; A-81, C3-C11): §1 gains the paragraph narrowing `undeposited_kinds` so a failed inquiry leaves the actor's own claim.

**Lands in batch:** B11 (each row independent; one commit each); the `17_CENSUS_REST_1_deletions` row that needs this file lands with it (U3 §4.1 row 11).

## Status: PROPOSED

Carries audit `audits/08_FI_audit.md` resolutions R-10 to R-17, R-22 to R-24, R-26. Each row is
independent. §1–§4 move behaviour (declared hash movers where noted); §5 moves none; §6 touches ratified
Layer 1 and is also listed in the audit's §11.

## What this changes in `engine/season/` at runtime

§1: two Event kinds renamed. §2: `research` needs presence; a repeated ungraded finding deposits nothing; a
forgotten trail claim stops closing its trail. §3: a razing is witnessed where it happened; custody
receipts name the prisoner and the seat. §4: a writ lapses. §5–§6: nothing.

## 1. Names (R-10, R-11)

| owner | old | new | precedent |
|---|---|---|---|
| `verb_table.yaml`, the six inquiry rows' `emits_on_refusal` | `finding.none` | `inquiry.refused` | CP-T05-03 split `tell.refused` from `news.untold` |
| same rows, `Failure` band | `finding.none` | unchanged | — |
| `rosters.yaml: undeposited_kinds` | `[finding.none]` | `[finding.none, inquiry.refused]` until CP-T06-04 lands, then per that card | — |

**A-81 on the same roster (wave-3 mop-up; `unified/work/W3_4a_DONE.md` "For another lane", second item).** At the
tree the roster's reason is that "a refused inquiry deposits nothing, and no `finding.none` is deposited" (`rosters.yaml:
undeposited_kinds` source; `loop/witness.py:381-386` drops the kind before any deposit). A-81 (every scene writes a
durable change, a failure included) cannot hold for an inquiry whose `Failure` is `finding.none` and is dropped. The
verb files that rely on it (`14_VERBS_MATERIAL_E`, `14_VERBS_PHYSICAL_C`, `14_VERBS_PHYSICAL_D`) plant the actor's own
`(subject, <verb>.failed, True)` claim at a `Failure`. So the roster's rule is narrowed here: `finding.none` no longer
fans to nobody; it leaves the actor's own claim and nothing to the other present persons (the skip arm's other purpose,
no deposit of "he found nothing" to bystanders, is kept). The mechanism in `witness.py` (a second roster, or a per-kind
audience on this one) is chosen when `witness.py:381` is edited. `[ASSUMPTION: the actor-only audience is the narrowest
reading that meets A-81 and keeps H-111's no-bystander intent — basis: H-111's text in `rosters.yaml`; reversible by
returning the kind to the skip list and giving the claim to the verb files' own Failure cell.]` Named test:
`engine/season/tests/test_fi_small_edits.py::test_failed_inquiry_leaves_the_actors_own_claim` (the count of failed
inquiries with zero durable writes is 0; control: the roster as shipped, count > 0).

(`argue`'s `Partial` rename to `argument.held` is withdrawn here: carried once by
`16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1, C-15.)

Gate: `corpus_run`'s per-kind census shows `inquiry.refused` > 0 and `finding.none` only with a degree.
Named test (new): `engine/season/tests/test_fi_small_edits.py::test_inquiry_refused_is_split_from_finding_none`.
Movers (kinds are in the log).

## 2. Wiring (R-12, R-13, R-15)

- **`verb_table.yaml`, `research`.** `requires_typed` gains `{form: relation, of: subject, relation:
  present_at}` beside its `existence` conjunct (`examine`'s and `surveil`'s cell). A Record is where its
  holder is (`world_q.place_of`). Gate: H-319's reading re-run: a `research` by someone elsewhere is refused
  40 of 40.
- **`loop/witness.py`, the first deposit.** Before depositing an event-kind claim from an Event whose verb
  row declares no `writes:` at any band and no bands (the ungraded inquiries), skip it when the holder
  already holds the exact `(subject, predicate, True)` firsthand: the told channel's exact-triple guard,
  one deposit over. Keyed on the row's shape, never on a verb name. Gate: ten repeated `interview` acts
  leave one claim, not 30 (H-320). Becomes moot for a row once `08_FI_03` gives it a product.
- **`epistemic.py::holds_trail`.** Add `and c.confidence > 0` to the held-claim test. `deeds_judged` is
  **not** changed: ED-IN-0320 rules that a stale claim leaves the opinion. Gate: H-341's trail arm: a claim
  decayed to 0 no longer closes the trail; control: at confidence 5 it still does.

## 3. Witnessing (R-23; H-231 (1) and (3))

- **`queries/world_q.py::event_place`.** For an act-caused Event whose actor has no place after the write,
  fall back to the place he departed in that write (`World.departed_from`, the limb H-206 added for a
  death). Gate: `test_in12_raze.py`'s razing is held by those who stood in the town, not by "somebody".
(The second bullet, `_hold_tenure_ends` expanding a `detain`/`ban` edge, is withdrawn: carried once, wider,
by `16_PESSIMIST_SC_C_a_verdict_names_its_party.md` edit 1, C-15.)

## 4. Dead carrier and a mis-read edge (R-24, R-22)

- **`Record.ttl`** has no reader. Delete the field and its `write_matrix.yaml` row (ID-13). A writ's end is
  its last declared stage maturing: `issue` already winds stages (`_declared_stages`) and MATTER matures
  them; `comply`'s cell gains "the writ's last stage has not matured". Gate: H-259's eight-season run: the
  writ stops admitting `comply` after its last stage. FA's lane to place.
- **`decision/budget.py::budget`**: **deleted** (C3-L8). `budget_office_bonus` is removed altogether
  (`04` §A.3 row 15 refuses an office bonus in `budget`), so a held Record, Proposition or rung no longer
  buys a scene (H-92) because no `hold` does; carried by `U5a_CORE_owed_edits.md` §H. The evidence stays:
  every document the information verbs mint is a `hold` (`create_record` 130 / 116 / 117 a season).

## 5. Text, rows and pointers (R-14, R-16, R-17; no behaviour)

- **`systems/fieldwork/sim/knots.py`.** `:4` *"Canon source: systems/fieldwork/reference/knots_v30.md"* →
  *"Intent (archived, not canon): knots_v30.md"*. `:218-221`: delete the `random.Random()` fallback and
  raise when no `rng` is supplied (an unseeded draw in an oracle). `form_knot`: return `None` when
  `actor_a == actor_b`. The module-level registry stays: it is an unplugged oracle, and the season's knot is
  a Tenure.
- **`engine/season/hole_register.yaml`, H-116.** Head rewritten: closed by W-A and W-B; clause 4 declined
  461 / 445 / 485 candidates in one realm season at seeds 0 / 1 / 2 (this audit, §12).
- **`references/module_contracts.yaml`, the `fieldwork` module row** (`:329-362`). Split what it describes:
  the registered entry `fieldwork.find` (typed in, typed out, no state) and, separately marked UNPLUGGED,
  the knots oracle's tracks and gates, so a reader of the contract is not told the module holds an
  Evidence Track.
- **`registers/editorial_ledger_fi.jsonl`.** Write the two rows `HANDOFF_FI.md` names as unwritten
  (ED-FI-0009's FI-01 build; ED-FI-0002's FI-02/FI-03 build) and correct the handoff's pointer: ED-FI-0002
  lives in `registers/editorial_ledger_fi_archive.jsonl` (verified by grep; settled).

## 6. Layer 1: `04_CODE_ARCHITECTURE.md` §A.2, the `loop/witness` row (R-26; also audit §11 item 2)

Ratified; not edited by this proposal. Decided (D-74, taken B: fix the witness code, not Layer 1): **the two
`decision/` imports are removed from the code**. `loop/witness.py:46` imports `ledger_weigh` and
`refracted_confidence` from `decision/options.py`; both functions move to `queries/person_q.py` (person-side,
World-free arithmetic over a holder's own ledger and interior), `decision/options.py` re-imports them from
there (`04` §C.3: `decision/` imports `person_q`), and `witness.py` imports them from `queries/person_q.py`,
so it imports nothing from `decision/` `[ASSUMPTION: the target module; basis: the "per-holder projection a
`queries/` function builds" this section first named, and `04` §C.3's import rule]`. The three reads no
refactor removes (the driver's `findings` store, older Events by id, the ledger id set) are listed for an
amendment text to `04` §A.2's `loop/witness` row, drafted by the unification stage and applied only by
Jordan; nothing in `04` is edited here. Gate for the refactor: the same content hash at seeds 0–2 before and
after; named test (new): `engine/season/tests/test_fi_small_edits.py::test_witness_imports_nothing_from_decision`
(a source scan of `loop/witness.py`).

## Falsifiers

Each gate above is its row's falsifier. For §5's knots edit: `engine/tests/test_knots_ed912.py` must still
pass with an explicit `rng` (if it relied on the fallback, the test was drawing unseeded).

## NERS reading

These are S and E repairs: one name per outcome, one presence rule across the three place-bound inquiries,
one "who holds" expansion for every person-on-seat edge, no field nothing reads. Nothing here adds a
mechanic.

## Cost class

Edit, throughout, except §6's refactor (small build).

**Lands it and tier.** The B11 batch, an FI `valoria-author` session on `sonnet` (`high`), one commit per row,
closed by B11's `methodology-close` once. **Hash movers.** §1–§3 (declared); §6's refactor none (gate).
