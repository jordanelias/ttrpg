# IN-48: the delegation carrier (a seat exercised by someone who does not hold it)

## Status: PROPOSED (2026-10-14) · design only, builds nothing · reference under `CLAUDE.md` §0.05
## Position: IN-48 (H-108's delegation half), `workplans/valoria_master_workplan_v9_part5.md` `### IN-48` · Lane: IN (FA SE) · IDs: none allocated
## Measured at HEAD `46c08d9c` (B-J boundary 1; IN-40 landed `3f320093`). A path with no top-level directory is under `engine/season/`.

The brief is the IN-48 entry: INSTRUCTION, DEPS, EXIT and FALSIFIER. This document does not restate it.

---

## 0. Verdict

**The carrier is a new `tenure_kinds` member, `delegate : Person → Office`.** The delegate owns it and
its object is the seat. The seat's sitting HOLDER opens it through that same seat: a `confer` whose
`office` is its own `via`, naming the delegate on `to`. The write gate admits it under one new basis,
`delegation`. It carries the same grant payload a `hold` carries, stamped by the one writer
(`World._grant_remit`), so `seat_hold` can return it as a second way to sit in a seat. The fold's remit
branch, the five `may_*` predicates and the person-side seat readers then admit the delegate's acts
`via` that seat with no further change. `purview_reaches` never reads a `delegate` edge, because
`sworn_to` filters on `kind == "oblige"` (`state/gate.py:393`). So the delegation can never be read as
vassalage, and no marker is needed to keep the two apart.

The edge ends in three ways:
- its `term` matures at MATTER (`T-n`; MATTER's term branch is already kind-general);
- the delegate's own `release` (`T-m`, a pure closure);
- the holder's `revoke` naming the seat itself and the delegate (the `delegation` basis's closing arm).

None of these touches the principal's `hold`.

---

## 1. What kills the other candidates

### (1) `oblige` plus a discriminator: killed three times, once by a ruling

- **The delegate would write his own delegation.** An `oblige` is opened by its owner under `T-m`.
  `_eff_oblige` mints `Tenure(..., a.actor, seat, "oblige", ...)` with `via=None`
  (`loop/effects_governance.py:367-370`), and `T-m` admits an owner's own opening
  (`state/gate.py:944-948`). A delegation carried on `oblige` is therefore self-grantable unless `T-m`
  gets a further carve-out keyed on the marker. That is a second special case on top of the marker.
- **The principal could not end it. Jordan ruled this.** If the delegate owns the edge, the principal
  ending it is an obligee-side closer. D-5 refused that kind of closer for `oblige` by ruling: *"no
  creditor verb, no `call_in`, no obligee-side closer on an obligation exists or will"* (quoted at
  `state/gate.py:988-990`; `verb_table.yaml:838`, `disposal_release_note`). SC-03a kept `determination`
  from closing an `oblige` for the same reason (`state/gate.py:836-837`). An `oblige` delegation would
  end only by its term or by the delegate's choice, which is not a delegation.
- **No discriminator already in the data tells the two apart.**
  - Direction: vassalage and delegation are both `Person → Office`.
  - Term: both may carry one. `_eff_oblige` always winds one (`_new_oblige_term`).
  - Who opened it: not on the edge. `Tenure.conferrer` was deleted as an `ID-2` second home
    (`state/carriers.py:84-93`); the opener is the Act in the log, and no gate basis reads the log.

  So any discriminator would be a second payload marker beside `DETERMINED_BY`
  (`state/carriers.py:70-72`, read by `Tenure.imposed`, `:112-115`). That marker is the shape
  divergence the IN-48 entry names.
- **Precedent decides it in any case.** SC-03a faced the same choice for `detain` and `ban` and made
  them kinds, *"which is why they are kinds and not an `oblige` (#453 §8.3)"* (`rosters.yaml:115-123`).
  The reason it gives is that an `oblige`'s holder can end it himself.

### (3) A co-hold, a second live `hold` with a narrowed grant: killed by the cardinality and by its readers

