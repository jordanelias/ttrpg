"""`queries/inputs.py` -- THE TYPED INPUT RECORDS the host builds for a module entry (A-25).

A-25 (`ED-IN-0284`, revised by `ED-IN-0285`): a verb is a loop-side ADAPTER. The host builds a typed
INPUT record from what `World` holds, calls the module ENTRY (a composition row carrying `entry:`,
registered in `manifest.MODULE_ENTRIES`) and interprets what comes back. A module never reads or
writes `World`; it reads the record. The record types live HOST-side, here, where projections are
built, and a module imports them -- it depends upward on `engine/`, and the host reaches the module
only by string. (`architecture/holonic_ARCHITECTURE.md` §45 puts a module's records inside the module;
in Python that would make `engine/` import module code, which
`test_importing_every_engine_module_pulls_in_no_subsystem` refuses, so the records stay here.)

⚠ THIS FILE IS A LEAF: stdlib only, and it imports nothing from the season package. A module that
imports a record type must pull in nothing else of the host
(`engine/season/tests/test_social_contest_module.py` observes it in a fresh process); a record type
placed beside a builder that reads `data/` would drag the registries into every module.

THREE INPUT RECORDS (plan positions `31a`, `31b`, `31c`) AND ONE OUTPUT RECORD, `Margin` (v9 SC-01 step
15). `Margin` types the MODULE -> HOST boundary of the social contest scene's provider: the module
entry returns one and the host adapter (`seam/wrappers/sigma.py::resolve`) refuses anything else, so a
winner cannot cross. The adapter still hands the seam the `dict` every provider returns -- the SEAM keeps
one return shape (`combat` returns a scene and `mass_battle` a field, neither a margin); typing the seam
itself is a `seam/` item of its own. It lives here, not in a sibling file, because a module imports it to
construct it and this leaf is the one host file a module may import
(`engine/season/tests/test_social_contest_module.py`).

B17.03 adds the mass-battle module's output record, `FieldOutcome` (with `SideOutcome`, `PartOutcome`), after `MassBattleInput`: the
entry returns it and the host adapter reads it (`seam/wrappers/mass_battle.py::resolve`). It carries no verdict.

B14.01 adds the combat module's output record, `CombatOutcome` (with `PartyWounds`, `Surrender`, `DecisiveBeat`), beside
`PersonalCombatInput`: the entry returns it and the host adapter reads it (`seam/wrappers/combat.py::resolve`). It is
not a `Margin` and carries no winner.

B24p.02 adds the proceeding's records after `Margin`: `Input` in (with `Present`, `Rite`, `Sitting`, `Point`, `Cond`, `Item`,
`Beat`), `Outcome` out, `View`/`Option`/`Choice`/`JudgeView` for a played chooser, and `Card` (derived by the host, never authored).

v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`) add the fieldwork scene's pair, at the foot of the file:
`TrailItem` and `FieldworkInput` in, `Findings` out -- the `inquiry` role's records, for the same reason.
v9 IN-07 E1 adds the settlements module's larder records after them: `Eater`, `LarderInput` and `Under`
in, `DrawRow`/`DrawRecord` out (built by `queries/world_q.py::larder_input` and `under_input`).
v9 IN-07 E2 adds `SubsistInput` in, `SubsistOutcome`/`BodyFall` out, for `settlements.subsist`.
v9 IN-07 E3 adds `ProduceInput` in, `ProduceRow`/`ProduceOutcome` out, for `settlements.produce`.
v9 IN-07 E4..E6 add `HousingInput`/`Housing`, `FabricInput`/`Fabric` and `FortInput` (its entry returns a
`float`), for `settlements.housing`, `settlements.fabric` and `settlements.fortification`.
v9 IN-52 adds `ProvisionInput` in, `Provision` out, for `settlements.provision` (the levy-to-field feed).
v10 REM-31 (IN-46) adds, beside `PersonalCombatInput`, the PLAYABLE fight's pair: `PlayHost` (the host's one
optional argument) and `CombatTurnView` (what its per-turn decider reads, handed outward by the module entry).
"""
from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Callable, Mapping, NamedTuple, Optional

# THE MATTER'S TWO SIDES, signed toward `for` (the sign every `stake` and `believes` is read in), and the flip to the other: the one owner
# the proceeding module, its host adapter, the person reads and the rite loader share.
SIDES = ("for", "against")
SIDE_SIGN = {"for": 1.0, "against": -1.0}


def other_side(side) -> str:
    return "against" if side == "for" else "for"


_NO_POINT = tuple((s, None) for s in SIDES)   # `Sitting`'s `live` and `last_voice` at the outset: no side has a point or a voice yet


@dataclass(frozen=True)
class SocialContestInput:
    """What the `social_contest` module's σ-leverage roll reads, and nothing else.

    Built by `seam/wrappers/sigma.py::contest_input` (the host input builder) from `World`:
      * `pool`      -- dice, from what the actor genuinely has (`sigma.py::faculty`);
      * `opposition` -- what a PERSON opposite brings to the act: his score in the opposing attribute the verb row names
                       (`opposed_attribute:`) PLUS his skill score in the verb's skill (A-79, A-137), or `None` where nobody is
                       opposite (a docket item, a Record, a site, a self-plea). A RAW OPERAND, not an obstacle;
      * `difficulty` -- the act's own, the size of its verb row's `difficulty:` level (`Fixtures.difficulty_ob`), raw;
      * `pool_default` -- the untrained score: the opposition where no person is opposite (`opposed_ob(pool_default, opposition_rate)`);
      * `pool_add` -- the pool's base, whose even line (`MU_PER_DIE x pool_add`) is the obstacle's first term;
      * `opposition_rate` -- the share of the opposing score an obstacle takes up, per point;
      * `obstacle_operands` -- `((name, raw operand, step), ...)` in `rosters.yaml: obstacle_terms` order, for the members that are a
                       raw operand times a step (`standard`, `stakes`, `regard` where each weighs, `reception`, `capability`; the three that do not need one carry their own field above);
      * `obstacle_ceiling` -- the `H-213` bound on how hard one matter can get; `None` is the
                       uncapped control arm;
      * `ceiling_per_pool` -- the `chance_floor` arm (CP-T01-06): from one die, the module solves the
                       cap for THIS pool from `obstacle_ceiling`'s own chance at one die, and the
                       fixed value stays the cap below one die. `False` is the fixed arm (the default);
      * `ceiling_form` -- the ceiling's form past the per-pool bound (`hard`: a flat bound; `soft`: the excess saturates toward it); `hard` by default, so every hand-built record keeps its reading;
      * `obstacle_refusal_multiple` -- S27.4's multiple, the fixture the host adapter refuses on,
                       on the pair the entry returns;
      * `leverage`  -- the σ-layer μ-shift: the host's `advantage_sigma` sums the act's advantage sources
                       (`rosters.yaml: advantage_sources`: `effort`, `capability`, `proofs`, `favour`), zero where none is taken.

    ⚠ NO `ob` FIELD, ON PURPOSE (v9 SC-01 step 14; ED-SC-0033 clause (3), *the obstacle has a single
    owner*). The obstacle is COMPOSED by the module (`modules/social_contest/roll.py::obstacle`) from
    the operands above; the host carries them and composes nothing, so a host-side obstacle has
    no field to travel in. `engine/season/tests/test_sc01_obstacle_ceiling.py` fails if one returns.
    ONE RECORD IS ONE MATTER'S DRAW: the ceiling bounds each matter's obstacle on its own and nothing
    aggregates obstacles across a bundle (ED-SC-0038's per-matter pick, `H-213`).

    THE ROOM'S OPERANDS (v9 SC-02 `22a`; proceedings `19_PLAN.md` steps 17, 18, 20), RAW AS THE OTHERS:
      * `reception` -- the bench's signed regard for the actor (`queries/world_q.py::reception`,
                       route erosion inside it); `0.0` where the prize is heard by no room;
      * `reception_gain` -- the `H-215` fixture scaling it into the obstacle;
      * `proofs`    -- the actor's unmirrored proofs against the opponent, each weighed by remove
                       (`queries/world_q.py::proofs`); `0.0` where no room hears the prize.
    B05.17 (PES-A): THE MODULE READS NONE OF THESE. The host turns them into what they are: the bench's hostile half is the
    obstacle's `reception` operand (`obstacle_operands`), and a proof or a friendly bench is `leverage` (`advantage_sources`:
    `proofs`, `favour`). They stay on the record raw, for the trace (SC-P1), and default to the no-room reading, which a record
    built for a prize no room hears carries.

    THE EXAMINED DOCUMENT'S OPERAND (v9 SC-02 `22b` step 25), RAW AS THE OTHERS:
      * `forgery_quality` -- `Record.forgery_quality` of the Record an INQUIRY examines (`sigma.py::
                       contest_input`'s `examined`); `0` for a genuine document, for any subject that
                       is not a Record, and for every contest a prize names; B11.68: the larger of that and
                       the strongest live cover among the doers of the trail an inquiry can uncover
                       (`epistemic.trail_concealment`). Composed by the module."""
    pool: float          # FRACTIONAL (B05.25): the mean of his governing attributes plus his rank, to the tenth (`pool.faculty`)
    opposition: Optional[float]
    obstacle_ceiling: Optional[float]
    obstacle_refusal_multiple: float
    leverage: float
    difficulty: float    # B05.14: raw, no default -- a record built without the act's difficulty is no record of a rolled act
    pool_default: float
    pool_add: float
    opposition_rate: float
    reception: float = 0.0
    reception_gain: float = 0.0
    proofs: float = 0.0
    forgery_quality: float = 0.0
    ceiling_per_pool: bool = False
    ceiling_form: str = "hard"   # B05.53: how the obstacle behaves past its ceiling -- `hard` a flat bound, `soft` the excess saturating toward it; read by `modules/social_contest/roll.py::obstacle`, which refuses any other value
    obstacle_operands: tuple = ()


