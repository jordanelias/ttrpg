# IN-48: the delegation carrier (a seat exercised by someone who does not hold it)

## Status: PROPOSED (2026-10-14) · §1 to §8 stay HELD: built at `40926a95` and REVERTED because they contradict ratified Layer 1 (§9) · §10 (B21b.24, 2026-11-27) is the design on Layer 1's route that B21b.25 builds · all of it reference under `CLAUDE.md` §0.05
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

---

## 10. The design on Layer 1's route (B21b.24, 2026-11-27)

**Reference, not mechanism (`CLAUDE.md` §0.05).** This section resolves nothing at runtime. The mechanism is B21b.25's code
and its tests (`engine/season/tests/test_in48_delegation.py`); where this text and that code disagree, the code is read and
this text is wrong. It replaces nothing in §1 to §8, which stay held. Read at `43af80cdb` (B21b.23 on top). Line numbers
are this tree's, not v11's. A path with no top-level directory is under `engine/season/`.

**The design in one sentence.** A delegation is a second SEAT, held by an ordinary `hold`. It is founded or authored and
conferred, with IN-10's term where the conferring act or the seat's row declares one. It ends by that term, by the regent's
own `release`, or by a `revoke` under one new `revocation_bases` value. That value licenses ANY other seat on the regent seat's
rung, of its faction, whose grant carries `revoke`: the principal's seat is one of these and need not be the only one ((3)).
No tenure kind is added, no carrier field is added and no gate basis is added. "Puppet rulers" is NOT met on this route:
it is a named limit ((3), (8)).

(1) **The route.** IN-48's entry, copied: *"the design, on Layer 1's route (`establish` a second seat over the domain, `confer` it, IN-10's `Tenure.term`) — MEASURE whether a principal can revoke a same-rung seat early. READ, not yet run: creating a regent works on today's code (`may_fill`, `gate.py` ~575-579; `_eff_confer` closes holds only on the seat conferred) but ending one early does not — both `REVOCATION_RULES` need the revoking seat on the PARENT rung (`gate.py` ~422-428, ~512-513), the top rung's seat is strippable by nobody, so a realm regency ends by `Tenure.term` or the regent's own `release`; an early dismissal would be a new `revocation` basis (data in Layer 1's shape); a revoked `appointed` regent would carry IN-31's ban (`d16bd895`). That design may rewrite this entry's EXIT (whose premise, a person holding no `hold`, is non-Layer-1). A new `tenure_kinds` member is NOT licensed (Jordan's)."*

- **At this tree.**
  - `may_fill` is `state/gate.py:867-891`. Its `via == off.id` refusal is `:887`.
  - `REVOCATION_RULES` is `:604-605`. Both rules share `seated_on_the_rung_above_structure` (`:523-536`).
  - `may_revoke` is `:852-864`.
  - `_eff_confer` closes only the holds on the office it names (`loop/effects_governance.py:127`).
  - `architecture/meta/04_CODE_ARCHITECTURE.md:354` reads *"delegation = `establish` → `confer` → `revoke`"*, and
    `01_AXIOMS.md` §E.2.5 gives the three shapes of delegation.
- **The route has two shapes, and the measurement (2) separates them.**
  - **(a) A governor over a holding** (§E.2.5: *"assign others of lesser rank to govern any of their holdings"*). This seat
    is on a rung BELOW the principal's seat.
    - `establish`'s computed founding admits it: `queries/world_q.py::founds_over`, `:4612`, with four conjuncts (holding,
      purview, lower kind, the seat on the parent).
    - The founded seat declares `revocation: rung_above_in_holdings` (`offices.yaml: founding:`, `:169-174`).
    - So the principal, who sits on the parent rung and holds the rung, may revoke it at any time. **This shape runs
      today, end to end** (measured, (2)). B21b.25 adds nothing to it except a test.
  - **(b) A regency over the principal's own rung** (§E.2.2: *"a seat conferred over the domain while the title stays
    put"*). This seat is on the SAME rung as the principal's seat.
    - `establish` cannot found it. `founds_over`'s conjuncts (iii) and (iv) refuse the principal's own rung (measured
      False). So this seat is an AUTHORED row, as `off_widow_regent` (`offices.yaml:235-247`, realm rung, `appointed`) already is.
    - `confer` fills it: `may_fill` admits it, because purview is reflexive on the rung and `via` is not the office.
    - IN-10's term (`_declared_term`, `loop/effects_governance.py:63-83`) bounds it ONLY where something declares one: a
      HAND-BUILT `confer`'s `term` payload key, or the seat's own `offices.yaml` row `term:` (`:72-76`). A computed
      `confer` carries no term (`loop/predicates.py:232-236`), and a seat placed in a test has no row. **So in computed play,
      a regency on a seat with no authored `term:` is for life**, ended only by `release`, a death, or (3). This limit
      goes into H-108's cite (E5).
    - Ending it early needs (3).
