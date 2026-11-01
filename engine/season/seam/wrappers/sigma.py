"""THE SOCIAL CONTEST SCENE'S CONTEST PROVIDER — the host adapter and the host INPUT BUILDER for the
`social_contest` module's σ-leverage roll (plan position `31a`, A-25; registered as
`@provider("contest", "social_contest")` since v9 SC-01 steps 13 + 15, which repointed the prize rows
`a standing`, `a proposition` and `a matter` from the interim name `sigma_leverage`, ED-SC-0033 clause
(2)). The file keeps its name because its automated mode is still the σ-leverage roll: SC-05's
measurement at step 15 kept it over the kernel (`modules/social_contest/roll.py`'s docstring).

`04_CODE_ARCHITECTURE.md` §A.2:182 types `seam/wrappers/*` as writing *"nothing, ever"*, reading
*"the projection"*, returning *"a `Margin`"*, holding token *"none"*. This module is that row. It
DECIDES NOTHING: `contest_input` (the host input builder) derives a pool and reads the obstacle's raw
operands from what the actor and the subject genuinely have -- since v9 SC-02 `22a` that includes, for a
prize a room hears (`heard_by:`), the bench's and the opponent's LEDGERS through `queries/world_q.py`'s
`reception` and `proofs`, a read `04_CODE_ARCHITECTURE.md` §B.2:250 (F8) words for the fold's own
ledger query and §A.2:168 permits `world_q` ("any store, via World"): the tension is recorded in
`hole_register.yaml` H-215/H-216, not resolved here -- and freezes them into
`queries/inputs.py::SocialContestInput`; `resolve` (the adapter) calls the module entry the prize row
names (`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its composition row), keeps
S27.4's refusal on the pair it returns, and otherwise returns what it returned -- the net/ob pair as a
dict, the shape `combat_seam` already returns and `degree_of` already grades. It NEVER returns a band; `seam/ladder.py` reads one by calling `degree_from_net`,
which is the single owner. The roll itself is `modules/social_contest/roll.py`, reached by string.

⚠ THIS DOCSTRING NAMES NO BAND, ON PURPOSE AND UNDER A MEASURED CONSTRAINT.
`tests/valoria/test_degree_ladder_single_owner.py`'s `_PRODUCES_BAND` scan reads raw file TEXT
INCLUDING DOCSTRINGS and flags any file where two or more band names appear in a produce-shape. A
prose line here spelling the four bands would redden a guard this module exists to stay clear of.
Keep it band-free.

RULED, ED-SC-0037. JORDAN, 2026-09-09, VERBATIM: *"we have the sigma leverage d10 resolver in
engine to use."* A third option neither of that row's two costed.

⚠⚠ **BOTH IMPORTS, AND THE SECOND ONE IS THE POINT** -- they are the module's now
(`modules/social_contest/roll.py`), carried there with this reasoning. `roll_net` ALONE APPLIES ZERO σ-LEVERAGE:
`sigma_leverage.py::roll_net` is a back-compat shim — *"The authoritative implementation is
dice_engine.roll_pool"* — that floors the pool, delegates, and **drops `roll_pool`'s `ob`
parameter**, which `roll_pool` accepts and grades on. Importing it alone is strictly `roll_pool`
minus the obstacle: **the bare pool roll ED-SC-0037 costed, wearing the ruled module's name.**
TERM-MATCHING ON THE MODULE IS NOT THE MECHANISM. The σ layer is `net_boost` — the μ-shift ED-884 /
ED-934 ruled, *"base_ob untouched, Ob floor never breached"* — and the composition is the tree's
own, at `systems/social_contest/sim/contest/resolver.py:302`:

    net = roll_net(pool) + net_boost(lev, pool)

⚠ **THE HOST NO LONGER DERIVES AN OBSTACLE (v9 SC-01 step 14).** `sigma_leverage.eff_ob` CONSUMES
`base_ob` and is *"DISPLAY ONLY (not the resolution value)"* by its own docstring; `effective_ob` is a
pure arg-order alias of it; `sigma_space_ob_shift` takes no `base_ob` at all and returns a shift. So
the dice engine owns no obstacle, and ED-SC-0037's cost 1 — *"the interim provider derives its own
obstacle in-seam, which is an nth obstacle site"* — stood until step 14 deleted that site
(`_obstacle_of`): the obstacle is now composed by the social contest module
(`modules/social_contest/roll.py::obstacle`, ceiling included, `H-213`), ED-SC-0033 clause (3)'s
single owner. Clause (2), the repoint, landed at steps 13 + 15: no prize row is `interim:` any more.

⚠ **THE PLACEMENT QUESTION, ADJUDICATED AT THE SITE RATHER THAN ASSUMED.** `04 §A.2` read
*"one wrapper per **deferred subsystem**"* (that line was since amended, ED-IN-0284 and ED-IN-0285; see 04:147-151), and `sigma_leverage` is not a deferred subsystem — it is
an in-engine resolver under `engine/dice_engine/`. Two readings were available: **(i)** it is a wrapper
BY ROLE — it writes nothing, returns a margin, holds no token, which is exactly the `04:182` row, and
a module satisfying that contract IS that row whatever supplies the margin; **(ii)** §A.2's
enumeration is short by one and the finding goes on the ledger. **This unit takes (i).**
⚠ COLUMN 3, *"a `Margin`"*, IS MET AT THE MODULE BOUNDARY SINCE STEP 15 AND NOT AT THE SEAM'S. The
module entry returns `queries/inputs.py::Margin` and `resolve` refuses any other return, naming the
entry -- so a winner (the kernel's `((band, reason), bout)`, or a dict carrying one) cannot cross. What
`resolve` hands the SEAM is still the dict every provider returns: typing the seam's return across
all three providers is a `seam/` item of its own, and `combat`/`mass_battle` return a scene and a
field, not a margin. Column 2 is *"the projection"* and the signature takes `w`, a World -- the
ADAPTER's does; since `31a` the MODULE reads only the typed record `contest_input` builds.
`combat.resolve(w, …)` is the precedent — **and it is a precedent for the deviation, not for
conformance.**

⚠ THE PRECEDENT IS `seam/wrappers/combat.py` AND IT IS FOLLOWED, NOT REINVENTED: derive exactly what
the actor genuinely has, leave every other operand at its registered fixture, and return a typed gap
rather than fabricate a party.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/` OR `modules/` AND INSERTS NO `sys.path`. The roll is
reached by STRING: the composition row `social_contest.roll` names it, the registrar resolves it at
driver construction into `MODULE_ENTRIES`, and `resolve` below looks it up there by the role its
prize row names. NO entry is added to
`tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED`. That set is shrink-only.
"""
from __future__ import annotations

