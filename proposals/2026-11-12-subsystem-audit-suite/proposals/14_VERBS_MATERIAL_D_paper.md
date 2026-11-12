# 14 · VERBS · MATERIAL · D — paper that says something: `create_record`, `forge`, `survey`, `destroy_record`, `seize`

## Status: PROPOSED

Batch M-D of `audits/14_VERBS_MATERIAL.md` §18 (its §1, §4, §11, §2, §10). Needs batch M-A §2 (the
family's draw) and `08_FI_01_claim-sourced-referents.md` edit 1 (`holders_named`). Cites and does not
redo `08_FI_05_evidence-interface_B.md` (what a cited paper is), `08_FI_02_rumour-that-travels.md` §4 (the
told thing as a choice), `02_CHAR_offer_what_can_be_done.md` item 5 (the `individual` conjunct),
`12_ARCS_cited_evidence.md`. Reference under CLAUDE.md §0.05. Read at `84d2a02`.

## 1. What changes in `engine/season/` at runtime

A person writes down what he holds about something, and whoever comes to hold the paper learns it with
the writer on its chain. A forgery is a false copy of a paper the forger holds, naming a person he
chose, at a quality the draw sets. A survey can come back thin. A paper that names its holder can be
burned, cleanly or not. A warrant against a person licenses taking his papers. Declared hash mover; the
largest in the family (`create_record` is 231 of 1,529 resolved acts at seed 0).

## 2. `create_record`: an account

**Problem.** 238 of 238 `text` Records at seed 0 after two seasons have no content (`mat_probe_s0_2.txt`);
cohorts wrote 115 of 231.

| owner | edit |
|---|---|
| `rosters.yaml: record_kinds.values` | `account: [terms, said]`, with a note: *minted by a computed `create_record`; `terms` is the act's `subject` (`content.read_from`), `said` the `Said` the writer copied at CHOOSE; a `record_sourced_operands` kind mapping `subject: terms`*. `text: []` stays for a hand-built act |
| `verb_table.yaml`, `create_record` | below |
| `decision/options.py` | nothing new: the named `own_ledger` conjunct already makes `opening_set` copy `said_of` onto the Candidate and decline when there is nothing to say (T4). When `08_FI_02` §4 lands, the same fan chooses which claim |
| `loop/effects_information.py::_eff_create_record` | a payload that declares no `kind` and carries `said` mints `account` with `{terms: subject, said: <the Said, drifted at Partial by the lossy-copy rule `loop/witness.py::_told_value` uses>}`; a declared kind mints as today; any kind at Failure returns `NO_CHANGE` under the Failure band's kind |
| `loop/witness.py`, the content deposit | for a `content:account` deposit to a person who came to hold the Record, also deposit the `Said` as a told claim: source `told_by`, chain = the `Said`'s chain + the writer, through the told channel's own guard, refraction and credit. `[UNVERIFIED: the deposit's exact branch; the rule is FI-05-B E-3's, a citation is a telling, one deposit over]` |
| `rosters.yaml: graded_acts` | gains `create_record` |

```yaml
  - verb:        "create_record"
    stratum:     "uncontested_material"
    eligibility: ["own"]
    beneficiary: "actor"
    capability:  copying
    difficulty:  plain
    requires:    "the writer holds a claim on what he writes about, and is one person"
    requires_typed:
      all:
        - {form: own_ledger, of: subject, conjunct: holds}
        - {form: relation, of: actor, relation: individual}
    writes:
      Overwhelming: ["Record.exists", "Record.stages"]
      Success:      ["Record.exists", "Record.stages"]
      Partial:      ["Record.exists", "Record.stages"]
      Failure:      []
    emits:
      Overwhelming: ["record.created"]
      Success:      ["record.created"]
      Partial:      ["record.created"]
      Failure:      ["record.spoiled"]
    emits_on_refusal: ["record.refused"]
```

The cell binds a computed act. A hand-built act that declares a `kind` and no `said` (a works, an army,
`mint_planned_works`' direct call) is admitted by a second alternative the loader already has a shape for:
`[UNVERIFIED: whether an `any:` combinator exists in `data/requires.py`; if not, the declared-kind path
keeps today's untyped admission by a row flag `declared_kind_admits: true`, read by `_admits`]`.

## 3. `forge`: a false copy of a held paper

| owner | edit |
|---|---|
| `rosters.yaml` | `forgeable_kinds: [dispensation, petition, faction_sheet, account]`; `forged_key: {faction_sheet: head, dispensation: terms, petition: terms, account: terms}` (checked against `record_kinds`' key lists at import). `_FORGED_SHEET_KEY` becomes a read of this map |
| `queries/world_q.py` | `papers_held(w, p, kinds)`: Records on his own live holds of the given kinds; stamped as `Record.<kind>` |
| `verb_table.yaml`, `forge` | below |
| `loop/effects_information.py::_eff_forge` | copy the exemplar's `subject_matter`, set `forged_key[kind]` to the act's `to`, mint the same kind through `_mint_document` with `forgery_quality` from the band; decline (`forge.refused`) where the exemplar is gone, its kind is not forgeable, or `to` already is the true value. `_mint_sheet`'s `forged=` arm is deleted; `survey` no longer shares a body with `forge` |
| `data/fixtures.py` | `forgery_quality_step=1`: Overwhelming `default_forgery_quality + step`, Success the default, Partial `max(1, default − step)` |
| `rosters.yaml: graded_acts` | gains `forge` |

```yaml
  - verb:        "forge"
    referent_class: Record        # a paper he holds (`papers_held` over `forgeable_kinds`)
    capability:  copying
    difficulty:  demanding
    counterparty_note: "`to` is whom the false paper names; no second side, so no `counterparty:`"
    requires:    "the forger holds the paper he copies, knows the person it will name, and is one person"
    requires_typed:
      all:
        - {form: existence, of: subject, kind: Record}
        - {form: relation,  of: subject, relation: held_by}
        - {form: existence, of: to, kind: Person}
        - {form: relation,  of: actor, relation: individual}
    writes:
      Overwhelming: ["Record.exists", "Record.forgery_quality"]
      Success:      ["Record.exists", "Record.forgery_quality"]
      Partial:      ["Record.exists", "Record.forgery_quality"]
      Failure:      []
    emits:
      Overwhelming: ["record.forged"]
      Success:      ["record.forged"]
      Partial:      ["record.forged"]
      Failure:      ["forge.failed"]
    emits_on_refusal: ["forge.refused"]
```

Binding `to` beside `subject` puts `to` in `known_person_operands`, so `operand_bags` forms one Candidate
per person the forger knows, himself included (`issue`'s IN-10 shape). That fan is a cost (H-361 measured
`marshal`'s); it is bounded by `Fixtures forge_names` (the newest N known persons, shipped 3).
`[ASSUMPTION; medium; Jordan to correct]`

## 4. `survey`: thin or full

`queries/person_q.py`, new and World-free: `faction_named(ledger, subject) -> Optional[str]`, the one
faction the holder's own claims give `subject`: a claim of a kind a `commit` opener emits pairing him with
a faction Proposition, a holder `holders_named` gives a rung, or the Proposition itself; `None` for none
or two. `rosters.yaml`: a line `own_faction_declines: [survey]` read in `opening_set` as
`own_stance_declines` is (the referent is kept only where `faction_named` answers). When CHAR's single
own-state decline lands this line folds into it.

```yaml
  - verb:        "survey"
    capability:  inquiry
    difficulty:  routine          # + `opposition` (SC-B) when his ledger names the faction's head
    requires_typed:
      all:
        - {form: own_ledger, of: subject}
        - {form: relation, of: actor, relation: individual}
    writes:  {Overwhelming: ["Record.exists"], Success: ["Record.exists"], Partial: ["Record.exists"], Failure: []}
    emits:   {Overwhelming: ["faction.surveyed"], Success: ["faction.surveyed"], Partial: ["faction.surveyed"], Failure: ["survey.failed"]}
    emits_on_refusal: ["survey.refused"]
```

`_eff_survey`: at `Partial` the minted sheet keeps `proposition` and `head` and carries `members`,
`holdings` and `seats` as empty lists (the key set is exact, so the keys stay). `graded_acts` gains it.

## 5. `destroy_record`: released, on a paper that names its holder

`data/fixtures.py`: `withheld_verbs` loses `destroy_record` (H-156 option (b); the member is the control
arm). `rosters.yaml: referent_classes` gains `Damning`; `queries/world_q.py::papers_damning(w, p)`: the
Records on his own live holds whose content, as his own content claim holds it, names him
(`world_q.named`, the reader clause 3 of Q2 uses). `own_hold_declines`' line for this verb goes (the stamp
is narrower).

```yaml
  - verb:        "destroy_record"
    eligibility: ["own"]
    referent_class: Damning
    capability:  none
    capability_note: "burning a paper draws on no skill; the draw is whether it is seen"
    difficulty:  plain            # + `watch`: (persons present at his rung − 1) x Fixtures watch_step
    requires_typed:
      all:
        - {form: existence, of: subject, kind: Record}
        - {form: relation,  of: subject, relation: held_by}
        - {form: relation,  of: actor, relation: individual}
    writes:  {Overwhelming: ["Record.exists"], Success: ["Record.exists"], Partial: ["Record.exists"], Failure: []}
    emits:
      Overwhelming: ["record.destroyed"]
      Success:      ["record.destroyed"]
      Partial:      ["record.destroyed", "destroy.seen"]
      Failure:      ["destroy.seen"]
    emits_on_refusal: ["destroy.refused"]
```

`rosters.yaml: covert_kinds` gains `record.destroyed` (the mask rule is the one
`14_VERBS_MATERIAL_A_mending.md` §5 states for `site.damaged`, and carries the same `[UNVERIFIED]`).
`graded_acts` gains it. The §E3 placeholders `hold:<record>` and `presence` leave the eligibility list:
they decline unconditionally (H-75) and the cell asks what they meant.

## 6. `seize`: a person's papers, an occupied place

| owner | edit |
|---|---|
| `queries/world_q.py` | `papers_warranted(w, p)`: for each person a `warrant_sourced` dispensation on his own live hold names, the Records `person_q.holders_named(p.ledger, record)` gives that person; stamped `Record`. `places_occupied(w, p)`: the `march_target_kinds` rungs a seat he holds occupies (`occupying_faction`, its one owner); stamped `Occupied` (new class) |
| `decision/options.py::opening_set` | `seize` leaves `warrant_sourced`'s narrowing (the stamp is the narrowing); `arrest` keeps it |
| `loop/effects_information.py::_held_warrant_names` | true when a held warrant names the Record **or the person who holds it** (`hold_force`) |
| `rosters.yaml: graded_acts` | gains `seize` |

```yaml
  - verb:        "seize"
    referent_class: Record        # and Occupied: a row may list two classes `[UNVERIFIED; if not, the Rung half is a second row, `occupy`, with this row's Rung columns]`
    capability:  none
    difficulty:  routine          # + `opposition` (the holder's score halved) for a Record; + `watch` for a Rung
    writes:
      Overwhelming: ["Tenure.until", "Tenure.since"]
      Success:      ["Tenure.until", "Tenure.since"]
      Partial:      []
      Failure:      []
    emits:
      Overwhelming: ["record.seized", "rung.seized"]
      Success:      ["record.seized", "rung.seized"]
      Partial:      ["seize.resisted"]
      Failure:      ["seize.resisted"]
    emits_on_refusal:             # unchanged
      eligibility: ["seize.unauthorized"]
      authority:   ["seize.unauthorized"]
      write:       ["seize.refused"]
```

`_eff_seize` at Overwhelming carries, as `observed`, one `held_by` Observation per other Record the
dispossessed person holds; at Partial one for the Record sought (he learns where it is). `_seize_rung` at
Partial stages `-graded_amount(w, res, _fall(...))` on each garrison Site of the place (adding
`Site.condition` to the Partial band's `writes`). The holder witnesses `seize.resisted` and is free to
`give`, `conceal` or `destroy_record` the paper.

## 7. Order of landing

`create_record` → `survey` → `forge` → `destroy_record` → `seize`. Each its own declared mover.
`create_record` first: the other four act on papers that say something. MILITARY's `kind: army` gates
plant a degree or accept a retry from the same commit (`audits/14_VERBS_MATERIAL.md` §17.2).

## 8. Gate and falsifier

- **`create_record`.** Realm, seeds 0 to 2: `account` Records with content > 0 and none written by a
  cohort. A two-hearth fixture: A writes an account of a deed, `give`s it to B; B's ledger holds the deed
  with A on the chain; B's candidate set on that subject differs from the control (the witness edit off).
  Across seeds 0 to 19 both a faithful and a drifted account occur.
- **`forge`.** `08_FI_03`'s `inquiry_world`: a forged writ naming a third person, given to its
  addressee, is followed by a `comply` the control lacks; a `research` at a planted `Success` deposits
  `(record, record.forged, True)`; one quality step higher, the same roll fails.
- **`survey`.** Realm: post-admission `survey.refused` 0 or stale only; full and thin sheets both occur.
- **`destroy_record`, `seize`.** One fixture, FI-05-B's hearing: a seized account is cited by the seizer;
  a destroyed one cannot be cited by anybody; at a planted `Partial` seizure the warned holder forms
  `destroy_record` the next round and the control does not.
- **Falsifiers.** An account whose receiver holds nothing new. A forgery of a paper the forger never
  held. A sheet with a non-empty list at `Partial`. A paper destroyed at `Failure`. A `seize` Candidate
  whose subject is a person.
- **Planted failure.** Pin the degree at `Success`: no drifted account, no thin sheet, no resisted
  seizure; each gate that asks for a spread must go red.

## 9. NERS reading (E last)

N: M-REC and M-INFO are the first stage of the arc sequence (`audits/12_ARCS_adjudication.md` §5) and
rest on a paper that carries content; top-down (the detective precedent: evidence held, moved, hidden,
forged, cited), bottom-up (one kind, one deposit branch, one copied operand that `tell` already has),
lateral (the hearing's `cites`), diagonal (a person-scale letter moves a faction-scale decision). R: a
letter intercepted, a writ forged, a ledger burned, a thin report acted on, all without a player. S: one
mint, one quality field, one copy rule, the family's draw. E, last: one record kind, four stamps and five
banded rows, against 238 blank papers and three verbs that cannot execute.

## 10. Cost class

Small builds, five declared movers. Lanes: FI (owner), SC (the consumer of cited paper), CHAR, BINDING
(`issue`'s writs are what is forged and what warrants).
