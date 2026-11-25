"""`season.data.fixtures` -- the harness fixtures and the matter-economy tables.

Owns `Fixtures` (S42.2.1's inject/grade/sweep registry: *"never invent a constant. Inject it,
declare it a harness fixture at `grade: assumption`, name the injection site, run a 3-point
sweep, and treat A VERDICT THAT FLIPS ACROSS THE SWEEP AS ITSELF A FINDING"*), the matter
economy's three roster-backed tables and their loader (`_load_matter_tables` / `WEAR_RATES`,
`BAND_FLOORS`, `SUBSISTENCE_WEIGHTS`, `SITE_YIELD`), and `DEFAULT_FIXTURES`, the baseline
instance built from all of it.

⚠ `_load_matter_tables` SITS BETWEEN `Fixtures` AND `DEFAULT_FIXTURES`. `DEFAULT_FIXTURES` reads
three of its values (`wear_per_season`, `band_floors`, `subsistence_weight`) OFF `rosters.yaml`
rather than as literals (`W8` -- one declaration, and it is the data), so it cannot be built
until those tables have loaded, and `Fixtures` must exist first because `DEFAULT_FIXTURES` is an
instance of it. The order is: class, then loader, then baseline.
"""

from __future__ import annotations

from typing import Any

from engine.dice_engine.dice_engine import MU_PER_DIE

from ..gaps import Forbidden, Ungraded
from .rosters import ARMY_VERBS, CRISIS_ARMS, DIFFICULTY_LEVELS, MORTAL_CAUSES, STANCE_MAX, roster, roster_map, table

class Fixtures:
    """S42.2.1: never invent a constant. Inject it, declare it a harness fixture at
    `grade: assumption`, name the injection site, run a 3-point sweep, and treat A VERDICT
    THAT FLIPS ACROSS THE SWEEP AS ITSELF A FINDING.

    `wear_per_season` is per SITE KIND, with NO SILENT DEFAULT -- S42.2.1 names a wear table with
    a silent default as the exact prior sin. There is no `caller_supplied_max_depth`: S39.3 says
    the depth cap has NO DEFAULT, and a default relocated into a default-argument object is still
    a default."""

    def __init__(self, **vals: Any):
        self._v = dict(vals)
        self.reads: dict[str, int] = {}

    def get(self, name: str) -> Any:
        if name not in self._v:
            raise Ungraded(
                f"harness fixture '{name}' is not registered",
                "S42.2.1",
                needs="inject it, grade it assumption, name the injection site, sweep it",
                law="S42.2.1 -- a silent default does not fail; it answers, plausibly and wrongly, forever",
            )
        self.reads[name] = self.reads.get(name, 0) + 1
        return self._v[name]

    def wear(self, site_kind: str) -> int:
        """NO SILENT DEFAULT. An unregistered site kind RAISES rather than answering 20."""
        table = self.get("wear_per_season")
        if site_kind not in table:
            raise Ungraded(
                f"wear for site kind '{site_kind}' is not registered",
                "S42.2.1",
                needs="a per-kind wear row; S22 assigns `wear per site kind` to params",
                law="S42.2.1 -- 'a wear table that returns 20 for an unregistered site kind does not fail -- it answers, plausibly and wrongly, forever'",
            )
        return table[site_kind]

    def claim_decay(self) -> int:
        """`W4` / `H-40`. Confidence lost per season by a claim nobody refreshed — the THIRD
        licensed clock (#353 `:864`).

        ⚠ ON `wear`'s PRECEDENT, DELIBERATELY, INCLUDING THE REFUSAL. #353 licenses the clock and
        gives NO RATE, so this is an INJECTED DEFAULT with a site and a sweep (`H-40`, re-graded
        `assumption`), not a value the design states. It is registered rather than literal for the
        same reason `wear` is: *"a wear table that returns 20 for an unregistered site kind does
        not fail — it answers, plausibly and wrongly, forever."*"""
        # ⚠ ROUTED THROUGH `get()` so `self.reads` counts the read: `claim_decay_per_season` must be
        # VISIBLE to R5 and to `W9`'s check 3 -- the two guards whose whole job is "no fill off the
        # register". A guard that cannot see the thing it guards is not a weak guard, it is an
        # absent one (§0.1 point 2).
        if "claim_decay_per_season" not in self._v:
            raise Ungraded(
                "claim confidence decay is not registered", "S42.2.1",
                needs="a `claim_decay_per_season` fixture row",
                law="S42.2.1 -- an unregistered rate must REFUSE, never answer plausibly")
        return self.get("claim_decay_per_season")

    def sweep(self, name: str, value: Any) -> "Fixtures":
        f = Fixtures(**self._v)
        f._v[name] = value
        return f

def _load_matter_tables() -> tuple:
    """`W8`. The matter economy's three tables, from `rosters.yaml`, with load-time checks.

    ⚠ THE FIXTURE READS THE DATA RATHER THAN RESTATING IT (PLAN `W8`), so there is exactly one
    declaration and it is the data.

    ⚠ THE CHECKS ARE THE POINT, not the relocation. A wear or weight table whose keys drift from
    the roster is §42.2.1's worked sin arriving through a data edit instead of through a literal:
    an unregistered kind that ANSWERS. Both directions are checked — a rate for a kind no roster
    carries, and a site kind with no rate."""
    kinds = set(roster("site_kinds"))
    rates = roster_map("wear_per_season", "rates")
    floors = table("band_floors")
    weights = roster_map("subsistence_weight", "weights")
    for name, got in (("wear_per_season", set(rates)), ("band_floors", set(floors))):
        _check_keyed_on_site_kinds(name, got, kinds)
    yields = table("site_yield")
    if set(yields) - kinds:
        raise Forbidden(
            f"site_yield names site kind(s) no roster carries: {sorted(set(yields) - kinds)}",
            "rosters.yaml", needs="add the kind to `site_kinds`, or drop the row",
            law="S42.2.1 -- a table keyed past its own roster answers for a kind nobody declared")
    mk = set(roster("matter_kinds"))
    for sk, produced in yields.items():
        if set(produced) - mk:
            raise Forbidden(
                f"site_yield[{sk}] produces matter kind(s) no registry row carries: "
                f"{sorted(set(produced) - mk)}", "rosters.yaml",
                needs="add the kind to `matter_kinds`, or drop the cell",
                law="#353 §10.4 -- MatterKind is a REGISTRY. Open means addable, not unchecked")
    if not any(produced for produced in yields.values()):
        raise Ungraded(
            "site_yield is empty for every site kind", "rosters.yaml",
            needs="at least one producing kind, or delete the economy",
            law="PLAN W8 -- `yield` is the matter economy's ONLY source; an all-empty table is "
                "the `none` CONTROL ARM, and shipping the control as the default would make "
                "every store deplete monotonically while the proof clause claims otherwise")
    unknown = set(weights) - mk
    if unknown:
        raise Forbidden(
            f"subsistence_weight names matter kind(s) no registry row carries: {sorted(unknown)}",
            "rosters.yaml",
            needs="add the kind to `matter_kinds`, or drop the weight",
            law="#353 §10.4 -- MatterKind is a REGISTRY. Open means addable, not unchecked")
    return rates, floors, weights, yields


def _check_keyed_on_site_kinds(name: str, got: set, kinds: set) -> None:
    """THE BOTH-DIRECTION KEY CHECK every per-site-kind mapping gets: a row for a kind no roster
    carries is FORBIDDEN, and a site kind with no row is UNGRADED. One owner for the three mappings
    (`wear_per_season`, `band_floors`, `capacity_floor`) so they cannot come to disagree about what
    "keyed on `site_kinds`" means (§8)."""
    if got - kinds:
        raise Forbidden(
            f"{name} names site kind(s) no roster carries: {sorted(got - kinds)}",
            "rosters.yaml",
            needs="add the kind to `site_kinds`, or drop the row",
            law="S42.2.1 -- an unregistered kind must RAISE, and a table keyed past its own "
                "roster is that same silent answer arriving through the data file")
    if kinds - got:
        raise Ungraded(
            f"{name} has no row for site kind(s): {sorted(kinds - got)}", "rosters.yaml",
            needs=f"a {name} row per site kind",
            law="S42.2.1 -- 'a wear table that returns 20 for an unregistered site kind does "
                "not fail -- it answers, plausibly and wrongly, forever'")


def _load_capacity_floor() -> dict:
    """`24d-ii`'s FLOOR: `rosters.yaml:
    capacity_floor.floors`, `{site kind: the lower bound on world_q.capacity}`, checked in both
    directions against `site_kinds` exactly as `wear_per_season` and `band_floors` are. The row says
    why its cells hold the floor and nothing else, and `H-167` grades and sweeps the number. A
    SEPARATE loader rather than a fifth value of `_load_matter_tables`: that function's four-tuple
    is unpacked by callers outside this module, and the floor is not a matter-economy table."""
    floors = roster_map("capacity_floor", "floors")
    _check_keyed_on_site_kinds("capacity_floor", set(floors), set(roster("site_kinds")))
    return floors


def _load_works_cost() -> dict:
    """v9 IN-28 (`H-166` limit 1): `rosters.yaml: works_cost.costs`, `{plan kind: {matter kind:
    amount}}` -- what `found`/`build` charge the works' rung (the row says why, and why it is keyed
    ONE way, not on `site_kinds` in both directions: a plan kind with no row has no price and is
    refused). The checks are the ones a cost table can fail silently: a key no ladder or site roster
    carries (a price for nothing), an empty cell or a non-positive amount (a place that rises for
    free, which is the defect this table exists to close), a matter kind no registry row carries."""
    return _check_works_cost(roster_map("works_cost", "costs"),
                             set(roster("rung_kinds")) | set(roster("site_kinds")),
                             set(roster("matter_kinds")))


def _check_works_cost(costs, plans: set, mk: set) -> dict:
    """`_load_works_cost`'s refusals, with the rosters passed in so a test can plant each one
    (`data/requires.py::_check_record_sourced`'s precedent, §0.1 pt 3): a plan key no roster carries
    is FORBIDDEN; an empty or non-mapping cell, a matter kind no registry row carries, a non-int
    (or bool) or non-positive amount is UNGRADED. Returns the validated copy."""
    if set(costs) - plans:
        raise Forbidden(
            f"works_cost prices plan kind(s) no roster carries: {sorted(set(costs) - plans)}",
            "rosters.yaml", needs="a `rung_kinds` or `site_kinds` member, or drop the row",
            law="S42.2.1 -- a table keyed past its own roster answers for a kind nobody declared")
    for plan, cell in costs.items():
        if not isinstance(cell, dict) or not cell or set(cell) - mk or any(
                not isinstance(n, int) or isinstance(n, bool) or n <= 0 for n in cell.values()):
            raise Ungraded(
                f"works_cost[{plan}] is {cell!r}: a cost is a non-empty mapping of registered "
                "matter kinds to positive ints", "rosters.yaml",
                needs="a positive amount of a `matter_kinds` member, or drop the row (unpriced: refused)",
                law="H-166 -- a place that rises at no cost is the defect the table closes; a zero "
                    "cell would ship it again looking like a price")
    return {plan: dict(cell) for plan, cell in costs.items()}


WEAR_RATES, BAND_FLOORS, SUBSISTENCE_WEIGHTS, SITE_YIELD = _load_matter_tables()
CAPACITY_FLOORS = _load_capacity_floor()
WORKS_COST = _load_works_cost()

# `H-424`'s CONTROL ARM (B05.21, T13 edit 1; B05.23): `Fixtures.difficulty_ob` below is the shipped arm -- the CALIBRATED one since B05.23,
# 0 / 0.8 / 1.6 / 2.4 above the even line -- and this is the CONTROL, 0 / 1 / 2 / 3 (with an unopposed act's opposition at
# `opposed_ob(pool_default)` = 1.0 at the control rate it reproduces the 2.0 the stand-in gave). `DIFFICULTY_OB_ARMS` (below `DEFAULT_FIXTURES`)
# names the two; the control sweep is `DEFAULT_FIXTURES.sweep("difficulty_ob", DIFFICULTY_OB_CONTROL)`. T13 named the second arm `half`
# (0 / 0.5 / 1 / 1.5); B05.23's reading left C1 red at ranks 4 and 7 and C3 at rank 7 on it, so the arm that ships is not the half ladder and is
# named for what it is, `calibrated` (H-424's sweep keeps the half ladder as a point).
# [ASSUMPTION: the arm switch's form (a second module table beside the one Fixtures setting, not a second Fixtures key) -- basis: T13 edit 1 "two
# arms: `control` ... and `half`, shipped `control` in commit 1"; B05.14 shipped the control values. Jordan to correct; revert: none needed.]
# [JUSTIFIED: engine/season/hole_register.yaml H-424 -- the table's sweep names the control arm (0 / 1 / 2 / 3), so this arm is a point of that sweep]
DIFFICULTY_OB_CONTROL = dict(zip(DIFFICULTY_LEVELS, (0, 1, 2, 3), strict=True))

# [JUSTIFIED: engine/season/hole_register.yaml H-06 -- `site: Fixtures condition_scale`, graded `assumption`; the mechanism is sourced and the magnitude is injected here and swept]
_CONDITION_SCALE = 1000            # `H-06`'s value, named once so `wound_step` is derived from the fixture's own scale and not typed beside it

