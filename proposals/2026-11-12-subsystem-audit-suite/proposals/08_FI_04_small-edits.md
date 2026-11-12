# 08 · FI · 04 — Small edits: names, wiring, stale rows, pointers, and one Layer-1 hunk

## Status: PROPOSED

Carries audit `audits/08_FI_audit.md` resolutions R-10 to R-17, R-22 to R-24, R-26. Each row is
independent. §1–§4 move behaviour (declared hash movers where noted); §5 moves none; §6 touches ratified
Layer 1 and is also listed in the audit's §11.

## What this changes in `engine/season/` at runtime

§1: two Event kinds renamed. §2: `research` needs presence; a repeated ungraded finding deposits nothing; a
forgotten trail claim stops closing its trail. §3: a razing is witnessed where it happened; custody
receipts name the prisoner and the seat. §4: a writ lapses; a held paper stops buying a scene. §5–§6:
nothing.

## 1. Names (R-10, R-11)

| owner | old | new | precedent |
|---|---|---|---|
| `verb_table.yaml`, the six inquiry rows' `emits_on_refusal` | `finding.none` | `inquiry.refused` | CP-T05-03 split `tell.refused` from `news.untold` |
| same rows, `Failure` band | `finding.none` | unchanged | — |
| `rosters.yaml: undeposited_kinds` | `[finding.none]` | `[finding.none, inquiry.refused]` until CP-T06-04 lands, then per that card | — |
| `verb_table.yaml`, `argue`, `Partial` | `argument.won` | `argument.held` | `speak`'s `matter.held` |

Gate: `corpus_run`'s per-kind census shows `inquiry.refused` > 0 and `finding.none` only with a degree;
`argument.won` never with an empty `changes[]`. Movers (kinds are in the log).

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
- **`epistemic.py::_hold_tenure_ends`.** Expand a `detain` or `ban` edge to `(prisoner, seat)` as it expands
  a `hold` to `(holder, held)`. The other kinds stay opaque, as its docstring argues. Gate: `arrest.made`
  deposits a claim about the prisoner.

## 4. Dead carrier and a mis-read edge (R-24, R-22)

- **`Record.ttl`** has no reader. Delete the field and its `write_matrix.yaml` row (ID-13). A writ's end is
  its last declared stage maturing: `issue` already winds stages (`_declared_stages`) and MATTER matures
  them; `comply`'s cell gains "the writ's last stage has not matured". Gate: H-259's eight-season run: the
  writ stops admitting `comply` after its last stage. FA's lane to place.
- **`decision/budget.py::budget`** counts live `hold`s whose object is an Office (S26.3: the budget varies
  *by office*), not every `hold`: a held Record, Proposition or rung stops paying `budget_office_bonus`
  (H-92). CHAR's owner; listed here because every document the information verbs mint is such a `hold`
  (`create_record` 130 / 116 / 117 a season). Gate: `p_carin`'s budget unchanged by her first record.

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
  (ED-FI-0009's FI-01 build; ED-FI-0002's FI-02/FI-03 build) and correct the handoff's pointer if
  ED-FI-0002 lives in the archive ledger [UNVERIFIED by the audit].

## 6. Layer 1: `04_CODE_ARCHITECTURE.md` §A.2, the `loop/witness` row (R-26; also audit §11 item 2)

Ratified; not edited by this proposal. Decided preference, for Jordan's merge: **restore the row for the
two `decision/` imports** (move `refracted_confidence` and `ledger_weigh`'s arithmetic behind a per-holder
projection a `queries/` function builds at the barrier; `witness.py` then imports no `decision/`), **and
amend the row** for the three reads no refactor removes: the driver's `findings` store, older Events by id,
and the ledger id set. The alternative is to amend the row for all five. Gate for the refactor: the same
content hash at seeds 0–2 before and after.

## Falsifiers

Each gate above is its row's falsifier. For §5's knots edit: `engine/tests/test_knots_ed912.py` must still
pass with an explicit `rng` (if it relied on the fallback, the test was drawing unseeded).

## NERS reading

These are S and E repairs: one name per outcome, one presence rule across the three place-bound inquiries,
one "who holds" expansion for every person-on-seat edge, no field nothing reads. Nothing here adds a
mechanic.

## Cost class

Edit, throughout, except §6's refactor (small build).
