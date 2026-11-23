"""B10.17: a pursuit's signature (the verbs its name must mean in acts) read against the lean the tables give it.

`signature_breaks` is a READER over `person_q.pursuit_lean`; the plant is a copy of the alignment table, bound for one
test and never the shipped one."""
from __future__ import annotations

import pytest

from engine.season.data import affiliations as A
from engine.season.data import verbs as V
from engine.season.harness.conviction_spread import signature_breaks
from engine.season.data.rosters import AFFILIATIONS

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


def test_affiliation_signatures_are_read_against_the_engagement_table(monkeypatch):
    """B10.19: a creed's signature is read against `tables.affiliation_engagement`, the one table that says what an act does
    to a held creed; the planted row and the planted cells are copies, never the shipped ones."""
    creed = sorted(AFFILIATIONS)[0]
    row = {creed: {"favours": ["give"], "opposes": ["forge"]}}
    monkeypatch.setattr(A, "ENGAGEMENT", {creed: {"give": 1.0, "forge": -1.0}})
    assert signature_breaks({}, row) == {}, "control: a favoured verb engaged up and an opposed one down is no break"
    monkeypatch.setattr(A, "ENGAGEMENT", {creed: {"give": 0.5, "forge": 1.0}})
    clauses = {(c["clause"], c["verb"]) for c in signature_breaks({}, row)[creed]}
    assert clauses == {("opposed_not_below_zero", "forge"), ("opposed_outleans_favoured", "forge")}
    monkeypatch.setattr(A, "ENGAGEMENT", {})
    assert {c["clause"] for c in signature_breaks({}, row)[creed]} == {"favoured_not_above_zero", "opposed_not_below_zero"}
