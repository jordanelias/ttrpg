"""THE IN-SIDE OF THE PERSONAL-COMBAT SEAM — the seam CALLS the engine that owns the prize.

This module is the HOST (plan position `31b`, A-25): the input builder `combat_input` (`World` ->
`queries/inputs.py::PersonalCombatInput`: the two parties, each one's derived `end`, the wound
quantities to lift) and the adapter `resolve`, which keeps the PARTY-GAP refusals and the seed, calls
the module entry the prize row names (`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its
composition row) and interprets the `CombatOutcome` that comes back (`queries/inputs.py`) -- the wound state with its
refusal, the surrender, the decisive beat and the rounds fought -- and returns the scene's trace beside them (PC-06
M-1). No winner crosses: the integer `wrapper.fight` returns is not lifted (B14.01). The fight itself is
`modules/combat/fight.py`, reached by string; it, not this module, constructs the `Combatant`s and calls
`wrapper.fight`.

⚠ JORDAN, 2026-09-02: *"kill / wound points towards a seam that should be calling in the personal
combat system."* The seam calls the engine; it does not resolve the subsystem by name and refuse.

WHAT THIS IS, AND WHAT IT DELIBERATELY IS NOT
---------------------------------------------
`references/module_contracts.yaml` declares `combat` (plan position `30`; the PROVIDER this module
registers keeps the name `personal_combat`) with `sim_module: modules/combat/` and `resolver: d_sigma`. Its public entry point is
`wrapper.fight(A, B, ...) -> int` (`modules/combat/wrapper.py`) — `+1` A wins, `-1` B wins, and
**`0` UNRESOLVED, which is a RULING and not a failure**: *"NO automatic tiebreak (Jordan
2026-06-02): if neither fighter is felled, the round ends UNRESOLVED... an undecided fight is a
legitimate outcome."*

This module does not decide anything about combat. It derives two parties, hands them to that
engine with a deterministic RNG, and returns what the engine says. Every combat rule stays in
the engine (`modules/combat/`), which this chain may read and may not edit.

⚠ THE LOADER: `composition.require("combat.fight")`, the module entry's own row. This module reads it only for
`engine()`, the availability probe its tests skip on, and `load_error()`, the resolver's raise translated into a
named reason; the roster check below reads the closed set of terms through the row `combat.duel_terms`. The adapter's typed refusal
`ENGINE-UNAVAILABLE` is the unregistered entry's (no driver constructed in the process), as in `sigma.py`.
⚠ THE PARTY DISCIPLINE FOLLOWS `combat_bridge.py` AS PRECEDENT (§0:
*answered by precedent — the tree has already decided this shape somewhere else*): set a field only from
something the actor genuinely has (his authored attributes, PC-06 K-1), leave every
other field at the class's own constructor default, and return a typed gap rather than fabricate a party. The
`Combatant` defaults it names — strength 4, agi 4, end 4, att 3, spirit 3, focus 3, disp 4,
weapon `arming`, armor `light`, tradition `none` — are the class's, not this module's. The record carries
each party's kit (CP-T03-03) and skill score (CR-85, `combat_input`).

⚠ THE ONE FIELD THE SEAM COMPUTES IS `end`, FROM `body_band_penalty`, AND IT INVENTS NO NUMBER. A
`Person` carries `body`, an int on the condition scale, and `attributes` (PC-06 K-1: those ride
whole on `PersonalCombatInput.attributes` and the module maps them by PC-14's `registry_key`, an
absent key at the class default). The tree already owns the body → bands reading: `body_band_penalty`
counts how many `band_floors["body"]` floors a person has fallen below (0 at full operations, +1 per
band), and `H-38` closed with *"`Site.condition` is the model"* so that table is the registered one.
`end` is the Combatant field that reading belongs to — it drives `wound_interval`, `max_wounds` and
`health_full`, i.e. how much punishment the body takes. A healthy person gets his authored
`attr.body.endurance`, else the class default; each band costs one.
Which field the penalty lands on is the injected part and is registered (`H-97`); the magnitude is
not invented, because the bands already exist.

⚠ THE SEAM DOES NOT MINT A DEGREE — IT READS ONE. JORDAN, 2026-09-03: *"kill/wound degrees should be
directly taken from scene combat, which is what actually needs to be called when kill/wound is
considered."*

  `wrapper.fight` returns `+1 / -1 / 0` and THROWS AWAY WHAT IT COMPUTED. But the module entry constructs
  `A` and `B` and still holds them after the call, and each carries a `WoundTracker` (`.wt`) with
  `felled`, `wounds`, `max_wounds`, `health_remaining` and `health_full`. The severity of the
  outcome was computed by scene combat and is sitting on objects the entry owns.

**So the degree is READ OFF THE SCENE, not mapped from a winner.** It invents nothing: the module entry reads
each Combatant's tracker after the fight into a `PartyWounds`, and this module lifts that into `wound_state`.

⚠ WHAT IS STILL REGISTERED, NARROWED RATHER THAN CLOSED (`H-98`). The engine distinguishes exactly
two terminal states — DECIDED (`result != 0`; `wrapper.fight` sets a result when a fighter is
felled, or when an unrefused §11.4 yield ends the scene, which `surrender` on the result carries) and UNRESOLVED (`result == 0`, *"an undecided fight is a legitimate outcome"*, Jordan
2026-06-02) — and the wound counts grade the second. What the DATA does not carry is any
separation of a decisive win from a narrow one beyond wound count on the victor. So the bands
below the felled/unresolved split are the remaining decision, and they are edges over a quantity
that exists rather than a mapping between types that do not meet.
"""
from __future__ import annotations

