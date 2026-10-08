"""
systems/threadwork/sim/coherence.py — Coherence as DISTANCE from the human equilibrium: two
quantities, elastic then plastic (P-10, P-15).

Canon source: canon/philosophy/07_drift.md §7.1 (what Coherence degradation is; elastic then
plastic; the point of no return) and §7.4 (the bands); canon/philosophy/RULINGS.md Batch 8 (E-1..E-4,
2026-09-07) and Batch 9 (C-1, C-2, 2026-09-08); canon/02_canon_constraints.md §A P-10 / P-15.

⚠ THE CITATION THIS FILE CARRIED UNTIL POSITION 27 IS SUPERSEDED, AND SO IS THE MODEL IT CITED.
It read `systems/threadwork/reference/threadwork_v30.md Part 3` — now quarantined under `.designs/`
(ED-IN-0231) and NOT a source — and implemented that Part's 10 -> 0 depleting integer track.
`ED-WR-0010`'s ruled row (2026-09-15, `registers/editorial_ledger_wr_archive.jsonl`) settles that
Part 3 is SUPERSEDED rather than edited, "by precedence": RULINGS.md had already replaced the
quantity. Nothing below is taken from Part 3; its band edges are not reused.

THE MODEL, and each clause is a ruling rather than a choice:
  - Coherence is a DISTANCE, not a resource (§7.1: "not a resource that runs out"). 0 is the
    equilibrium; the number grows as the configuration departs from it. The OLD direction
    (10 = coherent, 0 = crisis) is inverted, and a track that DEPLETES is exactly what RULINGS.md
    says must not be modelled ("What a track must not model is *depletion*").
  - TWO quantities with two different remedies (§7.1 "The point of no return"):
      `resting_point`        where the being rests once fully recovered. Moves OUT only by
                             permanent set; moves IN only by deliberate restorative work aimed at
                             the configuration (C-1: "extremely difficult to do but possible").
      `elastic_displacement` the stretch current stress has produced on top of the resting point.
                             Returns over time. `present_displacement` = the sum, and is what the
                             displacement bands read.
    They are STORED separately so that each remedy can write only its own field: `recover()`
    cannot touch the resting point because it never assigns it (§7.1: "recovery is elastic only:
    it never undoes a permanent set").
  - Elastic, then plastic (§7.1, ruled 2026-09-07). The elastic range is a CONSTANT of the being
    (E-3: no work hardening, no brittleness). Stretch that would pass the range is not held: the
    EXCESS becomes permanent set, the resting point moves out by exactly that excess, and the
    stretch sits at the range from the NEW resting point.
  - Only events deform (E-4). Every write here is an event a caller names. Nothing in this module
    adds displacement for time passing, and nothing ever will — "a load held below the threshold
    leaves nothing behind, however long it is held". Duration is a term INSIDE one event (the
    Leap's force x duration, §6.8), so it lives in the caller's stress magnitude, never here.
  - Recovery (E-1): time is the mechanism, environmental equilibrium is the condition, mending
    accelerates. See `recover()`.
  - Sensitivity is ORTHOGONAL (E-2: "exposure teaches; stress deforms"). This module holds no
    sensitivity term and must not grow one.
  - The point of no return (§7.1, §7.6). Being human is a BAND (derived, flagged in §7.1 as
    rejectable). Once the resting point leaves it the being "became other": working it back toward
    human is then restoring a remembered state — manipulation under §6.6 — so `mend_resting_point()`
    REFUSES past the crossing instead of offering a restore-to-human path.

WHY ACCUMULATION ACROSS EVENTS IS NOT CREEP. Stretch from separate events stacks until it is
recovered, and the event that carries the stack past the range is the one that deforms. That is
the reading C-2 forces (ruled 2026-09-08: Coherence loss is "supposed to build up in increments or a
big operation to discourage that player/character from doing it again without recuperation"), and
§7.1 bounds it: the range is how far a being "can be stretched ... and still come back", so stretch
cannot grow past it elastically. The rival — each event judged alone, stretch never stacking — lets a
practitioner who works and works take nothing permanent, which is §7.1's "It must bite" failing.
Creep (E-4) is deformation from a load HELD below the threshold; resting in between is exactly what
empties the stack, so a practitioner who recuperates between workings never yields from small ones.

⚠ WHAT IS NOT BUILT HERE, deliberately, each with the surface that owns it:
  - How much a working costs (the caller's `delta`): D-5 type x scale and §6.6's direction test
    live in the callers. R-14 (ruled 2026-09-09) adds a practitioner-side term — "how resilient
    their spirit is" — whose ARITHMETIC is unruled; it belongs in the working's cost, not in this
    state. Its one owner is `operations.resist_coherence_cost`, a swept fixture
    (`operations.RESILIENCE_GAIN`, shipped at the control 0), applied in
    `operations._resolve_operation`; `collective.py`/`opposing.py` do not route through it yet. ⚠ C-3's "cost is relative magnitude / no toughness term"
    was RETRACTED (RULINGS.md Batch 13) and is not modelled.
  - What follows the crossing (P-15's TS-gated branching, §7.5 reality-strain): this module reports
    the crossing and keeps the arithmetic running. Routing post-crossing load into the substrate has
    NO carrier: `systems/threadwork/sim/rendering.py`'s `apply_rs_strain` was STRUCK at position 27,
    and its docstring says why.

[ASSUMPTION: practitioner registry stored at module level when no world is passed — basis: legacy
 callers and tests that build no World. When a world is supplied, state lives on
 world.practitioners (post-2026-05-19 schema migration) and round-trips through
 CoherenceState.to_dict/from_dict (engine/autoload/game_state.py serialize/restore).]

Dependencies:
  - none (state store on engine/autoload/game_state.World.practitioners when a world is passed)

Entry points:
  - apply_coherence_delta(actor, delta, source, world=None) -> CoherenceState   # a STRESS event
  - recover(actor, *, seasons, environment_in_equilibrium, source, mending=0, world=None)
  - mend_resting_point(actor, amount, source, world=None) -> CoherenceState
  - check_coherence_failure_transition(actor, world=None) -> CoherenceFailureResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ─── The numbers. ⚠ EVERY MAGNITUDE BELOW IS INVENTED, AND LICENSED. ──────────────────────────────
# §7.4: "The numbers below are mechanism and are not owned by this document — the philosophy holds
# only that Coherence is indexed and that the stages are ordered." RULINGS.md (2026-09-07 note):
# the shape is "code's problem". So the MAGNITUDES are this file's to choose — the standing of
# `engine/season/rosters.yaml`'s `site_yield` (H-93) and `wound_harm_models` (H-123): an injected
# default, stated as invented rather than left to look derived.
# ⚠ WHAT IS *NOT* INVENTED is every ORDERING the canon fixes, and tests/valoria/
# test_coherence_elastic_plastic.py asserts each one so a re-tune cannot break it silently:
#   ELASTIC_RANGE >= DISPLACEMENT_FRACTURED_LOW — §7.1: a novice at rest "pushed as far as their
#     range allows" arrives in Fractured, and a veteran resting at Dissonant "arrives deeper".
#   DISPLACEMENT_DISSONANT_LOW <= HUMAN_BAND_LIMIT — §7.1 names a practitioner RESTING at Dissonant
#     who has not crossed, so the human band reaches at least that far.
#   HUMAN_BAND_LIMIT > RESTING_POINT_START — the band has extent (§7.1's derived "band, not
#     point": with a point, the first permanent set would already be the crossing).
# UNITS are chosen so the callers' existing integer costs (-1 per Relational working, -2
# Structural, -1 FR surcharge, -1 on a bad degree) keep their meaning: one unit of cost is one unit
# of stress. The callers were not re-priced by this position.
# The provenance tag is `[JUSTIFIED: ...]` — tools/ci_sim_fabrication_check.py's "mechanism
# sourced, magnitude fitted" — and never `[canonical: ...]`, because no canon names these numbers.

# Distance 0 = on the human equilibrium, where a being starts. The origin of the scale, not a tuning.
RESTING_POINT_START = 0            # [JUSTIFIED: canon/philosophy/07_drift.md §7.1 Coherence is distance from the human equilibrium; origin of that scale, ED-WR-0010]
# How far a being can be stretched from its resting point and still return; a constant (E-3).
ELASTIC_RANGE = 6                  # [JUSTIFIED: canon/philosophy/07_drift.md §7.1 elastic range constant per being; magnitude invented, ED-WR-0010]
# Farthest RESTING point still inside the human band. = the top of Fragmented, so a floor that
# reads Fractured IS the crossing: nobody rests at Fractured and stays human.
HUMAN_BAND_LIMIT = 5               # [JUSTIFIED: canon/philosophy/07_drift.md §7.1 being human is a band; extent invented, ED-WR-0010]

# §7.4 displacement bands — low edges of PRESENT displacement (inclusive). Stable is 0..1.
# Four displacement bands plus the terminal resting-point reading, because that is what §7.4 lists:
# Stable, Dissonant, Fragmented, Fractured, Coherence failure. The retired track's `Severed` band is
# NOT in §7.4 and is not carried; its `Rendering Crisis` is §7.4's `Coherence failure`.
DISPLACEMENT_DISSONANT_LOW = 2     # [JUSTIFIED: canon/philosophy/07_drift.md §7.4 band order; edge invented, ED-WR-0010]
DISPLACEMENT_FRAGMENTED_LOW = 4    # [JUSTIFIED: canon/philosophy/07_drift.md §7.4 band order; edge invented, ED-WR-0010]
# = ELASTIC_RANGE, so a novice at full stretch reads Fractured and a veteran reads deeper (§7.1).
DISPLACEMENT_FRACTURED_LOW = 6     # [JUSTIFIED: canon/philosophy/07_drift.md §7.4 band order; edge invented, ED-WR-0010]

# E-1 recovery rate: elastic return per season of rest in an environment at equilibrium.
# Calibrated on §7.4's own illustration — "shows as Fragmented while a hard operation still has hold
# of them and shows as Dissonant a month later, rested": about a band (2 units) a month, so a season
# returns the whole elastic range.
ELASTIC_RETURN_PER_SEASON = 6      # [JUSTIFIED: canon/philosophy/07_drift.md §7.4 "Dissonant a month later, rested"; rate invented, ED-WR-0010]

BAND_STABLE = "Stable"
BAND_DISSONANT = "Dissonant"
BAND_FRAGMENTED = "Fragmented"
BAND_FRACTURED = "Fractured"
BAND_FAILURE = "Coherence failure"   # §7.4's terminal band; P-15 / §7.6's "Coherence 0"

# Module-level practitioner state store — fallback when world is None.
# Key: actor id (str); Value: CoherenceState
_practitioner_state: dict[str, "CoherenceState"] = {}


def _store(world):
    """Return the practitioner store: world.practitioners if world supplied,
    else module-level fallback."""
    if world is not None and hasattr(world, 'practitioners'):
        return world.practitioners
    return _practitioner_state


def _displacement_band(d) -> str:
    """§7.4's ordered displacement ladder, read off ONE distance. The single owner of the edges."""
    if d >= DISPLACEMENT_FRACTURED_LOW:
        return BAND_FRACTURED
    if d >= DISPLACEMENT_FRAGMENTED_LOW:
        return BAND_FRAGMENTED
    if d >= DISPLACEMENT_DISSONANT_LOW:
        return BAND_DISSONANT
    return BAND_STABLE


