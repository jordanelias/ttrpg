"""`season.data.fixtures` -- the harness fixtures and the matter-economy tables, extracted from
`shape.py` (step 3 of the decomposition, a PURE MOVE: no behaviour changed, only where the code
lives).

Owns `Fixtures` (S42.2.1's inject/grade/sweep registry: *"never invent a constant. Inject it,
declare it a harness fixture at `grade: assumption`, name the injection site, run a 3-point
sweep, and treat A VERDICT THAT FLIPS ACROSS THE SWEEP AS ITSELF A FINDING"*), the matter
economy's three roster-backed tables and their loader (`_load_matter_tables` / `WEAR_RATES`,
`BAND_FLOORS`, `SUBSISTENCE_WEIGHTS`, `SITE_YIELD`), and `DEFAULT_FIXTURES`, the baseline
instance built from all of it.

⚠ `_load_matter_tables` SITS BETWEEN `Fixtures` AND `DEFAULT_FIXTURES` HERE TOO, FOR THE SAME
REASON IT DID IN `shape.py`. `DEFAULT_FIXTURES` reads three of its values (`wear_per_season`,
`band_floors`, `subsistence_weight`) OFF `rosters.yaml` rather than as literals (`W8` --
splitting them into the registry would otherwise "put one declaration in two files"; reading the
data instead keeps it at one), so it cannot be built until those tables have loaded, and
`Fixtures` must exist first because `DEFAULT_FIXTURES` is an instance of it. The order is: class,
then loader, then baseline -- moving all three together keeps that dependency in one file
instead of re-splitting it across an import.
"""

from __future__ import annotations

from typing import Any

from ..gaps import Forbidden, Ungraded
from .rosters import roster, roster_map, table

