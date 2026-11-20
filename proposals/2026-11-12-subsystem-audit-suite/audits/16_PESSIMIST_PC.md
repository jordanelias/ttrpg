# PC — pessimist audit (NERS, premise, emergent narrative) of personal combat

## Status: REFERENCE (an audit; resolves nothing at runtime)

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-22) — the lasting mark (`effects_combat.py:394-424`) opened: it is a certainty at the gate, shipped live. One `[UNVERIFIED]` mark settled; the row's finding is confirmed.

## Read at: 2eba83c (working tree)

Scope: `modules/combat/`, `systems/combat/`, `engine/season/seam/wrappers/combat.py`,
`engine/season/loop/effects_combat.py`, the grid seam, the verbs personal combat serves, Jordan's intent of
2026-11-12 (weapon, armour and skills as levers; an approach per phase; one path for the duel and the
automatic duel round), and the premise sentences of a fight. Prior work is cited, not redone:
`03_PC_audit.md` (F-PC-01..14), `03_PC_audit_addendum_B.md` (F-PC-15..23), the `03_PC_*` proposals,
`18_DETERMINISM_SWEEP.md` (C-12, C-13, D-04, D-11), `16_PESSIMIST_GAME.md` (the seam matrix, X2).
Everything measured below is new unless a lane is named. All runs `PYTHONHASHSEED=0`; the module is
driven through `wrapper.fight` with the trace seam (the registered entry `fight.py::fight` cannot carry a
`cfg`, a skill or a disposition, F-PC-07, so the cut tests cannot be run through it), and the season
readings through the real driver on `harness/probes.py::tiny_world`. "Tracker-true" means read off each
party's `WoundTracker`, which is what the season fold reads; `fight`'s integer (with its `UPSET_FLOOR`
flip) is never used. Scripts and outputs: the scratchpad directory named in §7.

## 0. Verdict

**Personal combat, as the season can run it, is a two-blow lottery between identical men that the world
remembers as one line; the engine around that lottery is mostly not running, and the per-phase choice the
intent asks for has, measured, almost nothing to decide.** The pessimist reading is in four parts.

1. **The fight is short and one-shaped (§3.2).** In the only fight a season person can have (arming
   sword, light armour, faculty 2 on both sides, F-PC-02), 5,000 fights to the death: the loser takes a
   single blow worth at least half his Health in 99.7%; 70.0% of deaths take exactly two blows on the
   loser and 27.4% three; four wound sequences (`AA`, `BB`, `ABA`, `BAB`) are 52% of all fights; 41% of
   turns draw no blood. Under `blood` terms (every `accept`) 92.6% of duels are one blow, and the man hit
   first yields in 94.8%. The cause is arithmetic, not chance: the exchange roll is centred 2.2 above its
   obstacle for any two equal fighters, so **Overwhelming is the modal band at every faculty from 1 to
   12** and within half a point of it at 0 (§1.1), and an Overwhelming blow is a median 25 of 40 Health.
2. **Most of the engine does not run in that fight (§1.3).** 100.0% of 17,021 engagements open closed:
   no approach phase, no stop-hit, no arrest, no fighting withdrawal, no pursuit, no re-presentation, in
   5,000 fights. Commit depth reaches the "deep" tier that gates the Indes steal, the single-time
   counter, the displace-and-step-inside and the lunge in 0.91% of exchanges. The grapple fires 5,812
   times and changes poise only: 1,107 "disarms" disarm nobody. A defender who reads the attack never
   chooses to wind. The cut tests (§1.2) say which of the remaining mechanisms move any outcome at all.
3. **The four premise sentences (§2).** *"A man strikes harder when he commits"*: weakly true (forced
   from the shallowest to the deepest commit, a blow lands 8 points more often and is 11% heavier),
   nobody chooses it, the depth at which it costs anything is drawn in 1% of exchanges, and inside the
   range the engine does draw, deeper is simply better. *"A wounded fighter yields"*: never under the
   terms a `fight` is fought on, always and at exactly one fraction of Health under the others, for
   every person alike: a threshold, not a decision. *"Armour turns a blade"*: false in its plain
   meaning: the share of Success rolls that draw no blood is 60 to 64% in plate and naked alike; armour
   multiplies every blow by a constant (a Success from an arming sword is exactly 15, 13, 8 and 1
   against the four tiers), and a swordsman cannot fell a man in plate (0 of 2,800). *"A skilled duelist
   beats a novice more often than not but not always"*: true of skill, and the best-shaped lever in the
   subsystem; no season person can be either, and two points of Perception outweigh four of skill.
4. **The world keeps almost nothing (§3.3).** A fight of 8 turns, 14 exchanges, 5 wounds and 2 grapples
   (110 trace events) reaches the log as `fight.declared`, `person.died`, `body.changed`. The victor, on
   12 of 40 Health with three wounds, is recorded as `undecided`. No blow, reversal, bind or bout count is
   anywhere a narrator can read. When the man attacked kills his attacker (half of all fights), no claim
   names the killer.

The steelman is owed and holds where tried: the draw is single-owned and reproducible, each party is
written by his own tracker, the skill lever is monotone with an honest tail, wounds impair, a weaker body
loses more often, and nothing in a fight is scripted. The largest obstacle found by this lane that the
earlier lanes did not state: **the engine's depth (reach, measure, tempo, commitment, the bind, the
grapple) and the engine's lethality are in conflict; the fight ends before the depth can matter, so
adding a per-phase approach on top (the stated intent) adds a choice with three decisions in it and, on
measurement, no situational content.** The fix order in §6 follows from that: length before levers.

## 1. NERS

Definitions `CLAUDE.md` §0.06; method `skills/ners/SKILL.md`; the draw read with
`skills/resolution-diagnostic`. The cut test is executed, not argued: remove the mechanism, re-run a
panel, name what moved.

### 1.1 The draw: where the exchange roll sits (resolution diagnostic)

`core.resolve` (`modules/combat/core.py:127-136`) rolls `pool = max(5, faculty + 6)` dice
(`resolution_pool`, `:54-58`) against `Ob = defender.faculty / 2` (`ob_from_defender`, `:102-124`), and
bands the margin on the owner ladder (Partial from margin 0, Success from +1, Overwhelming from +3).
Sampled from the engine's own `roll_net`, no σ, 40,000 draws per row (`pJ_roll.py`):

| faculty (mirror) | pool | Ob | mean margin | Fail | Partial | Success | Overwhelming |
|---|---|---|---|---|---|---|---|
| 0 | 6 | 0.0 | +2.41 | 10.9 | 12.8 | 38.3 | 38.0 |
| 2 (every season person) | 8 | 1.0 | +2.20 | 16.5 | 13.1 | 34.2 | **36.2** |
| 5 | 11 | 2.5 | +1.88 | 24.0 | 13.2 | 29.2 | **33.6** |
| 8 | 14 | 4.0 | +1.62 | 29.3 | 12.5 | 26.0 | **32.2** |
| 12 | 18 | 6.0 | +1.21 | 36.0 | 11.3 | 22.4 | **30.2** |