@dataclass(frozen=True)
class Margin:
    """What the social contest module's entry returns for one matter's draw: the roll's `net` and the
    `ob` it was thrown at, and the terms that made that `ob` (v9 SC-01 step 15; `08_SEAM.md`'s provider rule, intent
    only: *a MARGIN, never a winner*).

    `terms` (B05.14; OBS §1, §2; SC-B Edit B) is `((name, value), ...)`: every term of the obstacle in `rosters.yaml:
    obstacle_terms` order, then lane A's `forgery` where it acted, then `("ceiling", -clip)` and `("floor", +lift)`
    where a bound acted. THE VALUES SUM TO `ob`. Every roster member is non-negative (nothing lowers the obstacle: the favourable
    half of a room is leverage, B05.17); only the ceiling's clip is negative. `()` on a margin a
    stub entry returns with no composition behind it.

    ⚠ NO WINNER, NO BAND, NO SIDE. The band is the one ladder's reading of this pair
    (`seam/ladder.py::degree_of` -> `degree_from_net`), and who it favours is the fold's reading of the
    band; a field naming either would make the module a second resolver. The host adapter refuses a
    return of any other type (`seam/wrappers/sigma.py::resolve`)."""
    net: float
    ob: float
    terms: tuple = ()


@dataclass(frozen=True)
class Item:
    """A worldly matter one side brings: a typed reference, never text (V2 p2 §G; `rosters.yaml: matters`).

      * `id`      -- the item's own id;
      * `kind`    -- a member of `rosters.yaml: matters`;
      * `weight`  -- how much it weighs where it is shown;
      * `source`  -- whose it is (the holder, the witness, the one implicated), where it has one;
      * `about`   -- whom or what it bears on, where it has one;
      * `sincere` -- `False`: its holder knows it false (his own false word, or a forgery).

    B24.05: the item SHOWN at a sitting is this record (HEAR_B's `Exhibit` is not a second one), so it also carries, each defaulted
    (a record built without them is the record it was):
      * `side`   -- `"for"` | `"against"` the party it is shown for, `None` before it is entered;
      * `rung`   -- the `rosters.yaml: issue_rungs` member it bears on;
      * `cell`   -- `(subject, predicate, value)` as filed;  `origin` -- the root of its chain, the thing `impugn` halves by;
      * `forged_found` -- a filed finding names the Record it comes from forged.

    B24.19 (EVID_B edit 3; the same two cells HEAR_B's `Exhibit` names), each defaulted:
      * `pairs` -- `((another filed exhibit's id, "contradicts" | "agrees"), ...)`: the relation the host builder computed with `decision/options.py::contradicts`
        and hands over as data, so `modules/social_contest/evidence.py::standing` reads it and restates no pairing rule;
      * `answered_band` -- the band label (`dice_engine.DEGREE_LABEL`) of the best answering act drawn against it, `None` while none has been."""
    id: str
    kind: str
    weight: float
    source: Optional[str] = None
    about: Optional[str] = None
    sincere: bool = True
    side: Optional[str] = None
    rung: Optional[str] = None
    cell: tuple = ()
    origin: Optional[str] = None
    forged_found: bool = False
    pairs: tuple = ()
    answered_band: Optional[str] = None


@dataclass(frozen=True, kw_only=True)
class Present:
    """Everyone in the room: participant, adjudicator, audience (V2 p2 §A.1). Built by the host from `World`; read-only.

    ONE INVARIANT (A-139, as corrected): a sitting has at least two distinct characters (`Input.__post_init__`).
    `side` and `decides` are independent cells: a party may also decide, and he is partial by the same reading as anyone.

      * `id`, `weight` -- a cohort is a person at weight above one;
      * `side`         -- `"for"` | `"against"` | `None`   } the role is these two cells;
      * `decides`      -- he ADJUDICATES                    }
      * `focus`, `reason`, `attunement`, `presence`, `grace`, `will` -- his six attributes;
      * `rank`         -- his rank in the proceeding's skill;
      * `care`         -- `(want, hold, bond)` in 0..1: how much each kind of thing moves him (0.5 where none);
      * `stake`        -- `(want, hold, bond)` in -1..1: how THIS matter bears on him, toward `for`;
      * `bonds`        -- `((other person, -1..1), ...)`;
      * `start`        -- where his track starts (host: `start_step` x mean(stake), plus the arrangement);
      * `holds`        -- `((channel, tag, weight, how the matter bears on it), ...)`: his wants and convictions, tag by tag;
      * `believes`     -- what he KNOWS of the matter, -1..1 toward `for` (his own ledger);
      * `bias`         -- his stable misjudgement of what his options are worth: -1 pessimist .. +1 optimist;
      * `power`, `precedence` -- his circumstances: seat, office, wealth, influence, faction (host);
      * `items`        -- the `Item`s he holds;  `strain` -- what he carries in from earlier rattles."""
    id: str
    weight: int = 1
    side: Optional[str] = None
    decides: bool = False
    focus: float
    reason: float
    attunement: float
    presence: float
    grace: float
    will: float
    rank: float
    care: tuple = (0.5, 0.5, 0.5)
    stake: tuple = (0.0, 0.0, 0.0)
    bonds: tuple = ()
    start: float = 0.0
    holds: tuple = ()
    believes: float = 0.0
    bias: float = 0.0
    power: float = 0.0
    precedence: int = 0
    items: tuple = ()
    strain: float = 0.0


@dataclass(frozen=True, kw_only=True)
class Rite:
    """The type's cells (V2 p2 §B), read by the module; it compares no row, move or person id (a move is read by its `effect`).

      * `id`; `live` -- what the live thing is called (claim, offer, question, charge, motion, theme, plea);
        `bears` -- which side bears it: he opens;
      * `reply`   -- per side, `((side, must | may | raise), ...)`;
      * `silence` -- what not answering a standing point means here: `admits` | `refusal` | `free` (A-145);
      * `issues`  -- the stasis rungs it runs through (`rosters.yaml: issue_rungs`);
      * `weighs`  -- stasis: what each rung is argued from, `((issue, ((ground, weight), ...)), ...)`;
      * `concede`  -- `descends` | `accepts`;
      * `moves`   -- per side, `((side, (argue | press | rest | concede, ...)), ...)`;
      * `close`   -- `bench` | `declared` | `hearers` | `consent` | `exchange` (the abridged form);
      * `turns`   -- each speaker's turns this sitting; `standard` -- the Grace the occasion asks; `reason_lean` -- the
        venue's lean on Reason's share of the dice; `admits` -- the kinds of matter shown here;
      * `difficulty`, `gravity` -- the obstacle the close is drawn against; `gravity` is how grave the times make a change
        (renamed from `stakes`); `quorum` -- read by a `declared` close; `unrest` -- the pull of the times (Focus holds against it).

    B24.10 (the hearing's cells, from the rite and read by the module's board, B24.06; each defaulted, so a rite built without them is the rite it was):
    `faults` -- the `proceeding_faults` the sitting records; `disclosed` -- whether the other side's filings stand on a mover's board;
    `bears_by_rung` -- `((rung, side), ...)`, who bears each rung of the issue ladder (`bears` is the bearer of the first)."""
    id: str
    live: str
    bears: str
    reply: tuple
    silence: str
    issues: tuple
    weighs: tuple
    concede: str
    moves: tuple
    close: str
    turns: int
    standard: float
    reason_lean: float
    admits: tuple
    difficulty: float
    gravity: float
    quorum: Optional[int] = None
    unrest: float
    faults: tuple = ()
    disclosed: bool = False
    bears_by_rung: tuple = ()


@dataclass(frozen=True)
class Cond:
    """One person's condition in a sitting (V2 p2 §C.1): `rattles` landed on him, `strain` he carries, `heat` this sitting's
    provocation (a rattle adds one; it cools at each beat he makes), `spoken` his turns had, `spent` staying power used."""
    rattles: int = 0
    strain: float = 0.0
    heat: float = 0.0
    spoken: int = 0
    spent: float = 0.0


