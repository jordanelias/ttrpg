"""The Godot constants bridge must never pick a value by walk order.

`sim_params.json` keys are `<subsystem>.<NAME>` and are NOT unique: two modules in one subsystem
defining the same constant name emit two rows under one key. `export_game_constants._load_sources()`
used to write `vals[key] = value` for every row, so a colliding key resolved to whichever module the
extractor walked last — and that value is what `game_constants.json` hands to
`valoria-game/tools/check_constants_parity.py`.

Nothing had ever exercised that, because no MAPPING entry happened to name a colliding key. The
failure was therefore silent and one MAPPING line away, which is the §0.1 pt-5 shape that earns a
guard: the artifact is load-bearing on the game, not on this repository's process.

Falsifier (§0.1 pt 3): delete the `for k in ambiguous: del vals[k]` loop in `_load_sources` and
`test_an_ambiguous_key_is_withheld_not_guessed` fails.
"""
import json
import os
import sys

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import export_game_constants as egc  # noqa: E402


def _colliding_keys():
    rows = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))["params"]
    by_key = {}
    out = set()
    for r in rows:
        if r['kind'] == 'table' or not isinstance(r['value'], (int, float, bool)):
            continue
        if r['key'] in by_key and by_key[r['key']] != r['value']:
            out.add(r['key'])
        by_key[r['key']] = r['value']
    return out


def test_an_ambiguous_key_is_withheld_not_guessed():
    """The assertion can observe the failure it excludes (§0.1 pt 2): it is written against the
    live collision set, so it stays meaningful whether that set grows, shrinks, or empties."""
    src = egc._load_sources()
    collisions = _colliding_keys()
    assert collisions, (
        "no key in sim_params.json resolves to two different values any more. That is fine — but it "
        "means this test can no longer observe the behaviour it guards. Either re-point it at a "
        "synthetic fixture, or retire it; do not leave it passing vacuously."
    )
    for k in collisions:
        assert k not in src, f"{k} resolves to two different values and was still handed a single one"
    assert egc._AMBIGUOUS == collisions


def test_mapping_never_names_an_ambiguous_owner():
    """If someone maps a GD constant onto a colliding key, build() must refuse rather than ship."""
    src = egc._load_sources()
    for gd, key in egc.MAPPING.items():
        assert key in src, (
            f"{gd} -> {key}: the bridge cannot resolve this owner. If the key is ambiguous, name the "
            f"definition site you mean; do not let directory walk order choose the value Godot gets."
        )


def test_unambiguous_duplicates_are_still_exported():
    """Rows that share a key AND agree are not a hazard — withholding them would be over-correction."""
    rows = json.load(open(os.path.join(ROOT, 'engine', 'engine_params', 'sim_params.json')))["params"]
    seen, agreeing = {}, set()
    for r in rows:
        if r['kind'] == 'table' or not isinstance(r['value'], (int, float, bool)):
            continue
        if r['key'] in seen and seen[r['key']] == r['value']:
            agreeing.add(r['key'])
        seen[r['key']] = r['value']
    src = egc._load_sources()
    for k in agreeing - _colliding_keys():
        assert k in src, f"{k}'s definition sites agree — it should not have been withheld"
