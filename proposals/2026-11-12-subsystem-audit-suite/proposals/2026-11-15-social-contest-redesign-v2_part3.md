# SC — the social contest redesigned, v2, part 3: the scene and the world; verification by execution; the handshake

## Status: PROPOSED (the third part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## A. Thematic, immersive, worldly

**What a player sees.** The card: what kind of proceeding this is, who arranged it and how far it is tilted, who
is in the room in which role, what the live thing is and who must answer whom, **what silence means here**, what
he may do and what is barred, what may be shown, the standard the occasion expects, who decides, how long, what
each outcome writes. At each exchange: the issue, their point and his, the room's mood and his odds on that
reading, what the man opposite seems to want, his own standing, weariness and how far the bench cows him, whether
his temper has broken (then he cannot hold his tongue and resting is not offered), and a menu in which every line
carries the worth and chance he perceives and the frame he would put it in.

**What a rattled man looks like.** The room moves against him unless those who decide are focused enough to
discount the theatre; his standing falls unless his Grace has headroom; he is pulled off the point unless his
Focus holds; he tires sooner; an attuned judge reads his discomfort. Past what his Will and Grace carry his temper
breaks: he must speak, press or give way, and the room remembers that he broke.

**What the world keeps** (the host writes; part 2 §J): the beats; who was rattled and by whom; who argued what he
does not hold; who would not answer (contumacy); who lost his temper; a judge's stake, a ruling against the room,
and how the verdict was received (a brute's or a respected man's); a rigged forum; what was shown; who stood by
whom; what each wanted, moved by the outcome; the disposal; the strife.

---

## B. Verification: ONE battery on the current model

`checks_v7.py` (`sc_model_v2/`, `PYTHONHASHSEED=0`, output `v7_out.txt`); n = 300 sittings an arm unless stated
(two standard errors of a difference of shares about 0.08; 0.055 where n = 600). "all-mid": every attribute 4,
rank 1, flat interiors. Every figure in these four files is from this run; it replaces all earlier runs.

### B.1 The defects, as they stand

| | reading | control |
|---|---|---|
| D1 a bench reads the sitting | trial carried 0.055 / 0.226 / 0.323 / 0.611 by the presiding seat's track (≤ -3, < 0, < 3, ≥ 3); excommunication 0.227 | `track_step` 0: 0.236 / 0.290 / 0.226 / 0.244 |
| D2 the centre (n = 900) | the plan's plain roll: fail 0.350, half 0.171, carried 0.479. Under A-137: fail 0.576, half 0.147, carried 0.278 at `routine` 0.5; 0.619 / 0.149 / 0.232 at 0.8. Residual against A-79's 59 / 16 / 25: the cell that gives 25 % carried lies between; fail then reads about 0.60 | at controls the same; the abridged margin is the one roll on 200 of 200 keys |
| D3 the press | against a Will-2 Grace-2 respondent who plays automatically: one press then argue 0.530, argue only 0.463, press every turn 0.507 | a rattle that does nothing: 0.480 / 0.463 / 0.363 |
| F2 a concession decides | the questioned gives way 0.787 if he concedes at once, 0.420 automatic, 0.380 if never; trial: `for` carried 0.767 when the accused concedes every turn against 0.330; a full confession convicts 0.763; an accuser who withdraws 0.020; a debate's mover 0.003 | |
| D4 strain carried | greatest in 160 three-season runs 1.00 (the bound) | |
| D5 the opener | trial 0.325 against 0.250 (+0.075 ± 0.054): **an opener's edge of about one and a half standard errors has returned** | |
| D6 consent | negotiation: 37 accepted, 18 withdrawn, 245 impasses with no band | by construction |
| D7 types | table B.2; every move and end occurs; of 54 settings 4 read inert over this battery (`admit_step`, `gap_step`, `bias_step`, `relevance`: each has its own arm below that moves) | |
| D8 the adjudicator's operands | table B.3; each exactly 0 with its setting off | |
| **F7 speaking against silence** | **not fully closed.** The side that is not charged, all-mid (n = 600): trial argue every turn 0.243, rest every turn 0.300, automatic 0.353; debate 0.180 / 0.182 / 0.280; rally 0.297 / 0.293 / 0.278. Arguing every turn no longer loses to silence by a wide margin (it was 0.108 against 0.264) but does not beat it; mixing beats both. The accused (charged, so A-145 applies): `for` carried 0.400 when he stays silent, 0.428 when he argues every turn, 0.327 when he plays automatically | silence rule off: 0.298 silent |
| debate | pressing still outnumbers arguing between flat people (944 to 411) | **open** |

