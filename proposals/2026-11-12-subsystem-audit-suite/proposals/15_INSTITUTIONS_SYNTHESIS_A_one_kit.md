# INST-SYN-A — one institutional kit: one registry, one record-kind scheme, one seat row, one obstacle-term list, one fixture style, one arrangement vocabulary

Reconciled: 2026-11-12, U5d closure — folded Jordan's answers (`unified/DECISIONS_ANSWERED.md`) into the kit's five meetings with Layer 1 (audit §8.2). **L-1 / A-12**: a seat may carry a modifier, so "no seat-row key of the kit is read by any roll" is no longer a constraint; the kit may add an office modifier, entered as a named term through the one obstacle composer (`U5c_SC_one_obstacle_form.md`) so that office and regard are not counted twice, and the dignity "precedence" step withdrawn by X-19 may be re-entered in that form by a later content edit (none is added here). **L-2 / A-13**: the three optional seat facts (the clerks an order passes, paper-hands, the exit audit) are ruled; a seat declaring none behaves as today; the Layer 1 seat-list text is APPLIED (2026-11-12, A-97, node `L1-A13`; `04:331`). **L-3 / A-14**: a vote is a draw on the voter inside the presiding person's act; the ballot stays SC's (X-15). **L-5 / A-10**: institutions are the loop's own verbs and data; no module. **A-21 / A-22**: X-33's per-form `basis` stands with its two values ruled: a publication (`purview`) reaches everyone on the ground with the news of its issue; an order (`command`) binds the issuing seat's sworn men, the holders of seats it may revoke and the unseated in its land, and a writ to a superior is a petition. **A-41**: no `corvee` form is authored; caste is carried by regard, by the vote weight of `U5d_FA_owed_edits.md` §4 and by the practice table of `U5d_SE_cohort_heavy_moves_and_caste.md`.

Reconciled: 2026-11-12, wave 3 lane W3-4b — rewritten against A-12, A-13, A-14, A-35, A-36, A-41, A-42, A-56 and the re-grounding plans (`OWED_TO_UNIFICATION.md` §B); applied `R4_READ.md` §1.7 (SYN_A rows), §2 (A-12, A-13 rows), 7b.0, 7b.7; `U1_OWNERS_AND_VOCABULARY.md` D-U1-01/01a (a seat's help is its row's `modifier:` read by the `office` leverage source; a seat above stands against as `rank_gap`), D-U1-11k (`remove` → `distance`), D-U1-11r and S-24 (one seat schema), F-36, F-39; `U3_CONFLICT_LEDGER.md` C3-L9 (no Seat field for unruled keys), C3-C10 (favourable terms are leverage), C3-N31 (form count read by command). Changed: §2, §3, §4 and §6 tables; the "What it changes" list; gates 2 to 4; "What it does not do"; NERS R and E. **Correction of C3-L9 at the tree:** `lot` cannot be a `conferral_bases` value, which is Jordan's closed roster (`rosters.yaml:3042-3056`, `open: false`); it is `tables.selection` under `elected` (VENICE-C) and the fifth value is listed for Jordan. The first `Reconciled:` line's "named term through the one obstacle composer" for an office modifier is superseded by D-U1-01.

Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A12`, §`L1-A13`, `unified/work/L1_PROPAGATION.md`): A-13's Layer 1 seat-list text and A-12's `modifier?` are APPLIED (`04:331`); the "owed, not applied" clauses of the head and of §3 are rewritten, and `dignity` is recorded as not among the applied keys, its clause kept and re-pointed. The J-R4-1 sentence about "the owed A-13 amendment" now says option A needs a further amendment.

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B32** (institutions kit, FA), second, after `15_INSTITUTIONS_COLONIAL_A` and before `_SYNTHESIS_B` (`U3_DEPENDENCY_ORDER.md` §1 item 32). Depends on: `U5c_SC_one_obstacle_form.md` and `05_SC_obstacle_difficulty_and_modifiers_B.md` (B05, the one roster and composer), `14_VERBS_BINDING_D_orders.md` (B21, the `authority` conjunct's `basis`), `15_INSTITUTIONS_COLONIAL_A_instruments.md` (B32), `U1_OWNERS_AND_VOCABULARY.md` D-U1-01a (the `modifier:` column, landed by whichever batch first authors a seat modifier). Lane tag: FA. Tier: `sonnet` (loaders, rosters, readers), effort `high`; no `opus` node (the gates are equalities and refusals). Named test: `engine/season/tests/test_inst_syn_a_kit.py` (gates 1 to 4 as functions). Standing sentences: *Pool* — the kit adds no roll; every roll that reads its terms is a verb's, on the one pool rule (A-6, A-7, A-8). *Failure writes* — the kit adds no contested row (A-81 is the verb rows'). *Draw keys* — the kit adds no draw (A-30).

Source: `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (the collision ledger, X-01 to X-32) and §3; the
twenty-one family proposals `15_INSTITUTIONS_{BYZANTINE,PAPACY,VENICE,COLONIAL}_*`. This file states the
**reconciled set** and the edits that differ from what a family file wrote. Where a family file's edit
stands unchanged it is cited, not repeated. Each family file that lost a collision carries a
`Reconciled:` line naming this file. Ratifies nothing (CLAUDE.md §2).

