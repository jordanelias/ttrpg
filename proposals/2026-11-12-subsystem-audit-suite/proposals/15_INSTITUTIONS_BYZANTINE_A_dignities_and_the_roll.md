# INST-BYZ-A — dignities and the Roll: the founding order where persons can read it, and an honour that cites a deed

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §1.3 (D-2, D-5, D-6), §5, §6, §7.0; Jordan's fixed point
of 2026-11-12 (`INSTITUTIONS_BRIEF.md`); the standing rule of `AUDIT_BRIEF.md`. Batch A of six.
Depends on `06_FA_remit_grant_by_row.md` (remit by row), on the BINDING verb lane for `confer`'s row
text, and on `06_FA_office_capabilities.md` for the pool. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. **At build:** one Record of a new kind `roll` exists, held by the Chief Parliamentary Clerk, and
   every person holds, for each of the three founding seats, one deed claim whose subject is the seat.
   A declared build-hash mover.
2. **`person_q.legitimacy`** gains a third term, the presumption, read from those claims. At
   `presumption_gain: 0` (the control) it is today's function exactly.
3. **Seat rows may carry `dignity:`.** Six such rows are authored in the body `Imperial Court`, vacant
   at build. A `confer` on one requires the conferee's live oath to the conferring seat and a deed
   claim the conferrer holds about him; the cited deed is what the investiture publishes.
4. **`confer` is a draw** on the four-band ladder (§7.0 of the audit). With `procedure_draws: off`
   (the control arm only) it resolves as today.

## The problem (evidence)

- `build_realm(0)` (audit E-1): 13 persons hold a stance row toward the King (sum 59.00), **none**
  toward the Duchess of Hafenmark or the Duke of Varfell; mean regard 0.720, 0.000, 0.000. The world
  holds two Records, both `works`. The founding order Jordan states is nowhere a person can read, and
  the record case NPC-008 turns on does not exist.