import importlib
import random
from dataclasses import asdict
from typing import Any, Optional

from engine.dice_engine.sigma_leverage import levels_to_net_sigma, record_odds, settle_record
from engine.substrate import composition

from ...data.rosters import VERB_CAPABILITY, roster
from ...gaps import Unspecified
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup);
# `manifest/registry.py` imports only `data/` and `gaps` and `queries/` is below `seam/`, so the
# two imports below close none either (measured, v9 SC-02 `22a`).
from ...manifest.providers import provider
from ...manifest.registry import BENCH, resolve as _prize_row
from ...queries.inputs import Margin, SocialContestInput
# v9 SC-02 `22a`: the room's two resolver-side reads, the precedent `seam/wrappers/mass_battle.py`'s
# `world_q.mustered` set. The host READS them; the module composes the obstacle they move.
from ...queries.world_q import proofs, reception
from ...state.carriers import effort_of
from ._entry import entry_for

# The prize rows' `provider:` string (`rosters.yaml` `contest_subsystems`): the module's one identity
# (A-25), so the row says the social contest module runs its own prizes. Reached by that string only.
_PROVIDER = "social_contest"
_RESOLVER = "d10_sigma"


def _capability(entity: Any, verb: str):
    """What `entity` brings to `verb`'s capability key, or `None` if it brings nothing.

    ⚠ ONE READ, TWO CALLERS. `_pool_of` and `_opposition_of` each map the verb through
    `VERB_CAPABILITY`, guard a missing key, and guard a missing entry — the same three steps,
    differing only in WHOSE dict they read and what default they fall to. Those differences are the
    callers'; the read is not. Returning `None` rather than a default is what keeps it that way:
    the pool falls to `pool_default`, and the opposition's `None` reaches the module, which falls
    to `obstacle_default`; neither is this function's to know."""
    key = VERB_CAPABILITY.get(verb)
    if not key:
        return None
    return (getattr(entity, "capability", None) or {}).get(key)


