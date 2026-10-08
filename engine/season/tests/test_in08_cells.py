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
judged in the CELL-VALUE AND COSINE PASS). H7 (B-H) added the STANDING TEST at the foot of this file:
it computes the pair through `data.pursuits.to_axes` on the shipped table, asserts the computation
ran, prints the value, and goes red only when the INSTRUMENT cannot compute the pair. A cell-value
change that moves the cosine, even across the 60-degree bar, leaves it green.
"""
from __future__ import annotations

import math
import re

import pytest

from ..data import verbs as V
from ..data.cast import _rows, pursuits_of
from ..data.pursuits import pursuit, to_axes
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


def test_no_retired_pursuit_name_survives_in_the_cast_or_the_tables():
    """`faith`/`warden` as a PURSUIT (any case) is gone from every owner: the roster, the projection
    rows, the role templates and every NPC's `conviction:` value. The in-world Warden offices,
    faction and titles live in other files and are untouched (RS-4)."""
    assert not {"faith", "warden"} & {p.lower() for p in PURSUITS}
    assert "doctrine" in PURSUITS and "stewardship" in PURSUITS   # one name per test, not a roster literal
    for name in ("pursuit_projection", "role_template_pursuits"):
        rows = table(name)
        keys = set(rows) | {k for r in rows.values() for k in r}
        assert not {"faith", "warden"} & {str(k).lower() for k in keys}, name
    text = files.NPC_REGISTRY_YAML.read_text(encoding="utf-8")
    assert not re.search(r"conviction:\s*(faith|warden)\b", text, re.I)
    checked = 0
    for r in _rows().values():
        for name in pursuits_of(r):                  # raises on any name outside the fifteen
            checked += 1
    assert checked >= 40, f"only {checked} weighted entries were checked -- the cast did not load"


def test_the_split_adds_challenge_and_accept_and_no_kill_or_wound_row():
    assert "challenge" in V.VERB_TABLE and "accept" in V.VERB_TABLE
    assert V.VERB_TABLE["accept"].contests == "the body"
    assert not V.VERB_TABLE["challenge"].contests
    # `accept` carries `fight`'s degree-keyed writes and emits by hand (the YAML has no inheritance)
    fight, accept = V.VERB_TABLE["fight"], V.VERB_TABLE["accept"]
    assert accept.writes == fight.writes and accept.emits == fight.emits
    assert not {"kill", "wound", "kill / wound"} & set(V.VERB_TABLE)


# ---- H7 (B-H): THE DOCTRINE PAIR, A STANDING INSTRUMENT -- RECORDED, NOT GATED (RS-3) --------------
#
# Jordan's pair (S5 `:127-129`): a devout church-of-Solmund builder against a pure-Einhir dismantler,
# BOTH high on `doctrine`. The placements are test INPUTS -- two persons' weights, as the draft
# `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md` §5.1 arm A places
# them (`faith` there is `doctrine` here, RS-2) -- and the cosine is COMPUTED from the shipped
# `pursuit_projection` through `to_axes`, the one owner of convictions -> axes. No cell value and no
# expected cosine is copied into this file.
_BUILDER = {"doctrine": .45, "stability": .20, "honour": .15, "community": .10, "virtue": .10}
_DISMANTLER = {"doctrine": .45, "liberty": .20, "justice": .15, "community": .10, "individuality": .10}


class _PairUncomputable(Exception):
    """The instrument cannot compute the pair -- as opposed to computing a number someone dislikes."""


def _doctrine_pair_cosine() -> float:
    """cos(builder, dismantler) in the seven-axis basis, off whatever `V.PURSUIT_PROJECTION` holds now.

    It refuses (never returns a default) when the pair is not a doctrine pair on this table: a
    `doctrine` row missing or all-zero, a placement naming no `doctrine` weight, a zero vector, or
    a result outside [-1, +1] / not finite. It does NOT refuse a high or low cosine."""
    for who in (_BUILDER, _DISMANTLER):
        for name in who:
            pursuit(name)                                    # a retired/mistyped name raises here
        if not who.get("doctrine"):
            raise _PairUncomputable("a placement carries no `doctrine` weight")
    row = V.PURSUIT_PROJECTION.get("doctrine")
    if not row or not any(float(c) for c in row.values()):
        raise _PairUncomputable("the table has no non-zero `doctrine` row: the pair is not a doctrine pair")
    a, b = to_axes(_BUILDER), to_axes(_DISMANTLER)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if not na or not nb:
        raise _PairUncomputable("a placement projects to the zero vector")
    cos = sum(a[ax] * b[ax] for ax in PURSUIT_AXES) / (na * nb)
    if not math.isfinite(cos) or not -1.0 - 1e-9 <= cos <= 1.0 + 1e-9:
        raise _PairUncomputable(f"cosine {cos!r} is not a cosine")
    return cos


def test_the_doctrine_pair_cosine_is_computed_from_the_shipped_table_and_recorded(record_property):
    """RECORDED, NOT GATED: this asserts the instrument RAN and is well-formed, never where the value
    lies. The recorded +0.229 (`rosters.yaml` note, R-06) is the draft-weights reading at B-G; the
    doctrine row is provisional, so a moved cosine is a finding for the cosine pass, not a red here."""
    cos = _doctrine_pair_cosine()
    assert isinstance(cos, float) and math.isfinite(cos) and -1.0 <= cos <= 1.0 + 1e-9
    record_property("doctrine_pair_cosine", round(cos, 3))
    print(f"\nDOCTRINE PAIR (builder vs dismantler, shipped pursuit_projection): cos {cos:+.3f}")
    # the pair is two DIFFERENT persons: identical placements would read +1 and prove nothing
    assert _BUILDER != _DISMANTLER
    assert to_axes(_BUILDER) != to_axes(_DISMANTLER)


def test_the_doctrine_pair_instrument_can_fail_and_the_shipped_table_is_untouched(monkeypatch):
    """FALSIFIER, on PLANTED copies (`monkeypatch` restores; the shipped table is never edited).
    A control first: the shipped table computes, and zeroing its `doctrine` row MOVES the value, so
    the planted-table runs below are observably reading the planted table and not a cached one."""
    import copy
    shipped = copy.deepcopy(V.PURSUIT_PROJECTION)
    control = _doctrine_pair_cosine()
    # the shipped `doctrine` row is live in the projection: dropping the weight changes the vector,
    # so the refusals below are the instrument's, not an accident of arithmetic on an inert row
    assert to_axes(_BUILDER) != to_axes({k: v for k, v in _BUILDER.items() if k != "doctrine"})

    planted = copy.deepcopy(shipped)
    del planted["doctrine"]                                # the pair's defining row, absent
    monkeypatch.setattr(V, "PURSUIT_PROJECTION", planted)
    with pytest.raises(_PairUncomputable, match="doctrine"):
        _doctrine_pair_cosine()

    planted = copy.deepcopy(shipped)
    planted["doctrine"] = {ax: 0.0 for ax in PURSUIT_AXES}   # present but inert
    monkeypatch.setattr(V, "PURSUIT_PROJECTION", planted)
    with pytest.raises(_PairUncomputable, match="doctrine"):
        _doctrine_pair_cosine()
    planted = {k: {ax: 0.0 for ax in PURSUIT_AXES} for k in shipped}   # every row inert: zero vectors
    monkeypatch.setattr(V, "PURSUIT_PROJECTION", planted)
    with pytest.raises(_PairUncomputable):
        _doctrine_pair_cosine()

    monkeypatch.undo()
    assert V.PURSUIT_PROJECTION == shipped                   # the shipped table was never touched
    assert _doctrine_pair_cosine() == control                # and the instrument is back to the control


def test_a_moved_doctrine_cosine_does_not_turn_the_pair_test_red(monkeypatch):
    """RECORDED, NOT GATED, observed: scale the `doctrine` row's cells and the cosine moves (here
    far from the recorded value); the instrument still returns it. Were this gated, it would raise."""
    import copy
    control = _doctrine_pair_cosine()
    planted = copy.deepcopy(V.PURSUIT_PROJECTION)
    planted["doctrine"] = {ax: -3.0 * float(c) for ax, c in planted["doctrine"].items()}
    monkeypatch.setattr(V, "PURSUIT_PROJECTION", planted)
    moved = _doctrine_pair_cosine()
    assert moved != pytest.approx(control, abs=1e-6), "the planted row did not move the value"
