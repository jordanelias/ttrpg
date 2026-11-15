# SC — the social contest redesigned, v2, part 3: the scene and the world; verification by execution; the handshake

## Status: PROPOSED (the third part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## A. Thematic, immersive, worldly

**What a player sees.** Before the sitting, the card: what kind of proceeding this is, who arranged it and how far
it is tilted, who is in the room in which role, what the live thing is and who must answer whom, what he may do
and what is barred, what may be shown, the standard the occasion expects, how much the case counts against manner
here, who decides (or that nobody does and it turns on an accept), how long it runs, what each outcome writes. At
each exchange: the issue, their point and how far it seems to stand, his own, the room's mood and his odds on that
reading, what the man opposite seems to want, his own standing and how tired he is, and a menu with each line's
believed worth and chance. He chooses one, and sees what it did.

**What a rattled man looks like.** The room moves against him at once. His standing falls on every later speech
unless his Grace has headroom. He is pulled off the point unless his Focus holds. It has cost him staying power.
If it is past what his Will and Grace carry he stops choosing coolly: the proud press, the timid give way. Press
him again and the room gives less, then turns on the presser.

**Why each kind feels like itself.** A trial is points on a charge that must be answered, proof shown, witnesses
called and pressed, a concession that changes what the fight is about, and a bench that is never a party. A
negotiation and a conversation have no judge: they end when one of them accepts, or do not. A questioning yields
only what the questioned man gives. A debate is speeches on a motion before seats that each come down for
themselves. A rally has nobody to answer and a crowd in several bodies. An audience is a plea and a ruling.

**What the room remembers** (the host writes; part 2 §J): the beats and the end state; who was rattled and by
whom; who argued what he did not hold; a judge's stake, and a played judge's ruling against the room; a rigged
forum; what was shown; who stood by whom and against whom; what each wanted, moved by the outcome; the disposal;
the strife. A failed proposition leaves an acquittal that is precedent, a grievance, an appeal, strife inflamed
and a grudge (A-80).

---

## B. Verification by execution

Model `sc_model_v2/` (`sc2/engine.py`, `sc2/host.py`, `checks_v3.py`, `transcripts.py`), `PYTHONHASHSEED=0`,
output `v3_out.txt`; n = 400 sittings an arm unless stated (two standard errors of a share about 0.05; of a
difference about 0.07). "all-mid": every attribute 4, rank 1, flat interiors. "Before" is the stress test's
reading of the 2026-11-14 design. Readings from the first v2 run that this pass did **not** re-run are marked.

### B.1 The defects

