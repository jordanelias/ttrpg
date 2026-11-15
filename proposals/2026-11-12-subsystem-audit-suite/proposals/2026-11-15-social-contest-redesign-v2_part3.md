# SC — the social contest redesigned, v2, part 3: the scene and the world; verification by execution; the handshake

## Status: PROPOSED (the third part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## A. Thematic, immersive, worldly

**What a player sees.** Before the sitting, the card: this is a trial on a charge, the reeve arranged it and has
tilted it, a closed floor, one of his clients on the bench, two turns each, records and testimony admitted, what
each outcome will do to him, his odds as the room stands. At each exchange: the issue (*fact*), the point against
him and how far it seems to stand, his own point, the mood of the room, his own condition, and a menu: answer the
point (on what it will bring, on what is owed, as one of their own, or on the proof with the ledger he holds),
raise his own, go after the man, concede the fact and fight on the definition, or say nothing. Each line carries
its believed worth and chance, from his own reading. He chooses one. He then sees what it did: it landed or fell
flat, the room moved, the other man held or was shaken.

**What a rattled man looks like.** The room has moved against him at once. The venue now asks more composure of
him than before, so a graceless man's next speeches visibly fail where a graceful one's hold. He is pulled: his
next speech wanders unless his Focus holds. Press him again and the room gives less, then turns on the presser.
He is never forced to stop; if he concedes after it, the record says he broke.

**Why each kind feels like itself** (the structure says what it is about). A **trial** is points on a charge
that must be answered, proof shown and witnesses called and pressed, and a concession that changes what the fight
is about (he did it; was it a crime). A **negotiation** has no judge: each speech must answer the last offer, the
man who needs it more gives way sooner, and it ends when one of them accepts or the turns run out. A **rally** has
nobody to answer: every speech raises, the crowd is several bodies with different wants, and a speaker who has
landed two may do best to stop. A **questioning** is one man pressing his own judge: the questioned must answer
or be seen to evade, and what he gives up he gives up himself. A **debate** is speeches for and against a motion
before seats that each come down for themselves, with the floor in the room. An **inquisition** is a questioning
before a bench that may be the accuser's own. An **audience** is a plea and a ruling by a seat with its own stake.

**What the room remembers, and what the world does with it when nobody is playing.** Every sitting, played or
not, leaves these hooks (the host writes them; part 2 §J), and each is a thing another system or a later sitting
picks up:

| hook | written where | what picks it up |
|---|---|---|
| the beats and the end state | the Event's `ending`; the case file's stages for a docketed matter | a resumed sitting; a renderer; the next sitting's `precedent` and `confession` items |
| *he was rattled, and by whom* | a claim in each witness's ledger; strain carried by the man | his next sitting starts strained; the presser has made an enemy |
| *he argued against what he holds* | a `hypocrite` claim with those attuned enough to see it | regard; a later press aimed at him with it |
| *the judge had a stake* | a `partial` claim with everyone present | an appeal; the judge's own regard; a faction's legitimacy |
| *the forum was rigged* | a `rigged` claim; the arranger's faction's legitimacy down by how many saw | an appeal docketed; a grievance; a martyr |
| what was shown | a claim of each item with everyone present | the item is now known: it can be shown again by anyone who saw it |
| who stood against whom | regard from the man testified against toward the witness; from loser toward winner | grudges that are recognisably earned |
| what each wanted | pursuits moved by the outcome times his stake | his next choice of what to do |
| the disposal | a Tenure, a decree, an acquittal, an office contested, a precedent | the realm |
| the strife | eased by a carried matter that bears on it, inflamed by a failed one | what is convened next season |

A-80 (entrenchment must still move the world) is met in the same table: a proposition that fails leaves an
acquittal that is precedent, a grievance, an appeal, strife inflamed and a grudge; in the model's three seasons a
famine that a failed motion did not ease convenes the motion again.

---

## B. Verification by execution

