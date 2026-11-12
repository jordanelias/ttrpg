# FA — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subsystem: factions, governance, offices, war and diplomacy (dossier `06_FA.md`). Lane tags FA, and the IN
positions that build the governance slice. Every reading below names its command, seed and season count;
`[UNVERIFIED]` marks what was not checked.

## 0. Verdict

VERDICT-PLACEHOLDER

## 1. What it is, as coded

**There is no FA module.** FA is not a registered module under `modules/` and has no composition row; it is
a slice of the season loop itself (`engine/season/`, Layer 2). Its code is four things:

| piece | file | what it is |
|---|---|---|
| eight effects | `engine/season/loop/effects_governance.py` (549 lines) | `confer`, `succeed`, `establish`, `release`, `revoke`, `pardon`, `convene`, `oblige`, `requisition`: each returns a `Change` (named subjects plus a `perform` closure) that the write gate applies. None calls `w.write`; none holds state. |
| seven untyped preconditions | `engine/season/loop/predicates.py` (711 lines) | `_req_confer`, `_req_succeed`, `_req_establish`, `_req_release`, `_req_oblige`, `_req_revoke`, `_req_dispatch`, `_req_convene` (plus `_req_interrogate`). Each asks the write gate's own predicates (`may_fill`, `may_revoke`, `may_claim`, imported from `state/gate.py`) so a precondition cannot admit what the gate refuses. |
| the faction view | `engine/season/queries/faction_q.py` (245 lines) | `Faction` is a frozen five-field dataclass (`proposition`, `members`, `holdings`, `seats`, `head`) built by `resolve(w, prop)`; `head`, `holdings`, `purview`, `superiors`, `subordinates` are functions. It is never a field of `World`, never `Act.actor`. |
| data | `engine/season/offices.yaml` (31 seats + 2 foreign, and the `titles.domains` ladder), `arrangements.yaml` (nine proceedings rows, six speech kinds; loader `data/arrangements.py`), `governance_spine.yaml` (a 13-seat regular fixture; builder `harness/governance_spine.py`), `data/affiliations.py` (the affiliation roster checks, the `incompatible` half-matrix, the verb × affiliation engagement table) | content and closed sets the loop opens at runtime. |

**The governing rule the code implements** (and the one the special charge asks about): *a faction does not
act*. A faction is a Proposition persons `commit` to; a faction's act is a person's act `via` a seat
(`Act.via`); a faction's holdings are its members' `hold` edges; its treasury is `Rung.stores` at the
seat's rung. `predicates.py:85-88` states it and `faction_q.py:84-95` builds it: nothing in `faction_q`
writes, and nothing stores a faction stat.

**How the season loop reaches it.** A person holding a seat (`hold` Tenure on an `Office`) is granted that
seat's `remit_acts` as a snapshot on the Tenure (`Tenure.granted_acts`, stamped by `World.add_tenure` /
`_grant_remit`). `decision/options.py::opening_set` forms a candidate for a `remit:<act>`-eligible verb only
for a holder whose grant names the act; `decision/choose.py` sets `Act.via` to the exercised seat; RESOLVE
asks the row's `requires` (typed cell or the predicate above), runs the effect, and the write gate
(`state/gate.py::tenure_write_basis`) admits each Tenure edge under a named basis (T-m own edge, T-o
revocation, conferral, claim, determination). Six remit acts exist (`rosters.yaml: remit_acts`):
`dispatch`, `confer`, `determine`, `convene`, `revoke`, `issue`. Of the table's 67 verbs (66 resolvable;
probe E-2), 19 are seat-gated by `remit:` alone.

**State it owns.** None of its own. It writes `Tenure` edges (`hold`, `oblige`, `ban`, `detain`), `Office`
rows (`establish`), `w.dates` (`convene`) and `Rung.stores` (`requisition`), all through the gate.

**Entry points and instruments.** `python -m engine.season.harness.governance_spine` prints the fixture's
census only (it runs no season; E-1). The spine is run through `aperture` (its SPINE block),
`populated.run`, `interactions`, `strife`. `obligee_report`, `heir_hears` and `aperture` are the
instruments that read governance behaviour in the populated realm.

