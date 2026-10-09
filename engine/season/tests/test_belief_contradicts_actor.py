"""v9 IN-15 / H-201 -- `epistemic.belief_contradicts(..., actor=)`.

The keyword rebinds the cell's `actor` operand and nothing else: the ledger read is the person's
own either way. Default `None` is `p.id`, so every existing caller is byte-for-byte unchanged.

FALSIFIER: a spy on `evaluate` sees the binding. Mutations that must redden this file: ignore
`actor` (the second test), bind `None` for the default (the first), read the actor's ledger
instead of `p`'s (the third)."""
from engine.season import epistemic as E
from engine.season.data.verbs import VERB_TABLE

import pytest


class _Spy:
    def __init__(self, monkeypatch):
        self.calls = []
        real = E.evaluate

        def spy(typed, reader, binding):
            self.calls.append((reader, dict(binding)))
            return real(typed, reader, binding)

        monkeypatch.setattr(E, "evaluate", spy)


def _typed_row():
    for name in sorted(VERB_TABLE):
        r = VERB_TABLE[name]
        if getattr(r, "requires_typed", None) is not None and (r.requires or "").strip() not in E.NO_PRECONDITION:
            return r
    raise AssertionError("no verb row with a typed requirement")


class _P:
    def __init__(self, pid):
        self.id = pid
        self.ledger = []


def test_the_default_binds_the_person_as_actor(monkeypatch):
    spy = _Spy(monkeypatch)
    E.belief_contradicts(_P("p_w"), _typed_row(), "x", {})
    assert len(spy.calls) == 1, "belief_contradicts did not reach evaluate"
    assert spy.calls[0][1]["actor"] == "p_w"


def test_actor_rebinds_the_cells_actor_operand(monkeypatch):
    spy = _Spy(monkeypatch)
    E.belief_contradicts(_P("p_w"), _typed_row(), "x", {}, actor="p_doer")
    assert len(spy.calls) == 1
    assert spy.calls[0][1]["actor"] == "p_doer"


def test_the_ledger_stays_the_persons_own(monkeypatch):
    spy = _Spy(monkeypatch)
    w = _P("p_w")
    w.ledger = ["witness-claim-sentinel"]
    E.belief_contradicts(w, _typed_row(), "x", {}, actor="p_doer")
    assert spy.calls[0][0]._claims == ["witness-claim-sentinel"], (
        "the reader must be built over the witness's ledger, not the actor's")