Model: `sc_model_v2/` (`sc2/engine.py` 760 lines, `sc2/host.py` 500), `PYTHONHASHSEED=0`; outputs
`core_out_final.txt`, `world_out_final.txt`, `transcripts_out.txt` beside it. `n` is sittings an arm; "all-mid" is
the stress test's cast (every attribute 4, rank 1, flat interiors); "the cast" is fourteen characterful persons
(`sc2/fixtures.py`). "Before" is the stress test's reading of the old design at its shipped values. Two standard
errors of a share at n = 1000 are about 0.03.

### B.1 The defects

| | what was wrong | before | after (v2 model) | control arm | n, seed |
|---|---|---|---|---|---|
| D1 | a bench verdict ignores the sitting | a full trial carried 0.9 % at every track; excommunication 0 of 2000 | trial carried 0.074 / 0.224 / 0.371 / 0.556 by the presiding seat's track (≤ -3, -3..0, 0..3, ≥ 3); excommunication (declared, quorum 2) 0.206; R11's trial arm: the speaker's Reason slope +0.010 a point, z +2.9 | `track_step` 0: 0.258 / 0.310 / 0.279 / 0.275 (flat) | 1000, `d1` |
| D2 | the centre cannot be restored | the tell carried 0.53 to 0.70; 0.40 with fit off | the tell between equals: fail 0.565, half 0.153, carried 0.282 at B05's `routine` 0.5; fail 0.617, carried 0.247 at 0.8; full sittings between equals 0.28 to 0.39 | at controls the same 0.565 / 0.153 / 0.282, and the abridged margin equals the plain roll on 200 of 200 keys | 2000, `d2` |
| D3 | the rattle does nothing; pressing is dominated; the script helps the accused; `broken` unreachable | no rattle term in any ballot; questioner 0.26 scripted against 0.34 free; `broken` never | against a Will-2 Grace-2 respondent: one press then argue 0.541, argue only 0.428, press only 0.655; questioner 0.416 under the questioned rite against 0.339 where both may press; questioning that man ends yielded-while-rattled in 525 of 1000 | a rattle that does nothing: 0.485 / 0.428 / 0.456 | 1000, `d3c` |
| D4 | strain carried ratchets | 0 to 5.8-9 over 11 sittings | 0, 0.25, 0.38, 0.25, 0.38, ... never above 0.38 (bound 1.0), pressed at every exchange | the formula's bound | 11, `d4` |
| D5 | the opener speaks twice and has the last word | carried 0.433 against 0.257 on flipping the opener | speeches 1158 to 1153 over 300 trials; 0.356 against 0.313 (+0.043 ± 0.021) | nobody may answer: 0.341 against 0.335 (+0.006): what remains is the initiative of raising over answering | 2000, `d5` |
| D6 | the act's margin under consent is the actor's last exchange | 198 of 2000 graded Success with the track against the actor | 0 of 329 | by construction (the margin is the other party's) | 1000, `d6` |
| D7 | types are names | the room always `bench`; debate equals trial; 9 of 53 settings and three moves and two ends never occur | a crowd on the floor changes the band in 58 of 300 trials and 77 of 300 debates (0 in the closed inquisition); the eight rows differ in moves, relations, ends and length (table B.2); every move and every end occurs; 0 of 38 settings inert | the closed floor | 300; 400 a row |
| D8 | a dead `sense` passes the gate; sign error; lean outweighs the track; the track saturates | carried 0.27 hostile against 0.80 friendly at the same track; one speech filled the track in 45-52 % of openings | each decider attribute's slope is exactly 0 with its own setting off; at a track of 3 to 5 carried 0.545 hostile, 0.528 neutral, 0.525 friendly; P(carried) 0.28, 0.49, 0.66, 0.75, 0.79 at tracks 0, 3, 6, 9, 12; `for` conceding at every chance carries 0.122 against 0.318 | the settings off | 1000 to 2000 |
| D9 | integration with the plan | ten conflicts | the ordered edits of part 4 §H | **not run**: plan edits, applied by nobody here | |

Also re-read from what held: determinism (50 of 50 keyed sittings identical); the draw counts (2G+5 an exchange,
one a balloted decider, none under consent) asserted on every run; termination (every sitting ends by budget,
rest or yield); the module returns margins. **Not re-run:** the stress test's own `selfcheck.py` and lane probes
call the old model's API (`build_input`, `SideState`, `act_margin`) and cannot run against `sc2`; each quantity
they read was re-measured by the new checks named above, and the old probes still run unchanged against the
untouched copy of the old model in the same directory.

### B.2 The types in play (the cast, effort 3, automatic, 400 sittings a row)

| row | argue : press : concede : rest | raises : answers | ends budget : yielded : rested | beats | carried |
|---|---|---|---|---|---|
| conversation | 1319 : 863 : 99 : 0 | 1275 : 44 | 301 : 99 : 0 | 5.7 | 0.44 |
| negotiation | 1429 : 697 : 123 : 0 | 1174 : 255 | 277 : 123 : 0 | 5.6 | 0.37 |
| questioning | 2495 : 1 : 193 : 5 | 1692 : 803 | 207 : 193 : 0 | 6.7 | 0.54 |
| inquisition | 3137 : 4 : 17 : 38 | 1766 : 1371 | 393 : 7 : 0 | 8.0 | 0.64 |
| trial | 2372 : 787 : 41 : 0 | 1605 : 767 | 400 : 0 : 0 | 8.0 | 0.60 |
| debate | 1262 : 1373 : 159 : 23 | 1131 : 131 | 241 : 159 : 0 | 7.0 | 0.43 |
| rally | 1167 : 0 : 0 : 15 | 1167 : 0 | 385 : 0 : 15 | 3.0 | 0.46 |
| audience | 797 : 0 : 0 : 2 | 797 : 0 | 398 : 0 : 2 | 2.0 | 0.53 |

The trial and the inquisition are where points are answered; the debate is where the man is gone after; the
questioned concedes (talks) in half the sittings; the rally and the audience have nothing to answer.

### B.3 The roles (slope of carried per point of the attribute, z in brackets; n = 1000 a level)

| | Focus | Reason | Attunement | Presence | Grace | Will |
|---|---|---|---|---|---|---|
| the tell | 0 | +0.046 (13) | +0.008 (2) | +0.022 (6) | +0.032 (9) | 0 |
| conversation | 0 | +0.026 (7) | +0.004 (1) | +0.016 (4) | +0.026 (7) | +0.031 (8) |
| trial | +0.002 (1) | +0.016 (5) | 0 | +0.014 (4) | +0.020 (6) | +0.017 (5) |
| rally | 0 | +0.021 (6) | +0.003 (1) | +0.034 (9) | +0.024 (7) | 0 |

Each on its own operand: the hearer's Will at the tell -0.050 (z -15.6); a pressed man is rattled 0.508, 0.329,
0.188 at Will 1, 4, 7; the mean margin of a man's speeches after he has been rattled is -3.72, -2.22, -1.15 at
Grace 1, 4, 7; the speaker's Focus at a tell in a famine +0.008 (z +2.8). The decider's three: Reason +0.025 a
point (z +7.1) for a petitioner arguing on the proof and -0.013 (z -3.6) for a mannered speaker (it steers both
ways); Attunement -0.020 (z -9.2) against a man arguing against his own conviction; Focus -0.006 (z -1.8)
against a speaker who wanders. **Weak, and said so:** the speaker's Attunement (a poor reader carries 0.406 and a
good one 0.440 where the room is sharply peaked; the control with perfect reading for all reads 0.467 for both)
and Focus on both sides read small slopes; Focus, Attunement and the speaker's Will read zero at a quiet tell by
construction (part 2 §C.6; part 4 §I question 3).

