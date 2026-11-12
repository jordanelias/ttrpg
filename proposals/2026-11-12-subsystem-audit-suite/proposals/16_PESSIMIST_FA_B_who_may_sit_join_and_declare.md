# PES-FA-B — who may sit, who may join, who may declare: three eligibility checks the engine does not ask

Reconciled: 2026-11-12, U5d closure — folded **A-19**, **A-20** and **A-58**. Decision 1 (`may_sit`: an individual) is the first eligibility of the deed race and of a conquest's seats (a cohort taker leaves the seat vacant). Decision 2 stands and the "Jordan call of §5 for the crown's fallback" is answered (the race). Decision 4 (a war has two parties and a declarer of one) composes with A-20: the declarer must also be able to wage it for the declaration to be de jure (`may_wage`, `06_FA_war_lives_in_seats_B.md` edit 1); a member's WAR utterance without a muster seat is a call for war, not a war. No step is deleted.

## Status: PROPOSED

Source: `audits/16_PESSIMIST_FA.md` F-PES-FA-01, -04, -05 (premises P2, P3, P4; runs `pf2_premise.py` P2 to
P4 and `pf2b_followup.py` §2, §3, §7, §8, seed 0). Binds on, and does not redo:
`14_VERBS_BINDING_C_turnover.md` (the seat draws), `14_VERBS_BINDING_E_war_seats.md` and
`06_FA_war_lives_in_seats_B.md` (whose commit keeps a war de jure), `06_FA_remit_grant_by_row.md` R-16 (the
Queen consort's remit), `15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md` (`may_seat`, `eligible_from`),
`15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` (who elects the Confessor), CR-35.

**On the standing rule.** Everything below is an eligibility check: whether an act may be attempted at all
(`AUDIT_BRIEF.md`: "a person cannot sit a seat he does not hold"). None fixes an outcome. Where the act is
attempted, its outcome is the sibling proposals' draw.

## What it changes in `engine/season/` at runtime

1. A cohort (a village, a ward) cannot be named to a seat or claim one. Today a peasant cohort can be made
   heir and then King.
2. A `confer` across ladders (the exercised seat's faction is not the seat's) is harder, by a named
   obstacle term, once `confer` draws; and a holder cannot confer a seat on himself through a seat that is
   not above it in the same ladder.
3. Joining a faction is an offer the faction's side answers, not a sentence the joiner speaks. Today the
   King joins the insurgents by saying so and the insurgents' view gains the realm's holdings.
4. A `WAR` Proposition is formed only between two different factions that exist, by a member of one of
   them. Today a peasant cohort puts Hafenmark and Varfell at war, and Hafenmark can be at war with itself.

Movers: (1) and (4) move no shipped run (nothing computed does either today; verified for (4) by `at_war`
empty at every seed, for (1) by `tenure.opened` 0). (3) moves every run in which a person commits to a
faction Proposition he is not already in; the count is the gate's first reading.

## The problem (evidence, by execution, `build_realm(0)`)

- **The Crown is among the fillers of every fillable seat.** Of 34 seats, 26 can be filled by a seat
  whose row grants `confer`; `off_king` and `off_widow_regent` are fillers of all 26, the Church's six,
  the Restoration Movement's leader and Varfell's four included (`pf1`, grant-filtered). The Rebel leader
  dies: no member of the Movement can fill the seat; the King confers it on his Guard Captain,
  `tenure.opened`. The Confessor dies: no Cardinal can fill it (`confer.refused` × 4); the King confers
  it on his Guard Captain, `tenure.opened`, and `faction_q.head` reads the Guard Captain as head of the
  Church; the Queen consort confers it on herself through `off_widow_regent`, `tenure.opened`.
- **A cohort can be King.** The King and the heir die; the Queen consort names `cohort_set_s_001` heir
  (`tenure.opened`); the cohort's `succeed`: `succession.claimed`; `off_king` is held by the cohort.
- **Membership is a unilateral sentence.** `commit` to a faction Proposition is `own`-eligible, uncontested
  and unanswered: a stranger joins Valorsmark, a peasant cohort joins the Church, the King joins the
  Restoration Movement (its view then reads 3 seats and 6 holdings), the Duchess of Hafenmark joins Varfell
  while still in Hafenmark (`commitment.made` each). The Duke of Varfell leaves Varfell and joins
  Hafenmark: Varfell's holdings 4 → 0, Hafenmark's 4 → 8.
- **Anyone declares war for anyone.** `utter` of mood `WAR` then `commit`: `at_war(Hafenmark, Varfell)`
  true when the declarer is an unseated person in no faction, a peasant cohort, the King, or a clerk;
  `at_war(Hafenmark, Hafenmark)` true; a war between `fac_does_not_exist` and a person: true.

## The resolution, decided

| # | decision | ladder step |
|---|---|---|
| 1 | **A seat is held by an individual.** One predicate, asked where `may_fill` and `may_claim` are asked: the person who would own the opened seat-`hold` is not a cohort. If VENICE-C's `may_seat(w, off, person)` lands first, this is its first conjunct and no second predicate is written | 5; 4 (`Person.is_cohort` already splits the two kinds of agent) |
| 2 | **Cross-ladder conferral is admitted and priced.** `may_fill` is not narrowed: until an election arm exists (CR-35, PAPACY-B, VENICE-C), narrowing leaves the Church's head and Varfell's duke filled by nobody, which is worse. What changes: VB-C's `confer` obstacle gains one term, `ladder`, a step harder by a fixture when `office_faction(via) != office_faction(off)`, and the opposition is then the seat's body (VB-C already reads `reception` with that audience). **And the self-conferral is refused across ladders**: `to == actor` is admitted only where the exercised seat and the conferred seat are of one faction | 3 (VB-C's table; `counterparty_may_be_self` is D2's, kept inside a ladder), 5 |
| 3 | **Joining is `covenant`'s shape, not `commit`'s alone.** A `commit` to a faction Proposition by a non-member is admitted when a live member whose seat-grant carries `confer`, or the faction's `head_seat` holder, has `commit`ted to a Proposition naming the joiner (an admission the joiner's own ledger holds). Where a faction has no such seat (the Guilds, Schoenland, Altonia, an unrostered party), any live member's admission serves. Leaving stays the member's own `release` (AX-1). A member of one faction may hold a second membership only where `rosters.yaml` says the pair is compatible; the default for two rostered factions is incompatible | 4 (`covenant`: two commits make it in force; `terms_sourced` forms a commit from a held paper), 5 |
| 4 | **A war has two parties and a declarer who belongs to one.** `utter` of mood `WAR` is refused unless `subject != value`, both are Propositions with at least one live `commit`, and the utterer is a live member of one. Which commit keeps the war de jure is `06_FA_war_lives_in_seats_B.md`'s and is not re-decided | 3 (`10_FACTIONS_AND_DEPLOYMENT.md` §2: a war is between factions), 5 |

