# PC round — a personal-combat fight is a sequence of rounds (A-101): the definition, the engine mapping, the sweep and the coding items

## Status: PROPOSAL (lane `master/pc_round/`, 2026-11-12; reference, resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Lane: PC (with MB for the nested duel round and CORE for the season's word). Ruling served: A-101 as amended the
same day (`unified/DECISIONS_ANSWERED.md:137`): a round is one engagement in which two combatants close, exchange
attempts to attack, then disengage and create distance again; *"the 4-10 seconds is not absolute but an indicator
of how to cap exchanges roughly"*; the model is boxing and fencing, *"lots of closing to attack and separating to
disengage"*. Decided by the five-step ladder (CLAUDE.md §0); what survives the ladder is in `PCR_FOR_JORDAN.md`
beside this file. Parts: this file (§1 verdict, §2 definition, §3 mapping); `PC_ROUND_SPEC_part2.md` (§4 sweep and
clock table, §5 what the mass-battle abstraction lane should assume, §6 coding items).

**Read for this file** (each opened): `modules/combat/wrapper.py` (whole), `modules/combat/fight.py` (whole),
`modules/combat/config.py` (whole), `engine/substrate/pc_engine.py`, `engine/season/seam/wrappers/combat.py`
(head, `:395-423`), `engine/season/queries/inputs.py` (`PersonalCombatInput`, `CombatTurnView`),
`engine/season/state/carriers.py` (`Claim.round`, `:327-357`), `engine/season/loop/deliberate.py` (`:93-121`),
`architecture/meta/04_CODE_ARCHITECTURE.md` (rows 19, 22; the row-52 clauses at `:177`, `:654`), the suite's
`03_PC_duel_round_and_approach.md` (PA) and `_B.md` (PB) whole, `03_PC_typed_outcome_one_door.md` (`:1-100`),
`unified/U1_GLOSSARY.md` (§E, §J, the round row), `unified/U1_OWNERS_AND_VOCABULARY.md:355`,
`unified/MB_LEXICON_part2.md` (bout, tick, engagement, duel round rows), `unified/MB_LEXICON_part3.md` D-7,
`unified/U3_DEPENDENCY_ORDER.md` (B14–B16, B30). **Research:** none in `research/` on the duration or tempo of a
duel or of melee (searched `research/` for seconds, phrase, bout, tempo, duel, fencing, boxing:
`research/by_lane/PC_personal_combat.md:227` records the duelling-custom gap; nothing on timing). Every seconds
figure below is therefore marked an estimate.

---

## 1. Verdict: the engine already fights in rounds; three things keep them from being A-101's rounds

