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

v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`) add the fieldwork scene's pair, at the foot of the file:
`TrailItem` and `FieldworkInput` in, `Findings` out -- the `inquiry` role's records, for the same reason.
v9 IN-07 E1 adds the settlements module's larder records after them: `Eater`, `LarderInput` and `Under`
in, `DrawRow`/`DrawRecord` out (built by `queries/world_q.py::larder_input` and `under_input`).
v9 IN-07 E2 adds `SubsistInput` in, `SubsistOutcome`/`BodyFall` out, for `settlements.subsist`.
v9 IN-07 E3 adds `ProduceInput` in, `ProduceRow`/`ProduceOutcome` out, for `settlements.produce`.
v9 IN-07 E4..E6 add `HousingInput`/`Housing`, `FabricInput`/`Fabric` and `FortInput` (its entry returns a
`float`), for `settlements.housing`, `settlements.fabric` and `settlements.fortification`.
v9 IN-52 adds `ProvisionInput` in, `Provision` out, for `settlements.provision` (the levy-to-field feed).
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
                       prints its facts, not a 37 KB map;
      * `orders_of_battle` -- ED-IN-0305: `(attacker, defender)`, each an `OrderOfBattle` (the module's own typed
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
    orders_of_battle: Optional[tuple] = None


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
      * `larder`    -- the `LarderInput` the draw reads (`larder_input`'s projection, unchanged);
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
# the half it reads, so it pays the scans, `TRACE.query` rows and fixture reads its old body paid and no
# more (`residence_of` traces, `presence` traces, `Fixtures.reads` reaches `harness/corpus_run.py`'s
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
                        (`0` otherwise, unread), so the scan is paid exactly where it was;
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
      * `scale`      -- the `condition_scale` fixture, read only when `conditions` is non-empty (the old
                        body's read), else `None`. The entry returns a bare `float`."""
    conditions: tuple
    scale: Optional[int]


@dataclass(frozen=True)
class ArmyCommand:
    """What `mass_battle.army` (`modules/mass_battle/armyrecord.py::apply`) reads (ED-IN-0305 phase 2). Built by
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
    """What `mass_battle.army_order` (`modules/mass_battle/armyrecord.py::fielded`) reads (ED-IN-0305 phase 3).
    Built by `seam/wrappers/mass_battle.py::field_input` for one side of one field:
      * `record` -- the faction's army Record's `subject_matter` (`armyrecord.KEYS`), as the world holds it;
      * `fit`    -- `((cohort id, fraction), ...)`: each cohort of the side PRESENT on the field (mustered at the
                    place) and its body as a fraction of the full scale, in `[0.0, 1.0]`. A cohort not listed is
                    not there. The entry returns an `OrderOfBattle`, or None when nobody it names is present."""
    record: dict
    fit: tuple


@dataclass(frozen=True)
class ArmyOptionsQuery:
    """What `mass_battle.army_options` (`modules/mass_battle/armyrecord.py::options`) reads (ED-IN-0305 phase 5b). Built by
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
    """What `mass_battle.army_preset` (`modules/mass_battle/troop_types/presets.py::plan`) reads (ED-IN-0305 phase 5c). Built
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