### B.2 The types in play (the cast, effort 3, automatic, 150 sittings a row)

| row | argue : press : concede : rest | answers : raises | ends | bands (O, S, P, F) |
|---|---|---|---|---|
| questioning | 650 : 297 : 39 : 132 | 238 : 412 | budget 109, yielded 39, rested 2 | S 35, P 19, F 66, O 30 |
| inquisition | 733 : 284 : 56 : 127 | 305 : 428 | budget 150 | O 62, S 46, P 21, F 21 |
| trial | 535 : 500 : 67 : 90 | 218 : 317 | budget 143, rested 7 | O 39, S 33, P 18, F 60 |
| debate | 479 : 577 : 0 : 122 | 136 : 343 | budget 140, rested 10 | O 26, S 26, P 34, F 64 |
| rally | 388 : 0 : 0 : 35 | 0 : 388 | budget 115, rested 35 | O 22, S 35, P 31, F 62 |
| audience | 290 : 0 : 0 : 7 | 0 : 290 | budget 143, rested 7 | O 48, S 52, P 16, F 34 |

Conversation (all-mid, n = 300): carried 0.423 (O 61, S 66, P 37, F 136). Negotiation: accepted 50, withdrawn 23,
impasse 227. Invariants over 13,280 beats (and 9,289 in the A-139 run, someone holding both cells in half the
sittings): **0 violations** of: the beats chain; an argued beat names its point; an answer addresses the other
side's point; an item is held and admitted; no conceded issue is re-argued; no barred move; turning away is
charged; only a speaker who decides moves his own track; nobody exceeds the card's turns; the verdicts are the
card's adjudicators; one character is refused; every track equals its start plus the beats.

### B.3 The attributes (carried at 1 against 7; z; then with the operand's own setting off)

**The adjudicator's five (A-144):**

| his | arm | 1 → 7 | off |
|---|---|---|---|
| Reason (validation) | `for` sound but plain (Reason 7, Grace 2), the other polished (Reason 1, Grace 7), in a full trial | 0.060 → 0.760 (z +24.8); the other way round 0.673 → 0.030 | 0.000 |
| | the same two, both arguing consequence only | 0.607 → 0.793 (z +5.1) | 0.000 |
| Focus (the filter) | `for` wanders (Focus 1, a famine) | 0.473 → 0.270 (z -5.3); the other side wanders 0.147 → 0.367 (z +6.4) | 0.000 |
| | theatre alone (the other side presses a Will-2 man; his wandering not counted) | 0.570 → 0.527 (z -1.1): **not shown** | 0.000 |
| Attunement (perception) | a strained liar | 0.673 → 0.270 (z -10.8); a comfortable honest man 0.693 → 0.693; the other side lying 0.190 → 0.593 | 0.000 |
| Presence and station (`awe`) | a Will-2 petitioner before a Presence-7 judge of rung 5: awe 2.26; pressed in a trial he is rattled 2.31 times a sitting and carries 0.500 | a Will-7 peer: awe 0.00, 0.42 rattles, 0.747; the judge flattened: awe 0.26, 0.557; `awe_step` 0: 0.660; before commoner peers awe 0.01 |
| Grace (reception) | table below | |