DEFAULT_FIXTURES = Fixtures(
    # S48: condition is an int on an EXPORTED scale. S22 assigns the scale to `params`, and the
    # in-chain params document "proposes NO VALUES", so this is a fixture. Injection site: here.
    # [JUSTIFIED: engine/season/hole_register.yaml H-06 -- `site: Fixtures condition_scale`, graded `assumption`; the mechanism is sourced and the magnitude is injected here and swept]
    condition_scale=_CONDITION_SCALE,
    # RULED TWICE. #353 §26.3 puts the budget at "~5"; Jordan ruled 2026-09-02 that the UNIT is
    # the SCENE and the number is 5 -- *"5 scenes for a character to play per season"*. A band is
    # not an integer; this is the integer the instrument runs on, and A31 sweeps it because the
    # verdict moves with it.
    # ⚠ THE KEY SAYS `scene`, NOT `act`: the ruling counts scenes ("a wounded duke gets fewer
    # SCENES than a healthy one"), and a name is where the next reader learns what the number counts.
    # [JUSTIFIED: engine/season/hole_register.yaml H-10 -- *the SCENE budget as an integer of the ruled band ~5*; #353 §26.3 gives the band, Jordan's 2026-09-02 ruling the unit, and a band is not an integer]
    scene_budget=5,
    # S20: the ledger cap L. Params-owned; no in-chain value.
    # CR-82 (ED-IN-0319: people remember one another for years): the cap is large enough that the
    # eviction comparator (S20/S34, `state/ledgers.py::eviction_key`), which drops the acquaintance
    # claims first, does not run through eight seasons (two years at four seasons to the year,
    # ED-IN-0332). ⚠ THE VALUE BUYS TIME, NOT RETENTION: the ledger grows with the horizon and does
    # not plateau, so on the growth the cap binds near season ten (extrapolated, not measured), and then the comparator forgets
    # the oldest first again. The next lever is a selective eviction rule (a change to the S20/S34
    # comparator), not a larger number; it is not built.
    # [ASSUMPTION; medium; Jordan to correct; revert: ledger_cap back to 200]
    # [JUSTIFIED: engine/season/hole_register.yaml H-09 -- `site: Fixtures ledger_cap (L) · view_k (K) · confidence_default`; S20 names L, no in-chain value exists, 3200 is injected and swept (CR-82)]
    ledger_cap=3200,
    # S18: "at most K claim ids from the holder's OWN ledger -- BUILT, NOT FILTERED".
    # [JUSTIFIED: engine/season/hole_register.yaml H-09, the same row as `ledger_cap` above; S18 names K and the magnitude is injected and swept]
    view_k=12,
    # S22 assigns `wear per site kind` to params. NO in-chain table exists, so every kind the
    # instrument touches is declared here and an unregistered kind RAISES (see Fixtures.wear).
    # roster-exempt: Fixtures keys. `Fixtures` IS the registry for numbers and raises on an
    # unregistered kind, so the kinds are already declared data; splitting them into
    # rosters.yaml would put one declaration in two files. ⚠ `site_kinds` belongs in
    # rosters.yaml when W8 builds H-07's per-kind table, and not before.
    # ⚠ THE TABLE LIVES IN `rosters.yaml` (`W8`) AND THIS READS IT: the declaration is in exactly
    # one place and this is not a copy of it. `Fixtures.wear` still refuses an unregistered kind.
    wear_per_season=WEAR_RATES,
    # S20: Claim.confidence. A value of 1 would degenerate the eviction comparator.
    confidence_default=100,
    # `U4` / `H-96`. THE TEMPERATURE OF THE TRIAGE — how far a person's choice of what to leave
    # undone departs from the top of their own ranking. `0` is the pre-U4 behaviour exactly
    # (argmax, ties alphabetical by verb name) and is kept as the CONTROL; the shipped value
    # samples the order by `softmax(score / tau)`.
    #
    # ⚠ THE MAGNITUDE IS INJECTED AND THE SHAPE IS NOT. R-08's statement is Jordan's — *"decisions
    # must not be omniscient and perfectly rational — characters make choices based on their own
    # inclinations"* — so THAT the choice is sampled is ruled; how sharply is a number no document
    # supplies.
    #
    # ⚠ THE VALUE IS CHOSEN ON A SWEEP BY A RULE, NOT ASSERTED: tau is the LARGEST grid value at
    # which REM-12's split (`harness/decision_spread.py --decisions`, the built realm) reads the
    # sampler's top as the strict score leader in MORE THAN ONE HALF of the readings, among persons
    # holding a pursuit vector, AND `test_u4_the_choice_is_sampling_and_the_argmax_is_its_zero_
    # temperature_control` passes. Between-world variety falls MONOTONICALLY with temperature,
    # because a hotter draw makes every world sample the same broad mixture.
    #
    # THE ANALYTIC FACT: for TIED candidates `score/tau` is equal whatever tau is, so their order is
    # decided by the draw ALONE at any nonzero temperature. The alphabetical tie-break this unit
    # exists to remove is therefore dead at any nonzero tau, BY CONSTRUCTION rather than by degree.
    #
    # WHAT THIS MEANS IN PLAY: a scored candidate beats a lower-scored one essentially always, and
    # where the table says NOTHING, chance decides. *Inclinations are decisive where they exist; the
    # draw decides where they do not.* That is a closer reading of Jordan's *"characters make
    # choices based on their own inclinations"* than a hot temperature, which would override the
    # inclinations it is supposed to express. ⚠ RE-DERIVE THIS IF the alignment table densifies: fewer
    # ties move what tau is doing.
    #
    # ⚠ THE ODDS WEIGHTING (`odds_weighting`, below) MOVES THESE SHARES BY NOTHING AT ANY GRID VALUE: it
    # reaches only `determine`'s pursuit term. ⚠ THIS IS A PROPERTY OF THIS FLAT FIELD, NOT A TUNED
    # OPTIMUM: most contested rows score alike at stance 0, so the share is a function of how tau
    # compares to the score gaps. It goes stale under any later mover of those gaps (B10-18's,
    # CL-PERSON's first non-neutral value).
    # ⚠ THE TEMPERATURE IS IN SCORE UNITS, AND SCORE MARGINS SCALE WITH `person_q.decisiveness` (the length of the
    # person's projected pursuit vector, shown on `decision/sheet.py::DevelopmentSheet`): the 46 persons holding a
    # question at round 0 of `build_realm(0)` read 0.14 to 0.89, so one temperature is a different draw for each.
    # [ASSUMPTION; medium; Jordan to correct; revert: choice_temperature 0.1, one re-pin]
    # [JUSTIFIED: engine/season/hole_register.yaml H-96 -- `site: Fixtures choice_temperature`, graded `measured`; the alphabetical tie-break is the measured defect and this is the injected magnitude of its remedy, swept 0 / 0.01 / 0.02 / 0.03 / 0.05 / 0.1 / 0.25 / 0.5 / 1.0, the row's own `sweep:`]
    choice_temperature=0.05,
    # `W4` / `H-40`, THE THIRD LICENSED CLOCK (#353 `:864`). #353 licenses confidence decay at
    # MATTER and gives NO RATE, so this is an INJECTED DEFAULT with a `site:` and a three-point
    # sweep on the register, exactly as `H-09` treats the confidence default beside it. It is a
    # fixture rather than a literal so `Fixtures.claim_decay` can REFUSE when it is unregistered
    # — `wear`'s precedent, and S42.2.1's rule.
    # [JUSTIFIED: engine/season/hole_register.yaml H-40 -- the THIRD licensed clock; #353 licenses decay at MATTER and gives NO RATE, so the rate is injected with a `site:` and a three-point sweep]
    claim_decay_per_season=5,
    # `W6` / `H-33`. WHICH WITNESS CHANNELS ARE LIVE.
    #
    # ⚠ THE DEFAULT IS `all_five`, BY RULING, AND `total` IS THE CONTROL. S61's *"WITNESS AS
    # SPECIFIED FANS EVERY EVENT TO EVERY PERSON"* is the design as written; `R7`
    # (`references/design_rulings_2026-09-06.md`) overtakes it: Jordan chose the architecture model
    # over the echo model -- *legitimacy falls where the news has reached* -- and `total` IS the echo
    # model arriving one layer down, at the deposit. Under it nothing is hideable, so there is no
    # secret, no lie, no rumour and no such thing as being ABSENT. `19_PLAN.md` step 1 is the same
    # instruction from the subsystem's side.
    #
    # WHY `all_five` AND NOT `presence_only`: `presence_only` COSTS QUESTIONS (the narrowest arm
    # thins the claim->question link), while `all_five` removes most of the deposits and leaves that
    # link where `total` had it. (`all_five` names five channels and, when W6 measured it, was a measurement of
    # THREE -- the then `chronicle` (since replaced by `reach`, B11.04) matched nobody and `post_remit` needs an obligee at the seat an act was
    # exercised through; `test_w6_every_named_channel_has_a_predicate…` asserts exactly which two
    # are inert.)
    #
    # ⛔ AND IT IS NOT FREE. At the shipped `observation_deposit_mode: actor`, `W-D` (89 worlds, 1,467
    # genuine forks) reads zero forks changing a later decision at `all_five`, against `total`'s 62
    # and `presence_only`'s 229. A fork can change a later decision by exactly ONE route: §F1
    # clause 4 (`engine/season/epistemic.py::belief_contradicts`) -- a claim in the actor's own
    # ledger contradicts a candidate's precondition, so the candidate is DROPPED
    # (`wd_extra.corpus_drops`). The divergences track the drops exactly: at the shipped
    # configuration clause 4 SIMPLY NEVER FIRES, so a fork has nothing to change.
    #
    # ⭐ **Every clause-4 drop in the corpus is the verb `move` refusing on a `contain.path:<person>`
    # belief** -- *there is no road from here to there*, formed by witnessing a `travel.blocked` and
    # overturned by a later `travel.moved`. So the reactivity this metric measures is produced
    # ENTIRELY BY PEOPLE BEING WRONG, and a wider channel set **corrects the stale belief before it
    # can bite.**
    #
    # ⚠ THE ARM MUST NOT BE CHOSEN ON THIS METRIC AT ALL, in either direction: it is a monoculture of
    # one verb, one predicate, one stale-belief shape. **The real defect it exposes is that §F1
    # clause 4 has exactly ONE reachable instance in the corpus.** So the fixture holds
    # `19_PLAN.md` step 1's arm, which is also the only arm that produces a SECRET BETWEEN TWO PEOPLE
    # IN THE SAME ROOM (`presence_only` gives absence, not secrecy: two co-located persons hold
    # identical witness sets, and `test_r7_two_persons_hold_different…` asserts the difference
    # `presence_only` cannot produce). Recorded on `H-33`.
    #
    # ⚠ M-6 CANNOT OBSERVE THE THIRD LINK: `_r3_propagates` is an `Event.causes[]` walk over
    # `driver.resolved` and never reads a ledger, so M-6 as `19_PLAN.md` specifies it CANNOT FAIL, and
    # a check that cannot fail is not a measurement (§0.1 pt 2). The third link is real: in
    # `tiny_world` (five persons across four rungs) the same flip changes the resolved-act set and
    # makes suppressing `move` stop being larder-neutral
    # (`test_w8_the_proof_clause_is_still_not_met…`). What `question_aggregation_rule: first` and the
    # five-scene budget flatten (`ID-16`; the gain is `H-106`) is the SIZE of the third link, not its
    # existence.
    #
    # The three points remain `H-33`'s own declared sweep and the channel list is untouched
    # (`19_PLAN.md` step 1: *"do not touch the channel list itself -- it is a sweep's arm set"*).
    fan_out_mode="all_five",
    # `H-87`. S39.3 REFUSES a default for the contest depth cap -- *"a default is a number
    # somebody made up and it will be cited later as though it were measured"* -- so `contest()`
    # takes it from the CALLER. This is the caller's number, injected and swept, and it lives here
    # rather than in a body so that it is one.
    contest_max_depth=2,
    # S15.2: entrenchment(h,H) = min(1, seasons_held / 60). The 60 IS in-chain; it is a fixture
    # only so no literal sits in a body.
    # [canonical: architecture/holonic_ARCHITECTURE.md §15.2 -- `entrenchment(h, H) = min(1, seasons_held / 60)`, verbatim at :556 under the §15.2 heading at :553. THE 60 IS IN-CHAIN, which is why this label is `canonical` where its neighbours are `JUSTIFIED`]
    entrenchment_seasons=60,
    # S27.4: "an attempt at Ob > 2 x Pool is refused, and the season is spent."
    # `U1` / `H-126`. THE OPERAND OF A CONTESTED ROLL THAT NOTHING ELSE SUPPLIES (the other, `obstacle_default`, is deleted: B05.14).
    #
    # ⚠ `pool_default` IS WHAT `capability` WOULD SUPPLY. `03 §A.2` rules the
    # mechanism — *"Rank supplies dice and gates nothing"* — and `Person.capability` is the store
    # it would come from; it is written by a cast overlay (`data/cast.py::capability_of`) and by
    # `loop/effects_combat.py`'s `_eff_train` and `_grown`, and is empty for a person none of them
    # reaches. For such a person the roll varies by SEED and FIXTURE rather than by PERSON, and
    # R-09 reads `partial` rather than `met` until capability is written. `08 §3`'s `assumption`
    # row is what licenses injecting it at all: *inject the default, declare the site, sweep three
    # points* — the grade that REFUSES is `absent`, and this is not one.
    #
    # ⚠ `pool_default` IS ALSO THE UNTRAINED SCORE OF AN OPPONENT (`seam/wrappers/pool.py::untrained`), and where no person stands opposite
    # (a docket item, a Record, a site, a self-plea) the opposition term of the obstacle is `opposed_ob(pool_default, opposition_rate)`
    # (`modules/social_contest/roll.py::obstacle`): the deleted stand-in `obstacle_default` (2, halved) is that term at the control. **NO "Base Ob by scale"** (Jordan, 2026-09-05).
    # [JUSTIFIED: engine/season/hole_register.yaml H-126 -- `site: Fixtures pool_default`, graded `assumption`; `capability` is the declared source and is empty on every corpus person, so the magnitude is injected and swept]
    pool_default=2,
    # B01a.01: WHAT A PERSON HOLDS ON AN ATTRIBUTE NOBODY AUTHORED -- uniform on this range, one keyed draw per person and attribute (`state/carriers.py::generated_attributes`). Read at build and at the in-play mint. `(2, 2)` is B01's flat seating at `pool_default` (the control); `None` generates nothing.
    # [JUSTIFIED: engine/season/hole_register.yaml H-856 -- site: Fixtures generated_attribute_range, graded assumption; swept (1, 6) SHIPPED / (2, 2) B01's flat seating / None nothing generated]
    generated_attribute_range=(1, 6),
    obstacle_refusal_multiple=2,
    # [JUSTIFIED: engine/season/hole_register.yaml H-213 -- `site: Fixtures obstacle_ceiling`, graded `assumption`; M-7 fails at the 1D floor above 2 (p_success 0.0006 at Ob 3), and 2 = obstacle_refusal_multiple x the 1D floor; swept 1 / 2 / 3, `None` the uncapped control]
    obstacle_ceiling=2,
    # CP-T01-06: THE `chance_floor` ARM OF THE CEILING. From one die the cap is solved per pool (the highest
    # Ob at which this pool keeps the chance `obstacle_ceiling` leaves a one-die roll), so the fixed value
    # above is the cap below one die and the floor's source; `False` is the fixed arm, `obstacle_ceiling`
    # `None` the uncapped one (both still swept).
    # [JUSTIFIED: engine/season/hole_register.yaml H-213 -- `site: Fixtures ceiling_per_pool`, graded `assumption`; the chance it holds is not a new number (band_odds(1, obstacle_ceiling)'s Partial-or-better, about 2.3 % at zero boost on the closed form, 0.08 % at the -M_MAX the cap is read at), swept True / False]
    ceiling_per_pool=True,
    # B05.53/B05.55: THE CEILING'S FORM -- how the obstacle behaves once it passes its ceiling. `hard` is the flat bound (the control,
    # SHIPPED); `soft` bends the excess toward the per-pool bound. B05.55's flip to `soft` is HELD: at `soft` no `difficulty_ob` ladder
    # lands the calibration targets C1 and C3 together (H-430, measured), so `hard` stays shipped. `soft_late` (knee at cap - 1) is a
    # third arm named in the source and NOT built (the code reads two forms).
    # [JUSTIFIED: engine/season/hole_register.yaml H-213 -- the same hole: how hard one matter can get; `site: Fixtures ceiling_form`, graded `assumption`; swept hard (control, SHIPPED) / soft (held, H-430)]
    ceiling_form="hard",
    # CP-T01-05: THE NAMED LEVEL ONE SLOT OF `effort` IS WORTH (`sigma_leverage.LEVEL_SIGMA`: minor / moderate /
    # strong / major). An act carrying `effort` e contributes e of these to the social roll's sigma term through
    # `rosters.yaml: advantage_sources` (a mu-shift, `net_boost`), and fills `1 + e` scene slots. The magnitude is
    # Jordan's to tune (`resolution-diagnostic` section 7: the levels are Class B draft sim-seeds).
    # [JUSTIFIED: engine/season/hole_register.yaml H-244 -- `site: Fixtures effort_level`, graded `assumption`; the magnitude of one slot of effort is no document's, so it is injected and swept minor / moderate / strong]
    effort_level="moderate",           # `H-244`, swept minor / moderate (SHIPPED) / strong
    # CP-T01-02: THE PRACTICE ARM (`queries/world_q.py::practice`, a pool addend `faculty` sums). A person's pool in
    # a verb's key rises by the count of his own Success-or-better acts in it within the last `practice_window`
    # closed seasons, divided by `practice_step` (floor), capped at `practice_cap` dice. THE ARM SHIPS LIVE (v10 CR-18,
    # window 4, step 2, cap `pool_default` = 2): a delegated choice at CLAUDE.md §0's ladder step 5, a capped positive
    # loop (success -> dice -> success) and not a gain; the window damps it and the cap bounds it. `practice_cap` 0 is
    # the control: the arm off, the realm byte-equal to the tree without it. The three numbers are no document's.
    # [ASSUMPTION; medium; Jordan to correct; revert: `practice_cap` 0]
    # [JUSTIFIED: engine/season/hole_register.yaml H-245 -- `site: Fixtures practice_window`, graded `assumption`; how long a good result keeps a person better is no document's, so it is injected and swept 2 / 4 / 8]
    practice_window=4,                 # `H-245`, swept 2 / 4 / 8 (seasons; read only when `practice_cap` > 0)
    # [JUSTIFIED: engine/season/hole_register.yaml H-246 -- `site: Fixtures practice_step`, graded `assumption`; how many good results buy one die is no document's, so it is injected and swept 1 / 2 / 4]
    practice_step=2,                   # `H-246`, swept 1 / 2 / 4 (good results per die)
    # [JUSTIFIED: engine/season/hole_register.yaml H-247 -- `site: Fixtures practice_cap`, graded `assumption`; the most dice practice can add is no document's, so it is injected and swept 0 (the control, the arm off) / 1 / 2 (SHIPPED, = pool_default)]
    practice_cap=2,                    # `H-247`, swept 0 (control, off) / 1 / 2 (SHIPPED, = pool_default)
    # v9 SC-02 `22a` (proceedings `19_PLAN.md` steps 17 and 18), B05.17 (PES-A): THE ROOM'S THREE MAGNITUDES, carried raw by
    # `seam/wrappers/sigma.py::contest_input`. A HOSTILE bench is an obstacle term (`reception_gain x |reception|`, the `reception`
    # member of `obstacle_terms`); what the speaker BRINGS is leverage, never an obstacle reduction: a favourable bench is `favour`
    # levels (one `favour_level` per whole unit of `reception_gain x reception`) and an unmirrored proof is `proofs` levels (one
    # `proof_level` per whole unit of `world_q.proofs`), both `rosters.yaml: advantage_sources` members. `0` is `reception_gain`'s
    # CONTROL (the room moves nothing) and `None` is each level's (the source brings nothing).
    # [JUSTIFIED: engine/season/hole_register.yaml H-215 -- `site: Fixtures reception_gain`, graded `assumption`; no document gives how far a bench's regard moves an obstacle, so it is injected and swept 0 / 1 / 2]
    reception_gain=1.0,                # `H-215`, swept 0 (control) / 1 (SHIPPED) / 2
    # [JUSTIFIED: engine/season/hole_register.yaml H-216 -- `site: Fixtures proof_level`, graded `assumption`; no document gives how much one unmirrored proof is worth to the speaker, so it is injected and swept None / minor / moderate]
    proof_level="minor",               # `H-216`, swept None (control) / minor (SHIPPED) / moderate
    # [JUSTIFIED: engine/season/hole_register.yaml H-425 -- `site: Fixtures favour_level`, graded `assumption`; no document gives how much a unit of a bench's favour is worth to the speaker, so it is injected and swept None / strong / major]
    favour_level="major",              # `H-425`, swept None (control) / strong / major (SHIPPED)
    # B05.60 (ADV Edits B to D; A-8): THE WOUND AS A LEVEL ON THE ROLL, read by `seam/wrappers/sigma.py::_wound_levels` (`rosters.yaml: advantage_sources: wounds`).
    # One named level AGAINST the roller per `wound_step` of body his person has lost below his `body_ceiling`, one FOR him per `wound_step` the person he acts on
    # has lost, each side at most `wound_levels_max`; never an obstacle term. `None` is `wound_level`'s CONTROL (the source brings nothing). `wound_step` is a third
    # of the scale, a third of `condition_scale`'s SHIPPED value (`_CONDITION_SCALE // 3`, frozen at import: two thresholds, at one third and two thirds lost). It is its own swept key (H-432: a sixth / a third / a half), so a swept `condition_scale` does not move it.
    # [JUSTIFIED: engine/season/hole_register.yaml H-431 -- `site: Fixtures wound_level`, graded `assumption`; no document sizes what a wound costs a roll, so it is injected and swept None / minor / moderate]
    wound_level="minor",               # `H-431`, swept None (control) / minor (SHIPPED) / moderate
    # [JUSTIFIED: engine/season/hole_register.yaml H-432 -- `site: Fixtures wound_step`, graded `assumption`; a third of `condition_scale` per level is ADV Edit D's own size, injected and swept]
    wound_step=_CONDITION_SCALE // 3,  # `H-432`, swept a sixth / a third (SHIPPED) / a half of `condition_scale` (body lost per level)
    # [JUSTIFIED: engine/season/hole_register.yaml H-433 -- `site: Fixtures wound_levels_max`, graded `assumption`; the most levels a wound can stack is ADV Edit D's two, injected and swept]
    wound_levels_max=2,                # `H-433`, swept 1 / 2 (SHIPPED) / 3 (levels, per side)
    # B05.61 (`UPR` §3 edit 1; A-8): HOW A WOUND CARRIED INTO A FIGHT ENTERS IT, read ONLY by `seam/wrappers/combat.py` (`party_end`, `combat_input`).
    # `level` is the A-8 arm and the SHIPPED one since B15.11 (`UPR` §3's flip): the authored Endurance whole, and the person's `wounds` level carried
    # on `PersonalCombatInput.carried` against his own attack and defence. `endurance_cut` is the CONTROL: Endurance one point lower per body band, the
    # tracker clean (Health, Wound Interval and Max Wounds all shrink).
    # [JUSTIFIED: engine/season/hole_register.yaml H-434 -- `site: Fixtures carried_wound_model`, graded `ruled` (A-8); the arm is swept level (SHIPPED) / endurance_cut (control)]
    carried_wound_model="level",           # `H-434`, swept endurance_cut (control) / level (SHIPPED since B15.11)
    # v9 SC-02 `22b` step 24 (proceedings `19_PLAN.md` step 24): HOW FAR A DETERMINATION MOVES ITS MAKER'S
    # OWN PURSUITS, per unit of `queries/person_q.py::pursuit_lean` and per band step (`data/rosters.py::
    # DEGREE_STEP`), read by `person_q.consequence_pursuits` from `loop/effects_information.py::
    # _eff_determine`. `0` is the CONTROL: no consequence write, every determination as before.
    # [JUSTIFIED: engine/season/hole_register.yaml H-221 -- `site: Fixtures pursuit_shift`, graded `assumption`; no document gives how far a consequence moves a conviction, so it is injected and swept 0 / 0.1 / 0.25]
    pursuit_shift=0.1,                 # `H-221`, swept 0 (control) / 0.1 (SHIPPED) / 0.25
    # B07.02 (18-A edit 5): `default_forgery_quality` (H-210) is RETIRED -- the forgery quality a drawn `forge` / `conceal` writes is
    # `rosters.yaml: forge_quality`'s, by band (`data/rosters.py::forge_quality_at`).
    # v9 SC-02 `22b` step 23 (`19_PLAN.md` step 23): THE STANDING BANDS -- floors on `decision/options.py::
    # standing_of`'s gap (on `condition_scale`), read by `loop/matter.py::_standing_crossings`. A band is
    # `budget.body_band_penalty`'s reading (the floors a value is below), and the crossing is the band of
    # the gap over the claims landed before last season differing from the band over all of them. `()` is
    # the CONTROL: one band, so nothing crosses and no person-keyed question is ever raised.
    # [JUSTIFIED: engine/season/hole_register.yaml H-223 -- `site: Fixtures standing_band_floors`, graded `assumption`; no document gives where the standing gap's bands fall, so it is injected and swept () / (500,) / (250, 500, 750)]
    standing_band_floors=(500,),       # `H-223`, swept () (control) / (500,) (SHIPPED) / (250, 500, 750)
    # REM-50: WHERE A SETTLEMENT'S HUNGER BANDS FALL, in whole SEASONS OF FOOD ON HAND: the first floor is
    # `hungry`'s, the second `lean`'s (`world_q.HUNGER_FLOOR_BANDS`); `starving` (a shortfall in the next
    # draw) is not a floor. Read ONLY by `world_q.hunger`, a report the loop never reads. `()` is the
    # CONTROL: no floor band, so `starving` or `fed`.
    # [JUSTIFIED: engine/season/hole_register.yaml H-242 -- `site: Fixtures hunger_band_floors`, graded `assumption`; no document gives where a settlement's hunger bands fall, so the floors are injected and swept () / (1, 2) / (2, 4)]
    hunger_band_floors=(1, 2),         # `H-242`, swept () (control) / (1, 2) (SHIPPED) / (2, 4)
    # S12.1 gates verbs on `condition` against per-kind band FLOORS. S22 assigns "band
    # coefficients" and "the obstacle floor" to params; the params document proposes NO
    # VALUES, so these are harness fixtures and A31c sweeps them. S42.2.1 names "three band
    # edges" as one of the four constants a prior instrument in the chain invented.
    # roster-exempt: Fixtures keys, as `wear_per_season` above. These are H-08 and are swept.
    band_floors=BAND_FLOORS,          # `W8` -- `rosters.yaml: tables.band_floors`, `H-08`
    # `24d-ii`: the lower bound on
    # `world_q.capacity`, per site kind, read off `rosters.yaml: capacity_floor` (`H-167`, swept).
    capacity_floor=CAPACITY_FLOORS,
    # v9 IN-28: what a works' plan costs its rung, read off `rosters.yaml: works_cost` (`H-166`, swept).
    works_cost=WORKS_COST,
    # ⚠ `W8` / `H-26`. #353 §22.3 names *"`season_factor`'s distribution"* as a value with NO
    # OWNER, and §25 says `yield` is *"blocked on"* it -- so the SHAPE ruled is a DISTRIBUTION and
    # what is injected here is a degenerate one. The sweep is on its value, which is the only axis
    # a constant has; a real distribution is a different hole and is not invented here.
    season_factor=1.0,                # `H-26`, swept 0.5 / 1 / 2
    # v9 IN-21 / `H-26`'s DISTRIBUTION: one tuple per season of the year (so the year's length is the
    # table's), each holding the equally likely multipliers on `season_factor` that season. `()` is
    # the CONTROL: no year, no draw, the bare constant above. The on arm is the declared sweep
    # `((0.5, 1.0, 2.0),) * 4`; a drought-only arm is `((0.5,),) * 4`. Drawn by
    # `world_q.season_factor_of`, keyed on (world_seed, tick, territory rung id).
    season_factor_draw=(),            # `H-26`, swept () / ((0.5,),)*4 / ((0.5, 1.0, 2.0),)*4
    # ⚠ `W8` / `H-11`. #353 §10.4 makes `MatterKind` open and V2 gives the draw's SHAPE -- *from
    # the containing rung's stores, scaled by weight* -- and no weights. Registry row, not literal.
    subsistence_weight=SUBSISTENCE_WEIGHTS,
    # W5 / `H-28`. §F3's `budget` has three modifier terms and #353 gives a value for NONE of
    # them -- `:912-913` says only that "a wounded duke gets fewer acts than a healthy one".
    # So the DIRECTION is ruled and the MAGNITUDE is not, which is exactly a fixture. Injection
    # site: here. Row: `H-70`, swept. ⚠ The BAND TABLE they read is NOT invented -- `band_floors`
    # above already carries a `"body"` row, so `condition_penalty(p's body band)` counts bands
    # against the table the site gate already uses. `H-38` closed with "`Site.condition` is the
    # model"; this is that closure spent rather than restated.
    # `H-54`, swept. The rule was `qs[0]` in a subscript; see `aggregate_questions`.
    question_aggregation_rule="first",
    # `W17` / Jordan 2026-09-02. The unit is the scene and the number is 5; NEITHER of these two
    # was ruled, so both are fixtures with register rows and a sweep. Source for both defaults:
    # `player_agency_v30.md` §6.3 -- "One scene action = one scene opportunity pursued. A scene
    # contains 1-3 mechanical interactions" -- which is `## Status: CANONICAL` but pre-#337 and,
    # under `CLAUDE.md` §0.05, REFERENCE rather than mechanism. `None` means unbounded.
    # [JUSTIFIED: engine/season/hole_register.yaml H-76 -- `site: Fixtures interactions_per_scene`; `player_agency_v30.md` §6.3 gives *1-3 mechanical interactions*, CANONICAL but pre-#337 and REFERENCE under CLAUDE.md §0.05, so the magnitude is fitted]
    interactions_per_scene=3,          # `H-76`, swept 1 / 3 / unbounded
    extended_scene_cost=2,             # `H-77`, swept 1 / 2 / 3
    scene_packing_rule="greedy",       # `H-78`, swept greedy / one_per_scene / by_subject
    # `U2` / `H-124`. HOW MANY OF THE FIVE A PERSON MAY SPEND IN ONE LAP of the scene tick.
    #
    # ⚠ THIS IS NOT `scene_budget` UNDER A SECOND NAME. `scene_budget` is 5 and is the season's
    # total, RULED (Jordan, 2026-09-02: *"5 scenes for a character to play per season"*). This is
    # how those five are SPREAD across the season, and nothing rules it.
    #
    # ⚠ AND IT BOUNDS THE DRIVER, NOT THE PERSON. The person still chooses against their whole
    # season remainder — `pack_scenes` takes that as its COST budget, so an extended scene
    # (`extended_scene_cost` = 2) is still affordable — and the driver releases this many of the
    # scenes they chose per lap. Nothing is discarded, only deferred, so S26.3's *the engine
    # never truncates* is untouched. Making this the person's bound instead would have trimmed
    # every extended chunk to one interaction and driven `H-77`'s sweep inert.
    #
    # ⚠ `5` IS A REAL ARM AND NOT A CONTROL. A person whose triage leaves budget UNSPENT empties
    # their queue with remainder left, so a later lap asks them again and they spend it — where
    # the one-pass loop simply lost it. THE CONTROL IS THE `scene_budget = 1` ARM (one lap).
    # [JUSTIFIED: engine/season/hole_register.yaml H-124 -- `site: Fixtures scenes_per_lap`, graded `assumption`; Jordan ruled the unit, the per-season count and that the tick is scene-granular, and supplied no number for the lap, so this is injected, declared and swept 1 / 2 / 5]
    scenes_per_lap=1,                # `H-124`, swept 1 / 2 / 5; the control is `scene_budget = 1`
    claim_subject_rule="both",         # `H-79`, swept actor / per_change / both
    # `W-B` / `H-122`. WHO RECEIVES A CLAIM MINTED FROM WHAT THE FOLD READ. #353 §28 says WITNESS
    # deposits and never says whether the deposit may carry the reads, or to whom; the arms are
    # `rosters.yaml: observation_deposit_modes` and the row is `H-122`. `none` is the CONTROL --
    # the behaviour before `W-B` exactly -- and the default below is argued on the row rather than
    # assumed here. Injection site: this line, read by `SeasonDriver.witness`.
    observation_deposit_mode="actor",  # `H-122`, swept none / actor / total
    # `H-80`. #353 §13.1 says the ACT declares a Record's stages and their terms. §F1's Candidate
    # is `(verb, subject, why)` and carries no operands, so NO COMPUTED ACT CAN DECLARE ANY --
    # `(Record, stages)` is a Part D row unreachable from the person's own decision. These are
    # the instrument's declared stand-in, swept, and the row says plainly that they are.
    # [JUSTIFIED: engine/season/hole_register.yaml H-80 -- a computed act cannot declare its OPERANDS, so this is the instrument's declared stand-in, swept, and the row says so]
    record_stages_default=3,
    record_stage_term=1,
    budget_office_bonus=1,
    budget_leg_penalty=1,
    # `H-94`, `W-C`. THE TWO OPERANDS §54 ITEM 7'S FORMULA NAMES AND THE DESIGN NEVER SUPPLIES.
    # `stores(hearth(giver), kind) >= amount`: `hearth(giver)` is the actor's own live `contain`
    # Tenure and `to` is the question's referent, so both are DERIVED person-side -- but `kind`
    # and `amount` are values nobody states, which is `H-80`'s shape exactly (a declared stand-in
    # for operands the person cannot supply). Declare, default, sweep.
    #
    # ⚠ ONE OWNER OF THESE VALUES: the fold does not fill them under the person for an act whose
    # payload carried neither (a `transfer` whose effect then raised on operands the precondition
    # had invented for it).
    # ⚠ `H-94`'s `sweep: [0, 1, 3]` are INTEGERS, which cannot be arms for a matter kind, so the
    # kind has its own row (`H-121`) and its own three arms: `grain` (stocked) · `salt` (a second
    # stocked kind, which proves the fixture reaches the effect -- the store that moves is the one it
    # names) · `coin` (registered in `rosters.yaml: matter_kinds`, produced by no site and held by
    # no rung: THE CONTROL, and the only arm that can flip the verdict, because
    # `WorldReader.read` returns 0 rather than UNKNOWN for a kind a rung does not hold, so
    # `0 >= amount` is False and the transfer REFUSES). The kind is decision-live: at `coin`
    # `transfer` leaves the executed set entirely.
    default_store_kind="grain",        # `H-121`, swept grain / salt / coin
    # ⚠ `0` IS THE CONTROL AND IT IS SWEPT FIRST. Nothing is spent, so scarcity never binds and
    # `stores >= 0` admits every giver: a run at this point shows how much of the transfer
    # behaviour rests on the default rather than on the world.
    default_transfer_amount=1,         # `H-94`, swept 0 / 1 / 3
    # v9 IN-33 (`H-58`), restored at v10 REM-2B [ASSUMPTION; medium; Jordan to correct]. THE MATTER KIND AN
    # `exchange` RECEIVES IN RETURN (`return_kind`). The design names an exchange's two sides and supplies no
    # kind for the second, so it is `default_store_kind`'s shape: declare, default, sweep.
    # `return_amount` takes `default_transfer_amount` above (one unit back per default unit given),
    # so no second new fixture. `salt` because it is a STOCKED kind other than `kind`'s default
    # (`rosters.yaml: site_yield`: harbours yield grain and salt). ARMS: `salt` (shipped) · `timber` (the
    # other stocked family, a seam's) · `coin` (THE CONTROL: registered, produced by no site and held by no
    # rung, so the second side reads 0 and every exchange refuses). REVERT: delete this fixture with IN-33.
    default_return_kind="salt",        # `H-58`, swept salt / timber / coin
    # v10 CR-23 / `H-243` (M17 taken (a), [ASSUMPTION; medium; Jordan to correct; revert: `off`]): WHEN A
    # LARDER'S STOCK REACHES THE SEATS OVER IT. MATTER's last actorless `stores` write to a rung in the
    # barrier carries `(rung, "stores:<default_store_kind>", units after)` -- at `crossing` only when
    # `world_q.requisitionable` flips across the barrier, at `season` on every such write, at `off` never
    # (the CONTROL: every content hash is the tree's before CR-23). The arms are `rosters.yaml:
    # stock_reports`; the reader is `loop/matter.py`. Injection site: this line.
    stock_report="crossing",           # `H-243`, swept crossing / season / off
    # ⚠ ITEM 3b. HOW MUCH BODY ONE UNIT OF UNMET SUBSISTENCE COSTS. `AX-5` names three
    # self-motions and BODIES IS THE ONE WITH NO WRITER; `04 §A.3.3` asks for the shortfall to
    # reach `Person.body` through the gate, and the write matrix licenses `(Person, body)` at
    # `[MAT, RES]` already. What no document supplies is the MAGNITUDE — #353 rules that a body
    # falls, never by how much — so this is declared, defaulted and swept rather than chosen
    # inside a body, which is `H-80`'s shape exactly.
    #
    # ⚠ `0` IS THE CONTROL AND IT IS THE PRE-3b TREE EXACTLY: no body moves, no band is crossed,
    # and every reading of the corpus is identical to the day before this landed. That is what
    # makes the sweep able to flip a verdict rather than merely vary a number.
    #
    # ⚠ THE ARMS ARE CHOSEN AGAINST THE BAND TABLE, NOT PICKED. `condition_scale` is 1000 and
    # `band_floors["body"]` is `{full_operations: 800, limited: 500, withdrawal_only: 100}`, so a
    # person must lose 201 to cross the first floor. At the populated world's measured shortfall
    # of 3 units per eater per season: `0` never crosses · `10` crosses `full_operations` in 7
    # seasons · `67` crosses it in one. The three arms therefore bracket the question the number
    # actually decides — IS STARVATION A SEASON OR A CAMPAIGN — instead of bracketing a magnitude.
    # Injection site: this line, read by `loop/matter.py`'s subsistence pass.
    # ⚠⚠ SHIPPED AT `10` (REM-52, v10, B10-05): H-125's REGISTERED LIVE ARM, TAKEN AS A DELEGATED
    # PICK (M6 taken (a)), `[ASSUMPTION; medium; Jordan to correct; revert: 0]`. THIS LINE DOES NOT
    # ARGUE THE MAGNITUDE: CR-22 (B10-18) re-derives it by `H-125`'s own test above, IS STARVATION A
    # SEASON OR A CAMPAIGN. `0` stays the CONTROL arm and the first sweep point; the readers of that
    # arm sweep this fixture back to `0` in-process
    # (`test_lb3b_the_zero_arm_is_the_pre_item_tree_exactly`). `67` stays a swept arm only.
    # ⚠ A CASE FIXTURE MODELS A SCENE AND NOT AN ECONOMY: the buildable corpus worlds hold ZERO
    # stores, so every person in a case world starves from season 1. A famine in a world with no
    # larder measures the fixture's silence, not the world's scarcity (`CLAUDE.md` §0.1 pt 2: the
    # reading cannot observe the thing it names). The corpus, the spine and `headless` hold no
    # cohort, hence no eater (H-171); read what the live arm moves in a world that stocks a larder
    # (the built realm), not in a case world.
    # v9 SE-01 (`24g`): J-6 settles the SHAPE -- a fixture, the control kept for the corpus, a
    # one-line revert. `tests/test_territorial_subsistence.py` reads `H-125`'s `sweep:` off the
    # register and runs every non-control arm on the built realm.
    body_step=10,                      # `H-125`, swept 0 (control) / 10 (SHIPPED, REM-52) / 67
    # v9 IN-34 FORCE-BODIES (#457 D2, answered [medium; Jordan to correct]: ageing and illness are in
    # scope, a HAZARD READER only, rates swept). The hazard is `world_q.body_hazard`, a Query over
    # `Person.born` (ID-13: never a stored value); MATTER's bodies pass draws against it.
    # `age_step` is the chance of death added per season of age, `illness_rate` the age-free chance
    # a season. SHIPPED DARK: both ship at 0, THE CONTROL -- no draw is taken and no body is written,
    # so the season is today's (like `body_step` above and IN-21's `season_factor_draw ()`).
    # ⚠ NONE OF THE THREE NUMBERS IS CHOSEN HERE; ALL ARE JORDAN'S TO SET (#457 D2's gate).
    # No source authors an age: `references/npc_registry.yaml` carries `age: null [GAP]`
    # on 29 of its 46 rows and no age key on 17, so `age_at_build` -- the age every person the
    # realm builds has at tick 0 (`Person.born = -age_at_build`) -- is a declared control default,
    # not a reading of any source. The tests sweep their own arms and rule on none of them.
    age_step=0.0,                      # v9 IN-34, swept 0 (control, SHIPPED) / test arms only
    illness_rate=0.0,                  # v9 IN-34, swept 0 (control, SHIPPED) / test arms only
    age_at_build=0,                    # v9 IN-34, a declared default (seasons old at tick 0)
    # v9 IN-35 FORCE-HAZARD (#457 `:123-143`): THE LATTICE COUPLING WEIGHT -- the share, on
    # `condition_scale`, of a Site's gap down to the weakest Site in its own or a bordering territory that
    # it loses PER SEASON (SEAM-CLOCK, #457 `:174`: one unit, the season), added to its kind's wear in
    # `loop/matter.py`'s wear loop. `0` is THE CONTROL, SHIPPED: the pass returns before reading any Site,
    # so the season is today's (`body_step`'s and `age_step`'s shape). In [0, condition_scale]; outside it
    # raises (`_lattice_strain`), since a share above the whole gap would overshoot the weakest neighbour.
    # [JUSTIFIED: engine/season/hole_register.yaml H-235 -- `site: Fixtures lattice_coupling`, graded `assumption`; #457 gives the coupling and no magnitude (its only rate is the retired scalar's -1 a year), so it is injected and swept 0 / 250 / 500]
    lattice_coupling=0,                # `H-235`, swept 0 (control, SHIPPED) / 250 / 500
    # `W-E` / `H-123`. HOW MUCH BODY A WOUND COSTS WHEN THE SCENE SAYS THE SUBJECT BLED AND DID
    # NOT GO DOWN. Part E's `writes:` names the CELL and never the VALUE, and no in-chain document
    # supplies this one -- so it is declared, defaulted and swept rather than chosen in a body,
    # which is what `H-114` measured the cost of (`harm` defaulted to the whole body, so a fold at
    # `Wounded` deleted the person). The default introduces NO CONSTANT: it scales the body by the
    # health fraction the ENGINE computed. `total` is the CONTROL and is the code exactly as it
    # stood before `W-E`. Injection site: this line, read by `_eff_kill`.
    wound_harm_model="scene_fraction",  # `H-123`, swept scene_fraction / total / none
    # v11 CP-T03-07 (P32): WHETHER A FIGHT LEAVES A LASTING MARK on `Person.body_ceiling`
    # (`rosters.yaml: body_mark_models`). SHIPPED LIVE at `deepest_gate`, on REM-52's precedent for a
    # harm (`body_step` above: the live arm ships, the control is one named value away)
    # [ASSUMPTION; medium; Jordan to correct; revert: none]. `none` is the control: no ceiling moves.
    # Injection site: this line, read by `loop/effects_combat.py::_eff_kill`.
    # [JUSTIFIED: engine/season/hole_register.yaml H-258 -- the gate and the ceiling walk are the CP-T03-07 home's; only whether the live arm ships is undocumented, so it is injected and swept none / deepest_gate / drawn]
    body_mark_model="deepest_gate",    # `H-258`, swept none (control) / deepest_gate (SHIPPED) / drawn (B14.23, flipped by B15)
    # B14.23 (`H-567`). THE OBSTACLE OF THE LASTING MARK'S ROLL, read only under `body_mark_model` `drawn`: a survivor at his limit rolls once
    # (`loop/effects_combat.py::_marks`, the one pool rule on the untrained default, his body band entering as levels through the `wounds` source,
    # the one sampler) and the net meets this obstacle on the one ladder. Fractional like every obstacle (A-5); under `deepest_gate` and `none`
    # it is read by nothing. The seed value is the even line of a pool of `pool_add` dice (`sigma_leverage.even_line`, 0.4 a die); B15 sets it with the flip.
    # [ASSUMPTION; medium; Jordan to correct; revert: `body_mark_model: deepest_gate`, which reads no obstacle]
    # [JUSTIFIED: engine/season/hole_register.yaml H-567 -- `site: Fixtures mark_ob`, graded `assumption`; no document gives how hard it is to mend clean at one's limit, so it is injected and swept 1.2 / 2.4 / 4.8]
    mark_ob=2.4,                       # `H-567`, swept 1.2 / 2.4 (seed value, read only under `drawn`) / 4.8
    # B15.06 (`H-574`). HOW HARD A FELLED BODY IS TO KILL, per cause: the obstacle `queries/world_q.py::mortal_terms` answers for `death`,
    # `yield` and `blood` (PHY_A A3's three terms; `spell` has none until B37). Fractional like every obstacle (A-5). Shipped at B15.06 at an
    # unreachable control, 99.0 a cause (PC_A's "an obstacle no pool can beat"), under which every felled body dies as before the draw. B15.07's
    # sweep (0..4 a cause, 1,000 felled parties a cell, `H-574`) SETS THE SHIPPED VALUES: a felling under `death` terms is a death about half the
    # time, one whole obstacle step less lethal a term down the terms' intent (`yield`, then `blood`), on the one sampler and pool the mark roll takes.
    # [ASSUMPTION; medium; Jordan to correct (D-19, in the PR body); revert: 99.0 a cause, the control]
    # [JUSTIFIED: engine/season/hole_register.yaml H-574 -- `site: Fixtures mortal_wound_ob`, graded `assumption`; no document gives how hard a felled body is to kill, so it is injected and swept]
    mortal_wound_ob={_c: _v for _c, _v in (("death", 3.0), ("yield", 2.0), ("blood", 1.0)) if _c in MORTAL_CAUSES},   # `H-574`, swept 99.0 (control) / 0..4 a cause; death 3 / yield 2 / blood 1 SHIPPED (B15.07)
    # `H-184` (split out of `H-98`). WHERE THE `Wounded` BAND STARTS: the threshold `wounds` must be
    # strictly above for a standing subject to read `Wounded` rather than `Untouched`. The edge is
    # `rosters.yaml: combat_band_edges` and `None` MEANS ITS VALUE (`0`, any wound), so the number is
    # authored once -- `field_walls_dr`'s precedent, and for its reason: a literal `0` here would be a
    # second copy that drifts the day the roster is edited. An int, or the NAME of a
    # `wound_quantities` member, overrides it. Injection site: this line, read by
    # `seam/ladder.py::degree_of` -> `combat_degree`, handed the world's fixtures by `loop/resolve.py`.
    # Only this edge is swept; the `Felled` edge is the engine's own verdict and re-deciding it would
    # re-decide who went down (Jordan 2026-09-04: *the combat engine determines the result there*).
    # [JUSTIFIED: engine/season/hole_register.yaml H-184 -- where the Wounded band starts; the ruling reads the band off the scene and the engine does not separate a decisive win from a narrow one beyond wound count, so the threshold is injected and swept 0 (= None, SHIPPED) / 1 / max_wounds]
    combat_wounded_above=None,         # `H-184`, swept 0 (= None, SHIPPED) / 1 / max_wounds
    # M4 (`ED-IN-0279` clause (a)). `H-148`'s question asked of mass_battle's own result instead
    # of a scene's `WoundTracker` -- HOW MUCH `Person.body` A LOST FIELD COSTS. `total`/`none` are
    # the same two controls `wound_harm_model` ships above, for the same reason. Injection site:
    # this line, read by `_eff_march` (`loop/effects.py`). The default is settled
    # by `wound_harm_model`'s own precedent (Jordan, 2026-09-04: *"the combat engine determines
    # the result there"*) applied to this magnitude too (`rosters.yaml`'s `field_casualty_models`
    # note).
    # ⚠ NOT YET REGISTERED ON `hole_register.yaml`'s `site:` column, with
    # `field_morale_weight`/`field_grudge_weight` below.
    field_casualty_model="scaled_by_degree",  # `H-148`, swept scaled_by_degree / total / none
    # `H-148`, second half: HOW MUCH `Person.stance` A LOST FIELD MOVES against the winning
    # faction (the grudge) and against the loser's own creed (the morale hit) -- one weight for
    # each, on the ruled shape `(referent, valence, weight)` `queries/person_q.py::stance_toward`
    # already sums. #353 states neither the referent's valence sign nor its magnitude; declared,
    # defaulted and swept rather than chosen in a body. Injection site and register row: as
    # `field_casualty_model` above, deferred to the same reader.
    field_morale_weight=1,   # `H-148`, swept 0 / 1 / 3
    field_grudge_weight=1,   # `H-148`, swept 0 / 1 / 3
    # MB-03 (`ED-MB-0078`'s superseding row: d.1's *"faction state sets the morale baseline"*, option
    # (b)). HOW HARD A SIDE'S BUILD-TIME LOYALTY ROW MOVES ITS STARTING MORALE: the side's weight-mean
    # stance toward its faction creed's utterer (`data/cast.py::stance_from_loyalty`'s row, -5..+5,
    # read by `seam/wrappers/mass_battle.py`) is added to `massbattle._morale_start` at this gain. `0`
    # IS THE CONTROL AND IS SHIPPED: battle history only, option (a), the field as it was. The arms,
    # each derived and none tuned: `0.4` = (Morale ceiling 7 - base 5) / the row's bound 5, the gain
    # at which the bound lands exactly ON the ceiling -- and since `massbattle._morale_start` rounds
    # half-up, a side of loyalty >= 3.75 already starts at 7 at 0.4 (5 + 0.4 * 4.0 = 6.6 -> 7; at
    # `build_realm(0)` every creed-holding faction fields at least one such side); `1` = the 1:1 unit
    # `_morale_start` already gives the morale row (and the row's own reading, 2026-10-01). A fielded
    # SIDE reads its own members' mean, and a low-loyalty side does not saturate
    # (`test_mass_battle_d1_morale_baseline.py`'s pinned rows). Injection site: this line, read by
    # `seam/wrappers/mass_battle.py::field_input` into the record's `loyalty_gain`.
    field_morale_loyalty_gain=0,  # `H-148`, swept 0 (control, SHIPPED) / 0.4 / 1
    # `H-150`. THE DEFENDER DR A WALLED FIELD ADDS -- A.9's one Walls number,
    # applied 1:1 to the engine's own `Army.dr` (an ASSUMPTION about the unit, which is why it is
    # swept). `None` (the flat row, the control since B17.01 shipped `3`) MEANS A.9's NUMBER, NOT "NO WALLS": `engine/` cannot name
    # `systems/`, so the 3 stays authored once, at `terrain.WALLS_DEFENDER_DR`, and the engine reads it
    # when this is `None` -- a literal 3 here would be a second copy that drifts the day A.9 is
    # re-ruled (B17.01 nonetheless ships the spelled-out `3` below, plan-ordered, and the retired `test_cp_t04_05_graded_walls` pinned it equal to that owner). An int overrides it for the season: `3` spells A.9's number out (it reproduces `None`
    # at fort_level 1.0; CP-T04-05 grades it `int(3 * fort_level)` below that, `None` stays binary), `0` is the CONTROL (the only live
    # difference between a walled and an open field removed), `1` the middle arm. Injection site: this
    # line, read by `seam/wrappers/mass_battle.py::field_input` into the record's `walls_dr` (`31c`).
    # B17.01 SHIPS `3`, A.9's number spelled out: with CP-T04-05's scaling it is the archived table's +3 at a full garrison and
    # proportionally less below, and `None`, the flat row, stays in the sweep as the control.
    field_walls_dr=3,     # [JUSTIFIED: B17.01 -- A.9's Walls DR scaled by the garrison's condition (CP-T04-05), the archived table's +3 at a full garrison; H-308 graded as shipped] `H-150`, swept 3 (A.9, SHIPPED) / 0 (control) / 1 / None (the flat row, control)
    # CP-T04-01 (`H-359`). WHAT A HEADCOUNT SIDE IS MADE OF: `person` IS SHIPPED (B17.01) -- one subunit per commanding
    # person, sized by `under_arms_cap` of his own weight, and `_eff_march` scales each side's person by HIS subunit's ratio
    # and names, on the band Event, the person whose subunit broke first. `side` is the control: one subunit sized by the
    # side's Σ weight, every body of the side scaled by the SIDE's survivor ratio. A side that holds an order of battle, or
    # faces one, is unchanged by either value. Injection site: this line, read by
    # `seam/wrappers/mass_battle.py::field_input` into the record's `units`; the module refuses any other string.
    field_units="person",  # `H-359`, swept person (SHIPPED) / side (control) [JUSTIFIED: B17.01 -- a field is fought by the persons who command it, each scaled by his own subunit; H-359 default shipped]
    # CR-24 (`H-360`). WHAT A FOUGHT FIELD COSTS THE WINNER: `engine` IS SHIPPED -- each winner's `body` is scaled by his own
    # side's (or, under `field_units: person`, his own subunit's) survivor ratio from the engine's result, `body` ONLY: a
    # winner earns no stance row (no grudge, no morale hit) and is never in `touched`. `off` is the field as it was (the
    # winner is not written), and is the control. Read by `loop/effects_combat.py::_eff_march`, which refuses any other
    # string (`rosters.yaml` `field_winner_casualty_arms`).
    field_winner_casualties="engine",  # `H-360`, swept off (control) / engine (SHIPPED)
    # v9 IN-52 (`H-241`). THE LEVY-TO-FIELD FEED'S ARM [ASSUMPTION LF-1..LF-3, delegated-ruled,
    # `_part5` §J.2]: `True` bounds each side's fielded troops by its treasury at the larder's ration
    # (`modules/settlements/provision.py`) and debits what the field eats (`_eff_march`); `False` is the
    # CONTROL, SHIPPED -- every field is Σ weight, as before the feed. The flip ON is its own declared
    # hash-moving commit. Injection site: this line, read by `seam/wrappers/mass_battle.py::provision_input`.
    field_provisioning=False,  # `H-241`, swept False (control, SHIPPED) / True / True on empty treasuries
    # IN-08 H3 (`ED-IN-0261`'s scar model). The scar is a COUNT per pursuit, one per observer per
    # violated pursuit (`loop/resolve.py::_scar_witnesses`), so it has no magnitude to sweep. What IS open is WHETHER THE ACTOR COUNTS AS AN OBSERVER OF
    # HIS OWN ACT, and that is this arm. Injection site: this line, read by `_scar_witnesses`.
    # `False` -- the actor is scarred exactly when `epistemic.observers_for` admits him, like anyone
    # else (no actor rule at all; under `all_five` the witness-key channel admits the actor, under
    # `presence_only` only if he stands where the act happened). `True` -- the actor is never
    # scarred by his own act. ⚠ THE CONTROL IS NOT "TODAY'S BEHAVIOUR": the mechanism changed shape
    # at H3 (participant float -> observer count), so no arm reproduces the pre-H3 tree. `False`
    # is shipped as the arm that ADDS NO RULE to `observers_for`'s answer.
    # [JUSTIFIED: engine/season/hole_register.yaml H-128 -- the moral-wound row; ED-IN-0261 rules the unit (a count) and the trigger (witnessing) and leaves the actor's own standing as a witness unstated, so it is swept]
    scar_excludes_actor=False,         # `H-128`, swept False (SHIPPED, no actor rule) / True
    # IN-08 H9 / `ED-IN-0261`'s threshold 2 (*"WEIGHT SHIFTS, others gain proportionally"*): THE
    # FRACTION OF A PURSUIT'S WEIGHT A PERSON GIVES UP ONCE THEIR SCAR COUNT ON IT REACHES 2, shared
    # among their other held pursuits in proportion to those weights (total weight conserved).
    # Injection site: this line, read by `decision/choose.py`'s `make_chooser` -> `options.project`
    # -> `queries/person_q.py::crisis_weights`. A READER: it writes nothing and `Person.pursuits`
    # is untouched. `0` is the CONTROL and is SHIPPED [ASSUMPTION]: the plan names the arm "control
    # `0`, swept" and is silent on shipping it ON, and a non-zero value moves every outcome, so
    # arming it is a design choice (the sign test that feeds the counts is itself a candidate
    # reading; see `H-128`). At `0` the chooser reads `p.pursuits` itself, so the hash and the
    # fork divergence are those of the tree without the arm.
    # [JUSTIFIED: engine/season/hole_register.yaml H-187 -- the threshold-2 weight shift; ED-IN-0261 rules THAT the weight shifts and the others gain proportionally, and states no magnitude]
    scar_weight_shift=0,               # `H-187`, swept 0 (control, SHIPPED) / 0.5 / 1
    # IN-08 6f: HOW HARD RELIGIOUS STRAIN DAMPS A PERSON'S PURSUIT PULL. `make_chooser` reads the
    # pursuit dot at `1 / (1 + k * confliction(p))` (`queries/person_q.py::confliction`, the derived
    # Query 6f is the caller of). Injection site: this line, read by `decision/choose.py`'s
    # `make_chooser`. `0` is the CONTROL and is SHIPPED [ASSUMPTION]: the plan names 6f as the
    # Query's caller and states neither the form nor shipping it on; at `0` the factor is exactly
    # 1.0. Must be >= 0 (a negative `k` could invert the pull or divide by zero; `make_chooser` raises).
    # [JUSTIFIED: engine/season/hole_register.yaml H-188 -- the confliction term; ED-IN-0251 R1 rules confliction derived and states no effect on the score]
    confliction_weight=0,              # `H-188`, swept 0 (control, SHIPPED) / 0.2 / 1
    # v9 IN-23 (CARRY-STABILITY, ruling R7): HOW MANY SEASONS OF HIS OWN LEDGER A PERSON'S ESTIMATE
    # OF A HOLDER'S LEGITIMACY OR A RUNG'S STABILITY READS (`queries/person_q.py::recent_claims`,
    # anchored on his newest claim). 20 is `confidence_default` / `claim_decay_per_season`, 100 / 5
    # (H-09, H-40): the seasons an unrefreshed claim takes to decay to confidence 0, so the window
    # holds every claim the decay clock still credits and drops none it does [ASSUMPTION; medium;
    # Jordan to correct]. A whole number >= 1; `recent_claims` raises on anything else.
    # Injection site: this line, read by `harness/storybar.py::estimates` (the STORY-BAR instrument,
    # the Queries' only reader; no chooser reads it).
    # [JUSTIFIED: engine/season/hole_register.yaml H-224 -- R7 rules the estimate a windowed read over the person's own ledger and gives no window; 20 is derived from the H-09 / H-40 constants, swept 1 / 4 / 20; read by the STORY-BAR instrument only]
    estimate_window_seasons=20,        # `H-224`, swept 1 / 4 / 20 (SHIPPED)
    # `H-146` / `ED-IN-0261`. WHICH `pursuit_axes` MEMBER GATES `opening_set` -- deontology as a
    # REFUSAL, read by `decision/options.py::opening_set`. The axis NAME is ruled (`deontological`, the
    # NEG pole of `deontological/instrumental`) and the THRESHOLD is the person's own projected
    # weight, so there is no magnitude here to sweep. `None` is the CONTROL and is SHIPPED, but NOT
    # because no matching axis exists today -- a `layer-conformance` attack (2026-09-27) found that
    # `deontological_instrumental` (`references/descriptor_registry.yaml:179`, negative = the
    # deontological pole) WOULD arm this gate on the 15x7 basis. `None` is shipped because arming it
    # is an unruled design choice, not because the axis is unavailable -- `H6` has landed (IN-08);
    # arming waits on G-3's ruling (H-146 unarmed), not on this row.
    refusal_axis=None,                 # `H-146`, control None (SHIPPED)
    # `H-475` (B10.25; `16_PESSIMIST_CHAR_C` "The resolution, decided" 4, A-24). HOW SURELY A SCRUPLE STOPS A MAN: `decision/choose.py::make_ranker` strikes a candidate whose
    # `options.scruple` margin is positive; at `0` that is the THRESHOLD (every positive margin is struck, today's gate) and at `T > 0` the candidate is struck with probability
    # `1 - exp(-margin / T)` on the person's own draw `scruple:<verb>:<subject>`, so a large margin stops him nearly always and never certainly and a small one usually gives way.
    # `0` is the CONTROL and SHIPS; the gate is armed nowhere (`refusal_axis` None); B10.32 read the arming (H-146, H-475) and did NOT ship it: `0.2` is B98's, after BA1's cells. Must be >= 0. [ASSUMPTION; medium; Jordan to correct; revert: 0, the threshold.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-475 -- site: Fixtures scruple_temperature, graded `assumption`; the proposal's own gate arm is 0.2 and Jordan gave no value, so it is injected at the control and swept 0 / 0.1 / 0.2 / 0.4]
    scruple_temperature=0.0,           # `H-475`, swept 0 (control, SHIPPED) / 0.1 / 0.2 (the arm B10.32 read and did not ship) / 0.4
    # `H-153` (D-6, `19_PLAN.md:952-955`) -- THE ONE CORPUS FAULT THAT DOES NOT RECONCILE WITH
    # FAIL-FORWARD: *"whoever touches it is killed"* has no corpus-supplied next move. Swept
    # fixture, in the `H-128` shape: nothing reads it (the speech-kind resolution ladder this
    # would gate is not built), so the control arm changes no behaviour. `"removal"` is shipped -- the design's own two options are *"treat it as
    # the one place the ladder's failure is not the outcome -- the outcome is removal from the
    # world, which is a different contest entirely"* or *"soften the corpus."* D-6 itself: *"Handed
    # forward unsoftened."* Softening a corpus figure this position did not author is the invented
    # direction; the unsoftened reading is the one the source states, so it is the default rather
    # than a coin flip. [JUSTIFIED: engine/season/hole_register.yaml H-153 -- swept fixture, not Jordan's, `18`/PROC-A part 4]
    speech_kind_terminal_fault="removal",   # `H-153`, swept removal (control, SHIPPED) / softened
    # `H-154` (D-7 branch a, `19_PLAN.md:957`) -- WHETHER A DETAILED DENIAL OUTPERFORMS A BRIEF
    # ONE. *"Data authoring, per branch, low stakes, sweepable either way."* `"equal"` is the
    # control: the reading under which the resolution ladder (unbuilt, same reason as `H-153`
    # above) draws no distinction between the two, so shipping it changes nothing today.
    # [JUSTIFIED: engine/season/hole_register.yaml H-154 -- swept fixture, not Jordan's, `18`/PROC-A part 4]
    denial_detail_outperforms="equal",      # `H-154`, swept equal (control, SHIPPED) / detailed / brief
    # `H-154`'s second branch (D-7 branch b) -- WHETHER DISPLAYED ANGER EXTRACTS CONCESSIONS, and
    # *"the study marks the evidence for the second unverified itself"* -- the weakest-warranted
    # branch in this position's whole set. `False` is the control (no extraction effect), matching
    # `H-128`'s neutral-start convention; nothing reads it today for the same reason as above.
    displayed_anger_extracts_concessions=False,   # `H-154`, swept False (control, SHIPPED) / True
    # `H-155` (r2 `02_THE_WRIT_AND_THE_WORD.md` §A.10.2, `ED-IN-0222`). HOW
    # FAR A RUMOUR MAY DRIFT A BARE NUMBER at `Partial`. r2's own words give the fixture its
    # licence on `default_transfer_amount`'s precedent (`:432-436` above): "direction ruled,
    # magnitude open, is exactly a fixture." `0` is the CONTROL -- `_told_value`'s drift branch
    # reads `math.ceil(band * abs(before))` and a `0` band makes that `0`, so no draw can ever
    # clear the `max_delta < 1` floor and the branch is a verbatim no-op, reproducing the
    # pre-15b told channel exactly for a numeric claim. Shipped at `0.5`, not the control: unlike
    # `body_step` (H-125), this magnitude scales PROPORTIONALLY to whatever the claim already
    # carries rather than adding an absolute quantity into an economy the corpus may not stock, so
    # the "famine with no larder" hazard that forced `body_step` to the control does not apply
    # here, and the mechanism's own falsifier (§A.10's OBSERVABLE) asks for a telling that is
    # actually lossy at `Partial`, not one parked inert pending a later ruling.
    # [JUSTIFIED: engine/season/hole_register.yaml H-155 -- the drift band; r2 states the direction and leaves the magnitude, and the sweep brackets no-drift / shipped / aggressive]
    told_drift_band=0.5,               # `H-155`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # v12 B11.55 (`16_PESSIMIST_SC_E` edit 1, C3-K1): A HEARER WHO HOLDS THE FIGURE FIRSTHAND HEARS IT AS HE HOLDS IT at a `Partial` telling of an amount, instead of the drifted copy (`loop/witness.py::_told_value`). A switch, not
    # a number: `True` SHIPS (an honest teller's partial telling no longer lowers a knower's `record` of him), `False` is the control, today's drifted copy.
    # [JUSTIFIED: engine/season/hole_register.yaml H-155 -- the told channel's numeric loss; the telling that reaches a firsthand holder is the one case the copy has a figure to be measured against, swept True (SHIPPED) / False (the control)]
    knower_hears_true=True,            # `H-155`, swept False (control) / True (SHIPPED)
    # `H-177`..`H-179` (telling workplan `T3a`, `ED-IN-0282`; `RULINGS.yaml` CAT-3, closed: store
    # the teller, grade the claim WHEN READ by the hearer's relation to them). HOW MUCH A HEARER
    # CREDITS A CLAIM SOMEONE TOLD THEM, read by `queries/person_q.py::teller_weight` -- the `weigh`
    # `LedgerReader` ranks a person's own claims by in `belief_contradicts`. A told claim weighs
    # `clamp01(told_weight ** hops * relation * record)`, `relation = 1 + rank_gain*rank +
    # regard_gain*clamp(regard/STANCE_MAX, -1, 1)`, `record` = `H-183`'s factor below. CONTROL
    # FIRST: at `told_weight` 1.0 and every gain 0 every claim weighs exactly 1.0 and the reader
    # orders as it did before `T3a` -- the realm hash and `corpus_run 0` are byte-identical there.
    # SHIPPED: `told_weight` 0.5, so, while `rank` reads 0 (`H-181`) AND `record` is neutral (the
    # teller has no checkable record, or `record_gain` is 0), one hop of hearsay reaches at most
    # 0.5 x 1.5 = 0.75 and never outranks the hearer's own firsthand claim by being newer. At
    # NEUTRAL regard a good record ALONE gives 0.5 x 1 x 1.5 = 0.75 (< 1); 1.0 needs `relation` x
    # `record` >= 2, i.e. `relation` >= 4/3 (regard >= 2/3 of STANCE_MAX) at the best record. Gains 0.5
    # [ASSUMPTION], which at the extremes moves a told claim's weight by half either way. Read
    # only on a claim that names a teller.
    # [JUSTIFIED: engine/season/hole_register.yaml H-177 -- the hearsay discount; CAT-3 rules THAT a told claim is graded when read and gives no magnitude, so it is injected and swept 1.0 / 0.5 / 0.25]
    told_weight=0.5,                   # `H-177`, swept 1.0 (control, WITH the three gains 0) / 0.5 (SHIPPED) / 0.25
    # [JUSTIFIED: engine/season/hole_register.yaml H-178 -- rank's gain on a teller's weight; CAT-3 orders lord > peer, no magnitude; DORMANT while `rank` reads 0 (H-181)]
    rank_gain=0.5,                     # `H-178`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # [JUSTIFIED: engine/season/hole_register.yaml H-179 -- regard's gain on a teller's weight; CAT-3 orders peer > enemy, no magnitude, so it is injected and swept 0 / 0.5 / 1.0]
    regard_gain=0.5,                   # `H-179`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # `H-183` (telling workplan `T6`, `ED-IN-0282`). HOW FAR A TELLER'S RECORD MOVES THE WEIGHT OF
    # THEIR HEARSAY: `record = 1 + record_gain * (agree - dis) / (agree + dis)` over the hearer's
    # claims that teller passed on, each paired with the hearer's OWN firsthand claim on the same
    # `(subject, predicate)` (`queries/person_q.py::record`); no pair is exactly 1.0, neutral.
    # `0` is the CONTROL: `record` is 1.0 whatever the ledger holds, so every weight is its pre-`T6`
    # value. Shipped `0.5` [ASSUMPTION]: a teller who was always right weighs half again as much as
    # a stranger, one who was always wrong half as much.
    # [JUSTIFIED: engine/season/hole_register.yaml H-183 -- record's gain on a teller's weight; no document gives the gain, so it is injected and swept 0 / 0.5 / 1.0]
    record_gain=0.5,                   # `H-183`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # `H-180` (B10.63; `02_CHAR_relations_have_a_ground` edit 5). HOW MUCH LESS A HEARER CREDITS A CLAIM ABOUT A MAN TOLD HIM BY THAT MAN'S RIVAL:
    # `teller_weight` multiplies by `clamp(1 - rival_gain, 0, 1)` when the hearer holds the teller's own `bond:rivalry` claim on the claim's
    # subject, told to him (`chain[0]` the teller). `0` is the CONTROL and is SHIPPED [ASSUMPTION], so every claim weighs what it weighed before.
    # [JUSTIFIED: engine/season/hole_register.yaml H-180 -- the discount on a rival's report; no document states the magnitude, so it is injected at the control and swept 0 / 0.5 / 1.0]
    rival_gain=0.0,                    # `H-180`, swept 0 (control, SHIPPED) / 0.5 / 1.0
    # `H-190` (telling `T7`, G9 declared intent; v9 IN-16, `ED-IN-0282`). HOW OFTEN A TELLER DECLARES
    # AN INTENT: the chance that a telling whose teller has CHOSEN a later act naming the telling's
    # topic (in a later scene of the same `choose` return) passes on that intent instead of what the
    # teller holds about the topic (`decision/choose.py::declare_intents`, one keyed draw per telling).
    # `0` is the CONTROL and is SHIPPED [ASSUMPTION], on `H-187`/`H-188`'s precedent: the plan names
    # "control 0" and is silent on shipping it on, and a non-zero value moves the realm's outcome.
    # At 0 no draw is taken and no `said` is touched, so the season is the pre-`T7` tree exactly.
    # [JUSTIFIED: engine/season/hole_register.yaml H-190 -- the disclosure rate; no document gives how often a person tells what they mean to do, so it is injected and swept 0 / 0.5 / 1.0]
    intent_disclosure=0.0,             # `H-190`, swept 0 (control, SHIPPED) / 0.5 / 1.0
    # `H-192`, `H-193` (v9 IN-18 `G1`, judged regard; `ED-IN-0282`). HOW FAR WHAT A PERSON MAKES OF
    # ANOTHER'S DEEDS MOVES THEIR REGARD FOR THEM: `queries/person_q.py::regard` = stored stance +
    # `judged_gain` x the deeds they hold firsthand + `told_valence_gain` x the deeds they were
    # told, each deed scored by the holder's own pursuits against the deed's alignment
    # (`deeds_judged`). `0` is the CONTROL. SHIPPED LIVE at the sweep's midpoint 0.5 for both, per
    # Jordan's ruling of 2026-10-09 (B-E): *"Gains are improvements and therefore ship."* [ASSUMPTION;
    # medium; Jordan to correct; revert: set both back to 0.0 (the control)] -- the ruling ships the
    # gain and names no magnitude. A live gain can move the realm (`teller_weight`'s `relation` reads
    # regard; seed 0 measured unmoved, H-192). At 0 `regard` reads no ledger and is the stored half exactly. Separate from
    # `regard_gain` (`H-179`): see `regard`'s docstring.
    # [JUSTIFIED: engine/season/hole_register.yaml H-192 -- the judged half's gain; no document gives how much a witnessed deed moves regard, so it is injected and swept 0 / 0.5 / 1.0; shipped live at 0.5 per Jordan's 2026-10-09 ruling]
    judged_gain=0.5,                   # `H-192`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # [JUSTIFIED: engine/season/hole_register.yaml H-193 -- the told half's gain; no document gives how much a deed one was told of moves regard, so it is injected and swept 0 / 0.5 / 1.0; shipped live at 0.5 per Jordan's 2026-10-09 ruling]
    told_valence_gain=0.5,             # `H-193`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # `H-194` (v9 IN-18 `G2`, polarity in §F2 term 2). WHICH WAY REGARD FOR AN ACT'S SUBJECT PULLS
    # ON IT: `legacy` adds `stance_toward(p, subject)` to every candidate (the pre-G2 term);
    # `declared` adds G1's `regard` and negates it where the subject is the act's OPPONENT, so a
    # grudge makes `fight` on its object score higher (`decision/choose.py::stance_term`;
    # `rosters.yaml: stance_polarities`). `declared` is SHIPPED by CR-16 (v10, B10-07b)
    # [ASSUMPTION; medium; Jordan to correct; revert: set this back to "legacy" (re-pin what CR-16 re-recorded: the
    # seeded goldens, the `test_season_shape` figures, `test_sc01_the_bar`'s proceedings, `test_h9`'s seed); the
    # `subject_is_opponent` repair need not revert]: the sign is derived from the row's own columns
    # and IN-25's gain (`stance_gain`, below) is inert at `legacy`. `legacy` is the CONTROL, the
    # pre-G2 term verbatim, and stays selectable.
    # [JUSTIFIED: engine/season/hole_register.yaml H-194 -- the polarity arm; §F2 gives the term and no sign by role, so the readings are declared and swept legacy / regard / declared]
    stance_polarity="declared",        # `H-194`, swept legacy (control) / regard / declared (SHIPPED, CR-16)
    # `H-248` (v10 CR-17; M1, AQ-X1 (b)). WHETHER A PERSON'S CHANCE OF SUCCEEDING ENTERS THE RANKING: the pursuit term of
    # a CONTESTED candidate is multiplied by the person's own believed chance of the bands that write what the
    # term prices (`decision/choose.py::odds_weight`; the chance is `seam/wrappers/sigma.py::believed_chance`, CP-T01-03's
    # mode (b), handed to the chooser on `View.odds`). `none` is the CONTROL: the term as it stood before CR-17.
    # `believed` leaves a candidate alone where the person cannot say (`None`), where the verb contests nothing, and
    # where it writes in no band. [ASSUMPTION; medium; Jordan to correct; revert: `odds_weighting` `none`, one re-pin]
    # [JUSTIFIED: engine/season/hole_register.yaml H-248 -- `site: Fixtures odds_weighting`, graded `assumption`; whether and how a believed chance weighs a contested choice is no document's (AQ-X1 (b) is taken, M1), so the arm is declared and swept none (the control) / believed]
    odds_weighting="believed",         # `H-248`, swept none (control) / believed (SHIPPED, CR-17)
    # B05.62 (`10_DICE_believed_odds_have_a_prior` Edit B; `H-435`). WHAT A PERSON ASSUMES OF AN OPPONENT HE HOLDS NO CLAIM ABOUT, read ONLY by
    # `seam/wrappers/sigma.py::believed_input`: `ordinary` -- he takes the unheld for an ordinary person (the untrained skill score and the attribute
    # scale's mid-point, as a dealt roll against a person holding nothing composes them) and takes his stance toward the actor as neutral, so he
    # gets a figure; `none` is the CONTROL: he cannot say (`None`, which `odds_weight` reads as 1.0, certainty). His own guess, never a read of the World.
    # [ASSUMPTION; medium; Jordan to correct; revert: `none`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-435 -- `site: Fixtures believed_prior`, graded `assumption`; what a person takes an unknown opponent to be is no document's, so it is injected and swept none (the control) / ordinary]
    believed_prior="ordinary",         # `H-435`, swept none (control) / ordinary (SHIPPED, B05.62)
    # CP-T01-05, THE NPC HALF (B10-10; `H-249`). WHETHER THE COMPUTED CHOOSER MAY FORM AN `effort` ACT: for a contested
    # candidate a believed chance can price, `decision/choose.py::settle_efforts` scores the effort variants by the same
    # score (the pursuit term weighted by his believed chance, `odds_weighting`) and nets off the acts the extra slots
    # displace; `off` is the CONTROL, the chooser as it stood. [ASSUMPTION; medium; Jordan to correct; revert: `off`, one re-pin]
    # [JUSTIFIED: engine/season/hole_register.yaml H-249 -- `site: Fixtures npc_effort`, graded `assumption`; whether and how a person spends a scene on one roll is no document's (the plan is silent on the rule), so the arm is declared and swept off (the control) / on]
    npc_effort="on",                   # `H-249`, swept off (control) / on (SHIPPED, CP-T01-05 NPC half)
    # CP-T03-05 (`H-251`). HOW MANY FIGHTS THE PLAYER'S ODDS DISPLAY SAMPLES: `seam/wrappers/combat.py::fight_estimate`
    # runs the combat module this many times on a private rng and shows the shares. A DISPLAY SIZE, read by no loop
    # caller, so it moves no decision and no draw. A whole number >= 1; anything else raises in the reader. 400
    # keeps a share's standard error at or under 0.025 (0.5 / sqrt(400)). Shared with CP-T04-08's `field_estimate`.
    # [JUSTIFIED: engine/season/hole_register.yaml H-251 -- `site: Fixtures estimate_samples`, graded `assumption`; no document gives the sample size of a shown figure, so it is injected and swept 100 / 400 / 1600]
    estimate_samples=400,              # `H-251`, swept 100 / 400 (SHIPPED, CP-T03-05) / 1600
    # B14.24 (`H-568`). HOW MANY FIGHTS A PERSON'S BELIEF ABOUT A FIGHT SAMPLES: `seam/wrappers/sigma.py::believed_chance` on a row whose prize
    # binds `personal_combat` runs `combat.fight_estimate` this many times, on the believer's own picture of his opponent and the private
    # stream keyed `estimate.fight`. A BELIEF IS NOT A MEASUREMENT: a person weighing a fight runs it in his head a few dozen times, not the
    # display's `estimate_samples`, which a player reads as the odds. A whole number >= 1; anything else raises in the reader (`_estimate.samples_of`).
    # [ASSUMPTION; medium; Jordan to correct; revert: set it to `estimate_samples`' value, one re-pin]
    # [JUSTIFIED: engine/season/hole_register.yaml H-568 -- `site: Fixtures believed_fight_samples`, graded `assumption`; no document gives how often a person runs a fight in his head, so it is injected and swept 30 / 60 / 400]
    believed_fight_samples=60,         # `H-568`, swept 30 / 60 (SHIPPED, B14.24) / 400
    # `H-202` (v9 IN-25, BOUND-STAKES). HOW HARD §F2's STANCE TERM PULLS ON A CHOICE: the term
    # `stance_polarity` signs is read at `1 + this` (`decision/choose.py::stance_term`), so a grudge
    # or a judged deed outweighs a person's pursuits sooner as it rises. §F2 weights the term 1 and
    # states no gain, so this is the weight above §F2's; swept beside `field_morale_weight`/
    # `field_grudge_weight` (`H-148`), which set how much stance a lost field WRITES while this sets
    # how much the written stance WEIGHS. `0` is the CONTROL: the term is the pre-IN-25 one exactly.
    # SHIPPED LIVE at the sweep's middle arm 1 (the term at twice §F2's weight), per Jordan's ruling
    # of 2026-10-09 (B-E): *"Gains are improvements and therefore ship."* [ASSUMPTION; medium; Jordan
    # to correct; revert: set this back to 0.0 (the control)]. ⚠ At `stance_polarity` `legacy` the
    # term is constant within every realm deliberation that carries one (`H-202`'s measurement), so
    # this gain moved no realm outcome there; CR-16 ships `declared` (above), where the term varies
    # by subject and the gain scales it. Must be >= 0.
    # [JUSTIFIED: engine/season/hole_register.yaml H-202 -- the stance term's gain; §F2 gives the term and no gain, and the dukes' and Church's rising stakes have no rate, so it is injected and swept 0 / 1 / 3; shipped live at 1 per Jordan's 2026-10-09 ruling]
    stance_gain=1.0,                   # `H-202`, swept 0 (control) / 1 (SHIPPED) / 3
    # `H-255` (v11 CR-87, THE GRUDGE'S BOUND). THE WEIGHT §F2's STANCE TERM IS READ AT ON A VIOLENT ROW WHOSE SUBJECT
    # IS ITS OPPONENT (`data/verbs.py::VIOLENT_VERBS`: `fight`, `capture`; `decision/choose.py::stance_term`), in place
    # of `1 + stance_gain` -- under `declared` a -4 grudge read at 2 scored +8 against a pursuit term near 0.05, so the
    # grudge alone decided a killing. `None` is the REVERT: `1 + stance_gain`, exactly. Chosen by CR-87's reading rule
    # (the largest grid value at which, on seeds 0-4 at two seasons, no `fight` forms at stance above -3 and a
    # hand-built grudge in a war context still forms one). Must be >= 0 or None.
    # Once the contexts gate formation the bound is not binding on `fight`; it moves `capture` only. The second arm
    # of the rule (a -4 grudge in a war context ranks `fight` first) holds (`tests/test_cr87_violence_contexts.py`).
    # [JUSTIFIED: engine/season/hole_register.yaml H-255 -- the grudge's weight on a violent row; §F2 gives the term and no gain, and no document says how far a grudge may carry a man to violence, so it is injected, chosen by a declared reading rule and swept None (the revert) / the grid]
    hostile_stance_gain=2.0,           # `H-255`, swept None (revert: 1 + stance_gain) / 0 / 0.5 / 1.0 / 1.5 / 2.0 (SHIPPED)
    # `H-256` (v11 CR-87, ED-IN-0335: a major betrayal needs a series of events). WHERE A MEMBER'S BUILD-TIME LOYALTY
    # IS WRITTEN (`boot/realm.py`, its two `cast.stance_from_loyalty(cast.loyalty(...))` sites): `True` writes
    # the row toward the CREED Proposition (the faction's, or the goal's) and never toward its head person, and no
    # lower than the member band (valence x weight >= -1); `False` is the REVERT, the rows as they stood (a disloyal
    # member's -4 toward the King). A switch, not a number.
    loyalty_toward_creed=True,         # `H-256`, swept False (the revert) / True (SHIPPED, CR-87)
    # `H-274` (v11 CR-78, `strife-00` §5, the stamp). WHETHER A FLOW A PERSON HOLDS OPEN IS AMONG HIS OCCASIONS:
    # `True` appends `queries/world_q.py::flow_stakes` (the rungs, persons and offices at stake in each strand of
    # `flows_known` he does not read concluded) to `questions_for`'s stamp, as existing classes, so verbs form on
    # them; `False` is the CONTROL and the REVERT, the stamp as it stood. A switch, not a number. SHIPPED ON, CR-78
    # commit (2), a declared hash mover [ASSUMPTION; medium; Jordan to correct; revert: ship off]: it leaves
    # `build_realm(0)` and one-season default runs (seeds 0-2) EQUAL and moves some seeds from two to three seasons on; made on the
    # strife guard and HR-9 controls (2) and (4) holding, on against off (H-274's cite), IN-52's precedent.
    stamp_flow_stakes=True,            # `H-274`, swept False (the control, the revert) / True (SHIPPED, CR-78)
    # `H-196` (v9 IN-18 `G3`, slant). WHAT A TELLER PASSES ON ABOUT A SUBJECT: `newest` is the
    # pre-G3 pick; `valence` passes on the deed the teller judges most strongly by their own
    # pursuits, however old (`queries/person_q.py::said_of`; `rosters.yaml: said_slants`). `newest`
    # is the CONTROL and is SHIPPED [ASSUMPTION], on `H-190`'s precedent: the plan names the control
    # and is silent on shipping `valence`, and `valence` moves what tellings carry. v12 B11.09 (`08_FI_02` edits 2-4) adds `unshared` (drops the transport's
    # own kinds, `rosters.yaml: said_slants` `arms:`) and `unshared_first` (the same, then the first non-empty tier of `prefers`); `unshared_first` ships when
    # the batch's flip item sets it, once its gate reads (`16_PESSIMIST_FI_A` edits 1-3), so `newest` stays the shipped arm here.
    # [JUSTIFIED: engine/season/hole_register.yaml H-196 -- the slant arm; no document says which claim a teller chooses to pass on, so the readings are declared and swept newest / valence / unshared / unshared_first]
    said_slant="newest",               # `H-196`, swept newest (control, SHIPPED) / valence / unshared / unshared_first
    # v11 CR-29, A-32. WHETHER NEWS OF A SEAT CHANGE TRAVELS BY KIND: `realm` (SHIPPED) leaves the tenure-kind news
    # (`rosters.yaml: seat_news_kinds`) at the reach `witness_channels.event_reach` gives it; `local` lifts it from the
    # `reach` channel, so it reaches a person only by presence, jurisdiction and telling (`epistemic._ch_reach`,
    # `rosters.yaml: seat_news_arms`). A measurement arm, B of A-32, not a design.
    # [JUSTIFIED: A-32 -- ruled: one reach row for seat changes at `realm` ships, and `local` is kept as the tested alternative, so both are declared and swept realm / local]
    seat_news="realm",                 # A-32, swept realm (SHIPPED) / local (arm B)
    # v12 B11.08 (`08_FI_02` edit 5). WHO A TELLER OFFERS A TELLING (or a gift, an argument: a row whose cell carries a `with`
    # conjunct on `to`) TO: `known` (SHIPPED, the control) is every person he has any claim of (`person_q.known_persons`);
    # `seen_since_move` only those he holds a firsthand sighting of since his own newest movement (`person_q.present_persons`).
    # The fold's `hearer` conjunct still refuses an absent one (`rosters.yaml: telling_hearer_arms`). Flipped by the batch's flip item.
    # [JUSTIFIED: v12 B11.08 (08_FI_02 edit 5) -- no document gives who a teller offers a telling to, so both readings are declared and swept known / seen_since_move; shipped at the control]
    telling_hearers="known",           # B11.08, swept known (control, SHIPPED) / seen_since_move
    # v12 B11.22 (`08_FI_06` edit 6). WHETHER A TELLING CARRIES THE HAND THAT DID A DEED: under `on`, `queries/person_q.py::said_of` offers a person's deed claims
    # about what a subject DID (`attributed_deeds`) beside the claims whose subject he is, and a `PAIRED_KINDS` deed carries the sighting that names its doer
    # (`Said.pairing`); WITNESS deposits it as a told `seen` claim on the deed's chain, and `deed_doer` answers a told deed from it. `off` is the CONTROL (and the revert): a
    # paired deed heard second-hand names nobody. SHIPPED `on` by this item's last step, after the gate's `on` readings read (`test_told_pairing.py`). A value but `off` and `on` is refused where read.
    # [JUSTIFIED: engine/season/hole_register.yaml H-495 -- site: Fixtures told_pairing, the limit it closes; the proposal ships `on` when its gate reads, so it is injected, swept off (the control) / on, and shipped `on` once the hand-built gate read]
    told_pairing="on",                 # B11.22, swept off (the control) / on (SHIPPED, the gate read)
    # v12 B11.10 (`08_FI_02` edit 7). HOW MANY CLAIMS ABOUT A SUBJECT A TELLER MAY CHOOSE AMONG TO PASS ON: the top this many the slant ranks
    # (`queries/person_q.py::said_set`), one Candidate per claim and hearer (`rosters.yaml: choice_sourced`). `1` is the CONTROL and is SHIPPED: the single pick
    # `said_of` made before the choice, so no act is renamed or rescored. A whole number of 1 or more.
    # [JUSTIFIED: v12 B11.10 (08_FI_02 edit 7) -- no document gives how many claims a teller weighs, so it is injected and swept 1 (control, shipped) / 3; the shipped value is B98's]
    said_choices=1,                    # B11.10, swept 1 (control, SHIPPED) / 3
    # v12 B11.75 (`19_LACUNA` R-19-05). WHETHER `record` GRADES A CONCLUDER: at `1`, what a teller told a holder as a conclusion that names a doer (a told `concluded:<kind>` claim) is
    # paired by `queries/person_q.py::record` against the holder's own reading of who did that deed, as a told cell is (`_pair`), so a concluder caught naming the wrong hand loses his
    # record with that holder. `0` is the CONTROL and is SHIPPED: `record`'s `told` set is the cell predicates alone, so no pair is read and no weight moves. Only a TOLD holder is
    # scored (the design departs from R-19-05's "by WITNESS or by telling": `proposals/v12_B11_a_conclusion_acted_on.md` §2). B98 sets it.
    # [JUSTIFIED: v12 B11.75 (19_LACUNA R-19-05) -- no document gives whether a concluder is graded, only that one who is not is a free pass; injected and swept 0 (control, shipped) / 1, no target reading yet (B98)]
    record_concluders=0,               # B11.75, swept 0 (control, SHIPPED) / 1
    # `H-197` (v9 IN-18 `G6`, confidences). HOW OFTEN A TELLING IS MADE IN CONFIDENCE: the chance
    # `loop/witness.py::_circle_of` draws once per telling (its docstring says what a circle is and does).
    # `0` is the CONTROL and is SHIPPED [ASSUMPTION; medium; Jordan to
    # correct; revert: none needed while it ships at 0 -- shipping it on is this one value], on
    # `H-190`'s precedent: the plan names the shape (a swept chance at control 0) and is silent on
    # shipping it on. At 0 no draw is taken, every deposit is `own`, and no circle exists for a
    # retelling to break. Must lie in [0, 1]. v12 B11.10: an act that carries its own `in_confidence` (`tell`, `lie`: `rosters.yaml: choice_sourced`) is read by
    # that, and this is the share only for an act that carries none.
    # [JUSTIFIED: engine/season/hole_register.yaml H-197 -- the privacy chance; no document gives how often a telling is made in confidence, so it is injected and swept 0 / 0.5 / 1.0]
    telling_privacy=0.0,               # `H-197`, swept 0 (control, SHIPPED) / 0.5 / 1.0
    # `H-199` (v9 IN-15, `AX-7`'s divergence formula; `H-36` rules its shape). HOW FAR THE CHANNEL A
    # CLAIM ARRIVED ON AND WHAT ITS RECEIVER ALREADY HELD LOWER THE CONFIDENCE IT LANDS AT:
    # `queries/person_q.py::refracted_confidence` = `confidence * (1 - g*remove(channel)) *
    # (1 - g*dissent)`, applied by `loop/witness.py::_refract` to every deposit a person receives of
    # an act not their own. `0` is the CONTROL: nothing is refracted and every deposit is the
    # pre-IN-15 one. SHIPPED LIVE at the sweep's midpoint 0.5, per Jordan's ruling of 2026-10-09
    # (B-E): *"Gains are improvements and therefore ship."* [ASSUMPTION; medium; Jordan to correct;
    # revert: set this back to 0.0 (the control)]. Must lie in [0, 1] (`refracted_confidence` raises
    # outside it).
    # [JUSTIFIED: engine/season/hole_register.yaml H-199 -- the refraction gain; AX-7 rules THAT channel, competence and prior belief govern divergence and H-36 that it is receiver-side, and no document gives how much, so it is injected and swept 0 / 0.5 / 1.0; shipped live at 0.5 per Jordan's 2026-10-09 ruling]
    refraction_gain=0.5,               # `H-199`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # `H-200` (v10 CR-19, `AX-7`'s competence; `ED-IN-0327`). HOW FAR THE RECEIVER'S ATTUNEMENT SCALES THE
    # CONFIDENCE A TOLD CLAIM LANDS AT: `queries/person_q.py::refracted_confidence`'s `competence` factor =
    # `min(1, 1 + g*(attunement - mid)/(mid - floor))`, `mid`/`floor` the attribute scale's (`descriptors.py`),
    # a receiver with no authored Attunement reading 1. `0` is the CONTROL AND IT SHIPS (the knowledge-model
    # fold, `proposals/2026-11-04-knowledge-model-build-plan.md` §11 item 4): the factor is in place and the
    # flip to a live gain waits on CR-83's design, because a person-side gain cannot tell a lie from a truth
    # (`H-200`'s cite). Read only where `refraction_gain` refracts a deposit. Must lie in [0, 1].
    # [JUSTIFIED: engine/season/hole_register.yaml H-200 -- the competence gain; AX-7 rules THAT the reader's competence governs divergence and ED-IN-0327 that Attunement helps judge truthfulness, and no document gives how much, so it is injected and swept 0 / 0.5 / 1.0; shipped at the control 0 until CR-83's design gives a lie/truth separator]
    competence_gain=0.0,               # `H-200`, swept 0 (control, SHIPPED) / 0.5 / 1.0
    # `H-357` (v11 CR-27, M9 taken (a)). WHETHER A PERSON OFFERS A LIE: a row named in `rosters.yaml: lie_verbs`
    # (`lie`) forms a Candidate only while this is True (`decision/options.py::opening_set`; NOT
    # `loop/driver.py::resolvable_verbs()`). `False` is the CONTROL, swept, and is the tree before the row: no
    # lie is offered and `build_realm` reads as it did. `True` SHIPS [ASSUMPTION; medium; Jordan to correct;
    # revert: `lie_offered = False`, or delete the row, its cells and this key]. A bool, not a gain: it gates a
    # row's formation, and the false-value rule's own magnitude is `told_drift_band`'s.
    # [JUSTIFIED: engine/season/hole_register.yaml H-357 -- whether a person may offer a lie; M9 was taken (a) by delegation and no document says how often a person lies, so the offer is a switch and the chance is the scorer's, swept False / True; shipped True]
    lie_offered=True,                  # `H-357`, swept False (control) / True (SHIPPED)
    # `H-358` (v11 CR-31). HOW FAR WHAT A PERSON BELIEVES OF ANOTHER'S DESCENT, AGAINST HIS OWN CREED, MOVES HIS
    # REGARD FOR THEM: `queries/person_q.py::heritage_regard` = this x `STANCE_MAX` x the mean standing of the
    # hearer's own convictions on the concern the believed heritage engages (his newest own `seen` claim naming
    # the other, marks naming a heritage). `0` is the CONTROL: the term reads no ledger and `regard` is the tree
    # before it. 0.5 SHIPS, the shipped value of `judged_gain` and `told_valence_gain` [ASSUMPTION; medium;
    # Jordan to correct; revert: set this to 0.0 (one value)]. Must be >= 0.
    # [JUSTIFIED: engine/season/hole_register.yaml H-358 -- the caste estimate's gain; no document gives how far a believed descent moves regard, so it is injected and swept 0 / 0.5 / 1.0; shipped live at 0.5, the shipped value of the other two regard gains]
    heritage_gain=0.5,                 # `H-358`, swept 0 (control) / 0.5 (SHIPPED) / 1.0
    # `H-275` (v11 CR-79, `strife-00` §5, R14/A12). HOW FAR SHARED OR STRAINED AFFILIATION BETWEEN A HEARER
    # AND A TELLER MOVES THE CONFIDENCE A TOLD CLAIM LANDS AT: `loop/witness.py::_credit` =
    # `confidence * (1 + g*c)`, `c` = `queries/world_q.py::commensurate(hearer, teller)` in {-1, 0, +1},
    # clamped to `[0, max(confidence_default, the uncredited value)]`, applied after `_refract` to the told
    # deposit only, whether or not `refraction_gain` refracts. `0` is the CONTROL: nothing is credited and
    # `commensurate` is never read. 0.5 is the value given (`ED-IN-0316`) and SHIPS at CR-79 commit (2), a
    # declared hash mover, made on its guard [ASSUMPTION; medium; Jordan to correct; revert: set this back
    # to 0.0 (the control)]. Must lie in [0, 1] (`witness` raises outside it).
    # [JUSTIFIED: engine/season/hole_register.yaml H-275 -- the credit gain; strife-00 §5 gives the shape 1 + g*c and ED-IN-0316 the value 0.5, no document gives a measured magnitude, so it is injected and swept 0 / 0.5 / 1.0; shipped live at 0.5 at CR-79 commit (2), on its strife guard (ED-IN-0316)]
    regime_gain=0.5,                   # `H-275`, swept 0 (control) / 0.5 (SHIPPED at CR-79 (2)) / 1.0
    # `H-159` (`04 §B.8`'s `term?`; `T-n`, `architecture/meta/01_AXIOMS.md`:
    # *"the opening act declares the terms"*). HOW MANY SEASONS AN `oblige` RUNS BEFORE IT MATURES
    # UNPAID -- the term `_eff_oblige` declares on the edge it opens (`matures_at = tick + this`),
    # and the length each paying act winds it on by (`_eff_transfer`'s renewal: `matures_at + this`,
    # from where the term STOOD, so a payment made early buys the next term rather than being lost).
    # `H-80`'s shape exactly, and `record_stage_term` above is its precedent: the ACT declares the
    # term, a computed act carries no operands to declare one with, so this is the instrument's
    # declared stand-in. Injection sites: `loop/effects_governance.py::_eff_oblige` and `loop/effects_economy.py::_eff_transfer`.
    # ⚠ `None` IS THE CONTROL AND IT IS THE PRE-`17b` TREE EXACTLY: no `oblige` carries a term,
    # nothing matures at MATTER, no payment renews anything, and an establishment persists until
    # released -- `F.18`'s own *"assumed"* column. `1` is the shortest term the loop can express, and
    # it is harsh in a way worth knowing: RESOLVE runs AFTER MATTER within a tick, so the only window
    # to pay is the rest of the season in which the oblige was taken. `4` is SHIPPED: a holder has
    # three further seasons to pay in. NOT MEASURED, AND IT CANNOT BE YET -- no computed act forms an
    # `oblige` (its row is untyped), so no corpus run mints a
    # term and the shipped value moves no artifact; the falsifiers set it explicitly.
    # [JUSTIFIED: engine/season/hole_register.yaml H-159 -- the term an oblige is declared for; T-n rules THAT the opening act declares it and no document gives the length, so it is injected and swept None / 1 / 4]
    oblige_term=4,                     # `H-159`, swept None (control) / 1 / 4 (SHIPPED)
    # `H-158` (`04 §B.7` `Seat := ( …, upkeep, … )`, `F.18`). WHAT A SEAT PAYS
    # EACH PERSON OBLIGED TO IT, PER TERM, WHEN THE SEAT DECLARES NO `upkeep` OF ITS OWN -- which is
    # every seat any builder makes today. Read at ONE place, `queries/world_q.py::upkeep_of`, which
    # `_eff_transfer` asks when a seated holder pays out of the seat's own rung. `default_transfer_
    # amount`'s precedent (`H-94`, above) for both the shape and the arms: *"direction ruled,
    # magnitude open, is exactly a fixture."* `0` is the CONTROL of the MAGNITUDE -- keeping an
    # establishment costs nothing, so any payment at all renews every obligee at the home it
    # reaches; it is not the pre-`17b` tree (that is `oblige_term = None`), because the TERM still
    # matures unless somebody pays. `1` is SHIPPED: `default_transfer_amount`'s own unit, so the
    # default computed transfer, were one ever to pay, covers exactly one obligee. `3` makes an
    # establishment three times as dear.
    # [JUSTIFIED: engine/season/hole_register.yaml H-158 -- the per-obligee upkeep; ARCH §B.7 declares the field and F.18 its mechanism, and no document gives the amount, so it is injected and swept 0 / 1 / 3]
    default_upkeep=1,                  # `H-158`, swept 0 (control) / 1 (SHIPPED) / 3
    # `H-161` (`determine`; `21_RECONCILIATION.md:575`'s observable, *"below
    # quorum, `determine.refused`"*). HOW MANY PERSONS MUST SIT ON A BENCH FOR IT TO DETERMINE A
    # MATTER -- the RIGHT side of `determine`'s quorum conjunct (`bench.size >= quorum`, read by
    # `WorldReader`'s `quorum` stem, the only injection site). QUORUM IN ITS ORDINARY SENSE, the
    # members a body needs to transact business, and NOT the proceedings design's vote threshold (C-7:
    # live `commit`s to the disposition >= the quorum), which needs a disposition Proposition the
    # members commit to and the two grammar entries A.1 declared -- the SC lane's PHASE 2 step 15,
    # not `19`'s. `arrangements.yaml` owns a real `quorum:` key, required only on `disposal:
    # declared` rows, and no docketed matter maps to its arrangement yet (`judging_set`'s
    # docstring), so this is the stand-in for that key, `record_stage_term`'s shape.
    # `1` is SHIPPED and it is the LOOSEST value, not an argued one: `arbitration`, a seeded
    # arrangement whose disposal is a Tenure (since v9 SC-03a, four others are -- `detain`, `ban`),
    # has ONE decider, so a bench of one must be able to sit --
    # `speech_kinds`' *"the loosest floor rather than an authored restriction"* (`arrangements.yaml`).
    # At `1` the conjunct cannot refuse an actor the bench conjunct admitted (he is himself a member),
    # which is stated, not hidden: it is observable at `2` and `3`, where a lone judge is refused.
    # [JUSTIFIED: engine/season/hole_register.yaml H-161 -- the bench quorum; the observable rules THAT a determination below quorum refuses, and no document gives the number for a bench-disposal arrangement, so it is injected and swept 1 / 2 / 3]
    bench_quorum=1,                    # `H-161`, swept 1 (SHIPPED, loosest) / 2 / 3
    # `H-85` (v9 PC-06 K-3). THE THREAD SENSITIVITY A PERSON MUST HAVE TO ATTEMPT `thread_read` -- the
    # RIGHT side of its `scalar_threshold` cell (`thread_sensitivity >= thread_sensitivity.gate`), read
    # by `queries/person_q.py::OwnStateReader`'s gate stem, the only injection site, for the fold and
    # the person alike; `bench_quorum`'s shape one row up. `30` is SHIPPED and its SOURCE is
    # `fieldwork_v30.md` §4.2 (the Thread-Read row, *TS >= 30*), which is design prose and reference
    # (`CLAUDE.md` §0.05): the source of the number, not the reason it is correct. `0` is the CONTROL:
    # every AUTHORED value passes (the cast's three `ts: 0` rows included) and every unauthored one still
    # refuses, which is what makes "`None` is not 0" observable. `50` is the tighter point, declared,
    # not run. [ASSUMPTION; medium; Jordan to correct.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-239 -- `site: Fixtures thread_sensitivity_gate`, graded `assumption`; fieldwork_v30.md §4.2 gives TS >= 30 as design prose, which sources the number and does not make it correct, so it is injected and swept 0 / 30 / 50 (50 declared, not run)]
    thread_sensitivity_gate=30,        # `H-239`, swept 0 (control) / 30 (SHIPPED) / 50 (declared, not run)
    # `H-156` (v9 IN-26, BOUND-PAPER). THE VERBS `decision/options.py::opening_set` FORMS NO CANDIDATE FOR
    # -- `H-156`'s option (a), *hold it out of formation*, as a switch rather than a row edit, so the hold
    # and its release are one value and the hand-built fold is untouched (a withheld verb still executes
    # from an act that names it). Each member must be a `verb_table.yaml` verb (`opening_set` refuses
    # another). SHIPPED naming `destroy_record` -- THE SINK ARM OFF: since IN-26 its row is formable
    # (`A-13`'s shape), and withheld it forms for nobody, as before, so every hash is today's. `()` is THE
    # SINK ARM ON (`H-156` option (b) for that row): a holder may burn what he holds. ED-IN-0306 phase 2 adds the
    # four army verbs (`loop/effects_army.py`): their command is the act's payload, which no Candidate carries. [ASSUMPTION; medium;
    # Jordan to correct; the flip ON is a separate, declared hash-moving commit, IN-52's precedent.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-156 -- the formation-policy row; (a) and (b) are both defensible and lead to different corpora, so the arm ships at (a), today's state, and (b) is the declared second point]
    withheld_verbs=("destroy_record", *ARMY_VERBS, "marshal", "surrender"),   # `H-156`, swept ("destroy_record", *ARMY_VERBS, "marshal", "surrender") (control, SHIPPED) / (*ARMY_VERBS, "marshal", "surrender") (the sink arm: it also un-withholds both new verbs, so a destroy_record sink measurement on it carries the marshal fan); `marshal` (CP-T04-02, `H-361`) and `surrender` (CP-T04-07) ship withheld so the season is EQUAL at shipped, each flip a separate declared mover
    # `H-356` (v11 CR-55). HOW MANY SEASONS AFTER ITS OWN A DOCKET ITEM MAY BE HELD BEFORE MATTER LAPSES IT
    # (`matter.lapsed`, `loop/matter.py`; age read off the item's docketing Event or Date by
    # `queries/world_q.py::lapsing_items`, nothing stored). An item whose party has died, whose venue
    # seats no bench, or whose matter is no person (`determine` binds a person) is held for ever
    # otherwise, and `docket_question` keeps naming it. `None` is the CONTROL: no item lapses, the
    # pre-item docket. `4` is SHIPPED, `oblige_term`'s own length (`H-159`): a matter docketed in season
    # `t` is heard through season `t + 4` and lapses as `t + 5` opens. `2` is the harsh point, `8` the
    # patient one; `0` is the instrument's (a two-season probe), not a sweep point.
    # [ASSUMPTION; medium; Jordan to correct; revert: never]
    # [JUSTIFIED: engine/season/hole_register.yaml H-356 -- the docket lapse rule; the observable rules THAT a held matter lapses visibly, and no document gives the number of seasons, so it is injected and swept 2 / 4 / 8]
    docket_lapse=4,                    # `H-356`, swept None (control) / 2 / 4 (SHIPPED) / 8
    # `H-414` (B04.22). HOW MUCH A CONFERRER'S VIEW OF A CANDIDATE WEIGHS IN WHOM HE SEATS: the weight on the `fit` term
    # `decision/choose.py::score_terms` reads over a seating row's `to` (his regard for the candidate, and the skill his
    # own ledger holds of him where the seat's row names one). `0.0` is SHIPPED and the CONTROL: the term is exactly
    # 0.0 and the conferrer seats positionally, the lowest-id person he knows, as before. `0.5` and `1.0` are the sweep;
    # the flip to a non-zero value is its own declared mover, made on a reading.
    # [ASSUMPTION; medium; Jordan to correct; revert: `0.0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-414 -- site: Fixtures confer_fit_weight, graded `assumption`; 06_FA_office_capabilities edit 4 gives no number for the weight, so it is injected at the control and swept 0.0 / 0.5 / 1.0]
    confer_fit_weight=0.0,             # `H-414`, swept 0.0 (control, SHIPPED) / 0.5 / 1.0
    # `H-420` to `H-423` (B05.08; CAP B2, U1-B step 2). THE FOUR NUMBERS THE JOINT CALIBRATION SETS, one home each. B05.09 (`pool_add`,
    # `pool_floor`) and B05.14 (`opposition_rate`) are the readers; `attribute_level` is read only by a planted `edge` row (none ships,
    # B05.25). B05.23 SHIPS THE LIVE VALUES for the social roll (OBS §4 step 5; the calibration test reads them, CAL §2). One pair for every
    # site (`pool_add`, `pool_floor`); the per-site names MAP's `social_pool_*` and `combat_pool_*` are not created; the fight reads
    # `score + addends`, never the pair (B05.09).
    # `pool_add`: dice a skill score is given before the roll (the base of the pool). Control 0, live 6 (SHIPPED).
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-420 -- site: Fixtures pool_add, graded `assumption`; CAP B2 gives the live 6 and no document derives it, so it is injected and swept 0 / 3 / 6]
    pool_add=6,                        # `H-420`, swept 0 (control) / 3 / 6 (live, SHIPPED)
    # `pool_floor`: the fewest dice a pool is ever rolled at. Control 0 (no floor), live 5 (SHIPPED).
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-421 -- site: Fixtures pool_floor, graded `assumption`; CAP B2 gives the live 5 and no document derives it, so it is injected and swept 0 / 3 / 5]
    pool_floor=5,                      # `H-421`, swept 0 (control) / 3 / 5 (live, SHIPPED)
    # `attribute_level`: the size of one step of the governing attribute's edge (U1 §4, A-7): a `LEVEL_SIGMA` name per point
    # of the attribute above the mid-point (for the roller) or below it (against). Control `None` (no level), live `minor` (SHIPPED).
    # [ASSUMPTION; medium; Jordan to correct; revert: `None`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-422 -- site: Fixtures attribute_level, graded `assumption`; CAP B2 gives the live `minor` and no document derives it, so it is injected and swept None / minor / moderate]
    attribute_level="minor",           # `H-422`, swept None (control) / minor (live, SHIPPED) / moderate
    # `opposition_rate`: the share of the opposing person's score an obstacle takes up, per point. Control 0.5 (lane A's
    # halving); live `engine/dice_engine/dice_engine.py::MU_PER_DIE` (SHIPPED), READ FROM THAT OWNER and never retyped.
    # [RULED (A-26, A-71, A-79); revert: `0.5`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-423 -- site: Fixtures opposition_rate, graded `ruled` (A-26, A-71, A-79); the live value is `MU_PER_DIE` and the control is lane A's one half, so it is injected and swept 0.5 / MU_PER_DIE / 0.3]
    opposition_rate=MU_PER_DIE,        # `H-423`, swept 0.5 (control) / MU_PER_DIE (live, SHIPPED) / 0.3
    # `H-424` (B05.14; OBS §1, SC-B Edit A). HOW HARD EACH DIFFICULTY LEVEL IS: the obstacle a verb row's `difficulty:` level contributes
    # before any opposition (`rosters.yaml: difficulty_levels`, closed: refused at load if the keys are not exactly the roster's).
    # SHIPPED: the calibrated arm (B05.23), 0 / 0.8 / 1.6 / 2.4 in level order: `routine` at A-79's centre, equals on a routine matter
    # carrying about a quarter (C1's P(Success or better) 0.24 to 0.29 at skill scores 0 to 7, ON THE CALIBRATION GRID'S OPERANDS: the opponent scores rank + 4, `test_sc_calibration_targets.py`; `pool.score` floors an opponent below `pool_default` at `pool_default`, so a rank-0 actor against a rank-0 opponent composes opposition 6 and Ob 5.6 in play, P(Failure) about 0.74, outside C1's band), each level one more such step (C2's rise in
    # P(Failure) 0.08 to 0.12 a step). The control is `DIFFICULTY_OB_CONTROL` (0 / 1 / 2 / 3). Replaces lane A's
    # `rosters.yaml: task_difficulty` (a number per verb) and its `obstacle_model` switch.
    # [ASSUMPTION; Jordan to correct: `routine` 0.8, the value at which V2's model read 25 % carried -- basis:
    # `proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-15-social-contest-redesign-v2_part4.md` §H item 1 (A-137); the other levels
    # its multiples, the smallest change that keeps C2 green. revert: `DIFFICULTY_OB_CONTROL`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-424 -- site: Fixtures difficulty_ob, graded `assumption`; no document derives the size of a level, so it is injected and swept]
    difficulty_ob=dict(zip(DIFFICULTY_LEVELS, (0, 0.8, 1.6, 2.4), strict=True)),   # `H-424`, swept control (`DIFFICULTY_OB_CONTROL`) / half / three-quarter / calibrated (SHIPPED)
    # `H-426` (B05.21; T13 edit 1, T3). HOW FAR A HEARER'S HOSTILITY MOVES THE OBSTACLE, per full clamp: the obstacle term `regard` is
    # `regard_step x clamp(-stance / STANCE_MAX, 0, 1)` over the stance rows the counterparty holds toward the actor (`person_q.stance_toward`,
    # `data/rosters.py::STANCE_MAX`), for one person counterparty and no audience (`sigma.py::_regard_term`); the favourable half of the same clamp is
    # `favour` leverage, at the same step. `0` is the CONTROL: the term reads nothing and is not listed, and no stance brings a level.
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-426 -- site: Fixtures regard_step, graded `assumption`; T13 T3 gives the live 1.0 and no document derives it, so it is injected and swept 0 / 0.5 / 1.0 / 2.0]
    regard_step=1.0,                   # `H-426`, swept 0 (control) / 0.5 / 1.0 (live, SHIPPED, B05.23: C5) / 2.0
    # `H-610` (B21.09; OBS §2 member 6, OBS §4 step 6+; `14_VERBS_BINDING_A` commit A3). HOW MUCH ONE RUNG OF RANK STANDING AGAINST THE ACT WEIGHS, in
    # obstacle: the term `rank_gap` is `rank_step x` the count of `rung_kinds` steps by which the person (or holding) acted on or for stands above
    # the rung of the seat the actor exercises (`sigma.py::_rank_gap_of`, `_rank_gap_term`). `0` is the CONTROL ("equal at control"): the term
    # reads nothing and is not listed, so every roll composes the obstacle it had before.
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-610 -- site: Fixtures rank_step, graded `assumption`; OBS proposes 0.25 and no document derives it, so it is injected at the control and swept 0 / 0.25 / 0.5]
    rank_step=0.0,                     # `H-610`, swept 0 (control, SHIPPED) / 0.25 / 0.5
    # `H-613` (B21.61; OBS §2 member 29, OBS §4 step 6+; `16_PESSIMIST_FA_B` edit 2, A-105). HOW MUCH A SEAT OF ANOTHER CHAIN OF SEATS WEIGHS AGAINST A
    # CONFERRAL, in obstacle: the term `cross_chain` is `cross_chain_step x` 1 where the seat the act names and the seat it is exercised through are of
    # different factions (`gate.across_chains`; `sigma.py::_cross_chain_term`), so a foreign holder stays uncommon (A-105). `0` is the CONTROL ("equal at
    # control"): the term reads nothing and is not listed, so every roll composes the obstacle it had before.
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-613 -- site: Fixtures cross_chain_step, graded `assumption`; the source proposes 2 and no document derives it, so it is injected at the control and swept 0 / 1 / 2]
    cross_chain_step=0.0,              # `H-613`, swept 0 (control, SHIPPED) / 1 / 2 (proposed)
    # `H-614` (B21.69; `IS-B3-FA-07`, A-105). HOW MUCH THE POWER OF A HOLDER'S FACTION OVER THE HOST'S WEIGHS AGAINST AN ACT ON HIS SEAT, in obstacle: the
    # term `faction_power` is `faction_power_step x` 1 where the faction the seat's live holder coheres under outweighs the faction of the seat the act is
    # exercised through (`faction_q.weight`, compared; `sigma.py::_faction_power_of`, `_faction_power_term`), so a foreign officer of a stronger faction is
    # the harder to unseat or to cut down: "the king's appointee stays in place unless the king is convinced otherwise" (A-105). `0` is the CONTROL ("equal
    # at control"): the term reads nothing and is not listed, so every roll composes the obstacle it had before.
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-614 -- site: Fixtures faction_power_step, graded `assumption`; `IS-B3-FA-07` leaves the value to "Jordan or the B21 calibration" and no document derives it, so it is injected at the control and swept 0 / 1 / 2]
    faction_power_step=0.0,            # `H-614`, swept 0 (control, SHIPPED) / 1 / 2
    # `H-611` (B21.12; `14_VERBS_BINDING_C` commit C1, edit 1). THE LENGTH, IN SEASONS, OF THE TERM A PARTIAL `succeed`/`revoke` OPENS A HOLD FOR (the one
    # `provisional_term`; the BYZANTINE files cite it and ship no second value). Read at ONE place, `loop/effects_shared.py::_provisional_term`.
    # `2` SHIPS since B21.73 (BIND_C's flip; UNDECIDED u-1 reading (a)): a Partial `confer` or `succeed` opens its hold for two seasons, and MATTER
    # closes it at the barrier of tick `+ 2` (`T-n`), so the seat falls vacant and is offered again. `None` is the CONTROL and the REVERT: a Partial opens an
    # untermed hold, exactly as a Success does, so the two differ by nothing. The value is BIND_C's proposed one; no document derives it.
    # [ASSUMPTION; medium; Jordan to correct; revert: `None`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-611 -- site: Fixtures provisional_term, graded `assumption`; BIND_C proposes 2 and no document derives it, so it ships at the proposed 2 (B21.73) and is swept None (control) / 1 / 2 / 4]
    provisional_term=2,                # `H-611`, swept None (control) / 1 / 2 (proposed, SHIPPED) / 4
    # `H-612` (B21.23; `06_FA_decree_binds` edit 4). HOW MANY SEASONS OF SUSPICION OPEN A WRIT-MAKER'S RECALL: `queries/person_q.py::suspicions`
    # (his own ledger's count of the seasons a person withheld compliance on a writ he made, less those he only obeyed in, floored at zero)
    # reaching this number puts the person and each seat of his that `may_revoke` admits on the maker's question as classed referents
    # (`queries/world_q.py::recalls`). It opens the question and decides nothing: the recall is `revoke`'s resistible draw (A-24, A-47).
    # `None` is the REVERT: the occasion is off and no question carries a recall. The design names a threshold and no number; its audit
    # escape is worth two, so the threshold is read as above two.
    # [ASSUMPTION; medium; Jordan to correct; revert: `None`, the occasion off.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-612 -- site: Fixtures recall_suspicion, graded `assumption`; the design names a threshold and gives no number, so it ships at 3 (above its audit escape's two) and is swept 1 / 3 / 5, with None the revert]
    recall_suspicion=3,                # `H-612`, swept 1 / 3 (SHIPPED) / 5; `None` the revert (the occasion off)
    # `H-427` (B05.21; T13 edit 1, edit 4, T5). WHETHER THE ARRANGEMENT ROW'S `proofs:` COLUMN FILTERS WHAT A SPEAKER'S PROOFS WEIGH: `off` -- every
    # deed claim counts (`world_q.proofs` as it was); `on` -- under a docketed row only the claims whose kind (`rosters.yaml: proof_kind_of_source`) the
    # row admits count, the rest weigh 0 (`sigma.py::_read_social_roll` passes the row's `proofs:`; `world_q` reads no arrangement itself).
    # [ASSUMPTION; medium; Jordan to correct; revert: `off`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-427 -- site: Fixtures proof_admission, graded `assumption`; T13 T5 gives `on` as the calibrated value and no document derives it, so it is injected and swept off / on]
    proof_admission="on",              # `H-427`, swept off (control) / on (live, SHIPPED, B05.23)
    # `H-428` (B05.21; T13 edit 1, T4). THE WEIGHT OF WHAT AN ACT WOULD TAKE OR IMPOSE, in obstacle, by the Tenure kind it opens: the obstacle term
    # `stakes` (`sigma.py::_stakes_term`: `arrest` reads `detain`; `determine` the kind its docketed row `disposes:`). Keyed on exactly the
    # `tenure_kinds` roster (refused at load). `0` for every kind is the CONTROL (OBS §1: "control 0"): the term is not listed.
    # [ASSUMPTION; medium; Jordan to correct; revert: every kind 0.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-428 -- site: Fixtures stakes_ob, graded `assumption`; T13 T4 gives the live `oblige` 0, `detain` 0.5, `ban` 1.0 and no document derives them, so it is injected at the control and swept 0 / 0.5x / 1x / 2x of those]
    stakes_ob={kind: 0 for kind in roster("tenure_kinds")},   # `H-428`, swept 0 (control, SHIPPED) / 0.5x / 1x / 2x
    # `H-445` (B07.01; 18-A edit 7, UNDECIDED (11) (iii)). WHETHER THE LOOP TAKES A `graded_tasks` ROUTE THAT CARRIES `armed_by: task_draw_arm`
    # (`data/rosters.py::graded_route`, read by `loop/resolve.py` and `seam/wrappers/sigma.py::_rolled_as`): `off` -- each such verb (the 18 `task`
    # rows and `reconstruct`) folds flat, as before B07 (the control); `on` -- it is drawn through `seam.grade` and folded at its band. B07.05 flipped it (gate 5 read); the revert is the one value.
    # [JUSTIFIED: engine/season/hole_register.yaml H-445 -- site: Fixtures task_draw_arm, graded `assumption`; 18-A ships it `on` only once its gate 5 reads, so it was injected at the control and is swept off / on]
    task_draw_arm="on",                # `H-445`, swept off (control) / on (SHIPPED since B07.05; revert: `off`)
    # `H-456` (B09.03; B09.05; `16_PESSIMIST_CORE_a_refusal_is_remembered` edit 3). HOW HARD A REMEMBERED REFUSAL PUSHES A PERSON OFF RETRYING THE SAME
    # OPPORTUNITY: `decision/choose.py::admission_weight` puts `1 - refusal_memory * refused_before / confidence_default` on a candidate's
    # pursuit term, `refused_before` the present confidence of his newest firsthand refusal of that subject (`queries/person_q.py`). `0.5` SHIPS
    # (B09.05): half the pursuit weight is withheld at a fresh full-confidence refusal and returns as the claim fades at `claim_decay_per_season`.
    # `0.0` is the CONTROL (the factor is exactly 1.0 and no ledger is read; the revert); `1.0` zeroes the term at a fresh full-confidence refusal.
    # [ASSUMPTION; medium; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-456 -- site: Fixtures refusal_memory, graded `assumption`; the source proposes 0.5 and gives no derivation, so it ships as an assumption for Jordan and is swept 0.0 / 0.5 / 1.0]
    refusal_memory=0.5,                # `H-456`, swept 0.0 (control; revert) / 0.5 (SHIPPED since B09.05) / 1.0
    # `H-111` (B09.04; `U5a_DICE_owed_edits` §4; B11.12, A-81; B11.61, CP-T06-04). HOW WITNESS TREATS AN EVENT OF A KIND `rosters.yaml: undeposited_kinds` NAMES (`finding.none`, `inquiry.refused`):
    # `none` -- the whole Event fans to nobody (the CONTROL; revert); `actor` -- the Event is deposited as any Event but for its event-kind claim: its doer holds his own reads,
    # the present hold `seen` (SHIPS since B11.12: no null scene; the arm's name is B09.04's and B11.61 widened what it deposits). The arms are `finding_none_deposit_arms`.
    # [ASSUMPTION; medium; Jordan to correct; revert: `none`.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-111 -- site: Fixtures finding_none_deposit, graded `assumption`; the skip's own note names the narrower arm as the alternative Jordan would name, so it is injected at the control and swept none / actor]
    finding_none_deposit="actor",      # `H-111`, swept none (control; revert) / actor (SHIPPED since B11.12)
    # `H-183` (B09.06; `16_PESSIMIST_SC_B_one_reader_of_a_ledger` edit 1). WHETHER THE ONE COMPARATOR WEIGHS HOW SURE THE HOLDER STILL IS:
    # `queries/person_q.py::teller_weight` multiplies every claim's weight by `present_confidence(c) / confidence_default`, and
    # `ledger_weigh` takes the closure for any ledger holding a claim below full confidence. `False` is the CONTROL and the revert (the
    # closure and the condition are today's, exactly); `True` SHIPS (B09.08). A switch on an existing magnitude, `claim_decay_per_season`.
    # [ASSUMPTION; medium; Jordan to correct; shipped `True`; revert: `False`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-183 -- the row that weighs a told claim by its teller's `record`; this switch adds the claim's own present confidence to that one product, shipped `True` and swept False (control, the revert) / True]
    weigh_confidence=True,             # `H-183`, swept False (control; revert) / True (SHIPPED since B09.08)
    # `H-457` (B09.12; `16_PESSIMIST_GAME_standing_occasions_carry_their_cause`). WHETHER AN ACT FORMED ON A STANDING OCCASION NAMES THE EVENT THAT
    # OPENED IT: `loop/resolve.py::_occasion_ids` adds to `causes[]` the id of the first kind `rosters.yaml: standing_occasion_opened_by` lists for
    # the act's classed referent that the log holds as written about it (a `succession.claimed` cites the `tenure.closed` that emptied the seat).
    # `False` is the CONTROL and the revert (today's `[]`: the act's Events cite the act alone); `True` SHIPS.
    # [ASSUMPTION; medium; Jordan to correct; shipped `True`; revert: `False`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-457 -- site: Fixtures standing_occasion_cause, graded `assumption`; the proposal ships the arm `True` and gives no derivation for the opening kinds it reads, so it is injected and swept False (control, the revert) / True / True with `Office`'s two kinds in the other order]
    standing_occasion_cause=True,      # `H-457`, swept False (control; revert) / True (SHIPPED, B09.12) / True with `Office` read the other way
    # `H-458` (B09.17; `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds`). HOW OFTEN A WITNESS CONNECTS WHAT HE WITNESSED TO WHAT HE ALREADY HOLDS: for a
    # witness whose channel supplies `why` (`rosters.yaml: observation_terms.supplied_by`) who holds a claim deposited from an antecedent Event of the one he
    # witnessed, the chance that `Seen.why` names that claim (`epistemic._term_why`, one draw keyed `(pid, "why:<event id>")`, so no other stream moves);
    # the actor of the Event is not drawn for (he always knows the occasion he acted on) and reads it at any chance above 0. `0.0` is the CONTROL and SHIPS:
    # no draw is taken, no `why` is read, and every content hash is the one before B09.17 (the raise is B98's, one commit and one re-pin). The proposed on-value is
    # 0.6, +0.2 where his claim on the antecedent carries a `who` (the +0.2 half is NOT built here: it has no home but a second fixture, B98's to add).
    # [ASSUMPTION; medium; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-458 -- site: Fixtures connection_chance, graded `assumption`; the source proposes 0.6 and gives no derivation, so it is injected at the control and swept 0.0 / 0.6 / 1.0]
    connection_chance=0.0,             # `H-458`, swept 0.0 (control, SHIPPED) / 0.6 (proposed) / 1.0
    # `H-459` (B09.20, lane D4; IN-58's sworn-to half). HOW FAR AN OATH TO THE VICTIM'S SEAT BINDS A JUDGE TO THE VICTIM: for a judge who holds a live,
    # un-`imposed` `oblige` to a seat S and whose own ledger holds `(S, hold, patient)` (B09.22's claim: a seat closed by a death names its holder),
    # `queries/person_q.py::_bond` adds this to the allegiance `a` before its clamp, so a sworn judge weighs a deed done to the patient as the patient's ally
    # does. It reaches only `deeds_judged`'s paired-deed term (`lean * bond`) and so only the regard a judge forms of a doer. `0.0` is the CONTROL and
    # SHIPS ("it ships OFF"): `_bond` is the stored half alone, and every content hash is the one before B09.20. At the shipped `observation_deposit_mode`
    # (`actor`) only the killer holds `(S, hold, patient)`, so the arm is reached by few judges until a mode or a teller carries it.
    # [ASSUMPTION; medium; Jordan to correct -- the sweep's points; basis: `stance_toward` is bounded in [-1, 1] once normalised, so the oath is weighed on the stance's own scale; revert: 0.0, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-459 -- site: Fixtures sworn_bond, graded `assumption`; the entry states no value, so it is injected at the control and swept 0.0 / 0.5 / 1.0]
    sworn_bond=0.0,                    # `H-459`, swept 0.0 (control, SHIPPED) / 0.5 / 1.0
    # `H-464` (B10.04; `U5a_CHAR_owed_amendments` §2). HOW MUCH A FULL REGARD WEIGHS IN THE STANCE TERM: `decision/choose.py::stance_term` reads the arm's
    # value times `stance_scale / STANCE_MAX`, before either gain, so regard counts as a share of the stance bound. `STANCE_MAX` (25) is the CONTROL and
    # SHIPS: the quotient is exactly 1.0 and the term is today's. Swept 0.2 / 0.4 / 0.8, so that a full loyalty sits 4, 8 and 16 temperatures from zero at
    # `choice_temperature` 0.05; the flip is B98's, after a reading.
    # [ASSUMPTION; medium; Jordan to correct; revert: the control (`STANCE_MAX`).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-464 -- site: Fixtures stance_scale, graded `assumption`; the source gives no live value, so it is injected at the control (`STANCE_MAX`, read at import) and swept 25 / 0.2 / 0.4 / 0.8]
    stance_scale=STANCE_MAX,           # `H-464`, swept 25 = STANCE_MAX (control, SHIPPED) / 0.2 / 0.4 / 0.8
    # `H-465` (B10.06; `02_CHAR_scar_cap_and_regard_unit` edit 1, `02_CHAR_scar_is_a_wound` row 3). THE SCAR'S RATE: `loop/resolve.py::_scar_witnesses` drops, before
    # its write, every count an observer already took this season: `element` keeps one count per person per element, `person` one count per person, on the element
    # he holds most violated (largest weight x |lean|, ties by name). `None` is the CONTROL and SHIPS: uncapped, today's counts exactly, and every content hash
    # is the one before B10.06 (the flip to `person` is B98's). A value outside `rosters.yaml: scar_season_caps` is refused where it is read.
    # [ASSUMPTION; medium; Jordan to correct; revert: `None`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-465 -- site: Fixtures scar_season_cap, graded `assumption`; the sources give the domain and not a live value, so it is injected at the control and swept None / element / person]
    scar_season_cap=None,              # `H-465`, swept None (control, SHIPPED) / element / person
    # `H-466` (B10.07; `02_CHAR_scar_is_a_wound` row 1). WHO CAN BE SCARRED: `person_q.broken_by` reads it. `any` is the CONTROL and SHIPS: every held element
    # an act violates is counted, today's rule exactly. `primary` counts only a person's primary elements: the fewest top-weighted pursuits whose weights
    # sum to `scar_primary_mass`, and the affiliations he stands for (`person_q.stands_for`, intensity 3 or more of 5). A value outside `rosters.yaml: scar_holds` is refused where
    # it is read. [ASSUMPTION; medium; Jordan to correct; revert: `any`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-466 -- site: Fixtures scar_hold, graded `assumption`; the source proposes `primary` and no derivation of the arm, so it is injected at the control and swept any / primary]
    scar_hold="any",                   # `H-466`, swept any (control, SHIPPED) / primary (proposed)
    # `H-469` (B10.07). HOW MUCH OF A PERSON'S WEIGHT HIS PRIMARY PURSUITS MAKE UP: read only at `scar_hold: primary`, by `person_q.broken_by` and `upheld_by`. 0.6 is PP-684's
    # lower bound for the primary band, so it SHIPS (it moves nothing while `scar_hold` is `any`). [ASSUMPTION; medium; Jordan to correct; revert: none, it is inert at the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-469 -- site: Fixtures scar_primary_mass, graded `assumption`; PP-684's lower bound is the one value the source gives; the sweep points 0.4 and 0.8 are an assumption (a step of 0.2 either side), swept 0.4 / 0.6 / 0.8]
    scar_primary_mass=0.6,             # `H-469`, swept 0.4 / 0.6 (SHIPPED, PP-684's lower bound) / 0.8
    # `H-467` (B10.07). HOW FAR AN ACT MUST POINT AGAINST A PURSUIT TO VIOLATE IT (and for the vindication, how far it must point with one to honour it): `person_q._pursuits_violated_by`
    # counts a pursuit violated only when `pursuit_lean(verb, e) < -floor`, and `_pursuits_upheld_by` honoured when the lean is above `+floor`. `0.0` is the CONTROL and SHIPS: the
    # sign test, today's. [ASSUMPTION; medium; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-467 -- site: Fixtures scar_lean_floor, graded `assumption`; the source proposes 0.2, swept 0 / 0.2 / 0.4, so it is injected at the control]
    scar_lean_floor=0.0,               # `H-467`, swept 0.0 (control, SHIPPED) / 0.2 (proposed) / 0.4
    # `H-468` (B10.07). WHETHER SEEING A THING ONE LIVES FOR HONOURED TAKES A SCAR AWAY: under `on`, `loop/resolve.py::_scar_witnesses` writes `-1` on the primary pursuit an act upholds
    # most (above `+scar_lean_floor`) that the observer holds a count on, never below 0, at most once per person per season, before the act's own violations. `off` is the CONTROL and
    # SHIPS: no count ever falls. A value outside `rosters.yaml: scar_vindications` is refused where it is read. [ASSUMPTION; medium; Jordan to correct; revert: `off`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-468 -- site: Fixtures scar_vindication, graded `assumption`; the source proposes `on`, so it is injected at the control and swept off / on]
    scar_vindication="off",            # `H-468`, swept off (control, SHIPPED) / on (proposed)
    # `H-471` (B10.10; `U5a_CHAR_owed_amendments` §2). WHETHER THE STANCE TERM'S REGARD IS BOUND TO THE ROW TYPE'S OWN BOUND: `decision/choose.py::_stance_arm` clamps the
    # value it reads (`regard`, and `legacy`'s `stance_toward`) to `+-STANCE_MAX` (`data/rosters.py`) before the polarity sign, so B10.04's `stance_scale` factor in `stance_term`
    # reads the clamped value. `False` is the CONTROL and SHIPS: today's unbounded sum, the realm hash the one before B10.10; the flip is B98's, after a reading.
    # [ASSUMPTION; medium; Jordan to correct; revert: `False`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-471 -- site: Fixtures stance_clamp, graded `assumption`; the source proposes the clamp and no live reading, so it is injected at the control and swept False / True]
    stance_clamp=False,                # `H-471`, swept False (control, SHIPPED) / True (proposed)
    # `H-470` (B10.09; `02_CHAR_scar_cap_and_regard_unit` edits 1 (`regard_unit`), 3). THE UNIT `person_q.regard` COUNTS ITS JUDGED AND TOLD HALVES IN, an arm of `rosters.yaml: regard_units`:
    # `raw` is the CONTROL and SHIPS (today's sum of `deed_term`, a pursuit weight times an alignment cell, in no unit the stance row's valence step shares); `stance` sums
    # `person_q.deed_steps`, each deed's worth as the cosine of the holder's projected pursuits against the deed kind's alignment row (a paired deed's times its `_bond`), so one deed
    # is at most one valence step before `judged_gain` / `told_valence_gain`. A value outside the roster is refused where it is read. The flip is B98's, a declared mover read against the control.
    # [ASSUMPTION; medium; Jordan to correct; revert: `raw`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-470 -- site: Fixtures regard_unit, graded `assumption`; the source proposes `stance` as the live arm and ships no flip, so it is injected at the control and swept raw / stance]
    regard_unit="raw",                 # `H-470`, swept raw (control, SHIPPED) / stance (proposed)
    # `H-474` (B10.20; `U5a_CHAR_owed_amendments` §4, F-PES-CHAR-08). WHETHER A DEED DONE TO A PERSON IS WEIGHED BY THE JUDGE'S BOND TO THE ONE IT WAS DONE TO: `paired_only` is the
    # CONTROL and SHIPS (today: a `PAIRED_KINDS` deed carries `person_q._bond`, an unpaired deed is its pursuits' reading alone); `person_subject` gives the factor to an unpaired
    # deed whose verb row takes a Person as its subject (`referent_class: Person`), read by `person_q.regard` through `deed_term` and `deed_steps`. A value outside
    # `rosters.yaml: deed_counterparties` is refused where it is read. The flip is B98's. [ASSUMPTION; medium; Jordan to correct; revert: `paired_only`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-474 -- site: Fixtures deed_counterparty, graded `assumption`; the source proposes `person_subject` as the live arm and ships no flip, so it is injected at the control and swept paired_only / person_subject / person_subject at regard_unit stance]
    deed_counterparty="paired_only",   # `H-474`, swept paired_only (control, SHIPPED) / person_subject (proposed) / person_subject at regard_unit stance
    # `H-476` (B10.28; `02_CHAR_resolve_and_temper` edit 2; CR-93 item 2, AR-23). THE GAIN OF A PERSON'S OWN FACTOR ON THE CHOICE TEMPERATURE: `decision/choose.py::temper`
    # reads it through the `choice_temper` row of `rosters.yaml: tables.capability_uses` (key `attr.mind.focus`, role `judgement`), and `_sample_order` multiplies
    # `choice_temperature` by the factor. ⚠ THE SIGN: `about_mid` rises with the attribute, so a temperature that falls with Focus is a NEGATIVE gain; the value the flip (B98)
    # sets is -0.5 (CR-93 §2's sweep, the least magnitude at which the low-Focus group strays more and the high-Focus group less at seeds 0 to 2). Must lie in (-1, 0].
    # `0` is the CONTROL and SHIPS: the factor is exactly 1.0 for every person and the draw is today's. [ASSUMPTION; medium; Jordan to correct; revert: the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-476 -- site: Fixtures temper_gain, graded `assumption`; the design names no live value to ship, so it is injected at the control and swept 0 / -0.5 / -0.75]
    temper_gain=0.0,                   # `H-476`, swept 0 (control, SHIPPED) / -0.5 (proposed) / -0.75
    # `H-477` (B10.30; `02_CHAR_goal_lean_on_its_own_question` edit 3). THE GAIN ON `aim`, THE SCORE TERM THAT IS THE GOAL'S OWN LEAN ON THE QUESTION IT RAISED:
    # `decision/choose.py::score_terms` adds `aim_gain * damp * Σ_axis to_axes(goal.pursuits)[axis] * align(verb, axis) * odds_weight` on a `need` question whose
    # `about` is a goal in `goals.yaml` that the person holds a live `commit` to, and 0.0 on every other question. Must be >= 0 (a negative gain would
    # score a goal's business AGAINST the goal). `0` is the CONTROL and SHIPS: `aim` is exactly 0.0 for every candidate and the query is never asked. The flip is B98's.
    # [ASSUMPTION; medium; Jordan to correct; revert: 0, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-477 -- site: Fixtures aim_gain, graded `assumption`; the design ships no live value, so it is injected at the control and swept 0 / 0.5 / 1 / 2]
    aim_gain=0.0,                      # `H-477`, swept 0 (control, SHIPPED) / 0.5 / 1 / 2
    # `H-478` (B10.31; `02_CHAR_what_an_act_risks` edit 4). THE GAIN ON `risk`, THE SCORE TERM FOR WHAT AN ACT MIGHT COST THE PERSON WHO DOES IT IN BODY OR FIELD:
    # `decision/choose.py::score_terms` adds `- risk_gain * exposed * (1 - chance) * (1 + body_band_penalty) * nerve` on a candidate whose row contests a prize
    # `rosters.yaml: bodily_prizes` lists, and 0.0 on every other. Must be >= 0 (a negative gain would pull a person toward danger). `0` is the CONTROL and SHIPS:
    # `risk` is exactly 0.0 for every candidate and the chance is never asked. The flip is B98's. The source's sweep points 0.5 and 1.0 are about ten times
    # the choice temperature's margins (CR-93 / B10.53 measured it): the readings that separate persons sit nearer 0.05 and 0.1.
    # [ASSUMPTION; medium; Jordan to correct; revert: 0, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-478 -- site: Fixtures risk_gain, graded `assumption`; the design ships no live value, so it is injected at the control and swept 0 / 0.05 / 0.1 / 1]
    risk_gain=0.0,                     # `H-478`, swept 0 (control, SHIPPED) / 0.05 / 0.1 / 1 (the source's top point)
    # `H-479` (B10.31). THE CHANCE `risk` READS WHERE THE ONE ODDS QUERY CANNOT SAY: an answer of `None` (a row whose prize provider carries no believed estimate, a band
    # its ladder lacks, another's act), and no query at all, read this in place of the believed chance. A fixture, not his belief: it is not a figure he holds, so no later
    # error on his belief (B10.80) is put on it. In [0, 1]. Read only at `risk_gain` > 0. [ASSUMPTION; low; Jordan to correct; revert: none needed, read only where the gain is live.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-479 -- site: Fixtures risk_unknown_chance, graded `assumption`; no document gives the chance of coming through a danger he cannot estimate, so the even chance is injected and swept 0.25 / 0.5 / 0.75]
    risk_unknown_chance=0.5,           # `H-479`, swept 0.25 / 0.5 (SHIPPED) / 0.75
    # `H-480` (B10.31). THE GAIN OF `nerve`, A PERSON'S OWN FACTOR ON THE `risk` TERM: `decision/choose.py::nerve` reads it through the `choice_exposure` row of
    # `rosters.yaml: tables.capability_uses` (role `judgement`, Spirit) and `risk` is multiplied by the factor; NO ROW SHIPS, so the factor is 1.0 for every person whatever
    # this holds. ⚠ THE SIGN, as `temper_gain`'s: `about_mid` rises with the attribute, so a danger that weighs LESS on the high-Spirit needs a NEGATIVE gain. Must lie in [-1, 0].
    # `0` is the CONTROL and SHIPS. [ASSUMPTION; medium; Jordan to correct; revert: the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-480 -- site: Fixtures nerve_gain, graded `assumption`; the design names no live value to ship, so it is injected at the control and swept 0 / -0.25 / -0.5]
    nerve_gain=0.0,                    # `H-480`, swept 0 (control, SHIPPED) / -0.25 / -0.5
    # `H-472` (B10.13; `16_PESSIMIST_CHAR_A` "The resolution, decided" 3; U1 F-43). HOW A CRISIS OF FAITH COMES OUT: `rule` is the CONTROL and SHIPS (today's
    # `person_q.conviction_after_crisis`: the branch is chosen by a rule over state the crisis already reads, nothing is rolled); `drawn` rolls one draw per
    # scarring act and reads the band from `rosters.yaml: tables.crisis_bands` (B10.14, B10.15). A value outside `rosters.yaml: crisis_arms` is refused at load.
    # A-24 rules that `drawn` ships; it ships once `crisis_obstacle` is calibrated, and the flip is B98's. [ASSUMPTION; medium; Jordan to correct; revert: `rule`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-472 -- site: Fixtures crisis_arm, graded `assumption`; A-24 rules `drawn` and its obstacle has no shipped literal, so the arm is injected at the control and swept rule / drawn at the lightest obstacle / drawn at the heaviest]
    crisis_arm="rule",                 # `H-472`, swept rule (control, SHIPPED) / drawn at the lightest obstacle level / drawn at the heaviest
    # `H-473` (B10.13; same source, "no shipped literal"). THE OBSTACLE A CRISIS IS ROLLED AGAINST, a level of `rosters.yaml: difficulty_levels` (sized by
    # `difficulty_ob`), read by the emitter at `crisis_arm: drawn` (B10.15). `None` is the SHIPPED value: its number is set by the joint calibration of A-5, A-6, A-7
    # and A-26 (B98), and until then the term is absent; at `drawn` with `None` the emitter raises, naming B98. [ASSUMPTION; medium; Jordan to correct; revert: `None`, absent.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-473 -- site: Fixtures crisis_obstacle, graded `assumption`; no document gives a level, so it is absent at the control and swept over B05's four difficulty levels]
    crisis_obstacle=None,              # `H-473`, swept plain / routine / demanding / hard; None (SHIPPED, absent until B98)
    # B10.57 (`IS-B2-CHAR-02` step 5). THE COMPOSITION ROLES WHOSE NPC PARTY DECIDES A CHOICE BY `decision/decider.py::make_decider`: a wrapper passes that decider as its module's
    # `decide=` only for a role named here and a party the host does not play (`decider.decides_for`); for any other role the module runs its interim policy as it does
    # today. Each name is a role of `references/module_contracts.yaml`'s `composition_roles:` (refused at load otherwise). `()` is the CONTROL and SHIPS: no role is named, no
    # wrapper passes a decider. The first role is listed by the batch that makes its module accept `decide=` (B16 the duel round, B20 the field's commander, B24 the hearing), each a declared mover there.
    npc_decider_roles=(),
    # `H-481` (B10.58; `IS-B2-CHAR-07`, A-108). THE LARGEST STORED MANNER OFFSET A CAST ROW MAY AUTHOR: `data/cast.py::manner_offset_of` refuses a `manner:` value outside
    # `+-` this, at build (the seeder hands it in: `cast` cannot import this module). 0.15 is CL-PERSON's draft (`proposals/2026-10-24-character-layers-v2.md` section 2). No row authors an
    # offset today (`references/npc_registry.yaml`'s `manner:` header says why). [ASSUMPTION; medium; Jordan to correct; revert: none needed.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-481 -- site: Fixtures manner_offset_bound, graded `assumption`; CL-PERSON drafts +-0.15 and no live reading fixes it, so it is injected and swept 0.1 / 0.15 / 0.3]
    manner_offset_bound=0.15,          # `H-481`, swept 0.1 / 0.15 (SHIPPED, CL-PERSON's draft) / 0.3
    # `H-483` (B10.65; `U5a_CHAR_self_knowledge_is_a_belief` edit 6 (a)). THE LEAST A TOLD `self:<key>` CLAIM MUST WEIGH FOR HIM TO TAKE IT UP: `queries/person_q.py::knows_self` reads a
    # told claim by `teller_weight` (his regard for the teller, in `[0, 1]`) and counts it only at or above this; a claim he made of himself (no chain) is never weighed. `0.0` is the
    # CONTROL and SHIPS: every told claim is taken up, as an unweighed read does, and the fixture is read only where a told self-claim is the best he holds. [ASSUMPTION; medium; Jordan to correct; revert: 0.0.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-483 -- site: Fixtures self_told_floor, graded `assumption`; no document gives how far he must credit a teller before he believes a thing of himself, so it is injected at the control and swept 0 / 0.5 / 0.75]
    self_told_floor=0.0,               # `H-483`, swept 0 (control, SHIPPED) / 0.5 / 0.75
    # `H-496` (B11.66; `18_DETERMINISM_notice_is_a_draw` edit 6). WHETHER A BYSTANDER'S SEEING A DEED IS A DRAW, AND HOW HARD IT IS TO SEE: `notice_arm` `off` is the CONTROL and SHIPS (every pair
    # `observers_for` admits deposits, today's fan); `on` draws each non-party witness of a deed once (`epistemic.py::notice`, read at `loop/witness.py::witness`), at the obstacle `notice_ob` names --
    # a member of `rosters.yaml: difficulty_levels`, sized by `difficulty_ob` -- plus one level where the channel is not presence, one where the kind is covert, and the doer's live cover's
    # quality. An arm outside `rosters.yaml: notice_arms` is refused at read; a level outside the roster is refused at load. B11.67 flips the arm when the gate reads; B98 sets the level.
    # [ASSUMPTION; medium; Jordan to correct: the starting level `routine` -- basis: OBS's control arm uses `routine`; revert: `notice_arm: off`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-496 -- site: Fixtures notice_ob and notice_arm, graded `assumption`; the source gives the obstacle's member as "set at calibration" and the arm as `off` until its gate reads, so both are injected, the arm at the control and the level swept over B05's four difficulty levels]
    notice_arm="off",                  # `H-496`, swept off (control, SHIPPED) / on
    notice_ob="routine",               # `H-496`, swept plain / routine (SHIPPED) / demanding / hard
    # B24p.04 (V2 p2 §K): THE PROCEEDING'S OWN FIFTY-FOUR SETTINGS, each `[ASSUMPTION; Jordan to correct]`, read through `seam/wrappers/sigma.py::proceeding_dials`.
    # Every setting ships V2's value. B24p.04 left fifteen at the CONTROL (the levels `fit_level` and `answer_level` None; `repeat_step`, `esteem_step`, `off_step`,
    # `ploy_step`, `grain_strain`, `start_step`, `crowd_lean`, `heckle`, `room_level`, `heard_step`, `gap_step`, `weary_step` and `awe_step` at 0, the model's `CONTROL_ZERO`);
    # B24p.23 wrote V2's shipped value on each, and each line's comment names the control it left. Readers: `seam/wrappers/sigma.py::proceeding_dials`. `yield_track` and `sympathy_step` are cut (V2 p4 §L 3, §K C-dead) and are not here.
    # ---- the speech
    # [ASSUMPTION; Jordan to correct; revert: `None`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-861 -- site: Fixtures fit_level, graded `assumption`; V2 p2 §K gives "strong" and names the control `None`, and no document derives either, so it is injected at V2's shipped value (the control is `None`) and swept None / strong / major]
    fit_level="strong",                   # `H-861`, swept None / strong / major (V2's value, SHIPPED here; the control is None)
    # [ASSUMPTION; Jordan to correct; revert: `None`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-862 -- site: Fixtures answer_level, graded `assumption`; V2 p2 §K gives "moderate" and names the control `None`, and no document derives either, so it is injected at V2's shipped value (the control is `None`) and swept None / moderate / strong]
    answer_level="moderate",                # `H-862`, swept None / moderate / strong (V2's value, SHIPPED here; the control is None)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-863 -- site: Fixtures repeat_step, graded `assumption`; V2 p2 §K gives 0.35 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.175 / 0.35]
    repeat_step=0.35,                  # `H-863`, swept 0.0 / 0.175 / 0.35 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-864 -- site: Fixtures sense_step, graded `assumption`; V2 p2 §K gives 0.15 and no document derives it, so it is injected and swept 0.075 / 0.15 / 0.3]
    sense_step=0.15,                  # `H-864`, swept 0.075 / 0.15 / 0.3 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-865 -- site: Fixtures involve, graded `assumption`; V2 p2 §K gives 0.3 and no document derives it, so it is injected and swept 0.15 / 0.3 / 0.6]
    involve=0.3,                      # `H-865`, swept 0.15 / 0.3 / 0.6 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-866 -- site: Fixtures esteem_step, graded `assumption`; V2 p2 §K gives 0.2 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.1 / 0.2]
    esteem_step=0.2,                  # `H-866`, swept 0.0 / 0.1 / 0.2 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-867 -- site: Fixtures show, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    show=1.0,                         # `H-867`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-868 -- site: Fixtures off_step, graded `assumption`; V2 p2 §K gives 1.0 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.5 / 1.0]
    off_step=1.0,                     # `H-868`, swept 0.0 / 0.5 / 1.0 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-869 -- site: Fixtures admit_step, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    admit_step=0.5,                   # `H-869`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-870 -- site: Fixtures contempt_step, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    contempt_step=1.0,                # `H-870`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-871 -- site: Fixtures ploy_step, graded `assumption`; V2 p2 §K gives 1.5 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.75 / 1.5]
    ploy_step=1.5,                    # `H-871`, swept 0.0 / 0.75 / 1.5 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-872 -- site: Fixtures grain_strain, graded `assumption`; V2 p2 §K gives 0.5 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.25 / 0.5]
    grain_strain=0.5,                 # `H-872`, swept 0.0 / 0.25 / 0.5 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-873 -- site: Fixtures heard_step, graded `assumption`; V2 p2 §K gives 0.05 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.025 / 0.05]
    heard_step=0.05,                   # `H-873`, swept 0.0 / 0.025 / 0.05 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-874 -- site: Fixtures heard_floor, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    heard_floor=0.5,                  # `H-874`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-875 -- site: Fixtures gap_step, graded `assumption`; V2 p2 §K gives 0.25 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.125 / 0.25]
    gap_step=0.25,                     # `H-875`, swept 0.0 / 0.125 / 0.25 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-876 -- site: Fixtures weary_step, graded `assumption`; V2 p2 §K gives 0.5 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.25 / 0.5]
    weary_step=0.5,                   # `H-876`, swept 0.0 / 0.25 / 0.5 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-877 -- site: Fixtures stay_base, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    stay_base=1.0,                    # `H-877`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-878 -- site: Fixtures stay_per_will, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    stay_per_will=0.5,                # `H-878`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-879 -- site: Fixtures awe_step, graded `assumption`; V2 p2 §K gives 0.5 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.25 / 0.5]
    awe_step=0.5,                     # `H-879`, swept 0.0 / 0.25 / 0.5 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-880 -- site: Fixtures comfort_step, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    comfort_step=0.5,                 # `H-880`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-881 -- site: Fixtures rel_gain, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    rel_gain=0.5,                     # `H-881`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-882 -- site: Fixtures flop, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    flop=0.5,                         # `H-882`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-883 -- site: Fixtures invite, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    invite=0.5,                       # `H-883`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # ---- the press
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-884 -- site: Fixtures press_ob, graded `assumption`; V2 p2 §K gives 1.25 and no document derives it, so it is injected and swept 0.625 / 1.25 / 2.5]
    press_ob=1.25,                    # `H-884`, swept 0.625 / 1.25 / 2.5 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-885 -- site: Fixtures press_pull, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    press_pull=1.0,                   # `H-885`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-886 -- site: Fixtures rattle_pull, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    rattle_pull=0.5,                  # `H-886`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-887 -- site: Fixtures wear, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    wear=0.5,                         # `H-887`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-888 -- site: Fixtures rattle_gain, graded `assumption`; V2 p2 §K gives 1.5 and no document derives it, so it is injected and swept 0.75 / 1.5 / 3.0]
    rattle_gain=1.5,                  # `H-888`, swept 0.75 / 1.5 / 3.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-889 -- site: Fixtures rebound, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    rebound=1.0,                      # `H-889`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-890 -- site: Fixtures reactance, graded `assumption`; V2 p2 §K gives 0.75 and no document derives it, so it is injected and swept 0.5 / 0.75 / 1.0]
    reactance=0.75,                   # `H-890`, swept 0.5 / 0.75 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-891 -- site: Fixtures room_level, graded `assumption`; V2 p2 §K gives 0.5 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.25 / 0.5]
    room_level=0.5,                   # `H-891`, swept 0.0 / 0.25 / 0.5 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-892 -- site: Fixtures heckle, graded `assumption`; V2 p2 §K gives 1.0 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.5 / 1.0]
    heckle=1.0,                       # `H-892`, swept 0.0 / 0.5 / 1.0 (V2's value, SHIPPED here; the control is 0.0)
    # ---- conceding
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-893 -- site: Fixtures concede_step, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    concede_step=1.0,                 # `H-893`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-894 -- site: Fixtures consent_at, graded `assumption`; V2 p2 §K gives 2.5 and no document derives it, so it is injected and swept 1.25 / 2.5 / 5.0]
    consent_at=2.5,                   # `H-894`, swept 1.25 / 2.5 / 5.0 (V2's value, SHIPPED here)
    # ---- the room and the reading
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-895 -- site: Fixtures crowd_at, graded `assumption`; V2 p2 §K gives 12.0 and no document derives it, so it is injected and swept 6.0 / 12.0 / 24.0]
    crowd_at=12.0,                    # `H-895`, swept 6.0 / 12.0 / 24.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-896 -- site: Fixtures crowd_lean, graded `assumption`; V2 p2 §K gives 0.2 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 0.1 / 0.2]
    crowd_lean=0.2,                   # `H-896`, swept 0.0 / 0.1 / 0.2 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-897 -- site: Fixtures mood_scale, graded `assumption`; V2 p2 §K gives 5.0 and no document derives it, so it is injected and swept 2.5 / 5.0 / 10.0]
    mood_scale=5.0,                   # `H-897`, swept 2.5 / 5.0 / 10.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-898 -- site: Fixtures read_scale, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, so it is injected and swept 0.5 / 1.0 / 2.0]
    read_scale=1.0,                   # `H-898`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-899 -- site: Fixtures read_blur, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    read_blur=2.0,                    # `H-899`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-900 -- site: Fixtures read_noise, graded `assumption`; V2 p2 §K gives 0.3 and no document derives it, so it is injected and swept 0.15 / 0.3 / 0.6]
    read_noise=0.3,                   # `H-900`, swept 0.15 / 0.3 / 0.6 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-901 -- site: Fixtures bias_step, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    bias_step=2.0,                    # `H-901`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-902 -- site: Fixtures relevance, graded `assumption`; V2 p2 §K gives 1 and no document derives it, so it is injected and swept 0 / 0.5 / 1]
    relevance=1,                      # `H-902`, swept 0 / 0.5 / 1 (V2's value, SHIPPED here)
    # ---- the close
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-903 -- site: Fixtures track_step, graded `assumption`; V2 p2 §K gives 0.2 and no document derives it, so it is injected and swept 0.1 / 0.2 / 0.4]
    track_step=0.2,                   # `H-903`, swept 0.1 / 0.2 / 0.4 (V2's value, SHIPPED here)
    # ---- the NPC's temper
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-904 -- site: Fixtures temper_step, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    temper_step=0.5,                  # `H-904`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-905 -- site: Fixtures temper_break, graded `assumption`; V2 p2 §K gives 0.75 and no document derives it, so it is injected and swept 0.5 / 0.75 / 1.0]
    temper_break=0.75,                # `H-905`, swept 0.5 / 0.75 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-906 -- site: Fixtures temper_cool, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    temper_cool=0.5,                  # `H-906`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-907 -- site: Fixtures grain, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    grain=2.0,                        # `H-907`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-908 -- site: Fixtures grudge, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    grudge=2.0,                       # `H-908`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-909 -- site: Fixtures pride, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    pride=2.0,                        # `H-909`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # ---- the host
    # [ASSUMPTION; Jordan to correct; revert: `0.0`, the control.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-910 -- site: Fixtures start_step, graded `assumption`; V2 p2 §K gives 2.0 and names the control `0.0`, and no document derives either, so it is injected at V2's shipped value (the control is `0.0`) and swept 0.0 / 1.0 / 2.0]
    start_step=2.0,                   # `H-910`, swept 0.0 / 1.0 / 2.0 (V2's value, SHIPPED here; the control is 0.0)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-911 -- site: Fixtures presume_step, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    presume_step=2.0,                 # `H-911`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-912 -- site: Fixtures power_scale, graded `assumption`; V2 p2 §K gives 2.0 and no document derives it, so it is injected and swept 1.0 / 2.0 / 4.0]
    power_scale=2.0,                  # `H-912`, swept 1.0 / 2.0 / 4.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-913 -- site: Fixtures strain_fade, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, so it is injected and swept 0.25 / 0.5 / 1.0]
    strain_fade=0.5,                  # `H-913`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-914 -- site: Fixtures recuse_at, graded `assumption`; V2 p2 §K gives 0.25 and no document derives it, so it is injected and swept 0.125 / 0.25 / 0.5]
    recuse_at=0.25,                   # `H-914`, swept 0.125 / 0.25 / 0.5 (V2's value, SHIPPED here)
    # B24p.04: THE FOLD'S TABLE (V2 p2 §K, `sc2/host.py::FOLD`): twenty-four coefficients, each `[ASSUMPTION; Jordan to correct]`. The module never reads one; the fold does,
    # from B24p.24 (`fold_rig_price`, the rig's price in the arranger's choice), B27.28 (regard and pursuits) and B33.51 (standing, legitimacy and strife).
    # ---- fold: regard
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-915 -- site: Fixtures fold_carried, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_carried=0.1,                 # `H-915`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-916 -- site: Fixtures fold_accord, graded `assumption`; V2 p2 §K gives 0.15 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.075 / 0.15 / 0.3]
    fold_accord=0.15,                 # `H-916`, swept 0.075 / 0.15 / 0.3 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-917 -- site: Fixtures fold_unmoved, graded `assumption`; V2 p2 §K gives 0.05 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.025 / 0.05 / 0.1]
    fold_unmoved=0.05,                # `H-917`, swept 0.025 / 0.05 / 0.1 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-918 -- site: Fixtures fold_accuser, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_accuser=0.1,                 # `H-918`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-919 -- site: Fixtures fold_acquitted, graded `assumption`; V2 p2 §K gives 0.2 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.1 / 0.2 / 0.4]
    fold_acquitted=0.2,               # `H-919`, swept 0.1 / 0.2 / 0.4 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-920 -- site: Fixtures fold_heard, graded `assumption`; V2 p2 §K gives 0.03 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.015 / 0.03 / 0.06]
    fold_heard=0.03,                  # `H-920`, swept 0.015 / 0.03 / 0.06 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-921 -- site: Fixtures fold_contumacy, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_contumacy=0.1,               # `H-921`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-922 -- site: Fixtures fold_pressed, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_pressed=0.1,                 # `H-922`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-923 -- site: Fixtures fold_witness, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_witness=0.1,                 # `H-923`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-924 -- site: Fixtures fold_lost, graded `assumption`; V2 p2 §K gives 0.05 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.025 / 0.05 / 0.1]
    fold_lost=0.05,                   # `H-924`, swept 0.025 / 0.05 / 0.1 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-925 -- site: Fixtures fold_grudge_rig, graded `assumption`; V2 p2 §K gives 0.3 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.15 / 0.3 / 0.6]
    fold_grudge_rig=0.3,              # `H-925`, swept 0.15 / 0.3 / 0.6 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-926 -- site: Fixtures fold_reception, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_reception=0.1,               # `H-926`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-927 -- site: Fixtures fold_brute, graded `assumption`; V2 p2 §K gives 0.2 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.1 / 0.2 / 0.4]
    fold_brute=0.2,                   # `H-927`, swept 0.1 / 0.2 / 0.4 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-928 -- site: Fixtures fold_wrong, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_wrong=0.1,                   # `H-928`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # ---- fold: legitimacy and standing
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-929 -- site: Fixtures fold_legit_ruling, graded `assumption`; V2 p2 §K gives 0.1 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.05 / 0.1 / 0.2]
    fold_legit_ruling=0.1,            # `H-929`, swept 0.05 / 0.1 / 0.2 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-930 -- site: Fixtures fold_legit_brute, graded `assumption`; V2 p2 §K gives 0.4 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.2 / 0.4 / 0.8]
    fold_legit_brute=0.4,             # `H-930`, swept 0.2 / 0.4 / 0.8 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-931 -- site: Fixtures fold_legit_wrong, graded `assumption`; V2 p2 §K gives 0.2 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.1 / 0.2 / 0.4]
    fold_legit_wrong=0.2,             # `H-931`, swept 0.1 / 0.2 / 0.4 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-932 -- site: Fixtures fold_legit_fall, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.25 / 0.5 / 1.0]
    fold_legit_fall=0.5,              # `H-932`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none named, V2 gives it no control (the sweep's other points in its H row are the alternatives).]
    # [JUSTIFIED: engine/season/hole_register.yaml H-933 -- site: Fixtures fold_rig_price, graded `assumption`; V2 p2 §K gives 0.25 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.125 / 0.25 / 0.5]
    fold_rig_price=0.25,              # `H-933`, swept 0.125 / 0.25 / 0.5 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-934 -- site: Fixtures fold_partial_price, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.25 / 0.5 / 1.0]
    fold_partial_price=0.5,           # `H-934`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-935 -- site: Fixtures fold_standing, graded `assumption`; V2 p2 §K gives 0.5 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.25 / 0.5 / 1.0]
    fold_standing=0.5,                # `H-935`, swept 0.25 / 0.5 / 1.0 (V2's value, SHIPPED here)
    # ---- fold: the fold's thresholds
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-936 -- site: Fixtures fold_strife_ease, graded `assumption`; V2 p2 §K gives 0.25 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.125 / 0.25 / 0.5]
    fold_strife_ease=0.25,            # `H-936`, swept 0.125 / 0.25 / 0.5 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-937 -- site: Fixtures fold_merits_at, graded `assumption`; V2 p2 §K gives 1.0 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.5 / 1.0 / 2.0]
    fold_merits_at=1.0,               # `H-937`, swept 0.5 / 1.0 / 2.0 (V2's value, SHIPPED here)
    # [ASSUMPTION; Jordan to correct; revert: none needed, nothing reads it.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-938 -- site: Fixtures fold_fade, graded `assumption`; V2 p2 §K gives 0.25 and no document derives it, and the fold reads it only from B24p.24 (the rig's price), B27.28 and B33.51, so it is injected and swept 0.125 / 0.25 / 0.5]
    fold_fade=0.25,                   # `H-938`, swept 0.125 / 0.25 / 0.5 (V2's value, SHIPPED here)
    # `speech_blend` (a POINTER, no field): Reason's share of a speech's dice is two columns tuned as one table -- `rosters.yaml: grounds[*].reason` (B24p.01, 1.0 on every ground at the control) and
    # `arrangements.yaml` rows' `reason_lean` (B24p.03, 0 on every row at the control); B24p.23 writes V2's model column of each (`sc2/host.py::GROUNDS`, `::RITES`).
    # [JUSTIFIED: engine/season/hole_register.yaml H-939 -- site: Fixtures speech_blend (a pointer row, no field), graded `assumption`; the two columns are one blend and are swept together as a scale on V2's column, 0 (control) / 0.5 / 1]
    # `H-620` (B21b.01; IN-36 (a), ED-IN-0317). THE INTERIM TEST CAP ON MARCHES: at most this many `march`es are ADMITTED in one season (one `w.tick`) into each
    # territory, a march on a settlement counted against the territory that contains it, uniform for every marcher, civil-war marches included. It is the
    # `march_cap` conjunct of `march`'s cell (`verb_table.yaml`), read by the one admission path (`loop/resolve.py::_admits`) through the stems `march.nth`
    # and `march.cap` (`queries/world_q.py::marches_into`). `0` or unset is NO CAP: the control, and the revert.
    # A-103 (2026-11-12): the ruled test limit; a claim to a territory is an occasion, never a gate (`IS-B3-FA-04`).
    # [ASSUMPTION; medium; Jordan to correct; revert: `0`, no cap.]
    # [JUSTIFIED: engine/season/hole_register.yaml H-620 -- site: Fixtures march_cap_per_territory, graded `assumption`; ED-IN-0317 rules the limit and gives one march a season, so it ships at 1 and is swept 0 (control, no cap) / 1 / 2]
    march_cap_per_territory=1,         # `H-620`, swept 0 (control, no cap) / 1 (SHIPPED, IN-36 (a)) / 2
)

