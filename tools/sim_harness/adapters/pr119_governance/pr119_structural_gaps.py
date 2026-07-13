"""pr119_structural_gaps.py — provisional adapter turning two of the reconciliation doc's
"new reconciliation items" (designs/audit/2026-07-12-settlement-season-stress-sim/
reconciliation_with_existing_territory_work.md §C.3, §C.5) into live, re-runnable filesystem/
source checks instead of one-off prose claims:

  - §C.3 "Two event architectures, unreconciled": tests/sim/settlement_mgmt_stress_01/'s
    predicate-sweep model vs. governance_play_redesign_v1.md/goldenfurt_slice's stateful
    card-deck model — two different engines for "what happens to a settlement each season",
    both present in the repo with no reconciling decision.
  - §C.5 "PR#119's faction-standing items rest on inert substrate": §1.0b/c/d and the §1.8
    Mandate feedback all read Legitimacy/Popular Support (L/PS), which registry.py's own
    inline comment already calls PORT-BLOCKING/inert (ED-FA-0004) — "declared but NEVER READ
    OR WRITTEN anywhere in sim/".

Both decision points are deterministic (no rng draw) — they inspect real repo state, not a
sampled distribution — so they run at tier 1 (a single, locally-reversible check) per the
harness's own tier rubric, not tier 2/3.

canon_row=None: this adapter is itself a structural-audit tool over PROPOSED PR#119 items,
not a citation-bearing test of a single ratified mechanic.
"""
from __future__ import annotations

from pathlib import Path

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier

_REPO_ROOT = Path(__file__).resolve().parents[4]
_REGISTRY_PY = _REPO_ROOT / "sim" / "territory" / "registry.py"
_LEDGER_PY = _REPO_ROOT / "sim" / "territory" / "ledger.py"
_SETTLEMENT_PY = _REPO_ROOT / "sim" / "territory" / "settlement.py"
_PREDICATE_SWEEP_DIR = _REPO_ROOT / "tests" / "sim" / "settlement_mgmt_stress_01"
_CARD_DECK_DOC = _REPO_ROOT / "designs" / "territory" / "goldenfurt_slice" / "event_deck.md"


@register_adapter("pr119_structural_gaps")
class StructuralGapsAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        params = {
            "registry_py_path": str(_REGISTRY_PY.relative_to(_REPO_ROOT)),
            "ledger_py_path": str(_LEDGER_PY.relative_to(_REPO_ROOT)),
            "settlement_py_path": str(_SETTLEMENT_PY.relative_to(_REPO_ROOT)),
            "predicate_sweep_dir": str(_PREDICATE_SWEEP_DIR.relative_to(_REPO_ROOT)),
            "card_deck_doc": str(_CARD_DECK_DOC.relative_to(_REPO_ROOT)),
        }
        provenance = {k: "test-scenario value, not a canon citation: a literal repo path "
                      "this adapter inspects at run time, per the module docstring"
                      for k in params}
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="lps_inert_check", default_tier=Tier.MINOR,
                branches=["inert_confirmed", "wired"],
                justification="a single deterministic source-text check, locally reversible "
                               "(re-running it costs nothing) — tier-1 per the rubric",
            ),
            DecisionPoint(
                name="event_architecture_fork", default_tier=Tier.MINOR,
                branches=["both_present", "only_predicate_sweep", "only_card_deck", "neither"],
                justification="a single deterministic filesystem-presence check — tier-1 "
                               "per the rubric",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "lps_inert_check":
            # Real source-text inspection, not an assertion: count attribute-access sites
            # for legitimacy/popular_support OUTSIDE their own field declarations across the
            # settlement/ledger/derived-stat modules PR#119's L/PS-reading items would need.
            hits = 0
            for path in (_REGISTRY_PY, _LEDGER_PY, _SETTLEMENT_PY):
                text = path.read_text(encoding="utf-8")
                for line in text.splitlines():
                    stripped = line.strip()
                    if stripped.startswith(("legitimacy:", "popular_support:")):
                        continue  # the dataclass field declaration itself, not a use site
                    if ".legitimacy" in line or ".popular_support" in line:
                        hits += 1
            branch = "wired" if hits > 0 else "inert_confirmed"
            return Outcome(decision_point.name, hits, {"branch": branch})

        if decision_point.name == "event_architecture_fork":
            predicate_sweep_present = _PREDICATE_SWEEP_DIR.is_dir()
            card_deck_present = _CARD_DECK_DOC.is_file()
            if predicate_sweep_present and card_deck_present:
                branch = "both_present"
            elif predicate_sweep_present:
                branch = "only_predicate_sweep"
            elif card_deck_present:
                branch = "only_card_deck"
            else:
                branch = "neither"
            return Outcome(
                decision_point.name,
                {"predicate_sweep_present": predicate_sweep_present,
                 "card_deck_present": card_deck_present},
                {"branch": branch},
            )

        raise ValueError(f"unknown decision point {decision_point.name!r}")