def _pool_of(person: Any, verb: str, fx: Any) -> int:
    """Dice, from what the actor genuinely has. `03 §A.2` — *"Rank supplies dice and gates nothing"*.

    `VERB_CAPABILITY` maps a verb to the capability key it draws on; `Person.capability` is the
    person's own dict. ⚠ IT IS EMPTY ON EVERY CORPUS PERSON TODAY — its writers are a `cast:` overlay and (v9 IN-12 step 9) `train`, which raises a key only a person already holds —
    so in practice this returns `pool_default` for everybody, which is why R-09 reads `partial`
    after this unit and not `met`: the roll varies by SEED and by FIXTURE, not by PERSON. It varies
    by person the day capability is written, and that is character development, out of this arc.
    ⚠ `08 §3` GIVES THE POLARITY: an `assumption` grade means *inject the default, declare the site,
    sweep three points* — never refuse the whole corpus for a missing key. `absent` is the grade
    that refuses, and this is not one."""
    have = _capability(person, verb)
    return int(have if have is not None else fx.get("pool_default"))


def _opposition_of(w: Any, subject: Optional[str], verb: str) -> Optional[float]:
    """The subject's score on the verb's capability key, or `None` -- a READ, not an obstacle.

    ⚠ v9 SC-01 step 14 DELETED THIS MODULE'S OBSTACLE SITE (`_obstacle_of`; ED-SC-0033 clause (3),
    *the obstacle has a single owner*). What it composed -- `score/2`, the `obstacle_default`
    stand-in, and now the ceiling -- is `modules/social_contest/roll.py::obstacle`'s. What stays
    here is the half only the host can do: reading `World` for the score a PERSON subject brings
    (`None` for a record, a rung or a proposition, or a person with no entry)."""
    if subject and subject in w.persons:
        have = _capability(w.persons[subject], verb)
        if have is not None:
            return float(have)
    return None


def _effort_levels(fx: Any, operands: dict) -> list:
    """`effort`'s levels (CP-T01-05): an act at effort `e` brings `e` copies of the `effort_level` fixture
    (a `sigma_leverage.LEVEL_SIGMA` name, shipped `moderate`) -- one named level per slot of effort. None at
    effort 0, so the shipped chooser, which forms no effort, adds nothing."""
    return [fx.get("effort_level")] * int(operands.get("effort", 0))


# THE ADVANTAGE CHANNEL'S BINDING: each member of `rosters.yaml: advantage_sources` -> the function that
# returns the named levels it brings to an act, `fn(fixtures, operands) -> [level name, ...]`. THE ROSTER IS
# THE CLOSED SET AND THIS IS ITS BINDING: refused at import if the two disagree, so a member with no function
# (it would silently add nothing) and a function with no member (it would silently never run) are both loud.
ADVANTAGE_SOURCES = {"effort": _effort_levels}
if set(ADVANTAGE_SOURCES) != set(roster("advantage_sources")):
    raise Unspecified(
        f"`advantage_sources` members {sorted(roster('advantage_sources'))} and "
        f"`ADVANTAGE_SOURCES` functions {sorted(ADVANTAGE_SOURCES)} differ", "rosters.yaml",
        needs="a function for every member and a member for every function",
        law="CP-T01-05 -- the roster is the only door into the social roll's sigma term")