| | before | after (reconciled model) | control | n |
|---|---|---|---|---|
| D1 a bench ignores the sitting | trial carried 0.9 % at every track; excommunication 0 of 2000 | carried 0.054 / 0.217 / 0.369 / 0.673 by the presiding seat's track (≤ -3, < 0, < 3, ≥ 3); excommunication 0.223 | `track_step` 0: 0.228 / 0.304 / 0.243 / 0.230 | 400 |
| D2 the centre | the tell carried 0.53 to 0.70 | **the plan's plain roll** (B05.25's pool, the skill score alone opposing): fail 0.344, half 0.172, carried 0.483. **Under A-137** (the resisting attribute also at 0.4): fail 0.567, half 0.136, carried 0.297 at the difficulty cell's `routine` 0.5; fail 0.616, half 0.131, carried 0.253 at 0.8. **Residual against A-79's 59 / 16 / 25:** at the 25 % point the tell fails 2.6 points more and half-lands 2.9 fewer, because an 11-die pool is wider than the 8-die pool A-79's figures were taken on; one cell cannot fit all three | at controls the same; the abridged margin equals the one roll under A-137's rule on 200 of 200 keys | 1200 |
| D3 the rattle | no rattle term; pressing dominated | against a Will-2 Grace-2 respondent **who plays automatically**: one press then argue 0.545, argue only 0.487, press every turn 0.367 (the earlier "pressing throughout wins" was an artifact of a victim forced to argue) | a rattle that does nothing: 0.482 / 0.492 / 0.372 | 400 |
| F2 a concession decides | a yielding side usually won the draw | questioning: the questioner gets what he asks 1.000 when the questioned concedes at once, 0.255 automatic, 0.000 when he never concedes; trial: `for` carried 0.773 when the accused concedes at every turn, 0.363 automatic; a full confession convicts 0.790; an accuser who withdraws carries 0.038; a debate's mover who withdraws 0.000 | the same sittings without the concession: 0.36 to 0.39 | 400 |
| D4 strain ratchets | 0 to 5.8-9 | bounded under 1.0 by the formula; greatest carried in 80 three-season runs 0.96 | | 80 runs |
| D5 the opener | 0.433 against 0.257 | trial: 0.356 against 0.331 (+0.025 ± 0.048); equal turns | | 800 |
| D6 the act's margin under consent | 198 of 2000 graded Success against the track | negotiation: Success 79, all on the other party's accept; Failure 42, all on the bearer's withdrawal; 279 impasses with no band | by construction | 400 |
| D7 types are names | room always `bench`; 9 of 53 settings inert | the eight rows differ in moves, relations, ends and bands (B.2); every move and end occurs; 1 of 44 settings reads inert over the battery, `yield_track`, because 12 and 24 both sit at the soft cap (F2 shows it live). A crowd changing bench rows: 58 of 300 trials in the first run, **not re-run** | | 150 a row |
| D8 the decider's three | a dead `sense` passed; lean outweighed the track | table B.3: each has the ruled sign in a full trial and reads exactly 0 with its setting off; `start` is where the track begins, in the track's own unit | the settings off | 400 |
| D9 integration | ten conflicts | part 4 §H; **not run** | | |

### B.2 The types in play (the cast, effort 3, automatic; 150 sittings a row)

| row | argue : press : concede : rest | answers : raises | ends | beats | bands |
|---|---|---|---|---|---|
| conversation | 542 : 193 : 55 : 1 | 24 : 518 | budget 95, yielded 55 | 5.3 | accepted 54, withdrawn 1, impasse 95 |
| negotiation | 532 : 145 : 75 : 1 | 85 : 447 | budget 75, yielded 75 | 5.0 | accepted 72, withdrawn 3, impasse 75 |
| questioning | 751 : 19 : 84 : 24 | 203 : 548 | budget 66, yielded 84 | 5.9 | he gave it up 84, he did not 66 |
| inquisition | 1078 : 14 : 86 : 22 | 383 : 695 | budget 150 | 8.0 | O 67, S 38, P 17, F 28 |
| trial | 780 : 266 : 119 : 35 | 264 : 516 | budget 150 | 8.0 | O 49, S 36, P 15, F 50 |
| debate | 583 : 545 : 0 : 72 | 161 : 422 | budget 150 | 8.0 | O 35, S 22, P 27, F 66 |
| rally | 424 : 0 : 0 : 17 | 0 : 424 | budget 133, rested 17 | 2.9 | O 25, S 45, P 28, F 52 |
| audience | 294 : 0 : 0 : 6 | 0 : 294 | budget 144, rested 6 | 2.0 | O 46, S 37, P 14, F 53 |

### B.3 The attributes (carried at 1 against 7; z of the difference)

**A decider's own three, in a full trial (F8), each with the sign the ruling gives; with its setting off each
reads +0.000:**

| his | when | 1 → 7 |
|---|---|---|
| Reason | `for` argues on the proof (quality) | 0.555 → 0.688 (+0.132, z +3.9) |
| Reason | `for` argues as one of them (manner) | 0.515 → 0.443 (-0.073, z -2.1) |
| Focus | `for` wanders (Focus 1, a famine) | 0.237 → 0.175 (-0.062, z -2.2) |
| Focus | the other side wanders | 0.340 → 0.512 (+0.172, z +5.0) |
| Attunement | `for` argues what he knows false | 0.372 → 0.055 (-0.318, z -11.9) |
| Attunement | the other side does | 0.297 → 0.703 (+0.405, z +12.5) |