## What it changes in `engine/season/` at runtime

Nothing until content uses it. With `instruments.yaml` empty, no seat row carrying a new key, no
arrangement row added and every size fixture at its control, `build_realm(0)` is hash EQUAL at build and
at one and two seasons. What it changes is **which file each institutional fact lives in**, so that the
four families' builds land on one set of owners:

1. One registry, `engine/season/instruments.yaml`, holds every form a document can take and every
   document a world begins with.
2. One new Record kind (`debt`) and three content keys (`form`, `amounts`, `recites`).
3. Seat-row keys only where a ruling licenses them (`upkeep`, existing; `dignity`; A-13's
   `passes_through`, `hand_term`, `audit_at_exit`; A-12's `modifier`), four tables keyed by seat id
   (`patronage`, `eligible_from`, `cooling_off`, `selection`), one roster member (`members_by_warrant`),
   one new roster (`patronage_bases`), one anchor form.
4. One leverage source added to SC's roster (`obligation`, the favourable half of what the counterparty
   owes). No obstacle member is added: `remove` is OBS member 20 `distance`; the hostile half of
   `obligation` widens OBS member 12 `commitment`; the BINDING lane's rank term is `rank_gap`.
5. The fixtures of audit §3.6 in one style, less `obligation_step` and `remove_step` (retired), plus
   `obligation_level` (control `None`).
6. One arrangement key (`quorum_share`, combinable with `quorum`), one band-map cell value (`release`,
   requested of SC), eight rows.

## The problem (evidence)

Read at `8948603`. The four family lanes each proposed a home for the same facts
(`audits/15_INSTITUTIONS_SYNTHESIS.md` §1, §2):

- world-gen documents: `offices.yaml: founding:` (`15_INSTITUTIONS_BYZANTINE_A` edit 1),
  `offices.yaml: instruments:` (`15_INSTITUTIONS_PAPACY_C` edit 1), `off_king.obligees` as mappings
  (`15_INSTITUTIONS_COLONIAL_D` edit 3); and `06_FA_office_capabilities.md` edit 5 already claims
  `offices.yaml: founding:` for another meaning;
- forms of a document: `engine/season/instruments.yaml` (`15_INSTITUTIONS_COLONIAL_A`),
  `rosters.yaml: writ_terms_forms` (`15_INSTITUTIONS_PAPACY_D` edit 5, `_E` edit 2), bare dispensations
  told apart by what `terms` names (`15_INSTITUTIONS_VENICE_C`, `_D`);
