# FA-P3 — seats that end: a term on the office row, a refusal for a malformed one, and the scope of a ban

Reconciled: 2026-11-12, U5d closure — folded **A-15** (natural death on), **A-14** (a vote is a draw on the voter) and **A-36**. The first authoring ("the eight `elected` rows at `term: 8`") is withdrawn in favour of `06_FA_seat_terms_by_body_B.md` (the audit addendum's C-6); the mechanism (edits 1–6) stands. With A-15 a seat also empties by its holder's natural death at a rate, so the gate's "a `tenure.opened` after a `term.matured`" gains a sibling reading (an opening after a death) and the vacancy occasion must not assume the term is the only clock. Where a seat is `elected`, the filling is one presiding act whose ballots are draws (A-14), not a plain `confer`. The Confessor's seat takes no term and no removal (A-36: death or resignation only).

Reconciled: 2026-11-12, wave 3 (W3-3) — the body follows the head (R3 §2): "The resolution" paragraph 2 and gate bullet 2 now name `06_FA_seat_terms_by_body_B.md`'s three rows, not "the eight `elected` rows at `term: 8`". C3-C15 and R3 §1 Option A (7b-5 (b)): edit 3 adds no `Office.term` field; the row's `term:` is the default a conferral writes onto the Tenure's `term?` (`04` §B.8 T-n; U1 ledger S-24), read through `SEAT_ROW_BY_ID`, with `declared_by` the confer act, so no hash-fold special case is needed. A-14 (7b-5 (d)): the election act's effect calls the same `_declared_term`. 7b-5 (c): named tests. Tier and batch added (R3 7b-0; U3 C3-D5).

## Status: PROPOSED

Lands in batch: B21 (FA governance), first in C3-D5's order.
Depends on: nothing proposed for edits 1–6 (every symbol named is on `main`); the seeded gate's authoring step is `06_FA_seat_terms_by_body_B.md` (B21, later in the same batch).

Source: `audits/06_FA_audit.md` F-FA-02, F-FA-08, §6.2 R-06 and R-17, §13 (NPC-008, NPC-070, NPC-006,
NPC-009); hole rows H-290, H-294, H-207.

## What it changes in `engine/season/` at runtime

1. A `confer` that declares no term opens the seat-`hold` with the term its office row names, if the row
   names one. MATTER already matures a termed `hold` and closes it (`T-n`); the seat then falls vacant and
   `world_q.vacancies` already offers it to whoever may fill it.
2. A `confer` carrying a malformed term is refused (`confer.refused`) instead of raising out of the fold.
3. A ban bars seats within the banning seat's purview, not every seat.

With no row naming a term (the shipped state of step 1's first commit) nothing moves. Authoring a term on a
row is a data edit and a declared mover.

## The problem (evidence)

At `601e715`, `PYTHONHASHSEED=0` (audit E-3, E-5):

- Realm, seeds 0, 1 and 2, three seasons: `tenure.opened` 0, `succession.claimed` 0; one seat fell vacant at
  each of seeds 1 and 2 (a death) and stayed vacant; the faction view is otherwise identical build to end.
- `aperture 2 0`: `confer` formed for 5 persons, attempted 0.
- The one generator of vacancies the world runs on a clock is a term, and "no computed act declares a term
  for a seat" (H-290): `_declared_term` reads only the act's payload (`loop/effects_governance.py:39-55`),
  which a computed act never carries.
- The same function raises `InstrumentDefect` on a term of `0`, `-1`, `'2'`, `True` or `1.5` (`:50-54`), so
  the first client that lets a player name a term can end a season with a typing error.
- A ban refuses "ANY seat [ASSUMPTION; medium; revert: ask the banning seat's purview]"
  (`effects_governance.py:101-108`, `predicates.py:500-503`) and closes none (H-294).

## The resolution, decided

**The term is the seat's.** How long a post is held is a fact about the post, authored once on its row, as
its conferral and revocation bases are. The opening act may still declare a shorter or longer one (T-n:
"the opening act declares the terms"); where it declares none, the row's stands. This is ladder step 5: the
row is the single owner of every other standing fact about the seat, and the alternative (a ninth operand
so a computed `confer` can carry a number) coins a requires-operand the roster has refused twice.

**Which seats end, and when,** is content. The precedent in hand is shape only: fixed terms and
re-legitimation at each filling recur across the elective and collegiate cases the governance research
gathers, and no source gives a number that transfers. The proposal ships the mechanism with no row termed.
The first authoring is a separate, declared edit owned by `06_FA_seat_terms_by_body_B.md`: three rows
(`off_guild_comptroller`, `off_guild_leader`, `off_commune_rep_hm`) at `term: 4`, swept `{4, 8}`, with the
Confessor, the Duke of Varfell and the Jarls untermed (that file's reasoning; A-36 for the Confessor). A
term is counted in seasons; any statement of it in years reads the declared year (`20_NARRATIVE_E` edit 1,
D-U1-10), never a literal four. Appointed seats are left untermed: an appointee serves at pleasure, and his
exit is the recall of FA-P1.

**A ban is scoped to the seat that pronounced it.** The edge is `ban : person -> seat`; a rule that ignores
the edge's object would make every ban realm-wide whoever issued it. The archived ladder design agrees in
shape (a dismissal bars re-entry "in that branch", `.designs/…/faction_politics_v30.md` §1.0a; intent only).
A ban does not close seats already held: those are protected by `may_revoke`, including the seats ruled
`null`, and a ban that stripped them would be a revocation with no basis.

## Exact edits, by owner

**1. `engine/season/offices.yaml`.** A seat row may carry `term: <positive int> | null` (seasons). No shipped
row does in the first commit.

**2. `engine/season/data/rosters.py::_load_offices`.** Admit the key; refuse a value that is not a positive
whole number or `null`, at load, naming the row. Expose it on the row map `SEAT_ROW_BY_ID` already serves.

**3. No `Office` field (row data, not a `Seat` field; C3-C15).** `04` §B.7's `Seat` tuple is closed, and
`04` §B.8 makes the Tenure's `term?` (declared by the opening act, T-n) the one home of a term. The row's
`term:` is therefore the **default** a conferral writes onto that `term?`, not a second store (U1 ledger
S-24). `state/carriers.py::Office` is unchanged; `harness/populated.py` and `predicates.office_founded_by`
pass nothing new; no hash fold changes.

**4. `engine/season/loop/effects_governance.py`.**
`_declared_term(w, a, off)` returns the act's declared term where the payload names one, else
`Term(w.tick + n, a.id)` where `n = SEAT_ROW_BY_ID[off.id].get("term")` is not `None` (via
`data/rosters.py`; a founded seat has no row and reads `None`), else `None`. `declared_by` is the confer
act, so the Tenure's term cites its author as T-n requires. `_eff_confer` passes the office it already
holds. Where a seat is `elected`, its filling is one presiding act whose ballots are draws (A-14); that
act's effect calls this same `_declared_term`, so an elected seat is termed by the one reader.
`_eff_succeed` is unchanged: an inherited seat is not termed by this edit.

**5. `engine/season/loop/predicates.py::_req_confer`.** Before `may_fill`, read the payload's `term` key
(`TERM_KEY`, imported from the effect's module or moved beside `office_named_by`); if present and not a
positive whole number, `return _refuse("a confer declares a malformed term", ...)`. `_declared_term`'s raise
stays as the backstop for an act that skipped the precondition.

**6. The ban's scope.** One reader: `queries/world_q.py::restrained(w, person, kind)` gains an optional
`at: Optional[str] = None` (a rung). With `at` given and `kind == BAN_KIND` it answers whether some live
ban's seat reaches that rung (`state/gate.py::purview_reaches`, the one owner); without `at` it answers as
today. `_eff_confer` and `_req_succeed` pass the conferred seat's rung; `_req_oblige` passes the sworn
seat's. `detain` is unchanged (custody is not scoped). `[ASSUMPTION; medium; Jordan to correct; revert:
drop the argument at the three call sites]`, replacing the three existing `[ASSUMPTION]`s that name this
revert themselves.

## Gate (execution artifact)

- Hand-built, real fold: a `confer` with no declared term onto a row-termed seat opens a `hold` whose term
  matures at `tick + term`; MATTER closes it with a citing `tenure.closed`; the vacancy appears among the
  conferrer's classed referents the following season.
- Seeded, after the three rows of `06_FA_seat_terms_by_body_B.md` are termed: realm, seeds 0 to 2, twelve
  seasons, `fa_probe`'s per-season
  line: at least one `term.matured` on a seat-`hold` per seed, and the count of `tenure.opened` on a seat
  that matured. That count is **read and reported**. If it is zero, the term generates vacancies nobody
  fills and the remaining obstacle is selection and the question slot (audit F-FA-02 (b), (c)), which this
  proposal does not claim to move.
- A banned man is refused a seat under the banning seat's purview and admitted to one outside it.

Named tests (7b-5 (c)), new file `engine/season/tests/test_fa_seat_terms.py`:
`test_a_confer_with_no_term_onto_a_row_termed_seat_opens_a_termed_hold`,
`test_malformed_terms_0_minus1_str_true_float_each_refuse`, `test_a_ban_is_scoped_to_the_banning_seats_purview`,
`test_term_null_reproduces_the_hash`, and (A-15) `test_a_seat_emptied_by_a_death_is_offered_as_a_vacancy`.

## Falsifier

- Control: every `term: null` reproduces the pre-item `content_hash` at build and at one and two seasons.
- Mutation: `_declared_term` ignoring the office reddens the hand-built gate.
- The malformed terms `0`, `-1`, `'2'`, `True`, `1.5` each emit `confer.refused` and the season completes.
- The ban: with the scope removed, the "admitted outside it" arm reddens.

## What it does not do

No election (CR-35), no rank, no automatic refill. It does not make anyone choose to `confer`; it makes
there be something to confer on a schedule.

## NERS reading

- **N.** Vertical: realm seats and hearth seats end by the same rule. Lateral: an expiring seat is the
  occasion CR-35's election needs and does not itself supply. Without it the only vacancies are deaths:
  two in nine realm seasons over three seeds.
- **R.** Drama with no player: offices fall open on their own. Strategic: a holder near his term's end and a
  conferrer who can wait are choices the world did not have. Complete at the extremes: a term of one season
  is lawful; a malformed one refuses.
- **S.** No new clock: `T-n` maturation at MATTER is the existing one, and the term is read where the
  `oblige` term already is.
- **E, last.** One optional key, no new field, one changed reader, one refusal, one scoped argument.

## Cost class

Small build (steps 1 to 5 hash EQUAL at ship; the row authoring and step 6 are declared movers, each its own
commit). Tier: `sonnet` (R3 7b-0; the placement choice was made once in U3, C3-C15).