import dataclasses
from types import SimpleNamespace
from typing import Any, Callable, Optional

from engine.dice_engine.draw import Draw
from engine.dice_engine.sigma_leverage import levels_to_net_sigma

from ...data.rosters import ESTIMATE_OUTCOMES, FELLED, WOUND_QUANTITIES
from ...data.verbs import DUEL_TERMS_BY_VERB
from ...decision import body_band_penalty
from ...gaps import Forbidden, Unspecified
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup).
from ...manifest.providers import provider
from ...queries import person_q
from ...queries.inputs import CombatOutcome, PartyWounds, PersonalCombatInput, PlayHost
from ...queries.world_q import kit_of, stakes_of
from ....substrate import combat_kit, composition
from ....substrate.descriptors import attribute_key
from ...state.ids import draw_factory
from ..ladder import COMBAT_BANDS, party_degree
from ._entry import entry_for
from ._estimate import rng_of, samples_of
from .pool import FIGHT_DICE_SITE, addends_of, pool_pair, score
from .sigma import ADVANTAGE_SOURCES, WOUNDS

_END_KEY = attribute_key("Endurance")      # the registry key of `end` (`descriptors`, the one owner), not a typed literal
assert _END_KEY, "descriptors names no Endurance attribute: party_end would read the default for every person"
# The fight's default for `end` is the combat module's, read once from its typed export through `substrate/combat_kit.py`
# (the artifact's one reader; section `attributes`); the registry's `default: 1` is the sheet scale's floor, a different fact.
_END_DEFAULT = combat_kit.END_DEFAULT
_PROVIDER = "personal_combat"
_PRIZE = "the body"                 # the prize row this provider deals (`rosters.yaml`)
PROVIDER = _PROVIDER                # the name `odds_of` asks `_rolled_as` for (a prize row's `provider:`)


def _probe() -> tuple:
    """`(entry, "")` or `(None, reason)`: the entry is the module's `fight` callable, which the composition row
    `combat.fight` resolves; its RAISE is translated to a named reason. `composition.require` caches a success
    itself, and the resolution is lazy, so the tracer still imports where the engine tree is absent."""
    try:
        return composition.require("combat.fight"), ""
    except Exception as e:                  # a real load failure is a NAMED gap
        return None, f"{type(e).__name__}: {e}"


def engine() -> Optional[Callable]:
    """The module's `fight` entry, or `None` when it cannot resolve (`load_error()` says why). An
    AVAILABILITY PROBE only -- the adapter below never calls the engine through it."""
    return _probe()[0]


def load_error() -> str:
    """Why `engine()` is `None`, as `ExceptionType: message`; `""` when it loads."""
    return _probe()[1]


_CARRIED_MODELS = ("endurance_cut", "level")      # `Fixtures carried_wound_model`'s two arms (H-434); the control first


def _carried_level_model(fx: Any) -> bool:
    """True under `carried_wound_model` `level` (A-8), False under the control `endurance_cut`; any other value is refused by name, never read as the control."""
    model = fx.get("carried_wound_model")
    if model not in _CARRIED_MODELS:
        raise Unspecified(f"`Fixtures carried_wound_model` is {model!r}, and the arms are {list(_CARRIED_MODELS)}", "data/fixtures.py",
                          needs="one of the two arms", law="B05.61 (`UPR` §3 edit 1; H-434)")
    return model == "level"


def _carried_of(person: Any, fx: Any) -> float:
    """A party's wound carried into the fight as a SIGNED net sigma (B05.61, `UPR` §3 edits 2 and 3): the `wounds` advantage source's
    AGAINST-list for his own `body` and `body_ceiling`, summed by `levels_to_net_sigma`, the sum `advantage_sigma` takes (negative: his own wound is a level
    against his own rolls). The one-member read: `effort`, `capability` and the room's sources bring nothing to a fight [ASSUMPTION; basis: the source's
    "from the `wounds` advantage source ... computed host-side by the one reader"]. `0.0` where `wound_level` is None (the source's control) or he has lost
    less than one `wound_step`. The size is the season's own `wound_level`, never a constant of the module's."""
    _for, against = ADVANTAGE_SOURCES[WOUNDS](fx, {"body": person.body, "body_ceiling": person.body_ceiling})
    return float(levels_to_net_sigma([], against))


