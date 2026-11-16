# SC — the social contest redesigned, v2, part 3: the scene and the world; verification by execution; the handshake

## Status: PROPOSED (the third part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## A. Thematic, immersive, worldly

**What a player sees.** The card: what kind of proceeding this is, who arranged it, how far it is tilted and
against whom, who is in the room in which role (and who stepped down for a conflict), what the live thing is and
who must answer whom, **what silence means here and what happens if nobody speaks** (an unpressed charge lapses),
what he may do and what is barred, what may be shown, the standard the occasion expects, the pull of the times, who
decides, how long and when it closes, what each outcome writes. Before the sitting, if the forum is tilted against
him: accept it, contest it, or go elsewhere. At each exchange: the issue, their point and his, the room's mood and
his odds on that reading, what the man opposite seems to want, his own standing, weariness and how far the bench
cows him, whether he bears the matter with nothing of his standing (then resting is a charge not pressed), whether
his temper has broken (then he cannot hold his tongue and resting is not offered), and a menu in which every line
carries the worth and chance he perceives and the frame he would put it in, or the thing his press would hit.
After it, if it went against him: accept, appeal, another forum, or carry a grudge.

**What a rattled man looks like.** The room moves against him as each listener reads his nerves (an attuned one
discounts an honest man's, and reads a false man's as guilt); his standing falls unless his Grace has headroom; his
heat pulls him off the point unless his Focus holds; he tires sooner. If the heat runs past what his Will and Grace
carry, his temper breaks: he must speak, press or give way, and the room remembers, once, that he broke. The heat
cools as he speaks.

**What the world keeps** (the host writes; part 2 §J): the beats; who was rattled and by whom; whose false word a
listener saw through; who would not answer (contumacy); who lost his temper; a judge's conflict, a ruling against
the room, and how a ruling was received (a brute's or a respected man's, right or wrong by the record); a rigged
forum and who it worked against; what was shown, and what a questioned man yielded; who stood by whom; what each
wanted, moved by the outcome; the disposal; what a bystander heard; the docket the loser's choice wrote; a strife
eased by what was resolved. All of it bounded, and all of it fading between seasons.

---

## B. Verification: ONE battery on the current model

`checks_v8.py` (`sc_model_v2/`, `PYTHONHASHSEED=0`, output `v8_out.txt`); n = 300 sittings an arm unless stated
(two standard errors of a difference of shares about 0.08; 0.055 where n = 600). "all-mid": every attribute 4,
rank 1, flat interiors. Every figure in these four files is from this one run; it replaces all earlier runs. The
fix pass's own probes are its last part (`fix2/`); the premise-check's figures ("before") are on the model as it
stood, kept in `fix2/before/`.

### B.1 The defects and the five causes, as they stand