@dataclass(frozen=True)
class Point:
    """A point on the table (V2 p2 §C.1): `id`, `side`, `issue`, `ground`, `item`, `by` (its maker), and `held` -- how far it
    stands with each listener, `((person, value), ...)`."""
    id: int
    side: str
    issue: str
    ground: str
    item: Optional[str]
    by: str
    held: tuple


@dataclass(frozen=True)
class Sitting:
    """A sitting's value (V2 p2 §C.1): `Input.state` is a whole one, so a resume needs no replay.

      * `n` -- beats so far; `issue` -- the rung reached; `points` -- every `Point`, older ones kept;
      * `live` -- `((side, the side's live point id | None), ...)`: one live point a side;
      * `tracks` -- `((person, value), ...)`, each person's own running `start + the beats' moves` (never a verdict);
      * `cond` -- `((person, Cond), ...)`; `used` -- grounds and items used, for staleness;
      * `last_voice` -- `((side, who spoke last for it), ...)`; `ended` -- `None` | `budget` | `rested` | `yielded`.

    B24.06 adds the board (each defaulted, and each in `UNWRITTEN`: no sitting writes them yet, B24.14): `board` -- `((Item, status), ...)` in the order
    entered, an `Item` carrying the side it stands for and the weight it entered at (what it counts for now is `evidence.standing`'s, B24.19), `status` `stands` |
    `answered` (stands, an answer tried and failed or halved it) | `struck` (by `standing`) | `withdrawn` (refused at entry, the lighter of two of one side's); `faults` -- `((a `proceeding_faults` member, the side at fault), ...)` in order; `levels` -- `((side, how many), ...)`, each a
    level against that side on the closing draw (a fault's, or a failed `impugn`'s)."""
    n: int = 0
    issue: int = 0
    points: tuple = ()
    live: tuple = _NO_POINT
    tracks: tuple = ()
    cond: tuple = ()
    used: tuple = ()
    last_voice: tuple = _NO_POINT
    ended: Optional[str] = None
    board: tuple = ()
    faults: tuple = ()
    levels: tuple = ()


@dataclass(frozen=True)
class Option:
    """One entry of `View.options` (V2 p2 §E): `move`, `ground`, `item`, `relation`; `ev` its PERCEIVED worth and `p` its perceived
    chance; `frame` -- argue: what of the listeners' it is framed on; press: the held thing it hits."""
    move: str
    ground: Optional[str]
    item: Optional[str]
    relation: str
    ev: float
    p: Optional[float]
    frame: Optional[str] = None


class Choice(NamedTuple):
    """A chooser's pick for one exchange (V2 p2 §E): the move, and where it takes one the ground, the item and the relation."""
    move: str
    ground: Optional[str] = None
    item: Optional[str] = None
    relation: Optional[str] = None


@dataclass(frozen=True)
class Beat:
    """The typed record of one exchange (V2 p2 §C.1); no text field. `terms` (true values) is in the outcome only.

      * `n`, `mover`, `voice`, `side`, `move`, `relation`, `issue`, `ground`, `item`, `point`, `target`;
      * `margin` -- the speech's margin; `drift` -- how far he was pulled off the point;
      * `evaded` -- PRICED: a point he must answer left standing, or a matter he bears not put;
      * `left` -- the other side's point that stood against him and that he did not answer, in any rite, priced or not;
      * `insincere` -- 0..1; `caught` -- those whose reading of him turned a speech he did not hold;
      * `rattled` -- whom it rattled; `frame` -- the frame of an argument or the object of a press;
      * `relevance` (Reason), `heard` (Presence), `esteem` (Grace) -- the operands of the speech;
      * `broke` -- he spoke with his temper broken; `moved` -- each listener's move; `closed` -- how it ended the sitting;
      * `mood` -- the room's, named only at the beat that turns it; `terms` -- true values.

    B24.06 adds the board's three cells, each defaulted and after `terms`: `entered` -- the ids of the items this exchange put on the board;
    `struck` -- the ids it struck; `fault` -- the first `proceeding_faults` member it recorded. The item a move uses is `item`, as it always was.

    ⚠ EVERY FIELD BUT THOSE IN `UNWRITTEN["Beat"]` IS WRITTEN: `loop/resolve.py::_BEAT_CELLS` and `queries/world_q.py::EndedBeat` both read `written(Beat)`,
    so a field added here and left out of `UNWRITTEN` is a cell of every proceeding's `Event.ending` and moves the content hash."""
    n: int
    mover: str
    voice: str
    side: str
    move: str
    relation: str
    issue: str
    ground: Optional[str]
    item: Optional[str]
    point: Optional[int]
    target: Optional[str]
    margin: float
    drift: float
    evaded: bool
    left: Optional[int]
    insincere: float
    caught: tuple
    rattled: Optional[str]
    frame: Optional[str]
    relevance: float
    heard: float
    esteem: float
    broke: bool
    moved: tuple
    closed: Optional[str]
    mood: float
    terms: tuple = ()
    entered: tuple = ()
    struck: tuple = ()
    fault: Optional[str] = None


#: THE CELLS OF A RECORD THE EVENT'S `ending` DOES NOT CARRY AS CELLS, by record name (B24.06; the ONE OWNER, read through `written`): `Beat.terms` (the true
#: values are never written) and the board's cells (a cell on every beat and every sitting of every proceeding is a hash mover, the realm's own `tell` sittings
#: among them). B24.14 WRITES `Beat.entered` and `Beat.struck` AS THE EXCHANGE LIST (`exchanges`, one `("exchange", kind, item)` tuple beside the beats, only
#: where a sitting entered or struck an item), so they stay in this row: they are not a cell of a beat. `Beat.fault` and `Sitting.board`, `.faults`, `.levels`
#: are written by nobody yet.
UNWRITTEN = {"Beat": ("terms", "entered", "struck", "fault"), "Sitting": ("board", "faults", "levels")}

#: THE BEAT CELLS THAT ARE THE EXCHANGE LIST, in the order an exchange lists them (B24.14): an item an exchange put on the board, then one it struck. Each
#: cell's name is the kind of the stage written.
EXCHANGE_CELLS = ("entered", "struck")


def exchanges(beats) -> tuple:
    """B24.14 -- THE EXCHANGE LIST OF A SITTING: `((kind, item id), ...)`, one for each item a beat entered or struck, in the beats' order and within a beat
    in `EXCHANGE_CELLS` order. The one owner of the list: `loop/resolve.py::_proceeding_ending` carries it on the Event's `ending` and
    `loop/effects_information.py::_eff_determine` appends it to the case file's `Record.stages`, so the two are one value. `()` where no beat entered
    or struck an item (every sitting at `sitting_exchanges` 0)."""
    return tuple((cell, iid) for b in beats for cell in EXCHANGE_CELLS for iid in getattr(b, cell))


def written(cls) -> tuple:
    """The names of `cls`'s fields the Event's `ending` carries, in the record's declared order: every field but `UNWRITTEN[cls.__name__]`.
    `loop/resolve.py::_proceeding_ending` writes them and `queries/world_q.py::EndedBeat` reads them back, both through this."""
    return tuple(f.name for f in fields(cls) if f.name not in UNWRITTEN.get(cls.__name__, ()))


@dataclass(frozen=True)
class View:
    """What a chooser sees each exchange (V2 p2 §E): own values true; everything else perceived, each with its own noise, or public.

      * `n`, `mover`, `side`, `issue`, `turns_left`;
      * `live_theirs`, `live_own` -- `(point, ground, item, perceived strength)` or `None`;
      * `options` -- `Option`s: perceived worth and chance; `own` -- his `Cond`;
      * `esteem`, `weary`, `awe` -- his standing, his weariness, how far those who decide cow him;
      * `broke` -- his temper has broken: he cannot hold his tongue, and `rest` is not on his menu (A-146);
      * `visible` -- each speaker's rattles; `mood`, `odds` -- the room as he reads it, and P(carried) on that reading before an ordinary bench;
      * `intent` -- the perceived stake of the man opposite; `acc` -- his accuracy;
      * `burden` -- he bears the matter and no point of his stands: resting is a charge not pressed;
      * B24.05 (each defaulted): `board` -- the `Item`s standing and struck, as the rite discloses them to him;
        `hand` -- his own `Item`s not yet shown."""
    n: int
    mover: str
    side: str
    issue: str
    turns_left: int
    live_theirs: Optional[tuple]
    live_own: Optional[tuple]
    options: tuple
    own: Cond
    esteem: float
    weary: float
    awe: float
    broke: bool
    visible: tuple
    mood: float
    odds: float
    intent: float
    acc: float
    burden: bool = False
    board: tuple = ()
    hand: tuple = ()


