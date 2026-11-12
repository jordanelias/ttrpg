# INST-SYN-A — one institutional kit: one registry, one record-kind scheme, one seat row, one obstacle-term list, one fixture style, one arrangement vocabulary

Reconciled: 2026-11-12, U5d closure — folded Jordan's answers (`unified/DECISIONS_ANSWERED.md`) into the kit's five meetings with Layer 1 (audit §8.2). **L-1 / A-12**: a seat may carry a modifier, so "no seat-row key of the kit is read by any roll" is no longer a constraint; the kit may add an office modifier, entered as a named term through the one obstacle composer (`U5c_SC_one_obstacle_form.md`) so that office and regard are not counted twice, and the dignity "precedence" step withdrawn by X-19 may be re-entered in that form by a later content edit (none is added here). **L-2 / A-13**: the three optional seat facts (the clerks an order passes, paper-hands, the exit audit) are ruled; a seat declaring none behaves as today; the Layer 1 seat-list text is owed, not applied. **L-3 / A-14**: a vote is a draw on the voter inside the presiding person's act; the ballot stays SC's (X-15). **L-5 / A-10**: institutions are the loop's own verbs and data; no module. **A-21 / A-22**: X-33's per-form `basis` stands with its two values ruled: a publication (`purview`) reaches everyone on the ground with the news of its issue; an order (`command`) binds the issuing seat's sworn men, the holders of seats it may revoke and the unseated in its land, and a writ to a superior is a petition. **A-41**: no `corvee` form is authored; caste is carried by regard, by the vote weight of `U5d_FA_owed_edits.md` §4 and by the practice table of `U5d_SE_cohort_heavy_moves_and_caste.md`.

## Status: PROPOSED

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
3. Eight seat-row keys, three roster members, one new roster, one anchor form.
4. Two obstacle terms added to SC-B's roster (`obligation`, `remove`), beside the BINDING lane's
   `standing`.