def party_end(person: Any, fx: Any) -> int:
    """A `Person`'s `Combatant.end` (`H-97`): the `attr.body.endurance` he HOLDS (authored, or drawn by
    `state/carriers.py::generated_attributes` and seated by `build_realm(cast_attributes=True)`; the class default only where he holds none) less
    one point per body band. The other attributes ride on `PersonalCombatInput.attributes` and the module maps
    them (PC-06 K-1). The module entry builds the `Combatant` from this number (`modules/combat/fight.py`).

    UNDER `carried_wound_model` `level` (B05.61, A-8) NO BAND IS CUT: the authored Endurance arrives whole, so Health, Wound Interval and Max Wounds are
    an unwounded man's, and the wound rides on `PersonalCombatInput.carried` as a level (`_carried_of`). Under the control `endurance_cut`, as before."""
    bands = 0 if _carried_level_model(fx) else body_band_penalty(person, fx)
    # `end`'s default in a fight is the combat export's (`_END_DEFAULT`), not a copy of it. One band = one point, floored at 1: a dying
    # person still fights, which is the same floor `decision.budget` applies for the same reason.
    base_end = person.attributes.get(_END_KEY, _END_DEFAULT)
    return max(1, base_end - bands)


def duel_terms_of(verb: str, stakes: Optional[str] = None) -> Optional[str]:
    """THE TERMS A VERB'S SCENE IS FOUGHT UNDER (CP-T03-09; `rosters.yaml: duel_terms`), or `None` for a verb the
    roster does not name (its fight is lethal: `PersonalCombatInput.terms`' own default is the one place that says so).

    v10 PC-10b: `stakes`, a standing challenge's term (`queries/world_q.py::stakes_of`, `rosters.yaml:
    challenge_terms`), when the act fights under one -- THE SAME FIELD AND THE SAME CHECK, no second path. `None`
    (no challenge, or a challenge naming no stakes) falls through to the verb's roster line.

    ⚠ THE CLOSED SET IS THE ENGINE'S, AND THE CHECK IS AGAINST IT, NEVER A COPY: the term must be a member of
    `modules/combat/wrapper.py::DUEL_TERMS`, read through the composition row `combat.duel_terms`, and a value outside it REFUSES here naming
    the roster (`engine/season/data` cannot import the module, so the seam, which may reach it, is the first place
    the roster meets the tuple). Engine absent: the unchecked term goes on and the call is refused as
    `ENGINE-UNAVAILABLE` by `entry_for`, so a bad term cannot reach a fight."""
    term = stakes if stakes is not None else DUEL_TERMS_BY_VERB.get(verb)
    where = "challenge_terms" if stakes is not None else "duel_terms"
    if term is not None and engine() is not None:
        closed = tuple(composition.require("combat.duel_terms"))
        if term not in closed:
            raise Forbidden(
                f"`rosters.yaml: {where}` names {verb!r}: {term!r}, which is not one of the engine's "
                f"{closed}", "rosters.yaml",
                needs="a term in `modules/combat/wrapper.py::DUEL_TERMS`",
                law="CP-T03-09 -- a season roster is checked against the engine's closed set, not re-declared")
    return term


def record_of(act: Any) -> Optional[str]:
    """THE RECORD AN ACT IS ABOUT: its `subject` operand (`None` for an act with no dict payload). The one reader for
    `_cause_record` (the fold's act, off the store) and `sigma.odds_of` (the act in hand)."""
    payload = getattr(act, "payload", None)
    return payload.get("subject") if isinstance(payload, dict) else None


def _cause_record(w: Any, causes: list) -> Optional[str]:
    """v10 PC-10b -- THE RECORD THE CAUSING ACT IS ABOUT: the `subject` of `causes[0]`, read off the act store
    (`World.acts`; RESOLVE records the act before it reaches the seam, `loop/resolve.py`), or `None` (no cause,
    a cause the store does not hold, or a world with no store). Only a `challenge` Record answers `stakes_of`, so
    for `fight`, whose `subject` is a person, this changes nothing. The act names the Record; nothing re-derives
    which challenge a pair fights under."""
    store = getattr(w, "acts", None)
    return record_of(store.get(causes[0]) if store is not None and causes else None)


def _fight_score(w: Any, p: Any, verb: str) -> int:
    """A party's SKILL SCORE for the fight (B05.57, `UPR` §2 edit 2): `pool.score` (no attribute, no addend), `0` where the skill gives
    him none (`untrained: none`, a non-holder). It is what `ob_from_defender` opposes with and the base of his own pool. NOT `pool.faculty`,
    which applies the social pair (`pool_add`, `pool_floor`) and refuses a verb naming no `governing:` attribute (`fight` names none, B05.25)."""
    base = score(w, p, verb)
    return 0 if base is None else base


