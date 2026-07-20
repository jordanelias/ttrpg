"""
Unit tests for tools/definitions_store.py — the unified definitional surface (Phase 2, ED-IN-0077).

The spec's top-risk mitigation (repo_state_armature_v1.md §5 P2): a PERMANENT parity test asserting
the store is set-identical to its source registers, so the unification can never silently drift even
if review_core is not run. Runs against the live working tree.
"""
import os
import sys

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
import definitions_store as ds  # noqa: E402


def test_store_is_current_and_parity_holds():
    """The committed store must equal a fresh rebuild AND name fields must agree across registers.
    If this fails: run `python tools/definitions_store.py --build` and commit."""
    ok, msgs = ds.check()
    assert ok, "definitions store drift or name mismatch:\n" + "\n".join(msgs)


def test_store_keys_are_set_identical_to_source_union():
    """No key invented, none dropped — the store is exactly union(names_index, descriptor_registry)."""
    names, desc = ds._load_names(), ds._load_descriptors()
    expected = set(names) | set(desc)
    store_keys = set((ds.load_store().get('definitions') or {}).keys())
    assert store_keys == expected, (
        f"store != source union; missing={expected - store_keys}, extra={store_keys - expected}")


def test_name_fields_never_disagree_on_overlap():
    """Every key in BOTH registers must carry the same canonical/name (extends ci_names_consistency)."""
    names, desc = ds._load_names(), ds._load_descriptors()
    for key in set(names) & set(desc):
        assert (names[key] or {}).get('canonical') == (desc[key] or {}).get('name'), \
            f"name disagreement at {key}"


def test_every_definition_has_a_canonical():
    for key, rec in (ds.load_store().get('definitions') or {}).items():
        assert rec.get('canonical'), f"{key} has no canonical name"
