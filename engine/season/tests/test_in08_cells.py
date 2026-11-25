"""IN-08's CELLS COMMIT (B-G) -- the falsifiers its plan entry names, executed.

`workplans/valoria_master_workplan_v9_part5.md` IN-08, FALSIFIER: *a table verb with no cell on
some axis and absent from the declared `uncelled:` set, or an unrostered key, loading without an
error -> fail; a `faith` or `warden` PURSUIT token left in a key, row, loader token, test id or NPC
`pursuits:` entry -> fail; a `faith` or `warden` value left under an NPC's `conviction:` key ->
fail; a `kill` or `wound` verb row -> fail.* Each is asserted below on the loader or the data that
owns it, and each loader case is run on a PLANTED copy of the shipped table, so the shipped one is
never edited (the loaders take the table as a parameter for exactly this).

WHAT IS NOT HERE, DELIBERATELY: a PIN on the doctrine-pair cosine's value. IN-08 B-G MEASURED and
RECORDED it (`rosters.yaml: tables.pursuit_projection`'s note; R-06's `measured:`); a pin would gate
what the plan says is recorded, not gated (RS-3: the `doctrine` row is PROVISIONAL and the pair is
judged in the CELL-VALUE AND COSINE PASS).
"""
from __future__ import annotations

import re

import pytest

from ..data import verbs as V
from ..data.rosters import PURSUIT_AXES, table, table_meta
from ..gaps import Forbidden


def _shipped():
    return table("alignment"), dict(table_meta("alignment").get("uncelled") or {})


def test_the_shipped_alignment_is_dense_and_every_verb_is_celled_or_declared_uncelled():
    """The control: the shipped table loads under the density rule, and its two halves partition
    the verb table -- no verb is both, none is neither."""
    cells, uncelled = _shipped()
    V._load_alignment(cells, uncelled)                       # raises if the rule is broken
    verbs_of = lambda row: {k for k in row if not k.startswith(V.DEED_PREFIX)}    # `deed:<kind>` keys are lawful (IN-18 G1)
    keyed = {v for row in cells.values() for v in verbs_of(row)}
    assert set(uncelled) and set(uncelled) <= set(V.VERB_TABLE)
    assert keyed.isdisjoint(uncelled)
    assert keyed | set(uncelled) == set(V.VERB_TABLE), sorted(set(V.VERB_TABLE) - keyed - set(uncelled))
    assert set(cells) == set(PURSUIT_AXES)
    for ax in PURSUIT_AXES:
        assert verbs_of(cells[ax]) == set(V.VERB_TABLE) - set(uncelled), ax


def test_a_verb_missing_a_cell_on_one_axis_and_not_declared_uncelled_refuses_naming_both():
    cells, uncelled = _shipped()
    verb = sorted(set(V.VERB_TABLE) - set(uncelled))[0]          # chosen from the table, not named
    axis = sorted(PURSUIT_AXES)[0]
    planted, _ = _shipped()                                     # `table()` copies on every call
    del planted[axis][verb]
    with pytest.raises(Forbidden) as e:
        V._load_alignment(planted, uncelled)
    assert repr(verb) in str(e.value) and axis in str(e.value)
    # and DECLARING it uncelled is not enough while its other cells remain
    with pytest.raises(Forbidden, match=re.escape('is declared `uncelled:` and is celled on')):
        V._load_alignment(planted, dict(uncelled, **{verb: "planted"}))


def test_an_uncelled_verb_that_carries_a_cell_or_names_no_verb_refuses():
    cells, uncelled = _shipped()
    verb = sorted(uncelled)[0]
    planted, _ = _shipped()                                     # `table()` copies on every call
    planted[sorted(PURSUIT_AXES)[0]][verb] = 0.1
    with pytest.raises(Forbidden, match=re.escape('is declared `uncelled:` and is celled on')):
        V._load_alignment(planted, uncelled)
    with pytest.raises(Forbidden, match=re.escape('which the verb table does not carry')):
        V._load_alignment(cells, dict(uncelled, **{"a verb nobody declared": "planted"}))
    with pytest.raises(Forbidden, match=re.escape('gives no reason')):
        V._load_alignment(cells, dict(uncelled, **{verb: ""}))   # a declaration with no reason


def test_an_unrostered_axis_or_verb_key_refuses():
    cells, uncelled = _shipped()
    planted, _ = _shipped()                                     # `table()` copies on every call
    planted["sacred"] = {sorted(V.VERB_TABLE)[0]: 0.3}          # an axis the seven do not carry
    with pytest.raises(Forbidden, match=re.escape('which is not in the roster')):
        V._load_alignment(planted, uncelled)
    planted, _ = _shipped()                                     # `table()` copies on every call
    planted[sorted(PURSUIT_AXES)[0]]["kill"] = 0.7               # a verb the table does not carry
    with pytest.raises(Forbidden, match=re.escape('outside the roster')):
        V._load_alignment(planted, uncelled)


def test_a_role_template_naming_a_retired_pursuit_refuses_at_load():
    """The read path (`to_axes`) skips an unknown pursuit silently; the load-time check does not."""
    t = table("role_template_pursuits")
    first = sorted(t)[0]
    t[first] = dict(t[first], Authority=0.2)
    with pytest.raises(Forbidden, match=re.escape('outside the roster')):
        V._load_role_template_pursuits(t)


def test_the_split_adds_challenge_and_accept_and_no_kill_or_wound_row():
    assert "challenge" in V.VERB_TABLE and "accept" in V.VERB_TABLE
    assert V.VERB_TABLE["accept"].contests == "the body"
    assert not V.VERB_TABLE["challenge"].contests
    # `accept` carries `fight`'s degree-keyed writes and emits by hand (the YAML has no inheritance)
    fight, accept = V.VERB_TABLE["fight"], V.VERB_TABLE["accept"]
    assert accept.writes == fight.writes
    # v10 REM-31: the `Declared` band (`the body` deferred to ENCOUNTER) names each verb's own declaration, as each
    # names its own refusal; every band the scene reads is carried by hand, identical.
    # v10 PC-10b: `accept`'s `Wounded` declares `duel.yielded` (the yielder's own kind, earned off the scene's `surrender` in
    # `_eff_kill`); B15.10 (PC_A): `fight`'s `Wounded` declares it too, a failed yield roll ending a `fight` as it ends an `accept`. So every
    # band the scene reads is `fight`'s, identical and in `fight`'s order, and no band is added (H-98).
    fe, ae = fight.emits_by_degree, accept.emits_by_degree
    assert set(ae) == set(fe)
    assert {b: k for b, k in ae.items() if b != "Declared"} == {b: k for b, k in fe.items() if b != "Declared"}
    assert "duel.yielded" in ae["Wounded"] and "duel.yielded" in fe["Wounded"]
    assert (fe["Declared"], ae["Declared"]) == (["fight.declared"], ["accept.declared"])
    assert not {"kill", "wound", "kill / wound"} & set(V.VERB_TABLE)
