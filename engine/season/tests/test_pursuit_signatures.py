"""B10.17: a pursuit's signature (the verbs its name must mean in acts) read against the lean the tables give it.

`signature_breaks` is a READER over `person_q.pursuit_lean`; the plant is a copy of the alignment table, bound for one
test and never the shipped one."""
from __future__ import annotations

import pytest

from engine.season.data import verbs as V
from engine.season.data.pursuits import signature_breaks

SIGNATURE = {"love": {"favours": ["give"], "opposes": ["forge"]}}


def _plant(monkeypatch, give: float, forge: float):
    """`love` projects +0.7 on `selfish_selfless`; a copy of the table with one axis cell per verb sets each lean's sign."""
    monkeypatch.setattr(V, "ALIGNMENT", {"selfish_selfless": {"give": give, "forge": forge}})


def test_signature_breaks_reports_a_planted_break(monkeypatch):
    _plant(monkeypatch, give=1.0, forge=-1.0)
    assert signature_breaks(SIGNATURE) == {}, "control: a favoured verb leaning toward and an opposed one away is no break"
    _plant(monkeypatch, give=-1.0, forge=-1.0)
    broken = signature_breaks(SIGNATURE)
    assert [c["clause"] for c in broken["love"]] == ["favoured_not_above_zero"]
    assert broken["love"][0]["verb"] == "give" and broken["love"][0]["lean"] < 0
    _plant(monkeypatch, give=0.5, forge=1.0)
    clauses = {(c["clause"], c["verb"]) for c in signature_breaks(SIGNATURE)["love"]}
    assert clauses == {("opposed_not_below_zero", "forge"), ("opposed_outleans_favoured", "forge")}