**The speaker's six:**

| | Focus | Reason | Attunement | Presence | Grace | Will |
|---|---|---|---|---|---|---|
| the tell | 0 | +0.215 (6.6) | +0.030 (0.9) | +0.105 (3.1) | +0.155 (5.1) | 0 |
| trial | +0.005 (0.1) | +0.128 (3.8) | +0.070 (2.1) | +0.195 (5.8) | +0.305 (10.0) | +0.090 (2.7) |
| rally | 0 | +0.057 (1.7) | +0.017 (0.5) | +0.177 (5.4) | +0.100 (3.1) | +0.010 (0.3) |

**The restored carriers, each against its own setting at 0:** Reason accounting for a power-6 respondent's
circumstances (dice held to Presence): 0.092 → 0.323, against 0.233 → 0.323 with `gap_step` 0. Presence as the
share heard, before a crowd, arguing on the proof: 0.160 → 0.500, against 0.440 → 0.500. Will as staying power
over five turns with nobody pressing: 0.307 → 0.398, against 0.398 → 0.398. Grace as esteem in a trial against an
ordinary man: 0.142 → 0.400, against 0.315 → 0.315. Attunement reading intent: the believed stake of the man
opposite correlates +0.30 with the truth at Attunement 1 and +0.41 at 7. R11's venue arm: the same ground before
one seat, a Reason-7 Presence-2 man against a Presence-7 Reason-2 man: 0.410 against 0.125 where the venue leans
to the case (+0.3), 0.255 against 0.213 where it leans to manner (-0.3).

**Weak, and said so:** the speaker's Focus reads +0.005 in a trial (it acts only when something pulls; the famine
tell of the first run read +0.008, z 2.8, not re-run); the speaker's Attunement +0.07 in a trial and the intent
reading 0.30 to 0.41. A-138: Focus, Attunement and Will are silent at a quiet tell, as ruled.

### B.4 Played, and the NPC's temper

| check | reading |
|---|---|
| the view leaks nothing | among poor readers (accuracy under 0.3, n = 1261) the noise of two believed numbers is uncorrelated: mood and their point -0.020; two fits +0.011; intent and mood +0.008; aim and fit +0.053 (a shared term would read near 1). The view holds no `Present`, no track, no `terms` |
| odds are believed, and true of what happens | the card shows 0.277 before an unmoved ordinary bench and 0.261 is delivered with both sides silent (n = 800); under consent it shows none and the band is none; the abridged menu's mean chance to land 0.436 against 0.403 delivered (he assumes an ordinary Will and rank in the man addressed) |
| F7 speaking at a formal venue (trial, all-mid, n = 800) | argue every turn 0.261, rest every turn 0.285, automatic 0.356: a speech no longer moves the room toward the other side on average; for flat people arguing every turn and silence are level, and mixing beats both |
| the player against a man in the same seat (A-136), n = 800 | composed men (flat; Will 6 Grace 7 with a grudge): the automatic policy **is** the view-only best chooser: +0.000 by construction. A man who has lost his temper: hot and timid (Will 1, Grace 2) +0.021 trial, +0.029 inquisition, +0.017 debate; hot and proud (Will 6, Grace 1, a grudge) +0.003, -0.030, -0.007. Two standard errors 0.048: **not shown**. Temper changes what he does (press share 0.63 against 0.36 composed; the timid man concedes 0.34 of his trial turns against 0.12) but in this model costs him little |
| options | 4 to 12 a menu by rite and side (first run); the with-and-without readings for rest, descent, acceptance and answer (+0.07 to +0.09) are the first run's and were **not re-run** |
| resume | a two-turn sitting resumed under four turns runs four more beats, each speaker ending at four speeches, the beats numbered on from 5; a sitting that ended `yielded` is refused |
| refusals | a rally with nobody on the floor; an abridged act with nobody addressed; a cohort of weight 0; a judge trying his own charge; a side marked as adjudicator. A seat who accuses speaks and the other seats judge |
| a played judge | he has `JudgeView(id, track, odds, points)` and rules for, against, or by his draw; ruling against his own track of -6.38 came back as a departure of 6.38 for the fold to deposit |

