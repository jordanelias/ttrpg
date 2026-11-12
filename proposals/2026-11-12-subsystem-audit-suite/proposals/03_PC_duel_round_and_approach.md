# PC — one duel round as the unit of play: the approach choice, the round entry, the grid seam, the field's duel, and the NPC's decider

## Status: PROPOSED

Lane: PC, with CORE (the suspension), MB (a duel inside a field) and CHAR (the NPC's temperament).
Source: Jordan's design intent of 2026-11-12 (`AUDIT_BRIEF.md`, "Design intent … personal combat" and
"… mass battle"); `audits/03_PC_audit.md` F-PC-13, F-PC-14, §9, §10, §14. Read at `601e715`. Reference
only (CLAUDE.md §0.05); not ratified by being written. §6 names five conflicts with ruled, ratified or
recorded items and resolves none of them.

## What it changes in `engine/season/` at runtime

As built in the order given: step 1 changes nothing (a refactor with an equality control); step 2
re-seeds every fight per round, a declared mover of every season fight; step 3 changes nothing while
every approach is `normal`; steps 4 and 5 add callers.

## 1. The intent, set against the code

| the intent asks | what the module has today | gap |
|---|---|---|
| each character equips a weapon, armour and a suite of skills that correspond to levers | `Combatant(weapon, armor, skills, equipped, tradition)`; six skill axes; fifteen levers; the record carries weapon and armour only | the record cannot carry skills or levers; no off-hand or shield slot; no host carrier (`03_PC_person_inputs_content.md`) |
| an approach chosen per phase: aggressive, normal, defensive | `disp`, one aggression value fixed for the whole fight, with three hooks: commit-depth skew, counter selection, initiative drift (`config.py:280-286`). The per-turn decider's closed set is `{engage, withdraw}` (`wrapper.py:552-553`) | no per-phase approach; and the axis is monotone: aggressive `disp 7` wins 56.3% and is felled less often than the mirror, cautious `disp 1` wins 41.4% (1,000 fights each). A choice with a dominant answer is not a choice |
| moment by moment as a duel | one provider call runs the whole fight; a played person is asked once per turn inside that frame | the phase exists (one `engagement`, about ten seconds); nothing is shown between phases except what a client renders from the trace |
| inside grid combat the duel round resolves automatically from the selected approach, and returns to the grid | none. There is no entry that fights one round: `fight.py` exposes the whole fight only, and the tracker's damage is zeroed at each call (`wrapper.py:570`) | a round entry and a carried round state |
| both modes one code path | one resolver; `wrapper.fight` already is a loop over `engagement` (`wrapper.py:576-615`) | the loop is not exposed at its own joint |

## 2. The round is the unit (the structure)

`wrapper.fight` is already "an outer loop over one engagement"; its own comment says the game calls
one engagement per turn (`wrapper.py:576`). Expose that joint and let everything else compose on it.

```python
# engine/season/queries/inputs.py
@dataclass(frozen=True)
class DuelState:                 # what one party carries from round to round; held by the HOST, never by the module
    cumulative_damage: int = 0
    stamina: Optional[float] = None      # None: start of a fight (the module derives the maximum)
    conc: Optional[float] = None
    poise: float = 1.0

@dataclass(frozen=True)
class DuelRoundInput:
    fighters: PersonalCombatInput        # who they are: ends, attributes, kits, faculties, slots, terms
    states: tuple                        # (DuelState, DuelState), in claimant order
    approaches: tuple                    # one member of APPROACHES per party
    round: int                           # 1-based
    prev_closed: bool = False            # the measure the last round ended in

@dataclass(frozen=True)
class DuelRoundOutcome:
    states: tuple                        # the two DuelStates after the round
    wounds: Mapping                      # id -> PartyWounds, as CombatOutcome carries them
    felled: Optional[str]
    yielded: Optional[str]               # set when the fighters' terms were met this round
    closed: bool
    trace: tuple                         # this round's events
```

- `modules/combat/fight.py` gains `round(inp: DuelRoundInput, rng) -> DuelRoundOutcome`: build the two
  Combatants, apply each `DuelState` (seeded damage, stamina, concentration, poise), set each party's
  approach, call `wrapper.engagement` once, apply the between-round recovery `wrapper.fight` applies
  now (`wrapper.py:613-615`), lift the states. It keeps nothing.