@dataclass(frozen=True)
class JudgeView:
    """What a played adjudicator has at the close (V2 p2 §D): his OWN mind (he knows it), `track` and `odds`, the `points` as they
    stood, and `tells` -- `((participant, perceived insincerity, perceived discomfort), ...)` by his Attunement. He rules at the
    close only and asks nothing during the sitting."""
    id: str
    track: float
    odds: float
    points: tuple
    tells: tuple = ()


@dataclass(frozen=True)
class Input:
    """What the proceeding entry reads, and nothing else (V2 p2 §C): built by the host from `World`.

      * `rite` -- the `Rite`; `matter` -- what is argued;  `room` -- the `Present` records;
      * `grounds` -- `((ground, reason weight, era weight), ...)`; `dials` -- the settings, a mapping;
      * `state` -- a whole `Sitting` to resume, or `None` (a resume needs no replay);
      * `frames` -- `((channel, tag), ...)`: the wants and convictions a speech here can be framed on.

    `__post_init__` holds the one invariant (A-139) and refuses, each a `ValueError` whose message begins `refused[<key>]`:
    `one_character`, `abridged_self`, `no_weight`, `no_adjudicator`, `nobody_speaks`, `resume_yielded`, and, a resume being
    lawful only for the same people with a turn left, `abridged_resume`, `closed`, `room_changed`, `spent`."""
    rite: Rite
    matter: str
    room: tuple
    grounds: tuple
    dials: Mapping
    state: Optional[Sitting] = None
    frames: tuple = ()

    def __post_init__(self):
        room, rite, state = self.room, self.rite, self.state
        if len({p.id for p in room}) < 2:
            raise ValueError("refused[one_character]: a sitting with one character (A-139)")
        if rite.close == "exchange" and not any(p.decides and not p.side for p in room):
            raise ValueError("refused[abridged_self]: an abridged act needs someone addressed other than the speaker")
        if any(p.weight <= 0 for p in room):
            raise ValueError("refused[no_weight]: a person or cohort of no weight")
        if rite.close != "consent" and not any(p.decides for p in room):
            raise ValueError(f"refused[no_adjudicator]: close `{rite.close}` with nobody to adjudicate")
        if not any(p.side for p in room):
            raise ValueError("refused[nobody_speaks]: nobody speaks")
        if state is None:
            return
        if state.ended == "yielded":
            raise ValueError("refused[resume_yielded]: a sitting that ended `yielded` is not resumed (an adjourned one is)")
        if rite.close == "exchange":
            raise ValueError("refused[abridged_resume]: an abridged act is one speech; it is not resumed")
        if state.ended == "rested":
            raise ValueError("refused[closed]: a sitting that ended `rested` was closed on what was said; its close is not drawn again")
        if {p.id for p in room} != {i for i, _ in state.tracks}:
            raise ValueError("refused[room_changed]: a resumed sitting has the same people; a changed room is a new sitting")
        spoken, moves = {i: c.spoken for i, c in state.cond}, dict(rite.moves)
        if not any(p.side and moves.get(p.side) and spoken.get(p.id, 0) < rite.turns for p in room):
            raise ValueError("refused[spent]: no speaker has a turn left; a close once drawn is not drawn again")


@dataclass(frozen=True)
class Outcome:
    """What the proceeding entry returns (V2 p2 §M): `beats`, the whole `state` (a `Sitting`), `ended` and `ended_by`, `verdicts`,
    and `ruled` -- `((decider, how far his ruling departed from his own track), ...)` for a played judge.

    `verdicts` is a tuple of `(id, Margin)`: margins, never a band, a side or a winner: the host grades each on the one
    ladder (`seam/ladder.py::degree_of`).

    B24.05 (each defaulted): `standing` -- the `Item`s left standing on the board at the close; `faults` -- the `proceeding_faults`
    members recorded over the sitting, in order. Neither names a side or a winner."""
    beats: tuple
    state: Sitting
    ended: str
    ended_by: Optional[str]
    verdicts: tuple
    ruled: tuple = ()
    standing: tuple = ()
    faults: tuple = ()


@dataclass(frozen=True)
class Card:
    """What the proceeding IS (V2 p1 §E): derived by the host from the arranged rite and the room (B24p.13), NEVER authored; every
    participant reads it before and during a sitting. It holds no true attribute and no true start.

      * `kind`, `genre`; `arranged_by`, `tilt`, `tilted_against` -- who tilted the forum, how far, against whom (named only where there is a tilt);
      * `stake` -- what is disposed; `outcomes` -- `((band, the typed writes), ...)`;
      * `room` -- `((person, role, visible circumstances), ...)`;
      * `live`, `bears`, `reply`; `moves`, `barred`; `admits`;
      * `close`; `decided_by` -- the adjudicators (none under consent: each party's own accept);
      * `turns`, `issues`;
      * `silence` -- what not answering a standing point means here; `unargued` -- what happens to the matter if nobody speaks;
        `ends` -- when it closes;
      * `standard` -- the Grace asked; `unrest` -- the pull of the times (Focus); `gravity` -- how grave a change is;
      * `reason_weight` -- Reason's share of the dice per ground here; `recused` -- seats that stepped down for a conflict;
      * `odds` -- P(carried) of the close itself where nobody speaks; `None` where nothing is drawn (consent) or the verdict is the speech itself."""
    kind: str
    genre: str
    arranged_by: Optional[str]
    tilt: float
    tilted_against: Optional[str]
    stake: str
    outcomes: tuple
    room: tuple
    live: str
    bears: str
    reply: tuple
    moves: tuple
    barred: tuple
    admits: tuple
    close: str
    decided_by: tuple
    turns: int
    issues: tuple
    silence: str
    unargued: str
    ends: str
    standard: float
    unrest: float
    gravity: float
    reason_weight: tuple
    recused: tuple
    odds: Optional[float]


