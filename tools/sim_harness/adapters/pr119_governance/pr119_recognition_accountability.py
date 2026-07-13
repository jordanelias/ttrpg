"""pr119_recognition_accountability.py — provisional adapter testing PR#119's three
faction-rank accountability items (all PROPOSED, no sim code):
  - designs/provincial/faction_politics_v30.md §1.0b Recognition Fork (ED-FA-0019)
  - designs/provincial/faction_politics_v30.md §1.0c Court Attendance / Hostage-Kin (ED-FA-0020)
  - designs/provincial/faction_politics_v30.md §1.0d Patron-Sponsored Performance Audit (ED-FA-0021)

The load-bearing decision point is `performance_audit_vs_g606`. PR#125's reconciliation pass
(designs/audit/2026-07-12-settlement-season-stress-sim/reconciliation_with_existing_territory_work.md,
§A.2) claims §1.0d "likely DUPLICATES Goldenfurt's already-designed recall" — Goldenfurt's real
G606 "Bailiff's Report" cascade (event_deck.md), confirmed by the stress test's own NERS MERGE
verdict. That claim was argued in prose from reading both docs side by side; this decision point
tests it empirically by running §1.0d's triplicate-ledger cascade and G606's suspicion-progress
cascade off the SAME per-season compliance signal (both are, textually, reactions to "the
governor failed to satisfy the faction/Directive this season") and tallying how often they
co-fire within one trial window. High co-fire share is evidence FOR the merge recommendation;
this is a simplified model (see run_once docstring) — a scoping decision documented, not hidden.

canon_row=None throughout: none of these three items has a CURRENT.md row (all PROPOSED).
"""
from __future__ import annotations

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import NPCS

_KONRAD = NPCS["NPC-G06"]


@register_adapter("pr119_recognition_accountability")
class RecognitionAccountabilityAdapter(Adapter):
    contract_module = "faction_politics"  # references/module_contracts.yaml -> designs/provincial/faction_politics_v30.md
    canon_row = None  # all three items are PROPOSED, no CURRENT.md row yet
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        params = {
            "p_confirm": 0.5,          # §1.0b Confirm-vs-New-Grant split
            "p_skip_court": 0.3,       # §1.0c Court Attendance skip rate
            "p_comply": 0.5,           # per-season compliance draw feeding both cascades below
            "pa_demotion_streak": 3,   # §1.0d: "converts to ... Demotion Magnitude-1 ... after 3 seasons"
            "konrad_fire_threshold": _KONRAD["fires_threshold"],  # event_deck.md EVT-G606
            "konrad_progress_cap": _KONRAD["progress_cap_per_season"],
            "trial_seasons": 6,        # test-scenario: enough headroom for both terminal states to fire
        }
        provenance = {
            "p_confirm": "test-scenario value, not canon-derived: §1.0b describes Confirm/"
                "New-Grant as 'an explicit choice by the granting authority' with no stated "
                "base rate — 0.5 is a neutral default for exploring the branch space",
            "p_skip_court": "test-scenario value, not canon-derived: §1.0c states no base "
                "skip rate for the mandatory Standing-4+ Court Attendance",
            "p_comply": "test-scenario value, not canon-derived: the shared per-season "
                "compliance draw both cascades below react to — neither doc specifies a "
                "base compliance rate",
            "pa_demotion_streak": "PROVISIONAL: designs/provincial/faction_politics_v30.md "
                "§1.0d — 'It converts to an immediate Demotion Magnitude-1 trigger ... after "
                "3 seasons, bypassing the normal grace period'",
            "konrad_fire_threshold": "PROVISIONAL: designs/territory/goldenfurt_slice/"
                "event_deck.md EVT-G606 — 'fires when G06 progress >= 4'",
            "konrad_progress_cap": "PROVISIONAL: event_deck.md EVT-G606 — 'Konrad's advance "
                "is capped +1/season, see npc_cast G06'",
            "trial_seasons": "test-scenario value, not canon-derived: chosen so both the "
                "3-consecutive-season PA streak and the >=4-cumulative-season Konrad "
                "threshold have room to fire within one trial",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="recognition_fork", default_tier=Tier.MEDIUM,
                branches=["confirm", "new_grant"],
                justification="§1.0b: withholds or fires a rank's mechanical unlock — a "
                               "settlement/faction-scale write (Access/Hall Tier/Obligations), "
                               "not a locally-reversible single check",
            ),
            DecisionPoint(
                name="court_attendance_skip", default_tier=Tier.MEDIUM,
                branches=["attended", "skipped"],
                justification="§1.0c: a skip accrues the cross-scale Suspicion field at "
                               "double rate — a settlement-registry write, per the tier-2 rubric",
            ),
            DecisionPoint(
                name="performance_audit_vs_g606", default_tier=Tier.MAJOR,
                branches=["both_fire", "only_pa_fires", "only_g606_fires", "neither_fires"],
                justification="both terminal states gate a Demotion/Recall — campaign-"
                               "defining per the tier-3 rubric row, and this decision point "
                               "is the direct empirical test of the reconciliation doc's "
                               "'§1.0d duplicates Goldenfurt's recall' claim",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "recognition_fork":
            branch = "confirm" if rng.random() < params["p_confirm"] else "new_grant"
            return Outcome(decision_point.name, branch, {"branch": branch})

        if decision_point.name == "court_attendance_skip":
            branch = "skipped" if rng.random() < params["p_skip_court"] else "attended"
            return Outcome(decision_point.name, branch, {"branch": branch})

        if decision_point.name == "performance_audit_vs_g606":
            # Simplified shared-signal model: each season draws one compliance boolean that
            # BOTH cascades react to (a missed Obligation for §1.0d's triplicate ledger; a
            # Defy/shortfall for Konrad's G606 progress) — the textual overlap the
            # reconciliation doc points at. Real play has independent-but-correlated
            # triggers (§1.0d watches Required Obligations; G606 also watches Order and
            # Crown-contribution shortfall independently of Directive response) — collapsing
            # them to one shared draw is a deliberate simplification that tests the
            # DUPLICATION hypothesis directly rather than modeling every independent trigger
            # path; documented here, not hidden.
            pa_streak = 0
            pa_fired = False
            konrad_progress = 0
            konrad_fired = False
            for _season in range(params["trial_seasons"]):
                complied = rng.random() < params["p_comply"]
                if complied:
                    pa_streak = 0
                else:
                    pa_streak += 1
                    if pa_streak >= params["pa_demotion_streak"]:
                        pa_fired = True
                    konrad_progress = min(
                        konrad_progress + params["konrad_progress_cap"],
                        params["konrad_fire_threshold"],
                    )
                    if konrad_progress >= params["konrad_fire_threshold"]:
                        konrad_fired = True
            if pa_fired and konrad_fired:
                branch = "both_fire"
            elif pa_fired:
                branch = "only_pa_fires"
            elif konrad_fired:
                branch = "only_g606_fires"
            else:
                branch = "neither_fires"
            return Outcome(
                decision_point.name,
                {"pa_fired": pa_fired, "konrad_fired": konrad_fired},
                {"branch": branch},
            )

        raise ValueError(f"unknown decision point {decision_point.name!r}")
