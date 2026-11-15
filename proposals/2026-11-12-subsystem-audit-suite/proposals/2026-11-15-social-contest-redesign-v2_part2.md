# SC — the social contest redesigned, v2, part 2: the design

## Status: PROPOSED (the second part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first: its status, markers and binding list apply here; reference under CLAUDE.md §0.05, nothing reads it at runtime)

Reconciled 2026-11-15 after two antagonist passes and Jordan's rulings A-136 to A-140. Conventions: `mid` 4,
`floor` 1, `ceiling` 7 on the attribute scale; `pool_of`, `opposed_ob`, `even_line`, `net_boost` (soft cap),
`roll_net_continuous`, `level` are `engine/dice_engine/sigma_leverage.py`'s; `even = even_line(pool_add)`. Pools
are fractional, obstacles real (R8). Every formula is the model's (`sc2/engine.py`, `sc2/host.py`), stated once;
model and text were made to agree line by line in this pass.

---

## A. The person in the room

### A.1 One record, and the nemo rule

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
    believes: float            # what he KNOWS of the matter, -1..1 toward `for` (his own ledger)
    power: float; precedence: int   # his circumstances: seat, office, wealth, influence, faction (host)
    items: tuple; strain: float
```

**The nemo rule (A-139), one invariant on the input:** nobody is both a side and an adjudicator; no sitting has
one character; a drawn close has an adjudicator who is not a party; a cohort has weight. The builder never seats
a party to judge his own matter (a seat who is the accuser speaks, and the bench is the other seats; if none is
left the proceeding is refused). Consent is not adjudication: under `close: consent` nobody decides, and the
outcome is whether a party accepted, which is his act. Everyone in the room has a track; `decides` only says whose
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
| his **stake** (whether he comes, which side, how hard) and his **start** (partiality) | `stake = bearing(p, matter)`; `start = start_step x mean(stake)`; a decider with a tie starts where it puts him and the fold deposits a `partial` claim |
| the **fit** of an argument to him | it reads the MATTER: `clip(side x stake[channel] + 0.5 x (2 care[channel] - 1))` for `consequence` (want) and `authority` (hold); `clip(bond(him, speaker) + 0.5 x (2 care.bond - 1))` for `solidarity`; `credit(him, item)` for `evidence` |
| the **aim** of a press on him | `2 care[channel] - 1`; on `evidence`, what the item shows of him or of one he is bound to |
| **credit** of an item | `clip(2 weight - 1 + bond(him, source) - max(0, bond(him, the one implicated)))` |
| **sincerity** | `insincerity = max( -side x believes, -side x stake[channel], 1 if the item is one he knows false )`, clipped to 0..1: agreement between what he says and what he **knows and holds**; a self-serving lie is insincere through `believes` though it runs with his stake |
| the **cost of conceding** an issue | `concede_step x (1 + max |stake|)` |
| his **intent**, as the other side reads it | the mean of his stake, blurred, in the other's `View` |
| the **verdict's effect** | the fold: his pursuits move by `outcome x |stake|` |

So a consequence argument for remitting the tolls fits the guild and misfits the toll men, who lose by it.

### A.3 Which layers exist today

| layer | carrier | status |
|---|---|---|
| pursuits, convictions | `Person.pursuits`, `.conviction` (`state/carriers.py`); `data/affiliations.py` | exist |
| goals | `data/goals.py`; `rosters.yaml: goal_object_kinds` | exist |
| what he knows | his ledger of `Claim`s; `person_q.said_of`, `lie_said_of` | exist: `believes` and a lie's false item are read from them |
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
    issues: tuple           # the stasis rungs it runs through (B24.03's `issue_rungs`)
    concede: str            # descends | accepts
    moves: tuple            # per side, of: argue, press, rest, concede
    close: str              # bench | declared | hearers | consent | exchange (the abridged form)
    turns: int; standard: float; reason_lean: float; admits: tuple
    difficulty: float; stakes: float; quorum: Optional[int]; unrest: float
```

