# PAPACY-A — the Church stands on its own ground: the Confessor at Himmelenger, the Templars' command by row, the realm benches, and CR-74's carrier named

Re-grounded: 2026-11-12 (audit §15) — no edit of this file changes. One fact bears on it: at `build_realm(0)` the Church seats that carry `determine` are `off_confessor`, `off_cardinal_justice` and `off_senior_inquisitor` (map `unified/RESEARCH_MAP_INSTITUTIONS_A.md` §5, E-M1). Those are this file's three realm benches, and under the rule in force (`workplans/valoria_master_workplan_v11_part12.md:366`) the last two are also the whole electorate of the Confessor: audit §15.3 C-1.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_PAPACY.md` F-PAP-01, F-PAP-04, F-PAP-08, F-PAP-10; §12 R-1, R-4, R-5,
R-14; evidence E-1, E-2. Batch 1 of that file's §11. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. NPC-021 (the Confessor) is built at the cathedral of Himmelenger instead of a market in `terr_T1`. A
   declared build-hash mover (one person's `contain` and `reside` edges and whom he is co-located with).
2. `off_cardinal_fortitude` grants `dispatch` by its own row. Nothing moves while the unruled `dispatch`
   is kept on every loop-built seat (`offices.yaml: meta.remit_unruled`); it is the row that keeps the
   Church's military arm in command once FA-P2 (`06_FA_remit_grant_by_row.md`) removes the blanket grant.
3. Once CR-60's `scope:` key exists: three Church seats judge realm-wide. A declared mover (which seat
   may open a case or sit on a bench), inside CR-60's own re-record.
4. The CH strife code gains a signature. Harness only; `content_hash` EQUAL.

## The problem (evidence)

- `npcs.yaml:192-200`: `case: NPC-021`, `institution: null`, `home: b_s_003_market`, `tie: neighbour`.
  At `build_realm(0)` his `contain` chain is `b_s_003_market → q_s_003_market_quarter → set_s_003 →
  terr_T1` (E-2). The six other Church seat-holders are under `terr_T9`. The generator classes a case's
  institution by the words of its text (`harness/populated.py::institution_of`); his case text names no
  institution, so he was housed as an unaffiliated life. The file's header says a wrong home is a one-row
  hand edit.
- `offices.yaml:382-393`: `off_cardinal_fortitude.remit_acts: [issue, convene]`. Its body's note:
  *"Military. Knights Templar, enforcement, monstrous incursion suppression"* (`rosters.yaml:2279`). In
  E-1 the acts of force through Church seats (`raze`, `seize`, `capture`) came through the Cardinals of
  Prudence, Justice and Temperance, the Confessor and the Archbishop's Representative, by the testing
  grant; the Cardinal of Fortitude's two `seize` acts rode `issue`.
- Every Church bench has `scope_rung == rung == terr_T9` (E-2), so `sits_over` is False everywhere else
  and `excommunication_deliberation`, whose own comment says it disposes *"of a person who is not there"*,
  cannot run on anyone outside the city. CR-60 names this defect and supplies the key; it authors no value.
- `harness/strife_moves.yaml:90`: CH has `gap:`. CR-74 searches for *"a property the seat's institution
  already carries in code"* and forbids a named-faction list.

## The resolution, decided

One content edit per defect, at the owner. For CR-74 the property exists and is named:
`data/rosters.py::ROLE_TEMPLATE_OF` (`rosters.yaml: role_templates.by_faction`) maps a faction to its
role template, and `ecclesiastical` is the template of a church. A seat is a church seat when
`ROLE_TEMPLATE_OF.get(office_faction(seat.body, seat.faction)) == "ecclesiastical"`. A second
ecclesiastical faction (a schismatic obedience, a foreign church) is covered with no edit.

## Exact edits

1. `engine/season/npcs.yaml`, row `case: NPC-021`:
   - old: `institution: null` / `home: b_s_003_market` / `tie: neighbour`
   - new: `institution: Church` / `home: b_s_036_cathedral` / `tie: institution`
   `concerns: NPC-001` is unchanged. `tools/export_npc_roster.py --check` will report the row as a hand
   edit, which is its documented behaviour.
2. `engine/season/offices.yaml`, row `off_cardinal_fortitude`:
   - old: `remit_acts: [issue, convene]`
   - new: `remit_acts: [issue, convene, dispatch]`
   - `note:` gains: *"`dispatch`: the Templars' command (PAPACY-A). [ASSUMPTION; medium; Jordan to
     correct; revert: drop `dispatch`, and the Church commands no force after FA-P2.]"*
   `off_archbishops_rep` gaining `issue` is FA-P2's edit (FA audit §13, NPC-034) and is not repeated.
3. `engine/season/offices.yaml`, with CR-60's key (`scope:`, an anchor of the same four forms as `rung:`):
   - `off_confessor`: `scope: {realm: true}`
   - `off_cardinal_justice`: `scope: {realm: true}`
   - `off_senior_inquisitor`: `scope: {realm: true}`
   - the other four Church rows: no `scope:` (their bench ground stays their rung).
   `[ASSUMPTION; medium; Jordan to correct; revert: no `scope:` on the three rows.]` The three are the
   bench CR-34's test already assembles for the declared row.
4. `engine/season/arrangements.yaml`, the comment above `excommunication_deliberation`: add one sentence,
   *"Until three Church benches carry a realm `scope:` (CR-60, PAPACY-A) the party must stand in
   `terr_T9`: `may_determine` asks `sits_over(seat, home_of(party))`."* A comment; no key.
5. `engine/season/harness/strife_moves.yaml`, the CH row, and `harness/strife.py` (CR-74's files):
   - CH: `verbs: [arrest, determine, revoke]`, `kinds: [arrest.made]` (and `ban.opened`,
     `detention.opened` when PAPACY-D lands them), `gap:` removed, a `needs: [office]` marker kept.
   - one signature function, the shape of the march-side signature: an Event of one of the row's kinds
     whose causing act (`state/attribution.py::actor_of`'s walk to the act) has a `via` seat `s` with
     `ROLE_TEMPLATE_OF.get(office_faction(s.body, s.faction)) == "ecclesiastical"`.
   - the residue label CR-74 specifies, unchanged.

## Gate

- `probe_reach.py` (the audit's E-2 probe) re-run after edit 1: the Confessor's chain passes through
  `terr_T9`; persons under `terr_T9` 10 of 83.
- After CR-60 and edit 3: `sits_over(off_confessor, terr_T1)` True; `sits_over(off_cardinal_prudence,
  terr_T1)` False; `purview_reaches(off_confessor, terr_T1)` still False (judging reach, not acting reach).
- CR-74's own exit: a planted restraint through a Church seat reads CH; the same through a secular seat
  does not and lands in the labelled residue; `content_hash` unchanged by the reading.
- Control: each edit reverted reproduces the base build hash.

## Falsifier

A world in which a second faction is given the `ecclesiastical` template and its seat's restraint does
not read CH (the signature would be keyed on a name). A `scope:` that changes `purview_reaches`.

## NERS reading

N: without edit 1 the head of the Church is not at the Church, so no Church bench sits over him, no
sitting at the chapter house includes him and his co-location is with market traders; without edit 3
every Church hearing is a city court. R: a designer changes a bench's reach by one anchor. S: `scope:` is
CR-60's one key, the signature reads one existing roster. E (last): five edits, no new name.

## Cost class

Edit (1, 2, 4), edit inside CR-60 (3), small build inside CR-74 (5).
