# SC — the social contest redesigned, v2, part 2: the design

## Status: PROPOSED (the second part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first: its status, markers and binding list apply here; reference under CLAUDE.md §0.05, nothing reads it at runtime)

Conventions. `mid` is 4 and `floor` 1 on the attribute scale (`engine/substrate/descriptors.py`); `pool_of`,
`opposed_ob`, `even_line`, `net_boost` (with its soft cap), `roll_net_continuous` and `level` are
`engine/dice_engine/sigma_leverage.py`'s (the first three land at B04.24, the composer at B05.14). `even =
even_line(pool_add)`. A pool is fractional and never rounded; an obstacle is a real number (R8). Every formula
below is the model's (`sc2/engine.py`, `sc2/host.py`), stated once.

---

## A. The person in the room

### A.1 One record

```python
@dataclass(frozen=True)
class Present:                 # everyone: participant, adjudicator, audience
    id: str; weight: int       # a cohort is a person at weight above one (the tree's rule)
    side: Optional[str]        # "for" | "against" | None        } the role is
    decides: bool              # his verdict is drawn at the close } these two cells
    focus: float; reason: float; attunement: float; presence: float; grace: float; will: float
    rank: float                # his rank in the proceeding's skill (0 untrained)
    care: tuple                # (want, hold, bond) in 0..1: how much each kind of thing moves him at all
    stake: tuple               # (want, hold, bond) in -1..1: how THIS matter bears on him, toward `for`
    bonds: tuple               # ((other person, -1..1), ...): how each other person bears on him
    lean: float                # where his track starts (host: lean_step x mean(stake), plus the arrangement)
    power: float; precedence: int
    items: tuple               # the worldly matters he holds and may show (§G)
    strain: float              # carried in (A.4)