@dataclass
class CoherenceLogEntry:
    """One event against the two quantities.

    kind:   'stress' (apply_coherence_delta) | 'recover' (recover) | 'mend' (mend_resting_point).
    amount: the non-negative magnitude the event carried — stress applied, return offered, or
            inward movement asked for. Permanent set taken by a stress event is
            resting_after - resting_before; nothing else can move the resting point outward.
    """
    kind: str
    amount: int
    source: str
    resting_before: int
    resting_after: int
    elastic_before: int
    elastic_after: int

    def to_dict(self) -> dict:
        return {'kind': self.kind, 'amount': self.amount, 'source': self.source,
                'resting_before': self.resting_before, 'resting_after': self.resting_after,
                'elastic_before': self.elastic_before, 'elastic_after': self.elastic_after}

    @classmethod
    def from_dict(cls, d: dict) -> "CoherenceLogEntry":
        return cls(kind=d['kind'], amount=d['amount'], source=d['source'],
                   resting_before=d['resting_before'], resting_after=d['resting_after'],
                   elastic_before=d['elastic_before'], elastic_after=d['elastic_after'])


@dataclass
class CoherenceState:
    """Per-being Coherence: the two stored quantities, and everything else DERIVED from them.

    `band`, `resting_band`, `present_displacement` and `crossed` are properties, not fields: a
    stored band beside the quantities it summarizes is a second writer waiting to disagree
    (CLAUDE.md §0.1 pt 1), and the retired track stored one.
    """
    actor: str
    resting_point: int = RESTING_POINT_START
    elastic_displacement: int = 0
    log: list[CoherenceLogEntry] = field(default_factory=list)
    # Set by check_coherence_failure_transition the first time it OBSERVES the crossing, so that
    # the crossing is reported exactly once. It is a reporting latch, not the crossing itself.
    failure_observed: bool = False

    @property
    def present_displacement(self) -> int:
        """§7.1: "their resting point plus whatever displacement current stress has produced"."""
        return self.resting_point + self.elastic_displacement

    @property
    def crossed(self) -> bool:
        """The resting point has left the human band (§7.1 point of no return). Monotone: nothing
        here moves a crossed resting point inward (mend_resting_point refuses; recover cannot)."""
        return self.resting_point > HUMAN_BAND_LIMIT

    def _band_of(self, distance: int) -> str:
        """§7.4's band ladder, read off ONE distance — except Coherence failure, which is the
        resting point having left the band regardless of which distance was asked for, and which
        rest does not return anyone from. Shared by `band` and `resting_band` (CLAUDE.md §8)."""
        if self.crossed:
            return BAND_FAILURE
        return _displacement_band(distance)

    @property
    def band(self) -> str:
        """§7.4: every band reads PRESENT displacement — except Coherence failure, which is the
        resting point having left the band, and which rest does not return anyone from."""
        return self._band_of(self.present_displacement)

    @property
    def resting_band(self) -> str:
        """§7.4: "the band someone comes to rest in is their floor" — the community's instrument."""
        return self._band_of(self.resting_point)

    def _log(self, kind, amount, source, resting_before, elastic_before):
        # LOGGED ONLY IF SOMETHING MOVED — an inactive practitioner would otherwise grow
        # `state.log` (and every snapshot built from it) by one no-op entry every event forever,
        # once wired into the season loop. The single owner of the guard: every caller (a stress
        # of 0 is legal per apply_coherence_delta's own contract; a recover or mend that changes
        # nothing is legal per theirs) passes through here, so the check belongs to the one place
        # that sees both before- and after-state, not duplicated at each call site (found by an
        # adversarial /simplify pass on this position).
        if resting_before == self.resting_point and elastic_before == self.elastic_displacement:
            return
        self.log.append(CoherenceLogEntry(
            kind=kind, amount=amount, source=source,
            resting_before=resting_before, resting_after=self.resting_point,
            elastic_before=elastic_before, elastic_after=self.elastic_displacement))

    def to_dict(self) -> dict:
        # `band` is written for a reader of the save; from_dict ignores it and re-derives.
        return {'actor': self.actor, 'resting_point': self.resting_point,
                'elastic_displacement': self.elastic_displacement,
                'failure_observed': self.failure_observed, 'band': self.band,
                'log': [e.to_dict() for e in self.log]}

    @classmethod
    def from_dict(cls, d: dict) -> "CoherenceState":
        if 'resting_point' not in d:
            # ⚠ A RETIRED-SHAPE RECORD ({'coherence': 0..10, ...}) IS REFUSED, NOT MIGRATED. One
            # number on the depleting track cannot be split into resting point and elastic stretch
            # without inventing how much of the loss was permanent. Measured 2026-09-29: every
            # committed snapshot carrying the key has `"practitioners": {}`, so nothing loads one.
            raise ValueError(
                f"CoherenceState.from_dict: record for {d.get('actor')!r} has no 'resting_point' — "
                "it is the retired 10-0 track shape, which cannot be split into the two quantities "
                "(canon/philosophy/07_drift.md §7.1) without fabricating the split.")
        return cls(actor=d['actor'], resting_point=d['resting_point'],
                   elastic_displacement=d['elastic_displacement'],
                   failure_observed=d.get('failure_observed', False),
                   log=[CoherenceLogEntry.from_dict(e) for e in d.get('log', [])])