def advantage_sigma(fx: Any, operands: dict) -> float:
    """The social roll's net sigma: every `advantage_sources` member's named levels for this act, summed
    through `levels_to_net_sigma` (a mu-shift the roll applies as `net_boost`; never a flat bonus on the net,
    never an Ob reduction). `operands` is what the act brings (`{"effort": e}`); 0.0 when nothing does."""
    levels = []
    for name in roster("advantage_sources", ordered=True):
        levels.extend(ADVANTAGE_SOURCES[name](fx, operands))
    return levels_to_net_sigma(levels)


def contest_input(w: Any, claimants: list, *, verb: str = "",
                  subject: Optional[str] = None, room: Optional[str] = None,
                  examined: Optional[str] = None, effort: int = 0) -> SocialContestInput:
    """THE HOST INPUT BUILDER (plan position `31a`, A-25): `World` -> the frozen record the roll reads.

    Reads `w.persons` (the actor, `claimants[0]`, and a person subject), `w.fixtures`, `w.records` (the
    Record an inquiry examines) and, for a prize a room hears, the bench's and the opponent's ledgers
    through `queries/world_q.py::reception` and `proofs`; the module that consumes the record never sees
    `World`. §A.2's wrapper row types the column *"the projection"*: this builder reads `World`, the
    deviation named above (`combat.resolve` is its precedent), CONVENTION. Its precondition is the adapter's
    PARTY-GAP checks (`resolve`, below): at least one claimant, and the first a person.
    `leverage` is the sum of the named levels the `advantage_sources` roster brings to the act
    (`advantage_sigma`; CP-T01-05's `effort` is the first member) and is 0.0 when nothing does -- the
    honest form while nothing supplies it: a fabricated leverage would be a number nobody chose.
    `effort` is the act's own (`state/carriers.py::effort_of`), passed by the adapter. The obstacle's operands are carried RAW (`opposition`, `obstacle_default`,
    `obstacle_ceiling`); the module composes them (step 14).

    `room` (v9 SC-02 `22a`) is the rung whose bench hears the contest, or `None`: the adapter passes the
    act's rung when the prize row says `heard_by: bench` (`manifest.resolve`), and nothing otherwise.
    With a room, the record carries the bench's `reception` of the actor and the actor's unmirrored
    `proofs` against the subject (`queries/world_q.py`, both read raw) and their two gains; without
    one they stay at the record's no-room defaults, so a `tell`, a `determine` or an inquiry rolls
    exactly as before.

    `examined` (v9 SC-02 `22b` step 25) is the subject an INQUIRY examines, or `None`: the adapter passes
    the act's subject when there is no prize (an inquiry, `graded_inquiries`' route), and nothing
    otherwise. Where it names a Record, the record carries that Record's `forgery_quality` (read from
    `w.records`, the one read this builder adds), which the module adds to the obstacle; a site, a
    person, or a contest a prize names carries `0`."""
    fx = w.fixtures
    room_terms = {}
    if room is not None:
        room_terms = dict(reception=reception(w, claimants[0], room),
                          reception_gain=fx.get("reception_gain"),
                          proofs=proofs(w, claimants[0], subject, room),
                          proof_step=fx.get("proof_step"))
    doc = w.records.get(examined) if examined is not None else None
    return _frame(fx, _pool_of(w.persons[claimants[0]], verb, fx), _opposition_of(w, subject, verb),
                  doc.forgery_quality if doc is not None else 0.0, room_terms,
                  advantage_sigma(fx, {"effort": effort}))