### B.5 Character, context, power, the world (shipped against its flattened control)

| claim | shipped | control |
|---|---|---|
| fit reads the matter | a consequence argument for remitting the tolls fits the guild +1.00, the toll men -0.50, the townsfolk -0.05 | flattened 0.00 |
| a press on what he wants | rattled 0.138 at pursuit 0.1, 0.510 at 0.9 | 0.285, 0.285 |
| sincerity is what he knows and holds | before an attuned crowd: an honest plea 0.290; a self-serving lie 0.240; an argument on a claim he knows false 0.155; a press with a forged writ before an attuned judge 0.040 | `ploy_step` 0: 0.290; 0.290; 0.375; 0.325 |
| a partial judge | a petition before the respondent's client 0.315, before a neutral seat 0.435 | 0.367, 0.417 |
| credit by tie | the ledger: +0.80 to the neutral judge, +0.30 to the respondent's client | +0.80, +0.80 |
| a need | the diplomat accepts 0.512 with none, 0.785 with a need of 0.9 | 0.415, 0.415 |
| each man argues as himself | orator: fellowship 0.47 of his beats; scholar: the proof 0.62; the reeve: press 0.46 | with the temper terms off the shares are within 0.03: the differences come from attributes and bearing through the menu, not from temper, in men who are composed |
| strife | war 0.425 (three turns, unrest, stakes), famine 0.517 | peace 0.547 |
| regime, era | theocracy 0.542, commune 0.550; an age of faith 0.545, mercantile 0.562; an audience under crown, theocracy, commune 0.269, 0.260, 0.285 | 0.547: **within noise**. With esteem made relative (F7) a regime's standard no longer moves who wins; regime and era act through which rites are lawful, what is admitted and which ground is argued |
| power | the accuser carries 0.547 in a fair forum, 0.472 against a firm one (tilt 0.47, legitimacy -0.42 with the floor watching), 0.340 against a rigged one (tilt 0.94, the bench packed, the floor shut, two turns; legitimacy -0.16; an appeal) | power flattened 0.557 |
| the fold performs every write | 300 trials: `detain` 159, surety and adjournment 47, acquittals 94, offices contested 101, precedents 253, legitimacy up 159; regard writes up 1038, down 1718. 300 conversations: regard up 344, down 582 (the first v2 fold wrote none up) | not held: nothing |
| three seasons (80 runs, seeds 100 to 179) | the recurring trial carried 0.35 rigged, then 0.56, 0.45; the rigged trial returned as an appeal in 52 runs; the famine ended at 1.01 on average (0.25 to 1.75; began 1.00); the scholar's regard for the reeve fell from 0 to -0.42 on average (-0.90 to -0.03); the diplomat's rose in 0.10 of runs (the reeve accepted his terms in 13 of 240 sittings). **Open:** the third season's trial carried 0.57 after a first-season win (n = 28) and 0.38 after a loss (n = 52), z 1.6: a history effect or a snowball; this run cannot tell | |

**Invariants**, over 12,890 beats in the eight rites with automatic and random choosers, 0 violations of each:
the beats chain; an argued beat names its point; an answer addresses the other side's point; an item is held by
its mover and admitted by the card; no conceded issue is re-argued; no barred move; evasion is charged; no speech
moves its own side's track; nobody exceeds the card's turns; the verdicts are the card's adjudicators; no side
adjudicates; every track equals its start plus the beats; consent returns no verdict.

---

## C. Transcripts: seed 0 of each rite, not selected (B.2 gives how typical each outcome is)