| | reading | control |
|---|---|---|
| D1 a bench reads the sitting | trial carried 0.123 / 0.239 / 0.316 / 0.674 by the presiding seat's track (<= -3, < 0, < 3, >= 3); excommunication 0.250 | `track_step` 0: 0.277 / 0.301 / 0.263 / 0.261 |
| D2 the centre (n = 900) | the plan's plain roll: fail 0.350, half 0.171, carried 0.479. Under A-137: fail 0.572, half 0.126, carried 0.302 at `routine` 0.5; 0.602 / 0.139 / 0.259 at 0.8. Residual against A-79's 59 / 16 / 25: the cell that gives 25 % carried lies between | at controls the same; the abridged margin is the one roll on 200 of 200 keys |
| D3 the press | against a Will-2 Grace-2 respondent who plays automatically: one press FIRST, before any point of his own (so the burden prices it), then argue 0.453; argue only 0.507; press every turn 0.080 | a rattle that does nothing: 0.367 / 0.510 / 0.057 |
| F2 a concession decides | the questioner gets it 1.00 if the questioned concedes at once, 0.37 automatic, 0.23 if never; trial: `for` carried 0.65 when the accused concedes every turn against 0.26 when never; a full confession convicts 0.733; an accuser who drops the charge 0.00; a debate's mover who withdraws 0.00 | |
| D4 strain carried | bounded below 1.0 by construction (part 2 §A.4) | |
| D5 the opener | trial: `for` opens 0.303, `against` opens 0.337 (-0.033 +- 0.053): no opener's edge | |
| D6 consent | negotiation: 37 accepted, 16 withdrawn, 247 impasses with no band | by construction |
| D7 types | table B.2; every move and end occurs; of 55 settings 8 read inert over the settings panel (`admit_step`, `gap_step`, `bias_step`, `relevance`, `temper_break`, `grain`, `grudge`, `pride`): each moves its own arm (B.3, B.4) | |
| D8 the adjudicator's operands | table B.3; each exactly 0 with its setting off | |
| **C1 speaking between equals; silence** | the accused (charged) rests every turn / answers where a point stands, else rests: crown 0.627 / 0.293 (z +8.7), theocracy 0.660 / 0.300, commune (`free`) 0.340 / 0.280; inquisition 0.660 / 0.293; examination 0.567 / 0.233. The accuser (the bearer) rests every turn 0.033 / argues 0.320 / automatic 0.283 (trial); questioning 0.173 / 0.440 / 0.340; debate (no burden) 0.257 / 0.310 / 0.280; conversation 0.330 / 0.400; audience 0.250 / 0.293. Nobody speaks: trial 0.157 (card 0.141), inquisition 0.147 (0.152), questioning 0.237 (0.214), debate 0.263 (0.277: no burden). Mean move toward the speaker at those who decide, all-mid trial: raise +0.44, answer +0.46, press -0.28; debate +0.33, +0.59, -0.36. True-best option, share of decision points: trial raises 0.37, answers 0.31, press 0.24, rest 0.05, concede 0.02; questioning 0.57 / 0.27 / 0.06 / 0.08 / 0.03; debate press 0.46, rest 0.29, answers 0.13, raises 0.11 (but the automatic debaters argue 629 times to 315 presses in the cast, §B.2; all-mid 674 to 591); the formality of the venue: trial (formal) silence costs +0.270, arbitration (plain) +0.243 | silence rule off (crown): the accused rests 0.305, argues 0.352 |
| **C2 a party who decides** | a Reason 1 → 7 speaker arguing every turn, by who decides: a bench +0.357 (z +10.1), the other party in a conversation +0.470, in a questioning +0.477, a noble +0.213; against a sound-but-plain deciding party +0.403, +0.417, +0.233: **no sign change**; Presence, Grace, Will, Attunement likewise (C2.2b); a man who says nothing moves the deciding party by none of his own attributes (+0.000 for Reason, Will, Presence). His own argue against rest toward his side (n = 1,500): with a stake the questioned man +0.082 (z +5.2), the noble +0.045 (z +2.9), the inquisitor +0.129 (z +7.5); with none +0.032, +0.007, +0.071 | |
| **C3 the rig's price** | the full rig's price 0.245 against the half rig's 0.060 at gap 5 (0.144 against 0.036 at gap 2), whoever is in the room; P(the arranger carries) at gap 5 by rig 0 / 0.5 / 1: Reason 1 0.247 / 0.307 / 0.317, Reason 4 0.330 / 0.433 / 0.473, Reason 7 0.430 / 0.577 / 0.680, and the best rig on `2 x stake x P - price` at stakes 0.5 / 1 / 2 / 4: [0, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 1], [0.5, 1, 1, 1]: each level best somewhere (C3.6 over nine cases: ⟦C3G⟧). An accused of rung 4 arranging gets tilt 0.99 whatever his tie to the accuser (-0.1, 0, +0.3), and the card names him; between equals the tilt is 0 and no arranger is named. After a rigged loss the arranger who lost resents the winner -0.028 (his own rig counts for nothing), the rigged-against loser -0.349; when a third party rigs for `a` and `a` loses, `a` appeals only on a brute or wrong judge's grounds; every loser's regard for the judge -0.193 (nobody warms to a packed or brutish judge). The weak party's acts: accept, contest, elsewhere (only with another forum), shown with their worth; he goes elsewhere at full rig and full stake | power flattened |
| **C4 the temper** | ⟦C4⟧ | `temper_break` off |
| **C5 the record as a story** | ⟦C5⟧ | |

### B.2 The types in play (the cast, effort 3, automatic, 150 sittings a row)