def believed_picture(w: Any, believer: Any, pid: str) -> tuple:
    """THE BELIEVER'S OWN PICTURE OF ANOTHER PERSON FOR A FIGHT (B14.24; `U5b_PC_residue` §8 item 1): `((weapon, armor), person)`, `person` standing in
    for him where the fight reads his body (`party_end`, `_carried_of`: `body`, `body_ceiling`, `attributes`). What the believer's ledger gives:
      * HIS KIT -- per field, his latest claim at `person_q.KIT_CLAIM + field`, else the world's where he has SEEN him (`person_q.has_seen`), else the
        Combatant's own default (`combat_kit.DEFAULTS`): a person who knows nothing of the opponent's kit gets the default kit, never the true one;
      * HIS WOUNDS -- his latest `person_q.BODY_CLAIM` (a man of that condition and no lasting mark), else the world's `body` and `body_ceiling` where
        he has seen him, else a man at the top of the condition scale, unmarked.
    Everything else of the opponent (skill score, pool addends, attributes) is read as the dealt fight reads it [ASSUMPTION; medium; Jordan to correct;
    revert: none needed, read-only]: the B14.24 item is the kit and the wounds. Reads `believer`'s ledger and the world only where the ledger says he has seen him."""
    other = w.persons[pid]
    seen = person_q.has_seen(believer, pid)
    held = dict(zip(("weapon", "armor"), kit_of(w, pid))) if seen else dict(combat_kit.DEFAULTS)
    at = (w.tick, w.fixtures.claim_decay())          # B09.01: his claims are read faded at this tick, never as stored
    kit = tuple(held[f] if (said := person_q.believed_kit(believer, pid, f, *at)) is None else said for f in ("weapon", "armor"))
    wound = person_q.believed_body(believer, pid, *at)
    scale = w.fixtures.get("condition_scale")
    if wound is not None:
        body, ceiling = wound, scale
    elif seen:
        body, ceiling = other.body, other.body_ceiling
    else:
        body = ceiling = scale
    return kit, SimpleNamespace(body=body, body_ceiling=ceiling, attributes=other.attributes)


