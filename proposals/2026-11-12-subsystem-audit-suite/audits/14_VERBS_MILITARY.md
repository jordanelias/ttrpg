# VERBS · MILITARY — build-out of the seven army rows and the two `movement` rows

## Status: REFERENCE (a verb build-out audit; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 84d2a02 (working tree)

Work order: `VERBS_BRIEF.md`, FAMILY = MILITARY. Verbs: `train`, `recruit`, `form_unit`, `assign_troops`,
`disband_unit`, `discharge_troops`, `order_unit` (stratum `uncontested_material`) and `migrate`, `move`
(stratum `movement`), nine rows of `engine/season/verb_table.yaml`. The exact edits are in the proposals
named in §0.4; this file holds, per verb, the premise, the state today with its reading, the decided
build-out, and the family's order.

## 0. Verdict and reading

### 0.1 Verdict

**Two of the nine work (`move`, `migrate`), one forms for everybody and has never executed (`train`), and
six are sound commands that no person in the world can give (`recruit`, `form_unit`, `assign_troops`,
`disband_unit`, `discharge_troops`, `order_unit`).** The six are not stubs: each has a row, an effect, a
pure rule in `modules/mass_battle/armyrecord.py`, a refusal, and a headless menu that lists exactly what
the fold would accept. What is missing is the person. The command rides the act's payload, the operand
vocabulary is closed, so `Fixtures withheld_verbs` holds all six out of formation for everybody
(`data/fixtures.py:1157`), and the one caller that gives them for a faction nobody plays
(`harness/army_presets.py::install`) is shipped off by construction: nothing in the loop, the harness
`run` functions or the corpus calls it. So in every seeded run no `army` Record exists, no field is fought
from an order of battle, and the six `army.*` kinds are in the never-emitted list. The single largest
obstacle for the family is therefore **not an effect but a chooser: there is no commander** (the general
is the unbuilt `MB-08`), and the army economy that would give a commander reasons to raise, keep, order
and send home (wage, ration, readiness, loss) has no cost and no clock, so raising is free and
discharging has no motive.

`train` fails differently: it forms 83 of 83 and executed 0 of 85 attempts, because its subject is the
question's referent (a non-person 39 times, an absent person 33 times) and, when the pupil is present,
he holds no key in the vocation (13 of 13 post-admission refusals): the J-13 (iii) interim forbids
minting a key and no realm person holds one. It is a verb whose every refusal the actor could have read.

### 0.2 What this is read against

- HEAD `84d2a02`. One seeded instrument reading, shared with the PHYSICAL lane so the two families read
  one trajectory: `aperture 2 0` (realm and ladder arms, seed 0, two seasons, `PYTHONHASHSEED=0`, control
  hash EQUAL; copy at `scratchpad/runs/VERBS_MILITARY/aperture_2_0_shared_from_PHYSICAL.txt`) and
  `corpus_run` (`scratchpad/runs/VERBS_PHYSICAL/corpus_run.txt`). The family's own probes are in
  `scratchpad/runs/VERBS_MILITARY/` and are listed in §12.
- One seed is a reading of a trajectory, not a rate (CLAUDE.md §0.1 pt 4); nothing below is a balance
  claim.

### 0.3 State today, one line per verb

`elig` = persons eligible at build (seated / unseated); `formed` = persons who formed it; `att / ex / ref`
= acts attempted, executed (emitted a declared `emits:` kind), refused. Realm arm, `aperture 2 0`.

| verb | elig | formed | att | ex | ref | deciding read of the refusals | verdict |
|---|---|---|---|---|---|---|---|
| `train` | 33 / 50 | 83 | 85 | 0 | 85 | `exists:Person=0` 39 · `with=False` 33 · post-admission 13 (the pupil holds no key) | **forms but is refused**; `capability.raised` never emitted |
| `recruit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; executes by hand-built act |
| `form_unit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; executes by hand-built act |
| `assign_troops` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; executes by hand-built act |
| `disband_unit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; no caller at all outside tests and the menu |
| `discharge_troops` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; no caller at all outside tests and the menu |
| `order_unit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; no caller at all outside tests and the menu |
| `migrate` | 33 / 50 | 83 | 84 | 10 | 74 | `room` 60 · `path` 13 · `write` 1 | **works** (throttled by capacity, which is the design); its refusals teach the migrant |
| `move` | 33 / 50 | 83 | 55 | 15 | 40 | post-admission 33 (the effect's ladder decline) · `audience=UNKNOWN` 7 | **works, and 33 of its 40 refusals are a dead end the actor could have read** |

Never emitted in this run, of the family's declared kinds: `army.recruited`, `army.formed`,
`army.assigned`, `army.disbanded`, `army.discharged`, `army.ordered`, `capability.raised`, and the six
`*.refused` kinds of the army rows. Emitted: `travel.moved` 15, `travel.blocked` 53, `residence.changed`
10, `migrate.refused` 61, `train.refused` 85. In the ladder arm (13 persons): `migrate` 0 of 9 (all
`room`), `move` 0 of 3, `train` 0 of 12.

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_MILITARY_A_movement.md` | `move`, `migrate` | M-A |
| `proposals/14_VERBS_MILITARY_B_train.md` | `train` | M-B |
| `proposals/14_VERBS_MILITARY_C_the_muster.md` | `recruit`, `discharge_troops` | M-C |
| `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | `form_unit`, `assign_troops`, `disband_unit`, `order_unit` | M-D |