5. Eleven fixtures in one style.
6. One arrangement key (`quorum_share`), one band-map cell value (`release`, requested of SC), nine rows.

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
  - id: warrant                 # VEN-C: admission to a roll kept by warrant
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
    lapse: stands               # an unpaid bond does not vanish; `debt.lapsed` marks it
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
| `obstacle_terms` (SC-B's roster) | add `obligation` after `regard`, `remove` after `stakes` | VEN-A edit 1; COL-B §1 |
| `conferral_bases` | add `lot` | VEN-C edit 1 |
| `binds_bases` | add `members_by_warrant` | VEN-C edit 1 |
| `patronage_bases` (new) | `[purview, own_faction]` | PAP-B edit 1 |
| `office_bodies.<body>.term` | optional seasons | BYZ-C edit 3 |

### 3. `engine/season/offices.yaml`, `data/rosters.py::_load_offices`, `state/carriers.py::Office`

Eight optional keys, each folded into the hashed representation only when present (FA-P3's rule, so an
unkeyed world's hash does not move). Refusals at load:

| key | refused when |
|---|---|
| `dignity` | not an int in `[1, dignity_grades]`; or the row's `remit_acts` is not `[]`; or `revocation` is not `null` |
| `upkeep` | not an int ≥ 0 |
| `passes_through` | a member that is neither an `office_bodies` name nor `{seat: <row id>}` |
| `hand_term` | not a positive int |
| `patronage` | a member off `patronage_bases` |
| `eligible_from` | not a row id |
| `cooling_off` | not a positive int; or the row has no `term` |
| `audit_at_exit` | not an `arrangements.yaml` id |

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
| `owed_to(p, holder_seats, held_terms)` | `queries/person_q.py` | VEN-A edit 3; an `oblige` counts only if `gate.py::sworn_to` counts it |
| `remove(w, place_a, place_b)` | `queries/world_q.py` | COL-B §1 |
| `upkeep_owed(w, seat, person)` | `queries/world_q.py` | BYZ-B edit 3 |
| `hands_open(w, p)` | `queries/world_q.py` | BYZ-C edit 7 |
| `audits_due(w, p)` | `queries/world_q.py` | X-12: for each closed `hold` on a row carrying `audit_at_exit` whose `tenure.closed` claim `p` holds and over whose seat `p` may open (VEN-C edit 4's set), the departed holder (`Party`) and the arrangement |
| `may_seat`, `PATRONAGE_RULES`, `FILLED_BY["lot"]` | `state/gate.py` | VEN-C edit 4; PAP-B edit 3 |
| `legitimacy(…, seat, fx)` | `queries/person_q.py` | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` |

### 5. `engine/season/data/fixtures.py`

The table of audit §3.6, each row shipped at its control, each with a NUMBER row in `hole_register.yaml`.
Not added: `founding_confidence`, `procedure_draws`, `pledge_step`, `oath_step`, `levy_ob`,
`provisional_term` (the BINDING lane's).

### 6. `engine/season/arrangements.yaml`, `data/arrangements.py`

- `_ARRANGEMENT_KEYS` gains `quorum_share` (PAP-B edit 6, unchanged).
- The tally of a `declared` row (the ballot loop `13_SC_draw_for_unrolled_contests.md` edit 3 adds) is
  the one table of audit X-15; `verb_table.yaml: determine` gains `matter.undetermined`.
- Rows: `acclamation` (BYZ-E edit 4), `conclave` (PAP-B §2), `consecration` (PAP-C §2), `debt_suit`
  (VEN-B edit 6), `security_bench`, `enrolment_ballot` (VEN-D §4), `audit`, `quo_warranto` (COL-C edit 1),
  each as its file wrote it. `exit_audit` (VEN-D §4) is not added: every `audit_at_exit: exit_audit` in
  VEN-C and VEN-D reads `audit`. `general_council` waits on Jordan.

## Gate (execution artifacts)

1. **Neutral until used.** With the registry empty, no row keyed and all fixtures at control:
   `build_realm(0)` `content_hash` at build, one season and two seasons equals the pre-item hash
   (`PYTHONHASHSEED=0`).
2. **The loaders refuse.** One planted malformed row per refusal named in edits 1 and 3 raises, naming
   the row; the sixteen forms load.
3. **One of each, hand-built.** A two-seat world with a seat carrying all eight keys, one `tribute`, one
   `debt` and one `avoidance`: `dues` stamps the tribute payer and the debtor and not a bystander; after a
   `transfer.made` to the clause's place the stamp is gone and returns next period for the tribute and not
   for the debt; an addressee whose `comply` drew Success has the named dealings declined and one whose
   `comply` drew Failure does not.
4. **One term, one name.** On a hand-built `issue` to a sworn addressee two territories away, the
   recorded term list (SC-P1) carries `obligation` and `remove` and no `oath_step`.

## Falsifier

A hash move at gate 1. A `debt` whose debtor `dues` does not stamp (the second occasion source came
back). A form row with `by: addressee` under `made_by: covenant` that loads. A seat row carrying
`audited:` that loads. A roll over 200 seeds of gate 3's `comply` in which every addressee declines (the
writ would be a switch).

## What it does not do

It builds no institution: every institution is the family proposals' content on these owners. It adds no
verb, no Tenure kind, no carrier, no stored quantity. It does not rename `carriage`
(`14_VERBS_MATERIAL_B`) or `distance` (`14_VERBS_SOCIAL1_B`), which are the same quantity as `remove`;
those files are other lanes' and the collision is listed for them and for unification lane U1.

## NERS reading

- **N.** From above, a designer authors any grant, sanction or bond as one row of one file. From below,
  a person reads what he owes from one occasion. Laterally, a papal sentence, a ducal homage and a
  banker's bond are answered, kept and sued on by the same readers. Diagonally, a hearth's debt and a
  realm's tribute are one clause shape. Remove the reconciliation and the same sanction has two forms
  and the same deed three certificates.
- **R.** Customisation is the point: sixteen forms, eight keys and thirteen terms are the whole authoring
  surface of every institution. Complete at the extremes: an empty registry is today's world; a form with
  no clauses is a bare decree.
- **S.** One registry, one set of readers, one roster of terms, one fixture style, one tally. The kit
  removes three S defects the lanes would have landed (two audits, three certificates, two distances).
- **E, last.** Against four families' worth of institutions: one file, one kind, three content keys,
  eight row keys, two terms. It is smaller than the sum of what the four lanes asked for, by one record
  kind, one registry, one Query, two rows and five fixtures.

## Cost class

Edit, for the reconciliation itself (the family builds are their own small builds). The registry's loader
and readers are COL-A's small build with the three keys above.
