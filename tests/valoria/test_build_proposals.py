"""
Unit tests for tools/observability/build_proposals.py — the unified proposals register.

Pins the coverage guarantees: all designs/proposals/ docs surface BY LOCATION
(incl. the 8 without a Status line — the gap the dashboard had), the 17 non-PASS
audit-registry verdicts are not over-collapsed by shared ids, every item is
lane-tagged, and the schema/dedup hold. Runs against the live working tree.
"""
import os
import sys

HERE = os.path.dirname(__file__)
OBS = os.path.join(HERE, '..', '..', 'tools', 'observability')
REPO = os.path.join(HERE, '..', '..')
sys.path.insert(0, OBS)
import build_proposals as bp  # noqa: E402


def _reg():
    return bp.build()


def test_all_proposals_docs_surface_by_location():
    reg = _reg()
    props = {i["source"] for i in reg["items"] if i["kind"] == "proposal_doc"}
    on_disk = {
        f"designs/proposals/{f}"
        for f in os.listdir(os.path.join(REPO, "designs", "proposals"))
        if f.endswith(".md")
    }
    assert props == on_disk, f"missing: {on_disk - props}"
    # Regression pin on the location-scan count; bump when a designs/proposals doc
    # is added/removed. 10 since ED-IN-0071 (repo-reorganization-v1.md).
    assert len(props) == 10


def test_all_seventeen_audit_verdicts_present():
    # id is shared across subsystem rows; the register must not collapse them
    reg = _reg()
    audits = [i for i in reg["items"] if i["kind"] == "audit_partial"]
    assert len(audits) == 17


def test_every_item_lane_tagged():
    reg = _reg()
    valid = set(bp.core.LANE_CODES) | {"unassigned"}
    for it in reg["items"]:
        assert it["lane"] in valid, it


def test_dedup_stable_and_counts_consistent():
    reg = _reg()
    keys = [(i["kind"], i["source"], i["id"]) for i in reg["items"]]
    assert len(keys) == len(set(keys)), "duplicate (kind,source,id) rows"
    assert reg["counts"]["total"] == len(reg["items"])
    lane_total = sum(v["total"] for v in reg["counts"]["by_lane"].values())
    assert lane_total == reg["counts"]["total"]


def test_needs_jordan_split_matches_ledger():
    reg = _reg()
    nj_ledger = [i for i in reg["items"] if i["kind"] == "ledger_needs_jordan"]
    assert all(i["needs_jordan"] for i in nj_ledger)
    actionable = [i for i in reg["items"] if i["kind"] == "ledger_actionable"]
    assert all(not i["needs_jordan"] for i in actionable)


def test_design_docs_can_carry_needs_jordan():
    # regression for the structural undercount: proposal_doc / provisional_status_doc
    # kinds must be able to carry needs_jordan (a "HELD FOR JORDAN" doc is not actionable)
    reg = _reg()
    design = [i for i in reg["items"]
              if i["kind"] in ("proposal_doc", "provisional_status_doc")]
    flagged = [i for i in design if i["needs_jordan"]]
    assert flagged, "no design doc carries needs_jordan — the flag is unreachable again"


def test_links_out_not_reranks():
    # detect-not-author: the register LINKS the human ranked queue, never re-ranks
    reg = _reg()
    assert reg["ranked_view"].endswith("decision_queue_delta_v1.md")
    assert "valoria_master_workplan_v6.md" in reg["workplan_tiers"]
