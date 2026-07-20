"""
Unit tests for tools/export_sim_params.py — the typed values layer (ED-IN-0079).

Pins the two guarantees: the committed sim_params.json matches a fresh extract (drift), and every
extracted value is ANTI-FABRICATION-safe — it round-trips as a JSON literal (no synthesized values;
the extractor only reads Python literals). Runs against the live working tree.
"""
import ast
import json
import os
import sys

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, TOOLS)
import export_sim_params as esp  # noqa: E402


def test_sim_params_current():
    """Committed export == fresh extract. If this fails: run `python tools/export_sim_params.py --build`."""
    ok, msgs = esp.check()
    assert ok, "\n".join(msgs)


def test_every_value_is_a_real_literal_from_source():
    """Anti-fabrication: each record's value must equal the AST literal at its (module.name) — never
    a synthesized number. Re-extract independently and compare the value set."""
    fresh = {r["key"]: json.dumps(r["value"], sort_keys=True) for r in esp.build()["params"]}
    committed = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))
    for r in committed["params"]:
        assert r["key"] in fresh, f"committed key {r['key']} not in a fresh extract (stale/fabricated?)"
        assert json.dumps(r["value"], sort_keys=True) == fresh[r["key"]], \
            f"value drift at {r['key']} — committed != source literal"


def test_count_matches_records():
    d = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))
    assert d["count"] == len(d["params"])