```

RD's `Speaker` (19 fields), `Decider` (12), the `hearers` tuple and `Room` (5) are this one record; `pool`,
`score`, `modifier`, `lean` as a regard number, `moved_by`, `accounts`, `operands`, `levels`, `effort` and
`reception` are gone (part 4 §G). A speaker who also decides (the man addressed in a conversation; an inquisitor
on his own bench) is one record with both cells set. Roles change inside a sitting by one rule: **a cited
testimony whose source sits in the room without a side is spoken by its source**, with his own dice, manner and
sincerity; for that beat he is the voice, the other side may press him next, and his cells are unchanged after.

### A.2 The bearing reading: one derivation, read eight ways

`bearing(person, referent) -> (want, hold, bond)`, each signed, computed from the person's **own interior only**
(F8), the same way whatever his role:

```
want = clip( sum over tags t the referent bears on:  (pursuit[t] + need[t] + 0.5 [t is a goal] + 0.5 [t is an ambition]) x bears[t] )
hold = clip( sum over t:  conviction[t] / scale_max x bears[t]  +  office.duty[t] x bears[t] )
bond = clip( tie(for-party) - tie(against-party) + faction_stance[his faction] + 0.3 [a party shares his faction] )
tie(q) = clip( relationship[q] + 0.5 [kin] + 0.5 [patron or client] + debt[q] )
care = ( strongest pursuit or need,  strongest conviction / scale_max,  strongest |relationship| )      # 0.5 where he holds none
```

`bears` is data on the referent: a `Proposition` or docket matter carries which pursuits, convictions and offices'
duties it advances if it carries; an item carries whom it comes from and whom it implicates (§G). Three channels,
and no more: what he wants, what he holds, whom he stands with.

| it is read as | by | formula |
|---|---|---|
| his **stake**: whether he comes, which side, how hard | the host, the NPC's choice of effort | `stake = bearing(p, matter)`; side = sign of its mean; `lean = lean_step x mean(stake)` |
| his **partiality** as a decider or onlooker | the start of his track | the same `lean`: a judge with a tie starts where his tie puts him, and the fold deposits that as a claim |
| the **fit** of an argument to him | the speech's leverage | `2 x care[channel] - 1` for `consequence` (want) and `authority` (hold); `bond(him, speaker) + (care.bond - 0.5)` for `solidarity`; `credit(him, item)` for `evidence` |
| the **aim** of a press on him | the press's leverage | the same function on the man pressed; `evidence` aims by what the item shows of him or of one he is bound to |
| **credit** of an item | fit and aim on `evidence` | `clip(2 x weight - 1 + bond(him, source) - max(0, bond(him, the one implicated)))` |
| **sincerity** of a speech | what an attuned listener deducts | `insincerity = max(0, -side x stake[channel])`; 1 for an item its holder knows false |
| the **cost of conceding** | the concession's step | `concede_step x (1 + max |stake|)` |
| the **verdict's effect** on him | the fold | his pursuits move by `outcome x |stake|` (§J) |

So "sincere or a ploy" (R12) has a ground truth: a speech is insincere to the degree it runs against what its
speaker himself wants or holds. The NPC's own choices read the same numbers (§F). RD's `grounds: read:` cells,
`moved_by` vector, `fit_body`, `misfit_level`, `sore_gain`, `Decider.lean`, `regard_step` in a ballot and the
`proofs` leverage source are this one reading.

### A.3 Which layers exist today

| layer | carrier in the tree | status |
|---|---|---|
| pursuits | `state/carriers.py::Person.pursuits`; `rosters.yaml: pursuits` | exists |
| convictions | `Person.conviction`; `data/affiliations.py` (scale 0 to 5) | exists |
| goals | `data/goals.py`; `rosters.yaml: goal_object_kinds`, `goal_derivations` (a goal names pursuits) | exists |
| needs | world quantities only (`rosters.yaml: hunger_bands`, `subsistence_weight`); no per-person need | `[HOOK]`: a `needs` term on the reading's `want` |
| ambitions, arcs | none (`proposals/2026-10-24-character-layers-v2.md` and siblings) | `[HOOK]`: an ambition is a `want` tag; an arc sets `care` and `strain` at the door `[UNVERIFIED: those proposals were not opened this session]` |
| relationships, regard | `Person.stance`; `person_q.stance_toward`, `regard` (derived from his ledger) | exists |
| obligations, debts | `Tenure` of kind `oblige` (`carriers.py:78`) | exists |
| kin | `Person.heritage`, `person_q.heritage_regard` (heritage, not kin edges) | partial; kin edges `[HOOK]` |
| patronage | none found | `[HOOK]` |
| office, seat | `Office` (`:1056`), `hold` Tenures, `world_q.judging_set` | exists |
| faction | `rosters.yaml: factions`; `world_q.faction_of`; `gate.seat_faction` | exists |
| era | `world_q.open_era` (a derived reading) | exists |
| strife | `rosters.yaml: strife_kinds`; `world_q`'s strife reading | exists |
| regime | none (`proposals/30_WR_*`) | `[HOOK]`: a key on the context table |

The reading is designed against what exists; a `[HOOK]` is one more term in a sum, not a carrier invented here.

### A.4 What he carries in

`strain_carried(p) = 0.5 x sum over his rattles this season, freshest first, of max(0, 1 - strain_fade x scenes
since THAT rattle) / 2^k`. Each rattle fades on its own clock and the k-th counts half the one before, so the sum
is bounded (under 1.0) whatever he is put through: no ratchet (D4). It is a derived read of his own acts'
endings, as RD §A.2 placed it; nothing is stored.

---

## B. The rite: the type's cells

```python
@dataclass(frozen=True)
class Rite:
    id: str
    live: str        # what the live thing is called: claim | offer | question | charge | motion | theme | plea
    bears: str       # who bears it: he opens
    reply: tuple     # per side: must (answer what stands, or be seen to turn away) | may | raise (nothing to answer)
    issues: tuple    # the stasis rungs it can run through, in order (B24.03's `issue_rungs`)
    concede: str     # descends (the issue is given up, the next rung opens) | accepts (it ends)
    moves: tuple     # per side, of: argue, press, rest, concede
    close: str       # bench | declared | hearers | consent | exchange (the abridged form)
    turns: int       # speeches each speaker may make
    standard: float  # the Grace the occasion expects (decorum)
    lean: float      # the venue's weight toward Reason in the dice (R11)
    admits: tuple    # the kinds of matter that may be shown (§G)
    difficulty: float; stakes: float; quorum: Optional[int]
    unrest: float    # strife: a pull on every speaker
```

The module reads these cells and nothing else about the type: it compares no row id, no move id (a move is read
by its `effect` cell: `track`, `strike`, `yield`, `none`) and no person. The eight rows are part 1 §D; their cells
are `sc2/host.py::RITES`, each `[ASSUMPTION; Jordan to correct]` as content. `abridged(row)` is any row with one
turn, the one move `argue` for the bearer, and `close: exchange`.

---

## C. The exchange

### C.1 The sitting value, the order, the beat

```python
Sitting(n, issue, points, live, tracks, cond, used, last_voice)   # the live value, returned whole
Point(id, side, issue, ground, item, by, held)                     # held: how far it stands with each listener
Cond(rattles, strain, pressed, spoken)                             # one per person
Beat(n, mover, voice, side, move, relation, issue, ground, item, point, target,
     margin, drift, evaded, insincere, rattled, moved, closed, mood, terms)
```

- **Order.** The bearer of the live thing opens; the others follow by precedence, then id. Every speaker has the
  rite's `turns` speeches; the act's effort buys turns up to the row's maximum for both sides alike (D5).
- **One live point a side.** A raise makes the mover's point the live one; older points stay in the record and in
  the tracks and can no longer be answered.
- **A track is derived, never stored as a verdict.** `track[h] = h.lean + the sum of the beats' moves on h`
  (checked on every sitting). It is each listener's own; there is no room-wide scalar.