```
[trial; arranged by scholar; judged by judge; 4 turns each; standard 5; Reason's share: evidence 1.0, consequence 0.9]
1. [fact] scholar raises point 0 on the proof, citing ledger_of_tolls: it lands. (+1.00)
2. [fact] diplomat concedes fact. (+0.64)
3. [definition] scholar raises point 1 on the proof, citing ledger_of_tolls: it lands. (+0.92)
4. [definition] diplomat concedes definition. (+0.64)
5. [justification] scholar calls clerk, who raises point 2 on the proof, citing clerk_saw_it: it lands. (+0.87)
6. [justification] diplomat answers clerk's point 2 (evidence) as one of their own: it lands. (+0.64)
7. [justification] scholar presses diplomat from what it will bring: diplomat is rattled. (+0.94)
8. [justification] diplomat rests. (+0.94)
-> budget; judge +1.34; Success: detained, a precedent

[negotiation; nobody judges; 3 turns each]
1. [the terms] orator raises point 0 as one of their own: it lands. (+0.45)
2. [the terms] diplomat concedes the terms and yields.
-> yielded by diplomat; accepted: an obligation between them

[rally; decided by guildsmen, toll_men, townsfolk; 3 turns]
1. orator raises point 0 from what it will bring: it half lands. (+0.12)
2. orator raises point 1 from what it will bring: it half lands. (+0.16)
3. orator raises point 2 from what is owed: it half lands. (+0.17)
-> budget; guildsmen +1.74, townsfolk +1.01, toll_men -0.22; Success

[debate; judged by judge, judge2, judge3; 4 turns each]
1. orator presses diplomat as one of their own: diplomat holds. (-0.10)
2. diplomat presses orator from what it will bring: orator holds. (+0.10)
3. orator presses diplomat from what it will bring: diplomat holds. (-0.10)
4. diplomat presses orator as one of their own: orator holds. (+0.10)
5. orator raises point 0 from what is owed: it lands. (+1.00)
6. diplomat answers orator's point 0 (authority) from what is owed: it falls flat. (+1.00)
7. orator presses diplomat from what is owed: diplomat is rattled. (+1.00)
8. diplomat rests. (+1.00)
-> budget; judge +4.36, judge2 +2.58, judge3 +1.27; Overwhelming: the decree entered

[questioning; nobody judges; 4 turns each]
1. fox presses bully from what it will bring: bully holds. (-0.32)
2. bully raises point 0 as one of their own: it lands. (-0.38)
3. fox presses bully from what it will bring: bully is rattled. (-0.14)
4. bully raises point 1 from what it will bring: it falls flat; he wanders from the point. (-0.12)
5. fox raises point 2 as one of their own: it lands. (+0.08)
6. bully raises point 3 as one of their own: it falls flat. (+0.08)
7. fox raises point 4 from what is owed: it falls flat. (-0.43)
8. bully raises point 5 from what it will bring: it half lands. (-0.46)
-> budget; no band: he gave nothing up
```

The trial walks the stasis (fact, definition, justification) through confirmatio and one refutatio; the debate
opens on the men before the motion (a temper-free pattern the model shows often: 545 presses to 583 arguments);
the rally is three appeals to what the crowd wants and holds, and one body is not moved.

---

## D. The handshake: each claim, the primitive that carries it, the link as run

The primitives are part 2's (one owner each; the restated ledger was cut as a second copy).

