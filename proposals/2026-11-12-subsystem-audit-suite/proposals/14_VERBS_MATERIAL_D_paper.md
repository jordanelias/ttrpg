# 14 · VERBS · MATERIAL · D — paper that says something: `create_record`, `forge`, `survey`, `destroy_record`, `seize`

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-22) — `create_record` and `forge` take the route shape (the band is a quality on one Record); a row whose bands write different cells declares `contests: "a task"` (`U5c_VERBS_residue_and_governance_owner.md` §1). `watch` is the one name for who is there to see (`U5c_SC_one_obstacle_form.md` §2).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.2, §2, 7b.4; F-R4-01, F-R4-12): `create_record`, `forge`, `survey` take shape (a) (flat columns, failed draw in the `draw` refusal clause); `destroy_record` and `seize` take shape (b), `contests: "a task"`; `graded_acts` → `graded_tasks` (D-U1-11i); `seize`'s opposition is the holder's trained score through `opposed_ob` (A-79, D-U1-02), not "halved"; its keyed refusals flatten to one kind (a contested row keys one kind, `data/verbs.py:945-967`); §6's Rung half is the carrier of A-66's seizure after a won march and passes the anchored seats by the existing bases (`unified/U3_CONFLICT_LEDGER.md` C3-L12, C3-L7; lands in B23, U3 §4.1 row 82); the Rung half's row is not named `occupy` (A-66 uses "occupy" for holding ground without title); the two `[UNVERIFIED]` marks settled at the tree (the told deposit's branch; covert masking); C3-R7 (G-02, G-03 fallbacks are the plan); A-81 (C3-C11), A-30, U3 batch B26, R4 7b.0 block.

## Status: PROPOSED

Lands in batch: B26 for §2–§5 and §6's Record half (`unified/U3_DEPENDENCY_ORDER.md` §3.1); §6's Rung half (the seizure of a place) in B23 with `U5d_FA_land_and_seats_pass_on_a_won_march.md` (U3 §4.1 row 82, C3-L12).
Depends on: `14_VERBS_MATERIAL_A_mending.md` §2 (B12: `graded_amount`, the shapes); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` items 1, 2, 4 (B07; C3-R1); `U5c_VERBS_residue_and_governance_owner.md` §1 (B07: the `a task` prize); `08_FI_01_claim-sourced-referents.md` edit 1 and `08_FI_02_rumour-that-travels.md` (B11); `08_FI_05_evidence-interface_B.md` (B24); `02_CHAR_offer_what_can_be_done.md` item 5 (B10: the `individual` conjunct); for the Rung half, `U5d_FA_land_and_seats_pass_on_a_won_march.md` e1 as rewritten by C3-L7 (B23).
Lane: FI. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; the told deposit (§2) and the two contested rows `opus`; one `opus` read of each gate's spread. Test file: `engine/season/tests/test_vm_mat_d_paper.py` (one function per §8 gate; the probe `mat_probe.py` cited as evidence is not a gate).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's skill score in the row's `capability:` (A-6); the governing attribute as levels (A-7); a wound a level against the roll (A-8). Every draw takes `H(w.world_seed, w.tick, <actor id>, "<verb>.task")` (A-30). **A-81:** each failed draw (`record.spoiled`, `forge.failed`, `survey.failed`) is a refusal Event witnessed by those present (a claim of it to each) and, for a writer alone, his own firsthand claim `(self, <verb>.failed, True)`; `destroy.seen` and `seize.resisted` name the actor and are deposited to those present and, for `seize`, to the holder.

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-02, G-03) — two `[UNVERIFIED]` marks settled against the proposal's first reading: `data/requires.py` has no `any:` combinator and a verb row carries one `referent_class`. In both places the proposal's own stated fallback is now the edit.

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
| `loop/witness.py`, the told channel | for a person who came to hold an `account` Record (the `newly_held` pairs the content deposit reads), also deposit the `Said` as a told claim: source `told_by`, chain = the chain the paper's own `said` content records + the writer the paper names, through the told channel's own guard, refraction and credit. *(W3-4a: the `[UNVERIFIED]` branch is settled at the tree.)* The content deposit (`loop/witness.py:823-846`, "THE FOURTH DEPOSIT") carries **no attribution** by design (*"this document says X, never the Duke wrote X … what makes a forgery playable"*), so the told claim is **not** added there; it is one more case in the told-channel block that follows it (`:848`, "THE TOLD CHANNEL"), and its chain is read from the paper's content, never from the act store, so a forged account's false chain is what its holder comes to believe (the rule is FI-05-B E-3's: a citation is a telling) |
| `rosters.yaml: graded_tasks` | gains `create_record` |

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
    writes:  ["Record.exists", "Record.stages"]   # shape (a): one Record; the band sets the drift of `said`
    emits:   ["record.created"]
    emits_on_refusal: {draw: ["record.spoiled"], <each derived clause>: ["record.refused"]}   # MAT_A §2 row 5 note
```