The module reads these cells and compares no row, move or person id (a move is read by its `effect`: `track`,
`strike`, `yield`, `none`). The eight rows are part 1 §D. `abridged(row)` is any row with one turn, the one move
`argue` for the bearer, `close: exchange`, and the one addressed present as a hearer who decides.

---

## C. The exchange

### C.1 The value, the order, the beat

```python
Sitting(n, issue, points, live, tracks, cond, used, last_voice, ended)
Point(id, side, issue, ground, item, by, held)        # held: how far it stands with each listener
Cond(rattles, strain, pressed, spoken, spent)          # one per person; `spent` is staying power used
Beat(n, mover, voice, side, move, relation, issue, ground, item, point, target,
     margin, drift, evaded, insincere, rattled, moved, closed, mood, terms)
```

- **Order and turns.** The bearer opens, the rest by precedence. Each speaker has the rite's `turns`; a resumed
  sitting gives him the turns less what `cond.spoken` says he has had, the beats continue their count, the issue
  reached stands, and a sitting that ended `yielded` is not resumed (an adjourned one is).
- **One live point a side.** A raise makes the mover's point live; older points stay in the record.
- **A track** is each person's own: `track[h] = h.start + the sum of the beats' moves on h` (asserted). `tracks`
  is kept in `Sitting` as that running value so a resume needs no replay; it is never a verdict.
- **The beat** is the narrative record (no text field); `terms` (true values) is in the outcome only.

### C.2 The speech: one draw, one margin per listener

A fixed 2G+8 normals an exchange (the reading's accuracy; a blur for each believed fit, each believed aim, the
strain, the mood, their point, his own point, the other's intent; the hold; the speech), each believed number its
own. For voice `V`, side `s`, ground `g`, item `i`, heard by `h` (everyone not on the speaking side):

```
k        = clamp(content[g] + rite.reason_lean - crowd_lean x crowd, 0, 1)                  # R11: content AND venue
pool     = heard(V) x pool_of(weighted_tenth((V.reason, V.presence), (k, 1-k)) + V.rank)
heard(V) = clamp(1 - heard_step x max(0, (1 + 6 x crowd) - V.presence), heard_floor, 1)      # Presence: listened to
sigma_h  = level(fit_level) x era[g] x (fit(h, V, s, g, i) - repeat_step x uses) x q(h, g)   # q: R12 Reason (C.3)
         + esteem_step x esteem(V) x 2 (1 - elab(h))                                         # Grace; standing weighs less with the able
         + level(answer_level)  if the speech answers what stands
ob_h     = even + opposed_ob(h.will + h.rank) + weary(V) + gap(V)  [+ difficulty + stakes in the abridged form]
margin_h = roll_net_continuous(pool) + net_boost(sigma_h, pool) - ob_h
         - off_step x wF(h) x off  -  ploy_step x wA(h) x insincerity                        # R12 Focus, Attunement