@dataclass(frozen=True)
class PersonalCombatInput:
    """What the `combat` module's fight reads, and nothing else (plan position `31b`).

    Built by `seam/wrappers/combat.py::combat_input` (the host input builder) from `World`:
      * `claimants` -- the two parties' ids, `(A, B)`: each is a `Combatant` label, and the engine's
                       result is `+1` when A wins, `-1` when B does, `0` UNRESOLVED (a ruled outcome);
      * `ends`      -- each party's `end`, in `claimants` order (`combat.py::party_end`, `H-97`): the authored
                       `attr.body.endurance` (else the class default) less the body-band penalty, floored at 1;
      * `wound_quantities` -- the `WoundTracker` fields the host reads per party after the fight
                       (`rosters.yaml: wound_quantities`, in roster order) and the decider's view lifts. The module
                       returns `PartyWounds`'s five fixed fields whatever it names; the refusal for a name that
                       record lacks is the host's (`combat.py::_wound_state`);
      * `terms`     -- the duel's terms (RS-25, PC-10a, CP-T03-09): one of `modules/combat/wrapper.py::DUEL_TERMS`,
                       read by the module entry and handed to `wrapper.fight`. The default is the STRING `'death'`
                       (the engine's `LETHAL_TERMS`, pinned equal by `engine/season/tests/test_cp_t03_09_capture.py`), never `None`:
                       `wrapper.fight` refuses a term outside `DUEL_TERMS`, so a `None` default would raise. The ONE path
                       a non-lethal term reaches the fight by is `combat.py::combat_input`, from `rosters.yaml:
                       duel_terms` -- and, since v10 PC-10b, from the `stakes` of the `challenge` Record an
                       `accept` is about (`world_q.stakes_of`), into this same field through the same function;
      * `kits`      -- each party's kit, `(weapon, armor)`, in `claimants` order, `ends`' shape (CP-T03-03,
                       `world_q.kit_of`: what the rungs the person holds store, read not consumed). The module
                       passes each to `Combatant(..., weapon=, armor=)`. The default is `()`: a record built
                       without kits is fought by two Combatants at the engine's own default kit;
      * `scores`    -- each party's SKILL SCORE for the fight's verb, in `claimants` order, `ends`' shape (CR-85, ED-IN-0330,
                       B05.57; `seam/wrappers/pool.py::score`: no attribute, no addend; 0 where the skill gives him none). Passed
                       to `Combatant(..., score=)`, where it is the number the opponent's Ob is taken from
                       (`core.ob_from_defender`) and the base of his own pool. The default is `()`: a record built without it
                       is fought at the module's own default (3);
      * `addends`   -- each party's registered pool addends for the verb, the sum of `pool.py::POOL_ADDENDS` (`pool.addends_of`,
                       whole dice), in `claimants` order. The pool is `pool_of(score, addends, pool_add, pool_floor)`: the addend
                       raises his pool and never an opposition (A-79). The default is `()`: none;
      * `pool_add`, `pool_floor` -- the fight's row's two operands, carried raw from the fixtures the `fight` site's `dice` row
                       names (`rosters.yaml: tables.capability_uses`; `pool_add`, `pool_floor`). `None` is the module's own
                       constants (`core.BASE_POOL`, `core.POOL_FLOOR`), the workbench's;
      * `opposition_rate` -- the share of a defender's skill score the obstacle takes per point, carried for
                       `sigma_leverage.opposed_ob`. `None` is the module's own constant (0.5): in B05 `combat_input` carries
                       `None`, and the flip to the fixture belongs to B15;
      * `carried`   -- each party's wound carried into the fight, as a SIGNED net sigma (a level against his own rolls is negative), in
                       `claimants` order (B05.61, `UPR` §3 edit 2; A-8). The host reads it once, from the `wounds` advantage source alone
                       (`combat.py::_carried_of`: `levels_to_net_sigma` over that member's against-list for the party's own `body`), and
                       fills it only under `Fixtures carried_wound_model` `level`; the default `(0.0, 0.0)` is `endurance_cut`, the control,
                       where the wound rides on `ends` instead. The module adds the aggressor's against his attack and the defender's against
                       his defence beside `wound_impairment` (`combat_systems.assemble_net_sigma`) and holds no `wound_step` of its own;
      * `attributes` -- each party's authored `Person.attributes`, `{registry key: whole number}`, in `claimants`
                       order (PC-06 K-1, ED-IN-0347). The module maps each key to its `Combatant` field by PC-14's
                       `registry_key` (`modules/combat/attributes.py`); a key absent from the dict leaves its field at
                       the class default, and `end` is carried by `ends`, not read from here. The default is `()`:
                       `combat_input` fills it only when a claimant has an authored attribute;
      * `traditions`, `techniques`, `axes`, `dispositions` -- the WORKBENCH's four fields (B14.11, `03_PC_typed_outcome_one_door`
                       Part B), each one entry per party in `claimants` order, `ends`' shape, each entry `None` where that party
                       gives none, each defaulting to `()` so every record built before them is the record it was. The module
                       passes them to `Combatant(..., tradition=, equipped=, skills=, disp=)` as it passes `kits`:
                       `traditions` a tradition name; `techniques` `{name: level}` (a list of names is each at level 1.0);
                       `axes` `{axis: bonus}` (`Combatant`'s own attribute stays `skills`); `dispositions` the `disp` number.
                       The season fills none of them until a carrier exists (`03_PC_person_inputs_content.md`);
      * `mortal`    -- the MORTAL-WOUND DRAW's operands (B15.07, PHY_A A3), one entry per party in `claimants` order: `(pool, obstacle,
                       levels_for, levels_against, key)`. `(pool, obstacle)` is `queries/world_q.py::mortal_terms` at the record's
                       `terms`; the levels are tuples of `sigma_leverage.LEVEL_SIGMA` names, the host's reading of the `mortal` site's
                       `edge` rows and the `wounds` advantage source (`combat.py::_mortal_operands`); `key` the 16-hex key of the keyed
                       draw `(world_seed, tick, party, "fight.mortal:<causing act>")` (A-30, `state.ids.draw_factory`), never a position in the scene's
                       stream -- a key, not a `Draw`, so the record stays a value -- or `None` for a sampled estimate, whose draw is a
                       sub-key of its own private stream. The module draws (`modules/combat/fight.py::mortal_wound`) for each party the
                       scene felled. The default `()` is no draw: a felling stands, as before the draw;
      * `decisiveness` -- each party's σ for the YIELD ROLL (B15.10, `PC_A`, A-24), in `claimants` order: what the host knows that the module does
                       not (what he is fighting for). It enters the roll as `net_sigma`, under the owner's soft cap, beside his Spirit and wounds
                       (`wrapper._yield_roll`). The host reads it from `person_q.decisiveness` (`combat.py::combat_input`). The default `()` is
                       0.0 for both parties (`fight.py` passes `inp.decisiveness or (0.0, 0.0)`)."""
    claimants: tuple
    ends: tuple
    wound_quantities: tuple
    terms: str = "death"
    kits: tuple = ()
    scores: tuple = ()
    addends: tuple = ()
    pool_add: Optional[float] = None
    pool_floor: Optional[float] = None
    opposition_rate: Optional[float] = None
    carried: tuple = (0.0, 0.0)
    attributes: tuple = ()
    traditions: tuple = ()
    techniques: tuple = ()
    axes: tuple = ()
    dispositions: tuple = ()
    mortal: tuple = ()
    decisiveness: tuple = ()


@dataclass(frozen=True)
class MortalResult:
    """ONE FELLED PARTY'S MORTAL-WOUND DRAW (B15.07, PHY_A A3), returned on `CombatOutcome.mortal` by the module
    (`modules/combat/fight.py::mortal_wound`) and MAPPED by the host onto that party's `felled` and `wounds`
    (`seam/wrappers/combat.py::_wound_state`), which computes nothing (holonic §44.3: a wrapper that computes an outcome is the second resolver).
      * `mortal` -- he dies: the draw's band was Failure, and `felled` stands;
      * `wounds` -- his wounds after the draw: at least `max_wounds` at Partial (left for dead), the scene's otherwise;
      * `degree` -- the band (`core.degree`'s label of the one ladder, `degree_from_net`), for the trace."""
    mortal: bool
    wounds: int
    degree: str


@dataclass(frozen=True)
class PartyWounds:
    """One party's lifted `WoundTracker`: five FIXED fields (B14.01), whatever `wound_quantities` names. The host's
    `seam/wrappers/combat.py::_wound_state` reads it by that roster and refuses, by name, a roster member this record
    lacks."""
    felled: bool
    wounds: int
    max_wounds: int
    health_remaining: int
    health_full: int


@dataclass(frozen=True)
class Surrender:
    """The scene's `yield` event, lifted off its trace by the module entry (B14.01). `round` is the round at whose
    start or end the yield came (A-101; the engine's trace event still names it `turn`)."""
    by: str
    round: int
    accepted: Optional[bool]   # `None`: the scene ended with the yielder standing under `death` terms, the victor's choice the host's (B15.10)


@dataclass(frozen=True)
class DecisiveBeat:
    """The wound that ended the scene: the trace's last `wound` event that felled its victim (B14.01).
      * `by`     -- the striker's id;
      * `victim` -- the felled party's id;
      * `source` -- the engine's own site name for the wound: exchange | bind | stophit | pursuit | displace_graze | finalblow_riposte (a counter that fells, B15.09);
      * `weapon` -- the striker's weapon key as the fight opened (the `fight_start` event; the `wound` event carries none);
      * `round`  -- the round it landed in (A-101; the count of `turn_start` events up to it)."""
    by: str
    victim: str
    source: str
    weapon: str
    round: int


@dataclass(frozen=True)
class SceneShape:
    """WHAT THE SCENE'S TRACE SAYS OF ITS COURSE, folded by the module entry from the trace it already holds (B14.15; a pure
    fold over `wound`, `turn_start` and `yield`, no new engine event). The host reads it off the result and puts it on the
    act's Events (`loop/effects_combat.py::_eff_kill`); nothing is kept between scenes.
      * `rounds`      -- rounds fought: the `turn_start` count (A-101; `CombatOutcome.rounds`);
      * `blows`       -- wounding blows LANDED, by claimant id (a `wound` event is emitted only for a blow that took Health);
      * `first_blood` -- who landed the first wounding blow, `None` where none landed;
      * `lead_changes`-- times the party ahead on Health fraction changed (a tie is no lead and no change);
      * `nearest`     -- each party's lowest Health remaining during the scene, in points (his Health when no blow reached him).
    A party whose Combatant carries no tracker has no full Health to read a fraction against: it is absent from `nearest`
    and the scene's `lead_changes` is `0`."""
    rounds: int
    blows: Mapping[str, int]
    first_blood: Optional[str]
    lead_changes: int
    nearest: Mapping[str, int]


@dataclass(frozen=True)
class CombatOutcome:
    """WHAT THE `combat` MODULE ENTRY RETURNS FOR ONE SCENE (B14.01; the combat entry's output record, as `Margin` is
    the social contest's).

    ⚠ THIS RECORD IS NOT A `Margin`, AND MUST NOT BE 'FIXED' INTO ONE. Combat's degree is read off its WOUND STATE
    (`seam/ladder.py::combat_degree` over `wounds`), never off a net and an obstacle; a `net`/`ob` pair here would
    make the module a second resolver (Jordan, 2026-09-03: *"kill/wound degrees should be directly taken from scene
    combat"*). Nor does it name a winner: who prevailed is the fold's reading of `wounds` and `surrender`.

      * `claimants` -- `(A, B)`, as the input;
      * `wounds`    -- `{claimant id: PartyWounds}`; a party whose Combatant carries no tracker is ABSENT (the host
                       refuses it by name);
      * `surrender` -- the scene's `yield` event the engine did not refuse, or `None` (a refused declaration is not a surrender);
      * `beat`      -- the wound that felled a party, or `None` when nobody was felled;
      * `rounds`    -- rounds fought (A-101; the `turn_start` count);
      * `shape`     -- the scene's course, folded from its trace (B14.15);
      * `trace`     -- the scene's events, for a viewer; `shape` and `beat` are the only folds of it;
      * `mortal`    -- `{party id: MortalResult}` for each party the scene felled, where the record carried the draw's operands
                       (`PersonalCombatInput.mortal`, B15.07); empty where it carried none. `wounds` stays the scene's tracker: the host maps
                       this onto it."""
    claimants: tuple
    wounds: Mapping[str, PartyWounds]
    surrender: Optional[Surrender]
    beat: Optional[DecisiveBeat]
    rounds: int
    shape: SceneShape
    trace: tuple
    mortal: Mapping[str, MortalResult] = field(default_factory=dict)