- a certified deed: record kind `roll` (BYZ-A edit 2), `resolution` with `attests: n` (PAP-C), form
  `recognition` (COL audit §5.3 c);
- the audit at exit: `audit_at_exit` plus row `exit_audit` (VEN-C, VEN-D), `audited` plus row `audit`
  (COL-C);
- obstacle composition: "favourable / hostile steps" (BYZ-A, -B, -C, -E), `oath_step` (COL-B),
  `obligation` (VEN-A), a `charter` term (VEN-D);
- controls: `procedure_draws` (BYZ), shipped-at-control size fixtures (VEN), declared movers with no
  equal arm (COL-B).

Landed as written, they would put one fact in two or three files (CLAUDE.md §0.05 clause 3; §8).

## The resolution, decided

The decisions are the ledger's; each has its ladder step there. In one line each: the Colonial registry is
the home (X-01, X-02); a certificate is a content key, not a kind (X-03); a roll is a membership, not a
Record (X-04); `debt` is a kind **and** a form so one set of readers serves it (X-09); `audit_at_exit`
names its room and `audit` is the room (X-12); every odds source is a member of the one roster (X-19,
X-20); a verb row has one owner and that owner is its verb lane (X-23 to X-29); every number follows five
rules (§3.6).

## Exact edits, by owner

### 1. `engine/season/instruments.yaml` (new) and `engine/season/data/instruments.py` (new)

`15_INSTITUTIONS_COLONIAL_A` edits 1 and 2 stand, with these changes.