- `fight(inp, rng, decide)` becomes the loop over `round`: for each turn ask each party's decider for
  an approach (or `withdraw`), draw that round's private stream from the fight's stream
  (`random.Random(rng.getrandbits(64))`), call `round`, stop on a felling, a yield, a withdrawal or the
  twelfth turn. `wrapper.fight` shrinks to that loop or is deleted in its favour; the upset flip stays
  where it is, on the integer nobody in a season reads.
- A second composition row registers the round entry (`references/module_contracts.yaml`,
  `composition_roles:`, target `modules.combat.fight:round`), so a host reaches it by role, never by
  import.

**The three modes are then three callers of one function.**

| mode | caller | who supplies the approach | when the world is written |
|---|---|---|---|
| AUTOMATED fight | `fight`, from the season's provider | each party's decider; an NPC's is §4 | once, after the loop (as now) |
| duel, moment by moment | the same `fight`, with a played party's decider called between rounds and the round's trace rendered before the next question | the player | once, after the loop |
| grid round | the grid host calls `round` once per attack action, carrying the two `DuelState`s on its units | the acting unit's player or NPC decider | when the grid battle folds |

A grid attack and a duel turn are the same call with the same record; the grid only decides when the
next round happens and who else acts in between. The per-round stream makes a fight replay equal
whether its rounds are called in one frame or across grid turns: round `r`'s seed is the `r`-th
64-bit draw of the fight's seed, recomputable from `(seed, r)` with nothing stored.

## 3. The approach (the choice surface)

- `modules/combat/wrapper.py`: `APPROACHES = ('aggressive', 'normal', 'defensive')`, a closed set
  beside `TURN_CHOICES`; the decider's set becomes `APPROACHES + ('withdraw',)`, with `engage` kept as
  a synonym of `normal` so every existing decider is unchanged.
- An approach is a **prior on gates the engine already rolls**, never a command (the held Plan-layer
  proposal's rule, and ED-PC-0023's ruling against imposed outcomes): it sets a per-round lean that is
  added to `disp_lean` for that round, so it moves the commit-depth Beta, counter selection and
  initiative drift through the three hooks that exist. `normal` is lean 0: byte-identical.
- **Both ends must cost, in the same change.** Today the aggressive end is strictly better. The engine
  already has the cost side and under-charges it: deep commits raise `overcommit_exposure`
  (`combat_systems.py:1164-1175`) and readiness debt (`wrapper.py:287`), and a defender who out-reads
  a deep commit steals the initiative (`wrapper.py:325-329`). The proposal adds no new mechanic; it
  requires that the lean's magnitude and the three existing cost coefficients be swept together on the
  workbench until, in a mirror, no approach beats `normal` by more than the disjoint-seed band and
  each approach beats one other in some matchup (aggressive against a wounded or out-reached
  opponent; defensive against an aggressive one). The values are `[SIM-CALIBRATE]` and go in `CFG`.
- A skill or lever a character has equipped modulates the gates an approach leans on, which is the
  sense in which "skills correspond to levers": a fighter with a counter lever gains more from
  `defensive`, one with a tempo lever from `aggressive`.

## 4. The NPC's decider (one interface for a player and an NPC)

- The decider is per party: `deciders: Mapping[id, Callable[[CombatTurnView], str]]`. The host supplies
  the player's for a played person and the NPC's for everyone else; the module asks both the same
  question in claimant order. `decide=None` remains "normal every round".
- `CombatTurnView` gains what a fighter can see of the fight: both parties' lifted wounds (as now),
  the round, whether the measure is closed, and his own approach last round. It still carries no
  `Combatant` and no `World`.
- The NPC's policy is the chooser's, not the module's: `engine/season/decision/` gains one function
  that maps a person's own interior and the view to an approach. Its inputs are person-side only (AX-2):
  the temperament CHAR establishes for him, his stake in the fight, and the view. The intent for NPCs
  and the chooser is stated in `audits/02_CHAR_audit.md` (the section on the NPC and chooser intent);
  this proposal consumes that statement and adds no rule of its own. Until CHAR supplies a temperament
  reading the NPC decider returns `normal`, which is today's fight.
- The concession threshold (`YIELD_HEALTH_FRAC`, one number for everyone) becomes a per-party input on
  the record when CHAR names its source; until then it stays the config value.
- The reason trail: each round's trace gains one `approach` event per party with the view fields the
  decider read; the band's Event already carries the ending, and `03_PC_typed_outcome_one_door.md`
  adds the decisive beat.

## 5. A duel inside a field (the interface the MB lane needs)