| row | argue : press : concede : rest | answers : raises | ends | bands (O, S, P, F) |
|---|---|---|---|---|
| conversation | 384 : 251 : 73 : 72 | 91 : 293 | yielded 73, budget 75, rested 2 | O 9, S 87, P 11, F 43 |
| negotiation | 419 : 204 : 71 : 74 | 145 : 274 | budget 78, yielded 71, rested 1 | S 67, F 4, no band 79 |
| questioning | 619 : 78 : 95 : 86 | 207 : 412 | yielded 95, budget 55 | O 7, S 107, P 7, F 29 |
| inquisition | 1049 : 96 : 20 : 35 | 496 : 553 | budget 148, yielded 2 | O 64, S 52, P 16, F 18 |
| trial | 962 : 162 : 27 : 49 | 458 : 504 | budget 150 | O 51, S 41, P 17, F 41 |
| debate | 629 : 315 : 33 : 156 | 202 : 427 | budget 111, yielded 33, rested 6 | O 14, S 28, P 23, F 85 |
| rally | 395 : 0 : 0 : 29 | 0 : 395 | budget 121, rested 29 | O 23, S 49, P 26, F 52 |
| audience | 297 : 0 : 0 : 2 | 0 : 297 | budget 148, rested 2 | O 58, S 41, P 13, F 38 |

Conversation (all-mid, n = 300): carried 0.353 (O 20, S 86, P 40, F 154). Negotiation (all-mid): accepted 45,
withdrawn 19, impasse 236. Invariants over 12,749 beats (and 8,872 in the A-139 run, someone holding both cells in
800 of 1,600 sittings): **0 violations** of: the beats chain; an argued beat names its point; an answer addresses
the other side's point; an item is held and admitted; no conceded issue is re-argued; no barred move; a priced
beat moves the room; only a speaker who decides moves his own track; nobody exceeds the card's turns; the verdicts
are the card's adjudicators; one character is refused; every track equals its start plus the beats; consent
returns no verdict.

### B.3 The attributes (carried at 1 against 7; z; then with the operand's own setting off)

**The adjudicator's five (A-144):**

