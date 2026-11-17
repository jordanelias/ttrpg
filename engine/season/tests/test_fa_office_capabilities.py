"""B04.21 -- a seat row may name the skill its post calls on (`capability:`, row data, not a `Seat` field).

Created here because B04.19 is a POINTER (the social contest's V2 fold, ED-IN-0378); B04.22 and B04.23 add to it.
`data/rosters.py::_load_offices` refuses a `capability:` that is not a defined skill (`descriptors.CAPABILITIES`),
naming the row. The loader is pointed at a throwaway copy of the shipped file (as
`test_governance_build.py::test_8a_a_repeated_row_id_refuses_at_load_instead_of_being_collapsed` does); the unchanged
copy and a copy carrying a defined skill and a `null` are the positive controls, so a loader that refused every
file cannot pass.
"""
from __future__ import annotations

import pytest
import yaml

from engine.substrate.descriptors import CAPABILITIES

from ..data import files, rosters
from ..gaps import Unspecified


def _real() -> dict:
    return rosters.load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))


def _load_with(tmp_path, monkeypatch, doc: dict) -> dict:
    path = tmp_path / "offices.yaml"
    path.write_text(yaml.safe_dump(doc), encoding="utf-8")
    monkeypatch.setattr(rosters, "OFFICES_YAML", path)
    return rosters._load_offices()


def test_a_seat_row_naming_an_undefined_capability_is_refused(tmp_path, monkeypatch):
    real = _real()
    n = len(real["seats"])
    assert len(_load_with(tmp_path, monkeypatch, real)["seats"]) == n  # control: the unchanged file loads

    row = real["seats"][0]
    assert "capability" not in row  # control: no shipped row names one (the first commit authors none)
    for bad in ("swordplay", "", 7, ["arms"]):
        doc = dict(real, seats=[dict(row, capability=bad), *real["seats"][1:]])
        with pytest.raises(Unspecified) as red:
            _load_with(tmp_path, monkeypatch, doc)
        assert row["id"] in str(red.value) and "capability" in str(red.value), str(red.value)

    # the same refusal over `foreign_seats:`, which shares the row shape
    if real.get("foreign_seats"):
        frow = real["foreign_seats"][0]
        doc = dict(real, foreign_seats=[dict(frow, capability="swordplay"), *real["foreign_seats"][1:]])
        with pytest.raises(Unspecified) as red:
            _load_with(tmp_path, monkeypatch, doc)
        assert frow["id"] in str(red.value)


def test_a_seat_row_may_name_a_defined_skill_or_null(tmp_path, monkeypatch):
    real = _real()
    row = real["seats"][0]
    checked = 0
    for ok in (*CAPABILITIES, None):
        doc = dict(real, seats=[dict(row, capability=ok), *real["seats"][1:]])
        loaded = _load_with(tmp_path, monkeypatch, doc)
        assert loaded["seats"][0]["capability"] == ok
        checked += 1
    assert checked == len(CAPABILITIES) + 1 and checked > 1


def test_the_shipped_offices_file_names_no_capability_yet():
    # B04.21 ships the key, not its content (D-19): the candidate rows are for Jordan, not authored.
    named = [r["id"] for r in (*rosters.OFFICES_SEATS, *rosters.FOREIGN_SEATS) if r.get("capability") is not None]
    assert named == [], named
