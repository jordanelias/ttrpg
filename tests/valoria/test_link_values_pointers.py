"""
Unit tests for tools/link_values_pointers.py — the value↔pointer link (ED-IN-0079).

Pins: the committed link map matches a fresh build (drift), and every link is ANTI-FABRICATION-safe
— its recorded `token` literally appears in the linked value's constant-name or dict keys (nothing
semantic is invented). Runs against the live working tree.
"""
import json
import os
import sys

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, TOOLS)
import link_values_pointers as lvp  # noqa: E402


def _sim_params():
    return {r["key"]: r for r in json.load(
        open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))["params"]}


def test_links_current():
    ok, msgs = lvp.check()
    assert ok, "\n".join(msgs)


def test_every_link_token_is_real():
    """Anti-fabrication: each link's token must literally appear in the value's name OR its dict keys."""
    params = _sim_params()
    for l in lvp.build()["links"]:
        rec = params.get(l["value"])
        assert rec is not None, f"link references unknown value {l['value']}"
        tok = l["token"].lower()
        in_name = tok in rec["name"].lower()
        in_keys = isinstance(rec["value"], dict) and any(tok == str(k).lower() for k in rec["value"])
        assert in_name or in_keys, f"fabricated link: token '{l['token']}' not in {l['value']} name/keys"


def test_no_authoring_or_citeid_links():
    """The guards hold: no link to an authoring abbreviation, and no cite-ID token (PP_329)."""
    for l in lvp.build()["links"]:
        assert l["token"].lower() not in lvp._EXCLUDE_ABBR, f"authoring abbr leaked: {l}"


def test_indexes_agree_with_link_list():
    d = lvp.build()
    flat = {(l["value"], l["pointer_key"]) for l in d["links"]}
    for pk, blk in d["by_pointer"].items():
        for v in blk["values"]:
            assert (v, pk) in flat