@dataclass
class CoherenceFailureResult:
    """Result of checking for §7.4's Coherence failure (P-15 / §7.6's "Coherence 0")."""
    actor: str
    failed: bool                    # resting point is outside the human band
    just_transitioned: bool         # True iff this check is the first to observe it
    band: str
    resting_point: int
    present_displacement: int


def _get_or_create(actor: str, world=None) -> CoherenceState:
    """A being first seen rests on the equilibrium with no stretch."""
    store = _store(world)
    if actor not in store:
        store[actor] = CoherenceState(actor=actor)
    return store[actor]


def apply_coherence_delta(actor: str, delta: int, source: str, world=None) -> CoherenceState:
    """Apply ONE stress event — a Coherence cost — elastic then plastic (§7.1).

    delta:  a Coherence COST in canon's vocabulary ("Coherence loss", "the cost is their
            coherence"): zero or NEGATIVE, exactly as all four callers already pass it
            (operations.py `_resolve_operation`, opposing.py, collective.py, fieldwork knots.py
            rupture — every value they can produce is <= 0). The sign flips ONCE, here: a cost of
            -k is a stress of k, which moves the configuration k further from the equilibrium.
    source: free text naming the event, for the log.
    world:  if supplied, state lives on world.practitioners; else the module-level fallback.

    ⚠ A POSITIVE delta RAISES. The retired track read it as "recovery", but the ruling gives the
    two quantities DIFFERENT remedies — elastic return (`recover`) and moving the floor
    (`mend_resting_point`) — and one signed scalar cannot say which it means. No caller in the tree
    passes one, so this refuses a meaning nobody uses instead of guessing it.

    Stress stacks on current stretch; whatever would carry the stretch past ELASTIC_RANGE is taken
    as permanent set instead (the resting point moves out by exactly that excess, and the stretch
    sits at the range from the new resting point). After the crossing the same arithmetic runs:
    the being is still displaced by what it bears (§7.6's freefall); where that load SHOULD go
    instead is §7.5 reality-strain, not built here.

    Returns the updated CoherenceState.
    """
    if delta > 0:
        raise ValueError(
            f"apply_coherence_delta({actor!r}, {delta}, {source!r}): a positive delta is not a "
            "stress. Elastic return is recover(); moving the resting point inward is "
            "mend_resting_point(). They are different remedies (07_drift.md §7.1) and are not "
            "expressible as one signed number.")
    stress = -delta
    state = _get_or_create(actor, world=world)
    resting_before, elastic_before = state.resting_point, state.elastic_displacement
    stretched = state.elastic_displacement + stress
    if stretched > ELASTIC_RANGE:
        state.resting_point += stretched - ELASTIC_RANGE     # the permanent set: the excess, exactly
        state.elastic_displacement = ELASTIC_RANGE
    else:
        state.elastic_displacement = stretched
    state._log('stress', stress, source, resting_before, elastic_before)
    return state