| his | arm | 1 → 7 | off |
|---|---|---|---|
| Reason (validation) | `for` sound but plain (Reason 7, Grace 2), the other polished (Reason 1, Grace 7), both arguing, a full trial | 0.077 → 0.710 (z +20.9); the other way round 0.637 → 0.050 | 0.000 |
| | the same two, both arguing consequence only | 0.427 → 0.773 (z +9.3) | 0.000 |
| Focus (the filter) | `for` wanders (Focus 1, a famine) | 0.490 → 0.410 (z -2.0) in the full trial; 0.630 → 0.533 (z -2.4) in the audience-sized arm; the other side wanders (both arguing) 0.287 → 0.303 (z +0.4) | 0.000 |
| | the theatre half (a rattle's room move) | **cut** (B12): 0.570 → 0.570 | |
| Attunement (perception) | a strained liar | 0.627 → 0.257 (z -9.8); a comfortable honest man 0.660 → 0.660; **a strained honest man 0.660 → 0.660** (B10: no longer marked down); the other side lying 0.307 → 0.537 | 0.000 |
| | `discern`: the theatre of a rattle against an honest man | 0.550 → 0.613 (z +1.6); against a liar 0.563 → 0.513 | `comfort_step` 0: 0.570 flat |
| Presence and station (`awe`) | a Will-2 petitioner before a Presence-7 judge of rung 5: awe 2.26; pressed in a trial he is rattled 1.48 times a sitting and carries 0.503 | a Will-7 peer: awe 0.00, 0.20 rattles, 0.730; the judge flattened: awe 0.26, 0.547; `awe_step` 0: 0.643; before commoner peers awe 0.01 |
| Grace (reception) | table below | |

**Reception: whether the verdict was right (by the merits of the record), and how it was received** (a rung-5 judge,
played; n as shown):

| | legitimacy | compliance | appeal weight | the crowd's regard for him | his faction's standing |
|---|---|---|---|---|---|
| right, gracious (Grace 7), n = 226 | -0.01 | 1.00 | 0.00 | +0.10 | +0.00 |
| wrong, gracious, n = 174 | -0.25 | 0.60 | 0.50 | -0.10 | +0.00 |
| right, brutish (Grace 1), n = 226 | -0.45 | 0.50 | 1.00 | -0.20 | -0.20 |
| wrong, brutish, n = 174 | -1.00 | 0.30 | 1.50 | -0.30 | -0.20 |

A simulated judge pays as a played one (right, brutish: -0.43, 0.50, 1.00, -0.20, -0.20; n = 230). Control, Grace 4:
right -0.23, 0.75, 0.50, -0.05, -0.10; wrong -0.62, 0.45, 1.00, -0.20, -0.10. **How far station binds** (`brute`):
Grace 1 at power 0 / 3 / 5 / 7 / 9: 0.00 / 0.91 / 0.99 / 1.00 / 1.00; Grace 4: 0.00 / 0.41 / 0.49 / 0.50 / 0.50;
Grace 7: 0.00 at every station.

**The speaker's six** (1 → 7, z):

| | Focus | Reason | Attunement | Presence | Grace | Will |
|---|---|---|---|---|---|---|
| the tell | 0 | +0.450 (13.1) | +0.070 (1.9) | +0.150 (4.1) | +0.143 (4.4) | 0 |
| trial | -0.003 (-0.1) | +0.160 (4.3) | +0.083 (2.3) | +0.227 (6.3) | +0.337 (10.5) | +0.083 (2.3) |
| rally | +0.003 (0.1) | +0.177 (4.5) | +0.063 (1.6) | +0.243 (6.3) | +0.107 (2.9) | +0.003 (0.1) |

**Each operand against its own setting off:** Reason's `relevance` own share +0.273 (tell), +0.187 (bench), +0.250
(crowd); and it is magnitude, never sign: a tell on consequence at Reason 1 / 4 / 7 carries 0.280 / 0.620 / 0.840
where the matter helps the listener and 0.013 / 0.115 / 0.388 where it hurts him. Reason's `gap` against a power-6
respondent 0.033 → 0.417, against 0.137 → 0.417 off. Attunement's `frame` own share +0.090, +0.040, +0.083 (0.000
with a perfect reading); the frame is the listener's true best in 0.61 / 0.80 / 1.00 of speeches at Attunement 1 /
4 / 7; the gauge: a perceived-best chooser carries 0.297 / 0.360 / 0.427 in a trial (+0.130, s.e. 0.039; exactly
0.000 with perceived = true), +0.053 in a conversation, +0.067 at an audience, +0.070 at the tell; perceived intent
correlates +0.45 and +0.97 with the truth; perceived worth correlates +0.66 / +0.83 / +0.99 with true worth, mean
error +0.01 / +0.00 / -0.00. Presence's `heard` own share +0.133 before a crowd, about +0.01 where there is nobody to
be heard over (there it acts by its share of the dice); before a crowd at the proof 0.490 → 0.677 (0.610 → 0.677
off). Grace's `esteem` +0.087, +0.077, +0.170 (0.000 off); in a trial 0.107 → 0.350 (flat off). Will's staying
power 0.450 → 0.590 over five turns (0.590 flat off). R11's venue arm: a Reason-7 Presence-2 man against a
Presence-7 Reason-2 man on one ground: 0.493 against 0.143 where the venue leans to the case, 0.373 against 0.217
where it leans to manner. **Focus and Will: §B.6** (B14, B15).

### B.4 Silence, temper, the party who decides, the view

