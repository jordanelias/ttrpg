"""pr119_event_deck_engine.py — a real, card-based event-deck engine over Goldenfurt, built in
response to the explicit ask: "settlements [should] be able to fall into ruin or prosper or
remain as they are depending upon how well they are governed and how lucky/unlucky their
events [are]." `pr119_integrated_campaign.py` composes PR#119's *mechanics* (ledger families,
Clerk Capacity, Bind the Cells...) but drives them with independent ad-hoc probability draws,
not real event-deck content — it cannot produce a genuine PROSPER outcome because nothing in
it ever grows Prosperity. This module fixes that by implementing the actual deck.

**Thirteen of Goldenfurt's real 28 cards**, transcribed with citations from
`systems/settlements/goldenfurt_slice/event_deck.md` (the "Spine cards" full-schema section plus
selected "Remaining cards" compact entries), spanning all 7 card families so the family-weighted
draw bias is real, not token: G101, G201, G204 (Petition/Friction, full schema), G301, G303
(Opportunity, POSITIVE — the deck's own growth levers, absent from `pr119_integrated_campaign.py`
entirely), G401, G402, G404 (Crisis), G502, G505 (Intrigue, full schema), G601, G606 (Ambition, full
schema), G702 (Thread, compact). The other 15 cards are NOT transcribed: 12 have only one-line
"compact" summaries too thin to simulate honestly, and the deliberate 13-card sample already
covers every family. Not claimed as full-deck coverage — see the adapter docstring's "What this
is not."

**The real draw mechanic** (event_deck.md's own header): `n = 1 + floor(Pi/3)` cards drawn per
season, low-Pi seasons biased toward Opportunity/Ambition, high-Pi seasons biased toward Crisis
— transcribed verbatim, not invented.

**Skill vs. luck, separated explicitly:**
- LUCK = which cards are eligible to draw this season (trigger predicates over real state) and
  which of the eligible pool actually draws (weighted random).
- SKILL = `governance_skill` (0-1 dial): the probability the governor picks each card's
  best-available response (`skill_weight`, this module's own judgment call on which response a
  competent governor would prefer — documented per-card, not asserted as canon). A skilled
  governor is NOT guaranteed a good outcome (some cards have no good response, e.g. Concede vs
  Force under G401), and an unskilled governor is not guaranteed a bad one — this is deliberate:
  the ask was for luck and skill to BOTH matter, not for skill to fully determine the outcome.

canon_row=None: event_deck.md is part of the PROPOSED goldenfurt_slice (2026-06-23), no
CURRENT.md row. contract_module="settlement_layer" (same binding as the other settlement-scope
adapters in this cluster).
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

_SKILL_DIR = Path(__file__).resolve().parents[4] / "skills" / "valoria-dice-model"
if str(_SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(_SKILL_DIR))
import valoria_dice  # noqa: E402

from systems.settlements.sim import registry  # noqa: E402
from systems.settlements.sim.registry import STAT_MAX, STAT_MIN  # noqa: E402

from ...adapter import Adapter, Outcome, register_adapter  # noqa: E402
from ...depth import DecisionPoint, Tier  # noqa: E402
from .goldenfurt_fixture import build_goldenfurt_settlement  # noqa: E402
from .pr119_pressure_homeostat import _restore_toward  # noqa: E402 (single source of truth)

_EVENT_DECK_DOC = "systems/settlements/goldenfurt_slice/event_deck.md"


def _clamp_stat(v: int) -> int:
    return max(STAT_MIN, min(STAT_MAX, v))


@dataclass
class _Ctx:
    """Mutable per-trial state the card triggers/responses read and write, beyond what
    lives directly on the real Settlement object (registry.Settlement has no fields for
    per-NPC Disposition or Ambition progress — those live in npc_cast.md prose, not the
    built schema — so this dataclass is this adapter's own, explicitly non-canon, tracking
    of exactly the values the 13 transcribed cards' triggers/responses reference)."""
    directive: str = "Extract"
    hedda_disposition: int = 1       # npc_cast.md NPC-G01 starting Disposition
    orsk_disposition: int = 1        # NPC-G02
    hedda_progress: int = 0          # ambition progress toward EVT-G601 (fires at >=4)
    konrad_progress: int = 0         # toward EVT-G606 (fires at >=4, capped +1/season)
    orsk_progress: int = 0           # toward EVT-G602 (not transcribed here, tracked for realism)
    hostiles_seeded: bool = False    # event_deck.md G201-defy: "seeds G404 if hostiles in province"
    cooldowns: dict = field(default_factory=dict)  # card_id -> season it becomes eligible again


@dataclass
class CardResponse:
    name: str
    skill_weight: float  # this adapter's judgment of how favorable a skilled governor rates this
    apply: Callable[["_Ctx", registry.Settlement, "GameEvents", object], None]


@dataclass
class Card:
    card_id: str
    family: str
    cooldown: int
    trigger: Callable[["_Ctx", registry.Settlement], bool]
    responses: list


class GameEvents:
    """Accumulates a human-readable log of what fired each season -- consumed by
    death_spiral_log.py's tracer, not by the harness's own trace (which only wants a
    branch classification)."""
    def __init__(self):
        self.log: list = []

    def note(self, season: int, msg: str) -> None:
        self.log.append(f"s{season}: {msg}")


def _r_hold_court(ctx, s, ev, rng):
    r = valoria_dice.roll_pool(6, 7, rng)
    if valoria_dice.classify_outcome(r, 2) in ("overwhelming", "success"):
        s.pressure = max(0.0, s.pressure - 2)
        s.add_tag("Precedent", "only-sons-exempt")
        ctx.hedda_disposition += 1
        ev.note(0, "G101 Hold Court succeeded -> Precedent:only-sons-exempt, Pi-2")
    else:
        ev.note(0, "G101 Hold Court failed the Ob-2 roll -> no relief granted")


def _r_comply_levy(ctx, s, ev, rng):
    s.pressure = min(10.0, s.pressure + 1)
    s.add_tag("Grudge", "hedda-levy")
    ctx.hedda_disposition -= 2


def _r_bargain(ctx, s, ev, rng):
    ctx.konrad_progress = ctx.konrad_progress  # no suspicion; Bargain's whole point per §1.4


def _r_ignore_petition(ctx, s, ev, rng):
    s.pressure = min(10.0, s.pressure + 2)
    s.add_tag("Reputation", "weak")
    s.add_tag("Grudge", "mertha")


G101 = Card(
    card_id="G101", family="Petition", cooldown=2,
    trigger=lambda ctx, s: ctx.directive == "Extract" and s.order <= 3,
    responses=[
        CardResponse("hold_court", 0.8, _r_hold_court),
        CardResponse("comply_levy", 0.2, _r_comply_levy),
        CardResponse("bargain", 0.5, _r_bargain),
        CardResponse("ignore", 0.0, _r_ignore_petition),
    ],
)


def _r_g201_comply(ctx, s, ev, rng):
    s.order = _clamp_stat(s.order - 1)
    s.pressure = max(0.0, s.pressure - 1)


def _r_g201_bargain(ctx, s, ev, rng):
    r = valoria_dice.roll_pool(6, 7, rng)
    if valoria_dice.classify_outcome(r, 2) in ("overwhelming", "success"):
        s.pressure = max(0.0, s.pressure - 1)
        ev.note(0, "G201 Bargain succeeded -> halved levy, Pi-1, no suspicion")
    else:
        s.suspicion += 1
        ev.note(0, "G201 Bargain failed -> treated as a soft Defy")


def _r_g201_defy(ctx, s, ev, rng):
    s.suspicion += 1
    s.pressure = min(10.0, s.pressure + 1)
    ctx.konrad_progress = min(ctx.konrad_progress + 1, 4)
    s.add_tag("Reputation", "just")
    ctx.hostiles_seeded = True  # event_deck.md G201: "seeds G404 if hostiles in province"


G201 = Card(
    card_id="G201", family="Friction", cooldown=0,
    trigger=lambda ctx, s: ctx.directive == "Extract",
    responses=[
        CardResponse("comply", 0.4, _r_g201_comply),
        CardResponse("bargain", 0.7, _r_g201_bargain),
        CardResponse("defy", 0.3, _r_g201_defy),
    ],
)


def _r_g404_militia_defend(ctx, s, ev, rng):
    ctx.hostiles_seeded = False  # resolved -- a fresh G201-defy is needed to reseed
    r = valoria_dice.roll_pool(6, 7, rng)
    if valoria_dice.classify_outcome(r, 2) in ("overwhelming", "success"):
        s.add_tag("Precedent", "militia-held-the-ford")
        ev.note(0, "G404 Militia defend succeeded -> settlement held")
    else:
        s.defense = _clamp_stat(s.defense - 1)
        ev.note(0, "G404 Militia defend failed -> Defense-1")


def _r_g404_fortify(ctx, s, ev, rng):
    ctx.hostiles_seeded = False
    s.defense = _clamp_stat(s.defense + 1)


def _r_g404_abandon(ctx, s, ev, rng):
    ctx.hostiles_seeded = False
    s.prosperity = _clamp_stat(s.prosperity - 2)
    s.add_tag("Reputation", "weak")


G404 = Card(
    # event_deck.md: "Defense <=1 + hostile military in province ... mandatory scene ...
    # Often the cost of defying G201" -- hostile presence isn't a tracked province-military
    # field in this cluster, so eligibility is gated on the real G201-defy seed (per the
    # deck's own text) rather than an invented standalone probability. cooldown=3 is
    # test-scenario (event_deck.md's compact table states no cooldown for G404).
    card_id="G404", family="Crisis", cooldown=3,
    trigger=lambda ctx, s: ctx.hostiles_seeded and s.defense <= 1,
    responses=[
        CardResponse("militia_defend", 0.6, _r_g404_militia_defend),
        CardResponse("emergency_fortify", 0.8, _r_g404_fortify),
        CardResponse("abandon", 0.1, _r_g404_abandon),
    ],
)


def _r_g204_consent(ctx, s, ev, rng):
    s.order = _clamp_stat(s.order + 1)


def _r_g204_clergy(ctx, s, ev, rng):
    s.order = _clamp_stat(s.order + 1)
    s.church_attention = min(10, s.church_attention + 1)
    s.add_tag("Debt", "church-dependence")


def _r_g204_decline(ctx, s, ev, rng):
    pass  # Order stays low; Pi-neutral per the v1.1 fix cited in event_deck.md


def _r_g204_bargain(ctx, s, ev, rng):
    s.order = _clamp_stat(s.order + 1)
    s.add_tag("Leverage", "parish-favour")


G204 = Card(
    card_id="G204", family="Friction", cooldown=3,
    trigger=lambda ctx, s: s.order <= 2 and s.religious_building == "Chapel",
    responses=[
        CardResponse("keep_order_consent", 0.9, _r_g204_consent),
        CardResponse("keep_order_clergy", 0.3, _r_g204_clergy),
        CardResponse("decline", 0.5, _r_g204_decline),
        CardResponse("bargain", 0.6, _r_g204_bargain),
    ],
)


def _r_g301_sponsor(ctx, s, ev, rng):
    s.add_tag("Reputation", "generous")
    s.pressure = max(0.0, s.pressure - 1)


def _r_g301_attend(ctx, s, ev, rng):
    s.pressure = max(0.0, s.pressure - 0.5)


def _r_g301_skip(ctx, s, ev, rng):
    s.add_tag("Grudge", "local-actors")
    s.pressure = min(10.0, s.pressure + 0.5)


G301 = Card(
    card_id="G301", family="Opportunity", cooldown=4,
    trigger=lambda ctx, s: s.order >= 4 and s.prosperity >= 4 and s.pressure <= 4,
    responses=[
        CardResponse("sponsor", 0.8, _r_g301_sponsor),
        CardResponse("attend", 0.6, _r_g301_attend),
        CardResponse("skip", 0.1, _r_g301_skip),
    ],
)


def _r_g303_ally(ctx, s, ev, rng):
    ctx.konrad_progress = min(ctx.konrad_progress + 1, 4)  # Crown notices your growing power
    s.add_tag("Debt", "hedda-alliance")
    ev.note(0, "G303 Hedda alliance accepted -> Stage-2->3 progress, Konrad+1")


def _r_g303_decline(ctx, s, ev, rng):
    ctx.hedda_disposition -= 1


G303 = Card(
    card_id="G303", family="Opportunity", cooldown=6,
    trigger=lambda ctx, s: ctx.hedda_disposition >= 2,
    responses=[
        CardResponse("ally", 0.7, _r_g303_ally),
        CardResponse("decline", 0.3, _r_g303_decline),
    ],
)


def _r_g401_force(ctx, s, ev, rng):
    s.order = _clamp_stat(s.order + 1)
    s.add_tag("Grudge", "town")


def _r_g401_concede(ctx, s, ev, rng):
    s.pressure = max(0.0, s.pressure - 3)
    s.suspicion += 1
    ctx.hedda_disposition += 1


def _r_g401_hedda_mediates(ctx, s, ev, rng):
    s.pressure = max(0.0, s.pressure - 3)
    s.add_tag("Debt", "owed-to-hedda")


def _g401_responses(ctx):
    resp = [
        CardResponse("keep_order_force", 0.2, _r_g401_force),
        CardResponse("concede", 0.6, _r_g401_concede),
    ]
    if ctx.hedda_disposition >= 2:
        resp.append(CardResponse("hedda_mediates", 0.9, _r_g401_hedda_mediates))
    return resp


G401 = Card(
    card_id="G401", family="Crisis", cooldown=0,
    trigger=lambda ctx, s: s.pressure >= 8 and (s.has_tag("Grudge", "hedda-levy")
                                                  or s.has_tag("Grudge", "mertha")),
    responses=[],  # resolved dynamically via _g401_responses -- see draw loop
)


def _r_g402_sponsor_relief(ctx, s, ev, rng):
    s.prosperity = _clamp_stat(s.prosperity + 1)
    s.order = _clamp_stat(s.order + 1)


def _r_g402_beg_crown(ctx, s, ev, rng):
    s.add_tag("Debt", "crown-relief")


def _r_g402_let_orsk_profit(ctx, s, ev, rng):
    ctx.orsk_progress += 1


G402 = Card(
    card_id="G402", family="Crisis", cooldown=4,
    trigger=lambda ctx, s: s.prosperity <= 0,
    responses=[
        CardResponse("sponsor_relief", 0.8, _r_g402_sponsor_relief),
        CardResponse("beg_crown", 0.5, _r_g402_beg_crown),
        CardResponse("let_orsk_profit", 0.2, _r_g402_let_orsk_profit),
    ],
)


def _r_g502_investigate(ctx, s, ev, rng):
    r = valoria_dice.roll_pool(6, 7, rng)
    if valoria_dice.classify_outcome(r, 2) in ("overwhelming", "success"):
        s.add_tag("Leverage", "konrad-corrupt")
        ev.note(0, "G502 Investigate succeeded -> Leverage:konrad-corrupt")
    ctx.orsk_disposition -= 1


def _r_g502_confront(ctx, s, ev, rng):
    r = valoria_dice.roll_pool(6, 7, rng)
    if valoria_dice.classify_outcome(r, 2) in ("overwhelming", "success"):
        ev.note(0, "G502 Confront Orsk: won -> Guild Influence-1")
    else:
        ctx.konrad_progress = min(ctx.konrad_progress + 1, 4)


def _r_g502_concede(ctx, s, ev, rng):
    ctx.orsk_progress += 1


G502 = Card(
    card_id="G502", family="Intrigue", cooldown=3,
    trigger=lambda ctx, s: ctx.orsk_disposition <= -2,
    responses=[
        CardResponse("investigate", 0.8, _r_g502_investigate),
        CardResponse("confront", 0.4, _r_g502_confront),
        CardResponse("concede_charter", 0.2, _r_g502_concede),
    ],
)


def _r_g505_bury_warn(ctx, s, ev, rng):
    ctx.hedda_disposition += 3
    s.add_tag("Debt", "hedda-owes-you")


def _r_g505_bury_hold(ctx, s, ev, rng):
    s.add_tag("Leverage", "hedda-compromised")


def _r_g505_expose(ctx, s, ev, rng):
    s.pressure = min(10.0, s.pressure + 3)
    s.add_tag("Reputation", "harsh")


G505 = Card(
    card_id="G505", family="Intrigue", cooldown=None,  # "excludes: fires once"
    trigger=lambda ctx, s: s.has_tag("Leverage", "konrad-corrupt"),
    responses=[
        CardResponse("bury_warn_hedda", 0.8, _r_g505_bury_warn),
        CardResponse("bury_hold", 0.3, _r_g505_bury_hold),
        CardResponse("expose", 0.1, _r_g505_expose),
    ],
)


def _r_g702_investigate(ctx, s, ev, rng):
    pass  # Wealth+1 (abstract, not a tracked Settlement field this cluster models)


def _r_g702_mend(ctx, s, ev, rng):
    s.prosperity = _clamp_stat(s.prosperity + 1)


G702 = Card(
    card_id="G702", family="Thread", cooldown=5,
    # Thread Proximity isn't a tracked field in this cluster (real Thread-layer state lives
    # outside systems/settlements/sim/) -- a flat, documented test-scenario eligibility chance stands in.
    trigger=lambda ctx, s: True,
    responses=[
        CardResponse("investigate", 0.4, _r_g702_investigate),
        CardResponse("mend", 0.7, _r_g702_mend),
    ],
)

# G601 and G606 are state-RESOLVED (no player response menu) per event_deck.md -- handled
# directly in the draw loop below, not via the generic CardResponse dispatch.
_DECK = [G101, G201, G204, G301, G303, G401, G402, G404, G502, G505, G702]
_FAMILY_LOW_PI_BIAS = {"Opportunity", "Ambition"}
_FAMILY_HIGH_PI_BIAS = {"Crisis"}


def _choose_response(card: Card, ctx: _Ctx, s: registry.Settlement, governance_skill: float, rng) -> CardResponse:
    responses = _g401_responses(ctx) if card.card_id == "G401" else card.responses
    best = max(responses, key=lambda r: r.skill_weight)
    if rng.random() < governance_skill:
        return best
    return responses[rng.randrange(len(responses))]


def run_deck_campaign(rng, params: dict) -> tuple:
    """Run one multi-season campaign driven by the real 12-card Goldenfurt deck subset.
    Returns (branch, stats). Public so death_spiral_log.py can reuse it without duplicating
    the deck logic."""
    registry.reset_registry()
    s = build_goldenfurt_settlement()
    registry.register_settlement(s)
    ctx = _Ctx()
    ev = GameEvents()
    governance_skill = params["governance_skill"]
    directives = ["Extract", "Tax", "Suppress", "Host"]
    recalls = 0
    seasons_survived = 0
    prosperity_trend = []
    order_trend = []
    pressure_trend = []

    for season in range(params["seasons"]):
        seasons_survived = season + 1
        ctx.directive = directives[rng.randrange(len(directives))]

        # Neglect decay: governance_play_redesign_v1.md §1.1 -- "you cannot do everything the
        # settlement needs in one season -- you must prioritize, and what you neglect festers
        # (P5, feeds the deck)." The 13-card subset only ever RAISES Prosperity through a card
        # response; nothing represents the AP a governor did NOT spend this season simply not
        # maintaining the town. This term is that gap's stand-in: a skill-inverse chance
        # (test-scenario formula, not canon-derived -- P5 states the principle, not a rate)
        # Prosperity drifts down absent active upkeep, so "ruin" is a genuinely reachable
        # outcome for sustained low-skill/low-luck play, not just a theoretical branch label.
        if rng.random() < 0.5 * (1.0 - governance_skill):
            s.prosperity = _clamp_stat(s.prosperity - 1)
        if rng.random() < 0.5 * (1.0 - governance_skill):
            s.order = _clamp_stat(s.order - 1)

        # event_deck.md header: "each season the deck draws 1 + floor(Pi/3) cards"
        n_draw = 1 + math.floor(s.pressure / 3)
        eligible = [c for c in _DECK
                    if ctx.cooldowns.get(c.card_id, -1) <= season and c.trigger(ctx, s)]

        def _weight(c):
            if s.pressure <= 3 and c.family in _FAMILY_LOW_PI_BIAS:
                return 2.0
            if s.pressure >= 7 and c.family in _FAMILY_HIGH_PI_BIAS:
                return 2.0
            return 1.0

        for _ in range(min(n_draw, len(eligible) or 1)):
            if not eligible:
                break
            weights = [_weight(c) for c in eligible]
            total = sum(weights)
            pick_roll = rng.random() * total
            acc = 0.0
            card = eligible[-1]
            for c, w in zip(eligible, weights):
                acc += w
                if pick_roll <= acc:
                    card = c
                    break
            eligible.remove(card)
            if card.cooldown is not None:
                ctx.cooldowns[card.card_id] = season + card.cooldown
            else:
                ctx.cooldowns[card.card_id] = 10**9  # "excludes: fires once"
            response = _choose_response(card, ctx, s, governance_skill, rng)
            response.apply(ctx, s, ev, rng)
            ev.note(season, f"{card.card_id} ({card.family}) -> {response.name}")

        # G601 -- state-resolved by relationship, per event_deck.md.
        if rng.random() < 0.5:
            ctx.hedda_progress += 1
        if ctx.hedda_progress >= 4:
            if s.has_tag("Debt", "hedda-owes-you"):
                ev.note(season, "G601 Hedda's Bid: allied -> your parliamentary proxy")
            elif s.has_tag("Grudge", "hedda-levy"):
                ev.note(season, "G601 Hedda's Bid: estranged -> anti-you reform platform")
            else:
                ev.note(season, "G601 Hedda's Bid: neutral outcome")
            ctx.hedda_progress = 0

        # G606 -- state-resolved, real recall/succession call (reuses registry.succeed_governor).
        if ctx.konrad_progress >= 4:
            if s.has_tag("Leverage", "konrad-corrupt"):
                s.suspicion = 0
                ctx.konrad_progress = 0
                ev.note(season, "G606: buried (Leverage:konrad-corrupt held)")
            elif rng.random() < params["p_submit_to_audit"]:
                s.suspicion = max(0, s.suspicion - 2)
                ctx.konrad_progress = max(0, ctx.konrad_progress - 2)
                ev.note(season, "G606: Submit to audit -> suspicion -2, post kept")
            else:
                r = valoria_dice.roll_pool(6, 7, rng)
                ob = 2 if s.has_tag("Reputation", "just") else 3
                if valoria_dice.classify_outcome(r, ob) in ("overwhelming", "success"):
                    ev.note(season, "G606: Recall scene won, post kept")
                    ctx.konrad_progress = 0
                else:
                    recalls += 1
                    registry.succeed_governor(s.sid, None, world=None, season=season)
                    ctx.konrad_progress = 0
                    ev.note(season, f"G606: Recall scene LOST -> governor replaced (recall #{recalls})")

        # Pi homeostat -- same CG-1 formula as pr119_pressure_homeostat.py/pr119_integrated_campaign.py.
        active_grudges = len(s.tags("Grudge"))
        s.pressure = max(0.0, min(10.0, s.pressure + 0.3 * active_grudges + _restore_toward(s.pressure)))

        prosperity_trend.append(s.prosperity)
        order_trend.append(s.order)
        pressure_trend.append(s.pressure)

    final_prosperity, final_order, final_pressure = s.prosperity, s.order, s.pressure
    if final_prosperity >= 4 and final_order >= 3 and final_pressure <= 5:
        branch = "prospering"
    elif final_prosperity <= 1 and (final_order <= 1 or final_pressure >= 7):
        branch = "ruined"
    elif recalls >= 3:
        branch = "collapsed_repeated_recalls"
    else:
        branch = "holding_steady"

    stats = {
        "branch": branch, "recalls": recalls, "seasons_survived": seasons_survived,
        "final_prosperity": final_prosperity, "final_order": final_order,
        "final_pressure": final_pressure,
        "prosperity_trend": prosperity_trend, "order_trend": order_trend,
        "pressure_trend": pressure_trend, "event_log": ev.log,
    }
    return branch, stats


@register_adapter("pr119_event_deck_engine")
class EventDeckEngineAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple:
        params = {
            "seasons": 20,
            "governance_skill": 0.5,
            "p_submit_to_audit": 0.5,
        }
        provenance = {
            "seasons": "test-scenario value, not canon-derived: matches "
                "pr119_integrated_campaign.py's horizon for comparability",
            "governance_skill": "test-scenario value, not canon-derived: the dial this "
                "adapter exists to test (see module docstring's 'skill vs luck' section)",
            "p_submit_to_audit": "test-scenario value, not canon-derived: event_deck.md's "
                "EVT-G606 states Submit-to-audit is 'always available', not its selection "
                "rate against the other resolution branches",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="deck_campaign_outcome", default_tier=Tier.MAJOR,
                branches=["prospering", "holding_steady", "ruined", "collapsed_repeated_recalls"],
                justification="a full multi-season campaign driven by real event-deck content, "
                               "gating real recall/succession calls -- campaign-defining, tier-3",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        branch, stats = run_deck_campaign(rng, params)
        return Outcome(decision_point.name, stats, {"branch": branch})