def recover(actor: str, *, seasons, environment_in_equilibrium: bool, source: str,
            mending: int = 0, world=None) -> CoherenceState:
    """Elastic return toward the resting point, and NEVER past it (E-1; §7.1).

    The three terms are E-1's three, in its order of force:
      seasons                     TIME IS THE MECHANISM: ELASTIC_RETURN_PER_SEASON per season of
                                  rest (fractions allowed; the product is floored to whole units).
      environment_in_equilibrium  THE CONDITION. Required, with no default, so a caller cannot
                                  forget it: "surrounding configurations must themselves stand in
                                  harmony, or there is nothing to return toward" (§7.1). False
                                  returns nothing.
      mending                     ACCELERATES: extra units of return from one's own or another's
                                  mending — "accelerates the return without being required for it".
                                  `operations.attempt_mending` supplies it for the MENDER (C-1's
                                  restorative feedback, position 27).

    ⚠ DERIVED, NOT RULED: `mending` is gated by the environment too. E-1 says mending accelerates
    "this" — the return that has the condition — and §7.1's reason for the condition ("nothing to
    return toward") applies to any return, mended or not. Reject that and only the gate's scope
    moves.

    The resting point is never assigned here. That is the whole of "recovery is elastic only: it
    never undoes a permanent set" — structural, not a clamp that could be mis-ordered.
    """
    if seasons < 0 or mending < 0:
        raise ValueError(f"recover({actor!r}): seasons and mending are non-negative "
                         f"(got seasons={seasons}, mending={mending})")
    state = _get_or_create(actor, world=world)
    resting_before, elastic_before = state.resting_point, state.elastic_displacement
    offered = int(ELASTIC_RETURN_PER_SEASON * seasons) + mending if environment_in_equilibrium else 0
    state.elastic_displacement = max(0, state.elastic_displacement - offered)
    state._log('recover', offered, source, resting_before, elastic_before)
    return state