class Fixtures:
    """S42.2.1: never invent a constant. Inject it, declare it a harness fixture at
    `grade: assumption`, name the injection site, run a 3-point sweep, and treat A VERDICT
    THAT FLIPS ACROSS THE SWEEP AS ITSELF A FINDING.

    REV 2 added `wear_per_season` (per SITE KIND, with NO SILENT DEFAULT -- S42.2.1 names a
    wear table with a silent default as the exact prior sin), `confidence_default`, and
    `entrenchment_seasons`. It REMOVED `caller_supplied_max_depth`: S39.3 says the depth cap
    has NO DEFAULT, and a default relocated into a default-argument object is still a default."""

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
        # ⚠ ROUTED THROUGH `get()`, AND THE BYPASS WAS LOAD-BEARING ON A GREEN CHECK. This read
        # `self._v` directly, so `self.reads` was never incremented and `claim_decay_per_season`
        # was INVISIBLE to R5 and to `W9`'s check 3 -- the two guards whose whole job is "no fill
        # off the register". Check 3 was green BECAUSE of the bypass: route the read properly and
        # it fails with `missing == ["claim_decay_per_season"]` unless the fixture is named in a
        # register row's `site:`. A guard that cannot see the thing it guards is not a weak guard,
        # it is an absent one (§0.1 point 2). Found by the adversarial pass.
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

    ⚠ THESE WERE LITERALS IN `DEFAULT_FIXTURES` AND PLAN `W8` ASKS FOR THEM AS REGISTRY ROWS. The
    comment that stood beside them objected, reasonably, that *"splitting them into rosters.yaml
    would put one declaration in two files"* — and the answer is that the fixture READS the data
    rather than restating it, so there is still exactly one declaration and it is the data.

    ⚠ THE CHECKS ARE THE POINT, not the relocation. A wear or weight table whose keys drift from
    the roster is §42.2.1's worked sin arriving through a data edit instead of through a literal:
    an unregistered kind that ANSWERS. Both directions are checked — a rate for a kind no roster
    carries, and a site kind with no rate."""
    kinds = set(roster("site_kinds"))
    rates = roster_map("wear_per_season", "rates")
    floors = table("band_floors")
    weights = roster_map("subsistence_weight", "weights")
    for name, got in (("wear_per_season", set(rates)), ("band_floors", set(floors))):
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

WEAR_RATES, BAND_FLOORS, SUBSISTENCE_WEIGHTS, SITE_YIELD = _load_matter_tables()

DEFAULT_FIXTURES = Fixtures(
    # S48: condition is an int on an EXPORTED scale. S22 assigns the scale to `params`, and the
    # in-chain params document "proposes NO VALUES", so this is a fixture. Injection site: here.
    # [JUSTIFIED: engine/season/hole_register.yaml H-06 -- `site: Fixtures condition_scale`, graded `assumption`; the mechanism is sourced and the magnitude is injected here and swept]
    condition_scale=1000,
    # RULED TWICE. #353 §26.3 puts the budget at "~5"; Jordan ruled 2026-09-02 that the UNIT is
    # the SCENE and the number is 5 -- *"5 scenes for a character to play per season"*. A band is
    # not an integer; this is the integer the instrument runs on, and A31 sweeps it because the
    # verdict moves with it.
    # ⚠ `W17` RENAMED THIS FROM `act_budget`. #353 §26.3's prose counts ACTS throughout and the
    # ruling re-states it in scenes: "a wounded duke gets fewer SCENES than a healthy one". The
    # spray argument survives the noun change unaltered -- five scenes each spent petitioning is
    # exactly the triage the budget exists to create -- but the key must not keep saying `act`,
    # because a name is where the next reader learns what the number counts.
    # [JUSTIFIED: engine/season/hole_register.yaml H-10 -- *the SCENE budget as an integer of the ruled band ~5*; #353 §26.3 gives the band, Jordan's 2026-09-02 ruling the unit, and a band is not an integer]
    scene_budget=5,
    # S20: the ledger cap L. Params-owned; no in-chain value.
    # [JUSTIFIED: engine/season/hole_register.yaml H-09 -- `site: Fixtures ledger_cap (L) · view_k (K) · confidence_default`; S20 names L, no in-chain value exists, 200 is injected and swept]
    ledger_cap=200,
    # S18: "at most K claim ids from the holder's OWN ledger -- BUILT, NOT FILTERED".
    # [JUSTIFIED: engine/season/hole_register.yaml H-09, the same row as `ledger_cap` above; S18 names K and the magnitude is injected and swept]
    view_k=12,
    # S22 assigns `wear per site kind` to params. NO in-chain table exists, so every kind the
    # instrument touches is declared here and an unregistered kind RAISES (see Fixtures.wear).
    # roster-exempt: Fixtures keys. `Fixtures` IS the registry for numbers and raises on an
    # unregistered kind, so the kinds are already declared data; splitting them into
    # rosters.yaml would put one declaration in two files. ⚠ `site_kinds` belongs in
    # rosters.yaml when W8 builds H-07's per-kind table, and not before.
    # ⚠ `W8` MOVED THE TABLE TO `rosters.yaml` AND THIS READS IT. The literal that stood here
    # carried an objection to splitting it out ("one declaration in two files"); the fixture
    # reading the data answers it, because the declaration is now in exactly one place and this
    # is not a copy of it. `Fixtures.wear` still refuses an unregistered kind.
    wear_per_season=WEAR_RATES,
    # S20: Claim.confidence. Rev 1 hardcoded 1, which degenerated the eviction comparator.
    confidence_default=100,
    # `W4` / `H-40`, THE THIRD LICENSED CLOCK (#353 `:864`). #353 licenses confidence decay at
    # MATTER and gives NO RATE, so this is an INJECTED DEFAULT with a `site:` and a three-point
    # sweep on the register, exactly as `H-09` treats the confidence default beside it. It is a
    # fixture rather than a literal so `Fixtures.claim_decay` can REFUSE when it is unregistered
    # — `wear`'s precedent, and S42.2.1's rule.
    # [JUSTIFIED: engine/season/hole_register.yaml H-40 -- the THIRD licensed clock; #353 licenses decay at MATTER and gives NO RATE, so the rate is injected with a `site:` and a three-point sweep]
    claim_decay_per_season=5,
    # `W6` / `H-33`. WHICH WITNESS CHANNELS ARE LIVE. `total` is the DEFAULT AND THE CONTROL --
    # it is #353's specified behaviour (S61: *"WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY
    # PERSON"*), so the sweep's control arm is the design as written rather than a baseline
    # somebody invented. The three points are `H-33`'s own declared sweep.
    fan_out_mode="total",
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
    obstacle_refusal_multiple=2,
    # S12.1 gates verbs on `condition` against per-kind band FLOORS. S22 assigns "band
    # coefficients" and "the obstacle floor" to params; the params document proposes NO
    # VALUES, so these are harness fixtures and A31c sweeps them. S42.2.1 names "three band
    # edges" as one of the four constants a prior instrument in the chain invented -- rev 2
    # fixed the other three and left these hardcoded in probe bodies, unswept.
    # roster-exempt: Fixtures keys, as `wear_per_season` above. These are H-08 and are swept.
    band_floors=BAND_FLOORS,          # `W8` -- `rosters.yaml: tables.band_floors`, `H-08`
    # ⚠ `W8` / `H-26`. #353 §22.3 names *"`season_factor`'s distribution"* as a value with NO
    # OWNER, and §25 says `yield` is *"blocked on"* it -- so the SHAPE ruled is a DISTRIBUTION and
    # what is injected here is a degenerate one. The sweep is on its value, which is the only axis
    # a constant has; a real distribution is a different hole and is not invented here.
    season_factor=1.0,                # `H-26`, swept 0.5 / 1 / 2
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
    # ⚠ THESE ARE A MOVE, NOT AN INVENTION, AND THE OLD HOME IS DELETED. They were
    # `transfer`'s `operand_defaults: {kind: grain, amount: 1}` in `verb_table.yaml` -- the
    # relocated form of `_req_transfer`'s two literals -- and that cell filled them AT THE FOLD,
    # under the person, for an act whose payload carried neither. Two owners of one value, and
    # the fold's copy would have admitted a `transfer` whose effect then raised on the operands
    # the precondition had invented for it. The values are carried across unchanged.
    # ⚠ THE COMMENT HERE READ *"`H-94`, swept with the amount below"* AND NOTHING SWEPT IT. Struck
    # by the `W-C` adversarial pass: every `.sweep(...)` in the instrument named
    # `default_transfer_amount`, and `H-94`'s `sweep: [0, 1, 3]` are INTEGERS, which cannot be
    # arms for a matter kind -- one `sweep:` field was carrying two declared fixtures and
    # `register.rule_R2` cannot see that, so R2 was green on an unswept default. It has its own
    # row now (`H-121`) and its own three arms, RUN: `grain` (stocked) · `salt` (a second stocked
    # kind, which proves the fixture reaches the effect -- the store that moves is the one it
    # names) · `coin` (registered in `rosters.yaml: matter_kinds`, produced by no site and held by
    # no rung: THE CONTROL, and the only arm that can flip the verdict, because
    # `WorldReader.read` returns 0 rather than UNKNOWN for a kind a rung does not hold, so
    # `0 >= amount` is False and the transfer REFUSES).
    # ⚠ AND THE POLARITY WAS INVERTED: the SWEPT fixture was the decision-inert one and this
    # UNSWEPT one is decision-live. Measured over all 89 corpus worlds -- `transfer` executes
    # 702 / refuses 21 at both `grain` and `salt`, and 0 / 723 at `coin`, where it leaves the
    # executed set entirely (6 verbs -> 5). The 702-execution headline does rest on this value.
    default_store_kind="grain",        # `H-121`, swept grain / salt / coin
    # ⚠ `0` IS THE CONTROL AND IT IS SWEPT FIRST. Nothing is spent, so scarcity never binds and
    # `stores >= 0` admits every giver: a run at this point shows how much of the transfer
    # behaviour rests on the default rather than on the world.
    default_transfer_amount=1,         # `H-94`, swept 0 / 1 / 3
    # `W-E` / `H-125`. HOW MUCH BODY A WOUND COSTS WHEN THE SCENE SAYS THE SUBJECT BLED AND DID
    # NOT GO DOWN. Part E's `writes:` names the CELL and never the VALUE, and no in-chain document
    # supplies this one -- so it is declared, defaulted and swept rather than chosen in a body,
    # which is what `H-114` measured the cost of (`harm` defaulted to the whole body, so a fold at
    # `Wounded` deleted the person). The default introduces NO CONSTANT: it scales the body by the
    # health fraction the ENGINE computed. `total` is the CONTROL and is the code exactly as it
    # stood before `W-E`. Injection site: this line, read by `_eff_kill`.
    wound_harm_model="scene_fraction",  # `H-125`, swept scene_fraction / total / none
)