I measured this. `grep -rn 'kind == "hold"\|"hold" and\|kind != "hold"' engine/season --include=*.py`,
tests excluded, returns **50 matching lines in 15 files**, comments and docstrings included. I read
every code site that keys on the seat. **6 of them assume one live hold per seat**, or act on every
holder at once:

| reader | what a co-hold does to it |
|---|---|
| `queries/world_q.py:152-158` `hold_force` | **RAISES** `Forbidden` on two live holds. It is the S15 owner of "who holds this": *"`hold` cardinality is 1 PER OBJECT"*, `holonic §15`. Its live caller `loop/witness.py:373` reads Records, not seats, so the raise is reachable on seats only through probes. The law is the same either way. |
| `queries/world_q.py:1171` `leaders` | builds `{object: subject}`, so one of the two holders is silently dropped |
| `loop/predicates.py:154` `_req_confer` | `holder = next(...)`, which reads the first holder only |
| `loop/effects_governance.py:107` `_eff_confer` | closes every live hold, so re-filling the seat closes the principal too |
| `loop/effects_governance.py:191` `_eff_establish` | re-stamps every live hold with the full remit (`force=True`), which **erases the narrowed grant** |
| `loop/effects_governance.py:274` `_eff_revoke` | closes every live hold, so dismissing the delegate unseats the principal (**the plan's FALSIFIER**) |

Two more facts finish it:
- **The principal could not open it.** `may_fill` refuses `via == off` (`state/gate.py:575`), so only a
  superior seat could seat a co-holder. The principal could not delegate at all.
- **It contradicts the EXIT**, which asks for *"a person holding no `hold` on a seat"*.

### (4) Other rostered kinds: none has the right ends

`holonic_ARCHITECTURE.md:541-544` gives the ends of the kinds that are rostered but unopened:
- `succeed : Rung → Person`, the hearth's transmission pointer, with IN-51 as its reader;
- `tie` and `knot` : `Person ↔ Person`, stored once on the lower id.

None of them ends at an Office, and `succeed` already means heirship. An `oblige : Person → Person`
from the delegate to the principal names no seat, so it cannot answer `seat_hold(actor, via)`. It is
also the D-5 closer problem again.

### (2) A new kind: chosen. What it costs, counted

| cost | where | what it is |
|---|---|---|
| roster member | `rosters.yaml:124` `tenure_kinds.values` (`open: true`) | `+ delegate`, with a note on the `detain`/`ban` model (`:115-123`) |
| a named constant | `data/rosters.py:461` beside `DETAIN_KIND` | `DELEGATE_KIND = "delegate"`, plus `SEAT_KINDS = frozenset({"hold", DELEGATE_KIND})`: *the kinds through which a person sits in a seat*. One owner, ten readers (§3). |
| the `release` domain | `RELEASABLE_KINDS` is derived (`data/rosters.py:473`), so it gains `delegate` automatically | `verb_table.yaml:828` `release.domain` must add `delegate`, or loader invariant 6 fails the load (`data/verbs.py:954-961`). That is the falsifier working, not a cost to avoid. |
| opener derivation | `data/verbs.py` `_derive_openers_from_effects`: an AST walk that reads `kind` **only as a string Constant** at the `Tenure(...)` call (4th positional argument or `kind=`) | `_eff_confer`'s new construction must spell `"delegate"` literally. `DELEGATE_KIND` there would leave the kind reported opener-less by `tenure_kinds_without_an_opener()`. |
| `tenure_write_basis` | `state/gate.py:754-1011` | one new basis, `delegation`, plus `seat` widened to `SEAT_KINDS`. `T-m`'s existing seat carve-out (`:946`) then refuses a self-opening with no new clause, and `T-o` and `conferral` are narrowed to `hold` (§2.1). |
| write matrix | `write_matrix.yaml` rows are per carrier field (`Tenure.since`, `Tenure.until`, `Tenure.term`), not per kind | **none**. `confer` already declares `writes: [Tenure.until, Tenure.since, Tenure.term]` (`verb_table.yaml:176`), and `revoke` declares `Tenure.until`. |
| a verb | none | reuses `confer` and `revoke` (§2.1). A new verb would join R-05's denominator unexecuted. |
| shape pins | `tests/test_season_shape.py` | none expected. The `raise SystemExit` count does not move: no new loader raise. `len(VERB_TABLE)` does not move. The `tenure_kinds` readers in `engine/season/tests/` are a roster-is-data test (`:2517`, `:2539`) and a PRINTED opener-less list (`:3608-3610`), not a pinned member list. |
| hash | §4 | no field changes. `build_realm(0)` is unchanged by construction. |

---

## 2. The design, requirement by requirement

### 2.1 Who opens it, and under what gate basis

**The opener is `confer` with `office == via`.** The actor exercises seat `S` and names `S` itself as
the office, with the delegate on `to`. That act shape is **refused everywhere today**:
- `_req_confer` asks `may_fill` (`loop/predicates.py:136`), and `may_fill` refuses `via == off.id`
  (`state/gate.py:575`, *"exclusive on the SEAT"*);
- the gate's `conferral` basis asks the same predicate (`:1009`).

So the branch occupies only act space that has never executed. In ordinary English *"the King
conferred the regency on his brother"* is the idiom, so `confer` is the plain word (ED-IN-0179). It
mirrors `renewal`, which is reflexive on the seat: *"`via` IS `off` ... the only seat that may"*
(`state/gate.py:582-610`).

**New predicate `may_delegate(w, actor, via, off, delegate)`** in `state/gate.py`, beside `may_renew`.
Three conjuncts:
1. `via == off.id`.
2. `seat_hold(w, actor, via)` returns a Tenure **of kind `hold`**. A delegate cannot delegate further
   or dismiss a co-delegate. This filters the result of the one owner rather than re-scanning.
3. `delegate` is a person other than the actor.

The gate and both preconditions ask this one function, which is `may_fill`/`_req_confer`'s split.
Conditions that matter only when the edge is OPENED stay in `_req_confer`, below, so that a CLOSURE is
never refused because the delegate's standing changed after he was delegated. For example, a superior
may later confer the seat itself on the delegate.

**The `delegation` basis.** It admits:
- an OPENING of a `delegate` edge, judged on the opened edge as a whole, as `conferral` and
  `determination` are (`:807-809`, `:840-842`);
- a PURE CLOSURE of one (`_closes`, `:736`);

each only when `may_delegate(w, actor, via, seat, t.subject)` holds. It cannot grade, re-term or
re-grant. A `moved == {"payload"}` or `{"term"}` on a `delegate` edge is admitted by nothing.

**A delegate cannot write his own delegation**, and the existing code already gives this. Widen
`seat = w.offices.get(t.object) if t.kind == "hold" else None` (`state/gate.py:906`) to
`t.kind in SEAT_KINDS`. `T-m`'s existing guard `not (seat is not None and not closed)` (`:946`) then
refuses an owner opening his own `delegate` edge, exactly as it refuses one opening his own seat-`hold`
(the 2026-09-26 exploit, `:907-918`). It still admits his pure closure, which is the delegate's
`release`.

Placement in the chain: after `warrant` (`:1002-1004`) and after `if seat is None: return None`
(`:1005`), as `if t.kind == DELEGATE_KIND: return DELEGATION if ((opened or closed) and may_delegate(...)) else None`.
`T_O` and `CONFERRAL` below it are then reached by `hold` only, as they are today.

**The writes.**
- `_eff_confer` gains a branch at its top. When `office == a.via`, it builds
  `Tenure(H(w.world_seed, w.tick, to, f"delegate:{obj}:{a.id}"), to, obj, "delegate", w.tick, term=_declared_term(w, a))`.
  That is the id-salt pattern of `_eff_oblige` (`:368`), and it reuses `_declared_term` (`:37-53`, IN-10 (b)).
  The branch returns `Change((Subject.edge(nt, "tenure.opened"),), lambda: w.add_tenure(nt))` and
  **computes no `closed` list**, so it cannot reach the `perform()` that closes every hold (`:107`,
  `:116-117`).
- `_req_confer` gains the same branch **before** its `has_conferral_basis` test (`:126`). A delegation
  does not fill the seat, so the conferral basis is not its question. The branch admits on four tests:
  - `to` is a living person (the `:133-135` clause, reused);
  - `to` is not banned (`restrained(w, to, BAN_KIND)`, `_eff_confer`'s `:105` rule asked early);
  - `to` holds no live `hold` on `office`, and no live `delegate` from `to` to `office` exists (one per
    person and seat, `_req_oblige`'s rule);
  - `may_delegate` holds.

### 2.2 The remit: the seat's full grant, or a declared subset of it

The grant is written by the one writer. `add_tenure`'s branch `if t.kind == "hold": ... self._grant_remit(t)`
(`state/world.py:326-328`) becomes:
- `if t.kind in SEAT_KINDS: self._grant_remit(t)`;
- `_refuse_bad_hold` stays `hold`-only.

A `delegate` edge therefore carries `{"remit_acts", "seat_rung"}`, the shape `granted_acts` and
`seat_rung` already read (`state/carriers.py:117`, `:160`). No new payload key is added to the Tenure.

**Subset [ASSUMPTION; medium; Jordan to correct; revert: drop `within` and the act key, so every
delegation carries the seat's full grant].** A `confer` may declare `acts` in its payload, as it
declares `term` (`TERM_KEY`, `loop/effects_governance.py:30-34`, the `create_record` `stages`
precedent). The effect then calls `w._grant_remit(nt, force=True, within=acts)` in `perform()` after
`add_tenure`. `_grant_remit` gains a `within` parameter, `None` by default, and stamps
`tuple(a for a in off.remit_acts if a in within)`. It stays the only writer of the key, and it cannot
grant more than the seat has.

A computed act declares no `acts`, so it gets the full grant. The source of the subset is
`cases/chain/NPC3.yaml:83`: *"delegate separate domains of institutional power ... to different
subordinate leaders"*.

**`establish` does not re-stamp a delegation.** `_eff_establish` re-stamps `hold`s only (`:191`). A
delegation is a snapshot at opening, and nothing admits a `{"payload"}` change on it (§2.1).

### 2.3 Purview: the seat's, and never over the delegate's own ground

There is no edit to `purview_reaches` (`state/gate.py:297-372`). Every `may_*` asks it of
`w.offices[via]` (`may_fill` `:578`, `may_warrant`, `may_determine` through `sits_over`), which is
`04:350`: *"purview is asked of the seat exercised, not the actor ... A regent has the seat's purview"*.
The brief cites `:332`; the line is `:350` at this HEAD.

The oblige clause collects swearers from `sworn_to`, and `sworn_to` returns only `kind == "oblige"`
edges (`:393`). A `delegate` edge is never a swearer. So a delegate who holds seat `B` and exercises
seat `A` does not bring `B`'s ground under `A`. If he has ALSO sworn an `oblige` to `A`, his ground is
reached, because he is then a vassal as well. That is a second, independent fact, and the reason the
two must not share a kind.

### 2.4 What ends it, and the refusal after

| closer | basis | edit |
|---|---|---|
| its `term` matures at MATTER | `T-n` (`state/gate.py:971-973`, kind-general) | none. MATTER closes every live edge whose term has come (`loop/matter.py:229-236`) |
| the delegate's `release` | `T-m`, pure closure | none beyond the `release` domain (§1) |
| the holder's `revoke` with `office == via` and `to` = the delegate | `delegation`, closing arm | `_req_revoke` and `_eff_revoke` each gain an `office == a.via` branch that asks `may_delegate` and closes the live `delegate` edges `(to → office)` only, never a `hold` |

`revoke` with `office == via` is refused today for the same structural reason as `confer`: a seat is
never on the rung above itself (`seated_on_the_rung_above_structure`, `:422-428`).

**The refusal after.** `seat_hold` reads only live edges, so once the edge is closed it returns `None`.
The fold's remit branch (`loop/resolve.py:118-120`) refuses the same act, and so does every `may_*` at
the gate. No other state is involved.

### 2.5 The principal's hold closes, or the principal dies, while a delegation is live

**The delegation survives. It is the seat's, not the principal's**
[ASSUMPTION; medium; Jordan to correct; revert: `seat_hold` admits a `delegate` edge only while some
live `hold` on `via` exists, which makes a delegation dormant in a vacancy].

- **Death.** MATTER's death `cascade` closes edges whose subject or object is gone (`:949-950`). That
  closes the principal's `hold`. The `delegate` edge names neither him nor anything gone, so it stays
  live.
- **Resignation or revocation.** A principal's `release` or `revoke` closes his `hold` only.
- **Interregnum.** The delegate keeps exercising the seat until its term, his own release, or the next
  holder's `revoke` (the new holder satisfies `may_delegate`'s `hold` conjunct). This is regency during
  a vacancy. A delegate cannot seat himself through the seat he exercises, because `may_fill` refuses
  `via == off`.
- **Re-filling.** `_eff_confer` filling the seat through a superior seat closes `hold`s only, so the new
  holder inherits the seat's delegates and may dismiss them.

The EXIT's case, *"while the principal keeps his hold"*, holds under both readings.

### 2.6 `seat_hold`, the one owner

`seat_hold` returns the actor's live `hold` on `via` if he has one, and otherwise his live `delegate`
edge on `via`. The hold is preferred, so a person who holds a seat and is also delegated on it acts on
his own grant. The docstring's *"A `hold` AND NOTHING ELSE SEATS A PERSON TODAY"* (`:281-286`) is
rewritten to say what does. Its readers inherit the delegate:
- `may_revoke` `:552`, `may_fill` `:575`, `may_renew` `:610`, `may_determine` `:686`,
  `may_warrant` `:711`;
- the fold's remit branch, `loop/resolve.py:118`.

That is everything `seat_hold` decides. The person-side readers do not call it. They scan
`p.tenures` for `kind == "hold"` and must read `SEAT_KINDS` so that `via` and the gate agree (§3).

---

## 3. EDITS for the build

`state/gate.py`
- `seat_hold`: prefer the `hold`, else the `delegate` edge; new docstring.
- New `may_delegate`.
- New `DELEGATION = "delegation"` basis name.
- `tenure_write_basis`: `seat` over `SEAT_KINDS` (`:906`); the `delegation` clause after `:1005`; the
  docstring's basis list, *"ELEVEN"*.
- `refuse_unauthored`'s count prose.

`state/world.py`
- `add_tenure`: grant for `SEAT_KINDS` (`:326-328`).
- `_grant_remit(t, force=False, within=None)`.

`data/rosters.py`
- `DELEGATE_KIND`, `SEAT_KINDS`, checked as `<= TENURE_KINDS` with an `Unspecified`, on the
  `RESTRAINT_KINDS` precedent (`:463-469`).

`rosters.yaml`
- `tenure_kinds.values += delegate`, and a note.

`verb_table.yaml`
- `release.domain += delegate`.
- `confer` gains a `writes_note` sentence and a `requires` sentence for the `office == via` branch.
- `revoke` gains the same.

`loop/effects_governance.py`
- `_eff_confer`'s branch, with the literal `"delegate"`.
- `_eff_revoke`'s branch.
- `ACTS_KEY = "acts"`, beside `TERM_KEY`.

`loop/predicates.py`
- `_req_confer` and `_req_revoke` branches.

`decision/options.py`
- `_granting_holds` (`:455`) and the `seat_rung` reader (`:615-616`) read `SEAT_KINDS`. Without this
  the chooser never forms a computed act `via` a delegated seat, and the EXIT's seeded season cannot
  happen.

`queries/world_q.py`
- `judging_set` (`:412`) reads `SEAT_KINDS`, because `may_determine` will admit a delegate on a judging
  seat. Its own docstring forbids a bench listed one way and admitted another (`:406-407`).
  [ASSUMPTION; medium; revert: a judging seat's delegate does not sit in judgment, so `may_determine`
  asks for a `hold`.]
- The vacancies seat list (`:1614`) reads `SEAT_KINDS`.
- `reach` (`:554`, its held-office limb `:587`) and `governors_of` (`:594`, `:621`) read `SEAT_KINDS`.
  These give a delegate the seat's ground in his question filter and in the purview deposit: the
  seat's eyes go with its exercise. Without them, a delegate exercises a seat whose ground he never
  hears about. [ASSUMPTION; medium; Jordan to correct; revert: both stay `hold`-only, so a delegate
  acts on what he learns as himself.]

`epistemic.py`
- `_hold_tenure_ends`'s kind test (`:179`) becomes `SEAT_KINDS`, so a delegation's receipt names the
  delegate and the seat. Otherwise it is unwitnessable, the R8.1 gap that function closed for `hold`.

`hole_register.yaml`
- H-108 closed when the EXIT is observed.

Tests: see §5.

**Not edited:**
- `purview_reaches` and `sworn_to`: §2.3 is the point.
- `state/carriers.py`: no field.
- `Query.budget` (`decision/budget.py:57`): a delegate gets no office bonus [ASSUMPTION; medium;
  revert: count `SEAT_KINDS`].
- `world_q.leaders` (`:1171`): a delegate is not a faction leader.
- The harness readers (`harness/aperture.py:83`, `:195`, `harness/invariants.py:236`,
  `harness/governance_spine.py:227`).
- `IN-48`'s assumed `decision/choose.py` edit: `via` comes from `seat_of` → `_granting_holds`
  (`decision/options.py:436-456`), which is edited above. `choose.py:582` passes it through unchanged.

---

## 4. Hash

**No dataclass field changes, so there is no schema move.** `Tenure`'s fields are unchanged
(`state/carriers.py:75-106`). A `delegate` edge's payload has the shape a `hold`'s already has.

**`build_realm(0)` is unchanged with no delegation present.** No world builder mints a `delegate` edge,
and widening `_granting_holds`, `judging_set`, `seat_rung`, `_hold_tenure_ends` and `add_tenure` to
`SEAT_KINDS` changes nothing in a world that holds none. The precedent is SC-03a's two new kinds with
build `11989dcf` unchanged (commit `c2f855d2`).

**Outcomes:** no seeded run moves unless a computed act reaches `confer` or `revoke` with
`office == via`, which is refused today and would open or close a delegation after the build.
MEASURED, see §4.1.

### 4.1 The measurement

**The method.** I wrapped three predicates and counted calls by `via == off.id`:
`loop/predicates.py`'s `may_fill` (asked by `_req_confer`) and `may_revoke` (asked by `_req_revoke`),
and `queries/world_q.py`'s `may_fill` (asked by `vacancies`), which is the control. Then I ran
`harness.populated.build_realm(0)` through `run()` for four seasons on HEAD `46c08d9c`.

**Totals after season 4:**

| predicate | `via != off` | `office == via` |
|---|---|---|
| `world_q.may_fill` (control) | 289 calls | 0 |
| `predicates.may_fill` | 5 calls | 0 |
| `predicates.may_revoke` | 0 calls | 0 |

The log over the same run holds `confer.refused` 4, `revoke.refused` 11, `tenure.opened` 1 and
`tenure.closed` 9. Every `revoke` refused before `may_revoke` was reached, on an `office` that is not a
seat (`loop/predicates.py:427-429`). An `office == via` that names a real seat would have passed that
check and been counted.

An earlier run of seeds 0 and 1 for two seasons each also counted **0** predicate calls.

**So no seeded run measured here reaches the new branches.** I expect no outcome to move, and the build
re-checks this with its own control. This is the scope of the measurement: seed 0 over four seasons,
and seeds 0 and 1 over two. It does not cover the corpus.

**The live path, so the build knows where to look.** `opening_set` can form a computed `confer` on a
seat the actor was TOLD of, and that seat can be one he holds (`queries/world_q.py:1600-1605`;
H-207, C4). If that seat is also the one `seat_of` picks for `via`, the act is `office == via`. Today
it is refused. After the build it opens a delegation to a person he knows. The build must either
measure that this stays at zero across the corpus or decline it in `opening_set`.
[ASSUMPTION; medium; Jordan to correct; revert: allow it, since a told-of own seat delegated to a known
person is a decision source the EXIT could use].

---

## 5. Falsifiers the build must add

All go in `engine/season/tests/test_in48_delegation.py`, and each is seen red before its clause is
written.

1. **The plan's first falsifier.** A delegate's act `via` the seat is admitted. After the edge closes
   it is refused, at the fold (`*.refused`) and at the gate (`may_*` is False). Run three arms, one per
   closer: term maturity at MATTER, the delegate's `release`, and the holder's `revoke`.
2. **The plan's second falsifier.** A person with neither a `hold` nor a `delegate` on `S` names
   `via=S`, and the act is refused. A control arm: the same person with the edge is admitted.
3. **The plan's third falsifier.** Opening a delegation leaves the principal's `hold` live, with
   `until is None` and the same id, and `_eff_confer`'s `office == via` branch names no `tenure.closed`.
   `revoke` of a delegation closes no `hold`.
4. **No self-delegation.** A gate write in which a person opens his own `delegate` edge raises
   `NotYours`. The same write by the holder through the seat is admitted under `delegation`.
5. **No delegation by a delegate.** A delegate's `confer(office == via)` is refused, and so is his
   `revoke` of a co-delegate. Each is checked by `may_delegate`'s `hold` conjunct.
6. **Not vassalage.** A delegate holding seat `B` (on ground outside `A`) is delegated on `A`.
   `purview_reaches(A, B.rung)` is False. A control arm: the same man's live `oblige` to `A` makes it
   True. This is IN-40's test turned around.
7. **Subset.** A `confer` declaring `acts=[x]` grants `(x,)` ∩ the seat's remit. An act outside it,
   `via` the seat, is refused at the fold's remit branch.
8. **The principal dies.** Run a `cascade` on the principal: his `hold` closes and the delegation stays
   live and exercisable (§2.5's assumption, pinned so that a revert shows up as a red test).
9. **Load.** Removing `delegate` from `release.domain` fails the load (invariant 6, an existing raise).
   `_derive_openers_from_effects()["delegate"] == {"confer"}`.
10. **The EXIT.** In a seeded season (`build_realm` with one `delegate` edge placed at build, as the
    builders place `hold`s), the delegate's computed act executes `via` the seat while the principal
    holds it. After the holder's `revoke` the same computed act refuses. H-108 is closed on this test.

---

## 6. Assumptions and open decisions

Each assumption below is marked inline where it is made. Collected here:

- **A1. Subset by act declaration** (§2.2). The default is the full grant.
  Revert: full grant only, with no `acts` key.
- **A2. The delegation survives its principal**, because it is the seat's (§2.5).
  Revert: `seat_hold` admits a delegation only beside a live `hold`.
- **A3. A judging seat's delegate sits in judgment** (§3, `judging_set`).
  Revert: `may_determine` asks for a `hold`.
- **A4. The seat's knowledge goes with its exercise** (§3, `reach` and `governors_of`).
  Revert: both stay `hold`-only.
- **A5. No budget bonus for a delegate** (§3).
  Revert: `Query.budget` counts `SEAT_KINDS`.

**What the orchestrator decides, not this document:**
- **The opener is `confer`/`revoke` with `office == via`, not a new verb.** This keeps R-05's verb count
  where it is. The alternative is a `delegate` verb. Its cost is a full `verb_table.yaml` row, a
  `remit_acts` roster member granted on every seat that may delegate, and a new R-05 row that does not
  execute until a decision source exists.
- **No computed decision opens a delegation.** The EXIT's seeded season places the edge at build. A
  person-side reason to delegate is the residue H-108 hands on when it closes.