| check | reading |
|---|---|
| **silence is not free (A-145)**: the accused in a trial; `for` carried when he rests every turn / argues every turn / plays automatically | crown (`refusal`) 0.578 / 0.307 / 0.317; theocracy (`admits`) 0.630 / 0.305 / 0.318; commune (`free`) 0.302 / 0.347 / 0.333; with the rule off 0.305 / 0.352 / 0.335. So a regime changes what silence costs, and under a crown or a theocracy silence is far worse than answering |
| **a broken temper cannot hold its tongue (A-146)**: a debate; `for` puts a point, presses twice, then argues; the other man rests whenever he may (n = 600) | a low man (Will 2, Grace 2): 0.36 of his beats made with his temper broken, the provoker carries 0.513 against 0.427 with the rule off (+0.086, 2 s.e. 0.053); an ordinary man 0.03 and 0.230 against 0.232; a high man (Will 7, Grace 7) never breaks: 0.132 both |
| the NPC's temper (A-136) | composed men: the automatic policy is the perceived-best chooser (+0.000 in every rite for the flat, the cool and the hot proud man); the hot timid man +0.010 and +0.013 (his broken beats) |
| each man as himself (a trial, the cast) | the orator presses 0.23 of his beats and argues fellowship 0.37; the scholar argues on the proof 0.42; the bully as one of their own 0.29; below the break the temper terms change nothing (the shares are identical with them off): a composed man is his view, his attributes and what he holds |
| **a party who decides** | the party's own argue against rest (n = 600, flat): the man addressed in a conversation 0.303 against 0.325, the questioned man 0.272 against 0.340, the noble 0.232 against 0.305 (`for` carried; arguing helps the decider in all three); control, the accused in a trial (not a decider) 0.307 against 0.598. A questioned man who stays silent: the questioner gets it 0.298, against 0.275 when he answers (his silence is a refusal to yield, priced only as the room's contempt). With and without a stake, n = 1,500: §B.1 C2 |
| a noble's stake | start -0.60; the petitioner carries 0.193 against 0.267 flattened; an onlooker holds a `partial` claim; a played noble ruling against his own mind returns a departure of 6.37 |
| the view leaks nothing | each perceived number has its own noise: among poor readers the errors of two options correlate -0.009, argue against press on one ground -0.054, an option and the mood -0.079, mood and their point +0.023; `esteem` is perceived (s.d. 0.41 about the truth); resting's worth, `awe`, the frame and the press's object have their own normals. No `Present`, track or `terms` |
| odds | the trial's card shows 0.141 (nobody speaking: the charge lapses); 0.132 delivered with both sides silent (n = 600); the abridged menu's chance to land 0.424 against 0.432 delivered |
| refusals, each keyed | one character; one person as both parties; an abridged act whose only decider is the speaker; a rally with nobody on the floor; a cohort of weight 0; resuming a sitting that ended `yielded`; an unlawful rite; a bench rite with no seat of its authority. A two-turn sitting resumed under four turns runs four more beats |

### B.5 Character, context, power, the world