esteem(V) = short(the man opposite) - short(V);  short(p) = max(0, rite.standard + show x p.rattles - p.grace)
weary(V)  = weary_step x max(0, V.spent - (stay_base + stay_per_will x V.will))              # Will: keep arguing
gap(V)    = gap_step x max(0, power(the other side) - power(V)) x (1 - (V.reason - floor) / (ceiling - floor))   # Reason: accounts for it
```

- **The opposition (A-137)** is the listener's `will + rank` at 0.4 a point: the resisting attribute counts as the
  mirror of the attribute in the pool. At control the abridged margin is that one roll (200 of 200 keys).
- **Esteem** is his standing in the room this sitting: how much better he meets what the occasion, and his own
  rattles, ask than the man opposite does. It is relative, so the standard prices a shortfall against the other
  side and does not tilt the room against whoever speaks; with nobody opposite it is his own shortfall. Derived
  each exchange, never stored on a person (S-7).
- **The other side's circumstances** (`power`: his seat's rung, his office's modifier, the regime's weight for
  his authority; wealth and influence as `[HOOK]` terms) stand against a speaker as an obstacle unless his Reason
  accounts for them. This is the home of B28.10's *relative rung of the teller's seat* and B28.34 and B28.35's
  hearer terms. With nobody opposite, the weightiest of those who decide is who he must account for.
- **A raise** adds `s x margin_h` to each listener's track and puts a point on the table. **An answer** only
  undoes the other side's live point: `min(how far it stands with him, margin)` when it lands, the whole negative
  margin when not. **Turning away:** under `reply: must`, while their point stands, a raise, a press or silence is
  charged `off_step x evade x wF(h)`. **Staleness:** each earlier use of a ground or item costs `repeat_step`.
- **Drift.** `pull = press_pull [just rattled] + rattle_pull x rattles + unrest + heckle x max(0, heat)`; `drift =
  max(0, pull - (roll_net_continuous(pool_of(V.focus)) - even))`; `off = drift + evade` where he turned away.
- **Against his grain.** `strain += grain_strain x insincerity`.

### C.3 What each listener brings (R12)

| his attribute | Jordan's word | the one operand, in his own track |
|---|---|---|
| Reason | *"to see if argument/speech makes sense"* | `elab = clamp(0.5 + sense_step (reason - mid) + involve x max|stake| - crowd_lean x crowd, 0, 1)`; `q(h, g) = 2 elab` on a reasoned ground (`content >= 0.5`), `2 (1 - elab)` on a mannered one, and the speaker's esteem counts `2 (1 - elab)`: a **weight**, so that for an able and involved listener the quality of the case decides and manner and standing do not (ELM, `NP:62`) |
| Focus | *"to see if it's relevant"* | `wF = (focus - floor) / (mid - floor)`: how much of a speech's drift or evasion he deducts |
| Attunement | *"to see if it's sincere or a ploy"* | `wA = (attunement - floor) / (mid - floor)`: how much of its insincerity he deducts, on an argument and on a press made with something its holder knows false |
| Will | (R1) | the opposition to whatever is aimed at him |

No draw is taken for the three. Each reads slope exactly 0 with its own setting off and the sign the ruling gives
with it on, in a full trial (part 3 §B). **Decided (rung 5):** the ploy is carried by `insincerity` on `argue` and
`press`; `deceive` and `divert` are not restored, because a lie is an argument its speaker knows false (the host
gives it its item from his own false claim, `person_q.lie_said_of`) and being pulled off the point is what a
landed press and a heckling room already do (R1 Focus) and what turning away prices (R12 Focus).

### C.4 The press and the rattle

```
sigma  = level(fit_level) x era[g] x aim(T, g, i) + room_level x heat(T) + esteem_step x esteem(V)
ob     = even + opposed_ob(max(0, T.will + T.rank - T.strain / 0.4)) + weary(V) + gap(V) + press_ob
margin = roll_net_continuous(pool) + net_boost(sigma, pool) - ob
landed (margin >= 0):  T.rattles += 1, T.strain = 0, T.spent += 1, T is pulled on his next speech;
                       each listener moves rattle_gain x (1 - reactance x T's earlier rattles) x (1 - max(0, bond(h, T)))
failed:                T.strain += wear; each listener moves `rebound` against the presser
either:                less off_step x wF(h) x off, less ploy_step x wA(h) if it was made with a forged item
```

A rattle is the one discrete event and is decided by a draw. It moves the room at once (less with each repeat,
then against the presser); it lowers his esteem on every later speech (`show`, which Grace's headroom absorbs); it
pulls his next speech (Focus); it spends his staying power (Will); it is witnessed. Nothing forces him to stop.

### C.5 Conceding, resting, ending

- **Concede an issue** (`descends`, a rung remains): each listener's track becomes `his start - side x
  concede_step x (1 + max|stake|)`; the mover's grounds are fresh; the next rung opens.
- **Concede the matter** (the last rung, or `accepts`): the sitting ends `yielded`. Under `consent` that is the
  accept. Before those who decide, he has given the matter up: every listener's track becomes `-side x
  yield_track`, so the close is drawn with the room wholly against him. A confession is still not a verdict (the
  bench's draw stands, A-14), but it is decisive: part 3 §B gives the rates.
- **Rest**: nothing; silence under `must` while a point stands is turning away.
- **Ends**: `budget`, `rested`, `yielded`.

### C.6 The six, speaker side (R1, R2)

| attribute | Jordan's words (R1) | carried by |
|---|---|---|
| Reason | *"constructing the argument ... logical and reasonable and evidentiary with ability to account for opponent's factual circumstances like resources office influence"* | its share `k` of the dice (the reasoned grounds; `evidence` is where what he holds becomes fit); and `gap`: it discounts the other side's circumstances |
| Presence | *"the ability to be listened to and be compelling with your delivery"* | `heard` (the share of him the room listens to); its share `1 - k` of the dice |
| Attunement | *"what is most likely to rattle your opponent or reading their intent ... read the room ... what kind of argumentation is most effective"* | the accuracy of his `View`: believed aim and strain, believed intent, believed mood and points, believed fit |
| Focus | *"staying on topic, not being pulled away"* | the hold (`drift`) |
| Grace | *"correct manner for the venue ... seen as respectable ... composed in face of difficulties"* | `short` against the venue's standard; `esteem` in the room; headroom that absorbs a rattle |
| Will | *"keep arguing your case ... believe in yourself and remain confident ... not get rattled in first place"* | `weary` (staying power); the opposition to a press; as a listener, to an argument |

A-138: at a quiet tell Focus, Attunement and the speaker's Will have no object and are silent.

---

## D. The close

```
drawn (bench, declared, hearers): for each adjudicator, one normal:
    margin = roll_net_continuous(pool_of(mid)) + net_boost(track_step x track[d], pool)
             - (even + opposed_ob(mid) + rite.difficulty + rite.stakes)
consent:   nobody adjudicates and nothing is drawn; a party's accept is Success for the bearer, the bearer's
           withdrawal is Failure, neither is an impasse (no band)
exchange:  the one speech's margin with the one addressed, plus his start
```

The host reads the verdicts (`act_band`): `bench` the presiding seat's; `declared` the presiding seat's, demoted
when fewer than `quorum` seats read Success; `hearers` the weight-mean. Never the actor's last exchange.
**Questioning for information has no verdict:** it yields what the questioned man chooses to give (his accept);
a confession accepted or a charge laid on it is a separate proceeding with its own adjudicator. **A played
adjudicator** is a role: at the close he has `JudgeView(id, track, odds, points)` (his own mind, which he knows,
and the points as they stood) and three choices: rule for, rule against, or leave it to his draw; how far a
ruling departs from his own track is returned (`Outcome.ruled`) and deposited as a claim with everyone present.
What he asks during the sitting (bench moves) is a `moves` cell the rows do not yet fill `[not modelled]`.

---

## E. Played: the view, the choices, the pace

```python
@dataclass(frozen=True)
class View:                       # own values true; everything else believed (each with its own noise) or public
    n: int; mover: str; side: str; issue: str; turns_left: int
    live_theirs: Optional[tuple]; live_own: Optional[tuple]     # (point, ground, item, believed strength)
    options: tuple                # Option(move, ground, item, relation, ev, p)
    own: Cond; esteem: float; weary: float                      # his condition and standing
    visible: tuple                # each speaker's rattles
    mood: float; odds: float      # the room as he reads it; P(carried) on that reading before an ordinary bench
    intent: float                 # the believed stake of the man opposite
    fit: tuple; aim: tuple; strain_seen: float; acc: float
```

- **Honest and not omniscient.** `odds` and every option's worth are computed from his believed values and an
  ordinary stranger (B05.62), never from a true attribute or a true start. The card's `odds` is the close before
  an unmoved ordinary bench, and is `None` where nothing is drawn (consent) or the verdict is the speech itself.
- **What he chooses, per exchange:** raise a point (three grounds, or the proof with an item he holds), answer
  theirs, press the man, concede, rest: 4 to 12 options by rite and side. **Before:** whether to come, what and
  whom to bring, his effort (turns), and with power how hard to rig the forum (§H); without it, to accept the
  forum, contest it, or go elsewhere. **After:** accept, appeal, another forum. **To abridge:** no callback.
- **Any role:** speaker (the menu), adjudicator (§D), audience (a body in the mood; may be called as a witness).
  `proceed(inp, rng, decide, deciders, rulings)` takes a callback per person: played and automatic meet in one
  sitting.
- **Pace.** `turns` decisions a speaker: 1 abridged; 1 to 3 conversation, negotiation, rally; 1 to 2 audience;
  1 to 4 questioning; 2 to 4 debate; 2 to 5 trial and inquisition.

## F. Simulated: the automatic policy (A-136)

```
temper = clamp(temper_step x his rattles + (2 mid - will - grace) / 6, 0, 1)      # 0 composed .. 1 lost
value(option) = option.ev                                                          # what his own reading says
              + temper x { argue:   grain x ((2 care[channel] - 1) + (presence - mid) / 3 [as one of them])
                           press:   grudge x (-bond(him, the man opposite)) + pride x (will - mid) / 3
                           concede: -pride x (will - mid) / 3 }
```

While he keeps his temper the NPC takes the best option his own reading supports: the same menu and view as a
player, no other information. As he is rattled past what his Will and Grace carry, the man shows: he argues from
what he himself holds, the orator plays to the room, the proud press and will not give way, the timid give way, a
grudge goes after its object. So a player's edge is preparation, forum, arrangement, and provoking a man out of
his composure. An unwatched low-stakes matter may run as the abridged form of its row (R6): the host's choice of
`form` by the act's effort.

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
| `confession` | the conceding beat of an earlier sitting | the bench, the questioner | none |

An item is on a menu only if its mover holds it and the rite admits its kind. A false item (`sincere: false`) is
one its holder knows false: a lie's claim, a forgery. It bears on each listener through `credit`.

## H. Arrangement: the type is a power act (A-132)

`tilt = rig x max(0, tanh((power(arranger) - power(other party)) / power_scale))`; `power(p) = rung + 2 x
level(modifier) + the regime's weight for his authority`. `rig` is the arranger's one choice (0, 0.5, 1). In the
builder `tilt` packs the bench (drops the share least tied to him), shuts the floor at high tilt, cuts turns
toward the row's minimum, starts those who decide `presume_step x tilt` toward him and those who watch
`sympathy_step x tilt x (1 - their tie to him)` against him. A rigged forum is seen by whoever is in it (a `rigged`
claim, legitimacy down by how many saw, an appeal docketed): shutting the floor hides it. Between equals `tilt` is
0. It replaces `presumes`, the `scripted` order and `case_rows`. The weak party's options are acts that exist:
play the hand, contest the forum, appeal up (R-35), another forum.

## I. Context: era, regime, strife (A-131)

`arrangements.yaml: context`, read by the builder; no code per kind. **Era:** the weight of each ground. **Regime:**
which rites are lawful, `standard`, `reason_lean`, kinds added to or dropped from `admits`, each authority's
weight in `power`, the floor. **Strife:** `turns`, `unrest`, `stakes`, what the hungry want, who is absent.
**Office, seat, faction:** `precedence`, `power`, `office.duty`, who sits, `bond`. **Out** (the fold): standing,
legitimacy both ways, a strife eased or inflamed, an office contested, precedent, a matter docketed in turn.

## J. Disposal (A-133)

`arrangements.yaml: disposal`: `(what the row disposes, band) -> typed writes`; the fold performs every one.

| disposes | Overwhelming | Success | Partial | Failure | impasse (no band) |
|---|---|---|---|---|---|
| `none` | hearers' pursuits moved, regard up, a `converted` claim | pursuits, regard up | regard up | regard down, a grievance | regard down |
| `oblige` | an `oblige` Tenure, regard up, precedent | the Tenure, regard up | adjourned | a grievance; another forum | another forum |
| `detain` | a `detain` Tenure, office contested, precedent, legitimacy up | the Tenure, precedent, legitimacy up | surety, adjourned | an acquittal, precedent, the accuser's regard down | adjourned |
| `ban` | a `ban` Tenure, office contested, precedent | the Tenure, legitimacy up | surety, adjourned | an acquittal, legitimacy down | adjourned |
| `decree` | the decree, faction up, precedent, legitimacy up | the decree, faction up | adjourned | recorded defeated, faction down | adjourned |

Every sitting also leaves, from the beats: the stage on the case file; to each present a claim of each rattle,
item shown, concession, insincere speech an attuned man saw (`hypocrite`), a decider's partiality, a rigged forum,
a played judge's ruling against the room; regard both ways (down toward a presser and toward a witness who stood
against him; up toward a witness who stood by him and between parties who came to terms; each hearer by how far
his own track travelled); each party's pursuits by `outcome x |stake|`; rattles as strain carried; the strife;
an appeal where a rigged forum was lost. **A conviction is never written** (A-92, `04:251`). Owners `[UNVERIFIED
against `write_matrix.yaml`]`: the `ending` and case file B24p.20, B24.14; Tenures `determine`'s effect and
B24.08; claims WITNESS (B24p.22); regard and pursuits B27; offices BA1; obligations B28; standing, legitimacy,
strife B33.

