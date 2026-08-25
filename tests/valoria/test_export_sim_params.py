"""
Unit tests for tools/export_sim_params.py — the typed values layer (ED-IN-0079).

Pins the two guarantees: the committed sim_params.json matches a fresh extract (drift), and every
extracted value is ANTI-FABRICATION-safe — it round-trips as a JSON literal (no synthesized values;
the extractor only reads Python literals). Runs against the live working tree.
"""
import ast
import collections
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
    """Anti-fabrication: each record's value must equal the AST literal at its DEFINITION SITE —
    never a synthesized number. Re-extract independently and compare the value set.

    Indexed by (key, file), not by key alone. `key` is `<subsystem>.<NAME>`, so two modules in one
    subsystem that define the same constant name produce two rows with ONE key — and a dict keyed by
    `key` silently keeps whichever was walked last. That is not a weak check, it is an absent one:
    it made this test compare `mass_battle.SEED_BASE`'s bat.py row (1_000_000) against
    lanchester_signature.py's literal (2_000_000) and call the difference fabrication. (key, file) is
    unique across all rows; the pair is what the extractor actually reads."""
    fresh = {(r["key"], r["file"]): json.dumps(r["value"], sort_keys=True)
             for r in esp.build()["params"]}
    committed = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))
    for r in committed["params"]:
        site = (r["key"], r["file"])
        assert site in fresh, f"committed {r['key']} @ {r['file']} not in a fresh extract (stale/fabricated?)"
        assert json.dumps(r["value"], sort_keys=True) == fresh[site], \
            f"value drift at {r['key']} @ {r['file']} — committed != source literal"


def test_key_and_file_together_identify_one_definition_site():
    """The falsifier for the index above: if (key, file) ever stops being unique, the comparison
    silently collapses rows again and this test must say so before the drift check goes blind."""
    rows = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))["params"]
    sites = collections.Counter((r["key"], r["file"]) for r in rows)
    dupes = {s: n for s, n in sites.items() if n > 1}
    assert not dupes, f"(key, file) is no longer unique: {dupes}"


def test_key_alone_is_known_to_collide_and_is_not_used_as_an_index():
    """Records the measured collisions so a future session does not 'simplify' the index back to
    `key`. These are real: one subsystem, one constant name, two modules, two different values."""
    rows = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))["params"]
    by_key = collections.defaultdict(set)
    for r in rows:
        by_key[r["key"]].add(json.dumps(r["value"], sort_keys=True))
    ambiguous = sorted(k for k, v in by_key.items() if len(v) > 1)
    assert ambiguous == ['mass_battle.SEED_BASE'], (
        "the set of keys that resolve to more than one value changed: " + repr(ambiguous) +
        " — a new one means some consumer indexing sim_params.json by `key` alone is now picking a "
        "value by walk order. tools/export_game_constants.py is the one that reaches Godot."
    )


def test_count_matches_records():
    d = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))
    assert d["count"] == len(d["params"])