**Reception: whether the verdict was right, and how it was received** (a rung-5 judge, played; n = 300 each):

| | legitimacy | compliance | appeal weight | the crowd's regard for him | his faction's standing |
|---|---|---|---|---|---|
| accurate, gracious (Grace 7) | +0.02 | 0.83 | 0.17 | +0.05 | -0.03 |
| wrong, gracious | -0.03 | 0.77 | 0.29 | +0.02 | -0.03 |
| accurate, brutish (Grace 1) | -0.47 | 0.00 | 1.17 | -0.23 | -0.23 |
| wrong, brutish | -0.83 | 0.00 | 2.07 | -0.41 | -0.23 |

A simulated judge pays as a played one (accurate, brutish: -0.47, 0.00, 1.17, -0.23, -0.23; n = 171). Control,
Grace 4: -0.23, 0.33, 0.67, -0.10, -0.13.

**The speaker's six** (1 → 7, z):

| | Focus | Reason | Attunement | Presence | Grace | Will |
|---|---|---|---|---|---|---|
| the tell | 0 | +0.420 (12.0) | +0.057 (1.5) | +0.167 (4.4) | +0.173 (5.1) | 0 |
| trial | +0.007 (0.2) | +0.140 (3.6) | +0.110 (2.8) | +0.160 (4.1) | +0.220 (5.9) | +0.130 (3.5) |
| rally | +0.007 (0.2) | +0.143 (3.8) | +0.037 (1.0) | +0.330 (8.8) | +0.057 (1.6) | +0.010 (0.3) |

**Each operand against its own setting off:** Reason's `relevance` own share +0.310 (tell), +0.260 (bench), +0.177
(crowd); and it is magnitude, never sign: a tell on consequence at Reason 1 / 4 / 7 carries 0.288 / 0.642 / 0.857
where the matter helps the listener and 0.027 / 0.113 / 0.352 where it hurts him. Reason's `gap` against a
power-6 respondent 0.063 → 0.427, against 0.153 → 0.427 off. Attunement's `frame` own share +0.093, +0.097,
+0.073 (0.000 with a perfect reading); the frame is the listener's true best in 0.66 / 0.82 / 0.99 of speeches at
Attunement 1 / 4 / 7; the gauge: a perceived-best chooser carries 0.327 / 0.360 / 0.440 in a trial (+0.113, s.e.
0.039; exactly 0.000 with perceived = true); perceived intent correlates +0.45 and +0.97 with the truth. Presence's
`heard` own share +0.153 before a crowd, about +0.01 where there is nobody to be heard over (there it is carried
by its share of the dice, +0.08). Grace's `esteem` +0.077, +0.083, +0.127 (0.000 off). Will's staying power 0.373
→ 0.560 over five turns (0.560 flat off). R11's venue arm: a Reason-7 Presence-2 man against a Presence-7
Reason-2 man on one ground: 0.477 against 0.120 where the venue leans to the case. **The speaker's Focus is
carried only under pull**: 0.000 in these batteries (the critic measured +0.055 pressed every turn in a famine).
A-138: Focus and the speaker's Will are silent at a quiet tell.

### B.4 Silence, temper, the party who decides, the view

