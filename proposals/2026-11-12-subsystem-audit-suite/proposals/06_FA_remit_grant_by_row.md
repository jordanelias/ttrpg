# FA-P2 — a seat grants what its row names: `dispatch` by row, a row for the unauthored seat, the consort's remit

## Status: PROPOSED

Source: `audits/06_FA_audit.md` F-FA-03, §6.2 R-04 and R-16, §13 (NPC-032, NPC-034, NPC-036, NPC-072,
NPC-082), §15 (c); `engine/season/offices.yaml` J-8.

## What it changes in `engine/season/` at runtime

`harness/populated.py::build_realm` stops keeping `dispatch` on a seat whose `offices.yaml` row does not name
it. Seats that command keep `dispatch` because their rows say so; the others lose `dispatch` and with it
`march`, `capture`, `arrest`, `raze`, `marshal` and `surrender`. NPC-084's seat is built from a row instead
of from the testing default. The queen consort's seat grants nothing while the King lives. Every one of
these is a hash mover for the realm (`Tenure.granted_acts` and `Office.remit_acts` are hashed) and is
declared as such; the spine and the corpus worlds do not read `offices.yaml: seats` and do not move.

## The problem (evidence)

`aperture 2 0` at `601e715`, `PYTHONHASHSEED=0`, realm (audit E-3):

- 26 of 33 seated persons are eligible for `march`. The 13 acts that emitted `march.declared` were made by
  the Guilds' economic representative, the Lord Treasurer, the Legal Advisor and the Skald-Chief. No row of
  theirs names `dispatch`.
- `p_npc_084`, whose seat no row authors, reads `grant [confer, convene, determine, dispatch, issue, revoke]
  · eligible 67 of 67`: the King's aperture, from `rosters.yaml: remit_default`, on a seat with no rung.
- `p_npc_032` (the queen consort) reads `eligible 67 of 67` and executed `convene` and `dispatch`. Case
  NPC-032's first `core` need is that she has "no independent action economy of her own".
- The file states the cause itself (`offices.yaml:104-123`): `dispatch` is kept through
  `meta: remit_unruled`, so "identical rows diverge by BUILD ROUTE": a loop-built seat keeps it, a minted
  seat does not.

## The resolution, decided

J-8 asked whether `dispatch` is a remit act at all. It stays one: seven verb rows and four gate bases
(`WARRANT_ACT`, `MUSTER_ACT`, `CESSION_ACT` in `state/gate.py`) are keyed on it. What is decided is who holds
it: **a seat holds a remit act if and only if its row names it.** Ladder step 4: the file's own
`foreign_seats` rows already name `dispatch` explicitly, a minted row already "holds only what it names",
and IN-64 authored two rows by precedent for seats the loop had built without one.

Which posts command is content. The assignment below takes the posts whose titles or sources say they
command or keep order; each is `[ASSUMPTION; medium; Jordan to correct; revert: restore the
`remit_unruled` line, one re-pin]`.

## Exact edits, by owner

**1. `engine/season/offices.yaml`** (the one owner of a seat's grant).

- Delete `meta: remit_unruled: [dispatch]` and the header paragraph that explains it (`:104-123`), leaving
  one sentence: a seat's remit is its row's.
- Add `dispatch` to `remit_acts` on: `off_king`, `off_duke_valorsmark`, `off_duchess_hafenmark`,
  `off_duke_varfell` (rulers send and muster); `off_royal_marshal`, `off_guard_captain`,
  `off_military_commander_hm`, `off_military_jarl`, `off_grand_master` (command posts);
  `off_riskbreaker_covert`, `off_riskbreaker_doctrine` (operatives who are sent and who take people);
  `off_senior_inquisitor`, `off_cardinal_justice` (an inquisition arrests on a warrant). `off_katepano`
  already names it.
- `off_widow_regent`: `remit_acts: []`, with a note that the consort's powers arrive with a regency, which
  is a termed `confer` or the heir's claim, never a standing grant.
- `off_archbishops_rep`: `remit_acts: [issue]`, so the one Church seat on Crown ground can write the
  warrant an inquisitor acts on there (case NPC-034's conduit; the purview it needs is already his rung).
- A new row for NPC-084's seat, after `off_guild_comptroller`: `id: off_guild_leader`, `post: "Guild
  Leader"`, `rung: {duchy: "Hafenmark"}`, `body: "Guild"`, `faction: null`, `remit_acts: [convene]`,
  `conferral: elected`, `revocation: rung_above_same_faction`, `holder: "NPC-084"`, `obligees: []`. The
  anchor, body and bases follow `off_guild_comptroller` (the other Guild seat); `convene` because a guild
  leader calls the forum.

**2. `engine/season/data/rosters.py`.** Delete `OFFICES_REMIT_UNRULED` and its membership check
(`:926-935`).

**3. `engine/season/harness/populated.py`.** `authored_remit(row, held)` returns the row's `remit_acts` and
no longer unions the kept acts (`:1723-1726`); the `unauthored` branch (`:1736-1740`) stays for a future
seat with no row and is no longer reached by the shipped cast.

**4. Tests that read the old state** (named so the builder re-records rather than discovers; both are taken
from the notes that describe them, `offices.yaml:122-123` and the FA-01 handoff row, and were not opened:
[UNVERIFIED]):
`test_season_shape.py`'s remit-default test asserts `not ungranted`; a seat with an empty remit becomes
lawful (the heir, the princess, the consort hold titles, not powers), so that assertion narrows to "every
seat's grant equals its row's". `test_fa01_head_seats.py` reads each head executing a computed `dispatch`
through his seat: the Restoration leader's row names only `issue`, so his arm re-records on `issue`.

## Gate (execution artifact)

`python -m engine.season.harness.aperture 2 0`, realm, PER HOLDER:

- every person with `x`, `a` or `r` under `marc` holds a seat whose row names `dispatch`;
- `p_npc_084` reads `grant ['convene']`; `p_npc_032`'s nineteen seat-gated cells read `-`;
- the count of persons eligible for `march` falls from 26 to the number of rows naming `dispatch`.

## Falsifier

- Mutation: restore the `remit_unruled` line and the first gate line fails at seed 0 (the treasurer marches).
- Control: the spine's block of the same run is byte-identical before and after.
- Reported, not asserted: `march.declared`, `order.given` and `army.arrived` counts pooled over seeds 0 to 2
  before and after. If no command seat marches in three seeds, that is a finding about selection (audit
  F-FA-05), and the edit stands: a war nobody with the right to wage it chooses is the truthful reading.

## What it does not do

It does not split `dispatch` into a command act and a messenger act; `rosters.yaml: remit_acts` is closed,
and the split is one constant per gate basis if ever ruled. It does not decide the unauthored content the
cases flag as UNCLEAR (NPC-036's goals, NPC-072's territory).

## NERS reading

- **N.** Top-down: the Crown's command runs through named posts. Bottom-up: a clerk cannot raze a village.
  Laterally: two seats on one rung now differ in what they may do. Removing the edit returns a realm in
  which a post's title predicts nothing.
- **R.** Customization by data: a designer changes who commands by editing a row. Completeness: a seat with
  an empty remit is lawful and inert.
- **S.** One rule for every seat and both build routes, which is the consistency the placeholder broke.
- **E, last.** Net deletion: one meta key, one loader constant, one union. One row added.

## Cost class

Edit. Declared hash mover for `build_realm`; goldens re-recorded old to new in the commit body.