The cell binds a computed act. A hand-built act that declares a `kind` and no `said` (a works, an army,
`mint_planned_works`' direct call) is admitted by a second alternative the loader already has a shape for:
`[GROUNDED, 25 G-02: there is no `any:` combinator. `data/requires.py:1021-1026` builds `all:` only
(`AllOf`, `:558`), and a clause's `form` must be a `requires_forms` roster member (`:1027-1030`). So the
declared-kind path keeps today's untyped admission by a row flag `declared_kind_admits: true`, read by
`_admits`]`.

## 3. `forge`: a false copy of a held paper

| owner | edit |
|---|---|
| `rosters.yaml` | `forgeable_kinds: [dispensation, petition, faction_sheet, account]`; `forged_key: {faction_sheet: head, dispensation: terms, petition: terms, account: terms}` (checked against `record_kinds`' key lists at import). `_FORGED_SHEET_KEY` becomes a read of this map |
| `queries/world_q.py` | `papers_held(w, p, kinds)`: Records on his own live holds of the given kinds; stamped as `Record.<kind>` |
| `verb_table.yaml`, `forge` | below |
| `loop/effects_information.py::_eff_forge` | copy the exemplar's `subject_matter`, set `forged_key[kind]` to the act's `to`, mint the same kind through `_mint_document` with `forgery_quality` from the band; decline (`forge.refused`) where the exemplar is gone, its kind is not forgeable, or `to` already is the true value. `_mint_sheet`'s `forged=` arm is deleted; `survey` no longer shares a body with `forge` |
| `data/fixtures.py` | `forgery_quality_step=1`: Overwhelming `default_forgery_quality + step`, Success the default, Partial `max(1, default − step)`, with a NUMBER row in `hole_register.yaml`. A quality step on one field, not a second share table (R4 F-R4-09; U1 §3) |
| `rosters.yaml: graded_tasks` | gains `forge` |

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
    writes:  ["Record.exists", "Record.forgery_quality"]   # shape (a): the band sets the quality
    emits:   ["record.forged"]
    emits_on_refusal: {draw: ["forge.failed"], <each derived clause>: ["forge.refused"]}
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
    writes:  ["Record.exists"]                # shape (a): Partial is a thin sheet, the same cell
    emits:   ["faction.surveyed"]
    emits_on_refusal: {draw: ["survey.failed"], <each derived clause>: ["survey.refused"]}
```

`_eff_survey`: at `Partial` the minted sheet keeps `proposition` and `head` and carries `members`,
`holdings` and `seats` as empty lists (the key set is exact, so the keys stay). `graded_tasks` gains it.

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
    contests:    "a task"         # shape (b): Partial and Failure emit `destroy.seen`
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

`rosters.yaml: covert_kinds` gains `record.destroyed`, read by `epistemic.trail_of` (the inquiry's
trail). *(W3-4a: settled at the tree, as in `14_VERBS_MATERIAL_A_mending.md` §5:)* no masking rule exists
or is added (`04` §C.6: covertness is presence), so a person co-located at the burning holds the
attribution at every band; the clean/seen difference between bands is the `destroy.seen` deed. It is not
a `graded_tasks` member (a contest row). The §E3 placeholders `hold:<record>` and `presence` leave the
eligibility list: they decline unconditionally (H-75) and the cell asks what they meant.

## 6. `seize`: a person's papers, an occupied place

| owner | edit |
|---|---|
| `queries/world_q.py` | `papers_warranted(w, p)`: for each person a `warrant_sourced` dispensation on his own live hold names, the Records `person_q.holders_named(p.ledger, record)` gives that person; stamped `Record`. `places_occupied(w, p)`: the `march_target_kinds` rungs a seat he holds occupies (`occupying_faction`, its one owner); stamped `Occupied` (new class) |
| `decision/options.py::opening_set` | `seize` leaves `warrant_sourced`'s narrowing (the stamp is the narrowing); `arrest` keeps it |
| `loop/effects_information.py::_held_warrant_names` | true when a held warrant names the Record **or the person who holds it** (`hold_force`) |
| *(none)* | `seize` is a contest row (shape (b)), not a `graded_tasks` member |

```yaml
  - verb:        "seize"
    referent_class: Record        # one class per row `[GROUNDED, 25 G-03: `VerbRow.referent_class` is one string, `data/verbs.py:245`, loaded by `str(...)` at `:668` and checked as one roster member at `:693`; so the Rung half is a second row with this row's Rung columns, below]`
    contests:    "a task"         # shape (b): bands write different cells and emit different kinds
    capability:  none
    difficulty:  routine          # + `opposition` (the holder's skill score through `opposed_ob`, A-79, D-U1-02)
    writes:
      Overwhelming: ["Tenure.until", "Tenure.since"]
      Success:      ["Tenure.until", "Tenure.since"]
      Partial:      []
      Failure:      []
    emits:
      Overwhelming: ["record.seized"]
      Success:      ["record.seized"]
      Partial:      ["seize.resisted"]
      Failure:      ["seize.resisted"]
    emits_on_refusal: ["seize.refused"]   # a contested row keys one kind (`data/verbs.py:945-967`); the clause rides `observed`
```

*(W3-4a.)* The tree's keyed refusal (`seize.unauthorized` for the seat, `seize.refused` for the write) is
flattened to one kind because a contested row may key only one (`issue`'s precedent in
`14_VERBS_BINDING_D_orders.md` edit 8); the refusal's `observed` reads still name the failed clause.

`_eff_seize` at Overwhelming carries, as `observed`, one `held_by` Observation per other Record the
dispossessed person holds; at Partial one for the Record sought (he learns where it is). The holder
witnesses `seize.resisted` and is free to `give`, `conceal` or `destroy_record` the paper.

**The Rung half: the seizure of a place (C3-L12, C3-L7; A-58, A-66; lands in B23).** A second row,
`seize_place` `[ASSUMPTION: the name; not `occupy`, which A-66 uses for holding ground without title;
U1 to confirm; the verb roster's count moves by one at B23, C3-N30]`, class `Occupied` (stamped by
`places_occupied` above), `contests: "a task"`, `difficulty: routine` + `watch` (OBS member 22),
`writes: {Overwhelming: ["Tenure.until", "Tenure.since"], Success: ["Tenure.until", "Tenure.since"],
Partial: ["Site.condition"], Failure: []}`, `emits: {Overwhelming: ["rung.seized"], Success:
["rung.seized"], Partial: ["seize.resisted"], Failure: ["seize.resisted"]}`, `emits_on_refusal:
["seize.refused"]`. It is **the carrier of A-66's seizure**: after a `Won` on a march into held territory
the field's fold writes no title (`U5d_FA_land_and_seats_pass_on_a_won_march.md` e1 as rewritten by C3-L12);
the aggressor's scene continues (A-9) and he may form `seize_place` (title), stay in occupation (no act;
his army is there), or withdraw (`march`/`move` away). `_seize_rung` at O/S, after opening the seizer's
`hold` on the rung, closes each seat anchored on it whose row carries `revocation: holder_of_rung` through
the existing revocation basis with `Act.via` = the new hold, and opens it to the seizer by the existing
claim basis (C3-L7); a seat he cannot sit is closed and left vacant. At Partial it stages
`-graded_amount(w, res, _fall(...))` on each garrison Site of the place. A place a seat's faction holds is
declined, as today.

## 7. Order of landing

`create_record` → `survey` → `forge` → `destroy_record` → `seize` (Record half), each its own declared
mover, in B26. The Rung half (`seize_place`) lands earlier, in B23, with the land plan (C3-L12).
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
- **`seize_place` (B23).** A hand-built won march into held territory: the field's fold writes no title;
  the aggressor's opening set holds `seize_place` on the place; at a planted Success the rung's hold and
  each anchored seat whose row carries `revocation: holder_of_rung` pass to him; with that value null, no
  seat moves (C3-L7's control); not forming the act leaves title with the holder and the army in place
  (A-66's occupation).
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