| claim | shipped | control |
|---|---|---|
| fit reads the matter | guild +1.00, toll men -0.50, townsfolk -0.05 | flattened 0.00 |
| a press bites by what the matter does to what he holds (B7) | rattled 0.143 at pursuit 0.1 and 0.280 at 0.9 when the matter does not touch it; 0.157 and 0.497 when it does | flattened 0.197 throughout |
| sincerity | before an attuned crowd: honest 0.377; a self-serving lie 0.167; an argument on a claim he knows false 0.237; a press with a forged writ 0.017 | `ploy_step` 0: 0.377; 0.377; 0.467; 0.100 |
| a partial judge | 0.457 before the respondent's client, 0.567 before a neutral seat | 0.597, 0.590 |
| credit by tie | +0.50 neutral (a fellow of the bully's faction), +0.00 the respondent's client | +0.80, +0.80 |
| a need | the diplomat accepts 0.330 with none, 0.507 with a need of 0.9 | 0.200, 0.200 |
| strife, regime, era (the toll trial, the cast) | crown 0.590; theocracy 0.570, commune 0.620; famine 0.570, war 0.503; faith 0.603, mercantile 0.587 | 0.590. **War moves the outcome; regime and era act on play** (§B.6) |
| power (the bully arranges the toll trial) | fair 0.590; firm 0.567 (tilt 0.47, price 0.055); rigged 0.543 (tilt 0.94, price 0.221; his client recuses, the floor thinned) | power flattened 0.610 |
| the fold | 300 trials: `detain` 170, surety 40, acquittals 90, offices contested 84, precedents 260, a conflicted ruling priced 170; regard writes up 1,536, down 3,339; 300 conversations: up 410, down 505 | |
| three and twelve seasons | ⟦D2⟧ | |

### B.6 The second pass's other items

⟦B6⟧

## C. Transcripts: seed 0 of each rite on the current model (not selected; `transcripts_v8.py`, output `transcripts_v8_out.txt`)

Rendered by the template renderer from the beat record alone (B.2 says how typical each band is). Five of nine:

```
[trial: on a charge, arranged by custom; decided by judge; silence: refusal; 4 turns each]
1. [fact] scholar raises point 0 on fact on the proof, citing ledger_of_tolls: it half lands; his bearing tells against him.
2. [fact] diplomat presses scholar from what is owed on his faith: scholar holds; his bearing tells for him.
3. [fact] scholar raises point 1 on fact on the proof, citing ledger_of_tolls: it lands.
4. [fact] diplomat answers scholar's point 1 (on the proof) from what is owed: it falls flat.
5. [fact] scholar presses diplomat as one of their own: diplomat holds.
6. [fact] diplomat answers scholar's point 1 (on the proof) as one of their own: it lands.
7. [fact] scholar presses diplomat on the proof, with ledger_of_tolls: diplomat holds.
8. [fact] diplomat answers scholar's point 1 (on the proof) from what it will bring: it falls flat.
-> budget; judge -0.73; Failure: an acquittal on the case file, a precedent; the ruling received

[questioning: on a question; decided by bully (the questioned man); silence: refusal; 4 turns each]
1. fox raises point 0 on the question on the proof, citing forged_writ: it falls flat; it is not what he himself holds.
2. bully raises point 1 as one of their own: it falls flat.   3. fox raises point 2 as one of their own: it falls flat.
4. bully raises point 3 as one of their own: it falls flat.
5. fox raises point 4 on the proof, citing forged_writ: it lands; it is not what he himself holds.
6. bully answers fox's point 4 (on the proof) from what it will bring: it lands.
7. fox presses bully from what it will bring on his tolls: bully is rattled.
8. bully concedes the question and yields.
-> yielded by bully: Success (his own giving way): what he yielded is a claim in the fox's ledger

[inquisition: on a charge; decided by bishop (the accuser sits; the bishop is a party, so he does not recuse); silence: admits]
1. [fact] bishop presses scholar from what it will bring on his learning: scholar holds; he has put nothing of his own and the room marks it.
2. [fact] scholar raises point 0 on fact on the proof, citing ledger_of_tolls: it lands.
3. [fact] bishop answers scholar's point 0 (on the proof) from what is owed: it lands.
4-6. the same again: the scholar's proof lands, the bishop answers it; then the scholar raises a point framed on faith.
7. [fact] bishop presses scholar as one of their own: scholar is rattled; scholar's point 2 stands unanswered; he has put nothing of his own and the room marks it.
8. [fact] scholar raises point 3 on the proof, citing clerk_saw_it: it falls flat; he wanders from the point.
-> budget; bishop -6.45; Failure: an acquittal; the bishop's conflict (the accused is his client) priced

[debate: on a motion; decided by judge, judge2, judge3 (a quorum of two carries); silence: free; 4 turns each]
1. orator presses diplomat as one of their own: diplomat holds.  2. diplomat presses orator on his trade: orator is rattled.
3. orator rests.  4. diplomat presses orator on his trade: orator is rattled; his bearing tells for him.
5. orator presses diplomat on his trade: diplomat holds; he wanders from the point; his bearing tells against him.
6. diplomat rests.  7. orator concedes the question and yields.
-> yielded by the mover: the motion withdrawn, Failure (nothing left to decide); recorded defeated

[trial, arranged by bully (tilt 0.94; his client judge2 stepped down, so the judge presides): the scholar raises four
points on the proof and the law, the bully answers one and presses twice -> budget; judge +1.31; Success: the bully
detained, a precedent; the bully's faction pays for the rig; the judge's slight lean his way is priced]
```

Read honestly: the trial is proof and refutation at the first stasis; the questioning has a questioner who asks and
a questioned man who answers, is rattled on what he wants, and gives way; the inquisitor who will not put his
charge is marked for it each time; the debate between these two men is still a contest of presses, because the
diplomat has no case to make on the remitting of the tolls and goes after what the orator wants (it is the
characters, not the rule: between flat men a debate argues, part 3 §B.1 C5), and the mover, twice rattled with the
room wholly against him, withdraws his motion. None of the
"wait, what?" scenes of the premise-check remains: no questioning without a question, no debate gone silent, no
failed rally awarding legitimacy, no packed judge thanked by the man he ruled against (§B.1 C3).

## D. The handshake: each claim, its carrier, the link as run

Each link is run with a control in §B; the reading column names where. The figures are §B's and are not repeated.

| # | claim (source) | carried by | reading | verdict |
|---|---|---|---|---|
| T1 | a position holds unless something moves it (A-79, A-137) | the close; the mirrored opposition | D2 | pass, with its residual |
| T2 | a trial turns on proof and refutation at a stasis | the close; `credit`; the answer; `issues` and their `weighs` | B.1 C1, C5; B.2 | **pass**: the accused answers, descents buy the next rung's ground and cost |
| T3 | the case wins where the venue leans to it (R11) | `k` | B.3 venue arm | pass |
| T4 | going after the man is a real move, bounded | the press, its object; `reactance` | B.1 D3; C1's dominance matrix | pass; pressing no longer crowds out argument between flat men |
| T5 | composure: Will, Grace, Focus (R1) | `weary`, the press's opposition; `esteem`; the hold | B.3 | pass; Focus under pull only, and modestly (decided) |
| T6 | the adjudicator validates, filters, perceives (A-144) | `validation`, `wF`, insincerity and `discern` | B.3 | pass; the theatre half of Focus is cut |
| T7 | Attunement gauges his choices and frames his speech (A-141, A-142) | `perceived`, `frame`, the believed reading | B.3; B.4 | pass |
| T8 | a man's character is part of his case | `insincerity`, `caught` | B.5; B.6 B2 | pass |
| T9 | fit reads the matter, at any Reason | `landing`; `relevance` as magnitude | B.3, B.5 | pass |
| T10 | a judge can be partial and be seen to be, and recuses or pays | `start`; `conflict`; recusal; the `partial` claim; `partial_price` | B.5; B.6 B6 | pass |
| T11 | proof is worth what its source is to the hearer | `credit` | B.5 | pass |
| T12 | the powerful arrange the forum and pay | `tilt`, `rig_price` | B.1 C3 | pass; each rig level best somewhere |
| T13 | strife, regime and era bear on a sitting | the context rows; the `silence` cell | B.6 C | **on play**: strife moves outcomes; regime and era move choices (question 1) |
| T14 | the room is a body for or against a speaker | `mood`, `heat`, `heard` | B.3 | pass on `heard` |
| T15 | a need makes a man take terms | `stake` to his accept | B.5 | pass |
| T16 | a loss is a place to go next | `after`; the docket; the season driver | B.1 D2, D3 | pass: appeals re-heard and some reversed, grievances aired once |
| T17 | the bearer opens | the order | B.1 D5 | the edge is within noise |
| T18 | exchanges answer one another (A-129) | `relation`, `Point`, `left` | B.2 invariants; C5 | pass |
| T19 | each man argues as himself | the menu on his attributes and bearing; temperament past the break | B.4, B.5 | pass below the break as his view, past it as his temper |
| T20 | provoking a man out of his composure pays (A-136, A-146) | `temper_break`, heat | B.4 | pass where it can reach |
| T21 | Reason accounts for the other side's circumstances | `gap` | B.3 | pass |
| T22 | one character cannot hold a proceeding; a party may decide (A-139) | the invariant; the own-case rule | B.1 C2; B.6 B1 | pass; his choice matters where he has a stake |
| T23 | a concession decides something | the yield as decision; the accept; the leverage ceiling | B.1 D3 | pass |
| T24-26 | Reason is relevance; Presence is being heard; Grace is conduct (A-143) | `relevance`, `heard`, `esteem` | B.3 | pass |
| T27 | an adjudicator of station cows a man of less Will (A-144) | `awe` | B.3 | pass |
| T28 | a verdict's reception is apart from its rightness; a brute's is resented (A-144) | the fold's reception; `merits` | B.3 | pass |
| T29 | silence is never free where a point must be answered (A-145) | `silence_cost`; the `silence` cell; the burden | B.1 C1 | **pass for both sides** |

**Totals: 31 claims (T24-26 are three); 29 pass; 2 pass on play or conditionally (T5 Focus, T13 regime and era).**
What failed in the premise-check and changed the design is part 4 §K, item by item.
