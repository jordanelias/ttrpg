# WR · What the provided arcs need from the world, the clocks and the practitioner

Reconciled: 2026-11-12, U5d closure — folded **A-47** (a threshold may open a mandatory scene, never decide it; against the register's recommendation) and **A-15**. Edit 1 ("a private tally becomes a question") is rewritten in one respect: when the tally reaches its count the question is **mandatory** (it is placed first on the person's slate and cannot be declined for another; for the player it heads A-48's list and must be answered), and its outcome is the drawn act the scene resolves; the crossing itself still writes nothing. Edit 4's restatements of the "forced by threshold" and "automatic clock" arcs read "the threshold opens a scene" for all of them (A-47's class is the register's 27 threshold-closed or -forced arcs; the audit's 19 `forced_by_threshold` cases are its forced subset, C3-N12, `[ASSUMPTION: the 19 are a subset of the 27 — basis: `forced_by_threshold` is one of the two kinds the 27 count]`). Edit 2 (a body that mends when fed) lands after `U5d_WR_owed_edits.md` §3. ARC-02 (a state change with no actor) is now reachable through natural death (A-15).

Reconciled: 2026-11-12, wave 3 (W3-3) — C3-N12 (the two counts named in the head above); edit 1's body carries the head's mandatory question (A-47) through `Question.mandatory`, the field `12_ARCS_arcs_as_staged_goals.md` adds (R3 §1: a season-local value, cross-lane dependency); tier and batch added (R3 7b-0; U3 B12). R3 §2 found the body's "Nothing fires … what he does with it is his (L5)" in agreement with the head; it is kept.

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), after `09_WR_B_weather_with_memory_and_the_year.md` and before `07_SE_kernel_repairs.md` (U3 §1 item 13); edit 2 after `U5d_WR_owed_edits.md` §3 (same batch, per the head).
Depends on: `12_ARCS_arcs_as_staged_goals.md` (B10, `Question.mandatory`); `U5d_WR_owed_edits.md` §3 (B12, edit 2).

Carries §13 of `audits/09_WR_audit.md` (the adjudication table is there; this file holds the edits) and
finding F-WR-08. Evidence ids (E-nn) are that file's §12.

## What it changes in `engine/season/` at runtime

Edit 1 (a private tally becomes a question) and edit 2 (a body that mends when fed) are declared hash
movers, each shipped at a control that reproduces the base hash. Edits 3 and 4 change the harness and the
corpus overlay only.

## The problem

Of the 143 provided cases, 79 `core` needs fall on four mechanisms this lane owns or borders (the tagging
run is E-17): a quantity that counts up and then forces something (COUNTER, the largest group), an ambient
world quantity that decays in bands (SUBSTRATE), a working that costs its practitioner (THREAD), and a
body that is hurt and recovers (BODY). The corpus instrument cannot score any ending: `corpus_run` prints
`ARC (97 cases) ** ENDS = NOT-COMPUTABLE **` (E-15).

Three of the four are stated in the cases in the vocabulary of the retired design (a stored scalar that
moves by itself and fires an outcome at a threshold). Layer 1 forbids exactly that (L3 clause 2: no
cross-holder tally; L5: a crossing may never produce an outcome; `loop/census.py`: no clock generates
anything; M16's fourth motion not taken, ED-IN-0301), and the arc-reachability adjudication already found
the stories survive the loss of the mechanism in 64 of 74 scored arcs
(`proposals/2026-08-30-arc-reachability/04_SYNTHESIS.md` §1). So the adjudication is mostly restatement:
say each need in the form the engine can lawfully carry, then name the one missing piece.

## The resolution, decided

| need as written | lawful form | carrier | missing |
|---|---|---|---|
| a private counter held by one actor, fed by unrelated triggers, that forces an ultimatum at its ceiling (ARC-31, -32, -34, -47, NSC-05, NSC-08, EMG-C1) | what one person has come to hold: claims of named kinds in his own ledger; at the count, a question he answers | L3 clause 1 permits it (`world_q.single_holder_counter`, `:147-172`); the thrust ladder already evaluates stage predicates over a person's own ledger (`current_stage`, `:2900`) | the closed `axis` registry `single_holder_counter` raises `Unspecified` for; and something that turns "the tally is full" into a question (edit 1) |
| an institution's standing rises by itself every period (ARC-46, -50, EMG-C2, NSC-09) | a fold of the log over the institution's members' acts | CR-89 (B10-17b; ED-IN-0339 to 0345): "the clocks as folds of the log" | FA/IN's build; not this lane's |
| a ceiling eliminates a faction with nobody declaring it (ARC-52) | an ending the season reports (`endings_reached`) once persons' acts have made it true | `rosters.yaml: endings` | a row; Jordan's content |
| an ambient world quantity decays on a schedule, in bands, raising difficulty (ARC-05, -27, -43, -48, EMG-C3, ARC-41, EMG-X8) | Site fabric wearing (`condition.worn`), bands as `band_floors`, a crossing closing uses (`closed_uses`), spreading by the lattice coupling | `loop/matter.py::_lattice_strain`; `world_q.closed_uses` | the source and the live weight (`09_WR_world_motion.md` edit 1) |
| a working costs the practitioner a persistent personal resource; sensitivity gates perception (NPC-002, -004, -005, -075, ARC-51, EMG-X7, SCN-LOOP-A) | `Person.coherence` moved by a working's outcome; `thread_sensitivity` as a scalar-threshold cell | `(Person, coherence)` matrix row (unproduced); `thread_read`'s typed cell | B10-15, on `09_WR_threadwork_module.md` |
| an injury persists until a recovery action is taken; no passive recovery (ARC-53, SCN-07) | `Person.body` falls and only `tend` raises it | built and executed: `body.tended` 37 at seed 0 (E-07) | nothing |
| a fed population recovers (the positive half of hunger; r2 `MW-L+1`) | a signed body step at MATTER | `loop/matter.py`'s body pass | the rising half (edit 2; H-211) |

## The edits

### Edit 1 · a private tally raises a question (`rosters.yaml`, `queries/world_q.py`)

Add `rosters.yaml: tally_axes`, the closed registry L3 clause 1 asks for, shipped **empty** (the control:
`questions_for` is byte-identical):

```yaml
  tally_axes:
    source: "L3 clause 1; `queries/world_q.py::single_holder_counter` (which raises Unspecified without it)"
    members: {}      # <axis id>: {counts: [<Event kind>, ...], about: <person | office | rung>, at: <int>}
```

`world_q.tally_reached(w, p) -> tuple` returns, for each axis whose `counts` kinds number at least `at`
among the claims in `p`'s **own** ledger about one referent, that referent. `questions_for` appends it to
the `added` splice as a classed referent (the `vacancies` shape: a standing occasion, no new source),
stamped `mandatory` (`Question.mandatory`, `12_ARCS_arcs_as_staged_goals.md`; A-47: placed first on his
slate, not declinable for another, heading A-48's list for the player), so the rows that declare that class
form on it and the person chooses among them; the scene's outcome is the drawn act he takes. Nothing fires: a full tally is an
occasion, and what he does with it is his (L5). "Irreversible" in the cases (ARC-47, NSC-08) is restated:
a tally is what he still holds; claims decay and evict, so a grudge nobody refreshes fades. That is the
design's replacement for a monotone counter and is not softened.

`single_holder_counter` stops being probe-only and is the body `tally_reached` composes on.

### Edit 2 · a fed body mends (`loop/matter.py`, the body pass; `modules/settlements/subsist.py`)

r2 §A.4's signed step, `body_step × (2·ration − 1)`, replaces the falling half now built; `_crossings`
gains an upward predicate (`before < floor <= after`) for the body row only, so recovery is audible. A new
fixture `body_mend` ships `False` (the control: no rise, no upward crossing; MW-11's own control: the count
of downward site crossings is unchanged with the predicate added). This is CP-T10-04's ground; it is
written here because three provided needs (SCN-06, SCN-LOOP-C, NPC-075's burden) and H-211 meet on it.

### Edit 3 · the corpus stops planting endings from prose (`harness/corpus_run.py::build_at`)

Delete the block at `:656-660` that plants `d_forced` for a `forced_by_threshold` case. What it plants (a
holderless Date and a docket item whose matter is a Proposition) fires, forms no slot, can be determined by
nobody and lapses. Replace it with nothing; the case's overlay may author a `tally_axes` row once edit 1
lands, which is the lawful form of "a crossing forces the moment". `test_season_shape.py:4639-4696`, which
asserts the planted date fires, is deleted with the block (it tests the plant, not a behaviour of the
game). `ENDINGS_CLASSIFIED.yaml` stays as the classification it says it is; its path in
`corpus_run.py:36,79` and in H-176 is corrected to `engine/season/ENDINGS_CLASSIFIED.yaml`.

### Edit 4 · restated needs in the overlay (`engine/season/cases/exercises/`)

For the cases in §13's "wrongly stated" rows, the `exercises:` overlay binds the need (by `need_sha`) to the
token of its lawful form: `H-235` for the substrate needs, `H-211` for recovery, the new `tally_axes` axis
for a private counter, `CR-89`'s register row when it lands for an institutional clock. No case file is
edited: the case states what must be simulated; the overlay says by what.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.corpus_run          # ARC lane: fewer RUNS-UNDECLARED; no `d_forced`
python -m pytest engine/season/tests/test_cl_thrust_b31_current_stage.py -q   # the ledger-predicate precedent, unchanged
PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0        # hashes EQUAL at the empty registry and `body_mend` False
```

and one new falsifier per edit: (1) a person holding three claims of an authored axis's kinds about one
seat-holder has that person among his classed referents, and with two has not; a second person holding
none is offered nothing; (2) a cohort fed full rations from below a body floor crosses it upward and the
crossing is anchored on it, and at `body_mend` False does not.

## The falsifier

Edit 1 fails if the referent appears for a person who does not hold the claims (a world read leaked into a
person-side tally), or if anything happens at the count with no act. Edit 2 fails if a fed body rises past
its ceiling (`Person.body_ceiling`, CP-T03-07) or a downward crossing count moves.

## NERS reading

- **N.** Edit 1 is the one carrier seven core needs share; without it they have no lawful form at all.
  Bottom-up it is one person's memory; top-down it is the arc's "forced moment"; laterally it reuses the
  stamp and the ledger. Edit 2 is narrower: it holds for cohorts only (individuals do not eat, ED-IN-0255).
- **R.** Characterful by construction: two persons with different ledgers reach the tally at different
  times or never, and each answers it by his own convictions. The no-player half: a readiness that builds
  quietly and then becomes an act is the commonest shape in the corpus's THRESHOLD class.
- **S.** No new question source, no new Event kind, no counter stored. One methodology for "something has
  built up": a band over what is held, as `standing_crossed` already is.
- **E, last.** One roster, one Query, one splice term, against the largest single group of core needs in
  the corpus. High. Edit 2: one fixture and a predicate for the positive loop the body lacks. Medium.

## Cost class

Edit 1: small build; the rows' content is design-first per arc. Edit 2: small build, on CP-T10-04's order.
Edits 3, 4: edit. Tier: `sonnet` (R3 7b-0).
