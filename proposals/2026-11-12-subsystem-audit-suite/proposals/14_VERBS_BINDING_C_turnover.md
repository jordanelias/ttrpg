# VB-C — seats change hands by a draw: an appointment can be resisted, a revocation withstood, a claim contested

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-25, C-31, C-35) — the term `standing` is the roster member `rank_gap` (licensed by Jordan's A-12; the word `standing` already names a prize). Edit 3's audience is `heard_by: seat_body` on the prize row. `revoke` reads `reception` and not `regard`: a row has an audience or a single hearer, never both. §3's Partial for `succeed` opens termed seats under the existing claim basis and lays the title down; the variant that keeps the title needs a gate basis `04` §C.2 does not list and is not built. §2's `revoke` draw carries A-35 (the head strips an officer by a resistible draw).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head's corrections applied to the body (`unified/work/R4_READ.md` §1.1, §2, 7b.3): `standing` → `rank_gap` and `standing_step` → `rank_step` throughout (U1 R-21; the fixture is OBS's, not created here); `revoke` reads `reception`, not `regard`; edit 7's `state/gate.py` clause deleted and `succeed`'s Partial rewritten (C-31); `succeed`'s opposition and audience under A-19; gate C3 read with natural death on (A-15); the pool sentence follows U1 D-U1-01 (a seat helps as the `office` level, never as dice); `provisional_term` stays this file's one fixture at 2 (F-R4-10: U1 F-33 and U3 §11 each passed the value to the other; taken by ladder step 4, `15_INSTITUTIONS_SYNTHESIS_A`'s "`provisional_term` is VB-C's"); A-63/A-64 (C3-C13), A-81 (C3-C11), A-30 keys; U3 batch B21 and C3-D5's commit order; R4 7b.0 block. The Failure kind names stay this file's (F-R4-11; the BYZANTINE heads defer to them).

## Status: PROPOSED

Lands in batch: B21 (`unified/U3_DEPENDENCY_ORDER.md` §3.1). Inside B21 (C3-D5): after `14_VERBS_BINDING_A` and `U5d_FA_owed_edits` §2; the mutual pair with `06_FA_decree_binds.md` and `16_PESSIMIST_FA_C` lands in one commit order: this file's `revoke` draw at control, then the decree, then FA_C's command predicate, then this file's flip.
Depends on: `05_SC_obstacle_difficulty_and_modifiers_B.md` and `U5c_SC_one_obstacle_form.md` §4 steps 0–2 (B05: `difficulty`, `reception`, `stakes`; `rank_gap` with `rank_step` lands with BINDING_A in B21); `U5c_VERBS_residue_and_governance_owner.md` §2 (B07: the `a seat` row, `audience_of`); `06_FA_seat_terms_and_turnover.md`, `06_FA_remit_grant_by_row.md`, `06_FA_playable_scenario.md`, `06_FA_decree_binds.md`, `14_VERBS_BINDING_A_formation.md` (all B21).
Lane: FA. Tier (R4 7b.0 (1)): C1, C2, C4 `sonnet` producer, effort `high`; C3 (three contested rows and their obstacle terms) `opus` producer; one `opus` read of the 40-seed band tables. Test file: `engine/season/tests/test_vb_c_turnover.py` (one function per gate C2–C4).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's trained score (A-6), talent as levels (A-7), a wound a level against the roll (A-8). Each draw takes `H(w.world_seed, w.tick, <actor id>, "<verb>.seat")` for `confer`, `revoke`, `succeed` (A-30). A-12's licence for `rank_gap` stands only once the owed `04` §B.7 amendment (drafted in U1 D-U1-01) is applied; never by editing `04`. A-63/A-64 (C3-C13): a conferral, a revocation and a claim heard by the seat's body occupy the conferee, the holder and the claimant for the round; precedence, appointments and the waiting petition are `28_CORE_scene_access_A`–`C`'s, read and not restated.

Source: `audits/14_VERBS_BINDING.md` §0.2, §1 (`confer`), §11 (`revoke`), §12 (`succeed`); batch C.
Binds on, and does not redo: `06_FA_decree_binds.md` (FA-P1; its change 4 is this file's edit 5),
`06_FA_seat_terms_and_turnover.md` (FA-P3), `06_FA_seat_terms_by_body_B.md` (FA-B3),
`06_FA_shortest_loop_B.md` (FA-B4, the gate), `06_FA_playable_scenario.md` (FA-P4), CP-T09-06, CR-35,
CR-36, CR-88 (selection). Cross-lane reads of `U5c_SC_one_obstacle_form.md` (OBS): the obstacle member
`rank_gap` (member 6, fixture `rank_step`) and the audience operand on `reception` (VRES §2's
`audience_of`); nothing is requested beyond what those owners already carry.

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
binding precedent, its degree keyed writes the table's own method). Pool: the one pool rule on the actor's
trained score in the capability the row names (the governance vocations of FA-P6); the seat he exercises
helps him only as the `office` leverage level read off that seat row's `modifier:` (U1 D-U1-01, A-12),
never as dice. Obstacle, through the one composer (`U5c_SC_one_obstacle_form.md`):

| row | `difficulty` | `opposition` | other terms |
|---|---|---|---|
| `confer` | `routine` | the incumbent, only when displacing | `reception` (audience: the seat's body), `rank_gap` (the conferee against the seat), `stakes` `hold` |
| `revoke` | `routine` | the holder | `rank_gap`, `stakes` `hold`, `reception` (the seat's body); no `regard` (a row with an audience reads `reception` only, C-35) |
| `succeed` | `routine` | a docketed rival claimant where one exists, else none (A-19: heir, consort, princess and both houses' heads may claim one empty seat) | `reception` over three audiences, each reading `legitimacy(q, claimant, seat)` (`15_INSTITUTIONS_BYZANTINE_E` e1; the seat's body, or the realm's seated persons for a seat with no body), `rank_gap`; `may_claim` widened to the A-19 claimants by BYZ_E e2 (CR-35) |

**The bands**, one shape for the family: Overwhelming and Success do the act; Partial does it
provisionally (a seat-opening act opens a termed hold; `revoke`'s Partial unseats without the disposal);
Failure writes nothing on the seat and emits its own kind, and the act may be tried again.

**`rank_gap`** is the term the family needs: how far the person acted on (or for) stands above the
exercised seat. It is OBS §2 member 6 with its fixture `rank_step`, control 0 (U1 R-21), read off
`rosters.yaml: rung_kinds`' order through the gate's rank reader (the one `rank` stem); it lands with its
first reader, `14_VERBS_BINDING_A_formation.md` commit A3, earlier in B21. This file adds no member,
operand or fixture for it.

**The ledger filters** take `own_title_declines`' route: person-side, the newest claim in his own ledger
naming the seat (`LedgerReader`'s comparator), `tenure.opened`/`succession.claimed` → held,
`tenure.closed` → vacant.

## Exact edits, by owner

**Commit C1 — the shared parts.**

1. `engine/season/data/fixtures.py`: `provisional_term` (proposed 2 seasons; sweep {1, 2, 4}; control:
   Partial = Success), with a NUMBER row in `hole_register.yaml` (the one `provisional_term`; the
   BYZANTINE files cite it and ship no second value, F-R4-10). `[ASSUMPTION: 2 is uncalibrated; it enters at
   control and the joint re-centring (OBS §4 step 5) or the story census sets it — basis: R4 §2 on A-5,
   A-6, A-7, A-26]`. `rank_step` is OBS member 6's fixture, landed by BINDING_A commit A3, not this file.
2. `loop/effects_shared.py`: `_provisional_term(w, a) -> Term`, `_new_oblige_term`'s shape
   (`Term(w.tick + w.fixtures["provisional_term"], a.id)`), the one constructor of a Partial's term.
3. *(Was an SC-B request; now carried by its owners.)* `rank_gap` is OBS §2 member 6; `reception`'s
   audience is VRES §2's `audience_of(w, act, room)` over the prize row's `heard_by: seat_body`. No edit here.

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
   `Tenure.since` at O/S, `Tenure.until`, `Tenure.since`, `Tenure.term` at Partial (each seat opened
   termed; the title laid down, as at Success), `[]` at Failure; emits `succession.claimed`,
   `tenure.closed` at O/S/P, `succession.contested` at Failure. `_eff_succeed`: at `Partial` open each seat
   with `term=_provisional_term(w, a)` under the existing claim basis, licensed by the title's closure in
   the same write (`refuse_unauthored`'s second pass), exactly as at Success. *(W3-4a, C-31: the variant that
   kept the title needed a `state/gate.py` clause `04` §C.2 does not list, "the current, complete test";
   it is deleted, not built.)* `[Corrects R4 7b.3, which listed the Partial writes as `Tenure.since`,
   `Tenure.term` only: laying the title down is a `Tenure.until` write, as R4 §1.1's row says.]`
8. `rosters.yaml` and `data/verbs.py`: the five new kinds (`appointment.resisted`,
   `revocation.resisted`, `succession.contested`, and VB-A's `office.unrecognised`, VB-B's
   `pardon.denied`) land with their rows; each is emitted by one row only, so `KIND_VERB` maps it.
8a. **Durable write of every Failure band (A-81; C3-C11).** `appointment.resisted` is witnessed by the
   seat's body (the `reception` audience) and the conferee; `revocation.resisted` by the seat's body and
   the holder; `succession.contested` by the seat's body and the rival claimants present. Each deposits a
   claim of the Event to those witnesses (the `co_located` channel), so a failed turnover is a remembered
   deed and a lasting grievance, never a still scene.

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
  seeds and the Count keeps his seat. The "`succeed` formed 0" evidence above predates A-15 (natural death
  on): the C3 gate is also read on a realm run with the age pass live (`22_HAPPENINGS_A` edit 1's ages,
  owed by A-15), where `succeed` is reachable in ordinary play; until the ages are authored that arm is
  marked not run.
- C4: `aperture 2 0`: no `revoke` formed on a seat the actor believes vacant; no `succeed` formed while
  the heir's newest claim says the King holds. The load clause: plant an `inheritance` seat with no row;
  import fails.

## Falsifier

Pin the roll to Success: C3's band distribution collapses and its gate fails (the instrument can see a
deterministic regression). Revert C2: the `recall` gate shows no `Resolution`. Drop C4's filter: the heir's
refusals while the King sits return.

## What it does not do

It does not make vacancies (FA-P3, FA-B3, deaths), choose who confers (CR-88), build the elected seat's
bench (CR-35) or nomination (CR-36). Who may strip the `null` seats (FA §11 item 3) is answered by A-35
for Church officers (the head strips by a resistible draw, carried as `revoke` here through the
`head_of_faction` revocation basis of `15_INSTITUTIONS_PAPACY_B` item 4); Löwenritter stay unstrippable
until they have a head seat.

## NERS reading

N: the turnover loop's links are draws now, so a court can resist, a disgraced man can hold on, a claim
can stall. R: provisional seats make legitimacy a thing that is earned twice. S: one prize, one roll, one
Partial shape (a termed hold, matured by the existing MATTER branch). E (last): three band maps and one
term constructor; the player reads "appointed / provisional / resisted".

## Cost class

Medium: three contested rows, one fixture (`provisional_term`), two filters, one load clause. (The
obstacle term and its fixture are OBS's; the gate clause is deleted.)