- **The beat** is the whole narrative record: who rose (`mover`), who spoke (`voice`), on which issue, with which
  ground and which item, in what relation to what stood (`raises`, `answers`, `presses`, `concedes`, `rests`), the
  point raised or addressed, the man pressed, whether it drifted or turned away, how far it was against his own
  grain, who was rattled, whom it moved and how far, what it closed, and the room after it. No text field.
  `terms` (true values) is in the returned outcome only, never in a `View`.

### C.2 The speech: one draw, one margin per listener

A fixed 2G+5 normals are taken per exchange, used or not (G grounds: the reading's accuracy, one blur per believed
fit, one per believed aim, one for the believed strain, one for the believed mood, the hold, the speech), so a
choice never shifts the stream of the next exchange. For voice `V` on side `s`, ground `g`, item `i`, heard by `h`:

```
k        = clamp(content[g] + rite.lean - crowd_lean x crowd, 0, 1)            # R11: content and venue
pool     = pool_of(weighted_tenth((V.reason, V.presence), (k, 1-k)) + V.rank)
sigma_h  = level(fit_level) x era[g] x (fit(h, V, g, i) - repeat_step x uses(side, g or i))
         + sense_level x (2 x elab(h) - 1) x (2 x content[g] - 1)              # R12 Reason (C.3)
         + level(answer_level)  if the speech answers what stands
ob_h     = even + opposed_ob(h.will + h.rank) + manner(V)  [+ difficulty + stakes in the abridged form]
margin_h = roll_net_continuous(pool) + net_boost(sigma_h, pool) - ob_h
         - off_step x wF(h) x off  -  ploy_step x wA(h) x insincerity          # R12 Focus, Attunement (C.3)
manner(V) = manner_step x max(0, rite.standard + show x V.rattles - V.grace)   # Grace: decorum, and composure
```