Reading. The attacker's six base dice are opposed by nothing: an equal defender's skill enters the
obstacle at 0.5 a point and the attacker's own enters his mean at 0.4 a point, so the expected margin of
an even exchange is `2.4 − 0.1·faculty`, a standing offset of about +2 that sits just under the
Overwhelming edge. **Overwhelming is the most likely single band, or within two points of it, for equal
fighters at every level.** Partial, the band that produces the bind and the graze (the engine's texture),
is the least likely at every level (11 to 13%). The ladder is the owner's and is consistent
(`degree_from_net`); the defect is the pool/obstacle pair fed to it. It is an S defect in §0.06's sense
("calculations consistent in methodology"): the same ladder is centred near its Partial/Success edge in a
social contest and near its Overwhelming edge here, so one word ("Overwhelming") names a rare event in
one module and the modal one in the other.

What the band then costs (`pC_armour.py`, 1,500 fights a cell): an arming sword's Success against light
armour is 13 (one value; Wound Interval 9, so 1.4 intervals, where `core.py:168` says "even Success ≈ 1
WI"), and its Overwhelming is 20 to 33, median 25: 62% of a default man's 40 Health. So about a third of
all exchanges are a blow that takes most of a man, and a fight is two of them.

Evidence that this, and not the defence layer, sets the fight's length: `pK_scale2.py` (§6, J-1) and the
cut tests (§1.2), where removing the read, the riposte or the whole tempo layer moves the count of blows
by less than a third of a blow.

### 1.2 Cut tests, executed

Thirty-one cuts, each made by the mechanism's own ablation value in `CFG` or by replacing one function
for the run (`pE_cuts2.py`, `pE3_default.py`; nothing tracked is touched). Two readings.

**(a) The fight the season runs** (arming, light, faculty 2, both sides), 2,000 fights per cut. The cuts
are symmetric, so the win share cannot move; what can move is the fight's shape. Uncut: 3.37 turns, 6.37
exchanges, 3.17 wounding blows, a lead change in 34.3%, the first man wounded wins 22.9%. Two control
runs at disjoint seeds: 3.30 and 3.37 turns; 6.22 and 6.31 exchanges; 3.14 and 3.19 blows; 32.6 and
35.2%; 21.4 and 23.5%.

| cut | turns | exchanges | blows | lead change | first wounded wins | reading |
|---|---|---|---|---|---|---|
| wound impairment (`WOUND_ATK_OB`, `WOUND_DEF_OB`) | 3.76 | 7.15 | 3.48 | **48.9%** | **31.5%** | **moves the shape** |
| riposte (`RIPOSTE_*`) | **4.07** | 6.57 | 3.23 | 36.8% | 24.8% | **moves the length** |
| armour-defeat σ | 3.65 | 6.77 | 3.23 | 34.2% | 23.0% | moves the length a little |
| the read (defender always guesses his mode) | 3.16 | 6.20 | 3.12 | 33.8% | 22.2% | at the band's edge |
| concentration drain; mental and Focus terms | 3.21; 3.21 | 6.09; 6.08 | 3.13; 3.13 | 35.8; 36.0% | 23.7; 23.5% | at the band's edge |
| Vor σ and tempo; Vor gains and steals (one cut by two routes: identical rows) | 3.40 | 6.43 | 3.22 | 36.5% | 24.4% | inside or a point outside |
| cadence anticipation (`tempo_pressure`) | 3.43 | 6.47 | 3.21 | 36.0% | 24.0% | inside or a point outside |
| poise (every break) | 3.44 | 6.45 | 3.20 | 35.0% | 23.3% | inside |
| percussion stagger; stamina costs; handling | 3.42; 3.38; 3.37 | 6.43; 6.36; 6.33 | 3.20; 3.19; 3.17 | 35.0; 34.1; 33.9% | 23.5; 23.1; 22.3% | inside |
| commit σ; over-commit exposure; recovery tempo of a commit | 3.42; 3.36; 3.37 | 6.41; 6.34; 6.35 | 3.18; 3.17; 3.17 | 34.2; 34.4; 34.0% | 22.3; 23.2; 22.7% | inside |
| lunge; the deep-commit tier gated off; single-time counter | 3.38; 3.38; 3.37 | 6.38; 6.37; 6.36 | 3.18; 3.17; 3.17 | 34.5; 34.5; 34.5% | 23.2; 23.3; 23.0% | inside |
| grapple (contact axis); bind cannot wound | 3.43; 3.41 | 6.43; 6.44 | 3.19; 3.11 | 34.8; 33.9% | 23.4; 22.1% | inside |
| guard terms; legibility; footwork; morphology levers (eight constants) | 3.40; 3.43; 3.47; 3.39 | 6.42; 6.42; 6.46; 6.37 | 3.18; 3.20; 3.19; 3.17 | 34.0; 34.1; 34.2; 34.4% | 22.5; 23.1; 22.8; 23.8% | inside |
| stop-hits; the whole approach phase; reopen and disengage; reach σ; half-sword switch; contact-moment terms | 3.37 | 6.37 | 3.17 | 34.3% | 22.9% | **identical to the uncut run in every figure: the mechanism contributes exactly nothing** |

In the one fight the season can have, two mechanisms beyond the roll and the damage change anything a
reader of outcomes could detect: wounds impairing the wounded (which makes the fight *less* reversible:
without it a lead changes hands in 49% of fights and the first man hurt wins 31%) and the riposte (which
shortens it). Six contribute exactly nothing: the approach phase, its stop-hits and the re-opening never
run (every engagement opens closed); the half-sword switch has no form to switch to; reach σ and the
contact-moment terms are differences that vanish between equal weapons. The rest are inside or at the
edge of a band of about a tenth of a turn and two points. Limits: 2,000 fights resolve about 0.1 turn and 3 points; every fighter here
has default attributes, so terms centred on the default (footwork on Coordination 4, handling on
Strength 4, Focus 3) are zero by construction and are "inert for every season person", not "inert".

**(b) Six matchups** (the mirror; faculty 3 against 2; longsword, and spear, against arming; rapier
against longsword unarmoured; mace against arming, both in plate), 400 fights a cell. The base and
control runs differ by up to 5.8 points on a win share at this size, so only large effects are visible.

| cut | largest change in any outcome share | what moved |
|---|---|---|
| stop-hits; the whole approach phase | **80.5; 77.0 points** | spear against arming: the spearman felled 0.2% → 80.2%; longsword against arming 20.0% → 34.0% |
| reach as a standing σ | 12.3 | longsword against arming 20.0% → 32.2% |
| riposte | 9.3 | plate: the fight resolves less (undecided 12.5% → 21.8%) |
| wound impairment | 8.8 | lead changes up 12 to 19 points in three cells; plate resolves less |
| armour-defeat σ | 6.2 | plate: lead changes 40.9% → 54.5% |
| the read | 7.0 | nothing beyond the interval |
| concentration; mental; contact-moment | 6.5; 6.0; 6.2 | nothing beyond the interval |
| stamina; grapple; guard; handling; percussion stagger; legibility | 4.0; 3.8; 3.8; 3.7; 3.5; 3.0 | nothing |
| lunge; morphology levers; poise | 2.3; 2.3; 2.0 | nothing |
| Vor σ and tempo; Vor gains and steals; cadence anticipation; bind cannot wound | 1.5; 1.5; 1.5; 1.5 | nothing |
| recovery tempo; footwork; over-commit exposure; counter; commit σ; the deep tier; reopen and disengage | 1.3; 1.0; 1.0; 0.8; 0.5; 0.5; 0.3 | nothing |
| half-sword switch | 0.0 | not exercised: no cell pairs a half-sword weapon with plate (the PC addendum's F-PC-16 measures it) |

The spear row is the engine's largest single effect and also a fixed outcome: a spear against an arming
sword in light armour fells him 99.2 to 99.8% (four runs) in 1.1 turns, all of it the stop-hit.

### 1.3 Coverage: what the season's one fight exercises

`pF_story.py`. Branch counts over 5,000 season-default fights (31,757 exchanges), against the same counts
over every base weapon against an arming sword (50 weapons × 120 fights, light armour).

| branch (trace event or source) | season default, 5,000 fights | roster v arming, 6,000 fights |
|---|---|---|
| engagements opening closed | **100.0%** of 17,021 | (approach beats: 22,030) |
| `approach` beats | **0** | 22,030 |
| `stophit` rolls | **0** | 6,974 |
| wounds by `stophit` | **0** | 6,654 (43% of all wounds) |
| `disengage` (fighting withdrawal) | **0** | 280 |
| wounds by `pursuit` | **0** | 101 |
| wounds by `displace_graze` | **0** | 2 |
| wounds by `bind` | 538 (3.4%) | 284 |
| wounds by `exchange` | 15,237 (96.6%) | 8,481 |
| exchanges at commit ≥ `DEEP_COMMIT` (4.0) | **0.91%** | 1.97% |
| separation `collapse` (stamina) | **0** | 3 |
| separation `beat_exhaustion` | **0** | 0 |
| `contact` (grapple) resolutions | 5,812 | 5,529 |
| defence mode chosen on a won read | parry 7,280, dodge 5,537, **wind 0** | — |

Reading, by mechanism:

- **The measure game is unreachable in a season.** Equal reach gives `measure_gap = 0`, the latch is
  certainly closed (`wrapper.py:107-110`), and every function of the approach phase
  (`stophit_sigma`, `true_time_edge`, `arrest_impulse`, `approach_step`, `close_rate`,
  `approach_displace`, `reach_threat`, `represent_measure_p`, `reopen_prob`, `disengage_attempt_p`,
  `disengage_clean_p`, `pursuit_sigma`) is never called with a non-trivial argument. Across the roster the
  stop-hit deals 43% of all wounds, so this is the half of the engine that makes weapons differ, and it
  waits on an inventory (`rosters.yaml: arms_kinds` is empty, F-PC-02).
- **The deep-commit tier is nearly unreachable everywhere.** `commit_depth` draws a Beta over a window
  whose upper end is contracted by swing room at closed measure (`combat_systems.py:1126`); at
  `DEEP_COMMIT = 4.0` sit the Indes steal, `counter_select`, the displace-and-step-inside, the
  over-commit reopen and (at `LUNGE_COMMIT`, also 4.0) the lunge (`wrapper.py:284`, `:325-329`, `:387`,
  `:401`). They are consulted in 0.91% of season exchanges and 1.97% across the roster. The cause is a
  collision, not a rarity (F-PES-PC-04): at closed measure, the only measure an exchange is fought at,
  the window is [2, 4.03], and the largest commit drawn in 300 mirror fights is 4.03 for each of ten
  weapons (`pF_story.py` F3). Disposition moves the share (disposition 1: 0.08%; 4: 0.92%; 7: 13.8%,
  F4) and nothing else does.
- **The grapple is frequent and cosmetic.** `contact.grab_outcome` resolves on more than one fight in
  one (5,812 in 5,000) and its six outcomes write poise and initiative only (`wrapper.py:460-468`):
  `disarm` 1,107 times and both men still hold their swords; `throw` 959 and `pin` 948 and nobody is on
  the ground. The names promise events the engine does not have (premise question 3, §2.5).
- **Winding is never chosen.** With two arming swords, a defender who wins the read picks the best of
  three mode σ and it is never `wind`; `wind` occurs only as one of three equiprobable guesses on a lost
  read (6,300 of 18,940). The bind therefore enters a season fight by a missed read and a Partial roll,
  never by intent.
- **Stamina never ends a burst** and `beat_exhaustion` never fires (addendum B's F-PC-22 found the same
  for the latter over 1,728 fights; here 11,000).

### 1.4 False N-lines

A false N-line is a statement of necessity that a cut shows to be free. Each is quoted from the code.

| # | the line | where | the cut | verdict |
|---|---|---|---|---|
| 1 | "The ongoing initiative system (initiative_sigma + hit-gains/steals/decay) is retained and load-bearing"; "Both are required by the NERS audit for this positive-feedback state" | `combat_systems.py:1078-1079`; `config.py:233-240` | the Vor cut by its outputs and, separately, by its inputs: identical rows; 1.5 points at most on six matchups; a point of lead-change in the mirror | **false at neutral disposition.** At least twelve constants and six functions, a per-beat decay and a clamp. Its one outcome-visible effect in the tree is the disposition drift, which the PC addendum's F-PC-17 shows to be an unpriced advantage. As coded the Vor is load-bearing only for the defect |
| 2 | "aggression risks overcommit (its deep commits raise existing exposure) … BOTH poles cost" | `config.py:280-285` | over-commit exposure zeroed; the deep tier gated off; the counter removed: nothing moves; forced depth is monotone-better | **false, because the tier is unreachable** (window [2, 4.03], threshold 4.0). The cut is free for the wrong reason; proposal B restores it and the line becomes true (52.0 / 47.6 / 51.5) |
| 3 | "the closed-phase lever for the reach-weapon-loses-the-bind residual: cycling approach↔bind, the long weapon wins on accumulated stop-hits" | `wrapper.py:193-201`, ED-PC-0030 | reopen and disengage removed: 0.3 points, 0.08 turns, spear and longsword cells included | **false on this panel**: the spear wins by the first approach and never needs to re-open. 280 withdrawals in 6,000 roster fights. Narrowed, not refuted: a reach weapon that loses the bind was not in the panel `[UNVERIFIED for that case]` |
| 4 | "ACTIVATED … each lever is now routed through … ability_factor … a school that specializes in a lever amplifies it into a SITUATIONALLY-DECISIVE edge" (eight morphology constants) | `config.py:42-68`, ED-PC-0022 | all eight zeroed: 2.3 points at most | **rests on a layer nothing can reach**: the note itself concedes the flat terms are below the noise floor and defers to tradition abilities, which no season record carries (F-PC-09) and which the addendum measured at 48.6 to 54.3 alone |
| 5 | "a bind IS a contact opening (Ringen am Schwert)"; the grapple's six branches | `wrapper.py:421`, `contact.py:60-77` | the grapple removed: 3.8 points at most, nothing in the mirror | **decorative**: 5,812 resolutions in 5,000 fights, each a poise or initiative nudge; the poise cut is itself free (2.0 points) |
| 6 | "a stagger is decisive" (poise deepened, ED-PC-0031) | `config.py:245` | every poise break zeroed: 2.0 points, plate-and-mace cell included | **not shown** at this size; if it is decisive it is so in a matchup this panel lacks |
| 7 | the defender's read "picks the BEST mode" | `combat_systems.py:1130-1150` | the defender always guesses: 7.0 points at most, inside the interval; a fifth of a turn shorter in the mirror | **nearly free between equals**: the read's weight is carried by Perception *differences* (§2.4), where it is a certainty, not by the choice of mode |
| 8 | the bind as a place wounds happen | `wrapper.py:431-443` | `BIND_HIT_P = 0`: 1.5 points | **free**: 3.4% of season wounds |

True N-lines, for symmetry (the cut costs something): the stop-hit and the approach phase (they are why
weapons differ at all); reach σ; wound impairment; the riposte; armour-defeat σ in plate; the roll; the
damage model. Seven mechanisms carry the outcomes; the engine holds some thirty.

Attack from the other side (mechanisms that survive because nothing was tried against them): the
`UPSET_FLOOR` flip survives as "the 95% cap" and changes nothing the season reads (F-PC-06; the sweep
replaces it); `YIELD_HEALTH_FRAC` survived as an `[ASSUMPTION]` because every instrument reported the
yield *share* and none asked whether anyone ever declined (§2.2); the twelve-turn cap survived because
the calibration matchups resolve inside it and the plate mirror with one sword was not among them.

### 1.5 E, last, as a ratio

Against what N and R found: about 6,000 lines, 214 `CFG` keys and 64 further constants (F-PC-15)
deliver, in the fight the season runs, a result reproducible to within the control band by the roll,
the damage arithmetic, wound impairment and the riposte. E is not "too much code" (the weapon-and-armour
half earns its size the moment an inventory exists: §2.3's estoc row, §1.2's spear row). E is low on the
*tempo, commitment and contact* half, where the player is promised that simple choices have complex
outcomes and the cut tests show the complex machinery has no outcomes. "Allows the player to intuit
complex outcomes from simple choices" fails on both ends today: there is no choice, and the outcome is
simple.

N from all six directions, on the object "the closed exchange's tempo-commitment-contact layer":
top-down (the intent needs an approach to lean on it): narrowed, it has no cost to lean against;
bottom-up (does a primitive need it): the roll and damage do not; vertical (does the season read it):
no, the fold reads trackers; diagonal (does another scale reuse it): nothing under `modules/mass_battle/`
names the combat engine (grep); lateral (do sibling modules have the analogue):
`modules/social_contest/roll.py` has no commit, tempo or initiative term (grep); horizontal (do the
verbs differ by it): `fight`, `accept` and `capture`
differ by terms only. It holds in one direction (the design documents' doctrine), which is a narrowed
N-line.

### 1.6 S: the two tests the shorthand drops

*Pauses correctly.* The grid suspension (REM-31) pauses at the turn head for a played party and nowhere
else; with three turns to a fight the pause occurs about three times, and 41% of those turns draw no
blood, so a played duel is three prompts of which one or two show nothing. The between-beats terms stop
reads standing state, which is right only while a yield is certain (proposal A changes it).

*Calculations consistent in methodology.* (i) One ladder centred at two different places (§1.1). (ii)
Armour is an average where every other chance in the exchange is a draw (§2.3). (iii) The yield is a
threshold where the engine's every other decision point is a roll (§2.2). (iv) "Deep" is an absolute on
a quantity whose range is relative (proposal B). (v) Two verbs for taking a man, one of words and one of
the body (§2.5).

## 2. Premise

Method `skills/premise-check/SKILL.md`. For each sentence: what the words mean to a player who knows the
genre (written before the code was opened), what the code's own notes say in aggregate, and what the
running code does. Verdict by execution.

### 2.1 "A man strikes harder when he commits"

| account | says |
|---|---|
| ordinary | Committing to a blow is a choice the fighter makes; it makes the blow heavier and likelier to land, and leaves him open if it fails. A cautious blow is safer and weaker. The choice should matter and should cut both ways. |
| the notes | "COMMIT DEPTH: the commitment-recovery spectrum" (`wrapper.py:280`); "aggression risks overcommit (its deep commits raise existing exposure), caution bleeds the Vor … BOTH poles cost" (`config.py:280-285`); `attack_sigma` = `COMMIT_SIGMA·(commit − 3)` (`combat_systems.py:1095`); the deep commit pays `overcommit_exposure`, an initiative loss, a poise break, a tempo debt and legibility. |
| the code, run | Commit is **drawn**, not chosen (`commit_depth`, one Beta draw per exchange); the only per-fighter input is `disp`, which no season record carries (F-PC-13). It does not enter damage at all: `core.strike(attacker, defender, deg, cfg, net, pool)` has no commit argument; depth reaches the blow only through the degree. |

Observational (`pA_commit.py`, 4,000 season-default fights, 25,456 exchanges, binned by drawn depth;
control: the same bins with depth labels shuffled across exchanges):

| drawn commit | n | Overwhelming | the blow wounds | damage when it wounds | riposted |
|---|---|---|---|---|---|
| [2, 3) | 12,402 | 32.9% | 47.6% | 19.8 | 14.2% |
| [3, 4) | 12,811 | 39.5% | 51.8% | 20.8 | 14.4% |
| [4, 5] | 243 | 46.1% | 51.4% | 22.3 | 18.1% |
| shuffled control, three bins | | 36.5 / 36.1 / 40.7 | 49.9 / 49.5 / 50.6 | 20.4 / 20.3 / 21.0 | 14.4 / 14.3 / 16.0 |

Interventional (A's depth forced on every one of his exchanges, the Beta draw still consumed so the
streams align; B draws normally; 4,000 fights; as drawn A is felled 50.5%, disjoint-seed control 48.8%):

| A's commit forced to | A felled | A's blow wounds | damage when it wounds | A riposted |
|---|---|---|---|---|
| 2.0 | **54.7%** | 44.8% | 19.4 | 15.8% |
| 3.0 | 49.2% | 50.5% | 20.3 | 15.0% |
| 3.5 | 48.0% | 51.1% | 20.6 | 15.0% |
| 4.0 | **54.1%** | 50.7% | 20.7 | 22.3% |
| 5.0 | **53.8%** | 53.2% | 21.6 | 23.8% |

**Verdict: the premise holds in direction and fails as a premise about a man.** Harder: +11% damage per
landed blow and +8 points on landing across the whole range, all of it through the degree. Open if it
fails: yes, above 4.0 only (riposted 15% → 23%). But (a) nobody commits; the engine draws it; (b) the
depth at which commitment costs anything is drawn in 1% of exchanges; (c) forced, both poles lose 4 to 7
points to the middle, so as a lever it has one right answer, "do not lean". Addendum B's F-PC-17 found
the opposite single right answer through disposition (the initiative drift makes aggression dominant);
together they bracket the design problem: one hook makes "aggressive" free, the other makes "normal"
free, and neither is a trade. §2.6 tests whether the *situation* can make it one.

### 2.2 "A wounded fighter yields"

| account | says |
|---|---|
| ordinary | A man who is hurt and losing may give up, and whether he does depends on him (his nerve, what he is fighting for, how badly he is hurt, whether the other man will let him). Some fight on to the death; some quit at a scratch. The other man may refuse the surrender. |
| the notes | "a duel doesn't have to be lethal" (Jordan 2026-10-14, `wrapper.py:504`); three terms; "the fighter who crossed them yields"; `YIELD_HEALTH_FRAC = 0.5` `[ASSUMPTION; medium]`; `Yield.accepted` "is the OPPONENT's choice (the engine has no decider for it, so the caller supplies it)". |
| the code, run | Under `death` (every `fight`): nobody yields, ever. Under `yield` (every `capture`) and `blood` (every `accept`): the fighter who crosses the line yields with certainty at the end of that turn, and the surrender is accepted with certainty (`wrapper.py:600-612`). |

`pB_yield.py`, 3,000 season-default fights per term:

| terms | yields | felled | undecided | who yields |
|---|---|---|---|---|
| `death` | 0 | 99.8% | 0.2% | — |
| `blood` | 100.0% | 0 | 0 | the first man wounded in 94.8%; the winner's median Health is 100%; mean 1.78 turns |
| `yield` | 94.4% | 5.6% | 0.1% | the first man wounded in 82.2%; the winner's median Health is 100%; 3.0% of yielders end on 5% Health or less |

The threshold has no spread: of 3,000 `yield`-term fights, fighters who crossed the line and did not
yield: 0; yields above the line: 0. The person does not move it: with Spirit 1 or 7, disposition 1 or 7,
Focus 1 or 7 (1,500 fights each), the highest Health fraction at which anyone yielded is 0.500 in every
arm; those attributes change how often a man reaches the line (Spirit 1: 46.5%, Spirit 7: 37.0%), never
what he does there. Sweeping the constant moves everyone together (0.25: 37.1% yield and 62.7% die; 0.9:
100% yield at the first touch).

The 5.6% who die under `yield` terms are the only graded tail, and they are an artefact of §1.1: a man on
more than half his Health takes one Overwhelming blow and is dead before the turn-end check can read him.

**Verdict: fails.** In the fight that kills (`fight`), a wounded fighter never yields; in the fights that
do not, yielding is a fixed function of one number, identical for every person, and never refused. This
is a breach of the standing rule (a thing that could go either way for the people in the fiction goes by
a draw) in both directions, and it is distinct from the sweep's D-04 (which makes the *death after a
felling* a draw): the *decision to stop* is still nobody's. The PC lane's
`03_PC_exits_withdrawal_recovery.md` leaves NPC concession as a Jordan item; under the standing rule it
is no longer one (§6, R-1; proposal `16_PESSIMIST_PC_A_the_yield_is_a_draw.md`).

### 2.3 "Armour turns a blade"

| account | says |
|---|---|
| ordinary | Some blows that would have wounded glance off or are stopped; the better the armour, the more of them. A blow that gets through still hurts. Armour is weight: it tires the wearer. Armour is what lets a man stand in a fight he would otherwise lose, not what makes him unkillable. |
| the notes | `RESIST` per material and mode; "a blow whose coupling-reduced impact does not clear the tier's resistance inflicts little lasting wound (it is stopped/deflected)" (`core.py:169-176`); the gap game for points; `ARMOR_DEMAND` charges a weak wearer stamina. |
| the code, run | Armour multiplies the damage of every blow by a fixed transmission and a soft knee (`core.damage`, `:609-645`). It shifts the roll (`armor_defeat_sigma`) only where the weapon falls short of the tier's threshold: for an arming sword, not at all below plate. Whether a landed blow is "turned" is decided by the defender's mode, not by what he wears. |

`pL_misc.py` L1, A (arming, light) attacking B (arming) in each tier, 800 fights a cell: mean net σ of
A's rolls −0.08, 0.00, −0.07 and **−0.69**; an exchange draws blood 45.3%, 47.8%, 44.7% and **25.4%**;
mean damage per exchange 10.2, 9.7, 5.4 and **0.6**. So cloth and mail change no odds at all for a
sword; plate changes both the odds and, far more, the divisor.

`pC_armour.py` C1: A (light armour, faculty 2) strikes B (arming sword, faculty 2) in each tier; 1,500
fights a cell; "dry" is the share of A's Success rolls that drew no blood.

| A's weapon | tier | a Success deals | distinct values | dry | an Overwhelming deals (min / median / max) |
|---|---|---|---|---|---|
| arming | none | 15 | 1 | 61.7% | 23 / 28 / 38 |
| arming | light | 13 | 1 | 61.4% | 20 / 25 / 33 |
| arming | medium | 8 | 1 | 61.9% | 12 / 15 / 21 |
| arming | heavy | **1** | 1 | 60.5% | 2 / 3 / 7 |
| longsword | none / light / medium / heavy | 17 / 15 / 10 / 7 | 1 each | 63.0 / 63.3 / 60.9 / 62.2% | medians 33 / 29 / 20 / 17 |
| mace | none / light / medium / heavy | 12 / 11 / 8 / 5 | 1 each | 62.6 / 62.6 / 63.4 / 64.1% | medians 22 / 21 / 17 / 13 |

A Success has exactly one damage value per weapon and tier; the dry share is the defence mode's
neutralise coin (`NEUTRALIZE_PARRY` 0.55, `_DODGE` 0.62, `_WIND` 0.50, `wrapper.py:344-354`) and is the
same naked and in plate. So "turned" and "armoured" are unrelated in this engine: what turns a blade is a
coin the defender's mode owns, and armour is a divisor.

Armour as a lever, arming swords both, equal skill (`pC_armour.py` C2, 1,500 fights a cell; `pC3.py`,
400): the wearer of the better armour is felled

| A wears / B wears | A felled | B felled | undecided |
|---|---|---|---|
| none / none | 51.1% | 48.6% | 0.3% |
| none / light | 52.6% | 47.2% | 0.2% |
| none / medium | 74.8% | 24.6% | 0.6% |
| none / heavy | 97.1% | **0 of 1,500** | 2.9% |
| light / medium | 73.9% | 25.8% | 0.3% |
| light / heavy | 97.5% | **0 of 400** | 2.5% |
| light, faculty 6 / heavy, faculty 2 | 59.5% | 2.5% | 38.0% |
| light, faculty 10 / heavy, faculty 2 | 3.8% | 22.2% | 74.0% |
| light with estoc / heavy | 25.0% | 75.0% | 0 |
| light with mace / heavy | 78.8% | 20.8% | 0.5% |
| light with longsword / heavy | 53.0% | 46.8% | 0.2% |

The ladder has a dead step (light armour is worth 1.5 points, inside the interval), a strong step
(medium: three to one) and a certain step (heavy). Skill does not buy it back: a master at faculty 10
fells a plated novice one time in five and three fights in four end undecided. The weapon does: this is
where the engine is at its best, and it is a choice made before the fight, not in it.

**Verdict: fails on the meaning of the words, and its extreme is a fixed outcome.** The premise's
ordinary sense (armour makes some blows fail) is not modelled; its engine sense (armour makes all blows
smaller) drives an arming sword to 1 a blow against plate, at which a fight to the death between two
armoured swordsmen is 99.8% undecided, under `yield` terms 90.1% undecided and under `blood` terms 39.5%
undecided (`pB_yield.py`, 800 fights each); the same mirror resolves 54.5% at forty turns and 100% at
two hundred (`pH_extremes.py` H6), so the twelve-turn cap is what decides it. The engine's own answer is
correct history (the half-sword, the mace, the estoc: plate mirrors with those resolve 96.5 to 100%), so
the model is sound *for a world with an inventory*. With today's single sword it means the first person
who owns plate cannot be killed and cannot kill another such, which the sweep's riposte proposal
(`18_DETERMINISM_no_certain_matchup.md`) does not reach: in the mirror nobody is felled, so there is no
deciding blow to turn, and in the mismatch a turned blow against plate is still divided by plate.

The cause is one line. `core._transmit` (`core.py:321-322`) computes `t·(1−g) + 1.0·g` under the comment
"some blows reach a bare zone": the chance part of armour, averaged away. Drawn instead (15% of blows
reach a bare zone and bite as against no armour; the rest meet the harness), prototyped in-process
(`pQ2_gap.py`, 400 fights a cell): light against heavy, the plated man felled 0.0 → 5.0%; the plate
mirror undecided 99.8 → 68.5%, and under `yield` terms 90.8 → 43.0% with 53.5% yields; the master
against the plated novice 2.5 → 33.2%; the light mirror and the estoc unchanged. A first idea, the knee
as a draw, was tested and fails (0.0 → 0.2%, `pQ_knee.py`). Proposal
`16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw.md`.

### 2.4 "A skilled duelist beats a novice more often than not but not always"

| account | says |
|---|---|
| ordinary | Skill is the main thing. The better swordsman usually wins, the gap matters, and an upset stays possible until the gap is large. Two masters fight a different fight from two novices. |
| the notes | pool `max(5, faculty + 6)`; Ob from the defender's faculty; "no matchup is ever certain" (`UPSET_FLOOR`, a flip the season never sees, F-PC-06). |
| the code, run | below |

`pD_skill.py`, A's faculty against B at 2 (every season person), arming and light, 3,000 fights a row,
tracker-true; mirror control at two seed sets 50.4% and 49.0%:

| A's faculty | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|
| A felled | 79.0% | 65.9% | 50.4% | 34.8% | 23.3% | 12.7% | 7.1% | 1.4% | 0.2% (6) | 0 of 3,000 |

**Verdict: holds, and is the best-shaped lever in the subsystem.** About fifteen points a step near
parity, an honest tail (one upset in fourteen at four points' gap, one in seventy at six), near
certainty from eight. Three qualifications, each measured.

- *Two masters fight the novices' fight.* Mirrors at faculty 0, 2, 5, 8, 12 and 20 (1,500 fights each)
  take 3.26, 3.18, 3.10, 3.08, 3.05 and 2.92 wounding blows and 3.2 to 5.0 turns: the same two or three
  blows with more misses between. The level changes nothing a watcher would name.
- *Skill is not the strongest lever; Perception is.* One attribute against a default man
  (`pN_att.py`, 1,000 fights a cell; default Perception is 3): Perception 4 is felled 22.7% and fells
  77.0%; 5 reads 5.6 / 94.2; 6 reads 1.1 / 98.9; 7 reads 0.5 / 99.5. A fighter at faculty 6 against a
  novice with Perception 5 is at parity (51.2 / 47.5); at faculty 4 he is felled 78.5%. So two points of
  Perception are worth four of skill, and three are a certainty. At Perception 7 against 3 the defender
  wins the read 2.2% of the time, the attacker's mean net σ is +1.27 and 74.5% of his rolls are
  Overwhelming. Strength runs 96.6% felled at 1 to 19.4% at 7. The season carries authored attributes
  into the fight (PC-06 K-1), so the first cast member written with Perception 5 is unbeatable by any
  swordsman the game can train. Which term carries the slope was not isolated `[UNVERIFIED: the read's
  logistic at scale 1.0 (`combat_systems.py:1145`), `mode_sigma`'s read term, `init_emphasis_sigma` and
  `tempo_pressure` all read the bare Perception difference]`.
- *The six skill axes are steeper still and uncapped* (module scale; the record cannot carry them,
  F-PC-21): +1 on all six, felled 18.1%; +2, 5.5%; +4, 1.7%.

So the premise is true of `faculty` and false of the build: the levers Jordan's intent names (weapon,
armour, skills) sit beside one that outweighs them, and nothing bounds a lever's slope.

### 2.5 Premises the code makes that nobody asked for

- **"The man who attacks has the first move": false.** `fight` is the actor's act; the engine flips a
  coin for who acts first in every turn (`wrapper.py:593`) and gives the opener nothing. Through the
  seam, 300 seeds: the actor is felled 148, the subject 152 (`pS_season.py` S2; the PC audit's E3 read
  104 and 96 of 200). The estimate the engine offers a chooser says the same: `actor_felled` 0.485
  (S5). So an assault, an ambush and a murder are each a fair duel announced in advance, and a rational
  person never opens one. A man on `body` 400 who attacks dies 70% (S6); nothing in
  `decision/options.py` reads the actor's `body` when the Candidate forms (grep; `[UNVERIFIED]` for
  `choose.py`'s weighting, which addendum B's C-9 found never prices a fight by believed odds).
- **"Disarm", "throw", "pin"**: outcome names of `contact.grab_outcome`; each is a poise or initiative
  nudge (§1.3). A reader of a trace is told a man was disarmed and then watches him parry.
- **"The watch takes a man"**: `capture` is the same coin under `yield` terms: of 300, the subject
  yields 133, **the captor yields 148**, and 19 die (S2). An office confers no edge in the taking.
  `arrest`, the other verb for the same act, contests `a standing` through the social roll
  (`verb_table.yaml:186-187`, `[ASSUMPTION; medium]`): two resolutions for one deed, one of words and
  one of the body, neither handing off to the other.
- **"Undecided"** is the word the fold writes for the victor: `Event.ending` for a fight he won on 12 of
  40 Health reads `(('p_low', 'undecided'), ('p_mid', 'felled'))` (S1). The closed set has no word for
  winning.
- **"First blood"** means the first *wound gate*, which the first landed blow crosses in nearly every
  case (a Success is 13 against an interval of 9), so `blood` terms are "first hit".

### 2.6 Does an approach per phase have anything to decide?

The intent asks that a fighter choose an approach each phase. The PC addendum measured static leans (a
small, weapon-conditional trade once the initiative drift is excluded). The question left is whether
*when* to lean matters: whether the fight's state gives the choice any content. Two runs.

**Inside the window the engine actually draws** (`pP_window.py`; A's depth forced each exchange, B
draws; season-default mirror, 1,500 fights; as drawn 49.9% felled, control 52.1%): 3.9 → **45.3%**; 3.0
→ 49.0%; 2.3 → **54.4%**. Deeper is simply better. The reason is F-PES-PC-04: the commit window at
closed measure is [2, 4.03] and everything that punishes depth is gated at 4.0. With the tier restored
to the window's upper third (prototype, same run): 52.0 / 47.6 / 51.5: flat, both poles paying.

**Policies that read the state** (`pI_approach2.py`; A leans by a rule, B always normal; depths 4.5 /
3.5 / 2.3, so "aggressive" here is over the 4.0 cliff; 1,500 fights; normal against normal 49.1%,
control 50.6%; three standard errors of a difference 5.5 points):

| A's policy | A felled | against always-normal |
|---|---|---|
| always aggressive | 54.5% | −5.3 |
| always defensive | 55.0% | −5.9 |
| press the wounded (aggressive when the other is more hurt) | 52.2% | −3.1 |
| guard when hurt (defensive when more hurt) | 50.7% | −1.6 |
| press when ahead, guard when behind | 53.9% | −4.8 |
| guard when ahead, gamble when behind | 50.3% | −1.2 |
| press the off-balance (aggressive when the other's poise is under 0.9) | 51.9% | −2.8 |

No rule that reads wounds or poise beats never leaning; every one reads at or below it. Three rules
that read initiative and stamina were not completed (the run was cut for machine load) `[UNVERIFIED]`.

**Reading.** As built, the choice is degenerate twice over: under the cliff, lean in always; over it,
never. There is no state in which a different approach is right, because a fight is three blows (§3.2):
by the time "he is hurt" is true, the next blow ends it either way. The approach gains content only if
(a) the deep tier is reachable (proposal `16_PESSIMIST_PC_B_the_commit_window.md`) and (b) a fight lasts
long enough for a position to exist (§6 J-1). Until both, building the choice surface builds a menu.

## 3. Emergent narrative

### 3.1 What stories the code can produce (enumerated from the code)

Endings of a scene (`wrapper.fight`): one party felled (`:597-599`); a yield at the turn's end under
non-lethal terms (`:600-612`); an exact-tie under those terms, nobody yields (`:606-608`); twelve turns
without a felling, undecided (`:576`, `:616`); a played person's withdrawal (`:590-592`); a declared
`Yield` (`:577-585`, reachable only from the workbench: the entry cannot pass `yield_decl`, F-PC-07).
Inside a scene: a blow, a graze, a neutralised blow, a riposte, a bind with up to three iterations, a
grapple outcome, and off the season default a stop-hit, an arrest of the charge, a fighting withdrawal
and its pursuit, a half-sword change. After a scene (`effects_combat.py`): death and the seats it
empties; a body fraction; a lasting ceiling mark; a `detain` edge under `capture`; one point of `arms`
where the key is held.

### 3.2 What it produces (counts)

`pF_story.py` F1, 5,000 season-default fights to the death, seeds 0 to 4,999:

| reading | value |
|---|---|
| endings | felled 99.82%, undecided 0.18%, both felled 0 |
| turns, exchanges, wounding blows per fight | 3.4, 6.4, 3.2 |
| turns that draw no blood | 41.1% |
| blows the loser takes | two 70.0%, three 27.4%, four 2.5%, five or more 0.1% |
| the loser took one blow of at least half his Health | 99.7% |
| distinct wound sequences (who struck whom, in order) | 105; entropy 4.35 bits |
| the four commonest | `AA` 14.6%, `BB` 14.0%, `ABA` 11.8%, `BAB` 11.6% (52.0% together) |
| a lead change (the PC audit's E5) | about one fight in three |
| the man wounded first wins | 20 to 25% (two seed sets, §1.2's base and control) |

Under `blood`: 11 distinct sequences, 1.48 bits; `A` 47.6%, `B` 45.0%. Under `yield`: 38 sequences,
2.91 bits; `A` 32.3%, `B` 30.8%.

So the inner story of a fight has a beginning and an end and, two times in three, no middle: no
escalation (the second blow is the last), a reversal one time in four or five, a cost for the victor in
about half (the winner's median Health under non-lethal terms is 100%). In computed play the count of
such stories is what the earlier lanes measured and is not redone: zero fought scenes in the realm and
spine at seed 0 over two seasons, two `capture` scenes at seed 1, eight `fight` scenes in 143 case
worlds, all `Felled` (F-PC-01); and in `16_PESSIMIST_GAME.md` §1.2 the PC column of the seam matrix is
empty: no executed act of any other engine has a fight among its causes except through a `capture`.

### 3.3 Retelling: what a narrator can read afterwards

`pS_season.py` S1, one `fight` at world seed 1003 through RESOLVE, ENCOUNTER and WITNESS.

- The scene: 8 turns, 14 exchanges, 5 wounds, 2 grapples; 110 trace events; the loser dead, the winner
  on 12 of 40 Health with three wounds (his maximum).
- The log: `fight.declared` (Declared), `person.died` (Felled), `body.changed` (Felled), each carrying
  `ending = (('p_low', 'undecided'), ('p_mid', 'felled'))`. None of "bout", "turn", "exchange",
  "riposte", "bind", "parry" or "overwhelming" occurs anywhere in those Events. The trace is returned by
  the seam (`combat.py:422`) and dropped (F-PC-03).
- The ledgers: the bystander holds `(p_mid, person.died)`, `(p_low, person.died)` and
  `(p_low, body.changed)`. The second is the doer's anchor (`person_q.py:259-262`), so a claim "X,
  person.died, True" means "X died" or "X killed" and only the `seen.who` pairing separates them. Over
  100 fights, 106 of 306 `person.died` claims name a living person. Where the *attacker* dies (half of
  all fights, §2.5), the only death claim names him and no claim names the man who killed him; the
  module's note records this as a stated limit (`person_q.py:266-268`). Its frequency is not marginal:
  it is every killing in self-defence.

What a narrator can say of any fight is therefore one of three sentences: "A attacked B and B died", "A
attacked B and died", "A attacked B; A was hurt". Who struck first, whether it was close, whether a man
came back from the edge, how long it lasted and whether the dead man was killed by the man he attacked
are all computed and all discarded. The module emits a story and the host keeps a verdict.

### 3.4 What a player's choice changes

Today: `engage` or `withdraw` each turn, and withdrawing is free (F-PC-05). With the stated intent built
as designed (an approach per phase): §2.6.

### 3.5 The shape of the tail

All runs are close to one run. Two fighters who cannot differ (F-PC-02), one weapon, one armour, no
measure game, a fight of 3.2 blows: the variance is in who lands the first Overwhelming, and the stories
differ by a seed and by nothing a person is. The tail that exists is the 0.18% undecided (twelve turns
without a felling) and the 5.6% who die under `yield` terms.

### 3.6 Extremes

`pH_extremes.py`, 1,000 fights a row unless said.

| extreme | reading |
|---|---|
| Endurance 1 mirror (a man at the bottom body band; Health 13) | the loser dies to his first blow in 97.2%; 1.83 turns |
| Endurance 2, 3 mirror | first-blow deaths 58.0%, 28.4% |
| Endurance 7, 10 mirror (Health 55, 70) | 4.4 and 5.4 blows; undecided 0.8%, 1.9% |
| Endurance 1 against 4 | the weak man felled 80.9% (through the seam with `body` 1: 249 of 300, `pS_season.py` S6) |
| every attribute 1, mirror (Health 10) | first-blow deaths 74.5%; undecided 1.2% |
| every attribute 7 against a default man | felled 0.0%; 1.76 turns |
| Strength 20 against default | 1 of 1,000 felled |
| Perception 0, mirror | runs; indistinguishable from the default mirror |
| unarmoured dagger mirror | 4.1 blows, 4.4 turns |
| plate, arming mirror | 99.7% undecided (§2.3) |
| a half-sword *form* as the starting kit (the export lists four as weapons, F-PC-15) | accepted; `estoc_halfsword` against arming fells 99.0% |
| unknown weapon or armour key | `KeyError` at the Combatant (the seam's `kit_of` is the guard) |
| faculty −3 | runs; pool 5, and he is attacked against an obstacle of −1.5 |
| faculty 2.5, 3.5, 4.5 | pools 8, 10, 10 (`int(round(·))` is banker's rounding); the season passes integers, the workbench need not |
| one id as both claimants, through the seam | `RESOLVED`, a winner named, a `wound_state` of one key (`pS_season.py` S3); the fold declines the act (`fight.declared` only, `pS2.py` S8), so nothing is written. `fight_estimate` refuses the pair (`combat.py:257`); `resolve` does not |

The story survives its extremes badly at the low end (a wounded or weak man's fight is one blow, so
the season's own carry of wounds through `party_end` makes the second fight of a hurt man a formality)
and not at all at the armoured end.

### 3.7 Stories that cannot happen, and why

| story | why not |
|---|---|
| two men kill each other | a felling returns at once (`wrapper.py:418-419`); both felled 0 of 5,000 |
| a man is disarmed, thrown or pinned and the fight changes | the grapple writes poise and initiative only (§1.3) |
| an ambush, an assassination, a man cut down unready | the opener has no edge (§2.5); no surprise input exists |
| a man fights on past sense, or quits at a scratch | yield is a threshold common to all (§2.2) |
| a surrender refused; a prisoner killed | terms-yields are always accepted; `Yield.accepted` is unreachable from the entry |
| an NPC breaks and runs | only a played person has a decider (F-PC-14) |
| a third man joins, or parts them | two claimants; no interrupt between turns for anyone but a played party |
| a named wound (the hand, the eye, the leg) | no hit location (ED-PC-0055 closed the coverage level); a wound is a body fraction and a ceiling |
| a fight that goes long and is remembered for it | the log keeps no length (§3.3) |
| the famous swordsman | no reputation is written by a fight (F-PC-03: 0 stance rows); no winner is named (`undecided`) |
| vengeance for the dead | `person.died` is answered by no other person's executed act (`16_PESSIMIST_GAME.md` §1.2) |
| a missile, a shield, a bare hand | no ranged resolution, no shield, no unarmed record (F-PC-12, F-PC-20) |

## 4. Findings

Ranked worst first. Each: severity · claim · falsifier run and its control · requirement · minimal fix
at the owner.

**F-PES-PC-01 · blocks the stated intent; degrades narrative (R-09, R-04) · A fight is two blows.** The
exchange roll is centred 2.2 above its obstacle for equals at every level, Overwhelming is the modal
band, and one Overwhelming blow is 62% of a man (§1.1). Falsifier: a blows-to-fell distribution with
real mass beyond three; outcome 2.6% (5,000 fights), and the same shape at two disjoint seed sets and at
faculty 0 to 20 (3.26 to 2.92 blows). Control for the cause: with the damage scale lowered the count
rises (4.6 blows at `DMG_SCALE` 1.07, 6.5 at 0.75) while re-centring the obstacle leaves it at 3.5
(§6 J-1), so it is the blow's size, not the roll's centre, that fixes the length. Consequence: no
escalation, a reversal one time in four, a duel to first blood that is one blow in 92.6%, and three
decisions for any per-phase chooser. Fix: J-1 (Jordan's; evidence in §6).

**F-PES-PC-02 · design (NERS N, E) · The per-phase approach has nothing to decide.** In the window the
engine draws, deeper is monotone better (45.3 / 49.0 / 54.4% felled at depths 3.9 / 3.0 / 2.3; as drawn
49.9, control 52.1); seven state-reading policies all read at or below "never lean" (§2.6). Falsifier:
any policy that beats always-normal by more than the interval; none of seven. Control: with the deep
tier restored the three depths read flat (52.0 / 47.6 / 51.5), so the monotonicity is the window, not
the instrument. Requirement: the 2026-11-12 intent. Fix: proposal B, then J-1, then the PC lane's
`03_PC_duel_round_and_approach_B.md` step 3; not before (R-6).

**F-PES-PC-03 · standing rule (R-09) · Whether a wounded man gives up is a threshold.** 0 of 3,000 across
the line who did not yield; 0 yields above it; identical for Spirit, disposition and Focus 1 to 7; never
under `death` terms; always accepted (§2.2). Control: sweeping the constant moves every person together.
Fix: proposal A (prototype: the yielder's Health at yield spreads from 0.12 to 0.68, 11.9% had fought on
past an earlier check, Spirit 1 against 7 takes 55.8% against 32.9% of the yields).

**F-PES-PC-04 · calibration, a pattern defect · The commit window is [2, 4.03] and the deep tier sits at
4.0.** The largest commit drawn is 4.03 for ten weapons; 0.91% of season exchanges reach the tier; the
lunge, the Indes steal, the counter, the displace and the over-commit reopen are gated there, and
cutting each is free (§1.2, §1.3). Falsifier: a commit above 4.14 in any closed exchange; none in
300 fights × 10 weapons. Control: at `range_avail` 1.0 the factor is 1.0 and the window is [2, 5] by the
function's own branch (`combat_systems.py:458-459`). The broken thing was right when written (§0.1 pt
5). Fix: proposal B.

**F-PES-PC-05 · degrades narrative (R-01, R-07) · The world keeps a verdict, not a fight.** 110 trace
events become three Events with no length, blow or reversal; the trace is returned and dropped (§3.3).
Falsifier: any of seven beat words in the fold's Events; 0 of 7. Fix: proposal C (after the typed
record).

**F-PES-PC-06 · degrades narrative (R-07, R-08) · A killing in self-defence has no killer.** Where the
actor is felled (148 of 300) no claim names the man who killed him; 106 of 306 `person.died` claims name
a living person, separable only by the `seen.who` pairing (§3.3). A stated limit
(`person_q.py:266-268`), measured here at one killing in two. Fix: proposal C part 2.

**F-PES-PC-07 · standing rule; completeness · Armour is an average, and its top step is a certainty.**
A Success has one damage value per tier; the plated man is felled 0 of 1,500 (unarmoured opponent) and 0
of 1,300 over three runs (light opponent); the plate mirror is 99.7 to 99.8% undecided; a master at
faculty 10 fells a plated novice 22.2% (§2.3). Control: the same mirror with a mace, an estoc or a
longsword resolves 96.5 to 100%, so it is the sword against plate, not plate. Latent today (one kit in
the world). Fix: proposal D (prototype: 0.0 → 5.0%; mirror undecided 99.8 → 68.5%; the master 2.5 →
33.2% at faculty 6).

**F-PES-PC-08 · robustness (customisation), latent · One attribute outweighs the levers the intent
names.** Perception 4 against 3 is 77 to 23; 5 against 3 is 94 to 6 and equals four points of skill;
Strength 1 is felled 96.6% (§2.4). Control: the mirror at two seed sets, 50.4 and 49.0%. Reaches the
season through authored attributes (PC-06 K-1); no cast member carries one today. Fix: R-7.

**F-PES-PC-09 · NERS N · Eight false or narrowed N-lines** (§1.4): the Vor substrate; "both poles cost";
the fighting withdrawal; the eight morphology levers; the grapple; the decisive stagger; the read's mode
choice; the bind as a wound source. In the season's fight, 2 of 31 cuts move the shape and 6 contribute
exactly nothing. Fix: none by itself; it is the evidence for the build order (R-6) and for what the Godot port
should not carry yet (R-8).

**F-PES-PC-10 · premise (the words) · Names that promise events the engine does not have.** `disarm`
(1,107 in 5,000 fights), `throw`, `pin`: poise only. `undecided` for the victor (the typed-outcome
proposal's `standing` fixes this one). `blood` terms stop at the first *wound gate*, which the first
landed blow nearly always crosses. Fix: R-8; cite `03_PC_typed_outcome_one_door.md`.

**F-PES-PC-11 · premise (genre) · The man who opens a fight has no edge, and neither does the watch.**
Actor felled 148 of 300; acting first on turn 1 is worth nothing (A felled 50.7% when first, 50.1% when
second, 6,000 fights); landing the first wounding blow is worth 77%. `capture`: the captor yields 148
of 300. Control: by construction (`wrapper.py:593`). Fix: J-2 (Jordan's).

**F-PES-PC-12 · standing rule, weapon level · A spear against a sword is 99.2 to 99.8%, in 1.1 turns.**
One mechanism (the stop-hit) and one constant chain; with it cut the spearman is felled 80.2%. Not the
sweep's C-13 case (armour) and not reached by the riposte in any useful measure `[UNVERIFIED: not
prototyped]`. The roster-wide count of such cells was not taken (machine load). Fix: R-9 (a census
before `arms_kinds` is populated).

**F-PES-PC-13 · hygiene · Extremes.** `seam/wrappers/combat.py::resolve` does not refuse one id as both
claimants (`fight_estimate` does, `:257`); `resolution_pool`'s `int(round(·))` gives pools 8, 10, 10 at
faculty 2.5, 3.5, 4.5; a negative faculty yields a negative obstacle; a half-sword form is accepted as a
kit (F-PC-15). None reaches a season today. Fix: R-10.

## 5. The standing rule, read against the subject

| fixed function of state in personal combat | where | status |
|---|---|---|
| a felling is a death | `effects_combat.py::_eff_kill` | the sweep's D-04 / `14_VERBS_PHYSICAL_A` A3 (the mortal-wound draw); not restated |
| the larger man always wins at the season's scale (the flip is not read) | `wrapper.py:618-624` | the sweep's C-13 (the riposte); does not reach the armour cases (F-PES-PC-07) or the spear (F-PES-PC-12) |
| a man across the term's line yields; the yield is accepted | `wrapper.py:600-612` | **new: proposal A** |
| armour divides every blow; plate against a sword cannot be felled | `core.py:321-322`, `:637-644` | **new: proposal D** |
| a Success deals one fixed number | `core.damage` | arithmetic once the blow lands; D adds the one chance it lacked |
| an NPC engages every turn, never withdraws | `wrapper.py:586-592`, `decide=None` | F-PC-14; the PC lane's proposal B §4-§5 (a chooser act, sampled, D-06) |
| the defender's mode on a won read is the best of three, always | `combat_systems.py:1149` | a fighter's judgment, not an outcome; left |
| the lasting mark falls at the deepest gate crossed | `effects_combat.py:394-424` | `[GROUNDED, 25 G-22: opened, and it is a certainty. `_marks`, `loop/effects_combat.py:394-424`: every survivor whose tracker reads `wounds >= max_wounds` (`:418`) has his `body_ceiling` lowered by `marked_ceiling` (`:421-423`); no draw. Shipped live, `body_mark_model="deepest_gate"`, `data/fixtures.py:723`]`; owed to the sweep |
| a yielded captive is detained | `_eff_capture` | `14_VERBS_PHYSICAL_A` A1/A2 |
| one point of `arms` per fight where the key is held | `effects_combat.py:271-296` | the sweep's C-15 |

This lane's own text was checked against the rule: proposal A's draw decides the yield and leaves the
victor's response a sampled choice; proposal D makes the gap a draw and leaves ranking an expectation;
proposals B and C decide no outcome.

## 6. Resolutions, proposals, and what is Jordan's

### 6.1 Decided (the five-step ladder)

| # | inconsistency, gap or unclear passage | decided | step | carried by |
|---|---|---|---|---|
| R-1 | the yield is a threshold; `YIELD_HEALTH_FRAC` is an `[ASSUMPTION]` awaiting Jordan | the yield is a draw on Spirit against the term and the wounds; the constant becomes the burst-breaker only | 1 (the standing rule) | proposal A |
| R-2 | `03_PC_exits_withdrawal_recovery.md` lists NPC concession as Jordan's | superseded: a concession is a draw, for every party, under every term | 1 | proposal A |
| R-3 | commit "over [2, 5]" in the notes, [2, 4.03] in the run; thresholds absolute | the tier follows the window; the notes state the window drawn | 5 | proposal B |
| R-4 | "some blows reach a bare zone" computed as an average | drawn per blow at `core.strike`; ranking keeps the average | 1 | proposal D |
| R-5 | the scene's shape is computed and dropped; the self-defence killer is unnamed | five Observations and `fell_to_hand`, on the `broke_observed` precedent | 4 | proposal C |
| R-6 | the PC lane's build order puts the approach (its step 3) before the fight has length or a reachable deep tier | the approach is built after proposal B lands and J-1 is ruled; its gate adds "a state-reading policy beats never-lean by more than the interval" | 5 (do not build a menu) | recorded here for the PC lane; its file is not edited |
| R-7 | no bound on a lever's slope; Perception outweighs skill two to one | the calibration rule gains a slope bound (one point of any attribute moves the mirror no more than one point of faculty does); first act is to isolate the term, then lift the read's literal scale (`combat_systems.py:1145`, `/1.0`) into `CFG` and fit it | 5 | an edit in the PC lane; no proposal file (the value needs the workbench sweep) |
| R-8 | grapple outcomes named for events that do not occur | the six stay as poise and initiative shifts; `contact.py`'s `GRAB_OUTCOMES` note says so; the names are not shown to a player and the axis is not ported until an outcome has an effect a fold or a grid reads | 5 | an edit; GO lane to note |
| R-9 | weapon mismatches can be certainties (spear against sword) | before `arms_kinds` is populated, a tracker-true census of the roster's matrix names every cell beyond 95%, and the inventory proposal (`03_PC_person_inputs_content.md`) admits a weapon only with its answer | 5 | recorded for the PC lane |
| R-10 | `resolve` lacks the same-id refusal; fractional and negative faculty | `resolve` takes `fight_estimate`'s `PARTY-GAP` line; `resolution_pool` is F-PC-08 (d)'s (fractional pools), not re-raised | 4 (`combat.py:257`) | an edit |
| R-11 | the twelve-turn cap makes the plate mirror undecided | kept (ruled: an undecided fight is a legitimate outcome); proposal D makes it rarer | 3 | none |

Eleven resolutions decided.

### 6.2 Proposals written by this lane

| file | what | cost |
|---|---|---|
| `proposals/16_PESSIMIST_PC_A_the_yield_is_a_draw.md` | the yield as a graded draw; prototyped | small build |
| `proposals/16_PESSIMIST_PC_B_the_commit_window.md` | the deep tier follows the window; prototyped | small build, calibration re-record |
| `proposals/16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight.md` | the scene's shape and the killer's name on the Event | edit, after the typed record |
| `proposals/16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw.md` | the coverage gap as a draw; prototyped (and a failed alternative recorded) | small build |

### 6.3 For Jordan (what survives the ladder)

**J-1. How long is a fight?** Not answered by a ruling, a design document or precedent; the two answers
are different games, and the 2026-11-12 intent presupposes one of them.

- *Option A, as coded: fast and lethal.* Two or three blows, the first solid one usually decides. Then
  the choice that matters is made before the fight (the kit, and whether to fight at all), the grid's
  single selection is the natural surface, and a per-phase approach in the duel is three prompts with
  nothing behind them (F-PES-PC-02). The honest build under A drops "per phase" for "per fight".
- *Option B: long enough to have a position.* Evidence, season-default mirror, 1,500 fights
  (`pK_scale2.py`; shipped: 3.36 turns, 3.18 blows, a lead change in 34.1%, first-wounded wins 23.3%,
  undecided 0.2%; control 3.30, 3.17, 31.8%, 21.9%):

  | change (in-process only) | turns | blows | lead change | first wounded wins | undecided |
  |---|---|---|---|---|---|
  | `DMG_SCALE` 1.55 → 1.07 (a Success becomes one Wound Interval, as `core.py:168` says it is) | 4.60 | 4.58 | 43.9% | 28.1% | 0.5% |
  | `DMG_SCALE` → 0.75 | 6.24 | 6.45 | 50.4% | 31.2% | 3.1% |
  | `OW_MAX` 2.5 → 1.5 (the Overwhelming ceiling alone) | 3.62 | 3.43 | 32.8% | 25.6% | 0.3% |
  | obstacle = 0.4 × the defender's pool − 1 (an even exchange centred on the Success floor; bands Fail 34.7, Partial 16.8, Success 30.0, Overwhelming 18.5) | 5.65 | 3.48 | 31.8% | 23.8% | 5.3% |

  The damage scale buys blows and reversals; re-centring the roll buys misses (more turns, the same
  blows, more undecided fights) and would re-open the ruled obstacle (Jordan, 2026-08-15). If B, the
  scale is the lever and the obstacle is left alone.

**J-2. Does opening a fight give an edge?** As coded, never: an assault is a fair duel. Option A keeps
that (violence is symmetric; ambush belongs to the field and to fieldwork). Option B gives the opener of
a fight the other did not expect an edge on the first turn. Evidence for B's form: who acts first is
worth nothing (50.7% against 50.1%), so "the opener goes first" would be a no-op; the edge would have to
be σ on the first exchange or an exchange the defender cannot answer, and whether the other "expected
it" is a host fact (`with`, a held challenge, a hidden intention) that no reader supplies today. A and B
differ as games by whether murder and ambush exist at personal scale.

Not escalated: the two verbs for taking a man (`arrest` by standing, `capture` by the body) are in
`14_VERBS_PHYSICAL_A`'s A1 and A2 and are left to that lane.

## 7. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_PC/`
(shared helpers `lib.py`; each script's output is the `.txt` of the same name). All
`PYTHONHASHSEED=0`; seeds are `0..N-1` unless a control offset is named. The machine was loaded (load
average 30 to 45 on 4 cores) for the whole run, so several probes were cut down or stopped; each is
marked.

| probe | what, size | outcome used in |
|---|---|---|
| `p0.py` | timing (2.6 ms a fight unloaded) and trace shape | — |
| `pA_commit.py` | commit depth, observational (4,000 fights × 3 matchups, shuffled-label control) and forced (default mirror complete; the longsword and mace arms stopped for load) | §2.1 |
| `pB_yield.py` | terms census 3,000 × 3; person sweeps 1,500 × 6; threshold sweep; plate under each term 800 | §2.2, §2.3 |
| `pC_armour.py` | per-blow damage by tier, 1,500 × 28 cells; tier matrix (stopped after the `light` row) | §2.3 |
| `pC3.py` | skill and weapon against plate, 400 × 7 | §2.3 |
| `pD_skill.py` | faculty 0 to 14 against 2, 3,000 a row; mirrors by level 1,500; skills and attributes 1,500 | §2.4 |
| `pN_att.py` | Perception, Strength and Coordination ladders 1,000 a cell (Coordination 1 to 7: felled 72.2% to 24.6%); Perception against skill; the read at Perception 7 | §2.4 |
| `pE_cuts.py` → `pE_cuts_base800.txt` | base and control rows of nine matchups at 800 (the cut loop stopped for load) | §1.2 (spear, base rates) |
| `pE_cuts2.py` | 31 cuts × 6 matchups × 400 | §1.2 (b), §1.4 |
| `pE3_default.py` | 31 cuts × the season mirror × 2,000, two controls | §1.2 (a), §1.4 |
| `pF_story.py` | story census 5,000 (death), 2,000 (blood), 2,000 (yield); roster coverage 50 weapons × 120 × 3 armours; commit depth by weapon and disposition | §1.3, §3.2 |
| `pH_extremes.py` | extremes, 1,000 a row; cap sweep 200 | §3.6, §2.3 |
| `pI_approach.py`, `pI_approach2.py` | state-reading approach policies, 1,500 (seven of ten policies; the 3×3 and the terms arms not run) | §2.6 |
| `pJ_roll.py` | the roll's centre, 40,000 draws a row | §1.1 |
| `pK_scale.py`, `pK_scale2.py` | damage scale, Overwhelming ceiling and one obstacle variant, 1,500 (the second obstacle variant, the skill curve under it and the terms arms not run) | §6 J-1 |
| `pL_misc.py` | armour and the roll 800 × 4; first-mover 6,000 | §2.3, §2.5 |
| `pM_yield_draw.py` | prototype of proposal A, 1,500 × 3 terms, two controls, Spirit and modifier sweeps 1,000 | proposal A |
| `pP_window.py` | prototype of proposal B, 1,500 mirror, 1,000 a matchup | proposal B, §2.6 |
| `pQ_knee.py` | the knee as a draw, 500 (stopped after two cells: it fails) | proposal D |
| `pQ2_gap.py` | prototype of proposal D, 400 × 8 cells | proposal D, §2.3 |
| `pS_season.py`, `pS2.py` | `tiny_world` through the real driver: one fight's Events and ledgers; 300 seeds per verb through the seam; self-fight; the estimate; `body`-lowered actor; death-claim census over 100 fights | §2.5, §3.3, §3.6 |

Not run: a realm-scale season (the game lane's X1 and X2 took 95 to 107 s a season arm on this machine;
their readings are cited); `pytest`; any `aperture` run. Not read: the workbench files and the
`.designs/` combat set (the PC addendum's §B1 read them; cited through it); `combat_systems.py` outside
`:436-470` and `:1044-1175`; `weapon_physics.py`; `weapons.py`.

`git diff --stat 2eba83c HEAD` over `modules/`, `engine/`, `systems/`, `tools/`, `references/` and
`architecture/` was empty at the last check (HEAD `7b532b2`), so every code reading holds at both.