| # | claim (source) | carried by | with the carrier / without | verdict |
|---|---|---|---|---|
| T1 | a position holds unless something moves it (A-79, A-137) | the close at an empty track; the mirrored opposition | D2 | pass, with D2's residual |
| T2 | a trial turns on proof and refutation at a stasis (`RO:90`) | the close; `credit`; the answer; `issues` | D1's bins against the flat control; 264 answers in 150 trials; the trial of §C | pass (the answer's own with-and-without not re-run) |
| T3 | the case wins where the venue leans to it, manner where it does not (R11) | `k` | 0.410 against 0.125; 0.255 against 0.213 | pass |
| T4 | going after the man is a real move, bounded (`NP:253`) | the press; `reactance` | 0.545 / 0.487 / 0.367; a rattle that does nothing 0.482 / 0.492 / 0.372 | pass |
| T5 | composure: Will, Grace, Focus (R1) | `weary` and the press's opposition; `esteem`; the hold | Will 0.307 → 0.398 (0 off); Grace 0.142 → 0.400 (0 off); Focus +0.005 | pass for Will and Grace; **Focus weak** |
| T6 | the listener judges with his own mind (R12) | `q`, `wF`, `wA` | table B.3; each 0 off | pass |
| T7 | reading the room and the man is a skill (R1) | the `View`'s blur | intent 0.30 → 0.41; +0.07 in a trial | **weak** |
| T8 | a man's character is part of his case (`PM:39-47`) | `insincerity` | 0.290 / 0.240 / 0.155 / 0.040 against 0.290 / 0.290 / 0.375 / 0.325 | pass |
| T9 | what he wants is where he is moved and hurt | `care`, `stake` in `fit` and `aim` | +1.00, -0.50; 0.138 against 0.510; flattened 0, 0.285 | pass |
| T10 | a judge can be partial and be seen to be | `start`; the `partial` claim | 0.315 against 0.435; 0.367, 0.417 | pass |
| T11 | proof is worth what its source is to the hearer | `credit` | +0.80, +0.30; flattened +0.80, +0.80 | pass |
| T12 | the powerful arrange the forum and pay | `tilt` | 0.547, 0.472, 0.340; flattened 0.557 | pass |
| T13 | the same matter plays differently in strife, regime, age | the context rows | war 0.425; regime and era within noise | **strife passes; regime and era fail as movers of the outcome** |
| T14 | the room is a body for or against a speaker | `mood`, `heat`, `heard` | the share heard 0.160 → 0.500 against 0.440 → 0.500; the magnate arm of the first run not re-run | pass on `heard`; heat **not re-run** |
| T15 | a need makes a man take terms | `stake` to `start` to his accept | 0.512, 0.785; 0.415, 0.415 | pass |
| T16 | a loss is a place to go next (A-80) | the disposal rows | acquittal, precedent, grievance, appeal in 52 of 80 runs | pass |
| T17 | the bearer opens | the order | +0.025 ± 0.048 | pass (no edge left to explain) |
| T18 | exchanges answer one another (A-129) | `relation`, `evade`, `Point` | 0 violations in 12,890 beats | pass |
| T19 | unwatched, each man argues as himself (A-130) | the menu on his attributes and bearing; `auto` | B.5 | pass; the temper terms add little in composed men |
| T20 | a player's edge includes provoking a man out of his composure (A-136) | `temper` | +0.02 to +0.03 against the timid, about 0 against the proud; 2 s.e. 0.048 | **fail: not shown** |
| T21 | Reason accounts for the other side's circumstances (R1) | `gap` | 0.092 → 0.323 against 0.233 → 0.323 | pass |
| T22 | nobody judges his own cause (A-139) | the input's invariant; the builder | 5 refusals; 0 violations | pass |
| T23 | a concession decides something | `yield_track`; the accept | F2 | pass |

**Totals: 23 links; 18 pass; 2 weak (T5's Focus arm, T7); 1 fails in part (T13: regime and era); 1 fails (T20);
1 passes on one arm with the other not re-run (T14).** Links that failed in the antagonists' probes and were
changed in the design in this pass: the view's shared noise; a yield that won the draw; the card's odds; resume;
the crashes; the fold's dropped writes and one-way regard; speaking that tilted the room at a formal venue; the
judge's three without a positive arm; omniscient odds; fit that ignored the matter; a side as its own
adjudicator. Cut in this pass because it carried nothing: `elicit`, the policy's bonus for the proof, the
restated primitives table.