| check | reading |
|---|---|
| **silence is not free (A-145)**: the accused in a trial stays silent; `for` carried | crown (`refusal`) 0.400; theocracy (`admits`) 0.415; commune (`free`) 0.300; with the rule off 0.298 to 0.300 in all three. So a regime changes what silence costs: crown against commune +0.100 (n = 600, about 2.5 s.e.); `admits` against `refusal` +0.015, within noise |
| **a broken temper cannot hold its tongue (A-146)**: a debate; `for` presses twice then argues; the other man rests whenever he may (n = 600) | a low man (Will 2, Grace 2): 0.84 of his beats are made with his temper broken and the provoker carries 0.565, against 0.425 with the rule off (+0.140, 2 s.e. 0.053); an ordinary man 0.16 and 0.257 against 0.223 (within noise); a high man (Will 7, Grace 7) never breaks: 0.093 both. **Provoking a man out of his composure now pays against those it can reach** |
| the NPC's temper (A-136) | composed men: the automatic policy is the perceived-best chooser (+0.000); a hot proud man +0.002, a hot timid one about +0.03: the cost of temper lies in the rule above, not in his choices |
| **a party who decides** (n = 600): `for` carried when he argues every turn against rests | the man addressed in a conversation 0.355 against 0.312; the questioned man 0.402 against 0.367; a noble who is the other party 0.248 against 0.273; control, the accused in a trial (not a decider) 0.485 against 0.408. His own speech now moves his own track, so the choice is live; **its effect is within noise in all three, and where it shows it runs against him**, as arguing every turn does for any flat-interior man (F7). Open |
| a noble's stake | start -0.60; the petitioner carries 0.240 against 0.287 flattened; an onlooker holds a `partial` claim; a played noble ruling against his own mind returns a departure of 3.76 |
| the view leaks nothing | each perceived number has its own noise: among poor readers the errors of two options correlate -0.009, an option and the mood -0.079, mood and their point +0.022; `esteem` is perceived (s.d. 0.41 about the truth); resting's worth and `awe` are perceived; the frame has its own normals. No `Present`, track or `terms` |
| odds | the card shows 0.277 before an unmoved bench; 0.263 delivered with both sides silent (n = 600); the abridged menu's chance to land 0.424 against 0.437 delivered |
| refusals | one character; one person as both parties; an abridged act whose only decider is the speaker; a rally with nobody on the floor; a cohort of weight 0; resuming a sitting that ended `yielded`. A two-turn sitting resumed under four turns runs four more beats |

### B.5 Character, context, power, the world

| claim | shipped | control |
|---|---|---|
| fit reads the matter | guild +1.00, toll men -0.50, townsfolk -0.05 | flattened 0.00 |
| a press on what he wants | rattled 0.150 at pursuit 0.1, 0.553 at 0.9 | 0.317, 0.317 |
| sincerity | before an attuned crowd: honest 0.267; a self-serving lie 0.137; an argument on a claim he knows false 0.177; a press with a forged writ 0.047 | `ploy_step` 0: 0.267; 0.267; 0.363; 0.333 |
| a partial judge | 0.490 before the respondent's client, 0.590 before a neutral seat | 0.637, 0.623 |
| credit by tie | +0.80 neutral, +0.30 the respondent's client | +0.80, +0.80 |
| a need | the diplomat accepts 0.247 with none, 0.490 with a need of 0.9 | 0.253, 0.253 |
| each man as himself | in a trial the scholar argues on the proof in 0.26 of his beats and presses 0.34; the orator presses 0.67; the reeve 0.56; with the temper terms off the shares are within 0.04 | |
| strife, regime, era | war 0.433, famine 0.510; theocracy 0.520, commune 0.507; faith 0.507, mercantile 0.557 | 0.527. **Only war moves the outcome**; regime acts through lawfulness, admissible proof and what silence means (B.4) |
| power | fair 0.527; firm 0.483 (tilt 0.47); rigged 0.327 (tilt 0.94, the bench packed, the floor shut, two turns, an appeal) | power flattened 0.577 |
| the fold | 300 trials: `detain` 149, surety 32, acquittals 119, offices contested 79, precedents 268; regard writes up 864, down 3,833; 300 conversations: up 646, down 1,302, grievances 127 | not held: nothing |
| three seasons (160 runs) | the recurring trial carried 0.38 rigged, then 0.46, 0.51; the third season 0.48 after a first-season win (n = 61) and 0.53 after a loss (n = 99): **no snowball**; the rigged trial returned as an appeal in 99 runs; the famine ended at 1.11 (0.50 to 2.00); the scholar's regard for the reeve -0.58 (-1.00 to -0.05); the diplomat's rose in 0.03 of runs (terms accepted 10 of 480): regard still falls far more than it rises | |

