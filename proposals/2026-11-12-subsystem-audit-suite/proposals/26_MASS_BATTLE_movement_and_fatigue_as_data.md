# MB · movement and fatigue as typed data: pace by troop kind and ground, what tires a body, what it costs to re-form

## Status: PROPOSED

Lane MB. Carries rows M-1 to M-5 and M-7 of `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. Extends the
troop file of `04_MB_unit_loadout_and_weapon_in_hand_B.md` and the ledger of
`16_PESSIMIST_MB_one_stamina_ledger.md`; depends on both. Source keys as in the audit (**MV**, **CR**, **SQ**,
**WG**). Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

At the seeds marked *control*: nothing (every value is today's constant, moved). With the declared seeds on:
horse loses most of its speed advantage in broken ground and uphill; a body that moves faster than its base
pace arrives more tired; an army that marched hard, or fights a second field in a season round, starts
tired; a body may change its shape or depth out of contact, for a price in ticks. No natural season fights an
army field today.

## The problem

- Pace is a name test and two constants: every shape returns 1 (`modules/mass_battle/geometry.py:328-338`),
  a mounted type is multiplied by `MB_CAVALRY_SPEED_MULT = 3.0` (`config.py:376`; applied at
  `hierarchy/units.py:1768`, `:1787`, `:2096`, `:2107`), an enveloping body by `MB_ENVELOP_SPEED_MULT = 2.0`
  (`config.py:385`; `units.py:1775`).
- Ground never slows anything: the terrain row changes dice (`massbattle.py:411-422`).
- Speed is free: stamina drains per clash only (`16_PESSIMIST_MB_one_stamina_ledger.md`, the column ledger).
- Nothing enters a field tired (same file: `entry_stamina` has no writer).
- A body cannot be told to change shape: `shape` is not in `_ORDER_SAFE_FIELDS` (`units.py:271-290`);
  `check_drift` changes it at once and drops per-cell morale (`audits/04_MB_audit.md` F-MB-18).

History and wargame practice on each: MV M1–M10, X1–X6, T1–T7; WG K1, L4, T3.

## The resolution, decided

### 1. Pace (troop row)

`references/troops.yaml: troops.<kind>.pace`, cells a tick at base. Seeds reproduce today:

| kinds | `pace` | ground |
|---|---|---|
| every foot kind | 1 | no source read separates heavy from light formed foot on the field (MV M9); Lost Battles gives all foot one move (WG L4). **Control and seed are the same.** |
| `cavalry`, `light_cavalry`, `mounted_archers` | 3 | trot against a foot pace is 2.7 to 3.8 (MV M1, M3); Lost Battles 2 (WG L4). Today's constant, in range |
| `knights_templar` | 1 | today's behaviour (it is not in `MOUNTED_TYPES`); the visible cell `…_B.md` already hands to Jordan |

`MB_CAVALRY_SPEED_MULT` is deleted; the four sites read the row. The envelop multiplier becomes
`orders.envelop_pace: 2`, one datum beside the order vocabulary, because it is a property of the order, not
of a troop.

### 2. Ground (terrain table)

A `pace` column on the six terrain rows (`modules/mass_battle/terrain.py` today; the troop file's `terrain`
section when that file lands), by class:

| row | foot | mounted | ground |
|---|---|---|---|
| `open_flat` | 1.0 | 1.0 | — |
| `forest_broken` | 1.0 | **0.6** | Kriegsspiel 1824: cavalry 250 of 400 paces in light forest (WG K1); Lost Battles: rough ground costs horse double (WG L4) |
| `uphill` | 1.0 | **0.25** | Kriegsspiel: 100 of 400 paces up inclines (WG K1) |
| `narrow_pass`, `river_crossing`, `walls` | 1.0 | 1.0 | **not established**; no multiplier invented |

- Foot stays at 1.0 everywhere: no figure was read (MV M10), and slowing both sides' foot on a one-row field
  only spends ticks. Agincourt's mud is a fatigue effect on the attacker (section 3), not a pace.
- Control arm: every cell 1.0.
- The multiplier applies to the body's step before the stance modifier, at the one place the step is formed
  (`units.py::_node_advance`; the continuous-speed arm accumulates the fraction as it already does for
  discipline, `:2094-2100`).

### 3. Fatigue (one ledger, four sources)

A `fatigue` section in the troop file. `clash_drain`, `rest` and `lull_recover` are today's constants,
transcribed (`config.py:355-356`; `orchestration.py:1810`); the others are new and ship at their control
until flipped.

```yaml
fatigue:
  clash_drain: 12          # MB_STAMINA_DRAIN, per clash a column fights           (today)
  rest: 5                  # MB_STAMINA_REST, per tick a column is out of contact   (today)
  fast_move_drain: 0       # per tick a column moves above its row's pace. CONTROL 0. Seed for the flip: 2
  lull_recover: 30         # BETWEEN_TURN_STAMINA_RECOVERY (orchestration.py:1810), per lull (today)
  entry:                   # share of full stamina a side starts with. CONTROL: all 1.0
    march_partial: 0.7     # the army "arrives spent" (14_VERBS_MILITARY_A: the Partial band of the journey)
    second_field: 0.7      # a second field in one season round
    unfed: 0.7             # the side's ration was short at the field (SE's debit, when provisioning is on)
