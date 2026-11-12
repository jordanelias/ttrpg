# FA-P3 — seats that end: a term on the office row, a refusal for a malformed one, and the scope of a ban

## Status: PROPOSED

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
gathers, and no source gives a number that transfers. The proposal ships the mechanism with no row termed,
and names the first authoring as a separate, declared edit: the eight `elected` rows at `term: 8` (two
years of seasons), swept `{4, 8, 12}` `[ASSUMPTION; medium; Jordan to correct; revert: no `term:` keys]`.
Appointed seats are left untermed: an appointee serves at pleasure, and his exit is the recall of FA-P1.

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

**3. `engine/season/state/carriers.py::Office`.** A field `term: Optional[int] = None`, validated in
`__post_init__` with the same rule, folded into the office's hashed representation only when it is not
`None` (so an untermed world's hash does not move). `harness/populated.py` passes the row's value at build;
`predicates.office_founded_by` passes `None` for a founded seat.

**4. `engine/season/loop/effects_governance.py`.**
`_declared_term(w, a, off)` returns the act's declared term where the payload names one, else
`Term(w.tick + off.term, a.id)` where the office names one, else `None`. `_eff_confer` passes the office it
already holds. `_eff_succeed` is unchanged: an inherited seat is not termed by this edit.

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
- Seeded, after the eight rows are termed: realm, seeds 0 to 2, twelve seasons, `fa_probe`'s per-season
  line: at least one `term.matured` on a seat-`hold` per seed, and the count of `tenure.opened` on a seat
  that matured. That count is **read and reported**. If it is zero, the term generates vacancies nobody
  fills and the remaining obstacle is selection and the question slot (audit F-FA-02 (b), (c)), which this
  proposal does not claim to move.
- A banned man is refused a seat under the banning seat's purview and admitted to one outside it.

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
- **E, last.** One optional key, one field, one changed reader, one refusal, one scoped argument.

## Cost class

Small build (steps 1 to 5 hash EQUAL at ship; the row authoring and step 6 are declared movers, each its own
commit).
