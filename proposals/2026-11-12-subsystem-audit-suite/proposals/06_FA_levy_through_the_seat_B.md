# FA-B2 — men are levied through a seat, as stores are: who may raise, discharge and first muster a faction's army

## Status: PROPOSED

Source: `audits/06_FA_audit_addendum_B.md` F-FA-15, §B4.1 (the levy and command rows), §B6.1 R-24;
evidence E-B3, E-B9. Cross-lane: the six army verbs are ED-IN-0306's and the MB lane's
(`audits/04_MB_audit.md` §6.2 R-07, R-23; its step 5); this file states the authority, which is FA's,
and edits no rule of the army Record's content.

## What it changes in `engine/season/` at runtime

1. `recruit` and `discharge_troops` are exercised through a seat (`Act.via`) whose grant carries the
   muster act, whose faction is the army's, and whose purview reaches the cohort's residence. Today
   they are `own`-eligible on holding the Record.
2. The one army a faction may have is minted by a holder of such a seat. Today any member may mint it.
3. Nothing moves in computed play: all six army verbs are withheld from every NPC's opening set
   (`data/fixtures.py:1157`), `army_presets` is called by nothing, and no built world holds an `army`
   Record (addendum E-B1). Realm, spine and corpus hashes EQUAL. Hand-built acts and `army_presets`
   change as stated in the gate.

## The problem (evidence)

At `6eff039`, `PYTHONHASHSEED=0`, `build_realm(0)` (addendum E-B9, `levy_probe.py`):

- `p_npc_002`, a member of Varfell who holds no seat, mints Varfell's army (`record.created`) and
  raises 60 levy from `cohort_set_s_026` (`army.recruited`).
- The same `recruit` by `p_npc_052`, the Duke of Varfell and the faction's head, is then
  `recruit.refused`: he does not hold the Record, and a second army is refused at its mint
  (`loop/effects_information.py:116`, one per faction).
- The rule that admits the first and refuses the second: `loop/effects_army.py:34-42` (the commander is
  the Record's holder, committed to the army's faction) and `queries/world_q.py:2186-2195`
  (`raisable_by`: the faction holds where the cohort lives, or the cohort is committed to it).
- The sibling extraction: `requisition` is `remit:issue` with a purview cell on the place
  (`verb_table.yaml`, E-B3); `march` is `remit:dispatch`, and the gate's `may_muster` asks seat, grant
  and the mustered person's commitment (`state/gate.py:1036-1059`).

So the right to take stores from a place is a seat's, the right to move its faction's people is a
seat's, and the right to put its people under arms belongs to whoever minted a paper first. That is two
ladders for one quantity (an S defect, `CLAUDE.md` §0.06), and it lets a faction's army be captured by
its least member.

## The resolution, decided

Raising and discharging troops is an exercise of office over a place; ordering the troops one has is
the commander's. Ladder step 4: `requisition` and `may_muster` are the precedent, and ED-IN-0256 (4)
is the rule ("authority is asked of the seat exercised"). It is also a returning recommendation: the
FA research lane worded the act, before it was built, as "let a seat levy troops from a cohort in its
purview into its faction's muster" (`research/by_lane/FA_faction_actions.md` K-FA-13, 2026-10-16), on
Jordan's statements quoted there (`:347`): armies are "troops levied from settlements as their own
resource … differ in quantity and quality based upon equipment and experience and their commanders",
and "factions are supposed to be able to assemble armies". ED-IN-0306 built the Record and its content
rules; the seat was the part left out. The comparative research gives the same caution from history
(`research/governance/conflicts_power_struggles.md`, synthesis: a force bound to a named holder and
not to the office reproduces the collapse the office was built to prevent; the Marian legions, the
Tetrarchy), as shape only. The existing faction rule is kept, not
replaced: a seat levies only people its faction governs or who are committed to it. The four
organising verbs (`form_unit`, `assign_troops`, `order_unit`, `disband_unit`) stay `own` on `held_by`:
the Record is still the order of battle and its holder still commands it, as Jordan ruled on
2026-10-28 (the army is a Record).

Command passes as a Record passes: by `give`, or by `seize` through a warrant when a dismissed
commander will not hand over the roll (`seize`'s subject is "a Record or a settlement"). No rule for
that is added.

## Exact edits, by owner

**1. `engine/season/state/gate.py`** (owner of what a seat licenses), beside `may_muster`:

```python
def may_levy(w, actor, via, cohort: str, faction: str) -> bool:
    """May `actor`, exercising `via`, put `cohort`'s people under arms for `faction`'s army?
    seat_hold; the grant carries MUSTER_ACT; seat_faction(via) == faction;
    purview_reaches(seat, residence of the cohort); raisable_by(cohort, faction)."""
```

Each conjunct is an existing owner's (`_seat_grants`, `seat_faction`, `purview_reaches`,
`world_q.raisable_by`); `raisable_by` keeps its recorded assumption.