@dataclass(frozen=True)
class CombatTurnView:
    """What a PLAYABLE fight's per-turn decider reads, and nothing else (v10 REM-31, IN-46).

    Built by the `combat` module entry (`modules/combat/fight.py::fight`) at the top of each turn, before
    any draw of that turn, and handed OUTWARD to the host's decider -- the one record that crosses the
    module boundary in that direction. It names the quantities the input record already names and the
    turn index, never a `Combatant` (the design's `## Re-read at B-L`, [ASSUMPTION]):
      * `turn`        -- the 1-based turn about to be fought;
      * `claimants`   -- `PersonalCombatInput.claimants`, `(A, B)`;
      * `wound_state` -- `{id: {quantity: value}}` over `PersonalCombatInput.wound_quantities`, a fresh copy
                         per call, so a decider that mutates it moves nothing in the engine."""
    turn: int
    claimants: tuple
    wound_state: Mapping


@dataclass(frozen=True)
class PlayHost:
    """THE HOST'S ONE OPTIONAL ARGUMENT for PLAYABLE (v10 REM-31, IN-46; A-25's *"a `game/` scene for which
    the driver suspends"*). `SeasonDriver.season(..., host=)` threads it to ENCOUNTER alone, through
    `_contest` and `seam/contest.py::contest` to the provider, the path `contest_max_depth` already takes.
      * `persons` -- the ids the host plays. The mode is a PARTY TEST at the provider
                     (`seam/wrappers/combat.py::resolve`): a fight either of whose claimants is in this
                     set is PLAYABLE; every other fight, and every fight with no host, is AUTOMATED;
      * `decide`  -- `(CombatTurnView) -> str`, one member of the engine's closed per-turn set
                     (`modules/combat/wrapper.py::TURN_CHOICES`). It is written to draw nothing, write nothing and
                     hold no token (CONVENTION; `test_rem31_grid_suspension.py::test_no_draw_and_no_mint_while_suspended` checks the shipped deciders): it is called inside the provider's frame, with the driver below it on
                     the stack (a call-out, not a return), and its return is the only resume.
      * `deciders` -- B24.05, `module role -> decide(view) -> choice` (`social_contest.proceeding`, ...): the role-keyed form `decide` is
                     the first of. `decide` stays for `combat.fight` until B34 folds it into `deciders["combat.fight"]`. The wrapper
                     resolves a role's decider here and passes it as `decide=`; a role with none is automated for this host. Empty by
                     default, so a host built as before is the host it was.
    Nothing records the mode: no Event, id purpose, carrier or `RESOLVED` field names it."""
    persons: frozenset
    decide: Callable
    deciders: Mapping[str, Callable] = field(default_factory=dict)


@dataclass(frozen=True)
class FieldOrder:
    """CP-T04-02: ONE SIDE'S STANDING ORDER as the field reads it -- the content of the `standing_order`
    Record `seam/wrappers/mass_battle.py::field_input` chose (`rosters.yaml: record_kinds`): `role`, a `config.ROLE_SPEC`
    name the module maps onto each subunit of the side's line, and `retreat_at`, one of `ORDER_RETREAT_AT`, which the
    module reads (CP-T04-03) as each subunit's `own_strength` retreat Order. Plain strings: the closed sets are the module's (`engine/substrate/battle_orders.py`)."""
    role: str
    retreat_at: str


@dataclass(frozen=True)
class MassBattleInput:
    """What the `mass_battle` module's field reads, and nothing else (plan position `31c`).

    Built by `seam/wrappers/mass_battle.py::field_input` (the host input builder) from `World`, after
    the adapter's PARTY-GAP checks and its `Unopposed` branch (an empty defending side is never fought):
      * `weights`   -- `(attacker, defender)`, each a tuple of `Person.weight`, one per side member
                       `World` holds, in side order: the claimants, then the subject's members mustered
                       at the rung. The module sums each into its side's troops;
      * `territory` -- the geography territory id of the place fought over, or `None`
                       (`mass_battle.py::_territory_of`);
      * `fort_level` -- its fortification, `world_q.fortification_of`, in `[0.0, 1.0]`;
      * `stances`   -- `(attacker, defender)`: each side's weight-mean stance toward its own faction
                       (`mass_battle.py::_side_stance`), which the module turns into a morale-start. ⚠ Since
                       v11 CR-87 (5) that referent also carries every member's build-time loyalty row (H-256);
                       the morale-start reads it with no gain;
      * `walls_dr`  -- the `field_walls_dr` fixture (`H-150`); `None` is A.9's own number, which the
                       module reads from its terrain table;
      * `origin`    -- the geography territory id the attacking side marched from, or `None` where it
                       has no one origin (`mass_battle.py::_origin_of`, MB-05r). The module decides from
                       it and `territory` whether the march crossed a river (`terrain.py::river_crossed`);
      * `loyalties` -- `(attacker, defender)`: each side's weight-mean build-time loyalty row, the
                       stance toward its faction creed's utterer (`mass_battle.py::_side_stance` with
                       `_creed_referent`, MB-03), which the module adds to the morale-start at
                       `loyalty_gain`. ⚠ Since v11 CR-87 (5) no built realm holds such a row (the loyalty row
                       names the creed Proposition), so this reads 0 whatever `loyalty_gain` is (H-256);
      * `loyalty_gain` -- the `field_morale_loyalty_gain` fixture (`H-148`'s site); `0` is the control,
                       battle history only;
      * `members`   -- CP-T04-01: `(attacker, defender)`, each a tuple of person ids, ONE PER ENTRY OF `weights`, in the
                       same order (`field_input` filters both by the same test). Read only on the `person` arm;
                       `((), ())`, the default, names nobody;
      * `units`  -- CP-T04-01: the `field_units` fixture (`H-359`), `side` or `person`. `side`, the default, is
                       the side as it was: one subunit sized by Σ weight. `person` is one subunit per member;
      * `orders`    -- CP-T04-02 (`H-361`): `(attacker, defender)`, each a `FieldOrder` or `None`, the standing order
                       `field_input` read for that side (the `standing_order` Record its faction's seat holds
                       about the side's settlement whose holder edge is newest). `None`, the default, is both sides
                       without one: the field as it was;
      * `geography` -- the parsed geography file (`data/geography.py::geography`, read once per process
                       and SHARED by every record: read-only). The module's terrain lookup and river test
                       read it here and open no file. `repr=False`: a record in an assertion message
                       prints its facts, not a 37 KB map;
      * `condition_scale` -- B17.03: the body scale (`Fixtures condition_scale`) the module quantises each survivor share onto
                       (`FieldOutcome`): a share is `round(condition_scale x hp_left / hp_start)`, so a side the battle never
                       touched reads exactly the scale. The host's, handed on unread;
      * `orders_of_battle` -- ED-IN-0306: `(attacker, defender)`, each an `OrderOfBattle` (the module's own typed
                       record, `modules/mass_battle/orderofbattle.py`, held here as an opaque value: `engine/`
                       imports no module code) or `None`. `None` on both sides -- the default -- is the field as
                       it was: one headcount line per side. A side with an order of battle fights as that order
                       says; the record's headcounts are authoritative and `weights` is not read for that side."""
    weights: tuple
    territory: Optional[str]
    fort_level: float
    stances: tuple
    walls_dr: Optional[int]
    origin: Optional[str]
    loyalties: tuple
    loyalty_gain: float
    geography: Mapping = field(repr=False)
    condition_scale: int
    orders_of_battle: Optional[tuple] = None
    members: tuple = ((), ())
    units: str = "side"
    orders: Optional[tuple] = None


# B17.03: THE FIELD'S OUTPUT RECORD, on every arm. `modules/mass_battle/massbattle.py::resolve_field` returns one; the host adapter
# (`seam/wrappers/mass_battle.py::resolve`) lifts it, `seam/ladder.py::field_degree` reads the band off its two sides' flags and
# `loop/effects_combat.py::_eff_march` writes each person's casualty from the share of the part he is, else of his side.
# FIELD_ENDED is the one closed set of how a field stopped; the base fields are declared HERE and the other fields of the one
# `FieldOutcome` land each with its own proposal and are declared nowhere else (D-U1-11e).
FIELD_ENDED = ("rout", "concession", "time")