Held back, as a ruled item (R-16 is the FA lane's proposal; the consort's remit is a provided-character
reading): the Queen consort's `off_widow_regent` row. See "Interaction" below.

## Exact edits

1. **`engine/season/state/gate.py`**: `def may_sit(w, person_id) -> bool`: the person exists and
   `not w.persons[person_id].is_cohort`. Asked in the `conferral` and `claim` clauses of
   `tenure_write_basis` (the subject of the opened seat-`hold`), and by `loop/predicates.py::_req_confer`
   (of `to`) and `_req_succeed` (of the actor) through the same name, so the fold refuses
   (`confer.refused`, `succession.refused`) where the gate would raise. `decision/options.py`'s counterparty
   fan for `confer` drops cohorts through the same predicate (formation follows admission).
2. **`engine/season/loop/predicates.py::_req_confer`**: after the existing `may_fill` conjunct, refuse
   (`_refuse("self_across_ladders", …)`) when `to == a.actor` and
   `w.offices[a.via].faction != w.offices[obj].faction` (`Office.faction` is the resolved faction,
   `gate.py:505-507`). **`14_VERBS_BINDING_C_turnover.md`'s obstacle table**, row `confer`: add the term
   `ladder` (`cross_ladder_step`, fixture, control 0, proposed 2), read by SC-B's one obstacle owner. This
   file requests the term of that owner; it does not edit the table.