### B.4 Played

| check | reading |
|---|---|
| options on the first menu | conversation 12 and 8 (for, against); negotiation 10, 8; questioning and inquisition 11 (argue, press, rest), 5 (argue, rest, concede); trial 12, 8; debate 10, 8; rally 4; audience 5 |
| decisions a sitting | the row's turns: 2 to 4 each in these runs |
| a view-only chooser against a random legal one (played seat averaged over five characters; n = 1500 a rite) | carried +0.088 conversation, +0.175 negotiation, +0.109 questioning, +0.099 inquisition, +0.199 trial, +0.142 debate, +0.045 rally, +0.071 audience (2 s.e. 0.036) |
| the same chooser against the automatic policy in the same seat | -0.027, +0.003, +0.005, +0.005, +0.025, +0.003, +0.015, +0.019: **no margin**. The automatic policy takes the best option the same view shows, plus the man's grain; a one-step chooser cannot beat it. **Not met**; part 4 §I question 1 |
| a poor reader loses only through the view | Attunement 1 against 7: 0.406 against 0.440; with `read_blur` 0: 0.467 against 0.467 |
| every option earns its place (the view-only chooser with and without it) | rest, a plain man before a cold crowd: 0.243 against 0.150; concede as descent, the accused against a strong accuser: 0.540 against 0.458; concede as acceptance, the party addressed: 0.335 against 0.263; answer, two able advocates before a bench that can be moved: 0.688 against 0.602 (in a negotiation 0.603 against 0.585: there the answer is carried by evasion being seen, not by a pay-off); press: the best reply to an arguing opponent in every matrix read, and worse than arguing against the automatic policy |
| leaks | the `View` holds no `Present`, no track, no `Beat.terms`; the believed fits of two grounds differ from the truth independently (s.d. of the believed difference 1.38; the old design's was exactly 0); a played `for` met an automatic `against` in every rite |
| a residual | between all-mid people in a `must` rite the best reply to the automatic policy is to say little (trial 0.357 resting against 0.327, debate 0.247 against 0.233; about one standard error): a plain man with nothing to argue from and less Grace than the court asks does not help himself by talking |

### B.5 Simulated (`for` in a trial against an ordinary respondent; 400 sittings each)

| the man | press | argue | concede | on the proof | from interest | from principle | as one of them | insincere a beat | carried |
|---|---|---|---|---|---|---|---|---|---|
| orator (Presence 7) | 0.18 | 0.77 | 0.03 | 0 | 0.23 | 0.48 | 0.23 | 0 | 0.39 |
| scholar (Reason 7, holds the ledger) | 0 | 0.98 | 0.01 | 0.83 | 0.02 | 0.14 | 0 | 0 | 0.43 |
| bully (Will 7, a grudge) | 0.79 | 0.20 | 0 | 0 | 0.16 | 0.31 | 0.51 | 0.01 | 0.27 |
| diplomat (Grace 7, Will 3) | 0.21 | 0.66 | 0.08 | 0 | 0.26 | 0.51 | 0.10 | 0 | 0.40 |
| fox (holds a forged writ) | 0.52 | 0.39 | 0.02 | 0.21 | 0.43 | 0.15 | 0.12 | 0.24 | 0.37 |
| a plain man | 0.30 | 0.49 | 0.12 | 0 | 0.23 | 0.41 | 0.15 | 0 | 0.34 |

Who prevails: before the bench the scholar carries 0.58 against the orator and the orator 0.29 against him; before
the crowd the orator carries 0.44, the scholar 0.29, the bully 0.21 (R11). **Three seasons** (the same people; a
famine convenes a motion to remit the tolls each season it stands above a level; a trial the reeve rigs in the
first season; the loser's appeal; a negotiation over grain), 80 runs: the recurring trial carried 0.44 in the
rigged season, then 0.61 and 0.62; the third season's trial carried 0.63 after a first-season win and 0.62 after
a loss (no snowball); the rigged trial came back as an appeal in 45 of 80 runs; the famine ended between 0.00
and 2.50 (mean 1.36; it began at 1.00); the greatest strain anyone carried was 0.91 (bound 1.0); in the run
printed the scholar's regard for the reeve went from 0 to -0.54 over the rigged trial and the presses.

### B.6 Bearing, context, roles, power, the fold (each with its flattened control)

| claim | shipped | control |
|---|---|---|
| two men stand differently on one matter | the orator's bearing on the toll matter (+0.8, +0.3, +0.6): for; the reeve's (-1.0, 0, -1.0): against | flattened: both neutral |
| a press on what he wants hits harder | rattled 0.162 where his pursuit is 0.1, 0.548 where it is 0.9 | 0.343 and 0.343 |
| arguing against his own conviction is a ploy and costs | carried 0.282 with no conviction, 0.105 with one (insincerity 1.0, strain after 1.0) | `ploy_step` and `grain_strain` 0: 0.282 and 0.282 |
| the verdict moves what each wanted | winning: the orator +0.67, the reeve -0.53; losing: the reverse | flattened: ±0.10 (the faction term only) |
| a decider with a tie is partial and is seen to be | a petition against the reeve before his client carries 0.318, before a neutral seat 0.413; the petitioner then holds a `partial` claim | 0.400 and 0.420; no claim |
| one record, credited by relation to it | the ledger about the reeve: +0.80 to the neutral judge, +0.30 to his client and to his friends | (a direct read of `credit`) |
| a man whose patron is implicated | the bishop's client credits the letter +0.10 and a press with it aims -0.20 at him; a stranger +0.60 and -1.00 | (a direct read) |
| a need changes a concession | the diplomat accepts the grain terms 0.537 with no need, 0.828 with a need of 0.9 | 0.563 and 0.563 |
| two regimes | the toll trial carries 0.603 under the crown, 0.528 in a theocracy (standard 6, confession admitted, precedent dropped, debate unlawful), 0.612 in a commune (standard 4, inquisition unlawful) | all three flattened: 0.603 |
| peace and strife | famine 0.530 (unrest 0.75, stakes 0.25); war 0.505 in 6 beats instead of 8 | 0.603 |
| two ages | an age of faith 0.585, a mercantile age 0.602: **within noise** on this matter; the era's weights move which ground is chosen more than who wins | 0.603 |
| an office-holder and a commoner in the accuser's place | the reeve: power 3.5, tilt 0.94, two turns, his client alone on the bench, no floor, carried 0.322; the clerk: power 0, tilt 0, four turns, the open room, 0.243 | |
| a partisan bench and a neutral one | 0.432 against 0.597 | flattened 0.383 against 0.457 (the seats' attributes still differ) |
| one reading, any role | the judge's `care` is identical as advocate and as judge; two identical men swapped between advocate and judge give the identical result (0.320 and 0.320); a Reason-7 man as judge only 0.278, as advocate only 0.313 | |
| a magnate in the gallery | hostile: the speaker's drift 0.358 a speech and 0.462 rattles a sitting; friendly 0.213 and 0.387; none 0.059 and 0.390 | |
| a witness called from the floor | the clerk speaks his own testimony in 402 beats of 400 trials, is the one pressed next in 195, and his role cells are unchanged after in 400 of 400 | |
| the powerful arrange and pay | the accuser carries 0.617 in a fair forum, 0.567 against a firm one (tilt 0.47, legitimacy -0.47 with the floor watching), 0.355 against a rigged one (tilt 0.94, bench packed, floor shut, two turns; legitimacy -0.16, and an appeal docketed) | two equals, a weak arranger, power flattened: 0.617 each |
| two outcomes leave two worlds | Success: a `detain` Tenure, a precedent, the famine at 0.75; Failure: an acquittal on the case file, a precedent, the famine at 1.25, 9 to 11 typed writes | not held: nothing written |

---

## C. Transcripts (rendered by a 40-line template over the `Beat` records; the renderer is a test fixture)

Seeds are the first that show the structure named (`transcripts.py::pick`, reproducible). The number after each
beat is the room's mood toward `for`.

**A trial** (judicial; a charge; both must answer; fact, definition, justification). Confirmatio, refutatio, a
witness, a descent on the stasis:

```
[trial, arranged by scholar; decided by judge; 4 turns each]
1. [fact] scholar raises point 0 on the proof, citing ledger_of_tolls: it lands. (+0.44)
2. [fact] diplomat answers scholar's point 0 (evidence) from what is owed: it falls flat; he wanders from the point. (+1.00)
3. [fact] scholar raises point 1 on the proof, citing ledger_of_tolls: it lands. (+1.00)
4. [fact] diplomat concedes fact. (+0.64)
5. [definition] scholar calls clerk, who raises point 2 on the proof, citing clerk_saw_it: it falls flat. (+0.38)
6. [definition] diplomat raises point 3 from what is owed: it falls flat. (+1.00)
7. [definition] scholar calls clerk, who raises point 4 on the proof, citing clerk_saw_it: it falls flat. (+0.93)
8. [definition] diplomat answers clerk's point 4 (evidence) as one of their own: it falls flat. (+1.00)
-> budget; band Partial (+0.04): surety, and the matter adjourned to the docket
```

**A negotiation** (dyadic; an offer; each must answer the last; consent). Offer, counter, a turning away that is
seen, acceptance:

```
[negotiation, arranged by orator; decided by diplomat's consent; 3 turns each]
1. [the terms] orator raises point 0 as one of their own: it falls flat. (-0.01)
2. [the terms] diplomat raises point 1 from what is owed: it half lands. (-0.07)
3. [the terms] orator raises point 2 as one of their own: it falls flat; he has turned away from what was put to him and the room marks it. (-0.13)
4. [the terms] diplomat answers orator's point 2 (solidarity) from what it will bring: it lands. (-0.13)
5. [the terms] orator raises point 3 from what is owed: it lands; he has turned away from what was put to him and the room marks it. (+0.60)
6. [the terms] diplomat concedes the terms and yields. (+1.00)
-> yielded by diplomat; band Success: an obligation between them
```

**A rally** (epideictic; a theme; nothing to answer). Lost on ethos, won on pathos, and one body of the crowd
unmoved:

```
[rally, arranged by orator; decided by guildsmen, toll_men, townsfolk; 3 turns]
1. [the theme] orator raises point 0 as one of their own: it falls flat. (-0.07)
2. [the theme] orator raises point 1 from what is owed: it lands. (+1.00)
3. [the theme] orator raises point 2 from what it will bring: it lands. (+1.00)
-> budget; guildsmen +6.06, townsfolk +5.59, toll_men -0.04; band Overwhelming
```

**A debate** (deliberative; a motion; may answer or raise; every seat decides):

```
[debate, arranged by orator; decided by judge, judge2, judge3; 4 turns each]
1. orator raises point 0 from what is owed: it lands. (+0.38)
2. diplomat answers orator's point 0 (authority) from what is owed: it lands; he wanders from the point. (+0.14)
3. orator raises point 1 from what is owed: it falls flat. (-0.16)
4. diplomat raises point 2 from what is owed: it falls flat. (-0.09)
5. orator presses diplomat from what it will bring: diplomat holds. (-0.29)
6. diplomat presses orator from what it will bring: orator holds. (-0.09)
7. orator raises point 3 from what it will bring: it half lands. (+0.09)
8. diplomat rests. (+0.09)
-> budget; judge -2.19, judge2 -0.17, judge3 -3.63; band Failure: the motion recorded defeated
```

**A questioning** (the questioned must answer and is his own judge). A forged writ, a lie seen for what it is by
the record, a rattle:

```
[questioning, arranged by fox; decided by bully; 4 turns each]
1. fox presses bully on the proof, with forged_writ: bully holds. (-0.37)
2. bully raises point 0 as one of their own: it falls flat. (+0.25)
3. fox raises point 1 from what it will bring: it lands; it is not what he himself holds. (+0.52)
4. bully raises point 2 from what it will bring: it lands. (+0.27)
5. fox raises point 3 from what it will bring: it half lands; it is not what he himself holds. (+0.27)
6. bully answers fox's point 3 (consequence) from what it will bring: it lands. (+0.27)
7. fox presses bully from what it will bring: bully is rattled. (+0.57)
8. bully answers fox's point 3 (consequence) from what it will bring: it lands. (+0.57)
-> budget; bully +4.62; band Overwhelming: he gives it up
```

A rough edge the transcripts show and the design keeps: a man answers the point he *believes* still stands (beat
8 above); where the room no longer credits it, his answer achieves nothing. The continuity invariants hold on all
of this: over 12,947 beats in the eight rites, with automatic and random choosers, **0** violations of: the beats
chain from first to last; every argued beat names the point it raises or answers; an answer addresses a point of
the other side; no beat shows an item its mover does not hold or of a kind the card does not admit; no beat
argues an issue already conceded; no move is made that the card bars; a beat that turns away from the live point
is charged; nobody exceeds the card's turns; the verdicts are the card's deciders; every track equals its lean
plus the beats' moves.

---

## D. The handshake: primitives up, theory down

### D.1 The primitives (bottom-up; one owner each)

| primitive | owner | definition | the one thing it does |
|---|---|---|---|
| `pool_of`, `even_line`, `opposed_ob` | `sigma_leverage.py` (B04.24) | `max(floor, score + addends + pool_add)`; `0.4 x pool_add`; `0.4 x score` | the dice, the even line, the opposition |
| `roll_net_continuous`, `net_boost` (soft cap) | `sigma_leverage.py` | `N(0.4 p, 0.8 sqrt p)`; `1.5 tanh(sigma / 1.5) x 0.8 sqrt p` | one draw; leverage that saturates |
| the obstacle composer, `Margin` | `roll.py::obstacle` (B05.14) | `even + difficulty + opposition + sum(raw x step)` | every obstacle in a sitting, and the abridged form's control equality |
| the keyed `Draw` | `dice_engine/draw.py` (B06.03) | a stream from (seed, actor, label) | determinism; fixed counts |
| the one ladder | `dice_engine.degree_from_net` | margin < 0, < 1, < 3, else | grades a verdict, in the host only |
| `weighted_tenth` | `sigma_leverage.py` (B24p.07) | a blend to the tenth | Reason and Presence in the dice |
| `Present` | `inputs.py` | part 2 §A.1 | who is in the room |
| `bearing`, `care`, `tie` | `person_q.py` | part 2 §A.2 | what a thing means to a person |
| `fit`, `aim`, `credit`, `insincerity` | the module | part 2 §A.2 | the reading as leverage and as deduction |
| `elab`, `wF`, `wA` | the module | part 2 §C.3 | the listener's own judgement |
| `manner` | the module | part 2 §C.2 | decorum and composure |
| the hold (`drift`) | the module | part 2 §C.2 | staying on the point |
| `speech` | the module | part 2 §C.2 | one margin per listener |
| the press | the module | part 2 §C.4 | the rattle |
| `Rite` cells | `arrangements.yaml` | part 2 §B | what kind of proceeding this is |
| `Sitting`, `Point`, `Beat` | `inputs.py` | part 2 §C.1 | what is live; the record |
| `View`, `Option` | the module | part 2 §E | what a chooser has |
| `auto` | the module | part 2 §F | the man's own judgement |
| the close | the module | part 2 §D | the verdict margins |
| `tilt`, `power` | the host builder | part 2 §H | the arranged cells |
| context rows | `arrangements.yaml` | part 2 §I | era, regime, strife on the cells |
| `Item`, the matters roster | `rosters.yaml` | part 2 §G | what may be shown |
| the disposal rows, the fold | `arrangements.yaml`; `loop/resolve.py` | part 2 §J | the world's change |
| `Card` | the host builder | part 1 §E | legibility |
| `strain_carried` | `person_q.py` | part 2 §A.4 | what he carries in |

### D.2 The claims (top-down), the primitive that carries each, and the link as run

| # | claim (source) | carried by | the link, with the carrier and without it | verdict |
|---|---|---|---|---|
| T1 | a position holds unless something moves it (A-79) | the close at an empty track; the mirrored opposition | the tell: fail 0.565, carried 0.282; at controls the same | pass (within 3 points at B05's `routine`; 0.247 at 0.8) |
| T2 | a trial turns on proof and refutation at a stasis (`RO:90`, `RO:99`) | the close; `credit`; the answer; `issues` | D1's four bins against the flat control; answering 0.688 against 0.602; descending 0.540 against 0.458 | pass |
| T3 | the case wins the bench, the speaker the crowd (R11; `RO:77`) | `k` in the dice | the scholar 0.58 and the orator 0.29 before the bench; 0.29 and 0.44 before the crowd | pass |
| T4 | going after the man is a real move, bounded by the room (`NP:253`) | the press; `reactance` | one press then argue 0.541 against 0.428; a rattle that does nothing 0.485 | pass; **residual**: against a weak man pressing every time (0.655) still beats stopping at one |
| T5 | composure: Will whether, Grace whether it shows, Focus whether he keeps the point (R1) | the press's opposition; `manner`; the hold | rattled 0.508 / 0.329 / 0.188 by Will; margins after a rattle -3.72 / -2.22 / -1.15 by Grace; Focus +0.008 (z 2.8) in a famine | pass; Focus weak |
| T6 | the listener judges with his own mind (R12; ELM, `NP:62`) | `elab`, `wF`, `wA` | Reason +0.025 (z 7.1) and -0.013 (z -3.6); Attunement -0.020 (z -9.2); Focus -0.006 (z -1.8); each exactly 0 with its setting off | pass; Focus weak |
| T7 | reading the room is a skill (R1; the study's elicitation) | the `View`'s blur | 0.406 against 0.440; 0.467 both with perfect reading | **weak** |
| T8 | a man's character is part of his case (`PM:39-47`) | `insincerity` | 0.282 against 0.105; control 0.282 | pass |
| T9 | what he wants and holds is where he is moved and hurt (statement 6) | `care` in `fit` and `aim` | rattled 0.162 against 0.548; control 0.343 both | pass |
| T10 | a judge can be partial and be seen to be (statement 9) | `lean` from `stake`; the `partial` claim | 0.318 against 0.413; control 0.400, 0.420; the claim deposited | pass |
| T11 | proof is worth what its source is to the hearer (statement 7) | `credit` | +0.80, +0.30, +0.30; +0.10 against +0.60 | pass (a direct read, not an outcome arm) |
| T12 | the powerful arrange the forum and pay for rigging it (statement 10) | `tilt` | 0.617, 0.567, 0.355; legitimacy -0.47 seen, -0.16 hidden, an appeal; equals 0.617 | pass |
| T13 | the same matter plays differently in another regime, strife, age (statement 8) | the context rows | regime 0.528 to 0.612; strife 0.505 to 0.530; flattened 0.603 | pass; **the era arm is within noise** |
| T14 | the room is a body, for or against a speaker (statement 9) | `mood`, `heat`, the crowd | drift 0.358 against 0.059; a crowd changes 58 of 300 trials | pass |
| T15 | a need makes a man take terms (statement 7) | `stake` to `lean` to consent | 0.537 against 0.828; control 0.563 both | pass |
| T16 | a loss is a place to go next (statement 3; A-80) | the disposal rows | an acquittal that is precedent, a grievance, an appeal in 45 of 80 runs | pass |
| T17 | the bearer holds the initiative (`NP:118`) | the order; an answer only undoes | +0.043 ± 0.021; +0.006 where nobody may answer | pass |
| T18 | exchanges answer one another (R13) | `relation`, `evade`, `Point` | 0 violations in 12,947 beats | pass |
| T19 | unwatched, each man argues as himself (statement 5) | `auto` | table B.5 | pass |
| T20 | a careful player out-argues the man himself (statement 4) | the `View` | within ±0.03 in every rite | **fail** (part 4 §I question 1) |

**Totals:** 20 links; 16 pass, 3 weak (T7; the Focus arms of T5 and T6; the era arm of T13), 1 fail (T20).
No orphan primitive: all 38 settings move outcomes over the battery, and each primitive of D.1 is named by a
claim. No uncarried claim but T20. **Links that failed on the first run and what changed in the design:**
(1) *going after the man* was either dominated or dominant: a failed press still pulled its target, so pressing
an arguer always paid; the pull now follows only a landed press and `press_ob` rose. (2) *answering* earned
nothing; under `must` a press and a silence now count as turning away, and the answer carries a level.
(3) *silence beat speaking* under a charge; silence is now charged as evasion. (4) *the crowd* counted the bench;
it is now those who neither speak nor decide. (5) a party who decides and presses moved no track of his own; the
press now reaches him as an argument does. (6) *descending* was never chosen; a concession now replaces the
standing on the old issue, so it pays exactly when he is further behind than it costs. (7) the man addressed
started as an adversary of every matter; a party's own side no longer enters his bearing. (8) the listener's
Reason read no slope; elaboration was rescaled. (9) strain carried summed without bound inside one season; the
k-th rattle now counts half. (10) `gag` (a heavier press for the weak side) moved nothing over the battery and
was **cut**. A second chooser built to beat the automatic policy by planning for the close did not, and was
deleted rather than kept as apparatus.