---

## C. Transcripts: seed 0 of each rite on the current model (B.2 says how typical each band is)

```
[trial; judged by judge; silence: refusal; 4 turns each]
1. [fact] scholar presses diplomat from what is owed: diplomat holds. (-0.14)
2. [fact] diplomat presses scholar from what is owed: scholar is rattled. (-0.40)
3. [fact] scholar concedes fact. (-0.48)
4. [definition] diplomat presses scholar from what it will bring: scholar holds. (-0.31)
5. [definition] scholar raises point 0 from what is owed (framed on law): it falls flat; he wanders from the point. (-0.65)
6. [definition] diplomat presses scholar from what is owed: scholar is rattled. (-0.71)
7. [definition] (he can hold his tongue no longer) scholar presses diplomat as one of their own: diplomat is rattled. (-1.00)
8. [definition] diplomat rests. (-1.00)
-> budget; judge -5.89; Failure: an acquittal on the case file, a precedent

[negotiation; nobody judges]
1. orator raises point 0 as one of their own: it half lands. (+0.15)
2. diplomat presses orator from what it will bring: orator is rattled. (0.00)
3. orator raises point 1 as one of their own: it lands. (+0.29)
4. diplomat concedes the terms and yields.
-> accepted: an obligation between them

[rally; decided by guildsmen, toll_men, townsfolk]
1. orator raises point 0 from what it will bring (framed on grain): it falls flat. (-0.07)
2. orator raises point 1 as one of their own: it half lands. (-0.04)
3. orator rests. (-0.04)
-> rested; guildsmen -1.34, townsfolk -1.03, toll_men +1.39; Failure

[debate; judged by judge, judge2, judge3]
1-4. each presses the other; both hold.
5. orator presses diplomat from what is owed: diplomat is rattled. (+0.37)
6. diplomat rests. 7. orator presses again: diplomat holds. 8. diplomat presses: orator holds.
-> budget; judge -3.61, judge2 +0.39, judge3 -4.09; Failure: the motion recorded defeated

[questioning; the questioned man decides]
1. fox presses bully from what it will bring: bully holds. (-0.37)
2. bully raises point 0 as one of their own: it lands. (-1.00)
3. fox answers bully's point 0 as one of their own: it half lands. (-0.97)
4. bully raises point 1 from what is owed (framed on faith): it falls flat. (-0.90)
5. fox presses bully from what it will bring: bully is rattled. (-0.60)
6. bully raises point 2 from what it will bring (framed on tolls): it lands. (-1.00)
7. fox answers bully's point 2 as one of their own: it falls flat. (-1.00)
8. bully raises point 3 as one of their own: it falls flat. (-1.00)
-> budget; bully +1.21; Success: he gives it up
```

Read honestly: the trial at seed 0 is a contest of presses, not of proof and refutation, and the debate is almost
all presses. The structure the design promises (point, answer, descent, witness) occurs (218 answers and 67
concessions in 150 trials) but pressing is over-chosen by the automatic policy; that is the open item of B.1.

---

## D. The handshake: each claim, its carrier, the link as run