#: `H-424`'s two arms by name, the shipped one first: `calibrated` is `DEFAULT_FIXTURES`' own table (one copy), `control` is `DIFFICULTY_OB_CONTROL`.
DIFFICULTY_OB_ARMS = {"calibrated": DEFAULT_FIXTURES.get("difficulty_ob"), "control": DIFFICULTY_OB_CONTROL}


def load() -> None:
    """`data.load_all()`'s hook: refuse a `tables.capability_uses` row naming a Fixture this registry does not register.
    It lives here and not in `rosters.py` because this module imports `rosters` (the other way would close an import cycle)."""
    from .rosters import check_capability_fixtures
    check_capability_fixtures(dict(DEFAULT_FIXTURES._v))
    arm, obstacle = DEFAULT_FIXTURES.get("crisis_arm"), DEFAULT_FIXTURES.get("crisis_obstacle")
    if arm not in CRISIS_ARMS or (obstacle is not None and obstacle not in DIFFICULTY_LEVELS):
        raise Forbidden(f"`Fixtures crisis_arm` is {arm!r} and `crisis_obstacle` is {obstacle!r}", "data/fixtures.py",
                        needs=f"an arm of `rosters.yaml: crisis_arms` {sorted(CRISIS_ARMS)} and an obstacle that is None or a level of `difficulty_levels` {list(DIFFICULTY_LEVELS)}",
                        law="B10.13 (H-472, H-473) -- the arm is a closed set and the obstacle is a level the ladder names, never a number made up here")
    from engine.substrate import composition
    unknown = [r for r in DEFAULT_FIXTURES.get("npc_decider_roles") if r not in composition.ROLES]
    if unknown:
        raise Forbidden(f"`Fixtures npc_decider_roles` names {unknown}, which `references/module_contracts.yaml: composition_roles` does not register", "data/fixtures.py",
                        needs=f"roles of the composition registry {sorted(composition.ROLES)}",
                        law="B10.57 -- a role no wrapper carries is a setting read by nothing, and the decider would never be passed")
    levels, sized = DIFFICULTY_LEVELS, tuple(DEFAULT_FIXTURES.get("difficulty_ob"))
    if sized != levels:
        raise Forbidden(f"`Fixtures difficulty_ob` sizes {list(sized)}, and `rosters.yaml: difficulty_levels` names {list(levels)}", "data/fixtures.py",
                        needs="one size per difficulty level, in the roster's order",
                        law="B05.14 -- a level with no size is read by nothing, a size for no level is read by nothing; the roster is the closed set")
    for arm, arm_sizes in DIFFICULTY_OB_ARMS.items():
        if tuple(arm_sizes) != levels:
            raise Forbidden(f"`DIFFICULTY_OB_ARMS[{arm!r}]` sizes {list(arm_sizes)}, and `rosters.yaml: difficulty_levels` names {list(levels)}", "data/fixtures.py",
                            needs="one size per difficulty level, in the roster's order, in every arm",
                            law="T13 edit 1 -- the arms are one table at two sizes; an arm that skips a level answers for it with a KeyError mid-season")
    if DEFAULT_FIXTURES.get("notice_ob") not in DIFFICULTY_LEVELS:
        raise Forbidden(f"`Fixtures notice_ob` is {DEFAULT_FIXTURES.get('notice_ob')!r}", "data/fixtures.py",
                        needs=f"a level of `difficulty_levels` {list(DIFFICULTY_LEVELS)}",
                        law="B11.66 (H-496) -- the notice obstacle is a level the ladder names, sized by `difficulty_ob`, never a number made up here")
    kinds, stakes = set(roster("tenure_kinds")), set(DEFAULT_FIXTURES.get("stakes_ob"))
    if stakes != kinds:
        raise Forbidden(f"`Fixtures stakes_ob` sizes {sorted(stakes)}, and `rosters.yaml: tenure_kinds` names {sorted(kinds)}", "data/fixtures.py",
                        needs="one size per Tenure kind",
                        law="T13 T4 -- stakes are keyed by Tenure kind; a kind with no size is read by nothing, a size for no kind is read by nothing")
