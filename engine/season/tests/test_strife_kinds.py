"""CR-75 -- `rosters.yaml: strife_kinds` (opens, joins, never, concludes) and `foreign_factions`.

Two checks, and why they live apart:

  1. THE IMPORT CHECK (`data/verbs.py::_check_strife_kinds`, run when `EVENT_KINDS` is built) refuses a kind
     outside `EVENT_KINDS`, a kind in two of opens/joins/never, and a `concludes` kind outside opens and
     joins. It never reads `strife_moves.yaml`, so it cannot see a kind the registry names that no list
     decides, nor a `concludes` that disagrees with the rule. Each refusal is planted below on the function
     (the same call import makes), and the shipped build loading is itself the control.
  2. THIS TEST reads the chain the loader does not: every kind the registry names is in exactly one of
     opens, joins, never (a decision per kind, not a default), and `concludes` equals the rule's derivation
     over the registry -- a kind concludes only if every code it maps to is terminal (`ends` above 0 and not
     `terminal: false`), taken over the opens and joins kinds (a `never` kind is no move). The derivation is
     written here, once, as the check on the data; no loader reads it.

MUTATION (the exit line): `requisition.taken` added to `concludes` by hand passes the import check (it is in
`opens`) and is red here, because it maps to VI, which ends no case.
"""
from collections import defaultdict

import pytest

from engine.season.data import rosters as R
from engine.season.data.verbs import EVENT_KINDS, _check_strife_kinds
from engine.season.gaps import Unspecified
from engine.season.harness import strife_data as data

LISTS = tuple(sorted(R.STRIFE_KINDS))      # the four lists, read off the loader and not spelled again
DECIDED = tuple(n for n in LISTS if n != "concludes")   # opens, joins, never: a decision per kind


def _planted(**changes):
    """A copy of the shipped lists as plain lists, with `changes` (name -> new list) applied."""
    d = {n: sorted(R.STRIFE_KINDS[n]) for n in LISTS}
    d.update(changes)
    return d


def _terminal(row) -> bool:
    return row.get("ends", 0) > 0 and row.get("terminal", True) is not False


def derive_concludes(rows, lists) -> frozenset:
    """The kinds that may conclude a strand at the person reading, by `strife-01` §3 item 2's rule."""
    codes_of = defaultdict(list)
    for r in rows:
        for k in r["kinds"]:
            codes_of[k].append(r)
    moves = lists["opens"] | lists["joins"]
    return frozenset(k for k in moves if codes_of.get(k) and all(_terminal(r) for r in codes_of[k]))


def test_the_shipped_build_loads_and_the_lists_are_disjoint_decisions():
    # The import already ran `_check_strife_kinds`; running it again on the shipped lists is the control for
    # the three plants below (they must be red for the planted fault and not for the shipped data).
    _check_strife_kinds(R.STRIFE_KINDS, EVENT_KINDS)
    assert set(R.STRIFE_KINDS) == set(LISTS)
    assert all(R.STRIFE_KINDS[n] for n in LISTS)
    assert R.STRIFE_KINDS["concludes"] <= R.STRIFE_KINDS["opens"] | R.STRIFE_KINDS["joins"]


def test_import_check_refuses_a_kind_outside_event_kinds():
    bad = _planted(never=sorted(R.STRIFE_KINDS["never"]) + ["nonesuch.kind"])
    with pytest.raises(Unspecified, match="nonesuch.kind"):
        _check_strife_kinds({n: set(v) for n, v in bad.items()}, EVENT_KINDS)


def test_import_check_refuses_a_kind_in_two_lists():
    bad = _planted(never=sorted(R.STRIFE_KINDS["never"]) + ["field.won"])   # field.won is in `opens`
    with pytest.raises(Unspecified, match="field.won"):
        _check_strife_kinds({n: set(v) for n, v in bad.items()}, EVENT_KINDS)