@dataclass(frozen=True)
class PartOutcome:
    """One part of a side: a member's person id (the headcount `person` arm) or a cohort's (the army path). `share` is its
    survivors on the body scale, `round(condition_scale x hp_left / hp_start)`, `0..scale`; `routed` is whether its unit broke."""
    id: str
    share: int
    routed: bool


@dataclass(frozen=True)
class SideOutcome:
    """One side of a finished field. `share` is the side's survivors on the same scale; `parts` are its `PartOutcome`s in
    input order, `()` on the headcount `side` arm; `broke_first` is the part id that broke on its own account first (the engine's
    own order of breaking, `battle_loop.run_battle`), or `None`."""
    share: int
    routed: bool
    conceded: bool
    parts: tuple
    broke_first: Optional[str]


@dataclass(frozen=True)
class FieldOutcome:
    """What the mass-battle module's field returns (B17.03; A-3: no `verdict`, the host's `field_degree` reads the band off the two
    sides' flags). `ended` is `FIELD_ENDED`: `rout` when a side's army routed, `concession` when a side gave the field up,
    `time` when the ticks ran down; `ticks` is the field's ticks run. Shares are integers on the body scale, quantised at this seam
    (A-29: the engine's floats are declared floats now; this is not an integer-state commitment)."""
    ended: str
    ticks: int
    attacker: SideOutcome
    defender: SideOutcome

    def __post_init__(self) -> None:
        if self.ended not in FIELD_ENDED:
            raise ValueError(f"FieldOutcome.ended {self.ended!r} is not one of {FIELD_ENDED}")


# ---------------------------------------------------------------------------
# v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`): THE FIELDWORK SCENE'S RECORDS -- the `inquiry` role's
# input and output, built and held by `seam/wrappers/fieldwork.py`, read by `modules/fieldwork/find.py`.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TrailItem:
    """One Event an inquiry COULD uncover: a covert deed the investigator did not witness
    (`epistemic.trail_of`, the host's projection). Its id, its kind and when it was emitted -- what
    the module orders by; the Event itself stays with the host."""
    event_id: str
    kind: str
    emitted_at: int


@dataclass(frozen=True)
class FieldworkInput:
    """What the fieldwork module's `find` reads, and nothing else.

    Built by `seam/wrappers/fieldwork.py::fieldwork_input` (the host input builder) from `World`:
      * `band`  -- the finding Event's degree (`Event.degree`), the one ladder's reading of the
                   inquiry's roll; `None` for an ungraded finding;
      * `items` -- the trail the host projected for the inquiry's subject (`TrailItem`s);
      * `terms` -- `rosters.yaml: finding_terms`, band -> the observation terms a finding at that band
                   shows. Handed in because a module holds no data (A-25), on `MassBattleInput.geography`'s
                   precedent."""
    band: Optional[str]
    items: tuple
    terms: Mapping


@dataclass(frozen=True)
class Findings:
    """What the fieldwork module's `find` returns, and the host adapter refuses anything else: per
    uncovered trail item, `(event id, the terms shown)`. Empty is a real answer -- nothing found."""
    found: tuple


# ---------------------------------------------------------------------------
# THE SETTLEMENTS MODULE'S LARDER RECORDS (v9 IN-07 E1; `proposals/2026-10-07-settlements-computation-
# modules.md` §3 E1, intent only). Read by `modules/settlements/larder.py`'s two `query` entries; built
# by `queries/world_q.py`'s projection builders, which also turn the output back into the public dict
# shapes. ⚠ EVERY COLLECTION IS AN ORDERED TUPLE, NEVER A MAPPING: the order the draw debits a rung's
# kinds reaches `Rung.stores`' insertion order (the content hash no longer reads it: GO-07 folds a
# mapping sorted by its encoded keys; the order still decides what a reader iterating `stores` sees).
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Eater:
    """One housed person the larder draw considers: id, home rung, `Person.weight` and
    `Person.is_cohort` -- the carrier's own predicate, handed in so the module never re-derives it."""
    pid: str
    home: str
    weight: int
    is_cohort: bool


@dataclass(frozen=True)
class LarderInput:
    """What `settlements.larder_draw` reads, and nothing else. Built by
    `queries/world_q.py::larder_input` from `World`:
      * `weights` -- `subsistence_weight`, `((kind, weight), ...)` sorted by kind;
      * `eaters`  -- every housed person (`home_of`), `Eater`s sorted by pid, cohort or not;
      * `ladders` -- `((home, (rung, parent, ...)), ...)`: each COHORT eater's home's containment
                     ancestry (only a cohort eats, so no other home is projected), the home first, cut at
                     the first id that is not a rung;
      * `stores`  -- `((rung, ((kind, units), ...)), ...)` for every rung on a cohort ladder, each in its
                     own `Rung.stores` order. An eater whose home has no ladder here draws from nothing,
                     so the cohort exemption (`larder_draw`'s) and this projection must agree."""
    weights: tuple
    eaters: tuple
    ladders: tuple
    stores: tuple


@dataclass(frozen=True)
class DrawRow:
    """One eater's draw: `cells` is `((kind, want, take, source or None), ...)` in kind order."""
    pid: str
    home: str
    cells: tuple


@dataclass(frozen=True)
class DrawRecord:
    """What `settlements.larder_draw` returns: one `DrawRow` per eating cohort, in pid order."""
    rows: tuple


@dataclass(frozen=True)
class Under:
    """What `settlements.drawn_under` reads: a draw, the subtree (`world_q._subtree`) whose homes
    count, and the column summed -- `"want"` (`demanded`) or `"take"` (`delivered`)."""
    record: DrawRecord
    subtree: frozenset
    column: str


# v9 IN-07 E2: the `settlements.subsist` step_call's records -- one season's subsistence ledger. Built by
# `queries/world_q.py::subsist_input`, read by `modules/settlements/subsist.py`, interpreted by MATTER
# (`loop/matter.py`), which makes every write from the outcome.

@dataclass(frozen=True)
class SubsistInput:
    """What `settlements.subsist` reads, and nothing else. Built by `queries/world_q.py::subsist_input`:
      * `larder`    -- the `LarderInput` the draw reads (`larder_input`'s projection);
      * `chains`    -- `((home, (home, parent, ..., root)), ...)` per COHORT home, sorted: each home's whole
                       containment ancestry (`ancestry`), NOT cut at a non-rung as a ladder is. A drained
                       rung's gap counts the eaters whose chain passes through it -- `_subtree`'s
                       membership read from the other end on a single-parent containment tree (every
                       builder's; `World.add_tenure` checks ascent, not uniqueness, and `parent_of`
                       takes the first live edge), which is what `demanded`/`delivered` sum;
      * `body_step` -- the `body_step` fixture: body lost per unit short (`0` is the control arm);
      * `bodies`    -- `((pid, Person.body), ...)` for every eater in `larder.eaters`, sorted by pid."""
    larder: LarderInput
    chains: tuple
    body_step: int
    bodies: tuple


@dataclass(frozen=True)
class BodyFall:
    """One body the season's dearth falls: who, and the body it falls to (`max(0, body - lost)`); the
    host reads death as `body_after <= 0`."""
    pid: str
    body_after: int


@dataclass(frozen=True)
class SubsistOutcome:
    """What `settlements.subsist` returns. Every collection is an ordered tuple:
      * `draw`            -- the `DrawRecord` (`settlements.larder_draw`'s, the same rule);
      * `short_by_person` -- `((pid, ((kind, units), ...)), ...)`, pid order then kind order;
      * `shortfalls`      -- `((rung, ((kind, units), ...)), ...)`: each drained rung (sorted) with its
                             subtree's positive gap per kind it ran out of (sorted), `want - take` summed;
      * `falls`           -- `BodyFall`s, pid order, only where the loss is `> 0`;
      * `larder_after`    -- `((rung, ((kind, units), ...)), ...)`, sorted rung, changed rungs only; kinds
                             in the order the draw first debited them (it reaches `Rung.stores`' order)."""
    draw: DrawRecord
    short_by_person: tuple
    shortfalls: tuple
    falls: tuple
    larder_after: tuple


# v9 IN-07 E3: the `settlements.produce` step_call's records -- one season's yield and credit. Built by
# `queries/world_q.py::produce_input`, read by `modules/settlements/produce.py`, interpreted by MATTER
# (`loop/matter.py`), which makes the `yield` and `stores` writes from the outcome.

