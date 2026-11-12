# MB · what an army carries back: a loss has a kind, some of it returns by a draw, and fatigue stays on the one ledger

## Status: PROPOSED

Lane MB (the season-side write is IN's; a cohort's own deaths are SE's and the census's; custody is the
PHYSICAL lane's). Serves ruling **A-69** (`unified/DECISIONS_ANSWERED.md:90`), Jordan: *"armies carry fatigue
and losses back. losses are written. however some losses will be due to injury not death or from fleeing, so
there is SOME recuperation of numbers afterwards"*, with A-67 and A-68 (a drawn aggressor is back at his
station at once). **Extends, and does not replace:** `16_PESSIMIST_MB_rout_has_two_exits.md` (rally and
pursuit), `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §4 (the dead and the taken),
`16_PESSIMIST_MB_one_stamina_ledger.md` step 3 and `26_MASS_BATTLE_movement_and_fatigue_as_data.md` §3 (the
entry share), each amended in place with a `Folded:` line. Audit: `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md`
§7. Read at `faf0cea`. Reference, not mechanism (`CLAUDE.md` §0.05). No code is edited by this file.

**What is not established, and is therefore not quoted or built on.** The tree's research holds nothing on
the wounded: "Nothing on wounded. Every figure above is dead (or dead and captured where said)"
(`research/historical/mass_battle_casualties_and_results_grounding.md:124`); one engagement in that note
names wounded beside dead (row A9) and one case is not a ratio. Not established anywhere in the tree: the
ratio of dead to injured; how fast the injured return and over what span; whether men who fled come back
unprompted or only when recalled; what share never return. Every magnitude below is therefore a named
parameter with a control arm and **no shipped default**; §5 gives the calibration targets (orderings only)
and §6 the source search that must be filed before any figure is used.

## What it changes in `engine/season/` at runtime

With `recuperation: off` (the control): nothing; today's loop exactly. With it on, for a side that fought as
an army: its units' strength falls by what the field cost; part of that cost is held on the unit's row as men
injured and men fled; in later rounds some of them return, by a draw; the dead and the taken do not. A unit
that fights twice in one round enters the second field at the stamina the first left it. Declared hash movers
wherever an army field is fought; none in a natural season today (`audits/04_MB_audit.md` F-MB-03).

## The problem (opened at `faf0cea`)

- **One kind of loss, and all of it comes back.** A fought field scales the `body` of the persons and cohorts
  on the losing side (`engine/season/loop/effects_combat.py:630-657`, model `scaled_by_degree`). An army's
  strength at its next field is its assigned counts times each cohort's `body` share
  (`modules/mass_battle/armyrecord.py:256-271`; `seam/wrappers/mass_battle.py:192-214`: "that is the whole
  casualty loop ... and `tend` restores it"). `tend` raises a body to full in one act
  (`engine/season/verb_table.yaml:1565`: "the headroom ... taken whole"). So nobody is ever dead, every loss
  is one act from undone, and its return is certain.
- **Nothing is carried.** Every field starts every column at full stamina
  (`16_PESSIMIST_MB_one_stamina_ledger.md`, the problem); the stamina a field ends with is returned for a
  ledger that does nothing and then dropped.
- **Flight is not a loss at all.** A routed side "keeps about two-thirds of its men and stays where it stood"
  (`16_PESSIMIST_MB_rout_has_two_exits.md`, "what it changes").
- The earlier proposals stop at the field's edge on purpose: "What the field does not decide: who among the
  hurt dies ... that draw is the season's" (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §4). A-69 is
  that draw's ruling.

## The resolution, decided

### 1. A loss has a kind, and the field already returns what decides it

The field returns, per side and per part (the typed outcome as the two proposals above amend it):
`fight_loss`, `pursuit_loss`, of that `taken`, and the part's end state (`stood`, `gave_ground`, `routed`,
`rallied`, `withdrew`). No new draw is added inside the module. The kinds are read off those:

| kind | what it is | comes from | returns? |
|---|---|---|---|
| **dead** | killed in the line or in the pursuit | a drawn share of `fight_loss`; the untaken part of `pursuit_loss` | never |
| **injured** | hurt and out of the ranks | the rest of `fight_loss` | by the recovery draw (§3) |
| **fled** | alive, unhurt, gone from the colours | a drawn share of the **survivors** of a part that ended `routed` (not `rallied`, not `withdrew`) | by the return rule (§3) |
| **taken** | alive in the victor's custody | `taken` (the `26_…` §4 draw) | only by the custody verbs (`14_VERBS_PHYSICAL_A_custody_and_force.md`) |

- **Two draws, season-side, in `_eff_march`'s one casualty write, per part:** (a) of `fight_loss`, the share
  that is injured and not dead; (b) for a routed, unrallied part, the share of its survivors that fled. Each
  is a draw on the one sampler and ladder whose band selects a share from a four-row table
  (`aftermath.injured_share`, `aftermath.fled_share`), the form `26_…` §4 already uses for `taken`.
- **Odds terms, each a fact the outcome carries** (signs are the design; sizes are parameters):
  for (a): the side held the field at the end (its hurt are gathered: raises the injured share); the part was
  pursued (lowers it). For (b): the rally band (a `withdrew` part loses none this way); mounted pursuit
  against it (raises it); the part's Discipline (lowers it). `[The first term of (a) is a design assumption:
  no source in the tree says a victor recovers his wounded. It ships at control 0 until one is filed.]`
- Men lost in a pursuit are dead or taken, never injured-and-recovered: the sources read put the beaten
  side's decisive loss in the flight (CR A7, A12, as `16_PESSIMIST_MB_rout_has_two_exits.md` cites them).
- A rallied part and a part that withdrew in order have no fled men. Rally "saves men, not the place"
  (same file, Reconciled (2)); this is the men it saves.

### 2. Losses are written on the row that holds the unit's strength

A-69: "losses are written". The owner is the army Record's unit row (A-2), through the army verbs' one write
path, as `04_MB_campaign_party_economy.md` §1 writes `experience`.

- `assigned` counts fall by the whole loss: dead, injured, fled and taken.
- The unit row gains one column, `absent: ((cohort, kind, count), ...)`, `kind` in the closed set
  `(injured, fled)`, exported with the Record's key set. Men in `absent` are alive, are still the cohort's,
  and still count against what the army may hold of that cohort (`armyrecord.cohort_claims`).
- `armyrecord` gains two ops on the existing `mass_battle.army` composition row: `lose` (args: unit, and per
  cohort the four counts) and `restore` (args: unit, cohort, kind, count).
- **The read moves with the write** (`CLAUDE.md` §0.1 pt 1). Today strength is `assigned × the cohort's body
  share`; under `recuperation: on` it is `assigned` alone, because the loss is now in `assigned`. Both
  constructors that read fitness (`armyrecord.to_order_of_battle`, `seam/wrappers/mass_battle.py::_order_of_battle`)
  change in the same commit as `_eff_march`'s write; a field that scaled a cohort's body **and** lowered
  `assigned` would count the loss twice. Gate 2 is the falsifier.
- **The cohort.** Its dead are its own loss. Until SE and the census own a cohort's deaths
  (`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`; `U5d_SE_cohort_heavy_moves_and_caste.md`, both
  cited by title and not opened by this lane), `_eff_march` scales a cohort's `body` by its **dead share
  only**. `tend` then mends the place and no longer refills the unit: a unit is made up again by
  `assign_troops` or by §3.
- **The headcount path** (persons at weight, no army Record) is unchanged: a person's loss is already an
  injury on his own `body`, which his own recovery and `tend` restore, and a death is `_eff_kill`'s.
- **Both sides, the same way.** The write is per unit row and does not ask who won or who marched. A-69
  leaves the defender's case "taken to be yes by symmetry"; this is symmetric by construction.

### 3. Return is a draw, graded, and never a fixed share of the absent

**The injured** recover as the world moves (A-54: the world's motion is a draw on the one ladder, a place's
endurance against the season's hardship, and a person's skill bears on it). Once a round, for each unit row
with injured men, where the army stands:

```
pool      the endurance of the place the army is stationed at            (A-54's pool; the WR lane's reader)
levels    + a healer's `tend` on the army this round (his `healing` rank, as a named level for the roll)
obstacle  the season's hardship                                            (A-54's obstacle)
          + the army marched this round        + its ration was short (SE's debit)
          + the unit ended its last field routed
band  ->  aftermath.recover_share[band] of the injured return to `assigned`; the rest stay absent
          and are drawn again next round
```

- The four terms are A-69's four words: rest (did it march), supply (the ration), place (the station's
  endurance), the unit's state. Whether a Failure may also turn some injured to dead is not established and
  ships off (`aftermath.wounds_turn: off`).
- Injured men still absent after `aftermath.window` rounds are struck from `absent`: they have gone home or
  died, and the row stops carrying them. The window is not established; it is a parameter.

**The fled.** Whether they come back unprompted is not established (above). Decided by the ladder, step 4,
and reversible by one switch: **they return when recalled, and the recall can be refused.**

- Precedent: nothing but a person acts (`14_VERBS_MILITARY_D_the_order_of_battle.md` §5, on ED-IN-0306), and
  the common people have "comply or refuse" among their few heavy moves (A-56). A levy that ran went home;
  home is its cohort. So the commander's `assign_troops` on a unit with fled men is the recall
  (`restore`, kind `fled`), drawn on his `command` as that verb already is, with the cohort's stance toward
  him and the unit's `arrears` as terms, and the band gives the share that answers. No new verb.
- The other arm, kept as the test's comparison: `fled_return: unprompted` runs the injured's draw for the
  fled as well, with distance from the cohort's home as a term.
- `fled_return: off` is the third arm: they never return. It is the control for both.
- What the page-read source does say (and it is about a rally on the field, not a return afterwards): light
  troops "simply turned and ran, and then rallied once they had temporarily outdistanced pursuit", and a
  leader stops a panic in person (MV P1, P2). That is the field's rally draw, already amended by troop weight
  (`26_…` §5), and is not evidence for either arm here.

### 4. Fatigue is carried on the one ledger

- `FieldOutcome` returns, per part, `stamina_left`: the troop-weighted mean of that unit's column blocks at
  the field's end (`Unit.agg_stamina()` as `16_PESSIMIST_MB_one_stamina_ledger.md` step 2 redefines it,
  taken per unit).
- The season records a crossing, not a level (the D-48 precedent: computed when read): the unit row holds
  `last_field: (round, stamina_left)`.
- At the next field `entry_stamina` for that part is computed when the input is built
  (`seam/wrappers/mass_battle.py::field_input`): in the **same round**, the `stamina_left` it holds plus one
  lull's recovery (`fatigue.lull_recover`), in place of the flat `fatigue.entry.second_field` seed of
  `26_MASS_BATTLE_movement_and_fatigue_as_data.md` §3, which becomes the fallback for a part with no record;
  in a **later round**, full, times that file's other entry writers (a hard march; a short ration).
- **I do not know how long a season round is in the fiction** (A-51's record says it must be read from the
  code; this lane did not read it), so whether tiredness should outlast a round boundary is not decided here.
  `fatigue.carry_rounds` (0: within a round only) is the parameter, and its control is 0.
- A drawn aggressor returns to his station at once (A-67, A-68), and a drawn defender to his own base
  (A-70), each carrying exactly this: the row's lowered `assigned`, its `absent` men and its `last_field`.

### 5. Calibration targets (orderings; no historical figure exists to set a band)

Read on the instrument of `26_MASS_BATTLE_calibration_targets.md` §2, as rows T-11 to T-17 of its table;
n at least 400; each parameter swept at three points (the `assumption` grade's rule: inject, declare the
site, sweep three points), and an ordering must hold at all three to count.

| id | reading | what must hold | control |
|---|---|---|---|
| T-11 | of a unit's loss, the share that is recoverable | strictly between 0 and 1 in the mean; not the same at every seed | `recuperation: off` reads 1 (today: all of it) |
| T-12 | recoverable share of a routed, unrallied unit against a unit that stood, at equal loss | higher for the routed unit | the same units with `fled_share` zeroed: equal |
| T-13 | recoverable share of a unit pursued by horse against the same unit unpursued | lower when pursued | no horse on either side |
| T-14 | strength three rounds after a lost field | above its strength just after the field and below its strength before, in most seeds; equal to neither in all | `off` |
| T-15 | injured returned after one round at a supplied home station against on the march and short of ration | higher at rest; neither 0 nor all | the terms zeroed: equal |
| T-16 | fled men returned under `recalled` by a commander at `command` 5 against 0, and against no recall | higher; higher; zero with no recall | `unprompted`: above zero with no recall |
| T-17 | a side fighting its second field of a round against its rested mirror | loses more often than the mirror by more than the sampling band; its `entry_stamina` equals the first field's `stamina_left` plus one lull | `carry: off` |

No band is a number from history. If a source search (§6) later files one, it joins as a flag, never as a
gate, exactly as T-1 does.

### 6. The source search owed before any figure is used

To be filed as `research/historical/mass_battle_aftermath_grounding.md`, with the tier of each row
(`AUDIT_BRIEF.md`, the grounding rule), by whoever calibrates:

1. Wounded beside killed in pre-gunpowder field battles: any source giving both for one army. The one case
   filed is CR A9.
2. Return to the ranks: how many of the wounded fought again, and after how long.
3. Stragglers and deserters after a defeat: whether a beaten army's numbers rose again in the following days
   without a muster, and by what means they were gathered where they were.
4. Whether a victor's holding the field changed his own wounded's fate.

The works audit 26 lists as not reached at any tier above a snippet (`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`
§0, "What was sourced") are where to begin; nothing is attributed to them here.

## Exact edits

| file (owner) | edit |
|---|---|
| `engine/season/queries/inputs.py::FieldOutcome` parts (IN) | `stamina_left`; the end-state word per part |
| `modules/mass_battle/armyrecord.py` (MB) | the `absent` column; `lose`, `restore`; `to_order_of_battle` reads `assigned` alone under the arm; `options()` reports units with absent men |
| `engine/season/rosters.yaml: record_kinds.values.army` (IN) | the unit row's key set gains `absent`, `last_field` |
| `engine/season/loop/effects_combat.py::_eff_march` (IN) | the two draws of §1; `lose` through the army write path; the cohort's body by the dead share only; `last_field` |
| `engine/season/seam/wrappers/mass_battle.py` (IN) | `_order_of_battle` stops passing fitness under the arm; `field_input` computes `entry_stamina` per part from `last_field` |
| the world-motion step (WR; A-54's owner) | the injured's recovery draw as one more motion, reading the Record |
| `engine/season/loop/effects_army.py` (IN) | `assign_troops` on a unit with fled men is the recall |
| `references/troops.yaml: aftermath`, `fatigue.carry_rounds` (MB) | the tables and switches; every value marked not established |

## Gate (execution artifacts)

1. `recuperation: off`: hashes EQUAL; 200 seeded army fields fold to the same cohort bodies as before.
2. **No double count.** One army field folded with the arm on: for each unit, `assigned` after equals
   `assigned` before less the four kinds; the unit's strength at an immediate second field equals `assigned`;
   a planted "still multiply by fitness" reddens it.
3. Over 400 routed fields: a routed unrallied unit has fled men in some seeds and none in some; a unit that
   stood has none in all; a rallied unit has none in all.
4. Three rounds after a lost field, 200 seeds: some injured have returned and some have not, in most seeds;
   the dead count is unchanged by any `tend`.
5. Under `recalled`: with no `assign_troops`, no fled man returns in any seed; with it, some return in some
   seeds and the act's Failure band returns none. Under `unprompted`: some return with no act.
6. Two fields in one round for the same army: the second field's `entry_stamina` per part equals the first's
   `stamina_left` plus one lull's recovery, asserted on the built input.
7. Rows T-11 to T-17 print with their controls; a row whose mechanism is off prints "no mechanism".

## Falsifier

A unit whose every loss returns, or none, at every seed. A return of the same share at every seed. A dead man
restored by `tend`. A loss present in both the cohort's body and the unit's `assigned`. A second field in a
round entered at full stamina. Any figure for a ratio, a rate or a window appearing in the troop file without
a filed source row or a Jordan-set value.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** Top-down: the ruling. Bottom-up: the field already knows who routed, who was pursued and who was
  taken, and the season throws that away. Lateral: a person's wound heals by his own ladder; a unit's
  injured get its like. Vertical: a battle's cost reaches the next battle and the town that gave the men.
  Diagonal: a short ration or an unpaid army slows its mending. Horizontal: winner and loser alike. Cut it
  and a defeat is one `tend` from never having happened.
- **R.** Whether to fight again at once or wait for the hurt; whether to spend standing with a levy calling
  it back; an army that never recovers because nobody could feed it. With no player, armies waste and mend.
- **S.** One ledger for fatigue; one owner for strength; the recovery is the world's one motion draw; the
  recall is a verb that exists.
- **E, against that.** One column, two ops, two draws at one write, one motion, one switch; a certain,
  total restoration leaves.

## Cost class

Small build for §2 and §4. Design-first for §1's and §3's magnitudes: the form can land behind its arm; no
value ships until §6 is filed or Jordan sets one.