def mend_resting_point(actor: str, amount: int, source: str, world=None) -> CoherenceState:
    """Move the RESTING POINT inward — deliberate restorative work aimed at the configuration
    itself (C-1, ruled 2026-09-08: "extremely difficult to do but possible").

    A SEPARATE operation from recovery, and the only thing in this module that moves the floor
    inward. How hard it is to achieve is the caller's roll (the Ob of the working), not this
    function's: `amount` is what the working achieved. It floors at the equilibrium.

    ⚠ REFUSED PAST THE CROSSING. Once the resting point has left the human band, human is no longer
    where the configuration tends, so working it back is "restoring a remembered state — which is
    manipulation" (§7.1, §7.6: "The door is not locked. It leads somewhere else now."). That is a
    different operation with a Coherence cost of its own, and it is not offered here dressed as
    this one.
    """
    if amount < 0:
        raise ValueError(f"mend_resting_point({actor!r}): amount is non-negative (got {amount}); "
                         "outward movement is apply_coherence_delta's")
    state = _get_or_create(actor, world=world)
    if state.crossed:
        raise ValueError(
            f"mend_resting_point({actor!r}): resting point {state.resting_point} has left the human "
            f"band (> {HUMAN_BAND_LIMIT}). Past the crossing, working it back toward human restores a "
            "remembered state — manipulation, not Mending (canon/philosophy/07_drift.md §7.1).")
    resting_before, elastic_before = state.resting_point, state.elastic_displacement
    state.resting_point = max(RESTING_POINT_START, state.resting_point - amount)
    state._log('mend', amount, source, resting_before, elastic_before)
    return state