def combat_input(w: Any, claimants: list, verb: str, record: Optional[str] = None, *, believer: Any = None) -> PersonalCombatInput:
    """THE HOST INPUT BUILDER (plan position `31b`, A-25): `World` -> the frozen record the fight reads.

    Reads `w.persons` (the two claimants), `w.records` (a challenge's `stakes`, through `stakes_of`), `w.fixtures`
    and, for each party's `kits` entry, what his rungs store (`world_q.kit_of`, CP-T03-03: his holdings, else his
    residence; the Combatant default for a person who holds no arms, which is everyone while `rosters.yaml:
    arms_kinds` is empty), and each party's authored `Person.attributes` (PC-06 K-1), and nothing else; the module that consumes the record never sees `World`. Its precondition is the adapter's PARTY-GAP checks (`resolve`,
    below): two claimants, both persons.

    `verb` (CP-T03-09) is the act's verb and fills `terms` from `rosters.yaml: duel_terms` -- the ONE path a
    non-lethal term reaches the fight by (`duel_terms_of`). A verb the roster does not name leaves `terms` at the
    record's own default, `'death'`, so `fight` builds the record it always built.

    `record` (v10 PC-10b) is the Record the act is about (`_cause_record`); a `challenge` Record's `stakes`
    (`world_q.stakes_of`) fill the SAME field through the same `duel_terms_of`, so `accept` is fought under the
    challenge's terms; where it names none the verb's `duel_terms` line stands (`accept: blood`, v11 CR-87) and a
    verb the roster does not name is fought under `'death'`.

    `believer` (B14.24), a `Person` who is one of the parties, reads every OTHER party's kit and wounds as `believed_picture` has them (his ledger's,
    the world's where he has seen him, the default kit and an unhurt body where he knows nothing); his own are the world's. `None` (the dealt fight
    and the display) reads the world's for both, as before.

    `verb` also fills the fight's TWO INPUTS (CR-85, ED-IN-0330; B05.57, `UPR` §2): `scores`, each party's skill score (`_fight_score`), and
    `addends`, each party's registered pool addends (`pool.addends_of`, the one sum `pool.faculty` takes), read from their owner `pool.py`
    (a leaf both this adapter and `sigma.py` import) and never copied. The pool is the module's: `pool_of(score, addends, pool_add,
    pool_floor)` with the fight row's two operands carried raw (`pool_add`, `pool_floor`), the Ob the opponent's skill score alone.
    `opposition_rate` is `None` in B05 (the module's own constant). `carried` (B05.61, A-8) is each party's wound as a signed level (`_carried_of`), filled
    only under `Fixtures carried_wound_model` `level` -- where `party_end` also cuts no band; under the control `endurance_cut` it is `(0.0, 0.0)`. `fight`, `accept` and `capture` draw on the `arms` capability key
    (CP-T03-04, `rosters.yaml: verb_capability`); a person holding no such key reads the untrained score `pool_default`.
    [ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays] -- the CR-85 design is UNRATIFIED (ED-IN-0351)."""
    a_id, b_id = claimants[0], claimants[1]
    terms = duel_terms_of(verb, stakes_of(w, record))
    pa, pb = w.persons[a_id], w.persons[b_id]
    # WHOSE KIT AND WOUNDS THE FIGHT READS: the world's (`kit_of`, the person), or -- `believer` named, B14.24 -- his OWN picture of every party but himself
    (ka, ba), (kb, bb) = ((kit_of(w, pid), p) if believer is None or pid == believer.id else believed_picture(w, believer, pid)
                          for pid, p in ((a_id, pa), (b_id, pb)))
    pool_add, pool_floor = pool_pair(w.fixtures, FIGHT_DICE_SITE)      # the fight row's `dice` names the two fixtures, as the social roll's does
    return PersonalCombatInput(
        claimants=(a_id, b_id),
        ends=(party_end(ba, w.fixtures), party_end(bb, w.fixtures)),
        wound_quantities=tuple(WOUND_QUANTITIES),
        kits=(ka, kb),
        scores=(_fight_score(w, pa, verb), _fight_score(w, pb, verb)),
        addends=(addends_of(w, pa, verb), addends_of(w, pb, verb)),
        pool_add=pool_add, pool_floor=pool_floor,
        carried=(_carried_of(ba, w.fixtures), _carried_of(bb, w.fixtures)) if _carried_level_model(w.fixtures) else (0.0, 0.0),   # B05.61: `level` only
        opposition_rate=None,               # None until 29-3 (B15): the fixture is live for the social roll since B05; the fight flips with its scale (A-71, A-31)
        **({} if terms is None else dict(terms=terms)),
        # PC-06 K-1: the attributes each party HOLDS (authored or drawn), whenever either party holds any -- under the
        # shipped build (`cast_attributes=True`) every person does, so this always passes them; the field's default (the
        # record as it was) is reached only where neither holds one.
        **({} if not (pa.attributes or pb.attributes) else dict(attributes=(dict(pa.attributes), dict(pb.attributes)))))


def _party_gap(a: str, b: str) -> dict:
    """The refusal of a fight that is not between two persons (one id as both claimants, or an id the world does not hold): the one
    spelling `fight_estimate` and `resolve` share."""
    return dict(status="PARTY-GAP", why=f"personal combat needs two persons; got {a!r} / {b!r}", module=_PROVIDER)