def _frame(fx: Any, pool: int, opposition: Optional[float], forgery_quality: float,
           room_terms: dict, leverage: float) -> SocialContestInput:
    """THE RECORD, FILLED THE ONE WAY: what `contest_input` (the true input) and `believed_input` (a
    person's) both hand the module. They differ in where the pool's opposition, the forgery quality
    and the room terms COME FROM; the fixtures and the record's shape are this
    function's alone, so the two modes cannot compose different obstacles from the same fields."""
    return SocialContestInput(
        pool=pool, opposition=opposition,
        obstacle_default=fx.get("obstacle_default"),
        obstacle_ceiling=fx.get("obstacle_ceiling"),
        ceiling_per_pool=fx.get("ceiling_per_pool"),
        obstacle_refusal_multiple=fx.get("obstacle_refusal_multiple"),
        leverage=leverage, forgery_quality=forgery_quality, **room_terms)


# ---------------------------------------------------------------------------------------------
# EXACT ODDS (CP-T01-03): what a roll of this record would deal, read and never rolled.
# ---------------------------------------------------------------------------------------------
# The claim a person holds about another's capability: `Claim(subject=<that person>, predicate=
# CAPABILITY_CLAIM + <the verb's capability key>, value=<the score he believes>)`. NOTHING DEPOSITS
# ONE TODAY (the told, seen and inferred channels carry no capability), so a believed opposition is
# `None` for every person in a built realm until a depositor exists; this is the reading, not the writer.
CAPABILITY_CLAIM = "capability:"
_ROLL_ROLE = "social_contest.roll"    # the composition row whose module composes the obstacle


def _composed_obstacle(inp: SocialContestInput) -> float:
    """The obstacle the module composes for `inp`, through the module that owns it. Reached by the
    composition row's target (`composition.require`), the host's own way of naming a module; the
    attribute is read at call time, so the odds follow the owner when it changes."""
    module = importlib.import_module(composition.require(_ROLL_ROLE).__module__)
    return module.obstacle(inp)


def _odds_of_input(inp: SocialContestInput) -> Optional[tuple]:
    """`record_odds` over one record: the module's obstacle, the record's pool and leverage (the owner
    derives the roll's boost from them). `None` where S27.4 refuses the attempt -- no dice are dealt, so there is no distribution
    (`resolve` refuses on the same pair, one rule: `ob > multiple x pool`)."""
    ob = _composed_obstacle(inp)
    if ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
        return None
    return record_odds(inp.pool, ob, inp.leverage)


def believed_input(p: Any, verb: str, subject: Optional[str], fx: Any, *,
                   person_subject: bool, examined_record: bool = False,
                   room: Optional[dict] = None, heard: bool = False,
                   effort: int = 0) -> Optional[SocialContestInput]:
    """THE PERSON'S RECORD (mode (b)): the same `SocialContestInput`, filled only from what `p` holds.

    AX-2: it reads `p` (his own capability and his own ledger) and the fixtures, never the World; the
    facts about the act's SHAPE that only a World can answer (`person_subject`: the subject is a person;
    `examined_record`: an inquiry examines a Record; `heard`: a bench hears the contest) are the
    caller's, not a belief. His pool is his own and held with certainty. Every other field is filled
    only from what he holds, and WHERE A FACTOR IS UNKNOWN TO HIM THE ANSWER IS `None`, never a figure:
      * the opposition of a person subject, on a verb that names a capability key: a claim in his
        ledger on that subject at `CAPABILITY_CLAIM + key` (the latest, then the most confident);
        none held -> unknown. A non-person subject, or a verb naming no key, has no opposition: the
        module's stand-in applies, and that is known.
      * an examined Record's forgery quality: a property of the Record, held by nobody's claim here
        -> unknown.
      * the room's terms (`reception`, `proofs`) read other persons' ledgers: unknown unless the caller
        passes his own believed `room` (`{"reception": .., "proofs": ..}`).
    His `effort` is his own act's, held with certainty like his pool (CP-T01-05)."""
    key = VERB_CAPABILITY.get(verb)
    opposition = None
    if person_subject and key:
        held = [c for c in p.ledger
                if c.subject == subject and c.predicate == CAPABILITY_CLAIM + key]
        if not held:
            return None
        said = max(held, key=lambda c: (c.when, c.round, c.confidence))
        opposition = float(said.value)
    if examined_record:
        return None
    room_terms = {}
    if heard:
        if room is None:
            return None
        room_terms = dict(reception=room["reception"], reception_gain=fx.get("reception_gain"),
                          proofs=room["proofs"], proof_step=fx.get("proof_step"))
    return _frame(fx, _pool_of(p, verb, fx), opposition, 0.0, room_terms,
                  advantage_sigma(fx, {"effort": effort}))


