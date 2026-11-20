# SC — the social contest redesigned, v2, part 2: the design

## Status: PROPOSED (the second part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first: its status, markers and binding list apply here; reference under CLAUDE.md §0.05, nothing reads it at runtime)

Reconciled 2026-11-15 after two antagonist passes and Jordan's rulings A-136 to A-140; fixed a second time
2026-11-16 after the premise-check (part 4 §K is the one table of what changed and why). Conventions: `mid` 4,
`floor` 1, `ceiling` 7 on the attribute scale; `pool_of`, `opposed_ob`, `even_line`, `net_boost` (soft cap),
`roll_net_continuous`, `level` are `engine/dice_engine/sigma_leverage.py`'s; `even = even_line(pool_add)`. Pools
are fractional, obstacles real (R8). Every formula is the model's (`sc2/engine.py`, `sc2/host.py`), stated once;
model and text were made to agree line by line in this pass.

---

## A. The person in the room

### A.1 One record; a sitting needs two characters

```python
@dataclass(frozen=True)
class Present:                 # everyone: participant, adjudicator, audience
    id: str; weight: int       # a cohort is a person at weight above one
    side: Optional[str]        # "for" | "against" | None        } the role is
    decides: bool              # he ADJUDICATES                  } these two cells
    focus: float; reason: float; attunement: float; presence: float; grace: float; will: float
    rank: float                # his rank in the proceeding's skill
    care: tuple                # (want, hold, bond) in 0..1: how much each kind of thing moves him
    stake: tuple               # (want, hold, bond) in -1..1: how THIS matter bears on him, toward `for`
    bonds: tuple               # ((other person, -1..1), ...)
    start: float               # where his track starts (host: start_step x mean(stake), plus the arrangement)
    holds: tuple               # ((channel, tag, weight, how the matter bears on it), ...): his wants and convictions, tag by tag
    believes: float            # what he KNOWS of the matter, -1..1 toward `for` (his own ledger)
    bias: float                # his stable misjudgement of what his options are worth: -1 pessimist .. +1 optimist
    power: float; precedence: int   # his circumstances: seat, office, wealth, influence, faction (host)
    items: tuple; strain: float
```

**One invariant (A-139, as corrected): a sitting has at least two distinct characters; a proceeding with one
character in every role is refused.** `side` and `decides` are independent cells: a noble who speaks with a
petitioner and then decides, an inquisitor who questions and judges, a questioned man who decides whether to give
way, a seat who speaks in debate and votes each hold both. A party who decides is not forbidden; he is *partial*,
by the same reading as anyone: his stake and ties set where his track starts, the room holds a `partial` claim,
and a ruling against his own track is deposited. Consent is still not adjudication: under `close: consent` nobody
decides and the outcome is a party's accept. Everyone in the room has a track; `decides` only says whose
is drawn at the close. A role changes inside a sitting by one rule: **a cited testimony whose source sits in the
room with no side and no seat is spoken by its source**, with his own dice, standing and sincerity; the other side
may press him next; his cells are unchanged after.

### A.2 The bearing reading: one derivation

`bearing(person, referent) -> (want, hold, bond)`, signed, from the person's **own interior only**, the same
whatever his role:

```
want = clip( sum over tags the referent bears on: (pursuit[t] + need[t] + 0.5 [goal] + 0.5 [ambition]) x bears[t] )
hold = clip( sum: conviction[t] / scale_max x bears[t] + office.duty[t] x bears[t] )
bond = clip( tie(for-party) - tie(against-party) + faction_stance[his faction] + 0.3 [a party shares his faction] )
tie(q) = clip( relationship[q] + 0.5 [kin] + 0.5 [patron or client] + debt[q] )
care = ( strongest pursuit or need, strongest conviction / scale_max, strongest |relationship| )   # 0.5 where none
```