**Top level.** Two keys, `forms:` and `seeded:` (COL-A's top-level `instruments:` becomes `forms:`).

**Form row.** COL-A's keys, plus:

```yaml
    record_kind: dispensation     # dispensation | debt          (default dispensation)
    bearer:      false            # true: entitled = the Record's holder; bound = a live commit to its terms
    recites:     false            # true: the Record may carry a `recites` list (a certificate of deeds)
    basis:       command          # command | purview: whom an `issue` of this form may address (the `authority`
                                  #   conjunct's basis value, `14_VERBS_BINDING_D` edits 3 to 5). `purview` for a
                                  #   PUBLICATION (a sanction told to everyone on the ground); `command` for an order
    # in `confers:` — one optional key more:
    #   audit_at_exit: <arrangements.yaml id>
    # in a clause — value sets widened:
    #   by:   grantor | grantee | addressee        (`addressee` only where made_by: issue)
    #   over: grant_ground | grantee | named       (`named`: the person or rung the content's `of:` names)
    #   to:   grantor_rung | grantee_rung | grant_ground | named_rung
```

**COL-A's ten rows, changed cells only:** `homage`, `land_grant`, `march`, `charter`: `recites: true`.
`charter`, `staple`, `immunity`: `hardens: true` (COL audit §6.2; COL-A left the cell per row). `farm`,
and every row whose `confers:` seats an officer over other people's ground (`march`, `land_grant`):
`confers.audit_at_exit: audit`. `homage`: no `term` (it runs for the two holders' lives; `renewal: both`).

**Six rows added** (each `grade: assumption`; posts are functional labels, names are Jordan's through
`references/names_index.yaml`):

```yaml
  - id: warrant                 # VEN-C: admission to a list kept by warrant
    made_by: issue
    grantor_act: issue
    term: null
    renewal: grantor
    due: []
    forbears: []
    lapse: reverts
    hardens: false
    source: "15_INSTITUTIONS_VENICE_C §1; D-5's expulsion rule (the seat withholding renewal)"

  - id: commission              # VEN-D §2; PAP-E §4: what a seat held at distance may and may not do
    made_by: issue
    grantor_act: confer
    term: null                  # the conferred hold's own term (FA-P3)
    renewal: grantor
    due:
      - {by: grantee, kind: record.given, every: 4, to: grantor_rung}     # his books sent up yearly
    forbears:
      - {by: grantee, kind: exchange.made, over: grant_ground}            # no trade on his own account
      - {by: grantee, kind: duty.taken,    over: grant_ground}            # no local oath
    lapse: reverts
    hardens: false
    source: "15_INSTITUTIONS_VENICE.md §1.7 (the rector's commission), §2.4 (the branch manager's contract)"

  - id: avoidance               # PAP-D §3: addressees forbear named dealings with a named person
    made_by: issue
    grantor_act: issue
    basis: purview              # a publication: it addresses everyone on the issuing seat's ground (SYN-C edit 7)
    term: null                  # while the ban it publishes lives
    renewal: none
    due: []
    forbears:
      - {by: addressee, kind: exchange.made,   over: named}
      - {by: addressee, kind: record.given,    over: named}
      - {by: addressee, kind: duty.taken,      over: named}
      - {by: addressee, kind: covenant.offered, over: named}
      - {by: addressee, kind: tenure.opened,    over: named}   # the secular arm: a complier does not seat him (SYN-C edit 2)
    lapse: reverts
    hardens: false
    source: "15_INSTITUTIONS_PAPACY_D §3 (the verbs list: exchange, give, oblige, tend, train, covenant); 15_INSTITUTIONS_SYNTHESIS_C edit 2"

  - id: interdict               # PAP-D §4: the issuer's own seat-holders in a place withhold services
    made_by: issue
    grantor_act: issue
    term: null
    renewal: none
    due: []
    forbears:
      - {by: addressee, kind: transfer.made,      over: named}   # alms
      - {by: addressee, kind: matter.determined,  over: named}   # judging
    lapse: reverts
    hardens: false
    source: "15_INSTITUTIONS_PAPACY_D §4 (withhold: tend, transfer, train, determine)"

  - id: tithe                   # PAP-E §2: addressees render a share each season to a named rung
    made_by: issue
    grantor_act: issue
    term: null
    renewal: none
    due:
      - {by: addressee, kind: transfer.made, every: 1, to: named_rung}
    forbears: []
    lapse: stands
    hardens: false
    source: "15_INSTITUTIONS_PAPACY_E §2 (render: kind, share, to)"

  - id: debt                    # VEN-B: K-14 un-deferred
    record_kind: debt
    made_by: covenant
    grantor_act: issue
    bearer: true
    term: null                  # the Record's own stages
    renewal: none
    due:
      - {by: grantee, kind: transfer.made, every: once, to: named_rung}   # `amount` of `kind` to `at`
    forbears: []
    lapse: stands               # an unpaid bond does not vanish; it reads lapsed when its last stage has
                                #   matured with `owed > 0` (no `debt.lapsed` kind; C3-C7)
    hardens: false
    source: "15_INSTITUTIONS_VENICE_B; #453 K-14"
```

`[UNVERIFIED]` for the three sanction rows: which emitted kind each forborne verb's success carries
(`tend` and `train` are the MATERIAL and MILITARY lanes' rows; the loader's `DEED_KINDS` check decides at
landing which kinds may be named; a verb with no success kind yet is left out of the row until its lane
lands one).

**Loader, beyond COL-A's refusals:** `basis` off `{command, purview}`, or present on a row whose `made_by`
is `covenant`; `record_kind` off `{dispensation, debt}`; `bearer: true` on a row
whose `made_by` is not `covenant`; `by: addressee` on a row whose `made_by` is not `issue`; `over: named`
or `to: named_rung` on a row with no clause able to name one; `confers.audit_at_exit` that is no
`arrangements.yaml` id; `recites: true` with `record_kind: debt`.

**`seeded:` row.** Keys: `id`, `kind` (a `record_kinds` member), `form` (a `forms:` id, or absent for a
`resolution`), `via` and `held_at` (seat row ids), `to` (case ids), `at` (an anchor), `terms`, `amounts`,
`recites` (`{for: <seat id | case id>, deeds: [<prehistory deed id>]}`), `source`. The loader refuses an
unknown key, a `form` whose `record_kind` is not the row's `kind`, a `recites` on a kind or form that does
not admit it, and a `via` or `held_at` that is no seat row. `harness/populated.py::build_realm` mints each
row once, through the existing mint, after seats are held, with the `hold` on the live holder of
`held_at`; a vacant `held_at` is skipped and reported (PAP-C edit 2, unchanged but for the file it
reads). A case file's `setup.instruments` (COL-E) is the same row.

### 2. `engine/season/rosters.yaml`

| roster | edit | from |
|---|---|---|
| `record_kinds.dispensation` | optional content keys `form`, `amounts`, `recites` | COL-A edit 3; X-03 |
| `record_kinds` | add `debt: [terms, to, kind, amount, at]` | VEN-B edit 1 |
| `record_kinds.resolution` (CR-36's row, when it lands) | optional content key `recites` | X-03 |
| `record_kinds` | **no** `roll` | X-04 |
| `record_sourced_operands` | add `debt: {subject: terms, kind: kind, amount: amount}` | VEN-B edit 1 |
| `choice_sourced` | `covenant: [form]`, `issue: [form]` | COL-A edit 4 |
| `writ_terms_forms` | **not created** | X-02 |
| `obstacle_terms` (OBS's roster) | **nothing added**: `remove` is member 20 `distance` (fixture `distance_step`; D-U1-11k); the hostile half of `obligation` (the counterparty's edges toward the other party of a heard matter) is counted by member 12 `commitment`, whose read the SC rewrite lane widens to the counterparty's `owed_to` toward that party (`commitment_ob`) | VEN-A edit 1 as reconciled; COL-B §1; C3-C10; F-39 |
| `advantage_sources` (OBS §3) | add `obligation` after `favour`: aggressor levels, one `obligation_level` per whole unit of the counterparty's `owed_to` toward the actor (a lapsing edge counts `obligation_arrears`), scaled by `sealed_obligation` under a sealed room; defender levels none | VEN-A edit 1 as reconciled; C3-C10 |
| `conferral_bases` | **not edited** (Jordan's closed roster, `open: false`, `rosters.yaml:3042-3056`) | VEN-C as reconciled |
| `tables.selection` (new) | seat id → `lot`, only on an `elected` seat | VEN-C edit 1 as reconciled |
| `tables.patronage`, `tables.eligible_from`, `tables.cooling_off` (new) | seat id → a list of `patronage_bases` members; → the seat whose list fills it; → seasons | PAP-B §1, VEN-C §2 and §4 as reconciled; C3-L9 |
| `binds_bases` | add `members_by_warrant` (the roster's note foresees a second value with its rule) | VEN-C edit 1 |
| `patronage_bases` (new) | `[purview, own_faction]` | PAP-B edit 1 |
| `revocation_bases` | add `head_of_faction` (A-35) | PAP-B item 4 |
| `office_bodies.<body>.term` | optional seasons | BYZ-C edit 3 |

### 3. `engine/season/offices.yaml`, `data/rosters.py::_load_offices`, `state/carriers.py::Office`

One seat schema (D-U1-11r; S-24), owned by the `offices.yaml` row and `Office`, one loader. A key lands
only where a ruling licenses a Seat field (`04` §B.7 is STRUCTURAL; C3-L9): `upkeep` is in the ratified
tuple; `passes_through`, `hand_term`, `audit_at_exit` are A-13's three facts; `modifier` is A-12's
(D-U1-01a); `dignity` is a seat-row grade that a ruling's amendment text must name. The amendments are
APPLIED (2026-11-12, A-97): `04:331` now carries `modifier?` (A-12, node `L1-A12`) and `passes_through?`,
`hand_term?`, `audit_at_exit?` (A-13, node `L1-A13`, "no fourth key"), and **`dignity` is not among them**: no
applied Layer 1 text names it, so its clause stands as written (it needs a ruling's amendment text before it
lands as a Seat field; `04` §B.7 is STRUCTURAL). Each is folded into
the hashed representation only when present (FA-P3's rule, so an unkeyed world's hash does not move).
`data/rosters.py::_load_offices` (`:152-180`) refuses no unknown row key today (it checks the top level
and repeated ids only; opened by W3-4b); this edit gives it **one closed key set** over a seat row, the
tree's keys (`id, post, rung, body, faction, remit_acts, scope_rung, binds, conferral, revocation,
upkeep, holder, obligees, source, note`, read from `offices.yaml` at landing, not from this list) plus
the keys below as each lands, and a refusal naming the row and the key. Refusals at load:

| key | refused when |
|---|---|
| `dignity` | not an int in `[1, dignity_grades]`; or the row's `remit_acts` is not `[]`; or `revocation` is not `null` |
| `upkeep` | not an int ≥ 0 |
| `passes_through` | a member that is neither an `office_bodies` name nor `{seat: <row id>}` |
| `hand_term` | not a positive int |
| `audit_at_exit` | not an `arrangements.yaml` id |
| `modifier` | not a member of `sigma_leverage.LEVEL_SIGMA` (D-U1-01a; read by the `office` leverage source off `Act.via`; a dignity's precedence, withdrawn by X-19, may return only as this key, never as a step) |

`patronage`, `eligible_from`, `cooling_off` and the lot are **not Seat fields**: they are the four tables
of §2, keyed by seat id (the F-12 precedent; PAPACY-B §1). Their loader (`data/rosters.py`) refuses a key
that is no `offices.yaml` row, a `patronage` member off `patronage_bases`, an `eligible_from` that is no
row id, a `cooling_off` that is not a positive int or names a seat whose row has no `term`, and a
`selection` value other than `lot` or on a seat whose `conferral` is not `elected`. **For Jordan
(J-R4-1, kept):** option A widens the A-13 amendment (applied at `04:331`, which names only `passes_through?`,
`hand_term?` and `audit_at_exit?`, so a further amendment) to name the three keys as Seat fields and adds
`lot` to `conferral_bases`; option B, taken, is the tables. A seat that stands above the actor's
exercised seat enters a roll only as `rank_gap` (OBS member 6), and `regard` reads stance rows only, so
a seat is never counted twice (D-U1-01).

`audited:` (COL-C edit 2) is not a key. `founding:` (BYZ-A edit 1) and `instruments:` (PAP-C edit 1) are
not sections of this file.

`harness/populated.py::resolve_anchor` gains the form `{venue: <building id>}` (VEN-D edit 1).

### 4. Readers (one each)

| reader | file | from |
|---|---|---|
| `instrument_of`, `clauses_binding`, `dues`, `breaches` | `queries/world_q.py` | COL-A edit 5. `dues` stamps a clause while `owed > 0`; a party to a `bearer` form is read as X-09 states |
| `in_force(w, record)` | `queries/world_q.py` | new here: `covenant_in_force(w, rid) > 0` (`14_VERBS_SOCIAL1_B` §3) for a covenant-made form; unmatured `Record.stages` for an issue-made one. `dues` and `breaches` ask it and nothing else |
| `owed(w, record, clause) -> int` | `queries/world_q.py` | VEN-B's `debt_state` arithmetic, for any clause whose instrument names an amount: the amount, less the `transfer.made` Events to the clause's place whose act cites the Record. `debt_state`, `debts_held`, `debts_owed` are not added |
| `kept(p, record)` | `queries/person_q.py` | COL-A edit 6 |
| `forborne(p)` | `queries/person_q.py` | PAP-D edit 7, restated: for each live `oblige` of `p`'s own carrying `OBEYED_WRIT` (`14_VERBS_SOCIAL1_B` §2), the `forbears` clauses of that writ's form whose `by:` is `addressee`, with their named object. `decision/options.py::opening_set` declines those candidates. Person-side, his own Tenures and his own content claim |
| `owed_to(p, holder_seats, held_terms)` | `queries/person_q.py` | VEN-A edit 3; an `oblige` counts only if `gate.py::sworn_to` counts it. Read by the `obligation` leverage source and by member 12's widened read |
| `distance(w, place_a, place_b)` | the reader of OBS member 20 (`U5c_SC_one_obstacle_form.md` §2; `14_VERBS_SOCIAL1_B` §2) | COL-B §1's `remove` is this reader, not a second one (D-U1-11k) |
| `upkeep_owed(w, seat, person)` | `queries/world_q.py` | BYZ-B edit 3 |
| `hands_open(w, p)` | `queries/world_q.py` | BYZ-C edit 7 |
| `audits_due(w, p)` | `queries/world_q.py` | X-12: for each closed `hold` on a row carrying `audit_at_exit` whose `tenure.closed` claim `p` holds and over whose seat `p` may open (VEN-C edit 4's set), the departed holder (`Party`) and the arrangement |
| `may_seat`, `selection_of`, `PATRONAGE_RULES`, `patronage_of` | `state/gate.py` | VEN-C edit 4; PAP-B edit 3 (as reconciled: the tables, no `FILLED_BY` change) |
| `legitimacy(…, seat, fx)` | `queries/person_q.py` | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` |

### 5. `engine/season/data/fixtures.py`

The table of audit §3.6, each row shipped at its control, each with a NUMBER row in `hole_register.yaml`.
Not added: `founding_confidence`, `procedure_draws`, `pledge_step`, `oath_step`, `levy_ob`,
`provisional_term` (the BINDING lane's one fixture, `14_VERBS_BINDING_C` value 2; F-R4-10),
`obligation_step` and `remove_step` (retired with the terms; `distance_step` is OBS's). Added beside the
table: `obligation_level` (control `None`). Every value is calibrated with the joint re-centring of A-5,
A-6, A-7, A-26 (OBS §4 step 5), so each ships at its control and keeps its `[ASSUMPTION]`.

### 6. `engine/season/arrangements.yaml`, `data/arrangements.py`

- `_ARRANGEMENT_KEYS` gains `quorum_share`, combinable with `quorum` (the floor of fors) on a declared row
  (PAPACY-GROUNDING item 1 withdraws PAP-B edit 6's "exclusive"; U1 F-36). `excommunication_deliberation`
  and `conclave` ship `quorum: 2` beside `quorum_share: [2, 3]`.
- The tally of a `declared` row (the ballot loop `13_SC_draw_for_unrolled_contests.md` edit 3 adds) is
  the one table of audit X-15, with the pass test `fors >= max(1, quorum)` and the share; a candidate
  casts no ballot on his own candidacy; `verb_table.yaml: determine` gains `matter.undetermined`. Each
  ballot is a draw on the voter inside the presiding person's act (A-14). A body whose vote is weighted
  by territory or caste reads the authored franchise (`rosters.yaml: tables.territory_weight`, U1 F-12;
  `U5d_FA_owed_edits.md` §4) as a term of each voter's draw, never as a count: the kit's councils are the
  first reader A-42 names.
- Rows: `acclamation` (BYZ-E edit 4), `conclave` (PAP-B §2), `consecration` (PAP-C §2), `debt_suit`
  (VEN-B edit 6), `security_bench`, `enrolment_ballot` (VEN-D §4), `audit`, `quo_warranto` (COL-C edit 1),
  each as its file wrote it as reconciled. `exit_audit` (VEN-D §4) is not added: every
  `audit_at_exit: exit_audit` in VEN-C and VEN-D reads `audit`. `general_council` is **not added**: A-36
  (nobody judges the Confessor) dropped the council.
- A-41 and A-56: no `corvee` form. Caste reaches the kit three ways only: regard, the franchise above,
  and the informal tiers of `U5d_SE_cohort_heavy_moves_and_caste.md`; a cohort person is a person, so
  `dues` stamps him and his answers are the commons' heavy moves (`petition`, `comply`, `evade / defy`,
  `riot`; A-56).

## Gate (execution artifacts)

1. **Neutral until used.** With the registry empty, no row keyed and all fixtures at control:
   `build_realm(0)` `content_hash` at build, one season and two seasons equals the pre-item hash
   (`PYTHONHASHSEED=0`).
2. **The loaders refuse.** One planted malformed row per refusal named in edits 1 and 3 raises, naming
   the row; every form in `instruments.yaml` loads (the count read by command at the run, not written
   here: 16 after B32, 17 after `condotta` lands in B40; C3-N31). A planted `patronage:` key on an
   `offices.yaml` row is refused as an unknown key.
3. **One of each, hand-built.** A two-seat world with a seat carrying every seat-row key of §3 and named
   in each table of §2, one `tribute`, one
   `debt` and one `avoidance`: `dues` stamps the tribute payer and the debtor and not a bystander; after a
   `transfer.made` to the clause's place the stamp is gone and returns next period for the tribute and not
   for the debt; an addressee whose `comply` drew Success has the named dealings declined and one whose
   `comply` drew Failure does not.
4. **One term, one name.** On a hand-built `issue` to a sworn addressee two territories away, the
   recorded roll (SC-P1's `terms` and `levels`) carries `distance` among its terms and `obligation` among
   the answering roller's levels, and no `oath_step`, `remove` or `obligation` term. Control: the same
   act to an unsworn addressee in the issuer's own territory records neither.

## Falsifier

A hash move at gate 1. A `debt` whose debtor `dues` does not stamp (the second occasion source came
back). A form row with `by: addressee` under `made_by: covenant` that loads. A seat row carrying
`audited:` that loads. A roll over 200 seeds of gate 3's `comply` in which every addressee declines (the
writ would be a switch). An `Office` carrying a `patronage`, `eligible_from` or `cooling_off` field, or a
`conferral_bases` carrying `lot` (an unruled Seat field or roster value landed).

## What it does not do

It builds no institution: every institution is the family proposals' content on these owners. It adds no
verb, no Tenure kind, no carrier, no stored quantity. It adds no name for the distance between two rungs:
U1 decided one member, `distance`, with one fixture `distance_step` (D-U1-11k); `carriage`
(`14_VERBS_MATERIAL_B`) and `remove` (COL-B) are retired names, the first by the verbs lane. It adds no
Seat field beyond the ruled ones and no value to a closed roster of Jordan's.

## NERS reading

- **N.** From above, a designer authors any grant, sanction or bond as one row of one file. From below,
  a person reads what he owes from one occasion. Laterally, a papal sentence, a ducal homage and a
  banker's bond are answered, kept and sued on by the same readers. Diagonally, a hearth's debt and a
  realm's tribute are one clause shape. Remove the reconciliation and the same sanction has two forms
  and the same deed three certificates.
- **R.** Customisation is the point: the forms of one registry, the ruled seat keys, four seat tables and
  the one roster of terms and leverage sources are the whole authoring surface of every institution.
  Complete at the extremes: an empty registry is today's world; a form with no clauses is a bare decree.
  An unpaid due, a breached forbearance and an audit nobody opens are each readable referents others act
  on, so an institution that holds still still moves the world (A-80).
- **S.** One registry, one set of readers, one roster of terms, one fixture style, one tally. The kit
  removes three S defects the lanes would have landed (two audits, three certificates, two distances).
- **E, last.** Against four families' worth of institutions: one file, one kind, three content keys,
  the ruled row keys, four tables, one leverage source. It is smaller than the sum of what the four lanes
  asked for, by one record kind, one registry, one Query, two obstacle members, two rows and five
  fixtures.

## Cost class

Edit, for the reconciliation itself (the family builds are their own small builds). The registry's loader
and readers are COL-A's small build with the three keys above.