- **What is not used.** No `delegate` kind, no `office == via` branch, no dormancy rule and no `SEAT_KINDS`: none of §2's
  apparatus is used.

- **Falsifier.** A regent's act admitted through a seat on which he holds no live `hold` (B21b.25,
  `test_a_seat_is_exercised_only_by_its_holder`).
- **Control.** The principal's act through his own seat is admitted, both while the regency stands and after it ends.

(2) **The measurement.** A throwaway script was run once and not kept.

- **Setup.**
  - The world is `tests/test_g3_not_yours.py::_gov_world`: R ⊃ D ⊃ S ⊃ Hh. `p_king` holds `off_crown` at R, on the top
    rung, with revocation `rung_above_same_faction`.
  - One seat was added: `off_regent` at R, of `off_crown`'s faction, `appointed`, remit `[issue, dispatch, revoke]`.
  - `p_king` conferred `off_regent` on `p_mid` with `term: 4`, through the shipped `_fold` at Success. Its revocation was
    read three ways.
- **Readings.** Command: `PYTHONHASHSEED=0 python <script>`.

| reading | result |
|---|---|
| `may_fill(p_king, off_crown, off_regent)` (control: the confer is lawful) | **True** |
| the fold's `confer` | `['tenure.opened']`; the regent's hold carries `Term(matures_at=4)`; the principal's hold is the same object and still live |
| **`may_revoke(p_king, off_crown, off_regent)`**, with revocation `rung_above_same_faction` / `rung_above_in_holdings` / `None` | **False / False / False** |
| the same, `rung_above_in_holdings`, with `p_king` also HOLDING R (`in_holdings` True) | **False**: R has no parent |
| the fold's `revoke` through `off_crown` | `['revoke.unauthorized']`; the regent's hold is still live |
| `may_revoke(p_mid, off_regent, off_crown)`: can the regent strip the principal? | False |
| CONTROL, the governor shape: `off_gov` at D, conferred on `p_mid`; `may_revoke(p_king, off_crown, off_gov)` under `rung_above_in_holdings` (the king holding D) / `rung_above_same_faction` | **True / True**; the fold's revoke gives `['tenure.closed']`, the hold is closed, and IN-31's `ban : p_mid → off_crown` is opened |
| `founds_over(p_king, off_crown, R)` / `(…, D)` with the king holding D | False / True |
| the term: confer with `term: 1`, then MATTER at tick 1 | the regent's hold is closed (T-n); `_seat_grants(p_mid, off_regent, issue)` is False; the principal's hold is live |

- **Verdict.** The principal cannot revoke a same-rung seat today, as the READ said. Neither rostered rule can admit it,
  because both read the parent rung. A realm regency therefore ends only by its term or by the regent's `release`.
  Shape (a) needs nothing. Shape (b) needs (3).
- **Falsifier.** Any of the three same-rung readings coming back True would have shown (3) unneeded.
- **Control.** The governor seat in the same world reads True through the same `may_revoke`. So the instrument can observe
  an admission.
