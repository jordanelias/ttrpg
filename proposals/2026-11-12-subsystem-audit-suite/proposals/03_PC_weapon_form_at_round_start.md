# PC — a new engagement opens with the weapon as issued: the half-sword form does not cross the round boundary

## Status: PROPOSED

Lane: PC. Source: `audits/03_PC_audit_addendum_B.md` F-PC-16. Read at `2c24c81`. Reference only
(CLAUDE.md §0.05); not ratified by being written. Independent of the round entry
(`03_PC_duel_round_and_approach_B.md`); if it lands first, that proposal's `DuelState.form` field is
not needed.

## What it changes in `engine/season/` at runtime

Nothing today: every person fights with an arming sword in light armour, and the form switch fires
only for a half-sword-capable weapon closed against medium or heavy armour. It moves the workbench's
armour reference for the four weapons that half-sword (longsword, estoc, greatsword, flamberge).

## The problem, with evidence

`wrapper.engagement` opens every engagement with an open-measure reset (`modules/combat/wrapper.py:83-90`,
ED-PC-0033): grip position and lunge depth go back to zero, because, in the comment's words, a weapon that ended the
last engagement choked in "would UNDER-READ its own reach at THIS engagement's opening reach_base",
"corrupting the frozen longer/shorter labels and measure_gap for the whole new engagement". The weapon **form** is the same kind of state and is not reset. `halfsword_target`
swaps `Combatant.weapon` to the shortened record inside a closed exchange (`wrapper.py:273-274`), the
swap stays on the object, and the next engagement computes its opening reach on the shortened record
(`wrapper.py:91`).

| reading (`PYTHONHASHSEED=0`) | result |
|---|---|
| fighter-starts entering a later engagement still in a half-sword form, 800 fights over four matchups (`probe_round_state.txt`) | 1,142 of 3,318 |
| longsword against arming sword, both in plate, 3,000 fights: engagements that open at open measure | 36.4% as built; 60.5% with the form reset; 35.9% as built at disjoint seeds |
| estoc against arming sword, both in plate | 88.7% as built; 25.6% with the reset; 88.9% control. The reach labels do not invert (the arming sword is labelled the longer weapon in 0 of 1,958 half-sword starts over 600 fights); what moves is the re-presentation gate (`wrapper.py:121-124`), which reads the armour-defeat threat of whatever record is in hand, so a half-sworded estoc re-presents "at measure" in a grip the engine's own rule reserves for the close |
| greatsword against arming sword, both in mail | 100.0%, 84.7%, 100.0% |
| share of decided fights, longsword against mace, both in plate | 74.8% as built, 78.9% with the reset, 74.5% control. The other four matchups move inside their control |

The engine's own predicate says which is right: `halfsword_target` returns the full form "at reach /
vs unarmoured" (`combat_systems.py:880-890`), and an engagement that opens at open measure is at
reach. The form is re-taken at the first closed exchange that calls for it, so nothing is lost by
starting each engagement with the weapon as issued.

## The resolution, decided

Reset the form with the grip, at the same site (ladder step 4: ED-PC-0033's reset is the precedent,
and its stated reason covers the form word for word).

- `modules/combat/combat_systems.py`: `base_form(c) -> str`, pure: `HALFSWORD_BASE.get(c.weapon,
  c.weapon)` (the mapping is already imported there and already the first line of
  `halfsword_target`).
- `modules/combat/wrapper.py`, in the open-measure reset loop: `c.weapon = S.base_form(c)` beside
  `c.grip_position = 0.0; c.lunge_depth = 0.0`. The wrapper owns the mutation, as now.
- No constant, no draw: the reset reads no random number, so every fight in which no form was carried
  is byte-identical.

## Gate (execution artifacts)

- `probe_round_state.py` re-run: 0 fighter-starts enter an engagement in a half-sword form.
- Fights between weapons that never half-sword, and every fight off rigid armour: byte-identical at
  the same seeds (the season's hash EQUAL follows).
- `python systems/combat/combat_engine_v1/workbench/armour_participation.py --drift` printed in the
  commit body; the reference regenerated with `--update` **once**, and the diff is the disclosure
  (the file's own rule). Expected movers: the four half-swording weapons at medium and heavy.
- The mirror control (`build_levers.py mirror`) for longsword in plate stays at 50 ± 2.

## Falsifier

After the edit, an engagement whose `engagement_start` event shows a `_halfsword` record as either
fighter's weapon; a fight between two arming swords whose trace differs from today's at any seed.

## NERS reading

- N: from below, one field of transient geometry was left out of a reset whose reason names it; from
  the round entry's side, state that silently crosses a round boundary is state a caller must know to
  carry. Laterally it matters only to four weapons against rigid armour, and the proposal says so.
- R: completeness at an extreme: the estoc, the roster's most decisive plate weapon, currently opens
  nine engagements in ten at open measure while still gripped for the close.
- S: one reset for all per-engagement geometry; the round's carried state shrinks to the four
  quantities that are a fighter's condition.
- E, last: two lines and one regenerated reference table.

## Cost class

Edit, plus one deliberate re-record of `workbench/data/combat_armour_reference.json` and of any pin
that fights a half-swording weapon in rigid armour.