Today no edge exists between the two modules. With the round entry a duel can be embedded in a mass
engagement through the same path:

- The field's battle loop reports a **contact**: two named persons (officers, champions) in adjacent
  cells this field turn. It does not resolve it.
- The field's host adapter (`engine/season/seam/wrappers/mass_battle.py`), which already calls a
  second module entry by role for provisioning, builds a `DuelRoundInput` for the pair (their records
  from `combat_input`, their `DuelState`s carried on the adapter's side for the length of the battle)
  and calls the `combat.round` role. One field turn is one duel round.
- It hands the field module a typed result: `DuelContactResult(pair, felled, wounded, yielded)`.
  What the field does with it is MB's rule; the borrowed constraint from research is that a person's
  effect on a unit is a fraction of the unit's own cohesion, never a flat amount, because no surveyed
  game holds one person's leverage from 1 to 1,000 (`research/by_lane/PC_personal_combat.md` T-PC-15).
- A played commander is asked for his approach through the same decider; an auto-resolved battle uses
  the NPC decider for both. Fought and auto-resolved are then the same rounds.
- A duel that **arises from** a field (champions meeting before the lines close) is the existing
  `challenge` and `accept` pair with `stakes`, issued by the commanders; nothing new in combat.

What MB needs from combat, stated as the interface: the `combat.round` composition role; `DuelState`,
`DuelRoundInput`, `DuelRoundOutcome` in `queries/inputs.py`; the guarantee that the entry keeps no
state and draws only from the stream it is handed.

### 5.1 Squads of named characters and a commander in the field (the named referents)

Jordan's referents for mass battle are Ogre Battle, Unicorn Overlord, Football Manager, Total War and
Mount & Blade II: Bannerlord. Two of their shapes touch this module, and the same round serves both.

- **Squads resolved automatically from standing orders** (Ogre Battle, Unicorn Overlord). A squad
  exchange is a set of pairings, each one duel round; outnumbering is more rounds against one
  fighter's carried `DuelState` in the same field turn, which is the arithmetic the WS-7 envelope
  already describes. The approach each member takes comes from a **standing order**: an ordered list
  of `(condition over the turn view, approach)` rows, authored as data and evaluated host-side into the
  same per-party decider the player and the chooser supply. So "the player picks an approach", "the
  NPC's chooser picks one" and "a standing order picks one" are three suppliers of one callable, and
  the module cannot tell them apart. Who is paired with whom is the squad host's policy, not combat's.
- **A commander and companions fighting inside a field battle** (Bannerlord). This is §5's contact:
  a named person met on the field fights rounds through the role; a played commander is asked for his
  approach, an unplayed one is served by the chooser or by his standing order.

Interface added by these two, beyond §5: nothing in `modules/combat/`. Host-side: a `StandingOrder`
record (rows of condition and approach, the conditions a closed set over `CombatTurnView`'s fields:
own wounds, opponent's wounds, round, measure closed) and one function that turns it into a decider.
Its owner is the lane that owns squads and orders (MB, with the capability surface for who may hold
which order); combat only promises that the view carries what those conditions read.

Cost and a limit, measured: 200 whole fights (about 600 rounds) ran in about 0.4 s here, so one round
is well under a millisecond and a squad battle of two fives over ten field turns is tens of
milliseconds. That holds for named characters. It does not make per-soldier rounds for a mass unit
sensible, and nothing here proposes them: a headcount fights as the field resolves it, and a cohort
is never a party to a personal fight (CP-T03-01, ruled). Whether a side fights as one body or as its
commanding persons is H-359's question and MB's.

## 6. Conflicts with ruled or ratified items (named, not resolved)

1. **The ratified suspension (`proposals/2026-10-07-grid-mode-suspension.md`, REM-31).** It covers
   "one provider call for one deferred act", with a decider that draws nothing and mutates nothing,
   and lists "the grid map" under "Not decided here". A grid battle in which other units act between
   two rounds of one pair cannot run inside that decider. Either the grid battle is its own suspended
   scene that calls `combat.round` (this proposal's reading), or the suspension is re-designed; that is
   CORE's and Jordan's.
2. **R-04's reading of "grid-based map combat with units"** (`engine/season/requirements.yaml`, the
   combat scale row, `[ASSUMPTION; medium; Jordan to correct]`): it takes the grid to be mass battle's
   cell field. The intent describes a tactics-game grid on which individual units duel. The two
   readings name different builds.
3. **CR-85 §4 step 2 (held; ratification withdrawn, ED-IN-0351).** A round entry needs damage carried
   into a call, which is that step's seeded `cumulative_damage`. Building `DuelState` decides in
   practice a question that is formally held.
4. **ED-PC-0007** (deferred; "reopen only if `combat_engine_v1` grows a discrete player-action menu").
   Three approaches are such a menu; its reopen condition fires.

5. **`videogame_mode_spec.md`** (quarantined, headed CANONICAL, intent only): "Zone-based positioning:
   Use. No grid. Zones: Melee / Reach / Ranged / Out." The stated intent of 2026-11-12 asks for a
   tactics-game grid. The later statement is the newer intent; the code has neither zones nor a grid.

Also touched, not in conflict: J-15 (whether an unwatched fight is one act or spans scenes) is
answered for the played case by the intent and left open for the unwatched one.

**Design intent this composes on (quarantined documents, read for intent only, CLAUDE.md §0.05).**

- `auto_manual_resolution_duality_v1.md` (headed "Doctrine RULED 2026-07-08", ED-SC-0013 `[UNVERIFIED:
  the ledger row was not opened]`): one engine at three fidelities (played, witnessed, auto), with the
  calibration constraint that the expected outcome of an event be the same at each fidelity on matched
  inputs, so that choosing a fidelity is never a strategic advantage. The round entry is that one
  engine; §7's step 4 gate is the constraint's test for combat; and the free withdrawal measured in
  `03_PC_exits_withdrawal_recovery.md` Part A (a played fighter's death falling from 52% to 14%) is a
  breach of it in the tree today.
- `scene_combat_design_v1.md` (WS-7, design-only, gated on ED-911): a multi-combatant scene is "a
  second outer loop parallel to `fight()`" that calls `engagement()` for many pairs, "wrap, never
  fork". The grid host of §2 and the field contact of §5 are that outer loop; the difference is that
  here the round's carried state is a typed record the host holds, because a registered module keeps
  none, where the WS-7 sketch keeps `Combatant` objects alive inside the envelope.

## 7. Build order and gates

| step | change | gate (execution artifact) |
|---|---|---|
| 1 | `fight.round` and `fight` as a loop over it, drawing from the one stream as now | every existing combat test and season hash unchanged (hash EQUAL); `round` called twelve times by hand equals `fight` at three seeds |
| 2 | the per-round private stream | a fight run in one call and the same fight run as separate `round` calls from `(seed, r)` give identical outcomes; season pins re-recorded once, declared |
| 3 | `APPROACHES`, the lean, the swept costs | all-`normal` byte-identical to step 2; the workbench table: in a mirror no approach outside the control band of `normal`; each approach best in at least one named matchup |
| 4 | per-party deciders, the widened view, the chooser's NPC decider (returns `normal` until CHAR supplies temperament) | REM-31's equality test green; a scripted NPC decider that differs moves the hash; the fidelity reading: over 300 seeds, the played fighter's felled share under the best of a small set of scripted policies, set beside his share under the NPC decider, with the disjoint-seed band, reported in the commit body |
| 5 | the `combat.round` role called from the field adapter on a reported contact | a seeded field with two planted officers in contact shows one duel round per field turn in the trace and a `DuelContactResult` in the field's result; with the contact report off, the field's hash is unchanged |

## 8. Falsifier

A grid attack whose result differs from the same round inside a duel at the same seed and state; an
approach that is best in every matchup after step 3; an NPC whose in-fight choice is made by a rule
inside `modules/combat/` rather than by the chooser; a module attribute or cache that changes between
two `round` calls.

## 9. NERS reading

- N: from above, the stated intent has no carrier for its central choice; from the player's side the
  fight offers one binary; from below, the engagement is already the engine's unit and is hidden;
  laterally, the grid and the field need the same call. Without the round, each of the three modes
  would need its own loop.
- R: a per-phase choice with both ends priced is strategy; an NPC who fights in character produces
  fights worth retelling with no player present; a champion's duel inside a battle is a hook.
- S: one round at every scale (duel, grid, field); the scales pause at a round boundary; one decider
  interface for the player and the NPC; the approach reuses the disposition hooks, adding no second
  aggression axis.
- E, last: three records, one entry, one closed set, no new resolver. High, on the condition that the
  approach's costs are calibrated before it ships.

## 10. Cost class

Steps 1, 2 and 4: small builds. Step 3: small build plus a calibration pass on the workbench. Step 5:
small build in the MB adapter, design-first on the MB side for what a contact is and what its result
does to a unit.