- **Kept as a test.** B21b.25 keeps this reading as `test_a_principal_cannot_revoke_a_same_rung_seat_on_the_shipped_bases`,
  green before its roster edit, with the governor arm as its control.

(3) **The early dismissal: one `revocation_bases` value and its rule.**

- **The value.** `rosters.yaml: revocation_bases.values` gains `same_rung_same_faction`. It is named as the sibling of
  `rung_above_same_faction`.
- **The rule.** `state/gate.py` gains `seated_on_the_same_rung(w, seat, off)` beside `seated_on_the_rung_above`. It is true
  when `seat.rung` is not `None`, `seat.rung == off.rung`, `seat.faction == off.faction`, and `seat.id != off.id`.
  `REVOCATION_RULES` maps the new value to it.
  - It is structural, as ruling (3) is: no purview walk (the reading `seated_on_the_rung_above` rejects, `:516-517`), no
    holdings and no rank.
  - The faction clause is kept.
  - `seat.id != off.id` makes it exclusive on the seat, as `may_fill` is (`:887`). A holder stripping his own seat is
    `release` (T-m), not this.
  - The import check at `:609-616` refuses the roster value without its rule, and the rule without its value.
- **Who may strip a seat declaring it: its RUNG-SIBLINGS, not "the principal".** The holder of ANY other seat on the same
  rung, of the same faction (`may_revoke` asks that he sits in it), whose grant carries `revoke` (`revoke`'s `remit:revoke`
  eligibility, `loop/resolve.py:326`, not the rule's business). The principal's seat is one such sibling.
  - On the realm rung the siblings are `off_king`, `off_widow_regent`, `off_heir` and `off_princess` (`offices.yaml:182-273`).
    Only `off_king` grants `revoke` today. `off_widow_regent`'s own revert note (`:240`) would restore a grant carrying it,
    which would make the consort a second dismisser.
  - Two regent seats on one rung, both declaring the value and both granting `revoke`, can each strip the other's holder,
    and an `appointed` one bans the man it strips.
  - **This is fragile as a content rule.** Who may dismiss a regent is decided by what the OTHER seats on that rung grant,
    not by who conferred him. `Tenure.conferrer` was deleted as an ID-2 second home (§1), so no lighter rule can name the
    conferring seat. B21b.25's tests pin the sibling reach (a second same-rung seat granting `revoke` also admits), so it
    is visible, not hidden.
- **Necessity, stated narrowly.** Without the rule, a principal cannot unseat and refill an AUTHORED same-rung seat before
  its term ends. That is true only in authored content, and no such content exists today: no `offices.yaml` row declares
  the value, `founds_over` refuses the principal's own rung, and a computed founding writes `rung_above_in_holdings`.
  What survives without the rule:
  - "revoke at majority" (01_AXIOMS §E.2.2) is IN-10's term, where one is declared ((1));
  - "stop a bad regent now" partly survives: `arrest` (eligible on `remit:dispatch`, `verb_table.yaml:153`, through a
    seat whose warrant reaches him) opens a `detain`, and custody suspends every act through every seat he holds
    (`state/gate.py:344-358`). It does not vacate the seat or let it be refilled.
- **Basis.**
  - `04_CODE_ARCHITECTURE.md` §B.7 call 1: *"the revocation rule is data … two values of `revocation.conjuncts`"*.
  - **The shipped precedent is Jordan's own second value**, `rung_above_in_holdings` (2026-10-12). `REVOCATION_RULES` holds
    exactly those two entries (`state/gate.py:604-605`), and `revocation_bases` is `open: false` (`rosters.yaml:3851`): a
    third value arrives with its rule, as the import check requires.
  - `holder_of_rung` (`U5d_FA_land_and_seats_pass_on_a_won_march.md` edit 1, C3-L7) is UNBUILT. It is scheduled in B23
    (`workplans/valoria_master_workplan_v12_part37.md:121`). It is the same shape, data plus one rule, but not yet a
    precedent in code.
  - **Overlap to read across batches.** B21b.25 and B23 would add two new revocation values, for one question (who may
    strip a seat), in consecutive batches. Each batch's author reads the other's value before landing: the two rules must
    not admit the same seat for different reasons, and the roster note must list both.
- **Reach: only a seat that declares the value.**
  - No shipped row is edited. `off_king` stays `null`. `off_widow_regent` stays `null`: it is the consort's royal-house
    title, and giving it this value would let the king (and any sibling granted `revoke`) strip the queen and ban her, an
    outcome outside this position.
  - [ASSUMPTION; medium; Jordan to correct; revert: author a regent row in `offices.yaml` declaring the value — a content
    and build-hash mover, (7).]
  - **Symmetric, measured.** The rule applied by hand admits the regent's seat over the principal's seat just as it admits
    the reverse. The principal is safe only because his seat declares `null`. A principal's seat that declared this value
    would be strippable by his regent.
- **What the one rule unlocks, with no further code.**
  - Early dismissal (`revoke`).
  - Replacing a regent: `_req_confer`'s displacement asks `may_revoke` (`loop/predicates.py:201-204`).
  - Reducing a regent's grant: `revoke` with `keeps`, which is T-o (`state/gate.py:1612-1614`).
  - A-22's class (ii): the principal's seat then commands its regent, which it does not today (measured, (4)).
- **What dismissal costs.**
  - IN-31: an early dismissal of an `appointed` regent opens `ban : him → Act.via`, objected on the dismissing seat
    (`REVOCATION_DISPOSAL`, `state/gate.py:640`, Jordan B-Q). The ban is keyed on the seat's conferral basis, not on the
    revocation value. It is ruled and applied, not designed around.
  - **It lasts until pardoned through the dismissing seat. It is not permanent.** `_eff_pardon` closes every live
    restraint of the subject whose object is `Act.via` (`loop/effects_governance.py:427-454`), by a holder that seat's
    bench admits (`may_determine`; the `pardon` row's note names *"a revocation's `ban` (object: the revoking seat,
    IN-31)"*, `verb_table.yaml:1556`).
  - **Its reach is realm-wide from a realm seat.** `restrained(..., at=)` bars every seat whose rung the banning seat's
    purview reaches (`queries/world_q.py:2163-2177`).
  - **Three ways avoid it.** A term's end is T-n and no revocation, so it bans nobody. A displacing `confer` bans nobody,
    because `_eff_confer` reads no disposal (`state/gate.py:629-630`). A Partial-band revoke unseats him without the ban
    (`_eff_revoke`, `loop/effects_governance.py:395-398`, B21.14).
  - **Stale text inherited.** "no effect closes one, so only his death ends it" (`state/gate.py:627-628`;
    `loop/effects_governance.py:364`; `revoke`'s `disposal_note`, `verb_table.yaml:1841`) is false at the code: `_eff_pardon`
    closes it. B21b.25 corrects that factual clause (E3). It leaves Jordan's quoted word "PERMANENT" standing as his text
    and records that the code admits a pardon.
- **The puppet ruler is NOT met (a LIMIT).** Layer 1 defines the puppet as the title-holder whose seat's remit *"has been
  conferred elsewhere"* (`01_AXIOMS.md:1467`). On this route the title seat never loses its remit:
  - narrowing a sitting holder's grant is T-o and asks `may_revoke` (`state/gate.py:1612-1614`);
  - `off_king` declares `revocation: null` (`offices.yaml:190`), and `may_revoke` refuses a seat whose basis is off the
    roster (`state/gate.py:862-863`);
  - `_req_establish` refuses a re-stamp that reduces a sitting holder's grant (`loop/predicates.py:466-469`).
  So a regent seat declaring `null` beside a king who keeps his full grant gives two rulers, not a puppet. No path in the
  tree empties the title seat's grant without the holder's own consent (`release`, which vacates rather than hollows).
  "Puppet rulers" therefore stays OPEN in H-108's cite (E5), and is not claimed met here.
- **Falsifier.** With the value declared, the principal's `revoke` is admitted and closes only the regent's hold.
  - The rule refuses a seat on another rung (a child seat read from R; measured False by hand).
  - It refuses a same-rung seat of another faction.
  - It refuses the seat itself.
  - The regent cannot strip a principal's seat that declares `null`.
  - A second same-rung, same-faction seat whose grant carries `revoke` ALSO strips the regent (the sibling reach, pinned
    so it is visible); the same seat without `revoke` in its grant is refused at eligibility.
- **Control.** The same world with the regent seat declaring `null` is refused, which is (2)'s reading.

(4) **Whom the regent commands (A-22), and custody (A-23).**

- **A-22.** `world_q.commands` (`queries/world_q.py:3326`) composes on `state/gate.py::commands_a_seated` (`:1127`). All of
  it is asked of the SEAT `via` names, so the regent commands what his seat commands.
- **Measured** in the (2) world (regent seat `rung_above_same_faction`), principal's seat against regent's seat:

| person | through `off_crown` | through `off_regent` | why |
|---|---|---|---|
| `p_high` (holds `off_duke` at D, `rung_above_same_faction`) | True | True | class (ii): structural, the same for two seats on one rung of one faction |
| `p_other` (holds `off_duke2` at D2) | True | True | class (ii) |
| `p_low` (unseated, lives at Hh) | True | True | class (iii): the same ground |
| `p_far` (unseated, lives in a second realm), sworn to `off_crown` | True | **False** | class (i): each seat's establishment is its own |
| `p_far`, also sworn to `off_regent` | | True | class (i) |
| holder of a `rung_above_in_holdings` seat at D, the KING holding D: `may_revoke` | True | **False** | holdings are the person's (§E.2.3: *"Holdings GATE the act; they are not the authority"*) |
| the regent himself, from `off_crown` | **False** (today) | | class (ii) needs (3) |

- **Consequences, accepted as the ruled meaning, with no edit.**
  - Men sworn to the principal (the vassals, CR-86) serve the principal's seat, not the regency, until they swear to it.
  - A regent cannot strip a seat that declares `rung_above_in_holdings`, because the holdings stay with the principal.
- **A-23.**
  - A detained regent acts through no seat. Measured: `_seat_grants(p_mid, off_regent, issue)` is False, and the hold stays
    live (custody suspends, it does not vacate).
  - The person side agrees: `decision/options.py::seat_of`, `:884`.
  - A detained principal is the same, so the regency governs on while the principal is held, and the principal cannot
    dismiss the regent from custody, because `revoke`'s eligibility goes through `_seat_grants`.
  - No edit.
- **Falsifier.** The regent's seat commanding a man sworn only to the principal's seat.
  - The detained regent's act through his seat admitted.
- **Control.** The same man commanded once he is sworn to the regent's seat. The regent's act admitted once the `detain`
  is closed.

(5) **§9's Phase 1 findings on this route.**

| # | does it apply? | what the design does |
|---|---|---|
| 1 | **Changes shape.** The regent exercises HIS OWN seat, so `rung_above_in_holdings` reads his holdings, which are none. `founds_over` (i) does the same, so a regent founds no seat over the principal's holdings. | No fix. The measured refusal is the ruled reading ((4)); it is a residue in H-108's cite. |
| 2 | **Dissolved.** No delegate edge exists. A superior's displacing `confer` on the principal's seat leaves the regent's seat untouched. The successor may dismiss the regent through his seat under (3), because the rule is about seats, not persons. | None. |
| 3 | **Applies.** A seat granting `confer` but not `revoke` can fill a regent seat and cannot dismiss it. Every shipped seat that grants `confer` also grants `revoke` (`offices.yaml`: `off_king`, the three duchy heads, `off_confessor`). | A residue, unchanged. |
| 4 | **Dissolved.** The regent's grant is his `hold`'s, stamped at `confer` by `World._grant_remit`. `establish` re-stamps every live `hold` on the seat (`_eff_establish`, `:274-282`). Narrowing the grant is `revoke` with `keeps` under (3). | None. |
| 5 | **Dissolved.** No dormancy rule. `reach`, `governors_of` and every other `hold` reader see the regent as a holder. | None. |
| 6 | **Re-scoped.** The "hold preferred" and `delegate != actor` gaps die with the kind. Still owed: the EXIT judged by `harness/corpus_run.py::attribute` (refusal kinds include `<verb>.unauthorized`, read in (2)) with a same-world control. | B21b.25's tests, (6). |
| 7 | **Partly applies.** `state/gate.py::seat_hold`'s docstring (`:328-333`: *"A `hold` AND NOTHING ELSE SEATS A PERSON TODAY … delegation without a `hold` is `H-108`'s"*) is stale on this route, and cites `04:332` for what is now `04:353`. The other stale texts §9 lists belong to the reverted build. | B21b.25 rewrites that docstring: a regent is the holder of a second seat. |
| 8 | **Dissolved.** No `office == via` branch, so no DECLINE and no entry instrument are needed. | Covered by (7)'s hash control. |
| 9 | **Still applies for the puppet; changes answer for the outside installer.** "Puppet rulers" is NOT met: the title seat keeps its full grant ((3), the LIMIT). What IS measured: an OUTSIDE seat can fill a governor seat in a sworn duke's ground through `may_fill`. In the (2) world, `may_fill(p_other, off_duke2, off_dgov at D)` is False, then True once the Duke of D swears to `off_duke2` (the oblige clause); the fold's `confer` gives `['tenure.opened']` and the Duke keeps his seat. That is a governor installed from outside, not a puppet: the installer has no lever over the man installed (the seat declares `null`), and the Duke keeps his grant. | B21b.25 keeps the installer reading as a test. The puppet is named open in H-108's cite (E5). |

- **Falsifier.** A dissolved row reappearing in B21b.25: a dormancy read, an `office == via` branch, or a `SEAT_KINDS` set.
- **Control.** The rows that apply (1, 3, 6, 7, 9) are each named by a test or by H-108's cite.

(6) **The EXIT and FALSIFIER, rewritten.**

IN-48's EXIT is *"in a seeded season a person holding no `hold` on a seat exercises it `via` that seat through the delegation
carrier while the principal keeps the hold, and when the carrier ends the same act refuses"*. It becomes the following.

- **EXIT.** In a seeded season, a regent exercises the conferred seat `via` that seat while the principal keeps his own:
  - The season is `build_realm(0)`, one season, plus a same-rung regent seat declaring `same_rung_same_faction`, placed at
    build in the TEST, and the principal's HAND-BUILT `confer` of it with a `term` payload. The term is the hand-built
    act's: a computed `confer` carries none, and the test-placed seat has no row, so the term arm observes IN-10 only for
    a hand-built act ((1)). A computed regency on a seat with no authored `term:` is for life, and the EXIT does not claim
    otherwise.
  - "Exercises" means his act executes, judged by `harness/corpus_run.py::attribute` against a same-world control in which
    nobody holds the regent seat.
  - "Keeps" means the principal's hold is live and is the same object.
  - When the regency ends, the same act through it refuses. Three arms: the term at MATTER (T-n), the principal's `revoke`
    (T-o under (3)), and the regent's `release` (T-m).
- **FALSIFIER, kept from H-108.** *"delegate's act admitted after delegation ended, or a seat exercised by a person with
  neither hold nor carrier → fail; principal's hold closed by a delegation → regency by term (IN-10), not this."* On this
  route the carrier IS the second seat's `hold`, so "neither hold nor carrier" reads "no live `hold` on the seat exercised".
- **B21b.25's named tests**, each red before its edit where an edit exists:
  - `test_a_principal_cannot_revoke_a_same_rung_seat_on_the_shipped_bases` ((2); green before).
  - `test_a_principal_dismisses_his_regent_early` ((3)).
  - `test_the_regent_acts_via_his_seat_and_refuses_after_term_dismissal_and_release`.
  - `test_a_seat_is_exercised_only_by_its_holder`.
  - `test_conferring_a_regency_leaves_the_principals_hold`.
  - `test_the_regent_cannot_strip_a_principal_seat_declaring_null`.
  - `test_a_regent_seat_declaring_null_is_dismissed_by_nobody`.
  - `test_a_rung_sibling_granting_revoke_also_dismisses_the_regent` ((3), the sibling reach).
  - `test_an_outside_seat_installs_a_governor_through_a_sworn_holder`.
  - `test_the_regent_commands_what_his_seat_commands` ((4)).
  - `test_a_governor_over_a_holding_is_founded_conferred_and_revoked` (shape (a)).
  - `test_in48_exit_seeded_season`.
  - [ASSUMPTION: the names.]
- **Falsifier.** The EXIT test passes with the regent seat removed, which would mean the act was admitted on another
  ground.
- **Control.** That same-world run, which `attribute` must read as not executed `via` the seat.

(7) **Hash.**

- **No carrier field.** `state/carriers.py` is not edited (no `Tenure` or `Office` field), so there is no encoding mover
  under D-04.
- **The change is data and a rule:** one roster value and one `REVOCATION_RULES` entry.
  - No shipped seat declares the value ((3)), so no seeded run reaches it. The build hash and the one-season hash at seeds
    0 to 2 equal B21b.23's. That is B21b.25's control.
  - `engine/engine_params/season_registries.json` exports the roster: today it carries `rung_above_in_holdings` 6 times.
    So it is re-derived with `tools/export_season_registries.py` and checked with `--check`. That is a params export, not
    the content hash.
- **B21b.25's HASH MOVERS: none.** This holds unless the orchestrator takes (3)'s revert, a shipped regent row, which is a
  behaviour mover and a build-hash mover (`w.offices` is hashed).
- **Falsifier.** Any realm hash at seeds 0 to 2 moving at B21b.25. That would mean a shipped path reaches the new value,
  contrary to this design.
- **Control.** The same readings on B21b.23's tree.

(8) **What the route does not settle (D-18).**

- **The route holds. STOPPED: no.**
  - Nothing here needs a Layer 1 change. §B.7 call 1 makes the revocation rule data. `01_AXIOMS.md` §E.2.4 (*"`tenure_kinds`
    does not move; no new carrier"*) and `04:354` are the route itself, not obstacles to it.
  - No `tenure_kinds` member is added.
  - (2)'s measurement fails only the shipped bases, and (3) answers it in Layer 1's shape. So the `delegate` kind of §1 to
    §8 is NOT put to Jordan, and no `needs_jordan` row is written.
- **The necessity of (3) is narrow.** Without it, a principal cannot unseat and refill an AUTHORED same-rung seat before
  its term ends. That is true only in authored content, and none exists today ((3), "Necessity"). "Revoke at majority"
  survives as IN-10's term, and "stop a bad regent now" partly survives as `arrest` and custody. So (3) is a rule built
  ahead of the content that reaches it. It is kept because it is the lightest shape (data plus one rule), because B21b.25's
  own EXIT reaches it, and because without it a principal's seat does not even command its regent (A-22 (ii), (4)).
- **Four limits are named and not designed around.**
  - **"Puppet rulers" is not met.** The title seat keeps its full grant; nothing hollows it ((3)). It stays open in H-108's
    cite. Meeting it would need a path that empties a sitting title-holder's grant without his consent: a reduction under
    `revoke` with `keeps` through a basis the title seat declares. That is content plus (3)'s kind of value on the title
    seat, which no shipped row has, and it is not this position's to author.
  - **A computed regency has no term** unless the seat's row authors one ((1)).
  - **A same-rung seat is not founded at runtime.** `founds_over` (iii) and (iv) refuse the principal's own rung. Its
    founded post would also be the rung's title post (`founded_post`): a second "King". So a regency over a principal's own
    rung exists only as an authored row.
    - Widening `founds_over` is v11 CR-25's code (marked [ASSUMPTION]), not Layer 1, and not this position.
    - It is carried as a residue in H-108's cite.
    - Shape (a) is founded at runtime today.
  - **Ruling (3) is the one verbatim ruling on who may strip a seat** (ED-IN-0256, *"rung above of same faction"*). The new
    value answers the same question differently for a seat that declares it.
    - It is answered by the ladder, without a row: step 4 (the shipped precedent is Jordan's own second value,
      `rung_above_in_holdings`, 2026-10-12; `holder_of_rung` is the same shape but unbuilt, B23) and step 5 (§B.7 call 1).
    - The new value licenses the seat's RUNG-SIBLINGS that grant `revoke`, not the principal by name ((3)). That is
      fragile as a content rule, and it is stated, not hidden.
    - No shipped seat declares it, so no ruled seat changes answer.
    - If Jordan reads it otherwise, the two options are: (i) this value; or (ii) no value, in which case a realm regency
      ends only by its term or by the regent's `release`, as today, and a dismissed regent is replaced only at term.
    - The orchestrator may raise it. This design does not need it raised.
- **B21b.23, re-read.** A delegation on this route opens a SECOND SEAT, not a second hold. Every seat it touches keeps one
  live `hold`, as measured in (2): the confer emits `tenure.opened` alone, and the principal's hold is unchanged.
  `_req_confer`'s every-holder read (`loop/predicates.py:191`) is unaffected and needs no re-read edit.
- **Falsifier.** B21b.25's diff touching `architecture/`, `tenure_kinds`, `state/carriers.py` or the gate's basis list
  (`tenure_write_basis`).
- **Control.** `git show --stat` of B21b.25 lists only the edits below.

**B21b.25's edits, in order** (the owners named; nothing else):

- **E1.** `engine/season/tests/test_in48_delegation.py`, written first. It holds (6)'s tests, on `_gov_world` plus
  hand-placed seats, and the seeded EXIT.
- **E2.** `rosters.yaml: revocation_bases`: add the value `same_rung_same_faction`, plus one note sentence that names this
  section's rule and its reach (only a seat that declares it).
- **E3.** `state/gate.py`:
  - add `seated_on_the_same_rung`;
  - add its `REVOCATION_RULES` entry;
  - rewrite `seat_hold`'s stale docstring paragraph ((5) row 7);
  - correct the false clause "no effect closes one, so only his death ends it" at `:627-628`, the same clause in
    `_eff_revoke`'s docstring (`loop/effects_governance.py:364`), and `revoke`'s `disposal_note` (`verb_table.yaml:1841`):
    `_eff_pardon` closes the ban through the dismissing seat ((3)). Jordan's quoted word is left as his text.
- **E4.** Run `python tools/export_season_registries.py`, then its `--check`.
- **E5.** `hole_register.yaml` H-108: closed for regency and governors, grade `measured`. Its cite names the residues:
  - **"puppet rulers" NOT met** (the title seat keeps its grant, (3));
  - a computed regency on a seat with no authored `term:` is for life ((1));
  - no runtime founding of a same-rung seat;
  - the dismissal rule licenses rung-siblings granting `revoke`, not the conferrer ((3));
  - `rung_above_in_holdings` seats are outside a regent's reach;
  - a seat granting `confer` without `revoke`.
  Whether the open puppet residue keeps the row open instead is the orchestrator's call, not this design's.
- **E6.** The glossary row *regent* (`unified/U1_GLOSSARY.md`), with the plan's text.