@dataclass(frozen=True)
class ProduceInput:
    """What `settlements.produce` reads, and nothing else. Built by `queries/world_q.py::produce_input`:
      * `table`        -- `((site_kind, ((kind, base), ...)), ...)`: `SITE_YIELD`, each kind's bases in
                          its table order (that order reaches `Rung.stores`' key order);
      * `scale`        -- the `condition_scale` fixture, as MATTER read it;
      * `factor`       -- `((rung, factor), ...)`, sorted, one entry per rung in `stores` (the same rungs):
                          that rung's `world_q.season_factor_of`, as MATTER read it through
                          `world_q.season_factors_by_rung` (one draw a season per TERRITORY, keyed on its
                          rung id, so rungs of one territory read one factor; CL-EVENTS (1));
      * `sites`        -- `((site_id, site_kind, rung, condition), ...)`, every Site sorted by id;
      * `stores`       -- `((rung, ((kind, units), ...)), ...)`, every rung a Site stands on, sorted,
                          each in its own `Rung.stores` order, read BEFORE this season's debit is written;
      * `larder_after` -- `SubsistOutcome.larder_after` (E2): the debited rungs and kinds only. The module
                          overlays it on `stores`, because MATTER credits a rung after that rung's debit."""
    table: tuple
    scale: object
    factor: tuple
    sites: tuple
    stores: tuple
    larder_after: tuple


@dataclass(frozen=True)
class ProduceRow:
    """One producing rung: `produced` is its `yield` (`((kind, units), ...)`, nonzero only, site order
    then table order) and `credited` the stores it is written to (`((kind, held + produced), ...)`, in
    `produced`'s order, `held` read after the same rung's debit)."""
    rung: str
    produced: tuple
    credited: tuple


@dataclass(frozen=True)
class ProduceOutcome:
    """What `settlements.produce` returns: `rows`, one `ProduceRow` per rung with a nonzero yield, sorted."""
    rows: tuple


# v9 IN-07 E4..E6: the settlements module's three one-line `query` entries -- housing, a fabric's bound
# and share, a settlement's walls. Built by `queries/world_q.py`'s projection builders (one per half:
# `_housing_population_input`/`_housing_capacity_input`, `_fabric_ceiling_input`/`_fabric_share_input`;
# and `fort_input`), read by `modules/settlements/housing.py`, `fabric.py` and
# `fortification.py`; the public wrappers (`population`, `capacity`, `ceiling`, `share`,
# `fortification_of`) read the output back. ⚠ A HALF LEFT `None` WAS NOT PROJECTED: one record serves two
# public names (E4: `population` and `capacity`; E5: `ceiling` and `share`), and each wrapper projects only
# the half it reads, so it pays only the scans, `TRACE.query` rows and fixture reads its half needs
# (`residence_of` traces, `presence` traces, `Fixtures.reads` reaches `harness/corpus_run.py`'s
# report). The module answers `None` for a half it was not given.

@dataclass(frozen=True)
class HousingInput:
    """What `settlements.housing` reads. Built by `queries/world_q.py::_housing_population_input` / `_housing_capacity_input`:
      * `subtree`        -- the rung and everything under it (`world_q._subtree`);
      * `residents`      -- `((pid, residence rung, Person.weight), ...)`, every `residence_of` entry in
                            its own order; `None` when `capacity` asks;
      * `dwelling_rungs` -- `(rung, ...)`: each `dwelling` Site's own `rung`, one entry per Site, in
                            `World.sites` order; `None` when `population` asks;
      * `floor`          -- `capacity_floor[dwelling]` (`ED-SE-0051`); `None` when `population` asks."""
    subtree: frozenset
    residents: Optional[tuple]
    dwelling_rungs: Optional[tuple]
    floor: Optional[int]


@dataclass(frozen=True)
class Housing:
    """What `settlements.housing` returns: the subtree's `population` (summed resident weight) and its
    `capacity` (dwellings floored); either is `None` when its half was not projected."""
    population: Optional[int]
    capacity: Optional[int]


@dataclass(frozen=True)
class FabricInput:
    """What `settlements.fabric` reads. Built by `queries/world_q.py::_fabric_ceiling_input` / `_fabric_share_input`:
      * `scale`      -- the `condition_scale` fixture; `None` when `share` asks;
      * `live_works` -- how many live works name the site (`works_for`; the host refuses two, A6);
      * `declared`   -- that works' declared terms (`len(stages)`), `0` with no live works;
      * `matured`    -- its ripened terms (`matured_terms`, a log scan), counted only when `declared > 0`
                        (`0` otherwise, unread), so the scan is paid only where a works declares terms;
      * `present`    -- how many persons stand at the site's rung (`len(presence)`); `None` when
                        `ceiling` asks. The first four are `None` when `share` asks."""
    scale: Optional[int]
    live_works: Optional[int]
    declared: Optional[int]
    matured: Optional[int]
    present: Optional[int]


@dataclass(frozen=True)
class Fabric:
    """What `settlements.fabric` returns: `ceiling` (the bound on the fabric's rise) and `share`
    (`(1, n)`, the commons ratio); either is `None` when its half was not projected."""
    ceiling: Optional[int]
    share: Optional[tuple]


@dataclass(frozen=True)
class FortInput:
    """What `settlements.fortification` reads. Built by `queries/world_q.py::fort_input`:
      * `conditions` -- `(Site.condition, ...)` of every `garrison` Site in the subtree, `World.sites` order;
      * `scale`      -- the `condition_scale` fixture, read only when `conditions` is non-empty,
                        else `None`. The entry returns a bare `float`."""
    conditions: tuple
    scale: Optional[int]


@dataclass(frozen=True)
class ArmyCommand:
    """What `mass_battle.army` (`modules/mass_battle/armyrecord.py::apply`) reads (ED-IN-0306 phase 2). Built by
    `loop/effects_army.py`, one per army verb:
      * `record` -- the army Record's `subject_matter` (`armyrecord.KEYS`), as the world holds it;
      * `op`     -- `armyrecord.OPS`: recruit, form, assign or order;
      * `args`   -- the command's operands from the act's payload, plus for `recruit` the world's facts it needs
                    (`weight`, `sites`, `full`). The entry returns the new `subject_matter` dict."""
    record: dict
    op: str
    args: dict


@dataclass(frozen=True)
class ArmyMuster:
    """What `mass_battle.army_order` (`modules/mass_battle/armyrecord.py::fielded`) reads (ED-IN-0306 phase 3).
    Built by `seam/wrappers/mass_battle.py::field_input` for one side of one field:
      * `record` -- the faction's army Record's `subject_matter` (`armyrecord.KEYS`), as the world holds it;
      * `fit`    -- `((cohort id, fraction), ...)`: each cohort of the side PRESENT on the field (mustered at the
                    place) and its body as a fraction of the full scale, in `[0.0, 1.0]`. A cohort not listed is
                    not there. The entry returns an `OrderOfBattle`, or None when nobody it names is present."""
    record: dict
    fit: tuple


@dataclass(frozen=True)
class ArmyOptionsQuery:
    """What `mass_battle.army_options` (`modules/mass_battle/armyrecord.py::options`) reads (ED-IN-0306 phase 5b). Built by
    `harness/military_menu.py`, read-only:
      * `record` -- the army Record's `subject_matter`, as the world holds it;
      * `cohorts` -- `((cohort id, weight, {site kind: best condition}), ...)`, the cohorts the army's faction may raise
                    (`world_q.raisable_by`);
      * `full`   -- the condition scale (`condition_scale`);
      * `others` -- every other army Record's `subject_matter` (`world_q.other_army_records`)."""
    record: dict
    cohorts: tuple
    full: float
    others: tuple


@dataclass(frozen=True)
class ArmyPresetQuery:
    """What `mass_battle.army_preset` (`modules/mass_battle/troop_types/presets.py::plan`) reads (ED-IN-0306 phase 5c). Built
    by `harness/army_presets.py`: `faction` (its Proposition id), and `cohorts`, `full` and `others` as
    `ArmyOptionsQuery` has them. The entry returns the commands, in order."""
    faction: str
    cohorts: tuple
    full: float
    others: tuple


# v9 IN-52: the `settlements.provision` query's records -- the levy-to-field feed. Built per side by
# `seam/wrappers/mass_battle.py::provision_input`, read by `modules/settlements/provision.py`; the field
# adapter hands `troops` to the mass-battle entry and `_eff_march` debits `consumed` from the treasury.

@dataclass(frozen=True)
class ProvisionInput:
    """What `settlements.provision` reads, and nothing else. Built by
    `seam/wrappers/mass_battle.py::provision_input`, once per side:
      * `weight` -- the side's Σ `Person.weight` (what the field fields today);
      * `stores` -- `((kind, units), ...)`: the side's treasury, in its own `Rung.stores` order, `()`
                    for a side with no treasury rung;
      * `ration` -- `((kind, units per weight), ...)`: the `subsistence_weight` fixture, sorted by kind --
                    the larder's own ladder, so a field eats as the people it is made of eat;
      * `on`     -- the `field_provisioning` fixture. `False` is the control arm, today's field."""
    weight: int
    stores: tuple
    ration: tuple
    on: bool


@dataclass(frozen=True)
class Provision:
    """What `settlements.provision` returns: `troops`, the side's fielded troops, and `consumed`,
    `((kind, units), ...)` in `ration` order, what fielding them eats from the treasury (`()` when the
    arm is off)."""
    troops: int
    consumed: tuple
