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