def fight_estimate(w: Any, actor: str, via: Any, target: Optional[str], verb: str = "",
                   record: Optional[str] = None, *, believed: bool = False) -> dict:
    """THE ODDS A FIGHT WOULD DEAL, SAMPLED LIVE (CP-T03-05; `-08` AM-C-02; MODE (a), THE PLAYER'S DISPLAY ONLY).

    Builds the real `PersonalCombatInput` (`combat_input`, so the fight is the one `resolve` deals when it is AUTOMATED (a fight the player plays turn by turn can end undecided on his withdrawal, which the shares do not assume): the same
    `end`s and the same `terms`: `verb`'s, from `rosters.yaml: duel_terms`, the one path), runs the module entry `estimate_samples` times, and returns the SHARES of the
    four ways a scene can end, `actor_felled`, `subject_felled`, `yielded` and `undecided`, which sum to 1
    (`status` `ESTIMATED`, beside the `samples` count). A refusal is `resolve`'s own dict (`PARTY-GAP`,
    `ENGINE-UNAVAILABLE`). `via` is accepted for the shape of the call and read by nothing today; `verb` names the
    `terms` (CP-T03-09), so a `capture` is sampled under the terms it is fought under, and `record` (the act's
    `subject`, as `resolve`'s `_cause_record` reads it) lets a challenge's `stakes` reach the sampler by the same
    `combat_input` path, so an `accept` is sampled under the terms it is fought under. CP-T04-08's `field_estimate`
    shares the fixture and the stream's key (`_estimate.py`).

    ⚠ THE RNG IS PRIVATE AND IS NOT A SEASON DRAW. It is built here from `H(world_seed, tick, actor,
    "estimate")` and never from `w.new_draw()` or the driver's generator, so the call reads `World` and writes
    nothing: `content_hash` is the same with it and without it, and the display is the same on every ask in a
    tick (a shown figure that moved on re-asking would be noise, not the odds). The fights are NOT the ones the
    fold will deal -- `resolve` seeds its own scene from the causing act -- so the shares are the distribution
    the scene is drawn from, not a forecast of the scene dealt.

    `believed` (B14.24, `U5b_PC_residue` §8) is THE ACTOR'S OWN ESTIMATE OF THE FIGHT, the caller `sigma.believed_chance` reaches by the
    `believed_estimate` role: the input is built on HIS PICTURE of `target` (`believed_picture`: his kit and wounds as his ledger gives them, the
    world's where he has seen him, the default kit and an unhurt body where he knows nothing), the sample count is `believed_fight_samples`
    (a belief is not a measurement: the display's `estimate_samples` stays the display's), the stream is keyed `(world_seed, tick, actor,
    "estimate.fight")` (A-30), and the return gains `subject_bands`, the share of the sampled scenes in which `target`'s own band
    (`ladder.party_degree`, the one grader, at `combat_wounded_above`) was each of `COMBAT_BANDS`. Reads and writes what the display does."""
    claimants = [actor, target]
    pa, pb = w.persons.get(actor), w.persons.get(target)
    if pa is None or pb is None or actor == target:
        return _party_gap(actor, target)
    n = samples_of(w, "believed_fight_samples" if believed else "estimate_samples")
    entry, refusal = entry_for(_PRIZE, _PROVIDER)
    if entry is None:
        return refusal
    inp = combat_input(w, claimants, verb, record, believer=pa if believed else None)
    rng = rng_of(w, actor, "estimate.fight" if believed else "estimate")
    tally = dict.fromkeys(ESTIMATE_OUTCOMES, 0)
    bands = dict.fromkeys(COMBAT_BANDS, 0)
    edge = w.fixtures.get("combat_wounded_above")
    for _ in range(n):
        got = entry.fn(inp, rng)
        tally[scene_outcome(got, actor, target)[0]] += 1
        if believed:
            bands[party_degree(_wound_state(got.wounds.get(target)), edge)] += 1
    return dict(status="ESTIMATED", module=_PROVIDER, samples=n, **{k: v / n for k, v in tally.items()},
                **(dict(subject_bands={b: v / n for b, v in bands.items()}) if believed else {}))


def scene_outcome(got: CombatOutcome, actor: str, target: str) -> tuple:
    """`(outcome, yielder)` -- HOW ONE SCENE THE MODULE ENTRY DEALT ENDED, THE ONE OWNER OF THAT READING (the random-pairs
    instrument reads a scene the way the display does).
    `outcome` is one of `ESTIMATE_OUTCOMES`; `yielder` is the id `got.surrender.by` names, `None` where
    nobody yielded. `got` is the entry's `CombatOutcome` (`wounds`, `surrender`).

    ⚠ THE FELLING IS `ladder.party_degree`'S VERDICT ON THE PARTY'S TRACKER (the walk `_eff_kill` writes by and
    `combat_degree` grades by; it refuses a missing tracker), NEVER the integer `wrapper.fight` returns (not lifted).
    That integer flips after the scene in `UPSET_FLOOR` of the decided fights and leaves the trackers alone, so it
    names a winner the fold never grades by. A yield is read first; neither or both down is `undecided` (a draw has
    no one felled; a mutual felling names no one)."""
    a_down, b_down = (party_degree(_wound_state(got.wounds.get(pid))) == FELLED for pid in (actor, target))
    if got.surrender is not None:
        return "yielded", got.surrender.by
    if a_down and not b_down:
        return "actor_felled", None
    if b_down and not a_down:
        return "subject_felled", None
    return "undecided", None


@provider("estimate", _PROVIDER)
def estimate(w: Any, act: Any, claimants: list, target: Optional[str]) -> Optional[tuple]:
    """THIS PROVIDER'S CASE FOR `sigma.odds_of`, MODE (a): the
    shares `fight_estimate` samples for the act, as `(actor felled, subject felled, yielded, undecided)`
    (`ESTIMATE_OUTCOMES`' order), or `None` for a party gap or a refusal. `claimants` is the fold's own derivation
    of the act's parties (`loop/sides.py::sides_of`, which `odds_of` calls once for every provider); `target` is
    unused here (the fight's second party is `claimants[1]`). Reads, draws and writes what `fight_estimate` does."""
    if len(claimants) < 2:
        return None
    got = fight_estimate(w, claimants[0], act.via, claimants[1], act.verb, record_of(act))
    return tuple(got[k] for k in ESTIMATE_OUTCOMES) if got["status"] == "ESTIMATED" else None