```

- `fast_move_drain` is M-3's rule: a horse gallops one and a half to three kilometres before it must rest
  (MV M1); the official Total War manual's advice is "do not run everywhere" (WG T3). Its magnitude is not
  sourced. The seed is a sixth of a clash, chosen so that an envelopment at double pace over a whole bout
  costs about as much as three clashes; it is Jordan's to set.
- `entry` is M-7's rule. Each value multiplies; the lowest product is floored at 0.3 so no side arrives
  unable to stand (a seed). The three writers are the only writers; each reads a fact its owner already has
  (the march's band; the count of fields this round; the ration debit). The carry cost of a second weapon is
  **not** an entry term: it acts on the drain and the rest inside the fight (`…_B.md` §5).
- Every magnitude here but the three transcribed ones is a seed with no historical figure behind it (MV T2,
  T7). The form is what the sources support: fresh against tired is what decided Roman battles (CR D3, `[D]`).

### 4. Changing formation (order behaviour, out of contact)

- `shape`, `ranks` and `files` join `_ORDER_SAFE_FIELDS` as one behaviour key, `reform: {shape, ranks, files}`,
  applied through `rekey_cells` (after F-MB-18's repair: the three morale maps re-seeded from the body's
  aggregate).
- **Eligibility:** the body has no cell in contact on the tick the order fires. In contact the order stays
  pending. That is a rule about what may be attempted, not a resolution.
- **Cost:** `reform_ticks` during which the body's pair pools are 0, it does not volley, and its brace
  latch is down: the weapon switch's rule (`…_B.md` §4), for longer. Datum `orders.reform_ticks` by
  Discipline: 1 at Discipline 4 or more, 2 below. `[seeds; pre-gunpowder times are not established, MV X6.
  The only figures read are Napoleonic drill at second hand, 30 to 100 seconds for a battalion (MV X1),
  which at four seconds a tick would be 8 to 25 ticks, longer than a bout. The game compresses it and says
  so; in the lull between bouts (`26_MASS_BATTLE_cell_scale_and_time.md` §3) a reform costs no ticks.]`
- `check_drift` stays, and pays the same cost: a body that loses its shape for want of Discipline is
  disordered for `reform_ticks`, not instantly re-dressed.
- Caught re-forming, a body is what the sources say it is: beaten (MV X2). No extra rule is needed; its
  pools are zero.

## Exact edits

| file (owner) | edit |
|---|---|
| `references/troops.yaml`, `tools/export_troops.py`, `troop_types/table.py` | `troops.*.pace`; `terrain.*.pace`; `fatigue`; `orders.envelop_pace`, `orders.reform_ticks` |
| `modules/mass_battle/config.py` | delete `MB_CAVALRY_SPEED_MULT`, `MB_ENVELOP_SPEED_MULT`, `MB_STAMINA_DRAIN`, `MB_STAMINA_REST` (their values now rows) |
| `modules/mass_battle/hierarchy/units.py` | the step reads `pace x terrain pace`; `reform` in `_ORDER_SAFE_FIELDS`; `rekey_cells` repair; a `_reforming_until` tick on the subunit, read where the switch tick is |
| `modules/mass_battle/percell.py::update_stamina` | the fast-move term |
| `modules/mass_battle/massbattle.py::resolve_field` | passes the field's terrain row to the units for pace, as it passes it for dice |
| `engine/season/seam/wrappers/mass_battle.py::field_input` | forms `entry_stamina` from the three facts |

## Gate (execution artifacts)

1. Every new value at its control: `tools/export_troops.py --check` passes and
   `tools/ci_golden_modes_check.py` digests are equal.
2. A cavalry body and a foot body crossing 12 cells: on `open_flat` the horse arrives in a third of the
   ticks; on `forest_broken` in about half to two-thirds; on `uphill` after the foot. Read from the trace.
3. `fast_move_drain: 2`: an enveloping wing's columns read lower stamina at first contact than the same wing
   at the control, and the envelopment's win share against the same-run control is reported, not targeted.
4. `entry.march_partial: 0.7`, mirror field, n 100, friction pinned off for the test: the tired side loses
   more often than at 1.0 by more than the sampling band (the one-ledger proposal measured 36 wins to 15 at
   0.5).
5. A body ordered to `reform` from `Line` to `Column` while out of contact: its shape changes, its cells'
   morale ids match its troop ids, and for `reform_ticks` it deals no damage; the same order given in contact
   does not fire until contact ends; charged during the reform, it loses more than the same body charged
   after it.

## Falsifier

A pace that still depends on the spelling of a troop type's name; horse at three times foot on `uphill`;
stamina unchanged by a bout of double-pace movement at a non-zero drain; a re-forming body that fights.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the designer: a slow, heavy troop kind is one cell, where today it is Python. From the
  commander: ground and haste become choices. From the campaign: a march's result reaches the field. Cut the
  ground column and cavalry is equally good everywhere, which no source and no wargame read supports.
- **R.** Where to fight horse; whether to hurry a flank march; whether to rest before offering battle.
- **S.** One ledger; one place the step is formed; the re-form and the weapon switch are one rule.
- **E, against that.** Four constants become rows; two columns and five numbers are new, all with controls.

## Cost class

Sections 1 and the transcribed fatigue rows: edit, hash-equal. Sections 2 to 4: small build, three declared
flips. After `…_B.md` stage 1 and the one-ledger proposal.