| # | claim (source) | carried by | reading | verdict |
|---|---|---|---|---|
| T1 | a position holds unless something moves it (A-79, A-137) | the close; the mirrored opposition | D2 | pass, with its residual |
| T2 | a trial turns on proof and refutation at a stasis | the close; `credit`; the answer; `issues` | D1; answers and descents occur | **weak**: pressing crowds them out |
| T3 | the case wins where the venue leans to it (R11) | `k` | 0.477 against 0.120 | pass |
| T4 | going after the man is a real move, bounded | the press; `reactance` | 0.530 / 0.463 / 0.507; control 0.480 / 0.463 / 0.363 | pass on its worth; **not bounded** between flat people (debate) |
| T5 | composure: Will, Grace, Focus (R1) | `weary`, the press's opposition; `esteem`; the hold | Will +0.187; Grace +0.240; Focus only under pull | pass; Focus conditional |
| T6 | the adjudicator validates, filters, perceives (A-144) | `validation`, `wF` and `swayed`, `tell` | B.3 | pass; the theatre half of Focus **not shown** |
| T7 | Attunement gauges his choices and frames his speech (A-141, A-142) | `perceived`, `frame` | +0.113; +0.07 to +0.10 | pass |
| T8 | a man's character is part of his case | `insincerity`, `tell` | B.5 | pass |
| T9 | fit reads the matter, at any Reason | `landing`; `relevance` as magnitude | B.3, B.5 | pass |
| T10 | a judge can be partial and be seen to be | `start`; the `partial` claim | 0.490 against 0.590 | pass |
| T11 | proof is worth what its source is to the hearer | `credit` | +0.80, +0.30; flattened equal | pass |
| T12 | the powerful arrange the forum and pay | `tilt` | 0.527, 0.483, 0.327 | pass |
| T13 | strife, regime and era bear on a sitting | the context rows; the `silence` cell | war -0.094; silence by regime +0.100; standard, era within noise | **in part** |
| T14 | the room is a body for or against a speaker | `mood`, `heat`, `heard` | `heard` +0.153; heat not re-run | pass on `heard` |
| T15 | a need makes a man take terms | `stake` to his accept | 0.247, 0.490 | pass |
| T16 | a loss is a place to go next | the disposal rows | acquittal, precedent, grievance, appeal in 99 of 160 runs | pass |
| T17 | the bearer opens | the order | +0.075 ± 0.054 | an edge has returned; noted |
| T18 | exchanges answer one another (A-129) | `relation`, `Point` | 0 violations | pass |
| T19 | each man argues as himself | the menu on his attributes and bearing | B.5 | pass, weaker than before (pressing dominates most men) |
| T20 | provoking a man out of his composure pays (A-136, A-146) | `temper_break` | +0.140 against a low man; 0 against a high one | **pass where it can reach** |
| T21 | Reason accounts for the other side's circumstances | `gap` | +0.363 against +0.273 off | pass |
| T22 | one character cannot hold a proceeding; a party may decide (A-139) | the invariant; the own-case rule | refusals; both cells in half the sittings; argue against rest within noise | pass on structure; **his choices' effect not shown** |
| T23 | a concession decides something | `yield_track`; the accept | F2 | pass |
| T24-26 | Reason is relevance; Presence is being heard; Grace is conduct (A-143) | `relevance`, `heard`, `esteem` | B.3 | pass |
| T27 | an adjudicator of station cows a man of less Will (A-144) | `awe` | B.3 | pass |
| T28 | a verdict's reception is apart from its rightness; a brute's is resented (A-144) | the fold's reception | the 2 x 2 | pass |
| T29 | silence is never free where a point must be answered (A-145) | `silence_cost`; the `silence` cell | 0.400 against 0.298 | pass for the charged side; **speaking still does not beat silence for the side not charged** |

**Totals: 31 claims (T24-26 are three); 22 pass; 5 pass in part or conditionally (T5, T6, T13, T22, T29); 2 weak
(T2, T19); 1 unbounded (T4's second half); 1 with an edge returned (T17).** What failed in this pass and changed
the design: an obstacle of awe on every speech (speaking then lost before any bench: now it acts on staying power
and on a press); relevance as a multiplier of signed bearing (wrong sign for a hostile listener: now additive
magnitude); a party-decider's own speech moving nobody who decides (now his own track); a raise's whole shortfall
counting against it (now a share, and its worth counts the answer it invites); every reception docketing an appeal
(now a weight); four leaks in the view; two crashes.