@provider("believed_estimate", _PROVIDER)
def believed_estimate(w: Any, believer: Any, act: Any, claimants: list, bands: Any) -> Optional[float]:
    """THIS PROVIDER'S CASE FOR `sigma.believed_chance` (B14.24; `U5b_PC_residue` §8 item 1): the believer's chance that the person the act is aimed at
    (`claimants[1]`, the one its writes land on) ends the fight in ANY of `bands`, the sum of `fight_estimate(believed=True)`'s `subject_bands` over
    them: the resolver sampled on the believer's own picture of him (`believed_picture`), no closed form and no table. The bands are read by the
    scene's own grader (`ladder.party_degree`), so the figure is the chance of the cells the verb's `writes:` lands on the subject, as `believed_chance`
    reads the social roll's bands. `None` for a party gap or a refusal, for another's act (the believer is the act's first claimant), and for a band
    the combat ladder does not carry (no figure here speaks for it). READ-ONLY: a private stream and no season draw."""
    if len(claimants) < 2 or claimants[0] != believer.id or not bands or any(b not in COMBAT_BANDS for b in bands):
        return None
    got = fight_estimate(w, claimants[0], act.via, claimants[1], act.verb, record_of(act), believed=True)
    return sum(got["subject_bands"][b] for b in dict.fromkeys(bands)) if got["status"] == "ESTIMATED" else None   # the bands in the order asked, once each: a set sums in hash-seed order


# ⚠ THE OUTCOME'S SEVERITY, READ OFF THE COMBATANTS THE SCENE JUST FOUGHT WITH (Jordan
# 2026-09-03). No number is invented and no rule is re-implemented: every field below is a
# property the engine's own `WoundTracker` computes, on the objects the module entry constructed
# and lifted into a `CombatOutcome` before `fight()` collapsed the scene to an int (`modules/combat/fight.py`).
_NO_FIELD = object()    # `getattr`'s default for a roster member the lifted record lacks


