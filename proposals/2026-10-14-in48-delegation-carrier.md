# IN-48: the delegation carrier (a seat exercised by someone who does not hold it)

## Status: PROPOSED (2026-10-14) · HELD: built at `40926a95` and REVERTED because it contradicts ratified Layer 1 (§9) · reference under `CLAUDE.md` §0.05
## Position: IN-48 (H-108's delegation half), `workplans/valoria_master_workplan_v9_part5.md` `### IN-48` · Lane: IN (FA SE) · IDs: none allocated
## Measured at HEAD `46c08d9c` (B-J boundary 1; IN-40 landed `3f320093`). A path with no top-level directory is under `engine/season/`.
## Revised 2026-10-14 for an independent critic's findings. The orchestrator took the decisions marked ORCH (ladder step 5), each [ASSUMPTION; medium; Jordan to correct], with its revert named where it is applied.

The brief is the IN-48 entry: INSTRUCTION, DEPS, EXIT and FALSIFIER. This document does not restate it.

---

## 0. Verdict

> **HELD (B-J close, 2026-10-14): sections 0 to 8 below describe a build that was reverted because it contradicts ratified Layer 1. Read §9 first; nothing here is live.**

**The carrier is a new `tenure_kinds` member, `delegate : Person → Office`.** The delegate owns it and
its object is the seat. The seat's sitting HOLDER opens it through that same seat: a hand-built
`confer` whose `office` is its own `via`, naming the delegate on `to`. The write gate admits it under
one new basis, `delegation`.

The edge carries the same grant payload a `hold` carries, stamped by the one writer
(`World._grant_remit`). That lets `seat_hold` return it as a second way to sit in a seat, **but only
while the seat has a live `hold`** (ORCH, §2.5). The fold's remit branch, the `may_*` predicates
(except `may_determine`, §2.6) and the person-side seat readers then admit the delegate's acts `via`
that seat.

`purview_reaches` never reads a `delegate` edge, because `sworn_to` filters on `kind == "oblige"`
(`state/gate.py:393`). So the delegation can never be read as vassalage, and no marker is needed to
keep the two apart.

The edge ends in four ways:
- its `term` matures at MATTER (`T-n`; the term branch is already kind-general);
- the delegate's own `release` (`T-m`, a pure closure);
- the holder's hand-built `revoke` naming the seat itself and, on `to`, the delegate (the `delegation`
  basis's closing arm);
- the delegate being seated in that same seat by a `confer` (the `conferral` basis's closing arm, §2.1).

None of these touches the principal's `hold`. No computed decision opens a delegation (ORCH, §2.7).

---

## 1. What kills the other candidates

### (1) `oblige` plus a discriminator: killed three times, once by a ruling

- **The delegate would write his own delegation.** An `oblige` is opened by its owner under `T-m`.
  `_eff_oblige` mints `Tenure(..., a.actor, seat, "oblige", ...)` with `via=None`
  (`loop/effects_governance.py:367-370`), and `T-m` admits an owner's own opening
  (`state/gate.py:944-948`). A delegation carried on `oblige` is self-grantable unless `T-m` gets a
  further carve-out keyed on the marker.
- **The principal could not end it. Jordan ruled this.** If the delegate owns the edge, the principal
  ending it is an obligee-side closer. D-5 refused that for `oblige`: *"no creditor verb, no `call_in`,
  no obligee-side closer on an obligation exists or will"* (quoted at `state/gate.py:988-990`;
  `verb_table.yaml:838`). SC-03a kept `determination` from closing an `oblige` for the same reason
  (`state/gate.py:836-837`).
- **No discriminator already in the data tells the two apart.**
  - Direction: both are `Person → Office`.
  - Term: both may carry one.
  - Who opened it: not on the edge. `Tenure.conferrer` was deleted as an `ID-2` second home
    (`state/carriers.py:84-93`), and no gate basis reads the log.

  So a discriminator would be a second payload marker beside `DETERMINED_BY`
  (`state/carriers.py:70-72`, `Tenure.imposed` `:112-115`). That is the shape divergence the IN-48
  entry names.