| read as | formula |
|---|---|
| his **stake** (whether he comes, which side, how hard) and his **start** (partiality) | `stake = bearing(p, matter)`; `start = start_step x mean(stake)`; **which side** a man not named by the matter takes is the sign of `mean(stake)` and **how hard** (`effort`, the turns he prepares) is `round(3 abs(mean(stake)) + 1)`, 0 where nothing bears (D4: `takes_side`, `effort_of`; where a rite has an opposing side and the matter names no one to it, the most opposed man on the floor comes to oppose). **A party's stake is at least `PARTY_STAKE` (0.2) toward his own side** (his bond raised as far as it goes: being a party is a stake, A-139, B6; the season driver's literal, moved to the bearing, its one owner); `effort` reads what the matter touches of his own beyond being a party (p4 §L 2) |
| a decider's **conflict** (partiality) | `conflict = (abs(want) + abs(duty) + max(abs(bond), abs(tie to one party) + abs(tie to the other))) / 3`, `lean = (want + duty + bond) / 3`: partiality is his PERSONS (relationship, kin, patronage, debts, being a party; a shared faction is not partiality, it moves how he hears: p4 §L R1) and his WANT in the matter (pursuits, needs, goals, ambitions, his office's duty where it names what the matter bears on); **a conviction is not partiality** (it moves how he hears, A-131; p4 §L 19: a judge who holds by the law was priced as partial in a third of trials). Interests and ties on both sides are a conflict, never a cancellation (B6; A5: kin to both parties is a conflict as kin to one is; patronage is one record read from either man). A non-party seat whose conflict reaches `recuse_at` steps down where another seat of the authority can sit; one who cannot sits, and a party who holds a seat sits by choice (A-139: the inquisitor who accuses and judges, the seat who speaks and votes), the room holds a `partial` claim, and a ruling his own way is priced (§J) |
| the **fit** of an argument to him | it reads the MATTER, at the **frame** the speaker chose (one pursuit, need or goal of his for `consequence`; one conviction or duty for `authority`): `landing = clip(side x weight[tag] x bears[tag] + 0.5 x (2 weight[tag] - 1))`, and -0.5 for a frame he does not hold at all (the SIGN is what the matter does to him; relevance adds magnitude in C.2, never sign); `clip(bond(him, speaker) + 0.5 x (2 care.bond - 1))` for `solidarity`; `credit(him, item)` for `evidence` |
| the **aim** of a press on him | a press names its **object**, the held thing it hits (chosen from the presser's believed reading of him, as a frame is): `aim = clip(weight[tag] x (1 + abs(bears[tag])) - 1)`, -1 for a thing he does not hold: it bites by how much he holds it AND how far THIS matter bears on it, either way (B7; unsigned, so never the same number as the fit); on `solidarity` his bond in the matter; on `evidence`, what the item shows of him or of one he is bound to |
| **credit** of an item | `clip(2 weight - 1 + bond(him, source) - max(0, bond(him, the one implicated)))` |
| **sincerity** | `insincerity = max( -side x believes, 1 if the item is one he knows false, -side x stake.hold on the ground of authority )`, clipped to 0..1: agreement between what he says and what he **knows**, and on the ground of what is owed, what he **holds**. Arguing against his own interest is not insincere (B2: word against behaviour is not a lie); a self-serving lie is insincere through `believes` though it runs with his stake |
| the **cost of conceding** an issue | `concede_step x (1 + max abs(stake))`, from where he stands (C.5) |
| his **intent**, as the other side reads it | the mean of his stake, blurred, in the other's `View` |
| the **verdict's effect** | the fold: his pursuits move by `outcome x abs(stake)` |

So a consequence argument for remitting the tolls fits the guild and misfits the toll men, who lose by it.

### A.3 Which layers exist today

| layer | carrier | status |
|---|---|---|
| pursuits, convictions | `Person.pursuits`, `.conviction` (`state/carriers.py`); `data/affiliations.py` | exist |
| goals | `data/goals.py`; `rosters.yaml: goal_object_kinds` | exist |
| what he knows | his ledger of `Claim`s; `person_q.said_of`, `lie_said_of` | exist: `believes` is read from them |
| a false item (B2, D6) | his OWN FALSE WORD: where `believes` runs against the side he speaks for, the builder offers him his own assertion of the contrary as `testimony` he knows false (`false_items`); a forgery is a `Record` its maker knows false | the word: exists (read from his ledger); forging: `[HOOK]` an act that writes such a `Record` (fixture data in the model). Nothing else makes a false item |
| relationships, regard | `Person.stance`; `person_q.stance_toward`, `regard` | exist |
| obligations, debts | `Tenure` of kind `oblige` | exist |
| office, seat, faction | `Office`, `hold` Tenures, `world_q.judging_set`, `rosters.yaml: factions` | exist |
| era, strife | `world_q.open_era`; `rosters.yaml: strife_kinds` | exist |
| needs, ambitions, arcs, kin edges, patronage, wealth, regime | none found | `[HOOK]`: one more term in the reading's sums, in `power`, or a key of the context table `[UNVERIFIED: the 2026-10-24 character-layer and 30_WR proposals were not opened]` |

### A.4 What he carries in

`strain_carried(p) = 0.5 x sum over his rattles this season, freshest first, of max(0, 1 - strain_fade x scenes
since that rattle) / 2^k`: bounded under 1.0; a derived read of his own acts' endings.

---

## B. The rite: the type's cells

```python
@dataclass(frozen=True)
class Rite:
    id: str
    live: str; bears: str   # what the live thing is called (claim, offer, question, charge, motion, theme, plea); who bears it: he opens
    reply: tuple            # per side: must | may | raise
    silence: str            # what not answering a standing point means here: admits | refusal | free (A-145)
    issues: tuple           # the stasis rungs it runs through (B24.03's `issue_rungs`)
    weighs: tuple           # stasis: what each rung is argued from ((issue, ((ground, weight), ...)), ...)
    concede: str            # descends | accepts
    moves: tuple            # per side, of: argue, press, rest, concede
    close: str              # bench | declared | hearers | consent | exchange (the abridged form)
    turns: int; standard: float; reason_lean: float; admits: tuple
    difficulty: float; gravity: float; quorum: Optional[int]; unrest: float
```

The module reads these cells and compares no row, move or person id (a move is read by its `effect`: `track`,
`strike`, `yield`, `none`). The eight rows are part 1 §D. `abridged(row)` is any row with one turn, the one move
`argue` for the bearer, `close: exchange`, and the one addressed present as a hearer who decides (it needs no bench,
B3). **`gravity`** (renamed from `stakes`, B19: the word meant a burden on the bearer, not what is won or lost) is how
grave the times make a change: an obstacle on the bearer at the close, set by strife and by the regime. **`weighs`** is the stasis
table (A-134; part 1's handshake): `fact` is argued from the proof (evidence 1.25, consequence and solidarity 0.75),
`definition` from what is owed (authority 1.25, consequence 0.75), `justification` from what it brings and who
stands with whom (consequence and solidarity 1.25, evidence 0.75); a rung it does not name weighs every ground
alike. It multiplies the era's weight on the ground (`_weight`), and it is what makes descending a rung a real
choice (C.5). `quorum` is read by a `declared` close: the quorum-th best seat's margin is the verdict (§D).

---

## C. The exchange

### C.1 The value, the order, the beat

```python
Sitting(n, issue, points, live, tracks, cond, used, last_voice, ended)
Point(id, side, issue, ground, item, by, held)        # held: how far it stands with each listener
Cond(rattles, strain, heat, spoken, spent)             # one per person; `heat` is this sitting's provocation (F)
Beat(n, mover, voice, side, move, relation, issue, ground, item, point, target, margin, drift,
     evaded, left, insincere, caught, rattled, frame, relevance, heard, esteem, broke, moved, closed, mood, terms)
```

`evaded` marks a beat that was PRICED (a point he must answer left standing, or a matter he bears not put);
`left` names the other side's point that stood against him and that he did not answer, in any rite, priced or
not (C5: an ignored point is never unmarked); `caught` names those whose reading of him turned a speech he did not
hold (B2); `frame` is the frame of an argument or the object of a press.

- **Order and turns.** The bearer opens, the rest by precedence. Each speaker has the rite's `turns`; a resumed
  sitting gives him the turns less what `cond.spoken` says he has had, the beats continue their count, the issue
  reached stands, and a sitting that ended `yielded` is not resumed (an adjourned one is). A resume continues THE
  SAME sitting: the same people with a turn left; anything else is refused, keyed (`room_changed`,
  `abridged_resume`, `spent`, and `closed` for a sitting that ended `rested`: a close once drawn on what was said is
  not drawn again; p4 §L 1, R2).
- **One live point a side.** A raise makes the mover's point live; older points stay in the record.
- **A track** is each person's own: `track[h] = h.start + the sum of the beats' moves on h` (asserted). `tracks`
  is kept in `Sitting` as that running value so a resume needs no replay; it is never a verdict.
- **The beat** is the narrative record (no text field); `terms` (true values) is in the outcome only. The record
  names the room's stance in five bands of its mood (firmly with one side, leaning, hanging) and names it only at the
  beat that turns it; the clamped number is never shown (p4 §L 20).

### C.2 The speech: one draw, one margin per listener

A fixed **6G + 11** normals an exchange, stated once in the model (`DRAWS_PER_EXCHANGE`) and asserted on every
exchange: his accuracy; per ground one for what arguing on it is worth to him, one for pressing on it, two for the
frame, two for the press's object; conceding; resting; the mood; their point; his own point; the other's intent;
his esteem; his awe; the hold; the speech; each perceived number its own. For voice `V`, side `s`, ground `g`, item
`i`, heard by `h` (everyone not on the speaking side, and the speaker himself where he decides: below):

```
k        = clamp(content[g] + rite.reason_lean - crowd_lean x crowd, 0, 1)                  # R11: content AND venue
pool     = heard(V) x pool_of(weighted_tenth((V.reason, V.presence), (k, 1-k)) + V.rank)
heard(V) = own(V) / max(own(V), own(the man opposite))   (own(V) alone with nobody opposite) # Presence, against the man opposite
own(V)   = clamp(1 - heard_step x max(0, (1 + 6 x crowd) - V.presence), heard_floor, 1)
relevance(V) = 2 (V.reason - floor) / (ceiling - floor)                                      # Reason: content to the point; 1 at mid
sound_h  = 1 + 2 validation(h) x (relevance(V) - 1)                                          # A-144: what of its soundness HE can tell
sigma_h  = level(fit_level) x era[g] x weighs[rung][g] x (fit(h, V, s, g, i, frame) + rel_gain x (sound_h - 1) - repeat_step x uses)
         + esteem_step x esteem(V) x 2 (1 - validation(h))                                   # Grace; standing weighs less with one who can validate
         + sound_h x level(answer_level)  if the speech answers what stands
ob_h     = even + opposed_ob(h.will + h.rank) + weary(V) + gap(V)  [+ difficulty + gravity in the abridged form]
margin_h = roll_net_continuous(pool) + net_boost(sigma_h, pool) - ob_h
         - off_step x wF(h) x off  -  ploy_step x wA(h) x insincerity(V)                     # A-144 Focus, Attunement
awe(V)   = awe_step x mean over those who decide of max(0, (d.presence - mid)/3 + (d.power - V.power)/power_scale - (V.will - mid)/3)
esteem(V) = short(the man opposite) - short(V);  short(p) = max(0, rite.standard + show x p.rattles - p.grace)
weary(V)  = weary_step x max(0, V.spent - (stay_base + stay_per_will x V.will - awe(V)))     # Will: keep arguing; the bench's awe shortens it
gap(V)    = gap_step x max(0, power(the other side) - power(V)) x (1 - (V.reason - floor) / (ceiling - floor))   # Reason: accounts for it
            # the other side: its lead; in an abridged act the one addressed; nobody opposite, no gap (p4 §L 15)
```

- **The opposition (A-137)** is the listener's `will + rank` at 0.4 a point: the resisting attribute counts as the
  mirror of the attribute in the pool. At control the abridged margin is that one roll (200 of 200 keys).
- **Presence is relative to the man opposite (C1).** A crowd that hears a Presence-4 man at 0.85 of his pool used
  to cut every speaker's pool and none of the obstacles, so before any gallery every speech between equals lost on
  average and silence beat speaking. Now the better heard of the two is heard whole and the other by his share; a
  lone voice (a rally, a witness) keeps his own share of what the crowd demands. Esteem is relative the same way.
- **Esteem** is his standing in the room this sitting: how much better he meets what the occasion, and his own
  rattles, ask than the man opposite does. It is relative, so the standard prices a shortfall against the other
  side and does not tilt the room against whoever speaks; with nobody opposite it is his own shortfall. Derived
  each exchange, never stored on a person (S-7).
- **The other side's circumstances** (`power`: his seat's rung, his office's modifier, the regime's weight for
  his authority; wealth and influence as `[HOOK]` terms) stand against a speaker as an obstacle unless his Reason
  accounts for them. This is the home of B28.10's *relative rung of the teller's seat* and B28.34 and B28.35's
  hearer terms. With nobody opposite, the weightiest of those who decide is who he must account for.
- **A raise** that lands adds `s x margin_h` to each listener's track and puts a point on the table; one that
  falls flat costs `flop` of its shortfall (a point not made is not a point for the other side). **An answer**
  only undoes the other side's live point, and is **bounded both ways by how far that point stands with the
  listener** `s`: `min(s, margin)` when it lands, `flop x min(s, shortfall)` when it fails (a failed answer
  confirms the point, it does not make a new one). An answer is offered only to a point that stands; with a
  listener with whom it does not stand it moves nothing (C1, C5: before, a flop had no cap and an answer to a dead
  point could only lose). **A party who decides is moved by his own case too (C2):** his own speech, press and
  concession move his own track, heard **by himself**: his own Reason validates it and his own Will resists it,
  exactly as for any listener (A-144: the validating Reason is the adjudicator's). The other side's speeches are
  what move him from outside. Before, his own speech was measured on the other side's lead as its listener, which
  inverted Reason (a sound speaker lost against a sound-but-plain deciding party). **Silence is never free
  (A-145):** under `reply: must`, while their point stands, a side that rests or turns to anything but an answer or
  a concession is charged with each listener `silence_cost = contempt_step x (standard / mid) x (1 + his station /
  4, if he decides)` (refusal to engage: a disrespect that grows with the occasion and with whom he declines to
  answer), plus, where the rite's `silence` cell is `admits`, `admit_step x` how far the point stands with that
  listener (tacit admission); `free` charges nothing, and **a rite whose reply is `must` is never `free`**: no regime
  sets it so (the commune's `free` cell was cut, p4 §L 6: it acted only where an answer is owed, against A-145); a
  commune's lower `standard` makes silence cheaper there, never nothing. A man is not contemptuous of himself, but he is not alone: a party who
  decides and leaves a point owed an answer standing answers in his own ruling to the contempt of those present, at
  the floor (`contempt_step x standard / mid`), plus the admission (p4 §L R5: the questioned man rested for nothing). **The burden (C1; the same rule):** the bearer of a matter the other
  side must answer has to put it: while no point of his stands, his rest, or a press in place of a point, is a
  charge not pressed (a question not asked) and is priced as silence is, contempt only. So **an unargued charge
  lapses**: the card says so (`unargued`), and a trial where nobody speaks goes against the bearer instead of
  convicting at the bench's unmoved odds. **Staleness:** each earlier use of a ground or item costs `repeat_step`.
- **Drift (B14).** `pull = press_pull x heat + rattle_pull x rattles + unrest + heckle x max(0, heat of the room)`;
  `drift = max(0, pull - max(0, roll_net_continuous(pool_of(V.focus)) - even))`; `off = drift`. Continuous in the
  pull: at no pull no drift, and a weak hold is a hold of 0, never a push (before, a pull of 0.0001 gave a drift of
  0.67 at Focus 1).
- **Against his grain.** `strain += grain_strain x insincerity`.

### C.3 The adjudicator's five (A-144, later than R12 and governing; a listener who does not decide reads the first three the same way)

| his | Jordan's words | the one operand |
|---|---|---|
| Reason: **validation** | *"how well the person can understand and dissect a participant's argument/speech, ie the ability to validate whether it is coherent and sound and good"* | `validation = clamp(0.5 + sense_step (reason - mid) + involve x maxabs(stake) - crowd_lean x crowd, 0, 1)`: the share of a speech's true soundness (its speaker's `relevance`) that reaches his judgement (`sound_h`), the rest of his judgement falling on the speaker's standing (`esteem x 2 (1 - validation)`). A polished unsound speech takes in a judge who cannot validate and not one who can. It replaced the weighting by ground class (`q`), which is deleted |
| Focus: **the relevance filter** | *"not being distracted or misled by participants' acts ... only hold relevant information ... not being swayed by irrelevant things"* | `wF = (focus - floor)/(mid - floor)`, 0 to 2: he deducts what is off the point (drift) by `wF`; and **the theatre filter** `theatre = max(0, 2 - wF)`: a rattle proves nothing about the merits, so its move on the room reaches him at twice its weight at Focus 1, at its weight at the middle, not at all at Focus 7. The first fix pass cut this half (it then read no slope); it carries the clause's *not swayed by irrelevant things* alone, so it is **restored** (A-140: a ruled clause may not lose its only carrier; `discern` reads the rattled man, not the irrelevance). It multiplies the rattle's move with `discern`; a failed press's rebound is not theatre (it shows the presser's case) |
| Attunement: **perception of the participant** | *"perceive the comfort/discomfort and sincerity/insincerity and so forth of a participant"* | `wA = (attunement - floor)/(mid - floor)`. **Insincerity** is deducted as a ploy: `ploy_step x wA x insincerity` (R12). **Discomfort is never read as insincerity** (B10: a strained honest man was marked down by an attuned judge): it is perceived by its own signed rule, `discern = 1 + comfort_step x (wA - 1) x (2 x his case's falsity - 1)`, which scales how far a rattle moves this listener: an attuned listener discounts an honest man's nerves and reads a false man's as guilt; a dull one the other way; 1 at the middle. A played adjudicator is shown each participant's perceived insincerity and discomfort, scaled by his own Attunement |
| Presence and seat: **intimidation** | *"how intimidating they are to the participants and consequently how confident and composed the participants are"* | `awe`: it acts on the PARTICIPANT's confidence and composure, by how far the adjudicators' Presence and station exceed his own station and Will: his staying power is shorter by it (he tires sooner) and a press on him meets less (he is easier to rattle). It is not an obstacle on his speeches (a first build made it one, and speaking before any bench then moved the room toward the other side: F7 again; changed in this pass). Distinct from `gap` (the other SIDE's circumstances, answered by Reason) |
| Grace: **reception** | *"how well their decisions are received by audience and in game world"*; *"an otherwise perfect adjudicator who has little grace will have their verdicts seen as those of a brute whose station outstrips their respectability"* | in the fold, not in the sitting, and only for a RULING (a `bench` or `declared` close; never a tell, a rally or a party's own decision, B3): `brute = max(0, clip(power, floor, ceiling) - grace) / (ceiling - floor)`, station and respectability on ONE scale, the attribute scale (his power counts a rung a point, as `power` does: a mid judge of a mid seat, Grace 4 at rung 3 under a crown, is no brute; Grace 1 at the highest seat wholly one; monotone in rung, modifier and Grace; p4 §L 14: the old `tanh` station saturated at any office); `reception = 1 - brute`. **Decided (rung 3, A-144(6)'s words "little grace")**: a Grace-7 judge is never a brute whatever his station (before, a duke of Grace 7 was resented); respectability above station earns nothing further (it has no object in the ruling). Whether the verdict was right and how it is received are two axes (§J) |
| Will | (R1; A-137) | **not one of A-144's five** (B13, decided, rung 1: A-137 "keep 0.4" makes it the resisting attribute): the opposition to whatever is aimed at him, as a listener of an argument and as the man pressed. A-144's five are the adjudicator's JUDGING operands; Will is how hard he is to move |

No draw is taken for any of them. **Decided (rung 5):** the ploy is carried by `insincerity` on `argue` and `press`;
`deceive` and `divert` are not restored (a lie is an argument its speaker knows false, its item his own false
claim; being pulled off the point is what a landed press and a heckling room do, and turning away prices it).

### C.4 The press and the rattle

**A press lies only where something stands against the man pressed** (p4 §L 18): a live point of his own that
stands, or a charge laid on him (his side is not the bearer's and must answer). A man who has said nothing and is
charged with nothing is not cross-examined: the option is not on the menu.

```
sigma  = level(fit_level) x era[g] x weighs[rung][g] x aim(T, g, i, object) + room_level x heat(T) + esteem_step x esteem(V)
ob     = even + opposed_ob(max(0, T.will + T.rank - (T.strain + awe(T)) / 0.4)) + weary(V) + gap(V) + press_ob
margin = roll_net_continuous(pool) + net_boost(sigma, pool) - ob
landed (margin >= 0):  T.rattles += 1, T.strain = 0, T.heat += 1, T.spent += 1;
                       each listener moves rattle_gain x (1 - reactance x T's earlier rattles) x discern(h, T) x theatre(h) x (1 - max(0, bond(h, T)))
failed:                T.strain += wear; each listener moves `rebound` against the presser
either:                less off_step x wF(h) x off, less ploy_step x wA(h) if it was made with a forged item
```

A rattle is the one discrete event and is decided by a draw. It moves the room at once (less with each repeat,
then against the presser), as each listener reads the man's discomfort (`discern`) and as far as his Focus lets
theatre reach him (`theatre`); it lowers his esteem on every
later speech (`show`, which Grace's headroom absorbs: B16, surplus Grace is composure where he is pressed); it adds
to his heat, which pulls his next speeches (Focus) and is what his temper reads (F); it spends his staying power
(Will); it is witnessed. Nothing forces him to stop. **A press names its object** (A.2's aim): the beat records it
(`frame`), and a press on a thing the matter does not touch, or that he does not hold, barely bites. A press made
by the bearer while no point of his stands is a charge not pressed (C.2's burden).

### C.5 Conceding, resting, ending

- **Concede an issue** (`descends`, a rung remains): each listener's track moves `-side x concede_step x (1 +
  max|stake|)` **from where it stands** (C5: it used to be reset to his start, which improved the conceder's
  standing in 76 to 79 % of concessions); the issue's points stay on the record, conceded; the mover's grounds are
  fresh; the next rung opens, and with it the bearer's burden again. What descending buys is the next rung's
  ground (`weighs`): the menu prices it as the gain of the best raise there over the best raise here, for the
  turns left, less the cost.
- **Concede the matter** (the last rung, or `accepts`): the sitting ends `yielded`. Who yields decides what it is
  (one rule, `act_band`): under `consent` it is the accept; **the bearer who yields drops the matter** (nothing is
  left to decide: Failure); **a party who decides and yields gives way** (his own accept: Success for the other
  side) **where his verdict alone is the close** (one seat, one vote: on a close other seats share, his yield is priced
  and treated as any party's, p4 §L 2); anyone else gives the matter up before those who decide, every listener's track going to `-side x M_MAX /
  track_step` (as far as the close's leverage can carry it: `yield_track` is cut), and the bench still draws: a
  confession is not a verdict (A-14) but it is decisive (part 3 §B).
- **Rest**: tempo only, except as C.2's silence rule and the burden price it. **A broken temper cannot hold its
  tongue (A-146):** when `temper >= temper_break` (F), `rest` is not among his legal moves, player or NPC, a party
  who decides included; the view says so (`broke`), the beat is marked, and the fold leaves one claim per witness
  per sitting. A legality rule on one existing quantity; it resolves nothing.
- **Ends**: `budget`, `rested`, `yielded`. **"Those who decide are ready" (D5, decided, rung 5):** the forum's time
  is the measure of readiness: the turns it gives are spent, a whole round has nothing more to say, or a side
  yields. No second rule reads the deciders' state to close early (it would add a threshold and an end for no
  decision a player makes); the card says when it closes (`ends`).

### C.6 The division of labour on a speech (A-143, A-141, A-142; R1 for Focus and Will)

Jordan: *"reason informs the relevancy of contents and stakes of the speech in a logical manner / attunement allows
one to modulate and frame it in a way that appeals to the other's pursuits ethics personality / presence allows one
to be heard as assured and convincing / grace allows one to behave in a manner that is befitting the occasion and
thus be respectable"*. Four operands on one speech, each written on the beat (`relevance`, `frame`, `heard`,
`esteem`); two speakers who differ in one of the four differ on that field alone (part 3 §B).

| attribute | what it is | its operand | beside it (R1, R11) |
|---|---|---|---|
| **Reason**: the CONTENT | how relevant what he says is to the live point and to the stakes that bear on those who decide | `relevance` (0 to 2, 1 at the middle): it scales how far the matter's bearing on the listener is brought home in the fit, and the worth of an answer to the point on the table. Apart from Focus (not being pulled off the point) and from Attunement (how it is framed) | its share `k` of the dice (R11); `gap`: accounting for the other side's circumstances (R1) |
| **Attunement**: the FRAMING, and the gauge | how the content is aimed at what THIS listener wants and holds, and how well he judges what his own choices are worth | `frame(view, listeners)`: he picks, from his believed reading, the one thing of theirs to frame the ground on; the fit lands on their true interior at that frame. A body has one frame, so a split room dilutes it. And `perceived(true worth, accuracy, his noise, his bias)`: every worth on his view (A-141). One reading: `acc = (1 + tanh((0.4 (attunement - mid) + read_noise x z) / read_scale)) / 2`; nothing opposes it (rung 5: Grace has its own operand). Personality has no carrier in the tree: `[HOOK]`, a third kind of tag in `holds` | its believed mood, points and the other's intent |
| **Presence**: the DELIVERY | being heard as assured and convincing: how he lands on others (Will is his own inner staying power) | `heard`: the share of him the room listens to | its share `1 - k` of the dice |
| **Grace**: the CONDUCT | behaving as befits the occasion and so being respectable | `esteem`: how much better he meets the venue's standard, and his own rattles, than the man opposite | |
| Focus | *"staying on topic, not being pulled away"* | the hold (`drift`): **decided (B14, rung 3, R1's own words "not being pulled away")**: it acts where something pulls (the times' `unrest`, which the card shows; a heckling room; his own heat after a rattle) and is silent where nothing does; its outcome slope is modest and is stated in part 3, never inflated | |
| Will | *"keep arguing ... believe in yourself ... not get rattled"* | `weary`; the opposition to a press and, as a listener, to an argument; with Grace, what his temper is measured against (F). **Decided (B15, rung 4, A-138's precedent):** at a rally (no opponent to rattle him) it acts only through staying power, which a rally's three turns rarely reach, so it is silent there as at the tell; its C2-route effect in conversation is gone with the C2 fix | |

**The frame is automatic from the ground** (rung: A-130, game first: a second choice an exchange was refused); the
option shows it (`Option.frame`) with its perceived worth, so a mis-frame is a risk he can see only as well as he
reads. It replaced the per-ground believed fit and aim that the view used to carry, and the believed strain. A-138:
at a quiet tell Focus and the speaker's Will have no object; Attunement now acts there through the frame.

---

## D. The close

```
drawn (bench, declared, hearers): for each adjudicator, one normal:
    margin = roll_net_continuous(pool_of(mid)) + net_boost(track_step x track[d], pool)
             - (even + opposed_ob(mid) + rite.difficulty + rite.gravity)
consent:   nobody adjudicates and nothing is drawn; a party's accept is Success for the bearer, the bearer's
           withdrawal is Failure, neither is an impasse (no band). Kept for `negotiation` ON THE MERITS (rung 3:
           the NEG falsifier, "consent decided by a draw"; an obligation is each party's own act)
exchange:  the one speech's margin with the one addressed, plus his start
```

The host reads the verdicts (`act_band`): `bench` the presiding seat's; `declared` **the quorum-th best seat's
margin**, so a majority carries and the presiding seat is one vote (C5: the presiding seat used to decide and the
others could only demote; the veto step is deleted); `hearers` the weight-mean; a yield as C.5 says. Never the
actor's last exchange.
**Decided on the merits, now that a party may decide.** `conversation`: the man addressed is a side and the
adjudicator; his draw gives the act a band every time (A-14; the fold's pursuit shift needs a degree), and his
concession is giving way early (rung 1, rung 4: the 11-14 design's `hearers`). `questioning`: the questioned man
decides whether to give way (Jordan's own example, rung 3); what is then done with what he gave is `determine`'s
separate step. `audience`: where the seat is the other party he speaks, presses and then decides (Jordan's
example). `inquisition`: the accuser may sit. **A party who decides is moved by his own case as he hears it and by
the other side's from outside** (C.2), and a final concession by him is his giving way (C.5). **A played
adjudicator** is a role: at the close he has `JudgeView(id, track, odds, points, tells)` (his own mind, which he
knows; the points as they stood; what his Attunement perceives of each participant's insincerity and discomfort)
and three choices: rule for, rule against, or leave it to his draw; how far a ruling departs from his own track is
returned (`Outcome.ruled`) and deposited as a claim with everyone present. **Decided (D7, rung: A-130 game first,
and rung 5):** a played adjudicator rules at the close only; he asks nothing during the sitting. A bench move would
be a second interface for one role (shape divergence) and no row asks for it; a judge who must question is a party
who also decides (A-139), and that case exists (the inquisitor).

---

## E. Played: the view, the choices, the pace

```python
@dataclass(frozen=True)
class View:                       # own values true; everything else perceived, each with its own noise, or public
    n: int; mover: str; side: str; issue: str; turns_left: int
    live_theirs: Optional[tuple]; live_own: Optional[tuple]     # (point, ground, item, perceived strength)
    options: tuple                # Option(move, ground, item, relation, ev, p, frame): perceived worth and chance
    own: Cond; esteem: float; weary: float; awe: float          # his standing, his weariness, how far the bench cows him
    visible: tuple                # each speaker's rattles
    mood: float; odds: float      # the room as he reads it; P(carried) on that reading before an ordinary bench
    intent: float                 # the perceived stake of the man opposite
    acc: float
    burden: bool                  # he bears the matter and no point of his stands: resting is a charge not pressed
```

`menu(inp, state, mover)` computes each option's expected worth from the engine's own values, with **each listener
read as he believes him** (B11: his judging operands and his Will drawn toward the middle of the scale by what his
accuracy does not reach; a stranger is an ordinary man, B05.62): so a liar is deterred by a judge's Attunement only
as far as he can read it. A raise's worth is less the share `invite` of its gain that the answer it invites will
undo; an answer's is bounded both ways by how far the point stands; a press's counts what a rattle goes on doing
(`_lasting`: his standing falls only as far as his Grace lacks headroom, he tires only past his staying power, his
next speech is pulled); conceding an issue counts the next rung's ground; resting counts what silence and the
burden charge. The worth of resting, his esteem and his awe are perceived like the rest; `perceived(true, acc, x,
lean) = true + (1 - acc) x (read_blur x x + bias_step x lean)` is the one function through which every worth
reaches a view, and the automatic policy chooses on the same numbers. At `acc` 1 perceived is true; a pessimist
underrates acting, an optimist overrates it. A field for the move he expects of the man opposite was built and
**cut**: its hit rate (0.35 to 0.37, measured when it was cut in the first reconciliation) was under always guessing
his commonest move.

- **Honest and not omniscient.** `odds` and every option's worth are computed from his believed values and an
  ordinary stranger (B05.62), never from a true attribute or a true start. The card's `odds` is THE CLOSE ITSELF
  where nobody speaks (`close_odds`: each who decides at his own start, the rig's presumption and the packed bench
  included, less the unput charge; `declared` the chance that a quorum of the seats' own draws carry; `hearers` the
  weight-mean; p4 §L 7), and is `None` where nothing is drawn (consent) or the verdict is the speech itself.
- **What he chooses, per exchange:** raise a point (three grounds, or the proof with an item he holds), answer
  theirs (only while it stands), press the man (on the object his reading picks), concede, rest: 4 to 12 options
  by rite and side. **Before:** whether to come, what and whom to bring, his effort (turns), and with power how
  hard to rig the forum (§H); without it, the weak party's acts `before()`: accept the forum, or take it elsewhere
  where another authority sits (a fair forum next season). (`contest` was cut: in no case measured was it his best
  act, §F 42.) **After** (`after()`, D3):
  accept (the disposal holds; how galling it is reads `compliance`), appeal (a re-hearing before another authority
  in which the grounds, `appeal_weight`, are a presumption toward him), another forum where the disposal offered
  one, or carry a grudge to a later sitting. Each is an executable act with its worth shown and its price written
  (part 3 §B). **To abridge:** no callback; `form="auto"` is the host's rule (D6): a passing word (effort 0) nobody
  watches runs abridged.
- **What the view does not hand over (B17, in part open).** Choices matter in every played rite, the audience and
  the rally included (part 3 §B: a random chooser does far worse than one who takes his best perceived option), and
  a sharper reader wins more. But within one exchange the shown worth is close to sufficient: no view-only policy
  measured (a reader who weighs risk by his odds) beat taking the top worth by more than noise. The skill that the
  view does not hand over lives before and around the sitting (forum, rig, what to bring, effort, appeal) and in
  provoking. A second in-sitting choice per exchange is refused by precedent (§C.6: the frame is automatic from the
  ground, A-130 game first; part 4 §F 41); this item stays open in part, stated (part 4 §K B17).
- **Any role, or two at once:** speaker (the menu), adjudicator (§D; he may also be a side), audience (a body in the mood; may be called as a witness).
  `proceed(inp, rng, decide, deciders, rulings)` takes a callback per person: played and automatic meet in one
  sitting.
- **Pace.** `turns` decisions a speaker: 1 abridged; 1 to 3 conversation, negotiation, rally; 1 to 2 audience;
  1 to 4 questioning; 2 to 4 debate; 2 to 5 trial and inquisition.

## F. Simulated: the automatic policy (A-136)

```
temper = clamp(temper_step x heat x 2 mid / (will + grace), 0, 1)                 # 0 composed .. 1 lost (C4)
heat  += 1 at each rattle;  heat x= (1 - temper_cool) at each beat he makes        # it cools
t      = temper if temper >= temper_break else 0                                   # composed below the break (A-146, A-136)
value(option) = option.ev                                                          # its PERCEIVED worth (A-141)
              + t x { argue:   grain x ((2 care[channel] - 1) + (presence - mid) / 3 [as one of them])
                      press:   grudge x (-bond(him, the man opposite)) + pride x (will - mid) / 3
                      concede: -pride x (will - mid) / 3 }
```

**Decided (C4, rung 3: A-136 "so long as they keep their temper", A-146 "if your temper has hit a threshold"):**
"keeping his temper" means being below `temper_break`, and the temper is THIS sitting's provocation against what
his Will and Grace carry, not a standing property. Nobody is born broken (before, Will plus Grace of 3.5 or less was
past the break at zero rattles); it cools as he speaks; the break is logged once per witness. Below the break the
NPC is exactly the view-best chooser (part 3 §B), the same menu and view as a player, no other information. Past it
the man shows (the beat says how: "he can hold his tongue no longer" for a speech or a press, "his temper gone, he
gives way" for a concession): he argues from
what he himself holds, the orator plays to the room, the proud press and will not give way, the timid give way, a
grudge goes after its object. So a player's edge is preparation, forum, arrangement, and provoking a man out of
his composure. An unwatched low-stakes matter may run as the abridged form of its row (R6): the host's one rule
(D6) is `form="auto"`: abridged when the act's effort is 0 (nothing bears on the bearer) and nobody watches.

---

## G. Worldly matters

`Item(id, kind, weight, source, about, sincere)`: a typed reference, never text. `rosters.yaml: matters` (closed;
it absorbs the `proofs` roster):

| kind | carrier | who may bring it | what bringing it costs (the fold) |
|---|---|---|---|
| `record` | `Record` | its holder | disclosure: everyone present holds a claim of it |
| `testimony` | a `Claim` in the witness's ledger | the witness, or a side that calls him | he speaks and may be pressed |
| `deed` | a deed `Claim` | anyone holding it | names its source |
| `oath`, `debt` | an `oblige` Tenure | a party to it | binds the bringer again; a debt called in is spent |
| `title` | a `hold` Tenure, an `Office` | the holder | puts the title in question |
| `precedent` | an earlier matter's case-file stages | anyone who witnessed it | none |
| `law`, `treaty` | a `Record` of kind decree, covenant | anyone; a party | disclosure |
| `rumour` | a hearsay `Claim` | anyone holding it | low weight |
| `state_of_realm` | the strife reading, `open_era` | anyone in the realm | none |
| `confession` | the `record:confession` an earlier questioning wrote on the case file (B4) | the bench, the questioner | none |

An item is on a menu only if its mover holds it and the rite admits its kind. A false item (`sincere: false`) is
one its holder knows false, and it comes from one of two places only (A.3): his own false word (read from what he
knows) or a forgery (`[HOOK]`). It bears on each listener through `credit`, and a listener whose reading turns it
holds a `hypocrite` claim of him (§J).

## H. Arrangement: the type is a power act (A-132)

`tilt = rig x max(0, tanh((power(arranger) - power(other party)) / power_scale))`; `power(p) = rung + 2 x
level(modifier) + the regime's weight for his authority`. `rig` is the arranger's one choice (0, 0.5, 1). **The
arranger's side is his own where he is a party** (C3: an accused who arranges is tilted from his power, never from
his tie to his accuser), else the side his ties favour; the card names an arranger only where there is a tilt, and
names the side it works against (`tilted_against`); a third party leans to the side he is tied to, and tied to
neither more, tilts nothing (p4 §L 11). **The rig has one lever: those who decide start `presume_step x tilt`
toward him** (the bench leans his way), so where none but a party decides (a conversation, a questioning, a
negotiation) there is nothing to tilt: no tilt, no price, no grudge (p4 §L 10). **Cut by the stress-test pass (p4
§L 3, §L 9):** packing (dropping the seats and watchers least tied to him) and the watchers' sympathy against him.
Packing a declared bench changed its quorum arithmetic, not its lean, so it moved the verdict toward whoever did not
bear, whichever side arranged; the sympathy offset the presumption on a seat and on a watcher who decides nothing; with
both gone the rig moves every row toward its arranger and each rig level stays best somewhere. What a rig costs and
how it is seen are the fold's (below). A bench offered fewer seats than its quorum is refused `short_bench`. **It no
longer cuts turns** (C3: the cut fell on the arranger's own case as hard as on the other's, so the full rig bought
nothing over the half).

**The price (C3).** A rig is seen as plainly as it is pushed, and a shut door hides nothing (a closed court is
itself a sign): the arranger's faction pays `rig_price x tilt^2` in legitimacy whoever is in the room. Monotone in
the rig, no discount for secrecy (before, the price at the full rig was 0.165 against 0.49 at the half, because the
shut floor hid it). Resentment and the right of appeal follow the GRIEVANCE: the side the tilt worked against, if
it loses, resents the arranger (`grudge_rig x tilt`; the PARTY rigged against, moves or none, p4 §L 11) and carries the tilt as grounds of appeal; an arranger who
loses resents nobody for his own rig, and a side rigged FOR has no rig-grounds of appeal. Between equals `tilt` is
0. It replaces `presumes`, the `scripted` order and `case_rows`. On the reckoning `2 x stake x P(carried) - price`
each rig level is best somewhere (part 3 §B). **The weak party's options are executable acts** (§E, D1): accept, or
elsewhere where another authority sits (a fair forum next season); and after a loss, appeal up (R-35) to a
re-hearing before another authority, which reads the tilt as grounds. `contest` was cut (§F 42).

## I. Context: era, regime, strife (A-131)

`arrangements.yaml: context`, read by the builder; no code per kind. **Era:** the weight of each ground. **Regime:**
which rows are lawful (the regime's `unlawful` names the rows it outlaws: a theocracy the polity's debates, not the
Church's own deliberation on the debate rite, p4 §L 12), `standard`, `reason_lean`, kinds added to or dropped from `admits`, each authority's
weight in `power`, the floor, what silence means, `gravity`. **Strife:** `turns`, `unrest`, `gravity`, what the hungry want,
who is absent. **Office, seat, faction:** `precedence`, `power`, `office.duty`, who sits, `bond`, and a shared
faction is a tie (`tie` adds 0.3 for one of his own, so a solidarity argument lands with a partisan bench and a
partisan seat starts nearer his own). **Out** (the fold): standing, legitimacy both ways, a strife eased by what a
sitting resolved, an office contested, precedent, a matter docketed in turn.

**How era and regime act (requirement 8, decided by the ladder):** they act on PLAY, the choices men make: the era
changes which ground a speaker reaches for where his listeners want and hold alike; a regime changes what silence
means (a theocracy's silence admits; a commune's plainer occasion makes it cheaper, never free where an answer is owed: p4 §L 6), what may be shown, what the occasion asks of
Grace, and which rites exist at all. **And a regime enters the close the same way strife does** (rung 4, the
precedent of strife's `gravity`: one method for context's three inputs): each regime carries a `gravity` delta, so
a change is graver under a theocracy (+0.5) than under a crown or a commune (0), and the same case is harder to
carry there (part 3 §B.6). Every delta is data in the context table, `[ASSUMPTION; Jordan to correct]`.

## J. Disposal (A-133)

`arrangements.yaml: disposal`: `(what the row disposes, band) -> typed writes`; the fold performs every one.

| disposes | Overwhelming | Success | Partial | Failure | impasse (no band) |
|---|---|---|---|---|---|
| `none` | hearers' pursuits moved, regard up, a `converted` claim | pursuits, regard up | regard up | regard down, a grievance (only where someone opposed him: B3) | regard down |
| `yield` (questioning, B4) | what he yielded, in the questioner's ledger (weight 1); a `record:confession` on the case file, which later sittings may show; the questioned man's regard for the questioner down | what he yielded; his regard down | a hint (weight 0.4) | nothing yielded; the questioner's importuning noted | as failure |
| `oblige` | an `oblige` Tenure, regard up, precedent | the Tenure, regard up | adjourned | a grievance; another forum | another forum |
| `detain` | a `detain` Tenure, office contested, precedent, legitimacy up | the Tenure, precedent, legitimacy up | surety, adjourned | an acquittal, precedent, the accuser's regard down | adjourned |
| `ban` | a `ban` Tenure, office contested, precedent | the Tenure, legitimacy up | surety, adjourned | an acquittal; the ACCUSER's legitimacy down (a charge that failed discredits who brought it; a right acquittal never the court, p4 §L 4) | adjourned |
| `decree` | the decree, faction up, precedent, legitimacy up | the decree, faction up | adjourned | recorded defeated, faction down | adjourned |

**Reception (A-144, the adjudicator's Grace), for a RULING only** (a `bench` or `declared` close; B3: a tell, a
rally and a party's own decision are not received as rulings and mint nothing). **Wrong means against the merits
as the record shows them** (B5, decided, rung 5): `merits` is how far the sitting itself moved those who heard it
(each listener's track less where his stake and the arrangement started it), and a verdict is wrong where it
carries against merits below `-merits_at` or fails against merits above it; a judge's own lean is partiality
(below), not the measure of right. The fold scales what the ruling does in the world: his faction's legitimacy (his FORUM's: `forum_faction`, the
faction of the seat he holds, else his own, read at every legitimacy, standing and price write, p4 §L 4)
`+legit_ruling x reception` where right, `-legit_wrong` where wrong, less `legit_brute x brute` (doubled where
wrong); **compliance** `(1 + reception) / 2`, x 0.6 where wrong (a brute's right verdict is half obeyed: enforced
by his station, not accepted; it is read by the loser's after-sitting choice, §E); the **appeal weight** `brute +
0.5 if wrong + the tilt, if the loser is the side it worked against` (read by the appeal's re-hearing as a
presumption toward the appellant); each person's regard for him: the winner `+reception`, the loser `-brute` and
`-wrong` where the ruling was wrong, the forum rigged, or the judge conflicted and ruled his own way (a rigged-
against party never warms to the packed judge), everyone else `+reception - brute` where right and `-(wrong +
brute)` where wrong (a gracious judge who rules against the merits pays with the room that saw them); his
faction's standing `-brute`. **Partiality's price (B6):** a conflicted judge who rules the way he leans pays
`partial_price x conflict` in legitimacy. A played and a simulated judge pay alike.

Every sitting also leaves, from the beats: the stage on the case file; to each present a claim of each rattle,
item shown, concession, contumacy, insincere speech **that his own reading turned** (`hypocrite`, from the beat's
`caught`, B2), a decider's conflict and lean, a rigged forum, a played judge's ruling against the room, and **one**
`lost his temper` per man per sitting (C4); to each bystander who does not decide a claim of what he heard (B21:
he heard it, so his track moved; he learns, he does not rule); regard both ways (down toward a presser who rattled
him and toward a witness who stood against him; up toward a witness who stood by him and between parties who came
to terms; each hearer toward each speaker by how far his own track travelled toward that speaker's side; down
from those who decide toward a man who would not answer, A-145); each party's pursuits by `outcome x |stake|`;
rattles as strain carried; the loser's grudge against the winner, and against the arranger where he was rigged
against. **Every bounded quantity** (regard, legitimacy, standing, pursuits) moves by `bounded(x, d)`: a step is
worth less the nearer the bound it pushes, so nothing runs away (B9), the step and the result held to [-1, 1] (p4 §L 5), and the season driver fades each by `fade`
between seasons. **A strife moves only by what a sitting resolved** (B3): a carried decree, obligation, detention
or ban on a matter that names it eases it by `strife_ease`; nothing a sitting does creates or inflames it; it never
goes below 0. **A conviction is never written** (A-92, `04:251`). The fold's coefficients are one table
(`host.FOLD`), each `[ASSUMPTION; Jordan to correct]`. Owners `[UNVERIFIED
against `write_matrix.yaml`]`: the `ending` and case file B24p.20, B24.14; Tenures `determine`'s effect and
B24.08; claims WITNESS (B24p.22); regard and pursuits B27; offices BA1; obligations B28; standing, legitimacy,
strife B33.

**The docket has readers (D1 to D3).** The loser's `after()` act writes an `appeal`, `other_forum` or `grievance`
entry; the season driver (a labelled, minimal host loop in the model, `acts.season`; the real one is the season
loop's) convenes them the next season: an appeal is re-heard before another authority with no rig and the grounds
as a presumption toward the appellant, and a reversal removes the first disposal's tenure; **an appeal's verdict is
final**, a grievance is settled by its one hearing whatever its outcome (p4 §L R3) and an appeal lies only to a forum that exists and may hear the matter; a sitting the builder refuses
(keyed: a vacated seat, a man who is gone) is skipped and recorded, and the season goes on (p4 §L 8); a grievance is a
conversation between the two (and a grievance once aired cannot be carried again); an adjourned matter returns to
its row; another forum is an arbitration. An entry not convened within two seasons lapses. Between seasons every
bounded quantity fades by `fade` and rattles age (strain carried, A.4). So "a loss leaves somewhere to go" and
"three seasons" are measured on a loop the design itself defines (part 3 §B).

## K. The settings

Fifty-four of the proceeding's own, each `[ASSUMPTION; Jordan to correct]`. (The design this replaces had 53 and
three tables; this v2 had 54 before the second fix pass and 55 after it; the stress-test pass cut `sympathy_step`
with the watchers' sympathy, p4 §L 3: 55 - 1 = 54.) **54 - 1 + 2 = 55 at the second fix pass, for stated reasons:** `yield_track` is cut (a given-up matter goes as far as the close's
leverage carries, `M_MAX / track_step`); `temper_cool` is added (C4: a temper must cool, and nothing else measured
time within a sitting); `recuse_at` is added (B6: recusal was asserted and nothing carried it). The fold's
coefficients were hard-coded and uncounted; they are now one table of 24 (`host.FOLD`, below), so what was hidden is
counted, not new.

| group | settings (shipped) |
|---|---|
| the speech | `fit_level` strong; `answer_level` moderate; `repeat_step` 0.35; `sense_step` 0.15, `involve` 0.3; `esteem_step` 0.2 [a fifth of a level a point of Grace better than the other], `show` 1.0; `off_step` 1.0; `admit_step` 0.5, `contempt_step` 1.0 [silence and the burden]; `ploy_step` 1.5, `grain_strain` 0.5; `heard_step` 0.05, `heard_floor` 0.5; `gap_step` 0.25; `weary_step` 0.5, `stay_base` 1.0, `stay_per_will` 0.5 [Will 4 argues three speeches fresh]; `awe_step` 0.5; `comfort_step` 0.5 [now `discern`, B10]; `rel_gain` 0.5; `flop` 0.5; `invite` 0.5 |
| the press | `press_ob` 1.25, `press_pull` 1.0 [x heat], `rattle_pull` 0.5, `wear` 0.5, `rattle_gain` 1.5, `rebound` 1.0, `reactance` 0.75, `room_level` 0.5, `heckle` 1.0 |
| conceding | `concede_step` 1.0 [was 2.0: with the cost now taken from where he stands and descent buying the next rung's ground, 2.0 made descending best nowhere; at 1.0 it is best in some trial positions and still always costs], `consent_at` 2.5 |
| the room and the reading | `crowd_at` 12, `crowd_lean` 0.2, `mood_scale` 5, `read_scale` 1, `read_blur` 2, `read_noise` 0.3, `bias_step` 2, `relevance` on |
| the close | `track_step` 0.2 |
| the NPC's temper | `temper_step` 0.5, `temper_break` 0.75, `temper_cool` 0.5 [an ordinary man breaks at a second rattle that follows the first closely; Will 1 Grace 2 at his first; Will 7 Grace 7 only after three in quick succession; nobody at none], `grain` 2.0, `grudge` 2.0, `pride` 2.0 |
| the host | `start_step` 2.0, `presume_step` 2.0, `power_scale` 2.0, `strain_fade` 0.5, `recuse_at` 0.25 |
| the fold (`host.FOLD`) | regard: `carried` 0.1, `accord` 0.15, `unmoved` 0.05, `accuser` 0.1, `acquitted` 0.2, `heard` 0.03, `contumacy` 0.1, `pressed` 0.1, `witness` 0.1, `lost` 0.05, `grudge_rig` 0.3, `reception` 0.1, `brute` 0.2, `wrong` 0.1; legitimacy and standing: `legit_ruling` 0.1, `legit_brute` 0.4, `legit_wrong` 0.2, `legit_fall` 0.5, `rig_price` 0.25, `partial_price` 0.5, `standing` 0.5; `strife_ease` 0.25; `merits_at` 1.0; `fade` 0.25 a season |

Controls: the levels at none; `repeat_step`, `esteem_step`, `off_step`, `ploy_step`, `grain_strain`, `start_step`,
`crowd_lean`, `heckle`, `room_level`, `heard_step`, `gap_step`, `weary_step` at 0. The centre is the difficulty
cell (part 3 §B, D2).

## L. The precedent map

`PM` = `research/social_contest_procedures/03_persuasion_mechanisms.md` (its *Engine:* lines are its author's
assumption and are not used); `RO` = `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md`;
`NP` = `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md`.

| mechanism | passage opened | the source's grade | follows, adapts, departs |
|---|---|---|---|
| the grounds are the three means: **logos** `evidence` (the proof shown); **pathos** `consequence` and `authority` (what the listener wants and holds, as the matter bears on them); **ethos** `solidarity` (who the speaker is to him) | `RO:76`; `NP:26-28` | `RO:47` web-verified; `NP` `[T2]`, `[T1 — SEP]` | **adapts** (four grounds); **departs** on ethos, which `NP:26` puts in the speech, not in prior standing: here it is the listener's tie and the speaker's esteem, because the world holds those and a speech has no text |
| the families are the genres, by who judges and what they decide | `RO:77`; `NP:32` | as above | **follows**: judicial (trial, inquisition; questioning feeds one); deliberative (debate, audience, and the rally: a crowd urged to a course decides a future action); the dyadic rows have no classical genre; **epideictic** (praise and blame before spectators) has no row: none was asked for |
| an argument is aimed at those who decide | `RO:337` | the file's synthesis | **follows** |
| the issue ladder is stasis | `RO:90`, `RO:99`; v30 `:56-68`, `:107-112` | web-verified spine; v30 ratified | **adapts**: B24.03's rungs; conceding descends; each rung is argued from its own grounds (`weighs`: the conjectural from signs and proof, the definitional from what is owed, the qualitative from motive and sympathy), so conceding the fact to fight on its justification is a play |
| raise and answer are confirmatio and refutatio | `PM:23`; `NP:44-46` | primary citations; `[T1]` | **adapts**; exordium, narratio, partitio, peroratio give no decision and are not mechanisms |
| prove, please, move | `PM:15`; `NP:48` | `[T1 — Quintilian]` | **not a mechanism** |
| decorum is the venue's standard met by Grace | `PM:43`; `NP:50` | primary citation | **follows** |
| the *vir bonus*: a man's character is part of his case | `PM:39-47` | primary citation | **follows**: sincerity; esteem |
| fit reads what the listener already holds | `PM:66` | primary citation | **follows** |
| elaboration: for the able and involved, argument quality decides; for the rest, source and manner | `PM:137`; `NP:62-71`; N3 `NP:231` | published | **follows**, as a weight (C.3) |
| the room recoils from a repeated press | `PM:135`; `NP:110`; N5 `NP:248`, `:253` | `[FROM MEMORY, UNVERIFIED]`; `[T1 — standard; not re-verified]` | **adapts, lightly**: one setting |
| the bearer opens | `NP:118` | `[T0]` | **consistent, not built** |
| reading by acting on the other (elicitation) | `proposals/2026-09-05-proceedings-subsystem/01_THE_STUDY.md:113` | the study's finding | **not built**: the free reading stays (R1); a setting that sharpened it with each speech carried nothing measurable and was cut |
| inoculation; deliberation among deciders (N10, `NP:276`); attribution (N16); composition (N19) | `PM:136`; `NP:112` | memory-grade; N12 to N16 a paraphrase of a paraphrase | **not built** (rung 1: A-14 for N10); attribution is the beat; composition is raise and answer |
| a judgement formed item by item | `NP:101` | `[T1]` | **departs, knowingly** |

## M. The verbs, and the seam

RD §D stands: `argue`, `interrogate` (and `covenant`, `interview`, `determine` at their items) open the full form;
`tell`, `lie`, `speak` the abridged, by a `proceeds:` cell. A `lie` is an `argue` whose item is the liar's own
false word or forgery (`sincere: false`). `proceed(inp, rng, decide, deciders, rulings) -> Outcome(beats, state,
ended, ended_by, verdicts, ruled)`. The module keeps no state, grades no band, names no winner, writes nothing. The
acts around a sitting (`before`, `after`) and the season driver are the HOST's (`sc2/acts.py` in the model): the
module never sees them.
