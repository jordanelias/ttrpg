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
15). `Margin` types the MODULE -> HOST boundary of the social contest container's provider: the module
entry returns one and the host adapter (`seam/wrappers/sigma.py::resolve`) refuses anything else, so a
winner cannot cross. The adapter still hands the seam the `dict` every provider returns -- the SEAM keeps
one return shape (`combat` returns a scene and `mass_battle` a field, neither a margin); typing the seam
itself is a `seam/` item of its own. It lives here, not in a sibling file, because a module imports it to
construct it and this leaf is the one host file a module may import
(`engine/season/tests/test_social_contest_module.py`).

v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`) add the fieldwork container's pair, at the foot of the file:
`TrailItem` and `FieldworkInput` in, `Findings` out -- the `inquiry` role's records, for the same reason.
v9 IN-07 E1 adds the settlements module's larder records after them: `Eater`, `LarderInput` and `Under`
in, `DrawRow`/`DrawRecord` out (built by `queries/world_q.py::larder_input` and `under_input`).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Optional


@dataclass(frozen=True)
class SocialContestInput:
    """What the `social_contest` module's σ-leverage roll reads, and nothing else.

    Built by `seam/wrappers/sigma.py::contest_input` (the host input builder) from `World`:
      * `pool`      -- dice, from what the actor genuinely has (`sigma.py::_pool_of`);
      * `opposition` -- the subject's score on the verb's capability key when the subject is a person
                       carrying one, else `None`. A RAW OPERAND, not an obstacle;
      * `obstacle_default` -- the `H-127` stand-in for a subject with no score to halve;
      * `obstacle_ceiling` -- the `H-213` bound on how hard one matter can get; `None` is the
                       uncapped control arm;
      * `obstacle_refusal_multiple` -- S27.4's multiple, the fixture the host adapter refuses on,
                       on the pair the entry returns;
      * `leverage`  -- the σ-layer μ-shift. Zero until something supplies leverage: an `assumption`
                       reading with no producer, stated as zero rather than fabricated.

    ⚠ NO `ob` FIELD, ON PURPOSE (v9 SC-01 step 14; ED-SC-0033 clause (3), *the obstacle has a single
    owner*). The obstacle is COMPOSED by the module (`modules/social_contest/roll.py::obstacle`) from
    the three operands above; the host carries them and composes nothing, so a host-side obstacle has
    no field to travel in. `engine/season/tests/test_sc01_obstacle_ceiling.py` fails if one returns.
    ONE RECORD IS ONE MATTER'S DRAW: the ceiling bounds each matter's obstacle on its own and nothing
    aggregates obstacles across a bundle (ED-SC-0038's per-matter pick, `H-213`).

    THE ROOM'S OPERANDS (v9 SC-02 `22a`; proceedings `19_PLAN.md` steps 17, 18, 20), RAW AS THE OTHERS:
      * `reception` -- the bench's signed regard for the actor (`queries/world_q.py::reception`,
                       route erosion inside it); `0.0` where the prize is heard by no room;
      * `reception_gain` -- the `H-215` fixture scaling it into the obstacle;
      * `proofs`    -- the actor's unmirrored proofs against the opponent, each weighed by remove
                       (`queries/world_q.py::proofs`); `0.0` where no room hears the prize;
      * `proof_step` -- the `H-216` fixture: how far one firsthand proof moves the obstacle.
    The module composes them (`roll.py::obstacle`); the host composes nothing. They default to the
    no-room reading so a record built for a prize no room hears reads exactly as before.

    THE EXAMINED DOCUMENT'S OPERAND (v9 SC-02 `22b` step 25), RAW AS THE OTHERS:
      * `forgery_quality` -- `Record.forgery_quality` of the Record an INQUIRY examines (`sigma.py::
                       contest_input`'s `examined`); `0` for a genuine document, for any subject that
                       is not a Record, and for every contest a prize names. Composed by the module."""
    pool: int
    opposition: Optional[float]
    obstacle_default: float
    obstacle_ceiling: Optional[float]
    obstacle_refusal_multiple: float
    leverage: float
    reception: float = 0.0
    reception_gain: float = 0.0
    proofs: float = 0.0
    proof_step: float = 0.0
    forgery_quality: float = 0.0


@dataclass(frozen=True)
class Margin:
    """What the social contest module's entry returns for one matter's draw: the roll's `net` and the
    `ob` it was thrown at, and nothing else (v9 SC-01 step 15; `08_SEAM.md`'s provider rule, intent
    only: *a MARGIN, never a winner*).

    ⚠ NO WINNER, NO BAND, NO SIDE. The band is the one ladder's reading of this pair
    (`seam/ladder.py::degree_of` -> `degree_from_net`), and who it favours is the fold's reading of the
    band; a field naming either would make the module a second resolver. The host adapter refuses a
    return of any other type (`seam/wrappers/sigma.py::resolve`)."""
    net: float
    ob: float


@dataclass(frozen=True)
class PersonalCombatInput:
    """What the `combat` module's fight reads, and nothing else (plan position `31b`).

    Built by `seam/wrappers/combat.py::combat_input` (the host input builder) from `World`:
      * `claimants` -- the two parties' ids, `(A, B)`: each is a `Combatant` label, and the engine's
                       result is `+1` when A wins, `-1` when B does, `0` UNRESOLVED (a ruled outcome);
      * `ends`      -- each party's one derived field, `end`, in `claimants` order
                       (`combat.py::party_end`, `H-97`); every other field is the class's own default;
      * `wound_quantities` -- the `WoundTracker` fields the host lifts per party after the fight
                       (`rosters.yaml: wound_quantities`, in roster order). The module reads them off the
                       trackers and returns what it found; the refusal for one the tracker does not carry
                       is the host's (`combat.py::_wound_state`)."""
    claimants: tuple
    ends: tuple
    wound_quantities: tuple


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
                       (`mass_battle.py::_side_stance`), which the module turns into a morale-start;
      * `walls_dr`  -- the `field_walls_dr` fixture (`H-150`); `None` is A.9's own number, which the
                       module reads from its terrain table;
      * `origin`    -- the geography territory id the attacking side marched from, or `None` where it
                       has no one origin (`mass_battle.py::_origin_of`, MB-05r). The module decides from
                       it and `territory` whether the march crossed a river (`terrain.py::river_crossed`);
      * `loyalties` -- `(attacker, defender)`: each side's weight-mean build-time loyalty row, the
                       stance toward its faction creed's utterer (`mass_battle.py::_side_stance` with
                       `_creed_referent`, MB-03), which the module adds to the morale-start at
                       `loyalty_gain`;
      * `loyalty_gain` -- the `field_morale_loyalty_gain` fixture (`H-148`'s site); `0` is the control,
                       battle history only;
      * `geography` -- the parsed geography file (`data/geography.py::geography`, read once per process
                       and SHARED by every record: read-only). The module's terrain lookup and river test
                       read it here and open no file. `repr=False`: a record in an assertion message
                       prints its facts, not a 37 KB map."""
    weights: tuple
    territory: Optional[str]
    fort_level: float
    stances: tuple
    walls_dr: Optional[int]
    origin: Optional[str]
    loyalties: tuple
    loyalty_gain: float
    geography: Mapping = field(repr=False)


# ---------------------------------------------------------------------------
# v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`): THE FIELDWORK CONTAINER'S RECORDS -- the `inquiry` role's
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
# kinds reaches `Rung.stores`' insertion order, and that order reaches `World.content_hash()`.
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
      * `ladders` -- `((home, (rung, parent, ...)), ...)`: each home's containment ancestry, the home
                     first, cut at the first id that is not a rung;
      * `stores`  -- `((rung, ((kind, units), ...)), ...)` for every rung on a ladder, each in its own
                     `Rung.stores` order."""
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
