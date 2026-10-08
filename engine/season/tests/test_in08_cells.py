"""IN-08's CELLS COMMIT (B-G) -- the falsifiers its plan entry names, executed.

`workplans/valoria_master_workplan_v9_part5.md` IN-08, FALSIFIER: *a table verb with no cell on
some axis and absent from the declared `uncelled:` set, or an unrostered key, loading without an
error -> fail; a `faith` or `warden` PURSUIT token left in a key, row, loader token, test id or NPC
`pursuits:` entry -> fail; a `faith` or `warden` value left under an NPC's `conviction:` key ->
fail; a `kill` or `wound` verb row -> fail.* Each is asserted below on the loader or the data that
owns it, and each loader case is run on a PLANTED copy of the shipped table, so the shipped one is
never edited (the loaders take the table as a parameter for exactly this).

WHAT IS NOT HERE, DELIBERATELY: the doctrine-pair cosine. IN-08 B-G MEASURES and RECORDS it
(`rosters.yaml: tables.pursuit_projection`'s note); H7, in B-H, builds the standing test that pins
it. A pin here would gate what the plan says is recorded, not gated (RS-3).
"""
from __future__ import annotations

import re

import pytest

from ..data import verbs as V
from ..data.cast import _rows, pursuits_of
from ..data.rosters import PURSUIT_AXES, PURSUITS, table, table_meta
from ..gaps import Forbidden
from engine.season.data import files


def _shipped():
    return table("alignment"), dict(table_meta("alignment").get("uncelled") or {})


def test_the_shipped_alignment_is_dense_and_every_verb_is_celled_or_declared_uncelled():
    """The control: the shipped table loads under the density rule, and its two halves partition
    the verb table -- no verb is both, none is neither."""
    cells, uncelled = _shipped()
    V._load_alignment(cells, uncelled)                       # raises if the rule is broken
    keyed = {v for row in cells.values() for v in row}
    assert set(uncelled) and set(uncelled) <= set(V.VERB_TABLE)
    assert keyed.isdisjoint(uncelled)
    assert keyed | set(uncelled) == set(V.VERB_TABLE), sorted(set(V.VERB_TABLE) - keyed - set(uncelled))
    assert set(cells) == set(PURSUIT_AXES)
    for ax in PURSUIT_AXES:
        assert set(cells[ax]) == set(V.VERB_TABLE) - set(uncelled), ax


def test_a_verb_missing_a_cell_on_one_axis_and_not_declared_uncelled_refuses_naming_both():
    cells, uncelled = _shipped()
    verb = sorted(set(V.VERB_TABLE) - set(uncelled))[0]          # chosen from the table, not named
    axis = sorted(PURSUIT_AXES)[0]
    planted = {ax: dict(row) for ax, row in cells.items()}
    del planted[axis][verb]
    with pytest.raises(Forbidden) as e:
        V._load_alignment(planted, uncelled)
    assert repr(verb) in str(e.value) and axis in str(e.value)
    # and DECLARING it uncelled is not enough while its other cells remain
    with pytest.raises(Forbidden):
        V._load_alignment(planted, dict(uncelled, **{verb: "planted"}))


def test_an_uncelled_verb_that_carries_a_cell_or_names_no_verb_refuses():
    cells, uncelled = _shipped()
    verb = sorted(uncelled)[0]
    planted = {ax: dict(row) for ax, row in cells.items()}
    planted[sorted(PURSUIT_AXES)[0]][verb] = 0.1
    with pytest.raises(Forbidden):
        V._load_alignment(planted, uncelled)
    with pytest.raises(Forbidden):
        V._load_alignment(cells, dict(uncelled, **{"a verb nobody declared": "planted"}))
    with pytest.raises(Forbidden):
        V._load_alignment(cells, dict(uncelled, **{verb: ""}))   # a declaration with no reason


def test_an_unrostered_axis_or_verb_key_refuses():
    cells, uncelled = _shipped()
    planted = {ax: dict(row) for ax, row in cells.items()}
    planted["sacred"] = {sorted(V.VERB_TABLE)[0]: 0.3}          # an axis the seven do not carry
    with pytest.raises(Forbidden):
        V._load_alignment(planted, uncelled)
    planted = {ax: dict(row) for ax, row in cells.items()}
    planted[sorted(PURSUIT_AXES)[0]]["kill"] = 0.7               # a verb the table does not carry
    with pytest.raises(Forbidden):
        V._load_alignment(planted, uncelled)


def test_a_role_template_naming_a_retired_pursuit_refuses_at_load(monkeypatch):
    """The read path (`to_axes`) skips an unknown pursuit silently; the load-time check does not."""
    real = V.table
    def planted(name):
        t = real(name)
        if name == "role_template_pursuits":
            first = sorted(t)[0]
            t = dict(t, **{first: dict(t[first], Authority=0.2)})
        return t
    monkeypatch.setattr(V, "table", planted)
    with pytest.raises(Forbidden):
        V._load_role_template_pursuits()


def test_no_retired_pursuit_name_survives_in_the_cast_or_the_tables():
    """`faith`/`warden` as a PURSUIT (any case) is gone from every owner: the roster, the projection
    rows, the role templates and every NPC's `conviction:` value. The in-world Warden offices,
    faction and titles live in other files and are untouched (RS-4)."""
    assert not {"faith", "warden"} & {p.lower() for p in PURSUITS}
    assert {"doctrine", "stewardship"} <= set(PURSUITS)
    for name in ("pursuit_projection", "role_template_pursuits"):
        rows = table(name)
        keys = set(rows) | {k for r in rows.values() for k in r}
        assert not {"faith", "warden"} & {str(k).lower() for k in keys}, name
    text = files.NPC_REGISTRY_YAML.read_text(encoding="utf-8")
    assert not re.search(r"conviction:\s*(faith|warden)\b", text, re.I)
    checked = 0
    for r in _rows().values():
        for name in pursuits_of(r):                  # raises on any name outside the fifteen
            assert name in PURSUITS
            checked += 1
    assert checked >= 40, f"only {checked} weighted entries were checked -- the cast did not load"


def test_the_split_adds_challenge_and_accept_and_no_kill_or_wound_row():
    assert "challenge" in V.VERB_TABLE and "accept" in V.VERB_TABLE
    assert V.VERB_TABLE["accept"].contests == "the body"
    assert not V.VERB_TABLE["challenge"].contests
    assert not {"kill", "wound", "kill / wound"} & set(V.VERB_TABLE)