## K. The settings

Forty-four of the proceeding's own (the old design: 53 and three tables), each `[ASSUMPTION; Jordan to correct]`.

| group | settings (shipped) |
|---|---|
| the speech | `fit_level` strong; `answer_level` moderate; `repeat_step` 0.35; `sense_step` 0.15, `involve` 0.3; `esteem_step` 0.2 [a fifth of a level a point of Grace better than the other], `show` 1.0; `off_step` 1.0, `evade` 1.5; `ploy_step` 1.5, `grain_strain` 0.5; `heard_step` 0.05, `heard_floor` 0.5; `gap_step` 0.25; `weary_step` 0.5, `stay_base` 1.0, `stay_per_will` 0.5 [Will 4 argues three speeches fresh] |
| the press | `press_ob` 1.25, `press_pull` 1.0, `rattle_pull` 0.5, `wear` 0.5, `rattle_gain` 1.5, `rebound` 1.0, `reactance` 0.75, `room_level` 0.5, `heckle` 1.0 |
| conceding | `concede_step` 2.0, `consent_at` 2.5, `yield_track` 12 |
| the room and the reading | `crowd_at` 12, `crowd_lean` 0.2, `mood_scale` 5, `read_scale` 1, `read_blur` 2 |
| the close | `track_step` 0.2 |
| the NPC's temper | `temper_step` 0.5, `grain` 2.0, `grudge` 2.0, `pride` 2.0 |
| the host | `start_step` 2.0, `presume_step` 2.0, `sympathy_step` 1.5, `power_scale` 2.0, `strain_fade` 0.5 |

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
| the issue ladder is stasis | `RO:90`, `RO:99`; v30 `:56-68`, `:107-112` | web-verified spine; v30 ratified | **adapts**: B24.03's rungs; conceding descends |
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
false claim (`sincere: false`). `proceed(inp, rng, decide, deciders, rulings) -> Outcome(beats, state, ended,
ended_by, verdicts, ruled)`. The module keeps no state, grades no band, names no winner, writes nothing.