3. **`engine/season/rosters.yaml: terms_sourced`**, cell `commit`: add the admission source (a
   Proposition of mood `OUGHT` whose `subject` is the joiner and `value` the faction Proposition, held as
   a claim in the joiner's ledger and `commit`ted to by an admitting member).
   **`engine/season/loop/predicates.py`**: `commit`'s precondition (the row is typed; the conjunct is a
   `relation` cell of stem `admitted`, owner `queries/world_q.py::admitted_to(w, person, prop)`): true when
   `prop` is not a rostered faction Proposition and has no live member, or the person is already a member,
   or an admission stands. **`rosters.yaml: factions`**: a `compatible_with:` list per row, default empty.
4. **`engine/season/verb_table.yaml`, row `utter`** (`requires: "—"` today, no cell) and
   **`engine/season/loop/predicates.py`**: a registered precondition `_req_utter` (the untyped route
   `_req_confer` and its siblings use), true for every mood but `WAR`; for `WAR`: `subject != value`;
   `world_q.members(w, subject)` and `members(w, value)` both non-empty; the actor in one of them. The row
   gains `emits_on_refusal` if it has none `[UNVERIFIED: the row's refusal column was not read]`. The
   `commit` cell of edit 3 joins `commit`'s existing typed `requires` ("the Proposition exists"); the stem
   name `admitted` is this file's proposal, not an existing stem.

## Interaction with a sibling proposal (named, not resolved here)

`06_FA_remit_grant_by_row.md` R-16 sets `off_widow_regent.remit_acts: []` while the King lives. Measured
consequence: with the King and the heir dead, the only seats able to fill `off_heir` are `off_king` and
`off_widow_regent` (`pf1`); with the consort's `confer` gone, **nobody can ever name an heir and nobody
can ever claim the throne** (the same end state `pf2b` §7 reaches by killing all three). R-16 is right
about the living King; it needs the fallback PES-FA-C carries (or the regency it mentions, conferred by
someone who exists), or it moves the realm's dead end one death earlier.

## Gate (execution artifacts)

Re-run `pf2_premise.py 0`, `pf2b_followup.py 0`:

- **G1** the Queen names a cohort heir: `confer.refused`; control, she names an individual:
  `tenure.opened` (or VB-C's band).
- **G2** the Queen confers the Confessor's seat on herself: `confer.refused` (`self_across_ladders`);
  control, the King confers the heir's title on himself (one ladder): admitted as today.
- **G3** the King's `commit` to the Restoration Movement with no admission: refused; with a member's
  admission in his ledger: `commitment.made`. Control: a member's re-commit and every non-faction `commit`
  are unchanged. First reading before the edit: over seeds 0 to 2, three seasons, how many executed
  `commit`s are a non-member's to a rostered faction (if zero, edit 3 moves no shipped run and its gate
  is the hand-built pair only).
- **G4** a cohort's, a stranger's and a clerk's `WAR` between Hafenmark and Varfell: refused; the Duchess of
  Hafenmark's: `proposition.uttered`; `WAR(Hafenmark, Hafenmark)`: refused.
  `test_at_war_through_the_real_fold_utter_then_commit_then_release` (`tests/test_faction_q.py`) declares
  through a Valorsmark member and stays green.

## Falsifier

G3's first reading: if computed play today contains non-member commits to factions that other persons
then act on, edit 3 removes live behaviour and its cost must be stated before it lands. G2 is wrong if a
regency is meant to be exactly this act (a consort taking a vacant seat of another ladder); the provided
character NPC-032 says she has no action economy of her own, which is why it is refused here.

## NERS reading (E last)

- **N.** Top-down: a faction that cannot refuse a member is not a body. Bottom-up: a cohort on a throne
  breaks every reader that expects a seat-holder to be an individual (the sheet, the bench, the duel).
  Lateral: `at_war`'s one reader (`enemies_heard`) and the planned muster both trust the pair. Cut these
  checks and what dies is the meaning of three words: member, heir, war.
- **R.** Defection becomes a two-sided story (an admission sought, granted, refused) instead of a
  sentence. The extremes are closed: self-war, a war on nothing, a throne held by a village.
- **S.** `commit`-to-join reuses `covenant`'s two-commit shape and `terms_sourced`; no new ladder.
- **E, against that.** One predicate, one conjunct, one relation stem, one cell. The largest piece is
  edit 3; if G3's first reading is zero it can wait for the first scenario that needs defection.

## Cost class

Edits 1, 2, 4: edit. Edit 3: small build (one Query, one roster key, one typed cell).
