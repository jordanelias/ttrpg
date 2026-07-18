"""pr119_integrated_campaign.py — the cross-proposal, multi-season, world-state simulation
the other 7 pr119_governance adapters deliberately did NOT attempt: every other adapter in
this cluster tests one PR#119 item (or a tight pair) in isolation, with its own independent
random draws. That is real coverage, but it cannot see an INTERDEPENDENCY between two
proposals that only shows up when they share state over time — which is exactly what Jordan
asked this cluster to add after reviewing the first pass.

This adapter runs a real, persistent, multi-season campaign on ONE Goldenfurt Settlement
(goldenfurt_fixture.build_goldenfurt_settlement()), composing ALL 11 tested PR#119 items
(the 12th, §1.0b Recognition Fork, is a per-event choice with no season-to-season state to
compose and is left to its own dedicated adapter) plus the Pi homeostat, wired so later
mechanics read the REAL state earlier mechanics wrote — real systems/settlements/sim/ledger.py tag
writes, real systems/settlements/sim/registry.py Settlement fields (church_attention, pressure,
suspicion), and real systems/settlements/sim/infrastructure.py + systems/settlements/sim/registry.py functions
(seizure_ob_modifier, succeed_governor, province_accord, province_effective_prosperity) —
instead of each mechanic drawing its own independent random number every season.

Interdependencies this composition surfaces that no single-item adapter could:
  1. §1.0d Performance Audit and Goldenfurt's G606 recall cascade share the SAME per-season
     compliance signal (as in pr119_recognition_accountability.py), but here that signal also
     drives governor Standing, Za patron correlation, and the Pi homeostat's release term —
     one governor decision ripples through five mechanics, not two.
  2. §1.1a Clerk Capacity's hidden corruption counter sits on the exact same Orsk/Konrad
     bribery web npc_cast.md already authors ("Konrad takes Orsk's coin for advance levy
     notice") — modeled here as a chance that a Clerk-Corruption Investigate ALSO surfaces
     Konrad's own graft, writing the real `Leverage:konrad-corrupt` tag that event_deck.md's
     EVT-G606 already treats as the recall-defusing escape. A genuinely emergent finding: an
     unrelated PR#119 AP-economy mechanic can mechanically rescue a PR#119 accountability
     mechanic from firing, through a collision neither item's own text anticipates.
  3. §1.3b Bind the Cells writes REAL `Grudge`-family ledger tags; the Pi homeostat's
     `active_grudges` term reads `len(settlement.tags("Grudge"))` — a real accumulation, not
     an independent proxy draw as in pr119_pressure_homeostat.py's standalone version.
  4. §3.3c Seggio entrenchment is gated on the REAL `Settlement.church_attention` field
     (Wessel/G03's own arc, per npc_cast.md), not an invented counter.
  5. Every season registers Goldenfurt (+ one explicitly-labeled synthetic province-mate —
     see _SYNTHETIC_PROVINCE_MATE below) and calls the REAL `registry.province_accord()` /
     `province_effective_prosperity()` — settlement-scale churn actually propagating to
     province scale, the cross-scale direction PR#125's narrative sim never exercised in code.

`run_campaign(rng, params) -> (branch, stats)` is exposed as a public function so a
standalone statistics pass (see designs/audit/2026-07-12-pr119-harness-verification/
README.md "Interdependency & emergence" section) can gather full per-trial numeric world-
state (final Pi, ledger tag composition, recall rate, rescue rate, province Accord trend)
without duplicating this module's logic — the harness's own branch-count trace answers
"what happened," the stats pass answers "how much."

canon_row=None: this is a composition of 11 still-PROPOSED items; none has a CURRENT.md row.
contract_module=None: deliberately — this campaign spans BOTH `faction_politics` (§1.0d,
Clerk-Corruption-exposes-Konrad) and `settlement_layer` (everything else) contracts; no
single module_contracts.yaml row captures a cross-module composed campaign, and picking one
would misrepresent the scope as narrower than it is (see Adapter.contract_module's docstring
on this being a real, logged opt-out, not a placeholder).
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

_SKILL_DIR = Path(__file__).resolve().parents[4] / "skills" / "valoria-dice-model"
if str(_SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(_SKILL_DIR))
import valoria_dice  # noqa: E402

from systems.settlements.sim import infrastructure, registry  # noqa: E402

from ...adapter import Adapter, Outcome, register_adapter  # noqa: E402
from ...depth import DecisionPoint, Tier  # noqa: E402
from .goldenfurt_fixture import NPCS, build_goldenfurt_settlement  # noqa: E402
from .pr119_pressure_homeostat import _restore_toward  # noqa: E402 (single source of truth)
from .pr119_subnational_factions import FakeWorld  # noqa: E402 (single source of truth)

_KONRAD = NPCS["NPC-G06"]
_ORSK = NPCS["NPC-G02"]
# npc_cast.md "Timeline: N seasons" per NPC -- Hedda(G01)/Orsk(G02)/Wessel(G03)/Greta(G05)'s
# own ambition-firing cadence, reused here (not re-derived) to compute the Pi homeostat's
# real "ambitions in motion" term instead of a flat proxy rate.
_NPC_TIMELINES = {"NPC-G01": 4, "NPC-G02": 3, "NPC-G03": 4, "NPC-G05": 5}

# NOT a canon settlement -- a synthetic, explicitly-labeled test-scenario province-mate.
# registry.province_accord()/province_effective_prosperity() aggregate over a province's real
# member settlements (sim_build_spec.md §1: "the floor-average was always meant to do" this),
# which is DEGENERATE (single-member) with Goldenfurt alone in Kronmark. Static stats: this
# adapter's focus is Goldenfurt's dynamics, not authoring a second town's arc.
_SYNTHETIC_PROVINCE_MATE_SID = "S-TEST-KRONMARK-2"


@dataclass
class _GovernorState:
    standing: int = 5           # test-scenario 0-10 proxy; not a canon rank track
    pa_streak: int = 0          # §1.0d consecutive-miss streak
    clerk_capacity: int = 0     # §1.1a, 0-3 cap
    clerk_corruption: int = 0   # §1.1a hidden counter
    patron_standing: int = 5    # §3.3b Za patron proxy, 0-10
    guild_influence: int = 0    # §1.3c Ordenanza-ratify creep
    seggio_entrenched: bool = False
    recalled: bool = False
    recall_reason: str | None = None
    rescued_by_clerk_corruption: bool = False
    any_za_lapse: bool = False


def run_campaign(rng, params: dict) -> tuple[str, dict]:
    """Run one multi-season campaign trial. Returns (branch, stats) — see module docstring."""
    registry.reset_registry()
    infrastructure.reset_infrastructure()
    s = build_goldenfurt_settlement()
    mate = registry.Settlement(
        sid=_SYNTHETIC_PROVINCE_MATE_SID, name="(synthetic test-scenario province-mate)",
        stype="Village", province_id=s.province_id, prosperity=2, order=2,
    )
    registry.register_settlement(s)
    registry.register_settlement(mate)

    gov = _GovernorState()
    konrad_progress = 0
    npc_progress = {k: 0 for k in _NPC_TIMELINES}
    cell_size = params["cell_size"]
    n_cells = max(1, len(s.npc_ids) // cell_size)
    cell_stacks = [0] * n_cells
    seasons_survived = 0
    province_accord_trend = []

    for season in range(params["seasons"]):
        seasons_survived = season + 1

        # 1. Directive response (§1.4) -- the shared signal §1.0d and G606 both react to.
        #    §1.4's own response table: Comply "often strains the settlement (the Directive
        #    usually conflicts with a Need)"; Defy/Divert "protects the settlement" -- wired
        #    to the real Settlement.order field so province_accord() (step 9) aggregates a
        #    real, moving number instead of a flat, untouched stat.
        complied = rng.random() < params["p_comply"]
        if complied:
            gov.pa_streak = 0
            gov.standing = min(10, gov.standing + 1)
            if rng.random() < params["p_comply_strains_order"]:
                s.order = max(0, s.order - 1)
        else:
            s.suspicion += 1
            gov.pa_streak += 1
            konrad_progress = min(konrad_progress + _KONRAD["progress_cap_per_season"],
                                   _KONRAD["fires_threshold"])
            gov.standing = max(0, gov.standing - 1)
        pa_terminal = gov.pa_streak >= params["pa_demotion_streak"]

        # 2. §1.1a Clerk Capacity -- AP source + hidden corruption, cross-wired to Konrad's
        #    real bribery web (interdependency #2 in the module docstring).
        if rng.random() < params["p_retain_clerks"] and gov.clerk_capacity < params["cc_cap"]:
            gov.clerk_capacity += 1
        gov.clerk_corruption += gov.clerk_capacity
        p_discover = min(1.0, params["corruption_discovery_k"] * gov.clerk_corruption)
        corruption_exposed_konrad = False
        if rng.random() < p_discover and rng.random() < params["p_shared_discovery_hits_konrad"]:
            corruption_exposed_konrad = True
            s.add_tag("Leverage", "konrad-corrupt", created_season=season)

        # 3. §1.3a Compact -- real ledger write, exercising the confirmed silent-6th-family
        #    acceptance bug (pr119_ledger_family_collision.py) inside a live campaign.
        if rng.random() < params["p_negotiate_compact"]:
            s.add_tag("Compact", f"quota-s{season}", created_season=season,
                      ttl=params["compact_term"])

        # 4. §1.3b Bind the Cells -- real Grudge-family writes (interdependency #3).
        for i in range(n_cells):
            if rng.random() < params["p_infraction_per_cell_per_season"]:
                cell_stacks[i] += 1
                s.add_tag("Grudge", f"cell-{i}-s{season}", created_season=season, ttl=8)

        # 5. §1.3c Ordenanza Ratification -- periodic, real dice via Orsk (Gu-Std 3+ gate).
        if season % params["ordenanza_period"] == 0 and _ORSK["guild_standing"] >= 3:
            r = valoria_dice.roll_pool(params["amend_pool"], params["amend_tn"], rng)
            outcome = valoria_dice.classify_outcome(r, params["amend_ob"])
            if outcome in ("overwhelming", "success"):
                gov.guild_influence += 1
                s.add_tag("Precedent", f"ordenanza-ratified-s{season}", created_season=season)
            elif outcome == "failure":
                s.add_tag("Grudge", f"ordenanza-rejected-s{season}", created_season=season, ttl=8)

        # 6. §3.3b Za patron-lapse -- patron standing correlated with the governor's own
        #    standing (a weakening governor destabilizes who they've backed).
        gov.patron_standing = max(0, min(10, gov.patron_standing + (1 if complied else -1)))
        if gov.patron_standing < params["patron_lapse_threshold"]:
            if rng.random() < params["p_bargain_success"]:
                gov.patron_standing = min(10, gov.patron_standing + 2)
            else:
                gov.any_za_lapse = True

        # 7. §3.3c Seggio entrenchment -- gated on the REAL church_attention field
        #    (interdependency #4). On first crossing, seed the REAL infrastructure axis
        #    (Cathedral + Church Governor -- worst-case entrenchment, matching Wessel/G03's
        #    own arc goal per npc_cast.md) so the seizure_ob_modifier check below reflects
        #    genuine built state, not an assumption.
        if rng.random() < params["p_church_attention_rise"]:
            s.church_attention = min(10, s.church_attention + 1)
        if s.church_attention >= params["seggio_entrenchment_threshold"] and not gov.seggio_entrenched:
            gov.seggio_entrenched = True
            world = FakeWorld([s.sid])
            infrastructure.build_infrastructure(s.sid, "Cathedral", world=world)
            infrastructure.build_infrastructure(s.sid, "Church Governor", world=world)

        # 8. Pi homeostat -- REAL per-season terms derived from what fired this season, not
        #    independent proxy draws (interdependency #3).
        active_grudges = len(s.tags("Grudge"))
        for npc_id, timeline in _NPC_TIMELINES.items():
            if rng.random() < 0.5:
                npc_progress[npc_id] += 1
                if npc_progress[npc_id] >= timeline:
                    npc_progress[npc_id] = 0  # fires -> resets, per npc_cast.md's own cadence
        ambitions_in_motion = sum(1 for v in npc_progress.values() if v > 0)
        unserved_need = 0.0 if complied else params["unserved_need_pressure"]
        shock = (params["external_shock_magnitude"]
                 if rng.random() < params["p_external_shock"] else 0.0)
        release = params["player_release_magnitude"] if complied else 0.0
        s.pressure = max(0.0, min(10.0, (
            s.pressure + unserved_need
            + active_grudges * params["grudge_pressure_each"]
            + ambitions_in_motion * params["ambition_pressure_each"]
            + shock - release + _restore_toward(s.pressure)
        )))

        # 9. Province-scale aggregation (interdependency #5) -- real cross-scale propagation.
        province_accord_trend.append(registry.province_accord(s.province_id))

        # 10. Recall/demotion terminal check -- may be rescued by step 2's corruption exposure.
        if pa_terminal or konrad_progress >= _KONRAD["fires_threshold"]:
            if corruption_exposed_konrad:
                gov.rescued_by_clerk_corruption = True
                konrad_progress = 0
                gov.pa_streak = 0
                s.suspicion = max(0, s.suspicion - 2)
            else:
                gov.recalled = True
                gov.recall_reason = "performance_audit" if pa_terminal else "g606"
                registry.succeed_governor(s.sid, None, world=None, season=season)
                break

    if gov.recalled:
        branch = "recall_or_demotion_cascade"
    elif gov.rescued_by_clerk_corruption:
        branch = "rescued_by_corruption_discovery"
    elif s.pressure > 6.0 or gov.any_za_lapse or gov.seggio_entrenched:
        branch = "fracture_or_entrenchment_signal"
    else:
        branch = "stable_governance"

    seizure_mod = infrastructure.seizure_ob_modifier(s.sid, world=None) if gov.seggio_entrenched else None
    stats = {
        "branch": branch,
        "seasons_survived": seasons_survived,
        "final_pressure": s.pressure,
        "final_suspicion": s.suspicion,
        "compact_tag_count": len(s.tags("Compact")),
        "grudge_tag_count": len(s.tags("Grudge")),
        "recalled": gov.recalled,
        "recall_reason": gov.recall_reason,
        "rescued_by_corruption": gov.rescued_by_clerk_corruption,
        "guild_influence": gov.guild_influence,
        "za_lapsed": gov.any_za_lapse,
        "seggio_entrenched": gov.seggio_entrenched,
        "seggio_seizure_ob_modifier": seizure_mod,
        "final_province_accord": province_accord_trend[-1] if province_accord_trend else None,
        "final_province_prosperity": registry.province_effective_prosperity(s.province_id),
    }
    return branch, stats


@register_adapter("pr119_integrated_campaign")
class IntegratedCampaignAdapter(Adapter):
    contract_module = None  # see module docstring -- deliberately spans two module contracts
    canon_row = None
    registry_subsystem = "cross_cutting"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        params = {
            "seasons": 20,
            "p_comply": 0.5,
            "p_comply_strains_order": 0.4,
            "pa_demotion_streak": 3,
            "cc_cap": 3,
            "p_retain_clerks": 0.5,
            "corruption_discovery_k": 0.12,
            "p_shared_discovery_hits_konrad": 0.4,
            "p_negotiate_compact": 0.2,
            "compact_term": 6,
            "cell_size": 5,
            "p_infraction_per_cell_per_season": 0.35,
            "ordenanza_period": 3,
            "amend_pool": 6, "amend_tn": 7, "amend_ob": 2,
            "patron_lapse_threshold": 3,
            "p_bargain_success": 0.5,
            "p_church_attention_rise": 0.2,
            "seggio_entrenchment_threshold": 6,
            "grudge_pressure_each": 0.5,
            "ambition_pressure_each": 0.5,
            "unserved_need_pressure": 1.5,
            "p_external_shock": 0.15,
            "external_shock_magnitude": 1.0,
            "player_release_magnitude": 1.0,
        }
        provenance = {
            "seasons": "test-scenario value, not canon-derived: ~5 year-arcs (governance_"
                "play_redesign_v1.md §1.1: a year-arc is 4 seasons), enough headroom for "
                "every composed mechanic's terminal state to reach",
            "p_comply": "test-scenario value, not canon-derived: the shared per-season "
                "compliance signal every composed mechanic below reacts to",
            "p_comply_strains_order": "PROVISIONAL: systems/settlements/governance_play_"
                "redesign_v1.md §1.4 response table -- Comply 'often strains the settlement "
                "(the Directive usually conflicts with a Need)'; rate itself is test-scenario "
                "(not numerically stated) -- wires the real Settlement.order field so "
                "province_accord() aggregates a moving number, not a flat one",
            "pa_demotion_streak": "PROVISIONAL: systems/factions/faction_politics_v30.md "
                "§1.0d -- 3-season triplicate-ledger demotion trigger",
            "cc_cap": "PROVISIONAL: governance_play_redesign_v1.md §1.1a -- 'CC, 0-3'",
            "p_retain_clerks": "test-scenario value, not canon-derived",
            "corruption_discovery_k": "test-scenario value, not canon-derived: see "
                "pr119_clerk_capacity.py's identical parameter for the same documented "
                "simplification of an unspecified discovery curve",
            "p_shared_discovery_hits_konrad": "test-scenario value, not canon-derived: models "
                "how often a Clerk-Corruption Investigate also surfaces Konrad's SEPARATE "
                "bribe-taking (npc_cast.md NPC-G06) rather than assuming automatic overlap",
            "p_negotiate_compact": "test-scenario value, not canon-derived",
            "compact_term": "PROVISIONAL: governance_play_redesign_v1.md §1.3a -- 'locking a "
                "Treasury/troop figure for 4-6 seasons' (upper-bound test-scenario choice)",
            "cell_size": "PROVISIONAL: §1.3b -- 'five-household cells'",
            "p_infraction_per_cell_per_season": "test-scenario value, not canon-derived",
            "ordenanza_period": "test-scenario value, not canon-derived: an ordenanza is an "
                "NPC ambition-engine action (§1.3c), not a fixed cadence in canon",
            "amend_pool": "test-scenario value, not canon-derived: see pr119_guild_ladder.py",
            "amend_tn": "test-scenario value matching engine/params/core.md's Standard TN=7 (see "
                "pr119_guild_ladder.py's verified citation of the same constant)",
            "amend_ob": "PROVISIONAL: governance_play_redesign_v1.md §1.3c -- 'Amend ... Ob 2'",
            "patron_lapse_threshold": "test-scenario value, not canon-derived",
            "p_bargain_success": "test-scenario value, not canon-derived",
            "p_church_attention_rise": "test-scenario value, not canon-derived",
            "seggio_entrenchment_threshold": "test-scenario value, not canon-derived: "
                "Settlement.church_attention is a real 0-10 field (registry.py); the "
                "threshold at which it triggers Seggio-relevant entrenchment is not "
                "canon-specified",
            "grudge_pressure_each": "PROVISIONAL: goldenfurt_slice/sim_build_spec.md §5 -- "
                "'+0.5 per Grudge tag'",
            "ambition_pressure_each": "PROVISIONAL: same §5 -- '+0.5 per NPC with progress > "
                "0 and not firing'",
            "unserved_need_pressure": "test-scenario value, not canon-derived (see "
                "pr119_pressure_homeostat.py's identical parameter)",
            "p_external_shock": "test-scenario value, not canon-derived",
            "external_shock_magnitude": "test-scenario value, not canon-derived",
            "player_release_magnitude": "test-scenario value, not canon-derived",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="campaign_emergent_outcome", default_tier=Tier.MAJOR,
                branches=["stable_governance", "recall_or_demotion_cascade",
                          "fracture_or_entrenchment_signal", "rescued_by_corruption_discovery"],
                justification="a full multi-season campaign composing 11 PR#119 items on "
                               "shared, persistent world state, gating a real recall/"
                               "succession call (registry.succeed_governor) -- the harness "
                               "rubric's own definition of campaign-defining, tier-3",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        branch, stats = run_campaign(rng, params)
        return Outcome(decision_point.name, stats, {"branch": branch})
