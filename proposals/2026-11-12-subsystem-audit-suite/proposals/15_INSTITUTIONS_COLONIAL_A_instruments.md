# COLONIAL-A — an instrument is defined parameters: the closed set of grant and treaty forms, and the three readers `covenant` has waited for

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-01, X-02, X-03, X-09, X-11, X-29, X-31) — this file's registry is the kit's one home and gains what the other three lanes need (`15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` edit 1): the top-level key is `forms:` and a second section `seeded:` holds the Records a world begins with; a form row gains `record_kind`, `bearer` and `recites`; a clause's `by:` may be `addressee`, its `over:` may be `named`, its `to:` may be `named_rung`; six rows are added (`warrant`, `commission`, `avoidance`, `interdict`, `tithe`, `debt`); `recognition` is not a form (a certificate is the `recites` key); "live" for a covenant-made form is `14_VERBS_SOCIAL1_B_documents_and_obedience.md`'s `covenant_in_force`; `dues` stamps a clause while `world_q.owed` is above zero; a breach also excuses the wronged party (`person_q.excused`). The schema, the loader, the ten rows, `dues`, `kept` and `breaches` stand. Every finding below stands.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_COLONIAL.md` §4, §6.1, §10, §12 batch C-1. Cross-lane: the `covenant`
and `issue` rows are the SOCIAL and BINDING verb lanes' (`proposals/14_VERBS_SOCIAL2_A_formation_on_what_is_known.md`,
`audits/14_VERBS_BINDING.md`); FA-P1 (`proposals/06_FA_decree_binds.md`) owns how a writ's terms reach an
addressee. This file edits neither row's formation. Nothing is ratified by being written.

## What it changes in `engine/season/` at runtime

1. A `dispensation` minted by `issue` or `covenant` may name a **form**, a row of a new closed registry.
2. A party to a live formed instrument has, on the question he answers, the referent of each clause he
   owes and has not yet performed this period (an occasion, in `vacancies`' shape). Whether he performs is
   his choice through the one chooser; the performing act is rolled wherever its own row is graded
   (`15_INSTITUTIONS_COLONIAL_B_distance.md`).
3. A party who, **by his own ledger**, believes the other side has failed a clause has the other party
   and the granted seat on his question.
4. With the registry empty (the first commit) nothing moves: `build_realm(0)` hash EQUAL
   (`600d8b27147478e158553552cc1409a5` at `bb6dfc3`, `PYTHONHASHSEED=0`; audit E-1). Each authored row
   that a seeded world then uses is a declared mover.

No Record kind, Tenure kind, verb, remit act or stored quantity is added.

## The problem (evidence)

- `engine/season/verb_table.yaml`, `covenant.writes_note`: "ITS READERS ARE DEFERRED (#453 §10.4 step 7):
  `loop/effects_economy.py::_renewals` reads `oblige` edges only and `queries/world_q.py::mustered`
  faction members only, so neither tribute nor allied sides read a covenant."
- At `build_realm(0)` the world holds two Records, both `works`, and no `dispensation` (audit E-1). The
  "ancient trade treaties" of `goal_kommerkiarios_treaty_order` (`goals.yaml:484-493`), the containment
  grant (`canon/03_canonical_timeline.md:58`) and the settlement of 200 AG (:88) are carried by nothing
  a person can keep, break or cite.
- A covenant's `terms` is an uttered Proposition (`mood`, `subject`, `predicate`, `value`, `when`,
  `scope`; `state/carriers.py:968-978`). Its `predicate` is free text. No reader can tell a tribute from
  an alliance.
- The tree's precedent for a closed set of parameterised forms with one loader is `arrangements.yaml`
  (header: "the claim under test: a proceeding is just defined parameters").

## The resolution, decided

**An instrument is just defined parameters.** Ladder step 4 (precedent: `arrangements.yaml` and
`data/arrangements.py`). The Record stays a `dispensation`; its `terms` stays an uttered Proposition
(K-54 unchanged); it gains one content key naming a form; the form's clauses are read by three Queries
that store nothing.

**A clause forbids nothing.** A `forbears` clause is not a gate. The bound party can do the forborne
thing; doing it is an Event others witness, and what they do about it is theirs to choose (precedent:
`07_SE_treasury_granary_B.md` R-SE-29, "withholding is the act"). **Keeping is never automatic either:**
every `due` is performed by an act of the bound party, and that act is a draw where the act can go either
way (a tribute is a `transfer` between places).

## Exact edits, by owner

**1. `engine/season/instruments.yaml` (new; the single owner of the forms).** Header states the claim and
the count. Row schema, every key required unless marked:

```yaml
instruments:
  - id:          farm
    made_by:     covenant            # issue | covenant
    grantor_act: issue               # a rosters.yaml: remit_acts member the granting seat must hold
    term:        4                   # seasons; null = while the grantee holds the conferred seat
    renewal:     both                # grantor | both | none
    confers:                         # optional: the seat the grant establishes and confers on the grantee
      post:       "Farmer"
      at:         grant_ground       # the rung the instrument is drawn over (the act's `subject` place)
      remit_acts: [issue]
      conferral:  appointed
      revocation: rung_above_in_holdings
    due:
      - {by: grantee, kind: transfer.made, every: once, to: grantor_rung}
      - {by: grantee, kind: transfer.made, every: 1,    to: grantor_rung}
    forbears:
      - {by: grantor, kind: requisition.taken, over: grant_ground}
    lapse:       reverts             # reverts | stands
    hardens:     false