def check_coherence_failure_transition(actor: str, world=None) -> CoherenceFailureResult:
    """Report whether `actor` is in Coherence failure, and whether this is the first observation.

    P-15's FAIL test asks whether any mechanic allows "Coherence 0 with no consequence"; this is
    the surface a consumer reads the crossing from. Unlike the retired track's crisis flag it never
    clears: the crossing is not undone by rest, and mend_resting_point refuses past it.
    (Renamed from check_coherence_zero_transition: on a distance, 0 is the equilibrium, so "zero"
    would now name the opposite end.)
    """
    state = _get_or_create(actor, world=world)
    failed = state.crossed
    just_transitioned = failed and not state.failure_observed
    if failed:
        state.failure_observed = True
    return CoherenceFailureResult(
        actor=actor,
        failed=failed,
        just_transitioned=just_transitioned,
        band=state.band,
        resting_point=state.resting_point,
        present_displacement=state.present_displacement,
    )


def get_state(actor: str, world=None) -> Optional[CoherenceState]:
    """Inspection helper — returns the practitioner's current state, or None
    if the practitioner has never had an event applied."""
    store = _store(world)
    return store.get(actor)


def reset_all(world=None):
    """Test helper — clear the practitioner store. Not for production use."""
    store = _store(world)
    store.clear()