- **Precedent.** SC-03a made `detain` and `ban` kinds, *"which is why they are kinds and not an
  `oblige` (#453 §8.3)"* (`rosters.yaml:115-123`), because an `oblige`'s holder can end it himself.

### (3) A co-hold, a second live `hold` with a narrowed grant: killed by the cardinality and by its readers

I measured this. `grep -rn 'kind == "hold"\|"hold" and\|kind != "hold"' engine/season --include=*.py`,
tests excluded, returns **50 matching lines in 15 files**, comments included. **6 code sites assume one
live hold per seat**, or act on every holder at once:

| reader | what a co-hold does to it |
|---|---|
| `queries/world_q.py:152-158` `hold_force` | **RAISES** `Forbidden` on two live holds. It is S15's *"`hold` cardinality is 1 PER OBJECT"*, `holonic §15`. Its live caller `loop/witness.py:411` asks it of Records, so on seats the raise is reachable only through probes. The law is the same either way. |
| `queries/world_q.py:1171` `leaders` | builds `{object: subject}`, so one holder is silently dropped |
| `loop/predicates.py:154` `_req_confer` | `holder = next(...)`, which reads the first holder only |
| `loop/effects_governance.py:107` `_eff_confer` | closes every live hold |
| `loop/effects_governance.py:191` `_eff_establish` | re-stamps every live hold with the full remit, **erasing a narrowed grant** |
| `loop/effects_governance.py:274` `_eff_revoke` | closes every live hold, so dismissing the delegate unseats the principal (**the plan's FALSIFIER**) |

Two more facts finish it:
- **The principal could not open it.** `may_fill` refuses `via == off` (`state/gate.py:575`).
- **It contradicts the EXIT**, which asks for *"a person holding no `hold`"*.

### (4) Other rostered kinds: none has the right ends

`holonic_ARCHITECTURE.md:541-544` gives the ends:
- `succeed : Rung → Person` (heirship);
- `tie` and `knot` : `Person ↔ Person`.

None of them ends at an Office. An `oblige : Person → Person` to the principal names no seat, and it is
the D-5 closer problem again.

### (2) A new kind: chosen. What it costs, counted

| cost | where | what it is |
|---|---|---|
| roster member | `rosters.yaml:124` `tenure_kinds.values` (`open: true`) | `+ delegate`, with a note on the `detain`/`ban` model (`:115-123`) |
| constants | `data/rosters.py:461` beside `DETAIN_KIND` | `DELEGATE_KIND = "delegate"`, plus `SEAT_KINDS = frozenset({"hold", DELEGATE_KIND})`: *the kinds through which a person sits in a seat*. One owner; its readers are listed in §3. |
| the `release` domain | `RELEASABLE_KINDS` is derived (`data/rosters.py:473`) | `verb_table.yaml:828` `release.domain += delegate`, or loader invariant 6 fails the load (`data/verbs.py:954-961`) |
| opener derivation | `data/verbs.py` `_derive_openers_from_effects` reads `kind` only as a string Constant at a `Tenure(...)` call | `_eff_confer`'s construction spells `"delegate"` literally |
| `tenure_write_basis` | `state/gate.py:754-1011` | one new basis `delegation`; `seat` widened to `SEAT_KINDS`; `conferral` gains one closing arm (§2.1) |
| write matrix | rows are per carrier field | **none**. `confer` declares `writes: [Tenure.until, Tenure.since, Tenure.term]` (`verb_table.yaml:176`); `revoke` declares `Tenure.until` |
| a verb | none | reuses `confer` and `revoke` |
| shape pins | `tests/test_season_shape.py` | none expected: no new loader `SystemExit`, and `len(VERB_TABLE)` does not move. The `tenure_kinds` readers there are a roster-is-data test (`:2517`, `:2539`) and a PRINTED opener-less list (`:3608-3610`). |
| hash | §4 | no field changes |

---

## 2. The design, requirement by requirement

### 2.1 Who opens it, and under what gate basis

**The opener is `confer` with `office == via`.** The actor exercises seat `S`, names `S` itself as the
office and names the delegate on `to`. Today that act shape is refused everywhere: `_req_confer` asks
`may_fill` (`loop/predicates.py:136`), which refuses `via == off.id` (`state/gate.py:575`), and so does
the gate's `conferral` basis (`:1009`). *"Conferred the regency on his brother"* is the ordinary idiom
(ED-IN-0179). The shape mirrors `renewal`'s reflexive-on-the-seat rule (`state/gate.py:582-610`).

**New predicate `may_delegate(w, actor, via, off, delegate)`** in `state/gate.py`, beside `may_renew`.
Three conjuncts:
1. `via == off.id`.
2. `seat_hold(w, actor, via)` returns a Tenure **of kind `hold`**, so a delegate cannot delegate
   further or dismiss a co-delegate.
3. `delegate` is a person other than the actor.

Conditions that matter only at OPENING stay in `_req_confer`, so that a CLOSURE is never refused
because the delegate's standing changed afterwards.

**The `delegation` basis** admits an OPENING of a `delegate` edge, judged whole as `conferral` and
`determination` are (`:807-809`, `:840-842`), and a PURE CLOSURE of one (`_closes`, `:736`). Each needs
`may_delegate(w, actor, via, seat, t.subject)`. It cannot grade, re-term or re-grant.

**The `conferral` basis gains one closing arm (ORCH, point 3).** When a `confer` seats a person in `S`,
`_eff_confer` also closes that conferee's own live `delegate` edge on `S`, naming it `tenure.closed`.
Otherwise he would be left holding a delegation on a seat he now holds. The gate admits that closure
as `CONFERRAL` when two things are true:
- `may_fill(w, actor, via, seat)` holds;
- the edge's owner holds a live `hold` on `seat` in the world the write leaves.

This is judged on one change, as the module's *"JUDGED ON THE WORLD THE WRITE LEAVES"* rule says
(`:858-864`), so it needs no two-pass licence. A self-conferral reaches `T-m` first (`actor == owner`,
a pure closure).

**A delegate cannot write his own delegation.** Widen `seat = ... if t.kind == "hold"`
(`state/gate.py:906`) to `t.kind in SEAT_KINDS`. `T-m`'s existing guard
`not (seat is not None and not closed)` (`:946`) then refuses an owner opening his own `delegate`
edge, as it refuses a self-opened seat-`hold` (`:907-918`), and still admits his `release`.

**Placement.** After `if seat is None: return None` (`:1005`), add a `DELEGATE_KIND` block: the
`delegation` arms, then the `conferral` closing arm. `T_O` and `CONFERRAL` below it stay `hold`-only.

**The writes.**
- `_eff_confer`, when `office == a.via`, builds
  `Tenure(H(w.world_seed, w.tick, to, f"delegate:{obj}:{a.id}"), to, obj, "delegate", w.tick, term=_declared_term(w, a))`.
  The id salt follows `_eff_oblige` (`:368`), and `_declared_term` is reused (`:37-53`). The branch
  computes no `closed` list, so it cannot close a hold (`:107`, `:116-117`).
- On the ordinary hold branch, `closed` also takes the conferee's live `delegate` edges on `obj`.
- `_req_confer` takes the delegation branch **before** `has_conferral_basis` (`:126`), because a
  delegation does not fill the seat. It admits on four tests:
  - `to` is a living person (`:133-135`);
  - `to` is not banned (`_eff_confer`'s `:105` rule, asked early);
  - `to` holds no live `hold` and no live `delegate` on `office`;
  - `may_delegate` holds.

### 2.2 The remit: the seat's full grant, or a declared subset bounded at opening

The one writer stamps the grant. `add_tenure`'s `if t.kind == "hold": ... self._grant_remit(t)`
(`state/world.py:326-328`) becomes `if t.kind in SEAT_KINDS: self._grant_remit(t)`. A `delegate` edge
then carries `{"remit_acts", "seat_rung"}`, the shape `granted_acts` and `seat_rung` already read
(`state/carriers.py:117`, `:160`).

**Ends checked (ORCH, point 9).** `add_tenure` refuses a `delegate` edge that is not `Person → Office`,
using `class_of` and the `_refuse_bad_hold` pattern (`state/world.py:580-615`), so the EXIT's
build-placed edge is checked.

**Subset (A1).** [ASSUMPTION; medium; Jordan to correct; revert: drop `within` and the act key, so
every delegation carries the full grant.] A `confer` may declare `acts` in its payload, as it declares
`term` (`TERM_KEY`, `loop/effects_governance.py:30-34`). `perform()` then calls
`w._grant_remit(nt, force=True, within=acts)` after `add_tenure`. `_grant_remit` stamps
`tuple(a for a in off.remit_acts if a in within)`, so it stays the key's only writer. The source is
`cases/chain/NPC3.yaml:83`.

**The bound holds at opening only (ORCH, point 8).** The subset is intersected with the office's LIVE
`remit_acts` at the moment the edge opens. `_eff_establish` re-stamps `hold`s only (`:191`). So a later
`establish` that narrows the seat's remit leaves sitting delegates with acts the seat no longer
grants, until their edge ends. That is the same snapshot semantics a `hold` had before `13f`. Nothing
admits a `{"payload"}` change on a `delegate` edge.

### 2.3 Purview: the seat's, and never over the delegate's own ground

There is no edit to `purview_reaches` (`state/gate.py:297-372`). Every `may_*` asks it of
`w.offices[via]`. That is `04:350` at this HEAD (the brief cites `:332`): *"purview is asked of the
seat exercised, not the actor ... A regent has the seat's purview"*.

`sworn_to` returns only `oblige` edges (`:393`), so a delegate who holds seat `B` brings none of `B`'s
ground under the delegated seat `A`. Only a separate live `oblige` to `A` does that, and that is
vassalage, a second fact.

### 2.4 What ends it, and the refusal after

| closer | basis | edit |
|---|---|---|
| `term` matures at MATTER | `T-n` (`state/gate.py:971-973`) | none (`loop/matter.py:229-236`) |
| the delegate's `release` | `T-m`, pure closure | `release.domain` only |
| the holder's `revoke`, `office == via`, `to` = delegate | `delegation`, closing arm | `_req_revoke` and `_eff_revoke` branches |
| the delegate seated in the same seat by `confer` | `conferral`, closing arm (§2.1) | `_eff_confer`'s `closed` |

**The `revoke` arm (ORCH, point 5).**
- **The delegate is named on `to`.** The act's payload carries `{"office": <the seat>, "to": <the delegate>}`.
  `_req_revoke` reads `office` from the payload today (`loop/predicates.py:427`), and the branch reads
  `to` the same way.
- **It is hand-built only.** The `revoke` row has no `counterparty:` column, so no computed act carries
  a `to`. The EXIT's revoke is therefore hand-built too.
- **Branch condition: `office == a.via` AND `to` present.** A `revoke` naming its own `via` with no
  `to` takes the existing path, and `may_revoke` refuses it as today, because a seat is never on the
  rung above itself (`seated_on_the_rung_above_structure`, `:422-428`). Behaviour is unchanged.
- **What it closes:** the live `delegate` edges `(to → office)` only, never a `hold`.

**Release (ORCH, point 3, ACCEPTED).** `_eff_release` closes every releasable edge the actor owns on
the named subject (`loop/effects_governance.py:247-250`). A delegate who has also sworn an `oblige` to
the same seat therefore ends both in one `release`: leaving the seat's service ends both.

**The refusal after.** `seat_hold` reads only live edges. So the fold's remit branch
(`loop/resolve.py:118-120`) and every `may_*` refuse the same act once the edge is closed.

### 2.5 The principal's hold closes, or the principal dies: the delegation goes DORMANT (ORCH, point 2)

[ASSUMPTION; medium; Jordan to correct; revert: the delegation is the seat's and stays live and
exercisable through a vacancy, a permanent regent.]

**`seat_hold` returns a `delegate` edge only if some live `hold` on `via` exists.** If the actor has a
hold himself, the hold is preferred. There is no cascade and no new field. The edge stays live; it
is simply not read while the seat is vacant.
- **Death.** `World.remove_person` is the one death cascade (`state/world.py:617`). It closes every live
  edge naming the person; the gate admits it under the `cascade` basis (`state/gate.py:949-950`). The
  principal's `hold` closes. The `delegate` edge names neither him nor anything gone, so it stays live
  and becomes dormant.
- **Resignation or revocation.** Closing the principal's `hold` has the same effect: the delegation is
  dormant.
- **A later holder** revives it. Through `may_delegate`'s `hold` conjunct, that holder can also
  `revoke` it.
- **The null-conferral consequence.**
  - `build_realm(0)` at this HEAD has 30 offices. 7 grant `confer`, and 5 of those 7 declare
    `conferral: None`.
  - In `offices.yaml` the figures are 29 rows, 6 granting `confer`, 4 of them null.
  - `has_conferral_basis` refuses a `confer` onto a seat with no basis (`loop/predicates.py:126`). So
    a vacated null-conferral seat cannot be refilled by `confer`, and a delegation on it stays dormant
    until its term ends it, the delegate releases it, or a basis is declared.

### 2.6 `seat_hold`, the one owner, and who does NOT inherit the delegate

`seat_hold` returns:
- the actor's live `hold` on `via`, if he has one;
- otherwise his live `delegate` edge on `via`, but only if some live `hold` on `via` exists;
- otherwise nothing.

The docstring's *"A `hold` AND NOTHING ELSE SEATS A PERSON TODAY"* (`:281-286`) is rewritten.

Readers that inherit the delegate:
- `may_revoke` `:552`, `may_fill` `:575`, `may_renew` `:610`, `may_warrant` `:711`;
- the fold's remit branch, `loop/resolve.py:118`.

**`may_determine` does NOT inherit it (ORCH, point 4; A3 reversed).**
- Bench membership is holders. `judging_set` keeps `t.kind != "hold"` (`queries/world_q.py:412`), so a
  delegate adds no quorum.
- `may_determine` (`state/gate.py:686`) gains `t.kind == "hold"` on its `seat_hold` result, so the gate
  and the bench still agree (`queries/world_q.py:406-407`).
- **A delegate therefore cannot `determine`.** That is a named residue.

[ASSUMPTION; medium; Jordan to correct; revert: both read `SEAT_KINDS`, and a delegate sits in
judgment.]

### 2.7 Scope, and no computed opener (ORCH, points 6 and 7)

**Named residues, for H-108's cite when it closes. These are not new apparatus.**
- **Only a seat whose remit grants `confer` can delegate.** That is 7 of 30 offices in
  `build_realm(0)`, and 6 of the 29 rows in `offices.yaml`. ORCH's brief says 5 of 29, which I did not
  reproduce; the difference is unexplained.
- **No outside seat installs a regent or a puppet.** `may_delegate`'s conjunct 1 (`via == off`) means a
  delegation comes only from the seat's own holder. A puppet installed from outside stays expressible
  only as a holder seated by `confer` (or as vassalage, IN-40).
- **With the full grant, a delegate receives `confer` and `revoke` too.** He can fill or strip OTHER
  seats in the delegated seat's purview, but he cannot delegate further or dismiss a co-delegate
  (conjunct 2), and he cannot seat himself in the seat he exercises (`may_fill` refuses `via == off`).

**DECLINE: no computed decision opens a delegation.**
- **Why it is needed.** `opening_set` can form a computed `confer` on a seat the actor was told of,
  including one he holds (`queries/world_q.py:1608-1612`; H-207, C4). With that seat as `via`, the act
  is `office == via`, which after the build would open a delegation.
- **The edit.** In `decision/options.py::opening_set`'s per-seat loop (`:241-247`), a `confer`
  Candidate whose subject is the seat it would be exercised through is not formed.
- **The test** asserts that no computed `confer` reaches `_req_confer` with `office == via`.

Revert: allow it once a person-side reason to delegate exists. The EXIT's seeded season places its
edge at build.

---

## 3. EDITS for the build

`state/gate.py`
- `seat_hold`: §2.5 and §2.6.
- New `may_delegate`.
- New `DELEGATION` basis name.
- `may_determine`: the `hold` conjunct (§2.6).
- `tenure_write_basis`:
  - `seat` over `SEAT_KINDS` (`:906`);
  - the `DELEGATE_KIND` block after `:1005`, holding the `delegation` arms and the `conferral` closing
    arm;
  - its docstring's basis list.
- `refuse_unauthored`'s count prose.
- `not_yours`'s `needs=` message (`:1085-1098`), which lists every basis: add `delegation` and the
  `conferral` closing arm.

`state/world.py`
- `add_tenure`: grant for `SEAT_KINDS` (`:326-328`), and the `delegate` ends check (§2.2).
- `_grant_remit(t, force=False, within=None)`.

`data/rosters.py`
- `DELEGATE_KIND` and `SEAT_KINDS`, checked as `<= TENURE_KINDS` on the `RESTRAINT_KINDS` precedent
  (`:463-469`).

`rosters.yaml`
- `tenure_kinds.values += delegate`, and a note.

`verb_table.yaml`
- `release.domain += delegate`.
- Notes on the `confer` and `revoke` rows: the `office == via` branches, and `revoke`'s hand-built
  `to`.

`loop/effects_governance.py`
- `_eff_confer`: the delegation branch with the literal `"delegate"`, and the conferee's `delegate`
  edges added to `closed`.
- `_eff_revoke`: the delegation branch.
- `ACTS_KEY = "acts"`.

`loop/predicates.py`
- `_req_confer` and `_req_revoke` branches.

`decision/options.py`
- `_granting_holds` (`:455`) and the `seat_rung` reader (`:615-616`) read `SEAT_KINDS`.
- The `opening_set` DECLINE (§2.7).

`queries/world_q.py`
- The vacancies seat list (`:1614`) reads `SEAT_KINDS`.
- `reach` (`:554`, `:587`) and `governors_of` (`:594`, `:621`) read `SEAT_KINDS` (A4). [ASSUMPTION;
  medium; Jordan to correct; revert: `hold`-only.] Their `hold` test should go through `seat_hold`'s
  dormancy rule, so that a dormant delegate gains nothing.

`epistemic.py`
- `_hold_tenure_ends` (`:179`) reads `SEAT_KINDS`, so a delegation's receipt names both ends.

`hole_register.yaml`
- H-108 closed when the EXIT is observed, with §2.6's and §2.7's residues in its cite.

**Not edited, with the reason a delegate is correctly excluded:**
- `state/gate.py:372`, the oblige clause's swearer seats. A swearer brings the ground of the seats he
  HOLDS. A delegation is not his ground; counting it would let a vassal bring a delegated seat's
  ground to his lord.
- `loop/predicates.py:393`, `_req_oblige` clause 3 (*"the occupant is not his own seat's obligee"*). A
  delegate is not the occupant, and he may swear service to the seat he exercises (§2.4, release).
- `queries/faction_q.py:109`, a faction's `seats` and `holdings`. These are what the faction's members
  hold, and a delegation is not held.
- `queries/world_q.py:2089`, the `held_by` requires-stem. It asks custody (`hold`), not exercise.
- `epistemic.py:437`, `_ch_document_key`. A landholder witnesses changes to what he holds; a delegate
  holds nothing.
- `judging_set` (`queries/world_q.py:412`): §2.6.
- `purview_reaches` and `sworn_to`: §2.3.
- `state/carriers.py`: no field.
- `Query.budget` (`decision/budget.py:57`), A5. [ASSUMPTION; medium; revert: count `SEAT_KINDS`.]
- `world_q.leaders` (`:1171`).
- The harness readers (`harness/aperture.py:83`, `:195`, `harness/invariants.py:236`,
  `harness/governance_spine.py:227`).
- `decision/choose.py`: `via` comes from `seat_of` → `_granting_holds` (`decision/options.py:436-456`),
  and `choose.py:582` passes it through.

---

## 4. Hash

**No dataclass field changes, so there is no schema move** (`state/carriers.py:75-106`).

**`build_realm(0)` is unchanged with no delegation present.** No builder mints a `delegate` edge, and
every widened reader reads nothing new in a world holding none.

The precedent is SC-03a's two kinds. Its commit `c2f855d2` is an ancestor of HEAD (checked with
`git merge-base --is-ancestor`). Its message gives build hash `11989dcf` unchanged, and
`BASE_HASHES[0]` at `engine/season/tests/test_season_weather.py:64` still reads
`"11989dcf5e1c25afab556bf3f234a200"`.

**Outcomes:** a computed run can move only if a computed act reaches `_req_confer` or `_req_revoke`
with `office == via`. The DECLINE (§2.7) removes the `confer` path by construction, and the computed
`revoke` carries no `to`, so its behaviour is unchanged (§2.4).

### 4.1 The measurement

**My earlier count is withdrawn. It did not measure the space the new branch opens.** It wrapped
`may_fill`, but `_req_confer` refuses on `has_conferral_basis` (`loop/predicates.py:126`) before
`may_fill` (`:136`), and most confer-granting seats declare `conferral: None` (§2.5). Its "control",
`world_q.may_fill` from `vacancies`, can never be asked `office == via`. A zero there showed nothing.

**The instrument the build keeps:** count `office_named_by(a) == a.via` at the ENTRY of `_req_confer`,
before any clause, by wrapping `REQUIRES_PREDICATES["confer"]`. The test asserts the count was taken
(`assert checked >= N`, with `N` the number of `_req_confer` entries observed) and that the
`office == via` count is 0 under the DECLINE.

**Re-run at HEAD `46c08d9c`: the entry instrument, `build_realm` seeds 0 and 1, two seasons each.**

**`_req_confer` was entered 0 times in total, so the count observed nothing.** It is not evidence that
`office == via` is absent. Two caveats:
- `checked == 0` means I also could not show that the wrap is on the path the fold dispatches through.
  The fold reads `predicates.REQUIRES_PREDICATES` by module, `loop/predicates.py:18`.
- The earlier four-season run of seed 0 is the only sign of where `confer` starts: 5 `may_fill` calls
  from `_req_confer` and 4 `confer.refused`, all in season 4, and none in seasons 1-3.

**The build must therefore:**
- run the entry instrument for at least four seasons;
- assert `checked >= N` with `N > 0`, which is what shows the wrap is live;
- then assert `office == via` is 0 under the DECLINE.

A run that enters `_req_confer` zero times is a failed measurement, not a pass.

---

## 5. Falsifiers the build must add

All go in `engine/season/tests/test_in48_delegation.py`, each seen red before its clause is written.

1. **The plan's first falsifier.** A delegate's act `via` the seat is admitted, and after the edge
   closes it is refused, at the fold and at the gate. Three arms: term at MATTER, the delegate's
   `release`, and the holder's hand-built `revoke` with `to`.
2. **The plan's second falsifier.** A person with neither a `hold` nor a `delegate` on `S` names
   `via=S` and is refused. Control: the same person with the edge is admitted.
3. **The plan's third falsifier.** Opening a delegation leaves the principal's `hold` live with the same
   id, and the branch names no `tenure.closed`. `revoke` of a delegation closes no `hold`. A `revoke`
   with `office == via` and no `to` is refused exactly as before.
4. **No self-delegation.** A person opening his own `delegate` edge gets `NotYours`. The holder's write
   through the seat is admitted under `delegation`.
5. **No delegation by a delegate.** A delegate's `confer(office == via)` is refused, and so is his
   `revoke` of a co-delegate.
6. **Not vassalage.** A delegate holding `B` (ground outside `A`) is delegated on `A`, and
   `purview_reaches(A, B.rung)` is False. Control: his live `oblige` to `A` makes it True.
7. **Subset, bounded at opening.** `acts=[x]` grants `(x,)` ∩ the live remit. An act outside it is
   refused. A later `establish` narrowing the remit leaves the delegate's grant unchanged (point 8,
   pinned).
8. **Dormant (point 2).** The principal's `remove_person` closes his `hold`; the `delegate` edge stays
   live; `seat_hold` returns `None` for the delegate and his act is refused. A later `hold` on the seat
   revives it, and that holder's `revoke` closes it.
9. **Confer closes the conferee's delegation (point 3).** Seating the delegate in `S` closes his
   `delegate` edge on `S` under `conferral`. Control: his `delegate` edge on another seat stays live.
10. **No bench seat (point 4).** A delegate on a judging seat whose grant carries `determine` is
    absent from `judging_set`, and his `determine` is refused (`may_determine` False). Control: the
    holder is admitted.
11. **DECLINE (point 7).** In a seeded run the entry instrument counts `office_named_by(a) == a.via`
    at `_req_confer` as 0, with `checked >= N`. A hand-built Candidate list containing a told-of own
    seat shows `opening_set` forming no `confer` on it.
12. **Load and ends.** Removing `delegate` from `release.domain` fails the load. The derived opener set
    for `delegate` is `{"confer"}`. `add_tenure` refuses a `delegate` edge that is not
    `Person → Office`.
13. **The EXIT.** In a seeded season (`build_realm` plus one build-placed `delegate` edge), the
    delegate's computed act executes `via` the seat while the principal holds it, and after the
    holder's hand-built `revoke` the same computed act refuses. H-108 is closed on this test.

---

## 6. Assumptions and decisions

Each assumption is [medium; Jordan to correct] and marked inline:
- **A1. Subset by act declaration**, bounded at opening (§2.2). Revert: full grant only.
- **A2. Dormant while the seat is vacant** (§2.5, ORCH). Revert: a permanent regent.
- **A3. A delegate does not sit in judgment** (§2.6, ORCH). Revert: `SEAT_KINDS` in `judging_set` and
  `may_determine`.
- **A4. The seat's knowledge goes with its exercise** (§3). Revert: `reach` and `governors_of` stay
  `hold`-only.
- **A5. No budget bonus** (§3). Revert: `Query.budget` counts `SEAT_KINDS`.
- **ORCH, point 3:** `confer` closes the conferee's delegation, and `release` ends both an `oblige`
  and a `delegate` on one seat.
- **ORCH, point 7:** DECLINE (§2.7). Revert: allow when a reason to delegate exists.
- **The opener is `confer`/`revoke` with `office == via`, not a new `delegate` verb.** A new verb would
  cost a full row, a `remit_acts` member and an R-05 row that cannot execute without a decision source.

---

## 9. Held: the build contradicts ratified Layer 1 (B-J close, Phase 1, 2026-10-14)

The carrier was built at `40926a95`, all thirteen falsifiers passing, and reverted at the close before it
reached `main`. An independent cross-examiner and the compliance reviewer found, and the orchestrator
opened and confirmed, that this design contradicts text of `architecture/` (Layer 1, RATIFIED, ED-IN-0204,
binding as agent instruction) that §1 above never cites:
`architecture/meta/01_AXIOMS.md:1465-1467` (delegation is *conferring a seat*; a regency is a seat conferred
over the domain while the title stays put), `:1528-1530` (*"`tenure_kinds` does not move; no new carrier"*),
`:1544`, `:1569` (*"Delegation does not need a delegation mechanism. It needs the `conferral` basis to be
specified"*; the build's branch runs BEFORE `has_conferral_basis`), `:1640`; and
`architecture/meta/04_CODE_ARCHITECTURE.md:351` (*"delegation = `establish` → `confer` → `revoke`"*, MECHANICAL).
The plan's IN-48 entry assumed "an already-rostered `tenure_kinds` member" and said "attacked at the design";
that licenses testing the assumption, not amending Layer 1, and it has no `Layer-1 amendment` field. A
Layer-1 amendment is Jordan's (the `carry` precedent in `_part5` IN-45; SC-03a's `detain`/`ban` were named
by a ratified source, ED-IN-0288, and contradicted no Layer-1 sentence).

**What this changes.** §1's candidate list omitted Layer 1's own route: `establish` a second seat over the
domain, `confer` it, with IN-10's `Tenure.term` for "revoke at majority". The position returns to design on
THAT route first. Its open question, to be MEASURED: no rung-above revocation basis lets a principal revoke a
same-rung seat early. Only if that route fails on a named measurement is the `delegate` kind (this document)
put to Jordan, as one `needs_jordan` row with both options, and `architecture/` is then amended by him
(`_part8` IN-44 lists the Layer-1 edits owed, none by a batch).

**If this design is resumed, the Phase 1 findings that apply** (each was verified against the tree):
1. `rung_above_in_holdings` is judged on the DELEGATE's own holdings (`gate.py` `may_revoke` passes `actor`
   to the rule; `in_holdings` reads `t.subject == actor`), which also governs a delegate's `confer` that
   displaces an incumbent and the T-o clause. Fix: judge the principal (the occupying hold's subject).
2. A superior's displacing `confer` leaves the principal's third-party delegates live and revives them for
   the successor, who can end them only by a hand-built `revoke` naming `to` (the closing arm names only the
   conferee's own edge).
3. A seat that grants `confer` but not `revoke` can open a delegation and cannot dismiss it (`_eligible`
   runs first). Every shipped confer-granting seat also grants `revoke`.
4. A delegate's grant, full or declared, is the seat's remit at opening; `establish` re-stamps `hold`s only.
5. `reach` and `governors_of` read other people's tenures through the dormancy rule; their docstrings said
   they may not.
6. Test gaps to close: `delegate != actor` at the bare gate; "hold preferred" with the delegate listed
   BEFORE the hold; the EXIT test must judge execution with `harness/corpus_run.py::attribute` (refusal kinds
   include `<verb>.unauthorized`), with a same-world control; `reach`, `vacancies`, `treasury_of` and
   `_hold_tenure_ends` named by an assertion.
7. Stale text to correct with the build: `state/carriers.py` `granted_acts` ("every kind but `hold`"),
   `gate.py` ("nine now", `seat` "computed only for hold"), `epistemic.py:166-171, :229-247`,
   `verb_table.yaml` `confer` `writes_note`, `world_q.py` `reach` limb 4; `gate.py:289` cites `04:332` for
   `04:350`.
8. Measured on the build, `build_realm(0)`, four seasons, 1162 s: `_req_confer` entered 0, 0, 0, 5 times with
   0 own-seat; the same on the base (so the realm cannot tell the DECLINE from none); on the `_gov_world`
   fixture over four seasons, DECLINE off 39 entries with 11 own-seat and 2 delegations opened by computed
   decisions; DECLINE on 26 entries and 0 and 0. Build and one-season hashes were unchanged
   (`11989dcf5e1c25afab556bf3f234a200`, `0f8e0144220a3665d3286a9a54c39f3e`).
9. H-108 would have been graded `assumption`, not `measured` (four medium residues), and its "puppet rulers"
   unblock was not met (no outside seat installs a regent).