```

The ten rows of audit §4.3 (`homage`, `land_grant`, `march`, `farm`, `charter`, `staple`, `immunity`,
`tribute`, `wardship`, `capitulation`), each `grade: assumption`, each with a `source:` string naming the
research paragraph it is shaped on (a provenance string, never a reason). Amounts are **not** in the
form: how much rent or tribute is the act's own `amount` operand at the making, written into the
instrument's content beside `form`. Posts in `confers:` are generic labels `[ASSUMPTION; the names are
Jordan's, through `references/names_index.yaml`]`.

**2. `engine/season/data/instruments.py` (new; the one loader).** `data/arrangements.py`'s idiom
(`_refuse_unknown`, `_refuse_not_in`): refuses an unknown key; a `kind` that is not a
`data/verbs.py::DEED_KINDS` member; a `grantor_act` off `REMIT_ACTS`; a `confers:` whose `conferral` or
`revocation` is off its roster or whose `remit_acts` is not a subset of `REMIT_ACTS`; `made_by` off
`{issue, covenant}`; `every` that is neither a positive int nor `once`; `over` off `{grant_ground,
grantee}`; `to` off `{grantor_rung, grantee_rung, grant_ground}`. Exposes `INSTRUMENTS: dict[str, Form]`
(frozen dataclasses `Form`, `Clause`). `data/files.py` gains `INSTRUMENTS_YAML`; `data/__init__.py::
load_all` calls the loader. Import-order: `DEED_KINDS` is derived in `data/verbs.py`; the loader imports
it lazily inside `_load()` as `data/arrangements.py:36` records doing for its own derived map
[UNVERIFIED: that the same lazy import is admissible here; `data/arrangements.py:275` is the precedent].

**3. `engine/season/rosters.yaml: record_kinds`.** The `dispensation` row's content keys gain `form`
(optional; a writ with none is today's bare decree) and `amounts` (optional; a mapping from clause index
to an int). The loader refuses `form` on any other kind.

**4. `engine/season/rosters.yaml: choice_sourced`.** `covenant: [form]`, `issue: [form]`: the route
`marshal`'s `role` and `march`'s `posture` take (`data/verbs.py::_load_choice_sourced`,
`decision/options.py::operand_bags` at `:1344`; the function body was not opened [UNVERIFIED: that a
choice roster may be filtered per candidate]). The fan is the forms whose `made_by` is the verb and whose
`grantor_act` the exercised seat's grant carries, **plus the empty choice** for `issue` (a bare decree).
`loop/effects_information.py::_mint_document` writes the chosen `form` into the Record's content.

**5. `engine/season/queries/world_q.py` — two occasions.**

```python
def instrument_of(w, record_id) -> Optional[Form]      # the form a live dispensation names, or None
def clauses_binding(w, record_id, pid) -> tuple[Clause, ...]
    # the `due` clauses whose `by:` side `pid` is: grantor = the Record's maker; grantee = its `to`
def dues(w, pid) -> tuple[Referent, ...]
    # for each live formed instrument `pid` is party to (he holds it, or his own ledger holds its content
    # claim, FA-P1's `writs_addressed` test), each binding `due` clause with no matching deed in its
    # current period -> the clause's target (the rung to pay into, the ground to found on), classed by
    # `referent_classes`, stamped on out[0] by the one stamp site (`vacancies`' shape).
def breaches(w, pid) -> tuple[Referent, ...]
    # where person_q.kept(p, record) < 0: the other party (Person) and the conferred seat (Office).
```

"Matching deed": an Event of the clause's `kind` whose doer is the bound party (or a holder of the
conferred seat) and whose target is the clause's, inside the period `[made + k·every, made +
(k+1)·every)`. `dues` reads the world (it is an occasion source, as `vacancies` is); **`breaches` reads
only `pid`'s ledger**, through:

**6. `engine/season/queries/person_q.py::kept(p, record_content, now) -> int`.** Person-side, computed
when read, `suspicion_of`'s shape (FA-P1 edit 4): +1 for each elapsed period in which `p` holds a claim
of the due deed by the bound party; −1 for each elapsed period in which he holds none; −1 for each claim
of a forborne deed by the bound party over the clause's ground. Distinct origins once (ED-IN-0322, as
FA-P1 cites it). Nothing is written. Two parties' readings of one instrument differ whenever news of a
payment or a breach did not reach one of them, which `…_B_distance.md` makes ordinary.

**7. Lapse and renewal.** No MATTER pass is added. `Record.stages` already matures an instrument's term
(`covenant.writes_note`: "`Record.stages` as the term (matures at MAT)"). At maturity a form with
`lapse: reverts` whose `renewal` party has not re-made it is no longer live for `dues` and `breaches`;
the conferred seat's `hold` carries the same term (FA-P3's `term:` mechanism,
`06_FA_seat_terms_and_turnover.md`) and falls vacant by that existing path. `renewal` is the same verb
again by the same party.

## Gate (execution artifact)

One test file, `engine/season/tests/test_instruments.py`, and one seeded reading:

- loader refusals: each malformed row above raises naming the row; the ten shipped rows load.
- on a hand-built two-seat world with one `tribute` made at tick 0, `every: 1`: `dues(payer)` names the
  payee's rung in season 1; after a `transfer.made` by the payer to that rung it does not; in season 2 it
  does again.
- `kept` as the **payee** reads it is +1 after a season whose payment he witnessed and −1 after a season
  whose payment was made and not witnessed by him (the claim withheld from his ledger): the two readings
  differ by construction.
- realm reading: `build_realm(0)` with the three `homage` instruments of proposal D seeded, two seasons,
  seeds 0–2: the count of `dues` referents stamped, and of acts whose `occasioned_by` is one, printed.

## Falsifier

- Control: registry empty, base hash EQUAL at one and two seasons.
- Planted: delete the period test in `dues` (any past payment then matches for ever); the season-2
  assertion (the occasion returns) reddens.
- A bystander is offered nothing: a person not party to the instrument has `dues == ()` and
  `breaches == ()` whatever he has heard.
- A `forbears` clause refuses no act: the grantor's levy over the grant ground executes (or fails) on its
  own roll; only `kept` moves.

## What it does not do

No credit, no interest, no price (the banking lane's). No enforcement: nothing here compels a payment or
voids a grant. No public registry of instruments: a person knows of one by holding it or being told.
No clause over a quantity the engine does not emit (attendance, "good governance").

## NERS reading

- **N.** Top-down: a king's settlement with his dukes is a thing he can break. Bottom-up: a hearth head
  can know the farmer has no right to this levy. Lateral: tribute between two factions is read by both.
  Diagonal: a Church immunity is breached by a Crown officer and noticed by a parish. Vertical and
  horizontal: one schema at every rung. Remove it and `covenant` returns to a Record nobody reads.
- **R.** Strategic choice (which form, what term, what amount); variety (the same breach met by petition,
  release or march); drama with no player (audit §8); complete at the extremes: an instrument whose
  party is dead stamps nobody; one with no clauses is a bare decree.
- **S.** One methodology with `vacancies`, `writs_addressed` and `suspicion_of`; pauses nothing; hands to
  SC's hearing by `open_case`. One ladder for "what is owed": the clause, never a second tally.
- **E, last.** One file, one loader, three Queries, two roster cells, against ten institutions and every
  treaty in canon becoming playable. The ratio is good; the risk is a second such registry from another
  institution lane, which the synthesis lane must collapse into this one or this one into it.

## Cost class

Small build (loader and three Queries with their test file); the rows are edits.