**2. `engine/season/verb_table.yaml`** (owner: the table; the rows are ED-IN-0306's). `recruit` and
`discharge_troops`: `eligibility: ["remit:dispatch"]`. Their `requires_typed` (the subject is an army
Record the actor holds) is unchanged, so the actor must both sit in a muster seat and hold the roll.
The other four rows are unchanged.

**3. `engine/season/loop/effects_army.py`.** `_eff_recruit` and `_eff_discharge_troops` replace the
bare `world_q.raisable_by(w, cohort.id, faction)` test with `may_levy(w, a.actor, a.via, cohort.id,
faction)`. `_army` is unchanged.

**4. `engine/season/loop/effects_information.py::_army_mintable`.** One conjunct after the membership
test: the actor `may_wage` for the faction (the predicate `06_FA_war_lives_in_seats_B.md` adds; if that
file does not land, the same two lines inline: a live `hold` on an office of the faction whose grant
carries `MUSTER_ACT`).

**5. `engine/season/harness/military_menu.py::act_for` and `army_presets._commander`.** `act_for`
stamps `via` with the actor's seat that grants the muster act (`decision/options.py::seat_of`, the one
owner of "which seat grants this"), so the menu's acts are admitted as the chooser's would be.
`_commander` already tries leaders in id order against `_army_mintable` and needs no edit.
`military_menu.cohorts_raisable(w, faction)` becomes `cohorts_raisable(w, person)`, asking `may_levy`
for each cohort.

**6. `engine/season/tests/`** (the files that hand-build army acts; find them with
`grep -rl "army.recruited\|act_for(" engine/season/tests`). Each hand-built `recruit` gains a `via`;
each gains the refused twin of the gate below.

## Gate (execution artifact)

The addendum's probe, re-run after the edit, must read:

- `p_npc_002` (no seat): the mint is refused (`record.refused` or the row's refusal kind);
- `p_npc_052` through `off_duke_varfell`: `record.created`, then `army.recruited` for a cohort in a
  Varfell-held territory;
- the same seat on a cohort resident in a territory another faction holds: `recruit.refused`;
- a Varfell seat whose grant lacks the muster act: `recruit.refused`;
- `army_presets.install(build_realm(0))` raises the same three armies the MB audit records (Hafenmark
  600, Valorsmark 900, Varfell 600, all levy; `04_MB_audit.md` §1.3), now minted by a seated leader;
  if a count differs, the difference is a cohort outside the minting seat's purview and is reported by
  name.

## Falsifier

- Control: with `may_levy`'s seat conjuncts removed the first bullet executes as it does today.
- Mutation: drop `purview_reaches` and the third bullet executes; drop the faction match and a Crown
  seat raises a Varfell army.
- Hash: one-season `build_realm(0)` EQUAL (no army verb forms; none is unwithheld here).

## What it does not do

It does not lift `withheld_verbs`; when MB's step 5 does, an NPC forms `recruit` only from a muster
seat. It does not decide whose men the Löwenritter command: the Order holds no land and the realm's
cohorts carry no `commit`, so it can raise nobody before or after this edit (E-B9), and the archived
design's "the Crown's standing army is the Löwenritter" (`faction_layer_v30` §1.5) is content for
Jordan: either the Order holds its garrison settlements, or it commands Valorsmark's army by
appointment. It adds no upkeep (addendum R-31).

## NERS reading

- **N.** From above, a duke levies his duchy and nobody else's. From below, a cohort is called by the
  lord whose ground it lives on. Laterally, stores, marching and levy share one authority. Diagonally,
  the oath clause already extends a liege's purview over a sworn vassal's ground, so a feudal levy by
  oath needs no further rule. Remove it and the army is its first minter's.
- **R.** Appointment to a command post now carries something (the first lane's remit-by-row proposal
  decides which posts); a faction can lose its ability to raise men by losing its marshal. Complete at
  the extremes: no muster seat, no levy; a seat with no rung levies nothing by its own ground.
- **S.** `may_levy` is `may_muster`'s shape. No new operand: the cohort stays a payload key, checked in
  the effect as today.
- **E, last.** One predicate, two eligibility cells, one conjunct on the mint, one stamp in the menu.

## Cost class

Small build. No computed mover. MB lane reviews edits 2, 3 and 5.