**Yes — the round exists in the engine, under three other names.** `modules/combat/wrapper.py::engagement`
(`:76-481`) is one round: it opens at measure (`:82-146`, the open-measure reset, the closed latch, the
re-presentation gate), runs an approach phase while the measure is open (`:221-262`: the longer weapon's
stop-hits, the closer's step), then a tempo-gated closed exchange (`:264-469`), and returns at a **separation**
(`_emit('separation', reason=…)`: `clean_defence` `:480`, `burst_ceiling` `:479`, `collapse` `:261`, `:478`,
`terms` `:154`, `beat_exhaustion` `:481`) or a felling. Its own comment states Jordan's shape of 2026-06-03:
*"TURN = one approach -> burst -> separation"* (`:471`). `wrapper.fight` (`:555-625`) is the loop over it, at most
`max_bouts=12` iterations, each commented *"ONE engagement (~10s turn)"* (`:576`), with the between-round recovery
of stamina and concentration (`:613-615`). The code calls the one thing an **engagement** (the function), a
**turn** (`turn_start`, `decide(turn)`, `Yield.turn`, `TURN_CHOICES`, `CombatTurnView`) and a **bout**
(`max_bouts`; the seam's `bouts` count, `seam/wrappers/combat.py:415`). The suite's PA and PB already took
"the round is `wrapper.engagement`" (PA §2, PB §1 "Stands").

**What a beat is.** A beat is **one step of the engagement's loop** (`while beats < cfg['BEAT_BUDGET']`, `:147`):
both fighters' readiness advances by cadence times anticipation (`:180`); in the open measure a beat is one step
of the closing with at most one stop-hit (`:240`); at closed measure a beat holds **at most one attack attempt**,
by whichever fighter's readiness crossed `ACT_THRESHOLD` (`:264-270`), or none (`if not actors: continue`,
`:265`); a bind adds up to three sub-beats (`:431-432`). So a beat is not an attack and not an exchange of both
sides: it is the cadence step in which at most one attack is made.

**What an exchange is.** One closed-measure attack attempt and the defence against it, resolved in one beat:
the aggressor's commit, the read, the defence mode, the one roll (`core.resolve`, `:332`), the outcome
(hit, graze, bind, riposte opening, `:341-443`) and the contact tail (`:453-468`); one `outcome` event; counted by
`exchanges+=1` (`:470`). The **riposte** does not roll inside the exchange: it is the defender's opening, which
keeps the round going so that the next attack can be his (`:444-446`, `:480`). Either fighter may make the next
attack: who attacks is decided per beat by readiness, so a round is an exchange **of attempts by both sides** as
often as by one.

**What ends a round today, and how often** (the probe below): mostly a **clean defence** (an attack met with no
hit, no riposte and no bind: the measure breaks, the fencing phrase that ends on a parry); next, the **exchange
cap** `BURST_MAX=4` (`config.py:112`); rarely a stamina collapse; never, in the probe, the beat budget.

**The three things that keep the engine's round from being A-101's round.**

1. **A second closing inside one round (the continuous-melee residue).** When the measure re-opens inside an
   engagement — the longer weapon's created-moment reopen (`:186-191`) and the clean fighting withdrawal
   (`:206-210`) — the loop `continue`s into a new approach phase **in the same engagement**: the fighters separate
   and close again without a round boundary, so no between-round recovery, no fresh initiative and no decider
   consult happens. A-101 ends the round at the disengagement. Measured: 4.3% to 5.0% of rounds in
   reach-mismatched pairs, 0% in matched-reach mirrors.
2. **No one-round entry.** `modules/combat/fight.py` exposes `fight` only (`:55-117`); the round is reached only
   inside `wrapper.fight`'s loop, so a battle (A-4, A-72) cannot call one round, and the tracker's damage is
   zeroed at each call (`wrapper.py:570`). PB step 1 is the cure; this lane adds the round's typed ending.
3. **Three names for one thing, and a stated duration.** `turn`, `bout` and `engagement` all name the round in
   code; `wrapper.py:576` writes it as about ten seconds, as does PA §1 (`:34`) and `unified/work/R1_READ.md:326`.

### 1.1 The probe (the real engine, `PYTHONHASHSEED=0`, scratchpad, 3.2 s in total)

Scripts: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/probe.py`, `probe2.py`,
`probe3.py`. Each runs `wrapper.fight` through `engine/substrate/pc_engine.load()` at the engine's own defaults
(`Combatant(label, weapon=…, armor=…)`, every attribute at its class default), lethal terms, `random.Random(seed)`,
and reads the trace the engine emits (`wrapper._TRACE`, which draws nothing and mutates nothing: `:12-22`).
`probe.py`: seeds 1000–1149 per pair. `probe2.py`/`probe3.py`: seeds 5000–5119 per pair. A *round* below is one
`engagement` call; an *exchange* one `outcome` event; an *attack attempt* an exchange, a stop-hit or a pursuit
strike; a *loop beat* one iteration of `engagement`'s `while` (counted by wrapping `combat_systems.tempo_pressure`,
called twice per iteration; bind sub-beats excluded).

| pair (weapon/armour each side) | fights | rounds | rounds per fight (mean; range) | exchanges per round (mean; distribution) | attack attempts per round (mean; max) | loop beats per round (mean; max) | both sides attacked | re-opened inside the round | round ended by |
|---|---|---|---|---|---|---|---|---|---|
| arming/light v arming/light (seeds 1000+) | 150 | 519 | 3.46; 1–12 | 1.82; 1:260 2:134 3:82 4:43 | — | — | — | — | clean defence 341, felled 149, cap 29 |
| arming/light v arming/light (seeds 5000+) | 120 | 421 | 3.5 | 1.87; max 4 | 1.87; 4 | 2.2; 5 | 54% | 0.0% | clean defence 272, felled 120, cap 29 |
| mace/heavy v longsword/heavy | 150 | 598 | 3.99; 1–12 | 1.96; 0:6 1:274 2:143 3:86 4:89 | — | — | — | — | clean defence 369, felled 149, cap 79, collapse 1 |
| poleaxe/heavy v longsword/heavy | 120 | 348 | 2.9 | 1.90; max 4 | 2.51; 6 | 5.9; 12 | 52% | 4.3% | clean defence 171, felled 120, cap 57 |
| rapier/none v arming/light | 120 | 338 | 2.8 | 1.61; max 4 | 2.02; 5 | — | 42% | 5.0% | clean defence 198, felled 120, cap 20 |
| staff/none v dagger/none | 120 | 166 | 1.4 | 0.73; max 4 | 2.67; 5 | 6.3; 19 | 18% | 4.8% | felled 120, clean defence 41, cap 5 |
| spear/none v arming/none | 120 | 130 | 1.1 | 0.16; max 4 | 2.22; 5 | — | 4% | 0.0% | felled 120, clean defence 8, cap 2 |
| longsword/none v spear/none | 150 | 188 | 1.25; 1–3 | 0.58; 0:131 | — | — | — | — | felled 150, clean defence 36, cap 2 |

**Controls** (arming mirror, seeds 1000–1149, `CFG` overlaid per run): `BURST_MAX=99` (no cap): 488 rounds,
exchanges per round 1.91, distribution 1:236 2:128 3:81 4:25 5:11 6:5 7:2 — the natural tail past four is 18 of
488 rounds (3.7%), so the cap of four binds the arming mirror in 29 of 519 rounds (5.6%) and the heavy pair in 79 of
598 (13.2%). `BURST_MAX=1`: 858 rounds, every one a single exchange, 5.72 rounds per fight (twelve rounds fought in 6
fights, 3 of them unresolved at the budget). The controls show the instrument sees the cap: the round's exchange count follows `BURST_MAX`.

**Instrument note (a failure, stated):** `probe2.py`'s own loop-beat column read 0 for every pair (it counted
calls of `weapon_tempo`/`close_tempo` and reset its counter on a trace event; the count did not take); it is
discarded and `probe3.py` re-measured loop beats by a different hook on the same seeds (outcomes identical, the
wrapped function draws nothing). The `—` cells were not measured by the run that produced the row.

**What the numbers say.** (a) A round is short and mostly ends on a clean defence: in matched pairs 1.8–1.9
exchanges, half the rounds with attacks from both sides. (b) The cap of four is a ceiling the engine reaches in
5–13% of rounds, with a thin natural tail past it: it is the cap, not the usual ending. (c) Where reach differs,
the round is dominated by the approach (stop-hits), and the engine already counts those as part of the round.
(d) **The fights are short and one-sided where reach differs** (spear v arming: 1.1 rounds, 120 of 120 fights
felled): that is F-PC-04 and A-31's calibration (B15), not a round defect; a duel of "lots of closing and
separating" needs A-31's longer fight to be visible in the numbers. Every figure here is the pre-B15 engine.

---

## 2. The definition, decided

Each clause gives the decision, then the ladder step that decides it (CLAUDE.md §0: 1 superseded, 2 irrelevant,
3 design document, 4 precedent, 5 architecture). Jordan's own words are A-101's; nothing below overwrites them.

### 2.1 Words (one meaning each; the glossary rows in part 2 §4.3 carry them)

| word | meaning | code it names today |
|---|---|---|
| **fight** | the whole personal contest between two persons, from the first round to its ending | `wrapper.fight`; `modules/combat/fight.py::fight` |
| **round** | one engagement: the two close, exchange attempts to attack, and separate (A-101) | one call of `wrapper.engagement` (code name kept: §3.4) |
| **closing** | the part of a round in which the gap is closed: the approach while the measure is open, with the longer weapon's stop-hits; instant when the reaches are near equal or the closer is not held off (the closed latch and the re-presentation gate, `wrapper.py:98-124`) | the `if not closed:` block, `:221-262` |
| **exchange** | one closed-measure attack attempt and the defence against it, resolved in one beat | one `outcome` event; `exchanges` (`:470`) |
| **attack attempt** | any attack in a round: an exchange's attack, a stop-hit on the closing, a pursuit strike on a read withdrawal | `roll`, `stophit`, `disengage(pursued=True)` events |
| **separation** | the end of a round with both standing: the fighters are apart | `_emit('separation', reason=…)` |
| **beat** | one step of the round's loop, in which at most one attack is made; the engine's unit of cadence, never a unit of time a player sees | one iteration of `while beats < BEAT_BUDGET` (`:147`) |
| **phase** | one of the round's three states a fighter can lean in: `measure`, `exchange`, `bind` (PB §3) | PB's `PHASES` (proposed) |

"Turn" and "bout" are **not** words for any of these (part 2 §4: "turn" is A-9's scene sequence, "bout" is the
battle's 18 field ticks); "engagement" stays only as the code function's name.

### 2.2 The round: entry, the exchange, separation

- **Entry.** A round opens with the fighters apart, at open measure: grip and lunge reset (`:89-90`), each
  fighter's cadence phase drawn (`:140`), who presses first drawn (`wrapper.py:593`, moved inside the round by PB
  step 1), initiative even (`:127`). It then **closes**: an approach with stop-hits if one weapon outreaches the
  other beyond the latch band, or straight to closed measure if not. *Ladder 4 (the engine's own shape, Jordan
  2026-06-03 in `wrapper.py:471`) and A-101 ("close").* A closer the point cannot hold off (the re-presentation
  gate, ED-PC-0033, `:121-124`) re-closes at once: the fighters did separate at the end of the last round, and the
  next round's closing is instant. This reads the gate as part of the closing, not as a continuation of the last
  round, so it needs no change.
- **The exchange.** At closed measure, each beat, the fighter whose readiness crosses the threshold attacks (the
  higher readiness if both; a coin on an exact tie, `:266-269`); the other defends. **Both sides' attempts**, not
  the aggressor's and a reply: who attacks next is decided again each beat, so a fighter may land a combination
  (boxing) or the defender may take the next attack after a riposte opening. *Ladder 4 (as built) and A-101
  ("exchange attempts to attack", plural, no side named).* Measured: both fighters attacked in 52–54% of rounds
  in matched pairs (§1.1).
- **How many exchanges: the cap is four, a constant, `BURST_MAX = 4` in `CFG`.** *Ladder 4 and 5, with A-101's
  indicator.* (i) The band: Jordan's 4–10 seconds "is an indicator of how to cap exchanges roughly"; at an
  estimated 1 to 2 seconds per exchange and 2 to 3 seconds of closing and separating `[ESTIMATE: no research in
  the tree on duel tempo; the figures are the lane's reading of what a cut-and-parry or a thrust-and-void takes,
  not a measurement]`, a round of one to four exchanges reads about 3 to 11 seconds, and the cap of four sits at
  the top of the band. (ii) The engine: the cap exists, is exported with every `CFG` key, and binds in 5.6% (arming
  mirror) to 13.2% (heavy pair) of rounds with a thin natural tail past it (3.7% of uncapped rounds hold five to
  seven exchanges): it is a cap, not the common ending, which is what a rough cap should be. (iii) Not a function
  of state: the round's other endings already read state (a clean defence, a stamina collapse, a met term), and a
  cap computed from cadence would be a duration clock under another name, which A-101's amendment refuses. The
  closed range is **1 to 4 exchanges** per round at closed measure; stop-hits on the closing are attack attempts
  bounded by the closing itself (one per approach beat at most), not by the cap (measured attempts per round: max
  6).
- **What separates them (the disengagement triggers), as built and as changed.**

  | trigger | today | under A-101 | basis |
  |---|---|---|---|
  | a **clean defence**: an attack met with no hit, no riposte and no bind (`:480`) | ends the round | unchanged: the fencing phrase that ends on a parry or a void | ladder 4; Jordan 2026-06-03 (`:471-477`) |
  | a **hit landed**, a riposte opening, a bind | the pressing continues (`:480`) | unchanged: the boxing combination; the cap bounds it | ladder 4 (same comment): "a faster fighter can land SEVERAL hits in a single turn" |
  | the **exchange cap** (`:479`) | ends the round | unchanged | above |
  | **stamina collapse** (`:261`, `:478`) | ends the round; the fight goes on after the between-round recovery | unchanged: collapse ends the round, never the fight | ladder 4 |
  | the **fighting withdrawal**, clean (`:206-210`) | the round continues into a new approach (`continue`) | **ends the round** (`separation`, reason `disengage`); the next round opens at open measure with `prev_closed = False` | ladder 1: A-101 (later) defines the disengagement as the round's end; the code's in-round `continue` predates it |
  | the **created-moment reopen** by the longer weapon (`:186-191`) | the round continues into a new approach | **ends the round** (reason `reopen`), as above | ladder 1, as above |
  | a **read withdrawal** (pursued, `:211-219`) | the pursuer strikes and takes the tempo; the round continues | unchanged: the withdrawal failed, so they did not separate | ladder 5: no distance was made |
  | **poise loss** (a broken structure) | not a trigger; poise lowers defence and tempo (`config.py:245`) | not added | ladder 2/5: no ruling asks for it; adding a trigger moves every fight and would be a new mechanism; a calibration lane may test it as an arm |
  | the **beat budget** `BEAT_BUDGET = 24` (`:147`, `:481`) | ends the round | unchanged; it is a loop guard, never reached in the probe (max 19 loop beats) | ladder 5 |
  | the **duel's terms** met (`:153-154`) | ends the round; the fight then ends with the yield | unchanged | as built (RS-25) |
  | a **felling** | ends the round and the fight | unchanged | as built |

### 2.3 What ends a fight (between rounds or at a felling)

A fight ends at: a **felling** (inside a round); a **yield** — declared at the start of a round (`Yield`,
`:577-585`), by met terms at the end of a round (`:600-612`), or by the Spirit draw of
`16_PESSIMIST_PC_A_the_yield_is_a_draw.md` at the end of a round in which a wound gate was crossed (B15); a
**withdrawal** — the decider's `withdraw` at the start of a round (`:586-592`), priced by
`03_PC_exits_withdrawal_recovery.md` Part A (B16); the **round budget** — twelve rounds (`max_bouts=12`, renamed
`max_rounds`, §6), after which the fight is undecided (Jordan 2026-06-02, `:616-617`). **Stamina collapse is not a
fight ending:** it ends the round, and the fight resumes after the between-round recovery. *Ladder 4 (as built);
A-101's list.* The budget of twelve stands: the probe's fights take 1.1 to 4.0 rounds on average and twelve is
reached rarely (2 of 300 fights in the arming mirror and the mace-against-longsword heavy pair, `probe.py`). A-31's longer fight (B15) will raise the rounds per fight; B15's gate
reads the undecided share at twelve, which is where the budget is judged (PB's fold note: 0.1% undecided at the
re-read).

### 2.4 What is carried between rounds, and where it lives

The carried set is what PB's probe found differing at a later `turn_start` (PB §2): **damage (wounds),
stamina, concentration, poise and the weapon form**, plus the **measure the last round ended in**
(`prev_closed`, for the re-presentation gate). It lives in `DuelState` (and `DuelRoundInput.prev_closed`), held
**in the frame of the loop that calls the round** — the duel's `fight`, a skirmish's loop, a battle's loop — for
one provider call, never on an adapter, a module attribute or `World` (A-4; Layer 1 row 22 as amended).

| quantity | carried? | between rounds | code |
|---|---|---|---|
| wounds (cumulative damage) | yes | unchanged; a wound is A-8's level against the roll | `WoundTracker`; `DuelState.cumulative_damage` |
| stamina | yes | recovers `RECOVERY_FRAC` of the shortfall, scaled by `stamina_max / STAMINA_REF` | `wrapper.py:614` |
| concentration | yes | drains `CONC_DRAIN_BOUT`, recovers `CONC_RECOVER_FRAC` of the shortfall | `:615` |
| poise | yes | not reset; regenerates per beat inside the next round | `:166`; `DuelState.poise` |
| weapon form | yes until `03_PC_weapon_form_at_round_start.md` (B14) resets the grip form at round start; then the selected weapon (primary or secondary) | — | PB §2 `form` |
| initiative | **no: even at every round start** | reset to 0 | `:127` |
| grip, lunge, facing, swing room, selected mode | no | re-derived per beat | `:89-90`, `:161-172` |
| approach (PB) | no | asked again at the round's start and at each phase entry | PB §4 |

**Initiative does not carry.** A-101's record (`DECISIONS_ANSWERED.md:137`) lists initiative among the carried
state; that list is the record's gloss, not Jordan's quoted words, which name no quantity. *Ladder 1:* Jordan's own
cut of 2026-06-05 (`wrapper.py:125-127`: *"initiatives start even (0.0 …)"*, the pre-contact seizure verified
inert) is the ruling on the point, and A-101's words do not address it. *Ladder 4:* in fencing the right of way is
re-established at every halt, and a boxer's ring position resets at the break; separation is what resets the Vor.
What a round's ending does leave behind is the poise and stamina it cost, which is how pressing carries over.
Listed in `PCR_FOR_JORDAN.md` as information (the record's gloss differs), with no question.

### 2.5 What a round returns (A-3's discipline: the state and how the round ended, not a winner)

A round returns `DuelRoundOutcome` (PB §2: the two `DuelState`s after it, the lifted wounds, `felled`,
`yielded`, `closed`, the round's trace) **plus three fields this lane adds**: `ended_by` (one member of
`ROUND_ENDS`, below), `exchanges: int` (closed-measure exchanges in the round) and `attempts: Mapping[id, int]`
(attack attempts by each party). No `winner`: a round has none. What it does to a unit, a skirmish or a duel is the
caller's rule. `ROUND_ENDS = ('clean_defence', 'burst_ceiling', 'collapse', 'disengage', 'reopen', 'terms',
'felled', 'beat_exhaustion')` — the trace's existing separation strings kept (renaming them moves the
workbench's narrator for no reader's gain) and two added; owner `modules/combat/vocabulary.py`, the token alphabet
(`wrapper.py:9`).

### 2.6 Time: no clock; what the band feeds, and what it does not

**Decided: a round's duration is not a stored number, not a draw and not a rule** (A-101's amendment). Nothing
counts seconds. What the indicative band governs is the exchange cap (§2.2). Each place a duration could be
thought to enter:

| reader | decided | basis |
|---|---|---|
| **fatigue** | stamina is spent per attack act (`act_cost`, `wrapper.py:286`; `combat_systems.py:168-174`: base, heft, commit depth, armour short of Strength) and by percussion taken (`:250-251`, `:416-417`); recovered per separation (`:614`). Fatigue is therefore already derived from the exchanges made and the round boundaries, never from seconds. No per-second cost is added. | ladder 4 (as built); A-101's amendment |
| **the season and scene clock** | a whole fight is one act inside one scene; rounds never advance the season's clock or a scene's budget. A played duel's rounds are paced by the player, not by time | ladder 3/5: the fight is one provider call (`fight.py:55`) |
| **a duel round inside a battle** (A-4, A-72: depth 1) | the field calls one round per window per pair of named persons in contact (PB §4 table); the round returns at once and the field's tick count does not advance for it. As an indication only, one round is about one to two field ticks (a field tick is about four seconds, `MB_LEXICON_part2.md:15`), and a bout of 18 ticks (about seventy seconds, `:13`) with two windows (`MB_LEXICON.md:146`) holds at most two duel rounds per pair, a few tens of seconds of duelling in a bout — the flurries punctuated by stand-offs the lexicon's bout row cites (MV T1–T2) | A-4, A-72; ladder 5 (no second clock) |
| **the mass-battle abstraction** (A-100) | consumes per-round results; part 2 §5 | A-100 |
| **a narrator or the player surface** | may *say* "a few seconds" for a round from `exchanges` and `attempts` (an estimate of about 1 to 2 seconds per attempt plus closing), never a stored figure | the band is an indicator |

---

## 3. The mapping to the engine

### 3.1 The structures

| A-101 | engine structure | change |
|---|---|---|
| fight | `wrapper.fight`'s loop over rounds; after PB step 1, `modules/combat/fight.py::fight` as the loop over the one-round entry | PB step 1 |
| round | one `wrapper.engagement(A, B, first, cfg, rng, prev_closed, terms)` call | the two in-round re-openings end it (item PCR-1) |
| closing | the open-measure block (`:221-262`) and the latch/re-presentation at entry (`:98-124`) | none |
| exchange | one closed-measure beat with an actor (`:264-470`) | none |
| exchange cap | `CFG['BURST_MAX'] = 4` (`config.py:112`) | none to the value; comment and word (PCR-2) |
| separation | `_emit('separation', reason)` and the `return None, closed` beside it | two new reasons; the reason returned, not only emitted (PCR-1) |
| between rounds | `wrapper.py:613-615` (recovery) and `:127`, `:140`, `:593` (resets and draws at the next round's start) | `:593`'s coin moves inside the round (PB step 1) |
| beat | one iteration of `while beats < BEAT_BUDGET` | none |

### 3.2 The smallest addition so that rounds are a boundary the loop can observe

The engine does have distance (`measure_gap`, `closed`, `er`, `:91-124`) and disengagement (`:186-219`), so no
distance state is added. Two things are missing: (a) the in-round re-openings do not end the round; (b) the
round's ending is emitted to a trace hook and not returned. The smallest change at the single owner
(`modules/combat/wrapper.py::engagement`) is: at `:189-191` and `:208-210`, replace `continue` by
`_emit('separation', reason='reopen' | 'disengage'); return None, False`, and make every `return` of
`engagement` carry its reason as a third element, `(felled, ended_closed, ended_by)`, with `fight` (and PB's
round entry) reading it. That is the boundary: one function call per round, one returned reason, the state
between calls held by the caller.

### 3.3 The one-round entry, and the fight as the loop over it

PB step 1 is taken as written (`DuelState` with `form`, `DuelRoundInput`, `DuelRoundOutcome`, the coin moved
inside, the recovery applied at the round's end), with four amendments from this lane: (1) the entry is named
`fight_round`, not `round`, so `modules/combat/fight.py` does not shadow Python's builtin `round` (the engine's
own files call the builtin dozens of times, e.g. `wrapper.py:146`); the composition role stays `combat.round`
(target `modules.combat.fight:fight_round`); (2) `DuelRoundOutcome` gains `ended_by`, `exchanges`, `attempts`
(§2.5); (3) the between-round recovery is applied **after a separation only** (as `fight` does now: a felled or
yielded ending returns before it); (4) the loop's budget is `max_rounds` (12). The whole fight is then: for
`r` in 1..12, consult the deciders (PB §4), call `fight_round` with the round's key, stop on `felled`,
`yielded` or `withdraw`, else carry the states.

### 3.4 Names in code (tree names that fail the word test: rename candidates, not done here)

`engagement` stays as the function's name: renaming it to `round` would shadow the builtin in `wrapper.py`,
which calls `round(...)` at every emit; its docstring is corrected to "one round". The other names are listed
with their cost in part 2 §6 (item PCR-4).

### 3.5 The keyed draw per round (A-30)

Round `r` of a fight draws from `H(fight_key, 'round', r)` through `11_GO_one_draw_owner.md`'s `Draw.u`, each
draw inside the round keyed `(r, phase, purpose)` as PB §2 states. This lane adds one requirement: the purpose
must include the beat index (a round has up to 24 beats and a draw site may fire on several), so the in-round key
is `(r, beat, site)` with `site` the draw's fixed name (`coin_first`, `ready_A`, `stophit`, `commit`, `read`,
`roll`, …). Because PCR-1 ends some rounds earlier, the number of rounds a fight takes changes; with per-round keys
no round's draws depend on how many rounds came before (A-30), which is exactly PB step 2's gate.