def _wound_state(lifted: Optional[PartyWounds]) -> dict:
    if lifted is None:                  # ID-5 polarity: absence REFUSES, it does not default
        return dict(available=False)
    # ⚠ THE FIELD LIST IS `rosters.yaml: wound_quantities`, NOT A LITERAL HERE (`H-98`, plan
    # position `8`) -- the same list `combat_band_edges` is validated against at load, so an
    # edge cannot name a quantity this does not lift. A member the tracker does not carry
    # REFUSES by name; skipping it would hand `combat_degree` a dict that lacks it.
    out = dict(available=True)
    for q in WOUND_QUANTITIES:
        v = getattr(lifted, q, _NO_FIELD)
        if v is _NO_FIELD:
            raise Unspecified(
                f"`wound_quantities` lists {q!r} and the engine's WoundTracker has no such "
                f"field", "S39.4/H-98", needs=f"a `WoundTracker.{q}`, or delete it from "
                "rosters.yaml: wound_quantities and from every edge that reads it",
                law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE; a quantity the "
                    "scene does not carry cannot be lifted")
        out[q] = v if isinstance(v, bool) else int(v)
    return out


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[Draw] = None, rung: Optional[str] = None,
            effort: int = 0, host: Optional[PlayHost] = None, via: Optional[str] = None) -> dict:
    """CALL the personal-combat engine. Returns what it said; decides nothing itself.

    ⚠ `host` (v10 REM-31, IN-46) IS A SECOND INPUT BESIDE §A.2's adapter row's "the projection" (the persons it plays and
    a decider), named here as that row's departure (B4, third disposition) and picked for the reason A-25 gives.
    IT IS WHERE THE DRIVER SUSPENDS, AND THE ONLY PLACE. `None` -- every RESOLVE
    call, and every season run without a host -- is AUTOMATED, today's call exactly. With a host, the mode
    is a PARTY TEST (A-25): a fight either of whose claimants the host plays (`PlayHost.persons`) hands the
    host's decider to the module entry, which forwards it to the engine's own turn loop; every other fight
    stays AUTOMATED. The suspension is a CALL-OUT, not a return: the scene runs inside this frame with the
    ENCOUNTER token held below it in the driver's argument expression (minted once), the typed record `inp`
    and the `seed` built by the same lines in both modes, and nothing serialized. The decider is handed
    no `World` and no token, and is written not to reach `World.write` or `World.new_draw` -- a CONVENTION
    (a closure over `w` could; the test that planted those two shapes is retired, and
    `test_rem31_grid_suspension.py::test_no_draw_and_no_mint_while_suspended` checks the shipped deciders); it draws only by NOT drawing
    (its turn's draws are the engine's, in the engine's order). The `RESOLVED` dict below gains no mode
    field, so the fold cannot tell the modes apart. Design: `proposals/2026-10-07-grid-mode-suspension.md`
    (PROPOSED, held back) and its `## Re-read at B-L`; reference, never the reason this is correct --
    `engine/season/tests/test_rem31_grid_suspension.py` is.

    `effort` (CP-T01-05) is accepted and NOT USED HERE, as `rung`: the seam's call is uniform, and combat
    sums its own sigma (`modules/combat/core.py`), outside `rosters.yaml: advantage_sources`.

    ⚠ `rung` IS ACCEPTED AND NOT USED HERE, AS `rng` BELOW (`ED-IN-0279` clause (a)). The seam's call is
    uniform; two duellists need no place to scope a derivation over.

    The RNG is seeded from the WORLD's own clock and the causing act, so a contest is reproducible
    exactly as every other draw in this instrument is (`S33`: *unique per DRAW, not per
    operation*). `wrapper.fight`'s own note says to pass `draw.seeded(...)` for determinism.

    ⚠ **`@provider` AND THE KEYWORD PARAMETERS ARE THE PROVIDER SIGNATURE.** ED-SC-0033 clause (1) rules that
    *"the seam dispatches by manifest ROW rather than the hardcoded personal_combat literal"*, so this
    function is reached by lookup; the keywords are the signature the seam calls every provider with.
    ⚠ **`rng` IS ACCEPTED AND NOT USED HERE, DELIBERATELY.** `04 §C.12`'s
    rejection 4 wants the generator constructed by the driver, and `seam/wrappers/sigma.py` is built
    that way. This module derives its own seed from `H(world_seed, tick, a_id,
    f"contest:{prize}:{causes[0]}")` — a DIFFERENT string from the driver's, with a different third
    argument — so consuming the driver's `rng` here would re-seed every `kill / wound`
    result and silently re-record the goldens under cover of a refactor. `04 PART D row 35` needs
    `purpose` UNIQUENESS, not one spelling across providers. The parameter is in the signature because
    the SEAM's call is uniform; whose seed a provider uses is the provider's.
    """
    if len(claimants) < 2:
        # `combat_bridge.derive_parties` returns None on a derivation gap rather than faking a
        # side; the same rule here.
        return dict(status="PARTY-GAP", why=f"personal combat needs two parties; got {len(claimants)}",
                    module=_PROVIDER)
    a_id, b_id = claimants[0], claimants[1]
    pa, pb = w.persons.get(a_id), w.persons.get(b_id)
    if pa is None or pb is None:
        return dict(status="PARTY-GAP", why=f"claimant not a person: {a_id!r} / {b_id!r}",
                    module=_PROVIDER)
    if a_id == b_id:   # `fight_estimate`'s own line: one id as both claimants is refused before the engine is called
        return _party_gap(a_id, b_id)
    inp = combat_input(w, claimants, verb, _cause_record(w, causes))
    rng = draw_factory(w.world_seed, lambda: w.tick)(a_id, f"contest:{prize}:{causes[0] if causes else ''}")
    entry, refusal = entry_for(prize, _PROVIDER)
    if entry is None:
        return refusal
    # THE PARTY TEST (REM-31). The AUTOMATED call is byte-identical: the keyword is passed only when a played
    # person is a claimant, so the two other entries' shared `(inp, rng)` shape is untouched.
    if host is not None and any(c in host.persons for c in (a_id, b_id)):
        got = entry.fn(inp, rng, decide=host.decide)
    else:
        got = entry.fn(inp, rng)
    _wounds = {a_id: _wound_state(got.wounds.get(a_id)), b_id: _wound_state(got.wounds.get(b_id))}

    return dict(status="RESOLVED", module=_PROVIDER, resolver="d_sigma",
                # THE DEGREE SOURCE. A caller reads severity from here; it does not map it from a winner, which
                # carries none (and which this return no longer names: B14.01). `H-98`'s remaining half is which
                # wound counts sit in which band -- an edge over a real quantity, not an invented correspondence.
                # ⚠ An undecided fight is a RULED outcome (Jordan, 2026-06-02: *"an undecided fight is a legitimate
                # outcome."*), and nothing here retries it into a decision.
                wound_state=_wounds,
                # §11.4: `None` unless a yield ended the scene (nobody felled, the yielder standing).
                surrender=None if got.surrender is None else dataclasses.asdict(got.surrender),
                # THE WOUND THAT ENDED IT: `None` when nobody was felled.
                beat=None if got.beat is None else dataclasses.asdict(got.beat),
                # THE SCENE'S COURSE, folded from its trace by the module entry (B14.15): `_eff_kill` puts it on the act's Events.
                shape=dataclasses.asdict(got.shape),
                rounds=got.rounds,
                # PC-06 M-1: THE SCENE'S OWN TRACE, AS THE MODULE ENTRY CAPTURED IT, returned for a grid display or
                # B-3's per-event measure. Nothing here or downstream folds it into `World`: `contest()` hands this
                # dict to `_fold` as `Resolution.result`, whose effects read `wound_state`, `surrender`, `beat` and `shape`
                # (`loop/effects_combat.py`); `trace` is read by none, so this key moves no hash by itself.
                trace=list(got.trace))