- `canon/03_canonical_timeline.md:78-92`: the crown and the ducal houses are deed-families; the
  presumption is inherited and rebuttable. `person_q.legitimacy` (`:537-563`) has the rebuttable half
  (a window over the holder's deeds) and no inherited half but a stance row.
- The body `Imperial Court` (`rosters.yaml: office_bodies`) has no seat.
- `confer` carries no `contests:` (audit E-2): an appointment is a fixed function of the conferral
  basis. `06_FA_office_capabilities.md` records that the conferee is positional (the lowest id the
  conferrer knows).

## The resolution, decided

The founding order is authored once, in `offices.yaml`, and reaches persons twice from that one
owner: as a document (the Roll) and as claims (what everybody was told). A dignity is a seat row
with no remit (ladder step 4: `off_heir`, `offices.yaml:252-263`, and Layer 1 §B.7's "there is no
`Title` type"). An honour publishes a deed and is paid for; it adds nothing to anyone's regard by
existing. The order decides no outcome (the standing rule): it is the confidence of a claim.

## Exact edits

**1. `engine/season/offices.yaml` — new top-level section, after `titles:`.**

```yaml
# THE FOUNDING ORDER (Jordan, 2026-11-12: "the first king had the greatest accomplishment in the
# secession war, followed by the first Duke of Hafenmark and the first Duke of Varfell").
# One row per seat won in the Secession War. `deed` is a `data/verbs.py::DEED_KINDS` member; `order`
# is the rank of the accomplishment, read ONLY as the confidence of the claim `build_realm` deposits
# (`fixtures: founding_confidence`), never as a gate, a tie-break or a result.
founding:
  roll: {holder: "NPC-008", note: "the Record of kind `roll`; drawn up at the holder's seat rung"}
  entries:
    - {seat: off_king,              deed: field.won, order: 1}
    - {seat: off_duchess_hafenmark, deed: field.won, order: 2}
    - {seat: off_duke_varfell,      deed: field.won, order: 3}   # D-1: credited_in is §14 item 2
```

`[ASSUMPTION; medium; Jordan to correct]` the deed kind (`field.won` for all three; canon says
"wartime deeds" and no more). `[UNVERIFIED]` that `field.won` is scored by `deed_valence` for a
subject that is a seat id: `attributed_deeds` (`person_q.py:158-175`) filters an unpaired kind on
`c.subject == referent` and does not ask what the referent is; confirm that `field.won` is not a
paired kind before landing.

**2. `engine/season/rosters.yaml: record_kinds.values`** — add `roll: [entries]`. `entries` is the
list of `{seat, deed, order}` mappings above, copied at mint.

**3. `engine/season/offices.yaml: seats` — one new optional key, `dignity:`**, an int in
`[1, dignity_grades]`. A row carrying it must have `remit_acts: []` and `revocation: null` (the
loader refuses otherwise: a dignity with a remit is an office; a revocable one is not for life).
`[UNVERIFIED]` whether the seat-row reader refuses unknown keys; if it does, its key set gains this
and proposal B's and C's keys in the same commit.

Six rows, appended to `seats:` (posts are placeholders; canon names no court dignity, and research
never supplies a canon name: `rosters.yaml`'s source-precedence ruling):

```yaml
  - {id: off_dignity_1a, post: "[PLACEHOLDER] Dignity of the fifth grade",  rung: {realm: true}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 5, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A; Jordan names", note: "[NEW]. Vacant at build."}
  - {id: off_dignity_2a, post: "[PLACEHOLDER] Dignity of the fourth grade", rung: {realm: true}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 4, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_2b, post: "[PLACEHOLDER] Dignity of the fourth grade", rung: {realm: true}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 4, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_3a, post: "[PLACEHOLDER] Dignity of the third grade",  rung: {realm: true}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 3, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_3b, post: "[PLACEHOLDER] Dignity of the third grade",  rung: {realm: true}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 3, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_4a, post: "[PLACEHOLDER] Dignity of the second grade", rung: {realm: true}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 2, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
```

A closed number, deliberately: a place at the table is scarce, and it falls free only by a death or a
`release`. `[UNVERIFIED]` that `harness/populated.py` mints a row whose `holder` is null as a vacant
seat (`establish` leaves one vacant today, FA audit E-5; the authored-row path was not traced). If it
does not, the rows are minted by the build's own `establish` under `off_king`.

**4. `engine/season/data/fixtures.py`** — three fixtures:

| name | shipped | sweep | read by |
|---|---|---|---|
| `presumption_gain` | 0.5 | 0 (control) / 0.5 / 1.0 | `person_q.legitimacy` |
| `founding_confidence` | `[1.0, 0.8, 0.6]` of `Claim.confidence`'s full value, by `order` | flat `[1.0, 1.0, 1.0]` / the shipped | `harness/populated.py::build_realm` |
| `dignity_grades` | 5 | 3 / 5 / 7 | the `offices.yaml` loader |

**5. `engine/season/harness/populated.py::build_realm`** — after seats are built: mint the Roll
through `_mint_document` (kind `roll`, content `{entries: [...]}`, at the holder's seat rung, the
holder's `hold` riding on it), and for every person append one claim per entry:
`(entry.seat, entry.deed, True)`, source `told_by`, confidence `full · founding_confidence[order-1]`,
`when` the build tick. Both come from `OFFICES_FOUNDING` (the loader's one reading of edit 1).

**6. `engine/season/queries/person_q.py::legitimacy`** — signature gains `seat: Optional[str] = None`
and `fx=None`; body gains, after the existing sum:

```python
    if seat is not None and fx is not None and (g := float(fx.get("presumption_gain"))):
        if not _took_by_force(p.ledger, holder, seat):        # a dominance-kind deed of `holder`'s on `seat`
            for c in attributed_deeds(p.ledger, seat):        # the founding claims: subject is the seat
                total += g * deed_term(p, axis_w, c) * c.confidence / CONFIDENCE_FULL
```

`_took_by_force` reads `p`'s own claims only: any `standing_routes.kinds.dominance` deed attributed
to `holder` whose subject is `seat`. Person-side (AX-2). The two existing callers pass no `seat` and
are unchanged; the accession draw (proposal E) and the hearing's `opposition` term pass it.

**7. `confer` on a dignity row** (`loop/predicates.py::_req_confer`; `loop/effects_governance.py::_eff_confer`;
the row's text is the BINDING lane's):

- two more conjuncts, asked only where the object row carries `dignity`: the conferee holds a live
  `oblige` to the exercised seat (`gate.py::sworn_to`: homage before investiture, and the oath is the
  swearer's own act, AX-1); and the payload's `cites` names a deed claim about the conferee in the
  conferrer's own ledger (`own_ledger` of `to`, the form `survey` and `tell` use). A computed act
  binds `to` from the persons the conferrer holds deed claims about and ranks them by his own
  `deeds_judged`, which replaces the positional conferee for these rows.
- the draw, as audit §7.0: `contests: a standing`, `counterparty: to`. Pool `faculty(w, p, "confer")`.
  Obstacle in the SC form: `difficulty` by the rung kind of the seat's rung; `opposition` the mean
  regard for the conferee among the live holders of seats of the row's body (an empty body: none);
  `favourable` one step each for a `cites` claim held firsthand, for the conferee's regard for the
  conferrer above zero, and for the conferee's highest live dignity; `standard` raised at an open
  floor.
- by degree: Overwhelming and Success open the `hold` and deposit the cited deed, as a told claim
  from the conferrer, on every person the act's witness channel reaches (full confidence on
  Overwhelming, the conferrer's own on Success); Partial opens it with
  `Term(tick + provisional_term·season)` (fixture, shipped 4, swept 2 / 4 / 8); Failure opens nothing,
  emits `conferral.declined`, and closes nothing.

New emitted kind: `conferral.declined` (`write_matrix.yaml` needs no row: nothing is written).

## Gate (execution artifacts)

1. *Build.* The probe of audit E-1 re-run: persons' mean `legitimacy(p, holder, seat)` for the three
   founding holders is ordered King > Hafenmark > Varfell at the shipped fixtures; at
   `presumption_gain: 0` it reads 0.720, 0.000, 0.000 again (the control).
2. *Draw.* 200 seeds, one hand-placed `confer` of `off_dignity_3a` by the King on a sworn person with
   one firsthand deed: all four bands occur; no band exceeds 0.9; with `procedure_draws: off` every
   seed opens the hold (the control).
3. *Reach.* Realm, seeds 0 to 9, eight seasons: the count of `tenure.opened` on dignity rows and of
   `conferral.declined`, reported, with the cited deed among the conferee's told claims in at least
   one other person's ledger after an opening. A zero count is a finding against reach (F-FA-02's
   cause b, the question slot), not against this mechanism, and is reported as such.

## Falsifier

Reverse the three `order` values: gate 1's ordering reverses. Delete the `cites` conjunct: a seeded
conferral names a person the conferrer holds no deed of. Set `founding_confidence` flat: the three
presumptions are equal. If any of the three plants leaves its reading unmoved, the term is not read.

## NERS

N: cut the Roll and NPC-008's custody has no object; cut the claims and the ducal houses read zero;
cut `dignity` and the Imperial Court stays seatless. Holds top-down, bottom-up (a petitioner consults
the Roll), laterally (two houses compared by one formula). R: the conferrer chooses whom to honour and
is bound to pay (B); complete at the extremes (no deed known: no candidate forms; a seat taken by
force reads no presumption). S: `deed_term` and `reception`'s confidence weighting; no new scoring.
E, against that: one section, one key, one record kind, three fixtures.

## Cost class

Small build. Declared movers: the build hash (the Roll, the claims, six seats); any run in which a
`confer` resolves.
