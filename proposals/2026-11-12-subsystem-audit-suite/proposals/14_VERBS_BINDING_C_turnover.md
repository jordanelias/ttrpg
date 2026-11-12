# VB-C — seats change hands by a draw: an appointment can be resisted, a revocation withstood, a claim contested

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-25, C-31, C-35) — the term `standing` is the roster member `rank_gap` (licensed by Jordan's A-12; the word `standing` already names a prize). Edit 3's audience is `heard_by: seat_body` on the prize row. `revoke` reads `reception` and not `regard`: a row has an audience or a single hearer, never both. §3's Partial for `succeed` opens termed seats under the existing claim basis and lays the title down; the variant that keeps the title needs a gate basis `04` §C.2 does not list and is not built. §2's `revoke` draw carries A-35 (the head strips an officer by a resistible draw).

## Status: PROPOSED

Source: `audits/14_VERBS_BINDING.md` §0.2, §1 (`confer`), §11 (`revoke`), §12 (`succeed`); batch C.
Binds on, and does not redo: `06_FA_decree_binds.md` (FA-P1; its change 4 is this file's edit 5),
`06_FA_seat_terms_and_turnover.md` (FA-P3), `06_FA_seat_terms_by_body_B.md` (FA-B3),
`06_FA_shortest_loop_B.md` (FA-B4, the gate), `06_FA_playable_scenario.md` (FA-P4), CP-T09-06, CR-35,
CR-36, CR-88 (selection). Cross-lane request to `05_SC_obstacle_difficulty_and_modifiers_B.md` (SC-B):
one obstacle term, `standing`, and an audience operand on `reception`.

## What it changes in `engine/season/` at runtime

1. `confer`, `revoke` and `succeed` become contested rows (prize `a seat`, VB-A edit 11), each with
   graded, recoverable bands. Today each takes effect with certainty once admitted, against the standing
   rule (`AUDIT_BRIEF.md`, *"we do not do deterministic"*).
2. A seat-opening `Partial` opens a provisional hold, termed `provisional_term` seasons; MATTER already
   matures a termed hold and closes it (`T-n`).
3. `revoke` reads its seat from `subject` (FA-P1 change 4), so a computed revoke can execute.
4. `revoke` forms only on a seat the actor's own ledger says is held; `succeed` only on a seat it says is
   vacant.
5. Every seat whose `conferral` is `inheritance` must have a `successions` row, checked at load.

All movers where they bite. In the shipped realm (1) moves nothing until (3) and occasions exist
(`confer` attempted 0 at seeds 0 and 1; `succeed` formed 0); FA-B4's scenario is where it is read.

## The problem (evidence)

- `aperture 2 0` `[FA]`: `confer` formed 5, attempted 0; `revoke` formed 5, attempted 0. `aperture 2 1`:
  both formed 0. `succeed` formed 0 at both. `tenure.opened` 0 at seeds 0–2, three seasons (FA E-5).
- `_req_revoke` and `_eff_revoke` read `payload["office"]` (`loop/effects_governance.py:333-334`), which no
  computed act carries; refused at clause 1 by construction.
- `_eff_confer`, `_eff_revoke`, `_eff_succeed` write unconditionally once admitted: an appointment always
  takes, a man stripped always goes, the heir always reigns.
- `successions` has one row (`off_king: off_heir`); `rosters.yaml`'s own note defers Valorsmark to
  CP-T09-06.
- `own_title_declines` forms `succeed` while the King sits (its note: *"re-forms `succeed` on it while a
  King sits, and is refused each time"*).

## The resolution, decided

**The draw** (audit §0.2; ladder step 3 for the rule, step 4 for the shape: `determine` is the contested
binding precedent, its degree keyed writes the table's own method). Pool: the actor's, through the one
pool reader (office weight and the governance vocations of FA-P6). Obstacle, through SC-B's one owner:

| row | `difficulty` | `opposition` | other terms |
|---|---|---|---|
| `confer` | `routine` | the incumbent, only when displacing | `reception` (audience: the seat's body), `standing` (the conferee against the seat), `stakes` `hold` |
| `revoke` | `routine` | the holder | `regard`, `standing`, `stakes` `hold`, `reception` (the seat's body) |
| `succeed` | `routine` | none | `reception` (audience: the seat's body, or the realm's seated persons for a seat with no body), `standing` |

**The bands**, one shape for the family: Overwhelming and Success do the act; Partial does it
provisionally (a seat-opening act opens a termed hold; `revoke`'s Partial unseats without the disposal);
Failure writes nothing on the seat and emits its own kind, and the act may be tried again.

**`standing`** is the term the family needs and SC-B's closed roster lacks: how far the person acted on
(or for) stands above or below the exercised seat. Read off `rosters.yaml: rung_kinds`' order through the
gate's rank reader (the one `rank` stem), times a fixture `standing_step`, control 0. Requested of SC-B's
owner (one roster member, one operand, one composition line), not edited there.

**The ledger filters** take `own_title_declines`' route: person-side, the newest claim in his own ledger
naming the seat (`LedgerReader`'s comparator), `tenure.opened`/`succession.claimed` → held,
`tenure.closed` → vacant.

## Exact edits, by owner

**Commit C1 — the shared parts.**

1. `engine/season/data/fixtures.py`: `provisional_term` (proposed 2 seasons; sweep {1, 2, 4}; control:
   Partial = Success), `standing_step` (proposed 0.25; sweep {0, 0.25, 0.5}; control 0), each with a
   NUMBER row in `hole_register.yaml`.
2. `loop/effects_shared.py`: `_provisional_term(w, a) -> Term`, `_new_oblige_term`'s shape
   (`Term(w.tick + w.fixtures["provisional_term"], a.id)`), the one constructor of a Partial's term.
3. SC-B request (listed, not edited): `obstacle_terms` gains `standing`; `SocialContestInput` gains
   `standing`; `reception`'s reader takes an `audience: tuple[str, ...]` (the bench today).

**Commit C2 — `revoke` executes (FA-P1 change 4, adopted).**

4. `loop/predicates.py::_req_revoke` and `loop/effects_governance.py::_eff_revoke`: `obj =
   office_named_by(a)` in place of `payload.get("office")`.

**Commit C3 — the draws.**

5. `verb_table.yaml`, `confer`:
   ```yaml
   contests:    "a seat"
   difficulty:  routine
   writes:
     Overwhelming: ["Tenure.until", "Tenure.since", "Tenure.term"]
     Success:      ["Tenure.until", "Tenure.since", "Tenure.term"]
     Partial:      ["Tenure.until", "Tenure.since", "Tenure.term"]
     Failure:      []
   emits:
     Overwhelming: ["tenure.opened", "tenure.closed"]
     Success:      ["tenure.opened", "tenure.closed"]
     Partial:      ["tenure.opened", "tenure.closed"]
     Failure:      ["appointment.resisted"]
   ```
   `counterparty: to` stays (the conferee is the second side); the `opposition` operand is the incumbent,
   built host-side only when a live hold is displaced, else absent. `emits_on_refusal` stays flat.
   `_eff_confer`: at `Partial`, `term=_provisional_term(w, a)` unless the act or the row declares a
   shorter one.
6. `verb_table.yaml`, `revoke`: `contests: "a seat"`, `difficulty: routine`, `counterparty: subject`
   resolved to the holder host-side (`revoke`'s subject is the seat; the opponent is its live holder,
   read where `_contest` reads the counterparty); writes `Tenure.until`, `Tenure.since` at O/S,
   `Tenure.until` at Partial, `[]` at Failure; emits `tenure.closed` at O/S/P, `revocation.resisted` at
   Failure. `_eff_revoke`: at `Partial` skip the disposal (`bans = []`).
7. `verb_table.yaml`, `succeed`: `contests: "a seat"`, `difficulty: routine`; writes `Tenure.until`,
   `Tenure.since` at O/S, `Tenure.since` at Partial (the title is kept), `[]` at Failure; emits
   `succession.claimed`, `tenure.closed` at O/S, `succession.claimed` at Partial, `succession.contested`
   at Failure. `_eff_succeed`: at `Partial` open each seat with `term=_provisional_term(w, a)` and close
   no title. The gate's claim basis is licensed by the title's closure in the same write
   (`refuse_unauthored`'s second pass); a Partial that keeps the title needs that clause to admit the
   opening on the title being **held** live by the claimant (`may_claim` already asks it) — one clause in
   `state/gate.py`, `[ASSUMPTION; medium; revert: Partial = Success]`.
8. `rosters.yaml` and `data/verbs.py`: the five new kinds (`appointment.resisted`,
   `revocation.resisted`, `succession.contested`, and VB-A's `office.unrecognised`, VB-B's
   `pardon.denied`) land with their rows; each is emitted by one row only, so `KIND_VERB` maps it.

**Commit C4 — formation filters and the law.**

9. `rosters.yaml`: `own_title_declines`' note amended, and a sibling roster `seat_belief_declines`
   (`verb: held | vacant`): `revoke: held`, `succeed: vacant`; read in `opening_set` against the newest
   claim naming the seat in his own ledger; loader refuses a member whose row declares no `referent_class:
   Office`. `[ASSUMPTION; medium; revert: drop the roster]`.
10. `data/rosters.py` (the `successions` check beside `state/gate.py::FILLED_BY`): refuse at import an
    office in `offices.yaml` with `conferral: inheritance` and no `successions` key. Today that is one
    seat (`off_king`), which has its row; CP-T09-06's Valorsmark stays `appointed`, so nothing breaks.
11. `verb_table.yaml`, the three rows' notes: one sentence each naming VB-C and its reverts.

Order: C1, C2 (independent), C3 after SC-B, C4 after C3. Selection (CR-88) is not here.

## Gate (execution artifact)

- C2: FA-B4's `recall` scenario on the spine: the Duke's computed `revoke` reaches the roll (a `Resolution`
  recorded), where today it is refused at clause 1.
- C3: FA-P4's `vacancy` and `succession` situations, 40 seeds each: all four bands occur for `confer` and
  `succeed`; a Partial seat falls vacant at `provisional_term` and is offered again (`vacancies`); a
  Failure leaves the seat vacant and the act re-forms. `recall`: `revocation.resisted` occurs at some
  seeds and the Count keeps his seat.
- C4: `aperture 2 0`: no `revoke` formed on a seat the actor believes vacant; no `succeed` formed while
  the heir's newest claim says the King holds. The load clause: plant an `inheritance` seat with no row;
  import fails.

## Falsifier

Pin the roll to Success: C3's band distribution collapses and its gate fails (the instrument can see a
deterministic regression). Revert C2: the `recall` gate shows no `Resolution`. Drop C4's filter: the heir's
refusals while the King sits return.

## What it does not do

It does not make vacancies (FA-P3, FA-B3, deaths), choose who confers (CR-88), build the elected seat's
bench (CR-35) or nomination (CR-36), or decide who may strip the seven `null` seats (FA §11 item 3).

## NERS reading

N: the turnover loop's links are draws now, so a court can resist, a disgraced man can hold on, a claim
can stall. R: provisional seats make legitimacy a thing that is earned twice. S: one prize, one roll, one
Partial shape (a termed hold, matured by the existing MATTER branch). E (last): three band maps and one
term constructor; the player reads "appointed / provisional / resisted".

## Cost class

Medium: three contested rows, one new obstacle term (in SC-B's owner), one fixture pair, two filters, one
load clause, one gate clause.