def test_import_check_refuses_a_concludes_kind_outside_opens_and_joins():
    bad = _planted(concludes=sorted(R.STRIFE_KINDS["concludes"]) + ["news.told"])   # news.told is `never`
    with pytest.raises(Unspecified, match="news.told"):
        _check_strife_kinds({n: set(v) for n, v in bad.items()}, EVENT_KINDS)


def test_loader_refuses_a_malformed_block():
    base = {n: sorted(R.STRIFE_KINDS[n]) for n in LISTS}
    with pytest.raises(Unspecified):
        R._load_strife_kinds({**base, "extra": ["field.won"]})                                  # a list nobody reads
    with pytest.raises(Unspecified):
        R._load_strife_kinds({k: v for k, v in base.items() if k != "never"})                   # a decision nobody made
    with pytest.raises(Unspecified):
        R._load_strife_kinds({**base, "never": []})                                             # empty is not absent-but-fine
    with pytest.raises(Unspecified):
        R._load_strife_kinds({**base, "opens": base["opens"] + [base["opens"][0]]})             # a kind twice in one list


def test_every_registry_kind_is_in_exactly_one_of_opens_joins_never():
    registry = {k for r in data.MOVES for k in r["kinds"]}
    assert len(registry) >= 40     # the control: a registry that read empty would pass the loop below
    checked = 0
    for k in sorted(registry):
        homes = [n for n in DECIDED if k in R.STRIFE_KINDS[n]]
        assert len(homes) == 1, f"{k} is in {homes or 'none of'} opens/joins/never"
        checked += 1
    assert checked == len(registry)


def test_a_registry_kind_in_none_of_the_three_lists_is_seen():
    # FALSIFIER of the test above: strike one registry kind from its list and the same reading finds the hole.
    registry = {k for r in data.MOVES for k in r["kinds"]}
    struck = {n: set(R.STRIFE_KINDS[n]) - {"tenure.opened"} for n in LISTS}
    homes = [k for k in registry if not any(k in struck[n] for n in DECIDED)]
    assert homes == ["tenure.opened"]


def test_concludes_equals_the_rule_derived_over_the_registry():
    lists = {n: R.STRIFE_KINDS[n] for n in LISTS}
    derived = derive_concludes(data.MOVES, lists)
    assert derived and derived == R.STRIFE_KINDS["concludes"], (
        f"only in the derivation: {sorted(derived - R.STRIFE_KINDS['concludes'])}; "
        f"only in rosters.yaml: {sorted(R.STRIFE_KINDS['concludes'] - derived)}")


def test_the_kinds_whose_code_never_ends_a_case_do_not_conclude():
    # The reasons the entry names: AM (pardon refused), WR (a rebel assault repulsed), BR, VI.
    for k in ("detention.ended", "ban.ended", "field.won", "field.lost", "tenure.closed", "requisition.taken"):
        assert k not in R.STRIFE_KINDS["concludes"], k


def test_mutation_requisition_taken_in_concludes_passes_the_import_check_and_fails_the_derivation():
    mutated = {n: frozenset(v) for n, v in _planted(
        concludes=sorted(R.STRIFE_KINDS["concludes"]) + ["requisition.taken"]).items()}
    _check_strife_kinds(mutated, EVENT_KINDS)           # in `opens`, so the loader's check cannot see it
    derived = derive_concludes(data.MOVES, mutated)
    assert derived != mutated["concludes"]
    assert mutated["concludes"] - derived == {"requisition.taken"}     # VI never ends a case


def test_foreign_factions_live_in_the_roster_and_not_the_harness_file():
    assert R.FOREIGN_FACTIONS == frozenset({"Altonia", "Schoenland"})
    rows, sigs, foreign = data.load_moves()
    assert foreign == frozenset(R.faction_prop_id(n) for n in R.FOREIGN_FACTIONS) == data.FOREIGN
    assert "foreign_factions" not in R.load_yaml(data.STRIFE_MOVES_YAML.read_text(encoding="utf-8"))