def _rolled_as(w: Any, act: Any) -> Optional[tuple]:
    """`(claimants, subject, room, examined)` exactly as the fold hands the act to `resolve`, or `None`
    when the social roll does not deal it (an uncontested act, another subsystem's prize, a party
    gap). The derivation is the fold's own: `loop/resolve.py::_contests_of`, `loop/sides.py::sides_of`
    and the prize row's `heard_by:` for a contest; the verb's `graded_inquiries` route for an inquiry.
    Imported inside the function: `loop/` imports this package, so a module-level import would loop."""
    from ...data.rosters import GRADED_INQUIRIES
    from ...data.verbs import VERB_TABLE
    from ...loop.resolve import _contests_of
    from ...loop.sides import sides_of
    row = VERB_TABLE.get(act.verb)
    payload = act.payload if isinstance(act.payload, dict) else {}
    contests = _contests_of(act, row)
    if contests:
        prize = _prize_row("contest", contests[0])
        if prize is None or prize.get("provider") != _PROVIDER:
            return None
        target = payload.get(row.opponent_operand() if row is not None else "subject")
        parties, subject, rung = sides_of(w, act, target, contests[0])
        if not parties:
            return None
        return parties, subject, (rung if prize.get("heard_by") == BENCH else None), None
    route = GRADED_INQUIRIES.get(act.verb)
    if route is not None and route.get("provider") == _PROVIDER:
        subject = payload.get("subject")
        return [act.actor], subject, None, subject
    return None