One normal `z` serves every listener (`net = 0.4 pool + 0.8 sqrt(pool) z`): one speech, heard by each for himself.
The speech is composed through the one obstacle composer (B05.14's roster form), so **at control the abridged
form's margin is the plain roll** (200 of 200 keys equal in the model). The opposition is the listener's `will +
rank` at 0.4 a point, the mirror of what the pool counts, so equals stand at the even line: A-79's centre returns
(D2). Where the listener is the mover himself (a party who decides arguing his own corner) the opposition and the
fit are the other side's lead's: he must out-argue the proposer.

- **A raise** adds `s x margin_h` to each listener's track and puts a point on the table holding that strength.
- **An answer** is aimed at the other side's live point and only undoes it: with each listener it moves `min(how
  far the point stands with him, margin)` when it lands and the whole (negative) margin when it does not. It
  builds nothing of the answerer's own; it carries the relevance bonus `answer_level`.
- **Turning away.** Under `reply: must`, while the other side's point stands, anything but an answer or a
  concession is seen: a raise, a press or silence is charged `off_step x evade x wF(h)` with each listener.
- **Staleness.** Each earlier use of the same ground (or the same item) by a side takes `repeat_step` off its fit.
- **Drift.** `pull = press_pull [he was just rattled] + rattle_pull x rattles + unrest + heckle x max(0, heat)`;
  `drift = max(0, pull - (roll_net_continuous(pool_of(V.focus)) - even))`, a real number, 0 when nothing pulls.
  `off = drift + evade` where he turned away. No on-or-off flag: a speech wanders by an amount.
- **Against his grain.** `strain += grain_strain x insincerity`: arguing against what he holds wears on him.

### C.3 What each listener brings (R12), one operand each

| his attribute | Jordan's word | the one operand, in his own track | off, it reads |
|---|---|---|---|
| Reason | *"to see if argument/speech makes sense"* | his **elaboration**: `elab = clamp(0.5 + sense_step x (reason - mid) + involve x max|stake| - crowd_lean x crowd, 0, 1)`; a reasoned ground gains with him and a mannered one loses, and the reverse for a dull or uninvolved listener | slope exactly 0 |
| Focus | *"to see if it's relevant"* | `wF = (focus - floor) / (mid - floor)`: how much of a speech's drift or evasion he deducts | exactly 0 |
| Attunement | *"to see if it's sincere or a ploy"* | `wA = (attunement - floor) / (mid - floor)`: how much of a speech's insincerity he deducts | exactly 0 |
| Will | (R1: *"believe in yourself and remain confident"*) | the opposition to whatever is aimed at him: an argument he must be moved by, a press that would rattle him | not a setting: the opposed rule |

No draw is taken for any of the three: they are continuous weights on what he heard. RD's detection draw, its
`sense` re-derivation at the ballot and the decider's Reason acting a second time through `moved_by` are gone,
which is what let a dead `sense` pass (D8).

### C.4 The press, and what a rattle is

A press is aimed at the man: the last voice of the other side, or its lead.

```
sigma  = level(fit_level) x era[g] x aim(T, g, i) + room_level x heat(T)
ob     = even + opposed_ob(max(0, T.will + T.rank - T.strain / 0.4)) + manner(V) + press_ob
margin = roll_net_continuous(pool) + net_boost(sigma, pool) - ob
landed (margin >= 0):  T.rattles += 1, T.strain = 0, T is pulled on his next speech;
                       each listener moves  rattle_gain x (1 - reactance x T's earlier rattles) x (1 - max(0, bond(h, T)))
failed:                T.strain += wear;  each listener moves `rebound` against the presser
```

A rattle is the one discrete event in a sitting and it is decided by a draw, never by an accumulator crossing a
line; strain only shifts the next draw. It does four things, each with one owner: it **moves the room** at once
(and less with each repeat, then against the presser: the room will not watch a beaten man kicked); it **raises
what Grace must cover** on every later speech of his (`show`); it **pulls his next speeches** (Focus); and it is
**witnessed** (§J). Will is whether it happens; Grace is whether it shows; Focus is whether he keeps to the point
after. Nothing forces him to stop: `broken` is a derived word for a yield by a man who was rattled.

### C.5 Conceding, resting, ending

- **Concede**, where the rite says `descends` and a rung remains: the issue is closed against him; every
  listener's track is set to `his lean - side x concede_step x (1 + max|stake|)` (the dispute now turns on the
  next rung: what stood on the old one is replaced by the concession); his used grounds are fresh again. Worth it
  exactly when he is further behind than the concession costs.
- **Concede** on the last rung, or where the rite says `accepts`: the sitting ends `yielded`; under `consent` that
  is the agreement.
- **Rest**: nothing, except that silence under `must` while a point stands is turning away.
- **Ends**: `budget` (everyone has had his turns), `rested` (a whole round of rests), `yielded`. RD's `broken`,
  `struck` and `adjourned` are not ends of this module (`adjourned` is B24's bench move).

### C.6 The six, speaker side (R1, R2): one operand each

| attribute | Jordan's words (R1) | the one operand | silent when |
|---|---|---|---|
| Reason | *"constructing the argument ... logical and reasonable and evidentiary"* | its share `k` of the speech's dice; the reasoned grounds (`evidence`, `consequence`) are where it is the dice, and `evidence` is where the items he holds, including what he knows of the other side, become fit | the ground and venue put `k` at 0 |
| Presence | *"be listened to and be compelling with your delivery"* | its share `1 - k` of the dice; it grows with the crowd in the room | `k` at 1 |
| Attunement | *"what is most likely to rattle your opponent ... read the room ... what kind of argumentation is most effective"* | the accuracy of his `View`: every believed fit, aim, strain and mood is the truth blurred by `read_blur x (1 - acc) / (1 + elicit x his speeches so far)` | the room is flat (every ground the same to everyone) |
| Focus | *"staying on topic, not being pulled away"* | the hold: how far his speech drifts when something pulls | nothing pulls (a quiet room, no rattle, no heckling) |
| Grace | *"correct manner for the venue ... seen as respectable ... composed in face of difficulties"* | `manner`: the shortfall against what the venue and his own rattles demand; headroom above the standard is composure | never above the plain standard he is at or over |
| Will | *"keep arguing ... not get rattled in first place"* | the opposition to a press on him (and, as a listener, to an argument) | nobody presses him |

**Decided (rung 5), and said plainly:** in a quiet private tell between flat-interior people Focus, Attunement and
the speaker's Will have nothing to act on and read zero slope; Reason, Presence, Grace and the hearer's Will act.
RD made all six move at the tell by giving every room a standing distraction and every speech a Will discount,
which is what cost it the centre. Part 4 §I puts the choice to Jordan.

---

## D. The close

```
for each person who decides, in precedence order (one normal each):
    pool   = pool_of(mid)                                              # every decider draws on the same pool
    margin = roll_net_continuous(pool) + net_boost(track_step x track[d], pool)
             - (even + opposed_ob(mid) + rite.difficulty + rite.stakes)
close = consent:   the same margin with the draw at its mean (consent is his own move; it is never drawn)
close = exchange:  the one speech's margin against the one addressed, plus his lean
```

With an empty track on a routine matter that is A-79's centre; the sitting is the thing that moves it, through
`net_boost`'s soft cap (no clamp: more argument always counts, with diminishing return). The module returns one
`Margin` per decider. The host reads them (`act_band`): `bench`, `exchange`, `consent` the first; `declared` the
presiding seat's, demoted when fewer than `quorum` seats read Success; `hearers` the weight-mean. Never the
actor's last exchange (D6). A decider's judging skill is not read: what a good judge is, is his Reason, Focus and
Attunement (C.3), and a seat's pool with no base against an even-line obstacle was D1.

---

## E. Played: the view, the choices, the pace

```python
@dataclass(frozen=True)
class View:                      # everything a chooser has; own values true, the rest believed or public
    n: int; mover: str; side: str; issue: str; turns_left: int
    live_theirs: Optional[tuple] # (point, ground, item, believed strength against him)
    live_own: Optional[tuple]
    options: tuple               # Option(move, ground, item, relation, ev, p): his whole menu, with believed worth and chance
    own: Cond                    # his rattles, strain, speeches so far
    visible: tuple               # each speaker's rattles (public)
    mood: float                  # the room, toward him, as he reads it
    fit: tuple; aim: tuple       # per ground: believed appeal to those who decide; believed aim on the man opposite
    strain_seen: float; acc: float
```

- **What he sees.** The card (stakes, room, rules, odds as the room stands); the issue; their point and his; his
  menu with honest odds; his own condition and the others' visible condition; the room's mood. Six things to hold.
- **No leak.** The view holds no `Present`, no track and no `Beat.terms`; each believed number has its own normal
  (RD shared one per ground between two vectors, so their difference was the truth); the believed worth of an
  option is computed from believed values and an ordinary opponent, never from the true record.
- **What he chooses, per exchange:** *raise* a point (on one of three grounds, or on the proof with an item he
  holds), *answer* theirs (the same grounds), *press* the man (the same), *concede* the issue, *rest*. The model's
  first menus hold 4 to 12 options by rite and side (part 3 §B). **Before the sitting:** whether to come, what to
  bring and whom (items, a witness), the effort (turns), and, with power, how hard to rig the forum (§H);
  without it, to accept the forum, contest it on the first rung, or go to another. **After:** accept, appeal up,
  carry the grievance to another forum (§J). **To abridge:** `decide=None` is the one-click automatic policy.
- **Any role.** A played judge chooses his ruling in place of his draw `[HOOK: the host substitutes his choice for
  the close's draw; the fold deposits how far it departs from his track as a claim]` and, where the rite gives
  the bench moves, what he asks; a player in the gallery reacts as a body in the mood and may be called as a
  witness. The same entry and rules: `proceed(inp, rng, decide, deciders)` takes a callback per person, so a
  played side and an automatic side meet in one sitting.
- **Pace.** A sitting asks `turns` decisions of each speaker: 1 at the abridged form, 1 to 3 in a conversation,
  negotiation or rally, 1 to 2 at an audience, 1 to 4 questioning, 2 to 4 in a debate, 2 to 5 in a trial or
  inquisition. It pauses by returning `Sitting`; the host writes it on the case file and a later sitting starts
  from it (`Input.state`), so a player who steps in midway continues the same state.

## F. Simulated: the automatic policy is the man

With no callback the same `View` goes to `auto`, which takes the option worth most **to him**:

```
value(option) = option.ev                                             # the believed worth every chooser sees
  argue:    + grain x (2 x care[channel of the ground] - 1)           # he argues from what he himself holds
            (on the proof: + grain x (reason - mid) / 3)
  press:    + grudge x (-bond(him, the man opposite)) + pride x (will - mid) / 3 x (1 + his rattles)
  concede:  - pride x (will - mid) / 3 x (1 + his rattles)
```

Three settings, no entity named, the same menu and the same information as a player. A man of strong conviction
argues from principle, a schemer from interest, a hated rival is pressed, a proud man who has been rattled lashes
out and will not concede, a meek one gives way. Part 3 §B shows the differences by execution. An unwatched
low-stakes matter may run as the abridged form of its own row (R6: the same entry); that is the host's choice of
`form` by the act's effort, one rule, and it makes nothing unreachable: the abridged form is the first exchange of
the full one at control.

---

## G. Worldly matters: what may be shown

```python
Item(id, kind, weight, source, about, sincere)   # a typed reference to something the world holds; never text
```

`rosters.yaml: matters` (closed; it absorbs the `proofs` roster and RD's `proofs` leverage source):

| kind | carrier | who may bring it | what bringing it costs (the fold) |
|---|---|---|---|
| `record` | `Record` (`carriers.py:907`) | its holder | disclosure: everyone present now holds a claim of it |
| `testimony` | a `Claim` in the witness's own ledger | the witness, or a side that calls him | the witness speaks and may be pressed |
| `deed` | a deed `Claim` (`person_q.attributed_deeds`) | anyone holding the claim | names its source |
| `oath`, `debt` | an `oblige` Tenure | a party to it | binds the bringer again; a debt called in is spent |
| `title` | a `hold` Tenure, an `Office` | the holder | puts the title in question |
| `precedent` | an earlier matter's case-file stages | anyone who witnessed it | none |
| `law`, `treaty` | a `Record` of kind decree or covenant | anyone; a party | disclosure of a treaty |
| `rumour` | a hearsay `Claim` | anyone holding it | low weight; a known false one is a ploy |
| `state_of_realm` | `world_q`'s strife reading, `open_era` | anyone in the realm | none |
| `confession` | the conceding beat of an earlier sitting | the bench, the questioner | none |

An item is on a speaker's menu only if he holds it (own ledger) and the rite's `admits` holds its kind; a barred
kind is shown as barred on the card. It bears on each listener through `credit` (A.2): its weight, his tie to its
source, his tie to whom it implicates. So the same record is worth more to a neutral judge than to the accused's
client, a witness the bench distrusts is worth less than his testimony, and a letter that implicates a man's
patron both moves him less and aims a press at him. The evidence design's separate weight, impeachment and
forgery rules (`05_SC_evidence_and_rebuttal_B.md` `[UNVERIFIED: not opened this session]`) reduce to: origin sets
`weight`; impeachment is an answer; a forgery is `sincere: false` on its holder.

## H. Arrangement: the type is a power act

```
tilt = rig x max(0, tanh((power(arranger) - power(other party)) / power_scale))        # 0 fair .. 1 rigged
power(p) = his office's rung + 2 x level(its modifier) + the regime's weight for his authority
```

`rig` is the arranger's one choice (fair 0, firm 0.5, rigged 1). `tilt` moves the cells of the row inside its
ranges, all in the host builder: the bench is packed (a share `tilt` of the seats least tied to him is dropped);
the floor is closed at high tilt; turns are cut toward the row's minimum; those who decide start `presume_step x tilt` toward him; and those merely watching start
`sympathy_step x tilt x (1 - their tie to him)` against him. The check on power is in the same numbers: a rigged
forum is seen by whoever is in it (a `rigged` claim each, a legitimacy write scaled by how many saw, an appeal
docketed for the loser: §J), so closing the floor hides the rigging and loses the crowd's weight, and leaving it
open keeps the crowd and pays the legitimacy. Between equals `tilt` is 0 whatever `rig` says.

This replaces RD's `presumes`, the `scripted` order, `case_rows` and `row_for_case` (a static table two of whose
rows were unreachable): the convener names a lawful row for his authority and arranges it. The weak party's
options are acts that already exist: come and play the hand, contest the forum (a point on the first rung, where
the row's ladder has `procedure`), appeal up after (R-35), or take the matter to another forum. `[UNVERIFIED: the
existing `convene`, `open_case` operand channel (H-80) and P10 forum challenge were not opened; the rule needs
only that the arranger and `rig` reach the builder.]`

## I. Context: era, regime, strife

`arrangements.yaml: context`, read by the host builder into the rite's cells and the persons' reading; no code per
era, regime or strife kind:

| layer | cells it moves | example rows in the model |
|---|---|---|
| era | the weight of each ground (`era[g]` on fit and aim) | an age of faith weighs `authority` 1.4 and `consequence` 0.8; a mercantile age the reverse |
| regime | which rites are lawful; `standard`; `lean`; kinds added to or dropped from `admits`; the weight of each authority in `power`; the floor | a theocracy bars `debate`, raises the standard, admits `confession` and `oath`, drops `precedent`; a commune bars `inquisition`, opens the floor, admits `rumour` |
| strife | `turns` (urgency), `unrest` (a pull on every speaker), `stakes`, what the hungry want (`care.want`), who is absent | war: one turn fewer, unrest 0.5, stakes 0.5; famine: unrest 0.75, wants sharpened |
| office, seat | `precedence` (order), `power` (arrangement), `office.duty` (his `hold`), who sits | the bench is `judging_set` filtered by the seats' own faction (part 4 §H names the real chain) |
| faction | `bond` (stance on the matter; a shared faction with a party), the authority a row carries | a decider of the respondent's faction starts toward him |

**Out** (the fold, §J): a faction's standing and legitimacy, a strife eased or inflamed, an office contested, a
precedent that later sittings can show, a matter docketed in turn. **Convening:** a strife or regime event
becomes a matter on a docket by the acts that exist (`open_case`, `convene`); in the model's three seasons a
famine above a level convenes a motion to remit the tolls, whose outcome moves the famine.

## J. Disposal: what a resolution writes

`arrangements.yaml: disposal`: `(what the row disposes, band) -> typed writes`. The module returns margins and the
record and writes nothing; the host grades on the one ladder and the fold performs the row.

| disposes | Overwhelming | Success | Partial | Failure | impasse / adjourned |
|---|---|---|---|---|---|
| `none` (conversation, questioning, rally, the tell) | pursuits moved, regard up, a claim that he was converted | pursuits moved, regard up | regard up | regard down, a grievance docketed | the record only |
| `oblige` (negotiation, audience, arbitration) | an `oblige` Tenure, regard up, a precedent | an `oblige` Tenure | adjourned to the docket | a grievance; the matter may go to another forum | adjourned |
| `detain` (trial) | a `detain` Tenure, his office contested, a precedent | a `detain` Tenure, a precedent | an `oblige` Tenure (surety), adjourned | an acquittal on the case file, a precedent, the accuser's regard down | adjourned |
| `ban` (inquisition, tribunal, excommunication) | a `ban` Tenure, office contested, a precedent | a `ban` Tenure | surety, adjourned | an acquittal; the arranger's legitimacy down | adjourned |
| `decree` (debate) | the decree entered, the mover's faction up, a precedent | the decree, faction up | adjourned | the motion recorded defeated, faction down | adjourned |

Every sitting, whatever its band, also leaves (from the beats alone): the stage on the case file; to each person
present a claim of each rattle, each item shown, each concession, each speech an attuned man saw to be insincere
(*hypocrite*), each decider's partiality (*partial*), and a rigged forum (*rigged*); regard from the man pressed
toward the presser, from the man testified against toward the witness, from loser to winner (more when rigged);
each hearer's regard and pursuits moved by how far his own track travelled; each party's pursuits moved by
`outcome x |stake|`; the rattles as strain carried; the matter's strife eased or inflamed; an appeal docketed
where a rigged forum was lost. So a loss is a place to go: a grievance, an appeal, another forum, a grudge, and
the precedent the next sitting can show. **A conviction is never written** (A-92, `04:251`): the proceeding
deposits claims, and a conviction moves only in the person's own later drawn act (**rung 3**).

Owners of the writes `[UNVERIFIED against `engine/season/state/write_matrix.yaml`, which was not opened]`: the
Event `ending` and the case-file stage are B24p.20's and B24.14's; Tenures of `oblige`, `detain`, `ban` are
`determine`'s existing effect (`_disposal`) and B24.08's; claims to witnesses are WITNESS's deposit (B24p.22);
regard and pursuits are B27's (`argued_pursuits`, `consequence_pursuits` exist in `person_q.py`); offices are
BA1's; obligations B28's; faction standing, legitimacy and strife are B33's.

## K. The settings

Thirty-eight of the proceeding's own (RD: 53 plus three tables), every one `[ASSUMPTION; Jordan to correct]`; each
moves outcomes over the model's battery (none inert). Basis in brackets.

| group | settings (shipped) |
|---|---|
| the speech | `fit_level` strong [a full fit is one strong level]; `answer_level` moderate; `repeat_step` 0.35; `sense_level` 0.5, `sense_step` 0.15 [Reason 1 to 7 spans elaboration 0.05 to 0.95], `involve` 0.3; `manner_step` 0.5 [half an obstacle a point of Grace short], `show` 1.0; `off_step` 1.0, `evade` 1.5; `ploy_step` 1.5, `grain_strain` 0.5 |
| the press | `press_ob` 1.25 [a man is harder to shake than a point is to make: about one press in three lands between equals], `press_pull` 1.0, `rattle_pull` 0.5, `wear` 0.5, `rattle_gain` 1.5, `rebound` 1.0, `reactance` 0.75, `room_level` 0.5, `heckle` 1.0 |
| conceding | `concede_step` 2.0, `consent_at` 2.5 |
| the room and the reading | `crowd_at` 12, `crowd_lean` 0.2, `mood_scale` 5, `read_scale` 1, `read_blur` 2, `elicit` 0.5 |
| the close | `track_step` 0.2 [a track of 3 reads 49 % carried, 6 reads 66 %, 12 reads 79 %, on a routine matter] |
| the NPC | `grain` 1.5, `grudge` 1.5, `pride` 1.0 |
| the host | `lean_step` 2.0, `presume_step` 2.0, `sympathy_step` 1.5, `power_scale` 2.0, `strain_fade` 0.5 |

Tables that are content: the four grounds' `content` (0.8, 0.7, 0.4, 0.2: RD's), the rows' cells, the context
rows, the disposal rows. Controls: `fit_level`, `answer_level` at none and `repeat_step`, `sense_level`,
`manner_step`, `off_step`, `ploy_step`, `grain_strain`, `lean_step`, `crowd_lean`, `heckle`, `room_level` at 0.
The centre is B05's `difficulty_ob`: at its shipped `routine` 0.5 the tell reads the figures of part 3 §B.

## L. The precedent map

Each mechanism against its source, the passage opened this session, the source's own grade, and what the design
does with it. `PM` = `research/social_contest_procedures/03_persuasion_mechanisms.md` (its *Engine:* lines are its
author's assumption and are not used); `RO` = `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md`;
`NP` = `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md`.

| mechanism | source and passage | the source's grade | follows, adapts or departs |
|---|---|---|---|
| the grounds are the three means: logos (`evidence`, `consequence`), pathos (the listener's `want` and `hold`), ethos (`solidarity`: who the speaker is to him) | Aristotle's pisteis: `RO:76`; `NP:26-28` | `RO:47` web-verified that session; `NP` `[T2]` ethos, `[T1 — SEP]` logos | **adapts**: four grounds under three means; and **departs** on ethos, which `NP:26` says Aristotle places in the speech itself, not in prior standing: here it is the listener's tie to the speaker, because the world holds that and the speech has no text |
| the families of type are the genres: who judges and what they decide | `RO:77`; `NP:32` | as above; `[T1 — SEP]` | **follows**: judicial (trial, inquisition, questioning), deliberative (debate, audience), epideictic (rally); the dyadic rows have no classical genre |
| an argument is aimed at those who decide, not at the opponent | `RO:337` | the file's synthesis table | **follows**: the opposition is the listener's; the opponent answers with his own speech |
| the issue ladder is stasis | Hermagoras, Cicero: `RO:90`, `RO:99`; v30's start by proceeding, `.designs/systems/social_contest/reference/social_contest_v30.md:56-68`, `:107-112` | web-verified spine; v30 ratified at Gate C | **adapts**: the rungs are B24.03's `issue_rungs`, a row lists which it runs through, and conceding descends |
| raise and answer are confirmatio and refutatio | the six parts: `PM:23`; `NP:44-46` (*"a turn structure, not a template"*) | primary-text citations by the file; `[T1]` | **adapts**: two of the six are relations of a beat; exordium, narratio, partitio and peroratio give no decision and are **cut** as mechanisms (first and last beats are rendered so) |
| prove, please, move | Cicero's duties: `PM:15`; `NP:48` | `[T1 — Quintilian]` | **not a mechanism**: the grounds already are these; a third choice an exchange was refused (game first) |
| the venue's standard met by Grace is decorum | Quintilian: `PM:43`; `NP:50` | primary-text citation | **follows** |
| fit reads what the listener already holds | the enthymeme as a move on a held premise: `PM:66` | primary-text citation | **follows** |
| elaboration: the able and involved weigh the case, the rest go by manner | ELM: `PM:137`; `NP:62-71`; N3 `NP:231` | published (Petty and Cacioppo 1986) | **follows**: Reason (able), stake (involved), crowd (lowers it) |
| the room recoils from a repeated press | reactance: `PM:135`; `NP:110`; N5 `NP:248`, `:253` (*"without reactance, pressure is monotonically good"*) | `PM`: `[FROM MEMORY, UNVERIFIED]`; `NP`: `[T1 — standard; not re-verified]` | **adapts, lightly**: one setting on the rattle's gain; because the source is memory-grade nothing else rests on it |
| the reading sharpens as he engages | elicitation: `proposals/2026-09-05-proceedings-subsystem/01_THE_STUDY.md:113` (*"the one positive result in twenty-five experiments — perspective-getting, not taking"*) | that study's own finding | **adapts**: `elicit`; RD's free reading stays (R1), but it is no longer equally good at the first exchange and the last |
| the bearer opens and holds the initiative | first offers anchor: `NP:118` | `[T0 — Galinsky and Mussweiler 2001]` | **consistent, not built**: an offer's terms are B24.30's; the model shows a residual opener's edge (part 3, D5) |
| inoculation | `PM:136`; `NP:112` | `[FROM MEMORY, UNVERIFIED]` | **cut**: no decision beyond raising |
| deliberation among deciders (N10) | `NP:276` | the adjudication ranked it top | **not built** (rung 1: A-14 makes each verdict the voter's own draw; no ruling asks for rounds) |
| attribution (N16), composition (N19) | N12 to N16 rest on a paraphrase of a paraphrase (RD §F.6's note) | weak | attribution is the beat (who said what, witnessed); composition is raise and answer; nothing more is built on them |
| a judgement formed item by item | the story model: `NP:101` (*"a model that forces item-by-item judgment produces a different decision process"*) | `[T1]` | **departs, knowingly**: a track is item by item; a story model would be a second resolver |

## M. The verbs, and the seam

RD §D stands: `argue`, `interrogate` (and `covenant`, `interview`, `determine` at their own items) open the full
form, `tell`, `lie`, `speak` the abridged, by a `proceeds:` cell; a lie is an `argue` that shows an item its
holder knows false (there is no `deceive` move). `proceed(inp, rng, decide=None, deciders=None) -> Outcome(beats,
state, ended, ended_by, verdicts)`; `closing_odds(inp, state)` is pure. The module keeps no state, grades no band,
names no side as winner, writes nothing (Layer 1 `04` §A.2, G.1.5).
