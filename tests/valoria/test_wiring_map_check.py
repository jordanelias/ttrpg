"""Unit tests for tools/wiring_map_check.py (ED-IN-0074) — the wiring-manifest gate that
backs the MC-wiring map. Hermetic: every test runs validate()/work_list()/map_json() over
synthetic in-memory structures, never the live references/wiring_manifest.yaml. That is
deliberate — the live-manifest-is-green check is the report-only CI job's job (a legitimate
module rename shouldn't fail the BLOCKING unit-tests suite); these tests pin the tool's LOGIC
so the gate itself can't silently regress."""
import copy
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import wiring_map_check as wmc  # noqa: E402


def _man():
    """A tiny, internally-consistent manifest: 4 modules + 1 adapter, full coverage."""
    return {
        "build_states": ["live", "unwired", "design"],
        "godot_states": ["gd-ported", "typed-exported", "python-oracle", "no-oracle", "retire"],
        "golden_path": {"unit": "alpha", "chain": "x -> y", "note": "the template"},
        "modules": {
            "alpha": {"tier": "module", "build": "live",    "godot": "gd-ported",     "port_rank": 0, "note": "ported"},
            "beta":  {"tier": "module", "build": "unwired", "godot": "python-oracle",  "port_rank": 1, "note": "oracle"},
            "gamma": {"tier": "module", "build": "design",  "godot": "no-oracle",      "port_rank": 8, "note": "blocked"},
            "delta": {"tier": "module", "build": "design",  "godot": "retire",         "port_rank": 9, "note": "gone"},
        },
        "adapters": {
            "bridge": {"tier": "adapter", "build": "live",  "godot": "python-oracle",  "port_rank": 2, "note": "seam"},
        },
        "foundation_gaps": {"spine": {"godot": "no-oracle", "note": "undefined"}},
    }


def _reg():
    return {"module": {"alpha", "beta", "gamma", "delta"}, "adapter": {"bridge"}, "key": set()}


# ── the happy path ───────────────────────────────────────────────────────────
def test_validate_passes_on_consistent_manifest():
    assert wmc.validate(_man(), _reg()) == []


# ── the four drift scenarios the gate exists to catch ────────────────────────
def test_catches_unresolved_module_tag():
    man = _man()
    man["modules"]["alphaa"] = man["modules"].pop("alpha")   # a rename that didn't reach the registry
    fails = wmc.validate(man, _reg())
    assert any("does not resolve" in f and "alphaa" in f for f in fails)


def test_catches_missing_module_coverage():
    reg = _reg()
    reg["module"].add("epsilon")   # a real module absent from the map
    fails = wmc.validate(_man(), reg)
    assert any("coverage" in f and "epsilon" in f for f in fails)


def test_catches_moved_adapter_tag():
    man = _man()
    man["adapters"]["teleport"] = man["adapters"].pop("bridge")
    reg = _reg()  # registry still only knows "bridge"
    fails = wmc.validate(man, reg)
    assert any("adapter tag does not resolve" in f for f in fails)


def test_catches_bad_vocab():
    man = _man()
    man["modules"]["beta"]["build"] = "sorta-wired"
    man["adapters"]["bridge"]["godot"] = "kinda-ported"
    fails = wmc.validate(man, _reg())
    assert any("bad build_state" in f for f in fails)
    assert any("bad godot_state" in f for f in fails)


# ── the work-list query (what the Godot port queue is derived from) ──────────
def test_work_list_buckets_and_ranks():
    portable, blocked, ported, retire = wmc.work_list(_man())
    # python-oracle units, ranked by port_rank then name: beta(1) before bridge(2)
    assert [n for n, _, _ in portable] == ["beta", "bridge"]
    assert [n for n, _, _ in blocked] == ["gamma"]
    assert [n for n, _ in ported] == ["alpha"]
    assert retire == ["delta"]


# ── the embeddable block the HTML map's PORT is generated from ───────────────
def test_map_json_shape_matches_manifest():
    d = wmc.map_json(_man())
    assert set(d["modules"]) == {"alpha", "beta", "gamma", "delta"}
    assert set(d["adapters"]) == {"bridge"}
    assert d["godot_counts"]["gd-ported"] == 1
    assert d["godot_counts"]["python-oracle"] == 2   # beta + bridge
    assert d["build_counts"]["design"] == 2          # gamma + delta
    assert d["golden_path"]["unit"] == "alpha"


def test_validate_does_not_mutate_input():
    man = _man()
    before = copy.deepcopy(man)
    wmc.validate(man, _reg())
    assert man == before