def odds_of(w: Any, act: Any, *, believer: Any = None,
            believed_room: Optional[dict] = None) -> Optional[tuple]:
    """`(F, P, S, O)` for the social roll `act` would deal, or `None`. READ-ONLY; nothing is rolled.

    MODE (a), `believer=None`: the TRUE input -- `contest_input` over the act as the fold would hand it
    to `resolve`, the module's obstacle and `band_odds`. The shown number is the dealt number by
    construction: it is the same record, the same obstacle function and the same roll composition.

    MODE (b), `believer=<Person>`: the SAME function over `believed_input(believer, ...)`, the person's
    own record. It reads the believer's own ledger and nothing of the true state (the World answers only
    the act's shape), and returns `None` where a factor is unknown to him -- never a guessed figure.
    `None` is also the answer where the social roll deals no dice for the act (see `_rolled_as`) or
    S27.4 refuses it.

    Mode (b) HAS NO CALLER in this change; its first reader is the chooser's alignment term (CR-17)."""
    called = _rolled_as(w, act)
    if called is None:
        return None
    parties, subject, room, examined = called
    effort = effort_of(act)                 # the act's own, as the fold hands it to `resolve`
    if w.persons.get(parties[0]) is None:
        return None
    if believer is not None and believer.id != act.actor:
        return None                     # another's pool is not his own to know
    if believer is None:
        return _odds_of_input(contest_input(w, parties, verb=act.verb, subject=subject, room=room,
                                            examined=examined, effort=effort))
    inp = believed_input(believer, act.verb, subject, w.fixtures,
                         person_subject=bool(subject) and subject in w.persons,
                         examined_record=examined is not None and examined in w.records,
                         room=believed_room, heard=room is not None, effort=effort)
    return None if inp is None else _odds_of_input(inp)


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None, rung: Optional[str] = None,
            module_entry: Optional[str] = None, effort: int = 0) -> dict:
    """Roll for one contested act: build the record, call the module entry, hold its return to a
    `Margin`, refuse S27.4. Returns a net/ob pair, NEVER a band and never a winner.

    `effort` is the act's own (CP-T01-05, `state/carriers.py::effort_of`, passed by `seam/contest.py`): it
    reaches only `contest_input`, where it becomes `leverage`; the act's draw is unchanged (one id, one draw).

    RESOLVED -> dict(status, module, resolver, pool, ob, net, leverage, settled_margin)   # the entry's Margin + the record
                 # + the margin's fraction settled by the act's own draw (CP-T01-04), the integer `degree_of` grades
    REFUSED  -> dict(status, why, pool, ob)   # S27.4: ob > obstacle_refusal_multiple x pool

    ⚠ A RETURN THAT IS NOT A `Margin` RAISES, NAMING THE ENTRY (v9 SC-01 step 15, Lens B: *the provider
    returns a Margin*). It is a software defect in the module -- a winner where a margin belongs is the
    second resolver S27.2 refuses -- so it is loud, never a refusal the fold would read as a game
    outcome. `engine/season/tests/test_sc01_provider.py` plants the kernel's own winner shape.

    ⚠ THE ENTRY IS LOOKED UP BY THE ROLE THE PRIZE ROW NAMES (`module_entry:`), IN `MODULE_ENTRIES`.
    The registrar fills that table at driver construction from the composition row, and
    `manifest.check_contest_prizes` refuses construction when the two rows disagree; a call reaching
    here with the role unregistered (no driver constructed in the process) is `ENGINE-UNAVAILABLE`,
    `combat.py`'s typed refusal, never a direct import of the module.

    ⚠ `rung` IS READ FOR A PRIZE A ROOM HEARS, AND ONLY THERE (v9 SC-02 `22a`). It was accepted and
    unused (M4, `ED-IN-0279` clause (a), `combat.py`'s deliberate non-change) until the proceedings'
    room existed. Since v9 SC-01 step 13 (C-8) the seam passes the actor's place (`loop/sides.py`,
    `world_q.place_of`) rather than the placeholder `"R"`, so the venue is the act's own; a prize row
    declaring `heard_by: bench` (`a matter`, `speak`'s) has the bench sitting over it read the speaker
    (`contest_input`'s `room`). Every other prize still derives its obstacle from the parties alone.

    ⚠ THE RNG IS A PARAMETER AND IS NOT CONSTRUCTED HERE, WHICH IS `04 §C.12`'s REJECTION 4 BECOMING
    LOAD-BEARING FOR THE FIRST TIME: *"When R-09's producer is built … its generator must be
    constructed by the driver from the run seed and passed down exactly as `World` is. This is the
    one rejection that is not yet load-bearing, because no roll exists yet."* It exists now.
    ⚠ *"Threaded like `World`"* MEANS PASSED BY PARAMETER RATHER THAN REACHABLE BY A GLOBAL NAME —
    not one continuous stream. `04 PART D row 35` settles it: `H(seed, tick, subject, purpose)`, no
    counter, no service. A single stream threaded through a season would make every roll depend on
    the count of prior draws, so adding one contested verb would move every other verb's outcome.

    ⚠ S27.4 IS EVALUATED HERE, ON THE DERIVED PAIR, AND THE DRIVER'S OWN BRANCH KEEPS ITS JOB. The
    fold already refuses an act whose HAND-DECLARED `obstacle` exceeds the multiple; this refuses on
    the pair the provider derived. One rule, two inputs, and neither site re-evaluates the other's —
    which is §8's *the rule lives once* stated for a rule with two legitimate operands.
    ⚠ SINCE v9 SC-01 STEP 14 IT IS EVALUATED AFTER THE ENTRY, on the pair the entry RETURNS: the
    obstacle is the module's (`roll.py::obstacle`, ED-SC-0033 clause (3)), so the host has no pair
    until the entry has run. A refused act's roll is discarded; its generator is the act's own
    (`H(seed, tick, subject, purpose)` above), so no other act's draw moves. Under the shipped
    ceiling (`H-213`, 2 = the multiple x the 1D floor) a derived pair with a pool of 1 or more is
    never refused here; only a pool below the floor is.

    ⚠ `module_entry` IS THE INQUIRIES' ROUTE (v9 FI-01, `ED-FI-0009`, J-22 (A)): `seam/contest.py::grade`
    passes the role a `graded_inquiries` row names, with `prize=None`, and everything else here is the
    same body -- the same input builder, the same entry table, the same `Margin` hold and the same
    S27.4 -- so an inquiry is rolled by the one owner and graded on the one ladder, with no prize."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a contest needs at least one claimant",
                    module=_PROVIDER)
    if w.persons.get(claimants[0]) is None:
        return dict(status="PARTY-GAP", why=f"claimant is not a person: {claimants[0]!r}",
                    module=_PROVIDER)
    # v9 SC-02 `22a`: the room that hears this prize, off its row (`heard_by:`); an inquiry has no prize
    # and so no room. `rung` is the act's place (`loop/sides.py`), which the bench sits over.
    row = _prize_row("contest", prize) if prize is not None else None
    heard = rung if row is not None and row.get("heard_by") == BENCH else None
    # v9 SC-02 `22b` step 25: an inquiry (no prize) examines its subject; a Record's forgery quality
    # enters the obstacle (`contest_input`'s `examined`). A prize names a contest, which examines nothing.
    inp = contest_input(w, claimants, verb=verb, subject=subject, room=heard,
                        examined=subject if prize is None else None, effort=effort)
    entry, refusal = entry_for(prize, _PROVIDER, module_entry)
    if entry is None:
        return refusal
    margin = entry.fn(inp, rng)
    if not isinstance(margin, Margin):
        raise Unspecified(
            f"module entry {entry.role!r} ({entry.target}) returned {type(margin).__name__} "
            f"{margin!r:.120}, which is not a `Margin`", "S39.4",
            needs="the entry returning `queries.inputs.Margin(net, ob)`",
            law="08_SEAM provider rule (intent) and S27.2 -- a contest provider returns a MARGIN, never "
                "a winner; the band is the one ladder's reading of the margin, so a winner here is a "
                "second resolver")
    if margin.ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
        return dict(status="REFUSED", why="S27.4", module=_PROVIDER,
                    resolver=_RESOLVER, pool=inp.pool, ob=margin.ob)
    # CP-T01-04: the margin's fraction is settled here, AFTER the S27.4 check (a refused act draws
    # nothing), by the act's own generator, and only when there is a fraction to settle -- a whole
    # margin draws nothing, so the act's stream and every whole-Ob hash are unmoved. The owner derives
    # the roll and its boost from the record's fields (`settle_record`); the host does no arithmetic.
    # The recorded `net`, `ob` and `pool` below are unchanged: S27.4 and every reader of the pair see
    # what they saw.
    settled = settle_record(margin.net, inp.leverage, inp.pool, margin.ob,
                            rng.random if rng is not None else random.random)
    # The margin's own fields, copied whole: the host reads the pair, it never computes one.
    return dict(status="RESOLVED", module=_PROVIDER, resolver=_RESOLVER, pool=inp.pool,
                **asdict(margin), leverage=inp.leverage, settled_margin=settled)
