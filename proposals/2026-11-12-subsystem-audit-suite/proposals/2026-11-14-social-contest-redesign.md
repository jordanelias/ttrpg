# SC · DICE — the social contest redesigned: a proceeding is a run of exchanges, and each of the six attributes acts in the manner Jordan stated (part 1: the model and the six roles)

Written: 2026-11-14, stage 2 of three (1: the interrogation of the code, done; the collation of what was designed and is
missing, done; 2: this redesign, with build instructions and a fold map; 3: a Sonnet lane applies the fold map to workplan
v12). Read at the working tree of branch `exec/v12-b00-b03` on 2026-11-14, HEAD `1257a4a` (B01a.06 landed: the Spirit key
is `attr.spirit.will` in `references/descriptor_registry.yaml:51` and in `descriptors.ATTRIBUTES`, so INT E-7 and COL §4
item 8 are closed in the tree). Authored by a Fable lane on Jordan's direction
(a recorded departure from CLAUDE.md §10's "fable: not artifact authorship"; `STAGES.md` notes it). Nothing outside these
files was edited; no commit; the probes named in the text ran with `PYTHONHASHSEED=0`.

**Parts, in reading order:** this file (the head; §A the model; §B the six roles); `_part2.md` (§C the proceeding types as
data; §D the verbs); `_part3.md` and `_part4.md` (§E the build items); `_part5.md` (§F the fold map; §G what was not
decided).

**Depends on:** Jordan's rulings R1 to R11 (`2026-11-14-social-contest-jordan-rulings.md`, the contract; R11, the blend of the dice, folded 2026-11-14 after stage 3); stage 1
(`2026-11-14-social-contest-attribute-interrogation.md`, cited as INT); the collation
(`2026-11-14-social-contest-collation.md`, cited as COL); B01a (drawn attributes, `engine/season/harness/pairs.py`); B04
(the skill surface, `pool_of`, `opposed_ob`, `even_line`); B05 (the one continuous sampler, the obstacle roster, the signed
leverage channel); B06 (`engine/dice_engine/draw.py::Draw`); B07 (the rooms an act is heard by).
**Lands in batch:** a NEW batch, `B24p-sc-proceeding` (lane SC, step S12, before `B24-sc-hearing`), with edits to items of
B01a, B05, BA1, B24, B24a, B27, B28 and B98 (§F).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: it describes a design and the code it would become; it is not a mechanism
and nothing reads it at runtime. Every source under `.designs/`, `.audit/`, `research/` and `proposals/` is cited for
INTENT only. Lanes owning the files the build items edit: SC (`modules/social_contest/`), IN (`engine/season/`), DICE
(`engine/dice_engine/`).

Markers: `[ASSUMPTION: ... — basis]` a choice the sources do not settle; `[ASSUMPTION; Jordan to correct]` on every shipped
value; `[NEW]` a mechanism in no earlier source, with its reason; `[UNVERIFIED]` a claim not opened or not run. Primitive
ids: **N1 to N20** (`.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md` §4,
`sources/05_persuasion_in_the_era_sources.md` §2), **M1 to M14** (`sources/03_consolidation.md` §2), **P1 to P45**
(`sources/01_political_mechanics_primitives.md` §4); **v30** is
`.designs/systems/social_contest/reference/social_contest_v30.md`; **P4** is
`proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-proposal-4-authority-staged.md`; **K/** is
`systems/social_contest/sim/contest/`; **HEAR_B** is the suite's `05_SC_playable_hearing_B.md`; **wp** is
`master/workplan_v12/workplan_v12_`.

**The redesign in brief.** (1) One module entry, `social_contest.proceeding`, runs every proceeding: a run of exchanges
between sides, then a close in which each decider is balloted. The single roll stays the unit: an exchange is one
continuous draw with three more beside it (a reading, a hold, the pressed side's steadiness). (2) `tell`, `lie` and `speak` call the same entry under
a one-exchange type row whose close is that exchange's own margin: no second path (R6). (3) Each attribute has its own
operand: the dice of a speech are a blend of Reason and Presence, weighed by what the speech says and where it is said
(R11, B.2); Presence besides is leverage and the share of the speech that is heard; Attunement is the
accuracy of the reading the speaker chooses his ground and his target by; Focus is the hold against being drawn off the
topic; Grace is the shortfall against what the venue demands, the esteem he holds in the room and the cost of a rattle; Will is
the resistance to a rattle, the length a side can keep arguing and the discount on everything that counts against it (R1,
R2). (4) A proceeding type is an `arrangements.yaml` row; the nine rows gain five keys and four rows are added, and every
computed case names a row (R4). (5) The module keeps no state: a sitting's record is returned and the host writes it on the
Event and, for a docketed matter, on the case file (Layer 1, `04` §A.2).

---

## A. The model

### A.1 The words, one meaning each

| word | means | owner in code (after the build) |
|---|---|---|
| **proceeding** | a run of exchanges between sides, before an audience and deciders, at a venue, on a topic, under a proceeding type; Jordan's *"a proceeding is a social contest is a run of exchanges"* (R6) | `modules/social_contest/proceeding.py::proceed` |
| **sitting** | one call of the entry: one meeting of a proceeding (the plan's word, wp `part22.md:9`) | the same call |
| **exchange** | one speech by one side: one choice (a move and a ground), four draws taken in a fixed order (the reading, the hold, the speech, the other side's steadiness), one record | `proceeding.py::_exchange`; `queries/inputs.py::Exchange` |
| **side** | `for` (the side that put the proposition) or `against`; one speaker leads each | `queries/inputs.py::Speaker.side` |
| **topic** | the proposition the proceeding is about (a `Proposition` id or a docket matter), with the live *issue* where the type has an issue ladder | `queries/inputs.py::ProceedingInput.topic` |
| **move** | the kind of speech an exchange makes (`argue`, `press`, `divert`, `concede`, `rest`, and the evidence and bench moves B24 adds) | `rosters.yaml: proceeding_moves` |
| **ground** | what an argument appeals to: `evidence`, `consequence`, `authority`, `solidarity` (the four the tree already seats as hearer dispositions, wp `part22_cont.md:120`; v30's armature axes, `:182-188`); each names a content class, which weighs the speech's dice between Reason and Presence (B.2 a) | `rosters.yaml: grounds` |
| **content class** | what kind of content a speech is (`evidentiary`, `logical`, `procedural`, `appeal`, `emotional`), carrying the weight `w_reason` of Reason in its dice, the rest Presence (R11) | `rosters.yaml: content_classes` |
| **decider** | a person the close ballots: a bench seat, the one a speech is addressed to, a hearer in a crowd | `queries/inputs.py::Decider` |
| **audience** | the persons present who are not speakers; the type row says what kind it is, and its hearers are deciders only where the row says `disposal: hearers` | `arrangements.yaml: audience_kinds`; `ProceedingInput.hearers` |
| **proceeding type** | one row of `arrangements.yaml`: the parameters R4 lists | `data/arrangements.py` |
| **strain**, **mark** | strain is the pressure a side has taken in this sitting; a mark is a rattle: strain crossed the side's threshold once (v30 §4 Step 6, recast in levels) | `queries/inputs.py::SideState` |
| **resolve** | how much longer a side can keep arguing in this sitting (Will) | `SideState.resolve` |
| **track** | the running position of the proposition before the deciders, a signed real number, positive toward `for` | `ProceedingOutcome.track` |

"Round" is not used (A-101 reserves it for a fight). "Hearing" names a proceeding before a bench only.

### A.2 The module, and where the state lives (Layer 1)

`04` §A.2 gives a registered module one shape: a typed input in, a typed outcome back, no `World`, no token, no state kept
between calls; `roll.py:10-14` says it of the live entry. The proceeding keeps that shape, on the fight's precedent
(`queries/inputs.py:165-196`: `CombatTurnView`, `PlayHost`): the entry runs every exchange of one sitting inside one
call, calls a decider it is handed for each choice, and returns.

```python
# modules/social_contest/proceeding.py
def proceed(inp: ProceedingInput, rng, decide: Optional[Callable[[ExchangeView], Choice]] = None) -> ProceedingOutcome
def closing_odds(inp: ProceedingInput, state: ProceedingState) -> tuple   # pure: per decider, the four band shares; no draw
```

- `rng` is the act's own keyed `Draw` (B06.03: `engine/dice_engine/draw.py::Draw`), built by the host from
  `draw_factory(world_seed, tick)(actor, "roll:<prize>:<act id>")` (`loop/resolve.py:833`) and passed in. The module
  constructs no generator. Every sitting is reproducible from its key.
- `decide` is `None` for an automatic sitting (the module's own drawn policy, A.6) and the host's decider otherwise
  (`PlayHost.deciders["social_contest.proceeding"]` for a played person, the NPC decider B24.13 builds for the rest).
- The module imports `engine.dice_engine` and the record types in `engine/season/queries/inputs.py` (the leaf a module may
  import, `inputs.py:12-15`), nothing else.

**The state a contest carries is a value, never a module field.** Three places hold it:

| state | lifetime | where it lives | who writes it |
|---|---|---|---|
| the sides' strain, marks, resolve, hold and esteem in the room; the track; the exchange list | one sitting | local variables of `proceed`, returned whole as `ProceedingOutcome.state` (a frozen `ProceedingState`) | nobody outside the call |
| the sitting's record: the exchanges, each side's end state, the track, how it ended, the ballots | permanent | **the Event's `ending`** (`state/carriers.py:313`, the tuple a fight's ending already uses; B05.18 puts the social roll's record there) for every proceeding; and **the case file's `Record.stages`** for a docketed matter (B24.01 `case_file_of`, B24.14) | the fold (`loop/resolve.py::_fold`), under the verb's own token, from the outcome |
| what a later sitting of the same matter starts from: the track, the live issue, the standing items | between sittings | the case file's stages; the host builder reads them back into `ProceedingInput.state` | the same write as above |
| what a person carries out of the room: that he was rattled | to the season's end | nowhere new: `person_q.strain_carried(w, p)` reads his own acts' `ending` records of this season, as the practice addend reads his own acts (`sigma.py:306-307`) `[NEW; reason: S-7 (COL §8 row 21) forbids a stored standing number, H-335 needs a repeated argument to cost something; a derived read meets both]` | nobody |

So the carrier named is **the Event's `ending`**, with the case file as the durable copy for docketed matters. No new
`Person`, `Scene` or `Question` field is added, and no `write_matrix.yaml` row for a new field.

### A.3 The records

All in `engine/season/queries/inputs.py`, frozen, stdlib only. B24.05 planned seven hearing records; the proceeding's
records are those seven generalised, so B24.05 adds only the exhibit and the board fields (§F).

```python
@dataclass(frozen=True)
class Speaker:                 # one side's lead: a party, an advocate, an orator, a teller
    id: str
    side: str                  # "for" | "against"
    focus: float               # the six attributes, raw, as Person.attributes holds them (B01a)
    reason: float
    attunement: float
    presence: float
    grace: float
    will: float
    ranks: tuple               # ((skill id, rank), ...) for the skills the type's moves name; () untrained
    addends: int               # the pool addends (practice), as pool.py::POOL_ADDENDS sums them
    score: float               # his skill score in the proceeding's skill: what an opponent's draw is opposed by (A-79)
    proofs: float              # what he can show against the other side (world_q.proofs, raw)
    accounts: tuple            # the names of the other side's circumstance terms he holds a claim about (B.2)
    precedence: int            # the rung ordinal of his highest seat, 0 with none (order: rank)
    effort: int                # exchanges he is prepared to spend: his act's effort plus one
    levels: tuple              # ((source, sigma for, sigma against), ...) from the host's advantage sources (office, ...)
    operands: tuple            # ((name, raw, step, eased_by), ...): the host's obstacle operands on his speeches (B.7)
    moved_by: tuple            # ((ground, weight in [0, 1]), ...): what moves HIM, true values (B.3)
    strain: float              # strain carried in (A.2, last row)

@dataclass(frozen=True)
class Decider:                 # a person the close ballots (B24.05's `Seat`, generalised); also a hearer
    id: str
    weight: int                # Person.weight: a cohort counts as its weight
    pool: float                # his own dice for the ballot: a seat's judging pool, else the base
    score: float               # the skill score that opposes a speech to him and his own ballot: his own; a seat's is the respondent's
    grace: float               # raw; how little he gives away to a reader (B.3)
    attunement: float          # raw; his resistance to a `deceive` (C.4: the move's `resisted_by`)
    will: float                # raw; his resistance to being carried (B.6)
    lean: float                # signed sigma he arrives with (a seat's commits, B24.11; a hearer's regard)
    modifier: Optional[str]    # the seat's office level, a LEVEL_SIGMA name (B05.20), else None
    moved_by: tuple            # ((ground, weight), ...), true values

@dataclass(frozen=True)
class Room:                    # who is present, as the speech meets it (C.5)
    audience: str              # a member of arrangements.yaml: audience_kinds, computed from who is there
    attention: float           # what this audience demands before it listens, in points of Presence (B.4)
    distraction: float         # the room's own pull off the topic, in obstacle units (B.1)
    proof_weight: float        # how far this audience weighs proof against manner, in [0, 1] (B.2, B.4)
    reception: tuple           # ((speaker id, signed regard of the room for him), ...): world_q.reception, raw

@dataclass(frozen=True)
class Move:                    # one row of rosters.yaml: proceeding_moves, handed in (the module holds no roster)
    id: str
    draw: bool                 # does it roll a speech
    capability: Optional[str]  # the skill whose rank joins the case
    resisted_by: Optional[str] # "will" | "attunement": which attribute of the one addressed resists it (B.6 d)
    ground: bool               # does it take a ground
    fit: bool                  # does the ground's fit to the target count as leverage (B.3)
    holds: bool                # does it carry its own pull (a false story, C.4)
    effect: str                # "track" | "strike" | "pull" | "yield" | "none": what it does when it lands (A.4 step 5)
    reason_weight: Optional[float]  # a groundless drawing move's content weight toward Reason, its content class's
                               # `w_reason` (B.2 a); None on a move that takes a ground (the ground's class decides)

@dataclass(frozen=True)
class ProceedingType:          # the arrangements.yaml row, as the module reads it (C.2)
    id: str
    disposal: str              # bench | declared | mutual | hearers | exchange | none
    order: str                 # alternating | rank | scripted | single
    exchanges: tuple           # (min, max) exchanges in one sitting
    moves: tuple               # ((side, (Move, ...)), ...): what each side may do, from the row's rite
    standard: float            # what the venue demands of manner, in points of Grace (B.5)
    difficulty: float          # the type's difficulty level, already sized (B05.14 difficulty_ob)
    stakes: float              # the obstacle term of what the close disposes (B05.21 stakes_ob), 0 with none
    presumes: str              # "for" | "against" | "none": which side the proceeding presumes for (C.1)
    reason_bias: float         # the venue's lean of a speech's dice toward Reason (+) or Presence (-), in tenths (B.2 a, C.1)
    quorum: Optional[int]
    break_at: int              # marks at which a side cannot go on
    strikes: int               # off-topic speeches after which a side's off-topic speech counts for nothing; 0 = never

@dataclass(frozen=True)
class ProceedingInput:
    type: ProceedingType
    topic: str                 # the Proposition id or docket matter
    issue: Optional[str]       # the live issue, where the type has an issue ladder (B24.03), else None
    speakers: tuple            # one Speaker per side that speaks (one for an address, two for a contest)
    deciders: tuple            # Decider, ...: who the close ballots, in id order; () under exchange and none
    hearers: tuple             # Decider, ...: the audience present (they may equal `deciders` under `hearers`)
    room: Room
    grounds: tuple             # the members of rosters.yaml: grounds, in roster order (the module holds no roster)
    ground_reason: tuple       # ((ground, w_reason of its content class), ...) in roster order (B.2 a)
    dials: Mapping             # every setting the formulas read, by name (Fixtures values; the module holds none)
    state: Optional["ProceedingState"] = None   # a resumed sitting's start, else None

@dataclass(frozen=True)
class SideState:
    id: str
    strain: float              # pressure taken this sitting, in margin units
    marks: int                 # rattles
    resolve: float             # what is left of his staying power, in exchanges
    pull: float                # the pull on his next speech (B.1); 0.0 when none
    strikes: int               # speeches he has made off the topic
    esteem: float              # how he is regarded in the room, signed sigma (B.5); never stored past the sitting
    read: tuple                # what he believes of the other side and the room: ((key, value), ...) (B.3)

@dataclass(frozen=True)
class ProceedingState:
    n: int                     # exchanges run
    track: float               # signed, toward `for`, in margin units
    issue: Optional[str]
    sides: tuple               # SideState, ... in speakers' order

@dataclass(frozen=True)
class ExchangeView:            # what a decider is shown before he chooses; never the other side's true values
    n: int
    mover: str
    legal: tuple               # the move ids he may make now
    own: SideState
    read: tuple                # his reading: believed grounds of each target, believed sore ground, believed strain
    track_sign: int            # -1, 0, +1: which way the room stands, which anyone present can see
    issue: Optional[str]

class Choice(NamedTuple):
    move: str
    ground: Optional[str]      # for a move that argues; None for rest and concede

@dataclass(frozen=True)
class Exchange:
    n: int
    mover: str
    move: str
    ground: Optional[str]
    on_topic: bool
    margin: float              # the speech draw's real margin (net + boost - ob)
    terms: tuple               # the obstacle's named terms ((name, value), ...), summing to ob (B05.14's form)
    levels: tuple              # ((source, for sigma, against sigma), ...) as they entered the draw
    strain: float              # strain dealt to the other side by this exchange
    marked: bool               # the other side took a mark

@dataclass(frozen=True)
class ProceedingOutcome:
    exchanges: tuple           # Exchange, ...
    state: ProceedingState     # the end state
    ended: str                 # a member of rosters.yaml: proceeding_ends
    verdicts: tuple            # ((decider or target id, Margin), ...): each a net/ob pair, never a band or a side
```

`Margin` is the tree's own (`inputs.py:104-115`). `verdicts` holds margins, so the host grades each on the one ladder
(`seam/ladder.py::degree_of`) and the module names no winner; the adapter refuses any other return, as `sigma.resolve`
does today (`sigma.py:579-586`).

### A.4 One exchange

The mover is `S`, with state `s`; the other side is `T` with state `t` (for a one-speaker type, `T` is the weight-mean of
the deciders, built by `_target`). A fixed number of normals is taken from `rng` on every exchange, used or not, in this
order: the reading's (one for its roll, one per ground, one for the other side's state), the hold's, the speech's, the
steadiness draw's: `G + 5` for `G` grounds, nine at the shipped four. So a choice in one exchange never shifts the stream of
the next `[NEW; reason: B06's keyed draw makes a stream a function of its key and ordinal; a fixed count per exchange keeps
exchange k at the same ordinals whatever was chosen before]`.

| step | what happens | role | where defined |
|---|---|---|---|
| 1 | **The reading.** `S` reads the room and `T`: the first normal settles how exact his reading is; `s.read` is the true dispositions blurred by the error | Attunement | B.3 |
| 2 | **The choice.** `decide(view)` returns a `Choice`; with no decider the automatic policy takes the legal move and the ground his reading scores highest | (Attunement, through the reading) | A.6 |
| 3 | **The hold.** If a pull stands on `S` (`s.pull > 0`, from the other side's last `divert` or `press`, plus the room's `distraction`), the second normal settles whether he keeps to the topic; if not, the speech is off the topic | Focus | B.1 |
| 4 | **The speech.** The third normal is the speech draw: `margin = roll_net_continuous(pool) + net_boost(sigma, pool) - ob`, with the pool from the case (a blend of Reason and Presence by the ground's content and the venue, R11), `sigma` from delivery (Presence), fit (the ground against the target's true dispositions), esteem (Grace) and the other sources, the levels against scaled down by Will, and `ob` from the difficulty, the opposition, the venue's standard (Grace) and the hostile room | Reason, Presence, Grace, Will | B.2, B.4, B.5, B.6 |
| 5 | **The effect**, by the move's row: `argue` moves the track by the margin; `press` lands a blow on `T`, heavier on the ground he is most invested in, and `T`'s steadiness draw (the last normal) settles whether he takes a mark or carries the strain; `divert` sets a pull on `T`'s next speech; `concede` yields the issue; `rest` does nothing | Will, Grace | B.5, B.6 |
| 6 | **The cost of staying.** `s.resolve` falls by one exchange and by what the exchange cost him; at zero he yields | Will | B.6 |
| 7 | The `Exchange` record is appended | | A.3 |

No step grades a band: the speech draw's margin is used as a real number, so nothing inside a proceeding is a flat
threshold (R8). The one ladder is read once, by the host, on each verdict margin.

### A.5 Order, ends and the close

**Order** (`ProceedingType.order`; `arrangements.yaml: order`, read by nothing today, INT §G.1):

| value | who speaks |
|---|---|
| `free` | whoever has the most effort left speaks next, ties to `for`; with one speaker (an address: a rally, a sermon, a plain word) that is him every exchange. The value exists in the loader's enum and no row uses it (`data/arrangements.py:64`) |
| `written_only` | as `free`, and the speech is a document: delivery counts for nothing and all of it is heard (B.4); P4 §3.2's *"a written petition weighs no eloquence"*. In the enum, unused today |
| `alternating` | the sides in turn; `for` opens (it bears the proposition) `[ASSUMPTION: who opens — basis: the burden; v30 rolled it on Attunement (`:276-280`), which COL §8 row 4 records as superseded by the row's `order`]` |
| `rank` | the speakers by `precedence`, highest first, ties by id; then again in the same order |
| `scripted` | as `alternating`, with `for` (the questioner, the accuser, the inquisitor) holding every move and `against` held to the moves the rite allows the respondent (`answer`, `concede`, `rest`, and `argue` where the rite says): the asymmetry of v30 §7 `:398-402` carried as a move set, not a halved number |

**Ends** (`rosters.yaml: proceeding_ends`, closed): `budget` (the type's maximum reached, or every speaker's `effort`
spent), `rested` (every side rests in turn), `yielded` (a side's resolve reached zero, or it conceded the last issue),
`broken` (a side's marks reached `break_at`), `struck` (a side's off-topic strikes reached the type's `strikes` where that
ends it), `adjourned` (a bench move, B24). An end is never a verdict: `yielded`, `broken` and `struck` enter the close as
levels against the side concerned (`yield_level`, `break_level`), never as an automatic loss, which is HEAR_B's rule for
`silence` (`:128-137`) and its falsifier (*"if a fault can be shown to fix the band ... the module has named a winner"*,
wp `part22.md:211`).

**The close**, by `disposal` (the verdict system; one key, extended by two values, C.1):

| `disposal` | who is balloted | how the host reads the ballots |
|---|---|---|
| `exchange` | nobody: the last exchange's own `Margin` is the verdict, against its target | one band, folded as the verb row's `writes_at` and `emits_at` say: today's `tell`, `lie`, `speak` |
| `bench` | the presiding seat (the first decider) | one band: `determine`'s (B24.08) |
| `declared` | every seat | votes for at Success or better, against at Failure, an abstention at Partial; under `quorum` the provider sets a veto, which can only demote (B24.11; `04` §C.5) |
| `mutual` | nobody: consent is the other party's own move (`accept`, B24.30), never a draw (NEG's falsifier: *"consent decided by a draw"*, wp `part22_cont.md:35`) | an `accept` ends the sitting agreed and each party's `oblige` is opened by his own act (B24.31); no `accept` is an impasse, a legitimate ending (R-1, COL J07). The track, his strain and his resolve are what each party's decider weighs |
| `hearers` | the one addressed and every hearer the floor admits, each for himself | each carried hearer's pursuits move toward the speaker's on the topic; what the crowd then does is each hearer's own later act (R-29's *consent, not command*, COL J06) `[NEW value; reason: R4 names "rallying a crowd" and no existing value lets an audience decide]` |
| `none` | nobody | no verdict; the track and the sides' end states are the record (B32.15's `acclamation`) |

A ballot is one continuous draw on the decider (A-14: *"a draw on the voter"*):

```
ballot(d) = Margin(net = roll_net_continuous(d.pool, rng) + net_boost(sigma_d, d.pool),
                   ob  = even + type.difficulty + type.stakes + opposed_ob(d.score, opposition_rate))
sigma_d   = levels_to_sigma(track * track_step                      # the argument as it stands, toward `for`
                            + d.lean + level(d.modifier)             # what he arrived with (B24.11, B05.20)
                            - end_levels(for) + end_levels(against)  # a yield, a break or strikes, as levels
                            - resist(d))                             # his Will (B.6 d)
```

`d.score` is the skill score that stands against his ballot (his own; for a bench seat the respondent's: the host fills
it). `resist(d)` is B.6's reading of his Will. `track_step`, `yield_level`, `break_level` are dials (§E, B24p.04). The ballots
are drawn in decider id order, one normal each, after the last exchange.

### A.6 The automatic policy, and the abridged form

**The automatic policy** (`decide is None`). The mover argues, on the ground his reading scores highest for those the
argument addresses. He presses instead only when the track stands against him and his reading puts the chance that a
press marks the other side this exchange at or over the setting `press_at` (B.6's steadiness odds, computed on his
believed values): the side that is losing the argument goes after the man. Both are read off `s.read`, which is drawn
(step 1), so the policy is sampled, not fixed: two tellers of equal dice and unequal Attunement choose differently on the
same hearer. It is the module's own because an automatic sitting has no host decider to ask; a played or NPC-decided
sitting never reaches it. It picks by what a move does (its `effect` cell), never by a move's name.

**The abridged form is the same entry under a one-exchange row** (R6: *"TELLING or LYING or SPEAK etc can be abridged auto
proceedings"*). No abridged row is seeded: one function, `abridged(row)` (C.6), turns any type row into its one-speech
form: `order: free`, `exchanges: [1, 1]`, `disposal: exchange`, one move, the venue and audience unchanged. The host
passes `decide=None`. Then `proceed` runs steps 1 to 7 once, the close returns that exchange's margin against the hearer,
and the fold reads one band as it does today. A `tell` is the abridged form of `conversation`; a `speak` is the abridged
form of the row its sitting is held under. Decided, with the reason:

| option | verdict |
|---|---|
| **a degenerate type row of the same module** | **taken.** The six roles have one owner (the exchange step); a `tell` and the opening speech of a trial compose their pool, leverage and obstacle by the same lines; the abridged form costs nine normals and arithmetic where today's costs one roll; no verb is named in the module |
| a separate cheap path (keep `social_contest.roll` for `tell`, `lie`, `speak`) | refused: it is a second owner of every role's formula (CLAUDE.md §8), and R2 would then hold for a trial and not for a lie |
| the full form for every verb | refused: R6 says abridged; a `tell` that opens a decider loop would cost a scene's worth of choices for one sentence |

`social_contest.roll` (`roll.py::roll`) stays as the entry of the graded inquiries (`examine`, `research`, `surveil`) and
`arrest`, which are not influence by words (INT §D.2), and `roll.py::obstacle` stays the one composer of an obstacle: the
exchange's speech draw calls it (B.7).

### A.7 What a proceeding leaves in the world

The redesign changes how a contest goes; what it writes is the verb rows' and B27's. Three things follow from the model
and are stated so no item contradicts them:

1. **Every sitting writes** (A-81): the `ending` on its Event, at every end, including an impasse and an adjournment.
2. **The topic is read** (INT E-10): the fold's pursuit move for a carried hearer is toward the speaker's pursuits *as the
   topic proposition bears on them*; B27.05 to B27.08 own that effect and receive `ProceedingInput.topic` on the record.
3. **A mark is seen** (R1 Grace, *"being seen as respectable"*): an exchange in which a side takes a mark, or speaks below
   the venue's standard, is on the `ending`, and WITNESS deposits it to those present as it deposits any act
   (`loop/witness.py`); what regard does with it is B24.41's design (§F).

---

## B. The six roles

Each role below gives Jordan's words (R1), the mechanism, the state and units, the formula, the shipped values, the
sources by primitive id, and the falsifier. Conventions for every formula:

- `mid = (ATTRIBUTE_FLOOR + ATTRIBUTE_CEILING) / 2` (4 on 1 to 7), read from `engine/substrate/descriptors.py` and handed
  in as `dials["attribute_mid"]`; `span = ATTRIBUTE_CEILING - ATTRIBUTE_FLOOR`.
- `pool_of`, `opposed_ob`, `even_line`, `levels_to_net_sigma`, `net_boost`, `roll_net_continuous` and `band_odds` are
  `engine/dice_engine/sigma_leverage.py`'s (the first three land at B04.24; the sampler is B05.02's). `even =
  even_line(pool_add)`. A pool is fractional and is never rounded (R8); an obstacle is a real number.
- Every step and level named `*_step`, `*_gain`, `*_level` is a setting in `engine/season/data/fixtures.py` with a NUMBER
  row in `engine/season/hole_register.yaml`, shipped at its CONTROL (the value at which the role does nothing) until
  B24p.23 sets it. The "shipped" column below is the value B24p.23 sets: each is `[ASSUMPTION; Jordan to correct]`, and
  none is ruled.
- Sigma is leverage in the engine's own unit: a level of `LEVEL_SIGMA` (`minor` 0.25 to `major` 1.00), summed and soft-capped
  at 1.5 by `net_boost` (`sigma_leverage.py:103-110`, `:147-154`). A source returns two numbers, for and against; the
  channel is signed (B05.10).

**The scratch readings quoted below** come from a probe of these formulas with the shipped values, written for this
proposal and not repository code (20,000 to 40,000 keyed exchanges a point, attributes drawn uniform on 1 to 6, the plan's
live `pool_add` 6, `pool_floor` 5, `opposition_rate` 0.4, a `routine` difficulty of 0.5). They show the direction and
rough size each mechanism has; the gate's readings come from `pairs` on the built code (B24p.21). In a plain private
exchange the carried share rose per point of the speaker's attribute by about 0.064 (Reason), 0.063 (Presence), 0.020
(Grace), 0.011 (Focus), 0.008 (Attunement) and 0.005 (Will), and fell by 0.036 per point of the hearer's Will; before a
crowd Presence read 0.114 and Reason 0.050; before a solemn bench with two proofs Reason read 0.090, Grace 0.070 and
Presence 0.038. In a two-sided run of six exchanges with one decider: Presence 0.046, Reason 0.036, Grace 0.018, Will
0.007, Focus 0.005, Attunement 0.005; the other side's Grace −0.015 and Will −0.006; 82 % of sittings ran to the budget,
11 % ended on a yield and 7 % on a break. ⚠ These figures were taken with Reason alone as the dice, before R11 made the
dice a blend of Reason and Presence (B.2 a): under the blend Presence's slope rises and Reason's falls wherever the
content or the venue leans to Presence, and the reverse before a bench on evidence. They are kept as the record of that
probe only; no bound below is read from them without the built code's reading (B24p.21, B24p.23).

### B.1 Focus — *"staying on topic, not being pulled away from argument into something irrelevant"*

**Mechanism: the hold.** A pull is a pressure to speak to something other than the live topic. It comes from the room
(`Room.distraction`), from the other side's last `divert`, and from a mark just taken. When a pull stands on the mover, a
draw on his Focus settles whether his speech stays on the topic. An off-topic speech is harder to land and is counted.

| | |
|---|---|
| reads | `Speaker.focus`; `SideState.pull`; `Room.distraction` |
| changes | `Exchange.on_topic`; `SideState.strikes` (+1 when off the topic); `SideState.pull` (cleared after the hold) |
| side | the speaker's own |
| enters | the obstacle of his speech, as the roster term `off_topic`; and the type's `strikes` rule |
| units | the pull and the term are obstacle units; the hold's pool is dice |

```
pull     = s.pull + room.distraction
hold     = roll_net_continuous(pool_of(S.focus, 0, pool_add, pool_floor), rng) - (even + pull)
on_topic = (pull <= 0) or (hold >= 0)
term     = ("off_topic", 0.0 if on_topic else 1.0, off_topic_step, None)       # added to the speech's operands
s.strikes += 0 if on_topic else 1 ;  s.pull = 0.0
```

A `divert` by `T` that lands (`margin >= 0`) sets `s.pull += divert_pull + divert_gain * margin`. A mark taken sets
`s.pull += rattle_pull`. Where the type's `strikes` is `k > 0`, a side with `k` or more strikes takes
`strike_level` against it at the close for each strike over `k - 1`, and the sitting ends `struck` where the row's rite
lists the fault as ending (K/'s inquisition hearing: one strike, `modes.py:181-198`).

| setting | control | shipped | |
|---|---|---|---|
| `off_topic_step` | 0 | 1.5 | the obstacle an off-topic speech adds |
| `divert_pull`, `divert_gain` | 0, 0 | 1.0, 0.5 | the pull a landed `divert` sets |
| `rattle_pull` | 0 | 0.5 | the pull a mark sets |
| `strike_level` | `None` | `minor` | per strike over the row's allowance |
| `Room.distraction` | 0 for every audience kind | none 0.5, bench 0.25, gallery 0.5, crowd 1.0 | `arrangements.yaml: audience_kinds` (C.5) |

**Sources.** P5 (the stasis gate: *"argument may only be made at the live stasis"*); N3 (ability falls with distraction);
P17 (a speaker consuming the session with other matter) for `divert` `[NEW as a move; reason: R1 names being "pulled
away"; no earlier design gives the other side a move that pulls]`; HEAR_B's `irrelevance` fault (`:128-137`) and K/'s
evasion strikes (`primitives.py:262-280`) for the count; AR-23 (*"less likely to be distracted"*).

**Falsifier.** `test_focus_holds_the_topic_and_moves_nothing_else` (`engine/season/tests/test_sc_roles.py`): two
hand-built speakers equal but for Focus 2 and 6, a standing pull of 1.0, 20,000 keyed exchanges each. Asserts: the share
on topic is strictly higher at Focus 6 by at least four standard errors of the difference; the mean of `terms["off_topic"]`
is lower; every other entry of `Exchange.terms` and `Exchange.levels` is equal between the two (`==` on the tuples with
`off_topic` removed); `assert checked == 40000`. Control: with the pull at 0 and `distraction` 0 the two speakers' margin
lists are identical for the same keys (Focus changes nothing when nothing pulls); and with Focus equal and Reason 2 and
6, the share on topic is equal.

### B.2 Reason — *"constructing the argument/speech, making it logical and reasonable and evidentiary with ability to account for opponent's factual circumstances like resources office influence etc"*

**Mechanism: the case.** Three operands, all the speaker's. (a) The dice of his speech are a blend of his Reason and his
Presence, weighed by what the speech says and where it is said (R11, below), plus his rank in the move's skill: the
case he built and how he can carry it. (b) What he can show counts only as far as he can marshal it: his Reason caps the proofs
one speech uses. (c) The other side's circumstances (his seat's rank, the hearer's contrary commitments and debts, his
faction) stand against the speaker as obstacle terms; Reason discounts those of them the speaker knows of.

| | |
|---|---|
| reads | `Speaker.reason`, `.presence` (the blend only), `.ranks`, `.addends`, `.proofs`, `.accounts`, `.operands`; `Room.proof_weight`; `ProceedingInput.ground_reason`, `Move.reason_weight`, `ProceedingType.reason_bias` |
| changes | nothing of state; the speech draw's pool, one leverage source, the step of flagged obstacle operands |
| side | the speaker's own |
| enters | (a) the pool, as the Reason share of the blend; (b) leverage source `proofs`; (c) the obstacle, as a smaller step on terms flagged `eased_by: reason` |
| units | dice; sigma; obstacle |

**(a) The dice: the blend of Reason and Presence (R11).** Jordan, 2026-11-14: *"argument dice is Presence and/or Reason
depending upon content of argument and venue"*. The dice attribute of a speech is a weighted mean of the speaker's
Reason and Presence. The weights come from data, two rows, never from code:

- **the content**: every kind of speech has a *content class*, a row of NEW `rosters.yaml: content_classes` with one cell
  `w_reason` in `[0, 1]` (the pair is `(w_reason, 1 - w_reason)`: one cell, so the two sum to 1 by construction). A speech
  on a ground takes its ground's class (`grounds` gains a `content:` cell); a drawing move that takes no ground (`divert`)
  names its own (`proceeding_moves` gains a `content:` cell, on such moves only). The ground is the kind of speech: R1's
  *"what kind of argumentation/speech is most effective"*, chosen by Attunement (B.3).
- **the venue**: every proceeding type row of `arrangements.yaml` gains a sixth new key, `reason_bias`, in `[-1, 1]`: how
  far that venue leans every speech made in it toward Reason (+) or Presence (−). `abridged` keeps it (it keeps the venue).

| content class | `w_reason` control | shipped | taken by | |
|---|---|---|---|---|
| `evidentiary` | 1.0 | 0.8 | ground `evidence` | proofs and facts: the case made from what can be shown |
| `logical` | 1.0 | 0.7 | ground `consequence` | what follows from what: reasoning on interest |
| `procedural` | 1.0 | 0.6 | move `divert` | a point of order, other business (P17) |
| `appeal` | 1.0 | 0.4 | ground `authority` | to office, faith, law as an allegiance: carried by standing and gravity |
| `emotional` | 1.0 | 0.2 | ground `solidarity` | to fellow-feeling: carried by the speaker |

| venue (`reason_bias`) | control | shipped |
|---|---|---|
| `legal_trial`, `tribunal`, `inquisition_hearing` (a court) | 0 | +0.2 |
| `arbitration`, `interrogation`, `excommunication_deliberation`, `council_of_state` (formal, before a bench or a closed council) | 0 | +0.1 |
| `conversation`, `questioning`, `negotiation`, `audience` (private, or a plea before one seat) | 0 | 0 |
| `parliamentary_debate` (an open assembly) | 0 | −0.1 |
| `rally` (a crowd) | 0 | −0.3 |

```
c        = the content class's w_reason: ground_reason[ground] for a move with a ground, move.reason_weight otherwise
k        = clamp(10 * c + 10 * type.reason_bias, 0, 10)                        # whole tenths: both cells are tenths
blend    = weighted_tenth((S.reason, S.presence), (k, 10 - k))                  # nearest tenth, a half up
case     = blend + rank(S, skill_of(move))                                      # dice, fractional
pool     = pool_of(case, S.addends, pool_add, pool_floor) * heard(S, room)      # heard: B.4
usable   = min(S.proofs, proofs_per_reason * S.reason)                          # None = uncapped (control)
proofs   = (level(proof_level) * usable * 2 * room.proof_weight, 0.0)           # (for, against)
account  = min(account_max, account_step * (S.reason - ATTRIBUTE_FLOOR))
step'    = step * (1 - account)   for each operand (name, raw, step, "reason") with name in S.accounts
```

*The combination rule* is a sum, clamped: the venue shifts the content's weight, `w_reason = clamp(c + reason_bias, 0,
1)`, `w_presence = 1 - w_reason`. Decided by the ladder, step 4 (precedent): where this design combines a type row's
cell with a move's, it adds them (`difficulty = type.difficulty + move.difficulty`, B.7), and a bias of 0 leaves the
content alone, so a balanced venue is the content's own lean. The other reading, the product of the two pairs
renormalised, was refused at step 5: it is undefined where one pair is `(1, 0)` and the other `(0, 1)`, and a venue
cell that multiplies is harder to read off the row than one that adds. Both cells are held in tenths (the loaders
refuse any other value), so `k` is a whole number of tenths and the clamp is exact. *The rounding* is the one rule of
B05.24's sentence (Jordan's R8: fractional dice, *"round to nearest tenth"*), owned once: NEW
`sigma_leverage.weighted_tenth(scores, tenths)` beside `governing_mean` (B05.25), `(2 * sum(t_i * round(10 * s_i)) +
10) // 20 / 10`, exact in integers; `governing_mean` is its equal-weight case `[ASSUMPTION: a sibling of the governing
mean, not a second rounding rule — basis: CLAUDE.md §8, a rule lives once; B05.25's arithmetic in tenths]`. For whole
attribute scores and whole tenths the blend is exact and the rounding is vacuous; it binds only on a hand-built
fractional score.

*At control* every class reads `w_reason` 1.0 and every venue 0: the blend is Reason, the dice are R1's case alone, and
B.7's control equality holds unchanged. B24p.23 sets the shipped columns. The shipped weights are `[ASSUMPTION; Jordan
to correct]`; basis: R11's two poles (a logical, evidentiary speech before a court is Reason's; a rhetorical, emotional
one before a crowd is Presence's), with N4 (logos against pathos) and N3 (high elaboration before a bench, low before a
crowd) for the order; the numbers are sized so that the two poles reach 1.0 and 0.0 (evidence in a court 0.8 + 0.2;
solidarity at a rally 0.2 − 0.3, clamped) and the private middle keeps both attributes in the dice.

*Presence is used twice, as two mechanics.* In the blend it is part of what is said: the share of the dice his speech's
content draws from his Presence (R11). In B.4 it is whether he is listened to and how his manner lands: the share
heard (a gate on the whole pool, binding only below the room's demand) and the `delivery` source (manner against
proof, by `Room.proof_weight`) (R1). The first reads the content and the type row; the second reads the room. They are
distinct operands, each owned once, so no operand reads Presence twice `[ASSUMPTION: not a double count — basis: the
ladder, step 5: R1 and R11 are both Jordan's and each names a different thing Presence does; dropping either would
overwrite one of his rulings. Where the two compound, a rally on solidarity, the BATCH GATE's DOMINANT bound (no bin
above 0.90) is the check, and a breach resizes `delivery_step` first (B24p.23's STOP), never the blend]`. ED-IN-0350's
letter (*"argue main component is presence"*) is superseded by R11, Jordan's own later words: Presence is a component
of the dice by content and venue, not the pool attribute in every room.

`skill_of(move)` is the move row's `capability:` cell (B24.04's column: `argue`, or `law` on a procedure or definition
issue). `S.accounts` is filled by the host from the speaker's OWN ledger: a circumstance term is accounted when he holds
a claim about the fact it reads (the other's seat for `rank_gap`, the hearer's commitment for `commitment`), on
`person_q.attributed_deeds`' pattern; the module never sees a ledger. Which obstacle terms are circumstances is data: the
`eased_by:` cell of `rosters.yaml: obstacle_terms` (`reason` on `rank_gap`, `commitment` and, when B28.35 lands it, the
faction term).

| setting | control | shipped | |
|---|---|---|---|
| `proofs_per_reason` | `None` | 0.5 | proofs one speech can use, per point of Reason |
| `proof_level` | B05.17's (`minor`) | unchanged | this design sizes it by `usable`, without rounding to whole units |
| `account_step`, `account_max` | 0, 0.9 | 0.15, 0.9 | Reason 7 discounts a known circumstance by 0.9 |

**Sources.** N4 logos (*"operates on story coverage and consistency"*); N3 (argument quality decides at high
elaboration: `proof_weight`); N12 *Weigh* (*"estimate the counterpart's real situation: resources, pressures,
standing"*) for (c); P11 and M3 (evidence a party holds) for (b); P4 §3.2's *reasoning* faculty; AR-21; R11 for (a).
ED-IN-0350 ruled Presence the *main component* of `argue` (its pool attribute); R11 (2026-11-14) replaces that letter
with the blend, which answers J-SC-1: before a bench on evidence the dice are Reason's, before a crowd on solidarity
Presence's, and in between both.

**Falsifier.** `test_reason_weighs_in_the_dice_the_usable_proofs_and_the_account` `[ASSUMPTION: test name; B24p.07
creates it]`: (i) the judicial arm: under `reason_bias` +0.2 on an `evidence` ground (`w_reason` 0.8: `k` = 10), Reason
2 and 6, all else equal: the recorded pool differs by exactly 4 dice times the share heard, and `Exchange.levels` are
equal; (i′) the crowd arm: under `reason_bias` −0.3 on a `solidarity` ground (`k` = 0), Reason 2 and 6 give equal pools;
and under a bias of 0 on an `authority` ground (class `appeal`, `k` = 4) the pools differ by exactly 1.6 dice times the share heard; (ii) with five proofs
held, the `proofs` source reads `usable` 1.0 and 3.0; with none held it reads 0 for both; (iii) with a `rank_gap` operand
of raw 2.0 and the term in `accounts`, `terms["rank_gap"]` falls strictly with Reason, and is equal across Reason when the
term is not in `accounts` (he cannot account for what he does not know). Control: `proofs_per_reason` `None` and
`account_step` 0 give equal `usable` and equal `terms` at every Reason; every `w_reason` 1.0 and every bias 0 give the
pool of Reason alone at every Presence.

**Falsifier of the blend, by slope** (both roles; R11): `test_the_dice_lean_to_reason_or_presence_by_content_and_venue`
`[ASSUMPTION: test name; B24p.07 creates it]`, over generated speakers (B01a's `generated_attributes`, 20,000 keys an
arm) at the shipped settings in the test's own fixtures, the carried share regressed on the speaker's Reason and on his
Presence: (1) judicial venue (`legal_trial`'s bias, a bench) on `evidence`: Reason's slope exceeds Presence's by at
least two standard errors of the difference; (2) crowd venue (`rally`'s bias, a crowd) on `solidarity`: Presence's
slope exceeds Reason's by the same margin; (3) balanced venue (`conversation`'s bias, no audience) on `authority`: both
slopes exceed 0 by two standard errors. `assert checked == 3 * 20000`. The same three relations are read on the built
realm by `pairs proceeding --diff all` per type (B24p.23's gate), bounds `[ASSUMPTION; Jordan to correct]`.

### B.3 Attunement — *"understanding what is most likely to rattle your opponent or reading their intent, being able to read the room, identifying what kind of argumentation/speech is most effective for audience adjudicator opponent"*

**Mechanism: the reading, and the choice made on it.** Attunement adds no dice and no leverage to a speech (ED-IN-0350:
*"attunement informs how character thinks the other character is receiving it and the best style of argument to
deliver"*). Each exchange the mover reads the room and the other side by one roll on his Attunement; the roll's margin
sets how blurred his picture is. He then chooses his ground, and whether to argue or press, on that picture; the speech
is paid for by the TRUE values.

*What is read.* Every person has four dispositions, one per ground, in `[0, 1]`: how far that ground moves him.
`person_q.moved_by(p)` derives them from what he already holds, by the `read:` cell of each `rosters.yaml: grounds` row
`[NEW; reason: R1 asks the speaker to tell what works on "audience adjudicator opponent", so every one of them must
differ in it; today only the eighteen hearers B04.07 seats a trait on do. Deriving from held values adds no drawn field
and no carrier. The four `read:` cells are [ASSUMPTION; Jordan to correct], after the archived resonant-style map,
`.designs/systems/npcs/reference/npc_behavior_v30.md` §1.3]`:

| ground | derived from | where held |
|---|---|---|
| `evidence` | his Reason, `(reason - FLOOR) / span` | `Person.attributes` |
| `consequence` | his strongest pursuit weight | `Person.pursuits` (weights in `[0, 1]`; realm seed 0: 0.0 to 0.8) |
| `authority` | his strongest conviction, over the roster's scale | `Person.conviction` (`affiliation_roster.scale`, 0 to 5) |
| `solidarity` | his Attunement, `(attunement - FLOOR) / span` | `Person.attributes` |

A seated trait `moved_by_<ground>` (B04.07) reads 1.0 on its ground. The same vector serves the three clauses of R1:
*what is most effective* on a decider is the ground with his highest weight; *what is most likely to rattle* an opponent
is the ground he is most invested in (a blow there is heavier, B.6); *reading the room* is the weight-mean over the
deciders and hearers; *reading their intent* is the believed strain and resolve of the other side (AR-42: *"how close
the opponent may be to admitting defeat"*).

```
read    = roll_net_continuous(Pa, rng) + net_boost(-guard_step * (target.grace - mid), Pa) - (even + read_ob)
          where Pa = pool_of(S.attunement + rank(S, "insight"), 0, pool_add, pool_floor)
acc     = (1 + tanh(read / read_scale)) / 2                       # in (0, 1); fmath's tanh (B06.02)
blur    = read_blur * (1 - acc)
believed[g]      = clamp(true[g] + blur * xi_g, 0, 1)             # one normal xi_g per ground; `true` is the target's vector
believed_strain  = max(0, t.strain + blur * xi_0)                 # one more normal

fit(v, g)        = (v[g] - mean(v)) / (max(v) - mean(v))   if v[g] >= mean(v)      # +1 on his best ground
                 = (v[g] - mean(v)) / (mean(v) - min(v))   otherwise               # -1 on his worst; 0 if v is flat
fit_body(g)      = sum_d d.weight * fit(d.moved_by, g) / sum_d d.weight            # the deciders an argument addresses
fit source       = (level(fit_level) * max(fit_body(g), 0),  level(misfit_level) * max(-fit_body(g), 0))
```

The reading is opposed by the target's Grace: a composed person gives little away `[ASSUMPTION — basis: the registry's
Grace is composure (`descriptor_registry.yaml`, the Grace row); the proceedings study's "control of display" (COL §6.3
capacity 5); v30 opposed Appraise with Charisma ÷ 2 (`:155`) on a roster that had no Grace]`. A split room gives a small
`fit_body` whatever is chosen (N9). The `fit` source enters `argue`, and B24's `answer`; a `press` uses the same reading
for its aim (B.6). In an automatic sitting the policy of A.6 takes the argmax of `believed`; a decider is shown `believed`
in `ExchangeView.read` and never `true`.

**The reading is kept** `[NEW; reason: ED-IN-0350's choice-side role needs the reader to hold what he read before he
next chooses; capacity 3, "the read is got, not taken"; N12 gauge]`: `ProceedingOutcome` carries each speaker's last
`read`, and the fold may deposit it in his own ledger as claims `(other, "moved_by", ground)` at the confidence `acc`
(setting `reading_kept`, control off). The chooser then prices a later act on what he holds, by the ordinary believed
path (`sigma.py::believed_input`), with no read of another's sheet (AX-2).

| setting | control | shipped | |
|---|---|---|---|
| `fit_level`, `misfit_level` | `None`, `None` | `strong`, `moderate` | sigma on the target's best and worst ground |
| `read_ob` | 1.4 | 1.4 | the reading's own difficulty: an Attunement at the population's middle reads at even odds |
| `read_scale`, `read_blur` | 1.0, 1.0 | 1.0, 1.0 | inert while both fit levels are `None` |
| `guard_step` | 0 | 0.15 | sigma against the reader per point of the target's Grace over `mid` |
| `reading_kept` | off | on | the deposit of the read |

**Sources.** N12 (read before speaking: weigh, gauge, assess); N1 (each mind holds its own susceptibilities); N9 (a body
of factions and indeterminates); v30's Appraise and armature (`:154-188`: alignment as continuous sigma leverage, the exact
weights never revealed); K/`appraise.py`, `armature.py`; B24.35's four rows, which stay the owner of what a held trait
is worth when its condition holds and gain `ground:` in their `when` (§F). Against v30's *"never a penalty"*, the worst
ground costs: the proceedings study's register matrix (each manner heard as its misreading, COL H03) and N5 (reactance)
`[ASSUMPTION: a misfit costs — basis: those two; `misfit_level` `None` restores v30's rule]`.

**Falsifier.** `test_attunement_sharpens_the_reading_and_moves_only_the_choice`: (i) the choice forced (a scripted
decider naming one ground): Attunement 2 and 6 give identical `Exchange.margin` lists for the same keys (it adds nothing
to a speech); (ii) the choice free, the target's vector peaked on one ground: the share of exchanges choosing that ground
is strictly higher at Attunement 6, by at least four standard errors, over 20,000 keys; (iii) the target's Grace 2 and 6:
the share is lower at 6. Control: with the target's vector flat (all four equal) the two Attunements' carried shares are
equal within two standard errors, and with both fit levels `None` they are identical.

### B.4 Presence (charisma) — *"the ability to be listened to and be compelling with your delivery"*

**Mechanism: the share heard, and delivery** (R1), beside Presence's share of the dice (R11, B.2 a: a separate mechanic,
read off the content and the venue, not the room). Two operands here. *Listened to*: an audience demands a certain Presence before
it attends; a speaker short of it has only part of his case heard, and the dice of the unheard part are not rolled.
*Compelling delivery*: Presence over or under the middle is leverage for or against the speech, weighed by how far this
audience goes by manner rather than proof.

| | |
|---|---|
| reads | `Speaker.presence`; `Room.attention`, `Room.proof_weight`; `ProceedingType.order` |
| changes | nothing of state |
| side | the speaker's own |
| enters | the pool, as a share; leverage source `delivery` (and, by B.2 a, the pool's Presence share of the blend) |
| units | a share in `[heard_floor, 1]`; sigma |

```
heard(S, room) = 1.0                                                              if order is written_only
               = clamp(1 - heard_step * max(0, room.attention - S.presence), heard_floor, 1.0)
delivery       = delivery_step * (S.presence - mid) * 2 * (1 - room.proof_weight)   # for if > 0, against if < 0
               = 0                                                                 if order is written_only
```

`heard` multiplies the pool of every speech (B.2), so being unheard costs the case he built, whatever its blend of
Reason and Presence, and nothing else stands in for it. Both operands are zero-centred or neutral in a private room (`attention` 0, `proof_weight` 0.5).

| setting | control | shipped | |
|---|---|---|---|
| `delivery_step` | 0 | 0.25 | sigma per point of Presence from `mid`, at `proof_weight` 0.5 |
| `heard_step`, `heard_floor` | 0, 1.0 | 0.1, 0.5 | the share lost per point short of the room's demand |
| `Room.attention` | 0 for every audience kind | none 0, bench 2, gallery 4, crowd 5 | points of Presence (C.5) |
| `Room.proof_weight` | 0.5 for every kind | none 0.5, bench 0.75, gallery 0.5, crowd 0.25 | N3's route |

**Sources.** N4 ethos and pathos (the low-route channels); N3 (cues decide at low elaboration; *"forcing the route"*);
the exordium's three states, goodwill, attention, receptiveness (COL E11) for *listened to*; K/'s crowd adjudicator
(Charisma-primary, `dictionaries.py:351-386`) and `public_oration` venue; P4's *eloquence* faculty and its written
petition; AR-29; ED-IN-0350.

**Falsifier.** `test_presence_weighs_in_the_dice_is_the_share_heard_and_the_delivery` `[ASSUMPTION: test name; B24p.07
creates it]`: (o) the dice, two arms: under `reason_bias` −0.3 on a `solidarity` ground (`k` = 0) in a room of
`attention` 0, Presence 2 and 6 give pools differing by exactly 4 dice; under `reason_bias` +0.2 on an `evidence` ground
(`k` = 10) they give equal pools; (i) under `k` = 10 in a room of `attention` 0, Presence 2 and 6
give equal pools and `levels["delivery"]` of `-0.5` and `+0.5` sigma at the shipped step; (ii) under `k` = 10 in a room of `attention`
5, the recorded pool at Presence 2 is the pool at Presence 6 times `0.7` exactly (three points short at 0.1 a point;
Presence 6 is over the demand and loses nothing); (iii) under `written_only` both
operands are equal across Presence. Control: `delivery_step` 0, `heard_step` 0 and every `w_reason` 1.0 with every
bias 0 give identical exchanges at every Presence. The slope arms are B.2's
`test_the_dice_lean_to_reason_or_presence_by_content_and_venue`. The profile pair (AR-49, AR-50) is B.5's test.

### B.5 Grace — *"acting in the correct manner for the venue and occasion, as being seen as respectable, for remaining composed in face of difficulties and challenges"*

**Mechanism: three things, one per clause.** (a) *The correct manner*: the type row names a standard; a speaker whose
Grace falls short of it meets an obstacle for every point short, and a surplus adds nothing (AR-36a: a parliament
penalises one who is persuasive but *"not doing it right"*). (b) *Seen as respectable*: he enters with an esteem in the
room set by his Grace; it is leverage on every speech he makes, it falls when he is seen to be rattled or presses and
fails, and it is on the record for those present. (c) *Remaining composed*: a mark costs a side leverage on every later
speech; Grace covers part of that cost. Whether a blow marks him at all is Will's (B.6).

| | |
|---|---|
| reads | `Speaker.grace`; `ProceedingType.standard`; `SideState.marks`, `.standing` |
| changes | `SideState.esteem` |
| side | the speaker's own |
| enters | (a) the obstacle, roster term `standard` (OBS member 3, landed at step 0 by B05.21); (b) leverage source `respect`; (c) leverage source `marks`, against |
| units | obstacle; sigma |

```
(a) term       = ("standard", max(0, type.standard - S.grace), standard_step, None)
(b) esteem_0   = respect_step * (S.grace - mid)                    # s.esteem at the sitting's start
    respect    = (max(s.esteem, 0), max(-s.esteem, 0))
(c) cover      = min(cover_max, cover_step * (S.grace - ATTRIBUTE_FLOOR))
    marks      = (0.0, s.marks * level(mark_level) * (1 - cover))
    on a mark taken:        s.esteem -= mark_shame * (1 - cover)
    on a press that fails:  s.esteem -= press_rebound              # the presser's; B.6
```

`type.standard` is the row's `standard:` level sized by the table `standard_demand` (`plain` 0, `routine` 3, `demanding`
4, `hard` 5, in points of Grace). The key and its level names are B05.21's (the `difficulty_levels` roster); B05.21 sizes
the level by `difficulty_ob` as a flat obstacle on every speaker, and this design sizes it as a demand on Grace instead,
so the term is the speaker's shortfall and not the room's bare level (§F edits B05.21 and B05.23).

**Where Will ends and Grace begins** (INT §F item 4), decided by the ladder. Step 3, the design documents: the registry
calls Grace *"composure, calm, etiquette, manners"* and AR-44 gives Spirit *"the capacity to tolerate harm and strain
and stress"*. Step 5, the architecture: two attributes on one state need two operands or one of them is a second name
for the other. So **Will acts on the transition and Grace on the state**: Will settles whether a blow becomes a mark
(*"not get rattled in the first place"*); Grace settles what a mark costs him and how much of it shows (*"remaining
composed in face of difficulties"*). A person of high Will and low Grace is seldom rattled and badly thrown when he is;
one of low Will and high Grace is rattled often and carries it well.

| setting | control | shipped | |
|---|---|---|---|
| `standard_step` | 0 | 0.5 | obstacle per point of Grace short of the standard |
| `standard_demand` | every level 0 | `plain` 0, `routine` 3, `demanding` 4, `hard` 5 | points of Grace, keyed on `difficulty_levels` |
| `respect_step` | 0 | 0.08 | sigma per point of Grace from `mid`; small beside `delivery_step` so AR-50 holds |
| `mark_level` | `None` | `moderate` | sigma against a side per mark, before cover (v30's −1D per Rattled level, `:253`, recast) |
| `cover_step`, `cover_max` | 0, 0.9 | 0.15, 0.9 | the share of a mark's cost Grace covers |
| `mark_shame` | 0 | 0.25 | sigma of esteem lost on a mark, before cover |

**Sources.** N11 (register checked against decorum: *"the wrong register for the occasion succeeds at nothing and costs
ethos"*); N17 (the wrong form for the community fails); N20 (the speaker's character is part of the case and may be
attacked) and P1 (standing indexed per body) for (b); v30's Face and Rattled (`:240-258`) recast for (c), with S-7's rule
that standing is never a stored number (COL §8 row 21) kept by holding it in the sitting only; AR-32 to AR-36a; B24.41's
items (1), (3) and (6), which this builds for the room and leaves for regard (§F).

**Falsifier.** `test_grace_meets_the_standard_keeps_esteem_and_covers_a_mark`: (i) at `standard: plain` the obstacle
is equal at Grace 2 and 6; at `hard`, `terms["standard"]` is 1.5 at Grace 2 and 0 at Grace 5, 6 and 7 (a surplus adds
nothing: the three obstacles are `==`); (ii) `esteem` starts at `-0.16` and `+0.16`; (iii) with one mark planted,
`levels["marks"]` against is lower at Grace 6, and the esteem lost on a planted mark is lower. `test_the_two_profiles`
(AR-49, AR-50), over 20,000 keyed two-sided sittings under a `routine` standard with a gallery: the speaker of Presence 6,
Grace 2 is carried more often than the speaker of Presence 2, Grace 6, AND ends with the lower `esteem`; both
differences exceed four standard errors. Control: every Grace setting at control gives identical sittings at every Grace.

### B.6 Will (Spirit) — *"the ability to keep arguing your case, to believe in yourself and remain confident, to not get rattled in first place, that 'x factor' that supports you"*

**Mechanism: four things, one per clause.** (a) *Not rattled in the first place*: when a `press` lands on him, a draw on
his Will settles whether he takes a mark or carries the blow as strain. (b) *Keep arguing*: his resolve, set by his Will,
is how many exchanges he can go on; marks spend it; at zero he can only rest, and a side that can no longer answer has
yielded. (c) *Believe in yourself, the x factor*: his Will discounts everything that counts against him in his own
speech, the leverage against and the hostile terms of the obstacle (AR-44: *"the ability to get good results despite
poor circumstances ... ignoring obstacle modifiers"*). (d) As the one addressed, his Will is the resistance a speech or
a ballot must overcome (AR-44: *"free of external influence or compulsion"*).

| | |
|---|---|
| reads | `Speaker.will`, `Decider.will`; `SideState.strain`, `.marks`, `.resolve`; operands flagged `eased_by: will` |
| changes | `SideState.strain`, `.marks`, `.resolve`, `.pull` |
| side | (a), (b), (c) his own; (d) the speaker's opposite |
| enters | (a) a draw; (b) an end condition and levels at the close; (c) a factor on the levels against and on flagged obstacle steps; (d) leverage source `resist` and the ballot's obstacle |
| units | dice; exchanges; a share; sigma |

```
(a) a press by S lands when its margin m >= 0:
      aim    = 1 + sore_gain * T.moved_by[ground]                      # heavier on what he is most invested in (B.3)
      blow   = blow_gain * (press_base + m) * aim
      steady = roll_net_continuous(pool_of(T.will, 0, pool_add, pool_floor), rng) - (even + t.strain + blow)
      steady <  0:  t.marks += 1 ; t.strain = 0 ; t.resolve -= mark_resolve ; t.pull += rattle_pull ; esteem as B.5
      steady >= 0:  t.strain += strain_carry * blow
    a press that fails (m < 0):  s.esteem -= press_rebound
(b) resolve_0 = resolve_base + resolve_per_will * S.will ;  s.resolve -= 1 after each exchange he speaks
    s.resolve <= 0: his only legal move is rest; if the other side has resolve and effort left, the sitting ends `yielded`
(c) shield   = min(shield_max, shield_step * (S.will - ATTRIBUTE_FLOOR))
    sigma    = sum(for) - sum(against) * (1 - shield)
    step'    = step * (1 - shield)   for each operand flagged eased_by: will   (reception, regard: the hostile room and hearer)
(d) resist   = (max(-r, 0), max(r, 0))   with r = resist_step * (target.will - mid)       # on a speech addressed to him
    ballot ob term: opposed_ob(d.score, opposition_rate), and resist(d) among the ballot's levels (A.5)
```

`t.strain` starts at `Speaker.strain`, the strain he carries in (`person_q.strain_carried`, A.2): each mark he took in a
proceeding this season, less `strain_rest` per scene he has since spent on something else (v30 `:254`: a mark clears per
scene of rest) `[ASSUMPTION: the recovery rate — basis: v30]`. A side at `type.break_at` marks cannot go on and the
sitting ends `broken`. The automatic policy presses only when the mover is behind on the track and his believed odds of
a mark reach `press_at` (A.6): the side that is losing the argument goes after the man (N8).

| setting | control | shipped | |
|---|---|---|---|
| `press_base`, `blow_gain`, `sore_gain` | 1.0, 0, 0 | 1.0, 0.5, 1.0 | `blow_gain` 0 makes every press harmless |
| `strain_carry` | 0 | 0.5 | the share of an absorbed blow that stays as strain |
| `mark_resolve` | 0 | 1.0 | exchanges of resolve a mark costs |
| `resolve_base`, `resolve_per_will` | the type's maximum, 0 | 2.0, 0.5 | Will 1 can speak 2.5 exchanges, Will 6 five |
| `shield_step`, `shield_max` | 0, 0.6 | 0.1, 0.6 | Will 7 discounts what is against him by 0.6 |
| `resist_step` | 0 | 0.15 | sigma per point of the target's Will from `mid` |
| `press_rebound` | 0 | 0.25 | sigma of esteem a failed press costs the presser |
| `press_at` | 1.0 (never) | 0.4 | the automatic policy's threshold on believed odds |
| `strain_rest` | — | 1 | marks cleared per scene spent elsewhere |
| `yield_level`, `break_level` | `None`, `None` | `moderate`, `strong` | against the side that yielded or broke, at the close |

**Sources.** v30's strain, Rattled, Concentration and Spent (`:197-199`, `:240-270`), recast on the continuous engine with
Will in place of the Focus defence; N5 (a pressure tolerance; force beyond it turns on the mover: `press_rebound`); N8
(concession always available and priced; the loser may escalate); G09 (R-19: *"a cornered man breaks toward the feared
thing"*) for `aim`; CR5's backfire on a failed obscuring move (v30 `:230-234`) for the rebound; P4's *composure* faculty;
AR-44. `[NEW: the shield — reason: AR-44's "ignoring obstacle modifiers" and R1's "x factor" name an effect no earlier
design gives a mechanism; a factor on what is against him is the smallest one that reads both]`.

**Falsifier.** `test_will_resists_the_rattle_outlasts_and_discounts_what_is_against_him`: (i) a scripted presser lands
a blow of 1.5 on targets of Will 2 and 6, 20,000 keys: the share marked is strictly lower at Will 6 by at least four
standard errors; (ii) `resolve_0` reads 3.0 and 5.0, and under a decider that always argues the Will 2 side rests first
in every sitting; (iii) with 1.0 sigma planted against the speaker, the net sigma recorded is `-0.9` at Will 2 and `-0.5`
at Will 6, and `terms["reception"]` for a hostile room is lower at Will 6; (iv) a speech addressed to a hearer of Will 6
records `levels["resist"]` against, and of Will 2 for. Control: with nothing against the speaker and no press, Will 2 and 6
give identical exchanges; every Will setting at control gives identical sittings at every Will.

### B.7 The speech draw, composed once

The exchange builds one `SocialContestInput` and calls `roll.py::roll`, so the draw and the obstacle keep their single
owners (`roll.py::obstacle`, B05.14's composer; `Margin.terms` names every term).

```
operands = S.operands with steps eased (B.2 c, B.6 c)
         + ("standard", ...)  (B.5 a)  + ("off_topic", ...)  (B.1)
sources  = delivery (B.4) · fit (B.3; argue and answer only) · respect (B.5 b) · proofs (B.2 b) · marks (B.5 c)
         · resist (B.6 d) · S.levels (the host's: office, capability, obligation, ...)
sigma    = sum(for) - sum(against) * (1 - shield)                                       (B.6 c)
case     = weighted_tenth((S.reason, S.presence), (k, 10 - k)) + rank(S, skill_of(move))   (B.2 a; R11)
inp_x    = SocialContestInput(pool = pool_of(case, addends, pool_add, pool_floor) * heard,
                              opposition = T.score, difficulty = type.difficulty + move.difficulty,
                              obstacle_operands = operands, leverage = sigma, <the bounds, as contest_input fills them>)
margin   = roll(inp_x, rng)                                   # Margin(net, ob, terms)
```

`Exchange.levels` records each source's pair and `Exchange.terms` the obstacle's terms, so every role's contribution to
every speech can be read after the draw (SC-P1's record, B05.18). The new leverage sources (`delivery`, `fit`, `respect`,
`marks`, `resist`) are members of `rosters.yaml: advantage_sources`, bound in the module (`proceeding.LEVERAGE`) where
the host's are bound in `sigma.py::ADVANTAGE_SOURCES`; the import-time check that every member has exactly one binding
covers both tables (B24p.05). The roster stays the only door into the sigma term (CP-T01-05's law, `sigma.py:160-170`).

**At control the exchange is the single roll.** With every setting above at its control, `heard` is 1, every new source
returns `(0, 0)`, both new terms are 0, no step is eased and the blend is Reason (`k` = 10: every `w_reason` 1.0, every
bias 0), so `inp_x` is the record `contest_input` builds today with the pool's attribute changed, and `exchange_odds` equals `band_odds` on that record exactly. That equality is B24p.07's
control, asserted with `==`.

### B.8 The six, side by side

| attribute | acts on | operand | when it does nothing |
|---|---|---|---|
| Focus | whether the speech stays on the topic | a draw; obstacle term `off_topic`; strikes | nothing pulls |
| Reason | the size of the case, the proofs it can use, the other side's circumstances | the pool's Reason share (`w_reason`); source `proofs`; eased steps | `w_reason` 0 (the pool); no proofs held; nothing known of the other side |
| Attunement | which ground and which move are chosen | the reading's blur; source `fit` through the choice | the target's dispositions are flat; the choice is forced |
| Presence | the pool's Presence share; how much is heard, and how it lands | the pool's Presence share (`1 - w_reason`); `heard`, a share of the pool; source `delivery` | `w_reason` 1 (the pool); a written speech (the other two) |
| Grace | fit to the venue, esteem in the room, the cost of a mark | obstacle term `standard`; sources `respect`, `marks` | (a) a plain room or a surplus; (c) no mark |
| Will | marks, staying power, what is against him, being moved | a draw; resolve; the shield; source `resist` | (a) nobody presses; (c) nothing is against him |

No two rows share an operand but one, which is what R2 asks (*"in the manner that I specified"*) and what a mean of
attributes (B05.25) cannot give. The one: the dice attribute is a blend of Reason and Presence, by Jordan's R11; each
enters it in its own weight, read from the content and the venue, never as an unweighted mean, and each is exactly
observable (the pool moves by its weight times the difference, to the tenth). `test_each_role_moves_only_its_own_operand`
(B24p.18) holds it: for each of the six, two speakers differing in that attribute alone leave every operand of the
other five roles equal on the record, the pool under Reason and Presence moving only by that attribute's weight.
